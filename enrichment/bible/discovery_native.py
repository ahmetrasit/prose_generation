#!/usr/bin/env python3
"""Bookkeeping for two-turn native Bible discovery agents. Never calls a model."""
import argparse
import json
import re
from datetime import datetime
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from enrichment.bible import discovery as D, discovery_sessions as N


ARTIFACTS = ('started.json','input.json','prompt.md','package.md','spawn.md','followup.txt',
             'turn1.json','turn1.list.tsv','followup.tsv','list.tsv','consolidation.json',
             'validation.json','proposal_validation.json','tool_calls.json','session.json','session.events.jsonl')
REPAIR_ARTIFACTS = ('run.failed.log.json','validation.failed.json','repair.proposed.json',
                    'followup.repair.proposed.tsv','followup.accepted.tsv','repair.accepted.json')


def initial_file(d):
    if (d/'turn1.repair.accepted.json').exists() or (d/'turn1.accepted.tsv').exists():
        from enrichment.bible import discovery_first_repair as repair
        repair.verify(d)
        return d/'turn1.accepted.tsv'
    return d/'turn1.list.tsv'


def consolidation_plan(d, proposals_file='followup.tsv'):
    """Replayable, lossless consolidation; reference grouping happens only at handoff."""
    if proposals_file not in ('followup.tsv','followup.accepted.tsv'):
        raise ValueError('unsupported proposal file')
    initial_path = initial_file(d)
    first = initial_path.read_bytes()
    initial, bad = D.parse_rows(initial_path)
    proposals, extra_bad = D.parse_rows(d/proposals_file)
    if bad or extra_bad: raise ValueError(f'invalid TSV: {bad + extra_bad}')
    seen = {D.row_key(r):dict(phase=1,line=r['line'],row=r) for r in initial}
    if len(seen) != len(initial): raise ValueError('duplicate first-turn candidate')
    raw = (d/proposals_file).read_text().splitlines(keepends=True)
    additions, repeats = [], []
    for r in proposals:
        key = D.row_key(r)
        if key in seen: repeats.append(dict(proposal=r,retained=seen[key]))
        else:
            seen[key] = dict(phase=2,line=r['line'],row=r)
            additions.append(raw[r['line']-1].rstrip('\r\n')+'\n')
    if first and not first.endswith(b'\n'): raise ValueError('TSV must end in a newline')
    report = dict(protocol=D.PROTOCOL,initial_rows=len(initial),raw_proposal_rows=len(proposals),
                  unique_additions=len(additions),repeated_proposals=repeats,retained=list(seen.values()),
                  proposal_file=proposals_file,proposal_sha256=D.digest(d/proposals_file),
                  followup_sha256=D.digest(d/'followup.tsv'))
    if initial_path.name!='turn1.list.tsv':
        report.update(initial_file=initial_path.name,initial_sha256=D.digest(initial_path),
                      raw_initial_sha256=D.digest(d/'turn1.list.tsv'))
    return first+''.join(additions).encode(), report


def consolidate(d, proposals_file='followup.tsv'):
    if (d/'list.tsv').read_bytes() != (d/'turn1.list.tsv').read_bytes():
        raise ValueError('list.tsv changed during the separate-proposals follow-up')
    payload, report = consolidation_plan(d,proposals_file)
    (d/'list.tsv').write_bytes(payload)
    D.save(d/'consolidation.json',report)
    return report


def inputs_unchanged(d,start):
    files = [('prompt.md','prompt_sha256'),('package.md','package_sha256'),('input.json','input_sha256'),
             ('spawn.md','spawn_sha256'),('followup.txt','followup_text_sha256')]
    return (all(D.digest(d/name) == start[field] for name,field in files)
            and D.digest(Path(start['base_path'])) == start['base_sha256']
            and all(D.digest(Path(p)) == h for p,h in start['inputs'].items()))


def artifact_hashes(d):
    from enrichment.bible.discovery_first_repair import ARTIFACTS as FIRST_REPAIR_ARTIFACTS
    return {name:D.digest(d/name) for name in (*ARTIFACTS,*REPAIR_ARTIFACTS,*FIRST_REPAIR_ARTIFACTS) if (d/name).is_file()}


