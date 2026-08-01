#!/usr/bin/env python3
"""Build QAC↔word-analysis mapping artifacts for one or more surahs.

The script is intentionally strict:
- resolves word-analysis critical words to deterministic morpheme spans,
- preserves QAC identifiers (no renumbering),
- verifies full source coverage before writing crosswalk files,
- always emits per-surah reports for troubleshooting.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import shutil
import sqlite3
import subprocess
import tempfile
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROSE_GEN_ROOT = ROOT.parent
QURAN_DATA_ROOT = PROSE_GEN_ROOT.parent / "quran-data"
QURAN_DATA = QURAN_DATA_ROOT / "data"

QURAN_DATA_RELEASE = QURAN_DATA_ROOT / "RELEASE.json"
QAC_SQLITE_GZ = QURAN_DATA / "morphology" / "qac.sqlite.gz"
WORD_ANALYSIS_DIR = QURAN_DATA / "analysis" / "word-analysis"
V12_TR_DIR = QURAN_DATA / "analysis" / "ayah-activation" / "v12-tr"
QURAN_APPS_CROSSWALKS = PROSE_GEN_ROOT.parent / "quran-apps" / "packages" / "content-compiler" / "crosswalks"
CROSSWALK_FILENAME_TMPL = "s{surah:03d}-qac-to-analysis.json"

ZSTD_CANDIDATES = ["/opt/homebrew/bin/zstd", "zstd"]
OUTPUT_SCHEMA = "qac-analysis-crosswalk-v2"
REPORT_SCHEMA = "qac-masaq-surah-report-v1"

_MORPHEME_ID_RE = re.compile(r"^m-w-s(\d+)-a(\d+)-w(\d+)-(\d+)$")
_WORD_ID_RE = re.compile(r"^w-s(\d+)-a(\d+)-w(\d+)$")
_WA_ARABIC_RE = re.compile(r"\{\{ar:([^}]*)\}\}")
_MAX_SKIP_FOR_MORPHEME_MATCH = 3
_ANNOTATION_CODEPOINTS = set(range(0x06D6, 0x06EE)) | {
    0x06E5,
    0x06E6,
    0x0640,
}
_ALEF_VARIANTS = str.maketrans({
    "ٱ": "ا",
    "أ": "ا",
    "إ": "ا",
    "آ": "ا",
    "ى": "ي",
    "ؤ": "و",
    "ئ": "ي",
})


def _zstd_binary() -> str:
    for candidate in ZSTD_CANDIDATES:
        path = shutil.which(candidate) or (Path(candidate) if Path(candidate).exists() else None)
        if path:
            return str(path)
    raise RuntimeError(
        "No zstd binary found. Install zstd or set an alternative binary in the PATH."
    )


def _read_zstd(path: Path) -> bytes:
    try:
        result = subprocess.run([_zstd_binary(), "-dc", str(path)], check=True, stdout=subprocess.PIPE)
    except FileNotFoundError as exc:
        raise RuntimeError(f"Could not run zstd for {path}") from exc
    return result.stdout


def _read_gz(path: Path) -> bytes:
    with gzip.open(path, "rb") as fh:
        return fh.read()


def _sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_arabic_surface(text: str) -> str:
    """Normalize Arabic text for deterministic comparisons."""
    if not text:
        return ""
    decomposed = unicodedata.normalize("NFKD", text)
    out: list[str] = []
    prev_base = ""
    for c in decomposed:
        if unicodedata.category(c) in {"Mn", "Me", "Cf"}:
            if c == "\u0670":
                if prev_base != "ى":
                    out.append("ا")
            continue
        if c == "ـ":
            continue
        if ord(c) in _ANNOTATION_CODEPOINTS:
            continue
        out.append(c)
        prev_base = c

    return "".join(out).translate(_ALEF_VARIANTS)


def _analysis_surface_variants(text: str) -> list[str]:
    """Build conservative surface variants used for safe fallback matching."""
    if not text:
        return []

    base = normalize_arabic_surface(text)
    normalized = unicodedata.normalize("NFKD", text)
    without_dagger = "".join(
        c for c in normalized
        if unicodedata.category(c) not in {"Mn", "Me", "Cf"}
        and c != "ـ"
        and ord(c) not in _ANNOTATION_CODEPOINTS
    ).translate(_ALEF_VARIANTS).replace(" ", "")
    variants = {base, without_dagger, base.replace("ء", "ا"), without_dagger.replace("ء", "ا")}
    if base.endswith("يا"):
        variants.add(base[:-1])
    if without_dagger.endswith("يا"):
        variants.add(without_dagger[:-1])
    variants.update(re.sub("ا+", "ا", v) for v in set(variants))
    return list(dict.fromkeys(v for v in variants if v))


def _normalize_for_boundary_rule(text: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    )


def normalize_boundary_letters(text: str) -> str:
    return _normalize_for_boundary_rule(text)


def _load_seed_crosswalk(surah: int, quran_release: str) -> tuple[Path | None, dict | None]:
    path = QURAN_APPS_CROSSWALKS / CROSSWALK_FILENAME_TMPL.format(surah=surah)
    if not path.exists():
        return None, None
    with open(path, encoding="utf-8") as fh:
        payload = json.load(fh)
    if payload.get("quranDataReleaseId") and payload.get("quranDataReleaseId") != quran_release:
        return path, None
    return path, payload


def load_release_id() -> str:
    with open(QURAN_DATA_RELEASE, encoding="utf-8") as fh:
        payload = json.load(fh)
    return payload["release_id"]


def available_surahs() -> list[int]:
    surahs = []
    for path in sorted(WORD_ANALYSIS_DIR.glob("s*.jsonl.zst")):
        stem = path.name.removesuffix(".jsonl.zst")
        if stem.startswith("s") and len(stem) == 4 and stem[1:].isdigit():
            try:
                surahs.append(int(stem[1:]))
            except ValueError:
                pass
    return surahs


def load_qac_morphemes(surah: int) -> tuple[dict[int, list[dict]], list[str], dict[str, str]]:
    raw = _read_gz(QAC_SQLITE_GZ)
    with tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False) as tmp:
        tmp.write(raw)
        tmp_path = tmp.name

    rows_by_ayah: dict[int, list[dict]] = {}
    qac_word_refs: list[str] = []
    translit_by_ref: dict[str, str] = {}
    seen = set()

    try:
        conn = sqlite3.connect(tmp_path)
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT qac_ref, qac_word_ref, surah, ayah, word_index, morpheme_index,
                   surface_bw, surface_ar
              FROM qac_morphemes
             WHERE surah = ?
          ORDER BY ayah, word_index, morpheme_index
            """,
            (surah,),
        ).fetchall()
    finally:
        Path(tmp_path).unlink(missing_ok=True)

    try:
        for row in rows:
            d = dict(row)
            ayah = int(d["ayah"])
            rows_by_ayah.setdefault(ayah, []).append(d)
            word_ref = d["qac_word_ref"]
            if word_ref not in seen:
                qac_word_refs.append(word_ref)
                seen.add(word_ref)
            translit_by_ref[d["qac_ref"]] = (d["surface_bw"] or d["surface_ar"] or "").strip()
    finally:
        conn.close()

    return rows_by_ayah, qac_word_refs, translit_by_ref


