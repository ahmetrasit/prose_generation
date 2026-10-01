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
once before writing (the images step: once per ayah of the surah), and the call allows that single command and
nothing else; `missing.py text <refs>` (the Arabic of verses) may be run as often as needed.
r12 (user, 2026-10-01): a brief with "slice_images" gives the writer only the image sections whose Kaynaklar members
cite its ayah, plus ## Buluşmalar; the images call takes --tool and its output gets check.py too.
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


SAFE_CMD = re.compile(rf"{re.escape(ALLOW)} (?:S\d+|\d+:\d+|text)(?: [0-9:()\[\],;.\-–— ]*)?")  # fullmatch
LOOKUPS = 6  # assumed `text` calls per run, for the estimate: each re-reads the prompt and adds up to ~4k tokens


def surah_ayat(s: int) -> list[str]:
    q = V.src().quran
    return [f"{s}:{a}" for a in range(1, 300) if f"{s}:{a}" in q]


def check_targets(target: str, kind: str) -> list[str]:
    """The list targets a call may ask for: its ayah; for the images step every ayah of the surah; for the map S<n>."""
    if kind == "images":
        return surah_ayat(int(target.lstrip("S")))
    if kind == "lookup":
        return []
    return [target]


def tool_extra(target: str, kind: str = "ayah") -> int:
    """Upper bound on the tool results' tokens: every listed passage missing, rendered as missing.py would, for each
    list the call may ask for, plus the assumed verse lookups."""
    import missing as M
    text = M.verses()
    n = 0
    for t in check_targets(target, kind):
        if t.startswith("S"):
            focus = [r for r in text if r.split(":")[0] == t[1:] and r.split(":")[1] != "0"]
            groups, _ = M.listed(focus, M.SURAH_TIERS)
        else:
            groups, _ = M.listed([t], tuple(x[0] for x in M.TIERS))
        n += V.est_tokens(M.render(groups) + M.instruction()) if groups else 0
    return n + LOOKUPS * 4_000


DENIED = "Permission to use Bash has been denied"


def audit(d: Path, targets: list[str] | None = None) -> tuple[list[str], list[str]]:
    """Every command the agent ran must be the allowed check with plain refs, for one of its own targets, or a text
    lookup; anything else is reported. Returns (commands that ran outside the rule, commands the permission mode
    refused, which never ran)."""
    f = d / "tool_calls.json"
    calls = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    bad, denied = [], []
    for c in calls:
        cmd = str((c.get("input") or {}).get("command", ""))
        if c.get("is_error") and DENIED in str(c.get("result", "")):
            denied.append(cmd)
            continue
        if not SAFE_CMD.fullmatch(cmd):
            bad.append(cmd)
            continue
        t = cmd[len(ALLOW) + 1:].split(" ", 1)[0]
        if targets is not None and t != "text" and t not in targets:
            bad.append(cmd)
    return bad, denied


def tool_line(target: str, kind: str = "ayah") -> str:
    # The instruction set lives here, in the prompt, as well as in the script's output: the permission test showed
    # the model treats instructions inside a tool result as untrusted text (out/permtest/run.log.json).
    if kind == "lookup":  # r13: the writer reads verse text; the list is left to augment
        return (f"To read a Quran passage's Arabic before you use it, run `{ALLOW} text <refs>` (up to 40 refs "
                f"per call) as often as you need. No other command or tool is available.\n\n")
    if kind == "images":
        ayat = surah_ayat(int(target.lstrip("S")))
        run = (f"run this command once for each ayah of the surah ({ayat[0]} to {ayat[-1]}), each time with every "
               f"Quran reference outside this surah that your output will use: "
               f"`{ALLOW} <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier "
               f"cross-reference list")
    else:
        run = (f"run this command once, with every Quran reference outside this surah that your output will use: "
               f"`{ALLOW} {target} <refs separated by spaces>`. It lists refs from an earlier cross-reference list")
    return (f"When your discovery is complete and before you write your final output, {run}, by tier, that your "
            f"refs do not include. That list is not authoritative and may be incomplete: judge each passage "
            f"yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read "
            f"a passage's Arabic before judging it, run `{ALLOW} text <refs>` (up to 40 refs per call) as often as "
            f"you need. Also add any other passage you now recall that belongs, whether listed or not. Then write "
            f"your final output. No other command or tool is available.\n\n")


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


