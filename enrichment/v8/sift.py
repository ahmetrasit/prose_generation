#!/usr/bin/env python3
"""Enrichment v8: per-reference sift against a claim map.
Step 1: one Luna agent writes the page's claim map (every claim per paragraph, ids like 4a).
Step 2: Luna agents, one per cited verse (the focus ayah included; a verse above --max-chars is split at note
boundaries), plus one for notes elsewhere that name the focus ayah, read the page, the claim map and every note filed
under their verse, and grade each note: core (bears on claims, listed), context (background for paragraphs), off.
Nothing is trimmed: every note gets a grade, and the check refuses a file that skips one.
Step 3: the Opus writer gets the page, the claim map, every focus note with its grade, every core note in full, and
q.py (whose results show each note's grade) to search further.

  sift.py build RUN --ayah A --page PATH [--max-chars 50000] [--claims luna|opus]   index + page, sift inputs, spawn files
  sift.py check-claims RUN                                      the claim map; writes sift/claims.txt when OK
  sift.py check RUN KEY                                         one agent's output: one grade per note
  sift.py report RUN                                            per agent: done, grades, cost; per paragraph
  sift.py writer RUN                                            writer inputs + Opus spawn file

Spawn files: work/RUN/spawn/claims.md first, then work/RUN/spawn/sift_*.md; run with enrichment/v5/run_codex.py
(outputs land in work/RUN/runs/).
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
CLAIMS = {'luna': (HERE / 'briefs/claims.md').read_text(), 'opus': (HERE / 'briefs/claims-opus.md').read_text()}
RANK = {'core': 2, 'context': 1, 'off': 0}
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
def build(run, ayah, page, max_chars, claims_model='luna'):
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
            head = [f'# {len(rs)} notes filed under {label}' + (f' (group {k} of {len(chunks)} of this verse\'s notes)' if len(chunks) > 1 else ''),
                    *( [f'verse {v}: {qt[0]}'] if qt else [] ), '']
            lines = []
            for n, r in enumerate(rs, 1):
                lines.append(f'#{n} ' + short(r) + (f'   [filed under {r["verse"]}]' if v == 'links' else ''))
            text = '\n'.join(head + lines)
            nparts = q.parts(d / 'sift/in', key, text, f'notes for {key}')
            json.dump({'key': key, 'verse': v, 'ids': [r['id'] for r in rs], 'srcs': [r['src'] for r in rs]}, open(d / 'sift/in' / f'{key}.map.json', 'w'), ensure_ascii=False)
            if v == ayah:
                notes_are, where = (f'on {ayah} itself',
                    f'These are the notes on {ayah} itself, the verse the page is about. The writer receives every one of them anyway; your grade tells it which claims each bears on. '
                    f'Grade off only a note that bears on no claim (the writer uses those to show what the tradition says that the page does not).')
            elif v == 'links':
                notes_are, where = (f'filed under other verses that the page does not cite, but that name {ayah}',
                    f'Each note is filed under another verse (shown at its end) and names {ayah} in passing: a parallel, a contrast, a shared word.')
            else:
                notes_are, where = (f'filed under {v}, a verse the page cites',
                    f'The page cites {v} in ' + ', '.join(f'¶{p}' for p in cited_in[v]) + f' (the verse text is at the top of your notes); '
                    f'the claims that use it list {v} under `verses`. Those claims are the first place to look, but a note filed here may '
                    'bear on any claim of the page, and many notes on a verse bear on none.')
            agent = f"v8s_{run.replace('-', '_')}_{key}"
            spawn = LUNA
            for a, b in (('{AGENT}', agent), ('{RUN}', run), ('{AYAH}', ayah), ('{LABEL}', label), ('{KEY}', key),
                         ('{NOTES_ARE}', notes_are), ('{WHERE}', where), ('{N}', str(len(rs))),
                         ('{LAST_PAGE}', str(scope['parts']['page'] - 1)), ('{LAST_NOTES}', str(nparts - 1))):
                spawn = spawn.replace(a, b)
            (d / 'spawn' / f'sift_{key}.md').write_text(spawn)
            plan.append((key, len(rs), len(text)))
            total_chars += len(text)
    cs = CLAIMS[claims_model]
    for a, b in (('{AGENT}', f"v8c_{run.replace('-', '_')}_claims"), ('{RUN}', run), ('{AYAH}', ayah),
                 ('{LAST_PAGE}', str(scope['parts']['page'] - 1)), ('{LASTP}', str(max(int(x) for x in scope['paragraphs'])))):
        cs = cs.replace(a, b)
    # Luna: spawn/claims.md (run with run_codex.py, first); Opus: sift/claims-spawn.md (an agent reads it; not in spawn/)
    (d / ('spawn/claims.md' if claims_model == 'luna' else 'sift/claims-spawn.md')).write_text(cs)
    page_chars = sum(len((d / 'inputs' / f'page.p{k}.txt').read_text()) for k in range(scope['parts']['page']))
    json.dump({'agents': [k for k, *_ in plan]}, open(d / 'sift/plan.json', 'w'))
    print(f'sift: {len(plan)} agents, {sum(n for _, n, _ in plan):,} notes, {total_chars:,} chars of notes '
          f'+ page {page_chars:,} chars per agent ({len(plan) * page_chars:,} in all); claim map: {"spawn/claims.md" if claims_model == "luna" else "sift/claims-spawn.md"} ({claims_model}, run first)')
    for key, n, c in sorted(plan, key=lambda x: -x[2]):
        print(f'  {key}: {n} notes, {c:,} chars')


# ---------------------------------------------------------------- claim map
def claims(d):
    """(claims in order, problems)."""
    scope = json.loads((d / 'scope.json').read_text())
    paras = sorted(int(x) for x in scope['paragraphs'])
    page_verses = {v for vs in scope['cites'].values() for v in vs}
    f = d / 'sift/claims.jsonl'
    if not f.exists():
        return [], [f'{f.relative_to(ROOT)}: no file']
    out, problems, ids = [], [], set()
    for i, ln in enumerate(f.read_text().splitlines(), 1):
        if not ln.strip():
            continue
        try:
            x = json.loads(ln)
        except ValueError as e:
            problems.append(f'line {i}: not JSON ({e})'); continue
        if not isinstance(x, dict):
            problems.append(f'line {i}: not a JSON object'); continue
        cid, pn = x.get('id'), x.get('p')
        if not isinstance(pn, int) or pn not in paras:
            problems.append(f'line {i}: p must be a paragraph number {paras[0]}…{paras[-1]}'); continue
        if not isinstance(cid, str) or not re.fullmatch(rf'{pn}[a-z]', cid):
            problems.append(f'line {i}: id must be the paragraph number and a letter, e.g. {pn}a'); continue
        if cid in ids:
            problems.append(f'{cid}: more than one line'); continue
        if not (x.get('claim') or '').strip():
            problems.append(f'{cid}: no claim')
        if not isinstance(x.get('terms'), list) or not isinstance(x.get('verses'), list):
            problems.append(f'{cid}: terms and verses must be lists')
        elif any(v not in page_verses for v in x['verses']):
            problems.append(f"{cid}: verses not cited on the page: {', '.join(v for v in x['verses'] if v not in page_verses)}")
        ids.add(cid)
        out.append(x)
    miss = [n for n in paras if not any(c['p'] == n for c in out)]
    if miss:
        problems.append('paragraphs with no claim: ' + ' '.join(f'¶{n}' for n in miss))
    return out, problems


def claims_text(cs):
    out, cur = ['# Claim map of the page: id, claim, terms, verses'], None
    for c in cs:
        if c['p'] != cur:
            cur = c['p']
            out.append(f'\n## ¶{cur}')
        out.append(f"{c['id']}: {c['claim']}" + (f"  · terms: {', '.join(c['terms'])}" if c['terms'] else '')
                   + (f"  · verses: {', '.join(c['verses'])}" if c['verses'] else ''))
    return '\n'.join(out) + '\n'


def check_claims(run):
    d = d_of(run)
    cs, problems = claims(d)
    if problems:
        print('\n'.join(problems[:60]))
        return
    (d / 'sift/claims.txt').write_text(claims_text(cs))
    print('OK')


# ---------------------------------------------------------------- check
def load(d, key):
    """(map, grades by n, problems)."""
    m = json.loads((d / 'sift/in' / f'{key}.map.json').read_text())
    N = len(m['ids'])
    paras = {int(p) for p in json.loads((d / 'scope.json').read_text())['paragraphs']}
    cids = {c['id'] for c in claims(d)[0]}
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
        g = x.get('g')
        if g == 'core':
            c = x.get('c')
            if not isinstance(c, list) or not c or any(k not in cids for k in c):
                problems.append(f'#{n}: core needs c, a non-empty list of claim ids from the claim map')
        elif g == 'context':
            pp = x.get('p')
            if not isinstance(pp, list) or not pp or any(not isinstance(k, int) or k not in paras for k in pp):
                problems.append(f'#{n}: context needs p, a non-empty list of paragraph numbers ({min(paras)}…{max(paras)})')
        elif g != 'off':
            problems.append(f'#{n}: g must be core, context or off')
        if not (x.get('why') or '').strip():
            problems.append(f'#{n}: no why')
        if x.get('src') != m['srcs'][n - 1]:
            problems.append(f"#{n}: src {x.get('src')!r}, but note #{n} is from {m['srcs'][n - 1]} (grades shifted against the notes?)")
        got[n] = x
    missing = [n for n in range(1, N + 1) if n not in got]
    if missing:
        problems.append(f'{len(missing)} notes have no line: ' + ' '.join(f'#{n}' for n in missing[:80]) + (' …' if len(missing) > 80 else ''))
    return m, got, problems


def check(run, key):
    _, _, problems = load(d_of(run), key)
    print('OK' if not problems else '\n'.join(problems[:60]))


# ---------------------------------------------------------------- merge (report, writer, q.py marks)
def merged(run_dir):
    """{id: {'g': best grade, 'c': claim ids, 'p': paragraphs (core: of its claims), 'why': [..], 'verses': [...]}}
    and per-agent status. A note on several verses takes its highest grade and the union of claims/paragraphs."""
    d = run_dir
    plan = json.loads((d / 'sift/plan.json').read_text())['agents']
    out, status = {}, {}
    for key in plan:
        m, got, problems = load(d, key)
        status[key] = (len(m['ids']), got, problems)
        if problems:
            continue
        for n, i in enumerate(m['ids'], 1):
            x = got[n]
            e = out.setdefault(i, {'g': 'off', 'c': set(), 'p': set(), 'why': [], 'verses': []})
            if RANK[x['g']] > RANK[e['g']]:
                e['g'] = x['g']
            if x['g'] == 'core':
                e['c'] |= set(x['c'])
                e['p'] |= {int(re.match(r'\d+', k)[0]) for k in x['c']}
                if m['verse'] != 'links':
                    e['verses'].append(m['verse'])
            elif x['g'] == 'context':
                e['p'] |= set(x['p'])
            e['why'].append(f"{x['g']}: {x['why']}")
    return out, status


def mark(e):
    """The sift's grade on a note, as the writer sees it."""
    if e['g'] == 'core':
        return '  → core ' + ' '.join(sorted(e['c'], key=lambda k: (int(re.match(r'\d+', k)[0]), k)))
    if e['g'] == 'context':
        return '  → context ' + ' '.join(f'¶{k}' for k in sorted(e['p']))
    return '  → off: ' + e['why'][0].split(': ', 1)[1]


