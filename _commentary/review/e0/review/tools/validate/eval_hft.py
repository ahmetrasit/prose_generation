"""Path existence of each candidate link type on the independent HFT surprise set (3,398 raw cases; 3,325 unique
(ayah, root id, branch) targets with the union of their activator roots; named surahs excluded by construction).

For each target branch T in ayah X with HFT activator roots A:
  y   = share of A reached by a path of the type from T                       (true activator)
  e_a = share of the ayah's other words (not T's root, not an activator) reached from T   (base a)
  e_b = share of (other branch of T's root id, activator) pairs with a path   (base b; also non-B001 only)
lift_a = sum(y) / sum(e_a) over targets where base a is defined (paired); lift_b likewise.
CIs: percentile bootstrap, 2,000 resamples of ayat (clusters); also resampling surahs. Dev/test: odd / even surahs.
Volume and noise: on 300 seeded ayat of the set, every (branch of word i, other word j) pair is tested.
Writes cache/hft_matrix.pkl, results_hft.json, results_hft.tsv."""
import sys, os, json, random, collections, pickle, time, math
import numpy as np
sys.dont_write_bytecode = True
import lib, links

B = 2000
SEED = 20260928


BINS = (30, 100, 300, 1000)


def dfbin(r):
    d = lib.ROOT_DF.get(r, 0)
    for i, b in enumerate(BINS):
        if d <= b:
            return i
    return len(BINS)


ALLROOTS = sorted(r for r in lib.ROOT_DF if r in lib.ROOT_BR)
DF_SORTED = sorted(ALLROOTS, key=lambda r: lib.ROOT_DF[r])


def matched_pool(r, exclude, rng, k=20):
    """k random roots (with dictionary branches) whose ayah frequency is within +-25% of r's (widened if scarce)"""
    d = lib.ROOT_DF.get(r, 1)
    for w in (0.25, 0.5, 1.0):
        pool = [x for x in DF_SORTED if abs(lib.ROOT_DF[x] - d) <= max(2, w * d) and x not in exclude]
        if len(pool) >= k:
            break
    return rng.sample(pool, min(k, len(pool)))


def other_word_roots(X, exclude):
    out = []
    for w in lib.BY_AYAH[X]:
        if w['roots'] and w['roots'][0] not in exclude:
            out.append(w['roots'][0])
    return out


def build_matrix(cases):
    names = list(links.TYPES)
    n = len(cases)
    Y = np.full((len(names), n), np.nan); EA = Y.copy(); EB = Y.copy(); EB2 = Y.copy(); EAF = Y.copy(); EG = Y.copy()
    t0 = time.time()
    grng = random.Random(SEED)
    for ci, c in enumerate(cases):
        X = (c['s'], c['a']); T = (c['rid'], c['bid']); acts = c['acts']
        others = other_word_roots(X, {c['root']} | set(acts))
        ob = [k for k in lib.RID_BR[c['rid']] if k != T]
        ob2 = [k for k in ob if k[1] != 'B001']
        # frequency-matched partners inside the ayah (same frequency bin, else the nearest non-empty bin)
        match = []
        if others:
            ob_bins = collections.defaultdict(list)
            for r in others:
                ob_bins[dfbin(r)].append(r)
            for r in acts:
                b = dfbin(r)
                for dlt in range(0, len(BINS) + 1):
                    cand = ob_bins.get(b - dlt, []) + (ob_bins.get(b + dlt, []) if dlt else [])
                    if cand:
                        match.append(cand); break
        excl = {c['root']} | set(acts) | set(lib.AY_ROOTS[X])
        gpool = [matched_pool(r, excl, grng) for r in acts]
        for ti, nm in enumerate(names):
            fam, scope, f = links.TYPES[nm]
            y = sum(1 for r in acts if f(T, r, X)) / len(acts)
            Y[ti, ci] = y
            if scope in ('branch-only', 'root-only'):
                EAF[ti, ci] = y; EG[ti, ci] = y
            else:
                if match:
                    EAF[ti, ci] = sum(sum(1 for r in cand if f(T, r, X)) / len(cand) for cand in match) / len(match)
                gp = [p for p in gpool if p]
                if gp:
                    EG[ti, ci] = sum(sum(1 for r in p if f(T, r, X)) / len(p) for p in gp) / len(gp)
            if others:
                EA[ti, ci] = y if scope in ('branch-only', 'root-only') else sum(1 for r in others if f(T, r, X)) / len(others)
            if ob:
                if scope in ('root->root', 'root-only'):
                    EB[ti, ci] = y
                    EB2[ti, ci] = y if ob2 else np.nan
                else:
                    EB[ti, ci] = sum(1 for t2 in ob for r in acts if f(t2, r, X)) / (len(ob) * len(acts))
                    if ob2:
                        EB2[ti, ci] = sum(1 for t2 in ob2 for r in acts if f(t2, r, X)) / (len(ob2) * len(acts))
        if ci % 500 == 0:
            print(f'  {ci}/{n} {time.time() - t0:.0f}s', flush=True)
    return names, Y, EA, EB, EB2, EAF, EG


