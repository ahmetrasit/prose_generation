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
from enrichment.bible.fetch.bible_text import NAMES as BOOK_NAMES
MODELS = {'luna':'gpt-6-luna','terra':'gpt-5.6-terra','sol':'gpt-6-sol'}
EFFORT = 'max'  # the S1/S87 pair's effort
EFFORTS = {'luna':'max','terra':'max','sol':'high'}
# The two readers of an attempt are fixed when it is prepared (readers.json in the attempt directory). Attempts
# without that file are the S1/S87 Luna/Terra attempts. From 2026-10-09 new attempts use Luna max + Sol high
# (Terra has no saved rate, and the user requires costs; DECISIONS.md).
LEGACY_READERS = ('luna','terra')
PROTOCOL = 'bible-separate-proposals-v2'
HANDOFF = 'bible-discovery-v2'
REFERENCE_RESOLVER = 'edition-book-names-v2'
BOOK_CODES = {re.sub(r'\s+','',name).casefold():code for code,name in BOOK_NAMES.items()}
BOOK_CODES.update({code.casefold():code for code in BOOK_NAMES})
# Explicit, unambiguous conventional abbreviations. No fuzzy matching or
# chapter/verse correction is allowed in name resolution.
BOOK_CODES.update({'is':'Isa','jon':'Jonah','philem':'Phlm'})
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


def readers(s: int, run_tag: str) -> tuple:
    f = discovery_dir(s, run_tag) / 'readers.json'
    if not f.exists():
        return LEGACY_READERS
    r = tuple(json.loads(f.read_text())['readers'])
    if len(r) != 2 or len(set(r)) != 2 or any(m not in MODELS for m in r):
        raise ValueError(f'{f}: two distinct known readers required')
    return r


def tdir(s: int, target: str, run_tag: str) -> Path:
    if not re.fullmatch(r'(?:\d+:\d+|sec\d+)', target):
        raise ValueError(f'invalid discovery target {target}')
    return discovery_dir(s, run_tag) / target.replace(':', '_')


def targets_of(s: int) -> list[dict]:
    """Use the exact frozen pack, including augment9 for ayah discovery."""
    pk = R.V2 / 'work' / f's{s:03d}' / 'pack'
    bases = json.loads((pk / 'base.json').read_text())
    surah_name, surah_text, surah_info = R.target_page(s, 'surah')
    image_sections = sections.sections(surah_text)
    inputs = {str(pk/'base'/surah_name):surah_info['sha256'],
              str(pk/'quran.json'):digest(pk/'quran.json'), str(pk/'pack.json'):digest(pk/'pack.json')}
    out = []
    for ref, info in bases['ayat'].items():
        if info:
            name, text, _ = R.target_page(s, ref)
            kind = 'its frozen r13 commentary' if bases.get('ayah_base') == 'r13' else 'its augment9 commentary'
            out.append({'target':ref, 'ayat':[ref], 'prose':text, 'what':f'ayah {ref} with {kind}',
                        'base_path':str(pk/'base'/name), 'base_sha256':info['sha256'], 'inputs':inputs,
                        'members':[dict(m, image=sec['title']) for sec in image_sections
                                   for m in sec['members'] if m['ayah'] == ref]})
    for sec in image_sections:
        out.append({'target':f"sec{sec['k']}", 'ayat':sec['ayat'] or list(bases['ayat']), 'prose':sec['prose'],
                    'what':f"image section {sec['k']} ({sec['title']}) of the frozen surah commentary",
                    'base_path':str(pk/'base'/surah_name), 'base_sha256':surah_info['sha256'],
                    'inputs':inputs, 'members':sec['members']})
    return out


def package(s: int, t: dict, q: dict) -> str:
    lines = [f"# S{s}: {t['what']}", '', '## Ayat (Arabic)', '']
    lines += [f'{r}\t{q[r]}' for r in t['ayat']]
    lines += ['', '## Words, roots and branches named by the frozen surah commentary', '',
              'These are source labels, not dictionary definitions or verified cross-language cognates.', '',
              'ayah\tword\troot\tbranch\timage']
    lines += ['\t'.join(m.get(k,'') for k in ('ayah','word','root','branch','image')) for m in t.get('members',[])]
    if not t.get('members'): lines += ['(No lexical members recorded for this target.)']
    lines += ['', '## Semitic root table (Hebrew and Biblical Aramaic correspondences of the Arabic roots above)', '',
              'Generated by enrichment/bible/hebrew.py from the Open Scriptures lexicon and the WLC lemmas. A regular sound',
              'correspondence is a candidate, not proof of cognacy; "BDB cites an Arabic cognate" is the lexicon\'s own note.', '']
    lines += [semitic_table(t)]
    lines += ['', '## Frozen commentary (Turkish)', '', t['prose'].strip(), '', '## Whole surah (Arabic)', '']
    lines += [f'{r}\t{text}' for r, text in q.items() if r.startswith(f'{s}:')]
    return '\n'.join(lines) + '\n'


