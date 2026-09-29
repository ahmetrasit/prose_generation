"""Second seeded sample: 24 'present' calls (collocation + non_bare), compact, for a precision hand check."""
import csv, json, random, collections
G = '/Volumes/OZTURK/_projects/prose_generation/_commentary/review/e0/guard/guard_calls.tsv'
TR = '/Volumes/OZTURK/_projects/quran-data/data/dictionary/tr'
W = collections.defaultdict(list)
for r in csv.DictReader(open('/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/words.tsv', encoding='utf-8'), delimiter='\t'):
    W[f"{r['surah']}:{r['ayah']}"].append((int(r['w']), r['surface']))
rows = [r for r in csv.DictReader(open(G, encoding='utf-8'), delimiter='\t') if r['call'] == 'present']
print('present calls by reason:', collections.Counter(r['reason'].split(';')[0] for r in rows).most_common())
rnd = random.Random(7)
pick = rnd.sample(rows, 24)
import sys
if len(sys.argv) > 1 and sys.argv[1] == 'lexeme':
    lx = [r for r in rows if r['reason'].startswith('lexeme') and r['root'] != 'ع ن د']
    print('lexeme present calls excluding ع ن د:', len(lx), 'branches:', len({r['branch_ref'] for r in lx}))
    pick = random.Random(11).sample(lx, 30)
cache = {}
def br(bref):
    rid = bref.split('/')[0]
    if rid not in cache:
        import glob
        fs = glob.glob(f'{TR}/{rid}_entry.json') or glob.glob(f'{TR}/*{rid}*_entry.json')
        cache[rid] = {b['branch_ref']: b for f in fs for b in json.load(open(f))['branches']}
    return cache[rid].get(bref, {})
out = []
for r in pick:
    b = br(r['branch_ref'])
    s, a, w = r['occurrence'].split(':'); w = int(w)
    ctx = ' '.join(x[1] if x[0] != w else f'[{x[1]}]' for x in W[f'{s}:{a}'] if abs(x[0] - w) <= 4)
    rec = dict(occ=r['occurrence'], bref=r['branch_ref'], root=r['root'], kind=r['branch_kind'], reason=r['reason'],
               matched=r['matched_statement'], image=b.get('branch_image_ar'), ctx=ctx)
    out.append(rec)
    print(f"{rec['occ']} | {rec['root']} {rec['bref'][-4:]} {rec['kind']} «{rec['image']}» | {rec['reason']} | stmt: {rec['matched']} | {ctx}")
json.dump(out, open('/Volumes/OZTURK/_projects/prose_generation/_commentary/review/e0/review/out/guard_present_sample' + ('_lexeme' if len(sys.argv) > 1 else '') + '.json', 'w'), ensure_ascii=False, indent=1)
