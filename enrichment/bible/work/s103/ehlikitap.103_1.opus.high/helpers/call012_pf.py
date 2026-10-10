import json
p = json.load(open('/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/discovery/s103-20261009/prefetch.json'))
print(type(p), list(p.keys()) if isinstance(p, dict) else len(p))
for k, v in p.items():
    if isinstance(v, list):
        print(k, len(v))
        if v:
            print('  sample', json.dumps(v[0], ensure_ascii=False)[:600])
    else:
        print(k, json.dumps(v, ensure_ascii=False)[:600])
names = ["Ta'anit 23a", "Glory of the Martyrs", "Genesis Rabbah 89", "Berakhot 4:1", "Berakhot 26b", "Tertullian", "Avot", "Didache", "Wisdom of Solomon", "Protevangelium", "Maccabees 2", "Sirach 4", "Tobit 4"]
s = json.dumps(p, ensure_ascii=False)
items = []
for k, v in p.items():
    if isinstance(v, list):
        for x in v:
            items.append((k, x))
for k, x in items:
    js = json.dumps(x, ensure_ascii=False)
    if any(n in js for n in names) and ('103:1' in js or '103_1' in js or 'target' not in js):
        print(k, js[:500])
