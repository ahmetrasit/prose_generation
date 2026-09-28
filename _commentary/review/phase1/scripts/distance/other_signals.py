import csv, collections, itertools, json
csv.field_size_limit(10**9)
V15='/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data'
W=list(csv.DictReader(open(f'{V15}/words.tsv',encoding='utf-8'),delimiter='\t'))
by_ayah=collections.defaultdict(set)
for w in W:
    for r in w['roots'].split('|'):
        r=r.strip()
        if r: by_ayah[(int(w['surah']),int(w['ayah']))].add(r)
roots=set().union(*by_ayah.values())
pairs_ayah=collections.Counter()
for k,v in by_ayah.items():
    for a,b in itertools.combinations(sorted(v),2): pairs_ayah[(a,b)]+=1
# +-3 window within surah
pairs_win=set()
keys=sorted(by_ayah)
bys=collections.defaultdict(list)
for s,a in keys: bys[s].append(a)
for s,al in bys.items():
    for i,a in enumerate(al):
        win=set()
        for b in al[max(0,i-3):i+4]: win|=by_ayah[(s,b)]
        for x,y in itertools.combinations(sorted(win),2): pairs_win.add((x,y))
print('rooted words',sum(1 for w in W if w['roots'].strip()),'roots',len(roots),'ayat with roots',len(by_ayah))
print('root pairs co-occurring in >=1 ayah',len(pairs_ayah),'>=3 ayat',sum(1 for v in pairs_ayah.values() if v>=3),'possible',len(roots)*(len(roots)-1)//2)
print('root pairs co-occurring within a +-3 window',len(pairs_win))
# consonant relations among catalog roots
cat=json.load(open('/Volumes/OZTURK/_projects/quran-slm/artifacts/corpus_network/catalog.json'))['cards']
R=sorted({c['surface_root_key'] for c in cat})
tri=[r for r in R if len(r.split())==3]
perm=0; sub1=0
S=set(tri)
from itertools import permutations
seen=set()
for r in tri:
    L=r.split()
    for p in set(permutations(L)):
        q=' '.join(p)
        if q!=r and q in S and (q,r) not in seen: perm+=1; seen.add((r,q))
bypos=collections.defaultdict(list)
for r in tri:
    L=r.split()
    for i in range(3):
        bypos[(i,tuple(L[:i]+['_']+L[i+1:]))].append(r)
for k,v in bypos.items(): sub1+=len(v)*(len(v)-1)//2
print('triliteral catalog roots',len(tri),'metathesis (permutation) pairs',perm,'one-radical-substitution pairs',sub1)
# qiraat
Q=list(csv.DictReader(open('/Volumes/OZTURK/_projects/study/_project_corpus/qiraat.tsv',encoding='utf-8'),delimiter='\t'))
print('qiraat records',len(Q), list(Q[0].keys()))
print(collections.Counter(q.get('variant_type','') for q in Q).most_common(10))
