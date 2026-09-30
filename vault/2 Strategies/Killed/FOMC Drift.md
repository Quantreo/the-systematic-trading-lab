---
type: strategy
name: FOMC Drift
family: Event-driven
version: v2
status: killed
created: 2024-06
last_update: 2026-09
sharpe_net: 0.74 full sample, negative since 2025
turnover: 8 round trips per year
corr_to_book: low (event-based)
code: notebooks/01_fomc_drift.ipynb
data_snapshot: Dukascopy minute bid/ask, 6 pairs, 2012-01 → 2026-09-16
---

# FOMC Drift

> **Status** : **KILLED** on 2025-10-29 by the pre-registered drawdown stop. Kept as the reference case of a strategy that passed every test and died anyway. Register: [[_Index]]
> Reading notes: [[Lucca Moench 2015 Pre-FOMC Drift]] and the four papers in 1.2 · Log: [[Research Log]] · Monitoring: [[FOMC Drift Monitoring]]

---

## PASS 1 : the hypothesis (written 2024-06, before any test)

### 1.1 Mechanism
> Before a scheduled FOMC decision, many participants want to cut their dollar exposure so as not to carry the decision risk. They do it in advance, because their positions are too large to unwind at once and spreads widen as the announcement nears. Someone has to take the other side: liquidity providers with risk limits, who demand a premium for carrying that risk until the announcement. That de-risking flow pushes the dollar down over the run-up. I take the liquidity provider's side, long XXX/USD during the window, and exit before the decision so I never carry the decision itself. My risk is that the drift does not happen on my window, not the Fed surprise; that is what I am paid for.

### 1.2 Source and crowding
- **Sources**: five papers, one reading note each. None of them trades the dollar in the 24 h before the meeting: that construction, and the positioning story, are mine.
  - [[Lucca Moench 2015 Pre-FOMC Drift]] : the starting point. US equities earn a large share of their annual premium in the 24 h before scheduled FOMC announcements, and the paper has no accepted explanation for it.
  - [[Savor Wilson 2013 Macro Announcement Days]] : the effect is not only the Fed. Stock returns are much higher on days of scheduled macro announcements in general.
  - [[Ai Bansal 2018 Announcement Premium]] : a theory of why a premium can be earned when scheduled uncertainty is resolved.
  - [[Cieslak Morse Vissing-Jorgensen 2019 FOMC Cycle]] : the whole FOMC calendar matters for equities, not only the day before.
  - [[Mueller Tahbaz-Salehi Vedolin 2017 FX and FOMC]] : the bridge to FX. Short USD, long other currencies earns more on FOMC days, and more when monetary uncertainty is high.
- **Crowding**: the equity version is public since 2011 and widely traded; the FX version is not documented. If the equity drift is arbitraged, the FX one may follow.

### 1.3 Expected behaviour
- **Should work when**: the meeting is scheduled and watched. Initial hypothesis: stronger when monetary uncertainty is high (more people need to hedge). If the effect is spread at random across meetings, bad sign.
- **Should suffer when**: the outcome is fully priced, or the USD is bid for other reasons (risk-off, safe-haven flows).
- **Expected payoff profile**: small frequent gains (~+10 bp per trade), occasional larger losses on risk-off days.
- **What it could secretly be**: a risk-on day effect. If the basket only wins on days the whole market is risk-on, it is not an FOMC effect.

### 1.4 Universe (intended) and why
Short-USD basket of 6 legs: long EUR/USD, GBP/USD, AUD/USD, NZD/USD; short USD/CAD, USD/CHF. Equal weight. A basket rather than EUR/USD alone to isolate the USD leg and average out pair-specific noise. Minute bid/ask since 2012 (Dukascopy): real spreads, no survivorship question (fixed universe of majors).

