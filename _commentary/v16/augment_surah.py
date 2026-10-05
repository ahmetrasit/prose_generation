#!/usr/bin/env python3
"""The surah-commentary augment (user, 2026-10-04 evening): augment9's verdict pass over one image section of
images.md at a time, seeded by the image-based discovery list (discover.py) instead of the per-ayah reciprocal lists,
run by agents the orchestrator spawns. Paragraph numbers are those of the whole commentary; a section's call may
serve only its own paragraphs. The additions of all finished sections are merged into one images.md with the same
marked blocks as the ayah augment (augment.apply_marked; strip_augment gives the original back, asserted).

  python3 -B _commentary/v16/augment_surah.py --surah 87 --status
  python3 -B _commentary/v16/augment_surah.py --surah 87 --section 3            # build: the estimate, no files
  python3 -B _commentary/v16/augment_surah.py --surah 87 --section 3 --spawn    # prompt.md, started.json, spawn.md
  python3 -B _commentary/v16/augment_surah.py --surah 87 --section 3 --finish   # after the agent replied
  python3 -B _commentary/v16/augment_surah.py --surah 87 --merge                # images.md from every finished section

Output: out/sNNN/augment.augment9s.opus/sec<k>/ (prompt.md, response.md, insertions.json, additions.md, verdicts.md,
verdict_report.json, run.log.json) and out/sNNN/augment.augment9s.opus/images.md (+ check.json, merge.json).
The ledger rows: `augment-surah` (the call, ref S<N>, brief augment9s.opus.sec<k>) and `augment-surah-applied`.
"""
from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import v16 as V  # noqa: E402
import missing as M  # noqa: E402
import augment as A  # noqa: E402
import agentrun as AR  # noqa: E402
import batch as B  # noqa: E402
import discover as DS  # noqa: E402
import packets as P  # noqa: E402

BRIEF, MODEL, MODEL_ID, EFFORT = "augment9s", "opus", "claude-opus-5-5", "high"
TIERS = ["strong", "medium", "weak", "contrast"]
OUT_PER_PASSAGE, OUT_BASE = 330, 15_000  # as augment.VERDICT_OUT


def out_root(s: int) -> Path:
    return DS.surah_dir(s) / f"augment.{BRIEF}.{MODEL}"


def section_list(s: int, k: int, override: Path | None = None) -> list[dict]:
    if override is None:
        raise ValueError("Select the discovery attempt explicitly with --run-tag or --list")
    f = override
    if not f.exists():
        raise ValueError(f"{f}: missing merged discovery list")
    lines = f.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise ValueError(f"{f}: missing header")
    head = lines[0].split("\t")
    required = {"ref", "tier", "bases", "explanations", "luna_label", "luna_turn", "terra_label", "terra_turn"}
    if len(head) != len(set(head)) or not required <= set(head):
        raise ValueError(f"{f}: invalid merged header")
    q, rows, seen = M.verses(), [], set()
    for number, line in enumerate(lines[1:], 2):
        if not line.strip():
            continue
        fields = line.split("\t")
        if len(fields) != len(head):
            raise ValueError(f"{f}:{number}: wrong field count")
        row = dict(zip(head, fields))
        if (row["ref"] not in q or row["ref"].startswith(f"{s}:") or row["ref"] in seen
                or row["tier"] not in TIERS or not row["explanations"].strip()
                or not set(row["bases"].split("+")) <= DS.BASES):
            raise ValueError(f"{f}:{number}: invalid or duplicate candidate")
        for model in DS.MODELS:
            label, turn = row[f"{model}_label"], row[f"{model}_turn"]
            if (label and (label not in DS.STRENGTH or turn not in ("1", "2"))) or (not label and turn):
                raise ValueError(f"{f}:{number}: invalid model provenance")
        seen.add(row["ref"])
        rows.append(row)
    return rows


