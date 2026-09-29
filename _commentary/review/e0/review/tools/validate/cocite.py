"""Early-source co-citation index (six early sources only; no late lexicon, no Majaz).

For every dictionary root, find the ayat its early entries cite and file each citation under a dictionary branch.
  1. explicit references: Mufradat '[surah/ n]', Tahdhib '( surah : n )' (any source using these patterns is read)
  2. implicit quotations: runs of >= 3 consecutive tokens matching a single ayah (or at most 2 ayat) by consonant
     skeleton (Sihah, Ayn, Jamhara, Maqayis and Tahdhib quote without references)
  3. quoted words: the ayah word positions the quotation reproduces (LCS alignment of the quote with the ayah)
  4. branch attribution (positional): each branch's source-phrase clauses tagged with this source are located in the
     entry text; a citation belongs to the branch whose clause is the nearest one before it (single-branch roots:
     that branch). Attribution is a heuristic; its distance in tokens is kept.
A citation counts as verified when the cited ayah contains a word of the entry's root.
Writes cache/cocite.pkl and cocite_stats.json. Read-only on every source."""
import re, json, os, sys, collections, pickle
sys.dont_write_bytecode = True
import lib

SURAH_TS = f'{lib.P}/quran-note-app/src/data/surahNames.ts'


def surah_names():
    txt = open(SURAH_TS, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'id:\s*(\d+),\s*name:\s*"[^"]*",\s*nameAr:\s*"([^"]+)"', txt):
        out[int(m.group(1))] = m.group(2)
    return out


def nname(x):
    x = re.sub(r'ms\d+|PageV\d+P\d+|[#|~]|سورة', ' ', x)
    x = lib.norm(x)
    x = re.sub(r'\s+', ' ', x).strip()
    x = re.sub(r'^ال', '', x.replace(' ال', ' '))
    return x.replace('ا', '').replace(' ', '')


NAMES = surah_names()
ALIAS = {'الدهر': 76, 'عم': 78, 'النبإ': 78, 'سبإ': 34, 'طاه': 20, 'الرحمان': 55, 'ص': 38, 'ق': 50, 'والقلم': 68,
         'القصس': 28, 'المؤمنين': 23, 'البقر': 2, 'لبقرة': 2, 'المطفيين': 83, 'الإنشقاق': 84, 'بني إسرائيل': 17,
         'المؤمن': 40, 'حم السجدة': 41, 'براءة': 9, 'الملائكة': 35, 'التطفيف': 83, 'القتال': 47, 'تبارك': 67,
         'ن': 68, 'سأل': 70, 'الم نشرح': 94, 'الأعرا ف': 7}
NAME2S = {}
for s, n in NAMES.items():
    NAME2S[nname(n)] = s
for n, s in ALIAS.items():
    NAME2S[nname(n)] = s


def resolve(name):
    return NAME2S.get(nname(name))


# ------------------------------------------------------------------ Quran skeleton tokens
QTOK = {k: [lib.skel(w['surface']) for w in ws] for k, ws in lib.BY_AYAH.items()}
QROOTS = {k: [set(w['roots']) for w in ws] for k, ws in lib.BY_AYAH.items()}
GRAM = collections.defaultdict(set)
for k, toks in QTOK.items():
    for i in range(len(toks) - 2):
        GRAM[tuple(toks[i:i + 3])].add((k, i))

CLEAN = re.compile(r'~~|PageV\d+P\d+|ms\d+|@\d+@')
TOKRE = re.compile(r'[ء-يً-ْٰ]+|[\[\]\(\)\{\}#|/:،.]|\d+')


def tokenize(text):
    """tokens with char offsets over the cleaned text"""
    text = CLEAN.sub(' ', text)
    return text, [(m.group(0), m.start()) for m in TOKRE.finditer(text)]


def lcs_positions(qs, ayah_toks):
    """ayah word positions matched by an order-preserving alignment of quote skeletons qs"""
    n, m = len(qs), len(ayah_toks)
    if not n or not m:
        return []
    L = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            L[i][j] = L[i + 1][j + 1] + 1 if qs[i] and qs[i] == ayah_toks[j] else max(L[i + 1][j], L[i][j + 1])
    i = j = 0; out = []
    while i < n and j < m:
        if qs[i] and qs[i] == ayah_toks[j]:
            out.append(j); i += 1; j += 1
        elif L[i + 1][j] >= L[i][j + 1]:
            i += 1
        else:
            j += 1
    return out


