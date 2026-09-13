#!/usr/bin/env python3
"""
build_bundle.py — assemble the per-ayah / per-surah input bundle consumed by
`_ayah_commentary/v2/PROMPT.md` and `_surah_commentary/PROMPT.md`.

See `COMMENTARY_SPEC.md` §9 for the source inventory this script implements,
and `scripts/README.md` for usage.

Usage:
    python3 build_bundle.py --surah 103 [--ayah 1] [--out DIR]

Standard library only, with one exception: `.zst` files are decompressed by
shelling out to the `zstd` binary (the `zstandard` pip package is not assumed
to be installed). `.gz` files are decompressed with the stdlib `gzip` module.

Default commentary sources live under a single frozen root:
`../quran-data/data/` (see QURAN_DATA below). The intentional
sibling-workspace exception is Hermetic Focus Trace, which is required by
default and reads `../latent_activation/focus_trace` unless
`--exclude-focus-trace` is passed.

Before building anything, `preflight()` enumerates every expected source for
the requested surah/ayah and prints a table of present/missing sources,
aborting only if a REQUIRED source is missing. This is deliberate: two
sources have previously failed *silently* in production —
  (1) branch_inventories returning `{}` for surahs with no per-ayah focus run
      and no readable surah-level fallback packet (exit 0, no error), and
  (2) a zero-padding mismatch in a whole-surah-reading filename glob that
      silently dropped roughly half of the existing whole-surah readings.
Both classes of bug must be impossible to reproduce here: any source that is
*found but yields nothing parseable* must never collapse into the same
signal as "source absent" — see the whole-surah-reading and reader-walk
loaders below for the three-state (absent / parsed / found-but-unparsed)
distinction this requires.
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
import unicodedata
from datetime import datetime, timezone
from pathlib import Path


def compact_json_text(value):
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


# ---------------------------------------------------------------------------
# Repo layout — single source root
# ---------------------------------------------------------------------------

SCRIPT_PATH = Path(__file__).resolve()
PROSE_GEN_ROOT = SCRIPT_PATH.parent.parent          # .../prose_generation
PROJECTS_ROOT = PROSE_GEN_ROOT.parent               # .../_projects
sys.path.insert(0, str(PROSE_GEN_ROOT))

QURAN_DATA = PROJECTS_ROOT / "quran-data" / "data"
LATENT_ACTIVATION_ROOT = PROJECTS_ROOT / "latent_activation"

QURAN_TEXT_TSV = QURAN_DATA / "text" / "quran-uthmani.tsv"
WORD_ANALYSIS_DIR = QURAN_DATA / "analysis" / "word-analysis"
QAC_SQLITE_GZ = QURAN_DATA / "morphology" / "qac.sqlite.gz"
QAC_FURUQ_ROOT_MAP_SQLITE_GZ = QURAN_DATA / "bridges" / "qac-furuq-v4-root-map.sqlite.gz"

V12_TR_DIR = QURAN_DATA / "analysis" / "ayah-activation" / "v12-tr"
V12_TR_11AYAH_DIR = QURAN_DATA / "analysis" / "ayah-activation" / "v12-tr-11ayah"
V12_CROSS_RUN_TR_DIR = QURAN_DATA / "analysis" / "ayah-activation" / "v12-cross-run" / "tr"
NETWORK_V3_DIR = QURAN_DATA / "analysis" / "channels" / "network-v3"
FOCUS_TRACE_RUNS_DIR = LATENT_ACTIVATION_ROOT / "focus_trace" / "runs"
PERICOPES_PATH = NETWORK_V3_DIR / "pericopes" / "surah_pericopes.jsonl"
INTER_AYAH_DIR = QURAN_DATA / "analysis" / "inter-ayah"
DICTIONARY_TR_DIR = QURAN_DATA / "dictionary" / "tr"
GLOSSES_TR_DIR = QURAN_DATA / "translation" / "glosses" / "locales" / "tr"

ZSTD_CANDIDATES = ["/opt/homebrew/bin/zstd", "zstd"]

QUARANTINED_DIR_NAMES = {"pilot_invalid_prompt_leak"}
KNOWN_VARIANT_DIR_NAMES = {"left_first", "right_first"}
USE_PER_AYAH_FOCUS_RUNS = False
INCLUDE_HERMETIC_FOCUS_TRACE = True
REQUIRE_HERMETIC_FOCUS_TRACE = True
FOCUS_TRACE_VARIANT: str | None = None

BUNDLE_SCHEMA_VERSION = "input-bundle-v4"
SURAH_BUNDLE_SCHEMA_VERSION = "input-bundle-surah-v4"
BASMALA_LINGUISTIC_SOURCE_REF = "1:1"
BASMALA_EXCLUDED_SURAHS = {1, 9}


def relpath(path: Path) -> str:
    """Relative-ize a path against PROJECTS_ROOT for embedding in bundles
    (e.g. 'quran-data/data/analysis/...'), so provenance strings are stable
    regardless of where this checkout happens to live."""
    return str(path.relative_to(PROJECTS_ROOT))


def display_path(path: Path) -> str:
    """Project-relative path for logs and preflight output when possible."""
    try:
        return str(path.relative_to(PROJECTS_ROOT))
    except ValueError:
        return str(path)


def v12_lookup_ref(surah: int, ayah: int) -> str:
    """Reference used by V12 reader/publication files.

    S1 is the one canonical-numbering exception: Quran text and QAC count the
    basmalah as 1:1, while V12 reader/publication artifacts store it as 1:0.
    This is a transparent source lookup alias, not a bundle ayahRef rewrite."""
    if surah == 1 and ayah == 1:
        return "1:0"
    return f"{surah}:{ayah}"


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


# --- branch-inventory scoping (surah-scope fallback only) -------------------
#
# Citation forms found in real network-v3 review material (verified by scanning
# all 110 reader_a_pilot.md files corpus-wide -- do not narrow these without
# re-running that scan):
#
#   `ت ب ب:B001/m01`              arabic root, backticked   12,018 hits / 31 surahs
#   `quranic:root_000076:B007/m01` root_id, backticked      37,927 hits / 67 surahs
#   (ق د ر:B005/m01)              arabic root, NOT backticked  723 hits / 3 surahs
#
# The root_id form is the MOST common corpus-wide even though S1/S100/S103 --
# the surahs used for verification -- happen to contain only the arabic form.
# Handling only the arabic form would pass every specified test while silently
# dropping citations for 67 surahs; that is the exact failure class this
# builder is meant to preclude.
_CITE_AR_BACKTICK = re.compile(r"`([ء-ي](?:\s+[ء-ي])*)\s*:\s*(B\d+)(?:/(m\d+))?`")
_CITE_ID_BACKTICK = re.compile(r"`quranic:(root_\d+):(B\d+)(?:/(m\d+))?`")
_CITE_AR_BARE = re.compile(r"([ء-ي](?:\s+[ء-ي])*)\s*:\s*(B\d+)(?:/(m\d+))?")
_BACKTICK_SPAN = re.compile(r"`[^`]*`")


def normalize_root(root: str) -> str:
    """Join key for root strings. Inventory roots and qac_morphemes.root_ar are
    both space-separated (`'ق د ح'`) and in current data compare equal without
    normalisation -- verified across all 114 surahs: naive equality and
    space-stripped equality select the identical root set everywhere, and the
    join is non-empty for every surah. Spaces are stripped anyway so a future
    upstream spacing change degrades to a still-correct join rather than a
    silent zero-match."""
    if not root:
        return ""
    return unicodedata.normalize("NFC", root).replace(" ", "").strip()


def extract_channel_citations(channel_blocks: list) -> tuple:
    """Scans every string field of the channel subchannel records anchored at
    this ayah for `root:branch` citations, in all three observed forms.

    Returns (by_arabic_root, by_root_id, raw_tokens) where the first two are
    {normalized_key: set(branch_id)}. Every string field is scanned rather
    than only `active_motifs`: corpus-wide the tokens also appear in
    `ayah anchors` (33) and `synthesis` (1), and s002 carries 302 of them in
    an `active bridge motifs` field. Scanning all fields costs nothing and
    removes the need to keep a field allowlist in sync with upstream."""
    by_ar, by_id, raw = {}, {}, set()
    for block in channel_blocks or []:
        for value in block.values():
            if not isinstance(value, str) or not value:
                continue
            for m in _CITE_ID_BACKTICK.finditer(value):
                by_id.setdefault(m.group(1), set()).add(m.group(2))
                raw.add(m.group(0).strip("`"))
            for m in _CITE_AR_BACKTICK.finditer(value):
                by_ar.setdefault(normalize_root(m.group(1)), set()).add(m.group(2))
                raw.add(m.group(0).strip("`"))
            # Bare tokens: only look outside backticked spans, so the two
            # backticked forms above are not re-matched here.
            outside = _BACKTICK_SPAN.sub("", value)
            for m in _CITE_AR_BARE.finditer(outside):
                by_ar.setdefault(normalize_root(m.group(1)), set()).add(m.group(2))
                raw.add(m.group(0))
    return by_ar, by_id, raw


def _entry_root_ids(entry: dict) -> set:
    out = set()
    for branch in entry.get("branches", []) or []:
        for variant in branch.get("variants", []) or []:
            if variant.get("root_id"):
                out.add(variant["root_id"])
    return out


def scope_branch_inventories_to_ayah(branch_inventories: list, qac_rows: list,
                                      channel_blocks: list, ayah_ref: str) -> tuple:
    """Narrows a SURAH-scope branch inventory to what this ayah can justify.

    An inventory entry is retained if EITHER:
      (a) its root occurs in this ayah (from qac_morphemes[].root_ar) -- in
          which case EVERY branch is kept, unconditionally; or
      (b) it is explicitly cited by channel material anchored at this ayah --
          in which case only the specifically cited branches are kept.
    An entry admitted by both keeps all branches, per (a).

    Rule (a) keeps every branch on purpose. Layer 2 selects nothing
    (PRINCIPLES.md §3, §6): the non-activated branches of a root that is
    present in the ayah are the latent field the project exists to surface.
    Filtering them by activation or V12 strength would perform disambiguation
    invisibly and irreversibly, so no relevance signal is consulted here.

    Returns (scoped_inventories, report)."""
    ayah_roots = set()
    for row in qac_rows or []:
        key = normalize_root(row.get("root_ar") or "")
        if key:
            ayah_roots.add(key)

    cited_ar, cited_id, raw_tokens = extract_channel_citations(channel_blocks)

    retained, retained_meta = [], []
    dropped_roots = []
    matched_cite_ar, matched_cite_id = set(), set()

    for entry in branch_inventories:
        root = entry.get("root")
        root_key = normalize_root(root or "")
        entry_ids = _entry_root_ids(entry)
        in_ayah = bool(root_key) and root_key in ayah_roots

        cited_branches = set(cited_ar.get(root_key, set()))
        if root_key in cited_ar:
            matched_cite_ar.add(root_key)
        for rid in entry_ids:
            if rid in cited_id:
                cited_branches |= cited_id[rid]
                matched_cite_id.add(rid)

        if in_ayah:
            retained.append(entry)
            retained_meta.append({
                "root": root,
                "rule": "in_ayah",
                "branches_kept": len(entry.get("branches", []) or []),
                "branches_total": len(entry.get("branches", []) or []),
            })
        elif cited_branches:
            kept = [b for b in (entry.get("branches") or [])
                    if b.get("branch_id") in cited_branches]
            if not kept:
                # Root is cited but none of the cited branch ids exist on it.
                dropped_roots.append(root)
                continue
            retained.append({**entry, "branches": kept})
            retained_meta.append({
                "root": root,
                "rule": "cited_by_channel",
                "branches_kept": len(kept),
                "branches_total": len(entry.get("branches", []) or []),
                "cited_branch_ids": sorted(cited_branches),
            })
        else:
            dropped_roots.append(root)

    if not retained and not ayah_roots:
        report = {
            "applied": True,
            "roots_total": len(branch_inventories),
            "roots_retained": 0,
            "roots_dropped": len(dropped_roots),
            "retained": [],
            "dropped_roots": dropped_roots,
            "ayah_roots_from_qac": [],
            "channel_citations_found": len(raw_tokens),
            "citations_unresolvable_in_surah_inventory": sorted(
                [f"{k}:{b}" for k in set(cited_ar) - matched_cite_ar for b in sorted(cited_ar[k])] +
                [f"{k}:{b}" for k in set(cited_id) - matched_cite_id for b in sorted(cited_id[k])]
            ),
            "note": (
                "SCOPED, NOT ABSENT. This ayah has QAC morpheme rows but no "
                "lexical roots, so the surah-scope branch inventory has no "
                "ayah root to retain. The empty scoped inventory is deliberate "
                "for rootless units such as muqatta'at, not a missing source."
            ),
        }
        return retained, report

    if not retained:
        raise RequiredSourceMissing(
            f"branch-inventory scoping retained ZERO roots for {ayah_ref}: the "
            f"root join failed. ayah roots from qac_morphemes={sorted(ayah_roots)}; "
            f"inventory roots={[e.get('root') for e in branch_inventories][:10]}"
        )

    # Citations naming a root that is absent from the surah inventory entirely
    # were already unresolvable BEFORE scoping; recording them keeps that
    # pre-existing gap visible instead of letting scoping appear to cause it.
    unresolvable = sorted(
        [f"{k}:{b}" for k in set(cited_ar) - matched_cite_ar for b in sorted(cited_ar[k])] +
        [f"{k}:{b}" for k in set(cited_id) - matched_cite_id for b in sorted(cited_id[k])]
    )

    report = {
        "applied": True,
        "roots_total": len(branch_inventories),
        "roots_retained": len(retained),
        "roots_dropped": len(dropped_roots),
        "retained": retained_meta,
        "dropped_roots": dropped_roots,
        "ayah_roots_from_qac": sorted(ayah_roots),
        "channel_citations_found": len(raw_tokens),
        "citations_unresolvable_in_surah_inventory": unresolvable,
        "note": (
            "SCOPED, NOT ABSENT. The surah-scope fallback inventory covers every "
            "root in the surah; it is narrowed here to roots this ayah can "
            "justify -- roots occurring in this ayah (all their branches kept, "
            "unconditionally, because Layer 2 selects nothing) plus roots "
            "explicitly cited by channel material anchored here (only the cited "
            "branches kept, enough to resolve the citation). A root listed in "
            "dropped_roots is a deliberate scoping decision, not a missing source."
        ),
    }
    return retained, report


def augment_focus_inventory_with_citations(surah: int, focus_inventories: list,
                                            channel_blocks: list) -> tuple:
    """ADDITIVE-ONLY rule (b) for the focus-scoped path.

    A focus stage_00 packet covers only the focus ayah's own roots, but channel
    material anchored at that ayah legitimately cites roots from elsewhere in
    the surah (verified: 100:1's committed baseline bundle carried 18 such
    citations with no referent). This pulls the cited referents in from the
    surah packet and REMOVES NOTHING, so the focus path stays exactly as narrow
    as it was while its citations resolve.

    Returns (augmented_inventories, report)."""
    if not channel_blocks:
        return focus_inventories, {"applied": False, "note": "no channel blocks anchored here"}

    packet_path = V12_TR_DIR / f"s{surah:03d}" / "full_context_packet.json"
    if not packet_path.exists():
        return focus_inventories, {
            "applied": False,
            "note": f"no surah packet at {packet_path} to resolve citations from",
        }

    cited_ar, cited_id, _ = extract_channel_citations(channel_blocks)
    if not cited_ar and not cited_id:
        return focus_inventories, {"applied": False, "note": "no root:branch citations found"}

    present = {normalize_root(e.get("root") or "") for e in focus_inventories}
    surah_inv = json.loads(packet_path.read_text(encoding="utf-8")).get("branch_inventories", [])

    added, added_meta = [], []
    for entry in surah_inv:
        root_key = normalize_root(entry.get("root") or "")
        if root_key in present:
            continue  # already carried by the focus packet; never modified
        branch_ids = set(cited_ar.get(root_key, set()))
        for rid in _entry_root_ids(entry):
            if rid in cited_id:
                branch_ids |= cited_id[rid]
        if not branch_ids:
            continue
        kept = [b for b in (entry.get("branches") or [])
                if b.get("branch_id") in branch_ids]
        if not kept:
            continue
        added.append({**entry, "branches": kept})
        added_meta.append({
            "root": entry.get("root"),
            "rule": "cited_by_channel",
            "branches_kept": len(kept),
            "branches_total": len(entry.get("branches", []) or []),
            "cited_branch_ids": sorted(branch_ids),
        })

    if not added:
        return focus_inventories, {"applied": False, "note": "no unresolved citations to add"}

    return focus_inventories + added, {
        "applied": True,
        "roots_added": len(added),
        "added": added_meta,
        "note": (
            "ADDITIVE ONLY. The focus packet's own roots are untouched; these "
            "extra roots were appended solely so that `root:branch` citations "
            "made by channel material anchored at this ayah have their referent "
            "present. Only the specifically cited branches are included."
        ),
    }


def _load_branch_inventories_fallback(surah: int, ayah: int, focus_dir: Path,
                                       qac_rows: list = None,
                                       channel_blocks: list = None) -> tuple:
    """Surah-scope fallback for branch inventories.

    `full_context_packet.json` exists for all 114 surahs and carries the same
    `branch_inventories` list. Its scope differs from a stage_00 focus packet:
    it covers every root in the surah, not only this ayah's roots, and it is
    not staged (no before/neighbour-revealed distinction). Both facts are
    recorded in coverage so the writer can state them.

    When `qac_rows` is supplied the inventory is scoped to this ayah (see
    scope_branch_inventories_to_ayah). Preflight calls this without qac_rows
    purely to check presence, and must not pay for or be affected by scoping."""
    packet_path = V12_TR_DIR / f"s{surah:03d}" / "full_context_packet.json"
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
    scoping_report = {"applied": False, "note": "not scoped (presence check only)"}
    if qac_rows is not None:
        branch_inventories, scoping_report = scope_branch_inventories_to_ayah(
            branch_inventories, qac_rows, channel_blocks, f"{surah}:{ayah}"
        )

    variant = {
        "source_file": relpath(packet_path),
        "branch_inventories": branch_inventories,
    }
    coverage = {
        "present": True,
        "scope": "surah-fallback-scoped-to-ayah" if scoping_report["applied"] else "surah",
        "variants": {
            "full_context_packet": {
                "present": True,
                "roots": [r.get("root") for r in branch_inventories],
                "branch_counts": {
                    r.get("root"): len(r.get("branches", [])) for r in branch_inventories
                },
                "missing_branch_inventories": packet.get("missing_branch_inventories", []),
                "note": (
                    "surah-scope fallback: the default commentary workflow does "
                    "not consume per-ayah focus packets, so the source packet is "
                    "scoped by this builder to roots this ayah can justify and "
                    "carries no staged reveal order"
                ),
            }
        },
        "scoping": scoping_report,
    }
    return {"full_context_packet": variant}, coverage


def load_v12_branch_inventories(surah: int, ayah: int, qac_rows: list = None,
                                 channel_blocks: list = None) -> tuple:
    """Returns (variants_dict, coverage_dict).

    variants_dict: {variant_name: {"stage_00_file": relpath, "roots": [...]}}
    roots come verbatim from branch_inventories in the stage_00_*.json packet
    (the packet is scoped to the focus ayah's own roots at stage 0, before any
    neighbour is revealed).

    The focus-scoped path is already narrow and is returned untouched. Only the
    surah-scope fallback is narrowed, and only when `qac_rows` is supplied."""
    focus_dir = V12_TR_DIR / f"s{surah:03d}" / f"focus_{surah}_{ayah}"
    if not USE_PER_AYAH_FOCUS_RUNS:
        return _load_branch_inventories_fallback(
            surah, ayah, focus_dir, qac_rows, channel_blocks
        )

    variants = _variant_dirs(focus_dir)
    out = {}
    coverage = {"present": False, "variants": {}}
    if not variants:
        # Per-ayah focus runs exist for only a handful of ayahs corpus-wide
        # (a method-development pilot). The surah-scope full_context_packet.json
        # carries the same branch_inventories structure for all 114 surahs, so
        # fall back to it rather than emitting a bundle with no latent material.
        return _load_branch_inventories_fallback(
            surah, ayah, focus_dir, qac_rows, channel_blocks
        )

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
        branch_inventories, aug_report = augment_focus_inventory_with_citations(
            surah, branch_inventories, channel_blocks
        )
        coverage["citation_augmentation"] = aug_report
        out[variant_name] = {
            "stage_00_file": relpath(stage_00_path),
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
        return _load_branch_inventories_fallback(
            surah, ayah, focus_dir, qac_rows, channel_blocks
        )
    # Focus-scoped packets are already ayah-scoped upstream; left untouched.
    coverage["scope"] = "focus"
    coverage["scoping"] = {
        "applied": False,
        "note": "focus-scoped stage_00 packet is already narrow; scoping not applied",
    }
    return out, coverage


def load_v12_reader_responses(surah: int, ayah: int) -> tuple:
    """Returns (variants_dict, coverage_dict). Optional source: a missing
    response set is a machine-readable coverage fact, not an error.

    variants_dict: {variant_name: {reader_id: {"stage_00": {...}, ...}}}
    """
    focus_dir = V12_TR_DIR / f"s{surah:03d}" / f"focus_{surah}_{ayah}"
    if not USE_PER_AYAH_FOCUS_RUNS:
        return {}, {
            "present": False,
            "variants": {},
            "note": (
                "Per-ayah focus-run reader responses are retired from the "
                "default commentary workflow. Use regular reader walks, "
                "plus/minus-5 reader walks, and cross-run publication findings "
                "for corpus-wide reader-derived evidence."
            ),
        }

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
# Source: Hermetic Focus Trace responses (generated in latent_activation)
# ---------------------------------------------------------------------------

def focus_trace_run_dirs(surah: int) -> list[Path]:
    """Candidate Hermetic Focus Trace run dirs, newest canonical spelling first.

    Older upstream runs used unpadded names (`s12`) while the production
    commentary convention is zero-padded (`s012`). Probe both so a naming
    mismatch cannot silently remove HFT evidence.
    """
    padded = FOCUS_TRACE_RUNS_DIR / f"s{surah:03d}"
    unpadded = FOCUS_TRACE_RUNS_DIR / f"s{surah}"
    if padded == unpadded:
        return [padded]
    return [padded, unpadded]


def focus_trace_run_dir(surah: int) -> Path:
    """Compatibility helper for display-only callers."""
    return focus_trace_run_dirs(surah)[0]


def focus_trace_packet_path(surah: int, ayah: int) -> Path:
    return focus_trace_run_dir(surah) / "packets" / f"{surah}_{ayah}.packet.json"


def focus_trace_packet_paths(surah: int, ayah: int) -> list[Path]:
    return [
        run_dir / "packets" / f"{surah}_{ayah}.packet.json"
        for run_dir in focus_trace_run_dirs(surah)
    ]


def focus_trace_response_files_in_run(run_dir: Path, surah: int, ayah: int) -> list[Path]:
    readers_dir = run_dir / "readers"
    if not readers_dir.exists():
        return []
    files = []
    seen = set()
    for reader_dir in sorted(d for d in readers_dir.iterdir() if d.is_dir()):
        if reader_dir.name in QUARANTINED_DIR_NAMES:
            continue
        exact = reader_dir / f"{surah}_{ayah}.focus_trace.json"
        candidates = []
        if exact.exists():
            candidates.append(exact)
        candidates.extend(sorted(reader_dir.glob(f"{surah}_{ayah}.*.focus_trace.json")))
        for candidate in candidates:
            if candidate in seen:
                continue
            variant = focus_trace_response_variant(candidate, surah, ayah)
            if FOCUS_TRACE_VARIANT is not None and variant != FOCUS_TRACE_VARIANT:
                continue
            files.append(candidate)
            seen.add(candidate)
    return files


def focus_trace_response_files(surah: int, ayah: int) -> list[Path]:
    files = []
    seen = set()
    for run_dir in focus_trace_run_dirs(surah):
        for candidate in focus_trace_response_files_in_run(run_dir, surah, ayah):
            if candidate not in seen:
                files.append(candidate)
                seen.add(candidate)
    return files


def focus_trace_response_variant(path: Path, surah: int, ayah: int) -> str:
    prefix = f"{surah}_{ayah}"
    suffix = ".focus_trace.json"
    if path.name == f"{prefix}{suffix}":
        return "default"
    if path.name.startswith(f"{prefix}.") and path.name.endswith(suffix):
        return path.name[len(prefix) + 1 : -len(suffix)]
    return path.stem


def focus_trace_reader_key(path: Path, surah: int, ayah: int) -> str:
    variant = focus_trace_response_variant(path, surah, ayah)
    if variant == "default":
        return path.parent.name
    return f"{path.parent.name}:{variant}"


def focus_trace_packet_summary(packet_path: Path, expected_ref: str | None = None) -> dict | None:
    if not packet_path.exists():
        return None
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    if not isinstance(packet, dict):
        raise ValueError("packet JSON must be an object")
    if expected_ref is not None and packet.get("focus_ref") != expected_ref:
        raise ValueError(
            f"packet focus_ref {packet.get('focus_ref')!r} does not match {expected_ref}"
        )
    root_mappings = packet["root_mappings"] if "root_mappings" in packet else []
    if not isinstance(root_mappings, list):
        raise ValueError("packet root_mappings must be a list")
    split_roots = []
    for mapping in root_mappings:
        if not isinstance(mapping, dict):
            raise ValueError("packet root_mappings entries must be objects")
        if mapping.get("mapping_status") == "split":
            split_roots.append({
                "qac_root": mapping.get("qac_root"),
                "targets": mapping.get("targets", []),
            })
    return {
        "source_file": relpath(packet_path),
        "protocol": packet.get("protocol"),
        "focus_ref": packet.get("focus_ref"),
        "window": packet.get("window", []),
        "ayah_count": packet.get("ayah_count"),
        "split_root_mappings": split_roots,
    }


def load_v12_focus_trace_hermetic(surah: int, ayah: int) -> tuple:
    """Returns (dict, coverage_dict) for Hermetic Focus Trace.

    HFT is required by default. `--exclude-focus-trace` is the only normal
    escape hatch, and the coverage block must make that choice explicit.
    """
    checked_dirs = focus_trace_run_dirs(surah)
    if not INCLUDE_HERMETIC_FOCUS_TRACE:
        return {}, {
            "present": False,
            "packet_present": False,
            "readers": {},
            "run_dirs_checked": [display_path(path) for path in checked_dirs],
            "excluded": True,
            "note": (
                "Hermetic Focus Trace intentionally excluded with "
                "--exclude-focus-trace."
            ),
        }

    candidates = []
    for run_dir in checked_dirs:
        packet_path = run_dir / "packets" / f"{surah}_{ayah}.packet.json"
        reader_files = focus_trace_response_files_in_run(run_dir, surah, ayah)
        if packet_path.exists() or reader_files:
            candidates.append((run_dir, packet_path, reader_files))

    base_coverage = {
        "present": False,
        "packet_present": False,
        "packet_source_file": None,
        "readers": {},
        "run_dirs_checked": [display_path(path) for path in checked_dirs],
        "excluded": False,
    }
    if not candidates:
        coverage = dict(base_coverage)
        coverage["note"] = (
            "no Hermetic Focus Trace packet or responses found in checked "
            f"run dirs: {', '.join(display_path(path) for path in checked_dirs)}"
        )
        return {}, coverage
    if len(candidates) > 1:
        coverage = dict(base_coverage)
        coverage["active_run_dirs"] = [display_path(item[0]) for item in candidates]
        coverage["note"] = (
            "ambiguous Hermetic Focus Trace run dirs: more than one checked "
            "directory contains packet or response files for this ayah. "
            "Normalize upstream to one directory before building."
        )
        return {}, coverage

    ayah_ref = f"{surah}:{ayah}"
    run_dir, packet_path, reader_files = candidates[0]
    try:
        packet_summary = focus_trace_packet_summary(packet_path, ayah_ref)
    except (json.JSONDecodeError, ValueError) as exc:
        coverage = dict(base_coverage)
        coverage.update({
            "packet_present": True,
            "packet_source_file": relpath(packet_path),
            "selected_run_dir": display_path(run_dir),
            "note": f"Hermetic Focus Trace packet is invalid or mismatched: {exc}",
        })
        return {}, coverage

    out = {}
    coverage = {
        "present": False,
        "packet_present": packet_summary is not None,
        "packet_source_file": relpath(packet_path) if packet_path.exists() else None,
        "readers": {},
        "run_dirs_checked": [display_path(path) for path in checked_dirs],
        "selected_run_dir": display_path(run_dir),
        "excluded": False,
    }
    if packet_summary is None:
        coverage["note"] = (
            "Hermetic Focus Trace reader responses are present but the packet "
            f"is missing: {display_path(packet_path)}"
        )
        return out, coverage
    if packet_summary is not None:
        out["packet_summary"] = packet_summary
        coverage["packet_protocol"] = packet_summary.get("protocol")
        coverage["packet_bytes"] = packet_path.stat().st_size
        coverage["split_root_count"] = len(packet_summary.get("split_root_mappings", []))

    if not reader_files:
        coverage["note"] = (
            "Hermetic Focus Trace packet exists but no reader responses are "
            f"present under {display_path(run_dir / 'readers')}"
        )
        return out, coverage

    readers = {}
    reader_errors = []
    for response_path in reader_files:
        reader_id = focus_trace_reader_key(response_path, surah, ayah)
        variant = focus_trace_response_variant(response_path, surah, ayah)
        try:
            response = json.loads(response_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            coverage["readers"][reader_id] = {
                "present": False,
                "source_file": relpath(response_path),
                "variant": variant,
                "note": f"invalid JSON: {exc}",
            }
            reader_errors.append(f"{reader_id}: invalid JSON: {exc}")
            continue
        if not isinstance(response, dict):
            coverage["readers"][reader_id] = {
                "present": False,
                "source_file": relpath(response_path),
                "variant": variant,
                "note": "reader JSON must be an object",
            }
            reader_errors.append(f"{reader_id}: reader JSON must be an object")
            continue
        if response.get("focus_ref") != ayah_ref:
            coverage["readers"][reader_id] = {
                "present": False,
                "source_file": relpath(response_path),
                "variant": variant,
                "note": f"focus_ref {response.get('focus_ref')!r} does not match {ayah_ref}",
            }
            reader_errors.append(
                f"{reader_id}: focus_ref {response.get('focus_ref')!r} "
                f"does not match {ayah_ref}"
            )
            continue
        readers[reader_id] = response
        coverage["readers"][reader_id] = {
            "present": True,
            "source_file": relpath(response_path),
            "variant": variant,
            "protocol": response.get("protocol"),
            "baseline_models": len(response.get("baseline_models", []) or []),
            "context_deltas": len(response.get("context_deltas", []) or []),
            "surprising_valid_outliers": len(response.get("surprising_valid_outliers", []) or []),
        }

    if reader_errors:
        coverage["valid_reader_count"] = len(readers)
        coverage["note"] = (
            "Hermetic Focus Trace reader files are malformed or mismatched: "
            + "; ".join(reader_errors)
        )
        return out, coverage
    if readers:
        out["readers"] = readers
        coverage["present"] = True
        coverage["reader_count"] = len(readers)
    else:
        coverage["note"] = "Hermetic Focus Trace response files found, but none matched this ayah"
    return out, coverage


# ---------------------------------------------------------------------------
# Source: v12 reader ayah walks (markdown)
# ---------------------------------------------------------------------------

_WALK_H1_RE = re.compile(r"^#\s+(.*)$")
# The corpus uses punctuation separators (dash, colon, or pipe), a bare space
# before the Arabic surface, and ref-only headings. Keep the title optional so
# every observed form resolves to the same ayah block.
_WALK_H2_RE = re.compile(
    r"^##\s+(\d+:\d+)(?:(?:\s*[—–|:-]\s*|\s+)(.*))?$"
)
_WALK_H3_RE = re.compile(r"^###\s+(.*)$")


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
        m1 = _WALK_H1_RE.match(line)
        if m1:
            current_h1 = m1.group(1).strip()
            i += 1
            continue
        m2 = _WALK_H2_RE.match(line)
        if m2:
            ayah_ref = m2.group(1)
            block_start = i + 1
            j = block_start
            while j < n and not _WALK_H1_RE.match(lines[j]) and not _WALK_H2_RE.match(lines[j]):
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
                    m3 = _WALK_H3_RE.match(bl)
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


def load_v12_reader_walks(
    surah: int,
    ayah: int,
    source_dir: Path = V12_TR_DIR,
    source_label: str = "v12 reader walks",
) -> tuple:
    """Returns (dict, coverage_dict) for every reader_s{NNN}_{a,b}_ayah_walk.md
    found for this surah, restricted to this ayah's block.

    A walk file that exists but yields zero recognised `## ref — ...`
    headings at all is a *format* failure, not a per-ayah absence, and is
    reported as a distinct coverage state ("present": False with
    "zero_headings_parsed": True) rather than being silently indistinguishable
    from "this ayah's heading isn't in an otherwise-normal file"."""
    control_dir = source_dir / f"s{surah:03d}" / "full_context_control"
    canonical_ref = f"{surah}:{ayah}"
    alias_ref = v12_lookup_ref(surah, ayah)
    lookup_refs = [canonical_ref] + ([] if alias_ref == canonical_ref else [alias_ref])
    out = {}
    coverage = {"present": False, "readers": {}, "lookup_refs": lookup_refs}
    if not control_dir.exists():
        coverage["note"] = f"{source_label}: full_context_control dir not found: {control_dir}"
        return out, coverage

    walk_files = sorted(control_dir.glob(f"reader_s{surah:03d}_*_ayah_walk.md"))
    for wf in walk_files:
        m = re.search(r"reader_s\d+_([a-z])_ayah_walk\.md$", wf.name)
        reader_label = f"reader_{m.group(1)}" if m else wf.stem
        raw_text = wf.read_text(encoding="utf-8")
        parsed = parse_ayah_walk_markdown(raw_text)
        if not parsed and raw_text.strip():
            # File found, non-empty, but zero `## ref — ...` headings matched:
            # a format failure, never to be reported the same as "absent".
            print(
                f"WARNING: {wf} found but 0 ayah headings were recognised in it "
                f"(unrecognised format) -- treating as unparsed, not absent.",
                file=sys.stderr,
            )
            coverage["readers"][reader_label] = {
                "present": False,
                "zero_headings_parsed": True,
                "note": f"{wf.name} found but zero ayah headings recognised (unrecognised format)",
            }
            continue
        matched_ref = next((ref for ref in lookup_refs if ref in parsed), None)
        if matched_ref is not None:
            out[reader_label] = parsed[matched_ref]
            out[reader_label]["source_file"] = relpath(wf)
            coverage["readers"][reader_label] = {
                "present": True,
                "source_file": out[reader_label]["source_file"],
                "matched_ref": matched_ref,
            }
            coverage["present"] = True
        else:
            coverage["readers"][reader_label] = {
                "present": False,
                "note": f"{'/'.join(lookup_refs)} heading not found in {wf.name}",
            }
    if alias_ref != canonical_ref:
        coverage["note"] = (
            (coverage.get("note") + "; " if coverage.get("note") else "") +
            f"accepted V12 source lookup alias {alias_ref} for canonical ayah {canonical_ref}"
        )
    if not walk_files:
        coverage["note"] = f"{source_label}: no reader_s{surah:03d}_*_ayah_walk.md files found"
    return out, coverage


def load_v12_cross_run_publication(surah: int, ayah: int) -> tuple:
    """Returns (row_dict_or_none, coverage_dict) for the compact final
    v12-cross-run publication findings for this ayah.

    This source is reader-derived and reconciled across regular and +/-5
    readers upstream, so it is kept separate from the raw reader-walk fields.
    The bundle only carries the requested ayah's row, not the full surah file."""
    path = V12_CROSS_RUN_TR_DIR / f"{surah}_ayah_findings_publication.json"
    ayah_ref = v12_lookup_ref(surah, ayah)
    coverage = {"present": False, "source_file": None}
    if not path.exists():
        coverage["note"] = f"no v12 cross-run publication file at {path}"
        return None, coverage

    data = json.loads(path.read_text(encoding="utf-8"))
    row = None
    for candidate in data.get("ayat", []) or []:
        if candidate.get("ayah_ref") == ayah_ref:
            row = candidate
            break

    coverage["source_file"] = relpath(path)
    coverage["protocol"] = data.get("protocol")
    coverage["language"] = data.get("language")
    coverage["lookup_ref"] = ayah_ref
    if ayah_ref != f"{surah}:{ayah}":
        coverage["canonical_ayah_ref"] = f"{surah}:{ayah}"
    if row is None:
        coverage["note"] = f"{ayah_ref} not found in {path.name}"
        return None, coverage

    findings = row.get("findings", []) or []
    grade_counts = {}
    for finding in findings:
        grade = finding.get("grade") or "(missing)"
        grade_counts[grade] = grade_counts.get(grade, 0) + 1

    coverage.update({
        "present": True,
        "finding_count": len(findings),
        "grade_counts": grade_counts,
        "note": (
            "Compact final cross-run findings for this ayah, reconciled "
            "upstream from regular and plus/minus-5 reader runs; use as a "
            "coverage/priority check, not as replacement prose."
        ),
    })
    return {
        "source_file": relpath(path),
        "protocol": data.get("protocol"),
        "language": data.get("language"),
        "surah": data.get("surah"),
        "ayah_ref": row.get("ayah_ref"),
        "canonical_ayah_ref": f"{surah}:{ayah}",
        "baseline": row.get("baseline"),
        "findings": findings,
    }, coverage


