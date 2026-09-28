"""Neighbour-conditioned branch pull (layer H): for each root of the focus ayah, rank ALL its branches by their best
quran-slm fused affinity (0.35 E5 + 0.35 Neo + 0.30 char, symmetric RRF, as in Phase 1 branch_choice_eval.py) to any
branch of the OTHER roots in the ayah (and ±1 ayah). Output per root: branch order with the pulling neighbour branch
as the path. Used only as ordering; never a filter. Phase 1 measured this selector at MRR 0.54 for context-linked words."""
import json, sys, collections, csv
import numpy as np
import lib

SLM = '/Volumes/OZTURK/_projects/quran-slm'
cat = json.load(open(f'{SLM}/artifacts/corpus_network/catalog.json'))['cards']; N = len(cat)
gi = {(c['source_root_id'], c['branch_id']): c['global_index'] for c in cat}
by_root = collections.defaultdict(list)
for c in cat: by_root[c['surface_root_key']].append(c['global_index'])
key = {c['global_index']: (c['source_root_id'], c['branch_id'], c['surface_root_key']) for c in cat}
E5 = np.memmap(f'{SLM}/artifacts/corpus_network/e5_directional_rank.u16le', dtype='<u2', mode='r', shape=(N, N))
CH = np.memmap(f'{SLM}/artifacts/corpus_network/character_directional_rank.u16le', dtype='<u2', mode='r', shape=(N, N))
NEO = np.memmap(f'{SLM}/artifacts/corpus_ensemble/neoarabert_directional_rank.u16le', dtype='<u2', mode='r', shape=(N, N))


def fused_block(A, B):
    A = np.array(A); B = np.array(B)
    def rr(R):
        ab = R[np.ix_(A, B)].astype(np.float32); ba = R[np.ix_(B, A)].astype(np.float32).T
        # rank 0 means not ranked (same-root excluded) -> treat as very far
        ab[ab == 0] = 60000; ba[ba == 0] = 60000
        return 0.5 * (1 / (10 + ab) + 1 / (10 + ba))
    return 0.35 * rr(E5) + 0.35 * rr(NEO) + 0.30 * rr(CH)


def ayah_roots(ref):
    rs = []
    with open(lib.SLM + '/qac_root_ayah.tsv', encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['ayah_ref'] == ref: rs.append(r['root_norm'])
    return rs


def pull(ref, window=1):
    s, a = map(int, ref.split(':'))
    focus = [r for r in ayah_roots(ref) if r != 'ء ل ه']
    ctx = set(focus)
    for x in range(a - window, a + window + 1):
        if x != a: ctx |= set(ayah_roots(f'{s}:{x}'))
    ctx.discard('ء ل ه')
    out = {}
    for R in focus:
        A = by_root.get(R, [])
        if len(A) < 3: continue
        others = [i for R2 in ctx if R2 != R for i in by_root.get(R2, [])]
        if not others: continue
        M = fused_block(A, others)
        best = M.max(axis=1); arg = M.argmax(axis=1)
        order = np.argsort(-best)
        out[R] = [(key[A[i]][1], round(float(best[i]), 4), f"{key[others[arg[i]]][2]} {key[others[arg[i]]][1]}") for i in order]
    return out


if __name__ == '__main__':
    for ref in sys.argv[1:] or ['29:38']:
        res = pull(ref)
        print('==', ref)
        for R, lst in res.items():
            print(R, ' | '.join(f"{b}←{p} ({s})" for b, s, p in lst[:5]), f'| n={len(lst)}')
