# What the digest drops from v5 findings, and how much of it is defensive/negative framing.
import json, glob, re, collections, os
V5='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
B=collections.Counter(); neg=collections.Counter(); n=collections.Counter()
NEG=re.compile(r"\bnot\b|\bno\b|\bnever\b|\bwithout\b|değil|yoktur|anlamına gelmez|iddia edilmez",re.I)
for p in glob.glob(V5+'/raw/*/*/*/*.discovery.json'):
    if 'basmala' in p: continue
    d=json.load(open(p,encoding='utf-8'))
    for f in d.get('findings',[]):
        if not isinstance(f,dict): continue
        for k in ('title','claim','mechanism','reader_payoff','containment'):
            v=f.get(k) or ''; v=v if isinstance(v,str) else json.dumps(v,ensure_ascii=False); B[k]+=len(v.encode()); n[k]+=1
            if NEG.search(v): neg[k]+=1
        e=json.dumps(f.get('epistemic') or {},ensure_ascii=False); B['epistemic']+=len(e.encode())
        for a in f.get('branch_activations') or []:
            if not isinstance(a,dict): continue
            for k in ('carrier','independent_trigger','activation','resulting_reading','boundary'):
                v=a.get(k) or ''; v=v if isinstance(v,str) else json.dumps(v,ensure_ascii=False); B['act.'+k]+=len(v.encode()); n['act.'+k]+=1
                if NEG.search(v): neg['act.'+k]+=1
    for c in d.get('candidate_decisions',[]):
        B['decision.reason']+=len((c.get('reason') or '').encode())
tot=sum(B.values())
for k,v in B.most_common(): print(f'{k:22s} {v/1e6:8.1f} MB {v/tot:6.1%}  neg-framed {neg[k]}/{n[k]} ({(neg[k]/n[k] if n[k] else 0):.0%})')