# ---------------------------------------------------------------------------
# Source: whole-surah reading (butuncul-okuma.md)
# ---------------------------------------------------------------------------

# Three observed per-ayah marker formats across the corpus (verified against
# all 30 *-butuncul-okuma.md files):
#   BOLD: **103:1.** <arabic> — <turkish reading> {citations}   (27/30 files)
#   H2:   ## 88:1 — <arabic>          (turkish reading + citations on
#                                       following body line(s), S88)
#   BARE: 87:1 — <turkish reading> {citations}   (no arabic; second S87
#                                       reveal-order variant file)
# S89 (89-0-30-butuncul-okuma.md) uses running prose with no per-ayah marker
# at all in any of the three shapes; that file is a genuine "found but
# unparseable" case (see load_butuncul_okuma).
_BUTUNCUL_BOLD_RE = re.compile(r"^\*\*(\d+:\d+)\.\*\*\s+(.*)$")
_BUTUNCUL_BARE_RE = re.compile(r"^(\d+:\d+)\s*[—–-]\s*(.*)$")
_BUTUNCUL_H2_RE = re.compile(r"^##\s+(\d+:\d+)(?:\s*[—–-]\s*(.*))?$")
_BUTUNCUL_BRACE_RE = re.compile(r"\{([^{}]*)\}\s*$")
_BUTUNCUL_FILENAME_RE = re.compile(r"^(\d+)-(\d+)-(\d+)-butuncul-okuma\.md$")


