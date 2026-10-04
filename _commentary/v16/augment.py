#!/usr/bin/env python3
"""Augment step (user, 2026-10-01): a Sonnet 5.5 call adds missed Quran passages to a finished commentary, without
changing a word of it.

Production (user, 2026-10-04): augment8 with Opus 5.5 high (the defaults), on ayah readings only; a surah commentary
is refused unless --surah-commentary is given. See RUNBOOK.md.

  python3 -B _commentary/v16/augment.py out/s001/images.r12.map3.nohft.tool.tool [--go]   # a surah commentary
  python3 -B _commentary/v16/augment.py out/1_6/<run dir> [--go]                            # an ayah reading

Sonnet gets the brief (prompts/augment1/augment.md), the commentary with its prose paragraphs numbered, the writer's
ledger, and every passage of the inter-ayah lists (missing.py's tiers, all of them; for a surah commentary the lists
of all its ayat) that the commentary does not cite, each with its Arabic. It may also add passages from its own
knowledge, and writes a ledger line only for those. It returns insertions as data (paragraph, the exact words after
which the addition goes, ref, text); this script applies them and verifies that removing the inserted spans gives
back the original byte for byte. An insertion whose anchor is not found once in its paragraph, at a sentence end, is
not applied and is reported. Nothing is written into the run dir itself: everything goes to <run dir>/augment.<brief>/
(the merged commentary under the original file name, insertions.json, additions.md for reading, ledger.md,
check.json). One call, never rerun, gate $5, logged as arm "augment".
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import missing as M  # noqa: E402
import v16 as V  # noqa: E402

MODEL, EFFORT = "sonnet", "high"  # default model; --model opus for a comparison (user, 2026-10-03)
# briefs whose additions become paragraphs of their own after ¶n, with no anchor (user, 2026-10-03: augment3's
# mid-paragraph insertions broke the commentary's references and took over paragraph endings)
OWN_PARAGRAPH = {"augment4"}
# briefs that judge every listed passage against every paragraph, with no caps (user, 2026-10-03): prose additions
# and one reference line per paragraph, each a block of its own after its paragraph, headed by a marker comment so
# that a renderer can hide or show them. The marker is a namespaced HTML comment: it collides neither with v16's
# reader tags ({ar:…, source:…}) nor with enrichment v2's block lines ({id:…}) and its page header
# (<!-- schema:zenginlestirme …). Both v16's and enrichment's paragraph splitters count a marked block as one paragraph.
VERDICT = {"augment5", "augment6", "augment7", "augment8"}  # augment6: reference links name their mechanism; a refrain is one
# reference. augment7: conflict and context verdicts, the ledger answered, and the missing.py text lookup
LOOKUP = {"augment7", "augment8"}
# augment8 (user, 2026-10-03, from an Opus review of augment6/7): "already cited" is never a reason; a cited
# passage gets a "cited ¶n; …" verdict; a per-paragraph own-knowledge minimum; consecutive ayat as one reference;
# the ±2 neighbours of every passage the reading cites join the list as a tier of their own
NEIGHBOURS = {"augment8"}
CODEX = {"sol61": "gpt-6.1-sol"}  # --model sol61: GPT-6.1 Sol through `codex exec` (subscription, no USD)  # briefs whose call may read verse text (packets.ALLOW text …), as the r13 writer does
MARKED_BLOCK = re.compile(r"\n\n<!-- v16:augment [^\n]*-->\n[^\n]*")
OUT_TOKENS = {"images": 40_000, "ayah": 20_000}  # assumed, thinking included
PARA_SPLIT = re.compile(r"(\n[ \t]*\n)")
SENTENCE_END = re.compile(r"[.!?…][\"”’»)]*$")
VERDICT_OUT = 60_000  # a verdict line for every listed passage plus uncapped additions (87:8 Opus augment8: 55.2k)
MAX_IN = 400_000  # tokens; a larger prompt (a long surah's union of lists) needs splitting first


def target(d: Path) -> tuple[str, Path, list[str], str]:
    """(kind, commentary file, list ayat, check ref) for a run dir."""
    if (d / "images.md").exists():
        m = re.fullmatch(r"s(\d+)", d.parent.name)
        if not m:
            raise SystemExit(f"{d}: images.md outside out/s<NNN>/")
        s = int(m.group(1))
        q = M.verses()
        return "images", d / "images.md", [f"{s}:{a}" for a in range(1, 300) if f"{s}:{a}" in q], f"{s}:1"
    m = re.fullmatch(r"(\d+)_(\d+)", d.parent.name)
    f = d / f"{d.parent.name}.reading.tr.md"
    if not m or not f.exists():
        raise SystemExit(f"{d}: neither images.md nor {d.parent.name}.reading.tr.md")
    ref = f"{m.group(1)}:{m.group(2)}"
    return "ayah", f, [ref], ref


def paragraphs(text: str) -> list[tuple[int, int, int | None]]:
    """(start, end, number) for every block between blank lines; prose paragraphs are numbered from 1, headings and
    Kaynaklar lines get None."""
    out, pos, n = [], 0, 0
    for piece in PARA_SPLIT.split(text):
        if PARA_SPLIT.fullmatch(piece) or not piece.strip():
            pos += len(piece)
            continue
        body = piece.strip()
        num = None
        if not body.startswith("#") and not body.startswith("Kaynaklar:"):
            n += 1
            num = n
        out.append((pos, pos + len(piece), num))
        pos += len(piece)
    return out


def cited_by_paragraph(text: str) -> dict[int, set[str]]:
    """Prose paragraph number -> the Quran refs it cites."""
    return {num: M.expand([text[st:en]]) for st, en, num in paragraphs(text) if num}


def passages(prose: str, ayat: list[str], cites: dict[int, set[str]] | None = None,
             neighbours: bool = False) -> tuple[str, int, list[str]]:
    """The listed passages, best tier first, each with the ayat whose lists hold it. Without `cites`, those the prose
    cites anywhere are left out; with it (VERDICT briefs) every passage is kept and marked with the paragraphs that
    already cite it."""
    used = M.expand([prose]) if cites is None else set()
    rank = {t[4]: i for i, t in enumerate(M.TIERS)}
    best: dict[str, str] = {}
    where: dict[str, list[str]] = {}
    for a in ayat:
        groups, _ = M.listed([a], tuple(t[0] for t in M.TIERS))
        for label, rs in groups:
            for r in rs:
                if r in used:
                    continue
                where.setdefault(r, []).append(a)
                if r not in best or rank[label] < rank[best[r]]:
                    best[r] = label
    q = M.verses()
    key = lambda r: tuple(map(int, r.split(":")))
    blocks = []
    for t in M.TIERS:
        rs = sorted((r for r, b in best.items() if b == t[4]), key=key)
        if rs:
            blocks.append(f"## {t[4]} ({len(rs)})\n\n" + "\n".join(
                f"- ({r}) [listed for {', '.join(where[r])}]{cited_in(r, cites)} {q.get(r, '')}" for r in rs))
    order = [r for t in M.TIERS for r in sorted((r for r, b in best.items() if b == t[4]), key=key)]
    if neighbours:  # within two ayat of every passage outside the focus surah that the commentary cites
        fs = {a.split(":")[0] for a in ayat}
        near: dict[str, str] = {}
        for c in sorted(M.expand([prose]), key=key):
            cs, ca = c.split(":")
            if cs in fs:
                continue
            for k in (-2, -1, 1, 2):
                r = f"{cs}:{int(ca) + k}"
                if r in q and r not in best and r not in near and r not in M.expand([prose]):
                    near[r] = c
        if near:
            rs = sorted(near, key=key)
            blocks.append(f"## neighbours: within two ayat of a passage the commentary cites ({len(rs)})\n\n"
                          + "\n".join(f"- ({r}) [next to {near[r]}]{cited_in(r, cites)} {q.get(r, '')}" for r in rs))
            order += rs
    return "\n\n".join(blocks) + "\n", len(order), order


def cited_in(ref: str, cites: dict[int, set[str]] | None) -> str:
    ps = [n for n, rs in sorted(cites.items()) if ref in rs] if cites else []
    return f" [cited in {', '.join(f'¶{n}' for n in ps)}]" if ps else ""


def build(d: Path, brief: str) -> tuple[str, dict]:
    kind, f, ayat, _ = target(d)
    text = f.read_text(encoding="utf-8")
    led = d / "ledger.md"
    numbered = []
    for st, en, num in paragraphs(text):
        numbered.append((f"[¶{num}] " if num else "") + text[st:en].strip())
    pas, n, order = passages(text, ayat, cited_by_paragraph(text) if brief in VERDICT else None, brief in NEIGHBOURS)
    bf = V.HERE / "prompts" / brief / "augment.md"
    head = (f"Follow the brief below (augment.md) exactly. The commentary is "
            + ("a surah commentary on the images of the whole surah" if kind == "images" else
               f"a reading of the ayah {ayat[0]}")
            + "; its ledger and the listed passages follow it. Return only the output augment.md specifies.\n\n")
    if brief in LOOKUP:
        import packets as P
        head += P.tool_line(ayat[0], "lookup")
    secs = [(V.rel(bf), bf.read_text(encoding="utf-8")),
            (f"{V.rel(f)} (prose paragraphs numbered)", "\n\n".join(numbered)),
            (V.rel(led), led.read_text(encoding="utf-8") if led.exists() else "(no ledger)\n"),
            (f"passages not cited ({n})", pas)]
    full = head + "".join(f"===== {p} =====\n{b.rstrip()}\n\n" for p, b in secs)
    return full, {"kind": kind, "file": V.rel(f), "ayat": ayat, "passages": n, "listed": order}


def parse(result: str) -> tuple[list[dict], str]:
    result = re.sub(r"(?m)^[ \t]*```[^\n]*$", "", result)  # code fences around the output, if any
    body, _, led = result.partition(V.LEDGER_MARK)
    ins = []
    for blk in re.split(r"(?m)^=== INSERT ===[ \t]*$", body)[1:]:
        rec = {}
        m = re.search(r"(?ms)^text:[ \t]*(.*)\Z", blk)
        rec["text"] = re.sub(r"\s*\n\s*", " ", m.group(1)).strip() if m else ""
        head = blk[:m.start()] if m else blk
        for k in ("paragraph", "after", "ref"):  # "after" is absent for an OWN_PARAGRAPH brief
            mm = re.search(rf"(?m)^{k}:[ \t]*(.*)$", head)
            rec[k] = mm.group(1).strip() if mm else ""
        ins.append(rec)
    return ins, led.strip()


def apply(text: str, ins: list[dict]) -> tuple[str, list[dict]]:
    """Apply insertions at their anchors; return the merged text and each insertion's status. The merged text minus
    the inserted spans must equal the original exactly (asserted)."""
    paras = {num: (st, en) for st, en, num in paragraphs(text) if num}
    points = []  # (offset in original, order, inserted string)
    for i, r in enumerate(ins):
        r["status"] = "applied"
        m = re.search(r"\d+", r["paragraph"])
        n = int(m.group(0)) if m else -1
        if n not in paras:
            r["status"] = "no such paragraph"
        elif not r["text"] or len(r["after"].split()) < 3:
            r["status"] = "empty text or anchor"
        else:
            st, en = paras[n]
            p = text[st:en]
            k = p.count(r["after"])
            if k != 1:
                r["status"] = "anchor not found" if k == 0 else "anchor not unique"
            else:
                at = p.index(r["after"]) + len(r["after"])
                if p[:at].rfind("{") > p[:at].rfind("}"):
                    r["status"] = "anchor inside a tag"
                elif at < len(p) and not p[at].isspace():
                    r["status"] = "anchor not at a sentence end"
                elif not SENTENCE_END.search(r["after"]):
                    r["status"] = "anchor not at a sentence end"
                else:
                    points.append((st + at, i, " " + r["text"]))
    points.sort()
    out, spans, last, shift = [], [], 0, 0
    for off, i, s in points:
        out.append(text[last:off])
        spans.append((off + shift, off + shift + len(s)))
        out.append(s)
        shift += len(s)
        last = off
    out.append(text[last:])
    merged = "".join(out)
    back, prev = [], 0
    for a, b in spans:
        back.append(merged[prev:a])
        prev = b
    back.append(merged[prev:])
    assert "".join(back) == text, "removing the inserted spans does not give back the original"
    return merged, ins


def apply_own(text: str, ins: list[dict]) -> tuple[str, list[dict]]:
    """OWN_PARAGRAPH briefs: each addition becomes a paragraph of its own directly after its paragraph ¶n; the
    commentary's paragraphs are not touched. Refused (and reported): no such paragraph, the last prose paragraph, a
    second addition for one paragraph, empty text. The merged text minus the added blocks equals the original."""
    paras = {num: en for st, en, num in paragraphs(text) if num}
    last = max(paras) if paras else None
    used, points = set(), []
    for i, r in enumerate(ins):
        r["status"] = "applied"
        m = re.fullmatch(r"\s*¶?\s*(\d+)\s*", r["paragraph"])
        n = int(m.group(1)) if m else -1
        if n not in paras:
            r["status"] = "no such paragraph"
        elif n == last:
            r["status"] = "last paragraph"
        elif n in used:
            r["status"] = "second addition for this paragraph"
        elif not r["text"]:
            r["status"] = "empty text"
        else:
            used.add(n)
            points.append((paras[n], "\n\n" + r["text"]))
    points.sort()
    out, spans, prev, shift = [], [], 0, 0
    for off, s in points:
        out.append(text[prev:off])
        spans.append((off + shift, off + shift + len(s)))
        out.append(s)
        shift += len(s)
        prev = off
    out.append(text[prev:])
    merged = "".join(out)
    back, prev = [], 0
    for a, b in spans:
        back.append(merged[prev:a])
        prev = b
    back.append(merged[prev:])
    assert "".join(back) == text, "removing the added paragraphs does not give back the original"
    return merged, ins


def insert_issues(merged: str, ins: list[dict], check: Path) -> list[str]:
    """What check.py found inside the applied additions: unverified sources, untagged Arabic, unsourced quotes,
    process words (user, 2026-10-03: never silent)."""
    lines = {merged.count("\n", 0, merged.index(r["text"])) + 1 for r in ins if r["status"] == "applied"}
    if not check.exists():
        return []
    c = json.loads(check.read_text(encoding="utf-8"))
    out = [f"line {x['line']}: source {x.get('declared')} {x['status']}" for x in c.get("sources", [])
           if x.get("line") in lines and not str(x.get("status", "")).startswith("ok")]
    out += [f"line {x['line']}: Arabic outside a tag «{x['text']}»" for x in c.get("arabic_outside_tags", [])
            if x.get("line") in lines]
    out += [f"line {x['line']}: unsourced quote «{x['quote'][:40]}»" for x in c.get("unsourced_unmarked", [])
            if x.get("line") in lines]
    out += [f"line {x['line']}: process word «{x['word']}»" for x in c.get("process_lines", []) if x.get("line") in lines]
    return out


def parse_verdict(result: str) -> tuple[list[dict], dict[str, list[dict]], str]:
    """VERDICT briefs: (=== ADD === and === REFS === blocks in order, verdict lines by ref, the verdicts text)."""
    result = re.sub(r"(?m)^[ \t]*```[^\n]*$", "", result)
    body, _, ver = result.partition("=== VERDICTS ===")
    parts = re.split(r"(?m)^=== (ADD|REFS) ===[ \t]*$", body)
    items = []
    for kind, blk in zip(parts[1::2], parts[2::2]):
        rec = {"kind": "prose" if kind == "ADD" else "refs"}
        m = re.search(r"(?ms)^text:[ \t]*(.*)\Z", blk)
        rec["text"] = re.sub(r"\s*\n\s*", " ", m.group(1)).strip() if m else ""
        head = blk[:m.start()] if m else blk
        for k in ("paragraph", "ref"):
            mm = re.search(rf"(?m)^{k}:[ \t]*(.*)$", head)
            rec[k] = mm.group(1).strip() if mm else ""
        items.append(rec)
    verdicts: dict[str, list[dict]] = {}
    for line in ver.splitlines():
        m = re.match(r"\s*-\s*(\d+:\d+)(\s+own)?\s*:\s*(.*)$", line)
        if m:
            verdicts.setdefault(m.group(1), []).append({"own": bool(m.group(2)), "verdict": m.group(3).strip()})
    return items, verdicts, ver.strip()


def apply_marked(text: str, items: list[dict], brief: str, model: str) -> tuple[str, list[dict]]:
    """VERDICT briefs: each prose addition becomes a marked block after its paragraph, then the paragraph's one
    reference line. Refused (and reported): no such paragraph, empty text, a prose addition without a ref or for a
    passage its paragraph already cites, a second prose addition of one passage for one paragraph, a second reference
    line for one paragraph. A reference line naming a passage its paragraph already cites is kept and reported. The
    merged text minus the marked blocks equals the original (asserted)."""
    pinfo = {num: en for st, en, num in paragraphs(text) if num}
    cites = cited_by_paragraph(text)
    prose_seen, refs_seen, points = set(), set(), []
    for i, r in enumerate(items):
        r["status"] = "applied"
        m = re.fullmatch(r"\s*¶?\s*(\d+)\s*", r.get("paragraph", ""))
        n = int(m.group(1)) if m else -1
        if n not in pinfo:
            r["status"] = "no such paragraph"
        elif not r["text"] or "\n" in r["text"]:
            r["status"] = "empty text"
        elif r["kind"] == "prose":
            if not re.fullmatch(r"\d+:\d+", r.get("ref", "")):
                r["status"] = "prose addition without a ref"
            elif r["ref"] in cites[n]:
                r["status"] = "already cited in this paragraph"
            elif (n, r["ref"]) in prose_seen:
                r["status"] = "second prose addition of this passage here"
            else:
                prose_seen.add((n, r["ref"]))
        elif n in refs_seen:
            r["status"] = "second reference line for this paragraph"
        else:
            refs_seen.add(n)
            r["already_cited"] = sorted(M.expand([r["text"]]) & cites[n])
        if r["status"] == "applied":
            mark = (f"<!-- v16:augment brief={brief} model={model} para={n} kind={r['kind']}"
                    + (f" ref={r['ref']}" if r["kind"] == "prose" else "") + " -->")
            points.append((pinfo[n], 0 if r["kind"] == "prose" else 1, i, f"\n\n{mark}\n{r['text']}"))
    points.sort()
    out, prev = [], 0
    for off, _, _, s in points:
        out.append(text[prev:off])
        out.append(s)
        prev = off
    out.append(text[prev:])
    merged = "".join(out)
    assert strip_augment(merged) == text, "removing the marked blocks does not give back the original"
    return merged, items


def strip_augment(text: str) -> str:
    """The commentary without its marked augment blocks (hide)."""
    return MARKED_BLOCK.sub("", text)


ALREADY = re.compile(r"zaten|already|cited|anılıyor|anılmış|geçiyor|geçmiş", re.I)


def verdict_report(listed: list[str], verdicts: dict[str, list[dict]], items: list[dict],
                   cited_any: set[str] | None = None, looked: set[str] | None = None,
                   focus_surah: str = "") -> dict:
    """Completeness and consistency of the verdicts (never silent): listed passages without a verdict, prose or
    reference verdicts with no matching applied addition, applied additions with no verdict."""
    applied = [r for r in items if r["status"] == "applied"]
    prose = set()  # (ref, paragraph): an addition's own ref and every passage its text cites (context ayat)
    for r in applied:
        if r["kind"] == "prose":
            n = int(re.search(r"\d+", r["paragraph"]).group(0))
            prose |= {(x, n) for x in M.expand([r["ref"], r["text"]])}
    refs = {}
    for r in applied:
        if r["kind"] == "refs":
            refs[int(re.search(r"\d+", r["paragraph"]).group(0))] = M.expand([r["text"]])
    missing = [r for r in listed if r not in verdicts]
    mismatch, conflicts = [], []
    for ref, vs in verdicts.items():
        for v in vs:
            s = v["verdict"].split(" - ")[0]
            if s.strip().startswith("conflict"):
                conflicts.append(f"{ref}: {v['verdict']}")
                continue
            s = re.sub(r"\(in [^)]*\)", "", s)  # "context ¶10 (in 79:45)": the paragraph is what is checked
            for kind, nums in re.findall(r"(prose|ref|context)\s*((?:¶\s*\d+[,\s]*)+)", s):
                for n in map(int, re.findall(r"\d+", nums)):
                    if ((kind in ("prose", "context") and (ref, n) not in prose)
                            or (kind == "ref" and ref not in refs.get(n, set()))):
                        mismatch.append(f"{ref}: {kind} ¶{n} in the verdict, no such addition applied")
    unjudged = sorted(({r for r, _ in prose} | {x for s in refs.values() for x in s}) - set(verdicts))
    def kind(v: str) -> str:
        v = v.strip()
        if v.startswith("cited") and "nowhere else" in v.split(" - ")[0]:
            return "cited_only"
        return "not" if v.startswith("not relevant") else "conflict" if v.startswith("conflict") else "relevant"
    # "already cited" given as the reason a passage the commentary cites is not relevant (never a reason)
    already = sorted(r for r, vs in verdicts.items() if cited_any and r in cited_any
                     and all(kind(v["verdict"]) == "not" for v in vs)
                     and any(ALREADY.search(v["verdict"].split(" - ", 1)[-1]) for v in vs))
    looked_no = sorted(r for r in (looked or set()) - set(verdicts) - (cited_any or set())
                       if r.split(":")[0] != focus_surah)
    split = []  # consecutive ayat given as separate items of one reference line
    for r in items:
        if r["status"] == "applied" and r["kind"] == "refs":
            parts = [sorted(M.expand(re.findall(r"source:\s*(\d+:\d+)", x))) for x in r["text"].split(";")]
            for i, a in enumerate(parts):
                for b in parts[i + 1:]:
                    for x in a:
                        for y in b:
                            xs, xa = x.split(":"); ys, ya = y.split(":")
                            if xs == ys and abs(int(xa) - int(ya)) == 1:
                                split.append(f"¶{r['paragraph']}: {x} and {y}")
    return {"missing": missing, "mismatch": mismatch, "unjudged": unjudged, "conflicts": conflicts,
            "already_cited_rejects": already, "looked_up_no_verdict": looked_no, "consecutive_split": split,
            "cited_only": sum(1 for vs in verdicts.values() if any(kind(v["verdict"]) == "cited_only" for v in vs)),
            "relevant": sum(1 for vs in verdicts.values() if any(kind(v["verdict"]) == "relevant" for v in vs)),
            "not_relevant": sum(1 for vs in verdicts.values() if all(kind(v["verdict"]) == "not" for v in vs))}


CODEX_NOTE = ("Work only from this message and the lookup command it describes: read no file and run no other "
              "command.\n\n")
WRAPPED = re.compile(r"""^\S*(?:ba|z)?sh -l?c (['"])(.*)\1$""", re.S)


def call_codex(text: str, d: Path, model: str, effort: str) -> dict:
    """One GPT call through `codex exec` (subscription: tokens, no USD), in an empty temporary directory, read-only
    sandbox, no web search, no user config, ephemeral (no session file). The stream is kept; commands go to
    tool_calls.json in call_opus's form ({input: {command}}, unwrapped from the shell) so packets.audit reads them."""
    (d / "started.json").write_text(json.dumps({"started": time.strftime("%Y-%m-%dT%H:%M:%S"),
                                                 "prompt_sha256": hashlib.sha256(text.encode()).hexdigest(),
                                                 "model": model, "effort": effort, "runner": "codex"}) + "\n",
                                    encoding="utf-8")
    cmd = ["codex", "exec", "--ignore-user-config", "-m", model, "-c", f'model_reasoning_effort="{effort}"',
           "-c", 'web_search="disabled"', "--disable", "skill_search", "--skip-git-repo-check", "--ephemeral",
           "-s", "read-only", "--json"]
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    with tempfile.TemporaryDirectory(prefix="v16_augment_codex_") as cwd:
        last = Path(cwd) / "last.txt"
        try:
            p = subprocess.run(cmd + ["-o", str(last), "-C", cwd, "-"], input=text, capture_output=True, text=True,
                               env=env, timeout=5400)
        except subprocess.TimeoutExpired as x:
            p = subprocess.CompletedProcess(cmd, -9, x.stdout or "", x.stderr or "")
        result = last.read_text(encoding="utf-8") if last.exists() else ""
    stdout = p.stdout if isinstance(p.stdout, str) else (p.stdout or b"").decode("utf-8", "replace")
    (d / "run.stream.jsonl").write_text(stdout, encoding="utf-8")
    usage, completed, calls = {}, False, []
    for line in stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        it = ev.get("item") or {}
        if ev.get("type") == "turn.completed":
            completed, usage = True, ev.get("usage") or {}
        if ev.get("type") == "item.completed" and it.get("type") == "command_execution":
            c = it.get("command", "")
            m = WRAPPED.match(c)
            calls.append({"id": it.get("id"), "input": {"command": m.group(2) if m else c, "raw": c},
                          "result": (it.get("aggregated_output") or "")[:20000],
                          "is_error": (it.get("exit_code") or 0) != 0})
    if calls:
        (d / "tool_calls.json").write_text(json.dumps(calls, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    obj = {"result": result, "returncode": p.returncode, "turn_completed": completed, "usage": usage,
           "tool_calls": len(calls), "stderr": (p.stderr or "")[-3000:] if isinstance(p.stderr, str) else "",
           "prompt_chars": len(text), "prompt_sha256": hashlib.sha256(text.encode()).hexdigest(), "cli": "codex"}
    (d / "run.log.json").write_text(json.dumps(obj, ensure_ascii=False) + "\n", encoding="utf-8")
    return obj


def looked_up(out: Path) -> set[str]:
    """Refs the call read with `missing.py text`."""
    f = out / "tool_calls.json"
    refs = set()
    for c in (json.loads(f.read_text(encoding="utf-8")) if f.exists() else []):
        cmd = str((c.get("input") or {}).get("command", ""))
        if " text " in cmd:
            refs |= M.expand([cmd.split(" text ", 1)[1]])
    return refs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("run", type=Path)
    ap.add_argument("--brief", default="augment8")  # production (user, 2026-10-04): augment8, Opus 5.5 high, ayah readings only
    ap.add_argument("--model", choices=("sonnet", "opus", *CODEX), default="opus")
    ap.add_argument("--surah-commentary", action="store_true", help="allow a surah commentary (not production)")
    ap.add_argument("--go", action="store_true")
    a = ap.parse_args()
    model = a.model
    d = a.run if a.run.is_absolute() else V.HERE / a.run
    text, meta = build(d, a.brief)
    if model in CODEX:
        text = CODEX_NOTE + text
    model_id, w, o = (CODEX[model], 0.0, 0.0) if model in CODEX else V.MODELS[model]
    n_in = V.est_tokens(text)
    est = n_in * w + (VERDICT_OUT if a.brief in VERDICT else OUT_TOKENS[meta["kind"]]) * o
    out = d / (f"augment.{a.brief}" + ("" if model == MODEL else f".{model}"))
    print(f"{out.relative_to(V.HERE)}: {meta['passages']} passages, ~{n_in:,} tokens in; "
          + (f"subscription, no USD ({model_id}" if model in CODEX else f"est ${est:.2f} ({model_id}")
          + f", effort {EFFORT})")
    if n_in > MAX_IN:
        raise SystemExit(f"prompt ~{n_in:,} tokens is over {MAX_IN:,}: split the passages before augmenting")
    if not a.go:
        return
    if meta["kind"] == "images" and not a.surah_commentary:  # user, 2026-10-04: augment runs on ayah readings only
        raise SystemExit(f"{d}: a surah commentary; production augment runs on ayah readings only "
                         "(--surah-commentary to override, with the user's go)")
    ref = "S" + str(int(d.parent.name[1:])) if meta["kind"] == "images" else meta["ayat"][0]
    row = {"ref": ref, "arm": "augment", "brief": f"{out.name.removeprefix('augment.')}.{d.name}"}
    if V.blocked(out):
        raise SystemExit(f"{out}: started or finished before (never rerun)")
    if est >= V.GATE_USD:
        V.log({**row, "status": "gated", "estimate_usd": round(est, 2)})
        raise SystemExit(f"gated at ${est:.2f}")
    out.mkdir(parents=True, exist_ok=True)
    (out / "prompt.md").write_text(text, encoding="utf-8")
    (out / "packet.json").write_text(json.dumps({**{k: v for k, v in meta.items() if k != "listed"}, "brief": a.brief, "model": model_id},
                                                ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    t0 = time.time()
    if model in CODEX:
        obj = call_codex(text, out, model_id, EFFORT)
        u = obj.get("usage") or {}
        res = {**row, "model": model_id, "effort": EFFORT, "runner": "codex", "seconds": round(time.time() - t0),
               "status": "ok" if obj["returncode"] == 0 and obj["turn_completed"] and obj["result"].strip() else "error",
               "cost_usd": 0.0, "input_tokens": u.get("input_tokens"), "cached_input_tokens": u.get("cached_input_tokens"),
               "output_tokens": u.get("output_tokens"), "reasoning_tokens": u.get("reasoning_output_tokens"),
               "tool_calls": obj["tool_calls"], "words": len(obj["result"].split()), "prompt_chars": len(text),
               "prompt_sha256": obj["prompt_sha256"], "cli": "codex"}
    else:
        if a.brief in LOOKUP:
            import packets as P
            obj = V.call_opus(text, out, model, allow=P.ALLOW, effort=EFFORT)
        else:
            obj = V.call_opus(text, out, model, allow=None, effort=EFFORT)
        res = {**row, "model": model_id, "effort": EFFORT, "seconds": round(time.time() - t0),
               "estimate_usd": round(est, 2), **V.usage_row(obj, text)}
    result = (obj.get("result") or "").strip()
    if a.brief in LOOKUP:  # every command must be a text lookup; anything else is reported, never silent
        import packets as P
        bad, denied = P.audit(out, [])
        res["audit"] = "ok" if not bad else f"{len(bad)} outside the rule"
        res["denied"] = len(denied)
        for c in bad:
            print(f"WARNING: ran outside the rule: {c[:200]}")
        for c in denied:
            print(f"NOTE: refused (never ran): {c[:200]}")
    V.log(res)  # the paid call is recorded before any post-processing can fail
    if result and res["status"] == "ok":
        (out / "augment.raw.md").write_text(result + "\n", encoding="utf-8")
        src = V.HERE / meta["file"].replace("_commentary/v16/", "", 1)
        original = src.read_text(encoding="utf-8")
        if a.brief in VERDICT:
            ins, verdicts, led = parse_verdict(result)
            merged, ins = apply_marked(original, ins, a.brief, model)
            vr = verdict_report(meta["listed"], verdicts, ins, M.expand([original]), looked_up(out),
                                meta["ayat"][0].split(":")[0])
        else:
            ins, led = parse(result)
            merged, ins = (apply_own if a.brief in OWN_PARAGRAPH else apply)(original, ins)
            vr = None
        (out / src.name).write_text(merged, encoding="utf-8")
        (out / "insertions.json").write_text(json.dumps(ins, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        (out / "additions.md").write_text("".join(
            f"## ¶{r['paragraph']} · {r.get('kind', 'insert')} · {r.get('ref') or '-'} · {r['status']}\n\n"
            + (f"… {r['after']}\n\n" if r.get("after") else "")
            + f"**+** {r['text']}\n\n"
            for r in ins), encoding="utf-8")
        (out / ("verdicts.md" if vr else "ledger.md")).write_text((led or "(no ledger lines)") + "\n", encoding="utf-8")
        _, _, _, cref = target(d)
        res["check"] = V.run_check(out / src.name, cref, out / "check.json")
        res["insertions"] = len(ins)
        res["applied"] = sum(1 for r in ins if r["status"] == "applied")
        res["ledger_lines"] = sum(1 for ln in led.splitlines() if ln.strip().startswith("-"))
        for r in ins:  # never silent: every refused addition is printed
            if r["status"] != "applied":
                print(f"WARNING: not applied (¶{r['paragraph']}, {r['ref']}): {r['status']}")
        issues = insert_issues(merged, ins, out / "check.json")
        for x in issues:
            print(f"WARNING: in an addition, {x}")
        extra = {}
        if vr:
            for r in ins:
                if r.get("already_cited"):
                    print(f"WARNING: reference line of ¶{r['paragraph']} names what the paragraph already cites: "
                          f"{', '.join(r['already_cited'])}")
            if vr["missing"]:
                print(f"WARNING: {len(vr['missing'])} of {len(meta['listed'])} listed passages have no verdict: "
                      f"{', '.join(vr['missing'][:20])}{' …' if len(vr['missing']) > 20 else ''}")
            for x in vr["mismatch"]:
                print(f"WARNING: {x}")
            for x in vr["conflicts"]:
                print(f"WARNING: conflict with the commentary: {x}")
            if vr["unjudged"]:
                print(f"WARNING: added without a verdict line: {', '.join(vr['unjudged'])}")
            if vr["already_cited_rejects"]:
                print(f"WARNING: 'not relevant' because already cited: {', '.join(vr['already_cited_rejects'])}")
            if vr["looked_up_no_verdict"]:
                print(f"WARNING: looked up, no verdict: {', '.join(vr['looked_up_no_verdict'])}")
            for x in vr["consecutive_split"]:
                print(f"WARNING: consecutive ayat as separate references: {x}")
            (out / "verdict_report.json").write_text(json.dumps(vr, ensure_ascii=False, indent=1) + "\n",
                                                     encoding="utf-8")
            app = [r for r in ins if r["status"] == "applied"]
            extra = {"prose_added": sum(r["kind"] == "prose" for r in app),
                     "ref_lines": sum(r["kind"] == "refs" for r in app),
                     "refs_named": sum(len(re.findall(r"source:", r["text"])) for r in app if r["kind"] == "refs"),
                     "listed": len(meta["listed"]), "verdicts_missing": len(vr["missing"]),
                     "verdict_mismatch": len(vr["mismatch"]), "conflicts": len(vr["conflicts"]),
                     "already_cited_rejects": len(vr["already_cited_rejects"]),
                     "looked_up_no_verdict": len(vr["looked_up_no_verdict"]),
                     "consecutive_split": len(vr["consecutive_split"]), "cited_only": vr["cited_only"],
                     "relevant": vr["relevant"],
                     "not_relevant": vr["not_relevant"]}
        V.log({"ref": res["ref"], "arm": "augment-applied", "brief": res["brief"], "insertions": res["insertions"],
               "applied": res["applied"], "not_applied": res["insertions"] - res["applied"],
               "insert_issues": len(issues), "ledger_lines": res["ledger_lines"], **extra, "check": res["check"]})
    if model in CODEX:
        print(f"tokens: in {res.get('input_tokens')} (cached {res.get('cached_input_tokens')}), out "
              f"{res.get('output_tokens')} (reasoning {res.get('reasoning_tokens')}), commands {res.get('tool_calls')}")
    print(f"{out.relative_to(V.HERE)}: {res['status']} ${res.get('cost_usd')} "
          f"{res.get('applied')}/{res.get('insertions')} applied {res['seconds']}s")
    if res["status"] != "ok":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
