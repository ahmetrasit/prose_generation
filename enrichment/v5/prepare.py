#!/usr/bin/env python3
"""Prepare a v5 run: page inputs, packets, family directories and one spawn text per agent.

Nothing is launched. The orchestrator spawns each agent with the exact text of its spawn
file, under the agent name in that file, only after the user's go. Steps that depend on an
earlier agent (writers after extractors; search writers after leads.py) are listed in
run-plan.json as stages.

  python3 -B enrichment/v5/prepare.py pilot --date 20261007
"""
import argparse
import json
import re
from datetime import datetime, timezone

from common import FROZEN, ROOT, V5, dump, page, sources, tokens, usable
import packet

PREFIX = '/root/v5p_'
MODELS = {  # role -> (model, effort)
    'extract': ('gpt-6-luna', 'max'),     # user 2026-10-06: Luna max, run here via codex exec
    'write': ('claude-opus-5-5', 'high'),   # user 2026-10-06: Opus 5.5 high instead of Sol (agent enrich-page-high)
    'search': ('claude-opus-5-5', 'high'),
    'leads': ('claude-opus-5-5', 'high'),  # user 2026-10-06: Opus 5.5 instead of Astra (Claude subagent)
}
# The agreed test: two indexed families on a light page (rivayet both ways, to measure what
# the extractor loses), one indexed family on a heavy page, one non-indexed family with leads.
PILOT = [
    {'unit': '100_1', 'family': 'rivayet', 'route': 'extract', 'writers': ['extract', 'direct']},
    {'unit': '100_1', 'family': 'meal', 'route': 'extract', 'writers': ['extract']},
    {'unit': '1_6', 'family': 'grammar', 'route': 'extract', 'writers': ['extract']},
    {'unit': '100_1', 'family': 'poetry', 'route': 'search', 'writers': ['search']},
]


def label(unit):
    return unit.replace('_', ':')


