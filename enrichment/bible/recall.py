#!/usr/bin/env python3
"""Bible verses for a focus ayah, the augment9 way (user design, 2026-10-09).

1. recall: per focus ayah, Luna max and Terra max each recall from memory (no reading) Hebrew Bible and New
   Testament verses that say nearly the same thing or the opposite; a fixed follow-up turn in the same session
   asks for omissions. Rows: strength, relation (similar/opposite), OSIS ref (KJV numbering), explanation.
2. merge: union of the readers' rows per ayah; each ref is resolved against the corpus (KJV text, plus WLC/SBLGNT
   at the same reference). A ref the corpus lacks is kept and listed as unresolved, never dropped silently.
3. place: Sol reads the frozen numbered prose and the merged list (with texts) and puts each verse at a paragraph,
   in the closing section, or drops it with a reason. Every listed ref must appear exactly once.
4. preview: Markdown of the prose with the notes after their paragraphs and the closing section.

Production route (user, 2026-10-09): `sol` alone. One Sol session per ayah reads the frozen numbered prose (plus the
ayah's roots table from roots.py, no model call) and places verses from memory under the four ways (prompts/
sol_page.md); turn 2 asks for what it left out; turn 3 in the same session shows the KJV/WLC/SBLGNT text of every
cited verse and takes the final list. The recall/merge/place steps above are the earlier test route.

  recall.py sol     --surah S --tag T --ayat S:A,S:A [--parallel 3] --effort max
  recall.py recall  --surah S --tag T --ayat S:A,S:A [--models luna,terra] [--parallel 6] [--prose]
  recall.py merge   --surah S --tag T
  recall.py place   --surah S --tag T [--parallel 3] [--effort high]
  recall.py check   --surah S --tag T
  recall.py preview --surah S --tag T
  recall.py report  --surah S --tag T
Work lives in enrichment/bible/work/sSSS/recall/T/<S_A>/. Costs are API-equivalent (codexrun.RATES); a model
without a saved rate reports its tokens and 'no saved rate'.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import re
import sqlite3
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
from enrichment.bible import codexrun as CR  # noqa: E402

MODELS = {'luna': 'gpt-6-luna', 'terra': 'gpt-5.6-terra', 'sol': 'gpt-6-sol'}
QTEXT = ROOT.parent / 'quran-data' / 'data' / 'text' / 'quran-uthmani.tsv'
INDEX = HERE / 'corpus' / 'corpus.sqlite'
OSIS = re.compile(r'^([1-4]?[A-Z][A-Za-z]{1,6})\.(\d+)\.(\d+)$')
LOOSE = re.compile(r'^([1-4]?\s*[A-Za-z][A-Za-z ]*?)\s*[.\s]\s*(\d+)\s*[.:]\s*(\d+)$')
BOOK_CODES = None


def osis(ref: str) -> str | None:
    """The OSIS form of a reference written with an OSIS code, a Paratext code (Psa.8.4, ECC 1:2) or a full English
    book name (Hebrews.10.24, 1 Peter 1:22, Song of Solomon 2:1), or None."""
    global BOOK_CODES
    if BOOK_CODES is None:
        from enrichment.bible.discovery import BOOK_CODES as B
        from enrichment.bible.fetch.bible_text import USFM
        BOOK_CODES = {**{k.casefold(): v for k, v in USFM.items()},       # Paratext codes: PSA, ECC, JHN …
                      **{v.casefold(): v for v in USFM.values()},          # OSIS codes in any case
                      **B, 'songofsolomon': 'Song', 'songofsongs': 'Song', 'psalm': 'Ps', 'canticles': 'Song',
                      'pss': 'Ps', 'qoh': 'Eccl', 'mat': 'Matt', 'mk': 'Mark', 'lk': 'Luke', 'rm': 'Rom'}
        for amb in ('jud', 'sol', 'jn'):   # Judges/Jude, Song/Wisdom, John/Jonah: never guessed (None is reported)
            BOOK_CODES.pop(amb, None)
    m = LOOSE.match(ref.strip())
    if not m:
        return None
    code = BOOK_CODES.get(re.sub(r'\s+', '', m[1]).casefold())
    return f'{code}.{int(m[2])}.{int(m[3])}' if code else None
STRENGTH = ('strong', 'medium', 'weak')
RELATION = ('similar', 'opposite')
WAYS = ('same', 'opposite', 'background', 'word')     # per-paragraph brief (recall_par.md)
FOLLOWUP = ('Review your recall once more for verses that qualify under the same rules and are not in your list yet: '
            'the other Testament, other books, other distinct claims or images of the ayah, and verses that say the '
            'opposite. Reply only with the new rows, in the same four-field TSV. Zero rows is a valid answer. Answer '
            'from memory only; do not read files, run commands or search.')
FOLLOWUP_PAR = ('Go through the paragraphs once more for verses that would help a reader understand them and are not in '
                'your list yet: paragraphs you gave few or no rows, images and customs whose background the Bible shows, '
                'words whose Hebrew or Aramaic relatives it uses, and verses that say a paragraph\'s point the other way '
                'round. Reply only with the new rows, in the same five-field TSV. Zero rows is a valid answer. Answer '
                'from memory only; do not read files, run commands or search.')
OT = set('Gen Exod Lev Num Deut Josh Judg Ruth 1Sam 2Sam 1Kgs 2Kgs 1Chr 2Chr Ezra Neh Esth Job Ps Prov Eccl Song Isa '
         'Jer Lam Ezek Dan Hos Joel Amos Obad Jonah Mic Nah Hab Zeph Hag Zech Mal'.split())


def key(ref: str) -> str:
    return ref.replace(':', '_')


def run_dir(s: int, tag: str) -> Path:
    return HERE / 'work' / f's{s:03d}' / 'recall' / tag


def quran() -> dict:
    out = {}
    for line in QTEXT.read_text(encoding='utf-8').splitlines():
        ref, _, text = line.partition('|')
        out[ref] = text.lstrip('﻿')
    return out


def parse(text: str) -> tuple[list[dict], list[str]]:
    """Rows and the problems of a reader's reply (every malformed line is reported, none skipped silently)."""
    rows, bad = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        f = [x.strip() for x in line.split('\t')]
        if len(f) == 5 and f[0].lstrip('¶').isdigit():          # per-paragraph brief
            par, way, st, ref, ex = f
            way, st = way.lower(), st.lower()
            if way not in WAYS or st not in STRENGTH or not osis(ref):
                bad.append(f'bad way/strength/ref: {line[:120]}')
                continue
            rows.append(dict(paragraph=int(par.lstrip('¶')), relation=way, strength=st, ref=osis(ref), explanation=ex))
            continue
        if len(f) != 4:
            bad.append(f'not four fields: {line[:120]}')
            continue
        st, rel, ref, ex = f
        st, rel = st.lower(), rel.lower()
        if st not in STRENGTH or rel not in RELATION or not osis(ref):
            bad.append(f'bad strength/relation/ref: {line[:120]}')
            continue
        ref = osis(ref)
        rows.append(dict(strength=st, relation=rel, ref=ref, explanation=ex))
    return rows, bad


