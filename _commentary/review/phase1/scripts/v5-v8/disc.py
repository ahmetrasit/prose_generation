import json,os,glob,collections,re,statistics as st
BASE='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5/raw'
out=[]
bad=[]
for p in glob.glob(BASE+'/*/*/*/*.discovery.json'):
    parts=p[len(BASE)+1:].split('/')
    aid,sur,ay,fn=parts
    lane=fn.split('.')[0]
    try:
        d=json.load(open(p))
    except Exception as e:
        bad.append((p,str(e)[:80])); continue
    cds=d.get('candidate_decisions',[]); fs=d.get('findings',[])
    dec=collections.Counter(c.get('decision') for c in cds)
    rawacts=[a for f in fs if isinstance(f,dict) for a in (f.get('branch_activations') or [])]
    acts=[a for a in rawacts if isinstance(a,dict)]
    stracts=len(rawacts)-len(acts)
    modes=collections.Counter(a.get('application_mode') for a in acts)
    stat=collections.Counter((f.get('epistemic') or {}).get('status') for f in fs)
    tmpl=sum(1 for a in acts if re.match(r'(Independent contextual grounding enters at|The (context|focus) occurrence at)',str(a.get('independent_trigger',''))) )
    tmplc=sum(1 for a in acts if re.match(r'The (context|focus) occurrence at \S+ carries the supplied branch sense',str(a.get('carrier',''))))
    nocand=sum(1 for f in fs if not f.get('origin_candidate_id'))
    out.append(dict(aid=aid,ay=ay,lane=lane,schema=d.get('schema_version'),cov=d.get('coverage_complete'),ncand=len(cds),nf=len(fs),dec=dict(dec),nact=len(acts),modes=dict(modes),stat=dict(stat),tmpl_trig=tmpl,tmpl_carrier=tmplc,uncand=nocand,stracts=stracts,size=os.path.getsize(p)))
json.dump(out,open(os.path.join(os.path.dirname(__file__),'disc.json'),'w'))
print('parsed',len(out),'bad',len(bad)); print(bad[:5])
print(collections.Counter(o['schema'] for o in out))
print('coverage_complete',collections.Counter(o['cov'] for o in out))
# aggregate
agg=collections.defaultdict(lambda: collections.Counter())
for o in out:
    fam=re.sub(r'-\d{8}$','',o['aid']); fam=re.sub(r'-p\d\d-','-pNN-',fam); fam=re.sub(r'^s\d{3}','sNNN',fam)
    a=agg[(fam,o['lane'])]
    a['files']+=1; a['cand']+=o['ncand']; a['find']+=o['nf']; a['act']+=o['nact']; a['tmpl_trig']+=o['tmpl_trig']; a['tmpl_carrier']+=o['tmpl_carrier']; a['uncand']+=o['uncand']; a['stracts']+=o['stracts']
    for k,v in o['dec'].items(): a['dec_'+str(k)]+=v
    for k,v in o['stat'].items(): a['st_'+str(k)]+=v
    for k,v in o['modes'].items(): a['m_'+str(k)]+=v
for k in sorted(agg):
    print(k, dict(agg[k]))
