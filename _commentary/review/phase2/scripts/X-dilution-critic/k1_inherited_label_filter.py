# Critic check K1: does A's label-free digest still inherit v5's label-driven selection of inter-ayah partners?
# For every v5 ayah with an A digest: every pushed connection row (macro+global lanes) -> target ayah + prior_label.
# Presence of the target ref in (i) v5-inherited sections A/B/C/C2/D, (ii) script sections E/F1-F7, (iii) whole digest.
import json, glob, os, re, collections
V5='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
DG='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/A-v5-step/out/digests'
def sections(t):
    S=collections.defaultdict(str); cur='head'
    for l in t.split('\n'):
        if l.startswith('## '): cur=l[3:5].strip('. ')
        S[cur]+=l+'\n'
    return S
inh=('A','B','C','C2','D'); scr=('E','F1','F2','F3','F4','F5','F6','F7')
cnt=collections.Counter(); n=0; seen_ayah=set()
for p in sorted(glob.glob(V5+'/raw/*/*/*/global.discovery.json')):
    aid,sd,ay=p[len(V5)+5:].split('/')[:3]
    if 'basmala' in aid or ay in seen_ayah: continue
    dg=f'{DG}/{ay}.digest.md'
    if not os.path.exists(dg): continue
    seen_ayah.add(ay)
    S=sections(open(dg,encoding='utf-8').read())
    I=''.join(v for k,v in S.items() if k in inh); X=''.join(v for k,v in S.items() if k in scr)
    rows={}
    for lane in ('macro','global'):
        q=f'{V5}/input/{aid}/{sd}/{ay}/{lane}.discovery.prompt.md'
        if not os.path.exists(q): continue
        t=open(q,encoding='utf-8').read(); i=t.find('<lane_packet_json>'); j=t.find('</lane_packet_json>')
        pk=json.loads(t[i+len('<lane_packet_json>'):j])
        for r in pk.get('connection_registry',[]):
            m=re.match(r'^(\d+):(\d+)$',str(r.get('target_ref') or ''))
            if not m: continue
            tr=m.group(0); lab=r.get('prior_label') or 'none'
            # keep best label per target (strong>medium>weak>no value>none) to avoid double counting across lanes
            order={'strong':0,'medium':1,'weak':2,'no value':3,'none':4}
            if tr not in rows or order[lab]<order[rows[tr]]: rows[tr]=lab
    n+=1
    for tr,lab in rows.items():
        rx=re.compile(r'(?<![\d:])'+re.escape(tr)+r'(?![\d])')
        a=bool(rx.search(I)); b=bool(rx.search(X))
        cnt[(lab,'rows')]+=1; cnt[(lab,'inh')]+=a; cnt[(lab,'scr')]+=b; cnt[(lab,'any')]+=(a or b); cnt[(lab,'scr_only')]+=(b and not a)
print('ayat',n)
print('label\trows\tin v5-inherited A-D\tin script E-F7\tin digest (any)')
for lab in ('strong','medium','weak','no value','none'):
    r=cnt[(lab,'rows')]
    if r: print(f"{lab}\t{r}\t{cnt[(lab,'inh')]/r:.1%}\t{cnt[(lab,'scr')]/r:.1%}\t{cnt[(lab,'any')]/r:.1%}")
