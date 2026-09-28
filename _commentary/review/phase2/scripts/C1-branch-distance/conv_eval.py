"""CONVERGENCE ordering for neighbour activation: a branch c of word X is ordered by the largest number of independent
path types that tie it to ONE activating word Y (each type counted when above its 95th percentile over random
cross-root pairs), ties broken by similarity.  Rationale: v9's 'convergence' and the eye film in 29:38, which three
kinds of evidence (similar card, scene role, a lemma the Quran pairs with Y) tie to mustabṣirīn, while an RRF of many
noisy types rewards single strong hits.
Evaluated on: T6 (v12 NA, partner and ayah contexts, guarded), T5 (29:38 eye film, window 0 and +-3), T4 (29:38
links), S1 anchors at ayah level (rank of each S1 gold anchor among all branches of its Fatiha ayah).  Read-only."""
import sys, json, random, collections, math, csv, glob
sys.dont_write_bytecode = True
import numpy as np
import common as C, metrics as M, guard as G, metrics2 as M2
from rr import exp_rr

TYPES = ['slm_neo', 'clause_max', 'mention_shared', 'xref_idf', 'bridge_dir', 'scene_other', 'dict_rel', 'dict_contrast']
W = {w['ref']: w for w in C.WORDS}


def _f95():
    random.seed(4); v = collections.defaultdict(list)
    for _ in range(6000):
        p, q = random.randrange(C.N), random.randrange(C.N)
        if C.ROOTKEY[p] == C.ROOTKEY[q]: continue
        for t in TYPES: v[t].append(M.METRICS[t](p, q))
    return {t: sorted(xs)[int(0.95 * len(xs))] for t, xs in v.items()}
F95 = C.cached('floors95', _f95)
print('95th-percentile floors', {k: round(v, 4) for k, v in F95.items()})

_pm = {}
def pair_mat(t, rx, ry):
    k = (t, rx, ry)
    if k not in _pm:
        f = M.METRICS[t]
        if len(_pm) > 300000: _pm.clear()
        _pm[k] = np.array([[f(a, b) for b in C.BY_ROOT[ry]] for a in C.BY_ROOT[rx]], dtype=np.float64)
    return _pm[k]
_st = {}
def st(i, w):
    k = (i, w['ref'])
    if k not in _st: _st[k] = G.status(i, w)[0]
    return _st[k]


def scores(x, ctx, guard=True, window_weight=None):
    """returns dict ordering -> np.array over the branches of x's root"""
    rx = x['roots'][0]; cx = C.BY_ROOT[rx]
    conv = np.zeros(len(cx)); simmax = np.zeros(len(cx)); best_y = [None] * len(cx)
    for y in ctx:
        if not y['roots'] or y['roots'][0] == rx or y['ref'] == x['ref'] or y['roots'][0] not in C.BY_ROOT: continue
        ry = y['roots'][0]
        ok = [j for j, yb in enumerate(C.BY_ROOT[ry]) if not guard or st(yb, y) != 'absent']
        if not ok: continue
        cnt = np.zeros(len(cx))
        for t in TYPES:
            m = pair_mat(t, rx, ry)[:, ok].max(axis=1)
            cnt += (m > F95[t])
            if t == 'slm_neo': simmax = np.maximum(simmax, m)
        for j in range(len(cx)):
            if cnt[j] > conv[j]: conv[j] = cnt[j]; best_y[j] = y['ref']
    dem = np.array([-1e6 if (guard and st(c, x) == 'absent') else 0.0 for c in cx])
    return dict(convergence=conv + 10 * simmax + dem, slm_neo=simmax + dem), best_y


res = {}
# ---------------- T6 on the same 6,000 v12 cases as na_eval.py
exec(open(C.HERE + '/na_eval.py').read().split("TYPES = [")[0].split("W = {w['ref']: w for w in C.WORDS}", 1)[1])
print('T6 cases', len(cases))
for ctxname in ('partner', 'ayah'):
    per = collections.defaultdict(list)
    for b, wx, partners, ayahw, s in cases:
        x = W[wx]; cx = C.BY_ROOT[C.ROOTKEY[b]]
        if b not in cx or x['roots'][0] != C.ROOTKEY[b]: continue
        ctx = [W[r] for r in (partners if ctxname == 'partner' else ayahw)]
        sc, _ = scores(x, ctx)
        if C.BNUM[b] == 1: continue
        nonprim = np.array([C.BNUM[c] != 1 for c in cx]); ti = cx.index(b); tj = int(nonprim[:ti].sum())
        for name, v in sc.items():
            sub = v[nonprim]
            per[name + '_MRR_latent'].append(exp_rr(sub, tj))
            better = int((sub > sub[tj]).sum()); ties = int((sub == sub[tj]).sum())
            per[name + '_R@3_latent'].append(max(0.0, min(1.0, (3 - better) / ties)))
    res[f'T6_{ctxname}_guarded'] = {k: round(float(np.mean(v)), 3) for k, v in per.items()} | {'n': len(per['convergence_MRR_latent'])}
    print(ctxname, res[f'T6_{ctxname}_guarded'])