def _split_citations(raw: str) -> list:
    """Root-citation lists are semicolon-separated when more than one root is
    cited (every corpus file observed to use ';' does so consistently), but a
    few surahs (e.g. S88) separate branches of a *single* root with commas
    and never use ';' at all. Prefer ';' when present; otherwise fall back to
    ',' so a single-root citation block doesn't collapse into one opaque
    string. When neither separator is present the whole string is the one
    citation (identical to the original strict-';' behaviour in that case)."""
    raw = raw.strip()
    if not raw:
        return []
    sep = ";" if ";" in raw else ","
    return [c.strip() for c in raw.split(sep) if c.strip()]


def parse_butuncul_document(text: str) -> tuple:
    """Parses one *-butuncul-okuma.md file's full text, auto-detecting the
    per-ayah marker format line by line (a single file is expected to use one
    format consistently, but nothing here assumes that in a way that would
    break mixed input). Returns (ayahRef -> parsed dict, meta dict) where meta
    carries which format(s) fired and how many ayahs were recovered, so the
    caller can tell "matched nothing" apart from "matched fine"."""
    lines = text.splitlines()
    out: dict = {}
    formats_used: set = set()
    n = len(lines)
    i = 0
    while i < n:
        raw_line = lines[i]
        stripped = raw_line.strip()

        m_h2 = _BUTUNCUL_H2_RE.match(stripped)
        if m_h2:
            ref = m_h2.group(1)
            arabic_text = (m_h2.group(2) or "").strip()
            body_lines = []
            j = i + 1
            while j < n:
                nxt = lines[j].strip()
                if _BUTUNCUL_H2_RE.match(nxt) or _BUTUNCUL_BOLD_RE.match(nxt) or _BUTUNCUL_BARE_RE.match(nxt):
                    break
                body_lines.append(lines[j])
                j += 1
            body_text = "\n".join(body_lines).strip()
            text_no_brace, citations = _extract_butuncul_braces(body_text)
            reading_text = re.sub(r"^Birincil okuma[:,]?\s*", "", text_no_brace)
            out[ref] = {
                "raw_line": "\n".join([raw_line] + body_lines).strip(),
                "arabic_text": arabic_text,
                "reading_text_tr": reading_text.strip(),
                "root_citations": citations,
            }
            formats_used.add("h2")
            i = j
            continue

        m_bold = _BUTUNCUL_BOLD_RE.match(stripped)
        m_bare = None if m_bold else _BUTUNCUL_BARE_RE.match(stripped)
        m = m_bold or m_bare
        if m:
            ref = m.group(1)
            rest = m.group(2)
            if m_bold:
                # "<arabic> — <turkish> {citations}"
                arabic_text, sep, remainder = rest.partition(" — ")
                if not sep:
                    arabic_text, remainder = "", rest
            else:
                # bare format has no arabic segment at all: "<turkish> {citations}"
                arabic_text, remainder = "", rest
            text_no_brace, citations = _extract_butuncul_braces(remainder)
            reading_text = re.sub(r"^Birincil okuma[:,]?\s*", "", text_no_brace)
            out[ref] = {
                "raw_line": stripped,
                "arabic_text": arabic_text.strip(),
                "reading_text_tr": reading_text.strip(),
                "root_citations": citations,
            }
            formats_used.add("bold" if m_bold else "bare")
            i += 1
            continue

        i += 1

    fmt = "+".join(sorted(formats_used)) if formats_used else "none"
    return out, {"format": fmt, "ayah_count_parsed": len(out)}


def _extract_butuncul_braces(remainder: str) -> tuple:
    root_citations = []
    reading_text = remainder
    brace_m = _BUTUNCUL_BRACE_RE.search(remainder)
    if brace_m:
        root_citations = _split_citations(brace_m.group(1))
        reading_text = remainder[: brace_m.start()].strip()
    return reading_text, root_citations


