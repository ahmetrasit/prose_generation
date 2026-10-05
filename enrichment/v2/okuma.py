#!/usr/bin/env python3
"""Staged enrichment, stage 1: reading (user, 2026-10-04 night: "i'm ok to staged if it is better and more
efficient"). The 1:1 page cost ~$12.5 as one Opus agent that read ~0.5M characters over 88 turns, its context
growing from 28k to 510k tokens; the corpus ties 1.09M characters to 1:1. Here cheap readers (Sonnet subagents) read
EVERY segment in full, once, and write evidence cards with verbatim quotes that a script checks; one Opus call per
page then judges and writes the records from the cards (stage 2, not built yet).

  python3 -B enrichment/v2/okuma.py plan   --surah 1 --target 1:1   # the planner call: claims + search queries
  python3 -B enrichment/v2/okuma.py finish --surah 1 --target 1:1   # finish whatever calls have replied
  python3 -B enrichment/v2/okuma.py build  --surah 1 --target 1:1   # reading set + reader call dirs, cost estimate
  python3 -B enrichment/v2/okuma.py finish --surah 1 --target 1:1
  python3 -B enrichment/v2/okuma.py recall --surah 1 --target 1:1 --page work/s001/zengin.1_1.opus.high

Every call is spawned by the orchestrating session (Agent tool, subagent_type general-purpose, model sonnet, the
text of the call's spawn.md). Layout: work/sNNN/okuma.<tag>/plan/, …/cNN/ (one reader each), manifest.json,
cards.jsonl, rejected.jsonl, coverage.json.

The reading set: (a) every segment tied to the ayah (ranges included), all kinds except meal, translation and
quran, which go to the judge directly from the pack; (b) the classical lexica entries of the ayah's bound roots;
(c) the planner's search hits (hadith, wujūh, antecedents at other ayat …): a hit longer than HIT_WHOLE characters
is shown as windows around its matches, marked as such, the whole text reachable by locator. Nothing else is
shortened: a segment longer than PART_CHARS is read in parts by the same reader. Every exclusion, window and
dropped card is printed and recorded (no silent failures).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

V2 = Path(__file__).resolve().parent
PG = V2.parents[1]
WORK = V2 / "work"
PROMPTS = V2 / "prompts"
LEDGER = WORK / "ledger.jsonl"
sys.path.insert(0, str(V2 / "tools"))
sys.path.insert(0, str(PG / "_commentary" / "v16"))
import corpus as C  # noqa: E402
import agentrun  # noqa: E402

READER_MODEL = "claude-sonnet-5-5"   # the spawn uses model "sonnet"
FILE_CHARS = 28_000     # per material file: one Read each, under the Read tool's token cap
CHUNK_CHARS = 90_000    # material per reader
PART_CHARS = 60_000     # a longer segment is read in parts, never cut
HIT_WHOLE = 6_000       # a search hit up to this length is shown whole
WINDOW = 2_500          # otherwise: this many characters each side of a match
MAX_QUERIES, MAX_N = 40, 10
SKIP_KINDS = {"meal": "the judge reads the meal panel from the pack (meals.md) and fetches other meals itself",
              "translation": "ASAD-EN and ARBERRY are in the pack's meals.md for the judge",
              "quran": "the ayah text is in the page context"}
LEXICA = ["AYN", "JAMHARA", "TAHDHIB", "SIHAH", "MAQAYIS", "MUFRADAT", "LISAN", "ASAS", "FURUQ", "SAMIN-UMDA"]
CARD_TUR = {"tefsir_rivayet", "tefsir_dirayet", "nahiv", "belagat", "lugat", "vucuh", "kiraat", "hadis", "nuzul",
            "kelam", "fikih", "isari", "ayet_ayet", "nazm", "anlam_tarihi", "tarih", "diger"}
ILISKI = {"destek", "genisletme", "karsi", "yeni"}
# cost estimate: Arabic-heavy material at ~1.45 characters per token (measured on the 1:1 transcript), briefs and
# Turkish at ~2.1; a general-purpose subagent starts with ~28k tokens of system prompt and tools; cards ~12% of the
# material's tokens plus ~6k of thinking per reader (to be calibrated on the pilot)
SYSTEM_TOKENS, CARD_SHARE, THINK_TOKENS = 28_000, 0.12, 6_000


def tag(target: str) -> str:
    return target.replace(":", "_")


def rdir(s: int, target: str) -> Path:
    return WORK / f"s{s:03d}" / f"okuma.{tag(target)}"


def rel(p: Path) -> str:
    return str(p.relative_to(PG))


def warn(msg: str, sink: list | None = None) -> None:
    print(f"WARNING: {msg}")
    if sink is not None:
        sink.append(msg)


def log(row: dict) -> None:
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def wrap(text: str, width: int = 1800) -> str:
    import textwrap
    out = []
    for line in text.splitlines():
        out += textwrap.wrap(line, width, break_long_words=True, break_on_hyphens=False) or [""]
    return "\n".join(out)


def pack(s: int) -> Path:
    p = WORK / f"s{s:03d}" / "pack"
    if not (p / "binding.json").exists():
        sys.exit(f"no pack for surah {s}: build it first (enrich.py / pack.py)")
    return p


def ayah_text(con, s: int, a: int) -> str:
    r = con.execute("SELECT text FROM seg WHERE src='QURAN' AND s=? AND a=?", (s, a)).fetchone()
    return r[0] if r else ""


def write_call(d: Path, brief: str, header: str, sections: list[tuple[str, str]], kind: str, output: str,
               started: dict) -> Path:
    """prompt.md (brief, header, the list of material files) and m01.md … each under FILE_CHARS, so every file is
    one Read. A section longer than a file continues in the next, marked."""
    d.mkdir(parents=True, exist_ok=True)
    files, cur = [], ""
    for title, body in sections:
        block = f"\n===== {title} =====\n\n{wrap(body.rstrip())}\n"
        while block:
            room = FILE_CHARS - len(cur)
            if len(block) <= room:
                cur += block
                block = ""
            else:
                cut = block.rfind("\n", 0, room)
                cut = cut if cut > room // 2 else room
                cur += block[:cut] + f"\n[… continues in the next file]\n"
                files.append(cur)
                cur, block = f"[… continued: {title}]\n", block[cut:]
    if cur.strip():
        files.append(cur)
    names = []
    for i, text in enumerate(files, 1):
        name = f"m{i:02d}.md"
        (d / name).write_text(text, encoding="utf-8")
        names.append(name)
    listing = "\n".join(f"- {d / n}" for n in names)
    prompt = (f"{brief.rstrip()}\n\n{header.rstrip()}\n\n## Material files (read every one, completely, in order; "
              f"one Read each, no offset or limit)\n{listing}\n")
    started = {**started, "files": names, "material_chars": sum(map(len, files))}
    agentrun.prepare(d, prompt, started, kind, output=output, lookup=False)
    return d


# ---------------------------------------------------------------- plan

def cmd_plan(s: int, target: str) -> None:
    con, pk = C.connect(), pack(s)
    a = int(target.split(":")[1])
    d = rdir(s, target) / "plan"
    if (d / "started.json").exists():
        sys.exit(f"{rel(d)} was started already; a call is never rerun (move the dir aside if the user says so)")
    t = tag(target)
    tied = con.execute("SELECT count(*), sum(length(text)) FROM seg WHERE s=? AND a<=? AND coalesce(a_end,a)>=?",
                       (s, a, a)).fetchone()
    cat = []
    for sid, kind, meta in con.execute("SELECT id, kind, meta FROM src ORDER BY kind, id"):
        if kind in SKIP_KINDS:
            continue
        m = json.loads(meta)
        cat.append(f"- {sid} ({kind}): {m.get('title') or ''}" + (f" — {m['author']}" if m.get("author") else "")
                   + (" [memory pointer: no text]" if m.get("access") == "hafiza" else ""))
    sections = [(f"THE BASE: PACK/numbered/{t}.md", (pk / "numbered" / f"{t}.md").read_text(encoding="utf-8"))]
    for name in ("words", "dictionary", "usage"):
        f = pk / "ayah" / t / f"{name}.md"
        if f.exists():
            sections.append((f"PACK/ayah/{t}/{name}.md", f.read_text(encoding="utf-8")))
        else:
            warn(f"{rel(f)} missing: the planner works without it")
    sections.append(("CORPUS SOURCES (id, kind, title)", "\n".join(cat)))
    header = (f"## Job\nTarget: {target}  —  {ayah_text(con, s, a)}\nSegments tied to {target} (read anyway by the "
              f"readers): {tied[0]} segments, {tied[1] or 0:,} characters, plus the classical lexica entries of the "
              f"ayah's bound roots.\nYour call directory: {d}\nOutput: {d / 'plan.json'}")
    write_call(d, (PROMPTS / "okuma_plan.md").read_text(encoding="utf-8"), header, sections, "okuma-plan",
               "plan.json", {"surah": s, "target": target, "stage": "okuma-plan", "model": "sonnet"})


def check_plan(d: Path) -> tuple[dict | None, list[str]]:
    probs: list[str] = []
    try:
        plan = json.loads((d / "plan.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return None, [f"plan.json unreadable: {e}"]
    claims, queries = plan.get("iddialar") or [], plan.get("sorgular") or []
    if not claims:
        probs.append("no claims (iddialar)")
    if len(queries) > MAX_QUERIES:
        probs.append(f"{len(queries)} queries; only the first {MAX_QUERIES} are run")
    for i, q in enumerate(queries):
        if not str(q.get("q", "")).strip():
            probs.append(f"query {i + 1} is empty")
    return plan, probs


# ---------------------------------------------------------------- the reading set

def norm_map(text: str) -> tuple[str, list[int]]:
    """C.norm character by character, with each normalised character's index in the original."""
    out, idx = [], []
    for i, ch in enumerate(text):
        n = C.norm(ch)
        for c in n:
            out.append(c)
            idx.append(i)
    return "".join(out), idx


