#!/usr/bin/env python3
"""Enrichment v8 test: one query script over every tier-1 note, for a gatherer (Luna) and a writer (Opus).
The agent decides every query; the script only answers and logs each query with the ids it returned.

  q.py build RUN --ayah 95:1 --page PATH          index.sqlite (all tier-1 notes), page and focus-notes parts, scope
  q.py RUN ARM catalog V [V ...]                  per verse: notes, sources, notes per verse word, links
  q.py RUN ARM notes V [--word W] [--grep RE] [--source SRC] [--page N]
  q.py RUN ARM find RE [--verse V] [--page N]     regex over claims and exact words (Arabic normalised)
  q.py RUN ARM links A B                          notes on A that name B, and on B that name A
  q.py RUN ARM note ID [ID ...]                   full notes with locator and source
  q.py RUN ARM packet                             the gatherer's packet, expanded (opus-packet arm)
  q.py RUN ARM check-packet | check-write         the two output checks
  q.py report RUN                                 queries, recall of the packet against the writers, costs
"""
import json, re, sqlite3, sys, glob, time
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V7 = ROOT / 'enrichment/v7'
CORPUS = ROOT / 'enrichment/corpus/corpus.sqlite'
PART = 10_000
PAGE_ROWS = 25
DIAC = re.compile(r'[ً-ْٰـ۟-ۭٓ-ٟ]')
ARABIC_RUN = re.compile(r'[؀-ۿ][؀-ۿً-ْٰ\s]*[؀-ۿ]')
STOP = set('و ف ب ل ك من في على الي ان لا ما الا اذا اذ ثم او لم لن قد هو هي هم انا يا الذي الذين التي ذلك هذا تلك كان كانوا له لهم لكم لها بها به منه منها عليه عليهم فيه فيها الله يوم كل'.split())


def norm(s):
    s = DIAC.sub('', s or '')
    for a, b in (('ٱ', 'ا'), ('أ', 'ا'), ('إ', 'ا'), ('آ', 'ا'), ('ى', 'ي'), ('ة', 'ه'), ('ۥ', ''), ('ۦ', ''), ('ؤ', 'و'), ('ئ', 'ي')):
        s = s.replace(a, b)
    return s


def stem(w):
    w = norm(w).strip('،.؛:')
    for p in ('وال', 'فال', 'بال', 'كال', 'لل', 'ال'):
        if w.startswith(p) and len(w) - len(p) >= 3:
            return w[len(p):]
    if w[:1] in 'وف' and len(w) >= 4:
        w = w[1:]
    return w


def skel(s):
    """Quranic spelling drops some alifs (الإنسان written الانسن): compare without alif."""
    return s.replace('ا', '')


def parts(d, stem_, text, label):
    chunks = [text[i:i + PART] for i in range(0, len(text), PART)] or ['']
    for k, p in enumerate(chunks):
        tail = f'\n<<part {k} ends; continues in part {k + 1}>>' if k + 1 < len(chunks) else f'\n<<end of {label}>>'
        (d / f'{stem_}.p{k}.txt').write_text(f'<<{label}, part {k} of 0..{len(chunks) - 1}>>\n{p}{tail}\n')
    return len(chunks)


def line(r):
    who = r['src'] + (f" d.{r['death']}" if r['death'] else '')
    sp = '' if r['speaker'] == 'author' else f" · {r['speaker']}"
    return f"[{r['id']}] {who}{sp} · {r['stance']} · {r['claim']} «{r['anchor']}»"


