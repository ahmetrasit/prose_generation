"""Test a generic 'frame' state for the construction guard: a collocation-bound branch whose lexical construction is
NOT detected (C2 R5 index) counts as frame-present when its own definition/early phrase names (token -> Quranic root)
a root carried by another word of the same ayah within +-W words of the occurrence. No case rules.
Evaluated on: watch/NS loci; root-dossier plain-branch labels (collocation branches), as C2 did.
Uses C1's read-only token->root lexicon (common.token_roots) and C2's construction index. Read-only."""
import sys,os,csv,collections,re,json
sys.dont_write_bytecode=True
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import kb
C1='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/C1-branch-distance'
sys.path.insert(0,C1)
cwd=os.getcwd(); os.chdir(C1)
import common as C
os.chdir(cwd)
B=kb.load()
W=int(sys.argv[1]) if len(sys.argv)>1 else 4
C2='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/C2-loaded-parallels/construction_index.tsv'
rows=list(csv.DictReader(open(C2),delimiter='\t'))
# words by ref
WBY={}
for w in C.WORDS: WBY[(w['s'],w['a'],w['w'])]=w
def named_roots(b):
    txt=' '.join([b['image'] or '', b['what'] or '', b['phrase'] if isinstance(b['phrase'],str) else json.dumps(b['phrase'],ensure_ascii=False)])
    txt=re.sub(r'\([a-z;]+\)','',txt)
    out=set()
    for t in C.TOK.findall(C.norm(txt)):
        if t in C.STOP_TOK or len(t)<3: continue
        out|=C.token_roots(t)
    return out-{C.nroot(b['root'])}
NR={}
def frame(ref3,bref):
    s,a,w=map(int,ref3.split(':'))
    b=B[bref]
    if bref not in NR: NR[bref]=named_roots(b)
    nr=NR[bref]
    hits=[]
    for k in range(w-W,w+W+1):
        if k==w: continue
        x=WBY.get((s,a,k))
        if not x: continue
        for r in x['roots']:
            if r in nr: hits.append(f"{x['surface']}({r})")
    return hits
# 1) named loci
loci=[('100:1','root_000901/B002'),('4:34',None),('1:4',None),('1:6',None),('1:7',None),('1:5',None),('1:2',None),('29:38',None),('18:96',None)]
idx=collections.defaultdict(list)
for r in rows:
    s,a,w=r['ref3'].split(':'); idx[f'{s}:{a}'].append(r)
for ay,only in loci:
    for r in idx[ay]:
        if only and r['branch']!=only: continue
        if r['present']=='1': st='lexical'
        else:
            h=frame(r['ref3'],r['branch']); st='FRAME '+','.join(h[:3]) if h else 'absent'
        b=B[r['branch']]
        if ay in ('4:34',) and b['root']!='ض ر ب': continue
        print(ay,r['ref3'],b['root'],b['bid'],(b['image'] or '')[:40],'->',st)
# 2) dossier evaluation on collocation branches
dos={}
for r in csv.DictReader(open('/Volumes/OZTURK/_projects/root-dossier/out/activation_map.tsv'),delimiter='\t'):
    if r['role']=='dominant': dos[r['qac_word_ref']]=r['branch_ref']
droots={B[v]['root'] for v in dos.values() if v in B}
tp=fn=fp=tn=0; tpF=fpF=0; ex_fp=[]; ex_tp=[]
for r in rows:
    d=dos.get(r['ref3'])
    if not d or not d.startswith('root_'): continue
    if B.get(r['branch'],{}).get('root') not in droots: continue
    if B.get(d,{}).get('root')!=B[r['branch']]['root']: continue
    lex=r['present']=='1'
    fr=bool(frame(r['ref3'],r['branch'])) if not lex else False
    if d==r['branch']:
        tp+=lex; fn+=(not lex); tpF+=fr
        if fr and len(ex_tp)<8: ex_tp.append((r['ref3'],B[r['branch']]['root'],B[r['branch']]['bid']))
    else:
        fp+=lex; tn+=(not lex); fpF+=fr
        if fr and len(ex_fp)<8: ex_fp.append((r['ref3'],B[r['branch']]['root'],B[r['branch']]['bid'],frame(r['ref3'],r['branch'])[:2]))
print(f'W={W} dossier: lexical tp={tp} fn={fn} fp={fp} tn={tn} recall={tp/max(1,tp+fn):.3f} FAR={fp/max(1,fp+tn):.4f}')
print(f'  + frame: recall={(tp+tpF)/max(1,tp+fn):.3f} FAR={(fp+fpF)/max(1,fp+tn):.4f}  (frame adds tp {tpF}, fp {fpF})')
print('  frame tp ex',ex_tp); print('  frame fp ex',ex_fp[:5])
