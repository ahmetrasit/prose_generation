"""Per-ayah harvest sheet: what script discovery hands to synthesis (prototype, script only).

Sections (each item carries its evidence path; the full lists stay one read away in pull files):
  A  the ayah: words with root, lemma, POS
  B  branches of the ayah's roots: every activatable branch with kind, image, one early phrase, Turkish gloss;
     the plain branch here (root-dossier) marked; collocation-bound branches only where their construction is present
     (construction guard), the rest counted and sent to the pull file with the reason
  C  neighbour activation (simple C1): for each non-plain branch of the ayah's roots, the neighbouring words
     (same ayah, +-2 ayat) whose branches cohere with it: quran-slm fused affinity (the measured conditional branch
     selector), the branch's own definition naming the neighbour's root, typed dictionary relations; plus
     definitional cross-references: roots the definition names that occur in the surah, or that the Quran pairs with
     a root of this ayah
  D  Quran-loaded words: role statistics per root / construction (loaded.py), departures, shared and echo partners;
     concordance size of every root; same-root recurrence in the +-7 window
  E  parallels: Pareto union of the lenses (parallels.py), same surah and other surahs
  F  typed contrasts: dictionary antonym / polarity pairs whose partner root is in the window or surah
  G  alternative roots and qira'at
Writes harvest/<S_A>.md and harvest/<S_A>.pull.json; prints sizes.
"""
import sys, json, math, re, os, collections
sys.dont_write_bytecode = True
import numpy as np
import common as C
import construction as K
from loaded import Model
from parallels import Parallels, LENSES

OUT = os.path.join(C.HERE, 'harvest')
SLM_MAX = 40
KIND = {'mixed_non_bare': 'mixed', 'non_bare': 'non-bare', 'bare': 'bare', 'collocation': 'colloc', 'unresolved': 'unres'}
SLM_DIR = C.P + '/quran-slm/artifacts'


class SLM:
    def __init__(self):
        cat = json.load(open(SLM_DIR + '/corpus_network/catalog.json'))['cards']
        self.N = len(cat)
        self.gi = {(c['source_root_id'], c['branch_id']): c['global_index'] for c in cat}
        mm = lambda p: np.memmap(p, dtype='<u2', mode='r', shape=(self.N, self.N))
        self.E5 = mm(SLM_DIR + '/corpus_network/e5_directional_rank.u16le')
        self.CH = mm(SLM_DIR + '/corpus_network/character_directional_rank.u16le')
        self.NEO = mm(SLM_DIR + '/corpus_ensemble/neoarabert_directional_rank.u16le')
        self._rows = {}

    def idx(self, bref):
        rid, b = bref.split('/')
        return self.gi.get((rid, b))

    def fused_row(self, a):
        if a in self._rows:
            return self._rows[a]
        tot = np.zeros(self.N, np.float32)
        for M, w in ((self.E5, 0.35), (self.NEO, 0.35), (self.CH, 0.30)):
            out = np.asarray(M[a, :], np.float32); inn = np.asarray(M[:, a], np.float32)
            el = out != 0
            v = np.zeros(self.N, np.float32)
            v[el] = 0.5 * (1 / (10 + out[el]) + 1 / (10 + inn[el]))
            tot += w * v
        order = np.argsort(-tot)
        rank = np.empty(self.N, np.int32); rank[order] = np.arange(1, self.N + 1)
        rank[tot <= 0] = self.N
        self._rows[a] = rank
        return rank

    def rank(self, b1, b2):
        a, b = self.idx(b1), self.idx(b2)
        if a is None or b is None:
            return None
        return int(min(self.fused_row(a)[b], self.fused_row(b)[a]))


_CARD = {}


def card_roots(bref, own_root):
    if bref in _CARD:
        return _CARD[bref]
    info = C.trcache()['br'][bref]
    txt = re.sub(r'\([^)]*\)', ' ', ' '.join([info['image'], info['what'], info['phr']]))
    out = set()
    for t in re.findall(r'[ء-ي]+', C.strip(txt)):
        if t in K.STOPTOK or len(t) < 3:
            continue
        r = K.tok_root(t)
        if r and r != own_root and r not in K.GENERIC:
            out.add(r)
    _CARD[bref] = out
    return out