def windows(text: str, words: list[str]) -> list[tuple[int, int]]:
    """Up to three windows of ±WINDOW characters around the matches of the query words, merged when they overlap."""
    nt, idx = norm_map(text)
    pos = sorted({idx[m.start()] for w in words if w for m in re.finditer(r"(?<!\w)" + re.escape(w), nt)})
    spans: list[list[int]] = []
    for p in pos:
        lo, hi = max(0, p - WINDOW), min(len(text), p + WINDOW)
        if spans and lo <= spans[-1][1]:
            spans[-1][1] = max(spans[-1][1], hi)
        elif len(spans) < 3:
            spans.append([lo, hi])
    return [(lo, hi) for lo, hi in spans] or [(0, min(len(text), 2 * WINDOW))]


def _search(con, q: dict, words: list[str], n: int) -> list[tuple]:
    fq = " ".join(f'"{w}"' + ("" if q.get("exact") else "*") for w in words)
    sql = ("SELECT seg.seg, seg.src, src.kind, seg.head, seg.text, seg.extra FROM f JOIN seg ON seg.id=f.rowid "
           "JOIN src ON src.id=seg.src WHERE f MATCH ?")
    args: list = [fq]
    if q.get("src"):
        ids = [x.strip() for x in str(q["src"]).split(",") if x.strip()]
        sql += f" AND seg.src IN ({','.join('?' * len(ids))})"
        args += ids
    if q.get("kind"):
        ks = [x.strip() for x in str(q["kind"]).split(",") if x.strip()]
        sql += f" AND src.kind IN ({','.join('?' * len(ks))})"
        args += ks
    if q.get("sahih"):
        sql += " AND json_extract(seg.extra,'$.sahih')=1"
    return con.execute(sql + " ORDER BY rank LIMIT ?", args + [n]).fetchall()


