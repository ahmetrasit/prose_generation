"""Shared read-only loaders for the C2 prototypes (loaded words, construction guard, parallels, harvest sheet).

Reads only: v15 base tables (words/lemmas/branches/quran), quran-data dictionary tr entries (branch_kind +
aligned occurrences with grammar attachments), root-dossier activation map, qira'at. Writes caches only into
this scratch folder.
"""
import csv, re, json, pickle, math, os, glob, collections
from functools import lru_cache

csv.field_size_limit(10**9)
P = '/Volumes/OZTURK/_projects'
V15 = P + '/prose_generation/_commentary/v15/data'
HERE = os.path.dirname(os.path.abspath(__file__))

DIAC = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')


def strip(s):
    s = DIAC.sub('', s or '')
    s = re.sub('[ٱأإآا]', 'ا', s)
    s = s.replace('ى', 'ي').replace('ة', 'ه').replace('ؤ', 'ء').replace('ئ', 'ء')
    return s


def nroot(r):
    r = (r or '').strip()
    r = re.sub('[أإآؤئ]', 'ء', r)
    r = r.replace('ى', 'ي')
    if ' ' not in r and len(r) >= 3:
        r = ' '.join(r)
    return r


def surah(ref):
    return int(ref.split(':')[0])


@lru_cache(maxsize=1)
def quran():
    out = {}
    for r in csv.DictReader(open(V15 + '/quran.tsv', encoding='utf-8'), delimiter='\t'):
        out[r['ref']] = r['text']
    return out


@lru_cache(maxsize=1)
def refs():
    return list(quran().keys())


@lru_cache(maxsize=1)
def words():
    """ref -> list of word dicts (w:int, ref3, surface, roots[list], lemmas[list], pos)."""
    out = collections.defaultdict(list)
    for r in csv.DictReader(open(V15 + '/words.tsv', encoding='utf-8'), delimiter='\t'):
        out[f"{r['surah']}:{r['ayah']}"].append(dict(
            w=int(r['w']), ref3=r['ref'], surface=r['surface'],
            roots=[nroot(x) for x in r['roots'].split('|') if x],
            lemmas=[x for x in r['lemmas'].split('|') if x], pos=r['pos']))
    return out


@lru_cache(maxsize=1)
def root_df():
    df = collections.Counter()
    for ref, ws in words().items():
        for x in {r for w in ws for r in w['roots']}:
            df[x] += 1
    return df


@lru_cache(maxsize=1)
def lemma_df():
    df = collections.Counter()
    for ref, ws in words().items():
        for x in {(w['roots'][0] if w['roots'] else '', l) for w in ws for l in w['lemmas']}:
            df[x] += 1
    return df


def idf_root(r):
    N = len(refs())
    return math.log(N / max(1, root_df().get(r, 1)))


@lru_cache(maxsize=1)
def root_ids():
    """root letters -> [root_id,...] and root_id -> root letters (v15 branches.tsv)."""
    r2i = collections.defaultdict(list)
    i2r = {}
    for r in csv.DictReader(open(V15 + '/branches.tsv', encoding='utf-8'), delimiter='\t'):
        rt = nroot(r['root'])
        if r['root_id'] and r['root_id'] not in r2i[rt]:
            r2i[rt].append(r['root_id'])
        if r['root_id']:
            i2r[r['root_id']] = rt
    return dict(r2i), i2r


@lru_cache(maxsize=1)
def trcache():
    p = os.path.join(HERE, 'tr_cache.pkl')
    if not os.path.exists(p):
        build_trcache(p)
    return pickle.load(open(p, 'rb'))