def commentary(s: int, ayah: str, prose: bool) -> str:
    if not prose:
        return ''
    text = (HERE / 'work' / f's{s:03d}' / 'pack' / 'numbered' / f'{key(ayah)}.md').read_text()
    return ('A Turkish commentary on the focus ayah, showing how it is read here. Cover the claims, images and '
            'readings it develops as well as the ayah itself:\n\n' + text.strip() + '\n\n')


def one_recall(s: int, tag: str, ayah: str, model: str, q: dict, prose: bool = False, brief: str = 'ayah') -> str:
    d = run_dir(s, tag) / key(ayah) / model
    if (d / 'rows.json').exists():
        return f'{ayah} {model}: done already'
    d.mkdir(parents=True, exist_ok=True)
    surah = '\n'.join(f'{r} {t}' for r, t in q.items() if r.split(':')[0] == str(s) and not r.endswith(':0'))
    if brief == 'par':
        com = (HERE / 'work' / f's{s:03d}' / 'pack' / 'numbered' / f'{key(ayah)}.md').read_text().strip()
        tmpl, follow = 'recall_par.md', FOLLOWUP_PAR
    else:
        com, tmpl, follow = commentary(s, ayah, prose), 'recall.md', FOLLOWUP
    prompt = ((HERE / 'prompts' / tmpl).read_text().replace('{{REF}}', ayah).replace('{{ARABIC}}', q[ayah])
              .replace('{{SURAH}}', str(s)).replace('{{SURAH_TEXT}}', surah).replace('{{COMMENTARY}}', com))
    (d / 'prompt.md').write_text(prompt)
    t1 = CR.turn(d, 1, prompt, MODELS[model], 'max')
    if not t1['completed'] or not t1['thread_id']:
        return f'ERROR {ayah} {model}: turn 1 did not complete (rc {t1["returncode"]}); see {d}'
    t2 = CR.turn(d, 2, follow, MODELS[model], 'max', thread=t1['thread_id'])
    if not t2['completed'] or t2.get('error'):
        return f'ERROR {ayah} {model}: follow-up did not complete ({t2.get("error") or t2["returncode"]}); see {d}'
    r1, b1 = parse((d / 'turn1.last.txt').read_text())
    r2, b2 = parse((d / 'turn2.last.txt').read_text())
    for r in r1:
        r['turn'] = 1
    for r in r2:
        r['turn'] = 2
    tools = sum(1 for n in (1, 2) for line in (d / f'turn{n}.stream.jsonl').read_text().splitlines()
                if '"command_execution"' in line and '"item.started"' in line)
    try:
        cost = CR.cost(CR.rollout(t1['thread_id']))
    except ValueError as e:
        cost = {'usd_equivalent': None, 'note': str(e), **{f'total_{k}': (t1['usage'].get(k, 0) + t2['usage'].get(k, 0))
                                                         for k in CR.KEYS}}
    (d / 'rows.json').write_text(json.dumps(dict(ayah=ayah, model=MODELS[model], effort='max', brief=brief, rows=r1 + r2,
                                                 malformed=b1 + b2, tool_calls=tools, cost=cost),
                                            ensure_ascii=False, indent=1) + '\n')
    usd = cost.get('usd_equivalent')
    return (f'{ayah} {model}: {len(r1)}+{len(r2)} rows, {len(b1 + b2)} malformed, {tools} tool calls, '
            + (f'${usd:.3f}' if usd is not None else f"no saved rate ({cost.get('total_output_tokens')} output tokens)"))


def cmd_recall(a):
    q = quran()
    ayat = a.ayat.split(',')
    for x in ayat:
        if x not in q or int(x.split(':')[0]) != a.surah:
            raise SystemExit(f'{x}: not an ayah of surah {a.surah}')
    jobs = [(x, m) for x in ayat for m in a.models.split(',')]
    with cf.ThreadPoolExecutor(a.parallel) as ex:
        for msg in ex.map(lambda j: one_recall(a.surah, a.tag, j[0], j[1], q, a.prose, a.brief), jobs):
            print(msg, flush=True)


