import json, numpy as np
SLM='/Volumes/OZTURK/_projects/quran-slm/artifacts/surah_networks_global_ensemble'
def view(s):
    c=json.load(open(f'{SLM}/s{s:03d}/catalog.json')); A=np.load(f'{SLM}/s{s:03d}/affinity.npy')
    return {b['node_id']:b['index'] for b in c['branches']}, np.array([b['root'] for b in c['branches']]), A, c
def lr(v,a,b):
    k,roots,A,_=v; ia,ib=k[a],k[b]; row=A[ia].copy(); row[roots==roots[ia]]=-1
    return int((row>row[ib]).sum())+1, int((roots!=roots[ia]).sum())
v29=view(29)
pairs29=[('quranic:root_000879:B006','quranic:root_000671:B001'),('quranic:root_000879:B006','quranic:root_000671:B004'),('quranic:root_000879:B003','quranic:root_000671:B001')]
for a,b in pairs29:
    if a in v29[0] and b in v29[0]:
        r1,n=lr(v29,a,b); r2,_=lr(v29,b,a); print('S29',a.split(':',1)[1],'<->',b.split(':',1)[1],'local',r1,r2,'of',n)
    else: print('S29 missing', a in v29[0], b in v29[0])
print('S29 branches', len(v29[1]))
v100=view(100)
nodes=['quranic:root_000993:B002','quranic:root_000993:B001','quranic:root_001544:B004','quranic:root_000210:B001','quranic:root_000210:B002','quranic:root_000130:B001','quranic:root_000330:B001','quranic:root_000330:B002']
for a in nodes:
    print(a.split(':',1)[1], a in v100[0])
import itertools
for a,b in itertools.combinations(nodes,2):
    if a in v100[0] and b in v100[0] and v100[1][v100[0][a]]!=v100[1][v100[0][b]]:
        r1,n=lr(v100,a,b); r2,_=lr(v100,b,a); print('S100',a.split(':',1)[1],'<->',b.split(':',1)[1],'local',r1,r2,'of',n)
