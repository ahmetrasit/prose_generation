# Can a script-only harvest (HFT traces + channel subchannels + v12 cross-run anchors) reproduce v5's activated branches?
# For v5 ayat whose surah has HFT: V = branches in v5 activations (all lanes); H = union of the three script sources for that ayah.
import json, glob, os, re, collections, statistics as st, sys
H_=os.path.dirname(os.path.abspath(__file__))
sys.argv=['x']; exec(open(os.path.join(H_,'s05_digest.py')).read().rsplit("\nif __name__=='__main__':",1)[0])
V5='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
HFT='/Volumes/OZTURK/_projects/latent_activation/focus_trace/runs'
def hft_branches(s,a):
    out=set()
    for p in glob.glob(f'{HFT}/s{s}/readers/*/{s}_{a}.focus_trace.json'):
        d=json.load(open(p))
        for sec in ('baseline_models','context_deltas','surprising_valid_outliers'):
            for m in d.get(sec,[]):
                for t in m.get('activation_trace',[]) or []:
                    if t.get('mapped_root_id') and t.get('branch_id'): out.add(f"{t['mapped_root_id']}/{t['branch_id']}")
    return out
v12={}
for p in glob.glob('/Volumes/OZTURK/_projects/quran-data/data/analysis/ayah-activation/v12-cross-run/tr/*_ayah_findings_publication.json'):
    d=json.load(open(p))
    for ay in d.get('ayat',[]):
        bs=set()
        for f in ay.get('findings',[]):
            for w,rid,brs in f.get('anchors',[]):
                for b in brs: bs.add(f'{rid}/{b}')
        v12[ay['ayah_ref']]=bs
chan_cache={}
def chan_branches(s,a):
    if s not in chan_cache: chan_cache[s]=channels(s)
    ref=f'{s}:{a}'; out=set()
    for c in chan_cache[s]:
        if ref in c['ayat']: out|={m[1] for m in c['motifs'] if not m[1].startswith('?')}
    return out
res=[]; missing_examples=collections.Counter(); mode_missing=collections.Counter()
for p in sorted(glob.glob(V5+'/raw/*/*/*/macro.discovery.json')):
    aid,sd,ay=p[len(V5)+5:].split('/')[:3]
    if 'basmala' in aid or aid.startswith(('s013','s014','s029','s001')): continue
    s,a=map(int,ay.split('_'))
    if a==0 or not os.path.isdir(f'{HFT}/s{s}'): continue
    V=collections.Counter(); modes={}
    for lane in ('micro','macro','global'):
        f=os.path.dirname(p)+f'/{lane}.discovery.json'
        if not os.path.exists(f): continue
        d=json.load(open(f))
        for fi in d.get('findings',[]):
            if not isinstance(fi,dict): continue
            for x in fi.get('branch_activations') or []:
                if isinstance(x,dict) and x.get('branch_ref'): V[x['branch_ref']]+=1; modes.setdefault(x['branch_ref'],x.get('application_mode'))
    hb=hft_branches(s,a); cb=chan_branches(s,a); vb=v12.get(f'{s}:{a}',set())
    H=hb|cb|vb
    if not V: continue
    cov=len(set(V)&H)/len(V)
    res.append((f'{s}:{a}',len(V),len(H),cov,len(set(V)&hb)/len(V),len(set(V)&cb)/len(V),len(set(V)&vb)/len(V),len(H-set(V))))
    for b in set(V)-H: mode_missing[modes[b]]+=1
print('ayat',len(res))
for i,k in enumerate(['V_branches','H_branches','coverage_all','cov_hft','cov_channel','cov_v12','H_not_in_V'],start=1):
    v=[r[i] for r in res]; print(k,'median',round(st.median(v),3),'mean',round(st.mean(v),3))
print('modes of v5 branches not in script harvest',mode_missing.most_common())
json.dump(res,open(os.path.join(OUT,'script_harvest_coverage.json'),'w'))
