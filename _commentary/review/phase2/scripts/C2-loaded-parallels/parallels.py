"""Parallels list (NS6 + al-Biqa'i naẓm) as a Pareto union of lenses, script only.

Lenses (each ranks every other ayah for a focus ayah; same-surah and whole-Quran lists kept apart):
  root    sum of IDF of shared roots (v15's dry ranking)
  lemma   sum of IDF of shared (root, lemma)
  phrase  sum of IDF of shared token bigrams/trigrams (lemma for content words, particle + pronoun normalised:
          ʿalayhinna sabīlan ~ ʿalayhim sabīlan); n-grams made only of particles are ignored
  echo    shared roots whose lemma differs (word-level echo: kaʿbayn ~ al-Kaʿba), IDF-weighted
  loaded  for each root of the focus ayah (2..60 ayat): ayat sharing the occurrence's recurring or echo partners
          (loaded.py), plus the root's dominant-role ayat when the focus occurrence departs from it
  scene   shared v15 Luna scenes (each root's branches' scenes weighted 1/n_branches), IDF over ayat
  textmap quran-slm ayah semantic map, navigation fusion (0.35 E5 + 0.35 Neo + 0.30 char, symmetric RRF)
Union: the top K of every lens, ordered by best rank across lenses, each item with its lens tags and shared words.
Evaluation: recall@k per lens and for the union against recorded parallels (named lists and the refs cited in the
cold-arm and v15 prose), same-surah and whole-Quran.
"""
import sys, json, math, collections, glob, re, csv
sys.dont_write_bytecode = True
import numpy as np
import common as C

LENSES = ['root', 'lemma', 'phrase', 'echo', 'loaded', 'scene', 'textmap']