def surah_source(s: int) -> tuple[str, str]:
    """(prompt text, its path) of the r2 surah call a map packet starts from: S1's saved call prompt (the S1 packets
    stay byte-identical); any other surah's r2 surah prompt, built fresh by v16.surah_build (writes work/s<NNN>/)."""
    if s == 1:
        p = V.OUT / "s001" / "surah.r2" / "prompt.md"
        return p.read_text(encoding="utf-8"), "out/s001/surah.r2/prompt.md"
    # v16.surah_build needs the surah's channel review; v9 HFT files are optional (a nohft map drops them)
    ayat = surah_ayat(s)
    need = [V.CHANNELS / f"s{s:03d}" / "reader_a_pilot.md"]
    lacking = [str(x) for x in need if not x.exists()]
    if not ayat or lacking:
        raise SystemExit(f"surah {s}: inputs missing for the surah build ({len(lacking)} files, e.g. "
                         f"{lacking[0] if lacking else 'no ayat'})")
    text, wd = V.surah_build(s, "r2")
    return text, str((wd / "prompt.md").relative_to(V.HERE))


def map_packet(brief: str = "map3", hft: bool = True, tool: bool = False, tag: str = "",
               s: int = 1) -> tuple[str, Path]:
    src_text, src_path = surah_source(s)
    head, secs = split(src_text)
    body = (V.HERE / "prompts" / brief / "surah_map.md").read_text(encoding="utf-8")
    name = (brief if hft else f"{brief}.nohft") + (".tool" if tool else "") + (f".{tag}" if tag else "")
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
        head = head.rstrip("\n") + "\n\n" + tool_line(f"S{s}")
    text = join(head, secs)
    wd = V.WORK / f"s{s:03d}" / f"surah.{name}"
    wd.mkdir(parents=True, exist_ok=True)
    (wd / "prompt.md").write_text(text, encoding="utf-8")
    json.dump({"brief": brief, "hft": hft, "tool": tool, "source_prompt": src_path, "prompt_sha256": sha(text),
               "evidence_sha256": sha("".join(b for p, b in secs if not p.endswith("surah_map.md")))},
              (wd / "packet.json").open("w"), indent=1)
    return text, V.OUT / f"s{s:03d}" / f"surah.{name}"


# images (user, 2026-09-30): one surah call turns the map into developed images (the surah commentary draft); an
# ayah writer can then read the images in place of the map (`writer --images`).
MAP_DESC = ("map.md (an earlier reader's map of the image chains that run through the whole surah, with the dictionary "
            "phrases of their members in other ayat; a proposal, not an authority)")
IMAGES_DESC = ("images.md (an earlier reader's commentary on the surah's images: each image explained, what it makes "
               "perceptible, what each ayah's words add, where images meet, with each image's sources; a proposal, "
               "not an authority. The images are already explained at surah level: recall one briefly and develop what "
               "this ayah's words add to it)")


IMAGES_DESC_SLICED = ("images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources "
                      "include this ayah, and the section on where images meet: each image explained, what it makes "
                      "perceptible, what each ayah's words add, with each image's sources; a proposal, not an "
                      "authority. The images are already explained at surah level: recall one briefly and develop "
                      "what this ayah's words add to it)")


# r12_1 (user, 2026-10-01): the r12 reading presented the surah commentary as "earlier ayat explained"; a recalled
# image is tied to the ayah whose words carry it and restated briefly, never as something explained before.
IMAGES_DESC_RECALL = IMAGES_DESC_SLICED.replace(
    "The images are already explained at surah level: recall one briefly and develop what this ayah's words add to it",
    "The surah commentary develops these images for the reader: recall one briefly, tied to the ayah whose words "
    "carry it and restated in your own words, never as something explained or told before, and develop what this "
    "ayah's words add to it")
