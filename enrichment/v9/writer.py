#!/usr/bin/env python3
"""Enrichment v9 P1+P2: build the writer's inputs for one ayah page, and check what the writer wrote. Launches no
model.

The writer (one Opus agent) reads the numbered page, the focus ayah's whole verse map and the question index of every
cited verse; it looks up what it needs with q.py, writes a ledger line for every (paragraph, cited verse) pair and the
blocks.

  writer.py build RUN --ayah 103:1 --page PATH --model claude-opus-5-5:high
              refuses (and names them) when a cited verse has no verse map
  writer.py check RUN      the agent runs it until OK; it accepts the cited verses and every mapped verse of the
                           page's own surah (a page may cover same-surah verses it names without citing them)

Files: enrichment/v9/work/RUN/write/inputs/{page,focus,index}.pK.txt, spawn/, out/<TAG>/{ledger,blocks}.jsonl.
"""
import argparse
import contextlib
import io
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

V9 = Path(__file__).resolve().parent
sys.path.insert(0, str(V9.parent / 'v7'))
import digest  # noqa: E402
from digest import PART_CHARS, ROOT, contains, dump  # noqa: E402
sys.path.insert(0, str(V9))
import q as Q  # noqa: E402
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location('write7', V9.parent / 'v7' / 'write.py')
write7 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(write7)

BRIEF = V9 / 'briefs/write.md'
KINDS = ('focus', 'cited', 'agreement', 'closing')
STATUSES = ('written', 'same_as', 'agreed', 'tradition_silent', 'page_own', 'retelling')
VOICES = ('BIQAI', 'BIQAI-FULL', 'BINTSHATI', 'BINTSHATI-IJAZ', 'BINTSHATI-INSAN')
VOICE_FAMILIES = (('al-Biqāʿī', {'BIQAI', 'BIQAI-FULL'}), ("Bint al-Shāṭiʾ", {'BINTSHATI', 'BINTSHATI-IJAZ', 'BINTSHATI-INSAN'}))


def as_list(v):
    return v if isinstance(v, list) else []
IDS = re.compile(r'\d+:\d+/q\d+(?:/p\d+)?')
ARABIC_RUN = re.compile(r'[؀-ۿ][؀-ۿً-ْٰ\s]*[؀-ۿ]')


def wdir(run):
    return V9 / 'work' / run / 'write'


def captured(fn, **kw):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(argparse.Namespace(**kw))
    return buf.getvalue()


def parts(d, stem, text, label):
    chunks = [text[i:i + PART_CHARS] for i in range(0, len(text), PART_CHARS)] or ['']
    for k, p in enumerate(chunks):
        tail = f'\n<<part {k} ends; continues in part {k + 1}>>' if k + 1 < len(chunks) else f'\n<<end of {label}>>'
        (d / f'{stem}.p{k}.txt').write_text(f'<<{label}, part {k} of 0..{len(chunks) - 1}>>\n{p}{tail}\n')
    return len(chunks)


