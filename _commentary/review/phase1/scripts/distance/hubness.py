import json, csv, numpy as np
csv.field_size_limit(10**9)
SLM='/Volumes/OZTURK/_projects/quran-slm'
cat=json.load(open(f'{SLM}/artifacts/corpus_network/catalog.json'))['cards']; N=len(cat)
img={r['node_id']:r['branch_image_ar'] for r in csv.DictReader(open(f'{SLM}/resources/source/corpus_branches_ar.tsv',encoding='utf-8'),delimiter='\t')}
def gini(x):
    x=np.sort(x); n=len(x); return (2*np.arange(1,n+1)-n-1).dot(x)/(n*x.sum())
for name,p in [('e5','corpus_network/e5'),('char','corpus_network/character'),('neo','corpus_ensemble/neoarabert')]:
    R=np.fromfile(f'{SLM}/artifacts/{p}_directional_rank.u16le',dtype='<u2').reshape(N,N)
    ind=np.zeros(N,int)
    for s in range(0,N,1024):
        blk=R[s:s+1024]; ind+=((blk>0)&(blk<=10)).sum(0)
    top=np.argsort(-ind)[:5]
    print(name,'top-10 in-degree: gini',round(gini(ind),3),'max',ind.max(),'zero in-degree cards',(ind==0).sum(), 'top hubs',[(cat[i]['display_key'],img[cat[i]['node_id']][:25],int(ind[i])) for i in top])
