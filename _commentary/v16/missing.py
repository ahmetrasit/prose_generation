#!/usr/bin/env python3
"""End-of-discovery passage check, run once by the writing agent itself (user design, 2026-09-30).

The agent passes the Quran refs it will use; the script returns the strong cross-surah passages of the reciprocal
inter-ayah list that are not among them, each with its canonical Arabic (no list notes), plus a short instruction.
The full list never enters the agent's context. The agent judges and adds only what supports its output.

  python3 missing.py 1:6 6:153 36:60-62 20:10 ...     # an ayah's list
  python3 missing.py S1 6:153 7:57 ...                 # union of the surah's ayat (the map call)

It answers once per working directory; a second call is refused.
"""
import csv
import re
import sys
from pathlib import Path

QD = Path("/Volumes/OZTURK/_projects/quran-data/data")
LISTS = QD / "analysis" / "inter-ayah" / "reciprocal"
TEXT = QD / "text" / "quran-uthmani.tsv"
MARK = Path(".missing_py_used")
INSTRUCTION = (
    "These strong passages from an earlier cross-reference list are not among the refs you gave. The list is not "
    "authoritative and may be incomplete. Judge each passage yourself: add it only where it supports or sharpens "
    "what you are writing, and leave the rest. Also add any other passage you now recall that belongs, whether "
    "listed here or not. This check runs once; write your final output now.")


def verses() -> dict[str, str]:
    out = {}
    with TEXT.open(encoding="utf-8-sig") as f:
        for line in f:
            ref, _, txt = line.rstrip("\n").partition("|")
            if txt:
                out[ref] = txt.lstrip("﻿")
    return out


def expand(tokens: list[str]) -> set[str]:
    """Refs as written anywhere in the args: 6:153, (2:255), 36:60-62, 36:60–62, 7:11-7:12, 28:21–24."""
    used = set()
    for m in re.finditer(r"(\d+):(\d+)(?:\s*[-–—]\s*(?:(\d+):)?(\d+))?", " ".join(tokens)):
        s, a, s2, b = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
        if b and (s2 is None or int(s2) == s) and int(b) >= a:
            used.update(f"{s}:{v}" for v in range(a, int(b) + 1))
        else:  # a single ref, a cross-surah range or a reversed range: keep both endpoints
            used.add(f"{s}:{a}")
            if b:
                used.add(f"{int(s2) if s2 else s}:{int(b)}")
    return used


def strong(focus_refs: list[str]) -> tuple[list[str], int]:
    """Strong targets in list order, and how many focus lists were found (0 means the check could not run)."""
    seen, out, found = set(), [], 0
    for ref in focus_refs:
        path = LISTS / f"focus_{ref.replace(':', '_')}_cutoff_100.tsv"
        if not path.exists():
            continue
        found += 1
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                # the list's own focus-side judgement: a directional review labelled strong for this focus
                if (row["record_type"] != "directional_review" or row["relation_scope"] != "cross_surah"
                        or row["focus_direction_label"] != "strong"):
                    continue
                t = row["target_ref"].strip()
                if re.fullmatch(r"\d+:\d+", t) and t not in seen:
                    seen.add(t)
                    out.append(t)
    return out, found


def main() -> None:
    if len(sys.argv) < 2 or not re.fullmatch(r"S\d+|\d+:\d+", sys.argv[1]):
        sys.exit("usage: missing.py <S_A or S<surah>> <refs you will use ...>")
    if MARK.exists():
        print("This check has already run once. Write your final output now.")
        return
    target, text = sys.argv[1], verses()
    if target.startswith("S"):
        s = target[1:]
        focus = sorted((r for r in text if r.split(":")[0] == s and r.split(":")[1] != "0"),
                       key=lambda r: int(r.split(":")[1]))
    else:
        focus = [target]
    listed, found = strong(focus)
    if not found:
        answer = (f"No cross-reference list exists for {target}, so this check could not run. Add any passage you "
                  f"recall that belongs, then write your final output now.")
    else:
        used = expand(sys.argv[2:])
        missing = [r for r in listed if r not in used]
        if missing:
            answer = "\n".join([f"{len(missing)} passages:", *(f"- ({r}) {text.get(r, '')}" for r in missing), "",
                                INSTRUCTION])
        else:
            answer = ("Every strong passage of the earlier cross-reference list is already among your refs. The list "
                      "is not authoritative and may be incomplete: add any other passage you now recall that "
                      "belongs, then write your final output now. This check runs once.")
    MARK.write_text("used\n")  # only after the answer is ready, so a failure does not burn the one check
    print(answer)


if __name__ == "__main__":
    main()
