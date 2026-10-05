#!/usr/bin/env python3
"""Bible-only, opt-in Sol max surah authors: one frozen image per native session.

Uses the available local witnesses. Missing secondary sources are explicitly
unfetched gaps, not successful retrievals. Scripts never launch models.
"""
from __future__ import annotations

import argparse
from collections import Counter
from contextlib import closing
import copy
import json
from pathlib import Path
import re
import shlex
import sqlite3
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from enrichment.bible import corpus as C, discovery as D, discovery_sessions as N
from enrichment.bible import enrich as E, render as R, sections as S, validate as V, verdicts as VR

MODEL = 'gpt-6-sol'
EFFORT = 'max'
PROTOCOL = 'bible-image-author-v1'
OUTPUTS = ('annotations.jsonl', 'verdicts.jsonl', 'gaps.json')


def read_json(path):
    return json.loads(path.read_text())


def save_jsonl(path, rows):
    path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))


def run_dir(s, run_tag):
    D.discovery_dir(s, run_tag)  # validate the tag
    return E.wd(s) / f'ehlikitap-images.sol.max.{run_tag}'


def image_layout(base):
    """Global paragraph numbers and exact source spans; require complete coverage."""
    images = S.sections(base)
    paras = R.paragraphs(base)
    positions, cursor = {}, 0
    for n, index in R.prose_index(paras).items():
        p = paras[index]
        pos = base.find(p, cursor)
        if pos < 0:
            raise ValueError('cannot place a frozen paragraph')
        positions[n] = pos
        cursor = pos + len(p)
    covered = []
    for item in images:
        nums = [n for n, pos in positions.items() if item['start'] <= pos < item['end']]
        if not nums:
            raise ValueError(f"image {item['k']} has no prose paragraphs")
        item['paragraphs'] = nums
        item['numbered'] = f"## {item['title']}\n\n" + '\n\n'.join(
            f'[¶{n}] {paras[R.prose_index(paras)[n]]}' for n in nums) + '\n'
        covered.extend(nums)
    if sorted(covered) != list(positions):
        raise ValueError('image boundaries do not cover every prose paragraph exactly once')
    return images


def source_inputs(s):
    """Freeze the current index, sources, pack and full audited discovery chain."""
    path = E.discovery_list(s, 'surah')
    if path is None:
        raise ValueError('no selected full-surah Bible discovery')
    _, base, info = R.target_page(s, 'surah')
    meta = read_json(path.with_suffix('.json'))
    if meta.get('base_sha256') != info['sha256'] or meta.get('target') != 'surah':
        raise ValueError('discovery belongs to a different surah base')
    files = [path, path.with_suffix('.json'), E.wd(s)/'discovery/selected.json',
             *D.verify_handoff(path, s, 'surah')]
    index = C.INDEX_INTERTEXT
    manifest = index.with_suffix('.manifest.json')
    indexed = read_json(manifest)
    if indexed.get('format') != 'intertext-2' or indexed.get('index_sha256') != D.digest(index):
        raise ValueError('rebuild the Bible index before preparing image authors')
    if not {'WLC', 'SBLGNT', 'QURAN'}.issubset(indexed.get('source_hashes', {})):
        raise ValueError('WLC, SBLGNT and QURAN are required')
    files += [index, manifest]
    for field, filename in [('source_hashes', 'segments.jsonl'), ('metadata_hashes', 'source.json')]:
        if not indexed.get(field):
            raise ValueError(f'index lacks {field}')
        for sid, digest in indexed[field].items():
            p = C.CORPUS/sid/filename
            if D.digest(p) != digest:
                raise ValueError(f'rebuild index: {sid}/{filename} changed')
            files.append(p)
    pack = E.wd(s)/'pack'
    pm = read_json(pack/'pack.json')
    files.append(pack/'pack.json')
    for name, digest in pm['files'].items():
        p = pack/name
        if D.digest(p) != digest:
            raise ValueError(f'frozen pack changed: {name}')
        files.append(p)
    return path, base, info, {E.rel(p): D.digest(p) for p in files}


