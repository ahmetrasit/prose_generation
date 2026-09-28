"""A's F7 pair layer (quran-slm fused affinity, top-30 pushed) on the independent HFT neighbour-activation set:
rank of the (outlier branch, HFT activator branch) pair among all cross-word pairs of the ayah; share inside the
pushed top 30. Read-only import of A's s06/s11 code; writes nothing outside this dir."""
import sys,os,json,statistics
HERE=os.path.dirname(os.path.abspath(__file__))
A='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/A-v5-step'
sys.dont_write_bytecode=True
cwd=os.getcwd(); os.chdir(A)
src=open(os.path.join(A,'s11_pair_layer.py')).read().split("cases={")[0]
src=src.replace("os.path.dirname(os.path.abspath(__file__))",repr(A))
sys.argv=['x']; exec(src)
os.chdir(cwd)
S=json.load(open(os.path.join(HERE,'hft_na_set.json')))
cases=[c for c in S['all'] if c['ayah'] in set(S['sample'])]
out=[]; cache={}
for c in cases:
    ref=c['ayah']
    if ref not in cache:
        try: cache[ref]=pairs(ref)
        except Exception as e: cache[ref]=None; print('fail',ref,e)
    P=cache[ref]
    if not P: continue
    idx={}
    for k,(s,a,b) in enumerate(P):
        idx.setdefault((a,b),k+1); idx.setdefault((b,a),k+1)
    t=f"{c['root']} {c['branch']}"
    rks=[idx.get((t,f'{r} {bb}')) for r,bb in c['activators']]
    rks=[r for r in rks if r]
    out.append(dict(ayah=ref,target=t,best_rank=min(rks) if rks else None,n_pairs=len(P)))
ok=[o for o in out if o['best_rank']]
print('cases',len(out),'with pair ranked',len(ok))
print('in pushed top-30:',sum(o['best_rank']<=30 for o in ok),'of',len(ok))
print('median rank',statistics.median(o['best_rank'] for o in ok),'median n_pairs',statistics.median(o['n_pairs'] for o in ok))
print('median relative rank',statistics.median(o['best_rank']/o['n_pairs'] for o in ok))
json.dump(out,open(os.path.join(HERE,'a_f7_on_hft.json'),'w'),ensure_ascii=False)
