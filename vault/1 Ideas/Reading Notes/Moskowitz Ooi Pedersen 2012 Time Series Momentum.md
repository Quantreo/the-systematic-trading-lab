---
type: reading
source_type: paper
title: Time Series Momentum
authors: Tobias Moskowitz, Yao Hua Ooi, Lasse Pedersen
year: 2012
journal: Journal of Financial Economics, 104(2)
link: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2089463
family: Trend
status: derived
date_read: 2026-08
---

# Time Series Momentum

> **Status** : derived → see [[Crypto XS Momentum]] (two bricks changed) and [[TSMOM 12-Month Trend]] (the paper as it is, Pass 1 written)

## 1. The mechanism (one sentence)
> Prices under-react to information and then over-extend as flows chase them, so an asset's own past 12-month return predicts its next month return, across every liquid futures market.

## 2. What the paper actually tested
- **Assets / universe**: 58 liquid futures and forwards (equity indices, bonds, commodities, FX)
- **Period**: data from 1965, results mostly on 1985-2009
- **Signal**: sign of the past 12-month excess return (skip none), also 1-48 month lookbacks
- **Horizon / holding period**: 1 month, monthly rebalancing
- **Sizing**: position scaled to a 40 % ex-ante annualised vol per asset (inverse vol)
- **Rebalancing**: monthly
- **Headline result**: Sharpe above 1 for the diversified portfolio (about 2.5 times the equity market's), positive in all 58 contracts, best in extreme markets
- **Costs included?** no

## 2b. Numbers to remember
- Sharpe above 1 for the diversified 58-market portfolio, 1985-2009
- Positive in all 58 contracts, significant in 52 of them
- Best returns in the extreme months of the equity market (the "smile")

## 2c. What surprised me
- Every single market is positive. That is not a signal that works, that is a property of markets. It made me ask whether crypto, a market the paper never saw, has it too, and whether it survives when you remove the market bet.

## 2d. What could this secretly be?
- On crypto, a long-only momentum book is mostly a bet on the market: the coins move together. Cross-sectional, the suspect is **funding carry**: a demeaned book ends up short the high-funding names and collects it. Must be split out in Pass 2.

## 3. What may have changed since publication
- Roughly 2012 to 2019, a long flat period for futures trend following, then an exceptional 2022.
- Much more capital follows trend now (the CTA industry) than in the paper's sample.
- Crypto did not exist in the sample: a new, retail-heavy, highly volatile asset class where the under-reaction story is plausible but unproven at scale.

## 4. How I would test it with my data
- I have daily Binance perp data (prices, funding, volume) from 2020, a few hundred names ever listed.
- Direct TSMOM on crypto is mostly a bet on BTC: the names are too correlated. So go **cross-sectional**: rank by vol-adjusted past returns, long the top, short the bottom, market-neutral.
- Universe must be point-in-time (top 20 by volume at each date) or the result is survivorship.

## 5. Derivations
Priority: **next** · **later** · **no**

| # | Brick changed | Variant | Why it might still work | Priority |
| --- | --- | --- | --- | --- |
| 1 | Universe | Futures → crypto perps, top 20 by volume | Under-reaction is plausible in a retail-heavy market | done → [[Crypto XS Momentum]] |
| 2 | Signal method | Time-series → cross-sectional (rank, demean) | Removes the market bet in a highly correlated class | done |
| 3 | Horizon | 12 m → three speeds 7 / 30 / 90 days, averaged | Crypto moves faster; averaging speeds is Carver's approach | done |
| 4 | Signal method | EMA smoothing of the score | Cuts turnover on the fast speed | done |
| 5 | Universe | How many names: top 20 by volume | Beyond rank 20, names get small, noisy, costly | done, argued before the test |

## 6. Next step
Status is in the frontmatter (read → derived → tested → dropped). Row in [[Idea Journal]] ; sheet in `2 Strategies/` if it deserves one.