def load_butuncul_okuma(surah: int) -> tuple:
    """Returns (dict {ayahRef: parsed_line}, coverage_dict, file_path or None).

    Discovers ALL `*-butuncul-okuma.md` files for the surah regardless of
    zero-padding or reveal-order index (S87 has two: reveal-order 0 and 1),
    parses each independently, and — when more than one exists — picks the
    reveal-order-0 file as canonical when it parsed successfully, falling
    back to whichever file parsed the most ayahs. Every discovered file is
    recorded in coverage['files_found']; none is silently dropped. A file
    that is found but parses to zero ayahs (S89's running-prose format, which
    matches none of the three known per-ayah marker shapes) is flagged
    distinctly and never reported the same as "no file found"."""
    control_dir = V12_TR_DIR / f"s{surah:03d}" / "full_context_control"
    coverage = {"present": False}
    if not control_dir.exists():
        coverage["note"] = f"full_context_control dir not found: {control_dir}"
        return {}, coverage, None

    patterns = {f"{surah:03d}-*-*-butuncul-okuma.md", f"{surah}-*-*-butuncul-okuma.md"}
    matches = sorted({m for pattern in patterns for m in control_dir.glob(pattern)})
    if not matches:
        coverage["note"] = f"no *-butuncul-okuma.md for surah {surah} under {control_dir}"
        return {}, coverage, None

    parsed_by_path = {}
    files_found = []
    for path in matches:
        text = path.read_text(encoding="utf-8")
        ayah_map, meta = parse_butuncul_document(text)
        m = _BUTUNCUL_FILENAME_RE.match(path.name)
        reveal_index = int(m.group(2)) if m else None
        parsed_by_path[path] = (ayah_map, reveal_index, meta)
        files_found.append({
            "source_file": relpath(path),
            "reveal_index": reveal_index,
            "format_detected": meta["format"],
            "ayah_count_parsed": meta["ayah_count_parsed"],
        })
        if not ayah_map:
            print(
                f"WARNING: {path} found but 0 ayah lines parsed from it "
                f"(format_detected={meta['format']!r}) -- treating as unparsed, "
                f"not absent.",
                file=sys.stderr,
            )

    candidates = [p for p in matches if parsed_by_path[p][0]]
    primary_path = None
    if candidates:
        zero_rev = [p for p in candidates if parsed_by_path[p][1] == 0]
        pool = zero_rev if zero_rev else candidates
        primary_path = sorted(pool, key=lambda p: -len(parsed_by_path[p][0]))[0]

    out = parsed_by_path[primary_path][0] if primary_path else {}
    coverage["present"] = bool(out)
    coverage["files_found"] = files_found
    if len(matches) > 1 or not out:
        notes = []
        if len(matches) > 1:
            notes.append(
                f"{len(matches)} whole-surah reading files found for surah {surah}; "
                f"using {relpath(primary_path) if primary_path else 'none (all parsed to zero)'} as canonical"
            )
        if not out:
            notes.append(
                f"file(s) found for surah {surah} but zero ayah lines parsed from any "
                f"of them (see files_found for per-file format detection) -- this is NOT "
                f"the same as no file existing"
            )
        coverage["note"] = "; ".join(notes)
    return out, coverage, primary_path


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
    # s002 carries 302 `root:branch/motif` citations in an "Active bridge
    # motifs" field. Without this mapping the field never reaches the bundle,
    # so those citations are silently dropped -- the same silent-drop class
    # this builder exists to eliminate.
    "active bridge motifs": "active_bridge_motifs",
    "ayah anchors": "ayah_anchors",
    "synthesis": "synthesis",
}

CHANNEL_GENERATED_OUTPUT_FILES = [
    "channel_candidates.jsonl",
    "channel_candidates.tsv",
    "summary.json",
    "families/candidate_graphs.jsonl",
    "families/candidate_similarity_edges.tsv",
    "families/channel_families.jsonl",
    "families/candidate_family_membership.tsv",
    "families/family_branch_inventory.tsv",
    "families/consolidation_summary.json",
    "paths/path_summary.json",
    "paths/path_families/semantic_path_families.jsonl",
    "paths/path_families/semantic_path_families.jsonl.gz",
    "paths/path_families/path_similarity_edges.tsv",
    "paths/path_families/path_family_summary.json",
]


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

    Parses `analysis/channels/network-v3/s{NNN}/review/reader_a_pilot.md`
    into parent channels and their subchannels. This is FIRST-PASS,
    SINGLE-READER review output, not an adjudicated channel ledger: there is
    no accept/reject, no per-ayah maturity, and no second reader. Coverage
    says so explicitly, because the disclosure rules in docs/CHANNELS.md
    depend on a maturity column this source does not have."""
    review_dir = NETWORK_V3_DIR / f"s{surah:03d}" / "review"
    path = review_dir / "reader_a_pilot.md"
    coverage = {"present": False, "review_status": "first-pass-single-reader"}
    if not path.exists():
        coverage["note"] = (
            f"no channel review at {path}. network-v3 does not have a first-pass "
            f"review for every surah (some surah dirs don't exist at all — e.g. very "
            f"short surahs may be excluded from candidate discovery — and a few "
            f"existing surah dirs simply have no review/reader_a_pilot.md file yet)."
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


def load_channel_generated_outputs(surah: int) -> tuple:
    """Return a lightweight manifest for network-v3 generated channel outputs.

    These files can be large, so ayah bundles expose presence, paths, and sizes
    rather than inlining their contents. A cold agent with repository access may
    read only the listed quran-data files it needs."""
    base = NETWORK_V3_DIR / f"s{surah:03d}"
    files = []
    missing = []
    for rel in CHANNEL_GENERATED_OUTPUT_FILES:
        path = base / rel
        if path.exists():
            files.append({
                "path": relpath(path),
                "role": rel,
                "bytes": path.stat().st_size,
                "compressed": path.suffix == ".gz",
            })
        else:
            missing.append(rel)
    present = bool(files)
    coverage = {
        "present": present,
        "source_dir": relpath(base) if base.exists() else None,
        "file_count": len(files),
        "missing_expected_files": missing,
        "note": (
            "Generated network-v3 channel discovery/family/path outputs are "
            "available as external quran-data files; read them only when channel "
            "detail is necessary, and do not treat them as an adjudicated channel "
            "ledger."
            if present else
            f"no generated network-v3 channel output directory at {base}"
        ),
    }
    return {
        "source_dir": relpath(base) if base.exists() else None,
        "files": files,
        "usage": (
            "External source manifest only. These generated outputs may inform "
            "channel-family/path context when the agent has file access, but "
            "first-pass review limits still apply: no established channel name, "
            "accept/reject claim, or maturity claim unless a future adjudicated "
            "ledger is present."
        ),
    }, coverage


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

VALID_LABELS = {"strong", "medium", "weak", "no value", "contrast"}


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
            if label not in VALID_LABELS and ref in VALID_LABELS and re.match(r"^\d+:\d+(?:-\d+)?$", label):
                label, ref = ref, label
            if label not in VALID_LABELS:
                raise RuntimeError(f"{path}:{lineno}: unrecognised label {label!r}")
            rows.append({"label": label, "ref": ref, "note": note})
            label_counts[label] = label_counts.get(label, 0) + 1

    coverage["present"] = True
    coverage["row_count"] = len(rows)
    coverage["label_counts"] = label_counts
    return rows, coverage


# ---------------------------------------------------------------------------
# Source: surah pericopes (new)
# ---------------------------------------------------------------------------

_pericope_rows_by_surah_cache = None


def _load_all_pericope_rows() -> dict:
    global _pericope_rows_by_surah_cache
    if _pericope_rows_by_surah_cache is None:
        rows_by_surah: dict = {}
        if PERICOPES_PATH.exists():
            with open(PERICOPES_PATH, encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    row = json.loads(line)
                    rows_by_surah.setdefault(row["surah"], []).append(row)
            for k in rows_by_surah:
                rows_by_surah[k] = sorted(rows_by_surah[k], key=lambda r: r["pericope"])
        _pericope_rows_by_surah_cache = rows_by_surah
    return _pericope_rows_by_surah_cache


def load_surah_pericopes(surah: int, ayah_numbers: list) -> tuple:
    """Returns (pericopes_list, coverage_dict). Every pericope row carries the
    raw fields from surah_pericopes.jsonl (surah, pericope, ayah_from,
    ayah_to, label) plus a `synthesized` flag. Surahs absent from the index
    (351 rows / 79 surahs corpus-wide) are single-pericope by definition: a
    single synthesized row spanning the whole surah is emitted instead, with
    synthesized=True."""
    rows_by_surah = _load_all_pericope_rows()
    rows = rows_by_surah.get(surah)
    coverage = {"present": False, "synthesized": False, "source_file": relpath(PERICOPES_PATH) if PERICOPES_PATH.exists() else None}
    if rows:
        pericopes = [dict(r, synthesized=False) for r in rows]
        coverage.update({"present": True, "synthesized": False, "pericope_count": len(pericopes)})
        return pericopes, coverage

    if not ayah_numbers:
        coverage["note"] = "surah absent from pericope index and no ayah numbers known (cannot synthesize)"
        return [], coverage

    synthesized = [{
        "surah": surah,
        "pericope": 1,
        "ayah_from": min(ayah_numbers),
        "ayah_to": max(ayah_numbers),
        "label": "Whole surah",
        "synthesized": True,
    }]
    coverage.update({
        "present": True,
        "synthesized": True,
        "pericope_count": 1,
        "note": f"surah {surah} absent from surah_pericopes.jsonl; synthesized a single whole-surah pericope",
    })
    return synthesized, coverage


def pericope_for_ayah(pericopes: list, ayah: int) -> dict:
    for p in pericopes:
        if p["ayah_from"] <= ayah <= p["ayah_to"]:
            return p
    return None


# ---------------------------------------------------------------------------
# Source: Turkish dictionary entry + gloss (new)
# ---------------------------------------------------------------------------

_QAC_FURUQ_ROOT_MAP_CACHE: tuple[dict, dict] | None = None
_QAC_FURUQ_ROOT_MAP_ERROR: str | None = None


def load_qac_furuq_root_map() -> tuple[dict, dict]:
    """Returns (dominant_map, records_by_qac_root) from the authoritative
    QAC->Furuq root-map DB. dominant_map is {qac_root_norm: root_id}. Records
    include all split targets, so callers can include non-dominant roots in
    addition to the dominant dictionary/gloss entry."""
    global _QAC_FURUQ_ROOT_MAP_CACHE, _QAC_FURUQ_ROOT_MAP_ERROR
    if _QAC_FURUQ_ROOT_MAP_CACHE is not None:
        return _QAC_FURUQ_ROOT_MAP_CACHE
    if not QAC_FURUQ_ROOT_MAP_SQLITE_GZ.exists():
        _QAC_FURUQ_ROOT_MAP_CACHE = ({}, {})
        return _QAC_FURUQ_ROOT_MAP_CACHE

    tmp_path = None
    try:
        raw = read_gz_bytes(QAC_FURUQ_ROOT_MAP_SQLITE_GZ)
        with tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False) as tmp:
            tmp.write(raw)
            tmp_path = tmp.name

        conn = sqlite3.connect(tmp_path)
        conn.row_factory = sqlite3.Row
        records = {}
        for row in conn.execute(
            "SELECT qac_root_norm, qac_root_join_key, qac_total_occurrences, "
            "matched_occurrences, mapping_status, dominant_furuq_root_id, "
            "dominant_furuq_root_norm, dominant_resolution "
            "FROM qac_root_map"
        ):
            d = dict(row)
            d["targets"] = []
            records[d["qac_root_norm"]] = d
        for row in conn.execute(
            "SELECT qac_root_norm, target_rank, furuq_root_id, furuq_root_norm, "
            "furuq_resolution, occurrences, is_dominant "
            "FROM qac_furuq_targets ORDER BY qac_root_norm, target_rank"
        ):
            d = dict(row)
            if d.get("furuq_root_id"):
                records.setdefault(d["qac_root_norm"], {
                    "qac_root_norm": d["qac_root_norm"],
                    "mapping_status": "target_without_root_map_record",
                    "dominant_furuq_root_id": None,
                    "targets": [],
                })["targets"].append(d)
        conn.close()
    except Exception as exc:
        _QAC_FURUQ_ROOT_MAP_ERROR = f"{type(exc).__name__}: {exc}"
        print(
            f"WARNING: could not read QAC-Furuq root map at "
            f"{QAC_FURUQ_ROOT_MAP_SQLITE_GZ}; falling back to packet root IDs "
            f"where available ({_QAC_FURUQ_ROOT_MAP_ERROR}).",
            file=sys.stderr,
        )
        _QAC_FURUQ_ROOT_MAP_CACHE = ({}, {})
        return _QAC_FURUQ_ROOT_MAP_CACHE
    finally:
        if tmp_path:
            Path(tmp_path).unlink(missing_ok=True)

    dominant_map = {
        root: record["dominant_furuq_root_id"]
        for root, record in records.items()
        if record.get("dominant_furuq_root_id")
    }
    _QAC_FURUQ_ROOT_MAP_CACHE = (dominant_map, records)
    return _QAC_FURUQ_ROOT_MAP_CACHE


def load_packet_root_id_map(surah: int) -> tuple:
    """Fallback ({arabic_root_string: root_id}, packet_path or None) derived
    from full_context_packet.json branch inventories."""
    packet_path = V12_TR_DIR / f"s{surah:03d}" / "full_context_packet.json"
    if not packet_path.exists():
        return {}, None
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    root_id_map = {}
    for entry in packet.get("branch_inventories", []):
        root = entry.get("root")
        root_id = None
        for br in entry.get("branches", []):
            for v in br.get("variants", []) or []:
                if v.get("root_id"):
                    root_id = v["root_id"]
                    break
            if root_id:
                break
        if root and root_id:
            root_id_map[root] = root_id
    return root_id_map, packet_path


def load_root_id_map(surah: int) -> tuple:
    """Returns ({qac_root_norm: dominant_root_id}, source_path). The preferred
    source is qac-furuq-v4-root-map.sqlite.gz; full_context_packet.json remains
    a compatibility fallback."""
    root_id_map, _records = load_qac_furuq_root_map()
    if root_id_map:
        return root_id_map, QAC_FURUQ_ROOT_MAP_SQLITE_GZ
    return load_packet_root_id_map(surah)


# Concordance keys dropped from dictionary_entry.occurrence_evidence. These are
# a per-occurrence QAC concordance and character-span alignment table: raw
# morphology rows (qac_ref, surface_ar, morph_features, qac_char_span,
# attachment_unit_id) plus the flat ayah-ref list. They carry ZERO readings,
# branches or senses -- the lexical concept material lives in
# dictionary_entry.branches, which is kept in full. Dropping an index is not
# dropping a meaning, so the Layer-2 no-select rule (PRINCIPLES.md §3/§6) is
# not engaged; and inter_ayah_rows already carries cross-ayah relations for
# this ayah in reviewed, ordered form -- the same job a concordance would be
# used for, done better and already scoped.
# For root_000532 (ر ب ب) this is ~1,526 KB of a ~1,635 KB entry.
OCCURRENCE_EVIDENCE_DROPPED_KEYS = ("occurrences", "ayahs")


def _trim_occurrence_evidence(entry: dict) -> tuple:
    """Removes the bulk concordance lists from a dictionary entry (shallow
    copy; the source file is untouched). Returns (trimmed_entry, drop_record).
    `summary` and `forms` are KEPT: ~3 KB combined, carrying corpus frequency
    and the inflectional inventory, which are orienting facts a writer can
    use. drop_record makes the trim legible as a deliberate act."""
    if not entry:
        return entry, None
    oe = entry.get("occurrence_evidence")
    if not isinstance(oe, dict):
        return entry, None
    dropped = {}
    for key in OCCURRENCE_EVIDENCE_DROPPED_KEYS:
        value = oe.get(key)
        if value is not None:
            dropped[key] = len(value) if hasattr(value, "__len__") else 1
    if not dropped:
        return entry, None
    trimmed_oe = {k: v for k, v in oe.items()
                  if k not in OCCURRENCE_EVIDENCE_DROPPED_KEYS}
    new_entry = dict(entry)
    new_entry["occurrence_evidence"] = trimmed_oe
    return new_entry, {
        "dropped_keys": sorted(dropped),
        "dropped_row_counts": dropped,
        "kept_keys": sorted(trimmed_oe),
    }


def load_dictionary_entry(root_id: str) -> tuple:
    path = DICTIONARY_TR_DIR / f"{root_id}_entry.json"
    if not path.exists():
        return None, path
    return json.loads(path.read_text(encoding="utf-8")), path


def _mark_gloss_error(err: dict) -> None:
    """Adds a derived boolean to a gloss error object in place: True when the
    gloss narrows the root's concept (fit == 'narrowing') AND that narrowing
    actually drops facets (loses_facet_ids non-empty) -- i.e. this specific
    gloss text is materially incomplete about the root's core concept."""
    fit = err.get("fit")
    loses = err.get("loses_facet_ids") or []
    err["loses_core_concept"] = bool(fit == "narrowing" and loses)


