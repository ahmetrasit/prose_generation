"""Inline target evidence and reversible deduplication for V5 prompts."""

from __future__ import annotations

import gzip
import json
import sqlite3
import zlib
from collections import Counter
from pathlib import Path
from typing import Any

from _commentary.v5.composition import normalize_arabic_surface


MORPHEME_COLUMNS = (
    "qac_ref", "surface_ar", "lemma_ar", "root_ar", "pos",
    "morpheme_role", "morph_features",
)


def _morphology(path: Path, refs: set[str]) -> tuple[dict[str, list[list[Any]]], str | None]:
    """Read the existing corpus directly; target bundles need not be built."""
    if not refs:
        return {}, None
    if not path.is_file():
        return {}, f"QAC morphology source is unavailable: {path}"
    try:
        raw = gzip.decompress(path.read_bytes())
        connection = sqlite3.connect(":memory:")
        try:
            connection.deserialize(raw)
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
            return result, None
        finally:
            connection.close()
    except (OSError, EOFError, sqlite3.Error, ValueError, zlib.error) as exc:
        # Missing morphology limits claims; it does not erase the Arabic or
        # turn the absence of evidence into a semantic rejection.
        return {}, f"QAC morphology could not be projected: {exc}"


def attach_context_evidence(
    packets: dict[str, dict[str, Any]],
    quran_evidence: dict[str, dict[str, Any]],
    morphology_path: Path,
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
    morphology, error = _morphology(morphology_path, set(aliases.values()))
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
            "morphology_source": str(morphology_path),
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


def compact_packet(packet: dict[str, Any]) -> dict[str, Any]:
    """Intern exact repeated values, without summarizing or deleting evidence."""
    if "shared_evidence" in packet:
        raise ValueError("Source packet uses the reserved shared_evidence transport field")
    counts: Counter[str] = Counter()

    def key(value: Any) -> str:
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

    def count(value: Any) -> None:
        if isinstance(value, (dict, list, str)):
            serialized = key(value)
            if len(serialized) >= 80:
                counts[serialized] += 1
        if isinstance(value, dict):
            if set(value) == {"$v5_ref"}:
                raise ValueError("Source evidence uses the reserved $v5_ref transport key")
            for child in value.values():
                count(child)
        elif isinstance(value, list):
            for child in value:
                count(child)

    count(packet)
    refs: dict[str, int] = {}
    shared: dict[int, Any] = {}

    def replace(value: Any) -> Any:
        serialized = key(value) if isinstance(value, (dict, list, str)) else None
        if serialized is not None and counts[serialized] > 1:
            if serialized not in refs:
                ref = len(refs) + 1
                refs[serialized] = ref
                shared[ref] = children(value)
            return {"$v5_ref": refs[serialized]}
        return children(value)

    def children(value: Any) -> Any:
        if isinstance(value, dict):
            return {key: replace(child) for key, child in value.items()}
        if isinstance(value, list):
            return [replace(child) for child in value]
        return value

    result = replace(packet)
    # A repeated parent can make its children occur only once after factoring.
    # Inline those children instead of creating needless indirection/storage.
    while True:
        uses: Counter[int] = Counter()

        def count_refs(value: Any) -> None:
            if isinstance(value, dict):
                if set(value) == {"$v5_ref"}:
                    uses[value["$v5_ref"]] += 1
                else:
                    for child in value.values():
                        count_refs(child)
            elif isinstance(value, list):
                for child in value:
                    count_refs(child)

        count_refs(result)
        for value in shared.values():
            count_refs(value)
        singles = {ref for ref in shared if uses[ref] < 2}
        if not singles:
            break

        def inline(value: Any) -> Any:
            if isinstance(value, dict):
                if set(value) == {"$v5_ref"} and value["$v5_ref"] in singles:
                    return inline(shared[value["$v5_ref"]])
                return {k: inline(v) for k, v in value.items()}
            if isinstance(value, list):
                return [inline(v) for v in value]
            return value

        result = inline(result)
        shared = {ref: inline(value) for ref, value in shared.items() if ref not in singles}
    result["shared_evidence"] = [
        {"ref": ref, "value": value} for ref, value in sorted(shared.items())
    ]
    return result


def expand_packet(packet: dict[str, Any]) -> dict[str, Any]:
    """Decode the inline transport for review and losslessness checks."""
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
