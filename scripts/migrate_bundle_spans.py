#!/usr/bin/env python3
"""Audit or regenerate deterministic span joins in every saved input bundle.

Default: report stale mappings without writing. --apply updates mappings and
their coverage only, including surah summaries and existing package manifests.
Agent-authored evidence is preserved. Uncertain joins are reported, not forced.
"""

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile

import build_bundle as builder
import pericope_bundle_manifest as manifest_lib
from word_morpheme_alignment import ALIGNMENT_VERSION, coverage, resolve

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "_commentary" / "v3"))
from v3lib.prepare import _validated_qac_inventory, _word_analysis_qac_refs


def encode_like(value, original):
    multiline = original.lstrip().startswith('{\n')
    text = json.dumps(value, ensure_ascii=False, allow_nan=False,
                      indent=2 if multiline else None,
                      separators=None if multiline else (",", ":"))
    return text + ("\n" if original.endswith("\n") else "")


def write_checked(path, original, value):
    if path.is_symlink() or path.read_text(encoding="utf-8") != original:
        raise RuntimeError(f"Input changed during migration: {path}")
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(encode_like(value, original))
        os.chmod(name, path.stat().st_mode & 0o777)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def derive(bundle, morphology_cache):
    s, a = map(int, bundle["ayahRef"].split(":"))
    source_ref = bundle.get("linguistic_source_ref", bundle["ayahRef"])
    if a == 0:
        if source_ref != "1:1":
            raise ValueError("Prefatory input must explicitly use canonical 1:1")
        s, a = 1, 1
    if s not in morphology_cache:
        morphology_cache[s] = builder.load_morphemes_tsv(s)
    by_ayah, source_coverage, source_path = morphology_cache[s]
    if not source_path or not source_coverage.get("present"):
        raise RuntimeError(f"Required morpheme source missing for surah {s}")
    spans, gaps = resolve(bundle["word_analysis"], by_ayah.get(a, []))
    result = copy.deepcopy(bundle)
    result["word_morpheme_spans"] = spans
    result.setdefault("coverage", {})["word_morpheme_spans"] = coverage(
        spans, gaps, source_coverage, source_ref if bundle["ayah"] == 0 else None
    )
    qac = _validated_qac_inventory(result, ayah_ref=source_ref)
    _word_analysis_qac_refs(result, ayah_ref=source_ref,
                           words=bundle["word_analysis"]["words"], qac=qac)
    # Verify preservation separately from the write implementation.
    untouched = copy.deepcopy(result)
    if "word_morpheme_spans" in bundle:
        untouched["word_morpheme_spans"] = bundle["word_morpheme_spans"]
    else:
        untouched.pop("word_morpheme_spans", None)
    untouched["coverage"] = bundle.get("coverage", {})
    if untouched != bundle:
        raise AssertionError("Span migration changed source evidence")
    return result, gaps


