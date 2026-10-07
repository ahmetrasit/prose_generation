#!/usr/bin/env python3
"""Enrichment v7 page writer: build the group inputs and spawn files, check the outputs, render the page.
Launches no model.

A writer gets, by script: the frozen page with numbered paragraphs, its own ayah in full (every tier-1 note with its
anchor, plus the ayah's tier-2 views), and for each paragraph the tier-2 views of every verse it cites. It writes
concise Turkish blocks under the paragraphs, citing view ids and note ids, and one ledger row per
(paragraph, cited verse). The page is split into paragraph groups so each group's material fits one context.

  write.py build RUN --ayah 103:1 --page PATH --views sol-high --rows luna-max \\
                     --models claude-opus-5-5:high gpt-6-astra:high [--budget 250000]
  write.py check RUN --model TAG [--group N]       two checks: every (paragraph, verse) answered; quotes verbatim
  write.py render RUN --model TAG                  page with blocks + views/notes files the blocks link to
  write.py report RUN                              costs per group and model

Files: RUN/write/inputs/gNN/{page,own,cited}.pK.txt, RUN/write/<TAG>/gNN/{prompt.md,blocks.jsonl,ledger.jsonl},
RUN/write/spawn/<TAG>_gNN.md (Codex), RUN/write/render/<TAG>/.
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import digest
from digest import PART_CHARS, ROOT, V7, connect, contains, dump, run_dir
import merge

sys.path.insert(0, str(ROOT / 'enrichment/v3'))
import pilot  # noqa: E402  (paragraph splitter shared with v3-v5)
sys.path.insert(0, str(ROOT / '_commentary/v16'))
import agentrun  # noqa: E402  (Claude subagent transcripts and rates)

BRIEF = V7 / 'briefs/write.md'
VERSE = re.compile(r'(?<!\d)(\d{1,3}):(\d{1,3})(?:\s*[–-]\s*(\d{1,3}))?(?![\d:])')
ARABIC_RUN = re.compile(r'[؀-ۿ][؀-ۿً-ْٰ\s]*[؀-ۿ]')
MARK = 'v7-write-run:'


def parts(d, stem, text, label):
    chunks = [text[i:i + PART_CHARS] for i in range(0, len(text), PART_CHARS)] or ['']
    for k, p in enumerate(chunks):
        tail = f'\n<<part {k} ends; continues in part {k + 1}>>' if k + 1 < len(chunks) else f'\n<<end of {label}>>'
        (d / f'{stem}.p{k}.txt').write_text(f'<<{label}, part {k} of 0..{len(chunks) - 1}>>\n{p}{tail}\n')
    return len(chunks)


def page(path, ayah):
    """Frozen text, paragraph spans, numbered text, and the verses each paragraph cites (plus the own ayah)."""
    pilot.BASE = Path(path)
    text, paras = pilot.prose()
    with connect() as con:
        real = {(s, a) for s, a in con.execute("SELECT s,a FROM seg JOIN src ON src.id=seg.src WHERE kind='quran'")}
    own = tuple(map(int, ayah.split(':')))
    cites = {}
    for p, (lo, hi) in paras.items():
        found = {own}
        for m in VERSE.finditer(text[lo:hi]):
            su, st = int(m[1]), int(m[2])
            en = int(m[3]) if m[3] else st
            if 1 <= su <= 114 and st <= en <= st + 40:
                found |= {(su, x) for x in range(st, en + 1)}
        dropped = {v for v in found if v not in real}
        for s, a in sorted(dropped):
            print(f'NOTE: ¶{p}: {s}:{a} is not a verse; not a cited verse')
        cites[p] = sorted(found - dropped, key=lambda v: (v != own, v))
    numbered = text
    for p in sorted(paras, reverse=True):
        lo = paras[p][0]
        numbered = numbered[:lo] + f'[¶{p}] ' + numbered[lo:]
    return text, paras, numbered, {p: [f'{s}:{a}' for s, a in v] for p, v in cites.items()}


def page_verses(path, ayah):
    """The own ayah plus every verse the page's paragraphs cite, sorted (for digest.py and merge.py --page)."""
    cites = page(path, ayah)[3]
    return sorted({v for vs in cites.values() for v in vs}, key=lambda x: tuple(map(int, x.split(':'))))


