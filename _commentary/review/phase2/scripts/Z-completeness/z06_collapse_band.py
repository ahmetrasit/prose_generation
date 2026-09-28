"""Completeness critic check: is 'thinking collapses at >=~140k billed tokens' (the hard cap every proposal and
critic uses) a size effect or an arm (package-composition) effect? Lists thinking vs billed input for every fed arm
in Phase 1 metrics.tsv, grouped by arm. Read-only; writes z06_collapse_band.txt."""
import csv,collections,statistics as st
MT='/Volumes/OZTURK/_projects/prose_generation/_commentary/review/phase1/scripts/dilution/metrics.tsv'
by=collections.defaultdict(list)
for r in csv.DictReader(open(MT),delimiter='\t'):
    if not r['run'].startswith(('v9:w10-opus','v9:v11','v11:out')): continue
    try: b=float(r['billed_input_total']); t=float(r['thinking_tokens'])
    except: continue
    by[r['run']].append((b,t,r['ayah']))
L=[]
for arm,v in sorted(by.items()):
    lo=[t for b,t,a in v if b<140000]; hi=[t for b,t,a in v if b>=140000]
    L.append(f"{arm:22s} n={len(v):2d} thinking median <140k: {st.median(lo) if lo else '-':>8} (n={len(lo)})  >=140k: {st.median(hi) if hi else '-':>8} (n={len(hi)})  max billed {max(b for b,_,_ in v):.0f}")
big=sorted([(b,t,a,arm) for arm,v in by.items() for b,t,a in v if b>=140000])
L.append('runs >=140k billed: '+'; '.join(f"{a} {arm.split(':')[1]} {b/1000:.0f}k->{t/1000:.1f}k" for b,t,a,arm in big))
open('z06_collapse_band.txt','w').write('\n'.join(L)+'\n'); print('\n'.join(L))
