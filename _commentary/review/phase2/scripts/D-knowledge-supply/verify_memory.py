#!/usr/bin/env python3
"""Prototype of the post-synthesis verification step (script only), run on the existing v9 readings.

V1 phrase check: every Arabic tag ({ar:..}) that is not Quran text is looked up, diacritics folded, in the FULL
   early-source entries of all roots (dictionary/data/output/root_packets/*.json, dictionary_sources[].entry_text_clean:
   Maqayis, Ayn, Jamhara, Sihah, Tahdhib, Mufradat). Result per tag: quran | early:<sources> | not-found (-> must be
   marked memory). Phase 1 checked against the truncated v9 01_dictionary.md; this re-check uses the full entries.
V2 construction guard: for every collocation / non_bare branch of the ayah's identity roots, a sentence that states
   its sense (a distinctive Turkish stem pair of its gloss in a sentence naming the root, or a distinctive Arabic token
   of its phrase) is flagged unless the same sentence carries the construction: a partner word of the branch's own
   early phrase (content token other than the root word), or a Quran reference whose ayah contains the root and a
   partner. Flags are candidates for a (cheap) second look, never deletions.
Writes verify_memory.tsv and prints a summary."""
import csv, glob, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path
csv.field_size_limit(10**9)
HERE = Path(__file__).resolve().parent
P = Path('/Volumes/OZTURK/_projects')
V9 = P / 'prose_generation/_commentary/v9'
DI = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')
AL = str.maketrans({'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ى': 'ي', 'ة': 'ه', 'ؤ': 'و', 'ئ': 'ي', 'ۥ': '', 'ۦ': ''})


def fold(t):
    return re.sub(r'\s+', ' ', re.sub(r'[^ء-ي ]', ' ', DI.sub('', t or '').translate(AL))).strip()


# ---- corpora
QV = {}
for line in (P / 'quran-data/data/text/quran-uthmani.tsv').read_text(encoding='utf-8').splitlines():
    if '|' in line:
        ref, t = line.split('|', 1)
        s, a = ref.split(':')
        QV[f'{int(s)}:{int(a)}'] = fold(t)
QALL = ' ' + ' '.join(QV.values()) + ' '
EARLY = {}
for f in glob.glob(str(P / 'dictionary/data/output/root_packets/root_*.json')):
    d = json.load(open(f, encoding='utf-8'))
    for s in d.get('dictionary_sources', []):
        t = fold(s.get('entry_text_clean') or '')
        if t and t != '-':
            EARLY.setdefault(s.get('source_id'), []).append(t)
EARLY = {k: ' ' + ' || '.join(v) + ' ' for k, v in EARLY.items()}
B = [r for r in csv.DictReader(open(HERE.parent / 'branches.tsv', encoding='utf-8'), delimiter='\t')]
DICT_TXT = ' ' + ' || '.join(fold(r['phrase_ar'] + ' ; ' + r['what_is_ar'] + ' ; ' + r['image_ar']) for r in B) + ' '
BY = defaultdict(list)
for r in B:
    BY[r['root']].append(r)
ROOTS = {}
for d in sorted((V9 / 'input' / 'v2').glob('s*/*_*')):
    t = (d / '01_dictionary.md').read_text(encoding='utf-8') if (d / '01_dictionary.md').exists() else ''
    ROOTS[d.name] = list(dict.fromkeys(m.group(1) for m in re.finditer(r'^## (?!ECHO)(.+?) \(root_\d{6}\)', t, re.M)))
TAG = re.compile(r'\{\{?ar:([^,}]*)')
TR_FOLD = str.maketrans({'İ': 'i', 'I': 'ı', 'Â': 'a', 'â': 'a', 'Î': 'i', 'î': 'i', 'Û': 'u', 'û': 'u'})
STOP = set('bir olan olarak şey kişi veya ile gibi için yapı biçim durum türlü başka kendi yer olma etme yapma hale anlam '
           'kullanım kalıp genel bağlı ilgili verme alma kılma kadar üzere karşı doğru arası sonra önce daha çok birinin '
           'bulunan eden eylem'.split())


def stems(t):
    return {w[:5] for w in re.findall(r'[a-zçğıöşü]+', t.translate(TR_FOLD).lower()) if len(w) >= 4 and w not in STOP}


def root_named(sent, root):
    strong = [c.translate(AL) for c in root.split() if c not in 'اويءأإؤئى']
    for w in re.findall(r'[ء-يٱ-ۓ]+', DI.sub('', sent)):
        w = w.translate(AL); i = 0
        for ch in w:
            if i < len(strong) and ch == strong[i]:
                i += 1
        if strong and i == len(strong):
            return True
    return False


def partners(r):
    """content tokens of the branch's early phrases other than words built on the root (the construction partners)"""
    toks = Counter()
    for seg in re.split(r'؛|;', r['phrase_ar'] or ''):
        seg = re.sub(r'\([^)]*\)', ' ', seg)
        for w in fold(seg).split():
            w2 = re.sub(r'^(وال|فال|بال|كال|لل|ال|و|ف|ب)', '', w)
            if len(w2) >= 2 and not root_named(w2, r['root']) and w2 not in {'اي', 'اذا', 'يقال', 'قال', 'فلان', 'من', 'الى', 'علي', 'عن'}:
                toks[w2] += 1
    return {w for w, n in toks.items()}


