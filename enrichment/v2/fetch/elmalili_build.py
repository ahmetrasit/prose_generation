#!/usr/bin/env python3
"""Elmalılı, Hak Dini Kur'an Dili -- stage 2: logical lines -> pages/, segments, meal source.

Input : enrichment/corpus/ELMALILI/pages/v{n}/lines.jsonl.gz (+ cmaps.json), written by elmalili_extract.py
        /Volumes/aro/projects/quran-data/data/text/quran-uthmani.tsv (s:a|text; basmala is s:0)
Output: enrichment/corpus/ELMALILI/pages/v{n}/p{page}.txt   per-page body text + footnotes (all pages)
        enrichment/corpus/ELMALILI/segments.jsonl + source.json
        enrichment/corpus/MEAL-ELMALILI-HDKD/segments.jsonl + source.json  (the meal inside the tafsir)
        enrichment/corpus/ELMALILI/build_report.json

Structure of the book (all six volumes): a surah opens with an Arabic title line and a bold Turkish heading
("MÂ‘ÛN SÛRESİ"), then an introduction; each passage is printed as a block of Qur'an text (Emine type, ayah
markers ﴿n﴾), the heading "Meâl-i Şerîfi", Elmalılı's meal with (n) numbers, then the commentary, which
takes up the words of the passage in order as lemmas in braces {…}.  A passage (a..b) becomes one segment
per lemma-led sub-passage: the commentary is cut where a paragraph opens with a lemma from a later ayah of
the passage; each piece carries the meal sentences of its ayat.  Footnotes (per page in the print) are
renumbered per segment and kept in `notes`.

Usage: elmalili_build.py [--no-pages]
"""
import argparse
import bisect
import gzip
import hashlib
import json
import os
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from difflib import SequenceMatcher

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
CORPUS = os.path.join(ROOT, 'enrichment', 'corpus')
OUT = os.path.join(CORPUS, 'ELMALILI')
PAGES = os.path.join(OUT, 'pages')
MEAL_OUT = os.path.join(CORPUS, 'MEAL-ELMALILI-HDKD')
PDF_DIR = os.path.join(CORPUS, 'elmalili', 'pdf')
QURAN_TSV = os.path.join(os.path.dirname(ROOT), 'quran-data', 'data', 'text', 'quran-uthmani.tsv')

AYAH_COUNTS = [7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
               112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53, 89,
               59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 12, 12, 30,
               52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 19, 36, 25, 22, 17, 19, 26, 30, 20, 15,
               21, 11, 8, 8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6]
VOL_PAGES = {1: 1056, 2: 1024, 3: 944, 4: 928, 5: 1000, 6: 1155}
URLS = ['https://ekitap.yek.gov.tr/urun/hak-dini-kur-an-dili--cilt-1-4-_743.aspx'] + [
    f'https://ekitap.yek.gov.tr/Uploads/ProductsFiles/{g}.pdf' for g in (
        'e3bcffae-94c8-4654-b97e-caeb01ca8dbb', '58d14e6f-4b4f-44b5-bee4-255420a3bd43',
        'e8cd14a6-e6d0-4eed-aee6-a6a801480c21', '794abfb8-bcbc-4f38-b566-fe9d22c3729a',
        '77044037-3a34-41c2-9871-83f0e6ff5c83', 'd0873fd6-f93b-4d09-abc9-55a45f13a8f3')]
MUKADDIME = (1, 85, 119)          # Elmalılı's own Mukaddime (vol. 1, pp. 85-119): page segments
SPLIT_AT = 7000
DEBUG = os.environ.get('ELM_DEBUG', '').split(',')                   # long segments are cut at paragraph ends into #2, #3 ...

PUA_BASE = 0xF0000
HEBREW_FIX = {'\u05d0': 'ا', '\u05db': 'ك'}   # font ToUnicode bugs: alef/kaf forms -> Hebrew
AR_DIGITS = str.maketrans('٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹', '01234567890123456789')
_MK = '\u0610-\u061A\u064B-\u065F\u06D6-\u06ED'
MARKER = re.compile(rf'[﴾﴿][\s{_MK}]*([٠-٩۰-۹0-9]+)[\s{_MK}]*[﴾﴿]')
PAGE_MARK = re.compile(r'^\s*\[\d{1,4}\]\s*')
REF = re.compile(r'\[([^\[\]]{0,40}?)\s(\d{1,3})/(\d{1,3})(?:\s*-\s*(\d{1,3}))?\]')


# ------------------------------------------------------------------ Arabic normalisation / skeletons

_DIAC = re.compile('[\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed\u08d3-\u08ffـ]')
_SKMAP = str.maketrans({'ٱ': None, 'أ': None, 'إ': None, 'آ': None, 'ى': 'ي', 'ی': 'ي', 'ة': 'ه', 'ؤ': 'و',
                        'ئ': 'ي', 'ک': 'ك', 'ء': None, 'ا': None})


def is_ar(c):
    o = ord(c)
    return 0x0600 <= o <= 0x06FF or 0x0750 <= o <= 0x077F or 0xFB50 <= o <= 0xFDFF or 0xFE70 <= o <= 0xFEFF \
        or PUA_BASE <= o < PUA_BASE + 0xC000


def skel(t, wild=False):
    """Consonantal skeleton without alif/hamza/diacritics/spaces. With wild=True unknown glyphs become '?'."""
    t = unicodedata.normalize('NFKC', t)
    t = _DIAC.sub('', t)
    out = []
    for c in t:
        if c == '\ufffd' or PUA_BASE <= ord(c) < PUA_BASE + 0xC000:
            if wild:
                out.append('?')
            continue
        c = c.translate(_SKMAP)
        if c and 'ء' <= c <= 'ي':
            out.append(c)
    return ''.join(out)


class Quran:
    def __init__(self, path):
        self.text = {}
        for line in open(path, encoding='utf-8'):
            line = line.rstrip('\n').lstrip('\ufeff')
            if '|' not in line:
                continue
            ref, txt = line.split('|', 1)
            s, a = ref.split(':')
            self.text[(int(s), int(a))] = txt.lstrip('\ufeff').strip()
        # word index over the whole text (ayah >= 1; Fatiha's basmala is 1:1)
        self.words = []          # (s, a, uthmani word)
        self.wstart = []         # offset of word in self.sk
        parts, off = [], 0
        for s in range(1, 115):
            for a in range(1, AYAH_COUNTS[s - 1] + 1):
                for w in self.text[(s, a)].split():
                    k = skel(w)
                    if not k:
                        continue
                    self.words.append((s, a, w))
                    self.wstart.append(off)
                    parts.append(k)
                    off += len(k)
        self.sk = ''.join(parts)
        self.ayah_span = {}
        for i, (s, a, w) in enumerate(self.words):
            st = self.wstart[i]
            en = st + len(skel(w))
            lo, hi = self.ayah_span.get((s, a), (st, en))
            self.ayah_span[(s, a)] = (min(lo, st), max(hi, en))

    def span_skel(self, s, a, b):
        lo = self.ayah_span[(s, a)][0]
        hi = self.ayah_span[(s, b)][1]
        return self.sk[lo:hi], lo, hi

    def find(self, q, lo=0, hi=None):
        """All start offsets of skeleton q ('?' = 1-2 unknown letters) within self.sk[lo:hi]."""
        hi = len(self.sk) if hi is None else hi
        if not q:
            return []
        if '?' in q:
            pat = re.compile(''.join('.{0,2}' if c == '?' else re.escape(c) for c in q.strip('?')))
            return [(m.start(), m.end()) for m in pat.finditer(self.sk, lo, hi)]
        out, i = [], self.sk.find(q, lo, hi)
        while i >= 0:
            out.append((i, i + len(q)))
            i = self.sk.find(q, i + 1, hi)
        return out

    def render(self, st, en):
        """Uthmani words covering skeleton offsets [st, en) and their ayah range."""
        i = bisect.bisect_right(self.wstart, st) - 1
        j = bisect.bisect_left(self.wstart, en)
        ws = self.words[max(i, 0):max(j, i + 1)]
        return ' '.join(w for _, _, w in ws), (ws[0][0], ws[0][1]), (ws[-1][0], ws[-1][1])