def target_roots(t: dict) -> list[str]:
    """Every Arabic root the frozen text of a target cites (dictionary labels) or its surah members name."""
    from enrichment.bible import hebrew
    return sorted(set(hebrew.roots_in(t['prose'])) | {m['root'] for m in t.get('members', []) if m.get('root')})


def semitic_table(t: dict) -> str:
    from enrichment.bible import hebrew
    roots = target_roots(t)
    return hebrew.table(roots) if roots else '(The frozen text of this target cites no Arabic root.)'


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
            raw_ref = ref
            error = None
            if strength not in STRENGTH or trad not in TRAD or kind not in KIND or not all((ref,basis,note)):
                error = 'invalid/empty field'
            elif ref.startswith(('WLC:', 'SBLGNT:')):
                sid, osis = ref.split(':',1)
                # A full book name and its OSIS code name the same book. Resolve
                # only that token: never alter the edition, chapter or verse.
                parts = osis.rsplit('.',2)
                if len(parts)==3:
                    book = BOOK_CODES.get(re.sub(r'\s+','',parts[0]).casefold(),parts[0])
                    osis = '.'.join([book,*parts[1:]])
                    ref = sid+':'+osis
                if not OSIS.fullmatch(osis) or not con.execute('SELECT 1 FROM seg WHERE seg=?',(ref,)).fetchone():
                    error = f'unknown verse in specified edition: {ref}'
                elif trad != ('tevrat' if sid == 'WLC' else 'incil'):
                    error = f'{ref}: wrong tradition'
            elif OSIS.fullmatch(ref) or ref.startswith('KJV:') or re.fullmatch(r'\d+:\d+',ref):
                error = 'use WLC:<OSIS> or SBLGNT:<OSIS> in its own numbering'
            if error:
                bad.append(f'line {i}: {error}'); continue
            row = dict(line=i,strength=strength,tradition=trad,kind=kind,ref=ref,basis=basis,note=note)
            if raw_ref != ref:
                row.update(raw_ref=raw_ref,reference_resolution=REFERENCE_RESOLVER)
            rows.append(row)
    finally:
        con.close()
    return rows, bad


def row_key(r: dict) -> tuple:
    return tuple(r[k] for k in ('tradition','kind','ref','basis','note'))


def connection_id(target: str, row: dict) -> str:
    data = json.dumps([target, *row_key(row)], ensure_ascii=False, separators=(',',':'))
    return 'BC-' + hashlib.sha256(data.encode()).hexdigest()[:20]


def checked_run(d: Path, t: dict) -> list[dict]:
    from enrichment.bible import discovery_native as N
    log = json.loads((d/'run.log.json').read_text())
    if (log.get('target'), log.get('model'), log.get('effort')) != (t['target'], MODELS[d.name], EFFORTS[d.name]) \
            or log.get('runner') not in ('agent', 'codex-exec'):
        raise ValueError(f'{d}: wrong target, model, effort or runner')
    if log.get('run_tag') != d.parent.parent.name:
        raise ValueError('run log belongs to a different attempt')
    if log.get('status') not in ('ok','accepted') or not log.get('append_only') or not log.get('tool_audit_reviewed') or not log.get('turn2',{}).get('completed'):
        raise ValueError(f'{d}: not a completed, audited two-turn run')
    N.verify_run(d, log)
    for filename, field in [('list.tsv','list_sha256'),('turn1.list.tsv','turn1_sha256'),
                            ('prompt.md','prompt_sha256'),('package.md','package_sha256')]:
        if digest(d/filename) != log.get(field):
            raise ValueError(f'{d}: {filename} changed since finish')
    if digest(Path(t['base_path'])) != log.get('base_sha256') or log['base_sha256'] != t['base_sha256']:
        raise ValueError(f'{d}: discovery used a different frozen base')
    if not (d/'list.tsv').read_bytes().startswith(N.initial_file(d).read_bytes()):
        raise ValueError(f'{d}: first-turn rows changed')
    rows, bad = parse_rows(d/'list.tsv')
    if bad or len({row_key(r) for r in rows}) != len(rows):
        raise ValueError(f'{d}: invalid/duplicate rows: {bad}')
    n = len((d/'turn1.list.tsv').read_bytes().splitlines())
    return [{**r,'turn':1 if r['line'] <= n else 2} for r in rows]


