"""Evaluate the construction guard against root-dossier plain branches (collocation-bound ones), excluding dossier
rows marked 'stop' (unanalysed function roots). Subsets: all; excluding the two grammatical constructions
(nafs 'self', min duni 'other than'); lexically fixed signatures (a partner recurring in >=2 early-source phrases)."""
import sys, json, collections
sys.dont_write_bytecode = True
sys.path.insert(0, '.')
import construction as K, common as C
br = C.trcache()['br']; r2i, i2r = C.root_ids(); occ = K.root_occurrences(); dos = C.dossier()
GRAM = {'root_001533/B012', 'root_000502/B003'}
sigs = {}
for bref, info in br.items():
    if info['kind'] != 'collocation': continue
    root = i2r.get(bref.split('/')[0])
    if root and root in C.dossier_roots(): sigs[bref] = (root, K.signature(root, info))
ctxc = {}
out = {}
for rule in ('R1', 'R3', 'R4', 'R5'):
    for subset in ('all', 'excl_2_grammatical', 'lexically_fixed_excl_gram'):
        tp = fn = fp = tn = 0
        for bref, (root, sg) in sigs.items():
            fixed = any(n >= 2 for n in sg['roots'].values())
            if subset != 'all' and bref in GRAM: continue
            if subset == 'lexically_fixed_excl_gram' and not fixed: continue
            for ref3 in occ.get(root, []):
                d = dos.get(ref3)
                if not d or d['root'] != root or not d['b'].startswith('root_'): continue
                if (ref3, root) not in ctxc: ctxc[(ref3, root)] = K.occ_context(ref3, root)
                ok, _ = K.present(sg, ctxc[(ref3, root)], rule)
                if d['b'] == bref: tp += ok; fn += (not ok)
                else: fp += ok; tn += (not ok)
        out[f'{rule}:{subset}'] = dict(tp=tp, fn=fn, fp=fp, tn=tn, recall=round(tp / max(1, tp + fn), 3),
                                       false_activation_rate=round(fp / max(1, fp + tn), 4), precision=round(tp / max(1, tp + fp), 3))
        print(rule, subset, out[f'{rule}:{subset}'])
json.dump(out, open('construction_eval2.json', 'w'), indent=1)
