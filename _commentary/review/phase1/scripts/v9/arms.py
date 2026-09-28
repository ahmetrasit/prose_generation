import json, re, glob, os
from pathlib import Path
W = Path('/Volumes/OZTURK/_projects/prose_generation/_commentary/v9/lines/work')
rows=[]
for sa in sorted(os.listdir(W)):
    sd = W/sa/'synth'
    if not sd.exists(): continue
    for arm in sorted(os.listdir(sd)):
        d = sd/arm
        cost=inp=cw=cr=out=th=None; model=''
        lj = d/'run.log.json'
        if lj.exists():
            try:
                j=json.loads(lj.read_text())
                cost=j.get('total_cost_usd'); u=j.get('usage',{})
                inp=u.get('input_tokens'); cw=u.get('cache_creation_input_tokens'); cr=u.get('cache_read_input_tokens'); out=u.get('output_tokens')
                th=(u.get('output_tokens_details') or {}).get('thinking_tokens')
                model=','.join(j.get('modelUsage',{}).keys()) or ('ERR' if j.get('error') else '')
                if j.get('is_error'): model+=' is_error'
            except Exception as e:
                model='parse-err'
        else:
            # codex jsonl
            tot={'input':0,'cached':0,'output':0,'reasoning':0}
            for lf in d.glob('*.jsonl'):
                for line in lf.read_text(errors='ignore').splitlines():
                    try: e=json.loads(line)
                    except: continue
                    if e.get('type')=='turn.completed':
                        u=e.get('usage',{})
                        tot['input']+=u.get('input_tokens',0); tot['cached']+=u.get('cached_input_tokens',0); tot['output']+=u.get('output_tokens',0); tot['reasoning']+=u.get('reasoning_output_tokens',0)
            inp,cr,out,th=tot['input'],tot['cached'],tot['output'],tot['reasoning']; model='codex'
        rd = list(d.glob('*.reading.tr.md'))
        words = len(rd[0].read_text().split()) if rd else 0
        refs = len(set(re.findall(r'\b(\d{1,3}:\d{1,3})\b', rd[0].read_text()))) if rd else 0
        rows.append((sa,arm,model,cost,inp,cw,cr,out,th,words,refs))
for r in rows:
    print('\t'.join('' if x is None else (f'{x:.2f}' if isinstance(x,float) else str(x)) for x in r))
