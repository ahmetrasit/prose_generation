#!/usr/bin/env python3
"""Score a v5 run against the earlier benchmark runs. Parent-only: agents never read eval/.

Reference = every segment the v4 corpus runs cited for the unit/family (both efforts), plus
items verified on 100:1 that those runs missed. It is a reference set, not a gold standard:
it holds neither every useful finding nor guaranteed readings, so new v5 material is
reported for judgement, not scored as error.

Segment-level measures (per family, per writer lane):
  packet     reference segments inside the packet (a per-ayah slice counts when the packet holds
             the same work's FULL copy for that verse)
  extracted  reference segments an extractor quoted from
  cited      reference segments the writer cites;  new = cited segments outside the reference
Finding-level judgement uses REVIEW-<family>.md: per paragraph, reference blocks beside v5 blocks.

  python3 -B enrichment/v5/evaluate.py reference      (once; writes eval/reference.json)
  python3 -B enrichment/v5/evaluate.py score pilot-20261007
"""
import argparse
import json
from collections import defaultdict

from common import ROOT, V5, connect, dump, rows

REF_RUNS = {
    '1_6': ['enrichment/v4/work/1_6/corpus-sol-high-20261006', 'enrichment/v4/work/1_6/corpus-sol-max-20261006'],
    '87_6': ['enrichment/v4/work/87_6/corpus-sol-max-20261006'],
    '100_1': ['enrichment/v4/work/100_1/corpus-sol-high-20261007', 'enrichment/v4/work/100_1/corpus-sol-max-20261007'],
}
# Corpus-held items the 100:1 corpus agents missed, found via memory and checked by hand (2026-10-06).
EXTRA = {('100_1', 'poetry'): ['MUALLAQAT:v1p71#2'], ('100_1', 'historical'): ['WAHIDI-ASBAB:v1p55#2']}
EVAL = V5 / 'eval'


def reference():
    out = {}
    for unit, runs in REF_RUNS.items():
        for run in runs:
            for f in sorted((ROOT / run).glob('*/blocks.jsonl')):
                family = f.parent.name
                entry = out.setdefault(f'{unit}/{family}', {'locs': set(), 'blocks': []})
                for b in rows(f):
                    entry['locs'] |= {e['loc'] for e in b.get('evidence', [])}
                    entry['blocks'].append({'run': run.rsplit('/', 1)[1], 'p': b['p'], 'text': b['text'],
                                            'locs': [e['loc'] for e in b.get('evidence', [])]})
    for (unit, family), locs in EXTRA.items():
        out.setdefault(f'{unit}/{family}', {'locs': set(), 'blocks': []})['locs'] |= set(locs)
    dump(EVAL / 'reference.json', {k: {'locs': sorted(v['locs']), 'blocks': v['blocks']} for k, v in out.items()})
    print(f'{len(out)} unit/family reference sets -> {EVAL / "reference.json"}')


def slice_key(con, loc):
    """(work, s, a) for a per-verse slice whose work is also held whole (X versus X-FULL); else None."""
    r = con.execute('SELECT src,s,a FROM seg WHERE seg=?', (loc,)).fetchone()
    if not r or r[1] is None or r[0].endswith('-FULL'):
        return None
    has_full = con.execute('SELECT 1 FROM seg WHERE src=? LIMIT 1', (r[0] + '-FULL',)).fetchone()
    return (r[0], r[1], r[2]) if has_full else None


def full_keys(con, locs):
    """(work, s, a) for every verse a FULL segment spans."""
    out = set()
    for loc in locs:
        r = con.execute('SELECT src,s,a,a_end FROM seg WHERE seg=?', (loc,)).fetchone()
        if r and r[0].endswith('-FULL') and r[1] is not None:
            out |= {(r[0][:-5], r[1], a) for a in range(r[2], (r[3] or r[2]) + 1)}
    return out


def matched(con, ref_locs, found):
    """Reference segments found exactly, or slices whose verse a found FULL segment spans."""
    keys = full_keys(con, found)
    return {l for l in ref_locs if l in found or slice_key(con, l) in keys}


