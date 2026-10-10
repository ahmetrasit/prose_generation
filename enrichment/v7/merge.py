#!/usr/bin/env python3
"""Enrichment v7 tier 2: consolidated views per verse, built cell by cell from the tier-1 rows. Launches no model.

A cell is one verse word (or the whole verse) × one type, from the row tags (digest.TYPES; tags come from the row
itself or from a retag run). The script prints a verse's rows grouped by cell; the agent groups each cell's rows
into distinct views and never merges across cells. A verse too large for one context is split into slices of whole
cells, so no merging across slices is ever needed. The script fills in each view's word, type, holders, sources and
stances from the row ids, so nothing is retyped.

  merge.py build RUN --from luna-max (--ayat 95:1 6:99 … | --page PATH --ayah A) --models gpt-6-sol:high [--whole]
            --whole: no cells and no row tags needed; each verse is one slice and the agent labels every view with
            its verse words and type (briefs/merge-whole.md)
  merge.py check RUN [--model TAG] [--ayah 95:1 --slice s1]   the agent runs it with --ayah and --slice until OK;
                                                              without them: checks every slice, assembles each verse
  merge.py update RUN --model TAG    rows added since tier 2 ran: rebuild only the cells that gained rows (new slices)
  merge.py report RUN                costs, views, rows

Files: RUN/tier2/rows/<k>.json (rows by id), <k>.cells.json, <k>.<slice>.pK.txt (input parts), RUN/tier2/spawn,
RUN/tier2/runs, RUN/tier2/out/<TAG>/<k>.<slice>.jsonl (agent output), <k>.jsonl and <k>.md (the assembled verse).
"""
import argparse
import json
from collections import defaultdict

import digest
from digest import PART_CHARS, ROOT, TYPES, V7, WHOLE, connect, dump, run_dir

BRIEF = V7 / 'briefs/merge.md'
BRIEF_WHOLE = V7 / 'briefs/merge-whole.md'
WHOLE_CELL = 'verse'   # the single cell of a --whole run
SLICE_CHARS = 90_000   # input characters per agent; a single larger cell stands alone (printed)
UNTAGGED = 'untagged'


def key(ayah):
    return ayah.replace(':', '-')


_TAGS = None
_FILES = {}
_BAD_SUPPLEMENT = set()
_MISSING_LOC = set()


def _segments(f):
    """Verified segment lines, cached while the output, manifest and corpus stay unchanged."""
    try:
        st = f.stat()
        manifest = (f.parents[2] / 'manifest.json').stat()
        corpus = (ROOT / 'enrichment/corpus/corpus.sqlite').stat()
        version = (st.st_mtime_ns, st.st_size, manifest.st_mtime_ns, manifest.st_size,
                   corpus.st_mtime_ns, corpus.st_size,
                   digest.run_state(f.parents[2] / 'runs' / f'v7d_{f.parts[-4]}_{f.parts[-2]}_{f.stem}'))
        if _FILES.get(f, (None,))[0] == version:
            return _FILES[f][1]
        lines = f.read_text().splitlines()
    except FileNotFoundError:
        print(f'WARNING {f.relative_to(V7)}: vanished while reading (a run in progress?); skipped')
        return []
    valid = digest.valid_output_locs(f)
    out = []
    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            x = json.loads(line)
        except ValueError:
            print(f'WARNING {f.relative_to(V7)} line {i}: not JSON (a run in progress?); skipped')
            continue
        if isinstance(x, dict) and x.get('loc') in valid:
            out.append(x)
    _FILES[f] = (version, out)
    return out


def tier1_segments(tags):
    """(tag, verified segment line, cut, whole_again), counted once by tag then run order.
    Unresolved legacy inputs, excerpts, stale sources and invalid outputs cannot supply current notes."""
    tags = [tags] if isinstance(tags, str) else list(tags)
    seen = set()
    for tag in tags:
        for f in sorted((V7 / 'work').glob(f'*/out/{tag}/c*.jsonl')):  # tier 1 of every run: one database
            if digest.unfinished(f):
                continue
            for x in _segments(f):
                cut = x['loc'] in digest.excerpts().get(f.parts[-4], set())
                whole_again = not cut and any(x['loc'] in v for v in digest.excerpts().values())
                if (x['loc'], cut) in seen:
                    continue
                seen.add((x['loc'], cut))
                yield tag, x, cut, whole_again


