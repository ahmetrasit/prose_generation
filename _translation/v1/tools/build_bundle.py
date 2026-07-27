#!/usr/bin/env python3
"""Build a compact translation-agent bundle from live sibling-repo data."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


V1_DIR = Path(__file__).resolve().parents[1]
WORKSPACE = V1_DIR.parents[2]


def read_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def word_ref(morpheme_ref: str) -> str:
    return morpheme_ref.rsplit(":", 1)[0]


def morphology(row: dict[str, str]) -> dict[str, str]:
    result = {
        "role": row["morpheme_role"],
        "pos": row["pos"],
    }
    optional = {
        "aspect": "aspect",
        "mood": "mood",
        "voice": "voice",
        "measure": "measure",
        "person": "person",
        "gender": "gender",
        "number": "number",
        "case": "grammatical_case",
    }
    for output_key, source_key in optional.items():
        if row[source_key]:
            result[output_key] = row[source_key]
    return result


def language_policy(language: str) -> dict:
    if language == "tr":
        return {
            "standard": "Contemporary Standard Turkey Turkish",
            "loanwordRule": "Use no loanwords. Allah is the only exception.",
            "allowedLoanwords": ["Allah"],
            "fallbackRule": (
                "When no single native word is adequate, write a short, "
                "transparent Turkish phrase instead of using a conventional "
                "Quran-translation loanword."
            ),
        }
    return {
        "standard": f"Contemporary standard language for {language}",
        "loanwordRule": "Follow ordinary target-language usage.",
        "allowedLoanwords": [],
    }


def gloss_evidence(source: dict, error_key: str = "error") -> dict:
    evidence = {
        "text": source["text"],
        "facetIds": source.get("facet_ids", []),
    }
    error = source.get(error_key, {})
    if error.get("fit"):
        evidence["fit"] = error["fit"]
    if error.get("loses_facet_ids"):
        evidence["losesFacetIds"] = error["loses_facet_ids"]
    if error.get("reason"):
        evidence["lossReason"] = error["reason"]
    return evidence


def reviewed_entry_gloss_source(
    language: str,
    root_id: str,
    branch_ids: list[str],
    lexical_unit_ids: list[str],
) -> dict | None:
    path = (
        WORKSPACE
        / "dictionary"
        / "v2"
        / "work"
        / "entry_creation"
        / root_id
        / language
        / "fragments"
        / f"{root_id}_entry.json"
    )
    if not path.exists():
        return None

    entry = read_json(path)
    branch_cores: list[dict] = []
    contextual_senses: list[dict] = []
    lexical_senses: list[dict] = []
    for branch_id in branch_ids:
        branch_ref = f"{root_id}/{branch_id}"
        branch = next(
            item for item in entry["branches"] if item["branch_ref"] == branch_ref
        )
        branch_cores.append(
            {
                "branchId": branch_id,
                **gloss_evidence(
                    branch["concept_gloss"],
                    error_key="error_profile",
                ),
            }
        )
        for contextual in branch.get("contextual_glosses", []):
            contextual_senses.append(
                {
                    "branchId": branch_id,
                    **gloss_evidence(
                        contextual,
                        error_key="error_profile",
                    ),
                }
            )
        lexical_by_id = {
            item["lexical_unit_id"]: item
            for item in branch.get("lexical_glosses", [])
        }
        for lexical_unit_id in lexical_unit_ids:
            lexical = lexical_by_id.get(lexical_unit_id)
            if lexical:
                lexical_senses.append(
                    {
                        "branchId": branch_id,
                        "lexicalUnitId": lexical_unit_id,
                        "text": lexical["target_gloss"],
                        "facetIds": [],
                    }
                )

    return {
        "evidenceLanguage": language,
        "branchCores": branch_cores,
        "contextualSenses": contextual_senses,
        "lexicalSenses": lexical_senses,
    }


def bridge_gloss_source(
    root_id: str,
    branch_ids: list[str],
    lexical_unit_ids: list[str],
) -> dict:
    path = WORKSPACE / "dictionary" / "data" / "output" / "root_packets" / f"{root_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"Missing dictionary evidence for {root_id}: {path}")

    packet = read_json(path)
    branch_cores: list[dict] = []
    contextual_senses: list[dict] = []
    lexical_senses: list[dict] = []
    lexical_by_id = {
        item["lexical_unit_id"]: item for item in packet["lexical_senses"]
    }
    for branch_id in branch_ids:
        branch = next(
            item for item in packet["branches"] if item["branch_id"] == branch_id
        )
        branch_cores.append(
            {
                "branchId": branch_id,
                "text": branch.get("what_is_en") or branch["branch_image_en"],
                "facetIds": [],
            }
        )
        if branch.get("branch_image_en"):
            contextual_senses.append(
                {
                    "branchId": branch_id,
                    "text": branch["branch_image_en"],
                    "facetIds": [],
                }
            )
        for lexical_unit_id in lexical_unit_ids:
            lexical = lexical_by_id.get(lexical_unit_id)
            if lexical and branch_id in lexical["branch_ids"].split():
                lexical_senses.append(
                    {
                        "branchId": branch_id,
                        "lexicalUnitId": lexical_unit_id,
                        "text": lexical["sense_en"],
                        "facetIds": [],
                        "fit": lexical.get("sense_en_fit", "close"),
                    }
                )

    return {
        "evidenceLanguage": "en",
        "branchCores": branch_cores,
        "contextualSenses": contextual_senses,
        "lexicalSenses": lexical_senses,
    }


def gloss_source(
    language: str,
    root_id: str,
    branch_ids: list[str],
    lexical_unit_ids: list[str],
) -> dict:
    result_path = (
        WORKSPACE
        / "dictionary"
        / "v2"
        / "gloss_generation"
        / "results"
        / language
        / f"{root_id}.json"
    )
    if not result_path.exists():
        reviewed_entry = reviewed_entry_gloss_source(
            language,
            root_id,
            branch_ids,
            lexical_unit_ids,
        )
        if reviewed_entry:
            return reviewed_entry
        return bridge_gloss_source(root_id, branch_ids, lexical_unit_ids)

    result = read_json(result_path)
    branch_cores: list[dict] = []
    contextual_senses: list[dict] = []
    lexical_senses: list[dict] = []

    for branch_id in branch_ids:
        branch_ref = f"{root_id}/{branch_id}"
        branch = next(
            item for item in result["branches"] if item["branch_ref"] == branch_ref
        )

        concept = branch.get("concept_gloss")
        core_text = concept.get("text") if concept else None
        if not core_text:
            contextual = branch.get("contextual_glosses", [])
            core_text = contextual[0].get("text") if contextual else None
        if not core_text:
            raise ValueError(
                f"No target-language branch core for {root_id}/{branch_id} "
                f"in {language}"
            )
        branch_cores.append(
            {
                "branchId": branch_id,
                **gloss_evidence(concept or {"text": core_text}),
            }
        )

        for contextual in branch.get("contextual_glosses", []):
            contextual_senses.append(
                {
                    "branchId": branch_id,
                    **gloss_evidence(contextual),
                }
            )

        lexical_glosses = branch.get("lexical_glosses", {})
        for lexical_unit_id in lexical_unit_ids:
            lexical = lexical_glosses.get(lexical_unit_id)
            if lexical and lexical.get("text"):
                lexical_senses.append(
                    {
                        "branchId": branch_id,
                        "lexicalUnitId": lexical_unit_id,
                        **gloss_evidence(lexical),
                    }
                )

    return {
        "evidenceLanguage": language,
        "branchCores": branch_cores,
        "contextualSenses": contextual_senses,
        "lexicalSenses": lexical_senses,
    }


def root_bindings(surah: int, v12_dir: Path) -> tuple[dict[str, str], str]:
    surah_key = f"s{surah:03d}"
    crosswalk_path = (
        WORKSPACE
        / "quran-apps"
        / "packages"
        / "content-compiler"
        / "crosswalks"
        / f"{surah_key}-qac-root-to-furuq.json"
    )
    if crosswalk_path.exists():
        crosswalk = read_json(crosswalk_path)
        return (
            {
                item["qacRootJoinKey"]: item["furuqRootId"]
                for item in crosswalk["mappings"]
            },
            crosswalk["quranDataReleaseId"],
        )

    anchor_map = read_json(v12_dir / "anchor_map.v3.json")
    columns = {name: index for index, name in enumerate(anchor_map["columns"])}
    candidates: dict[str, set[str]] = {}
    for row in anchor_map["rows"]:
        join_key = "".join(row[columns["source_root"]].split())
        candidates.setdefault(join_key, set()).add(row[columns["root_id"]])
    ambiguous = {key: ids for key, ids in candidates.items() if len(ids) != 1}
    if ambiguous:
        raise ValueError(f"Ambiguous V12 root bindings: {ambiguous}")

    release = read_json(WORKSPACE / "quran-data" / "RELEASE.json")
    return (
        {key: next(iter(ids)) for key, ids in candidates.items()},
        release["release_id"],
    )


def grammar_unit_ref(unit_id: str) -> str | None:
    value = unit_id.strip()
    parts = value.split(":")
    if (
        len(parts) == 4
        and parts[0] == "q"
        and all(part.isdigit() for part in parts[1:])
    ):
        return value
    return None


def grammar_support_by_ayah(surah: int) -> dict[str, list[dict]]:
    path = (
        WORKSPACE
        / "quran-data"
        / "data"
        / "grammar"
        / "attachments"
        / "translation_support.tsv"
    )
    support: dict[str, list[dict]] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["row_kind"] != "support" or int(row["sura"]) != surah:
                continue

            refs: list[str] = []
            raw_refs = [row["anchor_unit_id"]]
            raw_refs.extend(row["related_word_unit_ids"].split(";"))
            for raw_ref in raw_refs:
                ref = grammar_unit_ref(raw_ref)
                if ref and ref not in refs:
                    refs.append(ref)
            if not row["risk"]:
                continue

            item = {
                "type": row["support_type"],
                "instruction": row["translation_instruction"],
                "guidance": row["risk"],
            }
            if refs:
                item["grammarUnitRefs"] = refs
            if row["construction"]:
                item["construction"] = row["construction"]
            if row["scope"]:
                item["scope"] = row["scope"]
            if row["force"]:
                item["force"] = row["force"]

            ayah_ref = f"{surah}:{int(row['ayah'])}"
            support.setdefault(ayah_ref, []).append(item)
    return support


def reading_alignment(baseline: dict) -> list[dict[str, list[str]]]:
    groups: list[dict[str, list[str]]] = []
    for _, refs in baseline["target_tokens"]:
        if groups and groups[-1]["qacWordRefs"] == refs:
            continue
        groups.append({"qacWordRefs": refs})
    return groups


def occurrence_gloss_id(language: str, qac_ref: str) -> str:
    return f"{language}:v1:{qac_ref}"


def build_bundle(surah: int, language: str) -> dict:
    surah_key = f"s{surah:03d}"
    v12_dir = (
        WORKSPACE / "latent_activation" / "_status" / "v12_cross_run" / surah_key
    )
    roster = read_json(v12_dir / "ayah_roster.v3.json")
    anchor_seed = read_json(
        V1_DIR / "source" / f"{surah_key}.primary-anchors.json"
    )
    anchors = {
        item["qacMorphemeRef"]: item for item in anchor_seed["anchors"]
    }

    root_ids, quran_data_release_id = root_bindings(surah, v12_dir)
    grammar_support = grammar_support_by_ayah(surah)

    morphemes_by_ayah: dict[str, list[dict[str, str]]] = {}
    with (v12_dir / "linguistic" / "morphemes.tsv").open(
        encoding="utf-8", newline=""
    ) as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            ayah_ref = ":".join(row["qac_ref"].split(":")[:2])
            morphemes_by_ayah.setdefault(ayah_ref, []).append(row)

    ayat = []
    for v12_ref, arabic_text, ayah_ref, baseline in roster["rows"]:
        del v12_ref
        cards = []
        for row in morphemes_by_ayah[ayah_ref]:
            qac_ref = row["qac_ref"]
            card = {
                "qacMorphemeRef": qac_ref,
                "qacWordRef": word_ref(qac_ref),
                "arabic": row["surface_ar"],
                "morphology": morphology(row),
            }
            if row["lemma_ar"]:
                card["lemma"] = row["lemma_ar"]

            anchor = anchors.get(qac_ref)
            if row["root_join_key"]:
                if anchor is None:
                    raise ValueError(f"Missing primary anchor for rooted {qac_ref}")
                root_id = root_ids[row["root_join_key"]]
                branch_ids = anchor["branchIds"]
                lexical_unit_ids = anchor.get("lexicalUnitIds", [])
                card.update(
                    {
                        "rootId": root_id,
                        "branchIds": branch_ids,
                        "glossId": occurrence_gloss_id(language, qac_ref),
                        "glossSource": gloss_source(
                            language,
                            root_id,
                            branch_ids,
                            lexical_unit_ids,
                        ),
                    }
                )
            elif anchor is not None:
                raise ValueError(f"Unexpected anchor on unrooted {qac_ref}")

            cards.append(card)

        ayat.append(
            {
                "ayahRef": ayah_ref,
                "arabicText": arabic_text,
                "primaryReading": {
                    "alignmentGroups": reading_alignment(baseline),
                },
                "grammarSupport": grammar_support.get(ayah_ref, []),
                "cards": cards,
            }
        )

    return {
        "schemaVersion": "translation-input-v1",
        "targetLanguage": language,
        "languagePolicy": language_policy(language),
        "quranDataReleaseId": quran_data_release_id,
        "surah": surah,
        "ayat": ayat,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--language", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    surah_key = f"s{args.surah:03d}"
    output = args.output or V1_DIR / "input" / args.language / f"{surah_key}.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        json.dump(
            build_bundle(args.surah, args.language),
            handle,
            ensure_ascii=False,
            indent=2,
        )
        handle.write("\n")


if __name__ == "__main__":
    main()
