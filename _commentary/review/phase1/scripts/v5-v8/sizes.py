import json,os,statistics as st,collections
D=os.path.dirname(__file__)
rows=json.load(open(os.path.join(D,'files.json')))
g=collections.defaultdict(list)
for layer,rel,f,sz in rows:
    aid=rel.split(os.sep)[0]
    if aid.endswith('no-fatiha'): continue
    import re
    k=(layer,re.sub(r'^\d+_\d+\.','S_A.',f))
    g[k].append(sz)
for k in sorted(g):
    v=g[k]
    if len(v)<5: continue
    v=sorted(v)
    print(f'{k[0]:10s} {k[1]:40s} n={len(v):5d} median={st.median(v)/1000:8.1f}KB p10={v[len(v)//10]/1000:8.1f} p90={v[9*len(v)//10]/1000:8.1f} max={v[-1]/1000:8.1f} total={sum(v)/1e6:7.1f}MB')
