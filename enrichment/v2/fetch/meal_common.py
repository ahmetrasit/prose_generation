"""Shared helpers for fetch_meal.py: polite HTTP, Qur'an geometry, text normalisation,
verse-group handling, and writing corpus source directories (see enrichment/corpus/README.md)."""
import gzip
import hashlib
import html
import json
import os
import re
import sys
import threading
import time
import unicodedata
from difflib import SequenceMatcher

import requests

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CORPUS = os.path.join(ROOT, 'enrichment', 'corpus')
FETCH_DIR = os.path.dirname(os.path.abspath(__file__))

AYAH_COUNTS = [7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
               112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53, 89,
               59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 12, 12, 30,
               52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 19, 36, 25, 22, 17, 19, 26, 30, 20, 15,
               21, 11, 8, 8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6]
assert len(AYAH_COUNTS) == 114 and sum(AYAH_COUNTS) == 6236
TOTAL_AYAT = 6236
PRIORITY = [1, 22] + list(range(87, 115))

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) research-corpus-fetch/1.0 (non-commercial; polite: <=2 req, >=0.35s)'


def log(*a):
    print(time.strftime('%H:%M:%S'), *a, file=sys.stderr, flush=True)


def parse_surahs(spec):
    """'1,22,87-114' | 'all' | 'priority' -> sorted list of surah numbers."""
    if not spec or spec == 'all':
        return list(range(1, 115))
    out = set()
    for part in spec.split(','):
        part = part.strip()
        if part == 'priority':
            out.update(PRIORITY)
        elif '-' in part:
            a, b = part.split('-')
            out.update(range(int(a), int(b) + 1))
        elif part:
            out.add(int(part))
    return sorted(s for s in out if 1 <= s <= 114)


def order_surahs(surahs):
    """Priority surahs first, then the rest in order."""
    pri = [s for s in PRIORITY if s in surahs]
    return pri + [s for s in surahs if s not in pri]


def all_ayat(surahs):
    return [(s, a) for s in surahs for a in range(1, AYAH_COUNTS[s - 1] + 1)]


# ---------------------------------------------------------------- HTTP

class Blocked(Exception):
    """Host answered with a challenge / login wall. We never try to get around it."""


class Host:
    """Per-host politeness: <= max_conc concurrent requests, >= min_gap s between request starts,
    retries with exponential backoff; a challenge page stops the host."""

    def __init__(self, name, min_gap=0.35, max_conc=2, timeout=60, encoding='utf-8'):
        self.name = name
        self.encoding = encoding
        self.min_gap = min_gap
        self.sem = threading.Semaphore(max_conc)
        self.lock = threading.Lock()
        self.last = 0.0
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': UA, 'Accept-Language': 'tr,en;q=0.8'})
        self.blocked = False
        self.n = 0

    def _wait(self):
        with self.lock:
            now = time.time()
            wait = self.last + self.min_gap - now
            if wait > 0:
                time.sleep(wait)
            self.last = time.time()

    def get(self, url, validate=None, tries=6, binary=False):
        if self.blocked:
            raise Blocked(self.name)
        delay = 2.0
        last_err = None
        for attempt in range(tries):
            with self.sem:
                self._wait()
                try:
                    r = self.session.get(url, timeout=self.timeout)
                    self.n += 1
                except requests.RequestException as e:
                    last_err = repr(e)
                    r = None
            if r is not None:
                body = r.content
                low = body[:4000].decode('utf-8', 'replace').lower()
                if r.status_code in (403, 503) and ('just a moment' in low or 'cf-chl' in low or 'captcha' in low):
                    self.blocked = True
                    raise Blocked(f'{self.name}: challenge page at {url}')
                if r.status_code == 200:
                    if binary:
                        return body
                    text = body.decode(self.encoding, 'replace')
                    if 'just a moment' in text[:3000].lower() and 'cloudflare' in text.lower():
                        self.blocked = True
                        raise Blocked(f'{self.name}: challenge page at {url}')
                    if validate is None or validate(text):
                        return text
                    last_err = 'validation failed'
                elif r.status_code == 404:
                    return None
                else:
                    last_err = f'HTTP {r.status_code}'
            log(f'[{self.name}] retry {attempt + 1}/{tries} {url}: {last_err}')
            time.sleep(delay)
            delay = min(delay * 2, 120)
        raise RuntimeError(f'{self.name}: giving up on {url}: {last_err}')


# ---------------------------------------------------------------- files

