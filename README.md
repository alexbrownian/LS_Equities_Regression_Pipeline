# LS Equities Regression Pipeline

there must be a more quantitative way to do L/S Equities

## Process: What This Project Does

This repository implements a full quantitative long/short equities workflow:

1. **Data ingestion ([01_data_ingestion.ipynb](01_data_ingestion.ipynb))**

- Pulls and cleans price/fundamental data for the long candidate and short universe.
- Writes aligned datasets used by downstream notebooks.

2. **Factor analysis ([02_factor_analysis.ipynb](02_factor_analysis.ipynb))**

- Computes factor signals (for example momentum, value, quality, growth).
- Standardises and combines factors into cross-sectional scores.

3. **ML selection ([03_ml_selection.ipynb](03_ml_selection.ipynb))**

- Trains/validates a return-prediction model on engineered features.
- Produces model-implied rankings to complement factor scores.

4. **Portfolio construction ([04_portfolio_construction.ipynb](04_portfolio_construction.ipynb))**

- Combines factor and ML ranks into a long vs basket-of-shorts candidate table.
- Defines portfolio-level candidate weights/exposures and risk context.

5. **Pair screening and backtest ([05_backtesting.ipynb](05_backtesting.ipynb))**

- Moves from basket analysis to a specific single-stock pair based on best performance.
- Screens short candidates against GEVO using always-in spread Sharpe (primary).
- Chooses the best short, optimises long/short weight split, and evaluates timing signals.
- Saves artifacts such as `data/pair_screening.parquet`, `data/best_pair_bt.parquet`, and `data/best_pair_meta.json`.

6. **Reporting ([06_report.ipynb](06_report.ipynb))**

- Consolidates outputs into visuals/tables for communication.
- Exports report artifacts to `outputs/` (for example `full_report.html`, `pitch_table.csv`).
- Investor-facing summary: [GEVO_PDM_Investor_Report.md](GEVO_PDM_Investor_Report.md).

In short, notebooks 01-04 build and evaluate a long vs short-basket portfolio, and notebook 05 narrows this to the best-performing specific long/short stock pair with reproducible outputs.

## Outcome Summary

This project builds an end-to-end long/short equities research workflow across data ingestion, factor analysis, model selection, portfolio construction, backtesting, and reporting.

From the latest generated backtest artifacts:

- Best pair selected: **Long GEVO / Short PDM**
- Optimal weight split: **31.03% long / 68.97% short** (ratio = 0.45)
- Always-in spread performance:
  - Annual return: **13.06%**
  - Annual volatility: **32.63%**
  - Sharpe ratio: **0.2469**
  - Max drawdown: **-46.67%**
- Z-score strategy Sharpe: **0.0714**
- Current z-score / signal snapshot: **2.2124 / -1 (short spread)**

In short, the current pipeline identifies a statistically preferred long/short pair and sizing rule, with modest positive risk-adjusted performance in the always-in spread and weaker incremental value from timing via z-score triggers in this run.

For a concise investor-oriented writeup, see [GEVO_PDM_Investor_Report.md](GEVO_PDM_Investor_Report.md).
