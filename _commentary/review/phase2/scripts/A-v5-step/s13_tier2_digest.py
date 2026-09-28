# Tier-2 adapter prototype: same digest, harvest taken from HFT traces + v12 cross-run findings (no v5, no Luna).
# Usage: python3 s13_tier2_digest.py 29:38 29:41 100:1
import sys, os, json, glob
H_=os.path.dirname(os.path.abspath(__file__))
argv=sys.argv[1:]; sys.argv=['x']
exec(open(os.path.join(H_,'s05_digest.py')).read().rsplit("\nif __name__=='__main__':",1)[0])
HFT='/Volumes/OZTURK/_projects/latent_activation/focus_trace/runs'
V12={}
for p in glob.glob('/Volumes/OZTURK/_projects/quran-data/data/analysis/ayah-activation/v12-cross-run/tr/*_ayah_findings_publication.json'):
    for ay in json.load(open(p)).get('ayat',[]): V12[ay['ayah_ref']]=ay.get('findings',[])
def lanes_tier2(ref):
    s,a=ref.split(':'); L={'micro':{'findings':[],'candidate_decisions':[]},'macro':{'findings':[],'candidate_decisions':[]},'global':{'findings':[],'candidate_decisions':[]}}
    for p in glob.glob(f'{HFT}/s{s}/readers/*/{s}_{a}.focus_trace.json'):
        d=json.load(open(p))
        for sec,lane in (('baseline_models','micro'),('context_deltas','macro'),('surprising_valid_outliers','macro')):
            for m in d.get(sec,[]):
                acts=[{'branch_ref':f"{t['mapped_root_id']}/{t['branch_id']}",'application_mode':'attributed','carrier_refs':[t.get('source_ref')],'trigger_refs':[t.get('source_ref')]} for t in (m.get('activation_trace') or []) if t.get('mapped_root_id') and t.get('branch_id')]
                cr=m.get('changed_reading') or {}
                claim=(cr.get('after') if isinstance(cr,dict) else None) or m.get('mechanism') or ''
                L[lane]['findings'].append({'title':(m.get('model_id') or m.get('delta_id') or m.get('outlier_id') or sec).replace('_',' '),'claim':claim,'branch_activations':acts})
        for m in d.get('discarded_or_unchanged',[]) or []:
            for t in (m.get('activation_trace') or []) if isinstance(m,dict) else []:
                if t.get('mapped_root_id') and t.get('branch_id'):
                    L['macro']['candidate_decisions'].append({'decision':'reject','branch_exclusions':[{'branch_ref':f"{t['mapped_root_id']}/{t['branch_id']}",'reason':'HFT discarded'}]})
    for f in V12.get(ref,[]):
        acts=[{'branch_ref':f'{rid}/{b}','application_mode':'attributed','carrier_refs':[w],'trigger_refs':[w]} for w,rid,brs in f.get('anchors',[]) for b in brs]
        L['global']['findings'].append({'title':'v12 reading ('+f.get('grade','')+')','claim':f.get('text',''),'branch_activations':acts})
    return L,None
lanes_for=lanes_tier2
DG2=os.path.join(OUT,'digests_tier2'); os.makedirs(DG2,exist_ok=True); DG=DG2
print('ayah\tdigest_bytes\t~tokens\tlookup_bytes\tfindings\tbranches\tset_aside')
for ref in argv:
    db,lb,secs,nf,na,ns=build(ref)
    print(f"{ref}\t{db}\t{db//2}\t{lb}\t{nf}\t{na}\t{ns}")
