---
type: strategy
name: {{title}}
family: 
version: v1
status: testing
created: {{date}}
last_update: {{date}}
sharpe_net: 
turnover: 
corr_to_book: 
code: 
data_snapshot: 
---

# {{title}}

> **Status** : testing → live / parked / killed (the folder is the status). Register: [[_Index]]
> **Rule** : Pass 1 is written **before a single line of code**. Pass 2 only after the diagnostic. Every variant run goes to the [[Research Log]] as you run it.
> Reading note: [[ ]]

---

## PASS 1 : the hypothesis (before any test)

### 1.1 Mechanism
Who pays me, and why? One sentence.

> 

### 1.2 Source and crowding
Where the idea comes from. Who else trades it, since when is it public, why would it still pay.

- **Source**: 
- **Crowding**: 

### 1.3 Expected behaviour
Start from the family row in [[Strategy Families]], then make it specific.

- **Should work when**: 
- **Should suffer when**: 
- **Expected payoff profile** (many small losses / few big gains, or the reverse): 
- **What it could secretly be** (beta, carry, short vol, liquidity): 

### 1.4 Universe (intended) and why
Liquidity, costs, history available, coherence with the mechanism. How survivorship is handled.

- 

### 1.5 Horizon, trade count, data
- **Holding period**: 
- **Expected trades per year**: 
- **Enough observations to conclude?** 
- **Data needed and known gaps**: 

### 1.6 Instrument traps
Dividends, roll, funding, coupons, bid/ask, survivorship, look-ahead in the universe. Anything that makes price return ≠ position return.

- 

### 1.7 Kill criterion : for the backtest (written now, before the result)
The result that makes me drop it without discussion. Judges the backtest. Two parts:
- **on the full sample**: minimum Sharpe or t-stat, maximum concentration, maximum turnover;
- **out-of-sample vs in-sample, three zones**: *confirms* if the OOS mean is above half the IS mean → keep; *ambiguous* if between −½ and +½ → wait for data, paper only; *contradicts* if below −½ the IS mean with an OOS t-stat under −1.5 → kill. Losing half of the edge out of sample is normal; a reversed sign with a significant t is not.

> 

### 1.8 Exit criterion : for live (written now, before going live)
The behaviour that makes me cut it once it runs. Judges the live strategy. Usually a drawdown limit on the vol-targeted equity, and a regime check against 1.3.

> 

### 1.9 Test plan (written now)
Sample and IS/OOS split fixed before looking. Variants planned. Cost assumption.

- **Sample**: 
- **IS / OOS split**: 
- **Variants planned** (each one will be a row in the log): 
- **Cost assumption (bps, one way)**: 

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
| v1 | {{date}} | first version | |