def supplements(tags):
    """(tag, run, segment line) for every finished recheck output (enrichment/v7/recheck/RUN/out/TAG/cNN.jsonl):
    notes a recheck run added to an already digested segment, for verses its notes did not name (recheck.py). Lines
    pass the same validation as digests (_segments: digest.valid_output_locs against the run's manifest, whose chunks
    carry source_sha256), so a stale or invalid line supplies no notes."""
    tags = [tags] if isinstance(tags, str) else list(tags)
    seen = set()                     # (loc, run): counted once, first tag wins, as tier1_segments does for digests
    for tag in tags:
        for f in sorted((V7 / 'recheck').glob(f'*/out/{tag}/c*.jsonl')):
            if digest.unfinished(f):
                continue
            bad = 0
            for x in _segments(f):
                if not (isinstance(x, dict) and isinstance(x.get('loc'), str) and isinstance(x.get('rows'), list)):
                    bad += 1
                    continue
                bad += sum(not isinstance(r, dict) for r in x['rows'])
                if (x['loc'], f.parts[-4]) in seen:
                    continue
                seen.add((x['loc'], f.parts[-4]))
                yield tag, f.parts[-4], x
            if bad and f not in _BAD_SUPPLEMENT:
                _BAD_SUPPLEMENT.add(f)
                print(f'WARNING {f.relative_to(V7)}: {bad} malformed line(s) or note(s) not read (recheck.py check)')


def full_row(r, n, x, whole_again, tag, src, meta, rid=None):
    rid = rid or f"{x['loc']}/{'f' if whole_again else 'r'}{n}"
    words, typ = (r.get('words'), r.get('type')) if r.get('type') else _TAGS.get(rid, (None, None))
    m = meta.get(src, {})
    return {**r, 'id': rid, 'src': src, 'author': m.get('author') or src, 'death': m.get('death_ah'), 'tag': tag,
            'words': words, 'type': typ}


def tier1_rows(d, tags, ayah, quiet=False, mentions=True):
    """Every tier-1 row about the ayah, with a stable id <loc>/rN (N = position in its segment) and its tags (words,
    type) from the row or a retag run. tags: one model tag or a list; a segment digested under several runs or tags
    counts once (first tag, then run order). No edition rule (removed 2026-10-09): rows of a short edition X were dropped when
    X-FULL has rows on the same ayah (printed).
    A row is about the ayah when its `verses` name it, ranges and lists included ("105:3-5", "92:7,10,12"), or when only
    its `mentions` name it: a point about another verse that quotes or names this one. Such a row gets via='mentions'
    and about=<its verses> (2026-10-10: a digest serves every verse it names; nothing is digested twice). mentions=False
    leaves those out (v7 tier 2, whose cells are verse words)."""
    return tier1_rows_by_verse(tags, [ayah], mentions)[ayah]


