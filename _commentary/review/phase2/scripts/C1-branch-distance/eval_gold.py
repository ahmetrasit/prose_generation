"""T3: S1 gold-ledger anchor pairs (62) -- rank of the partner among cross-root S1 branches, per metric and typed union.
T4: 29:38 cold-Opus links (19) -- neighbour-activation (NA) branch choice and discovery rank; ayah targets ranked
    among all ayat and within the surah.
T5: watch case 29:38 -- NA ranks of the sabal eye-film branch; the 29:41 spider link.
Construction guard applied as a flag and reported."""
import json, itertools, collections, sys, math
sys.dont_write_bytecode = True
import numpy as np
import common as C, metrics as M, guard as G
W = {w['ref']: w for w in C.WORDS}
LM = json.load(open(C.HERE + '/learned_no_prior.json')) if __import__('os').path.exists(C.HERE + '/learned_no_prior.json') else None
def learned(a, b):
    fv = {m: M.METRICS[m](a, b) for m in LM['feats']}
    x = (np.array([fv[f] for f in LM['feats']]) - np.array(LM['mu'])) / np.array(LM['sd'])
    return float(x @ np.array(LM['w']))
MET = ['slm_fused', 'slm_neo', 'clause_max', 'mention_shared', 'xref', 'dict_rel', 'dict_contrast', 'scene_other', 'scene_same', 'bridge', 'sound']
FN = dict(M.METRICS)
if LM: FN['learned_no_prior'] = learned; MET.append('learned_no_prior')
UNION = ['slm_neo', 'clause_max', 'mention_shared', 'xref', 'dict_rel', 'scene_other', 'bridge']

def ranks_for(a, cands, fn):
    sc = {c: fn(a, c) for c in cands}
    return sc
def rank_in(sc, b):
    if sc[b] <= 0 and all(v <= 0 for v in sc.values()): return len(sc)
    return C.rank_of(sc, b)
def union_rank(per_type, b):
    """typed union: position of b when the per-type lists are interleaved (min rank across types, ties by type count);
    a type where b scores 0 does not count"""
    best = min((r for t, (r, v) in per_type.items() if v > 0), default=None)
    return best

res = {}
# ---------------- T3 S1
s1roots = {r for w in C.WORDS if w['s'] == 1 for r in w['roots']}
S1C = [i for r in s1roots for i in C.BY_ROOT.get(r, [])]
print('S1 candidate branches', len(S1C), 'roots', len(s1roots))
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
gold = [json.loads(l) for l in open(f'{C.SLM}/reports/s1_ar3_v1_gold_ledger.jsonl')]
GP = [(g['gold_id'], C.NODE[a], C.NODE[b]) for g in gold if g['eligibility']['eligible'] for a, b in pairs_of(g)]
print('S1 eligible cross-root pairs', len(GP))
t3 = collections.defaultdict(list); t3u = []; t3rrf = []; items_hit = collections.defaultdict(set)
for gid, a, b in GP:
    per = {}
    for m in MET:
        best = None
        for x, y in ((a, b), (b, a)):
            cands = [c for c in S1C if C.ROOTKEY[c] != C.ROOTKEY[x]]
            sc = ranks_for(x, cands, FN[m]); r = rank_in(sc, y)
            if best is None or r < best[0]: best = (r, sc[y])
        t3[m].append(best[0]); per[m] = best
        if best[0] <= 10 and best[1] > 0: items_hit[m].add(gid)
    u = union_rank({t: per[t] for t in UNION}, b)
    t3u.append(u if u is not None else 999)
    if u is not None and u <= 10: items_hit['typed_union'].add(gid)
def summ(v):
    v = np.array(v, dtype=float)
    return dict(median=float(np.median(v)), le3=int((v <= 3).sum()), le10=int((v <= 10).sum()), n=len(v))
res['T3_S1_gold_pairs'] = {m: summ(v) for m, v in t3.items()}
res['T3_S1_gold_pairs']['typed_union(min over ' + '+'.join(UNION) + ')'] = summ(t3u)
res['T3_S1_items_with_a_pair_le10'] = {m: len(v) for m, v in items_hit.items()}
res['T3_S1_items_total'] = len({g for g, a, b in GP})
# guard on S1 gold anchors
blocked = set()
for gid, a, b in GP:
    for x in (a, b):
        if C.kind_of(x) == 'collocation':
            sts = {G.status(x, w)[0] for w in C.WORDS if w['s'] == 1 and C.ROOTKEY[x] in w['roots']}
            if sts <= {'absent'}: blocked.add((gid, C.DISP[x]))
