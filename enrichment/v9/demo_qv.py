"""Demo query over t2whole-103_1 tier-2 views. qv.py VERSE [REGEX] [--holders]"""
import json, re, sys
from collections import defaultdict
T = '/Volumes/aro/projects/prose_generation/enrichment/v7/work/t2whole-103_1-20261008/tier2'
args = [a for a in sys.argv[1:] if not a.startswith('--')]
v, pat = args[0], (args[1] if len(args) > 1 else None)
hold = '--holders' in sys.argv
k = v.replace(':', '-')
import os
if not os.path.exists(f'{T}/rows/{k}.json'): T = T.replace('t2whole-103_1-20261008', 't2whole-test-20261008')
rows = json.load(open(f'{T}/rows/{k}.json'))
for i, l in enumerate(open(f'{T}/out/sol-high/{k}.s1.jsonl'), 1):
    d = json.loads(l)
    text = ' '.join(d['words']) + ' ' + d['view'] + ' ' + d.get('note', '')
    if pat and not re.search(pat, text, re.I):
        continue
    print(f"v{i:03d} [{d['type']}] {' '.join(d['words'])[:40]} | {d['view']}" + (f" (note: {d['note']})" if d.get('note') else '') + f" | n={len(d['rows'])}")
    if hold:
        h = defaultdict(set)
        for r in d['rows']:
            x = rows.get(r)
            if x:
                h[x['src']].add(('' if x['speaker'] == 'author' else x['speaker']) + {'prefers': '+', 'rejects': '-'}.get(x['stance'], ''))
        print('      ', '; '.join(s + ('(' + ','.join(sorted(y for y in sp if y)) + ')' if any(sp) else '') for s, sp in sorted(h.items(), key=lambda kv: min(rows[r]['death'] or 9999 for r in d['rows'] if rows.get(r) and rows[r]['src'] == kv[0]))))
