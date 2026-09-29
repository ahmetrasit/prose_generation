#!/usr/bin/env python3
"""Supply v0 (E0): a deterministic, descriptive per-ayah supply built by script only.

For an ayah S:A this writes, under out/:
  <S_A>.md         what a model reads (sections A-I, see README.md)
  <S_A>.pull.json  every full list behind the page (model-readable, so it is kept as clean as the page)
  <S_A>.audit.json for the user only: the internal numbers the script used (significance, lens scores and
                   thresholds, defining-vocabulary counts, Majaz mapping basis). Never given to a model.
and entries/<envelope>.md (the six early dictionary entries of each root, full text) and out/sizes.json.

Binding rules applied here (user decisions, 2026-09-28): sense evidence only from the project dictionary and its six
early sources; Majaz al-Quran quoted directly from the Majaz text; no verdicts, grades, confidence, script
construction-presence verdicts, popularity sorting or scene tags in anything a model reads; branch lines in
dictionary order, keyed by branch_ref; no numeric caps and no trimming (sizes are reported, never judged).
No case-specific rule lives in this file; the named probes are evaluation inputs only (check_supply.py).

Usage: python3 build_supply.py 1:6 4:34 ...      (no argument: the probe and blind set in DEFAULT_REFS)
       python3 build_supply.py --rebuild-cache ...
Config: supply_config.json next to this file overrides DEFAULT_CONFIG (written on first run).
"""
import collections
import csv
import functools
import glob
import json
import math
import os
import pickle
import random
import re
import sqlite3
import sys

sys.dont_write_bytecode = True
csv.field_size_limit(10 ** 9)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from textclean import clean_early  # noqa: E402  (shared with the E0 checks)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('SUPPLY_OUT') or os.path.join(HERE, 'out')
ENTRIES = os.path.join(HERE, 'entries')
CACHE = os.path.join(HERE, 'cache')
P = '/Volumes/OZTURK/_projects'
V15 = P + '/prose_generation/_commentary/v15'
V15D = V15 + '/data'
QD = P + '/quran-data/data'
TR = QD + '/dictionary/tr'
PACKETS = P + '/dictionary/data/output/root_packets'
GLOSSRES = P + '/dictionary/v2/gloss_generation/results/tr'
DOSSIER = P + '/root-dossier/out/activation_map.tsv'
QIRAAT = P + '/study/_project_corpus/qiraat.tsv'
COLLOC = QD + '/grammar/contextual/collocation_profiles_v2.tsv'
GRAMMAR_ATT = QD + '/grammar/attachments/attachments.tsv'
CHANNELS = QD + '/analysis/channels/network-v3/s{S:03d}/review/reader_a_pilot.md'
HFT = P + '/latent_activation/focus_trace/runs'
V12 = QD + '/analysis/ayah-activation/v12-cross-run/tr'
MAJAZ_DB = P + '/quran-roots/_corpus/lexicons/cache/openiti_context.sqlite'
MAJAZ_RAW = P + '/quran-roots/_corpus/lexicons/sources/majaz_quran/raw/0209AbuCubayda.MajazQuran.JK010146-ara1'
TEXTMAP = P + '/quran-slm/artifacts/ayah_semantic_map/v1'
SLM_NET = P + '/quran-slm/artifacts/corpus_network'
ROOT_ALTS = QD + '/bridges/qac-dictionary-word-root-analyses.json'
LOANWORDS = V15D + '/loanwords/out'

DEFAULT_REFS = ['1:6', '4:34', '5:6', '18:86', '18:96', '29:38', '29:45', '19:70', '19:73', '19:75', '88:7', '88:17']

DEFAULT_CONFIG = {
    "_comment": "Switches and definitions for supply v0. Numbers here DEFINE a link type or a lens (what counts as "
                "a pointer, a bridge, a parallel); none of them caps or trims a list. Sizes are reported, never judged.",
    "window_radius": 7,
    "whole_surah_text_except": [2],
    "links": {
        "definitional_pointers": True,
        "definitional_pointers_inward": True,
        "rare_lemma_bridges": True,
        "dictionary_neighbours": True,
        "root_cooccurrence": True,
        "quran_slm_pairs": False
    },
    "cooccurrence": {
        "_comment": "The validator's root_cooccurrence rule (validate/recommended_links.json, push): two roots of the "
                    "ayah held together by at least min_other_ayat other ayat with ln PMI above min_ln_pmi, this ayah "
                    "removed from all counts. Every positively associated pair is kept in the pull file.",
        "min_other_ayat": 2,
        "min_ln_pmi": 2.0
    },
    "pointer": {
        "_comment": "A lexeme named in a branch's own text (image, definition, early phrases) points to another root. "
                    "Kept when that root is in this ayah or the window and the lexeme is not general defining "
                    "vocabulary (defining_df = number of dictionary branches whose text contains it), or elsewhere in "
                    "the surah and the lexeme is specific, or anywhere in the Quran when the root itself is rare.",
        "window_max_defining_df": 100,
        "window_root_max_ayat": 400,
        "surah_max_defining_df": 40,
        "surah_root_max_ayat": 100,
        "rare_root_max_ayat": 12
    },
    "bridge": {
        "_comment": "A lemma named in a branch text, found in few ayat, that the Quran puts beside a neighbour's root "
                    "in at least min_share of its ayat and in at least min_witness_ayat ayat (random branch-root "
                    "pairs pass this about 1.4% of the time; see README).",
        "lemma_max_ayat": 30,
        "neighbour_root_max_ayat": 400,
        "min_witness_ayat": 2,
        "min_share": 0.5
    },
    "neighbours": {
        "_comment": "Dictionary neighbour_distinctions whose other branch's root is in this ayah or window; "
                    "contrast relations also at surah level.",
        "surah_level_relations": ["antonym", "polarity_pair"]
    },
    "slm_pairs": {"max_mutual_rank": 10},
    "usage": {
        "every_use_max_uses": 40,
        "kwic_words": 4,
        "partner_min_attach": 1,
        "formula_max_ayat": 8
    },
    "parallels": {
        "_comment": "A lens includes an ayah when its lens score beats the quantile of the same lens over random ayah "
                    "pairs (membership by evidence, not by count).",
        "lenses": ["root", "lemma", "phrase", "echo", "loaded", "textmap"],
        "random_quantile": 0.999,
        "random_focus_sample": 400,
        "seed": 15,
        "show_text_other_surah": True,
        "echo_root_max_ayat": 200,
        "phrase_ngram_max_ayat": 60,
        "phrase_content_lemma_max_ayat": 300,
        "loaded_root_ayat": [2, 60]
    },
    "chains": {
        "channel_reviews": True,
        "hft_relay": True,
        "v12_relay": True,
        "relay_text": False
    },
    "majaz": {"raw_fallback": True, "marker_window": 5}
}


def load_config():
    p = os.path.join(HERE, 'supply_config.json')
    if not os.path.exists(p):
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_CONFIG, f, ensure_ascii=False, indent=1)
        return json.loads(json.dumps(DEFAULT_CONFIG))
    cfg = json.loads(json.dumps(DEFAULT_CONFIG))
    user = json.load(open(p, encoding='utf-8'))
    for k, v in user.items():
        if isinstance(v, dict) and isinstance(cfg.get(k), dict):
            cfg[k].update(v)
        else:
            cfg[k] = v
    return cfg


CFG = load_config()


# ============================================================================ text helpers

DIAC = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')
AR_CH = re.compile(r'[؀-ۿݐ-ݿࢠ-ࣿ]')
TOKRE = re.compile('[ء-ي]+')


def norm(t):
    """Diacritics off, alef forms unified, ى→ي, ة→ه (keeps hamza carriers as ؤ/ئ → و/ي)."""
    t = DIAC.sub('', t or '')
    t = re.sub('[أإآٱ]', 'ا', t)
    return t.replace('ى', 'ي').replace('ة', 'ه').replace('ؤ', 'و').replace('ئ', 'ي')


def rasm(t):
    """Folding for matching imla'i spelling against Uthmani rasm: waw/ya + dagger alif read as alif, then every
    alif and hamza dropped, ى→ي, ة→ه, diacritics off."""
    t = (t or '').replace('وٰ', 'ٰ').replace('ىٰ', 'ٰ')
    t = DIAC.sub('', t)
    t = re.sub('[اأإآٱءؤئ]', '', t)
    return t.replace('ى', 'ي').replace('ة', 'ه')


def lexnorm(t):
    """Normalisation for whole-word matching of dictionary (imla'i) tokens against Quranic (Uthmani) words:
    waw/ya + dagger alif and the dagger alif itself read as alif, other diacritics off, alef and hamza-seat
    forms unified (ءا/آ/أ/إ/ٱ → ا, ؤ → و, ئ → ي), ى → ي, ة → ه. Unlike rasm() it keeps every written alif."""
    t = (t or '').replace('\u0648\u0670', 'ا').replace('\u0649\u0670', 'ا').replace('\u0670', 'ا')
    t = DIAC.sub('', t)
    t = t.replace('ءا', 'ا')
    t = re.sub('[أإآٱ]', 'ا', t)
    return t.replace('ى', 'ي').replace('ة', 'ه').replace('ؤ', 'و').replace('ئ', 'ي')


def nroot(r):
    r = (r or '').strip()
    r = re.sub('[أإآؤئ]', 'ء', r).replace('ى', 'ي')
    if ' ' not in r and len(r) >= 3:
        r = ' '.join(r)
    return r


def refkey(r):
    return tuple(int(x) for x in r.split(':'))


def est_tokens(text):
    ar = len(AR_CH.findall(text))
    return 1.151 * ar + 0.366 * (len(text) - ar)


def cached(name, fn):
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, name + '.pkl')
    if os.path.exists(p) and '--rebuild-cache' not in sys.argv:
        with open(p, 'rb') as f:
            return pickle.load(f)
    v = fn()
    with open(p, 'wb') as f:
        pickle.dump(v, f)
    return v


def read_tsv(path):
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


# ============================================================================ Quran text and words (v15 base tables)

@functools.lru_cache(None)
def quran():
    return {r['ref']: r['text'] for r in read_tsv(V15D + '/quran.tsv')}


@functools.lru_cache(None)
def surah_len(s):
    n = 0
    while f'{s}:{n + 1}' in quran():
        n += 1
    return n


def _words():
    by = collections.defaultdict(list)
    for r in read_tsv(V15D + '/words.tsv'):
        by[f"{r['surah']}:{r['ayah']}"].append(dict(
            w=int(r['w']), ref3=r['ref'], surface=r['surface'],
            roots=[nroot(x) for x in r['roots'].split('|') if x],
            lemmas=[x for x in r['lemmas'].split('|')], pos=r['pos']))
    return dict(by)


W = cached('words', _words)
REFS = sorted(quran(), key=refkey)
NAY = len(REFS)
ROOT_AYAT = collections.defaultdict(set)
ROOT_WORDS = collections.defaultdict(list)
LEMMA_AYAT = collections.defaultdict(set)
AYAH_ROOTS = {}
for _ref in REFS:
    rs = set()
    for _w in W.get(_ref, []):
        for i, _r in enumerate(_w['roots']):
            rs.add(_r)
            ROOT_WORDS[_r].append(_w['ref3'])
            lem = _w['lemmas'][i] if i < len(_w['lemmas']) else ''
            if lem:
                LEMMA_AYAT[(_r, lem)].add(_ref)
        for _r in _w['roots']:
            ROOT_AYAT[_r].add(_ref)
    AYAH_ROOTS[_ref] = rs


def word_by_ref3(ref3):
    s, a, w = ref3.split(':')[:3]
    for x in W.get(f'{s}:{a}', []):
        if x['w'] == int(w):
            return x
    return None


def kwic(ref3, n=None):
    n = CFG['usage']['kwic_words'] if n is None else n
    s, a, w = ref3.split(':')[:3]
    ws = W.get(f'{s}:{a}', [])
    i = int(w) - 1
    toks = [x['surface'] for x in ws]
    if i >= len(toks):
        return ''
    left, right = toks[max(0, i - n):i], toks[i + 1:i + 1 + n]
    return (('… ' if i - n > 0 else '') + ' '.join(left) + f" ⟦{toks[i]}⟧ " + ' '.join(right)
            + (' …' if i + 1 + n < len(toks) else '')).replace('  ', ' ').strip()


# ============================================================================ the dictionary (Turkish entries)

SRC_TAG = re.compile(r'\(([a-z_;]+)\)\s*$')


def split_phrases(phrase):
    """Early-source phrase field -> [(segment, tags)]: segments separated by ؛, a '(tags)' closes a source group."""
    out, pending = [], []
    for seg in re.split('؛', phrase or ''):
        seg = seg.strip()
        if not seg:
            continue
        m = SRC_TAG.search(seg)
        if m:
            txt = seg[:m.start()].strip()
            if txt:
                pending.append(txt)
            for p in pending:
                out.append((p, m.group(1)))
            pending = []
        else:
            pending.append(seg)
    for p in pending:
        out.append((p, ''))
    return out


