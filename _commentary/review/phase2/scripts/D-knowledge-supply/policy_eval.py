#!/usr/bin/env python3
"""Static knowledge-gap score, evaluated on the manual cold-arm labels (recall_manual.tsv), then applied to the whole
dictionary.

memory_score(branch) = [position B001-B003] + [>=4 of the 6 early sources] + [HFT+v12 activations >= 10]
  (0-3; higher = the model more likely reaches the sense unaided). Every branch keeps an index line whatever its
  score; the score only decides whether its definition + one early-source phrase are PUSHED (score <= PUSH_MAX) or
  left one read away. branch_kind collocation / non_bare always gets its construction note pushed (the guard).
Prints: cold recall by score; confusion of the push rule on the labels; share of the whole dictionary pushed."""
import csv
from collections import Counter, defaultdict
from pathlib import Path
csv.field_size_limit(10**9)
HERE = Path(__file__).resolve().parent
PUSH_MAX = 1


def score(idx, nsrc, act):
    return int(idx <= 3) + int(nsrc >= 4) + int(act >= 10)


L = [r for r in csv.DictReader(open(HERE / 'recall_manual.tsv', encoding='utf-8'), delimiter='\t') if r['plain'] == '0']
t = defaultdict(Counter)
for r in L:
    s = score(int(r['idx']), int(r['n_sources']), int(r['hft_any']) + int(r['v12']))
    r['score'] = s
    t[s]['n'] += 1; t[s]['cold'] += int(r['cold']); t[s]['fed_only'] += int(r['fed']) and not int(r['cold'])
print('score | latent branches | cold recalled | rate | fed-only (memory missed)')
for s in sorted(t):
    print(f'  {s}   | {t[s]["n"]:4} | {t[s]["cold"]:3} | {t[s]["cold"]/t[s]["n"]:.0%} | {t[s]["fed_only"]}')
push = [r for r in L if r['score'] <= PUSH_MAX]
keep = [r for r in L if r['score'] > PUSH_MAX]
print(f'\npush rule score<={PUSH_MAX}: pushes {len(push)} of {len(L)} latent branches ({len(push)/len(L):.0%}).')
print(f'  cold positives among pushed (redundant push): {sum(int(r["cold"]) for r in push)} of {sum(int(r["cold"]) for r in L)}')
print(f'  fed-only among NOT pushed (memory-likely but missed; still has its index line): '
      f'{sum(1 for r in keep if int(r["fed"]) and not int(r["cold"]))} of {sum(1 for r in L if int(r["fed"]) and not int(r["cold"]))}')
for r in keep:
    if int(r['fed']) and not int(r['cold']):
        print(f"     {r['ayah']:6} {r['branch']:10} score={r['score']} | {r['concept']}")
# pairwise ranking quality (AUC) of the score for cold recall
pos = [r['score'] for r in L if r['cold'] == '1']; neg = [r['score'] for r in L if r['cold'] == '0']
auc = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg) / (len(pos) * len(neg))
print(f'  AUC of memory_score for cold recall: {auc:.2f} (n+={len(pos)}, n-={len(neg)})')

# whole dictionary
B = [r for r in csv.DictReader(open(HERE.parent / 'branches.tsv', encoding='utf-8'), delimiter='\t')]
Q = [r for r in B if int(r['root_words'] or 0) > 0]
c = Counter(); ck = Counter()
for r in Q:
    s = score(int(r['idx']), int(r['n_sources']), int(r['hft_any']) + int(r['v12']))
    c[s] += 1
    if r['branch_kind'] in ('collocation', 'non_bare'):
        ck['guard'] += 1
print(f'\nwhole dictionary, Quranic roots: {len(Q)} branches; score distribution {dict(sorted(c.items()))}; '
      f'pushed (score<={PUSH_MAX}) {sum(v for k, v in c.items() if k <= PUSH_MAX)} ({sum(v for k, v in c.items() if k <= PUSH_MAX)/len(Q):.0%}); '
      f'construction-guard branches {ck["guard"]} ({ck["guard"]/len(Q):.0%})')
for ref in ('root_000672/B010', 'root_001069/B008', 'root_000848/B013', 'root_001273/B012', 'root_001444/B006', 'root_001444/B008',
            'root_000354/B001', 'root_001529/B001', 'root_000906/B002', 'root_001321/B003'):
    r = next((x for x in B if x['branch_ref'] == ref), None)
    if r:
        s = score(int(r['idx']), int(r['n_sources']), int(r['hft_any']) + int(r['v12']))
        print(f"  {ref} {r['root']} {r['branch']} {r['branch_kind'][:5]} score={s} -> "
              f"{'PUSH definition+phrase' if s <= PUSH_MAX else 'index line only'}"
              f"{' + construction' if r['branch_kind'] in ('collocation', 'non_bare') else ''} | {r['tr_concept'][:50]}")
