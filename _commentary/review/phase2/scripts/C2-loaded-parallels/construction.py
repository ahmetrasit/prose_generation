"""Construction guard (dictionary principle): a collocation-bound branch is activatable only where its construction
is present at the occurrence. Script only.

1. For every branch with branch_kind collocation (and non_bare, as a form scope), extract a construction signature
   from its own early-source phrases (source_phrase_ar + what_is_ar): the words that stand next to the root word
   (content partners -> roots via a Quran surface lexicon; prepositions right after the root word).
2. For every Quranic occurrence of the root, collect its construction context: grammar attachments (dictionary
   occurrence_evidence), roots and stems of words within +-3 tokens, prepositions right after it.
3. present(branch, occurrence) by rule; evaluate against the root-dossier's per-occurrence plain branch (Luna,
   independent) where that branch is collocation-bound.

Outputs: construction_eval.json, construction_index.tsv (every occurrence x collocation branch of its root: present/absent
with the matched partner as evidence).
"""
import sys, re, json, collections
sys.dont_write_bytecode = True
import common as C

PREPS = {'في', 'على', 'عن', 'الى', 'ب', 'ل', 'من', 'بين', 'مع', 'لدى', 'عند'}
GENERIC = {'ء ل ه', 'ش ي ء', 'ق و ل', 'ك و ن', 'ك ل ل', 'ن ف س', 'ء ت ي', 'ج ع ل'}
PROCL = ('وال', 'فال', 'بال', 'كال', 'لل', 'ال', 'و', 'ف', 'ب', 'ل', 'ك')
SUFF = ('هما', 'كما', 'هم', 'هن', 'كم', 'كن', 'نا', 'ها', 'ه', 'ك', 'ي', 'ا', 'ات', 'ون', 'ين', 'ان')


STOPTOK = {'اي', 'يقال', 'قيل', 'يدخل', 'فيه', 'منه', 'ومنه', 'معناه', 'كقولك', 'تقول', 'قولك', 'نحو', 'فلان',
           'فلانا', 'الرجل', 'رجل', 'الشيء', 'شيء', 'كذا', 'كذلك', 'ذلك', 'هذا', 'هذه', 'هو', 'هي', 'الله', 'اذا',
           'اذ', 'قد', 'كل', 'بعض', 'يكون', 'كان', 'قال', 'اصله', 'يقول', 'اذن', 'وهو', 'وهي', 'لله', 'بالله', 'والله',
           'ايضا', 'الا', 'اما', 'اسم', 'الاسم', 'الواحد', 'واحد', 'واحده', 'جمع', 'الجمع', 'فعل', 'مصدر', 'المصدر'}


def key(s):
    s = s.replace('ا', '')
    if s.endswith('وه'):
        s = s[:-2] + 'ه'
    return s


def variants(tok):
    s = C.strip(tok)
    out = {s}
    for p in PROCL:
        if s.startswith(p) and len(s) - len(p) >= 2:
            out.add(s[len(p):])
    for x in list(out):
        for q in SUFF:
            if x.endswith(q) and len(x) - len(q) >= 2:
                out.add(x[:-len(q)])
    return {key(x) for x in out if len(key(x)) >= 2}


_LEX = None


def lexicon():
    """stripped surface variant -> Counter(root), from every Quran word and lemma."""
    global _LEX
    if _LEX is None:
        lex = collections.defaultdict(collections.Counter)
        for ref, ws in C.words().items():
            for w in ws:
                if not w['roots']:
                    continue
                r = w['roots'][0]
                for v in variants(w['surface']):
                    lex[v][r] += 1
                for l in w['lemmas']:
                    for v in variants(l):
                        lex[v][r] += 2
        _LEX = lex
    return _LEX


def tok_root(tok):
    lex = lexicon()
    s = key(C.strip(tok))
    if s in lex:
        return lex[s].most_common(1)[0][0]
    best = None
    for v in sorted(variants(tok), key=len, reverse=True):
        if v in lex and len(v) >= 3:
            best = lex[v].most_common(1)[0][0]
            break
    return best


def strong_letters(root):
    L = [c for c in root.split() if c not in 'ءاوي']
    out = []
    for c in L:
        if not out or out[-1] != c:
            out.append(c)
    return out


def matches_root(tok, root):
    s = C.strip(tok)
    st = strong_letters(root)
    if not st or len(s) > len(root.split()) + 7:
        return False
    i = 0
    last = -1
    for k, ch in enumerate(s):
        if i < len(st) and ch == st[i]:
            if last >= 0 and k - last > 3:
                return False
            last = k
            i += 1
    if i < len(st):
        return False
    return tok_root(tok) in (root, None) or len(st) >= 3


def segments(info):
    txt = (info.get('phr') or '') + ' ؛ ' + (info.get('what') or '')
    txt = re.sub(r'\([^)]*\)', ' ', txt)
    return [s for s in re.split('[؛;]', txt) if s.strip()]


