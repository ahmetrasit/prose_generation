import csv, json, sys
csv.field_size_limit(10**9)
p = sys.argv[1]
rows = list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
print(len(rows), 'rows')
n = 0
for r in rows:
    ev = json.loads(r['evidence'])
    cids = sorted({e.get('connection_id') for e in ev})
    n += len(cids)
    notes = ' || '.join(sorted({e['note'][:220] for e in ev}))
    print(f"{r['ref']} | {r['tier']} | {r['tradition']} | {r['kinds']} | {r['basis'][:80]} | {','.join(cids)}")
    if len(sys.argv) > 2:
        print('    ', notes)
print('total cids', n)
