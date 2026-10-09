#!/usr/bin/env python3
"""Second pass over eval.py's state.pkl: (1) why the faithful root filter missed reference notes on 95:1;
(2) the proposed alternative: a per-paragraph menu of cells (verse word on a cited verse) with the paragraph's
roots used as pointers (★) instead of a gate, plus link notes (notes that name a cited verse), measured for size and
for how much of the reference the pointers alone reach. No model is called.

  python3 -B enrichment/v8/work/root-filter-eval/analyze.py      writes improve.json, prints tables
"""
import json
import pickle
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rootlib as L  # noqa: E402

st = pickle.load(open(HERE / 'state.pkl', 'rb'))
qac = L.Qac()
STOP = {r for r, n in qac.freq.items() if n >= L.STOP_FREQ}
ref = [json.loads(x) for x in open(L.ROOT / 'enrichment/v8/work/luna-test-95_1/write/opus-alone/blocks.jsonl')]
PAIRS = sorted({(b['p'][0], n) for b in ref for n in b['notes']})
ARABIC = L.ARABIC_CH
out = {}

# ---------------------------------------------------------------- 1. miss classes (faithful B, 95:1)
P, notes, tags, sel, base = st['95:1']
B = sel['B faithful (lex+pat+tr)']
cls = Counter()
examples = defaultdict(list)
for p, n in PAIRS:
    if n in B[p]:
        continue
    r = notes[n]
    words, troots = tags[n]
    if not (r['verses'] & set(P[p]['cites'])):
        c = 'out of paragraph scope (note is on a verse the paragraph does not cite)'
    elif words and not (troots & P[p]['roots']):
        c = 'names a verse word the paragraph does not quote in Arabic (only in Turkish, or not at all)'
    elif not ARABIC.search(r['anchor'] or '') and not words:
        c = 'non-Arabic source (anchor in English/Turkish), names no verse word'
    elif not words:
        c = 'Arabic anchor quotes the explanation, not the verse word (whole-verse / referent / context note)'
    else:
        c = 'other'
    cls[c] += 1
    if len(examples[c]) < 4:
        examples[c].append(f"¶{p} {n}: {r['claim'][:110]}")
out['miss_classes_B'] = {'total_missed': sum(cls.values()), 'classes': dict(cls), 'examples': examples}

# ---------------------------------------------------------------- 2. the menu
con = sqlite3.connect(L.INDEX)


con.row_factory = sqlite3.Row
MSIZE = {}


def mentions_of(verse_set):
    """Notes anywhere in the index whose mentions name one of the verses (cross-reference notes), with sizes."""
    out_ = defaultdict(set)
    for r in con.execute("SELECT * FROM notes WHERE mentions != '[]'"):
        for x in json.loads(r['mentions']):
            if x in verse_set:
                out_[x].add(r['id'])
                MSIZE[r['id']] = len(L.line(r))
    return out_


def menu(ayah):
    P, notes, tags, sel, base = st[ayah]
    focus_roots = qac.verse_roots(ayah)
    page_verses = sorted({v for d in P.values() for v in d['cites']})
    size = {i: len(L.line(r)) for i, r in notes.items()}
    # cells: (verse, word) from the simulated tags; '*' when a note names no word of its verse
    cells = defaultdict(set)
    croot = {}
    for i, r in notes.items():
        words, _ = tags[i]
        if words:
            for v, c in words:
                cells[v, c].add(i)
                croot[v, c] = next((rs for w_, c_, rs in qac.words[v] if c_ == c), set())
        for v in r['verses']:
            if not any(w[0] == v for w in words):
                cells[v, '*'].add(i)
                croot[v, '*'] = set()
    cell_line = {k: len(f"{k[0]} {k[1]} · {len(ids)} notes · {len({notes[i]['src'] for i in ids})} sources · "
                        f"h{sum(notes[i]['stance'] == 'holds' for i in ids)} r{sum(notes[i]['stance'] == 'reports' for i in ids)} "
                        f"p{sum(notes[i]['stance'] == 'prefers' for i in ids)} x{sum(notes[i]['stance'] == 'rejects' for i in ids)} ★")
                 for k, ids in cells.items()}
    ment = mentions_of(set(page_verses))
    res = {}
    for p, d in P.items():
        cited = [v for v in d['cites'] if v != ayah]
        roots = {r for r in d['roots'] | focus_roots if r not in STOP or r in focus_roots}
        dict_roots = {r for r, w in d['why'].items() if 'dict' in w} | focus_roots
        my = [k for k in cells if k[0] in cited]                       # menu lines for the cited verses
        star = {k for k in my if croot[k] & roots}
        star_w = star | {k for k in my if k[1] == '*'}                 # variant: whole-verse cells starred too
        # cross-paragraph pointers: cells on other page verses whose word carries a dictionary/focus root of ¶
        cross = {k for k in cells if k[0] not in d['cites'] and k[0] != ayah and croot[k] & dict_roots
                 and k[1] != '*'}
        link, named = set(), set()
        for v in cited:                                                 # notes that name a cited verse...
            link |= {i for i in ment.get(v, ()) if i in notes and ayah in notes[i]['verses']}  # ...on the focus ayah
            named |= {i for i in ment.get(v, ()) if not (i in notes and (v in notes[i]['verses'] or ayah in notes[i]['verses']))}
        link |= {i for i in ment.get(ayah, ()) if i in notes and notes[i]['verses'] & set(cited)}  # cited → focus
        star_ids = set().union(*(cells[k] for k in star)) if star else set()
        cross_ids = set().union(*(cells[k] for k in cross)) if cross else set()
        res[p] = {'menu_lines': len(my), 'menu_chars': sum(cell_line[k] for k in my),
                  'cross_lines': len(cross), 'cross_chars': sum(cell_line[k] for k in cross),
                  'star_lines': len(star), 'star_notes': len(star_ids), 'star_chars': sum(size[i] for i in star_ids),
                  'link_notes': len(link), 'link_chars': sum(size.get(i) or MSIZE[i] for i in link),
                  'named_elsewhere_notes': len(named), 'named_elsewhere_lines': len(cited),
                  'named_elsewhere_chars': sum(size.get(i) or MSIZE[i] for i in named), '_named': named,
                  'cited_notes': len(base[p]) - sum(1 for i in base[p] if ayah in notes[i]['verses']),
                  'starw_chars': sum(size[i] for i in set().union(*(cells[k] for k in star_w))) if star_w else 0,
                  '_starw': set().union(*(cells[k] for k in star_w)) if star_w else set(),
                  '_star': star_ids, '_link': link, '_cross': cross_ids, '_cells': {k: cells[k] for k in my}}
    focus_cells = [k for k in cells if k[0] == ayah]
    return res, cells, focus_cells, cell_line


