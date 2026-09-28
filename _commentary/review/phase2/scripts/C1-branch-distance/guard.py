"""Construction-scope guard (dictionary principle, 2026-09-28).
For every collocation-bound branch, derive its construction signature from the dictionary's own lexical units
(dictionary/data/working/furuq_v4.sqlite lexical_unit_senses: unit_kind='collocation', expression_ar such as
'ضرب في الأرض'), then decide at every Quranic occurrence of the root whether the construction is present, using
the dictionary's aligned grammar attachments (quran-data dictionary/tr occurrence_evidence) and a +-4 word window.
Status per (occurrence, branch): free (bare / mixed / non_bare / unresolved), present_strict, present_window,
absent, unknown (no derivable signature or no aligned attachments).  Read-only."""
import sqlite3, re, collections, json, sys, os
sys.dont_write_bytecode = True
import common as C

PREPS = {'في', 'علي', 'عن', 'من', 'الي', 'مع', 'حتي', 'عند', 'بين', 'فوق', 'تحت', 'لدي', 'دون', 'ب', 'ل', 'ك'}
WILD = {'فلان', 'فلانا', 'فلانه', 'الشيء', 'شيء', 'شيا', 'الشي', 'احد', 'الرجل', 'رجل', 'القوم', 'الانسان', 'كذا',
        'الامر', 'امر', 'ما', 'من', 'له', 'لها', 'به', 'بها', 'عليه', 'عليها', 'منه', 'فيه', 'فيها', 'عنه', 'اليه', 'هو', 'هي'}
PRON = ('هم', 'هن', 'ها', 'ه', 'كم', 'نا', 'ك', 'ي')

def lus():
    c = sqlite3.connect(f'file:{C.P}/dictionary/data/working/furuq_v4.sqlite?mode=ro', uri=True)
    out = collections.defaultdict(list)
    for rid, root, luid, kind, expr, bids, sense in c.execute(
            "select root_id, root_norm, lexical_unit_id, unit_kind, expression_ar, branch_ids, sense_ar from lexical_unit_senses where origin_corpus='quranic'"):
        for b in re.findall(r'B\d+', bids or ''):
            out[(rid, b)].append(dict(luid=luid, kind=kind, expr=expr or '', sense=sense or '', root=C.nroot(root)))
    return dict(out)
LU = C.cached('lus', lus)

def radicals_in(tok, root):
    """token carries the root: its consonant skeleton contains >=2 radicals in order (weak radicals may drop)"""
    rad = [r for r in root.split() if r not in 'اويء']
    rad = rad or root.split()
    t = tok
    pos = 0; hit = 0
    for r in rad:
        j = t.find(r if r != 'ء' else 'ا', pos)
        if j >= 0: hit += 1; pos = j + 1
    return hit >= min(2, len(rad))

LEM2 = collections.defaultdict(set)
import csv as _csv
for _r in _csv.DictReader(open(f'{C.V15}/lemmas.tsv', encoding='utf-8'), delimiter='\t'):
    _f = C.norm(_r['lemma'])
    if _f.startswith('ال'): _f = _f[2:]
    if len(_f) == 2: LEM2[_f].add(C.nroot(_r['root']))

def troots(t, root):
    rs = C.token_roots(t) - {root}
    if not rs:
        for p in ('', 'ال', 'ب', 'ل', 'و'):
            if t.startswith(p) and t[len(p):] in LEM2: rs |= LEM2[t[len(p):]]
            for suf in ('ه', 'ها', 'هم', 'ك'):
                if t.startswith(p) and t.endswith(suf) and t[len(p):-len(suf)] in LEM2: rs |= LEM2[t[len(p):-len(suf)]]
    return rs - {root}

