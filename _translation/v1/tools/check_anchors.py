#!/usr/bin/env python3
"""Mechanically check one primary-anchor seed against its anchor input.

Checks only what the selection agent authored: that every rooted stem is covered
exactly once, that every branch and lexical unit id exists on that stem's own
root, that rejections are disjoint from selections, and that nothing was left
unresolved. It does not judge whether the chosen branch is the right one.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

V1_DIR = Path(__file__).resolve().parents[1]

SEED_KEYS = {"schemaVersion", "surah", "anchors", "unresolved"}
ANCHOR_KEYS = {
    "qacMorphemeRef",
    "branchIds",
    "lexicalUnitIds",
    "consideredNotPrimary",
}
REJECTION_KEYS = {"branchId", "reason"}
ACCEPTED_SCHEMA_VERSIONS = {"primary-anchor-seed-v1", "primary-anchor-seed-v2"}


def read_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def extra_keys(value: dict, allowed: set[str]) -> set[str]:
    return set(value) - allowed


def check(anchor_input: dict, seed: dict) -> list[str]:
    errors: list[str] = []

    extras = extra_keys(seed, SEED_KEYS)
    if extras:
        errors.append(f"seed has unsupported fields: {sorted(extras)}")
    if seed.get("schemaVersion") not in ACCEPTED_SCHEMA_VERSIONS:
        errors.append(
            f"schemaVersion: expected one of {sorted(ACCEPTED_SCHEMA_VERSIONS)}, "
            f"found {seed.get('schemaVersion')!r}"
        )
    elif seed["schemaVersion"] == "primary-anchor-seed-v1":
        lost = sum(
            len(
                {
                    candidate["branchId"]
                    for candidate in anchor_input["roots"][stem["rootId"]][
                        "branchCandidates"
                    ]
                    if candidate.get("v12Activated")
                }
            )
            for ayah in anchor_input["ayat"]
            for stem in ayah["rootedStems"]
        )
        errors.append(
            "seed is primary-anchor-seed-v1, which has no consideredNotPrimary "
            f"field: up to {lost} activated branch selections across this surah "
            "are recorded nowhere and are lost to layers 2 and 3 "
            "(PRINCIPLES.md §6). Re-seed at v2."
        )
    if seed.get("surah") != anchor_input["surah"]:
        errors.append(
            f"surah: expected {anchor_input['surah']}, found {seed.get('surah')!r}"
        )

    unresolved = seed.get("unresolved") or []
    if unresolved:
        refs = [item.get("qacMorphemeRef") for item in unresolved]
        errors.append(f"{len(unresolved)} unresolved stem(s): {refs}")

    stems = {
        stem["qacMorphemeRef"]: stem
        for ayah in anchor_input["ayat"]
        for stem in ayah["rootedStems"]
    }
    roots = anchor_input["roots"]

    anchors = seed.get("anchors")
    if not isinstance(anchors, list):
        return errors + ["anchors must be an array"]

    expected_order = list(stems)
    found_order = [
        anchor.get("qacMorphemeRef")
        for anchor in anchors
        if isinstance(anchor, dict)
    ]
    if found_order != expected_order:
        missing = [ref for ref in expected_order if ref not in found_order]
        unknown = [ref for ref in found_order if ref not in stems]
        duplicated = sorted(
            {ref for ref in found_order if found_order.count(ref) > 1}
        )
        if missing:
            errors.append(f"stems with no anchor: {missing}")
        if unknown:
            errors.append(f"anchors for unknown stems: {unknown}")
        if duplicated:
            errors.append(f"duplicate anchors: {duplicated}")
        if not (missing or unknown or duplicated):
            errors.append("anchors are not in input stem order")

    for index, anchor in enumerate(anchors):
        if not isinstance(anchor, dict):
            errors.append(f"anchors[{index}] must be an object")
            continue
        ref = anchor.get("qacMorphemeRef")
        label = ref or f"anchors[{index}]"
        extras = extra_keys(anchor, ANCHOR_KEYS)
        if extras:
            errors.append(f"{label}: unsupported fields {sorted(extras)}")

        stem = stems.get(ref)
        if stem is None:
            continue
        root = roots[stem["rootId"]]
        known_branches = {
            candidate["branchId"] for candidate in root["branchCandidates"]
        }
        units_by_id = {
            candidate["lexicalUnitId"]: candidate
            for candidate in root["lexicalCandidates"]
        }

        branch_ids = anchor.get("branchIds")
        if not isinstance(branch_ids, list) or not branch_ids:
            errors.append(f"{label}: branchIds must be a nonempty array")
            branch_ids = []
        unknown = [b for b in branch_ids if b not in known_branches]
        if unknown:
            errors.append(
                f"{label}: branch(es) {unknown} are not on root {stem['rootId']}"
            )

        unit_ids = anchor.get("lexicalUnitIds", [])
        if not isinstance(unit_ids, list):
            errors.append(f"{label}: lexicalUnitIds must be an array")
            unit_ids = []
        for unit_id in unit_ids:
            unit = units_by_id.get(unit_id)
            if unit is None:
                errors.append(
                    f"{label}: lexical unit {unit_id!r} is not on root "
                    f"{stem['rootId']}"
                )
            elif not set(unit["branchIds"]) & set(branch_ids):
                errors.append(
                    f"{label}: lexical unit {unit_id!r} belongs to "
                    f"{unit['branchIds']}, not to the selected {branch_ids}"
                )

        rejections = anchor.get("consideredNotPrimary", [])
        if not isinstance(rejections, list):
            errors.append(f"{label}: consideredNotPrimary must be an array")
            rejections = []
        seen: set[str] = set()
        for rejection in rejections:
            if not isinstance(rejection, dict):
                errors.append(f"{label}: consideredNotPrimary entries must be objects")
                continue
            extras = extra_keys(rejection, REJECTION_KEYS)
            if extras:
                errors.append(
                    f"{label}: consideredNotPrimary has unsupported fields "
                    f"{sorted(extras)}"
                )
            branch_id = rejection.get("branchId")
            if branch_id not in known_branches:
                errors.append(
                    f"{label}: rejected branch {branch_id!r} is not on root "
                    f"{stem['rootId']}"
                )
            if branch_id in branch_ids:
                errors.append(
                    f"{label}: branch {branch_id!r} is both selected and rejected"
                )
            if branch_id in seen:
                errors.append(f"{label}: branch {branch_id!r} rejected twice")
            seen.add(branch_id)
            if not isinstance(rejection.get("reason"), str) or not rejection["reason"]:
                errors.append(
                    f"{label}: rejection of {branch_id!r} needs a nonempty reason"
                )

        # A rejection that is not recorded is evidence destroyed
        # (`PRINCIPLES.md` §6). Activated-but-unselected branches are the set
        # the pipeline is known to lose, so they are enforced rather than
        # advised. A v1 seed has no field to record them in; that is reported
        # once for the file instead of once per stem.
        if seed.get("schemaVersion") == "primary-anchor-seed-v1":
            continue
        activated = {
            candidate["branchId"]
            for candidate in root["branchCandidates"]
            if candidate.get("v12Activated")
        }
        undocumented = sorted(activated - set(branch_ids) - seen)
        if undocumented:
            errors.append(
                f"{label}: activated branch(es) {undocumented} neither selected "
                "nor recorded in consideredNotPrimary"
            )

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--anchor-input", type=Path)
    parser.add_argument("--seed", type=Path)
    args = parser.parse_args()

    surah_key = f"s{args.surah:03d}"
    anchor_input = args.anchor_input or (
        V1_DIR / "anchors" / "input" / f"{surah_key}.anchor-input.json"
    )
    seed = args.seed or V1_DIR / "source" / f"{surah_key}.primary-anchors.json"

    errors = check(read_json(anchor_input), read_json(seed))
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
    print(f"OK: {seed}")


if __name__ == "__main__":
    main()
