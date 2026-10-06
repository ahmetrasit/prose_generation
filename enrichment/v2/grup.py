#!/usr/bin/env python3
"""The hybrid enrichment workflow, extract then place (HYBRID_PLAN.md Task C; REVIEW_plan_adversarial_2026-10-05.md,
agreed by the user 2026-10-05). The user's aim: after each paragraph of the frozen commentary an advanced reader sees
every discussion point the sources raise, one sentence each, with pointers (corpus locators) to the details.

Stage 1, extract (one call per group unit): a group's material for a surah (groups.json; balanced units of about
`budget_chars`) is read without the base; the agent writes one line per POSITION a source takes (lines.jsonl:
{"id","pg","w","t","f","k","a","m",…}, w = the ayah words it concerns, from binding.json) and accounts for every
segment (kapsam.jsonl: kullanildi with the lines whose pointers carry it, ilgisiz, okunamadi).
Stage 2, place (one call per page): the full numbered page once plus every line for it; each line gets a paragraph
(or a rejection with a reason), lines stating the same position are clustered (one representative kept unchanged,
the script unions every member's pointers and holders); the base's claims no line touches go to bos.jsonl.
Then oncul (antecedents) reads those untouched claims; merge expands lines into schema records (defaults recorded),
anchors them by script, checks, renders. The project dictionary and the lexica are not read (groups.json not_read).

  python3 -B enrichment/v2/grup.py plan    --surah 1 [--group G] [--write]
  python3 -B enrichment/v2/grup.py prepare --surah 1 --unit U|all --model astra|opus [--effort high]   stage 1
  python3 -B enrichment/v2/grup.py finish  --surah 1 --unit U --model astra [--effort high]
  python3 -B enrichment/v2/grup.py place   --surah 1 --page P|all --model astra [--effort high]        stage 2
  python3 -B enrichment/v2/grup.py finish-place --surah 1 --page P|all --model astra
  python3 -B enrichment/v2/grup.py prepare --surah 1 --unit oncul.u01 …; finish …   after every page is placed
  python3 -B enrichment/v2/grup.py merge   --surah 1         pages into work/sNNN/grup/pages/ (never out/)
  python3 -B enrichment/v2/grup.py status  --surah 1
  (agents run `lint --dir D` and `lint-place --dir D` themselves)

Astra calls are run by the user (`prepare`/`place` print the codex command; the prompt goes through stdin and holds
all the text, so nothing is read through truncated command output); Opus calls get spawn.md and files. No model is
ever called by this script.
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
import blocks as B  # noqa: E402

WORK = V2 / "work"
PROMPTS = V2 / "prompts"
LEDGER = WORK / "ledger.jsonl"
GROUPS = json.loads((V2 / "groups.json").read_text(encoding="utf-8"))
MODELS = {"astra": "gpt-6-astra", "opus": "claude-opus-5-5"}
FILE_CHARS = 24_000      # one material file for an Opus agent: one Read (the Read tool shows at most 25,000 tokens)
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
INDEX_REF_RATIO = (0.08, 0.40)  # verse refs per word that make a citing page (≥ 100 words) an index page: under an
#                                 "index" heading, or under any heading (listed in the plan, not read)
LINE_WORDS = 45         # a line's metin beyond this many words is reported (one sentence is the aim)
# iliski when a line does not give it: search hits share words or a theme with the ayah; the rest treat the ayah
ILISKI_DEFAULT = {"hadis": "tematik", "siyer-tarih": "tematik", "siir-sahid": "lafzi", "vucuh": "lafzi"}
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


# ---------------------------------------------------------------- pages

def pages(s: int) -> list[str]:
    n = json.loads((wd(s) / "pack" / "pack.json").read_text(encoding="utf-8"))["ayat"]
    return [p for p in ["surah"] + [f"{s}:{a}" for a in range(1, n + 1)]
            if (wd(s) / "pack" / "numbered" / f"{tag(p)}.md").exists()]


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
                untied_only: bool = False) -> tuple[list[dict], list[str]]:
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
    out, listed = [], []
    for seg, x in by.items():
        full, head = x["row"][6] or "", re.sub(r"\s", "", (x["row"][5] or "")).lower()
        nw = len(full.split())
        ratio = len(re.findall(r"(?<![\d:])\d{1,3}\s?:\s?\d{1,3}(?![\d:])", full)) / max(1, nw)
        if nw >= 100 and (ratio > INDEX_REF_RATIO[1] or ("index" in head and ratio > INDEX_REF_RATIO[0])):
            listed.append(seg)  # an index or concordance page: listed (plan), not read
            continue
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
    return out, listed


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
        more, listed = cites_items(con, s, held, valid, got, untied_only=not g.get("cites"))
        if listed:
            info["index_pages_listed"] = listed
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
        items, listed = cites_items(con, s, held, valid)
        if listed:
            info["index_pages_listed"] = listed
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


def unit_cost(material_tok: int, brief_tok: int) -> dict:
    ctx = HARNESS_TOK + brief_tok + material_tok
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


def plan(s: int, only: str | None = None) -> dict:
    con = sqlite3.connect(f"file:{C.INDEX}?mode=ro", uri=True)
    pg = pages(s)
    if "surah" not in pg:
        raise SystemExit(f"S{s}: no numbered surah page in the pack (PACK/numbered/surah.md): build the pack first")
    budget = GROUPS["budget_chars"]
    have = held_sources()
    out = {"surah": s, "planned": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "budget_chars": budget, "pages": pg,
           "pack_sha256": hashlib.sha256((wd(s) / "pack" / "pack.json").read_bytes()).hexdigest(),
           "index": index_stamp(), "not_read": GROUPS.get("not_read", []), "groups": {}, "units": [],
           "page_tok": {p: est_tokens(numbered_text(s, p)) for p in pg}}
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
            if mat == "none":  # the antecedent unit reads the claims no line touched (placement output)
                mat_tok = sum(out["page_tok"].values()) // 10
            cost = unit_cost(mat_tok, bt)
            if cost["context_tok"] > CONTEXT_WARN:
                print(f"WARNING: {gid}.u{k:02d}: starts at ~{cost['context_tok']:,} tokens of context")
            out["units"].append({"id": f"{gid}.u{k:02d}", "group": gid, "pages": covered, "items": [i["seg"] for i in us],
                                 "item_pages": {i["seg"]: i["pages"] for i in us},
                                 "material_chars": sum(i["chars"] for i in us), "material_tok": mat_tok, **cost})
        if g.get("required"):
            rec["pages_without_material"] = [p for p in pg if p not in covered_all]
        out["groups"][gid] = rec
    pb = est_tokens((PROMPTS / "grup_yer.md").read_text(encoding="utf-8")) if (PROMPTS / "grup_yer.md").exists() else 2000
    per_page: Counter = Counter()  # expected line tokens per page: ~120 per line, ~1 line per 2k material tokens,
    for u in out["units"]:          # a unit's share spread over its items' first pages
        if u["items"]:
            share = 120 * u["material_tok"] / 2000 / len(u["items"])
            for seg in u["items"]:
                per_page[u["item_pages"][seg][0]] += share
    for p in pg:
        lines_tok = int(per_page[p])
        out["units"].append({"id": f"yer.{tag(p)}", "group": "yer", "pages": [p], "items": [], "item_pages": {},
                             "material_chars": 0, "material_tok": out["page_tok"][p] + lines_tok,
                             **unit_cost(out["page_tok"][p] + lines_tok, pb)})
    out["total_usd"] = round(sum(u["usd"] for u in out["units"]), 2)
    return out


def print_plan(p: dict) -> None:
    n1 = sum(1 for u in p["units"] if u["group"] != "yer")
    print(f"S{p['surah']}: {len(p['pages'])} pages; budget {p['budget_chars']:,} chars per unit; {n1} extraction units "
          f"+ {len(p['units']) - n1} placement calls; ~${p['total_usd']:.2f} at Opus rates (uncalibrated; Astra: "
          f"subscription)")
    print(f"{'unit':<22} {'pages':>5} {'items':>6} {'material':>10} {'mat tok':>8} {'ctx tok':>8} {'$':>6}")
    for u in p["units"]:
        print(f"{u['id']:<22} {len(u['pages']):>5} {len(u['items']):>6} {u['material_chars']:>10,} {u['material_tok']:>8,} "
              f"{u['context_tok']:>8,} {u['usd']:>6.2f}")
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
        if g.get("index_pages_listed"):
            notes.append(f"index pages listed, not read: {len(g['index_pages_listed'])} "
                         f"({', '.join(g['index_pages_listed'])})")
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


# ---------------------------------------------------------------- shared by both stages

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
    """Text in files of at most FILE_CHARS characters, cut at line ends, every line at most WRAP characters (the
    Opus agent's Read tool; Astra gets the text inside its prompt)."""
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


def call_dir(s: int, uid: str, model: str, effort: str) -> Path:
    return gdir(s) / f"{uid}.{model}.{effort}"


def load_plan(s: int) -> dict:
    pf = gdir(s) / "plan.json"
    if not pf.exists():
        raise SystemExit("no plan: run `grup.py plan --surah S --write` first")
    return json.loads(pf.read_text(encoding="utf-8"))


def check_plan(s: int, p: dict) -> None:
    if hashlib.sha256((wd(s) / "pack" / "pack.json").read_bytes()).hexdigest() != p["pack_sha256"]:
        raise SystemExit("the pack changed since the plan: plan again")
    if p.get("index") != index_stamp():
        print(f"NOTE: the corpus index changed since the plan ({p.get('index')} → {index_stamp()}); every planned "
              f"segment is looked up again and a missing one stops the unit")


def write_call(s: int, d: Path, uid: str, model: str, effort: str, prompt: str, row: dict, out_name: str) -> dict:
    """started.json (the never-rerun guard) and prompt.md; spawn.md for an Opus agent; for Astra the command the user
    runs (the prompt through stdin: a long prompt must not pass through the argument list)."""
    row.update(model=model, model_id=MODELS[model], effort=effort, output=out_name, prompt_chars=len(prompt),
               runner="agent" if model == "opus" else "user", index=index_stamp())
    if model == "opus":
        row["agent_type"] = f"enrich-page-{effort}"
        AR.prepare(d, prompt, row, "grup", out_name, lookup=False)
        return {"unit": uid, "status": "prepared", "dir": rel(d), "spawn": rel(d / "spawn.md")}
    (d / "prompt.md").write_text(prompt, encoding="utf-8")
    row.update(started=time.strftime("%Y-%m-%dT%H:%M:%S%z"), prompt_sha256=hashlib.sha256(prompt.encode()).hexdigest())
    with (d / "started.json").open("x", encoding="utf-8") as f:
        json.dump(row, f, ensure_ascii=False, indent=1)
    return {"unit": uid, "status": "prepared", "dir": rel(d), "prompt_tokens": est_tokens(prompt),
            "run": f"cd {d} && codex exec -m {MODELS[model]} -c model_reasoning_effort=\"{effort}\" "
                   f"-s workspace-write --skip-git-repo-check - < prompt.md"}


def started_before(s: int, uid: str) -> list[str]:
    return [x.name for x in gdir(s).glob(f"{uid}.*.*") if (x / "started.json").exists()]


def numbered_text(s: int, page: str) -> str:
    return (wd(s) / "pack" / "numbered" / f"{tag(page)}.md").read_text(encoding="utf-8")


def finished_run(s: int, uid: str) -> tuple[Path, dict] | None:
    """The last finished call directory of a unit (a run.log.json with a status) and its log."""
    fin = []
    for x in sorted(gdir(s).glob(f"{uid}.*.*")):
        lf = x / "run.log.json"
        if lf.exists():
            lg = json.loads(lf.read_text(encoding="utf-8"))
            if "status" in lg:
                fin.append((x, lg))
    if len(fin) > 1:
        print(f"WARNING: {uid}: {len(fin)} finished runs ({[x.name for x, _ in fin]}): the last is used")
    return fin[-1] if fin else None


def read_jsonl(f: Path) -> tuple[list[dict], list[str]]:
    out, bad = [], []
    if not f.exists():
        return out, bad
    for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            x = json.loads(line)
        except json.JSONDecodeError:
            x = None
        if isinstance(x, dict):
            out.append(x)
        else:
            bad.append(f"{f.name} line {n}: not a JSON object")
    return out, bad


def run_usage(d: Path, model: str, out_name: str, row: dict, problems: list[str]) -> None:
    """The run's tokens and audits: the Opus transcript (cost, read audit, rule breaches) or the Codex session log
    (tokens, weekly readings, truncated command outputs)."""
    if model == "opus":
        import enrich as E
        obj = AR.finish(d, out_name)
        row.update({k: obj.get(k) for k in ("total_cost_usd", "cost_usd_est", "num_turns", "transcript", "stop_reason",
                                             "usage", "tool_use_outside_rule")})
        row["coverage"] = cov = E.audit(d, obj.get("transcript"), row.get("required_reads") or [])
        if obj.get("is_error"):
            problems.append("the agent's run ended in error")
        for k in ("files_unread", "files_partial", "cuts_not_followed", "spilled", "max_tokens_stops", "error"):
            if cov.get(k):
                problems.append(f"read audit {k}: {cov[k] if not isinstance(cov[k], list) else cov[k][:5]}")
                print(f"WARNING: {d.name}: read audit {k}: {cov[k]}")
        if obj.get("tool_use_outside_rule"):
            problems.append(f"tool use outside the run's rule: {obj['tool_use_outside_rule'][:5]}")
            print(f"WARNING: {d.name}: tool use outside the run's rule: {obj['tool_use_outside_rule']}")
    else:
        row["codex"] = codex_run(d, (d / "started.json").stat().st_mtime - 60)
        if row["codex"].get("truncated_outputs"):
            problems.append(f"{len(row['codex']['truncated_outputs'])} command outputs truncated by Codex")
    if not (d / out_name).exists():
        problems.append(f"no {out_name}: the run did not finish")


def close_run(d: Path, row: dict, problems: list[str], extra_bad: list[str] = ()) -> dict:
    row["problems"] = problems + list(extra_bad)
    row["status"] = ("error" if any(p.startswith(("no ", "the agent's run")) for p in problems) else
                     "ok" if not row["problems"] else "incomplete")
    row["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    (d / "run.log.json").write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log({k: row[k] for k in ("surah", "unit", "group", "stage", "model_id", "effort", "estimate_usd_opus",
                             "total_cost_usd", "status", "finished") if k in row})
    return row


