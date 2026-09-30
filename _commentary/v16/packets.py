#!/usr/bin/env python3
"""Controlled packets for the map3 test (2026-09-30; see REVIEW_r7_r10.md, steps 0-3).

Every packet is an earlier saved prompt with named sections swapped, so everything else stays byte-identical:
  map     the S1 map call: out/s001/surah.r2/prompt.md with only the brief replaced (prompts/map3/surah_map.md)
  writer  a writer call: work/<S_A>/DM.<brief>/prompt.md (frozen r3 evidence) with the map section replaced by a
          new map without its `## Not carried` section, and optionally the dictionary without branch labels

  python3 -B _commentary/v16/packets.py map [--go]
  python3 -B _commentary/v16/packets.py writer --ayah 1:6 --brief r10 --map out/s001/surah.map3/map.md
          [--no-labels] [--tool] [--go]
--tool adds the end-of-discovery check (missing.py): one line in the packet header tells the agent to run it
once before writing, and the call allows that single command and nothing else.
Without --go it only builds and prints the estimate. Calls follow v16's rules: one call, never rerun, gate $5.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import v16 as V  # noqa: E402

HEAD = re.compile(r"(?m)^===== (.+?) =====\n")
MISSING = V.HERE / "missing.py"
ALLOW = f"python3 {MISSING}"


SAFE_CMD = re.compile(rf"^{re.escape(ALLOW)} (?:S\d+|\d+:\d+)(?: [0-9:()\[\],;.\-–— ]*)?$")


def tool_extra(target: str) -> int:
    """Upper bound on the tool result's tokens: every strong passage missing, with its Arabic."""
    import missing as M
    text = M.verses()
    focus = [r for r in text if r.split(":")[0] == target[1:] and r.split(":")[1] != "0"] if target.startswith("S") \
        else [target]
    listed, _ = M.strong(focus)
    return V.est_tokens("\n".join(f"- ({r}) {text.get(r, '')}" for r in listed) + M.INSTRUCTION)


def audit(d: Path) -> list[str]:
    """Every command the agent ran must be the allowed check with plain refs; anything else is reported."""
    f = d / "tool_calls.json"
    calls = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    return [str((c.get("input") or {}).get("command")) for c in calls
            if not SAFE_CMD.match(str((c.get("input") or {}).get("command", "")))]


def tool_line(target: str) -> str:
    return (f"When your discovery is complete and before you write your final output, run this command once, "
            f"with every Quran reference outside this surah that your output will use: "
            f"`{ALLOW} {target} <refs separated by spaces>`. Judge what it returns, then write your final output. "
            f"Run it only once; no other tool is available.\n\n")


def split(text: str) -> tuple[str, list[list[str]]]:
    parts = HEAD.split(text)
    return parts[0], [[p, b] for p, b in zip(parts[1::2], parts[2::2])]


def join(head: str, secs: list[list[str]]) -> str:
    return head + "".join(f"===== {p} =====\n{b}" for p, b in secs)


def swap(secs: list[list[str]], suffix: str, path: str, body: str) -> None:
    hits = [s for s in secs if s[0].endswith(suffix)]
    if len(hits) != 1:
        raise SystemExit(f"expected one section ending {suffix}, got {len(hits)}")
    hits[0][0], hits[0][1] = path, body if body.endswith("\n\n") else body.rstrip("\n") + "\n\n"


def strip_not_carried(map_text: str) -> str:
    return re.split(r"(?m)^## Not carried\b", map_text)[0].rstrip() + "\n"


def drop_labels(dict_text: str) -> str:
    """`- **B012** label — gloss · gloss` becomes `- **B012** gloss · gloss` (per-sense glosses and phrases kept)."""
    return re.sub(r"(?m)^(- \*\*B\d+\*\*) [^\n—]*? — ", r"\1 ", dict_text)


def sha(t: str) -> str:
    return hashlib.sha256(t.encode()).hexdigest()