def signature_from_tokens(toks, root, focus=None):
    if focus is None:
        for k, t in enumerate(toks):
            if root in C.token_roots(t) or radicals_in(t, root):
                focus = k; break
    if focus is None: focus = 0
    elems, preps, pending, pre = [], set(), '', set()
    for k, t in enumerate(toks):
        if k == focus: continue
        if t in PREPS:
            if k == focus - 1: pre.add(t)
            pending = t; preps.add(t); continue
        m = re.match(r'^(علي|عن|من|الي|في|ب|ل|ك)(هم|هن|ها|ه|كم|نا|ك|ي)$', t)
        if m:
            preps.add(m.group(1)); pending = ''; continue
        p, t2 = pending, t
        if t[:1] in 'بلك' and len(t) > 3 and not troots(t, root):
            p, t2 = t[:1], t[1:]
        if t2 in WILD or t in WILD:
            pending = ''; continue
        rs = troots(t2, root)
        elems.append((p, frozenset(rs), re.sub(r'^ال', '', t2)))
        pending = ''
    return dict(elems=elems, preps=preps, pre=pre, focus=toks[focus], toks=toks)

def signature(lu):
    toks = C.TOK.findall(C.norm(lu['expr']))
    return signature_from_tokens(toks, lu['root']) if toks else None

def phrase_constructions(i):
    """extra construction variants from the branch's own classical phrases: a token carrying the root followed
    directly by a preposition and a content word (e.g. 'ضرب في سبيل الله')"""
    root = C.ROOTKEY[i]; out = []
    ph = C.TEXT.get(i, ('', '', ''))[2]
    for seg in re.split(r'[؛;]', re.sub(r'\([a-z;_ ]+\)', ' ', ph)):
        toks = C.TOK.findall(C.norm(seg))
        for k in range(len(toks) - 2):
            if radicals_in(toks[k], root) and toks[k + 1] in PREPS - {'ب', 'ل', 'ك'}:
                pr = toks[k + 1]; j = k + 2
                while j < len(toks):
                    t = toks[j]
                    if t not in WILD:
                        out.append(('phrase', f"{toks[k]} {pr} {t}", dict(elems=[(pr, frozenset(troots(t, root)), re.sub(r'^ال', '', t))], preps={pr}, focus=toks[k], toks=[toks[k], pr, t])))
                    # coordinated continuation: 'وفي X'
                    nxt = [x for x in toks[j + 1:j + 4]]
                    m = next((q for q, x in enumerate(nxt) if x == 'و' + pr), None)
                    if m is None: break
                    j = j + 1 + m + 1
    return out

SIG = {}
for key, L in LU.items():
    S = []
    for lu in L:
        if lu['kind'] in ('collocation',):
            sg = signature(lu)
            if sg: S.append((lu['luid'], lu['expr'], sg))
    SIG[key] = S
for i in range(C.N):
    if C.kind_of(i) == 'collocation':
        SIG.setdefault((C.RID[i], C.BID[i]), [])
        SIG[(C.RID[i], C.BID[i])] = SIG[(C.RID[i], C.BID[i])] + phrase_constructions(i)

def surf(w):
    f = C.norm(w['surface'])
    return re.sub(r'^(وال|فال|بال|كال|لل|ال|و|ف|ب|ل|ك)', '', f) if len(f) > 3 else f

def occ_context(qref, rid):
    o = C.OCC.get(qref, {}).get(rid)
    return o

def elem_match_dep(p, rs, tok, dep):
    for dp, dr, dsurf in dep:
        if (rs and dr in rs) or (not rs and tok and tok in dsurf):
            if p in ('ب', 'ل', 'ك'):
                return True                      # prefixed preposition: attachment may or may not record it
            if (not p and not dp) or (p and dp and C.norm(p) == dp):
                return True
    return False

def elem_match_win(p, rs, tok, ay, word):
    for k, w in enumerate(ay):
        if w['ref'] == word['ref'] or abs(w['w'] - word['w']) > 4: continue
        if (rs and set(w['roots']) & rs) or (not rs and tok and tok in surf(w)):
            if not p: return True
            prev = C.norm(ay[k - 1]['surface']) if k > 0 else ''
            if prev == p or C.norm(w['surface']).startswith(p) or C.norm(w['surface']).startswith('و' + p):
                return True
    return False

