#!/usr/bin/env python3
"""Test (1): which branch classes does Opus recall unaided (cold arm) vs when fed the dictionary?

For the 17 ayat with a v9 w10-opus-cold arm, every branch of every identity root of the ayah (roots from the v9
01_dictionary.md headers, ECHO roots excluded; branch data from the Turkish dictionary entries via branches.json)
is searched in each reading with two signals (heuristics, precision checked by hand on the printed evidence):
  AR  : a distinctive Arabic token of the branch (image / what_is / source phrase; unique to the branch within its
        root; absent from the Quran text and from context.md) appears in the reading's Arabic.
  TR  : within ONE sentence, the distinctive Turkish stems of one gloss variant (concept, contextual or lexical gloss;
        5-letter prefixes of words >=4 letters, not stop words, not in any other branch of the root, not in context.md)
        appear: all of them if the variant has <=2 such stems, else >=2.
A branch is 'recalled' by an arm if AR or TR fires. Groups: cold = w10-opus-cold(+cold2); fed = every v9 arm that
saw 01_dictionary.md or package.md (dict, dslim, dhft, ledger, package, v11-script, v11-luna).
Also flags 'cued': the branch's Turkish stems do not help here, so cueing by the English word notes of context.md is
checked by hand for the printed hits (see cold_hits.tsv column cue_check).
Outputs: recall_rows.tsv (ayah x branch), recall_by_class.tsv, cold_hits.tsv.
"""
import csv, json, os, re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
V9 = Path('/Volumes/OZTURK/_projects/prose_generation/_commentary/v9')
QURAN = Path('/Volumes/OZTURK/_projects/quran-data/data/text/quran-uthmani.tsv')
csv.field_size_limit(10**9)

DIAC = re.compile(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]')
AR_WORD = re.compile(r'[ء-يٱ-ۓۺ-ۿؐ-ًؚ-ٰٟۖ-ۭـ]+')
MAP = str.maketrans({'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ى': 'ي', 'ة': 'ه', 'ؤ': 'و', 'ئ': 'ي'})
AR_STOP = set('الذي التي الذين هذا هذه ذلك كان يقال قال اذا على الي عن من في مثل كل بعض غير ليس اي هو هي به له لها ما لا ان او ثم قد فلان فلانا شيء الشيء شي منه فيه عليه كذا وهو وهي والجمع جمع واحد الواحد يكون تقول ويقال اسم ايضا الامر امر معروف'.split())


def norm(w):
    w = DIAC.sub('', w).translate(MAP)
    w = re.sub(r'[^ء-ي]', '', w)
    if len(w) > 3 and w[0] in 'وف':
        w = w[1:]
    for p in ('بال', 'كال', 'فال', 'وال', 'لل'):
        if w.startswith(p) and len(w) > len(p) + 2:
            return w[len(p):]
    if w.startswith('ال') and len(w) > 4:
        w = w[2:]
    return w


def ar_tokens(t):
    return {x for x in (norm(m.group(0)) for m in AR_WORD.finditer(t)) if len(x) >= 3 and x not in AR_STOP}


TR_FOLD = str.maketrans({'İ': 'i', 'I': 'ı', 'Â': 'a', 'â': 'a', 'Î': 'i', 'î': 'i', 'Û': 'u', 'û': 'u'})
TR_STOP = set('''bir olan olarak şey şeyi kişi kimse veya ile gibi için özel yapı biçim biçimde durum türlü ayrı başka kendi
birinin birine birini yer yeri olma olmak etme etmek yapma yapmak hale anlam anlamı çeşitli belirli kullanım kalıp
kalıplaşmış genel tür türü bağlı ilgili gelme getirme verme alma kılma düşme tutma çıkma ortaya kadar üzere karşı doğru
arası arasında üzerinde içinde dışında sonra önce daha çok az bir şeyin bir şeyi birinin başkasının herhangi olması
olmayan olan yapılan edilen bulunan bulunma kılınan veren alan eden eylemi eylem adı adıdır'''.split())


def tr_words(t):
    return re.findall(r'[a-zçğıöşü]+', t.translate(TR_FOLD).lower())


def stems(t):
    return {w[:5] for w in tr_words(t) if len(w) >= 4 and w not in TR_STOP}


QV = set()
for line in QURAN.read_text(encoding='utf-8').splitlines():
    if '|' in line:
        QV |= ar_tokens(line.split('|', 1)[1])

