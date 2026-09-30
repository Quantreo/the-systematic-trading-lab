---
type: strategy
name: TSMOM 12-Month Trend
family: Trend
version: v1
status: testing
created: 2026-09
last_update: 2026-09
sharpe_net: 
turnover: 
corr_to_book: 
code: 
data_snapshot: 
---

# TSMOM 12-Month Trend

> **Status** : testing. Pass 1 is written (lesson 2.1). **Pass 2 is yours** : build it, run the diagnostic, fill every box, and give the verdict. Register: [[_Index]]
> **Rule** : Pass 2 only after the diagnostic. Every variant you run goes to the [[Research Log]] as you run it. Do not change Pass 1 after seeing a result.
> Reading note: [[Moskowitz Ooi Pedersen 2012 Time Series Momentum]]

---

## PASS 1 : the hypothesis (before any test)

### 1.1 Mechanism
> Prices under-react to news, then flows chase them. I am paid by whoever sells a rising market too early and buys it back later.

### 1.2 Source and crowding
- **Source**: Moskowitz, Ooi and Pedersen (2012), *Time Series Momentum*; every CTA since the 1980s.
- **Crowding**: very crowded. It still works because the mechanism is a property of how people trade (under-reaction, then chasing), not a secret someone can arbitrage away.

### 1.3 Expected behaviour
- **Should work when**: long, sustained moves (2022 in rates and energy).
- **Should suffer when**: ranges, sharp V-shaped reversals.
- **Expected payoff profile**: many small losses, a few large gains.
- **What it could secretly be**: long volatility, roughly: it earns when markets move a lot.

### 1.4 Universe (intended) and why
- About fifty liquid futures across equities, bonds, commodities and FX. The mechanism needs breadth; the assets must be tradable at low cost.

### 1.5 Horizon, trade count, data
- **Holding period**: weeks to months.
- **Expected trades per year**: a few per market, a few hundred in total.
- **Enough observations to conclude?** Yes, across fifty markets and several decades.
- **Data needed and known gaps**: daily futures prices, back-adjusted for the signal; contract-level prices for the P&L.

### 1.6 Instrument traps
- Roll yield: back-adjusted series for the signal, the real contracts for the P&L.

### 1.7 Kill criterion : for the backtest
> Drop it if the net Sharpe is below 0.3, or if two markets carry the whole P&L, or if turnover is above 50 × a year. Out of sample: the three-zone rule of the template.

### 1.8 Exit criterion : for live
> Cut it if the drawdown of the vol-targeted equity goes past 1.5 × the worst drawdown of the backtest, or if it loses for twelve months while markets are clearly trending.

### 1.9 Test plan
- **Sample**: all the history the data gives.
- **IS / OOS split**: one date, fixed before any result.
- **Variants planned**: lookback 3, 6 and 12 months. Nothing else.
- **Cost assumption (bps, one way)**: written as a number before the test (for liquid futures, a few bps plus the roll).

---

## PASS 2 : what I measured (after design and diagnostic)

### 2.0 Implementation
- **Code**: (path / notebook)
- **Data snapshot**: (source, date range, date pulled)
- **Run date**: 

### 2.1 Signal retained
Raw signal, normalisation, variants averaged, FDM.

- 

### 2.2 Universe retained
- 

### 2.3 Sizing and risk
- **Position sizing** (equal weight / inverse vol / ERC): 
- **Strategy vol target**: 
- **Rebalancing rule and hysteresis**: 
- **Minimum capital**: 

### 2.4 Diagnostic
| Metric | IS | OOS | Full |
| --- | --- | --- | --- |
| Sharpe gross | | | |
| Sharpe net | | | |
| 95 % interval on Sharpe (bootstrap) | | | |
| t-stat | | | |
| Annual return / vol | | | |
| Worst drawdown | | | |
| Turnover (× per year) | | | |
| Breakeven cost (bps) | | | |
| Positive years / total | | | |

### 2.5 Contribution by asset and by day
Does it hold without the top 2 assets? Without the top 10 days?

- 

### 2.6 Behaviour by regime vs expected
| Regime | Expected (1.3) | Observed | Match? |
| --- | --- | --- | --- |
| High vol | | | |
| Low vol | | | |
| Trending | | | |
| Range | | | |

### 2.7 Variants tested
From the [[Research Log]]. The more you tried, the more your best result is inflated.

- **Variants tested**: 
- **Haircut applied** (see [[Deflated Sharpe]]): 

### 2.8 Known weaknesses
What would invalidate it tomorrow. Cost sensitivity. Concentration.

- 

### 2.9 What I did not test
Honest scope. What a reviewer would ask for next.

- 

### 2.10 Verdict
- [ ] **Keep** → move to `Live/`, create a [[Portfolio Checklist Template|Portfolio Checklist]] note, then a [[Live Monitoring Template|Live Monitoring]] note
- [ ] **Kill** → move to `Killed/`, log the reason in [[Research Log]]
- [ ] **Park** (on hold, not killed) → move to `Parked/`, write what would bring it back: 

**Decided on**:   **Next review**: 

---

## Changelog
| Version | Date | What changed | Why |
| --- | --- | --- | --- |
| v1 | 2026-09 | Pass 1 written | example of lesson 2.1 |