def own_text(ayah, rows_tag, views_tag):
    rs = merge.tier1_rows(None, rows_tag, ayah)
    rs.sort(key=lambda r: (r['death'] if isinstance(r['death'], int) else 9999, r['src'], r['id']))
    out, cur = [f'# {ayah}: every tier-1 note ({len(rs)}), oldest author first'], None
    for r in rs:
        if r['src'] != cur:
            cur = r['src']
            out.append(f"\n## {r['src']}: {r['author']}" + (f", d. {r['death']} AH" if r['death'] else ''))
        out.append(f"[{r['id']}] {r['speaker']} | {r['stance']} | {r['claim']} «{r.get('anchor', '')}»")
    views, known = merge.load(ayah, views_tag)
    return '\n'.join(out) + '\n\n' + merge.compact(ayah, views, known), {r['id'] for r in rs}


def build(a):
    d = run_dir(a.run) / 'write'
    if d.exists():
        raise SystemExit(f'{d} exists; use a new run')
    text, paras, numbered, cites = page(a.page, a.ayah)
    needed = sorted({v for vs in cites.values() for v in vs}, key=lambda x: tuple(map(int, x.split(':'))))
    material, missing = {}, []
    for v in needed:
        try:
            views, known = merge.load(v, a.views)
        except SystemExit as e:
            missing.append(str(e))
            continue
        material[v] = (merge.compact(v, views, known), {x['vid'] for x in views},
                       {r for x in views for r in x['rows']})
    if missing:
        raise SystemExit('Tier 2 missing for cited verses, nothing built:\n' + '\n'.join(missing))
    groups, cur, size = [], [], 0
    for p in sorted(paras):
        new = sum(len(material[v][0]) for v in cites[p] if v != a.ayah and all(v not in cites[q] for q in cur))
        if cur and size + new > a.budget:
            groups.append(cur)
            cur, size = [], 0
        cur.append(p)
        size += new
    groups.append(cur)
    own, own_rows = own_text(a.ayah, a.rows, a.views)
    plan = []
    for g, ps in enumerate(groups, 1):
        gi = d / 'inputs' / f'g{g:02d}'
        gi.mkdir(parents=True)
        verses = [v for v in dict.fromkeys(v for p in ps for v in cites[p]) if v != a.ayah]
        head = '\n'.join(f"[¶{p}] cites: " + ', '.join(cites[p]) for p in ps)
        body = '\n\n'.join(material[v][0] for v in verses) or '(no verse other than the own ayah)'
        n_page = parts(gi, 'page', numbered, 'page')
        n_own = parts(gi, 'own', own, f'{a.ayah} in full')
        n_cited = parts(gi, 'cited', head + '\n\n' + body, 'cited verses')
        allowed_views = set().union(*(material[v][1] for v in verses + [a.ayah])) if verses else material[a.ayah][1]
        allowed_rows = own_rows.union(*(material[v][2] for v in verses))
        pairs = [[p, v] for p in ps for v in cites[p]]
        dump(gi / 'scope.json', {'paragraphs': ps, 'pairs': pairs, 'views': sorted(allowed_views),
                                 'rows': sorted(allowed_rows)})
        plan.append({'group': g, 'paragraphs': ps, 'pairs': len(pairs), 'verses': len(verses),
                     'chars': len(numbered) + len(own) + len(head) + len(body), 'parts': [n_page, n_own, n_cited]})
    brief = BRIEF.read_text()
    for spec in a.models:
        model, effort = spec.split(':')
        tag = model.split('-')[-1] + '-' + effort
        for c in plan:
            out = d / tag / f"g{c['group']:02d}"
            out.mkdir(parents=True)
            fill = {'AGENT': f"/root/v7w_{a.run}_{tag}_g{c['group']:02d}", 'MODEL': model, 'EFFORT': effort,
                    'RUN': a.run, 'TAG': tag, 'G': str(c['group']), 'GG': f"g{c['group']:02d}", 'GROUPS': str(len(plan)),
                    'AYAH': a.ayah, 'PARAS': ', '.join(f'¶{p}' for p in c['paragraphs']),
                    'LAST_PAGE': str(c['parts'][0] - 1), 'LAST_OWN': str(c['parts'][1] - 1),
                    'LAST_CITED': str(c['parts'][2] - 1), 'MARK': f'{MARK} {out}'}
            text_ = brief
            for k, v in fill.items():
                text_ = text_.replace('{' + k + '}', v)
            (out / 'prompt.md').write_text(text_)
            if not model.startswith('claude'):
                f = d / 'spawn' / f"{tag}_g{c['group']:02d}.md"
                f.parent.mkdir(exist_ok=True)
                f.write_text(text_)
            else:
                (out / 'spawn.md').write_text(
                    f'{MARK} {out}\n\nRead {out}/prompt.md with the Read tool and follow it exactly. Run only the '
                    f'commands it lists, each alone and exactly as written. Write only inside {out}. When your two '
                    'output files are complete and the check prints OK, reply with one line: written.\n')
    dump(d / 'manifest.json', {'ayah': a.ayah, 'page': str(a.page), 'views': a.views, 'rows': a.rows,
                               'models': a.models, 'budget': a.budget, 'cites': cites, 'groups': plan})
    print(f'{a.ayah}: {len(paras)} paragraphs, {len(needed)} cited verses (own included), '
          f'{sum(len(v) for v in cites.values())} (paragraph, verse) pairs, {len(plan)} group(s)')
    for c in plan:
        print(f"  g{c['group']:02d}: ¶{c['paragraphs'][0]}–¶{c['paragraphs'][-1]}, {c['pairs']} pairs, "
              f"{c['verses']} cited verses, {c['chars']:,} characters of input")


