#!/usr/bin/env python3
"""Recorded, explicitly approved first-turn repairs; preserve the native raw list."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from enrichment.bible import discovery as D, discovery_native as N, discovery_repair as R, check_discovery as C
from enrichment.bible import discovery_sessions as S

ARTIFACTS = ('turn1.original.tsv','turn1.validation.failed.json','turn1.tool_calls.json',
             'turn1.repair.proposed.json','turn1.repair.proposed.tsv',
             'turn1.accepted.tsv','turn1.repair.accepted.json')


def eligible(d):
    if any((d/name).exists() for name in ('turn1.json','followup.tsv','run.log.json')):
        raise ValueError('first-turn repair must precede snapshot and follow-up')
    start=json.loads((d/'started.json').read_text())
    if start.get('protocol')!=D.PROTOCOL or not N.inputs_unchanged(d,start):
        raise ValueError('discovery protocol or inputs changed')
    session,events,done,contexts,usage=S.events_for(d)
    if len(done)!=1 or not contexts or any(c.get('model')!=start['model'] or c.get('effort')!=start.get('effort',D.EFFORT) for c in contexts):
        raise ValueError('expected one completed turn with the requested model and effort')
    if N.followup_proof(session,events,(d/'followup.txt').read_text()):
        raise ValueError('follow-up already delivered')
    return events,done,contexts


def audit(d):
    events,done,contexts=eligible(d)
    calls,diagnostics=S.tool_audit(events,done[0]['timestamp'])
    D.save(d/'turn1.tool_calls.json',calls)
    return dict(completions=1,contexts=contexts,diagnostics=diagnostics,tool_calls=str(d/'turn1.tool_calls.json'))


def propose(d,changes):
    eligible(d)
    if any((d/name).exists() for name in ARTIFACTS if name!='turn1.tool_calls.json'):
        raise ValueError('first-turn repair already proposed; do not overwrite it')
    raw=(d/'list.tsv').read_bytes()
    validation=C.check(d/'list.tsv')
    if not validation['schema_errors']:
        raise ValueError('only a structurally failed first turn can enter this repair')
    payload=R.repaired_bytes(raw,changes,allow_schema_swap=True)
    (d/'turn1.original.tsv').write_bytes(raw)
    D.save(d/'turn1.validation.failed.json',validation)
    proposed=d/'turn1.repair.proposed.tsv';proposed.write_bytes(payload)
    rows,bad=D.parse_rows(proposed)
    if len({D.row_key(r) for r in rows})!=len(rows): bad.append('duplicate repaired first-turn connection')
    if payload and not payload.endswith(b'\n'): bad.append('TSV must end in a newline')
    proposal=dict(raw_sha256=D.digest(d/'turn1.original.tsv'),changes=changes,
                  proposed_sha256=D.digest(proposed),schema_errors=bad,model_calls=0)
    D.save(d/'turn1.repair.proposed.json',proposal)
    audit(d)
    if bad: raise ValueError(f'proposed first-turn repair remains invalid: {bad}')
    return proposal


def proposed_bytes(d):
    proposal=json.loads((d/'turn1.repair.proposed.json').read_text())
    raw=(d/'turn1.original.tsv').read_bytes()
    if D.digest(d/'turn1.original.tsv')!=proposal['raw_sha256']:
        raise ValueError('raw first-turn evidence changed')
    payload=R.repaired_bytes(raw,proposal['changes'],allow_schema_swap=True)
    path=d/'turn1.repair.proposed.tsv'
    if payload!=path.read_bytes() or D.digest(path)!=proposal['proposed_sha256']:
        raise ValueError('proposed first-turn file has unrecorded changes')
    rows,bad=D.parse_rows(path)
    if bad or len({D.row_key(r) for r in rows})!=len(rows):
        raise ValueError(f'invalid/duplicate repaired first turn: {bad}')
    return proposal,payload


def accept(d,approval,reviewed=False):
    if not approval.strip(): raise ValueError('explicit approval of the exact first-turn repair is required')
    if not reviewed: raise ValueError('inspect the first-turn tool audit before accepting')
    if (d/'turn1.repair.accepted.json').exists(): raise ValueError('first-turn repair already accepted')
    events,done,_=eligible(d)
    proposal,payload=proposed_bytes(d)
    if (d/'list.tsv').read_bytes()!=(d/'turn1.original.tsv').read_bytes():
        raise ValueError('native first-turn list changed')
    calls,_=S.tool_audit(events,done[0]['timestamp'])
    if calls!=json.loads((d/'turn1.tool_calls.json').read_text()):
        raise ValueError('native tools changed since the inspected first-turn audit')
    (d/'turn1.accepted.tsv').write_bytes(payload)
    record=dict(policy='bible-first-turn-repair-v1',approval=approval,tool_audit_reviewed=True,
                accepted_at=datetime.now(timezone.utc).isoformat(),changes=proposal['changes'],model_calls=0,
                artifacts={name:D.digest(d/name) for name in ARTIFACTS if name!='turn1.repair.accepted.json'})
    D.save(d/'turn1.repair.accepted.json',record)
    verify(d)
    return record


def verify(d):
    record=json.loads((d/'turn1.repair.accepted.json').read_text())
    expected=set(ARTIFACTS)-{'turn1.repair.accepted.json'}
    if (record.get('policy')!='bible-first-turn-repair-v1' or not record.get('approval','').strip()
            or record.get('tool_audit_reviewed') is not True or set(record.get('artifacts',{}))!=expected):
        raise ValueError('incomplete first-turn repair provenance')
    for name,sha in record['artifacts'].items():
        if D.digest(d/name)!=sha: raise ValueError(f'first-turn repair evidence changed: {name}')
    proposal,payload=proposed_bytes(d)
    if record['changes']!=proposal['changes'] or payload!=(d/'turn1.accepted.tsv').read_bytes():
        raise ValueError('accepted first-turn correction differs from the recorded changes')
    if (d/'turn1.list.tsv').exists() and (d/'turn1.list.tsv').read_bytes()!=(d/'turn1.original.tsv').read_bytes():
        raise ValueError('raw first-turn snapshot changed')
    return record


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('phase',choices=('audit','propose','accept'))
    ap.add_argument('--surah',type=int,required=True);ap.add_argument('--target',required=True)
    ap.add_argument('--run-tag',required=True);ap.add_argument('--model',choices=D.MODELS,required=True)
    ap.add_argument('--changes',type=Path);ap.add_argument('--approval');ap.add_argument('--reviewed',action='store_true')
    a=ap.parse_args();d=D.tdir(a.surah,a.target,a.run_tag)/a.model
    if a.phase=='audit': result=audit(d)
    elif a.phase=='propose':
        if not a.changes: ap.error('propose requires --changes')
        result=propose(d,json.loads(a.changes.read_text()))
    else:
        if not a.approval: ap.error('accept requires --approval')
        result=accept(d,a.approval,a.reviewed)
    print(json.dumps(result,ensure_ascii=False))


if __name__=='__main__': main()
