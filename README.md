# Group 10 — S&P 500 Forecast Evidence
Frozen numerical forecast: **7,666.98 index points**. Official S&P Dow Jones Indices price-index close on 20 November 2026, 16:00 EST / 21:00 UTC. Actual information cutoff and issue time: **13 November 2026 11:45:32 UTC**, earlier than the coursework noon maximum. No later market inputs used.

## Reproduce offline without an account or AI
1. Extract this ZIP to any folder.
2. Use Python 3.12 (the calculation uses only the standard library).
3. From the extracted folder run:
```
python3 reproduction/verify_hashes.py
python3 reproduction/reproduce_forecast.py
```
Both commands should report PASS; forecast must be 7666.98. They do not fetch data or call an AI. Output includes OLS coefficients, factor, return, sensitivity, six-session dates and flat-price benchmark. Execution transcript and software versions are included. Dependency installation is only needed for optional raw-data refitting with model/model.py.

## Reproduction scope
The frozen real aggregate inputs reproduce OLS coefficients, volatility arithmetic and final point forecast. Restricted underlying price observations are excluded; the CSV sample is synthetic and cannot fit the real model. Raw-source verification, full training-row reconstruction and historical backtest reruns require lawful access to the private original snapshot. This limitation is explicit, not concealed. See data/DATA_ACCESS.md.

Model: population standard deviation of 20 daily log returns (21 closes), unannualized; unpenalized OLS with intercept; daily 12 UTC origins; rolling three calendar years; 747 fully matured labels; six subsequent XNYS sessions. No discretionary adjustment. Historical release availability is conservatively reconstructed and not certified.

## Evidence and limitations
- final_forecast/: binding-value candidate record and cover text; genuine group approval remains to be completed.
- model/: unchanged raw-fitting code and fixed specification.
- data/: real sufficient statistics and explicitly fictional schema sample.
- agent/: instructions, decisions/corrections, labelled workflow, translated chat video and selected final-run transcript.
- evidence/: dated source receipt and historical validation summaries, including failures against the unchanged-price benchmark.
- reproduction/: saved-input program, tests, actual log and versions.
- AUDIT_CHECKLIST.md: item-by-item assessment and remaining submission actions.

Nov12 close 7592.40 was verified via Yahoo indexed history and an earlier AP report; FRED still ended Nov11. Primary index-provider confirmation and historical first-publication certification are not claimed. No 20 November realised result exists in this package.

## Submission and repository access
Under the teacher clarification supplied by the group, upload only the Final Report (Word or PDF) to the coursework system. Put a clickable GitHub repository hyperlink on the first report page. Code and supporting evidence are hosted here; slides and the evidence ZIP do not require separate coursework upload under that clarification. Slides remain useful for the presentation. A downloadable ZIP may be retained as a convenience.

The unique binding forecast on the report cover must match 7666.98, with the correct target and actual information cutoff. Human submission approval and actual contribution statements remain to be completed. Do not add post-cutoff market inputs.

Repository: https://github.com/catherinezhang0709-ux/SP500-market-price-forecasting . This local folder has not been uploaded automatically. The older SP500_GitHub_Public_20261110 directory is superseded for final forecast reproduction. Report and presentation exports are not included here as final documents.

The chat video is an edited translation/reconstruction of earlier work and its historical worked example is not the final forecast. reproduction/run_transcript.txt is the actual packaging reproduction log. No account credentials, financial login, paid API or live AI service is needed.

Integrity checking ignores only OS metadata (.DS_Store, Thumbs.db) and Python __pycache__ directories, which may be created after extraction. All declared payload hashes still must match. See reproduction/REQUIREMENT_RECHECK.json for the second audit.
