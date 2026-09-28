"""Surah-level chain index from the stored v5 harvest (for the one-call surah coalition step).
For each branch activated in >=2 ayat of the surah: the ayat whose own words carry the root (carrier ayat) and
the ayat where the branch was activated through context only (relay ayat). Grouped by root; plain B001 of frequent
roots dropped (they are the ground, not chains). Size measured; channel review size measured alongside."""
import json, collections, sys, os
import lib
PB = json.load(open(lib.W + '/cache/per_branch.json'))
idx, roots = lib.dict_index(); rmap = lib.root_ar_map()
conc = lib.concordance()
root_ayat = {r: {a for a, *_ in occ} for r, occ in conc.items()}

def index(s):
    ays = sorted([r for r in PB if r.split(':')[0] == str(s)], key=lib.refkey)
    act = collections.defaultdict(set)
    for a in ays:
        for b in PB[a]: act[b].add(a)
    L = [f"# chain index S{s} ({len(ays)} ayat in v5)"]
    byroot = collections.defaultdict(list)
    for b, aa in act.items():
        if len(aa) < 2: continue
        rid = b.split('/')[0]; rn = rmap.get(rid, rid)
        if b.endswith('/B001') and len(root_ayat.get(rn, ())) > 80: continue
        car = sorted([a for a in aa if a in root_ayat.get(rn, set())], key=lib.refkey)
        rel = sorted([a for a in aa if a not in root_ayat.get(rn, set())], key=lib.refkey)
        byroot[rn].append((b, car, rel))
    for rn in sorted(byroot, key=lambda r: -sum(len(c) + len(x) for _, c, x in byroot[r])):
        for b, car, rel in sorted(byroot[rn]):
            di = idx.get(b, {})
            L.append(f"- {rn} {b.split('/')[1]} [{di.get('kind')}] {di.get('gloss')} | words in: {','.join(a.split(':')[1] for a in car) or '-'} | via context: {','.join(a.split(':')[1] for a in rel) or '-'}")
    return '\n'.join(L)

if __name__ == '__main__':
    print('surah\tayat\tindex_bytes\tindex_tok(0.451/byte)\tchannel_review_bytes\tchannel_tok')
    for s in (sys.argv[1:] or ['1', '18', '100', '12', '103']):
        t = index(int(s))
        open(f'{lib.W}/out/chain_index_s{int(s):03d}.txt', 'w').write(t)
        p = f'/Volumes/OZTURK/_projects/quran-data/data/analysis/channels/network-v3/s{int(s):03d}/review/reader_a_pilot.md'
        cb = os.path.getsize(p) if os.path.exists(p) else 0
        n = len([r for r in PB if r.split(':')[0] == s])
        print(s, n, len(t.encode()), int(0.451 * len(t.encode())), cb, int(0.451 * cb), sep='\t')
