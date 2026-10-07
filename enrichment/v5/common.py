#!/usr/bin/env python3
"""Shared paths, routes, rates and read-only corpus access for enrichment v5.

v5 separates discovery, reading and writing:
  packet  a script gathers every roster segment tied to the page's verses (no model);
  extract cheap fresh-context readers quote the relevant passages verbatim, per chunk;
  write   one writer per family turns the page plus extracts into Turkish blocks;
  search  families the verse index cannot serve keep keyword discovery, plus memory leads.
Nothing here launches a model or writes to the corpus.
"""
import json
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V5 = ROOT / 'enrichment/v5'
DB = ROOT / 'enrichment/corpus/corpus.sqlite'
OVERLAY = V5 / 'index/range_overlay.jsonl'
sys.path.insert(0, str(ROOT / 'enrichment/v3'))
import pilot  # noqa: E402  (paragraph splitter shared with v3/v4)
from memory_assemble import FAMILIES  # noqa: E402  (family -> Turkish section title)

# Frozen inputs byte-identical to the v3/v4 benchmarks, so v5 results compare directly.
FROZEN = {
    '1_6': ROOT / 'enrichment/v4/work/1_6/corpus-sol-max-20261006/frozen.reading.tr.md',
    '87_6': ROOT / 'enrichment/v4/work/87_6/corpus-sol-max-20261006/frozen.reading.tr.md',
    '100_1': ROOT / 'enrichment/v4/work/100_1/corpus-sol-max-20261007/frozen.reading.tr.md',
}
# Source rosters and availability (v4); v5 applies TRANSLATION_OK on top.
ROSTERS = ROOT / 'enrichment/v4/work/1_6/corpus-sol-max-20261006'

# Routes. Verse-indexed families get packets; the others keep keyword discovery.
SEARCH = {'hadith', 'poetry', 'rhetoric', 'wujuh', 'academic', 'modern-coherence'}
# Indexed, but the 1:6/87:6 index held only 25-60% of what the benchmark agents cited.
PACKET_PLUS_SEARCH = {'bayani', 'qiraat', 'historical'}
DIRECT_MAX_TOKENS = 60_000      # a writer reads packets up to this size itself
# Luna's window is ~258k; the user caps an extractor's whole context at 120k tokens (2026-10-06).
# Measured on the first Luna max run (100:1 rivayet c04, 61k chars): peak request 114k tokens, because the
# verbatim quotes it writes come back into context (output ~ input) and max reasoning stays in context.
# Peak ~ 37k + 2 x chunk tokens, so chunks <= 80k chars keep the peak near 90k.
CHUNK_CHARS = 40_000            # one fresh extractor context per chunk (c01 at 70k chars still reached 114k)
CONTEXT_CAP = 120_000
PART_CHARS = 10_000             # one helper delivery; Codex clips longer command output (v4's size; read with 12,000 output tokens)

# Sources excluded in v4 only for being translations: usable in v5, labelled.
TRANSLATION_OK = {
    'ISLAHI-TADABBUR': 'English translation (Kayani et al.); the Urdu original is not held. '
                       'Quote it as the translation and never present its wording as Islahi\'s Urdu.',
}

# Standard API-equivalent rates per million tokens (saved benchmark basis):
# input, cached input, cache write, output. Sol has a long-context tier above 272k.
RATES = {
    'gpt-6-sol': (2.0, 0.2, 2.5, 10.0),
    'gpt-6-luna': (0.1, 0.01, 0.125, 0.5),
    'gpt-6-astra': (10.0, 1.0, 12.5, 50.0),
}
# Claude subagents are costed from their transcript by _commentary/v16/agentrun.py (its RATES).
SOL_LONG = (4.0, 0.4, 5.0, 15.0)
LONG_CONTEXT = 272_000


def connect():
    return sqlite3.connect(f'file:{DB}?mode=ro', uri=True)


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def rows(path):
    return [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]


def write_rows(path, items):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in items))


def tokens(chars):
    """Rough estimate for Arabic/Turkish/English mixed text; reported as an estimate."""
    return chars // 3


def page(unit):
    """Frozen text and {paragraph: (start, end)} using the v3 splitter."""
    pilot.BASE = FROZEN[unit]
    return pilot.prose()


VERSE = re.compile(r'(?<!\d)(\d{1,3}):(\d{1,3})(?:\s*[–-]\s*(\d{1,3}))?(?![\d:])')


def verses_by_paragraph(unit):
    """Verse references each frozen paragraph cites, plus the target ayah and its neighbours."""
    text, paragraphs = page(unit)
    s, a = map(int, unit.split('_'))
    target = {(s, x) for x in (a - 1, a, a + 1) if x >= 1}
    out = {}
    for p, (lo, hi) in paragraphs.items():
        found = set(target)
        for m in VERSE.finditer(text[lo:hi]):
            su, start = int(m[1]), int(m[2])
            end = int(m[3]) if m[3] else start
            if 1 <= su <= 114 and start <= end <= start + 40:
                found |= {(su, x) for x in range(start, end + 1)}
        out[p] = found
    return out


def sources(family):
    """v4 roster metadata with the v5 translation rule applied."""
    config = json.loads((ROSTERS / family / 'sources.json').read_text())
    for src in config['sources']:
        if src['id'] in TRANSLATION_OK and src['segments']:
            src['usable'] = True
            src['translation'] = TRANSLATION_OK[src['id']]
            src['limitation'] = TRANSLATION_OK[src['id']]
    return config


def usable(config):
    return [s['id'] for s in config['sources'] if s['usable']]


def body(row, family):
    """Full segment text with source flags; meal also carries its en/tr parallel text."""
    _, _, _, text, extra = row
    extra = json.loads(extra or '{}')
    details = {k: v for k, v in extra.items() if k not in ('en', 'tr')}
    parts = [text or '']
    if details:
        parts.append('CORPUS SOURCE NOTES / FLAGS: ' + json.dumps(details, ensure_ascii=False))
    if family == 'meal':
        for key in ('en', 'tr'):
            if extra.get(key):
                value = extra[key]
                parts.append(key + ': ' + (value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)))
    return '\n\n'.join(parts)


def compact(value):
    return re.sub(r'\s+', ' ', value or '').strip()


def normalized(text):
    """Loose comparison form: no Arabic vowel marks or tatweel, unified alef/ya/ta marbuta."""
    text = unicodedata.normalize('NFKC', text or '')
    text = re.sub(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]', '', text)
    text = text.translate(str.maketrans({'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ى': 'ي', 'ة': 'ه'}))
    return re.sub(r'\s+', ' ', text).strip().lower()


def contains(haystack, needle, minimum=8):
    """Exact phrase check after whitespace compaction (v4 rule), with a vowel-insensitive fallback."""
    if len(needle.strip()) < minimum:
        return False
    return compact(needle) in compact(haystack) or normalized(needle) in normalized(haystack)
