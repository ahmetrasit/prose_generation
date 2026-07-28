#!/usr/bin/env python3
"""Build the lean input bundle for combined Layer 3 + Layer 2.5 commentary.

The upstream network review is the reviewed channel source. This builder keeps
its prose judgments, normalizes its root/branch citations, and joins them to
typed Quran anchors. Layer-2 prose is added by ``instantiate_channel.py`` rather
than duplicated in this bundle.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

from check_channel_bundle import validate_data as validate_channel_bundle

WORK_ROOT = Path(__file__).resolve().parent.parent
ROOT = WORK_ROOT.parents[2]
BUNDLES = ROOT / "bundles"
GENERATED_BUNDLES = WORK_ROOT / "generated" / "bundles"
TRANSLATIONS = ROOT / "_translation" / "v1" / "output" / "tr"
PRIMARY_ANCHORS = ROOT / "_translation" / "v1" / "source"
CITE_AR = re.compile(
    r"`?([ء-ي](?:\s+[ء-ي])*)\s*:\s*(B\d{3})(?:/(m\d+))?`?"
)
CITE_ID = re.compile(r"(root_\d{6})\s*[: ]\s*(B\d{3})(?:/(m\d+))?")
ROOT_ID = re.compile(r"^root_\d{6}$")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path.resolve())


def norm_root(value: str) -> str:
    return unicodedata.normalize("NFC", value).replace(" ", "").strip()


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"error: required input does not exist: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"error: present input is unparseable JSON: {path}: {exc}")


def discover_ayahs(surah: int) -> list[int]:
    directory = BUNDLES / f"s{surah:03d}"
    ayahs: list[int] = []
    for path in directory.glob(f"{surah}_*.ayah.json"):
        match = re.fullmatch(rf"{surah}_(\d+)\.ayah\.json", path.name)
        if match:
            ayahs.append(int(match.group(1)))
    if not ayahs:
        raise SystemExit(f"error: no ayah bundles found for surah {surah}")
    return sorted(set(ayahs))


def cited_motifs(text: str) -> list[dict]:
    """Return the review's stable root/branch identity without parsing its prose."""
    motifs: list[dict] = []
    seen: set[tuple[str, str, str | None]] = set()
    for match in CITE_AR.finditer(text):
        root_ar, branch_id, motif_id = match.groups()
        identity = (norm_root(root_ar), branch_id, motif_id)
        if identity in seen:
            continue
        seen.add(identity)
        item = {
            "rootAr": root_ar,
            "branchId": branch_id,
        }
        if motif_id:
            item["motifId"] = motif_id
        motifs.append(item)
    for match in CITE_ID.finditer(text):
        root_id, branch_id, motif_id = match.groups()
        identity = (root_id, branch_id, motif_id)
        if identity in seen:
            continue
        seen.add(identity)
        item = {
            "rootId": root_id,
            "branchId": branch_id,
        }
        if motif_id:
            item["motifId"] = motif_id
        motifs.append(item)
    return motifs


def anchored_refs(surah: int, record: dict) -> list[str]:
    refs = [
        ref
        for ref in record.get("ayah_refs", [])
        if re.fullmatch(rf"{surah}:\d+", str(ref))
    ]
    if refs:
        return list(dict.fromkeys(refs))
    pattern = re.compile(rf"\b{surah}:(\d+)(?:-(\d+))?")
    for match in pattern.finditer(str(record.get("ayah_anchors", ""))):
        start = int(match.group(1))
        end = int(match.group(2) or start)
        refs.extend(f"{surah}:{ayah}" for ayah in range(start, end + 1))
    return list(dict.fromkeys(refs))


