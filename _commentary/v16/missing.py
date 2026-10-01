#!/usr/bin/env python3
"""End-of-discovery passage check, run by the writing agent itself (user design, 2026-09-30; r12 form 2026-10-01).

The agent passes the Quran refs it will use; the script returns the cross-surah passages of the earlier inter-ayah
list (quran-data analysis/inter-ayah/reciprocal) that are not among them, as refs only, grouped by tier:
  strong, medium, weak       this ayah's own review of the target (directional_review, focus-side label)
  named by the other side    the target's own list names this ayah (reciprocal_nomination, labelled by that list)
"no value" rows, counterevidence and same-surah rows are left out. A ref sits in its best tier only. The map call
(S<n>) gets only the strong tier of every ayah's own list, as before. The agent can read any passage's Arabic with
the `text` subcommand, as often as it needs; the list itself is answered once per ayah (or surah) and directory.
The full list never enters the agent's context. The agent judges and adds only what supports its output.

  python3 missing.py 1:6 6:153 36:60-62 20:10 ...     # an ayah's list (once per ayah: the images step runs it per ayah)
  python3 missing.py S1 6:153 7:57 ...                 # union of the surah's ayat, strong only (the map call)
  python3 missing.py text 72:16 41:17 36:60-62         # the Arabic of up to 40 verses
"""
import csv
import re
import sys
from pathlib import Path

QD = Path("/Volumes/OZTURK/_projects/quran-data/data")
LISTS = QD / "analysis" / "inter-ayah" / "reciprocal"
TEXT = QD / "text" / "quran-uthmani.tsv"
SELF = Path(__file__).resolve()
# Claude Code shows a tool output above roughly 30-40 KB (bytes) only as a 2 KB preview plus a path the agent cannot
# open (S1 map run, 2026-09-30). Refs only stay far below this; the limit guards the worst case.
LIMIT_BYTES = 20_000
TEXT_MAX = 40
# (record_type, label column, label) -> tier, best first. Ayah: every tier; surah (map call): strong only.
TIERS = [
    ("strong", "directional_review", "focus_direction_label", "strong",
     "strong (this ayah's own list)"),
    ("medium", "directional_review", "focus_direction_label", "medium",
     "medium (this ayah's own list)"),
    ("other_strong", "reciprocal_nomination", "source_direction_label", "strong",
     "named by the passage's own list as strong for this ayah"),
    ("other_medium", "reciprocal_nomination", "source_direction_label", "medium",
     "named by the passage's own list as medium for this ayah"),
    ("weak", "directional_review", "focus_direction_label", "weak",
     "weak (this ayah's own list)"),
    ("other_weak", "reciprocal_nomination", "source_direction_label", "weak",
     "named by the passage's own list as weak for this ayah"),
]
SURAH_TIERS = ("strong",)


def size(s: str) -> int:
    return len(s.encode("utf-8"))


def refs_only(rs: list[str]) -> str:
    """Refs by surah, in Quran order (a cut keeps the best-ranked refs; only the display is sorted)."""
    by: dict[str, list[str]] = {}
    for r in sorted(rs, key=lambda r: tuple(map(int, r.split(":")))):
        s, a = r.split(":")
        by.setdefault(s, []).append(a)
    return "\n".join(f"- {s}: {', '.join(a)}" for s, a in by.items())


def instruction() -> str:
    return ("These refs from an earlier cross-reference list are not among the refs you gave. The list is not "
            "authoritative and may be incomplete; a weak tier is the list's own doubt. Judge each passage yourself: "
            "add it only where it supports or sharpens what you are writing, and leave the rest. To read a "
            f"passage's text first, run `python3 {SELF} text <refs>` (up to {TEXT_MAX} refs per call), as often as "
            "you need. Also add any other passage you now recall that belongs, whether listed here or not. This "
            "list is given once; write your final output when you are done.")


def render(groups: list[tuple[str, list[str]]]) -> str:
    """The tiers within LIMIT_BYTES: lower tiers are cut first, with an explicit count of what is not shown."""
    budget = LIMIT_BYTES - size(instruction()) - 300
    total = sum(len(rs) for _, rs in groups)
    blocks, used, cut = [], 0, 0
    for label, rs in groups:
        block = f"{label} ({len(rs)}):\n{refs_only(rs)}"
        if used + size(block) + 2 <= budget:
            blocks.append(block)
            used += size(block) + 2
            continue
        n = len(rs)  # part of this tier, then nothing more
        while n > 0 and used + size(f"{label} (first {n} of {len(rs)}):\n{refs_only(rs[:n])}") + 2 > budget:
            n = int(n * 0.9) if n > 10 else n - 1
        if n:
            blocks.append(f"{label} (first {n} of {len(rs)}):\n{refs_only(rs[:n])}")
            used = budget
        cut += len(rs) - n
    head = f"{total} passages, refs only, by tier and surah" + (f"; {cut} more not shown (list too long)" if cut else "")
    return head + ":\n\n" + "\n\n".join(blocks)


def verses() -> dict[str, str]:
    out = {}
    with TEXT.open(encoding="utf-8-sig") as f:
        for line in f:
            ref, _, txt = line.rstrip("\n").partition("|")
            if txt:
                out[ref] = txt.lstrip("﻿")
    return out