# English (KJV) -> Hebrew (WLC) verse numbers: versification/eng.json, the Copenhagen Alliance standard mapping
# (github.com/Copenhagen-Alliance/versification-specification, versification-mappings/standard-mappings/eng.json,
# fetched 2026-10-09). Paratext book codes in the OT order of OT above.
PT_OT = ('GEN EXO LEV NUM DEU JOS JDG RUT 1SA 2SA 1KI 2KI 1CH 2CH EZR NEH EST JOB PSA PRO ECC SNG ISA JER LAM EZK DAN '
         'HOS JOL AMO OBA JON MIC NAM HAB ZEP HAG ZEC MAL').split()
ENG_TO_MT = None


def mt_ref(ref: str) -> str:
    """The WLC reference of a KJV-numbered Hebrew Bible verse (the same reference where the numbering agrees)."""
    global ENG_TO_MT
    if ENG_TO_MT is None:
        osis_of = dict(zip(PT_OT, [b for b in 'Gen Exod Lev Num Deut Josh Judg Ruth 1Sam 2Sam 1Kgs 2Kgs 1Chr 2Chr Ezra '
                                   'Neh Esth Job Ps Prov Eccl Song Isa Jer Lam Ezek Dan Hos Joel Amos Obad Jonah Mic Nah '
                                   'Hab Zeph Hag Zech Mal'.split()]))
        rng = re.compile(r'^([1-4A-Z]{3}) (\d+):(\d+)(?:-(\d+))?$')
        ENG_TO_MT = {}
        for k, v in json.loads((HERE / 'versification' / 'eng.json').read_text())['mappedVerses'].items():
            a, b = rng.match(k), rng.match(v)
            if not (a and b and a[1] in osis_of and b[1] in osis_of):
                continue
            ea, eb = int(a[3]), int(a[4] or a[3])
            ma, mb = int(b[3]), int(b[4] or b[3])
            if eb - ea != mb - ma:
                raise ValueError(f'versification/eng.json: {k} = {v} has ranges of different length')
            for i in range(eb - ea + 1):
                if ea + i > 0:
                    ENG_TO_MT[f'{osis_of[a[1]]}.{a[2]}.{ea + i}'] = f'{osis_of[b[1]]}.{b[2]}.{ma + i}'
    return ENG_TO_MT.get(ref, ref)


def texts(db, ref: str) -> dict:
    """KJV and TURNTB (Kutsal Kitap 2009, English numbering) at the KJV reference; WLC at the Hebrew-numbered
    reference (key 'WLC_ref' when it differs); SBLGNT at the same reference."""
    book = OSIS.match(ref)[1]
    out = {}
    for src, r2 in (('KJV', ref), ('TURNTB', ref), ('WLC', mt_ref(ref)) if book in OT else ('SBLGNT', ref)):
        r = db.execute('select text, extra from seg where seg = ?', (f'{src}:{r2}',)).fetchone()
        if r:
            out[src] = r[0]
            if src == 'TURNTB' and r[1] and json.loads(r[1]).get('bridge'):
                out['TURNTB_bridge'] = json.loads(r[1])['bridge']   # the translation joins this verse with others
            if r2 != ref:
                out[f'{src}_ref'] = r2
    return out


def reparse(f: Path) -> None:
    """Rebuild a reader's rows from its saved replies (after a parser change); cost and tool counts are kept."""
    r = json.loads(f.read_text())
    r1, b1 = parse((f.parent / 'turn1.last.txt').read_text())
    r2, b2 = parse((f.parent / 'turn2.last.txt').read_text())
    for x in r1:
        x['turn'] = 1
    for x in r2:
        x['turn'] = 2
    r['rows'], r['malformed'] = r1 + r2, b1 + b2
    f.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')


def cmd_merge(a):
    for f in run_dir(a.surah, a.tag).glob('*/*/rows.json'):
        reparse(f)
    db = sqlite3.connect(INDEX)
    for ad in sorted(p for p in run_dir(a.surah, a.tag).iterdir() if p.is_dir()):
        readers = sorted(ad.glob('*/rows.json'))
        merged = {}
        for f in readers:
            r = json.loads(f.read_text())
            for row in r['rows']:
                m = merged.setdefault(row['ref'], dict(ref=row['ref'], readers=[], strength=row['strength'],
                                                        relations=[], notes=[], paragraphs=[]))
                if row.get('paragraph') is not None and row['paragraph'] not in m['paragraphs']:
                    m['paragraphs'].append(row['paragraph'])
                rd = f.parent.name
                if rd not in m['readers']:
                    m['readers'].append(rd)
                if STRENGTH.index(row['strength']) < STRENGTH.index(m['strength']):
                    m['strength'] = row['strength']
                if row['relation'] not in m['relations']:
                    m['relations'].append(row['relation'])
                m['notes'].append(f"{rd}" + (f" (¶{row['paragraph']})" if row.get('paragraph') is not None else '')
                                  + f": {row['explanation']}")
        if a.roots:
            for f in sorted((HERE / 'work' / f's{a.surah:03d}' / 'roots' / a.roots / ad.name).glob('*/rows.json')):
                r = json.loads(f.read_text())
                cog = {x['ar']: x for x in r['rows'] if x['kind'] == 'root'}
                for row in r['rows']:
                    if row['kind'] != 'verse' or row.get('check') not in ('verified', 'nearby'):
                        continue
                    c = cog.get(row['ar'], {})
                    m = merged.setdefault(row['ref'], dict(ref=row['ref'], readers=[], strength='medium', relations=[],
                                                            notes=[], paragraphs=[]))
                    rd = f'roots-{f.parent.name}'
                    if rd not in m['readers']:
                        m['readers'].append(rd)
                    if 'word' not in m['relations']:
                        m['relations'].append('word')
                    m['notes'].append(f"{rd}: Arabic {row['ar']} ~ Hebrew {c.get('he')} ({c.get('relation')}: "
                                      f"{c.get('note', '')}) {row['explanation']}"
                                      + (f" [Hebrew text has the root at WLC {row['wlc_ref']}]" if row.get('wlc_ref') else ''))
        items = sorted(merged.values(), key=lambda m: (STRENGTH.index(m['strength']), -len(m['readers'])))
        unresolved = []
        for m in items:
            m['text'] = texts(db, m['ref'])
            if 'KJV' not in m['text']:
                unresolved.append(m['ref'])
        (ad / 'merged.json').write_text(json.dumps(dict(ayah=ad.name.replace('_', ':'), readers=[f.parent.name for f in readers],
                                                        items=items, unresolved=unresolved),
                                                   ensure_ascii=False, indent=1) + '\n')
        both = sum(len(m['readers']) > 1 for m in items)
        print(f"{ad.name}: {len(items)} refs ({both} from both readers), {len(unresolved)} unresolved"
              + (f': {unresolved}' if unresolved else ''))