def reopen(d: Path, uid: str) -> dict | None:
    """None when the call may be finished now; else the reason it may not."""
    if not (d / "started.json").exists():
        return {"unit": uid, "status": "error", "reason": f"not prepared ({d.name})"}
    lf = d / "run.log.json"
    if lf.exists():
        if "status" in json.loads(lf.read_text(encoding="utf-8")):
            return {"unit": uid, "status": "error", "reason": "already finished; never twice"}
        print(f"NOTE: {uid}: run.log.json has no status (a finish that stopped part way): finishing again")
        lf.unlink()
    return None


KAPSAM = {"kullanildi", "ilgisiz", "okunamadi"}


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
              f"(original sizes {cut[:8]} tokens)")
    return res


# ---------------------------------------------------------------- lines: the stage-1 output, expanded by script

SHORT = {"t": "tur", "f": "islev", "k": "kaynak", "a": "alim", "m": "metin", "l": "iliski", "d": "durum"}
LINE_META = {"id", "pg", "w", "p"}


def word_refs(s: int) -> dict[str, int]:
    """QAC word ref (S:A:W) → ayah, from PACK/binding.json."""
    return {w["qac_word_ref"]: int(ref.split(":")[1]) for ref, ws in binding(s).items() for w in ws
            if w.get("qac_word_ref")}


