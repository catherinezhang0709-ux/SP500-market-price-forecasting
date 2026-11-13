# Coursework evidence audit — Group 10
This is repository evidence accompanying the separately submitted Final Report. PASS means the named file/check is present; it does not certify data licensing or genuine human approval.

| Requirement | Result | Evidence or remaining action |
|---|---|---|
| Correct market and unit | PASS | S&P 500 price index; index points; no ETF/futures substitution |
| One point forecast, two decimals | PASS IN EVIDENCE | 7666.98 in final_forecast/forecast_record.json |
| Correct target | PASS | Official 20 Nov 2026 16:00 EST / 21:00 UTC close |
| Information boundary | PASS LOGICAL CHECK | Actual cutoff 13 Nov 11:45:32 UTC, before noon; no later inputs added |
| Frozen input snapshot | QUALIFIED | Real aggregate inputs frozen and hashed; licensed raw price library excluded |
| Raw data redistribution | RESTRICTED | Permission unconfirmed; labelled synthetic schema sample supplied |
| Source URLs, retrieval time, latest observation | PRESENT WITH CAVEAT | source receipt; original publication time not independently certified |
| Nov12 close primary-source confirmation | UNRESOLVED | AP/Yahoo match 7592.40; FRED check still ends Nov11 |
| Factor definition | PASS | 20 daily log returns, population std, 21 closes, no annualisation |
| Mechanism and expected sign | PARTIAL PACKAGE SCOPE | Fitted positive slope; weak short-horizon directional rationale must remain explained critically in report |
| Transparent return-to-level mapping | PASS | Code recomputes alpha, beta, factor, return, 7666.98 |
| Fixed training/horizon | PASS | Daily rolling 3 years, 747 mature pairs; six equity sessions |
| Benchmark | PRESENT | Flat baseline 7592.40; historical benchmark summaries preserved |
| Chronological evaluation and failures | QUALIFIED | Historical diagnostic summaries present; full historical reruns need licensed inputs and original project runners |
| Sensitivity/adverse scenario | PASS | ±25% factor with fixed coefficients; separate -3% baseline stress |
| Agent instructions and decisions | PASS | Translated selected prompts; decision/correction record |
| Agent actual tool use | PRESENT | Selected final-run summary and actual packaging calculation transcript; not full original chat export |
| Labelled workflow diagram | PRESENT | agent/WORKFLOW_DIAGRAM.md (Mermaid source) |
| Run transcript/screenshots | PASS | Actual command/output transcript; edited 60s chat video additionally supplied |
| Offline marker reproduction | PASS FOR AGGREGATE CALCULATION | Standard-library Python; no account, network or AI needed |
| Full raw-price fit and all backtests | NOT REPRODUCIBLE FROM THIS ZIP ALONE | Disclosed restricted-data limitation; optional raw-fitting instructions supplied |
| Software versions | PASS | software_versions.json and requirements-full.lock |
| Credentials and restricted full data | PASS SCAN | No detected credential patterns, full price rows or training-pair records |
| SHA256 integrity/ZIP extraction | PASS AFTER PACKAGING | Manifest, CRC and isolated extracted-copy reproduction tested |
| Final report cover matches forecast | HUMAN ACTION REQUIRED | Update cover to 7666.98, target and actual 11:45:32 cutoff; do not submit old pending cover |
| Report <=2400 words, references, AI declaration | NOT RECHECKED IN THIS EVIDENCE TASK | Final report PDF remains a separate required deliverable |
| Presentation matches frozen forecast | HUMAN ACTION REQUIRED | Update report/slides using these frozen inputs only; all members contribute |
| Genuine group approval | HUMAN ACTION REQUIRED | Approval template blank; no approval invented |
| Contribution statement | HUMAN ACTION REQUIRED | Confirm actual work against planned allocation |
| Clickable accessible GitHub link | LINK PROVIDED; ONLINE VERSION NOT UPDATED | Existing repository link in README; ensure final report contains it and online evidence version matches |
| Submit Final Report with GitHub hyperlink | HUMAN ACTION REQUIRED | Teacher clarification: coursework system accepts report only; code/evidence in linked GitHub repository; no separate PPT/ZIP upload required |

## Final numerical checks
Reproduced point = 7666.98; flat benchmark = 7592.40.
Volatility -25% = 7641.38; +25% = 7692.57 (fixed coefficients; not a prediction interval).
Adverse scenario -3% baseline = 7364.63 (stress scenario; not a second forecast).
QR and future-price poisoning passed in original local run. Exact historical first-publication vintages are not certified. Forecast accuracy is unknown until the target outcome; no guarantee of beating a benchmark or reaching a mark.

## Submission actions
1. Review/approve the candidate and complete genuine approval/contributions.
2. Put the unique point 7666.98 on final report cover with correct market/unit/target and actual cutoff. Ensure slides agree.
3. Retain source/rights and reproducibility caveats. Do not call aggregate reproduction a full raw-data refit.
4. Confirm the GitHub repository is accessible and contains the intended evidence/code version, excluding restricted inputs.
5. Upload the Final Report (Word or PDF) through the module channel by 13 November 17:00 GMT. Put the clickable accessible repository link on its first page. Keep slides for presentation; no separate PPT/ZIP upload is required under the supplied clarification. No post-cutoff market inputs.
