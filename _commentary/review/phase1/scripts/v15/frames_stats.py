import json,glob,os,csv,re
from collections import Counter,defaultdict
csv.field_size_limit(10**9)
D='/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data'
inv={f['id'] for f in json.load(open(D+'/frames_inventory.json'))['frames']}
items=[];newdefs=defaultdict(list)
jobs_sample=0
for p in sorted(glob.glob(D+'/frames/out/*.json')):
    d=json.load(open(p))
    for it in d.get('items',[]):
        it['_job']=os.path.basename(p); items.append(it)
    for nf in d.get('new_frames',[]): newdefs[nf['id']].append(nf.get('scene',''))
print('jobs',len(glob.glob(D+'/frames/out/*.json')),'items',len(items))
keys=Counter(it['key'] for it in items)
print('unique keys',len(keys),'dup keys',sum(1 for k,v in keys.items() if v>1))
nfr=Counter(len(it.get('frames',[])) for it in items)
print('frames per item',sorted(nfr.items()))
# normalize like lib
def norm(fid):
    if fid in inv or fid.startswith('new.'): return fid
    same=[i for i in inv if i.split('.',1)[1]==fid.split('.',1)[-1]]
    return same[0] if len(same)==1 else fid
allf=Counter(); newc=defaultdict(set); offinv=Counter()
only_new=0; has_new=0; zero=0
bykey=defaultdict(list)
for it in items:
    fs=[norm(f['frame']) for f in it.get('frames',[])]
    bykey[it['key']]+= [(norm(f['frame']),f['role']) for f in it.get('frames',[])]
    if not fs: zero+=1
    for f in fs:
        allf[f]+=1
        if f.startswith('new.'): newc[f].add(it['key'])
        elif f not in inv: offinv[f]+=1
    if fs and all(f.startswith('new.') for f in fs): only_new+=1
    if any(f.startswith('new.') for f in fs): has_new+=1
print('items with zero frames',zero,'only-new',only_new,'has-new',has_new, 'pct has new',round(100*has_new/len(items),1))
print('inventory scenes used',len([f for f in inv if allf[f]]),'of',len(inv))
print('new ids',len(newc),'singletons',sum(1 for v in newc.values() if len(v)==1))
print('off-inventory non-new ids',len(offinv),offinv.most_common(10))
# top inventory scenes by branch count
print('top scenes',allf.most_common(15))
print('bottom inv scenes',sorted([(allf[f],f) for f in inv])[:15])
# near duplicates in new ids
toks=defaultdict(list)
for n in newc:
    base=n[4:]
    stem=re.sub(r'(ia|s|es|ing|ion)$','',base)
    toks[stem].append(n)
print('new ids sharing stem:',[v for v in toks.values() if len(v)>1][:20])
# biggest new ids
print('largest new ids',sorted(((len(v),k) for k,v in newc.items()),reverse=True)[:25])
json.dump({k:v for k,v in bykey.items()},open('/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase1/v15/bykey.json','w'),ensure_ascii=False)
