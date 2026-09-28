"""Quran-loaded word detector (NS5), script only.

Unit of analysis: a root, and inside it each construction group (collocation-bound constructions kept apart from the
bare uses, per the dictionary principle: root-dossier plain branch where it exists, else the construction guard).
Each distinct ayah where the unit occurs gets a context: the roots of that ayah and the grammar-attachment partners
of the occurrence (weight 1) plus the roots of the adjacent ayat (weight 0.5).

  recurring partner: in >=2 of the unit's ayat, binomial tail p < 1e-3 against its ayah frequency, lift >= 3
  echo partner:      same with p < 0.05 (reported, never used to decide)
  dominant role:     greedy cover of the unit's ayat by at most two recurring partners; 'loaded' when n >= 3 and the
                     cover reaches >= 60% of the ayat
  departure (per occurrence of a loaded unit, outside the cover): 'frame' (no recurring partner at all),
                     'form' (lemma/POS differs from the covered uses' dominant lemma), 'plain_branch' (root-dossier
                     branch differs from the covered uses' branch), 'construction' (its construction group differs
                     from the root's dominant one)
Also: clusters = connected components over shared recurring partners (descriptive; scored against the known
partitions with score_dossiers.py).

Outputs (this folder): loaded_roots.tsv, loaded_flags.tsv, loaded_eval.json, dossier_groups/<key>.json.
"""
import sys, json, math, collections, os
sys.dont_write_bytecode = True
import common as C

ALPHA, LOOSE, LIFT, COVER = 1e-3, 0.05, 3.0, 0.6


def binom_tail(k, n, p):
    if k <= 0:
        return 1.0
    p = min(max(p, 1e-12), 1 - 1e-12)
    lp, lq = math.log(p), math.log(1 - p)
    terms = [math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1) + i * lp + (n - i) * lq
             for i in range(k, n + 1)]
    m = max(terms)
    return min(1.0, math.exp(m) * sum(math.exp(t - m) for t in terms))


