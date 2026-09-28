"""T1 (partner branch given; Phase 1 protocol, same 12,000 cases as eval_v12.py) for the second-generation metrics
(xref_idf, bridge_lemma) and the RRF typed unions, plus the exact random baseline (expected MRR of a random order,
H_n/n; Phase 1's 'random 0.145' was mean 1/n, which understates it)."""
import csv, glob, collections, itertools, random, json, math, sys
sys.dont_write_bytecode = True
import numpy as np
import common as C, metrics as M, guard as G, metrics2
from rr import exp_rr
W = {w['ref']: w for w in C.WORDS}
V = f'{C.P}/latent_activation/_status/v12_cross_run'
F = collections.defaultdict(dict); GR = {}; SUR = {}
for f in glob.glob(f'{V}/s[0-9][0-9][0-9]/derived/finding_word_branches.v3.tsv'):
    for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
        k = (f, r['finding_id']); GR[k] = r['grade']; SUR[k] = int(r['ayah_ref'].split(':')[0])
        i = C.GI.get((r['root_id'], r['branch_id']))
        if i is not None: F[k][i] = r['qac_word_ref']
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
TYPES = ['slm_fused', 'slm_neo', 'clause_max', 'mention_shared', 'xref', 'xref_idf', 'bridge', 'bridge_lemma', 'bridge_dir', 'scene_other', 'dict_rel', 'dict_contrast']
U1 = ['slm_neo', 'clause_max', 'mention_shared', 'xref', 'bridge', 'scene_other', 'dict_rel']
U2 = ['slm_neo', 'clause_max', 'mention_shared', 'xref_idf', 'bridge_dir', 'scene_other', 'dict_rel', 'dict_contrast']
FL = metrics2.FLOORS
def hm(n): return sum(1.0 / k for k in range(1, n + 1)) / n
res = collections.defaultdict(lambda: collections.defaultdict(list))
for a, b, wref, s in tests:
    cands = C.BY_RID[C.RID[b]]
    w = W.get(wref)
    dem = {c: (-1e6 if (w and G.status(c, w)[0] == 'absent') else 0.0) for c in cands}
    S = {t: {c: M.METRICS[t](a, c) for c in cands} for t in TYPES}
    S['prior_B001'] = {c: (1.0 if C.BNUM[c] == 1 else 0.0) for c in cands}
    for name, types in (('typed_union_v1', U1), ('typed_union_v2', U2)):
        u = collections.defaultdict(float)
        for t in types:
            vals = sorted({v for v in S[t].values() if v > 0}, reverse=True)
            for c, v in S[t].items():
                if v > 0: u[c] += 1.0 / (2 + vals.index(v))
        S[name] = {c: u.get(c, 0.0) for c in cands}
        S[name + '+guard'] = {c: u.get(c, 0.0) + dem[c] for c in cands}
    u = collections.defaultdict(float)
    for t in U2:
        vals = sorted({v for v in S[t].values() if v > FL[t]}, reverse=True)
        for c, v in S[t].items():
            if v > FL[t]: u[c] += 1.0 / (2 + vals.index(v))
    S['typed_union_floor'] = {c: u.get(c, 0.0) + 1e-3 * S['slm_neo'][c] for c in cands}
    S['typed_union_floor+guard'] = {c: S['typed_union_floor'][c] + dem[c] for c in cands}
    for name, sc in S.items():
        r = exp_rr(sc, b)
        res[name]['all'].append(r)
        if C.BNUM[b] != 1: res[name]['nonB001'].append(r)
        if C.BNUM[b] != 1 and C.BNUM[a] != 1: res[name]['latent_latent'].append(r)
    res['random_exact']['all'].append(hm(len(cands)))
    if C.BNUM[b] != 1: res['random_exact']['nonB001'].append(hm(len(cands)))
    if C.BNUM[b] != 1 and C.BNUM[a] != 1: res['random_exact']['latent_latent'].append(hm(len(cands)))
out = {n: {k: round(float(np.mean(v)), 3) for k, v in d.items()} for n, d in res.items()}
for n, v in out.items(): print(f'{n:22s}', v)
json.dump(out, open(C.HERE + '/eval_t1_new.json', 'w'), ensure_ascii=False, indent=1)