def build(a):
    d = wdir(a.run)
    if d.exists():
        raise SystemExit(f'{d} exists; use a new run')
    _, paras, numbered, cites = write7.page(a.page, a.ayah)
    verses = sorted({a.ayah} | {v for vs in cites.values() for v in vs}, key=lambda x: tuple(map(int, x.split(':'))))
    missing = [v for v in verses if not Q.located(v)]
    if missing:
        raise SystemExit(f'no verse map for {len(missing)} cited verse(s): {", ".join(missing)}; map them first')
    stale = [(v, Q.stale(v)) for v in verses]
    stale = [f'{v} ({r})' for v, r in stale if r]
    if stale:
        raise SystemExit(f'{len(stale)} cited verse map(s) not current, nothing built: ' + '; '.join(stale))
    qs, _ = Q.load(a.ayah)
    Q.MAX_BYTES = 10 ** 9  # the lookup cap is for an agent's own calls; preloaded text is written whole into parts
    focus = captured(Q.cmd_question, qids=[q['id'] for q in qs])
    if '[cut:' in focus:  # the focus map is written whole, question by question
        focus = ''.join(captured(Q.cmd_question, qids=[q['id']]) for q in qs)
    index = ''.join(captured(Q.cmd_index, verses=[v]) for v in verses if v != a.ayah)
    if '[cut:' in focus + index:
        raise SystemExit('a verse map is larger than one lookup output; split it before building')
    (d / 'inputs').mkdir(parents=True)
    (d / 'spawn').mkdir()
    n = {'page': parts(d / 'inputs', 'page', numbered, f'{a.ayah} reading, paragraphs numbered'),
         'focus': parts(d / 'inputs', 'focus', focus, f'{a.ayah} verse map, every question in full'),
         'index': parts(d / 'inputs', 'index', index, 'question index of the cited verses')}
    model, effort = a.model.split(':')
    tag = digest.tag_of(model, effort)
    agent = f'/root/v9w_{a.run}_{tag}_{a.ayah.replace(":", "-")}'
    cite_lines = '\n'.join(f"- ¶{p}: {', '.join(v)}" for p, v in sorted(cites.items()))
    fill = {'AGENT': agent, 'MODEL': model, 'EFFORT': effort, 'RUN': a.run, 'TAG': tag, 'AYAH': a.ayah,
            'LAST_PAGE': str(n['page'] - 1), 'LAST_FOCUS': str(n['focus'] - 1), 'LAST_INDEX': str(n['index'] - 1),
            'CITES': cite_lines, 'LASTP': str(max(paras))}
    text = BRIEF.read_text()
    for x, v in fill.items():
        text = text.replace('{' + x + '}', v)
    (d / 'spawn' / f'{tag}.md').write_text(text)
    (d / 'out' / tag).mkdir(parents=True)
    dump(d / 'manifest.json', {'ayah': a.ayah, 'page': a.page, 'model': a.model, 'tag': tag, 'agent': agent,
                               'paragraphs': sorted(paras), 'pairs': [[p, v] for p, vs in sorted(cites.items()) for v in vs],
                               'focus_questions': [q['id'] for q in qs], 'verses': verses, 'parts': n})
    print(f"{a.ayah}: {len(paras)} paragraphs, {len(verses)} verses ({len(verses) - 1} cited), "
          f"{sum(len(vs) for vs in cites.values())} pairs; page {len(numbered):,} chars, focus map {len(focus):,}, "
          f"index {len(index):,}; spawn {(d / 'spawn' / f'{tag}.md').relative_to(ROOT)}")


def read(f, problems):
    out = []
    if not f.exists():
        problems.append(f'{f.name}: no file')
        return out
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if line.strip():
            try:
                x = json.loads(line)
            except ValueError as e:
                problems.append(f'{f.name} line {i}: not JSON ({e})')
                continue
            if not isinstance(x, dict):
                problems.append(f'{f.name} line {i}: not a JSON object')
                continue
            if f.name == 'ledger.jsonl' and 'p' in x and not (isinstance(x['p'], int) and not isinstance(x['p'], bool)):
                problems.append(f'{f.name} line {i}: "p" must be one paragraph number')
                x['p'] = None
            for k in ('p', 'questions', 'positions', 'notes', 'blocks'):
                if k == 'p' and f.name == 'ledger.jsonl':
                    continue
                if k in x and x[k] is not None and not (isinstance(x[k], list) and all(isinstance(y, (str, int)) and not isinstance(y, bool) for y in x[k])):
                    problems.append(f'{f.name} line {i}: "{k}" has the wrong type')
                    x[k] = []
            for k in ('id', 'verse', 'kind', 'topic', 'text', 'status', 'says', 'reason', 'voices'):
                if k in x and x[k] is not None and not isinstance(x[k], str):
                    problems.append(f'{f.name} line {i}: "{k}" must be text')
                    x[k] = ''
            out.append(x)
    return out


