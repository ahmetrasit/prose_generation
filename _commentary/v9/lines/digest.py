#!/usr/bin/env python3
"""Script-only Quranic reach for the writer (no model): lines/work/S_A/digest.md

  1  variant readings of the ayah (study/_project_corpus/qiraat.tsv)
  2  usage digest: every root of the ayah with its occurrences (ref + the word as it occurs), same form and other
     forms, from the usage worklists (candidates.py); the ayat texts are left out (the writer recalls them, and
     every Quran quotation is checked against the canonical text afterwards)
  3  related passages: the reciprocal inter-ayah targets (input/v2/…/09_inter_ayah.md) — formula groups with their
     shared roots, then single targets — as refs with the opening words of each ayah; earlier review labels are
     left out (they are hints at best and have suppressed good links before)

This is the candidate set the Luna usage and related lines judge; the writer gets it unjudged.
Usage: python3 _commentary/v9/lines/digest.py 4:34
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
QIRAAT = Path("/Volumes/OZTURK/_projects/study/_project_corpus/qiraat.tsv")
OPENING = 60  # characters of each related ayah's text


def variants(ref: str) -> list[str]:
    if not QIRAAT.exists():
        return ["(no qirāʾāt source found)"]
    out = []
    with QIRAAT.open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["tsv_word_ref"].rsplit(":", 1)[0] == ref:
                out.append(f"- word {r['tsv_word_ref'].rsplit(':', 1)[1]} · {r['qiraat_arabic']} ({r['qiraat_transliteration']}) · "
                           f"{r['qiraat_reader_set']} · {r['qiraat_note'].strip()}")
    return out or ["(none recorded)"]


def usage(w: Path) -> list[str]:
    out = []
    for f in sorted(w.glob("usage_*.md")):
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.startswith("### "):
                out += ["", line]
            elif re.match(r"\s*- tier|\s*- other forms|\s*- [a-z].*:\s*\d", line) and "|" not in line:
                out.append(line.rstrip())
            elif "|" in line and re.match(r"\s*- \d{1,3}:\d{1,3}", line):
                out.append(line.split("|")[0].rstrip())
            elif line.strip().startswith("-") and "|" not in line and len(line) < 300:
                out.append(line.rstrip())
    return out


def related(pkg: Path) -> list[str]:
    f = pkg / "09_inter_ayah.md"
    if not f.exists():
        return ["(no inter-ayah list)"]
    out = []
    for line in f.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Formula group"):
            out += ["", "#" + line.split(" — ")[0].replace("## ", "## ", 1)]
        elif line.startswith("## ") and re.search(r"\d+:\d+", line) and not out[-1:] == ["", "## Single targets"]:
            if not any(x == "## Single targets" for x in out):
                out += ["", "## Single targets"]
        m = re.match(r"\s*- \*\*(\d{1,3}:\d{1,3})\*\* (.*)$", line)
        if m:
            out.append(f"- {m.group(1)} {m.group(2)[:OPENING]}…")
    return out


def main() -> None:
    ref = sys.argv[1]
    s, a = ref.split(":")
    sa = f"{s}_{a}"
    w = V9 / "lines" / "work" / sa
    pkg = V9 / "input" / "v2" / f"s{int(s):03d}" / sa
    L = [f"# Quranic reach for {ref} (script digest, unjudged)", "",
         "Candidates for reading the ayah through the Quran itself. Nothing here is a finding yet: judge each one.", "",
         "## 1. Variant readings (qirāʾāt)", ""] + variants(ref) + \
        ["", "## 2. Usage: each root of the ayah across the Quran (ref and the word as it occurs)"] + usage(w) + \
        ["", "## 3. Related passages (reciprocal inter-ayah candidates; opening words only)"] + related(pkg)
    (w / "digest.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"digest: {w / 'digest.md'} ({len(chr(10).join(L).encode()):,} bytes)")


if __name__ == "__main__":
    main()