def tier1_rows_by_verse(tags, ayat, mentions=True):
    """tier1_rows for many verses in one pass over tier 1: verse -> its rows, with the same ids, fields and order as
    tier1_rows gives for that verse alone. Each verse gets its own row dicts; their list values (verses, mentions,
    words) are shared with the digest cache, as before: callers read rows and never change them in place."""
    global _TAGS
    if _TAGS is None:
        _TAGS = digest.row_tags()
    want = set(ayat)
    out = {ayah: [] for ayah in ayat}

    def file_row(row, vs, mentioned):
        for ayah in want.intersection(vs):
            out[ayah].append(dict(row))
        if mentions:
            for ayah in want.intersection(mentioned) - set(vs):
                out[ayah].append({**row, 'via': 'mentions', 'about': list(vs)})

    with connect() as con:
        meta = {i: json.loads(m or '{}') for i, m in con.execute('SELECT id, meta FROM src')}
        seg_src = {}
        for tag, x, cut, whole_again in tier1_segments(tags):
            for n, r in enumerate(x['rows'], 1):
                vs = digest.verse_list(r.get('verses'))
                mentioned = digest.verse_list(r.get('mentions')) if mentions else []
                if not want.intersection(vs) and not want.intersection(mentioned):
                    continue
                if x['loc'] not in seg_src:
                    seg_src[x['loc']] = con.execute('SELECT src FROM seg WHERE seg=?', (x['loc'],)).fetchone()[0]
                file_row(full_row(r, n, x, whole_again, tag, seg_src[x['loc']], meta), vs, mentioned)
        for tag, run, x in supplements(tags):     # recheck notes: ids <loc>/x<N>-<RUN>
            for n, r in enumerate(x['rows'], 1):
                if not isinstance(r, dict):
                    continue
                vs = digest.verse_list(r.get('verses'))
                mentioned = digest.verse_list(r.get('mentions')) if mentions else []
                if not want.intersection(vs) and not want.intersection(mentioned):
                    continue
                if x['loc'] not in seg_src:
                    hit = con.execute('SELECT src FROM seg WHERE seg=?', (x['loc'],)).fetchone()
                    if hit is None:
                        if x['loc'] not in _MISSING_LOC:
                            _MISSING_LOC.add(x['loc'])
                            print(f"WARNING recheck {run}: {x['loc']} is not in the corpus index; its notes are not read")
                        seg_src[x['loc']] = None
                        continue
                    seg_src[x['loc']] = hit[0]
                if seg_src[x['loc']] is None:
                    continue
                file_row(full_row(r, n, x, False, tag, seg_src[x['loc']], meta, rid=f"{x['loc']}/x{n}-{run}"),
                         vs, mentioned)
    return out  # no edition rule: short and FULL editions are both kept (user, 2026-10-09: nothing dropped)


def segment_rows(tags, locs, digested=None):
    """loc -> its tier-1 rows (as tier1_rows gives them, whatever verse they are about), for the given locators. A
    segment digested both as an excerpt and whole gives the rows of both, as in tier1_rows. digested: a set that
    receives the locators with a valid digest; a locator in the result but not in it has recheck notes only."""
    global _TAGS
    if _TAGS is None:
        _TAGS = digest.row_tags()
    want, out = set(locs), {}
    if digested is None:
        digested = set()
    with connect() as con:
        meta = {i: json.loads(m or '{}') for i, m in con.execute('SELECT id, meta FROM src')}
        for tag, x, cut, whole_again in tier1_segments(tags):
            if x['loc'] in want:
                digested.add(x['loc'])
                src = con.execute('SELECT src FROM seg WHERE seg=?', (x['loc'],)).fetchone()[0]
                out.setdefault(x['loc'], []).extend(full_row(r, n, x, whole_again, tag, src, meta)
                                                    for n, r in enumerate(x['rows'], 1))
        for tag, run, x in supplements(tags):
            if x['loc'] in want:             # a valid supplement remains evidence even if its base is unresolved
                hit = con.execute('SELECT src FROM seg WHERE seg=?', (x['loc'],)).fetchone()
                if hit is None:
                    if x['loc'] not in _MISSING_LOC:
                        _MISSING_LOC.add(x['loc'])
                        print(f"WARNING recheck {run}: {x['loc']} is not in the corpus index; its notes are not read")
                    continue
                src = hit[0]
                out.setdefault(x['loc'], []).extend(full_row(r, n, x, False, tag, src, meta, rid=f"{x['loc']}/x{n}-{run}")
                                     for n, r in enumerate(x['rows'], 1) if isinstance(r, dict))
    return out


