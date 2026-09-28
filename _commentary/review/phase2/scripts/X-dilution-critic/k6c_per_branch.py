# K6c: per-branch (macro) view of K6 and K5, so a few frequent branches (ء ت ي B011, و ل ي B007, ق و م B005) do not dominate.
import sys,os,csv,collections,statistics
exec(open('k6_guards_vs_dossier.py').read().split("cnt=collections.Counter()")[0])
C1='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/C1-branch-distance'
sys.path.insert(0,C1); cwd=os.getcwd(); os.chdir(C1)
import common as C, guard as G
os.chdir(cwd)
W={w['ref']:w for w in C.WORDS}
per=collections.defaultdict(lambda: collections.Counter())
seen=set()
for r in csv.DictReader(open('/Volumes/OZTURK/_projects/root-dossier/out/activation_map.tsv',encoding='utf-8'),delimiter='\t'):
    if r['role']!='dominant' or not r['branch_ref'].startswith('root_'): continue
    b=r['branch_ref']
    if BI.get(b,{}).get('kind')!='collocation': continue
    rid,bn=b.split('/'); ref3=':'.join(r['qac_word_ref'].split(':')[:3]); ay=r['verse_ref']
    if (rid,bn) in GRAM or (ref3,b) in seen: continue
    seen.add((ref3,b))
    per[b]['n']+=1
    per[b]['A_abs']+= a_cue(b,ay)!='present'
    row=BROW.get((rid,bn)); per[b]['B_abs']+= not (row and BC.licensed_v2(ref3,row))
    w=W.get(ref3); st='nw'
    if w:
        for i in C.BY_RID.get(rid,[]):
            if C.BID[i]==bn: st=G.status(i,w)[0]
    per[b]['C1_echo']+= st=='absent'
    per[b]['C1_notstrict']+= st!='present_strict'
print('distinct collocation branches with dossier placements (excl 2 grammatical):',len(per),' placements:',sum(v['n'] for v in per.values()))
for k in ('A_abs','B_abs','C1_echo','C1_notstrict'):
    sh=[v[k]/v['n'] for v in per.values()]
    print(f"{k}: median share of a branch's true placements = {statistics.median(sh):.2f}; branches where ALL placements miss: {sum(1 for s in sh if s==1.0)}/{len(sh)}")
