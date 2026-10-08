#!/usr/bin/env python3
"""Enrichment v8: per-reference sift. One Luna agent per verse the page cites (the focus ayah included) reads the
whole page, then every tier-1 note filed under that verse, and gives each note the paragraphs it serves (or none,
with a reason). One more agent does the same for notes on other verses that name the focus ayah. Nothing is trimmed:
every note gets a verdict, and the check refuses a file that skips one. The Opus writer then gets, per paragraph,
the notes the sift assigned, every focus note with its assignment, and q.py to search further.

  sift.py build RUN --ayah A --page PATH [--max-chars 200000]   index + page (q.py build), sift inputs, Luna spawn files
  sift.py check RUN KEY                                          one agent's output: one verdict per note
  sift.py report RUN                                             per agent: done, kept, dropped, cost; per paragraph
  sift.py writer RUN                                             writer inputs (sifted notes, focus with assignments) + Opus spawn file

Luna spawn files: work/RUN/spawn/sift_*.md, run with enrichment/v5/run_codex.py (outputs land in work/RUN/runs/).
"""
import json, re, sqlite3, sys
from collections import defaultdict, Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import q  # noqa: index build, note line, parts

ROOT = q.ROOT
PART = q.PART
LUNA = (HERE / 'briefs/sift.md').read_text()
WRITE = (HERE / 'briefs/write-sift.md').read_text()


def d_of(run):
    return ROOT / 'enrichment/v8/work' / run


def vkey(v):
    """Sort key; tolerant of malformed verse strings in tier 1 (e.g. "36:71-72")."""
    return tuple(int(x) for x in re.findall(r'\d+', v)[:2]) or (9999,)


def short(r):
    """A note line without its long id: the agent answers by number."""
    return q.line(r).split('] ', 1)[1]


ARABIC = re.compile(r'[\u0600-\u06ff]')


def tokens(s):
    a = len(ARABIC.findall(s))
    return a / 2 + (len(s) - a) / 4


def order(rs):
    return sorted(rs, key=lambda r: (r['death'] if isinstance(r['death'], int) else 9999, r['src'], r['id']))