BR = json.load(open(HERE / 'branches.json', encoding='utf-8'))
ROWS = {r['branch_ref']: r for r in csv.DictReader(open(HERE / 'branches.tsv', encoding='utf-8'), delimiter='\t')}
ROWS_BY_ROOT = {r['root_id']: r['root'] for r in ROWS.values()}
WEAK = set('اويىءأإؤئآ')
TL = {'ء': {'', 'e', 'a', 'ʾ', "'"}, 'ا': {'a', 'e', 'ʾ', "'"}, 'ب': {'b'}, 'ت': {'t'}, 'ث': {'s', 'ṯ', 'th'},
      'ج': {'c', 'j', 'ǧ'}, 'ح': {'h', 'ḥ'}, 'خ': {'h', 'ḫ', 'kh', 'ḥ'}, 'د': {'d'}, 'ذ': {'z', 'ẕ', 'dh', 'ḏ', 'ẓ'},
      'ر': {'r'}, 'ز': {'z'}, 'س': {'s'}, 'ش': {'ş', 'š', 'sh'}, 'ص': {'s', 'ṣ'}, 'ض': {'d', 'ḍ', 'z', 'ż'},
      'ط': {'t', 'ṭ'}, 'ظ': {'z', 'ẓ'}, 'ع': {'', 'ʿ', "'", 'a', 'e', '‘'}, 'غ': {'g', 'ğ', 'ġ', 'gh'}, 'ف': {'f'},
      'ق': {'k', 'q', 'ḳ'}, 'ك': {'k'}, 'ل': {'l'}, 'م': {'m'}, 'ن': {'n'}, 'ه': {'h'}, 'و': {'v', 'w', 'u'},
      'ي': {'y', 'i'}, 'ى': {'y', 'i'}}
ROOT_LET = {}


def root_letters(rid):
    if rid not in ROOT_LET:
        lets = ROWS_BY_ROOT.get(rid, '')
        ROOT_LET[rid] = [c.translate(MAP) for c in lets.split()]
    return ROOT_LET[rid]


def root_cue(sent, rid):
    """True when the sentence names the root: an Arabic token containing its radicals in order (weak radicals
    optional), or a hyphenated transliteration like s-r-t / d-r-b of the right length."""
    lets = root_letters(rid)
    if not lets:
        return False
    strong = [c for c in lets if c not in WEAK]
    for m in AR_WORD.finditer(sent):
        w = DIAC.sub('', m.group(0)).translate(MAP)
        i = 0
        for ch in w:
            if i < len(strong) and ch == strong[i]:
                i += 1
        if strong and i == len(strong):
            return True
    lat = [TL.get(c, set()) for c in lets]
    for m in re.finditer(r"\b([^\s\-]{1,3})-([^\s\-]{1,3})-([^\s\-]{1,3})\b", sent):
        parts = [p.lower().strip("ʿʾ'’") for p in m.groups()]
        if len(lat) == 3 and all(any(p.startswith(x) or p == x for x in lat[k]) for k, p in enumerate(parts)):
            return True
    return False


by_root = defaultdict(list)
for ref in BR:
    by_root[ref.split('/')[0]].append(ref)

AYAT = ['1:1', '1:2', '1:3', '1:4', '1:5', '1:6', '1:7', '4:34', '5:6', '18:86', '18:96', '100:1', '100:6', '100:10',
        '103:1', '103:2', '103:3']
COLD = {'w10-opus-cold', 'w10-opus-cold2'}
import sys
STRICT1 = '--single' in sys.argv
FED = {'w10-opus-dict', 'w10-opus-dslim', 'w10-opus-dhft', 'w10-opus-ledger', 'w10-opus', 'v11-script', 'v11-luna'}


def sentences(text):
    return [s for s in re.split(r'(?<=[.!?])\s+|\n+', text) if s.strip()]


