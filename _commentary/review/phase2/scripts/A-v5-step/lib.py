"""Shared read-only loaders for the A-v5-step Phase 2 prototype.
Reads v5 raw/input, the quran-data dictionary, quran-slm concordance. Writes nothing into any repo."""
import json, os, re, glob, csv, collections, functools, pickle

PG = '/Volumes/OZTURK/_projects/prose_generation'
V5 = PG + '/_commentary/v5'
DICT = '/Volumes/OZTURK/_projects/quran-data/data/dictionary/tr'
SLM = '/Volumes/OZTURK/_projects/quran-slm/resources/source'
W = os.path.dirname(os.path.abspath(__file__))
CACHE = W + '/cache'
os.makedirs(CACHE, exist_ok=True)
LANES = ('micro', 'macro', 'global')


def ayah_dir(ref, kind='raw'):
    s, a = ref.split(':')
    pat = f'{V5}/{kind}/*/s{int(s):03d}/{s}_{a}'
    ds = sorted(d for d in glob.glob(pat) if os.path.exists(d + '/macro.discovery.json' if kind == 'raw' else d))
    # prefer non-basmala, non-29 experimental ids
    ds = [d for d in ds if 'basmala' not in d] or ds
    return ds[0] if ds else None


def load_discovery(ref, base=None):
    d = base or ayah_dir(ref)
    out = {}
    for l in LANES:
        p = f'{d}/{l}.discovery.json'
        if os.path.exists(p):
            out[l] = json.load(open(p))
    return out, d


def load_packet(ref, lane, raw_dir=None):
    raw_dir = raw_dir or ayah_dir(ref)
    p = raw_dir.replace('/raw/', '/input/') + f'/{lane}.discovery.prompt.md'
    if not os.path.exists(p):
        return None
    t = open(p, encoding='utf-8').read()
    i = t.find('<lane_packet_json>'); j = t.find('</lane_packet_json>')
    return json.loads(t[i + len('<lane_packet_json>'):j])


@functools.lru_cache(None)
def dict_index():
    """branch_ref -> dict(kind, note, gloss, image_ar, phrase_ar, not_ar, root_ar)"""
    pk = CACHE + '/dict_index.pkl'
    if os.path.exists(pk):
        return pickle.load(open(pk, 'rb'))
    idx = {}
    roots = {}
    for p in sorted(glob.glob(DICT + '/root_*_entry.json')):
        d = json.load(open(p))
        rid = d['root_envelope_id']
        for b in d.get('branches', []):
            ls = b.get('lexicalization_scope') or {}
            idx[b['branch_ref']] = dict(
                kind=ls.get('branch_kind'), note=ls.get('note'),
                gloss=(b.get('concept_gloss') or {}).get('text'),
                image_ar=b.get('branch_image_ar'), phrase_ar=b.get('source_phrase_ar'),
                not_ar=b.get('what_is_not_ar'), what_ar=b.get('what_is_ar'),
                boundary=(b.get('identity_judgment') or {}).get('boundary_note'))
        oe = d.get('occurrence_evidence') or {}
        roots[rid] = dict(n_words=(oe.get('summary') or {}).get('word_count'),
                          ayahs=[a['ayah_ref'] for a in oe.get('ayahs', [])])
    pickle.dump((idx, roots), open(pk, 'wb'))
    return idx, roots


@functools.lru_cache(None)
def root_ar_map():
    """root_id -> Arabic root string, from quranic_branches_ar.tsv"""
    m = {}
    with open(SLM + '/quranic_branches_ar.tsv', encoding='utf-8') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            m[row['source_root_id']] = row['surface_root']
    return m


@functools.lru_cache(None)
def quran_text():
    t = {}
    with open(SLM + '/quran_ayah_text_ar.tsv', encoding='utf-8') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            t[row['ayah_ref']] = row['text_uthmani']
    return t


@functools.lru_cache(None)
def concordance():
    """root_norm -> list of (ayah_ref, surfaces)"""
    c = collections.defaultdict(list)
    with open(SLM + '/qac_root_ayah.tsv', encoding='utf-8') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            c[row['root_norm']].append((row['ayah_ref'], row['surfaces_ar'], row['lemmas_ar'], int(row['occurrence_count'])))
    return c


def est_tokens(s):
    """Rough Claude token estimate. Arabic script ~1 token per 2.2 chars; Latin/Turkish ~1 per 3.6 chars.
    Calibration is an assumption (no local Claude tokenizer); bytes/4 reported alongside."""
    ar = sum(1 for ch in s if '؀' <= ch <= 'ۿ' or 'ݐ' <= ch <= 'ࣿ')
    other = len(s) - ar
    return int(ar / 2.2 + other / 3.6)


def refkey(r):
    try:
        return tuple(int(x) for x in r.split(':')[:2])
    except Exception:
        return (999, 999)


def cal_tokens(s):
    """Calibrated on billed Opus 5.5 runs (v9 arms, n=52): tokens ~= 0.451 * UTF-8 bytes (+ fixed overhead)."""
    return int(0.451 * len(s.encode()))