def lift(y, e):
    m = ~np.isnan(e)
    se = e[m].sum()
    return (y[m].sum() / se) if se > 0 else float('nan')


def boot(y, e, clusters, rng):
    """percentile CI of lift under cluster resampling; a resample with no expected path but a true path counts as
    an infinite lift (so tiny bases give an open upper bound instead of no interval)"""
    m = ~np.isnan(e)
    y, e, cl = y[m], e[m], clusters[m]
    uniq, inv = np.unique(cl, return_inverse=True)
    ys = np.bincount(inv, weights=y, minlength=len(uniq)); es = np.bincount(inv, weights=e, minlength=len(uniq))
    k = len(uniq)
    idx = rng.integers(0, k, size=(B, k))
    num = ys[idx].sum(1); den = es[idx].sum(1)
    with np.errstate(divide='ignore', invalid='ignore'):
        L = np.where(den > 0, num / den, np.where(num > 0, np.inf, np.nan))
    L = L[~np.isnan(L)]
    if len(L) < B * 0.5:
        return (float('nan'), float('nan'))
    return (float(np.percentile(L, 2.5, method='lower')), float(np.percentile(L, 97.5, method='higher')))


def boot_diff(y, e, clusters, rng):
    m = ~np.isnan(e)
    y, e, cl = y[m], e[m], clusters[m]
    uniq, inv = np.unique(cl, return_inverse=True)
    d = np.bincount(inv, weights=y - e, minlength=len(uniq)); cnt = np.bincount(inv, minlength=len(uniq))
    idx = rng.integers(0, len(uniq), size=(B, len(uniq)))
    D = d[idx].sum(1) / cnt[idx].sum(1)
    return (float(np.percentile(D, 2.5)), float(np.percentile(D, 97.5)))


def summarize(names, Y, EA, EB, EB2, EAF, EG, cases, mask=None):
    rng = np.random.default_rng(SEED)
    ay = np.array([c['s'] * 1000 + c['a'] for c in cases])
    su = np.array([c['s'] for c in cases])
    if mask is None:
        mask = np.ones(len(cases), bool)
    out = {}
    for ti, nm in enumerate(names):
        fam, scope, _ = links.TYPES[nm]
        y, ea, eb, eb2 = Y[ti, mask], EA[ti, mask], EB[ti, mask], EB2[ti, mask]
        eaf, eg = EAF[ti, mask], EG[ti, mask]
        r = dict(family=fam, scope=scope, n=int(mask.sum()),
                 coverage=float(np.nanmean(y)),                       # P(path to a true activator)
                 any_true=float(np.mean(y > 0)),
                 base_a=float(np.nanmean(ea)), base_b=float(np.nanmean(eb)), base_b_nonB001=float(np.nanmean(eb2)))
        r['lift_a'] = lift(y, ea)
        r['base_af'] = float(np.nanmean(eaf)); r['base_g'] = float(np.nanmean(eg))
        r['lift_af'] = lift(y, eaf); r['lift_g'] = lift(y, eg)
        m = ~np.isnan(eaf)
        r['true_paths'] = float(y[m].sum()); r['expected_af'] = float(eaf[m].sum())
        word_level = scope not in ('branch-only', 'root-only')
        r['lift_af_ci_ayah'] = boot(y, eaf, ay[mask], rng) if word_level else None
        r['lift_af_ci_surah'] = boot(y, eaf, su[mask], rng) if word_level else None
        r['diff_af_ci_ayah'] = boot_diff(y, eaf, ay[mask], rng) if word_level else None
        r['lift_g_ci_ayah'] = boot(y, eg, ay[mask], rng) if word_level else None
        r['lift_b'] = lift(y, eb) if scope not in ('root->root', 'root-only') else None
        r['lift_b_nonB001'] = lift(y, eb2) if scope not in ('root->root', 'root-only') else None
        r['lift_a_ci_ayah'] = boot(y, ea, ay[mask], rng) if scope not in ('branch-only', 'root-only') else None
        r['lift_a_ci_surah'] = boot(y, ea, su[mask], rng) if scope not in ('branch-only', 'root-only') else None
        r['diff_a_ci_ayah'] = boot_diff(y, ea, ay[mask], rng) if scope not in ('branch-only', 'root-only') else None
        if scope not in ('root->root', 'root-only'):
            r['lift_b_ci_ayah'] = boot(y, eb, ay[mask], rng)
            r['lift_b_ci_surah'] = boot(y, eb, su[mask], rng)
            r['lift_b_nonB001_ci_ayah'] = boot(y, eb2, ay[mask], rng)
        out[nm] = r
    return out


