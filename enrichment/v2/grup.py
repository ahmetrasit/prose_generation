#!/usr/bin/env python3
"""The hybrid enrichment workflow (HYBRID_PLAN.md Task C; user, 2026-10-05: "many passes … group by tradition …
small-enough groups per agent … each enrichment block is an independent unit, attached to the correct frozen v16
prose"). Every source is read by the group that claims it (groups.json); a group's material for a surah is packed
into as few units as fit `budget_chars`; one agent per unit reads a digest of the pages it covers plus its material,
writes records for those pages and accounts for every material segment in kapsam.jsonl. Units are independent: a
page's blocks are the union of all units' kept records (merge).

  python3 -B enrichment/v2/grup.py plan   --surah 1 [--group G]       units, material, estimated cost (no model call)
  python3 -B enrichment/v2/grup.py spawn  --surah 1 --unit U|all [--effort high]   prepare unit calls (spawn.md)
  python3 -B enrichment/v2/grup.py finish --surah 1 --unit U          after the agent replied: cost, coverage, checks
  python3 -B enrichment/v2/grup.py merge  --surah 1                   pages from all finished units (work dir only)
  python3 -B enrichment/v2/grup.py status --surah 1

Files: work/sNNN/grup/plan.json (the plan, frozen once a unit is prepared), work/sNNN/grup/<unit>.<model>.<effort>/
(a unit's call directory: prompt.md, digest.*.md, material.*.md, records.<page>[.n].jsonl, kapsam.jsonl, gaps.json,
check.json, run.log.json), work/sNNN/grup/pages/ (merged pages; never out/: acceptance is the user's).
No agent is ever spawned by this script: `spawn` prepares, the orchestrating session spawns with the user's go.
"""
from __future__ import annotations

import argparse
import hashlib
import json
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
FILE_CHARS = 24_000      # one material/digest file: one Read (the Read tool shows at most 25,000 tokens)
SEARCH_TOP = 6           # hits kept per (query, source) for search groups
COMMON_HITS = 150        # a phrase or pair with more hits than this in one source is too common there (recorded)
RARE_WORD = 25           # a single word is searched in a source only if it occurs at most this often there
DIGEST_HEAD, DIGEST_TAIL = 24, 10   # words of a paragraph shown in the digest (head … tail)
POINTER_LEXICA = ["LISAN", "LANE", "ASAS", "QAMUS", "TAJ", "MUHIT", "VASIT", "HANSWEHR"]
# cost model (HYBRID_PLAN C9; recalibrate after the first run): Opus 5.5 list rates
RATE = {"write": 5.0, "read": 0.20, "output": 20.0}
HARNESS_TOK, TURNS, THINK_TOK, REC_TOK = 5_300, 6, 15_000, 4_000


def wd(s: int) -> Path:
    return WORK / f"s{s:03d}"


def gdir(s: int) -> Path:
    return wd(s) / "grup"


def tag(page: str) -> str:
    return "surah" if page == "surah" else page.replace(":", "_")


def est_tokens(text_or_chars, ar_share: float | None = None) -> int:
    if isinstance(text_or_chars, str):
        t = text_or_chars
        ar = sum(1 for ch in t if "؀" <= ch <= "ۿ")
        return int(ar / 1.3 + (len(t) - ar) / 2.0)
    n = text_or_chars
    ar = n * (ar_share or 0.5)
    return int(ar / 1.3 + (n - ar) / 2.0)


def log(row: dict) -> None:
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def rel(p: Path) -> str:
    return str(p.relative_to(PG))


# ---------------------------------------------------------------- pages and digests

def pages(s: int) -> list[str]:
    n = json.loads((wd(s) / "pack" / "pack.json").read_text(encoding="utf-8"))["ayat"]
    have = [p for p in ["surah"] + [f"{s}:{a}" for a in range(1, n + 1)]
            if (wd(s) / "pack" / "numbered" / f"{tag(p)}.md").exists()]
    return have


TAG = re.compile(r"\{ar:[^{}]*?(?:source:([^,}]+))?\}")


def digest(s: int, page: str) -> str:
    """A page's numbered base in short: each paragraph cut to its first DIGEST_HEAD and last DIGEST_TAIL words, the
    Arabic citation tags shortened to their source («{ar… 11:41}»), headings, paragraph numbers and v16 addition
    markers kept. Anchoring needs only ¶n and three consecutive words of the paragraph as printed (a capa from the
    words shown outside the shortened tags); the agent reads a whole paragraph from PACK/numbered/<page>.md
    (Read with offset and limit) when the point needs more than the digest shows."""
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