def write_gz(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with gzip.open(tmp, 'wt', encoding='utf-8') as f:
        f.write(text)
    os.replace(tmp, path)


def read_gz(path):
    with gzip.open(path, 'rt', encoding='utf-8') as f:
        return f.read()


def write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        f.write(text)
    os.replace(tmp, path)


def write_bytes(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'wb') as f:
        f.write(data)
    os.replace(tmp, path)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def src_dir(sid):
    return os.path.join(CORPUS, sid)


# ---------------------------------------------------------------- text

_WS = re.compile(r'[ \t\r\f\v      ]+')


def clean(text):
    """Whitespace + HTML entities only. Brackets, quotes, apostrophes and markers stay as published."""
    if text is None:
        return ''
    t = html.unescape(text)
    t = t.replace('\u200b', '').replace('\ufeff', '').replace('\u00ad', '')
    t = re.sub(r'\s*\n\s*', ' ', t)
    t = _WS.sub(' ', t)
    return t.strip()


def html_to_paras(fragment):
    """HTML -> clean text keeping paragraph breaks (blank line between paragraphs)."""
    if not fragment or fragment == '\\N':
        return ''
    t = re.sub(r'(?i)<br\s*/?>', '\n', fragment)
    t = re.sub(r'(?i)</p\s*>|</div\s*>|</li\s*>|</h\d\s*>', '\n\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t).replace('\u00a0', ' ').replace('\ufeff', '').replace('\u00ad', '').replace('\u200b', '')
    paras = []
    for p in re.split(r'\n\s*\n', t):
        p = re.sub(r'[ \t]*\n[ \t]*', ' ', p)
        p = _WS.sub(' ', p).strip()
        if p:
            paras.append(p)
    return '\n\n'.join(paras)


_TR_LOWER = str.maketrans({'I': 'ı', 'İ': 'i'})
_MARKERS = re.compile(r'\[\s*[\d⁰¹²³⁴⁵⁶⁷⁸⁹*]+\s*\]|\(\s*\d{1,4}\s*\)|[⁰¹²³⁴⁵⁶⁷⁸⁹]+|\*+')


def norm_cmp(text):
    """Loose form for cross-host comparison: no footnote markers, no diacritics, no punctuation,
    lower case (Turkish dotted/dotless i folded), single spaces."""
    t = _MARKERS.sub(' ', text or '')
    t = re.sub(r"[’‘'`´ʼ‛]", '', t)
    t = t.translate(_TR_LOWER).lower()
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = t.replace('ı', 'i')
    t = re.sub(r"[’‘'`´ʼ‛]", '', t)
    t = re.sub(r'[^\w\s]', ' ', t)
    return ' '.join(t.split())


def norm_ws(text):
    return ' '.join((text or '').split())


def sim(a, b):
    return SequenceMatcher(None, a, b, autojunk=False).ratio()


def bracket_sig(text):
    return (text.count('['), text.count('('))


# ---------------------------------------------------------------- Arabic (for the merge exception)

_AR = None


def arabic():
    """{(s,a): consonantal Arabic}; tanzil simple-clean kept next to this script."""
    global _AR
    if _AR is None:
        path = os.path.join(FETCH_DIR, 'meal_quran_simple_clean.txt')
        _AR = {}
        if os.path.exists(path):
            for line in open(path, encoding='utf-8'):
                p = line.rstrip('\n').split('|', 2)
                if len(p) == 3 and p[0].isdigit():
                    _AR[(int(p[0]), int(p[1]))] = re.sub(r'[^ء-ي ]', '', p[2])
    return _AR


def arabic_twins(s, a):
    """True when ayah a and a+1 are near-identical in Arabic (94:5-6, 102:3-4, 75:34-35 ...):
    identical translations there are a translator's choice, not a merged group."""
    ar = arabic()
    x, y = ar.get((s, a)), ar.get((s, a + 1))
    if not x or not y:
        return False
    strip = lambda t: re.sub(r'^(ف|ثم ?|و)', '', t.replace(' ', ''))
    return sim(strip(x), strip(y)) > 0.7


# ---------------------------------------------------------------- verse groups

_GROUP_PREFIX = re.compile(r'^\s*\(?\s*(\d{1,3}(?:\s*(?:[-–,]|ve)\s*\d{1,3})+)\s*\)?\s*[.:\-–)]?\s+')


def group_prefix(text, a):
    """Host verse-number prefix like '6, 7. ', '(6-7) ', '4-7 ' -> (first, last, rest) or None."""
    m = _GROUP_PREFIX.match(text or '')
    if not m:
        return None
    nums = [int(x) for x in re.findall(r'\d+', m.group(1))]
    if '-' in m.group(1) or '–' in m.group(1):
        lo, hi = min(nums), max(nums)
    else:
        lo, hi = min(nums), max(nums)
        if sorted(nums) != list(range(lo, hi + 1)):
            return None
    if not (lo <= a <= hi) or hi == lo or hi - lo > 40:
        return None
    return lo, hi, text[m.end():]


def build_segments(sid, rows, explicit_groups=False, strip_prefix=True):
    """rows: {(s,a): {'text','notes'?, 'a_end'? (explicit)}} -> list of segments (merged groups once).
    Returns (segments, info) with info: merged-group count, prefix-stripped count, missing list."""
    segs = []
    groups = 0
    stripped = 0
    missing = []
    for s in range(1, 115):
        n = AYAH_COUNTS[s - 1]
        a = 1
        while a <= n:
            r = rows.get((s, a))
            if r is None:
                a += 1
                continue
            text = r.get('text') or ''
            notes = r.get('notes') or ''
            a_end = a
            if explicit_groups and r.get('a_end'):
                a_end = max(a, min(int(r['a_end']), n))
            elif strip_prefix:
                gp = group_prefix(text, a)
                if gp:
                    lo, hi, rest = gp
                    text = rest
                    stripped += 1
                    a_end = min(hi, n)
                    # absorb following ayat that repeat the group text or are empty
                    j = a + 1
                    while j <= a_end:
                        rj = rows.get((s, j))
                        if rj is not None:
                            tj = rj.get('text') or ''
                            gj = group_prefix(tj, j)
                            if gj:
                                tj = gj[2]
                            if tj.strip() and norm_ws(tj) != norm_ws(text):
                                break
                            nj = rj.get('notes') or ''
                            if nj and nj not in notes:
                                notes = (notes + '\n' + nj).strip()
                        j += 1
                    a_end = j - 1
            if not text.strip() or re.fullmatch(r'[\d\s.,;:()\-–]+', text):  # empty, or only the ayah number the host printed
                missing.append((s, a))
                a += 1
                continue
            if not explicit_groups:
                # consecutive duplicates (tanzil style) unless the Arabic itself repeats
                while a_end < n:
                    rn = rows.get((s, a_end + 1))
                    if rn is None:
                        break
                    tn = rn.get('text') or ''
                    gp = group_prefix(tn, a_end + 1) if strip_prefix else None
                    if gp:
                        tn = gp[2]
                    if norm_ws(tn) == norm_ws(text) and not arabic_twins(s, a_end):
                        a_end += 1
                    else:
                        break
            seg = {'seg': f'{sid}:{s}:{a}', 's': s, 'a': a, 'a_end': a_end, 'page': None, 'text': text}
            if notes:
                seg['notes'] = notes
            for k in ('notes_truncated', 'ref', 'head', 'host_flag'):
                if r.get(k):
                    seg[k] = r[k]
            if a_end > a:
                groups += 1
            segs.append(seg)
            a = a_end + 1
    return segs, {'merged_groups': groups, 'prefix_stripped': stripped, 'missing': missing}


def expand(segs):
    """segments -> {(s,a): text} with merged groups copied to each member (comparison only)."""
    out = {}
    for g in segs:
        for a in range(g['a'], g['a_end'] + 1):
            out[(g['s'], a)] = g['text']
    return out


def coverage_of(segs):
    cov = set()
    for g in segs:
        for a in range(g['a'], (g.get('a_end') or g['a']) + 1):
            cov.add((g['s'], a))
    return cov


def coverage_string(cov):
    full = [s for s in range(1, 115) if all((s, a) in cov for a in range(1, AYAH_COUNTS[s - 1] + 1))]
    part = [s for s in range(1, 115) if s not in full and any((s, a) in cov for a in range(1, AYAH_COUNTS[s - 1] + 1))]

    def ranges(xs):
        out, i = [], 0
        while i < len(xs):
            j = i
            while j + 1 < len(xs) and xs[j + 1] == xs[j] + 1:
                j += 1
            out.append(str(xs[i]) if i == j else f'{xs[i]}-{xs[j]}')
            i = j + 1
        return ','.join(out)
    s = ranges(full) if full else ''
    if part:
        s += (' + partial ' if s else 'partial ') + ranges(part)
    return f'{s or "none"} ({len(cov)}/{TOTAL_AYAT} ayat)'


def write_segments(sid, segs):
    path = os.path.join(src_dir(sid), 'segments.jsonl')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        for g in segs:
            f.write(json.dumps(g, ensure_ascii=False) + '\n')
    os.replace(tmp, path)


def read_segments(sid):
    path = os.path.join(src_dir(sid), 'segments.jsonl')
    if not os.path.exists(path):
        return []
    return [json.loads(l) for l in open(path, encoding='utf-8') if l.strip()]


def load_source_json(sid):
    p = os.path.join(src_dir(sid), 'source.json')
    if os.path.exists(p):
        return json.load(open(p, encoding='utf-8'))
    return None


def save_source_json(sid, obj):
    p = os.path.join(src_dir(sid), 'source.json')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')
    os.replace(tmp, p)


def raw_manifest(sid, subdir=''):
    """sha256 of every file under raw/<subdir>; small sets inline, large sets via raw/<subdir>/MANIFEST.sha256."""
    base = os.path.join(src_dir(sid), 'raw', subdir) if subdir else os.path.join(src_dir(sid), 'raw')
    if not os.path.isdir(base):
        return {}
    files = []
    for dp, dn, fn in os.walk(base):
        dn.sort()
        for f in sorted(fn):
            if f.endswith('.tmp') or f == 'MANIFEST.sha256':
                continue
            files.append(os.path.join(dp, f))
    rel = lambda p: os.path.relpath(p, src_dir(sid))
    if len(files) <= 20:
        return {rel(p): sha256_file(p) for p in files}
    man = os.path.join(base, 'MANIFEST.sha256')
    with open(man, 'w', encoding='utf-8') as f:
        for p in files:
            f.write(f'{sha256_file(p)}  {os.path.relpath(p, base)}\n')
    return {rel(man): sha256_file(man), '_count': f'{len(files)} files listed in {rel(man)}'}