res['T3_S1_pairs_touching_a_blocked_collocation_branch'] = sorted(blocked)

# ---------------- T4 29:38
GOLD = [("ع و د", "B009", "F:1>F:14"), ("ع م ل", "B011", "F:14"), ("ص د د", "B004", "F:14"), ("ص د د", "B013", "F:16"), ("س ب ل", "B010", "F:16"),
        ("ب ي ن", "B007", "F:16"), ("ع م ل", "B010", "F:16"), ("ز ي ن", "B001", "F:10"), ("ش ط ن", "B005", "F:8"), ("ش ط ن", "B003", "F:12"),
        ("س ب ل", "B010", "A:29:41"), ("س ك ن", "B004", "A:29:37"), ("ص د د", "B005", "A:7:74"), ("ص د د", "B002", "A:89:9"), ("س ب ل", "B005", "A:46:24"),
        ("ش ط ن", "B001", "A:11:68"), ("ز ي ن", "B001", "A:29:7"), ("ع م ل", "B012", "A:29:29"), ("س ب ل", "B010", "A:1:6")]
AY = [w for w in C.BY_AYAH[(29, 38)] if w['roots']]
wordof = {w['roots'][0]: w for w in AY}
def cards_of(ws, exclude_root=None):
    return [i for w in ws for r in w['roots'] if r != exclude_root for i in C.BY_ROOT.get(r, [])]
def na(c, target_words, fn, exclude_root):
    ys = cards_of(target_words, exclude_root)
    if not ys: return 0.0, None
    vals = [(fn(c, y), y) for y in ys]
    return max(vals)
# vector of a metric from branch c to all cards (for ayah ranking)
def vec(c, m):
    if m == 'slm_fused':
        return np.array([C.s_fused(c, j) for j in range(C.N)])
    if m == 'slm_neo':
        return np.array([C.s_neo(c, j) for j in range(C.N)])
    if m == 'clause_max':
        A = M.MOTC[c]; out = np.zeros(C.N)
        for j in range(C.N):
            if C.ROOTKEY[j] != C.ROOTKEY[c]: out[j] = float((A @ M.MOTC[j].T).max())
        return out
    return np.array([FN[m](c, j) for j in range(C.N)])
AYCARDS = {k: cards_of([w for w in ws if w['roots']]) for k, ws in C.BY_AYAH.items()}
t4 = collections.defaultdict(list); t4rows = []
vcache = {}
for r, b, tgt in GOLD:
    X = wordof[r]; bi = [i for i in C.BY_ROOT[r] if C.BID[i] == b][0]
    targets = tgt.split('>')[-1]
    row = dict(link=f"{r} {b} -> {tgt}", guard=G.status(bi, X)[0])
    for m in MET + ['typed_union']:
        if m == 'typed_union': continue
        fn = FN[m]
        if targets.startswith('F:'):
            Y = [w for w in AY if w['w'] == int(targets[2:])]
            # branch choice: rank b among the branches of X's root by NA to Y
            sc = {c: na(c, Y, fn, r)[0] for c in C.BY_ROOT[r]}
            bc = C.rank_of(sc, bi) if sc[bi] > 0 else len(sc)
            # discovery: rank (b, Y) among all (branch of any 29:38 word, other word) links
            allp = {}
            for x in AY:
                for c in C.BY_ROOT.get(x['roots'][0], []):
                    for y in AY:
                        if y['roots'][0] == x['roots'][0]: continue
                        allp[(c, y['ref'])] = na(c, [y], fn, x['roots'][0])[0]
            dr = C.rank_of(allp, (bi, Y[0]['ref'])) if allp[(bi, Y[0]['ref'])] > 0 else len(allp)
            row[m] = dict(branch_choice=bc, of=len(sc), discovery=dr, of_links=len(allp))
        else:
            s_, a_ = map(int, targets[2:].split(':'))
            key = (bi, m)
            if key not in vcache: vcache[key] = vec(bi, m)
            v = vcache[key]
            ays = {k: (max(v[j] for j in cs) if cs else 0.0) for k, cs in AYCARDS.items() if k != (29, 38)}
            rg = C.rank_of(ays, (s_, a_)) if ays[(s_, a_)] > 0 else len(ays)
            sur = {k: x for k, x in ays.items() if k[0] == s_}
            rs = C.rank_of(sur, (s_, a_)) if sur[(s_, a_)] > 0 else len(sur)
            sc = {c: na(c, [w for w in C.BY_AYAH[(s_, a_)] if w['roots']], fn, None)[0] for c in C.BY_ROOT[r]}
            bc = C.rank_of(sc, bi) if sc[bi] > 0 else len(sc)
            row[m] = dict(branch_choice=bc, of=len(sc), ayah_rank_global=rg, ayah_rank_in_surah=rs, surah_ayat=len(sur))
    t4rows.append(row)
    print(row['link'], row['guard'], {m: row[m] for m in ('slm_fused', 'clause_max', 'mention_shared', 'xref', 'bridge', 'scene_other', 'dict_rel', 'sound')})
