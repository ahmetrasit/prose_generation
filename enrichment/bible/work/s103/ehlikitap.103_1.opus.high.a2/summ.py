import csv, json, sys
csv.field_size_limit(10**9)
p = '/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/discovery/s103-20261009/103_1.merged.tsv'
mode = sys.argv[1] if len(sys.argv) > 1 else 'short'
rows = list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
ids = set()
for i, r in enumerate(rows):
    ev = json.loads(r['evidence'])
    cids = sorted(set(e.get('connection_id') for e in ev))
    ids.update(cids)
    if mode == 'short':
        print(i, '|', r['ref'], '|', r['tier'], '|', r['tradition'], '|', r['kinds'], '|', r['basis'][:90], '|', len(cids))
    elif mode == 'ids':
        for e in ev:
            print(e.get('connection_id'), '|', r['ref'], '|', e.get('kind'), '|', e.get('strength'), '|', e.get('model'), '|', (e.get('note') or '')[:160])
print('rows', len(rows), 'distinct ids', len(ids), file=sys.stderr)
