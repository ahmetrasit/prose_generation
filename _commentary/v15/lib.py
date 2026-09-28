"""v15 shared paths and loaders.

Reads raw sources (Quran text, QAC root/lemma table, Furuq branch table, Turkish
dictionary entries, qira'at, pericopes, inter-ayah lists) and the tables that
build.py derives from them under data/. Never reads earlier pipeline packets.
"""
import csv
import glob
import json
import os
import re
from collections import defaultdict
from functools import lru_cache

csv.field_size_limit(10**9)

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
PROJECTS = os.path.abspath(os.path.join(REPO, '..'))
DATA = os.path.join(HERE, 'data')
WORK = os.path.join(HERE, 'work')
OUT = os.path.join(HERE, 'out')
PROMPTS = os.path.join(HERE, 'prompts')
SCHEMAS = os.path.join(HERE, 'schemas')

with open(os.path.join(HERE, 'config.json'), encoding='utf-8') as _f:
    CFG = json.load(_f)


def src(key, **fmt):
    """Absolute path of a raw source named in config.json."""
    return os.path.join(PROJECTS, CFG['sources'][key].format(**fmt))


def read_tsv(path):
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def write_tsv(path, rows, fields):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, '') for k in fields})


def write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def write_json(path, obj):
    write_text(path, json.dumps(obj, ensure_ascii=False, indent=1) + '\n')


def read_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


# ---------------------------------------------------------------- text

DIACRITICS = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')


def skeleton(ar):
    """Consonantal skeleton for matching: no diacritics, unified alifs/hamza seats."""
    s = DIACRITICS.sub('', ar)
    s = re.sub('[ٱأإآا]', 'ا', s)
    s = s.replace('ى', 'ي').replace('ة', 'ه')
    return s


