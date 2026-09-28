#!/usr/bin/env python3
"""Reuse the inter-ayah memory-only suggestions (rows after the first 100 retrieval-ranked rows of each
quran-data/data/analysis/inter-ayah/focus_*_cutoff_100.tsv) as a free probe of Quran-parallel recall (GPT runs).

Question: does memory recall LEXICAL partners (same root, esp. low-frequency roots = the loaded-word concordance)
or THEMATIC partners? For every memory row: does the target share a content root with the focus (any root; a root
with <= 60 uses; a root with <= 30 uses)? Compared with the retrieval rows (first 100) and with a random baseline
(random ayah pairs). Also the watch-case partners: are they among memory rows or retrieval rows, and with what grade?
Writes nothing but prints; interayah_probe.txt holds the output."""
import csv, glob, os, random, re, sys
from collections import Counter, defaultdict
csv.field_size_limit(10**9)
V15 = '/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data'
IA = '/Volumes/OZTURK/_projects/quran-data/data/analysis/inter-ayah'
roots = defaultdict(set)
uses = Counter()
for r in csv.DictReader(open(f'{V15}/words.tsv', encoding='utf-8'), delimiter='\t'):
    for rt in r['roots'].split('|'):
        if rt:
            roots[f"{r['surah']}:{r['ayah']}"].add(rt)
            uses[rt] += 1
GEN = {rt for rt, n in uses.items() if n > 1500}   # الله, قول, كون ... excluded from 'any'
def shared(a, b, maxuse=None):
    s = (roots.get(a, set()) & roots.get(b, set())) - GEN
    if maxuse:
        s = {x for x in s if uses[x] <= maxuse}
    return bool(s)
stat = {k: Counter() for k in ('retrieval', 'memory', 'random')}
grades = {k: Counter() for k in ('retrieval', 'memory')}
allrefs = list(roots)
random.seed(15)
WATCH = {'18:86': ['15:26', '15:28', '15:33'], '18:96': ['15:29', '38:72', '32:9', '3:49', '5:110', '21:91', '66:12'],
         '29:38': ['29:41'], '5:6': ['5:97', '5:8', '5:95'], '4:34': ['4:128', '4:135']}
watch_out = []
files = glob.glob(f'{IA}/focus_*_cutoff_100.tsv')
for f in files:
    m = re.search(r'focus_(\d+)_(\d+)_cutoff', f)
    focus = f'{m.group(1)}:{m.group(2)}'
    rows = [l.rstrip('\n').split('\t') for l in open(f, encoding='utf-8') if l.strip()]
    for i, r in enumerate(rows):
        if len(r) < 3:
            continue
        grade, tgt = r[0].strip(), r[1].strip()
        if not re.fullmatch(r'\d+:\d+', tgt):
            continue
        k = 'retrieval' if i < 100 else 'memory'
        stat[k]['n'] += 1
        stat[k]['any'] += shared(focus, tgt)
        stat[k]['le60'] += shared(focus, tgt, 60)
        stat[k]['le30'] += shared(focus, tgt, 30)
        stat[k]['same_surah'] += tgt.split(':')[0] == focus.split(':')[0]
        grades[k][grade] += 1
        if focus in WATCH and tgt in WATCH[focus]:
            watch_out.append(f'  {focus} -> {tgt}: {k} row {i + 1}, grade "{grade}": {r[2][:150]}')
    for _ in range(20):
        tgt = random.choice(allrefs)
        stat['random']['n'] += 1
        stat['random']['any'] += shared(focus, tgt)
        stat['random']['le60'] += shared(focus, tgt, 60)
        stat['random']['le30'] += shared(focus, tgt, 30)
print(f'files {len(files)}')
for k, c in stat.items():
    n = c['n']
    print(f"{k:9} rows {n:7}: share a content root {c['any']/n:.1%}; share a root with <=60 uses {c['le60']/n:.2%}; "
          f"<=30 uses {c['le30']/n:.2%}" + (f"; same surah {c['same_surah']/n:.1%}" if k != 'random' else ''))
for k, g in grades.items():
    print(k, 'grades:', dict(g.most_common(6)))
print('watch-case partners found:')
print('\n'.join(watch_out) or '  none')
for focus, ts in WATCH.items():
    got = {w.split('-> ')[1].split(':')[0] + ':' + w.split('-> ')[1].split(':')[1] for w in watch_out if w.strip().startswith(focus + ' ')}
    miss = [t for t in ts if t not in got]
    print(f'  {focus}: absent from both retrieval and memory rows: {miss}')
