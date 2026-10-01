"""
Rebuild the crypto data of the course from Binance's public dataset (data.binance.vision):
    data_trend/prices_funding.parquet   daily close, funding (sum of the day) and quote volume, 450 perps
    data_trend/volume_all_perps.parquet daily quote volume of every USDT perp in perp_meta.csv (832 names),
                                        dead ones included: this is what makes a point-in-time universe possible

It downloads one small monthly file per symbol and per month: about 40,000 files in total.

Usage (from the repository root):
    python data/get_crypto_daily.py
    python data/get_crypto_daily.py --compare-dir old_data_trend     # check against previous files

Data source: Binance Vision public datasets (https://data.binance.vision), licensed CC BY-NC-SA 4.0 under the
Binance Vision Dataset Terms. You download it yourself, for your own non-commercial research and backtesting.
It is not redistributed here.
"""
import argparse, io, re, time, zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pandas as pd
import requests

BASE = "https://data.binance.vision/"
LIST = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?delimiter=/&prefix={prefix}"
KLINES = "data/futures/um/monthly/klines/{s}/1d/"
FUNDING = "data/futures/um/monthly/fundingRate/{s}/"
ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "data_trend"
PRICE_START, VOLUME_START = "2019-12-31", "2020-01-01"


def get(session, url, tries=5):
    for k in range(tries):
        try:
            r = session.get(url, timeout=30)
            if r.status_code == 404:
                return None
            r.raise_for_status()
            return r
        except requests.RequestException:
            time.sleep(1 + 2 * k)
    raise RuntimeError(f"failed after {tries} tries: {url}")


def list_files(session, prefix):
    """All .zip keys under a prefix (the listing is paginated by 1000)."""
    keys, marker = [], ""
    while True:
        r = get(session, LIST.format(prefix=prefix) + (f"&marker={marker}" if marker else ""))
        if r is None:
            return keys
        found = re.findall(r"<Key>([^<]+\.zip)</Key>", r.text)
        keys += found
        if "<IsTruncated>true</IsTruncated>" not in r.text or not found:
            return keys
        marker = found[-1]


def read_zip_csv(content, names):
    with zipfile.ZipFile(io.BytesIO(content)) as z:
        raw = z.read(z.namelist()[0]).decode()
    first = raw.split("\n", 1)[0].split(",")[0]
    skip = 0 if first.strip().lstrip("-").isdigit() else 1          # newer files carry a header row
    return pd.read_csv(io.StringIO(raw), header=None, skiprows=skip, names=names)