def load_gloss_record(root_id: str) -> tuple:
    """Returns (gloss_json_or_None, path). The gloss json's error objects
    (branches[].concept_gloss.error, branches[].contextual_glosses[].error,
    branches[].lexical_glosses{}.error) are annotated in place with the
    derived `loses_core_concept` boolean described in _mark_gloss_error."""
    path = GLOSSES_TR_DIR / f"{root_id}.json"
    if not path.exists():
        return None, path
    data = json.loads(path.read_text(encoding="utf-8"))
    for br in data.get("branches", []) or []:
        cg = br.get("concept_gloss")
        if cg and cg.get("error"):
            _mark_gloss_error(cg["error"])
        for cx in br.get("contextual_glosses", []) or []:
            if cx.get("error"):
                _mark_gloss_error(cx["error"])
        for lu_id, lg in (br.get("lexical_glosses") or {}).items():
            if lg.get("error"):
                _mark_gloss_error(lg["error"])
    return data, path


def _root_targets(root_ar: str, root_id_map: dict, root_records: dict) -> tuple[list[dict], dict]:
    record = root_records.get(root_ar)
    if record:
        targets = [dict(t) for t in record.get("targets", []) if t.get("furuq_root_id")]
        if not targets and record.get("dominant_furuq_root_id"):
            targets = [{
                "target_rank": 1,
                "furuq_root_id": record["dominant_furuq_root_id"],
                "furuq_root_norm": record.get("dominant_furuq_root_norm"),
                "furuq_resolution": record.get("dominant_resolution"),
                "occurrences": record.get("matched_occurrences"),
                "is_dominant": 1,
            }]
        mapping = {
            "source": relpath(QAC_FURUQ_ROOT_MAP_SQLITE_GZ),
            "qac_root_norm": root_ar,
            "mapping_status": record.get("mapping_status"),
            "primary_root_id": record.get("dominant_furuq_root_id"),
            "targets": targets,
        }
        return targets, mapping

    root_id = root_id_map.get(root_ar)
    if not root_id:
        return [], {
            "source": relpath(QAC_FURUQ_ROOT_MAP_SQLITE_GZ)
            if QAC_FURUQ_ROOT_MAP_SQLITE_GZ.exists()
            else "full_context_packet.json fallback",
            "qac_root_norm": root_ar,
            "mapping_status": "unmapped",
            "primary_root_id": None,
            "targets": [],
        }
    target = {
        "target_rank": 1,
        "furuq_root_id": root_id,
        "furuq_root_norm": root_ar,
        "furuq_resolution": "packet_fallback",
        "occurrences": None,
        "is_dominant": 1,
    }
    return [target], {
        "source": "full_context_packet.json fallback",
        "qac_root_norm": root_ar,
        "mapping_status": "packet_fallback",
        "primary_root_id": root_id,
        "targets": [target],
    }


def build_root_lexicon(qac_rows: list, root_id_map: dict) -> tuple:
    """For each distinct root appearing in this ayah's QAC morphemes, joins
    the Turkish dictionary entry and gloss record. Split QAC->Furuq mappings
    include all mapped Furuq target roots, dominant and non-dominant. Returns
    (dict keyed by root_id, coverage_dict). Turkish is the only language with
    glosses currently sourced; that fact is recorded in coverage, not assumed."""
    roots_in_ayah = []
    seen = set()
    for row in qac_rows:
        root_ar = row.get("root_ar")
        if root_ar and root_ar not in seen:
            seen.add(root_ar)
            roots_in_ayah.append(root_ar)

    entries = {}
    per_root = {}
    _dominant_map, root_records = load_qac_furuq_root_map()
    split_roots = 0
    dictionary_branches_total = 0
    gloss_branches_total = 0
    emitted_root_ids = set()

    for root_ar in roots_in_ayah:
        targets, mapping = _root_targets(root_ar, root_id_map, root_records)
        if not targets:
            per_root[root_ar] = {
                "root_id": None,
                "root_ids": [],
                "root_mapping": mapping,
                "dictionary_present": False,
                "gloss_present": False,
                "note": "no root_id mapping found for this QAC root",
            }
            continue
        if mapping.get("mapping_status") == "split":
            split_roots += 1
        target_coverage = []
        for target in targets:
            root_id = target.get("furuq_root_id")
            if not root_id:
                continue
            mapping_role = "dominant" if target.get("is_dominant") else "non_dominant_split_target"
            dict_entry, dict_path = load_dictionary_entry(root_id)
            gloss_entry, gloss_path = load_gloss_record(root_id)
            dict_entry, drop_record = _trim_occurrence_evidence(dict_entry)
            dictionary_branch_count = len(dict_entry.get("branches", []) or []) if dict_entry else 0
            gloss_branch_count = len(gloss_entry.get("branches", []) or []) if gloss_entry else 0
            if root_id not in emitted_root_ids:
                dictionary_branches_total += dictionary_branch_count
                gloss_branches_total += gloss_branch_count
                emitted_root_ids.add(root_id)
                entries[root_id] = {
                    "root_ar": root_ar,
                    "qac_roots_ar": [root_ar],
                    "root_id": root_id,
                    "root_mapping_role": mapping_role,
                    "root_mapping_roles": [mapping_role],
                    "qac_root_mappings": [{
                        "root_ar": root_ar,
                        "root_mapping_role": mapping_role,
                        "target_rank": target.get("target_rank"),
                        "furuq_resolution": target.get("furuq_resolution"),
                        "occurrences": target.get("occurrences"),
                    }],
                    "dictionary_entry": dict_entry,
                    "dictionary_source_file": relpath(dict_path) if dict_entry is not None else None,
                    "gloss": gloss_entry,
                    "gloss_source_file": relpath(gloss_path) if gloss_entry is not None else None,
                }
            else:
                qac_roots = entries[root_id].setdefault("qac_roots_ar", [])
                if root_ar not in qac_roots:
                    qac_roots.append(root_ar)
                roles = entries[root_id].setdefault("root_mapping_roles", [])
                if mapping_role not in roles:
                    roles.append(mapping_role)
                mappings = entries[root_id].setdefault("qac_root_mappings", [])
                if not any(m.get("root_ar") == root_ar for m in mappings):
                    mappings.append({
                        "root_ar": root_ar,
                        "root_mapping_role": mapping_role,
                        "target_rank": target.get("target_rank"),
                        "furuq_resolution": target.get("furuq_resolution"),
                        "occurrences": target.get("occurrences"),
                    })
            note = None
            if dict_entry is None:
                note = "no Turkish dictionary entry found for this root_id"
            elif gloss_entry is None:
                note = "no reviewed Turkish gloss found for this root_id"
            target_coverage.append({
                "root_id": root_id,
                "target_rank": target.get("target_rank"),
                "is_dominant": bool(target.get("is_dominant")),
                "furuq_root_norm": target.get("furuq_root_norm"),
                "furuq_resolution": target.get("furuq_resolution"),
                "occurrences": target.get("occurrences"),
                "dictionary_present": dict_entry is not None,
                "gloss_present": gloss_entry is not None,
                "dictionary_branch_count": dictionary_branch_count,
                "gloss_branch_count": gloss_branch_count,
                "occurrence_evidence_trimmed": drop_record,
                "note": note,
            })
        per_root[root_ar] = {
            "root_id": mapping.get("primary_root_id"),
            "root_ids": [target["root_id"] for target in target_coverage],
            "root_mapping": mapping,
            "dictionary_present": any(target["dictionary_present"] for target in target_coverage),
            "gloss_present": any(target["gloss_present"] for target in target_coverage),
            "targets": target_coverage,
            "note": None,
        }

    coverage = {
        "present": bool(entries),
        "roots_in_ayah": roots_in_ayah,
        "per_root": per_root,
        "occurrence_evidence_trim": {
            "applied": True,
            "dropped_keys": list(OCCURRENCE_EVIDENCE_DROPPED_KEYS),
            "note": (
                "TRIMMED, NOT ABSENT. dictionary_entry.occurrence_evidence."
                "occurrences and .ayahs are removed from every root by design: "
                "they are a per-occurrence QAC concordance and character-span "
                "alignment table carrying zero readings, branches or senses, and "
                "they dominated bundle size (~1.5 MB for a single common root). "
                "occurrence_evidence.summary (corpus frequency) and .forms "
                "(inflectional inventory) are retained. Dictionary/gloss branches "
                "are kept in full for every included Furuq root target."
            ),
        },
        "branch_policy": {
            "mode": "full_branches_no_filtering",
            "dictionary_branches_total": dictionary_branches_total,
            "dictionary_branches_kept": dictionary_branches_total,
            "dictionary_branches_dropped": 0,
            "gloss_branches_total": gloss_branches_total,
            "note": (
                "No branch filtering is applied. Every branch present in each "
                "included dictionary/gloss root entry is kept."
            ),
        },
        "root_mapping": {
            "source": relpath(QAC_FURUQ_ROOT_MAP_SQLITE_GZ)
            if QAC_FURUQ_ROOT_MAP_SQLITE_GZ.exists()
            else "full_context_packet.json fallback",
            "policy": (
                "Use the dominant Furuq root for every QAC root, and include "
                "non-dominant Furuq targets as additional root_lexicon entries "
                "when qac-furuq-v4-root-map marks the QAC root as split."
            ),
            "split_roots_in_ayah": split_roots,
        },
        "note": "Turkish is the only language with dictionary entries/glosses currently sourced.",
    }
    return entries, coverage


# ---------------------------------------------------------------------------
# Preflight — enumerate every expected source, report all gaps, abort once
# ---------------------------------------------------------------------------

# --- word_analysis -> morpheme-span crosswalk -------------------------------
#
# `linguistic/morphemes.tsv` (present for all 114 surahs) is the deterministic
# crosswalk. word_analysis's "critical words" are orthographic/analytic units,
# NOT QAC words: for 100:1, وَ and ٱلْعَٰدِيَٰتِ are two critical words but ONE
# QAC word (100:1:1 = وَ + ٱلْ + عَٰدِيَٰتِ). So aligned_qac_word_ref is not off
# by one -- it is the wrong unit type, and no renumbering fixes it. A critical
# word maps to a MORPHEME SPAN.
#
# Ayah attribution comes from qac_ref in this dataset because morpheme_id-based
# ayah (a000) rows are preface markers that can carry surrogate qac_refs.
_MORPHEME_ID_RE = re.compile(r"^m-w-s(\d+)-a(\d+)-w(\d+)-(\d+)$")
_WA_ARABIC_RE = re.compile(r"\{\{ar:([^}]*)\}\}")
_MAX_SKIP_FOR_MORPHEME_MATCH = 3
# Quranic annotation letters + tatweel + superscript alef: present in one
# source's orthography and absent from the other's (e.g. word_analysis
# ضَبْحًۭا vs morphemes.tsv ضَبْحًا; morphemes.tsv هِۦ vs word_analysis هِ).
_ANNOTATION_CODEPOINTS = set(range(0x06D6, 0x06EE)) | {0x0670, 0x06E5, 0x06E6, 0x0640}
_ALEF_FOLD = str.maketrans({"ٱ": "ا", "أ": "ا", "إ": "ا", "آ": "ا", "ى": "ي"})


def normalize_arabic_surface(text: str) -> str:
    """Fold an Arabic surface to comparable letters: drop combining marks and
    Quranic annotation signs, fold alef variants. Used only for MATCHING; the
    original surfaces are never rewritten in the bundle."""
    if not text:
        return ""
    decomposed = unicodedata.normalize("NFD", text)
    stripped = "".join(
        c for c in decomposed
        if unicodedata.category(c) != "Mn" and ord(c) not in _ANNOTATION_CODEPOINTS
    )
    return stripped.translate(_ALEF_FOLD)


def normalize_basmala_surface(text: str) -> str:
    """Normalize Quran rows for S:0-to-1:1 surface equivalence only."""
    normalized = normalize_arabic_surface(text)
    return "".join(
        char
        for char in normalized
        if unicodedata.category(char) != "Cf" and not char.isspace()
    )


def _find_word_span_from_position(
    morpheme_rows: list[dict],
    position: int,
    target: str,
    max_skip: int = _MAX_SKIP_FOR_MORPHEME_MATCH,
) -> tuple[bool, int, int, int]:
    """Find a morpheme span that matches ``target`` from a position.

    Returns (matched, span_start, span_end, skipped_rows).
    """
    for skip in range(max_skip + 1):
        span_start = position + skip
        if span_start >= len(morpheme_rows):
            return False, position, position, 0
        if skip and _qac_word_ref_from_qac_ref(
            morpheme_rows[span_start - 1].get("qac_ref", "")
        ) == _qac_word_ref_from_qac_ref(
            morpheme_rows[span_start].get("qac_ref", "")
        ):
            continue
        accumulated = ""
        for j in range(span_start + 1, len(morpheme_rows) + 1):
            accumulated = "".join(
                normalize_arabic_surface(row["surface_ar"]) for row in morpheme_rows[span_start:j]
            )
            if accumulated == target:
                while (
                    j < len(morpheme_rows)
                    and not normalize_arabic_surface(morpheme_rows[j]["surface_ar"])
                    and _qac_word_ref_from_qac_ref(morpheme_rows[j - 1].get("qac_ref", ""))
                    == _qac_word_ref_from_qac_ref(morpheme_rows[j].get("qac_ref", ""))
                ):
                    j += 1
                return True, span_start, j, skip
            if not target.startswith(accumulated):
                break
    return False, position, position, 0


def _qac_word_ref_from_qac_ref(qac_ref: str) -> str:
    parts = qac_ref.split(":")
    return ":".join(parts[:3]) if len(parts) >= 3 else ""