def _dictionary():
    env, branch, word_env = {}, {}, collections.defaultdict(set)
    occ = {}
    for f in sorted(glob.glob(TR + '/root_*_entry.json')):
        d = json.load(open(f, encoding='utf-8'))
        eid = d['root_envelope_id']
        brs = []
        for b in d.get('branches', []):
            bref = b.get('branch_ref', '')
            if '/' not in bref:
                continue
            ls = b.get('lexicalization_scope') or {}
            cg = b.get('concept_gloss') or {}

            def flat(v):
                return '؛ '.join(str(x) for x in v) if isinstance(v, list) else (v or '')
            branch[bref] = dict(
                ref=bref, env=eid, kind=ls.get('branch_kind') or 'missing', note=ls.get('note') or '',
                image=flat(b.get('branch_image_ar')), what=flat(b.get('what_is_ar')), whatnot=flat(b.get('what_is_not_ar')),
                phrase=flat(b.get('source_phrase_ar')), sources=b.get('sources') or [],
                gloss=cg.get('text') or '', gloss_profile=cg.get('error_profile') or {},
                ctx=[dict(text=g.get('text'), role=g.get('usage_role'), profile=g.get('error_profile') or {})
                     for g in b.get('contextual_glosses') or []],
                definition_tr=(b.get('concept_map') or {}).get('definition', ''),
                facets={f.get('facet_id'): f.get('statement', '') for f in (b.get('concept_map') or {}).get('facets', [])},
                boundary=(b.get('identity_judgment') or {}).get('boundary_note', ''),
                neighbours=[(x.get('neighbor_ref'), x.get('relation_type')) for x in b.get('neighbor_distinctions') or []
                            if x.get('neighbor_ref')])
            brs.append(bref)
        oe = d.get('occurrence_evidence') or {}
        for o in oe.get('occurrences', []):
            al = o.get('alignment') or {}
            word_env[o['qac_word_ref']].add(eid)
            occ[(eid, o['qac_word_ref'])] = dict(
                lemma=o.get('lemma_ar') or '', pos=o.get('pos') or '', measure=o.get('measure') or '',
                voice=o.get('voice') or '', status=al.get('status') or '',
                atts=[(a.get('relation') or '', a.get('focus_role') or '', a.get('prep_base') or '',
                       nroot(a.get('other_root') or ''), a.get('other_surface') or '') for a in al.get('attachments') or []])
        env[eid] = dict(file=f, branches=brs, n_occ=len(oe.get('occurrences', [])))
    return env, branch, dict(word_env), occ


ENV, BR, WORD_ENV, OCC = cached('dictionary', _dictionary)


def _env_letters():
    """Envelope -> root letters by majority over the words its occurrences name (packet root_norm otherwise)."""
    votes = collections.defaultdict(collections.Counter)
    for ref3, envs in WORD_ENV.items():
        w = word_by_ref3(ref3)
        if not w:
            continue
        for e in envs:
            for r in w['roots']:
                votes[e][r] += 1
    out = {}
    for e in ENV:
        if votes[e]:
            out[e] = votes[e].most_common(1)[0][0]
        else:
            p = os.path.join(PACKETS, e + '.json')
            if os.path.exists(p):
                out[e] = nroot(json.load(open(p, encoding='utf-8')).get('root_norm', ''))
    return out


ENV_LETTERS = cached('env_letters', _env_letters)
LETTERS_ENV = collections.defaultdict(list)
for _e, _l in sorted(ENV_LETTERS.items()):
    LETTERS_ENV[_l].append(_e)


def _furuq():
    """Fallback for roots with no Turkish entry: Furuq table rows from v15 branches.tsv, keyed by branch_ref."""
    out = collections.defaultdict(list)
    for r in read_tsv(V15D + '/branches.tsv'):
        out[nroot(r['root'])].append(dict(ref=f"{r['root_id']}/{r['branch']}", env='furuq:' + r['root_id'],
                                          kind='', note='', image=r['image'], what=r['what_is'], whatnot='',
                                          phrase=r['source_phrase'], sources=[], gloss=r['tr_gloss'],
                                          gloss_profile={}, ctx=[], definition_tr='', facets={}, boundary='', neighbours=[]))
    return dict(out)


FURUQ = cached('furuq', _furuq)


def envs_for_word(w, root):
    """Dictionary envelopes a word's root belongs to: the entry whose occurrence list names this word first,
    then the entries spelled with these root letters, then the Furuq table."""
    envs = [e for e in sorted(WORD_ENV.get(w['ref3'], ())) if ENV_LETTERS.get(e) == root]
    if not envs:
        envs = list(LETTERS_ENV.get(root, []))
    if not envs and root in FURUQ:
        envs = [FURUQ[root][0]['env']]
    return envs


def env_branches(eid):
    if eid.startswith('furuq:'):
        rid = eid.split(':', 1)[1]
        for rows in FURUQ.values():
            if rows and rows[0]['env'] == eid:
                return rows
        return []
    return [BR[b] for b in ENV[eid]['branches']]


def env_label(eid):
    return eid.split(':', 1)[1] + ' (Furūq table only; no Turkish entry)' if eid.startswith('furuq:') else eid


def branch_of(bref):
    if bref in BR:
        return BR[bref]
    rid = bref.split('/')[0]
    for rows in FURUQ.values():
        for r in rows:
            if r['ref'] == bref:
                return r
    return None


@functools.lru_cache(None)
def rid_env():
    out = {}
    for b in BR.values():
        out.setdefault(b['ref'].split('/')[0], b['env'])
    return out


def letters_of_bref(bref):
    e = rid_env().get(bref.split('/')[0])
    return ENV_LETTERS.get(e, '') if e else ''


def strip_whatis(t):
    return re.sub(r'^\s*يدخل فيه\s*', '', t or '')


def early_phrases(b, n=2):
    """The first phrase of each of the first n source groups, with its source tag (never gated)."""
    groups, seen = [], set()
    for seg, tags in split_phrases(b['phrase']):
        if tags in seen:
            continue
        seen.add(tags)
        groups.append((seg, tags))
        if len(groups) >= n:
            break
    return groups


def construction_tag(b):
    first = split_phrases(b['phrase'])
    seg = first[0][0] if first else ''
    if b['kind'] == 'collocation':
        return f"C[{seg}]"
    if b['kind'] == 'non_bare':
        return f"F[{seg}]"
    return ''


# ============================================================================ other sources

def _dossier():
    plain, minor = collections.defaultdict(list), collections.defaultdict(list)
    for r in read_tsv(DOSSIER):
        if not r['branch_ref'].startswith('root_'):
            continue
        if r['role'] == 'dominant':
            plain[r['qac_word_ref']].append(r['branch_ref'])
        elif r['role'] == 'minor':
            minor[r['qac_word_ref']].append((r['branch_ref'], r['note']))
    return dict(plain), dict(minor)


PLAIN, MINOR = cached('dossier', _dossier)


@functools.lru_cache(None)
def qiraat():
    out = collections.defaultdict(list)
    for r in read_tsv(QIRAAT):
        s, a = r['tsv_word_ref'].split(':')[:2]
        out[f'{s}:{a}'].append(r)
    return out


@functools.lru_cache(None)
def documented_alternatives():
    d = json.load(open(ROOT_ALTS, encoding='utf-8'))
    out = collections.defaultdict(list)
    for rec in d.get('records', []):
        sel = rec['selector']
        key = (sel.get('qacRootJoinKey'), sel.get('qacLemma') or sel.get('qacRef'))
        for an in rec.get('analyses', []):
            if an.get('standing') != 'primary' and an.get('rootArabic'):
                out[key].append((nroot(an['rootArabic']), an.get('reasonTr') or '', an.get('attributionTr') or ''))
    return out


def qiraat_word(v):
    """The QAC word a qira'at record belongs to. The corpus has its own word numbering, so the record is matched by
    spelling: a word of the ayah with the same rasm, else the most similar word (similarity >= 0.6, unique best),
    else the word with the corpus index."""
    import difflib
    s, a, wi = v['tsv_word_ref'].split(':')[:3]
    ws = W.get(f'{s}:{a}', [])
    var = rasm(v['qiraat_arabic'].split('/')[0].split()[-1] if v['qiraat_arabic'].split('/')[0].split() else '')
    same = [x for x in ws if rasm(x['surface']) == var]
    if len(same) == 1:
        return same[0]['ref3']
    if len(same) > 1:
        return min(same, key=lambda x: abs(x['w'] - int(wi)))['ref3']
    sc = sorted(((difflib.SequenceMatcher(None, var, rasm(x['surface'])).ratio(), -abs(x['w'] - int(wi)), x['ref3'])
                 for x in ws), reverse=True)
    if sc and sc[0][0] >= 0.6 and (len(sc) == 1 or sc[0][:2] != sc[1][:2]):
        return sc[0][2]
    return f'{s}:{a}:{int(wi)}'


SUBSTITUTIONS = {'ص': 'سز', 'س': 'صز', 'ز': 'صس', 'ط': 'ت', 'ت': 'ط', 'ض': 'ظ', 'ظ': 'ض'}


@functools.lru_cache(None)
def surface_index():
    """rasm of a Quranic surface (and with one proclitic / the article stripped) -> {root: [ref3...]}."""
    idx = collections.defaultdict(lambda: collections.defaultdict(list))
    for ref in REFS:
        for w in W[ref]:
            if len(w['roots']) != 1:
                continue
            n = norm(w['surface'])
            cands = {rasm(w['surface'])}
            if n[:1] in 'وف' and len(n) > 3:          # a conjunction, only when a word remains
                n = n[1:]
                cands.add(rasm(n))
            if n.startswith('ال') and len(n) > 4:      # the article, only where it is written as such
                cands.add(rasm(n[2:]))
            for c in cands:
                if len(c) >= 3:
                    idx[c][w['roots'][0]].append(w['ref3'])
    return {k: dict(v) for k, v in idx.items()}


def alternative_roots(w, root, lemma):
    """Roots the word may also be heard from, each with its documented basis: documented alternative analyses,
    canonical-reading letter exchanges (v15 rule), a variant reading spelled like a Quranic word of another root,
    and root-dossier 'minor' placements under another root."""
    out = []
    s, a, wi = w['ref3'].split(':')
    join = root.replace(' ', '')
    for key in ((join, lemma), (join, f'{s}:{a}:{wi}:1'), (join, w['ref3'])):
        for alt, reason, attr in documented_alternatives().get(key, []):
            if alt != root and alt not in [x for x, _ in out]:
                out.append((alt, f"documented alternative analysis ({attr}): {reason}"))
    canon = rasm(w['surface'])
    for v in qiraat().get(f'{s}:{a}', []):
        if v['qiraat_reader_set'] == 'canonical' or qiraat_word(v) != w['ref3']:
            continue
        var = rasm(v['qiraat_arabic'].split('/')[0])
        letters = root.split()
        for i, L in enumerate(letters):
            for M in SUBSTITUTIONS.get(L, ''):
                if M in var and var.count(L) < canon.count(L):
                    cand = ' '.join(letters[:i] + [M] + letters[i + 1:])
                    if cand != root and (cand in LETTERS_ENV or cand in FURUQ) and cand not in [x for x, _ in out]:
                        out.append((cand, f"reading {v['qiraat_transliteration']} ({v['qiraat_reader_set']}) exchanges {L}/{M}"))
        found = collections.OrderedDict()
        vn = norm(v['qiraat_arabic'].split('/')[0])
        vc = [var]
        if vn[:1] in 'وف' and len(vn) > 3:
            vn = vn[1:]
            vc.append(rasm(vn))
        if vn.startswith('ال') and len(vn) > 4:
            vc.append(rasm(vn[2:]))
        for c in vc:
            for r2, refs in sorted(surface_index().get(c, {}).items()):
                if r2 != root:
                    found.setdefault(r2, [])
                    found[r2] += [x for x in refs if x not in found[r2]]
        for r2, refs in found.items():
            if r2 not in [x for x, _ in out]:
                ex = ', '.join(f"{x.rsplit(':', 1)[0]} {word_by_ref3(x)['surface']}" for x in sorted(refs, key=refkey))
                out.append((r2, f"reading {v['qiraat_arabic']} ({v['qiraat_transliteration']}; {v['qiraat_reader_set']}) "
                                f"is spelled like the Quranic word(s) of this root at {ex}"))
    for bref, note in MINOR.get(w['ref3'], []):
        r2 = letters_of_bref(bref)
        if r2 and r2 != root and r2 not in [x for x, _ in out]:
            out.append((r2, f"root-dossier also places this word under {bref}: {note}"))
    return out


def _colloc():
    d = collections.defaultdict(list)
    for r in read_tsv(COLLOC):
        d[nroot(r['root_arabic'])].append(r)
    return dict(d)


COLLOC_BY_ROOT = cached('colloc', _colloc)


