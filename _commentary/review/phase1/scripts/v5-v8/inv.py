import os, re, json, collections, sys
BASE='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
layers=['input','raw','editorial','middle','concise','output','archive']
rows=[]
for layer in layers:
    lp=os.path.join(BASE,layer)
    for root,dirs,files in os.walk(lp):
        rel=os.path.relpath(root,lp)
        parts=rel.split(os.sep)
        for f in files:
            if f=='.DS_Store': continue
            p=os.path.join(root,f)
            try: sz=os.path.getsize(p)
            except: sz=-1
            rows.append((layer,rel,f,sz))
json.dump(rows,open(os.path.join(os.path.dirname(__file__),'files.json'),'w'))
print(len(rows))
# summary: file-name patterns per layer
pat=collections.Counter()
szs=collections.defaultdict(int)
for layer,rel,f,sz in rows:
    g=re.sub(r'^\d+_\d+\.','S_A.',f)
    pat[(layer,g)]+=1; szs[(layer,g)]+=sz
for k in sorted(pat):
    print(k[0],k[1],pat[k],round(szs[k]/1e6,1),'MB')
