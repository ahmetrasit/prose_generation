from html.parser import HTMLParser
from pathlib import Path
import json,hashlib,re
W=Path(__file__).resolve().parent
class Extract(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.level=0;self.capture=None;self.buffer=[];self.paras=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='div':
   self.level+=1
   if 'nass' in a.get('class','').split():self.capture=self.level
  if self.capture:
   if tag=='a' and 'btn_tag' in a.get('class',''):self.skip+=1
   if tag in ('br','hr','p') or tag=='span' and a.get('class')=='anchor':self.buffer.append('\n')
   if re.fullmatch('p[0-9]+',a.get('id','')):self.paras.append(a['id'])
 def handle_endtag(self,tag):
  if self.capture and tag in ('p','div'):self.buffer.append('\n')
  if tag=='a' and self.skip:self.skip-=1
  if tag=='div':
   if self.capture==self.level:self.capture=None
   self.level-=1
 def handle_data(self,d):
  if self.capture and not self.skip:self.buffer.append(d)
items=[]
for f in sorted((W/'sources').glob('*_100_*.html')):
 e=Extract();e.feed(f.read_text());clean='\n'.join(s.strip() for s in ''.join(e.buffer).splitlines() if s.strip())+'\n';out=f.with_suffix('.txt');out.write_text(clean)
 author,s,a=f.stem.split('_');origin='https://quran.ksu.edu.sa/tafseer' if author in ['tabary','katheer'] else 'https://quran-tafsir.net'
 items.append(dict(file=out.name,url=f'{origin}/{author}/sura{s}-aya{a}.html',author=author,surah=int(s),ayah=int(a),lines=len(clean.splitlines()),chars=len(clean),sha256=hashlib.sha256(clean.encode()).hexdigest(),raw_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),anchors=e.paras,state='retrieved_not_yet_inspected'))
(W/'retrieval_index.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
for author in ['tabary','katheer','zamakhshary','alrazy','baidawy','seoty','beqaay']:
 a=[x for x in items if x['author']==author];print(author,[(x['ayah'],x['lines'],x['chars']) for x in a])
