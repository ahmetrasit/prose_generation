#!/usr/bin/env python3
"""Enrichment v9 P3: the meal block of one ayah page. Launches no model.

One agent per ayah reads the numbered page, the ayah's meal table (panel, relay pair and Arberry, reference set; the
v2 packer's rendering) and the focus ayah's verse map, and writes the meal block(s): which renderings take which
position of the tradition, the best literal and best explanatory rendering per word, and what the meals lose.

  meal.py build RUN --ayah 103:1 --page PATH --model claude-opus-5-5:high
  meal.py check RUN                  ids, paragraphs and positions exist (the agent runs it until OK)

Files: enrichment/v9/work/RUN/meal/inputs/{page,dict,meals,map}.pK.txt, spawn/, out/<TAG>/blocks.jsonl.
"""
import argparse
import json
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

V9 = Path(__file__).resolve().parent
sys.path.insert(0, str(V9.parent / 'v7'))
sys.path.insert(0, str(V9.parent / 'v2'))
import digest  # noqa: E402
from digest import PART_CHARS, ROOT, dump  # noqa: E402
import write  # noqa: E402  (v7 page numbering)
import pack  # noqa: E402  (v2 meal table)

BRIEF = V9 / 'briefs/meal.md'


def mdir(run):
    return V9 / 'work' / run / 'meal'


def parts(d, stem, text, label):
    chunks = [text[i:i + PART_CHARS] for i in range(0, len(text), PART_CHARS)] or ['']
    for k, p in enumerate(chunks):
        tail = f'\n<<part {k} ends; continues in part {k + 1}>>' if k + 1 < len(chunks) else f'\n<<end of {label}>>'
        (d / f'{stem}.p{k}.txt').write_text(f'<<{label}, part {k} of 0..{len(chunks) - 1}>>\n{p}{tail}\n')
    return len(chunks)


def meal_ids(ayah):
    s, a = map(int, ayah.split(':'))
    with sqlite3.connect(ROOT / 'enrichment/corpus/corpus.sqlite') as con:
        return {r[0] for r in con.execute("SELECT src FROM seg WHERE s=? AND a<=? AND coalesce(a_end,a)>=? AND src IN "
                                          "(SELECT id FROM src WHERE kind IN ('meal','translation'))", (s, a, a))}


def profile(ep):
    """A gloss's error profile. With a fit: fit and every bit. Without one (fit none/None): only what the gloss loses,
    adds or collides with (a "preserves" note alone says nothing a meal judgement needs)."""
    ep = ep or {}
    fit = ep.get('fit') if ep.get('fit') not in (None, 'none') else ''
    keys = ('preserves', 'loses', 'adds', 'collision') if fit else ('loses', 'adds', 'collision')
    bits = [f"{k}: {ep[k]}" for k in keys if ep.get(k) not in (None, '', 'None')]
    if not fit and not bits:
        return ''
    return (f" [{fit}] " if fit else ' ') + '; '.join(bits)


def dictionary_text(ayah):
    """The project dictionary for the ayah's words, for the meal judgement: every branch of each identity root and
    documented alternative, its Turkish label and glosses, and every gloss with an error profile (narrowing,
    broadening, displacement, drifted_loanword), including the glosses the dictionary excludes."""
    state = pack.dictionary_state()
    if not state['match']:
        raise SystemExit(f"dictionary transfer {state['transfer_commit']} != ../dictionary HEAD {state['dictionary_head']}: "
                         'sync quran-data first')
    src = pack.D.P.Sources()
    out = [f'# Project dictionary for {ayah}: Turkish glosses and their error profiles', '',
           'Per branch: the Turkish label, the glosses of its attested senses, the contextual glosses, and the glosses '
           'the dictionary excludes. A profile in brackets says how a Turkish word fails the branch: narrowing (keeps '
           'part of the range), broadening (adds what the branch lacks), displacement (a different concept), '
           'drifted_loanword (a Turkish word whose present sense moved away).', '']
    done = set()
    for w in src.words(ayah):
        r = src.word_roots(w)
        for rid, why in [(x, 'identity root') for x in r['identity']] + [(x, 'documented alternative') for x, _ in r['alternatives']]:
            if rid in done:
                continue
            done.add(rid)
            e = src.entry(rid)
            out.append(f"## {src.root_name.get(rid, rid)} ({rid}): {why} of {w['surface']}")
            if not e:
                out += ['(no Turkish dictionary entry)', '']
                continue
            for b in e.get('branches', []):
                g = b.get('concept_gloss') or {}
                out.append(f"- **{b['branch_ref'].split('/')[-1]}** {g.get('text', '')}{profile(g.get('error_profile'))}")
                senses = ' · '.join(x['target_gloss'] for x in b.get('lexical_glosses', []) if x.get('target_gloss'))
                if senses:
                    out.append(f'  senses: {senses}')
                for x in b.get('contextual_glosses', []):
                    out.append(f"  contextual «{x.get('text')}»: {x.get('applicability', '')}{profile(x.get('error_profile'))}")
                for x in b.get('excluded_glosses', []):
                    out.append(f"  excluded ({x.get('category')}) «{x.get('text')}»{profile(x.get('error_profile'))}")
            out.append('')
    return '\n'.join(out) + '\n'


