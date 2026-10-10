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
  recheck.py build RUN [SCOPE] [--tier1 luna-max] [--models gpt-6-luna:max] [--chunk-chars 20000] [--allow-overlap]
            refuses while chunks of earlier recheck runs have no valid answer (their pairs would be checked twice)

SCOPE (default: every candidate pair): --verses V … or --verses-file F (only these verses are checked), --mapped
(only verses with a v9 map, plus any --verses), --index-only (only verses inside the segment's own index range).
Build the run on the machine that runs it (the chunks hold the segment texts; nothing to commit but the outputs).
  recheck.py check RUN [--model TAG] [--chunk N]             the agent runs it with --chunk until OK
  recheck.py report RUN                                      costs, segments, new notes
"""
import argparse
import contextlib
import hashlib
import io
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import digest
import merge
from digest import (DEFAULT_CHUNK_CHARS, PART_CHARS, QUOTE_MAX_HITS, ROOT, TYPE_GUIDE, V7, connect, contains,
                    dump, normalize_map, source_line, tag_of, tag_problems)

HOME = V7 / 'recheck'
BRIEF = V7 / 'briefs/recheck.md'
sys.path.insert(0, str(ROOT / 'enrichment/v2/fetch'))
from openiti_quran import SURAH_NAMES  # names only; no source file is opened


def run_dir(run):
    return HOME / run


def checked_before(tags=None):
    """(loc, verse) pairs a finished recheck agent has already answered, from every recheck run."""
    out = set()
    for man in HOME.glob('*/manifest.json'):
        m = json.loads(man.read_text())
        for tag in m.get('tags', []):
            if tags is not None and tag not in tags:
                continue
            for c in m['chunks']:
                f = man.parent / 'out' / tag / f"c{c['chunk']:02d}.jsonl"
                if not f.exists():
                    continue
                done = digest.valid_output_locs(f)     # finished, valid, source unchanged
                out |= {(loc, v) for loc in c['locs'] if loc in done for v in c['check'][loc]}
    return out


def unanswered(tags):
    """Chunks of earlier recheck runs (for these model tags) whose output is missing or not valid for every segment."""
    out = []
    for man in sorted(HOME.glob('*/manifest.json')):
        try:
            m = json.loads(man.read_text())
            plan = [(tag, c['chunk'], set(c['locs'])) for tag in m.get('tags', []) if tag in tags for c in m['chunks']]
        except (OSError, ValueError, KeyError, TypeError) as e:
            out.append(f'{man.parent.name} (manifest unreadable: {e})')
            continue
        for tag, n, locs in plan:
            f = man.parent / 'out' / tag / f'c{n:02d}.jsonl'
            with contextlib.redirect_stdout(io.StringIO()):     # per-line warnings; the chunk itself is listed
                valid = digest.valid_output_locs(f) if f.exists() else set()
            if valid != locs:
                out.append(f'{man.parent.name}/{tag}/c{n:02d}')
    return out


def scope_of(a):
    """The verses to check (None = all) and whether only index-range verses count, from the command line."""
    vs = set(a.verses or [])
    if a.verses_file:
        vs |= set(Path(a.verses_file).read_text().split())
    if a.mapped:
        vs |= {f.stem.replace('-', ':') for f in (ROOT / 'enrichment/v9/work').glob('*/map/out/sol-high/*.jsonl')
               if '.' not in f.stem}
    bad = [v for v in vs if not re.fullmatch(r'\d+:\d+', v) or v not in digest.quran()]
    if bad:
        raise SystemExit(f'not verses of the Quran index: {", ".join(sorted(bad))}')
    if (a.verses or a.verses_file or a.mapped) and not vs:
        raise SystemExit('the scope options give no verses (no maps found, or an empty verses file); nothing built')
    return (vs or None), a.index_only


_ARABIC_DIGITS = str.maketrans('٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹', '01234567890123456789')
_MARK = re.compile(r'([\[(﴿])([^\[\]()﴿﴾\n]{0,30})[\])﴾]')
_NOT_VERSE = re.compile(r'(?:^|[^\w])(?:p|pp|vol|no|n|s|d|ص|ج|رقم|ت)\.?\s*\d|\d\s*(?:AH|H|CE|AD|هـ)\b|\d\s*/\s*\d', re.I)
_ONLY_NUMBERS = re.compile(r'^[^\d]{0,20}?[\d\s,،\-–]+$')   # an optional label, then numbers, ranges, separators


VERSE_WORDS = {'v', 'vv', 'verse', 'verses', 'ayah', 'ayat', 'āyah', 'āyāt', 'ayet', 'âyet', 'آية', 'آيات', 'الآية',
               'الآيات', 'الآيتان', 'الآيتين'}


LATIN_LEADS = {'see', 'in', 'cf', 'compare', 'also', 'and', 'sura', 'surah', 'sure', 'sūra', 'sūrah', 'q', 'vgl', 'siehe',
               'bkz', 'ayrıca', 'bakınız'}   # capitalised words that are not surah names


def surahs_named(label):
    """Surah numbers whose name the label is ("البلد", "سورة البلد"), or an empty set."""
    normalized = normalize_map(re.sub(r'^سورة\s+', '', label.strip(' ،,:')))[0]
    return {s for s, names in SURAH_NAMES.items()
            if normalized and normalized in {normalize_map(name)[0] for name in names.split('|')}}


def label_fits(label, surah):
    """Whether the words before a marker's numbers allow it to be this surah's ayah: a name of this surah ("البلد"),
    a verse word ("vv.", "الآية"), or text ending in a verse word that names no other surah ("سورة البلد الآية",
    "i.e., verses", "vgl. V."). Any other label ("(c. 1)", "(Buhâri, Tefsir 1, 1)") is not a verse marker."""
    named = surahs_named(label)
    if named:
        return surah in named
    words = label.split()
    last = words[-1].lower().strip('.,،:') if words else ''
    if last not in VERSE_WORDS and not (last[:1] in 'وف' and last[1:] in VERSE_WORDS):   # "والآية", "فالآية"
        return False
    rest = words[:-1]
    named = surahs_named(' '.join(rest)) if rest else set()
    for i in range(len(rest)):                   # a surah named anywhere before the verse word ("see البلد, verse")
        for j in (i + 1, i + 2):
            if j <= len(rest):
                named |= surahs_named(' '.join(rest[i:j]))
    if named:
        return surah in named
    # Latin labels: the names table is Arabic, so a capitalised word that is not an abbreviation ("Fatiha" in
    # "see Fatiha, verse 3") may be a surah name: not counted as this surah's marker
    return not any(re.fullmatch(r'[A-ZÀ-Þ][^\W\d_]+', w.strip(',;:')) and w.strip(',;:').lower() not in LATIN_LEADS
                   for w in rest)


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
        label = re.split(r'\d', c, maxsplit=1)[0].strip().rstrip(':').strip()
        if label and not label_fits(label, surah):
            continue
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
        meta, citations, locs = {}, defaultdict(set), list(segs)
        for i in range(0, len(locs), 900):
            part = locs[i:i + 900]
            for r in con.execute('SELECT seg.id, seg.seg, seg.src, src.kind, seg.s, seg.a, coalesce(seg.a_end, seg.a), '
                                 f"seg.head, seg.text, seg.extra FROM seg JOIN src ON src.id=seg.src WHERE seg.seg IN "
                                 f"({','.join('?' * len(part))})", part):
                meta[r[1]] = r
            for s, start, end, loc in con.execute(
                    'SELECT ref.s, ref.a, coalesce(ref.a_end,ref.a), seg.seg FROM ref JOIN seg ON seg.id=ref.seg_id '
                    f"WHERE seg.seg IN ({','.join('?' * len(part))})", part):
                citations[loc].update(f'{s}:{a}' for a in range(start, end + 1))
    missing = [loc for loc in segs if loc not in meta]
    if missing:
        print(f'NOTE {len(missing)} digested locator(s) are not in the corpus index (renamed or removed); not checked: '
              + ', '.join(missing[:10]) + (' …' if len(missing) > 10 else ''))
    extra = defaultdict(set)
    for r in digest.overlay_rows():          # seg_id resolved by locator (the corpus index renumbers ids)
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
    done = checked_before(tier1)
    full = {v: ' ' + ' '.join(w) + ' ' for v, w in words.items()
            if len(w) >= 3 and len(' '.join(w)) >= 12}
    out, pairs, by_marker, by_citation, skipped_done, lost_common, no_verse = {}, 0, 0, 0, 0, 0, []
    for loc, (sid, _, src, kind, s, a, ae, head, text, seg_extra) in meta.items():
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
        norm = ' ' + normalize_map(text)[0] + ' '
        cited = {v for v in citations[loc] if v in full and full[v] in norm}
        vs |= cited
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
        by_citation += len(cited & set(vs))
        if vs:
            out[loc] = {'verses': vs, 'marked': sorted(marked & set(vs)), 'src': src, 'kind': kind, 'head': head or '',
                        'text': text, 'extra': json.loads(seg_extra or '{}'), 'notes': segs[loc],
                        'sha': digest.source_fingerprint(head, text, json.loads(seg_extra or '{}')),
                        'index': f'{s}:{a}' + (f'-{ae}' if ae != a else '') if s is not None and a is not None else ''}
            pairs += len(vs)
    if no_verse:
        print(f'NOTE {len(no_verse)} marker pair(s) name no verse of the Qur\'an text (an index range past the sūra\'s '
              f'end); not checked: ' + ', '.join(no_verse[:8]) + (' …' if len(no_verse) > 8 else ''))
    reached = {v for x in out.values() for v in x['verses']}
    counts = {'digested segments': len(segs), 'candidate pairs': pairs, 'segments to check': len(out),
              'characters': sum(len(x['text'] or '') for x in out.values()), 'pairs by marker only': by_marker,
              'pairs with explicit citation and full verse': by_citation,
              'pairs left out, checked by an earlier recheck': skipped_done,
              'too-common 2-word windows (a pair reached only through one is not checked)': len(common),
              'pairs not checked: reached only through a too-common window': lost_common}
    if only is not None:
        counts['scope verses'] = len(only)
        counts['scope verses with at least one candidate'] = len(reached & only)
    print('NOTE selection checks unnamed verses only; it cannot establish exhaustive missing-point coverage. '
          'Common-only matches and quotations without a unique window, marker or verified full-verse citation remain outside it.')
    return out, counts, quran


def segment_input(loc, x, notes):
    check = ', '.join(v + (' (number only)' if v in x.get('marked', []) else '') for v in x['verses'])
    lines = [f"=== SEGMENT {loc} | source {x['src']} | indexed {x['index'] or 'none'} | CHECK {check}"
             f" | {x['head']} ==="]
    provenance = {k: x.get('extra', {})[k] for k in digest.PROVENANCE_KEYS if k in x.get('extra', {})}
    if provenance:
        lines.append('CORPUS METADATA (provenance/index; not source words or an anchor): '
                     + json.dumps(provenance, ensure_ascii=False, sort_keys=True))
    lines += [(x['text'] or '').strip(), '--- notes already taken on this segment ---']
    lines += [note_line(n, r) for n, r in enumerate(notes, 1) if isinstance(r, dict)] or ['(none)']
    return '\n'.join(lines) + f'\n=== END SEGMENT {loc} ===\n\n'


def note_line(n, r):
    """An earlier note, compact (user, 2026-10-10: full JSON nearly doubled the run): the verses it is about, the
    verses it mentions, speaker, stance, claim and its exact words. Word tags and types are left out."""
    def text(v):
        return ', '.join(map(str, v)) if isinstance(v, list) else str(v or '')
    def one(v):
        return ' '.join(str(v).split()) if v else '-'
    return (f"[{n}] verses {text(r.get('verses')) or '-'}"
            + (f" | mentions {text(r.get('mentions'))}" if r.get('mentions') else '')
            + f" | {one(r.get('speaker'))} | {one(r.get('stance'))} | {one(r.get('claim'))} «{' '.join(str(r.get('anchor') or '').split())}»")


LUNA_USD_PER_M = 1.32         # API-equivalent USD per million chunk characters (tier-1 s1_87_114: $13.60 / 10.29M)


def cmd_plan(a):
    cand, counts, _ = candidates(a.tier1, *scope_of(a))
    for k, v in counts.items():
        print(f'{k}: {v:,}' if isinstance(v, int) else f'{k}: {v}')
    chunks = pack(cand, a.chunk_chars)
    est = sum(len(segment_input(loc, cand[loc], cand[loc]['notes'])) for loc in cand)
    print(f"plan: {est:,} rendered chunk characters, {len(chunks):,} chunks per model (Luna agents), "
          f"about ${est / 1e6 * LUNA_USD_PER_M:,.0f} API-equivalent at the historical tier-1 rate; cost is an estimate")


def pack(candidates, chunk_chars):
    if chunk_chars < 1:
        raise SystemExit('--chunk-chars must be positive')
    chunks, cur, size = [], [], 0
    for loc in sorted(candidates, key=lambda loc: (candidates[loc]['kind'], candidates[loc]['src'], loc)):
        x = candidates[loc]
        n = len(segment_input(loc, x, x['notes']))
        if n > chunk_chars:
            print(f'NOTE {loc}: {n:,} characters with its notes, over --chunk-chars; it forms a chunk alone')
        if cur and size + n > chunk_chars:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(loc)
        size += n
    if cur:
        chunks.append(cur)
    return chunks


def cmd_build(a):
    d = run_dir(a.run)
    if d.exists():
        raise SystemExit(f'{d} exists; choose a new run name')
    if a.chunk_chars < 1:
        raise SystemExit('--chunk-chars must be positive')
    tags = [tag_of(*spec.split(':')) for spec in a.models]
    open_ = unanswered(tags)
    if open_ and not a.allow_overlap:
        raise SystemExit(f'{len(open_)} chunk(s) of earlier recheck runs have no valid answer yet (running, failed or '
                         f'unrepaired): {", ".join(open_[:10])}{" …" if len(open_) > 10 else ""}. Their pairs are not '
                         'skipped, so a new run would check them twice. Finish or repair them first, or pass '
                         '--allow-overlap to build anyway.')
    if open_:
        print(f'NOTE --allow-overlap: {len(open_)} unanswered chunk(s) of earlier runs; their pairs are checked again here')
    only, index_only = scope_of(a)
    cand, counts, quran = candidates(a.tier1, only, index_only)
    counts['scope'] = {'verses': len(only) if only else 'all', 'index_only': index_only}
    for k, v in counts.items():
        print(f'{k}: {v:,}' if isinstance(v, int) else f'{k}: {v}')
    if not cand:
        raise SystemExit('no candidate pairs')
    notes = {loc: x['notes'] for loc, x in cand.items()}
    with connect() as con:
        smeta = {i: (k, json.loads(m or '{}')) for i, k, m in con.execute('SELECT id, kind, meta FROM src')}
    chunks = pack(cand, a.chunk_chars)
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
                     'source_sha256': {loc: cand[loc]['sha'] for loc in locs},
                     'input_sha256': hashlib.sha256(text.encode()).hexdigest(),
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
    dump(d / 'manifest.json', {'run': a.run, 'kind': 'recheck', 'row_tags': True, 'strict_fields': True,
                               'tier1': a.tier1, 'models': a.models, 'tags': tags,
                               'chunk_chars': a.chunk_chars, 'counts': counts, 'chunks': plan, 'spawn': spawns})
    print(f"{len(plan)} chunks, {sum(c['chars'] for c in plan):,} characters, {len(spawns)} spawn files; "
          f"written {d.relative_to(ROOT)}")


def check_chunk(d, tag, c):
    """Use exactly the same source and CHECK rules as coverage and downstream readers."""
    if not c.get('check') or not c.get('source_sha256'):
        return ['missing CHECK assignment or source provenance; rebuild this chunk'], 0
    return digest.check_chunk(d, tag, c, True, True)


def cmd_check(a):
    d = run_dir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    tags = [a.model] if a.model else man['tags']
    if not tags or any(tag not in man['tags'] for tag in tags):
        raise SystemExit('unknown model tag or no models in manifest')
    plan = [c for c in man['chunks'] if a.chunk is None or c['chunk'] == a.chunk]
    if a.chunk is not None and not plan:
        raise SystemExit(f'unknown chunk: {a.chunk}')
    bad = 0
    for tag in tags:
        for c in plan:
            problems, n = check_chunk(d, tag, c)
            for p in problems:
                print(f"{tag} c{c['chunk']:02d}: {p}")
            bad += len(problems)
            if a.chunk is not None:
                print('OK' if not problems else f'{len(problems)} problem(s)', f'({n} new notes)')
    if a.chunk is None:
        print('OK' if not bad else f'{bad} problem(s)')
    return 1 if bad else 0


def cmd_report(a):
    d = run_dir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    for tag in man['tags']:
        usd = done = new = segs_with = pairs = segments = 0
        for c in man['chunks']:
            x = digest.usage(d / 'runs', f"/root/v7d_{a.run}_{tag}_c{c['chunk']:02d}")
            if x is None:
                print(f"WARNING {tag} c{c['chunk']:02d}: no run.json")
                continue
            usd += x['usd']
            if not x['completed']:
                print(f"WARNING {tag} c{c['chunk']:02d}: did not complete ({x['via']}); its notes are not counted")
                continue
            done += 1
            f = d / 'out' / tag / f"c{c['chunk']:02d}.jsonl"
            valid = digest.valid_output_locs(f) if f.exists() else set()
            if len(valid) != len(c['locs']):
                print(f"WARNING {tag} c{c['chunk']:02d}: {len(c['locs']) - len(valid)} segment(s) lack valid output; not counted")
            segments += len(valid)
            pairs += sum(len(c['check'][loc]) for loc in valid)
            for line in (f.read_text().splitlines() if f.exists() else []):
                try:
                    row = json.loads(line)
                    if not isinstance(row, dict) or row.get('loc') not in valid:
                        continue
                    k = len(row['rows'])
                except (ValueError, AttributeError):
                    print(f"WARNING {tag} c{c['chunk']:02d}: unreadable line (run recheck.py check)")
                    continue
                new += k
                segs_with += k > 0
        planned = sum(len(v) for c in man['chunks'] for v in c['check'].values())
        print(f"{tag}: {done}/{len(man['chunks'])} runs, ${usd:.2f} API-equivalent, {pairs} pairs checked in "
              f"{segments} validated segments ({planned} pairs planned), {new} new notes in {segs_with} segments")


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
    p.add_argument('--chunk-chars', type=int, default=DEFAULT_CHUNK_CHARS)
    scope(p)
    p = sub.add_parser('build')
    p.add_argument('run')
    p.add_argument('--tier1', nargs='+', default=['luna-max'])
    scope(p)
    p.add_argument('--models', nargs='+', default=['gpt-6-luna:max'])
    p.add_argument('--chunk-chars', type=int, default=DEFAULT_CHUNK_CHARS)
    p.add_argument('--allow-overlap', action='store_true',
                   help='build although chunks of earlier recheck runs have no valid answer yet (their pairs are checked again)')
    p = sub.add_parser('check')
    p.add_argument('run')
    p.add_argument('--model')
    p.add_argument('--chunk', type=int)
    p = sub.add_parser('report')
    p.add_argument('run')
    a = ap.parse_args()
    return globals()[f'cmd_{a.cmd}'](a)


if __name__ == '__main__':
    sys.exit(main() or 0)
