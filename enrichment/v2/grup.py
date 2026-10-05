#!/usr/bin/env python3
"""The hybrid enrichment workflow (HYBRID_PLAN.md Task C; user, 2026-10-05: "many passes … group by tradition …
small-enough groups per agent … each enrichment block is an independent unit, attached to the correct frozen v16
prose"). Every source is read by the group that claims it (groups.json); a group's material for a surah is packed
into balanced units of at most about `budget_chars`; one agent per unit reads a digest of the pages its material
concerns plus the material, writes records for those pages and accounts for every material segment in kapsam.jsonl.
Units are independent: a page's blocks are the union of all units' kept records (merge). The project dictionary and
the lexica are not read (groups.json not_read: the base was written from them).

  python3 -B enrichment/v2/grup.py plan    --surah 1 [--group G] [--write]   units and material (no model call)
  python3 -B enrichment/v2/grup.py prepare --surah 1 --unit U|all --model astra|opus [--effort high]
  python3 -B enrichment/v2/grup.py finish  --surah 1 --unit U --model astra [--effort high]   after the run
  python3 -B enrichment/v2/grup.py merge   --surah 1                  pages from all finished units (work dir only)
  python3 -B enrichment/v2/grup.py status  --surah 1

`prepare` writes a unit's call directory work/sNNN/grup/<unit>.<model>.<effort>/ (prompt.md, digest.*.md,
material.*.md, started.json). An Astra unit is run by the user (e.g. `codex exec` with the directory as its working
directory and prompt.md as the prompt); an Opus unit gets spawn.md for the orchestrating session. The agent writes
records.<page>[.n].jsonl, kapsam.jsonl and gaps.json there; `finish` adds check.json and run.log.json. Merged pages
go to work/sNNN/grup/pages/ (never out/: acceptance is the user's). No model is ever called by this script.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sqlite3
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

V2 = Path(__file__).resolve().parent
PG = V2.parents[1]
sys.path.insert(0, str(V2 / "tools"))
sys.path.insert(0, str(V2))
sys.path.insert(0, str(PG / "_commentary" / "v16"))
import corpus as C  # noqa: E402
import render as R  # noqa: E402
import validate as VAL  # noqa: E402
import agentrun as AR  # noqa: E402

WORK = V2 / "work"
PROMPTS = V2 / "prompts"
LEDGER = WORK / "ledger.jsonl"
GROUPS = json.loads((V2 / "groups.json").read_text(encoding="utf-8"))
MODELS = {"astra": "gpt-6-astra", "opus": "claude-opus-5-5"}
FILE_CHARS = 24_000      # one material/digest file: one Read (the Read tool shows at most 25,000 tokens)
WRAP = 1_900             # longer lines are broken at a space (the Read tool cuts a line at 2,000 characters)
OVERFLOW = 1.15          # a balanced unit may exceed its share by this much to end at a page boundary
SEARCH_TOP = 6           # hits kept per (query, source) for search groups
COMMON_HITS = 150        # a phrase with more hits than this in one source is too common there (recorded)
RARE_WORD = 25           # a single word is searched in a source only if it occurs at most this often there
# what each search group looks for: phrase = the ayah's three-word sequences that hold a content word (a passage
# quoting the ayah); phrase+names = those and the ayah's proper names; words = its rare content words
SEARCH_MODE = {"hadis": "phrase", "icaz-belagat": "phrase", "siyer-tarih": "phrase+names", "siir-sahid": "words",
               "vucuh": "words"}
SEARCH_TOP_BY = {"siir-sahid": 3, "vucuh": 4}
CONTENT_POS = {"N", "V", "ADJ"}
NOT_CONTENT = {"الله", "لله", "بالله"}   # «ما شاء الله», «بسم الله الرحمن»: formulae found everywhere
DIGEST_HEAD, DIGEST_TAIL = 24, 10   # words of a paragraph shown in the digest (head … tail)
# an Opus-rate estimate for comparing units (uncalibrated; Astra runs on the subscription)
RATE = {"write": 5.0, "read": 0.20, "output": 20.0}
HARNESS_TOK, TURNS, THINK_TOK, REC_TOK = 5_300, 6, 15_000, 4_000
CONTEXT_WARN = 200_000   # a unit that starts above this many tokens is printed


def wd(s: int) -> Path:
    return WORK / f"s{s:03d}"


def gdir(s: int) -> Path:
    return wd(s) / "grup"


def tag(page: str) -> str:
    return "surah" if page == "surah" else page.replace(":", "_")


def est_tokens(text: str) -> int:
    ar = sum(1 for ch in text if "؀" <= ch <= "ۿ")
    return int(ar / 1.3 + (len(text) - ar) / 2.0)


def is_arabic(text: str) -> bool:
    t = text[:2000]
    return sum(1 for ch in t if "؀" <= ch <= "ۿ") > 0.3 * max(1, len(t))


def log(row: dict) -> None:
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def rel(p: Path) -> str:
    return str(p.relative_to(PG)) if p.is_relative_to(PG) else str(p)


# ---------------------------------------------------------------- pages and digests

def pages(s: int) -> list[str]:
    n = json.loads((wd(s) / "pack" / "pack.json").read_text(encoding="utf-8"))["ayat"]
    return [p for p in ["surah"] + [f"{s}:{a}" for a in range(1, n + 1)]
            if (wd(s) / "pack" / "numbered" / f"{tag(p)}.md").exists()]


TAG = re.compile(r"\{ar:[^{}]*?(?:source:([^,}]+))?\}")


def digest(s: int, page: str) -> str:
    """A page's numbered base in short: each paragraph cut to its first DIGEST_HEAD and last DIGEST_TAIL words, the
    Arabic citation tags shortened to their source («{ar… 11:41}»), headings, paragraph numbers and v16 addition
    markers kept. Anchoring needs only ¶n and three consecutive words of the paragraph as printed; the agent reads a
    whole paragraph from PACK/numbered/<page>.md when the point needs more than the digest shows."""
    text = (wd(s) / "pack" / "numbered" / f"{tag(page)}.md").read_text(encoding="utf-8")
    out = [f"# Digest of {page} — full text: PACK/numbered/{tag(page)}.md (… marks words left out; «{{ar… S:A}}» a "
           f"shortened Arabic citation tag)", ""]
    for para in re.split(r"\n\s*\n", text):
        p = para.strip()
        if not p:
            continue
        p = TAG.sub(lambda m: "{ar… " + (m.group(1) or "").strip() + "}", p)
        w = p.split()
        if p.startswith("#") or len(w) <= DIGEST_HEAD + DIGEST_TAIL + 6:
            out.append(p)
        else:
            out.append(" ".join(w[:DIGEST_HEAD]) + f" … [{len(w) - DIGEST_HEAD - DIGEST_TAIL} words] … "
                       + " ".join(w[-DIGEST_TAIL:]))
        out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------- material

SEG_COLS = "seg.seg,seg.src,seg.s,seg.a,seg.a_end,seg.head,seg.text,seg.extra"


def item_text(row, pgs: list[str], note: str = "") -> str:
    """One segment as the agent reads it: `### <locator> [tie] → <page(s)>`, flags, an optional note line, the text.
    Translations (en, tr) are left out when the segment's own text is Arabic (the hadith collections carry both,
    each as long as the Arabic); notes are kept."""
    seg, src, rs, a, a_end, head, text, extra = row
    extra = json.loads(extra or "{}")
    flags = []
    if extra.get("text_status"):
        flags.append(f"STATUS: {extra['text_status']}")
    if extra.get("marker_found") is False:
        flags.append("note marker not found: tie approximate")
    if extra.get("align_uncertain"):
        flags.append("verse alignment uncertain")
    if "sahih" in extra:
        flags.append(f"sahih={extra['sahih']}")
    span = (f"{rs}:{a}" + (f"-{a_end}" if a_end and a_end != a else "") if a else f"{rs}") if rs else "untied"
    lines = [f"### {seg}  [{span}] → {' | '.join(pgs)}" + (f"  {head}" if head else "")
             + ("  {" + "; ".join(flags) + "}" if flags else "")]
    if note:
        lines.append(note)
    lines.append((text or "").strip())
    arabic = is_arabic(text or "")
    for k in ("notes",) if arabic else ("en", "tr", "notes"):
        if extra.get(k):
            lines.append(f"{k}: {C.flat(extra[k])}")
    return "\n".join(lines) + "\n"


def item(row, page: str, extra_pages: list[str] | None = None, note: str = "") -> dict:
    pgs = [page] + [p for p in (extra_pages or []) if p != page]
    text = item_text(row, pgs, note)
    return {"seg": row[0], "src": row[1], "page": page, "pages": pgs, "chars": len(text), "text": text}


def cited_ayat(con, s: int, seg: str) -> list[int]:
    out = set()
    for a, b in con.execute("SELECT ref.a, ref.a_end FROM ref JOIN seg ON seg.id=ref.seg_id WHERE seg.seg=? AND ref.s=?",
                            (seg, s)):
        if a:
            out.update(range(a, (b or a) + 1))
    return sorted(out)


def ayah_items(con, s: int, srcs: list[str], valid: set[str]) -> tuple[list[dict], list[str]]:
    """Segments of the group's sources tied to the surah: a tie of up to 3 ayat goes to its first ayah's page; a wider
    or surah-level tie to the surah page, and also to the page of each ayah it cites when it cites at most three (the
    agent places the point). Duplicates (extra.duplicate; a FULL-edition segment at least 80% inside the short
    edition) are listed, not read."""
    q = f"SELECT {SEG_COLS} FROM seg WHERE s=? AND src IN ({','.join('?' * len(srcs))}) ORDER BY src, a, id"
    items, dups = [], []
    rows = con.execute(q, [s] + srcs).fetchall()
    short_text: dict[str, set] = {}
    for r in rows:
        if r[1] + "-FULL" in srcs:
            short_text.setdefault(r[1], set()).update(grams5(r[6] or ""))
    for row in rows:
        extra = json.loads(row[7] or "{}")
        if extra.get("duplicate"):
            dups.append(row[0])
            continue
        base = row[1][:-5] if row[1].endswith("-FULL") else None
        if base and base in short_text:
            g5 = grams5(row[6] or "")
            if g5 and len(g5 & short_text[base]) / len(g5) >= 0.8:
                dups.append(f"{row[0]} (in {base})")
                continue
        a, b = row[3], row[4] or row[3]
        if a and b - a <= 2 and f"{s}:{a}" in valid:
            items.append(item(row, f"{s}:{a}"))
            continue
        cites = cited_ayat(con, s, row[0])
        extra_pages = [f"{s}:{x}" for x in cites if f"{s}:{x}" in valid] if len(cites) <= 3 else []
        items.append(item(row, "surah", extra_pages))
    return items, dups


def grams5(text: str) -> set:
    t = re.sub(r"[^ء-ي]", "", C.norm(text))
    return {t[i:i + 5] for i in range(len(t) - 4)}


def cites_items(con, s: int, srcs: list[str], valid: set[str], skip: set[str] = frozenset(),
                untied_only: bool = False) -> list[dict]:
    """Segments of the group's sources that cite ayat of the surah (the ref table), excerpted around the citations:
    to the page of the ayah they cite, or the surah page (and, for two or three ayat, their pages too) when they cite
    several. Segments in `skip` (already read as tied material) are left out; untied_only: only segments tied to no
    ayah at all (an ayah group's essays, introductions and appendices that cite the surah)."""
    q = (f"SELECT {SEG_COLS},ref.a,ref.a_end FROM ref JOIN seg ON seg.id=ref.seg_id WHERE ref.s=? AND seg.src IN "
         f"({','.join('?' * len(srcs))})" + (" AND seg.s IS NULL" if untied_only else "") + " ORDER BY seg.id")
    by: dict[str, dict] = {}
    for r in con.execute(q, [s] + srcs):
        if r[0] in skip:
            continue
        x = by.setdefault(r[0], {"row": r[:8], "ayat": set()})
        if r[8]:
            x["ayat"].update(range(r[8], (r[9] or r[8]) + 1))
    out = []
    for seg, x in by.items():
        ay = sorted(x["ayat"])
        page = f"{s}:{ay[0]}" if len(ay) == 1 and f"{s}:{ay[0]}" in valid else "surah"
        row = list(x["row"])
        full = row[6] or ""
        text = excerpt(full, s, ay)
        if len(text) < len(full):
            row[6] = text + f"\n[excerpt around the citations: {len(text):,} of {len(full):,} characters; the whole " \
                            f"segment: corpus.py get {seg}]"
        extra_pages = [f"{s}:{x}" for x in ay if f"{s}:{x}" in valid] if page == "surah" and len(ay) <= 3 else []
        out.append(item(tuple(row), page, extra_pages, note=f"(cites {s}:{','.join(map(str, ay))})"))
    return out


def excerpt(text: str, s: int, ayat: list[int], half: int = 1200) -> str:
    """The parts of a reference page around its citations of the surah (± half characters each, merged), with the
    gaps marked; the whole page when the windows cover most of it."""
    spans = []
    for m in re.finditer(rf"(?<![\d:]){s}\s?:\s?(\d{{1,3}})", text):
        spans.append((max(0, m.start() - half), min(len(text), m.end() + half)))
    if not spans:
        return text
    spans.sort()
    merged = [list(spans[0])]
    for a, b in spans[1:]:
        if a <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    if sum(b - a for a, b in merged) > 0.8 * len(text):
        return text
    parts = []
    for a, b in merged:
        parts.append(("… " if a > 0 else "") + text[a:b] + (" …" if b < len(text) else ""))
    return "\n[…]\n".join(parts)


def binding(s: int) -> dict:
    return json.loads((wd(s) / "pack" / "binding.json").read_text(encoding="utf-8"))


def bare(surface: str) -> str:
    return C.norm(re.sub(r"[ًٌٍَُِّْٰٓ]", "", surface or "")).strip()


def search_items(con, s: int, srcs: list[str], mode: str, top: int, sahih: bool,
                 valid: set[str]) -> tuple[list[dict], list[dict]]:
    """Script-run searches (HYBRID_PLAN C8), every query recorded with its hits per source, what was kept, and why a
    query or a source was skipped. phrase: the ayah's three-word sequences that hold a content word (not a formula
    of function words and «الله»); words: its content words (N, V, ADJ; a source where the word occurs more than
    RARE_WORD times is skipped there); names: its proper names. `top` hits kept per (query, source)."""
    quran = {a: t for a, t in con.execute("SELECT a, text FROM seg WHERE src='QURAN' AND s=?", (s,))}
    queries, items, seen = [], [], {}
    for ref, words in sorted(binding(s).items(), key=lambda x: int(x[0].split(":")[1])):
        a = int(ref.split(":")[1])
        aw = C.norm(quran.get(a, "")).split()
        content = {bare(w.get("surface")) for w in words
                   if set((w.get("pos") or "").split(";")) & CONTENT_POS} - NOT_CONTENT
        terms, skipped = [], []
        if mode.startswith("phrase"):
            seqs = [" ".join(aw[i:i + 3]) for i in range(len(aw) - 2)] if len(aw) >= 3 else ([" ".join(aw)] if aw else [])
            for q in seqs:
                (terms.append(("phrase", q)) if set(q.split()) & content else skipped.append(q))
        for w in words:
            pos = set((w.get("pos") or "").split(";"))
            surface = bare(w.get("surface"))
            if len(surface) < 3 or surface in NOT_CONTENT:
                continue
            if (mode == "words" and pos & CONTENT_POS) or (mode == "phrase+names" and "PN" in pos):
                terms.append(("word", surface))
        if skipped:
            queries.append({"ayah": ref, "kind": "phrase", "skipped": skipped, "reason": "no content word (formula)"})
        seen_terms: set = set()
        for kind, term in [x for x in terms if not (x[1] in seen_terms or seen_terms.add(x[1]))]:
            fq = f'"{term}"'
            rec = {"ayah": ref, "kind": kind, "query": term, "hits": {}, "kept": {}, "too_common_in": []}
            for sid in srcs:
                n = con.execute("SELECT count(*) FROM f JOIN seg ON seg.id=f.rowid WHERE f MATCH ? AND seg.src=?"
                                + (" AND json_extract(seg.extra,'$.sahih')=1" if sahih else ""), (fq, sid)).fetchone()[0]
                if not n:
                    continue
                rec["hits"][sid] = n
                if n > (RARE_WORD if kind == "word" else COMMON_HITS):  # too frequent to point at this ayah: recorded
                    rec["too_common_in"].append(sid)
                    continue
                sql = (f"SELECT {SEG_COLS} FROM f JOIN seg ON seg.id=f.rowid WHERE f MATCH ? AND seg.src=?"
                       + (" AND json_extract(seg.extra,'$.sahih')=1" if sahih else "") + " ORDER BY rank LIMIT ?")
                k = 0
                for r in con.execute(sql, (fq, sid, top)):
                    k += 1
                    pg = ref if ref in valid else "surah"
                    if r[0] in seen:  # found again for another ayah: the item names every ayah it was found for
                        old = seen[r[0]]
                        if pg not in old["pages"] or term not in old["terms"]:
                            old["terms"].append(term)
                            old["pages"] += [pg] if pg not in old["pages"] else []
                            old["item"].update(item(r, old["pages"][0], old["pages"][1:], note="(found by " + ", ".join(
                                f"«{x}»" for x in old["terms"]) + f", for {' | '.join(old['pages'])})"))
                        continue
                    it = item(r, pg, note=f"(found by «{term}», for {ref})")
                    seen[r[0]] = {"item": it, "pages": [pg], "terms": [term]}
                    items.append(it)
                rec["kept"][sid] = k
            queries.append(rec)
    return items, queries


def search_summary(queries: list[dict]) -> dict:
    """What the searches left out, for the plan printout: formula phrases skipped, (query, source) pairs too common
    to search, and pairs whose hits were cut to the kept number."""
    out = {"queries": sum(1 for q in queries if "query" in q),
           "skipped_formulae": sum(len(q["skipped"]) for q in queries if "skipped" in q),
           "too_common": [], "capped": []}
    for q in queries:
        for sid in q.get("too_common_in", []):
            out["too_common"].append((q["query"], sid, q["hits"][sid]))
        for sid, k in q.get("kept", {}).items():
            if q["hits"][sid] > k:
                out["capped"].append((q["query"], sid, q["hits"][sid], k))
    return out


def pack_items(s: int, files: tuple, stem: str) -> list[dict]:
    """Per-ayah pack files as material: words.md + meals.md (meal) or turkish.md (turkce-sozluk)."""
    out = []
    for p in pages(s):
        if p == "surah":
            continue
        d = wd(s) / "pack" / "ayah" / tag(p)
        text = "\n".join((d / n).read_text(encoding="utf-8") for n in files if (d / n).exists())
        if not text.strip():
            continue
        text = f"### {stem}:{p}  [{p}] → {p}\n{text}\n"
        out.append({"seg": f"{stem}:{p}", "src": "pack", "page": p, "pages": [p], "chars": len(text), "text": text})
    return out


def group_items(con, s: int, g: dict, held: list[str]) -> tuple[list[dict], dict]:
    """A group's material for the surah (the same call at plan and at prepare) and what the plan records about it."""
    gid, mat = g["id"], g.get("material")
    valid = set(pages(s))
    info: dict = {}
    if mat in ("ayah", "cites", "search") and not held and gid != "turkce-sozluk":
        return [], {"unit_note": "none of the group's sources is held"}
    if mat == "ayah":
        items, info["duplicates_listed_not_read"] = ayah_items(con, s, held, valid)
        got = {i["seg"] for i in items} | {d.split(" ")[0] for d in info["duplicates_listed_not_read"]}
        # cites: true reads every segment that cites the surah; otherwise only those tied to no ayah anywhere (an
        # essay or appendix of a per-verse source), which no tie can ever bring in
        more = cites_items(con, s, held, valid, got, untied_only=not g.get("cites"))
        if more:
            info["citing_segments"] = len(more)
            items += more
        # a held source with no ayah tie anywhere is reached by phrase search, never declared empty
        tied = {r[0] for r in con.execute(f"SELECT DISTINCT src FROM seg WHERE s IS NOT NULL AND src IN "
                                          f"({','.join('?' * len(held))})", held)} if held else set()
        untied = [x for x in held if x not in tied]
        if untied:
            info["untied_sources"] = untied
            got = {i["seg"] for i in items}
            more, q = search_items(con, s, untied, "phrase", SEARCH_TOP, False, valid)
            items += [i for i in more if i["seg"] not in got]
            info["queries"] = q
    elif mat == "cites":
        items = cites_items(con, s, held, valid)
    elif mat == "search" and gid == "turkce-sozluk":
        items = pack_items(s, ("turkish.md",), "turkish")
        info["read_through"] = "the pack's turkish.md per ayah (the Turkish dictionaries' entries for the meals' key words)"
    elif mat == "search":
        items, info["queries"] = search_items(con, s, held, SEARCH_MODE.get(gid, "phrase"),
                                              SEARCH_TOP_BY.get(gid, SEARCH_TOP), gid == "hadis", valid)
    elif mat == "meal":
        items = pack_items(s, ("words.md", "meals.md"), "meals")
    elif mat == "none":
        items = []
    else:
        raise SystemExit(f"group {gid}: unknown material {mat!r}")
    return items, info


# ---------------------------------------------------------------- plan

def pack_units(items: list[dict], budget: int, page_order: list[str], whole: bool) -> list[list[dict]]:
    """Items in page order, split into n = ⌈total / budget⌉ balanced units; a unit ends at a page boundary once it
    holds its share, or mid-page only when it would exceed its share by more than OVERFLOW. whole: one unit."""
    order = {p: i for i, p in enumerate(page_order)}
    items = sorted(items, key=lambda x: (order.get(x["page"], 999), x["src"], x["seg"]))
    total = sum(i["chars"] for i in items)
    if whole or total <= budget:
        return [items] if items else []
    share = total / math.ceil(total / budget)
    units, cur, n = [], [], 0
    for it in items:
        if cur and (n + it["chars"] > share * OVERFLOW or (n >= share and it["page"] != cur[-1]["page"])):
            units.append(cur)
            cur, n = [], 0
        cur.append(it)
        n += it["chars"]
    if cur:
        units.append(cur)
    return units


def unit_cost(material_tok: int, digest_tok: int, brief_tok: int) -> dict:
    ctx = HARNESS_TOK + brief_tok + digest_tok + material_tok
    out_tok = REC_TOK + THINK_TOK + int(0.08 * material_tok)
    usd = (RATE["write"] * (ctx + out_tok) + RATE["read"] * TURNS * (ctx + out_tok / 2) + RATE["output"] * out_tok) / 1e6
    return {"context_tok": ctx, "output_tok": out_tok, "usd": round(usd, 2)}


def brief_tokens(gid: str) -> int:
    text = "".join((PROMPTS / n).read_text(encoding="utf-8") for n in ("grup.md", f"grup_{gid}.md")
                   if (PROMPTS / n).exists())
    return est_tokens(text + (V2 / "SCHEMA_CARD.md").read_text(encoding="utf-8")) + 600


def held_sources() -> set[str]:
    con = sqlite3.connect(f"file:{C.INDEX}?mode=ro", uri=True)
    return {r[0] for r in con.execute("SELECT id FROM src WHERE access!='hafiza'")}


def index_stamp() -> str:
    st = Path(C.INDEX).stat()
    return f"{st.st_size}:{int(st.st_mtime)}"


def plan(s: int, only: str | None = None) -> tuple[dict, dict]:
    con = sqlite3.connect(f"file:{C.INDEX}?mode=ro", uri=True)
    pg = pages(s)
    if "surah" not in pg:
        raise SystemExit(f"S{s}: no numbered surah page in the pack (PACK/numbered/surah.md): build the pack first")
    budget = GROUPS["budget_chars"]
    dig = {p: digest(s, p) for p in pg}
    have = held_sources()
    out = {"surah": s, "planned": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "budget_chars": budget, "pages": pg,
           "pack_sha256": hashlib.sha256((wd(s) / "pack" / "pack.json").read_bytes()).hexdigest(),
           "index": index_stamp(), "not_read": GROUPS.get("not_read", []), "groups": {}, "units": []}
    for g in GROUPS["groups"]:
        gid, mat, srcs = g["id"], g.get("material"), list(g["sources"])
        if only and gid != only:
            continue
        held = [x for x in srcs if x in have]
        items, info = group_items(con, s, g, held)
        rec = {"material": mat, "sources": srcs, "held": held, "pointers": [x for x in srcs if x not in held],
               "required": bool(g.get("required")), "whole_surah": g.get("unit") == "surah", **info}
        rec["items"] = len(items)
        rec["chars"] = sum(i["chars"] for i in items)
        rec["by_source"] = dict(Counter(i["src"] for i in items))
        dup_srcs = {d.split(":")[0] for d in info.get("duplicates_listed_not_read", [])}
        rec["no_material_sources"] = [x for x in held if x not in rec["by_source"] and x not in dup_srcs] \
            if mat in ("ayah", "cites", "search") and not info.get("read_through") else []
        rec["duplicate_only_sources"] = [x for x in held if x not in rec["by_source"] and x in dup_srcs]
        if mat == "none":
            groups_units = [[]]
        else:
            groups_units = pack_units(items, budget, pg, g.get("unit") == "surah")
            if not items:
                rec["unit_note"] = "no material for this surah: no unit"
        bt = brief_tokens(gid)
        covered_all: set = set()
        for k, us in enumerate(groups_units, 1):
            covered = {p for i in us for p in i["pages"]}
            if mat in ("none", "meal"):
                covered |= set(pg)
            covered = sorted(covered, key=pg.index)
            covered_all |= set(covered)
            mat_tok = sum(est_tokens(i["text"]) for i in us)
            dig_tok = sum(est_tokens(dig[p]) for p in covered)
            if g.get("unit") == "surah" and sum(i["chars"] for i in us) > 2 * budget:
                print(f"WARNING: {gid}: one whole-surah unit holds {sum(i['chars'] for i in us):,} characters "
                      f"(over twice the budget {budget:,})")
            cost = unit_cost(mat_tok, dig_tok, bt)
            if cost["context_tok"] > CONTEXT_WARN:
                print(f"WARNING: {gid}.u{k:02d}: starts at ~{cost['context_tok']:,} tokens of context ({len(covered)} "
                      f"page digests {dig_tok:,}, material {mat_tok:,})")
            out["units"].append({"id": f"{gid}.u{k:02d}", "group": gid, "pages": covered, "items": [i["seg"] for i in us],
                                 "item_pages": {i["seg"]: i["pages"] for i in us},
                                 "material_chars": sum(i["chars"] for i in us), "material_tok": mat_tok,
                                 "digest_tok": dig_tok, **cost})
        if g.get("required"):
            rec["pages_without_material"] = [p for p in pg if p not in covered_all]
        out["groups"][gid] = rec
    out["total_usd"] = round(sum(u["usd"] for u in out["units"]), 2)
    return out, dig


def print_plan(p: dict) -> None:
    print(f"S{p['surah']}: {len(p['pages'])} pages; budget {p['budget_chars']:,} chars per unit; "
          f"{len(p['units'])} units; ~${p['total_usd']:.2f} at Opus rates (uncalibrated; Astra: subscription)")
    print(f"{'unit':<22} {'pages':>5} {'items':>6} {'material':>10} {'mat tok':>8} {'dig tok':>8} {'ctx tok':>8} {'$':>6}")
    for u in p["units"]:
        print(f"{u['id']:<22} {len(u['pages']):>5} {len(u['items']):>6} {u['material_chars']:>10,} {u['material_tok']:>8,} "
              f"{u['digest_tok']:>8,} {u['context_tok']:>8,} {u['usd']:>6.2f}")
    for nr in p.get("not_read", []):
        print(f"  NOT READ (by decision): {', '.join(nr['sources'])} — {nr['reason'][:110]}")
    for gid, g in p["groups"].items():
        notes = []
        if g.get("pointers"):
            notes.append(f"pointers (no text): {', '.join(g['pointers'])}")
        if g.get("no_material_sources"):
            notes.append(f"no segment for this surah: {', '.join(g['no_material_sources'])}")
        if g.get("duplicate_only_sources"):
            notes.append(f"only duplicates of the short edition: {', '.join(g['duplicate_only_sources'])}")
        if g.get("duplicates_listed_not_read"):
            notes.append(f"duplicate segments listed, not read: {len(g['duplicates_listed_not_read'])}")
        if g.get("citing_segments"):
            notes.append(f"citing segments (excerpts): {g['citing_segments']}")
        if g.get("untied_sources"):
            notes.append(f"no ayah ties anywhere, read by phrase search: {', '.join(g['untied_sources'])}")
        if g.get("queries"):
            sm = search_summary(g["queries"])
            hidden = sum(h - k for _, _, h, k in sm["capped"])
            notes.append(f"{sm['queries']} searches; {sm['skipped_formulae']} formula phrases skipped; "
                         f"{len(sm['too_common'])} query×source pairs too common "
                         f"({sum(x[2] for x in sm['too_common']):,} hits not read); {len(sm['capped'])} pairs capped "
                         f"({hidden:,} hits beyond the kept ones)")
        if g.get("unit_note"):
            notes.append(g["unit_note"])
        if g.get("pages_without_material"):
            notes.append(f"REQUIRED voice, no material on: {', '.join(g['pages_without_material'])} (recorded per page)")
        if notes:
            print(f"  {gid}: " + "; ".join(notes))


# ---------------------------------------------------------------- prepare

def wrap(line: str) -> list[str]:
    """A line longer than WRAP broken at spaces (at WRAP characters when there is no space)."""
    out = []
    while len(line) > WRAP:
        cut = line.rfind(" ", 0, WRAP)
        cut = cut if cut > WRAP // 2 else WRAP
        out.append(line[:cut] + "\n")
        line = line[cut:].lstrip(" ")
    return out + [line]


def split_files(text: str, stem: str, d: Path) -> list[Path]:
    """Text in files of at most FILE_CHARS characters, cut at line ends, every line at most WRAP characters."""
    files, cur = [], ""
    for raw in text.splitlines(keepends=True):
        for line in wrap(raw):
            if cur and len(cur) + len(line) > FILE_CHARS:
                files.append(cur)
                cur = ""
            cur += line
    if cur:
        files.append(cur)
    out = []
    for i, body in enumerate(files, 1):
        assert max(map(len, body.splitlines() or [""])) <= 2000, f"{stem}.{i}: a line over 2,000 characters"
        f = d / f"{stem}.{i}.md"
        f.write_text(body, encoding="utf-8")
        out.append(f)
    return out


def out_file(u: dict) -> str:
    """The file whose presence says a unit's run finished: kapsam.jsonl, or gaps.json for a unit with no material."""
    return "kapsam.jsonl" if u["items"] else "gaps.json"


def unit_dir(s: int, uid: str, model: str, effort: str) -> Path:
    return gdir(s) / f"{uid}.{model}.{effort}"


def build_prompt(s: int, u: dict, g: dict, d: Path, files: list[Path]) -> str:
    gid = u["group"]
    lines = ["# Job", "",
             f"- Surah: {s}; ids use S{s:03d}",
             f"- Unit: {u['id']} of group «{gid}»{' — a REQUIRED voice' if g.get('required') else ''}",
             f"- Pages this unit writes for: {', '.join(u['pages'])}",
             f"- PACK: {wd(s) / 'pack'}",
             f"- Your call directory (write only here): {d}",
             f"- Corpus tool: python3 {V2 / 'tools' / 'corpus.py'}",
             f"- Check (per page): python3 {V2 / 'tools' / 'check.py'} --surah {s} --target <page> --annotations "
             f"{d}/records.<page-tag>.jsonl",
             f"- Group focus: {g.get('odak', '')}",
             "", "## Files to read completely, once, at the start (in your call directory unless a path is given)", ""]
    lines += [f"- {f.name if f.parent == d else f}" for f in files]
    if g.get("material") != "none":
        lines += ["", f"Material segments to account for in kapsam.jsonl: {len(u['items'])} (every `### ` heading)."]
    parts = ["\n".join(lines) + "\n", (PROMPTS / "grup.md").read_text(encoding="utf-8")]
    extra = PROMPTS / f"grup_{gid}.md"
    if extra.exists():
        parts.append(extra.read_text(encoding="utf-8"))
    return "\n\n".join(parts)


def load_plan(s: int) -> dict:
    pf = gdir(s) / "plan.json"
    if not pf.exists():
        raise SystemExit("no plan: run `grup.py plan --surah S --write` first")
    return json.loads(pf.read_text(encoding="utf-8"))


def prepare(s: int, uid: str, model: str, effort: str, dry: Path | None = None) -> dict:
    p = load_plan(s)
    if hashlib.sha256((wd(s) / "pack" / "pack.json").read_bytes()).hexdigest() != p["pack_sha256"]:
        raise SystemExit("the pack changed since the plan: plan again")
    if p.get("index") != index_stamp():
        print(f"NOTE: the corpus index changed since the plan ({p.get('index')} → {index_stamp()}); every planned "
              f"segment is looked up again below and a missing one stops the unit")
    u = next((x for x in p["units"] if x["id"] == uid), None)
    if not u:
        raise SystemExit(f"no unit {uid} in the plan")
    done = [x.name for x in gdir(s).glob(f"{uid}.*.*") if (x / "started.json").exists()]
    if done and dry is None:
        return {"unit": uid, "status": "skipped", "reason": f"prepared or run before ({', '.join(done)}): never rerun"}
    d = unit_dir(s, uid, model, effort) if dry is None else dry / f"{uid}.{model}.{effort}"
    g = next(x for x in GROUPS["groups"] if x["id"] == u["group"])
    d.mkdir(parents=True, exist_ok=True)
    files = []
    for page in u["pages"]:
        files += split_files(digest(s, page), f"digest.{tag(page)}", d)
    con = sqlite3.connect(f"file:{C.INDEX}?mode=ro", uri=True)
    pool, _ = group_items(con, s, g, [x for x in g["sources"] if x in held_sources()])
    by = {i["seg"]: i for i in pool}
    missing = [x for x in u["items"] if x not in by]
    if missing:
        raise SystemExit(f"{uid}: {len(missing)} planned segments no longer found ({missing[:5]}): plan again")
    if u["items"]:
        files += split_files("".join(by[x]["text"] + "\n" for x in u["items"]), "material", d)
    files.append(V2 / "SCHEMA_CARD.md")
    prompt = build_prompt(s, u, g, d, files)
    reads = []
    for f in files:
        n = len(f.read_text(encoding="utf-8").splitlines())
        reads.append({"path": str(f), "lines": n, "pages": [[1, n]]})
    row = {"surah": s, "unit": uid, "group": u["group"], "pages": u["pages"], "items": len(u["items"]),
           "stage": "grup", "model": model, "model_id": MODELS[model], "effort": effort,
           "runner": "agent" if model == "opus" else "user", "required_reads": reads, "estimate_usd_opus": u["usd"],
           "pack_sha256": p["pack_sha256"], "index": index_stamp(), "prompt_chars": len(prompt)}
    if dry is not None:  # a look at the unit as it would be prepared: no started.json, nothing marked
        (d / "prompt.md").write_text(prompt, encoding="utf-8")
        (d / "row.json").write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        return {"unit": uid, "status": "dry", "dir": str(d), "prompt_chars": len(prompt), "files": len(files)}
    if model == "opus":
        row["agent_type"] = f"enrich-page-{effort}"
        AR.prepare(d, prompt, row, "grup", out_file(u), lookup=False)
        return {"unit": uid, "status": "prepared", "dir": rel(d), "spawn": rel(d / "spawn.md")}
    (d / "prompt.md").write_text(prompt, encoding="utf-8")
    row.update(started=time.strftime("%Y-%m-%dT%H:%M:%S%z"), prompt_sha256=hashlib.sha256(prompt.encode()).hexdigest())
    with (d / "started.json").open("x", encoding="utf-8") as f:
        json.dump(row, f, ensure_ascii=False, indent=1)
    return {"unit": uid, "status": "prepared", "dir": rel(d), "prompt": rel(d / "prompt.md"),
            "run": f"cd {d} && codex exec -m {MODELS[model]} -c model_reasoning_effort=\"{effort}\" "
                   f"-s workspace-write --skip-git-repo-check - < prompt.md"}


# ---------------------------------------------------------------- finish

KAPSAM = {"kullanildi", "yeni_yok", "tekrar", "ilgisiz", "okunamadi"}


def codex_session(d: Path, since: float) -> Path | None:
    """The Codex session log of a run the user started in d: a rollout written after `since` whose session cwd is d
    or whose first lines name d (the prompt's call directory)."""
    import enrich as E
    for f in sorted(E.SESSIONS.glob("*/*/*/rollout-*.jsonl"), key=lambda q: q.stat().st_mtime, reverse=True):
        if f.stat().st_mtime < since:
            break
        with f.open(encoding="utf-8") as fh:
            head = "".join(fh.readline() for _ in range(40))
        if f'"cwd":"{d}"' in head.replace(" ", "") or f"write only here): {d}" in head.replace("\\n", "\n"):
            return f
    return None


def codex_run(d: Path, since: float) -> dict:
    """Tokens, the weekly-limit readings and the command outputs Codex truncated before the model saw them."""
    import enrich as E
    f = codex_session(d, since)
    if not f:
        print(f"NOTE: {d.name}: no Codex session log names this directory: tokens and truncated reads not recorded")
        return {"session": None}
    res = E.read_session(f)
    cut = []
    for line in f.read_text(encoding="utf-8").splitlines():
        try:
            pl = json.loads(line).get("payload") or {}
        except json.JSONDecodeError:
            continue
        if pl.get("type") in ("function_call_output", "custom_tool_call_output"):
            o = pl.get("output")
            o = o if isinstance(o, str) else json.dumps(o, ensure_ascii=False)
            m = re.search(r"truncated output \(original token count: (\d+)\)", o)
            if m:
                cut.append(int(m.group(1)))
    res["truncated_outputs"] = cut
    if cut:
        print(f"WARNING: {d.name}: {len(cut)} command outputs were truncated by Codex before the model saw them "
              f"(original sizes {cut[:8]} tokens): those reads were partial")
    return res


def record_files(d: Path, t: str) -> tuple[list[Path], str | None]:
    """A page's records as check.py reads them: records.<t>.jsonl if it exists, else its parts in order."""
    whole = d / f"records.{t}.jsonl"
    parts = sorted((q for q in d.glob(f"records.{t}.*.jsonl") if re.fullmatch(rf"records\.{t}\.\d+\.jsonl", q.name)),
                   key=lambda q: int(q.name.split(".")[-2]))
    if whole.exists():
        return [whole], (f"records.{t}.jsonl and parts {[q.name for q in parts]} both exist: the whole file is used "
                         f"(as check.py does), the parts are not") if parts else None
    return parts, None


def load_records(paths: list[Path]) -> tuple[list[dict], list[str]]:
    recs, bad = [], []
    for p in paths:
        for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if line.strip():
                try:
                    x = json.loads(line)
                except json.JSONDecodeError:
                    x = None
                if isinstance(x, dict):
                    recs.append(x)
                else:
                    bad.append(f"{p.name} line {n}: not a JSON object")
    return recs, bad


def finish(s: int, uid: str, model: str, effort: str) -> dict:
    d = unit_dir(s, uid, model, effort)
    st = d / "started.json"
    if not st.exists():
        return {"unit": uid, "status": "error", "reason": "not prepared"}
    lf = d / "run.log.json"
    if lf.exists():
        if "status" in json.loads(lf.read_text(encoding="utf-8")):
            return {"unit": uid, "status": "error", "reason": "already finished; never twice"}
        print(f"NOTE: {uid}: run.log.json has no status (a finish that stopped part way): finishing again")
        lf.unlink()
    row = json.loads(st.read_text(encoding="utf-8"))
    u = next(x for x in load_plan(s)["units"] if x["id"] == uid)
    g = next(x for x in GROUPS["groups"] if x["id"] == u["group"])
    problems: list[str] = []
    if model == "opus":
        import enrich as E  # the transcript audit (files read completely, spills, cuts)
        obj = AR.finish(d, out_file(u))
        row.update({k: obj.get(k) for k in ("total_cost_usd", "cost_usd_est", "num_turns", "transcript", "stop_reason",
                                             "usage", "tool_use_outside_rule")})
        row["coverage"] = cov = E.audit(d, obj.get("transcript"), row.get("required_reads") or [])
        if obj.get("is_error"):
            problems.append("the agent's run ended in error")
        for k in ("files_unread", "files_partial", "cuts_not_followed", "spilled", "max_tokens_stops", "error"):
            if cov.get(k):
                problems.append(f"read audit {k}: {cov[k] if not isinstance(cov[k], list) else cov[k][:5]}")
                print(f"WARNING: {uid}: read audit {k}: {cov[k]}")
        if obj.get("tool_use_outside_rule"):
            problems.append(f"tool use outside the run's rule: {obj['tool_use_outside_rule'][:5]}")
            print(f"WARNING: {uid}: tool use outside the run's rule: {obj['tool_use_outside_rule']}")
    else:
        row["codex"] = codex_run(d, st.stat().st_mtime - 60)
        if row["codex"].get("truncated_outputs"):
            problems.append(f"{len(row['codex']['truncated_outputs'])} reads truncated by Codex")
    if not (d / out_file(u)).exists():
        problems.append(f"no {out_file(u)}: the run did not finish")
    # records per page, checked as merge will check them
    checks, kept_ids = {}, set()
    for page in u["pages"]:
        files, note = record_files(d, tag(page))
        if note:
            print(f"WARNING: {uid}: {note}")
            problems.append(note)
        if not files:
            checks[page] = {"records": 0}
            continue
        recs, bad = load_records(files)
        for b in bad:
            print(f"WARNING: {uid}: {b}")
            problems.append(b)
        kept, dropped, warnings = VAL.check_records(s, page, recs, "islami")
        kept_ids |= {(page, r["id"]) for r in kept}
        checks[page] = {"records": len(recs), "kept": len(kept), "dropped": dropped, "warnings": warnings,
                        "not_json": bad}
        for x in dropped:
            print(f"DROPPED {uid} {page}: {'; '.join(x['errors'])}")
    read = {q.name for p in u["pages"] for q in record_files(d, tag(p))[0]}
    ignored = {q.name for p in u["pages"] for q in d.glob(f"records.{tag(p)}.*.jsonl")
               if record_files(d, tag(p))[1]}  # parts beside a whole file: warned above
    stray = sorted({q.name for q in d.glob("records.*.jsonl")} - read - ignored)
    if stray:
        print(f"WARNING: {uid}: records files not read (another page, or not named records.<page>[.n].jsonl): {stray}")
        problems.append(f"records files not read: {stray}")
    (d / "check.json").write_text(json.dumps(checks, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    # kapsam: every planned segment exactly once with a known durum; used ids exist; a required voice on every page
    kap, bad, yok = {}, [], {}
    for i, line in enumerate((d / "kapsam.jsonl").read_text(encoding="utf-8").splitlines()
                             if (d / "kapsam.jsonl").exists() else [], 1):
        if not line.strip():
            continue
        try:
            x = json.loads(line)
        except json.JSONDecodeError:
            x = None
        if not isinstance(x, dict):
            bad.append(f"line {i}: not a JSON object")
            continue
        if x.get("page"):
            if x["page"] not in u["pages"]:
                bad.append(f"line {i}: a yok line for {x['page']}, not a page of this unit")
            yok[x["page"]] = x.get("neden", "")
            continue
        if x.get("seg") in kap:
            bad.append(f"line {i}: {x.get('seg')} listed twice")
        if x.get("durum") not in KAPSAM:
            bad.append(f"line {i}: durum {x.get('durum')!r} not one of {sorted(KAPSAM)}")
        if x.get("durum") == "kullanildi":
            ids = {r for _, r in kept_ids}
            gone = [k for k in x.get("kayit_ids") or [] if k not in ids]
            if not x.get("kayit_ids") or gone:
                bad.append(f"line {i}: {x.get('seg')} kullanildi, but its kayit_ids {gone or '(none)'} are not kept records")
        kap[x.get("seg")] = x
    missing = [x for x in u["items"] if x not in kap]
    extra = [x for x in kap if x not in set(u["items"])]
    voice = {}
    if g.get("required"):
        for page in u["pages"]:
            voice[page] = ("cited" if any(p == page for p, _ in kept_ids) else
                           f"yok: {yok[page]}" if page in yok else "MISSING: no block and no recorded reason")
        silent = [p for p, v in voice.items() if v.startswith("MISSING")]
        if silent:
            print(f"WARNING: {uid}: required voice with neither a kept block nor a yok line on {silent}")
            problems.append(f"required voice silent on {silent}")
    row["kapsam"] = {"listed": len(kap), "planned": len(u["items"]), "missing": missing, "not_planned": extra,
                     "problems": bad, "by_durum": dict(Counter(x.get("durum") for x in kap.values())),
                     "required_voice": voice}
    if missing:
        print(f"WARNING: {uid}: {len(missing)} material segments not accounted for in kapsam.jsonl: {missing[:8]}")
        problems.append(f"{len(missing)} segments missing from kapsam")
    if extra:
        print(f"WARNING: {uid}: kapsam names {len(extra)} segments that are not this unit's material: {extra[:8]}")
        problems.append(f"{len(extra)} kapsam lines for segments outside the unit")
    for b in bad:
        print(f"WARNING: {uid}: kapsam {b}")
    row["records"] = {pg: {k: (len(v) if isinstance(v, list) else v) for k, v in c.items()} for pg, c in checks.items()}
    row["problems"] = problems
    row["status"] = ("error" if any(p.startswith(("no kapsam", "no gaps", "the agent's run")) for p in problems) else
                     "ok" if not problems and not bad else "incomplete")
    row["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    (d / "run.log.json").write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log({k: row[k] for k in ("surah", "unit", "group", "stage", "model_id", "effort", "estimate_usd_opus",
                             "total_cost_usd", "status", "finished") if k in row})
    kept_n = sum(c.get("kept", 0) for c in checks.values())
    print(f"{uid}: {row['status']}; kept {kept_n} records over {len(u['pages'])} pages; kapsam "
          f"{len(kap)}/{len(u['items'])}" + (f"; problems: {problems}" if problems else ""))
    return row


# ---------------------------------------------------------------- merge

def para_no(r: dict) -> int:
    return int(re.sub(r"\D", "", str(r.get("paragraf"))) or 0)


def merge(s: int) -> dict:
    """Every finished unit's records, per page: ids made unique (unit order within paragraph order) before the page
    check, so no record shares an id with another; the check's drops listed with their reasons; kept ids renumbered
    per KOD; rendered into work/sNNN/grup/pages/<page>/ (never out/). Units that ended in error are not merged
    (listed); incomplete units are merged with their problems listed. Near-duplicates (same locator after the same
    paragraph) are reported for review, never dropped. Each required voice's state is written per page."""
    p = load_plan(s)
    out = gdir(s) / "pages"
    res: dict = {"units_merged": [], "units_not_merged": {}, "units_not_finished": [], "pages": {}}
    run_of: dict[str, tuple[Path, dict]] = {}
    for u in p["units"]:
        fin = [x for x in sorted(gdir(s).glob(f"{u['id']}.*.*")) if (x / "run.log.json").exists()
               and "status" in json.loads((x / "run.log.json").read_text(encoding="utf-8"))]
        if not fin:
            res["units_not_finished"].append(u["id"])
            continue
        if len(fin) > 1:
            print(f"WARNING: {u['id']}: {len(fin)} finished runs ({[x.name for x in fin]}): the last is merged")
        lg = json.loads((fin[-1] / "run.log.json").read_text(encoding="utf-8"))
        if lg.get("status") == "error":
            res["units_not_merged"][u["id"]] = lg.get("problems")
            print(f"WARNING: {u['id']}: not merged (error: {lg.get('problems')})")
            continue
        if lg.get("status") == "incomplete":
            print(f"NOTE: {u['id']}: merged though incomplete: {lg.get('problems')}")
        run_of[u["id"]] = (fin[-1], lg)
        res["units_merged"].append(u["id"])
    if res["units_not_finished"]:
        print(f"NOTE: {len(res['units_not_finished'])} units not finished: {res['units_not_finished']}")
    group_of = {u["id"]: u["group"] for u in p["units"]}
    for page in p["pages"]:
        t = tag(page)
        recs, meta = [], {}  # meta[id(record)] = (unit, the unit's own id): kept beside the record, never inside it
        for u in p["units"]:
            if u["id"] not in run_of or page not in u["pages"]:
                continue
            files, _ = record_files(run_of[u["id"]][0], t)
            rr, bad = load_records(files)
            for b in bad:
                print(f"WARNING: {u['id']} {b}")
            for r in rr:
                meta[id(r)] = (u["id"], str(r.get("id")))
                recs.append(r)
        info: dict = {"records": len(recs)}
        if recs:
            recs.sort(key=lambda r: (para_no(r), meta[id(r)][0]))

            def renumber(rs: list[dict]) -> None:
                n: Counter = Counter()
                for r in rs:
                    own = meta[id(r)][1]
                    kod = own.split("-")[1] if own.count("-") >= 2 else "X"
                    n[kod] += 1
                    r["id"] = f"S{s:03d}-{kod}-{n[kod]:03d}"

            renumber(recs)  # unique before the check: a collision between units never drops or re-admits a record
            kept, dropped, warnings = VAL.check_records(s, page, recs, "islami")
            by_id = {r["id"]: r for r in recs}
            info["dropped"] = [{"unit": meta[id(by_id[x["id"]])][0], "id": meta[id(by_id[x["id"]])][1],
                                "errors": x["errors"]} for x in dropped]
            for x in info["dropped"]:
                print(f"DROPPED {page} {x['unit']} {x['id']}: {'; '.join(x['errors'])}")
            renumber(kept)
            near = defaultdict(list)
            for r in kept:
                for loc in str(r.get("kaynak", "")).split("|"):
                    near[(str(r.get("paragraf")), loc.strip())].append(r["id"])
            pd = out / t
            pd.mkdir(parents=True, exist_ok=True)
            clean = kept
            (pd / "annotations.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in clean),
                                                  encoding="utf-8")
            (pd / "provenance.json").write_text(json.dumps({r["id"]: {"unit": meta[id(r)][0], "unit_id": meta[id(r)][1]}
                                                            for r in kept}, ensure_ascii=False, indent=1) + "\n",
                                                encoding="utf-8")
            page_file, placement = R.render(s, page, clean, pd / "page")
            info.update(kept=len(clean), warnings=warnings, placement=placement, page=rel(page_file),
                        near_duplicates={f"¶{k[0]} {k[1]}": v for k, v in near.items()
                                         if len(v) > 1 and k[1] not in ("", "hafiza")})
            kept_groups = {group_of[meta[id(r)][0]] for r in kept}
        else:
            kept_groups = set()
        # each required voice on this page: cited, the agent's reason, the script's "no material", or MISSING
        voices = {}
        for gid, g in p["groups"].items():
            if not g.get("required"):
                continue
            if gid in kept_groups:
                voices[gid] = "cited"
            elif page in g.get("pages_without_material", []):
                voices[gid] = "no material of this group for this page (plan)"
            else:
                why = [run_of[u][1].get("kapsam", {}).get("required_voice", {}).get(page)
                       for u in run_of if group_of[u] == gid]
                why = [w for w in why if w and w.startswith("yok")]
                voices[gid] = why[0] if why else ("unit not merged or not finished" if not any(
                    group_of[u] == gid for u in run_of) else "MISSING: no kept block and no recorded reason")
            if voices[gid].startswith(("MISSING", "unit not")):
                print(f"WARNING: {page}: required voice {gid}: {voices[gid]}")
        info["required_voices"] = voices
        res["pages"][page] = info
        print(f"{page}: kept {info.get('kept', 0)} of {info['records']}; dropped {len(info.get('dropped', []))}; "
              f"near-duplicates {len(info.get('near_duplicates', {}))}")
    out.mkdir(parents=True, exist_ok=True)
    (out / "merge.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return res


def status(s: int) -> None:
    p = load_plan(s)
    for u in p["units"]:
        st = "planned"
        for d in sorted(gdir(s).glob(f"{u['id']}.*.*")):
            if (d / "run.log.json").exists():
                st = f"finished {json.loads((d / 'run.log.json').read_text(encoding='utf-8')).get('status')} ({d.name})"
            elif (d / "started.json").exists():
                st = f"prepared ({d.name})"
        print(f"{u['id']:<22} {len(u['pages']):>3} pages {u['material_tok']:>8,} tok  {st}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["plan", "prepare", "finish", "merge", "status"])
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--group")
    ap.add_argument("--unit")
    ap.add_argument("--model", choices=sorted(MODELS), default="astra")
    ap.add_argument("--effort", default="high", help="the reasoning effort the unit is run at (names its directory)")
    ap.add_argument("--write", action="store_true", help="plan: write plan.json (refused once a unit is prepared)")
    ap.add_argument("--dry", type=Path, help="prepare: build the unit's files in this directory only (no started.json)")
    a = ap.parse_args()
    if a.cmd == "plan":
        p, _ = plan(a.surah, a.group)
        print_plan(p)
        if a.write:
            if a.group:
                raise SystemExit("--write needs the whole plan (no --group)")
            if any(gdir(a.surah).glob("*.*.*/started.json")):
                raise SystemExit("units of this plan are prepared or run: the plan is frozen")
            gdir(a.surah).mkdir(parents=True, exist_ok=True)
            (gdir(a.surah) / "plan.json").write_text(json.dumps(p, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print(f"wrote {rel(gdir(a.surah) / 'plan.json')}")
    elif a.cmd == "prepare":
        p = load_plan(a.surah)
        ids = [u["id"] for u in p["units"]] if a.unit == "all" else [x for x in (a.unit or "").split(",") if x]
        if not ids:
            raise SystemExit("prepare needs --unit U[,U…] or --unit all")
        for uid in ids:
            print(json.dumps(prepare(a.surah, uid, a.model, a.effort, a.dry), ensure_ascii=False))
    elif a.cmd == "finish":
        if not a.unit:
            raise SystemExit("finish needs --unit U")
        r = finish(a.surah, a.unit, a.model, a.effort)
        if r.get("reason"):
            raise SystemExit(f"{a.unit}: {r['reason']}")
    elif a.cmd == "merge":
        merge(a.surah)
    else:
        status(a.surah)


if __name__ == "__main__":
    main()
