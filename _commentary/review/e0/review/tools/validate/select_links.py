"""Freeze the link-type recommendation from results_hft.json by a mechanical rule, then measure the chosen set.

Rule (fixed in this file; volume is reported, never used to gate -- no caps):
  1. Per family, among its candidate variants, pick the one with the highest DEV-half (odd surahs) lower 95% bound
     of lift_af (frequency-matched other word of the same ayah, ayah-cluster bootstrap). A variant needs at least
     10 true paths on the dev half to be eligible (below that the bound is not estimable).
  2. The family is INCLUDED if, on the TEST half (even surahs), that variant's lift_af lower bound is > 1.
     It is marked branch-discriminating if its test-half lift_b lower bound is also > 1 (branch->root scope only).
  3. A family whose every variant has test lift_af upper bound <= 1.05 or dev lower bound < 1 is EXCLUDED as carrying
     no activation signal on this set.
Then, for the included set: union coverage and union lift (per activator pair), each type's unique contribution, and
lift by the target's branch_kind and branch number. Writes selection.json and prints a summary."""
import sys, os, json, math, random, collections
import numpy as np
sys.dont_write_bytecode = True
import lib, links
import eval_hft as E

FAMILIES = collections.OrderedDict([
    ('definitional_pointer', ['ptr', 'ptr_card400', 'ptr_df1000', 'ptr_df300', 'ptr_df100', 'ptr_df30', 'ptr_lemma']),
    ('rare_lemma_bridge', ['bridge30', 'bridge100', 'bridge30_sig2', 'bridge100_sig2', 'bridge30_rev']),
    ('dictionary_neighbour', ['nb_any', 'nb_synonym', 'nb_near_neighbor', 'nb_same_field', 'nb_thematic']),
    ('antonym_polarity', ['nb_contrast']),
    ('root_cooccurrence', ['cooc_ayah_pmi0', 'cooc_ayah_pmi1', 'cooc_ayah_pmi2', 'cooc_win3_pmi0', 'cooc_win3_pmi1',
                           'cooc_win3_pmi2']),
    ('formula_cooccurrence', ['formula_k3', 'formula_k5', 'formula_k10', 'formula_k5_pmi']),
    ('slm_similarity', ['slm_pair10', 'slm_pair3', 'slm_p99', 'slm_p95']),
    ('qnet_keywords', ['qnet_any', 'qnet_df50', 'qnet_df200', 'qnet_core', 'qnet_core_df50']),
    ('early_cocitation', ['cc_quote_root', 'cc_quote_branch', 'cc_else_branch', 'cc_else_root']),
])
MIN_TRUE = 10
# Diagnostics, never selectable: the field splits (image/what_is were shown to the HFT readers for the focus word, the
# source phrase was not), and the reverse pointer, which is the same type seen from the partner's branch (in a supply
# it is shown at the naming branch, so it is already covered by the definitional pointer run over every branch).
DIAGNOSTIC = ['ptr_imgwhat', 'ptr_imgwhat_df300', 'ptr_phrase', 'ptr_phrase_only', 'ptr_phrase_only_df300', 'ptr_rev',
              'ptr_rev_df300', 'cc_here_branch', 'cc_here_root']


def lo(t):
    return -1 if not t or t[0] is None or (isinstance(t[0], float) and math.isnan(t[0])) else t[0]


