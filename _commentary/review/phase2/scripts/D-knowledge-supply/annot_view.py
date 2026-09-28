#!/usr/bin/env python3
"""Print, for manual annotation, a root's branches (id, kind, sources, activation history, Turkish concept, Arabic image)
and every sentence of the given reading(s) that names the root (Arabic radicals in order, a transliteration, or an extra
regex). Usage: annot_view.py S_A 'r o o t' arm1,arm2 [extra_regex]"""
import csv, re, sys, subprocess
from pathlib import Path
csv.field_size_limit(10**9)
HERE = Path(__file__).resolve().parent
B = [r for r in csv.DictReader(open(HERE.parent / 'branches.tsv', encoding='utf-8'), delimiter='\t')]
sa, root, arms = sys.argv[1], sys.argv[2], sys.argv[3].split(',')
extra = sys.argv[4] if len(sys.argv) > 4 else ''
rows = [r for r in B if r['root'] == root]
rid = {r['root_id'] for r in rows}
print(f'### {sa} {root} {sorted(rid)} words={rows[0]["root_words"] if rows else "?"}')
for r in rows:
    print(f"  {r['branch']} {r['branch_kind'][:5]:5} src{r['n_sources']} hft{r['hft_any']:>4} base{r['hft_base']:>3} v12 {r['v12']:>3} ch{r['channel']:>3} dom{r['dossier_dominant']:>3} | {r['tr_concept'][:60]} | {r['image_ar'][:40]}")
for arm in arms:
    print(f'--- {arm}')
    out = subprocess.run(['python3', str(HERE.parent / 'root_sents.py'), sa, arm, root, extra], capture_output=True, text=True)
    print(out.stdout[:6000] or out.stderr[:500])
