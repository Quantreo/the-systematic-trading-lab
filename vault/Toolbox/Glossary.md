---
type: reference
---

# Glossary

> **What this is** : every term used in the course, one paragraph each.
> **Open it** : whenever a word in a lesson or a template is not clear.

**Mechanism** : the reason money moves from someone else to you. A risk premium, a constraint on a participant, a behavioural bias, a scheduled flow. The answer to "who pays me, and why".

**Pattern** : the observable trace that lets you capture a mechanism. A moving-average cross, a ranking, a breakout. A pattern without a mechanism is noise that survived your backtest.

**Risk premium** : a return earned for holding a risk others want to shed. Equity premium, carry, volatility selling. Pays on average, loses hard occasionally.

**Constraint** : a participant who must trade regardless of price. Index rebalancing, futures roll, forced liquidation, a central bank mandate. You are paid for taking the other side when they have no choice.

**Behavioural bias** : a systematic mistake by other participants. Under-reaction (trend), over-reaction (reversal), anchoring. It persists because those making it do not learn or cannot act.

**Scheduled flow** : predictable buying or selling at a known time. Month-end, option expiry, index reconstitution, macro announcements.

**The six bricks** : economic intuition, universe, signal, horizon, sizing, rebalancing. Every strategy is these six decisions.

**Universe** : the set of assets the strategy can hold. **Point-in-time** universe: membership decided with information available at each date. **Frozen** universe: today's list applied to the past (survivorship bias).

**Survivorship bias** : testing on the assets that exist today, which are by construction the ones that did not die. Inflates results.

**Forecast** : the signal scaled to a common unit (Carver: average absolute value 10), so that different signals and assets are comparable.

**FDM, forecast diversification multiplier** : when you average several correlated forecasts, the average is smaller than each. The FDM scales it back up. Principle: averaging shrinks, FDM restores.

**IDM, instrument diversification multiplier** : the same idea across assets: a portfolio of N assets at target vol each has less vol than target; IDM scales positions up.

**Vol targeting** : sizing each position so that the strategy runs at a chosen annualised volatility (15-20 % per strategy in this course, 10 % for the whole book).

**Inverse vol sizing** : each asset gets a weight proportional to 1 / its volatility, so each contributes about the same risk.

**Equal weight** : each asset gets the same capital. Simple; the most volatile assets dominate the risk.

**ERC, equal risk contribution** : weights such that each asset contributes exactly the same share of portfolio risk, correlations included. Inverse vol is ERC with correlations ignored.

**Basis point (bp, said "bips")** : 0.01 %. The unit for costs, spreads and small returns in every asset class. 5 bp = 0.05 %. Not "pips": a pip is an FX quoting convention, not a unit of return.

**Turnover** : how many times per year you trade your whole capital (× per year). Each unit traded pays the cost once: 32× at 5 bp ≈ 1.6 % of capital a year. The number that decides whether a strategy is tradable.

**Hysteresis, buffer, dead zone** : not trading small changes. Buffer: only trade if the gap to the ideal position exceeds a threshold (10 % here). Entry/exit thresholds: enter the top 20, exit only when falling below rank 25.

**Sharpe ratio** : annualised return divided by annualised vol. **t-stat** : Sharpe × sqrt(years), roughly. Below 2 you have not shown much.

**Breakeven cost** : the cost per trade, in bps, at which the strategy's net return is zero. Compare it with what you actually pay.

**Funding rate** : on a perpetual future, the periodic payment between longs and shorts that keeps the perp close to spot. When it is positive, longs pay and shorts collect. It is a carry return, and it must be kept apart from the price P&L.

**P&L split** : the P&L kept in separate columns (price, funding or carry, costs) instead of one total. It tells you what the strategy really earns from.

**Block bootstrap** : redrawing the history from blocks of consecutive days (about three months) to see the range of Sharpe, vol and drawdown the same strategy could have shown. A Sharpe is one draw; the range is what you remember.

**Dispersion** : how differently the assets of a universe move on a given day, measured as the standard deviation of their daily returns. Cross-sectional strategies need it: when everything moves together, there is nothing to rank.

**Drawdown** : the fall from the equity peak. **Max drawdown**: the worst one in the sample.

**Contribution by asset** : the share of total P&L each asset made. If two assets make it all, you do not have a universe strategy.

**Regime** : a market condition (high or low vol, trending or ranging, bull or bear). Behaviour by regime: does the strategy lose where the mechanism says it should?

**Kill criterion** : the result, written before the test, that makes you drop the strategy without discussion.

**Exit criterion** : the live mirror of the kill criterion, written when the strategy enters the book.

**Try (trial)** : a choice made after looking at a result. A stress test, a control or a choice fixed in advance is not a try. The Research Log keeps every run; the count keeps only the tries.

**Effective number of tries** : tries of one idea are correlated, so they are worth fewer independent tries. N_eff = N ÷ (1 + (N − 1) × ρ), the same rule as the IDM.

**Luck line** : the best Sharpe you would expect from N independent tries with no edge at all, on the same length of data. Above it, the result is more than the best of N draws.

**Haircut / deflated Sharpe** : the discount applied to your best Sharpe for the tries it took to find it: Sharpe minus the luck line of your effective tries. See [[Deflated Sharpe]].

**Sharpe marginal rule** : a strategy adds value to the book if its Sharpe > its correlation to the book × the book's Sharpe.

**Book** : the portfolio of strategies you actually run.

**Risk weight** : a strategy's share of the book's risk (not its capital), once each strategy runs at its own vol target.

**CUSUM** : a cumulative-sum test that flags a change in the mean of a series earlier than a rolling average would.
