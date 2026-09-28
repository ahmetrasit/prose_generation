"""Gold evaluations with the second-generation metrics and single-list typed unions (fair comparison):
 T3  S1 gold-ledger pairs (62): rank of the partner among the other-root S1 branches (144 cards), per metric;
     'union_rrf' = one ordered list (reciprocal-rank fusion of the per-type ranks, k=2);
     'union_min' = min rank over types (= reading every type's list), reported with its effective list size.
 T3b M8 set-conditioned coalition growth on S1 multi-anchor gold (G023 six-root water coalition, G026 herd,
     road spine G001-G003): seed with one anchor, add the S1 card with the highest mean proximity to the growing set
     (greedy, 12 steps), count gold members recovered, versus the 12 nearest to the seed alone.
 T4  29:38 cold-Opus links (19): NA branch choice + discovery rank per metric and union_rrf.
 T5  watch case: NA rank of the sabal eye film (س ب ل B010) in 29:38 (window 0 and +-3), with the guard, and the
     29:41 spider link at ayah level.
Read-only."""
import json, itertools, collections, sys, math
sys.dont_write_bytecode = True
import numpy as np
import common as C, metrics as M, guard as G, metrics2 as M2
from rr import exp_rr

W = {w['ref']: w for w in C.WORDS}
MET = ['slm_fused', 'slm_neo', 'clause_max', 'mention_shared', 'xref_idf', 'bridge_lemma', 'bridge_dir', 'scene_other', 'scene_same', 'dict_rel', 'dict_contrast']
UNION = ['slm_neo', 'clause_max', 'mention_shared', 'xref_idf', 'bridge_dir', 'scene_other', 'dict_rel', 'dict_contrast']
FL = M2.FLOORS
FN = M.METRICS
res = {}


def rrf_union(score_by_type, cands, floor=False):
    u = {c: 0.0 for c in cands}
    for t, sc in score_by_type.items():
        f = FL.get(t, 0.0) if floor else 0.0
        vals = sorted({v for v in sc.values() if v > f}, reverse=True)
        pos = {v: k for k, v in enumerate(vals)}
        for c, v in sc.items():
            if v > f: u[c] += 1.0 / (2 + pos[v])
    if floor and 'slm_neo' in score_by_type:
        for c in cands: u[c] += 1e-3 * score_by_type['slm_neo'][c]
    return u


def rank(sc, b):
    if sc[b] <= 0: return float(len(sc))
    return C.rank_of(sc, b)


# ------------------------------------------------------------------ T3 S1 pairs
s1roots = {r for w in C.WORDS if w['s'] == 1 for r in w['roots']}
S1C = sorted({i for r in s1roots for i in C.BY_ROOT.get(r, [])})
s1words = [w for w in C.WORDS if w['s'] == 1]
def s1_absent(i):
    if C.kind_of(i) != 'collocation': return False
    sts = {G.status(i, w)[0] for w in s1words if C.ROOTKEY[i] in w['roots']}
    return bool(sts) and sts <= {'absent'}
S1ABS = {i for i in S1C if s1_absent(i)}
gold = [json.loads(l) for l in open(f'{C.SLM}/reports/s1_ar3_v1_gold_ledger.jsonl')]
def pairs_of(r):
    req = r['required_branch_anchors']; groups = [g['node_ids'] for g in r['required_branch_anchor_groups']]
    ps = set()
    for a, b in itertools.combinations(req, 2): ps.add((a, b))
    for g in groups:
        for a in req:
            for b in g: ps.add((a, b))
    if not req and len(groups) >= 2:
        for a in groups[0]:
            for b in groups[1]: ps.add((a, b))
    return sorted(p for p in ps if p[0] in C.NODE and p[1] in C.NODE and C.ROOTKEY[C.NODE[p[0]]] != C.ROOTKEY[C.NODE[p[1]]])
