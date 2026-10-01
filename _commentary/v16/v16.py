#!/usr/bin/env python3
"""v16: one permitted Opus reading per ayah on the E1 base plus assembled findings (see DESIGN.md).

Briefs:
  r1  the E1 base: v9/prompts/write_v10.md + prompts/additions.md, v9 context.md with word notes. Every run up to
      2026-09-29 used r1; its packets rebuild byte for byte (outputs in out/<S_A>/<arm>/, out/sNNN/surah/).
  r2  after REVIEW.md: prompts/r2/{write,additions,surah_map}.md, context.md without the word notes, the v16
      dictionary in every arm, the judgements clause on HFT and channel review (outputs in <arm>.r2/, surah.r2/).
  r3  cinematic scenes; memory and omissions in a separate ledger; reuses the r2 surah map.
  r4  discovery before themes; every coherent contribution develops the themes; no selection quota (default).
      Reuses the r2 surah map. GPT-6 Astra subscription runs use run_astra.py with frozen earlier evidence.

  r5  r4 plus grounding for readers unfamiliar with a contributing Quranic passage.
  r6  r5 with the filmmaker's-eye paragraph replaced by a commentator's register: no staged tableaux, images
      attributed where they enter, no aphoristic closers, no added lessons.
  r7  minimal core for Opus: task, evidence framing, guards, format and ledger; no craft instructions.
  r8  r7 plus r6's discovery paragraph (with scene-level Quran search), attribution without dictionary names,
      thesis sections and no first-person hedging.
  r9  r8 plus: every Arabic quotation in the reader tag; family images quoted in Arabic; chains judged together;
      dictionary joins explored; exclusion only after trying, never for rarity or plain-meaning mismatch, one
      ledger line per finding; end on what was established, not a summary.
  r10 r7 plus a theme-first paragraph (user, 2026-09-30): themes lead and words serve them; no family walked
      through for its own sake; family images quoted in Arabic without dictionary talk; every Arabic quotation in
      the reader tag; no first-person hedging.
  r10_1 r10 with the adversarial review's three replacements (REVIEW_r7_r10.md): judge senses by their work, not
      their branch; chains another ayah completes can found a theme, earlier chains recalled briefly; usage
      reported as "… denir", the family never a speaker; ledger states what an omission would have shown.
  r11 r10_1 with four edits (user, 2026-09-30): no "do not use tools" (the check is allowed by the packet header);
      usage in varied wording instead of the "… denir" example; a scene where two chains meet can found a theme;
      the ledger says why an omission could not found, reshape or join a theme.
  r11_1 r11 with two fixes after its 1:6 run: no recurring attribution formula ("… denir", "Araplar … derlerdi");
      a Quran passage or hadith gets its actual speaker and the exact ayah that holds the cited words.
  r12 r11_1 (and images1 for the images step) with every reader tag carrying its source (a dictionary branch as
      "root letters,branch id", a Quran ayah, "hadis" or "memory"; a passage named without quoting it gets a
      source-only tag); the ayah writer reads only the images that cite its ayah, plus ## Buluşmalar; the check
      (missing.py) gives refs only, by tier, with a text lookup, and runs per ayah in the images step.
  r13 r12_1 frozen (user, 2026-10-01, after the Opus progress review): an image the ayah's own words take part
      in is developed in the reading as far as the word carries it, the shared scene recalled in a sentence;
      no "sözlük"/map/chain talk; surah words in tags, its ayat named in words; the writer gets the dictionary
      and the sliced images (no map base) and only the `text` lookup (the list is left to augment).
  r12_1 r12 with no hadith, tafsir or outside report (a passage's situation as the Quran tells it), terse ledger
      lines, and a recalled image tied to the ayah whose words carry it, never "explained before" (images too).

Arms (the assembled-findings slot):
  H   the ayah's HFT records (v9/input/v2/…/02_hft.md) and the surah channel review's subchannels anchored in the
      ayah (latent_activation/network/v3/reviews/sNNN/reader_a_pilot.md), verbatim
  V   v5 scope prose (raw/<analysis>/sNNN/S_A/{micro,macro,global}.scope.tr.md); a lane whose gzip ratio is below
      0.2 is template-generated ledger text, not prose, and is left out
  D   no findings slot
  VD  (r1 only) V with the v16 dictionary; in r1, D/VD/DM read the v16 dictionary and H/V read v9's clipped one
  DM  D plus the surah map, written once per surah by the surah call

Surah call (`surah`): one Opus call reads the whole surah (text, v16 surah dictionary, the whole channel review,
the trimmed HFT of every ayah) and writes the map of its image chains.

Rules: one call per arm per ayah; never rerun (a started or finished call blocks any other); no retries; a call
starts only if its estimate is below $5; every call is logged in out/ledger.jsonl with its prompt hash; check.py
runs after writing and never edits the prose. Packets are built in the main thread; only the calls run in parallel.

Usage:
  python3 _commentary/v16/v16.py build [--brief r1|r2|r3|r4] [--arm X] [--ayah S:A]
  python3 _commentary/v16/v16.py run --arm X [--brief r4] [--ayah S:A] [--parallel N]
  python3 _commentary/v16/v16.py surah --surah 1 [--brief r2] [--run]
  python3 _commentary/v16/run_astra.py --ayah 1:5 --ayah 1:6 [--run]
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import uuid
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
C = REPO / "_commentary"
V9 = C / "v9"
V5 = C / "v5"
CHANNELS = REPO.parent / "latent_activation" / "network" / "v3" / "reviews"
CHECK = C / "review" / "e0" / "checks" / "check.py"
WORK = HERE / "work"
OUT = HERE / "out"
sys.path.insert(0, str(HERE))
import dictionary as D  # noqa: E402

SYSTEM = ("You are a careful scholar of Quranic Arabic and a fine Turkish prose writer. Follow the brief in the "
          "user message exactly and return only the requested output.")
AYAT = ["1:6", "100:1", "100:6"]
BRIEFS = {
    "r1": {"write": V9 / "prompts" / "write_v10.md", "add": HERE / "prompts" / "additions.md",
           "surah": HERE / "prompts" / "surah_map.md", "arms": ["H", "V", "D", "VD", "DM"]},
    "r2": {"write": HERE / "prompts" / "r2" / "write.md", "add": HERE / "prompts" / "r2" / "additions.md",
           "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"]},
    # r3 (user, 2026-09-29): cinematic prose with hooks, scenes not words, no source talk in the prose; memory and
    # what was left out go to a ledger split off after "=== LEDGER ==="; DM reads the r2 surah map.
    "r3": {"write": HERE / "prompts" / "r3" / "write.md", "add": HERE / "prompts" / "r3" / "additions.md",
           "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
           "map_from": "r2", "ledger": True},
    "r4": {"write": HERE / "prompts" / "r4" / "write.md", "add": HERE / "prompts" / "r4" / "additions.md",
           "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
           "map_from": "r2", "ledger": True},
    "r5": {"write": HERE / "prompts" / "r5" / "write.md", "add": HERE / "prompts" / "r5" / "additions.md",
           "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
           "map_from": "r2", "ledger": True},
    # r6 (user, 2026-09-30): r5 prose read as fiction; the filmmaker's-eye paragraph becomes a commentator's register.
    "r6": {"write": HERE / "prompts" / "r6" / "write.md", "add": HERE / "prompts" / "r6" / "additions.md",
           "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
           "map_from": "r2", "ledger": True},
    # r7 (user, 2026-09-30): the best synthesis came from cold Opus with minimal instructions; keep only guards.
    "r7": {"write": HERE / "prompts" / "r7" / "write.md", "add": HERE / "prompts" / "r7" / "additions.md",
           "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
           "map_from": "r2", "ledger": True},
    # r8 (user, 2026-09-30): middle brief after the 1:5 r6/r7 x Opus/Fable comparison.
    "r8": {"write": HERE / "prompts" / "r8" / "write.md", "add": HERE / "prompts" / "r8" / "additions.md",
           "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
           "map_from": "r2", "ledger": True},
    # r10_1 (2026-09-30): the adversarial review's replacements; tested only after the map3 test (REVIEW step 4).
    "r10_1": {"write": HERE / "prompts" / "r10_1" / "write.md", "add": HERE / "prompts" / "r10_1" / "additions.md",
              "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
              "map_from": "r2", "ledger": True},
    # r11 (user, 2026-09-30): r10_1 with four minimal edits after the r10_1 1:6 read against the North Star.
    "r11": {"write": HERE / "prompts" / "r11" / "write.md", "add": HERE / "prompts" / "r11" / "additions.md",
            "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
            "map_from": "r2", "ledger": True},
    # r11_1 (user, 2026-09-30): r11 plus the attribution-formula and speaker/ayah fixes.
    "r11_1": {"write": HERE / "prompts" / "r11_1" / "write.md", "add": HERE / "prompts" / "r11_1" / "additions.md",
              "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
              "map_from": "r2", "ledger": True},
    # r13 (user, 2026-10-01): r12_1 frozen with the own-images rule, style lines, lookup-only check, D base.
    "r13": {"write": HERE / "prompts" / "r13" / "write.md", "add": HERE / "prompts" / "r13" / "additions.md",
            "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
            "map_from": "r2", "ledger": True, "slice_images": True, "own_images": True, "lookup_only": True,
            "base": "D"},
    # r12_1 (user, 2026-10-01): r12 without hadith/tafsir, terse ledger, recall rule in the images description.
    "r12_1": {"write": HERE / "prompts" / "r12_1" / "write.md", "add": HERE / "prompts" / "r12_1" / "additions.md",
              "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
              "map_from": "r2", "ledger": True, "slice_images": True, "recall_rule": True},
    # r12 (user, 2026-10-01): sources inside every tag; images sliced to the ayah; refs-only check with lookup.
    "r12": {"write": HERE / "prompts" / "r12" / "write.md", "add": HERE / "prompts" / "r12" / "additions.md",
            "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
            "map_from": "r2", "ledger": True, "slice_images": True},
    # r10 (user, 2026-09-30): theme-first rewrite after r9 slid back toward a catalogue.
    "r10": {"write": HERE / "prompts" / "r10" / "write.md", "add": HERE / "prompts" / "r10" / "additions.md",
            "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
            "map_from": "r2", "ledger": True},
    # r9 (user, 2026-09-30): r8's fixes after the r8 runs on 1:5 and 1:6.
    "r9": {"write": HERE / "prompts" / "r9" / "write.md", "add": HERE / "prompts" / "r9" / "additions.md",
           "surah": HERE / "prompts" / "r2" / "surah_map.md", "arms": ["H", "V", "D", "DM"],
           "map_from": "r2", "ledger": True},
}
LEDGER_MARK = "=== LEDGER ==="
# model key -> (model id, cache-write $/token (1h = 2x input), output $/token); opus is the default and has no suffix
MODELS = {"opus": ("claude-opus-5-5", 8e-6, 20e-6), "fable": ("claude-fable-5-1", 20e-6, 50e-6),
          "sonnet": ("claude-sonnet-5-5", 4e-6, 10e-6), "solmax": ("gpt-6-sol", 0.0, 0.0)}
R1_V16_DICT = {"D", "VD", "DM"}
V5_RUN = {1: "s001-fresh-20260910", 100: "s100-regular-20260911"}
LANES = ["micro", "macro", "global"]
PROSE_MIN_GZ = 0.2  # natural prose compresses to 0.28-0.38 of its size; templated lanes to 0.06-0.09
GATE_USD = 5.0
SESSIONS = Path(tempfile.gettempdir()) / "v16_sessions"  # per-call cwd; sessions live in ~/.claude
OUT_TOKENS = {"ayah": 40_000, "surah": 80_000}  # assumed; E1-shaped calls measured 15-33k, the S1 surah call 71k
MESSAGE_CAP = 64_000  # observed per-message output cap; a longer answer continues in a new turn and re-caches

BASE_EVIDENCE = ("context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and "
                 "01_dictionary.md (every attested branch of every root of the ayah's words, with the classical "
                 "dictionaries' source phrases)")
JUDGEMENTS = ("both are earlier readers' proposals: ignore their judgements (grades, strength or confidence labels, "
              "reading types, statements of what a reading may or may not do) and make your own")
V_EVIDENCE = ("the scope notes (an earlier reader's findings: micro on the ayah's own words, macro on its surah, "
              "global on the Quran and the Fatiha; that reader had to state every limit, so its boundary sentences are "
              "its caution, not rules for you)")
ARM_EVIDENCE = {
    "r1": {"H": ("02_hft.md (earlier activation hypotheses for this ayah in its surah) and channels.md (the surah's "
                 "channel-review subchannels anchored in this ayah)"),
           "V": V_EVIDENCE, "VD": V_EVIDENCE, "D": None,
           "DM": ("surah_map.md (an earlier reader's map of the image chains that run through the whole surah, with "
                  "the dictionary phrases of their members in other ayat; a proposal, not an authority)")},
    "r2": {"H": ("02_hft.md (earlier activation hypotheses for this ayah in its surah) and channels.md (the surah's "
                 f"channel-review subchannels anchored in this ayah; {JUDGEMENTS})"),
           "V": V_EVIDENCE, "D": None,
           "DM": ("map.md (an earlier reader's map of the image chains that run through the whole surah, with the "
                  "dictionary phrases of their members in other ayat; a proposal, not an authority)")},
}
ARM_EVIDENCE["r3"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r4"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r5"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r6"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r7"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r8"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r9"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r10"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r10_1"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r11"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r11_1"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r12"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r12_1"] = ARM_EVIDENCE["r2"]
ARM_EVIDENCE["r13"] = ARM_EVIDENCE["r2"]
_SRC = None


def src() -> D.P.Sources:
    global _SRC
    if _SRC is None:
        _SRC = D.P.Sources()
    return _SRC


def rel(p: Path) -> str:
    return str(p.relative_to(REPO))


def inline(*files: Path) -> str:  # identical to v9/luna/run.py inline()
    return "\n\n".join(f"===== {rel(p)} =====\n{p.read_text(encoding='utf-8')}" for p in files)


def sa(ref: str) -> tuple[int, str]:
    s, a = ref.split(":")
    return int(s), f"{s}_{a}"


def arm_dir(root: Path, name: str, arm: str, brief: str, model: str = "opus") -> Path:
    d = arm if brief == "r1" else f"{arm}.{brief}"
    return root / name / (d if model == "opus" else f"{d}.{model}")


# ---- inputs


def anchored_refs(text: str, surah: int | None = None) -> set[str]:
    """Ayah refs in an anchor or span line: 'S:A', 'S:A-B' ranges, and bare ayah numbers or ranges that continue
    the last surah ('12:10,15', '39:2-3, 11, 14'). Backticked spans (Arabic, root letters) are ignored."""
    refs, cur = set(), surah
    for m in re.finditer(r"(?:(\d{1,3}):)?(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?", re.sub(r"`[^`]*`", " ", text)):
        s, a, b = m.group(1), int(m.group(2)), m.group(3)
        if s:
            cur = int(s)
        elif cur is None:
            continue
        for x in range(a, (int(b) if b else a) + 1):
            refs.add(f"{cur}:{x}")
    return refs


def channel_slice(ref: str, legacy: bool = False) -> str:
    """Parent headers plus every subchannel whose 'Ayah anchors' name the ayah, and every cross-pericope block whose
    pericope spans contain it, verbatim. Section headings are kept only when something follows them (legacy, as
    run under r1: every section heading kept)."""
    s, _ = sa(ref)
    src_path = CHANNELS / f"s{s:03d}" / "reader_a_pilot.md"
    blocks, cur = [], []
    for line in src_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            blocks.append(cur)
            cur = []
        cur.append(line)
    blocks.append(cur)
    out, parent, section = [], None, None
    for b in blocks:
        if not b:
            continue
        head = b[0]
        leaf = head.startswith("#### ") or re.match(r"### [SX]\d+\.", head)
        if leaf:
            key = "Pericopes" if head.startswith("### X") else "Ayah anchors"
            spans = " ".join(l for l in b if key in l)
            if ref in anchored_refs(spans):
                if section:
                    out.append(section)
                    section = None
                if parent:
                    out.append("\n".join(parent).rstrip())
                    parent = None
                out.append("\n".join(b).rstrip())
        elif head.startswith("### "):
            parent = b
        elif head.startswith("## "):
            parent, section = None, head
            if legacy:
                out.append(head)
                section = None
    text = "\n\n".join(x for x in out if x)
    return (f"# Channel review of surah {s}: subchannels anchored in {ref}\n\n"
            f"(source: {src_path.relative_to(REPO.parent)})\n\n{text}\n")


def v5_lanes(ref: str) -> list[tuple[Path, float]]:
    s, name = sa(ref)
    d = V5 / "raw" / V5_RUN[s] / f"s{s:03d}" / name
    lanes = []
    for lane in LANES:
        p = d / f"{lane}.scope.tr.md"
        b = p.read_bytes()
        lanes.append((p, len(zlib.compress(b, 9)) / len(b)))
    return lanes


def fresh_context(ref: str) -> str:
    """The same context.md for an ayah v9 never prepared (S107, 2026-10-01): the focus ayah, its anchor translation
    from the ayah bundle, its words, the Fatiha and the whole surah, built by v9's own section functions."""
    s, a = (int(x) for x in ref.split(":"))
    bundle = D.P.load_bundle(REPO / "bundles" / f"s{s:03d}" / f"{s}_{a}.ayah.json", s, a)
    head = D.P.section_ayah(src(), ref, bundle)
    fat = "# Fatiha (recited in every salah)\n" + "".join(f"- 1:{i} {src().quran[f'1:{i}']}\n" for i in range(1, 8))
    return head + "\n" + fat + "\n" + D.P.section_surah(src(), ref)


