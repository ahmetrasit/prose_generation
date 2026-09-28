# branch_kind guard audit over every v5 activation of a collocation-bound branch (read-only).
# Construction-cue test (heuristic): the branch root occurs in a carrier/focus ayah AND one of that
# occurrence's grammar-attachment partners (other_root letters or surface) appears in the branch's
# early-source phrase / definition. Categories: cue_present, cue_absent, root_absent_in_carrier_ayat.
import json, glob, os, re, collections
V5='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
OUT=os.path.join(os.path.dirname(__file__),'out')
BI=json.load(open(os.path.join(OUT,'branch_index.json'))); OCC=json.load(open(os.path.join(OUT,'root_occ.json')))
DIAC=re.compile(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]')
def norm(s):
    s=DIAC.sub('',s or ''); s=s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه').replace('ؤ','و').replace('ئ','ي')
    return s
occ_by=collections.defaultdict(list)  # (rid, ayah) -> occurrences
for rid,v in OCC.items():
    for q,ay,lem,surf,atts in v['occ']: occ_by[(rid,ay)].append((q,surf,atts))
def cue(b, ayahs):
    rid=b.split('/')[0]; v=BI[b]
    text=norm(' '.join([v.get('src_ar') or '',v.get('what_is_ar') or '',v.get('image_ar') or '']))
    found_root=False
    for ay in ayahs:
        for q,surf,atts in occ_by.get((rid,ay),[]):
            found_root=True
            for rel,osurf,oroot,prep,role in atts:
                cands=[]
                if oroot: cands.append(norm(oroot.replace(' ','')))
                if osurf: cands.append(norm(osurf).replace('ال','',1) if norm(osurf).startswith('ال') else norm(osurf))
                if prep: pass
                for c in cands:
                    c=c.strip()
                    if len(c)>=3 and c in text: return 'cue_present'
    return 'cue_absent' if found_root else 'root_absent_in_carrier_ayat'
agg=collections.Counter(); ex=collections.defaultdict(list)
for p in glob.glob(V5+'/raw/*/*/*/*.discovery.json'):
    aid,sd,ay,fn=p[len(V5)+5:].split('/'); lane=fn.split('.')[0]
    focus=ay.replace('_',':')
    d=json.load(open(p,encoding='utf-8'))
    for f in d.get('findings',[]):
        if not isinstance(f,dict): continue
        for a in f.get('branch_activations') or []:
            if not isinstance(a,dict): continue
            b=a.get('branch_ref')
            if not b or b not in BI: continue
            k=BI[b]['kind']
            if k!='collocation': continue
            refs=set()
            for r in (a.get('carrier_refs') or [])+(a.get('focus_return_refs') or [])+[focus]:
                m=re.match(r'(\d+):(\d+)',str(r))
                if m: refs.add(f'{m.group(1)}:{m.group(2)}')
            c=cue(b,refs)
            agg[(c,)]+=1; agg[(c,a.get('application_mode'))]+=1
            if len(ex[c])<400: ex[c].append((focus,lane,b,BI[b]['root'],BI[b]['gloss'],a.get('application_mode'),sorted(refs)[:4],(a.get('activation') or '')[:160]))
json.dump({'agg':{'|'.join(map(str,k)):v for k,v in agg.items()},'examples':ex},open(os.path.join(OUT,'collocation_check.json'),'w'),ensure_ascii=False)
for k in sorted(agg,key=str): print('|'.join(map(str,k)),agg[k])
import random; random.seed(1)
for c in ex:
    print('==',c)
    for e in random.sample(ex[c],min(6,len(ex[c]))): print('  ',e)
