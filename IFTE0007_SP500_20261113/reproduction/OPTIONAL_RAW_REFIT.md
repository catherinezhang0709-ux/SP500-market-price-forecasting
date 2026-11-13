# Optional full raw-data refit (requires lawful data access)
The supplied synthetic CSV cannot be used for this real fit. Obtain the private price_snapshot.csv matching the SHA-256 in final_forecast/forecast_record.json using an authorised institutional channel.

Install the versions in reproduction/requirements-full.lock. From the package root:
```
python model/model.py --prices /path/to/lawfully_obtained/price_snapshot.csv --asof 2026-11-13T11:45:32Z --output reproduced_full_fit
```
Output directory must not already exist. This fits OLS, selects rows, calculates volatility and checks QR. The wrapper arithmetic is baseline*(1+intercept+volatility_coefficient*latest_input_volatility20), rounded only at the end to two decimals. The model.py fit-only legacy flag nov20_final_forecast_generated=False does not invalidate the separately calculated final point record.

Expected n=747, latest baseline=2026-11-12, 7592.40; last training target=2026-11-11. Compare coefficients to the final record. Actual final-run local checks already verified all training targets strictly precede the baseline and synthetic future target values do not affect the fit. These are logic checks, not certified historical data vintages.