def _count(con, q: dict, word: str) -> int:
    return len(_search(con, q, [word], 100_000))


def search(con, q: dict) -> tuple[list[tuple], str]:
    """All the query's words first. When that finds nothing (a planner's phrase rarely matches a source's wording
    exactly), smaller sets of its words, the most specific first (the summed inverse frequency of the words within
    the query's own sources, whatever the set's size; a word they never hold is left out), down to two words (one
    word when every named source is a dictionary, whose entries are single words). The first set that matches is
    kept; the note says which words matched."""
    words = C.norm(str(q["q"])).split()
    n = max(1, min(int(q.get("n") or MAX_N), MAX_N))
    rows = _search(con, q, words, n)
    if rows or len(words) < 2:
        return rows, "all words"
    srcs = [x.strip() for x in str(q.get("src") or "").split(",") if x.strip()]
    kinds = {k for (k,) in con.execute(f"SELECT kind FROM src WHERE id IN ({','.join('?' * len(srcs))})", srcs)} if srcs else set()
    floor = 1 if (kinds == {"lexicon"} or (not srcs and q.get("kind") == "lexicon")) else 2
    import math
    from itertools import combinations
    df = {w: _count(con, q, w) for w in dict.fromkeys(words)}
    live = [w for w in df if df[w]]  # a word the sources never hold cannot help
    total = max(df.values()) * 4 + 1  # a stand-in for the size of the searched sources: only the order matters
    subsets = [c for m in range(floor, min(len(live), len(words) - 1) + 1) for c in combinations(live, m)]
    subsets.sort(key=lambda c: -sum(math.log(total / df[w]) for w in c))  # most specific first, whatever the size
    for sub in subsets[:64]:
        rows = _search(con, q, list(sub), n)
        if rows:
            absent = [w for w in df if not df[w]]
            return rows, (f"fallback: {len(sub)} of {len(words)} words ({' '.join(sub)})"
                          + (f"; never in these sources: {' '.join(absent)}" if absent else ""))
    return [], f"nothing, down to {floor} of {len(words)} words"


