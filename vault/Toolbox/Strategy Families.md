---
type: reference
updated: 2026-09-30
---

# Strategy Families

> **What this is** : the map. Seven families, the same six questions for each.
> **Open it** : every time you meet a strategy, to find its family in 30 seconds; and when you fill box 1.3 of a strategy sheet.

**The question behind every family: who pays me, and why?**

Each family below answers the same six questions: who pays, when it works, when it breaks, what the P&L feels like, what a naive backtest forgets, and where to read more. Same questions every time, so any paper or strategy you see online can be classified in 30 seconds.

Two families are built end to end in the course: **trend** (Crypto XS Momentum) and **event-driven** (FOMC Drift). Carry is described as the mirror image of trend.

---

## Trend
- **Who pays** : prices under-react to information, then flows chase them. Risk-management rules that cut positions as prices fall push them further; herding does the rest.
- **Works when** : long, sustained moves (2022 in rates and energy, 2014 in the dollar, 2020 in the crash).
- **Breaks when** : choppy ranges, sharp V-shaped reversals (2023).
- **Payoff** : many small losses, a few large gains. Positive skew.
- **Instrument traps** : roll yield on futures, funding on perps, survivorship in crypto universes.
- **Read** : [[Moskowitz Ooi Pedersen 2012 Time Series Momentum]] · Hurst, Ooi, Pedersen, *A Century of Evidence on Trend-Following Investing* · [[Carver 2023 Advanced Futures Trading Strategies - trend chapters]] · [[Liu Tsyvinski Wu 2022 Crypto Risk Factors]] (crypto)

## Event-driven (macro announcements)
- **Who pays** : participants who de-risk before a scheduled announcement, and pay whoever carries the risk through it.
- **Works when** : around the event window, when there is real uncertainty to resolve.
- **Breaks when** : the premium is documented and traded away, or the regime shifts and the flow reverses.
- **Payoff** : few trades a year, close to binary.
- **Instrument traps** : 8 events a year means a decade for 80 observations: statistical power is the problem. Real bid/ask around news.
- **Read** : [[Lucca Moench 2015 Pre-FOMC Drift]] · [[Savor Wilson 2013 Macro Announcement Days]] · [[Mueller Tahbaz-Salehi Vedolin 2017 FX and FOMC]]

## Carry
- **Who pays** : whoever wants to shed a risk pays you to hold it. Rate differential, roll yield, dividend against financing.
- **Works when** : calm markets, stable or falling volatility.
- **Breaks when** : volatility spikes, deleveraging, crisis (2008, March 2020).
- **Payoff** : steady small gains, rare large loss. Negative skew: the mirror image of trend.
- **Instrument traps** : the carry you measure is not the carry you earn. Dividends, coupons, roll and funding must all be in the P&L.
- **Read** : [[Koijen 2018 Carry]]

## Reversal
- **Who pays** : forced sellers and buyers overshoot; the liquidity provider is paid when the price snaps back.
- **Works when** : high volatility, liquidation cascades, short horizons.
- **Breaks when** : a real regime change (the "dip" keeps falling), trending markets.
- **Payoff** : frequent small gains, occasional large loss.
- **Instrument traps** : costs dominate at short horizons; the bid/ask must be in the backtest.
- **Read** : Jegadeesh (1990) · Nagel (2012), *Evaporating Liquidity*

## Value
- **Who pays** : prices drift away from a fundamental anchor and come back; whoever pushed them away pays.
- **Works when** : multi-year horizons, after dislocations.
- **Breaks when** : long stretches away from the anchor (equity value, 2010-2020).
- **Payoff** : slow and lumpy.
- **Instrument traps** : the anchor must be defined before the test (PPP for FX, yield for bonds, book value for equities).
- **Read** : Asness, Moskowitz, Pedersen (2013), *Value and Momentum Everywhere*

## Low volatility / defensive
- **Who pays** : investors who cannot use leverage overpay for high-beta assets, so low-beta assets are underpriced.
- **Works when** : most of the time, quietly.
- **Breaks when** : sharp risk-on rallies.
- **Payoff** : steady, low beta.
- **Instrument traps** : it needs leverage to matter, and the borrowing cost is part of the P&L.
- **Read** : Frazzini, Pedersen (2014), *Betting Against Beta*

## Seasonality and flows
- **Who pays** : participants who must trade at a known date: month-end rebalancing, index reconstitution, option expiry, hedge rebalancing.
- **Works when** : around the scheduled flow.
- **Breaks when** : the flow is arbitraged away or the calendar changes.
- **Payoff** : event-based, few trades.
- **Instrument traps** : few observations per year; statistical power is the problem.
- **Read** : Etula, Rinne, Suominen, Vaittinen (2020), *Dash for Cash* · Melvin, Prins (2015), *Equity hedging and exchange rates at the London 4 p.m. fix* · Quantpedia seasonality screens

---

## How to use this note
1. You read about a strategy: find its family. If it fits none, you either found something new (rare) or you do not yet know who pays (common).
2. Copy its "works when" and "breaks when" into box 1.3 of the strategy sheet, then make them specific to your strategy. That is what you will check after the backtest.
3. Keep it alive: every source you read goes under its family. Two or three per family is plenty.

Related: [[Reading Sources]] · [[Glossary]] · [[Strategy Sheet Template]]