class Model:
    def __init__(self, with_constructions=True):
        self.W = C.words()
        self.refs = C.refs()
        self.pos = {r: i for i, r in enumerate(self.refs)}
        self.N = len(self.refs)
        self.ayah_roots = {r: {x for w in ws for x in w['roots']} for r, ws in self.W.items()}
        self.df = C.root_df()
        self.occ = collections.defaultdict(list)
        for ref, ws in self.W.items():
            for w in ws:
                for x in w['roots']:
                    self.occ[x].append((ref, w))
        self.tr = C.trcache()['occ']
        self.dos = C.dossier()
        self.br = C.trcache()['br']
        self.ckey = {}
        if with_constructions:
            self._constructions()

    def _constructions(self):
        """ref3 -> construction key (collocation branch ref) where a collocation construction is present."""
        import construction as K
        r2i, i2r = C.root_ids()
        sigs = collections.defaultdict(list)
        for bref, info in self.br.items():
            if info['kind'] == 'collocation' and bref.split('/')[0] in i2r:
                sigs[i2r[bref.split('/')[0]]].append((bref, K.signature(i2r[bref.split('/')[0]], info)))
        for root, lst in sigs.items():
            for ref, w in self.occ.get(root, []):
                d = self.dos.get(w['ref3'])
                if d and d['root'] == root and d['b'].startswith('root_'):
                    if self.br.get(d['b'], {}).get('kind') == 'collocation':
                        self.ckey[(root, w['ref3'])] = d['b']
                    continue
                ctx = K.occ_context(w['ref3'], root)
                for bref, sg in lst:
                    ok, _ = K.present(sg, ctx, 'R5')
                    if ok:
                        self.ckey[(root, w['ref3'])] = bref
                        break

    def construction_of(self, root, ref):
        if not hasattr(self, '_cref'):
            self._cref = {}
            for (rt, ref3), k in self.ckey.items():
                s, a, _ = ref3.split(':')
                self._cref.setdefault((rt, f'{s}:{a}'), k)
        return self._cref.get((root, ref), 'bare/other')

    def neighbours(self, ref):
        i = self.pos[ref]
        return [self.refs[j] for j in (i - 1, i + 1) if 0 <= j < self.N and C.surah(self.refs[j]) == C.surah(ref)]

    def context(self, root, ref, words_here):
        ctx = {}
        for x in self.ayah_roots.get(ref, ()):
            if x != root:
                ctx[x] = 1.0
        for w in words_here:
            for o in self.tr.get(w['ref3'], []):
                for rel, role, orr, prep, osurf in o['atts']:
                    if orr and orr != root:
                        ctx[orr] = 1.0
        for nb in self.neighbours(ref):
            for x in self.ayah_roots.get(nb, ()):
                if x != root and x not in ctx:
                    ctx[x] = 0.5
        return ctx

    def p_ctx(self, x):
        q = self.df.get(x, 1) / self.N
        return 1 - (1 - q) ** 3

    def analyse(self, root, subset=None, label='root'):
        by_ref = collections.defaultdict(list)
        for ref, w in self.occ.get(root, []):
            if subset is None or ref in subset:
                by_ref[ref].append(w)
        refs = sorted(by_ref, key=lambda r: self.pos[r])
        n = len(refs)
        if n < 2:
            return None
        ctxs = {r: self.context(root, r, by_ref[r]) for r in refs}
        k = collections.Counter(x for r in refs for x in ctxs[r])
        rec, loose = {}, {}
        for x, kx in k.items():
            if kx < 2:
                continue
            p = self.p_ctx(x)
            lift = kx / max(n * p, 1e-9)
            if lift < LIFT:
                continue
            pv = binom_tail(kx, n, p)
            if pv < ALPHA:
                rec[x] = dict(k=kx, p=pv, refs=[r for r in refs if x in ctxs[r]])
            elif pv < LOOSE:
                loose[x] = dict(k=kx, p=pv, refs=[r for r in refs if x in ctxs[r]])
        # greedy cover by at most two recurring partners
        covered, cover = set(), []
        for _ in range(2):
            best = max(rec, key=lambda x: (len(set(rec[x]['refs']) - covered), rec[x]['k'], -rec[x]['p']), default=None)
            if best is None or not (set(rec[best]['refs']) - covered):
                break
            cover.append(best)
            covered |= set(rec[best]['refs'])
        share = len(covered) / n
        loaded = n >= 3 and share >= COVER
        lem = collections.Counter((w['lemmas'][0] if w['lemmas'] else '', w['pos']) for r in covered for w in by_ref[r][:1])
        brs = collections.Counter(self.dos[w['ref3']]['b'] for r in covered for w in by_ref[r][:1] if w['ref3'] in self.dos)
        # clusters (descriptive)
        parent = {r: r for r in refs}

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        for x, v in rec.items():
            for a in v['refs'][1:]:
                parent[find(a)] = find(v['refs'][0])
        comps = collections.defaultdict(list)
        for r in refs:
            comps[find(r)].append(r)
        clusters = sorted(comps.values(), key=len, reverse=True)
        return dict(root=root, label=label, n=n, refs=refs, ctxs=ctxs, rec=rec, loose=loose, cover=cover,
                    covered=covered, share=round(share, 3), loaded=loaded,
                    dom_lemma=lem.most_common(1)[0][0] if lem else None,
                    dom_branch=brs.most_common(1)[0][0] if brs else '', clusters=clusters, by_ref=by_ref)

    def unit_for(self, root, ref):
        """The construction group of this occurrence, analysed; falls back to the root."""
        key = self.construction_of(root, ref)
        members = {r for r, w in self.occ.get(root, []) if self.construction_of(root, r) == key}
        A = self.analyse(root, members, label=key) if len(members) >= 3 else None
        return A, key

    def occurrence_report(self, A, ref, root_A=None, key=None):
        if A is None or ref not in A['by_ref']:
            return None
        ctx = A['ctxs'][ref]
        shared = {x: [r for r in A['rec'][x]['refs'] if r != ref] for x in ctx if x in A['rec']}
        echoes = {x: [r for r in A['loose'][x]['refs'] if r != ref] for x in ctx if x in A['loose']}
        ws = A['by_ref'][ref]
        lem = (ws[0]['lemmas'][0] if ws[0]['lemmas'] else '', ws[0]['pos'])
        dep = []
        in_cover = ref in A['covered']
        if A['loaded'] and not in_cover:
            if not shared:
                dep.append('frame')
            if A['dom_lemma'] and lem != A['dom_lemma']:
                dep.append('form')
            b = self.dos.get(ws[0]['ref3'], {}).get('b')
            if b and A['dom_branch'] and b != A['dom_branch']:
                dep.append('plain_branch')
        if root_A is not None and key is not None and root_A['loaded'] and ref not in root_A['covered']:
            if key != 'bare/other':
                dep.append('construction')
        return dict(ref=ref, lemma=lem, in_cover=in_cover, shared=shared, echoes=echoes, departure=dep)


