import json, glob, os
from collections import Counter
V9='/Volumes/OZTURK/_projects/prose_generation/_commentary/v9'
def use(f):
    t=Counter()
    for line in open(f,errors='ignore'):
        try: e=json.loads(line)
        except: continue
        if e.get('type')=='turn.completed':
            u=e['usage']; t['in']+=u.get('input_tokens',0); t['cached']+=u.get('cached_input_tokens',0); t['out']+=u.get('output_tokens',0); t['reason']+=u.get('reasoning_output_tokens',0); t['sessions']+=1
    return t
def cost(t, pin=0.20, pout=1.20, cached_frac=0.10):
    return ((t['in']-t['cached'])*pin + t['cached']*pin*cached_frac + t['out']*pout)/1e6
for sa in sorted(os.listdir(V9+'/lines/work'), key=lambda x:[int(p) for p in x.split('_')]):
    lines=Counter(); net=Counter()
    for f in glob.glob(f'{V9}/lines/work/{sa}/logs/*.jsonl'): lines+=use(f)
    for f in glob.glob(f'{V9}/network/out/{sa}/luna/*.log.jsonl'): net+=use(f)
    if lines or net:
        print(f"{sa}: lines sessions {lines['sessions']} in {lines['in']} out {lines['out']} ${cost(lines):.2f} | netpass in {net['in']} out {net['out']} ${cost(net):.2f} | total Luna-price ${cost(lines)+cost(net):.2f}")
# findings lane archive 29:38
t=Counter()
for f in glob.glob(f'{V9}/luna/work/29_38.archive-20260924-222824/logs/*.jsonl'): t+=use(f)
print('findings-lane 29:38 archive', dict(t), f"${cost(t):.2f}")