def verify_artifacts(d, log):
    for name, expected in log.get('artifacts',{}).items():
        if Path(name).name != name or D.digest(d/name) != expected:
            raise ValueError(f'{d}: {name} changed since finish')


def verify_run(d, log):
    if log.get('protocol') != D.PROTOCOL:
        raise ValueError('legacy discovery needs a fresh attempt; its history cannot be upgraded')
    if not set(ARTIFACTS).issubset(log.get('artifacts',{})):
        raise ValueError('incomplete discovery artifact chain')
    verify_artifacts(d,log)
    if not all(log.get(k) is True for k in ('append_only','model_effort_verified','inputs_unchanged','tool_audit_reviewed')):
        raise ValueError('unverified discovery provenance')
    if log.get('protocol_findings') or log.get('consolidation_error'):
        raise ValueError('unresolved discovery failure')
    start = json.loads((d/'started.json').read_text())
    if not inputs_unchanged(d,start): raise ValueError('discovery inputs changed')
    proof = log.get('followup_delivery',[])
    if len(proof) != 1 or not (proof[0].get('encrypted') or proof[0].get('matches')):
        raise ValueError('missing same-session follow-up proof')
    first = json.loads((d/'turn1.json').read_text())
    if first['sha256'] != D.digest(d/'turn1.list.tsv'):
        raise ValueError('first-turn snapshot changed')
    if (d/'turn1.repair.accepted.json').exists():
        from enrichment.bible import discovery_first_repair as first_repair
        if not set(first_repair.ARTIFACTS).issubset(log['artifacts']):
            raise ValueError('incomplete first-turn repair artifact chain')
        if log.get('first_turn_repair')!=first_repair.verify(d):
            raise ValueError('first-turn repair record differs from finished log')
    elif log.get('first_turn_repair'):
        raise ValueError('missing first-turn repair evidence')
    proposal_file = 'followup.tsv'
    if log['status'] == 'accepted':
        from enrichment.bible import discovery_repair as repair
        repair.verify_repair(d,log)
        proposal_file = 'followup.accepted.tsv'
    payload, report = consolidation_plan(d,proposal_file)
    if payload != (d/'list.tsv').read_bytes() or report != json.loads((d/'consolidation.json').read_text()):
        raise ValueError('consolidated rows do not reproduce the preserved proposals')
    if report != log['consolidation']:
        raise ValueError('consolidation differs from finished log')


