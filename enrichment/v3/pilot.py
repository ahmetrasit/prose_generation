#!/usr/bin/env python3
"""Read-only research views, native usage totals, and simple rendering for the 1:6 pilot.

This helper never launches models or writes tracking ledgers.
"""
import argparse
import json
import re
import sqlite3
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE_DIR = ROOT / '_commentary/v16/out/1_6/DM.r13.images.r13.map3.nohft.tool.tool.tool'


def select_input(directory, stem='1_6'):
    augmented = directory / 'augment.augment9.opus' / f'{stem}.reading.tr.md'
    return augmented if augmented.is_file() else directory / f'{stem}.reading.tr.md'


BASE = select_input(BASE_DIR)
DB = ROOT / 'enrichment/corpus/corpus.sqlite'
WORK = ROOT / 'enrichment/v3/work/1_6'


def connect():
    return sqlite3.connect(f'file:{DB}?mode=ro', uri=True)


def prose():
    text = BASE.read_bytes().decode('utf-8')
    bounds, start = [], 0
    for match in re.finditer(r'\n[ \t]*\n', text):
        bounds.append((start, match.start()))
        start = match.end()
    bounds.append((start, len(text)))
    groups, current = {}, 0
    for lo, hi in bounds:
        body = text[lo:hi].strip()
        if not body:
            continue
        if body.startswith('<!-- v16:augment '):
            p = int(re.search(r'\bpara=(\d+)', body)[1])
            if p != current:
                raise ValueError(f'Augmentation paragraph {p} follows {current}')
            groups[current][1] = hi
        elif not body.startswith(('#', 'Kaynaklar:')):
            current += 1
            groups[current] = [lo, hi]
    return text, groups


def core_packets():
    groups = json.loads((ROOT / 'enrichment/v2/groups.json').read_text())['groups']
    mapping = {s: g['id'] for g in groups for s in g['sources']}
    combine = {'meani-nahiv': 'language', 'kiraat': 'language',
               'modern-arap': 'modern', 'modern-bati': 'modern', 'ulum-nuzul': 'modern',
               'turkce': 'turkish-meal', 'meal': 'turkish-meal', 'isari': 'mezhep-isari',
               'mezhep': 'mezhep-isari'}
    con = connect()
    metadata = {sid: json.loads(meta) for sid, meta in con.execute('SELECT id,meta FROM src')}
    direct = '(seg.s=1 AND seg.a<=6 AND coalesce(seg.a_end,seg.a)>=6)'
    rows = con.execute('WITH selected(id) AS ('
                       'SELECT id FROM seg WHERE s=1 AND a<=6 AND coalesce(a_end,a)>=6 '
                       'UNION SELECT seg_id FROM ref WHERE s=1 AND a<=6 AND coalesce(a_end,a)>=6) '
                       'SELECT seg.seg,seg.src,src.kind,seg.head,seg.text,seg.extra,' + direct +
                       ' FROM selected JOIN seg ON seg.id=selected.id JOIN src ON src.id=seg.src '
                       "WHERE src.kind NOT IN ('lexicon','quran') ORDER BY seg.src,seg.id")
    by = defaultdict(list)
    for loc, sid, kind, head, body, extra, directly_tied in rows:
        if kind == 'quran':
            continue
        group = 'meal' if kind in ('meal', 'translation') else mapping.get(sid, kind)
        group = combine.get(group, group)
        if not directly_tied:
            group = 'citing-eq' if sid == 'EQ' else 'citing-study' if sid == 'STUDYQURAN' else 'citing-other'
        meta, extra = metadata[sid], json.loads(extra or '{}')
        shown = [f'### {loc} | {meta.get("author", sid)} | {meta.get("title", "")}\n{head or ""}\n{body or ""}']
        for key in ('text_status', 'marker_found', 'align_uncertain', 'sahih', 'graded_by', 'notes', 'tr', 'en'):
            value = extra.get(key)
            if value not in (None, '', [], {}) and str(value) != str(body):
                shown.append(f'{key}: {value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)}')
        rendered = '\n'.join(shown) + '\n'
        # A long passage is split for delivery, never silently truncated.
        while len(rendered) > 45000:
            cut = rendered.rfind('\n', 20000, 45000)
            cut = cut if cut > 0 else 45000
            by[group].append((loc, rendered[:cut] + '\n[Continues in next part]\n'))
            rendered = f'### {loc} [continued]\n' + rendered[cut:]
        by[group].append((loc, rendered))
    packets = {}
    for group, rows in sorted(by.items()):
        part, text, locs = 1, '', []
        for loc, rendered in rows:
            if text and len(text) + len(rendered) > 48000:
                packets[f'{group}.{part}'] = (text, locs)
                part, text, locs = part + 1, '', []
            text += rendered + '\n'
            locs.append(loc)
        if text:
            packets[f'{group}.{part}'] = (text, locs)
    return packets