def load_morphemes_tsv(surah: int) -> tuple:
    """Returns ({ayah_int: [morpheme_row, ...]}, coverage, path or None).
    Rows keep file order. Uses qac_ref-derived ayah attribution to avoid
    silently keying basmalah rows into surah-1 ayahs."""
    path = V12_TR_DIR / f"s{surah:03d}" / "linguistic" / "morphemes.tsv"
    coverage = {"present": False, "source_file": None}
    if not path.exists():
        coverage["note"] = f"morphemes.tsv not found at {path}"
        return {}, coverage, None

    by_ayah, malformed = {}, 0
    dropped_marker_rows = 0
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 5 or not parts[0].strip() or parts[0] == "morpheme_id":
                continue
            m = _MORPHEME_ID_RE.match(parts[0])
            if not m:
                malformed += 1
                continue
            is_marker = m.group(2) == "000"
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
                if is_marker:
                    dropped_marker_rows += 1
                continue
            if is_marker and ayah == 0:
                # standalone preface marker rows should remain unmapped in per-ayah mapping.
                dropped_marker_rows += 1
                continue
            by_ayah.setdefault(ayah, []).append({
                "morpheme_id": parts[0],
                "word_id": parts[1],
                "qac_ref": parts[2],
                "morpheme_index": parts[3],
                "surface_ar": parts[4],
                "root": parts[7] if len(parts) > 7 else "",
                "lemma_ar": parts[6] if len(parts) > 6 else "",
                "pos": parts[9] if len(parts) > 9 else "",
            })
    coverage.update({
        "present": bool(by_ayah),
        "source_file": relpath(path),
        "ayah_count": len(by_ayah),
        "row_count": sum(len(v) for v in by_ayah.values()),
        "malformed_rows": malformed,
        "note": (
            "ayah attribution taken from qac_ref, with non-surah rows and "
            "standalone basmala ayah marker rows (1:0) filtered out"
        ),
    })
    coverage["dropped_preface_rows"] = dropped_marker_rows
    if dropped_marker_rows:
        coverage["note"] += f" | dropped_preface_rows={dropped_marker_rows}"
    if not by_ayah:
        coverage["note"] = f"{path} present but no parseable morpheme rows"
    return by_ayah, coverage, path


def resolve_word_morpheme_spans(wa_record: dict, morpheme_rows: list) -> tuple:
    """Resolve unambiguous spans using the complete ayah's ordered surfaces.

    Returns (spans, unresolved). `spans` is a list parallel to
    wa_record['words']; each entry carries the resolved word_id(s) and the
    qac_ref of every morpheme spanned, or is None when unresolved.

    This ADDS a resolution; it never overwrites or deletes the upstream
    `aligned_qac_word_ref`, so the discrepancy stays inspectable
    (PRINCIPLES.md §11, and the basmalah no-hidden-renumbering rule)."""
    from word_morpheme_alignment import resolve
    return resolve(wa_record, morpheme_rows)


def build_word_qac_alignment(wa_record: dict, qac_rows: list) -> tuple:
    """Project the release's accepted many-to-many links, preserving analysis."""
    from _commentary.qac_analysis_bridge import get_bridge
    try:
        return get_bridge(QURAN_DATA.parent).align(wa_record, qac_rows)
    except (OSError, ValueError, sqlite3.Error, subprocess.SubprocessError) as exc:
        raise RequiredSourceMissing(f"Required word-analysis/QAC bridge: {exc}") from exc


def check_word_alignment(surah: int, word_analysis: dict, qac_by_ayah: dict,
                          target_ayahs: list) -> dict:
    """Cross-validates word_analysis[].aligned_qac_word_ref against the QAC word
    refs that actually exist for each ayah.

    This is a SOURCE-DATA defect detector, not a repair. word-analysis appears
    to treat orthographic words as QAC words: for 100:1 QAC has two words
    (`100:1:1` = وَ+ٱلْ+عَٰدِيَٰتِ, `100:1:2` = ضَبْحًا) while word-analysis emits
    three, so `100:1:3` dangles and any word-level join between word-analysis
    topics and QAC morphology silently fails to join.

    The alignment is deliberately NOT auto-repaired by renumbering: a hidden
    renumbering is precisely what the basmalah boundary rule in STATUS.md
    forbids, and guessing a mapping would fabricate the stable identities
    PRINCIPLES.md §11 requires. The defect is reported loudly and recorded in
    coverage so downstream consumers can refuse the join."""
    per_ayah = {}
    for a in target_ayahs:
        record = word_analysis.get(f"{surah}:{a}")
        if record is None:
            continue
        actual = {r.get("qac_word_ref") for r in qac_by_ayah.get(a, []) if r.get("qac_word_ref")}
        claimed = {w.get("aligned_qac_word_ref") for w in record.get("words", [])
                   if w.get("aligned_qac_word_ref")}
        dangling = sorted(claimed - actual)
        if dangling:
            per_ayah[f"{surah}:{a}"] = {
                "qac_word_count": len(actual),
                "word_analysis_word_count": len(claimed),
                "dangling_refs": dangling,
            }
    return {
        "consistent": not per_ayah,
        "ayahs_checked": len(target_ayahs),
        "ayahs_with_dangling_refs": len(per_ayah),
        "detail": per_ayah,
        "note": (
            "word_analysis[].aligned_qac_word_ref does not resolve against "
            "qac_morphemes.qac_word_ref for the listed ayahs; word-analysis "
            "appears to count orthographic words where QAC counts morphological "
            "words. Word-level joins between word_analysis topics and QAC "
            "morphology are UNRELIABLE for these ayahs. Upstream defect in "
            "quran-data's word-analysis; deliberately not auto-repaired here "
            "(renumbering would fabricate identities -- PRINCIPLES.md §11, "
            "STATUS.md basmalah boundary rule)."
        ) if per_ayah else "aligned_qac_word_ref resolves against QAC for all checked ayahs.",
    }


def _row(name, path, required, present, note=None):
    return {"name": name, "path": display_path(path), "required": required, "present": present, "note": note}


def print_preflight_table(surah: int, rows: list) -> None:
    print(f"\n=== Preflight source inventory: surah {surah} ===")
    name_w = max([len(r["name"]) for r in rows] + [6])
    header = f"{'SOURCE':<{name_w}}  {'REQ':<4} {'STATUS':<8} PATH"
    print(header)
    print("-" * min(len(header) + 40, 160))
    for r in rows:
        req = "yes" if r["required"] else "no"
        status = "OK" if r["present"] else "MISSING"
        print(f"{r['name']:<{name_w}}  {req:<4} {status:<8} {r['path']}")
        if r.get("note"):
            print(f"{'':<{name_w}}  {'':<4} {'':<8} note: {r['note']}")
    print()


def preflight(surah: int, ayah_filter: int = None,
              ayah_from: int = None, ayah_to: int = None) -> dict:
    """Enumerates every expected source for `surah` (or just `ayah_filter`'s
    per-ayah sources if given), prints a full present/missing table, and
    raises RequiredSourceMissing (after printing, listing every gap at once)
    if any REQUIRED source is missing. Required = Quran text, word analysis,
    QAC morphemes, branch inventories, and Hermetic Focus Trace responses unless
    --exclude-focus-trace is active. Everything else is optional. Returns the
    already-loaded data so main() doesn't have to reload it."""
    rows = []
    problems = []

    quran_text = None
    try:
        quran_text = load_quran_text(surah)
        rows.append(_row("Quran text", QURAN_TEXT_TSV, True, True, f"{len(quran_text)} rows"))
    except RequiredSourceMissing as exc:
        rows.append(_row("Quran text", QURAN_TEXT_TSV, True, False, str(exc)))
        problems.append(str(exc))

    word_analysis = None
    wa_path = WORD_ANALYSIS_DIR / f"s{surah:03d}.jsonl.zst"
    try:
        word_analysis = load_word_analysis(surah)
        rows.append(_row("Word analysis", wa_path, True, True, f"{len(word_analysis)} ayah records"))
    except RequiredSourceMissing as exc:
        rows.append(_row("Word analysis", wa_path, True, False, str(exc)))
        problems.append(str(exc))

    qac_by_ayah = None
    try:
        qac_by_ayah = load_qac_morphemes(surah)
        total_rows = sum(len(v) for v in qac_by_ayah.values())
        rows.append(_row("QAC morphemes", QAC_SQLITE_GZ, True, True, f"{total_rows} rows across {len(qac_by_ayah)} ayat"))
    except RequiredSourceMissing as exc:
        rows.append(_row("QAC morphemes", QAC_SQLITE_GZ, True, False, str(exc)))
        problems.append(str(exc))

    ayah_numbers = discover_ayah_numbers(surah, quran_text) if quran_text else []
    if ayah_filter is not None:
        target_ayahs = [ayah_filter]
    elif ayah_from is not None or ayah_to is not None:
        lo = ayah_from if ayah_from is not None else min(ayah_numbers)
        hi = ayah_to if ayah_to is not None else max(ayah_numbers)
        missing_bounds = [a for a in (lo, hi) if a not in ayah_numbers]
        if missing_bounds:
            raise RequiredSourceMissing(
                f"Span bound(s) outside surah {surah}: "
                f"{', '.join(str(a) for a in missing_bounds)}. "
                f"Valid ayah range is {min(ayah_numbers)}-{max(ayah_numbers)}"
            )
        target_ayahs = [a for a in ayah_numbers if lo <= a <= hi]
    else:
        target_ayahs = ayah_numbers
    if not target_ayahs:
        raise RequiredSourceMissing(
            f"No ayahs selected for surah {surah}"
            + (f" in span {ayah_from}-{ayah_to}" if ayah_from is not None or ayah_to is not None else "")
        )

    for a in target_ayahs:
        focus_dir = V12_TR_DIR / f"s{surah:03d}" / f"focus_{surah}_{a}"
        try:
            variants, cov = load_v12_branch_inventories(surah, a)
            scope = cov.get("scope", "focus")
            branch_path = (
                V12_TR_DIR / f"s{surah:03d}" / "full_context_packet.json"
                if scope.startswith("surah")
                else focus_dir
            )
            rows.append(_row(f"Branch inventories {surah}:{a}", branch_path, True, True, f"scope={scope}, variants={sorted(variants.keys())}"))
        except RequiredSourceMissing as exc:
            rows.append(_row(f"Branch inventories {surah}:{a}", focus_dir, True, False, str(exc)))
            problems.append(str(exc))

    root_id_map, packet_path = load_root_id_map(surah)
    packet_path_display = packet_path or QAC_FURUQ_ROOT_MAP_SQLITE_GZ
    rows.append(_row(
        "Root ID map (QAC-Furuq)", packet_path_display, False,
        bool(root_id_map),
        f"{len(root_id_map)} roots mapped" if root_id_map else "no root_id map available; dictionary/gloss join will be empty for this surah",
    ))

    bridge_path = QURAN_DATA / "bridges/qac-masaq.sqlite.gz"
    if word_analysis and qac_by_ayah:
        try:
            resolved = total = 0
            for a in target_ayahs:
                _spans, cov = build_word_qac_alignment(
                    word_analysis[f"{surah}:{a}"], qac_by_ayah.get(a, []))
                resolved += cov["words_resolved"]
                total += cov["words_total"]
            rows.append(_row("Word-analysis/QAC bridge", bridge_path, True, True,
                             f"{resolved}/{total} accepted analysis mappings; "
                             "any excluded source entries remain explicitly qualified"))
        except RequiredSourceMissing as exc:
            rows.append(_row("Word-analysis/QAC bridge", bridge_path, True, False, str(exc)))
            problems.append(str(exc))

    review_path = NETWORK_V3_DIR / f"s{surah:03d}" / "review" / "reader_a_pilot.md"
    rows.append(_row("Channel review", review_path, False, review_path.exists(),
                      None if review_path.exists() else "no first-pass channel review for this surah"))

    channel_outputs, cgo_cov = load_channel_generated_outputs(surah)
    rows.append(_row(
        "Channel generated outputs",
        NETWORK_V3_DIR / f"s{surah:03d}",
        False,
        cgo_cov.get("present", False),
        (
            f"{cgo_cov.get('file_count', 0)} files available; external manifest only"
            if cgo_cov.get("present")
            else cgo_cov.get("note")
        ),
    ))

    control_dir = V12_TR_DIR / f"s{surah:03d}" / "full_context_control"
    _, bu_cov, bu_path = load_butuncul_okuma(surah)
    rows.append(_row("Whole-surah reading (butuncul-okuma)", bu_path or control_dir, False,
                      bu_cov.get("present", False), bu_cov.get("note")))

    wide_control_dir = V12_TR_11AYAH_DIR / f"s{surah:03d}" / "full_context_control"
    wide_walks, wide_cov = load_v12_reader_walks(
        surah, target_ayahs[0] if len(target_ayahs) == 1 else ayah_numbers[0],
        V12_TR_11AYAH_DIR,
        "v12 plus/minus-5 reader walks",
    )
    rows.append(_row("Reader walks (+/-5 context)", wide_control_dir, False,
                      wide_cov.get("present", False), wide_cov.get("note")))

    if INCLUDE_HERMETIC_FOCUS_TRACE:
        focus_trace_dirs = focus_trace_run_dirs(surah)
        ft_packets = sum(
            1
            for a in target_ayahs
            for path in focus_trace_packet_paths(surah, a)
            if path.exists()
        )
        ft_response_files = sum(len(focus_trace_response_files(surah, a)) for a in target_ayahs)
        ft_usable_readers = 0
        ft_coverage_by_ayah = {}
        for a in target_ayahs:
            _trace, coverage = load_v12_focus_trace_hermetic(surah, a)
            ft_coverage_by_ayah[a] = coverage
            ft_usable_readers += int(coverage.get("reader_count", 0) or 0)
        ft_all_targets_usable = all(c.get("present") for c in ft_coverage_by_ayah.values())
        rows.append(_row(
            "Hermetic Focus Trace",
            focus_trace_dirs[0],
            REQUIRE_HERMETIC_FOCUS_TRACE,
            ft_all_targets_usable,
            (
                f"{ft_packets} packet(s), {ft_response_files} response file(s), "
                f"{ft_usable_readers} usable reader(s)"
                f", all targets usable={ft_all_targets_usable}"
                + (f", variant={FOCUS_TRACE_VARIANT}" if FOCUS_TRACE_VARIANT else "")
                + f"; checked dirs: {', '.join(display_path(path) for path in focus_trace_dirs)}"
            ),
        ))
        if REQUIRE_HERMETIC_FOCUS_TRACE:
            for a, coverage in ft_coverage_by_ayah.items():
                if not coverage.get("present"):
                    problems.append(
                        f"Hermetic Focus Trace usable reader response missing "
                        f"for {surah}:{a}: {coverage.get('note') or coverage.get('readers')}. "
                        f"Checked: {', '.join(coverage.get('run_dirs_checked', []))}"
                    )
        elif any(not c.get("present") for c in ft_coverage_by_ayah.values()):
            absent = sorted(
                a for a, c in ft_coverage_by_ayah.items() if not c.get("present")
            )
            print(
                f"WARNING: Hermetic Focus Trace missing for {len(absent)} of "
                f"{len(ft_coverage_by_ayah)} target ayahs "
                f"({', '.join(f'{surah}:{a}' for a in absent[:8])}"
                f"{', ...' if len(absent) > 8 else ''}). "
                f"Those bundles will reach Layer 2 without latent activation "
                f"material.",
                file=sys.stderr,
            )

    cross_path = V12_CROSS_RUN_TR_DIR / f"{surah}_ayah_findings_publication.json"
    rows.append(_row("V12 cross-run publication", cross_path, False, cross_path.exists(),
                      None if cross_path.exists() else "no final cross-run publication file for this surah"))

    pericopes, pc_cov = load_surah_pericopes(surah, ayah_numbers)
    rows.append(_row("Pericopes", PERICOPES_PATH, False, pc_cov.get("present", False),
                      pc_cov.get("note") or f"{pc_cov.get('pericope_count', 0)} pericope(s), synthesized={pc_cov.get('synthesized')}"))

    for a in target_ayahs:
        p = INTER_AYAH_DIR / f"focus_{surah}_{a}_cutoff_100.tsv"
        rows.append(_row(f"Inter-ayah rows {surah}:{a}", p, False, p.exists(),
                          None if p.exists() else "no inter-ayah file for this ayah"))

    if qac_by_ayah and root_id_map:
        _dominant_map, root_records = load_qac_furuq_root_map()
        seen_roots = {}
        for a in target_ayahs:
            for qrow in qac_by_ayah.get(a, []):
                root_ar = qrow.get("root_ar")
                if not root_ar:
                    continue
                targets, _mapping = _root_targets(root_ar, root_id_map, root_records)
                for target in targets:
                    root_id = target.get("furuq_root_id")
                    if not root_id:
                        continue
                    seen_roots.setdefault(root_id, {
                        "root_ar": root_ar,
                        "ayahs": [],
                        "is_dominant": bool(target.get("is_dominant")),
                    })["ayahs"].append(a)
        for root_id, info in sorted(seen_roots.items()):
            dpath = DICTIONARY_TR_DIR / f"{root_id}_entry.json"
            gpath = GLOSSES_TR_DIR / f"{root_id}.json"
            role = "dominant" if info.get("is_dominant") else "split target"
            ayahs_note = f"{role}; used in ayahs {sorted(set(info['ayahs']))}"
            rows.append(_row(f"Dictionary entry {root_id} ({info['root_ar']})", dpath, False, dpath.exists(), ayahs_note if not dpath.exists() else None))
            rows.append(_row(f"Gloss {root_id} ({info['root_ar']})", gpath, False, gpath.exists(),
                              "no reviewed gloss for this root" if not gpath.exists() else None))

    print_preflight_table(surah, rows)

    alignment = {"consistent": True, "ayahs_with_dangling_refs": 0, "detail": {}}
    if word_analysis and qac_by_ayah:
        alignment = check_word_alignment(surah, word_analysis, qac_by_ayah, target_ayahs)
        if not alignment["consistent"]:
            print(
                f"NOTE: legacy analysis/QAC numbering differs in "
                f"{alignment['ayahs_with_dangling_refs']} of {alignment['ayahs_checked']} "
                f"ayah(s) for surah {surah}. The accepted bridge supplies exact "
                f"morpheme links in word_morpheme_spans; legacy numbers are preserved "
                f"as source observations.",
                file=sys.stderr,
            )
            for ref, d in list(alignment["detail"].items())[:12]:
                print(
                    f"    {ref}: word_analysis claims {d['word_analysis_word_count']} "
                    f"word(s), QAC has {d['qac_word_count']}; dangling: "
                    f"{', '.join(d['dangling_refs'])}",
                    file=sys.stderr,
                )

    if problems:
        raise RequiredSourceMissing(
            "Preflight found required-source gaps (see table above):\n" +
            "\n".join(f"  - {p}" for p in problems)
        )

    return {
        "quran_text": quran_text,
        "word_analysis": word_analysis,
        "qac_by_ayah": qac_by_ayah,
        "root_id_map": root_id_map,
        "pericopes": pericopes,
        "alignment": alignment,
    }


