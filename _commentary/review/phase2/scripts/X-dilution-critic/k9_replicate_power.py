# K9: can a 2-replicate plan detect a single watch item being dropped at a handover?
# Model: an item lands in a run with probability p (identical runs share ~60% of citations: Phase 1 §4.3, so single-item
# landing is far from deterministic). Criterion "present in >=1 of 2" (A V1) and "present in 2 of 2" (A 'robust',
# C1 V3) evaluated for a design that keeps the item at p=0.8 vs one that drops it to p=0.3.
from math import comb
def p_atleast(k,n,p): return sum(comb(n,i)*p**i*(1-p)**(n-i) for i in range(k,n+1))
for p in (0.9,0.8,0.6,0.4,0.3,0.2):
    print(f"p={p}: pass '>=1 of 2' {p_atleast(1,2,p):.2f} | pass '2 of 2' {p_atleast(2,2,p):.2f} | pass '>=3 of 4' {p_atleast(3,4,p):.2f} | pass '>=6 of 8' {p_atleast(6,8,p):.2f}")
# per-item: probability that the rule distinguishes p=0.8 (good) from p=0.3 (lossy): P(good passes and lossy fails)
for k,n in ((1,2),(2,2),(3,4),(6,8)):
    g=p_atleast(k,n,0.8); l=p_atleast(k,n,0.3)
    print(f"rule >= {k} of {n}: good passes {g:.2f}, lossy passes {l:.2f}, separates both ways {g*(1-l):.2f}")
