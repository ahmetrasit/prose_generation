#!/usr/bin/env python3
"""Check an enriched Markdown file against its original commentary."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys


ENUMS = {
    "type": set("tafsir asbab hadith qiraat revelation_history historical_context semantic_history nazm cross_quran method_note reader_note novelty modern_scholarship source_note".split()),
    "tradition": set("rivayet dirayet nazm edebi hadith historical project none".split()),
    "role": set("anchor early_attestation clarification corroboration disagreement semantic_range historical_development historical_context asbab_context chronology nazm constraint contrast interpretive_consequence project_synthesis novelty_assessment methodological_note reader_orientation source_criticism rejected_candidate intertext".split()),
    "relation": set("direct_tafsir asbab direct_hadith_tafsir thematic lexical grammatical structural historical comparative methodological".split()),
    "status": set("explicit reported disputed inferred interpretive weak not_assessed".split()),
    "confidence": set("high medium low".split()),
    "historicity": set("established probable uncertain contested not_applicable".split()),
    "hadith_grade": set("sahih hasan daif mawdu not_assessed".split()),
    "connection": set("direct strong resonant speculative rejected not_applicable".split()),
    "classical_attestation": set("explicit partial building_blocks_only none_found_in_checked_sources not_checked not_applicable".split()),
    "priority": set("core extended research".split()),
    "audience": set("general advanced research".split()),
    "canonical": {"true", "false"},
}
REQUIRED = {"id", "type", "ayah", "role", "relation", "status", "prose", "source"}
KNOWN_FIELDS = set(ENUMS) | REQUIRED | {
    "checked_sources", "scholar", "transmitter", "term", "scope",
    "source_ref", "origin", "attested_in", "reason", "note",
}
KEY = re.compile(r"[a-z][a-z_]*")
ANNOTATION_KEY = re.compile(r"(?:^|[,{])\s*(?:id|type|role|relation|status|prose)\s*:")
AYAH = re.compile(r"(\d+):(\d+)(?:-(\d+))?")


def parse_block(line):
    """Parse the protocol's flat tag grammar without splitting quoted commas."""
    s = line.strip()
    if not (s.startswith("{") and s.endswith("}")):
        raise ValueError("annotation must occupy one physical line in outer braces")
    fields, quoted = {}, set()
    i = 1
    while i < len(s) - 1:
        while i < len(s) - 1 and s[i].isspace():
            i += 1
        match = KEY.match(s, i)
        if not match:
            raise ValueError("expected a lowercase field name")
        key = match.group()
        if key in fields:
            raise ValueError(f"duplicate field: {key}")
        i = match.end()
        while i < len(s) - 1 and s[i].isspace():
            i += 1
        if s[i] != ":":
            raise ValueError(f"missing colon after {key}")
        i += 1
        while i < len(s) - 1 and s[i].isspace():
            i += 1
        if s[i] == '"':
            start = i
            i += 1
            escaped = False
            while i < len(s):
                char = s[i]
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    break
                i += 1
            if i >= len(s):
                raise ValueError(f"unterminated quoted value: {key}")
            try:
                value = json.loads(s[start:i + 1])
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid quoted value for {key}: {exc.msg}") from exc
            quoted.add(key)
            i += 1
        else:
            start = i
            while i < len(s) - 1 and s[i] != ",":
                i += 1
            value = s[start:i].strip()
            if not re.fullmatch(r"[A-Za-z_]+", value):
                raise ValueError(f"{key}: punctuation, numbers, or human text need double quotes")
            if key not in ENUMS:
                raise ValueError(f"{key}: only machine enum values may be unquoted")
        if not value:
            raise ValueError(f"empty value: {key}")
        fields[key] = value
        while i < len(s) - 1 and s[i].isspace():
            i += 1
        if i == len(s) - 1:
            break
        if s[i] != ",":
            raise ValueError(f"expected comma after {key}")
        i += 1
        if not s[i:len(s) - 1].strip():
            raise ValueError("trailing comma")
    if "prose" in fields and "prose" not in quoted:
        raise ValueError("prose must be double-quoted")
    return fields


