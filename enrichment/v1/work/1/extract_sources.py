import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path

W = Path(__file__).resolve().parent

class Extract(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.level=0
        self.capture=None
        self.buffer=[]
        self.paras=[]
        self.tag_skip=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='div':
            self.level+=1
            if a.get('class')=='nass': self.capture=self.level
        if self.capture:
            if tag=='a' and 'btn_tag' in a.get('class',''): self.tag_skip+=1
            if tag in ('br','hr','p') or (tag=='span' and a.get('class')=='anchor'): self.buffer.append('\n')
            if a.get('id','').startswith('p') and a.get('id','')[1:].isdigit(): self.paras.append(a['id'])
    def handle_endtag(self,tag):
        if self.capture and tag in ('p','div'): self.buffer.append('\n')
        if tag=='a' and self.tag_skip: self.tag_skip-=1
        if tag=='div':
            if self.capture==self.level: self.capture=None
            self.level-=1
    def handle_data(self,data):
        if self.capture and not self.tag_skip: self.buffer.append(data)

items=[]
for path in sorted((W/'sources').glob('*.html')):
    e=Extract()
    e.feed(path.read_text())
    clean='\n'.join(x.strip() for x in ''.join(e.buffer).splitlines() if x.strip())+'\n'
    out=path.with_suffix('.txt')
    out.write_text(clean)
    code,s,a=path.stem.split('_')
    root='https://quran.ksu.edu.sa/tafseer' if code in ('tabary','katheer') else 'https://quran-tafsir.net'
    item=dict(file=out.name,url=f'{root}/{code}/sura{s}-aya{a}.html',author_code=code,surah=int(s),ayah=int(a),text_lines=len(clean.splitlines()),text_characters=len(clean),text_sha256=hashlib.sha256(clean.encode()).hexdigest(),raw_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),paragraph_anchors=e.paras,state='retrieved_not_yet_inspected')
    items.append(item)
    print(f'{out.name} lines={item["text_lines"]} chars={len(clean)} anchors={len(e.paras)}')
(W/'retrieval_index.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