def build_trcache(p):
    br, occ = {}, {}
    for f in sorted(glob.glob(P + '/quran-data/data/dictionary/tr/*_entry.json')):
        d = json.load(open(f))
        rid = d['root_envelope_id']
        for b in d['branches']:
            br[b['branch_ref']] = dict(
                kind=b['lexicalization_scope']['branch_kind'], note=b['lexicalization_scope'].get('note', ''),
                image=b.get('branch_image_ar', ''), what=b.get('what_is_ar', ''), whatnot=b.get('what_is_not_ar', ''),
                phr=b.get('source_phrase_ar', ''), gloss=(b.get('concept_gloss') or {}).get('text', ''),
                nd=[(x.get('neighbor_ref'), x.get('relation_type')) for x in b.get('neighbor_distinctions') or []])
        for o in d['occurrence_evidence'].get('occurrences', []):
            a = o.get('alignment', {})
            occ.setdefault(o['qac_word_ref'], []).append(dict(
                rid=rid, lemma=o.get('lemma_ar'), pos=o.get('pos'), aspect=o.get('aspect'), voice=o.get('voice'),
                stem=o.get('stem_ar'), status=a.get('status'),
                atts=[(x.get('relation'), x.get('focus_role'), nroot(x.get('other_root') or ''), x.get('prep_base') or '',
                       x.get('other_surface') or '') for x in a.get('attachments') or []]))
    pickle.dump(dict(br=br, occ=occ), open(p, 'wb'))


def branches_of_root(root):
    """[(branch_ref, info)] for all root_ids of a root letters string (11 roots have two entries)."""
    r2i, _ = root_ids()
    br = trcache()['br']
    out = []
    for rid in r2i.get(root, []):
        k = 1
        while True:
            ref = f'{rid}/B{k:03d}'
            if ref not in br:
                break
            out.append((ref, br[ref]))
            k += 1
    return out


@lru_cache(maxsize=1)
def dossier():
    """word ref (S:A:W) -> dict(branch_ref, role, group, root) from root-dossier activation_map (dominant rows)."""
    out = {}
    for r in csv.DictReader(open(P + '/root-dossier/out/activation_map.tsv', encoding='utf-8'), delimiter='\t'):
        if r['role'] == 'dominant':
            out[r['qac_word_ref']] = dict(b=r['branch_ref'], group=r['group'], root=nroot(r['root']))
    return out


@lru_cache(maxsize=1)
def dossier_roots():
    return {v['root'] for v in dossier().values()}


@lru_cache(maxsize=1)
def qiraat():
    out = collections.defaultdict(list)
    for r in csv.DictReader(open(P + '/study/_project_corpus/qiraat.tsv', encoding='utf-8'), delimiter='\t'):
        out[r['tsv_word_ref']].append(r)
    return out


# ---- tokens for phrase matching ---------------------------------------------------------------
PRON = ('هما', 'كما', 'هم', 'هن', 'كم', 'كن', 'نا', 'ها', 'ه', 'ك', 'ي')
PART_BASE = {'علي': 'على', 'على': 'على', 'الي': 'الى', 'الى': 'الى', 'في': 'في', 'من': 'من', 'عن': 'عن',
             'ل': 'ل', 'ب': 'ب', 'مع': 'مع', 'عند': 'عند', 'بين': 'بين', 'لدي': 'لدى', 'ان': 'ان', 'لكن': 'لكن',
             'حتي': 'حتى', 'ما': 'ما', 'لا': 'لا', 'لم': 'لم', 'لن': 'لن', 'اذا': 'اذا', 'قد': 'قد', 'ثم': 'ثم',
             'او': 'او', 'الذي': 'الذي', 'الذين': 'الذين', 'التي': 'التي', 'هو': 'هو', 'هي': 'هي', 'انما': 'انما'}


def particle_token(surface):
    s = strip(surface)
    for pre in ('و', 'ف'):
        if s.startswith(pre) and len(s) > 2 and s[1:] not in ('ي',):
            s2 = s[1:]
            if any(s2.startswith(b) for b in PART_BASE) or s2 in PART_BASE:
                s = s2
                break
    if s in PART_BASE:
        return PART_BASE[s]
    for p in PRON:
        if s.endswith(p) and len(s) > len(p):
            b = s[:-len(p)]
            if b in PART_BASE:
                return PART_BASE[b] + '+P'
            if b.startswith('ل') and b[1:] in ('', ) :
                return 'ل+P'
    if s in ('له', 'لها', 'لهم', 'لهن', 'لكم', 'لنا', 'لي', 'لك', 'بهم', 'به', 'بها', 'بكم'):
        return s[0] + '+P'
    return s


def word_token(w):
    if w['lemmas']:
        return 'L:' + strip(w['lemmas'][0])
    return 'P:' + particle_token(w['surface'])
