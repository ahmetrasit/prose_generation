"""Script-only 'v5-like' digest for any ayah with HFT traces (no Luna): coalitions = HFT models (baseline/delta/outlier)
with their branches, carriers and changed reading; plus v12 anchors. Same branch-index format as digest.py."""
import json, glob, collections, sys, re
import lib
FT = '/Volumes/OZTURK/_projects/latent_activation/focus_trace/runs'
def build(ref):
    s, a = ref.split(':')
    files = glob.glob(f'{FT}/s{s}/readers/*/{s}_{a}.focus_trace.json') + glob.glob(f'{FT}/s{s}/readers/*/{s}_{a}.*.focus_trace.json')
    branches = collections.OrderedDict(); coal = []
    for p in files:
        d = json.load(open(p))
        for k in ('baseline_models', 'context_deltas', 'surprising_valid_outliers'):
            for m in d.get(k) or []:
                bl = []
                for st in m.get('activation_trace') or []:
                    if not (st.get('mapped_root_id') and st.get('branch_id')): continue
                    b = f"{st['mapped_root_id']}/{st['branch_id']}"
                    bi = branches.setdefault(b, dict(carriers=set(), roles=[], models=[]))
                    bi['carriers'].add(f"{st.get('source_ref')} {st.get('source_phrase_ar','')}")
                    if st.get('assigned_role'): bi['roles'].append(st['assigned_role'])
                    bi['models'].append(m.get('model_id'))
                    if b not in bl: bl.append(b)
                cr = (m.get('changed_reading') or {}).get('after') or m.get('mechanism') or ''
                coal.append((m.get('model_id'), cr, bl))
    return files, branches, coal
def render(ref):
    idx, roots = lib.dict_index(); rmap = lib.root_ar_map()
    files, branches, coal = build(ref)
    L = [f"# script digest {ref} from {len(files)} HFT trace files (no Luna)", "## Branches"]
    for b, bi in branches.items():
        di = idx.get(b, {})
        ph = (di.get('phrase_ar') or '').split('؛')[0][:160]
        L.append(f"- {rmap.get(b.split('/')[0])} {b.split('/')[1]} [{di.get('kind')}] {di.get('gloss')} | {ph} | carriers: {'; '.join(sorted(bi['carriers'])[:4])} | roles: {' / '.join(dict.fromkeys(bi['roles']))[:200]}")
    L.append("## Coalitions (HFT models)")
    groups = collections.OrderedDict()
    for mid, cr, bl in coal:
        g = groups.setdefault(tuple(sorted(bl)), [])
        g.append(str(mid or (cr or '')[:60]))
    for k, mids in groups.items():
        L.append(f"- {' / '.join(dict.fromkeys(mids))[:200]} [{','.join(rmap.get(b.split('/')[0],'?')+'/'+b.split('/')[1] for b in k[:12])}]")
    return '\n'.join(L), branches
if __name__ == '__main__':
    for ref in sys.argv[1:] or ['29:38', '18:86', '18:96', '100:1']:
        t, br = render(ref)
        open(f'{lib.W}/out/pseudo_digest_{ref.replace(":","_")}.txt', 'w').write(t)
        print(ref, 'branches', len(br), 'tokens', lib.cal_tokens(t), 'has sabal B010:', 'root_000672/B010' in br)