def report(run):
    d = d_of(run)
    scope = json.loads((d / 'scope.json').read_text())
    db = sqlite3.connect(d / 'index.sqlite'); db.row_factory = sqlite3.Row
    cs, cp = claims(d)
    print(f"# {run}: sift of {scope['ayah']}\n")
    print(f'claim map: {len(cs)} claims' + (f'; NOT DONE: {cp[0]}' if cp else ''))
    out, status = merged(d)
    usd = 0.0
    for name in ['claims'] + list(status):
        agent = f"v8c_{run.replace('-', '_')}_claims" if name == 'claims' else f"v8s_{run.replace('-', '_')}_{name}"
        rj = d / 'runs' / agent / 'run.json'
        cost = ''
        if rj.exists():
            x = json.loads(rj.read_text())
            usd += x.get('usd_equivalent') or 0
            cost = (f" · ${x.get('usd_equivalent', 0):.3f} eq, peak {x.get('max_request_input_tokens')} tok, rc {x.get('returncode')}, "
                    f"completed {x.get('turn_completed')}" + (' · OVER CONTEXT CAP' if x.get('over_context_cap') else ''))
        if name == 'claims':
            if cost:
                print(f'claims agent{cost}')
            continue
        N, got, problems = status[name]
        if problems:
            print(f'NOT DONE {name}: {N} notes; {problems[0]}' + (f' (+{len(problems) - 1} more problems)' if len(problems) > 1 else '') + cost)
        else:
            c = Counter(x['g'] for x in got.values())
            print(f"{name}: {N} notes, core {c['core']}, context {c['context']}, off {c['off']}{cost}")
    focus = {r[0] for r in db.execute('SELECT id FROM notes WHERE verse=?', (scope['ayah'],))}
    g = Counter(e['g'] for i, e in out.items() if i not in focus)
    gf = Counter(out[i]['g'] for i in focus if i in out)
    core_other = [i for i, e in out.items() if e['g'] == 'core' and i not in focus]
    chars = sum(len(q.line(dict(db.execute('SELECT * FROM notes WHERE id=?', (i,)).fetchone()))) for i in core_other)
    print(f"\nnotes graded {len(out):,}. focus ({len(focus)}): core {gf['core']}, context {gf['context']}, off {gf['off']}. "
          f"other: core {g['core']:,}, context {g['context']:,}, off {g['off']:,}; core other in full {chars:,} chars")
    per_c = Counter(k for i, e in out.items() if e['g'] == 'core' and i not in focus for k in e['c'])
    per_p = Counter(p for i, e in out.items() if e['g'] == 'core' and i not in focus for p in e['p'])
    print('core other notes per paragraph: ' + ', '.join(f'¶{p} {n}' for p, n in sorted(per_p.items())))
    print('claims with no core note (focus or other): ' + (', '.join(c['id'] for c in cs if not any(c['id'] in e['c'] for e in out.values())) or 'none'))
    print(f'core notes on more than one claim: {sum(1 for e in out.values() if len(e["c"]) > 1)}')
    print(f'Luna total: ${usd:.3f} API-equivalent (actual $0 on the subscription)')