def migrate(root, apply=False):
    paths = sorted(root.rglob("*.ayah.json"))
    if not paths:
        raise ValueError(f"No ayah bundles under {root}")
    code_records = {
        key: manifest_lib.file_record(ROOT / "scripts" / name, ROOT)
        for key, name in (
            ("builder", "build_pericope_bundles.py"),
            ("lower_level_builder", "build_bundle.py"),
            ("manifest_implementation", "pericope_bundle_manifest.py"),
            ("alignment_implementation", "word_morpheme_alignment.py"),
        )
    }
    manifests, stale_manifests = [], []
    for path in sorted(root.rglob("pericope.bundle-manifest.json")):
        original = path.read_text(encoding="utf-8")
        value = json.loads(original)
        if value.get("schema_version") != manifest_lib.SCHEMA_VERSION:
            raise RuntimeError(f"Unsupported package manifest: {path}")
        row = manifest_lib._manifest_row(value)
        if value.get("output_dir") != manifest_lib.stable_path(path.parent, ROOT):
            raise RuntimeError(f"Package output directory is stale: {path}")
        if value.get("generation_policy") not in (
            manifest_lib.generation_policy(), manifest_lib.legacy_v4_generation_policy()
        ):
            raise RuntimeError(f"Unknown package generation policy: {path}")
        manifest_lib._validate_build_command(value.get("command"), row=row,
            out_dir=path.parent, repo_root=ROOT,
            expected_lower_level_builder=ROOT / "scripts/build_bundle.py")
        if value.get("source") == "index":
            index = manifest_lib.verify_file_record(value.get("pericope_index"),
                label="pericope index", repo_root=ROOT)
            manifest_lib._verify_index_row(index, row)
        elif value.get("source") != "cli-span" or value.get("pericope_index") is not None:
            raise RuntimeError(f"Invalid package source: {path}")
        # A migration must not conceal already-modified package evidence.
        records = manifest_lib.generated_file_records(value, path.parent, ROOT)
        if records != value.get("ayah_bundle_files"):
            raise RuntimeError(f"Package evidence was already stale: {path}")
        manifests.append((path, original, value))
        if any(value.get(key) != record for key, record in code_records.items()):
            stale_manifests.append(str(path.relative_to(ROOT)))

    cache, summaries, stale, failures, gaps = {}, {}, [], [], []
    counts = {"files": len(paths), "words": 0, "resolved": 0}
    hashes = {}
    # Validate the complete proposed migration before writing its first file.
    for path in paths:
        try:
            original = path.read_text(encoding="utf-8")
            bundle = json.loads(original)
            updated, unresolved = derive(bundle, cache)
            hashes[path] = hashlib.sha256(original.encode("utf-8")).hexdigest()
            summaries.setdefault(path.parent, {})[bundle["ayahRef"]] = updated["coverage"]["word_morpheme_spans"]
            counts["words"] += len(updated["word_morpheme_spans"])
            counts["resolved"] += sum(span is not None for span in updated["word_morpheme_spans"])
            if updated != bundle:
                stale.append(str(path.relative_to(ROOT)))
            if unresolved:
                gaps.append({"path": str(path.relative_to(ROOT)), "words": unresolved})
        except Exception as exc:
            failures.append({"path": str(path), "error": str(exc)})
    aggregate_updates = []
    for path in sorted(root.rglob("*.surah.json")):
        original = path.read_text(encoding="utf-8")
        bundle = json.loads(original)
        updated = copy.deepcopy(bundle)
        for ref, item in updated.get("coverage", {}).get("per_ayah", {}).items():
            if ref not in summaries.get(path.parent, {}):
                failures.append({"path": str(path), "error": f"Summary has missing ayah {ref}"})
                continue
            item["word_morpheme_spans"] = summaries[path.parent][ref]
        if updated != bundle:
            aggregate_updates.append((path, original, updated))

    report = {"alignment_version": ALIGNMENT_VERSION, **counts,
              "stale_bundles": stale, "stale_surah_summaries": len(aggregate_updates),
              "stale_manifests": stale_manifests,
              "errors": failures, "unresolved": gaps, "applied": False}
    if not apply or failures:
        return report
    for path in paths:
        if str(path.relative_to(ROOT)) not in stale:
            continue
        original = path.read_text(encoding="utf-8")
        if hashlib.sha256(original.encode("utf-8")).hexdigest() != hashes[path]:
            raise RuntimeError(f"Input changed after preflight: {path}")
        updated, _ = derive(json.loads(original), cache)
        write_checked(path, original, updated)
    for path, original, updated in aggregate_updates:
        write_checked(path, original, updated)
    for path, original, previous in manifests:
        updated = copy.deepcopy(previous)
        records = manifest_lib.generated_file_records(previous, path.parent, ROOT)
        if (records == previous["ayah_bundle_files"]
                and str(path.relative_to(ROOT)) not in stale_manifests):
            continue
        updated["span_migration"] = {
            "alignment_version": ALIGNMENT_VERSION,
            "previous_manifest_sha256": hashlib.sha256(original.encode("utf-8")).hexdigest(),
            "previous_generation": {key: previous[key] for key in (
                "generated_at", "builder", "lower_level_builder", "manifest_implementation")},
            "tool": manifest_lib.file_record(Path(__file__), ROOT),
            "scope": "word_morpheme_spans and coverage only; source evidence preserved",
        }
        updated.update(code_records)
        updated["generation_policy"] = manifest_lib.generation_policy()
        updated["ayah_bundle_files"] = records
        write_checked(path, original, updated)
        manifest_lib.validate_manifest(path, repo_root=ROOT,
            expected_builder=ROOT / "scripts/build_pericope_bundles.py",
            expected_lower_level_builder=ROOT / "scripts/build_bundle.py")
    report["applied"] = True
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundles-dir", type=Path, default=ROOT / "bundles")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    result = migrate(args.bundles_dir.resolve(), args.apply)
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: len(value) if isinstance(value, list) else value
                      for key, value in result.items()}, ensure_ascii=False))
    return int(bool(result["errors"] or (not args.apply and (
        result["stale_bundles"] or result["stale_surah_summaries"] or result["stale_manifests"]))))


if __name__ == "__main__":
    raise SystemExit(main())