def load_morphemes_tsv(surah: int) -> tuple[dict[int, list[dict]], dict]:
    """Load per-ayah morphemes from v12-tr/morphemes.tsv.

    Uses qac_ref-derived ayah attribution to preserve the intended verse split
    for non-Fātiha files where morpheme_id-a000 rows point to Surah 1.
    """
    path = V12_TR_DIR / f"s{surah:03d}" / "linguistic" / "morphemes.tsv"
    coverage = {"present": False, "path": str(path)}
    by_ayah: dict[int, list[dict]] = {}
    malformed = 0
    dropped_marker_rows = 0

    if not path.exists():
        coverage["note"] = f"missing {path}"
        return by_ayah, coverage

    with open(path, encoding="utf-8") as fh:
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if not parts or parts[0] == "morpheme_id" or len(parts) < 5:
                continue
            if not _MORPHEME_ID_RE.match(parts[0]):
                malformed += 1
                continue
            m = _MORPHEME_ID_RE.match(parts[0])
            if not m:
                malformed += 1
                continue
            qac_ref = parts[2]
            qac_ref_parts = qac_ref.split(":") if qac_ref else []
            if len(qac_ref_parts) < 2:
                malformed += 1
                continue
            try:
                qac_surah = int(qac_ref_parts[0])
                ayah = int(qac_ref_parts[1])
            except ValueError:
                malformed += 1
                continue
            if qac_surah != surah:
                continue
            if qac_surah == 1 and ayah == 0:
                # standalone basmala marker rows should remain unmapped for non-Fātiha surahs.
                dropped_marker_rows += 1
                continue
            by_ayah.setdefault(ayah, []).append({
                "morpheme_id": parts[0],
                "word_id": parts[1],
                "qac_ref": parts[2],
                "morpheme_index": parts[3],
                "surface_ar": parts[4],
            })

    def sort_key(row: dict[str, str]) -> tuple[int, int]:
        m = _WORD_ID_RE.match(row["word_id"])
        word_index = int(m.group(3)) if m else 0
        morpheme_index = int(row["morpheme_index"]) if row["morpheme_index"].isdigit() else 0
        return word_index, morpheme_index

    for rows in by_ayah.values():
        rows.sort(key=sort_key)

    coverage.update(
        {
            "present": True,
            "ayah_count": len(by_ayah),
            "row_count": sum(len(v) for v in by_ayah.values()),
            "malformed_rows": malformed,
            "word_count": len(by_ayah),
        }
    )
    coverage["dropped_preface_rows"] = dropped_marker_rows
    if dropped_marker_rows:
        coverage["dropped_preface_rows"] = dropped_marker_rows
        coverage["note"] = (
            (coverage.get("note", "") + " | " if coverage.get("note") else "")
            + f"dropped_preface_rows={dropped_marker_rows}"
        )
    if malformed:
        coverage["note"] = (
            (coverage.get("note", "") + " | " if coverage.get("note") else "")
            + f"{malformed} malformed morpheme_id rows"
        )
    return by_ayah, coverage


