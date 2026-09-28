"""Generic analogue of the 29:38 watch case, from an independent labeller (HFT, Sol max): surprising_valid_outliers
whose first trace step activates a non-B001 branch of a word IN the focus ayah and whose trace also cites another
root of the SAME ayah (the neighbour activator). Named-case surahs are excluded. Read-only; writes hft_na_set.json."""
import json,glob,os,random,collections
R='/Volumes/OZTURK/_projects/latent_activation/focus_trace/runs'
EXCL={1,4,5,18,29,100,103,96,15,38,32}
out=[]
for f in glob.glob(R+'/s*/readers/reader_hft_a/*.focus_trace.json'):
    try: d=json.load(open(f))
    except Exception: continue
    ref=d.get('focus_ref') or os.path.basename(f).split('.')[0].replace('_',':')
    s,a=map(int,ref.replace('_',':').split(':'))
    if s in EXCL: continue
    for o in d.get('surprising_valid_outliers') or []:
        tr=o.get('activation_trace') or []
        if not tr: continue
        t0=tr[0]
        if t0.get('source_ref')!=f'{s}:{a}' or t0.get('branch_id') in (None,'B001'): continue
        nb=[t for t in tr[1:] if t.get('source_ref')==f'{s}:{a}' and t.get('root')!=t0.get('root')]
        if not nb: continue
        out.append(dict(ayah=f'{s}:{a}',root=t0['root'],rid=t0.get('mapped_root_id'),branch=t0['branch_id'],
                        widx=t0.get('source_word_indices'),activators=[(t['root'],t['branch_id']) for t in nb],
                        oid=o.get('outlier_id'),conf=o.get('confidence')))
print('cases',len(out),'ayat',len({c['ayah'] for c in out}))
random.seed(20260928)
by=collections.defaultdict(list)
for c in out: by[c['ayah']].append(c)
ay=sorted(by); random.shuffle(ay)
sample=ay[:40]
json.dump(dict(all=out,sample=sample),open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'hft_na_set.json'),'w'),ensure_ascii=False)
print('sample ayat',len(sample),'cases in sample',sum(len(by[x]) for x in sample)); print(sample[:10])