def normalize_review(review: dict, surah: int) -> dict:
    """Keep reviewed meaning and evidence while removing redundant prose."""
    parents = []
    for parent_index, parent in enumerate(review.get("parent_channels", []), 1):
        subchannels = []
        for subchannel in parent.get("subchannels", []):
            subchannels.append(
                {
                    "key": subchannel.get("key", ""),
                    "name": subchannel.get("name", ""),
                    "reading_type": subchannel.get("reading_type", ""),
                    "active_motifs": subchannel.get("active_motifs", ""),
                    "synthesis": subchannel.get("synthesis", ""),
                    "ayah_refs": anchored_refs(surah, subchannel),
                }
            )
        normalized = {
            "key": f"P{parent_index:02d}",
            "name": parent.get("name", ""),
            "semantic_invariant": parent.get("semantic_invariant", ""),
            "surface_relation": parent.get("surface_relation", ""),
            "surprising_reach": parent.get("surprising_reach", ""),
            "subchannels": subchannels,
        }
        if not subchannels:
            normalized.update(
                {
                    "reading_type": parent.get("reading_type", ""),
                    "active_motifs": parent.get("active_motifs", ""),
                    "synthesis": parent.get("synthesis", ""),
                    "ayah_refs": anchored_refs(surah, parent),
                }
            )
        elif parent.get("synthesis"):
            normalized["synthesis"] = parent["synthesis"]
        parents.append(normalized)
    return {"parent_channels": parents}


def prune_review(review: dict, surah: int | None = None) -> dict:
    """Compatibility alias for callers of the former draft-lane helper."""
    if surah is None:
        raise ValueError("surah is required when normalizing reviewed channels")
    return normalize_review(review, surah)


def citation_universe(review: dict) -> tuple[set[str], set[str]]:
    roots_ar: set[str] = set()
    roots_id: set[str] = set()
    for parent in review.get("parent_channels", []):
        records = parent.get("subchannels", []) or [parent]
        for subchannel in records:
            text = " ".join(
                str(value) for value in subchannel.values() if isinstance(value, str)
            )
            roots_ar.update(norm_root(match.group(1)) for match in CITE_AR.finditer(text))
            roots_id.update(match.group(1) for match in CITE_ID.finditer(text))
    return roots_ar, roots_id


def root_candidates(bundle: dict) -> tuple[dict[str, set[str]], dict[str, str]]:
    by_ar: dict[str, set[str]] = {}
    ar_for_id: dict[str, str] = {}
    inventories = bundle.get("branch_inventories", {})
    for variant in inventories.values():
        for entry in variant.get("branch_inventories", []):
            root_ar = entry.get("root", "")
            for branch in entry.get("branches", []):
                for item in branch.get("variants", []):
                    root_id = item.get("root_id")
                    if root_id:
                        by_ar.setdefault(norm_root(root_ar), set()).add(root_id)
                        ar_for_id[root_id] = root_ar
    lexicon = bundle.get("root_lexicon", {}) or {}
    entries = lexicon.values() if isinstance(lexicon, dict) else lexicon
    for entry in entries:
        root_id = entry.get("rootId") or entry.get("root_id")
        roots = entry.get("qac_roots_ar") or [
            entry.get("root_ar") or entry.get("root")
        ]
        if root_id:
            for root_ar in filter(None, roots):
                by_ar.setdefault(norm_root(root_ar), set()).add(root_id)
                ar_for_id.setdefault(root_id, root_ar)
    return by_ar, ar_for_id