def local_sources(candidates):
    """Report local availability, without claiming that absent sources were fetched."""
    refs = sorted({r['ref'] for r in candidates.values()})
    rows = []
    with closing(sqlite3.connect(f'file:{C.INDEX_INTERTEXT}?mode=ro', uri=True)) as con:
        for ref in refs:
            found = con.execute('SELECT seg FROM seg WHERE seg=?', (ref,)).fetchone()
            # Only a locator-identical source is resolved. Never guess a work or verse.
            if not found and ref.startswith(('WLC:', 'SBLGNT:')):
                raise ValueError(f'canonical discovery verse is missing: {ref}')
            rows.append(dict(ref=ref, status='local' if found else 'not_in_local_snapshot',
                             locators=[ref] if found else []))
    return dict(mode='available-local-witnesses', network_attempted=False,
                coverage_complete=all(r['locators'] for r in rows),
                missing=[r['ref'] for r in rows if not r['locators']], candidates=rows,
                limitation='Absent works were not fetched or searched in this run; do not call them nonexistent.')


def prepare(s, run_tag):
    root = run_dir(s, run_tag)
    if root.exists():
        raise ValueError('run directory already exists; use a fresh run tag')
    if E.accepted(s, 'surah'):
        raise ValueError('a Bible surah page is already accepted')
    handoff, base, info, inputs = source_inputs(s)
    images = image_layout(base)
    all_expected = VR.candidates(handoff)
    quran = read_json(E.wd(s)/'pack/quran.json')
    jobs = []
    prepared = []
    for sec in images:
        target = f"sec{sec['k']}"
        selected = E.discovery_list(s, target)
        if selected is None:
            raise ValueError(f'no selected handoff for {target}')
        candidates = VR.candidates(selected)
        if candidates != {k:v for k,v in all_expected.items() if v['target'] == target}:
            raise ValueError(f'{target} differs from the full-surah discovery')
        D.verify_handoff(selected, s, target)
        for p in [selected, selected.with_suffix('.json')]:
            inputs[E.rel(p)] = D.digest(p)
        prepared.append((sec, selected, candidates, local_sources(candidates)))
    root.mkdir(parents=True)
    (root/'discovery.merged.tsv').write_bytes(handoff.read_bytes())
    D.save(root/'prefetch.json', local_sources(all_expected))
    template = (E.PROMPTS/'image_author.md').read_text()
    rules = (E.PROMPTS/'common.md').read_text() + '\n' + (E.PROMPTS/'ehlikitap.md').read_text()
    for sec, selected, candidates, sources in prepared:
        target = f"sec{sec['k']}"
        d = root/target
        d.mkdir()
        task = f"bible_s{s:03d}_{run_tag.replace('-', '_')}_{target}_sol"
        (d/'discovery.merged.tsv').write_bytes(selected.read_bytes())
        (d/'discovery.merged.json').write_bytes(selected.with_suffix('.json').read_bytes())
        (d/'base.md').write_text(sec['numbered'])
        D.save(d/'quran.json', quran)
        D.save(d/'prefetch.json', sources)
        save_jsonl(d/'candidates.jsonl', [dict(connection_id=k, **v) for k,v in candidates.items()])
        (d/'rules.md').write_text(rules)
        (d/'schema.md').write_bytes((E.V2/'SCHEMA_BIBLE_CARD.md').read_bytes())
        job = dict(surah=s, target=target, section=sec['k'], title=sec['title'],
                   paragraphs=sec['paragraphs'], agent_path='/root/'+task, task=task,
                   model=MODEL, effort=EFFORT, protocol=PROTOCOL, directory=E.rel(d),
                   connections=len(candidates), missing_sources=len(sources['missing']))
        prompt = template.replace('{{DIRECTORY}}', str(d)).replace('{{SURAH}}', str(s)).replace(
            '{{SECTION}}', target).replace('{{PARAGRAPHS}}', ', '.join(map(str, sec['paragraphs']))).replace(
            '{{ROOT}}', str(E.PG)).replace('{{COUNT}}', str(len(candidates)))
        (d/'prompt.md').write_text(prompt)
        spawn = f'Read {d}/prompt.md completely and follow it. You are the independent Sol max Bible author for S{s} {target}. '
        spawn += 'Use only the named Bible inputs and tools, and write only the permitted deliverables in your call directory. '
        spawn += 'Do not spawn or consult other agents. Complete verification and writing in this session.\n'
        (d/'spawn.md').write_text(spawn)
        frozen = {p.name:D.digest(p) for p in d.iterdir() if p.is_file()}
        D.save(d/'started.json', dict(**job, frozen=frozen, started_at=time.strftime('%Y-%m-%dT%H:%M:%S%z')))
        jobs.append(job)
    row = dict(surah=s, target='surah', model=MODEL, effort=EFFORT, protocol=PROTOCOL,
               source_mode='available-local-witnesses', network_attempted=False, jobs=jobs,
               base_sha256=info['sha256'], pack_sha256=D.digest(E.wd(s)/'pack/pack.json'),
               bible_inputs=inputs, discovery=E.rel(handoff),
               root_frozen={name:D.digest(root/name) for name in ('discovery.merged.tsv','prefetch.json')})
    D.save(root/'started.json', row)  # also locks the corpus against mutation
    return dict(directory=E.rel(root), agents=len(jobs), connections=len(all_expected), jobs=jobs)