def seg_header(seg: str, head: str | None, extra: str | None, note: str = "") -> str:
    ex = json.loads(extra or "{}")
    flags = []
    if "sahih" in ex:
        flags.append(f"sahih={ex['sahih']} graded_by={'|'.join(ex.get('graded_by') or []) or '-'}")
    if ex.get("page"):
        flags.append(f"page={ex['page']}")
    return (f"== {seg}" + (f"  [{head}]" if head else "") + ("  " + " ".join(flags) if flags else "")
            + (f"  {note}" if note else ""))


def seg_extra_text(extra: str | None) -> str:
    ex = json.loads(extra or "{}")
    return "".join(f"\n  {k}: {C.flat(ex[k])}" for k in ("en", "tr", "notes") if ex.get(k))


def reading_set(s: int, target: str, plan: dict, notes: list) -> tuple[list[dict], dict]:
    con, pk = C.connect(), pack(s)
    a = int(target.split(":")[1])
    items: dict[str, dict] = {}
    skipped: dict[str, list[str]] = {}

    def add(seg, src, kind, head, text, extra, origin, shown=None):
        if seg in items:
            items[seg]["origin"].append(origin)
            return
        items[seg] = {"seg": seg, "src": src, "kind": kind, "head": head, "text": text, "extra": extra,
                      "origin": [origin], "shown": shown}

    for seg, src, kind, head, text, extra in con.execute(
            "SELECT seg.seg, seg.src, src.kind, seg.head, seg.text, seg.extra FROM seg JOIN src ON src.id=seg.src "
            "WHERE seg.s=? AND seg.a<=? AND coalesce(seg.a_end, seg.a)>=? ORDER BY src.kind, seg.src, seg.a, seg.id",
            (s, a, a)):
        if kind in SKIP_KINDS:
            skipped.setdefault(kind, []).append(seg)
            continue
        add(seg, src, kind, head, text, extra, "ayet")
    for kind, segs in skipped.items():
        print(f"NOTE: {len(segs)} {kind} segments tied to {target} are not given to readers: {SKIP_KINDS[kind]}")
    binding = json.loads((pk / "binding.json").read_text(encoding="utf-8"))
    roots = []
    for w in binding.get(target, []):
        for i in w.get("identity", []):
            if i["root"] not in roots:
                roots.append(i["root"])
    if not roots:
        warn(f"binding.json gives no identity root for {target}: no lexica by root", notes)
    for root in roots:
        key = root.replace(" ", "")
        for lex in LEXICA:
            rows = con.execute("SELECT seg.seg, seg.src, src.kind, seg.head, seg.text, seg.extra FROM seg JOIN src ON "
                               "src.id=seg.src WHERE seg.src=? AND (seg.seg=? OR seg.seg LIKE ?)",
                               (lex, f"{lex}:{key}", f"{lex}:{key}#%")).fetchall()
            for r in rows:
                add(*r, origin=f"kok:{root}")
    queries = []
    for i, q in enumerate((plan.get("sorgular") or [])[:MAX_QUERIES], 1):
        try:
            rows, how = search(con, q)
        except Exception as e:  # a malformed FTS query: recorded, the rest goes on
            warn(f"query {i} ({q.get('q')!r}) failed: {e}", notes)
            queries.append({**q, "i": i, "error": str(e), "hits": []})
            continue
        if how != "all words":
            print(f"NOTE: query {i} ({q.get('q')!r}): {how}")
        words = C.norm(str(q["q"])).split()
        hits = []
        for seg, src, kind, head, text, extra in rows:
            hits.append(seg)
            if kind in SKIP_KINDS:
                warn(f"query {i} hit {seg} ({kind}): not given to readers ({SKIP_KINDS[kind]})", notes)
                continue
            shown = None if len(text) <= HIT_WHOLE else windows(text, words)
            add(seg, src, kind, head, text, extra, f"sorgu:{i}", shown)
        queries.append({**q, "i": i, "hits": hits, "matched": how})
    return list(items.values()), {"skipped": skipped, "queries": queries, "roots": roots}