# ------------------------------------------------------------------ private-use glyph resolution

def load_cmaps():
    """Union of the Arabic fonts' ToUnicode tables over all volumes, per font slot."""
    maps = defaultdict(dict)
    for v in range(1, 7):
        p = os.path.join(PAGES, f'v{v}', 'cmaps.json')
        if not os.path.exists(p):
            continue
        for slot, d in json.load(open(p, encoding='utf-8')).items():
            for cid, u in d.items():
                maps[int(slot)].setdefault(int(cid), u)
    res = {}
    for slot, d in maps.items():
        anchors = sorted(d)
        res[slot] = (anchors, {c: ''.join(HEBREW_FIX.get(ch, ch) for ch in u) for c, u in d.items()})
    return res


class Resolver:
    def __init__(self):
        self.cm = load_cmaps()
        self.inferred = 0
        self.unresolved = 0

    def char(self, c):
        o = ord(c)
        if not (PUA_BASE <= o < PUA_BASE + 0xC000):
            return HEBREW_FIX.get(c, c)
        slot, cid = divmod(o - PUA_BASE, 0x4000)
        anchors, d = self.cm.get(slot, ([], {}))
        if cid in d:
            return d[cid]
        k = bisect.bisect_left(anchors, cid) - 1
        if k >= 0 and cid - anchors[k] <= 3:
            u = d[anchors[k]]
            if len(u) == 1 and unicodedata.category(u) == 'Lo' and 'ء' <= u <= 'ي':
                self.inferred += 1
                return u + '\u200b'     # zero-width marker: inferred letter (removed later, counted)
        self.unresolved += 1
        return '\ufffd'

    def text(self, t):
        if not any(ord(c) >= 0x0590 for c in t):
            return t
        return ''.join(self.char(c) for c in t)


# ------------------------------------------------------------------ page model

def norm_line_text(sp):
    return ''.join(t for _, t in sp)


def line_kind(ln):
    if ln['y'] > 600:
        return 'hdr'
    if ln['sz'] <= 8.6:
        return 'note'
    sp = [(c, t) for c, t in ln['sp'] if t.strip()]
    txt = norm_line_text(sp).strip()
    core = PAGE_MARK.sub('', ''.join(t for c, t in sp if c != 'sup')).strip()
    fold = ''.join(c for c in unicodedata.normalize('NFKD', core.replace('İ', 'i').replace('I', 'ı').lower())
                   if not unicodedata.combining(c))
    if re.fullmatch(r'meal-?i\s*serifi?', fold):
        return 'mhead'
    if re.fullmatch(r'[A-ZÇĞİÖŞÜÂÎÛĀĪŪÊ‘’\'\-\s.]+\sS[ÛU]RES[İI]', core) and ln['sz'] >= 12.5 and \
            all(c in ('bold', 'sup', 'tr') for c, _ in sp):
        return 'shead'
    ncls = Counter()
    for c, t in sp:
        if c in ('tr', 'bold') and re.fullmatch(r'\s*\[\d{1,4}\]\s*', t):
            continue
        ncls[c] += len(t.strip())
    tot = sum(ncls.values()) or 1
    if ncls['quran'] + ncls['sup'] >= 0.97 * tot and (ln['sz'] >= 12.5 or MARKER.search(txt)
                                                      or ln['x1'] - ln['x0'] > 250):
        return 'qblock'
    if ncls['meal'] >= 0.6 * tot:
        return 'meal'
    if ln['sz'] >= 14 and (ncls['ar'] + ncls['quran']) >= 0.8 * tot:
        return 'title_ar'
    return 'body'


def is_meal_cont(r):
    """A body row that continues the meal: has meal type and no plain Turkish commentary text."""
    sp = r['raw']['sp']
    if not any(c == 'meal' and t.strip() for c, t in sp):
        return False
    plain = sum(len(t.strip()) for c, t in sp if c in ('tr', 'it', 'bold') and not re.fullmatch(r'[\s\[\]\d.,;:()“”"’]*', t))
    return plain <= 3


def parse_notes(lines):
    """Footnote lines of one page -> (continuation text, {n: text})."""
    notes, cont, cur = {}, [], None
    for ln in lines:
        sp = [[c, t] for c, t in ln['sp']]
        first = sp[0]
        m = re.match(r'^\s*(\d{1,3})\s+', first[1]) if first[0] in ('bold', 'sup', 'tr') else None
        if m and (first[0] in ('bold', 'sup') or ln['x0'] < 72):
            cur = int(m.group(1))
            first[1] = first[1][m.end():]
            notes[cur] = [sp]
        elif cur is None:
            cont.append(sp)
        else:
            notes[cur].append(sp)
    return cont, notes


class Tok:
    """A piece of running text: cls in tr/it/bold/quran/ar/meal/mhead/sym, or ref (footnote call)."""
    __slots__ = ('cls', 't', 'v', 'p')

    def __init__(self, cls, t, v=None, p=None):
        self.cls, self.t, self.v, self.p = cls, t, v, p


def line_tokens(ln, v, p):
    toks = []
    for c, t in ln['sp']:
        if c == 'sup':
            nums = re.findall(r'\d+', t)
            if nums:
                for n in nums:
                    toks.append(Tok('ref', n, v, p))
                continue
            c = 'tr'
        if c == 'sym':        # Simgeler: ornamental symbols (e.g. a sun glyph before ayah commentary)
            continue
        if c in ('quran', 'ar'):   # braces / brackets set in the Arabic font belong to the running text
            m = re.match(r'^([\s{}\[\]()]*)(.*?)([\s{}\[\]()]*)$', t, re.S)
            if m.group(1):
                toks.append(Tok('tr', m.group(1), v, p))
            if m.group(2):
                toks.append(Tok(c, m.group(2), v, p))
            if m.group(3):
                toks.append(Tok('tr', m.group(3), v, p))
            continue
        toks.append(Tok(c, t, v, p))
    return toks


