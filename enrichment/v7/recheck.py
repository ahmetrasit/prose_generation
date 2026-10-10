#!/usr/bin/env python3
"""Recheck of tier-1 digests for missed verses (user, 2026-10-10). A digest serves every verse its notes name
(merge.tier1_rows). A digested segment may still say something about a verse that none of its notes names: the
spot check (enrichment/v9/work/spot-linked-20261010) found 1 such point in 40 candidate pairs. This run finds every
candidate pair in everything digested so far and asks Luna, segment by segment, for the missed points only.

A candidate pair (segment, verse): the segment was digested, none of its notes names the verse (in `verses` or
`mentions`), and the segment contains the verse's own words (a 2- or 3-word window that occurs in no other verse; a
2-word window found in more than QUOTE_MAX_HITS digested segments counts only through its 3-word windows) or, for a
verse inside the segment's index range, a verse marker (markers(): "[البلد: 2]", "(2)", "(vv. 9-12)", "﴿٢﴾",
"(90:2)"; not footnotes "[1]", other sūras' S:A, page, volume or date numbers, or numbers inside words). Pairs checked
by an earlier recheck run are left out.

The new notes are supplements: merge.tier1_rows reads them beside the digests, with ids <loc>/x<N>-<RUN>, so no
digest is replaced and nothing is digested twice. Runs live in enrichment/v7/recheck/<RUN>/ (not in work/, whose
outputs are read as digests). Same layout as a tier-1 run: chunks/, spawn/, runs/, out/<TAG>/cNN.jsonl.

  recheck.py plan [SCOPE] [--tier1 luna-max]                 counts only: candidate pairs, segments, characters
  recheck.py build RUN [SCOPE] [--tier1 luna-max] [--models gpt-6-luna:max] [--chunk-chars 20000]

SCOPE (default: every candidate pair): --verses V … or --verses-file F (only these verses are checked), --mapped
(only verses with a v9 map, plus any --verses), --index-only (only verses inside the segment's own index range).
Build the run on the machine that runs it (the chunks hold the segment texts; nothing to commit but the outputs).
  recheck.py check RUN [--model TAG] [--chunk N]             the agent runs it with --chunk until OK
  recheck.py report RUN                                      costs, segments, new notes
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import digest
import merge
from digest import (DEFAULT_CHUNK_CHARS, OVERLAY, PART_CHARS, QUOTE_MAX_HITS, ROOT, TYPE_GUIDE, V7, connect, contains,
                    dump, normalize_map, rows, source_line, tag_of, tag_problems)

HOME = V7 / 'recheck'
BRIEF = V7 / 'briefs/recheck.md'


def run_dir(run):
    return HOME / run


def checked_before():
    """(loc, verse) pairs a finished recheck agent has already answered, from every recheck run."""
    out = set()
    for man in HOME.glob('*/manifest.json'):
        m = json.loads(man.read_text())
        for tag in m.get('tags', []):
            for c in m['chunks']:
                f = man.parent / 'out' / tag / f"c{c['chunk']:02d}.jsonl"
                if not f.exists() or digest.unfinished(f):
                    continue
                done = set()
                for line in f.read_text().splitlines():
                    try:
                        done.add(json.loads(line)['loc'])
                    except (ValueError, KeyError, TypeError):
                        pass
                out |= {(loc, v) for loc in c['locs'] if loc in done for v in c['check'][loc]}
    return out


def scope_of(a):
    """The verses to check (None = all) and whether only index-range verses count, from the command line."""
    vs = set(a.verses or [])
    if a.verses_file:
        vs |= set(Path(a.verses_file).read_text().split())
    if a.mapped:
        vs |= {f.stem.replace('-', ':') for f in (ROOT / 'enrichment/v9/work').glob('*/map/out/sol-high/*.jsonl')
               if '.' not in f.stem}
    bad = [v for v in vs if not re.fullmatch(r'\d+:\d+', v)]
    if bad:
        raise SystemExit(f'not S:A verses: {", ".join(sorted(bad)[:10])}')
    if (a.verses or a.verses_file or a.mapped) and not vs:
        raise SystemExit('the scope options give no verses (no maps found, or an empty verses file); nothing built')
    return (vs or None), a.index_only


_ARABIC_DIGITS = str.maketrans('٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹', '01234567890123456789')
_MARK = re.compile(r'([\[(﴿])([^\[\]()﴿﴾\n]{0,30})[\])﴾]')
_NOT_VERSE = re.compile(r'(?:^|[^\w])(?:p|pp|vol|no|n|s|d|ص|ج|رقم|ت)\.?\s*\d|\d\s*(?:AH|H|CE|AD|هـ)\b|\d\s*/\s*\d', re.I)
_ONLY_NUMBERS = re.compile(r'^[^\d]{0,20}?[\d\s,،\-–]+$')   # an optional label, then numbers, ranges, separators


def markers(text, surah):
    """Ayah numbers of this surah that the text marks: "[البلد: 2]", "(2)", "(vv. 9-12)", "﴿2﴾", "(90:2)". A bare number in
    square brackets ("[1]", "[^16]") is a footnote, a "S:A" of another surah is not this surah's ayah, and page or
    volume numbers ("(p. 5)", "(ج 2)") are not ayat."""
    out = set()
    for m in _MARK.finditer((text or '').translate(_ARABIC_DIGITS)):
        open_, c = m.groups()
        c = re.sub(r'(\d)\s*:\s*(\d)', r'\1:\2', c)
        if re.search(r'\d:\d', c):
            out |= {int(v.split(':')[1]) for v in digest.verse_list([c]) if int(v.split(':')[0]) == surah}
            continue
        if _NOT_VERSE.search(c) or c.lstrip().startswith('^') or not _ONLY_NUMBERS.match(c.strip()):
            continue                         # "(3 men)", "(d. 310 AH)", "(p. 5)": not a verse marker
        if open_ == '[' and not re.search(r'[^\W\d_]', c):
            continue                         # [1], [12]: footnote numbers
        for x, y in re.findall(r'(?<![\d.])(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?(?![\d.])', c):
            a, b = int(x), int(y or x)
            if 1 <= a <= b and b - a <= 50:
                out.update(range(a, b + 1))
    return out


def candidates(tier1, only=None, index_only=False):
    """{loc: {'verses': [...], 'src', 'kind', 'head', 'text', 'index'}} for every candidate pair, and counts. only: a
    set of verses to check (None = all); index_only: only verses inside the segment's own index range."""
    segs = defaultdict(list)                 # loc -> its notes (digests and earlier supplements)
    for _, x, _, _ in merge.tier1_segments(tier1):
        segs[x['loc']] += x.get('rows') or []
    for _, _, x in merge.supplements(tier1):
        segs[x['loc']] += x.get('rows') or []
    with connect() as con:
        quran = {f'{s}:{a}': t for s, a, t in con.execute(
            "SELECT s, a, text FROM seg JOIN src ON src.id=seg.src WHERE src.kind='quran' AND a IS NOT NULL")}
        meta, locs = {}, list(segs)
        for i in range(0, len(locs), 900):
            part = locs[i:i + 900]
            for r in con.execute('SELECT seg.id, seg.seg, seg.src, src.kind, seg.s, seg.a, coalesce(seg.a_end, seg.a), '
                                 f"seg.head, seg.text FROM seg JOIN src ON src.id=seg.src WHERE seg.seg IN "
                                 f"({','.join('?' * len(part))})", part):
                meta[r[1]] = r
    missing = [loc for loc in segs if loc not in meta]
    if missing:
        print(f'NOTE {len(missing)} digested locator(s) are not in the corpus index (renamed or removed); not checked: '
              + ', '.join(missing[:10]) + (' …' if len(missing) > 10 else ''))
    extra = defaultdict(set)
    if OVERLAY.exists():
        for r in rows(OVERLAY):
            extra[r['seg_id']].update(f"{r['s']}:{x}" for x in range(r['indexed_end'] + 1, r['a_end'] + 1))
    words = {v: normalize_map(t)[0].split() for v, t in quran.items()}
    owner = defaultdict(set)
    for v, w in words.items():
        for n in (2, 3):
            for i in range(len(w) - n + 1):
                owner[' '.join(w[i:i + n])].add(v)
    unique = {g: next(iter(vs)) for g, vs in owner.items() if len(vs) == 1}
    found = {}
    for loc in meta:
        w = normalize_map(meta[loc][8] or '')[0].split()
        hits = {}
        for n in (2, 3):
            for i in range(len(w) - n + 1):
                g = ' '.join(w[i:i + n])
                if g in unique:
                    hits.setdefault(g, unique[g])
        found[loc] = hits
    seen = defaultdict(int)                  # 2-word window -> digested segments it occurs in
    for hits in found.values():
        for g in hits:
            if ' ' in g and g.count(' ') == 1:
                seen[g] += 1
    common = {g for g, k in seen.items() if k > QUOTE_MAX_HITS}
    done = checked_before()
    out, pairs, by_marker, skipped_done, lost_common, no_verse = {}, 0, 0, 0, 0, []
    for loc, (sid, _, src, kind, s, a, ae, head, text) in meta.items():
        named = set()
        for r in segs[loc]:
            named.update(digest.verse_list(r.get('verses')))
            named.update(digest.verse_list(r.get('mentions')))
        vs, index, marked, via_common = set(), set(), set(), set()
        for g, v in found[loc].items():
            if g in common:
                via_common.add(v)
                continue
            vs.add(v)
        if s is not None and a is not None:
            index = {f'{s}:{x}' for x in range(a, ae + 1)} | extra[sid]
            marks = {f'{s}:{n}' for n in markers(text, s)}
            for v in (index & marks) - vs:
                vs.add(v)
                marked.add(v)
        if index_only:
            vs &= index
        if only is not None:
            vs &= only
        vs -= named
        ghost = {v for v in vs if v not in quran}   # an index range or overlay row past a sūra's last ayah
        if ghost:
            vs -= ghost
            no_verse.extend(f'{loc} {v}' for v in sorted(ghost))
        lost = via_common - vs - named - {v for v in via_common if (loc, v) in done}
        if index_only:
            lost &= index
        if only is not None:
            lost &= only
        lost_common += len(lost)
        again = {v for v in vs if (loc, v) in done}
        skipped_done += len(again)
        vs = sorted(vs - again)
        by_marker += len(marked & set(vs))
        if vs:
            out[loc] = {'verses': vs, 'marked': sorted(marked & set(vs)), 'src': src, 'kind': kind, 'head': head or '',
                        'text': text,
                        'index': f'{s}:{a}' + (f'-{ae}' if ae != a else '') if s is not None and a is not None else ''}
            pairs += len(vs)
    if no_verse:
        print(f'NOTE {len(no_verse)} marker pair(s) name no verse of the Qur\'an text (an index range past the sūra\'s '
              f'end); not checked: ' + ', '.join(no_verse[:8]) + (' …' if len(no_verse) > 8 else ''))
    reached = {v for x in out.values() for v in x['verses']}
    counts = {'digested segments': len(segs), 'candidate pairs': pairs, 'segments to check': len(out),
              'characters': sum(len(x['text'] or '') for x in out.values()), 'pairs by marker only': by_marker,
              'pairs left out, checked by an earlier recheck': skipped_done,
              'too-common 2-word windows (a pair reached only through one is not checked)': len(common),
              'pairs not checked: reached only through a too-common window': lost_common}
    if only is not None:
        counts['scope verses'] = len(only)
        counts['scope verses with at least one candidate'] = len(reached & only)
    return out, counts, quran


