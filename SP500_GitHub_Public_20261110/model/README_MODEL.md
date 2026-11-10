# Public repository note
This source README describes the private research snapshot. Real data and fit_snapshot_20261106 are deliberately absent from this public repository. Use the root README and synthetic reproduction command for public files.

# Selected model rule V1: single-factor volatility OLS
Model ID: SP500_VOL20_DAILY_OLS_ROLLING3Y_V1. This is the selected research model rule, not an approved final coursework forecast. Earlier research results remain preserved.

## Fixed specification
Daily log return: r_i = ln(P_i / P_(i-1)).
Factor: sigma20 = sqrt(sum((r_i - mean(r))^2) / 20). It uses 21 price-index closes to obtain 20 returns, with population standard deviation, no annualisation and decimal units.
Expected six-session simple return: Rhat = alpha + beta * sigma20.
Forecast level: F = P0 * (1 + Rhat), rounded to two decimal places only at the end.

## Training and timing
The underlying library contains approximately ten years of daily closes. Each fit uses eligible trading-day origins at 12:00 UTC within the preceding three calendar years, with at least 130 complete matured training pairs. The target is the sixth equity session after the baseline. Features must be available at each historical origin. Training labels must be available at fitting time, and their target dates must strictly precede the current baseline.

Historical price availability follows the assumed next-equity-session 06:00 New York rule. This is a conservative reconstruction, not certification of actual first-publication timestamps. The final model uses no interest-rate eligibility screen, momentum factor, Ridge penalty, SVR, shrinkage weight or manual adjustment.

## Saved research snapshot
As of 6 November 2026, 16:25 UTC: baseline 5 November, 7,353.73 points; 746 training pairs; latest training target 4 November.
Intercept = -0.0033238676973588732.
Volatility coefficient = 0.973737278415176.
Coefficients change when the rolling model refits. No new point forecast or final 20 November forecast is emitted by this snapshot code.

## Offline reproduction
From the package root, in a prepared Python environment:
```
python model/model.py --prices model/data/price_library.csv --asof 2026-11-06T16:25:00Z --output my_reproduced_fit
python reproduction/check_outputs.py my_reproduced_fit
```
The output directory must not already exist. Code reads local files only and needs no financial account, network data retrieval or live AI service. requirements.lock lists core dependencies; reproduction/software_versions.json and environment.freeze.txt record the packaging environment. Outputs include model parameters, selected training rows and source hashes.

## Evidence and limitations
validation/ preserves multi-year, half-year and monthly comparisons, failed shrinkage results and dependence-aware checks. Half-year MAPE is 1.3686% across 128 targets; monthly MAPE is 1.2936% across 23 targets. Recent unchanged-price performance can be stronger. The 5 November failure remains included.

Volatility describes risk magnitude more directly than return direction. Six-session labels overlap, repeated model selection creates hindsight bias, and these diagnostics are not untouched tests. No calibrated prediction interval, guaranteed accuracy or guaranteed coursework score is claimed.

Before submission, freeze cutoff-available inputs by 13 November 12:00 UTC, refit, calculate the unique 20 November forecast and obtain genuine student approval. The specification's final_forecast_value and final_group_approval remain null. Read data_notes/RIGHTS_AND_AVAILABILITY.md before sharing licensed inputs.