def frozen_ok(d):
    job = read_json(d/'started.json')
    root = read_json(d.parent/'started.json')
    E.verify_bible_inputs(root)
    for name, digest in root['root_frozen'].items():
        if D.digest(d.parent/name) != digest:
            raise ValueError(f'run input changed: {name}')
    for name, digest in job['frozen'].items():
        if D.digest(d/name) != digest:
            raise ValueError(f'image input changed: {name}')
    return job


def output_text(output):
    if isinstance(output, list):
        return '\n'.join(output_text(x) for x in output)
    if isinstance(output, dict):
        return str(output.get('text', ''))
    return str(output or '')


def bootstrap_object(raw):
    """Literal-only object syntax for the initial prompt read, before rules are visible."""
    decoder = json.JSONDecoder()
    pos, result = 1, {}
    if not raw.startswith('{'): raise ValueError('expected a literal object')
    while True:
        while pos < len(raw) and raw[pos].isspace(): pos += 1
        if pos >= len(raw): raise ValueError('unterminated object')
        if raw[pos] == '}':
            if raw[pos+1:].strip(): raise ValueError('trailing object code')
            return result
        if raw[pos] == '"': key, pos = decoder.raw_decode(raw, pos)
        else:
            match = re.match(r'[A-Za-z_]\w*', raw[pos:])
            if not match: raise ValueError('invalid literal key')
            key = match[0]; pos += len(key)
        while pos < len(raw) and raw[pos].isspace(): pos += 1
        if pos >= len(raw) or raw[pos] != ':' or key in result: raise ValueError('invalid/duplicate key')
        pos += 1
        while pos < len(raw) and raw[pos].isspace(): pos += 1
        value, pos = decoder.raw_decode(raw, pos)
        result[key] = value
        while pos < len(raw) and raw[pos].isspace(): pos += 1
        if pos >= len(raw) or raw[pos] not in ',}': raise ValueError('nonliteral object value')
        if raw[pos] == ',': pos += 1


