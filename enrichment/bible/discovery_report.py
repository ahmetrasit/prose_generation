#!/usr/bin/env python3
"""Report Bible discovery attempts and a dry verifier handoff; no model calls."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from enrichment.bible import discovery as D


def report(s, tag, targets=None, attempts=None):
    targets = D.targets_of(s) if targets is None else targets
    attempts = attempts or {}
    data = dict(surah=s,run_tag=tag,protocol=D.PROTOCOL,jobs=[],targets=[],model_calls=0,opus_started=False,
                ready_for_merge=True,cost_usd=0.0,cost_basis='Recorded completed discovery calls, Codex subscription')
    for t in targets:
        selected = attempts.get(t['target'],tag)
        per = {}
        for model in D.MODELS:
            d = D.tdir(s,t['target'],selected)/model
            item = dict(target=t['target'],model=model,run_tag=selected,status='missing',errors=[])
            try:
                if not (d/'run.log.json').exists():
                    item['status'] = 'started' if (d/'started.json').exists() else 'prepared' if (d/'prompt.md').exists() else 'missing'
                    raise ValueError('no completed native run')
                log = json.loads((d/'run.log.json').read_text())
                cons = log.get('consolidation') or {}
                item.update(status=log.get('status'),check=log.get('check'),initial=log.get('turn1_rows'),
                    proposals=cons.get('raw_proposal_rows'),added=cons.get('unique_additions'),
                    repeats=cons.get('repeated_proposals',[]),usage_tokens=log.get('usage_tokens'),
                    cost_usd=log.get('cost_usd'),diagnostics=log.get('tool_diagnostics',[]),
                    protocol_findings=log.get('protocol_findings',[]),consolidation_error=log.get('consolidation_error'),
                    repair=log.get('repair'),first_turn_repair=log.get('first_turn_repair'))
                data['cost_usd'] += log.get('cost_usd') or 0
                if (d/'validation.json').exists(): item['validation']=json.loads((d/'validation.json').read_text())
                if (d/'proposal_validation.json').exists():
                    item['raw_proposal_validation']=json.loads((d/'proposal_validation.json').read_text())
                rows = D.checked_run(d,t)
                per[model]=rows
                cited=set(re.findall(r'(?:WLC|SBLGNT):[1-4]?[A-Za-z]+\.\d+\.\d+',t['prose']))
                item.update(final=len(rows),strengths=dict(Counter(r['strength'] for r in rows)),
                            missing_existing_citations=sorted(cited-{r['ref'] for r in rows}))
            except (OSError,ValueError,KeyError) as exc:
                item['errors'].append(str(exc)); data['ready_for_merge']=False
            data['jobs'].append(item)
        if set(per)==set(D.MODELS):
            refs=[{(r['tradition'],r['ref']) for r in per[m]} for m in D.MODELS]
            data['targets'].append(dict(target=t['target'],run_tag=selected,dry_handoff=True,
                unique_references=len(set.union(*refs)),overlap=len(set.intersection(*refs)),
                connections=len({D.connection_id(t['target'],r) for rows in per.values() for r in rows}),
                page_author_estimate='No Bible live-call calibration yet; use enrich.py build after prefetch/indexing.'))
    if not targets: data['ready_for_merge']=False
    data['limits']='Reader labels and wording findings are unverified. Prefetch, index build and complete verdicts remain required.'
    return data


def markdown(data):
    lines=[f"# S{data['surah']} Bible discovery: {data['run_tag']}",'',
           '| Target | Reader | Attempt | Status | Initial | Proposals | New | Repeats | Final |',
           '|---|---|---|---|---:|---:|---:|---:|---:|']
    for j in data['jobs']:
        lines.append(f"| {j['target']} | {j['model']} | {j['run_tag']} | {j['status']} | {j.get('initial','—')} | "
                     f"{j.get('proposals','—')} | {j.get('added','—')} | {len(j.get('repeats',[]))} | {j.get('final','—')} |")
    for j in data['jobs']:
        lines += ['',f"## {j['target']} / {j['model']} / {j['run_tag']}",'']
        details={k:j[k] for k in ('errors','protocol_findings','consolidation_error','diagnostics','repeats',
                                 'validation','raw_proposal_validation','missing_existing_citations','repair','first_turn_repair','usage_tokens') if j.get(k)}
        lines += ['```json',json.dumps(details,ensure_ascii=False,indent=2),'```']
    lines += ['', '## Dry handoff', '', '```json',json.dumps(data['targets'],ensure_ascii=False,indent=2),'```','',
              f"Ready to merge: {data['ready_for_merge']}. Recorded charge: ${data['cost_usd']:.2f}. No model calls.",
              '',data['limits']]
    return '\n'.join(lines)+'\n'


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--surah',type=int,required=True)
    ap.add_argument('--run-tag',required=True)
    ap.add_argument('--targets',help='N:A,secK,surah; default all prepared targets')
    ap.add_argument('--selection',type=Path,help='same explicit target/run-tag mapping as merge')
    ap.add_argument('--write',action='store_true',help='save report.json and report.md within this Bible attempt')
    a=ap.parse_args()
    root=D.discovery_dir(a.surah,a.run_tag)
    targets=D.targets_of(a.surah)
    attempts=json.loads(a.selection.read_text()) if a.selection else {}
    if a.targets:
        want=set(a.targets.split(','))
        if want-{t['target'] for t in targets}-{'surah'}: ap.error('unknown target')
        targets=[t for t in targets if t['target'] in want or ('surah' in want and t['target'].startswith('sec'))]
    else:
        targets=[t for t in targets if any((D.tdir(a.surah,t['target'],attempts.get(t['target'],a.run_tag))/m).exists() for m in D.MODELS)]
    data=report(a.surah,a.run_tag,targets,attempts)
    if a.write:
        root.mkdir(parents=True,exist_ok=True)
        D.save(root/'report.json',data)
        (root/'report.md').write_text(markdown(data))
    print(json.dumps(data,ensure_ascii=False,indent=2))
    if not data['ready_for_merge']: raise SystemExit(1)


if __name__=='__main__': main()