def item_text(row, s: int) -> str:
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
    span = f"{rs}:{a}" + (f"-{a_end}" if a_end and a_end != a else "") if rs else "untied"
    lines = [f"### {seg}  [{span}]" + (f"  {head}" if head else "") + ("  {" + "; ".join(flags) + "}" if flags else ""),
             (text or "").strip()]
    for k in ("en", "tr", "notes"):
        if extra.get(k):
            lines.append(f"{k}: {C.flat(extra[k])}")
    return "\n".join(lines) + "\n"


def ayah_items(con, s: int, srcs: list[str], n_ayat: int) -> tuple[list[dict], list[str]]:
    """Segments of the group's sources tied to the surah: a tie of up to 3 ayat goes to its first ayah's page, a wider
    tie to the surah page. Duplicates (extra.duplicate) are listed, not read."""
    q = (f"SELECT seg,src,s,a,a_end,head,text,extra FROM seg WHERE s=? AND src IN ({','.join('?' * len(srcs))}) "
         f"ORDER BY src, a, id")
    items, dups = [], []
    rows = con.execute(q, [s] + srcs).fetchall()
    # two editions of one work (X and X-FULL): the short per-ayah edition is read whole; a full-edition segment
    # whose text is at least 80% inside the short edition's text for this surah is the same text: listed, not read
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
        # a narrow range (up to 3 ayat) belongs to its first ayah's page; a wider tie (an introduction, the whole
        # surah) to the surah page
        page = f"{s}:{a}" if a and b - a <= 2 else "surah"
        items.append({"seg": row[0], "src": row[1], "page": page, "chars": len(row[6] or ""), "text": item_text(row, s)})
    return items, dups


def grams5(text: str) -> set:
    t = re.sub(r"[^ء-ي]", "", C.norm(text))
    return {t[i:i + 5] for i in range(len(t) - 4)}


def cites_items(con, s: int, srcs: list[str]) -> list[dict]:
    """Segments of the group's sources that cite ayat of the surah without being tied to it: to the page of the
    ayah they cite (or the surah page when they cite several of its ayat)."""
    q = (f"SELECT seg.seg,seg.src,seg.s,seg.a,seg.a_end,seg.head,seg.text,seg.extra,ref.a,ref.a_end FROM ref JOIN seg "
         f"ON seg.id=ref.seg_id WHERE ref.s=? AND seg.src IN ({','.join('?' * len(srcs))}) ORDER BY seg.id")
    by: dict[str, dict] = {}
    for r in con.execute(q, [s] + srcs):
        x = by.setdefault(r[0], {"row": r[:8], "ayat": set()})
        x["ayat"].update(range(r[8], (r[9] or r[8]) + 1))
    out = []
    for seg, x in by.items():
        ay = sorted(x["ayat"])
        page = f"{s}:{ay[0]}" if len(ay) == 1 else "surah"
        row = list(x["row"])
        full = row[6] or ""
        text = excerpt(full, s, ay)
        if len(text) < len(full):
            row[6] = text + f"\n[excerpt around the citations: {len(text):,} of {len(full):,} characters; the whole " \
                            f"segment: corpus.py get {seg}]"
        out.append({"seg": seg, "src": row[1], "page": page, "chars": len(row[6]), "cites": ay,
                    "text": item_text(tuple(row), s).replace("\n", f"\n(cites {s}:{','.join(map(str, ay))})\n", 1)})
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
    for i, (a, b) in enumerate(merged):
        parts.append(("… " if a > 0 else "") + text[a:b] + (" …" if b < len(text) else ""))
    return "\n[…]\n".join(parts)


def binding(s: int) -> dict:
    return json.loads((wd(s) / "pack" / "binding.json").read_text(encoding="utf-8"))


