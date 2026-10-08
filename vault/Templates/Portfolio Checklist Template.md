---
type: checklist
strategy: 
date: {{date}}
verdict: 
---

# Portfolio Checklist : {{title}}

> **Question** : does this strategy deserve to enter the book?
> **Rule** : Sharpe(strategy) > Correlation(strategy, book) × Sharpe(book)

Strategy sheet: [[ ]]

## The rule
| | Value |
| --- | --- |
| Sharpe of the strategy (net, after haircut) | |
| Sharpe of the current book | |
| Correlation to the book (full sample) | |
| Correlation to the book **in the book's worst 25 % months** | |
| Threshold = corr × Sharpe(book) | |
| **Passes?** | yes / no |
| Book Sharpe with it, equal risk weight | before → after |
| **Block bootstrap**: share of rewritten histories where the book improves | |

## Sanity checks
- [ ] Pass 2 of the sheet is complete
- [ ] Kill criterion was written before the test, and the strategy passed it
- [ ] Still works without its top 2 assets
- [ ] Loses where the sheet said it would (regime table matches)
- [ ] Turnover and costs realistic for my execution
- [ ] Minimum capital available
- [ ] Variants counted in [[Research Log]], haircut applied
- [ ] Suffers in **different** conditions from what is already in the book

## Decision
Bootstrap **≥ 90 %**: enter. **60 to 90 %**: stay on paper, re-test every quarter. **Below 60 %**: reject. Measured at the decision date, past data only (notebook 03, sections 3 to 6).

- **Enter** at half target weight, review after N months → row in [[Strategy Table]], create a [[Live Monitoring Template|Live Monitoring]] note
- **Wait** : what is missing → 
- **Reject** : reason → 