def signature(root, info):
    roots, stems, preps, pbefore = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
    nseg = 0
    for seg in segments(info):
        toks = re.findall(r'[ء-ي]+', C.strip(seg))
        heads = [i for i, t in enumerate(toks) if matches_root(t, root)]
        if not heads:
            continue
        nseg += 1
        sr, ss, sp, sb = set(), set(), set(), set()
        for h in heads:
            for j in range(max(0, h - 3), min(len(toks), h + 4)):
                if j in heads:
                    continue
                t = toks[j]
                if C.strip(t) in STOPTOK:
                    continue
                pt = C.particle_token(t).replace('+P', '')
                if pt in PREPS:
                    if 0 < j - h <= 2:
                        sp.add(pt)
                    elif j - h == -1:
                        sb.add(pt)
                    continue
                if len(C.strip(t)) < 2 or pt in C.PART_BASE.values():
                    continue
                r = tok_root(t)
                if r and r != root and r not in GENERIC:
                    sr.add(r)
                if r and r not in GENERIC and r != root:
                    for v in variants(t):
                        if len(v) >= 3:
                            ss.add(v)
        roots.update(sr); stems.update(ss); preps.update(sp); pbefore.update(sb)
    return dict(nseg=nseg, roots=roots, stems=stems, preps=preps, pbefore=pbefore)


def occ_context(ref3, root):
    s, a, w = ref3.split(':')
    ws = C.words()[f'{s}:{a}']
    idx = [k for k, x in enumerate(ws) if x['w'] == int(w)]
    if not idx:
        return None
    k = idx[0]
    near_roots, near_stems, after_preps, before_preps = set(), set(), set(), set()
    if k > 0:
        pt = C.particle_token(ws[k - 1]['surface']).replace('+P', '')
        if pt in PREPS:
            before_preps.add(pt)
    st0 = C.strip(ws[k]['surface'])
    for pre in ('ب', 'ل', 'ك'):
        if st0.startswith(pre) or st0.startswith('و' + pre) or st0.startswith('ف' + pre):
            before_preps.add(pre)
    for j in range(max(0, k - 1), min(len(ws), k + 4)):
        if j == k:
            continue
        x = ws[j]
        near_roots.update(r for r in x['roots'] if r != root)
        for v in variants(x['surface']):
            if len(v) >= 3:
                near_stems.add(v)
        if 0 < j - k <= 2:
            pt = C.particle_token(x['surface']).replace('+P', '')
            if pt in PREPS:
                after_preps.add(pt)
            # attached preposition on the next word (bi-, li-, ka-)
            st = C.strip(x['surface'])
            if j - k == 1 and st[:1] in ('ب', 'ل') and x['roots']:
                after_preps.add(st[0])
    att_roots, att_preps = set(), set()
    for o in C.trcache()['occ'].get(ref3, []):
        for rel, role, orr, prep, osurf in o['atts']:
            if orr and orr != root:
                att_roots.add(orr)
            if rel == 'prep_complement' and role == 'head' and prep:
                pb = C.particle_token(prep).replace('+P', '').replace('ـ', '')
                att_preps.add(C.strip(prep).replace('ـ', '') if pb not in PREPS else pb)
    return dict(near_roots=near_roots, near_stems=near_stems, after_preps=after_preps,
                att_roots=att_roots, att_preps=att_preps, before_preps=before_preps)


def present(sig, ctx, rule='R3'):
    """Returns (bool, evidence string)."""
    if ctx is None:
        return False, 'no context'
    ev = []
    ctxroots = ctx['near_roots'] | ctx['att_roots']
    fixed = any(n >= 2 for n in sig['roots'].values())
    minc = 2 if (fixed and rule in ('R5', 'R6')) else 1
    hit_r = [r for r, n in sig['roots'].items() if r in ctxroots and n >= minc]
    hit_s = [s for s, n in sig['stems'].items() if s in ctx['near_stems'] and C.strip(s) not in C.PART_BASE and n >= minc]
    content = bool(hit_r or hit_s)
    if hit_r:
        ev.append('partner root ' + ','.join(sorted(hit_r)[:3]))
    elif hit_s:
        ev.append('partner word ' + ','.join(sorted(hit_s)[:3]))
    domp = [p for p, n in sig['preps'].items() if n >= max(2, 0.5 * sig['nseg'])] if sig['nseg'] else []
    anyp = [p for p in sig['preps']]
    cp = ctx['after_preps'] | ctx['att_preps']
    prep_dom = [p for p in domp if p in cp]
    prep_any = [p for p in anyp if p in cp]
    if prep_dom:
        ev.append('preposition ' + ','.join(prep_dom))
    if rule == 'R1':
        ok = content
    elif rule == 'R2':
        ok = bool(prep_dom)
    elif rule == 'R3':
        ok = content or bool(prep_dom)
    elif rule == 'R4':
        ok = content and (bool(prep_any) if anyp else True)
    elif rule in ('R5', 'R6'):
        domb = [p for p, n in sig['pbefore'].items() if n >= max(2, 0.5 * sig['nseg'])] if sig['nseg'] else []
        pb = [p for p in domb if p in ctx['before_preps']]
        if pb:
            ev.append('preposition before ' + ','.join(pb))
        ok = content or ((bool(prep_dom) or bool(pb)) and not fixed)
    else:
        raise ValueError(rule)
    return ok, '; '.join(ev)


