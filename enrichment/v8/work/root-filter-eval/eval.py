#!/usr/bin/env python3
"""Evaluate the root filter (per paragraph: roots the paragraph mentions → notes on its cited verses that are about
those roots) on the 103:1, 1:3 and 95:1 pages. No model is called.

  python3 -B enrichment/v8/work/root-filter-eval/eval.py            writes results.json, sample_*.tsv, misses_95_1.tsv
"""
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rootlib as L  # noqa: E402

REF = L.ROOT / 'enrichment/v8/work/luna-test-95_1/write/opus-alone/blocks.jsonl'
MUST = {'MAJAZ:v1p312/r7', 'MAJAZ:v1p312/r8', 'IBNQUTAYBA-GHARIB:v1p218#5/r3', 'TAB-FULL:v13p197/r1',
        'SAMIN-DURR:12:49/r8'}

qac = L.Qac()
NR = L.NoteRoots(qac)
STOP = {r for r, n in qac.freq.items() if n >= L.STOP_FREQ}


def configs(focus_roots):
    """name -> (roots of a paragraph -> roots used, detectors, use simulated tags, untagged policy, scope)."""
    keep = lambda rs: {r for r in rs if r not in STOP or r in focus_roots}  # noqa: E731
    return {
        'A faithful (lex)':          (lambda rs: rs, ('lex',), False, None, 'para'),
        'B faithful (lex+pat+tr)':   (lambda rs: rs, ('lex', 'pat', 'tr'), False, None, 'para'),
        'C B + focus roots':         (lambda rs: rs | focus_roots, ('lex', 'pat', 'tr'), False, None, 'para'),
        'D C − common roots':        (lambda rs: keep(rs | focus_roots), ('lex', 'pat', 'tr'), False, None, 'para'),
        'T1 tagged sim, untagged out': (lambda rs: keep(rs | focus_roots), None, True, 'out', 'para'),
        'T2 tagged sim, untagged in':  (lambda rs: keep(rs | focus_roots), None, True, 'in', 'para'),
        'X T2 + page scope (root-gated)': (lambda rs: keep(rs | focus_roots), None, True, 'in', 'page'),
    }