res['T4_29_38_links'] = t4rows
# summaries: branch-choice MRR and #links with discovery/ayah rank <= 10 per metric; typed union = best over UNION types
summ4 = {}
for m in MET + ['typed_union']:
    mr, top = [], 0
    for row in t4rows:
        if m == 'typed_union':
            bc = min(row[t]['branch_choice'] for t in UNION)
            d = min(row[t].get('discovery', row[t].get('ayah_rank_in_surah', 999)) for t in UNION)
        else:
            bc = row[m]['branch_choice']; d = row[m].get('discovery', row[m].get('ayah_rank_in_surah'))
        mr.append(1 / bc); top += d <= 10
    summ4[m] = dict(branch_choice_MRR=round(float(np.mean(mr)), 3), links_found_le10=top, n=len(t4rows))
rnd = float(np.mean([1 / len(C.BY_ROOT[r]) for r, b, t in GOLD]))
summ4['random'] = dict(branch_choice_MRR=round(rnd, 3))
res['T4_summary'] = summ4
print(json.dumps(summ4, ensure_ascii=False))

# ---------------- T5 watch: NA of every branch of every 29:38 word; sabal's eye film
def na_all(fn, window=0):
    tw = [w for (s, a) in C.window(29, 38, window) for w in C.BY_AYAH[(s, a)] if w['roots']]
    out = {}
    for x in AY:
        for c in C.BY_ROOT.get(x['roots'][0], []):
            others = [y for y in tw if y['roots'][0] != x['roots'][0]]
            best = (0.0, None, None)
            for y in others:
                v, yb = na(c, [y], fn, x['roots'][0])
                if v > best[0]: best = (v, y['ref'], yb)
            out[c] = best
    return out
sab = [i for i in C.BY_ROOT['س ب ل'] if C.BID[i] == 'B010'][0]
t5 = {}
for m in ['slm_fused', 'slm_neo', 'clause_max', 'mention_shared', 'xref', 'bridge', 'scene_other', 'scene_same', 'dict_rel'] + (['learned_no_prior'] if LM else []):
    for wdw in (0, 3):
        o = na_all(FN[m], wdw)
        sab_sc = {c: o[c][0] for c in C.BY_ROOT['س ب ل']}
        nonprim = {c: v[0] for c, v in o.items() if C.BNUM[c] != 1}
        t5[f'{m} win{wdw}'] = dict(rank_in_sabil_branches=C.rank_of(sab_sc, sab) if sab_sc[sab] > 0 else len(sab_sc), of=len(sab_sc),
                                   rank_among_all_nonprimary_branches_of_the_ayah=C.rank_of(nonprim, sab) if nonprim[sab] > 0 else len(nonprim), of_all=len(nonprim),
                                   activated_by=(o[sab][1], C.DISP[o[sab][2]] if o[sab][2] is not None else None),
                                   path=M.EXPLAIN.get(m, lambda a, b: '')(sab, o[sab][2]) if o[sab][2] is not None else '')
res['T5_watch_sabal'] = t5
for k, v in t5.items(): print(k, v)
# 29:41 spider: rank of 29:41 among all ayat and within S29 for the eye-film branch under xref / mention / clause
sp = {}
for m in ['xref', 'mention_shared', 'bridge', 'clause_max', 'slm_fused']:
    key = (sab, m)
    if key not in vcache: vcache[key] = vec(sab, m)
    v = vcache[key]
    ays = {k: (max(v[j] for j in cs) if cs else 0.0) for k, cs in AYCARDS.items() if k != (29, 38)}
    sur = {k: x for k, x in ays.items() if k[0] == 29}
    sp[m] = dict(global_rank=C.rank_of(ays, (29, 41)) if ays[(29, 41)] > 0 else 'score 0', in_surah=C.rank_of(sur, (29, 41)) if sur[(29, 41)] > 0 else 'score 0')
    top = sorted(ays.items(), key=lambda x: -x[1])[:6]
    sp[m]['top_ayat'] = [f"{k[0]}:{k[1]}" for k, x in top]
res['T5_spider_29_41'] = sp
print('spider', sp)
json.dump(res, open(C.HERE + '/eval_gold.json', 'w'), ensure_ascii=False, indent=1)
