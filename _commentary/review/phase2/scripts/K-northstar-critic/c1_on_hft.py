"""Run C1's harvest2 (read-only import; outputs only to this dir) on the 40 sampled HFT neighbour-activation ayat and
measure where each HFT outlier branch lands in C1's per-word order: rank among the word's live branches, whether it
is pushed with paths (top-3/pointer) vs 'then:' vs echo-only, and whether its displayed activator is the HFT
neighbour root. Baselines: dictionary id order and random. Writes c1_on_hft.json / .txt."""
import sys,os,json,re,statistics,pickle
sys.dont_write_bytecode=True
HERE=os.path.dirname(os.path.abspath(__file__))
C1='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/C1-branch-distance'
sys.path.insert(0,C1); cwd=os.getcwd(); os.chdir(C1)
import common as C
_orig=C.cached
def cached_ro(name,fn):
    p=os.path.join(C.CACHE,name+'.pkl')
    if os.path.exists(p): return pickle.load(open(p,'rb'))
    return fn()          # never write into C1's cache
C.cached=cached_ro
import harvest2 as H
os.chdir(cwd)
H.OUT=os.path.join(HERE,'c1_hft_out'); os.makedirs(H.OUT,exist_ok=True)
S=json.load(open(os.path.join(HERE,'hft_na_set.json')))
cases=[c for c in S['all'] if c['ayah'] in set(S['sample'])]
res=[]; done={}
for ay in S['sample']:
    s,a=map(int,ay.split(':'))
    try:
        push,pull,pushed=H.fmt(s,a)
    except Exception as e:
        print('fail',ay,e); continue
    open(os.path.join(H.OUT,f'{s:03d}_{a:03d}.push.md'),'w').write(push)
    done[ay]=(push,pull)
    print(ay,len(push),flush=True)
def norm(r): return r.replace(' ','')
for c in cases:
    if c['ayah'] not in done: continue
    push,pull=done[c['ayah']]
    rows=[r for r in pull['rows'] if norm(r['card'].split(' B')[0])==norm(c['root'])]
    # per word blocks in push: find block whose root matches
    blocks=re.split(r'\n## w\d+ ',push)
    blk=None
    for b in blocks[1:]:
        m=re.match(r'\S+ \(([^;]+);',b)
        if m and norm(m.group(1))==norm(c['root']): blk=b; break
    if blk is None: res.append(dict(c,status='root_not_in_push')); continue
    lines=blk.split('\n')
    top=[re.match(r'  - (B\d+)',l).group(1) for l in lines if re.match(r'  - B\d+',l)]
    then=[]; echo=[]
    for l in lines:
        if l.startswith('  - then:'): then=re.findall(r'(B\d+) «',l)
        if l.startswith('  - echo only'): echo=re.findall(r'(B\d+) «',l)
    order=top+then
    n=len(order)+len(echo)
    if c['branch'] in top: st='pushed_with_paths'; rk=top.index(c['branch'])+1
    elif c['branch'] in then: st='listed_then'; rk=order.index(c['branch'])+1
    elif c['branch'] in echo: st='echo_only'; rk=None
    else: st='absent'; rk=None
    line=next((l for l in lines if l.startswith(f"  - {c['branch']} ")),'')
    act_hit=any(norm(r0) in norm(line) or False for r0,_ in c['activators'])
    # activator surface check: does the displayed '← word' belong to an HFT activator root? approximate via pull row
    prow=next((r for r in rows if r['card'].endswith(c['branch'])),None)
    act_roots=set()
    if prow:
        for t,(v,yc,yw) in prow['paths'].items(): act_roots.add(norm(yc.split(' B')[0]))
    hit=any(norm(r0) in act_roots for r0,_ in c['activators'])
    bnum=int(c['branch'][1:])
    res.append(dict(c,status=st,rank=rk,n_live=len(order),n_all=n,dict_rank=sorted([int(x[1:]) for x in order+echo]).index(bnum)+1 if c['branch'] in order+echo else None,
                    hft_activator_among_best_paths=hit))
json.dump(res,open(os.path.join(HERE,'c1_on_hft.json'),'w'),ensure_ascii=False,indent=0)
from collections import Counter
print(Counter(r['status'] for r in res))
rr=[r for r in res if r.get('rank')]
if rr:
    print('median C1 rank',statistics.median(r['rank'] for r in rr),'median dict-order rank',statistics.median(r['dict_rank'] for r in rr),
          'median random expectation',statistics.median((r['n_live']+1)/2 for r in rr))
    print('C1 MRR',sum(1/r['rank'] for r in rr)/len(rr),'dict-order MRR',sum(1/r['dict_rank'] for r in rr)/len(rr))
    print('top-1',sum(r['rank']==1 for r in rr),'top-3',sum(r['rank']<=3 for r in rr),'of',len(rr))
print('HFT activator root among the branch best-path activators:',sum(r.get('hft_activator_among_best_paths',False) for r in res),'of',len(res))