def root_items(con, s: int, srcs: list[str]) -> list[dict]:
    """The lexica of the surah's bound roots: the pack's root file (project dictionary + the six classical lexica in
    full) and the full entries of the further lexica the group claims; one item per root, on the page of the first
    ayah that binds it."""
    first: dict[str, str] = {}
    names: dict[str, str] = {}
    for ref, words in binding(s).items():
        for w in words:
            for idn in w.get("identity") or []:
                first.setdefault(idn["root_id"], ref)
                names[idn["root_id"]] = idn["root"]
    out = []
    for rid, ref in sorted(first.items(), key=lambda x: (int(x[1].split(":")[1]), x[0])):
        f = wd(s) / "pack" / "roots" / f"{rid}.md"
        parts = [f.read_text(encoding="utf-8")] if f.exists() else [f"# {names[rid]} ({rid}): no pack root file\n"]
        key = names[rid].replace(" ", "")
        for sid in [x for x in POINTER_LEXICA if x in srcs]:
            rows = con.execute("SELECT seg,src,s,a,a_end,head,text,extra FROM seg WHERE src=? AND (seg=? OR "
                               "(seg>=? AND seg<?))", (sid, f"{sid}:{key}", f"{sid}:{key}#", f"{sid}:{key}$")).fetchall()
            parts += [item_text(r, s) for r in rows] or [f"### {sid}: no entry under {key}\n"]
        text = "\n".join(parts)
        out.append({"seg": f"root:{rid}", "src": "lexica", "page": ref, "chars": len(text),
                    "text": f"## Root {names[rid]} ({rid}), first bound in {ref}\n\n{text}\n"})
    return out


def search_items(con, s: int, gid: str, srcs: list[str]) -> tuple[list[dict], list[dict]]:
    """Script-run searches (HYBRID_PLAN C8), recorded: each ayah's content words (and, for hadith, the ayah's
    opening phrase, sahih only) in the group's sources; SEARCH_TOP hits per (query, source); a word with more than
    COMMON_HITS index hits is not searched (listed)."""
    quran = {a: t for a, t in con.execute("SELECT a, text FROM seg WHERE src='QURAN' AND s=?", (s,))}
    queries, items, seen = [], [], set()
    sahih = gid == "hadis"
    for ref, words in sorted(binding(s).items(), key=lambda x: int(x[0].split(":")[1])):
        a = int(ref.split(":")[1])
        terms = []
        aw = C.norm(quran.get(a, "")).split()
        if len(aw) >= 2:
            terms.append(("phrase", " ".join(aw[:6])))
            terms += [("pair", f"{aw[i]} {aw[i + 1]}") for i in range(len(aw) - 1)]
        for w in words:
            if any(p in (w.get("pos") or "") for p in ("N", "V", "ADJ", "PN")):
                surface = C.norm(re.sub(r"[ًٌٍَُِّْٰٓ]", "", w.get("surface") or "")).strip()
                if len(surface) >= 3:
                    terms.append(("word", surface))
        seen_terms = set()
        terms = [x for x in terms if not (x[1] in seen_terms or seen_terms.add(x[1]))]
        for kind, term in terms:
            fq = f'"{term}"'
            rec = {"ayah": ref, "kind": kind, "query": term, "per_source": {}, "too_common_in": []}
            got = 0
            for sid in srcs:
                n = con.execute("SELECT count(*) FROM f JOIN seg ON seg.id=f.rowid WHERE f MATCH ? AND seg.src=?",
                                (fq, sid)).fetchone()[0]
                rec["per_source"][sid] = n
                if n > (RARE_WORD if kind == "word" else COMMON_HITS):  # too frequent in this source: no signal
                    rec["too_common_in"].append(sid)
                    continue
                sql = ("SELECT seg.seg,seg.src,seg.s,seg.a,seg.a_end,seg.head,seg.text,seg.extra FROM f JOIN seg ON "
                       "seg.id=f.rowid WHERE f MATCH ? AND seg.src=?" + (" AND json_extract(seg.extra,'$.sahih')=1"
                                                                          if sahih else "") + " ORDER BY rank LIMIT ?")
                for r in con.execute(sql, (fq, sid, SEARCH_TOP)):
                    got += 1
                    if r[0] in seen:
                        continue
                    seen.add(r[0])
                    items.append({"seg": r[0], "src": r[1], "page": ref, "chars": len(r[6] or ""),
                                  "text": item_text(r, s).replace("\n", f"\n(found by «{term}», for {ref})\n", 1)})
            rec["kept"] = got
            queries.append(rec)
    return items, queries


def dictionary_items(s: int) -> list[dict]:
    """The lexicon group's material (user, 2026-10-05: «I already have dictionaries built — why spend so much on
    dictionaries»): the project dictionary's section for each ayah (PACK ayah/S_A/dictionary.md: every branch of every
    bound root, early phrases whole), which was built from the six classical lexica. A lexicon's own entry is opened
    only for a block that cites it (pack roots/<root_id>.md for the six, corpus.py get for the others)."""
    out = []
    for p in pages(s):
        if p == "surah":
            continue
        f = wd(s) / "pack" / "ayah" / tag(p) / "dictionary.md"
        if f.exists():
            text = f.read_text(encoding="utf-8")
            out.append({"seg": f"dictionary:{p}", "src": "PROJE", "page": p, "chars": len(text), "text": text + "\n"})
    return out