### 1.5 Horizon, trade count, data
- **Holding period**: 24 h, entry at announcement −24 h, exit at announcement −5 min.
- **Expected trades per year**: 8.
- **Enough observations?** ~115 over 14 years: enough for a t-stat, not enough to detect slow decay quickly. Hence the drawdown stop.
- **Data**: Dukascopy minute bid/ask; FOMC calendar rebuilt deterministically (scheduled meetings, 14:00 ET with DST). Gaps possible in minute bars: snap to last bar ≤ timestamp, 12-minute tolerance.

### 1.6 Instrument traps
- Bid/ask: buy the ask, sell the bid. A flat 1 bp cost understates AUD and NZD spreads.
- Exit 5 min before: never hold the announcement itself.
- No future bar ever used (searchsorted, side right, minus one). **A look-ahead was found and fixed in v1**: the exit was glued to the announcement timestamp and captured a sliver of the reaction. Moving the exit before the announcement on minute data confirmed the drift is real and prior to the news, not an artefact.

### 1.7 Kill criterion : backtest (written 2024-06)
> Full sample: basket t-stat below 2 on the in-sample, or a result carried by one pair.
> OOS vs IS, three zones: confirms if OOS mean > +½ IS mean (> +5.4 bp) ; ambiguous between −5.4 and +5.4 bp ; contradicts if OOS mean < −5.4 bp with t < −1.5 → kill.
> Applied: OOS 2019-2024 = +11.6 bp → confirms. Fresh 2025-2026 = −18.5 bp, t −3.4 → contradicts. Not a fading edge, a reversed one.

### 1.8 Exit criterion : live (written 2024-07, before going live)
> Drawdown of the 10 %-vol-targeted equity below −20 %, point-in-time. Secondary: rolling 24-trade Sharpe < 0, rolling 24-trade cumulative return < 0.

### 1.9 Test plan (written before)
- **Sample**: 2012-01 → latest FOMC.
- **IS / OOS split**: IS before 2019, OOS 2019-2024, then "fresh" 2025+ as it arrives.
- **Variants planned**: EUR/USD alone vs basket; exit at 0 vs −5 min; mid vs bid/ask; 12 h and 48 h windows.
- **Cost assumption**: real bid/ask from the data.

---

## PASS 2 : what I measured

### 2.0 Implementation
- **Code**: `notebooks/01_fomc_drift.ipynb`
- **Data snapshot**: Dukascopy minute, 6 pairs, 2012-01-24 → 2026-09-16, 117 meetings with ≥ 5 legs.
- **Run date**: 2026-09.

### 2.1 Signal retained
No signal: pure calendar. Short USD basket from T−24 h to T−5 min on every scheduled FOMC.

### 2.2 Universe retained
The 6-leg basket; a trade counts if at least 5 legs have data.

### 2.3 Sizing and risk
- **Position sizing**: equal weight across legs.
- **Strategy vol target**: 10 % annualised (constant leverage, calibrated ex-post for display only).
- **Rebalancing**: none within the trade.
- **Minimum capital**: low; spot FX or CFDs on 6 pairs.

### 2.4 Diagnostic
| Metric | IS 2012-2018 | OOS 2019-2024 | Fresh 2025-2026 | Full |
| --- | --- | --- | --- | --- |
| Mean per trade, net bid/ask (bp) | +10.9 | +11.6 | **−18.5** | +7.7 |
| t-stat | 2.85 | 2.75 | **−3.37** | 2.82 |
| Hit rate | 64 % | 62 % | **14 %** (2 of 14) | 57 % |
| Trades | 56 | 47 | 14 | 117 |
| Sharpe (8 trades/yr) | | | | 0.74 |
| CAGR at 10 % vol | | | | 7.1 % |
| Worst drawdown | ≈ −12 % | | **−29.5 %** | −29.5 % |
| Gross (mid) vs net (bid/ask), full | | | | +9.1 vs +7.7 bp |
| Bootstrap 5-95 % : Sharpe / max DD | | | | 0.34-1.16 / −10 to −28 % |

