import glob, csv, collections, itertools, random, json, numpy as np
csv.field_size_limit(10**9)
SLM='/Volumes/OZTURK/_projects/quran-slm'
cat=json.load(open(f'{SLM}/artifacts/corpus_network/catalog.json'))['cards']; N=len(cat)
idx={(c['source_root_id'],c['branch_id']):c['global_index'] for c in cat}
def load(p): return np.fromfile(p,dtype='<u2').reshape(N,N)
E5=load(f'{SLM}/artifacts/corpus_network/e5_directional_rank.u16le'); CH=load(f'{SLM}/artifacts/corpus_network/character_directional_rank.u16le'); NEO=load(f'{SLM}/artifacts/corpus_ensemble/neoarabert_directional_rank.u16le')
def rrf(R,a):
    out=R[a,:].astype(np.float32); inn=R[:,a].astype(np.float32); el=R[a,:]!=0
    res=np.zeros(N,np.float32); res[el]=0.5*(1/(10+out[el])+1/(10+inn[el])); return res,el
cache={}
def fr(a):
    if a not in cache:
        e,el=rrf(E5,a); c,_=rrf(CH,a); n,_=rrf(NEO,a); s=0.35*e+0.35*n+0.3*c; s[~el]=-1; s[a]=-1
        o=np.argsort(-s,kind='stable'); rk=np.empty(N,np.int64); rk[o]=np.arange(1,N+1); cache[a]=rk
        if len(cache)>400: cache.pop(next(iter(cache)))
    return cache[a]
V='/Volumes/OZTURK/_projects/latent_activation/_status/v12_cross_run'
F=collections.defaultdict(set); G={}
for f in glob.glob(f'{V}/s[0-9][0-9][0-9]/derived/finding_word_branches.v3.tsv'):
    for r in csv.DictReader(open(f,encoding='utf-8'),delimiter='\t'):
        k=(f,r['finding_id']); G[k]=r['grade']; F[k].add((r['root_id'],r['branch_id']))
pairs=collections.defaultdict(set)
for k,v in F.items():
    for a,b in itertools.combinations(sorted(v),2):
        if a[0]!=b[0] and a in idx and b in idx: pairs[G[k]].add((idx[a],idx[b]))
random.seed(5)
for g in ['strong','weak','reject']:
    P=list(pairs[g]); P=random.sample(P,min(2500,len(P)))
    P.sort()
    rks=[min(fr(a)[b],fr(b)[a]) for a,b in P]
    v=np.array(rks); print(g,'pairs total',len(pairs[g]),'sampled',len(v),'median best-direction fused rank',int(np.median(v)),'share<=10',round(float(np.mean(v<=10)),3),'<=100',round(float(np.mean(v<=100)),3),'<=1000',round(float(np.mean(v<=1000)),3))
# random baseline
rs=[]
for _ in range(1500):
    a,b=random.randrange(N),random.randrange(N)
    if cat[a]['surface_root_key']!=cat[b]['surface_root_key']: rs.append(min(fr(a)[b],fr(b)[a]))
v=np.array(rs); print('random median',int(np.median(v)),'share<=100',round(float(np.mean(v<=100)),3))