def build(s: int, k: int, override: Path | None = None) -> tuple[str, dict]:
    _, images, _ = B.surah_inputs(s)
    text = images.read_text(encoding="utf-8")
    secs = DS.sections(text)
    sec = next((x for x in secs if x["k"] == k), None)
    if not sec:
        raise SystemExit(f"S{s}: no section {k} (1–{len(secs)})")
    paras = [(st, en, num) for st, en, num in A.paragraphs(text) if num and sec["start"] <= st < sec["end"]]
    numbered = [f"[¶{num}] " + text[st:en].strip() for st, en, num in paras]
    nums = [num for _, _, num in paras]
    cites = A.cited_by_paragraph(text)
    sec_cites = {n: cites[n] for n in nums}
    q = M.verses()
    key = lambda r: tuple(map(int, r.split(":")))
    rows = section_list(s, k, override)
    by_tier: dict[str, list[dict]] = {t: [] for t in TIERS}
    for r in rows:
        by_tier.setdefault(r["tier"], []).append(r)
    labels = [h for h in rows[0].keys() if h.endswith("_label")] if rows else []
    blocks, order = [], []
    for t in TIERS:
        rs = sorted(by_tier.get(t, []), key=lambda r: key(r["ref"]))
        if not rs:
            continue
        lines = []
        for r in rs:
            who = "; ".join(f"{h[:-6]}: {r[h]}" + (" (missing-ayat turn)" if r.get(h[:-6] + "_turn") == "2" else "")
                            for h in labels if r.get(h))
            lines.append(f"- ({r['ref']}) [{who}; basis: {r['bases']}]{A.cited_in(r['ref'], sec_cites)} {q[r['ref']]}"
                         f"\n  Unverified discovery rationale: {r['explanations']}")
            order.append(r["ref"])
        blocks.append(f"## {t} ({len(rs)})\n\n" + "\n".join(lines))
    listed = set(order)
    near: dict[str, str] = {}  # within two of every passage the section cites outside the surah
    for c in sorted({x for n in nums for x in cites[n]}, key=key):
        cs, ca = c.split(":")
        if cs == str(s):
            continue
        for d in (-2, -1, 1, 2):
            r = f"{cs}:{int(ca) + d}"
            if r in q and r not in listed and r not in near and r.split(":")[0] != str(s):
                near[r] = c
    if near:
        rs = sorted(near, key=key)
        blocks.append(f"## neighbours: within two ayat of a passage the section cites ({len(rs)})\n\n"
                      + "\n".join(f"- ({r}) [next to {near[r]}]{A.cited_in(r, sec_cites)} {q.get(r, '')}" for r in rs))
        order += rs
    led = images.parent / "ledger.md"
    bf = HERE / "prompts" / BRIEF / "augment.md"
    head = (f"Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of "
            f"surah {s}; below is its section {k} of {len(secs)} (\"{sec['title']}\"), with its paragraphs numbered as "
            "in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the "
            "output augment.md specifies.\n\n") + P.tool_line(f"{s}:1", "lookup")
    secs_txt = [(V.rel(bf), bf.read_text(encoding="utf-8")),
                (f"{V.rel(images)} section {k} (prose paragraphs numbered)", "\n\n".join(numbered)),
                (V.rel(led), led.read_text(encoding="utf-8") if led.exists() else "(no ledger)\n"),
                (f"passages from the discovery list ({len(order)})", "\n\n".join(blocks) + "\n")]
    import hashlib
    audit_path = override.with_suffix(".audit.json") if override else None
    if audit_path and audit_path.exists():
        audit = json.loads(audit_path.read_text())
        if audit.get("list_sha256") != hashlib.sha256(override.read_bytes()).hexdigest():
            raise ValueError("Discovery list differs from its audit sidecar")
        if audit.get("source_sha256") and audit["source_sha256"] != hashlib.sha256(images.read_bytes()).hexdigest():
            raise ValueError("Commentary changed since the selected discovery attempt")
        secs_txt.append(("Discovery accuracy findings (unverified; inspect canonical text)", json.dumps(audit, ensure_ascii=False)))
    head += "Discovery rationales and accuracy flags are unverified. Judge each against canonical Arabic, including speaker, negation and ayah boundaries.\n\n"
    full = head + "".join(f"===== {p} =====\n{b.rstrip()}\n\n" for p, b in secs_txt)
    return full, {"kind": "images-section", "file": V.rel(images), "surah": s, "section": k, "title": sec["title"],
                  "paragraphs": nums, "passages": len(order), "listed": order, "sections": len(secs),
                  "list_file": str(override), "list_sha256": hashlib.sha256(override.read_bytes()).hexdigest(),
                  "source_sha256": hashlib.sha256(images.read_bytes()).hexdigest(),
                  "discovery_candidates": len(rows), "context_neighbours": len(near)}


def estimate(text: str, n: int) -> float:
    _, w, o = V.MODELS[MODEL]
    return V.est_tokens(text) * w * A.LOOKUP_INPUT + (OUT_BASE + OUT_PER_PASSAGE * n) * o