def meal_items(s: int) -> list[dict]:
    out = []
    for p in pages(s):
        if p == "surah":
            continue
        d = wd(s) / "pack" / "ayah" / tag(p)
        text = "\n".join((d / n).read_text(encoding="utf-8") for n in ("words.md", "meals.md", "turkish.md")
                         if (d / n).exists())
        out.append({"seg": f"meals:{p}", "src": "pack", "page": p, "chars": len(text), "text": text})
    return out


# ---------------------------------------------------------------- plan

def pack_units(items: list[dict], budget: int, page_order: list[str]) -> list[list[dict]]:
    """Items in page order (surah page first, then the ayat), packed into as few units as fit the budget; an item
    larger than the budget is a unit alone (said in the plan)."""
    order = {p: i for i, p in enumerate(page_order)}
    items = sorted(items, key=lambda x: (order.get(x["page"], 999), x["src"], x["seg"]))
    units, cur, n = [], [], 0
    for it in items:
        if cur and n + it["chars"] > budget:
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
    text = "".join((PROMPTS / n).read_text(encoding="utf-8") for n in ("common.md", "grup.md") if (PROMPTS / n).exists())
    text += (V2 / "SCHEMA_CARD.md").read_text(encoding="utf-8")
    return est_tokens(text) + 600


def plan(s: int, only: str | None = None) -> dict:
    con = sqlite3.connect(f"file:{C.INDEX}?mode=ro", uri=True)
    pg = pages(s)
    n_ayat = json.loads((wd(s) / "pack" / "pack.json").read_text(encoding="utf-8"))["ayat"]
    budget = GROUPS["budget_chars"]
    dig = {p: digest(s, p) for p in pg}
    out = {"surah": s, "planned": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "budget_chars": budget, "pages": pg,
           "pack_sha256": hashlib.sha256((wd(s) / "pack" / "pack.json").read_bytes()).hexdigest(),
           "groups": {}, "units": []}
    for g in GROUPS["groups"]:
        gid, mat, srcs = g["id"], g.get("material"), list(g["sources"])
        if only and gid != only:
            continue
        held = [x for x in srcs if x in {r[0] for r in con.execute("SELECT id FROM src WHERE access!='hafiza'")}]
        rec = {"material": mat, "sources": srcs, "held": held, "pointers": [x for x in srcs if x not in held],
               "required": bool(g.get("required"))}
        if mat == "ayah":
            items, dups = ayah_items(con, s, held, n_ayat)
            rec["duplicates_listed_not_read"] = dups
        elif mat == "cites":
            items = cites_items(con, s, held)
        elif mat == "root":
            items = dictionary_items(s)
            rec["read_through"] = ("the project dictionary (PACK ayah/S_A/dictionary.md), built from the six classical "
                                   "lexica; entries of any lexicon opened on demand for the blocks that cite them")
        elif mat == "search":
            items, rec["queries"] = search_items(con, s, gid, held)
        elif mat == "meal":
            items = meal_items(s)
        else:  # none: the antecedent search unit reads the digests and searches itself
            items = []
        rec["items"] = len(items)
        rec["chars"] = sum(i["chars"] for i in items)
        rec["by_source"] = dict(Counter(i["src"] for i in items))
        rec["no_material_sources"] = [x for x in held if x not in rec["by_source"]] if mat in ("ayah", "cites", "search") else []
        out["groups"][gid] = rec
        if mat == "none":
            groups_units = [[]]
        elif not items:
            rec["unit_note"] = "no material for this surah: no unit (required groups: every page records why)"
            groups_units = [] if not g.get("required") else [[]]
        else:
            groups_units = pack_units(items, budget, pg)
        bt = brief_tokens(gid)
        for k, us in enumerate(groups_units, 1):
            covered = sorted({i["page"] for i in us}, key=pg.index) or pg
            if any(i["page"] == "surah" for i in us) or mat in ("none", "meal") or not us:
                covered = sorted(set(covered) | {"surah"}, key=pg.index)
            mat_chars = sum(i["chars"] for i in us)
            mat_tok = sum(est_tokens(i["text"]) for i in us)
            dig_tok = sum(est_tokens(dig[p]) for p in covered)
            cost = unit_cost(mat_tok, dig_tok, bt)
            out["units"].append({"id": f"{gid}.u{k:02d}", "group": gid, "pages": covered, "items": [i["seg"] for i in us],
                                 "item_pages": {i["seg"]: i["page"] for i in us},
                                 "material_chars": mat_chars, "material_tok": mat_tok, "digest_tok": dig_tok, **cost})
    out["total_usd"] = round(sum(u["usd"] for u in out["units"]), 2)
    return out, dig


