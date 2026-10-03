#!/usr/bin/env python3
"""Elmalılı, Hak Dini Kur'an Dili (YEK critical edition, 6 vols) -- stage 1: PDF -> logical lines.

Reads enrichment/corpus/elmalili/pdf/cilt{1..6}.pdf with pdfminer.six at glyph level and writes, per volume,
enrichment/corpus/ELMALILI/pages/v{n}/lines.jsonl.gz: one JSON object per PDF page

  {"v": 6, "p": 786, "lines": [{"y": 575.2, "x0": 69.4, "x1": 400.1, "sz": 12.0,
                                "sp": [["tr", "olarak zikrolunan ..."], ["sup", "1"], ["quran", "..."]]}, ...]}

Why glyph level: the PDFs store Arabic in *visual* order (presentation forms in vols 1-5, base letters in
vol 6), and pypdf's run positions are unreliable on these files.  Here each glyph keeps its real position;
lines are rebuilt geometrically, combining marks are re-attached to their base glyph, and a small bidi pass
turns every right-to-left stretch back into logical order (digits and brackets fixed), then Arabic
presentation forms are NFKC-normalised.

Span classes: tr (Turkish body/notes), it (italic Garamond), quran (Emine = Qur'an type), ar (other Arabic
type: quotations from tafsir/hadith/poetry), meal (Minion italic = Elmalılı's meal), mhead (Minion bold:
"Meâl-i Şerîfi"), sup (superscript footnote call), sym (Simgeler symbol font), bold.

Usage: elmalili_extract.py [--vols 1,2,...] [--jobs 6]
"""
import argparse
import gzip
import json
import os
import re
import sys
import unicodedata
from multiprocessing import Pool

from pdfminer import glyphlist
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTChar, LTContainer
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

# The Garamond fonts name the ʿayn sign /halfringleft, which is not in the Adobe glyph list.
glyphlist.glyphname2unicode.setdefault('halfringleft', '\u2018')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF_DIR = os.path.join(ROOT, 'enrichment', 'corpus', 'elmalili', 'pdf')
OUT = os.path.join(ROOT, 'enrichment', 'corpus', 'ELMALILI', 'pages')

CID = re.compile(r'\(cid:(\d+)\)')
# Unmapped glyphs of the Arabic fonts (no ToUnicode entry) are kept as private-use code points
# U+F0000 + slot*0x4000 + cid and resolved in stage 2 from the fonts' own ToUnicode tables (fill-down over
# glyph ids: contextual forms follow the isolated form of the same letter in these fonts).
PUA_BASE = 0xF0000
SLOTS = {'TraditionalNaskh': 0, 'TraditionalArabic': 1, 'Emine': 2}


def font_slot(fontname):
    base = fontname.split('+')[-1]
    for k, v in SLOTS.items():
        if k in base:
            return v
    return None
MIRROR = str.maketrans('()[]{}<>«»﴾﴿', ')(][}{><»«﴿﴾')


def is_arabic_letter(c):
    o = ord(c)
    if PUA_BASE <= o < PUA_BASE + 3 * 0x4000:
        return True
    if 0x0660 <= o <= 0x0669 or 0x06F0 <= o <= 0x06F9:
        return False
    return (0x0590 <= o <= 0x06FF or 0x0750 <= o <= 0x077F or 0x08A0 <= o <= 0x08FF
            or 0xFB50 <= o <= 0xFDFF or 0xFE70 <= o <= 0xFEFF)


def is_ar_digit(c):
    o = ord(c)
    return 0x0660 <= o <= 0x0669 or 0x06F0 <= o <= 0x06F9


def is_mark(t):
    return bool(t) and all(unicodedata.category(c) in ('Mn', 'Me') for c in t)