def status(i, word):
    """construction status of card i at a word occurrence (word dict from C.WORDS)"""
    k = C.kind_of(i)
    if k != 'collocation':
        return 'free', None
    sigs = [x for x in SIG.get((C.RID[i], C.BID[i]), []) if x[2]['elems'] or x[2]['preps'] or x[2].get('pre')]
    if not sigs:
        return 'unknown', 'no derivable construction'
    o = occ_context(word['ref'], C.RID[i])
    ats = o['ats'] if o else []
    dep = [(a[2], a[3], C.norm(a[4])) for a in ats if a[1] == 'head' or a[0] == 'subject']
    depreps = {a[0] for a in dep if a[0]}
    ay = C.BY_AYAH[(word['s'], word['a'])]
    k0 = next((k for k, x in enumerate(ay) if x['ref'] == word['ref']), 0)
    prev = C.norm(ay[k0 - 1]['surface']) if k0 > 0 else ''
    gov = {a[2] for a in ats if a[1] == 'dependent' and a[0] == 'prep_complement' and a[2]} | ({prev} if prev in PREPS else set())
    best = None
    for luid, expr, sg in sigs:
        need = sg['elems']
        pre = sg.get('pre') or set()
        if pre and not (pre & gov):
            continue                                   # the construction's preposition does not govern this word
        if pre and not need:
            return 'present_strict', expr
        if need and all(elem_match_dep(p, rs, tok, dep) for p, rs, tok in need):
            return 'present_strict', expr
        if not need and sg['preps'] and (sg['preps'] & depreps):
            best = best or ('possible_prep_only', expr)
        if need and not best and all(elem_match_win(p, rs, tok, ay, word) for p, rs, tok in need):
            best = ('present_window', expr)
    if best: return best
    if not o:
        return 'unknown', 'no aligned attachments'
    return 'absent', '; '.join(e for _, e, _ in sigs)

def word_branch_status(word):
    """for every card of the word's roots: (card, status, detail)"""
    out = []
    for r in word['roots']:
        for i in C.BY_ROOT.get(r, []):
            st, det = status(i, word)
            out.append((i, st, det))
    return out

if __name__ == '__main__':
    import numpy as np
    coll = [i for i in range(C.N) if C.kind_of(i) == 'collocation']
    withsig = [i for i in coll if any(s[2]['elems'] or s[2]['preps'] for s in SIG.get((C.RID[i], C.BID[i]), []))]
    anylu = [i for i in coll if SIG.get((C.RID[i], C.BID[i]))]
    print('catalog collocation branches', len(coll), 'with >=1 collocation lexical unit', len(anylu), 'with derivable construction signature', len(withsig))
    # status over every Quranic occurrence of roots that have collocation branches
    cnt = collections.Counter(); per_branch = collections.defaultdict(collections.Counter)
    for w in C.WORDS:
        for r in w['roots']:
            for i in C.BY_ROOT.get(r, []):
                if C.kind_of(i) == 'collocation':
                    st, _ = status(i, w); cnt[st] += 1; per_branch[i][st] += 1
    print('occurrence x collocation-branch statuses', dict(cnt), 'total', sum(cnt.values()))
    json.dump({C.DISP[i]: dict(v) for i, v in per_branch.items()}, open(os.path.join(C.HERE, 'guard_status_by_branch.json'), 'w'), ensure_ascii=False, indent=0)
    # hand check: ḍaraba
    print('\n== ض ر ب occurrences')
    for w in C.WORDS:
        if 'ض ر ب' in w['roots']:
            sts = [(C.BID[i], st) for i, st, det in word_branch_status(w) if C.kind_of(i) == 'collocation']
            print(w['ref'], w['surface'], ' '.join(f"{b}:{st.replace('present_', 'P-').replace('absent', 'ABS').replace('unknown', '?')}" for b, st in sts))
    for i in C.BY_ROOT['ض ر ب']:
        print(C.DISP[i], C.kind_of(i), [(e, [(p, sorted(r), t) for p, r, t in sg['elems']], sorted(sg['preps'])) for _, e, sg in SIG.get((C.RID[i], C.BID[i]), [])])
