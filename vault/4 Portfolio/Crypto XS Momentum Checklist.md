---
type: checklist
strategy: Crypto XS Momentum
date: 2026-10
verdict: Portfolio 1 paper · Portfolio 2 enter at half weight
---

# Portfolio Checklist : Crypto XS Momentum

> **Question** : does this strategy deserve to enter the book?
> **Rule** : Sharpe(strategy) > Correlation(strategy, book) × Sharpe(book)

Strategy sheet: [[Crypto XS Momentum]] · Notebook 03, sections 2 to 6 · Daily returns 2021-06 to 2026-08, equal risk weights.

## The rule, against two books
| | Portfolio 1 (Carry, Momentum, Low vol) | Portfolio 2 (Carry, Low vol) |
| --- | --- | --- |
| Sharpe of the strategy (net) | 0.74 (0.56 after haircut) | 0.74 (0.56 after haircut) |
| Sharpe of the book | 1.61 | 1.07 |
| Correlation to the book (full sample) | 0.20 | −0.12 |
| Correlation in the book's worst 25 % months | 0.15 (strategy −0.50 %/month) | −0.24 (strategy +2.35 %/month) |
| Threshold = corr × Sharpe(book) | 0.32 | −0.13 |
| **Passes?** | yes | yes |
| Book Sharpe with it, equal risk weight | 1.61 → 1.61 | 1.07 → 1.38 |
| **Block bootstrap: book improves in** | **62 % of histories** | **91 % of histories** |

Where the overlap is: correlation 0.42 with the Momentum strategy, 0.16 with Carry. The funding part does not look like the Carry strategy.

## Sanity checks
- [x] Pass 2 of the sheet is complete
- [x] Kill criterion written before the test; the strategy passes it (Sharpe 0.74 > 0.3, top 5 names 69 %, turnover 32)
- [x] Still works without its best days : Sharpe 0.32 without the 10 best days
- [x] Loses where the sheet said it would (low dispersion months)
- [x] Turnover and costs realistic : 32 ×/yr, breakeven 47 bp, top 20 is liquid
- [x] Minimum capital available
- [x] Tries counted (9, about 1.8 independent), haircut applied (luck line 0.18)
- [x] Suffers in different conditions from the rest of the book : yes for Portfolio 2, partly not for Portfolio 1 (momentum overlap)

## Decision (2026-10)
- **Portfolio 1 : stays on paper.** Passes the bar, but 62 % (a coin flip), no gain at equal weight, loses in the book's bad months. Re-test every quarter.
- **Portfolio 2 : enter at half weight** (1/6 of risk, target 1/3, momentum family budget). Bootstrap at 91 %, above 90 % since mid-2026. Row in [[Strategy Table]], monitoring with the levels written there.