def build(a):
    d = mdir(a.run)
    if d.exists():
        raise SystemExit(f'{d} exists; use a new run')
    import q as Q
    why = Q.stale(a.ayah)
    if why:
        raise SystemExit(f'{a.ayah}: verse map not current ({why}); nothing built')
    (d / 'inputs').mkdir(parents=True)
    (d / 'spawn').mkdir()
    _, paras, numbered, _ = write.page(a.page, a.ayah)
    with sqlite3.connect(ROOT / 'enrichment/corpus/corpus.sqlite') as con:
        metas = {r[0]: json.loads(r[1] or '{}') for r in con.execute('SELECT id, meta FROM src')}
        meals = pack.meals_md(con, metas, a.ayah)
    themap = subprocess.run([sys.executable, '-B', str(V9 / 'q.py'), 'index', a.ayah], capture_output=True, text=True,
                            check=True).stdout
    dic = dictionary_text(a.ayah)
    n = {'page': parts(d / 'inputs', 'page', numbered, f'{a.ayah} reading, paragraphs numbered'),
         'dict': parts(d / 'inputs', 'dict', dic, f'{a.ayah} project dictionary'),
         'meals': parts(d / 'inputs', 'meals', meals, f'{a.ayah} translations'),
         'map': parts(d / 'inputs', 'map', themap, f'{a.ayah} verse map, question list')}
    model, effort = a.model.split(':')
    tag = digest.tag_of(model, effort)
    agent = f'/root/v9meal_{a.run}_{tag}_{a.ayah.replace(":", "-")}'
    fill = {'AGENT': agent, 'MODEL': model, 'EFFORT': effort, 'RUN': a.run, 'TAG': tag, 'AYAH': a.ayah,
            'LAST_PAGE': str(n['page'] - 1), 'LAST_DICT': str(n['dict'] - 1), 'LAST_MEALS': str(n['meals'] - 1), 'LAST_MAP': str(n['map'] - 1)}
    text = BRIEF.read_text()
    for x, v in fill.items():
        text = text.replace('{' + x + '}', v)
    (d / 'spawn' / f'{tag}.md').write_text(text)
    (d / 'out' / tag).mkdir(parents=True)
    dump(d / 'manifest.json', {'ayah': a.ayah, 'page': a.page, 'model': a.model, 'tag': tag, 'agent': agent,
                               'paragraphs': sorted(paras), 'meals': sorted(meal_ids(a.ayah)), 'parts': n})
    print(f"{a.ayah}: page {len(numbered):,} chars, dictionary {len(dic):,}, meals {len(meals):,}, map {len(themap):,}; "
          f"spawn {(d / 'spawn' / f'{tag}.md').relative_to(ROOT)}")


def check(a):
    d = mdir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    f = d / 'out' / man['tag'] / 'blocks.jsonl'
    if not f.exists():
        print(f'{f.name}: no output file')
        sys.exit(1)
    import q as Q
    qs_, _ = Q.load(man['ayah'])
    if qs_ is None:
        print(f"{man['ayah']}: no verse map; positions cannot be checked")
        sys.exit(1)
    pids = {x['id'] for q in qs_ for x in q['positions']}
    problems, n = [], 0
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            b = json.loads(line)
        except ValueError as e:
            problems.append(f'line {i}: not JSON ({e})')
            continue
        if not isinstance(b, dict):
            problems.append(f'line {i}: not a JSON object')
            continue
        n += 1
        for k in ('meals', 'positions'):
            if not isinstance(b.get(k), list) or not b[k] or not all(isinstance(x, str) for x in b[k]):
                problems.append(f'line {i}: "{k}" must be a non-empty list of ids')
                b[k] = [x for x in b[k] if isinstance(x, str)] if isinstance(b.get(k), list) else []
        for k in ('topic', 'text'):
            if not isinstance(b.get(k), str):
                problems.append(f'line {i}: "{k}" must be text')
                b[k] = ''
        if not (b.get('topic') or '').strip():
            problems.append(f'line {i}: missing "topic"')
        if type(b.get('p')) is not int or b.get('p') not in man['paragraphs']:
            problems.append(f"line {i}: paragraph {b.get('p')} is not a paragraph of the page")
        if re.search(r'\d+:\d+/q\d+', b.get('text') or ''):
            problems.append(f'line {i}: ids in the text; ids go only in the "positions" field')
        if not (b.get('text') or '').strip():
            problems.append(f'line {i}: empty text')
        for m in b.get('meals') or []:
            if m not in man['meals']:
                problems.append(f'line {i}: {m} has no rendering of {man["ayah"]}')
        for q in b.get('positions') or []:
            if q not in pids:
                problems.append(f'line {i}: position {q} is not in the map of {man["ayah"]}')
    if not n:
        problems.append('no block')
    if n > 2:
        problems.append(f'{n} blocks; two at most')
    for x in problems:
        print(x)
    print('OK' if not problems else f'{len(problems)} problem(s)')
    sys.exit(1 if problems else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('build'); p.add_argument('run'); p.add_argument('--ayah', required=True)
    p.add_argument('--page', required=True); p.add_argument('--model', required=True)
    p = sub.add_parser('check'); p.add_argument('run')
    a = ap.parse_args()
    {'build': build, 'check': check}[a.cmd](a)


if __name__ == '__main__':
    main()