def score(run):
    plan = json.loads((V5 / f'work/{run}.json').read_text())
    ref = json.loads((EVAL / 'reference.json').read_text())
    report = {}
    with connect() as con:
        for job in plan['jobs']:
            unit, family = job['unit'], job['family']
            d = ROOT / plan['units'][unit] / family
            r = ref.get(f'{unit}/{family}', {'locs': [], 'blocks': []})
            ref_locs = set(r['locs'])
            res = {'reference_segments': len(ref_locs)}
            covered = set(ref_locs)
            if (d / 'packet/segments.jsonl').exists():
                segs = rows(d / 'packet/segments.jsonl')
                inside = {s['loc'] for s in segs}
                verse_keys = {(s['src'][:-5], *map(int, v.split(':'))) for s in segs
                              if s['src'].endswith('-FULL') for v in s['verses']}
                covered = {l for l in ref_locs if l in inside or slice_key(con, l) in verse_keys}
                res['packet'] = len(covered)
                res['packet_missing'] = sorted(ref_locs - covered)
                quoted = {x['loc'] for f in d.glob('extract/c*/extracts.jsonl') for x in rows(f)}
                if quoted:
                    hit = matched(con, covered, quoted)
                    res['extracted'] = len(hit)
                    res['extract_missed'] = sorted(covered - hit)
                    res['extracted_segments'] = len(quoted)
            for lane in job['writers']:
                f = d / f'write-{lane}/blocks.jsonl'
                if not f.exists():
                    res[f'write-{lane}'] = 'not run'
                    continue
                blocks = rows(f)
                cited = {e['loc'] for b in blocks for e in b.get('evidence', [])}
                hit = matched(con, ref_locs, cited)
                res[f'write-{lane}'] = {'blocks': len(blocks), 'cited_segments': len(cited),
                                        'reference_cited': len(hit), 'new_segments': len(cited - ref_locs)}
                review(unit, family, lane, r['blocks'], blocks, run)
            report[f'{unit}/{family}'] = res
    usage = V5 / f'work/{run}-usage/usage.json'
    if usage.exists():
        u = json.loads(usage.read_text())
        by = defaultdict(float)
        for a in u['agents']:
            name = a['agent'].removeprefix(plan['prefix'])
            by[name.split('_extract')[0].split('_write')[0].split('_leads')[0]] += a['usd']
        report['cost_usd_by_unit_family'] = {k: round(v, 4) for k, v in by.items()}
    dump(EVAL / f'{run}-score.json', report)
    print(json.dumps(report, ensure_ascii=False, indent=1)[:4000])


def review(unit, family, lane, ref_blocks, blocks, run):
    by_p = defaultdict(lambda: {'ref': [], 'v5': []})
    for b in ref_blocks:
        by_p[b['p'][0]]['ref'].append(b)
    for b in blocks:
        by_p[b['p'][0]]['v5'].append(b)
    lines = [f'# {run}: {unit} {family}, write-{lane} beside the reference runs', '',
             'Judge findings, not length: distinct positions, preserved disagreements, preferences, '
             'direct witnesses, translator wording, attribution errors, omissions, and genuinely new material.', '']
    for p in sorted(by_p):
        lines.append(f'## Paragraph {p}')
        for b in by_p[p]['ref']:
            lines += [f"**Reference ({b['run']})** — {', '.join(b['locs'])}", '', b['text'], '']
        for b in by_p[p]['v5']:
            lines += [f"**v5 {lane}** — {', '.join(e['loc'] for e in b.get('evidence', []))}", '', b['text'], '']
    path = EVAL / f'{run}-REVIEW-{unit}-{family}-{lane}.md'
    path.write_text('\n'.join(lines) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', choices=('reference', 'score'))
    parser.add_argument('run', nargs='?')
    a = parser.parse_args()
    reference() if a.command == 'reference' else score(a.run)
