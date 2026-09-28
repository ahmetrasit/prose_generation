# Do pushed inter-ayah prior labels act as filters in v5? Compare label distribution of pushed rows vs rows cited in discovery.
import json, glob, re, collections, os
V5='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
pushed=collections.Counter(); cited=collections.Counter(); n=0
for p in glob.glob(V5+'/raw/*/*/*/global.discovery.json'):
    aid,sd,ay=p[len(V5)+5:].split('/')[:3]
    if 'basmala' in aid: continue
    cmap={}
    for lane in ('macro','global'):
        q=f'{V5}/input/{aid}/{sd}/{ay}/{lane}.discovery.prompt.md'
        if not os.path.exists(q): continue
        t=open(q,encoding='utf-8').read(); i=t.find('<lane_packet_json>'); j=t.find('</lane_packet_json>')
        pk=json.loads(t[i+len('<lane_packet_json>'):j])
        for r in pk.get('connection_registry',[]):
            lab=r.get('prior_label') or 'none'
            pushed[(lane,lab)]+=1
            for k in ('connection_ref','connection_evidence_ref'):
                if r.get(k): cmap[r[k]]=(lane,lab)
    if not cmap: continue
    used=set()
    for lane in ('micro','macro','global'):
        f=f'{V5}/raw/{aid}/{sd}/{ay}/{lane}.discovery.json'
        if os.path.exists(f): used|=set(re.findall(r'conn(?:_ev)?_[0-9a-f]{20}',open(f,encoding='utf-8').read()))
    seen=set()
    for c in used:
        if c in cmap and cmap[c] not in seen or True:
            if c in cmap: cited[cmap[c]]+=1
    n+=1
print('ayat',n)
for lane in ('macro','global'):
    tp=sum(v for k,v in pushed.items() if k[0]==lane); tc=sum(v for k,v in cited.items() if k[0]==lane)
    for lab in ('strong','medium','weak','no value','none'):
        a=pushed[(lane,lab)]; b=cited[(lane,lab)]
        if a: print(lane,lab,'pushed',a,f'({a/tp:.1%})','cited',b,f'({(b/tc if tc else 0):.1%})','cite rate',f'{b/a:.1%}')
