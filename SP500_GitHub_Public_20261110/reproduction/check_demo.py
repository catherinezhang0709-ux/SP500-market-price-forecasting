from pathlib import Path
import sys,json,math
root=Path(__file__).resolve().parents[1]
a=json.loads((Path(sys.argv[1])/'fitted_model.json').read_text())
b=json.loads((root/'reproduction/expected_synthetic_fit/fitted_model.json').read_text())
for k,v in b.items():
 if isinstance(v,float):assert math.isclose(a[k],v,rel_tol=1e-10,abs_tol=1e-12),k
 else:assert a[k]==v,k
assert a['independent_QR_passed']
assert not a['nov20_final_forecast_generated']
print('PASS: synthetic example matches saved demonstration. This does not validate real-market accuracy.')