def verses_block(items: list[dict]) -> str:
    out = []
    for m in items:
        rel = '/'.join(m['relations'])
        hint = f"; readers' paragraph hint: {', '.join('¶' + str(p) for p in m['paragraphs'])}" if m.get('paragraphs') else ''
        lines = [f"### {m['ref']} ({m['strength']}, {rel}{hint})"]
        if 'KJV' in m['text']:
            lines.append(f"KJV: {m['text']['KJV']}")
        else:
            lines.append('KJV: (not in the corpus under this reference; judge it from the readers\' notes and your '
                         'own knowledge, and drop it if you cannot confirm what it says)')
        for src in ('WLC', 'SBLGNT'):
            if src in m['text']:
                lines.append(f"{src}: {m['text'][src]}")
        lines += [f'- {n}' for n in m['notes']]
        out.append('\n'.join(lines))
    return '\n\n'.join(out)


def one_place(s: int, tag: str, ad: Path, effort: str) -> str:
    d = ad / 'sol'
    if (d / 'placed.json').exists():
        return f'{ad.name} sol: done already'
    merged = json.loads((ad / 'merged.json').read_text())
    prose = (HERE / 'work' / f's{s:03d}' / 'pack' / 'numbered' / f'{ad.name}.md').read_text()
    prompt = ((HERE / 'prompts' / 'place.md').read_text().replace('{{REF}}', merged['ayah'])
              .replace('{{PROSE}}', prose).replace('{{VERSES}}', verses_block(merged['items'])))
    d.mkdir(parents=True, exist_ok=True)
    (d / 'prompt.md').write_text(prompt)
    t = CR.turn(d, 1, prompt, MODELS['sol'], effort)
    if not t['completed']:
        return f'ERROR {ad.name} sol: turn did not complete (rc {t["returncode"]}); see {d}'
    rows, bad = [], []
    for line in (d / 'turn1.last.txt').read_text().splitlines():
        if line.strip():
            try:
                rows.append(json.loads(line))
            except ValueError:
                bad.append(line[:160])
    cost = CR.cost(CR.rollout(t['thread_id']))
    (d / 'placed.json').write_text(json.dumps(dict(ayah=merged['ayah'], model=MODELS['sol'], effort=effort, rows=rows,
                                                   malformed=bad, cost=cost), ensure_ascii=False, indent=1) + '\n')
    return f"{ad.name} sol: {len(rows)} rows, {len(bad)} malformed, ${cost['usd_equivalent']:.3f}; " + check_one(ad)


OMISSIONS_TURN = ('Go through the paragraphs once more for verses you have not listed yet that pass the same test: verses '
                  'that state a paragraph\'s point the other way round, so the difference shows what is distinctive here; '
                  'words a paragraph discusses whose Hebrew or Aramaic relatives in the roots table the Bible uses in a way '
                  'that makes the paragraph clearer; images, customs and practices whose background the Bible shows, even '
                  'with no shared word; and paragraphs you gave few or no verses. Reply only with the new rows, in the same '
                  'JSON Lines form, drop rows included. Zero rows is a valid answer. Work from memory; do not read files, '
                  'run commands or search.')
CHECK_TURN = ('Below is the text of every verse you cited: KJV, and the Hebrew (WLC) or Greek (SBLGNT) text at the same '
              'reference when available. The Hebrew text is given at its own verse number where that differs from the KJV\'s. '
              ' Check each row against these texts: does the verse say what your note says, and '
              'does it still pass the test? Then reply with your complete final list in the same JSON Lines form, every '
              'verse of your earlier replies exactly once: keep a row, correct its note or paragraph, or turn it into a drop '
              'row with the reason. If a reference was wrong and you are sure of the right one, put the right one in '
              '`refs` and the wrong one in `"was": [...]`. Do not add new verses. Do not read files, run commands or '
              'search.\n\n=== VERSES ===\n\n')


