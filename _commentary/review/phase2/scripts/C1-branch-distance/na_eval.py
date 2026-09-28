"""T6 NEIGHBOUR ACTIVATION on independent v12 strong findings (the harvest's actual task).

Unlike T1 (Phase 1 protocol: the partner BRANCH is given), here only the context is given:
  context 'partner' : the other words the v12 reader cited in the finding (their branches unknown)
  context 'ayah'    : every other content word of the ayah (no reader information at all)
For a cited branch b of word X (root with >=3 branches, one branch of that root cited), every branch c of X's root is
scored NA(c) = max over context words Y (other root) and over ALL branches y of Y's root of metric(c, y); we report the
rank of b.  Measures: MRR over all branches; MRR for non-B001 targets; MRR of a non-B001 target among the NON-primary
branches only (the harvest orders latent branches; the plain sense is given anyway); recall@3 in that list.
Guard variants: 'g' = context branches whose construction is absent at Y cannot activate (they are not senses of Y
there), and candidate branches whose construction is absent at X are ordered last (never removed).
Typed union = reciprocal-rank fusion (k=2) of the per-type ranks, a type counting only where it scores > 0.
Read-only; sample sizes printed."""
import csv, glob, collections, itertools, random, json, math, sys, time
sys.dont_write_bytecode = True
import numpy as np
import common as C, metrics as M, guard as G, metrics2  # metrics2 registers xref_idf, bridge_lemma
from rr import exp_rr

W = {w['ref']: w for w in C.WORDS}
V = f'{C.P}/latent_activation/_status/v12_cross_run'
F = collections.defaultdict(list); GR = {}
for f in glob.glob(f'{V}/s[0-9][0-9][0-9]/derived/finding_word_branches.v3.tsv'):
    for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
        k = (f, r['finding_id']); GR[k] = r['grade']
        i = C.GI.get((r['root_id'], r['branch_id']))
        if i is not None and r['qac_word_ref'] in W:
            F[k].append((i, r['qac_word_ref']))

def root_of_word(wref):
    w = W[wref]
    return w['roots'][0] if w['roots'] else None

cases = []
for k, v in F.items():
    if GR[k] != 'strong':
        continue
    for b, wx in v:
        rx = C.ROOTKEY[b]
        if root_of_word(wx) != rx or len(C.BY_ROOT.get(rx, [])) < 3:
            continue
        if sum(1 for x, _ in v if C.ROOTKEY[x] == rx) != 1:
            continue
        partners = sorted({wy for y, wy in v if root_of_word(wy) and root_of_word(wy) != rx})
        if not partners:
            continue
        s, a, _ = map(int, wx.split(':'))
        ayahw = [w['ref'] for w in C.BY_AYAH[(s, a)] if w['roots'] and w['roots'][0] != rx]
        cases.append((b, wx, tuple(partners), tuple(ayahw), s))
cases = sorted(set(cases))
random.seed(11)
N_CASES = int(sys.argv[1]) if len(sys.argv) > 1 else 2500
cases = random.sample(cases, min(N_CASES, len(cases)))
print('T6 cases', len(cases), 'share B001 targets', round(float(np.mean([C.BNUM[c[0]] == 1 for c in cases])), 3))

TYPES = ['slm_fused', 'slm_neo', 'clause_max', 'mention_shared', 'xref', 'xref_idf', 'bridge', 'bridge_lemma', 'bridge_dir', 'scene_other', 'scene_same', 'dict_rel', 'dict_contrast']
UNION = ['slm_neo', 'clause_max', 'mention_shared', 'xref', 'bridge', 'scene_other', 'dict_rel']
UNION2 = ['slm_neo', 'clause_max', 'mention_shared', 'xref_idf', 'bridge_dir', 'scene_other', 'dict_rel', 'dict_contrast']
FL = metrics2.FLOORS

_st = {}
def status(i, wref):
    key = (i, wref)
    if key not in _st:
        _st[key] = G.status(i, W[wref])[0]
    return _st[key]

_pair = {}
def pair_mat(t, rx, ry):
    """metric values between every branch of root rx (rows) and root ry (cols)"""
    key = (t, rx, ry)
    if key not in _pair:
        if len(_pair) > 400000:
            _pair.clear()
        cx, cy = C.BY_ROOT[rx], C.BY_ROOT[ry]
        f = M.METRICS[t]
        _pair[key] = np.array([[f(a, b) for b in cy] for a in cx], dtype=np.float64)
    return _pair[key]