summary = {}
for ayah in st:
    res, cells, focus_cells, cell_line = menu(ayah)
    P, notes, tags, sel, base = st[ayah]
    s = {k: sum(r[k] for r in res.values()) for k in ('named_elsewhere_notes', 'named_elsewhere_chars', 'named_elsewhere_lines',
                                                       'menu_lines', 'menu_chars', 'cross_lines', 'cross_chars',
                                                       'star_lines', 'star_notes', 'star_chars', 'link_notes',
                                                       'link_chars', 'cited_notes')}
    s['max_menu_chars'] = max(r['menu_chars'] + r['cross_chars'] for r in res.values())
    s['avg_star_chars'] = s['star_chars'] / len(res)
    s['avg_starw_chars'] = sum(r['starw_chars'] for r in res.values()) / len(res)
    s['max_star_chars'] = max(r['star_chars'] for r in res.values())
    s['star_union_notes'] = len(set().union(*(r['_star'] for r in res.values())))
    s['star_union_chars'] = sum(len(L.line(notes[i])) for i in set().union(*(r['_star'] for r in res.values())))
    s['focus_cells'] = len(focus_cells)
    s['focus_cell_chars'] = sum(cell_line[k] for k in focus_cells)
    s['page_cells'] = len(cells)
    s['page_menu_chars'] = sum(cell_line.values())
    s['per_para'] = {p: {k: v for k, v in r.items() if not k.startswith('_')} for p, r in res.items()}
    summary[ayah] = s
    if ayah == '95:1':
        # reach: reference pairs on cited verses (focus notes are loaded whole, so they are always reached)
        reach = Counter()
        for p, n in PAIRS:
            r = res[p]
            on_focus = '95:1' in notes[n]['verses']
            if on_focus:
                reach['on focus ayah (loaded whole)'] += 1
                continue
            reach['cited-verse pairs'] += 1
            if n in r['_starw'] or n in r['_link']:
                reach['reached with whole-verse cells starred too'] += 1
            if n in r['_star'] or n in r['_link']:
                reach['reached by ★ cell or link note'] += 1
            elif n in r['_named']:
                reach['on the menu as a note elsewhere that names a cited verse'] += 1
            elif any(n in ids for ids in r['_cells'].values()):
                reach['in an unstarred menu cell of the paragraph (writer must choose to pull it)'] += 1
            else:
                reach['not on the paragraph menu'] += 1
        s['reach'] = dict(reach)
        # pull cost if the writer pulled exactly the cells that hold the reference notes (oracle)
        pulled = set()
        for p, n in PAIRS:
            for k, ids in res[p]['_cells'].items():
                if n in ids:
                    pulled.add(k)
        s['oracle_pull_cells'] = len(pulled)
        ids = {i for k in pulled for i in cells[k] if '95:1' not in notes[i]['verses']}
        s['oracle_pull_notes'] = len(ids)
        s['oracle_pull_chars'] = sum(len(L.line(notes[i])) for i in ids)
        s['oracle_pull_cells_list'] = sorted(f'{k[0]} {k[1]} ({len(cells[k])})' for k in pulled)
    if ayah == '103:1':
        must = {'MAJAZ:v1p312/r7', 'MAJAZ:v1p312/r8', 'IBNQUTAYBA-GHARIB:v1p218#5/r3', 'TAB-FULL:v13p197/r1',
                'SAMIN-DURR:12:49/r8'}
        s['must_p11'] = {'star_or_link': sorted(must & (res[11]['_star'] | res[11]['_link'])),
                         'cross_pointer': sorted(must & res[11]['_cross']),
                         'cross_cells': sorted(f'{k[0]} {k[1]}' for k in cells if k[0] not in P[11]['cites']
                                               and k[0] != '103:1' and qac.verse_roots(k[0]) and
                                               any(c_ == k[1] and 'عصر' in rs for _, c_, rs in qac.words[k[0]]))}
        s['must_p12'] = sorted(must & (res[12]['_star'] | res[12]['_link']))

(HERE / 'improve.json').write_text(json.dumps({'misses': out, 'menu': summary}, ensure_ascii=False, indent=1,
                                              default=list))
print(json.dumps(out, ensure_ascii=False, indent=1, default=list))
for a, s in summary.items():
    print(a, {k: v for k, v in s.items() if k != 'per_para'})
