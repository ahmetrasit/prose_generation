from html.parser import HTMLParser
from pathlib import Path
import json,re,hashlib
W=Path(__file__).resolve().parent
class Lex(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.depth=0;self.start=None;self.buf=[];self.entries=[];self.code=None;self.canonical=''
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='link' and a.get('rel')=='canonical':self.canonical=a.get('href','')
  if t=='div':
   self.depth+=1
   if 'definition-container' in a.get('class','').split():self.start=self.depth;self.buf=[];self.code=a.get('class')
  if self.start and t in ['br','p','li']:self.buf.append('\n')
 def handle_endtag(self,t):
  if t=='div':
   if self.start==self.depth:
    clean=re.sub(r'\n\s*\n+','\n',''.join(self.buf)).strip();self.entries.append({'code':self.code,'text':clean});self.start=None
   self.depth-=1
 def handle_data(self,d):
  if self.start:self.buf.append(d)
items=[]
for f in sorted((W/'sources').glob('lex_*.html')):
 e=Lex();e.feed(f.read_text());ident=f.stem;entries=[]
 for i,b in enumerate(e.entries):
  code=re.search(r'dictionary_(\d+)',b['code']).group(1);out=f.with_name(ident+f'_d{code}_{i}.txt');out.write_text(b['text']+'\n');entries.append({'dictionary_code':code,'file':out.name,'chars':len(b['text']),'incipit':b['text'][:180],'state':'retrieved_not_yet_inspected'})
 items.append({'root_file':f.name,'url':e.canonical,'entries':entries,'raw_sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(W/'lexicon_retrieval_index.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
for r in items:print(r['root_file'],[(b['dictionary_code'],b['chars']) for b in r['entries'] if b['dictionary_code'] in ['7','2','3','4']])