def write_handoff(path, rows, base_hash, provenance, findings=None):
    fields = ['ref','tier','tradition','kinds','basis','explanations','target','evidence']
    stream = io.StringIO()
    writer = csv.DictWriter(stream,fields,delimiter='\t',lineterminator='\n')
    writer.writeheader(); writer.writerows(rows)
    path.write_text(stream.getvalue())
    target = path.name.removesuffix('.merged.tsv').replace('_', ':')
    save(path.with_suffix('.json'),dict(format=HANDOFF,status='ok',target=target,base_sha256=base_hash,
         tsv_sha256=digest(path),provenance=provenance,rows=len(rows),findings=findings or [],
         confidence='Unverified reader labels; agreement and follow-up origin do not verify a connection.'))


def merge(s, targets, run_tag, models=None, attempts=None):
    if C.running_calls():
        raise ValueError('Bible page calls are active; do not change their discovery inputs')
    pair = set(readers(s,run_tag))
    models = models or sorted(pair)
    if set(models) != pair:
        raise ValueError(f'both {" and ".join(m.capitalize() for m in readers(s,run_tag))} are required for every merged target')
    root = discovery_dir(s,run_tag)
    attempts = attempts or {}
    for tag in set(attempts.values()):
        if set(readers(s,tag)) != pair:
            raise ValueError(f'attempt {tag} used other readers than {run_tag}')
    if set(attempts) - {t['target'] for t in targets}:
        raise ValueError('attempt selection names an unselected target')
    order = {'strong':0,'medium':1,'weak':2}
    prepared = []
    for t in targets:  # validate all runs before writing handoffs
        selected_tag = attempts.get(t['target'],run_tag)
        per = {m:checked_run(tdir(s,t['target'],selected_tag)/m,t) for m in models}
        groups = {}
        for m, records in per.items():
            for r in records:
                groups.setdefault((r['tradition'],r['ref']),[]).append({**r,'model':m,
                    'connection_id':connection_id(t['target'],r)})
        rows = []
        for (trad,ref), evidence in sorted(groups.items()):
            rows.append(dict(ref=ref,tier=min((r['strength'] for r in evidence),key=order.get),tradition=trad,
                kinds='|'.join(sorted({r['kind'] for r in evidence})),
                basis=' | '.join(dict.fromkeys(r['basis'] for r in evidence)),
                explanations=' | '.join(dict.fromkeys(r['note'] for r in evidence)),target=t['target'],
                evidence=json.dumps(evidence,ensure_ascii=False)))
        provenance, findings = [], []
        for m in models:
            d = tdir(s,t['target'],selected_tag)/m
            log = json.loads((d/'run.log.json').read_text())
            provenance.append(dict(target=t['target'],model=m,run_tag=selected_tag,
                                   path=str(d.relative_to(root.parent)),sha256=digest(d/'run.log.json')))
            findings.append(dict(target=t['target'],model=m,validation=json.loads((d/'validation.json').read_text()),
                                 raw_proposal_validation=json.loads((d/'proposal_validation.json').read_text()),
                                 repeats=log['consolidation']['repeated_proposals'],
                                 diagnostics=log['tool_diagnostics'],repair=log.get('repair'),
                                 first_turn_repair=log.get('first_turn_repair')))
        prepared.append((t,rows,provenance,findings))
    root.mkdir(parents=True,exist_ok=True)
    out, selection = [], {}
    selected = root.parent/'selected.json'
    if selected.exists(): selection = json.loads(selected.read_text())
    for t, rows, provenance, findings in prepared:
        path = root/(t['target'].replace(':','_')+'.merged.tsv')
        write_handoff(path,rows,t['base_sha256'],provenance,findings)
        selection[t['target']] = str(path.relative_to(root.parent)); out.append(path)
    sections = [x for x in prepared if x[0]['target'].startswith('sec')]
    expected = {t['target'] for t in targets_of(s) if t['target'].startswith('sec')}
    if sections and {t['target'] for t,_,_,_ in sections} == expected:
        path = root/'surah.merged.tsv'
        write_handoff(path,[r for _,rs,_,_ in sections for r in rs],sections[0][0]['base_sha256'],
                      [p for _,_,ps,_ in sections for p in ps], [f for _,_,_,fs in sections for f in fs])
        selection['surah'] = str(path.relative_to(root.parent)); out.append(path)
    save(selected,selection)
    print(f'S{s}: merged {len(prepared)} targets; {len(out)} handoffs; models {", ".join(models)}')
    return out


