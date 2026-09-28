#!/usr/bin/env python3
"""Read-only: are the network-v3 channel-review subchannels (built from candidates mined
on the quran-slm surah-local affinity) closer in that affinity than Luna scene partners?
Measures circularity of the channel reviews as an evaluation set for a new distance.

For each surah: parse '- Active motifs:' lines (one subchannel each), take cross-root
branch pairs, compute best-direction local rank in the s### view (affinity.npy), and the
same for Luna scene-tag pairs (same concrete scene) restricted to that surah's catalog.
"""
import json, re, glob, sys, collections, itertools, random
import numpy as np

SLM = '/Volumes/OZTURK/_projects/quran-slm/artifacts/surah_networks_global_ensemble'
REV = '/Volumes/OZTURK/_projects/latent_activation/network/v3/reviews'
V15 = '/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/frames/out'

tags = collections.defaultdict(set)
for f in glob.glob(f'{V15}/*.json'):
    for it in json.load(open(f))['items']:
        for fr in it['frames']:
            if not fr['frame'].startswith(('moral.', 'divine.')):
                tags[it['key']].add(fr['frame'])

pat = re.compile(r'`([^`:]+):(B\d{3})(?:/m\d+)?`')
res = collections.defaultdict(list)
rng = random.Random(3)
nsur = 0
for d in sorted(glob.glob(f'{REV}/s*/reader_a_pilot.md')):
    s = d.split('/')[-2]
    try:
        cat = json.load(open(f'{SLM}/{s}/catalog.json'))
        A = np.load(f'{SLM}/{s}/affinity.npy')
    except FileNotFoundError:
        continue
    # display key -> index (skip ambiguous display keys)
    cnt = collections.Counter(b['display_key'] for b in cat['branches'])
    k2i = {b['display_key']: b['index'] for b in cat['branches'] if cnt[b['display_key']] == 1}
    roots = np.array([b['root'] for b in cat['branches']])
    n = len(roots)
    if n > 2500:  # keep it quick: skip the very largest views
        continue
    nsur += 1
    # local rank matrix (best direction later)
    M = A.copy()
    same = roots[:, None] == roots[None, :]
    M[same] = -1
    order = np.argsort(-M, axis=1, kind='stable')
    R = np.empty_like(order); R[np.arange(n)[:, None], order] = np.arange(1, n + 1)[None, :]
    elig_counts = (~same).sum(1)
    def best(i, j):
        return min(R[i, j], R[j, i])
    text = open(d, encoding='utf-8').read()
    rev_pairs = set()
    for line in text.splitlines():
        if line.startswith('- Active motifs:') or line.startswith('- Active bridge motifs:'):
            ids = {f"{r.strip()}:{b}" for r, b in pat.findall(line)}
            ids = [k2i[x] for x in ids if x in k2i]
            for i, j in itertools.combinations(sorted(set(ids)), 2):
                if roots[i] != roots[j]:
                    rev_pairs.add((i, j))
    for i, j in rev_pairs:
        res['review_subchannel'].append(best(i, j) / ((elig_counts[i] + elig_counts[j]) / 2))
        res['review_subchannel_raw'].append(best(i, j))
    # Luna scene pairs inside this surah
    keyof = {b['index']: f"{b['root']} {b['branch_id']}" for b in cat['branches']}
    byscene = collections.defaultdict(list)
    for i in range(n):
        for fr in tags.get(keyof[i], ()):
            byscene[fr].append(i)
    sc_pairs = set()
    for fr, mem in byscene.items():
        for i, j in itertools.combinations(sorted(mem), 2):
            if roots[i] != roots[j]:
                sc_pairs.add((i, j))
    sc_pairs = list(sc_pairs)
    if len(sc_pairs) > 5 * max(1, len(rev_pairs)):
        sc_pairs = rng.sample(sc_pairs, 5 * max(1, len(rev_pairs)))
    for i, j in sc_pairs:
        res['luna_same_scene'].append(best(i, j) / ((elig_counts[i] + elig_counts[j]) / 2))
        res['luna_same_scene_raw'].append(best(i, j))
    # random cross-root pairs
    for _ in range(len(rev_pairs)):
        i, j = rng.randrange(n), rng.randrange(n)
        if roots[i] != roots[j]:
            res['random'].append(best(i, j) / ((elig_counts[i] + elig_counts[j]) / 2))
            res['random_raw'].append(best(i, j))

print('surahs processed:', nsur)
for k in ['review_subchannel', 'luna_same_scene', 'random']:
    v = np.array(res[k]); raw = np.array(res[k + '_raw'])
    print(f'{k}: pairs={len(v)} median relative rank={np.median(v):.3f} share best-rank<=10={np.mean(raw<=10):.3f} '
          f'share<=3={np.mean(raw<=3):.3f} median raw rank={np.median(raw):.0f}')