def jsonl(text: str) -> tuple[list[dict], list[str]]:
    """Rows of a JSON Lines reply with refs in OSIS form; every unreadable line or ref is reported."""
    rows, bad = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except ValueError:
            bad.append(line[:160])
            continue
        if not isinstance(r, dict):
            bad.append(f'not a JSON object: {line[:140]}')
            continue
        for k in ('refs', 'was'):
            if k in r:
                if not isinstance(r[k], list) or not all(isinstance(x, str) for x in r[k]):
                    bad.append(f'"{k}" is not a list of references: {line[:120]}')
                    r[k] = [x for x in r[k] if isinstance(x, str)] if isinstance(r[k], list) else []
                bad += [f'unknown or ambiguous book code: {x}' for x in r[k] if osis(x) is None]
                fixed = [osis(x) or x for x in r[k]]
                bad += [f'not an OSIS ref: {x}' for x in fixed if not OSIS.match(x)]
                r[k] = fixed
        rows.append(r)
    return rows, bad


def resume_turn(d: Path, n: int, text: str, effort: str, thread: str | None = None) -> dict:
    """Turn n of a Sol session: reuse a completed turn, set aside a started-but-unfinished one (its files move to
    turnN.failed-K.*, printed), then run it. Never starts a completed turn twice."""
    rec = d / f'turn{n}.run.json'
    if rec.exists():
        r = json.loads(rec.read_text())
        if r.get('completed') and not r.get('error') and (d / f'turn{n}.last.txt').exists():
            return r
    if (d / f'turn{n}.stream.jsonl').exists():
        k = 1 + len(list(d.glob(f'turn{n}.failed-*.stream.jsonl')))
        for f in list(d.glob(f'turn{n}.*')):
            if '.failed-' not in f.name:
                f.rename(d / f.name.replace(f'turn{n}.', f'turn{n}.failed-{k}.', 1))
        print(f'NOTE {d}: unfinished turn {n} set aside as turn{n}.failed-{k}.*; running it again', flush=True)
    return CR.turn(d, n, text, MODELS['sol'], effort, thread=thread)


def one_sol(s: int, tag: str, ayah: str, effort: str, q: dict) -> str:
    """The single Sol session of an ayah: turn 1 places from memory, turn 2 adds what it left out (other way round,
    word, background, thin paragraphs), turn 3 checks every cited verse against its text and gives the final list."""
    from enrichment.bible import roots as RT
    ad = run_dir(s, tag) / key(ayah)
    d = ad / 'sol'
    if (d / 'placed.json').exists():
        return f'{ayah} sol: done already'
    d.mkdir(parents=True, exist_ok=True)
    prose = (HERE / 'work' / f's{s:03d}' / 'pack' / 'numbered' / f'{key(ayah)}.md').read_text().strip()
    prompt = ((HERE / 'prompts' / 'sol_page.md').read_text().replace('{{REF}}', ayah).replace('{{ARABIC}}', q[ayah])
              .replace('{{ROOTS}}', RT.table_text(RT.ayah_roots(ayah)).strip()).replace('{{PROSE}}', prose))
    (d / 'prompt.md').write_text(prompt)
    t1 = resume_turn(d, 1, prompt, effort)
    if not t1['completed'] or not t1['thread_id']:
        return f'ERROR {ayah} sol: turn 1 did not complete (rc {t1["returncode"]}); see {d}'
    t2 = resume_turn(d, 2, OMISSIONS_TURN, effort, t1['thread_id'])
    if not t2['completed'] or t2.get('error'):
        return f'ERROR {ayah} sol: omissions turn did not complete ({t2.get("error") or t2["returncode"]}); see {d}'
    r1, b1 = jsonl((d / 'turn1.last.txt').read_text())
    r2, b2 = jsonl((d / 'turn2.last.txt').read_text())
    for r in r2:
        r['turn'] = 2
    r1, b1 = r1 + r2, b1 + b2
    cited = list(dict.fromkeys(x for r in r1 for x in r.get('refs') or [] if OSIS.match(x)))
    db = sqlite3.connect(INDEX)
    shown = [dict(ref=x, text=texts(db, x)) for x in cited]
    block = '\n\n'.join(f"### {m['ref']}\n" + '\n'.join(
        [f"KJV: {m['text'].get('KJV', '(not in our corpus under this reference; drop it unless you are sure what it says)')}"]
        + [f"{src}{' (Hebrew numbering ' + m['text'][src + '_ref'] + ')' if src + '_ref' in m['text'] else ''}: {m['text'][src]}"
           for src in ('WLC', 'SBLGNT') if src in m['text']]) for m in shown)
    t3 = resume_turn(d, 3, CHECK_TURN + block, effort, t1['thread_id'])
    if not t3['completed'] or t3.get('error'):
        return f'ERROR {ayah} sol: check turn did not complete ({t3.get("error") or t3["returncode"]}); see {d}'
    rows, bad = jsonl((d / 'turn3.last.txt').read_text())
    cost = CR.cost(CR.rollout(t1['thread_id']))
    (ad / 'cited.json').write_text(json.dumps(dict(ayah=ayah, turn1_rows=r1, turn1_malformed=b1, turn2_new=len(r2), shown=shown,
                                                   unresolved=[m['ref'] for m in shown if 'KJV' not in m['text']]),
                                              ensure_ascii=False, indent=1) + '\n')
    (d / 'placed.json').write_text(json.dumps(dict(ayah=ayah, model=MODELS['sol'], effort=effort, brief='sol_page',
                                                   rows=rows, malformed=bad, cost=cost),   # turns 1-2: cited.json
                                              ensure_ascii=False, indent=1) + '\n')
    return f"{ayah} sol: {len(r1) - len(r2)}+{len(r2)} -> {len(rows)} rows, ${cost['usd_equivalent']:.3f}; " + check_one(ad)


