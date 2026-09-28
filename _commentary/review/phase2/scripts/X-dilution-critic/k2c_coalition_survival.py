# K2c: control for K2. For v5 candidate decisions (qac_morpheme ledger rows excluded), accepted vs rejected vs narrowed:
#  (i) candidate title visible in A's digest; (ii) COALITION survival: some C reading in the digest carries >=50% of the
#  candidate's branch_refs (candidates with >=2 branches); (iii) every branch of the candidate appears (r-id) somewhere.
import json, glob, os, re, collections
V5='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
DG='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/A-v5-step/out/digests'
def rid(b):
    m=re.match(r'root_0*(\d+)/(B\d+)',b); return f"r{int(m.group(1)):04d}/{m.group(2)}" if m else None
cnt=collections.Counter(); seen=set()
for p in sorted(glob.glob(V5+'/raw/*/*/*/macro.discovery.json')):
    aid,sd,ay=p[len(V5)+5:].split('/')[:3]
    if 'basmala' in aid or ay in seen or not os.path.exists(f'{DG}/{ay}.digest.md'): continue
    seen.add(ay); D=open(f'{DG}/{ay}.digest.md',encoding='utf-8').read()
    csec=D.split('\n## C. ',1)[1].split('\n## ',1)[0] if '\n## C. ' in D else ''
    creads=[set(re.findall(r'r\d{4}/B\d+',l.split('{')[-1])) for l in csec.split('\n') if l.startswith('- ')]
    for lane in ('micro','macro','global'):
        f=f'{V5}/raw/{aid}/{sd}/{ay}/{lane}.discovery.json'; q=f'{V5}/input/{aid}/{sd}/{ay}/{lane}.discovery.prompt.md'
        if not (os.path.exists(f) and os.path.exists(q)): continue
        t=open(q,encoding='utf-8').read(); i=t.find('<lane_packet_json>'); j=t.find('</lane_packet_json>')
        cands={c['candidate_id']:c for c in json.loads(t[i+len('<lane_packet_json>'):j]).get('candidate_inventory',[])}
        for c in json.load(open(f,encoding='utf-8')).get('candidate_decisions',[]):
            cc=cands.get(c.get('candidate_id')) or {}
            if cc.get('source_type')=='qac_morpheme': continue
            dec=c.get('decision'); title=(cc.get('title') or '').strip()
            bs={rid(b) for b in cc.get('branch_refs') or []}-{None}
            cnt[(dec,'n')]+=1; cnt[(dec,'title')]+= bool(title) and title in D
            if len(bs)>=2:
                cnt[(dec,'n2')]+=1
                cnt[(dec,'coal')]+= any(len(bs&r)/len(bs)>=0.5 for r in creads)
            if bs: cnt[(dec,'nb')]+=1; cnt[(dec,'allb')]+= all(b in D for b in bs)
print('ayat',len(seen))
print('decision\tn\ttitle visible\tcoalition (>=50% of its branches in one C reading)\tall branches somewhere')
for dec in ('accept','narrow','reject'):
    n=cnt[(dec,'n')]
    if not n: continue
    print(f"{dec}\t{n}\t{cnt[(dec,'title')]/n:.1%}\t{cnt[(dec,'coal')]/max(1,cnt[(dec,'n2')]):.1%} of {cnt[(dec,'n2')]}\t{cnt[(dec,'allb')]/max(1,cnt[(dec,'nb')]):.1%} of {cnt[(dec,'nb')]}")