### 2.5 Contribution by asset and by day
The 2025-2026 reversal is not one leg: on the bad meetings (2025-03, 2025-07, 2026-03, 2026-04) almost all six pairs are negative at once. It is the USD, not a pair. EUR/USD alone gives the same picture (−17.8 bp net since 2025).

### 2.6 Behaviour by regime vs expected
| Regime | Expected (1.3) | Observed | Match? |
| --- | --- | --- | --- |
| 2012-2024, uncertainty about the path | positive drift | +11 bp, stable IS and OOS | yes |
| 2025-2026 | positive drift | **USD bid into almost every meeting**, −18 bp | **no** : the mechanism no longer describes the market |
| High vs low monetary uncertainty | drift should scale with uncertainty | tested on 3 independent proxies (bond vol, realised 2Y vol, dispersion of FOMC probabilities): **no relation**, drift constant at ~12 bp | **no** : hypothesis revised, see 2.8 |
| Basket vs single pair | basket smoother | basket t 2.8 vs EUR/USD 2.6 | yes |

### 2.7 Variants tested
- **Variants tested**: 6 (see [[Research Log]]).
- **Haircut**: with the deflated Sharpe (variance of the Sharpes across trials, which handles the fact that variants are correlated), a raw t of 2.5 on eight trials falls close to the significance threshold. Choices on execution criteria (exit time set on the spread) do not consume a trial; choices on performance do.

### 2.8 Known weaknesses and what the data changed
- **Mechanism revised after the regime test.** The drift did not scale with uncertainty. So it is not a variable uncertainty premium but a structural, recurring positioning flow. Consequence for sizing: vol target, not a scaling on uncertainty, because in agitated regimes the signal stays constant while the noise rises, so the Sharpe degrades. I changed the story when the data contradicted it, and wrote down that I did.
- **Three ways it breaks, written before it did**: (1) the effect gets arbitraged, the classic post-publication decay; (2) another driver dominates a meeting (crisis, geopolitics, a larger macro shock) and the window is polluted by noise stronger than the signal; (3) the dollar regime changes and the USD strengthens into the meeting instead of weakening. 2025-2026 looks like (3), but 14 meetings cannot prove it and I do not attach a macro story I could not have predicted.
- 8 trades a year: a regime break takes a year to show in averages. The drawdown stop is the only fast indicator.
- Costs on AUD/NZD are the largest share of the gross-to-net gap.
- **Why it stopped is not understood.** Rates, positioning and vol conditioning were checked in 2025: no reliable relation. An edge can die without an explanation; that is exactly why the stop had to be mechanical.

### 2.9 What I did not test
- Conditioning on implied vol or on the priced probability of a move (derivation 3 of the reading note).
- Other central banks (ECB, BoE): in the [[Idea Journal]].
- Whether the 2025 reversal is itself tradable (long USD into FOMC). Tempting, and exactly the kind of after-the-fact story Pass 1 exists to prevent.

### 2.10 Verdict
- [ ] Keep
- [x] **Kill** : passed the backtest kill criterion (t 2.85 IS, 2.75 OOS, no single pair carrying it). Killed live by the exit criterion: drawdown stop hit 2025-10-29 at −20 %. The 7 trades after the stop averaged −14.3 bp: cutting was right. The two rolling stops never fired: too slow for a break this sharp.
- [ ] Park (on hold, not killed) : would come back if 8 consecutive meetings show a positive drift again **and** a mechanism for the 2025 reversal is found.

**Decided on**: 2025-10-29   **Next review**: none (killed)

---

## Changelog
| Version | Date | What changed | Why |
| --- | --- | --- | --- |
| v1 | 2024-06 | EUR/USD alone, hourly data, exit at announcement, 1 bp flat cost | first version |
| v2 | 2024-07 | 6-leg short-USD basket, minute bid/ask, exit −5 min, pre-registered stops | isolate the USD leg, real costs, never hold the reaction |
| v2 | 2026-09 | data extended to 2026-09-16, verdict recorded | post-mortem |
