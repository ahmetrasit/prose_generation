#!/usr/bin/env python3
"""Split a V9 package into Luna worklists: small files of numbered items, each judged on its own.

  context.md        the ayah (00), the Fatiha text, the whole surah (08) — read first in every session
  W0_dictionary.md  one item per focus root with its full dictionary entry and no pairs: open discovery
                    from the entries alone (cross-root images and contrasts, sound play, grammar)
  W1_branches_N.md  one item per focus branch: its dictionary line + pairs (03) + concept paths (06) +
                    Fatiha pairs (07) + bridges (04) that point at it; one usage item per focus root (05)
  W2_hft.md         one item per HFT record (02) and per precomputed lead (10)
  W3_global_N.md    one item per inter-ayah target (09); formula groups stay together
  items.tsv         every item id with its worklist (the checker's reference)

Usage: python3 _commentary/v9/luna/worklists.py PACKAGE_DIR OUT_DIR
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

MAX_BYTES = 40_000  # per worklist file; Luna reads each whole in a few shell calls
BRANCH_RE = re.compile(r"^- \*\*(B\d{3})\*\*")
ROOT_RE = re.compile(r"^((?:[ء-ي] ){1,5}[ء-ي])(?![ء-ي])")  # spaced root letters, e.g. "ع و د"


def read(pkg: Path, prefix: str) -> str:
    return next(pkg.glob(f"{prefix}_*.md")).read_text(encoding="utf-8")


def blocks(text: str, head: str) -> list[tuple[str, list[str]]]:
    """Split text at lines starting with `head`; returns (heading line, body lines)."""
    out, cur = [], None
    for line in text.splitlines():
        if line.startswith(head) and not line.startswith(head + "#"):
            cur = (line, [])
            out.append(cur)
        elif cur is not None:
            cur[1].append(line)
    return out


def root_key(s: str) -> str:
    m = ROOT_RE.match(s.strip().removeprefix("ECHO ").strip())
    return m.group(1) if m else s.strip()


def branch_items(pkg: Path) -> tuple[list[str], list[tuple[str, str]]]:
    dictionary, pairs, concepts = read(pkg, "01"), read(pkg, "03"), read(pkg, "06")
    fatiha, bridges, usage = read(pkg, "07"), read(pkg, "04"), read(pkg, "05")

    pair_lines = defaultdict(list)       # (root, branch) -> lines
    for head, body in blocks(pairs, "## "):
        root, cur = root_key(head[3:]), None
        for line in body:
            m = BRANCH_RE.match(line)
            if m:
                cur = m.group(1)
            elif cur and line.startswith("  - "):
                pair_lines[(root, cur)].append(line.strip()[2:])
    concept_lines = defaultdict(list)
    root = None
    for line in concepts.splitlines():
        if line.startswith("- **"):
            root = root_key(line[4:])
        elif root and line.startswith("  - B"):
            concept_lines[(root, line.strip()[2:6])].append(line.strip()[2:])
    fatiha_lines = defaultdict(list)
    key = None
    for line in fatiha.splitlines():
        if line.startswith("- **"):
            m = re.match(r"- \*\*((?:\S ){1,5}\S) (B\d{3})", line)
            key = (m.group(1), m.group(2)) if m else None
        elif key and line.startswith("  - "):
            fatiha_lines[key].append(line.strip()[2:])
    bridge_lines = defaultdict(list)
    for line in bridges.splitlines():
        m = re.search(r"‖ focus: ((?:\S ){1,5}\S) (B\d{3})", line)
        if m:
            bridge_lines[(m.group(1), m.group(2))].append(line[2:].split("  ‖")[0])
    usage_by_root = defaultdict(list)
    for head, body in blocks(usage, "## "):
        m = re.search(r"root ((?:\S ){1,5}\S),", head)
        if m:
            usage_by_root[m.group(1)].append("\n".join([head[3:]] + [l for l in body if l.strip()]))

    roots, items = [], []
    for head, body in blocks(dictionary, "## "):
        root = root_key(head[3:])
        roots.append(head[3:])
        r = len(roots)
        desc = next((l for l in body if l.strip() and not l.startswith("-")), "")
        usage_lines = [l for block in usage_by_root.get(root, []) for l in block.splitlines()[1:]]
        items.append((f"R{r:02d}.U", numbered(
            f"R{r:02d}.U — usage of {root} ({head[3:]})",
            [desc] + [b.splitlines()[0] for b in usage_by_root.get(root, [])]
            or [desc, "(no usage profile: echo or alternative root)"], usage_lines)))
        for line in body:
            m = BRANCH_RE.match(line)
            if not m:
                continue
            b = m.group(1)
            evidence = [f"{label}: {x}" for label, src in (("pair", pair_lines), ("concept", concept_lines),
                                                           ("fatiha", fatiha_lines), ("bridge", bridge_lines))
                        for x in src.get((root, b), [])]
            items.append((f"R{r:02d}.{b}", numbered(f"R{r:02d}.{b} — {root} {b}", [f"dictionary: {line[2:]}"], evidence)))
    return roots, items


def numbered(title: str, head: list[str], lines: list[str]) -> str:
    """An item whose evidence lines are numbered [1]…[n]; Luna returns one code per line."""
    body = [f"[{k}] {l.strip().removeprefix('- ')}" for k, l in enumerate(lines, 1)]
    template = [f"codes: {'_' * len(body)} ({len(body)})"] if body else []
    return "\n".join([f"### {title} — lines: {len(body)}"] + head + template + body)


def hft_items(pkg: Path) -> list[tuple[str, str]]:
    items = []
    for i, (head, body) in enumerate(blocks(read(pkg, "02"), "## "), 1):
        items.append((f"H{i:02d}", "\n".join([f"### H{i:02d} — {head[3:]}"] + [l for l in body if l.strip()])))
    for i, (head, body) in enumerate(blocks(read(pkg, "10"), "## "), 1):
        items.append((f"L{i:02d}", "\n".join([f"### L{i:02d} — lead: {head[3:]}"] + [l for l in body if l.strip()])))
    return items


def global_units(pkg: Path) -> list[list[tuple[str, str]]]:
    """Inter-ayah targets as items; a formula group is one unit so it is never split across files."""
    units, n = [], 0
    for head, body in blocks(read(pkg, "09"), "## "):
        if head.startswith("## Formula group"):
            unit = []
            for sub, sbody in blocks("\n".join(body), "### "):
                n += 1
                ref = sub.split(". ", 1)[1].strip()
                unit.append((f"G{n:03d}", "\n".join(
                    [f"### G{n:03d} — {ref} ({head[3:]})"] + [l for l in sbody if l.strip()])))
            units.append(unit)
        else:
            n += 1
            ref = head.split(". ", 1)[1].strip()
            units.append([(f"G{n:03d}", "\n".join([f"### G{n:03d} — {ref}"] + [l for l in body if l.strip()]))])
    return units


def dictionary_items(pkg: Path) -> list[tuple[str, str]]:
    return [(f"D{i:02d}", "\n".join([f"### D{i:02d} — {head[3:]}"] + [l for l in body if l.strip()]))
            for i, (head, body) in enumerate(blocks(read(pkg, "01"), "## "), 1)]


def pack(units: list[list[tuple[str, str]]]) -> list[list[tuple[str, str]]]:
    files, cur, size = [], [], 0
    for unit in units:
        u_size = sum(len(t.encode()) for _, t in unit)
        if cur and size + u_size > MAX_BYTES:
            files.append(cur)
            cur, size = [], 0
        cur += unit
        size += u_size
    if cur:
        files.append(cur)
    return files


def main() -> None:
    pkg, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    ayah = read(pkg, "00")
    fatiha_text = "\n".join(l for l in read(pkg, "07").splitlines() if re.match(r"- 1:\d ", l))
    (out / "context.md").write_text(
        f"{ayah.rstrip()}\n\n# Fatiha (recited in every salah)\n{fatiha_text}\n\n{read(pkg, '08').rstrip()}\n",
        encoding="utf-8")

    roots, b_items = branch_items(pkg)
    by_root = defaultdict(list)
    for iid, text in b_items:
        by_root[iid.split(".")[0]].append((iid, text))
    plan = [("W0_dictionary", [dictionary_items(pkg)]),
            ("W1_branches", pack(list(by_root.values()))),
            ("W2_hft", [hft_items(pkg)]),
            ("W3_global", pack(global_units(pkg)))]
    index = []
    for stem, files in plan:
        for k, items in enumerate(files, 1):
            name = f"{stem}_{k}.md" if len(files) > 1 else f"{stem}.md"
            head = [f"# {name} — {len(items)} items: {items[0][0]} … {items[-1][0]}", ""]
            if stem == "W1_branches":
                head += ["Roots in this package:"] + [f"- R{i:02d} {r}" for i, r in enumerate(roots, 1)] + [""]
            (out / name).write_text("\n".join(head) + "\n\n".join(t for _, t in items) + "\n", encoding="utf-8")
            index += [f"{iid}\t{name}" for iid, _ in items]
    (out / "items.tsv").write_text("\n".join(index) + "\n", encoding="utf-8")
    sizes = {p.name: p.stat().st_size for p in sorted(out.glob("*.md"))}
    print(f"{len(index)} items; files: {sizes}")


if __name__ == "__main__":
    main()
