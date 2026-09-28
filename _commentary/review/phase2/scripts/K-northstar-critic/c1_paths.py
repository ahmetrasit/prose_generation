"""Quality of C1 push paths: share of 'Quran pairs «X» with ...' bridge paths whose bridge lemma X is frequent
(ayah df of any root it maps to > 100), and where the plain/B001 branch sits per word. Read-only."""
import re,glob,os,sys,collections,csv
sys.dont_write_bytecode=True
C1='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/C1-branch-distance'
sys.path.insert(0,C1); cwd=os.getcwd(); os.chdir(C1); import common as C; os.chdir(cwd)
df=collections.Counter()
for (s,a),ws in C.BY_AYAH.items():
    for r in {r for w in ws for r in w['roots']}: df[r]+=1
tot=freq=0; ex=collections.Counter(); b1pos=[]; first_lines=[]
for f in sorted(glob.glob(C1+'/harvest2/*.push.md')):
    txt=open(f).read()
    for m in re.finditer(r'Quran pairs «([^»]+)»',txt):
        tot+=1; x=C.norm(m.group(1)); rs=C.token_roots(x)
        if rs and max(df[r] for r in rs)>100: freq+=1; ex[m.group(1)]+=1
    for blk in re.split(r'\n## w\d+ ',txt)[1:]:
        lines=[l for l in blk.split('\n') if l.startswith('  - B')]
        ids=[re.match(r'  - (B\d+)',l).group(1) for l in lines]
        if 'B001' in ids: b1pos.append(ids.index('B001')+1)
print(f'bridge paths {tot}; bridge lemma in >100 ayat: {freq} ({freq/max(1,tot):.1%})'); print('top bridges',ex.most_common(12))
print('position of B001 among listed live branches per word: median',sorted(b1pos)[len(b1pos)//2],'share not first',sum(p>1 for p in b1pos)/len(b1pos), 'n',len(b1pos))