def finish_run(d, start, session, events, done, contexts, usage, proof, diagnostics, protocol_findings=()):
    """Record failures as failures; only malformed proposals can enter a recorded repair."""
    from enrichment.bible import check_discovery as check
    first = json.loads((d/'turn1.json').read_text())
    problems = list(protocol_findings)
    model_ok = bool(contexts) and all(c.get('model') == start['model'] and c.get('effort') == D.EFFORT for c in contexts)
    if not model_ok: problems.append('unexpected model/effort')
    if len(done) != 2: problems.append('expected exactly two completed turns')
    if len(proof) != 1 or not (proof[0].get('encrypted') or proof[0].get('matches')):
        problems.append('missing/incorrect same-session follow-up delivery')
    unchanged = inputs_unchanged(d,start)
    if not unchanged: problems.append('discovery inputs changed')
    append_only = ((d/'list.tsv').read_bytes() == (d/'turn1.list.tsv').read_bytes()
                   and first['sha256'] == D.digest(d/'turn1.list.tsv'))
    if not append_only: problems.append('first-turn list or snapshot changed')
    cons, error = None, None
    if not problems:
        try: cons = consolidate(d)
        except (OSError,ValueError) as exc: error = str(exc)
    validation = check.check(d/'list.tsv')
    D.save(d/'validation.json',validation)
    proposal_validation = check.check(d/'followup.tsv')
    D.save(d/'proposal_validation.json',proposal_validation)
    rows,_ = D.parse_rows(d/'list.tsv')
    # Preserve the inspected native evidence, even when consolidation fails.
    (d/'session.events.jsonl').write_text(''.join(json.dumps(e,ensure_ascii=False)+'\n' for e in events))
    row = {**start,**session,'arm':'discover-bible','reference_resolver':D.REFERENCE_RESOLVER,
           'status':'partial' if problems or error else 'ok',
           'check':'findings' if problems or error or diagnostics or validation['findings'] or proposal_validation['findings'] or (cons and cons['repeated_proposals']) or (d/'turn1.repair.accepted.json').exists() else 'ok',
           'turn1_rows':first['rows'],'turn1_sha256':first['sha256'],
           'turn2':dict(completed=len(done)==2,rows_total=len(rows),rows_added=cons['unique_additions'] if cons else 0),
           'append_only':append_only,'model_effort_verified':model_ok,'inputs_unchanged':unchanged,
           'tool_audit_reviewed':True,'tool_diagnostics':diagnostics,'protocol_findings':problems,
           'consolidation':cons,'consolidation_error':error,'list_sha256':D.digest(d/'list.tsv'),
           'followup_delivery':proof,'usage_tokens':usage,'estimate_usd':0.0,'cost_usd':0.0,
           'cost_basis':'Codex subscription','completed_at':done[-1]['timestamp'] if done else None,
           'artifacts':artifact_hashes(d)}
    if (d/'turn1.repair.accepted.json').exists():
        from enrichment.bible import discovery_first_repair as repair
        row['first_turn_repair']=repair.verify(d)
    D.save(d/'run.log.json',row)
    ledger = D.HERE/'work/discovery-ledger.jsonl'
    ledger.parent.mkdir(parents=True,exist_ok=True)
    with ledger.open('a') as stream: stream.write(json.dumps(row,ensure_ascii=False)+'\n')
    return row