def preflight_basmala(surah: int) -> dict:
    """Load the target surface and the canonical 1:1 linguistic evidence.

    A prefatory basmala is not a numbered ayah and therefore must not enter the
    normal per-ayah HFT/inter-ayah completeness checks. Its morphology and word
    analysis are the canonical 1:1 records, while surah-conditioned reader
    evidence is loaded later from the target surah.
    """
    if surah in BASMALA_EXCLUDED_SURAHS:
        reason = "S1 already numbers the basmala as 1:1" if surah == 1 else "S9 has no prefatory basmala"
        raise RequiredSourceMissing(f"Cannot build {surah}:0: {reason}")
    if not 2 <= surah <= 114:
        raise RequiredSourceMissing(f"Surah out of range for prefatory basmala: {surah}")

    rows: list[dict] = []
    problems: list[str] = []
    target_quran_text = load_quran_text(surah)
    target_ref = f"{surah}:0"
    if target_ref not in target_quran_text:
        problems.append(f"Quran text missing prefatory basmala row {target_ref}")
    rows.append(_row(
        f"Basmala surface {target_ref}",
        QURAN_TEXT_TSV,
        True,
        target_ref in target_quran_text,
        None if target_ref in target_quran_text else problems[-1],
    ))

    source_quran_text = load_quran_text(1)
    source_word_analysis = load_word_analysis(1)
    source_qac_by_ayah = load_qac_morphemes(1)
    source_root_id_map, source_root_map_path = load_root_id_map(1)
    source_alignment = check_word_alignment(
        1, source_word_analysis, source_qac_by_ayah, [1]
    )

    source_record = source_word_analysis.get(BASMALA_LINGUISTIC_SOURCE_REF)
    source_qac = source_qac_by_ayah.get(1)
    for label, present, note in (
        ("Canonical 1:1 Quran text", BASMALA_LINGUISTIC_SOURCE_REF in source_quran_text, None),
        ("Canonical 1:1 word analysis", source_record is not None, None),
        ("Canonical 1:1 QAC morphemes", bool(source_qac), None),
    ):
        rows.append(_row(label, QURAN_TEXT_TSV, True, present, note))
        if not present:
            problems.append(f"{label} is missing")

    try:
        branch_inventories, branch_coverage = load_v12_branch_inventories(
            1, 1, source_qac or [], []
        )
        rows.append(_row(
            "Canonical 1:1 branch inventories",
            V12_TR_DIR / "s001",
            True,
            bool(branch_inventories),
            f"scope={branch_coverage.get('scope')}",
        ))
    except RequiredSourceMissing as exc:
        rows.append(_row(
            "Canonical 1:1 branch inventories", V12_TR_DIR / "s001", True, False, str(exc)
        ))
        problems.append(str(exc))

    rows.append(_row(
        "Canonical 1:1 root ID map",
        source_root_map_path or QAC_FURUQ_ROOT_MAP_SQLITE_GZ,
        False,
        bool(source_root_id_map),
        f"{len(source_root_id_map)} roots mapped" if source_root_id_map else None,
    ))
    rows.append(_row(
        f"Hermetic Focus Trace {target_ref}",
        focus_trace_run_dirs(surah)[0],
        False,
        False,
        "not applicable to a prefatory basmala unit",
    ))
    rows.append(_row(
        f"Inter-ayah rows {target_ref}",
        INTER_AYAH_DIR / f"focus_{surah}_0_cutoff_100.tsv",
        False,
        False,
        "not applicable to a prefatory basmala unit",
    ))
    print_preflight_table(surah, rows)

    if problems:
        raise RequiredSourceMissing(
            "Basmala preflight found required-source gaps (see table above):\n"
            + "\n".join(f"  - {problem}" for problem in problems)
        )
    return {
        "target_quran_text": target_quran_text,
        "source_quran_text": source_quran_text,
        "source_word_analysis": source_word_analysis,
        "source_qac_by_ayah": source_qac_by_ayah,
        "source_root_id_map": source_root_id_map,
        "source_alignment": source_alignment,
    }


# ---------------------------------------------------------------------------
# Bundle assembly
# ---------------------------------------------------------------------------

def build_ayah_bundle(surah: int, ayah: int, quran_text: dict, word_analysis: dict,
                       qac_by_ayah: dict, root_id_map: dict, pericopes: list,
                       alignment: dict = None) -> dict:
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

    word_spans, span_coverage = build_word_qac_alignment(
        wa_record, qac_by_ayah.get(ayah, []))
    span_unresolved = span_coverage["unresolved"]
    if span_unresolved:
        print(
            f"WARNING: {ayah_ref}: {len(span_unresolved)} of "
            f"{len(wa_record.get('words', []) or [])} analysis entries are excluded "
            f"from accepted bridge links by the source review "
            f"(see coverage.word_morpheme_spans.unresolved).",
            file=sys.stderr,
        )
    coverage["word_morpheme_spans"] = span_coverage

    # Cross-layer identity check: does this ayah's word-analysis actually align
    # to QAC words? Recorded per ayah so a consumer can refuse the join rather
    # than joining on refs that do not resolve.
    this_ayah_alignment = (alignment or {}).get("detail", {}).get(ayah_ref)
    coverage["word_analysis_qac_alignment"] = {
        "consistent": this_ayah_alignment is None,
        "detail": this_ayah_alignment,
        "note": (
            "Legacy analysis refs happen to use existing QAC word numbers; "
            "use accepted word_morpheme_spans for actual joins."
            if this_ayah_alignment is None else
            "Legacy analysis numbering differs from QAC word numbering. "
            "Accepted word_morpheme_spans supply the actual many-to-many joins; "
            "source analysis identities remain unchanged."
        ),
    }

    qac_rows = qac_by_ayah.get(ayah)
    if not qac_rows:
        raise RequiredSourceMissing(f"QAC morphemes missing for {ayah_ref}")
    coverage["qac_morphemes"] = {"present": True, "row_count": len(qac_rows)}

    # Channel material is resolved BEFORE branch inventories because the
    # surah-fallback inventory is scoped against the subchannels anchored here
    # (rule (b) in scope_branch_inventories_to_ayah).
    channel_review, ch_coverage, ch_path = load_channel_review(surah)
    channel_blocks = channel_blocks_for_ayah(channel_review, ayah_ref)
    channel_generated_outputs, cgo_coverage = load_channel_generated_outputs(surah)
    coverage["channel_review"] = {
        **ch_coverage,
        "source_file": relpath(ch_path) if ch_path else None,
        "subchannels_anchored_here": len(channel_blocks),
    }
    coverage["channel_generated_outputs"] = cgo_coverage

    branch_inventories, bi_coverage = load_v12_branch_inventories(
        surah, ayah, qac_rows, channel_blocks
    )
    coverage["branch_inventories"] = bi_coverage

    # --- source families below are optional except HFT, which is required
    # by default and can only be skipped with --exclude-focus-trace. ---
    reader_responses, rr_coverage = load_v12_reader_responses(surah, ayah)
    coverage["v12_reader_responses"] = rr_coverage

    focus_trace_hermetic, ft_coverage = load_v12_focus_trace_hermetic(surah, ayah)
    coverage["v12_focus_trace_hermetic"] = ft_coverage

    reader_walks, walk_coverage = load_v12_reader_walks(surah, ayah)
    coverage["v12_reader_walks"] = walk_coverage

    reader_walks_wide, walk_wide_coverage = load_v12_reader_walks(
        surah, ayah, V12_TR_11AYAH_DIR, "v12 plus/minus-5 reader walks"
    )
    coverage["v12_reader_walks_wide"] = walk_wide_coverage

    cross_run_publication, cross_run_coverage = load_v12_cross_run_publication(surah, ayah)
    coverage["v12_cross_run_publication"] = cross_run_coverage

    butuncul_all, butuncul_cov, butuncul_path = load_butuncul_okuma(surah)
    butuncul_line = butuncul_all.get(ayah_ref)
    if butuncul_line is not None:
        note = None
    elif butuncul_path is None:
        note = "no whole-surah reading file exists for this surah"
    elif not butuncul_all:
        # File(s) found for the surah but zero ayah lines parsed at all --
        # distinct from "this particular ayah has no line in an otherwise
        # normal file". See load_butuncul_okuma's coverage['note'] for detail.
        note = (
            "whole-surah reading file(s) found for this surah but zero ayah "
            "lines were parsed from any of them (unrecognised format) -- this "
            "is NOT the same as this ayah being absent from a working file"
        )
    else:
        note = "no line for this ayah found in whole-surah reading"
    coverage["butuncul_okuma"] = {
        "present": butuncul_line is not None,
        "source_file": relpath(butuncul_path) if butuncul_path else None,
        "note": note,
    }

    inter_ayah_rows, ia_coverage = load_inter_ayah_rows(surah, ayah)
    coverage["inter_ayah"] = ia_coverage

    pericope = pericope_for_ayah(pericopes, ayah)
    coverage["pericope"] = {
        "present": pericope is not None,
        "synthesized": pericope.get("synthesized") if pericope else None,
        "note": None if pericope is not None else "no pericope span covers this ayah (data gap)",
    }

    root_lexicon, rl_coverage = build_root_lexicon(qac_rows, root_id_map)
    coverage["root_lexicon"] = rl_coverage

    bundle = {
        "bundle_type": "ayah",
        "schema_version": BUNDLE_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "unit_kind": "numbered_ayah",
        "surah": surah,
        "ayah": ayah,
        "ayahRef": ayah_ref,
        "surface_ref": ayah_ref,
        "linguistic_source_ref": ayah_ref,
        "text": {
            "arabic_uthmani": quran_text[ayah_ref],
            "source": relpath(QURAN_TEXT_TSV),
        },
        "qac_morphemes": qac_rows,
        "word_analysis": wa_record,
        "word_morpheme_spans": word_spans,
        "branch_inventories": branch_inventories,
        "v12_reader_responses": reader_responses,
        "v12_focus_trace_hermetic": focus_trace_hermetic,
        "v12_reader_walks": reader_walks,
        "v12_reader_walks_wide": reader_walks_wide,
        "v12_cross_run_publication": cross_run_publication,
        "butuncul_okuma_line": butuncul_line,
        "inter_ayah_rows": inter_ayah_rows,
        "channel_subchannels_anchored_here": channel_blocks,
        "channel_generated_outputs": channel_generated_outputs,
        "pericope": pericope,
        "root_lexicon": root_lexicon,
        "coverage": coverage,
    }
    return bundle