def unwrap_call(name, arguments, bootstrap=False):
    """Small explicit wrapper grammar; never evaluate agent-supplied JavaScript."""
    name = name.split('.')[-1]
    if name in ('exec_command', 'apply_patch'):
        return name, json.loads(arguments) if name == 'exec_command' else arguments
    if name != 'exec':
        raise ValueError(f'unsupported tool: {name}')
    if re.fullmatch(r'\s*const r\s*=\s*await tools\.clock__curr_time\(\{\}\);\s*text\(r\.current_time\);?\s*',arguments):
        return 'clock', {}
    command = re.fullmatch(r'\s*const r\s*=\s*await tools\.exec_command\((\{[\s\S]*\})\);\s*text\(r\.output\);?\s*', arguments)
    if command:
        return 'exec_command', bootstrap_object(command[1]) if bootstrap else json.loads(command[1])
    patch = re.fullmatch(r'\s*text\(await tools\.apply_patch\(("[\s\S]*")\)\);?\s*', arguments)
    if patch:
        return 'apply_patch', json.loads(patch[1])
    raise ValueError('unsupported orchestration wrapper; use the exact prompt forms')


def allowed_patch(patch, d):
    writes = []
    for line in patch.splitlines():
        m = re.match(r'\*\*\* (?:Add File|Update File|Delete File|Move to): (.+)$', line)
        if m:
            p = Path(m[1])
            if not p.is_absolute(): p = E.PG/p
            writes.append(p.resolve())
    allowed = {d/name for name in (*OUTPUTS, 'notes.md')}
    return bool(writes) and all(p in allowed for p in writes)


def allowed_command(cmd, d):
    if re.search(r'[;&|<>`$\n\r]', cmd):
        return False
    try: args = shlex.split(cmd)
    except ValueError: return False
    if not args: return False
    if args[0] == 'cat':
        paths = args[1:]
    elif args[:2] == ['sed', '-n'] and len(args) == 4 and re.fullmatch(r'\d+,\d+p', args[2]):
        paths = args[3:]
    else:
        paths = None
    if paths is not None:
        resolved=[(Path(p) if Path(p).is_absolute() else E.PG/p).resolve() for p in paths]
        return bool(paths) and all(p.parent == d or p == d/'preview/surah.md' for p in resolved)
    if len(args) < 3 or args[0] not in ('python3', sys.executable): return False
    script = Path(args[1])
    if not script.is_absolute(): script = E.PG/script
    if script.resolve().parent != E.V2: return False
    tail = args[2:]
    if script.name == 'corpus.py':
        if tail[0] == '--intertext': tail = tail[1:]
        return bool(tail) and tail[0] in ('get','search','ayah','sources')
    if script.name == 'image_enrich.py':
        return tail == ['check','--dir',str(d)]
    return False


def audit_turns(d, session, events, done):
    """Keep interrupted/failed attempts visible; one successful author completion."""
    from enrichment.bible import discovery_native as DN
    successful=[e for e in done if not e['payload'].get('error')]
    failed=[e['payload'] for e in events if e.get('type')=='event_msg' and
            (e.get('payload',{}).get('type')=='turn_aborted' or
             (e.get('payload',{}).get('type') in ('task_complete','task_completed') and e['payload'].get('error')))]
    errors=[];proof=[]
    if len(successful)!=1: errors.append(f'expected one successful native completion, found {len(successful)}')
    if failed:
        try:
            resumed=read_json(d/'resume.json')
            job=read_json(d/'started.json')
            if resumed.get('failures')!=failed or resumed.get('successful_turns_before')!=0:
                raise ValueError('resume record does not match the unfinished native history')
            if (resumed.get('model'),resumed.get('effort'),resumed.get('agent_path'))!=(MODEL,EFFORT,job['agent_path']):
                raise ValueError('resume identity/model differs')
            if not resumed.get('authorized_by') or D.digest(d/'resume-message.txt')!=resumed.get('message_sha256'):
                raise ValueError('missing or changed resume authorization/message')
            if (d/'resume-message.txt').read_text().strip()!=resumed['message']:
                raise ValueError('resume message differs')
            proof=DN.followup_proof(session,events,resumed['message'])
            if len(proof)!=1 or not (proof[0].get('matches') or proof[0].get('encrypted')):
                raise ValueError('missing exact same-session resume delivery')
        except (OSError,ValueError,KeyError,TypeError) as exc:
            errors.append(str(exc))
    return errors,dict(successful_completions=len(successful),unfinished_attempts=failed,resume_delivery=proof)


