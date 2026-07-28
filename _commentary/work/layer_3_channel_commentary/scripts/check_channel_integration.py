#!/usr/bin/env python3
"""Validate Layer 3 integration of already-reviewed channels.

This checker never admits, rejects, or scores source channels. It verifies that
the prose-facing integration uses compiled identities, accounts for every
reviewed source, and derives maturity without running ahead of reading order.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

WORK_ROOT = Path(__file__).resolve().parent.parent
ROOT = WORK_ROOT.parents[2]
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ROOT_RE = re.compile(r"^root_[0-9]{6}$")
BRANCH_RE = re.compile(r"^B[0-9]{3}$")
QAC_RE = re.compile(
    r"^([1-9][0-9]{0,2}):([1-9][0-9]{0,2}):[1-9][0-9]*:[1-9][0-9]*$"
)
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
STATES = {"latent": 0, "emerging": 1, "mature": 2, "complete": 3}
RELATIONS = {"supports-primary", "shifts-primary"}

TOP_REQUIRED = {
    "schemaVersion",
    "surah",
    "sourceLane",
    "sourceBundle",
    "sourceBundleSha256",
    "primaryFloorBasis",
    "channels",
    "sourceCoverage",
}
CHANNEL_REQUIRED = {
    "channelId",
    "name_tr",
    "statement_tr",
    "wholeSurahRelation",
    "wholeSurahShift_tr",
    "sourceChannels",
    "members",
    "maturityStatus",
    "maturityByAyah",
}
MEMBER_REQUIRED = {
    "memberId",
    "ayahRef",
    "qacMorphemeRef",
    "rootId",
    "branchId",
    "primaryStatus",
    "surface_tr",
    "contribution_tr",
    "evidenceRefs",
}
MEMBER_ALLOWED = MEMBER_REQUIRED | {"motifId"}
MATURITY_REQUIRED = {
    "ayahRef",
    "state",
    "newMemberIds",
    "recalledMemberIds",
    "cumulativeImage_tr",
}
MATURITY_ALLOWED = MATURITY_REQUIRED | {
    "focusAyahRelation",
    "focusAyahShift_tr",
    "relationStatus",
    "disclosure_tr",
}
COVERAGE_REQUIRED = {"sourceRef", "disposition", "channelIds"}
COVERAGE_ALLOWED = COVERAGE_REQUIRED | {"reason_tr"}


def fail(errors: list[str], where: str, message: str) -> None:
    errors.append(f"{where}: {message}")


def object_shape(
    value: object,
    where: str,
    required: set[str],
    allowed: set[str],
    errors: list[str],
) -> bool:
    if not isinstance(value, dict):
        fail(errors, where, "must be an object")
        return False
    missing = required - set(value)
    extra = set(value) - allowed
    if missing:
        fail(errors, where, f"missing required fields {sorted(missing)}")
    if extra:
        fail(errors, where, f"forbidden fields {sorted(extra)}")
    return not missing and not extra


def ayah_number(
    ref: object, surah: int, errors: list[str], where: str
) -> int | None:
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


def resolve(path_value: str, parent: Path) -> Path:
    path = Path(path_value)
    if path.is_absolute():
        return path
    local = parent / path
    return local if local.exists() else ROOT / path


def load_bundle(
    bundle_path: Path,
) -> tuple[
    dict,
    set[tuple[str, str, str]],
    dict[tuple[str, str, str], str],
    set[str],
    list[str],
]:
    errors: list[str] = []
    try:
        bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {}, set(), {}, set(), [f"bundle: cannot read JSON: {exc}"]

    anchors = {
        item.get("anchorId"): item
        for item in bundle.get("anchorInventory", [])
        if isinstance(item, dict)
        and item.get("rootOccurrenceStatus") == "resolved"
    }
    allowed: set[tuple[str, str, str]] = set()
    for branches in bundle.get("motifAnchorMap", {}).values():
        if not isinstance(branches, dict):
            continue
        for branch_id, motifs in branches.items():
            if not isinstance(motifs, dict):
                continue
            for mapping in motifs.values():
                if (
                    not isinstance(mapping, dict)
                    or mapping.get("rootOccurrenceStatus") != "resolved"
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
        errors.append("bundle: no resolved reviewed channel-member triples")

    primary: dict[tuple[str, str], set[str]] = {}
    for item in bundle.get("primaryBranchMap", {}).get("entries", []):
        if isinstance(item, dict):
            primary[(item.get("qacMorphemeRef"), item.get("rootId"))] = set(
                item.get("primaryBranchIds", [])
            )
    primary_statuses = {}
    for qac, root_id, branch_id in allowed:
        branches = primary.get((qac, root_id))
        primary_statuses[(qac, root_id, branch_id)] = (
            "unknown"
            if branches is None
            else "primary"
            if branch_id in branches
            else "non-primary"
        )

    source_refs: set[str] = set()
    for parent in bundle.get("reviewedChannels", {}).get("parent_channels", []):
        parent_ref = parent.get("key")
        subchannels = parent.get("subchannels", [])
        if not isinstance(parent_ref, str):
            continue
        if subchannels:
            source_refs.update(
                f"{parent_ref}/{item.get('key')}"
                for item in subchannels
                if isinstance(item, dict) and isinstance(item.get("key"), str)
            )
        else:
            source_refs.add(parent_ref)
    if not source_refs:
        errors.append("bundle: no reviewed source-channel references")
    return bundle, allowed, primary_statuses, source_refs, errors


def validate(plan_path: Path, bundle_path: Path | None = None) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(plan_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{plan_path}: cannot read JSON: {exc}"]
    if not object_shape(data, "integration", TOP_REQUIRED, TOP_REQUIRED, errors):
        if not isinstance(data, dict):
            return errors

    if data.get("schemaVersion") != "surah-channel-integration-v1":
        fail(
            errors,
            "integration",
            "schemaVersion must be surah-channel-integration-v1",
        )
    if data.get("sourceLane") != "combined-layer3-layer2.5":
        fail(errors, "integration", "sourceLane must be combined-layer3-layer2.5")
    surah = data.get("surah")
    if not isinstance(surah, int) or not 1 <= surah <= 114:
        fail(errors, "integration", "surah must be an integer from 1 through 114")
        return errors

    declared_bundle = data.get("sourceBundle")
    if bundle_path is None and isinstance(declared_bundle, str):
        bundle_path = resolve(declared_bundle, plan_path.parent)
    if bundle_path is None:
        fail(errors, "integration", "source bundle is required")
        return errors
    bundle, allowed, primary_statuses, source_refs, bundle_errors = load_bundle(
        bundle_path
    )
    errors.extend(bundle_errors)
    if bundle.get("surah") != surah:
        fail(errors, "integration", "source bundle belongs to another surah")
    if not isinstance(declared_bundle, str) or not declared_bundle:
        fail(errors, "integration", "sourceBundle is required")
    elif resolve(declared_bundle, plan_path.parent).resolve() != bundle_path.resolve():
        fail(errors, "integration", "sourceBundle does not match validated bundle")
    actual_bundle_sha = hashlib.sha256(bundle_path.read_bytes()).hexdigest()
    if data.get("sourceBundleSha256") != actual_bundle_sha:
        fail(errors, "integration", "sourceBundleSha256 does not match source bundle")

    basis = data.get("primaryFloorBasis")
    if object_shape(
        basis,
        "primaryFloorBasis",
        {"status", "apparatusStatus"},
        {"status", "apparatusStatus", "sourcePath", "sourceSha256"},
        errors,
    ):
        status = basis.get("status")
        if status == "authored":
            if not str(basis.get("sourcePath", "")).strip():
                fail(errors, "primaryFloorBasis", "authored floor requires sourcePath")
            if not SHA_RE.fullmatch(str(basis.get("sourceSha256", ""))):
                fail(errors, "primaryFloorBasis", "authored floor requires sourceSha256")
            if basis.get("apparatusStatus") != "canonical-translation-floor":
                fail(
                    errors,
                    "primaryFloorBasis",
                    "authored floor requires canonical-translation-floor",
                )
        elif status == "arabic-only-inference":
            if "sourcePath" in basis or "sourceSha256" in basis:
                fail(
                    errors,
                    "primaryFloorBasis",
                    "Arabic-only floor cannot cite authored translation",
                )
            if basis.get("apparatusStatus") != "writer-primary-inference":
                fail(
                    errors,
                    "primaryFloorBasis",
                    "Arabic-only floor requires writer-primary-inference",
                )
        else:
            fail(errors, "primaryFloorBasis", "invalid status")

    channels = data.get("channels")
    if not isinstance(channels, list):
        fail(errors, "integration", "channels must be an array")
        return errors
    channel_ids: set[str] = set()
    channel_sources: dict[str, set[str]] = {}
    for ci, channel in enumerate(channels):
        where = f"channels[{ci}]"
        if not object_shape(
            channel, where, CHANNEL_REQUIRED, CHANNEL_REQUIRED, errors
        ):
            if not isinstance(channel, dict):
                continue
        channel_id = channel.get("channelId")
        if not isinstance(channel_id, str) or not ID_RE.fullmatch(channel_id):
            fail(errors, where, f"invalid channelId {channel_id!r}")
        elif channel_id in channel_ids:
            fail(errors, where, f"duplicate channelId {channel_id!r}")
        else:
            channel_ids.add(channel_id)
        for field in ("name_tr", "statement_tr", "wholeSurahShift_tr"):
            if not str(channel.get(field, "")).strip():
                fail(errors, where, f"{field} is empty")
        if channel.get("wholeSurahRelation") not in RELATIONS:
            fail(errors, where, "invalid wholeSurahRelation")
        if channel.get("maturityStatus") != "derived":
            fail(errors, where, "maturityStatus must be derived")
        sources = channel.get("sourceChannels")
        if not isinstance(sources, list) or not sources:
            fail(errors, where, "sourceChannels must be a non-empty array")
            sources = []
        unknown_sources = set(sources) - source_refs
        if unknown_sources:
            fail(errors, where, f"unknown sourceChannels {sorted(unknown_sources)}")
        channel_sources[channel_id] = set(sources)

        members = channel.get("members")
        if not isinstance(members, list) or len(members) < 2:
            fail(errors, where, "a rendered channel requires at least two members")
            continue
        member_ids: set[str] = set()
        member_ayah: dict[str, int] = {}
        non_primary = 0
        for mi, member in enumerate(members):
            mwhere = f"{where}.members[{mi}]"
            if not object_shape(
                member, mwhere, MEMBER_REQUIRED, MEMBER_ALLOWED, errors
            ):
                if not isinstance(member, dict):
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
            elif number is not None and (
                int(match.group(1)),
                int(match.group(2)),
            ) != (surah, number):
                fail(errors, mwhere, "qacMorphemeRef does not match ayahRef")
            if not ROOT_RE.fullmatch(str(member.get("rootId", ""))):
                fail(errors, mwhere, "invalid rootId")
            if not BRANCH_RE.fullmatch(str(member.get("branchId", ""))):
                fail(errors, mwhere, "invalid branchId")
            triple = (
                member.get("qacMorphemeRef"),
                member.get("rootId"),
                member.get("branchId"),
            )
            if triple not in allowed:
                fail(
                    errors,
                    mwhere,
                    "member is not a resolved reviewed qac/root/branch mapping",
                )
            expected_primary = primary_statuses.get(triple)
            if expected_primary is not None and member.get("primaryStatus") != expected_primary:
                fail(
                    errors,
                    mwhere,
                    f"primaryStatus must be {expected_primary!r}",
                )
            if member.get("primaryStatus") == "non-primary":
                non_primary += 1
            if not str(member.get("surface_tr", "")).strip():
                fail(errors, mwhere, "surface_tr is empty")
            if not str(member.get("contribution_tr", "")).strip():
                fail(errors, mwhere, "contribution_tr is empty")
            if not isinstance(member.get("evidenceRefs"), list) or not member["evidenceRefs"]:
                fail(errors, mwhere, "evidenceRefs must be non-empty")
        if len(set(member_ayah.values())) < 2:
            fail(errors, where, "rendered channel does not recur across two ayahs")
        if non_primary == 0:
            fail(errors, where, "rendered channel has no non-primary member")

        maturity = channel.get("maturityByAyah")
        if not isinstance(maturity, list) or not maturity:
            fail(errors, where, "maturityByAyah must be non-empty")
            continue
        seen_members: set[str] = set()
        seen_refs: set[str] = set()
        previous_ayah = 0
        previous_state = -1
        for ai, entry in enumerate(maturity):
            awhere = f"{where}.maturityByAyah[{ai}]"
            if not object_shape(
                entry, awhere, MATURITY_REQUIRED, MATURITY_ALLOWED, errors
            ):
                if not isinstance(entry, dict):
                    continue
            ref = entry.get("ayahRef")
            number = ayah_number(ref, surah, errors, awhere)
            if ref in seen_refs:
                fail(errors, awhere, f"duplicate ayahRef {ref!r}")
            if isinstance(ref, str):
                seen_refs.add(ref)
            if number is not None and number <= previous_ayah:
                fail(errors, awhere, "maturity is not in reading order")
            if number is not None:
                previous_ayah = number
            state = entry.get("state")
            if state not in STATES:
                fail(errors, awhere, f"invalid state {state!r}")
                continue
            if STATES[state] < previous_state:
                fail(errors, awhere, "maturity runs backwards")
            previous_state = STATES[state]
            new_ids = entry.get("newMemberIds")
            recalled_ids = entry.get("recalledMemberIds")
            if not isinstance(new_ids, list) or not isinstance(recalled_ids, list):
                fail(errors, awhere, "member ID fields must be arrays")
                continue
            expected_new = {
                member_id
                for member_id, member_at in member_ayah.items()
                if member_at == number
            }
            if set(new_ids) != expected_new:
                fail(errors, awhere, "newMemberIds do not match members at this ayah")
            unknown = (set(new_ids) | set(recalled_ids)) - member_ids
            if unknown:
                fail(errors, awhere, f"unknown member IDs {sorted(unknown)}")
            if not set(recalled_ids) <= seen_members:
                fail(errors, awhere, "recalled member has not appeared yet")
            seen_members.update(new_ids)
            if len(seen_members) <= 1 and state != "latent":
                fail(errors, awhere, "first member must remain latent")
            if state == "latent" and len(seen_members) > 1:
                if entry.get("relationStatus") != "not-yet-statable":
                    fail(
                        errors,
                        awhere,
                        "multi-member latent state requires not-yet-statable",
                    )
            if state != "latent" and new_ids:
                if entry.get("focusAyahRelation") not in RELATIONS:
                    fail(errors, awhere, "visible arrival requires focusAyahRelation")
                if not str(entry.get("focusAyahShift_tr", "")).strip():
                    fail(errors, awhere, "visible arrival requires focusAyahShift_tr")
            if state == "complete" and seen_members != member_ids:
                fail(errors, awhere, "complete declared before all members appear")
        if seen_members != member_ids:
            fail(errors, where, "maturity does not introduce every member")
        if previous_state != STATES["complete"]:
            fail(errors, where, "maturity must end at complete")

    coverage = data.get("sourceCoverage")
    if not isinstance(coverage, list):
        fail(errors, "sourceCoverage", "must be an array")
        return errors
    seen_sources: set[str] = set()
    coverage_links: dict[str, set[str]] = {}
    for index, item in enumerate(coverage):
        where = f"sourceCoverage[{index}]"
        if not object_shape(
            item, where, COVERAGE_REQUIRED, COVERAGE_ALLOWED, errors
        ):
            if not isinstance(item, dict):
                continue
        source_ref = item.get("sourceRef")
        if source_ref in seen_sources:
            fail(errors, where, f"duplicate sourceRef {source_ref!r}")
        if isinstance(source_ref, str):
            seen_sources.add(source_ref)
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
        if disposition == "integrated":
            if not linked:
                fail(errors, where, "integrated source requires channelIds")
            coverage_links[str(source_ref)] = set(linked)
        else:
            if linked:
                fail(errors, where, "apparatus-only source cannot name channelIds")
            if not str(item.get("reason_tr", "")).strip():
                fail(errors, where, "apparatus-only source requires reason_tr")
    if seen_sources != source_refs:
        fail(
            errors,
            "sourceCoverage",
            f"must account for every reviewed source; "
            f"missing={sorted(source_refs - seen_sources)}, "
            f"extra={sorted(seen_sources - source_refs)}",
        )
    for channel_id, sources in channel_sources.items():
        for source_ref in sources:
            if channel_id not in coverage_links.get(source_ref, set()):
                fail(
                    errors,
                    "sourceCoverage",
                    f"{source_ref!r} does not link integrated channel {channel_id!r}",
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("integration", type=Path)
    parser.add_argument("--bundle", type=Path)
    args = parser.parse_args()
    plan_path = (
        args.integration
        if args.integration.is_absolute()
        else ROOT / args.integration
    )
    bundle_path = None
    if args.bundle is not None:
        bundle_path = args.bundle if args.bundle.is_absolute() else ROOT / args.bundle
    errors = validate(plan_path, bundle_path)
    if errors:
        print(f"FAIL {plan_path}")
        for error in errors:
            print(f"  error: {error}")
        return 1
    data = json.loads(plan_path.read_text(encoding="utf-8"))
    print(
        f"ok   {plan_path}  surah={data['surah']} "
        f"integrated-channels={len(data['channels'])}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
