---
type: strategy
name: Crypto XS Momentum
family: Trend (cross-sectional)
version: v2
status: testing
created: 2026-08
last_update: 2026-09
sharpe_net: 0.74 (top 20, point-in-time)
turnover: 32 × per year
corr_to_book: to measure
code: notebooks/02_crypto_xs_momentum.ipynb
data_snapshot: Binance USDT perps, daily, 2019-12-31 → 2026-08-24, 276 names
---

# Crypto XS Momentum

> **Status** : **TESTING**, paper at half weight, v2 (top 20). The course strategy: built brick by brick in Section 2, judged in Section 3. Register: [[_Index]]
> Reading note: [[Moskowitz Ooi Pedersen 2012 Time Series Momentum]] · Log: [[Research Log]] · Checklist: [[Crypto XS Momentum Checklist]]

---

## PASS 1 : the hypothesis (written before any test)

### 1.1 Mechanism
> Inside crypto, relative strength persists for weeks: retail flows chase recent winners and abandon recent losers, and information diffuses slowly across hundreds of small names. A long/short book captures that while neutralising the market bet, which in crypto is most of any long-only result.

### 1.2 Source and crowding
- **Source**: [[Moskowitz Ooi Pedersen 2012 Time Series Momentum]], derived on two bricks: universe (futures → crypto perps) and signal method (time-series → cross-sectional). An earlier attempt on 29 CME futures failed (Sharpe −0.61, turnover 152 ×/yr): logged in [[Research Log]].
- **Crowding**: momentum is the most published factor in finance; crypto cross-sectional momentum is documented since 2019 ([[Liu Tsyvinski Wu 2022 Crypto Risk Factors]]); the sizing chain follows [[Carver 2023 Advanced Futures Trading Strategies - trend chapters]]. Retail-heavy market: plausible that it persists longer than in equities.

### 1.3 Expected behaviour
- **Should work when**: dispersion across names is high (alt seasons, sector rotations), trends last weeks.
- **Should suffer when**: everything moves together (BTC-driven crashes and squeezes), sharp reversals of leadership, low dispersion.
- **Expected payoff profile**: many small losses, a few large gains; positive skew; a handful of days carry the year.
- **What it could secretly be**: **funding carry**. A demeaned book ends up short the high-funding names and collects it. Must be split out.

### 1.4 Universe (intended) and why
Top 20 Binance USDT perpetuals by trailing 30-day volume, **point-in-time**: at each date, the 20 largest among names listed ≥ 180 days, with an exit hysteresis (leave at rank > 25) so names do not flicker. Why 20, written before looking: beyond rank 20, names are smaller and noisier, and a 5 bp cost assumption stops being realistic.
Survivorship is **measured**, not declared: the same code on today's top 20 applied to the past is the control.

### 1.5 Horizon, trade count, data
- **Holding period**: days to weeks (three speeds: 7, 30, 90 days).
- **Expected trades per year**: continuous; turnover target below 50 × per year.
- **Enough observations?** ~1,900 daily observations × 20 names since mid-2021. Fine for the signal, short for regimes (one cycle).
- **Data**: daily close, funding, quote volume for all perps ever listed (to rebuild membership). Gaps: pre-2021 is thin; some tickers were recycled (a token relisted under an old name).

### 1.6 Instrument traps
- Funding: separate price P&L from funding P&L.
- Costs: 5 bp one way assumed; the tail of the universe is worse.
- Survivorship: see 1.4. Membership must use volume known at the date.
- Look-ahead in FDM/IDM warm-up: no back-filling of multipliers for names listed mid-sample (a real bug found and fixed: the leak was the same size as the signal).

### 1.7 Kill criterion : for the backtest (written before the result)
> Net Sharpe below 0.3 on the point-in-time universe; or a 95 % bootstrap interval containing zero **and** a P&L made by fewer than 5 names; or turnover above 60 × per year at 5 bp.
> Out of sample vs in sample: the three-zone rule. The in-sample (2020-07 → 2022) is short and covers one bad regime, so the regime table (2.6) is the real check.

### 1.8 Exit criterion : for live (written before going live)
> Drawdown of the vol-targeted equity beyond 1.5 × the worst backtest drawdown. Or twelve months of negative returns while dispersion is high: the mechanism is there and the strategy is not catching it.

### 1.9 Test plan (written before)
- **Sample**: 2020-07 → 2026-08.
- **IS / OOS split**: 2023-01-01, fixed before any analysis.
- **Variants planned**: buffer {0, 5, 10, 20 %}; cost {1, 5, 10, 20 bp}; frozen vs point-in-time universe. (Research version also swept horizons, smoothing and the neutralisation ladder: see Research Log.)
- **Cost assumption**: 5 bp one way.

---

## PASS 2 : what I measured (top 20, point-in-time, capital-neutral)

### 2.0 Implementation
- **Code**: `notebooks/02_crypto_xs_momentum.ipynb` (course version, ~180 lines). Research version: `07_momentum_crypto_xs.ipynb`.
- **Data snapshot**: Binance perps daily, 450 names with prices, 832 with volume, 2019-12-31 → 2026-08-24.
- **Run date**: 2026-09-26.

