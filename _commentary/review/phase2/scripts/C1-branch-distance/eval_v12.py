"""T1: conditional branch choice on independent v12 strong findings (Phase 1 protocol, extended metrics),
    plus a learned conditional-logit combination with surah-grouped 5-fold CV (Q2b), with and without the
    B001 prior, and the construction guard as a feature.
T2: strong vs reject separation of cross-root pairs (AUC per metric; guard indicator)."""
import csv, glob, collections, itertools, random, json, math, sys, time
sys.dont_write_bytecode = True
import numpy as np
import common as C, metrics as M, guard as G
W = {w['ref']: w for w in C.WORDS}
V = f'{C.P}/latent_activation/_status/v12_cross_run'
F = collections.defaultdict(dict); GR = {}; SUR = {}
for f in glob.glob(f'{V}/s[0-9][0-9][0-9]/derived/finding_word_branches.v3.tsv'):
    for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
        k = (f, r['finding_id']); GR[k] = r['grade']; SUR[k] = int(r['ayah_ref'].split(':')[0])
        i = C.GI.get((r['root_id'], r['branch_id']))
        if i is not None: F[k][i] = r['qac_word_ref']
# ---------------- T1 cases
tests = set()
for k, v in F.items():
    if GR[k] != 'strong': continue
    for a, b in itertools.permutations(sorted(v), 2):
        if C.RID[a] != C.RID[b] and len(C.BY_RID[C.RID[b]]) >= 3 and sum(1 for x in v if C.RID[x] == C.RID[b]) == 1:
            tests.add((a, b, v[b], SUR[k]))
tests = sorted(tests)
random.seed(1)
if len(tests) > 12000: tests = random.sample(tests, 12000)
print('T1 cases', len(tests))
FEATS = ['slm_neo', 'slm_char', 'slm_e5', 'clause_max', 'clause_top2', 'mention_shared', 'xref', 'dict_rel', 'dict_contrast', 'scene_other', 'scene_same', 'sound']
t0 = time.time()
rows = []   # per case: list of (cand, feats dict, is_target)
for a, b, wref, s in tests:
    cands = C.BY_RID[C.RID[b]]
    w = W.get(wref)
    R = []
    for c in cands:
        fv = {m: M.METRICS[m](a, c) for m in FEATS}
        fv['slm_fused'] = 0.35 * fv['slm_e5'] + 0.35 * fv['slm_neo'] + 0.30 * fv['slm_char']
        fv['prior_b001'] = 1.0 if C.BNUM[c] == 1 else 0.0
        fv['neg_bnum'] = -math.log(C.BNUM[c])
        st = G.status(c, w)[0] if w else 'free'
        fv['guard_absent'] = 1.0 if st == 'absent' else 0.0
        fv['kind_coll'] = 1.0 if C.kind_of(c) == 'collocation' else 0.0
        R.append((c, fv, c == b))
    rows.append((a, b, s, R))
print(f'features computed in {time.time() - t0:.0f}s')

def rr(R, key):
    sc = {c: key(fv) for c, fv, _ in R}
    tgt = next(c for c, _, t in R if t)
    return 1.0 / C.rank_of(sc, tgt)
def mrr(sel, key):
    return float(np.mean([rr(R, key) for a, b, s, R in sel])) if sel else float('nan')
subsets = dict(all=rows, nonB001=[x for x in rows if C.BNUM[x[1]] != 1],
               latent_latent=[x for x in rows if C.BNUM[x[0]] != 1 and C.BNUM[x[1]] != 1])
res = {}
single = ['slm_fused', 'slm_neo', 'slm_char', 'slm_e5', 'clause_max', 'clause_top2', 'mention_shared', 'xref', 'dict_rel', 'scene_other', 'scene_same', 'sound', 'prior_b001']
for m in single:
    res[m] = {k: round(mrr(v, lambda fv, m=m: fv[m]), 3) for k, v in subsets.items()}
