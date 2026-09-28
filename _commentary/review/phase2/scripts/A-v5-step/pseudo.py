"""Could a script build the v5 branch harvest without Luna? For every v5 ayah: the union of branches named by
(a) HFT focus traces for that focus ayah (all reader files), (b) v12 cross-run anchors for that ayah,
(c) channel-review motifs of subchannels anchored at that ayah; compared with v5's activated branch set."""
import json, glob, re, os, collections
import lib
from supplement import channels
PB = json.load(open(lib.W + '/cache/per_branch.json'))
FT = '/Volumes/OZTURK/_projects/latent_activation/focus_trace/runs'
V12 = '/Volumes/OZTURK/_projects/quran-data/data/analysis/ayah-activation/v12-cross-run/tr'
rmap = lib.root_ar_map(); inv = {}
for rid, r in rmap.items(): inv.setdefault(r.replace(' ', ''), rid)
def hft(ref):
    s, a = ref.split(':'); out = set(); nfiles = 0
    for p in glob.glob(f'{FT}/s{s}/readers/*/{s}_{a}.focus_trace.json') + glob.glob(f'{FT}/s{s}/readers/*/{s}_{a}.*.focus_trace.json'):
        nfiles += 1
        try: d = json.load(open(p))
        except Exception: continue
        for k in ('baseline_models', 'context_deltas', 'surprising_valid_outliers'):
            for m in d.get(k) or []:
                for st in m.get('activation_trace') or []:
                    if st.get('mapped_root_id') and st.get('branch_id'):
                        out.add(f"{st['mapped_root_id']}/{st['branch_id']}")
    return out, nfiles
V12C = {}
def v12(ref):
    s = ref.split(':')[0]
    if s not in V12C:
        V12C[s] = {}
        p = f'{V12}/{s}_ayah_findings_publication.json'
        if os.path.exists(p):
            for ay in json.load(open(p))['ayat']:
                V12C[s][ay['ayah_ref']] = {f'{rid}/{b}' for f in ay.get('findings', []) for w, rid, bs in f.get('anchors', []) for b in bs}
    return V12C[s].get(ref, set())
def chan(ref):
    out = set()
    for c in channels(ref):
        for r, b in re.findall(r'`([^`:]+):(B\d+)', c['motifs']):
            rid = inv.get(r.replace(' ', '').replace('quranic', ''))
            if rid: out.add(f'{rid}/{b}')
        for rid, b in re.findall(r'(root_\d+):(B\d+)', c['motifs']):
            out.add(f'{rid}/{b}')
    return out
tot = collections.Counter(); per_s = collections.defaultdict(collections.Counter)
for ref, pb in PB.items():
    v5 = set(pb)
    h, nf = hft(ref); w = v12(ref); c = chan(ref)
    if nf == 0: tot['no_hft_ayat'] += 1
    u = h | w | c
    tot['ayat'] += 1; tot['v5'] += len(v5); tot['hft'] += len(h); tot['union'] += len(u)
    tot['v5_in_hft'] += len(v5 & h); tot['v5_in_union'] += len(v5 & u); tot['union_not_v5'] += len(u - v5)
    s = ref.split(':')[0]
    per_s[s]['v5'] += len(v5); per_s[s]['in_union'] += len(v5 & u)
print(dict(tot))
print('v5 branches found by HFT alone: %.3f; by HFT+v12+channels: %.3f; extra branches in union not in v5: %d' % (tot['v5_in_hft']/tot['v5'], tot['v5_in_union']/tot['v5'], tot['union_not_v5']))
print({s: round(c['in_union']/c['v5'],2) for s, c in sorted(per_s.items(), key=lambda x: int(x[0]))})
json.dump(dict(tot), open(lib.W + '/out/pseudo.json', 'w'))
