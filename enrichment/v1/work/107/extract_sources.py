from html.parser import HTMLParser
from pathlib import Path
import re,json,hashlib

WORK=Path(__file__).parent; S=WORK/'sources'
class TextParser(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.buf=[];self.hidden=0
    def handle_starttag(self,t,a):
        if t in ('script','style','h1','h2','h3'): self.hidden+=1
        if t in ('p','section','h3','br'): self.buf.append('\n')
    def handle_endtag(self,t):
        if t in ('script','style','h1','h2','h3'):self.hidden-=1
        if t in ('p','section','h3'): self.buf.append('\n')
    def handle_data(self,d):
        if not self.hidden:self.buf.append(d)

class LexParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True);self.depth=0;self.outer=None;self.inner=None;self.key=None;self.buf=[];self.sections=[];self.credits='';self.perma=''
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if t=='div':
            self.depth+=1
            cls=a.get('class','').split()
            if 'definition-container' in cls:
                self.outer=self.depth; self.key=next((c for c in cls if c.startswith('dictionary_')),'unknown')
            if self.outer and 'definition' in cls:self.inner=self.depth;self.buf=[]
        if self.inner and t in ('p','br'): self.buf.append('\n')
    def handle_endtag(self,t):
        if t=='div':
            if self.depth==self.inner:
                tx=re.sub(r'\n\s*\n+', '\n', ''.join(self.buf)).strip()
                self.sections.append((self.key,tx));self.inner=None
            if self.depth==self.outer:self.outer=None
            self.depth-=1
    def handle_data(self,d):
        if self.inner:self.buf.append(d)

index=[]
for f in sorted(S.glob('lex_*.html')):
    p=LexParser();p.feed(f.read_text())
    for n,(k,tx) in enumerate(p.sections):
        out=f.with_name(f'{f.stem}_{k}_{n:02d}.txt');out.write_text(tx+'\n')
        index.append(dict(source_html=f.name,section=k,section_number=n,chars=len(tx),file=out.name,inspected=False))
(WORK/'lexicon_sections.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')

f=S/'maqayis_book.html';p=TextParser();p.feed(f.read_text());txt=''.join(p.buf)
txt=re.sub(r'\n[ \t]*\n+', '\n',txt);txt=re.sub(r'[ \t]+',' ',txt)
norm=lambda s:re.sub(r'[\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed]','',s).replace('ى','ي').replace('\u0640','')
all_markers=[]
for m in re.finditer(r'(?m)^\(([^()\n]{2,24})\)\s+(\S+)',txt):
    r=norm(m.group(1))
    if len(r) in (2,3,4) and ' ' not in r and m.group(2).startswith('ال'):
        all_markers.append((m.start(),r))
roots=['رأي','كذب','يتم','سهو','صلي','معن','سكن','دين','دع','حض','طعم','منع','ويل']
maq=[]
for r in roots:
    hits=[(i,begin) for i,(begin,root) in enumerate(all_markers) if root==r]
    if len(hits)!=1:
        print('AMBIGUOUS',r,hits); continue
    i,b=hits[0];e=all_markers[i+1][0] if i+1<len(all_markers) else len(txt)
    out=S/f'maqayis_{r}.txt'; out.write_text(txt[b:e].strip()+'\n')
    maq.append(dict(root=r,file=out.name,chars=e-b,html_offset_not_relevant=True,text_start=b,text_end=e,inspected=False,source_html=f.name))
(WORK/'maqayis_sections.json').write_text(json.dumps(maq,ensure_ascii=False,indent=2)+'\n')
print('lex sections',len(index));print('maqayis roots',len(maq));print('\n'.join(f"{x['root']} {x['chars']}" for x in maq))
