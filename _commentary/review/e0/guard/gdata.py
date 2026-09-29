"""Read-only data layer for the form-aware construction guard (E0, verification only).

Sources (all read-only):
  quran-data/data/morphology/qac.sqlite.gz                QAC morphology (measure, voice, pos, lemma, suffixes)
  quran-data/data/bridges/qac-masaq.sqlite.gz             grammar-unit / attachment endpoint -> QAC morpheme joins
  quran-data/data/grammar/attachments/{attachments,verb_instances,cross_references}.tsv
  quran-data/data/dictionary/tr/root_*_entry.json         branches, branch_kind + scope note, early phrases, occurrences
  dictionary/data/working/furuq_v4.sqlite                 the dictionary's own lexical units (expression_ar per branch)
  root-dossier/out/activation_map.tsv                     evaluation labels only (never used by the detector)

The two .gz databases are decompressed once into a temp cache (GUARD_CACHE, default: ./cache, not committed), never
into any repo. Small pickles of the joined tables go to the same cache.
"""
import os, sys, csv, json, glob, gzip, re, shutil, sqlite3, pickle, functools, collections

csv.field_size_limit(sys.maxsize)
P = '/Volumes/OZTURK/_projects'
QD = f'{P}/quran-data/data'
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.environ.get('GUARD_CACHE', os.path.join(HERE, 'cache'))
os.makedirs(CACHE, exist_ok=True)

DIAC = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')


def norm(s):
    """Loose Arabic folding (diacritics, tatweel, alef/hamza seats, ya/alef maqsura, ta marbuta)."""
    s = DIAC.sub('', s or '')
    for a, b in (('ٱ', 'ا'), ('أ', 'ا'), ('إ', 'ا'), ('آ', 'ا'), ('ؤ', 'و'), ('ئ', 'ي'), ('ى', 'ي'), ('ة', 'ه'),
                 ('ء', '')):
        s = s.replace(a, b)
    return s


def nroot(r):
    """Root key: 'ء ت ي' style, hamza seats unified (dictionary writes ح م ء, grammar writes ح م أ)."""
    r = (r or '').strip()
    for a in 'أإؤئآ':
        r = r.replace(a, 'ء')
    if r and ' ' not in r and len(r) >= 2:
        r = ' '.join(r)
    return r


def _db(name, gz):
    path = os.path.join(CACHE, name)
    if not os.path.exists(path):
        tmp = path + '.tmp'
        with gzip.open(gz, 'rb') as fi, open(tmp, 'wb') as fo:
            shutil.copyfileobj(fi, fo)
        os.replace(tmp, path)
    return sqlite3.connect(f'file:{path}?mode=ro', uri=True)


def qac():
    return _db('qac.sqlite', f'{QD}/morphology/qac.sqlite.gz')


def bridge():
    return _db('qac_masaq.sqlite', f'{QD}/bridges/qac-masaq.sqlite.gz')


def cached(name):
    def deco(fn):
        @functools.lru_cache(None)
        def wrap():
            path = os.path.join(CACHE, f'guard_{name}.pkl')
            if os.path.exists(path):
                with open(path, 'rb') as f:
                    return pickle.load(f)
            val = fn()
            with open(path + '.tmp', 'wb') as f:
                pickle.dump(val, f)
            os.replace(path + '.tmp', path)
            return val
        return wrap
    return deco


# ----------------------------------------------------------------------------------------------------- QAC words
@cached('words')
def words():
    """ref3 -> dict(surface, s, a, w, root, lemma, pos, measure, voice, aspect, feats, stem, prefixes, suffixes)."""
    c = qac()
    out = {}
    for (qref, wref, s, a, w, m, surf, stem, lem, root, pos, role, feats, aspect, mood, voice, measure) in c.execute(
            'select qac_ref,qac_word_ref,surah,ayah,word_index,morpheme_index,surface_ar,stem_ar,lemma_ar,root_ar,pos,'
            'morpheme_role,morph_features,aspect,mood,voice,measure from qac_morphemes order by surah,ayah,word_index,'
            'morpheme_index'):
        d = out.get(wref)
        if d is None:
            d = out[wref] = dict(ref=wref, s=s, a=a, w=w, surface='', root='', lemma='', pos='', measure='', voice='',
                                 aspect='', feats='', stem='', prefixes=[], suffixes=[], morphemes=[])
        d['surface'] += surf
        d['morphemes'].append(qref)
        if role == 'STEM':
            if not d['pos'] or (root and not d['root']):
                d.update(root=nroot(root), lemma=lem, pos=pos, measure=measure, voice=voice, aspect=aspect,
                         feats=feats, stem=stem)
        elif role == 'PREFIX':
            d['prefixes'].append((pos, surf, feats))
        else:
            d['suffixes'].append((pos, surf, feats))
    return out


@functools.lru_cache(None)
def ayah_words():
    by = collections.defaultdict(list)
    for r, d in words().items():
        by[(d['s'], d['a'])].append(r)
    for k in by:
        by[k].sort(key=lambda r: words()[r]['w'])
    return dict(by)