def _grammar_att():
    d = collections.defaultdict(list)
    with open(GRAMMAR_ATT, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            d[f"{r['sura']}:{r['ayah']}"].append((r['relation'], r['dep_surface'], nroot(r['dep_root_norm']),
                                                  r['head_surface'], nroot(r['head_root_norm']), r['prep_base']))
    return dict(d)


GATT = cached('grammar_att', _grammar_att)


# ============================================================================ lexicon for pointers and bridges

STOP_TOK = {lexnorm(x) for x in '''من في على إلى عن أي هو هي الذي التي إذا كل ما لا أو ثم به له بها لها يقال سمي ذلك شيء أصل يدل
واحد معروف اسم أيضا قال وهو وهي كان بعض فهو فلان جمع قيل يقول أنه أن كما حتى مثل غير بين قبل عند هذا هذه ذو ذات لم قد لأن
الواحد يسمى تقول العرب أمر كذا عنه منه فعل يفعل مصدر يكون صار يستعمل يذكر يؤنث كأنه تعني ناس قوم قول لما منسوب إذ إلا
إنما وقد فيه فيها منها عليه إليه وكل يعني أراد معنى كثير قليل حين حيث وقت نحو دون سواء أبو فيما مما عما بما كلما
هم هن وهم وهن فهم فهن أنا نحن أنت أنتم أنتن إياه تلك ذا ذي هؤلاء أولئك الذين اللذان اللتان اللاتي أحد كلها كله بعضهم بعضها
وذلك وكذلك كذلك ذاك إذن لكن لكنه بل ليس ليست لن لو لولا أما إما حيثما متى أين كيف لدى لدن يدخل ويدخل ويقال معناه وقيل
عليها عليهم لهم لكم لنا بهم منهم فيهم إليها إليهم وهو وهي ومنه ومنها وفيه به وبه
كأن كأنه كأنها كأنهم وكأن فكأن لكأن إياها إياهم أنها أنهم إنه إنها إنهم ولا وما ومن وفي وعلى وإلى وعن'''.split()}
PREFIXES = ('وال', 'فال', 'بال', 'كال', 'لل', 'ال', 'و', 'ف', 'ب', 'ل', 'ك')
SUFFIXES = ('هما', 'كما', 'ها', 'هم', 'هن', 'كم', 'كن', 'نا', 'ه', 'ك')


def token_tiers(t):
    """Candidate stems of a token, least stripped first; forms that still carry the article are never stems.
    Tiers 1 and 3 have a pronoun suffix (or ة, folded to ه) removed."""
    pre = [t[len(p):] for p in PREFIXES if t.startswith(p) and len(t) - len(p) >= 3]
    tiers = [[t],
             [t[:-len(x)] for x in SUFFIXES if t.endswith(x) and len(t) - len(x) >= 3],
             pre,
             [c[:-len(x)] for c in pre for x in SUFFIXES if c.endswith(x) and len(c) - len(x) >= 3]]
    return [[c for c in tier if not c.startswith('ال') and not c.startswith('لل')] for tier in tiers]


def _lexicon():
    """rasm of a Quranic lemma or surface (proclitic/article and pronoun suffix stripped variants) -> Counter(root);
    and rasm -> set(lemma) for words with one root and one lemma."""
    lex = collections.defaultdict(collections.Counter)
    flem = collections.defaultdict(set)
    lem_root = {}
    for r in read_tsv(V15D + '/lemmas.tsv'):
        f = lexnorm(r['lemma'])
        f = f[2:] if f.startswith('ال') else f
        k = f
        if len(k) >= 3:
            lex[k][nroot(r['root'])] += int(r['count'] or 1)
            flem[k].add((nroot(r['root']), r['lemma']))
    for ref in REFS:
        for w in W[ref]:
            if len(w['roots']) != 1:
                continue
            t = lexnorm(w['surface'])
            forms = {t}
            g = re.sub('^(وال|فال|بال|كال|لل|ال)', '', t)
            if len(g) >= 3:
                forms.add(g)
            h = re.sub('^(و|ف)', '', t)
            if len(h) >= 4:
                forms.add(h)
            for x in list(forms):
                for sfx in SUFFIXES:
                    if x.endswith(sfx) and len(x) - len(sfx) >= 3:
                        forms.add(x[:-len(sfx)])
            for x in forms:
                k = x
                if len(k) >= 3 and not k.startswith('ال'):
                    lex[k][w['roots'][0]] += 1
                    if w['lemmas'] and w['lemmas'][0]:
                        flem[k].add((w['roots'][0], w['lemmas'][0]))
    return {k: dict(v) for k, v in lex.items()}, {k: sorted(v) for k, v in flem.items()}


LEX, FLEM = cached('lexicon', _lexicon)


def _stop(tok):
    return tok in STOP_TOK or (tok[:1] in 'وف' and tok[1:] in STOP_TOK) or len(tok) < 3


def _hamza_seat_stem(tier_index, stem, root):
    """A stem left ending in alif by removing a suffix (tier 1 or 3) does not join a hamza root: the folding writes a
    final hamza seat as alif (Uthmani حمإ -> حما), so حماة / وحماه (ح م و, in-law) would read as حمإ (ح م ء)."""
    return tier_index in (1, 3) and stem.endswith('ا') and 'ء' in root.split()


def token_root(tok):
    """Whole-word match of a dictionary token to one Quranic root (least-stripped spelling first)."""
    if _stop(tok):
        return None
    for ti, tier in enumerate(token_tiers(tok)):
        cnt = collections.Counter()
        for c in tier:
            if c in STOP_TOK:
                continue
            k = c
            if len(k) >= 3:
                for r, n in LEX.get(k, {}).items():
                    if not _hamza_seat_stem(ti, k, r):
                        cnt[r] += n
        if cnt:
            return cnt.most_common(1)[0][0]
    return None


def token_lemma(tok):
    """The single Quranic lemma (root, lemma) a dictionary token spells, else None."""
    if _stop(tok):
        return None
    for ti, tier in enumerate(token_tiers(tok)):
        lems = set()
        for c in tier:
            if c in STOP_TOK:
                continue
            k = c
            if len(k) >= 3:
                lems |= {tuple(x) for x in FLEM.get(k, []) if not _hamza_seat_stem(ti, k, x[0])}
        if lems:
            return next(iter(lems)) if len(lems) == 1 else None
    return None


def branch_text(b):
    return ' '.join([b['image'], strip_whatis(b['what']), re.sub(r'\([a-z_;]+\)', ' ', b['phrase'])])


def text_tokens(txt):
    return TOKRE.findall(lexnorm(txt))


def _defining_df():
    df = collections.Counter()
    for b in BR.values():
        df.update(set(text_tokens(branch_text(b))))
    return df


DEFDF = cached('defining_df', _defining_df)


def branch_mentions(b, own_root):
    """[(token, root)] named in the branch's own text, whole-word, own root excluded, first spelling kept."""
    out, seen = [], set()
    for t in text_tokens(branch_text(b)):
        r = token_root(t)
        if r and r != own_root and r not in seen:
            seen.add(r)
            out.append((t, r))
    return out


# ============================================================================ significance helper (audit only)

def neglog10_binom_tail(k, n, q):
    if k <= 0 or n <= 0:
        return 0.0
    q = min(max(q, 1e-12), 1 - 1e-12)
    logs = [math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1) + j * math.log(q) + (n - j) * math.log(1 - q)
            for j in range(k, n + 1)]
    m = max(logs)
    lp = m + math.log(sum(math.exp(x - m) for x in logs))
    return max(0.0, -lp / math.log(10))


# ============================================================================ per-ayah roots

def ayah_units(ref):
    """Per word: its own roots with envelopes, then alternative roots. Returns (units, order) where each unit is
    dict(root, envs, words=[(ref3, surface, lemma)], alt_of=[(ref3, surface, reason)])."""
    units, order = {}, []
    for w in W.get(ref, []):
        for i, r in enumerate(w['roots']):
            lem = w['lemmas'][i] if i < len(w['lemmas']) else ''
            u = units.get(r)
            if u is None:
                u = units[r] = dict(root=r, envs=envs_for_word(w, r), words=[], alt_of=[])
                order.append(r)
            u['words'].append((w['ref3'], w['surface'], lem))
    for w in W.get(ref, []):
        for i, r in enumerate(w['roots']):
            lem = w['lemmas'][i] if i < len(w['lemmas']) else ''
            for alt, why in alternative_roots(w, r, lem):
                u = units.get(alt)
                if u is None:
                    envs = list(LETTERS_ENV.get(alt, [])) or ([FURUQ[alt][0]['env']] if alt in FURUQ else [])
                    u = units[alt] = dict(root=alt, envs=envs, words=[], alt_of=[])
                    order.append(alt)
                u['alt_of'].append((w['ref3'], w['surface'], why))
    return units, order


def window_refs(ref, radius=None):
    s, a = refkey(ref)
    r = CFG['window_radius'] if radius is None else radius
    return [f'{s}:{x}' for x in range(max(1, a - r), min(surah_len(s), a + r) + 1)]


def surah_refs(s):
    return [f'{s}:{x}' for x in range(1, surah_len(s) + 1)]


def surfaces_of_root_in(root, refs):
    out = []
    for r in refs:
        for w in W.get(r, []):
            if root in w['roots']:
                out.append((w['ref3'], w['surface']))
    return out


def where_text(pairs):
    by = collections.OrderedDict()
    for ref3, sf in pairs:
        by.setdefault(ref3.rsplit(':', 1)[0], []).append(sf)
    return '; '.join(f"{k} {' '.join(v)}" for k, v in by.items())


# ============================================================================ A. ayah, words, surah text

def section_A(ref, pull):
    s, a = refkey(ref)
    q = quran()
    L = ['## A. The ayah, its words and its surah', '', f'{ref}| {q[ref]}', '',
         '### Words (ref | surface | root | lemma | POS)', '']
    words = []
    for w in W.get(ref, []):
        L.append(f"{w['ref3']} | {w['surface']} | {' / '.join(w['roots']) or '-'} | "
                 f"{' / '.join(x for x in w['lemmas'] if x) or '-'} | {w['pos'] or '-'}")
        words.append(dict(ref=w['ref3'], surface=w['surface'], roots=w['roots'], lemmas=[x for x in w['lemmas'] if x],
                          pos=w['pos']))
    pull['words'] = words
    whole = s not in CFG['whole_surah_text_except']
    shown = surah_refs(s) if whole else window_refs(ref)
    L += ['', f"### Surah {s}, {'the whole surah' if whole else f'ayat {shown[0].split(':')[1]}-{shown[-1].split(':')[1]} (window)'}"
          f" ({surah_len(s)} ayat; ◀ marks this ayah)", '']
    for r in shown:
        L.append(f"{r}| {q[r]}" + ('  ◀' if r == ref else ''))
    pull['text_shown'] = shown
    if not whole:
        units, order = ayah_units(ref)
        L += ['', '### Other ayat of this surah with this ayah\'s roots (outside the window)', '']
        for root in order:
            hits = surfaces_of_root_in(root, [r for r in surah_refs(s) if r not in shown])
            if hits:
                L.append(f"- {root}: {where_text(hits)}")
    return '\n'.join(L)


# ============================================================================ B. every branch of every root

def plain_marks(ref3s):
    marks = collections.defaultdict(list)
    for r3 in ref3s:
        for b in PLAIN.get(r3, []):
            marks[b].append(r3)
    return marks


def branch_line(b, marks=None):
    parts = [f"- {b['ref']}"]
    if marks and b['ref'] in marks:
        parts[0] += f" [plain: {', '.join(marks[b['ref']])}]"
    parts.append(b['image'])
    if b['what']:
        parts.append(strip_whatis(b['what']))
    ph = early_phrases(b)
    if ph:
        parts.append('early: ' + '; '.join(f"«{t}» ({tags})" if tags else f"«{t}»" for t, tags in ph))
    if b['gloss']:
        parts.append(f"tr: {b['gloss']}")
    if b['kind']:
        k = f"kind: {b['kind']}" + (f" — {b['note']}" if b['note'] else '')
        ct = construction_tag(b)
        parts.append(k + (f" {ct}" if ct else ''))
    return ' | '.join(parts)


def branch_record(b):
    return dict(branch_ref=b['ref'], image=b['image'], what_is=strip_whatis(b['what']), what_is_not=b['whatnot'],
                early_phrases=[dict(text=t, sources=tags) for t, tags in split_phrases(b['phrase'])],
                sources=b['sources'], tr_gloss=b['gloss'], tr_definition=b['definition_tr'],
                branch_kind=b['kind'], scope_note=b['note'], construction=construction_tag(b),
                boundary_note=b['boundary'])


def write_entries_file(eid):
    """The six early entries of an envelope (full text), for reading on demand."""
    if eid.startswith('furuq:'):
        return None
    os.makedirs(ENTRIES, exist_ok=True)
    dst = os.path.join(ENTRIES, eid + '.md')
    if not os.path.exists(dst):
        p = os.path.join(PACKETS, eid + '.json')
        if not os.path.exists(p):
            return None
        d = json.load(open(p, encoding='utf-8'))
        parts = [f"# {ENV_LETTERS.get(eid, '')} ({eid}): the early dictionary entries, full text\n"]
        for src in d.get('dictionary_sources', []):
            t = (src.get('entry_text_clean') or '').strip()
            if t and t != '-':
                parts.append(f"## {src.get('source_id')}\n{clean_early(t, src.get('source_id'))}\n")
        with open(dst, 'w', encoding='utf-8') as f:
            f.write('\n'.join(parts))
    return dst


