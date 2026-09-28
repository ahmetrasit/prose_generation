# K6: A's construction cue (s03, used as an S3 HARD flag -> S4 repair) and B's licence v2 (construction.py, used in
# verification + challenge turn "show the construction or drop the root attribution") scored against root-dossier
# plain branches, the same independent labels K5 used for C1 and C2 used for itself.
# A dossier 'dominant' row whose branch is collocation-bound = the construction is present by definition.
# Reported: share of TRUE placements each guard would call "no construction" (= flag / echo / withhold).
import sys, os, csv, json, re, collections
sys.dont_write_bytecode = True
SP='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2'
A=SP+'/A-v5-step/out'; sys.path.insert(0, SP+'/B-noniterative')
import load, construction as BC
BI=json.load(open(A+'/branch_index.json')); OCC=json.load(open(A+'/root_occ.json'))
DIAC=re.compile('[\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed\u0640]')  # same class as A s03 (escaped)
def norm(s):
    s=DIAC.sub('',s or ''); s=s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه').replace('ؤ','و').replace('ئ','ي')
    return s
occ_by=collections.defaultdict(list)
for rid,v in OCC.items():
    for q,ay,lem,surf,atts in v['occ']: occ_by[(rid,ay)].append((q,surf,atts))
def a_cue(b, ay):   # verbatim logic of A s03 cue(), for one ayah
    rid=b.split('/')[0]; v=BI[b]
    text=norm(' '.join([v.get('src_ar') or '',v.get('what_is_ar') or '',v.get('image_ar') or '']))
    found=False
    for q,surf,atts in occ_by.get((rid,ay),[]):
        found=True
        for rel,osurf,oroot,prep,role in atts:
            cands=[]
            if oroot: cands.append(norm(oroot.replace(' ','')))
            if osurf: cands.append(norm(osurf).replace('ال','',1) if norm(osurf).startswith('ال') else norm(osurf))
            for c in cands:
                c=c.strip()
                if len(c)>=3 and c in text: return 'present'
    return 'absent' if found else 'root_absent'
BROW={(r['root_id'],r['branch']):r for r in load.branches().values()}
GRAM={('root_001533','B012'),('root_000502','B003')}
by_rid=collections.defaultdict(list)
for b,v in BI.items():
    if v['kind']=='collocation': by_rid[b.split('/')[0]].append(b)
cnt=collections.Counter(); ex=[]
seen=set()
for r in csv.DictReader(open('/Volumes/OZTURK/_projects/root-dossier/out/activation_map.tsv',encoding='utf-8'),delimiter='\t'):
    if r['role']!='dominant' or not r['branch_ref'].startswith('root_'): continue
    rid,bt=r['branch_ref'].split('/'); ref3=':'.join(r['qac_word_ref'].split(':')[:3]); ay=r['verse_ref']
    if (ref3,rid) in seen: continue
    seen.add((ref3,rid))
    for b in by_rid.get(rid,[]):
        bn=b.split('/')[1]; true=(bn==bt); g=(rid,bn) in GRAM
        ac=a_cue(b,ay)
        row=BROW.get((rid,bn))
        try: bl=('present' if (row and BC.licensed_v2(ref3,row)) else 'absent') if row else 'no_row'
        except Exception as e: bl='error'
        for sub in (('all',)+(() if g else ('excl_gram',))):
            cnt[(sub,'A',true,ac)]+=1; cnt[(sub,'B',true,bl)]+=1
        if true and not g and ac!='present' and bl!='present' and len(ex)<8: ex.append((ref3,BI[b]['root'],bn,BI[b]['gloss'][:40]))
for sub in ('all','excl_gram'):
    for G in ('A','B'):
        T={k[3]:v for k,v in cnt.items() if k[0]==sub and k[1]==G and k[2]}
        F={k[3]:v for k,v in cnt.items() if k[0]==sub and k[1]==G and not k[2]}
        nt=sum(T.values()); nf=sum(F.values())
        print(f"[{sub}] {G}: true placements {nt}: "+', '.join(f"{k} {v} ({v/nt:.0%})" for k,v in sorted(T.items()))+
              f" | other-branch occ {nf}: "+', '.join(f"{k} {v} ({v/nf:.1%})" for k,v in sorted(F.items())))
print('true placements that both A and B call construction-absent (examples):')
for e in ex: print(' -',e)
