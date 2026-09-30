---
type: reference
---

# Reading the Diagnostic

> **What this is** : every number in the diagnostic table, in three lines each: what it is, how to read it, the trap.
> **Open it** : every time you look at a backtest result, yours or someone else's.

The numbers below are the Crypto XS Momentum ones (top 20, point-in-time, net of funding and 5 bp).

## Return and risk

**Sharpe ratio** : annualised return divided by annualised volatility. Return per unit of risk. Here 0.74.
Read it as a point on a scale: below 0.5 is hard to distinguish from luck in five years; 1 is a good strategy; above 2 on daily data over many years is rare and deserves suspicion.
Trap: it says nothing about *how* the return came (one great year or a steady stream), and it is a point estimate. See the range below.

**t-stat** : the Sharpe scaled by the length of the sample, roughly Sharpe × √years. Here 1.69.
Read it as "how many standard errors away from zero". Below 2, you have not shown much; above 3, something is there.
Trap: it grows with time, not with skill. A weak strategy with 30 years of data has a great t-stat.

**Bootstrap range** : resample the history in 3-month blocks and recompute. Here Sharpe 0.19 to 1.52, vol 16 to 20 %, max drawdown −14 to −33 %.
Read it as "what else this history could have looked like". A Sharpe is a point; the range is what to remember.
Trap: the bootstrap only reshuffles what happened. It cannot show you a regime the sample never saw.

**CAGR and volatility** : the compounded annual return, and its annualised standard deviation. Here 12.4 % and 17.8 %.
Read them together, never alone: 12 % at 18 % vol is a different thing from 12 % at 8 %.
Trap: the vol is what you chose (vol target). The CAGR follows from it. Compare strategies at the same vol, or compare Sharpes.

**Max drawdown** : the worst peak-to-trough fall. Here −22.8 %.
Read it against the vol: a strategy at 18 % vol will see 20-30 % drawdowns as a matter of course. Then ask whether *you* can sit through it.
Trap: the max drawdown of the past is not the max drawdown of the future. Expect the next one to be worse. The exit criterion uses 1.5× as a rule.

## Cost and mechanics

**Turnover** : how many times per year you trade your whole capital. Here 32×.
Read it in costs: every unit traded pays the cost once, so 32 × 5 bp ≈ 1.6 % of capital per year in fees, before slippage. Over the five years of the sample, that is the −8 % cost line.
Trap: turnover is the number that tells you whether a strategy is tradable, and almost nobody looks at it. A Sharpe of 1.5 at 300× turnover is a Sharpe of zero after costs.

**Breakeven cost** : the cost per trade, in bp, at which the net return would be exactly zero. Here 47 bp.
Read it against what you actually pay. If you pay 5 bp and breakeven is 47, you have margin. If breakeven is 8, you do not.
Trap: it is an average. The tail of the universe costs more than the average name.

**P&L split (price / funding / costs)** : where the money comes from. Here +53 % / +24 % / −8 % of capital, summed over the sample.
Read it as the honesty check: a third of this "momentum" strategy is funding collected by the short book. That is carry, and it will correlate with a carry strategy.
Trap: a backtest on price alone would have missed both the funding and its correlation.

## Concentration and regime

**Contribution by asset** : share of P&L made by the top names. Here top 5 = 69 %.
Read it as "is this a universe strategy or a bet on two names". 100 % in five names means the other fifteen are decoration.
Trap: convex strategies (trend) are always concentrated in their winners. Compare with the same test on a known trend strategy before panicking.

**Contribution by day** : share of P&L made by the best 10 days. Here 60 %; Sharpe 0.32 without them.
Read it as fragility. If ten days carry everything and you were not there, you have nothing.
Trap: same as above; the level matters more than the concentration.

**Behaviour by regime** : returns conditioned on the state the mechanism needs. Here +1.8 % per month in high-dispersion months, +0.4 % in low-dispersion.
Read it against Pass 1: does it lose where you said it would? If yes, you understand what you trade.
Trap: if it wins everywhere, you do not understand what you trade, and you will not know when it stops.

## What to do with the table
1. Read the split and the turnover first. They tell you whether the Sharpe is real and tradable.
2. Read the range, not the point.
3. Read the regime table against Pass 1.
4. Then, and only then, read the Sharpe.
