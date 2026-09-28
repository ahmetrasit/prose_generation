"""Reconstruct item->node mapping of the historical s1_ar3_v1 E5 clause/source-unit embeddings
(read-only import of quran-slm source; no bytecode written). Verifies via the cache content hash."""
import sys, os, csv, json, hashlib
sys.dont_write_bytecode = True
SLM='/Volumes/OZTURK/_projects/quran-slm'
sys.path.insert(0, SLM+'/src')
from quran_slm import dense
csv.field_size_limit(10**9)
rows={r['node_id']:r for r in csv.DictReader(open(SLM+'/resources/source/quranic_branches_ar.tsv',encoding='utf-8'),delimiter='\t')}
order=[json.loads(l)['node_id'] for l in open(SLM+'/artifacts/s1_ar3_v1/nodes/global_nodes.jsonl')]
print('nodes',len(order),'rows',len(rows), 'cols', list(next(iter(rows.values())).keys())[:12])
br=[dense.prepare_dense_branch(node_id=n, branch_image_ar=rows[n].get('branch_image_ar'), what_is_ar=rows[n].get('what_is_ar'), source_phrase_ar=rows[n].get('source_phrase_ar')) for n in order]
cl_ids=[];cl_txt=[];cl_own=[];su_ids=[];su_txt=[];su_own=[]
for b in br:
    for i,c in enumerate(b.scope_clauses):
        cl_ids.append(f"{b.node_id}:scope:{i:03d}"); cl_txt.append(c); cl_own.append(b.node_id)
    for uid,t in zip(b.source_unit_ids,b.source_units):
        su_ids.append(uid); su_txt.append(t); su_own.append(b.node_id)
print('clauses',len(cl_ids),'source units',len(su_ids))
E=SLM+'/artifacts/s1_ar3_v1/embeddings/'
m=json.load(open(E+'what_is_ar_clauses.passage.cdf675821d0ac88aae7a.json'))
m2=json.load(open(E+'source_phrase_ar_units.passage.5a178a5098c0b51a2d97.json'))
print('meta counts',m['item_count'],m2['item_count'])
json.dump(dict(clause_owner=cl_own,clause_text=cl_txt,unit_owner=su_own,unit_text=su_txt),open('clause_map.json','w'),ensure_ascii=False)