REF_M = re.compile(r'\[\s*([^\]\[/]{1,40}?)\s*/\s*(\d+)\s*\]')
REF_T = re.compile(r'\(\s*([^():\d]{1,40}?)\s*:\s*(\d+)\s*\)')


def citations_in(text):
    """[(ayah, char_pos, quoted_positions, explicit)]"""
    text, toks = tokenize(text)
    words = [(i, t, p) for i, (t, p) in enumerate(toks) if re.match(r'[ء-ي]', t)]
    wsk = [lib.skel(t) for _, t, _ in words]
    wpos = [p for _, _, p in words]
    out = []
    covered = set()
    # explicit references
    refs = []
    for rx in (REF_M, REF_T):
        for m in rx.finditer(text):
            s = resolve(m.group(1))
            if not s:
                continue
            a = int(m.group(2))
            if (s, a) not in QTOK:
                continue
            refs.append((m.start(), m.end(), (s, a)))
    refs.sort()
    prev_end = 0
    for st, en, k in refs:
        # quote = words between the previous reference (or 25 words back) and this reference
        idx = [j for j, p in enumerate(wpos) if prev_end <= p < st]
        idx = idx[-25:]
        qs = [wsk[j] for j in idx]
        pos = lcs_positions(qs, QTOK[k])
        matched = [idx[x] for x in range(len(idx))]  # word indices of the quote window
        for j in idx:
            covered.add(j)
        out.append((k, st, pos, True))
        prev_end = en
    # implicit quotations (runs >= 3 words over one or two ayat)
    i = 0
    n = len(wsk)
    while i < n - 2:
        if i in covered:
            i += 1; continue
        hits = GRAM.get(tuple(wsk[i:i + 3]))
        if not hits:
            i += 1; continue
        best = {}
        for k, j in hits:
            L = 3
            while i + L < n and j + L < len(QTOK[k]) and wsk[i + L] == QTOK[k][j + L]:
                L += 1
            best.setdefault(L, []).append((k, j))
        L = max(best)
        cands = {k for k, j in best[L]}
        if len(cands) <= 2 and not all(len(wsk[x]) <= 2 for x in range(i, i + L)):
            for k, j in best[L]:
                out.append((k, wpos[i], list(range(j, j + L)), False))
        i += L
    return out


def branch_clauses(rid):
    """{source: [(bid, clause_skeleton_tokens)]} from each branch's source phrase (tagged clauses)"""
    out = collections.defaultdict(list)
    for k in lib.RID_BR.get(rid, []):
        ph = lib.BR[k]['phrase']
        for cl in re.split('؛', ph):
            m = re.search(r'\(([a-z;_ ]+)\)\s*$', cl.strip())
            if not m:
                continue
            srcs = [x.strip() for x in m.group(1).split(';')]
            body = cl[:m.start()] if m else cl
            sk = [lib.skel(t) for t in lib.TOK.findall(body)]
            sk = [t for t in sk if t]
            for s in srcs:
                if s in lib.EARLY and sk:
                    out[s].append((k[1], sk))
    return out


def gram_index(wsk):
    g3, g2 = {}, {}
    for i in range(len(wsk)):
        if i + 3 <= len(wsk):
            g3.setdefault(tuple(wsk[i:i + 3]), i)
        if i + 2 <= len(wsk):
            g2.setdefault(tuple(wsk[i:i + 2]), i)
    return g3, g2


def locate(clause, gi):
    """earliest word index in the entry where a 3-word (else 2-word with a long word) run of the clause occurs"""
    g3, g2 = gi
    hits = [g3[tuple(clause[a:a + 3])] for a in range(len(clause) - 2) if tuple(clause[a:a + 3]) in g3]
    if hits:
        return min(hits)
    hits = [g2[tuple(clause[a:a + 2])] for a in range(len(clause) - 1)
            if tuple(clause[a:a + 2]) in g2 and max(len(x) for x in clause[a:a + 2]) >= 4]
    return min(hits) if hits else None


def strip_forms(sk):
    """skeleton variants of a word with common clitics removed"""
    out = {sk}
    for p in ('ول', 'فل', 'بل', 'كل', 'لل', 'ل', 'و', 'ف', 'ب', 'ك', 'س'):
        if sk.startswith(p) and len(sk) - len(p) >= 3:
            out.add(sk[len(p):])
    for x in list(out):
        for s in ('هم', 'هن', 'كم', 'ها', 'نا', 'ه', 'ك', 'ي'):
            if x.endswith(s) and len(x) - len(s) >= 3:
                out.add(x[:-len(s)])
    return out


