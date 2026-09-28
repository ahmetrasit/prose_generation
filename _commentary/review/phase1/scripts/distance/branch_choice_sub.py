exec(open('branch_choice_eval.py').read().split("res = {s: [] for s in SIGNALS}")[0])
sub=[(a,b) for a,b in tests if bnum[a]!=1 and bnum[b]!=1]
print('both non-B001 cases', len(sub))
rnd=np.mean([1/len(by_root[rid[b]]) for a,b in sub]); print('random MRR', round(rnd,3))
for name in ['slm_fused','slm_neo','luna_scene','luna_scene_other_role','qnet_kw','dict_neighbor','prior_B001_first']:
    fn=SIGNALS[name]; out=[]
    for a,b in sub:
        cands=by_root[rid[b]]; sc={c:fn(a,c) for c in cands}; v=sc[b]
        rank=sum(1 for c in cands if sc[c]>v)+1+(sum(1 for c in cands if sc[c]==v)-1)/2; out.append(1/rank)
    print(f'{name:24s} MRR={np.mean(out):.3f}')
