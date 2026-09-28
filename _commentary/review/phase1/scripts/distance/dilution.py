import json, glob, random, collections, numpy as np
exec(open('scene_vs_rank.py').read().split("random.seed(7)")[0])  # reuse loaders, tags, fused_ranks, by_scene
random.seed(11)
sources=[i for i in tags if concrete(tags[i])]
sample=random.sample(sources,600)
strat=collections.defaultdict(list)
for a in sample:
    rk,elig=fused_ranks(a)
    ca=concrete(tags[a]); sa={t[0] for t in ca}
    for s in sa:
        for j in by_scene[s]:
            if j==a or not elig[j]: continue
            sb={t[0] for t in concrete(tags[j])}
            same_role = bool({t for t in ca if t[0]==s} & {t for t in concrete(tags[j]) if t[0]==s})
            if same_role: continue
            nab=len(sa)+len(sb)
            strat[min(nab,8)].append(rk[j])
for k in sorted(strat):
    v=np.array(strat[k]); print('sum of concrete scenes of the pair =',k,'n=',len(v),'median rank',int(np.median(v)),'share<=100',round(float(np.mean(v<=100)),3))
