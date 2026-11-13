"""Offline real-aggregate reproduction. This does not reconstruct licensed raw observations."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, date, timedelta
import json, math
ROOT = Path(__file__).resolve().parents[1]
s = json.loads((ROOT/'data/frozen_aggregate_inputs.json').read_text())
r = json.loads((ROOT/'final_forecast/forecast_record.json').read_text())
assert s['n']==747 and s['Sxx_centered']>0
beta=s['Sxy_centered']/s['Sxx_centered']; alpha=s['mean_y']-beta*s['mean_x']
f=s['factor']; assert f['ddof']==0 and f['n_log_returns']==20
vol=math.sqrt(f['sum_squared_centered_log_returns']/f['n_log_returns'])
ret=alpha+beta*vol; raw=s['baseline']*(1+ret)
def cents(x):return str(Decimal(str(x)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP))
assert abs(alpha-r['fit']['intercept'])<1e-12
assert abs(beta-r['fit']['volatility_coefficient'])<1e-10
assert abs(vol-r['fit']['latest_input_volatility20'])<1e-12
assert cents(raw)==r['forecast_value']=='7666.98'
cutoff=datetime.fromisoformat(r['information_cutoff_utc']);maximum=datetime.fromisoformat(r['coursework_maximum_information_cutoff_utc'].replace('Z','+00:00'))
assert datetime.fromisoformat('2026-11-13T11:00:00+00:00')<=cutoff<=maximum
assert s['last_training_target']<r['baseline_date']
assert datetime.fromisoformat(s['latest_training_label_available'])<=cutoff
# For this fixed interval there are no scheduled NYSE holidays. Saved six-session list
# is checked against weekdays; raw model.py uses exchange-calendars for general dates.
d=date.fromisoformat(r['baseline_date']);sessions=[]
while len(sessions)<6:
 d+=timedelta(days=1)
 if d.weekday()<5:sessions.append(d.isoformat())
assert sessions==r['sessions'] and sessions[-1]=='2026-11-20'
assert r['checks']['future_price_poison_passed'] is True
# Forecast sensitivity holds fitted coefficients fixed; not a prediction interval.
scenarios={label:cents(s['baseline']*(1+alpha+beta*vol*mult)) for label,mult in [('volatility_minus25pct',.75),('base',1),('volatility_plus25pct',1.25)]}
adverse=cents(s['baseline']*.97)
print(json.dumps({'training_n':s['n'],'intercept':alpha,'slope':beta,'volatility20':vol,'predicted_return':ret,'forecast_points':cents(raw),'unchanged_price_benchmark':cents(s['baseline']),'six_equity_sessions':sessions,'sensitivity_fixed_coefficients':scenarios,'adverse_scenario_3pct_below_baseline_not_forecast':adverse,'actual_information_cutoff_utc':r['information_cutoff_utc'],'scope':'real aggregate arithmetic only; raw-data and historical-backtest reconstruction excluded'},indent=2))
print('PASS: saved-aggregate OLS, factor, final point value, timing and six-session mapping.')