def followup_proof(session,events,message):
    meta = next((e['payload'] for e in events if e.get('type') == 'session_meta'),{})
    parent_id = meta.get('parent_thread_id') or meta.get('source',{}).get('subagent',{}).get('thread_spawn',{}).get('parent_thread_id')
    proof = []
    if parent_id:
        for parent in Path.home().joinpath('.codex/sessions').glob(f'*/*/*/*{parent_id}.jsonl'):
            for line in parent.read_text().splitlines():
                p = json.loads(line).get('payload',{})
                if p.get('name','').split('.')[-1] != 'followup_task': continue
                args = json.loads(p.get('arguments') or '{}')
                if args.get('target') not in (session['agent_path'],session['agent_path'].split('/')[-1],session['agent_id']): continue
                sent = args.get('message','')
                proof.append(dict(call_id=p.get('call_id'),encrypted=sent.startswith('gAAAAA'),matches=sent == message.strip()))
    return proof


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('phase',choices=['start','snapshot','audit','finish'])
    ap.add_argument('--surah',type=int,required=True)
    ap.add_argument('--target',required=True,help='N:A or secK')
    ap.add_argument('--run-tag',required=True)
    ap.add_argument('--model',choices=D.MODELS,required=True)
    ap.add_argument('--task',help='native task path/name for start')
    ap.add_argument('--reviewed',action='store_true',help='operator reviewed the tool audit')
    ap.add_argument('--protocol-finding',action='append',default=[],help='record a protocol violation; blocks merge/repair')
    a = ap.parse_args()
    d = D.tdir(a.surah,a.target,a.run_tag)/a.model
    if a.phase == 'start':
        if ((d/'started.json').exists() or (d/'run.log.json').exists()): raise SystemExit(f'BLOCKED: {d} already started; use a fresh run tag')
        if not a.task or not re.fullmatch(r'(?:/[a-z0-9_]+/)?[a-z0-9_]+',a.task): ap.error('start requires a valid --task')
        inp = json.loads((d/'input.json').read_text())
        if D.digest(Path(inp['base_path'])) != inp['base_sha256']: raise ValueError('pack base changed after preparation')
        start = {**inp,'started':datetime.now().astimezone().isoformat(),'runner':'agent','protocol':D.PROTOCOL,
                 'agent_path':a.task if a.task.startswith('/') else '/root/'+a.task,
                 'model':D.MODELS[a.model],'effort':D.EFFORT,'run_tag':a.run_tag,
                 'prompt_sha256':D.digest(d/'prompt.md'),'package_sha256':D.digest(d/'package.md'),'input_sha256':D.digest(d/'input.json')}
        message = (f'Read {d/"prompt.md"} and {d/"package.md"} fully. Follow the brief independently using only '
                   'those inputs and your remembered knowledge of Jewish and Christian texts. '
                   f'Write only {d/"list.tsv"}. After creating it you may read it for formatting checks. '
                   'No web, retrieval, other agents, other run files or research scripts. Tools may read the '
                   'permitted inputs, write your TSV and check its format. Do not call models or read repository '
                   'instructions beyond the supplied inputs. Reply briefly after saving. A follow-up will arrive '
                   'in this same session; do not anticipate it.')
        (d/'spawn.md').write_text(message+'\n')
        (d/'followup.txt').write_text(D.FOLLOWUP.format(output=d/'followup.tsv')+'\n')
        start.update(spawn_sha256=D.digest(d/'spawn.md'),followup_text_sha256=D.digest(d/'followup.txt'))
        if not inputs_unchanged(d,start): raise ValueError('pack changed after preparation')
        with (d/'started.json').open('x') as f: json.dump(start,f,indent=2)
        print(message); return
    if (d/'run.log.json').exists(): raise SystemExit('BLOCKED: already finished')
    start = json.loads((d/'started.json').read_text())
    if start.get('protocol') != D.PROTOCOL: raise ValueError('legacy run: preserve it and use a fresh attempt')
    if not inputs_unchanged(d,start): raise ValueError('discovery inputs changed')
    session,events,done,contexts,usage = N.events_for(d)
    if a.phase == 'snapshot':
        if (d/'turn1.json').exists(): raise SystemExit('BLOCKED: already snapshotted')
        repaired = (d/'turn1.repair.accepted.json').exists()
        rows,bad = D.parse_rows(initial_file(d) if repaired else d/'list.tsv')
        if repaired and (d/'list.tsv').read_bytes()!=(d/'turn1.original.tsv').read_bytes():
            raise ValueError('native first-turn list changed since repair approval')
        if len(done) != 1 or bad or len({D.row_key(r) for r in rows}) != len(rows): raise ValueError(f'incomplete/invalid first turn: {bad}')
        data = (d/'list.tsv').read_bytes()
        if data and not data.endswith(b'\n'): raise ValueError('TSV must end in a newline')
        (d/'turn1.list.tsv').write_bytes(data)
        D.save(d/'turn1.json',dict(rows=len(rows),completed_at=done[0]['timestamp'],usage=usage,sha256=D.digest(d/'turn1.list.tsv')))
        print(f'{a.target} {a.model}: first turn snapshotted, {len(rows)} rows'); return
    first = json.loads((d/'turn1.json').read_text())
    if first['sha256'] != D.digest(d/'turn1.list.tsv'): raise ValueError('first-turn snapshot changed')
    calls,diagnostics = N.tool_audit(events,first['completed_at'])
    D.save(d/'tool_calls.json',calls)
    if a.phase == 'audit':
        print(json.dumps(dict(completions=len(done),contexts=contexts,diagnostics=diagnostics,tool_calls=str(d/'tool_calls.json')),ensure_ascii=False)); return
    if not a.reviewed: ap.error('finish requires --reviewed after inspecting tool_calls.json')
    if len(done) < 2: raise ValueError('wait for the second completed turn before finish')
    proof = followup_proof(session,events,(d/'followup.txt').read_text())
    row = finish_run(d,start,session,events,done,contexts,usage,proof,diagnostics,a.protocol_finding)
    print(json.dumps({k:row[k] for k in ('status','check','target','turn1_rows','turn2','tool_diagnostics',
                                       'protocol_findings','consolidation_error')},ensure_ascii=False))
    if row['status'] != 'ok': raise SystemExit(1)

if __name__ == '__main__': main()