assert IMAGES_DESC_RECALL != IMAGES_DESC_SLICED
# r13 (user, 2026-10-01): the writer develops each image its ayah's words take part in; the brief says how.
IMAGES_DESC_OWN = ("images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources "
                   "include this ayah, and the section on where images meet; a proposal, not an authority. Develop "
                   "here each image this ayah's words take part in, as write.md says; the shared scenes are the "
                   "surah commentary's)")


def slice_images(text: str, ref: str, preamble: bool = True) -> tuple[str, list[str]]:
    """The images text before the first section (unless preamble=False: r13, after a process note opened the S100
    images), every `## ` section whose Kaynaklar members (the part before "Kur'an:") cite `ref`, and ## Buluşmalar;
    with the kept headings."""
    parts = re.split(r"(?m)^(?=## )", text)
    pre, secs = (parts[0], parts[1:]) if not parts[0].startswith("## ") else ("", parts)
    cite = re.compile(rf"(?<![\d:]){re.escape(ref)}(?![\d:])")
    kept = []
    for sec in secs:
        head = sec.split("\n", 1)[0][3:].strip()
        members = " ".join(re.split(r"Kur'?an:", ln, maxsplit=1)[0] for ln in sec.splitlines() if ln.startswith("Kaynaklar:"))
        if head.startswith("Buluşmalar") or cite.search(members):
            kept.append(sec)
    return (pre if preamble else "") + "".join(kept), [s.split("\n", 1)[0][3:].strip() for s in kept]


def images_complete(f: Path) -> bool:
    t = "\n" + (f.read_text(encoding="utf-8") if f.exists() else "")
    return t.count("\n## ") >= 3 and "\n## Buluşmalar" in t


def images_packet(map_path: Path, brief: str = "images1", tool: bool = False, s: int = 1) -> tuple[str, Path]:
    if not V.map_complete(map_path):
        raise SystemExit(f"{map_path}: incomplete map (no ## Chains or ## Ayat)")
    if map_path.parent.parent.name != f"s{s:03d}":
        raise SystemExit(f"{map_path}: not a map of surah {s}")
    _, secs = split(surah_source(s)[0])
    text_sec = [s for s in secs if s[0].endswith("text.md")]
    if len(text_sec) != 1:
        raise SystemExit("surah.r2 prompt: expected one text.md section")
    brief_f = V.HERE / "prompts" / brief / "surah_images.md"
    head = (f"Surah: {s}. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and "
            "map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their "
            "members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of "
            "Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.\n\n")
    if tool:
        head = head.rstrip("\n") + "\n\n" + tool_line(f"S{s}", "images")
    secs = [[V.rel(brief_f), brief_f.read_text(encoding="utf-8")], text_sec[0],
            [f"_commentary/v16/{map_path.relative_to(V.HERE)} (without ## Not carried)",
             strip_not_carried(map_path.read_text(encoding="utf-8"))]]
    for sec in secs:
        sec[1] = sec[1] if sec[1].endswith("\n\n") else sec[1].rstrip("\n") + "\n\n"
    text = join(head, secs)
    name = f"images.{brief}.{map_path.parent.name.replace('surah.', '')}" + (".tool" if tool else "")
    wd = V.WORK / f"s{s:03d}" / name
    wd.mkdir(parents=True, exist_ok=True)
    (wd / "prompt.md").write_text(text, encoding="utf-8")
    json.dump({"brief": brief, "map": str(map_path.relative_to(V.HERE)), "tool": tool, "prompt_sha256": sha(text)},
              (wd / "packet.json").open("w"), indent=1)
    return text, V.OUT / f"s{s:03d}" / name


