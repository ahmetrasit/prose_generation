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

  recall.py recall  --surah S --tag T --ayat S:A,S:A [--models luna,terra] [--parallel 6]
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
STRENGTH = ('strong', 'medium', 'weak')
RELATION = ('similar', 'opposite')
FOLLOWUP = ('Review your recall once more for verses that qualify under the same rules and are not in your list yet: '
            'the other Testament, other books, other distinct claims or images of the ayah, and verses that say the '
            'opposite. Reply only with the new rows, in the same four-field TSV. Zero rows is a valid answer. Answer '
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
        if len(f) != 4:
            bad.append(f'not four fields: {line[:120]}')
            continue
        st, rel, ref, ex = f
        st, rel = st.lower(), rel.lower()
        if st not in STRENGTH or rel not in RELATION or not OSIS.match(ref):
            bad.append(f'bad strength/relation/ref: {line[:120]}')
            continue
        rows.append(dict(strength=st, relation=rel, ref=ref, explanation=ex))
    return rows, bad


def one_recall(s: int, tag: str, ayah: str, model: str, q: dict) -> str:
    d = run_dir(s, tag) / key(ayah) / model
    if (d / 'rows.json').exists():
        return f'{ayah} {model}: done already'
    d.mkdir(parents=True, exist_ok=True)
    surah = '\n'.join(f'{r} {t}' for r, t in q.items() if r.split(':')[0] == str(s) and not r.endswith(':0'))
    prompt = ((HERE / 'prompts' / 'recall.md').read_text().replace('{{REF}}', ayah).replace('{{ARABIC}}', q[ayah])
              .replace('{{SURAH}}', str(s)).replace('{{SURAH_TEXT}}', surah))
    (d / 'prompt.md').write_text(prompt)
    t1 = CR.turn(d, 1, prompt, MODELS[model], 'max')
    if not t1['completed'] or not t1['thread_id']:
        return f'ERROR {ayah} {model}: turn 1 did not complete (rc {t1["returncode"]}); see {d}'
    t2 = CR.turn(d, 2, FOLLOWUP, MODELS[model], 'max', thread=t1['thread_id'])
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
    (d / 'rows.json').write_text(json.dumps(dict(ayah=ayah, model=MODELS[model], effort='max', rows=r1 + r2,
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
        for msg in ex.map(lambda j: one_recall(a.surah, a.tag, j[0], j[1], q), jobs):
            print(msg, flush=True)


def texts(db, ref: str) -> dict:
    book = OSIS.match(ref)[1]
    orig = 'WLC' if book in OT else 'SBLGNT'
    out = {}
    for src in ('KJV', orig):
        r = db.execute('select text from seg where seg = ?', (f'{src}:{ref}',)).fetchone()
        if r:
            out[src] = r[0]
    return out


def cmd_merge(a):
    db = sqlite3.connect(INDEX)
    for ad in sorted(p for p in run_dir(a.surah, a.tag).iterdir() if p.is_dir()):
        readers = sorted(ad.glob('*/rows.json'))
        merged = {}
        for f in readers:
            r = json.loads(f.read_text())
            for row in r['rows']:
                m = merged.setdefault(row['ref'], dict(ref=row['ref'], readers=[], strength=row['strength'],
                                                        relations=[], notes=[]))
                rd = f.parent.name
                if rd not in m['readers']:
                    m['readers'].append(rd)
                if STRENGTH.index(row['strength']) < STRENGTH.index(m['strength']):
                    m['strength'] = row['strength']
                if row['relation'] not in m['relations']:
                    m['relations'].append(row['relation'])
                m['notes'].append(f"{rd}: {row['explanation']}")
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
        lines = [f"### {m['ref']} ({m['strength']}, {rel})"]
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


def check_one(ad: Path) -> str:
    merged = json.loads((ad / 'merged.json').read_text())
    placed = json.loads((ad / 'sol' / 'placed.json').read_text())
    paras = set(map(int, re.findall(r'\[¶(\d+)\]', (HERE / 'work' / f"s{int(ad.name.split('_')[0]):03d}" / 'pack'
                                                     / 'numbered' / f'{ad.name}.md').read_text())))
    listed, seen, problems = {m['ref'] for m in merged['items']}, {}, []
    for i, r in enumerate(placed['rows']):
        dec = r.get('decision')
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
            + ('check OK' if not problems else f'{len(problems)} problem(s): ' + '; '.join(problems[:6])))


def cmd_place(a):
    ads = sorted(p for p in run_dir(a.surah, a.tag).iterdir() if (p / 'merged.json').exists())
    with cf.ThreadPoolExecutor(a.parallel) as ex:
        for msg in ex.map(lambda ad: one_place(a.surah, a.tag, ad, a.effort), ads):
            print(msg, flush=True)


def cmd_check(a):
    for ad in sorted(p for p in run_dir(a.surah, a.tag).iterdir() if (p / 'sol' / 'placed.json').exists()):
        print(f'{ad.name}: {check_one(ad)}')


def cmd_preview(a):
    for ad in sorted(p for p in run_dir(a.surah, a.tag).iterdir() if (p / 'sol' / 'placed.json').exists()):
        rows = json.loads((ad / 'sol' / 'placed.json').read_text())['rows']
        prose = (HERE / 'work' / f's{a.surah:03d}' / 'pack' / 'numbered' / f'{ad.name}.md').read_text()
        by_p = {}
        for r in rows:
            if r.get('decision') == 'place':
                for p in r['paragraphs']:
                    by_p.setdefault(p, []).append(r)
        out = []
        for block in prose.split('\n\n'):
            out.append(block)
            m = re.match(r'\[¶(\d+)\]', block.strip())
            for r in by_p.get(int(m[1]) if m else -1, []):
                mark = '≈' if r.get('relation') == 'similar' else '≠'
                out.append(f"> **{mark} {', '.join(r['refs'])}** — {r['note_tr']}")
        end = [r for r in rows if r.get('decision') == 'end']
        if end:
            out.append('## Bu ayete benzeyen diğer Kitab-ı Mukaddes ayetleri')
            for r in end:
                mark = '≈' if r.get('relation') == 'similar' else '≠'
                out.append(f"- **{mark} {', '.join(r['refs'])}** — {r['note_tr']}")
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
    ap.add_argument('cmd', choices=('recall', 'merge', 'place', 'check', 'preview', 'report'))
    ap.add_argument('--surah', type=int, required=True)
    ap.add_argument('--tag', required=True)
    ap.add_argument('--ayat')
    ap.add_argument('--models', default='luna,terra')
    ap.add_argument('--parallel', type=int, default=6)
    ap.add_argument('--effort', default='high')
    a = ap.parse_args()
    if a.cmd == 'recall' and not a.ayat:
        raise SystemExit('recall needs --ayat')
    globals()[f'cmd_{a.cmd}'](a)


if __name__ == '__main__':
    main()
