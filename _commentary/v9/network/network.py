#!/usr/bin/env python3
"""V9 ayah network: typed, evidence-carrying links around one focus ayah, and the structures they form.

No model is involved. The network proposes; Luna judges edges and names structures; Sol writes.

Nodes
  F  a word of the focus ayah (content words only)
  B  a dictionary branch of a focus word's root (identity, documented alternative or echo root), attached to its
     word. A branch is `plain` when it is the word's sense in the ayah (from the HFT focus-only baseline; else B001
     of the identity root) and `rare` otherwise. Rarity is also described by the number of source dictionaries and
     sole attestation (reported, not used as a filter).
  A  a context ayah: the host surah, the Fatiha, and passages about the focus ayah's named people (ayat naming them
     ±PEOPLE_WINDOW; very frequent names such as Allah are not people anchors)
  M  an HFT record (a mechanism); used to attach structures, never to form them

Edges (every edge carries its evidence: the Arabic that makes it)
  lex    a word of the branch's Arabic image or source phrases is a form of the target's root, or names the
         target focus word's plain image
  rel    the dictionary's own neighbour relation (synonym, near_synonym, antonym, polarity_pair, thematic, …)
         to a root present in the target
  img    quran-slm image network: top-k partner by distinct root (same ayah, ±7, surah, Fatiha, people passages)
  sound  a root or a definition word one letter away from a focus root (sound play; never etymology)
  frame  focus word and a context word stand in the same frame (same governing verb lemma right before them)
  form   focus word and a context word share a rare derived form (measure V–XII) and participle status
  hft    the branch or word is a step of an HFT trace

Structures
  hub          a focus word or context ayah that rare branches of ≥3 different roots point to
  triangle     three nodes pairwise linked, at least one a rare branch (the image confirms itself)
  convergence  rare branches ranked by how many *kinds* of edge support them
  bridge       a node linked to members of two different hubs (thread joins, Kapanış)
  chain        per hub, the surah ayat its members touch, in surah order (candidate material; the writer chooses)
  formula      other ayat sharing ≥2 focus roots, grouped by the roots they share (leaves, not members)

Usage: python3 _commentary/v9/network/network.py 29:38 [--k 3] [--out DIR]
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(V9))
import prepare as P  # noqa: E402

PEOPLE_WINDOW = 3     # ayat around each ayah that names a focus person or people
PEOPLE_MAX = 60       # a name in more ayat than this is not a people anchor (Allah, Shaytan, …)
ROOT_DF_MAX = 400     # a root in more ayat than this is too common to carry a lexical link to a focus word
LEMMA_DF_MAX = 150    # a lemma in more ayat than this is too common to carry a lexical link to a context ayah
PLAIN_DF_MAX = 120    # a word naming a focus word's plain image must be a Quranic lemma in at most this many ayat
SRC_RARE_DF = 40      # a source-phrase word (not the branch's own image) links strongly only through a rarer lemma
NEAREST = 3           # per (branch, edge type, target root) and zone: the nearest context ayat kept
# adverbial nouns (after, before, between, above, below, without, at, around, behind): never with the article, so an
# article in a dictionary word rules them out (البعد is 'distance', not 'after')
ADVERBIAL = {"بَعْد", "قَبْل", "بَيْن", "فَوْق", "تَحْت", "دُون", "عِند", "عِنْد", "حَوْل", "خَلْف", "أَمَام", "لَدُن", "لَدَى"}
RARE_FORMS = {"V", "VI", "VII", "IX", "X", "XI", "XII"}
HUB_MIN = 3
HUBS_PER_ZONE = 6     # context hubs shown per zone (surah, Fatiha, people, inter), by evidence score
CONTRAST = {"antonym", "polarity_pair"}

DIAC = re.compile(r"[ؐ-ًؚ-ٟۖ-ۭـ]")
STOP = {"من", "في", "على", "الي", "عن", "اي", "هو", "هي", "الذي", "التي", "اذا", "كل", "ما", "لا", "او", "ثم", "به",
        "له", "بها", "لها", "يقال", "سمي", "ذلك", "شيء", "اصل", "يدل", "واحد", "معروف", "ضرب", "اسم", "ايضا", "قال",
        "وهو", "وهي", "كان", "بعض", "فهو", "فلان", "جمع", "قيل", "يقول", "انه", "ان", "كما", "حتي", "مثل", "غير",
        "بين", "قبل", "عند", "هذا", "هذه", "ذو", "ذات", "لم", "قد", "لان", "الواحد", "يسمي", "تقول", "العرب", "امر",
        "كذا", "عنه", "منه", "فعل", "يفعل", "مصدر", "يكون", "صار", "يستعمل", "يذكر", "يونث", "كانه", "تعني", "ناس",
        "قوم", "خلق", "قول", "لما", "منسوب", "اذ", "الا", "انما", "وقد", "فيه", "فيها", "منها", "عليه", "اليه",
        "وكل", "يعني", "اراد", "اسم", "معني", "كثير", "قليل", "حين", "حيث", "وقت", "نحو", "دون", "سواء", "ابو",
        "فيما", "مما", "عما", "بما", "انما", "كلما", "ايضا", "الذين", "هولاء", "اولئك", "لانه", "لانها", "حتي"}


def nz(t: str) -> str:
    t = DIAC.sub("", t or "").replace("ٰ", "ا")
    return t.translate(str.maketrans("ٱأإآىةؤئ", "ااااياوي"))


def core(t: str) -> str:
    for p in ("وال", "فال", "بال", "كال", "لل", "ال"):
        if t.startswith(p) and len(t) - len(p) >= 3:
            return t[len(p):]
    return t


def ar_tokens(text: str) -> list[str]:
    """Content words of a dictionary phrase, article stripped; a word after نقيض/ضد/خلاف is marked with a leading '!'."""
    text = re.sub(r"\([^)]*\)", " ", text or "")
    out, contrast = [], False
    for raw in (nz(x) for x in re.findall(r"[ء-يٰٱً-ٟ]+", text)):
        t = core(raw)
        if t in ("نقيض", "ضد", "خلاف"):
            contrast = True
            continue
        if len(t) >= 3 and t not in STOP and not (t[0] in "وفبلك" and t[1:] in STOP):
            out.append(("!" if contrast else "") + ("^" if t != raw else "") + t)  # ^ = had the article (nominal)
        contrast = False
    return out


def bare(t: str) -> str:
    return t.lstrip("!^")


def lraw(lemma: str) -> str:
    """Lemma identity: vowelled (بَعْد 'after' and بُعْد 'distance' stay apart), digits dropped, final short vowel and a
    defective final ي dropped (QAC spells وَاد and وَادِي)."""
    lem = re.sub(r"\d", "", lemma or "").replace("ٱ", "ا")
    lem = re.sub(r"[\u064B-\u0652]+$", "", lem)
    if lem.endswith("ي") and len(nz(lem)) >= 4:
        lem = re.sub(r"[\u064B-\u0652]+$", "", lem[:-1])
    return lem


def lnorm(lemma: str) -> str:
    return re.sub(r"\d", "", nz(lemma))


def root_dist(a: str, b: str) -> int:
    return sum(x != y for x, y in zip(a, b)) + abs(len(a) - len(b))


class Lexicon:
    """Quranic forms → root (exact lookups only), root ayah frequency, gateway root ids per QAC root key."""

    def __init__(self, src: P.Sources) -> None:
        self.form_root = defaultdict(Counter)
        self.form_lemma = defaultdict(Counter)
        self.ayat_of = defaultdict(set)
        lemma_ayat = defaultdict(set)
        for s, a, surf, stem, lemma, key, pos in src.qac.execute(
                "select surah, ayah, surface_ar, stem_ar, lemma_ar, root_join_key, pos from qac_morphemes "
                "where root_join_key!=''"):
            self.ayat_of[key].add((s, a))
            lemma_ayat[lraw(lemma)].add((s, a))
            nominal = pos in ("N", "ADJ", "PN")
            for f in {nz(surf), nz(stem), nz(lemma), core(nz(surf))}:
                if len(f) >= 2:
                    self.form_root[f][key] += 1
                    self.form_lemma[f][(lraw(lemma), nominal)] += 1
        self.df = {k: len(v) for k, v in self.ayat_of.items()}
        self.lemma_df = {k: len(v) for k, v in lemma_ayat.items()}
        self.gw = {k: r["rootIds"] for k, r in src.gateway.items()}

    def lemma(self, tok: str) -> str | None:
        """Quranic lemma of a dictionary word; a word written with the article can only be a nominal lemma."""
        nominal = "^" in tok
        tok = bare(tok)
        for c in self._cands(tok):
            ctr = Counter()
            for (lem, is_nom), n in self.form_lemma.get(c, {}).items():
                if not nominal or (is_nom and lem not in ADVERBIAL):
                    ctr[lem] += n
            if ctr:
                lem, n = ctr.most_common(1)[0]
                if n / sum(ctr.values()) >= 0.7:
                    return lem
        return None

    @staticmethod
    def _cands(tok: str) -> list[str]:
        cands = [tok]
        if tok[0] in "وفبلك" and len(tok) >= 4:
            cands.append(tok[1:])
        if tok.endswith("ي") and len(tok) >= 4:  # defective nouns: الوادي → وَاد, الداعي → دَاع
            cands.append(tok[:-1])
        return cands

    def root(self, tok: str) -> str | None:
        cands = [tok]
        for p in ("وال", "فال", "بال", "كال", "لل", "ال"):
            if tok.startswith(p) and len(tok) - len(p) >= 3:
                cands.append(tok[len(p):])
        if tok[0] in "وفبلك" and len(tok) >= 4:
            cands.append(tok[1:])
        for c in cands:
            ctr = self.form_root.get(c)
            if ctr:
                key, n = ctr.most_common(1)[0]
                if n / sum(ctr.values()) >= 0.7:
                    return key
        return None


class Net:
    def __init__(self) -> None:
        self.nodes: dict[str, dict] = {}
        self.edges: list[dict] = []
        self.adj: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))

    def node(self, nid: str, **attrs) -> str:
        self.nodes.setdefault(nid, attrs)
        return nid

    def edge(self, a: str, b: str, kind: str, evidence: str, sub: str = "") -> None:
        if a == b:
            return
        e = {"a": a, "b": b, "kind": kind, "sub": sub, "evidence": evidence}
        self.edges.append(e)
        self.adj[a][b].append(e)
        self.adj[b][a].append(e)


def build(ref: str, k: int, inter: bool = False) -> tuple[Net, dict]:
    src = P.Sources()
    lex = Lexicon(src)
    surah, ayah = (int(x) for x in ref.split(":"))
    bundle = json.loads((P.PG / "bundles" / f"s{surah:03d}" / f"{surah}_{ayah}.ayah.json").read_text(encoding="utf-8"))
    net = Net()

    # ---- focus words, branches, plain senses
    hft_plain = defaultdict(set)   # word index → {(root_id, branch_id)} from HFT focus-only baselines
    hft_records = []
    for r in ((bundle.get("v12_focus_trace_hermetic") or {}).get("readers") or {}).values():
        for kind in ("baseline_models", "context_deltas", "surprising_valid_outliers"):
            for rec in r.get(kind) or []:
                name = rec.get("model_id") or rec.get("delta_id") or rec.get("outlier_id")
                steps = rec.get("activation_trace") or []
                hft_records.append((name, kind, steps))
                if kind == "baseline_models":
                    for s in steps:
                        if s.get("source_ref") == ref:
                            for i in s.get("source_word_indices") or []:
                                hft_plain[int(i)].add((s.get("mapped_root_id"), s.get("branch_id")))
    focus_words = [w for w in src.words(ref) if w["roots"]]
    fkeys = {}                      # F id → QAC root join keys
    froot_ids = {}                  # F id → gateway identity root ids
    plain_tokens = {}               # F id → Arabic tokens naming the word's plain sense
    for w in focus_words:
        f = net.node(f"F:{w['w']}", type="F", surface=w["surface"], w=w["w"], lemma=w["lemmas"], pos=w["pos"])
        roots = src.word_roots(w)
        fkeys[f] = [k_ for k_ in w["roots"].split(";") if k_]
        froot_ids[f] = roots["identity"] + [a[0] for a in roots["alternatives"]]
        plain = hft_plain.get(w["w"], set())
        if not plain and roots["identity"]:
            plain = {(roots["identity"][0], "B001")}
        toks = set()
        for rid, bid in plain:
            toks |= {t.lstrip("!") for t in ar_tokens(src.image(f"quranic:{rid}:{bid}"))}
        for rid in roots["identity"][:1]:
            toks |= {t.lstrip("!") for t in ar_tokens(src.image(f"quranic:{rid}:B001"))}
        plain_tokens[f] = {lex.lemma(t) for t in toks
                           if lex.lemma(t) and lex.lemma_df.get(lex.lemma(t), 0) <= PLAIN_DF_MAX
                           and not any(root_dist(bare(t), k_) == 0 for k_ in fkeys[f])}
        for kind, rids in (("identity", roots["identity"]), ("alternative", [a[0] for a in roots["alternatives"]]),
                           ("echo", [e[0] for e in roots["echo"]])):
            for rid in rids:
                for nid in src.branches_of.get(rid, []):
                    bid = nid.split(":")[2]
                    br = src.branch(nid)
                    details = (br.get("source_synthesis") or {}).get("source_details") or []
                    b = net.node(f"B:{nid}@{w['w']}", type="B", node_id=nid, word=f, root=src.root_name.get(rid, rid),
                                 root_id=rid, bid=bid, root_kind=kind, gloss=src.gloss(nid), image=src.image(nid),
                                 src=br.get("source_phrase_ar", ""), n_sources=len(br.get("sources") or []),
                                 sole=any(d.get("kind") == "sole_attestation" for d in details),
                                 plain=(rid, bid) in plain and kind == "identity")
                    net.nodes[b]["rare"] = not net.nodes[b]["plain"]

    # ---- context ayat
    zone = {}
    for r in P.ayah_refs(surah, src):
        if r != ref:
            zone[r] = "surah"
    for i in range(1, 8):
        zone.setdefault(f"1:{i}", "fatiha")
    pn = {l for w in src.words(ref) if "PN" in w["pos"].split(";") for l in w["lemmas"].split(";") if l}
    anchors = []
    for lemma in sorted(pn):
        refs = sorted({(s, a) for s, a in src.qac.execute(
            "select distinct surah, ayah from qac_morphemes where lemma_ar=?", (lemma,))})
        if len(refs) <= PEOPLE_MAX:
            anchors.append((lemma, len(refs)))
            for s, a in refs:
                for a2 in range(a - PEOPLE_WINDOW, a + PEOPLE_WINDOW + 1):
                    r = f"{s}:{a2}"
                    if r in src.quran and r != ref:
                        zone.setdefault(r, "people")
    if inter:  # targets of the reciprocal inter-ayah rows (quran-data), not already in scope
        rows = (P.RECIPROCAL_DIR / f"focus_{surah}_{ayah}_cutoff_100.tsv").read_text(encoding="utf-8").splitlines()
        head = rows[0].split("\t")
        for line in rows[1:]:
            r = dict(zip(head, line.split("\t"))).get("target_ref", "")
            if r and r != ref:
                zone.setdefault(r, "inter")
    words_of = {r: src.words(r) for r in zone}
    for r, z in zone.items():
        net.node(f"A:{r}", type="A", ref=r, zone=z)

    def dist(r: str) -> tuple:
        s, a = (int(x) for x in r.split(":"))
        return (0, abs(a - ayah)) if s == surah else ((1, a) if s == 1 else (2, s, a))  # order within a zone

    lemma_index = defaultdict(list)  # lemma → [(ayah ref, surface)]
    rid_index = defaultdict(list)    # gateway root id → [(ayah ref, surface)]
    for r, ws in words_of.items():
        for w in ws:
            for lem in (x for x in w["lemmas"].split(";") if x):
                lemma_index[lraw(lem)].append((r, w["surface"]))
            for key in (x for x in w["roots"].split(";") if x):
                for rid in lex.gw.get(key, []):
                    rid_index[rid].append((r, w["surface"]))

    def nearest(hits: list[tuple[str, str]]) -> list[tuple[str, list[str]]]:
        """The nearest NEAREST occurrences in each zone (surah, Fatiha, people passages)."""
        by = defaultdict(list)
        for r, s in hits:
            by[r].append(s)
        out, per_zone = [], Counter()
        for r, surfs in sorted(by.items(), key=lambda kv: dist(kv[0])):
            if per_zone[zone[r]] < NEAREST:
                per_zone[zone[r]] += 1
                out.append((r, surfs))
        return out

    fkey_of = {k_: f for f, ks in fkeys.items() for k_ in ks}
    frid_of = {rid: f for f, rids in froot_ids.items() for rid in rids}
    B = [n for n, d in net.nodes.items() if d["type"] == "B"]

    # ---- lex, rel, sound edges from branches
    for b in B:
        d = net.nodes[b]
        own_keys = set(fkeys[d["word"]])
        image_toks = ar_tokens(d["image"])
        seen = set()
        n_image = len(image_toks)
        for i_tok, t in enumerate(image_toks + ar_tokens(d["src"])):
            sub = "contrast" if t.startswith("!") else ""
            traw, t = t, bare(t)
            field = "image" if i_tok < n_image else "src"
            key = lex.root(t)
            own = key in own_keys
            # a focus word of another root: the definition word is a form of its root, or names its plain image
            if key and not own and key in fkey_of and fkey_of[key] != d["word"] and lex.df.get(key, 0) <= ROOT_DF_MAX \
                    and ("F", key) not in seen:
                seen.add(("F", key))
                net.edge(b, fkey_of[key], "lex", f"{t} → root {P.spaced(key)}", sub or field)
            tl = lex.lemma(traw)
            for f, ptoks in plain_tokens.items():
                if f != d["word"] and tl in ptoks and (f, tl) not in seen:
                    seen.add((f, tl))
                    net.edge(b, f, "lex", f"{t} names the plain image of {net.nodes[f]['surface']}", sub or field)
            # a context ayah: the same Quranic lemma occurs there (lemma-level; common lemmas skipped)
            lem = tl
            if lem and not own and lex.lemma_df.get(lem, 0) <= LEMMA_DF_MAX and ("A", lem) not in seen:
                seen.add(("A", lem))
                rare_src = lex.lemma_df.get(lem, 0) <= SRC_RARE_DF
                for r, surfs in nearest(lemma_index.get(lem, [])):
                    net.edge(b, f"A:{r}", "lex", f"{t} → {' '.join(dict.fromkeys(surfs))}",
                             sub or ("image" if field == "image" else ("src-rare" if rare_src else "src")))
        for t in image_toks + ar_tokens(d["src"]):  # sound: only a word the dictionary sets in contrast (نقيض/ضد/خلاف)
            if not t.startswith("!"):
                continue
            t = bare(t)
            if len(t) == 3:
                for f, keys in fkeys.items():
                    if f != d["word"] and t not in keys and any(len(k_) == 3 and root_dist(t, k_) == 1 for k_ in keys) \
                            and (f, "sound", t) not in seen:
                        seen.add((f, "sound", t))
                        net.edge(b, f, "sound", f"contrast word {t} ~ {net.nodes[f]['surface']} (one letter apart)", "contrast")
        for nd in src.branch(d["node_id"]).get("neighbor_distinctions") or []:
            rid = nd.get("neighbor_ref", "").split("/")[0]
            if rid == d["root_id"]:
                continue
            rtype = nd.get("relation_type", "")
            ev = f"{src.root_name.get(rid, rid)} {nd['neighbor_ref'].split('/')[-1]} ({nd.get('gloss', '')})"
            if rid in frid_of and frid_of[rid] != d["word"]:
                net.edge(b, frid_of[rid], "rel", ev, rtype)
            for r, surfs in nearest(rid_index.get(rid, [])):
                net.edge(b, f"A:{r}", "rel", f"{ev} → {' '.join(dict.fromkeys(surfs))}", rtype)

    # ---- img edges (quran-slm), top-k by distinct partner root per pool
    focus_pool = []
    for w in focus_words:
        rr = src.word_roots(w)
        for rid in rr["identity"] + [a[0] for a in rr["alternatives"]]:
            focus_pool += [(n, f"F:{w['w']}") for n in src.branches_of.get(rid, [])]
    ctx = defaultdict(list)
    for r, z in zone.items():
        pool = "near" if z == "surah" and abs(int(r.split(":")[1]) - ayah) <= P.WINDOW else z
        for n, w in src.ayah_branches(r):
            ctx[pool].append((n, f"A:{r}|{w['surface']}"))
    for b in B:
        d = net.nodes[b]
        n = d["node_id"]
        if n not in src.net_ix:
            continue
        pools = [("same", [(m, wh) for m, wh in focus_pool if wh != d["word"]])] + list(ctx.items())
        for label, pool in pools:
            for p, where, aff in P.top_distinct(src, n, pool, k):
                target, _, surf = where.partition("|")
                ev = f"{label}: {P.short(src, p)}" + (f" ← {surf}" if surf else "")
                net.edge(b, target, "img", ev, label)

    # ---- word-level edges: sound between focus roots, frame, rare form
    for f1, f2 in itertools.combinations(fkeys, 2):
        for k1 in fkeys[f1]:
            for k2 in fkeys[f2]:
                if len(k1) == 3 and len(k2) == 3 and root_dist(k1, k2) == 1:
                    net.edge(f1, f2, "sound", f"{P.spaced(k1)} ~ {P.spaced(k2)}")
    morph = {}
    for r in list(zone) + [ref]:
        s, a = (int(x) for x in r.split(":"))
        morph[r] = list(src.qac.execute(
            "select word_index, lemma_ar, pos, measure, morph_features, surface_ar from qac_morphemes "
            "where surah=? and ayah=? and morpheme_role='STEM' order by word_index", (s, a)))
    fw = {row[0]: row for row in morph[ref]}
    for f in fkeys:
        w = net.nodes[f]["w"]
        row = fw.get(w)
        prev = fw.get(w - 1)
        if prev and prev[2] == "V":  # same governing verb, same inflection, in the host surah
            pgn = prev[4].split("|")[-1]
            for r, rows in morph.items():
                if r == ref or zone.get(r) != "surah":
                    continue
                for (i1, l1, p1, _m1, f1, s1), (i2, l2, p2, _m, _f, s2) in zip(rows, rows[1:]):
                    if l1 == prev[1] and f1.split("|")[-1] == pgn and i2 == i1 + 1 and p2 in ("N", "ADJ", "V"):
                        net.edge(f, f"A:{r}", "frame", f"{prev[5]} {net.nodes[f]['surface']} ~ {s1} {s2}")
        if row and row[3] in RARE_FORMS:
            pcpl = "PCPL" in row[4]
            hits = []
            for r, rows in morph.items():
                if r != ref:
                    hits += [(r, s2) for (_i, _l, _p, m2, f2, s2) in rows if m2 == row[3] and ("PCPL" in f2) == pcpl]
            for r, surfs in nearest(hits) if len(hits) <= 40 else []:
                net.edge(f, f"A:{r}", "form", f"form {row[3]}{' participle' if pcpl else ''}: {' '.join(surfs)}")
            fat = [(r, s2) for r, s2 in hits if r.startswith("1:")]
            for r, surfs in nearest(fat):
                net.edge(f, f"A:{r}", "form", f"form {row[3]}{' participle' if pcpl else ''}: {' '.join(surfs)}")

    # ---- HFT mechanisms
    for name, kind, steps in hft_records:
        m = net.node(f"M:{name}", type="M", kind=kind)
        for s in steps:
            r = s.get("source_ref", "")
            if r == ref:
                for i in s.get("source_word_indices") or []:
                    b = f"B:quranic:{s.get('mapped_root_id')}:{s.get('branch_id')}@{int(i)}"
                    if b in net.nodes:
                        net.edge(m, b, "hft", name)
                    elif f"F:{int(i)}" in net.nodes:
                        net.edge(m, f"F:{int(i)}", "hft", name)
            elif f"A:{r}" in net.nodes:
                net.edge(m, f"A:{r}", "hft", name)

    # ---- formula leaves: other ayat sharing ≥2 focus roots (content roots only)
    content = {k_ for ks in fkeys.values() for k_ in ks if lex.df.get(k_, 0) <= ROOT_DF_MAX}
    shared = defaultdict(set)
    for key in content:
        for s, a in lex.ayat_of[key]:
            r = f"{s}:{a}"
            if r != ref and s != surah and s != 1:
                shared[r].add(key)
    groups = defaultdict(list)
    for r, keys in shared.items():
        if len(keys) >= 2:
            groups[tuple(sorted(keys))].append(r)
    meta = {"ref": ref, "k": k, "anchors": anchors, "zones": Counter(zone.values()), "groups": groups,
            "words_of": {r: " ".join(w["surface"] for w in ws) for r, ws in words_of.items()}}
    return net, meta


# ---------------------------------------------------------------- structures

STRONG_REL = {"synonym", "near_synonym", "antonym", "polarity_pair", "thematic"}


def weight(e: dict) -> float:
    """Evidence weight of one edge. 0 = weak: it may extend a structure but never makes one."""
    k, sub = e["kind"], e["sub"]
    if k == "rel":
        if sub in ("synonym", "near_synonym", "antonym", "polarity_pair"):
            return 2.0
        # looser neighbours count only inside the small standing scopes: the focus ayah itself and the Fatiha
        return 1.0 if sub == "thematic" or e["b"].startswith(("F:", "A:1:")) else 0
    if k == "lex":
        return {"contrast": 2.5, "image": 2.0, "src-rare": 1.5}.get(sub, 1.0 if e["b"].startswith("F:") else 0)
    if k == "sound":
        return 2.0
    if k in ("frame", "form"):
        return 1.0
    return 0.0


def strong(e: dict) -> bool:
    return weight(e) > 0


def structures(net: Net) -> dict:
    N = net.nodes
    rare = {n for n, d in N.items() if d["type"] == "B" and d["rare"]}
    CORE = {"lex", "rel", "img", "sound"}

    def targets(b, strong_only=False):
        return {t for t, es in net.adj[b].items() if N[t]["type"] in "FA" and t != N[b]["word"]
                and any(strong(e) if strong_only else e["kind"] in CORE for e in es)}

    hubs = []
    for h, d in N.items():
        if d["type"] not in "FA":
            continue
        members = [b for b in rare if h in targets(b, strong_only=True)]
        best = defaultdict(float)
        for b in members:
            if not (d["type"] == "F" and N[b]["word"] == h):
                best[N[b]["root_id"]] = max(best[N[b]["root_id"]], max(weight(e) for e in net.adj[b][h]))
        if len(best) >= HUB_MIN:
            hubs.append((round(sum(best.values()), 1), h, members, len(best)))
    hubs.sort(key=lambda x: (N[x[1]]["type"] != "F", -x[0], x[1]))

    # triangles: a rare branch and two of its targets that are linked to each other (directly, or through another
    # branch of the target word by lex/rel — a "lifted" link), plus rare-rare-target triangles
    def linked(x, y):
        es = [e for e in net.adj[x].get(y, []) if e["kind"] in CORE | {"frame", "form"}]
        if es:
            return es
        for fx, ay in ((x, y), (y, x)):
            if N[fx]["type"] == "F" and N[ay]["type"] == "A":
                for b2, es2 in net.adj[ay].items():
                    if N[b2]["type"] == "B" and N[b2]["word"] == fx:
                        lifted = [e for e in es2 if e["kind"] in ("lex", "rel")]
                        if lifted:
                            return [dict(lifted[0], kind=f"{lifted[0]['kind']} (via {N[b2]['root']} {N[b2]['bid']})")]
        return []

    tris = []
    for b in rare:
        ts = sorted(targets(b))
        for x, y in itertools.combinations(ts, 2):
            xy = linked(x, y)
            if not xy:
                continue
            n_strong = sum((any(strong(e) for e in net.adj[b][x]), any(strong(e) for e in net.adj[b][y]),
                            any(strong(e) or " (via " in e["kind"] for e in xy)))
            if n_strong >= 2:
                kinds = {e["kind"] for e in net.adj[b][x]} | {e["kind"] for e in net.adj[b][y]} | {xy[0]["kind"].split()[0]}
                tris.append((len(kinds), b, x, y, xy[0]))
    tris.sort(key=lambda t: (-t[0], N[t[1]]["n_sources"], t[1]))

    conv = []
    for b in rare:
        kinds = {e["kind"] for es in net.adj[b].values() for e in es}
        ts = targets(b)
        if ts:
            conv.append((len(kinds & (CORE | {"hft"})), len(ts), b, sorted(kinds)))
    conv.sort(key=lambda c: (-c[0], -c[1], N[c[2]]["n_sources"]))

    hub_members = {h: set(m) for _, h, m, _n in hubs}
    bridges = []
    for n, d in N.items():
        if d["type"] not in "FA":
            continue
        touching = [h for h, ms in hub_members.items() if h != n and any(n in targets(b) for b in ms)]
        if len(touching) >= 2:
            bridges.append((n, touching))
    return {"hubs": hubs, "triangles": tris, "convergence": conv, "bridges": bridges, "targets": targets}


# ---------------------------------------------------------------- report

def label(net: Net, n: str) -> str:
    d = net.nodes[n]
    if d["type"] == "F":
        return f"{d['surface']} (w{d['w']})"
    if d["type"] == "A":
        return f"{d['ref']} [{d['zone']}]"
    if d["type"] == "B":
        flags = ("echo " if d["root_kind"] == "echo" else "") + ("plain" if d["plain"] else f"rare, {d['n_sources']} src"
                                                                 + (", sole" if d["sole"] else ""))
        return f"{d['root']} {d['bid']} «{d['gloss']}» {d['image']} ({flags}) @ {net.nodes[d['word']]['surface']}"
    return n


def ev(net: Net, a: str, b: str, kinds: set | None = None) -> str:
    out = []
    for e in net.adj[a][b]:
        if kinds is None or e["kind"] in kinds:
            out.append(f"{e['kind']}{'/' + e['sub'] if e['sub'] else ''}: {e['evidence']}")
    return "; ".join(dict.fromkeys(out))


def report(net: Net, meta: dict, st: dict) -> str:
    N = net.nodes
    kinds = Counter(e["kind"] for e in net.edges)
    rare_n = sum(1 for d in N.values() if d["type"] == "B" and d["rare"])
    L = [f"# Network for {meta['ref']} (img top-{meta['k']})", "",
         f"Nodes: {Counter(d['type'] for d in N.values())}; rare branches {rare_n}. Context zones: {dict(meta['zones'])}; "
         f"people anchors: {', '.join(f'{l} ({n} ayat)' for l, n in meta['anchors']) or '—'}.",
         f"Edges: {dict(kinds)}.", ""]
    targets = st["targets"]
    L += ["## Hubs (rare branches of ≥3 roots point here)", ""]
    shown, per_zone = [], Counter()
    for hub in st["hubs"]:  # focus-word hubs all; context hubs up to HUBS_PER_ZONE per zone (surah, people, inter …)
        z = "focus" if N[hub[1]]["type"] == "F" else N[hub[1]]["zone"]
        if z == "focus" or per_zone[z] < HUBS_PER_ZONE:
            per_zone[z] += 1
            shown.append(hub)
    st["shown"] = shown
    for score, h, members, n_roots in shown:
        L.append(f"### {label(net, h)} — {n_roots} roots, score {score}")
        if N[h]["type"] == "A":
            L.append(f"  {meta['words_of'].get(N[h]['ref'], '')}")
        for b in sorted(members, key=lambda b: (N[b]["root"], N[b]["bid"])):
            if N[h]["type"] == "F" and N[b]["word"] == h:
                continue
            L.append(f"- {label(net, b)} — {ev(net, b, h)}")
        L.append("")
    L += ["## Triangles (top 40)", ""]
    for nk, b, x, y, xy in st["triangles"][:40]:
        L.append(f"- [{nk} kinds] {label(net, b)}")
        L.append(f"  - → {label(net, x)}: {ev(net, b, x)}")
        L.append(f"  - → {label(net, y)}: {ev(net, b, y)}")
        L.append(f"  - {label(net, x)} ↔ {label(net, y)}: {xy['kind']}: {xy['evidence']}")
    L += ["", "## Convergence (rare branches by kinds of support; top 40)", ""]
    for nk, nt, b, ks in st["convergence"][:40]:
        L.append(f"- {nk} kinds, {nt} targets: {label(net, b)} — {', '.join(ks)}")
    L += ["", "## Bridges (linked to members of two or more hubs)", ""]
    for n, hs in st["bridges"]:
        L.append(f"- {label(net, n)} joins {', '.join(label(net, h) for h in hs)}")
    L += ["", "## Chain material (per hub: surah ayat its members touch, in surah order)", ""]
    for _, h, members, _n in st["hubs"][:8]:
        touch = defaultdict(set)
        for b in members:
            for t in targets(b):
                if N[t]["type"] == "A" and N[t]["zone"] == "surah":
                    touch[N[t]["ref"]].add(f"{N[b]['root']} {N[b]['bid']}")
        order = sorted(touch, key=lambda r: int(r.split(":")[1]))
        L.append(f"- {label(net, h)}: " + " → ".join(f"{r} ({', '.join(sorted(touch[r]))})" for r in order))
    L += ["", "## Formula groups (other ayat sharing ≥2 focus roots; leaves, not members)", ""]
    for keys, refs in sorted(meta["groups"].items(), key=lambda kv: (-len(kv[0]), -len(kv[1])))[:30]:
        L.append(f"- {' + '.join(P.spaced(k_) for k_ in keys)} ({len(refs)}): {', '.join(sorted(refs, key=lambda r: tuple(map(int, r.split(':'))))[:8])}")
    L += ["", "## HFT mechanisms and the hubs they touch", ""]
    hubsets = {h: set(m) | {h} for _, h, m, _n in st["shown"]}
    for m, d in N.items():
        if d["type"] != "M":
            continue
        steps = set(net.adj[m])
        touched = [label(net, h) for h, s in hubsets.items() if s & steps or any(h in net.adj[x] for x in steps)]
        L.append(f"- {m[2:]} [{d['kind']}] → {'; '.join(touched[:4]) or '—'}")
    return "\n".join(L) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ref")
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--out", default="")
    ap.add_argument("--inter", action="store_true", help="add the inter-ayah target ayat as a context zone")
    a = ap.parse_args()
    s, n = a.ref.split(":")
    out = Path(a.out) if a.out else V9 / "network" / "out" / f"{s}_{n}"
    out.mkdir(parents=True, exist_ok=True)
    net, meta = build(a.ref, a.k, a.inter)
    st = structures(net)
    tag = f"k{a.k}" + ("-inter" if a.inter else "")
    (out / f"network.{tag}.md").write_text(report(net, meta, st), encoding="utf-8")
    (out / f"network.{tag}.json").write_text(json.dumps(
        {"nodes": net.nodes, "edges": net.edges,
         "hubs": [(n_, h, m, r_) for n_, h, m, r_ in st["hubs"]],
         "triangles": [(k_, b, x, y) for k_, b, x, y, _ in st["triangles"]],
         "convergence": [(a_, b_, c_, d_) for a_, b_, c_, d_ in st["convergence"]]}, ensure_ascii=False), encoding="utf-8")
    print(f"{a.ref} k={a.k}: {len(net.nodes)} nodes, {len(net.edges)} edges, {len(st['hubs'])} hubs, "
          f"{len(st['triangles'])} triangles → {out}")


if __name__ == "__main__":
    main()