def check_group(d, tag, g):
    scope = json.loads((d / 'inputs' / f'g{g:02d}' / 'scope.json').read_text())
    out = d / tag / f'g{g:02d}'
    problems = []
    for name in ('blocks.jsonl', 'ledger.jsonl'):
        if not (out / name).exists():
            problems.append(f'{name}: no file')
    if problems:
        return problems, [], []
    blocks, ledger = [], []
    for name, into in (('blocks.jsonl', blocks), ('ledger.jsonl', ledger)):
        for i, line in enumerate((out / name).read_text().splitlines(), 1):
            if line.strip():
                try:
                    into.append(json.loads(line))
                except ValueError as e:
                    problems.append(f'{name} line {i}: not JSON ({e})')
    ids = {b.get('id') for b in blocks}
    views, rows = set(scope['views']), set(scope['rows'])
    behind = defaultdict(set)  # view id -> its row ids, for the quote check
    for v in {x.split('/v')[0] for x in views}:
        for x in merge.load(v, json.loads((d / 'manifest.json').read_text())['views'])[0]:
            behind[x['vid']] = set(x['rows'])
    anchors = {}
    for b in blocks:
        bid = b.get('id', '?')
        for k in ('id', 'p', 'verse', 'topic', 'text'):
            if not b.get(k):
                problems.append(f'block {bid}: missing {k}')
        if not (b.get('views') or b.get('rows')):
            problems.append(f'block {bid}: cites no view and no note')
        for v in b.get('views') or []:
            if v not in views:
                problems.append(f'block {bid}: view {v} was not in your material')
        for r in b.get('rows') or []:
            if r not in rows:
                problems.append(f'block {bid}: note {r} was not in your material')
        for p in b.get('p') or []:
            if p not in scope['paragraphs']:
                problems.append(f'block {bid}: paragraph {p} is not in this group')
        cited = set(b.get('rows') or [])
        for v in b.get('views') or []:
            cited |= behind[v]
        quotes = [q.strip() for q in ARABIC_RUN.findall(b.get('text', '')) if len(q.split()) >= 3]
        if quotes:
            if not anchors:
                for f in sorted((V7 / 'work').glob(f"*/out/{json.loads((d / 'manifest.json').read_text())['rows']}/c*.jsonl")):
                    for line in f.read_text().splitlines():
                        if line.strip():
                            x = json.loads(line)
                            for n, r in enumerate(x['rows'], 1):
                                anchors.setdefault(f"{x['loc']}/r{n}", r.get('anchor', ''))
            for q in quotes:
                if not any(contains(anchors.get(r, ''), q, minimum=1) for r in cited):
                    problems.append(f'block {bid}: Arabic not found in the anchors of the notes it cites: {q[:80]}')
    want = {(p, v) for p, v in scope['pairs']}
    seen = defaultdict(int)
    for r in ledger:
        pair = (r.get('p'), r.get('verse'))
        if pair not in want:
            problems.append(f'ledger: ({pair[0]}, {pair[1]}) is not a pair of this group')
            continue
        seen[pair] += 1
        if r.get('status') == 'written':
            if not r.get('blocks') or any(x not in ids for x in r['blocks']):
                problems.append(f'ledger ¶{pair[0]} {pair[1]}: written, but its blocks are missing or unknown')
        elif r.get('status') == 'no_match':
            if not (r.get('reason') or '').strip():
                problems.append(f'ledger ¶{pair[0]} {pair[1]}: no_match without a reason')
        else:
            problems.append(f'ledger ¶{pair[0]} {pair[1]}: status must be written or no_match')
    for pair in sorted(want):
        if seen[pair] != 1:
            problems.append(f'ledger ¶{pair[0]} {pair[1]}: {seen[pair]} rows (expected exactly 1)')
    return problems, blocks, ledger


