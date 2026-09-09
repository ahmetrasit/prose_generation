"""Explicitly reviewed additions to the compact V5 evidence contract.

These five 29:38 items were approved individually. Do not expand this into an
automatic context crawl or import complete neighboring root inventories.
"""

from __future__ import annotations

import copy
from collections.abc import Callable
from pathlib import Path
from typing import Any

from _commentary.v5 import packet_evidence


MICRO_REFERENCES = {
    "29:38": {
        "29:38:23:inverse-rare-echo": "7:201",
        "29:38:22:next-ayah-participle-echo": "29:39",
    },
}
MACRO_LEXICAL_SOURCES = {
    "29:38": {
        "root_000347/B011": "29:44",
        "root_001222/B008": "29:31",
        "root_001273/B012": "29:28",
    },
}
LEXICAL_FIELDS = (
    "branch_ref", "concept_gloss", "source_phrase_ar", "sources",
    "lexicalization_scope", "what_is_ar", "what_is_not_ar",
)


class SupplementError(ValueError):
    """An explicitly requested source item cannot be supplied completely."""


def attach(
    packets: dict[str, dict[str, Any]],
    quran_evidence: dict[str, dict[str, Any]],
    morphology_path: Path,
    cache_dir: Path,
    load_bundle: Callable[[str], dict[str, Any]],
) -> dict[str, Any]:
    """Add only reviewed evidence owned by candidates in these lane packets."""
    focus_ref = packets["micro"]["identity"]["ayah_ref"]
    topics = {
        candidate.get("source_local_id")
        for candidate in packets["micro"]["candidate_inventory"]
        if candidate.get("source_type") == "word_analysis"
    }
    refs = sorted({
        ref for topic, ref in MICRO_REFERENCES.get(focus_ref, {}).items()
        if topic in topics
    }, key=lambda ref: tuple(map(int, ref.split(":"))))
    requested_branches = {
        ref for candidate in packets["macro"]["candidate_inventory"]
        for ref in candidate.get("branch_refs", [])
    }
    branches = {
        ref: source_ref
        for ref, source_ref in MACRO_LEXICAL_SOURCES.get(focus_ref, {}).items()
        if ref in requested_branches
    }

    references = None
    if refs:
        missing_arabic = [ref for ref in refs
                          if not quran_evidence.get(ref, {}).get("arabic_uthmani")]
        if missing_arabic:
            raise SupplementError("Reviewed reference Arabic is missing: " + ", ".join(missing_arabic))
        morphology, error, source_hash = packet_evidence._morphology(
            morphology_path, set(refs), cache_dir)
        missing_morphology = [ref for ref in refs if not morphology.get(ref)]
        if error or missing_morphology:
            raise SupplementError(
                "Reviewed reference QAC morphology is unavailable: "
                + (error or ", ".join(missing_morphology)))
        references = {
            "morpheme_columns": list(packet_evidence.MORPHEME_COLUMNS),
            "context": [{
                "ayah_ref": ref,
                "arabic_uthmani": quran_evidence[ref]["arabic_uthmani"],
                "morphemes": morphology[ref],
            } for ref in refs],
        }
    else:
        source_hash = None

    lexical = []
    source_pointers = {}
    for branch_ref, source_ref in branches.items():
        bundle = load_bundle(source_ref)
        root_id = branch_ref.split("/", 1)[0]
        records = bundle.get("root_lexicon", {}).get(root_id, {}).get(
            "dictionary_entry", {}).get("branches", [])
        matches = [(index, row) for index, row in enumerate(records)
                   if row.get("branch_ref") == branch_ref]
        if len(matches) != 1:
            raise SupplementError(f"Reviewed lexical branch {branch_ref} is missing or duplicated in {source_ref}")
        index, record = matches[0]
        if any(record.get(field) in (None, "", [], {}) for field in LEXICAL_FIELDS):
            raise SupplementError(f"Reviewed lexical branch {branch_ref} has incomplete source fields")
        lexical.append({field: copy.deepcopy(record[field]) for field in LEXICAL_FIELDS})
        source_pointers[branch_ref] = {
            "ayah_ref": source_ref,
            "pointer": f"/root_lexicon/{root_id}/dictionary_entry/branches/{index}",
        }

    # Publish together only after every requested source has been checked.
    if references is not None:
        packets["micro"]["reference_evidence"] = references
    if lexical:
        packets["macro"]["lexical_evidence"] = lexical
    return {
        "micro_reference_refs": refs,
        "qac_source_sha256": source_hash,
        "macro_lexical_sources": source_pointers,
    }