def section_B(ref, pull):
    units, order = ayah_units(ref)
    L = ['## B. Dictionary: every branch of every root of the ayah',
         '',
         'Branch lines follow dictionary order. early = the first phrase of the first two early sources, with the '
         'source tag; tr = the Turkish concept gloss; kind = the dictionary\'s lexicalization scope with its Turkish '
         'scope note; C[…] / F[…] = the first early phrase of a collocation-bound / derived-form branch; '
         '[plain: word] = the branch root-dossier assigns to that word.', '']
    out = []
    for root in order:
        u = units[root]
        ref3s = [x[0] for x in u['words']]
        marks = plain_marks(ref3s)
        for eid in u['envs'] or [None]:
            head = f"### {root}"
            if eid:
                head += f" — {env_label(eid)}"
            if u['words']:
                head += ' — here: ' + '; '.join(f"{r3} {sf}" for r3, sf, _ in u['words'])
            if u['alt_of']:
                head += ' — alternative root for ' + '; '.join(f"{r3} {sf} ({why})" for r3, sf, why in u['alt_of'])
            head += f" — {len(ROOT_WORDS.get(root, []))} uses in the Quran"
            L.append(head)
            if not eid:
                L.append('- (no dictionary entry for this root)')
                out.append(dict(root=root, envelope=None, words=u['words'], alternative_for=u['alt_of'], branches=[]))
                continue
            brs = env_branches(eid)
            for b in brs:
                L.append(branch_line(b, marks))
            L.append('')
            ef = write_entries_file(eid)
            out.append(dict(root=root, envelope=eid, words=[dict(ref=r3, surface=sf, lemma=lm) for r3, sf, lm in u['words']],
                            alternative_for=[dict(ref=r3, surface=sf, basis=why) for r3, sf, why in u['alt_of']],
                            plain={k: v for k, v in marks.items()}, early_entries_file=ef,
                            branches=[branch_record(b) for b in brs]))
    pull['roots'] = out
    return '\n'.join(L).rstrip()


# ============================================================================ C. typed links

def locations(root, ref, exclude_ref3s=()):
    """Where a root stands relative to the ayah: this ayah (other words), the window, the rest of the surah."""
    s, a = refkey(ref)
    win = window_refs(ref)
    here = [(r3, sf) for r3, sf in surfaces_of_root_in(root, [ref]) if r3 not in exclude_ref3s]
    wn = surfaces_of_root_in(root, [r for r in win if r != ref])
    sr = surfaces_of_root_in(root, [r for r in surah_refs(s) if r not in win])
    return here, wn, sr


def loc_text(here, wn, sr, qrefs=None):
    parts = []
    if here:
        parts.append('in this ayah: ' + where_text(here))
    if wn:
        parts.append('in the window: ' + where_text(wn))
    if sr:
        parts.append('elsewhere in this surah: ' + ', '.join(dict.fromkeys(x[0].rsplit(':', 1)[0] for x in sr)))
    if qrefs:
        parts.append(f"in the Quran ({len(qrefs)} ayat): " + ', '.join(qrefs))
    return '; '.join(parts)


def ayah_branches(ref):
    units, order = ayah_units(ref)
    for root in order:
        for eid in units[root]['envs']:
            for b in env_branches(eid):
                yield root, units[root], b


def window_units(ref):
    """Roots of the window's other ayat (not roots of this ayah): root -> (envs, [(ref3, surface)])."""
    units, _ = ayah_units(ref)
    out = collections.OrderedDict()
    for r in window_refs(ref):
        if r == ref:
            continue
        for w in W.get(r, []):
            for root in w['roots']:
                if root in units:
                    continue
                e = out.setdefault(root, [set(), []])
                e[0].update(envs_for_word(w, root))
                e[1].append((w['ref3'], w['surface']))
    return out


def links_pointers(ref, pull, audit):
    pc = CFG['pointer']
    units, order = ayah_units(ref)
    own_ref3 = {x[0] for u in units.values() for x in u['words']}
    L, cands, aud = [], [], []
    for root, u, b in ayah_branches(ref):
        for tok, r2 in branch_mentions(b, root):
            here, wn, sr = locations(r2, ref, exclude_ref3s={x[0] for x in u['words']})
            qn = len(ROOT_AYAT.get(r2, ()))
            df = DEFDF.get(tok, 0)
            qrefs = sorted(ROOT_AYAT.get(r2, ()), key=refkey) if qn <= pc['rare_root_max_ayat'] else None
            cands.append(dict(branch_ref=b['ref'], token=tok, root=r2,
                              in_ayah=[x[0] for x in here], in_window=[x[0] for x in wn], in_surah=[x[0] for x in sr],
                              quran_ayat=qrefs or []))
            keep = ((here or wn) and df <= pc['window_max_defining_df'] and qn <= pc['window_root_max_ayat']) \
                or (sr and df <= pc['surah_max_defining_df'] and qn <= pc['surah_root_max_ayat']) \
                or (qrefs is not None and df <= pc['surah_max_defining_df'])
            aud.append(dict(branch_ref=b['ref'], token=tok, root=r2, defining_df=df, root_ayat=qn, shown=bool(keep)))
            if keep:
                L.append(f"- {b['ref']} «{b['image']}» names «{tok}» → {r2}: {loc_text(here, wn, sr, qrefs)}")
    if CFG['links']['definitional_pointers_inward']:
        ayah_roots = set(order)
        for wr, (envs, occ) in window_units(ref).items():
            for eid in sorted(envs):
                for b in env_branches(eid):
                    for tok, r2 in branch_mentions(b, wr):
                        if r2 not in ayah_roots:
                            continue
                        df = DEFDF.get(tok, 0)
                        here = [x for x in surfaces_of_root_in(r2, [ref])]
                        cands.append(dict(branch_ref=b['ref'], token=tok, root=r2, direction='inward',
                                          branch_root_in_window=[x[0] for x in occ], in_ayah=[x[0] for x in here]))
                        keep = df <= pc['window_max_defining_df'] and len(ROOT_AYAT.get(r2, ())) <= pc['window_root_max_ayat']
                        aud.append(dict(branch_ref=b['ref'], token=tok, root=r2, defining_df=df, direction='inward',
                                        shown=bool(keep)))
                        if keep:
                            L.append(f"- {b['ref']} «{b['image']}» ({wr}, in the window: {where_text(occ)}) names "
                                     f"«{tok}» → {r2}, in this ayah: {where_text(here)}")
    pull['definitional_pointer_candidates'] = cands
    audit['definitional_pointers'] = aud
    return L


def bridge_passes(k, n, bc=None):
    bc = bc or CFG['bridge']
    return k >= bc['min_witness_ayat'] and k / n >= bc['min_share']


def links_bridges(ref, pull, audit):
    bc = CFG['bridge']
    units, order = ayah_units(ref)
    neigh = collections.OrderedDict()
    for r in window_refs(ref):
        for w in W.get(r, []):
            for root in w['roots']:
                neigh.setdefault(root, []).append((w['ref3'], w['surface']))
    L, cands, aud = [], [], []
    for root, u, b in ayah_branches(ref):
        seen = set()
        for tok in text_tokens(branch_text(b)):
            tl = token_lemma(tok)
            if not tl or tl in seen:
                continue
            seen.add(tl)
            lr, lem = tl
            if lr == root:
                continue
            ayl = LEMMA_AYAT.get((lr, lem), set())
            if not ayl or len(ayl) > bc['lemma_max_ayat']:
                continue
            hits = []
            for nr, occ in neigh.items():
                if nr in (root, lr) or len(ROOT_AYAT.get(nr, ())) > bc['neighbour_root_max_ayat']:
                    continue
                inter = ayl & ROOT_AYAT.get(nr, set())
                wit = sorted(inter - {ref}, key=refkey)
                if not wit:
                    continue
                sig = neglog10_binom_tail(len(inter), len(ayl), len(ROOT_AYAT[nr]) / NAY)
                cands.append(dict(branch_ref=b['ref'], token=tok, lemma=lem, lemma_root=lr, lemma_ayat=len(ayl),
                                  neighbour_root=nr, neighbour_words=[x[0] for x in occ], witness_ayat=wit))
                # the focus ayah is not a witness of itself: k and n count only the other ayat
                n_x = len(ayl - {ref})
                ok = bool(n_x) and bridge_passes(len(wit), n_x, bc)
                aud.append(dict(branch_ref=b['ref'], lemma=lem, neighbour_root=nr, k=len(wit), n=n_x,
                                neglog10_p=round(sig, 3), shown=ok))
                if ok:
                    hits.append(f"{nr} ({where_text(occ)}) in {', '.join(wit)}")
            if hits:
                L.append(f"- {b['ref']} «{b['image']}» names «{tok}» (lemma {lem}, {lr}, in {len(ayl)} ayat); the Quran "
                         f"puts it beside " + '; beside '.join(hits))
    pull['rare_lemma_bridge_candidates'] = cands
    audit['rare_lemma_bridges'] = aud
    return L


def links_neighbours(ref, pull, audit):
    nc = CFG['neighbours']
    units, order = ayah_units(ref)
    s, _ = refkey(ref)
    L, recs, seen = [], [], set()
    for root, u, b in ayah_branches(ref):
        for nref, rel in b['neighbours']:
            r2 = letters_of_bref(nref)
            if not r2 or r2 == root:
                continue
            here, wn, sr = locations(r2, ref, exclude_ref3s={x[0] for x in u['words']})
            if not (here or wn or (sr and rel in nc['surah_level_relations'])):
                continue
            key = tuple(sorted([b['ref'], nref]))
            if key in seen:
                continue
            seen.add(key)
            nb = branch_of(nref) or {'image': ''}
            L.append(f"- {b['ref']} «{b['image']}» — dictionary relation: {rel} — {nref} «{nb['image']}» ({r2}): "
                     f"{loc_text(here, wn, sr if rel in nc['surah_level_relations'] else [])}")
            recs.append(dict(branch_ref=b['ref'], relation=rel, other=nref, other_root=r2))
    ayah_brefs = {b['ref'] for _, _, b in ayah_branches(ref)}
    for wr, (envs, occ) in window_units(ref).items():
        for eid in sorted(envs):
            for b in env_branches(eid):
                for nref, rel in b['neighbours']:
                    if nref not in ayah_brefs:
                        continue
                    key = tuple(sorted([b['ref'], nref]))
                    if key in seen:
                        continue
                    seen.add(key)
                    nb = branch_of(nref) or {'image': ''}
                    L.append(f"- {b['ref']} «{b['image']}» ({wr}, in the window: {where_text(occ)}) — dictionary relation: "
                             f"{rel} — {nref} «{nb['image']}» ({letters_of_bref(nref)}, this ayah)")
                    recs.append(dict(branch_ref=b['ref'], relation=rel, other=nref, direction='inward'))
    pull['dictionary_neighbour_links'] = recs
    return L


@functools.lru_cache(None)
def slm_catalog():
    import numpy as np
    cat = json.load(open(SLM_NET + '/catalog.json', encoding='utf-8'))['cards']
    gi = {f"{c['source_root_id']}/{c['branch_id']}": c['global_index'] for c in cat}
    n = len(cat)
    neo = np.memmap(P + '/quran-slm/artifacts/corpus_ensemble/neoarabert_directional_rank.u16le', dtype='<u2', mode='r',
                    shape=(n, n))
    return gi, neo


def links_slm(ref, pull, audit):
    gi, neo = slm_catalog()
    k = CFG['slm_pairs']['max_mutual_rank']
    L, recs = [], []
    for root, u, b in ayah_branches(ref):
        i = gi.get(b['ref'])
        if i is None:
            continue
        for wr, (envs, occ) in window_units(ref).items():
            for eid in sorted(envs):
                for c in env_branches(eid):
                    j = gi.get(c['ref'])
                    if j is None:
                        continue
                    ra, rb = int(neo[i, j]), int(neo[j, i])
                    if 0 < ra <= k and 0 < rb <= k:
                        L.append(f"- {b['ref']} «{b['image']}» ~ {c['ref']} «{c['image']}» ({wr}, in the window: {where_text(occ)})")
                        recs.append(dict(branch_ref=b['ref'], other=c['ref']))
    pull['quran_slm_pairs'] = recs
    return L


