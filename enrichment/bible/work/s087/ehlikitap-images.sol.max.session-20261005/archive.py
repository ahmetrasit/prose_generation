"""Preserve the accepted S87 pilot and verify every compressed member."""
import hashlib
import json
from pathlib import Path
import sys
import tarfile

sys.path.insert(0, str(Path(__file__).resolve().parents[5]))
from enrichment.bible import image_enrich as I

root = Path(__file__).resolve().parent
result = I.read_json(root/'run.log.json')
assert result['status'] == 'ok' and result['images'] == 18
audit = I.E.V2/'audits/image-s087-session-20261005'
bundle = audit/'evidence.tar.gz'
assert not bundle.exists(), 'never overwrite an archived run'
sources = {}
for job in I.read_json(root/'started.json')['jobs']:
    d = root/job['target']
    log = I.read_json(d/'run.log.json')
    assert log['status'] == 'ok'
    for name, digest in log['artifacts'].items():
        assert I.D.digest(d/name) == digest, (job['target'], name)
    for p in sorted(d.iterdir()):
        if p.is_file():
            sources[f'images/{job["target"]}/{p.name}'] = p
for name in ('annotations.jsonl','assembly.json','discovery.merged.tsv','gaps.json',
             'prefetch.json','quotation-review.json','quote_audit.json','editorial-review.json',
             'run.log.json','started.json','tool_calls.json','verdict_report.json','verdicts.jsonl','launch.json','validation-run.json'):
    sources[f'assembly/{name}'] = root/name
selected = I.E.wd(87)/'discovery/selected.json'
sources['discovery/selected.json'] = selected
for name in I.read_json(selected).values():
    for p in (selected.parent/name, (selected.parent/name).with_suffix('.json')):
        sources[f'discovery/{p.relative_to(selected.parent)}'] = p
for name in ('image_enrich.py','test_image_enrich.py','RUNBOOK.md'):
    sources[f'workflow/{name}'] = I.E.V2/name
for name in ('operator.py','preflight.py','quote_audit.py','review_changes.py','final_review.py','archive.py'):
    sources[f'operator/{name}'] = root/name
for p in sorted(root.glob('editorial-progress.*.json')):
    sources[f'operator/review-snapshots/{p.name}'] = p
audit.mkdir(parents=True, exist_ok=True)
accepted = audit/'accepted'
accepted.mkdir(exist_ok=True)
accepted_hashes = {}
for p in sorted((I.E.OUT/'s087').glob('surah.ehlikitap.*')):
    with (accepted/p.name).open('xb') as stream:
        stream.write(p.read_bytes())
    accepted_hashes[p.name] = I.D.digest(accepted/p.name)
assert len(accepted_hashes) == 7
members = []
with tarfile.open(bundle, 'w:gz', compresslevel=6) as tar:
    for name, p in sorted(sources.items()):
        members.append(dict(path=name,sha256=I.D.digest(p),bytes=p.stat().st_size,source=I.E.rel(p)))
        tar.add(p, arcname=name, recursive=False)
with tarfile.open(bundle, 'r:gz') as tar:
    assert set(tar.getnames()) == {r['path'] for r in members}
    for r in members:
        assert hashlib.sha256(tar.extractfile(r['path']).read()).hexdigest() == r['sha256'], r['path']
I.D.save(audit/'evidence-manifest.json',dict(bundle=bundle.name,sha256=I.D.digest(bundle),files=members,
    accepted_files=accepted_hashes,
    discovery_history={'bundle':'../s087-prepared-20261005/completed-turns.evidence.tar.gz',
                       'wave2_overlay':'../s087-prepared-20261005/repairs-wave2.manifest.json'},
    verification='Every archive member reread and SHA256 checked; every accepted image artifact checked against its immutable run log.'))
for name in ('quotation-review.json','editorial-review.json'):
    (audit/name).write_bytes((root/name).read_bytes())
I.D.save(audit/'result.json', result)
print(json.dumps(dict(directory=I.E.rel(audit),members=len(members),bytes=bundle.stat().st_size,accepted_files=len(accepted_hashes))))
