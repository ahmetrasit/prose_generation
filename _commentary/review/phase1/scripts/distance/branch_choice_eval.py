#!/usr/bin/env python3
"""Read-only evaluation, independent of the quran-slm ranks: given branch a of word X that a
v12 reader co-cited with branch b of word Y (another root) in one strong finding, which signal best
picks b among ALL branches of Y's root?  (Controls for word identity; asks exactly 'which branch
of the neighbouring word is activated by a'.)

Signals: slm fused affinity (0.35 E5 + 0.35 Neo + 0.30 char, symmetric RRF) and its components;
Luna scene tags (shared concrete scene; shared scene with a different role); Turkish dictionary
neighbor_distinctions link; Qnet keyword Jaccard; a naive shared-mention score; and the
branch-order prior (B001 first), because readers cite primary branches most.
"""
import csv, json, glob, collections, itertools, random, math, re
import numpy as np
csv.field_size_limit(10**9)
SLM = '/Volumes/OZTURK/_projects/quran-slm'
cat = json.load(open(f'{SLM}/artifacts/corpus_network/catalog.json'))['cards']; N = len(cat)
gi = {(c['source_root_id'], c['branch_id']): c['global_index'] for c in cat}
rootkey = [c['surface_root_key'] for c in cat]
rid = [c['source_root_id'] for c in cat]
bnum = [int(c['branch_id'][1:]) for c in cat]
by_root = collections.defaultdict(list)
for c in cat: by_root[c['source_root_id']].append(c['global_index'])

def load(p): return np.fromfile(p, dtype='<u2').reshape(N, N)
E5 = load(f'{SLM}/artifacts/corpus_network/e5_directional_rank.u16le')
CH = load(f'{SLM}/artifacts/corpus_network/character_directional_rank.u16le')
NEO = load(f'{SLM}/artifacts/corpus_ensemble/neoarabert_directional_rank.u16le')
def rrf(R, a, b): return 0.5 * (1 / (10 + float(R[a, b])) + 1 / (10 + float(R[b, a])))
def s_fused(a, b): return 0.35 * rrf(E5, a, b) + 0.35 * rrf(NEO, a, b) + 0.30 * rrf(CH, a, b)

# Luna scenes
tags = collections.defaultdict(set)
k2i = {f"{c['surface_root_key']} {c['branch_id']}": c['global_index'] for c in cat}
for f in glob.glob('/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/frames/out/*.json'):
    for it in json.load(open(f))['items']:
        if it['key'] in k2i:
            for fr in it['frames']:
                if not fr['frame'].startswith(('moral.', 'divine.')):
                    tags[k2i[it['key']]].add((fr['frame'], fr['role']))
def s_scene(a, b): return len({t[0] for t in tags[a]} & {t[0] for t in tags[b]})
def s_scene_comp(a, b):
    sa = {t[0] for t in tags[a]} & {t[0] for t in tags[b]}
    return sum(1 for s in sa if {t[1] for t in tags[a] if t[0] == s} != {t[1] for t in tags[b] if t[0] == s})
def s_domain(a, b): return len({t[0].split('.')[0] for t in tags[a]} & {t[0].split('.')[0] for t in tags[b]})

# Turkish dictionary neighbor_distinctions
rel = collections.defaultdict(set)
for f in glob.glob('/Volumes/OZTURK/_projects/quran-data/data/dictionary/tr/*_entry.json'):
    d = json.load(open(f))
    for br in d.get('branches', []):
        ref = br.get('branch_ref', '')
        m = re.search(r'(root_\d+)/(B\d+)', ref)
        if not m: continue
        a = gi.get((m.group(1), m.group(2)))
        for nd in br.get('neighbor_distinctions') or []:
            m2 = re.search(r'(root_\d+)/(B\d+)', nd.get('neighbor_ref', ''))
            if not m2: continue
            b = gi.get((m2.group(1), m2.group(2)))
            if a is not None and b is not None:
                rel[a].add(b); rel[b].add(a)