def groups(n):
    sizes = [n // 4 + (1 if i >= 4 - n % 4 else 0) for i in range(4)]
    out, at = [], 1
    for size in sizes:
        out.append((at, at + size - 1))
        at += size
    return out


def purpose(unit, family):
    for d in sorted((ROOT / f'enrichment/v4/work/{unit}').glob(f'corpus-sol-*/{family}/assignment.json')) + \
            sorted((ROOT / 'enrichment/v4/work/1_6').glob(f'corpus-sol-max-*/{family}/assignment.json')):
        return json.loads(d.read_text())['research_purpose']
    raise ValueError(f'No research purpose for {family}')


def fill(template, **values):
    text = (V5 / f'briefs/{template}.md').read_text()
    for k, v in values.items():
        text = text.replace('{' + k + '}', str(v))
    leftover = re.findall(r'\{[A-Z][A-Z_0-9]*\}', text)
    if leftover:
        raise ValueError(f'Unfilled placeholders in {template}: {leftover}')
    return text


def spawn(run, name, role, text, plan):
    model, effort = MODELS[role]
    path = run / 'spawn' / f'{name}.md'
    path.parent.mkdir(parents=True, exist_ok=True)
    if model.startswith('claude'):
        text = (f'Working directory: run every command from {ROOT} (prefix it with `cd {ROOT} && `). Write output '
                f'files with the Write tool at absolute paths under {ROOT}. Use no other files, tools or commands than '
                'those the brief names.\n\n' + text)
    path.write_text(f'<!-- agent {PREFIX}{name} | model {model} | effort {effort} | service default | fast off -->\n\n' + text)
    plan.append({'agent': PREFIX + name, 'role': role, 'model': model, 'effort': effort,
                 'spawn': str(path.relative_to(ROOT))})
    return model, effort


def prepare_unit(run, unit):
    run.mkdir(parents=True, exist_ok=True)
    (run / 'frozen.reading.tr.md').write_bytes(FROZEN[unit].read_bytes())
    text, paragraphs = page(unit)
    for n, (lo, hi) in enumerate(groups(len(paragraphs)), 1):
        body = '\n\n'.join(f'[Paragraph {p}]\n{text[paragraphs[p][0]:paragraphs[p][1]].strip()}' for p in range(lo, hi + 1))
        (run / f'input-{n}.txt').write_text(body + '\n')
    return len(paragraphs)


def pilot(date):
    name = f'pilot-{date}'
    runs = {u: V5 / f'work/{u}/{name}' for u in {j['unit'] for j in PILOT}}
    if any(r.exists() for r in runs.values()):
        raise ValueError('Run directories exist; preparation never overwrites')
    counts = {u: prepare_unit(r, u) for u, r in runs.items()}
    stages = {'1_extract_and_leads': [], '2_write': []}
    for job in PILOT:
        unit, family = job['unit'], job['family']
        run, d = runs[unit], runs[unit] / family
        rel = str(d.relative_to(ROOT))
        common = dict(FAMILY=family, UNIT_LABEL=label(unit), PARAGRAPHS=counts[unit], DIR=rel,
                      PURPOSE=purpose(unit, family))
        if job['route'] == 'search':
            d.mkdir(parents=True)
            config = sources(family)
            (d / 'sources.json').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n')
            dump(d / 'family.json', {'unit': unit, 'family': family, 'route': 'search', 'search': True})
            roster = '; '.join(f"{s['id']} ({s['author']}, {s['title']})" for s in config['sources'] if s['usable'])
            m, e = MODELS['leads']
            text = fill('leads', **common, ROSTER=roster, MODEL=m, EFFORT=e)
            spawn(run, f'{unit}_{family}_leads', 'leads', text, stages['1_extract_and_leads'])
            stages['1_extract_and_leads'][-1]['after'] = f'python3 -B enrichment/v5/leads.py {rel}'
            m, e = MODELS['search']
            leads = ('Run `candidates --part 0` and every following part. Each lead is a remembered, '
                     'unverified item with the corpus passages its search terms hit. Leads are pointers only: '
                     'confirm by reading the passage; a lead without hits may still be worth one search of your own.')
            text = fill('search', **common, LEADS=leads, LANE='search', MODEL=m, EFFORT=e)
            spawn(run, f'{unit}_{family}_write_search', 'search', text, stages['2_write'])
            continue
        chosen = packet.build(unit, family, d / 'packet', job['route'])
        manifest = json.loads((d / 'packet/manifest.json').read_text())
        dump(d / 'family.json', {'unit': unit, 'family': family, 'route': chosen, 'search': chosen.endswith('+search')})
        chunks = len(manifest['chunks'])
        size = f"{manifest['segments']} segments, about {manifest['estimated_tokens']:,} tokens"
        for c in range(1, chunks + 1):
            (d / f'extract/c{c:02d}').mkdir(parents=True)
            m, e = MODELS['extract']
            text = fill('extract', **common, CHUNK=c, CHUNKS=chunks, CHUNK2=f'{c:02d}', MODEL=m, EFFORT=e)
            spawn(run, f'{unit}_{family}_extract_c{c:02d}', 'extract', text, stages['1_extract_and_leads'])
        for lane in job['writers']:
            m, e = MODELS['write']
            if lane == 'extract':
                material = (f'Run `extracts --part 0` and every following part until `next: None`. These are verbatim '
                            f'quotes, grouped by paragraph, taken by fresh readers from every segment of your packet '
                            f'({size}); each quote names its locator, kind and what it shows.')
            else:
                material = (f'Read your whole packet ({size}): `chunk 1 --part 0` and every following part until '
                            f'`next: None`, then the same for each further chunk up to chunk {chunks}. Each segment '
                            f'header names its locator, source, verses and the paragraphs it was gathered for.')
            text = fill('write', **common, MATERIAL=material, LANE=lane, MODEL=m, EFFORT=e)
            spawn(run, f'{unit}_{family}_write_{lane}', 'write', text, stages['2_write'])
    plan = {'run': name, 'created': datetime.now(timezone.utc).isoformat(), 'prefix': PREFIX,
            'units': {u: str(r.relative_to(ROOT)) for u, r in runs.items()}, 'jobs': PILOT, 'stages': stages,
            'rules': ['Spawn only after the user\'s go; each agent gets the exact text of its spawn file.',
                      'Stage 2 starts for a family only after `check.py extract` passes for all its chunks '
                      '(or leads.py ran, for search routes).',
                      'Agents never see enrichment/v5/eval, v3/v4 outputs or other families.']}
    dump(V5 / f'work/{name}.json', plan)
    print(f"{name}: {sum(len(v) for v in stages.values())} agents in {len(stages)} stages -> enrichment/v5/work/{name}.json")


def packet_family(run, job, counts, stage1, stage2):
    """Packet, family.json, extract dirs and the extractor + writer spawn texts for one packet-route job."""
    unit, family = job['unit'], job['family']
    d = run / family
    rel = str(d.relative_to(ROOT))
    common = dict(FAMILY=family, UNIT_LABEL=label(unit), PARAGRAPHS=counts[unit], DIR=rel, PURPOSE=purpose(unit, family))
    chosen = packet.build(unit, family, d / 'packet', job['route'])
    manifest = json.loads((d / 'packet/manifest.json').read_text())
    dump(d / 'family.json', {'unit': unit, 'family': family, 'route': chosen, 'search': chosen.endswith('+search')})
    chunks = len(manifest['chunks'])
    size = f"{manifest['segments']} segments, about {manifest['estimated_tokens']:,} tokens"
    for c in range(1, chunks + 1):
        (d / f'extract/c{c:02d}').mkdir(parents=True)
        m, e = MODELS['extract']
        text = fill('extract', **common, CHUNK=c, CHUNKS=chunks, CHUNK2=f'{c:02d}', MODEL=m, EFFORT=e)
        spawn(run, f'{unit}_{family}_extract_c{c:02d}', 'extract', text, stage1)
    for lane in job['writers']:
        m, e = MODELS['write']
        if lane == 'extract':
            material = (f'Run `extracts --part 0` and every following part until `next: None`. These are verbatim '
                        f'quotes, grouped by paragraph, taken by fresh readers from every segment of your packet '
                        f'({size}); each quote names its locator, kind and what it shows.')
        else:
            material = (f'Read your whole packet ({size}): `chunk 1 --part 0` and every following part until '
                        f'`next: None`, then the same for each further chunk up to chunk {chunks}. Each segment '
                        f'header names its locator, source, verses and the paragraphs it was gathered for.')
        text = fill('write', **common, MATERIAL=material, LANE=lane, MODEL=m, EFFORT=e)
        spawn(run, f'{unit}_{family}_write_{lane}', 'write', text, stage2)


def rechunk(date, families):
    """Rebuild packet families of an existing run (after a chunk-size or brief change). Earlier packets,
    extracts, spawn texts and runs move to superseded/<stamp>/; nothing is deleted. Other families untouched."""
    import shutil
    import time
    name = f'pilot-{date}'
    plan_path = V5 / f'work/{name}.json'
    plan = json.loads(plan_path.read_text())
    stamp = time.strftime('%Y%m%dT%H%M%S')
    counts = {u: len(page(u)[1]) for u in plan['units']}
    for job in PILOT:
        if job['family'] not in families or job['route'] == 'search':
            continue
        unit, family = job['unit'], job['family']
        run = ROOT / plan['units'][unit]
        old = run / family / 'superseded' / stamp
        old.mkdir(parents=True)
        for part in ('packet', 'extract', 'family.json'):
            if (run / family / part).exists():
                shutil.move(str(run / family / part), str(old / part))
        for folder, pattern in ((run / 'spawn', f'{unit}_{family}_*.md'), (run / 'runs', f'v5p_{unit}_{family}_*')):
            for f in sorted(folder.glob(pattern)):
                target = folder / 'superseded' / stamp
                target.mkdir(parents=True, exist_ok=True)
                shutil.move(str(f), str(target / f.name))
        agents = {PREFIX + f'{unit}_{family}_'}
        for stage in plan['stages'].values():
            stage[:] = [a for a in stage if not a['agent'].startswith(next(iter(agents)))]
        packet_family(run, job, counts, plan['stages']['1_extract_and_leads'], plan['stages']['2_write'])
    plan.setdefault('history', []).append({'rechunked': stamp, 'families': families,
                                           'chunk_chars': __import__('common').CHUNK_CHARS})
    dump(plan_path, plan)
    print(f'{name}: rebuilt {families}; earlier material under superseded/{stamp}/')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', choices=('pilot', 'rechunk'))
    parser.add_argument('--date', required=True)
    parser.add_argument('--families', nargs='+')
    a = parser.parse_args()
    if a.command == 'pilot':
        pilot(a.date)
    else:
        rechunk(a.date, a.families)
