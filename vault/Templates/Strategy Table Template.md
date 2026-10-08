---
type: portfolio
book_vol_target: 10%
---

# Strategy Table : {{title}}

> **What this is** : the book you actually trade. One row per strategy, weights in **risk**, risk rules written the day a strategy enters.
> **Open it** : at every monthly portfolio slot, and the day a strategy enters or leaves.
> **Example** : [[Strategy Table]]

## Strategies

| Strategy | Family | Status | Risk weight now | Target | Entered | Halve at (DD) | Cut at (DD) | Next review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | paper / half / full / cut |  |  |  | worst DD × 1.5 | worst DD × 2 | entry + 6 months |

## Risk rules of each strategy

- **Entry** : half weight for the first 6 months.
- **Full weight** : after 6 months, if the tests of lesson 3.5 are green and its losses look like its backtest losses.
- **Halve** : drawdown below worst backtest drawdown × 1.5.
- **Cut** : drawdown below worst backtest drawdown × 2.
- **Watch** : rolling 12-month Sharpe below the backtest 5th percentile, or CUSUM alarm.

## Risk rules of the book

| Rule | Level | Now | Last checked |
| --- | --- | --- | --- |
| Vol target | 10 % |  |  |
| IDM cap | 2.5 |  |  |
| Loss limit (everything halved) | worst book DD × 1.5 =  |  |  |
| Bad-day correlation | measured, not assumed | all days:  · worst 10 %:  |  |

Related: [[Portfolio Checklist Template]] · [[Live Monitoring Template]]