def blocks_of(it: dict) -> list[tuple[str, str, int]]:
    """(header, body, chars) per shown block of one item: the whole text, its parts, or its windows."""
    text, extra = it["text"] or "", it["extra"]
    tail = seg_extra_text(extra)
    if it.get("shown"):
        out = []
        for lo, hi in it["shown"]:
            note = (f"[search hit, WINDOW: characters {lo + 1}–{hi} of {len(text):,} around the query's match; "
                    f"the rest of this segment is not shown here]")
            out.append((seg_header(it["seg"], it["head"], extra, note), text[lo:hi], hi - lo))
        return out
    if len(text) <= PART_CHARS:
        return [(seg_header(it["seg"], it["head"], extra), text + tail, len(text) + len(tail))]
    n = -(-len(text) // PART_CHARS)
    out, start = [], 0
    for k in range(1, n + 1):
        end = len(text) if k == n else (text.rfind(" ", start, start + PART_CHARS) if " " in text[start:start + PART_CHARS] else start + PART_CHARS)
        end = end if end > start else start + PART_CHARS
        note = f"[part {k} of {n}: characters {start + 1}–{end} of {len(text):,}; the same segment continues]"
        out.append((seg_header(it["seg"], it["head"], extra, note), text[start:end] + (tail if k == n else ""),
                    end - start))
        start = end
    return out


def est_cost(material_chars: int, context_chars: int, files: int) -> tuple[float, int]:
    r = agentrun.RATES[READER_MODEL]
    mat_tok = material_chars / 1.45
    ctx_tok = context_chars / 2.1
    total = SYSTEM_TOKENS + ctx_tok + mat_tok
    reads = sum(SYSTEM_TOKENS + ctx_tok + mat_tok * k / max(1, files) for k in range(files + 2))
    out = mat_tok * CARD_SHARE + THINK_TOKENS
    usd = (total * r["cache_5m"] + reads * r["cache_read"] + out * r["output"]) / 1e6
    return usd, int(total)


def cmd_build(s: int, target: str, dry: bool) -> None:
    base = rdir(s, target)
    pd = base / "plan"
    if not (pd / "run.log.json").exists():
        sys.exit(f"the plan call is not finished ({rel(pd)}): spawn it, then `okuma.py finish`")
    plan, probs = check_plan(pd)
    if plan is None:
        sys.exit(f"plan unusable: {probs}")
    notes: list[str] = []
    for p in probs:
        warn(f"plan: {p}", notes)
    if list(base.glob("c*/started.json")):
        sys.exit(f"reader calls in {rel(base)} were started already; a call is never rerun")
    items, info = reading_set(s, target, plan, notes)
    con, pk = C.connect(), pack(s)
    a = int(target.split(":")[1])
    t = tag(target)
    claims = plan.get("iddialar") or []
    claim_text = "\n".join(f"I{i}. ¶{c.get('paragraf', '?')} ({c.get('tur', '?')}): {c.get('ozet', '')}"
                           for i, c in enumerate(claims, 1))
    words_md = (pk / "ayah" / t / "words.md").read_text(encoding="utf-8")
    context = [("THE PAGE: the target ayah, its words", words_md),
               ("THE BASE'S CLAIMS (numbered; cards name them as I1, I2 …)", claim_text)]
    context_chars = sum(len(b) for _, b in context)
    # chunks: items in order (kind, source), whole blocks never split across readers except a segment's parts
    chunks: list[list[tuple[str, str, int, str]]] = [[]]
    size = 0
    for it in items:
        for h, body, n in blocks_of(it):
            if size + n > CHUNK_CHARS and chunks[-1]:
                chunks.append([])
                size = 0
            chunks[-1].append((h, body, n, it["seg"]))
            size += n
    brief = (PROMPTS / "okuma.md").read_text(encoding="utf-8")
    manifest = {"surah": s, "target": target, "built": time.strftime("%Y-%m-%dT%H:%M:%S"), "chunks": [],
                "items": [{k: it[k] for k in ("seg", "src", "kind", "origin")} | {
                    "chars": len(it["text"] or ""), "shown": it["shown"]} for it in items],
                "skipped_kinds": info["skipped"], "queries": info["queries"], "roots": info["roots"], "notes": notes}
    total_usd, total_chars = 0.0, 0
    for k, ch in enumerate(chunks, 1):
        mat = sum(x[2] for x in ch)
        segs = list(dict.fromkeys(x[3] for x in ch))
        files = -(-(mat + context_chars) // FILE_CHARS)
        usd, tok = est_cost(mat, context_chars + len(brief), files)
        total_usd += usd
        total_chars += mat
        manifest["chunks"].append({"chunk": f"c{k:02d}", "segments": segs, "chars": mat, "est_usd": round(usd, 2),
                                   "est_tokens": tok})
        print(f"  c{k:02d}: {len(segs):>3} segments {mat:>8,} chars  ~{tok:>7,} tokens  ~${usd:.2f}")
        if dry:
            continue
        d = base / f"c{k:02d}"
        sections = context + [("MATERIAL", "\n\n".join(f"{h}\n{body}" for h, body, _, _ in ch))]
        header = (f"## Job\nTarget: {target}  —  {ayah_text(con, s, a)}\nYour call directory: {d}\nOutput: "
                  f"{d / 'cards.jsonl'}\nSegments in your material ({len(segs)}; every one must appear in your "
                  f"output, as cards or as one bos line): {', '.join(segs)}")
        write_call(d, brief, header, sections, "okuma", "cards.jsonl",
                   {"surah": s, "target": target, "stage": "okuma", "chunk": f"c{k:02d}", "model": "sonnet",
                    "segments": segs})
    windowed = sum(1 for it in items if it["shown"])
    print(f"{len(items)} segments ({total_chars:,} characters shown) in {len(chunks)} readers; {windowed} search hits "
          f"shown as windows; estimated ${total_usd:.2f} at {READER_MODEL} rates (an estimate until the pilot "
          f"calibrates it)")
    if not dry:
        (base / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n",
                                            encoding="utf-8")
        print(f"spawn {len(chunks)} agents: subagent_type general-purpose, model sonnet, prompt = the text of "
              f"{rel(base)}/cNN/spawn.md; then `okuma.py finish --surah {s} --target {target}`")


# ---------------------------------------------------------------- finish

_MARKUP = re.compile(r"[\{\}\[\]\(\)«»\"'،,.:;!?؟؛\-–—*^~|0-9٠-٩#¬]+")


def near_quote(q: str, full: str) -> tuple[str, float] | None:
    """The stretch of the source that a near-verbatim quote copies: the words compared after normalisation with
    punctuation, brackets and footnote marks removed; accepted at 85% word agreement over at least four words.
    Returns the source's own text for that stretch and the agreement."""
    import difflib
    def words_with_spans(text: str) -> list[tuple[str, int, int]]:
        nt, idx = norm_map(text)
        nt = _MARKUP.sub(lambda m: " " * len(m.group()), nt)
        return [(m.group(), idx[m.start()], idx[m.end() - 1] + 1) for m in re.finditer(r"\S+", nt)]
    qw = [w for w, _, _ in words_with_spans(q)]
    if len(qw) < 4:
        return None
    sw = words_with_spans(full)
    words = [w for w, _, _ in sw]
    best, at = 0.0, None
    first = set(qw[:3]) | set(qw[-3:])
    for i, w in enumerate(words):  # windows start near a word the quote holds at either end
        if w not in first:
            continue
        for n in (len(qw) - 2, len(qw) - 1, len(qw), len(qw) + 1, len(qw) + 2):
            if n < 1 or i + n > len(words):
                continue
            r = difflib.SequenceMatcher(None, qw, words[i:i + n], autojunk=False).ratio()
            if r > best:
                best, at = r, (i, i + n)
    if not at or best < 0.85:
        return None
    lo, hi = sw[at[0]][1], sw[at[1] - 1][2]
    return full[lo:hi], best


def check_cards(d: Path, s: int) -> tuple[list[dict], list[dict], list[str], list[str]]:
    """Cards that pass, cards rejected (with the reason), segments with neither a card nor a bos line, warnings."""
    con = C.connect()
    started = json.loads((d / "started.json").read_text(encoding="utf-8"))
    segs = set(started.get("segments") or [])
    good, bad, warns = [], [], []
    seen: set[str] = set()
    f = d / "cards.jsonl"
    lines = f.read_text(encoding="utf-8").splitlines() if f.exists() else []
    for n, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            c = json.loads(line)
        except json.JSONDecodeError as e:
            bad.append({"line": n, "raw": line[:300], "why": f"not JSON: {e}"})
            continue
        seg = str(c.get("seg", ""))
        if seg not in segs:
            bad.append({**c, "line": n, "why": f"seg {seg!r} is not in this reader's material"})
            continue
        seen.add(seg)
        if c.get("bos"):
            good.append({**c, "chunk": d.name})
            continue
        why = []
        if c.get("tur") not in CARD_TUR:
            why.append(f"tur {c.get('tur')!r} not in {sorted(CARD_TUR)}")
        if c.get("iliski") not in ILISKI:
            why.append(f"iliski {c.get('iliski')!r} not in {sorted(ILISKI)}")
        q = str(c.get("alinti", "")).strip()
        row = con.execute("SELECT text, extra FROM seg WHERE seg=?", (seg,)).fetchone()
        full = (row[0] or "") + seg_extra_text(row[1]) if row else ""
        if not q:
            why.append("no alinti")
        elif " ".join(q.split()) in " ".join(full.split()):
            c["alinti_kontrol"] = "tam"
        elif C.norm(q) in C.norm(full):
            c["alinti_kontrol"] = "norm"  # the same words; diacritics or letter forms differ
        else:
            near = near_quote(q, full)
            if near:  # a reader's small slip (a dropped particle, the editor's brackets, a footnote mark): the source's own words replace the quote
                span, ratio = near
                c.update(alinti_okuyucu=q, alinti=span, alinti_kontrol="yakin", alinti_oran=round(ratio, 3))
            else:
                why.append("alinti is not in the segment's text")
        if why:
            bad.append({**c, "line": n, "why": "; ".join(why)})
        else:
            good.append({**c, "chunk": d.name})
    missing = sorted(segs - seen)
    for r in bad:
        warns.append(f"{d.name} line {r.get('line')}: card dropped ({r['why']}): {str(r.get('seg', ''))}")
    for m in missing:
        warns.append(f"{d.name}: segment {m} has no card and no bos line (not read, or skipped)")
    return good, bad, missing, warns


def finish_call(d: Path, s: int, target: str, output: str) -> dict | None:
    if not (d / "started.json").exists():
        return None
    if (d / "run.log.json").exists():
        return json.loads((d / "run.log.json").read_text(encoding="utf-8"))
    if not (d / output).exists():
        print(f"NOTE: {rel(d)}: no {output} yet (not spawned, or still running)")
        return None
    obj = agentrun.finish(d, output)
    started = json.loads((d / "started.json").read_text(encoding="utf-8"))
    row = {"surah": s, "target": target, "stage": started.get("stage"), "chunk": started.get("chunk"),
           "model": "sonnet", "model_id": obj.get("model"), "runner": "agent", "started": started.get("started"),
           "prompt_sha256": started.get("prompt_sha256"), "material_chars": started.get("material_chars"),
           "usage": obj.get("usage"), "cost_usd": obj.get("total_cost_usd"), "cost_basis": obj.get("cost_basis"),
           "num_turns": obj.get("num_turns"), "commands": obj.get("tool_calls"), "transcript": obj.get("transcript"),
           "stop_reason": obj.get("stop_reason"), "dir": rel(d)}
    if obj.get("tool_use_outside_rule"):
        row["tool_use_outside_rule"] = obj["tool_use_outside_rule"]
    if obj.get("is_error"):
        row.update(status="error", check=obj.get("error"))
    elif started.get("stage") == "okuma":
        good, bad, missing, warns = check_cards(d, s)
        for w in warns:
            print(f"WARNING: {w}")
        row.update(status="ok", cards=sum(1 for c in good if not c.get("bos")), bos=sum(1 for c in good if c.get("bos")),
                   rejected=len(bad), missing=missing, check="ok" if not (bad or missing) else "ok with drops")
    else:
        plan, probs = check_plan(d)
        for p in probs:
            print(f"WARNING: plan: {p}")
        row.update(status="ok" if plan else "error", check="; ".join(probs) or "ok",
                   claims=len((plan or {}).get("iddialar") or []), queries=len((plan or {}).get("sorgular") or []))
    log(row)
    print(f"{rel(d)}: {row['status']} {row.get('check')}  cost ${row['cost_usd'] or 0:.2f}  turns {row['num_turns']}")
    return obj


def cmd_finish(s: int, target: str) -> None:
    base = rdir(s, target)
    if not base.exists():
        sys.exit(f"nothing built for {target}")
    finish_call(base / "plan", s, target, "plan.json")
    readers = sorted(base.glob("c[0-9][0-9]"))
    done = [d for d in readers if (d / "run.log.json").exists()]
    for d in readers:
        if d not in done and finish_call(d, s, target, "cards.jsonl"):
            done.append(d)
    if not readers:
        return
    if len(done) < len(readers):
        print(f"NOTE: {len(done)} of {len(readers)} readers finished; cards are merged when all are")
        return
    cards, rejected, missing, warns = [], [], {}, []
    for d in sorted(readers):
        g, b, m, w = check_cards(d, s)
        cards += g
        rejected += [{**x, "chunk": d.name} for x in b]
        if m:
            missing[d.name] = m
        warns += w
    k = 0
    for c in cards:
        if not c.get("bos"):
            k += 1
            c["kart"] = f"K{k:04d}"
    (base / "cards.jsonl").write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in cards), encoding="utf-8")
    (base / "rejected.jsonl").write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in rejected),
                                         encoding="utf-8")
    cov = {"cards": k, "bos": sum(1 for c in cards if c.get("bos")), "rejected": len(rejected), "missing": missing,
           "warnings": warns, "alinti_norm": sum(1 for c in cards if c.get("alinti_kontrol") == "norm")}
    (base / "coverage.json").write_text(json.dumps(cov, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    cost = sum((json.loads((d / "run.log.json").read_text(encoding="utf-8")).get("total_cost_usd") or 0)
               for d in [base / "plan", *readers] if (d / "run.log.json").exists())
    print(f"merged: {k} cards, {cov['bos']} empty segments, {len(rejected)} rejected, "
          f"{sum(map(len, missing.values()))} segments missing; stage cost ${cost:.2f} -> {rel(base / 'cards.jsonl')}")
    for w in warns:
        print(f"WARNING: {w}")


# ---------------------------------------------------------------- recall against an existing page

def cmd_recall(s: int, target: str, page: Path) -> None:
    base = rdir(s, target)
    cards = [json.loads(x) for x in (base / "cards.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    man = json.loads((base / "manifest.json").read_text(encoding="utf-8"))
    read = {it["seg"] for it in man["items"]}
    carded = {c["seg"] for c in cards if not c.get("bos")}
    empty = {c["seg"] for c in cards if c.get("bos")}
    recs = [json.loads(x) for x in (page / "annotations.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    con = C.connect()
    kind_of = dict(con.execute("SELECT id, kind FROM src").fetchall())
    rows, used = [], set()
    for r in recs:
        locs = [x.strip() for x in str(r.get("kaynak") or "").split("|") if x.strip() and x.strip() != "hafiza"]
        for loc in locs:
            used.add(loc)
            state = ("carded" if loc in carded else "read, marked empty" if loc in empty
                     else "read, no card" if loc in read
                     else "judge input (meal, translation, Qur'an text)" if kind_of.get(loc.split(":")[0]) in SKIP_KINDS
                     else "not in the reading set")
            rows.append((r["id"], r.get("tur"), loc, state))
    from collections import Counter
    by = Counter(x[3] for x in rows)
    print(f"{len(rows)} locators cited by {len(recs)} records of {rel(page)}:")
    for k2, v in by.most_common():
        print(f"  {v:>4}  {k2}")
    judge = "judge input (meal, translation, Qur'an text)"
    recs_full = sum(1 for r in recs if all(x[3] in ("carded", judge) for x in rows if x[0] == r["id"]))
    print(f"records whose every source is carded or is judge input: {recs_full} of {len(recs)}")
    print("not carded:")
    for x in rows:
        if x[3] not in ("carded", judge):
            print(f"  {x[0]:14} {x[1]:16} {x[2]:30} {x[3]}")
    new = sorted(carded - used)
    print(f"carded segments the page does not cite: {len(new)} (material the Opus agent did not use or did not open)")
    out = {"page": rel(page), "locators": len(rows), "states": dict(by), "records_fully_carded": recs_full,
           "records": len(recs), "rows": rows, "carded_not_cited": new}
    (base / "recall.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["plan", "build", "finish", "recall"])
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--target", required=True, help="S:A (ayah pages)")
    ap.add_argument("--dry", action="store_true", help="build: print the chunks and the estimate, write nothing")
    ap.add_argument("--page", type=Path, help="recall: an existing page's call directory")
    a = ap.parse_args()
    if ":" not in a.target:
        sys.exit("okuma is built for ayah pages (--target S:A)")
    if a.cmd == "plan":
        cmd_plan(a.surah, a.target)
    elif a.cmd == "build":
        cmd_build(a.surah, a.target, a.dry)
    elif a.cmd == "finish":
        cmd_finish(a.surah, a.target)
    else:
        if not a.page:
            sys.exit("recall needs --page <call dir>")
        cmd_recall(a.surah, a.target, a.page if a.page.is_absolute() else (PG / a.page if (PG / a.page).exists() else V2 / a.page))


if __name__ == "__main__":
    main()
