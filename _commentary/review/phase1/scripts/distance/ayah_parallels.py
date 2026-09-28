import csv, numpy as np
csv.field_size_limit(10**9)
D='/Volumes/OZTURK/_projects/quran-slm/artifacts/ayah_semantic_map/v1'
nodes=list(csv.DictReader(open(f'{D}/nodes.tsv',encoding='utf-8'),delimiter='\t'))
print(list(nodes[0].keys())[:12])
N=len(nodes)
key=[n.get('ayah_ref') or n.get('ref') or f"{n['surah']}:{n['ayah']}" for n in nodes]
ix={k:i for i,k in enumerate(key)}
sur=np.array([int(k.split(':')[0]) for k in key])
def load(n): return np.fromfile(f'{D}/{n}_raw_directional_rank.u16le',dtype='<u2').reshape(N,N)
R={s:load(s) for s in ['e5','neo','character']}
def rrf(M,a):
    out=M[a,:].astype(np.float32); inn=M[:,a].astype(np.float32); el=M[a,:]!=0
    r=np.zeros(N,np.float32); r[el]=0.5*(1/(10+out[el])+1/(10+inn[el])); return r
def ranks(a, sig):
    if sig=='nav': s=0.35*rrf(R['e5'],a)+0.35*rrf(R['neo'],a)+0.30*rrf(R['character'],a)
    else: s=rrf(R[sig],a)
    s[a]=-1
    o=np.argsort(-s,kind='stable'); rk=np.empty(N,int); rk[o]=np.arange(1,N+1)
    same=(sur==sur[a]); so=[j for j in o if same[j] and j!=a]; srk={j:i+1 for i,j in enumerate(so)}
    return rk, srk
cases={'4:34':['4:5','4:36','4:37','4:38','2:238','4:81','4:3','4:129','4:130','4:128','4:19','4:90','4:135','5:8','4:58'],
       '5:6':['5:89','5:91','5:11','35:10','5:8','5:97','5:95','5:5','5:1','2:185','4:43']}
for f,ts in cases.items():
    a=ix[f]
    for sig in ['nav','e5','neo','character']:
        rk,srk=ranks(a,sig)
        print(f, sig, ' '.join(f"{t}:{rk[ix[t]]}" + (f"(s{srk[ix[t]]})" if ix[t] in srk else '') for t in ts))
