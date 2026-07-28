#!/usr/bin/env python3
"""Mechanically check one assembled translation-layer artifact against its bundle.

Since decision D1 the writer no longer supplies identities — `tools/assemble.py`
joins them from the spine — so the identity checks here are a regression test on
the assembler rather than a guard against model transcription error. What they
still catch is a bundle/artifact mismatch: an artifact assembled against a
different release, a different anchor seed, or a stale bundle.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


V1_DIR = Path(__file__).resolve().parents[1]

TOP_KEYS = {
    "schemaVersion",
    "language",
    "quranDataReleaseId",
    "surah",
    "missingGlosses",
    "provenance",
    "ayat",
}
REQUIRED_PROVENANCE_KEYS = {
    "quranDataReleaseId",
    "anchorsSha256",
    "bundleSha256",
    "authoredSha256",
    "assemblerVersion",
}
AYAH_KEYS = {"ayahRef", "cards", "translation"}
CARD_KEYS = {
    "qacMorphemeRef",
    "qacWordRef",
    "rootId",
    "branchIds",
    "occurrenceGloss",
    "selectedGlossId",
    "cardGloss",
}
TRANSLATION_KEYS = {"text", "targetTokens"}
TOKEN_KEYS = {"text", "separatorAfter", "qacMorphemeRefs"}
OCCURRENCE_GLOSS_KEYS = {"glossId", "text"}
MISSING_GLOSS_KEYS = {"qacMorphemeRef", "reason"}
LOCKED_CARD_KEYS = (
    "qacMorphemeRef",
    "qacWordRef",
    "rootId",
    "branchIds",
)


def read_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def extra_keys(value: dict, allowed: set[str]) -> set[str]:
    return set(value) - allowed


def check(bundle: dict, output: dict, surah: int, language: str) -> list[str]:
    errors: list[str] = []

    extras = extra_keys(output, TOP_KEYS)
    if extras:
        errors.append(f"output has unsupported fields: {sorted(extras)}")

    expected_top = {
        "schemaVersion": "translation-layer-v1",
        "language": language,
        "quranDataReleaseId": bundle["quranDataReleaseId"],
        "surah": surah,
    }
    for key, expected in expected_top.items():
        if output.get(key) != expected:
            errors.append(
                f"{key}: expected {expected!r}, found {output.get(key)!r}"
            )

    # D2: an artifact that cannot say what produced it cannot support the claim
    # that a re-run is the same workflow.
    provenance = output.get("provenance")
    if not isinstance(provenance, dict):
        errors.append("provenance must be an object")
    else:
        absent = sorted(REQUIRED_PROVENANCE_KEYS - set(provenance))
        if absent:
            errors.append(f"provenance is missing {absent}")
        if provenance.get("quranDataReleaseId") != bundle["quranDataReleaseId"]:
            errors.append(
                "provenance.quranDataReleaseId does not match the bundle: "
                f"{provenance.get('quranDataReleaseId')!r} vs "
                f"{bundle['quranDataReleaseId']!r}"
            )

    all_source_refs = {
        card["qacMorphemeRef"]
        for ayah in bundle["ayat"]
        for card in ayah["cards"]
    }
    missing_glosses = output.get("missingGlosses")
    if not isinstance(missing_glosses, list):
        errors.append("missingGlosses must be an array")
    else:
        for index, missing in enumerate(missing_glosses):
            if not isinstance(missing, dict):
                errors.append(f"missingGlosses[{index}] must be an object")
                continue
            extras = extra_keys(missing, MISSING_GLOSS_KEYS)
            if extras:
                errors.append(
                    f"missingGlosses[{index}] has unsupported fields: "
                    f"{sorted(extras)}"
                )
            ref = missing.get("qacMorphemeRef")
            if ref not in all_source_refs:
                errors.append(
                    f"missingGlosses[{index}] has unknown ref {ref!r}"
                )
            if not isinstance(missing.get("reason"), str) or not missing["reason"]:
                errors.append(
                    f"missingGlosses[{index}].reason must be nonempty"
                )
        if missing_glosses:
            errors.append(
                f"output has {len(missing_glosses)} unresolved occurrence gloss(es)"
            )

    output_ayat = output.get("ayat")
    if not isinstance(output_ayat, list):
        return errors + ["ayat must be an array"]
    if len(output_ayat) != len(bundle["ayat"]):
        errors.append(
            f"ayat count: expected {len(bundle['ayat'])}, found {len(output_ayat)}"
        )

    for index, source_ayah in enumerate(bundle["ayat"]):
        if index >= len(output_ayat):
            break
        ayah = output_ayat[index]
        label = source_ayah["ayahRef"]
        if not isinstance(ayah, dict):
            errors.append(f"{label}: ayah must be an object")
            continue

        extras = extra_keys(ayah, AYAH_KEYS)
        if extras:
            errors.append(f"{label}: unsupported ayah fields: {sorted(extras)}")
        if ayah.get("ayahRef") != label:
            errors.append(
                f"ayah {index}: expected ref {label!r}, found {ayah.get('ayahRef')!r}"
            )

        source_cards = source_ayah["cards"]
        cards = ayah.get("cards")
        if not isinstance(cards, list):
            errors.append(f"{label}: cards must be an array")
            continue
        if len(cards) != len(source_cards):
            errors.append(
                f"{label}: expected {len(source_cards)} cards, found {len(cards)}"
            )

        source_refs = {
            source_card["qacMorphemeRef"] for source_card in source_cards
        }
        for card_index, source_card in enumerate(source_cards):
            if card_index >= len(cards):
                break
            card = cards[card_index]
            if not isinstance(card, dict):
                errors.append(f"{label} card {card_index}: must be an object")
                continue
            extras = extra_keys(card, CARD_KEYS)
            if extras:
                errors.append(
                    f"{label} card {card_index}: unsupported fields: {sorted(extras)}"
                )
            for key in LOCKED_CARD_KEYS:
                if card.get(key) != source_card.get(key):
                    errors.append(
                        f"{label} card {card_index} {key}: expected "
                        f"{source_card.get(key)!r}, found {card.get(key)!r}"
                    )
            if not isinstance(card.get("cardGloss"), str) or not card["cardGloss"]:
                errors.append(f"{label} card {card_index}: cardGloss must be nonempty")

            rooted = "rootId" in source_card
            occurrence = card.get("occurrenceGloss")
            selected_gloss_id = card.get("selectedGlossId")
            if rooted:
                expected_gloss_id = source_card["glossId"]
                if not isinstance(occurrence, dict):
                    errors.append(
                        f"{label} card {card_index}: rooted card requires "
                        "occurrenceGloss"
                    )
                else:
                    extras = extra_keys(occurrence, OCCURRENCE_GLOSS_KEYS)
                    if extras:
                        errors.append(
                            f"{label} card {card_index}: occurrenceGloss has "
                            f"unsupported fields {sorted(extras)}"
                        )
                    if occurrence.get("glossId") != expected_gloss_id:
                        errors.append(
                            f"{label} card {card_index}: occurrence gloss ID "
                            f"expected {expected_gloss_id!r}, found "
                            f"{occurrence.get('glossId')!r}"
                        )
                    if (
                        not isinstance(occurrence.get("text"), str)
                        or not occurrence["text"]
                    ):
                        errors.append(
                            f"{label} card {card_index}: occurrence gloss text "
                            "must be nonempty"
                        )
                if selected_gloss_id != expected_gloss_id:
                    errors.append(
                        f"{label} card {card_index}: selectedGlossId expected "
                        f"{expected_gloss_id!r}, found {selected_gloss_id!r}"
                    )
            elif occurrence is not None or selected_gloss_id is not None:
                errors.append(
                    f"{label} card {card_index}: unrooted card must not have "
                    "occurrence gloss fields"
                )

        translation = ayah.get("translation")
        if not isinstance(translation, dict):
            errors.append(f"{label}: translation must be an object")
            continue
        extras = extra_keys(translation, TRANSLATION_KEYS)
        if extras:
            errors.append(
                f"{label}: unsupported translation fields: {sorted(extras)}"
            )
        text = translation.get("text")
        tokens = translation.get("targetTokens")
        if not isinstance(text, str) or not text:
            errors.append(f"{label}: translation.text must be nonempty")
        if not isinstance(tokens, list) or not tokens:
            errors.append(f"{label}: targetTokens must be a nonempty array")
            continue

        rebuilt = ""
        for token_index, token in enumerate(tokens):
            if not isinstance(token, dict):
                errors.append(f"{label} token {token_index}: must be an object")
                continue
            extras = extra_keys(token, TOKEN_KEYS)
            if extras:
                errors.append(
                    f"{label} token {token_index}: unsupported fields: {sorted(extras)}"
                )
            token_text = token.get("text")
            separator = token.get("separatorAfter")
            refs = token.get("qacMorphemeRefs")
            if not isinstance(token_text, str) or not token_text:
                errors.append(f"{label} token {token_index}: text must be nonempty")
                token_text = ""
            if not isinstance(separator, str):
                errors.append(
                    f"{label} token {token_index}: separatorAfter must be a string"
                )
                separator = ""
            if not isinstance(refs, list) or not refs:
                errors.append(
                    f"{label} token {token_index}: qacMorphemeRefs must be nonempty"
                )
                refs = []
            elif len(refs) != len(set(refs)):
                errors.append(
                    f"{label} token {token_index}: duplicate qacMorphemeRefs"
                )
            unknown = set(refs) - source_refs
            if unknown:
                errors.append(
                    f"{label} token {token_index}: unknown refs {sorted(unknown)}"
                )
            rebuilt += token_text + separator

        if isinstance(text, str) and rebuilt != text:
            errors.append(
                f"{label}: targetTokens reconstruct {rebuilt!r}, not {text!r}"
            )

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--language", required=True)
    parser.add_argument("--bundle", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    surah_key = f"s{args.surah:03d}"
    bundle_path = (
        args.bundle
        or V1_DIR / "input" / args.language / f"{surah_key}.json"
    )
    output_path = (
        args.output
        or V1_DIR / "output" / args.language / f"{surah_key}.json"
    )

    errors = check(
        read_json(bundle_path),
        read_json(output_path),
        args.surah,
        args.language,
    )
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
    print(f"OK: {output_path}")


if __name__ == "__main__":
    main()
