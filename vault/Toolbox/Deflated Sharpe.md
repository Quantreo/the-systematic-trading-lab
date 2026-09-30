---
type: appendix
updated: 2026-09-25
---

# Deflated Sharpe

> **What this is** : how much to discount your best Sharpe for the number of variants you tried.
> **Open it** : when filling section 2.7 of a strategy sheet, or the Counts table of the [[Research Log]].

## The idea
If you test N variants and keep the best, its Sharpe is the maximum of N noisy draws, not an estimate of skill. The more you try, the higher the best one looks, even with zero true edge.

## The luck line (what the course uses)
Expected maximum annual Sharpe of N strategies with **no** skill, on T years of data (Bailey & López de Prado):

```
E[max SR] ≈ sqrt(1/T) · [ (1 − γ) · Z(1 − 1/N) + γ · Z(1 − 1/(N·e)) ]
```

γ ≈ 0.5772 (Euler), Z = inverse normal. With T = 5.2 years: N = 9 → 0.67 ; N = 2 → 0.18 ; N ≈ 1 → about 0.

The cruder sqrt(2 · ln N / T) overstates the line (0.92 instead of 0.67 for N = 9). Use the formula above.

## Correlated tries
N is the number of **independent** tries, not the number of runs. Variants of the same idea (with or without IDM, width 8 or 10, other lookback) move together. Rough effective N:

```
N_eff = N ÷ (1 + (N − 1) · ρ)     (ρ = average correlation of daily returns, same rule as the IDM)
```

Crypto XS Momentum: 9 design tries. Measured ρ 0.85 on the variants we can rebuild, but stay cautious and use 0.5: 1.8 independent tries, luck line 0.18, haircut Sharpe 0.56, about 90 % probability of beating luck. What remains uncertain is the short sample, not the search.

## The haircut
Haircut Sharpe = Sharpe − luck line(N_eff). For 0.74 on 5.2 years: 1 try → 0.74 ; 1.8 → 0.56 ; 3 → 0.37 ; 5 → 0.22 ; 9 → 0.08 ; past about 13 independent tries, nothing left.

## What counts as a trial
Log everything, count only choices made on a result. Stress tests (cost sensitivity, the pre-fixed buffer, the frozen control) are not trials: you did not pick them because they looked better.

## The formal version
Bailey & López de Prado (2014), *The Deflated Sharpe Ratio*: computes the probability that the observed Sharpe beats the expected maximum under the null, correcting for skewness, kurtosis and sample length. Harvey & Liu (2015), *Backtesting*, give haircut tables by number of trials.

## What to do in practice
1. Count your trials honestly in the [[Research Log]]. Every design choice made on a result counts, including the ones you forgot.
2. Estimate N_eff, then apply the luck line. If your best Sharpe is not clearly above E[max SR], you have not found anything yet.
3. Prefer averaging variants over picking the best: it lowers N and gives a more honest estimate.