def build_basmala_bundle(
    surah: int,
    target_quran_text: dict,
    source_quran_text: dict,
    source_word_analysis: dict,
    source_qac_by_ayah: dict,
    source_root_id_map: dict,
    source_alignment: dict | None = None,
) -> dict:
    """Build a prefatory S:0 unit without fabricating S:0 linguistic refs."""
    if surah in BASMALA_EXCLUDED_SURAHS:
        reason = "S1 already numbers the basmala as 1:1" if surah == 1 else "S9 has no prefatory basmala"
        raise RequiredSourceMissing(f"Cannot build {surah}:0: {reason}")
    target_ref = f"{surah}:0"
    target_surface = target_quran_text.get(target_ref)
    source_surface = source_quran_text.get(BASMALA_LINGUISTIC_SOURCE_REF)
    if target_surface is None:
        raise RequiredSourceMissing(f"Quran text missing for {target_ref}")
    if source_surface is None:
        raise RequiredSourceMissing(
            f"Quran text missing canonical basmala source {BASMALA_LINGUISTIC_SOURCE_REF}"
        )
    target_normalized = normalize_basmala_surface(target_surface)
    source_normalized = normalize_basmala_surface(source_surface)
    if not target_normalized or target_normalized != source_normalized:
        raise RequiredSourceMissing(
            f"Normalized basmala surface mismatch: {target_ref} != "
            f"{BASMALA_LINGUISTIC_SOURCE_REF}"
        )

    wa_record = source_word_analysis.get(BASMALA_LINGUISTIC_SOURCE_REF)
    qac_rows = source_qac_by_ayah.get(1)
    if wa_record is None:
        raise RequiredSourceMissing(
            f"word-analysis record missing for {BASMALA_LINGUISTIC_SOURCE_REF}"
        )
    if not qac_rows:
        raise RequiredSourceMissing(
            f"QAC morphemes missing for {BASMALA_LINGUISTIC_SOURCE_REF}"
        )

    word_spans, span_coverage = build_word_qac_alignment(wa_record, qac_rows)
    branch_inventories, branch_coverage = load_v12_branch_inventories(
        1, 1, qac_rows, []
    )
    root_lexicon, root_coverage = build_root_lexicon(
        qac_rows, source_root_id_map
    )
    alignment_detail = (source_alignment or {}).get("detail", {}).get(
        BASMALA_LINGUISTIC_SOURCE_REF
    )

    reader_responses, reader_response_coverage = load_v12_reader_responses(surah, 0)
    reader_walks, reader_walk_coverage = load_v12_reader_walks(surah, 0)
    reader_walks_wide, reader_walk_wide_coverage = load_v12_reader_walks(
        surah, 0, V12_TR_11AYAH_DIR, "v12 plus/minus-5 reader walks"
    )
    cross_run_publication, cross_run_coverage = load_v12_cross_run_publication(
        surah, 0
    )
    butuncul_all, butuncul_coverage, butuncul_path = load_butuncul_okuma(surah)
    butuncul_line = butuncul_all.get(target_ref)
    channel_review, channel_coverage, channel_path = load_channel_review(surah)
    channel_blocks = channel_blocks_for_ayah(channel_review, target_ref)
    channel_outputs, channel_outputs_coverage = load_channel_generated_outputs(surah)

    coverage = {
        "quran_text": {"present": True, "surface_ref": target_ref},
        "word_analysis": {
            "present": True,
            "word_count": len(wa_record.get("words", [])),
            "linguistic_source_ref": BASMALA_LINGUISTIC_SOURCE_REF,
        },
        "word_morpheme_spans": span_coverage,
        "word_analysis_qac_alignment": {
            "consistent": alignment_detail is None,
            "detail": alignment_detail,
            "linguistic_source_ref": BASMALA_LINGUISTIC_SOURCE_REF,
            "note": (
                "Canonical 1:1 word-analysis/QAC alignment is preserved "
                "without renumbering."
            ),
        },
        "qac_morphemes": {
            "present": True,
            "row_count": len(qac_rows),
            "linguistic_source_ref": BASMALA_LINGUISTIC_SOURCE_REF,
        },
        "branch_inventories": {
            **branch_coverage,
            "linguistic_source_ref": BASMALA_LINGUISTIC_SOURCE_REF,
        },
        "root_lexicon": {
            **root_coverage,
            "linguistic_source_ref": BASMALA_LINGUISTIC_SOURCE_REF,
        },
        "v12_reader_responses": reader_response_coverage,
        "v12_focus_trace_hermetic": {
            "present": False,
            "packet_present": False,
            "readers": {},
            "excluded": False,
            "status": "not_applicable",
            "note": "prefatory basmala units have no native HFT focus run",
        },
        "v12_reader_walks": reader_walk_coverage,
        "v12_reader_walks_wide": reader_walk_wide_coverage,
        "v12_cross_run_publication": cross_run_coverage,
        "butuncul_okuma": {
            **butuncul_coverage,
            "present": butuncul_line is not None,
            "source_file": relpath(butuncul_path) if butuncul_path else None,
            "note": (
                None
                if butuncul_line is not None
                else "no prefatory basmala line in the target whole-surah reading"
            ),
        },
        "inter_ayah": {
            "present": False,
            "status": "not_applicable",
            "row_count": 0,
            "label_counts": {},
            "note": "inter-ayah completeness is defined on numbered ayahs only",
        },
        "channel_review": {
            **channel_coverage,
            "source_file": relpath(channel_path) if channel_path else None,
            "subchannels_anchored_here": len(channel_blocks),
        },
        "channel_generated_outputs": channel_outputs_coverage,
        "pericope": {
            "present": False,
            "synthesized": None,
            "status": "not_applicable",
            "note": "pericope intervals are defined on numbered ayahs only",
        },
        "basmala_alias": {
            "present": True,
            "surface_ref": target_ref,
            "linguistic_source_ref": BASMALA_LINGUISTIC_SOURCE_REF,
            "normalized_surface_equivalent": True,
            "target_normalized": target_normalized,
            "source_normalized": source_normalized,
        },
    }

    bundle = {
        "bundle_type": "ayah",
        "schema_version": BUNDLE_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "unit_kind": "prefatory_basmala",
        "surah": surah,
        "ayah": 0,
        "ayahRef": target_ref,
        "surface_ref": target_ref,
        "linguistic_source_ref": BASMALA_LINGUISTIC_SOURCE_REF,
        "text": {
            "arabic_uthmani": target_surface,
            "source": relpath(QURAN_TEXT_TSV),
        },
        "qac_morphemes": qac_rows,
        "word_analysis": wa_record,
        "word_morpheme_spans": word_spans,
        "branch_inventories": branch_inventories,
        "v12_reader_responses": reader_responses,
        "v12_focus_trace_hermetic": {},
        "v12_reader_walks": reader_walks,
        "v12_reader_walks_wide": reader_walks_wide,
        "v12_cross_run_publication": cross_run_publication,
        "butuncul_okuma_line": butuncul_line,
        "inter_ayah_rows": [],
        "channel_subchannels_anchored_here": channel_blocks,
        "channel_generated_outputs": channel_outputs,
        "pericope": None,
        "root_lexicon": root_lexicon,
        "coverage": coverage,
    }
    return bundle


def build_surah_bundle(
    surah: int,
    ayah_bundles: list,
    ayah_bundle_filenames: list,
    pericopes: list,
    bundle_unit_refs: list[str] | None = None,
    bundle_unit_files: list[str] | None = None,
) -> dict:
    quran_text = load_quran_text(surah)  # includes S:0 basmalah row if present
    butuncul_all, butuncul_cov, butuncul_path = load_butuncul_okuma(surah)
    channel_review, ch_coverage, ch_path = load_channel_review(surah)
    channel_generated_outputs, cgo_coverage = load_channel_generated_outputs(surah)

    coverage = {
        "ayah_count": len(ayah_bundles),
        "per_ayah": {b["ayahRef"]: b["coverage"] for b in ayah_bundles},
        "butuncul_okuma": {
            "present": butuncul_cov.get("present", False),
            "source_file": relpath(butuncul_path) if butuncul_path else None,
            "ayah_refs_found": sorted(butuncul_all.keys()),
        },
        "channel_review": {
            **ch_coverage,
            "source_file": relpath(ch_path) if ch_path else None,
        },
        "channel_generated_outputs": cgo_coverage,
        "pericopes": {
            "present": bool(pericopes),
            "pericope_count": len(pericopes),
            "synthesized": any(p.get("synthesized") for p in pericopes),
        },
    }

    surah_bundle = {
        "bundle_type": "surah",
        "schema_version": SURAH_BUNDLE_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "surah": surah,
        "ayah_refs": [b["ayahRef"] for b in ayah_bundles],
        "ayah_bundle_files": ayah_bundle_filenames,
        "bundle_unit_refs": (
            bundle_unit_refs
            if bundle_unit_refs is not None
            else [b["ayahRef"] for b in ayah_bundles]
        ),
        "bundle_unit_files": (
            bundle_unit_files
            if bundle_unit_files is not None
            else ayah_bundle_filenames
        ),
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
            "channel_generated_outputs": channel_generated_outputs,
            "pericopes": pericopes,
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


def discover_bundle_unit_numbers(surah: int, quran_text: dict) -> list:
    """Return ordered bundle units without changing numbered-ayah discovery."""
    numbered = discover_ayah_numbers(surah, quran_text)
    if surah in BASMALA_EXCLUDED_SURAHS:
        return numbered
    basmala_ref = f"{surah}:0"
    if basmala_ref not in quran_text:
        raise RequiredSourceMissing(
            f"Expected prefatory basmala surface is missing: {basmala_ref}"
        )
    return [0, *numbered]


def main() -> int:
    global INCLUDE_HERMETIC_FOCUS_TRACE, REQUIRE_HERMETIC_FOCUS_TRACE, FOCUS_TRACE_VARIANT

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--ayah", type=int, default=None)
    parser.add_argument("--ayah-from", type=int, default=None)
    parser.add_argument("--ayah-to", type=int, default=None)
    parser.add_argument("--pericope", type=int, default=None)
    parser.add_argument("--pericope-label", default=None)
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument(
        "--include-focus-trace",
        action="store_true",
        help=(
            "deprecated no-op: Hermetic Focus Trace is included and required "
            "by default"
        ),
    )
    parser.add_argument(
        "--require-focus-trace",
        action="store_true",
        help=(
            "deprecated no-op: Hermetic Focus Trace is required by default"
        ),
    )
    parser.add_argument(
        "--exclude-focus-trace",
        action="store_true",
        help=(
            "explicitly build without Hermetic Focus Trace; coverage records "
            "the exclusion so absence cannot be mistaken for a lookup miss"
        ),
    )
    parser.add_argument(
        "--allow-missing-focus-trace",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--focus-trace-variant",
        default=None,
        help=(
            "select one Hermetic Focus Trace filename variant, e.g. 'default', "
            "'5.5-high', or '5.6-sol-high'. By default all variants are included."
        ),
    )
    args = parser.parse_args()
    if args.ayah is not None and args.ayah < 0:
        parser.error("--ayah must be >= 0")
    if args.ayah is not None and (args.ayah_from is not None or args.ayah_to is not None):
        parser.error("--ayah cannot be combined with --ayah-from/--ayah-to")
    if (args.ayah_from is None) != (args.ayah_to is None):
        parser.error("--ayah-from and --ayah-to must be passed together")
    if args.ayah_from is not None and args.ayah_from > args.ayah_to:
        parser.error("--ayah-from must be <= --ayah-to")
    if args.ayah_from is not None and (args.ayah_from <= 0 or args.ayah_to <= 0):
        parser.error("--ayah-from/--ayah-to spans must contain numbered ayahs only")
    if args.pericope is not None and args.ayah_from is None:
        parser.error("--pericope requires --ayah-from/--ayah-to")
    if args.pericope_label is not None and args.ayah_from is None:
        parser.error("--pericope-label requires --ayah-from/--ayah-to")
    if args.allow_missing_focus_trace:
        parser.error(
            "--allow-missing-focus-trace was removed; use "
            "--exclude-focus-trace only for an intentional no-HFT build"
        )
    if args.exclude_focus_trace and args.focus_trace_variant is not None:
        parser.error("--focus-trace-variant cannot be combined with --exclude-focus-trace")

    INCLUDE_HERMETIC_FOCUS_TRACE = not args.exclude_focus_trace
    REQUIRE_HERMETIC_FOCUS_TRACE = not args.exclude_focus_trace
    FOCUS_TRACE_VARIANT = args.focus_trace_variant

    surah = args.surah
    out_dir = args.out or (PROSE_GEN_ROOT / "bundles" / f"s{surah:03d}")
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.ayah == 0:
        loaded = preflight_basmala(surah)
        bundle = build_basmala_bundle(surah, **loaded)
        out_path = out_dir / f"{surah}_0.ayah.json"
        out_path.write_text(compact_json_text(bundle), encoding="utf-8")
        print(f"wrote {out_path}")
        return 0

    loaded = preflight(surah, args.ayah, args.ayah_from, args.ayah_to)
    quran_text = loaded["quran_text"]
    word_analysis = loaded["word_analysis"]
    qac_by_ayah = loaded["qac_by_ayah"]
    root_id_map = loaded["root_id_map"]
    pericopes = loaded["pericopes"]
    alignment = loaded.get("alignment")
    if args.ayah_from is not None:
        pericopes = [{
            "surah": surah,
            "pericope": args.pericope or 1,
            "ayah_from": args.ayah_from,
            "ayah_to": args.ayah_to,
            "label": args.pericope_label or f"Ayahs {args.ayah_from}-{args.ayah_to}",
            "synthesized": False,
            "source": "cli-span",
        }]

    if args.ayah is not None:
        bundle = build_ayah_bundle(surah, args.ayah, quran_text, word_analysis, qac_by_ayah,
                                    root_id_map, pericopes, alignment)
        out_path = out_dir / f"{surah}_{args.ayah}.ayah.json"
        out_path.write_text(compact_json_text(bundle), encoding="utf-8")
        print(f"wrote {out_path}")
        return 0

    ayah_numbers = discover_ayah_numbers(surah, quran_text)
    if args.ayah_from is not None:
        ayah_numbers = [a for a in ayah_numbers if args.ayah_from <= a <= args.ayah_to]
    ayah_bundles = []
    filenames = []
    bundle_unit_refs: list[str] = []
    bundle_unit_files: list[str] = []
    if args.ayah_from is None and 0 in discover_bundle_unit_numbers(surah, quran_text):
        basmala_loaded = preflight_basmala(surah)
        basmala_bundle = build_basmala_bundle(surah, **basmala_loaded)
        basmala_filename = f"{surah}_0.ayah.json"
        (out_dir / basmala_filename).write_text(
            compact_json_text(basmala_bundle), encoding="utf-8"
        )
        bundle_unit_refs.append(f"{surah}:0")
        bundle_unit_files.append(basmala_filename)
        print(f"wrote {out_dir / basmala_filename}")
    for a in ayah_numbers:
        bundle = build_ayah_bundle(surah, a, quran_text, word_analysis, qac_by_ayah,
                                    root_id_map, pericopes, alignment)
        fname = f"{surah}_{a}.ayah.json"
        (out_dir / fname).write_text(compact_json_text(bundle), encoding="utf-8")
        ayah_bundles.append(bundle)
        filenames.append(fname)
        bundle_unit_refs.append(bundle["ayahRef"])
        bundle_unit_files.append(fname)
        print(f"wrote {out_dir / fname}")

    if args.ayah_from is not None:
        return 0

    surah_bundle = build_surah_bundle(
        surah,
        ayah_bundles,
        filenames,
        pericopes,
        bundle_unit_refs,
        bundle_unit_files,
    )
    surah_out_path = out_dir / f"{surah}.surah.json"
    surah_out_path.write_text(compact_json_text(surah_bundle), encoding="utf-8")
    print(f"wrote {surah_out_path}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RequiredSourceMissing as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        sys.exit(1)
