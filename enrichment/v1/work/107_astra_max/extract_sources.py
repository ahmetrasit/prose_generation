from html.parser import HTMLParser
from pathlib import Path
import re,json,hashlib
class P(HTMLParser):
 def __init__(self):super().__init__();self.depth=0;self.a=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if self.depth:
   if t=='div':self.depth+=1
   if t in ('p','br','hr'):self.a.append('\n')
  elif t=='div' and 'nass' in d.get('class','').split():self.depth=1
 def handle_endtag(self,t):
  if self.depth:
   if t=='div':self.depth-=1;self.a.append('\n')
   elif t=='p':self.a.append('\n')
 def handle_data(self,d):
  if self.depth:self.a.append(d)
folder=Path('enrichment/v1/work/107_astra_max/sources')
rows=[]
for f in sorted(folder.glob('*_107_*.html')):
 p=P();p.feed(f.read_text());txt='\n'.join(x.strip() for x in ''.join(p.a).splitlines() if x.strip())
 f.with_suffix('.txt').write_text(txt+'\n')
 rows.append({'name':f.stem,'characters':len(txt),'lines':txt.count('\n')+1,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
for a in ['tabari','ibnkathir','qurtubi','razi','suyuti','zamakhshari','baydawi','biqai']:
 out='\n\n'.join('### '+f.stem+'\n'+f.read_text() for f in sorted(folder.glob(a+'_107_*.txt')))
 (folder/(a+'_all.txt')).write_text(out)
 print(a,len(out),out.count('\n'))
(folder/'download_manifest.json').write_text(json.dumps(rows,indent=2))
