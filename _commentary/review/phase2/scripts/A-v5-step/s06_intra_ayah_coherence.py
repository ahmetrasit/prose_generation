# Script layer test: neighbour-activated branches. For each root X in the ayah (and optionally ±1 ayat),
# rank X's branches by their best quran-slm fused affinity (0.35 E5 + 0.35 Neo + 0.30 char, symmetric RRF)
# with any branch of the OTHER roots of the ayah. Reports where the watch-case branches land.
import csv, json, collections, sys
import numpy as np
csv.field_size_limit(10**9)
SLM='/Volumes/OZTURK/_projects/quran-slm'
cat=json.load(open(f'{SLM}/artifacts/corpus_network/catalog.json'))['cards']; N=len(cat)
gi={(c['source_root_id'],c['branch_id']):c['global_index'] for c in cat}
by_rootkey=collections.defaultdict(list)
for c in cat: by_rootkey[c['surface_root_key']].append(c['global_index'])
lab={c['global_index']:f"{c['surface_root_key']} {c['branch_id']}" for c in cat}
def load(p): return np.fromfile(p,dtype='<u2').reshape(N,N)
E5=load(f'{SLM}/artifacts/corpus_network/e5_directional_rank.u16le'); CH=load(f'{SLM}/artifacts/corpus_network/character_directional_rank.u16le'); NEO=load(f'{SLM}/artifacts/corpus_ensemble/neoarabert_directional_rank.u16le')
def rrfM(R,A,B):
    X=R[np.ix_(A,B)].astype(np.float32); Y=R[np.ix_(B,A)].astype(np.float32).T
    s=0.5*(1/(10+X)+1/(10+Y)); s[(X==0)&(Y==0)]=0; return s
def fused(A,B): return 0.35*rrfM(E5,A,B)+0.35*rrfM(NEO,A,B)+0.30*rrfM(CH,A,B)
QRA=collections.defaultdict(list)
for r in csv.DictReader(open(f'{SLM}/resources/source/qac_root_ayah.tsv',encoding='utf-8'),delimiter='\t'): QRA[r['ayah_ref']].append(r['root_norm'])
def run(ref, window=0, watch=()):
    s,a=map(int,ref.split(':'))
    roots=list(dict.fromkeys(QRA[ref])); ctx=[]
    for k in range(a-window,a+window+1):
        if k!=a: ctx+=QRA.get(f'{s}:{k}',[])
    allr=[r for r in dict.fromkeys(roots+ctx) if r in by_rootkey]
    out={}
    for X in roots:
        if X not in by_rootkey: continue
        A=by_rootkey[X]; others=[i for r in allr if r!=X for i in by_rootkey[r]]
        if not others: continue
        S=fused(A,others); best=S.max(axis=1); arg=S.argmax(axis=1)
        order=np.argsort(-best)
        out[X]=[(lab[A[i]],round(float(best[i]),4),lab[others[arg[i]]],rank+1,len(A)) for rank,i in enumerate(order)]
    return out
if __name__=='__main__':
    cases=[('29:38',0,['س ب ل B010','ز ي ن B002','ب ص ر B001']),('29:38',1,['س ب ل B010']),('1:7',0,['ض ل ل B005']),('1:6',0,['ص ر ط B002','ق و م B012']),('5:6',0,['ر ف ق B004','ك ع ب B001']),('18:86',0,['ح م ء B001','ع ي ن B008']),('18:96',0,['ن ف خ B001'])]
    for ref,w,watch in cases:
        o=run(ref,w)
        print(f'### {ref} window ±{w}')
        for X,rows in o.items():
            for r in rows:
                if r[0] in watch: print('   watch',r[0],'rank',r[3],'of',r[4],'best partner',r[2],'score',r[1])
        # top-3 non-B001 per root
        for X,rows in o.items():
            print('   ',X,'top:',', '.join(f"{r[0].split()[-1]}~{r[2]}" for r in rows[:4]))
