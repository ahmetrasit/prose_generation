from html.parser import HTMLParser
from pathlib import Path
class P(HTMLParser):
 def __init__(self):super().__init__();self.depth=0;self.out=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='div' and ('nass' in a.get('class','').split()):self.depth=1
  elif self.depth and t=='div':self.depth+=1
  if self.depth and t in ('p','br','hr'):self.out.append('\n')
 def handle_endtag(self,t):
  if self.depth and t=='div':self.depth-=1
  if self.depth and t=='p':self.out.append('\n')
 def handle_data(self,d):
  if self.depth:self.out.append(d)
for f in Path('enrichment/v1/work/107_astra_high/sources').glob('*.html'):
 p=P();p.feed(f.read_text());txt='\n'.join(x.strip() for x in ''.join(p.out).splitlines() if x.strip());f.with_suffix('.txt').write_text(txt)
 print(f.stem,len(txt))