# ---------------------------------------------------------------- writer inputs
def writer(run):
    d = d_of(run)
    scope = json.loads((d / 'scope.json').read_text())
    ayah = scope['ayah']
    db = sqlite3.connect(d / 'index.sqlite'); db.row_factory = sqlite3.Row
    cs, cp = claims(d)
    out, status = merged(d)
    bad = [k for k, (_, _, pr) in status.items() if pr]
    if cp or bad:
        raise SystemExit(f'NOT DONE: claim map {"invalid" if cp else "ok"}; {len(bad)} sift agents have no valid output: '
                         f'{" ".join(bad)}; no writer inputs built')
    row = lambda i: dict(db.execute('SELECT * FROM notes WHERE id=?', (i,)).fetchone())
    focus = order([dict(r) for r in db.execute('SELECT * FROM notes WHERE verse=?', (ayah,))])
    lines, cur = [f'# {ayah}: every tier-1 note ({len(focus)}), oldest author first, each with the first reader\'s grade '
                  '(→ core: the claims it bears on; → context / off: no claim)'], None
    for r in focus:
        if r['src'] != cur:
            cur = r['src']
            lines.append(f"\n## {r['src']}: {r['author']}" + (f", d. {r['death']} AH" if r['death'] else ''))
        lines.append(q.line(r) + (mark(out[r['id']]) if r['id'] in out else '  → not graded'))
    ftext = '\n'.join(lines)
    nf = q.parts(d / 'inputs', 'focus-sifted', ftext, f'{ayah} notes with grades')
    fids = {r['id'] for r in focus}
    other = {i: e for i, e in out.items() if e['g'] == 'core' and i not in fids}
    txt = [f'# Core notes filed under the verses the page cites (and notes elsewhere that name {ayah}), each once, in full, '
           'by the verse it is filed under; → the claims the first reader found it bears on']
    rows = []
    for i in other:
        r = row(i)
        if other[i]['verses']:                 # file it under the verse whose agent graded it core
            r['verse'] = sorted(other[i]['verses'], key=vkey)[0]
        rows.append(r)
    rows.sort(key=lambda r: (vkey(r['verse']), r['death'] if isinstance(r['death'], int) else 9999, r['src'], r['id']))
    cur = None
    for r in rows:
        if r['verse'] != cur:
            cur = r['verse']
            txt.append(f'\n### filed under {cur}')
        txt.append(q.line(r) + mark(other[r['id']]))
    text = '\n'.join(txt)
    no = q.parts(d / 'inputs', 'sifted', text, 'core notes')
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
    ctext = (d / 'sift/claims.txt').read_text()
    tok = sum(tokens(x) for x in (page, ctext, ftext, text, spawn))
    print(f'writer inputs: claims {len(cs)}; focus {len(focus)} notes ({len(ftext):,} chars, {nf} parts); core other {len(other):,} notes '
          f'({len(text):,} chars, {no} parts); context notes reachable through q.py: {sum(1 for e in out.values() if e["g"] == "context"):,}; '
          f'spawn {sp.relative_to(ROOT)}')
    print(f'writer context before any search: ~{tok / 1000:.0f}k tokens (Arabic 2 chars/token, other 4)')


def main():
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    if a[0] == 'build':
        mc = int(a[a.index('--max-chars') + 1]) if '--max-chars' in a else 50_000
        cm = a[a.index('--claims') + 1] if '--claims' in a else 'luna'
        build(a[1], a[a.index('--ayah') + 1], a[a.index('--page') + 1], mc, cm)
    elif a[0] == 'check-claims':
        check_claims(a[1])
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