def cell_of(r, ayah):
    """(cell id, word label, type) of a row on this ayah: its first tag word found in the verse, else the whole verse."""
    typ = r.get('type') if r.get('type') in TYPES else UNTAGGED
    toks = digest.verse_tokens(ayah)
    for w in r.get('words') or []:
        if w == WHOLE:
            continue
        pos = digest.word_position(w, ayah)
        if pos is not None:
            return f'w{pos + 1}-{typ}', f'{toks[pos][0]} (word {pos + 1})', typ
    return f'all-{typ}', 'whole verse', typ


def cell_order(cid):
    w, typ = cid.split('-', 1)
    return (0 if w == 'all' else int(w[1:]), TYPES.index(typ) if typ in TYPES else len(TYPES))


def cells(ayah, rows):
    """cell id -> {'word', 'type', 'rows': [ids]} in verse-word then type order; rows sorted oldest author first."""
    out = {}
    rows = sorted(rows, key=lambda r: (r['death'] if isinstance(r['death'], int) else 9999, r['src'], r['id']))
    for r in rows:
        cid, word, typ = cell_of(r, ayah)
        out.setdefault(cid, {'word': word, 'type': typ, 'rows': []})['rows'].append(r['id'])
    return dict(sorted(out.items(), key=lambda kv: cell_order(kv[0])))


def row_line(r):
    who = r['src'] + (f", d. {r['death']}" if r['death'] else '')
    mentions = f" | mentions {', '.join(r.get('mentions') or [])}" if r.get('mentions') else ''
    about = f"(about {', '.join(r.get('about') or []) or 'another verse'}; names this verse) " if r.get('via') == 'mentions' else ''
    return f"[{r['id']}] {who} · {r['speaker']} | {r['stance']} | {about}{r['claim']}{mentions}"


def cell_text(cid, c, by_id):
    return (f"\n### cell {cid} · {c['word']} · {c['type']} · {len(c['rows'])} notes\n"
            + '\n'.join(row_line(by_id[i]) for i in c['rows']) + '\n')


def pack(cs, by_id, ayah):
    """Slices of whole cells, each at most SLICE_CHARS of input (a larger single cell stands alone, printed)."""
    slices, cur, size = [], [], 0
    for cid, c in cs.items():
        n = len(cell_text(cid, c, by_id))
        if n > SLICE_CHARS:
            print(f'NOTE {ayah}: cell {cid} alone is {n:,} characters, over the {SLICE_CHARS:,} slice size; it gets its own slice')
        if cur and size + n > SLICE_CHARS:
            slices.append(cur)
            cur, size = [], 0
        cur.append(cid)
        size += n
    if cur:
        slices.append(cur)
    return slices


def write_slice(t, ayah, sid, cell_ids, cs, by_id):
    k = key(ayah)
    text = ''.join(cell_text(cid, cs[cid], by_id) for cid in cell_ids).strip() + '\n'
    parts = [text[i:i + PART_CHARS] for i in range(0, len(text), PART_CHARS)]
    for n, p in enumerate(parts):
        tail = f'\n<<part {n} ends; continues in part {n + 1}>>' if n + 1 < len(parts) else '\n<<end of rows>>'
        (t / 'rows' / f'{k}.{sid}.p{n}.txt').write_text(f'<<{ayah} slice {sid}, part {n} of 0..{len(parts) - 1}>>\n{p}{tail}\n')
    return {'slice': sid, 'cells': cell_ids, 'rows': sum(len(cs[c]['rows']) for c in cell_ids),
            'sources': len({by_id[i]['src'] for c in cell_ids for i in cs[c]['rows']}), 'chars': len(text), 'parts': len(parts)}


def save_rows(t, ayah, rs, cs):
    k = key(ayah)
    (t / 'rows').mkdir(parents=True, exist_ok=True)
    dump(t / 'rows' / f'{k}.json', {r['id']: {x: r.get(x) for x in ('src', 'author', 'death', 'speaker', 'stance', 'claim',
                                                                    'mentions', 'words', 'type')} for r in rs})
    dump(t / 'rows' / f'{k}.cells.json', cs)