def print_plan(p: dict) -> None:
    print(f"S{p['surah']}: {len(p['pages'])} pages; budget {p['budget_chars']:,} chars per unit; "
          f"{len(p['units'])} units; estimated ${p['total_usd']:.2f} (Opus list rates; model in grup.py, to recalibrate)")
    print(f"{'unit':<22} {'pages':>5} {'items':>6} {'material':>10} {'mat tok':>8} {'dig tok':>8} {'ctx tok':>8} {'$':>6}")
    for u in p["units"]:
        print(f"{u['id']:<22} {len(u['pages']):>5} {len(u['items']):>6} {u['material_chars']:>10,} {u['material_tok']:>8,} "
              f"{u['digest_tok']:>8,} {u['context_tok']:>8,} {u['usd']:>6.2f}")
    for gid, g in p["groups"].items():
        notes = []
        if g.get("pointers"):
            notes.append(f"pointers (no text): {', '.join(g['pointers'])}")
        if g.get("no_material_sources"):
            notes.append(f"no material for this surah: {', '.join(g['no_material_sources'])}")
        if g.get("duplicates_listed_not_read"):
            notes.append(f"duplicates listed, not read: {len(g['duplicates_listed_not_read'])}")
        if g.get("queries"):
            sk = [q["query"] for q in g["queries"] if q.get("skipped")]
            notes.append(f"{len(g['queries'])} searches" + (f", {len(sk)} too common: {' '.join(sk[:8])}" if sk else ""))
        if g.get("unit_note"):
            notes.append(g["unit_note"])
        if notes:
            print(f"  {gid}: " + "; ".join(notes))


# ---------------------------------------------------------------- spawn

def split_files(text: str, stem: str, d: Path) -> list[Path]:
    """Text cut at line ends into files of at most FILE_CHARS characters; a longer line continues in the next file,
    marked (no cut is silent)."""
    files, cur = [], ""
    for line in text.splitlines(keepends=True):
        while len(line) > FILE_CHARS:
            if cur:
                files.append(cur)
                cur = ""
            files.append(line[:FILE_CHARS] + "\n[continued in the next file]\n")
            line = line[FILE_CHARS:]
        if cur and len(cur) + len(line) > FILE_CHARS:
            files.append(cur)
            cur = ""
        cur += line
    if cur:
        files.append(cur)
    out = []
    for i, body in enumerate(files, 1):
        f = d / f"{stem}.{i}.md"
        f.write_text(body, encoding="utf-8")
        out.append(f)
    return out


def unit_dir(s: int, uid: str, effort: str) -> Path:
    return gdir(s) / f"{uid}.opus.{effort}"


def build_prompt(s: int, u: dict, g: dict, d: Path, digest_files: list[Path], material_files: list[Path]) -> str:
    gid = u["group"]
    pages_txt = ", ".join(u["pages"])
    lines = ["# Job", "",
             f"- Surah: {s}; ids use S{s:03d}",
             f"- Unit: {u['id']} of group «{gid}» (material: {g.get('material')}){' — a REQUIRED voice' if g.get('required') else ''}",
             f"- Pages this unit writes for: {pages_txt}",
             f"- Workspace root: {PG}", f"- PACK: {wd(s) / 'pack'}",
             f"- Your call directory (write only here): {d}",
             f"- Schema card: {V2 / 'SCHEMA_CARD.md'}",
             f"- Corpus tool: python3 {V2 / 'tools' / 'corpus.py'} (get, ayah, cites, search)",
             f"- Check, per page (run it; never write your own validator): python3 {V2 / 'tools' / 'check.py'} --surah {s} "
             f"--target <page> --annotations {d}/records.<page-tag>.jsonl",
             f"- Group focus: {g.get('odak', '')}",
             "", "## Files to read completely in your first turn (one Read each, in parallel)", ""]
    lines += [f"- {f}" for f in digest_files + material_files]
    if not material_files:
        lines += ["", "(This unit has no material files: " + (
            "the group searches itself; see the brief's section for this group)" if g.get("material") == "none" else
            "no segment of the group's sources concerns this surah; write kapsam lines saying so for every page)")]
    lines += ["", "## Material segments to account for in kapsam.jsonl (every one, exactly once)", ""]
    lines += [f"- {seg} → {u['item_pages'][seg]}" for seg in u["items"]] or ["- (none)"]
    parts = ["\n".join(lines) + "\n", (PROMPTS / "common.md").read_text(encoding="utf-8"),
             (PROMPTS / "grup.md").read_text(encoding="utf-8")]
    extra = PROMPTS / f"grup_{gid}.md"
    if extra.exists():
        parts.append(extra.read_text(encoding="utf-8"))
    return "\n\n".join(parts)


