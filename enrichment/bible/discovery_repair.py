#!/usr/bin/env python3
"""Prepare and accept recorded Bible reference repairs; never call a model."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from enrichment.bible import discovery as D, discovery_native as N, check_discovery as C


def eligible(log):
    if log.get('protocol') != D.PROTOCOL or log.get('status') != 'partial' or not log.get('consolidation_error'):
        raise ValueError('only a failed proposal consolidation can be repaired')
    if log.get('protocol_findings') or not log.get('turn2',{}).get('completed'):
        raise ValueError('unresolved protocol failure blocks repair')
    for key in ('append_only','model_effort_verified','inputs_unchanged','tool_audit_reviewed'):
        if log.get(key) is not True: raise ValueError(f'unverified provenance: {key}')


def repaired_bytes(raw, changes, *, allow_schema_swap=False, allow_witness_tradition=False):
    """Only a reference correction or reference/basis swap; never change a judgement."""
    lines = raw.decode().splitlines(keepends=True)
    if not changes: raise ValueError('repair requires exact before/after changes')
    seen = set()
    for change in changes:
        n, before, after = change['line'],change['before'],change['after']
        if type(n) is not int or not 1<=n<=len(lines) or n in seen:
            raise ValueError('invalid/repeated repair line')
        seen.add(n)
        if lines[n-1].rstrip('\r\n').split('\t') != before:
            raise ValueError('repair does not match the preserved raw row')
        if (len(before)!=6 or len(after)!=6 or any(not isinstance(x,str) or any(c in x for c in '\t\n\r') for x in after)):
            raise ValueError('repair requires six literal fields')
        schema_swap = (allow_schema_swap and before[1:3]==after[1:3][::-1]
                       and after[1] in D.TRAD and after[2] in D.KIND
                       and before[0]==after[0] and before[3:]==after[3:])
        expected_tradition = ('tevrat' if before[3].startswith('WLC:') else
                              'incil' if before[3].startswith('SBLGNT:') else None)
        witness_label = (allow_witness_tradition and expected_tradition is not None
                         and after[1]==expected_tradition and before[1]!=after[1]
                         and before[0]==after[0] and before[2:]==after[2:])
        if not (schema_swap or witness_label) and (before[:3]!=after[:3] or before[5]!=after[5]):
            raise ValueError('repair must preserve strength, tradition, kind and explanation')
        if before[4]!=after[4] and before[3:5]!=after[3:5][::-1]:
            raise ValueError('only reference corrections or reference/basis swaps are allowed')
        if before==after or not str(change.get('reason','')).strip():
            raise ValueError('each change needs a specific reason')
        lines[n-1] = '\t'.join(after)+'\n'
    return ''.join(lines).encode()


def check_failed(d):
    if (d/'repair.accepted.json').exists() or (d/'run.failed.log.json').exists():
        raise ValueError('repair already started or accepted; preserve it')
    log = json.loads((d/'run.log.json').read_text())
    eligible(log)
    N.verify_artifacts(d,log)
    if not N.inputs_unchanged(d,json.loads((d/'started.json').read_text())):
        raise ValueError('discovery input changed')
    if (d/'list.tsv').read_bytes() != (d/'turn1.list.tsv').read_bytes():
        raise ValueError('first-turn list changed')
    return log


def propose(d, changes, *, allow_witness_tradition=False, allow_schema_swap=False):
    check_failed(d)
    if (d/'repair.proposed.json').exists() or (d/'followup.repair.proposed.tsv').exists():
        raise ValueError('proposal exists; inspect it without overwriting')
    payload = repaired_bytes((d/'followup.tsv').read_bytes(),changes,
                             allow_witness_tradition=allow_witness_tradition,allow_schema_swap=allow_schema_swap)
    path = d/'followup.repair.proposed.tsv'
    path.write_bytes(payload)
    _, bad = D.parse_rows(path)
    proposal = dict(raw_sha256=D.digest(d/'followup.tsv'),changes=changes,
                    proposed_sha256=D.digest(path),schema_errors=bad,model_calls=0)
    if allow_witness_tradition: proposal['allow_witness_tradition']=True
    if allow_schema_swap: proposal['allow_schema_swap']=True
    D.save(d/'repair.proposed.json',proposal)
    if bad: raise ValueError(f'proposed repair remains invalid: {bad}')
    return proposal


def accept(d, approval):
    if not approval.strip(): raise ValueError('record the explicit approval of this exact proposed repair')
    if D.C.running_calls(): raise ValueError('Bible page calls are active')
    old = check_failed(d)
    proposal = json.loads((d/'repair.proposed.json').read_text())
    if D.digest(d/'followup.tsv') != proposal['raw_sha256']:
        raise ValueError('raw proposals changed')
    payload = repaired_bytes((d/'followup.tsv').read_bytes(),proposal['changes'],
                             allow_witness_tradition=proposal.get('allow_witness_tradition',False),
                             allow_schema_swap=proposal.get('allow_schema_swap',False))
    proposed = d/'followup.repair.proposed.tsv'
    if payload != proposed.read_bytes() or D.digest(proposed) != proposal['proposed_sha256']:
        raise ValueError('proposed file has unrecorded changes')
    _, bad = D.parse_rows(proposed)
    if bad: raise ValueError(bad)
    (d/'run.failed.log.json').write_bytes((d/'run.log.json').read_bytes())
    (d/'validation.failed.json').write_bytes((d/'validation.json').read_bytes())
    (d/'followup.accepted.tsv').write_bytes(payload)
    cons = N.consolidate(d,'followup.accepted.tsv')
    validation = C.check(d/'list.tsv')
    D.save(d/'validation.json',validation)
    record = dict(approval=approval,accepted_at=datetime.now(timezone.utc).isoformat(),
                  changes=proposal['changes'],raw_sha256=proposal['raw_sha256'],
                  accepted_sha256=D.digest(d/'followup.accepted.tsv'),
                  proposal_sha256=D.digest(d/'repair.proposed.json'),failed_log_sha256=D.digest(d/'run.failed.log.json'),
                  model_calls=0,policy='Raw proposals, failed validation and failed log preserved; no regrading.')
    if proposal.get('allow_witness_tradition'): record['allow_witness_tradition']=True
    if proposal.get('allow_schema_swap'): record['allow_schema_swap']=True
    D.save(d/'repair.accepted.json',record)
    log = {**old,'status':'accepted','check':'findings','consolidation':cons,'consolidation_error':None,
           'repair':record,'list_sha256':D.digest(d/'list.tsv'),
           'turn2':dict(completed=True,rows_total=validation['rows'],rows_added=cons['unique_additions']),
           'artifacts':N.artifact_hashes(d)}
    D.save(d/'run.log.json',log)
    N.verify_run(d,log)
    with (D.HERE/'work/discovery-ledger.jsonl').open('a') as stream:
        stream.write(json.dumps(dict(arm='discover-bible-repair',target=log['target'],run_tag=log['run_tag'],
                                    model=log['model'],status='accepted',repair=record),ensure_ascii=False)+'\n')
    return record


def verify_repair(d, log):
    if not set(N.REPAIR_ARTIFACTS).issubset(log['artifacts']):
        raise ValueError('incomplete repair artifact chain')
    record = json.loads((d/'repair.accepted.json').read_text())
    proposal = json.loads((d/'repair.proposed.json').read_text())
    old = json.loads((d/'run.failed.log.json').read_text())
    eligible(old)
    if (not record.get('approval','').strip() or log.get('repair') != record
            or record['failed_log_sha256'] != D.digest(d/'run.failed.log.json')
            or record['proposal_sha256'] != D.digest(d/'repair.proposed.json')
            or record['raw_sha256'] != D.digest(d/'followup.tsv')
            or record['accepted_sha256'] != D.digest(d/'followup.accepted.tsv')
            or record['changes'] != proposal['changes']
            or record.get('allow_witness_tradition',False)!=proposal.get('allow_witness_tradition',False)
            or record.get('allow_schema_swap',False)!=proposal.get('allow_schema_swap',False)):
        raise ValueError('repair provenance changed')
    for name, expected in old['artifacts'].items():
        original = {'list.tsv':'turn1.list.tsv','validation.json':'validation.failed.json'}.get(name,name)
        if D.digest(d/original) != expected: raise ValueError(f'failed-run evidence changed: {name}')
    payload = repaired_bytes((d/'followup.tsv').read_bytes(),record['changes'],
                             allow_witness_tradition=record.get('allow_witness_tradition',False),
                             allow_schema_swap=record.get('allow_schema_swap',False))
    if payload != (d/'followup.accepted.tsv').read_bytes() or payload != (d/'followup.repair.proposed.tsv').read_bytes():
        raise ValueError('accepted correction differs from the recorded changes')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('phase',choices=('propose','accept'))
    ap.add_argument('--surah',type=int,required=True)
    ap.add_argument('--target',required=True)
    ap.add_argument('--run-tag',required=True)
    ap.add_argument('--model',choices=D.MODELS,required=True)
    ap.add_argument('--changes',type=Path,help='JSON array of line/before/after/reason objects')
    ap.add_argument('--approval',help='record of explicit approval for the exact proposal')
    ap.add_argument('--allow-witness-tradition',action='store_true',help='propose only an edition-derived tradition-label correction; still requires exact approval')
    ap.add_argument('--allow-schema-swap',action='store_true',help='propose only a transposition of tradition/kind columns; still requires exact approval')
    a=ap.parse_args()
    d=D.tdir(a.surah,a.target,a.run_tag)/a.model
    if a.phase=='propose':
        if not a.changes: ap.error('propose requires --changes')
        result=propose(d,json.loads(a.changes.read_text()),allow_witness_tradition=a.allow_witness_tradition,
                       allow_schema_swap=a.allow_schema_swap)
    else:
        if not a.approval: ap.error('accept requires --approval')
        result=accept(d,a.approval)
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__': main()
