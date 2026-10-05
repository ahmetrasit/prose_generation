#!/usr/bin/env python3
"""Apply an explicitly approved, recorded discovery repair; never call a model."""
import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import discover as D
import discovery_native as N
import check_discovery as C


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def accept(d, surah, approval):
    if not approval.strip():
        raise ValueError('Explicit user approval is required')
    if (d/'repair.accepted.json').exists() or (d/'run.failed.log.json').exists():
        raise ValueError('Repair already started or accepted; do not repeat')
    old = json.loads((d/'run.log.json').read_text())
    if old['status'] != 'partial' or not old.get('consolidation_error'):
        raise ValueError('Expected a failed consolidation')
    if old.get('protocol_findings') or old.get('bad_rows') or old.get('duplicates'):
        raise ValueError('Other unresolved failures block repair')
    for key in ('append_only', 'model_effort_verified', 'inputs_unchanged', 'tool_audit_reviewed'):
        if old.get(key) is not True:
            raise ValueError(f'Unverified provenance: {key}')
    if not old['turn2']['completed']:
        raise ValueError('Both original turns must be complete')
    start = json.loads((d/'started.json').read_text())
    for name, key in [('prompt.md','prompt_sha256'), ('package.md','package_sha256')]:
        if digest(d/name) != start[key]:
            raise ValueError('Input changed')
    if digest(Path(start['source_file'])) != start['source_sha256']:
        raise ValueError('Source commentary changed')
    if (d/'list.tsv').read_bytes() != (d/'turn1.list.tsv').read_bytes():
        raise ValueError('Initial list changed')
    proposal = json.loads((d/'repair.proposed.json').read_text())
    expected = proposal.get('raw_sha256', proposal.get('raw_unchanged'))
    if digest(d/'followup.tsv') != expected:
        raise ValueError('Raw proposals changed')
    lines = (d/'followup.tsv').read_text().splitlines(keepends=True)
    seen = set()
    for change in proposal['changes']:
        i = change['line'] - 1
        before, after = change['before'], change['after']
        if i in seen or lines[i].rstrip('\n').split('\t') != before:
            raise ValueError('Repair does not match original row')
        seen.add(i)
        if len(before) != 4 or len(after) != 4 or before[0] != after[0] or before[3] != after[3]:
            raise ValueError('Repair must preserve grade and explanation')
        if not (before[2] == after[2] or before[1:3] == after[1:3][::-1]):
            raise ValueError('Only reference corrections or reference/basis swaps are supported')
        lines[i] = '\t'.join(after) + '\n'
    corrected = ''.join(lines).encode()
    if corrected != (d/'followup.repair.proposed.tsv').read_bytes():
        raise ValueError('Proposed file contains unrecorded changes')
    q = D.M.verses()
    _, bad = D.parse_rows(d/'followup.repair.proposed.tsv', surah, q)
    if bad:
        raise ValueError(bad)
    # All preconditions checked before preserving the failure and applying changes.
    (d/'run.failed.log.json').write_bytes((d/'run.log.json').read_bytes())
    (d/'validation.failed.json').write_bytes((d/'validation.json').read_bytes())
    (d/'followup.accepted.tsv').write_bytes(corrected)
    cons = N.consolidate(d, surah, q, 'followup.accepted.tsv')
    rows, bad = D.parse_rows(d/'list.tsv', surah, q)
    if bad or len({r['ref'] for r in rows}) != len(rows):
        raise ValueError('Consolidated output invalid')
    validation = C.check(d/'list.tsv', surah, q)
    N.save(d/'validation.json', validation)
    record = {'approval': approval, 'accepted_at': datetime.now(timezone.utc).isoformat(),
              'changes': proposal['changes'], 'raw_sha256': expected,
              'accepted_sha256': digest(d/'followup.accepted.tsv'),
              'failed_log_sha256': digest(d/'run.failed.log.json'),
              'model_calls': 0, 'policy': 'Raw follow-up and failed log preserved; grades and explanations unchanged.'}
    N.save(d/'repair.accepted.json', record)
    log = {**old, 'status': 'accepted', 'check': 'findings', 'consolidation': cons,
           'consolidation_error': None, 'repair': record,
           'repair_record_sha256': digest(d/'repair.accepted.json'),
           'turn2': {**old['turn2'], 'rows_total': len(rows), 'rows_added': len(rows)-old['turn1_rows']},
           'arabic_findings': len(validation['arabic_findings']),
           'strength_counts': dict(Counter(r['strength'] for r in rows)),
           'list_sha256': digest(d/'list.tsv')}
    N.save(d/'run.log.json', log)
    D.V.log({'ref': old['ref'], 'arm': 'discover-repair', 'brief': old['brief'],
             'status': 'accepted', 'check': 'findings', 'cost_usd': 0, 'estimate_usd': 0,
             'model_calls': 0, 'repair_record': str(d/'repair.accepted.json'),
             'approval': approval, 'source_sha256': old['source_sha256']})
    return {'section': old['section_number'], 'model': old['model'], 'status': 'accepted',
            'final_rows': len(rows), 'added': len(rows)-old['turn1_rows'],
            'repeated_proposals': len(cons['repeated_proposals']),
            'arabic_flags': log['arabic_findings']}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--surah', type=int, required=True)
    p.add_argument('--section', type=int, required=True)
    p.add_argument('--model', choices=D.MODELS, required=True)
    p.add_argument('--run-tag', required=True)
    p.add_argument('--approval', required=True)
    a = p.parse_args()
    print(json.dumps(accept(D.discovery_dir(a.surah,a.run_tag)/f'sec{a.section}'/a.model,
                            a.surah,a.approval)))
