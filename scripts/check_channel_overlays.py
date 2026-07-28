#!/usr/bin/env python3
"""Validate Layer-2.5 channel overlays against a reviewed channel plan."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VISIBLE_STATES = {"emerging", "mature", "complete"}


def resolve(path_value: str, parent: Path) -> Path:
    path = Path(path_value)
    if path.is_absolute():
        return path
    local = parent / path
    return local if local.exists() else ROOT / path


def paragraphs(text: str) -> list[str]:
    return [part.strip() for part in text.split("\n\n") if part.strip()]


def validate(overlay_path: Path, plan_path: Path) -> list[str]:
    errors: list[str] = []
    try:
        overlay = json.loads(overlay_path.read_text(encoding="utf-8"))
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read JSON: {exc}"]

    if overlay.get("schemaVersion") != "ayah-channel-overlays-v1":
        errors.append("overlay: schemaVersion must be ayah-channel-overlays-v1")
    if plan.get("schemaVersion") != "surah-channel-plan-v1":
        errors.append("plan: schemaVersion must be surah-channel-plan-v1")
    if plan.get("reviewState") != "reviewed":
        errors.append("plan: Layer 2.5 accepts only reviewState=reviewed")
    if overlay.get("sourceReviewState") != "reviewed":
        errors.append("overlay: sourceReviewState must be reviewed")
    if overlay.get("surah") != plan.get("surah"):
        errors.append("overlay and plan name different surahs")

    accepted = {
        channel.get("channelId"): channel
        for channel in plan.get("channels", [])
        if channel.get("reviewDecision") == "accepted"
    }
    member_ids = {
        channel_id: {member.get("memberId") for member in channel.get("members", [])}
        for channel_id, channel in accepted.items()
    }
    maturity = {
        (channel_id, entry.get("ayahRef")): entry
        for channel_id, channel in accepted.items()
        for entry in channel.get("maturityByAyah", [])
    }

    insertion_ids: set[str] = set()
    inserted_channels: set[str] = set()
    inserted_points: set[tuple[str, str]] = set()
    ayah_refs: set[str] = set()
    for ai, ayah in enumerate(overlay.get("ayahs", [])):
        where = f"ayahs[{ai}]"
        ayah_ref = ayah.get("ayahRef")
        if ayah_ref in ayah_refs:
            errors.append(f"{where}: duplicate ayahRef {ayah_ref!r}")
        ayah_refs.add(ayah_ref)
        base_value = ayah.get("baseProse")
        if not isinstance(base_value, str) or not base_value:
            errors.append(f"{where}: baseProse is required")
            base_parts: list[str] = []
        else:
            base_path = resolve(base_value, overlay_path.parent)
            if not base_path.is_file():
                errors.append(f"{where}: baseProse does not exist: {base_value}")
                base_parts = []
            else:
                base_parts = paragraphs(base_path.read_text(encoding="utf-8"))

        for ii, insertion in enumerate(ayah.get("insertions", [])):
            iwhere = f"{where}.insertions[{ii}]"
            insertion_id = insertion.get("insertionId")
            if insertion_id in insertion_ids:
                errors.append(f"{iwhere}: duplicate insertionId {insertion_id!r}")
            insertion_ids.add(insertion_id)
            channel_id = insertion.get("channelId")
            if channel_id not in accepted:
                errors.append(f"{iwhere}: channel {channel_id!r} is not accepted")
                continue
            inserted_channels.add(channel_id)
            inserted_points.add((channel_id, ayah_ref))
            stage = maturity.get((channel_id, ayah_ref))
            if stage is None:
                errors.append(f"{iwhere}: no reviewed maturity entry for this channel/ayah")
                continue
            if stage.get("state") not in VISIBLE_STATES:
                errors.append(f"{iwhere}: an insertion cannot disclose a latent channel")
            if insertion.get("stage") != stage.get("state"):
                errors.append(
                    f"{iwhere}: stage {insertion.get('stage')!r} does not match reviewed "
                    f"state {stage.get('state')!r}"
                )
            unknown = (
                set(insertion.get("newMemberIds", []))
                | set(insertion.get("recalledMemberIds", []))
            ) - member_ids[channel_id]
            if unknown:
                errors.append(f"{iwhere}: unknown member IDs {sorted(unknown)}")
            if not set(insertion.get("newMemberIds", [])) <= set(stage.get("newMemberIds", [])):
                errors.append(f"{iwhere}: newMemberIds were not introduced at this ayah")
            if not set(insertion.get("recalledMemberIds", [])) <= set(stage.get("recalledMemberIds", [])):
                errors.append(f"{iwhere}: recalledMemberIds exceed the reviewed disclosure")
            if insertion.get("focusAyahRelation") != stage.get("focusAyahRelation"):
                errors.append(f"{iwhere}: focusAyahRelation differs from reviewed plan")
            if not str(insertion.get("focusAyahShift_tr", "")).strip():
                errors.append(f"{iwhere}: focusAyahShift_tr is empty")
            if not str(insertion.get("prose_tr", "")).strip():
                errors.append(f"{iwhere}: prose_tr is empty")

            placement = insertion.get("placement", {})
            after = placement.get("afterParagraph")
            if not isinstance(after, int) or after < 1 or (base_parts and after > len(base_parts)):
                errors.append(f"{iwhere}: afterParagraph is outside the base prose")
            phrase = placement.get("afterPhrase")
            if isinstance(phrase, str) and phrase:
                if not base_parts or not isinstance(after, int) or after > len(base_parts):
                    continue
                if phrase not in base_parts[after - 1]:
                    errors.append(f"{iwhere}: afterPhrase is not in the selected paragraph")

    coverage = overlay.get("coverage", {})
    accepted_ids = set(coverage.get("acceptedChannelIds", []))
    if accepted_ids != set(accepted):
        errors.append(
            f"coverage: acceptedChannelIds {sorted(accepted_ids)} do not match plan "
            f"{sorted(accepted)}"
        )
    if set(coverage.get("insertedChannelIds", [])) != inserted_channels:
        errors.append("coverage: insertedChannelIds do not match actual insertions")
    omitted_points = {
        (item.get("channelId"), item.get("ayahRef"))
        for item in coverage.get("omitted", [])
        if isinstance(item, dict) and str(item.get("reason", "")).strip()
    }
    eligible = {
        (channel_id, entry.get("ayahRef"))
        for channel_id, channel in accepted.items()
        for entry in channel.get("maturityByAyah", [])
        if entry.get("state") in VISIBLE_STATES and entry.get("newMemberIds")
    }
    uncovered = eligible - inserted_points - omitted_points
    if uncovered:
        errors.append(f"coverage: eligible channel/ayah points neither inserted nor omitted: {sorted(uncovered)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("overlays", type=Path)
    parser.add_argument("--plan", type=Path, required=True)
    args = parser.parse_args()
    overlay_path = args.overlays if args.overlays.is_absolute() else ROOT / args.overlays
    plan_path = args.plan if args.plan.is_absolute() else ROOT / args.plan
    errors = validate(overlay_path, plan_path)
    if errors:
        print(f"FAIL {overlay_path}")
        for error in errors:
            print(f"  error: {error}")
        return 1
    data = json.loads(overlay_path.read_text(encoding="utf-8"))
    count = sum(len(ayah.get("insertions", [])) for ayah in data.get("ayahs", []))
    print(f"ok   {overlay_path}  surah={data['surah']} insertions={count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