GP = [(g['gold_id'], C.NODE[a], C.NODE[b]) for g in gold if g['eligibility']['eligible'] for a, b in pairs_of(g)]
t3 = collections.defaultdict(list); items = collections.defaultdict(set); umin_size = []
for gid, a, b in GP:
    best = {}
    for x, y in ((a, b), (b, a)):
        cands = [c for c in S1C if C.ROOTKEY[c] != C.ROOTKEY[x]]
        S = {t: {c: FN[t](x, c) for c in cands} for t in MET}
        S['union_rrf'] = rrf_union({t: S[t] for t in UNION}, cands)
        S['union_rrf+guard'] = {c: v - (1e6 if c in S1ABS else 0) for c, v in S['union_rrf'].items()}
        S['union_floor'] = rrf_union({t: S[t] for t in UNION}, cands, floor=True)
        for t, sc in S.items():
            r = rank(sc, y)
            if t not in best or r < best[t]: best[t] = r
        # union_min: min rank over types; effective list = union of each type's top-10
        rm = min(rank(S[t], y) for t in UNION)
        top = set()
        for t in UNION:
            top |= {c for c, v in sorted(S[t].items(), key=lambda kv: -kv[1])[:10] if v > 0}
        if 'union_min' not in best or rm < best['union_min']: best['union_min'] = rm
        umin_size.append(len(top))
    for t, r in best.items():
        t3[t].append(r)
        if r <= 10: items[t].add(gid)
def summ(v):
    v = np.array(v, dtype=float)
    return dict(median=float(np.median(v)), le3=int((v <= 3).sum()), le10=int((v <= 10).sum()), le20=int((v <= 20).sum()), n=len(v))
res['T3_S1_pairs'] = {t: summ(v) for t, v in t3.items()}
res['T3_S1_items_with_pair_le10'] = {t: len(v) for t, v in items.items()}
res['T3_S1_union_min_effective_list_size_for_top10'] = dict(median=float(np.median(umin_size)), mean=round(float(np.mean(umin_size)), 1))
# slm at the union_min list size, for a fair comparison
k = int(np.median(umin_size))
res['T3_S1_slm_fused_at_union_min_size'] = dict(k=k, pairs_le_k=int(sum(1 for r in t3['slm_fused'] if r <= k)))
res['T3_S1_candidate_pool'] = len(S1C)
print(json.dumps(res, ensure_ascii=False, indent=0))

# ------------------------------------------------------------------ T3b M8 coalition growth
def prox_fn(t):
    if t == 'union_rrf':
        return None
    return FN[t]
def grow(seed, members, t, steps=12, pool=S1C):
    pool = [c for c in pool if c != seed]
    if t == 'union_rrf':
        def score_to(x, cands):
            S = {tt: {c: FN[tt](x, c) for c in cands} for tt in UNION}
            return rrf_union(S, cands)
    else:
        def score_to(x, cands):
            return {c: FN[t](x, c) for c in cands}
    # pairwise from seed
    s0 = score_to(seed, pool)
    pair_top = [c for c, _ in sorted(s0.items(), key=lambda kv: -kv[1])[:steps]]
    # greedy set-conditioned (mean of normalized per-member scores)
    S = [seed]; acc = {c: [s0[c]] for c in pool}; chosen = []
    for _ in range(steps):
        cand = [c for c in pool if c not in chosen and C.ROOTKEY[c] not in {C.ROOTKEY[x] for x in S}]
        if not cand: break
        best = max(cand, key=lambda c: np.mean(acc[c]))
        chosen.append(best); S.append(best)
        sb = score_to(best, [c for c in pool if c not in chosen])
        for c, v in sb.items(): acc[c].append(v)
    gm = set(members) - {seed}
    return len(gm & set(pair_top)), len(gm & set(chosen)), len(gm)
coal = {'G023_water': [C.NODE[n] for n in gold[22]['required_branch_anchors']],
        'G026_herd': [C.NODE[gold[25]['required_branch_anchors'][0]]] + [C.NODE[n] for n in gold[25]['required_branch_anchor_groups'][0]['node_ids']],
        'road_spine_G001-3': [C.NODE[n] for n in ('quranic:root_001040:B002', 'quranic:root_001444:B006', 'quranic:root_000973:B005',
                                                   'quranic:root_001583:B001', 'quranic:root_000858:B001', 'quranic:root_001273:B008')]}
