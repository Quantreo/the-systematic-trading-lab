---
type: reading
source_type: paper
title: The Pre-FOMC Announcement Drift
authors: David Lucca, Emanuel Moench
year: 2015
journal: Journal of Finance, 70(1)
link: https://www.newyorkfed.org/research/staff_reports/sr512.html
family: Event-driven
status: derived
date_read: 2024-06
---

# The Pre-FOMC Announcement Drift

> **Status** : derived → see [[FOMC Drift]]

## 1. The mechanism (one sentence)
> US equities earn most of their annual excess return in the 24 hours before scheduled FOMC announcements. The paper documents the effect; it does not find a mechanism that explains it.

## 2. What the paper actually tested
- **Assets / universe**: S&P 500, intraday; other major equity indices as a check
- **Period**: September 1994 to March 2011, 131 scheduled meetings
- **Signal**: none, purely calendar: long from 2 pm the day before the announcement to 2 pm on announcement day (the statement came out around 2:15 pm)
- **Horizon / holding period**: 24 h
- **Sizing**: constant
- **Rebalancing**: 8 trades per year
- **Headline result**: about +49 bp per pre-FOMC window. Those 24-hour windows account for more than 80 % of the equity premium over the sample; all the other days together earn under 1 % a year
- **Costs included?** no (index level)

## 2b. Numbers to remember
- About +49 bp per pre-FOMC window, S&P 500, 1994-2011
- More than 80 % of the equity premium earned in those 8 windows a year
- Returns on announcement days more than 30 times larger than on other days, and earned **before** the announcement

## 2c. What surprised me
- The effect is huge and has no accepted explanation in the paper itself. The authors test several risk-based explanations and none of them works. An effect without a mechanism is fragile, and mine (hedging flows) is a hypothesis, not their finding.
- The authors also report that the pattern does **not** appear in other asset classes. My FX version therefore goes against what they found: it has to be tested, not assumed.

## 2d. What could this secretly be?
- Could be plain equity beta concentrated on 8 days (it is, by construction: the paper measures it). In FX, the suspect is a risk-on / USD-down day effect: is the basket just short USD on days that happened to be risk-on?

## 2e. Related reading (the literature around this paper, one short note each)
- [[Savor Wilson 2013 Macro Announcement Days]] : stock returns are higher on macro announcement days in general.
- [[Ai Bansal 2018 Announcement Premium]] : a theory of why a premium is earned when scheduled uncertainty resolves.
- [[Cieslak Morse Vissing-Jorgensen 2019 FOMC Cycle]] : the whole FOMC calendar shapes equity returns.
- [[Mueller Tahbaz-Salehi Vedolin 2017 FX and FOMC]] : short USD pays on FOMC days. The bridge to FX.

## 3. What may have changed since publication
- Published 2011 (NY Fed staff report), 2015 (Journal of Finance). Widely cited and traded since; later studies find the equity drift much weaker after publication (for example Kurov, Wolfe and Gilbert, *The Disappearing Pre-FOMC Announcement Drift*).
- Fed communication changed: press conferences at every meeting since 2019, forward guidance, dot plots. Less uncertainty to resolve on the day.

## 4. How I would test it with my data
- I do not have clean intraday equity data but I have Dukascopy minute bid/ask FX since 2012.
- The same logic in FX: if participants hedge or reduce risk before the announcement, the USD should weaken (risk-on unwinds of USD hedges) in the 24 h before. Test long EUR/USD, then a short-USD basket.
- Exit **before** the announcement (5 min before) to never hold the reaction.

## 5. Derivations
Priority: **next** · **later** · **no**

| # | Brick changed | Variant | Why it might still work | Priority |
| --- | --- | --- | --- | --- |
| 1 | Universe | Equity → short-USD FX basket (EUR, GBP, AUD, NZD long; CAD, CHF via USD pairs) | Same pre-announcement de-risking, different instrument, real bid/ask | done → [[FOMC Drift]] |
| 2 | Horizon | 24 h → 12 h, 48 h | Where in the window is the drift concentrated | no : tested, 24 h kept |
| 3 | Conditioning | Only when implied vol is high / when a hike is priced | Drift should be larger when there is more uncertainty to resolve | later |
| 4 | Event | ECB, BoE, BoJ announcements | Same behaviour if the event is as scheduled and as watched | next : in [[Idea Journal]] |

## 6. Next step
Status is in the frontmatter (read → derived → tested → dropped). Row in [[Idea Journal]] ; sheet in `2 Strategies/` if it deserves one.

