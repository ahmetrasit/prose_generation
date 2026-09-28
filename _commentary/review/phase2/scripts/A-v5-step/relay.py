"""How much of v5's harvest is relay (HFT / channel / v12 / word-topic candidates) vs Luna's own?
Over all v5 discovery files (numbered ayat, non-basmala, one analysis per ayah).
Per activation: application_mode; the origin candidate's kind/source; whether the activated branch was nominated
by ANY candidate in that lane packet (branch_refs/nominated_branch_refs/focus_branch_refs) -> 'nominated' vs 'own'.
Also the dictionary branch_kind of each activated branch, and whether it is the root's B001."""
import json, os, glob, re, collections, sys
from multiprocessing import Pool
import lib

BASE = lib.V5 + '/raw'


def pick_dirs():
    by = {}
    for p in glob.glob(BASE + '/*/*/*/macro.discovery.json'):
        d = os.path.dirname(p)
        aid, sur, ay = d[len(BASE) + 1:].split('/')
        if 'basmala' in aid or aid.startswith('s029') or ay.endswith('_0'):
            continue
        by.setdefault(ay, []).append(d)
    return {ay: sorted(ds)[0] for ay, ds in by.items()}


def one(args):
    ay, d = args
    ref = ay.replace('_', ':')
    res = collections.Counter()
    per_branch = {}
    for l in lib.LANES:
        p = f'{d}/{l}.discovery.json'
        if not os.path.exists(p):
            continue
        disc = json.load(open(p))
        pk = lib.load_packet(ref, l, d)
        cands = {c['candidate_id']: c for c in (pk or {}).get('candidate_inventory', [])}
        nominated = set()
        for c in cands.values():
            for k in ('branch_refs', 'nominated_branch_refs', 'focus_branch_refs'):
                nominated |= set(c.get(k) or [])
        for f in disc.get('findings', []):
            oc = f.get('origin_candidate_id')
            ck = cands.get(oc, {}).get('kind') if oc else 'uncandidate'
            if oc and ck is None:
                ck = 'unknown'
            res[(l, 'finding_origin', ck)] += 1
            for a in f.get('branch_activations') or []:
                if not isinstance(a, dict) or not a.get('branch_ref'):
                    continue
                b = a['branch_ref']
                m = a.get('application_mode')
                nom = 'nominated' if b in nominated else 'own'
                res[(l, 'act_mode', m)] += 1
                res[(l, 'act_nom', nom)] += 1
                res[(l, 'act_origin', ck)] += 1
                key = b
                pb = per_branch.setdefault(key, set())
                pb.add((l, m, nom, ck))
    return ref, res, {b: list(v) for b, v in per_branch.items()}


if __name__ == '__main__':
    dirs = pick_dirs()
    print('ayat', len(dirs), file=sys.stderr)
    with Pool(8) as pool:
        results = pool.map(one, sorted(dirs.items()), chunksize=4)
    idx, roots = lib.dict_index()
    tot = collections.Counter()
    # distinct (ayah, branch) classification
    ab = collections.Counter()
    ab_kind = collections.Counter()
    ab_b001 = collections.Counter()
    for ref, res, pb in results:
        tot.update(res)
        for b, lst in pb.items():
            modes = {x[1] for x in lst}
            noms = {x[2] for x in lst}
            if modes == {'attributed'}:
                cls = 'attributed_only'
            elif 'attributed' in modes:
                cls = 'attributed_and_own_mode'
            else:
                cls = 'no_attributed'
            cls2 = 'own_only' if noms == {'own'} else ('nominated_only' if noms == {'nominated'} else 'both')
            ab[(cls, cls2)] += 1
            k = idx.get(b, {}).get('kind') or 'missing'
            ab_kind[(k, cls2)] += 1
            ab_b001[('B001' if b.endswith('/B001') else 'other', cls2)] += 1
    out = dict(n_ayat=len(results),
               totals={'|'.join(map(str, k)): v for k, v in sorted(tot.items())},
               ayah_branch={'|'.join(k): v for k, v in sorted(ab.items())},
               ayah_branch_kind={'|'.join(k): v for k, v in sorted(ab_kind.items())},
               ayah_branch_b001={'|'.join(k): v for k, v in sorted(ab_b001.items())})
    json.dump(out, open(lib.W + '/out/relay.json', 'w'), indent=1)
    json.dump({ref: pb for ref, res, pb in results}, open(lib.W + '/cache/per_branch.json', 'w'))
    print(json.dumps(out, indent=1))
