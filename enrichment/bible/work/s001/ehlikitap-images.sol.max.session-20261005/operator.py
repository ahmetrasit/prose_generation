"""Local image-run monitor; no model calls or source mutations."""
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[5]))
from enrichment.bible import image_enrich as I,discovery_sessions as N,verdicts as V
root=Path(__file__).resolve().parent
rows=[]
for j in I.read_json(root/'started.json')['jobs']:
 d=root/j['target']
 try:
  _,events,done,contexts,usage=N.events_for(d)
  calls,diagnostics=N.tool_audit(events,'9999');normalized=[];errors=[]
  for i,c in enumerate(calls):
   try:
    kind,inp=I.unwrap_call(c['name'],c['arguments'],bootstrap=i==0)
    if kind=='exec_command':
     if not I.allowed_command(inp['cmd'],d):errors.append({'call':c['call_id'],'command':inp['cmd'][:180]})
     normalized.append(dict(name='Bash',input={'command':inp['cmd']},result=I.output_text(c['output']),is_error=False))
    elif kind=='apply_patch' and not I.allowed_patch(inp,d):errors.append({'call':c['call_id'],'patch':'outside'})
   except Exception as exc:errors.append({'call':c['call_id'],'error':str(exc),'code':c['arguments'][:180]})
  requested,opened=V.lookup_audit(normalized)
  count=lambda name:sum(bool(x.strip()) for x in (d/name).read_text().splitlines()) if (d/name).exists() else 0
  rows.append(dict(target=j['target'],completed_turns=len(done),successful_turns=sum(not e['payload'].get('error') for e in done),calls=len(calls),requested=len(requested),opened=len(opened),
   annotations=count('annotations.jsonl'),verdicts=count('verdicts.jsonl'),expected=j['connections'],errors=errors,
   draft=I.read_json(d/'draft_report.json').get('ok') if (d/'draft_report.json').exists() else None,
   finished=I.read_json(d/'run.log.json').get('status') if (d/'run.log.json').exists() else None))
 except Exception as exc:rows.append(dict(target=j['target'],error=str(exc)))
I.D.save(root/'monitor.json',rows)
for row in rows:print(json.dumps(row,ensure_ascii=False))
