from pathlib import Path
import hashlib,json,re,unicodedata
W=Path(__file__).resolve().parent
B=Path('/Volumes/aro/projects/prose_generation/_commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md')
q={}
for line in (W/'sources/quran-uthmani-numbered.txt').read_text().splitlines():
 if re.match(r'^\d+\|\d+\|',line):
  s,a,t=line.split('|',2);q[f'{s}:{a}']=t
def norm(s):
 s=unicodedata.normalize('NFKD',s)
 s=''.join(c for c in s if not unicodedata.category(c).startswith('M') and c!='ـ')
 return re.sub(r'\s+','',s.translate(str.maketrans({'ٱ':'ا','أ':'ا','إ':'ا','آ':'ا','ى':'ي'})))
base=B.read_text();rows=[]
for match in re.finditer(r'\{ar:([^{}]*?),\s*tr:[^{}]*?source:\s*(\d+:\d+)\}',base):
 text,ref=match.groups();rows.append({'ref':ref,'base_ar':text,'canonical_ar':q.get(ref),'match_normalized':ref in q and norm(text) in norm(q[ref])})
refs={r['ref'] for r in rows}
extra=['5:90','9:17','99:8','36:79','56:74','68:18','68:22','68:23','68:25','68:26','68:27','68:28','68:29','68:30','68:31','68:32','68:33','3:153','34:14','37:3','77:3','99:5']
refs.update(extra);refs.update(f'100:{a}' for a in range(1,12))
ordered=sorted(refs,key=lambda s:tuple(map(int,s.split(':'))))
(W/'sources/quran_selected.txt').write_text('\n'.join(f'{ref}|{q[ref]}' for ref in ordered)+'\n\n'+ '\n'.join(x for x in (W/'sources/quran-uthmani-numbered.txt').read_text().splitlines() if x.startswith('#'))+'\n')
data={'edition':'Tanzil Uthmani v1.1','download_url':'https://tanzil.net/pub/download/index.php?quranType=uthmani&outType=txt-2&agree=true','download_sha256':hashlib.sha256((W/'sources/quran-uthmani-numbered.txt').read_bytes()).hexdigest(),'downloaded_verses':len(q),'unique_base_quran_refs':len({r['ref'] for r in rows}),'quote_count':len(rows),'normalized_matches':sum(r['match_normalized'] for r in rows),'selected_refs':ordered,'normalization_note':'Only comparison normalizes marks, hamza/alif variants, alif maqsurah and whitespace. This is an orthographic substring check, not a validation of Turkish interpretation. Original base and download remain unchanged.','rows':rows}
(W/'quran_quote_audit.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('Quran verses',len(q),'base refs',data['unique_base_quran_refs'],'quotes',len(rows),'normalized_matches',data['normalized_matches'],'selected',len(ordered))
for r in rows:
 if not r['match_normalized']:print('MISMATCH',r['ref'],r['base_ar'],r['canonical_ar'])