def links_cooccurrence(ref, pull, audit):
    """Pairs of roots of this ayah that the Quran puts together in other ayat more than chance would (the validator's
    root_cooccurrence rule: at least min_other_ayat other ayat hold both roots and ln(c(N-1)/(nA nB)) > min_ln_pmi,
    with this ayah removed from every count). The page shows the defined pairs; the pull file keeps every pair with
    a positive association. No number reaches the page."""
    cc = CFG['cooccurrence']
    units, order = ayah_units(ref)
    roots = [r for r in order if units[r]['words']]
    surf = {r: [(x[0], x[1]) for x in units[r]['words']] for r in roots}
    n = NAY - 1
    L, cands, aud = [], [], []
    for i, ra in enumerate(roots):
        A = ROOT_AYAT.get(ra, set()) - {ref}
        for rb in roots[i + 1:]:
            B = ROOT_AYAT.get(rb, set()) - {ref}
            both = sorted(A & B, key=refkey)
            c = len(both)
            if not c or not A or not B:
                continue
            v = math.log(c * n / (len(A) * len(B)))
            if v <= 0:
                continue
            ok = c >= cc['min_other_ayat'] and v > cc['min_ln_pmi']
            cands.append(dict(roots=[ra, rb], other_ayat=both))
            aud.append(dict(roots=[ra, rb], c=c, nA=len(A), nB=len(B), ln_pmi=round(v, 3), shown=ok))
            if ok:
                L.append(f"- {ra} ({where_text(surf[ra])}) and {rb} ({where_text(surf[rb])}) also stand together in "
                         f"{', '.join(both)}")
    pull['root_cooccurrence_candidates'] = cands
    audit['root_cooccurrence'] = aud
    return L


def section_C(ref, pull, audit):
    L = ['## C. Typed links (each with its path in words)', '']
    lk = CFG['links']
    blocks = [('definitional_pointers', 'Definitional pointers: a branch\'s own text names a word of another root '
               'that stands in this ayah, the window or the surah (or a rare root anywhere); lines marked with a window '
               'root read the other way (a neighbour\'s branch names a word of this ayah)', links_pointers),
              ('rare_lemma_bridges', 'Rare-lemma bridges: a word named in a branch text that the Quran puts beside a '
               'neighbouring root, with the witness ayat', links_bridges),
              ('dictionary_neighbours', 'Dictionary neighbour relations (the dictionary\'s own neighbour_distinctions) '
               'reaching a root of this ayah or the window', links_neighbours),
              ('root_cooccurrence', 'Root co-occurrence: two roots of this ayah that the Quran puts together in '
               'other ayat, with those ayat', links_cooccurrence),
              ('quran_slm_pairs', 'quran-slm branch pairs (mutual near neighbours)', links_slm)]
    for key, title, fn in blocks:
        if not lk.get(key):
            continue
        lines = fn(ref, pull, audit)
        L += [f'### {title}', ''] + (lines or ['(none)']) + ['']
    return '\n'.join(L).rstrip()


# ============================================================================ D. Quran usage

def pron_token(ref3, prep):
    """The prep+pronoun token near a word (فيه, فيها ...), for attachments whose partner is a pronoun."""
    s, a, w = ref3.split(':')[:3]
    ws = W.get(f'{s}:{a}', [])
    p = rasm(norm(prep))
    for x in ws[int(w):int(w) + 4]:
        t = rasm(norm(x['surface']))
        if p and t.startswith(p) and not x['roots']:
            return x['surface']
    return None


def construction_parts(ref3, root):
    """Construction of one use from grammar attachments: the dictionary's aligned occurrence first, else the
    quran-data grammar attachments of the ayah that name this root. Returns ([(key, display)], voice, source)."""
    w = word_by_ref3(ref3)
    atts, voice, src = None, '', ''
    for eid in envs_for_word(w, root) if w else []:
        o = OCC.get((eid, ref3))
        if o:
            voice = o['voice']
            if o['status'] == 'aligned':
                atts = [(rel, role, prep, orr, osf) for rel, role, prep, orr, osf in o['atts']]
                src = 'dictionary occurrence attachments'
            break
    if atts is None:
        s, a = ref3.split(':')[:2]
        atts = []
        for rel, dsf, dr, hsf, hr, prep in GATT.get(f'{s}:{a}', []):
            if dr == root and hr != root:
                atts.append((rel, 'dependent', prep, hr, hsf))
            elif hr == root and dr != root:
                atts.append((rel, 'head', prep, dr, dsf))
        src = 'quran-data grammar attachments (root in ayah)' if atts else 'none'
    parts = []
    for rel, role, prep, orr, osf in atts:
        pt = ''
        if not osf and rel == 'prep_complement':
            pt = pron_token(ref3, prep) or '[pronoun]'
        partner = osf or pt
        pk = orr or ('PRON' if pt else rasm(norm(osf)))
        rl = f" ({orr})" if orr else ''
        if rel == 'prep_complement' and role == 'head':
            parts.append(((rel, role, rasm(norm(prep)), pk), f"~ {prep} {partner}{rl}" if osf else f"~ {partner}"))
        elif rel == 'prep_complement':
            parts.append(((rel, role, rasm(norm(prep)), pk), f"{partner}{rl} {prep} ~"))
        elif rel == 'direct_object' and role == 'head':
            parts.append(((rel, role, '', pk), f"~ + object {partner}{rl}"))
        elif rel == 'idafa':
            parts.append(((rel, role, '', pk), f"~ {partner}{rl}" if role == 'head' else f"{partner}{rl} ~"))
        elif rel == 'adjective':
            parts.append(((rel, role, '', pk), f"~ {partner}{rl}" if role == 'head' else f"{partner}{rl} ~"))
    parts.sort(key=lambda x: x[0])
    return parts, voice, src


def usage_every(root, ref):
    uses = sorted(ROOT_WORDS.get(root, []), key=refkey)
    groups = collections.OrderedDict()
    recs = []
    for r3 in uses:
        w = word_by_ref3(r3)
        i = w['roots'].index(root) if w and root in w['roots'] else 0
        lem = w['lemmas'][i] if w and i < len(w['lemmas']) else ''
        parts, voice, src = construction_parts(r3, root)
        key = (lem, 'passive' if voice == 'PASS' else '', tuple(k for k, _ in parts))
        g = groups.setdefault(key, dict(display=[d for _, d in parts], uses=[]))
        g['uses'].append(r3)
        recs.append(dict(ref=r3, lemma=lem, voice=voice, construction=[d for _, d in parts], source=src))
    L = [f"#### {root} — {len(uses)} uses"]
    for (lem, vc, _), g in groups.items():
        cons = ' · '.join(g['display']) or 'no attached partner'
        L.append(f"- {lem}{', ' + vc if vc else ''} [{cons}] — {len(g['uses'])}: "
                 + ', '.join(x.rsplit(':', 1)[0] for x in g['uses']))
        for r3 in g['uses']:
            L.append(f"  - {r3.rsplit(':', 1)[0]} {kwic(r3)}" + ('  ◀' if r3.startswith(ref + ':') else ''))
    return L, recs


def usage_partners(root):
    rows = [r for r in COLLOC_BY_ROOT.get(root, []) if int(r['attach_count'] or 0) >= CFG['usage']['partner_min_attach']]
    forms = collections.defaultdict(list)
    for r in rows:
        forms[(r['form_tag'], r['instance_count'])].append(r)
    L = [f"#### {root} — {len(ROOT_WORDS.get(root, []))} uses — partners by form"]
    for (ft, n) in sorted(forms, key=lambda x: x[0]):
        ps = sorted(forms[(ft, n)], key=lambda r: (r['partner_root'], r['partner_form_tag']))
        L.append(f"- {ft} ({n} instances): " + '; '.join(
            f"{p['partner_root']} {p['partner_form_tag']} {p['attach_count']}/{p['total_attach']} {p['top_rel']}" for p in ps))
    return L, rows


def section_D(ref, pull):
    uc = CFG['usage']
    units, order = ayah_units(ref)
    own = [r for r in order if units[r]['words']]
    s, a = refkey(ref)
    L = ['## D. Quran usage', '', f"### Every use, grouped by lemma and construction (roots with up to "
         f"{uc['every_use_max_uses']} uses; ~ = the word; construction from grammar attachments)", '']
    every, partners = {}, {}
    for root in own:
        n = len(ROOT_WORDS.get(root, []))
        if 0 < n <= uc['every_use_max_uses']:
            lines, recs = usage_every(root, ref)
            L += lines + ['']
            every[root] = recs
    if not every:
        L += ['(none)', '']
    L += ['### Partners by form for the other roots (quran-data grammar collocation profiles: form, instances, '
          'partner root and form, attachments / all attachments of the form, main relation)', '']
    for root in own:
        n = len(ROOT_WORDS.get(root, []))
        if n > uc['every_use_max_uses']:
            lines, rows = usage_partners(root)
            L += lines + ['']
            partners[root] = [{k: r[k] for k in ('form_tag', 'instance_count', 'partner_root', 'partner_form_tag',
                                                  'attach_count', 'total_attach', 'top_rel', 'rel_dist')} for r in rows]
    L += ['### Rare pairings among this ayah\'s roots (root pairs that share only a few ayat)', '']
    fe = []
    for i, x in enumerate(own):
        for y in own[i + 1:]:
            co = sorted(ROOT_AYAT.get(x, set()) & ROOT_AYAT.get(y, set()), key=refkey)
            if 2 <= len(co) <= uc['formula_max_ayat']:
                L.append(f"- {x} + {y}: {len(co)} ayat — {', '.join(co)}")
                fe.append(dict(roots=[x, y], ayat=co))
    if not fe:
        L.append('(none)')
    L += ['', '### Same-surah occurrences of this ayah\'s roots', '']
    ss = {}
    for root in own:
        hits = surfaces_of_root_in(root, [r for r in surah_refs(s) if r != ref])
        if hits:
            L.append(f"- {root}: {where_text(hits)}")
            ss[root] = [h[0] for h in hits]
    pull['usage'] = dict(every_use=every, partners_by_form=partners, rare_pairings=fe, same_surah=ss)
    return '\n'.join(L).rstrip()


# ============================================================================ E. parallels (union of lenses)

PRON = ('هما', 'كما', 'هم', 'هن', 'كم', 'كن', 'نا', 'ها', 'ه', 'ك', 'ي')
PART_BASE = {'علي': 'على', 'على': 'على', 'الي': 'الى', 'الى': 'الى', 'في': 'في', 'من': 'من', 'عن': 'عن',
             'ل': 'ل', 'ب': 'ب', 'مع': 'مع', 'عند': 'عند', 'بين': 'بين', 'لدي': 'لدى', 'ان': 'ان', 'لكن': 'لكن',
             'حتي': 'حتى', 'ما': 'ما', 'لا': 'لا', 'لم': 'لم', 'لن': 'لن', 'اذا': 'اذا', 'قد': 'قد', 'ثم': 'ثم',
             'او': 'او', 'الذي': 'الذي', 'الذين': 'الذين', 'التي': 'التي', 'هو': 'هو', 'هي': 'هي', 'انما': 'انما'}


def particle_token(surface):
    """Particles with their pronoun suffix normalised (ʿalayhinna ~ ʿalayhim), from the C2 prototype."""
    s = norm(surface)
    for pre in ('و', 'ف'):
        if s.startswith(pre) and len(s) > 2:
            s2 = s[1:]
            if any(s2.startswith(b) for b in PART_BASE) or s2 in PART_BASE:
                s = s2
                break
    if s in PART_BASE:
        return PART_BASE[s]
    for p_ in PRON:
        if s.endswith(p_) and len(s) > len(p_):
            b = s[:-len(p_)]
            if b in PART_BASE:
                return PART_BASE[b] + '+P'
    if s in ('له', 'لها', 'لهم', 'لهن', 'لكم', 'لنا', 'لي', 'لك', 'بهم', 'به', 'بها', 'بكم'):
        return s[0] + '+P'
    return s


def word_token(w):
    if w['lemmas'] and w['lemmas'][0]:
        return 'L:' + norm(w['lemmas'][0])
    return 'P:' + particle_token(w['surface'])


