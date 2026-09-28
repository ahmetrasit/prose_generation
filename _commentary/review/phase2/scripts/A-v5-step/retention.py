"""Heuristic: how many distinct branches activated in v5 discovery reach the v5 editorial (the Sol/Astra CE output)?
Signal: the branch's Turkish gloss content-word stems (5-letter prefixes, words >=5 letters, stopwords removed) found in the
editorial (all stems if the gloss has <=2 content words, else >=2), OR a distinctive Arabic token of the branch image
(>=4 letters, not in the focus ayah text) found in the editorial. Lower-bound-ish; paraphrase escapes it."""
import json, re, glob, random, collections
import lib
from watch import editorial_text
from kinds import norm
PB = json.load(open(lib.W + '/cache/per_branch.json'))
idx, roots = lib.dict_index()
TRS = set('bir veya ile olan olarak gibi için özellikle belirli kişi şeyi şeyin kendi başka birinin yapma etme olma durumu hale haline'.split())
def fold(s): return s.replace('İ','i').replace('I','ı').lower()
def stems(g):
    ws=[w for w in re.findall(r'[a-zçğıöşüâîû]+', fold(g or '')) if len(w)>=5 and w not in TRS]
    return [w[:5] for w in ws]
random.seed(11)
refs = [r for r in PB if not r.startswith('1:')]
sample = random.sample(refs, 150) + [r for r in PB if r.startswith('1:')]
res = collections.Counter()
for r in sample:
    ed = editorial_text(r)
    if not ed: continue
    edf = fold(ed); edn = norm(ed)
    ayah = norm(lib.quran_text().get(r, ''))
    grp = 'S1' if r.startswith('1:') else 'other'
    for b in PB[r]:
        di = idx.get(b)
        if not di: continue
        st = stems(di['gloss'])
        hit_tr = bool(st) and (sum(1 for s in st if s in edf) >= (len(st) if len(st) <= 2 else 2))
        artoks = [t for t in re.findall(r'[ء-ي]+', norm(di.get('image_ar') or '')) if len(t) >= 4 and t not in ayah]
        hit_ar = any(t in edn for t in artoks)
        cls = 'B001' if b.endswith('/B001') else ('collocation' if di['kind']=='collocation' else 'other_branch')
        res[(grp, cls, 'n')] += 1
        if hit_tr or hit_ar: res[(grp, cls, 'hit')] += 1
out = {}
for (g, c, k), v in sorted(res.items()):
    if k == 'n':
        out[f'{g}|{c}'] = f"{res[(g,c,'hit')]}/{v} = {res[(g,c,'hit')]/v:.2f}"
print(json.dumps(out, indent=1))
json.dump(out, open(lib.W + '/out/retention.json', 'w'), indent=1)