def check(a):
    d = wdir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    out = d / 'out' / man['tag']
    problems = []
    blocks, ledger = read(out / 'blocks.jsonl', problems), read(out / 'ledger.jsonl', problems)
    surah = man['ayah'].split(':')[0]
    # page verses: the cited set, plus every mapped verse of the page's own surah (user, 2026-10-09: a page may cover
    # same-surah verses it names without citing them; full coverage)
    page_verses = set(man['verses']) | {k.replace('-', ':') for k in Q.mapped() if k.split('-')[0] == surah}
    loaded = {v: Q.load_current(v) for v in sorted(page_verses)}
    needed = set(man['verses']) | {b.get('verse') for b in ledger if b.get('verse') in page_verses}
    not_current = {v: why for v, (_, _, why) in loaded.items() if why}
    for v, why in sorted(not_current.items()):
        if v in needed:
            problems.append(f'{v}: map not current ({why})')
        else:
            print(f'NOTE {v}: same-surah map not current ({why}); its questions and notes are not available to this check')
    for v in sorted(page_verses):
        if v not in not_current and loaded[v][0] is None:
            if v in needed:
                problems.append(f'{v}: verse map is missing')
            else:
                print(f'NOTE {v}: same-surah verse has no assembled map (its runs are superseded or unassembled)')
    maps = {v: (qs, rs) for v, (qs, rs, why) in loaded.items() if qs is not None}

    def unknown(x, what):
        v = str(x).split('/')[0]
        return f'{what} {x} is in a map that is not current ({v})' if v in not_current else None

    qids = {q['id']: (v, q) for v, (qs, _) in maps.items() for q in qs}
    pids = {p['id']: (v, p) for v, (qs, _) in maps.items() for q in qs for p in q['positions']}
    rows = {i: x for v, (_, rs) in maps.items() for i, x in rs.items()}
    ids = set()
    for b in blocks:
        bid = b.get('id', '?')
        if bid in ids:
            problems.append(f'block {bid}: id used twice')
        ids.add(bid)
        for k in ('id', 'p', 'kind', 'topic', 'text'):
            if not b.get(k):
                problems.append(f'block {bid}: missing {k}')
        if b.get('kind') not in KINDS:
            problems.append(f"block {bid}: kind must be one of {', '.join(KINDS)}")
        for p in b.get('p') or []:
            if p not in man['paragraphs']:
                problems.append(f'block {bid}: paragraph {p} is not a paragraph of the page')
        if not (b.get('questions') or b.get('notes')):
            problems.append(f'block {bid}: cites no question and no note')
        for x in b.get('questions') or []:
            if x not in qids:
                problems.append(f'block {bid}: ' + (unknown(x, 'question') or f'question {x} is not in a verse map of this page'))
        for x in b.get('positions') or []:
            if x not in pids:
                problems.append(f'block {bid}: ' + (unknown(x, 'position') or f'position {x} is not in a verse map of this page'))
        for x in b.get('notes') or []:
            if x not in rows:
                problems.append(f'block {bid}: note {x} is not a note of this page\'s verses'
                                + (f" (maps not current: {', '.join(sorted(not_current))})" if not_current else ''))
        if IDS.search(b.get('text', '')):
            problems.append(f"block {bid}: ids in the text ({', '.join(sorted(set(IDS.findall(b['text']))))}); ids go only in the id fields")
        cited = set(b.get('notes') or [])
        for x in b.get('positions') or []:
            if x in pids:
                p = pids[x][1]
                cited |= set(p['rows']) | set(p.get('against') or [])
        for x in [q.strip() for q in ARABIC_RUN.findall(b.get('text', '')) if len(q.split()) >= 3]:
            if not any(contains(rows[r].get('anchor') or '', x, minimum=1) for r in cited if r in rows):
                problems.append(f'block {bid}: Arabic not in the exact words of the notes it cites: {x[:80]}')
        held = set()
        for x in b.get('questions') or []:
            if x in qids:
                for p in qids[x][1]['positions']:
                    held |= {rows[r]['src'] for r in (p.get('rows') or []) + (p.get('against') or []) if r in rows}
        named = {rows[r]['src'] for r in cited if r in rows}
        for name, fam in VOICE_FAMILIES:     # each major voice separately: one cited voice does not excuse the other
            if held & fam and not named & fam and not (b.get('voices') or '').strip():
                problems.append(f"block {bid}: its questions hold {name} ({', '.join(sorted(held & fam))}); cite them or say why in \"voices\"")
    want = {(p, v) for p, v in man['pairs']}
    seen = defaultdict(int)
    for r in ledger:
        pair = (r.get('p'), r.get('verse'))
        if pair not in want:
            if pair[0] in man['paragraphs'] and pair[1] in page_verses:
                want.add(pair)          # an uncited page verse (or same-surah verse) the paragraph discusses
            else:
                problems.append(f'ledger: (¶{pair[0]}, {pair[1]}) is not a paragraph and verse of this page')
                continue
        seen[pair] += 1
        st = r.get('status')
        if st not in STATUSES:
            problems.append(f"ledger ¶{pair[0]} {pair[1]}: status must be one of {', '.join(STATUSES)}")
        elif st in ('written', 'same_as', 'agreed'):
            if not r.get('blocks') or any(x not in ids for x in r['blocks']):
                problems.append(f'ledger ¶{pair[0]} {pair[1]}: {st}, but its blocks are missing or unknown')
            if not (r.get('says') or '').strip():
                problems.append(f'ledger ¶{pair[0]} {pair[1]}: {st} needs "says" (what the paragraph commits to)')
        elif not (r.get('reason') or '').strip():
            problems.append(f'ledger ¶{pair[0]} {pair[1]}: {st} needs a reason')
    for pair in sorted(want):
        if seen[pair] != 1:
            problems.append(f'ledger ¶{pair[0]} {pair[1]}: {seen[pair]} lines (expected exactly 1)')
    used = {x for b in blocks for x in b.get('questions') or []}
    for x in man['focus_questions']:
        if x not in used:
            problems.append(f'focus question {x} is in no block (a closing line at least)')
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
