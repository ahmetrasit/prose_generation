import csv, json, sys, collections
csv.field_size_limit(10**9)
P = '/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/discovery/s103-20261009/103_3.merged.tsv'
rows = list(csv.DictReader(open(P), delimiter='\t'))
mode = sys.argv[1] if len(sys.argv) > 1 else 'compact'
ids = collections.OrderedDict()
for i, r in enumerate(rows):
    ev = json.loads(r['evidence'])
    for e in ev:
        cid = e['connection_id']
        ids.setdefault(cid, []).append((i, r['ref'], e))
if mode == 'count':
    print('rows', len(rows), 'ids', len(ids))
    c = collections.Counter(r['tradition'] for r in rows)
    print(c)
    c = collections.Counter(r['tier'] for r in rows)
    print(c)
elif mode == 'compact':
    lo = int(sys.argv[2]); hi = int(sys.argv[3])
    for i, r in enumerate(rows[lo:hi], lo):
        ev = json.loads(r['evidence'])
        print(f"#{i} {r['ref']} | {r['tier']} | {r['tradition']} | {r['kinds']}")
        for e in ev:
            print(f"   {e['connection_id']} [{e['model']},{e['strength']},{e['kind']}] ref={e['ref']} :: {e['basis']} :: {e['note'][:260]}")
