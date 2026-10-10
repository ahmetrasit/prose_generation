"""Read-only quotation review aid for the live image-author pilot."""
import json,re,sqlite3,sys,unicodedata
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[5]))
from enrichment.bible import image_enrich as I,corpus as C
root=Path(__file__).resolve().parent
pattern=re.compile(r"\{(he|el):\s*(.*?),\s*tr:.*?,\s*gloss:.*?,\s*source:\s*([^{}]+)\}")
rows=[]
with sqlite3.connect(f'file:{C.INDEX_INTERTEXT}?mode=ro',uri=True) as con:
 for job in I.read_json(root/'started.json')['jobs']:
  p=root/job['target']/'annotations.jsonl'
  if not p.exists():continue
  for line in p.read_text().splitlines():
   if not line.strip():continue
   r=json.loads(line)
   for m in pattern.finditer(r.get('metin','')):
    lang,quote,ref=m.groups();ref=ref.strip()
    src=con.execute('SELECT text,extra FROM seg WHERE seg=?',(ref,)).fetchone()
    exact=bool(src and unicodedata.normalize('NFC',quote) in unicodedata.normalize('NFC',src[0]))
    normalized=bool(src and C.norm(quote) in C.norm(src[0]))
    row=dict(section=job['target'],annotation=r['id'],ref=ref,language=lang,quote=quote,exact=exact,normalized=normalized)
    if not normalized:row['source_text']=src[0] if src else None
    rows.append(row)
report=dict(quotes=len(rows),exact=sum(x['exact'] for x in rows),normalized=sum(x['normalized'] for x in rows),
 findings=[r for r in rows if not r['exact']],rows=rows,
 limits='A text-match aid, not a judgment of interpretation, transliteration or Turkish glosses.')
I.D.save(root/'quote_audit.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='rows'},ensure_ascii=False,indent=2))