def s_dict(a, b): return 1.0 if b in rel[a] else 0.0

# Qnet keywords
kw = collections.defaultdict(set)
for r in csv.DictReader(open('/Volumes/OZTURK/_projects/quran-roots/_corpus/activation/Qnet/v2/network/incidence_full/branch_keywords.tsv', encoding='utf-8'), delimiter='\t'):
    i = gi.get((r['root_id'], r['branch_id']))
    if i is not None: kw[i].add(r['keyword'])
kdf = collections.Counter(k for v in kw.values() for k in v)
def s_qnet(a, b):
    sh = kw[a] & kw[b]
    return sum(math.log(N / kdf[k]) for k in sh)

def s_prior(a, b): return -bnum[b]

SIGNALS = dict(slm_fused=s_fused, slm_e5=lambda a, b: rrf(E5, a, b), slm_neo=lambda a, b: rrf(NEO, a, b),
               slm_char=lambda a, b: rrf(CH, a, b), luna_scene=s_scene, luna_scene_other_role=s_scene_comp,
               luna_domain=s_domain, dict_neighbor=s_dict, qnet_kw=s_qnet, prior_B001_first=s_prior)

# v12 strong co-citations
F = collections.defaultdict(set); G = {}
for f in glob.glob('/Volumes/OZTURK/_projects/latent_activation/_status/v12_cross_run/s[0-9][0-9][0-9]/derived/finding_word_branches.v3.tsv'):
    for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
        k = (f, r['finding_id']); G[k] = r['grade']
        i = gi.get((r['root_id'], r['branch_id']))
        if i is not None: F[k].add(i)
tests = set()
for k, v in F.items():
    if G[k] != 'strong': continue
    for a, b in itertools.permutations(sorted(v), 2):
        if rid[a] != rid[b] and len(by_root[rid[b]]) >= 3:
            # the finding must not also cite another branch of b's root (keeps one target)
            if sum(1 for x in v if rid[x] == rid[b]) == 1:
                tests.add((a, b))
tests = sorted(tests)
random.seed(1)
if len(tests) > 12000: tests = random.sample(tests, 12000)
print('test cases (a -> b among all branches of root(b), root has >=3 branches):', len(tests))
res = {s: [] for s in SIGNALS}; nonB001 = {s: [] for s in SIGNALS}; rnd = []
for a, b in tests:
    cands = by_root[rid[b]]
    rnd.append(1 / len(cands))
    for name, fn in SIGNALS.items():
        sc = {c: fn(a, c) for c in cands}
        v = sc[b]
        better = sum(1 for c in cands if sc[c] > v); ties = sum(1 for c in cands if sc[c] == v) - 1
        rank = better + 1 + ties / 2
        res[name].append(1 / rank)
        if bnum[b] != 1: nonB001[name].append(1 / rank)
print(f'random-choice MRR baseline: {np.mean(rnd):.3f}')
share_b001 = np.mean([bnum[b] == 1 for a, b in tests])
print(f'share of targets that are B001: {share_b001:.3f}')
for name in SIGNALS:
    print(f'{name:24s} MRR all={np.mean(res[name]):.3f}  MRR non-B001 targets={np.mean(nonB001[name]):.3f} (n={len(nonB001[name])})')
# combined simple rules
def comb(a, b):
    return (s_scene_comp(a, b) + s_scene(a, b)) * 1.0 + 20 * s_fused(a, b) + 0.5 * s_dict(a, b)
res_c = []; res_c2 = []
for a, b in tests:
    cands = by_root[rid[b]]
    sc = {c: comb(a, c) for c in cands}; v = sc[b]
    rank = sum(1 for c in cands if sc[c] > v) + 1 + (sum(1 for c in cands if sc[c] == v) - 1) / 2
    res_c.append(1 / rank)
    if bnum[b] != 1: res_c2.append(1 / rank)
print(f'{"scene+slm+dict (untuned)":24s} MRR all={np.mean(res_c):.3f}  MRR non-B001 targets={np.mean(res_c2):.3f}')