class Parallels:
    def __init__(self, loaded_model=None):
        self.W = C.words()
        self.refs = C.refs()
        self.N = len(self.refs)
        self.ix = {r: i for i, r in enumerate(self.refs)}
        self.roots = {r: {x for w in ws for x in w['roots']} for r, ws in self.W.items()}
        self.lem = {r: {(w['roots'][0], C.strip(w['lemmas'][0])) for w in ws if w['roots'] and w['lemmas']} for r, ws in self.W.items()}
        self.lem_by_root = {r: collections.defaultdict(set) for r in self.refs}
        for r, ws in self.W.items():
            for w in ws:
                if w['roots'] and w['lemmas']:
                    self.lem_by_root[r][w['roots'][0]].add(C.strip(w['lemmas'][0]))
        self.ngr = {}
        LEMDF = collections.Counter()
        for r, ws in self.W.items():
            for x in {C.word_token(w) for w in ws}:
                LEMDF[x] += 1
        for r, ws in self.W.items():
            toks = [C.word_token(w) for w in ws]
            g = set()
            for n in (2, 3):
                for i in range(len(toks) - n + 1):
                    t = tuple(toks[i:i + n])
                    if any(x.startswith('L:') and LEMDF.get(x, 0) <= 300 for x in t):
                        g.add(t)
            self.ngr[r] = g
        self.df_root = collections.Counter(x for s in self.roots.values() for x in s)
        self.df_lem = collections.Counter(x for s in self.lem.values() for x in s)
        self.df_ngr = collections.Counter(x for s in self.ngr.values() for x in s)
        self.inv_root = collections.defaultdict(set)
        for r, s in self.roots.items():
            for x in s:
                self.inv_root[x].add(r)
        self.inv_ngr = collections.defaultdict(set)
        for r, s in self.ngr.items():
            for x in s:
                self.inv_ngr[x].add(r)
        self._scenes()
        self._textmap()
        self.LM = loaded_model

    def idf(self, df):
        return math.log(self.N / max(1, df))

    def _scenes(self):
        tags = collections.defaultdict(set)
        for f in glob.glob(C.V15 + '/frames/out/*.json'):
            for it in json.load(open(f)).get('items', []):
                root = C.nroot(it['key'].rsplit(' ', 1)[0])
                for fr in it.get('frames', []):
                    tags[root].add((it['key'], fr['frame']))
        root_scene = {}
        for root, s in tags.items():
            nb = len({k for k, _ in s}) or 1
            w = collections.Counter()
            for k, sc in s:
                w[sc] += 1 / nb
            root_scene[root] = w
        self.ayah_scene = {}
        for r, rs in self.roots.items():
            v = collections.Counter()
            for x in rs:
                for sc, wt in root_scene.get(x, {}).items():
                    v[sc] = max(v[sc], wt)
            self.ayah_scene[r] = v
        self.df_scene = collections.Counter(sc for v in self.ayah_scene.values() for sc in v)
        self.inv_scene = collections.defaultdict(set)
        for r, v in self.ayah_scene.items():
            for sc in v:
                self.inv_scene[sc].add(r)

    def _textmap(self):
        D = C.P + '/quran-slm/artifacts/ayah_semantic_map/v1'
        nodes = list(csv.DictReader(open(f'{D}/nodes.tsv', encoding='utf-8'), delimiter='\t'))
        self.tm_key = [n['ayah_ref'] for n in nodes]
        self.tm_ix = {k: i for i, k in enumerate(self.tm_key)}
        n = len(nodes)
        self.tm = {s: np.memmap(f'{D}/{s}_raw_directional_rank.u16le', dtype='<u2', mode='r', shape=(n, n))
                   for s in ('e5', 'neo', 'character')}

    def lens_scores(self, f):
        S = {L: collections.Counter() for L in LENSES}
        why = {L: collections.defaultdict(list) for L in LENSES}
        fr = self.roots[f]
        for x in fr:
            w = self.idf(self.df_root[x])
            for r in self.inv_root[x]:
                if r == f:
                    continue
                S['root'][r] += w
                why['root'][r].append(x)
                # lemma and echo
                fl, cl = self.lem_by_root[f].get(x, set()), self.lem_by_root[r].get(x, set())
                for l in fl & cl:
                    S['lemma'][r] += self.idf(self.df_lem.get((x, l), 1))
                    why['lemma'][r].append(l)
                if fl and cl and not (fl & cl) and self.df_root[x] <= 200:
                    S['echo'][r] += w + max(self.idf(self.df_lem.get((x, a), 1)) + self.idf(self.df_lem.get((x, b), 1))
                                            for a in fl for b in cl) / 2
                    why['echo'][r].append(f"{x}: {'/'.join(sorted(fl))} ~ {'/'.join(sorted(cl))}")
        for g in self.ngr[f]:
            w = self.idf(self.df_ngr[g])
            if self.df_ngr[g] > 60:
                continue
            for r in self.inv_ngr[g]:
                if r != f:
                    S['phrase'][r] += w
                    why['phrase'][r].append(' '.join(t[2:] for t in g))
        fv = self.ayah_scene[f]
        for sc, wf in fv.items():
            w = self.idf(self.df_scene[sc])
            if self.df_scene[sc] > 1500:
                continue
            for r in self.inv_scene[sc]:
                if r != f:
                    S['scene'][r] += w * min(wf, self.ayah_scene[r][sc])
                    why['scene'][r].append(sc)
        a = self.tm_ix[f]
        tot = np.zeros(len(self.tm_key), np.float32)
        for s, wt in (('e5', 0.35), ('neo', 0.35), ('character', 0.30)):
            M = self.tm[s]
            out = np.asarray(M[a, :], dtype=np.float32)
            inn = np.asarray(M[:, a], dtype=np.float32)
            el = out != 0
            v = np.zeros_like(out)
            v[el] = 0.5 * (1 / (10 + out[el]) + 1 / (10 + inn[el]))
            tot += wt * v
        tot[a] = -1
        for j in np.argsort(-tot)[:400]:
            S['textmap'][self.tm_key[j]] = float(tot[j])
        if self.LM is not None:
            for x in fr:
                n = len({r for r, _ in self.LM.occ.get(x, [])})
                if not (2 <= n <= 60):
                    continue
                UA, key = self.LM.unit_for(x, f)
                A = UA or self.LM.analyse(x)
                rep = self.LM.occurrence_report(A, f) if A else None
                if not rep:
                    continue
                wr = self.idf(self.df_root[x])
                for p, rs in list(rep['shared'].items()) + list(rep['echoes'].items()):
                    for r in rs:
                        S['loaded'][r] += wr + self.idf(self.df_root.get(p, 1))
                        why['loaded'][r].append(f'{x} with {p}')
                if A['loaded'] and not rep['in_cover']:
                    wc = sum(self.idf(self.df_root.get(p, 1)) for p in A['cover']) / max(1, len(A['cover']))
                    for r in A['covered']:
                        if r != f:
                            S['loaded'][r] += wr + wc
                            why['loaded'][r].append(f'{x} dominant role ({"+".join(A["cover"])})')
        return S, why

    def ranked(self, f, S, lens, same_surah):
        s = C.surah(f)
        items = [(v, r) for r, v in S[lens].items() if (C.surah(r) == s) == same_surah or not same_surah]
        if same_surah:
            items = [(v, r) for v, r in items if C.surah(r) == s]
        items.sort(key=lambda t: (-t[0], self.ix[t[1]]))
        return [r for _, r in items]

    def union(self, f, S, why, K=10, same_surah=True):
        best = {}
        for L in LENSES:
            for i, r in enumerate(self.ranked(f, S, L, same_surah)[:K]):
                if r not in best or i < best[r][0]:
                    best[r] = (i, best.get(r, (0, []))[1])
                best[r][1].append((L, i + 1))
        order = sorted(best, key=lambda r: (best[r][0], -len(best[r][1]), self.ix[r]))
        return [(r, best[r][1], {L: why[L][r][:4] for L, _ in best[r][1]}) for r in order]