# ---------------------------------------------------------------- build
def build(run, ayah, page):
    sys.path.insert(0, str(V7))
    import write  # noqa: paragraph splitter and cited verses
    d = ROOT / 'enrichment/v8/work' / run
    if d.exists():
        raise SystemExit(f'{d} exists; use a new run')
    (d / 'inputs').mkdir(parents=True)
    corpus = sqlite3.connect(CORPUS)
    meta = {i: json.loads(m or '{}') for i, m in corpus.execute('SELECT id, meta FROM src')}
    files = sorted(glob.glob(str(V7 / 'work/*/out/*/c*.jsonl')), key=lambda f: ('/luna-max/' not in f, f))
    seen, rows = set(), []
    for f in files:
        for ln in open(f):
            if not ln.strip():
                continue
            try:
                x = json.loads(ln)
            except ValueError:
                print(f'WARNING {f}: a line is not JSON; skipped')
                continue
            if x['loc'] in seen:
                continue
            seen.add(x['loc'])
            r0 = corpus.execute('SELECT src FROM seg WHERE seg=?', (x['loc'],)).fetchone()
            src = r0[0] if r0 else x['loc'].split(':')[0]
            m = meta.get(src, {})
            for n, r in enumerate(x['rows'], 1):
                for v in r.get('verses') or []:
                    rows.append((f"{x['loc']}/r{n}", v, src, m.get('author') or src, m.get('death_ah'), r.get('speaker', ''),
                                 r.get('stance', ''), r.get('claim', ''), r.get('anchor', ''), norm(r.get('anchor', '')),
                                 norm(r.get('claim', '')), json.dumps(r.get('mentions') or [])))
    # edition rule: drop a short edition's notes on a verse where its FULL edition has notes on that verse
    full = {(v, s[:-5]) for _, v, s, *rest in rows if s.endswith('-FULL')}
    kept = [r for r in rows if (r[1], r[2]) not in full]
    print(f'index: {len(seen)} segments, {len(rows)} note-verse pairs, {len(rows) - len(kept)} dropped by the edition rule')
    db = sqlite3.connect(d / 'index.sqlite')
    db.execute('CREATE TABLE notes(id, verse, src, author, death, speaker, stance, claim, anchor, an, cn, mentions)')
    db.executemany('INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', kept)
    db.execute('CREATE INDEX nv ON notes(verse)'); db.execute('CREATE INDEX ni ON notes(id)')
    qt = {f'{s}:{a}': t for s, a, t in corpus.execute("SELECT s, a, text FROM seg WHERE src='QURAN' AND a IS NOT NULL")}
    db.execute('CREATE TABLE quran(verse PRIMARY KEY, text)')
    db.executemany('INSERT INTO quran VALUES (?,?)', qt.items())
    db.commit()
    text, paras, numbered, cites = write.page(page, ayah)
    n_page = parts(d / 'inputs', 'page', numbered, f'{ayah} reading, paragraphs numbered')
    db.row_factory = sqlite3.Row
    own = [dict(r) for r in db.execute('SELECT * FROM notes WHERE verse=?', (ayah,))]
    own.sort(key=lambda r: (r['death'] if isinstance(r['death'], int) else 9999, r['src'], r['id']))
    out, cur = [f'# {ayah}: every tier-1 note ({len(own)}), oldest author first'], None
    for r in own:
        if r['src'] != cur:
            cur = r['src']
            out.append(f"\n## {r['src']}: {r['author']}" + (f", d. {r['death']} AH" if r['death'] else ''))
        out.append(line(r))
    n_focus = parts(d / 'inputs', 'focus', '\n'.join(out), f'{ayah} notes')
    pairs = [[p, v] for p in sorted(cites) for v in cites[p]]
    json.dump({'ayah': ayah, 'page': str(page), 'paragraphs': sorted(paras), 'cites': cites, 'pairs': pairs,
               'parts': {'page': n_page, 'focus': n_focus}, 'own_notes': len(own)}, open(d / 'scope.json', 'w'), ensure_ascii=False, indent=1)
    print(f'{ayah}: {len(paras)} paragraphs, {len(pairs)} (paragraph, verse) pairs, {len({v for _, v in pairs})} verses incl. own; '
          f'page {len(numbered):,} chars in {n_page} parts; focus notes {len(own)} in {n_focus} parts')