def finish(s: int, k: int, override: Path | None = None) -> None:
    out = out_root(s) / f"sec{k}"
    st = json.loads((out / "started.json").read_text(encoding="utf-8")) if (out / "started.json").exists() else {}
    if st.get("runner") != "agent":
        raise SystemExit(f"{out}: not an agent-spawned run")
    if (out / "run.log.json").exists():
        raise SystemExit(f"{out}: already finished; never twice")
    text, meta = build(s, k, override)
    if (out / "prompt.md").read_text(encoding="utf-8") != text:
        print("WARNING: the prompt rebuilt now differs from the one the agent got (images.md or the list changed); "
              "the agent's prompt.md is what counts, the verdict report may be off")
    row = {"ref": f"S{s}", "arm": "augment-surah", "brief": f"{BRIEF}.{MODEL}.sec{k}", "section": meta["title"]}
    obj = AR.finish(out, "response.md")
    t0 = time.mktime(time.strptime(st["started"], "%Y-%m-%dT%H:%M:%S"))
    res = {**row, "model": obj.get("model") or MODEL_ID, "effort": EFFORT, "seconds": round(time.time() - t0),
           "estimate_usd": st.get("estimate_usd"), "runner": "agent", "cost_basis": obj.get("cost_basis"),
           **V.usage_row(obj, text)}
    try:
        bad, denied = P.audit(out, [])
        res["audit"] = "ok" if not bad else f"{len(bad)} outside the rule"
        res["denied"] = len(denied)
        for c in bad:
            print(f"WARNING: ran outside the rule: {c[:200]}")
        for c in denied:
            print(f"NOTE: refused (never ran): {c[:200]}")
    finally:
        V.log(res)
    result = (obj.get("result") or "").strip()
    if result and res["status"] != "ok":
        (out / "augment.raw.partial.md").write_text(result + "\n", encoding="utf-8")
        print(f"WARNING: status {res['status']}: nothing applied; the output is in augment.raw.partial.md")
    if not result or res["status"] != "ok":
        print(f"{out.relative_to(V.HERE)}: {res['status']} ${res.get('cost_usd')} None/None applied {res['seconds']}s")
        raise SystemExit(1)
    try:
        (out / "augment.raw.md").write_text(result + "\n", encoding="utf-8")
        original = Path(V.HERE / meta["file"].replace("_commentary/v16/", "", 1)).read_text(encoding="utf-8")
        ins, verdicts, led, diag = A.parse_verdict(result)
        for x in diag["unparsed_verdict_lines"]:
            print(f"WARNING: verdict line not understood: {x[:200]}")
        if not diag["verdicts_marker"]:
            print("WARNING: no === VERDICTS === line in the output")
        if diag["preamble"]:
            print(f"{'WARNING' if '===' in diag['preamble'] else 'NOTE'}: text before the first block (not applied): {diag['preamble'][:200]}")
        allowed = set(meta["paragraphs"])
        outside = []
        for r in ins:
            m = re.search(r"\d+", r.get("paragraph", "") or "")
            if not m or int(m.group(0)) not in allowed:
                outside.append(r)
        ins_in = [r for r in ins if r not in outside]
        merged, ins_in = A.apply_marked(original, ins_in, BRIEF, MODEL)
        for r in outside:
            r["status"] = "paragraph outside this section"
            print(f"WARNING: not applied (¶{r.get('paragraph')}, {r.get('ref')}): paragraph outside section {k}")
        ins = ins_in + outside
        (out / "insertions.json").write_text(json.dumps(ins, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        (out / "additions.md").write_text("".join(
            f"## ¶{r['paragraph']} · {r.get('kind', 'insert')} · {r.get('ref') or '-'} · {r['status']}\n\n**+** {r['text']}\n\n"
            for r in ins), encoding="utf-8")
        (out / "verdicts.md").write_text((led or "(no verdict lines)") + "\n", encoding="utf-8")
        for r in ins_in:
            if r["status"] != "applied":
                print(f"WARNING: not applied (¶{r['paragraph']}, {r['ref']}): {r['status']}")
        vr = A.verdict_report(meta["listed"], verdicts, ins_in, M.expand([original]), A.looked_up(out), str(s))
        for key_, label in (("missing", "listed passages have no verdict"), ("mismatch", ""), ("conflicts", "conflict with the commentary"),
                            ("unjudged", "added without a verdict line"), ("already_cited_rejects", "'not relevant' because already cited"),
                            ("looked_up_no_verdict", "looked up, no verdict"), ("consecutive_split", "consecutive ayat as separate references")):
            xs = vr[key_]
            if xs and key_ in ("mismatch", "conflicts", "consecutive_split"):
                for x in xs:
                    print(f"WARNING: {label + ': ' if label else ''}{x}")
            elif xs:
                print(f"WARNING: {len(xs)} {label}: {', '.join(xs[:20])}{' …' if len(xs) > 20 else ''}")
        (out / "verdict_report.json").write_text(json.dumps({**vr, "parse": diag}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        app = [r for r in ins_in if r["status"] == "applied"]
        V.log({"ref": res["ref"], "arm": "augment-surah-applied", "brief": res["brief"], "insertions": len(ins),
               "applied": len(app), "not_applied": len(ins) - len(app), "outside_section": len(outside),
               "prose_added": sum(r["kind"] == "prose" for r in app), "ref_lines": sum(r["kind"] == "refs" for r in app),
               "listed": len(meta["listed"]), "verdicts_missing": len(vr["missing"]), "verdict_mismatch": len(vr["mismatch"]),
               "conflicts": len(vr["conflicts"]), "relevant": vr["relevant"], "not_relevant": vr["not_relevant"]})
    except BaseException as x:
        print(f"WARNING: post-processing failed after the call: {x!r}; nothing is applied")
        V.log({"ref": res["ref"], "arm": "augment-surah-applied", "brief": res["brief"], "post_error": repr(x)[:500]})
        raise
    print(f"{out.relative_to(V.HERE)}: {res['status']} ${res.get('cost_usd')} {len(app)}/{len(ins)} applied {res['seconds']}s")


def merge(s: int) -> None:
    _, images, _ = B.surah_inputs(s)
    original = images.read_text(encoding="utf-8")
    root = out_root(s)
    secs = DS.sections(original)
    items, done, missing = [], [], []
    for sec in secs:
        f = root / f"sec{sec['k']}" / "insertions.json"
        if f.exists():
            done.append(sec["k"])
            items += [r for r in json.loads(f.read_text(encoding="utf-8")) if r["status"] == "applied"]
        else:
            missing.append(sec["k"])
    if missing:
        print(f"NOTE: sections without a finished augment: {', '.join(map(str, missing))} (merged without them)")
    for r in items:
        r["status"] = "applied"
    merged, items = A.apply_marked(original, items, BRIEF, MODEL)
    refused = [r for r in items if r["status"] != "applied"]
    for r in refused:
        print(f"WARNING: at merge, not applied (¶{r['paragraph']}, {r.get('ref')}): {r['status']}")
    (root / "images.md").write_text(merged, encoding="utf-8")
    check = V.run_check(root / "images.md", f"{s}:1", root / "check.json", report=False)
    (root / "merge.json").write_text(json.dumps({"sections_done": done, "sections_missing": missing, "applied": len(items) - len(refused),
                                                 "refused": len(refused), "check": check, "merged_at": time.strftime("%Y-%m-%dT%H:%M:%S")},
                                                indent=1) + "\n", encoding="utf-8")
    print(f"{root.relative_to(V.HERE)}/images.md: {len(items) - len(refused)} additions from sections {done}; check {check}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--section", type=int)
    ap.add_argument("--list", type=Path, help="a merged list file in place of the discovery's (tests)")
    ap.add_argument("--run-tag", help="explicit discovery attempt to use")
    ap.add_argument("--spawn", action="store_true")
    ap.add_argument("--finish", action="store_true")
    ap.add_argument("--merge", action="store_true")
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args()
    if a.run_tag and a.list:
        ap.error("choose --run-tag or --list, not both")
    if a.run_tag and a.section is not None:
        a.list = DS.discovery_dir(a.surah, a.run_tag) / f"sec{a.section}.merged.tsv"
    if a.merge:
        merge(a.surah); return
    if a.status or a.section is None:
        _, images, _ = B.surah_inputs(a.surah)
        for sec in DS.sections(images.read_text(encoding="utf-8")):
            d = out_root(a.surah) / f"sec{sec['k']}"
            lst = DS.surah_dir(a.surah) / "discovery" / f"sec{sec['k']}.merged.tsv"
            state = ("done" if (d / "insertions.json").exists() else "BLOCKED (started, not finished)" if V.blocked(d)
                     else "partial" if (d / "augment.raw.partial.md").exists() else "-")
            print(f"S{a.surah} sec{sec['k']} '{sec['title']}': list {'yes' if lst.exists() else 'no'}; augment {state}")
        if (out_root(a.surah) / "images.md").exists():
            print(f"merged: {out_root(a.surah).relative_to(V.HERE)}/images.md")
        return
    if a.finish:
        finish(a.surah, a.section, a.list); return
    text, meta = build(a.surah, a.section, a.list)
    out = out_root(a.surah) / f"sec{a.section}"
    est = estimate(text, meta["passages"])
    print(f"{out.relative_to(V.HERE)}: section {a.section}/{meta['sections']} '{meta['title']}', paragraphs "
          f"{meta['paragraphs'][0]}–{meta['paragraphs'][-1]}, {meta['passages']} passages, ~{V.est_tokens(text):,} tokens in; "
          f"est ${est:.2f} ({MODEL_ID}, effort {EFFORT})")
    V.blocked_note(out)
    if not a.spawn:
        return
    if V.blocked(out):
        raise SystemExit(f"{out}: started or finished before (never rerun)")
    AR.prepare(out, text, {"ref": f"S{a.surah}", "arm": "augment-surah", "brief": f"{BRIEF}.{MODEL}.sec{a.section}",
                           "model": MODEL_ID, "effort": EFFORT, "estimate_usd": round(est, 2), "section": a.section},
               "augment", "response.md", lookup=True)


if __name__ == "__main__":
    main()
