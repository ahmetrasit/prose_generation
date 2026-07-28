#!/usr/bin/env python3
"""Build the language-neutral anchor-selection input for one surah.

Stage 0 of layer 1. Enumerates every rooted QAC stem in the surah and attaches
the complete candidate space for it: all branches of its root, the lexical units
linked to those branches, which branches V12 activated locally, and the
word-analysis note for the word. Selecting one primary branch per stem is the
authoring act; this file only assembles what that act chooses between.

Language-neutral by construction (`PRINCIPLES.md` §10). Branch selection is
shared across target languages, so no target-language gloss evidence enters here.
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
from pathlib import Path

from build_bundle import morphology, read_json, root_bindings, word_ref

V1_DIR = Path(__file__).resolve().parents[1]
WORKSPACE = V1_DIR.parents[2]

BUILDER_VERSION = "anchor-input-v1"


class RequiredSourceMissing(RuntimeError):
    """A source that must exist for every canonical surah is absent."""


# ---------------------------------------------------------------------------
# Sources
# ---------------------------------------------------------------------------

def v12_dir(surah: int) -> Path:
    path = (
        WORKSPACE
        / "latent_activation"
        / "_status"
        / "v12_cross_run"
        / f"s{surah:03d}"
    )
    if not path.is_dir():
        raise RequiredSourceMissing(f"no v12 cross-run directory: {path}")
    return path


def root_packet(root_id: str) -> dict:
    path = (
        WORKSPACE / "dictionary" / "data" / "output" / "root_packets" / f"{root_id}.json"
    )
    if not path.exists():
        raise RequiredSourceMissing(f"no dictionary root packet: {path}")
    return read_json(path)


def v12_activated_branches(surah: int) -> dict[str, list[str]]:
    """Branch ids V12 touched in this surah, keyed by root id.

    These are candidates, not selections. The v3 publication flattens primary
    and resonance roles, so an activated branch is not automatically the
    translational one — see `README.md`, *Anchor decisions*.
    """
    anchor_map = read_json(v12_dir(surah) / "anchor_map.v3.json")
    columns = {name: index for index, name in enumerate(anchor_map["columns"])}
    activated: dict[str, set[str]] = {}
    for row in anchor_map["rows"]:
        root_id = row[columns["root_id"]]
        branch_id = row[columns["branch_id"]]
        if branch_id:
            activated.setdefault(root_id, set()).add(branch_id)
    return {root_id: sorted(ids) for root_id, ids in activated.items()}


def word_analysis_by_word_ref(surah: int) -> tuple[dict[str, dict], str]:
    """Word-analysis notes keyed by the word ref they claim to align to.

    The alignment is known to be defective for some ayahs — `aligned_qac_word_ref`
    does not always resolve against QAC. Unresolved notes are reported in
    coverage rather than dropped silently.
    """
    path = (
        WORKSPACE
        / "quran-data"
        / "data"
        / "analysis"
        / "word-analysis"
        / f"s{surah:03d}.jsonl.zst"
    )
    if not path.exists():
        return {}, f"absent: {path}"

    raw = subprocess.run(
        ["zstd", "-dc", str(path)],
        capture_output=True,
        check=True,
    ).stdout.decode("utf-8")

    notes: dict[str, dict] = {}
    for line in raw.strip().split("\n"):
        if not line:
            continue
        record = json.loads(line)
        for word in record.get("words", []):
            ref = word.get("aligned_qac_word_ref")
            if not ref:
                continue
            topics = [
                {
                    "status": topic.get("status"),
                    "headline": topic.get("headline"),
                }
                for topic in word.get("topics", [])
                if topic.get("headline")
            ]
            notes[ref] = {
                "glossRange": word.get("gloss_range"),
                "rootGlossRange": word.get("root_gloss_range"),
                "rootDisplay": word.get("root_display"),
                "topics": topics,
            }
    return notes, "parsed"


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def branch_candidates(packet: dict, activated: list[str]) -> list[dict]:
    candidates = []
    for branch in packet["branches"]:
        branch_id = branch["branch_id"]
        candidate = {
            "branchId": branch_id,
            "imageAr": branch.get("branch_image_ar"),
            "imageEn": branch.get("branch_image_en"),
            "whatIsEn": branch.get("what_is_en"),
            "whatIsNotAr": branch.get("what_is_not_ar"),
            "v12Activated": branch_id in activated,
        }
        candidates.append({k: v for k, v in candidate.items() if v not in (None, "")})
    return candidates


def lexical_candidates(packet: dict) -> list[dict]:
    units = []
    for unit in packet["lexical_senses"]:
        units.append(
            {
                "lexicalUnitId": unit["lexical_unit_id"],
                "expressionAr": unit.get("expression_ar"),
                "senseEn": unit.get("sense_en"),
                "senseEnFit": unit.get("sense_en_fit"),
                "branchIds": unit.get("branch_ids", "").split(),
            }
        )
    return units


def parse_ayah_range(value: str | None) -> tuple[int, int] | None:
    if not value:
        return None
    if "-" in value:
        first, last = value.split("-", 1)
        return int(first), int(last)
    return int(value), int(value)


def build_anchor_input(surah: int, ayahs: tuple[int, int] | None = None) -> dict:
    directory = v12_dir(surah)
    roster = read_json(directory / "ayah_roster.v3.json")
    root_ids, quran_data_release_id = root_bindings(surah, directory)
    activated = v12_activated_branches(surah)
    analysis_notes, analysis_state = word_analysis_by_word_ref(surah)

    morphemes_by_ayah: dict[str, list[dict[str, str]]] = {}
    with (directory / "linguistic" / "morphemes.tsv").open(
        encoding="utf-8", newline=""
    ) as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            ayah_ref = ":".join(row["qac_ref"].split(":")[:2])
            morphemes_by_ayah.setdefault(ayah_ref, []).append(row)

    packets: dict[str, dict] = {}
    ayat = []
    rooted_count = 0
    analysis_hits = 0
    for _, arabic_text, ayah_ref, _ in roster["rows"]:
        if ayahs is not None:
            ayah_surah, ayah_number = (int(part) for part in ayah_ref.split(":"))
            # Prefatory basmalah rows carry another surah's ref and belong to
            # the first chunk only.
            in_chunk = (
                ayahs[0] <= ayah_number <= ayahs[1]
                if ayah_surah == surah
                else ayahs[0] <= 1
            )
            if not in_chunk:
                continue
        stems = []
        for row in morphemes_by_ayah[ayah_ref]:
            if not row["root_join_key"]:
                continue
            rooted_count += 1
            qac_ref = row["qac_ref"]
            root_id = root_ids[row["root_join_key"]]
            if root_id not in packets:
                packets[root_id] = root_packet(root_id)
            packet = packets[root_id]

            stem = {
                "qacMorphemeRef": qac_ref,
                "qacWordRef": word_ref(qac_ref),
                "arabic": row["surface_ar"],
                "morphology": morphology(row),
                "rootId": root_id,
                "rootAr": row["root"],
            }
            if row["lemma_ar"]:
                stem["lemma"] = row["lemma_ar"]
            note = analysis_notes.get(word_ref(qac_ref))
            if note:
                analysis_hits += 1
                stem["wordAnalysis"] = note
            stems.append(stem)

        ayat.append(
            {
                "ayahRef": ayah_ref,
                "arabicText": arabic_text,
                "rootedStems": stems,
            }
        )

    if not rooted_count:
        raise RequiredSourceMissing(
            f"surah {surah}: no rooted stems resolved — refusing to emit an "
            "anchor input with nothing to select"
        )
    if ayahs is not None and not any(ayah["rootedStems"] for ayah in ayat):
        raise RequiredSourceMissing(
            f"surah {surah} ayahs {ayahs[0]}-{ayahs[1]}: chunk contains no "
            "rooted stems"
        )

    # The candidate space is per root, not per occurrence. Carrying it once
    # keeps the file linear in roots rather than in stems; S1 has 23 stems over
    # 18 roots, and a long surah repeats a root dozens of times.
    roots = {
        root_id: {
            "rootId": root_id,
            "branchCandidates": branch_candidates(
                packet, activated.get(root_id, [])
            ),
            "lexicalCandidates": lexical_candidates(packet),
        }
        for root_id, packet in sorted(packets.items())
    }

    return {
        "schemaVersion": "anchor-input-v1",
        "builderVersion": BUILDER_VERSION,
        "quranDataReleaseId": quran_data_release_id,
        "surah": surah,
        "ayahRange": list(ayahs) if ayahs else None,
        "roots": roots,
        "coverage": {
            "rootedStems": rooted_count,
            "roots": len(packets),
            "wordAnalysis": {
                "state": analysis_state,
                "stemsWithNote": analysis_hits,
                "note": (
                    "aligned_qac_word_ref is a word-analysis claim, not a QAC "
                    "identity; stems without a note are recorded here rather "
                    "than repaired"
                ),
            },
            "v12ActivatedRoots": len(activated),
        },
        "ayat": ayat,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument(
        "--ayahs",
        help="ayah chunk, e.g. '1' or '1-20'. The candidate space is per root, "
        "so a long surah is seeded in chunks and the parts concatenate.",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    ayahs = parse_ayah_range(args.ayahs)
    suffix = f".{ayahs[0]}-{ayahs[1]}" if ayahs else ""
    output = args.output or (
        V1_DIR / "anchors" / "input" / f"s{args.surah:03d}{suffix}.anchor-input.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    bundle = build_anchor_input(args.surah, ayahs)
    with output.open("w", encoding="utf-8") as handle:
        json.dump(bundle, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    coverage = bundle["coverage"]
    print(
        f"{output}: {coverage['rootedStems']} rooted stems, "
        f"{coverage['roots']} roots, "
        f"{coverage['wordAnalysis']['stemsWithNote']} with a word-analysis note"
    )


if __name__ == "__main__":
    main()