def spawn(s: int, uid: str, effort: str, dry: Path | None = None) -> dict:
    pf = gdir(s) / "plan.json"
    if not pf.exists():
        raise SystemExit("no plan: run `grup.py plan --surah S --write` first")
    p = json.loads(pf.read_text(encoding="utf-8"))
    pack_now = hashlib.sha256((wd(s) / "pack" / "pack.json").read_bytes()).hexdigest()
    if pack_now != p["pack_sha256"]:
        raise SystemExit("the pack changed since the plan: plan again")
    u = next((x for x in p["units"] if x["id"] == uid), None)
    if not u:
        raise SystemExit(f"no unit {uid} in the plan")
    d = unit_dir(s, uid, effort) if dry is None else dry / f"{uid}.opus.{effort}"
    if (d / "started.json").exists():
        return {"unit": uid, "status": "skipped", "reason": "prepared or started before (never rerun; a new try is a "
                                                             "new plan with the user's go)"}
    g = next(x for x in GROUPS["groups"] if x["id"] == u["group"])
    d.mkdir(parents=True, exist_ok=True)
    digest_files = []
    for page in u["pages"]:
        digest_files += split_files(digest(s, page), f"digest.{tag(page)}", d)
    con = sqlite3.connect(f"file:{C.INDEX}?mode=ro", uri=True)
    # the material, rebuilt from the plan's segment list (same order); a segment missing now stops the unit
    texts = material_texts(con, s, u, g)
    material_files = split_files("".join(texts), "material", d) if texts else []
    prompt = build_prompt(s, u, g, d, digest_files, material_files)
    reads = []
    for f in digest_files + material_files + [V2 / "SCHEMA_CARD.md"]:
        n = len(f.read_text(encoding="utf-8").splitlines())
        reads.append({"path": str(f), "lines": n, "pages": [[1, n]]})
    row = {"surah": s, "unit": uid, "group": u["group"], "pages": u["pages"], "items": len(u["items"]),
           "stage": "grup", "model": "opus", "model_id": "claude-opus-5-5", "effort": effort, "runner": "agent",
           "agent_type": f"enrich-page-{effort}", "required_reads": reads, "estimate_usd": u["usd"],
           "pack_sha256": p["pack_sha256"], "prompt_chars": len(prompt)}
    if dry is not None:  # a look at the unit as it would be prepared: no started.json, nothing marked
        (d / "prompt.md").write_text(prompt, encoding="utf-8")
        (d / "row.json").write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        return {"unit": uid, "status": "dry", "dir": str(d), "prompt_chars": len(prompt),
                "files": len(digest_files) + len(material_files)}
    AR.prepare(d, prompt, row, "grup", "kapsam.jsonl", lookup=False)
    return {"unit": uid, "status": "prepared", "dir": rel(d), "spawn": rel(d / "spawn.md"), "estimate_usd": u["usd"]}


def material_texts(con, s: int, u: dict, g: dict) -> list[str]:
    mat, srcs = g.get("material"), list(g["sources"])
    want = set(u["items"])
    if not want:
        return []
    if mat == "ayah":
        pool, _ = ayah_items(con, s, srcs, 0)
    elif mat == "cites":
        pool = cites_items(con, s, srcs)
    elif mat == "root":
        pool = dictionary_items(s)
    elif mat == "search":
        pool, _ = search_items(con, s, g["id"], srcs)
    elif mat == "meal":
        pool = meal_items(s)
    else:
        pool = []
    by = {i["seg"]: i for i in pool}
    missing = [x for x in u["items"] if x not in by]
    if missing:
        raise SystemExit(f"{u['id']}: {len(missing)} planned segments no longer found ({missing[:5]}): plan again")
    return [by[x]["text"] + "\n" for x in u["items"]]