# ---------------------------------------------------------------- build
def build(run, ayah, page, max_chars):
    q.build(run, ayah, page)
    d = d_of(run)
    scope = json.loads((d / 'scope.json').read_text())
    db = sqlite3.connect(d / 'index.sqlite')
    db.row_factory = sqlite3.Row
    cites = {int(p): vs for p, vs in scope['cites'].items()}
    cited_in = defaultdict(list)
    for p, vs in sorted(cites.items()):
        for v in vs:
            cited_in[v].append(p)
    verses = sorted(cited_in, key=vkey)
    groups = []                                    # (key, label, verse or None, rows)
    for v in verses:
        rs = {r['id']: dict(r) for r in db.execute('SELECT * FROM notes WHERE verse=?', (v,))}
        groups.append((v, v, list(rs.values())))
    page_verses = set(verses)
    link = {}
    for r in db.execute('SELECT * FROM notes WHERE mentions LIKE ?', (f'%"{ayah}"%',)):
        if r['verse'] not in page_verses and r['id'] not in link:
            link[r['id']] = dict(r)
    if link:
        groups.append(('links', f'other verses, naming {ayah}', list(link.values())))
    (d / 'sift/in').mkdir(parents=True)
    (d / 'sift/out').mkdir()
    (d / 'spawn').mkdir(exist_ok=True)
    plan, total_chars = [], 0
    for v, label, rows in groups:
        rows = order(rows)
        if not rows:
            print(f'NOTE {v}: no tier-1 notes; no agent')
            continue
        chunks, cur, size = [], [], 0          # split only a verse above max_chars, at note boundaries
        for r in rows:
            n = len(short(r)) + 8
            if cur and size + n > max_chars:
                chunks.append(cur); cur, size = [], 0
            cur.append(r); size += n
        chunks.append(cur)
        for k, rs in enumerate(chunks, 1):
            key = (v.replace(':', '_') if v != 'links' else 'links') + (f'_c{k}' if len(chunks) > 1 else '')
            qt = db.execute('SELECT text FROM quran WHERE verse=?', (v,)).fetchone() if v != 'links' else None
            head = [f'# {len(rs)} notes filed under {label}' + (f' (part {k} of {len(chunks)} of this verse)' if len(chunks) > 1 else ''),
                    *( [f'verse {v}: {qt[0]}'] if qt else [] ), '']
            lines = []
            for n, r in enumerate(rs, 1):
                lines.append(f'#{n} ' + short(r) + (f'   [filed under {r["verse"]}]' if v == 'links' else ''))
            text = '\n'.join(head + lines)
            nparts = q.parts(d / 'sift/in', key, text, f'notes for {key}')
            json.dump({'key': key, 'verse': v, 'ids': [r['id'] for r in rs], 'srcs': [r['src'] for r in rs]}, open(d / 'sift/in' / f'{key}.map.json', 'w'), ensure_ascii=False)
            if v == ayah:
                notes_are, where = (f'on {ayah} itself',
                    f'These are the notes on {ayah} itself, the verse the page is about. Every paragraph treats {ayah}; give each note every paragraph whose claim or question it bears on.')
                empty = f'when no paragraph treats what the note says (the writer still uses it: it shows what the tradition says that the page does not)'
            elif v == 'links':
                notes_are, where = (f'filed under other verses that the page does not cite, but that name {ayah}',
                    f'Each note is filed under another verse (shown at its end) and names {ayah} in passing: a parallel, a contrast, a shared word. Keep it for the paragraphs whose point it bears on.')
                empty = 'when it serves no paragraph'
            else:
                notes_are, where = (f'filed under {v}, a verse the page cites',
                    f'The page cites {v} in ' + ', '.join(f'¶{p}' for p in cited_in[v]) + f' (the verse text is at the top of your notes). '
                    'A note serves the paragraph whose point it bears on, whichever paragraph cites the verse: a note filed here may serve '
                    'none of the citing paragraphs and another one instead.')
                empty = 'when it serves no paragraph'
            agent = f"v8s_{run.replace('-', '_')}_{key}"
            spawn = LUNA
            for a, b in (('{AGENT}', agent), ('{RUN}', run), ('{AYAH}', ayah), ('{LABEL}', label), ('{KEY}', key),
                         ('{NOTES_ARE}', notes_are), ('{WHERE}', where), ('{EMPTY_MEANS}', empty), ('{N}', str(len(rs))),
                         ('{LAST_PAGE}', str(scope['parts']['page'] - 1)), ('{LAST_NOTES}', str(nparts - 1))):
                spawn = spawn.replace(a, b)
            (d / 'spawn' / f'sift_{key}.md').write_text(spawn)
            plan.append((key, len(rs), len(text)))
            total_chars += len(text)
    page_chars = sum(len((d / 'inputs' / f'page.p{k}.txt').read_text()) for k in range(scope['parts']['page']))
    json.dump({'agents': [k for k, *_ in plan]}, open(d / 'sift/plan.json', 'w'))
    print(f'sift: {len(plan)} agents, {sum(n for _, n, _ in plan):,} notes, {total_chars:,} chars of notes '
          f'+ page {page_chars:,} chars per agent ({len(plan) * page_chars:,} in all)')
    for key, n, c in sorted(plan, key=lambda x: -x[2]):
        print(f'  {key}: {n} notes, {c:,} chars')


# ---------------------------------------------------------------- check
def load(d, key):
    """(verdicts by n, problems)."""
    m = json.loads((d / 'sift/in' / f'{key}.map.json').read_text())
    N = len(m['ids'])
    paras = set(json.loads((d / 'scope.json').read_text())['paragraphs'])
    paras = {int(p) for p in paras}
    f = d / 'sift/out' / f'{key}.jsonl'
    if not f.exists():
        return m, {}, [f'{f.relative_to(ROOT)}: no file']
    got, problems = {}, []
    for i, ln in enumerate(f.read_text().splitlines(), 1):
        if not ln.strip():
            continue
        try:
            x = json.loads(ln)
        except ValueError as e:
            problems.append(f'line {i}: not JSON ({e})'); continue
        if not isinstance(x, dict):
            problems.append(f'line {i}: not a JSON object'); continue
        n = x.get('n')
        if not isinstance(n, int) or not 1 <= n <= N:
            problems.append(f'line {i}: n must be a note number 1…{N}'); continue
        if n in got:
            problems.append(f'#{n}: more than one line'); continue
        p = x.get('p')
        if not isinstance(p, list) or any(not isinstance(k, int) or k not in paras for k in p):
            problems.append(f'#{n}: p must be a list of paragraph numbers of this page ({min(paras)}…{max(paras)}), or []')
        if not (x.get('why') or '').strip():
            problems.append(f'#{n}: no why')
        if x.get('src') != m['srcs'][n - 1]:
            problems.append(f"#{n}: src {x.get('src')!r}, but note #{n} is from {m['srcs'][n - 1]} (verdicts shifted against the notes?)")
        got[n] = x
    missing = [n for n in range(1, N + 1) if n not in got]
    if missing:
        problems.append(f'{len(missing)} notes have no line: ' + ' '.join(f'#{n}' for n in missing[:80]) + (' …' if len(missing) > 80 else ''))
    return m, got, problems