def spawn(t, run, spec, ayah, s, whole=False):
    model, effort = spec.split(':')
    tag = digest.tag_of(model, effort)
    k = key(ayah)
    with connect() as con:
        verse = con.execute("SELECT text FROM seg JOIN src ON src.id=seg.src WHERE src.kind='quran' AND s=? AND a=?",
                            tuple(map(int, ayah.split(':')))).fetchone()[0]
    fill = {'AGENT': f"/root/v7m_{run}_{tag}_{k}_{s['slice']}", 'MODEL': model, 'EFFORT': effort, 'RUN': run, 'TAG': tag,
            'AYAH': ayah, 'KEY': k, 'SLICE': s['slice'], 'LAST': str(s['parts'] - 1), 'ROWS': str(s['rows']),
            'NCELLS': str(len(s['cells'])), 'SOURCES': str(s['sources']), 'VERSE': verse}
    text = (BRIEF_WHOLE if whole else BRIEF).read_text()
    if whole:
        fill['TYPES'] = '\n'.join(f'  - `{k}`: {v}' for k, v in digest.TYPE_GUIDE.items())
    for x, v in fill.items():
        text = text.replace('{' + x + '}', v)
    f = t / 'spawn' / f"{tag}_{k}.{s['slice']}.md"
    if f.exists():
        raise SystemExit(f'{f} exists')
    f.parent.mkdir(exist_ok=True)
    f.write_text(text)
    (t / 'out' / tag).mkdir(parents=True, exist_ok=True)
    print(f'  spawn {f.relative_to(ROOT)}')


def build(a):
    d = run_dir(a.run)
    t = d / 'tier2'
    if (t / 'manifest.json').exists():
        raise SystemExit(f'{t} has a manifest; use `update` for new rows, or a new run')
    if bool(a.ayat) == bool(a.page):
        raise SystemExit('give either --ayat, or --page with --ayah')
    if a.page:
        import write  # late import: write imports this module
        a.ayat = write.page_verses(a.page, a.ayah)
        print(f'{a.ayah}: own ayah + {len(a.ayat) - 1} cited verses from {a.page}')
    tags = [digest.tag_of(*s.split(':')) for s in a.models]
    done = [x for x in a.ayat if all(list((V7 / 'work').glob(f'*/tier2/out/{g}/{key(x)}.jsonl')) for g in tags)]
    for x in done:
        print(f'SKIPPED {x}: tier 2 already exists for {", ".join(tags)} (use update in its run for new rows)')
    plan = []
    for ayah in [x for x in a.ayat if x not in done]:
        rs = tier1_rows(d, a.from_tags, ayah, mentions=False)
        if not rs:
            print(f'NOTE {ayah}: no tier-1 notes ({", ".join(a.from_tags)}); no tier 2')
            continue
        untagged = sum(1 for r in rs if r.get('type') not in TYPES)
        if untagged and not a.whole:
            print(f'WARNING {ayah}: {untagged} of {len(rs)} rows have no tags; they form the {UNTAGGED} cells (run retag first)')
        by_id = {r['id']: r for r in rs}
        if a.whole:
            order = sorted(rs, key=lambda r: (r['death'] if isinstance(r['death'], int) else 9999, r['src'], r['id']))
            cs = {WHOLE_CELL: {'word': 'whole verse', 'type': 'all', 'rows': [r['id'] for r in order]}}
            groups = [[WHOLE_CELL]]
        else:
            cs = cells(ayah, rs)
            groups = pack(cs, by_id, ayah)
        save_rows(t, ayah, rs, cs)
        slices = [write_slice(t, ayah, f's{n}', ids, cs, by_id) for n, ids in enumerate(groups, 1)]
        if a.whole and slices[0]['chars'] > SLICE_CHARS:
            print(f"NOTE {ayah}: {slices[0]['chars']:,} characters in one slice (--whole never splits a verse)")
        plan.append({'ayah': ayah, 'rows': len(rs), 'cells': len(cs), 'slices': slices})
        print(f"{ayah}: {len(rs)} rows, {len(cs)} cells, {len(slices)} slice(s), "
              f"{sum(s['chars'] for s in slices):,} characters")
    if not plan:
        raise SystemExit('nothing to build')
    for spec in a.models:
        for p in plan:
            for s in p['slices']:
                spawn(t, a.run, spec, p['ayah'], s, a.whole)
    dump(t / 'manifest.json', {'from': a.from_tags, 'models': a.models, 'whole': a.whole, 'ayat': plan})


