# Public data scope
Licensed raw WRDS/CRSP/S&P daily prices and observation-level training pairs are excluded from this public repository. The CSV sample is clearly labelled SYNTHETIC and illustrates schema only; it cannot fit the real three-year model. Do not present the sample as observed market data.

Real frozen sufficient statistics in frozen_aggregate_inputs.json reproduce the reported OLS coefficients, volatility arithmetic and final 7666.98 point forecast offline. They do not independently reconstruct raw observations, training-row selection or historical backtests. model/model.py and OPTIONAL_RAW_REFIT.md explain the separate raw-fitting route for a marker with lawful input access; full raw inputs are not included.

The group supplied a classmate's account of teacher clarification allowing raw data to be omitted in favour of code, running instructions and labelled synthetic inputs. That account is not a licence grant or direct written confirmation to this group. No rights to publish licensed raw data are asserted.

Historical availability remains reconstructed, not certified original first-release vintages. The data boundary and hashes refer to the original frozen calculation; documentation updates do not add later market data.
