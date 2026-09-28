#!/usr/bin/env python3
"""Test (3): the instruction confound behind the 'bulk input dilutes synthesis' lesson.

(a) Lists every evidence/permission clause the w10 arms saw: the per-arm evidence clause in v9/lines/synth.py and the
    evidence-restricting sentences of the shared brief write_v10.md; the same for write_v11.md (v11 arms).
(b) Groups the Phase 1 metrics rows (review/phase1/scripts/dilution/metrics.tsv) by input x permission:
      COLD        context only; clause grants 'your own knowledge of Arabic and the Quran'
      FED-NOPERM  dictionary / dhft / dslim / ledger / full package; clause lists files only + 'Work only from the
                  supplied evidence'
      FED-PERM    v11 brief on context + dictionary + digest/slim (v9 v11-script, v11-luna; v11/out): 'The Quran
                  itself, from the files and from your own knowledge of the whole Quran'; lexical memory only as
                  [recall] in the ledger
    and compares, ayah by ayah, other-surah refs, same-surah refs, thinking tokens and billed input.
(c) Rank correlation of billed input with other-surah refs inside each permission group (does size matter once the
    permission is fixed?).
Writes confound.tsv and prints the tables."""
import csv, re, statistics
from collections import defaultdict
from pathlib import Path
csv.field_size_limit(10**9)
PG = Path('/Volumes/OZTURK/_projects/prose_generation')
M = PG / '_commentary/review/phase1/scripts/dilution/metrics.tsv'
HERE = Path(__file__).resolve().parent

# ---------- (a) clauses
syn = (PG / '_commentary/v9/lines/synth.py').read_text(encoding='utf-8')
w10 = (PG / '_commentary/v9/prompts/write_v10.md').read_text(encoding='utf-8')
w11 = (PG / '_commentary/v9/prompts/write_v11.md').read_text(encoding='utf-8')
print('== (a) evidence clauses')
m = re.search(r'evidence = \((.*?)\n    prompt', syn, re.S)
clauses = re.findall(r'"([^"]*)"', m.group(1))
print(' synth.py evidence expression: %d string pieces; "own knowledge" appears %d time(s) (cold branch only)'
      % (len(clauses), ''.join(clauses).count('own knowledge')))
joined = re.sub(r'"\s*\n\s*"', '', m.group(1))
for part in re.split(r'\bif (?:cold|dic|dslim|dhft) else', joined):
    print('   clause:', re.sub(r'\s+', ' ', part).strip()[:260])
def sentences(t):
    return [s.strip() for s in re.split(r'(?<=[.;])\s+', re.sub(r'\s*\n\s*', ' ', t)) if s.strip()]
PAT = re.compile(r'supplied|evidence|only from|invent|memory|own knowledge|concordance|canonical text|present for', re.I)
for name, t in (('write_v10.md', w10), ('write_v11.md', w11)):
    hits = [s for s in sentences(t) if PAT.search(s)]
    print(f' {name}: {len(sentences(t))} sentences, {len(hits)} evidence-related:')
    for s in hits:
        tag = ('RESTRICT' if re.search(r'only from|Work only|Copy Quran Arabic from the supplied|Dictionary senses only', s)
               else 'PERMIT' if re.search(r'own knowledge|from memory', s, re.I)
               else 'NO-INVENT' if re.search(r'invent', s, re.I) else 'OTHER')
        print(f'   [{tag}] {s[:230]}')

# ---------- (b) groups
rows = list(csv.DictReader(open(M, encoding='utf-8'), delimiter='\t'))
def grp(run):
    if run in ('v9:w10-opus-cold', 'v9:w10-opus-cold2'):
        return 'COLD'
    if run in ('v9:w10-opus-dict', 'v9:w10-opus-dhft', 'v9:w10-opus-dslim', 'v9:w10-opus-ledger', 'v9:w10-opus'):
        return 'FED-NOPERM'
    if run in ('v9:v11-script', 'v9:v11-luna', 'v11:out'):
        return 'FED-PERM'
    return None
def num(x):
    try:
        return float(str(x).split()[0])
    except Exception:
        return None
