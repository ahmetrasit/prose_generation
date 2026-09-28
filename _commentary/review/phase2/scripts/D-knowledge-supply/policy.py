#!/usr/bin/env python3
"""Per-branch supply policy (script only, no model): for every dictionary branch decide how it is PUSHED.

Every branch of every root of the ayah always gets one index line (id | Arabic image | short Turkish gloss) - nothing
is dropped. The policy only decides what is added to that line:
  memory_likely  : the model is likely to reach the sense unaided. Signals (any):
                   - plain sense of some Quranic occurrence (HFT baseline step >0 or root-dossier dominant >0),
                   - the branch's early-source phrases quote the Quran (a 3-token Quran sequence, normalised),
                   - B001 of its root (the lexicographers' lead sense; a weak, order-based signal, reported separately).
  push_phrase    : NOT memory_likely -> add one quotable classical phrase (shortest early-source segment with its tag).
  guard          : branch_kind collocation / non_bare -> add the construction marker (the scope note's construction and
                   the source phrase), whatever the other flags say (memory folds constructions into roots too).
Outputs policy.tsv (one row per branch) and prints class sizes. Evaluation against recall labels is in policy_eval.py."""
import sys, re
sys.path.insert(0, __import__('os').path.dirname(__file__))
from common import *
Q = quran()
# Quran 3-token shingles (folded)
tri = set()
for t in Q.values():
    w = fold(t).split()
    for i in range(len(w) - 2):
        tri.add((w[i], w[i + 1], w[i + 2]))
def qcite(phrase):
    w = fold(phrase).split()
    return any((w[i], w[i + 1], w[i + 2]) in tri for i in range(len(w) - 2))
def shortest_segment(phrase):
    segs = [s.strip() for s in re.split(r'؛|;', phrase) if s.strip()]
    segs = [s for s in segs if len(fold(s).split()) >= 2] or segs
    return min(segs, key=len) if segs else ''
rows = branches()
out = []
for r in rows:
    base, dom = int(r['hft_base']), int(r['dossier_dominant'])
    qc = qcite(r['phrase_ar'])
    q_attested = base > 0 or dom > 0 or qc
    lead = r['branch'] == 'B001'
    mem = q_attested or lead
    guard = r['branch_kind'] in ('collocation', 'non_bare')
    out.append({**{k: r[k] for k in ('branch_ref', 'root', 'branch', 'branch_kind', 'n_sources', 'root_words', 'hft_any', 'hft_base',
                                     'v12', 'channel', 'dossier_dominant')},
                'qcite': int(qc), 'q_attested': int(q_attested), 'lead': int(lead), 'memory_likely': int(mem),
                'push_phrase': int(not mem), 'guard': int(guard), 'never_activated': int(int(r['hft_any']) + int(r['v12']) == 0),
                'phrase_short': shortest_segment(r['phrase_ar']).replace('\t', ' ')[:160]})
cols = list(out[0].keys())
with open(HERE / 'policy.tsv', 'w', encoding='utf-8') as fh:
    fh.write('\t'.join(cols) + '\n')
    for o in out:
        fh.write('\t'.join(str(o[c]) for c in cols) + '\n')
q = [o for o in out if int(o['root_words'] or 0) > 0]
print('branches', len(out), 'Quranic-root branches', len(q))
for k in ('qcite', 'q_attested', 'memory_likely', 'push_phrase', 'guard', 'never_activated'):
    print(f'  {k}: {sum(o[k] for o in q)} ({sum(o[k] for o in q)/len(q):.1%})')
print('  push_phrase & guard:', sum(1 for o in q if o['push_phrase'] and o['guard']))
