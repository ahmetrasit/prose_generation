#!/usr/bin/env python3
"""Prepare, merge and prefetch Bible discovery. Never calls a model.

Prepare --surah N --run-tag NAME [--targets N:A,surah]. Native agents use
 discovery_bible_native.py start/snapshot/audit/finish, then --merge --prefetch.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import re
import sqlite3
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT_PG = HERE.parents[1]
sys.path.insert(0,str(ROOT_PG))
from enrichment.bible import corpus as C, render as R, sections
MODELS = {'luna':'gpt-6-luna','terra':'gpt-5.6-terra'}
EFFORT = 'max'
STRENGTH = {'strong', 'medium', 'weak'}
TRAD = {'tevrat', 'incil'}
KIND = {'paralel', 'motif', 'karsi_anlati', 'soydas', 'yorum_gelenegi'}
OSIS = re.compile(r'^[1-4]?[A-Z][A-Za-z]{1,6}\.\d+\.\d+$')
INDEX = HERE / 'corpus/corpus.sqlite'
FOLLOWUP = ('Review your remembered coverage for qualifying omitted Hebrew Bible, New Testament, Jewish and '
            'Christian passages under the same inclusion and grading rules. Check distinct scenes, formulas, '
            'cognates, secondary details, counter-narratives and necessary passage continuations. Write only new '
            'candidate proposals to {output}, using the same six-field TSV with edition-qualified Bible references. '
            'Do not modify list.tsv or regrade existing candidates. Preserve distinct reasons or kinds for a passage. '
            'Zero additions is valid: create an empty followup.tsv. Do not read files, retrieve sources, consult '
            'other agents or run research scripts. A file-write tool or literal shell write solely to save '
            'followup.tsv is permitted. Reply with a brief completion notice and any accuracy concerns.')


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def save(path: Path, data) -> None:
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(path)


def discovery_dir(s: int, run_tag: str) -> Path:
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*', run_tag):
        raise ValueError('invalid run tag')
    return HERE / 'work' / f's{s:03d}' / 'discovery' / run_tag


def tdir(s: int, target: str, run_tag: str) -> Path:
    if not re.fullmatch(r'(?:\d+:\d+|sec\d+)', target):
        raise ValueError(f'invalid discovery target {target}')
    return discovery_dir(s, run_tag) / target.replace(':', '_')


def targets_of(s: int) -> list[dict]:
    """Use the exact frozen pack, including augment9 for ayah discovery."""
    pk = R.V2 / 'work' / f's{s:03d}' / 'pack'
    bases = json.loads((pk / 'base.json').read_text())
    out = []
    for ref, info in bases['ayat'].items():
        if info:
            name, text, _ = R.target_page(s, ref)
            out.append({'target':ref, 'ayat':[ref], 'prose':text, 'what':f'ayah {ref} with its augment9 commentary',
                        'base_path':str(pk/'base'/name), 'base_sha256':info['sha256']})
    name, text, info = R.target_page(s, 'surah')
    for sec in sections.sections(text):
        out.append({'target':f"sec{sec['k']}", 'ayat':sec['ayat'] or list(bases['ayat']), 'prose':sec['prose'],
                    'what':f"image section {sec['k']} ({sec['title']}) of the frozen surah commentary",
                    'base_path':str(pk/'base'/name), 'base_sha256':info['sha256']})
    return out


def package(s: int, t: dict, q: dict) -> str:
    lines = [f"# S{s}: {t['what']}", '', '## Ayat (Arabic)', '']
    lines += [f'{r}\t{q[r]}' for r in t['ayat']]
    lines += ['', '## Frozen commentary (Turkish)', '', t['prose'].strip(), '', '## Whole surah (Arabic)', '']
    lines += [f'{r}\t{text}' for r, text in q.items() if r.startswith(f'{s}:')]
    return '\n'.join(lines) + '\n'


def prompt_text(s: int, t: dict, d: Path) -> str:
    tpl = (HERE / 'prompts/discover.md').read_text()
    for key, value in {'{{PACKAGE_PATH}}':str(d/'package.md'), '{{OUTPUT_PATH}}':str(d/'list.tsv'),
                       '{{SURAH}}':str(s), '{{WHAT}}':t['what']}.items():
        tpl = tpl.replace(key, value)
    if '{{' in tpl:
        raise ValueError('unfilled Bible discovery placeholder')
    return tpl


def parse_rows(path: Path) -> tuple[list[dict], list[str]]:
    if not path.exists():
        return [], [f'missing deliverable: {path}']
    rows, bad = [], []
    con = sqlite3.connect(f'file:{INDEX}?mode=ro', uri=True)
    try:
        for i, line in enumerate(path.read_text().splitlines(), 1):
            if not line.strip(): continue
            fields = [x.strip() for x in line.split('\t')]
            if len(fields) != 6:
                bad.append(f'line {i}: expected six fields'); continue
            strength, trad, kind, ref, basis, note = fields
            error = None
            if strength not in STRENGTH or trad not in TRAD or kind not in KIND or not all((ref,basis,note)):
                error = 'invalid/empty field'
            elif ref.startswith(('WLC:', 'SBLGNT:')):
                sid, osis = ref.split(':',1)
                if not OSIS.fullmatch(osis) or not con.execute('SELECT 1 FROM seg WHERE seg=?',(ref,)).fetchone():
                    error = f'unknown verse in specified edition: {ref}'
                elif trad != ('tevrat' if sid == 'WLC' else 'incil'):
                    error = f'{ref}: wrong tradition'
            elif OSIS.fullmatch(ref) or ref.startswith('KJV:') or re.fullmatch(r'\d+:\d+',ref):
                error = 'use WLC:<OSIS> or SBLGNT:<OSIS> in its own numbering'
            if error:
                bad.append(f'line {i}: {error}'); continue
            rows.append(dict(line=i,strength=strength,tradition=trad,kind=kind,ref=ref,basis=basis,note=note))
    finally:
        con.close()
    return rows, bad


def row_key(r: dict) -> tuple:
    return tuple(r[k] for k in ('tradition','kind','ref','basis','note'))


def checked_run(d: Path, t: dict) -> list[dict]:
    log = json.loads((d/'run.log.json').read_text())
    if (log.get('target'), log.get('runner'), log.get('model'), log.get('effort')) != (
            t['target'], 'agent', MODELS[d.name], EFFORT):
        raise ValueError(f'{d}: wrong target, model, effort or runner')
    if log.get('status') != 'ok' or not log.get('append_only') or not log.get('tool_audit_reviewed') or not log.get('turn2',{}).get('completed'):
        raise ValueError(f'{d}: not a completed, audited two-turn run')
    for filename, field in [('list.tsv','list_sha256'),('turn1.list.tsv','turn1_sha256'),
                            ('prompt.md','prompt_sha256'),('package.md','package_sha256')]:
        if digest(d/filename) != log.get(field):
            raise ValueError(f'{d}: {filename} changed since finish')
    if digest(Path(t['base_path'])) != log.get('base_sha256') or log['base_sha256'] != t['base_sha256']:
        raise ValueError(f'{d}: discovery used a different frozen base')
    if not (d/'list.tsv').read_bytes().startswith((d/'turn1.list.tsv').read_bytes()):
        raise ValueError(f'{d}: first-turn rows changed')
    rows, bad = parse_rows(d/'list.tsv')
    if bad or len({row_key(r) for r in rows}) != len(rows):
        raise ValueError(f'{d}: invalid/duplicate rows: {bad}')
    n = len((d/'turn1.list.tsv').read_bytes().splitlines())
    return [{**r,'turn':1 if r['line'] <= n else 2} for r in rows]


def write_handoff(path, rows, base_hash, provenance):
    fields = ['ref','tier','tradition','kinds','basis','explanations','target','evidence']
    stream = io.StringIO()
    writer = csv.DictWriter(stream,fields,delimiter='\t',lineterminator='\n')
    writer.writeheader(); writer.writerows(rows)
    path.write_text(stream.getvalue())
    target = path.name.removesuffix('.merged.tsv').replace('_', ':')
    save(path.with_suffix('.json'),dict(status='ok',target=target,base_sha256=base_hash,
         tsv_sha256=digest(path),provenance=provenance,rows=len(rows)))


def merge(s, targets, run_tag, models=None):
    if C.running_calls():
        raise ValueError('Bible page calls are active; do not change their discovery inputs')
    models = models or list(MODELS)
    root = discovery_dir(s,run_tag)
    order = {'strong':0,'medium':1,'weak':2}
    prepared = []
    for t in targets:  # validate all runs before writing handoffs
        per = {m:checked_run(tdir(s,t['target'],run_tag)/m,t) for m in models}
        groups = {}
        for m, records in per.items():
            for r in records:
                groups.setdefault((r['tradition'],r['ref']),[]).append({**r,'model':m})
        rows = []
        for (trad,ref), evidence in sorted(groups.items()):
            rows.append(dict(ref=ref,tier=min((r['strength'] for r in evidence),key=order.get),tradition=trad,
                kinds='|'.join(sorted({r['kind'] for r in evidence})),
                basis=' | '.join(dict.fromkeys(r['basis'] for r in evidence)),
                explanations=' | '.join(dict.fromkeys(r['note'] for r in evidence)),target=t['target'],
                evidence=json.dumps(evidence,ensure_ascii=False)))
        provenance = {m:digest(tdir(s,t['target'],run_tag)/m/'run.log.json') for m in models}
        prepared.append((t,rows,provenance))
    out, selection = [], {}
    selected = root.parent/'selected.json'
    if selected.exists(): selection = json.loads(selected.read_text())
    for t, rows, provenance in prepared:
        path = root/(t['target'].replace(':','_')+'.merged.tsv')
        write_handoff(path,rows,t['base_sha256'],provenance)
        selection[t['target']] = str(path.relative_to(root.parent)); out.append(path)
    sections = [x for x in prepared if x[0]['target'].startswith('sec')]
    expected = {t['target'] for t in targets_of(s) if t['target'].startswith('sec')}
    if sections and {t['target'] for t,_,_ in sections} == expected:
        path = root/'surah.merged.tsv'
        write_handoff(path,[r for _,rs,_ in sections for r in rs],sections[0][0]['base_sha256'],{t['target']:p for t,_,p in sections})
        selection['surah'] = str(path.relative_to(root.parent)); out.append(path)
    save(selected,selection)
    print(f'S{s}: merged {len(prepared)} targets; {len(out)} handoffs; models {", ".join(models)}')
    return out


def prefetch(merged, per_type):
    if C.running_calls():
        raise ValueError('Bible page calls are active; do not change their prefetched inputs')
    from enrichment.bible.fetch import bible_text as BT, bible_sefaria as SF
    candidates = {}
    for path in merged:
        for r in csv.DictReader(io.StringIO(path.read_text()),delimiter='\t'):
            candidates[(r['tradition'],r['ref'])] = r
    report = dict(lists={p.name:digest(p) for p in merged},candidates=[],errors=[],missing=[],source_hashes={},complete=False)
    for trad, ref in sorted(candidates):
        item = dict(ref=ref,tradition=trad,locators=[],related=[])
        try:
            if ref.startswith('WLC:'):
                b,ch,v = ref.split(':',1)[1].split('.')
                item['locators'] = [ref]
                result = SF.cmd_related(f'{BT.NAMES[b]} {ch}:{v}',['targum','midrash','talmud','commentary'],per_type)
            elif ref.startswith('SBLGNT:'):
                item['locators'] = [ref]; result = None
            elif trad == 'tevrat':
                named = ref.removeprefix('SEFARIA:').replace('_',' ') if ref.startswith('SEFARIA:') else ref
                result = SF.cmd_text([named]); item['locators'] = list(result['resolved'].values())
            else:
                result = None; report['missing'].append(ref)
            if result:
                item['related'] = list(result['resolved'].values()) if ref.startswith('WLC:') else []
                report['missing'].extend(result['missing']); report['errors'].extend(result['errors'])
            item['status'] = 'resolved' if item['locators'] else 'gap'
        except Exception as exc:
            item['status'] = 'failed'; report['errors'].append(dict(ref=ref,error=str(exc)))
        report['candidates'].append(item)
    for sid in ('WLC','SBLGNT','SEFARIA','CORPUSCORANICUM-INTERTEXT'):
        path = HERE/'corpus'/sid/'segments.jsonl'
        if path.exists(): report['source_hashes'][sid] = digest(path)
    report['complete'] = not report['errors']
    report['coverage_complete'] = report['complete'] and not report['missing']
    for root in {p.parent for p in merged}: save(root/'prefetch.json',report)
    for error in report['errors']: print(f'WARNING: Bible prefetch failed: {error}')
    for ref in dict.fromkeys(report['missing']): print(f'WARNING: Bible source gap: {ref}')
    print(f'prefetch: {len(candidates)} candidates; {len(report["missing"])} gaps; {len(report["errors"])} errors')
    return report


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--surah',type=int,required=True)
    ap.add_argument('--run-tag',required=True)
    ap.add_argument('--targets',help='N:A,secK,surah (surah selects every image section)')
    ap.add_argument('--models',default=','.join(MODELS))
    ap.add_argument('--merge',action='store_true')
    ap.add_argument('--prefetch',action='store_true')
    ap.add_argument('--per-type',type=int,default=6)
    ap.add_argument('--status',action='store_true')
    a = ap.parse_args()
    discovery_dir(a.surah,a.run_tag)  # validate before resolving any call paths
    models = a.models.split(',')
    if not models or any(m not in MODELS for m in models): ap.error('unknown model')
    targets = targets_of(a.surah)
    if a.targets:
        want = set(a.targets.split(','))
        unknown = want-{t['target'] for t in targets}-{'surah'}
        if unknown: ap.error(f'unknown/unavailable targets: {sorted(unknown)}')
        targets = [t for t in targets if t['target'] in want or ('surah' in want and t['target'].startswith('sec'))]
    if a.prefetch and not a.merge: ap.error('--prefetch requires --merge')
    if a.merge:
        merged = merge(a.surah,targets,a.run_tag,models)
        if a.prefetch and not prefetch(merged,a.per_type)['complete']: raise SystemExit(1)
        return
    q = json.loads((HERE/'work'/f's{a.surah:03d}'/'pack/quran.json').read_text())
    for t in targets:
        for model in models:
            d = tdir(a.surah,t['target'],a.run_tag)/model
            if a.status:
                log = d/'run.log.json'
                state = json.loads(log.read_text()).get('status') if log.exists() else 'started' if (d/'started.json').exists() else 'prepared' if (d/'prompt.md').exists() else '-'
                print(f'S{a.surah} {t["target"]} {model}: {state}'); continue
            if ((d/'started.json').exists() or (d/'run.log.json').exists()):
                print(f'NOTE: {d}: already started; never overwrite'); continue
            d.mkdir(parents=True,exist_ok=True)
            (d/'package.md').write_text(package(a.surah,t,q))
            (d/'prompt.md').write_text(prompt_text(a.surah,t,d))
            save(d/'input.json',{k:t[k] for k in ('target','base_path','base_sha256')})
    if not a.status: print(f'{len(targets)*len(models)} native sessions prepared; no model calls made. Use enrichment/bible/discovery_native.py.')

if __name__ == '__main__':
    main()
