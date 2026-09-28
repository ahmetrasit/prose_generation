"""Targeted supply for the lexicon reading (R_lex) of design B ("three readings, one integration").

Everything is descriptive (no verdicts, no scores, no 'no value' labels, no earlier readers' conclusions).
Sections, per focus ayah:
  A  ayah + words (surface, root, lemma, POS)
  B  window: +-7 ayat of the same surah (vocalised text)
  C  branch index: EVERY branch of every root of the ayah: image, full definition, early-source phrase,
     Turkish concept gloss, branch_kind; for collocation-bound branches the construction keys and whether a key
     occurs in this ayah (the dictionary-principle guard, shown to the reader, not applied as a filter)
  D  same-surah echoes: every other occurrence in the surah of the ayah's roots (ref + the word)
  E  concordance (KWIC) for roots with <= 30 Quranic occurrences
  F  usage profile rows (collocation profiles, descriptive counts) for roots with <= 60 occurrences
  G  definitional cross-references (materialised joins): a lexeme of another Quranic root sitting inside the
     definition/phrase of one of the ayah's branches (out), or a lexeme of the ayah's roots inside a window root's
     branch text (in); each with where that other root occurs (surah first, then Quran-wide if rare)
  H  qira'at variants of the ayah's words
Output: supply/<S_A>.md and a size line on stdout.
"""
import re, os, sys, csv, collections, functools
import load, construction

OUTD = os.path.join(load.OUT, "supply")
os.makedirs(OUTD, exist_ok=True)
QIRAAT = "/Volumes/OZTURK/_projects/study/_project_corpus/qiraat.tsv"
AR = re.compile(r"[ء-ي]+")


@functools.lru_cache(None)
def qiraat():
    d = collections.defaultdict(list)
    for r in csv.DictReader(open(QIRAAT, encoding="utf-8"), delimiter="\t"):
        s, a, w = r["tsv_word_ref"].split(":")
        d[f"{s}:{a}"].append(r)
    return d


def kwic(ref_word, span=4):
    s, a, w = ref_word.split(":")
    ws = load.words()[1][f"{s}:{a}"]
    w = int(w)
    return " ".join(x["surface"] for x in ws if abs(int(x["w"]) - w) <= span)


def skel(t):
    """Orthographic skeleton for matching dictionary spelling against Quranic rasm (غشاوة vs غشوة): drop alif."""
    return t.replace("ا", "")


def strip_clitics(t):
    """One proclitic (و ف ب ل ك) then the article; returns the stem form only."""
    if len(t) > 4 and t[0] in "وفبلك" and (t[1:].startswith("ال") or len(t) > 5):
        t2 = t[1:]
        if t2.startswith("ال") or t[0] in "وف":
            t = t2
    if t.startswith("ال") and len(t) > 4:
        t = t[2:]
    elif t.startswith("لل") and len(t) > 4:
        t = t[2:]
    return t


@functools.lru_cache(None)
def lexeme_roots():
    """skeleton of the clitic-stripped Quranic surface -> most frequent root (stems >= 4 letters, skeleton >= 3)."""
    rows, _ = load.words()
    m = {}
    for r in rows:
        root = load.nroot((r["roots"] or "").split("|")[0])
        if not root:
            continue
        st = strip_clitics(load.norm(r["surface"]))
        if len(st) >= 4 and len(skel(st)) >= 3:
            m.setdefault(skel(st), collections.Counter())[root] += 1
    return {k: c.most_common(1)[0][0] for k, c in m.items()}


BOILER = re.compile(r"يدخل فيه|ويدخل فيه|يقال|ويقال|أي|معناه")
STOPROOT = {"ء ل ه", "ق و ل", "ك و ن", "ش ي ء", "ع ل و", "ج ع ل", "ء ت ي", "ف ع ل", "ء م ن", "ف ل ن"}


def text_lexemes(text):
    text = BOILER.sub(" ", text)
    out = set()
    for t in AR.findall(load.norm(text)):
        st = strip_clitics(t)
        if len(st) >= 4:
            out.add(skel(st))
    return out


@functools.lru_cache(None)
def defining_df():
    """In how many branch texts of the whole dictionary each lexeme occurs: very common ones are defining
    vocabulary (a word used to define many senses), not cues."""
    df = collections.Counter()
    for (root, b), r in load.branches().items():
        kind, note, sp, img, what = load.kind_of(r)
        df.update(text_lexemes(" ".join([r["image"], what or r["what_is"], sp or r["source_phrase"]])))
    return df