class Parallels:
    """Lens scores for every other ayah (C2 prototype, scene lens removed, loaded lens at root level without any
    construction detector). Scores stay internal; the page shows lens names and shared words only."""

    def __init__(self):
        pc = CFG['parallels']
        self.pc = pc
        self.ix = {r: i for i, r in enumerate(REFS)}
        self.roots = {r: set(AYAH_ROOTS[r]) for r in REFS}
        self.lem_by_root = {}
        self.lem_show = {}
        for r in REFS:
            d = collections.defaultdict(set)
            for w in W.get(r, []):
                for i, rt in enumerate(w['roots']):
                    lem = w['lemmas'][i] if i < len(w['lemmas']) else ''
                    if lem:
                        d[rt].add(norm(lem))
                        self.lem_show.setdefault(norm(lem), lem)
            self.lem_by_root[r] = d
        self.df_root = collections.Counter(x for s in self.roots.values() for x in s)
        self.df_lem = collections.Counter((rt, l) for d in self.lem_by_root.values() for rt, ls in d.items() for l in ls)
        tokdf = collections.Counter()
        toks = {}
        for r in REFS:
            toks[r] = [word_token(w) for w in W.get(r, [])]
            tokdf.update(set(toks[r]))
        self.ngr = {}
        for r in REFS:
            t = toks[r]
            g = set()
            for n in (2, 3):
                for i in range(len(t) - n + 1):
                    tup = tuple(t[i:i + n])
                    if any(x.startswith('L:') and tokdf.get(x, 0) <= pc['phrase_content_lemma_max_ayat'] for x in tup):
                        g.add(tup)
            self.ngr[r] = g
        self.df_ngr = collections.Counter(x for s in self.ngr.values() for x in s)
        self.inv_root = collections.defaultdict(set)
        for r, s in self.roots.items():
            for x in s:
                self.inv_root[x].add(r)
        self.inv_ngr = collections.defaultdict(set)
        for r, s in self.ngr.items():
            for x in s:
                self.inv_ngr[x].add(r)
        self._tm = None
        self._loaded = {}

    def idf(self, df):
        return math.log(NAY / max(1, df))

    def textmap(self):
        if self._tm is None:
            import numpy as np
            nodes = read_tsv(TEXTMAP + '/nodes.tsv')
            key = [n_['ayah_ref'] for n_ in nodes]
            n = len(key)
            mm = {s: np.memmap(f'{TEXTMAP}/{s}_raw_directional_rank.u16le', dtype='<u2', mode='r', shape=(n, n))
                  for s in ('e5', 'neo', 'character')}
            self._tm = (key, {k: i for i, k in enumerate(key)}, mm)
        return self._tm

    def context(self, root, ref):
        ctx = set(x for x in self.roots.get(ref, ()) if x != root)
        s, a = refkey(ref)
        for nb in (f'{s}:{a - 1}', f'{s}:{a + 1}'):
            if nb in self.roots:
                ctx |= {x for x in self.roots[nb] if x != root}
        return ctx

    def loaded_partners(self, root):
        """Recurring partners of a root across its ayat (binomial tail, lift >= 3): {partner: [ayat]}."""
        if root in self._loaded:
            return self._loaded[root]
        refs = sorted(ROOT_AYAT.get(root, ()), key=refkey)
        n = len(refs)
        lo, hi = self.pc['loaded_root_ayat']
        out = {}
        if lo <= n <= hi:
            ctxs = {r: self.context(root, r) for r in refs}
            k = collections.Counter(x for r in refs for x in ctxs[r])
            for x, kx in sorted(k.items()):
                if kx < 2:
                    continue
                q = 1 - (1 - self.df_root.get(x, 1) / NAY) ** 3
                if kx / max(n * q, 1e-9) < 3.0:
                    continue
                if 10 ** (-neglog10_binom_tail(kx, n, q)) < 0.05:
                    out[x] = [r for r in refs if x in ctxs[r]]
        self._loaded[root] = out
        return out

    def scores(self, f):
        import numpy as np
        S = {L: collections.Counter() for L in ('root', 'lemma', 'phrase', 'echo', 'loaded', 'textmap')}
        why = {L: collections.defaultdict(list) for L in S}
        for x in sorted(self.roots.get(f, ())):
            wgt = self.idf(self.df_root[x])
            for r in sorted(self.inv_root[x], key=refkey):
                if r == f:
                    continue
                S['root'][r] += wgt
                why['root'][r].append(x)
                fl, cl = self.lem_by_root[f].get(x, set()), self.lem_by_root[r].get(x, set())
                for l in sorted(fl & cl):
                    S['lemma'][r] += self.idf(self.df_lem.get((x, l), 1))
                    why['lemma'][r].append(self.lem_show.get(l, l))
                if fl and cl and not (fl & cl) and self.df_root[x] <= self.pc['echo_root_max_ayat']:
                    S['echo'][r] += wgt
                    sh = lambda ls: '/'.join(sorted(self.lem_show.get(l, l) for l in ls))
                    why['echo'][r].append(f"{x}: {sh(fl)} ~ {sh(cl)}")
        for g in sorted(self.ngr.get(f, ())):
            if self.df_ngr[g] > self.pc['phrase_ngram_max_ayat']:
                continue
            wgt = self.idf(self.df_ngr[g])
            for r in sorted(self.inv_ngr[g], key=refkey):
                if r != f:
                    S['phrase'][r] += wgt
                    why['phrase'][r].append(' '.join(t[2:] for t in g))
        for x in sorted(self.roots.get(f, ())):
            parts = self.loaded_partners(x)
            if not parts:
                continue
            ctx = self.context(x, f)
            for pt, refs in sorted(parts.items()):
                if pt not in ctx:
                    continue
                for r in refs:
                    if r != f:
                        S['loaded'][r] += self.idf(self.df_root[x]) + self.idf(self.df_root.get(pt, 1))
                        why['loaded'][r].append(f"{x} with {pt}")
        key, kix, mm = self.textmap()
        if f in kix:
            a = kix[f]
            tot = np.zeros(len(key), np.float32)
            for s, wt in (('e5', 0.35), ('neo', 0.35), ('character', 0.30)):
                out = np.asarray(mm[s][a, :], dtype=np.float32)
                inn = np.asarray(mm[s][:, a], dtype=np.float32)
                ok = (out != 0) & (inn != 0)
                v = np.zeros_like(out)
                v[ok] = 0.5 * (1 / (10 + out[ok]) + 1 / (10 + inn[ok]))
                tot += wt * v
            tot[a] = 0
            for j in np.nonzero(tot > 0)[0]:
                S['textmap'][key[j]] = float(tot[j])
        return S, why


@functools.lru_cache(None)
def parallels_model():
    return Parallels()


def _parallel_thresholds():
    """Per lens: the configured quantile of its score over random (focus, other ayah) pairs, zeros included."""
    import numpy as np
    pc = CFG['parallels']
    PA = parallels_model()
    rnd = random.Random(pc['seed'])
    foci = rnd.sample(REFS, pc['random_focus_sample'])
    vals = {L: [] for L in pc['lenses']}
    for f in foci:
        S, _ = PA.scores(f)
        for L in pc['lenses']:
            v = np.zeros(NAY - 1, np.float32)
            nz = [x for r, x in S[L].items() if r != f]
            v[:len(nz)] = nz
            vals[L].append(v)
    out = {}
    for L in pc['lenses']:
        allv = np.concatenate(vals[L])
        out[L] = float(np.quantile(allv, pc['random_quantile']))
    return dict(quantile=pc['random_quantile'], sample=pc['random_focus_sample'], thresholds=out)


def parallel_thresholds():
    pc = CFG['parallels']
    return cached(f"parallel_thresholds_q{pc['random_quantile']}_n{pc['random_focus_sample']}_s{pc['seed']}",
                  _parallel_thresholds)['thresholds']


# Display names for the lenses. 'echo' and 'loaded' are the user's ruling terms (echo tier, loaded word); a script lens
# must not look like one of those verdicts, so the page names the computation instead.
LENS_LABEL = {'echo': 'same-root-other-form', 'loaded': 'recurring-partner'}


def section_E(ref, pull, audit):
    pc = CFG['parallels']
    PA = parallels_model()
    thr = parallel_thresholds()
    S, why = PA.scores(ref)
    s, a = refkey(ref)
    members = collections.defaultdict(dict)
    aud = collections.defaultdict(dict)
    for L in pc['lenses']:
        for r, v in S[L].items():
            if r != ref and v > thr[L]:
                members[r][L] = list(dict.fromkeys(why[L][r]))
                aud[r][L] = round(v, 4)
    same = sorted([r for r in members if refkey(r)[0] == s], key=refkey)
    other = sorted([r for r in members if refkey(r)[0] != s], key=refkey)
    shown_text = set(pull.get('text_shown', []))

    def line(r):
        lens = '; '.join(f"{LENS_LABEL.get(L, L)}: {', '.join(members[r][L])}" if members[r][L] else LENS_LABEL.get(L, L)
                         for L in pc['lenses'] if L in members[r])
        txt = ''
        if r not in shown_text and pc['show_text_other_surah']:
            txt = f"\n  {quran()[r]}"
        return f"- {r} — {lens}{txt}"
    L = ['## E. Parallels (a union of lenses; each ayah with the lenses that include it and the words it shares; '
         'same surah first, then Quran order)', '',
         'Lenses: root = shared roots weighted by rarity; lemma = shared lemmas; phrase = shared two- or three-word '
         'sequences (pronouns on particles normalised); same-root-other-form = a shared root in a different word form; '
         'recurring-partner = a word of this ayah with a partner it recurs with across its uses; textmap = the quran-slm '
         'ayah text map.', '',
         f"### Same surah ({len(same)})", ''] + ([line(r) for r in same] or ['(none)']) + \
        ['', f"### Other surahs ({len(other)})", ''] + ([line(r) for r in other] or ['(none)'])
    pull['parallels'] = [dict(ref=r, lenses={LENS_LABEL.get(L, L): v for L, v in members[r].items()}) for r in same + other]
    audit['parallels'] = dict(thresholds=thr, scores={r: aud[r] for r in same + other})
    return '\n'.join(L)


# ============================================================================ F. existing chains and relays

ANCHOR_RE = re.compile(r'(\d{1,3}):(\d{1,3}(?:\s?[-–]\s?\d{1,3})?(?:,\s?\d{1,3}(?:\s?[-–]\s?\d{1,3})?(?![\d:]))*)')
MOTIF_RE = re.compile(r'([^;`]*?)\s*\(?`(?:quranic:)?([^`]+?):(B\d+)(?:/m\d+)?`\)?')
FIELD_RE = re.compile(r'^- ([A-Z][A-Za-z ]+?):\s*(.*)$')


def anchor_refs(text):
    out = set()
    for m in ANCHOR_RE.finditer(text or ''):
        s = int(m.group(1))
        for part in re.split(r',\s?', m.group(2)):
            part = part.replace(' ', '')
            if re.search('[-–]', part):
                lo, hi = re.split('[-–]', part)
                if lo.isdigit() and hi.isdigit() and int(hi) >= int(lo):
                    out |= {f'{s}:{x}' for x in range(int(lo), int(hi) + 1)}
            elif part.isdigit():
                out.add(f'{s}:{int(part)}')
    return out


def motif_members(text):
    """[(label, [branch_ref...], root letters)] from an 'Active motifs' field (both review formats)."""
    out = []
    for m in MOTIF_RE.finditer(text or ''):
        label = m.group(1).strip(' ;,.()')
        key, bid = m.group(2).strip(), m.group(3)
        if key.startswith('root_'):
            refs = [f'{key}/{bid}']
            letters = letters_of_bref(refs[0])
        else:
            letters = nroot(key)
            refs = [b for e in LETTERS_ENV.get(letters, []) for b in ENV[e]['branches'] if b.endswith('/' + bid)]
        out.append((label, refs, letters))
    return out


@functools.lru_cache(None)
def channel_blocks(s):
    p = CHANNELS.format(S=s)
    if not os.path.exists(p):
        return []
    text = open(p, encoding='utf-8').read()
    blocks, parent = [], None
    for blk in re.split(r'\n(?=#{3,4} )', text):
        head = blk.split('\n', 1)[0]
        if not head.startswith('###'):
            continue
        fields = collections.OrderedDict()
        for line in blk.split('\n')[1:]:
            m = FIELD_RE.match(line.strip())
            if m:
                fields[m.group(1)] = m.group(2).strip()
        title = head.lstrip('#').strip()
        if head.startswith('#### '):
            blocks.append(dict(kind='sub', title=title, parent=parent, fields=fields))
        elif re.match(r'### \d+\.', head):
            parent = dict(title=title, fields=fields)
        elif re.match(r'### S\d+\.', head):
            blocks.append(dict(kind='standalone', title=title, parent=None, fields=fields))
        else:
            blocks.append(dict(kind='cross', title=title, parent=None, fields=fields))
    return blocks


def member_text(label, refs, letters):
    if not refs:
        return f"{label} — {letters} (branch not in the dictionary)"
    parts = []
    for r in refs:
        b = branch_of(r)
        if not b:
            parts.append(f"{letters} {r}")
            continue
        k = f"{b['kind']}" + (f" — {b['note']}" if b['note'] else '')
        ct = construction_tag(b)
        parts.append(f"{letters} {r} «{b['image']}» [{k}{(' ' + ct) if ct else ''}]")
    return f"{label} — " + ' / '.join(parts)