def segment_input(loc, x, notes):
    check = ', '.join(v + (' (number only)' if v in x.get('marked', []) else '') for v in x['verses'])
    lines = [f"=== SEGMENT {loc} | source {x['src']} | indexed {x['index'] or 'none'} | CHECK {check}"
             f" | {x['head']} ===", (x['text'] or '').strip(), '--- notes already taken on this segment ---']
    lines += [f"[{n}] verses {', '.join(map(str, r.get('verses') or [])) or '-'} | {r.get('speaker')} | "
              f"{r.get('stance')} | {r.get('claim')}" for n, r in enumerate(notes, 1) if isinstance(r, dict)] or ['(none)']
    return '\n'.join(lines) + f'\n=== END SEGMENT {loc} ===\n\n'


LUNA_USD_PER_M = 1.32         # API-equivalent USD per million chunk characters (tier-1 s1_87_114: $13.60 / 10.29M)
NOTES_FACTOR = 1.6            # chunk characters / segment characters, with the notes printed beside each segment


def cmd_plan(a):
    _, counts, _ = candidates(a.tier1, *scope_of(a))
    for k, v in counts.items():
        print(f'{k}: {v:,}' if isinstance(v, int) else f'{k}: {v}')
    est = counts['characters'] * NOTES_FACTOR
    print(f"estimate: about {est / 1e6:.0f}M chunk characters, {est / DEFAULT_CHUNK_CHARS:,.0f} chunks (Luna agents), "
          f"about ${est / 1e6 * LUNA_USD_PER_M:,.0f} API-equivalent at the tier-1 rate (build prints the exact chunks)")


