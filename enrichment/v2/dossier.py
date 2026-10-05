#!/usr/bin/env python3
"""The dossier for a tool-free enrichment call (user, 2026-10-04 evening: "make enrichment much more cheap"): everything
the page agent used to fetch turn by turn, gathered once by script into one file, so the call is one input and one
output instead of ninety tool turns re-reading a growing context.

  python3 -B enrichment/v2/dossier.py --surah 1 --target 1:3            # work/s001/dossier/1_3.md, sizes printed

Sections, in order: the numbered base; the pack's ayah files (words, dictionary, usage, meals, turkish, sources) and
the errata candidates; the bound roots' pack files; every corpus segment tied to the ayah (all kinds, by kind then
source, each segment cut at --seg-chars with a note); the classical lexica entries of the bound roots; sahih hadith
and readings whose text holds the ayah's phrase (exact search); the schema card. Lines are wrapped so the Read tool
shows them whole. Locators appear as the corpus prints them (the agent cites only what is in the dossier).
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import textwrap
from collections import defaultdict
from pathlib import Path

V2 = Path(__file__).resolve().parent
sys.path.insert(0, str(V2 / "tools"))
sys.path.insert(0, str(V2))
import corpus as C  # noqa: E402

LEXICA = ["PROJE", "AYN", "JAMHARA", "TAHDHIB", "SIHAH", "MAQAYIS", "MUFRADAT", "LISAN", "ASAS", "FURUQ", "SAMIN-UMDA"]
KIND_ORDER = ["tafsir", "tafsir_tr", "maani", "wujuh", "ulum", "nazm", "isari", "qiraat", "hadith", "sira", "poetry",
              "modern", "reference", "meal", "translation", "quran", "lexicon"]
WRAP = 1800  # the Read tool truncates lines over 2000 characters


def wrap(text: str) -> str:
    out = []
    for line in text.splitlines():
        out += textwrap.wrap(line, WRAP, break_long_words=True, break_on_hyphens=False) or [""]
    return "\n".join(out)


def cut(text: str, n: int) -> str:
    return text if len(text) <= n else text[:n] + f" … [cut at {n} of {len(text)} characters]"


def seg_block(seg, head, text, extra, n) -> str:
    extra = json.loads(extra or "{}")
    flags = []
    if "sahih" in extra:
        flags.append(f"sahih={extra['sahih']} by={'|'.join(extra.get('graded_by') or []) or '-'}")
    if extra.get("page"):
        flags.append(f"page={extra['page']}")
    lines = [f"== {seg}" + (f"  [{head}]" if head else "") + ("  " + " ".join(flags) if flags else ""), cut(text, n)]
    for k in ("en", "tr", "notes"):
        if extra.get(k):
            lines.append(f"  {k}: {cut(str(extra[k]), n // 2)}")
    return "\n".join(lines)


def build(s: int, target: str, seg_chars: int, src_chars: int) -> Path:
    pk = V2 / "work" / f"s{s:03d}" / "pack"
    a = int(target.split(":")[1])
    tag = target.replace(":", "_")
    con = C.connect()
    parts: list[tuple[str, str]] = []
    sizes = {}
    # 1. the numbered base
    base = (pk / "numbered" / f"{tag}.md").read_text(encoding="utf-8")
    parts.append((f"THE BASE: PACK/numbered/{tag}.md (anchor every block by its [¶n])", base))
    # 2. the pack's ayah files and the errata candidates
    for name in ("words", "dictionary", "usage", "meals", "turkish", "sources"):
        f = pk / "ayah" / tag / f"{name}.md"
        if f.exists():
            parts.append((f"PACK/ayah/{tag}/{name}.md", f.read_text(encoding="utf-8")))
    ec = pk / "errata_candidates.json"
    if ec.exists():
        cands = [x for x in json.loads(ec.read_text(encoding="utf-8")) if str(x.get("file", "")).startswith(tag)]
        parts.append(("PACK/errata_candidates.json (this page's entries)", json.dumps(cands, ensure_ascii=False, indent=1)))
    # 3. the bound roots
    binding = json.loads((pk / "binding.json").read_text(encoding="utf-8"))
    roots = []
    for w in binding.get(target, []):
        for i in w.get("identity", []):
            if (i["root_id"], i["root"]) not in roots:
                roots.append((i["root_id"], i["root"]))
    for rid, root in roots:
        f = pk / "roots" / f"{rid}.md"
        if f.exists():
            parts.append((f"PACK/roots/{rid}.md ({root})", cut(f.read_text(encoding="utf-8"), src_chars)))
    # 4. every corpus segment tied to the ayah
    rows = con.execute("SELECT seg.seg, seg.src, src.kind, seg.head, seg.text, seg.extra FROM seg JOIN src ON src.id=seg.src "
                       "WHERE seg.s=? AND seg.a<=? AND coalesce(seg.a_end, seg.a)>=? ORDER BY src.kind, seg.src, seg.a",
                       (s, a, a)).fetchall()
    by_kind: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for seg, src, kind, head, text, extra in rows:
        by_kind[kind][src].append((seg, head, text, extra))
    cut_notes = []
    for kind in sorted(by_kind, key=lambda k: KIND_ORDER.index(k) if k in KIND_ORDER else 99):
        blocks = []
        for src, segs in by_kind[kind].items():
            used = 0
            for seg, head, text, extra in segs:
                if used >= src_chars:
                    cut_notes.append(f"{src}: {len(segs)} segments, shown up to {src_chars} characters; the rest is in the corpus")
                    blocks.append(f"== {seg}  [not shown: {src} is over the per-source limit; {len(text)} characters]")
                    continue
                blocks.append(seg_block(seg, head, text, extra, seg_chars))
                used += min(len(text), seg_chars)
        parts.append((f"CORPUS, kind {kind}: every segment tied to {target} ({sum(len(v) for v in by_kind[kind].values())})",
                      "\n\n".join(blocks)))
    # 5. the lexica by root key
    blocks = []
    for rid, root in roots:
        key = root.replace(" ", "")
        for lex in LEXICA:
            for r in con.execute("SELECT seg, head, text, extra FROM seg WHERE src=? AND (seg=? OR seg LIKE ?) LIMIT 3",
                                 (lex, f"{lex}:{key}", f"{lex}:{key}#%")).fetchall():
                blocks.append(seg_block(r[0], r[1], r[2], r[3], seg_chars))
    if blocks:
        parts.append((f"LEXICA: entries of the bound roots ({', '.join(r for _, r in roots)})", "\n\n".join(blocks)))
    # 6. sahih hadith and readings holding the ayah's phrase
    ayah_text = con.execute("SELECT text FROM seg WHERE src='QURAN' AND s=? AND a=?", (s, a)).fetchone()
    if ayah_text:
        words = C.norm(ayah_text[0]).split()
        phrase = " ".join(f'"{w}"' for w in words)
        for kind, extra_sql, label in (("hadith", " AND json_extract(seg.extra,'$.sahih')=1", "SAHIH HADITH"),
                                       ("qiraat", "", "READINGS")):
            rs = con.execute("SELECT seg.seg, seg.head, seg.text, seg.extra FROM f JOIN seg ON seg.id=f.rowid WHERE f MATCH ? "
                             "AND seg.src IN (SELECT id FROM src WHERE kind=?)" + extra_sql + " ORDER BY rank LIMIT 20",
                             (phrase, kind)).fetchall()
            if rs:
                parts.append((f"{label} whose text holds the ayah's words (exact search, {len(rs)} shown, each cut at 1500)",
                              "\n\n".join(seg_block(*r, 1500) for r in rs)))
    # 7. the schema card
    parts.append(("SCHEMA_CARD.md", (V2 / "SCHEMA_CARD.md").read_text(encoding="utf-8")))
    out = []
    for title, body in parts:
        out.append(f"\n\n===== {title} =====\n\n{wrap(body.rstrip())}\n")
        sizes[title] = len(body)
    text = f"# Dossier for {target} (surah {s}), built by script from the pack and the corpus index\n" + "".join(out)
    d = V2 / "work" / f"s{s:03d}" / "dossier"
    d.mkdir(parents=True, exist_ok=True)
    f = d / f"{tag}.md"
    f.write_text(text, encoding="utf-8")
    for note in dict.fromkeys(cut_notes):
        print(f"NOTE: {note}")
    for title, n in sizes.items():
        print(f"  {n:>8,}  {title[:90]}")
    print(f"{f.relative_to(V2.parents[1])}: {len(text):,} characters, ~{len(text) // 3:,} tokens")
    return f


# ---------------------------------------------------------------- the bounded extract (mode dosya2, user 2026-10-05)
# The order of zengin.md Step 3: transmitted tafsir, then analytical, Turkish, allusive; then the other kinds; a
# source's -FULL edition after every short one. Within the budget a segment is shown whole up to WHOLE characters,
# a longer one by its opening (the rest by `corpus.py get LOC --from N`); past the budget every remaining segment is
# listed by locator and size. Every cut is printed and recorded in the extract's own header.
ORDER = ["TAB", "IBNKATHIR", "DURR", "BAGHAWI", "MUQATIL", "MUJAHID", "ABDURRAZZAQ", "IBNABIHATIM", "YAHYA-SALLAM",
         "KASHSHAF", "RAZI", "BAYDAWI", "NASAFI", "QURTUBI", "IBNATIYYA", "ABUHAYYAN", "ALUSI", "MAWARDI", "IBNASHUR",
         "TABRISI", "BIQAI", "ELMALILI", "KURANYOLU-TEFSIR", "QUSHAYRI", "SULAMI", "TUSTARI", "BURSEVI", "ABDUH-AMMA",
         "TABATABAI", "WAHIDI-BASIT", "SAMIN-DURR", "MAJAZ", "FARRA", "ZAJJAJ", "AKHFASH", "IBNQUTAYBA-GHARIB", "NAHHAS"]
KIND_RANK = ["tafsir", "tafsir_tr", "maani", "qiraat", "wujuh", "isari", "nazm", "ulum", "hadith", "sira", "poetry",
             "modern", "reference", "lexicon"]
SKIP_KINDS = {"meal": "the panel is in PACK meals.md; other meals by corpus.py get",
              "translation": "ASAD-EN and ARBERRY are in PACK meals.md", "quran": "the ayah text is in PACK words.md"}


def bounded(s: int, target: str, budget: int = 150_000, per_source: int = 5_000) -> tuple[str, dict]:
    """(extract text, record): every segment tied to the ayah, sources in rank order, each source shown up to
    per_source characters (its segments in order; the one crossing the share is cut, with the command for the rest),
    until the budget; every segment not shown is listed by locator and size."""
    con = C.connect()
    a = int(target.split(":")[1])
    rows = con.execute("SELECT seg.seg, seg.src, src.kind, seg.head, seg.text, seg.extra FROM seg JOIN src ON "
                       "src.id=seg.src WHERE seg.s=? AND seg.a<=? AND coalesce(seg.a_end, seg.a)>=? ORDER BY seg.id",
                       (s, a, a)).fetchall()

    def rank(src, kind):
        full = src.endswith("-FULL")
        base = src[:-5] if full else src
        return (full, ORDER.index(base) if base in ORDER else len(ORDER),
                KIND_RANK.index(kind) if kind in KIND_RANK else len(KIND_RANK), src)
    skipped = {k: [r[0] for r in rows if r[2] == k] for k in SKIP_KINDS}
    by_src: dict[str, list] = {}
    for r in rows:
        if r[2] not in SKIP_KINDS:
            by_src.setdefault(r[1], []).append(r)
    used, whole, cut_segs, listed = 0, 0, [], []
    blocks, index = [], []
    for src in sorted(by_src, key=lambda x: rank(x, by_src[x][0][2])):
        share = 0
        for seg, _, kind, head, text, extra in by_src[src]:
            text = text or ""
            room = min(per_source - share, budget - used)
            if room <= 0:
                index.append(f"- {seg} ({kind}, {len(text):,} chars)")
                listed.append(seg)
                continue
            body = text[:room]
            note = "" if len(body) == len(text) else (f"[shown {len(body):,} of {len(text):,} characters; the rest: "
                                                      f"corpus.py get {seg} --from {len(body)}]")
            blocks.append(seg_block(seg, head, body, extra, len(body) + 1) + (f"\n{note}" if note else ""))
            (cut_segs.append(seg) if note else None)
            whole += not note
            share += len(body)
            used += len(body)
    for k, segs in skipped.items():
        if segs:
            print(f"NOTE: {len(segs)} {k} segments not in the extract: {SKIP_KINDS[k]}")
    rec = {"target": target, "budget": budget, "per_source": per_source, "chars_shown": used, "segments_whole": whole,
           "segments_cut": cut_segs, "segments_listed_only": listed, "sources": len(by_src),
           "skipped_kinds": {k: len(v) for k, v in skipped.items()}}
    head = (f"# Corpus extract for {target}: every segment tied to the ayah, sources ranked (zengin.md Step 3 order; "
            f"short editions before -FULL), each source up to {per_source:,} characters, {budget:,} in all\n\n"
            f"{whole} segments whole, {len(cut_segs)} cut (each says how to get the rest), {len(listed)} not shown "
            f"(listed at the end by locator and size). Meals, translations and the Qur'an text are in the pack files.\n")
    text = head + "\n\n".join(blocks) + ("\n\n## Not shown (locator, kind, size): fetch with corpus.py get\n"
                                          + "\n".join(index) if index else "")
    print(f"extract {target}: {used:,} characters shown from {len(by_src)} sources ({whole} segments whole, "
          f"{len(cut_segs)} cut), {len(listed)} segments listed only")
    return wrap(text), rec


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--target", required=True, help="S:A (ayah pages only)")
    ap.add_argument("--seg-chars", type=int, default=3000)
    ap.add_argument("--src-chars", type=int, default=24000)
    a = ap.parse_args()
    if ":" not in a.target:
        raise SystemExit("the dossier mode is for ayah pages (--target S:A)")
    build(a.surah, a.target, a.seg_chars, a.src_chars)


if __name__ == "__main__":
    main()
