"""Shared, verified many-to-many analysis/QAC links from the frozen release.

The analysis namespace is independent of QAC word numbering. A whole expression
and its component may share morphemes when the accepted bridge says they do.
This module changes derived links only; it never rewrites source analyses.
"""

from __future__ import annotations

import atexit
from collections import defaultdict
from contextlib import ExitStack
from functools import lru_cache
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from _commentary.v5.qac_cache import open_database, _signature

DEFAULT_DATA_ROOT = ROOT.parent / "quran-data"
ALIGNMENT_VERSION = "qac-analysis-bridge-v1"
BRIDGE_PATH = "data/bridges/qac-masaq.sqlite.gz"
QAC_PATH = "data/morphology/qac.sqlite.gz"
SHARD_DIR = "data/analysis/word-analysis"
QAC_COLUMNS = ("qac_ref", "qac_word_ref", "surface_ar", "lemma_ar", "root_ar",
               "pos", "morpheme_role", "morph_features")
ARABIC_TAG = re.compile(r"\{\{ar:([^}]*)\}\}")


def _digest(path):
    before = _signature(path.stat())
    with path.open("rb") as stream:
        value = hashlib.file_digest(stream, "sha256").hexdigest()
    if before != _signature(path.stat()):
        raise ValueError(f"Source changed while hashing {path.name}")
    return value


