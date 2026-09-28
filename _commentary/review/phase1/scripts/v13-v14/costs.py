import json,glob,os,sys
base=sys.argv[1]
rows=[]
for f in sorted(glob.glob(base+'/out*/**/*status.json',recursive=True)):
    try: d=json.load(open(f))
    except Exception as e: print('ERR',f,e); continue
    rel=os.path.relpath(f,base)
    rows.append((rel,d.get('state'),d.get('cost'),d.get('estimate'),d.get('input_bytes'),d.get('in'),d.get('out'),d.get('thinking'),d.get('minutes'),d.get('effort'),d.get('cache_read'),d.get('responses'),d.get('model')))
tot={}
for r in rows:
    print(' | '.join(str(x) for x in r))
    arm=r[0].split('/')[0]
    tot.setdefault(arm,0)
    if isinstance(r[2],(int,float)): tot[arm]+=r[2]
print(tot, sum(tot.values()))
