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

MODEL, EFFORT = "sonnet", "high"
OUT_TOKENS = {"images": 40_000, "ayah": 20_000}  # assumed, thinking included
PARA_SPLIT = re.compile(r"(\n[ \t]*\n)")
SENTENCE_END = re.compile(r"[.!?…][\"”’»)]*$")
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


def passages(prose: str, ayat: list[str]) -> tuple[str, int]:
    """The listed passages not cited in the prose, best tier first, each with the ayat whose lists hold it."""
    used = M.expand([prose])
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
                f"- ({r}) [listed for {', '.join(where[r])}] {q.get(r, '')}" for r in rs))
    return "\n\n".join(blocks) + "\n", len(best)


def build(d: Path, brief: str) -> tuple[str, dict]:
    kind, f, ayat, _ = target(d)
    text = f.read_text(encoding="utf-8")
    led = d / "ledger.md"
    numbered = []
    for st, en, num in paragraphs(text):
        numbered.append((f"[¶{num}] " if num else "") + text[st:en].strip())
    pas, n = passages(text, ayat)
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
    return full, {"kind": kind, "file": V.rel(f), "ayat": ayat, "passages": n}


def parse(result: str) -> tuple[list[dict], str]:
    result = re.sub(r"(?m)^[ \t]*```[^\n]*$", "", result)  # code fences around the output, if any
    body, _, led = result.partition(V.LEDGER_MARK)
    ins = []
    for blk in re.split(r"(?m)^=== INSERT ===[ \t]*$", body)[1:]:
        rec = {}
        m = re.search(r"(?ms)^text:[ \t]*(.*)\Z", blk)
        rec["text"] = re.sub(r"\s*\n\s*", " ", m.group(1)).strip() if m else ""
        head = blk[:m.start()] if m else blk
        for k in ("paragraph", "after", "ref"):
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


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("run", type=Path)
    ap.add_argument("--brief", default="augment1")
    ap.add_argument("--go", action="store_true")
    a = ap.parse_args()
    d = a.run if a.run.is_absolute() else V.HERE / a.run
    text, meta = build(d, a.brief)
    _, w, o = V.MODELS[MODEL]
    n_in = V.est_tokens(text)
    est = n_in * w + OUT_TOKENS[meta["kind"]] * o
    out = d / f"augment.{a.brief}"
    print(f"{out.relative_to(V.HERE)}: {meta['passages']} passages, ~{n_in:,} tokens in; est ${est:.2f} "
          f"({V.MODELS[MODEL][0]}, effort {EFFORT})")
    if n_in > MAX_IN:
        raise SystemExit(f"prompt ~{n_in:,} tokens is over {MAX_IN:,}: split the passages before augmenting")
    if not a.go:
        return
    ref = "S" + str(int(d.parent.name[1:])) if meta["kind"] == "images" else meta["ayat"][0]
    row = {"ref": ref, "arm": "augment", "brief": f"{a.brief}.{d.name}"}
    if V.blocked(out):
        raise SystemExit(f"{out}: started or finished before (never rerun)")
    if est >= V.GATE_USD:
        V.log({**row, "status": "gated", "estimate_usd": round(est, 2)})
        raise SystemExit(f"gated at ${est:.2f}")
    out.mkdir(parents=True, exist_ok=True)
    (out / "prompt.md").write_text(text, encoding="utf-8")
    (out / "packet.json").write_text(json.dumps({**meta, "brief": a.brief, "model": V.MODELS[MODEL][0]},
                                                ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    t0 = time.time()
    obj = V.call_opus(text, out, MODEL, allow=None, effort=EFFORT)
    res = {**row, "model": V.MODELS[MODEL][0], "effort": EFFORT, "seconds": round(time.time() - t0),
           "estimate_usd": round(est, 2), **V.usage_row(obj, text)}
    result = (obj.get("result") or "").strip()
    V.log(res)  # the paid call is recorded before any post-processing can fail
    if result and res["status"] == "ok":
        (out / "augment.raw.md").write_text(result + "\n", encoding="utf-8")
        ins, led = parse(result)
        src = V.HERE / meta["file"].replace("_commentary/v16/", "", 1)
        original = src.read_text(encoding="utf-8")
        merged, ins = apply(original, ins)
        (out / src.name).write_text(merged, encoding="utf-8")
        (out / "insertions.json").write_text(json.dumps(ins, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        (out / "additions.md").write_text("".join(
            f"## ¶{r['paragraph']} · {r['ref']} · {r['status']}\n\n… {r['after']}\n\n**+** {r['text']}\n\n"
            for r in ins), encoding="utf-8")
        (out / "ledger.md").write_text((led or "(no ledger lines)") + "\n", encoding="utf-8")
        _, _, _, cref = target(d)
        subprocess.run([sys.executable, str(V.CHECK), str(out / src.name), "--ref", cref, "--out",
                        str(out / "check.json"), "--quiet"], cwd=V.CHECK.parent)
        res["insertions"] = len(ins)
        res["applied"] = sum(1 for r in ins if r["status"] == "applied")
        res["ledger_lines"] = sum(1 for ln in led.splitlines() if ln.strip().startswith("-"))
        V.log({"ref": res["ref"], "arm": "augment-applied", "brief": res["brief"], "insertions": res["insertions"],
               "applied": res["applied"], "ledger_lines": res["ledger_lines"]})
    print(f"{out.relative_to(V.HERE)}: {res['status']} ${res.get('cost_usd')} "
          f"{res.get('applied')}/{res.get('insertions')} applied {res['seconds']}s")
    if res["status"] != "ok":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
