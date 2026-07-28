#!/usr/bin/env python3
"""Check layer-2 findings indexes against their bundles.

The index is a table of contents for the field an ayah commentary carries. Its
one non-negotiable property is that it compresses how a reading is *said* and
never how many readings there are — layer 2 is the level forbidden to select
(`PRINCIPLES.md` §3), so an index that quietly drops a reading destroys the
guarantee in a form nobody can see.

Surprise synthesis rows expose a different omission: prose may contain strong
secondary resonances without ever stating what they do to the primary reading.
Rows whose refs begin `surprise:` therefore carry exactly one relation marker,
`[supports-primary]` or `[shifts-primary]`. Use `--require-surprise` when the run
is expected to produce at least one such turn per unit.

That is checkable in one direction only. Whether the prose carries a reading is a
reading judgement; whether the index names every obligatory topic is arithmetic.
This script does the arithmetic and says nothing about the prose.

    python3 scripts/check_index.py --surah 1
    python3 scripts/check_index.py --surah 1 --ayah 2 --profile default.v2.5.6-sol-high
    python3 scripts/check_index.py --surah 1 --outputs-dir _commentary/outputs/s001-default
    python3 scripts/check_index.py --surah 87 --profile default.v2.5.6-sol-high --require-surprise

Exit status is 1 if any unit fails, so it can gate a run.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BUNDLES_DIR = REPO_ROOT / "bundles"
OUTPUTS_DIR = REPO_ROOT / "_commentary" / "outputs"

# - `<ref>` — <clause>            with optional trailing markers
INDEX_LINE = re.compile(
    r"^-\s+`(?P<ref>[^`]+)`\s+[—-]\s+(?P<clause>.+?)\s*$"
)

INFERENCE_MARKER = "[inference]"
SURPRISE_RELATIONS = ("supports-primary", "shifts-primary")
SURPRISE_REF = re.compile(r"^surprise:[a-z0-9]+(?:-[a-z0-9]+)*$")


class BundleProblem(RuntimeError):
    """A bundle could not be read. Never reported as an empty result."""


@dataclass
class UnitResult:
    unit: str
    index_path: Path
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    line_count: int = 0
    required_count: int = 0
    inference_count: int = 0
    surprise_count: int = 0

    @property
    def ok(self) -> bool:
        return not self.errors


def required_topic_ids(bundle: dict) -> tuple[list[str], list[str]]:
    """Topic ids the index must carry, and the ledger_only ids it must not.

    `ledger_only` marks a topic review has set aside — a duplicate of another
    topic, or one whose claim the bundle contradicts. It is excluded from the
    commentary and from the index. `candidate` topics are discretionary, so they
    are neither required nor forbidden.
    """
    word_analysis = bundle.get("word_analysis")
    if not isinstance(word_analysis, dict):
        raise BundleProblem("word_analysis is missing or not an object")
    words = word_analysis.get("words")
    if not isinstance(words, list) or not words:
        raise BundleProblem("word_analysis.words is missing or empty")

    required: list[str] = []
    excluded: list[str] = []
    for word in words:
        for topic in word.get("topics") or []:
            topic_id = topic.get("topic_id")
            if not topic_id:
                continue
            obligation = topic.get("commentary_obligation")
            if obligation == "must_integrate":
                required.append(topic_id)
            elif obligation == "ledger_only":
                excluded.append(topic_id)
    return required, excluded


def _split_markers(clause: str) -> tuple[str, list[str]]:
    """Remove recognized trailing markers without treating bracketed prose as metadata."""
    markers: list[str] = []
    marker_re = re.compile(
        r"\s+\[(inference|supports-primary|shifts-primary)\]\s*$"
    )
    while match := marker_re.search(clause):
        markers.append(match.group(1))
        clause = clause[:match.start()].rstrip()
    markers.reverse()
    return clause, markers


def parse_index(path: Path) -> tuple[list[tuple[str, bool, list[str], str]], list[str]]:
    """Return parsed entries plus lines that are not index entries."""
    entries: list[tuple[str, bool, list[str], str]] = []
    malformed: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        match = INDEX_LINE.match(line)
        if match:
            clause, markers = _split_markers(match.group("clause").strip())
            entries.append(
                (
                    match.group("ref").strip(),
                    "inference" in markers,
                    [m for m in markers if m in SURPRISE_RELATIONS],
                    clause,
                )
            )
        else:
            malformed.append(line)
    return entries, malformed


def check_unit(
    unit: str,
    bundle_path: Path,
    index_path: Path,
    require_surprise: bool = False,
) -> UnitResult:
    result = UnitResult(unit=unit, index_path=index_path)

    with bundle_path.open(encoding="utf-8") as handle:
        bundle = json.load(handle)
    required, excluded = required_topic_ids(bundle)
    result.required_count = len(required)

    if not index_path.exists():
        result.errors.append(f"no index file at {index_path.relative_to(REPO_ROOT)}")
        return result

    entries, malformed = parse_index(index_path)
    result.line_count = len(entries)
    result.inference_count = sum(1 for _, inf, _, _ in entries if inf)

    if not entries:
        # A file that exists and yields nothing is worse than one that is absent,
        # because the absence is visible and the emptiness is not.
        result.errors.append("index file is present but contains no parsable entries")
        return result

    refs = [ref for ref, _, _, _ in entries]
    seen: dict[str, int] = {}
    for ref in refs:
        seen[ref] = seen.get(ref, 0) + 1

    missing = [t for t in required if t not in seen]
    if missing:
        result.errors.append(
            f"{len(missing)} must_integrate topic(s) absent from the index — "
            "the index dropped readings the prose is obliged to carry: "
            + ", ".join(missing[:8])
            + (" …" if len(missing) > 8 else "")
        )

    duplicated = sorted(t for t in required if seen.get(t, 0) > 1)
    if duplicated:
        result.errors.append(
            "must_integrate topic(s) listed more than once: " + ", ".join(duplicated)
        )

    present_excluded = sorted(t for t in excluded if t in seen)
    if present_excluded:
        result.errors.append(
            "ledger_only topic(s) in the index — review set these aside: "
            + ", ".join(present_excluded)
        )

    surprise_refs: list[str] = []
    for ref, _, relations, clause in entries:
        is_surprise = ref.startswith("surprise:")
        if is_surprise:
            surprise_refs.append(ref)
            if not SURPRISE_REF.fullmatch(ref):
                result.errors.append(
                    f"invalid surprise ref {ref!r}; use surprise:<lowercase-ascii-id>"
                )
            if len(relations) != 1:
                result.errors.append(
                    f"{ref} must carry exactly one of [supports-primary] or "
                    "[shifts-primary]"
                )
            if not clause:
                result.errors.append(f"{ref} has no surprise statement")
        elif relations:
            result.errors.append(
                f"primary-relation marker appears on non-surprise row {ref!r}"
            )

    result.surprise_count = len(surprise_refs)
    duplicated_surprises = sorted(
        ref for ref in set(surprise_refs) if surprise_refs.count(ref) > 1
    )
    if duplicated_surprises:
        result.errors.append(
            "surprise synthesis ref(s) listed more than once: "
            + ", ".join(duplicated_surprises)
        )
    if require_surprise and not surprise_refs:
        result.errors.append(
            "no explicit surprise synthesis row; --require-surprise expects at "
            "least one grounded [supports-primary] or [shifts-primary] turn"
        )
    elif not surprise_refs:
        result.warnings.append(
            "no explicit surprise synthesis row; new runs should explain in "
            "evidence coverage when no grounded local surprise forms"
        )

    for line in malformed:
        if INFERENCE_MARKER.lower() in line.lower() or line.startswith("-"):
            result.errors.append(f"unparsable index line: {line[:90]}")
        else:
            result.warnings.append(f"ignored non-entry line: {line[:90]}")

    return result


def discover_units(surah: int, ayah: int | None, outputs_dir: Path, profile: str | None):
    bundle_dir = BUNDLES_DIR / f"s{surah:03d}"
    if not bundle_dir.is_dir():
        raise BundleProblem(f"no bundle directory at {bundle_dir.relative_to(REPO_ROOT)}")

    bundles = sorted(
        bundle_dir.glob(f"{surah}_*.ayah.json"),
        key=lambda p: int(p.name.split("_")[1].split(".")[0]),
    )
    if not bundles:
        raise BundleProblem(f"no ayah bundles in {bundle_dir.relative_to(REPO_ROOT)}")

    units = []
    for bundle_path in bundles:
        stem = bundle_path.name.split(".")[0]  # e.g. "1_2"
        this_ayah = int(stem.split("_")[1])
        if ayah is not None and this_ayah != ayah:
            continue
        suffix = f".{profile}" if profile else ""
        units.append((stem, bundle_path, outputs_dir / f"{stem}.index{suffix}.md"))
    if not units:
        raise BundleProblem(f"no units matched (surah {surah}, ayah {ayah})")
    return units


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--ayah", type=int, default=None)
    parser.add_argument(
        "--profile",
        default=None,
        help="label between '.index' and '.md', e.g. 'default.v2.5.6-sol-high'",
    )
    parser.add_argument("--outputs-dir", default=None, help="defaults to _commentary/outputs/s{NNN}")
    parser.add_argument(
        "--require-surprise",
        action="store_true",
        help="fail a unit with no explicit surprise:<id> synthesis row",
    )
    args = parser.parse_args()

    outputs_dir = (
        Path(args.outputs_dir) if args.outputs_dir else OUTPUTS_DIR / f"s{args.surah:03d}"
    )
    if not outputs_dir.is_absolute():
        outputs_dir = REPO_ROOT / outputs_dir

    try:
        units = discover_units(args.surah, args.ayah, outputs_dir, args.profile)
    except BundleProblem as exc:
        print(f"check_index: {exc}", file=sys.stderr)
        return 2

    results = []
    for unit, bundle_path, index_path in units:
        try:
            results.append(
                check_unit(
                    unit,
                    bundle_path,
                    index_path,
                    require_surprise=args.require_surprise,
                )
            )
        except BundleProblem as exc:
            failed = UnitResult(unit=unit, index_path=index_path)
            failed.errors.append(f"bundle unusable: {exc}")
            results.append(failed)

    width = max(len(r.unit) for r in results)
    failures = 0
    for r in results:
        status = "ok  " if r.ok else "FAIL"
        print(
            f"{status} {r.unit:<{width}}  entries={r.line_count:<4} "
            f"required={r.required_count:<4} inference={r.inference_count:<4} "
            f"surprises={r.surprise_count}"
        )
        for err in r.errors:
            print(f"       error: {err}")
        for warn in r.warnings:
            print(f"       warn:  {warn}")
        if not r.ok:
            failures += 1

    print(f"\n{len(results) - failures}/{len(results)} units pass")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