def build_anchor_inventory(
    surah: int, ayahs: list[int], cited_ar: set[str], cited_ids: set[str]
) -> tuple[list[dict], list[dict]]:
    anchors: list[dict] = []
    ambiguous: list[dict] = []
    relevant: list[tuple[int, dict, str, list[str]]] = []
    for ayah in ayahs:
        bundle = load_json(BUNDLES / f"s{surah:03d}" / f"{surah}_{ayah}.ayah.json")
        candidates_by_ar, _ = root_candidates(bundle)
        for row in bundle.get("qac_morphemes", []):
            root_ar = row.get("root_ar") or ""
            key = norm_root(root_ar)
            candidates = [
                root_id
                for root_id in sorted(candidates_by_ar.get(key, set()))
                if key in cited_ar or root_id in cited_ids
            ]
            if candidates:
                relevant.append((ayah, row, root_ar, candidates))

    # Recurrence is scoped to the whole surah, because that is the scope
    # membership criterion 3 asks about. It is not an ambiguity: each row below
    # already carries one exact qacMorphemeRef and one rootId.
    refs_by_root_id: dict[str, set[str]] = {}
    for _, row, _, candidates in relevant:
        for root_id in candidates:
            refs_by_root_id.setdefault(root_id, set()).add(row["qac_ref"])

    for ayah, row, root_ar, candidates in relevant:
        for root_id in candidates:
            # Only an unresolved rootId is an ambiguity: the same root string
            # maps to several roots and nothing in the bundle chooses between
            # them. Repeated occurrences of one root are recurrence evidence.
            reasons = ["root-id"] if len(candidates) > 1 else []
            record = {
                "ayahRef": f"{surah}:{ayah}",
                "qacMorphemeRef": row["qac_ref"],
                "surface_ar": row.get("surface_ar", ""),
                "root_ar": root_ar,
                "rootId": root_id,
                "rootOccurrenceStatus": "ambiguous-root" if reasons else "resolved",
            }
            if reasons:
                record["ambiguityReasons"] = reasons
                record["candidateRootIds"] = candidates
            recurrence = sorted(refs_by_root_id[root_id])
            if len(recurrence) > 1:
                record["recurrenceRefs"] = recurrence
            anchors.append(record)
            if reasons:
                ambiguous.append(record)
    anchors.sort(
        key=lambda item: (item["ayahRef"], item["qacMorphemeRef"], item["rootId"])
    )
    for index, anchor in enumerate(anchors, 1):
        anchor["anchorId"] = f"a{surah:03d}-{index:04d}"
    return anchors, ambiguous


def build_motif_anchor_map(review: dict, anchors: list[dict]) -> dict:
    """Compile every reviewed root/branch citation to Quran anchors once."""
    anchors_by_root: dict[str, list[dict]] = {}
    anchors_by_root_id: dict[str, list[dict]] = {}
    for anchor in anchors:
        anchors_by_root.setdefault(norm_root(anchor["root_ar"]), []).append(anchor)
        anchors_by_root_id.setdefault(anchor["rootId"], []).append(anchor)
    result: dict = {}
    for parent in review.get("parent_channels", []):
        records = parent.get("subchannels", []) or [parent]
        for record in records:
            allowed_refs = set(record.get("ayah_refs", []))
            for motif in cited_motifs(str(record.get("active_motifs", ""))):
                identity_key = motif.get("rootId") or motif["rootAr"]
                identity_anchors = (
                    anchors_by_root_id.get(motif["rootId"], [])
                    if "rootId" in motif
                    else anchors_by_root.get(norm_root(motif["rootAr"]), [])
                )
                candidates = [
                    anchor
                    for anchor in identity_anchors
                    if not allowed_refs or anchor["ayahRef"] in allowed_refs
                ]
                slot = (
                    result.setdefault(identity_key, {})
                    .setdefault(motif["branchId"], {})
                    .setdefault(
                        motif.get("motifId", "_"),
                        {"anchorIds": [], "rootOccurrenceStatus": "unmatched"},
                    )
                )
                slot["anchorIds"] = sorted(
                    set(slot["anchorIds"])
                    | {anchor["anchorId"] for anchor in candidates}
                )
                if not candidates:
                    status = "unmatched"
                elif any(
                    anchor["rootOccurrenceStatus"] == "ambiguous-root"
                    for anchor in candidates
                ):
                    status = "ambiguous-root"
                else:
                    status = "resolved"
                rank = {"unmatched": 0, "resolved": 1, "ambiguous-root": 2}
                if rank[status] > rank[slot["rootOccurrenceStatus"]]:
                    slot["rootOccurrenceStatus"] = status
    return result


