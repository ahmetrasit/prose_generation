#!/usr/bin/env python3
"""
build_bundle.py — assemble the per-ayah / per-surah input bundle consumed by
`_ayah_commentary/PROMPT.md` and `_surah_commentary/PROMPT.md`.

See `/Volumes/OZTURK/_projects/prose_generation/COMMENTARY_SPEC.md` §9 for the
source inventory this script implements, and
`/Volumes/OZTURK/_projects/prose_generation/scripts/README.md` for usage.

Usage:
    python3 build_bundle.py --surah 103 [--ayah 1] [--out DIR]

Standard library only, with one exception: `.zst` files are decompressed by
shelling out to the `zstd` binary (the `zstandard` pip package is not assumed
to be installed). `.gz` files are decompressed with the stdlib `gzip` module.
"""

from __future__ import annotations

import argparse
import gzip
import json
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Repo layout
# ---------------------------------------------------------------------------

SCRIPT_PATH = Path(__file__).resolve()
PROSE_GEN_ROOT = SCRIPT_PATH.parent.parent          # .../prose_generation
SIBLING_ROOT = PROSE_GEN_ROOT.parent                # .../_projects

QURAN_DATA = SIBLING_ROOT / "quran-data" / "data"
LATENT_ACTIVATION = SIBLING_ROOT / "latent_activation"
QURAN_SLM = SIBLING_ROOT / "quran-slm"

QURAN_TEXT_TSV = QURAN_DATA / "text" / "quran-uthmani.tsv"
WORD_ANALYSIS_DIR = QURAN_DATA / "analysis" / "word-analysis"
QAC_SQLITE_GZ = QURAN_DATA / "morphology" / "qac.sqlite.gz"

V12_RUNS_DIR = LATENT_ACTIVATION / "v12" / "runs"
NETWORK_V3_REVIEWS_DIR = LATENT_ACTIVATION / "network" / "v3" / "reviews"
INTER_AYAH_DIR = QURAN_SLM / "inter-ayah" / "outputs"

ZSTD_CANDIDATES = ["/opt/homebrew/bin/zstd", "zstd"]

QUARANTINED_DIR_NAMES = {"pilot_invalid_prompt_leak"}
KNOWN_VARIANT_DIR_NAMES = {"left_first", "right_first"}

BUNDLE_SCHEMA_VERSION = "input-bundle-v1"
SURAH_BUNDLE_SCHEMA_VERSION = "input-bundle-surah-v1"


# ---------------------------------------------------------------------------
# Decompression helpers
# ---------------------------------------------------------------------------

def _zstd_binary() -> str:
    for candidate in ZSTD_CANDIDATES:
        path = shutil.which(candidate) or (candidate if Path(candidate).exists() else None)
        if path:
            return path
    raise RuntimeError(
        "No zstd binary found (tried: %s). Install zstd or the `zstandard` "
        "pip package." % ", ".join(ZSTD_CANDIDATES)
    )