def chain_section(ref, ayah_brefs):
    s, _ = refkey(ref)
    blocks = channel_blocks(s)
    L, recs, included_titles = [], [], []
    for b in blocks:
        if b['kind'] == 'cross':
            continue
        f = b['fields']
        mem = motif_members(f.get('Active motifs', ''))
        hit_anchor = ref in anchor_refs(f.get('Ayah anchors', ''))
        hit_member = any(set(refs) & ayah_brefs for _, refs, _ in mem)
        if not (hit_anchor or hit_member):
            continue
        included_titles.append(re.sub(r'^(Subchannel [A-Z]\.|S\d+\.)\s*', '', b['title']))
        head = f"#### {b['parent']['title']} › {b['title']}" if b['parent'] else f"#### {b['title']}"
        L.append(head)
        if b['parent'] and b['parent']['fields'].get('Semantic invariant'):
            L.append(f"- invariant: {b['parent']['fields']['Semantic invariant']}")
        if f.get('Scene or process'):
            L.append(f"- scene or process: {f['Scene or process']}")
        L.append('- members: ' + '; '.join(member_text(*m) for m in mem))
        if f.get('Synthesis'):
            L.append(f"- synthesis: {f['Synthesis']}")
        if f.get('Ayah anchors'):
            L.append(f"- anchors: {f['Ayah anchors']}")
        L.append('')
        recs.append(dict(title=b['title'], parent=b['parent']['title'] if b['parent'] else None,
                         members=[dict(label=l, branch_refs=r, root=lt) for l, r, lt in mem],
                         anchors=f.get('Ayah anchors', ''), via=('anchor' if hit_anchor else '') + ('+member' if hit_member else '')))
    for b in blocks:
        if b['kind'] != 'cross':
            continue
        f = b['fields']
        mem = motif_members(f.get('Active bridge motifs', '') + ' ' + f.get('Active motifs', ''))
        placements = ' '.join(v for k, v in f.items() if 'lacement' in k)
        hit_title = any(t and t in placements for t in included_titles)
        hit_member = any(set(refs) & ayah_brefs for _, refs, _ in mem)
        if not (hit_title or hit_member):
            continue
        L.append(f"#### {b['title']} (across the surah)")
        for k, v in f.items():
            if k in ('Reading type',):
                continue
            if k in ('Active bridge motifs', 'Active motifs'):
                L.append('- members: ' + '; '.join(member_text(*m) for m in mem))
            else:
                L.append(f"- {k.lower()}: {v}")
        L.append('')
        recs.append(dict(title=b['title'], cross=True, members=[dict(label=l, branch_refs=r, root=lt) for l, r, lt in mem]))
    return L, recs


def relay_member(bref, letters, src_ref, idx):
    b = branch_of(bref)
    words = []
    if src_ref and idx:
        for i in idx:
            w = word_by_ref3(f'{src_ref}:{i}') if str(i).isdigit() else None
            if w:
                words.append(w['surface'])
    where = f"{src_ref}" + (f" {' '.join(words)}" if words else '')
    if not b:
        return f"{letters} {bref} ({where})"
    k = b['kind'] + (f" — {b['note']}" if b['note'] else '')
    ct = construction_tag(b)
    return f"{letters or letters_of_bref(bref)} {bref} «{b['image']}» ({where}) [{k}{(' ' + ct) if ct else ''}]"


def hft_relay(ref):
    s, a = refkey(ref)
    files = sorted(set(glob.glob(f'{HFT}/s{s}/readers/*/{s}_{a}.focus_trace.json')
                       + glob.glob(f'{HFT}/s{s}/readers/*/{s}_{a}.*.focus_trace.json')))
    rows, seen = [], set()
    for p in files:
        try:
            d = json.load(open(p, encoding='utf-8'))
        except Exception:
            continue
        for sect in ('baseline_models', 'context_deltas', 'surprising_valid_outliers'):
            for m in d.get(sect) or []:
                mem = []
                for t in m.get('activation_trace') or []:
                    if t.get('mapped_root_id') and t.get('branch_id'):
                        mem.append((f"{t['mapped_root_id']}/{t['branch_id']}", nroot(t.get('root', '')),
                                    t.get('source_ref', ''), t.get('source_word_indices') or []))
                key = tuple(sorted(x[0] for x in mem))
                if not mem or key in seen:
                    continue
                seen.add(key)
                anchor = m.get('focus_anchor', '')
                line = (f"- «{anchor}»: " if anchor else '- ') + ' + '.join(relay_member(*x) for x in mem)
                if CFG['chains']['relay_text']:
                    cr = m.get('changed_reading') or {}
                    line += f"\n  {cr.get('after', '') if isinstance(cr, dict) else ''}"
                rows.append((key, line, dict(anchor=anchor, members=[dict(branch_ref=x[0], root=x[1], ref=x[2], words=x[3])
                                                                     for x in mem])))
    # HFT's own section order (baseline, context delta, surprising outlier) is a class; sort by branch so it cannot leak
    rows.sort(key=lambda r: r[0])
    L, recs = [r[1] for r in rows], [r[2] for r in rows]
    return L, recs


@functools.lru_cache(None)
def v12_surah(s):
    p = f'{V12}/{s}_ayah_findings_publication.json'
    if not os.path.exists(p):
        return {}
    return {ay['ayah_ref']: ay.get('findings', []) for ay in json.load(open(p, encoding='utf-8')).get('ayat', [])}


def v12_relay(ref):
    s, _ = refkey(ref)
    L, recs, seen = [], [], set()
    for f in v12_surah(s).get(ref, []):
        mem = []
        for anc in f.get('anchors', []):
            if len(anc) == 3:
                wref, rid, bids = anc
                for bid in bids:
                    wr = wref.rsplit(':', 1)
                    mem.append((f'{rid}/{bid}', letters_of_bref(f'{rid}/{bid}'), wr[0], [wr[1]]))
        key = tuple(sorted(x[0] for x in mem))
        if not mem or key in seen:
            continue
        seen.add(key)
        line = '- ' + ' + '.join(relay_member(*x) for x in mem)
        if CFG['chains']['relay_text']:
            line += f"\n  {f.get('text', '')}"
        L.append(line)
        recs.append(dict(members=[dict(branch_ref=x[0], root=x[1], ref=f'{x[2]}:{x[3][0]}') for x in mem]))
    return L, recs


def section_F(ref, pull):
    ayah_brefs = {b['ref'] for _, _, b in ayah_branches(ref)}
    s, _ = refkey(ref)
    L = ['## F. Existing chains', '']
    ch = CFG['chains']
    if ch['channel_reviews']:
        lines, recs = chain_section(ref, ayah_brefs)
        L += [f"### Surah {s} channel review: subchannels anchored in this ayah or using a branch of its roots "
              f"(members with the dictionary's branch_kind and scope note)", ''] + (lines or ['(none)', ''])
        pull['chains'] = recs
    if ch['hft_relay']:
        lines, recs = hft_relay(ref)
        L += ['### Earlier focus-trace relay for this ayah (HFT): branches activated together, with the ayah phrase '
              'they were attached to', ''] + (lines or ['(none)']) + ['']
        pull['hft_relay'] = recs
    if ch['v12_relay']:
        lines, recs = v12_relay(ref)
        L += ['### Earlier cross-run relay for this ayah (v12): branches anchored together', ''] + (lines or ['(none)']) + ['']
        pull['v12_relay'] = recs
    return '\n'.join(L).rstrip()


# ============================================================================ G. Majaz al-Quran (Abu Ubayda), quoted directly

HEADER_RE = re.compile(r'^#\s*[\("]?\s*سورة\s')
NUM_ENTRY_RE = re.compile(r'^# \(([^)]+)\) \(([0-9،,]+)\)')
QUOTE_ENTRY_RE = re.compile(r'^# "\s*([^"]+?)\s*"')
PROCL = {'و', 'ف', 'ب', 'ل', 'ك', 'س', 'وب', 'ول', 'فل', 'فب', 'وس', 'فس', 'ا', 'وا', 'فا', 'لل', 'ول', 'بال', 'وال', 'فال'}


def majaz_clean(t):
    t = re.sub(r'(^|\n)#\s?', ' ', t or '')
    t = re.sub(r'PageV\d+P\d+', ' ', t)
    t = re.sub(r'\bms\d+\b', ' ', t)
    return re.sub(r'\s+', ' ', t.replace('~~', ' ')).strip()


def rasm_tokens(t):
    return [x for x in (rasm(w) for w in re.findall('[ء-يٰ-ۓؐ-ًؚ-ٟۖ-ۭ]+', t or '')) if x]


def tok_match(pt, at):
    if pt == at or (len(pt) >= 3 and (pt == at + 'ي' or at == pt + 'ي')):
        return True
    for a_, b_ in ((at, pt), (pt, at)):
        if a_.endswith(b_) and len(b_) >= 2 and a_[:len(a_) - len(b_)] in PROCL:
            return True
    return False


@functools.lru_cache(None)
def ayah_rasm_tokens(ref):
    return [rasm(w['surface']) for w in W.get(ref, [])]


def phrase_in_ayah(phrase_toks, ref):
    at = ayah_rasm_tokens(ref)
    n = len(phrase_toks)
    for i in range(len(at) - n + 1):
        if all(tok_match(phrase_toks[j], at[i + j]) for j in range(n)):
            return True
    return False


def _majaz_raw_entries():
    """Walk the OpenITI Majaz text: surah headers in order (Fatiha first, then 2..114), numbered '(phrase) (N)' entries
    and quoted '" phrase "' entries, each with its full text up to the next entry."""
    lines = open(MAJAZ_RAW, encoding='utf-8').read().split('\n')
    surah, entries, cur = 0, [], None
    next_surah = 2
    for no, line in enumerate(lines, 1):
        if surah == 0 and 'مجاز تفسير ما في سورة (الحمد)' in line:
            surah = 1
        if HEADER_RE.match(line) and surah >= 1:
            q_ = QUOTE_ENTRY_RE.match(line)
            # a quoted "سورة …" line whose phrase is the text of an ayah of the current surah is an entry, not a header
            if not (q_ and surah >= 2 and any(phrase_in_ayah(rasm_tokens(q_.group(1)), f'{surah}:{x}')
                                              for x in range(1, surah_len(surah) + 1))):
                surah = next_surah
                next_surah += 1
                cur = None
                continue
        m = NUM_ENTRY_RE.match(line)
        q = None if m else QUOTE_ENTRY_RE.match(line)
        if m or q:
            cur = dict(line=no, surah=surah, phrase=(m or q).group(1).strip(), marker=m.group(2) if m else None,
                       numbered=bool(m), text=[line])
            entries.append(cur)
        elif cur is not None and line.strip():
            cur['text'].append(line)
    for e in entries:
        e['text'] = '\n'.join(e['text'])
    if next_surah != 115:
        print(f"warning: Majaz surah headers counted to {next_surah - 1}, expected 114", file=sys.stderr)
    return entries


DB_HEADER_RE = re.compile(r'#\s*[\("]?\s*(?:سورة\s|تم الجزء)')


def majaz_cut_header(t):
    """The sqlite table appends the next surah's header to the last entry of each surah, and its entry 1308 (18:108)
    runs on through surahs 19-114. An entry's text ends at the first surah header or volume end inside it."""
    m = DB_HEADER_RE.search(t or '')
    return t[:m.start()].rstrip() if m and m.start() > 0 else t


def _majaz_db():
    con = sqlite3.connect(f'file:{MAJAZ_DB}?mode=ro', uri=True)
    rows = con.execute("select id, surface_form, ayah_marker, entry_text_clean, section_path from quran_specialized_entries "
                       "where source='majaz_quran' order by id").fetchall()
    con.close()
    return [(i, sf, mk, majaz_cut_header(t), sec) for i, sf, mk, t, sec in rows]


def map_marker(phrase, marker, s):
    """Numbered entry -> (ref, basis) or (None, reason). The marker ayah must contain the phrase; else a unique
    ayah within the marker window, else the unique nearest one; otherwise unresolved."""
    toks = rasm_tokens(phrase)
    if sum(len(t) for t in toks) < 3:
        return None, 'phrase too short to map'
    nums = [int(x) for x in re.split('[،,]', marker or '') if x.isdigit()]
    if not nums or s < 1:
        return None, 'no surah or marker'
    win = CFG['majaz']['marker_window']
    n = surah_len(s)
    for m in nums:
        if 1 <= m <= n and phrase_in_ayah(toks, f'{s}:{m}'):
            return f'{s}:{m}', 'marker ayah contains the phrase'
    m = nums[0]
    if m > n + win:
        return None, 'marker outside the surah'
    cands = [x for x in range(max(1, m - win), min(n, m + win) + 1) if phrase_in_ayah(toks, f'{s}:{x}')]
    if len(cands) == 1:
        return f'{s}:{cands[0]}', f'only ayah within {win} of the marker containing the phrase (offset {cands[0] - m:+d})'
    if len(cands) > 1:
        d = sorted(cands, key=lambda x: abs(x - m))
        if abs(d[0] - m) < abs(d[1] - m):
            return f'{s}:{d[0]}', f'nearest of {len(cands)} ayat near the marker containing the phrase (offset {d[0] - m:+d})'
        return None, f'phrase in several ayat equally near the marker: {", ".join(f"{s}:{x}" for x in cands)}'
    return None, 'phrase not found near the marker'