def check(run, key):
    _, _, problems = load(d_of(run), key)
    print('OK' if not problems else '\n'.join(problems[:60]))


# ---------------------------------------------------------------- merge (report and writer)
def merged(run):
    """{id: {'p': set, 'why': [..], 'verse': v, 'agents': [...]}} and per-agent status."""
    d = d_of(run)
    plan = json.loads((d / 'sift/plan.json').read_text())['agents']
    out, status = {}, {}
    for key in plan:
        m, got, problems = load(d, key)
        status[key] = (len(m['ids']), got, problems)
        if problems:
            continue
        for n, i in enumerate(m['ids'], 1):
            e = out.setdefault(i, {'p': set(), 'why': [], 'agents': [], 'verses': []})
            if got[n]['p'] and m['verse'] != 'links':
                e['verses'].append(m['verse'])
            e['p'] |= set(got[n]['p'])
            e['why'].append(got[n]['why'])
            e['agents'].append(key)
    return out, status


def report(run):
    d = d_of(run)
    scope = json.loads((d / 'scope.json').read_text())
    db = sqlite3.connect(d / 'index.sqlite'); db.row_factory = sqlite3.Row
    out, status = merged(run)
    usd = 0.0
    print(f"# {run}: sift of {scope['ayah']}\n")
    for key, (N, got, problems) in status.items():
        agent = f"v8s_{run.replace('-', '_')}_{key}"
        rj = d / 'runs' / agent / 'run.json'
        cost = ''
        if rj.exists():
            x = json.loads(rj.read_text())
            usd += x.get('usd_equivalent') or 0
            cost = (f" · ${x.get('usd_equivalent', 0):.3f} eq, peak {x.get('max_request_input_tokens')} tok, rc {x.get('returncode')}, "
                    f"completed {x.get('turn_completed')}" + (' · OVER CONTEXT CAP' if x.get('over_context_cap') else ''))
        if problems:
            print(f'NOT DONE {key}: {N} notes; {problems[0]}' + (f' (+{len(problems) - 1} more problems)' if len(problems) > 1 else '') + cost)
        else:
            kept = sum(1 for x in got.values() if x['p'])
            print(f'{key}: {N} notes, kept {kept}, [] {N - kept}{cost}')
    focus = {r[0] for r in db.execute('SELECT id FROM notes WHERE verse=?', (scope['ayah'],))}
    per_p = defaultdict(set)
    for i, e in out.items():
        for p in e['p']:
            per_p[p].add(i)
    kept_other = {i for i, e in out.items() if e['p'] and i not in focus}
    chars = sum(len(q.line(dict(db.execute('SELECT * FROM notes WHERE id=?', (i,)).fetchone()))) for i in kept_other)
    print(f"\nnotes judged {len(out):,}; kept {sum(1 for e in out.values() if e['p']):,} "
          f"(focus {len([i for i in focus if out.get(i, {}).get('p')])} of {len(focus)}, other {len(kept_other):,}: {chars:,} chars in full)")
    print('per paragraph (focus + other): ' + ', '.join(f"¶{p} {len(per_p[p] & focus)}+{len(per_p[p] - focus)}" for p in sorted(per_p)))
    multi = sum(1 for e in out.values() if len(e['p']) > 1)
    print(f'notes kept for more than one paragraph: {multi}')
    print(f'Luna total: ${usd:.3f} API-equivalent (actual $0 on the subscription)')