def read_zst_bytes(path: Path) -> bytes:
    """Decompress a .zst file to bytes. Uses the `zstandard` package if
    importable, otherwise shells out to the `zstd` binary."""
    try:
        import zstandard  # type: ignore

        dctx = zstandard.ZstdDecompressor()
        with open(path, "rb") as fh:
            return dctx.stream_reader(fh).read()
    except ImportError:
        zstd_bin = _zstd_binary()
        result = subprocess.run(
            [zstd_bin, "-dc", str(path)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.stdout


def read_gz_bytes(path: Path) -> bytes:
    with gzip.open(path, "rb") as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# Fail-loud helper
# ---------------------------------------------------------------------------

class RequiredSourceMissing(RuntimeError):
    """Raised when a source the spec marks as structurally required is absent."""


def require_path(path: Path, description: str) -> Path:
    if not path.exists():
        raise RequiredSourceMissing(f"Required source missing: {description} -> {path}")
    return path


# ---------------------------------------------------------------------------
# Source: Quran text (pipe-delimited TSV)
# ---------------------------------------------------------------------------

def load_quran_text(surah: int) -> dict:
    """Returns {ayahRef: arabic_text} for every row of the given surah,
    including the S:0 prefatory basmalah row if present."""
    require_path(QURAN_TEXT_TSV, "Quran text TSV")
    out = {}
    prefix = f"{surah}:"
    with open(QURAN_TEXT_TSV, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            ref, _, text = line.partition("|")
            if ref.startswith(prefix):
                out[ref] = text
    if not out:
        raise RequiredSourceMissing(f"No Quran text rows found for surah {surah}")
    return out


# ---------------------------------------------------------------------------
# Source: word analysis (zstd JSONL, one record per ayah)
# ---------------------------------------------------------------------------

def load_word_analysis(surah: int) -> dict:
    """Returns {ayahRef: full_record_dict}."""
    path = WORD_ANALYSIS_DIR / f"s{surah:03d}.jsonl.zst"
    require_path(path, f"word-analysis file for surah {surah}")
    raw = read_zst_bytes(path)
    out = {}
    for line in raw.decode("utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        record = json.loads(line)
        out[record["ref"]] = record
    return out


# ---------------------------------------------------------------------------
# Source: QAC morphology (gzip'd sqlite, table qac_morphemes)
# ---------------------------------------------------------------------------

def load_qac_morphemes(surah: int) -> dict:
    """Returns {ayah_number(int): [row_dict, ...]} ordered by word_index,
    morpheme_index, for every row of the given surah."""
    require_path(QAC_SQLITE_GZ, "QAC sqlite")
    raw = read_gz_bytes(QAC_SQLITE_GZ)
    with tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False) as tmp:
        tmp.write(raw)
        tmp_path = tmp.name
    try:
        conn = sqlite3.connect(tmp_path)
        conn.row_factory = sqlite3.Row
        cur = conn.execute(
            "SELECT * FROM qac_morphemes WHERE surah = ? "
            "ORDER BY ayah, word_index, morpheme_index",
            (surah,),
        )
        rows_by_ayah: dict = {}
        for row in cur.fetchall():
            d = dict(row)
            rows_by_ayah.setdefault(d["ayah"], []).append(d)
        conn.close()
    finally:
        Path(tmp_path).unlink(missing_ok=True)
    if not rows_by_ayah:
        raise RequiredSourceMissing(f"No qac_morphemes rows found for surah {surah}")
    return rows_by_ayah


# ---------------------------------------------------------------------------
# Source: v12 input packets (branch_inventories) + reader responses
# ---------------------------------------------------------------------------

def _variant_dirs(focus_dir: Path) -> dict:
    """Returns {variant_name: dir_path}. If the focus dir has left_first/
    right_first subdirectories, those are the variants (labelled, kept
    separately). Otherwise the focus dir itself is the single 'default'
    variant. pilot_invalid_prompt_leak is always excluded."""
    if not focus_dir.exists():
        return {}
    subdirs = {d.name for d in focus_dir.iterdir() if d.is_dir()}
    subdirs -= QUARANTINED_DIR_NAMES
    variant_names = subdirs & KNOWN_VARIANT_DIR_NAMES
    if variant_names:
        return {name: focus_dir / name for name in sorted(variant_names)}
    return {"default": focus_dir}


def _load_branch_inventories_fallback(surah: int, ayah: int, focus_dir: Path) -> tuple:
    """Surah-scope fallback for branch inventories.

    `full_context_packet.json` exists for all 114 surahs and carries the same
    `branch_inventories` list. Its scope differs from a stage_00 focus packet:
    it covers every root in the surah, not only this ayah's roots, and it is
    not staged (no before/neighbour-revealed distinction). Both facts are
    recorded in coverage so the writer can state them."""
    packet_path = V12_RUNS_DIR / f"s{surah:03d}" / "full_context_packet.json"
    if not packet_path.exists():
        raise RequiredSourceMissing(
            f"branch_inventories unavailable for {surah}:{ayah}: no focus dir at "
            f"{focus_dir} and no {packet_path}"
        )
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    branch_inventories = packet.get("branch_inventories", [])
    if not branch_inventories:
        raise RequiredSourceMissing(
            f"branch_inventories empty for {surah}:{ayah} in {packet_path}"
        )
    variant = {
        "source_file": str(packet_path.relative_to(SIBLING_ROOT)),
        "branch_inventories": branch_inventories,
    }
    coverage = {
        "present": True,
        "scope": "surah",
        "variants": {
            "full_context_packet": {
                "present": True,
                "roots": [r.get("root") for r in branch_inventories],
                "branch_counts": {
                    r.get("root"): len(r.get("branches", [])) for r in branch_inventories
                },
                "missing_branch_inventories": packet.get("missing_branch_inventories", []),
                "note": (
                    "surah-scope fallback: no per-ayah focus run exists, so this "
                    "covers every root in the surah rather than only this ayah's "
                    "roots, and carries no staged reveal order"
                ),
            }
        },
    }
    return {"full_context_packet": variant}, coverage


def load_v12_branch_inventories(surah: int, ayah: int) -> tuple:
    """Returns (variants_dict, coverage_dict).

    variants_dict: {variant_name: {"stage_00_file": relpath, "roots": [...]}}
    roots come verbatim from branch_inventories in the stage_00_*.json packet
    (the packet is scoped to the focus ayah's own roots at stage 0, before any
    neighbour is revealed)."""
    focus_dir = V12_RUNS_DIR / f"s{surah:03d}" / f"focus_{surah}_{ayah}"
    variants = _variant_dirs(focus_dir)
    out = {}
    coverage = {"present": False, "variants": {}}
    if not variants:
        # Per-ayah focus runs exist for only a handful of ayahs corpus-wide
        # (a method-development pilot). The surah-scope full_context_packet.json
        # carries the same branch_inventories structure for all 114 surahs, so
        # fall back to it rather than emitting a bundle with no latent material.
        return _load_branch_inventories_fallback(surah, ayah, focus_dir)

    for variant_name, vdir in variants.items():
        stage_00_matches = sorted(vdir.glob("stage_00_*.json"))
        if not stage_00_matches:
            coverage["variants"][variant_name] = {
                "present": False,
                "note": "no stage_00_*.json packet found",
            }
            continue
        stage_00_path = stage_00_matches[0]
        packet = json.loads(stage_00_path.read_text(encoding="utf-8"))
        branch_inventories = packet.get("branch_inventories", [])
        out[variant_name] = {
            "stage_00_file": str(stage_00_path.relative_to(SIBLING_ROOT)),
            "branch_inventories": branch_inventories,
        }
        coverage["variants"][variant_name] = {
            "present": True,
            "roots": [r.get("root") for r in branch_inventories],
            "branch_counts": {
                r.get("root"): len(r.get("branches", [])) for r in branch_inventories
            },
        }
        coverage["present"] = True

    if not out:
        # Focus dir exists but no variant carries a stage_00 packet.
        return _load_branch_inventories_fallback(surah, ayah, focus_dir)
    return out, coverage


def load_v12_reader_responses(surah: int, ayah: int) -> tuple:
    """Returns (variants_dict, coverage_dict). Optional source: a missing
    response set is a machine-readable coverage fact, not an error.

    variants_dict: {variant_name: {reader_id: {"stage_00": {...}, ...}}}
    """
    focus_dir = V12_RUNS_DIR / f"s{surah:03d}" / f"focus_{surah}_{ayah}"
    variants = _variant_dirs(focus_dir)
    out = {}
    coverage = {"present": False, "variants": {}}

    for variant_name, vdir in variants.items():
        responses_dir = vdir / "responses"
        if not responses_dir.exists():
            coverage["variants"][variant_name] = {
                "present": False,
                "readers": [],
                "note": "no responses/ directory; packet exists but zero reader responses recorded",
            }
            continue
        reader_dirs = sorted(
            d for d in responses_dir.iterdir()
            if d.is_dir() and d.name not in QUARANTINED_DIR_NAMES
        )
        if not reader_dirs:
            coverage["variants"][variant_name] = {
                "present": False,
                "readers": [],
                "note": "responses/ directory exists but is empty",
            }
            continue
        variant_out = {}
        readers_meta = []
        for reader_dir in reader_dirs:
            stage_files = sorted(reader_dir.glob("stage_*.json"))
            stages = {}
            for sf in stage_files:
                stages[sf.stem] = json.loads(sf.read_text(encoding="utf-8"))
            variant_out[reader_dir.name] = stages
            readers_meta.append({"reader_id": reader_dir.name, "stages": sorted(stages.keys())})
        out[variant_name] = variant_out
        coverage["variants"][variant_name] = {"present": True, "readers": readers_meta}
        coverage["present"] = True

    return out, coverage


# ---------------------------------------------------------------------------
# Source: v12 reader ayah walks (markdown)
# ---------------------------------------------------------------------------

_H1_RE = re.compile(r"^#\s+(.*)$")
_H2_RE = re.compile(r"^##\s+(\d+:\d+)\s+—\s*(.*)$")
_H3_RE = re.compile(r"^###\s+(.*)$")


def parse_ayah_walk_markdown(text: str) -> dict:
    """Parses a reader_s{NNN}_{a,b}_ayah_walk.md file into
    {ayahRef: {"title": h1_context, "activated_readings_md": str|None,
               "retrospective_surprises_md": str|None,
               "turkish_prose_synthesis_md": str|None}}.

    The file structure (verified on S103) is: a run of `## {ref} — ...`
    blocks under the walk's own H1, each containing `### Activated readings`
    and `### Retrospective surprises`; then a second `# Turkish Prose
    Synthesis` H1 with its own flat `## {ref} — ...` blocks (no H3s)."""
    lines = text.splitlines()
    out: dict = {}
    current_h1 = None
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        m1 = _H1_RE.match(line)
        if m1:
            current_h1 = m1.group(1).strip()
            i += 1
            continue
        m2 = _H2_RE.match(line)
        if m2:
            ayah_ref = m2.group(1)
            block_start = i + 1
            j = block_start
            while j < n and not _H1_RE.match(lines[j]) and not _H2_RE.match(lines[j]):
                j += 1
            block_lines = lines[block_start:j]
            entry = out.setdefault(
                ayah_ref,
                {
                    "activated_readings_md": None,
                    "retrospective_surprises_md": None,
                    "turkish_prose_synthesis_md": None,
                },
            )
            is_turkish_synthesis = bool(current_h1) and "turkish prose synthesis" in current_h1.lower()
            if is_turkish_synthesis:
                entry["turkish_prose_synthesis_md"] = "\n".join(block_lines).strip()
            else:
                # split block by H3 subheadings
                sub_start = None
                sub_title = None
                for bi, bl in enumerate(block_lines):
                    m3 = _H3_RE.match(bl)
                    if m3:
                        if sub_title is not None:
                            content = "\n".join(block_lines[sub_start:bi]).strip()
                            _assign_walk_subsection(entry, sub_title, content)
                        sub_title = m3.group(1).strip()
                        sub_start = bi + 1
                if sub_title is not None:
                    content = "\n".join(block_lines[sub_start:]).strip()
                    _assign_walk_subsection(entry, sub_title, content)
            i = j
            continue
        i += 1
    return out


def _assign_walk_subsection(entry: dict, title: str, content: str) -> None:
    key = title.strip().lower()
    if key == "activated readings":
        entry["activated_readings_md"] = content
    elif key == "retrospective surprises":
        entry["retrospective_surprises_md"] = content
    else:
        entry.setdefault("other_sections", {})[title] = content


def load_v12_reader_walks(surah: int, ayah: int) -> tuple:
    """Returns (dict, coverage_dict) for every reader_s{NNN}_{a,b}_ayah_walk.md
    found for this surah, restricted to this ayah's block."""
    control_dir = V12_RUNS_DIR / f"s{surah:03d}" / "full_context_control"
    ayah_ref = f"{surah}:{ayah}"
    out = {}
    coverage = {"present": False, "readers": {}}
    if not control_dir.exists():
        coverage["note"] = f"full_context_control dir not found: {control_dir}"
        return out, coverage

    walk_files = sorted(control_dir.glob(f"reader_s{surah:03d}_*_ayah_walk.md"))
    for wf in walk_files:
        m = re.search(r"reader_s\d+_([a-z])_ayah_walk\.md$", wf.name)
        reader_label = f"reader_{m.group(1)}" if m else wf.stem
        parsed = parse_ayah_walk_markdown(wf.read_text(encoding="utf-8"))
        if ayah_ref in parsed:
            out[reader_label] = parsed[ayah_ref]
            out[reader_label]["source_file"] = str(wf.relative_to(SIBLING_ROOT))
            coverage["readers"][reader_label] = {"present": True, "source_file": out[reader_label]["source_file"]}
            coverage["present"] = True
        else:
            coverage["readers"][reader_label] = {
                "present": False,
                "note": f"{ayah_ref} heading not found in {wf.name}",
            }
    if not walk_files:
        coverage["note"] = f"no reader_s{surah:03d}_*_ayah_walk.md files found"
    return out, coverage


# ---------------------------------------------------------------------------
# Source: whole-surah reading (butuncul-okuma.md)
# ---------------------------------------------------------------------------

_BUTUNCUL_LINE_RE = re.compile(r"^\*\*(\d+:\d+)\.\*\*\s+(.*)$")
_BUTUNCUL_BRACE_RE = re.compile(r"\{([^{}]*)\}\s*$")


def load_butuncul_okuma(surah: int) -> tuple:
    """Returns (dict {ayahRef: parsed_line}, coverage_dict, file_path or None)."""
    control_dir = V12_RUNS_DIR / f"s{surah:03d}" / "full_context_control"
    # File names are inconsistently zero-padded upstream: S103 is
    # `103-0-3-...` but S1 is `1-0-7-...` and S87-S99 are unpadded too.
    # Globbing only the padded form silently dropped 15 of the 30 existing
    # whole-surah readings, including S1 and S96.
    patterns = {f"{surah:03d}-0-*-butuncul-okuma.md", f"{surah}-0-*-butuncul-okuma.md"}
    matches = sorted(
        {m for pattern in patterns for m in control_dir.glob(pattern)}
    ) if control_dir.exists() else []
    out = {}
    coverage = {"present": False}
    if not matches:
        coverage["note"] = f"no *-0-*-butuncul-okuma.md for surah {surah} under {control_dir}"
        return out, coverage, None

    path = matches[0]
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        line = line.strip()
        m = _BUTUNCUL_LINE_RE.match(line)
        if not m:
            continue
        ayah_ref, rest = m.group(1), m.group(2)
        arabic_text, _, remainder = rest.partition(" — ")
        root_citations = []
        brace_m = _BUTUNCUL_BRACE_RE.search(remainder)
        reading_text = remainder
        if brace_m:
            root_citations = [c.strip() for c in brace_m.group(1).split(";") if c.strip()]
            reading_text = remainder[: brace_m.start()].strip()
        reading_text = re.sub(r"^Birincil okuma:\s*", "", reading_text)
        out[ayah_ref] = {
            "raw_line": line,
            "arabic_text": arabic_text.strip(),
            "reading_text_tr": reading_text.strip(),
            "root_citations": root_citations,
        }
    coverage["present"] = bool(out)
    return out, coverage, path


# ---------------------------------------------------------------------------
# Source: network/v3 channel review (blind candidate review, first pass)
# ---------------------------------------------------------------------------

_PARENT_RE = re.compile(r"^###\s+(?:\d+\.\s*)?(.+?)\s*$")
_SUBCHANNEL_RE = re.compile(r"^####\s+(?:Subchannel\s+)?([A-Z0-9]+)\.\s*(.+?)\s*$")
_FIELD_RE = re.compile(r"^-\s*([A-Za-z][A-Za-z /]*?):\s*(.*)$")

_FIELD_KEYS = {
    "semantic invariant": "semantic_invariant",
    "surface relation": "surface_relation",
    "surprising reach": "surprising_reach",
    "reading type": "reading_type",
    "scene or process": "scene_or_process",
    "active motifs": "active_motifs",
    "ayah anchors": "ayah_anchors",
    "synthesis": "synthesis",
}


def _ayah_refs_in(text: str, surah: int) -> list:
    """Ayah refs of this surah mentioned in a block, in order, deduplicated."""
    seen = []
    for m in re.finditer(r"\b(\d+):(\d+)\b", text or ""):
        if int(m.group(1)) != surah:
            continue
        ref = f"{m.group(1)}:{m.group(2)}"
        if ref not in seen:
            seen.append(ref)
    return seen


def load_channel_review(surah: int) -> tuple:
    """Returns (review_dict, coverage_dict, path or None).

    Parses `network/v3/reviews/s{NNN}/reader_a_pilot.md` into parent channels
    and their subchannels. This is FIRST-PASS, SINGLE-READER review output, not
    an adjudicated channel ledger: there is no accept/reject, no per-ayah
    maturity, and no second reader. Coverage says so explicitly, because the
    disclosure rules in docs/CHANNELS.md depend on a maturity column this
    source does not have."""
    review_dir = NETWORK_V3_REVIEWS_DIR / f"s{surah:03d}"
    path = review_dir / "reader_a_pilot.md"
    coverage = {"present": False, "review_status": "first-pass-single-reader"}
    if not path.exists():
        coverage["note"] = (
            f"no channel review at {path}. network/v3 excludes three-ayah surahs "
            f"(S103, S108, S110) from candidate discovery."
        )
        return {}, coverage, None

    text = path.read_text(encoding="utf-8")
    parents, parent, sub = [], None, None

    def close_sub():
        nonlocal sub
        if sub is not None:
            sub["ayah_refs"] = _ayah_refs_in(
                " ".join([sub.get("ayah_anchors", ""), sub.get("active_motifs", "")]), surah
            )
            parent["subchannels"].append(sub)
            sub = None

    def close_parent():
        nonlocal parent
        close_sub()
        if parent is not None:
            parents.append(parent)
            parent = None

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#### "):
            m = _SUBCHANNEL_RE.match(stripped)
            if m and parent is not None:
                close_sub()
                sub = {"key": m.group(1), "name": m.group(2)}
                continue
        if stripped.startswith("### "):
            m = _PARENT_RE.match(stripped)
            if m:
                close_parent()
                parent = {"name": m.group(1), "subchannels": []}
                continue
        m = _FIELD_RE.match(stripped)
        if m and parent is not None:
            key = _FIELD_KEYS.get(m.group(1).strip().lower())
            if key:
                (sub if sub is not None else parent)[key] = m.group(2).strip()
    close_parent()

    for p in parents:
        refs = []
        for s in p["subchannels"]:
            refs.extend(s.get("ayah_refs", []))
        refs.extend(_ayah_refs_in(p.get("surface_relation", ""), surah))
        p["ayah_refs"] = sorted(set(refs), key=lambda r: int(r.split(":")[1]))

    coverage.update({
        "present": bool(parents),
        "parent_channel_count": len(parents),
        "subchannel_count": sum(len(p["subchannels"]) for p in parents),
        "note": (
            "first-pass blind review by a single reader; no adjudication, no "
            "accept/reject, no per-ayah channel maturity. Not a channel ledger."
        ),
    })
    return {"parent_channels": parents}, coverage, path


def channel_blocks_for_ayah(review: dict, ayah_ref: str) -> list:
    """Subchannels whose anchors include this ayah, each carrying its parent's
    invariant so the block is readable on its own."""
    out = []
    for p in review.get("parent_channels", []):
        for s in p.get("subchannels", []):
            if ayah_ref in s.get("ayah_refs", []):
                out.append({
                    "parent_channel": p.get("name"),
                    "parent_semantic_invariant": p.get("semantic_invariant"),
                    "parent_surprising_reach": p.get("surprising_reach"),
                    **s,
                })
    return out


# ---------------------------------------------------------------------------
# Source: inter-ayah rows (headerless 3-col TSV)
# ---------------------------------------------------------------------------

VALID_LABELS = {"strong", "medium", "weak", "no value"}


def load_inter_ayah_rows(surah: int, ayah: int) -> tuple:
    """Returns (rows_list, coverage_dict). Never filters by label."""
    path = INTER_AYAH_DIR / f"focus_{surah}_{ayah}_cutoff_100.tsv"
    coverage = {"present": False}
    if not path.exists():
        coverage["note"] = f"file not found: {path}"
        return [], coverage

    rows = []
    label_counts = {}
    with open(path, encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, start=1):
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t", 2)
            if len(parts) != 3:
                raise RuntimeError(
                    f"{path}:{lineno}: expected 3 tab-separated fields, got {len(parts)}"
                )
            label, ref, note = parts
            if label not in VALID_LABELS:
                raise RuntimeError(f"{path}:{lineno}: unrecognised label {label!r}")
            rows.append({"label": label, "ref": ref, "note": note})
            label_counts[label] = label_counts.get(label, 0) + 1

    coverage["present"] = True
    coverage["row_count"] = len(rows)
    coverage["label_counts"] = label_counts
    return rows, coverage


# ---------------------------------------------------------------------------
# Bundle assembly
# ---------------------------------------------------------------------------

def build_ayah_bundle(surah: int, ayah: int, quran_text: dict, word_analysis: dict,
                       qac_by_ayah: dict) -> dict:
    ayah_ref = f"{surah}:{ayah}"
    coverage = {}

    # --- required sources ---
    if ayah_ref not in quran_text:
        raise RequiredSourceMissing(f"Quran text missing for {ayah_ref}")
    coverage["quran_text"] = {"present": True}

    wa_record = word_analysis.get(ayah_ref)
    if wa_record is None:
        raise RequiredSourceMissing(f"word-analysis record missing for {ayah_ref}")
    coverage["word_analysis"] = {"present": True, "word_count": len(wa_record.get("words", []))}

    qac_rows = qac_by_ayah.get(ayah)
    if not qac_rows:
        raise RequiredSourceMissing(f"QAC morphemes missing for {ayah_ref}")
    coverage["qac_morphemes"] = {"present": True, "row_count": len(qac_rows)}

    branch_inventories, bi_coverage = load_v12_branch_inventories(surah, ayah)
    coverage["branch_inventories"] = bi_coverage

    # --- optional sources (degrade gracefully) ---
    reader_responses, rr_coverage = load_v12_reader_responses(surah, ayah)
    coverage["v12_reader_responses"] = rr_coverage

    reader_walks, walk_coverage = load_v12_reader_walks(surah, ayah)
    coverage["v12_reader_walks"] = walk_coverage

    butuncul_all, butuncul_cov, butuncul_path = load_butuncul_okuma(surah)
    butuncul_line = butuncul_all.get(ayah_ref)
    coverage["butuncul_okuma"] = {
        "present": butuncul_line is not None,
        "source_file": str(butuncul_path.relative_to(SIBLING_ROOT)) if butuncul_path else None,
        "note": None if butuncul_line is not None else "no line for this ayah found in whole-surah reading",
    }

    inter_ayah_rows, ia_coverage = load_inter_ayah_rows(surah, ayah)
    coverage["inter_ayah"] = ia_coverage

    channel_review, ch_coverage, ch_path = load_channel_review(surah)
    channel_blocks = channel_blocks_for_ayah(channel_review, ayah_ref)
    coverage["channel_review"] = {
        **ch_coverage,
        "source_file": str(ch_path.relative_to(SIBLING_ROOT)) if ch_path else None,
        "subchannels_anchored_here": len(channel_blocks),
    }

    bundle = {
        "bundle_type": "ayah",
        "schema_version": BUNDLE_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "surah": surah,
        "ayah": ayah,
        "ayahRef": ayah_ref,
        "text": {
            "arabic_uthmani": quran_text[ayah_ref],
            "source": "quran-data/data/text/quran-uthmani.tsv",
        },
        "qac_morphemes": qac_rows,
        "word_analysis": wa_record,
        "branch_inventories": branch_inventories,
        "v12_reader_responses": reader_responses,
        "v12_reader_walks": reader_walks,
        "butuncul_okuma_line": butuncul_line,
        "inter_ayah_rows": inter_ayah_rows,
        "channel_subchannels_anchored_here": channel_blocks,
        "coverage": coverage,
    }
    return bundle


def build_surah_bundle(surah: int, ayah_bundles: list, ayah_bundle_filenames: list) -> dict:
    quran_text = load_quran_text(surah)  # includes S:0 basmalah row if present
    butuncul_all, butuncul_cov, butuncul_path = load_butuncul_okuma(surah)
    channel_review, ch_coverage, ch_path = load_channel_review(surah)

    coverage = {
        "ayah_count": len(ayah_bundles),
        "per_ayah": {b["ayahRef"]: b["coverage"] for b in ayah_bundles},
        "butuncul_okuma": {
            "present": butuncul_cov.get("present", False),
            "source_file": str(butuncul_path.relative_to(SIBLING_ROOT)) if butuncul_path else None,
            "ayah_refs_found": sorted(butuncul_all.keys()),
        },
        "channel_review": {
            **ch_coverage,
            "source_file": str(ch_path.relative_to(SIBLING_ROOT)) if ch_path else None,
        },
    }

    surah_bundle = {
        "bundle_type": "surah",
        "schema_version": SURAH_BUNDLE_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "surah": surah,
        "ayah_refs": [b["ayahRef"] for b in ayah_bundles],
        "ayah_bundle_files": ayah_bundle_filenames,
        "surah_scope": {
            "quran_text_all_rows": [
                {"ayahRef": ref, "arabic_uthmani": text} for ref, text in sorted(
                    quran_text.items(),
                    key=lambda kv: (int(kv[0].split(":")[1]),),
                )
            ],
            "butuncul_okuma_all_lines": [
                dict(ayahRef=ref, **line) for ref, line in sorted(
                    butuncul_all.items(), key=lambda kv: (int(kv[0].split(":")[1]),)
                )
            ],
            "channel_review": channel_review,
        },
        "coverage": coverage,
    }
    return surah_bundle


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def discover_ayah_numbers(surah: int, quran_text: dict) -> list:
    nums = sorted(
        int(ref.split(":")[1])
        for ref in quran_text
        if int(ref.split(":")[1]) != 0
    )
    return nums


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--ayah", type=int, default=None)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    surah = args.surah
    out_dir = args.out or (PROSE_GEN_ROOT / "bundles" / f"s{surah:03d}")
    out_dir.mkdir(parents=True, exist_ok=True)

    quran_text = load_quran_text(surah)
    word_analysis = load_word_analysis(surah)
    qac_by_ayah = load_qac_morphemes(surah)

    if args.ayah is not None:
        bundle = build_ayah_bundle(surah, args.ayah, quran_text, word_analysis, qac_by_ayah)
        out_path = out_dir / f"{surah}_{args.ayah}.ayah.json"
        out_path.write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"wrote {out_path}")
        return 0

    ayah_numbers = discover_ayah_numbers(surah, quran_text)
    ayah_bundles = []
    filenames = []
    for a in ayah_numbers:
        bundle = build_ayah_bundle(surah, a, quran_text, word_analysis, qac_by_ayah)
        fname = f"{surah}_{a}.ayah.json"
        (out_dir / fname).write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")
        ayah_bundles.append(bundle)
        filenames.append(fname)
        print(f"wrote {out_dir / fname}")

    surah_bundle = build_surah_bundle(surah, ayah_bundles, filenames)
    surah_out_path = out_dir / f"{surah}.surah.json"
    surah_out_path.write_text(json.dumps(surah_bundle, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {surah_out_path}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RequiredSourceMissing as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        sys.exit(1)
