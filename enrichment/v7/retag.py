#!/usr/bin/env python3
"""Enrichment v7 retag: add the row tags (verse words, type) to tier-1 rows digested before row tags existed.
Launches no model. Claims and exact words are never changed; tags go to RUN/retag/out/<TAG>/cNN.jsonl and are read
by merge.py through digest.row_tags().

  retag.py build RUN (--ayat 95:1 95:2 … | --page PATH --ayah A) --models gpt-6-luna:max [--from luna-max] [--chunk-chars 25000]
  retag.py check RUN [--model TAG] [--chunk N]      every row answered once; words in its verses; type in the list
  retag.py report RUN                               runs, API-equivalent cost, tagged rows

Rows that already carry tags (digested with row tags, or tagged by an earlier retag run) are skipped and counted.
"""
import argparse
import json
from collections import defaultdict

import digest
from digest import PART_CHARS, ROOT, TYPE_GUIDE, V7, dump, run_dir, tag_problems

BRIEF = V7 / 'briefs/retag.md'
DEFAULT_CHUNK_CHARS = 25_000


def untagged_rows(ayat, tags_from):
    """Every tier-1 row on the ayat (first digest of each segment, in tag order), minus rows already tagged."""
    want = set(ayat)
    tagged = digest.row_tags()
    seen, out, skipped = set(), [], 0
    for tag in tags_from:
        for f in sorted((V7 / 'work').glob(f'*/out/{tag}/c*.jsonl')):
            for i, line in enumerate(f.read_text().splitlines(), 1):
                if not line.strip():
                    continue
                try:
                    x = json.loads(line)
                except ValueError:
                    print(f'WARNING {f.relative_to(V7)} line {i}: not JSON; skipped')
                    continue
                if x['loc'] in seen:
                    continue
                seen.add(x['loc'])
                for n, r in enumerate(x['rows'], 1):
                    vs = [v for v in r.get('verses') or [] if v in want]
                    if not vs:
                        continue
                    rid = f"{x['loc']}/r{n}"
                    if (r.get('words') and r.get('type')) or rid in tagged:
                        skipped += 1
                        continue
                    out.append({'id': rid, 'verses': r.get('verses') or [], 'first': vs[0],
                                'claim': r.get('claim', ''), 'anchor': r.get('anchor', '')})
    return out, skipped


def build(a):
    d = run_dir(a.run) / 'retag'
    if d.exists():
        raise SystemExit(f'{d} exists; choose a new run name')
    if bool(a.ayat) == bool(a.page):
        raise SystemExit('give either --ayat, or --page with --ayah')
    if a.page:
        import write
        a.ayat = write.page_verses(a.page, a.ayah)
    rows, skipped = untagged_rows(a.ayat, a.tags_from)
    print(f'{len(a.ayat)} verses: {len(rows)} rows to tag, {skipped} already tagged (skipped)')
    if not rows:
        raise SystemExit('nothing to tag')
    def key(v):
        """Sort key for a verse string; malformed ones (e.g. '71:71-72') sort last instead of failing."""
        try:
            su, a_ = v.split(':')
            return (int(su), int(a_.split('-')[0]))
        except (ValueError, AttributeError):
            return (999, 0)
    rows.sort(key=lambda r: (key(r['first']), r['id']))
    render = lambda r: (f"[{r['id']}] verses {', '.join(r['verses'])} | {r['claim']} «{r['anchor']}»\n")
    groups, cur, size = [], [], 0
    for r in rows:
        n = len(render(r))
        if cur and size + n > a.chunk_chars:
            groups.append(cur)
            cur, size = [], 0
        cur.append(r)
        size += n
    groups.append(cur)
    (d / 'chunks').mkdir(parents=True)
    plan = []
    for n, g in enumerate(groups, 1):
        verses = sorted({v for r in g for v in r['verses']}, key=key)
        head = '# Verses\n' + '\n'.join(f'- {v}: {digest.quran().get(v, "(not a verse)")}' for v in verses) + '\n\n# Notes\n'
        body, cur_v = [], None
        for r in g:
            if r['first'] != cur_v:
                cur_v = r['first']
                body.append(f'\n## {cur_v}\n')
            body.append(render(r))
        text = head + ''.join(body)
        parts = [text[i:i + PART_CHARS] for i in range(0, len(text), PART_CHARS)]
        for k, p in enumerate(parts):
            tail = f'\n<<part {k} ends; continues in part {k + 1}>>' if k + 1 < len(parts) else '\n<<end of chunk>>'
            (d / 'chunks' / f'c{n:02d}.p{k}.txt').write_text(f'<<chunk {n} part {k} of 0..{len(parts) - 1}>>\n{p}{tail}\n')
        plan.append({'chunk': n, 'row_verses': {r['id']: r['verses'] for r in g}, 'verses': verses, 'chars': len(text), 'parts': len(parts)})
    brief = BRIEF.read_text()
    spawns = []
    for spec in a.models:
        model, effort = spec.split(':')
        tag = digest.tag_of(model, effort)
        (d / 'out' / tag).mkdir(parents=True)
        for c in plan:
            fill = {'AGENT': f"/root/v7t_{a.run}_{tag}_c{c['chunk']:02d}", 'MODEL': model, 'EFFORT': effort, 'RUN': a.run,
                    'TAG': tag, 'N': str(c['chunk']), 'NN': f"{c['chunk']:02d}", 'LAST': str(c['parts'] - 1),
                    'ROWS': str(len(c['row_verses'])), 'NVERSES': str(len(c['verses'])),
                    'TYPES': '\n'.join(f'  - `{k}`: {v}' for k, v in TYPE_GUIDE.items())}
            text = brief
            for k, v in fill.items():
                text = text.replace('{' + k + '}', v)
            f = d / 'spawn' / f"{tag}_c{c['chunk']:02d}.md"
            f.parent.mkdir(exist_ok=True)
            f.write_text(text)
            spawns.append(str(f.relative_to(ROOT)))
    dump(d / 'manifest.json', {'run': a.run, 'ayat': a.ayat, 'from': a.tags_from, 'models': a.models,
                               'chunk_chars': a.chunk_chars, 'already_tagged': skipped, 'chunks': plan, 'spawn': spawns})
    print(f'{len(plan)} chunks, {sum(c["chars"] for c in plan):,} characters, {len(spawns)} spawn files')