def delivery_parts(text, limit=9000):
    parts, start = [], 0
    while start < len(text):
        end = min(len(text), start + limit)
        if end < len(text):
            boundary = text.rfind('\n', start + limit // 2, end)
            if boundary > start:
                end = boundary + 1
        part = text[start:end]
        if start and not part.lstrip().startswith('### '):
            headings = list(re.finditer(r'^### [^\n]+', text[:start], re.M))
            if headings:
                part = headings[-1][0] + ' [delivery continuation]\n' + part
        parts.append(part)
        start = end
    return parts


def research_notes(track):
    folder = WORK / track
    claims = {x['id']: x for x in map(json.loads, (folder / 'claims.jsonl').read_text().splitlines())}
    notes, seen = [], set()
    for file in sorted((folder / 'notes').glob('*.jsonl')):
        for line in file.read_text().splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row['id'] in seen:
                raise ValueError(f'Duplicate note ID: {row["id"]}')
            seen.add(row['id'])
            paragraphs = sorted(set(row.get('p') or [p for cid in row['c'] for p in claims[cid]['p']]))
            notes.append((row, paragraphs, file))
    return claims, notes


def notes_for(track, paragraphs):
    claims, notes = research_notes(track)
    selected = set(paragraphs)
    related = [(row, ps, file) for row, ps, file in notes if selected.intersection(ps)]
    linked = {cid for row, _, _ in related for cid in row['c']}
    for row, ps, file in related:
        print(json.dumps({'file': str(file.relative_to(ROOT)), 'paragraphs': ps, **row}, ensure_ascii=False))
    missing = [c for cid, c in claims.items() if selected.intersection(c['p']) and cid not in linked]
    if missing:
        print('[Claims without a linked note; a link alone does not establish adequate treatment]')
        for row in missing:
            print(json.dumps(row, ensure_ascii=False))


def cited_leads(group):
    """Discovery excerpts from secondary passages citing 1:6; never full-source substitutes."""
    con = connect()
    rows = con.execute('SELECT DISTINCT seg.seg,seg.src,seg.head,seg.text FROM ref '
                       'JOIN seg ON seg.id=ref.seg_id JOIN src ON src.id=seg.src '
                       'WHERE ref.s=1 AND ref.a<=6 AND coalesce(ref.a_end,ref.a)>=6 '
                       "AND src.kind NOT IN ('lexicon','quran') "
                       'AND NOT (coalesce(seg.s,0)=1 AND coalesce(seg.a,0)<=6 AND coalesce(seg.a_end,seg.a,0)>=6) '
                       'ORDER BY seg.src,seg.id')
    print('[Discovery excerpts only. Read relevant surrounding external passages before attributing a position.]')
    for loc, sid, head, body in rows:
        if (sid == 'EQ') != (group == 'eq'):
            continue
        matches = []
        for m in re.finditer(r'(?<!\d)1\s*:\s*(\d{1,3})(?:\s*[–—-]\s*(\d{1,3}))?', body or ''):
            if int(m[1]) <= 6 <= int(m[2] or m[1]):
                matches.append(m.start())
        excerpts = []
        last_end = 0
        for at in matches[:3]:
            lo, hi = max(last_end, at - 160), min(len(body), at + 500)
            if hi > lo:
                excerpts.append(body[lo:hi]); last_end = hi
        if not excerpts:
            excerpts = [(body or '')[:600]]
        print(json.dumps({'loc': loc, 'head': head, 'source_characters': len(body or ''),
                          'excerpt': ' […] '.join(excerpts)}, ensure_ascii=False))


def render(track, write=True):
    frozen, groups = prose()
    _, notes = research_notes(track)
    if not notes:
        raise ValueError('No research notes to render')
    notes.sort(key=lambda x: (x[1][0], x[0]['id']))
    primary, links, sources = defaultdict(list), defaultdict(list), set()
    for number, (row, ps, _) in enumerate(notes, 1):
        citations = []
        for source in row.get('src', []):
            loc, anchor = source['loc'], source.get('anchor', '')
            if source.get('url'):
                pointer = f'[{loc}]({source["url"]})'
            else:
                sources.add(loc.split(':', 1)[0])
                pointer = loc
            citations.append(pointer + (f' — «{anchor}»' if anchor else ''))
        suffix = ' (' + '; '.join(citations) + ')' if citations else ''
        primary[ps[0]].append(f'> - <a id="enrichment-note-{number}"></a>**{number}.** {row["text"]}{suffix}')
        for p in ps[1:]:
            links[p].append(f'[{number}](#enrichment-note-{number})')
    insertions = []
    for p, (_, end) in groups.items():
        lines = primary[p][:]
        if links[p]:
            lines.append('> Bu paragrafla da ilgili önceki kaynak notları: ' + ', '.join(links[p]) + '.')
        if lines:
            block = f'\n\n<!-- enrichment:v3 paragraph={p} -->\n> **Kaynak notları**\n>\n' + '\n>\n'.join(lines) + '\n<!-- /enrichment:v3 -->'
            insertions.append((end, block))
    output, at = [], 0
    for end, block in insertions:
        output.extend([frozen[at:end], block])
        at = end
    output.append(frozen[at:])
    body = ''.join(output)
    # One direct preservation check, without hashes or a separate acceptance pass.
    recovered = re.sub(r'\n\n<!-- enrichment:v3 paragraph=\d+ -->.*?\n<!-- /enrichment:v3 -->', '', body, flags=re.S)
    if recovered != frozen:
        raise ValueError('Rendering changed the frozen text')
    con = connect()
    metadata = {sid: json.loads(meta) for sid, meta in con.execute('SELECT id,meta FROM src') if sid in sources}
    missing = sources - metadata.keys()
    if missing:
        raise ValueError(f'Unknown source IDs: {sorted(missing)}')
    bibliography = []
    for sid in sorted(sources):
        meta = metadata[sid]
        author = meta.get('author') or meta.get('translator') or ''
        bibliography.append(f'- **{sid}**: ' + (author + ', ' if author else '') + f'*{meta.get("title", sid)}*.')
    intro = ('> **Kaynak notları hakkında:** Notlar, bulgularla örtüşen, ayrışan, onları genişleten veya farklı bir açıdan ele alan kaynak görüşlerini tanıtır. '
             '“Bulunamadı” ifadeleri incelenen kaynaklarla sınırlıdır; tarih boyunca hiç söylenmediği anlamına gelmez. '
             'Tekrarlanan ilişkiler önceki nota bağlantıyla gösterilir.\n\n')
    tail = ('\n\n## Kaynak kısaltmaları\n\n'
            'Notlardaki konumlar ayet, hadis, madde veya cilt/sayfayı gösterir; örneğin `v1p167`, cilt 1, sayfa 167’dir. '
            'Kısa Arapça ibareler ilgili pasajı bulmaya yardım eder.\n\n' + '\n'.join(bibliography) + '\n')
    result = intro + body + tail
    if write:
        target = WORK / track / '1_6.enriched.tr.md'
        target.write_bytes(result.encode('utf-8'))
        print(f'{target}: {len(notes)} notes; frozen text preserved exactly')
    return result


def native_usage(file, end=None):
    end = end or file.stat().st_size
    last = None
    with file.open('rb') as handle:
        handle.seek(max(0, end - 800000))
        for line in handle:
            if handle.tell() > end:
                break
            try:
                row = json.loads(line)
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            payload = row.get('payload', {})
            if row.get('type') == 'event_msg' and payload.get('type') == 'token_count' and payload.get('info'):
                last = payload['info']
    return last


def usage(detail=False, context=None):
    totals = defaultdict(lambda: defaultdict(int))
    counts = defaultdict(int)
    sessions = Path('/Users/ahmetrasit/.codex/sessions/2026/10/06')
    threads = {}
    for file in sessions.glob('*.jsonl'):
        with file.open() as handle:
            meta = json.loads(handle.readline()).get('payload', {})
            if meta.get('cwd') != str(ROOT):
                continue
            header = ''
            for _, line in zip(range(12), handle):
                row = json.loads(line)
                payload = row.get('payload', {})
                if row.get('type') == 'response_item' and payload.get('role') == 'user':
                    for content in payload.get('content', []):
                        value = content.get('text', '')
                        if value.startswith('ENRICHMENT_V3_1_6 track='):
                            header = value.split('.', 1)[0]
            threads[meta['id']] = {'file': file, 'meta': meta, 'header': header}

    def lane_for(tid):
        thread = threads.get(tid)
        if not thread:
            return None
        meta = thread['meta']
        agent = str(meta.get('agent_path', ''))
        if agent.startswith('/root/enrich_1_6_'):
            return 'sol-max' if '_sol_' in agent else 'astra-xhigh' if '_astra_' in agent else None
        match = re.search(r'track=(sol-max|astra-xhigh)', thread['header'])
        if match:
            return match[1]
        parent = meta.get('forked_from_id')
        return lane_for(parent) if parent else None

    def run_for(tid):
        thread = threads.get(tid)
        if not thread:
            return 'interrupted'
        if re.search(r'\brun=bounded\b', thread['header']):
            # Superseded hadith assignments exceeded the intended context size.
            if re.search(r'\bstage=hadith01a?$', thread['header']):
                return 'interrupted'
            return 'clean'
        parent = thread['meta'].get('forked_from_id')
        return run_for(parent) if parent else 'interrupted'

    if context:
        track, stage = context
        matches = [thread for tid, thread in threads.items()
                   if lane_for(tid) == track and thread['header'].endswith('stage=' + stage)]
        if not matches:
            raise ValueError(f'No native usage session for {track}/{stage}')
        current = max(matches, key=lambda thread: thread['file'].stat().st_mtime)
        info = native_usage(current['file'])
        if not info:
            raise ValueError(f'Native usage not yet available for {track}/{stage}')
        print(json.dumps({'context_input_tokens': info['last_token_usage']['input_tokens']}))
        return

    for tid, thread in threads.items():
        lane = lane_for(tid)
        if not lane:
            continue
        run = run_for(tid)
        group = (lane, run)
        info = native_usage(thread['file'])
        if info:
            last = info['total_token_usage']
            base = thread['meta'].get('history_base') or {}
            parent = threads.get(base.get('thread_id'))
            inherited = native_usage(parent['file'], base.get('end_byte_offset')) if parent else None
            baseline = inherited['total_token_usage'] if inherited else {}
            counts[group] += 1
            delta = {}
            for key, value in last.items():
                if isinstance(value, int):
                    delta[key] = value - baseline.get(key, 0)
                    totals[group][key] += delta[key]
            if detail:
                print(json.dumps({'session': tid, 'track': lane, 'run': run,
                                  'stage': thread['header'] or thread['meta'].get('agent_path', 'continuation'),
                                  'last_context_input': info['last_token_usage']['input_tokens'],
                                  **delta}, ensure_ascii=False))
    for (lane, run), row in sorted(totals.items()):
        row['sessions_with_usage'] = counts[(lane, run)]
        row['visible_output_tokens'] = row['output_tokens'] - row['reasoning_output_tokens']
        uncached = max(0, row['input_tokens'] - row['cached_input_tokens'] - row['cache_write_input_tokens'])
        rate = 2 if lane == 'sol-max' else 10
        cost = (uncached * rate + row['cached_input_tokens'] * rate * .1 +
                row['cache_write_input_tokens'] * rate * 1.25 + row['output_tokens'] * rate * 5) / 1e6
        print(json.dumps({'track': lane, 'run': run, **row, 'standard_api_equivalent_usd': round(cost, 4)}, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='cmd', required=True)
    sub.add_parser('packets')
    packet = sub.add_parser('packet'); packet.add_argument('name'); packet.add_argument('--part', type=int)
    para = sub.add_parser('prose'); para.add_argument('numbers', help='Comma-separated paragraph numbers')
    note = sub.add_parser('notes'); note.add_argument('track', choices=['sol-max', 'astra-xhigh']); note.add_argument('numbers')
    cited = sub.add_parser('cited'); cited.add_argument('group', choices=['eq', 'other'])
    rendered = sub.add_parser('render'); rendered.add_argument('track', choices=['sol-max', 'astra-xhigh'])
    use = sub.add_parser('usage'); use.add_argument('--detail', action='store_true')
    context = sub.add_parser('context', help='Current assignment input size from existing native usage')
    context.add_argument('track', choices=['sol-max', 'astra-xhigh']); context.add_argument('stage')
    args = parser.parse_args()
    if args.cmd == 'usage':
        usage(args.detail)
    elif args.cmd == 'context':
        usage(context=(args.track, args.stage))
    elif args.cmd == 'notes':
        notes_for(args.track, [int(p) for p in args.numbers.split(',')])
    elif args.cmd == 'cited':
        cited_leads(args.group)
    elif args.cmd == 'render':
        render(args.track)
    elif args.cmd == 'prose':
        text, groups = prose()
        for number in map(int, args.numbers.split(',')):
            lo, hi = groups[number]
            print(f'[Paragraph {number}]\n{text[lo:hi]}\n')
    else:
        packets = core_packets()
        if args.cmd == 'packet':
            text = packets[args.name][0]
            if args.part:
                parts = delivery_parts(text)
                print(f'[{args.name}: part {args.part}/{len(parts)}; read all assigned parts]')
                print(parts[args.part - 1])
            else:
                print(text)
        else:
            for name, (text, locs) in packets.items():
                print(json.dumps({'packet': name, 'characters': len(text), 'segments': len(locs),
                                  'parts': len(delivery_parts(text)),
                                  'sources': list(dict.fromkeys(x.split(':')[0] for x in locs))}, ensure_ascii=False))


if __name__ == '__main__':
    main()