def native_audit(d):
    job = frozen_ok(d)
    session, events, done, contexts, usage = N.events_for(d)
    errors, turn_history = audit_turns(d,session,events,done)
    normalized = []
    if not contexts or any(c.get('model') != MODEL or c.get('effort') != EFFORT for c in contexts):
        errors.append('unexpected native model or effort')
    calls, diagnostics = N.tool_audit(events, done[0]['timestamp'] if done else '9999')
    for ordinal, call in enumerate(calls):
        try:
            kind, inp = unwrap_call(call['name'], call['arguments'], bootstrap=ordinal==0)
            if kind == 'exec_command':
                if inp.get('workdir', str(E.PG)) != str(E.PG) or not allowed_command(inp.get('cmd',''), d):
                    raise ValueError('command outside Bible image rules')
                if ordinal == 0:
                    args = shlex.split(inp['cmd'])
                    p = Path(args[-1])
                    if not p.is_absolute(): p = E.PG/p
                    if len(args)!=2 or args[0]!='cat' or p.resolve()!=d/'prompt.md':
                        raise ValueError('initial bootstrap may only read this image prompt')
                normalized.append(dict(name='Bash', input={'command':inp['cmd']}, result=output_text(call['output']),
                                       is_error=False, call_id=call['call_id']))
            elif kind == 'apply_patch' and not allowed_patch(inp, d):
                raise ValueError('patch outside image deliverables')
        except (ValueError, TypeError, KeyError) as exc:
            errors.append(f"{call['call_id']}: {exc}")
    D.save(d/'native-tool-calls.json', calls)
    D.save(d/'tool_calls.json', normalized)
    (d/'session.events.jsonl').write_text(''.join(json.dumps(e,ensure_ascii=False)+'\n' for e in events))
    return dict(ok=not errors, errors=errors, session=session, completed_turns=len(done),
                turn_history=turn_history,
                contexts=[dict(model=c.get('model'),effort=c.get('effort')) for c in contexts],
                usage_tokens=usage, diagnostics=diagnostics, calls=len(calls),
                cost_basis='Codex subscription; no per-call dollar charge recorded'), normalized


def check(d, final=False, calls=None):
    job = read_json(d/'started.json')
    s = job['surah']
    records = R.load(d/'annotations.jsonl')
    kept, dropped, warnings = V.check_records(s, 'surah', records)
    base = R.target_page(s, 'surah')[1]
    report = VR.check(d, d/'discovery.merged.tsv', base, kept, calls=calls or [], require_opened=final)
    allowed = set(job['paragraphs'])
    for r in kept:
        if int(str(r['paragraf']).strip().lstrip('¶')) not in allowed:
            report['errors'].append(f"{r['id']}: annotation outside assigned image")
    for row in R.load(d/'verdicts.jsonl'):
        if not set(row.get('paragraphs', [])).issubset(allowed):
            report['errors'].append(f"{row.get('connection_id') or row.get('ref')}: verdict outside assigned image")
    if dropped: report['errors'].append(f'{len(dropped)} invalid annotations')
    if not records and not read_json(d/'gaps.json').get('no_findings_reason'):
        report['errors'].append('empty annotations require no_findings_reason')
    counts = Counter(str(r['paragraf']) for r in kept)
    if any(n > 5 for n in counts.values()): report['errors'].append('more than five annotations after a paragraph')
    page, placement = R.render(s, 'surah', kept, d/'preview')
    page_errors = V.check_page(page, base, kept) + placement
    report['errors'].extend(page_errors)
    report.update(ok=not report['errors'], records=len(records), kept=len(kept), dropped=dropped, warnings=warnings)
    D.save(d/('verdict_report.json' if final else 'draft_report.json'), report)
    return report