def expand(line: dict, s: int, page: str, gid: str, n_ayat: int) -> tuple[dict, list[str]]:
    """A line → a schema record (no paragraf/capa: placement adds them), and the fields the script defaulted."""
    r, defaulted = {}, []
    for k, v in line.items():
        if k in LINE_META:
            continue
        r[SHORT.get(k, k)] = v
    if "ayet" not in r:
        if page != "surah":
            r["ayet"] = page
        else:
            wr = word_refs(s)
            ay = sorted({wr[x] for x in (line.get("w") or []) if x in wr}) if isinstance(line.get("w"), list) else []
            r["ayet"] = (f"{s}:{ay[0]}" + (f"-{ay[-1]}" if ay[-1] != ay[0] else "")) if ay else f"{s}:1-{n_ayat}"
        defaulted.append("ayet")
    if "iliski" not in r:
        r["iliski"] = ILISKI_DEFAULT.get(gid, "dogrudan")
        defaulted.append("iliski")
    if "durum" not in r:
        r["durum"] = ("aktarilan" if r.get("tur") in ("tefsir_rivayet", "esbab", "isari") else
                      "tartismali" if r.get("islev") == "ihtilaf" else "acik")
        defaulted.append("durum")
    if "kat" not in r:
        r["kat"] = "ek"
        defaulted.append("kat")
    r["id"] = f"S{s:03d}-{B.KOD.get(r.get('tur'), 'XXX')}-001"
    if "gelenek" not in r:
        r["gelenek"] = "islami"
        defaulted.append("gelenek")
    return r, defaulted


def lint_lines(s: int, d: Path, u: dict, gid: str) -> tuple[dict[str, dict], dict[str, list[str]], list[str]]:
    """Every line of d/lines.jsonl checked as far as it can be before placement: keys, page, words, every schema rule
    the validator applies to a record (locators resolve, sahih hadith, required fields, word limits), the ayah covers
    the page, Arabic quotes found in the cited segments. Returns (good lines by id, errors by id, warnings)."""
    import check as CK
    lines, bad = read_jsonl(d / "lines.jsonl")
    wr = word_refs(s)
    n_ayat = json.loads((wd(s) / "pack" / "pack.json").read_text(encoding="utf-8"))["ayat"]
    corpus = B.Corpus(C.INDEX)
    con = C.connect()
    good, errs, warns = {}, {}, list(bad)
    counts = Counter(str(ln.get("id")) for ln in lines if ln.get("id"))
    for i, ln in enumerate(lines, 1):
        lid = str(ln.get("id") or f"(line {i} without id)")
        e = []
        if not ln.get("id"):
            e.append("missing id")
        elif counts[lid] > 1:
            e.append(f"id used {counts[lid]} times (every line with it is dropped)")
        for k in ("pg", "w", "t", "f", "k", "m"):
            if not ln.get(k):
                e.append(f"missing {k}")
        unknown = [k for k in ln if k not in LINE_META and k not in SHORT and k not in B.FIELDS]
        if unknown:
            e.append(f"unknown keys {unknown}")
        page = ln.get("pg")
        if page not in u["pages"]:
            e.append(f"pg {page!r} is not a page of this unit ({', '.join(u['pages'])})")
        w = ln.get("w")
        if isinstance(w, list) and not all(isinstance(x, str) for x in w):
            e.append("w must hold word refs as strings")
        elif isinstance(w, list):
            wrong = [x for x in w if x not in wr]
            if wrong:
                e.append(f"w {wrong} not word refs of S{s} (binding.json)")
            elif page and page != "surah" and any(wr[x] != int(page.split(":")[1]) for x in w):
                e.append(f"w {w} has words of another ayah than {page}")
        elif w not in ("ayah", "surah"):
            e.append(f"w must be a list of word refs, \"ayah\" or \"surah\"")
        if gid == "oncul":
            try:
                n = int(ln.get("p"))
                if page in u["pages"] and n not in R.prose_index(R.paragraphs(R.target_page(s, page)[1])):
                    e.append(f"p {n} is not a paragraph of {page}")
            except (TypeError, ValueError):
                e.append("p (the paragraph) is required for an antecedent line")
        if not e:
            r, _ = expand(ln, s, page, gid, n_ayat)
            e += [x.split(": ", 1)[1] for x in B.check_record(r, s, n_ayat, corpus, "")
                  if not re.search(r": (missing (paragraf|capa)|id code|id must)", x)]
            if page != "surah":
                a = int(page.split(":")[1])
                try:
                    if not any(x[1] <= a <= x[2] for x in B.ayah_refs(r.get("ayet", ""))):
                        e.append(f"ayet {r.get('ayet')} does not cover {page}")
                except ValueError:
                    pass
            e += [x.split(": ", 1)[1] for x in CK.quote_problems(con, r)]
            if B.words(r.get("metin", "")) > LINE_WORDS:
                warns.append(f"{lid}: metin {B.words(r['metin'])} words (aim for one sentence, ≤ {LINE_WORDS})")
        if e:
            errs.setdefault(lid, []).extend(e)
        else:
            good[lid] = ln
    for lid in [x for x in good if x in errs]:  # a repeated id: no occurrence is kept
        del good[lid]
    return good, errs, warns


