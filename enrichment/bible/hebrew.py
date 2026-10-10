#!/usr/bin/env python3
"""Hebrew root and cognate layer of the Bible pass (Bible-owned; reads only enrichment/bible/corpus).

WLC words carry morphhb lemmas (Strong's number + augment letter, e.g. `c/1254 a`); the Open Scriptures Lexical Index
maps each lemma to a lexicon entry and its root; Brown-Driver-Briggs entry heads give the cognate notes. This BDB
edition replaces Arabic, Syriac, Ethiopic … script with a placeholder word (shown here as [Arabic]) but keeps the
glosses, so "BDB cites an Arabic cognate" is known, the Arabic word itself is not.

  hebrew.py build                    corpus/HEBLEX/index.json from the lexicon XML and WLC segments
  hebrew.py root ROOT [--from N]     entries of a Hebrew (or Aramaic) root, BDB heads, every WLC occurrence by book
  hebrew.py cognates "ع ص ر"         Hebrew/Aramaic roots that correspond to an Arabic root by regular sound
                                     correspondences and exist in the lexicon, each labelled with its basis
  hebrew.py word WLC:Gen.1.1         each word of a WLC verse with its lemma, entry, root and gloss
  hebrew.py table "ع ص ر" "خ س ر"    the compact cognate table of several Arabic roots (discovery packages, briefs)

A sound correspondence is a candidate, not proof of cognacy; a shared root is related vocabulary, not borrowing.
Occurrence lists are paged (--from), never cut silently.
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
import threading
from pathlib import Path
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
LEX = HERE / 'corpus' / 'HEBLEX'
RAW = LEX / 'raw'
INDEX = LEX / 'index.json'
WLC = HERE / 'corpus' / 'WLC' / 'segments.jsonl'
NS = '{http://openscriptures.github.com/morphhb/namespace}'
XML_LANG = '{http://www.w3.org/XML/1998/namespace}lang'
PAGE = 400          # occurrences per `root` call; the rest is named with its --from value
FINALS = str.maketrans('ךםןףץ', 'כמנפצ')
LANG_NAME = {'ara': 'Arabic', 'syr': 'Syriac', 'gez': 'Ethiopic', 'akk': 'Assyrian', 'arc': 'Aramaic', 'heb': 'Hebrew'}

# Arabic -> Hebrew / Aramaic consonants (regular Proto-Semitic correspondences). Weak letters depend on position.
AR_HE = {'ء': 'א', 'ب': 'ב', 'ت': 'ת', 'ث': 'ש', 'ج': 'ג', 'ح': 'ח', 'خ': 'ח', 'د': 'ד', 'ذ': 'ז', 'ر': 'ר', 'ز': 'ז',
         'س': 'שס', 'ش': 'ש', 'ص': 'צ', 'ض': 'צ', 'ط': 'ט', 'ظ': 'צט', 'ع': 'ע', 'غ': 'ע', 'ف': 'פ', 'ق': 'ק', 'ك': 'כ',
         'ل': 'ל', 'م': 'מ', 'ن': 'נ', 'ه': 'ה'}
AR_ARC = dict(AR_HE, **{'ث': 'ת', 'ذ': 'ד', 'ض': 'עק', 'ظ': 'ט', 'س': 'שס', 'ش': 'ש'})
WEAK = {('و', 0): 'יו', ('و', 1): 'וי', ('و', 2): 'היו', ('ي', 0): 'י', ('ي', 1): 'יו', ('ي', 2): 'הי',
        ('ء', 0): 'א', ('ء', 1): 'אוי', ('ء', 2): 'אה'}
WEAK_ARC = {('و', 2): 'אהי', ('ي', 2): 'אהי', ('ء', 2): 'אה'}
AR_NORM = str.maketrans({'أ': 'ء', 'إ': 'ء', 'آ': 'ء', 'ؤ': 'ء', 'ئ': 'ء', 'ا': 'ء', 'ٱ': 'ء', 'ى': 'ي', 'ة': 'ت'})


FINAL_OF = {'כ': 'ך', 'מ': 'ם', 'נ': 'ן', 'פ': 'ף', 'צ': 'ץ'}


def show(key: str) -> str:
    """A root key for readers: its last letter in final form (keys are stored with final forms folded)."""
    return key[:-1] + FINAL_OF.get(key[-1], key[-1]) if key else key


def cons(s: str) -> str:
    """Hebrew consonants only, final forms folded."""
    return ''.join(ch for ch in (s or '') if 'א' <= ch <= 'ת').translate(FINALS)


def text_of(el, stop=None) -> str:
    """Element text with <foreign> script placeholders bracketed; stops before the first `stop` child."""
    out = [el.text or '']
    for ch in el:
        tag = ch.tag.replace(NS, '')
        if stop and tag == stop:
            break
        if tag == 'foreign':
            out.append(f"[{ch.text or LANG_NAME.get(ch.get(XML_LANG), '?')}]")
        elif tag != 'status':
            out.append(text_of(ch))
        out.append(ch.tail or '')
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


# ------------------------------------------------------------------------------------------------------------- build
def build() -> None:
    for f in ('LexicalIndex.xml', 'BrownDriverBriggs.xml', 'HebrewStrong.xml'):
        if not (RAW / f).exists():
            raise SystemExit(f'missing {RAW / f}: run fetch/hebrew_lexicon.py first')
    entries, by_strong = {}, {}
    for part in ET.parse(RAW / 'LexicalIndex.xml').getroot().iter(NS + 'part'):
        lang = part.get(XML_LANG)
        for e in part.iter(NS + 'entry'):
            w = e.find(NS + 'w')
            x = e.find(NS + 'xref')
            et = e.find(NS + 'etym')
            rec = {'lang': lang, 'w': (w.text or '').strip() if w is not None else '',
                   'xlit': w.get('xlit', '') if w is not None else '',
                   'pos': (e.findtext(NS + 'pos') or '').strip(), 'def': (e.findtext(NS + 'def') or '').strip(),
                   'strong': x.get('strong') if x is not None else None, 'aug': x.get('aug') if x is not None else None,
                   'bdb': x.get('bdb') if x is not None else None,
                   'etym': (et.get('type'), et.get('root'), (et.text or '').strip()) if et is not None else None}
            entries[e.get('id')] = rec
            if rec['strong']:
                by_strong.setdefault((lang, rec['strong']), []).append(e.get('id'))
    for eid, r in entries.items():
        t = r['etym']
        root = None
        if t and t[1]:
            root = cons(t[1])
        elif t and t[0] == 'sub' and t[2]:
            main = entries.get(t[2].split(',')[0].strip())
            if main:
                root = cons(main['etym'][1]) if main['etym'] and main['etym'][1] else cons(main['w'])
        r['root'] = root
        r['key'] = root or cons(r['w'])
    for r in entries.values():
        del r['etym']
    heads = {}
    for e in ET.parse(RAW / 'BrownDriverBriggs.xml').getroot().iter(NS + 'entry'):
        langs = set()   # cognate languages named in the head only (before the first sense)
        for ch in e:
            if ch.tag == NS + 'sense':
                break
            langs |= {f.get(XML_LANG) for f in ch.iter(NS + 'foreign')}
        st = e.find(NS + 'status')
        heads[e.get('id')] = {'head': text_of(e, stop='sense'), 'status': st.text if st is not None else '',
                              'langs': sorted(x for x in langs if x)}
    strong_def = {}
    for e in ET.parse(RAW / 'HebrewStrong.xml').getroot().iter(NS + 'entry'):
        m = e.find(NS + 'meaning')
        if m is not None:
            strong_def[e.get('id')] = text_of(m)
    occ, unresolved, prefix_only, ambiguous, words = {}, {}, 0, 0, 0
    with WLC.open(encoding='utf-8') as f:
        for line in f:
            r = json.loads(line)
            for t in r.get('tokens', []):
                if t.get('kind') != 'w':
                    continue
                words += 1
                eids, how = lemma_entries(t.get('lemma', ''), t.get('morph', ''), by_strong, entries)
                if how == 'prefix':
                    prefix_only += 1
                    continue
                if not eids:
                    unresolved[t.get('lemma', '')] = unresolved.get(t.get('lemma', ''), 0) + 1
                    continue
                ambiguous += how == 'ambiguous'
                occ.setdefault(eids[0], []).append([r['seg'][4:], t['text']])
    data = {'entries': entries, 'bdb': {k: v for k, v in heads.items()}, 'strong_meaning': strong_def, 'occ': occ,
            'build': {'words': words, 'mapped': sum(map(len, occ.values())), 'prefix_only': prefix_only,
                      'ambiguous_first_entry': ambiguous, 'unresolved': sum(unresolved.values()),
                      'unresolved_lemmas': dict(sorted(unresolved.items(), key=lambda kv: -kv[1]))}}
    INDEX.write_text(json.dumps(data, ensure_ascii=False))
    b = data['build']
    print(f"HEBLEX index: {len(entries)} entries, {words} WLC words, {b['mapped']} mapped to an entry")
    print(f"NOTE: {prefix_only} words have a prefix-only lemma (a preposition with a pronoun suffix); not mapped")
    print(f"NOTE: {ambiguous} words name a Strong's number shared by several entries without an augment letter; "
          f"counted under the first entry")
    if unresolved:
        print(f"WARNING: {b['unresolved']} words ({len(unresolved)} lemmas) map to no lexicon entry: "
              + ', '.join(f'{k}×{v}' for k, v in list(b['unresolved_lemmas'].items())[:30])
              + (' … (all in index.json build.unresolved_lemmas)' if len(unresolved) > 30 else ''))
    print(f'-> {INDEX}')


def lemma_entries(lemma, morph, by_strong, entries):
    last = lemma.split('/')[-1].strip().rstrip('+').strip()
    if not last or not last[0].isdigit():
        return [], 'prefix'
    m = re.fullmatch(r'(\d+)\s*([a-z]?)', last)
    if not m:
        return [], 'bad'
    lang = 'arc' if morph.startswith('A') else 'heb'
    cands = by_strong.get((lang, m[1])) or by_strong.get(('heb' if lang == 'arc' else 'arc', m[1])) or []
    if m[2]:
        hit = [e for e in cands if entries[e]['aug'] == m[2]]
        if hit:
            return hit, 'exact'
    plain = [e for e in cands if not entries[e]['aug']]
    if len(plain) == 1:
        return plain, 'exact'
    if len(cands) == 1:
        return cands, 'exact'
    return (plain or cands), ('ambiguous' if cands else 'none')


# ------------------------------------------------------------------------------------------------------------ lookups
_DATA = None
_DATA_LOCK = threading.Lock()


def data() -> dict:
    """The Hebrew root index with its families; built once, under a lock, and published only when complete
    (recall.py calls it from many threads)."""
    global _DATA
    if _DATA is None:
        with _DATA_LOCK:
            if _DATA is None:
                if not INDEX.exists():
                    raise SystemExit(f'no {INDEX}: run `hebrew.py build`')
                d = json.loads(INDEX.read_text(encoding='utf-8'))
                fam = {}
                for eid, r in d['entries'].items():
                    fam.setdefault((r['lang'], r['key']), []).append(eid)
                d['families'] = fam
                _DATA = d
    return _DATA


def bdb_line(r: dict) -> str:
    h = data()['bdb'].get(r.get('bdb') or '')
    if not h:
        return 'BDB: no entry linked'
    if not h['head'] or len(h['head']) < 3:
        return f"BDB ({r['bdb']}, {h['status']}): no head text in this edition"
    return f"BDB ({r['bdb']}, {h['status']}): {h['head']}"


def entry_line(eid: str) -> str:
    d = data()
    r = d['entries'][eid]
    n = len(d['occ'].get(eid, []))
    strong = f"H{r['strong']}{r['aug'] or ''}" if r['strong'] else 'no Strong'
    sm = d['strong_meaning'].get(f"H{r['strong']}") if r['strong'] else None
    return (f"{r['w']} ({r['xlit']}) {r['pos']} '{r['def']}' [{strong}; {'Aramaic' if r['lang'] == 'arc' else 'Hebrew'}; "
            f"{n} WLC occurrence{'s' if n != 1 else ''}]" + (f" Strong: {sm}" if sm else ''))


def is_header(r: dict) -> bool:
    """A lexicon root heading (no Strong's number, no part of speech): it carries BDB's root note, not a word."""
    return not r['strong'] and not r['pos']


def family(key: str, lang: str | None = None) -> list[str]:
    fam = data()['families']
    return [e for lg in ((lang,) if lang else ('heb', 'arc')) for e in fam.get((lg, key), [])]


def cmd_root(root: str, start: int) -> None:
    key = cons(root)
    eids = family(key)
    if not eids:
        print(f'{root}: no lexicon entry has this root or consonantal form')
        return
    print(f"== root {show(key)}: {len(eids)} lexicon entries")
    for e in eids:
        r = data()['entries'][e]
        if is_header(r):
            print('- root entry: ' + bdb_line(r))
            continue
        print('- ' + entry_line(e))
        print('  ' + bdb_line(r))
    occ = [(o[0], o[1], data()['entries'][e]['w']) for e in eids for o in data()['occ'].get(e, [])]
    order = {b: i for i, b in enumerate(BOOKS)}
    occ.sort(key=lambda o: (order.get(o[0].split('.')[0], 99), *map(int, o[0].split('.')[1:])))
    print(f"== {len(occ)} WLC occurrences (verse surface-form [entry])" + (f", from {start}" if start else ''))
    page = occ[start:start + PAGE]
    book = None
    line = []
    for ref, surf, w in page:
        b = ref.split('.')[0]
        if b != book:
            if line:
                print(' '.join(line))
            book, line = b, [f'{b}:']
        line.append(f"{ref.split('.', 1)[1]} {surf}" + (f'[{w}]' if len(eids) > 1 else '') + ';')
    if line:
        print(' '.join(line))
    if start + PAGE < len(occ):
        print(f'MORE: {len(occ) - start - PAGE} occurrences not shown in this call; continue with '
              f'`hebrew.py root {show(key)} --from {start + PAGE}`')


def ar_letters(ar: str) -> list[str]:
    s = re.sub(r'[ً-ٰٟـ\s,]', '', ar).translate(AR_NORM)
    letters = [ch for ch in s if 'ء' <= ch <= 'ي']
    if not 2 <= len(letters) <= 4:
        raise SystemExit(f'{ar!r}: expected an Arabic root of 2–4 letters')
    return letters


def candidates(ar: str) -> list[tuple[str, str, str]]:
    """(lang, Hebrew/Aramaic key, trace) for every regular correspondence of an Arabic root, existing or not."""
    letters = ar_letters(ar)
    n = len(letters)
    out = []
    for lang, table, weak in (('heb', AR_HE, WEAK), ('arc', AR_ARC, {**WEAK, **WEAK_ARC})):
        opts = []
        for i, ch in enumerate(letters):
            pos = 0 if i == 0 else (2 if i == n - 1 else 1)
            o = weak.get((ch, pos)) or table.get(ch)
            if not o:
                raise SystemExit(f'{ar!r}: no correspondence for {ch!r}')
            opts.append(o)
        seen = set()
        for combo in itertools.product(*opts):
            keys = {''.join(combo)}
            if n == 3 and letters[1] == letters[2]:
                keys.add(''.join(combo[:2]))          # geminate root, written with two radicals
            if n == 3 and letters[1] in 'وي':
                keys.add(combo[0] + combo[2])         # hollow root, written without its middle radical
            if n == 3 and letters[2] in 'وي':
                keys.add(combo[0] + combo[1])         # third-weak root, written with two radicals
            for k in keys - seen:
                seen.add(k)
                out.append((lang, k, ' '.join(f'{a}→{b}' for a, b in zip(letters, combo))))
    return out


def cognates(ar: str) -> list[dict]:
    rows = []
    for lang, key, trace in candidates(ar):
        eids = family(key, lang)
        if not eids:
            continue
        bdb_ar = [e for e in eids if 'ara' in data()['bdb'].get(data()['entries'][e].get('bdb') or '', {}).get('langs', [])]
        rows.append({'lang': lang, 'key': key, 'trace': trace, 'entries': eids,
                     'basis': 'BDB cites an Arabic cognate' if bdb_ar else 'sound correspondence only (unverified)',
                     'occurrences': sum(len(data()['occ'].get(e, [])) for e in eids)})
    rows.sort(key=lambda r: (r['basis'] != 'BDB cites an Arabic cognate', -r['occurrences']))
    return rows


def cmd_cognates(ar: str, full: bool = True) -> list[str]:
    letters = ar_letters(ar)
    rows = cognates(ar)
    out = [f"== Arabic root {' '.join(letters)}: {len(rows)} Hebrew/Aramaic correspondence"
           f"{'s' if len(rows) != 1 else ''} found in the lexicon (regular sound correspondences; a candidate, not proof)"]
    if full:
        out.append('  (BDB heads with status base/ref/made are abridged in this edition and give no cognate notes; '
                   'a missing note is not evidence against cognacy)')
    if not rows:
        out.append('  no Hebrew or Aramaic root with these corresponding consonants is in the lexicon')
    for r in rows:
        out.append(f"* {'Aramaic' if r['lang'] == 'arc' else 'Hebrew'} {show(r['key'])} ({r['trace']}): {r['basis']}; "
                   f"{r['occurrences']} WLC occurrences; `hebrew.py root {show(r['key'])}` lists them")
        for e in r['entries']:
            x = data()['entries'][e]
            if is_header(x):
                if full:
                    out.append('  - root entry: ' + bdb_line(x))
                continue
            out.append('  - ' + entry_line(e))
            if full:
                out.append('    ' + bdb_line(x))
    return out


def cmd_word(loc: str) -> None:
    import sqlite3
    db = HERE / 'corpus' / 'corpus.sqlite'
    con = sqlite3.connect(f'file:{db}?mode=ro', uri=True)
    row = con.execute('SELECT text, extra FROM seg WHERE seg=?', (loc,)).fetchone()
    if not row:
        print(f'== {loc}: NOT FOUND (a WLC locator such as WLC:Gen.1.1)')
        return
    print(f'== {loc}  {row[0]}')
    d = data()
    by_strong = {}
    for eid, r in d['entries'].items():
        if r['strong']:
            by_strong.setdefault((r['lang'], r['strong']), []).append(eid)
    for t in json.loads(row[1]).get('tokens', []):
        if t.get('kind') != 'w':
            continue
        eids, how = lemma_entries(t.get('lemma', ''), t.get('morph', ''), by_strong, d['entries'])
        if how == 'prefix':
            print(f"{t.get('position')}. {t['text']}  lemma {t.get('lemma')} (preposition with suffix)")
        elif not eids:
            print(f"{t.get('position')}. {t['text']}  lemma {t.get('lemma')}: no lexicon entry")
        else:
            r = d['entries'][eids[0]]
            print(f"{t.get('position')}. {t['text']}  lemma {t.get('lemma')} morph {t.get('morph')} -> "
                  f"{entry_line(eids[0])}; root {r['root'] or '(none recorded)'}"
                  + ('  [Strong number shared: first entry shown]' if how == 'ambiguous' else ''))


def table(roots: list[str]) -> str:
    """The cognate table of several Arabic roots, for packages and briefs (entries and basis, no BDB heads)."""
    out = []
    data()  # a missing index stops here, never as a per-root warning
    for ar in roots:
        try:
            out += cmd_cognates(ar, full=False)
        except SystemExit as e:
            out.append(f'== Arabic root {ar}: WARNING {e}')
        out.append('')
    return '\n'.join(out)


ROOT_LABEL = re.compile(r'source:"([ء-ي](?: [ء-ي]){1,3}),B\d+"')


def roots_in(text: str) -> list[str]:
    """Arabic roots a frozen commentary cites through its dictionary labels (source:"ع ص ر,B006")."""
    return sorted(set(ROOT_LABEL.findall(text)))


BOOKS = ['Gen', 'Exod', 'Lev', 'Num', 'Deut', 'Josh', 'Judg', 'Ruth', '1Sam', '2Sam', '1Kgs', '2Kgs', '1Chr', '2Chr',
         'Ezra', 'Neh', 'Esth', 'Job', 'Ps', 'Prov', 'Eccl', 'Song', 'Isa', 'Jer', 'Lam', 'Ezek', 'Dan', 'Hos', 'Joel',
         'Amos', 'Obad', 'Jonah', 'Mic', 'Nah', 'Hab', 'Zeph', 'Hag', 'Zech', 'Mal']


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('build')
    p = sub.add_parser('root'); p.add_argument('root'); p.add_argument('--from', dest='start', type=int, default=0)
    p = sub.add_parser('cognates'); p.add_argument('ar')
    p = sub.add_parser('word'); p.add_argument('loc')
    p = sub.add_parser('table'); p.add_argument('ar', nargs='+')
    a = ap.parse_args()
    if a.cmd == 'build':
        build()
    elif a.cmd == 'root':
        cmd_root(a.root, a.start)
    elif a.cmd == 'cognates':
        print('\n'.join(cmd_cognates(a.ar)))
    elif a.cmd == 'word':
        cmd_word(a.loc)
    else:
        print(table(a.ar))


if __name__ == '__main__':
    main()