def finish(d):
    if (d/'run.log.json').exists():
        raise ValueError('image was already finished')
    audit, calls = native_audit(d)
    report = check(d, final=True, calls=calls)
    result = dict(status='ok' if audit['ok'] and report['ok'] else 'failed', audit=audit, check=report)
    result['artifacts'] = {p.name:D.digest(p) for p in d.iterdir() if p.is_file() and p.name != 'run.log.json'}
    D.save(d/'run.log.json', result)
    return result


def assemble(s, run_tag):
    root = run_dir(s, run_tag)
    if (root/'run.log.json').exists(): raise ValueError('run was already assembled')
    started = read_json(root/'started.json')
    records, discovery_rows, research, calls, sections = [], [], {}, [], []
    gaps = dict(missing_sources=[], not_found=[], unresolved=[])
    counters = Counter()
    for job in started['jobs']:
        d = root/job['target']
        frozen_ok(d)
        log = read_json(d/'run.log.json')
        if log['status'] != 'ok': raise ValueError(f"{job['target']}: failed image cannot be assembled")
        for name, digest in log['artifacts'].items():
            if D.digest(d/name) != digest: raise ValueError(f"{job['target']}: changed accepted artifact {name}")
        # Recheck per-image evidence before combining; evidence cannot be borrowed from another author.
        local_calls = read_json(d/'tool_calls.json')
        if not check(d, final=True, calls=local_calls)['ok']:
            raise ValueError(f"{job['target']}: image no longer passes")
        mapping = {}
        for record in R.load(d/'annotations.jsonl'):
            row = copy.deepcopy(record)
            prefix = row['id'].rsplit('-',1)[0]
            counters[prefix] += 1
            if counters[prefix] > 999: raise ValueError('annotation namespace exhausted')
            mapping[row['id']] = f'{prefix}-{counters[prefix]:03d}'
            row['id'] = mapping[row['id']]
            records.append(row)
        for row in R.load(d/'verdicts.jsonl'):
            row['annotations'] = [mapping[x] for x in row['annotations']]
            if row.get('connection_id'):
                discovery_rows.append(row)
            else:
                research.setdefault(row['ref'], []).append(dict(section=job['target'], verdict=row))
                discovery_rows.append(dict(row, scope=job['target']))
        for key in gaps:
            gaps[key].extend(read_json(d/'gaps.json')[key])
        calls.extend(local_calls)
        sections.append(dict(target=job['target'], run_log_sha256=D.digest(d/'run.log.json'), id_map=mapping))
    # A context verse may support different decisions in different images. Keep
    # each decision unchanged, namespaced by its already-validated image scope.
    for key in gaps:
        unique = {json.dumps(x,ensure_ascii=False,sort_keys=True):x for x in gaps[key]}
        gaps[key] = list(unique.values())
    if not records: gaps['no_findings_reason'] = 'All image authors recorded explicit empty findings; see their individual gap ledgers.'
    save_jsonl(root/'annotations.jsonl', records)
    save_jsonl(root/'verdicts.jsonl', discovery_rows)
    D.save(root/'gaps.json', gaps)
    D.save(root/'tool_calls.json', calls)
    D.save(root/'assembly.json', dict(sections=sections, research_decisions=research))
    kept, dropped, warnings = V.check_records(s, 'surah', records)
    base = R.target_page(s, 'surah')[1]
    verdict = VR.check(root,root/'discovery.merged.tsv',base,kept,calls=calls,
                       research_scopes={j['target'] for j in started['jobs']})
    if dropped or not verdict['ok']:
        D.save(root/'assembly.failed.json',dict(dropped=dropped,verdict=verdict))
        raise ValueError('combined annotations or verdicts failed validation')
    D.save(root/'verdict_report.json', verdict)
    page, errors = R.render(s,'surah',kept,root/'page')
    errors += V.check_page(page,base,kept)
    if errors: raise ValueError(f'combined page errors: {errors}')
    out = E.OUT/f's{s:03d}'
    out.mkdir(parents=True, exist_ok=True)
    destination = out/'surah.ehlikitap.md'
    if destination.exists(): raise ValueError('never overwrite an accepted Bible page')
    snapshots = {}
    for name in (*OUTPUTS, 'verdict_report.json','assembly.json'):
        dst = destination.with_suffix('.'+name)
        if dst.exists(): raise ValueError(f'acceptance snapshot already exists: {dst}')
        with dst.open('xb') as f: f.write((root/name).read_bytes())
        snapshots[name] = dict(path=E.rel(dst),sha256=D.digest(dst))
    errata = [r for r in kept if r.get('tur')=='duzeltme']
    if errata:
        seen = set()
        if E.ERRATA.exists():
            for line in E.ERRATA.read_text().splitlines():
                try:
                    row=json.loads(line)
                    seen.add((row.get('surah'),row.get('target'),row.get('id'),row.get('taban')))
                except ValueError: continue
        with E.ERRATA.open('a') as f:
            for r in errata:
                if (s,'surah',r['id'],r.get('taban')) in seen: continue
                f.write(json.dumps(dict(surah=s,target='surah',base=R.target_page(s,'surah')[2]['path'],
                     id=r['id'],taban=r.get('taban'),hata=r.get('hata'),metin=r.get('metin'),kaynak=r.get('kaynak')),
                     ensure_ascii=False)+'\n')
    with destination.open('xb') as f: f.write(page.read_bytes())
    meta = dict(surah=s,target='surah',protocol=PROTOCOL,model=MODEL,effort=EFFORT,
                base=R.target_page(s,'surah')[2],page_sha256=D.digest(destination),kept=len(kept),dropped=[],
                annotations=E.rel(root/'annotations.jsonl'),accepted_annotations=snapshots['annotations.jsonl']['path'],
                annotations_sha256=snapshots['annotations.jsonl']['sha256'],
                verdict_artifacts={k:v for k,v in snapshots.items() if k!='annotations.jsonl'},
                bible_inputs=started['bible_inputs'], source_mode=started['source_mode'],
                network_attempted=False, accepted_at=time.strftime('%Y-%m-%dT%H:%M:%S%z'), sections=sections)
    D.save(destination.with_suffix('.json'), meta)
    result = dict(status='ok',surah=s,images=len(sections),annotations=len(kept),warnings=warnings,
                  verdicts=verdict['verdicts'],status_counts=verdict['status_counts'],page=E.rel(destination),
                  errata=len(errata))
    D.save(root/'run.log.json', result)
    E.log(dict(**result,model='sol',model_id=MODEL,effort=EFFORT,brief='ehlikitap',target='surah',protocol=PROTOCOL))
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('phase', choices=('prepare','check','finish','assemble','status'))
    ap.add_argument('--surah',type=int)
    ap.add_argument('--run-tag')
    ap.add_argument('--dir',type=Path)
    a = ap.parse_args()
    if a.phase in ('check','finish'):
        if not a.dir: ap.error('--dir is required')
        result = check(a.dir.resolve()) if a.phase=='check' else finish(a.dir.resolve())
    else:
        if not a.surah or not a.run_tag: ap.error('--surah and --run-tag are required')
        if a.phase=='prepare': result=prepare(a.surah,a.run_tag)
        elif a.phase=='assemble': result=assemble(a.surah,a.run_tag)
        else:
            root=run_dir(a.surah,a.run_tag)
            result=[dict(target=j['target'], status=read_json(root/j['target']/'run.log.json')['status']
                         if (root/j['target']/'run.log.json').exists() else 'pending') for j in read_json(root/'started.json')['jobs']]
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if isinstance(result,dict) and (result.get('ok') is False or result.get('status')=='failed'): raise SystemExit(1)


if __name__ == '__main__': main()