MAX_RANGE = 300  # the longest surah has 286 ayat; a longer range is kept as its two endpoints


def expand(tokens: list[str]) -> set[str]:
    """Refs as written anywhere in the args: 6:153, (2:255), 36:60-62, 36:60–62, 7:11-7:12, 28:21–24."""
    used = set()
    for m in re.finditer(r"(\d+):(\d+)(?:\s*[-–—]\s*(?:(\d+):)?(\d+))?", " ".join(tokens)):
        s, a, s2, b = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
        if b and (s2 is None or int(s2) == s) and a <= int(b) <= a + MAX_RANGE:
            used.update(f"{s}:{v}" for v in range(a, int(b) + 1))
        else:  # a single ref, a cross-surah range or a reversed range: keep both endpoints
            used.add(f"{s}:{a}")
            if b:
                used.add(f"{int(s2) if s2 else s}:{int(b)}")
    return used


def ordered(tokens: list[str]) -> list[str]:
    """expand() in the order written (for `text`)."""
    out = []
    for m in re.finditer(r"(\d+):(\d+)(?:\s*[-–—]\s*(?:(\d+):)?(\d+))?", " ".join(tokens)):
        for r in sorted(expand([m.group(0)]), key=lambda r: tuple(map(int, r.split(":")))):
            if r not in out:
                out.append(r)
    return out


def listed(focus_refs: list[str], tiers: tuple[str, ...]) -> tuple[list[tuple[str, list[str]]], int]:
    """[(tier label, refs)] in tier order, each ref in its best tier, within a tier by how many focus lists name it,
    then list order; and how many focus lists were found (0 means the check could not run)."""
    rank = {t[0]: i for i, t in enumerate(TIERS) if t[0] in tiers}
    found, best, count, order = 0, {}, {}, {}
    for ref in focus_refs:
        path = LISTS / f"focus_{ref.replace(':', '_')}_cutoff_100.tsv"
        if not path.exists():
            continue
        found += 1
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                if row["relation_scope"] != "cross_surah":
                    continue
                tier = next((t[0] for t in TIERS if t[0] in rank and row["record_type"] == t[1]
                             and row[t[2]] == t[3]), None)
                t = row["target_ref"].strip()
                if tier is None or not re.fullmatch(r"\d+:\d+", t):
                    continue
                count[t] = count.get(t, 0) + 1
                order.setdefault(t, len(order))
                if t not in best or rank[tier] < rank[best[t]]:
                    best[t] = tier
    groups = []
    for t in TIERS:
        if t[0] in rank:
            rs = sorted((r for r, b in best.items() if b == t[0]), key=lambda r: (-count[r], order[r]))
            if rs:
                groups.append((t[4], rs))
    return groups, found


def text_cmd(args: list[str]) -> None:
    rs, q = ordered(args), verses()
    if not rs:
        sys.exit(f"usage: missing.py text <refs> (up to {TEXT_MAX})")
    lines = [f"- ({r}) {q[r]}" if r in q else f"- ({r}) no such ayah" for r in rs[:TEXT_MAX]]
    out, used = [], 0
    for ln in lines:
        if used + size(ln) + 1 > LIMIT_BYTES - 200:
            break
        out.append(ln)
        used += size(ln) + 1
    rest = rs[len(out):]
    print("\n".join(out) + (f"\n({len(rest)} refs not shown; ask for them in another call: "
                            f"{' '.join(rest)})" if rest else ""))


def main() -> None:
    if len(sys.argv) >= 2 and sys.argv[1] == "text":
        text_cmd(sys.argv[2:])
        return
    if len(sys.argv) < 2 or not re.fullmatch(r"S\d+|\d+:\d+", sys.argv[1]):
        sys.exit("usage: missing.py <S:A or S<surah>> <refs you will use ...> | missing.py text <refs>")
    target = sys.argv[1]
    mark = Path(f".missing_py_used_{target.replace(':', '_')}")
    if mark.exists():
        print(f"The list for {target} has already been given once. Write your final output when you are done.")
        return
    text = verses()
    if target.startswith("S"):
        s = target[1:]
        focus = sorted((r for r in text if r.split(":")[0] == s and r.split(":")[1] != "0"),
                       key=lambda r: int(r.split(":")[1]))
        tiers = SURAH_TIERS
    else:
        if target not in text:
            sys.exit(f"{target}: no such ayah")
        focus, tiers = [target], tuple(t[0] for t in TIERS)
    groups, found = listed(focus, tiers)
    if not found:
        answer = (f"No cross-reference list exists for {target}, so this check could not run. Add any passage you "
                  f"recall that belongs, then write your final output.")
    else:
        used = expand(sys.argv[2:])
        groups = [(label, [r for r in rs if r not in used]) for label, rs in groups]
        groups = [(label, rs) for label, rs in groups if rs]
        if groups:
            answer = render(groups) + "\n\n" + instruction()
        else:
            answer = ("Every passage of the earlier cross-reference list is already among your refs. The list "
                      "is not authoritative and may be incomplete: add any other passage you now recall that "
                      "belongs, then write your final output.")
    mark.write_text("used\n")  # only after the answer is ready, so a failure does not burn the one check
    print(answer)


if __name__ == "__main__":
    main()
