---
type: reference
---

# Instrument Traps

> **What this is** : the ways a price return is not the return you actually earn. One example with numbers per trap.
> **Open it** : when filling box 1.6 of a strategy sheet, and before believing any backtest built on close prices alone.

The price series tells you what the asset did. Your P&L depends on what your **position** did, and the two differ by everything below.

---

## By instrument

### Equities : dividends
- **What it does to a naive backtest** : a long strategy on price alone understates its return; a short one understates its cost.
- **Example** : S&P 500 price return 2010-2020 ≈ 10.7 % a year, total return ≈ 13.0 %. A short book pays that 2.3 % every year.

### Futures : roll yield
- **What it does** : a continuous price series hides the gain or loss of rolling from one contract to the next. Contango costs a long; backwardation pays it.
- **Example** : natural gas in chronic contango: spot roughly flat over a decade, a rolled long lost most of its value. A trend signal on the non-adjusted series shorts it for the wrong reason.

### Perpetual futures : funding
- **What it does** : paid every 8 hours between longs and shorts, often larger than the price drift you are trying to capture.
- **Example** : 0.03 % per 8 hours = 33 % a year. A long book on high-funding names bleeds it; a short book collects it. In Crypto XS Momentum, about a third of the P&L on the honest universe is funding.

### Bonds : coupons and pull to par
- **What it does** : price alone misses the coupon and the mechanical convergence to par.
- **Example** : a 10-year bond with a 4 % coupon whose price is flat over a year returned about +4 %, not zero.

### FX : interest differential
- **What it does** : holding a pair earns or pays the rate differential (the carry) on top of the spot move.
- **Example** : long AUD/JPY 2010-2014: spot roughly flat, carry about +3 % a year. A spot-only backtest shows nothing.

---

## On everything

### Bid/ask and slippage
- **What it does** : buying and selling at mid does not exist. A flat cost per trade understates the illiquid names.
- **Example** : FOMC Drift: going from mid prices to the real bid/ask took the edge from 9.1 to 7.7 bp per trade.

### Survivorship
- **What it does** : today's list applied to the past only contains the names that did not die.
- **Example** : Crypto XS Momentum: today's top 20 applied to the past makes 83 % of its P&L on price; the point-in-time top 20 makes 53 %. Same code.

### Look-ahead in membership
- **What it does** : if membership uses volume or market cap, that number must be known at the date.
- **Example** : a "top 20 by average volume over the sample" knows in 2021 what will be big in 2026.

---

## The rule
Before the first backtest, write in box 1.6 of the sheet which of these apply, and how the P&L will account for them. If the data cannot account for one of them, say so in box 2.9 (what I did not test).

Related: [[Strategy Families]] · [[Glossary]] · [[Data Sources]]
