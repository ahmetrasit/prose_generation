"""Score the SUPPLY's bridge rule (share >= 0.5 of the lemma's ayat, >= 2 co-occurring ayat, lemma <= 30 ayat,
partner root <= 400 ayat) and the supply's pointer levels on the validator's HFT harness (copied into
review/tools/validate; read-only on sources; cache = that copy). The validator's own bridge variants accept ANY
single witness ayah, which is a much looser rule than the one the supply ships."""
import sys, os, json, collections, random
import numpy as np
HERE = '/Volumes/OZTURK/_projects/prose_generation/_commentary/review/e0/review/tools/validate'
sys.path.insert(0, HERE); os.chdir(HERE)
sys.dont_write_bytecode = True
import lib, links, eval_hft as E

def supply_bridge(T, r, X, strict=False):
    rt = lib.BR[T]['root']
    if lib.ROOT_DF.get(r, 0) > 400:
        return None
    for L in links.NM_LEM.get(T, ()):
        n = lib.LEM_DF.get(L, 0)
        if n == 0 or n > 30:
            continue
        lr = lib.LEM_ROOT.get(L)
        if lr in (rt, r) or lr in links.EXCL_ROOTS:
            continue
        ayl = lib.LEM_AY[L]
        inter = ayl & lib.ROOT_AY.get(r, set())
        if not (inter - {X}):
            continue
        if strict:
            k = len(inter - {X}); n2 = len(ayl - {X})
            ok = k >= 2 and n2 and k / n2 >= 0.5
        else:
            ok = len(inter) >= 2 and len(inter) / n >= 0.5
        if ok:
            return L
    return None

import pickle
DEFDF = pickle.load(open('/Volumes/OZTURK/_projects/prose_generation/_commentary/review/e0/supply/cache/defining_df.pkl', 'rb'))
def supply_ptr(T, r, X):
    if r not in links.NM_ANY.get(T, ()):
        return None
    tok = links.NM_TOK[T].get(r)
    if DEFDF.get(tok, DEFDF.get(lib.norm(str(tok)), 0)) > 100 or lib.ROOT_DF.get(r, 0) > 400:
        return None
    return tok
VAR0 = {'supply_bridge': lambda T, r, X: supply_bridge(T, r, X),
       'supply_bridge_strict': lambda T, r, X: supply_bridge(T, r, X, strict=True),
       'ptr_card400': links.TYPES['ptr_card400'][2]}
VAR = {'supply_ptr_window_rule': supply_ptr}
cases = lib.hft_cases()
n = len(cases)
res = {}
for nm, f in VAR.items():
    Y = np.full(n, np.nan); EAF = Y.copy(); EB = Y.copy()
    for ci, c in enumerate(cases):
        X = (c['s'], c['a']); T = (c['rid'], c['bid']); acts = c['acts']
        others = E.other_word_roots(X, {c['root']} | set(acts))
        ob = [k for k in lib.RID_BR[c['rid']] if k != T]
        match = []
        if others:
            bins = collections.defaultdict(list)
            for r in others: bins[E.dfbin(r)].append(r)
            for r in acts:
                b = E.dfbin(r)
                for d in range(0, len(E.BINS) + 1):
                    cand = bins.get(b - d, []) + (bins.get(b + d, []) if d else [])
                    if cand: match.append(cand); break
        Y[ci] = sum(1 for r in acts if f(T, r, X)) / len(acts)
        if match:
            EAF[ci] = sum(sum(1 for r in cand if f(T, r, X)) / len(cand) for cand in match) / len(match)
        if ob:
            EB[ci] = sum(1 for t2 in ob for r in acts if f(t2, r, X)) / (len(ob) * len(acts))
    rng = np.random.default_rng(E.SEED)
    ay = np.array([c['s'] * 1000 + c['a'] for c in cases]); su = np.array([c['s'] for c in cases])
    out = {}
    for part, mask in (('full', np.ones(n, bool)), ('dev', su % 2 == 1), ('test', su % 2 == 0)):
        y, eaf, eb = Y[mask], EAF[mask], EB[mask]
        m = ~np.isnan(eaf)
        out[part] = dict(coverage=float(np.nanmean(y)), true_paths=float(y[m].sum()), expected=float(eaf[m].sum()),
                         lift_af=E.lift(y, eaf), ci=E.boot(y, eaf, ay[mask], rng),
                         lift_b=E.lift(y, eb), ci_b=E.boot(y, eb, ay[mask], rng))
    res[nm] = out
    print(nm, json.dumps(out))
json.dump(res, open('/Volumes/OZTURK/_projects/prose_generation/_commentary/review/e0/review/out/test_supply_ptr.json', 'w'), indent=1)