def na_scores(rx, ctx_words, t, guard):
    cx = C.BY_ROOT[rx]
    best = np.zeros(len(cx))
    for wy in ctx_words:
        ry = root_of_word(wy)
        if ry is None or ry == rx or ry not in C.BY_ROOT:
            continue
        m = pair_mat(t, rx, ry)
        if guard:
            ok = np.array([status(y, wy) != 'absent' for y in C.BY_ROOT[ry]])
            if not ok.any():
                continue
            m = m[:, ok]
        best = np.maximum(best, m.max(axis=1))
    return best

def rank_pos(scores, idx):
    v = scores[idx]
    return 1 + (scores > v).sum() + ((scores == v).sum() - 1) / 2

def evaluate(ctx_name, guard):
    per = collections.defaultdict(lambda: collections.defaultdict(list))
    for b, wx, partners, ayahw, s in cases:
        rx = C.ROOTKEY[b]; cx = C.BY_ROOT[rx]; ti = cx.index(b)
        ctx = partners if ctx_name == 'partner' else ayahw
        demote = np.array([-1e6 if (guard and status(c, wx) == 'absent') else 0.0 for c in cx])
        nonprim = np.array([C.BNUM[c] != 1 for c in cx])
        S = {}
        for t in TYPES:
            S[t] = na_scores(rx, ctx, t, guard) + demote
        # typed union (RRF over per-type ranks, a type counts only where > 0)
        u = np.zeros(len(cx))
        for t in UNION:
            sc = S[t]
            order = sorted(set(sc[sc > 0].tolist()), reverse=True)
            for j, v in enumerate(sc):
                if v > 0:
                    u[j] += 1.0 / (2 + order.index(v))
        S['typed_union'] = u + demote
        u2 = np.zeros(len(cx))
        for t in UNION2:
            sc = S[t]
            order = sorted(set(sc[sc > 0].tolist()), reverse=True)
            for j, v in enumerate(sc):
                if v > 0:
                    u2[j] += 1.0 / (2 + order.index(v))
        S['typed_union2'] = u2 + demote
        u3 = np.zeros(len(cx))                   # floor-gated: a type counts only above its random-pair 90th percentile
        for t in UNION2:
            sc = S[t]
            order = sorted(set(sc[sc > FL[t]].tolist()), reverse=True)
            for j, v in enumerate(sc):
                if v > FL[t]:
                    u3[j] += 1.0 / (2 + order.index(v))
        S['typed_union_floor'] = u3 + demote + 1e-3 * S['slm_neo']   # slm_neo breaks ties
        S['prior_B001'] = np.array([1.0 if C.BNUM[c] == 1 else 0.0 for c in cx]) + demote
        S['random'] = None
        for name, sc in S.items():
            if sc is None:                       # exact expected values of a random order: MRR = H_n / n
                hm = lambda n: sum(1.0 / k for k in range(1, n + 1)) / n
                per[name]['all'].append(hm(len(cx)))
                if C.BNUM[b] != 1:
                    per[name]['nonB001'].append(hm(len(cx)))
                    n = int(nonprim.sum()); per[name]['latent_among_latent'].append(hm(n)); per[name]['latent_R@3'].append(min(1.0, 3 / n))
                continue
            rr_ = exp_rr(sc, ti)
            per[name]['all'].append(rr_)
            if C.BNUM[b] != 1:
                per[name]['nonB001'].append(rr_)
                sub = sc[nonprim]; tj = int(nonprim[:ti].sum())
                per[name]['latent_among_latent'].append(exp_rr(sub, tj))
                # recall@3 under random tie-breaking
                better = int((sub > sub[tj]).sum()); ties = int((sub == sub[tj]).sum())
                per[name]['latent_R@3'].append(max(0.0, min(1.0, (3 - better) / ties)))
    return {name: {k: round(float(np.mean(v)), 3) for k, v in d.items()} | {'n_nonB001': len(d['nonB001'])} for name, d in per.items()}

t0 = time.time()
res = {}
for ctx in ('partner', 'ayah'):
    for guard in (False, True):
        key = f"{ctx}{'_guarded' if guard else ''}"
        res[key] = evaluate(ctx, guard)
        print(key, f'{time.time() - t0:.0f}s')
        for name, v in res[key].items():
            print(f'   {name:14s}', v)
json.dump(dict(n_cases=len(cases), results=res), open(C.HERE + '/na_eval3.json', 'w'), ensure_ascii=False, indent=1)
