"""Robustness: base (a) matched on part of speech AND frequency bin (activators are content words chosen by a reader;
frequency matching alone leaves a POS difference). For each activator root, candidates are other words of the same
ayah with the same QAC POS tag and frequency bin; else same POS any bin; else same bin; else skipped.
Reported for the recommended and borderline types only. Writes robust_pos.json."""
import sys, os, json, collections
import numpy as np
sys.dont_write_bytecode = True
import lib, links
import eval_hft as E

TYPES = ['ptr_card400', 'ptr_df300', 'ptr_phrase_only', 'nb_any', 'cooc_ayah_pmi2', 'cooc_win3_pmi1', 'slm_p99',
         'qnet_core_df50', 'cc_quote_root', 'bridge30_sig2', 'formula_k5_pmi']


def main():
    cases = lib.hft_cases()
    y = collections.defaultdict(list); e = collections.defaultdict(list); cl = []
    used = collections.Counter()
    for c in cases:
        X = (c['s'], c['a']); T = (c['rid'], c['bid']); acts = c['acts']
        excl = {c['root']} | set(acts)
        others = [(w['roots'][0], w['pos']) for w in lib.BY_AYAH[X] if w['roots'] and w['roots'][0] not in excl]
        if not others:
            continue
        matches = []
        for r in acts:
            pos = next((w['pos'] for w in lib.BY_AYAH[X] if r in w['roots']), None)
            b = E.dfbin(r)
            for lab, cand in (('pos+bin', [o for o, p in others if p == pos and E.dfbin(o) == b]),
                              ('pos', [o for o, p in others if p == pos]),
                              ('bin', [o for o, p in others if E.dfbin(o) == b])):
                if cand:
                    matches.append((r, cand)); used[lab] += 1; break
            else:
                used['none'] += 1
        if not matches:
            continue
        cl.append(c['s'] * 1000 + c['a'])
        for nm in TYPES:
            f = links.TYPES[nm][2]
            y[nm].append(sum(1 for r, _ in matches if f(T, r, X)) / len(matches))
            e[nm].append(sum(sum(1 for o in cand if f(T, o, X)) / len(cand) for _, cand in matches) / len(matches))
    rng = np.random.default_rng(E.SEED)
    cl = np.array(cl)
    out = dict(match_levels=dict(used), types={})
    for nm in TYPES:
        Y = np.array(y[nm]); Ea = np.array(e[nm])
        out['types'][nm] = dict(lift_pos_bin=E.lift(Y, Ea), ci_ayah=E.boot(Y, Ea, cl, rng),
                                true=float(Y.sum()), expected=float(Ea.sum()))
    json.dump(out, open(os.path.join(lib.HERE, 'robust_pos.json'), 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