def check(a):
    d = run_dir(a.run) / 'write'
    man = json.loads((d / 'manifest.json').read_text())
    groups = [a.group] if a.group else [c['group'] for c in man['groups']]
    for g in groups:
        problems, blocks, ledger = check_group(d, a.model, g)
        if a.group:  # the agent's own check
            print('OK' if not problems else '\n'.join(problems[:60]) + (f'\n... {len(problems) - 60} more' if len(problems) > 60 else ''))
            return
        for p in problems:
            print(f'WARNING {a.model} g{g:02d}: {p}')
        written = sum(1 for r in ledger if r.get('status') == 'written')
        words = sum(len(b.get('text', '').split()) for b in blocks)
        print(f'{a.model} g{g:02d}: {len(blocks)} blocks, {words} words, {written} pairs written, '
              f'{len(ledger) - written} no_match, {len(problems)} problems')


def render(a):
    """The page with every block after its paragraph (after the paragraph's augment blocks), each block linking to
    its views; views/<ayah>.md lists each view with its notes (claim, anchor, locator). Strip check: removing the
    blocks gives the frozen page back byte for byte."""
    d = run_dir(a.run) / 'write'
    man = json.loads((d / 'manifest.json').read_text())
    pilot.BASE = Path(man['page'])
    text, paras = pilot.prose()
    out_dir = d / 'render' / a.model
    (out_dir / 'views').mkdir(parents=True, exist_ok=True)
    blocks, used = defaultdict(list), set()
    for c in man['groups']:
        problems, bs, _ = check_group(d, a.model, c['group'])
        if problems:
            raise SystemExit(f"g{c['group']:02d} has {len(problems)} problems; run check first")
        for b in bs:
            blocks[min(b['p'])].append(b)
            used |= {v.split('/v')[0] for v in b.get('views') or []}
            if b.get('rows'):
                used.add(man['ayah'])
    notes = {}
    for f in sorted((V7 / 'work').glob(f"*/out/{man['rows']}/c*.jsonl")):
        for line in f.read_text().splitlines():
            if line.strip():
                x = json.loads(line)
                for n, r in enumerate(x['rows'], 1):
                    notes.setdefault(f"{x['loc']}/r{n}", {**r, 'loc': x['loc']})
    counts = {}
    for v in sorted(used):
        views, known = merge.load(v, man['views'])
        lines = [f'# {v}: {len(views)} views']
        for x in views:
            lines.append(f"\n## <a id=\"{x['vid'].replace(':', '-').replace('/', '-')}\"></a>{x['vid']} · {x['topic']}\n\n{x['view']}"
                         + (f"\n\n_{x['note']}_" if x.get('note') else ''))
            for r in x['rows']:
                k, nt = known.get(r, {}), notes.get(r, {})
                lines.append(f"- {k.get('src')} ({k.get('author')}) · {k.get('speaker')} · {k.get('stance')}: {k.get('claim')} "
                             f"«{nt.get('anchor', '')}» `{nt.get('loc', '')}`")
            counts[x['vid']] = (len(x['rows']), len({known.get(r, {}).get('src') for r in x['rows']}))
        (out_dir / 'views' / f"{merge.key(v)}.md").write_text('\n'.join(lines) + '\n')
    pieces, last = [], 0
    for p in sorted(paras):
        lo, hi = paras[p]
        pieces.append(text[last:hi])
        last = hi
        for b in blocks.get(p, []):
            links = ' · '.join(f"[{v.split('/')[1]}](views/{merge.key(v.split('/v')[0])}.md#{v.replace(':', '-').replace('/', '-')})"
                               for v in b.get('views') or [])
            n_rows = sum(counts.get(v, (0, 0))[0] for v in b.get('views') or []) + len(b.get('rows') or [])
            pieces.append(f"\n\n<!-- v7:enrich block={b['id']} p={','.join(map(str, b['p']))} verse={b['verse']} -->\n"
                          f"> **{b['topic']}** — {b['text']}\n>\n> _Ayrıntı: {links or 'notlar'} · {n_rows} not_\n"
                          f"<!-- /v7:enrich -->")
    pieces.append(text[last:])
    page_out = ''.join(pieces)
    stripped = re.sub(r'\n\n<!-- v7:enrich [^>]*-->\n.*?<!-- /v7:enrich -->', '', page_out, flags=re.S)
    if stripped != text:
        raise SystemExit('strip check failed: removing the blocks does not give the frozen page back')
    stem = Path(man['page']).name.replace('.reading.tr.md', '')
    (out_dir / f'{stem}.enriched.tr.md').write_text(page_out)
    print(f"{out_dir / f'{stem}.enriched.tr.md'}: {sum(len(v) for v in blocks.values())} blocks, {len(used)} view files; strip check ok")