def run_page(ayah, rng):
    P = L.paragraphs(ayah, qac)
    page_verses = sorted({v for d in P.values() for v in d['cites']})
    notes = L.notes_on(page_verses)
    focus_roots = qac.verse_roots(ayah)
    # simulated tags: per note, verse words it names (on its verses that are on the page)
    tags = {i: NR.tag(r, sorted(r['verses']), STOP) for i, r in notes.items()}
    size = {i: len(L.line(r)) for i, r in notes.items()}
    toks = {i: L.tokens_est(L.line(r)) for i, r in notes.items()}
    all_roots = set().union(*(d['roots'] for d in P.values())) | focus_roots
    cache = {}
    res = {'ayah': ayah, 'paras': {}, 'configs': {}}
    sel_by = {}
    for name, (rootf, how, tagged, untagged, scope) in configs(focus_roots).items():
        per, union = {}, set()
        for p, d in P.items():
            roots = rootf(d['roots'])
            if scope == 'para':
                cand = [i for i, r in notes.items() if r['verses'] & set(d['cites'])]
            else:   # page scope: notes on any page verse; off-paragraph verses only when tagged with a paragraph root
                cand = list(notes)
            sel = {}
            for i in cand:
                r = notes[i]
                in_para = bool(r['verses'] & set(d['cites']))
                if tagged:
                    words, troots = tags[i]
                    if not words:
                        if untagged == 'in' and in_para:
                            sel[i] = '*'
                        continue
                    hit = troots & roots
                    if not in_para:
                        hit = hit & {x for x in d['roots'] if x in d['why'] and 'dict' in d['why'][x]} | \
                              (hit & focus_roots)
                else:
                    if (how, i) not in cache:
                        cache[how, i] = NR.match(r, all_roots, how)
                    hit = cache[how, i] & roots
                if hit:
                    sel[i] = ','.join(sorted(hit))
            per[p] = sel
            union |= set(sel)
        sel_by[name] = per
        res['configs'][name] = {
            'per_para': {p: {'n': len(s), 'chars': sum(size[i] for i in s)} for p, s in per.items()},
            'sum_n': sum(len(s) for s in per.values()), 'sum_chars': sum(size[i] for s in per.values() for i in s),
            'sum_tok': sum(toks[i] for s in per.values() for i in s),
            'cited_sum_n': sum(1 for s in per.values() for i in s if ayah not in notes[i]['verses']),
            'cited_sum_chars': sum(size[i] for s in per.values() for i in s if ayah not in notes[i]['verses']),
            'cited_sum_tok': sum(toks[i] for s in per.values() for i in s if ayah not in notes[i]['verses']),
            'cited_max_chars': max(sum(size[i] for i in s if ayah not in notes[i]['verses']) for s in per.values()),
            'focus_avg_n': sum(1 for s in per.values() for i in s if ayah in notes[i]['verses']) / len(per),
            'focus_union_n': len({i for s in per.values() for i in s if ayah in notes[i]['verses']}),
            'empty_paras': [p for p, s in per.items() if not s],
            'union_n': len(union), 'union_chars': sum(size[i] for i in union),
            'union_tok': sum(toks[i] for i in union)}
    # baseline: every note on the paragraph's cited verses
    base = {p: [i for i, r in notes.items() if r['verses'] & set(d['cites'])] for p, d in P.items()}
    res['baseline'] = {'per_para': {p: {'n': len(s), 'chars': sum(size[i] for i in s)} for p, s in base.items()},
                       'sum_n': sum(len(s) for s in base.values()),
                       'sum_chars': sum(size[i] for s in base.values() for i in s),
                       'sum_tok': sum(toks[i] for s in base.values() for i in s),
                       'cited_sum_n': sum(1 for s in base.values() for i in s if ayah not in notes[i]['verses']),
                       'cited_sum_chars': sum(size[i] for s in base.values() for i in s if ayah not in notes[i]['verses']),
                       'cited_sum_tok': sum(toks[i] for s in base.values() for i in s if ayah not in notes[i]['verses']),
                       'cited_max_chars': max(sum(size[i] for i in s if ayah not in notes[i]['verses']) for s in base.values()),
                       'union_n': len(notes), 'union_chars': sum(size.values()), 'union_tok': sum(toks.values())}
    focus_ids = [i for i, r in notes.items() if ayah in r['verses']]
    res['focus'] = {'n': len(focus_ids), 'chars': sum(size[i] for i in focus_ids),
                    'tok': sum(toks[i] for i in focus_ids)}
    res['tag_coverage'] = sum(1 for i in notes if tags[i][0]) / len(notes)
    for p, d in P.items():
        res['paras'][p] = {'cites': d['cites'], 'roots': sorted(d['roots']), 'why': {k: sorted(v) for k, v in d['why'].items()},
                           'unmatched': d['unmatched'], 'chars': len(d['text'])}
    return P, notes, tags, sel_by, res, base


