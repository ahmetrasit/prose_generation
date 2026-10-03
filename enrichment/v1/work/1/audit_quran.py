from pathlib import Path
import json,re,unicodedata,hashlib
p=Path(__file__).parent
base=Path('_commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md').read_text()
q={}
for l in (p/'sources/quran-uthmani.txt').read_text().splitlines():
    m=re.match(r'^(\d+)\|(\d+)\|(.*)$',l)
    if m:q[f'{m[1]}:{m[2]}']=m[3]
def norm(s):
    s=s.translate(str.maketrans({'ٱ':'ا','أ':'ا','إ':'ا','آ':'ا','ؤ':'و','ئ':'ي','ى':'ي','ـ':''}))
    return ''.join(c for c in unicodedata.normalize('NFD',s) if not unicodedata.category(c).startswith('M') and ('\u0621'<=c<='\u064a' or c==' ')).strip()
rows=[]
refs=set(re.findall(r'source:(\d+:\d+)',base))
for t in re.findall(r'\{[^{}]+\}',base):
    a=re.search(r'^\{ar:(.*?),\s*tr:',t);r=re.search(r'\bsource:(\d+:\d+)',t)
    if a and r:
        ar,ref=a[1],r[1];whole=q.get(ref,'');n=norm(ar);nw=norm(whole)
        rows.append({'ref':ref,'ar':ar,'match_normalized':n in nw,'base_normalized':n,'quran':whole,'quran_normalized':nw})
data={'edition':'Tanzil Uthmani v1.1','unchanged_download_sha256':hashlib.sha256((p/'sources/quran-uthmani.txt').read_bytes()).hexdigest(),'downloaded_verses':len(q),'unique_base_quran_refs':len(refs),'quote_count':len(rows),'normalized_matches':sum(r['match_normalized'] for r in rows),'normalization_note':'Only comparison representation changes; downloaded source and base remain unmodified. Consonantal/orthographic screening does not validate Turkish glosses or every attribution.','rows':rows}
(p/'quran_quote_audit.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
reftext='\n'.join(f'{r}|{q[r]}' for r in sorted(refs,key=lambda r:tuple(map(int,r.split(':')))))+'\n'
(p/'sources/base_quran_passages.txt').write_text(reftext)
print({k:v for k,v in data.items() if k!='rows'})
for r in rows:
    if not r['match_normalized']:print(r['ref'],r['ar'],' / ',r['quran'])