# ---------------------------------------------------------------- writer inputs
def writer(run):
    d = d_of(run)
    scope = json.loads((d / 'scope.json').read_text())
    ayah = scope['ayah']
    db = sqlite3.connect(d / 'index.sqlite'); db.row_factory = sqlite3.Row
    out, status = merged(run)
    bad = [k for k, (_, _, pr) in status.items() if pr]
    if bad:
        raise SystemExit(f'NOT DONE: {len(bad)} sift agents have no valid output: {" ".join(bad)}; no writer inputs built')
    row = lambda i: dict(db.execute('SELECT * FROM notes WHERE id=?', (i,)).fetchone())
    # focus notes, every one, with the paragraphs the sift gave it
    focus = order([dict(r) for r in db.execute('SELECT * FROM notes WHERE verse=?', (ayah,))])
    lines, cur = [f'# {ayah}: every tier-1 note ({len(focus)}), oldest author first; → the paragraphs the sift assigned it '
                  '("→ none": no paragraph treats what it says)'], None
    for r in focus:
        if r['src'] != cur:
            cur = r['src']
            lines.append(f"\n## {r['src']}: {r['author']}" + (f", d. {r['death']} AH" if r['death'] else ''))
        p = sorted(out.get(r['id'], {}).get('p', ()))
        lines.append(q.line(r) + '  → ' + (' '.join(f'¶{k}' for k in p) if p else 'none'))
    nf = q.parts(d / 'inputs', 'focus-sifted', '\n'.join(lines), f'{ayah} notes with assignments')
    # other notes: per paragraph the ids, then each kept note once, in full, by the verse it is filed under
    fids = {r['id'] for r in focus}
    other = {i: e for i, e in out.items() if e['p'] and i not in fids}
    per_p = defaultdict(list)
    for i, e in other.items():
        for p in e['p']:
            per_p[p].append(i)
    txt = ['# Notes filed under the verses the page cites (and notes elsewhere that name ' + ayah + ') that the sift kept, '
           'each once, by the verse it is filed under; → the paragraphs the sift assigned it']
    rows = []
    for i in other:
        r = row(i)
        if other[i]['verses']:                 # file it under the verse whose agent kept it
            r['verse'] = sorted(other[i]['verses'], key=vkey)[0]
        rows.append(r)
    rows.sort(key=lambda r: (vkey(r['verse']), r['death'] if isinstance(r['death'], int) else 9999, r['src'], r['id']))
    cur = None
    for r in rows:
        if r['verse'] != cur:
            cur = r['verse']
            txt.append(f'\n### filed under {cur}')
        txt.append(q.line(r) + '  → ' + ' '.join(f'¶{k}' for k in sorted(other[r['id']]['p'])))
    text = '\n'.join(txt)
    no = q.parts(d / 'inputs', 'sifted', text, 'sifted notes')
    arm = 'opus-sift'
    cites = '\n'.join(f"¶{p}: {', '.join(vs)}" for p, vs in sorted(((int(p), vs) for p, vs in scope['cites'].items())))
    spawn = WRITE
    for a, b in (('{MARK}', f'<!-- v8-test-run: enrichment/v8/work/{run}/write/{arm} | model claude-opus-5-5 -->'),
                 ('{RUN}', run), ('{ARM}', arm), ('{AYAH}', ayah), ('{CITES}', cites),
                 ('{LASTP}', str(max(int(x) for x in scope['paragraphs']))),
                 ('{LAST_PAGE}', str(scope['parts']['page'] - 1)), ('{LAST_FOCUS}', str(nf - 1)), ('{LAST_SIFTED}', str(no - 1))):
        spawn = spawn.replace(a, b)
    (d / 'write' / arm).mkdir(parents=True, exist_ok=True)
    sp = d / 'write' / arm / 'spawn.md'          # not in spawn/: run_codex.py runs every file there
    sp.write_text(spawn)
    page = ''.join((d / 'inputs' / f'page.p{k}.txt').read_text() for k in range(scope['parts']['page']))
    ftext = '\n'.join(lines)
    tok = sum(tokens(x) for x in (page, ftext, text, spawn))
    print(f'writer inputs: focus {len(focus)} notes ({len(ftext):,} chars, {nf} parts); other kept {len(other):,} notes '
          f'({len(text):,} chars, {no} parts); spawn {sp.relative_to(ROOT)}')
    print(f'writer context before any search: ~{tok / 1000:.0f}k tokens (Arabic 2 chars/token, other 4)')


def main():
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    if a[0] == 'build':
        mc = int(a[a.index('--max-chars') + 1]) if '--max-chars' in a else 200_000
        build(a[1], a[a.index('--ayah') + 1], a[a.index('--page') + 1], mc)
    elif a[0] == 'check':
        check(a[1], a[2])
    elif a[0] == 'report':
        report(a[1])
    elif a[0] == 'writer':
        writer(a[1])
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main()
