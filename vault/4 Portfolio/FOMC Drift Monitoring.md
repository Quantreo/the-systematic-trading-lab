---
type: monitoring
strategy: FOMC Drift
review_frequency: after each meeting
started: 2024-07
---

# Live Monitoring : FOMC Drift

> **Question** : is the edge fading?
> **What happened** : yes, and the pre-registered drawdown stop caught it on 2025-10-29. The two rolling stops never fired. This note is the worked example for lesson 3.5.

Strategy sheet: [[FOMC Drift]]

## A. Performance (slow)
| Indicator | Backtest reference | Live value (2025-10) | Status |
| --- | --- | --- | --- |
| Rolling 24-trade Sharpe | > 0 in every window 2012-2024 | still positive (window contains 2022-2024) | green (too slow) |
| Rolling 24-trade cumulative return | > 0 | still positive | green (too slow) |
| Drawdown of 10 %-vol equity | worst 2012-2024 −13.0 % | **−20 % → −29.5 %** | **red** |
| CUSUM of trades vs backtest mean | alarm −5.0 (5 % false alarms) | **−5.9 on 2025-07-30**, −11.8 by 2026-09 | **red first** |
| Mean per trade, last 8 | +10 bp | **−26 bp** | red |

## B. Mechanics (medium)
| Indicator | Backtest reference | Live value | Status |
| --- | --- | --- | --- |
| Hit rate | 57-64 % | **14 %** over 14 trades | red |
| Average gain / loss | small, symmetric | losses 2-5× the historical gain | red |
| Spread paid | as modelled | as modelled | green : not an execution problem |

## C. Structure (fast, qualitative)
- [x] Losing where Pass 1 said it would? **No.** Pass 1 said "suffers when the outcome is fully priced". 2025 meetings were not all fully priced, and the USD was bid into almost every one. The mechanism no longer describes the market.
- [x] Conditions of the mechanism still there? Unknown. Rates, positioning, vol conditioning checked: no reliable relation. **The edge died without an explanation.**
- [ ] Crowded? Possibly (the equity version was published in 2011 and widely traded).
- [x] Correlation to the book changed? Not relevant, event-based.

## Decision rules (written 2024-07, before going live)
| Level | Trigger | Action |
| --- | --- | --- |
| Watch | all green | continue |
| Reduce | one red | halve size |
| Cut | DD < −20 %, or two reds | exit, log, park |

## Review log
| Date | A | B | C | Level | Note |
| --- | --- | --- | --- | --- | --- |
| 2025-03 | amber | amber | ? | watch | one bad meeting, −54 bp |
| 2025-07 | **red (CUSUM)** | red | ? | **watch** | CUSUM alarm: five meetings out of five below the backtest mean |
| 2025-09 | red | red | ? | **halve** | DD −20.0 %, past 1.5× the worst backtest DD |
| 2025-10-29 | **red** | red | no mechanism | **cut** | DD stop hit. 7 trades after the cut, 6 losers, −14.3 bp average: another −11.6 % of capital avoided. Cutting was right. |

## Lesson
The slow indicators (24-trade windows) would have kept us in for another two years. The CUSUM saw the leak first (July), the drawdown confirmed it (September), the stop written before going live cut it (October). Use several indicators of different speeds, and let the fastest one that is not noise decide.