# ---------------------------------------------------------------- queries
class Q:
    def __init__(self, run, arm):
        self.d = ROOT / 'enrichment/v8/work' / run
        self.arm = arm
        self.db = sqlite3.connect(self.d / 'index.sqlite')
        self.db.row_factory = sqlite3.Row
        self.scope = json.loads((self.d / 'scope.json').read_text())

    def log(self, cmd, ids):
        (self.d / 'log').mkdir(exist_ok=True)
        with open(self.d / 'log' / f'{self.arm}.jsonl', 'a') as f:
            f.write(json.dumps({'t': time.strftime('%H:%M:%S'), 'cmd': cmd, 'ids': ids}, ensure_ascii=False) + '\n')

    def rows(self, verse):
        return [dict(r) for r in self.db.execute('SELECT * FROM notes WHERE verse=? ORDER BY death IS NULL, death, src, id', (verse,))]

    def show(self, rs, page, header):
        total = len(rs)
        start = (page - 1) * PAGE_ROWS
        chunk = rs[start:start + PAGE_ROWS]
        print(header + f' — showing {start + 1 if chunk else 0}–{start + len(chunk)} of {total}'
              + (f'; more: --page {page + 1}' if start + len(chunk) < total else ''))
        for r in chunk:
            print(line(r))
        return [r['id'] for r in chunk]

    def catalog(self, verses):
        ids = []
        for v in verses:
            rs = self.rows(v)
            q = self.db.execute('SELECT text FROM quran WHERE verse=?', (v,)).fetchone()
            print(f"\n## {v}: {len(rs)} notes from {len({r['src'] for r in rs})} sources")
            if q:
                print(f'verse: {q[0]}')
                words = [w for w in q[0].split() if stem(w) not in STOP and len(stem(w)) >= 3]
                counts = []
                for w in words:
                    s = skel(stem(w))
                    counts.append(f'{w} {sum(1 for r in rs if s in skel(r["an"]) or s in skel(r["cn"]))}')
                print('notes whose Arabic carries each word (English-only notes not counted): ' + ' · '.join(counts))
            st = Counter(r['stance'] for r in rs)
            print('stances: ' + ', '.join(f'{k} {n}' for k, n in st.most_common()))
            ment = Counter(m for r in rs for m in json.loads(r['mentions']) if m != v)
            print('verses these notes name most: ' + ', '.join(f'{k} ({n})' for k, n in ment.most_common(12)))
            own = self.scope['ayah'].split(':')[0]
            back = [r for r in self.db.execute('SELECT id, verse, mentions FROM notes WHERE verse<>? AND mentions LIKE ?', (v, f'%"{v}"%'))]
            print(f'notes on other verses that name {v}: {len(back)}' + (f" (from surah {own}: {sum(1 for r in back if r['verse'].startswith(own + ':'))})" if back else ''))
        self.log(f'catalog {" ".join(verses)}', ids)

    def notes(self, v, word=None, grep=None, source=None, page=1):
        rs = self.rows(v)
        if word:
            s = skel(stem(word))
            rs = [r for r in rs if s in skel(r['an']) or s in skel(r['cn'])]
        if grep:
            rx = re.compile(norm(grep), re.I)
            rs = [r for r in rs if rx.search(r['an']) or rx.search(r['cn'])]
        if source:
            rs = [r for r in rs if r['src'] == source]
        ids = self.show(rs, page, f'# notes on {v}' + (f' word {word}' if word else '') + (f' grep {grep}' if grep else '') + (f' source {source}' if source else ''))
        self.log(f'notes {v} word={word} grep={grep} source={source} page={page}', ids)

    def find(self, rx_, verse=None, page=1):
        rx = re.compile(norm(rx_), re.I)
        q = 'SELECT * FROM notes' + (' WHERE verse=?' if verse else '')
        rs = [dict(r) for r in self.db.execute(q, (verse,) if verse else ()) if rx.search(r['an']) or rx.search(r['cn'])]
        ids = []
        if not verse:
            c = Counter(r['verse'] for r in rs)
            print(f'# find {rx_}: {len(rs)} notes on {len(c)} verses. By verse: ' + ', '.join(f'{k} {n}' for k, n in c.most_common(40))
                  + (' …' if len(c) > 40 else ''))
            if len(rs) <= PAGE_ROWS:
                ids = self.show(rs, 1, '# notes')
            else:
                print('narrow with --verse V to list them')
        else:
            rs.sort(key=lambda r: (r['death'] if isinstance(r['death'], int) else 9999, r['src']))
            ids = self.show(rs, page, f'# find {rx_} on {verse}')
        self.log(f'find {rx_} verse={verse} page={page}', ids)

    def links(self, a, b):
        rs = [dict(r) for r in self.db.execute('SELECT * FROM notes WHERE (verse=? AND mentions LIKE ?) OR (verse=? AND mentions LIKE ?)',
                                               (a, f'%"{b}"%', b, f'%"{a}"%'))]
        ids = self.show(rs, 1, f'# notes on {a} naming {b}, and on {b} naming {a}')
        self.log(f'links {a} {b}', ids)

    def note(self, ids):
        out = []
        for i in ids:
            rs = [dict(r) for r in self.db.execute('SELECT * FROM notes WHERE id=?', (i,))]
            if not rs:
                print(f'[{i}] not found')
                continue
            r = rs[0]
            print(line(r) + f"\n    verses: {', '.join(x['verse'] for x in rs)} · author: {r['author']} · locator: {i.rsplit('/', 1)[0]}")
            out.append(i)
        self.log(f'note {" ".join(ids)}', out)

    # ---- packet
    def packet_lines(self):
        f = self.d / 'gather' / 'packet.jsonl'
        if not f.exists():
            return None, [f'{f.relative_to(ROOT)}: no file']
        out, problems = [], []
        for i, ln in enumerate(f.read_text().splitlines(), 1):
            if ln.strip():
                try:
                    out.append(json.loads(ln))
                except ValueError as e:
                    problems.append(f'line {i}: not JSON ({e})')
        return out, problems

    def check_packet(self):
        lines, problems = self.packet_lines()
        if lines is not None:
            seen = Counter(x.get('p') for x in lines)
            for p in self.scope['paragraphs']:
                if seen[p] != 1:
                    problems.append(f'paragraph {p}: {seen[p]} lines (expected exactly 1)')
            for x in lines:
                for it in x.get('items') or []:
                    if not self.db.execute('SELECT 1 FROM notes WHERE id=?', (it.get('id'),)).fetchone():
                        problems.append(f"paragraph {x.get('p')}: unknown note id {it.get('id')}")
                if not x.get('items') and not (x.get('searched') or '').strip():
                    problems.append(f"paragraph {x.get('p')}: no items and no 'searched' line")
        print('OK' if not problems else '\n'.join(problems[:60]))

    def packet(self):
        lines, problems = self.packet_lines()
        if problems:
            raise SystemExit('\n'.join(problems))
        ids = []
        print('# Gatherer packet. The notes are evidence; the gatherer\'s "why" lines are only its pointers, never evidence.')
        for x in sorted(lines, key=lambda x: x['p']):
            print(f"\n## ¶{x['p']}: {len(x.get('items') or [])} notes" + (f"  (gatherer searched: {x['searched']})" if x.get('searched') else ''))
            for it in x.get('items') or []:
                r = dict(self.db.execute('SELECT * FROM notes WHERE id=?', (it['id'],)).fetchone())
                focus = self.db.execute('SELECT 1 FROM notes WHERE id=? AND verse=?', (it['id'], self.scope['ayah'])).fetchone()
                shown = f"[{it['id']}] (focus note, text in your focus notes)" if focus else line(r)
                print(shown + (f"   — why: {it.get('why')}" if it.get('why') else ''))
                ids.append(it['id'])
        self.log('packet', ids)

    def packet_parts(self):
        """Compact packet for the writer: per paragraph the note ids (no gatherer reasons), then every non-focus note
        once, in full. Formatting only: no note is dropped."""
        lines, problems = self.packet_lines()
        if problems:
            raise SystemExit('\n'.join(problems))
        ayah = self.scope['ayah']
        focus = {r[0] for r in self.db.execute('SELECT id FROM notes WHERE verse=?', (ayah,))}
        out = ['# Gatherer packet. Part A: per paragraph, the notes the gatherer judged relevant (ids). '
               'Part B: every note in part A that is not a focus note, once, in full (focus notes are in your focus notes).', '', '## Part A']
        other = []
        for x in sorted(lines, key=lambda x: x['p']):
            ids = [it['id'] for it in x.get('items') or []]
            f = [i for i in ids if i in focus]
            o = [i for i in ids if i not in focus]
            other += [i for i in o if i not in other]
            out.append(f"¶{x['p']}: focus {len(f)}: {' '.join(f) or '-'}")
            out.append(f"¶{x['p']}: other {len(o)}: {' '.join(o) or '-'}")
        out += ['', '## Part B']
        rows = [dict(self.db.execute('SELECT * FROM notes WHERE id=?', (i,)).fetchone()) for i in other]
        rows.sort(key=lambda r: (tuple(map(int, r['verse'].split(':'))), r['death'] if isinstance(r['death'], int) else 9999, r['src']))
        cur = None
        for r in rows:
            if r['verse'] != cur:
                cur = r['verse']
                out.append(f'\n### notes filed under {cur}')
            out.append(line(r))
        text = '\n'.join(out)
        n = parts(self.d / 'gather', 'packet', text, 'gatherer packet')
        print(f'packet parts: {n}, {len(text):,} chars, {len(other)} non-focus notes in full')

    def check_write(self):
        out = self.d / 'write' / self.arm
        problems = []
        blocks, ledger = [], []
        for name, into in (('blocks.jsonl', blocks), ('ledger.jsonl', ledger)):
            f = out / name
            if not f.exists():
                problems.append(f'{name}: no file')
                continue
            for i, ln in enumerate(f.read_text().splitlines(), 1):
                if ln.strip():
                    try:
                        into.append(json.loads(ln))
                    except ValueError as e:
                        problems.append(f'{name} line {i}: not JSON ({e})')
        bids = {b.get('id') for b in blocks}
        for b in blocks:
            bid = b.get('id', '?')
            for k in ('id', 'p', 'topic', 'text', 'notes'):
                if not b.get(k):
                    problems.append(f'block {bid}: missing {k}')
            anchors = []
            for n in b.get('notes') or []:
                r = self.db.execute('SELECT an FROM notes WHERE id=?', (n,)).fetchone()
                if not r:
                    problems.append(f'block {bid}: unknown note id {n}')
                else:
                    anchors.append(r[0])
            for qte in ARABIC_RUN.findall(b.get('text', '')):
                if len(qte.split()) >= 3 and not any(norm(qte).strip() in a for a in anchors):
                    problems.append(f'block {bid}: Arabic not in the exact words of the notes it cites: {qte[:60]}')
        want = {(p, v) for p, v in self.scope['pairs']}
        seen = Counter()
        for r in ledger:
            pair = (r.get('p'), r.get('verse'))
            if pair not in want:
                problems.append(f'ledger: ({pair[0]}, {pair[1]}) is not a pair of this page')
                continue
            seen[pair] += 1
            if r.get('status') == 'written':
                if not r.get('blocks') or any(x not in bids for x in r['blocks']):
                    problems.append(f'ledger ¶{pair[0]} {pair[1]}: written, but its blocks are missing or unknown')
            elif r.get('status') == 'no_match':
                if not (r.get('reason') or '').strip():
                    problems.append(f'ledger ¶{pair[0]} {pair[1]}: no_match without a reason')
            else:
                problems.append(f'ledger ¶{pair[0]} {pair[1]}: status must be written or no_match')
        for pair in sorted(want):
            if seen[pair] != 1:
                problems.append(f'ledger ¶{pair[0]} {pair[1]}: {seen[pair]} rows (expected exactly 1)')
        print('OK' if not problems else '\n'.join(problems[:60]))


