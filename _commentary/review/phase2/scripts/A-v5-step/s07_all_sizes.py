# Digest size distribution over every numbered v5 ayah with 3 lanes (read-only).
import glob, os, re, statistics as st, json, sys, time
sys.argv=['x']; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'s05_digest.py')).read().rsplit("\nif __name__=='__main__':",1)[0])
V5='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
refs=set()
for p in glob.glob(V5+'/raw/*/*/*/macro.discovery.json'):
    aid,sd,ay=p[len(V5)+5:].split('/')[:3]
    if 'basmala' in aid or aid.startswith(('s013','s014','s029')): continue
    s_,a_=ay.split('_')
    if a_=='0': continue
    if all(os.path.exists(os.path.dirname(p)+f'/{l}.discovery.json') for l in ('micro','global')): refs.add(f'{int(s_)}:{int(a_)}')
refs=sorted(refs,key=lambda z:tuple(map(int,z.split(':'))))
rows=[]; t0=time.time()
for i,r in enumerate(refs):
    try:
        db,lb,secs,nf,na,ns=build(r); rows.append((r,db,lb,dict(secs),nf,na,ns))
    except Exception as e: print('ERR',r,e,file=sys.stderr)
    if i%100==0: print(i,round(time.time()-t0),file=sys.stderr)
json.dump(rows,open(os.path.join(OUT,'all_digest_sizes.json'),'w'))
def q(v,p): v=sorted(v); return v[int(p*(len(v)-1))]
print('n',len(rows))
for k,idx in [('digest_bytes',1),('lookup_bytes',2),('findings',4),('branches',5),('set_aside',6)]:
    v=[x[idx] for x in rows]; print(k,'median',st.median(v),'p10',q(v,.1),'p90',q(v,.9),'max',max(v))
for sec in ['A','B','C','C2','D','E','F1','F2','F3','F4','F5','F6']:
    v=[x[3].get(sec,0) for x in rows]; print('sec',sec,'median',st.median(v),'p90',q(v,.9),'max',max(v))
