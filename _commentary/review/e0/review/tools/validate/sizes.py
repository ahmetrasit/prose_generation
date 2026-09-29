"""Supply size of the recommended link lines, in calibrated tokens (1.151 x Arabic chars + 0.366 x other chars; the
4,581-token per-call constant is NOT included: these are increments). Display templates are descriptive only: no
score, rank, PMI value or count used for sorting; lines in ayah word order, branches in dictionary order.
Sample: 300 seeded ayat from the whole Quran (not only the HFT set), plus 2:282 (the longest ayah).
Also: the merged image-pair line (slm_p99 OR qnet_core_df50) on the HFT set, and the 29:38 in-sample union.
Writes sizes.json."""
import sys, os, json, random, re, collections
import numpy as np
sys.dont_write_bytecode = True
import lib, links
import eval_hft as E
import select_links as S

AR = re.compile('[؀-ۿ]')


def ctok(s):
    a = len(AR.findall(s))
    return 1.151 * a + 0.366 * (len(s) - a)


def img(k):
    return lib.BR[k]['image']


def lines_for(X, types):
    """one display line per unit, per type"""
    words = [w for w in lib.BY_AYAH[X] if w['roots']]
    first = {}
    for w in words:
        first.setdefault(w['roots'][0], w)
    out = collections.defaultdict(list)
    seen = collections.defaultdict(set)
    for ri, wi in first.items():
        for T in lib.ROOT_BR.get(ri, ()):
            for rj, wj in first.items():
                if rj == ri:
                    continue
                for nm in types:
                    fam, scope, f = links.TYPES[nm]
                    el = f(T, rj, X)
                    if not el:
                        continue
                    u = (T, rj) if scope == 'branch->root' else tuple(sorted((ri, rj)))
                    if u in seen[nm]:
                        continue
                    seen[nm].add(u)
                    if nm.startswith('ptr'):
                        s = f"- {ri} {T[1]} names «{el}» → {wj['surface']} ({rj}, w{wj['w']})"
                    elif nm.startswith('nb'):
                        b = next(b for b in lib.ROOT_BR[rj] if lib.REL.get(T, {}).get(b))
                        s = f"- {ri} {T[1]} «{img(T)}» / {rj} {b[1]} «{img(b)}»: {el}"
                    elif nm.startswith('cooc'):
                        wit = sorted((lib.ROOT_AY[ri] & lib.ROOT_AY[rj]) - {X})
                        s = f"- {ri} + {rj} also meet in " + ', '.join(f'{a}:{b}' for a, b in wit)
                    elif nm in ('slm_p99', 'qnet_core_df50', 'imgpair'):
                        best, bb = links._slm_best(T, rj)
                        if bb is None:
                            bb = lib.ROOT_BR[rj][0]
                        s = f"- {ri} {T[1]} «{img(T)}» ~ {rj} {bb[1]} «{img(bb)}»"
                    elif nm == 'cc_quote_root':
                        s = f"- early citation of {X[0]}:{X[1]} under {ri} quotes {wj['surface']} ({rj})"
                    else:
                        s = f"- {ri} {T[1]} ~ {rj}: {el}"
                    out[nm].append(s)
    return out


def main():
    links.TYPES['imgpair'] = ('similarity', 'branch->root',
                              lambda T, r, X: links.TYPES['slm_p99'][2](T, r, X) or links.TYPES['qnet_core_df50'][2](T, r, X))
    types = ['ptr_card400', 'nb_any', 'cooc_ayah_pmi2', 'slm_p99', 'qnet_core_df50', 'imgpair', 'cc_quote_root']
    rnd = random.Random(E.SEED + 1)
    samp = rnd.sample(lib.AYAT, 300)
    per = {nm: [] for nm in types}
    nlines = {nm: [] for nm in types}
    for X in samp:
        L = lines_for(X, types)
        for nm in types:
            per[nm].append(sum(ctok(s) + 1 for s in L[nm]))
            nlines[nm].append(len(L[nm]))
    L282 = lines_for((2, 282), types)
    out = dict(sample='300 random ayat of the whole Quran (seed %d)' % (E.SEED + 1), types={})
    for nm in types:
        a = np.array(per[nm]); n = np.array(nlines[nm])
        out['types'][nm] = dict(lines_mean=float(n.mean()), lines_p90=float(np.percentile(n, 90)),
                                tokens_mean=float(a.mean()), tokens_median=float(np.median(a)),
                                tokens_p90=float(np.percentile(a, 90)), tokens_max=float(a.max()),
                                lines_2_282=len(L282[nm]), tokens_2_282=float(sum(ctok(s) + 1 for s in L282[nm])),
                                example=(L282[nm][:2] if L282[nm] else []))
    core = ['ptr_card400', 'nb_any', 'cooc_ayah_pmi2']
    tot_core = np.sum([per[nm] for nm in core], axis=0)
    out['push_core_total'] = dict(types=core, tokens_mean=float(tot_core.mean()), tokens_p90=float(np.percentile(tot_core, 90)),
                                  tokens_2_282=float(sum(out['types'][nm]['tokens_2_282'] for nm in core)))
    tot_all = tot_core + np.array(per['imgpair'])
    out['push_core_plus_imgpair_total'] = dict(tokens_mean=float(tot_all.mean()), tokens_p90=float(np.percentile(tot_all, 90)),
                                               tokens_2_282=out['push_core_total']['tokens_2_282'] + out['types']['imgpair']['tokens_2_282'])
    # merged image-pair on the HFT set (lift vs frequency-matched other word; branch lift)
    cases = lib.hft_cases()
    rows = S.union_analysis(['imgpair'], cases)
    w = np.array([r['w'] for r in rows]); cl = [r['ay'] for r in rows]
    Lf, ci, yt, et = S.lift_ci([r['any'] for r in rows], [r['base_any'] for r in rows], cl, w)
    Lb, cib, _, _ = S.lift_ci([r['any'] for r in rows], [r['base_b_any'] for r in rows], cl, w)
    out['imgpair_hft'] = dict(coverage=float(np.average([r['any'] for r in rows], weights=w)), lift_af=Lf, ci=ci,
                              lift_b=Lb, ci_b=cib)
    for label, ts in (('push_core_hft', core), ('push_core_plus_imgpair_hft', core + ['imgpair'])):
        rows = S.union_analysis(ts, cases)
        w = np.array([r['w'] for r in rows]); cl = [r['ay'] for r in rows]
        Lf, ci, yt, et = S.lift_ci([r['any'] for r in rows], [r['base_any'] for r in rows], cl, w)
        Lb, cib, _, _ = S.lift_ci([r['any'] for r in rows], [r['base_b_any'] for r in rows], cl, w)
        out[label] = dict(types=ts, coverage=float(np.average([r['any'] for r in rows], weights=w)), lift_af=Lf, ci=ci,
                          lift_b=Lb, ci_b=cib)
    # 29:38 in-sample union of the recommended push set and of push + imgpair
    import eval_29_38 as G
    hits = {}
    for label, ts in (('push_core', core), ('push_core_plus_imgpair', core + ['imgpair'])):
        h = 0
        for root, bid, Y, pr, note in G.GOLD:
            T = G.key(root, bid)
            h += any(links.TYPES[nm][2](T, pr, G.X0) for nm in ts)
        c = G.CONTROL; T = G.key(c[0], c[1])
        hits[label] = dict(gold_hits=h, of=len(G.GOLD), control_hit=any(links.TYPES[nm][2](T, c[3], G.X0) for nm in ts))
    out['in_sample_29_38'] = hits
    json.dump(out, open(os.path.join(lib.HERE, 'sizes.json'), 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
