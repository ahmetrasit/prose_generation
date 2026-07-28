#!/usr/bin/env python3
"""Join an authored translation file to the spine and emit translation-layer-v1.

Decision D1 in `README.md`: the writer authors four kinds of content and nothing
else. Every identity — QAC refs, root ids, branch ids, gloss ids — comes from the
input bundle here, which makes transcription error structurally impossible rather
than merely detectable.

Decision D2: the artifact records what produced it, so that "the same workflow"
is a checkable fact rather than an assertion.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

V1_DIR = Path(__file__).resolve().parents[1]

ASSEMBLER_VERSION = "translation-v1-assembler-1"


class AuthoredFileInvalid(RuntimeError):
    """The authored file does not join cleanly to the spine."""


def read_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(bundle: dict, authored: dict, language: str, surah: int) -> list[str]:
    """Check only what the writer authored. Identities are not checked because
    the writer no longer supplies them."""
    errors: list[str] = []

    if authored.get("schemaVersion") != "translation-authored-v1":
        errors.append(
            "schemaVersion: expected 'translation-authored-v1', found "
            f"{authored.get('schemaVersion')!r}"
        )
    if authored.get("language") != language:
        errors.append(
            f"language: expected {language!r}, found {authored.get('language')!r}"
        )
    if authored.get("surah") != surah:
        errors.append(f"surah: expected {surah}, found {authored.get('surah')!r}")

    glosses = authored.get("glosses")
    if not isinstance(glosses, dict):
        return errors + ["glosses must be an object keyed by qacMorphemeRef"]
    ayat = authored.get("ayat")
    if not isinstance(ayat, dict):
        return errors + ["ayat must be an object keyed by ayahRef"]

    all_refs = {
        card["qacMorphemeRef"] for ayah in bundle["ayat"] for card in ayah["cards"]
    }
    missing_glosses = authored.get("missingGlosses") or []
    excused = set()
    for index, missing in enumerate(missing_glosses):
        ref = missing.get("qacMorphemeRef") if isinstance(missing, dict) else None
        if ref not in all_refs:
            errors.append(f"missingGlosses[{index}]: unknown ref {ref!r}")
            continue
        if not missing.get("reason"):
            errors.append(f"missingGlosses[{index}]: reason must be nonempty")
        excused.add(ref)
    if missing_glosses:
        errors.append(
            f"{len(missing_glosses)} unresolved occurrence gloss(es): the surah "
            "is not complete"
        )

    unknown_glosses = sorted(set(glosses) - all_refs)
    if unknown_glosses:
        errors.append(f"glosses for unknown morphemes: {unknown_glosses}")

    for ayah in bundle["ayat"]:
        label = ayah["ayahRef"]
        for card in ayah["cards"]:
            ref = card["qacMorphemeRef"]
            authored_gloss = glosses.get(ref)
            if authored_gloss is None:
                if ref not in excused:
                    errors.append(f"{label}: no gloss authored for {ref}")
                continue
            if not authored_gloss.get("card"):
                errors.append(f"{ref}: card gloss must be nonempty")
            rooted = "rootId" in card
            occurrence = authored_gloss.get("occurrence")
            if rooted and not occurrence:
                errors.append(f"{ref}: rooted card requires an occurrence gloss")
            if not rooted and occurrence:
                errors.append(
                    f"{ref}: unrooted card must not carry an occurrence gloss"
                )

    expected_ayah_refs = [ayah["ayahRef"] for ayah in bundle["ayat"]]
    unknown_ayat = sorted(set(ayat) - set(expected_ayah_refs))
    if unknown_ayat:
        errors.append(f"translations for unknown ayahs: {unknown_ayat}")

    for ayah_ref in expected_ayah_refs:
        translation = ayat.get(ayah_ref)
        if translation is None:
            errors.append(f"{ayah_ref}: no translation authored")
            continue
        text = translation.get("text")
        tokens = translation.get("targetTokens")
        if not isinstance(text, str) or not text:
            errors.append(f"{ayah_ref}: translation text must be nonempty")
            text = ""
        if not isinstance(tokens, list) or not tokens:
            errors.append(f"{ayah_ref}: targetTokens must be a nonempty array")
            continue

        rebuilt = ""
        for index, token in enumerate(tokens):
            token_text = token.get("text")
            separator = token.get("separatorAfter")
            refs = token.get("qacMorphemeRefs")
            if not isinstance(token_text, str) or not token_text:
                errors.append(f"{ayah_ref} token {index}: text must be nonempty")
                token_text = ""
            if not isinstance(separator, str):
                errors.append(
                    f"{ayah_ref} token {index}: separatorAfter must be a string"
                )
                separator = ""
            if not isinstance(refs, list) or not refs:
                errors.append(
                    f"{ayah_ref} token {index}: qacMorphemeRefs must be nonempty"
                )
                refs = []
            elif len(refs) != len(set(refs)):
                errors.append(f"{ayah_ref} token {index}: duplicate qacMorphemeRefs")
            unknown = sorted(set(refs) - all_refs)
            if unknown:
                errors.append(f"{ayah_ref} token {index}: unknown refs {unknown}")
            rebuilt += token_text + separator

        if rebuilt != text:
            errors.append(
                f"{ayah_ref}: targetTokens reconstruct {rebuilt!r}, not {text!r}"
            )

    return errors


def assemble(
    bundle: dict,
    authored: dict,
    language: str,
    surah: int,
    provenance: dict,
) -> dict:
    glosses = authored["glosses"]

    ayat = []
    for source_ayah in bundle["ayat"]:
        cards = []
        for source_card in source_ayah["cards"]:
            ref = source_card["qacMorphemeRef"]
            authored_gloss = glosses[ref]
            card = {
                "qacMorphemeRef": ref,
                "qacWordRef": source_card["qacWordRef"],
                "cardGloss": authored_gloss["card"],
            }
            if "rootId" in source_card:
                gloss_id = source_card["glossId"]
                card.update(
                    {
                        "rootId": source_card["rootId"],
                        "branchIds": source_card["branchIds"],
                        "occurrenceGloss": {
                            "glossId": gloss_id,
                            "text": authored_gloss["occurrence"],
                        },
                        "selectedGlossId": gloss_id,
                    }
                )
            cards.append(card)

        translation = authored["ayat"][source_ayah["ayahRef"]]
        ayat.append(
            {
                "ayahRef": source_ayah["ayahRef"],
                "cards": cards,
                "translation": {
                    "text": translation["text"],
                    "targetTokens": translation["targetTokens"],
                },
            }
        )

    return {
        "schemaVersion": "translation-layer-v1",
        "language": language,
        "quranDataReleaseId": bundle["quranDataReleaseId"],
        "surah": surah,
        "missingGlosses": authored.get("missingGlosses", []),
        "provenance": provenance,
        "ayat": ayat,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--language", required=True)
    parser.add_argument("--bundle", type=Path)
    parser.add_argument("--authored", type=Path)
    parser.add_argument("--anchors", type=Path)
    parser.add_argument("--prompt", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--model",
        help="model id that produced the authored file, recorded in provenance",
    )
    args = parser.parse_args()

    surah_key = f"s{args.surah:03d}"
    bundle_path = args.bundle or V1_DIR / "input" / args.language / f"{surah_key}.json"
    authored_path = args.authored or (
        V1_DIR / "authored" / args.language / f"{surah_key}.authored.json"
    )
    anchors_path = args.anchors or (
        V1_DIR / "source" / f"{surah_key}.primary-anchors.json"
    )
    prompt_path = args.prompt or (
        V1_DIR / "prompts" / f"{surah_key}.translation.{args.language}.prompt.md"
    )
    output_path = args.output or (
        V1_DIR / "output" / args.language / f"{surah_key}.json"
    )

    bundle = read_json(bundle_path)
    authored = read_json(authored_path)

    errors = validate(bundle, authored, args.language, args.surah)
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)

    provenance = {
        "quranDataReleaseId": bundle["quranDataReleaseId"],
        "anchorsSha256": sha256(anchors_path),
        "bundleSha256": sha256(bundle_path),
        "authoredSha256": sha256(authored_path),
        "assemblerVersion": ASSEMBLER_VERSION,
    }
    if prompt_path.exists():
        provenance["promptSha256"] = sha256(prompt_path)
    if args.model:
        provenance["model"] = {"id": args.model}

    artifact = assemble(bundle, authored, args.language, args.surah, provenance)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(artifact, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"OK: {output_path}")


if __name__ == "__main__":
    main()