@functools.lru_cache(None)
def morph_word():
    """qac morpheme ref -> word ref."""
    return {m: w for w, d in words().items() for m in d['morphemes']}


# ------------------------------------------------------------------------------------------- grammar joins to QAC
@cached('unit2word')
def unit2word():
    """attachment-corpus unit id (q:S:A:wid) -> sorted QAC word refs it covers (via the reviewed bridge)."""
    b = bridge()
    g2m = collections.defaultdict(list)
    for g, m in b.execute('select grammar_ref, qac_morpheme_ref from grammar_qac_edges'):
        g2m[g].append(m)
    s2m = collections.defaultdict(list)
    for s, m in b.execute('select masaq_segment_ref, qac_morpheme_ref from masaq_qac_paths where accepted=1'):
        s2m[s].append(m)
    mw = {}
    for m, w in b.execute('select qac_morpheme_ref, qac_word_ref from qac_morphemes'):
        mw[m] = w
    out = {}
    for u, ns, t in b.execute('select attachment_unit_ref, target_namespace, target_ref from attachment_unit_resolutions'):
        ms = g2m.get(t, []) if ns == 'grammar-unit' else s2m.get(t, [])
        ws = sorted({mw[m] for m in ms if m in mw})
        if ws:
            out[u] = ws
    return out


@cached('endpoints')
def endpoints():
    """(attachment_id, endpoint_role) -> list of QAC morpheme refs."""
    b = bridge()
    out = collections.defaultdict(list)
    for aid, role, m in b.execute('select attachment_id, endpoint_role, qac_morpheme_ref from attachment_endpoint_qac_edges'):
        out[(aid, role)].append(m)
    return dict(out)


def _w_of(aid, role, unit, ep, u2w, mw):
    ms = ep.get((aid, role))
    if ms:
        ws = sorted({mw[m] for m in ms if m in mw})
        if ws:
            return ws
    return u2w.get(unit, [])