def describe(A, maxrefs=12):
    if A is None:
        return 'n<2'
    s = [f"{A['root']} [{A['label']}]: {A['n']} ayat; loaded={A['loaded']} (cover {A['share']} by "
         f"{' + '.join(A['cover']) or '-'})"]
    for x in A['cover']:
        rs = A['rec'][x]['refs']
        s.append(f"  role partner {x} ({len(rs)}): {', '.join(rs[:maxrefs])}{' …' if len(rs) > maxrefs else ''}")
    other = sorted(((x, v['k']) for x, v in A['rec'].items() if x not in A['cover']), key=lambda t: -t[1])[:8]
    if other:
        s.append('  other recurring partners: ' + ', '.join(f'{x} {k}' for x, k in other))
    out = [r for r in A['refs'] if r not in A['covered']]
    if out:
        s.append(f"  outside the dominant role ({len(out)}): {', '.join(out[:maxrefs])}{' …' if len(out) > maxrefs else ''}")
    return '\n'.join(s)


def to_dossier_groups(A, key):
    groups = []
    for i, c in enumerate(A['clusters']):
        groups.append(dict(id=f'g{i + 1}', label='cluster', ids=[w['ref3'] for r in c for w in A['by_ref'][r]]))
    return dict(key=key, root=A['root'], groups=groups, act=[], complete=True)


def main():
    M = Model()
    os.makedirs(C.HERE + '/dossier_groups', exist_ok=True)
    report = {}
    for root, focus in (('ح م ء', '18:86'), ('ن ف خ', '18:96'), ('ض ر ب', '4:34'), ('س ب ل', '29:38'), ('ك ع ب', '5:6'),
                        ('ر ف ق', '5:6'), ('ق و م', '4:34'), ('ن ش ز', '4:34'), ('ص ل و', '29:45')):
        RA = M.analyse(root)
        UA, key = M.unit_for(root, focus)
        rep = M.occurrence_report(UA or RA, focus, RA, key)
        txt = describe(RA) + ('\n' + describe(UA) if UA and UA['n'] != RA['n'] else '')
        print(txt); print('  focus', focus, 'construction', key, rep); print()
        report[f'{root}@{focus}'] = dict(root=describe(RA), unit=describe(UA) if UA else None, construction=key, focus=rep)
    for key, root in (('حمء', 'ح م ء'), ('نفخ', 'ن ف خ'), ('عرش', 'ع ر ش'), ('ربب', 'ر ب ب'), ('صلو', 'ص ل و')):
        json.dump(to_dossier_groups(M.analyse(root), key), open(f'{C.HERE}/dossier_groups/{key}.json', 'w'),
                  ensure_ascii=False, indent=1)
    rows, flags = [], []
    stats = collections.Counter()
    for root in sorted(M.occ):
        RA = M.analyse(root)
        if RA is None:
            continue
        stats['roots_n>=2'] += 1
        stats['roots_n>=3'] += RA['n'] >= 3
        stats['loaded_root'] += RA['loaded']
        rows.append('\t'.join(map(str, [root, RA['n'], int(RA['loaded']), RA['share'], ' + '.join(RA['cover']),
                                          len(RA['clusters'])])))
        groups = collections.defaultdict(set)
        for r, w in M.occ[root]:
            groups[M.construction_of(root, r)].add(r)
        units = {k: (M.analyse(root, g, k) if len(g) >= 3 else None) for k, g in groups.items()}
        for k, UA in units.items():
            if UA is not None and len(groups) > 1:
                stats['construction_units'] += 1
                stats['loaded_construction_units'] += UA['loaded']
        for ref in RA['refs']:
            k = M.construction_of(root, ref)
            UA = units.get(k) if len(groups) > 1 else RA
            rep = M.occurrence_report(UA or RA, ref, RA, k)
            if rep and rep['departure']:
                stats['flags'] += 1
                A = UA or RA
                flags.append('\t'.join(map(str, [root, ref, A['label'], A['n'], A['share'], ' + '.join(A['cover']),
                                                   ','.join(rep['departure']), ' '.join(rep['lemma']),
                                                   ';'.join(f"{x}:{','.join(v[:4])}" for x, v in rep['shared'].items()),
                                                   ';'.join(f"{x}:{','.join(v[:4])}" for x, v in rep['echoes'].items())])))
    open(C.HERE + '/loaded_roots.tsv', 'w').write('root\tn_ayat\tloaded\tcover_share\tcover_partners\tn_clusters\n' + '\n'.join(rows) + '\n')
    open(C.HERE + '/loaded_flags.tsv', 'w').write('root\tref\tunit\tunit_n\tcover_share\tcover_partners\tdeparture\tlemma_pos\tshared\techoes\n' + '\n'.join(flags) + '\n')
    report['stats'] = stats
    json.dump(report, open(C.HERE + '/loaded_eval.json', 'w'), ensure_ascii=False, indent=1, default=str)
    print(stats)


if __name__ == '__main__':
    main()