RECHECK_TURN = ('Some verses in your final list were not shown to you with their text (their references were not '
                'resolved). Below is the text of each: KJV, and the Hebrew (WLC) or Greek (SBLGNT) text, the Hebrew at '
                'its own verse number where that differs from the KJV\'s. Check those rows as before: does the verse say '
                'what your note says, and does it still pass the test? Then reply with your complete final list again in '
                'the same JSON Lines form, every verse of your last reply exactly once, with references in OSIS form '
                '(Book.Chapter.Verse, e.g. Ps, Eccl, Song, Matt). Do not add new verses. Do not read files, run commands '
                'or search.\n\n=== VERSES ===\n\n')


def text_block(shown: list[dict]) -> str:
    return '\n\n'.join(f"### {m['ref']}\n" + '\n'.join(
        [f"KJV: {m['text'].get('KJV', '(not in our corpus under this reference; drop it unless you are sure what it says)')}"]
        + [f"{src}{' (Hebrew numbering ' + m['text'][src + '_ref'] + ')' if src + '_ref' in m['text'] else ''}: {m['text'][src]}"
           for src in ('WLC', 'SBLGNT') if src in m['text']]) for m in shown)


def one_recheck(s: int, tag: str, ayah: str, effort: str) -> str:
    """Same-session repair: show Sol the text of every final verse it was not shown, take the final list again."""
    ad = run_dir(s, tag) / key(ayah)
    d = ad / 'sol'
    c = json.loads((ad / 'cited.json').read_text())
    placed = json.loads((d / 'placed.json').read_text())
    db = sqlite3.connect(INDEX)
    seen = {osis(m['ref']) or m['ref'] for m in c['shown'] if 'KJV' in texts(db, osis(m['ref']) or m['ref'])
            and m['text'].get('KJV')}
    todo = list(dict.fromkeys(osis(x) or x for r in placed['rows'] if r.get('decision') != 'drop'
                              for x in r.get('refs') or [] if (osis(x) or x) not in seen))
    if not todo:
        return f'{ayah}: nothing to recheck'
    shown = [dict(ref=x, text=texts(db, x)) for x in todo if OSIS.match(x)]
    done = [int(f.name[4:].split('.')[0]) for f in d.glob('turn*.run.json') if '.failed-' not in f.name
            and json.loads(f.read_text()).get('completed')]
    n = max(done) + 1
    thread = json.loads((d / 'turn1.run.json').read_text())['thread_id']
    t = resume_turn(d, n, RECHECK_TURN + text_block(shown), effort, thread)
    if not t['completed'] or t.get('error'):
        return f'ERROR {ayah} sol: recheck turn {n} did not complete ({t.get("error") or t["returncode"]}); see {d}'
    rows, bad = jsonl((d / f'turn{n}.last.txt').read_text())
    (d / f'placed.turn{n - 1}.json').write_text((d / 'placed.json').read_text())
    for m in c['shown']:
        m['ref'] = osis(m['ref']) or m['ref']
        m['text'] = texts(db, m['ref'])
    have = {m['ref'] for m in c['shown']}
    c['shown'] += [m for m in shown if m['ref'] not in have]
    c['unresolved'] = [m['ref'] for m in c['shown'] if 'KJV' not in m['text']]
    c['rechecked'] = c.get('rechecked', []) + [dict(turn=n, refs=todo)]
    (ad / 'cited.json').write_text(json.dumps(c, ensure_ascii=False, indent=1) + '\n')
    placed.update(rows=rows, malformed=bad, cost=CR.cost(CR.rollout(thread)))
    (d / 'placed.json').write_text(json.dumps(placed, ensure_ascii=False, indent=1) + '\n')
    return f"{ayah} recheck turn {n}: {len(todo)} verse(s) shown, {len(rows)} rows, total ${placed['cost']['usd_equivalent']:.3f}; " + check_one(ad)


def cmd_recheck(a):
    for x in a.ayat.split(','):
        if x:
            print(one_recheck(int(x.split(':')[0]), a.tag, x, a.effort), flush=True)


def live_sol(tag: str, exclude: set[str]) -> int:
    """codex processes of this tag's Sol calls (their -o path names the call directory), other than `exclude` keys."""
    import subprocess
    ps = subprocess.run(['ps', '-ax', '-o', 'command='], capture_output=True, text=True, check=True).stdout
    mark = f'/recall/{tag}/'
    return len({l.split(mark)[1].split('/')[0] for l in ps.splitlines() if 'codex' in l and mark in l} - exclude)


def cmd_sol(a):
    """Ayat may come from several surahs (--ayat 96:1,87:1,...; --surah is then ignored). With --cap N, an ayah starts
    only while fewer than N Sol calls of this tag are live, counting calls started by other processes."""
    import threading
    import time
    q = quran()
    ayat = [x for x in a.ayat.split(',') if x]
    for x in ayat:
        if x not in q:
            raise SystemExit(f'{x}: not an ayah')
    if a.cap:
        own, lock, mine = set(), threading.Lock(), {key(x) for x in ayat}

        def gated(x):
            while True:
                with lock:
                    if len(own) + live_sol(a.tag, mine) < a.cap:
                        own.add(x)
                        break
                time.sleep(20)
            try:
                return one_sol(int(x.split(':')[0]), a.tag, x, a.effort, q)
            except Exception as e:  # one ayah's failure is reported, never stops the others
                return f'ERROR {x} sol: {type(e).__name__}: {e}'
            finally:
                with lock:
                    own.discard(x)
        work, n = gated, a.cap
    else:
        def work(x):
            try:
                return one_sol(int(x.split(':')[0]), a.tag, x, a.effort, q)
            except Exception as e:
                return f'ERROR {x} sol: {type(e).__name__}: {e}'
        n = a.parallel
    with cf.ThreadPoolExecutor(n) as ex:
        for msg in ex.map(work, ayat):
            print(msg, flush=True)