# ---------------------------------------------------------------- finish

KAPSAM = {"kullanildi", "yeni_yok", "tekrar", "ilgisiz", "okunamadi"}


def finish(s: int, uid: str, effort: str) -> dict:
    import enrich as E  # the transcript audit (files read completely, spills, cuts)
    d = unit_dir(s, uid, effort)
    st = d / "started.json"
    if not st.exists():
        return {"unit": uid, "status": "error", "reason": "not prepared"}
    if (d / "run.log.json").exists():
        return {"unit": uid, "status": "error", "reason": "already finished; never twice"}
    row = json.loads(st.read_text(encoding="utf-8"))
    p = json.loads((gdir(s) / "plan.json").read_text(encoding="utf-8"))
    u = next(x for x in p["units"] if x["id"] == uid)
    obj = AR.finish(d, "kapsam.jsonl")
    row.update({"cost_usd": obj.get("total_cost_usd"), "cost_usd_est": obj.get("cost_usd_est"),
                "output_tokens_est": obj.get("output_tokens_est"), "num_turns": obj.get("num_turns"),
                "transcript": obj.get("transcript"), "stop_reason": obj.get("stop_reason"), "usage": obj.get("usage")})
    row["coverage"] = E.audit(d, obj.get("transcript"), row.get("required_reads") or [])
    # kapsam: every planned segment exactly once, with a known durum
    kap, bad = {}, []
    for i, line in enumerate((d / "kapsam.jsonl").read_text(encoding="utf-8").splitlines() if (d / "kapsam.jsonl").exists() else [], 1):
        if not line.strip():
            continue
        try:
            x = json.loads(line)
        except json.JSONDecodeError:
            bad.append(f"line {i}: not JSON")
            continue
        if x.get("seg") in kap:
            bad.append(f"line {i}: {x.get('seg')} listed twice")
        if x.get("durum") not in KAPSAM and not x.get("page"):
            bad.append(f"line {i}: durum {x.get('durum')!r} not one of {sorted(KAPSAM)}")
        kap[x.get("seg") or f"page:{x.get('page')}"] = x
    missing = [x for x in u["items"] if x not in kap]
    row["kapsam"] = {"listed": len(kap), "planned": len(u["items"]), "missing": missing, "problems": bad,
                     "by_durum": dict(Counter(x.get("durum") for x in kap.values()))}
    if missing:
        print(f"WARNING: {uid}: {len(missing)} material segments not accounted for in kapsam.jsonl: {missing[:8]}")
    # records per page: join parts, check
    checks = {}
    for page in u["pages"]:
        t = tag(page)
        parts = sorted(d.glob(f"records.{t}.[0-9]*.jsonl"), key=lambda q: int(q.suffixes[-2].lstrip(".")))
        whole = d / f"records.{t}.jsonl"
        if parts and not whole.exists():
            whole.write_text("".join(q.read_text(encoding="utf-8").rstrip("\n") + "\n" for q in parts), encoding="utf-8")
        if not whole.exists():
            checks[page] = {"records": 0}
            continue
        recs = R.load(whole)
        kept, dropped, warnings = VAL.check_records(s, page, recs, "islami")
        checks[page] = {"records": len(recs), "kept": len(kept), "dropped": dropped, "warnings": warnings}
    (d / "check.json").write_text(json.dumps(checks, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    row["records"] = {pg: {k: (len(v) if isinstance(v, list) else v) for k, v in c.items()} for pg, c in checks.items()}
    row["status"] = "ok" if not obj.get("is_error") else "error"
    row["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    (d / "run.log.json").write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log({k: row[k] for k in ("surah", "unit", "group", "stage", "model_id", "effort", "estimate_usd", "cost_usd",
                             "cost_usd_est", "num_turns", "status", "finished") if k in row})
    kept = sum(c.get("kept", 0) for c in checks.values())
    print(f"{uid}: kept {kept} records over {len(u['pages'])} pages; estimate ${u['usd']}, recorded "
          f"${row['cost_usd']}, estimated true ${row['cost_usd_est']}; kapsam {len(kap)}/{len(u['items'])}")
    return row


# ---------------------------------------------------------------- merge

