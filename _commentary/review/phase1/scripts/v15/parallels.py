import csv,math,sys
from collections import defaultdict
csv.field_size_limit(10**9)
W='/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/words.tsv'
roots=defaultdict(set); lem=defaultdict(set)
for r in csv.DictReader(open(W),delimiter='\t'):
    ref=f"{r['surah']}:{r['ayah']}"
    for x in r['roots'].split('|'):
        if x: roots[ref].add(x)
    for x in r['lemmas'].split('|'):
        if x: lem[ref].add(x)
N=len(roots)
df=defaultdict(int)
for ref,rs in roots.items():
    for x in rs: df[x]+=1
dfl=defaultdict(int)
for ref,ls in lem.items():
    for x in ls: dfl[x]+=1
idf=lambda x: math.log(N/df[x]); idfl=lambda x: math.log(N/dfl[x])
def rank(focus, scope_surah=True, use_lemma=False, targets=()):
    s=focus.split(':')[0]
    F=lem[focus] if use_lemma else roots[focus]
    f=idfl if use_lemma else idf
    sc=[]
    for ref,rs in (lem if use_lemma else roots).items():
        if ref==focus: continue
        if scope_surah and ref.split(':')[0]!=s: continue
        shared=F & rs
        if shared: sc.append((sum(f(x) for x in shared), ref, sorted(shared, key=lambda x:-f(x))[:4]))
    sc.sort(reverse=True)
    pos={ref:i+1 for i,(_,ref,_) in enumerate(sc)}
    return pos, sc
for focus,targets in [('5:6',['5:97','5:89','5:91','5:8','5:95','35:10','5:11','4:43']),('4:34',['4:128','4:129','4:130','4:19','4:3','4:90','4:81','4:35','4:36','4:5','2:238'])]:
    for lemma in (False,True):
        pos,sc=rank(focus,True,lemma)
        posQ,scQ=rank(focus,False,lemma)
        print(focus,'lemma' if lemma else 'root','same-surah candidates',len(sc),{t:pos.get(t) for t in targets if t.split(':')[0]==focus.split(':')[0]}, 'whole-Quran:',{t:posQ.get(t) for t in targets}, 'of', len(scQ))
