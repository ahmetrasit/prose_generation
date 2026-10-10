import json, csv, sys
csv.field_size_limit(10**9)
d = json.load(open(sys.argv[1]))
rows = list(csv.DictReader(open(sys.argv[2], encoding='utf-8'), delimiter='\t'))
refs = {r['ref'] for r in rows}
for c in d['candidates']:
    if c['ref'] in refs and not c['ref'].startswith(('WLC:', 'SBLGNT:')):
        print(json.dumps(c, ensure_ascii=False))
print('missing among page refs:', [m for m in d['missing'] if m in refs])