# ------------------------------------------------------------------ text assembly

def join_lines(lines_toks):
    """Join lines into one token list; de-hyphenate Turkish line ends."""
    out = []
    for toks in lines_toks:
        if not toks:
            continue
        if out:
            last = next((x for x in reversed(out) if x.cls != 'ref'), None)
            nxt = toks[0]
            if last is not None and re.search(r'[a-zçğıöşüâîûāīū]-$', last.t) and nxt.cls != 'ref' \
                    and re.match(r'[a-zçğıöşüâîûāīū]', nxt.t) and not re.match(r'[ıiuü]\s', nxt.t) \
                    and last.cls not in ('quran', 'ar'):
                last.t = last.t[:-1]
            else:
                out.append(Tok(None, ' '))
        out.extend(toks)
    return out


def merge_tokens(toks):
    """Merge adjacent tokens of the same class (spaces join their neighbours)."""
    out = []
    for t in toks:
        if t.cls is None:
            if out and out[-1].cls != 'ref':
                out[-1].t += t.t
            else:
                out.append(Tok('tr', t.t))
            continue
        if out and out[-1].cls == t.cls and t.cls != 'ref':
            out[-1].t += t.t
        elif out and t.cls not in ('ref',) and out[-1].cls not in ('ref',) and out[-1].t.strip() == '' \
                and len(out) >= 2 and out[-2].cls == t.cls:
            sp = out.pop()
            out[-1].t += sp.t + t.t
        else:
            out.append(Tok(t.cls, t.t, t.v, t.p))
    # Arabic quotations split by a line break with only spaces between: merge across a whitespace token
    res = []
    for t in out:
        if res and len(res) >= 2 and res[-1].cls not in ('quran', 'ar', 'ref') and res[-1].t.strip() == '' \
                and res[-2].cls == t.cls and t.cls in ('quran', 'ar'):
            sp = res.pop()
            res[-1].t += sp.t + t.t
        else:
            res.append(t)
    return res


# ------------------------------------------------------------------ Qur'an quotation matching

class QuoteMatcher:
    def __init__(self, Q):
        self.Q = Q
        self.stats = Counter()

    def match(self, text, ctx_s, ctx_a, ctx_b, ref=None):
        """-> (uthmani text, 's:a' or 's:a-b') or None.  ctx = current surah and passage a..b."""
        Q = self.Q
        q = skel(text, wild=True)
        core = q.replace('?', '')
        if len(core) < 2:
            self.stats['too_short'] += 1
            return None
        cands = []
        if ref:                                  # explicit [Sûre s/a(-b)] after the quotation
            s, a, b = ref
            if 1 <= s <= 114 and 1 <= a <= AYAH_COUNTS[s - 1]:
                b = min(max(b, a), AYAH_COUNTS[s - 1])
                lo = Q.ayah_span[(s, max(1, a - 1))][0]
                hi = Q.ayah_span[(s, min(AYAH_COUNTS[s - 1], b + 1))][1]
                cands = Q.find(q, lo, hi)
                if cands:
                    self.stats['ref'] += 1
        if not cands and ctx_s and ctx_a:
            lo = Q.ayah_span[(ctx_s, ctx_a)][0]
            hi = Q.ayah_span[(ctx_s, ctx_b)][1]
            cands = Q.find(q, lo, hi)
            if cands:
                self.stats['passage'] += 1
        if not cands and ctx_s and len(core) >= 5:
            lo = Q.ayah_span[(ctx_s, 1)][0]
            hi = Q.ayah_span[(ctx_s, AYAH_COUNTS[ctx_s - 1])][1]
            c = Q.find(q, lo, hi)
            if len(c) == 1:
                cands = c
                self.stats['surah'] += 1
        if not cands and len(core) >= 9:
            c = Q.find(q)
            if len(c) == 1:
                cands = c
                self.stats['global'] += 1
        if not cands:
            self.stats['unmatched'] += 1
            return None
        st, en = cands[0]
        txt, (s1, a1), (s2, a2) = Q.render(st, en)
        loc = f'{s1}:{a1}' if (s1, a1) == (s2, a2) else (f'{s1}:{a1}-{a2}' if s1 == s2 else f'{s1}:{a1}-{s2}:{a2}')
        return txt, loc, (s1, a1)


# ------------------------------------------------------------------ main build

def load_volume(v):
    pages = {}
    with gzip.open(os.path.join(PAGES, f'v{v}', 'lines.jsonl.gz'), 'rt', encoding='utf-8') as f:
        for line in f:
            pg = json.loads(line)
            pages[pg['p']] = pg['lines']
    return pages


def clean_text(t):
    t = t.replace('\u200b', '')
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r' +([.,;:!?)\]”’])', r'\1', t)
    t = re.sub(r'([(\[“‘]) +', r'\1', t)
    return t.strip()


def fix_braces(t):
    """The print sets lemma braces mirrored around right-to-left text: '}X{' -> '{X}'."""
    return re.sub(r'\}\s*([^{}A-Za-zÇĞİÖŞÜÂÎÛçğıöşüâîû]{1,600}?)\s*\{', lambda m: '{' + m.group(1).strip() + '}', t)


