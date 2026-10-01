---
type: log
---

# Research Log

> **What this is** : one line per variant you actually ran, grouped by strategy. The count tells you how much to discount your best Sharpe.
> **Open it** : during every test slot, after every run. Not at the end of the day: after every run.
> **Rule** : a variant you ran and forgot still counts. Write it while the cell is executing.

**How it is organised** : one section per strategy, newest strategy first. Inside a section, runs in the order you ran them: read top to bottom, it is the story of the research. The count at the top of each section feeds box 2.7 of the strategy sheet.

**Line format** : `date · what changed → result · verdict`

**Verdicts** : baseline · step · insight · dropped · retained · control · logged

---

## [[Crypto XS Momentum]]

> **Count** : about 9 design tries (choices made on a result), plus the research runs below. Cost sensitivity, buffer and frozen control are stress tests, not counted. Measured correlation between rebuildable tries 0.85; counted cautiously at 0.5, that is 1.8 independent tries. Luck line 0.18 (0.67 if they were independent), haircut Sharpe 0.56. 0.74 beats luck with about 90 % probability. The main doubt is the 5.2-year sample: keep on paper.

**Research runs (August 2026, before the course chain)**
- 2026-08 · XS momentum on 29 CME futures → Sharpe −0.61, turnover 152/yr. Two or three contracts per class: ranking them is a spread, not a cut · **dropped**
- 2026-08 · Crypto perps point-in-time, speeds 7/30/90, no smoothing, directional (no demean) → Sharpe −0.08, turnover 13/yr. Directional momentum does not pay in crypto · **dropped**
- 2026-08 · + simple demean → Sharpe 0.34, turnover 40/yr. The forecasts sum to zero, the positions do not · **step**
- 2026-08 · + demean weighted by 1/σ → Sharpe 0.52, turnover 41/yr. Net exposure down to 10 % of gross · **step**
- 2026-08 · + re-centre after the cap → Sharpe 0.54. Capital-neutral · **step**
- 2026-08 · + beta weighting → Sharpe 0.43. Beta close to zero; kept in the research version on the argument, not on the Sharpe · **retained (research)**
- 2026-08 · Horizons 14/60/180 → Sharpe 0.62. Best cell of the sweep · **noted, not adopted**
- 2026-08 · Horizons 3/14/60 → Sharpe 0.66, turnover 73/yr. Too much turnover · **dropped**
- 2026-08 · 7 days only, with / without smoothing → 0.31 / 0.09. Smoothing helps the fast speed · **insight**
- 2026-08 · 90 days only, with / without smoothing → −0.10 / 0.21. Smoothing hurts the slow speed · **insight**

**Course chain (September 2026, notebook 02)**
- 2026-09 · Top 20 point-in-time, capital-neutral, buffer 10 %, 5 bp → Sharpe **0.74**, t 1.69, turnover 32/yr. Width argued before the test · **retained**
- 2026-09 · Buffer 0 / 5 / 20 % → Sharpe 0.70 / 0.74 / 0.77, turnover 46 / 37 / 25. Monotone, 10 % kept · **logged**
- 2026-09 · Cost 1 / 10 / 20 bp → Sharpe 0.82 / 0.66 / 0.48. Costs are the sensitive input · **logged**
- 2026-09 · Frozen top 20 (today's list on the past) → Sharpe 0.82. Price P&L 83 % against 53 % for the honest universe · **control**

---

## [[FOMC Drift]]

> **Count** : 6 variants. Best net Sharpe 0.78. Luck line with 6 independent trials on 14 years: about 0.35. Above the luck line in the backtest; killed live by the exit criterion.

- 2024-06 · EUR/USD alone, exit at the announcement, mid prices, 1 bp cost → Sharpe 0.7, +12 bp per trade, t 3.3 (2012-2025) · **baseline**
- 2024-06 · 12 h window instead of 24 h → lower. The drift is spread over the 24 h · **dropped**
- 2024-06 · 48 h window → lower, noisier · **dropped**
- 2026-09 · EUR/USD, real bid/ask, exit 5 min before → +8.3 bp, t 2.6 on the full sample · **control**
- 2026-09 · 6-leg short-USD basket, bid/ask, exit 5 min before → Sharpe 0.78, +7.7 bp, t 2.8. 2025-26: −18.5 bp · **retained, then killed**
- 2026-09 · Stops written in 2024, replayed point-in-time → the −20 % drawdown stop fires on 2025-10-29; the rolling stops never fire · **kill confirmed**

---

## The luck line behind the count
Expected best Sharpe of N strategies with no edge, over T years (Bailey and López de Prado), with N the number of independent tries: N_eff = N ÷ (1 + (N − 1) × ρ). Haircut Sharpe = Sharpe − luck line. Details in [[Deflated Sharpe]].