class AnalysisBridge:
    def __init__(self, root=DEFAULT_DATA_ROOT, cache_dir=None):
        self.root = Path(root).resolve()
        self.stack = ExitStack()
        self.signatures = {}
        try:
            checksum_path = self.root / "CHECKSUMS.sha256"
            self.signatures["CHECKSUMS.sha256"] = _signature(checksum_path.stat())
            checksums = {}
            for line in checksum_path.read_text().splitlines():
                digest, name = line.split(maxsplit=1)
                if name in checksums or not re.fullmatch(r"[0-9a-f]{64}", digest):
                    raise ValueError("Invalid or duplicate release checksum")
                checksums[name] = digest
            self.checksums = checksums
            for name in ("RELEASE.json", BRIDGE_PATH, QAC_PATH):
                self._verify_file(name)
            release = json.loads((self.root / "RELEASE.json").read_text())
            if not any(row.get("path") == BRIDGE_PATH for row in release["datasets"]):
                raise ValueError("Release does not declare the analysis/QAC bridge")
            cache_args = {} if cache_dir is None else {"cache_dir": Path(cache_dir)}
            self.connection, digest = self.stack.enter_context(open_database(
                self.root / BRIDGE_PATH, **cache_args,
                schema_probe="SELECT analysis_ref, qac_morpheme_ref FROM analysis_qac_edges LIMIT 0",
            ))
            if digest != checksums[BRIDGE_PATH]:
                raise ValueError("Bridge checksum changed during opening")
            self.connection.row_factory = sqlite3.Row
            metadata = dict(self.connection.execute("SELECT key, value FROM metadata"))
            if (self.connection.execute("PRAGMA user_version").fetchone()[0] != 4
                    or metadata.get("schema_version") != "qac-masaq-bridge-v1"):
                raise ValueError("Unsupported analysis/QAC bridge schema")
            expected = {
                "qac_sha256": checksums[QAC_PATH],
                "quran_data_release_manifest_sha256": checksums["RELEASE.json"],
                "quran_data_release_id": release["release_id"],
            }
            # Verify the complete source tree once per process, then recheck the
            # relevant shard's stat before each use. Decompression is bounded.
            tree = hashlib.sha256()
            shards = sorted((self.root / SHARD_DIR).glob("s[0-9][0-9][0-9].jsonl.zst"))
            if len(shards) != 114:
                raise ValueError("The bridge requires all 114 released analysis shards")
            for path in shards:
                name = path.relative_to(self.root).as_posix()
                self._verify_file(name)
                tree.update(f"{path.name}\t{path.stat().st_size}\t{checksums[name]}\n".encode())
            expected["word_analysis_tree_sha256"] = tree.hexdigest()
            if any(metadata.get(key) != value for key, value in expected.items()):
                raise ValueError("Bridge metadata disagrees with the released sources")
            self.qac, qac_digest = self.stack.enter_context(open_database(
                self.root / QAC_PATH, **cache_args))
            if qac_digest != checksums[QAC_PATH]:
                raise ValueError("QAC checksum changed during opening")
            self.qac.row_factory = sqlite3.Row
            self.provenance = {
                "source": "quran-data/" + BRIDGE_PATH,
                "source_sha256": digest,
                "schema_version": metadata["schema_version"],
                "sqlite_user_version": 4,
                "release_id": release["release_id"],
                "release_manifest_sha256": checksums["RELEASE.json"],
                "qac_source_sha256": qac_digest,
                "word_analysis_tree_sha256": tree.hexdigest(),
            }
            for name in ("CHECKSUMS.sha256", "RELEASE.json", BRIDGE_PATH, QAC_PATH):
                if self.signatures[name] != _signature((self.root / name).stat()):
                    raise ValueError(f"Bridge source changed during opening: {name}")
        except BaseException:
            self.close()
            raise

    def close(self):
        self.stack.close()

    def _verify_file(self, name):
        path = self.root / name
        if self.checksums.get(name) != _digest(path):
            raise ValueError(f"Released source checksum mismatch: {name}")
        self.signatures[name] = _signature(path.stat())

    def _check_current(self, surah):
        for name in ("CHECKSUMS.sha256", "RELEASE.json", BRIDGE_PATH, QAC_PATH,
                     f"{SHARD_DIR}/s{surah:03d}.jsonl.zst"):
            if _signature((self.root / name).stat()) != self.signatures[name]:
                raise ValueError(f"Bridge source changed during this process: {name}")

    @lru_cache(maxsize=2)
    def _analysis(self, surah):
        executable = shutil.which("zstd")
        if executable is None:
            raise ValueError("zstd is required to verify released word analysis")
        path = self.root / SHARD_DIR / f"s{surah:03d}.jsonl.zst"
        payload = subprocess.run([executable, "-dc", str(path)], check=True,
                                 capture_output=True).stdout
        records = [json.loads(line) for line in payload.splitlines() if line.strip()]
        result = {row["ref"]: row for row in records}
        if len(result) != len(records):
            raise ValueError("Duplicate released word-analysis ayah")
        return result

    def align(self, analysis, qac_rows, source_ref=None):
        ref = source_ref or analysis.get("ref")
        if not isinstance(ref, str) or not re.fullmatch(r"[1-9][0-9]*:[1-9][0-9]*", ref):
            raise ValueError("Bridge alignment requires a canonical linguistic source ref")
        s, a = map(int, ref.split(":"))
        self._check_current(s)
        if analysis != self._analysis(s).get(ref):
            raise ValueError(f"{ref}: word analysis differs from the bridge's released source")
        canonical = self.qac.execute(
            "SELECT " + ",".join(QAC_COLUMNS) + " FROM qac_morphemes "
            "WHERE surah=? AND ayah=? ORDER BY word_index,morpheme_index", (s, a)
        ).fetchall()
        if not canonical or [tuple(row.get(k) for k in QAC_COLUMNS) for row in qac_rows] != [tuple(row) for row in canonical]:
            raise ValueError(f"{ref}: bundled morphology differs from canonical QAC")
        qac_refs = {row["qac_ref"] for row in canonical}
        units = {row["analysis_ref"]: row for row in self.connection.execute(
            "SELECT * FROM word_analysis_units WHERE surah=? AND ayah=?", (s, a))}
        edges = defaultdict(list)
        for row in self.connection.execute(
            "SELECT e.* FROM analysis_qac_edges e JOIN word_analysis_units u USING(analysis_ref) "
            "WHERE u.surah=? AND u.ayah=? ORDER BY u.critical_w,e.qac_order", (s, a)):
            edges[row["analysis_ref"]].append(row["qac_morpheme_ref"])
        words = analysis["words"]
        ids = [f"{ref}:{word['critical_w']}" for word in words]
        if len(set(ids)) != len(ids) or set(ids) != set(units):
            raise ValueError(f"{ref}: bridge and analysis unit inventories differ")
        spans, gaps, owners = [], [], defaultdict(list)
        for index, (word, analysis_ref) in enumerate(zip(words, ids)):
            unit = units[analysis_ref]
            surface = ARABIC_TAG.search(word.get("surface_display", ""))
            if surface is None or surface[1] != unit["surface_ar"]:
                raise ValueError(f"{analysis_ref}: bridge analysis surface mismatch")
            refs = edges[analysis_ref]
            if unit["relation_status"] == "excluded-source-defect":
                if refs or not unit["exclusion_reason"]:
                    raise ValueError(f"{analysis_ref}: invalid bridge exclusion")
                spans.append(None)
                gaps.append({"word_index": index, "analysis_ref": analysis_ref,
                             "surface_ar": surface[1], "status": "excluded-source-defect",
                             "reason": unit["exclusion_reason"]})
                continue
            if (unit["relation_status"] != "accepted" or not refs
                    or len(refs) != len(set(refs)) or not set(refs) <= qac_refs):
                raise ValueError(f"{analysis_ref}: invalid accepted bridge mapping")
            ordered = sorted(refs, key=lambda value: tuple(map(int, value.split(":"))))
            if refs != ordered:
                raise ValueError(f"{analysis_ref}: reordered bridge QAC refs")
            word_ids, morpheme_ids = [], []
            for qref in refs:
                qs, qa, qw, qm = map(int, qref.split(":"))
                wid = f"w-s{qs:03d}-a{qa:03d}-w{qw:03d}"
                if wid not in word_ids:
                    word_ids.append(wid)
                morpheme_ids.append(f"m-{wid}-{qm:02d}")
                owners[qref].append(analysis_ref)
            spans.append({"word_index": index, "analysis_ref": analysis_ref,
                          "surface_ar": surface[1], "word_ids": word_ids,
                          "qac_refs": refs, "morpheme_ids": morpheme_ids,
                          "aligned_qac_word_ref_upstream": word.get("aligned_qac_word_ref")})
        coverage = {
            "present": True, "alignment_version": ALIGNMENT_VERSION,
            "source_namespace": "word-analysis", "target_namespace": "qac-morpheme",
            "bridge": dict(self.provenance), "linguistic_source_ref": ref,
            "words_total": len(words), "words_resolved": len(words) - len(gaps),
            "words_unresolved": len(gaps), "unresolved": gaps,
            "shared_morphemes": [{"qac_ref": qref, "analysis_refs": refs}
                                 for qref, refs in owners.items() if len(refs) > 1],
            "note": "Accepted bridge links preserve independent analysis identities. "
                    "Several analysis entries may share canonical morphemes. Read their "
                    "distinct semantic claims; shared morphology alone is not duplication. "
                    "Legacy aligned_qac_word_ref values are source observations, not QAC joins. "
                    "Excluded source entries remain available with their explicit qualification.",
        }
        self._check_current(s)
        return spans, coverage


_BRIDGES = {}


def get_bridge(root=DEFAULT_DATA_ROOT):
    key = (os.getpid(), str(Path(root).resolve()))
    if key not in _BRIDGES:
        _BRIDGES[key] = AnalysisBridge(root)
        atexit.register(_BRIDGES[key].close)
    return _BRIDGES[key]


def validate_bundle(bundle, *, source_ref):
    spans, coverage = get_bridge().align(bundle["word_analysis"], bundle["qac_morphemes"], source_ref)
    if spans != bundle.get("word_morpheme_spans"):
        raise ValueError("Bundle word/QAC links differ from the accepted bridge; regenerate the bundle")
    if coverage != bundle.get("coverage", {}).get("word_morpheme_spans"):
        raise ValueError("Bundle word/QAC bridge provenance or coverage is stale; regenerate the bundle")
    return [span["qac_refs"] if span else [] for span in spans]