def validate(base_path, output_path, target):
    base_bytes = base_path.read_bytes()
    base = base_bytes.decode("utf-8")
    output = output_path.read_text(encoding="utf-8")
    errors, warnings = [], []
    chunks = [p for p in re.split(r"\n[ \t]*\n", base) if p.strip()]
    cursor, preserved = 0, 0
    for number, chunk in enumerate(chunks, 1):
        found = output.find(chunk, cursor)
        if found < 0:
            errors.append(f"base block {number} missing or changed: {chunk[:100]!r}")
        else:
            cursor = found + len(chunk)
            preserved += 1
    original_headings = [line for line in base.splitlines() if line.startswith("#")]
    heading_cursor = 0
    for heading in original_headings:
        found = output.find(heading, heading_cursor)
        if found < 0:
            errors.append(f"original heading missing or reordered: {heading}")
        else:
            heading_cursor = found + len(heading)
    original_tags = re.findall(r"\{[^{}]*\}", base)
    tag_cursor = 0
    preserved_tags = 0
    for tag in original_tags:
        found = output.find(tag, tag_cursor)
        if found < 0:
            errors.append(f"original tag missing or reordered: {tag[:100]}")
        else:
            tag_cursor = found + len(tag)
            preserved_tags += 1

    registry_ids = []
    registry_start = None
    for number, line in enumerate(output.splitlines(), 1):
        if re.match(r"^##\s+Kaynak kayıtları\s*$", line):
            registry_start = number
        if registry_start is not None:
            match = re.match(r"^\s*-\s+\*\*([^*]+)\*\*\s*[—–:-]", line)
            if match:
                registry_ids.append(match.group(1).strip())
    if registry_start is None:
        errors.append("missing source registry heading: ## Kaynak kayıtları")
    duplicate_registry = [key for key, count in Counter(registry_ids).items() if count > 1]
    if duplicate_registry:
        errors.append(f"duplicate registry IDs: {duplicate_registry}")
    registry = set(registry_ids)
    annotations, locations = [], []
    for number, line in enumerate(output.splitlines(), 1):
        if not ANNOTATION_KEY.search(line):
            continue
        if not line.lstrip().startswith("{"):
            errors.append(f"line {number}: annotation embedded in prose or split across lines")
            continue
        try:
            fields = parse_block(line)
        except (ValueError, IndexError) as exc:
            errors.append(f"line {number}: {exc}")
            continue
        annotations.append(fields)
        locations.append(number)
        missing = REQUIRED - fields.keys()
        if missing:
            errors.append(f"line {number}: missing required fields {sorted(missing)}")
        unknown = fields.keys() - KNOWN_FIELDS
        if unknown:
            warnings.append(f"line {number}: undocumented fields {sorted(unknown)}")
        for key, allowed in ENUMS.items():
            if key in fields and fields[key] not in allowed:
                errors.append(f"line {number}: invalid {key}={fields[key]!r}")
        for focus in fields.get("ayah", "").split("|"):
            match = AYAH.fullmatch(focus)
            if not match:
                errors.append(f"line {number}: invalid ayah scope {focus!r}")
                continue
            surah, first, last = (int(match.group(1)), int(match.group(2)), int(match.group(3) or match.group(2)))
            if surah != target or first < 1 or last < first or (target == 1 and last > 7):
                errors.append(f"line {number}: ayah scope outside target: {focus!r}")
        for source in fields.get("source", "").split("|"):
            if source and source not in registry:
                errors.append(f"line {number}: unresolved source ID {source!r}")
        if fields.get("type") == "novelty":
            for key in ("classical_attestation", "checked_sources"):
                if not fields.get(key):
                    errors.append(f"line {number}: novelty missing {key}")
        for key in ("tradition", "priority", "audience"):
            if key not in fields:
                warnings.append(f"line {number}: no {key} metadata")
        if fields.get("type") == "hadith" and "hadith_grade" not in fields:
            warnings.append(f"line {number}: hadith grade assessment not declared")
        if fields.get("type") == "asbab" and "historicity" not in fields:
            warnings.append(f"line {number}: asbab historicity not declared")
    if not annotations:
        errors.append("no comprehensive annotation blocks found")
    ids = [a["id"] for a in annotations if "id" in a]
    duplicates = [key for key, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"duplicate annotation IDs: {duplicates}")
    if registry_start is not None and any(line >= registry_start for line in locations):
        errors.append("annotations occur after the start of the source registry")
    if "Enrichment pending." in output:
        errors.append("output still contains the pending scaffold marker")
    if any(marker in output for marker in ("=== INSERT ===", "=== LEDGER ===", "\ufffd")):
        errors.append("output contains unfinished insertion/ledger markers or replacement characters")
    if re.search(r"turn\d+(?:search|view|fetch)\d+|cite", output):
        errors.append("output contains internal web citation identifiers")
    return {
        "target": target,
        "base_file": str(base_path),
        "output_file": str(output_path),
        "base_sha256": hashlib.sha256(base_bytes).hexdigest(),
        "output_sha256": hashlib.sha256(output.encode("utf-8")).hexdigest(),
        "base_blocks": len(chunks),
        "base_blocks_preserved_exactly_in_order": preserved,
        "base_prose_paragraphs": sum(not p.startswith("#") and not p.startswith("Kaynaklar:") for p in chunks),
        "original_headings": len(original_headings),
        "original_inline_tags": len(original_tags),
        "original_inline_tags_preserved_in_order": preserved_tags,
        "annotation_count": len(annotations),
        "annotations_by_type": dict(sorted(Counter(a.get("type", "?") for a in annotations).items())),
        "novelty_count": sum(a.get("type") == "novelty" for a in annotations),
        "source_count": len(registry),
        "errors": errors,
        "warnings": warnings,
        "structural_qc_passed": not errors,
        "scope_note": "Checks preservation and annotation structure. Source accuracy and research coverage require editorial review.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--target", type=int, required=True)
    parser.add_argument("--audit", type=Path)
    args = parser.parse_args()
    report = validate(args.base, args.output, args.target)
    if args.audit:
        args.audit.parent.mkdir(parents=True, exist_ok=True)
        args.audit.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["structural_qc_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
