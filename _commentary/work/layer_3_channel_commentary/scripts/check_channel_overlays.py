#!/usr/bin/env python3
"""Validate Layer-2.5 overlays against a Layer-3 channel integration."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

WORK_ROOT = Path(__file__).resolve().parent.parent
ROOT = WORK_ROOT.parents[2]
VISIBLE_STATES = {"emerging", "mature", "complete"}
RELATIONS = {"supports-primary", "shifts-primary"}
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")

TOP_REQUIRED = {
    "schemaVersion",
    "surah",
    "sourceIntegration",
    "sourceIntegrationSha256",
    "baseLayer2Directory",
    "ayahs",
    "coverage",
}
AYAH_REQUIRED = {"ayahRef", "baseProse", "baseProseSha256", "insertions"}
INSERTION_REQUIRED = {
    "insertionId",
    "channelId",
    "stage",
    "placement",
    "newMemberIds",
    "recalledMemberIds",
    "focusAyahRelation",
    "focusAyahShift_tr",
    "prose_tr",
}
PLACEMENT_REQUIRED = {"afterParagraph", "afterPhrase"}
COVERAGE_REQUIRED = {
    "integratedChannelIds",
    "insertedChannelIds",
    "omitted",
}
OMITTED_REQUIRED = {"channelId", "ayahRef", "reason"}


def object_shape(
    value: object,
    where: str,
    required: set[str],
    allowed: set[str],
    errors: list[str],
) -> bool:
    if not isinstance(value, dict):
        errors.append(f"{where}: must be an object")
        return False
    missing = required - set(value)
    extra = set(value) - allowed
    if missing:
        errors.append(f"{where}: missing required fields {sorted(missing)}")
    if extra:
        errors.append(f"{where}: forbidden fields {sorted(extra)}")
    return not missing and not extra


def resolve(path_value: str, parent: Path) -> Path:
    path = Path(path_value)
    if path.is_absolute():
        return path
    local = parent / path
    return local if local.exists() else ROOT / path


def paragraphs(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"\n[ \t]*\n", text) if part.strip()]


def validate(overlay_path: Path, integration_path: Path) -> list[str]:
    errors: list[str] = []
    try:
        overlay = json.loads(overlay_path.read_text(encoding="utf-8"))
        integration = json.loads(integration_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read JSON: {exc}"]

    if not object_shape(
        overlay, "overlay", TOP_REQUIRED, TOP_REQUIRED, errors
    ):
        if not isinstance(overlay, dict):
            return errors
    if overlay.get("schemaVersion") != "ayah-channel-overlays-v1":
        errors.append("overlay: schemaVersion must be ayah-channel-overlays-v1")
    if integration.get("schemaVersion") != "surah-channel-integration-v1":
        errors.append(
            "integration: schemaVersion must be surah-channel-integration-v1"
        )
    if overlay.get("surah") != integration.get("surah"):
        errors.append("overlay and integration name different surahs")

    declared_integration = overlay.get("sourceIntegration")
    if not isinstance(declared_integration, str) or not declared_integration:
        errors.append("overlay: sourceIntegration is required")
    else:
        resolved_integration = resolve(declared_integration, overlay_path.parent)
        if resolved_integration.resolve() != integration_path.resolve():
            errors.append("overlay: sourceIntegration does not match validated file")
    actual_integration_sha = hashlib.sha256(integration_path.read_bytes()).hexdigest()
    if overlay.get("sourceIntegrationSha256") != actual_integration_sha:
        errors.append(
            "overlay: sourceIntegrationSha256 does not match integration file"
        )
    expected_ayah_refs: set[str] | None = None
    source_bundle_value = integration.get("sourceBundle")
    if isinstance(source_bundle_value, str):
        source_bundle_path = resolve(source_bundle_value, integration_path.parent)
        try:
            source_bundle = json.loads(source_bundle_path.read_text(encoding="utf-8"))
            expected_ayah_refs = {
                item.get("ayahRef")
                for item in source_bundle.get("text", [])
                if isinstance(item, dict)
                and isinstance(item.get("ayahRef"), str)
                and not item["ayahRef"].endswith(":0")
            }
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"integration: cannot read sourceBundle: {exc}")

    base_directory_value = overlay.get("baseLayer2Directory")
    if not isinstance(base_directory_value, str) or not base_directory_value:
        errors.append("overlay: baseLayer2Directory is required")
        base_directory = None
    else:
        base_directory = resolve(base_directory_value, overlay_path.parent)
        if not base_directory.is_dir():
            errors.append("overlay: baseLayer2Directory is not a directory")
            base_directory = None

    integrated = {
        channel.get("channelId"): channel
        for channel in integration.get("channels", [])
        if isinstance(channel, dict)
    }
    member_ids = {
        channel_id: {
            member.get("memberId")
            for member in channel.get("members", [])
            if isinstance(member, dict)
        }
        for channel_id, channel in integrated.items()
    }
    maturity = {
        (channel_id, entry.get("ayahRef")): entry
        for channel_id, channel in integrated.items()
        for entry in channel.get("maturityByAyah", [])
        if isinstance(entry, dict)
    }

    insertion_ids: set[str] = set()
    inserted_channels: set[str] = set()
    inserted_points: set[tuple[str, str]] = set()
    ayah_refs: set[str] = set()
    ayahs = overlay.get("ayahs")
    if not isinstance(ayahs, list):
        errors.append("overlay: ayahs must be an array")
        ayahs = []
    for ai, ayah in enumerate(ayahs):
        where = f"ayahs[{ai}]"
        if not object_shape(ayah, where, AYAH_REQUIRED, AYAH_REQUIRED, errors):
            if not isinstance(ayah, dict):
                continue
        ayah_ref = ayah.get("ayahRef")
        if not re.fullmatch(r"[1-9]\d{0,2}:[1-9]\d{0,2}", str(ayah_ref or "")):
            errors.append(f"{where}: invalid ayahRef")
        if ayah_ref in ayah_refs:
            errors.append(f"{where}: duplicate ayahRef {ayah_ref!r}")
        ayah_refs.add(ayah_ref)

        base_value = ayah.get("baseProse")
        base_parts: list[str] = []
        if not isinstance(base_value, str) or not base_value:
            errors.append(f"{where}: baseProse is required")
        else:
            base_path = resolve(base_value, overlay_path.parent)
            if not base_path.is_file():
                errors.append(f"{where}: baseProse does not exist: {base_value}")
            else:
                if base_directory is not None:
                    try:
                        base_path.resolve().relative_to(base_directory.resolve())
                    except ValueError:
                        errors.append(
                            f"{where}: baseProse is outside baseLayer2Directory"
                        )
                actual_sha = hashlib.sha256(base_path.read_bytes()).hexdigest()
                if ayah.get("baseProseSha256") != actual_sha:
                    errors.append(f"{where}: baseProseSha256 does not match file")
                base_parts = paragraphs(base_path.read_text(encoding="utf-8"))

        insertions = ayah.get("insertions")
        if not isinstance(insertions, list):
            errors.append(f"{where}: insertions must be an array")
            insertions = []
        for ii, insertion in enumerate(insertions):
            iwhere = f"{where}.insertions[{ii}]"
            if not object_shape(
                insertion,
                iwhere,
                INSERTION_REQUIRED,
                INSERTION_REQUIRED,
                errors,
            ):
                if not isinstance(insertion, dict):
                    continue
            insertion_id = insertion.get("insertionId")
            if not isinstance(insertion_id, str) or not ID_RE.fullmatch(insertion_id):
                errors.append(f"{iwhere}: invalid insertionId")
            elif insertion_id in insertion_ids:
                errors.append(f"{iwhere}: duplicate insertionId {insertion_id!r}")
            insertion_ids.add(insertion_id)

            channel_id = insertion.get("channelId")
            if channel_id not in integrated:
                errors.append(
                    f"{iwhere}: channel {channel_id!r} is not in integration"
                )
                continue
            inserted_channels.add(channel_id)
            inserted_points.add((channel_id, ayah_ref))
            stage = maturity.get((channel_id, ayah_ref))
            if stage is None:
                errors.append(
                    f"{iwhere}: no derived maturity entry for channel/ayah"
                )
                continue
            if stage.get("state") not in VISIBLE_STATES:
                errors.append(f"{iwhere}: insertion cannot disclose a latent channel")
            if insertion.get("stage") != stage.get("state"):
                errors.append(f"{iwhere}: stage differs from derived maturity")
            for field in ("newMemberIds", "recalledMemberIds"):
                if not isinstance(insertion.get(field), list):
                    errors.append(f"{iwhere}: {field} must be an array")
            unknown = (
                set(insertion.get("newMemberIds", []))
                | set(insertion.get("recalledMemberIds", []))
            ) - member_ids[channel_id]
            if unknown:
                errors.append(f"{iwhere}: unknown member IDs {sorted(unknown)}")
            if not set(insertion.get("newMemberIds", [])) <= set(
                stage.get("newMemberIds", [])
            ):
                errors.append(f"{iwhere}: newMemberIds exceed maturity entry")
            if not set(insertion.get("recalledMemberIds", [])) <= set(
                stage.get("recalledMemberIds", [])
            ):
                errors.append(f"{iwhere}: recalledMemberIds exceed maturity entry")
            if insertion.get("focusAyahRelation") != stage.get(
                "focusAyahRelation"
            ):
                errors.append(f"{iwhere}: focus relation differs from integration")
            if insertion.get("focusAyahRelation") not in RELATIONS:
                errors.append(f"{iwhere}: invalid focusAyahRelation")
            for field in ("focusAyahShift_tr", "prose_tr"):
                if not str(insertion.get(field, "")).strip():
                    errors.append(f"{iwhere}: {field} is empty")

            placement = insertion.get("placement")
            if not object_shape(
                placement,
                f"{iwhere}.placement",
                PLACEMENT_REQUIRED,
                PLACEMENT_REQUIRED,
                errors,
            ):
                placement = {} if not isinstance(placement, dict) else placement
            after = placement.get("afterParagraph")
            if (
                not isinstance(after, int)
                or after < 1
                or (base_parts and after > len(base_parts))
            ):
                errors.append(f"{iwhere}: afterParagraph is outside base prose")
            phrase = placement.get("afterPhrase")
            if phrase is not None and not isinstance(phrase, str):
                errors.append(f"{iwhere}: afterPhrase must be string or null")
            elif phrase:
                if (
                    base_parts
                    and isinstance(after, int)
                    and 1 <= after <= len(base_parts)
                    and phrase not in base_parts[after - 1]
                ):
                    errors.append(
                        f"{iwhere}: afterPhrase is not in selected paragraph"
                    )
    if expected_ayah_refs is not None and ayah_refs != expected_ayah_refs:
        errors.append(
            "overlay: ayahs must cover the complete surah; "
            f"missing={sorted(expected_ayah_refs - ayah_refs)}, "
            f"extra={sorted(ayah_refs - expected_ayah_refs)}"
        )

    coverage = overlay.get("coverage")
    if not object_shape(
        coverage,
        "coverage",
        COVERAGE_REQUIRED,
        COVERAGE_REQUIRED,
        errors,
    ):
        coverage = {} if not isinstance(coverage, dict) else coverage
    integrated_ids = set(coverage.get("integratedChannelIds", []))
    if integrated_ids != set(integrated):
        errors.append("coverage: integratedChannelIds do not match integration")
    if set(coverage.get("insertedChannelIds", [])) != inserted_channels:
        errors.append("coverage: insertedChannelIds do not match insertions")

    omitted_points: set[tuple[str, str]] = set()
    omitted = coverage.get("omitted")
    if not isinstance(omitted, list):
        errors.append("coverage: omitted must be an array")
        omitted = []
    for index, item in enumerate(omitted):
        where = f"coverage.omitted[{index}]"
        if not object_shape(
            item, where, OMITTED_REQUIRED, OMITTED_REQUIRED, errors
        ):
            if not isinstance(item, dict):
                continue
        if item.get("channelId") not in integrated:
            errors.append(f"{where}: unknown channelId")
        if not str(item.get("reason", "")).strip():
            errors.append(f"{where}: reason is empty")
        omitted_points.add((item.get("channelId"), item.get("ayahRef")))

    eligible = {
        (channel_id, entry.get("ayahRef"))
        for channel_id, channel in integrated.items()
        for entry in channel.get("maturityByAyah", [])
        if entry.get("state") in VISIBLE_STATES and entry.get("newMemberIds")
    }
    uncovered = eligible - inserted_points - omitted_points
    if uncovered:
        errors.append(
            "coverage: eligible channel/ayah points neither inserted nor omitted: "
            f"{sorted(uncovered)}"
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("overlays", type=Path)
    parser.add_argument("--integration", type=Path, required=True)
    args = parser.parse_args()
    overlay_path = (
        args.overlays if args.overlays.is_absolute() else ROOT / args.overlays
    )
    integration_path = (
        args.integration
        if args.integration.is_absolute()
        else ROOT / args.integration
    )
    errors = validate(overlay_path, integration_path)
    if errors:
        print(f"FAIL {overlay_path}")
        for error in errors:
            print(f"  error: {error}")
        return 1
    data = json.loads(overlay_path.read_text(encoding="utf-8"))
    count = sum(
        len(ayah.get("insertions", [])) for ayah in data.get("ayahs", [])
    )
    print(f"ok   {overlay_path}  surah={data['surah']} insertions={count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
