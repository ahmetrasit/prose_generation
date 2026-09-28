import sys, json, collections, itertools
import numpy as np
sys.dont_write_bytecode = True
sys.path.insert(0, '/Volumes/OZTURK/_projects/prose_generation/_commentary/v15')
import build, lib
SLM = '/Volumes/OZTURK/_projects/quran-slm'
loc = json.load(open(f'{SLM}/artifacts/surah_networks_global_ensemble/s001/catalog.json'))
A = np.load(f'{SLM}/artifacts/surah_networks_global_ensemble/s001/affinity.npy')
lk = {f"{b['root']} {b['branch_id']}": b['index'] for b in loc['branches']}
lroot = np.array([b['root'] for b in loc['branches']])
def lrank(a, b):
    row = A[a].copy(); row[lroot == lroot[a]] = -1
    return int((row > row[b]).sum()) + 1
mem = build.scene_members(lib.refs_of_surah(1))
for fr in ['travel.route', 'water.well', 'water.rain_cloud', 'water.gathered', 'water.thirst_drinking', 'pastoral.herding', 'travel.open_land', 'race.contest' ]:
    ms = mem.get(fr, [])
    nodes = {}
    for ref, surf, root, br, role, alt in ms:
        k = f"{root} {br}"
        nodes[k] = (role, alt, ref)
    print('\n==', fr, len(nodes), 'branches:', {k: v[0] + ('~alt' if v[1] else '') for k, v in nodes.items()})
    rks = []
    for a, b in itertools.combinations(nodes, 2):
        if a.split(' B')[0] == b.split(' B')[0]: continue
        if a in lk and b in lk:
            r1, r2 = lrank(lk[a], lk[b]), lrank(lk[b], lk[a])
            rks.append(min(r1, r2))
            print(f'   {a} ({nodes[a][0]}) <-> {b} ({nodes[b][0]}): local ranks {r1}/{r2}')
        else:
            print(f'   {a} <-> {b}: not in S1 local view (alt root)')
    if rks: print('   best-direction ranks: min', min(rks), 'median', np.median(rks), 'max', max(rks))
