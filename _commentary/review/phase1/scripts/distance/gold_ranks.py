#!/usr/bin/env python3
"""Read-only: ranks of S1 gold-ledger anchor pairs in the quran-slm networks.

Global: directional ranks per signal (E5, char, Neo) from the u16 rank maps, and
the rank of b in a's fused affinity row (0.35 E5 + 0.35 Neo + 0.30 char, symmetric
RRF offset 10), counted over all other-root cards.
Local S1: rank of b among a's cross-root branches in the stored s001 affinity.npy.
"""
import json, csv, sys, itertools
import numpy as np

SLM = '/Volumes/OZTURK/_projects/quran-slm'
cat = json.load(open(f'{SLM}/artifacts/corpus_network/catalog.json'))['cards']
N = len(cat)
idx = {c['node_id']: c['global_index'] for c in cat}
root = np.array([c['surface_root_key'] for c in cat])
disp = {c['global_index']: c['display_key'] for c in cat}

csv.field_size_limit(10**9)
img = {}
with open(f'{SLM}/resources/source/corpus_branches_ar.tsv', encoding='utf-8') as f:
    for r in csv.DictReader(f, delimiter='\t'):
        img[r['node_id']] = r['branch_image_ar']

def load(p):
    return np.fromfile(p, dtype='<u2').reshape(N, N)

E5 = load(f'{SLM}/artifacts/corpus_network/e5_directional_rank.u16le')
CH = load(f'{SLM}/artifacts/corpus_network/character_directional_rank.u16le')
NEO = load(f'{SLM}/artifacts/corpus_ensemble/neoarabert_directional_rank.u16le')

def rrf_row(R, a):
    out = R[a, :].astype(np.float32); inn = R[:, a].astype(np.float32)
    elig = R[a, :] != 0
    res = np.zeros(N, np.float32)
    res[elig] = 0.5 * (1 / (10 + out[elig]) + 1 / (10 + inn[elig]))
    res[a] = 0
    return res, elig

_fused = {}
def fused_row(a):
    if a not in _fused:
        e, elig = rrf_row(E5, a); c, _ = rrf_row(CH, a); n, _ = rrf_row(NEO, a)
        s = 0.35 * e + 0.35 * n + 0.30 * c
        s[~elig] = -1
        _fused[a] = s
    return _fused[a]

def fused_rank(a, b):
    s = fused_row(a)
    return int((s > s[b]).sum()) + 1

# local S1 view
loc = json.load(open(f'{SLM}/artifacts/surah_networks_global_ensemble/s001/catalog.json'))
A = np.load(f'{SLM}/artifacts/surah_networks_global_ensemble/s001/affinity.npy')
lidx = {b['node_id']: b['index'] for b in loc['branches']}
lroot = np.array([b['root'] for b in loc['branches']])
lnode = [b['node_id'] for b in loc['branches']]

def local_rank(a, b):
    ia, ib = lidx[a], lidx[b]
    row = A[ia].copy()
    elig = lroot != lroot[ia]
    row[~elig] = -1
    return int((row > row[ib]).sum()) + 1, int(elig.sum())

def local_top(a, k=3):
    ia = lidx[a]
    row = A[ia].copy(); row[lroot == lroot[ia]] = -1
    o = np.argsort(-row)[:k]
    return [(lnode[j].split(':', 1)[1], img.get(lnode[j], '')[:40]) for j in o]

def pairs_of(r):
    req = r['required_branch_anchors']
    groups = [g['node_ids'] for g in r['required_branch_anchor_groups']]
    ps = set()
    for a, b in itertools.combinations(req, 2):
        ps.add((a, b))
    for g in groups:
        for a in req:
            for b in g:
                ps.add((a, b))
    if not req and len(groups) >= 2:
        for a in groups[0]:
            for b in groups[1]:
                ps.add((a, b))
    return sorted(p for p in ps if root[idx[p[0]]] != root[idx[p[1]]])

rows = []
for l in open(f'{SLM}/reports/s1_ar3_v1_gold_ledger.jsonl'):
    r = json.loads(l)
    for a, b in pairs_of(r):
        ia, ib = idx[a], idx[b]
        lr, lc = local_rank(a, b) if a in lidx and b in lidx else (None, None)
        lr2, _ = local_rank(b, a) if a in lidx and b in lidx else (None, None)
        rows.append(dict(g=r['gold_id'], elig=r['eligibility']['eligible'], a=disp[ia], b=disp[ib],
                         ia=img[a][:30], ib=img[b][:30],
                         e5=(int(E5[ia, ib]), int(E5[ib, ia])), ch=(int(CH[ia, ib]), int(CH[ib, ia])),
                         neo=(int(NEO[ia, ib]), int(NEO[ib, ia])),
                         fused=(fused_rank(ia, ib), fused_rank(ib, ia)), local=(lr, lr2), lc=lc))

json.dump(rows, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
for x in rows:
    print(x['g'], x['elig'], x['a'], '->', x['b'], '|', x['ia'], '|', x['ib'], '| e5', x['e5'], 'ch', x['ch'], 'neo', x['neo'],
          'fusedG', x['fused'], 'localS1', x['local'], '/', x['lc'])

# summary
el = [x for x in rows if x['elig'] and x['local'][0]]
best_local = [min(x['local']) for x in el]
best_glob = [min(x['fused']) for x in el]
print('\nEligible anchor pairs:', len(el))
print('local S1 best-direction rank: median', np.median(best_local), 'min', min(best_local), 'max', max(best_local),
      '<=3:', sum(v <= 3 for v in best_local), '<=10:', sum(v <= 10 for v in best_local))
print('global fused best-direction rank: median', np.median(best_glob), 'min', min(best_glob), 'max', max(best_glob),
      '<=10:', sum(v <= 10 for v in best_glob), '<=100:', sum(v <= 100 for v in best_glob), '<=1000:', sum(v <= 1000 for v in best_glob))

print('\nTop-3 local partners for scene anchors:')
for a in ['quranic:root_001040:B002', 'quranic:root_001444:B006', 'quranic:root_000973:B005', 'quranic:root_000858:B002',
          'quranic:root_000913:B005', 'quranic:root_001444:B008', 'quranic:root_001525:B005', 'quranic:root_000532:B013',
          'quranic:root_001444:B007', 'quranic:root_000745:B004', 'quranic:root_001040:B005', 'quranic:root_001273:B012',
          'quranic:root_001119:B001', 'quranic:root_000858:B001']:
    print(disp[idx[a]], img[a][:40], '=>', local_top(a))