def primary_branch_map(
    surah: int, anchors: list[dict]
) -> tuple[dict, dict[tuple[str, str], set[str]]]:
    """Compile primary branches for channel-member occurrences only."""
    candidates = sorted(PRIMARY_ANCHORS.glob(f"s{surah:03d}*.primary-anchors.json"))
    if len(candidates) != 1:
        return {
            "status": "absent" if not candidates else "ambiguous-source",
            "entries": [],
        }, {}
    path = candidates[0]
    data = load_json(path)
    if data.get("surah") != surah or not isinstance(data.get("anchors"), list):
        return {"status": "invalid-source", "entries": []}, {}

    channel_by_qac: dict[str, set[str]] = {}
    root_by_qac: dict[str, set[str]] = {}
    for anchor in anchors:
        qac = anchor["qacMorphemeRef"]
        channel_by_qac.setdefault(qac, set()).add(anchor["rootId"])
        root_by_qac.setdefault(qac, set()).add(anchor["rootId"])

    source_by_qac = {
        item.get("qacMorphemeRef"): item
        for item in data["anchors"]
        if isinstance(item, dict) and isinstance(item.get("qacMorphemeRef"), str)
    }
    entries: list[dict] = []
    lookup: dict[tuple[str, str], set[str]] = {}
    for qac in sorted(channel_by_qac):
        item = source_by_qac.get(qac)
        if not item:
            continue
        primary = item.get("primary")
        if isinstance(primary, dict):
            root_id = primary.get("rootId")
            branches = primary.get("branchIds", [])
        else:
            root_id = item.get("rootId")
            if not root_id and len(root_by_qac[qac]) == 1:
                root_id = next(iter(root_by_qac[qac]))
            branches = item.get("branchIds", [])
        if (
            not isinstance(root_id, str)
            or not ROOT_ID.fullmatch(root_id)
            or not isinstance(branches, list)
            or not branches
        ):
            continue
        branch_ids = sorted(
            {branch for branch in branches if re.fullmatch(r"B\d{3}", str(branch))}
        )
        if not branch_ids:
            continue
        entries.append(
            {
                "qacMorphemeRef": qac,
                "rootId": root_id,
                "primaryBranchIds": branch_ids,
            }
        )
        lookup[(qac, root_id)] = set(branch_ids)

    expected = set(channel_by_qac)
    covered = {item["qacMorphemeRef"] for item in entries}
    status = "complete" if covered == expected else "partial"
    rendered = path.read_text(encoding="utf-8")
    return {
        "status": status,
        "sourcePath": rel(path),
        "sourceSha256": sha256_text(rendered),
        "coveredChannelAnchorCount": len(covered),
        "channelAnchorCount": len(expected),
        "entries": entries,
    }, lookup


def primary_floor(surah: int, ayahs: list[int]) -> tuple[dict, dict]:
    exact = TRANSLATIONS / f"s{surah:03d}.json"
    candidates = (
        [exact]
        if exact.is_file()
        else sorted(TRANSLATIONS.glob(f"s{surah:03d}.*.json"))
    )
    complete: list[tuple[Path, dict, list[dict]]] = []
    partial: list[str] = []
    required = {f"{surah}:{ayah}" for ayah in ayahs}
    for path in candidates:
        data = load_json(path)
        if (
            data.get("schemaVersion") != "translation-layer-v1"
            or data.get("language") != "tr"
            or data.get("surah") != surah
        ):
            continue
        lines = [
            {
                "ayahRef": item.get("ayahRef"),
                "text": item.get("translation", {}).get("text", ""),
            }
            for item in data.get("ayat", [])
            if item.get("ayahRef") in required
            and item.get("translation", {}).get("text")
        ]
        refs = {item["ayahRef"] for item in lines}
        all_refs = {
            item.get("ayahRef")
            for item in data.get("ayat", [])
            if isinstance(item, dict) and item.get("ayahRef")
        }
        allowed_extra = {"1:1"} if surah != 1 else set()
        unexpected = all_refs - required - allowed_extra
        if refs == required and not unexpected:
            complete.append((path, data, lines))
        elif refs:
            partial.append(rel(path))
    if exact.is_file() and complete:
        path, data, lines = complete[0]
        text = path.read_text(encoding="utf-8")
        return {
            "status": "authored",
            "language": data.get("language", "tr"),
            "sourcePath": rel(path),
            "sourceSha256": sha256_text(text),
            "lines": lines,
        }, {"status": "authored", "sourcePath": rel(path)}
    # Coverage reports the same `status` vocabulary the writer sees, so the two
    # cannot disagree; `reason` carries why no floor was authored, and the paths
    # are named so an auditor can tell a junk test file from a missing rename.
    noncanonical = [rel(item[0]) for item in complete]
    return {"status": "arabic-only-inference"}, {
        "status": "arabic-only-inference",
        "reason": (
            "partial"
            if partial
            else "noncanonical-only"
            if noncanonical
            else "absent"
        ),
        "partialSources": partial,
        "noncanonicalCompleteSources": noncanonical,
    }