def choose(R):
    out = collections.OrderedDict()
    for fam, vs in FAMILIES.items():
        elig = [v for v in vs if R['dev'][v]['true_paths'] >= MIN_TRUE]
        if not elig:
            out[fam] = dict(decision='insufficient data', variants=vs,
                            note='fewer than %d true paths on the dev half in every variant' % MIN_TRUE)
            continue
        best = max(elig, key=lambda v: lo(R['dev'][v]['lift_af_ci_ayah']))
        t = R['test'][best]; d = R['dev'][best]; f = R['full'][best]
        inc = lo(t['lift_af_ci_ayah']) > 1.0
        branch_disc = None
        if f['scope'] == 'branch->root':
            branch_disc = lo(t.get('lift_b_ci_ayah')) > 1.0
        out[fam] = dict(decision='include' if inc else 'exclude', chosen=best, scope=f['scope'],
                        dev_lift_af=d['lift_af'], dev_ci=d['lift_af_ci_ayah'],
                        test_lift_af=t['lift_af'], test_ci=t['lift_af_ci_ayah'],
                        test_lift_b=t.get('lift_b'), test_lift_b_ci=t.get('lift_b_ci_ayah'),
                        branch_discriminating=branch_disc,
                        full_lift_af=f['lift_af'], full_ci_ayah=f['lift_af_ci_ayah'], full_ci_surah=f['lift_af_ci_surah'],
                        full_lift_b=f.get('lift_b'), full_lift_b_ci=f.get('lift_b_ci_ayah'),
                        coverage=f['coverage'], paths_per_ayah=R['volume'][best]['paths_per_ayah_mean'],
                        paths_per_ayah_p90=R['volume'][best]['paths_per_ayah_p90'],
                        share_frequent_element=R['volume'][best]['share_frequent_element'],
                        share_frequent_partner=R['volume'][best]['share_frequent_partner'])
    return out


def union_analysis(types, cases):
    """per activator pair: reached by any included type; base: frequency-matched other word (same rule as eval)"""
    rng = np.random.default_rng(E.SEED)
    rows = []
    for c in cases:
        X = (c['s'], c['a']); T = (c['rid'], c['bid']); acts = c['acts']
        others = E.other_word_roots(X, {c['root']} | set(acts))
        if not others:
            continue
        bins = collections.defaultdict(list)
        for r in others:
            bins[E.dfbin(r)].append(r)
        ob = [k for k in lib.RID_BR[c['rid']] if k != T]
        for r in acts:
            b = E.dfbin(r)
            cand = None
            for dlt in range(0, len(E.BINS) + 1):
                cand = bins.get(b - dlt, []) + (bins.get(b + dlt, []) if dlt else [])
                if cand:
                    break
            hit = {nm: bool(links.TYPES[nm][2](T, r, X)) for nm in types}
            base = {nm: sum(1 for x in cand if links.TYPES[nm][2](T, x, X)) / len(cand) for nm in types}
            base_any = sum(1 for x in cand if any(links.TYPES[nm][2](T, x, X) for nm in types)) / len(cand)
            bb = (sum(1 for t2 in ob if any(links.TYPES[nm][2](t2, r, X) for nm in types)) / len(ob)) if ob else float('nan')
            rows.append(dict(ay=c['s'] * 1000 + c['a'], s=c['s'], hit=hit, base=base, any=any(hit.values()),
                             base_any=base_any, base_b_any=bb, kind=lib.BR[T]['kind'], bnum=int(c['bid'][1:]),
                             w=1 / len(acts)))
    return rows


def lift_ci(y, e, cl, w):
    y = np.array(y, float) * w; e = np.array(e, float) * w
    m = ~np.isnan(e)
    y, e, cl = y[m], e[m], np.array(cl)[m]
    uniq, inv = np.unique(cl, return_inverse=True)
    ys = np.bincount(inv, weights=y); es = np.bincount(inv, weights=e)
    rng = np.random.default_rng(E.SEED)
    idx = rng.integers(0, len(uniq), size=(E.B, len(uniq)))
    L = ys[idx].sum(1) / es[idx].sum(1)
    return float(y.sum() / e.sum()), (float(np.percentile(L, 2.5)), float(np.percentile(L, 97.5))), float(y.sum()), float(e.sum())


