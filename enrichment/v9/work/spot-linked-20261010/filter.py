import sys, json, re, sqlite3, random
from collections import Counter, defaultdict
from pathlib import Path
root=Path('/Volumes/aro/projects/prose_generation'); sys.path[:0]=[str(root/'enrichment/v9'),str(root/'enrichment/v7'),str(root/'enrichment/v5')]
import digest, merge
L=root/'enrichment/v9/linked'
idx={json.loads(f.read_text())['ayah']:json.loads(f.read_text()) for f in L.glob('*.json')}
locs={l for d in idx.values() for l in d['segments']}
rows=merge.segment_rows(['luna-max'],locs)
c=sqlite3.connect(f'file:{root}/enrichment/corpus/corpus.sqlite?mode=ro',uri=True)
quran={f'{s}:{a}':t for s,a,t in c.execute("select s,a,text from seg join src on src.id=seg.src where src.kind='quran'")}
# unique 2- and 3-word windows per verse (as quote_packet)
norm={v:digest.normalize_map(t)[0].split() for v,t in quran.items()}
grams=defaultdict(set)
for v,w in norm.items():
    for n in (2,3):
        for i in range(len(w)-n+1): grams[' '.join(w[i:i+n])].add(v)
def windows(v):
    w=norm[v]; return {' '.join(w[i:i+n]) for n in (2,3) for i in range(len(w)-n+1) if grams[' '.join(w[i:i+n])]=={v}}
pairs=[]
for v,d in idx.items():
    for loc,s in d['segments'].items():
        rs=rows.get(loc)
        if rs is None: continue
        if any(v in digest.verse_list(r.get('verses')) or v in digest.verse_list(r.get('mentions')) for r in rs): continue
        pairs.append((v,loc,s['by'],s['kind']))
print('linked pairs whose digested notes do not name the verse:',len(pairs), Counter(p[2] for p in pairs))
text={}
for i in range(0,len({p[1] for p in pairs}),900):
    chunk=list({p[1] for p in pairs})[i:i+900]
    for loc,t in c.execute(f"select seg,text from seg where seg in ({','.join('?'*len(chunk))})",chunk): text[loc]=t
cand=[]
for v,loc,by,kind in pairs:
    t=' '+digest.normalize_map(text.get(loc,''))[0]+' '
    s_,a_=v.split(':')
    hit=any(f' {w} ' in t for w in windows(v)) or re.search(rf'[\[(]\s*[^\]\)]{{0,25}}?\b{a_}\s*[\])]', text.get(loc,'') or '') is not None
    if hit: cand.append((v,loc,by,kind))
print('candidates (segment contains the verse\'s own words or a marker):',len(cand), Counter(p[2] for p in cand), Counter(p[3] for p in cand).most_common(8))
json.dump({'pairs':pairs,'cand':cand},open(sys.argv[1],'w'))
