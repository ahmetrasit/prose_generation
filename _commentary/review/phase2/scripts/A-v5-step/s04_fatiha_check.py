# Evaluation only (never a prompt input): are the North Star Fatiha chain ingredients present in v5's S1 harvest,
# in which lane/ayah, with what status, relayed or Luna's own; and were any excluded?
import json, os, re, collections
V5='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
BI=json.load(open('out/branch_index.json'))
GOLD={'root_001040/B002':'waymark','root_001040/B005':'ʿaylam well','root_001444/B006':'road middle','root_001444/B008':'lead animal',
 'root_001444/B007':'water as mainstay','root_000973/B005':'trodden road','root_000858/B002':'swallowing road','root_000913/B005':'stray animal',
 'root_000532/B014':'herd (rabrab)','root_000532/B013':'gathered water','root_000532/B008':'hanging clouds','root_001273/B012':'well frame/pulley',
 'root_001273/B016':'water standing','root_001583/B008':'walking leaning on others','root_001064/B006':'herd of wild asses','root_001525/B005':'livestock'}
def packet(p):
    t=open(p,encoding='utf-8').read(); i=t.find('<lane_packet_json>'); j=t.find('</lane_packet_json>')
    return json.loads(t[i+len('<lane_packet_json>'):j])
res=collections.defaultdict(list)
for a in range(1,8):
    for lane in ['micro','macro','global']:
        d=json.load(open(f'{V5}/raw/s001-fresh-20260910/s001/1_{a}/{lane}.discovery.json'))
        pk=packet(f'{V5}/input/s001-fresh-20260910/s001/1_{a}/{lane}.discovery.prompt.md')
        cands={c['candidate_id']:c for c in pk['candidate_inventory']}
        inreg=set(b.get('branch_ref') for b in pk.get('branch_registry',[]) if isinstance(b,dict))
        for f in d['findings']:
            oc=f.get('origin_candidate_id'); c=cands.get(oc)
            for act in f.get('branch_activations',[]):
                b=act.get('branch_ref')
                if b in GOLD:
                    nominated = bool(c and b in set((c.get('branch_refs') or [])+(c.get('nominated_branch_refs') or [])+(c.get('focus_branch_refs') or [])))
                    who=('relay:'+c['source_type']) if nominated else ('luna:'+(c['source_type'] if c else 'uncandidate'))
                    res[b].append(f"1:{a} {lane} ACT {f['epistemic']['status']} {act.get('application_mode')} {who}")
        for cd in d['candidate_decisions']:
            for be in cd.get('branch_exclusions') or []:
                if be.get('branch_ref') in GOLD: res[be['branch_ref']].append(f"1:{a} {lane} EXCL({cd['decision']}): {be.get('reason','')[:110]}")
            if cd['decision']=='reject':
                c=cands.get(cd['candidate_id']) or {}
                for b in set((c.get('branch_refs') or [])+(c.get('nominated_branch_refs') or [])):
                    if b in GOLD: res[b].append(f"1:{a} {lane} REJECTED-CAND: {cd['reason'][:110]}")
        for b in GOLD:
            if b in inreg: res[b+'#reg'].append(f'1:{a}{lane[:2]}')
for b,lab in GOLD.items():
    acts=[x for x in res[b] if ' ACT ' in x]
    print(f'## {b} {BI[b]["root"]} [{BI[b]["kind"]}] {lab}: {len(acts)} activations; in registry: {",".join(res[b+"#reg"])[:120]}')
    c=collections.Counter(re.sub(r'^(1:\d) (\w+) ACT (\w+) (\w+) (\S+)$',r'\1 \2 \3 \5',x) for x in acts)
    for k,v in sorted(c.items()): print('    ',k,'x',v)
    for x in res[b]:
        if ' ACT ' not in x: print('    ',x)
