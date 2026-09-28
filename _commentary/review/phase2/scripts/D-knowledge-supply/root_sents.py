#!/usr/bin/env python3
"""Print the sentences of a reading that name a root (Arabic token with its radicals, or keyword regex), for manual
branch annotation. Usage: root_sents.py S_A arm 'ع ي ن' [extra_regex]"""
import re, sys
from pathlib import Path
sys.argv += [''] * 5
sa, arm, root, extra = sys.argv[1:5]
t = Path(f'/Volumes/OZTURK/_projects/prose_generation/_commentary/v9/lines/work/{sa}/synth/{arm}/{sa}.reading.tr.md').read_text()
DIAC = re.compile(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]')
MAP = str.maketrans({'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ى': 'ي', 'ة': 'ه', 'ؤ': 'و', 'ئ': 'ي'})
lets = [c.translate(MAP) for c in root.split()]
WEAK = set('اويء')
strong = [c for c in lets if c not in WEAK] or lets
def has(sent):
    for w in re.findall(r'[ء-يٱ-ۓؐ-ًؚ-ٰٟۖ-ۭـ]+', sent):
        w = DIAC.sub('', w).translate(MAP)
        i = 0
        for ch in w:
            if i < len(strong) and ch == strong[i]:
                i += 1
        if i == len(strong):
            return True
    return bool(extra) and re.search(extra, sent, re.I)
for s in re.split(r'(?<=[.!?])\s+|\n+', t):
    if s.strip() and has(s):
        print('-', re.sub(r'\{ar:([^,]*), tr:[^,]*, gloss:([^}]*)\}', r'[\1 = \2]', s.strip())[:400])