def verify_handoff(path, s, target):
    """Require both readers and recheck their complete artifact chains at page build."""
    meta = json.loads(path.with_suffix('.json').read_text())
    if meta.get('format') != HANDOFF or meta.get('tsv_sha256') != digest(path):
        raise ValueError('Bible handoff needs the current audited discovery protocol')
    current = {t['target']:t for t in targets_of(s)}
    required = {k for k in current if k.startswith('sec')} if target == 'surah' else {target}
    tags = {p.get('run_tag') for p in meta.get('provenance',[])}
    pairs = {readers(s,tag) for tag in tags if tag}
    if len(pairs) != 1:
        raise ValueError('discovery provenance mixes reader pairs or names no attempt')
    pair = pairs.pop()
    expected = {(k,m) for k in required for m in pair}
    seen, files = set(), []
    root = HERE/'work'/f's{s:03d}'/'discovery'
    for p in meta.get('provenance',[]):
        key = (p['target'],p['model'])
        if key not in expected or key in seen:
            raise ValueError('unexpected/duplicate discovery provenance')
        seen.add(key)
        d = (root/p['path']).resolve()
        if d != tdir(s,p['target'],p['run_tag']).joinpath(p['model']).resolve():
            raise ValueError('discovery provenance path differs from selected attempt')
        if digest(d/'run.log.json') != p['sha256']:
            raise ValueError('discovery log changed after merge')
        checked_run(d,current[p['target']])
        log = json.loads((d/'run.log.json').read_text())
        files += [d/'run.log.json', *[d/name for name in log['artifacts']]]
    if seen != expected:
        raise ValueError('both readers must complete every selected discovery target')
    return files


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
    ap.add_argument('--models',help='default: the attempt\'s two readers')
    ap.add_argument('--readers',help='prepare only: the two readers of a new attempt, e.g. luna,sol (default luna,terra '
                    'for attempts without readers.json)')
    ap.add_argument('--selection',type=Path,help='JSON mapping target to explicit completed run tag for merge')
    ap.add_argument('--merge',action='store_true')
    ap.add_argument('--prefetch',action='store_true')
    ap.add_argument('--per-type',type=int,default=6)
    ap.add_argument('--status',action='store_true')
    a = ap.parse_args()
    root = discovery_dir(a.surah,a.run_tag)  # validate before resolving any call paths
    if a.readers:
        if a.merge or a.status: ap.error('--readers is for preparing an attempt')
        pair = a.readers.split(',')
        if len(pair) != 2 or len(set(pair)) != 2 or any(m not in MODELS for m in pair): ap.error('two distinct known readers')
        f = root/'readers.json'
        if f.exists() and sorted(json.loads(f.read_text())['readers']) != sorted(pair):
            ap.error(f'{f} names other readers; use a fresh run tag')
        if not f.exists() and root.exists() and any(root.iterdir()):
            ap.error(f'{root} was prepared without readers.json; use a fresh run tag')
        root.mkdir(parents=True,exist_ok=True)
        if not f.exists(): save(f,{'readers':pair})
    models = a.models.split(',') if a.models else list(readers(a.surah,a.run_tag))
    if not models or any(m not in MODELS for m in models): ap.error('unknown model')
    targets = targets_of(a.surah)
    if a.targets:
        want = set(a.targets.split(','))
        unknown = want-{t['target'] for t in targets}-{'surah'}
        if unknown: ap.error(f'unknown/unavailable targets: {sorted(unknown)}')
        targets = [t for t in targets if t['target'] in want or ('surah' in want and t['target'].startswith('sec'))]
    if a.prefetch and not a.merge: ap.error('--prefetch requires --merge')
    if a.selection and not a.merge: ap.error('--selection requires --merge')
    if a.merge:
        attempts = json.loads(a.selection.read_text()) if a.selection else None
        merged = merge(a.surah,targets,a.run_tag,models,attempts)
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
            save(d/'input.json',{k:t[k] for k in ('target','base_path','base_sha256','inputs')})
    if not a.status: print(f'{len(targets)*len(models)} reader sessions prepared ({", ".join(models)}); no model calls made. '
                           'Run them with enrichment/bible/discovery_exec.py (Claude Code) or discovery_native.py.')

if __name__ == '__main__':
    main()