res['random'] = {k: round(float(np.mean([1 / len(R) for a, b, s, R in v])), 3) for k, v in subsets.items()}
# guard as a demotion on slm_neo (ordering only)
res['slm_neo+guard_demote'] = {k: round(mrr(v, lambda fv: fv['slm_neo'] - 1.0 * fv['guard_absent']), 3) for k, v in subsets.items()}
res['untuned_typed_rrf'] = None
# typed RRF over per-metric ranks inside the candidate set (no learning)
def typed_rrf(R, types=('slm_neo', 'clause_max', 'mention_shared', 'scene_other', 'dict_rel', 'xref')):
    sc = collections.defaultdict(float)
    for t in types:
        vals = sorted({fv[t] for _, fv, _ in R}, reverse=True)
        for c, fv, _ in R:
            if fv[t] > 0: sc[c] += 1.0 / (2 + vals.index(fv[t]))
    return sc
def mrr_rrf(sel, **kw):
    out = []
    for a, b, s, R in sel:
        sc = typed_rrf(R, **kw); sc = {c: sc.get(c, 0.0) for c, _, _ in R}
        out.append(1 / C.rank_of(sc, b))
    return float(np.mean(out))
res['untuned_typed_rrf'] = {k: round(mrr_rrf(v), 3) for k, v in subsets.items()}

# ---------------- learned conditional logit, surah-grouped 5-fold CV
def pack(sel, feats):
    X, Y, gid = [], [], []
    for g, (a, b, s, R) in enumerate(sel):
        for c, fv, t in R:
            X.append([fv[f] for f in feats]); Y.append(1.0 if t else 0.0); gid.append(g)
    X = np.array(X, dtype=np.float64); Y = np.array(Y); gid = np.array(gid)
    starts = np.flatnonzero(np.r_[True, gid[1:] != gid[:-1]])
    return X, Y, gid, starts
def fit_clogit(sel, feats, l2=1e-2, iters=400, lr=0.5):
    X, Y, gid, starts = pack(sel, feats)
    mu = X.mean(0); sd = X.std(0) + 1e-9; X = (X - mu) / sd
    w = np.zeros(X.shape[1]); ng = len(starts)
    for it in range(iters):
        z = X @ w; z = z - np.maximum.reduceat(z, starts)[gid]
        p = np.exp(z); p = p / np.add.reduceat(p, starts)[gid]
        g = X.T @ (p - Y) / ng + l2 * w
        w -= lr * g
    return w, mu, sd
def mrr_model(sel, feats, w, mu, sd):
    out = []
    for a, b, s, R in sel:
        x = (np.array([[fv[f] for f in feats] for _, fv, _ in R]) - mu) / sd
        sc = {c: float(v) for (c, _, _), v in zip(R, x @ w)}
        out.append(1 / C.rank_of(sc, b))
    return float(np.mean(out)) if out else float('nan')
surahs = sorted({s for a, b, s, R in rows}); random.seed(7); random.shuffle(surahs)
folds = [set(surahs[k::5]) for k in range(5)]
LFEATS = dict(
    learned_no_prior=['slm_neo', 'slm_char', 'slm_e5', 'clause_max', 'clause_top2', 'mention_shared', 'xref', 'dict_rel', 'dict_contrast', 'scene_other', 'scene_same', 'sound'],
    learned_no_prior_guard=['slm_neo', 'slm_char', 'slm_e5', 'clause_max', 'clause_top2', 'mention_shared', 'xref', 'dict_rel', 'dict_contrast', 'scene_other', 'scene_same', 'sound', 'guard_absent', 'kind_coll'],
    learned_with_prior=['slm_neo', 'slm_char', 'slm_e5', 'clause_max', 'clause_top2', 'mention_shared', 'xref', 'dict_rel', 'dict_contrast', 'scene_other', 'scene_same', 'sound', 'prior_b001', 'neg_bnum'],
    learned_slm_only=['slm_neo', 'slm_char', 'slm_e5'])