### 2.1 Signal retained
Vol-adjusted daily returns (r / EWMA σ), summed over 7, 30 and 90 days (skip today's bar), each smoothed by an EMA of span h/4, divided by √h, averaged into one score × FDM (1.37, from the average correlation 0.30 between speeds). Demeaned across the universe weighted by w/σ, scaled to avg |f| = 10 on the past only, capped ±20 and re-centred, so that the sum of positions is zero.

### 2.2 Universe retained
Top 20 point-in-time: 176 names seen, 20 held at a time. Frozen control: today's 20, only 12 held per day before 2024.

### 2.3 Sizing and risk
- **Position sizing**: inverse vol, 1/n over live names, IDM measured on past years only, capped at √20 (first year at 1).
- **Strategy vol target**: 20 % (realised 17.8 %).
- **Rebalancing**: daily, position buffer 10 %.
- **Minimum capital**: 20 names × minimum ticket; realistically 10-30 k USD.

### 2.4 Diagnostic
| Metric | Point-in-time (honest) | Frozen (today's 20, control) |
| --- | --- | --- |
| Sharpe net | **0.74** | 0.82 |
| t-stat | 1.69 | 1.87 |
| CAGR / vol | 12.4 % / 17.8 % | 14.1 % / 18.0 % |
| Max drawdown | −22.8 % | −18.9 % |
| Turnover | 32 × / yr | 34 |
| Breakeven cost | 47 bp | 49 |
| P&L: price / funding / costs (% total) | +53 / +24 / −8 | +83 / +2 / −9 |
| By year (%) | 2021 +4, 2022 −6, 2023 +16, 2024 +23, 2025 +23, 2026 +9 | |
| Positive months | 57 % ; worst −9.2 %, best +12.9 % | |
| Bootstrap 5-95 % : Sharpe / vol / max DD | 0.19-1.52 / 16-20 % / −14 to −33 % | |

Five years of data, of which two (2024-2025) carry the result. That is what a t-stat of 1.7 means: promising, not proven.

### 2.5 Contribution by asset and by day
Top 5 names = 69 % of P&L (SUI, SIREN, BTC, LAB, SOL). Top 10 days = 60 % of P&L; without them, Sharpe 0.32. 36 % of the P&L comes from names no longer in today's top 20, which the frozen universe cannot hold. Concentrated, as a convex strategy is; not dominated by one name.

### 2.6 Behaviour by regime vs expected
| Regime | Expected (1.3) | Observed | Match? |
| --- | --- | --- | --- |
| High dispersion months (37) | positive | +1.8 % per month, 68 % positive | yes |
| Low dispersion months (44) | flat or negative | +0.4 % per month, 47 % positive | yes |
| 2022, BTC-driven, liquidation cascades (Luna, FTX) | should suffer: everything moves together, V-shaped reversals | −6 % | yes |
| 2024-2025, sector rotations (memes, SOL, AI) | should work | +23 %, +23 % | yes |
| 2021 | | flat: IDM at 1 the first year, book at reduced vol | mechanical |

It loses where the mechanism is absent and wins where it is present. That is the behaviour we wanted, and it gives 2024-2025 more weight than the raw Sharpe does.

### 2.7 Variants tested
- **Variants tested**: 9 in the course notebook (buffer × 4, cost × 4, frozen control), more in the research version (see [[Research Log]]).
- **Haircut**: expected max Sharpe by luck with 9 trials on 5 years ≈ 0.9. 0.74 is below it. But the universe width was argued before the test and the regime behaviour matches the hypothesis, which counts for more than the sweep.

### 2.8 Known weaknesses
- Two years out of five carry the result. Five years of crypto is one cycle.
- A third of the P&L is funding collected, not momentum: correlation with a funding-carry sleeve on the same universe will be material (+0.44 monthly in the research version).
- Cost sensitivity: Sharpe 0.82 / 0.74 / 0.66 / 0.48 at 1 / 5 / 10 / 20 bp.
- Buffer: 0.70 / 0.74 / 0.74 / 0.77 at 0 / 5 / 10 / 20 %, turnover 46 → 25. Monotone up to the degenerate point; 10 % kept.

### 2.9 What I did not test
- Realistic per-name costs (spread × depth) instead of a flat 5 bp.
- Momentum net of the funding sleeve (residual after regressing on carry).
- Beta neutrality (the course version is capital-neutral; the research version adds beta weighting, which costs ~0.1 Sharpe).
- Anything intraday.

### 2.10 Verdict
- [ ] Keep
- [ ] Kill
- [x] **Keep, paper at half weight** : above the kill line on every criterion (Sharpe 0.74 > 0.3, top 5 names < 100 %, turnover 32 < 60), regime behaviour matches Pass 1. Not proven: t = 1.7, two years carry the result. Enters the [[Strategy Table]] at half weight, judged against the book in Section 3.

**Decided on**: 2026-09   **Next review**: 2026-12

---

## Changelog
| Version | Date | What changed | Why |
| --- | --- | --- | --- |
| v0 | 2026-08 | XS momentum on 29 CME futures | first attempt, killed (Sharpe −0.61, turnover 152 ×) |
| v1 | 2026-08 | crypto perps point-in-time, three speeds, EMA smoothing, demeaned book | the two fixes noted at v0's post-mortem, tested where the cut is wide enough |
| v1 | 2026-09 | data fixes: causal universe age per listing episode, no FDM back-fill | look-ahead found in the multiplier warm-up |
| v2 | 2026-09 | top 20 ; capital-neutral ; course notebook | beyond rank 20, names are small, noisy, costly ; simpler chain for the course |
