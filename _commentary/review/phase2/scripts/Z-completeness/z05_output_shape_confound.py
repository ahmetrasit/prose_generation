"""Completeness critic check: is the FED-PERM output shape (median 50.6k output, used by X-cost-critic to re-price every
permitted call) and the FED-PERM QeQ reach (median 30 outside refs, used by D and the executive summary) a
permission effect, or a v11-brief effect? Every FED-PERM run used the v11 brief ('findings ledger, then the reading';
'Collect every finding the evidence and your knowledge of the Quran support'). Decomposes output into thinking and
visible text, and shows ledger findings. Read-only; writes z05_output_shape_confound.txt."""
import csv,statistics as st,collections,re
MT='/Volumes/OZTURK/_projects/prose_generation/_commentary/review/phase1/scripts/dilution/metrics.tsv'
CF='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/D-knowledge-supply/r3/confound.tsv'
BRIEF='/Volumes/OZTURK/_projects/prose_generation/_commentary/v9/prompts/write_v11.md'
g={(r['ayah'],r['run']):r['group'] for r in csv.DictReader(open(CF),delimiter='\t')}
M={(r['ayah'],r['run']):r for r in csv.DictReader(open(MT),delimiter='\t')}
f=lambda x: float(x) if x not in ('',None) else None
L=[]
b=open(BRIEF).read().split('\n')
L.append('v11 brief line 1: '+b[0]); L.append('v11 brief line 29: '+b[28][:160])
by=collections.defaultdict(list)
for k,grp in g.items():
    m=M.get(k)
    if not m: continue
    o,t=f(m['output_tokens']),f(m['thinking_tokens'])
    by[(grp,k[1])].append((o,t,o-t,f(m['words']),f(m['ledger_findings']),f(m['other_surah_refs'])))
for key in sorted(by):
    v=by[key]; med=lambda i:[x[i] for x in v if x[i] is not None]
    L.append(f"{key[0]:11s} {key[1]:22s} n={len(v):2d} out {st.median(med(0)):8.0f} thinking {st.median(med(1)):8.0f} visible {st.median(med(2)):7.0f} reading words {st.median(med(3)):6.0f} ledger findings {st.median(med(4)) if med(4) else '-'} other-surah refs {st.median(med(5)) if med(5) else '-'}")
open('z05_output_shape_confound.txt','w').write('\n'.join(L)+'\n'); print('\n'.join(L))
