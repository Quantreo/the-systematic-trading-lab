---
type: monitoring
strategy: 
review_frequency: monthly
started: {{date}}
---

# Live Monitoring : {{title}}

> **Question** : is the edge fading?
> **Method** : compare live to what the backtest promised, never live to zero. Several indicators, different speeds. Decide on written rules only.

Strategy sheet: [[ ]]

## A. Performance (slow)
| Indicator | Backtest reference | Live value | Status |
| --- | --- | --- | --- |
| Rolling 12-month Sharpe | 5th pct of backtest 12m Sharpes: | | green / amber / red |
| Current drawdown | Worst backtest DD: | | amber > 1.5×, red > 2× |
| CUSUM of live vs backtest mean | Alarm level (5 % false alarms on the backtest): | | red below the alarm |
| Monthly P&L vs backtest monthly distribution | | | |

## B. Mechanics (medium)
| Indicator | Backtest reference | Live value | Status |
| --- | --- | --- | --- |
| Hit rate | | | |
| Average gain / average loss | | | |
| Turnover (× per year) | | | |
| Realised costs and slippage (bps) | | | |

If mechanics are intact but costs doubled, the edge is not gone: the execution is the problem.

## C. Structure (fast, qualitative)
- [ ] Losing where Pass 1 said it would (expected), or where it should win (serious)?
- [ ] Are the conditions of the mechanism still there?
- [ ] Has the idea become consensus / crowded?
- [ ] Has the correlation to the book changed?

## Decision rules (written before going live)
| Level | Trigger | Action |
| --- | --- | --- |
| Watch | One slow alarm (CUSUM or rolling Sharpe), or one amber | Keep the size. Check B and C. Write it in the log. |
| Halve | Drawdown 1.5× the worst backtest DD, or one red | Halve the risk weight. Review every week. |
| Cut | Drawdown 2× the worst, two reds, or the exit criterion in [[Strategy Table]] hit | Exit. Log in [[Research Log]]. Park, do not delete. |

Never decide on a single bad month. Never decide without re-reading Pass 1.

## Review log
| Date | A | B | C | Level | Note |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
