"""v2: both motif formats; anchored ayat = every ref in the subchannel's 'Ayah anchors' line (fallback: every ref in
the block) where the member's root occurs. A collocation-bound member counts as 'construction not detected' when
no occurrence of its root in those ayat has the construction per C2's index (R5, recall 0.33 -> upper bound on drift).
Also reports the strict view: not detected AND C1-style 'absent' is unknowable here, so a hand sample is printed."""
import re,glob,csv,collections,json,sys,os,random
sys.path.insert(0,os.path.dirname(__file__))
import kb
B=kb.load()
root2rid={}
for ref,b in B.items(): root2rid[b['root']]=b['rid']
NET='/Volumes/OZTURK/_projects/quran-data/data/analysis/channels/network-v3'
C2='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/C2-loaded-parallels/construction_index.tsv'
pres=collections.defaultdict(int); seen=set(); evid={}
for r in csv.DictReader(open(C2),delimiter='\t'):
    s,a,w=r['ref3'].split(':'); key=(f'{s}:{a}',r['branch'])
    seen.add(key)
    if int(r['present']): pres[key]=1; evid[key]=r['evidence']
REF=re.compile(r'\b(\d{1,3}):(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?((?:\s*,\s*\d{1,3}(?:[-–]\d{1,3})?)*)')
def refs(text):
    out=[]
    for m in REF.finditer(text):
        s=m.group(1); a=int(m.group(2))
        if m.group(3): out+= [f'{s}:{i}' for i in range(a,int(m.group(3))+1)]
        else: out.append(f'{s}:{a}')
        for part in re.findall(r'\d{1,3}(?:[-–]\d{1,3})?',m.group(4) or ''):
            if '-' in part or '–' in part:
                x,y=re.split('[-–]',part); out+=[f'{s}:{i}' for i in range(int(x),int(y)+1)]
            else: out.append(f'{s}:{part}')
    return out
M1=re.compile(r'quranic:(root_\d+):(B\d+)')
M2=re.compile(r'`([^\s`:]+(?: [^\s`:]+)+):(B\d+)/m\d+`')
st=collections.Counter(); rows=[]; sur_tot=collections.Counter(); sur_nd=collections.Counter(); sur_col=collections.Counter()
for f in sorted(glob.glob(NET+'/s*/review/reader_a_pilot.md')):
    sur=f.split('/')[-3]; txt=open(f).read()
    for block in re.split(r'\n#{3,4} ',txt):
        title=block.split('\n',1)[0][:80]
        mem=set()
        for rid,bid in M1.findall(block): mem.add(f'{rid}/{bid}')
        for root,bid in M2.findall(block):
            rid=root2rid.get(root)
            if rid: mem.add(f'{rid}/{bid}')
        if not mem: continue
        anc=re.search(r'Ayah anchors:(.*)',block)
        ayat=refs(anc.group(1)) if anc else refs(block)
        for ref in mem:
            b=B.get(ref)
            if not b: st['missing']+=1; continue
            st['members']+=1; sur_tot[sur]+=1
            if b['kind']!='collocation': continue
            st['collocation']+=1; sur_col[sur]+=1
            here=[a for a in ayat if (a,ref) in seen]
            if not here: st['colloc_root_not_at_anchors']+=1; continue
            if any(pres.get((a,ref)) for a in here): st['colloc_detected']+=1
            else:
                st['colloc_not_detected']+=1; sur_nd[sur]+=1
                rows.append((sur,title,b['root'],b['bid'],b['image'] or '',','.join(here[:5]),(b['note'] or '')[:140]))
print(json.dumps(st,indent=1))
m=st['members']
print(f"collocation members {st['collocation']}/{m}={st['collocation']/m:.3f}; with root at anchors {st['colloc_detected']+st['colloc_not_detected']}; construction not detected {st['colloc_not_detected']} ({st['colloc_not_detected']/m:.3%} of all members; {st['colloc_not_detected']/max(1,st['colloc_detected']+st['colloc_not_detected']):.1%} of anchored collocation members)")
for s in ['s001','s018','s029','s100','s103','s005','s004','s019','s088']:
    print(s,'members',sur_tot[s],'colloc',sur_col[s],'not-detected',sur_nd[s])
out=os.path.join(os.path.dirname(__file__),'channel_drift2_rows.tsv')
with open(out,'w') as o:
    o.write('surah\tsubchannel\troot\tbranch\timage\tanchored\tnote\n')
    for r in rows: o.write('\t'.join(r)+'\n')
random.seed(11)
for r in random.sample(rows,min(15,len(rows))): print(' | '.join(r)[:300])
print('S1 rows:'); [print(' | '.join(r)[:260]) for r in rows if r[0]=='s001']