def build(surah: int) -> dict:
    surah_path = BUNDLES / f"s{surah:03d}" / f"{surah}.surah.json"
    surah_bundle = load_json(surah_path)
    scope = surah_bundle.get("surah_scope", {})
    original_review = scope.get("channel_review")
    if not isinstance(original_review, dict) or not original_review.get(
        "parent_channels"
    ):
        raise SystemExit(f"error: absent channel review for surah {surah}")
    review = normalize_review(original_review, surah)
    ayahs = discover_ayahs(surah)
    cited_ar, cited_ids = citation_universe(review)
    anchors, ambiguous = build_anchor_inventory(surah, ayahs, cited_ar, cited_ids)
    motif_anchor_map = build_motif_anchor_map(review, anchors)
    floor, floor_coverage = primary_floor(surah, ayahs)
    primary_map, _ = primary_branch_map(surah, anchors)
    review_coverage = (
        surah_bundle.get("coverage", {})
        .get("per_ayah", {})
        .get(f"{surah}:{ayahs[0]}", {})
        .get("channel_review", {})
    )
    review_source = review_coverage.get("source_file")
    review_path = ROOT.parent / review_source if review_source else None
    review_sha = (
        sha256_text(review_path.read_text(encoding="utf-8"))
        if review_path and review_path.is_file()
        else None
    )
    anchored_root_ar = {norm_root(item["root_ar"]) for item in anchors}
    anchored_root_ids = {item["rootId"] for item in anchors}
    return {
        "schemaVersion": "channel-bundle-v1",
        "bundleType": "combined-channel-commentary",
        "surah": surah,
        "reviewedChannels": review,
        "text": scope.get("quran_text_all_rows", []),
        "anchorInventory": anchors,
        "motifAnchorMap": motif_anchor_map,
        "primaryFloor": floor,
        "primaryBranchMap": primary_map,
        "coverage": {
            "reviewedChannels": {
                "reviewStatus": "reviewed",
                "sourcePath": review_source,
                "sourceSha256": review_sha,
                "parentCount": len(review["parent_channels"]),
                "subchannelCount": sum(
                    len(parent["subchannels"])
                    for parent in review["parent_channels"]
                ),
            },
            "primaryFloor": floor_coverage,
            "primaryBranchMap": {
                key: value
                for key, value in primary_map.items()
                if key != "entries"
            },
            "identityMappings": {
                "anchorCount": len(anchors),
                "ambiguousAnchorCount": len(ambiguous),
                "unmatchedReviewRootCount": len(cited_ar - anchored_root_ar),
                "unmatchedReviewRootIdCount": len(cited_ids - anchored_root_ids),
            },
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", required=True, type=int)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    data = build(args.surah)
    errors = validate_channel_bundle(data, args.surah)
    if errors:
        details = "\n".join(f"  {error}" for error in errors)
        raise SystemExit(f"error: generated channel bundle failed validation:\n{details}")
    out = args.out or (
        GENERATED_BUNDLES / f"s{args.surah:03d}" / f"{args.surah}.channel.json"
    )
    if not out.is_absolute():
        out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    out.write_text(rendered, encoding="utf-8")
    print(
        f"wrote {out} ({len(rendered.encode('utf-8')):,} bytes; "
        f"reviewed channels, Layer-2 prose added at instantiation)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