weights = {}
for name, feats in LFEATS.items():
    agg = collections.defaultdict(list)
    for k, fold in enumerate(folds):
        tr = [x for x in rows if x[2] not in fold]; te = [x for x in rows if x[2] in fold]
        w, mu, sd = fit_clogit(tr, feats)
        for sname, sub in subsets.items():
            tes = [x for x in sub if x[2] in fold]
            agg[sname].append((mrr_model(tes, feats, w, mu, sd), len(tes)))
        if k == 0: weights[name] = dict(zip(feats, [round(float(v), 3) for v in w]))
    res[name + ' (5-fold surah CV)'] = {s: round(sum(m * n for m, n in v) / sum(n for m, n in v), 3) for s, v in agg.items()}
# learning curve for the no-prior model: fraction of training surahs
lc = {}
for frac in (0.1, 0.25, 0.5, 1.0):
    vals = []
    for k, fold in enumerate(folds):
        trs = [s for s in surahs if s not in fold]; random.seed(k); trs = random.sample(trs, max(2, int(len(trs) * frac)))
        tr = [x for x in rows if x[2] in set(trs)]; te = [x for x in subsets['nonB001'] if x[2] in fold]
        w, mu, sd = fit_clogit(tr, LFEATS['learned_no_prior'], iters=200)
        vals.append((mrr_model(te, LFEATS['learned_no_prior'], w, mu, sd), len(te)))
    lc[frac] = round(sum(m * n for m, n in vals) / sum(n for m, n in vals), 3)
res['learning_curve_nonB001_no_prior'] = lc
print(json.dumps(res, indent=1, ensure_ascii=False))
print('fold-0 weights', json.dumps(weights, ensure_ascii=False))
# final model trained on all surahs except 1 and 29 (for the independent S1 / 29:38 evaluations)
tr = [x for x in rows if x[2] not in (1, 29)]
w, mu, sd = fit_clogit(tr, LFEATS['learned_no_prior'])
json.dump(dict(feats=LFEATS['learned_no_prior'], w=w.tolist(), mu=mu.tolist(), sd=sd.tolist()), open(C.HERE + '/learned_no_prior.json', 'w'))

# ---------------- T2 strong vs reject pairs
pairs = collections.defaultdict(set)
for k, v in F.items():
    for a, b in itertools.combinations(sorted(v), 2):
        if C.ROOTKEY[a] != C.ROOTKEY[b]:
            pairs[GR[k]].add((a, b, v[a], v[b]))
random.seed(5)
S = random.sample(sorted(pairs['strong']), 3000); Rj = sorted(pairs['reject'])
def auc(pos, neg):
    pos = np.array(pos); neg = np.array(neg)
    allv = np.concatenate([pos, neg]); order = allv.argsort(kind='mergesort')
    ranks = np.empty(len(allv)); ranks[order] = np.arange(1, len(allv) + 1)
    # average ties
    vals, inv, cnt = np.unique(allv, return_inverse=True, return_counts=True)
    sums = np.bincount(inv, ranks); ranks = sums[inv] / cnt[inv]
    return float((ranks[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))
t2 = {}
for m in ['slm_fused', 'slm_neo', 'clause_max', 'mention_shared', 'xref', 'dict_rel', 'scene_other', 'scene_same', 'bridge']:
    f = M.METRICS[m]
    t2[m] = round(auc([max(f(a, b), f(b, a)) for a, b, wa, wb in S], [max(f(a, b), f(b, a)) for a, b, wa, wb in Rj]), 3)
def gpair(a, b, wa, wb):
    x = G.status(a, W[wa])[0] if wa in W else 'free'; y = G.status(b, W[wb])[0] if wb in W else 'free'
    return 0.0 if 'absent' in (x, y) else 1.0
gs = [gpair(*p) for p in S]; gr = [gpair(*p) for p in Rj]
t2['guard (1 = no absent-collocation branch)'] = round(auc(gs, gr), 3)
t2['share of pairs with an absent-collocation branch'] = dict(strong=round(1 - float(np.mean(gs)), 3), reject=round(1 - float(np.mean(gr)), 3))
t2['n'] = dict(strong=len(S), reject=len(Rj))
print('T2 AUC strong vs reject:', json.dumps(t2, ensure_ascii=False))
json.dump(dict(T1=res, T1_weights_fold0=weights, T2=t2), open(C.HERE + '/eval_v12.json', 'w'), ensure_ascii=False, indent=1)