t3b = {}
for name, mem in coal.items():
    for t in ['slm_fused', 'bridge_dir', 'scene_other', 'union_rrf']:
        pw = gr = tot = 0
        for seed in mem:
            a_, b_, n_ = grow(seed, mem, t)
            pw += a_; gr += b_; tot += n_
        t3b[f'{name} {t}'] = dict(pairwise_from_seed=pw, set_conditioned=gr, of=tot)
        print(name, t, t3b[f'{name} {t}'])
res['T3b_M8_coalition_growth_12_steps'] = t3b

# ------------------------------------------------------------------ T4 29:38 links
GOLD = [("ع و د", "B009", "F:14"), ("ع م ل", "B011", "F:14"), ("ص د د", "B004", "F:14"), ("ص د د", "B013", "F:16"), ("س ب ل", "B010", "F:16"),
        ("ب ي ن", "B007", "F:16"), ("ع م ل", "B010", "F:16"), ("ز ي ن", "B001", "F:10"), ("ش ط ن", "B005", "F:8"), ("ش ط ن", "B003", "F:12"),
        ("س ب ل", "B010", "A:29:41"), ("س ك ن", "B004", "A:29:37"), ("ص د د", "B005", "A:7:74"), ("ص د د", "B002", "A:89:9"), ("س ب ل", "B005", "A:46:24"),
        ("ش ط ن", "B001", "A:11:68"), ("ز ي ن", "B001", "A:29:7"), ("ع م ل", "B012", "A:29:29"), ("س ب ل", "B010", "A:1:6")]
AY = [w for w in C.BY_AYAH[(29, 38)] if w['roots']]
wordof = {w['roots'][0]: w for w in AY}
def na(c, words, t, exclude_root, guard=False):
    best = (0.0, None, None)
    for y in words:
        ry = y['roots'][0]
        if ry == exclude_root: continue
        for yb in C.BY_ROOT.get(ry, []):
            if guard and G.status(yb, y)[0] == 'absent': continue
            v = FN[t](c, yb)
            if v > best[0]: best = (v, yb, y['ref'])
    return best
rows4 = []
for r, b, tgt in GOLD:
    X = wordof[r]; bi = [i for i in C.BY_ROOT[r] if C.BID[i] == b][0]
    if tgt.startswith('F:'):
        Y = [w for w in AY if w['w'] == int(tgt[2:])]
    else:
        s_, a_ = map(int, tgt[2:].split(':')); Y = [w for w in C.BY_AYAH[(s_, a_)] if w['roots']]
    row = dict(link=f'{r} {b} -> {tgt}', guard=G.status(bi, X)[0])
    S = {t: {c: na(c, Y, t, r)[0] for c in C.BY_ROOT[r]} for t in MET}
    S['union_rrf'] = rrf_union({t: S[t] for t in UNION}, C.BY_ROOT[r])
    S['union_floor'] = rrf_union({t: S[t] for t in UNION}, C.BY_ROOT[r], floor=True)
    for t, sc in S.items():
        row[t] = rank(sc, bi)
        row[t + '_rr'] = exp_rr(sc, bi)
    row['n_branches'] = len(C.BY_ROOT[r])
    row['union_path'] = ' | '.join(f"{t}: {M.EXPLAIN[t](bi, na(bi, Y, t, r)[1])}" for t in ('bridge_dir', 'xref_idf', 'scene_other', 'dict_rel')
                                   if na(bi, Y, t, r)[1] is not None and M.EXPLAIN.get(t))[:300]
    rows4.append(row)
    print(row['link'], row['guard'], {t: row[t] for t in ['slm_fused', 'bridge_dir', 'xref_idf', 'scene_other', 'union_rrf', 'union_floor']}, '/', row['n_branches'])