@cached('links')
def links():
    """ref3 -> list of grammar relations touching the word:
       dict(rel, role ('head'|'dependent'), other (ref3 list), prep (prep_base), prep_w (ref3 list), obj_type,
            status, part_self, part_other)."""
    ep, u2w, mw = endpoints(), unit2word(), morph_word()
    out = collections.defaultdict(list)
    with open(f'{QD}/grammar/attachments/attachments.tsv', encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            aid = r['unit_id']
            dw = _w_of(aid, 'dependent', r['dep_unit_id'], ep, u2w, mw)
            hw = _w_of(aid, 'head', r['head_unit_id'], ep, u2w, mw)
            pw = _w_of(aid, 'preposition', r['prep_unit_id'], ep, u2w, mw) if r['prep_unit_id'] else []
            base = dict(rel=r['relation'], prep=(r['prep_base'] or '').replace('ـ', ''), prep_w=pw,
                        obj_type=r['obj_type'], status=r['status'], conf=r['confidence'],
                        dep_root=nroot(r['dep_root_norm']), head_root=nroot(r['head_root_norm']),
                        dep_surface=r['dep_surface'], head_surface=r['head_surface'])
            for w in hw:
                out[w].append(dict(base, role='head', other=dw, part_self=r['head_part'], part_other=r['dep_part']))
            for w in dw:
                out[w].append(dict(base, role='dependent', other=hw, part_self=r['dep_part'], part_other=r['head_part']))
    return dict(out)


@cached('frames')
def frames():
    """ref3 (verb) -> verb_instances frame: obj_status, object roots, preps, prep object roots, object wids."""
    u2w = unit2word()
    out = {}
    with open(f'{QD}/grammar/attachments/verb_instances.tsv', encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            for w in u2w.get(r['word_unit_id'], []):
                out[w] = dict(obj=r['frame_obj_status'], obj_roots=[nroot(x) for x in r['object_roots'].split(';') if x],
                              preps=[x.replace('ـ', '') for x in r['preps'].split(';') if x],
                              prep_roots=[nroot(x) for x in r['prep_object_roots'].split(';') if x],
                              sig=r['frame_signature'], grammar=r['grammar'])
    return out


@cached('antecedents')
def antecedents():
    """ref3 carrying a pronoun -> list of (part, antecedent ref3 list, antecedent_text)."""
    u2w = unit2word()
    out = collections.defaultdict(list)
    with open(f'{QD}/grammar/attachments/cross_references.tsv', encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['ref_type'] != 'pronoun_antecedent':
                continue
            ws = u2w.get(r['word_unit_id'], [])
            anc = []
            if r['antecedent_word_unit_id']:
                anc = u2w.get(r['antecedent_word_unit_id'], [])
            for w in ws:
                out[w].append((r['part'], anc, r['antecedent_text']))
    return dict(out)


# -------------------------------------------------------------------------------------------------- dictionary
@cached('dictionary')
def dictionary():
    """branches: ref -> dict(root_id, bid, root, kind, note, image, what, what_not, phrase, gloss, sources);
       occ: root_id -> list of ref3 (QAC word refs listed by the entry); root_of: root_id -> root string."""
    br, occ, root_of = {}, {}, {}
    q = words()
    for f in sorted(glob.glob(f'{QD}/dictionary/tr/root_*_entry.json')):
        d = json.load(open(f, encoding='utf-8'))
        refs = []
        for o in d['occurrence_evidence']['occurrences']:
            if o['qac_word_ref'] not in refs:
                refs.append(o['qac_word_ref'])
        ids = os.path.basename(f).replace('_entry.json', '').split('--')
        for b in d['branches']:
            rid, bid = b['branch_ref'].split('/')
            rt = ''
            br[b['branch_ref']] = dict(
                ref=b['branch_ref'], root_id=rid, bid=bid, envelope=os.path.basename(f),
                kind=b['lexicalization_scope']['branch_kind'], note=b['lexicalization_scope']['note'],
                image=b.get('branch_image_ar', ''), what=b.get('what_is_ar', ''), what_not=b.get('what_is_not_ar', ''),
                phrase=b.get('source_phrase_ar', ''), gloss=(b.get('concept_gloss') or {}).get('text', ''),
                sources=b.get('sources', []))
        # root string per root id: from the occurrences' QAC roots (most common)
        cnt = collections.Counter(q[r]['root'] for r in refs if r in q and q[r]['root'])
        for rid in ids:
            occ.setdefault(rid, [])
        # merged envelopes list one occurrence set; keep it for each id and let the root string decide
        for rid in ids:
            occ[rid] = refs
            root_of[rid] = cnt.most_common(1)[0][0] if cnt else ''
    # furuq root_norm is the authority for the root string when present
    c = sqlite3.connect(f'file:{P}/dictionary/data/working/furuq_v4.sqlite?mode=ro', uri=True)
    for rid, rn in c.execute('select root_id, root_norm from roots'):
        if rid in root_of:
            root_of[rid] = nroot(rn)
    for v in br.values():
        v['root'] = root_of.get(v['root_id'], '')
    return dict(branches=br, occ=occ, root_of=root_of)


@cached('lexunits')
def lexunits():
    """(root_id, Bnnn) -> list of the dictionary's own lexical units (kind, expression_ar, sense_ar)."""
    c = sqlite3.connect(f'file:{P}/dictionary/data/working/furuq_v4.sqlite?mode=ro', uri=True)
    out = collections.defaultdict(list)
    for rid, kind, expr, bids, sense in c.execute(
            "select root_id, unit_kind, expression_ar, branch_ids, sense_ar from lexical_unit_senses "
            "where origin_corpus='quranic'"):
        for b in re.findall(r'B\d+', bids or ''):
            out[(rid, b)].append(dict(kind=kind, expr=expr or '', sense=sense or ''))
    return dict(out)


@functools.lru_cache(None)
def quran_text():
    out = {}
    with open(f'{QD}/text/quran-uthmani.tsv', encoding='utf-8') as f:
        for line in f:
            ref, _, txt = line.rstrip('\n').partition('|')
            if re.fullmatch(r'\d+:\d+', ref.strip()):
                out[ref.strip()] = txt.replace('﻿', '').strip()
    if not out:  # fall back to QAC surfaces
        for (s, a), refs in ayah_words().items():
            out[f'{s}:{a}'] = ' '.join(words()[r]['surface'] for r in refs)
    return out


@functools.lru_cache(None)
def dossier_rows():
    """Evaluation labels: root-dossier activation map rows (plain branch per occurrence)."""
    with open(f'{P}/root-dossier/out/activation_map.tsv', encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


if __name__ == '__main__':
    import time
    t = time.time()
    W = words(); print('qac words', len(W), round(time.time() - t, 1)); t = time.time()
    U = unit2word(); print('units joined', len(U), round(time.time() - t, 1)); t = time.time()
    L = links(); print('words with grammar links', len(L), round(time.time() - t, 1)); t = time.time()
    F = frames(); print('verb frames joined', len(F), round(time.time() - t, 1)); t = time.time()
    A = antecedents(); print('pronoun antecedent rows joined', len(A), round(time.time() - t, 1)); t = time.time()
    D = dictionary(); print('branches', len(D['branches']), 'roots', len(D['occ']), round(time.time() - t, 1))
    LU = lexunits(); print('lexical-unit keys', len(LU))
    print('quran ayat', len(quran_text()))
    rooted = [r for r, d in W.items() if d['root']]
    print('rooted words', len(rooted), 'with >=1 grammar link', sum(1 for r in rooted if r in L),
          'verbs', sum(1 for r in rooted if W[r]['pos'] == 'V'), 'verbs with frame',
          sum(1 for r in rooted if W[r]['pos'] == 'V' and r in F))
