#!/usr/bin/env python3
"""Augment step (user, 2026-10-01): a Sonnet 5.5 call adds missed Quran passages to a finished commentary, without
changing a word of it.

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
import json
import re
import subprocess
import sys
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
VERDICT = {"augment5", "augment6"}  # augment6: reference links name their mechanism; a refrain is one reference
MARKED_BLOCK = re.compile(r"\n\n<!-- v16:augment [^\n]*-->\n[^\n]*")
OUT_TOKENS = {"images": 40_000, "ayah": 20_000}  # assumed, thinking included
PARA_SPLIT = re.compile(r"(\n[ \t]*\n)")
SENTENCE_END = re.compile(r"[.!?…][\"”’»)]*$")
VERDICT_OUT = 35_000  # assumed: a verdict line for every listed passage plus uncapped additions
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


def passages(prose: str, ayat: list[str], cites: dict[int, set[str]] | None = None) -> tuple[str, int, list[str]]:
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
    return "\n\n".join(blocks) + "\n", len(best), order


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
    pas, n, order = passages(text, ayat, cited_by_paragraph(text) if brief in VERDICT else None)
    bf = V.HERE / "prompts" / brief / "augment.md"
    head = (f"Follow the brief below (augment.md) exactly. The commentary is "
            + ("a surah commentary on the images of the whole surah" if kind == "images" else
               f"a reading of the ayah {ayat[0]}")
            + "; its ledger and the listed passages follow it. Return only the output augment.md specifies.\n\n")
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


def verdict_report(listed: list[str], verdicts: dict[str, list[dict]], items: list[dict]) -> dict:
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
    mismatch = []
    for ref, vs in verdicts.items():
        for v in vs:
            s = v["verdict"].split(" - ")[0]
            for kind, nums in re.findall(r"(prose|ref)\s*((?:¶\s*\d+[,\s]*)+)", s):
                for n in map(int, re.findall(r"\d+", nums)):
                    if (kind == "prose" and (ref, n) not in prose) or (kind == "ref" and ref not in refs.get(n, set())):
                        mismatch.append(f"{ref}: {kind} ¶{n} in the verdict, no such addition applied")
    unjudged = sorted(({r for r, _ in prose} | {x for s in refs.values() for x in s}) - set(verdicts))
    return {"missing": missing, "mismatch": mismatch, "unjudged": unjudged,
            "relevant": sum(1 for vs in verdicts.values() if any("not relevant" not in v["verdict"] for v in vs)),
            "not_relevant": sum(1 for vs in verdicts.values() if all("not relevant" in v["verdict"] for v in vs))}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("run", type=Path)
    ap.add_argument("--brief", default="augment1")
    ap.add_argument("--model", choices=("sonnet", "opus"), default=MODEL)
    ap.add_argument("--go", action="store_true")
    a = ap.parse_args()
    model = a.model
    d = a.run if a.run.is_absolute() else V.HERE / a.run
    text, meta = build(d, a.brief)
    _, w, o = V.MODELS[model]
    n_in = V.est_tokens(text)
    est = n_in * w + (VERDICT_OUT if a.brief in VERDICT else OUT_TOKENS[meta["kind"]]) * o
    out = d / (f"augment.{a.brief}" + ("" if model == MODEL else f".{model}"))
    print(f"{out.relative_to(V.HERE)}: {meta['passages']} passages, ~{n_in:,} tokens in; est ${est:.2f} "
          f"({V.MODELS[model][0]}, effort {EFFORT})")
    if n_in > MAX_IN:
        raise SystemExit(f"prompt ~{n_in:,} tokens is over {MAX_IN:,}: split the passages before augmenting")
    if not a.go:
        return
    ref = "S" + str(int(d.parent.name[1:])) if meta["kind"] == "images" else meta["ayat"][0]
    row = {"ref": ref, "arm": "augment", "brief": f"{out.name.removeprefix('augment.')}.{d.name}"}
    if V.blocked(out):
        raise SystemExit(f"{out}: started or finished before (never rerun)")
    if est >= V.GATE_USD:
        V.log({**row, "status": "gated", "estimate_usd": round(est, 2)})
        raise SystemExit(f"gated at ${est:.2f}")
    out.mkdir(parents=True, exist_ok=True)
    (out / "prompt.md").write_text(text, encoding="utf-8")
    (out / "packet.json").write_text(json.dumps({**{k: v for k, v in meta.items() if k != "listed"}, "brief": a.brief, "model": V.MODELS[model][0]},
                                                ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    t0 = time.time()
    obj = V.call_opus(text, out, model, allow=None, effort=EFFORT)
    res = {**row, "model": V.MODELS[model][0], "effort": EFFORT, "seconds": round(time.time() - t0),
           "estimate_usd": round(est, 2), **V.usage_row(obj, text)}
    result = (obj.get("result") or "").strip()
    V.log(res)  # the paid call is recorded before any post-processing can fail
    if result and res["status"] == "ok":
        (out / "augment.raw.md").write_text(result + "\n", encoding="utf-8")
        src = V.HERE / meta["file"].replace("_commentary/v16/", "", 1)
        original = src.read_text(encoding="utf-8")
        if a.brief in VERDICT:
            ins, verdicts, led = parse_verdict(result)
            merged, ins = apply_marked(original, ins, a.brief, model)
            vr = verdict_report(meta["listed"], verdicts, ins)
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
            if vr["unjudged"]:
                print(f"WARNING: added without a verdict line: {', '.join(vr['unjudged'])}")
            (out / "verdict_report.json").write_text(json.dumps(vr, ensure_ascii=False, indent=1) + "\n",
                                                     encoding="utf-8")
            app = [r for r in ins if r["status"] == "applied"]
            extra = {"prose_added": sum(r["kind"] == "prose" for r in app),
                     "ref_lines": sum(r["kind"] == "refs" for r in app),
                     "refs_named": sum(len(re.findall(r"source:", r["text"])) for r in app if r["kind"] == "refs"),
                     "listed": len(meta["listed"]), "verdicts_missing": len(vr["missing"]),
                     "verdict_mismatch": len(vr["mismatch"]), "relevant": vr["relevant"],
                     "not_relevant": vr["not_relevant"]}
        V.log({"ref": res["ref"], "arm": "augment-applied", "brief": res["brief"], "insertions": res["insertions"],
               "applied": res["applied"], "not_applied": res["insertions"] - res["applied"],
               "insert_issues": len(issues), "ledger_lines": res["ledger_lines"], **extra, "check": res["check"]})
    print(f"{out.relative_to(V.HERE)}: {res['status']} ${res.get('cost_usd')} "
          f"{res.get('applied')}/{res.get('insertions')} applied {res['seconds']}s")
    if res["status"] != "ok":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
