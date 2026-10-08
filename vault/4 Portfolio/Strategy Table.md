---
type: portfolio
book_vol_target: 10%
---

# Strategy Table : the book

> **What this is** : the object you actually trade. One row per strategy, weights in **risk**, exit criteria written the day it enters.
> **Open it** : at every monthly portfolio slot, and the day a strategy enters or leaves.

Book shown: **Portfolio 2** of notebook 03, after the decision of lesson 3.2.

| Strategy | Family | Status | Sharpe net | Corr. to rest of book | Risk weight now | Target | Entered | Exit criterion | Next review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Carry | Carry | live | from its sheet | −0.38 with Low vol | 1/3 | 1/3 | 2026-09 | from its sheet | monthly |
| Low vol | Low vol | live | from its sheet | −0.38 with Carry | 1/3 | 1/3 | 2026-09 | from its sheet | monthly |
| [[Crypto XS Momentum]] | Momentum (XS) | **half weight** | 0.74 | −0.12 to the book | 1/6 | 1/3 | 2026-10 | Watch: 12m Sharpe < −0.76 or CUSUM alarm. Halve: DD −34 % (1.5× worst). Cut: DD −46 % (2×) | 2027-04 (full weight if all green) |
| [[FOMC Drift]] | Event-driven | **cut 2025-10-29** | 0.78 → negative | ≈ 0 | 0 | 0 | 2024-07 | DD of 10 %-vol equity < −20 % (fired) | closed |

Weights are in risk. The book is then scaled to its 10 % target by the IDM (2.14 at target weights for these three strategies).

## Rules of the book
1. **Enter small, then scale.** A new strategy starts at half its target risk weight. It reaches target after at least 6 months live (execution check: fills, costs, slippage), all tests of lesson 3.5 green, and losses that look like its backtest losses. One check missing: stay at half, look again in 3 months.
2. **Exit on a written criterion, not on feeling.** The exit criterion is the live mirror of the Pass 1 kill criterion. Write it the day the strategy enters: worst backtest drawdown × 1.5 halve, × 2 cut.
3. **Equal risk weights** between strategies, **one budget per family**: two strategies of the same family share it. Fine optimisation on a handful of strategies does more harm than good (notebook 03, section 8: fitted 1.15 → unseen 1.66, against 0.93 → 2.08 for equal weights).
4. **Correlations can rise in a crisis.** Check the bad-day correlation, not only the average. This book: −0.17 on all days, −0.36 on its worst 10 % of days. Measured every month.
5. **Book-level limits**: IDM capped at **2.5** (now 2.14). Book loss limit **−14 %** (1.5× the worst book drawdown, −9.1 %): every strategy halved. Vol target of the book: 10 % (frontmatter). Strategies run at 15-20 % each so that a decorrelated book lands near 10 %.

Related: [[Portfolio Checklist Template]] · [[Live Monitoring Template]] · [[Research Log]]
