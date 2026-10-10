"""Audit completed S87 image sessions; never finish or alter author deliverables."""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5]))
from enrichment.bible import image_enrich as I, discovery_sessions as N

root = Path(__file__).resolve().parent
reviewed = {(r['section'], r['id']): r['sha256'] for r in I.read_json(root/'editorial-progress.json')['reviewed']}
for job in I.read_json(root/'started.json')['jobs']:
    d = root/job['target']
    if (d/'run.log.json').exists():
        continue
    _, _, done, _, _ = N.events_for(d)
    if sum(not e['payload'].get('error') for e in done) != 1:
        continue
    audit, calls = I.native_audit(d)
    report = I.check(d, final=True, calls=calls)
    changes = []
    for r in I.R.load(d/'annotations.jsonl'):
        digest = hashlib.sha256(json.dumps(r, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        if reviewed.get((job['target'], r['id'])) != digest:
            changes.append(r['id'])
    result = dict(audit=audit, check=report, editorial_changes=changes)
    I.D.save(d/'operator-preflight.json', result)
    print(json.dumps(dict(target=job['target'], audit_ok=audit['ok'], check_ok=report['ok'],
                         errors=audit['errors']+report['errors'], editorial_changes=changes,
                         annotations=report['records'], verdicts=report['verdicts']), ensure_ascii=False), flush=True)
