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


def consolidate(d):
    first = (d/'turn1.list.tsv').read_bytes()
    if (d/'list.tsv').read_bytes() != first:
        raise ValueError('list.tsv changed during the separate-proposals follow-up')
    initial, bad = D.parse_rows(d/'turn1.list.tsv')
    proposals, extra_bad = D.parse_rows(d/'followup.tsv')
    if bad or extra_bad: raise ValueError(f'invalid TSV: {bad + extra_bad}')
    seen = {D.row_key(r) for r in initial}
    if len(seen) != len(initial): raise ValueError('duplicate first-turn candidate')
    raw = (d/'followup.tsv').read_text().splitlines(keepends=True)
    additions, repeats = [], []
    for r in proposals:
        key = D.row_key(r)
        if key in seen: repeats.append(r)
        else:
            seen.add(key); additions.append(raw[r['line']-1].rstrip('\r\n')+'\n')
    if first and not first.endswith(b'\n'): raise ValueError('TSV must end in a newline')
    (d/'list.tsv').write_bytes(first+''.join(additions).encode())
    report = dict(unique_additions=len(additions),repeated_proposals=repeats,followup_sha256=D.digest(d/'followup.tsv'))
    D.save(d/'consolidation.json',report)
    return report


def inputs_unchanged(d,start):
    return all(D.digest(d/name) == start[field] for name,field in
               [('prompt.md','prompt_sha256'),('package.md','package_sha256'),('input.json','input_sha256')]) and D.digest(Path(start['base_path'])) == start['base_sha256']


def followup_proof(session,events,message):
    meta = next((e['payload'] for e in events if e.get('type') == 'session_meta'),{})
    parent_id = meta.get('parent_thread_id') or meta.get('source',{}).get('subagent',{}).get('thread_spawn',{}).get('parent_thread_id')
    proof = []
    if parent_id:
        for parent in Path.home().joinpath('.codex/sessions').glob(f'*/*/*/*{parent_id}.jsonl'):
            for line in parent.read_text().splitlines():
                p = json.loads(line).get('payload',{})
                if p.get('name') != 'followup_task': continue
                args = json.loads(p.get('arguments') or '{}')
                if args.get('target') not in (session['agent_path'],session['agent_path'].split('/')[-1]): continue
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
    a = ap.parse_args()
    d = D.tdir(a.surah,a.target,a.run_tag)/a.model
    if a.phase == 'start':
        if ((d/'started.json').exists() or (d/'run.log.json').exists()): raise SystemExit(f'BLOCKED: {d} already started; use a fresh run tag')
        if not a.task or not re.fullmatch(r'(?:/[a-z0-9_]+/)?[a-z0-9_]+',a.task): ap.error('start requires a valid --task')
        inp = json.loads((d/'input.json').read_text())
        if D.digest(Path(inp['base_path'])) != inp['base_sha256']: raise ValueError('pack base changed after preparation')
        start = {**inp,'started':datetime.now().astimezone().isoformat(),'runner':'agent',
                 'agent_path':a.task if a.task.startswith('/') else '/root/'+a.task,
                 'model':D.MODELS[a.model],'effort':D.EFFORT,'run_tag':a.run_tag,
                 'prompt_sha256':D.digest(d/'prompt.md'),'package_sha256':D.digest(d/'package.md'),'input_sha256':D.digest(d/'input.json')}
        with (d/'started.json').open('x') as f: json.dump(start,f,indent=2)
        message = (f'Read {d/"prompt.md"} and {d/"package.md"} fully. Follow the brief independently using only '
                   'those inputs and your remembered knowledge of Jewish and Christian texts. '
                   f'Write only {d/"list.tsv"}. After creating it you may read it for formatting checks. '
                   'No web, retrieval, other agents, other run files or research scripts. Tools may read the '
                   'permitted inputs, write your TSV and check its format. Do not call models or read repository '
                   'instructions beyond the supplied inputs. Reply briefly after saving. A follow-up will arrive '
                   'in this same session; do not anticipate it.')
        (d/'spawn.md').write_text(message+'\n')
        (d/'followup.txt').write_text(D.FOLLOWUP.format(output=d/'followup.tsv')+'\n')
        print(message); return
    if (d/'run.log.json').exists(): raise SystemExit('BLOCKED: already finished')
    start = json.loads((d/'started.json').read_text())
    if not inputs_unchanged(d,start): raise ValueError('discovery inputs changed')
    session,events,done,contexts,usage = N.events_for(d)
    if a.phase == 'snapshot':
        if (d/'turn1.json').exists(): raise SystemExit('BLOCKED: already snapshotted')
        rows,bad = D.parse_rows(d/'list.tsv')
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
    if len(done) != 2 or not contexts or not all(c.get('model') == D.MODELS[a.model] and c.get('effort') == D.EFFORT for c in contexts):
        raise ValueError('expected two completed turns in the same model/effort session')
    proof = followup_proof(session,events,(d/'followup.txt').read_text())
    if len(proof) != 1 or not (proof[0]['encrypted'] or proof[0]['matches']): raise ValueError('missing/incorrect same-session follow-up delivery')
    consolidation = consolidate(d)
    rows,bad = D.parse_rows(d/'list.tsv')
    if bad: raise ValueError(f'invalid consolidated rows: {bad}')
    row = {**start,**session,'ref':f'S{a.surah}','arm':'discover-bible','brief':f'{a.run_tag}.{a.model}.{a.target}',
           'status':'ok','turn1_rows':first['rows'],'turn1_sha256':first['sha256'],
           'turn2':dict(completed=True,rows_total=len(rows),rows_added=consolidation['unique_additions']),
           'append_only':True,'tool_audit_reviewed':True,'tool_diagnostics':diagnostics,'consolidation':consolidation,
           'list_sha256':D.digest(d/'list.tsv'),'followup_delivery':proof,'usage_tokens':usage,'cost_usd':0.0,
           'cost_basis':'Codex subscription','completed_at':done[-1]['timestamp']}
    D.save(d/'run.log.json',row)
    with (D.HERE/'work/discovery-ledger.jsonl').open('a') as stream: stream.write(json.dumps(row)+'\n')
    print(json.dumps({k:row[k] for k in ('status','target','turn1_rows','turn2','tool_diagnostics')},ensure_ascii=False))

if __name__ == '__main__': main()