def render(toks, refmap=None, quote_fn=None):
    """Tokens -> string. refmap(tok) gives the footnote label; quote_fn(i, tok) may replace Qur'an text."""
    out = []
    for i, t in enumerate(toks):
        if t.cls == 'ref':
            lab = refmap(t) if refmap else t.t
            if lab:
                out.append(f'[^{lab}]')
            nxt = toks[i + 1].t if i + 1 < len(toks) else ''
            if nxt[:1].isalnum() or (not lab and out and out[-1][-1:].isalnum() and nxt[:1].isalpha()):
                out.append(' ')
            continue
        if t.cls == 'quran' and quote_fn:
            r = quote_fn(i, t)
            if r is not None:
                lead = ' ' if t.t[:1].isspace() else ''
                trail = ' ' if t.t[-1:].isspace() else ''
                out.append(lead + r + trail)
                continue
        txt = t.t
        if t.cls in ('quran', 'ar'):
            txt = unicodedata.normalize('NFKC', txt) if any(0xFB50 <= ord(c) <= 0xFEFF for c in txt) else txt
        out.append(txt)
    return fix_braces(clean_text(''.join(out)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--no-pages', action='store_true')
    args = ap.parse_args()

    Q = Quran(QURAN_TSV)
    R = Resolver()
    QM = QuoteMatcher(Q)
    report = {'warnings': []}
    warn = report['warnings'].append

    # ---------- pass 1: per volume, classify lines, collect notes, build a flat stream of body lines
    stream = []          # dicts: kind, v, p, x0, y, sz, toks, raw
    notes = {}           # (v, p, n) -> text
    notes_bad = set()    # notes whose Arabic has inferred or unknown glyphs
    for v in range(1, 7):
        pages = load_volume(v)
        prev_last_note = None
        for p in sorted(pages):
            lines = pages[p]
            for ln in lines:
                ln['sp'] = [[c, R.text(t) if c in ('ar', 'quran', 'it', 'tr', 'bold', 'meal') else t]
                            for c, t in ln['sp']]
            body, nlines = [], []
            for ln in lines:
                k = line_kind(ln)
                if k == 'hdr':
                    continue
                if k == 'note':
                    nlines.append(ln)
                else:
                    body.append((k, ln))
            cont, pn = parse_notes(nlines)

            def ntext(sps):
                return clean_text(' '.join(render([Tok(c if c != 'sup' else 'tr', t) for c, t in sp])
                                           for sp in sps))
            def badsp(sps):
                return any(('\u200b' in t or '\ufffd' in t) and c in ('ar', 'quran') for sp in sps for c, t in sp)
            if cont and prev_last_note in notes:
                notes[prev_last_note] += ' ' + ntext(cont)
                if badsp(cont):
                    notes_bad.add(prev_last_note)
            for n, sps in pn.items():
                notes[(v, p, n)] = ntext(sps)
                if badsp(sps):
                    notes_bad.add((v, p, n))
            if pn:
                prev_last_note = (v, p, max(pn))
            if DEBUG and f'v{v}p{p}' in DEBUG:
                for k, ln in body:
                    print('DBG', f'v{v}p{p}', k, ln['sz'], norm_line_text(ln['sp'])[:90])
            for k, ln in body:
                stream.append({'kind': k, 'v': v, 'p': p, 'x0': ln['x0'], 'y': ln['y'], 'sz': ln['sz'],
                               'toks': line_tokens(ln, v, p), 'raw': ln})
            if not args.no_pages:
                write_page(v, p, body, pn, cont, ntext)
    # front matter of each volume (before its first surah heading), vol. 1 Mukaddime, vol. 6 indexes
    first_head = {}
    for idx, r in enumerate(stream):
        if r['kind'] == 'shead' and r['v'] not in first_head:
            first_head[r['v']] = idx
    back = None
    for idx, r in enumerate(stream):
        if r['v'] == 6 and r['p'] > 1000 and r['sz'] >= 12.5 and \
                re.search(r'DİZİNİ\s*$', norm_line_text(r['raw']['sp'])):
            back = idx
            break
    for idx, r in enumerate(stream):
        if idx < first_head.get(r['v'], 0):
            r['kind'] = 'muk' if (r['v'] == MUKADDIME[0] and MUKADDIME[1] <= r['p'] <= MUKADDIME[2]) else 'front'
        elif back is not None and idx >= back:
            r['kind'] = 'back'
    report['back_matter_from'] = f"v6p{stream[back]['p']}" if back is not None else None
    report['glyphs_inferred'] = R.inferred
    report['glyphs_unresolved'] = R.unresolved

    # ---------- pass 2: structure (surahs, passages, meal, commentary)
    units = []           # {'type': 'front'|'mukaddime'|'intro'|'basmala'|'block', ...}
    surah = 0
    i = 0
    n = len(stream)

    def para_breaks(rows):
        """Group body rows into paragraphs (indent / vertical gap / page start heuristics)."""
        paras, cur, prev = [], [], None
        for r in rows:
            newp = False
            if prev is None:
                newp = True
            elif r['kind'] != prev['kind'] and r['kind'] in ('body', 'meal'):
                newp = True
            elif (r['v'], r['p']) == (prev['v'], prev['p']):
                gap = prev['y'] - r['y']
                if gap > 1.45 * max(r['sz'], 12) + 2 or r['x0'] > 78 or r['kind'] == 'title_ar':
                    newp = True
            else:
                if r['x0'] > 78:
                    newp = True
            if newp and cur:
                paras.append(cur)
                cur = []
            cur.append(r)
            prev = r
        if cur:
            paras.append(cur)
        return paras

    # locate surah headings
    heads = [k for k, r in enumerate(stream) if r['kind'] == 'shead']
    if len(heads) != 114:
        warn(f'{len(heads)} surah headings found (expected 114)')
    report['surah_headings'] = len(heads)
    head_of = {k: s + 1 for s, k in enumerate(heads)}

    # walk
    cur_surah, k = 0, 0
    pending_rows = []

    def flush(kind, rows, **kw):
        if rows:
            units.append(dict(kind=kind, rows=list(rows), **kw))

    blocks = []
    muk_rows = []
    while k < n:
        r = stream[k]
        if r['kind'] in ('front', 'back'):
            k += 1
            continue
        if r['kind'] == 'muk':
            muk_rows.append(r)
            k += 1
            continue
        if r['kind'] == 'shead':
            flush('pre' if cur_surah == 0 else 'comm', pending_rows, s=cur_surah)
            pending_rows = []
            cur_surah = head_of[k]
            units.append(dict(kind='shead', rows=[r], s=cur_surah))
            k += 1
            continue
        if r['kind'] == 'qblock':
            # collect the block (allow page-marker-only lines in between)
            j, brows = k, []
            while j < n and (stream[j]['kind'] == 'qblock' or (
                    stream[j]['kind'] == 'body' and re.fullmatch(r'\s*\[\d{1,4}\]\s*',
                                                                 render(stream[j]['toks']) or 'x')
                    and j + 1 < n and stream[j + 1]['kind'] == 'qblock')):
                brows.append(stream[j])
                j += 1
            # meal heading + meal lines (page-marker-only lines may sit in between)
            mrows, m = [], j
            while m < n and stream[m]['kind'] == 'body' and \
                    re.fullmatch(r'\s*\[\d{1,4}\]\s*', render(stream[m]['toks']) or 'x'):
                mrows.append(stream[m])
                m += 1
            if not (m < n and stream[m]['kind'] in ('mhead', 'meal')):
                mrows, m = [], j
            if m < n and stream[m]['kind'] == 'mhead':
                mh = stream[m]
                m += 1
                while m < n and (stream[m]['kind'] == 'meal' or (mrows and stream[m]['kind'] == 'body' and
                                                                 is_meal_cont(stream[m]))):
                    mrows.append(stream[m])
                    m += 1
            else:
                mh = None
                while m < n and (stream[m]['kind'] == 'meal' or (mrows and stream[m]['kind'] == 'body' and
                                                                 is_meal_cont(stream[m]))):
                    mrows.append(stream[m])
                    m += 1
            if (mh is None and not mrows) or cur_surah == 0:
                pending_rows.extend(brows + mrows)
                k = j if mh is None else m
                continue
            if cur_surah == 0:
                pending_rows.extend(brows + mrows)
                k = m
                continue
            flush('comm', pending_rows, s=cur_surah)
            pending_rows = []
            units.append(dict(kind='block', rows=brows, meal=mrows, mhead=mh, s=cur_surah))
            k = m
            continue
        if r['kind'] in ('mhead',):      # stray meal heading without a block (rare)
            warn(f'meal heading without Qur\'an block at v{r["v"]}p{r["p"]}')
        pending_rows.append(r)
        k += 1
    flush('comm', pending_rows, s=cur_surah)

    if DEBUG and DEBUG != ['']:
        for u in units:
            if any(f"v{r['v']}p{r['p']}" in DEBUG for r in u['rows']):
                print('UNIT', u['kind'], u.get('s'), len(u['rows']), f"v{u['rows'][0]['v']}p{u['rows'][0]['p']}",
                      norm_line_text(u['rows'][0]['raw']['sp'])[:60])
    # ---------- pass 3: passages (a..b) from the blocks
    last_b = defaultdict(int)
    passages = []        # dict(s, a, b, block_unit, comm_unit, score)
    for ui, u in enumerate(units):
        if u['kind'] != 'block':
            continue
        s = u['s']
        btxt = ' '.join(norm_line_text(r['raw']['sp']) for r in u['rows'])
        digs = [x.translate(AR_DIGITS) for x in MARKER.findall(btxt)]
        nums = [int(x) for x in digs]
        exp = last_b[s] + 1
        score, a, b = 0.0, None, None
        bsk = skel(MARKER.sub(' ', btxt), wild=False)
        bas = skel(Q.text[(1, 1)])
        if bsk.startswith(bas) and not (s == 1):
            bsk = bsk[len(bas):]
        if nums and len(nums) > 1 and nums[0] == exp - 1 and MARKER.match(btxt.strip()):
            nums, digs = nums[1:], digs[1:]       # end marker of the previous ayah carried over a page
        if nums:
            # markers run exp, exp+1, ...; a marker whose digits came out reversed is read back
            e = exp if not (s == 1 and exp == 1) else 2
            fixed = []
            for x, d in zip(nums, digs):
                rx = int(d[::-1])
                if x != e and rx == e:
                    x = rx
                fixed.append(x)
                e = x + 1
            nums = fixed
            a, b = nums[0], nums[-1]
            if nums != list(range(a, b + 1)):
                # fall back on the meal's (n) numbers when they run on from the previous passage
                mn = [int(x) for x in re.findall(r'\((\d{1,3})\)', ' '.join(
                    norm_line_text(r['raw']['sp']) for r in u['meal']))]
                chain, want = [], (exp if not (s == 1 and exp == 1) else 2)
                for x in mn:
                    if x == want:
                        chain.append(x)
                        want += 1
                if chain:
                    a, b = chain[0], chain[-1]
                    warn(f'S{s}: block markers {nums} unreadable, passage {a}-{b} taken from the meal '
                         f'(v{u["rows"][0]["v"]}p{u["rows"][0]["p"]})')
                else:
                    warn(f'S{s}: block markers not consecutive {nums} (v{u["rows"][0]["v"]}p{u["rows"][0]["p"]})')
                    a, b = min(nums), max(nums)
        if a is None or b is None or not (1 <= a <= b <= AYAH_COUNTS[s - 1]):
            # no usable marker: locate the block text in the surah
            if len(bsk) >= 8:
                lo = Q.ayah_span[(s, 1)][0]
                hi = Q.ayah_span[(s, AYAH_COUNTS[s - 1])][1]
                sm = SequenceMatcher(None, Q.sk[lo:hi], bsk, autojunk=False)
                mt = sm.find_longest_match(0, hi - lo, 0, len(bsk))
                if mt.size >= 6:
                    _, (s1, a1), _ = Q.render(lo + mt.a, lo + mt.a + 1)
                    a = b = a1
            if a is None:
                warn(f'block without ayah numbers at v{u["rows"][0]["v"]}p{u["rows"][0]["p"]} (S{s})')
                continue
        if a != exp and not (s == 1 and a == 2 and exp == 1):
            warn(f'S{s}: passage {a}-{b} follows {exp - 1} (v{u["rows"][0]["v"]}p{u["rows"][0]["p"]})')
        ref_sk, _, _ = Q.span_skel(s, a, b)
        score = SequenceMatcher(None, ref_sk, bsk, autojunk=False).ratio() if bsk else 0.0
        last_b[s] = max(last_b[s], b)
        passages.append(dict(s=s, a=a, b=b, ui=ui, score=round(score, 3)))
    report['passages'] = len(passages)
    report['passage_list'] = [f"{p['s']}:{p['a']}-{p['b']} {p['score']} v{units[p['ui']]['rows'][0]['v']}"
                              f"p{units[p['ui']]['rows'][0]['p']}" for p in passages]
    low = [p for p in passages if p['score'] < 0.85]
    report['passages_low_score'] = [(p['s'], p['a'], p['b'], p['score']) for p in low]

    # ---------- pass 4: segments
    segs, meal_segs = [], []
    seg_ids = Counter()
    fn_counter = {}

    def new_seg(base, s, a, b, rows, head, toks_paras, extra=None, ctx=None):
        """toks_paras: list of token lists (paragraphs). Writes one or more segments (#2… for long ones)."""
        ctx = ctx or (s, a, b)
        refs_used, labels = [], {}

        def refmap(t):
            key = (t.v, t.p, int(t.t))
            if key not in notes:
                return None
            if key not in labels:
                labels[key] = len(labels) + 1
                refs_used.append(key)
            return str(labels[key])
        quotes = []
        state = {'cur': ctx[1]}

        flags = {'bad': False}

        def quote_fn(i, t, toks):
            ref = None
            tail = render(toks[i + 1:i + 4])[:60]
            m = REF.match(tail.lstrip())
            if m:
                ref = (int(m.group(2)), int(m.group(3)), int(m.group(4) or m.group(3)))
            r = QM.match(t.t, ctx[0], max(1, ctx[1] or 1), ctx[2] or ctx[1] or 1, ref) if ctx[0] else \
                QM.match(t.t, None, None, None, ref)
            if r is None:
                if '\u200b' in t.t or '\ufffd' in t.t:
                    flags['bad'] = True
                return None
            quotes.append(r[1])
            return r[0]
        for toks in toks_paras:
            for t in toks:
                if t.cls == 'ar' and ('\u200b' in t.t or '\ufffd' in t.t):
                    flags['bad'] = True
        texts = []
        for toks in toks_paras:
            q0 = len(quotes)
            x = render(toks, refmap, lambda i, t, toks=toks: quote_fn(i, t, toks))
            if x:
                texts.append((x, quotes[q0:]))
        if not texts:
            return
        # split long text
        parts, cur = [], []
        for x in texts:
            if cur and sum(len(y[0]) for y in cur) + len(x[0]) > SPLIT_AT:
                parts.append(cur)
                cur = []
            cur.append(x)
        if cur:
            parts.append(cur)
        pages = sorted({(r['v'], r['p']) for r in rows})
        for pi, part in enumerate(parts):
            body = '\n'.join(x for x, _ in part)
            pquotes = [q for _, qs in part for q in qs]
            seg = base if pi == 0 else f'{base}#{pi + 1}'
            seg_ids[seg] += 1
            if seg_ids[seg] > 1:
                seg = f'{seg}#{seg_ids[seg]}x'
            nlabels = sorted(set(int(m) for m in re.findall(r'\[\^(\d+)\]', body)))
            inv = {v_: k_ for k_, v_ in labels.items()}
            nts = [f'[^{lab}] {notes[inv[lab]]}' for lab in nlabels if lab in inv]
            o = {'seg': seg, 's': s, 'a': a, 'a_end': b, 'page': f'v{pages[0][0]}p{pages[0][1]}',
                 'pages': f'v{pages[0][0]}p{pages[0][1]}-' + (f'{pages[-1][1]}' if pages[-1][0] == pages[0][0]
                                                             else f'v{pages[-1][0]}p{pages[-1][1]}')}
            if head:
                o['head'] = head if pi == 0 else f'{head} ({pi + 1})'
            o['text'] = body
            if nts:
                o['notes'] = nts
            if extra and pi == 0:
                o.update(extra)
            if pquotes:
                o['quran_quotes'] = sorted(set(pquotes), key=lambda x: [int(y) for y in re.findall(r'\d+', x)])
            # Arabic reliability (non-Qur'an Arabic left in text or notes)
            rest = re.sub(r'\{[^{}]*\}', '', body) + ' '.join(nts)
            nbad = any(inv[lab] in notes_bad for lab in nlabels if lab in inv)
            if any(is_ar(c) for c in rest):
                o['arabic_reliable'] = not (flags['bad'] or nbad or '\ufffd' in rest)
            segs.append(o)

    def para_toks(rows):
        return [merge_tokens(join_lines([r['toks'] for r in pr])) for pr in para_breaks(rows)]

    # front matter / mukaddime / intros / commentary
    passage_by_ui = {p['ui']: p for p in passages}
    surah_names = {}
    for ui, u in enumerate(units):
        if u['kind'] == 'shead':
            nm = PAGE_MARK.sub('', render(u['rows'][0]['toks']))
            nm = re.sub(r'\[\^\d+\]', '', nm).strip()
            surah_names[u['s']] = tr_title(nm)
    report['surah_names'] = surah_names

    covered = defaultdict(set)
    byp = defaultdict(list)
    for r in muk_rows:
        byp[(r['v'], r['p'])].append(r)
    for (v, p), rows in sorted(byp.items()):
        new_seg(f'ELMALILI:v{v}p{p}', None, None, None, rows, 'Mukaddime', para_toks(rows), ctx=(None, None, None))
    for ui, u in enumerate(units):
        if u['kind'] == 'pre':
            warn(f'{len(u["rows"])} lines before the first surah heading outside the front matter')
            continue
        if u['kind'] == 'comm':
            s = u['s']
            prev = units[ui - 1] if ui else None
            if prev is not None and prev['kind'] == 'shead':
                # surah introduction (Fatiha: intro, then BESMELE = 1:1)
                rows = u['rows']
                if s == 1:
                    kb = next((j for j, r in enumerate(rows) if render(r['toks']).strip() == 'BESMELE'), None)
                    if kb is not None:
                        new_seg('ELMALILI:1:0', 1, 0, 0, rows[:kb], f'{surah_names.get(1, "")} — giriş',
                                para_toks(rows[:kb]))
                        new_seg('ELMALILI:1:1', 1, 1, 1, rows[kb:], 'Fâtiha 1 — Besmele', para_toks(rows[kb:]),
                                ctx=(1, 1, 1))
                        covered[1].add(1)
                        continue
                new_seg(f'ELMALILI:{s}:0', s, 0, 0, rows, f'{surah_names.get(s, "")} — giriş', para_toks(rows))
                continue
            if prev is not None and prev['kind'] == 'block' and (ui - 1) in passage_by_ui:
                continue      # handled with its block
            # trailing matter after the last surah (vol. 6 end: closing pages / indexes)
            if s == 114 and prev is not None:
                pass
            byp = defaultdict(list)
            for r in u['rows']:
                byp[(r['v'], r['p'])].append(r)
            warn(f'unattached commentary rows S{s} v{u["rows"][0]["v"]}p{u["rows"][0]["p"]} '
                 f'({len(u["rows"])} lines)')
            continue
        if u['kind'] != 'block' or ui not in passage_by_ui:
            continue
        P = passage_by_ui[ui]
        s, a, b = P['s'], P['a'], P['b']
        if s == 1 and a == 2:
            pass
        comm = units[ui + 1]['rows'] if ui + 1 < len(units) and units[ui + 1]['kind'] == 'comm' else []
        # trailing back matter after Nâs: stop at the first page that looks like an index/bibliography
        if s == 114 and comm:
            cut = None
            for j, r in enumerate(comm):
                t = render(r['toks']).strip()
                if r['kind'] == 'body' and re.fullmatch(r'(DİZİN|KAYNAKÇA|BİBLİYOGRAFYA|İNDEKS|GENEL DİZİN)', t):
                    cut = j
                    break
            if cut is not None:
                comm = comm[:cut]
        # meal: split by (n)
        meal_toks = merge_tokens(join_lines([r['toks'] for r in u['meal']]))
        meal_plain = render(meal_toks, refmap=lambda t: None)
        pieces, reached = split_meal(meal_plain, a, b) if meal_plain else ({}, a - 1)
        meal_in_comm = False
        if not meal_plain and comm:
            # a passage printed without the «Meâl-i Şerîfi» heading: its meal is the opening of the text, with the (n) numbers
            cm_ = render(merge_tokens(join_lines([r['toks'] for r in comm[:14]])), refmap=lambda t: None)
            mb_ = re.search(rf'\({b}\)[.,;:!?…]*', cm_)
            if mb_:
                cm_ = cm_[:mb_.end()]  # the meal ends at its last number; what follows is commentary
            pieces2_, reached2_ = split_meal(cm_, a, b)
            if pieces2_ and reached2_ == b:
                meal_plain, pieces, reached = cm_, pieces2_, reached2_
                meal_in_comm = True  # its text stays in the commentary: not prepended again
                report.setdefault('meal_read_without_heading', []).append(f'{s}:{a}-{b}')
        mh_ok = bool(pieces)
        mpage = f'v{u["meal"][0]["v"]}p{u["meal"][0]["p"]}' if u['meal'] else None
        for k_, (e_, txt, pu_) in sorted(pieces.items()):
            txt = clean_text(txt + pu_)
            loc_ = f'{s}:{k_}' if e_ == k_ else f'{s}:{k_}-{e_}'
            meal_segs.append({'seg': f'MEAL-ELMALILI-HDKD:{loc_}', 's': s, 'a': k_, 'a_end': e_,
                              'page': mpage, 'text': txt})
        if meal_plain and reached < b:
            warn(f'S{s}:{a}-{b} meal numbering stops at {reached}')
            rest = meal_plain
            if pieces:
                rest = meal_plain[split_meal.last_pos:].strip()  # after the last number the chain accepted
            if len(rest) > 3:
                meal_segs.append({'seg': f'MEAL-ELMALILI-HDKD:{s}:{reached + 1}-{b}', 's': s, 'a': reached + 1,
                                  'a_end': b, 'page': mpage, 'text': clean_text(rest), 'split': False})
                pieces[reached + 1] = (b, clean_text(rest), '')
        if not meal_plain:
            warn(f'S{s}:{a}-{b} no meal found')
        # commentary paragraphs, cut at lemma paragraphs of later ayat
        paras = para_breaks(comm) if comm else []
        ptoks = [merge_tokens(join_lines([r['toks'] for r in pr])) for pr in paras]
        groups = [[a, []]]          # [start ayah, [para indices]]
        cur = a
        for pi, toks in enumerate(ptoks):
            k_ = lemma_ayah(toks, Q, s, cur, b)
            if k_ is not None and k_ > cur and groups[-1][1]:
                groups.append([k_, []])
                cur = k_
            groups[-1][1].append(pi)
        for gi, (ga, pis) in enumerate(groups):
            gb = groups[gi + 1][0] - 1 if gi + 1 < len(groups) else b
            rows = [r for pi in pis for r in paras[pi]] or list(u['rows'])
            mealtxt = ''
            if mh_ok:
                mealtxt = ' '.join(f'{pieces[x][1]} ({x if pieces[x][0] == x else f"{x}-{pieces[x][0]}"}){pieces[x][2]}'
                                   for x in range(ga, gb + 1) if x in pieces)
            elif gi == 0 and meal_plain:
                mealtxt = meal_plain
            tparas = [ptoks[pi] for pi in pis]
            if mealtxt and not meal_in_comm:
                tparas = [[Tok('tr', 'Meâl: ' + mealtxt)]] + tparas
            loc = f'{s}:{ga}' if ga == gb else f'{s}:{ga}-{gb}'
            extra = {'passage': f'{s}:{a}-{b}' if a != b else f'{s}:{a}', 'quran_block_match': P['score']}
            if s == 1 and a == 2 and gi == 0:
                extra['note_basmala'] = '1:1 (Besmele) is commented separately before this passage'
            new_seg(f'ELMALILI:{loc}', s, ga, gb, rows + u['meal'], f'{surah_names.get(s, "")} {loc.split(":")[1]}',
                    tparas, extra=extra, ctx=(s, ga, gb))
            covered[s].update(range(ga, gb + 1))

    # ---------- coverage & output
    missing = [(s, x) for s in range(1, 115) for x in range(1, AYAH_COUNTS[s - 1] + 1) if x not in covered[s]]
    report['segments'] = len(segs)
    report['ayah_segments'] = sum(1 for x in segs if x['s'] and x['a'])
    report['surahs_covered'] = sum(1 for s in range(1, 115) if covered[s])
    report['ayat_covered'] = sum(len(covered[s]) for s in covered)
    report['ayat_missing'] = len(missing)
    report['ayat_missing_list'] = compress(missing)
    report['meal_segments'] = len(meal_segs)
    report['meal_ayat'] = sum(m['a_end'] - m['a'] + 1 for m in meal_segs if m.get('split', True))
    report['quote_match'] = dict(QM.stats)
    write_outputs(segs, meal_segs, report)
    print(json.dumps({k: v for k, v in report.items() if k not in ('warnings', 'ayat_missing_list',
                                                                   'surah_names', 'passages_low_score', 'passage_list')},
                     ensure_ascii=False, indent=1))
    print('warnings:', len(report['warnings']))
    for w in report['warnings'][:40]:
        print('  ', w)
    print('missing:', report['ayat_missing_list'][:400])
    print('low-score passages:', report['passages_low_score'][:30])


def tr_title(t):
    low = t.replace('I', 'ı').replace('İ', 'i').lower()
    return re.sub(r"(^|[\s\-])(\w)", lambda m: m.group(1) + m.group(2).replace('i', 'İ').upper(), low)


def compress(pairs):
    out, prev = [], None
    for s, a in pairs:
        if prev and prev[0] == s and prev[2] == a - 1:
            prev[2] = a
        else:
            if prev:
                out.append(prev)
            prev = [s, a, a]
    if prev:
        out.append(prev)
    return ', '.join(f'{s}:{a}' if a == b else f'{s}:{a}-{b}' for s, a, b in out)


def split_meal(text, a, b):
    """'… (1) … (2). … (3-4) …' -> {start: (end, text)} along the chain a, a+1, … ; also returns the last
    ayah reached (b when the meal splits completely)."""
    out, pos, want = {}, 0, a
    split_meal.last_pos = 0
    for m in re.finditer(r'\((\d{1,3})(?:\s*[-–,]\s*(\d{1,3}))?\)([.,;:!?…]*)', text):
        x = int(m.group(1))
        y = int(m.group(2)) if m.group(2) else x
        if x != want or y < x or y > b:
            continue
        out[x] = (y, clean_text(text[pos:m.start()].strip()), m.group(3))
        pos = m.end()
        split_meal.last_pos = pos
        want = y + 1
    tail = text[pos:].strip()
    if out and tail and len(tail) > 3 and want == b + 1:
        last = max(out)
        out[last] = (out[last][0], clean_text(out[last][1] + out[last][2] + ' ' + tail), '')
    return out, want - 1


def lemma_ayah(toks, Q, s, cur, b):
    """If a paragraph opens with a Qur'an lemma from ayah k in cur..b of surah s, return k."""
    seen = 0
    for t in toks:
        if t.cls == 'ref':
            continue
        txt = t.t.strip()
        if not txt:
            continue
        if t.cls in ('tr', 'it', 'bold') and re.fullmatch(r'[\[\]\d\s{}]*', txt):
            continue
        if t.cls != 'quran':
            return None
        q = skel(t.t, wild=True)
        if len(q.replace('?', '')) < 2:
            return None
        lo = Q.ayah_span[(s, cur)][0]
        hi = Q.ayah_span[(s, b)][1]
        c = Q.find(q, lo, hi)
        if not c:
            return None
        _, (s1, a1), _ = Q.render(c[0][0], c[0][1])
        # the earliest occurrence must not sit in the current ayah when the lemma is ambiguous
        return a1
    return None


def write_page(v, p, body, pn, cont, ntext):
    d = os.path.join(PAGES, f'v{v}')
    rows = []
    for k, ln in body:
        rows.append(render(merge_tokens(line_tokens(ln, v, p))))
    txt = '\n'.join(rows)
    nt = []
    if cont:
        nt.append('(cont.) ' + ntext(cont))
    for n_, sps in sorted(pn.items()):
        nt.append(f'[^{n_}] ' + ntext(sps))
    if nt:
        txt += '\n\n--- notes ---\n' + '\n'.join(nt)
    with open(os.path.join(d, f'p{p}.txt'), 'w', encoding='utf-8') as f:
        f.write(txt.replace('\u200b', '') + '\n')


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def write_outputs(segs, meal_segs, report):
    os.makedirs(OUT, exist_ok=True)
    raw = os.path.join(OUT, 'raw')
    if not os.path.lexists(raw):
        os.symlink(os.path.join('..', 'elmalili', 'pdf'), raw)
    files = {f'raw/cilt{v}.pdf': sha256(os.path.join(PDF_DIR, f'cilt{v}.pdf')) for v in range(1, 7)}
    with open(os.path.join(OUT, 'segments.jsonl.tmp'), 'w', encoding='utf-8') as f:
        for o in segs:
            f.write(json.dumps(o, ensure_ascii=False) + '\n')
    os.replace(os.path.join(OUT, 'segments.jsonl.tmp'), os.path.join(OUT, 'segments.jsonl'))
    with open(os.path.join(OUT, 'build_report.json'), 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    qs = report['quote_match']
    src = {
        'id': 'ELMALILI',
        'title': "Hak Dini Kur'an Dili",
        'author': 'Elmalılı Muhammed Hamdi Yazır',
        'death_ah': 1361,
        'kind': 'tafsir_tr',
        'tradition': 'ottoman-late, hanafi-maturidi; republican-era official tafsir (1935-38)',
        'language': 'tr',
        'edition': "Hak Dini Kur'an Dili, ed. Asım Cüneyd Köksal & Murat Kaya, YEK 2021–2023, 6 vols "
                   "(ISBN 978-975-17-4868-3)",
        'access': 'yerel',
        'locator': 'ayah',
        'coverage': f"1-114; {report['ayat_covered']} of 6236 ayat in ayah segments "
                    f"({report['ayat_missing']} without one); plus surah introductions (s:0) and the "
                    "author's Mukaddime as page segments (ELMALILI:v1p85…v1p119)",
        'urls': URLS,
        'fetched_at': date.today().isoformat(),
        'files': files,
        'licence': 'official free e-book from YEK; local research copy',
        'segments': len(segs),
        'notes': (
            "Text from the publisher's PDFs (real text layer) via pdfminer.six at glyph level "
            "(enrichment/v2/fetch/elmalili_extract.py, elmalili_build.py); per-page text with running heads "
            "removed in pages/v{n}/p{page}.txt. Original first-edition page numbers are kept inline as "
            "[nnnn]. Footnotes (variant readings of the manuscripts/prints H, M, B, F and source references "
            "by the editors) are renumbered per segment as [^n] and listed in `notes`. "
            "Segmentation: Elmalılı prints a passage (Arabic, 'Meâl-i Şerîfi', commentary); a passage a..b is cut "
            "into sub-segments where a paragraph opens with a lemma {…} of a later ayah, otherwise kept as one "
            "a..a_end group; every segment starts with 'Meâl:' + his meal sentences for its ayat. "
            "Surah introductions are s:0 segments (not the basmala); for al-Fātiḥa 1:0 is the introduction "
            "and 1:1 the long Besmele section. Long segments are cut at paragraph ends into #2, #3 … parts. "
            "Arabic: the PDFs store Arabic in visual order (presentation forms in vols 1-5); it is rebuilt in "
            "logical order from glyph positions and NFKC-normalised. Qur'an quotations (Emine type) are "
            "identified by consonantal skeleton against quran-uthmani.tsv (explicit [Sûre s/a] reference, "
            "current passage, current surah, or a unique match in the whole Qur'an) and replaced by the "
            f"Uthmani text of the matched words (matched: {qs.get('ref', 0) + qs.get('passage', 0) + qs.get('surah', 0) + qs.get('global', 0)}, "
            f"unmatched/too short: {qs.get('unmatched', 0) + qs.get('too_short', 0)}; refs in `quran_quotes`). "
            "Other Arabic (quotations from tafsir, hadith, poetry, mostly in footnotes) is best-effort: in vols 1-2 "
            "many glyphs of the Traditional Naskh font have no Unicode mapping; contextual letter forms are "
            "inferred from the font's glyph order and unknown glyphs are shown as U+FFFD; segments with such "
            "Arabic carry arabic_reliable: false. The Arabic passage blocks themselves are not in the text "
            "(see `passage` and `quran_block_match`, the skeleton similarity of the printed block to the "
            "Uthmani text). Front matter (editors' introduction), the table of contents and indexes are in "
            "pages/ only."),
    }
    with open(os.path.join(OUT, 'source.json'), 'w', encoding='utf-8') as f:
        json.dump(src, f, ensure_ascii=False, indent=2)
        f.write('\n')
    # meal source
    os.makedirs(MEAL_OUT, exist_ok=True)
    with open(os.path.join(MEAL_OUT, 'segments.jsonl.tmp'), 'w', encoding='utf-8') as f:
        for o in meal_segs:
            f.write(json.dumps(o, ensure_ascii=False) + '\n')
    os.replace(os.path.join(MEAL_OUT, 'segments.jsonl.tmp'), os.path.join(MEAL_OUT, 'segments.jsonl'))
    msrc = {
        'id': 'MEAL-ELMALILI-HDKD',
        'title': "Hak Dini Kur'an Dili — Meâl-i Şerîf (the meal printed inside the tafsir)",
        'author': 'Elmalılı Muhammed Hamdi Yazır',
        'death_ah': 1361,
        'kind': 'meal',
        'tradition': 'ottoman-late, hanafi-maturidi',
        'language': 'tr',
        'edition': "Meal sections ('Meâl-i Şerîfi') of Hak Dini Kur'an Dili, ed. Köksal & Kaya, YEK 2021–2023 "
                   "(critical edition of the 1935-38 print, original orthography)",
        'access': 'yerel',
        'locator': 'ayah',
        'coverage': f"{report['meal_ayat']} of 6236 ayat split per ayah",
        'urls': URLS,
        'fetched_at': date.today().isoformat(),
        'files': files,
        'lineage': 'elmalili-1935',
        'licence': 'official free e-book from YEK; local research copy',
        'segments': len(meal_segs),
        'notes': ("Elmalılı's own meal as printed in the tafsir (italic type, after each Arabic passage), cut at "
                  "his (n) ayah numbers; text before (n) is ayah n, punctuation after the number stays with it. "
                  "Footnote calls are dropped. Not the later 'sadeleştirilmiş' or edited meal editions: use this "
                  "source to compare the meal inside the tafsir with separately published Elmalılı meals. "
                  "Groups whose numbering did not split cleanly are one segment a..a_end with split: false. "
                  "1:1 (Besmele) is not printed in the Fātiḥa meal block. Built by "
                  "enrichment/v2/fetch/elmalili_build.py; raw files are the ELMALILI PDFs."),
        'ingestion': {
            'date': date.today().isoformat(), 'script': 'enrichment/v2/fetch/elmalili_build.py',
            'method': 'meal block of each passage (italic type after the Arabic), cut at the (n) numbers; the rest after a '
                      'misprinted or missing number is one group a..a_end with split: false',
            'meal_extended_or_read_without_heading': report.get('meal_read_without_heading', []),
            'missing': [{'ayah': '1:1',
                         'reason': "the Besmele is not translated in the Fâtiha meal block; Elmalılı comments on it separately "
                                   "(ELMALILI:1:1) without a meal of its own",
                         'checked': ['the printed meal block of the Fâtiha passage 1:2-7 (volume 1)',
                                     'the commentary segment ELMALILI:1:1']}]},
    }
    with open(os.path.join(MEAL_OUT, 'source.json'), 'w', encoding='utf-8') as f:
        json.dump(msrc, f, ensure_ascii=False, indent=2)
        f.write('\n')


if __name__ == '__main__':
    main()