def load_word_analysis(surah: int) -> dict[str, dict]:
    path = WORD_ANALYSIS_DIR / f"s{surah:03d}.jsonl.zst"
    raw = _read_zstd(path)
    out = {}
    for line in raw.decode("utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rec = json.loads(line)
        out[rec["ref"]] = rec
    return out


def _find_word_span_from_position(
    morpheme_rows: list[dict],
    position: int,
    target_variants: list[str],
    max_skip: int = _MAX_SKIP_FOR_MORPHEME_MATCH,
) -> tuple[bool, int, int, int]:
    """Find a morpheme span that matches the target surface.

    Returns (matched, span_start, span_end, skipped_rows).
    """
    normalized_targets = [normalize_arabic_surface(v) for v in target_variants]
    for skip in range(max_skip + 1):
        span_start = position + skip
        if span_start >= len(morpheme_rows):
            return False, position, position, 0
        accumulated = ""
        for j in range(span_start + 1, len(morpheme_rows) + 1):
            accumulated = "".join(
                normalize_arabic_surface(row["surface_ar"]) for row in morpheme_rows[span_start:j]
            )
            if accumulated in normalized_targets:
                return True, span_start, j, skip
            if not any(v.startswith(accumulated) for v in normalized_targets):
                break
    return False, position, position, 0


def resolve_word_morpheme_spans(
    wa_record: dict,
    morpheme_rows: list[dict],
) -> tuple[list[dict | None], list[dict]]:
    """Resolve each critical word to a morpheme span in ayah order."""
    spans: list[dict | None] = []
    unresolved: list[dict] = []
    position = 0

    words = wa_record.get("words", []) or []
    for index, word in enumerate(words):
        critical_w = word.get("critical_w", index + 1)
        display = word.get("surface_display") or ""
        m = _WA_ARABIC_RE.search(display)
        target = m.group(1) if m else ""
        target_variants = _analysis_surface_variants(target)
        if not target:
            spans.append(None)
            unresolved.append(
                {
                    "word_index": index,
                    "critical_w": critical_w,
                    "reason": "word_analysis missing parsable {{ar:...}} surface",
                    "surface_display": display,
                }
            )
            continue

        matched, span_start, j, skipped = _find_word_span_from_position(
            morpheme_rows=morpheme_rows,
            position=position,
            target_variants=target_variants,
        )
        if not matched:
            spans.append(None)
            unresolved.append(
                {
                    "word_index": index,
                    "critical_w": critical_w,
                    "reason": (
                        "surface mismatch: this critical word does not equal the next morpheme run"
                        " from current position"
                        if morpheme_rows
                        else "no morpheme rows for this ayah"
                    ),
                    "surface_display": display,
                    "analysis_surface": m.group(1) if m else "",
                    "analysis_surface_candidates": target_variants,
                }
            )
            continue

        selected = morpheme_rows[span_start:j]
        position = j

        qac_word_refs = []
        seen = set()
        for row in selected:
            word_ref = ":".join(row["qac_ref"].split(":")[:3])
            if word_ref not in seen:
                qac_word_refs.append(word_ref)
                seen.add(word_ref)

        spans.append(
            {
                "word_index": index,
                "critical_w": critical_w,
                "surface_display": display,
                "analysis_surface": m.group(1) if m else "",
                "morpheme_refs": [row["qac_ref"] for row in selected],
                "qac_word_refs": qac_word_refs,
                "morpheme_skip_count": skipped,
            }
        )
    return spans, unresolved


def infer_boundary_rule(qac_word_surface: str, analysis_surface: str) -> str | None:
    a = normalize_boundary_letters(analysis_surface)
    q = normalize_boundary_letters(qac_word_surface)
    if a == q:
        return None
    if a.replace("لٱلل", "لل", 1) == q:
        return "li-allah-contraction"
    return None


def analyze_surah(surah: int, out_dir: Path, qac_cache: dict[int, tuple]) -> dict:
    quran_release = load_release_id()

    if surah in qac_cache:
        qac_by_ayah, qac_word_refs, translit_by_qac_ref = qac_cache[surah]
    else:
        qac_by_ayah, qac_word_refs, translit_by_qac_ref = load_qac_morphemes(surah)
        qac_cache[surah] = (qac_by_ayah, qac_word_refs, translit_by_qac_ref)

    word_records = load_word_analysis(surah)
    morphemes_by_ayah, morpheme_tsv_coverage = load_morphemes_tsv(surah)
    morpheme_tsv_path = Path(V12_TR_DIR / f"s{surah:03d}" / "linguistic" / "morphemes.tsv")
    seed_crosswalk_path, seed_crosswalk = _load_seed_crosswalk(surah, quran_release)

    qac_by_ref = {}
    expected_qac_morphemes: list[str] = []
    for _, rows in sorted(qac_by_ayah.items(), key=lambda kv: kv[0]):
        for row in rows:
            expected_qac_morphemes.append(row["qac_ref"])
            qac_by_ref[row["qac_ref"]] = row

    qac_ayahs = sorted(qac_by_ayah.keys())
    wa_ayahs = morpheme_tsv_coverage["ayah_count"] and sorted(morphemes_by_ayah.keys()) or []
    available_ayahs = sorted(set(qac_ayahs) | set(wa_ayahs) | {int(ref.split(":")[1]) for ref in word_records})

    # One-to-one check for aligned_qac_word_ref in incoming word-analysis data.
    qac_word_set = set(qac_word_refs)
    dangling_aligned: list[str] = []
    for rec in word_records.values():
        for word in rec.get("words", []) or []:
            ref = word.get("aligned_qac_word_ref")
            if ref and ref not in qac_word_set:
                dangling_aligned.append(f"{rec['ref']}:{word.get('critical_w')}->{ref}")

    mapping_by_word: dict[str, list[dict]] = {qwr: [] for qwr in qac_word_refs}
    unresolved_by_surah: list[dict] = []
    span_skip_quality: list[dict] = []
    boundary_rules: dict[str, str] = {}
    seed_crosswalk_note = {
        "path": str(seed_crosswalk_path) if seed_crosswalk_path else None,
        "release": quran_release,
        "seedEntries": 0,
        "applied": False,
        "entriesApplied": 0,
    }
    if seed_crosswalk_path and not seed_crosswalk:
        seed_crosswalk_note["skippedReason"] = "release mismatch between quran-data and seed crosswalk"

    mapped_from_seed_analysis: set[str] = set()
    mapped_analysis_refs = set()
    mapped_morpheme_refs = set()

    if seed_crosswalk:
        seed_crosswalk_note["sourceRelease"] = seed_crosswalk.get("quranDataReleaseId", "")
        seed_issues_before = len(unresolved_by_surah)
        for entry in seed_crosswalk.get("mappings", []) or []:
            seed_crosswalk_note["seedEntries"] += 1
            qac_word_ref = entry.get("qacWordRef")
            if not qac_word_ref:
                unresolved_by_surah.append({"reason": "seed crosswalk entry missing qacWordRef"})
                continue
            if qac_word_ref not in mapping_by_word:
                unresolved_by_surah.append(
                    {
                        "reason": "seed crosswalk qacWordRef not found in QAC source",
                        "seed_qacWordRef": qac_word_ref,
                    }
                )
                continue

            valid = True
            for am in entry.get("analysisMappings", []) or []:
                analysis_ref = am.get("analysisRef")
                if not analysis_ref:
                    unresolved_by_surah.append(
                        {
                            "reason": "seed crosswalk analysis mapping missing analysisRef",
                            "seed_qacWordRef": qac_word_ref,
                        }
                    )
                    valid = False
                    continue
                analysis_parts = analysis_ref.split(":")
                if len(analysis_parts) != 3:
                    unresolved_by_surah.append(
                        {
                            "reason": "seed crosswalk analysisRef has invalid format",
                            "seed_qacWordRef": qac_word_ref,
                            "analysisRef": analysis_ref,
                        }
                    )
                    valid = False
                    continue
                ayah_ref = ":".join(analysis_parts[:2])
                if ayah_ref not in word_records:
                    unresolved_by_surah.append(
                        {
                            "reason": "seed crosswalk analysisRef missing from word-analysis",
                            "seed_qacWordRef": qac_word_ref,
                            "analysisRef": analysis_ref,
                        }
                    )
                    valid = False
                    continue
                try:
                    analysis_critical_w = int(analysis_parts[2])
                except ValueError:
                    unresolved_by_surah.append(
                        {
                            "reason": "seed crosswalk analysisRef has non-integer critical_w",
                            "seed_qacWordRef": qac_word_ref,
                            "analysisRef": analysis_ref,
                        }
                    )
                    valid = False
                    continue
                if not any(
                    (w.get("critical_w") == analysis_critical_w) for w in (word_records[ayah_ref].get("words") or [])
                ):
                    unresolved_by_surah.append(
                        {
                            "reason": "seed crosswalk analysisRef critical_w not found in word-analysis words",
                            "seed_qacWordRef": qac_word_ref,
                            "analysisRef": analysis_ref,
                        }
                    )
                    valid = False
                    continue
                qac_morphemes = []
                for mm in am.get("qacMorphemes", []) or []:
                    mref = mm.get("qacMorphemeRef")
                    if not mref:
                        unresolved_by_surah.append(
                            {
                                "reason": "seed crosswalk morpheme missing qacMorphemeRef",
                                "seed_qacWordRef": qac_word_ref,
                                "analysisRef": analysis_ref,
                            }
                        )
                        valid = False
                        continue
                    m = qac_by_ref.get(mref)
                    if not m:
                        unresolved_by_surah.append(
                            {
                                "reason": "seed crosswalk references missing QAC morpheme",
                                "seed_qacWordRef": qac_word_ref,
                                "analysisRef": analysis_ref,
                                "qacMorphemeRef": mref,
                            }
                        )
                        valid = False
                        continue
                    morpheme_word_ref = ":".join(m["qac_ref"].split(":")[:3])
                    if morpheme_word_ref != qac_word_ref:
                        unresolved_by_surah.append(
                            {
                                "reason": "seed crosswalk morpheme mapped to different QAC word",
                                "seed_qacWordRef": qac_word_ref,
                                "analysisRef": analysis_ref,
                                "qacMorphemeRef": mref,
                            }
                        )
                        valid = False
                        continue
                    if mref in mapped_morpheme_refs:
                        unresolved_by_surah.append(
                            {
                                "reason": "seed crosswalk reused an already mapped QAC morpheme",
                                "seed_qacWordRef": qac_word_ref,
                                "analysisRef": analysis_ref,
                                "qacMorphemeRef": mref,
                            }
                        )
                        valid = False
                        continue
                    mapped_morpheme_refs.add(mref)
                    qac_morphemes.append(
                        {
                            "qacMorphemeRef": mref,
                            "transliteration": (
                                mm.get("transliteration")
                                or translit_by_qac_ref.get(mref)
                                or m.get("surface_ar")
                                or ""
                            ),
                        }
                    )

                if not qac_morphemes or not valid:
                    continue
                mapping_by_word[qac_word_ref].append(
                    {
                        "analysisRef": analysis_ref,
                        "qacMorphemes": qac_morphemes,
                    }
                )
                mapped_from_seed_analysis.add(analysis_ref)
                mapped_analysis_refs.add(analysis_ref)
                seed_crosswalk_note["entriesApplied"] += 1

                if entry.get("arabicBoundaryRule"):
                    boundary_rules[qac_word_ref] = entry["arabicBoundaryRule"]

        seed_crosswalk_note["applied"] = (
            len(unresolved_by_surah) == seed_issues_before
            and seed_crosswalk_note["seedEntries"] > 0
        )

    # For deterministic checks, preserve first-seen ordering for mapped analysis refs.
    for ayah in sorted(word_records, key=lambda v: int(v.split(":")[1])):
        _, ayah_s = rec = ayah.split(":")
        ayah_num = int(ayah_s)
        record = word_records[ayah]
        morphemes = morphemes_by_ayah.get(ayah_num, [])
        if not morphemes:
            unresolved_by_surah.append({
                "ayah_ref": ayah,
                "surah": surah,
                "reason": "no morphemes.tsv rows for this ayah",
                "ayah": ayah_num,
            })
            continue

        spans, unresolved = resolve_word_morpheme_spans(record, morphemes)
        resolved_spans = [span for span in spans if span]
        skip_counts = [span.get("morpheme_skip_count", 0) for span in resolved_spans]
        if skip_counts:
            skip_histogram: dict[str, int] = {}
            for skip_count in skip_counts:
                k = str(skip_count)
                skip_histogram[k] = skip_histogram.get(k, 0) + 1
        else:
            skip_histogram = {}
        if skip_histogram.get("0", 0) != len(skip_counts):
            span_skip_quality.append({
                "ayah_ref": ayah,
                "surah": surah,
                "reason": "alignment used skip tolerance while resolving morpheme spans",
                "morpheme_skip_total": sum(skip_counts),
                "morpheme_skip_max": max(skip_counts),
                "morpheme_skip_histogram": skip_histogram,
            })
        for item in unresolved:
            item_analysis_ref = f"{surah}:{ayah_num}:{item.get('critical_w')}"
            if item_analysis_ref in mapped_from_seed_analysis:
                continue
            item.update({"ayah_ref": ayah, "surah": surah})
            unresolved_by_surah.append(item)

        for idx, word in enumerate(record.get("words", []) or []):
            span = spans[idx]
            if span is None:
                continue

            critical_w = span["critical_w"]
            analysis_ref = f"{surah}:{ayah_num}:{critical_w}"
            if analysis_ref in mapped_from_seed_analysis:
                continue
            qac_refs = span["qac_word_refs"]

            if len(qac_refs) != 1:
                unresolved_by_surah.append(
                    {
                        "ayah_ref": ayah,
                        "surah": surah,
                        "word_index": idx,
                        "critical_w": critical_w,
                        "reason": "analysis span crosses multiple QAC word refs",
                        "span_qac_word_refs": qac_refs,
                        "analysis_surface": span["analysis_surface"],
                    }
                )
                continue

            qac_word_ref = qac_refs[0]
            if qac_word_ref not in mapping_by_word:
                unresolved_by_surah.append(
                    {
                        "ayah_ref": ayah,
                        "surah": surah,
                        "word_index": idx,
                        "critical_w": critical_w,
                        "reason": "resolved to unknown QAC word ref",
                        "span_qac_word_ref": qac_word_ref,
                        "analysis_surface": span["analysis_surface"],
                    }
                )
                continue

            qac_morphemes: list[dict] = []
            duplicates = []
            analysis_surfaces = []
            for mref in span["morpheme_refs"]:
                m = qac_by_ref.get(mref)
                if not m:
                    unresolved_by_surah.append(
                        {
                            "ayah_ref": ayah,
                            "surah": surah,
                            "word_index": idx,
                            "critical_w": critical_w,
                            "reason": "resolved morpheme not found in QAC source table",
                            "missing_qac_ref": mref,
                        }
                    )
                    continue
                morpheme_word_ref = ":".join(m["qac_ref"].split(":")[:3])
                if morpheme_word_ref != qac_word_ref:
                    unresolved_by_surah.append(
                        {
                            "ayah_ref": ayah,
                            "surah": surah,
                            "word_index": idx,
                            "critical_w": critical_w,
                            "reason": "morpheme crosses a QAC word boundary",
                            "analysis_qac_word": qac_word_ref,
                            "morpheme_qac_ref": m["qac_ref"],
                        }
                    )
                    continue
                if mref in mapped_morpheme_refs:
                    duplicates.append(mref)
                    continue
                mapped_morpheme_refs.add(mref)
                qac_morphemes.append(
                    {
                        "qacMorphemeRef": mref,
                        "transliteration": translit_by_qac_ref.get(mref) or m["surface_ar"] or "",
                    }
                )
                analysis_surfaces.append(m["surface_ar"])

            if duplicates:
                unresolved_by_surah.append(
                    {
                        "ayah_ref": ayah,
                        "surah": surah,
                        "word_index": idx,
                        "critical_w": critical_w,
                        "reason": "duplicate morpheme already mapped",
                        "duplicate_qac_morpheme_refs": duplicates,
                        "analysis_surface": span["analysis_surface"],
                    }
                )
            if not qac_morphemes:
                continue

            mapped_analysis_refs.add(analysis_ref)
            mapping_by_word[qac_word_ref].append(
                {
                    "analysisRef": analysis_ref,
                    "qacMorphemes": qac_morphemes,
                }
            )

            inferred = infer_boundary_rule("".join(analysis_surfaces), span["analysis_surface"])
            if inferred:
                boundary_rules[qac_word_ref] = inferred

    mapped_word_refs = [q for q in qac_word_refs if mapping_by_word[q]]
    unmapped_qac_words = [q for q in qac_word_refs if q not in mapped_word_refs]

    expected_analysis_refs = []
    for ayah in sorted(word_records):
        for word in (word_records[ayah].get("words") or []):
            critical_w = word.get("critical_w")
            if critical_w is not None:
                expected_analysis_refs.append(f"{ayah}:{critical_w}")

    all_qac_morphemes = {
        morpheme["qacMorphemeRef"]
        for mappings in mapping_by_word.values()
        for m in mappings
        for morpheme in m.get("qacMorphemes", [])
    }
    coverage = {
        "surah": surah,
        "release": quran_release,
        "seedCrosswalk": seed_crosswalk_note,
        "wordAnalysisSource": str(WORD_ANALYSIS_DIR / f"s{surah:03d}.jsonl.zst"),
        "qacSource": str(QAC_SQLITE_GZ),
        "qacWordCount": len(qac_word_refs),
        "qacMorphemeCount": len(expected_qac_morphemes),
        "analysisTokenCount": len(expected_analysis_refs),
        "morphemeSkipTotal": 0,
        "morphemeSkipMax": 0,
        "morphemeSkipHistogram": {},
        "mappedQacWordCount": len(mapped_word_refs),
        "mappedMorphemeCount": len(all_qac_morphemes),
        "mappedAnalysisCount": len(mapped_analysis_refs),
        "unresolvedCount": len(unresolved_by_surah),
        "danglingAlignedQacRefs": sorted(set(dangling_aligned)),
        "unmappedQacWords": unmapped_qac_words,
        "unmappedAnalysisCount": len(set(expected_analysis_refs) - mapped_analysis_refs),
        "coverageByMorphemesTsv": morpheme_tsv_coverage,
        "inputSha256": {
            "qac.sqlite.gz": _sha256_hex(_read_gz(QAC_SQLITE_GZ)),
            f"word-analysis/s{surah:03d}.jsonl.zst": _sha256_hex(_read_zstd(WORD_ANALYSIS_DIR / f"s{surah:03d}.jsonl.zst")),
            f"v12-tr/s{surah:03d}/linguistic/morphemes.tsv": _sha256_hex(morpheme_tsv_path.read_bytes()) if morpheme_tsv_path.exists() else "",
        },
    }

    if span_skip_quality:
        skip_histogram: dict[str, int] = {}
        skip_total = 0
        skip_max = 0
        for item in span_skip_quality:
            histogram = item.get("morpheme_skip_histogram", {})
            skip_max = max(skip_max, item.get("morpheme_skip_max", 0))
            skip_total += item.get("morpheme_skip_total", 0)
            for key, value in histogram.items():
                skip_histogram[key] = skip_histogram.get(key, 0) + value
        coverage["morphemeSkipTotal"] = skip_total
        coverage["morphemeSkipMax"] = skip_max
        coverage["morphemeSkipHistogram"] = skip_histogram
        coverage["morphemeSkipWarnings"] = span_skip_quality
    else:
        coverage["morphemeSkipWarnings"] = []

    complete = (
        len(unmapped_qac_words) == 0
        and len(unresolved_by_surah) == 0
        and coverage["mappedAnalysisCount"] == coverage["analysisTokenCount"]
        and coverage["mappedMorphemeCount"] == coverage["qacMorphemeCount"]
        and set(expected_qac_morphemes) == set(all_qac_morphemes)
    )

    crosswalk = {
        "schemaVersion": OUTPUT_SCHEMA,
        "quranDataReleaseId": quran_release,
        "surah": surah,
        "qacWordCount": len(qac_word_refs),
        "qacMorphemeCount": len(expected_qac_morphemes),
        "analysisTokenCount": len(expected_analysis_refs),
        "mappings": [
            {
                "qacWordRef": qwr,
                **({"arabicBoundaryRule": boundary_rules[qwr]} if qwr in boundary_rules else {}),
                "analysisMappings": mapping_by_word[qwr],
            }
            for qwr in qac_word_refs
            if mapping_by_word[qwr]
        ],
    }

    report = {
        "schemaVersion": REPORT_SCHEMA,
        "status": "complete" if complete else "partial",
        "coverage": coverage,
        "qa": {
            "qacAyahCount": len(qac_by_ayah),
            "wordAnalysisAyahCount": len(word_records),
            "morphemeAyahCount": len(morphemes_by_ayah),
            "availableAyahs": available_ayahs,
        },
        "unresolved": unresolved_by_surah,
    }

    out_dir.mkdir(parents=True, exist_ok=True)
    report_path = out_dir / f"s{surah:03d}.qac-masaq-report.json"
    crosswalk_path = out_dir / f"s{surah:03d}-qac-to-analysis.json"
    with open(report_path, "w", encoding="utf-8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=2)

    status = {
        "surah": surah,
        "release": quran_release,
        "complete": complete,
        "report_path": str(report_path),
        "crosswalk_path": None,
        "mapped_qac_word_count": len(mapped_word_refs),
        "mapped_morpheme_count": len(all_qac_morphemes),
    }
    if complete:
        with open(crosswalk_path, "w", encoding="utf-8") as fh:
            json.dump(crosswalk, fh, ensure_ascii=False, indent=2)
        status["crosswalk_path"] = str(crosswalk_path)
        status["mappings"] = len(crosswalk["mappings"])
    return status


def main() -> int:
    parser = argparse.ArgumentParser(description="Build QAC-to-word-analysis mappings and reports")
    parser.add_argument("--surah", type=int, default=None, help="Generate only this surah")
    parser.add_argument("--all", action="store_true", help="Generate all surahs with available word-analysis")
    parser.add_argument("--out", type=Path, default=ROOT / "output", help="Output directory")
    args = parser.parse_args()

    if args.all:
        surahs = available_surahs()
    elif args.surah:
        surahs = [args.surah]
    else:
        parser.error("Either --surah or --all is required")

    qac_cache = {}
    results = []
    for s in surahs:
        results.append(analyze_surah(s, args.out, qac_cache))

    manifest = {
        "schemaVersion": "qac-masaq-manifest-v1",
        "quranDataReleaseId": load_release_id(),
        "runs": results,
    }
    manifest_path = args.out / "manifest.json"
    args.out.mkdir(parents=True, exist_ok=True)
    with open(manifest_path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)

    complete_count = sum(1 for r in results if r.get("complete"))
    print(f"processed {len(results)} surah(s); complete={complete_count}; manifest={manifest_path}")
    if complete_count != len(results):
        print("some surahs were partial; review per-surah .qac-masaq-report.json files")
        return 1
    print("all surahs completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