def merge(s: int) -> dict:
    """Every finished unit's kept records, per page: ids renumbered per KOD in page order, checked again, rendered
    into work/sNNN/grup/pages/<page>/ (never out/). Near-duplicates (same locator after the same paragraph) are
    reported for review, never dropped."""
    out = gdir(s) / "pages"
    res = {}
    for page in pages(s):
        t = tag(page)
        recs = []
        for d in sorted(gdir(s).glob("*.opus.*")):
            log_f, f = d / "run.log.json", d / f"records.{t}.jsonl"
            if not log_f.exists() or not f.exists():
                continue
            for r in R.load(f):
                r["_unit"] = d.name
                recs.append(r)
        if not recs:
            continue
        kept, dropped, _ = VAL.check_records(s, page, [dict(r) for r in recs], "islami")
        ids = {r["id"] for r in kept}
        kept_full = [r for r in recs if r["id"] in ids]
        # renumber: S<sss>-<KOD>-<NNN> in paragraph order per KOD (unit ids may collide across units)
        kept_full.sort(key=lambda r: (int(re.sub(r"\D", "", str(r.get("paragraf"))) or 0), r["_unit"]))
        n: Counter = Counter()
        for r in kept_full:
            kod = r["id"].split("-")[1] if r["id"].count("-") >= 2 else "X"
            n[kod] += 1
            r["kaynak_birim"] = r.pop("_unit")
            r["id"] = f"S{s:03d}-{kod}-{n[kod]:03d}"
        near = defaultdict(list)
        for r in kept_full:
            for loc in str(r.get("kaynak", "")).split("|"):
                near[(str(r.get("paragraf")), loc.strip())].append(r["id"])
        dups = {f"¶{k[0]} {k[1]}": v for k, v in near.items() if len(v) > 1 and k[1] not in ("", "hafiza")}
        pd = out / t
        pd.mkdir(parents=True, exist_ok=True)
        clean = [{k: v for k, v in r.items() if k != "kaynak_birim"} for r in kept_full]
        (pd / "annotations.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in clean), encoding="utf-8")
        (pd / "provenance.json").write_text(json.dumps({r["id"]: r["kaynak_birim"] for r in kept_full}, indent=1) + "\n",
                                            encoding="utf-8")
        page_file, placement = R.render(s, page, clean, pd / "page")
        res[page] = {"records": len(recs), "kept": len(clean), "dropped_at_merge": len(recs) - len(kept),
                     "near_duplicates": dups, "placement": placement, "page": rel(page_file)}
    (out / "merge.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for page, r in res.items():
        print(f"{page}: kept {r['kept']} of {r['records']}; near-duplicates {len(r['near_duplicates'])}; {r['page']}")
    return res


def status(s: int) -> None:
    pf = gdir(s) / "plan.json"
    if not pf.exists():
        print("no plan")
        return
    p = json.loads(pf.read_text(encoding="utf-8"))
    for u in p["units"]:
        ds = sorted(gdir(s).glob(f"{u['id']}.opus.*"))
        st = "planned"
        for d in ds:
            st = ("finished" if (d / "run.log.json").exists() else "prepared") + f" ({d.name})"
        print(f"{u['id']:<22} ${u['usd']:>5.2f}  {st}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["plan", "spawn", "finish", "merge", "status"])
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--group")
    ap.add_argument("--unit")
    ap.add_argument("--effort", default="high", choices=["high", "medium"])
    ap.add_argument("--write", action="store_true", help="plan: write plan.json (refused once a unit is prepared)")
    ap.add_argument("--dry", type=Path, help="spawn: build the unit's files in this directory only (no started.json)")
    a = ap.parse_args()
    if a.cmd == "plan":
        p, _ = plan(a.surah, a.group)
        print_plan(p)
        if a.write:
            if any(gdir(a.surah).glob("*.opus.*/started.json")):
                raise SystemExit("units of this plan are prepared or run: the plan is frozen")
            gdir(a.surah).mkdir(parents=True, exist_ok=True)
            (gdir(a.surah) / "plan.json").write_text(json.dumps(p, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print(f"wrote {rel(gdir(a.surah) / 'plan.json')}")
    elif a.cmd == "spawn":
        p = json.loads((gdir(a.surah) / "plan.json").read_text(encoding="utf-8"))
        ids = [u["id"] for u in p["units"]] if a.unit == "all" else [x for x in (a.unit or "").split(",") if x]
        for uid in ids:
            print(json.dumps(spawn(a.surah, uid, a.effort, a.dry), ensure_ascii=False))
    elif a.cmd == "finish":
        finish(a.surah, a.unit, a.effort)
    elif a.cmd == "merge":
        merge(a.surah)
    else:
        status(a.surah)


if __name__ == "__main__":
    main()
