"""Completeness critic check: are root-dossier 'dominant' placements of collocation-bound branches a valid ground truth
for 'construction present'? (Used as gold by C2 construction_eval2, X-dilution-critic k5/k6 and K-critic frame_rule.)
root-dossier assigns the branch per GROUP by Luna (README: 'group | Luna (max) | ... one branch per group'), so
occurrences inherit their group's branch. Seeded sample of 30 distinct (occurrence, branch) true placements,
excluding the two grammatical constructions; prints ayah text, surface, branch gloss, scope note, first source
clauses, for hand judgement. Read-only. Writes z02_dossier_colloc_sample.txt."""
import csv,json,random,collections
SP='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2'
BI=json.load(open(SP+'/A-v5-step/out/branch_index.json'))
Q={r['ref']:r['text'] for r in csv.DictReader(open('/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/quran.tsv'),delimiter='\t')}
GRAM={'root_001533/B012','root_000502/B003'}
rows=[];seen=set();grp=collections.Counter()
for r in csv.DictReader(open('/Volumes/OZTURK/_projects/root-dossier/out/activation_map.tsv',encoding='utf-8'),delimiter='\t'):
    if r['role']!='dominant' or not r['branch_ref'].startswith('root_'): continue
    b=r['branch_ref']
    if b in GRAM or b not in BI or BI[b]['kind']!='collocation': continue
    ref3=':'.join(r['qac_word_ref'].split(':')[:3])
    if (ref3,b) in seen: continue
    seen.add((ref3,b)); rows.append(r); grp[(b,r['group'])]+=1
print('true collocation placements (excl. 2 grammatical):',len(rows),'branches',len({r['branch_ref'] for r in rows}),'basis',collections.Counter(r['basis'] for r in rows))
random.seed(20260928)
smp=random.sample(rows,30)
L=[]
for i,r in enumerate(smp,1):
    b=r['branch_ref'];v=BI[b]
    L.append(f"#{i} {r['qac_word_ref']} {r['surface_ar']} ({v['root']} {b.split('/')[1]}; group {r['group']} size {grp[(b,r['group'])]}; basis {r['basis']})\n"
             f"   gloss: {v['gloss']} | scope: {v.get('scope_note','')[:220]}\n   src: {(v.get('src_ar') or '')[:260]}\n   ayah {r['verse_ref']}: {Q.get(r['verse_ref'],'')[:400]}")
open('z02_dossier_colloc_sample.txt','w').write('\n'.join(L)+'\n'); print('\n'.join(L))
