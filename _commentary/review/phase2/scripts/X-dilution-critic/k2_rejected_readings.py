# Critic check K2: v5 rejected candidate READINGS (not branches) - does A's digest keep any trace of them?
# s05 shows a rejected candidate only via section D, only if one of its branches is activated nowhere in the ayah,
# and only once per branch (first proposal title wins). Count rejected candidates whose title reaches the digest.
import json, glob, os, re, collections
V5='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
DG='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/A-v5-step/out/digests'
cnt=collections.Counter(); bysrc=collections.Counter(); ex=[]
seen_ayah=set()
for p in sorted(glob.glob(V5+'/raw/*/*/*/macro.discovery.json')):
    aid,sd,ay=p[len(V5)+5:].split('/')[:3]
    if 'basmala' in aid or ay in seen_ayah: continue
    dg=f'{DG}/{ay}.digest.md'
    if not os.path.exists(dg): continue
    seen_ayah.add(ay); D=open(dg,encoding='utf-8').read()
    for lane in ('micro','macro','global'):
        f=f'{V5}/raw/{aid}/{sd}/{ay}/{lane}.discovery.json'; q=f'{V5}/input/{aid}/{sd}/{ay}/{lane}.discovery.prompt.md'
        if not (os.path.exists(f) and os.path.exists(q)): continue
        t=open(q,encoding='utf-8').read(); i=t.find('<lane_packet_json>'); j=t.find('</lane_packet_json>')
        cands={c['candidate_id']:c for c in json.loads(t[i+len('<lane_packet_json>'):j]).get('candidate_inventory',[])}
        d=json.load(open(f,encoding='utf-8'))
        for c in d.get('candidate_decisions',[]):
            dec=c.get('decision')
            if dec not in ('reject','narrow'): continue
            cc=cands.get(c.get('candidate_id')) or {}
            title=(cc.get('title') or '').strip()
            src=cc.get('source_type','unknown')
            vis = bool(title) and (title in D)
            cnt[(dec,'n')]+=1; cnt[(dec,'visible')]+=vis
            bysrc[(dec,src,'n')]+=1; bysrc[(dec,src,'vis')]+=vis
            if dec=='reject' and not vis and len(ex)<12 and title: ex.append((ay,lane,src,title[:160],(c.get('reason') or '')[:160]))
print('ayat',len(seen_ayah))
for dec in ('reject','narrow'):
    n=cnt[(dec,'n')]; v=cnt[(dec,'visible')]
    print(f"{dec}: {n} candidate decisions; title visible anywhere in digest: {v} ({v/n:.1%}); invisible {n-v}")
print('\nreject by source: n / title visible')
for (dec,src,k),v in sorted(bysrc.items()):
    if dec=='reject' and k=='n': print(f"  {src}: {v} / {bysrc[(dec,src,'vis')]}")
print('\nexamples of rejected readings with no trace in the digest (ayah, lane, source, title, reason):')
for e in ex: print(' -',e)