def branch_forms(rid):
    """{bid: set of skeleton forms appearing in the branch's image / what_is / source phrase}"""
    out = {}
    for k in lib.RID_BR.get(rid, []):
        b = lib.BR[k]
        fs = set()
        for t in lib.TOK.findall(b['image'] + ' ' + b['what'] + ' ' + lib.clean_phrase(b['phrase'])):
            fs |= strip_forms(lib.skel(t))
        out[k[1]] = fs
    return out


def build():
    idx = []
    stats = collections.Counter()
    for rid in sorted(lib.RID_BR):
        root = lib.BR[lib.RID_BR[rid][0]]['root']
        texts = lib.load_early_texts(rid)
        clauses = branch_clauses(rid)
        bids = [k[1] for k in lib.RID_BR[rid]]
        bforms = branch_forms(rid)
        for src, raw in texts.items():
            text, toks = tokenize(raw)
            words = [(t, p) for (t, p) in toks if re.match(r'[ء-ي]', t)]
            wsk = [lib.skel(t) for t, _ in words]
            wpos = [p for _, p in words]
            anchors = []
            gi = gram_index(wsk)
            for bid, cl in clauses.get(src, []):
                w = locate(cl, gi)
                if w is not None:
                    anchors.append((wpos[w], bid))
            anchors.sort()
            stats[f'anchors_{src}'] += len(anchors)
            stats[f'clauses_{src}'] += len(clauses.get(src, []))
            for k, cpos, qpos, explicit in citations_in(raw):
                verified = any(root in QROOTS[k][j] for j in range(len(QROOTS[k])))
                method = None
                if len(bids) == 1:
                    bid, dist, method = bids[0], 0, 'single'
                else:
                    before = [(p, b) for p, b in anchors if p <= cpos]
                    pos_bid, dist = (before[-1][1], cpos - before[-1][0]) if before else (None, None)
                    # lexical: the quoted root word's form appears in exactly the texts of some branches
                    rw = [j for j in (qpos or []) if root in QROOTS[k][j]] or \
                         [j for j in range(len(QROOTS[k])) if root in QROOTS[k][j]]
                    qforms = set()
                    for j in rw:
                        qforms |= strip_forms(QTOK[k][j])
                    cand = [b for b in bids if bforms[b] & qforms]
                    if len(cand) == 1:
                        bid, method = cand[0], 'lexical'
                    elif cand and pos_bid in cand:
                        bid, method = pos_bid, 'lexical+position'
                    elif cand:
                        # nearest preceding anchor among the candidates
                        bc = [(p, b) for p, b in anchors if p <= cpos and b in cand]
                        bid, method = (bc[-1][1], 'lexical+position') if bc else (None, None)
                    else:
                        bid, method = pos_bid, ('position' if pos_bid else None)
                idx.append(dict(rid=rid, root=root, src=src, ayah=k, pos=cpos, qpos=qpos, explicit=explicit,
                                verified=verified, bid=bid, dist=dist, method=method))
                stats[f'cit_{src}_{"exp" if explicit else "imp"}'] += 1
                stats[f'ver_{src}'] += verified
    return idx, stats


if __name__ == '__main__':
    idx, stats = build()
    pickle.dump(idx, open(os.path.join(lib.CACHE, 'cocite.pkl'), 'wb'))
    ver = [c for c in idx if c['verified']]
    att = [c for c in ver if c['bid']]
    loci = {(c['rid'], c['ayah']) for c in ver}
    s = dict(citations=len(idx), verified=len(ver), verified_share=round(len(ver) / max(1, len(idx)), 3),
             attributed_of_verified=len(att), attributed_share=round(len(att) / max(1, len(ver)), 3),
             distinct_root_ayah_loci=len(loci), distinct_ayat=len({c['ayah'] for c in ver}),
             by_source={src: dict(explicit=stats[f'cit_{src}_exp'], implicit=stats[f'cit_{src}_imp'],
                                  verified=stats[f'ver_{src}'], clauses=stats[f'clauses_{src}'],
                                  anchors_located=stats[f'anchors_{src}']) for src in lib.EARLY},
             verified_share_explicit=round(sum(c['verified'] for c in idx if c['explicit']) /
                                           max(1, sum(1 for c in idx if c['explicit'])), 3),
             verified_share_implicit=round(sum(c['verified'] for c in idx if not c['explicit']) /
                                           max(1, sum(1 for c in idx if not c['explicit'])), 3))
    s['attribution_method'] = dict(collections.Counter(c['method'] for c in ver))
    json.dump(s, open(os.path.join(lib.HERE, 'cocite_stats.json'), 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(s, ensure_ascii=False, indent=1))
