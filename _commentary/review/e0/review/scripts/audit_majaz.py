"""Audit the supply's Majaz mapping (read-only: supply/cache/majaz.pkl + v15 quran/words tables).
1) unresolved raw entries whose phrase occurs in a neighbouring surah (header drift?)
2) a seeded sample of mapped entries with the ayah text, for eyeballing."""
import pickle, re, csv, collections, random, json, functools
S = '/Volumes/OZTURK/_projects/prose_generation/_commentary/review/e0/supply'
V15D = '/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data'
m = pickle.load(open(S + '/cache/majaz.pkl', 'rb'))
W = pickle.load(open(S + '/cache/words.pkl', 'rb'))
Q = {r['ref']: r['text'] for r in csv.DictReader(open(V15D + '/quran.tsv', encoding='utf-8'), delimiter='\t')}
DIAC = re.compile('[\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed\u0640]')
def rasm(t):
    t = (t or '').replace('\u0648\u0670', '\u0670').replace('\u0649\u0670', '\u0670'); t = DIAC.sub('', t)
    t = re.sub('[اأإآٱءؤئ]', '', t); return t.replace('ى', 'ي').replace('ة', 'ه')
PROCL = {'و','ف','ب','ل','ك','س','وب','ول','فل','فب','وس','فس','ا','وا','فا','لل','بال','وال','فال'}
def rt(t): return [x for x in (rasm(w) for w in re.findall('[\u0621-\u064a\u0670-\u06d3\u0610-\u061a\u064b-\u065f\u06d6-\u06ed]+', t or '')) if x]
def tm(pt, at):
    if pt == at or (len(pt) >= 3 and (pt == at + 'ي' or at == pt + 'ي')): return True
    for a_, b_ in ((at, pt), (pt, at)):
        if a_.endswith(b_) and len(b_) >= 2 and a_[:len(a_) - len(b_)] in PROCL: return True
    return False
@functools.lru_cache(None)
def art(ref): return [rasm(w['surface']) for w in W.get(ref, [])]
def pin(toks, ref):
    at = art(ref); n = len(toks)
    return any(all(tm(toks[j], at[i + j]) for j in range(n)) for i in range(len(at) - n + 1))
def slen(s):
    n = 0
    while f'{s}:{n+1}' in Q: n += 1
    return n
drift = []
for e in m:
    if e['source'] == 'openiti_raw' and e['ref'] is None and e['basis'] == 'phrase not found in the surah':
        toks = rt(e['phrase'])
        hits = {}
        for s2 in (e['surah'] - 1, e['surah'] + 1):
            if 1 <= s2 <= 114:
                h = [x for x in range(1, slen(s2) + 1) if pin(toks, f'{s2}:{x}')]
                if h: hits[s2] = h
        anyq = sum(1 for s2 in range(1, 115) for x in range(1, slen(s2) + 1) if pin(toks, f'{s2}:{x}')) if len(toks) >= 2 else None
        drift.append(dict(surah=e['surah'], line=e['raw_line'], phrase=e['phrase'], neighbour_hits=hits, quran_hits=anyq))
nb = [d for d in drift if d['neighbour_hits']]
print('raw unresolved "not found in surah":', len(drift), '; found in a neighbouring surah:', len(nb))
for d in nb[:15]: print(' ', d)
nf = [d for d in drift if d['quran_hits'] == 0]
print('multiword phrases found nowhere in the Quran (spelling/typo):', len(nf))
rnd = random.Random(7)
mapped = [e for e in m if e['ref']]
samp = rnd.sample([e for e in mapped if e['source'] == 'openiti_raw'], 15) + rnd.sample([e for e in mapped if e['source'] == 'sqlite'], 10)
out = []
for e in samp:
    out.append(dict(source=e['source'], ref=e['ref'], phrase=e['phrase'], marker=e['marker'], basis=e['basis'], ayah=Q[e['ref']]))
    print(e['source'], e['ref'], '|', e['phrase'], '|', e['basis'], '|', Q[e['ref']][:120])
json.dump(dict(drift=drift, sample=out), open('/Volumes/OZTURK/_projects/prose_generation/_commentary/review/e0/review/out/audit_majaz.json', 'w'), ensure_ascii=False, indent=1)