def same_family(seg: str, loc: str) -> bool:
    return seg == loc or seg.startswith(loc + "#") or loc.startswith(seg + "#")


# ---------------------------------------------------------------- stage 1: extract (per group unit)

def build_extract_prompt(s: int, u: dict, g: dict, d: Path, model: str, material: str, files: list[Path]) -> str:
    gid = u["group"]
    py = f"python3 {V2 / 'grup.py'}"
    lines = ["# Job", "",
             f"- Surah: {s}",
             f"- Unit: {u['id']} of group «{gid}»{' — a REQUIRED voice' if g.get('required') else ''}",
             f"- Pages this unit writes lines for: {', '.join(u['pages'])}",
             f"- PACK: {wd(s) / 'pack'} (binding.json: the ayah's words and their refs S:A:W)",
             f"- Your call directory (write only here): {d}",
             f"- Corpus tool: python3 {V2 / 'tools' / 'corpus.py'}",
             f"- Check (run it once you have written lines.jsonl; fix every FAIL): {py} lint --surah {s} --dir {d}",
             f"- Group focus: {g.get('odak', '')}",
             f"- Schema card (values of t, f and the fields some types require): {V2 / 'SCHEMA_CARD.md'}"]
    if gid == "oncul":
        lines += ["", "## Your input: the commentary's claims that no source line touched, per page and paragraph", ""]
    elif model == "opus":
        lines += ["", "## Files to read completely, once, at the start (in your call directory)", ""]
        lines += [f"- {f.name}" for f in files]
    else:
        lines += ["", f"## Your material: {len(u['items'])} segments, each opening with `### <locator>`; account for "
                      f"every one in kapsam.jsonl. It is all here: do not read copies of it from disk.", ""]
    head = "\n".join(lines) + "\n"
    parts = [head, (PROMPTS / "grup.md").read_text(encoding="utf-8")]
    extra = PROMPTS / f"grup_{gid}.md"
    if extra.exists():
        parts.append(extra.read_text(encoding="utf-8"))
    if material and (model != "opus" or gid == "oncul"):
        parts.append("# MATERIAL\n\n" + material)
    return "\n\n".join(parts)


def oncul_input(s: int, p: dict) -> str:
    """Every placement call's bos.jsonl (the base's claims no line touched), by page and paragraph."""
    out = []
    for page in p["pages"]:
        fr = finished_run(s, f"yer.{tag(page)}")
        if not fr or fr[1].get("status") == "error":
            raise SystemExit(f"oncul: page {page} has no usable placement ({'error' if fr else 'not finished'}): "
                             f"place every page first")
        if fr[1].get("status") == "incomplete":
            print(f"NOTE: oncul: placement of {page} finished incomplete: {fr[1].get('problems')}")
        rows, bad = read_jsonl(fr[0] / "bos.jsonl")
        for b in bad:
            print(f"WARNING: yer.{tag(page)}: {b}")
        out.append(f"## {page}\n" + "".join(f"- ¶{x.get('p')}: {x.get('iddia')}\n" for x in rows))
    return "\n".join(out)


def prepare(s: int, uid: str, model: str, effort: str, dry: Path | None = None) -> dict:
    p = load_plan(s)
    check_plan(s, p)
    u = next((x for x in p["units"] if x["id"] == uid), None)
    if not u or u["group"] == "yer":
        raise SystemExit(f"no extraction unit {uid} in the plan (placement calls are prepared with `place`)")
    done = started_before(s, uid)
    if done and dry is None:
        return {"unit": uid, "status": "skipped", "reason": f"prepared or run before ({', '.join(done)}): never rerun"}
    d = call_dir(s, uid, model, effort) if dry is None else dry / f"{uid}.{model}.{effort}"
    g = next(x for x in GROUPS["groups"] if x["id"] == u["group"])
    if g["id"] == "oncul":
        material = oncul_input(s, p)
    else:
        con = sqlite3.connect(f"file:{C.INDEX}?mode=ro", uri=True)
        pool, _ = group_items(con, s, g, [x for x in g["sources"] if x in held_sources()])
        by = {i["seg"]: i for i in pool}
        missing = [x for x in u["items"] if x not in by]
        if missing:
            raise SystemExit(f"{uid}: {len(missing)} planned segments no longer found ({missing[:5]}): plan again")
        material = "".join(by[x]["text"] + "\n" for x in u["items"])
    d.mkdir(parents=True, exist_ok=True)
    files = split_files(material, "material", d) if material and model == "opus" and g["id"] != "oncul" else []
    if material and not files:
        (d / "material.md").write_text(material, encoding="utf-8")  # the inlined text, kept for reference
    prompt = build_extract_prompt(s, u, g, d, model, material, files)
    reads = [{"path": str(f), "lines": len(f.read_text(encoding="utf-8").splitlines()),
              "pages": [[1, len(f.read_text(encoding="utf-8").splitlines())]]} for f in files]
    row = {"surah": s, "unit": uid, "group": u["group"], "stage": "grup-extract", "pages": u["pages"],
           "items": len(u["items"]), "required_reads": reads, "estimate_usd_opus": u["usd"],
           "pack_sha256": p["pack_sha256"]}
    if dry is not None:
        (d / "prompt.md").write_text(prompt, encoding="utf-8")
        return {"unit": uid, "status": "dry", "dir": str(d), "prompt_tokens": est_tokens(prompt)}
    return write_call(s, d, uid, model, effort, prompt, row, "kapsam.jsonl" if u["items"] else "lines.jsonl")


def lint_cmd(s: int, d: Path) -> None:
    """The agent's check: FAIL lines (the line is dropped if it still fails at finish), WARN lines, a summary."""
    st = json.loads((d / "started.json").read_text(encoding="utf-8")) if (d / "started.json").exists() else None
    uid = st["unit"] if st else d.name.split(".")[0] + "." + d.name.split(".")[1]
    u = next(x for x in load_plan(s)["units"] if x["id"] == uid)
    good, errs, warns = lint_lines(s, d, u, u["group"])
    for lid, e in errs.items():
        for x in e:
            print(f"FAIL {lid}: {x}")
    for w in warns:
        print(f"WARN {w}")
    print(f"{len(good) + len(errs)} lines: {len(good)} pass, {len(errs)} fail, {len(warns)} warnings")


