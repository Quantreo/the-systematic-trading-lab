---
type: reference
---

# Data Sources

> **What this is** : enough data to spot ideas and run a first diagnostic, with links.
> **Open it** : when a paper note reaches question 4 ("how would I test it with my data").

## Going further : Quant Lake
The sources below are enough to spot an idea and run a first diagnostic. Building and storing a proper database, the same one for backtest and live, is a different job, and the subject of **Quant Lake**.
- **Programme** : [QUANT LAKE LINK]
- **Coupon for students of this course** : `[COUPON CODE]`

## The sources

| Data | Where | Free? | Use |
| --- | --- | --- | --- |
| Crypto OHLCV, spot and perps | Binance API https://binance-docs.github.io/apidocs/futures/en/ · `ccxt` https://github.com/ccxt/ccxt | yes | Universe of the momentum strategy |
| Crypto funding rates | Binance / Bybit API · Coinglass https://www.coinglass.com/FundingRate | yes | Funding in the P&L (instrument trap) |
| Crypto open interest, liquidations | Coinglass · exchange APIs | partial | Positioning, conditioning |
| Historical crypto volumes (for point-in-time universes) | Binance API (klines quote volume) · CoinGecko https://www.coingecko.com/en/api | yes | Rebuild who was in the top N at each date |
| Futures continuous series | Nasdaq Data Link https://data.nasdaq.com · Databento https://databento.com · Norgate https://norgatedata.com | paid | Trend and carry on futures |
| Futures term structure | CME settlements https://www.cmegroup.com/market-data · Databento | paid | Carry (roll yield) |
| Equity prices | `yfinance` https://github.com/ranaroussi/yfinance · Tiingo https://www.tiingo.com | yes / cheap | Pre-FOMC drift on equity indices |
| FX minute bid/ask | Dukascopy https://www.dukascopy.com/swiss/english/marketwatch/historical/ | yes | Event strategies with real spreads |
| Macro series | FRED https://fred.stlouisfed.org | yes | Regime conditioning |
| FOMC calendar | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm | yes | Event windows |
| Economic calendar (CPI, NFP, ECB) | Investing.com calendar · FRED release calendar | yes | Other event strategies |
| Positioning (COT) | CFTC https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm | yes | Contrarian and flow ideas |
| Implied vol | CBOE VIX https://www.cboe.com/tradable_products/vix/ · Deribit DVOL for crypto | yes | Regime tables |

## Traps
- **Survivorship** : today's top 20 crypto is not the top 20 of 2020. Rebuild the universe by date, or at least know you did not. In the course, the frozen universe makes almost all its P&L on price, the honest one a third on funding: same code, different story.
- **Price return ≠ position return** : funding, roll, dividends, coupons, and the spread you actually pay.
- **Thin early history** : crypto before 2019, most perps before 2021. Weight your conclusions by the number of observations.
- **Look-ahead in the universe itself** : if membership uses volume, the volume must be known at the date, not computed over the whole sample.

Related: [[Strategy Families]] · [[Glossary]]