def cmd_build(a):
    d = run_dir(a.run)
    if d.exists():
        raise SystemExit(f'{d} exists; choose a new run name')
    only, index_only = scope_of(a)
    cand, counts, quran = candidates(a.tier1, only, index_only)
    counts['scope'] = {'verses': len(only) if only else 'all', 'index_only': index_only}
    for k, v in counts.items():
        print(f'{k}: {v:,}' if isinstance(v, int) else f'{k}: {v}')
    if not cand:
        raise SystemExit('no candidate pairs')
    notes = defaultdict(list)                # digest notes, then notes of earlier recheck runs
    for _, x, _, _ in merge.tier1_segments(a.tier1):
        if x['loc'] in cand:
            notes[x['loc']] += x.get('rows') or []
    for _, _, x in merge.supplements(a.tier1):
        if x['loc'] in cand:
            notes[x['loc']] += [r for r in x['rows'] if isinstance(r, dict)]
    with connect() as con:
        smeta = {i: (k, json.loads(m or '{}')) for i, k, m in con.execute('SELECT id, kind, meta FROM src')}
    by_src = defaultdict(list)
    for loc in sorted(cand):
        by_src[cand[loc]['src']].append(loc)
    chunks, cur, size = [], [], 0          # whole segments, packed in source order; a larger segment stands alone
    for sr in sorted(by_src, key=lambda s: (smeta[s][0], s)):
        for loc in by_src[sr]:
            n = len(segment_input(loc, cand[loc], notes[loc]))
            if n > a.chunk_chars:
                print(f'NOTE {loc}: {n:,} characters with its notes, over --chunk-chars; it forms a chunk alone')
            if cur and size + n > a.chunk_chars:
                chunks.append(cur)
                cur, size = [], 0
            cur.append(loc)
            size += n
    if cur:
        chunks.append(cur)
    (d / 'chunks').mkdir(parents=True)
    plan = []
    for n, locs in enumerate(chunks, 1):
        text = ''.join(segment_input(loc, cand[loc], notes[loc]) for loc in locs)
        parts = [text[i:i + PART_CHARS] for i in range(0, len(text), PART_CHARS)]
        for k, p in enumerate(parts):
            tail = f'\n<<part {k} ends; continues in part {k + 1}>>' if k + 1 < len(parts) else '\n<<end of chunk>>'
            (d / 'chunks' / f'c{n:02d}.p{k}.txt').write_text(f'<<chunk {n} part {k} of 0..{len(parts) - 1}>>\n{p}{tail}\n')
        srcs = list(dict.fromkeys(cand[loc]['src'] for loc in locs))
        plan.append({'chunk': n, 'sources': srcs, 'source_lines': [source_line(s, smeta[s][1], smeta[s][0]) for s in srcs],
                     'locs': locs, 'check': {loc: cand[loc]['verses'] for loc in locs},
                     'verses': sorted({v for loc in locs for v in cand[loc]['verses']},
                                      key=lambda v: tuple(map(int, v.split(':')))),
                     'chars': len(text), 'parts': len(parts)})
    brief, spawns, tags = BRIEF.read_text(), [], []
    for spec in a.models:
        model, effort = spec.split(':')
        tag = tag_of(model, effort)
        tags.append(tag)
        for c in plan:
            fill = {'AGENT': f"/root/v7d_{a.run}_{tag}_c{c['chunk']:02d}", 'MODEL': model, 'EFFORT': effort,
                    'RUN': a.run, 'TAG': tag, 'N': str(c['chunk']), 'NN': f"{c['chunk']:02d}", 'LAST': str(c['parts'] - 1),
                    'SEGMENTS': str(len(c['locs'])), 'SOURCES': '\n'.join(f'- {x}' for x in c['source_lines']),
                    'AYAT': '\n'.join(f'- {v}: {quran[v]}' for v in c['verses']),
                    'TYPES': '\n'.join(f'- `{k}`: {v}' for k, v in TYPE_GUIDE.items())}
            text = brief
            for k, v in fill.items():
                text = text.replace('{' + k + '}', v)
            f = d / 'spawn' / f"{tag}_c{c['chunk']:02d}.md"
            f.parent.mkdir(exist_ok=True)
            f.write_text(text)
            spawns.append(str(f.relative_to(ROOT)))
        (d / 'out' / tag).mkdir(parents=True)
    dump(d / 'manifest.json', {'run': a.run, 'tier1': a.tier1, 'models': a.models, 'tags': tags,
                               'chunk_chars': a.chunk_chars, 'counts': counts, 'chunks': plan, 'spawn': spawns})
    print(f"{len(plan)} chunks, {sum(c['chars'] for c in plan):,} characters, {len(spawns)} spawn files; "
          f"written {d.relative_to(ROOT)}")


