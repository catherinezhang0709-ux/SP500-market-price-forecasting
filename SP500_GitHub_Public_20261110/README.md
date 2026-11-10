# S&P 500 Market Price Forecasting
IFTE0007 coursework research. Single-factor20-day volatility OLS predicts a simple return over six equity sessions using a rolling three-calendar-year training window and daily origins.

**Draft: no final20November forecast or group approval has been recorded.** Information cutoff:13November2026 12:00UTC. Target: official S&P500 price-index close20November2026 16:00EST (21:00UTC), in index points.

Repository: https://github.com/catherinezhang0709-ux/SP500-market-price-forecasting

## Reproduce the public example
Prepare Python3.12 and install dependencies once:
```
python -m pip install -r model/requirements.lock
python model/model.py --prices data/SYNTHETIC_DEMO_NOT_MARKET_DATA.csv --asof 2026-11-06T16:25:00Z --output reproduced_demo
python reproduction/check_demo.py reproduced_demo
```
Use a new output folder on each run. The calculation reads saved local files, needs no account or live AI subscription, and does not make network data requests. Installation may require internet. Exact observed software versions are recorded in reproduction/.

**The public CSV is synthetic and is not market data.** It demonstrates the calculation and timing controls, not the real-market forecast, fitted coefficients or reported validation numbers. See data/DATA_ACCESS.md. Restricted input data remain excluded. A marker can read all public code and evidence without signing in, at the public repository linked below.

## Method
r_i = ln(P_i / P_(i-1)); sigma20 = population standard deviation of20 daily log returns, unannualized. Rhat6 = alpha + beta*sigma20; F = baseline*(1+Rhat6), round only at the end. An intercept and unrestricted slope enter unpenalized OLS. Training labels must be matured and target strictly before the current baseline. Historical next-session06NY availability is assumed, not certified historical publication timing.

## Evidence and limitations
- evidence/validation/: aggregate multi-year, half-year and monthly results, dependence-aware checks and rejected shrinkage.
- agent/: selected instructions translated into English, decisions and corrections.
- reproduction/: a genuine synthetic example execution, versions and deterministic output checker.
- final_forecast/: intentionally pending record and remaining work.

Codex inspected sources, invoked Python and checked calculations. Human members remain responsible for reasoning, lawful data sharing and final approval. The public example is a new packaging run, not an original live prediction transcript. Historical research selected among inspected alternatives and cannot establish an independent out-of-sample edge. Volatility estimates magnitude more naturally than direction, overlapping labels are dependent, and recent unchanged-price forecasts can perform better.

## Before submission
Replace pending fields using only cutoff-available evidence, obtain group approval, align report/slide/record values, resolve access to any restricted evidence, and preserve the final commit SHA. The report must contain the actual clickable repository URL. No final value is invented here.
