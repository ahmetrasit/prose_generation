from pathlib import Path
from html.parser import HTMLParser
import json, hashlib, re

ROOT=Path(__file__).parent/'sources'

class LexParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.depth=0; self.start=None; self.buf=[]; self.sections=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='div':
            self.depth+=1
            if 'dictionary_7' in a.get('class','').split():
                self.start=self.depth; self.buf=[]
        if self.start and tag in ['br','p','li']:self.buf.append('\n')
    def handle_endtag(self,tag):
        if tag=='div':
            if self.start==self.depth:
                self.sections.append(re.sub(r'\n\s*\n+', '\n', ''.join(self.buf)).strip());self.start=None
            self.depth-=1
    def handle_data(self,data):
        if self.start:self.buf.append(data)

index=[]
for f in sorted(ROOT.glob('lex_*.html')):
    p=LexParser();p.feed(f.read_text());text='\n\n'.join(p.sections)
    out=f.with_name(f.stem+'_maqayis.txt');out.write_text(text+'\n')
    index.append({'file':out.name,'sections':len(p.sections),'chars':len(text),'source_html':f.name,'source_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'state':'retrieved_not_yet_inspected','attribution':'Hawramani definition-container dictionary_7, Ibn Faris Maqayis; print-edition comparison not performed'})
(ROOT.parent/'lexicon_retrieval_index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
for r in index:print(r['file'],r['sections'],r['chars'])
