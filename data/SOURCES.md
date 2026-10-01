# Data sources

The market data used in the notebooks is **not** included in this repository. You download it yourself, from the original sources, with the two scripts in this folder. It takes a few minutes, once.

```
pip install -r requirements.txt
python data/get_fomc_minute.py      # FOMC Drift  → data_fomc/dukascopy_fomc_minute.parquet
python data/get_crypto_daily.py     # Crypto XS Momentum → data_trend/prices_funding.parquet, data_trend/volume_all_perps.parquet
```

## FX minute bid/ask (FOMC Drift)
- **Source** : Dukascopy Bank SA, historical tick data, https://www.dukascopy.com
- **What the script builds** : for each scheduled FOMC announcement since 2012, from 25 hours before to 6 hours after, one row per minute with bid and ask open/high/low/close and the number of ticks. Six pairs: EUR/USD, GBP/USD, AUD/USD, NZD/USD, USD/CAD, USD/CHF.
- **Terms** : Dukascopy's terms of use apply to your download: https://www.dukascopy.com/swiss/english/legal-pages/terms-of-use/

## Crypto perpetuals, daily (Crypto XS Momentum)
- **Source** : Binance Vision public datasets, https://data.binance.vision, licensed CC BY-NC-SA 4.0 under the Binance Vision Dataset Terms.
- **What the script builds** : daily close, daily funding (sum of the day's payments) and daily quote volume for USDT perpetual futures, dead contracts included, from 2019-12-31.
- **Terms** : for your own non-commercial research and backtesting, as the Binance Vision Dataset Terms allow.

## Reference files included here
Small lists built for the course, not market data:
- `data_fomc/event_calendar.csv` : dates and times of scheduled FOMC and ECB announcements (public calendars of the Federal Reserve and the ECB).
- `data_trend/perp_meta.csv` : the list of USDT perpetual symbols, with type, sector and listing date.
- `data_trend/symbols_prices.csv` : the symbols for which prices and funding are downloaded.
- `data_trend/universe_today.csv` : today's largest names, used as the survivorship control.