# ------------------------------------------------------------------ volume and noise
SYMMETRIC = {'cooc_ayah_pmi0', 'cooc_ayah_pmi1', 'cooc_ayah_pmi2', 'formula_k3', 'formula_k5', 'formula_k10',
             'formula_k5_pmi'}


def volume(names, ayat, freq=300):
    """distinct display units per ayah: branch->root types count distinct (branch, partner root); root->root types
    count distinct (root, partner root) pairs (unordered for symmetric types); branch-only / root-only types count
    distinct branches / roots with the property."""
    res = {nm: dict(frequent_partner=0, frequent_element=0, generic_token=0, units=0, per_ayah=[]) for nm in names}
    for X in ayat:
        words = [w for w in lib.BY_AYAH[X] if w['roots']]
        roots = []
        for w in words:
            if w['roots'][0] not in roots:
                roots.append(w['roots'][0])
        units = {nm: set() for nm in names}
        for ri in roots:
            for T in lib.ROOT_BR.get(ri, ()):
                for rj in roots:
                    if rj == ri:
                        continue
                    for nm in names:
                        fam, scope, f = links.TYPES[nm]
                        el = f(T, rj, X)
                        if not el:
                            continue
                        if scope == 'branch->root':
                            u = (T, rj)
                        elif scope == 'root->root':
                            u = tuple(sorted((ri, rj))) if nm in SYMMETRIC else (ri, rj)
                        elif scope == 'branch-only':
                            u = T
                        else:
                            u = ri
                        if u in units[nm]:
                            continue
                        units[nm].add(u)
                        R = res[nm]
                        if lib.ROOT_DF.get(rj, 0) > freq:
                            R['frequent_partner'] += 1
                        if fam == 'pointer':
                            named = ri if scope == 'root->root' else rj
                            fe = (lib.LEM_DF.get(el, 0) > freq) if nm == 'ptr_lemma' else (lib.ROOT_DF.get(named, 0) > freq)
                            t = lib.norm(str(el))
                            if t in lib.GENERIC_TOK or t[2:] in lib.GENERIC_TOK:
                                R['generic_token'] += 1
                        elif fam == 'bridge':
                            fe = lib.LEM_DF.get(el, 0) > freq
                        elif fam in ('cooccurrence', 'formula'):
                            fe = lib.ROOT_DF.get(rj, 0) > freq
                        elif fam == 'qnet':
                            fe = links.QDF.get(el, 0) > 500
                        else:
                            fe = False
                        R['frequent_element'] += fe
        for nm in names:
            res[nm]['per_ayah'].append(len(units[nm]))
            res[nm]['units'] += len(units[nm])
    out = {}
    for nm, R in res.items():
        pa = np.array(R['per_ayah'])
        n = max(1, R['units'])
        out[nm] = dict(paths_per_ayah_mean=float(pa.mean()), paths_per_ayah_median=float(np.median(pa)),
                       paths_per_ayah_p90=float(np.percentile(pa, 90)), paths_per_ayah_max=float(pa.max()),
                       share_frequent_partner=R['frequent_partner'] / n,
                       share_frequent_element=R['frequent_element'] / n,
                       share_generic_token=R['generic_token'] / n)
    return out


