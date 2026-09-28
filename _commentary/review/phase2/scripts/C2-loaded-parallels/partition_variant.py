"""Variant partition for the known-dossier check: each ayah of the root goes to its most specific recurring partner
(same-ayah or attachment context only; highest IDF, then highest count); ayat without one stay alone.
Writes dossier_groups_v2/<key>.json for score_dossiers.py."""
import sys, json, os, collections
sys.dont_write_bytecode = True
sys.path.insert(0, '.')
import common as C
from loaded import Model
M = Model(with_constructions=False)
os.makedirs('dossier_groups_v2', exist_ok=True)
for key, root in (('حمء', 'ح م ء'), ('نفخ', 'ن ف خ'), ('عرش', 'ع ر ش'), ('ربب', 'ر ب ب'), ('صلو', 'ص ل و')):
    A = M.analyse(root)
    groups = collections.defaultdict(list)
    for r in A['refs']:
        cands = [x for x, wgt in A['ctxs'][r].items() if wgt == 1.0 and x in A['rec']]
        if cands:
            x = max(cands, key=lambda x: (C.idf_root(x), A['rec'][x]['k']))
            groups[x].append(r)
        else:
            groups['solo:' + r].append(r)
    gl = [dict(id=f'g{i + 1}', label=k, ids=[w['ref3'] for r in v for w in A['by_ref'][r]]) for i, (k, v) in enumerate(groups.items())]
    json.dump(dict(key=key, root=root, groups=gl, act=[], complete=True), open(f'dossier_groups_v2/{key}.json', 'w'), ensure_ascii=False, indent=1)
    print(key, {k: len(v) for k, v in groups.items() if not k.startswith('solo')}, 'solo', sum(1 for k in groups if k.startswith('solo')))