def report(run):
    sys.path.insert(0, str(ROOT / '_commentary/v16'))
    import agentrun
    q = Q(run, 'report')
    d = q.d
    ayah = q.scope['ayah']
    focus = {r[0] for r in q.db.execute('SELECT id FROM notes WHERE verse=?', (ayah,))}
    print(f'# {run}: {ayah}, {len(q.scope["paragraphs"])} paragraphs, {len(q.scope["pairs"])} (paragraph, verse) pairs\n')
    # Luna
    rj = list((d / 'runs').glob('*/run.json'))
    if rj:
        x = json.loads(rj[0].read_text())
        print(f"luna gatherer: ${x.get('usd_equivalent', 0):.3f} API-equivalent (actual $0), {x.get('requests')} requests, "
              f"peak {x.get('max_request_input_tokens')} tokens, {x.get('commands')} commands, completed {x.get('turn_completed')}")
    lines, _ = q.packet_lines()
    packet = defaultdict(set)
    for x in lines or []:
        for it in x.get('items') or []:
            packet[x['p']].add(it['id'])
    allp = set().union(*packet.values()) if packet else set()
    if lines:
        chars = 0
        for i in allp:
            if i not in focus:
                r = q.db.execute('SELECT * FROM notes WHERE id=?', (i,)).fetchone()
                chars += len(line(dict(r)))
        print(f"packet: {sum(len(v) for v in packet.values())} items, {len(allp)} distinct notes "
              f"({len(allp & focus)} focus by id, {len(allp - focus)} other in full, {chars:,} chars of other notes); "
              'per paragraph: ' + ', '.join(f'¶{p} {len(v)}' for p, v in sorted(packet.items())))
    # writers
    for arm in ('opus-alone', 'opus-packet'):
        out = d / 'write' / arm
        mark = f'v8-test-run: enrichment/v8/work/{run}/write/{arm}'
        hits = [f for f in agentrun.PROJECTS.glob('*/*/subagents/agent-*.jsonl')
                if mark in f.read_text(encoding='utf-8', errors='ignore')[:20000]]
        cost = ''
        if hits:
            t = agentrun.parse(sorted(hits, key=lambda f: f.stat().st_mtime)[-1])
            u = t.get('usage_tokens') or {}
            cost = (f"${t.get('cost_usd') or 0:.2f} (with estimated full output ${t.get('cost_usd_est') or 0:.2f}), "
                    f"messages {t.get('num_messages')}, peak context {t.get('max_context'):,}, "
                    f"cache write {u.get('cache_5m', 0) + u.get('cache_1h', 0):,}, cache read {u.get('cache_read', 0):,}, "
                    f"output ≥{u.get('output', 0):,} (est. {t.get('output_tokens_est') or 0:,}), completed {t.get('completed')}")
        logf = d / 'log' / f'{arm}.jsonl'
        log = [json.loads(x) for x in logf.read_text().splitlines()] if logf.exists() else []
        searched = set(i for e in log for i in e['ids'])
        blocks = [json.loads(x) for x in (out / 'blocks.jsonl').read_text().splitlines() if x.strip()] if (out / 'blocks.jsonl').exists() else []
        ledger = [json.loads(x) for x in (out / 'ledger.jsonl').read_text().splitlines() if x.strip()] if (out / 'ledger.jsonl').exists() else []
        cited = [n for b in blocks for n in b.get('notes') or []]
        cset = set(cited)
        words = sum(len(b.get('text', '').split()) for b in blocks)
        reused = sum(1 for n, c in Counter(cited).items() if c > 1)
        print(f"\n{arm}: {cost or 'no transcript found'}")
        print(f"  queries {len(log)} ({', '.join(f'{k} {v}' for k, v in Counter(e['cmd'].split()[0] for e in log).most_common())}); "
              f"blocks {len(blocks)}, {words} words; ledger written {sum(1 for r in ledger if r.get('status') == 'written')}, "
              f"no_match {sum(1 for r in ledger if r.get('status') == 'no_match')}")
        print(f"  notes cited {len(cset)} distinct ({len(cset & focus)} focus, {len(cset - focus)} other); notes cited in more than one block: {reused}")
        if allp:
            other = cset - focus
            print(f"  of the non-focus notes it cites, in the packet: {len(other & allp)}/{len(other)}; "
                  f"of its focus notes, in the packet: {len(cset & focus & allp)}/{len(cset & focus)}")
            if arm == 'opus-packet':
                gap = other - allp
                print(f"  non-focus notes it cites that the packet lacked (gap finds): {len(gap)} {sorted(gap)[:12]}")
            if arm == 'opus-alone':
                miss = sorted((cset - focus) - allp)
                print(f"  non-focus notes opus-alone cites that the packet lacks: {miss[:20]}")
        for b in blocks:
            print(f"  [{b.get('id')}] ¶{b.get('p')} {b.get('verse')} · {b.get('topic')} · {len(b.get('text', '').split())} words, {len(b.get('notes') or [])} notes")


