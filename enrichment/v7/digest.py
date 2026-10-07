#!/usr/bin/env python3
"""Enrichment v7 verse digests: build the inputs and spawn files, check the outputs. Launches no model.

A digest records what one source says about the verses its segments are tied to: one line per segment,
one row per claim, each row with a short verbatim anchor. Agents run through enrichment/v5/run_codex.py
(Codex, at most seven at a time); the same chunk files serve every model.

  digest.py build RUN --ayat 100:1 87:6 --models gpt-6-luna:max gpt-6-sol:high
  digest.py check RUN [--model TAG] [--chunk N]     two checks: every segment answered, every anchor verbatim
  digest.py report RUN                              per-model totals and costs

Every skipped source or segment is printed and listed in RUN/manifest.json.
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'enrichment/v5'))
from common import CHUNK_CHARS, OVERLAY, PART_CHARS, TRANSLATION_OK, connect, contains, dump, rows  # noqa: E402

V7 = ROOT / 'enrichment/v7'
BRIEF = V7 / 'briefs/digest.md'
# Stage 1 kinds. Meal and translations go to the meal table; lexicon, poetry, wujuh, grammar and hadith
# are keyed by root or term in a later stage.
KINDS = ('tafsir', 'tafsir_tr', 'maani', 'nazm', 'isari', 'modern', 'qiraat', 'ulum', 'reference', 'sira')
GUIDE = {
    'tafsir': 'A Qurʾān commentary. Record the author\'s own explanation of each verse, every view it reports with '
              'who holds it, reports and narrations (the authority at the end of the chain, the gist, any grading '
              'the author states), occasions of revelation, linguistic, grammatical, rhetorical, qirāʾa, legal and '
              'theological points, disagreements and the view the author prefers, and links it draws to other verses.',
    'tafsir_tr': 'A Turkish Qurʾān commentary. Record the author\'s explanation, the views he reports and from whom, his '
                 'preferences, his word choices in rendering the verse, and the links he draws to other verses.',
    'maani': 'A maʿānī al-Qurʾān work (language and grammar of the Qurʾān). Record each lexical, grammatical and '
             'syntactic analysis, the variant readings discussed, the authorities and the poetry or Arab usage cited '
             'as evidence (poet and the word witnessed), and which analysis the author prefers.',
    'nazm': 'A work on the coherence (naẓm) of the Qurʾān. Record how the author links the verse to its neighbours, '
            'its passage and the sūra\'s theme, the structure he sees, and the other verses he connects it to.',
    'isari': 'A Sufi (ishārī) commentary. Record the outward explanation the author gives, then each inward (ishārī) '
             'reading, the authorities and Sufi masters he cites, and the spiritual lessons he draws.',
    'modern': 'A modern commentary or study. Record the author\'s reading of the verse, his arguments and evidence, the '
              'classical or modern views he engages, where he departs from them, and the links to other verses.',
    'qiraat': 'A work on the variant readings. Record each reading, its readers, the argument (ḥujja) for it, and the '
              'difference in meaning the author draws.',
    'ulum': 'A work on the Qurʾānic sciences. Record what it says about the verse: rhetoric, inimitability, '
            'abrogation, occasions of revelation, structure, with the authorities cited.',
    'reference': 'A reference work. Record what the entry says about the verse and its terms, with the scholars cited.',
    'sira': 'A biography of the Prophet or a history. Record the events it ties to the verse, its sources and '
            'reports, and any dating or occasion it gives.',
}


def run_dir(run):
    return V7 / 'work' / run


def parse_ayah(text):
    s, a = text.split(':')
    return int(s), int(a)


def gather(ayat):
    """Segments tied to the ayat (index range plus range overlay), stage-1 kinds, text held locally."""
    skipped = []
    with connect() as con:
        src = {i: (k, acc, json.loads(m or '{}')) for i, k, acc, m in con.execute('SELECT id,kind,access,meta FROM src')}
        extra = defaultdict(set)
        if OVERLAY.exists():
            for r in rows(OVERLAY):
                for a in range(r['indexed_end'] + 1, r['a_end'] + 1):
                    extra[r['s'], a].add(r['seg_id'])
        found = {}
        for s, a in ayat:
            hits = con.execute('SELECT id,seg,src,s,a,coalesce(a_end,a),head,text FROM seg WHERE s=? AND a<=? '
                               'AND coalesce(a_end,a)>=?', (s, a, a)).fetchall()
            if extra[s, a]:
                q = ','.join('?' * len(extra[s, a]))
                hits += con.execute(f'SELECT id,seg,src,s,a,coalesce(a_end,a),head,text FROM seg WHERE id IN ({q})',
                                    list(extra[s, a])).fetchall()
            full = {h[2][:-5] for h in hits if h[2].endswith('-FULL')}
            for sid, loc, sr, ss, aa, ae, head, text in hits:
                kind, access, _ = src[sr]
                why = None
                if kind not in KINDS:
                    why = f'kind {kind}: meal table or a later stage'
                elif access != 'yerel':
                    why = f'access {access}: no local text'
                elif sr in full:
                    why = f'{sr}-FULL covers {s}:{a}'
                elif not (text or '').strip():
                    why = 'empty text'
                if why:
                    skipped.append({'ayah': f'{s}:{a}', 'loc': loc, 'src': sr, 'reason': why})
                    continue
                if sid in extra[s, a]:
                    ae = max(ae, a)
                found[sid] = {'loc': loc, 'src': sr, 'kind': kind, 'verses': f'{ss}:{aa}' + (f'-{ae}' if ae != aa else ''),
                              'head': head or '', 'text': text}
    return src, [found[k] for k in sorted(found)], skipped


def chunks(segments):
    """Whole sources packed in kind order into chunks of at most CHUNK_CHARS; a source is split only when it alone
    is longer, and then between segments (a longer segment stands alone)."""
    by_src = defaultdict(list)
    for g in segments:
        by_src[g['src']].append(g)
    out, cur, size = [], [], 0
    for sr in sorted(by_src, key=lambda s: (by_src[s][0]['kind'], s)):
        n = sum(len(g['text']) for g in by_src[sr])
        if cur and size + n > CHUNK_CHARS:
            out.append(cur)
            cur, size = [], 0
        for g in by_src[sr]:
            if cur and size + len(g['text']) > CHUNK_CHARS:
                out.append(cur)
                cur, size = [], 0
            cur.append(g)
            size += len(g['text'])
    if cur:
        out.append(cur)
    return out


def source_line(sr, meta, kind):
    bits = [f"{meta.get('title', sr)}", meta.get('author') or '', f"d. {meta['death_ah']} AH" if meta.get('death_ah') else '']
    line = f'{sr}: ' + ', '.join(b for b in bits if b) + f' ({kind})'
    if sr in TRANSLATION_OK:
        line += f'\nTRANSLATION: {TRANSLATION_OK[sr]}'
    return line


def build(a):
    d = run_dir(a.run)
    if d.exists():
        raise SystemExit(f'{d} exists; choose a new run name')
    ayat = [parse_ayah(x) for x in a.ayat]
    src, segments, skipped = gather(ayat)
    with connect() as con:
        verse_text = {f'{s}:{x}': con.execute("SELECT text FROM seg JOIN src ON src.id=seg.src WHERE src.kind='quran' "
                                              'AND s=? AND a=?', (s, x)).fetchone()[0] for s, x in ayat}
    parts_dir = d / 'chunks'
    parts_dir.mkdir(parents=True)
    plan = []
    for n, chunk in enumerate(chunks(segments), 1):
        srcs = list(dict.fromkeys(g['src'] for g in chunk))
        kinds = list(dict.fromkeys(src[s][0] for s in srcs))
        text = ''.join(f"=== SEGMENT {g['loc']} | source {g['src']} | verses {g['verses']} | {g['head']} ===\n"
                       f"{g['text'].strip()}\n\n" for g in chunk)
        parts = [text[i:i + PART_CHARS] for i in range(0, len(text), PART_CHARS)]
        for k, p in enumerate(parts):
            tail = f'\n<<part {k} ends; continues in part {k + 1}>>' if k + 1 < len(parts) else '\n<<end of chunk>>'
            (parts_dir / f'c{n:02d}.p{k}.txt').write_text(f'<<chunk {n} part {k} of 0..{len(parts) - 1}>>\n{p}{tail}\n')
        plan.append({'chunk': n, 'sources': srcs, 'kinds': kinds,
                     'source_lines': [source_line(s, src[s][2], src[s][0]) for s in srcs],
                     'locs': [g['loc'] for g in chunk], 'chars': len(text), 'parts': len(parts)})
    brief = BRIEF.read_text()
    spawns = []
    for spec in a.models:
        model, effort = spec.split(':')
        tag = model.split('-')[-1] + '-' + effort
        for c in plan:
            agent = f'/root/v7d_{a.run}_{tag}_c{c["chunk"]:02d}'
            fill = {'AGENT': agent, 'MODEL': model, 'EFFORT': effort, 'RUN': a.run, 'TAG': tag, 'N': str(c['chunk']),
                    'NN': f'{c["chunk"]:02d}', 'LAST': str(c['parts'] - 1), 'SEGMENTS': str(len(c['locs'])),
                    'NSRC': str(len(c['sources'])), 'SOURCES': '\n'.join(f'- {x}' for x in c['source_lines']),
                    'GUIDES': '\n'.join(f'- **{k}**: {GUIDE[k]}' for k in c['kinds']),
                    'AYAT': '\n'.join(f'- {k}: {v}' for k, v in verse_text.items())}
            text = brief
            for k, v in fill.items():
                text = text.replace('{' + k + '}', v)
            f = d / 'spawn' / f'{tag}_c{c["chunk"]:02d}.md'
            f.parent.mkdir(exist_ok=True)
            f.write_text(text)
            spawns.append(str(f.relative_to(ROOT)))
        (d / 'out' / tag).mkdir(parents=True)
    dump(d / 'manifest.json', {'run': a.run, 'ayat': a.ayat, 'models': a.models, 'chunk_chars': CHUNK_CHARS,
                               'chunks': plan, 'skipped': skipped, 'spawn': spawns})
    total = sum(c['chars'] for c in plan)
    print(f'{len(segments)} segments, {len(plan)} chunks, {total:,} characters, {len(spawns)} spawn files')
    for c in plan:
        print(f"  c{c['chunk']:02d} {len(c['sources']):2d} sources {len(c['locs']):3d} segments {c['chars']:7,} chars: "
              + ' '.join(c['sources']))
    routine = defaultdict(int)
    for s in skipped:
        if s['reason'].startswith(('kind meal', 'kind translation', 'kind quran')):
            routine[s['ayah'], s['reason']] += 1
        else:
            print(f"SKIPPED {s['ayah']} {s['loc']}: {s['reason']}")
    for (ayah, reason), k in sorted(routine.items()):
        print(f"SKIPPED {ayah}: {k} segments, {reason} (listed in manifest.json)")


def check_chunk(d, tag, c):
    """Problems in one output file: missing, extra or duplicate segments, bad lines, anchors not verbatim."""
    f = d / 'out' / tag / f"c{c['chunk']:02d}.jsonl"
    if not f.exists():
        return [f'{f.name}: no output file'], 0
    with connect() as con:
        text = {loc: con.execute('SELECT text FROM seg WHERE seg=?', (loc,)).fetchone()[0] for loc in c['locs']}
    problems, seen, n_rows = [], [], 0
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            x = json.loads(line)
        except ValueError as e:
            problems.append(f'line {i}: not JSON ({e})')
            continue
        loc = x.get('loc')
        if loc not in text:
            problems.append(f'line {i}: locator {loc!r} is not in this chunk')
            continue
        seen.append(loc)
        rs = x.get('rows')
        if not isinstance(rs, list):
            problems.append(f'{loc}: "rows" must be a list')
            continue
        if not rs and not (x.get('none') or '').strip():
            problems.append(f'{loc}: no rows and no "none" reason')
        for j, r in enumerate(rs, 1):
            n_rows += 1
            missing = [k for k in ('verses', 'speaker', 'stance', 'claim', 'anchor') if not r.get(k)]
            if missing:
                problems.append(f'{loc} row {j}: missing {", ".join(missing)}')
            if r.get('anchor') and not contains(text[loc], r['anchor']):
                problems.append(f'{loc} row {j}: anchor not found verbatim in the segment: {r["anchor"][:80]}')
    for loc in c['locs']:
        if loc not in seen:
            problems.append(f'{loc}: segment has no line')
    for loc in {x for x in seen if seen.count(x) > 1}:
        problems.append(f'{loc}: more than one line')
    return problems, n_rows


def check(a):
    d = run_dir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    tags = [a.model] if a.model else sorted(p.name for p in (d / 'out').iterdir())
    plan = [c for c in man['chunks'] if a.chunk in (None, c['chunk'])]
    if a.chunk is not None:  # the agent's own check: print problems or OK, record nothing
        problems, _ = check_chunk(d, tags[0], plan[0])
        print('OK' if not problems else '\n'.join(problems[:60]) + (f'\n... {len(problems) - 60} more' if len(problems) > 60 else ''))
        return
    for tag in tags:
        result = {}
        for c in plan:
            problems, n_rows = check_chunk(d, tag, c)
            result[f"c{c['chunk']:02d}"] = {'rows': n_rows, 'problems': problems}
            for p in problems:
                print(f"WARNING {tag} c{c['chunk']:02d}: {p}")
        dump(d / 'out' / tag / 'check.json', result)
        bad = sum(1 for v in result.values() if v['problems'])
        print(f'{tag}: {len(result)} chunks checked, {bad} with problems, {sum(v["rows"] for v in result.values())} rows')


def report(a):
    d = run_dir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    src_chars = {f"c{c['chunk']:02d}": c['chars'] for c in man['chunks']}
    for tag in sorted(p.name for p in (d / 'out').iterdir()):
        usd = reqs = peak = done = 0
        for c in man['chunks']:
            r = d / 'runs' / f"v7d_{a.run}_{tag}_c{c['chunk']:02d}" / 'run.json'
            if r.exists():
                x = json.loads(r.read_text())
                done += 1
                usd += x.get('usd_equivalent', 0)
                reqs += x.get('requests', 0)
                peak = max(peak, x.get('max_request_input_tokens') or 0)
                if not x.get('turn_completed') or x.get('returncode'):
                    print(f"WARNING {tag} c{c['chunk']:02d}: rc {x.get('returncode')}, completed {x.get('turn_completed')}")
        out_chars = sum(len(f.read_text()) for f in (d / 'out' / tag).glob('c*.jsonl'))
        chk = d / 'out' / tag / 'check.json'
        rows_n = sum(v['rows'] for v in json.loads(chk.read_text()).values()) if chk.exists() else '?'
        print(f'{tag}: {done}/{len(man["chunks"])} runs, ${usd:.2f} API-equivalent, {reqs} requests, peak {peak:,} tokens, '
              f'{rows_n} rows, digest/source characters {out_chars / max(1, sum(src_chars.values())):.2f}')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('build'); p.add_argument('run'); p.add_argument('--ayat', nargs='+', required=True)
    p.add_argument('--models', nargs='+', required=True)
    p = sub.add_parser('check'); p.add_argument('run'); p.add_argument('--model'); p.add_argument('--chunk', type=int)
    p = sub.add_parser('report'); p.add_argument('run')
    a = parser.parse_args()
    {'build': build, 'check': check, 'report': report}[a.cmd](a)


if __name__ == '__main__':
    main()
