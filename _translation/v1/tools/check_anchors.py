#!/usr/bin/env python3
"""Mechanically check a primary-anchor seed against its frozen input."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

V1_DIR = Path(__file__).resolve().parents[1]

SEED_KEYS = {"schemaVersion", "surah", "anchors", "unresolved"}
V4_ANCHOR_KEYS = {"qacMorphemeRef", "primary", "resonances"}
ROOT_BRANCH_KEYS = {"rootId", "branchIds"}
LEGACY_ANCHOR_KEYS = {
    "qacMorphemeRef",
    "rootId",
    "branchIds",
    "lexicalUnitIds",
    "consideredNotPrimary",
}
LEGACY_REJECTION_KEYS = {"rootId", "branchId", "reason"}
UNRESOLVED_KEYS = {"qacMorphemeRef", "reason"}
ACCEPTED_SCHEMA_VERSIONS = {
    "primary-anchor-seed-v1",
    "primary-anchor-seed-v2",
    "primary-anchor-seed-v3",
    "primary-anchor-seed-v4",
}


def read_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def extra_keys(value: dict, allowed: set[str]) -> set[str]:
    return set(value) - allowed


def stem_root_ids(stem: dict) -> list[str]:
    resolution = stem.get("rootResolution")
    if resolution:
        return [
            target["rootId"]
            for target in resolution.get("targets", [])
            if target.get("rootId")
        ]
    return [stem["rootId"]]


def known_branch_ids(anchor_input: dict, root_id: str) -> set[str]:
    root = anchor_input["roots"].get(root_id)
    if not isinstance(root, dict):
        return set()
    candidates = root.get("branches", root.get("branchCandidates", []))
    return {
        candidate["branchId"]
        for candidate in candidates
        if isinstance(candidate, dict) and candidate.get("branchId")
    }


def validate_root_branch_group(
    group: object,
    *,
    label: str,
    stem: dict,
    anchor_input: dict,
    errors: list[str],
) -> tuple[str | None, list[str]]:
    if not isinstance(group, dict):
        errors.append(f"{label} must be an object")
        return None, []
    extras = extra_keys(group, ROOT_BRANCH_KEYS)
    if extras:
        errors.append(f"{label} has unsupported fields: {sorted(extras)}")

    root_id = group.get("rootId")
    candidates = stem_root_ids(stem)
    if root_id not in candidates:
        errors.append(f"{label}.rootId {root_id!r} is not among {candidates}")
        return None, []

    branch_ids = group.get("branchIds")
    if not isinstance(branch_ids, list) or not branch_ids:
        errors.append(f"{label}.branchIds must be a nonempty array")
        branch_ids = []
    elif len(branch_ids) != len(set(branch_ids)):
        errors.append(f"{label}.branchIds contains duplicates")

    known = known_branch_ids(anchor_input, root_id)
    unknown = [branch_id for branch_id in branch_ids if branch_id not in known]
    if unknown:
        errors.append(
            f"{label}: branch(es) {unknown} are not on root {root_id}"
        )
    return root_id, branch_ids


def collect_scope(
    anchor_input: dict,
    seed: dict,
    errors: list[str],
) -> tuple[dict[str, dict], set[str], list[dict]]:
    stems = {
        stem["qacMorphemeRef"]: stem
        for ayah in anchor_input["ayat"]
        for stem in ayah["rootedStems"]
    }

    unresolved = seed.get("unresolved")
    unresolved_refs: set[str] = set()
    if not isinstance(unresolved, list):
        errors.append("unresolved must be an array")
        unresolved = []
    for index, item in enumerate(unresolved):
        label = f"unresolved[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{label} must be an object")
            continue
        extras = extra_keys(item, UNRESOLVED_KEYS)
        if extras:
            errors.append(f"{label} has unsupported fields: {sorted(extras)}")
        ref = item.get("qacMorphemeRef")
        if ref not in stems:
            errors.append(f"{label} has unknown ref {ref!r}")
            continue
        if ref in unresolved_refs:
            errors.append(f"{label} duplicates {ref!r}")
        unresolved_refs.add(ref)
        if not isinstance(item.get("reason"), str) or not item["reason"]:
            errors.append(f"{label} needs a nonempty reason")
    if unresolved_refs:
        errors.append(
            f"{len(unresolved_refs)} unresolved stem(s): {sorted(unresolved_refs)}"
        )

    anchors = seed.get("anchors")
    if not isinstance(anchors, list):
        errors.append("anchors must be an array")
        return stems, unresolved_refs, []

    expected_order = [ref for ref in stems if ref not in unresolved_refs]
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
    return stems, unresolved_refs, anchors


def check_v4(
    anchor_input: dict,
    anchors: list[dict],
    stems: dict[str, dict],
    errors: list[str],
) -> None:
    if anchor_input.get("schemaVersion") != "anchor-input-v2":
        errors.append(
            "primary-anchor-seed-v4 requires anchor-input-v2, found "
            f"{anchor_input.get('schemaVersion')!r}"
        )

    for index, anchor in enumerate(anchors):
        if not isinstance(anchor, dict):
            errors.append(f"anchors[{index}] must be an object")
            continue
        ref = anchor.get("qacMorphemeRef")
        label = ref or f"anchors[{index}]"
        extras = extra_keys(anchor, V4_ANCHOR_KEYS)
        if extras:
            errors.append(f"{label}: unsupported fields {sorted(extras)}")
        stem = stems.get(ref)
        if stem is None:
            continue

        primary_root, primary_branches = validate_root_branch_group(
            anchor.get("primary"),
            label=f"{label}.primary",
            stem=stem,
            anchor_input=anchor_input,
            errors=errors,
        )

        resonances = anchor.get("resonances")
        if not isinstance(resonances, list):
            errors.append(f"{label}.resonances must be an array")
            continue
        seen: set[tuple[str, str]] = set()
        seen_roots: set[str] = set()
        for resonance_index, resonance in enumerate(resonances):
            resonance_label = f"{label}.resonances[{resonance_index}]"
            root_id, branch_ids = validate_root_branch_group(
                resonance,
                label=resonance_label,
                stem=stem,
                anchor_input=anchor_input,
                errors=errors,
            )
            if root_id is None:
                continue
            if root_id in seen_roots:
                errors.append(
                    f"{resonance_label}: resonances for root {root_id} "
                    "must be grouped in one object"
                )
            seen_roots.add(root_id)
            for branch_id in branch_ids:
                key = (root_id, branch_id)
                if key in seen:
                    errors.append(f"{resonance_label}: duplicate resonance {key}")
                seen.add(key)
                if root_id == primary_root and branch_id in primary_branches:
                    errors.append(
                        f"{resonance_label}: {branch_id} is both primary and resonance"
                    )


def selected_legacy_root_id(
    anchor: dict,
    stem: dict,
    label: str,
    errors: list[str],
) -> str | None:
    candidates = stem_root_ids(stem)
    root_id = anchor.get("rootId")
    if root_id is not None:
        if root_id not in candidates:
            errors.append(f"{label}: rootId {root_id!r} is not among {candidates}")
            return None
        return root_id
    if len(candidates) == 1:
        return candidates[0]
    errors.append(f"{label}: rootId is required for split candidate roots {candidates}")
    return None


def check_legacy(
    anchor_input: dict,
    seed: dict,
    anchors: list[dict],
    stems: dict[str, dict],
    errors: list[str],
) -> None:
    if seed.get("schemaVersion") == "primary-anchor-seed-v1":
        errors.append("primary-anchor-seed-v1 is obsolete; re-seed at v4")

    for index, anchor in enumerate(anchors):
        if not isinstance(anchor, dict):
            errors.append(f"anchors[{index}] must be an object")
            continue
        ref = anchor.get("qacMorphemeRef")
        label = ref or f"anchors[{index}]"
        extras = extra_keys(anchor, LEGACY_ANCHOR_KEYS)
        if extras:
            errors.append(f"{label}: unsupported fields {sorted(extras)}")
        stem = stems.get(ref)
        if stem is None:
            continue
        root_id = selected_legacy_root_id(anchor, stem, label, errors)
        if root_id is None:
            continue

        branch_ids = anchor.get("branchIds")
        if not isinstance(branch_ids, list) or not branch_ids:
            errors.append(f"{label}: branchIds must be a nonempty array")
            branch_ids = []
        elif len(branch_ids) != len(set(branch_ids)):
            errors.append(f"{label}: branchIds contains duplicates")
        unknown = [
            branch_id
            for branch_id in branch_ids
            if branch_id not in known_branch_ids(anchor_input, root_id)
        ]
        if unknown:
            errors.append(
                f"{label}: branch(es) {unknown} are not on root {root_id}"
            )

        root = anchor_input["roots"].get(root_id, {})
        lexical_candidates = root.get("lexicalCandidates")
        if lexical_candidates is not None:
            units = {
                candidate["lexicalUnitId"]: candidate
                for candidate in lexical_candidates
            }
            unit_ids = anchor.get("lexicalUnitIds", [])
            if not isinstance(unit_ids, list):
                errors.append(f"{label}: lexicalUnitIds must be an array")
                unit_ids = []
            for unit_id in unit_ids:
                unit = units.get(unit_id)
                if unit is None:
                    errors.append(
                        f"{label}: lexical unit {unit_id!r} is not on root {root_id}"
                    )
                elif not set(unit["branchIds"]) & set(branch_ids):
                    errors.append(
                        f"{label}: lexical unit {unit_id!r} belongs to "
                        f"{unit['branchIds']}, not selected {branch_ids}"
                    )

        rejections = anchor.get("consideredNotPrimary", [])
        if not isinstance(rejections, list):
            errors.append(f"{label}: consideredNotPrimary must be an array")
            continue
        seen: set[tuple[str, str]] = set()
        for rejection_index, rejection in enumerate(rejections):
            rejection_label = (
                f"{label}.consideredNotPrimary[{rejection_index}]"
            )
            if not isinstance(rejection, dict):
                errors.append(f"{rejection_label} must be an object")
                continue
            extras = extra_keys(rejection, LEGACY_REJECTION_KEYS)
            if extras:
                errors.append(
                    f"{rejection_label} has unsupported fields {sorted(extras)}"
                )
            rejection_root = rejection.get("rootId") or root_id
            if rejection_root not in stem_root_ids(stem):
                errors.append(
                    f"{rejection_label}: root {rejection_root!r} is not a candidate"
                )
                continue
            branch_id = rejection.get("branchId")
            if branch_id not in known_branch_ids(anchor_input, rejection_root):
                errors.append(
                    f"{rejection_label}: branch {branch_id!r} is not on "
                    f"{rejection_root}"
                )
            key = (rejection_root, branch_id)
            if key in seen:
                errors.append(f"{rejection_label}: duplicate rejection {key}")
            seen.add(key)
            if rejection_root == root_id and branch_id in branch_ids:
                errors.append(
                    f"{rejection_label}: branch is both selected and rejected"
                )
            if not isinstance(rejection.get("reason"), str) or not rejection["reason"]:
                errors.append(f"{rejection_label}: reason must be nonempty")


def check(anchor_input: dict, seed: dict) -> list[str]:
    errors: list[str] = []
    extras = extra_keys(seed, SEED_KEYS)
    if extras:
        errors.append(f"seed has unsupported fields: {sorted(extras)}")

    schema_version = seed.get("schemaVersion")
    if schema_version not in ACCEPTED_SCHEMA_VERSIONS:
        errors.append(
            f"schemaVersion: expected one of {sorted(ACCEPTED_SCHEMA_VERSIONS)}, "
            f"found {schema_version!r}"
        )
    if seed.get("surah") != anchor_input.get("surah"):
        errors.append(
            f"surah: expected {anchor_input.get('surah')}, "
            f"found {seed.get('surah')!r}"
        )

    stems, _, anchors = collect_scope(anchor_input, seed, errors)
    if schema_version == "primary-anchor-seed-v4":
        check_v4(anchor_input, anchors, stems, errors)
    elif schema_version in ACCEPTED_SCHEMA_VERSIONS:
        check_legacy(anchor_input, seed, anchors, stems, errors)
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--anchor-input", type=Path)
    parser.add_argument("--seed", type=Path)
    args = parser.parse_args()

    surah_key = f"s{args.surah:03d}"
    anchor_input_path = args.anchor_input or (
        V1_DIR / "anchors" / "input" / f"{surah_key}.anchor-input.json"
    )
    seed_path = args.seed or (
        V1_DIR / "source" / f"{surah_key}.primary-anchors.json"
    )

    errors = check(read_json(anchor_input_path), read_json(seed_path))
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
    print(f"OK: {seed_path}")


if __name__ == "__main__":
    main()