def check_one(ad: Path) -> str:
    """Single-Sol runs: every verse of turn 1 must have a final decision (directly or via `was`), and every final
    verse must be one whose text Sol was shown. Placement runs: every merged verse must have a decision."""
    placed = json.loads((ad / 'sol' / 'placed.json').read_text())
    paras = set(map(int, re.findall(r'\[¶(\d+)\]', (HERE / 'work' / f"s{int(ad.name.split('_')[0]):03d}" / 'pack'
                                                     / 'numbered' / f'{ad.name}.md').read_text())))
    seen, problems, notes = {}, [], []
    if (ad / 'cited.json').exists():
        c = json.loads((ad / 'cited.json').read_text())
        listed = {osis(m['ref']) or m['ref'] for m in c['shown']}                       # every verse of turns 1-2
        texted = {osis(m['ref']) or m['ref'] for m in c['shown'] if m['text'].get('KJV')}
        for r in placed['rows']:
            r['refs'] = [osis(x) or x for x in r.get('refs') or []]
        final = {x for r in placed['rows'] for x in r['refs']}
        # a `was` counts only on a row that names its replacement in the same book; one naming a kept ref removes nothing
        was = set()
        for r in placed['rows']:
            for x in {osis(y) or y for y in r.get('was') or []} - final:
                if r['refs'] and any(y.split('.')[0] == x.split('.')[0] for y in r['refs']):
                    was.add(x)
                elif r['refs']:
                    problems.append(f"{x}: replaced via was by {r['refs']} from another book (no decision for it)")
        for r in placed['rows']:
            if r.get('was') and not r['refs']:
                problems.append(f"row with was {r['was']} names no replacement")
            for ref in r['refs']:
                if ref not in texted and r.get('decision') != 'drop':
                    problems.append(f'{ref}: final verse whose text Sol was not shown')
                if ref not in listed:
                    r['added'] = True
        listed -= was
        if was:
            notes.append(f'NOTE {len(was)} reference(s) replaced via was: {sorted(was)[:6]}')
    else:
        listed = {m['ref'] for m in json.loads((ad / 'merged.json').read_text())['items']}
    for i, r in enumerate(placed['rows']):
        dec = r.get('decision')
        if not r.get('refs'):
            problems.append(f'row {i}: no refs')
        if dec not in ('place', 'end', 'drop'):
            problems.append(f'row {i}: decision {dec!r}')
        if dec == 'place' and (not r.get('paragraphs') or not set(r['paragraphs']) <= paras):
            problems.append(f"row {i}: paragraphs {r.get('paragraphs')} not in the prose")
        if dec in ('place', 'end') and not r.get('note_tr'):
            problems.append(f'row {i}: no note')
        if dec == 'drop' and not r.get('reason'):
            problems.append(f'row {i}: drop without a reason')
        for ref in r.get('refs') or []:
            if ref in seen:
                problems.append(f'{ref}: in rows {seen[ref]} and {i}')
            seen[ref] = i
            if ref not in listed and not r.get('added'):
                problems.append(f'{ref}: not listed and not marked added')
    missing = sorted(listed - set(seen))
    if missing:
        problems.append(f'{len(missing)} listed ref(s) without a decision: {missing[:8]}')
    if placed.get('malformed'):
        problems.append(f"{len(placed['malformed'])} malformed line(s)")
    n = {k: sum(len(r.get('refs') or []) for r in placed['rows'] if r.get('decision') == k) for k in ('place', 'end', 'drop')}
    return (f"placed {n['place']}, end {n['end']}, dropped {n['drop']}; "
            + ('check OK' if not problems else f'{len(problems)} problem(s): ' + '; '.join(problems[:6]))
            + ''.join(f'; {x}' for x in notes))


def cmd_place(a):
    ads = sorted(p for p in run_dir(a.surah, a.tag).iterdir() if (p / 'merged.json').exists())
    with cf.ThreadPoolExecutor(a.parallel) as ex:
        for msg in ex.map(lambda ad: one_place(a.surah, a.tag, ad, a.effort), ads):
            print(msg, flush=True)


def cmd_check(a):
    for ad in sorted(p for p in run_dir(a.surah, a.tag).iterdir() if (p / 'sol' / 'placed.json').exists()):
        print(f'{ad.name}: {check_one(ad)}')


MARK = {'same': '≈', 'similar': '≈', 'opposite': '≠', 'background': '◦', 'word': 'ʾ'}


