"""branch_kind guard audit of the v5 harvest (the dictionary principle, 2026-09-28).
For every v5 activation of a dictionary branch whose lexicalization_scope.branch_kind == 'collocation':
  - is the carrier an occurrence of the branch's own root (the root word itself is claimed to carry the sense)?
  - is the construction present? Heuristic: collocate roots are the Quranic roots of the content words in the
    branch's early-source phrase (source_phrase_ar) other than the root's own derivatives; the construction counts as
    present if any collocate root occurs in the same ayah (strict) or in the ±2-ayah window (loose).
Also reports the ض ر ب B002 case explicitly. Output: out/kinds.json and a sample for manual checking."""
import json, os, re, glob, collections, random
import lib
from relay import pick_dirs

AR_DIAC = re.compile(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]')
STOP = set('في من على إذا اذا أي اي له به لها بها عن إلى الى ما لا هو هي ذلك هذا هذه التي الذي كل أو او ثم قد لم لن إن ان أن كان يقال قال منه فيه وهو وهي الشيء شيء أصل اصل يدل واحد صحيح ومنه أيضا ايضا'.split())


def norm(w):
    w = AR_DIAC.sub('', w)
    w = w.replace('ٱ', 'ا').replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا').replace('ى', 'ي').replace('ة', 'ه').replace('ؤ', 'و').replace('ئ', 'ي')
    return w


def surface_root_map():
    m = collections.defaultdict(collections.Counter)
    for root, occ in lib.concordance().items():
        for ay, surfs, lems, n in occ:
            for s in surfs.split(';') + lems.split(';'):
                s = norm(s)
                if not s: continue
                m[s][root] += 1
                for pre in ('وال', 'بال', 'فال', 'كال', 'لل', 'ال', 'و', 'ف', 'ب', 'ل'):
                    if s.startswith(pre) and len(s) - len(pre) >= 3:
                        m[s[len(pre):]][root] += 1
    return {k: v.most_common(1)[0][0] for k, v in m.items()}


def radicals(root):
    return [norm(x) for x in root.split()]


def is_self(tok, root):
    r = radicals(root)
    i = 0
    for ch in tok:
        if i < len(r) and ch == r[i]:
            i += 1
    return i == len(r)


def collocates(phrase, root, smap):
    if not phrase: return set()
    ph = re.sub(r'\([^)]*\)', ' ', phrase)
    toks = re.findall(r'[ء-يٱً-ٟ]+', ph)
    out = set()
    for t in toks:
        n = norm(t)
        if len(n) < 3 or n in STOP or is_self(n, root):
            continue
        cands = [n] + [n[len(p):] for p in ('وال', 'بال', 'فال', 'ال', 'و', 'ب', 'ف', 'ل') if n.startswith(p) and len(n) - len(p) >= 3]
        for c in cands:
            if c in smap and smap[c] != root:
                out.add(smap[c]); break
    return out


def ayah_roots():
    ar = collections.defaultdict(set)
    occ_refs = collections.defaultdict(set)  # root -> set of word refs S:A:W
    for root, occ in lib.concordance().items():
        for ay, surfs, lems, n in occ:
            ar[ay].add(root)
    # word-level refs from qac_root_ayah qac_refs
    import csv
    with open(lib.SLM + '/qac_root_ayah.tsv', encoding='utf-8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            for q in row['qac_refs'].split(';'):
                occ_refs[row['root_norm']].add(':'.join(q.split(':')[:3]))
    return ar, occ_refs


def window(ref, k=2):
    s, a = map(int, ref.split(':'))
    return [f'{s}:{x}' for x in range(max(1, a - k), a + k + 1)]


if __name__ == '__main__':
    idx, roots = lib.dict_index()
    rmap = lib.root_ar_map()
    smap = surface_root_map()
    ar, occ_refs = ayah_roots()
    coll = {b: v for b, v in idx.items() if v['kind'] == 'collocation'}
    colloc_roots = {}
    for b, v in coll.items():
        root = rmap.get(b.split('/')[0], '')
        colloc_roots[b] = collocates(v.get('phrase_ar'), root, smap)
    n_with = sum(1 for v in colloc_roots.values() if v)
    dirs = pick_dirs()
    stats = collections.Counter(); samples = []
    per_branch = collections.Counter()
    darb = []
    for ay, d in sorted(dirs.items()):
        ref = ay.replace('_', ':')
        seen = set()
        for l in lib.LANES:
            p = f'{d}/{l}.discovery.json'
            if not os.path.exists(p): continue
            disc = json.load(open(p))
            for f in disc.get('findings', []):
                for a in f.get('branch_activations') or []:
                    if not isinstance(a, dict): continue
                    b = a.get('branch_ref')
                    if b not in coll: continue
                    key = (b,)
                    root = rmap.get(b.split('/')[0], '')
                    carriers = [':'.join(c.split(':')[:3]) for c in a.get('carrier_refs') or []]
                    own_word = any(c in occ_refs.get(root, ()) for c in carriers)
                    cr = colloc_roots.get(b) or set()
                    strict = bool(cr & ar.get(ref, set()))
                    loose = bool(cr & set().union(*[ar.get(w, set()) for w in window(ref)]))
                    stats['activations'] += 1
                    stats[f'own_word={own_word}'] += 1
                    if not cr:
                        stats['no_collocate_extracted'] += 1
                        cls = 'unknown'
                    else:
                        cls = 'present_same_ayah' if strict else ('present_window' if loose else 'absent')
                    stats[cls] += 1
                    stats[f'{cls}|own_word={own_word}'] += 1
                    if (b, ref) not in seen:
                        seen.add((b, ref)); stats['distinct_ayah_branch'] += 1; stats[f'distinct|{cls}'] += 1
                        per_branch[(b, cls)] += 1
                        if cls == 'absent' and own_word:
                            samples.append(dict(ref=ref, branch=b, root=root, gloss=idx[b]['gloss'], note=idx[b]['note'], collocate_roots=sorted(cr), mode=a.get('application_mode'), reading=(a.get('resulting_reading') or '')[:200]))
                    if b.startswith('root_000906/'):
                        darb.append((ref, b, idx[b]['kind'], cls, own_word, a.get('application_mode'), (a.get('resulting_reading') or '')[:160]))
    random.seed(7)
    out = dict(collocation_branches=len(coll), with_extracted_collocates=n_with, stats=dict(stats),
               top_absent=[(b, rmap.get(b.split('/')[0]), idx[b]['gloss'], n) for (b, c), n in per_branch.most_common() if c == 'absent'][:25],
               darb_activations=darb[:40], sample_absent_own_word=random.sample(samples, min(15, len(samples))), n_absent_own_word=len(samples))
    json.dump(out, open(lib.W + '/out/kinds.json', 'w'), ensure_ascii=False, indent=1)
    print(json.dumps({k: out[k] for k in ('collocation_branches', 'with_extracted_collocates', 'stats', 'n_absent_own_word')}, ensure_ascii=False, indent=1))
    for x in out['top_absent']: print(x)
    print('darb', len(darb)); [print(x) for x in darb[:20]]