def check_chunk(d, tag, c):
    """Problems in one output file: ids missing, unknown or repeated; words not in the row's verses; type not listed."""
    f = d / 'out' / tag / f"c{c['chunk']:02d}.jsonl"
    if not f.exists():
        return [f'{f.name}: no output file'], 0
    problems, seen = [], defaultdict(int)
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            x = json.loads(line)
        except ValueError as e:
            problems.append(f'line {i}: not JSON ({e})')
            continue
        rid = x.get('id')
        if rid not in c['row_verses']:
            problems.append(f'line {i}: id {rid!r} is not in this chunk')
            continue
        seen[rid] += 1
        problems += [f'{rid}: {p}' for p in tag_problems({**x, 'verses': c['row_verses'][rid]})]
    for rid in c['row_verses']:
        if seen[rid] != 1:
            problems.append(f'{rid}: {seen[rid]} lines (expected exactly 1)')
    return problems, sum(seen.values())


def check(a):
    d = run_dir(a.run) / 'retag'
    man = json.loads((d / 'manifest.json').read_text())
    tags = [a.model] if a.model else sorted(p.name for p in (d / 'out').iterdir())
    plan = [c for c in man['chunks'] if a.chunk in (None, c['chunk'])]
    if a.chunk is not None:
        problems, _ = check_chunk(d, tags[0], plan[0])
        print('OK' if not problems else '\n'.join(problems[:60]) + (f'\n... {len(problems) - 60} more' if len(problems) > 60 else ''))
        return
    for tag in tags:
        bad = n = 0
        for c in plan:
            problems, k = check_chunk(d, tag, c)
            n += k
            bad += bool(problems)
            for p in problems:
                print(f"WARNING {tag} c{c['chunk']:02d}: {p}")
        print(f'{tag}: {len(plan)} chunks, {bad} with problems, {n} rows tagged')


def report(a):
    d = run_dir(a.run) / 'retag'
    man = json.loads((d / 'manifest.json').read_text())
    for tag in sorted(p.name for p in (d / 'out').iterdir()):
        usd = reqs = peak = done = 0
        for c in man['chunks']:
            x = digest.usage(d / 'runs', f"/root/v7t_{a.run}_{tag}_c{c['chunk']:02d}")
            if x is None:
                print(f"WARNING {tag} c{c['chunk']:02d}: no run record")
                continue
            done += 1
            usd += x['usd']; reqs += x['requests']; peak = max(peak, x['peak'])
            if not x['completed']:
                print(f"WARNING {tag} c{c['chunk']:02d}: did not complete ({x['via']})")
        print(f"{tag}: {done}/{len(man['chunks'])} runs, ${usd:.2f} API-equivalent, {reqs} requests, peak {peak:,} tokens")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('build'); p.add_argument('run'); p.add_argument('--ayat', nargs='+'); p.add_argument('--page')
    p.add_argument('--ayah'); p.add_argument('--models', nargs='+', required=True)
    p.add_argument('--from', dest='tags_from', nargs='+', default=['luna-max'])
    p.add_argument('--chunk-chars', type=int, default=DEFAULT_CHUNK_CHARS)
    p = sub.add_parser('check'); p.add_argument('run'); p.add_argument('--model'); p.add_argument('--chunk', type=int)
    p = sub.add_parser('report'); p.add_argument('run')
    a = parser.parse_args()
    {'build': build, 'check': check, 'report': report}[a.cmd](a)


if __name__ == '__main__':
    main()
