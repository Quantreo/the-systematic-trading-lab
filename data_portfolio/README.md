# data_portfolio

Inputs of `notebooks/03_portfolio.ipynb`. No download needed.

| File | What it holds |
| --- | --- |
| `portfolio_1_returns.csv` | Daily net returns of a real crypto book: Carry, Momentum, Low vol. 2021-02 to 2026-08. |
| `portfolio_2_returns.csv` | The same book without its Momentum strategy. |
| `xs_momentum_returns.csv` | Daily P&L of Crypto XS Momentum from notebook 02: price, funding, costs, total. |
| `fomc_drift_trades.csv` | The 117 basket returns of FOMC Drift from notebook 01, one row per meeting. |

Returns are in fractions (0.01 = 1 %), each strategy at its own volatility. The notebook rescales them.