def check_chunk(d, tag, c):
    f = d / 'out' / tag / f"c{c['chunk']:02d}.jsonl"
    if not f.exists():
        return [f'{f.name}: no output file'], 0
    with connect() as con:
        hit = {loc: con.execute('SELECT text FROM seg WHERE seg=?', (loc,)).fetchone() for loc in c['locs']}
    gone = [loc for loc, h in hit.items() if h is None]
    if gone:
        return [f'{loc}: no longer in the corpus index (rebuilt after this run was built?)' for loc in gone], 0
    text = {loc: h[0] or '' for loc, h in hit.items()}
    problems, seen, n_rows = [], [], 0
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            x = json.loads(line)
        except ValueError as e:
            problems.append(f'line {i}: not JSON ({e})')
            continue
        loc = x.get('loc') if isinstance(x, dict) else None
        if not isinstance(loc, str) or loc not in text:
            problems.append(f'line {i}: locator {loc!r} is not in this chunk')
            continue
        seen.append(loc)
        rs = x.get('rows')
        if not isinstance(rs, list):
            problems.append(f'{loc}: "rows" must be a list')
            continue
        if not rs and not (x.get('none') or '').strip():
            problems.append(f'{loc}: no rows and no "none" reason')
        check = set(c['check'][loc])          # S:A strings
        for j, r in enumerate(rs, 1):
            n_rows += 1
            if not isinstance(r, dict):
                problems.append(f'{loc} row {j}: not an object')
                continue
            missing = [k for k in ('verses', 'words', 'type', 'speaker', 'stance', 'claim', 'anchor') if not r.get(k)]
            if missing:
                problems.append(f'{loc} row {j}: missing {", ".join(missing)}')
            rej = []
            vs = digest.verse_list(r.get('verses'), rej)
            digest.verse_list(r.get('mentions') or [], rej)
            if rej:
                problems.append(f'{loc} row {j}: not verses (write S:A): {", ".join(map(str, rej))[:120]}')
            if not check & set(vs):
                problems.append(f'{loc} row {j}: "verses" must include one of the verses to check here: '
                                f'{", ".join(sorted(check))}')
            if r.get('stance') and r['stance'] not in ('holds', 'prefers', 'reports', 'rejects'):
                problems.append(f'{loc} row {j}: stance must be holds, prefers, reports or rejects')
            if r.get('anchor') and not contains(text[loc], r['anchor']):
                problems.append(f'{loc} row {j}: anchor not found verbatim in the segment: {r["anchor"][:80]}')
            if r.get('words') and r.get('type'):
                problems += [f'{loc} row {j}: {p}' for p in tag_problems({**r, 'verses': vs})]
    for loc in c['locs']:
        if loc not in seen:
            problems.append(f'{loc}: segment has no line')
    for loc in {x for x in seen if seen.count(x) > 1}:
        problems.append(f'{loc}: more than one line')
    return problems, n_rows