def first_phrase(info, n=1, maxc=90):
    segs = [s.strip() for s in re.split('[؛;]', info['phr']) if s.strip()]
    t = '؛ '.join(segs[:n])
    return t if len(t) <= maxc else t[:maxc] + '…'


class Harvester:
    def __init__(self):
        self.LM = Model()
        self.PA = Parallels(self.LM)
        self.S = SLM()
        self.W = C.words()
        self.refs = C.refs()
        self.pos = {r: i for i, r in enumerate(self.refs)}
        self.dos = C.dossier()
        self.br = C.trcache()['br']
        self.sigs = {}
        r2i, i2r = C.root_ids()
        for bref, info in self.br.items():
            if info['kind'] == 'collocation' and bref.split('/')[0] in i2r:
                self.sigs[bref] = K.signature(i2r[bref.split('/')[0]], info)
        self.root_ayat = collections.defaultdict(set)
        for ref, ws in self.W.items():
            for w in ws:
                for x in w['roots']:
                    self.root_ayat[x].add(ref)
        sys.path.insert(0, C.P + '/prose_generation/_commentary/v15')
        import lib as V15LIB  # read-only loaders
        self.v15 = V15LIB

    def window(self, ref, k):
        i = self.pos[ref]
        s = C.surah(ref)
        return [self.refs[j] for j in range(max(0, i - k), min(len(self.refs), i + k + 1))
                if C.surah(self.refs[j]) == s and j != i]

    def surah_refs(self, ref):
        s = C.surah(ref)
        return [r for r in self.refs if C.surah(r) == s]

    def activatable(self, root, w):
        """[(bref, info, status)] status: plain / active / bound-present(evidence); plus withheld list."""
        act, withheld = [], []
        plain = self.dos.get(w['ref3'], {}).get('b')
        ctx = None
        for bref, info in C.branches_of_root(root):
            if info['kind'] == 'collocation':
                if bref == plain:
                    act.append((bref, info, 'plain; construction per root-dossier'))
                    continue
                if ctx is None:
                    ctx = K.occ_context(w['ref3'], root)
                ok, ev = K.present(self.sigs.get(bref, dict(nseg=0, roots={}, stems={}, preps={}, pbefore={})), ctx, 'R5')
                if ok:
                    act.append((bref, info, f'construction present ({ev})'))
                else:
                    withheld.append((bref, info, 'collocation-bound; construction not found here'))
            else:
                act.append((bref, info, 'plain' if bref == plain else ''))
        return act, withheld, plain

    def sheet(self, ref):
        L, pull = [], {}
        s = C.surah(ref)
        ws = self.W[ref]
        L.append(f'# Harvest sheet {ref}')
        L.append(C.quran()[ref])
        L.append('')
        L.append('## A. Words (QAC)')
        L.append(' '.join(f"{w['w']}:{w['surface']}[{'/'.join(w['roots']) or '-'}]" for w in ws))
        # ---- B branches
        L.append('')
        L.append('## B. Branches of this ayah\'s roots (dict:root Bnnn; kind; early phrase; plain here = root-dossier)')
        focus_branches = []
        withheld_all = []
        seen = set()
        for w in ws:
            for root in w['roots']:
                if root in seen:
                    continue
                seen.add(root)
                act, withheld, plain = self.activatable(root, w)
                withheld_all += [(root, b, why) for b, _, why in withheld]
                n_ay = len(self.root_ayat[root])
                L.append(f"- {root} (word {w['w']} {w['surface']}; {n_ay} ayat in the Quran)")
                for bref, info, st in act:
                    focus_branches.append((root, w, bref, info, st))
                    tag = f" [{st}]" if st else ''
                    L.append(f"  - {bref.split('/')[1]} {KIND.get(info['kind'], info['kind'])}{tag}: {info['image']} «{first_phrase(info, 1, 70)}» {info['gloss']}")
                if withheld:
                    L.append(f"  - withheld here (construction absent; in pull file): {', '.join(b.split('/')[1] + ' ' + i['image'] for b, i, _ in withheld)}")
        pull['withheld_collocation_branches'] = [(r, b, why) for r, b, why in withheld_all]
        # ---- C neighbour activation
        L.append('')
        L.append('## C. Neighbour activation (non-plain branches; neighbours = this ayah and +-2 ayat)')
        neigh = []
        for r2 in [ref] + self.window(ref, 2):
            for w2 in self.W[r2]:
                for root2 in w2['roots']:
                    neigh.append((r2, w2, root2))
        ayah_roots = {x for w in ws for x in w['roots']}
        surah_roots = collections.defaultdict(set)
        for r2 in self.surah_refs(ref):
            for w2 in self.W[r2]:
                for x in w2['roots']:
                    surah_roots[x].add(r2)
        full_c = []
        for root, w, bref, info, st in focus_branches:
            if st.startswith('plain'):
                continue
            cands = []
            names = card_roots(bref, root)
            done = set()
            for r2, w2, root2 in neigh:
                if root2 == root or (root2, r2) in done:
                    continue
                done.add((root2, r2))
                best = None
                for bref2, info2 in C.branches_of_root(root2):
                    if info2['kind'] == 'collocation':
                        continue
                    ev, sc = [], 0.0
                    rk = self.S.rank(bref, bref2)
                    if rk is not None and rk <= SLM_MAX:
                        ev.append(f'slm rank {rk}'); sc += 1 + (SLM_MAX - rk) / SLM_MAX
                    if root2 in names and len(self.root_ayat.get(root2, ())) <= 100:
                        ev.append('definition names ' + root2); sc += 2.5
                    if root in card_roots(bref2, root2) and len(self.root_ayat.get(root, ())) <= 100:
                        ev.append(f'{root2} {bref2.split("/")[1]} definition names {root}'); sc += 2.0
                    rel = [t for n, t in info['nd'] if n == bref2] + [t for n, t in info2['nd'] if n == bref]
                    if rel:
                        ev.append('dict relation ' + rel[0]); sc += 1.5
                    strong = bool(rel) or any(e.startswith(('definition names', f'{root2} ')) for e in ev) or (rk is not None and rk <= SLM_MAX)
                    if sc and strong and (best is None or sc > best[0]):
                        pl = self.dos.get(w2['ref3'], {}).get('b')
                        best = (sc, bref2, info2, ev, pl == bref2)
                if best:
                    sc, bref2, info2, ev, isplain = best
                    dist = 'same ayah' if r2 == ref else r2
                    cands.append((sc, f"{w2['surface']} ({dist}) {root2} {bref2.split('/')[1]} {info2['image']}"
                                      f"{' [plain]' if isplain else ''} ({'; '.join(ev)})", r2 == ref, rk))
            xref = []
            for X in sorted(names, key=lambda x: -C.idf_root(x)):
                if X in ayah_roots:
                    continue
                if X in surah_roots and len(self.root_ayat.get(X, ())) <= 30:
                    xref.append((C.idf_root(X) + 1, f"definition names {X}, which occurs in this surah at {', '.join(sorted(surah_roots[X], key=lambda r: self.pos[r])[:4])}"))
                nX = len(self.root_ayat.get(X, ()))
                here = ayah_roots - {root}
                co = [r3 for r3 in self.root_ayat.get(X, ()) if (self.PA.roots[r3] & here)]
                if co and nX <= 12:
                    pair = {}
                    for r3 in co:
                        for y in self.PA.roots[r3] & here:
                            pair.setdefault(y, []).append(r3)
                    pair = {y: rs for y, rs in pair.items() if len(rs) >= 2 and len(rs) / nX >= 0.5 and len(self.root_ayat.get(y, ())) <= 400}
                    if not pair:
                        continue
                    y, rs = max(pair.items(), key=lambda t: (len(t[1]) / nX, C.idf_root(t[0])))
                    xref.append((C.idf_root(X) + C.idf_root(y) / 2, f"definition names {X}; the Quran pairs {X} with {y} (this ayah) in {len(rs)} of its {nX} ayat: {', '.join(sorted(rs, key=lambda r: self.pos[r])[:4])}"))
            cands.sort(key=lambda t: -t[0])
            xref.sort(key=lambda t: -t[0])
            # push: same-ayah partners with any strong signal; +-2 ayat partners only with score >= 2 or slm rank <= 10
            push_c = [c for c in cands if c[2] or c[0] >= 2.0 or (c[3] is not None and c[3] <= 10)]
            full_c.append(dict(branch=bref, candidates=[c[1] for c in cands], xref=[x for _, x in xref]))
            if push_c or xref:
                items = [c[1] for c in push_c[:3]] + [x for _, x in xref[:2]]
                more = max(0, len(cands) - min(3, len(push_c))) + max(0, len(xref) - 2)
                L.append(f"- {root} {bref.split('/')[1]} {info['image']} ← " + ' | '.join(items) + (f' (+{more} in pull)' if more else ''))
        pull['neighbour_activation'] = full_c
        # ---- D loaded words
        L.append('')
        L.append('## D. Quran-loaded words (role statistics per root / construction; loaded.py)')
        win7 = set(self.window(ref, 7))
        for root in sorted(ayah_roots, key=lambda x: len(self.root_ayat[x])):
            n = len(self.root_ayat[root])
            if n < 2 or n > 60:
                continue
            RA = self.LM.analyse(root)
            UA, key = self.LM.unit_for(root, ref)
            A = UA or RA
            rep = self.LM.occurrence_report(A, ref, RA, key)
            same_win = sorted(win7 & self.root_ayat[root], key=lambda r: self.pos[r])
            parts = [f"{root}: {n} ayat"]
            if key != 'bare/other':
                parts.append(f"construction {key}")
            if A and A['cover']:
                parts.append('dominant role: ' + '; '.join(f"{x} {len(A['rec'][x]['refs'])} ({', '.join(A['rec'][x]['refs'][:6])})" for x in A['cover'])
                             + f" = {A['share']} of {A['n']}")
            if rep:
                if rep['departure']:
                    parts.append('THIS OCCURRENCE DEPARTS: ' + ', '.join(rep['departure']) + f" (lemma {rep['lemma'][0]} {rep['lemma'][1]})")
                elif A['loaded']:
                    parts.append('this occurrence is inside the dominant role')
                if rep['shared']:
                    parts.append('shares ' + '; '.join(f"{x} with {', '.join(v[:4])}" for x, v in list(rep['shared'].items())[:3]))
                if rep['echoes']:
                    parts.append('echo ' + '; '.join(f"{x} with {', '.join(v[:4])}" for x, v in list(rep['echoes'].items())[:3]))
            if same_win:
                parts.append('same root in +-7: ' + ', '.join(same_win[:6]))
            if (A and A['loaded']) or same_win or (rep and (rep['shared'] or rep['echoes'])):
                L.append('- ' + ' | '.join(parts))
        # ---- E parallels
        L.append('')
        L.append('## E. Parallels (Pareto union of lenses, top 10 per lens; lens:rank; shared words)')
        Ssc, why = self.PA.lens_scores(ref)
        pull['parallels'] = {}
        for label, same in (('same surah', True), ('other surahs', False)):
            U = self.PA.union(ref, Ssc, why, 10, same)
            if not same:
                U = [u for u in U if C.surah(u[0]) != s]
            pull['parallels'][label] = [(r, tags) for r, tags, _ in U]
            L.append(f"### {label} ({len(U)})")
            for r, tags, wy in U:
                w_short = '; '.join(f"{Ln}: {', '.join(map(str, v[:3]))}" for Ln, v in wy.items() if v and Ln not in ('textmap',))
                L.append(f"- {r} [{' '.join(f'{a}:{b}' for a, b in tags)}] {w_short}")
        # ---- F contrasts
        L.append('')
        L.append('## F. Typed contrasts (dictionary antonym / polarity pairs present in the window or surah)')
        wins = set(self.window(ref, 7)) | {ref}
        r2i, i2r = C.root_ids()
        seen_c = set()
        for root, w, bref, info, st in focus_branches:
            for nref, rt in info['nd']:
                if rt not in ('antonym', 'polarity_pair'):
                    continue
                nroot = i2r.get(nref.split('/')[0])
                if not nroot or (bref, nref) in seen_c:
                    continue
                seen_c.add((bref, nref))
                inwin = sorted(wins & self.root_ayat.get(nroot, set()), key=lambda r: self.pos[r])
                insur = sorted(surah_roots.get(nroot, set()), key=lambda r: self.pos[r])
                if inwin or insur:
                    nb = self.br.get(nref, {})
                    L.append(f"- {root} {bref.split('/')[1]} {info['image']} ↔ {nroot} {nref.split('/')[1]} {nb.get('image', '')} ({rt}): "
                             f"{'window ' + ', '.join(inwin[:4]) if inwin else 'surah ' + ', '.join(insur[:4])}")
        # ---- G alternatives
        L.append('')
        L.append('## G. Alternative roots and qira\'at')
        for w in ws:
            root = w['roots'][0] if w['roots'] else ''
            vs = C.qiraat().get(w['ref3'], [])
            alts = self.v15.alternative_roots(w['ref3'], root, w['lemmas'][0] if w['lemmas'] else '', w['surface']) if root else []
            # weak-letter exchange (hamza / waw / ya), not in v15's table
            canon = C.strip(w['surface'])
            for v in vs:
                var = C.strip(v['qiraat_arabic'])
                if root and 'ء' in root.split():
                    for M in ('ي', 'و'):
                        cand = root.replace('ء', M)
                        if M in var and var.count(M) > canon.count(M) and cand in C.root_ids()[0] and cand not in [a for a, _ in alts]:
                            alts.append((cand, f"reading {v['qiraat_transliteration']} ({v['qiraat_reader_set']}), hamza/{M} exchange"))
            for v in vs:
                if v['qiraat_reader_set'] != 'canonical':
                    L.append(f"- {w['surface']} ({w['ref3']}): {v['qiraat_arabic']} {v['qiraat_transliteration']} ({v['qiraat_reader_set']}) — {v['qiraat_note'][:160]}")
            for a, why2 in alts:
                L.append(f"- {w['surface']}: alternative root {a} — {why2}")
        L.append('')
        L.append(f'Pull: harvest/{ref.replace(":", "_")}.pull.json (withheld branches, all neighbour candidates, full lens lists); '
                 f'v15/data/branches.tsv and dictionary tr entries (full branch index); construction_index.tsv; loaded_flags.tsv.')
        return '\n'.join(L), pull


def main(refs):
    os.makedirs(OUT, exist_ok=True)
    H = Harvester()
    sizes = {}
    for ref in refs:
        txt, pull = H.sheet(ref)
        base = os.path.join(OUT, ref.replace(':', '_'))
        open(base + '.md', 'w').write(txt + '\n')
        json.dump(pull, open(base + '.pull.json', 'w'), ensure_ascii=False, indent=1)
        sec = {}
        cur = None
        for line in txt.split('\n'):
            if line.startswith('## '):
                cur = line[3:5].strip('. ')
                sec[cur] = 0
            if cur:
                sec[cur] += len(line) + 1
        sizes[ref] = dict(chars=len(txt), sections=sec, words=len(H.W[ref]))
        print(ref, sizes[ref])
    json.dump(sizes, open(os.path.join(OUT, 'sizes.json'), 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1:] or ['1:6', '4:34', '5:6', '18:86', '18:96', '29:38', '2:282', '2:255'])
