"""
Rebuild data_fomc/dukascopy_fomc_minute.parquet from Dukascopy's public tick feed.

Only the FOMC windows are downloaded: for each scheduled announcement in
data_fomc/event_calendar.csv, from 25 hours before to 6 hours after, minute by minute.
That is about 117 windows x 31 hours x 6 pairs = ~22,000 small hourly files.

Usage (from the repository root):
    python data/get_fomc_minute.py
    python data/get_fomc_minute.py --compare data_fomc/old_file.parquet   # check against a previous file

Data source: Dukascopy Bank SA historical tick data (https://www.dukascopy.com).
The data is downloaded by you, for your own use, under Dukascopy's terms. It is not redistributed here.
"""
import argparse, io, lzma, struct, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pandas as pd
import requests

PAIRS = ["EURUSD", "GBPUSD", "AUDUSD", "NZDUSD", "USDCAD", "USDCHF"]   # the six legs used in the course
POINT = 1e5                                                           # price scale for these six pairs
URL = "https://datafeed.dukascopy.com/datafeed/{pair}/{y}/{m:02d}/{d:02d}/{h:02d}h_ticks.bi5"   # month is 0-based
BEFORE_H, AFTER_H = 25, 6
ROOT = Path(__file__).resolve().parent.parent
CALENDAR = ROOT / "data_fomc" / "event_calendar.csv"
OUT = ROOT / "data_fomc" / "dukascopy_fomc_minute.parquet"


def hours_to_fetch(end_utc):
    ev = pd.read_csv(CALENDAR)
    ev = ev[ev["event"] == "FOMC"].copy()
    ev["announce"] = pd.to_datetime(ev["announce_utc"], utc=True)
    ev = ev[ev["announce"] <= end_utc]
    hours = set()
    for a in ev["announce"]:
        start = a.floor("h") - pd.Timedelta(hours=BEFORE_H)
        for k in range(BEFORE_H + AFTER_H):
            hours.add(start + pd.Timedelta(hours=k))
    return sorted(hours), len(ev)


def parse_bi5(raw, hour_start):
    """One hourly tick file -> DataFrame(ts, bid, ask). Record: ms offset, ask, bid, ask vol, bid vol."""
    if not raw:
        return None
    data = lzma.decompress(raw)
    n = len(data) // 20
    rec = np.frombuffer(data[: n * 20], dtype=np.dtype([("ms", ">u4"), ("ask", ">u4"), ("bid", ">u4"), ("av", ">f4"), ("bv", ">f4")]))
    ts = hour_start + pd.to_timedelta(rec["ms"].astype("int64"), unit="ms")
    return pd.DataFrame({"ts": ts, "bid": rec["bid"] / POINT, "ask": rec["ask"] / POINT})


def to_minutes(ticks, pair):
    """Ticks -> one row per minute with ticks: bid and ask OHLC, and the number of ticks."""
    t = ticks.set_index(ticks["ts"].dt.floor("min"))
    g = t.groupby(level=0)
    out = pd.concat({"bid": g["bid"].agg(["first", "max", "min", "last"]), "ask": g["ask"].agg(["first", "max", "min", "last"])}, axis=1)
    out.columns = [f"{side}_{f}" for side, f in zip(["bid"] * 4 + ["ask"] * 4, ["open", "high", "low", "close"] * 2)]
    out["n_ticks"] = g.size().astype("int64")
    out.index.name = "ts_utc"
    out = out.reset_index()
    out.insert(0, "instrument", pair)
    return out


def fetch(session, pair, h, tries=5):
    url = URL.format(pair=pair, y=h.year, m=h.month - 1, d=h.day, h=h.hour)
    for k in range(tries):
        try:
            r = session.get(url, timeout=30)
            if r.status_code == 404:
                return pair, h, b""
            r.raise_for_status()
            return pair, h, r.content
        except requests.RequestException:
            time.sleep(1 + 2 * k)
    raise RuntimeError(f"failed after {tries} tries: {url}")


def compare(new, old_path):
    old = pd.read_parquet(old_path)
    old = old[old["instrument"].isin(new["instrument"].unique())]
    key = ["instrument", "ts_utc"]
    m = new.merge(old, on=key, how="outer", suffixes=("", "_old"), indicator=True)
    print(f"\nCompare with {old_path}: new {len(new):,} rows, old {len(old):,} rows, "
          f"only in new {int((m['_merge'] == 'left_only').sum()):,}, only in old {int((m['_merge'] == 'right_only').sum()):,}")
    both = m[m["_merge"] == "both"]
    for c in [c for c in new.columns if c not in key]:
        print(f"  {c:10s} max abs diff {np.nanmax(np.abs(both[c].to_numpy(float) - both[c + '_old'].to_numpy(float))):.2e}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--end", default="2026-09-16 23:59", help="last date to include (UTC)")
    ap.add_argument("--workers", type=int, default=12, help="parallel downloads; keep it moderate")
    ap.add_argument("--compare", help="an existing parquet file to compare with")
    args = ap.parse_args()

    hours, n_events = hours_to_fetch(pd.Timestamp(args.end, tz="UTC"))
    jobs = [(p, h) for p in PAIRS for h in hours]
    print(f"{n_events} FOMC windows, {len(hours)} hours x {len(PAIRS)} pairs = {len(jobs):,} files")
    t0, done, frames = time.time(), 0, {p: [] for p in PAIRS}
    with requests.Session() as s, ThreadPoolExecutor(args.workers) as ex:
        futs = [ex.submit(fetch, s, p, h) for p, h in jobs]
        for f in as_completed(futs):
            pair, h, raw = f.result()
            df = parse_bi5(raw, h)
            if df is not None and len(df):
                frames[pair].append(df)
            done += 1
            if done % 500 == 0 or done == len(jobs):
                el = time.time() - t0
                print(f"\r  {done:,}/{len(jobs):,} files, {el:,.0f} s elapsed, ~{el / done * (len(jobs) - done):,.0f} s left", end="", flush=True)
    print()
    out = pd.concat([to_minutes(pd.concat(frames[p]).sort_values("ts"), p) for p in PAIRS if frames[p]], ignore_index=True)
    out = out.sort_values(["instrument", "ts_utc"]).reset_index(drop=True)
    OUT.parent.mkdir(exist_ok=True)
    out.to_parquet(OUT)
    print(f"Saved {OUT} : {len(out):,} rows, {out['instrument'].nunique()} pairs, in {time.time() - t0:,.0f} s")
    if args.compare:
        compare(out, args.compare)


if __name__ == "__main__":
    main()
