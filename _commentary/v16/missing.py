#!/usr/bin/env python3
"""End-of-discovery passage check, run once by the writing agent itself (user design, 2026-09-30).

The agent passes the Quran refs it will use; the script returns the reciprocal inter-ayah list's cross-surah passages
that are not among them, each with its canonical Arabic (no list notes, no labels), plus a short instruction. An
ayah gets its strong and medium passages, strong first: the medium tier holds some of the closest passages (1:6:
38:22 «واهدنا إلى سواء الصراط», 20:135, 90:10; user, 2026-09-30). A surah (the map call) gets strong only: its
medium union is 424 more refs, which it could only see as bare numbers. The full list never enters the agent's
context. The agent judges and adds only what supports its output.

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
# Claude Code shows a tool output above roughly 30-40 KB (bytes, not characters) only as a 2 KB preview plus a file
# path the agent cannot open: the S1 map run's answer (24,514 characters, 44,228 bytes) was cut to a preview
# (2026-09-30), although the documented BASH_MAX_OUTPUT_LENGTH default is 30,000 characters, so that setting cannot
# be relied on. 11.7 KB passed whole. The answer is therefore built within LIMIT_BYTES: the first passages in list
# order with their full Arabic, the rest as refs only, by surah; if even the refs do not fit, the first of them with
# an explicit count of the rest. Opening words were dropped: the part that makes a passage relevant is often at the
# end (38:22 opens «إذ دخلوا على داوود»).
LIMIT_BYTES = 20_000
LABELS = {"ayah": ("strong", "medium"), "surah": ("strong",)}


def size(s: str) -> int:
    return len(s.encode("utf-8"))


def refs_only(rs: list[str]) -> str:
    by: dict[str, list[str]] = {}
    for r in rs:
        s, a = r.split(":")
        by.setdefault(s, []).append(a)
    return "\n".join(f"- {s}: {', '.join(a)}" for s, a in by.items())


def render(missing: list[str], text: dict[str, str]) -> str:
    """The passage block within LIMIT_BYTES (the instruction is added by the caller and counted in the budget)."""
    budget = LIMIT_BYTES - size(INSTRUCTION) - 200
    lines = [f"- ({r}) {text.get(r, '')}" for r in missing]
    k, used = 0, 0
    while k < len(missing) and used + size(lines[k]) + 1 + size(refs_only(missing[k + 1:])) <= budget - 120:
        used += size(lines[k]) + 1
        k += 1
    if k == len(missing):
        return f"{len(missing)} passages:\n" + "\n".join(lines)
    if k:
        return (f"{len(missing)} passages, in list order; the first {k} with their text, the other {len(missing) - k} "
                f"as refs only, by surah:\n" + "\n".join(lines[:k]) + "\n" + refs_only(missing[k:]))
    if size(refs_only(missing)) <= budget:
        return f"{len(missing)} passages (refs only, by surah, most widely listed first):\n{refs_only(missing)}"
    n = len(missing)
    while n > 1 and size(refs_only(missing[:n])) > budget - 120:
        n = int(n * 0.9)
    assert budget > 0 and size(refs_only(missing[:n])) <= budget, "LIMIT_BYTES too small for INSTRUCTION"
    return (f"{len(missing)} passages; the {n} most widely listed are shown (refs only, by surah), "
            f"{len(missing) - n} more are not shown:\n{refs_only(missing[:n])}")


INSTRUCTION = (
    "These passages from an earlier cross-reference list are not among the refs you gave. The list is not "
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


def listed(focus_refs: list[str], labels: tuple[str, ...]) -> tuple[list[str], int]:
    """Targets with one of `labels`, by best label (in `labels` order), then most widely listed, then list order; and
    how many focus lists were found (0 means the check could not run). For one ayah the count is almost always 1
    (22 lists repeat a target), so within a label list order is nearly always kept."""
    seen, out, found, count, tier = set(), [], 0, {}, {}
    for ref in focus_refs:
        path = LISTS / f"focus_{ref.replace(':', '_')}_cutoff_100.tsv"
        if not path.exists():
            continue
        found += 1
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                # the list's own focus-side judgement: a directional review labelled strong for this focus
                if (row["record_type"] != "directional_review" or row["relation_scope"] != "cross_surah"
                        or row["focus_direction_label"] not in labels):
                    continue
                t = row["target_ref"].strip()
                if re.fullmatch(r"\d+:\d+", t):
                    count[t] = count.get(t, 0) + 1
                    tier[t] = min(tier.get(t, len(labels)), labels.index(row["focus_direction_label"]))
                    if t not in seen:
                        seen.add(t)
                        out.append(t)
    order = {r: i for i, r in enumerate(out)}
    return sorted(out, key=lambda r: (tier[r], -count[r], order[r])), found


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
    passages, found = listed(focus, LABELS["surah" if target.startswith("S") else "ayah"])
    if not found:
        answer = (f"No cross-reference list exists for {target}, so this check could not run. Add any passage you "
                  f"recall that belongs, then write your final output now.")
    else:
        used = expand(sys.argv[2:])
        missing = [r for r in passages if r not in used]
        if missing:
            answer = render(missing, text) + "\n\n" + INSTRUCTION
        else:
            answer = ("Every passage of the earlier cross-reference list is already among your refs. The list "
                      "is not authoritative and may be incomplete: add any other passage you now recall that "
                      "belongs, then write your final output now. This check runs once.")
    MARK.write_text("used\n")  # only after the answer is ready, so a failure does not burn the one check
    print(answer)


if __name__ == "__main__":
    main()