def cmd_check(a):
    d = run_dir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    tags = [a.model] if a.model else man['tags']
    bad = 0
    for tag in tags:
        for c in man['chunks']:
            if a.chunk and c['chunk'] != a.chunk:
                continue
            problems, n = check_chunk(d, tag, c)
            for p in problems:
                print(f"{tag} c{c['chunk']:02d}: {p}")
            bad += len(problems)
            if a.chunk:
                print('OK' if not problems else f'{len(problems)} problem(s)', f'({n} new notes)')
    if not a.chunk:
        print('OK' if not bad else f'{bad} problem(s)')


def cmd_report(a):
    d = run_dir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    for tag in man['tags']:
        usd = done = new = segs_with = 0
        for c in man['chunks']:
            x = digest.usage(d / 'runs', f"/root/v7d_{a.run}_{tag}_c{c['chunk']:02d}")
            if x is None:
                print(f"WARNING {tag} c{c['chunk']:02d}: no run.json")
                continue
            done += 1
            usd += x['usd']
            if not x['completed']:
                print(f"WARNING {tag} c{c['chunk']:02d}: did not complete ({x['via']}); its notes are not counted")
                continue
            f = d / 'out' / tag / f"c{c['chunk']:02d}.jsonl"
            for line in (f.read_text().splitlines() if f.exists() else []):
                try:
                    k = len(json.loads(line).get('rows') or [])
                except (ValueError, AttributeError):
                    print(f"WARNING {tag} c{c['chunk']:02d}: unreadable line (run recheck.py check)")
                    continue
                new += k
                segs_with += k > 0
        pairs = sum(len(v) for c in man['chunks'] for v in c['check'].values())
        print(f"{tag}: {done}/{len(man['chunks'])} runs, ${usd:.2f} API-equivalent, {pairs} pairs checked in "
              f"{sum(len(c['locs']) for c in man['chunks'])} segments, {new} new notes in {segs_with} segments")


def scope(p):
    p.add_argument('--verses', nargs='+', help='check only these verses (S:A)')
    p.add_argument('--verses-file', help='check only the verses listed in this file (S:A, whitespace-separated)')
    p.add_argument('--mapped', action='store_true', help='check only verses that have a v9 map (plus --verses)')
    p.add_argument('--index-only', action='store_true', help="only verses inside the segment's own index range")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('plan')
    p.add_argument('--tier1', nargs='+', default=['luna-max'])
    scope(p)
    p = sub.add_parser('build')
    p.add_argument('run')
    p.add_argument('--tier1', nargs='+', default=['luna-max'])
    scope(p)
    p.add_argument('--models', nargs='+', default=['gpt-6-luna:max'])
    p.add_argument('--chunk-chars', type=int, default=DEFAULT_CHUNK_CHARS)
    p = sub.add_parser('check')
    p.add_argument('run')
    p.add_argument('--model')
    p.add_argument('--chunk', type=int)
    p = sub.add_parser('report')
    p.add_argument('run')
    a = ap.parse_args()
    globals()[f'cmd_{a.cmd}'](a)


if __name__ == '__main__':
    main()