def _majaz_index():
    raw = _majaz_raw_entries()
    db = _majaz_db()
    numbered = [e for e in raw if e['numbered']]
    out, j = [], 0
    for rid, sf, mk, txt, sec in db:
        k = j
        while k < len(numbered) and not (numbered[k]['phrase'] == (sf or '').strip() and numbered[k]['marker'] == mk):
            k += 1
        s = numbered[k]['surah'] if k < len(numbered) else 0
        line = numbered[k]['line'] if k < len(numbered) else None
        if k < len(numbered):
            j = k + 1
        ref, basis = map_marker(sf, mk, s)
        out.append(dict(source='sqlite', id=rid, surah=s, raw_line=line, phrase=sf, marker=mk, text=txt, ref=ref, basis=basis))
    if CFG['majaz']['raw_fallback']:
        db_surahs = {e['surah'] for e in out if e['surah']}
        by_surah = collections.defaultdict(list)
        for e in raw:
            if not e['numbered'] and e['surah'] >= 1 and e['surah'] not in db_surahs:
                by_surah[e['surah']].append(e)
        for s, es in by_surah.items():
            cands = []
            for e in es:
                toks = rasm_tokens(e['phrase'])
                if sum(len(t) for t in toks) < 3:
                    cands.append([])
                    continue
                cands.append([x for x in range(1, surah_len(s) + 1) if phrase_in_ayah(toks, f'{s}:{x}')])
            fixed = [c[0] if len(c) == 1 else None for c in cands]
            for i, e in enumerate(es):
                c = cands[i]
                if len(c) == 1:
                    ref, basis = f'{s}:{c[0]}', 'phrase found in one ayah of the surah'
                elif not c:
                    ref, basis = None, 'phrase not found in the surah'
                else:
                    lo = max([f for f in fixed[:i] if f] or [0])
                    hi = min([f for f in fixed[i + 1:] if f] or [10 ** 6])
                    inside = [x for x in c if lo <= x <= hi]
                    if len(inside) == 1:
                        ref, basis = f'{s}:{inside[0]}', 'phrase in several ayat; one lies between the neighbouring entries'
                    else:
                        ref, basis = None, f'phrase in several ayat: {", ".join(f"{s}:{x}" for x in c)}'
                out.append(dict(source='openiti_raw', id=None, surah=s, raw_line=e['line'], phrase=e['phrase'], marker=None,
                                text=e['text'], ref=ref, basis=basis))
    return out


MAJAZ = cached('majaz', _majaz_index)


def section_G(ref, pull):
    s, _ = refkey(ref)
    mine = [e for e in MAJAZ if e['ref'] == ref]
    unresolved = [e for e in MAJAZ if e['surah'] == s and e['ref'] is None]
    L = ["## G. Majāz al-Qurʾān (Abū ʿUbayda), entries for this ayah, quoted from the Majāz text", '']
    for e in mine:
        src = (f"openiti_context.sqlite quran_specialized_entries id {e['id']}" if e['source'] == 'sqlite'
               else f"OpenITI Majāz text line {e['raw_line']} (this surah is not segmented in the sqlite table)")
        L.append(f"- ({e['phrase']}){' (' + e['marker'] + ')' if e['marker'] else ''} [{src}]")
        L.append(f"  {majaz_clean(e['text'])}")
    if not mine:
        L.append('(no entry mapped to this ayah)')
    pull['majaz'] = dict(entries=[dict(source=e['source'], id=e['id'], raw_line=e['raw_line'], phrase=e['phrase'],
                                       marker=e['marker'], mapping_basis=e['basis'], text=majaz_clean(e['text'])) for e in mine],
                         unresolved_in_this_surah=[dict(source=e['source'], id=e['id'], raw_line=e['raw_line'],
                                                        phrase=e['phrase'], marker=e['marker'], reason=e['basis'])
                                                   for e in unresolved])
    return '\n'.join(L)


# ============================================================================ H. Turkish gloss losses

@functools.lru_cache(None)
def gloss_results(eid):
    p = os.path.join(GLOSSRES, eid + '.json')
    if not os.path.exists(p):
        return {}
    d = json.load(open(p, encoding='utf-8'))
    return {b['branch_ref']: b for b in d.get('branches', [])}


def profile_text(pr):
    parts = []
    if pr.get('fit') and pr.get('fit') != 'none':
        parts.append(f"fit: {pr['fit']}")
    for k in ('loses', 'adds', 'collision'):
        if pr.get(k):
            parts.append(f"{k}: {pr[k]}")
    return '; '.join(parts)


@functools.lru_cache(None)
def loanword_cards():
    out = {}
    for p in sorted(glob.glob(LOANWORDS + '/*.json')):
        try:
            d = json.load(open(p, encoding='utf-8'))
        except Exception:
            continue
        for it in d.get('items', []):
            out[f"{nroot(it['root'])}|{it['lemma']}"] = it
    return out


def gr_items(b, with_lexical=False):
    """Gloss-generation results (dictionary v2) for a branch: the concept and contextual glosses (lexical-unit glosses
    only when asked: they narrow by design) whose error profile records something."""
    gr = gloss_results(b['env']).get(b['ref']) if not b['env'].startswith('furuq:') else None
    if not gr:
        return None
    items, seen = [], set()
    cands = [('concept', gr.get('concept_gloss') or {})] + [('contextual', g) for g in gr.get('contextual_glosses') or []] \
        + ([('lexical', g) for g in (gr.get('lexical_glosses') or {}).values()] if with_lexical else [])
    for kind, g in cands:
        e = g.get('error') or {}
        if not ((e.get('fit') and e.get('fit') != 'none') or e.get('loses_facet_ids') or e.get('adds') or e.get('collision')):
            continue
        key = (g.get('text'), json.dumps(e, ensure_ascii=False, sort_keys=True))
        if key in seen:
            continue
        seen.add(key)
        parts = []
        if e.get('fit') and e['fit'] != 'none':
            parts.append(f"fit: {e['fit']}")
        if e.get('loses_facet_ids'):
            parts.append('loses: ' + '; '.join(b['facets'].get(f, f) for f in e['loses_facet_ids']))
        for k in ('adds', 'collision', 'reason'):
            if e.get(k):
                parts.append(f"{k}: {e[k]}")
        items.append(dict(text=g.get('text'), gloss_kind=kind, error=e, line=f"«{g.get('text')}» ({kind}) " + '; '.join(parts)))
    return items


def section_H(ref, pull):
    L = ['## H. Turkish gloss losses (the dictionary\'s gloss error profiles for the branches of this ayah\'s roots: '
         'fit, what the Turkish gloss loses, adds or collides with)', '']
    recs = []
    for root, u, b in ayah_branches(ref):
        items = gr_items(b)
        src = 'dictionary v2 gloss results'
        if items is None:
            src = 'Turkish entry'
            items = []
            t = profile_text(b['gloss_profile'])
            if t:
                items.append(dict(text=b['gloss'], gloss_kind='concept', error=b['gloss_profile'], line=f"«{b['gloss']}» (concept) {t}"))
            for g in b['ctx']:
                tt = profile_text(g['profile'])
                if tt:
                    items.append(dict(text=g['text'], gloss_kind='contextual', error=g['profile'], line=f"«{g['text']}» (contextual) {tt}"))
        full = gr_items(b, with_lexical=True) or items
        if items:
            L.append(f"- {b['ref']} «{b['image']}»: " + ' | '.join(x['line'] for x in items))
        if full:
            recs.append(dict(branch_ref=b['ref'], source=src, glosses=[{k: v for k, v in x.items() if k != 'line'} for x in full]))
    if len(L) == 2:
        L.append('(no loss, addition or collision recorded for the concept and contextual glosses)')
    cards = loanword_cards()
    lw = []
    for w in W.get(ref, []):
        for i, r in enumerate(w['roots']):
            lem = w['lemmas'][i] if i < len(w['lemmas']) else ''
            c = cards.get(f'{r}|{lem}')
            if c and c.get('loanwords'):
                for x in c['loanwords']:
                    keeps = '; '.join(f"{k.get('branch', '')} {k.get('note', '')}" for k in x.get('arabic_keeps', []))
                    lw.append(f"- {lem} ({r}) → {x.get('word', '')}: the reader hears {x.get('reader_hears', '')} "
                              f"Drift: {x.get('drift', '')} Arabic keeps: {keeps}"
                              + (f" False friend: {x['false_friend']}" if x.get('false_friend') else ''))
    if lw:
        L += ['', '### Turkish loanword cards (v15)', ''] + list(dict.fromkeys(lw))
    pull['turkish_gloss_losses'] = recs
    pull['loanword_cards'] = list(dict.fromkeys(lw))
    return '\n'.join(L)


# ============================================================================ I. variant readings

def section_I(ref, pull):
    L = ['## I. Variant readings (qirāʾāt corpus; its own word numbering, with the matching word of the ayah in brackets)', '']
    rows = qiraat().get(ref, [])
    for r in rows:
        qw = word_by_ref3(qiraat_word(r))
        L.append(f"- {r['tsv_word_ref']} {r['qiraat_arabic']} ({r['qiraat_transliteration']}; {r['qiraat_reader_set']}; "
                 f"{r['qiraat_transmission_type']})" + (f" [word {qw['ref3']} {qw['surface']}]" if qw else '')
                 + f" {r['qiraat_note']}")
    if not rows:
        L.append('(none recorded)')
    pull['qiraat'] = rows
    return '\n'.join(L)


# ============================================================================ assembly

SECTIONS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']


def build(ref):
    s, a = refkey(ref)
    pull = dict(ayah=ref, text=quran()[ref])
    audit = dict(ayah=ref, config=CFG)
    parts = collections.OrderedDict()
    parts['A'] = section_A(ref, pull)
    parts['B'] = section_B(ref, pull)
    parts['C'] = section_C(ref, pull, audit)
    parts['D'] = section_D(ref, pull)
    parts['E'] = section_E(ref, pull, audit)
    parts['F'] = section_F(ref, pull)
    parts['G'] = section_G(ref, pull)
    parts['H'] = section_H(ref, pull)
    parts['I'] = section_I(ref, pull)
    stem = f'{s}_{a}'
    pull_path = os.path.join(OUT, stem + '.pull.json')
    files = ['', '## Files you may read', '',
             f"- every full list behind this page (all branch fields and early phrases, every link candidate, the "
             f"collocation profiles, chain members, Majāz mapping): {pull_path}"]
    ents = sorted({r['early_entries_file'] for r in pull.get('roots', []) if r.get('early_entries_file')})
    if ents:
        files.append('- the six early dictionary entries (full text) of each root of this ayah: '
                     + ', '.join(ents))
    head = f"# {ref}\n"
    md = head + '\n\n'.join(parts.values()) + '\n' + '\n'.join(files) + '\n'
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, stem + '.md'), 'w', encoding='utf-8') as f:
        f.write(md)
    with open(pull_path, 'w', encoding='utf-8') as f:
        json.dump(pull, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, stem + '.audit.json'), 'w', encoding='utf-8') as f:
        json.dump(audit, f, ensure_ascii=False, indent=1)
    ar = len(AR_CH.findall(md))
    size = dict(chars=len(md), arabic_chars=ar, other_chars=len(md) - ar,
                tokens_calibrated=round(4581 + 1.151 * ar + 0.366 * (len(md) - ar)),
                sections={k: dict(chars=len(v), tokens=round(est_tokens(v))) for k, v in parts.items()},
                pull_bytes=os.path.getsize(pull_path))
    # what the partner lists would cost at a minimum of two attachments (reported only; the page keeps them all)
    alt = 0
    for root, rows in pull['usage']['partners_by_form'].items():
        forms = collections.defaultdict(list)
        for r in rows:
            if int(r['attach_count'] or 0) >= 2:
                forms[(r['form_tag'], r['instance_count'])].append(r)
        alt += sum(len(f"- {ft} ({n} instances): ") + sum(len(f"{p['partner_root']} {p['partner_form_tag']} "
                   f"{p['attach_count']}/{p['total_attach']} {p['top_rel']}; ") for p in ps) for (ft, n), ps in forms.items())
    size['report_only'] = dict(D_partner_lines_chars_if_min_attach_2=alt)
    return md, size


def main():
    refs = [a for a in sys.argv[1:] if not a.startswith('--')] or DEFAULT_REFS
    sizes_p = os.path.join(OUT, 'sizes.json')
    sizes = json.load(open(sizes_p, encoding='utf-8')) if os.path.exists(sizes_p) else {}
    for ref in refs:
        md, size = build(ref)
        sizes[ref] = size
        print(f"{ref}: {size['chars']:,} chars, ~{size['tokens_calibrated']:,} tokens (calibrated, with the 4,581 prefix); "
              + ' '.join(f"{k}:{v['tokens']:,}" for k, v in size['sections'].items()), flush=True)
    sizes = {k: sizes[k] for k in sorted(sizes, key=refkey)}
    with open(sizes_p, 'w', encoding='utf-8') as f:
        json.dump(sizes, f, ensure_ascii=False, indent=1)
    write_majaz_index()


def write_majaz_index():
    """The Majaz entries with their mapped ayah, for the E0 checks (checks/common.py reads this file, so a quote from
    the Majaz is attributed with the same parser and mapping the supply uses)."""
    rows = [dict(source=e['source'], id=e['id'], raw_line=e['raw_line'], surah=e['surah'], phrase=e['phrase'],
                 marker=e['marker'], ref=e['ref'], mapping_basis=e['basis'], text=majaz_clean(e['text'])) for e in MAJAZ]
    with open(os.path.join(OUT, 'majaz_index.json'), 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=0)


if __name__ == '__main__':
    main()