data = []
for r in rows:
    g = grp(r['run'])
    if not g or not r.get('words'):
        continue
    data.append({'ayah': r['ayah'], 'run': r['run'], 'group': g, 'billed_in': num(r['billed_input_total']),
                 'thinking': num(r['thinking_tokens']), 'other': num(r['other_surah_refs']),
                 'same': num(r['same_surah_refs']), 'words': num(r['words']), 'recall_marks': num(r['recall_marks'])})
with open(HERE / 'confound.tsv', 'w', encoding='utf-8') as fh:
    cols = list(data[0])
    fh.write('\t'.join(cols) + '\n')
    for d in data:
        fh.write('\t'.join(str(d[c]) for c in cols) + '\n')
print('\n== (b) per group (runs with a reading)')
by = defaultdict(list)
for d in data:
    by[d['group']].append(d)
for g in ('COLD', 'FED-NOPERM', 'FED-PERM'):
    L = by[g]
    oth = [d['other'] for d in L]; sam = [d['same'] for d in L]; bi = [d['billed_in'] for d in L if d['billed_in']]
    th = [d['thinking'] for d in L if d['thinking']]
    print(f' {g:11} n={len(L):2}  other-surah refs median {statistics.median(oth):5.1f} (min {min(oth):.0f}, max {max(oth):.0f}; '
          f'zero in {sum(1 for x in oth if x == 0)})  same-surah median {statistics.median(sam):4.1f}  '
          f'billed input median {statistics.median(bi):8.0f} (max {max(bi):.0f})  thinking median {statistics.median(th):7.0f}')
print('\n== (b2) matched ayat: COLD vs FED-NOPERM vs FED-PERM, other-surah refs (billed input tokens)')
ay = sorted({d['ayah'] for d in data}, key=lambda x: tuple(int(p) for p in x.split(':')))
matched = 0
for a in ay:
    cells = []
    for g in ('COLD', 'FED-NOPERM', 'FED-PERM'):
        L = [d for d in by[g] if d['ayah'] == a]
        cells.append(', '.join(f"{d['run'].split(':')[1].replace('w10-opus-', '').replace('w10-opus', 'package')}={d['other']:.0f}"
                               f"({(d['billed_in'] or 0)/1000:.0f}k)" for d in L) or '-')
    if cells[0] != '-' and (cells[1] != '-' or cells[2] != '-'):
        matched += 1
    print(f' {a:7} COLD: {cells[0]:32} | NOPERM: {cells[1]:70} | PERM: {cells[2]}')

# ---------- (c) size vs outside reach within a permission group
def spearman(x, y):
    def rank(v):
        s = sorted(range(len(v)), key=lambda i: v[i]); r = [0] * len(v); i = 0
        while i < len(s):
            j = i
            while j + 1 < len(s) and v[s[j + 1]] == v[s[i]]:
                j += 1
            for k in range(i, j + 1):
                r[s[k]] = (i + j) / 2
            i = j + 1
        return r
    rx, ry = rank(x), rank(y); mx, my = statistics.mean(rx), statistics.mean(ry)
    num_ = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return num_ / den if den else float('nan')
print('\n== (c) Spearman(billed input, other-surah refs) inside each group')
for g in ('FED-NOPERM', 'FED-PERM'):
    L = [d for d in by[g] if d['billed_in']]
    print(f' {g}: n={len(L)} rho={spearman([d["billed_in"] for d in L], [d["other"] for d in L]):.2f}')
allfed = [d for d in by['FED-NOPERM'] + by['FED-PERM'] if d['billed_in']]
perm = [1 if d['group'] == 'FED-PERM' else 0 for d in allfed]
print(f' all fed runs: n={len(allfed)} rho(input, other)={spearman([d["billed_in"] for d in allfed], [d["other"] for d in allfed]):.2f}; '
      f'rho(permission, other)={spearman(perm, [d["other"] for d in allfed]):.2f}')
print('\n== (d) thinking vs input, all three groups (Spearman)')
L = [d for d in data if d['billed_in'] and d['thinking']]
print(f' n={len(L)} rho(billed input, thinking)={spearman([d["billed_in"] for d in L], [d["thinking"] for d in L]):.2f}')
for lo, hi in ((0, 50e3), (50e3, 150e3), (150e3, 1e9)):
    S = [d['thinking'] for d in L if lo <= d['billed_in'] < hi]
    if S:
        print(f'  billed input {lo/1000:.0f}-{hi/1000:.0f}k: n={len(S)} thinking median {statistics.median(S):.0f}')
