#!/usr/bin/env python3
"""Read-only: does the quran-slm fused affinity put scene partners (same Luna scene,
different role) near each other, or only near-synonyms (same scene, same role)?

Labels: v15 Luna scene tags (data/frames/out/*.json), keyed 'root Bnnn'.
Network: quran-slm global 10,932-card Quran catalog, fused 0.35 E5 + 0.35 Neo + 0.30 char.
"""
import json, csv, glob, random, collections
import numpy as np

SLM = '/Volumes/OZTURK/_projects/quran-slm'
V15 = '/Volumes/OZTURK/_projects/prose_generation/_commentary/v15'
cat = json.load(open(f'{SLM}/artifacts/corpus_network/catalog.json'))['cards']
N = len(cat)
key2i = {}
for c in cat:
    key2i[f"{c['surface_root_key']} {c['branch_id']}"] = c['global_index']
root = np.array([c['surface_root_key'] for c in cat])

tags = collections.defaultdict(set)
for f in glob.glob(f'{V15}/data/frames/out/*.json'):
    for it in json.load(open(f))['items']:
        k = it['key']
        if k in key2i:
            for fr in it['frames']:
                tags[key2i[k]].add((fr['frame'], fr['role']))
print('catalog cards with scene tags:', len(tags), 'of', N)

ABSTRACT = ('moral.', 'divine.')
def concrete(ts):
    return {t for t in ts if not t[0].startswith(ABSTRACT)}

def load(p):
    return np.fromfile(p, dtype='<u2').reshape(N, N)
E5 = load(f'{SLM}/artifacts/corpus_network/e5_directional_rank.u16le')
CH = load(f'{SLM}/artifacts/corpus_network/character_directional_rank.u16le')
NEO = load(f'{SLM}/artifacts/corpus_ensemble/neoarabert_directional_rank.u16le')

def rrf(R, a):
    out = R[a, :].astype(np.float32); inn = R[:, a].astype(np.float32)
    elig = R[a, :] != 0
    res = np.zeros(N, np.float32)
    res[elig] = 0.5 * (1 / (10 + out[elig]) + 1 / (10 + inn[elig]))
    return res, elig

def fused_ranks(a):
    e, elig = rrf(E5, a); c, _ = rrf(CH, a); n, _ = rrf(NEO, a)
    s = 0.35 * e + 0.35 * n + 0.30 * c
    s[~elig] = -1; s[a] = -1
    order = np.argsort(-s, kind='stable')
    rk = np.empty(N, np.int64); rk[order] = np.arange(1, N + 1)
    return rk, elig

# index: scene -> cards ; (scene, role) -> cards
by_scene = collections.defaultdict(set); by_sr = collections.defaultdict(set)
for i, ts in tags.items():
    for fr, ro in concrete(ts):
        by_scene[fr].add(i); by_sr[(fr, ro)].add(i)

random.seed(7)
sources = [i for i in tags if concrete(tags[i])]
sample = random.sample(sources, 1500)
cats = collections.defaultdict(list)   # category -> list of ranks
top10 = collections.Counter(); base = collections.Counter()
auc_num = 0; auc_den = 0
per_source_med = collections.defaultdict(list)
for a in sample:
    rk, elig = fused_ranks(a)
    ca = concrete(tags[a])
    sr_a = ca; sc_a = {t[0] for t in ca}
    same_role = set().union(*[by_sr[t] for t in sr_a]) if sr_a else set()
    same_scene = set().union(*[by_scene[s] for s in sc_a]) if sc_a else set()
    same_role = {j for j in same_role if elig[j] and j != a}
    diff_role = {j for j in same_scene if elig[j] and j != a} - same_role
    for j in same_role: cats['same_scene_same_role'].append(rk[j])
    for j in diff_role: cats['same_scene_other_role_only'].append(rk[j])
    if same_role: per_source_med['same_role'].append(np.median([rk[j] for j in same_role]))
    if diff_role: per_source_med['diff_role'].append(np.median([rk[j] for j in diff_role]))
    # top-10 composition
    t10 = np.flatnonzero(rk <= 10)
    for j in t10:
        if j in same_role: top10['same_role'] += 1
        elif j in diff_role: top10['other_role_same_scene'] += 1
        elif j in tags: top10['no_shared_concrete_scene'] += 1
        else: top10['untagged'] += 1
    ne = int(elig.sum())
    base['same_role'] += len(same_role) / ne * 10
    base['other_role_same_scene'] += len(diff_role) / ne * 10
    # AUC of other-role scene partners vs random eligible non-scene cards
    if diff_role:
        none = np.flatnonzero(elig)
        none = [j for j in random.sample(list(none), 200) if j not in same_scene and j != a]
        dr = [rk[j] for j in diff_role]
        for x in random.sample(dr, min(30, len(dr))):
            for y in none:
                auc_den += 1; auc_num += (x < y) + 0.5 * (x == y)

print('sources sampled:', len(sample))
for k, v in cats.items():
    v = np.array(v)
    print(f'{k}: n={len(v)} median rank={np.median(v):.0f} p10={np.percentile(v,10):.0f} p25={np.percentile(v,25):.0f} '
          f'share<=10={np.mean(v<=10):.3f} share<=100={np.mean(v<=100):.3f} share<=1000={np.mean(v<=1000):.3f}')
for k, v in per_source_med.items():
    print(f'per-source median rank of {k} partners: median over sources {np.median(v):.0f} (n sources {len(v)})')
tot = sum(top10.values())
print('top-10 neighbour composition:', {k: round(v / tot, 3) for k, v in top10.items()}, 'n=', tot)
print('expected share in a random top-10:', {k: round(v / (10 * len(sample)), 4) for k, v in base.items()})
print('AUC (other-role scene partner ranked above a random non-scene card):', round(auc_num / auc_den, 3), 'pairs', auc_den)