@lru_cache(maxsize=1)
def quran():
    """'S:A' -> Uthmani text (S:0 prefatory basmalah records skipped)."""
    out = {}
    with open(src('quran_text'), encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n').replace('﻿', '')
            if '|' not in line:
                continue
            ref, text = line.split('|', 1)
            s, a = ref.split(':')
            if a == '0':
                continue
            out[ref] = text.strip()
    return out


# standalone pause/section marks (ۖ ۗ ۘ ۙ ۚ ۛ ۜ ۞ ۩) are not words; QAC word indices skip them
MARK_TOKEN = re.compile('^[ۖ-ۭ۞۩]+$')


@lru_cache(maxsize=None)
def tokens(ref):
    """Words of an ayah in QAC word-index order (pause marks dropped)."""
    return [t for t in quran()[ref].split() if not MARK_TOKEN.match(t)]


@lru_cache(maxsize=None)
def surah_len(s):
    n = 0
    while f'{s}:{n + 1}' in quran():
        n += 1
    return n


def refs_of_surah(s):
    return [f'{s}:{a}' for a in range(1, surah_len(s) + 1)]


def parse_ref(ref):
    parts = [int(x) for x in ref.split(':')]
    return parts


@lru_cache(maxsize=1)
def pericopes():
    """surah -> list of (from, to, label); surahs without records are one window."""
    out = defaultdict(list)
    with open(src('pericopes'), encoding='utf-8') as f:
        for line in f:
            if line.strip():
                p = json.loads(line)
                out[p['surah']].append((p['ayah_from'], p['ayah_to'], p.get('label', '')))
    return out


def windows_of_surah(s):
    """Window units for the window pass: whole surah if short or unsplit, else pericopes."""
    n = surah_len(s)
    per = pericopes().get(s)
    if n <= CFG['windows']['short_surah_max_ayat'] or not per:
        return [(1, n, 'whole surah')]
    return sorted(per)


def window_of_ayah(s, a):
    for lo, hi, label in windows_of_surah(s):
        if lo <= a <= hi:
            return lo, hi, label
    return 1, surah_len(s), 'whole surah'


def local_range(s, a, radius=None):
    r = CFG['windows']['local_radius'] if radius is None else radius
    return max(1, a - r), min(surah_len(s), a + r)


# ---------------------------------------------------------------- derived tables (build.py base)

@lru_cache(maxsize=1)
def words():
    """'S:A' -> list of word dicts (w, surface, roots, lemmas, pos). Built by build.py base."""
    out = defaultdict(list)
    for r in read_tsv(os.path.join(DATA, 'words.tsv')):
        out[f"{r['surah']}:{r['ayah']}"].append(r)
    return out


@lru_cache(maxsize=1)
def branches():
    """root -> list of branch dicts. Built by build.py base."""
    out = defaultdict(list)
    for r in read_tsv(os.path.join(DATA, 'branches.tsv')):
        out[r['root']].append(r)
    return out


@lru_cache(maxsize=1)
def branch_by_key():
    return {f"{r['root']} {r['branch']}": r for rs in branches().values() for r in rs}


@lru_cache(maxsize=1)
def root_by_id():
    """'root_000123' -> Arabic root with spaces."""
    return {r['root_id']: r['root'] for rs in branches().values() for r in rs}


@lru_cache(maxsize=1)
def lemmas():
    """(root, lemma) -> list of 'S:A:W'. Built by build.py base."""
    out = {}
    for r in read_tsv(os.path.join(DATA, 'lemmas.tsv')):
        out[(r['root'], r['lemma'])] = r['refs'].split(';') if r['refs'] else []
    return out


def kwic(word_ref, n=None):
    """The word (marked) with n words either side."""
    n = CFG['concordance']['kwic_context_words'] if n is None else n
    s, a, w = parse_ref(word_ref)
    toks = tokens(f'{s}:{a}')
    i = w - 1
    left = toks[max(0, i - n):i]
    right = toks[i + 1:i + 1 + n]
    pre = '… ' if i - n > 0 else ''
    post = ' …' if i + 1 + n < len(toks) else ''
    return f"{pre}{' '.join(left)} ⟦{toks[i] if i < len(toks) else '?'}⟧ {' '.join(right)}{post}".replace('  ', ' ').strip()


# ---------------------------------------------------------------- other raw sources

@lru_cache(maxsize=1)
def qiraat():
    """'S:A:W' -> list of variant dicts."""
    out = defaultdict(list)
    for r in read_tsv(src('qiraat')):
        out[r['tsv_word_ref']].append(r)
    return out


def inter_ayah(ref):
    """Earlier GPT relation lists for an ayah: (strength, target, note)."""
    s, a = ref.split(':')
    p = os.path.join(src('inter_ayah_dir'), f'focus_{s}_{a}_cutoff_100.tsv')
    if not os.path.exists(p):
        return []
    out = []
    with open(p, encoding='utf-8') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t')
            if len(parts) >= 3:
                out.append((parts[0], parts[1], parts[2]))
    return out


@lru_cache(maxsize=1)
def documented_alternatives():
    """(root_join_key, lemma or ref) -> list of alternative Arabic roots."""
    d = read_json(src('root_alternatives'))
    out = defaultdict(list)
    for rec in d.get('records', []):
        sel = rec['selector']
        key = (sel.get('qacRootJoinKey'), sel.get('qacLemma') or sel.get('qacRef'))
        for an in rec.get('analyses', []):
            if an.get('standing') != 'primary' and an.get('rootArabic'):
                out[key].append(' '.join(an['rootArabic'].replace(' ', '')))
    return out


# letter pairs that canonical readings exchange at a root position (ibdal)
SUBSTITUTIONS = {'ص': 'سز', 'س': 'صز', 'ز': 'صس', 'ط': 'ت', 'ت': 'ط', 'ض': 'ظ', 'ظ': 'ض'}


def alternative_roots(word_ref, root, lemma, surface):
    """Roots the word may also be heard from: documented alternatives + qira'at letter exchanges."""
    alts = []
    join = root.replace(' ', '')
    s, a, w = word_ref.split(':')
    for key in ((join, lemma), (join, f'{s}:{a}:{w}:1'), (join, f'{s}:{a}:{w}')):
        for r in documented_alternatives().get(key, []):
            if r != root and r not in [x for x, _ in alts]:
                alts.append((r, 'documented alternative analysis'))
    canon = skeleton(surface)
    for v in qiraat().get(word_ref, []):
        var = skeleton(v['qiraat_arabic'])
        letters = root.split()
        for i, L in enumerate(letters):
            for M in SUBSTITUTIONS.get(L, ''):
                if M in var and var.count(L) < canon.count(L):
                    cand = ' '.join(letters[:i] + [M] + letters[i + 1:])
                    if cand in branches() and cand != root and cand not in [x for x, _ in alts]:
                        alts.append((cand, f"reading {v['qiraat_transliteration']} ({v['qiraat_reader_set']})"))
    return alts


# ---------------------------------------------------------------- Luna-built tables (optional until built)

def _jsonl_items(pattern):
    for p in sorted(glob.glob(pattern)):
        with open(p, encoding='utf-8') as f:
            try:
                d = json.load(f)
            except json.JSONDecodeError:
                continue
        for it in d.get('items', []):
            yield it


@lru_cache(maxsize=1)
def inventory_ids():
    return {f['id'] for f in read_json(os.path.join(DATA, 'frames_inventory.json'))['frames']}


def normalize_frame(fid):
    """Map a slipped id (e.g. weather.rain_cloud) to the inventory id with the same name, if unique."""
    inv = inventory_ids()
    if fid in inv or fid.startswith('new.'):
        return fid
    same = [i for i in inv if i.split('.', 1)[1] == fid.split('.', 1)[-1]]
    return same[0] if len(same) == 1 else fid


@lru_cache(maxsize=1)
def frames():
    """'root Bnnn' -> list of (frame, role). From Luna frame jobs under data/frames/out/."""
    out = defaultdict(list)
    for it in _jsonl_items(os.path.join(DATA, 'frames', 'out', '*.json')):
        for fr in it.get('frames', []):
            out[it['key']].append((normalize_frame(fr['frame']), fr['role']))
    return out


@lru_cache(maxsize=1)
def new_frames():
    """Scenes Luna added when the inventory had none: id -> {scene, roles} (first description wins)."""
    out = {}
    for it in _jsonl_items(os.path.join(DATA, 'frames', 'out', '*.json')):
        for nf in it.get('new_frames', []):
            out.setdefault(nf['id'], {'scene': nf.get('scene', ''), 'roles': nf.get('roles', [])})
    return out


@lru_cache(maxsize=1)
def loanword_cards():
    """'root|lemma' -> card. From Luna loanword jobs under data/loanwords/out/."""
    out = {}
    for it in _jsonl_items(os.path.join(DATA, 'loanwords', 'out', '*.json')):
        out[f"{it['root']}|{it['lemma']}"] = it
    return out


@lru_cache(maxsize=1)
def profiles():
    """'root|lemma' -> use profile. From Luna profile jobs under data/profiles/out/."""
    out = {}
    for it in _jsonl_items(os.path.join(DATA, 'profiles', 'out', '*.json')):
        out[f"{it['root']}|{it['lemma']}"] = it
    return out
