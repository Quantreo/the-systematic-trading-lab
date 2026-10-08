---
type: routine
---

# My Research Routine

> **What this is** : the whole method as a schedule. Weekly to produce research, monthly to run the book, quarterly to step back.
> **Open it** : Monday morning, until it becomes a habit.
> **The rule behind everything** : write what you expect before you look at the result.

## The week at a glance

| Slot | Time | Output | Note it lives in |
| --- | --- | --- | --- |
| 1. Read | 1-2 h | 1 reading note, 1 journal row | [[Reading Note Template]] · [[Idea Journal]] |
| 2. Derive | 1-2 h | 1 strategy sheet, Pass 1 complete | [[Strategy Sheet Template]] |
| 3. Test | 2-4 h | Pass 2, a verdict, every run logged | [[Research Log]] |

About 5 to 8 hours a week. Same slots, same order, every week.

## Weekly

**1. Read (1-2 h)**
- One paper, fund letter or book chapter from [[Reading Sources]].
- A note from the [[Reading Note Template]]: mechanism, data and period, what changed since, how I would test it.
- One row in the [[Idea Journal]]. **Do not test today.** An idea that still looks good a week later deserves a sheet.

**2. Derive (1-2 h)**
- Pick one idea from the journal that has survived a week.
- Break it into its six bricks: economic intuition, universe, signal, horizon, sizing, rebalancing. Move one brick at a time: each variant is a candidate.
- A note in `2 Strategies/` from the [[Strategy Sheet Template]]. Fill **Pass 1 entirely**, kill criterion and "should suffer when" included, **before any code**.

**3. Test (2-4 h)**
- Notebook: universe, signal (variants averaged), sizing (inverse vol, vol target), backtest net of costs.
- Diagnostic against what Pass 1 said: Sharpe and how much of it is luck, turnover and breakeven cost, drawdown, contribution by asset, behaviour by regime. See [[Reading the Diagnostic]].
- High turnover: add hysteresis before you judge.
- **Every run gets a row in the [[Research Log]]**, the failures first.
- Fill Pass 2. Verdict: keep, kill or park. Move the note, update [[_Index]].

## Monthly

**4. Run the book (1 h)**
- **Candidates** ("keep"): a note from the [[Portfolio Checklist Template]]. The bar: Sharpe > correlation × Sharpe of the book. Then the block bootstrap.
  - 90 % or more: in, at half weight.
  - 60 to 90 %: on paper, re-test next quarter.
  - Below 60 %: no.
- **Live strategies**: update each [[Live Monitoring Template|Live Monitoring]] note. Rolling Sharpe, drawdown, CUSUM. Status on written rules only: watch, halve, cut.
- **The book**: update the [[Strategy Table]]. Weights, bad-day correlation, IDM against its cap (2.5), drawdown against the loss limit.

## Quarterly

**5. Step back (2 h)**
- Re-run the bootstrap for every strategy on paper. New data, new decision.
- Half-weight strategies past 6 months: full weight only if the three checks pass (tests green, losses look like the backtest, costs as planned).
- Read the [[Research Log]] of the quarter: which families keep failing? Which bricks keep working? Adjust next quarter's reading.
- Count the pipeline (below). If nothing reached a verdict, the routine slipped: fix the slots, not the standards.

## The pipeline, measured

Track it once a month, not the P&L.

| Stage | Healthy pace |
| --- | --- |
| Ideas in the journal | 4 or more a month |
| Strategy sheets (Pass 1 done) | 2 to 4 a month |
| Verdicts (Pass 2 done) | 2 or more a month |
| Strategies kept | 1 a quarter is a good quarter |

Most sheets end in "kill". That is the routine working, not failing.

## Non-negotiables

1. Pass 1 before code. Always.
2. Every run is logged, especially the bad ones.
3. Entries at half weight, exits on the written rule.
4. Nothing changes in the book outside the monthly slot.
