"""Refinement of relay.py: per distinct (ayah, activated branch), which upstream source groups nominated it
(hft / channel / v12 / none) across the three lanes. Also: branches nominated upstream but never activated."""
import json, os, collections, sys
from multiprocessing import Pool
import lib
from relay import pick_dirs
GROUP = {'hft': 'hft', 'channel': 'channel', 'cross_run_publication': 'v12', 'v12_reader_walks': 'v12', 'v12_reader_walks_wide': 'v12'}

def one(args):
    ay, d = args
    ref = ay.replace('_', ':')
    nom = collections.defaultdict(set); act = collections.defaultdict(set)
    for l in lib.LANES:
        p = f'{d}/{l}.discovery.json'
        if not os.path.exists(p): continue
        disc = json.load(open(p)); pk = lib.load_packet(ref, l, d) or {}
        for c in pk.get('candidate_inventory', []):
            g = GROUP.get(c.get('source_type'), c.get('source_type'))
            for k in ('branch_refs', 'nominated_branch_refs', 'focus_branch_refs'):
                for b in c.get(k) or []: nom[b].add(g)
        for f in disc.get('findings', []):
            for a in f.get('branch_activations') or []:
                if isinstance(a, dict) and a.get('branch_ref'):
                    act[a['branch_ref']].add(a.get('application_mode'))
    return ref, {b: sorted(v) for b, v in nom.items()}, {b: sorted(v) for b, v in act.items()}

if __name__ == '__main__':
    dirs = pick_dirs()
    with Pool(8) as pool:
        R = pool.map(one, sorted(dirs.items()), chunksize=4)
    idx, roots = lib.dict_index()
    c = collections.Counter(); unact = collections.Counter(); own_kind = collections.Counter(); nom_kind=collections.Counter()
    for ref, nom, act in R:
        for b, modes in act.items():
            src = '+'.join(nom.get(b, [])) or 'none(own)'
            c[src] += 1
            if src == 'none(own)': own_kind[idx.get(b, {}).get('kind')] += 1
        for b, g in nom.items():
            if b not in act: unact['+'.join(g)] += 1
            nom_kind[idx.get(b, {}).get('kind')] += 1
    n_act = sum(c.values()); n_nom = sum(len(nom) for _, nom, _ in R)
    out = dict(n_ayat=len(R), distinct_ayah_branch_activated=n_act, by_nominating_source=dict(c.most_common()),
               own_share=round(c['none(own)'] / n_act, 4), own_by_branch_kind=dict(own_kind),
               distinct_ayah_branch_nominated=n_nom, nominated_not_activated=dict(unact.most_common()),
               nominated_not_activated_total=sum(unact.values()))
    json.dump(out, open(lib.W + '/out/relay2.json', 'w'), indent=1)
    print(json.dumps(out, indent=1))
