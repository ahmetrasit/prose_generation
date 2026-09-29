"""Seeded sample of guard detector calls with the dictionary's own statements, for hand checking."""
import csv, json, random, re, collections
G = '/Volumes/OZTURK/_projects/prose_generation/_commentary/review/e0/guard/guard_calls.tsv'
TR = '/Volumes/OZTURK/_projects/quran-data/data/dictionary/tr'
Q = {r['ref']: r['text'] for r in csv.DictReader(open('/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/quran.tsv', encoding='utf-8'), delimiter='\t')}
rows = list(csv.DictReader(open(G, encoding='utf-8'), delimiter='\t'))
rnd = random.Random(20260928)
pick = []
for call, k in (('present', 4), ('absent', 3), ('unknown', 3)):
    pool = [r for r in rows if r['call'] == call and r['branch_kind'] == 'collocation']
    pick += rnd.sample(pool, k)
cache = {}
def branch(bref):
    rid, bid = bref.split('/')
    if rid not in cache:
        cache[rid] = json.load(open(f'{TR}/{rid}_entry.json'))
    for b in cache[rid]['branches']:
        if b['branch_ref'] == bref:
            return b
out = []
for r in pick:
    b = branch(r['branch_ref'])
    ls = b.get('lexicalization_scope') or {}
    s, a, w = r['occurrence'].split(':')
    rec = dict(occ=r['occurrence'], surface=r['surface'], bref=r['branch_ref'], root=r['root'], kind=r['branch_kind'],
               call=r['call'], reason=r['reason'], matched=r['matched_statement'], image=b.get('branch_image_ar'),
               what_is=b.get('what_is_ar'), phrase=b.get('source_phrase_ar'), scope=ls.get('note'),
               lex_units=[u.get('expression_ar') for u in (b.get('lexical_units') or []) if isinstance(u, dict)][:6],
               ayah=Q[f'{s}:{a}'])
    out.append(rec)
    print(json.dumps(rec, ensure_ascii=False)); print()
json.dump(out, open('/Volumes/OZTURK/_projects/prose_generation/_commentary/review/e0/review/out/guard_sample.json', 'w'), ensure_ascii=False, indent=1)