out_rows, hits_out = [], []
for ayah in AYAT:
    s, a = ayah.split(':')
    sa = f'{s}_{a}'
    dpath = V9 / 'input' / 'v2' / f's{int(s):03d}' / sa / '01_dictionary.md'
    ctx = (V9 / 'lines' / 'work' / sa / 'context.md').read_text(encoding='utf-8')
    ctx_ar, ctx_tr = ar_tokens(ctx), stems(ctx)
    roots = []
    for line in dpath.read_text(encoding='utf-8').splitlines():
        m = re.match(r'## (?!ECHO)(.+?) \((root_\d{6})\) — (identity root|word-scoped)', line)
        if m and m.group(2) not in roots:
            roots.append(m.group(2))
        m2 = re.match(r'## (?!ECHO)(.+?) \((root_\d{6})\)', line)
        if m2 and m2.group(2) not in roots:
            roots.append(m2.group(2))
    runs = {}
    for arm_dir in (V9 / 'lines' / 'work' / sa / 'synth').iterdir():
        f = arm_dir / f'{sa}.reading.tr.md'
        if arm_dir.name in COLD | FED and f.exists():
            runs[arm_dir.name] = f.read_text(encoding='utf-8')
    for rid in roots:
        refs = by_root.get(rid, [])
        # distinctive Arabic tokens and Turkish stems per branch within the root
        tok = {r: ar_tokens(' '.join([BR[r]['image_ar'], BR[r]['what_is_ar'], BR[r]['phrase_ar']])) for r in refs}
        tcount = Counter(t for r in refs for t in tok[r])
        variants = {r: [BR[r]['concept']] + BR[r]['ctx'] + BR[r]['lex'] for r in refs}
        allst = {r: set().union(*[stems(v) for v in variants[r]]) if variants[r] else set() for r in refs}
        scount = Counter(x for r in refs for x in allst[r])
        for r in refs:
            dist_ar = {t for t in tok[r] if tcount[t] == 1 and t not in ctx_ar and t not in QV}
            vstems = []
            for v in variants[r]:
                st = [x for x in stems(v) if scount[x] == 1 and x not in ctx_tr]
                if st:
                    vstems.append(sorted(set(st)))
            rec = {'ayah': ayah, 'branch_ref': r}
            for arm, text in runs.items():
                at = ar_tokens(text)
                ar_hit = sorted(dist_ar & at)
                tr_hit, ev = None, ''
                for sent in sentences(text):
                    ss = stems(sent)
                    cue = root_cue(sent, rid)
                    for st in vstems:
                        got = [x for x in st if x in ss]
                        if (len(got) >= 2 and cue) or (len(got) == 1 and len(st) == 1 and cue and len(got[0]) == 5 and STRICT1):
                            tr_hit, ev = got, sent.strip()[:300]
                            break
                    if tr_hit:
                        break
                rec[arm] = int(bool(ar_hit or tr_hit))
                if (ar_hit or tr_hit) and arm in COLD:
                    hits_out.append({'ayah': ayah, 'arm': arm, 'branch_ref': r, 'root': ROWS[r]['root'],
                                     'kind': ROWS[r]['branch_kind'], 'root_words': ROWS[r]['root_words'],
                                     'n_sources': ROWS[r]['n_sources'], 'idx': ROWS[r]['idx'],
                                     'concept': BR[r]['concept'][:70], 'ar_hit': ' '.join(ar_hit),
                                     'tr_hit': ' '.join(tr_hit or []), 'evidence': ev.replace('\t', ' ')})
            rec['cold'] = int(any(rec.get(x, 0) for x in COLD))
            rec['fed'] = int(any(rec.get(x, 0) for x in FED))
            rec['n_fed_arms'] = sum(1 for x in runs if x in FED)
            out_rows.append(rec)

# per-class table
def bucket(n):
    n = int(n)
    return '0-1' if n <= 1 else '2-10' if n <= 10 else '11-100' if n <= 100 else '>100'


def cls_rows(keyf, name):
    tab = defaultdict(Counter)
    for rec in out_rows:
        if rec['n_fed_arms'] == 0:
            continue
        R = ROWS[rec['branch_ref']]
        k = keyf(R)
        tab[k]['n'] += 1
        tab[k]['cold'] += rec['cold']
        tab[k]['fed'] += rec['fed']
        tab[k]['both'] += rec['cold'] and rec['fed']
        tab[k]['cold_only'] += rec['cold'] and not rec['fed']
        tab[k]['fed_only'] += rec['fed'] and not rec['cold']
    out = []
    for k in sorted(tab):
        c = tab[k]
        out.append({'class': name, 'value': k, 'branches': c['n'], 'cold_hit': c['cold'], 'fed_hit': c['fed'],
                    'both': c['both'], 'cold_only': c['cold_only'], 'fed_only': c['fed_only'],
                    'cold_rate': round(c['cold'] / c['n'], 3), 'fed_rate': round(c['fed'] / c['n'], 3),
                    'memory_share_of_fed': round(c['both'] / c['fed'], 3) if c['fed'] else ''})
    return out


def primary(R):
    return 'primary' if (int(R['hft_base']) > 0 or int(R['dossier_dominant']) > 0) else 'minor'


table = []
table += cls_rows(lambda R: 'all', 'all')
table += cls_rows(lambda R: bucket(R['root_words']), 'root_words')
table += cls_rows(lambda R: R['branch_kind'], 'branch_kind')
table += cls_rows(lambda R: str(min(int(R['n_sources']), 6)) if int(R['n_sources']) >= 4 else '1-3', 'n_early_sources')
table += cls_rows(lambda R: 'B001' if R['branch'] == 'B001' else 'other', 'branch_idx')
table += cls_rows(primary, 'hft_baseline_or_dossier_plain')
table += cls_rows(lambda R: 'activated' if int(R['hft_any']) + int(R['v12']) > 0 else 'never', 'hft_v12_history')
table += cls_rows(lambda R: primary(R) + '|' + bucket(R['root_words']), 'primary_x_freq')


def dump(name, recs):
    cols = []
    for r in recs:
        for c in r:
            if c not in cols:
                cols.append(c)
    with open(HERE / name, 'w', encoding='utf-8') as fh:
        fh.write('\t'.join(cols) + '\n')
        for r in recs:
            fh.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')


dump('recall_rows.tsv', out_rows)
dump('recall_by_class.tsv', table)
dump('cold_hits.tsv', hits_out)
for t in table:
    print('\t'.join(str(t[c]) for c in ('class', 'value', 'branches', 'cold_hit', 'fed_hit', 'both', 'cold_only',
                                            'fed_only', 'cold_rate', 'fed_rate', 'memory_share_of_fed')))
print('cold hits', len(hits_out))
