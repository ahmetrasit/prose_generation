#!/usr/bin/env python3
"""Enrichment v9 lookup over verse maps and their notes (used by the writer and the orchestrator). Read-only.

  q.py index V [V …]                 one line per question of each verse's map: id, question, words, type, positions
  q.py question QID [QID …]          a question in full: positions, reasons, holders (+ prefers, - argues against),
                                     note ids, and the sources named
  q.py notes ID [ID …]               notes in full: source, author, death, speaker, stance, claim, «exact words»
  q.py find REGEX [--verse V …] [--page N]
                                     notes whose claim or exact words match (Arabic matched without vowels), with the
                                     position each note sits in; default all mapped verses; 25 per page
  q.py linked V [--seg LOC …]        segments tied to the verse (its index range, or quoting its words) whose notes do
                                     not name it (about other verses, or none), with those notes; from the linked.py
                                     index (2026-10-10)

Maps: enrichment/v9/work/*/map/out/sol-high/<k>.jsonl (the newest when a verse was mapped twice). Output stays under
24,000 bytes by leaving out whole items (a question, a note, a verse's index, a search hit), never part of one: the
first item is always printed whole, and every item left out is named so it can be asked for alone.
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

V9 = Path(__file__).resolve().parent
sys.path.insert(0, str(V9.parent / 'v7'))
sys.path.insert(1, str(V9))          # linked.py, also when q is imported from elsewhere
import digest  # noqa: E402

TAG = 'sol-high'
MAX_BYTES = 24_000
PAGE = 25
_DROP = {ord(c): None for c in set(digest._ARABIC_DROP) | {'ـ', 'ء'}}   # as digest.normalize_map
_MAP = str.maketrans(digest._ARABIC_MAP)


def key(ayah):
    return ayah.replace(':', '-')


def plain(text):
    """Arabic without vowels and with letter variants folded (as in digest), for matching; the dagger alif after ى is
    dropped, as in digest.normalize_map (عَلَىٰ → على)."""
    return (text or '').translate(_DROP).replace('ىٰ', 'ى').translate(_MAP)


def located(ayah):
    """(map file, rows file) of the newest map of the verse, or None."""
    fs = [f for f in (V9 / 'work').glob(f'*/map/out/{TAG}/{key(ayah)}.jsonl')]
    if not fs:
        return None
    f = max(fs, key=lambda x: x.stat().st_mtime)
    return f, f.parents[2] / 'rows' / f'{key(ayah)}.json'


def stale(ayah):
    """Why the assembled map of a verse cannot be used yet, or None. Stale when a map or update agent output is newer
    than the assembled file (run `map.py check RUN` to assemble), or when an update recorded in the manifest has no
    output yet (its agent has not finished)."""
    loc = located(ayah)
    if not loc:
        return 'no assembled map'
    m = loc[0].parents[2]
    man = json.loads((m / 'manifest.json').read_text())
    p = next((x for x in man['ayat'] if x['ayah'] == ayah), None)
    if p is None:
        return f'not in {m.parent.name} manifest'
    k = key(ayah)
    raws = [m / 'out' / TAG / f'{k}.raw.jsonl'] + [m / 'out' / TAG / f"{k}.u{u['n']}.raw.jsonl"
                                                    for u in p.get('updates', []) if u['tag'] == TAG]
    missing = [r.name for r in raws if not r.exists()]
    if missing:
        return f'{m.parent.name}: no output yet for {", ".join(missing)}'
    if loc[0].stat().st_mtime < max(r.stat().st_mtime for r in raws):
        return f'{m.parent.name}: assembled map older than its outputs (run map.py check {m.parent.name})'
    return None


def load(ayah):
    loc = located(ayah)
    if not loc:
        return None, None
    return [json.loads(l) for l in loc[0].read_text().splitlines() if l.strip()], json.loads(loc[1].read_text())


def translation(ayah):
    """qid -> Turkish rendering of the verse map's questions (newest translation run wins per question):
    {'src': hash of the English it was made from, 'question', 'turns_on', 'positions': {pid: {'position', 'reasons'}}}."""
    out = {}
    for man in sorted((V9 / 'work').glob('*/maptr/manifest.json'), key=lambda f: f.stat().st_mtime):
        m = json.loads(man.read_text())
        src = {q: h for c in m['chunks'] for q, h in c['src'].items() if q.split('/')[0] == ayah}
        if not src:
            continue
        for f in (man.parent / 'out' / m['tag']).glob('c*.jsonl'):
            for line in f.read_text().splitlines():
                if not line.strip():
                    continue
                try:
                    t = json.loads(line)
                except ValueError:
                    continue
                if not isinstance(t, dict) or t.get('id') not in src:
                    continue
                prev = out.get(t['id'])
                if prev and prev['src'] == src[t['id']] and prev['question'] and not (t.get('question') or '').strip():
                    continue               # an empty newer line never replaces a rendering of the same English
                ps = t.get('positions') if isinstance(t.get('positions'), list) else []
                out[t['id']] = {'src': src[t['id']], 'question': t.get('question') or '', 'turns_on': t.get('turns_on') or '',
                                'positions': {p['id']: p for p in ps if isinstance(p, dict) and isinstance(p.get('id'), str)}}
    return out


def mapped():
    return sorted({f.stem for f in (V9 / 'work').glob(f'*/map/out/{TAG}/*.jsonl') if '.' not in f.stem},
                  key=lambda k: tuple(map(int, k.split('-'))))


def out(items, head=()):
    """items: (name, lines) pairs. Whole items are printed while they fit under MAX_BYTES (the first one always, whatever
    its size); the names of the items left out are listed at the end."""
    text = list(head)
    size = sum(len(x.encode()) + 1 for x in text)
    left = []
    for name, lines in items:
        n = sum(len(x.encode()) + 1 for x in lines)
        if left or (size + n > MAX_BYTES and len(text) > len(head)):
            left.append(name)
            continue
        text += lines
        size += n
    if left:
        text.append(f'[output limit: {len(left)} item(s) not shown; ask for them alone: {" ".join(left)}]')
    print('\n'.join(text))


def holders(ids, rows, mark=''):
    by = defaultdict(set)
    for r in ids:
        x = rows.get(r)
        if x:
            by[x['src']].add('' if x['speaker'] == 'author' else x['speaker'])
    return [s + (f"({'، '.join(sorted(w for w in sp if w))})" if any(sp) else '') + mark for s, sp in by.items()]


def cmd_index(a):
    items = []
    for v in a.verses:
        qs, rows = load(v)
        if qs is None:
            items.append((v, [f'# {v}: NO MAP']))
            continue
        lines = [f'# {v}: {len(qs)} questions, {len(rows)} notes']
        for q in qs:
            n = len({r for p in q['positions'] for r in p['rows'] + (p.get('against') or [])})
            lines.append(f"{q['id']} {q['question']} [{' '.join(q['words'])} · {q['type']}] "
                         f"{len(q['positions'])} positions, {n} notes")
        items.append((v, lines))
    out(items)


def cmd_question(a):
    items = []
    for qid in a.qids:
        v = qid.split('/')[0]
        qs, rows = load(v)
        q = next((x for x in qs or [] if x['id'] == qid), None)
        if q is None:
            items.append((qid, [f'# {qid}: not found' + ('' if qs else f' ({v} has no map)')]))
            continue
        lines = []
        lines.append(f"# {q['id']} {q['question']} [{' '.join(q['words'])} · {q['type']}]")
        if q.get('turns_on'):
            lines.append(f"turns on: {q['turns_on']}")
        srcs = set()
        for p in q['positions']:
            pro, con = set(p.get('prefer') or []), p.get('against') or []
            who = holders([r for r in p['rows'] if r not in pro], rows) + holders(sorted(pro), rows, '+') + holders(con, rows, '-')
            srcs |= {rows[r]['src'] for r in p['rows'] + con if r in rows}
            lines.append(f"- {p['id']} {p['position']}")
            if p.get('reasons'):
                lines.append(f"  reasons: {p['reasons']}")
            lines.append(f"  holders ({len(p['rows'])} notes): {'; '.join(who)}")
            lines.append(f"  notes: {' '.join(p['rows'])}" + (f" | against: {' '.join(con)}" if con else ''))
        legend = {}
        for r in rows.values():
            if r['src'] in srcs:
                legend[r['src']] = f"{r['author']}" + (f", d. {r['death']}" if r['death'] else '')
        lines.append('sources: ' + '; '.join(f'{s} = {n}' for s, n in sorted(legend.items())))
        lines.append('')
        items.append((qid, lines))
    out(items)


def cmd_notes(a):
    items, cache = [], {}
    for i in a.ids:
        x = None
        for v in mapped():
            if v not in cache:
                cache[v] = load(v.replace('-', ':'))[1]
            if i in cache[v]:
                x = cache[v][i]
                break
        if x is None:
            items.append((i, [f'[{i}] not found']))
            continue
        items.append((i, [f"[{i}] {x['src']} ({x['author']}" + (f", d. {x['death']}" if x['death'] else '') + f") · "
                          f"{x['speaker']} · {x['stance']} · {about(x)}{x['claim']} «{x.get('anchor') or ''}»"]))
    out(items)


def about(x):
    """'(about 2:106) ' for a note that only names the verse it is filed under (merge.tier1_rows via='mentions')."""
    return f"(about {', '.join(x.get('about') or []) or 'another verse'}) " if x.get('via') == 'mentions' else ''


def cmd_linked(a):
    import linked
    import merge
    f = linked.OUT / f'{key(a.verse)}.json'
    if not f.exists():
        print(f'# {a.verse}: no link index (run python3 -B enrichment/v9/linked.py build --ayat {a.verse}, or for its '
              'whole range)')
        return
    idx = json.loads(f.read_text())
    head = []
    now = linked.stamp()
    if any(idx.get(k) != v for k, v in now.items()):
        head.append(f"NOTE this link index ({idx.get('built_at', 'old format')}) was built from another corpus index, range "
                    'overlay or link code than the current ones; rebuild it with linked.py build')
    segs = idx['segments']
    if a.seg:
        missing = [s for s in a.seg if s not in segs]
        head += [f'# {s}: not linked to {a.verse}' for s in missing]
        segs = {s: segs[s] for s in a.seg if s in segs}
    rows = merge.segment_rows(a.tier1, segs)
    items, named, undigested = [], 0, []
    with digest.connect() as con:
        meta = {i: json.loads(m or '{}') for i, m in con.execute('SELECT id, meta FROM src')}
    for loc, s in segs.items():
        rs = rows.get(loc)
        if rs is None:
            undigested.append(loc)
            continue
        if any(a.verse in digest.verse_list(r.get('verses')) or a.verse in digest.verse_list(r.get('mentions'))
               for r in rs):
            named += 1                       # already reaches the map through tier1_rows
            if a.seg:
                head.append(f'# {loc}: its notes name {a.verse}; they are in the map (q.py find, q.py notes)')
            continue
        m = meta.get(s['src'], {})
        about_vs = sorted({v for r in rs for v in digest.verse_list(r.get('verses'))},
                          key=lambda v: tuple(map(int, v.split(':'))))
        lines = [f"## {loc} · {s['src']} ({m.get('author') or s['src']}" + (f", d. {m['death_ah']}" if m.get('death_ah') else '')
                 + f") · {s['kind']} · tied by {'its index range' if s['by'] == 'index' else 'quoting the verse'}: "
                 f"{s['verses']} · {len(rs)} notes, about {', '.join(about_vs) or 'no verse'}"]
        lines += [f"[{r['id']}] {r['speaker']} · {r['stance']} · {r['claim']} «{r.get('anchor') or ''}»" for r in rs]
        if not rs:
            lines.append('(digested with no notes)')
        items.append((loc, lines))
    head.insert(0, f"# {a.verse}: {len(idx['segments'])} linked segments; {named} have notes naming this verse (in its "
                   f"map already); {len(items)} listed below; {len(undigested)} not digested yet")
    if undigested:
        head.append('not digested yet: ' + ', '.join(undigested))
    sk = idx.get('skipped') or []
    if sk:
        why = defaultdict(int)
        for x in sk:
            why[x['reason'].split(':')[0]] += 1
        head.append(f"{len(sk)} more tied by index but not tier-1 material: "
                    + ', '.join(f'{r} {n}' for r, n in sorted(why.items(), key=lambda x: -x[1])))
    out(items, head)


def cmd_find(a):
    try:
        rx = re.compile(plain(a.regex), re.I)
    except re.error as e:
        print(f'invalid regular expression {a.regex!r}: {e}')
        sys.exit(1)
    verses = [v.replace(':', '-') for v in a.verse] if a.verse else mapped()
    hits, nomap = [], []
    for k in verses:
        v = k.replace('-', ':')
        qs, rows = load(v)
        if qs is None:
            nomap.append(v)
            continue
        where = defaultdict(list)
        for q in qs:
            for p in q['positions']:
                for r in p['rows'] + (p.get('against') or []):
                    where[r].append(p['id'])
        for i, x in rows.items():
            if rx.search(plain(x['claim'])) or rx.search(plain(x.get('anchor') or '')):
                hits.append((v, i, x, where.get(i, [])))
    pages = max(1, -(-len(hits) // PAGE))
    head = [f'{len(hits)} notes match' + (f' on {", ".join(a.verse)}' if a.verse else ' on all mapped verses')
            + f'; page {a.page} of {pages}' + (' (no such page)' if a.page > pages else '')]
    head += [f'# {v}: NO MAP (not searched)' for v in nomap]
    if not a.verse:
        per = defaultdict(int)
        for h in hits:
            per[h[0]] += 1
        head.append('per verse: ' + ', '.join(f'{v} {n}' for v, n in per.items()))
    items = [(i, [f"[{i}] {v} {x['src']} · {x['speaker']} · {x['stance']} · {about(x)}{x['claim']} «{x.get('anchor') or ''}» → {' '.join(w)}"])
             for v, i, x, w in hits[(a.page - 1) * PAGE:a.page * PAGE]]
    out(items, head)   # a hit left out is named: read it with q.py notes


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('index'); p.add_argument('verses', nargs='+')
    p = sub.add_parser('question'); p.add_argument('qids', nargs='+')
    p = sub.add_parser('notes'); p.add_argument('ids', nargs='+')
    p = sub.add_parser('find'); p.add_argument('regex'); p.add_argument('--verse', nargs='+'); p.add_argument('--page', type=int, default=1)
    p = sub.add_parser('linked'); p.add_argument('verse'); p.add_argument('--seg', nargs='+')
    p.add_argument('--tier1', nargs='+', default=['luna-max'], help='tier-1 model tags (default luna-max)')
    a = parser.parse_args()
    {'index': cmd_index, 'question': cmd_question, 'notes': cmd_notes, 'find': cmd_find, 'linked': cmd_linked}[a.cmd](a)


if __name__ == '__main__':
    main()