summ4 = {}
for t in MET + ['union_rrf', 'union_floor']:
    summ4[t] = dict(branch_choice_MRR=round(float(np.mean([row[t + '_rr'] for row in rows4])), 3),
                    top1=sum(1 for row in rows4 if row[t] <= 1), top3=sum(1 for row in rows4 if row[t] <= 3))
summ4['random_exact'] = dict(branch_choice_MRR=round(float(np.mean([sum(1 / k for k in range(1, row['n_branches'] + 1)) / row['n_branches'] for row in rows4])), 3))
res['T4_29_38_rows'] = rows4
res['T4_29_38_summary'] = summ4
print(json.dumps(summ4, ensure_ascii=False))

# ------------------------------------------------------------------ T5 watch: eye film
sab = [i for i in C.BY_ROOT['س ب ل'] if C.BID[i] == 'B010'][0]
def na_all(t, window, guard):
    tw = [w for (s, a) in C.window(29, 38, window) for w in C.BY_AYAH[(s, a)] if w['roots']]
    out = {}
    for x in AY:
        for c in C.BY_ROOT.get(x['roots'][0], []):
            out[c] = na(c, [y for y in tw if y['ref'] != x['ref']], t, x['roots'][0], guard)
    return out
t5 = {}
for wdw in (0, 3):
    for guard in (False, True):
        per = {t: na_all(t, wdw, guard) for t in MET}
        cands = list(per['slm_fused'])
        u = rrf_union({t: {c: per[t][c][0] for c in cands} for t in UNION}, cands)
        uf = rrf_union({t: {c: per[t][c][0] for c in cands} for t in UNION}, cands, floor=True)
        if guard:
            gd = {c: (1e6 if G.status(c, next(w for w in AY if C.ROOTKEY[c] in w['roots']))[0] == 'absent' else 0) for c in cands}
            u = {c: v - gd[c] for c, v in u.items()}; uf = {c: v - gd[c] for c, v in uf.items()}
        allsc = dict({t: {c: per[t][c][0] for c in cands} for t in MET}, union_rrf=u, union_floor=uf)
        for t, sc in allsc.items():
            sab_sc = {c: sc[c] for c in C.BY_ROOT['س ب ل']}
            nonprim = {c: v for c, v in sc.items() if C.BNUM[c] != 1}
            key = f'{t} win{wdw}{" guarded" if guard else ""}'
            p = per.get(t, {}).get(sab)
            t5[key] = dict(rank_in_sabil=rank(sab_sc, sab), of=len(sab_sc), rank_among_nonprimary_of_ayah=rank(nonprim, sab), of_all=len(nonprim),
                           path=(M.EXPLAIN[t](sab, p[1]) + f' [{p[2]}]') if p and p[1] is not None and M.EXPLAIN.get(t) else '')
for k_, v in t5.items():
    if k_.split()[0] in ('slm_fused', 'bridge_dir', 'xref_idf', 'scene_other', 'union_rrf', 'union_floor'): print(k_, v)
res['T5_eye_film'] = t5
# spider at ayah level
AYC = {k: [i for w in ws if w['roots'] for i in C.BY_ROOT.get(w['roots'][0], [])] for k, ws in C.BY_AYAH.items()}
sp = {}
for t in ['xref_idf', 'bridge_dir', 'slm_fused', 'mention_shared']:
    v = np.array([FN[t](sab, j) for j in range(C.N)])
    ays = {k: (max(v[j] for j in cs) if cs else 0.0) for k, cs in AYC.items() if k != (29, 38)}
    sur = {k: x for k, x in ays.items() if k[0] == 29}
    sp[t] = dict(global_rank=rank(ays, (29, 41)), in_surah=rank(sur, (29, 41)), top=[f'{k[0]}:{k[1]}' for k, _ in sorted(ays.items(), key=lambda kv: -kv[1])[:5]])
print('spider', sp)
res['T5_spider_29_41'] = sp
json.dump(res, open(C.HERE + '/gold2.json', 'w'), ensure_ascii=False, indent=1)
