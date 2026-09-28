#!/usr/bin/env python3
"""Feasibility of scoring a knowledge-gap probe by script: can an Arabic definition be mapped to the right branch of
its root by character 3-gram cosine alone? Proxy query = the branch's own what_is_ar (definition); candidates =
image_ar + phrase_ar of every branch of the same root (definition field excluded, so the query text is not in the
candidate). Reports top-1 / top-2 within-root accuracy against chance, by branch count. Optimistic proxy: real probe
answers are model paraphrases, not dictionary definitions."""
import csv, re, math
from collections import Counter, defaultdict
from pathlib import Path
csv.field_size_limit(10**9)
HERE = Path(__file__).resolve().parent
DI = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')
def fold(t): return re.sub(r'\s+', ' ', re.sub(r'[^ء-ي ]', ' ', DI.sub('', t or '').translate(str.maketrans('أإآٱىة', 'اااايه'))))
def grams(t):
    t = f' {fold(t)} '
    return Counter(t[i:i+3] for i in range(len(t) - 2))
def cos(a, b):
    num = sum(v * b.get(k, 0) for k, v in a.items())
    return num / (math.sqrt(sum(v*v for v in a.values())) * math.sqrt(sum(v*v for v in b.values())) or 1)
BY = defaultdict(list)
for r in csv.DictReader(open(HERE.parent / 'branches.tsv', encoding='utf-8'), delimiter='\t'):
    if int(r['root_words'] or 0) > 0 and r['what_is_ar'].strip():
        BY[r['root_id']].append(r)
t1 = t2 = n = 0; chance = 0.0; byk = defaultdict(Counter)
for rid, brs in BY.items():
    if len(brs) < 2: continue
    cand = [grams(b['image_ar'] + ' ' + re.sub(r'\([^)]*\)', ' ', b['phrase_ar'])) for b in brs]
    for i, b in enumerate(brs):
        q = grams(re.sub(r'^يدخل فيه', '', b['what_is_ar']))
        order = sorted(range(len(brs)), key=lambda j: -cos(q, cand[j]))
        n += 1; t1 += order[0] == i; t2 += i in order[:2]; chance += 1 / len(brs)
        k = '2-4' if len(brs) <= 4 else '5-9' if len(brs) <= 9 else '10+'
        byk[k]['n'] += 1; byk[k]['t1'] += order[0] == i; byk[k]['ch'] += 1 / len(brs)
print(f'branches {n}: top-1 {t1/n:.1%}, top-2 {t2/n:.1%}, chance top-1 {chance/n:.1%}')
for k in ('2-4', '5-9', '10+'):
    c = byk[k]; print(f'  roots with {k} branches: n={c["n"]} top-1 {c["t1"]/c["n"]:.1%} (chance {c["ch"]/c["n"]:.1%})')