# ---------------- T5 watch: eye film in 29:38
AY = [w for w in C.BY_AYAH[(29, 38)] if w['roots'] and w['roots'][0] in C.BY_ROOT]
sab = [i for i in C.BY_ROOT['س ب ل'] if C.BID[i] == 'B010'][0]
for wdw in (0, 3):
    ctx = [w for k in C.window(29, 38, wdw) for w in C.BY_AYAH[k] if w['roots']]
    allsc = {}; by = {}
    for x in AY:
        sc, bys = scores(x, ctx)
        for j, c in enumerate(C.BY_ROOT[x['roots'][0]]):
            allsc[c] = sc['convergence'][j]; by[c] = bys[j]
    sabsc = {c: allsc[c] for c in C.BY_ROOT['س ب ل']}
    lat = {c: v for c, v in allsc.items() if C.BNUM[c] != 1}
    res[f'T5_eye_film_win{wdw}_convergence'] = dict(rank_in_sabil=C.rank_of(sabsc, sab), of=len(sabsc), rank_among_latent=C.rank_of(lat, sab), of_all=len(lat),
                                                    types_converging=int(allsc[sab] // 10 if False else math.floor(allsc[sab])), activator=by[sab])
    top = sorted(lat.items(), key=lambda kv: -kv[1])[:8]
    res[f'T5_eye_film_win{wdw}_top8_latent'] = [(C.DISP[c], C.TEXT[c][0], round(v, 2), by[c]) for c, v in top]
    print(wdw, res[f'T5_eye_film_win{wdw}_convergence']); print('   top', res[f'T5_eye_film_win{wdw}_top8_latent'])

# ---------------- S1 anchors at ayah level: rank of each gold anchor among all branches of its Fatiha ayah (window = surah)
gold = [json.loads(l) for l in open(f'{C.SLM}/reports/s1_ar3_v1_gold_ledger.jsonl')]
anchors = set()
for g in gold:
    if not g['eligibility']['eligible']: continue
    for n in g['required_branch_anchors'] + [x for grp in g['required_branch_anchor_groups'] for x in grp['node_ids']]:
        if n in C.NODE: anchors.add(C.NODE[n])
s1 = collections.defaultdict(list)
for a in range(1, 8):
    AYa = [w for w in C.BY_AYAH[(1, a)] if w['roots'] and w['roots'][0] in C.BY_ROOT]
    ctx = [w for k in C.window(1, a, 7) for w in C.BY_AYAH[k] if w['roots']]
    allsc = {}; sl = {}
    for x in AYa:
        sc, _ = scores(x, ctx)
        for j, c in enumerate(C.BY_ROOT[x['roots'][0]]):
            allsc[c] = max(allsc.get(c, -1e9), sc['convergence'][j]); sl[c] = max(sl.get(c, -1e9), sc['slm_neo'][j])
    lat = [c for c in allsc if C.BNUM[c] != 1]
    for c in anchors:
        if c in allsc and C.BNUM[c] != 1:
            for name, d in (('convergence', allsc), ('slm_neo', sl)):
                s1[name].append(C.rank_of({k: d[k] for k in lat}, c) / len(lat))
res['S1_anchor_relative_rank_among_latent_branches_of_their_ayah'] = {k: dict(median=round(float(np.median(v)), 3), top10pct=int(sum(1 for x in v if x <= 0.1)),
                                                                            top25pct=int(sum(1 for x in v if x <= 0.25)), n=len(v)) for k, v in s1.items()}
print(res['S1_anchor_relative_rank_among_latent_branches_of_their_ayah'])
json.dump(res, open(C.HERE + '/conv_eval.json', 'w'), ensure_ascii=False, indent=1)