def check_slice(t, tag, ayah, s, whole=False):
    """Problems in one slice output: unknown cell or id, a view mixing cells, a row of the slice in no view.
    whole: views carry no cell but their own words (in the verse) and type (in the list)."""
    k = key(ayah)
    cs = json.loads((t / 'rows' / f'{k}.cells.json').read_text())
    f = t / 'out' / tag / f"{k}.{s['slice']}.jsonl"
    if not f.exists():
        return [f'{f.name}: no output file'], []
    mine = {cid: set(cs[cid]['rows']) for cid in s['cells'] if cid in cs}
    problems, views, covered = [], [], set()
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            v = json.loads(line)
        except ValueError as e:
            problems.append(f'line {i}: not JSON ({e})')
            continue
        missing = [x for x in (('view', 'rows') if whole else ('cell', 'view', 'rows')) if not v.get(x)]
        if missing:
            problems.append(f'line {i}: missing {", ".join(missing)}')
            continue
        if whole:
            v['cell'] = WHOLE_CELL
            bad = digest.tag_problems({'words': v.get('words'), 'type': v.get('type'), 'verses': [ayah]})
            if bad:
                problems += [f'line {i}: {x}' for x in bad]
                continue
        if v['cell'] not in mine:
            problems.append(f"line {i}: cell {v['cell']} is not a cell of this slice")
            continue
        for r in v['rows']:
            if r not in mine[v['cell']]:
                problems.append(f"line {i}: row {r} is not in cell {v['cell']}")
            covered.add(r)
        views.append(v)
    for cid, ids in mine.items():
        for r in ids - covered:
            problems.append(f'row {r} (cell {cid}) is in no view')
    return problems, views


def assemble(t, tag, p, whole=False):
    """The verse's views: for each cell, the views of the latest slice that covers it, in cell order. whole: each view's
    own words and type give its cell."""
    k = key(p['ayah'])
    cs = json.loads((t / 'rows' / f'{k}.cells.json').read_text())
    if whole:
        _, views = check_slice(t, tag, p['ayah'], p['slices'][0], True)
        out = []
        for v in views:
            cid, word, typ = cell_of(v, p['ayah'])
            out.append({'cell': cid, 'word': word, 'type': typ, 'topic': f'{word} · {typ}', 'words': v['words'],
                        'view': v['view'], 'rows': v['rows'], 'note': v.get('note', '')})
        out.sort(key=lambda v: cell_order(v['cell']))
        (t / 'out' / tag / f'{k}.jsonl').write_text(''.join(json.dumps(v, ensure_ascii=False) + '\n' for v in out))
        known = json.loads((t / 'rows' / f'{k}.json').read_text())
        (t / 'out' / tag / f'{k}.md').write_text(compact(p['ayah'], out, known, tag))
        return out
    by_cell = {}
    for s in p['slices']:
        _, views = check_slice(t, tag, p['ayah'], s)
        for cid in s['cells']:
            by_cell[cid] = [v for v in views if v['cell'] == cid]
    out = []
    for cid in sorted(by_cell, key=cell_order):
        c = cs.get(cid, {})
        for v in by_cell[cid]:
            out.append({'cell': cid, 'word': c.get('word'), 'type': c.get('type'),
                        'topic': f"{c.get('word')} · {c.get('type')}", 'view': v['view'], 'rows': v['rows'],
                        'note': v.get('note', '')})
    (t / 'out' / tag / f'{k}.jsonl').write_text(''.join(json.dumps(v, ensure_ascii=False) + '\n' for v in out))
    views, known = out, json.loads((t / 'rows' / f'{k}.json').read_text())
    (t / 'out' / tag / f'{k}.md').write_text(compact(p['ayah'], [{**v} for v in views], known, tag))
    return out


