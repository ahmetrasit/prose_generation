#!/usr/bin/env python3
"""Dependency-free checks for combined channel-commentary bundles."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT_ID = re.compile(r"^root_\d{6}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
ANCHOR_ID = re.compile(r"^a\d{3}-\d{4}$")
BRANCH_ID = re.compile(r"^B\d{3}$")
MOTIF_ID = re.compile(r"^(m\d{2,}|_)$")
REMOVED_TOP_LEVEL = {"pericopes", "channelGeneratedOutputs"}
# Mirrors "additionalProperties": false in channel-bundle-v1.schema.json. The
# schema is not loaded at runtime, so an unlisted key would otherwise pass —
# which is how a post-adjudication field could ride into a draft bundle.
ALLOWED_TOP_LEVEL = {
    "schemaVersion",
    "bundleType",
    "surah",
    "reviewedChannels",
    "text",
    "anchorInventory",
    "motifAnchorMap",
    "primaryFloor",
    "primaryBranchMap",
    "coverage",
}
REQUIRED_TOP_LEVEL = set(ALLOWED_TOP_LEVEL)
PARENT_ALLOWED = {
    "key",
    "name",
    "semantic_invariant",
    "surface_relation",
    "surprising_reach",
    "reading_type",
    "active_motifs",
    "synthesis",
    "ayah_refs",
    "subchannels",
}
SUBCHANNEL_ALLOWED = {
    "key",
    "name",
    "reading_type",
    "active_motifs",
    "synthesis",
    "ayah_refs",
}
ALLOWED_ANCHOR = {
    "anchorId",
    "ayahRef",
    "qacMorphemeRef",
    "surface_ar",
    "root_ar",
    "rootId",
    "rootOccurrenceStatus",
    "ambiguityReasons",
    "candidateRootIds",
    "recurrenceRefs",
}


def validate_data(data: object, expected_surah: int | None = None) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["bundle must be an object"]
    if data.get("schemaVersion") != "channel-bundle-v1":
        errors.append("schemaVersion must be channel-bundle-v1")
    if data.get("bundleType") != "combined-channel-commentary":
        errors.append("bundleType must be combined-channel-commentary")
    surah = data.get("surah")
    if not isinstance(surah, int) or not 1 <= surah <= 114:
        errors.append("surah must be an integer from 1 through 114")
    if expected_surah is not None and surah != expected_surah:
        errors.append(f"expected surah {expected_surah}, got {surah!r}")
    for key in REMOVED_TOP_LEVEL:
        if key in data:
            errors.append(f"{key} is redundant in the combined bundle")
    for key in sorted(set(data) - ALLOWED_TOP_LEVEL - REMOVED_TOP_LEVEL):
        errors.append(f"{key} is not part of the bundle contract")
    missing = REQUIRED_TOP_LEVEL - set(data)
    if missing:
        errors.append(f"bundle is missing required fields {sorted(missing)}")
    for key in ("text", "anchorInventory"):
        if not isinstance(data.get(key), list):
            errors.append(f"{key} must be an array")
    if isinstance(data.get("text"), list):
        for index, item in enumerate(data["text"]):
            where = f"text[{index}]"
            if not isinstance(item, dict) or set(item) != {
                "ayahRef",
                "arabic_uthmani",
            }:
                errors.append(f"{where} must contain only ayahRef and arabic_uthmani")
    if not isinstance(data.get("coverage"), dict):
        errors.append("coverage must be an object")

    review = data.get("reviewedChannels")
    if not isinstance(review, dict) or not isinstance(
        review.get("parent_channels"), list
    ):
        errors.append("reviewedChannels.parent_channels must be an array")
    else:
        if set(review) != {"parent_channels"}:
            errors.append("reviewedChannels may contain only parent_channels")
        for parent_index, parent in enumerate(review["parent_channels"]):
            where = f"reviewedChannels.parent_channels[{parent_index}]"
            if not isinstance(parent, dict):
                errors.append(f"{where} must be an object")
                continue
            extra = set(parent) - PARENT_ALLOWED
            if extra:
                errors.append(f"{where} contains forbidden fields {sorted(extra)}")
            if not re.fullmatch(r"P\d{2}", str(parent.get("key", ""))):
                errors.append(f"{where}.key is invalid")
            subchannels = parent.get("subchannels")
            if not isinstance(subchannels, list):
                errors.append(f"{where}.subchannels must be an array")
                continue
            for record_index, record in enumerate(subchannels or [parent]):
                record_where = f"{where}.records[{record_index}]"
                if not isinstance(record, dict):
                    errors.append(f"{record_where} must be an object")
                    continue
                allowed = PARENT_ALLOWED if record is parent else SUBCHANNEL_ALLOWED
                extra = set(record) - allowed
                if extra:
                    errors.append(
                        f"{record_where} contains forbidden fields {sorted(extra)}"
                    )
                for key in (
                    "name",
                    "reading_type",
                    "active_motifs",
                    "synthesis",
                    "ayah_refs",
                ):
                    if key not in record:
                        errors.append(f"{record_where}.{key} is required")

    anchor_keys: set[tuple[object, object, object]] = set()
    anchor_ids: set[str] = set()
    ambiguous_count = 0
    for index, item in enumerate(data.get("anchorInventory", [])):
        where = f"anchorInventory[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{where} must be an object")
            continue
        for key in sorted(set(item) - ALLOWED_ANCHOR):
            errors.append(f"{where}.{key} is not part of the anchor contract")
        anchor_id = item.get("anchorId")
        if not ANCHOR_ID.fullmatch(str(anchor_id or "")):
            errors.append(f"{where}.anchorId is invalid")
        elif anchor_id in anchor_ids:
            errors.append(f"{where}.anchorId is duplicated")
        else:
            anchor_ids.add(anchor_id)
        root_id = item.get("rootId")
        if not ROOT_ID.fullmatch(str(root_id or "")):
            errors.append(f"{where}.rootId is invalid")
        key = (item.get("ayahRef"), root_id, item.get("qacMorphemeRef"))
        if key in anchor_keys:
            errors.append(f"{where} duplicates an anchor identity")
        anchor_keys.add(key)
        status = item.get("rootOccurrenceStatus")
        if status not in {"resolved", "ambiguous-root"}:
            errors.append(f"{where}.rootOccurrenceStatus is invalid")
        if status == "ambiguous-root":
            ambiguous_count += 1
            reasons = item.get("ambiguityReasons")
            if not isinstance(reasons, list) or not reasons:
                errors.append(f"{where} ambiguous mapping requires ambiguityReasons")
            if "root-id" in (reasons or []):
                candidates = item.get("candidateRootIds")
                if (
                    not isinstance(candidates, list)
                    or len(set(candidates)) < 2
                    or root_id not in candidates
                ):
                    errors.append(f"{where} must retain every root-ID candidate")
            unknown_reasons = set(reasons or []) - {"root-id"}
            if unknown_reasons:
                errors.append(
                    f"{where} ambiguityReasons {sorted(unknown_reasons)} are not "
                    "identity ambiguities"
                )
        recurrence = item.get("recurrenceRefs")
        if recurrence is not None and (
            not isinstance(recurrence, list)
            or len(set(recurrence)) < 2
            or item.get("qacMorphemeRef") not in recurrence
        ):
            errors.append(f"{where}.recurrenceRefs must retain every occurrence")

    motif_map = data.get("motifAnchorMap")
    if not isinstance(motif_map, dict) or not motif_map:
        errors.append("motifAnchorMap must be a non-empty object")
    else:
        for root_ar, branches in motif_map.items():
            root_where = f"motifAnchorMap[{root_ar!r}]"
            if not str(root_ar).strip() or not isinstance(branches, dict):
                errors.append(f"{root_where} is invalid")
                continue
            for branch_id, motifs in branches.items():
                branch_where = f"{root_where}[{branch_id!r}]"
                if not BRANCH_ID.fullmatch(str(branch_id)):
                    errors.append(f"{branch_where} branch ID is invalid")
                if not isinstance(motifs, dict):
                    errors.append(f"{branch_where} must be an object")
                    continue
                for motif_id, mapping in motifs.items():
                    motif_where = f"{branch_where}[{motif_id!r}]"
                    if not MOTIF_ID.fullmatch(str(motif_id)):
                        errors.append(f"{motif_where} motif ID is invalid")
                    if not isinstance(mapping, dict):
                        errors.append(f"{motif_where} must be an object")
                        continue
                    refs = mapping.get("anchorIds")
                    extra = set(mapping) - {"anchorIds", "rootOccurrenceStatus"}
                    if extra:
                        errors.append(
                            f"{motif_where} contains forbidden keys {sorted(extra)}"
                        )
                    status = mapping.get("rootOccurrenceStatus")
                    if not isinstance(refs, list):
                        errors.append(f"{motif_where}.anchorIds must be an array")
                        continue
                    unknown = set(refs) - anchor_ids
                    if unknown:
                        errors.append(
                            f"{motif_where}.anchorIds contain unknown IDs {sorted(unknown)}"
                        )
                    if status not in {"resolved", "ambiguous-root", "unmatched"}:
                        errors.append(
                            f"{motif_where}.rootOccurrenceStatus is invalid"
                        )
                    if status == "unmatched" and refs:
                        errors.append(
                            f"{motif_where} unmatched mapping cannot carry anchors"
                        )
                    if status != "unmatched" and not refs:
                        errors.append(
                            f"{motif_where} matched mapping requires anchors"
                        )

    if isinstance(review, dict) and isinstance(motif_map, dict):
        citation_ar = re.compile(
            r"`?([ء-ي](?:\s+[ء-ي])*)\s*:\s*(B\d{3})(?:/(m\d+))?`?"
        )
        citation_id = re.compile(
            r"(root_\d{6})\s*[: ]\s*(B\d{3})(?:/(m\d+))?"
        )
        for parent_index, parent in enumerate(review.get("parent_channels", [])):
            records = parent.get("subchannels", []) or [parent]
            for record_index, record in enumerate(records):
                text = str(record.get("active_motifs", ""))
                citations = citation_ar.findall(text) + citation_id.findall(text)
                for root_key, branch_id, motif_id in citations:
                    if (
                        motif_id or "_"
                    ) not in motif_map.get(root_key, {}).get(branch_id, {}):
                        errors.append(
                            "reviewedChannels.parent_channels"
                            f"[{parent_index}].records[{record_index}] citation "
                            f"{root_key}:{branch_id}/{motif_id or '_'} has no motif mapping"
                        )

    floor = data.get("primaryFloor")
    if not isinstance(floor, dict):
        errors.append("primaryFloor must be an object")
    elif floor.get("status") == "authored":
        if not str(floor.get("sourcePath", "")).strip():
            errors.append("authored primaryFloor requires sourcePath")
        if not SHA256.fullmatch(str(floor.get("sourceSha256", ""))):
            errors.append("authored primaryFloor requires sourceSha256")
        if not isinstance(floor.get("lines"), list) or not floor["lines"]:
            errors.append("authored primaryFloor requires lines")
    elif floor != {"status": "arabic-only-inference"}:
        errors.append("arabic-only primaryFloor cannot carry invented content")

    primary_map = data.get("primaryBranchMap")
    if not isinstance(primary_map, dict):
        errors.append("primaryBranchMap must be an object")
    else:
        allowed_primary_map = {
            "status",
            "sourcePath",
            "sourceSha256",
            "coveredChannelAnchorCount",
            "channelAnchorCount",
            "entries",
        }
        extra = set(primary_map) - allowed_primary_map
        if extra:
            errors.append(f"primaryBranchMap has forbidden keys {sorted(extra)}")
        if primary_map.get("status") not in {
            "complete",
            "partial",
            "absent",
            "ambiguous-source",
            "invalid-source",
        }:
            errors.append("primaryBranchMap.status is invalid")
        entries = primary_map.get("entries")
        if not isinstance(entries, list):
            errors.append("primaryBranchMap.entries must be an array")
        else:
            seen_primary: set[tuple[object, object]] = set()
            for index, entry in enumerate(entries):
                where = f"primaryBranchMap.entries[{index}]"
                if not isinstance(entry, dict):
                    errors.append(f"{where} must be an object")
                    continue
                if set(entry) != {
                    "qacMorphemeRef",
                    "rootId",
                    "primaryBranchIds",
                }:
                    errors.append(f"{where} has invalid fields")
                key = (entry.get("qacMorphemeRef"), entry.get("rootId"))
                if key in seen_primary:
                    errors.append(f"{where} duplicates a primary occurrence")
                seen_primary.add(key)
                if not ROOT_ID.fullmatch(str(entry.get("rootId", ""))):
                    errors.append(f"{where}.rootId is invalid")
                branches = entry.get("primaryBranchIds")
                if (
                    not isinstance(branches, list)
                    or not branches
                    or any(not BRANCH_ID.fullmatch(str(item)) for item in branches)
                ):
                    errors.append(f"{where}.primaryBranchIds is invalid")

    coverage = data.get("coverage", {})
    if isinstance(coverage, dict):
        if set(coverage) != {
            "reviewedChannels",
            "primaryFloor",
            "primaryBranchMap",
            "identityMappings",
        }:
            errors.append("coverage must remain the compact four-part audit block")
        identity = coverage.get("identityMappings", {})
        if identity.get("anchorCount") != len(data.get("anchorInventory", [])):
            errors.append("coverage identity anchorCount is inconsistent")
        if identity.get("ambiguousAnchorCount") != ambiguous_count:
            errors.append("coverage ambiguousAnchorCount is inconsistent")
    return errors


def validate(path: Path, expected_surah: int | None = None) -> list[str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read JSON: {exc}"]
    return validate_data(data, expected_surah)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path)
    parser.add_argument("--surah", type=int)
    args = parser.parse_args()
    errors = validate(args.bundle, args.surah)
    if errors:
        print(f"FAIL {args.bundle}")
        for error in errors:
            print(f"  error: {error}")
        return 1
    print(f"ok   {args.bundle}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