def main():
    rng = random.Random(7)
    out, keep = {}, {}
    for ayah in L.PAGES:
        P, notes, tags, sel_by, res, base = run_page(ayah, rng)
        out[ayah] = res
        keep[ayah] = (P, notes, tags, sel_by, base)
        # precision sample: 30 selected (paragraph, note) pairs from config D and from T2
        for name in ('B faithful (lex+pat+tr)', 'T1 tagged sim, untagged out'):
            pairs = [(p, i) for p, s in sel_by[name].items() for i in s if ayah not in notes[i]['verses']]
            pairs_f = [(p, i) for p, s in sel_by[name].items() for i in s if ayah in notes[i]['verses']]
            k = name.split()[0]
            # half cited-verse notes, half focus notes (cited-verse notes are where the filter acts)
            smp = rng.sample(pairs, min(20, len(pairs))) + rng.sample(pairs_f, min(10, len(pairs_f)))
            with open(HERE / f"sample_{ayah.replace(':', '_')}_{k}.tsv", 'w') as f:
                f.write('para\tnote\tverses\tmatched\tclaim\tanchor\n')
                for p, i in smp:
                    r = notes[i]
                    f.write(f"{p}\t{i}\t{','.join(sorted(r['verses']))}\t{sel_by[name][p][i]}\t{r['claim']}\t"
                            f"{(r['anchor'] or '').replace(chr(10), ' ')}\n")
        if ayah == '103:1':
            out[ayah]['must'] = {name: {p: sorted(MUST & set(sel_by[name][p])) for p in (11, 12)} for name in sel_by}
            out[ayah]['must_matched_by'] = {name: {i: sel_by[name][12].get(i) for i in MUST} for name in sel_by}
            out[ayah]['must_tags'] = {i: [list(map(list, tags[i][0])), sorted(tags[i][1])] for i in MUST if i in tags}
    # recall on 95:1
    P, notes, tags, sel_by, base = keep['95:1']
    ref = [json.loads(x) for x in open(REF)]
    pairs = sorted({(b['p'][0], n) for b in ref for n in b['notes']})
    rec = {}
    for name, per in sel_by.items():
        hit = [(p, n) for p, n in pairs if n in per[p]]
        page_hit = {n for p, n in pairs if any(n in s for s in per.values())}
        byp = defaultdict(lambda: [0, 0])
        for p, n in pairs:
            byp[p][1] += 1
            byp[p][0] += n in per[p]
        foc = [(p, n) for p, n in pairs if '95:1' in notes[n]['verses']]
        rec[name] = {'pairs': len(pairs), 'hit': len(hit), 'focus_pairs': len(foc),
                     'focus_hit': sum(1 for p, n in foc if n in per[p]), 'page_ids': len({n for _, n in pairs}),
                     'page_hit': len(page_hit), 'by_para': dict(byp)}
    out['95:1']['recall'] = rec
    out['95:1']['ref_in_scope'] = sum(1 for p, n in pairs if n in base[p])
    # misses of B and T2, with what the note names
    with open(HERE / 'misses_95_1.tsv', 'w') as f:
        f.write('config\tpara\tnote\tverses\tin_scope\tnote_words(sim tag)\tpara_roots\tclaim\tanchor\n')
        for name in ('B faithful (lex+pat+tr)', 'D C − common roots', 'T1 tagged sim, untagged out'):
            for p, n in pairs:
                if n in sel_by[name][p]:
                    continue
                r = notes.get(n)
                f.write(f"{name}\t{p}\t{n}\t{','.join(sorted(r['verses'])) if r else '?'}\t{n in base[p]}\t"
                        f"{' '.join(c for _, c in tags[n][0]) if r else ''}\t{' '.join(sorted(P[p]['roots']))}\t"
                        f"{r['claim'] if r else ''}\t{(r['anchor'] or '').replace(chr(10), ' ') if r else ''}\n")
    import pickle
    pickle.dump({a: (P_, notes_, tags_, sel_, base_) for a, (P_, notes_, tags_, sel_, base_) in keep.items()},
                open(HERE / 'state.pkl', 'wb'))
    (HERE / 'results.json').write_text(json.dumps(out, ensure_ascii=False, indent=1, default=list))
    # short console summary
    for ayah, res in out.items():
        b = res['baseline']
        print(f"\n== {ayah}: {len(res['paras'])} paragraphs; notes on page verses {b['union_n']} "
              f"({b['union_chars']:,} ch, ~{b['union_tok']:,.0f} tok); focus notes {res['focus']['n']} "
              f"({res['focus']['chars']:,} ch); sim-tag coverage {res['tag_coverage']:.0%}")
        print(f"   baseline per-paragraph sum: {b['sum_n']} notes {b['sum_chars']:,} ch ~{b['sum_tok']:,.0f} tok")
        for name, c in res['configs'].items():
            print(f"   {name:34s} sum {c['sum_n']:6d} notes {c['sum_chars']:>11,} ch ~{c['sum_tok']:>9,.0f} tok | "
                  f"union {c['union_n']:5d} {c['union_chars']:>10,} ch")
    for name, r in out['95:1']['recall'].items():
        print(f"recall 95:1 {name:34s} pairs {r['hit']}/{r['pairs']}  page ids {r['page_hit']}/{r['page_ids']}")
    print('must-find 103:1', json.dumps(out['103:1']['must'], ensure_ascii=False, indent=0))


if __name__ == '__main__':
    main()
