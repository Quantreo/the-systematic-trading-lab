# The Systematic Trading Lab

The research vault and notebooks of the course **[The Systematic Trading Lab](https://www.quantreo.com/systematic-trading-lab/)**: find, design, diagnose and document a systematic strategy, the way a desk does, then decide if it deserves a place in a portfolio.

## What is inside

| Folder | What it holds |
| --- | --- |
| `vault/` | An Obsidian vault: idea journal, strategy sheets, research log, portfolio, templates and toolbox. Open it with *File → Open folder as vault*. |
| `data_portfolio/` | Daily returns of two crypto books, of Crypto XS Momentum, and the FOMC Drift trades. Used by notebook 03, no download needed. |
| `notebooks/` | `01_fomc_drift`: a strategy tested and killed. `02_crypto_xs_momentum`: a strategy built brick by brick. `02_tutorial_step_by_step`: the same, every step drawn on real data. `03_portfolio`: what a strategy is worth to a book, how to combine, when to cut. |
| `data/` | The scripts that download the market data, and their sources. |

## Setup

Python 3.12.

```
pip install -r requirements.txt
python data/get_fomc_minute.py      # FOMC Drift
python data/get_crypto_daily.py     # Crypto XS Momentum
```

The market data is not in this repository: you download it from the original sources. See `data/SOURCES.md` for the sources and their terms of use.

## The course

The videos, exercises and Discord are in the course: [quantreo.com/systematic-trading-lab](https://www.quantreo.com/systematic-trading-lab/)

## Disclaimer

Educational material only. Nothing here is investment advice, and no strategy in this repository is a recommendation to trade.
