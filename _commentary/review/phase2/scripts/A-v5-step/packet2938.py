"""29:38 packet from git-history v5 files (commit 4f34d87ff, analysis s029-p03-ledger-20260909)."""
import json, lib, digest, supplement as S, packet
base = lib.W + '/git2938'
disc = {l: json.load(open(f'{base}/{l}.discovery.json')) for l in lib.LANES}
def pk(l):
    t = open(f'{base}/{l}.discovery.prompt.md', encoding='utf-8').read()
    i = t.find('<lane_packet_json>'); j = t.find('</lane_packet_json>')
    return json.loads(t[i + len('<lane_packet_json>'):j])
packets = {l: pk(l) for l in lib.LANES}
D = digest.build('29:38', disc=disc, packets=packets, raw_dir='git:4f34d87ff:_commentary/v5/raw/s029-p03-ledger-20260909/s029/29_38')
parts = dict(brief=open(lib.W + '/brief_draft.md').read(), core=packet.core('29:38'),
             branches=digest.render(D, 'branches_only'))
parts['coalitions_setasides'] = digest.render(D, 'packet')[len(parts['branches']):]
sup = S.render_supp('29:38', D)
lines = sup.split('\n'); out = []; inF = False; n = 0
for ln in lines:
    if ln.startswith('## F.'): inF = True; out.append(ln); continue
    if ln.startswith('## ') and inF: inF = False
    if inF:
        n += 1
        if n > 40: continue
    out.append(ln)
parts['supplements'] = '\n'.join(out)
txt = '\n\n'.join(parts.values())
open(lib.W + '/out/packet_29_38.txt', 'w').write(txt)
print({k: lib.cal_tokens(v) for k, v in parts.items()}, 'TOTAL', lib.cal_tokens(txt))
for ln in txt.split('\n'):
    if 'B010' in ln and ('س ب ل' in ln or 'Webbed' in ln or 'عنكبوت' in ln): print(ln[:400])