def report(a):
    d = run_dir(a.run) / 'write'
    man = json.loads((d / 'manifest.json').read_text())
    for spec in man['models']:
        model, effort = spec.split(':')
        tag = model.split('-')[-1] + '-' + effort
        total = 0.0
        for c in man['groups']:
            out = d / tag / f"g{c['group']:02d}"
            if model.startswith('claude'):
                hits = [f for f in agentrun.PROJECTS.glob('*/*/subagents/agent-*.jsonl')
                        if f'{MARK} {out}' in f.read_text(encoding='utf-8', errors='ignore')[:20000]]
                if not hits:
                    print(f"WARNING {tag} g{c['group']:02d}: no transcript found")
                    continue
                p = agentrun.parse(hits[-1])
                usd, note = p['cost_usd'] or 0, f"stop {p.get('stop_reason')}"
            else:
                x = digest.usage(d / 'runs', f"/root/v7w_{a.run}_{tag}_g{c['group']:02d}")
                if x is None:
                    print(f"WARNING {tag} g{c['group']:02d}: no run.json and no native session")
                    continue
                usd, note = x['usd'], f"{x['requests']} requests, peak {x['peak']}, {x['via']}"
            total += usd
            print(f"{tag} g{c['group']:02d}: ${usd:.2f} ({note})")
        print(f'{tag}: ${total:.2f} total')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('build'); p.add_argument('run'); p.add_argument('--ayah', required=True)
    p.add_argument('--page', required=True); p.add_argument('--views', required=True); p.add_argument('--rows', required=True)
    p.add_argument('--models', nargs='+', required=True); p.add_argument('--budget', type=int, default=250_000)
    p = sub.add_parser('check'); p.add_argument('run'); p.add_argument('--model', required=True); p.add_argument('--group', type=int)
    p = sub.add_parser('render'); p.add_argument('run'); p.add_argument('--model', required=True)
    p = sub.add_parser('report'); p.add_argument('run')
    a = parser.parse_args()
    {'build': build, 'check': check, 'render': render, 'report': report}[a.cmd](a)


if __name__ == '__main__':
    main()
