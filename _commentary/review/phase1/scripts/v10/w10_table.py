import json, glob, os, re
base='/Volumes/OZTURK/_projects/prose_generation/_commentary/v9/lines/work'
rows=[]
for d in sorted(glob.glob(base+'/*/synth/w10-*')):
    ayah=d.split('/')[-3]; arm=d.split('/')[-1]
    cost=inp=out=cr=cw=dur=None; model=None; err=None
    p=d+'/run.log.json'
    if os.path.exists(p):
        try:
            j=json.loads(open(p).read())
            cost=j.get('total_cost_usd'); u=j.get('usage',{})
            inp=u.get('input_tokens'); out=u.get('output_tokens'); cr=u.get('cache_read_input_tokens'); cw=u.get('cache_creation_input_tokens')
            dur=j.get('duration_ms'); model=list((j.get('modelUsage') or {}).keys())
            err=j.get('error') or (j.get('is_error') and j.get('subtype'))
        except Exception as ex:
            err=str(ex)[:80]
    pj=d+'/run.log.jsonl'
    if os.path.exists(pj):
        # codex usage
        tot={}
        for line in open(pj):
            try: ev=json.loads(line)
            except: continue
            if ev.get('type')=='turn.completed':
                for k,v in ev.get('usage',{}).items(): tot[k]=tot.get(k,0)+v
        inp=tot.get('input_tokens'); out=tot.get('output_tokens'); cr=tot.get('cached_input_tokens'); model='codex'
    r=glob.glob(d+'/*.reading.tr.md')
    words=len(open(r[0]).read().split()) if r else 0
    refs=len(set(re.findall(r'(\d{1,3}:\d{1,3})',open(r[0]).read()))) if r else 0
    rows.append((ayah,arm,cost,inp,cw,cr,out,dur,words,refs,model,err))
for r in rows: print('\t'.join(str(x) for x in r))