def main():
    R = json.load(open(os.path.join(lib.HERE, 'results_hft.json')))
    ch = choose(R)
    inc = [v['chosen'] for v in ch.values() if v.get('decision') == 'include']
    cases = lib.hft_cases()
    rows = union_analysis(inc, cases)
    w = np.array([r['w'] for r in rows]); cl = [r['ay'] for r in rows]
    U = {}
    L, ci, yt, et = lift_ci([r['any'] for r in rows], [r['base_any'] for r in rows], cl, w)
    Lb, cib, _, _ = lift_ci([r['any'] for r in rows], [r['base_b_any'] for r in rows], cl, w)
    U['union'] = dict(types=inc, coverage_pairs=float(np.average([r['any'] for r in rows], weights=w)),
                      lift_af=L, ci=ci, lift_b=Lb, ci_b=cib, true=yt, expected=et)
    # unique contribution: pairs reached only by this type
    uniq = {}
    for nm in inc:
        only = [r['hit'][nm] and not any(r['hit'][o] for o in inc if o != nm) for r in rows]
        uniq[nm] = dict(reached=float(np.average([r['hit'][nm] for r in rows], weights=w)),
                        only_this=float(np.average(only, weights=w)))
    U['unique'] = uniq
    # overlap matrix (Jaccard over reached pairs)
    J = {}
    for a in inc:
        for b in inc:
            if a < b:
                A = np.array([r['hit'][a] for r in rows]); Bm = np.array([r['hit'][b] for r in rows])
                J[f'{a}|{b}'] = float((A & Bm).sum() / max(1, (A | Bm).sum()))
    U['jaccard'] = J
    # by branch_kind and by branch number
    byk = {}
    for kind in ('bare', 'mixed_non_bare', 'non_bare', 'collocation', 'unresolved'):
        sel = [i for i, r in enumerate(rows) if r['kind'] == kind]
        if len(sel) < 30:
            continue
        L, ci, yt, et = lift_ci([rows[i]['any'] for i in sel], [rows[i]['base_any'] for i in sel], [cl[i] for i in sel], w[sel])
        byk[kind] = dict(pairs=len(sel), coverage=float(np.average([rows[i]['any'] for i in sel], weights=w[sel])),
                         lift_af=L, ci=ci)
    U['by_branch_kind'] = byk
    byb = {}
    for lab, f in (('B002-B003', lambda n: n <= 3), ('B004+', lambda n: n >= 4)):
        sel = [i for i, r in enumerate(rows) if f(r['bnum'])]
        L, ci, yt, et = lift_ci([rows[i]['any'] for i in sel], [rows[i]['base_any'] for i in sel], [cl[i] for i in sel], w[sel])
        byb[lab] = dict(pairs=len(sel), coverage=float(np.average([rows[i]['any'] for i in sel], weights=w[sel])),
                        lift_af=L, ci=ci)
    U['by_branch_number'] = byb
    # per-type lift by branch_kind (bare+mixed vs collocation) for the included types
    pk = {}
    for nm in inc:
        pk[nm] = {}
        for lab, ks in (('bare_or_mixed', ('bare', 'mixed_non_bare')), ('collocation_or_non_bare', ('collocation', 'non_bare'))):
            sel = [i for i, r in enumerate(rows) if r['kind'] in ks]
            L, ci, yt, et = lift_ci([rows[i]['hit'][nm] for i in sel], [rows[i]['base'][nm] for i in sel], [cl[i] for i in sel], w[sel])
            pk[nm][lab] = dict(pairs=len(sel), lift_af=L, ci=ci, true=yt)
    U['per_type_by_kind'] = pk
    out = dict(rule=__doc__.split('Rule')[1].split('Then,')[0].strip(), families=ch, included=U)
    json.dump(out, open(os.path.join(lib.HERE, 'selection.json'), 'w'), ensure_ascii=False, indent=1)
    for fam, v in ch.items():
        if v.get('decision') in ('include', 'exclude'):
            print(f"{fam:22s} {v['decision']:8s} {v['chosen']:18s} dev {v['dev_lift_af']:.2f} {v['dev_ci']} test {v['test_lift_af']:.2f} "
                  f"[{v['test_ci'][0]:.2f},{v['test_ci'][1]:.2f}] lift_b {v['test_lift_b']} disc {v['branch_discriminating']} "
                  f"paths/ayah {v['paths_per_ayah']:.1f}")
        else:
            print(fam, v)
    print(json.dumps(U, ensure_ascii=False, indent=1)[:6000])


if __name__ == '__main__':
    main()