def root_occurrences():
    occ = collections.defaultdict(list)
    for ref, ws in C.words().items():
        for x in ws:
            for r in x['roots']:
                occ[r].append(x['ref3'])
    return occ


RULE = 'R5'


def main():
    br = C.trcache()['br']
    r2i, i2r = C.root_ids()
    occ = root_occurrences()
    dos = C.dossier()
    sigs = {}
    kinds_total = collections.Counter()
    for bref, info in br.items():
        kinds_total[info['kind']] += 1
        if info['kind'] not in ('collocation', 'non_bare'):
            continue
        rid = bref.split('/')[0]
        root = i2r.get(rid)
        if not root:
            continue
        sigs[bref] = (root, signature(root, info))
    ext = collections.Counter()
    for bref, (root, sg) in sigs.items():
        k = br[bref]['kind']
        ext[(k, 'has_head')] += sg['nseg'] > 0
        ext[(k, 'has_partner')] += bool(sg['roots'] or sg['stems'])
        ext[(k, 'has_dom_prep')] += bool([p for p, n in sg['preps'].items() if n >= max(2, 0.5 * sg['nseg'])]) if sg['nseg'] else 0
        ext[(k, 'n')] += 1
    # evaluation against dossier labels, for collocation branches of dossier roots
    res = {}
    per_branch = {}
    for rule in ('R1', 'R2', 'R3', 'R4', 'R5'):
        tp = fn = fp = tn = 0
        pb = collections.defaultdict(lambda: [0, 0, 0, 0])
        for bref, (root, sg) in sigs.items():
            if br[bref]['kind'] != 'collocation':
                continue
            if root not in C.dossier_roots():
                continue
            for ref3 in occ.get(root, []):
                d = dos.get(ref3)
                if not d or d['root'] != root:
                    continue
                ctx = occ_context(ref3, root)
                ok, _ = present(sg, ctx, rule)
                if d['b'] == bref:
                    if ok: tp += 1; pb[bref][0] += 1
                    else: fn += 1; pb[bref][1] += 1
                else:
                    if ok: fp += 1; pb[bref][2] += 1
                    else: tn += 1; pb[bref][3] += 1
        res[rule] = dict(tp=tp, fn=fn, fp=fp, tn=tn, recall=round(tp / max(1, tp + fn), 3),
                         false_activation_rate=round(fp / max(1, fp + tn), 3),
                         precision=round(tp / max(1, tp + fp), 3))
        per_branch[rule] = {b: v for b, v in pb.items()}
    # daraba detail under R3
    darab = []
    root = 'ض ر ب'
    for ref3 in occ[root]:
        ctx = occ_context(ref3, root)
        d = dos.get(ref3, {})
        row = [ref3, d.get('b', '')]
        for bref, info in C.branches_of_root(root):
            if info['kind'] != 'collocation':
                continue
            ok, ev = present(sigs[bref][1], ctx, RULE)
            if ok:
                row.append(f"{bref.split('/')[1]}:{ev}")
        darab.append(row)
    # index for all occurrences (R3)
    lines = ['ref3\troot\tbranch\tkind\tpresent\tevidence']
    n_occ_bound = collections.Counter()
    by_root_sigs = collections.defaultdict(list)
    for bref, (root, sg) in sigs.items():
        by_root_sigs[root].append((bref, sg))
    for root, lst in by_root_sigs.items():
        for ref3 in occ.get(root, []):
            ctx = occ_context(ref3, root)
            for bref, sg in lst:
                if br[bref]['kind'] != 'collocation':
                    continue
                ok, ev = present(sg, ctx, RULE)
                n_occ_bound[ok] += 1
                lines.append(f"{ref3}\t{root}\t{bref}\tcollocation\t{int(ok)}\t{ev}")
    open(C.HERE + '/construction_index.tsv', 'w').write('\n'.join(lines) + '\n')
    top = {}
    for rule in (RULE,):
        items = sorted(per_branch[rule].items(), key=lambda x: -(x[1][0] + x[1][1]))
        top = {b: dict(image=br[b]['image'], tp=v[0], fn=v[1], fp=v[2], tn=v[3],
                       sig_roots=dict(sigs[b][1]['roots'].most_common(6)), sig_preps=dict(sigs[b][1]['preps']))
               for b, v in items[:25]}
    out = dict(kinds_total=kinds_total, extraction={f'{k[0]}:{k[1]}': v for k, v in ext.items()}, eval=res,
               per_branch=top, daraba=darab, rule=RULE, index_rows=n_occ_bound)
    json.dump(out, open(C.HERE + '/construction_eval.json', 'w'), ensure_ascii=False, indent=1, default=str)
    print(json.dumps(dict(extraction=out['extraction'], eval=res), ensure_ascii=False, indent=1))
    for b, v in top.items():
        print(b, v['image'], v['tp'], v['fn'], v['fp'], v['tn'], v['sig_roots'], v['sig_preps'])
    for row in darab:
        print('\t'.join(row))


if __name__ == '__main__':
    main()
