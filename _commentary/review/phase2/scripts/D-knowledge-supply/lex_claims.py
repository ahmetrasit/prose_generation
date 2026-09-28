#!/usr/bin/env python3
"""Extract lexical-claim sentences from the v9 cold arms (memory only) for manual branch annotation.
A sentence is a lexical claim when it names a root/word family or the lexicographers ("kök", "sözlük", "Arap",
"denir", "anlamı", "türev", transliterated root like d-r-b) or carries a non-Quran Arabic tag.
Usage: lex_claims.py [arm]   (default w10-opus-cold). Writes lex_claims_<arm>.txt next to this script."""
import re, sys
from pathlib import Path
V9 = Path('/Volumes/OZTURK/_projects/prose_generation/_commentary/v9/lines/work')
QURAN = Path('/Volumes/OZTURK/_projects/quran-data/data/text/quran-uthmani.tsv')
arm = sys.argv[1] if len(sys.argv) > 1 else 'w10-opus-cold'
DIAC = re.compile(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]')
MAP = str.maketrans({'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ى': 'ي', 'ة': 'ه', 'ؤ': 'و', 'ئ': 'ي'})
def fold(s):
    return re.sub(r'[^ء-ي ]', '', DIAC.sub('', s).translate(MAP))
QT = ' '.join(fold(l.split('|', 2)[-1]) for l in QURAN.read_text(encoding='utf-8').splitlines() if '|' in l)
QT = re.sub(r'\s+', ' ', QT)
CUE = re.compile(r"\bkök|sözlük|Arap|denir|anlam|türev|kelime|sözcük|lügat|dilci|\b[a-zçşğıöüḍṣṭẓḥʿ']{1,3}-[a-zçşğıöüḍṣṭẓḥʿ']{1,3}-[a-zçşğıöüḍṣṭẓḥʿ']{1,3}\b", re.I)
TAG = re.compile(r'\{\{?ar:([^,}]*)')
out = []
for d in sorted(V9.iterdir()):
    f = d / 'synth' / arm / f'{d.name}.reading.tr.md'
    if not f.exists():
        continue
    text = f.read_text(encoding='utf-8')
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+|\n+', text) if s.strip()]
    out.append(f'\n######## {d.name} ({len(text.split())} words)')
    for i, s in enumerate(sents):
        tags = TAG.findall(s)
        nonq = [t for t in tags if fold(t).strip() and fold(t).strip() not in QT]
        if CUE.search(s) or nonq:
            s2 = re.sub(r'\{\{?ar:([^,]*), tr:([^,]*), gloss:([^}]*)\}\}?', r'[\1 | \3]', s)
            out.append(f'{i:03d} {"NONQ " if nonq else ""}{s2[:600]}')
p = Path(__file__).with_name(f'lex_claims_{arm}.txt')
p.write_text('\n'.join(out), encoding='utf-8')
print(p, sum(1 for l in out if not l.startswith('\n')), 'lines')