def main():
    a = sys.argv[1:]
    if a and a[0] == 'report':
        report(a[1])
        return
    if a and a[0] == 'build':
        run = a[1]
        build(run, a[a.index('--ayah') + 1], a[a.index('--page') + 1])
        return
    run, arm, cmd, rest = a[0], a[1], a[2], a[3:]

    def opt(name, default=None, cast=str):
        if name in rest:
            i = rest.index(name)
            v = rest[i + 1]
            del rest[i:i + 2]
            return cast(v)
        return default
    q = Q(run, arm)
    if cmd == 'catalog':
        q.catalog(rest)
    elif cmd == 'notes':
        word, grep, source, page = opt('--word'), opt('--grep'), opt('--source'), opt('--page', 1, int)
        q.notes(rest[0], word, grep, source, page)
    elif cmd == 'find':
        verse, page = opt('--verse'), opt('--page', 1, int)
        q.find(rest[0], verse, page)
    elif cmd == 'links':
        q.links(rest[0], rest[1])
    elif cmd == 'note':
        q.note(rest)
    elif cmd == 'packet':
        q.packet()
    elif cmd == 'packet-parts':
        q.packet_parts()
    elif cmd == 'check-packet':
        q.check_packet()
    elif cmd == 'check-write':
        q.check_write()
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main()