def writer_packet(ref: str, brief: str, map_path: Path, labels: bool, tool: bool = False,
                  images: Path | None = None) -> tuple[str, Path, str]:
    name = V.sa(ref)[1]
    d_base = V.BRIEFS[brief].get("base") == "D"
    if d_base:  # r13: the dictionary arm's packet plus the images; no map section to swap (any surah)
        if not images:
            raise SystemExit(f"brief {brief} needs --images")
        head, secs = split(V.build(ref, "D", brief)[0])
        anchor = V.BASE_EVIDENCE + " and your own knowledge"
        if head.count(anchor) != 1:
            raise SystemExit("header: evidence line not found once")
        head = head.replace(anchor, V.BASE_EVIDENCE + " and " + MAP_DESC + " and your own knowledge")
        secs.append(["map.md", ""])
    else:
        head, secs = split((V.WORK / name / f"DM.{brief}" / "prompt.md").read_text(encoding="utf-8"))
    if images:  # the images replace the map section; the header describes them instead of the map
        if not images_complete(images) or not (images.parent / "ledger.md").exists():
            raise SystemExit(f"{images}: incomplete images (fewer than 3 sections, no ## Buluşmalar or no ledger)")
        src = images.parent / "packet.json"  # out/ has no packet.json; the build record is in work/
        if not src.exists() and images.parent.is_relative_to(V.OUT):
            src = V.WORK / images.parent.relative_to(V.OUT) / "packet.json"
        if not src.exists() or json.loads(src.read_text(encoding="utf-8")).get("map") != str(map_path.relative_to(V.HERE)):
            raise SystemExit(f"{images}: --map does not match the map these images were built from ({src})")
        if head.count(MAP_DESC) != 1:
            raise SystemExit("header: map description not found once")
        sliced = V.BRIEFS[brief].get("slice_images", False)
        body, kept = images.read_text(encoding="utf-8"), None
        if sliced:
            body, kept = slice_images(body, ref, preamble=not V.BRIEFS[brief].get("own_images", False))
            if not any(not k.startswith("Buluşmalar") for k in kept):
                raise SystemExit(f"{images}: no image section cites {ref} in its Kaynaklar line")
        recall = V.BRIEFS[brief].get("recall_rule", False)
        desc = (IMAGES_DESC_OWN if V.BRIEFS[brief].get("own_images") else
                (IMAGES_DESC_RECALL if recall else IMAGES_DESC_SLICED) if sliced else IMAGES_DESC)
        head = head.replace(MAP_DESC, desc)
        tag = images.parent.name + ("" if labels else ".nolabel") + (".tool" if tool else "")
        swap(secs, "map.md", f"_commentary/v16/{images.relative_to(V.HERE)}"
             + (f" (only the images that cite {ref}, and ## Buluşmalar)" if sliced else ""), body)
    else:
        if not V.map_complete(map_path):
            raise SystemExit(f"{map_path}: incomplete map (no ## Chains or ## Ayat); a writer is never built on it")
        tag = map_path.parent.name.replace("surah.", "") + ("" if labels else ".nolabel") + (".tool" if tool else "")
        swap(secs, "map.md", f"_commentary/v16/{map_path.relative_to(V.HERE)} (without ## Not carried)",
             strip_not_carried(map_path.read_text(encoding="utf-8")))
    if not labels:
        d = [s for s in secs if s[0].endswith("01_dictionary.md")][0]
        d[0], d[1] = d[0] + " (without branch labels)", drop_labels(d[1])
    if tool:
        head = head.rstrip("\n") + "\n\n" + tool_line(ref, "lookup" if V.BRIEFS[brief].get("lookup_only") else "ayah")
    text = join(head, secs)
    wd = V.WORK / name / f"DM.{brief}.{tag}"
    wd.mkdir(parents=True, exist_ok=True)
    (wd / "prompt.md").write_text(text, encoding="utf-8")
    meta = {"ref": ref, "brief": brief, "map": str(map_path.relative_to(V.HERE)), "labels": labels, "tool": tool}
    if images:
        meta["images"] = str(images.relative_to(V.HERE))
        if kept is not None:
            meta["images_sections"] = kept
    json.dump({**meta, "prompt_sha256": sha(text)}, (wd / "packet.json").open("w"), indent=1)
    return text, V.OUT / name / f"DM.{brief}.{tag}", tag


