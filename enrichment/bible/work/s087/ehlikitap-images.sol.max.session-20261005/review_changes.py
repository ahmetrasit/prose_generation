"""Snapshot unseen annotation changes for the parent to read before recording review."""
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[5]))
from enrichment.bible import image_enrich as I

root = Path(__file__).resolve().parent
progress = I.read_json(root/'editorial-progress.json')
known = {(r['section'],r['id']):r for r in progress['reviewed']}
pending = root/'editorial-changes.json'
if '--acknowledge' in sys.argv:
    for r in I.read_json(pending):
        known[(r['section'],r['id'])] = {k:r[k] for k in ('section','id','sha256')}
    progress['reviewed'] = list(known.values())
    I.D.save(root/'editorial-progress.json',progress)
    print(json.dumps({'recorded_review':len(I.read_json(pending))}))
else:
    rows=[]
    for job in I.read_json(root/'started.json')['jobs']:
        for r in I.R.load(root/job['target']/'annotations.jsonl'):
            digest=hashlib.sha256(json.dumps(r,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
            if known.get((job['target'],r['id']),{}).get('sha256') != digest:
                rows.append(dict(section=job['target'],id=r['id'],sha256=digest,record=r))
    I.D.save(pending,rows)
    for r in rows:
        record=r['record']
        print(r['section'],r['id'],record['paragraf'],record['kaynak'],'\n'+record['metin'])
    print(json.dumps({'unreviewed':len(rows)}))
