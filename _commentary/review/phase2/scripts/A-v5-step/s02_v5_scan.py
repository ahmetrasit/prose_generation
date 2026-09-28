# Full scan of v5 discovery JSON + matching input packets (read-only).
# Measures: HFT/channel/v12 relay vs Luna's own activations; reason classes of rejects/narrows;
# branch_kind of activated and excluded branches; rejected branches that survive nowhere in the ayah.
import json, glob, os, re, collections, sys, time
V5='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
OUT=os.path.join(os.path.dirname(__file__),'out')
BI=json.load(open(os.path.join(OUT,'branch_index.json')))
def kind(b): return (BI.get(b) or {}).get('kind','not_in_dict')
REASON=[('lane_boundary',re.compile(r'not (a )?supplied|not locally|is absent|are absent|outside (the |this )?(micro|macro|lane|packet)|micro (lane|packet|context)|this lane|cannot be (locally )?landed|host surface|no supplied host|unavailable|not supplied as|not verif|cannot be verified|absent (as|from)',re.I)),
        ('anchor_binding',re.compile(r'unanchored|no exact|zero exact|coordinate|focus return|anchor refs|no ayah, word|exact anchor|without identifying their separate carriers',re.I)),
        ('ledger_or_duplicate',re.compile(r'ledger_only|ledger evidence|morphological identity|duplicat|already (retained|carried)|represented',re.I)),
        ('literal_or_mechanism',re.compile(r'literal|no [a-z\- ]*(event|contact|implement|material|throat|ingestion)|does not (establish|supply|support|make|turn)|do not establish|not establish|adds the missing|no functional|physical',re.I)),
        ('semantic_other',re.compile(r'catalogue|decorative|generic|co-membership|not a positive|evidentiary question|not an anchored changed reading|aggregat',re.I))]
def rclass(t):
    for n,rx in REASON:
        if rx.search(t or ''): return n
    return 'unclassified'
def packet(p):
    try:
        t=open(p,encoding='utf-8').read()
    except FileNotFoundError: return None
    i=t.find('<lane_packet_json>'); j=t.find('</lane_packet_json>')
    if i<0: return None
    return json.loads(t[i+len('<lane_packet_json>'):j])
agg=collections.Counter(); per_ayah={}
t0=time.time()
files=sorted(glob.glob(V5+'/raw/*/*/*/*.discovery.json'))
by_ayah=collections.defaultdict(dict)
for p in files:
    aid,sd,ay,fn=p[len(V5)+5:].split('/')
    lane=fn.split('.')[0]
    if lane not in('micro','macro','global'): continue
    by_ayah[(aid,sd,ay)][lane]=p
n=0
for key,lanes in sorted(by_ayah.items()):
    aid,sd,ay=key
    rec={'aid':aid,'ay':ay,'lanes':{}}
    accepted_branches=set(); excluded=[]
    for lane,p in lanes.items():
        d=json.load(open(p,encoding='utf-8'))
        pk=packet(f'{V5}/input/{aid}/{sd}/{ay}/{lane}.discovery.prompt.md')
        cands={}
        if pk:
            for c in pk.get('candidate_inventory',[]):
                cands[c['candidate_id']]={'src':f"{c.get('source_type')}/{c.get('kind')}",'br':set((c.get('branch_refs') or [])+(c.get('focus_branch_refs') or [])+(c.get('nominated_branch_refs') or []))}
        L=collections.Counter()
        for c in d.get('candidate_decisions',[]):
            dec=c.get('decision'); src=(cands.get(c.get('candidate_id')) or {}).get('src','unknown')
            agg[('dec',lane,dec)]+=1; agg[('dec_src',src.split('/')[0],dec)]+=1
            if dec in('reject','narrow'):
                rc=rclass(c.get('reason')); agg[('reason',dec,rc)]+=1
                for be in c.get('branch_exclusions') or []:
                    if isinstance(be,dict):
                        excluded.append((lane,dec,be.get('branch_ref'),rclass(be.get('reason')),be.get('reason')))
                        agg[('excl_kind',kind(be.get('branch_ref')))]+=1
                if dec=='reject':
                    for b in (cands.get(c.get('candidate_id')) or {}).get('br',[]):
                        excluded.append((lane,'reject_cand',b,rc,c.get('reason')))
        for f in d.get('findings',[]):
            if not isinstance(f,dict): continue
            oc=f.get('origin_candidate_id'); cinfo=cands.get(oc) if oc else None
            src='luna_uncandidate' if not oc else (cinfo['src'] if cinfo else 'unknown')
            agg[('find_src',lane,src.split('/')[0])]+=1
            agg[('find_status',(f.get('epistemic') or {}).get('status'))]+=1
            for a in f.get('branch_activations') or []:
                if not isinstance(a,dict): continue
                b=a.get('branch_ref'); mode=a.get('application_mode')
                if b: accepted_branches.add(b)
                nominated = bool(cinfo and b in cinfo['br'])
                who = 'luna_uncandidate_finding' if not oc else ('relayed_branch' if nominated else 'luna_added_branch_in_candidate_finding')
                agg[('act_who',who)]+=1; agg[('act_mode',mode)]+=1; agg[('act_who_src',who,src.split('/')[0])]+=1
                agg[('act_kind',kind(b) if b else 'none')]+=1
                agg[('act_mode_who',mode,who)]+=1
                L['act']+=1
        rec['lanes'][lane]=dict(L)
    lost=[e for e in excluded if e[2] and e[2] not in accepted_branches]
    for e in lost: agg[('lost_excl_reason',e[1],e[3])]+=1; agg[('lost_kind',kind(e[2]))]+=1
    rec['n_excluded']=len(excluded); rec['n_lost_branches']=len(set(e[2] for e in lost)); rec['lost']=sorted(set((e[2],e[3]) for e in lost))
    rec['n_accepted_branches']=len(accepted_branches)
    per_ayah[f'{aid}|{ay}']=rec
    n+=1
    if n%100==0: print(n,round(time.time()-t0),'s',file=sys.stderr)
json.dump({'agg':{ '|'.join(map(str,k)):v for k,v in agg.items()},'per_ayah':per_ayah},open(os.path.join(OUT,'v5_scan.json'),'w'),ensure_ascii=False)
for k in sorted(agg,key=lambda x:(x[0],)+tuple(map(str,x[1:]))):
    print('|'.join(map(str,k)),agg[k])
