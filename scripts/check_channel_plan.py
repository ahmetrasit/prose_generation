#!/usr/bin/env python3
"""Validate a draft or reviewed surah channel plan.

Standard-library validation covers the cross-record rules JSON Schema cannot:
surah identity, stable-ID uniqueness, cross-ayah recurrence, member/maturity
joins, reading-order monotonicity, and review-state consistency.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ROOT_RE = re.compile(r"^root_[0-9]{6}$")
BRANCH_RE = re.compile(r"^B[0-9]{3}$")
QAC_RE = re.compile(r"^([1-9][0-9]{0,2}):([1-9][0-9]{0,2}):[1-9][0-9]*:[1-9][0-9]*$")
STATES = {"latent": 0, "emerging": 1, "mature": 2, "complete": 3}
RELATIONS = {"supports-primary", "shifts-primary"}


def fail(errors: list[str], where: str, message: str) -> None:
    errors.append(f"{where}: {message}")


def ayah_number(ref: object, surah: int, errors: list[str], where: str) -> int | None:
    if not isinstance(ref, str):
        fail(errors, where, "ayahRef must be a string")
        return None
    match = re.fullmatch(r"([1-9][0-9]{0,2}):([1-9][0-9]{0,2})", ref)
    if not match:
        fail(errors, where, f"invalid ayahRef {ref!r}")
        return None
    if int(match.group(1)) != surah:
        fail(errors, where, f"ayahRef {ref!r} belongs to another surah")
    return int(match.group(2))


def bundle_members(bundle_path: Path) -> tuple[set[tuple[str, str, str]], list[str]]:
    errors: list[str] = []
    try:
        bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return set(), [f"bundle: cannot read JSON: {exc}"]
    anchors = {
        item.get("anchorId"): item
        for item in bundle.get("anchorInventory", [])
        if isinstance(item, dict)
        and (
            item.get("rootOccurrenceStatus") == "resolved"
            or item.get("mappingStatus") == "exact"
        )
    }
    allowed: set[tuple[str, str, str]] = set()
    motif_map = bundle.get("motifAnchorMap", {})
    if not isinstance(motif_map, dict):
        return set(), ["bundle: motifAnchorMap must be an object"]
    for branches in motif_map.values():
        if not isinstance(branches, dict):
            continue
        for branch_id, motifs in branches.items():
            if not isinstance(motifs, dict):
                continue
            for mapping in motifs.values():
                if (
                    not isinstance(mapping, dict)
                    or (
                        mapping.get("rootOccurrenceStatus") != "resolved"
                        and mapping.get("mappingStatus") != "exact"
                    )
                ):
                    continue
                for anchor_id in mapping.get("anchorIds", []):
                    anchor = anchors.get(anchor_id)
                    if anchor:
                        allowed.add(
                            (
                                anchor.get("qacMorphemeRef"),
                                anchor.get("rootId"),
                                branch_id,
                            )
                        )
    if not allowed:
        errors.append("bundle: no exact channel-member triples are available")
    return allowed, errors


def bundle_source_refs(bundle_path: Path) -> tuple[set[str], list[str]]:
    try:
        bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return set(), [f"bundle: cannot read JSON: {exc}"]
    refs = set()
    for parent in bundle.get("reviewedChannels", {}).get("parent_channels", []):
        parent_ref = parent.get("key")
        if not isinstance(parent_ref, str):
            continue
        subchannels = parent.get("subchannels", [])
        if subchannels:
            refs.update(
                f"{parent_ref}/{subchannel.get('key')}"
                for subchannel in subchannels
                if isinstance(subchannel, dict)
                and isinstance(subchannel.get("key"), str)
            )
        else:
            refs.add(parent_ref)
    return refs, ([] if refs else ["bundle: no reviewed channel source refs"])


def validate(
    path: Path,
    expected_state: str | None = None,
    bundle_path: Path | None = None,
) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: cannot read JSON: {exc}"]

    if data.get("schemaVersion") != "surah-channel-plan-v1":
        fail(errors, "plan", "schemaVersion must be surah-channel-plan-v1")
    surah = data.get("surah")
    if not isinstance(surah, int) or not 1 <= surah <= 114:
        fail(errors, "plan", "surah must be an integer from 1 through 114")
        return errors

    review_state = data.get("reviewState")
    if review_state not in {"draft", "reviewed"}:
        fail(errors, "plan", "reviewState must be draft or reviewed")
    if expected_state and review_state != expected_state:
        fail(errors, "plan", f"expected reviewState {expected_state!r}, got {review_state!r}")
    if review_state == "reviewed" and not isinstance(data.get("review"), dict):
        fail(errors, "plan", "reviewed plans require a review object")
    if review_state == "draft" and "review" in data:
        fail(errors, "plan", "draft plans must not contain a review object")
    source_lane = data.get("sourceLane")
    channel_lane = source_lane == "channel-only"
    combined_lane = source_lane == "combined"
    if combined_lane and review_state != "reviewed":
        fail(errors, "plan", "combined plans must have reviewState=reviewed")
    allowed_members: set[tuple[str, str, str]] | None = None
    expected_source_refs: set[str] | None = None
    if combined_lane:
        if bundle_path is None:
            fail(errors, "plan", "combined validation requires the source channel bundle")
        else:
            allowed_members, bundle_errors = bundle_members(bundle_path)
            errors.extend(bundle_errors)
            expected_source_refs, source_errors = bundle_source_refs(bundle_path)
            errors.extend(source_errors)
    if channel_lane or combined_lane:
        basis = data.get("primaryFloorBasis")
        if not isinstance(basis, dict):
            fail(errors, "plan", f"{source_lane} plans require primaryFloorBasis")
        else:
            status = basis.get("status")
            apparatus = basis.get("apparatusStatus")
            if status == "authored":
                if not str(basis.get("sourcePath", "")).strip():
                    fail(errors, "plan", "authored primary floor requires sourcePath")
                if not re.fullmatch(r"[0-9a-f]{64}", str(basis.get("sourceSha256", ""))):
                    fail(errors, "plan", "authored primary floor requires sourceSha256")
                if apparatus != "typed-primary-floor":
                    fail(errors, "plan", "authored primary floor requires typed-primary-floor apparatus")
            elif status == "arabic-only-inference":
                if "sourcePath" in basis or "sourceSha256" in basis:
                    fail(errors, "plan", "arabic-only primary floor cannot cite an authored source")
                if apparatus != "writer-primary-inference":
                    fail(errors, "plan", "arabic-only primary floor requires writer-primary-inference apparatus")
            else:
                fail(errors, "plan", "invalid primary-floor status")

    channels = data.get("channels")
    if not isinstance(channels, list):
        fail(errors, "plan", "channels must be an array")
        return errors

    channel_ids: set[str] = set()
    for ci, channel in enumerate(channels):
        where = f"channels[{ci}]"
        if not isinstance(channel, dict):
            fail(errors, where, "channel must be an object")
            continue
        channel_id = channel.get("channelId")
        if not isinstance(channel_id, str) or not ID_RE.fullmatch(channel_id):
            fail(errors, where, f"invalid channelId {channel_id!r}")
        elif channel_id in channel_ids:
            fail(errors, where, f"duplicate channelId {channel_id!r}")
        else:
            channel_ids.add(channel_id)

        decision = channel.get("reviewDecision")
        if review_state == "draft" and decision != "draft":
            fail(errors, where, "draft plan channels must have reviewDecision=draft")
        if review_state == "reviewed" and decision not in {"accepted", "rejected", "revise"}:
            fail(errors, where, "reviewed plan channels cannot retain a draft decision")
        enforce_admission = review_state == "draft" or decision == "accepted"
        if channel.get("wholeSurahRelation") not in RELATIONS:
            fail(errors, where, "invalid wholeSurahRelation")
        if not str(channel.get("wholeSurahShift_tr", "")).strip():
            fail(errors, where, "wholeSurahShift_tr is empty")
        if not isinstance(channel.get("sourceCandidates"), list) or not channel["sourceCandidates"]:
            fail(errors, where, "at least one sourceCandidate is required")

        members = channel.get("members")
        if not isinstance(members, list) or len(members) < 2:
            fail(errors, where, "a channel requires at least two members")
            continue

        member_ids: set[str] = set()
        member_ayah: dict[str, int] = {}
        non_primary = 0
        for mi, member in enumerate(members):
            mwhere = f"{where}.members[{mi}]"
            if not isinstance(member, dict):
                fail(errors, mwhere, "member must be an object")
                continue
            member_id = member.get("memberId")
            if not isinstance(member_id, str) or not ID_RE.fullmatch(member_id):
                fail(errors, mwhere, f"invalid memberId {member_id!r}")
                continue
            if member_id in member_ids:
                fail(errors, mwhere, f"duplicate memberId {member_id!r}")
            member_ids.add(member_id)
            number = ayah_number(member.get("ayahRef"), surah, errors, mwhere)
            if number is not None:
                member_ayah[member_id] = number
            qac = member.get("qacMorphemeRef")
            match = QAC_RE.fullmatch(qac) if isinstance(qac, str) else None
            if not match:
                fail(errors, mwhere, f"invalid qacMorphemeRef {qac!r}")
            elif number is not None and (int(match.group(1)), int(match.group(2))) != (surah, number):
                fail(errors, mwhere, "qacMorphemeRef does not match ayahRef")
            if not ROOT_RE.fullmatch(str(member.get("rootId", ""))):
                fail(errors, mwhere, f"invalid rootId {member.get('rootId')!r}")
            if not BRANCH_RE.fullmatch(str(member.get("branchId", ""))):
                fail(errors, mwhere, f"invalid branchId {member.get('branchId')!r}")
            if allowed_members is not None and (
                member.get("qacMorphemeRef"),
                member.get("rootId"),
                member.get("branchId"),
            ) not in allowed_members:
                fail(
                    errors,
                    mwhere,
                    "member does not resolve to an exact reviewed "
                    "qacMorphemeRef + rootId + branchId bundle mapping",
                )
            if member.get("primaryStatus") == "non-primary":
                non_primary += 1
            if not isinstance(member.get("evidenceRefs"), list) or not member["evidenceRefs"]:
                fail(errors, mwhere, "evidenceRefs must be non-empty")
        distinct_ayahs = set(member_ayah.values())
        if enforce_admission and len(distinct_ayahs) < 2:
            fail(errors, where, "members do not recur across at least two ayahs")
        if enforce_admission and non_primary == 0:
            fail(errors, where, "no member is marked non-primary")

        maturity = channel.get("maturityByAyah")
        deferred_maturity = channel_lane and review_state == "draft"
        if deferred_maturity:
            if channel.get("maturityStatus") != "deferred-to-review":
                fail(
                    errors,
                    where,
                    "channel-only drafts require maturityStatus=deferred-to-review",
                )
            if maturity != []:
                fail(
                    errors,
                    where,
                    "channel-only draft maturity must be an empty deferred array",
                )
            continue
        if review_state == "reviewed" and (channel_lane or combined_lane):
            if channel.get("maturityStatus") != "reviewed":
                fail(
                    errors,
                    where,
                    f"reviewed {source_lane} plans require maturityStatus=reviewed",
                )
        if not isinstance(maturity, list) or not maturity:
            fail(errors, where, "maturityByAyah must be non-empty")
            continue
        seen_refs: set[str] = set()
        seen_members: set[str] = set()
        previous_ayah = 0
        previous_state = -1
        for ai, entry in enumerate(maturity):
            awhere = f"{where}.maturityByAyah[{ai}]"
            if not isinstance(entry, dict):
                fail(errors, awhere, "maturity entry must be an object")
                continue
            ref = entry.get("ayahRef")
            number = ayah_number(ref, surah, errors, awhere)
            if isinstance(ref, str) and ref in seen_refs:
                fail(errors, awhere, f"duplicate maturity ayah {ref}")
            if isinstance(ref, str):
                seen_refs.add(ref)
            if number is not None and number <= previous_ayah:
                fail(errors, awhere, "maturityByAyah is not in reading order")
            if number is not None:
                previous_ayah = number
            state = entry.get("state")
            if state not in STATES:
                fail(errors, awhere, f"invalid state {state!r}")
                continue
            if enforce_admission and STATES[state] < previous_state:
                fail(errors, awhere, "maturity runs backwards")
            previous_state = STATES[state]

            new_ids = entry.get("newMemberIds")
            recalled_ids = entry.get("recalledMemberIds")
            if not isinstance(new_ids, list) or not isinstance(recalled_ids, list):
                fail(errors, awhere, "newMemberIds and recalledMemberIds must be arrays")
                continue
            expected_new = {
                member_id for member_id, member_at in member_ayah.items() if member_at == number
            }
            if set(new_ids) != expected_new:
                fail(
                    errors,
                    awhere,
                    f"newMemberIds {sorted(set(new_ids))} do not match members anchored here {sorted(expected_new)}",
                )
            unknown = (set(new_ids) | set(recalled_ids)) - member_ids
            if unknown:
                fail(errors, awhere, f"unknown member IDs: {sorted(unknown)}")
            if not set(recalled_ids) <= seen_members:
                fail(errors, awhere, "recalledMemberIds includes a member not yet encountered")
            seen_members.update(new_ids)
            if enforce_admission and len(seen_members) <= 1 and state != "latent":
                fail(errors, awhere, "a channel with at most one encountered member must be latent")
            if enforce_admission and state == "latent" and len(seen_members) > 1:
                if entry.get("relationStatus") != "not-yet-statable":
                    fail(
                        errors,
                        awhere,
                        "latent with two or more encountered members requires relationStatus=not-yet-statable",
                    )
                if "focusAyahRelation" in entry or str(entry.get("focusAyahShift_tr", "")).strip():
                    fail(errors, awhere, "a not-yet-statable latent relation cannot carry a focus relation")
            if enforce_admission and state == "complete" and seen_members != member_ids:
                fail(errors, awhere, "complete is declared before every member appears")
            if enforce_admission and state != "latent" and new_ids:
                if entry.get("relationStatus") not in {None, "statable"}:
                    fail(errors, awhere, "a non-latent member arrival must have a statable relation")
                if entry.get("focusAyahRelation") not in RELATIONS:
                    fail(errors, awhere, "non-latent member arrival requires focusAyahRelation")
                if not str(entry.get("focusAyahShift_tr", "")).strip():
                    fail(errors, awhere, "non-latent member arrival requires focusAyahShift_tr")

        if enforce_admission and set(member_ayah) != seen_members:
            fail(errors, where, "maturityByAyah does not introduce every member exactly at its ayah")
        if enforce_admission and previous_state != STATES["complete"]:
            fail(errors, where, "maturityByAyah must end at complete")

    if combined_lane:
        coverage = data.get("sourceCoverage")
        if not isinstance(coverage, list):
            fail(errors, "plan", "combined plans require sourceCoverage")
        else:
            seen_refs: set[str] = set()
            for index, item in enumerate(coverage):
                where = f"sourceCoverage[{index}]"
                if not isinstance(item, dict):
                    fail(errors, where, "entry must be an object")
                    continue
                source_ref = item.get("sourceRef")
                if not isinstance(source_ref, str):
                    fail(errors, where, "sourceRef must be a string")
                    continue
                if source_ref in seen_refs:
                    fail(errors, where, f"duplicate sourceRef {source_ref!r}")
                seen_refs.add(source_ref)
                disposition = item.get("disposition")
                linked = item.get("channelIds")
                if disposition not in {"integrated", "apparatus-only"}:
                    fail(errors, where, "invalid disposition")
                if not isinstance(linked, list):
                    fail(errors, where, "channelIds must be an array")
                    continue
                unknown = set(linked) - channel_ids
                if unknown:
                    fail(errors, where, f"unknown channel IDs {sorted(unknown)}")
                if disposition == "integrated" and not linked:
                    fail(errors, where, "integrated sources require channelIds")
                if disposition == "apparatus-only":
                    if linked:
                        fail(errors, where, "apparatus-only sources cannot name channelIds")
                    if not str(item.get("reason_tr", "")).strip():
                        fail(errors, where, "apparatus-only sources require reason_tr")
            if expected_source_refs is not None and seen_refs != expected_source_refs:
                missing = sorted(expected_source_refs - seen_refs)
                extra = sorted(seen_refs - expected_source_refs)
                fail(
                    errors,
                    "sourceCoverage",
                    f"must account for every reviewed source; missing={missing}, extra={extra}",
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--state", choices=("draft", "reviewed"), default=None)
    parser.add_argument("--bundle", type=Path)
    args = parser.parse_args()
    path = args.plan if args.plan.is_absolute() else ROOT / args.plan
    bundle_path = None
    if args.bundle is not None:
        bundle_path = args.bundle if args.bundle.is_absolute() else ROOT / args.bundle
    errors = validate(path, args.state, bundle_path)
    if errors:
        print(f"FAIL {path}")
        for error in errors:
            print(f"  error: {error}")
        return 1
    data = json.loads(path.read_text(encoding="utf-8"))
    decisions = {}
    for channel in data["channels"]:
        decision = channel["reviewDecision"]
        decisions[decision] = decisions.get(decision, 0) + 1
    print(
        f"ok   {path}  surah={data['surah']} channels={len(data['channels'])} "
        f"state={data['reviewState']} decisions={decisions}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
