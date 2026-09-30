---
type: reading
source_type: paper
title: Common Risk Factors in Cryptocurrency
authors: Yukun Liu, Aleh Tsyvinski, Xi Wu
year: 2022
journal: Journal of Finance, 77(2)
link: https://www.nber.org/papers/w25882
family: Trend
status: read
date_read: 2026-08
---

# Common risk factors in cryptocurrency (Liu, Tsyvinski and Wu, 2022)

> **Status** : read, used for [[Crypto XS Momentum]] (source of box 1.2, with [[Moskowitz Ooi Pedersen 2012 Time Series Momentum]]).

## 1. The mechanism (one sentence)
> Three factors, the crypto market, size and momentum, explain the differences in expected returns across coins; momentum means coins that did better than the others over the last weeks keep doing better the following week.

**Type** : **behavioural bias**, as for momentum in general (the paper documents the factor; the behavioural reading is ours).

## 2. What the paper actually tested
- **Assets / universe**: coins with price, volume and market cap on CoinMarketCap, market cap above $1 million: from 109 coins in 2014 to 1,583 in 2018.
- **Period**: 2014 to 2018.
- **Signal**: past returns over 1 to 4 weeks, coins sorted into groups each week, long the top, short the bottom.
- **Holding period**: one week, rebalanced weekly.
- **Headline result**: the long-short momentum portfolios earn significant weekly returns for lookbacks of one to four weeks; about 4 % a week for the three-week version.
- **Costs included?** no.

## 2c. What surprised me
- Weekly, cross-sectional, and on a universe that grows from a hundred to fifteen hundred coins. Most of those coins could not be traded at size. The effect is real in the data; the question is how much of it survives on what you can actually trade.

## 2d. What could this secretly be?
- A small-coin effect: on tiny, illiquid coins, "momentum" can be stale prices and noise. On perps, a funding effect: the short book collects funding from the weak names (box 1.3 of [[Crypto XS Momentum]]).

## 3. What may have changed since publication
- The sample ends in 2018, before perpetual futures became the main crypto market. Shorting a coin in 2018 was hard; on perps it is as easy as buying.
- The universe has changed completely: most of the 2018 coins are dead or irrelevant.

## 4. How I would test it with my data
- Only what I can trade: the top 20 Binance perps by volume, point-in-time. Daily data, three speeds (7, 30, 90 days) instead of one weekly sort, funding in the P&L.

## 5. Derivations
| # | Brick changed | Variant | Why it might still work | Priority |
| --- | --- | --- | --- | --- |
| 1 | Universe | All coins → top 20 perps by volume | Tradable, shortable, costs realistic | done → [[Crypto XS Momentum]] |
| 2 | Horizon | 1-4 weeks → 7 / 30 / 90 days averaged | Do not bet on one horizon | done |