def clean_context(ref: str, path: Path) -> Path:
    """v9 context.md without its '## Word notes' section (precomputed verdicts, REVIEW.md I7); for an ayah v9 never
    prepared, the same file built fresh (fresh_context)."""
    _, name = sa(ref)
    v9 = V9 / "lines" / "work" / name / "context.md"
    t = v9.read_text(encoding="utf-8") if v9.exists() else fresh_context(ref)
    t = re.sub(r"\n## Word notes[^\n]*\n.*?(?=\n#)", "\n", t, flags=re.S)
    path.write_text(t, encoding="utf-8")
    return path


def map_complete(m: Path) -> bool:
    t = "\n" + (m.read_text(encoding="utf-8") if m.exists() else "")
    return "\n## Chains" in t and "\n## Ayat" in t


def build(ref: str, arm: str, brief: str) -> tuple[str, dict]:
    if arm not in BRIEFS[brief]["arms"]:
        raise SystemExit(f"{ref} {arm}: not an arm of brief {brief}")
    s, name = sa(ref)
    wd = arm_dir(WORK, name, arm, brief)
    wd.mkdir(parents=True, exist_ok=True)
    if brief == "r1":
        ctx = V9 / "lines" / "work" / name / "context.md"
        v16_dict = arm in R1_V16_DICT
    else:
        ctx = clean_context(ref, wd / "context.md")
        v16_dict = True
    if v16_dict:
        dic = wd / "01_dictionary.md"
        dic.write_text(D.section(src(), ref, "r1" if brief == "r1" else "r2"), encoding="utf-8")
    else:
        dic = V9 / "input" / "v2" / f"s{s:03d}" / name / "01_dictionary.md"
    meta = {"ref": ref, "arm": arm, "brief": brief}
    if arm == "H":
        ch = wd / "channels.md"
        ch.write_text(channel_slice(ref, legacy=brief == "r1"), encoding="utf-8")
        extra = [V9 / "input" / "v2" / f"s{s:03d}" / name / "02_hft.md", ch]
    elif arm == "D":
        extra = []
    elif arm == "DM":
        mb = BRIEFS[brief].get("map_from", brief)
        m = OUT / f"s{s:03d}" / ("surah" if mb == "r1" else f"surah.{mb}") / "map.md"
        if not map_complete(m):
            raise SystemExit(f"{ref} DM: no complete surah map at {rel(m)} (needs '## Chains' and '## Ayat')")
        extra = [m]
    else:
        lanes = v5_lanes(ref)
        extra = [p for p, r in lanes if r >= PROSE_MIN_GZ]
        meta["v5_lanes"] = {p.name: {"gz_ratio": round(r, 3), "kept": r >= PROSE_MIN_GZ} for p, r in lanes}
    b = BRIEFS[brief]
    ev = ARM_EVIDENCE[brief][arm]
    stdin = inline(b["write"], b["add"], ctx, dic, *extra)
    prompt = (f"Focus: {ref}. Follow the brief below (write.md) and its additions (additions.md) exactly. The "
              f"evidence is {BASE_EVIDENCE}{' and ' + ev if ev else ''} and your own "
              f"knowledge of Arabic and the Quran. "
              + ("Return the reader's prose and then the ledger, as write.md specifies." if b.get("ledger") else
                 "Return only the reader's prose as your final message."))
    text = prompt + "\n\n" + stdin
    (wd / "prompt.md").write_text(text, encoding="utf-8")
    meta["files"] = [rel(p) for p in (b["write"], b["add"], ctx, dic, *extra)]
    (wd / "packet.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return text, meta


HFT_TRACE = re.compile(r"^(\s*- )(\d+:\d+)\s+w[\d,]+\s+(\*\*.+?\*\*)\s+\((.+?)\s+(B\d+):.*?\)\s+—\s+(.*)$")
HFT_PREFIX = re.compile(r"^(?:baseline|base|ctx|context|delta|outlier|out|[bcdo]\d*)[_-]", re.I)
HFT_NOTE = ("Note: HFT used an older root map; a trace step on a root the gateway now withholds is an echo, not "
            "identity.")


def trim_hft(text: str) -> str:
    """One ayah's HFT records without judgements: the record name without its class prefix and [label], the
    changed reading, the mechanism, and each trace step as ayah, word, branch and contribution (the dictionary
    carries the branch glosses). Drops `before`, `containment` and the reader overview."""
    out, keep = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            keep = not line.startswith("## HFT reader overview")
            if keep:
                name = HFT_PREFIX.sub("", re.sub(r"\s*\[[^\]]*\]\s*$", "", line[3:]))
                name = re.sub(r"^(?:\d+[_-])+", "", name)
                out += ["", "## " + re.sub(r"[_-]", " ", name).lower()]
            continue
        if not keep:
            continue
        if line.startswith("- after:"):
            reading = re.sub(r"^Exploratorily,\s*", "", line[len("- after:"):].strip())
            out.append("- reading: " + reading[:1].upper() + reading[1:])
        elif line.startswith(("- mechanism:", "- trace:")):
            out.append(line)
        elif line.startswith("  - "):
            m = HFT_TRACE.match(line)
            out.append(f"{m[1]}{m[2]} {m[3]} {m[4]} {m[5]}: {m[6]}" if m else line)
    return "\n".join(out).strip() + "\n"


def surah_build(s: int, brief: str) -> tuple[str, Path]:
    refs = []
    while f"{s}:{len(refs) + 1}" in src().quran:
        refs.append(f"{s}:{len(refs) + 1}")
    wd = WORK / f"s{s:03d}" / ("surah" if brief == "r1" else f"surah.{brief}")
    wd.mkdir(parents=True, exist_ok=True)
    text = wd / "text.md"
    text.write_text(f"# Surah {s}\n\n" + "\n".join(f"- {r} {src().quran[r]}" for r in refs) + "\n", encoding="utf-8")
    dic = wd / "dictionary.md"
    dic.write_text(D.surah_section(src(), refs, "r1" if brief == "r1" else "r2"), encoding="utf-8")
    hft = wd / "hft.md"
    parts = [f"# HFT: earlier activation hypotheses, per focus ayah of surah {s}"]
    if brief != "r1":
        parts.append("\n" + HFT_NOTE)
    for r in refs:  # an ayah without v9 HFT gets a stated gap (a nohft map drops this file anyway)
        f = V9 / "input" / "v2" / f"s{s:03d}" / r.replace(":", "_") / "02_hft.md"
        parts.append(f"\n# Focus {r}\n\n" + (trim_hft(f.read_text(encoding="utf-8")) if f.exists() else
                                                "(no HFT records for this ayah)\n"))
    hft.write_text("\n".join(parts), encoding="utf-8")
    ch_src = CHANNELS / f"s{s:03d}" / "reader_a_pilot.md"
    ch = wd / "channels.md"
    ch.write_text(f"(source: {ch_src.relative_to(REPO.parent)})\n\n" + ch_src.read_text(encoding="utf-8"),
                  encoding="utf-8")
    if brief == "r1":
        prompt = (f"Surah: {s}. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), "
                  f"dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own "
                  f"phrases), hft.md and channels.md ({JUDGEMENTS}) and your own knowledge of Arabic and the Quran. "
                  f"Return only the map as your final message.")
        files = (BRIEFS[brief]["surah"], text, dic, hft, ch)
    else:
        prompt = (f"Surah: {s}. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), "
                  f"dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own "
                  f"phrases), channels.md and hft.md ({JUDGEMENTS}) and your own knowledge of Arabic and the Quran. "
                  f"Return only the map as your final message.")
        files = (BRIEFS[brief]["surah"], text, dic, ch, hft)
    full = prompt + "\n\n" + inline(*files)
    (wd / "prompt.md").write_text(full, encoding="utf-8")
    return full, wd


# ---- calls


def est_tokens(text: str) -> int:  # the cost critic's calibrated formula, as in E1
    ar = len(re.findall(r"[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]", text))
    return int(4581 + 1.151 * ar + 0.366 * (len(text) - ar))


def estimate(text: str, kind: str = "ayah", model: str = "opus") -> float:
    """Opus measured: cache write $8/M, output $20/M; Fable 2.5x. Output past a message cap re-caches the prompt."""
    n_in, n_out = est_tokens(text), OUT_TOKENS[kind]
    _, w, o = MODELS[model]
    return (n_in * (1 + n_out // MESSAGE_CAP)) * w + n_out * o


_CLI = None


def cli_version() -> str:
    global _CLI
    if _CLI is None:
        p = subprocess.run(["claude", "--version"], capture_output=True, text=True)
        _CLI = (p.stdout or p.stderr).strip()
    return _CLI


def log(row: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "ledger.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def blocked(d: Path) -> bool:
    """Never rerun: a finished call (run.log.json) or a started one (started.json) blocks any other."""
    return (d / "run.log.json").exists() or (d / "started.json").exists()


def call_solmax(text: str, d: Path) -> dict:
    """Run GPT-6 Sol at max reasoning through the Codex subscription, isolated and read-only."""
    (d / "started.json").write_text(json.dumps({"started": time.strftime("%Y-%m-%dT%H:%M:%S"),
                                                 "prompt_sha256": hashlib.sha256(text.encode()).hexdigest()}) + "\n",
                                    encoding="utf-8")
    cmd = ["codex", "exec", "-m", "gpt-6-sol", "-c", 'model_reasoning_effort="max"',
           "--disable", "skill_search", "--skip-git-repo-check", "--ephemeral", "-s", "read-only", "--json"]
    with tempfile.TemporaryDirectory(prefix="v16_solmax_") as cwd:
        last = Path(cwd) / "last.txt"
        p = subprocess.run(cmd + ["-o", str(last), "-C", cwd, "-"], input=text,
                           capture_output=True, text=True, timeout=5400)
        result = last.read_text(encoding="utf-8") if last.exists() else ""
    (d / "run.stream.jsonl").write_text(p.stdout or "", encoding="utf-8")
    obj = {"result": result, "returncode": p.returncode, "stderr": (p.stderr or "")[-3000:],
           "words": len(result.split()) if result else 0, "prompt_chars": len(text),
           "prompt_sha256": hashlib.sha256(text.encode()).hexdigest(), "cli": "codex"}
    (d / "run.log.json").write_text(json.dumps(obj, ensure_ascii=False) + "\n", encoding="utf-8")
    return obj

def call_opus(text: str, d: Path, model: str = "opus", allow: str | None = None, effort: str = "high") -> dict:
    """One Opus call. stream-json keeps every assistant message: a long answer that the CLI splits over several
    turns is joined back in order (`--output-format json` returns only the last message; the first S1 surah call
    lost two thirds of its map that way). The raw event stream is kept in run.stream.jsonl. If the stream ends
    without a result event, the text received is still returned, marked partial."""
    # Sessions are kept (user, 2026-09-30) so that resume.py can ask diagnostic follow-ups in the same session; each
    # call gets its own id and a working directory of its own that outlives the call (the CLI files a session under
    # its cwd, and missing.py's once-only marker lives there too).
    sid = str(uuid.uuid4())
    cwd = SESSIONS / sid
    cwd.mkdir(parents=True, exist_ok=False)
    (d / "started.json").write_text(json.dumps({"started": time.strftime("%Y-%m-%dT%H:%M:%S"),
                                                "prompt_sha256": hashlib.sha256(text.encode()).hexdigest(),
                                                "model": MODELS[model][0], "effort": effort, "session_id": sid,
                                                "session_cwd": str(cwd)}) + "\n",
                                    encoding="utf-8")
    # allow: one Bash command prefix the model may run (the end-of-discovery check, missing.py); every other
    # command is refused by --permission-mode dontAsk, and no other tool exists.
    tools = ["--tools", "Bash", "--allowedTools", f"Bash({allow} *)"] if allow else ["--tools", ""]
    cmd = ["claude", "-p", "--model", MODELS[model][0], "--effort", effort, *tools,
           "--output-format", "stream-json", "--verbose", "--session-id", sid, "--safe-mode",
           "--permission-mode", "dontAsk", "--system-prompt", SYSTEM]
    env = {**os.environ, "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "128000"}
    p = subprocess.run(cmd, input=text, capture_output=True, text=True, cwd=cwd, env=env)
    (d / "run.stream.jsonl").write_text(p.stdout or "", encoding="utf-8")
    texts, ids, final, tool_calls, pre_tool, pre_ids, safety = [], [], {}, [], [], [], []
    for line in (p.stdout or "").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        # The model's safeguards can stop a response; the CLI then continues once and the model may write a note in
        # place of the rest (S1 map3.nohft.tool.check2, 2026-09-30). The run is then not a clean output.
        if ev.get("type") == "system" and "safeguards" in str(ev.get("content", "")):
            safety.append(str(ev.get("content")))
        if ev.get("type") == "assistant" and isinstance(ev.get("message"), dict):
            msg = ev["message"]
            for c in msg.get("content", []):  # in order: the output is the text after the last tool call
                if c.get("type") == "tool_use":
                    tool_calls.append({"id": c.get("id"), "input": c.get("input")})
                    if texts:
                        pre_tool, pre_ids = texts, ids  # kept as a fallback if nothing follows the last tool call
                    texts, ids = [], []
                elif c.get("type") == "text":
                    texts.append(c.get("text", ""))
                    if msg.get("id") not in ids:
                        ids.append(msg.get("id"))
        elif ev.get("type") == "user" and isinstance(ev.get("message"), dict):
            for c in ev["message"].get("content", []) or []:
                if isinstance(c, dict) and c.get("type") == "tool_result" and tool_calls:
                    res = c.get("content")
                    if isinstance(res, list):
                        res = "".join(b.get("text", "") for b in res if isinstance(b, dict))
                    call = next((x for x in tool_calls if x.get("id") == c.get("tool_use_id")), tool_calls[-1])
                    call["result"], call["is_error"] = res, c.get("is_error", False)
        elif ev.get("type") == "result":
            final = ev
    if tool_calls:
        (d / "tool_calls.json").write_text(json.dumps(tool_calls, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    joined = "".join(texts)
    if not joined and pre_tool:
        joined, ids = "".join(pre_tool), pre_ids
    had_result = bool(final)
    if final:
        final["result_last_message"] = final.get("result")
        final["result"] = joined or final.get("result")
    elif joined:
        final = {"result": joined, "partial": True, "is_error": True, "stderr_tail": p.stderr[-3000:]}
    if not final:
        final = {"error": p.stderr[-3000:]}
    elif not had_result:
        final.setdefault("stderr_tail", p.stderr[-3000:])
    final["text_message_ids"] = ids
    final["session_id"], final["session_cwd"] = sid, str(cwd)
    final["tool_calls"] = len(tool_calls)
    if safety:
        final["safety_stop"] = safety
    (d / "run.log.json").write_text(json.dumps(final, ensure_ascii=False) + "\n",
                                    encoding="utf-8")
    return final


def usage_row(obj: dict, text: str) -> dict:
    usage = obj.get("usage", {}) or {}
    result = (obj.get("result") or "").strip()
    return {"status": "safety-stop" if obj.get("safety_stop") else "partial" if obj.get("partial")
            else ("ok" if result and not obj.get("is_error") else "error"),
            "cost_usd": obj.get("total_cost_usd"), "output_tokens": usage.get("output_tokens"),
            "thinking_tokens": (usage.get("output_tokens_details") or {}).get("thinking_tokens"),
            "cache_write": usage.get("cache_creation_input_tokens"), "num_turns": obj.get("num_turns"),
            "text_messages": len(obj.get("text_message_ids") or []), "tool_calls": obj.get("tool_calls", 0),
            "words": len(result.split()) if result else 0, "prompt_chars": len(text),
            "prompt_sha256": hashlib.sha256(text.encode()).hexdigest(), "cli": cli_version()}


def run_one(ref: str, arm: str, brief: str, text: str, est: float, model: str = "opus") -> str:
    _, name = sa(ref)
    d = arm_dir(OUT, name, arm, brief, model)
    tag = f"{ref} {arm} {brief} {model}"
    d.mkdir(parents=True, exist_ok=True)
    (d / "prompt.md").write_text(text, encoding="utf-8")
    t0 = time.time()
    obj = call_solmax(text, d) if model == "solmax" else call_opus(text, d, model)
    row = {"ref": ref, "arm": arm, "brief": brief, "model": MODELS[model][0], "seconds": round(time.time() - t0),
           "estimate_usd": round(est, 2),
           **usage_row(obj, text)}
    result = (obj.get("result") or "").strip()
    if result and BRIEFS[brief].get("ledger"):
        prose, sep, ledger = result.partition(LEDGER_MARK)
        row["ledger"] = bool(sep)
        if sep:
            (d / "ledger.md").write_text(ledger.strip() + "\n", encoding="utf-8")
            result = prose.strip()
    if result:
        reading = d / f"{name}.reading.tr.md"
        reading.write_text(result + "\n", encoding="utf-8")
        subprocess.run([sys.executable, str(CHECK), str(reading), "--ref", ref, "--out", str(d / "check.json"),
                        "--quiet"], cwd=CHECK.parent)
    log(row)
    return f"{tag}: {row['status']} ${row['cost_usd']} {row['words']}w {row['seconds']}s"


def surah_run(s: int, brief: str) -> str:
    d = OUT / f"s{s:03d}" / ("surah" if brief == "r1" else f"surah.{brief}")
    if blocked(d):
        return f"S{s} surah {brief}: started or finished before, skipped (never rerun)"
    text, _ = surah_build(s, brief)
    est = estimate(text, "surah")
    if est >= GATE_USD:
        log({"ref": f"S{s}", "arm": "surah", "brief": brief, "status": "gated", "estimate_usd": round(est, 2)})
        return f"S{s} surah {brief}: gated at ${est:.2f}"
    d.mkdir(parents=True, exist_ok=True)
    (d / "prompt.md").write_text(text, encoding="utf-8")
    t0 = time.time()
    obj = call_opus(text, d)
    row = {"ref": f"S{s}", "arm": "surah", "brief": brief, "seconds": round(time.time() - t0),
           "estimate_usd": round(est, 2), **usage_row(obj, text)}
    result = (obj.get("result") or "").strip()
    if result:
        (d / "map.md").write_text(result + "\n", encoding="utf-8")
        row["map_complete"] = map_complete(d / "map.md")
    log(row)
    return f"S{s} surah {brief}: {row['status']} ${row['cost_usd']} {row['words']}w {row['seconds']}s"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=("build", "run", "surah"))
    ap.add_argument("--brief", choices=tuple(BRIEFS), default="r4")
    ap.add_argument("--arm")
    ap.add_argument("--ayah")
    ap.add_argument("--surah", type=int)
    ap.add_argument("--run", action="store_true", help="surah: make the call (default: build and estimate)")
    ap.add_argument("--parallel", type=int, default=3)
    ap.add_argument("--model", choices=tuple(MODELS), default="opus")
    a = ap.parse_args()
    if a.cmd == "surah":
        if not a.surah:
            ap.error("surah needs --surah N")
        if a.run:
            print(surah_run(a.surah, a.brief))
            return
        full, wd = surah_build(a.surah, a.brief)
        for f in ("text.md", "dictionary.md", "channels.md", "hft.md"):
            print(f"  {f:14} {len((wd / f).read_text(encoding='utf-8')):>8,} chars")
        e = estimate(full, "surah")
        print(f"S{a.surah} surah {a.brief}: {len(full):,} chars ~{est_tokens(full):,} tokens  est ${e:.2f}"
              f"  ({'ok' if e < GATE_USD else 'BLOCK'})")
        return
    arms = BRIEFS[a.brief]["arms"]
    if a.arm and a.arm not in arms:
        ap.error(f"arm {a.arm} is not in brief {a.brief}: {arms}")
    if a.cmd == "run" and not a.arm:
        ap.error("run needs --arm (each arm is approved separately)")
    jobs = [(r, k) for r in ([a.ayah] if a.ayah else AYAT) for k in ([a.arm] if a.arm else arms)]
    built = []
    for r, k in jobs:  # main thread: Sources' SQLite connections belong to the thread that opened them
        if a.cmd == "run" and blocked(arm_dir(OUT, sa(r)[1], k, a.brief, a.model)):
            print(f"{r} {k} {a.brief}: started or finished before, skipped (never rerun)")
            continue
        try:
            t, meta = build(r, k, a.brief)
        except SystemExit as e:
            print(f"{r:6} {k}  skipped: {e}")
            continue
        e = estimate(t, "ayah", a.model)
        lanes = ""
        if "v5_lanes" in meta:
            lanes = "  v5: " + ", ".join(f"{n.split('.')[0]} {v['gz_ratio']}{'' if v['kept'] else ' (out)'}"
                                         for n, v in meta["v5_lanes"].items())
        print(f"{r:6} {k} {a.brief}  {len(t):>8,} chars ~{est_tokens(t):>7,} tokens  est ${e:.2f}"
              f"  ({'ok' if e < GATE_USD else 'BLOCK'}){lanes}")
        if e >= GATE_USD:
            if a.cmd == "run":
                log({"ref": r, "arm": k, "brief": a.brief, "status": "gated", "estimate_usd": round(e, 2)})
            continue
        built.append((r, k, t, e))
    if a.cmd == "build":
        print(f"total for {len(built)} calls: ${sum(x[3] for x in built):.2f} "
              f"(assumes {OUT_TOKENS['ayah']:,} output tokens each)")
        return
    with cf.ThreadPoolExecutor(a.parallel) as ex:
        for msg in ex.map(lambda j: run_one(j[0], j[1], a.brief, j[2], j[3], a.model), built):
            print(msg, flush=True)


if __name__ == "__main__":
    sys.exit(main())