# --no-hft (user, 2026-09-30): the map call without the HFT section, to keep its cost safely under the gate. The
# brief and header lines that mention HFT are adapted in the packet only; prompts/<brief>/ keeps them for re-adding.
NO_HFT = [
    ("earlier readers' channel review (channels.md) and activation hypotheses (hft.md),",
     "an earlier reader's channel review (channels.md),"),
    ("The channel review and the HFT records are proposals by earlier readers. Ignore their judgements:",
     "The channel review is an earlier reader's proposal. Ignore its judgements:"),
    ("Do not rediscover what they already assembled: start from their chains,",
     "Do not rediscover what it already assembled: start from its chains,"),
    ("Where their wording\nabstracts", "Where its wording\nabstracts"),
    ("Each channel subchannel and each HFT record you did not carry", "Each channel subchannel you did not carry"),
]
NO_HFT_HEAD = ("channels.md and hft.md (both are earlier readers' proposals: ignore their judgements",
               "channels.md (an earlier reader's proposal: ignore its judgements")


def map_packet(brief: str = "map3", hft: bool = True, tool: bool = False) -> tuple[str, Path]:
    head, secs = split((V.OUT / "s001" / "surah.r2" / "prompt.md").read_text(encoding="utf-8"))
    body = (V.HERE / "prompts" / brief / "surah_map.md").read_text(encoding="utf-8")
    name = (brief if hft else f"{brief}.nohft") + (".tool" if tool else "")
    if not hft:
        for a, b in NO_HFT:
            if body.count(a) != 1:
                raise SystemExit(f"brief line not found once: {a[:50]}")
            body = body.replace(a, b)
        if head.count(NO_HFT_HEAD[0]) != 1:
            raise SystemExit("header line not found")
        head = head.replace(*NO_HFT_HEAD)
        secs = [s for s in secs if not s[0].endswith("hft.md")]
    swap(secs, "surah_map.md", f"_commentary/v16/prompts/{brief}/surah_map.md" + ("" if hft else " (adapted)"),
         body)
    if tool:
        head = head.rstrip("\n") + "\n\n" + tool_line("S1")
    text = join(head, secs)
    wd = V.WORK / "s001" / f"surah.{name}"
    wd.mkdir(parents=True, exist_ok=True)
    (wd / "prompt.md").write_text(text, encoding="utf-8")
    json.dump({"brief": brief, "hft": hft, "tool": tool, "source_prompt": "out/s001/surah.r2/prompt.md", "prompt_sha256": sha(text),
               "evidence_sha256": sha("".join(b for p, b in secs if not p.endswith("surah_map.md")))},
              (wd / "packet.json").open("w"), indent=1)
    return text, V.OUT / "s001" / f"surah.{name}"


def writer_packet(ref: str, brief: str, map_path: Path, labels: bool, tool: bool = False) -> tuple[str, Path, str]:
    name = V.sa(ref)[1]
    head, secs = split((V.WORK / name / f"DM.{brief}" / "prompt.md").read_text(encoding="utf-8"))
    tag = map_path.parent.name.replace("surah.", "") + ("" if labels else ".nolabel") + (".tool" if tool else "")
    swap(secs, "map.md", f"_commentary/v16/{map_path.relative_to(V.HERE)} (without ## Not carried)",
         strip_not_carried(map_path.read_text(encoding="utf-8")))
    if not labels:
        d = [s for s in secs if s[0].endswith("01_dictionary.md")][0]
        d[0], d[1] = d[0] + " (without branch labels)", drop_labels(d[1])
    if tool:
        head = head.rstrip("\n") + "\n\n" + tool_line(ref)
    text = join(head, secs)
    wd = V.WORK / name / f"DM.{brief}.{tag}"
    wd.mkdir(parents=True, exist_ok=True)
    (wd / "prompt.md").write_text(text, encoding="utf-8")
    json.dump({"ref": ref, "brief": brief, "map": str(map_path.relative_to(V.HERE)), "labels": labels, "tool": tool,
               "prompt_sha256": sha(text)}, (wd / "packet.json").open("w"), indent=1)
    return text, V.OUT / name / f"DM.{brief}.{tag}", tag


