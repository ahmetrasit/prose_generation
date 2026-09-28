"""The branch_kind guard as a script (dictionary principle, 2026-09-28).

For every collocation-bound branch (lexicalization_scope.branch_kind == 'collocation'), derive construction keys
from the early-source phrases (source_phrase_ar): content tokens that stand next to a form of the root in the
phrases. An occurrence of the root LICENSES the branch only if one key occurs within +-4 words of it in the ayah.

This is a heuristic: it is meant to (a) show the guard can be computed before synthesis and in verification, and
(b) measure how much it bites. It is evaluated by hand on ḍaraba (all Quranic occurrences), see __main__.
"""
import re, sys, collections, json
import load

STOP = set(load.norm(w) for w in """في من على عن الى إلى الي ما لا لم لن إذا اذا إذ اذ أي اي أو او و ف ب ل ك ثم قد
هو هي هم هن أن ان إن كان كل بعض شيء الشيء الذي التي وهو وهي به بها له لها منه عنه فيه فيها عليه عليها اذا كذا فلان
عليهم عليكم علينا عليهن لهم لكم لنا لهن منهم منكم بينهم بينكم الرجل رجل قال قولهم يقال ويقال وقيل قيل ذلك هذا هذه تلك معناه أيضا ايضا مثل نحو غير وغيرها وغيره اسم""".split())
SRC_TAG = re.compile(r"\((?:[a-z;]+)\)")


def root_letters(root):
    return [c for c in root.split() if c]


def is_root_form(tok, root):
    """Crude: token contains the root's radicals in order (allowing weak letters to drop)."""
    rl = [load.norm(c) for c in root_letters(root)]
    rl = [c for c in rl if c]
    strong = [c for c in rl if c not in "اوي"]
    i = 0
    for ch in tok:
        if i < len(strong) and ch == strong[i]:
            i += 1
    return i == len(strong) and len(strong) >= 2


def construction_keys(root, source_phrase):
    segs = [SRC_TAG.sub("", s) for s in re.split(r"[؛;]", source_phrase or "")]
    cnt = collections.Counter()
    for s in segs:
        toks = [load.norm(t) for t in re.findall(r"[؀-ۿ]+", s)]
        seen = set()
        for i, t in enumerate(toks):
            if is_root_form(t, root):
                for j in range(max(0, i - 3), min(len(toks), i + 4)):
                    u = toks[j]
                    for pre in ("و", "ف"):
                        if u.startswith(pre) and len(u) > 3 and u[1:] in STOP | {"في"}:
                            u = u[1:]
                    if j == i or u in STOP or len(u) < 3 or is_root_form(u, root):
                        continue
                    # fold the article so الأرض / أرض / الارض match
                    k = u[2:] if u.startswith("ال") and len(u) > 4 else u
                    if k not in seen:
                        seen.add(k)
                        cnt[k] += 1
    return cnt


import functools


@functools.lru_cache(None)
def surface_roots():
    """normalised surface (and the surface with common proclitics / the article stripped) -> Counter of roots."""
    rows, _ = load.words()
    m = {}
    for r in rows:
        root = load.nroot((r["roots"] or "").split("|")[0])
        if not root:
            continue
        t = load.norm(r["surface"])
        cands = {t}
        for pre in ("و", "ف", "ب", "ل", "ك"):
            if t.startswith(pre) and len(t) > 3:
                cands.add(t[1:])
        for c in list(cands):
            if c.startswith("ال") and len(c) > 4:
                cands.add(c[2:])
            if c.startswith("لل") and len(c) > 4:
                cands.add(c[2:])
        for c in cands:
            m.setdefault(c, collections.Counter())[root] += 1
    return m


@functools.lru_cache(None)
def root_ayah_df():
    rows, by = load.words()
    df = collections.Counter()
    for ref, ws in by.items():
        for root in {load.nroot((w["roots"] or "").split("|")[0]) for w in ws}:
            if root:
                df[root] += 1
    return df


STOP_ROOTS = {"ء ل ه", "ق و ل", "ك و ن", "ش ي ء", "ف ل ن"}


def key_roots(row, top=3, max_df=None):
    """Construction keys as ROOTS: content tokens near the root form in the early-source phrases, mapped to Quranic
    roots; very frequent roots (in >2% of ayat, e.g. ء ل ه) are dropped as uninformative.
    Keys seen in >=2 phrase segments are preferred; otherwise the single most frequent one."""
    kind, note, sp, img, what = load.kind_of(row)
    cnt = construction_keys(row["root"], sp or row.get("source_phrase", ""))
    sr = surface_roots()
    df = root_ayah_df()
    n = len(load.quran())
    rc = collections.Counter()
    for tok, c in cnt.items():
        roots = sr.get(tok) or sr.get("ال" + tok)
        if not roots:
            continue
        root = roots.most_common(1)[0][0]
        if root == load.nroot(row["root"]) or root in STOP_ROOTS or (max_df and df[root] / n > max_df):
            continue
        rc[root] += c
    strong = [r for r, c in rc.most_common(top) if c >= 2]
    return strong or [r for r, c in rc.most_common(1)]


