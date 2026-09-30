---
type: reading
source_type: paper
title: Carry
authors: Ralph Koijen, Tobias Moskowitz, Lasse Pedersen, Evert Vrugt
year: 2018
journal: Journal of Financial Economics, 127(2)
link: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2298565
family: Carry
status: derived
date_read: 2026-08
---

# Carry

> **Status** : derived. Two derivations noted in the [[Idea Journal]], no sheet yet.

## 1. The mechanism (one sentence)
> Carry is the return you earn if prices do not move; it is positive on average because it compensates for bearing risk in bad times (carry crashes when volatility spikes).

## 2. What the paper actually tested
- **Assets / universe**: eight asset classes: global equity indices, global government bonds, currencies, commodities, US Treasuries, US credit, equity index calls and puts
- **Period**: from the 1970s or 1980s depending on the class, to 2012
- **Signal**: the asset's carry (futures basis, rate differential, dividend yield minus financing, roll)
- **Horizon / holding period**: monthly
- **Sizing**: long/short within each class, weights proportional to the rank of the carry; the classes are then combined into a global portfolio
- **Rebalancing**: monthly
- **Headline result**: carry predicts returns in every class. Sharpe ratios from about 0.4 (credit, calls) to about 1 (equities, bond slope), 1.8 for puts; 1.2 for the diversified global carry portfolio
- **Costs included?** no

## 2b. Numbers to remember
- Sharpe 1.2 for the diversified global carry portfolio, most classes between 0.5 and 1
- Carry predicts returns in every class tested, eight of them
- Carry does badly in global recessions and liquidity crises, across classes at the same time

## 2c. What surprised me
- Carry is defined the same way everywhere: the return if nothing moves. One definition, eight asset classes. Once you see it, you find carry in places the paper does not list.

## 2d. What could this secretly be?
- Carry is short volatility by construction: it earns while nothing moves and loses when vol spikes. Before believing a carry backtest, look at its worst month next to a volatility index.

## 3. What may have changed since publication
- Well known and widely traded; FX carry in particular weakened after 2008.
- From 2009 to 2021, near-zero rates in most developed countries left little rate differential to earn in FX. Since 2022, differentials are back.

## 4. How I would test it with my data
- FX: I have minute bid/ask on the majors (Dukascopy) and short-term rates by country (FRED). Carry of a pair = rate differential. Rank the majors by it, long the highest, short the lowest.
- Traps: the P&L must include the rate differential itself, not only the spot move (see [[Instrument Traps]]); and six to ten majors are few names, partly one bet on the dollar.

## 5. Derivations
Priority: **next** · **later** · **no**

| # | Brick changed | Variant | Why it might still work | Priority |
| --- | --- | --- | --- | --- |
| 1 | Universe | Eight asset classes → G10 FX majors only | The differential is explicit and large again since 2022 | next : in [[Idea Journal]] |
| 2 | Universe | Eight asset classes → commodity futures curve | Backwardation pays the holder, same definition | later : in [[Idea Journal]] |
| 3 | Signal method | Raw carry vs carry divided by volatility | Which one ranks better | later |

## 6. Next step
Status is in the frontmatter (read → derived → tested → dropped). Row in [[Idea Journal]] ; sheet in `2 Strategies/` if it deserves one.
