"""Final research model rule. No automatic coursework submission forecast."""
import argparse,csv,json,math,hashlib,sys
from pathlib import Path
from datetime import datetime,time,timezone
from zoneinfo import ZoneInfo
import numpy as np
import exchange_calendars as xcals

MODEL_ID='SP500_VOL20_DAILY_OLS_ROLLING3Y_V1'

def boundary(at):
 try:return at.replace(year=at.year-3)
 except ValueError:return at.replace(year=at.year-3,day=28)

def volatility(levels):
 x=np.asarray(levels,float)
 if len(x)!=21 or not np.isfinite(x).all() or (x<=0).any():raise ValueError('Exactly21 finite positive closes required')
 return float(np.std(np.diff(np.log(x)),ddof=0))

def fit_model(price_file,asof):
 if asof.tzinfo is None:raise ValueError('Timezone-aware asof required')
 at=asof.astimezone(timezone.utc);prices={}
 with Path(price_file).open() as f:
  for r in csv.DictReader(f):
   d=r['observation_date'];v=float(r['SP500'])
   if d in prices or not math.isfinite(v) or v<=0:raise ValueError('Invalid or duplicate price')
   prices[d]=v
 if not prices:raise ValueError('Empty price file')
 # Coverage beyond latest observation is a scheduled calendar only, not future market data.
 end=f'{at.year+1}-01-31';cal=xcals.get_calendar('XNYS',start=min(prices),end=end);days=[d.date().isoformat() for d in cal.sessions];idx={d:i for i,d in enumerate(days)}
 if any(d not in idx for d in prices):raise ValueError('Price date not an XNYS session')
 def available(d):return datetime.combine(datetime.fromisoformat(days[idx[d]+1]).date(),time(6),ZoneInfo('America/New_York')).astimezone(timezone.utc)
 usable=[d for d in sorted(prices) if available(d)<=at]
 if not usable:raise ValueError('No completed available baseline')
 baseline=usable[-1];i=idx[baseline];window=days[i-20:i+1]
 if len(window)!=21 or any(d not in prices for d in window):raise ValueError('Incomplete latest price window')
 lower=boundary(at);pairs=[]
 for j,d in enumerate(days):
  if j<21 or d>at.date().isoformat():continue
  origin=datetime.combine(datetime.fromisoformat(d).date(),time(12),timezone.utc)
  if not lower<=origin<at:continue
  base=days[j-1];target=days[j+5]
  if target>=baseline or target not in prices or available(target)>at:continue
  w=days[j-21:j]
  if len(w)!=21 or any(t not in prices for t in w) or max(available(t) for t in w)>origin:continue
  pair={'origin':origin.isoformat(),'baseline':base,'target':target,'volatility20':volatility([prices[t] for t in w]),'future_return':prices[target]/prices[base]-1,'feature_available_at':available(base).isoformat(),'label_available_at':available(target).isoformat()}
  assert pair['feature_available_at']<=pair['origin'];pairs.append(pair)
 if len(pairs)<130:raise ValueError(f'Only{len(pairs)} mature training pairs; require130')
 x=np.array([[1,p['volatility20']] for p in pairs]);y=np.array([p['future_return'] for p in pairs]);beta,_,rank,_=np.linalg.lstsq(x,y,rcond=None)
 if rank!=2 or not np.isfinite(beta).all():raise ValueError('Invalid OLS fit')
 q,r=np.linalg.qr(x);assert np.max(abs(beta-np.linalg.solve(r,q.T@y)))<1e-10
 return {'model_id':MODEL_ID,'asof_utc':at.isoformat(),'latest_usable_baseline_date':baseline,'latest_usable_baseline':prices[baseline],'latest_input_volatility20':volatility([prices[d] for d in window]),'intercept':float(beta[0]),'volatility_coefficient':float(beta[1]),'training_count':len(pairs),'training_window_start':lower.isoformat(),'first_training_origin':pairs[0]['origin'],'last_training_origin':pairs[-1]['origin'],'last_training_target':max(p['target'] for p in pairs),'latest_training_label_available':max(p['label_available_at'] for p in pairs),'independent_QR_passed':True,'strict_PIT_certified':False,'nov20_final_forecast_generated':False},pairs

def main():
 p=argparse.ArgumentParser();p.add_argument('--prices',type=Path,default=Path(__file__).parent/'data/price_library.csv');p.add_argument('--asof',required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 model,pairs=fit_model(a.prices,datetime.fromisoformat(a.asof.replace('Z','+00:00')));a.output.mkdir(parents=True,exist_ok=False)
 for name,value in [('fitted_model.json',model),('selected_training_pairs.json',pairs)]:
  with (a.output/name).open('x') as f:json.dump(value,f,indent=2)
 (a.output/'source_sha256.json').write_text(json.dumps({'prices':hashlib.sha256(a.prices.read_bytes()).hexdigest(),'model.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
 print(json.dumps(model,indent=2))
if __name__=='__main__':main()
