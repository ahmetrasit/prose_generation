"""Completeness critic check (continues z02): per-branch C2 R5 'present' rate on the 397 dossier true placements,
for the largest branches, plus my hand judgement of the 30-sample in z02 (entered below, judged from the ayah text and
the branch's early phrases/scope note). Shows (a) how much of the 'heuristics miss most constructions' finding is
driven by a few large groups, (b) the gold's own noise. Read-only; writes z03_dossier_gold_by_branch.txt."""
import csv,json,collections
SP='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2'
BI=json.load(open(SP+'/A-v5-step/out/branch_index.json'))
GRAM={'root_001533/B012','root_000502/B003'}
C2={}
for r in csv.DictReader(open(SP+'/C2-loaded-parallels/construction_index.tsv'),delimiter='\t'): C2[(r['ref3'],r['branch'])]=r['present']
seen=set();per=collections.defaultdict(lambda:[0,0,0])
for r in csv.DictReader(open('/Volumes/OZTURK/_projects/root-dossier/out/activation_map.tsv',encoding='utf-8'),delimiter='\t'):
    if r['role']!='dominant' or not r['branch_ref'].startswith('root_'): continue
    b=r['branch_ref']
    if b in GRAM or b not in BI or BI[b]['kind']!='collocation': continue
    ref3=':'.join(r['qac_word_ref'].split(':')[:3])
    if (ref3,b) in seen: continue
    seen.add((ref3,b)); p=C2.get((ref3,b))
    per[b][0]+=1; per[b][1]+= (p=='1'); per[b][2]+= (p is None)
L=[]
tot=sum(v[0] for v in per.values())
top=sorted(per.items(),key=lambda x:-x[1][0])[:8]
L.append(f'true placements {tot}; top-8 branches hold {sum(v[0] for _,v in top)} ({sum(v[0] for _,v in top)/tot:.0%})')
for b,(n,p,miss) in top:
    L.append(f"  {BI[b]['root']} {b.split('/')[1]} {BI[b]['gloss'][:40]}: n={n}, C2 R5 present {p} ({p/n:.0%}), not in index {miss}")
# hand judgement of the z02 30-sample: P present (lexical/syntactic construction in the ayah), F present by derived form
# only (tawalla intransitive), S semantic frame without a lexical construction (dhikr 'by tongue'), A absent
J={1:'P',2:'P',3:'P',4:'P',5:'F',6:'A?',7:'S',8:'P',9:'P',10:'P',11:'P',12:'S',13:'P',14:'P',15:'P',16:'P',17:'A',18:'P',19:'P',20:'P',
   21:'P',22:'P',23:'F',24:'P',25:'P',26:'P',27:'P',28:'P',29:'P',30:'A'}
c=collections.Counter(J.values())
L.append(f'hand judgement of 30 sampled dossier placements (z02): {dict(c)}; the 3 absent/arguable all come from one Luna group (ء ت ي B011 g23, 33 occurrences: bare "the punishment/Hour comes to them")')
open('z03_dossier_gold_by_branch.txt','w').write('\n'.join(L)+'\n'); print('\n'.join(L))
EX={b for b in per if (BI[b]['root'],b.split('/')[1]) in {('و ل ي','B007'),('ذ ك ر','B004'),('ء ت ي','B011')}}
n=sum(v[0] for b,v in per.items() if b not in EX); p=sum(v[1] for b,v in per.items() if b not in EX)
N=sum(v[0] for v in per.values()); P=sum(v[1] for v in per.values())
line=f'C2 R5 recall on dossier gold: all {P}/{N} = {P/N:.2f}; without the 3 branches above (form-bound tawalla, semantic dhikr, over-assigned ata B011) {p}/{n} = {p/n:.2f}'
print(line); open('z03_dossier_gold_by_branch.txt','a').write(line+'\n')