def verse_lines(db, refs: list[str], quote: str) -> list[str]:
    """One tag per verse, the prose's tag structure with a `bible` field (user, 2026-10-09):
    {bible:<WLC or SBLGNT>, tr:<KJV>, gloss:<Kutsal Kitap 2009>, source:<OSIS ref, KJV numbering>}. Where the Turkish
    joins verses (TURNTB `bridge`), the row's verses of one range share one tag (source = the range) and the Turkish
    is given once; a range only partly in the row says so in `source`. A text the corpus lacks is written as "—"
    and printed as a NOTE, never left out silently."""
    groups = []
    for ref in refs:
        t = texts(db, ref)
        br = t.get('TURNTB_bridge')
        if groups and br and groups[-1][0] == br:
            groups[-1][1].append((ref, t))
        else:
            groups.append((br, [(ref, t)]))
    out = []
    for br, members in groups:
        for ref, t in members:
            for name, v in (('original', t.get('WLC') or t.get('SBLGNT')), ('KJV', t.get('KJV')), ('TURNTB', t.get('TURNTB'))):
                if not v:
                    print(f'NOTE: {ref}: no {name} text in the corpus; written as "—"')
                elif '}' in v or re.search(r', (tr|gloss|source):', v):
                    print(f'NOTE: {ref}: {name} text contains a tag delimiter; check the rendering')
        o = ' '.join((t.get('WLC') or t.get('SBLGNT') or '—') for _, t in members)
        en = ' '.join(t.get('KJV') or '—' for _, t in members)
        tr = members[0][1].get('TURNTB') or '—'
        refs_here = [r for r, _ in members]
        if br:
            start, end = br.split('-')
            b, c, _ = start.split('.')
            end = end if '.' in end else f'{c}.{end}'
            whole = len(refs_here) > 1 and refs_here[0] == start and refs_here[-1] == f'{b}.{end}'
            src = br if whole else f"{', '.join(refs_here)} (Türkçe {br} birlikte)"
        else:
            src = refs_here[0]
        out.append(f'{quote}{{bible:{o}, tr:{en}, gloss:{tr}, source:{src}}}')
    return out


def cmd_preview(a):
    db = sqlite3.connect(INDEX)
    for ad in sorted(p for p in run_dir(a.surah, a.tag).iterdir() if (p / 'sol' / 'placed.json').exists()):
        rows = json.loads((ad / 'sol' / 'placed.json').read_text())['rows']
        prose = (HERE / 'work' / f's{a.surah:03d}' / 'pack' / 'numbered' / f'{ad.name}.md').read_text()
        by_p = {}
        for r in rows:
            if r.get('decision') == 'place':
                for p in r.get('paragraphs') or []:
                    by_p.setdefault(p, []).append(r)
        out = []
        for block in prose.split('\n\n'):
            out.append(block)
            m = re.match(r'\[¶(\d+)\]', block.strip())
            for r in by_p.get(int(m[1]) if m else -1, []):
                mark = MARK.get(r.get('way') or r.get('relation'), '·')
                out.append('\n>\n'.join([f"> **{mark} {', '.join(r['refs'])}** — {r['note_tr']}"]
                                         + verse_lines(db, r['refs'], '> ')))
        end = [r for r in rows if r.get('decision') == 'end']
        if end:
            out.append('## Bu ayete benzeyen diğer Kitab-ı Mukaddes ayetleri')
            for r in end:
                mark = MARK.get(r.get('way') or r.get('relation'), '·')
                out.append('\n'.join([f"- **{mark} {', '.join(r['refs'])}** — {r['note_tr']}"]
                                      + verse_lines(db, r['refs'], '  - ')))
        drops = [r for r in rows if r.get('decision') == 'drop']
        if drops:
            out.append('<details><summary>Elenenler (' + str(sum(len(r['refs']) for r in drops)) + ')</summary>\n\n'
                       + '\n'.join(f"- {', '.join(r['refs'])}: {r.get('reason', '')}" for r in drops) + '\n</details>')
        (ad / 'preview.md').write_text('\n\n'.join(out) + '\n')
        print(ad / 'preview.md')


def cmd_report(a):
    tot = {}
    for f in sorted(run_dir(a.surah, a.tag).glob('*/*/rows.json')) + sorted(run_dir(a.surah, a.tag).glob('*/sol/placed.json')):
        r = json.loads(f.read_text())
        m = f.parent.name
        usd = r['cost'].get('usd_equivalent')
        tot.setdefault(m, [0.0, 0, 0])
        if usd is None:
            tot[m][2] += r['cost'].get('total_output_tokens') or 0
        else:
            tot[m][0] += usd
        tot[m][1] += 1
        print(f"{f.parents[1].name if m != 'sol' else f.parents[1].name} {m}: "
              + (f'${usd:.3f}' if usd is not None else f"no saved rate, {r['cost'].get('total_input_tokens')} in / "
                 f"{r['cost'].get('total_output_tokens')} out tokens"))
    for m, (usd, n, outtok) in tot.items():
        print(f'TOTAL {m}: {n} calls, ${usd:.2f}' + (f' + {outtok} output tokens without a saved rate' if outtok else ''))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=('sol', 'recheck', 'recall', 'merge', 'place', 'check', 'preview', 'report'))
    ap.add_argument('--surah', type=int, default=0, help='required except for sol')
    ap.add_argument('--cap', type=int, help='sol: at most this many live Sol calls of the tag (top up as each ends)')
    ap.add_argument('--tag', required=True)
    ap.add_argument('--ayat')
    ap.add_argument('--models', default='luna,terra')
    ap.add_argument('--parallel', type=int, default=6)
    ap.add_argument('--effort', default='high')
    ap.add_argument('--prose', action='store_true', help='recall: include the frozen ayah commentary')
    ap.add_argument('--brief', default='ayah', choices=('ayah', 'par'), help='recall: par = per-paragraph understanding brief')
    ap.add_argument('--roots', help='merge: also take the verified verses of this roots.py tag')
    a = ap.parse_args()
    if a.cmd not in ('sol', 'recheck') and not a.surah:
        raise SystemExit(f'{a.cmd} needs --surah')
    if a.cmd in ('recall', 'sol', 'recheck') and not a.ayat:
        raise SystemExit(f'{a.cmd} needs --ayat')
    globals()[f'cmd_{a.cmd}'](a)


if __name__ == '__main__':
    main()
