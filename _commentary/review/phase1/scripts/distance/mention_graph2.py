#!/usr/bin/env python3
"""Read-only prototype check: a 'mentioned-object' signal. Each branch card's Arabic text
(image + definition + classical phrases) is tokenised; a token that equals an undiacritised
Quranic lemma (with or without the article) of ANOTHER root is a mention of that root.
Two cards are linked when they mention the same root (IDF-weighted), or when one mentions the
other's root. Measures coverage and how the S1 gold-ledger / Luna scene pairs fare.
"""
import csv, re, json, math, collections, itertools, glob
import numpy as np
csv.field_size_limit(10**9)
V15 = '/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data'
SLM = '/Volumes/OZTURK/_projects/quran-slm'
DIAC = re.compile(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]')
def norm(t):
    t = DIAC.sub('', t)
    t = t.replace('ٱ', 'ا').replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا').replace('ى', 'ي').replace('ة', 'ه')
    return t
lem2roots = collections.defaultdict(set)
for r in csv.DictReader(open(f'{V15}/lemmas.tsv', encoding='utf-8'), delimiter='\t'):
    f = norm(r['lemma'])
    if f.startswith('ال'): f = f[2:]
    if len(f) >= 3:
        lem2roots[f].add(r['root'])
print('lemma forms', len(lem2roots))
cards = list(csv.DictReader(open(f'{SLM}/resources/source/corpus_branches_ar.tsv', encoding='utf-8'), delimiter='\t'))
TOK = re.compile(r'[ء-يٱ]+')
def mentions(c):
    txt = norm(' '.join([c['branch_image_ar'], c['what_is_ar'], c['source_phrase_ar']]))
    out = set()
    for w in TOK.findall(txt):
        for cand in (w, w[2:] if w.startswith('ال') else None, w[1:] if w[:1] in 'وفبلك' else None,
                     w[3:] if w[:3] in ('وال', 'فال', 'بال', 'كال') else None, w[2:] if w.startswith('لل') else None):
            if cand and len(cand) >= 3 and cand in lem2roots:
                out |= lem2roots[cand]
    out.discard(c['surface_root_key'])
    return out
M = {c['node_id']: mentions(c) for c in cards}
root_of = {c['node_id']: c['surface_root_key'] for c in cards}
df = collections.Counter(r for v in M.values() for r in v)
STOP = {r for r, k in df.items() if k > 400}
M = {k: v - STOP for k, v in M.items()}
n = len(cards)
cov = sum(1 for v in M.values() if v)
print('cards', n, 'cards mentioning >=1 other Quranic root', cov, f'({cov/n:.3f})', 'median mentioned roots', np.median([len(v) for v in M.values()]))
print('most mentioned roots', df.most_common(12))

def score(a, b):
    shared = (M[a] & M[b]) - {root_of[a], root_of[b]}
    s = sum(math.log(n / df[r]) for r in shared)
    direct = (root_of[b] in M[a]) or (root_of[a] in M[b])
    return s, direct, sorted(shared, key=lambda r: df[r])[:4]

gold = [json.loads(l) for l in open(f'{SLM}/reports/s1_ar3_v1_gold_ledger.jsonl')]
rows = json.load(open('gold_ranks.json'))
key = {c['display_key']: c['node_id'] for c in json.load(open(f'{SLM}/artifacts/corpus_network/catalog.json'))['cards']}
# rank of the mention score inside S1 local view
loc = json.load(open(f'{SLM}/artifacts/surah_networks_global_ensemble/s001/catalog.json'))
lnodes = [b['node_id'] for b in loc['branches']]
def mrank(a, b):
    sa = {x: score(a, x)[0] + (3.0 if score(a, x)[1] else 0) for x in lnodes if root_of[x] != root_of[a]}
    v = sa[b]
    return sum(1 for x in sa.values() if x > v) + 0.5 * (sum(1 for x in sa.values() if x == v) - 1) + 1, v
print('\nS1 gold pairs: slm local rank vs mention-graph local rank (score) and shared mentions')
out = []
for x in rows:
    if not x['elig']: continue
    a, b = key[x['a']], key[x['b']]
    s, d, sh = score(a, b)
    r1, v1 = mrank(a, b); r2, v2 = mrank(b, a)
    out.append((x['g'], x['a'], x['b'], min(x['local']), min(r1, r2), round(max(v1, v2), 2), d, sh))
for o in out: print(o)
sl = np.array([o[3] for o in out]); ml = np.array([o[4] for o in out])
print('pairs', len(out), 'slm median', np.median(sl), 'mention median', np.median(ml), 'slm<=10', (sl <= 10).sum(), 'mention<=10', (ml <= 10).sum(),
      'either<=10', ((sl <= 10) | (ml <= 10)).sum(), 'pairs with zero mention score', sum(1 for o in out if o[5] == 0))