def bidi_class(t):
    """R (Arabic letters), AN (Arabic-Indic digits), L (Latin letters, European digits), N (neutral)."""
    for c in t:
        if is_arabic_letter(c) and (unicodedata.category(c)[0] == 'L' or unicodedata.category(c) == 'Co'):
            return 'R'
    for c in t:
        if is_ar_digit(c):
            return 'AN'
    for c in t:
        if c.isalnum():
            return 'L'
    return 'N'


def font_class(font, size, line_size, text=''):
    f = font.split('+')[-1]
    if size < 0.8 * line_size and 'Emine' not in f and 'Traditional' not in f and 'Naskh' not in f \
            and not any(is_arabic_letter(c) for c in text):
        return 'sup'
    if 'Emine' in f:
        return 'quran'
    if 'Traditional' in f or 'Naskh' in f or 'Arab' in f:
        return 'ar'
    if 'Minion' in f:
        if 'Bold' in f:
            return 'mhead'
        if 'It' in f or f.endswith('Medium'):
            return 'meal'
        return 'tr'
    if 'Simge' in f:
        return 'sym'
    if 'Italic' in f:
        return 'it'
    if 'Bold' in f:
        return 'bold'
    return 'tr'


def iter_chars(obj):
    for o in obj:
        if isinstance(o, LTChar):
            yield o
        elif isinstance(o, LTContainer):
            yield from iter_chars(o)


