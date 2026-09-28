"""Completeness critic check: re-score K-critic's C1-on-HFT test (K-northstar-critic/c1_on_hft.py) under C1's own
T6 protocol: rank the latent target among the word's NON-B001 branches. Also give a variant where echo-only and
absent branches are ranked at the bottom (tie-averaged) so no case is dropped. Read-only: parses the push files
K-critic already wrote (K-northstar-critic/c1_hft_out) and its case list. Writes z01_c1_hft_rerank.txt."""
import json,re,os,statistics,random
K='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/K-northstar-critic'
S=json.load(open(K+'/hft_na_set.json'))
samp=set(S['sample'])
cases=[c for c in S['all'] if c['ayah'] in samp]
def norm(r): return r.replace(' ','')
def H(n): return sum(1/k for k in range(1,n+1))
out=[];miss=[]
for c in cases:
    s,a=map(int,c['ayah'].split(':'))
    p=f'{K}/c1_hft_out/{s:03d}_{a:03d}.push.md'
    if not os.path.exists(p): continue
    push=open(p).read()
    blocks=re.split(r'\n## w\d+ ',push)
    blk=None
    for b in blocks[1:]:
        m=re.match(r'\S+ \(([^;]+);\s*(\d+) branches',b)
        if m and norm(m.group(1))==norm(c['root']): blk=b; nbr=int(m.group(2)); break
    if blk is None: continue
    lines=blk.split('\n')
    top=[re.match(r'  - (B\d+)',l).group(1) for l in lines if re.match(r'  - B\d+',l)]
    then=[];echo=[]
    for l in lines:
        if l.startswith('  - then:'): then=re.findall(r'(B\d+) «',l)
        if l.startswith('  - echo only'): echo=re.findall(r'(B\d+) «',l)
    live=[b for b in top+then if b!='B001']
    allb=[f'B{i:03d}' for i in range(1,nbr+1)]
    cand=sorted((set(live)|set(echo)|set(allb))-{'B001'},key=lambda x:int(x[1:]))
    absent=[b for b in cand if b not in live and b not in echo]
    t=c['branch']
    if t not in cand and t not in live and t not in echo:
        miss.append((c['ayah'],c['root'],t,nbr)); continue
    # variant 1: rank among live non-B001 only (drops echo/absent targets), C1 T6-like
    r1=live.index(t)+1 if t in live else None
    # variant 2: full non-B001 list: live order, then echo, then absent; ties at the bottom averaged (expected RR)
    if t in live: rr2=1/(live.index(t)+1)
    else:
        tail=echo+absent if t in echo+absent else None
        grp=echo if t in echo else absent
        start=len(live)+(0 if t in echo else len(echo))
        rr2=sum(1/(start+k) for k in range(1,len(grp)+1))/len(grp)
    out.append(dict(dictrank=cand.index(t)+1,ayah=c['ayah'],root=c['root'],b=t,n_live=len(live),n_cand=len(cand),r1=r1,rr2=rr2,
                    top3=t in top[:4] and t!='B001' and (top.index(t)+1 - (1 if 'B001' in top[:top.index(t)] else 0))<=3 if t in top else False))
r1=[o for o in out if o['r1']]
mrr1=statistics.mean(1/o['r1'] for o in r1)
rnd1=statistics.mean(H(o['n_live'])/o['n_live'] for o in r1)
top3_1=sum(o['r1']<=3 for o in r1); exp3_1=sum(min(3,o['n_live'])/o['n_live'] for o in r1)
mrr2=statistics.mean(o['rr2'] for o in out); rnd2=statistics.mean(H(o['n_cand'])/o['n_cand'] for o in out)
# dictionary-id order among non-B001 (B002 first)
dict2=statistics.mean(1/o['dictrank'] for o in out)
L=[]
L.append(f'cases scored {len(out)} (of {len(cases)}); targets live {len(r1)}')
L.append(f'V1 (rank among live non-B001, C1 T6 protocol): C1 MRR {mrr1:.3f} vs random {rnd1:.3f}; top-3 {top3_1}/{len(r1)} vs expected {exp3_1:.1f}')
L.append(f'V2 (all non-B001 branches; echo then absent at bottom, tie-averaged): C1 MRR {mrr2:.3f} vs random {rnd2:.3f}; dictionary-id order {dict2:.3f}')
L.append(f'targets not among the root\'s dictionary branches (skipped): {len(miss)} {miss[:8]}')
L.append('K-critic (B001 kept in the list, echo/absent dropped): C1 0.296 vs random 0.355')
open('z01_c1_hft_rerank.txt','w').write('\n'.join(L)+'\n'); print('\n'.join(L))
json.dump(out,open('z01_c1_hft_rerank.json','w'),ensure_ascii=False,indent=0)
# bootstrap by ayah (cluster) for the V2 difference C1 - random and C1 - dictionary order
import collections
random.seed(7)
by=collections.defaultdict(list)
for o in out: by[o['ayah']].append((o['rr2']-H(o['n_cand'])/o['n_cand'], o['rr2']-1/o['dictrank']))
ays=list(by); D1=[];D2=[]
for _ in range(5000):
    smp=[x for a in random.choices(ays,k=len(ays)) for x in by[a]]
    D1.append(statistics.mean(x[0] for x in smp)); D2.append(statistics.mean(x[1] for x in smp))
D1.sort();D2.sort()
line=f'bootstrap (by ayah, 5000): C1-random {statistics.mean(D1):+.3f} [95% {D1[125]:+.3f},{D1[4875]:+.3f}]; C1-dict {statistics.mean(D2):+.3f} [{D2[125]:+.3f},{D2[4875]:+.3f}]'
print(line); open('z01_c1_hft_rerank.txt','a').write(line+'\n')
