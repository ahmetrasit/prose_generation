# K2b: rejected semantic readings (excluding ledger-only qac_morpheme rows) by A's own reason classes (s02 regexes),
# and how many leave a title trace in A's digest. Lane/anchor reasons = killed by the lane architecture, not by meaning.
import json, glob, os, re, collections, sys
sys.path.insert(0,'/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/A-v5-step')
src=open('/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/A-v5-step/s02_v5_scan.py').read()
ns={'__file__':'/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/A-v5-step/s02_v5_scan.py'}; exec(src.split('def packet')[0].replace("BI=json.load(open(os.path.join(OUT,'branch_index.json')))","BI={}"),ns); rclass=ns['rclass']
V5='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
DG='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/A-v5-step/out/digests'
cnt=collections.Counter(); seen=set(); ex=collections.defaultdict(list)
for p in sorted(glob.glob(V5+'/raw/*/*/*/macro.discovery.json')):
    aid,sd,ay=p[len(V5)+5:].split('/')[:3]
    if 'basmala' in aid or ay in seen or not os.path.exists(f'{DG}/{ay}.digest.md'): continue
    seen.add(ay); D=open(f'{DG}/{ay}.digest.md',encoding='utf-8').read()
    for lane in ('micro','macro','global'):
        f=f'{V5}/raw/{aid}/{sd}/{ay}/{lane}.discovery.json'; q=f'{V5}/input/{aid}/{sd}/{ay}/{lane}.discovery.prompt.md'
        if not (os.path.exists(f) and os.path.exists(q)): continue
        t=open(q,encoding='utf-8').read(); i=t.find('<lane_packet_json>'); j=t.find('</lane_packet_json>')
        cands={c['candidate_id']:c for c in json.loads(t[i+len('<lane_packet_json>'):j]).get('candidate_inventory',[])}
        for c in json.load(open(f,encoding='utf-8')).get('candidate_decisions',[]):
            if c.get('decision')!='reject': continue
            cc=cands.get(c.get('candidate_id')) or {}
            if cc.get('source_type')=='qac_morpheme': continue
            rc=rclass(c.get('reason')); title=(cc.get('title') or '').strip()
            vis=bool(title) and title in D
            cnt[(rc,'n')]+=1; cnt[(rc,'vis')]+=vis
            if not vis and len(ex[rc])<4: ex[rc].append((ay,lane,cc.get('source_type'),title[:120],(c.get('reason') or '')[:140]))
tot=sum(v for k,v in cnt.items() if k[1]=='n'); totv=sum(v for k,v in cnt.items() if k[1]=='vis')
print('ayat',len(seen),'semantic rejects',tot,'title visible',totv)
for rc in sorted({k[0] for k in cnt}):
    print(f"{rc}\t{cnt[(rc,'n')]}\tvisible {cnt[(rc,'vis')]}")
for rc in ('lane_boundary','anchor_binding'):
    print('\nexamples',rc)
    for e in ex[rc]: print(' -',e)
