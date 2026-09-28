import json, glob, collections
V15='/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/frames/out'
tags=collections.defaultdict(set)
for f in glob.glob(f'{V15}/*.json'):
    for it in json.load(open(f))['items']:
        for fr in it['frames']: tags[it['key']].add((fr['frame'],fr['role']))
rows=json.load(open('gold_ranks.json'))
def k(d): return d.replace(':',' ')
res=collections.Counter(); per=[]
for x in rows:
    if not x['elig']: continue
    A=tags.get(k(x['a']),set()); B=tags.get(k(x['b']),set())
    ca={t for t in A if not t[0].startswith(('moral.','divine.'))}; cb={t for t in B if not t[0].startswith(('moral.','divine.'))}
    sc=({t[0] for t in A}&{t[0] for t in B}); scc=({t[0] for t in ca}&{t[0] for t in cb})
    dom=({t[0].split('.')[0] for t in ca}&{t[0].split('.')[0] for t in cb})
    slm=min(x['local'])<=10
    res['pairs']+=1; res['same_scene_any']+=bool(sc); res['same_concrete_scene']+=bool(scc); res['same_concrete_domain']+=bool(dom); res['slm_local<=10']+=slm
    res['scene_or_slm']+=bool(scc) or slm; res['domain_or_slm']+=bool(dom) or slm
    per.append((x['g'],x['a'],x['b'],sorted(scc)[:3],sorted(dom)[:3],min(x['local'])))
print(dict(res))
for p in per: print(p)