def main():
    cases = lib.hft_cases()
    mp = os.path.join(lib.CACHE, 'hft_matrix.pkl')
    if os.path.exists(mp):
        names, Y, EA, EB, EB2, EAF, EG = pickle.load(open(mp, 'rb'))
        if names != list(links.TYPES):
            os.remove(mp)
    if not os.path.exists(mp):
        print('building matrix over', len(cases), 'targets')
        names, Y, EA, EB, EB2, EAF, EG = build_matrix(cases)
        pickle.dump((names, Y, EA, EB, EB2, EAF, EG), open(mp, 'wb'))
    su = np.array([c['s'] for c in cases])
    full = summarize(names, Y, EA, EB, EB2, EAF, EG, cases)
    dev = summarize(names, Y, EA, EB, EB2, EAF, EG, cases, su % 2 == 1)
    test = summarize(names, Y, EA, EB, EB2, EAF, EG, cases, su % 2 == 0)
    rnd = random.Random(SEED)
    ayat = sorted({(c['s'], c['a']) for c in cases})
    samp = rnd.sample(ayat, 300)
    vp = os.path.join(lib.CACHE, 'volume.pkl')
    if os.path.exists(vp) and set(pickle.load(open(vp, 'rb'))) == set(names):
        vol = pickle.load(open(vp, 'rb'))
    else:
        print('volume on 300 ayat')
        vol = volume(names, samp)
        pickle.dump(vol, open(vp, 'wb'))
    meta = dict(targets=len(cases), raw_cases=sum(c['n_raw'] for c in cases), ayat=len(ayat),
                surahs=len({c['s'] for c in cases}), activator_pairs=sum(len(c['acts']) for c in cases),
                dev_targets=int((su % 2 == 1).sum()), test_targets=int((su % 2 == 0).sum()),
                bootstrap=B, seed=SEED, volume_ayat=len(samp))
    json.dump(dict(meta=meta, full=full, dev=dev, test=test, volume=vol), open(os.path.join(lib.HERE, 'results_hft.json'), 'w'),
              ensure_ascii=False, indent=1)
    # flat table
    def f(x, d=3):
        return '' if x is None or (isinstance(x, float) and math.isnan(x)) else (f'{x:.{d}f}' if isinstance(x, float) else str(x))
    def ci(t):
        return '' if not t else f'[{t[0]:.2f},{t[1]:.2f}]'
    cols = ['type', 'family', 'scope', 'coverage', 'base_a', 'lift_a', 'base_af', 'lift_af', 'lift_af_ci_ayah',
            'lift_af_ci_surah', 'diff_af_ci_ayah', 'lift_g', 'lift_g_ci_ayah', 'base_b', 'lift_b', 'lift_b_ci_ayah',
            'lift_b_ci_surah', 'lift_b_nonB001', 'dev_lift_af', 'dev_af_ci', 'test_lift_af', 'test_af_ci', 'dev_lift_b',
            'dev_b_ci', 'test_lift_b', 'test_b_ci', 'paths_per_ayah', 'paths_per_ayah_p90', 'share_frequent_element',
            'share_frequent_partner']
    rows = ['\t'.join(cols)]
    def cid(t):
        return '' if not t else f'[{t[0]:+.3f},{t[1]:+.3f}]'
    for nm in names:
        r, d, t, v = full[nm], dev[nm], test[nm], vol[nm]
        rows.append('\t'.join([nm, r['family'], r['scope'], f(r['coverage']), f(r['base_a']), f(r['lift_a'], 2),
                               f(r['base_af']), f(r['lift_af'], 2), ci(r['lift_af_ci_ayah']), ci(r['lift_af_ci_surah']),
                               cid(r['diff_af_ci_ayah']), f(r['lift_g'], 2), ci(r['lift_g_ci_ayah']),
                               f(r['base_b']), f(r['lift_b'], 2), ci(r.get('lift_b_ci_ayah')), ci(r.get('lift_b_ci_surah')),
                               f(r['lift_b_nonB001'], 2), f(d['lift_af'], 2), ci(d['lift_af_ci_ayah']), f(t['lift_af'], 2),
                               ci(t['lift_af_ci_ayah']), f(d['lift_b'], 2), ci(d.get('lift_b_ci_ayah')), f(t['lift_b'], 2),
                               ci(t.get('lift_b_ci_ayah')), f(v['paths_per_ayah_mean'], 1), f(v['paths_per_ayah_p90'], 0),
                               f(v['share_frequent_element'], 2), f(v['share_frequent_partner'], 2)]))
    open(os.path.join(lib.HERE, 'results_hft.tsv'), 'w').write('\n'.join(rows) + '\n')
    print(json.dumps(meta))
    print('\n'.join(rows))


if __name__ == '__main__':
    main()