def keys_for(row):
    return key_roots(row)


def licensed(ref_word, root, keys, win=4):
    """ref_word = S:A:W. Returns the key root found within +-win words of the occurrence (None if absent).
    win=None means anywhere in the ayah."""
    s, a, w = ref_word.split(":")
    _, by = load.words()
    ws = by[f"{s}:{a}"]
    w = int(w)
    near = {load.nroot((x["roots"] or "").split("|")[0]) for x in ws
            if (win is None or abs(int(x["w"]) - w) <= win) and int(x["w"]) != w}
    for k in keys:
        if k in near:
            return k
    return None


def occurrences(root):
    return load.root_index().get(load.nroot(root), [])


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "ض ر ب"
    rows = load.branches_by_root()[load.nroot(root)]
    colls = [r for r in rows if r["qac_attested"] == "yes" and load.kind_of(r)[0] == "collocation"]
    print(f"{root}: {len(rows)} branches, collocation-bound: {[r['branch'] for r in colls]}")
    keys = {r["branch"]: keys_for(r) for r in colls}
    for b, k in keys.items():
        print(" ", b, "keys:", k)
    occ = occurrences(root)
    print(f"{len(occ)} occurrences")
    q = load.quran()
    for o in occ:
        s, a, w = o.split(":")
        lic = {b: licensed(o, root, k) for b, k in keys.items()}
        lic = {b: v for b, v in lic.items() if v}
        print(o, "licensed:", lic or "-", "|", q[f"{s}:{a}"][:90])


# ---------------------------------------------------------------- v2: preposition patterns + quoted-ayah licence
PARTICLES = {"في", "علي", "عن", "الي", "بين", "من", "له", "لهم", "لكم", "لنا", "به", "بها"}


def skel(t):
    return t.replace("ا", "")


def construction_patterns(root, source_phrase):
    """(ROOT, next-token) patterns from the early-source phrases, where next-token is a particle (fī, ʿalā, ʿan, ilā,
    bayna ...). Returned as skeleton prefixes, e.g. {'في', 'علي'}."""
    pats = set()
    for s in re.split(r"[؛;]", source_phrase or ""):
        toks = [load.norm(t) for t in re.findall(r"[؀-ۿ]+", SRC_TAG.sub("", s))]
        for i, t in enumerate(toks[:-1]):
            if is_root_form(t, root):
                nxt = toks[i + 1]
                for p in PARTICLES:
                    if nxt == p or (len(p) >= 2 and nxt.startswith(p) and p in {"علي", "عن", "الي", "بين"}):
                        pats.add(p)
    return pats


def quoted_ayah(row, ayah_ref):
    """True if the branch's early-source phrase quotes >= 3 consecutive words of the ayah (e.g. Mufradat citing it)."""
    kind, note, sp, img, what = load.kind_of(row)
    ph = " ".join(skel(load.norm(t)) for t in re.findall(r"[؀-ۿ]+", sp or ""))
    toks = [skel(load.norm(t)) for t in re.findall(r"[؀-ۿ]+", load.quran()[ayah_ref])]
    for i in range(len(toks) - 2):
        g = " ".join(toks[i:i + 3])
        if len(g) >= 8 and g in ph:
            return g
    return None


def licensed_v2(ref_word, row, win=4):
    """Construction licence: quoted ayah, OR a particle pattern right after the occurrence, OR a key root nearby."""
    root = load.nroot(row["root"])
    s, a, w = ref_word.split(":")
    q = quoted_ayah(row, f"{s}:{a}")
    if q:
        return "quoted:" + q
    kind, note, sp, img, what = load.kind_of(row)
    pats = construction_patterns(root, sp or row.get("source_phrase", ""))
    ws = load.words()[1][f"{s}:{a}"]
    w = int(w)
    after = [skel(load.norm(x["surface"])) for x in ws if w < int(x["w"]) <= w + 2]
    for p in pats:
        sp_ = skel(p)
        if any(t == sp_ or (len(sp_) >= 2 and t.startswith(sp_) and p in {"علي", "عن", "الي", "بين"}) for t in after[:1]):
            return "pattern:" + p
    k = licensed(ref_word, root, keys_for(row), win)
    return ("key:" + k) if k else None