def estimate(text: str, kind: str, target: str | None) -> float:
    """v16's estimate, plus (with the check) the tool result written to cache and one extra cached re-read."""
    est = V.estimate(text, kind)
    if target:
        _, w, _ = V.MODELS["opus"]
        est += tool_extra(target) * w + V.est_tokens(text) * w * 0.05
    return est


def call(text: str, d: Path, kind: str, row: dict, ledger: bool, tool: bool = False) -> None:
    est = estimate(text, kind, (row["ref"] if tool else None))
    if V.blocked(d):
        raise SystemExit(f"{d}: started or finished before (never rerun)")
    if est >= V.GATE_USD:
        V.log({**row, "status": "gated", "estimate_usd": round(est, 2)})
        raise SystemExit(f"gated at ${est:.2f}")
    d.mkdir(parents=True, exist_ok=True)
    (d / "prompt.md").write_text(text, encoding="utf-8")
    t0 = time.time()
    obj = V.call_opus(text, d, allow=ALLOW if tool else None)
    out = {**row, "model": V.MODELS["opus"][0], "seconds": round(time.time() - t0), "estimate_usd": round(est, 2),
           **V.usage_row(obj, text)}
    result = (obj.get("result") or "").strip()
    if result and kind == "surah":
        (d / "map.md").write_text(result + "\n", encoding="utf-8")
        out["map_complete"] = V.map_complete(d / "map.md")
    elif result:
        prose, sep, led = result.partition(V.LEDGER_MARK)
        out["ledger"] = bool(sep)
        if sep:
            (d / "ledger.md").write_text(led.strip() + "\n", encoding="utf-8")
        reading = d / f"{d.parent.name}.reading.tr.md"
        reading.write_text(prose.strip() + "\n", encoding="utf-8")
        subprocess.run([sys.executable, str(V.CHECK), str(reading), "--ref", row["ref"], "--out",
                        str(d / "check.json"), "--quiet"], cwd=V.CHECK.parent)
    if tool:
        bad = audit(d)
        out["tool_audit"] = "ok" if not bad else {"unexpected_commands": bad}
        if bad:
            print(f"WARNING: unexpected commands run by the agent, treat this run as contaminated: {bad}")
    V.log(out)
    print(f"{d.relative_to(V.HERE)}: {out['status']} ${out.get('cost_usd')} {out.get('words')}w {out['seconds']}s")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=("map", "writer"))
    ap.add_argument("--brief")
    ap.add_argument("--ayah")
    ap.add_argument("--map", type=Path)
    ap.add_argument("--no-labels", action="store_true")
    ap.add_argument("--no-hft", action="store_true")
    ap.add_argument("--tool", action="store_true")
    ap.add_argument("--go", action="store_true")
    a = ap.parse_args()
    if a.cmd == "map":
        brief = a.brief or "map3"
        text, d = map_packet(brief, not a.no_hft, a.tool)
        n_out = 130_000  # r2 map measured 121.8k output; the estimate below also shows v16's standard 80k
        _, w, o = V.MODELS["opus"]
        n_in = V.est_tokens(text)
        realistic = n_in * (1 + n_out // V.MESSAGE_CAP) * w + n_out * o
        extra = estimate(text, "surah", "S1") - V.estimate(text, "surah") if a.tool else 0.0
        print(f"{d.relative_to(V.HERE)}: {len(text):,} chars ~{n_in:,} tokens; est ${V.estimate(text, 'surah') + extra:.2f} "
              f"(80k out), ${realistic + extra:.2f} at {n_out // 1000}k out")
        if a.go:
            call(text, d, "surah", {"ref": "S1", "arm": "surah", "brief": d.name.replace("surah.", "")}, False, a.tool)
        return
    text, d, tag = writer_packet(a.ayah, a.brief, (V.HERE / a.map) if not a.map.is_absolute() else a.map,
                                 not a.no_labels, a.tool)
    print(f"{d.relative_to(V.HERE)}: {len(text):,} chars; est ${estimate(text, 'ayah', a.ayah if a.tool else None):.2f}")
    if a.go:
        call(text, d, "ayah", {"ref": a.ayah, "arm": "DM", "brief": f"{a.brief}.{tag}"}, True, a.tool)


if __name__ == "__main__":
    main()