FUNC = {'في', 'من', 'الي', 'علي', 'عن', 'اي', 'اذا', 'يقال', 'قال', 'فلان', 'فلانا', 'الله', 'هو', 'هي', 'ما', 'لا', 'ان', 'كل', 'شيء', 'الشيء'}


def construction_at(ayah_folded, root, part):
    toks = ayah_folded.split()
    pos = [i for i, w in enumerate(toks) if root_named(w, root)]
    near = {re.sub(r'^(وال|فال|بال|كال|لل|ال|و|ف|ب)', '', toks[j]) for i in pos for j in range(max(0, i - 3), min(len(toks), i + 4)) if j != i}
    return any(p in near for p in part if len(p) >= 3 and p not in FUNC)


def sentences(t):
    return [s for s in re.split(r'(?<=[.!?])\s+|\n+', t) if s.strip()]


rows, tagstat, guard = [], defaultdict(Counter), defaultdict(list)
for sa, roots in ROOTS.items():
    synth = V9 / 'lines' / 'work' / sa / 'synth'
    if not synth.exists():
        continue
    for arm in ('w10-opus-cold', 'w10-opus-cold2', 'w10-opus-dict'):
        f = synth / arm / f'{sa}.reading.tr.md'
        if not f.exists():
            continue
        text = f.read_text(encoding='utf-8')
        grp = 'cold' if 'cold' in arm else 'dict'
        # V1
        for tag in TAG.findall(text):
            ft = fold(tag)
            if len(ft.replace(' ', '')) < 3:
                continue
            if f' {ft} ' in QALL or ft in QALL:
                cls = 'quran'
            else:
                src = [k for k, v in EARLY.items() if ft in v]
                cls = ('early:' + '+'.join(sorted(src)) if src else
                       'dictionary-branch' if ft in DICT_TXT else 'not-found')
            tagstat[grp][cls.split(':')[0]] += 1
            if cls != 'quran':
                rows.append({'ayah': sa, 'arm': arm, 'check': 'phrase', 'item': tag.strip(), 'result': cls, 'sentence': ''})
        # V2
        sents = sentences(text)
        for root in roots:
            brs = BY.get(root, [])
            allst = Counter(x for b in brs for x in stems(b['tr_concept'] + ' ' + b['tr_glosses']))
            for b in brs:
                if b['branch_kind'] not in ('collocation', 'non_bare'):
                    continue
                dist = sorted(x for x in stems(b['tr_concept']) if allst[x] == 1)
                part = partners(b)
                for s in sents:
                    got = [x for x in dist if x in stems(s)]
                    if not (root_named(s, root) and len(got) >= min(2, len(dist)) and got):
                        continue
                    focus = f"{int(sa.split('_')[0])}:{int(sa.split('_')[1])}"
                    at_focus = construction_at(QV.get(focus, ''), root, part)
                    refs = [x for x in re.findall(r'\b(\d{1,3}:\d{1,3})\b', s) if x != focus]
                    at_ref = [x for x in refs if construction_at(QV.get(x, ''), root, part)]
                    status = ('construction present at the focus' if at_focus else
                              'cited at its own locus ' + ','.join(at_ref) + ' (check it is not transferred)' if at_ref else
                              'FLAG: construction absent at the focus and not cited')
                    guard[grp].append(status)
                    rows.append({'ayah': sa, 'arm': arm, 'check': 'construction', 'item': f"{root} {b['branch']} {b['branch_kind']} ({b['tr_concept'][:40]})",
                                 'result': status, 'sentence': re.sub(r'\{\{?ar:([^,]*), tr:[^,]*, gloss:([^}]*)\}\}?', r'[\1 = \2]', s)[:300]})
with open(HERE / 'verify_memory.tsv', 'w', encoding='utf-8') as fh:
    fh.write('ayah\tarm\tcheck\titem\tresult\tsentence\n')
    for r in rows:
        fh.write('\t'.join(str(r[k]).replace('\t', ' ') for k in ('ayah', 'arm', 'check', 'item', 'result', 'sentence')) + '\n')
for g in ('cold', 'dict'):
    print(f'{g}: Arabic tags {dict(tagstat[g])}; construction-bound sense statements {Counter(guard[g])}')
print('\nnot-found tags (cold):', [r['item'] for r in rows if r['check'] == 'phrase' and r['result'] == 'not-found' and 'cold' in r['arm']])
print('not-found tags (dict):', [r['item'] for r in rows if r['check'] == 'phrase' and r['result'] == 'not-found' and 'dict' in r['arm']][:20])
print('\nconstruction statements:')
for r in rows:
    if r['check'] == 'construction':
        print(f"  {r['ayah']:7} {r['arm']:15} {r['item'][:60]:60} {r['result']}\n        {r['sentence'][:230]}")