def check(a):
    t = run_dir(a.run) / 'tier2'
    man = json.loads((t / 'manifest.json').read_text())
    tags = [a.model] if a.model else sorted(p.name for p in (t / 'out').iterdir())
    if a.ayah:  # the agent's own check
        p = next(x for x in man['ayat'] if x['ayah'] == a.ayah)
        s = next(x for x in p['slices'] if x['slice'] == (a.slice or 's1'))
        problems, _ = check_slice(t, tags[0], a.ayah, s, man.get('whole', False))
        print('OK' if not problems else '\n'.join(problems[:60]) + (f'\n... {len(problems) - 60} more' if len(problems) > 60 else ''))
        return
    for tag in tags:
        for p in man['ayat']:
            bad = 0
            for s in p['slices']:
                problems, _ = check_slice(t, tag, p['ayah'], s, man.get('whole', False))
                bad += bool(problems)
                for x in problems:
                    print(f"WARNING {tag} {p['ayah']} {s['slice']}: {x}")
            if bad:
                print(f"{tag} {p['ayah']}: {bad} slice(s) with problems; not assembled")
                continue
            views = assemble(t, tag, p, man.get('whole', False))
            print(f"{tag} {p['ayah']}: {len(views)} views from {p['rows']} rows in {p['cells']} cells, assembled")


def update(a):
    """Cells that gained (or lost) rows since tier 2 ran get a new slice; other cells keep their views."""
    d = run_dir(a.run)
    t = d / 'tier2'
    man = json.loads((t / 'manifest.json').read_text())
    if man.get('whole'):
        raise SystemExit('update works on cell runs only; for a --whole run, build a new run')
    tag = a.model
    spec = next(s for s in man['models'] if digest.tag_of(*s.split(':')) == tag)
    changed = False
    for p in man['ayat']:
        old = json.loads((t / 'rows' / f"{key(p['ayah'])}.cells.json").read_text())
        rs = tier1_rows(d, man['from'], p['ayah'], quiet=True, mentions=False)
        by_id = {r['id']: r for r in rs}
        cs = cells(p['ayah'], rs)
        stale = [cid for cid, c in cs.items() if set(c['rows']) != set(old.get(cid, {}).get('rows', []))]
        gone = [cid for cid in old if cid not in cs]
        if not stale and not gone:
            print(f"{p['ayah']}: up to date")
            continue
        changed = True
        save_rows(t, p['ayah'], rs, cs)
        n0 = sum(1 for s in p['slices'] if s['slice'].startswith('u'))
        for n, ids in enumerate(pack({c: cs[c] for c in stale}, by_id, p['ayah']), n0 + 1):
            s = write_slice(t, p['ayah'], f'u{n}', ids, cs, by_id)
            p['slices'].append(s)
            spawn(t, a.run, spec, p['ayah'], s)
        for cid in gone:  # a cell that lost all its rows (retagged elsewhere): its old views are dropped, printed
            print(f"NOTE {p['ayah']}: cell {cid} has no rows any more; its views are dropped at assembly")
            p['slices'].append({'slice': f'gone-{cid}', 'cells': [cid], 'rows': 0, 'sources': 0, 'chars': 0, 'parts': 0,
                                'empty': True})
        p['rows'], p['cells'] = len(rs), len(cs)
        print(f"{p['ayah']}: {len(stale)} cell(s) rebuilt, {len(gone)} cell(s) gone")
    if changed:
        dump(t / 'manifest.json', man)


def view_id(ayah, n):
    return f'{ayah}/v{n:03d}'


