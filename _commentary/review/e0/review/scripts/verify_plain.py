"""Verify [plain: ref] marks on every supply page against root-dossier activation_map.tsv (dominant rows)."""
import csv, re, glob, os, collections, json
AM = '/Volumes/OZTURK/_projects/root-dossier/out/activation_map.tsv'
OUT = '/Volumes/OZTURK/_projects/prose_generation/_commentary/review/e0/supply/out'
rows = list(csv.DictReader(open(AM), delimiter='\t'))
dom = collections.defaultdict(set)   # verse -> {(wordref, branch_ref)}
minor = collections.defaultdict(set)
for x in rows:
    if x['branch_ref'] in ('stop', ''):
        continue
    (dom if x['role'] == 'dominant' else minor)[x['verse_ref']].add((x['qac_word_ref'], x['branch_ref']))
res = {}
for p in sorted(glob.glob(OUT + '/*.md')):
    ref = os.path.basename(p)[:-3].replace('_', ':')
    txt = open(p, encoding='utf-8').read()
    # only B section
    b = txt.split('\n## B.')[1].split('\n## C.')[0]
    marks = set()
    for m in re.finditer(r'^- (root_\d+(?:--root_\d+)?/B\d+) \[plain: ([^\]]+)\]', b, re.M):
        for w in m.group(2).split(','):
            marks.add((w.strip(), m.group(1)))
    # also any [plain elsewhere in the page (C..I)
    other = len(re.findall(r'\[plain', txt.split('\n## C.')[1])) if '\n## C.' in txt else 0
    exp = dom.get(ref, set())
    res[ref] = dict(marks=len(marks), expected=len(exp), missing=sorted(exp - marks), extra=sorted(marks - exp),
                    minor_marked=sorted(marks & minor.get(ref, set())), plain_mentions_outside_B=other)
for k, v in res.items():
    print(k, v['marks'], v['expected'], 'missing', v['missing'][:6], 'extra', v['extra'][:6], 'outsideB', v['plain_mentions_outside_B'])
json.dump(res, open('/Volumes/OZTURK/_projects/prose_generation/_commentary/review/e0/review/out/verify_plain.json', 'w'), indent=1, ensure_ascii=False)
