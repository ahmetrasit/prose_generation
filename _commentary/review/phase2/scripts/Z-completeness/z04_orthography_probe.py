"""Completeness critic check: is part of the guards' low recall an orthography artefact (Uthmani rasm in the Quran
text vs classical spelling in the early phrases: ٱلصَّلَوٰة -> 'الصلوه' vs 'الصلاة' -> 'الصلاه')? Re-runs A's s03 cue
logic (as copied verbatim into X-dilution-critic/k6_guards_vs_dossier.py) on the dossier true placements of the
8 largest collocation branches, with and without a rasm-folding step (وٰ/ىٰ with dagger alif -> ا, then the same
normaliser). Read-only; writes z04_orthography_probe.txt."""
import sys,os,csv,json,re,collections
sys.dont_write_bytecode=True
SP='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2'
A=SP+'/A-v5-step/out'
BI=json.load(open(A+'/branch_index.json')); OCC=json.load(open(A+'/root_occ.json'))
DIAC=re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')
def base(s):
    s=s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه').replace('ؤ','و').replace('ئ','ي')
    return s
def norm(s): return base(DIAC.sub('',s or ''))
def norm_rasm(s):
    s=s or ''
    s=re.sub('و[ً-ٟ]*ٰ','ا',s)   # صلوٰة -> صلاة , زكوٰة -> زكاة , حيوٰة -> حياة
    s=re.sub('ى[ً-ٟ]*ٰ','ا',s)   # rasm alif maqsura + dagger alif
    s=re.sub('([ء-ي])[ً-ٟ]*ٰ',r'\1ا',s)  # other dagger alifs -> alif (هٰذا -> هاذا)
    return norm(s)
occ_by=collections.defaultdict(list)
for rid,v in OCC.items():
    for q,ay,lem,surf,atts in v['occ']: occ_by[(rid,ay)].append((q,surf,atts))
def cue(b,ay,nf):
    rid=b.split('/')[0]; v=BI[b]
    text=norm(' '.join([v.get('src_ar') or '',v.get('what_is_ar') or '',v.get('image_ar') or '']))
    text2=text.replace('اا','ا')
    for q,surf,atts in occ_by.get((rid,ay),[]):
        for rel,osurf,oroot,prep,role in atts:
            cands=[]
            if oroot: cands.append(norm(oroot.replace(' ','')))
            if osurf:
                n=nf(osurf); cands.append(n[2:] if n.startswith('ال') else n)
            for c in cands:
                c=c.strip()
                if len(c)>=3 and (c in text or c in text2): return True
    return False
GRAM={'root_001533/B012','root_000502/B003'}
seen=set();per=collections.defaultdict(lambda:[0,0,0])
for r in csv.DictReader(open('/Volumes/OZTURK/_projects/root-dossier/out/activation_map.tsv',encoding='utf-8'),delimiter='\t'):
    if r['role']!='dominant' or not r['branch_ref'].startswith('root_'): continue
    b=r['branch_ref']
    if b in GRAM or b not in BI or BI[b]['kind']!='collocation': continue
    ref3=':'.join(r['qac_word_ref'].split(':')[:3])
    if (ref3,b) in seen: continue
    seen.add((ref3,b))
    per[b][0]+=1; per[b][1]+=cue(b,r['verse_ref'],norm); per[b][2]+=cue(b,r['verse_ref'],norm_rasm)
L=[]
N=sum(v[0] for v in per.values()); P1=sum(v[1] for v in per.values()); P2=sum(v[2] for v in per.values())
L.append(f'A s03 cue on {N} dossier true placements: present {P1} ({P1/N:.0%}) as built; {P2} ({P2/N:.0%}) with rasm folding')
for b,(n,p1,p2) in sorted(per.items(),key=lambda x:-x[1][0])[:8]:
    L.append(f"  {BI[b]['root']} {b.split('/')[1]} {BI[b]['gloss'][:34]}: n={n} as-built {p1} -> rasm-folded {p2}")
open('z04_orthography_probe.txt','w').write('\n'.join(L)+'\n'); print('\n'.join(L))
