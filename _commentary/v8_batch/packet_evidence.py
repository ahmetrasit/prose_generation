"""Inline target evidence and decoding for historical V5 compact packets."""

from __future__ import annotations

import sqlite3
import zlib
from pathlib import Path
from typing import Any

from _commentary.v8_batch.composition import normalize_arabic_surface
from _commentary.v8_batch.qac_cache import DEFAULT_CACHE_DIR, open_database


MORPHEME_COLUMNS = (
    "qac_ref", "surface_ar", "lemma_ar", "root_ar", "pos",
    "morpheme_role", "morph_features",
)


def _morphology(
    path: Path, refs: set[str], cache_dir: Path = DEFAULT_CACHE_DIR,
) -> tuple[dict[str, list[list[Any]]], str | None, str | None]:
    """Return projected rows, a path-free qualification, and source SHA-256."""
    if not refs:
        return {}, None, None
    if not path.is_file():
        return {}, "QAC morphology source is unavailable", None
    source_hash = None
    try:
        with open_database(path, cache_dir) as (connection, source_hash):
            columns = ", ".join(MORPHEME_COLUMNS)
            result = {}
            for ref in sorted(refs, key=lambda r: tuple(map(int, r.split(":")))):
                surah, ayah = map(int, ref.split(":"))
                rows = connection.execute(
                    f"SELECT {columns} FROM qac_morphemes "
                    "WHERE surah = ? AND ayah = ? ORDER BY word_index, morpheme_index",
                    (surah, ayah),
                ).fetchall()
                if any(not str(row[0]).startswith(ref + ":") for row in rows):
                    raise ValueError(f"QAC identity mismatch for {ref}")
                if rows:
                    result[ref] = [list(row) for row in rows]
            return result, None, source_hash
    except (OSError, EOFError, sqlite3.Error, ValueError, zlib.error) as exc:
        # Missing morphology limits claims; it does not erase the Arabic or
        # turn the absence of evidence into a semantic rejection.
        return {}, f"QAC morphology could not be projected ({type(exc).__name__})", source_hash


def attach_context_evidence(
    packets: dict[str, dict[str, Any]],
    quran_evidence: dict[str, dict[str, Any]],
    morphology_path: Path,
    cache_dir: Path = DEFAULT_CACHE_DIR,
) -> None:
    refs = {
        ref
        for packet in packets.values()
        for ref in packet["review_inventory"]["context_refs"]
    }
    aliases = {}
    for ref in refs:
        if ref.endswith(":0"):
            text = quran_evidence.get(ref, {}).get("arabic_uthmani", "")
            source = quran_evidence.get("1:1", {}).get("arabic_uthmani", "")
            if text and source and normalize_arabic_surface(text) == normalize_arabic_surface(source):
                aliases[ref] = "1:1"
        else:
            aliases[ref] = ref
    morphology, error, source_hash = _morphology(morphology_path, set(aliases.values()), cache_dir)
    for packet in packets.values():
        rows = []
        for ref in packet["review_inventory"]["context_refs"]:
            source = quran_evidence.get(ref, {})
            linguistic_ref = aliases.get(ref)
            rows.append({
                "ayah_ref": ref,
                "arabic_uthmani": source.get("arabic_uthmani"),
                "source_pointer": source.get("source_pointer"),
                "linguistic_source_ref": linguistic_ref,
                "morphemes": morphology.get(linguistic_ref, []),
            })
        packet["context_evidence"] = rows
        packet["context_morpheme_columns"] = list(MORPHEME_COLUMNS)
        packet["context_evidence_coverage"] = {
            "missing_arabic_refs": [r["ayah_ref"] for r in rows if not r["arabic_uthmani"]],
            "missing_morphology_refs": [r["ayah_ref"] for r in rows if not r["morphemes"]],
            "morphology_source": "qac-morphology/qac.sqlite.gz",
            "morphology_source_sha256": source_hash,
            "morphology_source_hash_basis": "compressed_source_bytes",
            "morphology_error": error,
            "boundary": (
                "Morpheme columns describe source QAC forms, not activated lexical "
                "branches. HFT word indices and root/branch identities remain "
                "nominations; bind them to these occurrences before using them. "
                "Prefatory aliases apply to morphology only, not host context."
            ),
        }
        typed_refs = {r["ayah_ref"] for r in rows if r["morphemes"]}
        if packet.get("focus", {}).get("qac_morphemes"):
            identity = packet.get("identity", {})
            typed_refs.update(
                ref for ref in (identity.get("ayah_ref"), identity.get("linguistic_source_ref"))
                if isinstance(ref, str)
            )
        hft = packet.get("hft_evidence")
        if isinstance(hft, dict):
            anchors = {
                ref for record in hft.get("assigned_records", [])
                for ref in record.get("anchor_refs", [])
            }
            missing = sorted(anchors - quran_evidence.keys())
            hft["anchor_evidence_coverage"] = {
                "cited_unique_anchor_count": len(anchors),
                "supplied_unique_anchor_count": len(anchors) - len(missing),
                "missing_anchor_refs": missing,
            }
        for item in packet.get("connection_registry", []):
            qualification = item.setdefault("qualification", {})
            qualification["target_morphology_supplied"] = item.get("target_ref") in typed_refs
            qualification["boundary"] = (
                "Assess this nomination using its exact target Arabic and the "
                "context_evidence registry; consult context_evidence_coverage "
                "for missing morphology. Retrieval labels and opposite-direction "
                "nominations or counterevidence are not focus-direction verdicts."
            )
        for support in packet.get("support_registry", []):
            coverage = support.get("anchor_evidence_coverage")
            if isinstance(coverage, dict):
                required = set(support.get("context_refs", []))
                coverage["context_morphology_refs"] = sorted(required & typed_refs)
                coverage["target_morphology_supplied"] = required <= typed_refs
                coverage["boundary"] = (
                    "Exact Arabic verifies surface contact. Independently supplied "
                    "context morphology is in context_evidence; HFT-stated word "
                    "indices and branch roles remain attributed nominations."
                )


def expand_packet(packet: dict[str, Any]) -> dict[str, Any]:
    """Decode historical v3 inline transport; new prompts use whole records."""
    shared = {row["ref"]: row["value"] for row in packet.get("shared_evidence", [])}

    def expand(value: Any) -> Any:
        if isinstance(value, dict):
            if set(value) == {"$v5_ref"}:
                return expand(shared[value["$v5_ref"]])
            return {key: expand(child) for key, child in value.items()}
        if isinstance(value, list):
            return [expand(child) for child in value]
        return value

    return expand({key: value for key, value in packet.items() if key != "shared_evidence"})