def load(ayah, tag):
    """Tier 2 of one ayah from any run: (views with 'vid', rows by id). Exactly one run may hold it."""
    k = key(ayah)
    found = sorted((V7 / 'work').glob(f'*/tier2/out/{tag}/{k}.jsonl'))
    if len(found) != 1:
        raise SystemExit(f'{ayah}: {len(found)} tier-2 files for {tag} ({[str(f) for f in found]}); expected exactly one')
    rows_file = found[0].parents[2] / 'rows' / f'{k}.json'
    views = [json.loads(x) for x in found[0].read_text().splitlines() if x.strip()]
    for n, v in enumerate(views, 1):
        v['vid'] = view_id(ayah, n)
    return views, json.loads(rows_file.read_text())


def compact(ayah, views, known, tag=''):
    """Compact view list grouped by cell (older outputs: by topic): view ids, source ids, the speaker only when not
    the source's author, stance marks (+ prefers, - rejects). Claims and anchors stay in tier 1 behind the row ids."""
    out, topic = [f'# {ayah}: {len(views)} views from {len(known)} rows' + (f' ({tag})' if tag else '')], None
    for n, v in enumerate(views, 1):
        if v['topic'] != topic:
            topic = v['topic']
            out.append(f'\n## {topic}')
        holders = defaultdict(set)
        for r in v['rows']:
            k = known.get(r)
            if k:
                holders['' if k['speaker'] == 'author' else k['speaker']].add(
                    k['src'] + {'prefers': '+', 'rejects': '-'}.get(k['stance'], ''))
        who = '; '.join((f'{s}: ' if s else '') + ','.join(sorted(x)) for s, x in holders.items())
        out.append(f"- {view_id(ayah, n)} {v['view']}" + (f" ({v['note']})" if v.get('note') else '') + f' [{who}]')
    return '\n'.join(out) + '\n'


def report(a):
    t = run_dir(a.run) / 'tier2'
    man = json.loads((t / 'manifest.json').read_text())
    for tag in sorted(p.name for p in (t / 'out').iterdir()):
        total = 0.0
        for p in man['ayat']:
            f = t / 'out' / tag / f"{key(p['ayah'])}.jsonl"
            n = len(f.read_text().splitlines()) if f.exists() else 0
            for s in p['slices']:
                if s.get('empty'):
                    continue
                x = digest.usage(t / 'runs', f"/root/v7m_{a.run}_{tag}_{key(p['ayah'])}_{s['slice']}")
                if x is None:
                    print(f"WARNING {tag} {p['ayah']} {s['slice']}: no run record")
                    continue
                total += x['usd']
                print(f"{tag} {p['ayah']} {s['slice']}: ${x['usd']:.3f}, {x['requests']} requests, peak {x['peak']} tokens, "
                      f"{s['rows']} rows in {len(s['cells'])} cells" + ('' if x['completed'] else ' — DID NOT COMPLETE'))
            print(f"{tag} {p['ayah']}: {p['rows']} rows -> {n} views")
        print(f'{tag}: ${total:.2f} total')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('build'); p.add_argument('run'); p.add_argument('--from', dest='from_tags', nargs='+', required=True,
                                                                          help='tier-1 model tags, e.g. luna-max')
    p.add_argument('--ayat', nargs='+'); p.add_argument('--models', nargs='+', required=True)
    p.add_argument('--page', help="a frozen page: its own ayah (--ayah) and every verse it cites"); p.add_argument('--ayah')
    p.add_argument('--whole', action='store_true', help='one slice per verse; the agent labels each view (no row tags needed)')
    p = sub.add_parser('check'); p.add_argument('run'); p.add_argument('--model'); p.add_argument('--ayah'); p.add_argument('--slice')
    p = sub.add_parser('update'); p.add_argument('run'); p.add_argument('--model', required=True)
    p = sub.add_parser('report'); p.add_argument('run')
    a = parser.parse_args()
    {'build': build, 'check': check, 'update': update, 'report': report}[a.cmd](a)


if __name__ == '__main__':
    main()
