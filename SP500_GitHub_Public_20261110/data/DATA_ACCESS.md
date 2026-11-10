# Data access and restrictions
The CSV in this folder is a deterministic synthetic example, not S&P 500 observations. It supports an offline demonstration of the full calculation, not reproduction of the reported real-market coefficients or validation metrics. No WRDS/CRSP, FRED/S&P price series, real selected training pairs or original restricted samples are uploaded here.

The private frozen research library remains in the local evidence package. It contains WRDS CRSP index1000502 historical observations, a saved FRED SP500 extension and an official S&P endpoint record. Its final row is5November2026. Redistribution permission has not been verified. The coursework allows labelled samples where redistribution is restricted. This repository deliberately uses a synthetic full-length sample rather than expose restricted records.

For an authorised marker with a lawful copy of the actual frozen data, use CSV columns observation_date, SP500, source and run model/model.py with --prices pointing to that file. The asof must remain fixed. Public aggregate validation files document results but cannot reconstruct the private data. Do not assume current downloads reproduce the same historical snapshot.

Source definitions:
- https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- https://fred.stlouisfed.org/series/SP500
- https://wrds-www.wharton.upenn.edu/ (institutional licensed access)

Historical first-publication timestamps and data vintages are not certified. Next-session06:00 New York availability is a documented reconstruction assumption.