def estimate(text: str, kind: str, target: str | None, model: str = "opus", check: str | None = None) -> float:
    """v16's estimate, plus (with the check) the tool result written to cache and one extra cached re-read."""
    est = V.estimate(text, "surah" if kind == "images" else kind, model)  # images: a surah-sized answer
    if target:
        _, w, _ = V.MODELS[model]
        ck = check or kind
        turns = len(check_targets(target, ck)) + LOOKUPS  # each tool turn re-reads the cached prompt
        est += tool_extra(target, ck) * w + V.est_tokens(text) * w * 0.05 * turns
    return est


def call(text: str, d: Path, kind: str, row: dict, ledger: bool, tool: bool = False, model: str = "opus",
         effort: str = "high", check: str | None = None) -> None:
    est = estimate(text, kind, (row["ref"] if tool else None), model, check)
    targets = check_targets(row["ref"], check or kind) if tool else None
    if V.blocked(d):
        raise SystemExit(f"{d}: started or finished before (never rerun)")
    if est >= V.GATE_USD:
        V.log({**row, "status": "gated", "estimate_usd": round(est, 2)})
        raise SystemExit(f"gated at ${est:.2f}")
    d.mkdir(parents=True, exist_ok=True)
    (d / "prompt.md").write_text(text, encoding="utf-8")
    t0 = time.time()
    obj = V.call_opus(text, d, model, allow=ALLOW if tool else None, effort=effort)
    out = {**row, "model": V.MODELS[model][0], "effort": effort, "seconds": round(time.time() - t0),
           "estimate_usd": round(est, 2),
           **V.usage_row(obj, text)}
    result = (obj.get("result") or "").strip()
    if result and kind == "surah":
        (d / "map.md").write_text(result + "\n", encoding="utf-8")
        out["map_complete"] = V.map_complete(d / "map.md")
    elif result and kind == "images":
        prose, sep, led = result.partition(V.LEDGER_MARK)
        out["ledger"] = bool(sep)
        if sep:
            (d / "ledger.md").write_text(led.strip() + "\n", encoding="utf-8")
        (d / "images.md").write_text(prose.strip() + "\n", encoding="utf-8")
        out["map_complete"] = images_complete(d / "images.md") and bool(sep)
        # the same verification record as a reading (sources, unsourced Arabic); the focus only sets "where" labels
        subprocess.run([sys.executable, str(V.CHECK), str(d / "images.md"), "--ref", f"{row['ref'].lstrip('S')}:1",
                        "--out", str(d / "check.json"), "--quiet"], cwd=V.CHECK.parent)
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
        bad, denied = audit(d, targets)
        out["tool_audit"] = "ok" if not bad else {"unexpected_commands": bad}
        if denied:
            out["tool_denied_not_run"] = denied
            print(f"note: {len(denied)} command(s) refused by the permission mode (not run)")
        if bad:
            print(f"WARNING: unexpected commands run by the agent, treat this run as contaminated: {bad}")
    V.log(out)
    print(f"{d.relative_to(V.HERE)}: {out['status']} ${out.get('cost_usd')} {out.get('words')}w {out['seconds']}s")
    if out["status"] != "ok" or out.get("map_complete") is False:
        raise SystemExit(f"{d.relative_to(V.HERE)}: not a clean output ({out['status']}, map_complete="
                         f"{out.get('map_complete')}); stopping so a chained call does not use it")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=("map", "writer", "images"))
    ap.add_argument("--brief")
    ap.add_argument("--ayah")
    ap.add_argument("--map", type=Path)
    ap.add_argument("--no-labels", action="store_true")
    ap.add_argument("--no-hft", action="store_true")
    ap.add_argument("--tool", action="store_true")
    ap.add_argument("--tag", default="", help="map: suffix for a new output dir (e.g. a later version of the check)")
    ap.add_argument("--model", choices=("opus", "sonnet"), default="opus", help="writer only")
    ap.add_argument("--effort", choices=("low", "medium", "high", "xhigh", "max"), default="high", help="writer only")
    ap.add_argument("--images", type=Path, help="writer: an images.md (from `images`) in place of the map")
    ap.add_argument("--surah", type=int, default=1, help="map and images: the surah (default 1)")
    ap.add_argument("--go", action="store_true")
    a = ap.parse_args()
    if a.cmd == "writer" and a.surah != 1:
        ap.error("--surah is for map and images; a writer's surah comes from --ayah")
    if a.cmd == "images":
        if not a.map or a.ayah:
            ap.error("images needs --map and takes no --ayah")
        if a.no_labels or a.no_hft or a.tag or a.images or a.model != "opus" or a.effort != "high":
            ap.error("images takes only --map, --brief, --tool and --go")
        mp = (V.HERE / a.map) if not a.map.is_absolute() else a.map
        text, d = images_packet(mp, a.brief or "images1", a.tool, a.surah)
        print(f"{d.relative_to(V.HERE)}: {len(text):,} chars; "
              f"est ${estimate(text, 'images', f'S{a.surah}' if a.tool else None):.2f} (80k out)")
        if a.go:
            call(text, d, "images", {"ref": f"S{a.surah}", "arm": "images", "brief": d.name}, True, a.tool)
        return
    if a.cmd == "map" and (a.model != "opus" or a.effort != "high"):
        ap.error("--model and --effort are for writer only")
    if a.cmd == "map":
        brief = a.brief or "map3"
        if a.tag and not re.fullmatch(r"[a-z0-9_]+", a.tag):
            ap.error("--tag: lowercase letters, digits and _ only")
        text, d = map_packet(brief, not a.no_hft, a.tool, a.tag, a.surah)
        n_out = 130_000  # r2 map measured 121.8k output; the estimate below also shows v16's standard 80k
        _, w, o = V.MODELS["opus"]
        n_in = V.est_tokens(text)
        realistic = n_in * (1 + n_out // V.MESSAGE_CAP) * w + n_out * o
        extra = estimate(text, "surah", f"S{a.surah}") - V.estimate(text, "surah") if a.tool else 0.0
        print(f"{d.relative_to(V.HERE)}: {len(text):,} chars ~{n_in:,} tokens; est ${V.estimate(text, 'surah') + extra:.2f} "
              f"(80k out), ${realistic + extra:.2f} at {n_out // 1000}k out")
        if a.go:
            call(text, d, "surah", {"ref": f"S{a.surah}", "arm": "surah", "brief": d.name.replace("surah.", "")}, False,
                 a.tool)
        return
    if a.tag:
        ap.error("--tag is for map only; a writer's dir name comes from its --map dir")
    images = ((V.HERE / a.images) if not a.images.is_absolute() else a.images) if a.images else None
    text, d, tag = writer_packet(a.ayah, a.brief, (V.HERE / a.map) if not a.map.is_absolute() else a.map,
                                 not a.no_labels, a.tool, images)
    if a.model != "opus" or a.effort != "high":  # the prompt is the same; only the output dir differs
        d, tag = d.with_name(f"{d.name}.{a.model}.{a.effort}"), f"{tag}.{a.model}.{a.effort}"
    ck = "lookup" if V.BRIEFS[a.brief].get("lookup_only") else None
    est = estimate(text, 'ayah', a.ayah if a.tool else None, a.model, ck)
    print(f"{d.relative_to(V.HERE)}: {len(text):,} chars; est ${est:.2f} ({V.MODELS[a.model][0]}, effort {a.effort})")
    if a.go:
        call(text, d, "ayah", {"ref": a.ayah, "arm": "DM", "brief": f"{a.brief}.{tag}"}, True, a.tool, a.model,
             a.effort, ck)


if __name__ == "__main__":
    main()
