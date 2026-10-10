import sys, json, random, sqlite3
from collections import defaultdict
from pathlib import Path
root=Path('/Volumes/aro/projects/prose_generation'); sys.path[:0]=[str(root/'enrichment/v9'),str(root/'enrichment/v7'),str(root/'enrichment/v5')]
import merge
S=Path(sys.argv[1]); d=json.load(open(S/'spot.json'))
cand=[tuple(x) for x in d['cand']]
random.seed(20261010)
groups=defaultdict(list)
for p in cand: groups[(p[2], p[3] if p[3] in ('tafsir','modern','ulum','tafsir_tr','nazm') else 'other')].append(p)
N=40; tot=len(cand)
quota={g:max(1,round(N*len(v)/tot)) for g,v in groups.items()}
while sum(quota.values())>N: quota[max(quota,key=quota.get)]-=1
while sum(quota.values())<N: quota[max(groups,key=lambda g:len(groups[g])/quota[g])]+=1
sample=[p for g,q in quota.items() for p in random.sample(groups[g],min(q,len(groups[g])))]
c=sqlite3.connect(f'file:{root}/enrichment/corpus/corpus.sqlite?mode=ro',uri=True)
quran={f'{s}:{a}':t for s,a,t in c.execute("select s,a,text from seg join src on src.id=seg.src where src.kind='quran'")}
rows=merge.segment_rows(['luna-max'],{p[1] for p in sample})
out=S/'spot_sample'; out.mkdir(exist_ok=True)
man=[]
for i,(v,loc,by,kind) in enumerate(sample,1):
    head,text,src=c.execute('select head,text,src from seg where seg=?',(loc,)).fetchone()
    link=json.load(open(root/f"enrichment/v9/linked/{v.replace(':','-')}.json"))['segments'][loc]
    notes='\n'.join(f"[{r['id']}] verses {r.get('verses')} · {r['speaker']} · {r['stance']} · {r['claim']} «{r.get('anchor') or ''}»" for r in rows.get(loc,[]))
    (out/f'p{i:02d}.txt').write_text(f"PAIR p{i:02d}\nVERSE {v}: {quran[v]}\nSEGMENT {loc} · source {src} · kind {kind} · tied by {'index range' if by=='index' else 'quoting the verse'}: {link['verses']} · heading: {head or ''}\n\n=== SEGMENT TEXT ===\n{text}\n\n=== EXISTING DIGEST NOTES FOR THIS SEGMENT ===\n{notes or '(none)'}\n")
    man.append({'pair':f'p{i:02d}','verse':v,'loc':loc,'by':by,'kind':kind,'chars':len(text)})
json.dump(man,open(out/'manifest.json','w'),indent=1,ensure_ascii=False)
from collections import Counter
print(len(man), Counter((m['by'],m['kind']) for m in man), sum(m['chars'] for m in man))