def to_utc_ms(x):
    x = pd.to_numeric(x)
    return pd.to_datetime(np.where(x > 1e14, x // 1000, x), unit="ms", utc=True)   # some files use microseconds


def klines(content):
    df = read_zip_csv(content, ["open_time", "open", "high", "low", "close", "volume", "close_time", "quote_volume",
                                "count", "taker_buy_volume", "taker_buy_quote_volume", "ignore"])
    return pd.DataFrame({"date": to_utc_ms(df["open_time"]).tz_localize(None).normalize(),
                         "close": df["close"].astype(float), "quote_volume": df["quote_volume"].astype(float)})


def funding(content):
    df = read_zip_csv(content, ["calc_time", "funding_interval_hours", "last_funding_rate"])
    d = pd.DataFrame({"date": to_utc_ms(df["calc_time"]).tz_localize(None).normalize(), "rate": df["last_funding_rate"].astype(float)})
    return d.groupby("date")["rate"].sum()


def run(session, jobs, parse, workers, label):
    t0, out, n = time.time(), {}, len(jobs)
    with ThreadPoolExecutor(workers) as ex:
        futs = {ex.submit(get, session, BASE + key): (sym, key) for sym, key in jobs}
        for i, f in enumerate(as_completed(futs), 1):
            sym, _ = futs[f]
            r = f.result()
            if r is not None:
                out.setdefault(sym, []).append(parse(r.content))
            if i % 500 == 0 or i == n:
                el = time.time() - t0
                print(f"\r  {label}: {i:,}/{n:,} files, {el:,.0f} s, ~{el / i * (n - i):,.0f} s left", end="", flush=True)
    print()
    return out


def compare(new, old, name, key):
    m = new.merge(old, on=key, how="outer", suffixes=("", "_old"), indicator=True)
    print(f"  {name}: new {len(new):,} rows, old {len(old):,}, only new {int((m['_merge'] == 'left_only').sum()):,}, "
          f"only old {int((m['_merge'] == 'right_only').sum()):,}")
    b = m[m["_merge"] == "both"]
    for c in [c for c in new.columns if c not in key]:
        a, o = b[c].to_numpy(float), b[c + "_old"].to_numpy(float)
        print(f"    {c:14s} max relative diff {np.nanmax(np.abs(a - o) / np.maximum(np.abs(o), 1e-12)):.2e}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--end", default="2026-08-24")
    ap.add_argument("--workers", type=int, default=12, help="parallel downloads; keep it moderate (Binance rate limits)")
    ap.add_argument("--compare-dir", help="a folder holding the previous prices_funding.parquet and volume_all_perps.parquet")
    args = ap.parse_args()
    end = pd.Timestamp(args.end)
    all_syms = pd.read_csv(DIR / "perp_meta.csv")["symbol"].tolist()
    price_syms = pd.read_csv(DIR / "symbols_prices.csv")["symbol"].tolist()
    t0 = time.time()

    with requests.Session() as s:
        print(f"Listing files for {len(all_syms)} symbols ...")
        with ThreadPoolExecutor(args.workers) as ex:
            k_keys = dict(zip(all_syms, ex.map(lambda x: list_files(s, KLINES.format(s=x)), all_syms)))
            f_keys = dict(zip(price_syms, ex.map(lambda x: list_files(s, FUNDING.format(s=x)), price_syms)))
        month = lambda key: pd.Timestamp(key[-11:-4] + "-01")
        k_jobs = [(x, k) for x, ks in k_keys.items() for k in ks if pd.Timestamp("2019-12-01") <= month(k) <= end]
        f_jobs = [(x, k) for x, ks in f_keys.items() for k in ks if pd.Timestamp("2019-12-01") <= month(k) <= end]
        K = run(s, k_jobs, klines, args.workers, "klines ")
        F = run(s, f_jobs, funding, args.workers, "funding")

    kl = pd.concat([pd.concat(v).assign(symbol=x) for x, v in K.items()], ignore_index=True)
    kl = kl.drop_duplicates(["symbol", "date"], keep="last")
    vol = kl.pivot(index="date", columns="symbol", values="quote_volume").sort_index()
    vol = vol.loc[VOLUME_START:end].reindex(columns=sorted(vol.columns))
    vol.columns.name, vol.index.name = "symbol", "date"

    fund = pd.concat({x: pd.concat(v).groupby(level=0).sum() for x, v in F.items()}, names=["symbol", "date"]).rename("funding_rate").reset_index()
    px = kl[kl["symbol"].isin(price_syms)].merge(fund, on=["symbol", "date"], how="left")
    px["funding_rate"] = px["funding_rate"].fillna(0.0)
    px = px[(px["date"] >= PRICE_START) & (px["date"] <= end)].dropna(subset=["close"])
    px = px[["date", "symbol", "close", "funding_rate", "quote_volume"]].sort_values(["date", "symbol"]).reset_index(drop=True)

    px.to_parquet(DIR / "prices_funding.parquet")
    vol.to_parquet(DIR / "volume_all_perps.parquet")
    print(f"Saved prices_funding ({len(px):,} rows, {px['symbol'].nunique()} names) and volume_all_perps "
          f"({vol.shape[0]} days x {vol.shape[1]} names) in {time.time() - t0:,.0f} s")

    if args.compare_dir:
        d = Path(args.compare_dir)
        compare(px, pd.read_parquet(d / "prices_funding.parquet"), "prices_funding", ["date", "symbol"])
        ov = pd.read_parquet(d / "volume_all_perps.parquet").stack().rename("quote_volume").reset_index()
        compare(vol.stack().rename("quote_volume").reset_index(), ov, "volume_all_perps", ["date", "symbol"])


if __name__ == "__main__":
    main()