def page_lines(layout):
    raw = []
    for i, ch in enumerate(iter_chars(layout)):
        slot = font_slot(ch.fontname)
        if slot is None:
            t = CID.sub('\ufffd', ch.get_text())
        else:
            t = CID.sub(lambda m: chr(PUA_BASE + slot * 0x4000 + int(m.group(1)))
                        if int(m.group(1)) < 0x4000 else '\ufffd', ch.get_text())
        t = t.replace('/halfringleft', '‘')
        if not t:
            continue
        raw.append({'i': i, 't': t, 'x0': ch.x0, 'x1': ch.x1, 'y': ch.matrix[5], 'sz': round(ch.size, 1),
                    'f': ch.fontname, 'mk': is_mark(t), 'sp': t.isspace()})
    bases = [c for c in raw if not c['mk'] and not c['sp']]
    if not bases:
        return []
    # --- cluster base glyphs into lines by baseline (gap-based)
    order = sorted(bases, key=lambda c: -c['y'])
    clusters, cur = [], [order[0]]
    for prev, c in zip(order, order[1:]):
        gap = prev['y'] - c['y']
        if gap > 0.3 * max(prev['sz'], c['sz']):
            clusters.append(cur)
            cur = []
        cur.append(c)
    clusters.append(cur)
    # merge clusters made only of small glyphs (superscripts) into the line just below them
    lines = []
    for cl in clusters:
        lines.append({'ch': cl, 'sz': max(c['sz'] for c in cl), 'y': max(cl, key=lambda c: c['sz'])['y']})
    merged = []
    for k, ln in enumerate(lines):
        if k + 1 < len(lines) and len(ln['ch']) <= 6:
            nxt = lines[k + 1]
            if ln['sz'] < 0.8 * nxt['sz'] and 0 < ln['y'] - nxt['y'] < 0.6 * nxt['sz']:
                nxt['ch'].extend(ln['ch'])
                continue
        merged.append(ln)
    lines = merged
    for ln in lines:
        szs = {}
        for c in ln['ch']:
            szs[c['sz']] = szs.get(c['sz'], 0) + len(c['t'])
        ln['body_sz'] = max(szs, key=szs.get)
        base_y = [c['y'] for c in ln['ch'] if c['sz'] == ln['body_sz']]
        ln['y'] = sorted(base_y)[len(base_y) // 2]
    line_of = {}
    for li, ln in enumerate(lines):
        for c in ln['ch']:
            line_of[c['i']] = li
    by_i = {c['i']: c for c in raw}
    idx = [c['i'] for c in raw]
    pos = {ii: k for k, ii in enumerate(idx)}

    def nearest_line(c):
        best, bd = None, 1e9
        for li, ln in enumerate(lines):
            d = abs(ln['y'] - c['y'])
            if d < bd:
                best, bd = li, d
        return best if bd <= 0.6 * max(lines[best]['body_sz'], c['sz']) else None

    # --- spaces: assign to nearest line
    for c in raw:
        if c['sp']:
            li = nearest_line(c)
            if li is not None:
                lines[li].setdefault('spaces', []).append(c)
    # --- marks: attach to the next base glyph in stream order when it is adjacent, else geometric
    for c in raw:
        if not c['mk']:
            continue
        k = pos[c['i']] + 1
        tgt = None
        while k < len(idx):
            n = by_i[idx[k]]
            if n['mk']:
                k += 1
                continue
            if not n['sp'] and n['i'] in line_of and abs(n['y'] - c['y']) < 1.2 * n['sz'] \
                    and n['x0'] - 2.5 <= c['x0'] <= n['x1'] + 2.5:
                tgt = n
            break
        if tgt is None:
            li = nearest_line(c)
            if li is not None:
                cands = [b for b in lines[li]['ch'] if b['x0'] - 1 <= c['x0'] <= b['x1'] + 1]
                if cands:
                    tgt = min(cands, key=lambda b: b['x1'] - b['x0'])
        if tgt is not None:
            tgt.setdefault('marks', []).append(c['t'])
    out = []
    for ln in sorted(lines, key=lambda l: -l['y']):
        items = sorted(ln['ch'] + ln.get('spaces', []), key=lambda c: (round(c['x0'], 1), pos[c['i']]))
        units, pending, prev = [], False, None
        for c in items:
            if c['sp']:
                if prev is not None:
                    pending = True
                continue
            if prev is not None and not pending and c['x0'] - prev['x1'] > 0.3 * max(c['sz'], prev['sz']):
                pending = True
            if pending:
                units.append({'t': ' ', 'b': 'N', 'cls': None})
                pending = False
            t = c['t'] + ''.join(c.get('marks', []))
            units.append({'t': t, 'b': bidi_class(t), 'cls': font_class(c['f'], c['sz'], ln['body_sz'], t),
                          'x1': c['x1']})
            prev = c
        units = bidi(units)
        # spans
        sp = []
        for u in units:
            cls = u['cls']
            t = u['t']
            if any(0xFB50 <= ord(ch) <= 0xFDFF or 0xFE70 <= ord(ch) <= 0xFEFF for ch in t):
                t = unicodedata.normalize('NFKC', t)
            if cls is None:  # space: attach to previous span
                if sp:
                    sp[-1][1] += t
                continue
            if sp and sp[-1][0] == cls:
                sp[-1][1] += t
            else:
                sp.append([cls, t])
        sp = [[c, re.sub(r' {2,}', ' ', t)] for c, t in sp]
        if sp:
            sp[-1][1] = sp[-1][1].rstrip()
        sp = [s for s in sp if s[1]]
        if not sp:
            continue
        xs = [c['x0'] for c in ln['ch']]
        out.append({'y': round(ln['y'], 1), 'x0': round(min(xs), 1),
                    'x1': round(max(c['x1'] for c in ln['ch']), 1), 'sz': ln['body_sz'], 'sp': sp})
    return out


def _reverse_run(units):
    """Reverse a visual-order RTL run into logical order; keep digit sequences LTR; mirror brackets."""
    r = list(reversed(units))
    out, k = [], 0
    while k < len(r):
        if r[k]['b'] in ('AN', 'EN'):
            j = k
            while j < len(r) and r[j]['b'] in ('AN', 'EN'):
                j += 1
            out.extend(reversed(r[k:j]))
            k = j
        else:
            u = r[k]
            if u['b'] == 'N':
                u = dict(u, t=u['t'].translate(MIRROR))
            out.append(u)
            k += 1
    return out


def bidi(units):
    for u in units:
        if u['b'] == 'L' and all(c.isdigit() for c in u['t']):
            u['b'] = 'EN'
    nR = sum(len(u['t']) for u in units if u['b'] == 'R')
    nL = sum(len(u['t']) for u in units if u['b'] == 'L')
    if nR == 0 and not any(u['b'] == 'AN' for u in units):
        return units
    if nL <= max(3, 0.05 * nR):  # right-to-left line (no running Turkish): reverse all, restore LTR stretches
        r = list(reversed(units))
        out, k = [], 0
        while k < len(r):
            if r[k]['b'] in ('L', 'EN', 'AN'):
                j, last = k, k
                while j < len(r) and r[j]['b'] in ('L', 'EN', 'AN', 'N'):
                    if r[j]['b'] in ('L', 'EN', 'AN'):
                        last = j
                    j += 1
                out.extend(reversed(r[k:last + 1]))
                k = last + 1
            else:
                u = r[k]
                if u['b'] == 'N':
                    u = dict(u, t=u['t'].translate(MIRROR))
                out.append(u)
                k += 1
        return out
    # left-to-right line: reverse each maximal Arabic stretch (R/AN with neutrals inside)
    out, k = [], 0
    while k < len(units):
        if units[k]['b'] in ('R', 'AN'):
            j, last = k, k
            while j < len(units) and units[j]['b'] in ('R', 'AN', 'N'):
                if units[j]['b'] in ('R', 'AN'):
                    last = j
                j += 1
            run = units[k:last + 1]
            if all(u['b'] in ('AN', 'N') for u in run):  # bare Arabic-Indic number: already LTR
                out.extend(run)
            else:
                out.extend(_reverse_run(run))
            k = last + 1
        else:
            out.append(units[k])
            k += 1
    return out


def do_volume(vol):
    path = os.path.join(PDF_DIR, f'cilt{vol}.pdf')
    od = os.path.join(OUT, f'v{vol}')
    os.makedirs(od, exist_ok=True)
    rm = PDFResourceManager()
    dev = PDFPageAggregator(rm, laparams=None)
    it = PDFPageInterpreter(rm, dev)
    tmp = os.path.join(od, 'lines.jsonl.gz.tmp')
    n = 0
    with open(path, 'rb') as fh, gzip.open(tmp, 'wt', encoding='utf-8') as out:
        for pno, page in enumerate(PDFPage.get_pages(fh), 1):
            try:
                it.process_page(page)
                lines = page_lines(dev.get_result())
                w, h = page.mediabox[2], page.mediabox[3]
            except Exception as e:  # keep going; record the failure
                print(f'v{vol} p{pno}: {e!r}', file=sys.stderr)
                lines, w, h = [], 0, 0
            out.write(json.dumps({'v': vol, 'p': pno, 'w': round(w, 1), 'h': round(h, 1), 'lines': lines},
                                 ensure_ascii=False) + '\n')
            n += 1
    os.replace(tmp, os.path.join(od, 'lines.jsonl.gz'))
    # ToUnicode tables of the Arabic fonts seen in this volume (for resolving the private-use glyphs)
    maps = {}
    for font in list(getattr(rm, '_cached_fonts', {}).values()):
        slot = font_slot(getattr(font, 'fontname', '') or '')
        um = getattr(font, 'unicode_map', None)
        if slot is None or um is None:
            continue
        d = maps.setdefault(str(slot), {})
        for cid, u in um.cid2unichr.items():
            d.setdefault(str(cid), u)
    with open(os.path.join(od, 'cmaps.json'), 'w', encoding='utf-8') as f:
        json.dump(maps, f, ensure_ascii=False, sort_keys=True)
    return vol, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vols', default='1,2,3,4,5,6')
    ap.add_argument('--jobs', type=int, default=6)
    a = ap.parse_args()
    vols = [int(v) for v in a.vols.split(',')]
    with Pool(min(a.jobs, len(vols))) as pool:
        for vol, n in pool.imap_unordered(do_volume, vols):
            print(f'v{vol}: {n} pages', flush=True)


if __name__ == '__main__':
    main()