GOLD = {
    '4:34': ['4:3', '4:5', '4:19', '4:36', '4:37', '4:38', '4:81', '4:90', '4:128', '4:129', '4:130', '2:238'],
    '5:6': ['5:8', '5:11', '5:89', '5:91', '5:95', '5:97', '35:10'],
    '18:86': ['15:26', '15:28', '15:33'],
    '18:96': ['15:29', '38:72', '32:9', '3:49', '5:110', '21:91', '66:12', '18:99'],
}
PROSE = {
    '4:34': ['v9/lines/work/4_34/synth/w10-opus-cold/4_34.reading.tr.md', 'v9/lines/work/4_34/synth/w10-opus-cold2/4_34.reading.tr.md',
             'v15/out-nocap/s004/4_34/commentary.tr.md', 'v15/out-nocap/s004/4_34/commentary.tagged.tr.md'],
    '5:6': ['v9/lines/work/5_6/synth/w10-opus-cold/5_6.reading.tr.md', 'v15/out-nocap/s005/5_6/commentary.tr.md',
            'v15/out-nocap/s005/5_6/commentary.tagged.tr.md'],
}


def prose_refs(focus):
    out = set()
    for p in PROSE.get(focus, []):
        try:
            t = open(C.P + '/prose_generation/_commentary/' + p).read()
        except FileNotFoundError:
            continue
        for m in re.finditer(r'(?<![\d:])(\d{1,3}):(\d{1,3})(?:[–-](\d{1,3}))?', t):
            s, a, b = int(m.group(1)), int(m.group(2)), m.group(3)
            if 1 <= s <= 114 and f'{s}:{a}' in C.quran():
                if b and 0 < int(b) - a < 15:
                    out.update(f'{s}:{x}' for x in range(a, int(b) + 1))
                else:
                    out.add(f'{s}:{a}')
    out.discard(focus)
    return sorted(out)


def recall_table(PA, f, gold, ks=(5, 10, 20, 30)):
    S, why = PA.lens_scores(f)
    s = C.surah(f)
    g_same = [g for g in gold if C.surah(g) == s]
    g_all = list(gold)
    res = {}
    for scope, gl, same in (('same_surah', g_same, True), ('whole_quran', g_all, False)):
        if not gl:
            continue
        for L in LENSES:
            rk = PA.ranked(f, S, L, same)
            pos = {r: i + 1 for i, r in enumerate(rk)}
            res[f'{scope}:{L}'] = {f'R@{k}': round(sum(1 for g in gl if pos.get(g, 10**9) <= k) / len(gl), 2) for k in ks}
            res[f'{scope}:{L}']['ranks'] = {g: pos.get(g) for g in gl}
        for K in (5, 10, 20):
            U = [r for r, _, _ in PA.union(f, S, why, K, same)]
            res[f'{scope}:union@K{K}'] = dict(size=len(U), recall=round(sum(1 for g in gl if g in U) / len(gl), 2),
                                              missing=[g for g in gl if g not in U])
    return res


def main():
    from loaded import Model
    LM = Model()
    PA = Parallels(LM)
    out = {}
    def outside(f, gl, w=7):
        s, a = map(int, f.split(':'))
        return [g for g in gl if not (C.surah(g) == s and abs(int(g.split(':')[1]) - a) <= w)]
    for f, gold in GOLD.items():
        out[f'{f}:named'] = recall_table(PA, f, gold)
        og = outside(f, gold)
        if og != gold:
            out[f'{f}:named_outside_window7'] = recall_table(PA, f, og)
        pr = prose_refs(f)
        if pr:
            out[f'{f}:prose'] = recall_table(PA, f, pr)
            out[f'{f}:prose']['gold'] = pr
            op = outside(f, pr)
            out[f'{f}:prose_outside_window7'] = recall_table(PA, f, op)
            out[f'{f}:prose_outside_window7']['gold'] = op
    json.dump(out, open(C.HERE + '/parallels_eval.json', 'w'), ensure_ascii=False, indent=1)
    for k, v in out.items():
        print('==', k)
        for kk, vv in v.items():
            if kk == 'gold':
                print('  gold', len(vv)); continue
            if 'union' in kk:
                print(f'  {kk}: size {vv["size"]} recall {vv["recall"]} missing {vv["missing"][:12]}')
            else:
                print(f'  {kk}: ' + ' '.join(f'{a}={b}' for a, b in vv.items() if a != 'ranks') + ('  ranks ' + str(vv['ranks']) if len(vv['ranks']) <= 12 else ''))


if __name__ == '__main__':
    main()