def finish(s: int, uid: str, model: str, effort: str) -> dict:
    d = call_dir(s, uid, model, effort)
    stop = reopen(d, uid)
    if stop:
        return stop
    row = json.loads((d / "started.json").read_text(encoding="utf-8"))
    u = next(x for x in load_plan(s)["units"] if x["id"] == uid)
    g = next(x for x in GROUPS["groups"] if x["id"] == u["group"])
    problems: list[str] = []
    run_usage(d, model, row.get("output", "kapsam.jsonl"), row, problems)
    good, errs, warns = lint_lines(s, d, u, u["group"])
    for lid, e in errs.items():
        print(f"DROPPED {uid} {lid}: {'; '.join(e)}")
    for w in warns:
        print(f"NOTE: {uid}: {w}")
    row["lines"] = {"kept": sorted(good), "dropped": errs, "warnings": warns}
    # kapsam: every segment once; a used segment's locator stands in the pointers (k) of the lines it names
    kap, bad, yok = {}, [], {}
    rows, nb = read_jsonl(d / "kapsam.jsonl")
    bad += nb
    for x in rows:
        if x.get("page"):
            if x["page"] not in u["pages"]:
                bad.append(f"a yok line for {x['page']}, not a page of this unit")
            yok[x["page"]] = x.get("neden", "")
            continue
        seg = x.get("seg")
        if not isinstance(seg, str) or not seg:
            bad.append(f"a kapsam line without seg: {json.dumps(x, ensure_ascii=False)[:80]}")
            continue
        if seg in kap:
            bad.append(f"{seg} listed twice")
        if x.get("durum") not in KAPSAM:
            bad.append(f"{seg}: durum {x.get('durum')!r} not one of {sorted(KAPSAM)}")
        if x.get("durum") == "kullanildi":
            named = [good[i] for i in x.get("satir") or [] if i in good]
            if not named:
                bad.append(f"{seg}: kullanildi, but none of its lines {x.get('satir') or '(none)'} was kept")
            elif not any(same_family(seg, loc.strip()) for ln in named for loc in str(ln.get("k", "")).split("|")):
                bad.append(f"{seg}: kullanildi, but its locator is in no k of its lines {x.get('satir')} (pointer lost)")
        kap[seg] = x
    missing = [x for x in u["items"] if x not in kap]
    extra = [x for x in kap if x not in set(u["items"])]
    if missing:
        bad.append(f"{len(missing)} material segments not in kapsam.jsonl: {missing[:8]}")
    if extra:
        bad.append(f"kapsam names {len(extra)} segments that are not this unit's material: {extra[:8]}")
    voice = {}
    if g.get("required"):
        for page in u["pages"]:
            voice[page] = ("lines" if any(ln.get("pg") == page for ln in good.values()) else
                           f"yok: {yok[page]}" if page in yok else "MISSING: no line and no recorded reason")
        silent = [pg for pg, v in voice.items() if v.startswith("MISSING")]
        if silent:
            bad.append(f"required voice silent on {silent}")
    for b in bad:
        print(f"WARNING: {uid}: {b}")
    gaps = {}
    if (d / "gaps.json").exists():
        try:
            gaps = json.loads((d / "gaps.json").read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            bad.append("gaps.json is not JSON")
    else:
        bad.append("no gaps.json")
    row["gaps"] = gaps
    if isinstance(gaps, dict) and (gaps.get("missing_sources") or gaps.get("not_found")):
        print(f"NOTE: {uid}: gaps: missing {gaps.get('missing_sources')}; not found {gaps.get('not_found')}")
    row["kapsam"] = {"listed": len(kap), "planned": len(u["items"]), "missing": missing, "not_planned": extra,
                     "by_durum": dict(Counter(x.get("durum") for x in kap.values())), "required_voice": voice}
    row = close_run(d, row, problems, bad)
    print(f"{uid}: {row['status']}; {len(good)} lines kept, {len(errs)} dropped; kapsam {len(kap)}/{len(u['items'])}")
    return row


# ---------------------------------------------------------------- stage 2: place (per page)

def page_lines(s: int, p: dict, page: str) -> tuple[list[dict], list[str], dict]:
    """Every kept line for a page from the finished extraction units (oncul excluded), ids made global
    (<unit>/<line id>); units covering the page that are not finished or ended in error are named, and so are
    incomplete ones with their problems."""
    out, missing, incomplete = [], [], {}
    for u in p["units"]:
        if u["group"] in ("yer", "oncul") or page not in u["pages"]:
            continue
        fr = finished_run(s, u["id"])
        if not fr or fr[1].get("status") == "error":
            missing.append(u["id"] + ("" if not fr else " (error)"))
            continue
        if fr[1].get("status") == "incomplete":
            incomplete[u["id"]] = fr[1].get("problems")
        lines, _ = read_jsonl(fr[0] / "lines.jsonl")
        keep = set(fr[1].get("lines", {}).get("kept", []))
        for ln in lines:
            if ln.get("id") and str(ln["id"]) in keep and ln.get("pg") == page:
                out.append({"id": f"{u['id']}/{ln['id']}", **{k: v for k, v in ln.items() if k not in ("id", "pg")}})
    return out, missing, incomplete


def wkey(ln: dict) -> tuple:
    w = ln.get("w")
    return (0, w[0]) if isinstance(w, list) and w else (1 if w == "ayah" else 2, "")


def place(s: int, page: str, model: str, effort: str, dry: Path | None = None, allow_missing: bool = False) -> dict:
    p = load_plan(s)
    check_plan(s, p)
    uid = f"yer.{tag(page)}"
    if page not in p["pages"]:
        raise SystemExit(f"no page {page} in the plan")
    done = started_before(s, uid)
    if done and dry is None:
        return {"unit": uid, "status": "skipped", "reason": f"prepared or run before ({', '.join(done)}): never rerun"}
    lines, missing, incomplete = page_lines(s, p, page)
    if missing and not allow_missing:
        raise SystemExit(f"{uid}: extraction units for {page} not finished or in error: {missing} "
                         f"(--allow-missing places the page without them, recorded)")
    if missing:
        print(f"WARNING: {uid}: placed WITHOUT the lines of {len(missing)} units: {missing}")
    for k, v in incomplete.items():
        print(f"NOTE: {uid}: {k} finished incomplete: {v}")
    lines.sort(key=lambda x: (wkey(x), str(x.get("t")), x["id"]))
    d = call_dir(s, uid, model, effort) if dry is None else dry / f"{uid}.{model}.{effort}"
    d.mkdir(parents=True, exist_ok=True)
    body = "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lines)
    (d / "input_lines.jsonl").write_text(body, encoding="utf-8")
    text = numbered_text(s, page)
    head = ["# Job", "", f"- Surah: {s}; page {page}", f"- Your call directory (write only here): {d}",
            f"- Check (run it once you have written yer.jsonl and bos.jsonl; fix every FAIL): python3 {V2 / 'grup.py'} "
            f"lint-place --surah {s} --dir {d}",
            f"- Lines to place: {len(lines)} (every id exactly once in yer.jsonl)"]
    files = []
    if model == "opus":
        files = split_files(text, "page", d) + split_files(body, "lines", d)
        head += ["", "## Files to read completely, once, at the start (in your call directory)", ""]
        head += [f"- {f.name}" for f in files]
    prompt = "\n".join(head) + "\n\n" + (PROMPTS / "grup_yer.md").read_text(encoding="utf-8")
    if model != "opus":
        prompt += f"\n\n# THE PAGE ({page}, numbered)\n\n{text}\n\n# THE LINES\n\n{body}"
    row = {"surah": s, "unit": uid, "group": "yer", "stage": "grup-place", "pages": [page], "lines": len(lines),
           "units_missing": missing, "units_incomplete": incomplete,
           "required_reads": [{"path": str(f), "lines": len(f.read_text(encoding="utf-8").splitlines()),
                               "pages": [[1, len(f.read_text(encoding="utf-8").splitlines())]]} for f in files],
           "estimate_usd_opus": next((u["usd"] for u in p["units"] if u["id"] == uid), None),
           "pack_sha256": p["pack_sha256"]}
    if dry is not None:
        (d / "prompt.md").write_text(prompt, encoding="utf-8")
        return {"unit": uid, "status": "dry", "dir": str(d), "prompt_tokens": est_tokens(prompt), "lines": len(lines)}
    return write_call(s, d, uid, model, effort, prompt, row, "yer.jsonl")


YER_KEYS = {"id", "p", "kat", "f", "guc", "gerekce", "c", "rep", "elenen"}


def check_place(s: int, d: Path, page: str) -> tuple[dict[str, dict], list[str]]:
    """yer.jsonl against the input lines: every id exactly once, placed (a paragraph of the page) or rejected with a
    reason; clusters with exactly one representative; values in the schema; bos.jsonl paragraphs exist."""
    inp = {x["id"]: x for x in read_jsonl(d / "input_lines.jsonl")[0]}
    rows, bad = read_jsonl(d / "yer.jsonl")
    paras = R.paragraphs(R.target_page(s, page)[1])
    nums = R.prose_index(paras)
    got, reps = {}, defaultdict(list)
    for x in rows:
        i = x.get("id")
        if i not in inp:
            bad.append(f"{i}: not an input line")
            continue
        if i in got:
            bad.append(f"{i}: listed twice")
        unknown = [k for k in x if k not in YER_KEYS]
        if unknown:
            bad.append(f"{i}: unknown keys {unknown}")
        if not x.get("elenen"):
            try:
                if int(x.get("p")) not in nums:
                    bad.append(f"{i}: p {x.get('p')} is not a paragraph of {page} (1-{len(nums)})")
            except (TypeError, ValueError):
                bad.append(f"{i}: needs p (a paragraph number) or elenen (a reason)")
        for k, enum in (("kat", "kat"), ("f", "islev"), ("guc", "guc")):
            if x.get(k) and x[k] not in B.ENUMS[enum]:
                bad.append(f"{i}: {k}={x[k]!r} not in {sorted(B.ENUMS[enum])}")
        if x.get("f") == "itiraz" and not x.get("gerekce"):
            bad.append(f"{i}: f itiraz needs gerekce (why the paragraph's reading cannot hold)")
        if x.get("f") == "oncul" and not x.get("guc"):
            bad.append(f"{i}: f oncul needs guc")
        if x.get("rep") and x.get("elenen"):
            bad.append(f"{i}: a cluster representative cannot be elenen")
        if x.get("rep") and not x.get("c"):
            bad.append(f"{i}: rep without a cluster c")
        if x.get("c"):
            reps[x["c"]].append(bool(x.get("rep")) and not x.get("elenen"))
        if i not in got:
            got[i] = x
    for c, r in reps.items():
        if sum(r) != 1:
            bad.append(f"cluster {c}: {sum(r)} representatives (exactly one)")
    lost = [i for i in inp if i not in got]
    if lost:
        bad.append(f"{len(lost)} input lines not in yer.jsonl: {lost[:8]}")
    bos, nb = read_jsonl(d / "bos.jsonl")
    bad += nb
    for x in bos:
        try:
            if int(x.get("p")) not in nums or not x.get("iddia"):
                bad.append(f"bos: ¶{x.get('p')} not a paragraph or no iddia")
        except (TypeError, ValueError):
            bad.append(f"bos: p {x.get('p')!r} is not a number")
    return got, bad


def lint_place_cmd(s: int, d: Path) -> None:
    page = json.loads((d / "started.json").read_text(encoding="utf-8"))["pages"][0] if (d / "started.json").exists() \
        else d.name.split(".")[1].replace("_", ":").replace("surah", "surah")
    got, bad = check_place(s, d, page)
    for b in bad:
        print(f"FAIL {b}")
    print(f"{len(got)} placements checked: {len(bad)} problems")


def finish_place(s: int, page: str, model: str, effort: str) -> dict:
    uid = f"yer.{tag(page)}"
    d = call_dir(s, uid, model, effort)
    stop = reopen(d, uid)
    if stop:
        return stop
    row = json.loads((d / "started.json").read_text(encoding="utf-8"))
    problems: list[str] = []
    run_usage(d, model, "yer.jsonl", row, problems)
    got, bad = check_place(s, d, page)
    for b in bad:
        print(f"WARNING: {uid}: {b}")
    row["placed"] = sum(1 for x in got.values() if not x.get("elenen"))
    row["rejected"] = {i: x["elenen"] for i, x in got.items() if x.get("elenen")}
    row["clusters"] = len({x["c"] for x in got.values() if x.get("c")})
    row["unclaimed_claims"] = len(read_jsonl(d / "bos.jsonl")[0])
    for i, why in row["rejected"].items():
        print(f"NOTE: {uid}: {i} rejected: {why}")
    row = close_run(d, row, problems, bad)
    print(f"{uid}: {row['status']}; placed {row['placed']}, rejected {len(row['rejected'])}, clusters {row['clusters']}, "
          f"claims with no line {row['unclaimed_claims']}")
    return row


# ---------------------------------------------------------------- merge

def capa_for(paras: list[str], n: int) -> str | None:
    """Five consecutive words of prose paragraph n outside the Arabic tags, that render.locate finds there."""
    i = R.prose_index(paras).get(n)
    if i is None:
        return None
    toks, depth, ok = R.squash(paras[i]).split(), 0, []
    for t in toks:
        ok.append(depth == 0 and "{" not in t and "}" not in t)
        depth += t.count("{") - t.count("}")
    for j in range(len(toks) - 4):
        if all(ok[j:j + 5]):
            cand = " ".join(toks[j:j + 5])
            if R.locate(paras, {"paragraf": n, "capa": cand})[0] is not None:
                return cand
    return None


def merge(s: int) -> dict:
    """Per page: the placed lines (one per input line; a cluster becomes its representative line, unchanged, with the
    union of every member's pointers and holders) and the antecedent lines, expanded into schema records (every
    defaulted field recorded), anchored by script (capa from the paragraph), checked, renumbered, rendered into
    work/sNNN/grup/pages/<page>/ (never out/). Rejections, drops and each required voice's state are listed."""
    p = load_plan(s)
    out = gdir(s) / "pages"
    n_ayat = json.loads((wd(s) / "pack" / "pack.json").read_text(encoding="utf-8"))["ayat"]
    res: dict = {"pages": {}, "units_not_finished": []}
    all_locs: set = set()
    group_of = {u["id"]: u["group"] for u in p["units"]}
    runs = {}
    for u in p["units"]:
        fr = finished_run(s, u["id"])
        if not fr:
            res["units_not_finished"].append(u["id"])
        elif fr[1].get("status") == "error":
            print(f"WARNING: {u['id']}: ended in error, not merged: {fr[1].get('problems')}")
            res["units_not_finished"].append(u["id"] + " (error)")
        else:
            runs[u["id"]] = fr
            if fr[1].get("status") == "incomplete":
                print(f"NOTE: {u['id']}: merged though incomplete: {fr[1].get('problems')}")
                res.setdefault("units_incomplete", {})[u["id"]] = fr[1].get("problems")
    if res["units_not_finished"]:
        print(f"WARNING: not finished or in error, their lines are missing: {res['units_not_finished']}")
    oncul = [(uid, fr) for uid, fr in runs.items() if group_of[uid] == "oncul"]
    for page in p["pages"]:
        t = tag(page)
        paras = R.paragraphs(R.target_page(s, page)[1])
        info: dict = {"rejected": {}, "unanchored": [], "dropped": []}
        built = []  # (record, provenance)
        yr = runs.get(f"yer.{t}")
        if yr:
            lines = {x["id"]: x for x in read_jsonl(yr[0] / "input_lines.jsonl")[0]}
            yer: dict[str, dict] = {}
            for x in read_jsonl(yr[0] / "yer.jsonl")[0]:
                i = x.get("id")
                if i not in lines:
                    info.setdefault("unknown_yer_ids", []).append(i)
                elif i in yer:
                    info.setdefault("duplicate_yer_rows", []).append(i)
                else:
                    yer[i] = x
            for i in lines:
                if i not in yer:
                    info.setdefault("unplaced", []).append(i)

            def p_of(x: dict) -> int | None:
                try:
                    return int(x.get("p"))
                except (TypeError, ValueError):
                    return None

            # a cluster is used only with exactly one representative that is placed; otherwise every member stands alone
            members, reps = defaultdict(list), defaultdict(list)
            for i, x in yer.items():
                if x.get("c") and not x.get("elenen"):
                    members[x["c"]].append(i)
                    if x.get("rep") and p_of(x) is not None:
                        reps[x["c"]].append(i)
            broken = {c for c in members if len(reps[c]) != 1}
            for c in broken:
                info.setdefault("clusters_without_one_rep", {})[c] = members[c]
            for i, x in yer.items():
                if x.get("elenen"):
                    info["rejected"][i] = x["elenen"]
                    continue
                c = x.get("c") if x.get("c") not in broken else None
                if c and i not in reps[c]:
                    continue  # a cluster member: its pointers and holders go to the representative
                if p_of(x) is None:
                    info.setdefault("unplaced", []).append(i)
                    continue
                ln = dict(lines[i])
                group_ids = members[c] if c else [i]
                ks, als = [], []
                for m in [i] + [g for g in group_ids if g != i]:
                    ks += [k.strip() for k in str(lines[m].get("k", "")).split("|") if k.strip()]
                    als += [a.strip() for a in str(lines[m].get("a", "")).split(";") if a.strip()]
                ln["k"] = "|".join(dict.fromkeys(ks))
                if als:
                    ln["a"] = "; ".join(dict.fromkeys(als))
                unit = i.split("/")[0]
                rec, dft = expand(ln, s, page, group_of.get(unit, ""), n_ayat)
                for k_line, k_rec in (("kat", "kat"), ("f", "islev"), ("guc", "guc"), ("gerekce", "gerekce")):
                    if x.get(k_line):
                        rec[k_rec] = x[k_line]
                        if k_rec in dft:
                            dft.remove(k_rec)
                rec["paragraf"] = p_of(x)
                built.append((rec, {"line": i, "unit": unit, "merged": [g for g in group_ids if g != i],
                                    "groups": sorted({group_of.get(g.split("/")[0], "") for g in group_ids}),
                                    "defaulted": dft}))
            for k in ("unknown_yer_ids", "duplicate_yer_rows", "unplaced", "clusters_without_one_rep"):
                if info.get(k):
                    print(f"WARNING: {page}: {k.replace('_', ' ')}: {info[k]}")
        elif any(page in u["pages"] for u in p["units"] if group_of[u["id"]] not in ("yer", "oncul")):
            print(f"WARNING: {page}: no finished placement: its extraction lines are not on the page")
            info["not_placed"] = True
        for uid, (d, lg) in oncul:
            keep = set(lg.get("lines", {}).get("kept", []))
            for ln in read_jsonl(d / "lines.jsonl")[0]:
                if str(ln.get("id")) in keep and ln.get("pg") == page:
                    rec, dft = expand(ln, s, page, "oncul", n_ayat)
                    rec["paragraf"] = int(ln["p"])  # lint checked it
                    built.append((rec, {"line": f"{uid}/{ln['id']}", "unit": uid, "merged": [], "groups": ["oncul"],
                                        "defaulted": dft}))
        recs, prov = [], {}
        for rec, pv in built:
            capa = capa_for(paras, rec["paragraf"])
            if not capa:
                info["unanchored"].append(pv["line"])
                print(f"WARNING: {page}: {pv['line']}: no anchor words found in ¶{rec['paragraf']}: not placed")
                continue
            rec["capa"] = capa
            recs.append(rec)
            prov[id(rec)] = pv
        recs.sort(key=lambda r: (int(r["paragraf"]), prov[id(r)]["line"]))

        def renumber(rs: list[dict]) -> None:
            n: Counter = Counter()
            for r in rs:
                kod = B.KOD.get(r.get("tur"), "XXX")
                n[kod] += 1
                r["id"] = f"S{s:03d}-{kod}-{n[kod]:03d}"

        renumber(recs)
        kept, dropped, warnings = VAL.check_records(s, page, recs, "islami") if recs else ([], [], [])
        by_id = {r["id"]: r for r in recs}
        for x in dropped:
            pv = prov[id(by_id[x["id"]])]
            info["dropped"].append({"line": pv["line"], "errors": x["errors"]})
            print(f"DROPPED {page} {pv['line']}: {'; '.join(x['errors'])}")
        renumber(kept)
        pd = out / t
        pd.mkdir(parents=True, exist_ok=True)
        (pd / "annotations.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in kept),
                                              encoding="utf-8")
        (pd / "provenance.json").write_text(json.dumps({r["id"]: prov[id(r)] for r in kept}, ensure_ascii=False,
                                                       indent=1) + "\n", encoding="utf-8")
        page_file, placement = R.render(s, page, kept, pd / "page")
        kept_groups = {gr for r in kept for gr in prov[id(r)]["groups"]}  # a cluster credits every member's group
        for r in kept:
            all_locs.update(k.strip() for k in str(r.get("kaynak", "")).split("|") if k.strip())
        voices = {}
        for gid, g in p["groups"].items():
            if not g.get("required"):
                continue
            if gid in kept_groups:
                voices[gid] = "on the page"
            elif page in g.get("pages_without_material", []):
                voices[gid] = "no material of this group for this page (plan)"
            else:
                why = [lg.get("kapsam", {}).get("required_voice", {}).get(page)
                       for uid, (_, lg) in runs.items() if group_of[uid] == gid]
                why = [w for w in why if w and w.startswith("yok")]
                lost_here = [i for i in list(info["rejected"]) + [x["line"] for x in info["dropped"]] + info["unanchored"]
                             + info.get("unplaced", []) if group_of.get(i.split("/")[0]) == gid]
                voices[gid] = (why[0] if why else
                               f"MISSING: its lines were rejected, dropped or not placed: {lost_here}" if lost_here else
                               "MISSING: no kept line and no recorded reason")
            if voices[gid].startswith("MISSING"):
                print(f"WARNING: {page}: required voice {gid}: {voices[gid]}")
        info.update(kept=len(kept), warnings=warnings, placement=placement, page=rel(page_file),
                    required_voices=voices,
                    defaults=dict(Counter(f for r in kept for f in prov[id(r)]["defaulted"])))
        res["pages"][page] = info
        print(f"{page}: {len(kept)} blocks; rejected {len(info['rejected'])}; dropped {len(info['dropped'])}; "
              f"unanchored {len(info['unanchored'])}")
    # the pointer ledger: every segment a unit used must reach a kept block of some page through its locator
    lost = {}
    for uid, (d, lg) in runs.items():
        if group_of[uid] in ("yer", "oncul"):
            continue
        for x in read_jsonl(d / "kapsam.jsonl")[0]:
            seg = x.get("seg")
            if x.get("durum") == "kullanildi" and isinstance(seg, str) and \
                    not any(same_family(seg, loc) for loc in all_locs):
                lost.setdefault(uid, []).append(seg)
    res["pointers_lost"] = lost
    if lost:
        print(f"WARNING: {sum(map(len, lost.values()))} used segments reach no kept block (their lines were rejected, "
              f"dropped, unanchored or not placed): " + "; ".join(f"{u}: {v[:5]}" for u, v in lost.items()))
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
    ap.add_argument("cmd", choices=["plan", "prepare", "lint", "finish", "place", "lint-place", "finish-place",
                                    "merge", "status"])
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--group")
    ap.add_argument("--unit")
    ap.add_argument("--page")
    ap.add_argument("--dir", type=Path, help="lint / lint-place: the call directory")
    ap.add_argument("--model", choices=sorted(MODELS), default="astra")
    ap.add_argument("--effort", default="high", help="the reasoning effort the call runs at (names its directory)")
    ap.add_argument("--write", action="store_true", help="plan: write plan.json (refused once a call is prepared)")
    ap.add_argument("--dry", type=Path, help="prepare/place: build the call's files in this directory only")
    ap.add_argument("--allow-missing", action="store_true",
                    help="place: place a page although some of its extraction units are not finished (recorded)")
    a = ap.parse_args()
    if a.cmd == "plan":
        p = plan(a.surah, a.group)
        print_plan(p)
        if a.write:
            if a.group:
                raise SystemExit("--write needs the whole plan (no --group)")
            if any(gdir(a.surah).glob("*.*.*/started.json")):
                raise SystemExit("calls of this plan are prepared or run: the plan is frozen")
            gdir(a.surah).mkdir(parents=True, exist_ok=True)
            (gdir(a.surah) / "plan.json").write_text(json.dumps(p, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print(f"wrote {rel(gdir(a.surah) / 'plan.json')}")
    elif a.cmd == "prepare":
        p = load_plan(a.surah)
        ids = [u["id"] for u in p["units"] if u["group"] not in ("yer", "oncul")] if a.unit == "all" else \
            [x for x in (a.unit or "").split(",") if x]
        if not ids:
            raise SystemExit("prepare needs --unit U[,U…] or --unit all (all = every extraction unit but oncul, "
                             "which runs after placement)")
        for uid in ids:
            print(json.dumps(prepare(a.surah, uid, a.model, a.effort, a.dry), ensure_ascii=False))
    elif a.cmd in ("lint", "lint-place"):
        if not a.dir:
            raise SystemExit(f"{a.cmd} needs --dir <call directory>")
        (lint_cmd if a.cmd == "lint" else lint_place_cmd)(a.surah, a.dir.resolve())
    elif a.cmd == "finish":
        if not a.unit:
            raise SystemExit("finish needs --unit U")
        r = finish(a.surah, a.unit, a.model, a.effort)
        if r.get("reason"):
            raise SystemExit(f"{a.unit}: {r['reason']}")
    elif a.cmd in ("place", "finish-place"):
        p = load_plan(a.surah)
        pgs = p["pages"] if a.page == "all" else [x for x in (a.page or "").split(",") if x]
        if not pgs:
            raise SystemExit(f"{a.cmd} needs --page P[,P…] or --page all")
        for pg in pgs:
            r = place(a.surah, pg, a.model, a.effort, a.dry, a.allow_missing) if a.cmd == "place" else \
                finish_place(a.surah, pg, a.model, a.effort)
            if a.cmd == "place":
                print(json.dumps(r, ensure_ascii=False))
            elif r.get("reason"):
                print(f"ERROR yer.{tag(pg)}: {r['reason']}")
    elif a.cmd == "merge":
        merge(a.surah)
    else:
        status(a.surah)


if __name__ == "__main__":
    main()
