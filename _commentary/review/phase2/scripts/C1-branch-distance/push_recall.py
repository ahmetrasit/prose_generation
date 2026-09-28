"""How much of the independent gold does the harvest PUSH carry with paths (vs. listed without paths, vs. echo only)?
 - 29:38 cold-Opus link branches (v9 eval_29_38.py GOLD, 16 distinct branches)
 - S1 gold-ledger anchors at the Fatiha ayat where their root occurs (harvest2 pull files for 1:1-1:7)
Reads harvest2/*.pull.json only."""
import json, os, collections, sys
sys.dont_write_bytecode = True
H = os.path.dirname(os.path.abspath(__file__))
def load(s, a):
    p = os.path.join(H, 'harvest2', f'{s:03d}_{a:03d}.pull.json')
    return json.load(open(p)) if os.path.exists(p) else None
out = {}
g29 = {("ع و د", "B009"), ("ع م ل", "B011"), ("ص د د", "B004"), ("ص د د", "B013"), ("س ب ل", "B010"), ("ب ي ن", "B007"), ("ع م ل", "B010"),
       ("ز ي ن", "B001"), ("ش ط ن", "B005"), ("ش ط ن", "B003"), ("س ك ن", "B004"), ("ص د د", "B005"), ("ص د د", "B002"), ("س ب ل", "B005"),
       ("ش ط ن", "B001"), ("ع م ل", "B012")}
P = load(29, 38)
st = collections.Counter(); detail = []
for r in P['rows']:
    root, b = r['card'].rsplit(' ', 1)
    if (root, b) in g29:
        k = 'echo_only' if r['guard'] == 'absent' else ('pushed_with_paths' if r['pushed'] else 'listed_in_order_no_paths')
        st[k] += 1; detail.append((r['card'], r['image'], k))
out['29:38_gold_branches'] = dict(counts=dict(st), n=len(g29), detail=detail)
C_gold = [json.loads(l) for l in open('/Volumes/OZTURK/_projects/quran-slm/reports/s1_ar3_v1_gold_ledger.jsonl')]
cat = {c['node_id']: c for c in json.load(open('/Volumes/OZTURK/_projects/quran-slm/artifacts/corpus_network/catalog.json'))['cards']}
anchors = set()
for g in C_gold:
    if not g['eligibility']['eligible']: continue
    for n in g['required_branch_anchors'] + [x for grp in g['required_branch_anchor_groups'] for x in grp['node_ids']]:
        if n in cat: anchors.add(f"{cat[n]['surface_root_key'].replace('أ', 'ء')} {cat[n]['branch_id']}")
st1 = collections.Counter(); seen = {}
for a in range(1, 8):
    P = load(1, a)
    if not P: continue
    for r in P['rows']:
        if r['card'] in anchors:
            k = 'echo_only' if r['guard'] == 'absent' else ('pushed_with_paths' if r['pushed'] else 'listed_in_order_no_paths')
            # best status over the ayat where the anchor's root occurs
            rank = {'pushed_with_paths': 0, 'listed_in_order_no_paths': 1, 'echo_only': 2}
            if r['card'] not in seen or rank[k] < rank[seen[r['card']]]: seen[r['card']] = k
st1 = collections.Counter(seen.values())
out['S1_gold_anchors'] = dict(counts=dict(st1), n_anchors_found=len(seen), n_anchors=len(anchors),
                              not_pushed=[a for a, k in seen.items() if k != 'pushed_with_paths'])
print(json.dumps(out, ensure_ascii=False, indent=1))
json.dump(out, open(os.path.join(H, 'push_recall.json'), 'w'), ensure_ascii=False, indent=1)
