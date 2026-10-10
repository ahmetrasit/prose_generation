"""Local pilot bookkeeping. Never launches agents or sends follow-ups."""
import argparse,json,re,subprocess,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[6]))
from enrichment.bible import discovery as D, discovery_native as N, discovery_sessions as S
ROOT=Path(__file__).resolve().parent
PLAN=json.loads((ROOT/'orchestration.json').read_text())

def directory(job): return D.tdir(1,job['target'],PLAN['run_tag'])/job['model']
def native(job,phase,*extra):
    args=[sys.executable,'-B',str(D.HERE/'discovery_native.py'),phase,'--surah','1','--run-tag',PLAN['run_tag'],
          '--target',job['target'],'--model',job['model'],*extra]
    r=subprocess.run(args,capture_output=True,text=True)
    return dict(exit_code=r.returncode,output=r.stdout+r.stderr)

def scan():
    ready=[];finished=[];issues=[];counts={}
    for job in PLAN['jobs']:
        d=directory(job)
        try:
            session,events,done,contexts,usage=S.events_for(d)
            counts[len(done)]=counts.get(len(done),0)+1
            key=dict(target=job['target'],model=job['model'],task=job['task'])
            if (d/'run.log.json').exists():
                log=json.loads((d/'run.log.json').read_text());finished.append(dict(**key,status=log['status']));continue
            if len(done)>=2:
                finished.append(dict(**key,status='audit_pending',turns=len(done)));continue
            if len(done)!=1: continue
            if not (d/'turn1.json').exists():
                rows,bad=D.parse_rows(N.initial_file(d) if (d/'turn1.repair.accepted.json').exists() else d/'list.tsv')
                if bad:
                    issue=dict(**key,errors=bad,raw_sha256=D.digest(d/'list.tsv'));issues.append(issue)
                    if not (d/'first-validation.original.json').exists():D.save(d/'first-validation.original.json',issue)
                    continue
                result=native(job,'snapshot')
                if result['exit_code']:issues.append(dict(**key,**result));continue
            proof=N.followup_proof(session,events,(d/'followup.txt').read_text())
            if not proof: ready.append(key)
            elif len(proof)!=1:issues.append(dict(**key,followup_deliveries=proof))
        except Exception as exc: issues.append(dict(target=job['target'],model=job['model'],error=str(exc)))
    result=dict(completed_turn_counts=counts,ready=ready,finished=finished,issues=issues)
    D.save(ROOT/'operator-state.json',result)
    print(json.dumps(result,ensure_ascii=False,indent=2))

def audit(target,model):
    job=next(j for j in PLAN['jobs'] if (j['target'],j['model'])==(target,model));d=directory(job)
    if (d/'turn1.json').exists():result=native(job,'audit')
    else:
        from enrichment.bible import discovery_first_repair as repair
        result=dict(exit_code=0,output=json.dumps(repair.audit(d)))
    if result['exit_code']:
        print(json.dumps(result,ensure_ascii=False));return
    meta=json.loads(result['output'])
    meta['contexts']=[dict(model=c.get('model'),effort=c.get('effort')) for c in meta['contexts']]
    calls=json.loads(Path(meta['tool_calls']).read_text())
    if (d/'turn1.repair.accepted.json').exists():
        from enrichment.bible import discovery_first_repair as repair
        repair.verify(d)
        prior=json.loads((d/'turn1.tool_calls.json').read_text())
        meta['phase1_matches_accepted_audit']=[c for c in calls if c['phase']==1]==prior
        if meta['phase1_matches_accepted_audit']:calls=[c for c in calls if c['phase']==2]
    print(json.dumps(dict(target=target,model=model,**meta),ensure_ascii=False))
    for call in calls:
        raw=call['arguments']
        try:
            obj=json.loads(raw)
            raw=obj.get('cmd') or obj.get('input') or raw
        except (ValueError,TypeError):pass
        # This is display-only. Keep every non-TSV line, tool name, phase and code
        # prefix/suffix; raw arguments remain in tool_calls.json for inspection.
        decoded=raw.replace('\\n','\n').replace('\\t','\t') if isinstance(raw,str) else str(raw)
        lines=decoded.splitlines();out=[];omitted=0
        for line in lines:
            try:
                literal=json.loads(line.strip().rstrip(','))
                if isinstance(literal,list) and len(literal)==6 and all(isinstance(x,str) for x in literal) and literal[0] in D.STRENGTH:
                    omitted+=1;continue
            except ValueError:pass
            if re.match(r'^[+-]?\s*[\"\']?(?:strong|medium|weak)\t',line):omitted+=1
            else:out.append(line)
        print(json.dumps(dict(phase=call['phase'],name=call['name'],call_id=call['call_id'],
                              omitted_tsv_data_lines=omitted,code='\n'.join(out)),ensure_ascii=False))

ap=argparse.ArgumentParser();ap.add_argument('phase',choices=['scan','audit']);ap.add_argument('--target');ap.add_argument('--model')
a=ap.parse_args()
if a.phase=='scan':scan()
else:audit(a.target,a.model)
