import csv, json, sys
csv.field_size_limit(10**9)
base = '/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/discovery/s103-20261009/'
rows = list(csv.DictReader(open(base + '103_1.merged.tsv'), delimiter='\t'))
n = 0
for i, r in enumerate(rows):
    ev = json.loads(r['evidence'])
    cids = sorted({e['connection_id'] for e in ev})
    n += len(cids)
    print(f"{i}\t{r['ref']}\t{r['tier']}\t{r['tradition']}\t{r['kinds']}\t{r['basis'][:90]}\t{' '.join(c[3:9] for c in cids)}")
    if len(cids) > 1 or len(ev) > 1:
        for e in ev:
            print(f"    - {e['model']} {e['connection_id']} {e['kind']} {e['basis'][:80]}")
print('total cids', n, file=sys.stderr)
m = json.load(open(base + '103_1.merged.json'))
for f in m['findings']:
    for x in f['validation']['findings']:
        print('FINDING', f['model'], json.dumps(x, ensure_ascii=False)[:300])
print('CONF', json.dumps(m['confidence'], ensure_ascii=False)[:3000])