MAX_DEF_DF = 40
LIGHT = bool(os.environ.get("LIGHT"))


def build(ref, window=7):
    s, a = map(int, ref.split(":"))
    q = load.quran()
    _, by = load.words()
    n = load.surah_len(s)
    roots = load.ayah_roots(ref)
    bbr = load.branches_by_root()
    ridx = load.root_index()
    parts = {}

    # A
    A = [f"# Focus {ref}", q[ref], "", "| w | surface | root | lemma | pos |", "|---|---|---|---|---|"]
    for w in by[ref]:
        A.append(f"| {w['w']} | {w['surface']} | {w['roots']} | {w['lemmas']} | {w['pos']} |")
    parts["A ayah+words"] = "\n".join(A)

    # B
    lo, hi = max(1, a - window), min(n, a + window)
    parts["B window"] = "\n".join(["## Window"] + [f"{s}:{i} {q[f'{s}:{i}']}" for i in range(lo, hi + 1)])

    # C
    C = ["## Branch index (every branch of every root in the ayah)"]
    for root in roots:
        occ = [o for o in ridx.get(root, []) if o.startswith(f"{s}:{a}:")]
        for r in bbr.get(root, []):
            if r["qac_attested"] != "yes":
                continue
            kind, note, sp, img, what = load.kind_of(r)
            line = (f"- {root} {r['branch']} [{kind}] {r['image']}: {what or r['what_is']}"
                    + ("" if LIGHT else f" | {sp or r['source_phrase']}") + f" | tr: {r['tr_gloss']}")
            if kind == "collocation":
                keys = construction.keys_for(r)
                lic = [construction.licensed(o, root, keys, None) for o in occ]
                line += f" | construction keys: {' / '.join(keys) or '?'}; present in this ayah: {'yes' if any(lic) else 'no'}"
            C.append(line)
    parts["C branch index"] = "\n".join(C)

    # D
    D = ["## Same-surah echoes of the ayah's roots"]
    for root in roots:
        occ = [o for o in ridx.get(root, []) if o.split(":")[0] == str(s) and not o.startswith(f"{s}:{a}:")]
        if occ:
            words = []
            for o in occ:
                ss, aa, ww = o.split(":")
                sf = next(x["surface"] for x in by[f"{ss}:{aa}"] if x["w"] == ww)
                words.append(f"{ss}:{aa} {sf}")
            D.append(f"- {root} ({len(occ)}): " + "; ".join(words))
    parts["D same-surah echoes"] = "\n".join(D)

    # E
    E = ["## Concordance of rarer roots (<= 30 Quranic occurrences)"]
    for root in roots:
        occ = ridx.get(root, [])
        if 0 < len(occ) <= 30:
            E.append(f"### {root} ({len(occ)} occurrences)")
            for o in occ:
                E.append(f"- {o} {kwic(o)}")
    parts["E concordance"] = "\n".join(E)

    # F
    F = ["## Usage profiles (collocation partners, descriptive counts)"]
    col = load.collocations()
    for root in roots:
        occ = ridx.get(root, [])
        if 0 < len(occ) <= 60 and root in col:
            rows = sorted(col[root], key=lambda r: (-int(r["attach_count"]), r["form_tag"]))
            F.append(f"- {root}: " + "; ".join(
                f"{r['form_tag']} x{r['instance_count']}: {r['partner_root']} {r['attach_count']}/{r['total_attach']} ({r['top_rel']})"
                for r in rows[:12]))
    parts["F usage profiles"] = "\n".join(F)

    # G
    G = ["## Definitional cross-references (a lexeme of one root inside another root's branch text)"]
    lr = lexeme_roots()
    surah_roots = collections.Counter()
    for i in range(1, n + 1):
        for rt in load.ayah_roots(f"{s}:{i}"):
            surah_roots[rt] += 1
    win_roots = set()
    for i in range(lo, hi + 1):
        win_roots |= set(load.ayah_roots(f"{s}:{i}"))
    seen = set()
    # out: ayah branch text -> other roots
    for root in roots:
        for r in bbr.get(root, []):
            if r["qac_attested"] != "yes":
                continue
            kind, note, sp, img, what = load.kind_of(r)
            text = " ".join([r["image"], what or r["what_is"], sp or r["source_phrase"]])
            for lx in text_lexemes(text):
                other = lr.get(lx)
                if not other or other == root or other in STOPROOT:
                    continue
                # window hits (the other root stands within +-7 ayat) bypass the defining-vocabulary filter:
                # they are few and they are exactly the neighbour activations; farther hits must be specific.
                if other not in win_roots and defining_df()[lx] > MAX_DEF_DF:
                    continue
                qn = len(ridx.get(other, []))
                in_surah = [o for o in ridx.get(other, []) if o.split(":")[0] == str(s)]
                in_window = other in win_roots
                # attention argument: a frequent root inside a definition is usually a defining word, not a cue;
                # keep window hits always, surah hits for roots with <= 100 Quranic uses, Quran-wide for <= 12.
                if in_window or (in_surah and qn <= 100) or (not in_surah and qn <= 12):
                    key = (root, r["branch"], other)
                    if key in seen:
                        continue
                    seen.add(key)
                    allrefs = sorted({':'.join(o.split(':')[:2]) for o in ridx.get(other, [])},
                                     key=lambda x: tuple(map(int, x.split(':'))))
                    srefs = [x for x in allrefs if x.split(':')[0] == str(s)]
                    where = (f"in this surah at {', '.join(srefs)}" if srefs else "")
                    if qn <= 30:
                        where += ("; " if where else "") + f"Quran-wide ({qn}): {', '.join(allrefs)}"
                    G.append(f"- out: {root} {r['branch']} ({r['image']}) contains «{lx}» → {other}; {where}")
    # in: window roots' branch text -> the ayah's roots
    ayah_lex_roots = set(roots)
    for wr in sorted(win_roots - set(roots)):
        for r in bbr.get(wr, []):
            if r["qac_attested"] != "yes":
                continue
            kind, note, sp, img, what = load.kind_of(r)
            text = " ".join([r["image"], what or r["what_is"], sp or r["source_phrase"]])
            for lx in text_lexemes(text):
                other = lr.get(lx)
                if other in ayah_lex_roots and other != wr and other not in STOPROOT and defining_df()[lx] <= MAX_DEF_DF:
                    key = (wr, r["branch"], other)
                    if key in seen:
                        continue
                    seen.add(key)
                    wrefs = sorted({f"{s}:{i}" for i in range(lo, hi + 1) if wr in load.ayah_roots(f"{s}:{i}")},
                                   key=lambda x: int(x.split(":")[1]))
                    G.append(f"- in: {wr} {r['branch']} ({r['image']}) at {', '.join(wrefs)} contains «{lx}» → {other} (in the focus ayah)")
    parts["G cross-references"] = "\n".join(G)

    # H
    H = ["## Qira'at"]
    for r in qiraat().get(ref, []):
        if r["qiraat_reader_set"] != "canonical":
            H.append(f"- {r['tsv_word_ref']} {r['qiraat_arabic']} ({r['qiraat_reader_set']}): {r['qiraat_note'][:160]}")
    parts["H qiraat"] = "\n".join(H)

    txt = "\n\n".join(parts.values()) + "\n"
    open(os.path.join(OUTD, f"{s}_{a}.md"), "w", encoding="utf-8").write(txt)
    sizes = {k: len(v) for k, v in parts.items()}
    # tokens: vocalised Quran text ~1.0 char/token; the rest ~1.55 chars/token (calibrated on v9 cold/dict arms)
    quranish = sizes["A ayah+words"] + sizes["B window"] + sizes["D same-surah echoes"] + sizes["E concordance"]
    other = len(txt) - quranish
    tokens = int(quranish / 1.0 + other / 1.55)
    return txt, sizes, tokens


if __name__ == "__main__":
    refs = sys.argv[1:] or ["1:6", "4:34", "5:6", "18:86", "18:96", "29:38", "2:255"]
    print("ref | total chars | est tokens | " + " | ".join(["A", "B", "C", "D", "E", "F", "G", "H"]))
    for ref in refs:
        txt, sizes, tok = build(ref)
        print(f"{ref} | {len(txt)} | {tok} | " + " | ".join(str(v) for v in sizes.values()))
