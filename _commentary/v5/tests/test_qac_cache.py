"""Cache behavior at the file/query boundary, including simultaneous first use."""

import gzip
import hashlib
import os
import sqlite3
import sys
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from _commentary.v5 import packet_evidence, qac_cache, workflow


class QacCacheTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "qac.sqlite.gz"
        self.cache = self.root / "cache with spaces"
        self.write_source("first")

    def write_source(self, surface):
        connection = sqlite3.connect(":memory:")
        try:
            columns = ",".join(f"{key} TEXT" for key in packet_evidence.MORPHEME_COLUMNS)
            connection.execute(f"CREATE TABLE qac_morphemes ({columns},surah INT,ayah INT,word_index INT,morpheme_index INT)")
            connection.execute("INSERT INTO qac_morphemes VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                               ("7:201:12:1", surface, "مُبْصِر", "ب ص ر", "N", "STEM", "ACT|PCPL|(IV)|MP|NOM", 7, 201, 12, 1))
            connection.commit()
            self.source.write_bytes(gzip.compress(connection.serialize(), compresslevel=0, mtime=0))
        finally:
            connection.close()

    def read_surface(self):
        rows, error, source_hash = packet_evidence._morphology(self.source, {"7:201"}, self.cache)
        self.assertIsNone(error)
        self.assertEqual(source_hash, hashlib.sha256(self.source.read_bytes()).hexdigest())
        return rows["7:201"][0][1]

    def test_streamed_cache_is_exact_and_reused_without_decompression(self):
        self.assertEqual(self.read_surface(), "first")
        database, = self.cache.glob("*.sqlite")
        self.assertEqual(database.read_bytes(), gzip.decompress(self.source.read_bytes()))
        with patch.object(qac_cache.gzip, "GzipFile", side_effect=AssertionError("unexpected decompression")):
            self.assertEqual(self.read_surface(), "first")
        with qac_cache.open_database(self.source, self.cache) as (connection, _source_hash):
            connection.execute("PRAGMA query_only = OFF")
            with self.assertRaisesRegex(sqlite3.OperationalError, "readonly"):
                connection.execute("DELETE FROM qac_morphemes")

    def test_same_size_same_mtime_source_replacement_does_not_reuse_stale_rows(self):
        self.assertEqual(self.read_surface(), "first")
        previous = self.source.stat()
        self.write_source("other")
        os.utime(self.source, ns=(previous.st_atime_ns, previous.st_mtime_ns))
        self.assertEqual(self.source.stat().st_size, previous.st_size)
        self.assertEqual(self.source.stat().st_mtime_ns, previous.st_mtime_ns)
        self.assertEqual(self.read_surface(), "other")
        self.assertEqual(len(list(self.cache.glob("*.sqlite"))), 2)

    def test_concurrent_cold_readers_build_once_and_get_complete_rows(self):
        barrier = threading.Barrier(4)
        def read():
            barrier.wait(timeout=10)
            return self.read_surface()
        with patch.object(qac_cache.gzip, "GzipFile", wraps=gzip.GzipFile) as decompress:
            with ThreadPoolExecutor(max_workers=4) as executor:
                self.assertEqual(list(executor.map(lambda _: read(), range(4))), ["first"] * 4)
            self.assertEqual(decompress.call_count, 1)
        self.assertEqual(len(list(self.cache.glob("*.sqlite"))), 1)
        self.assertEqual(list(self.cache.glob("*.tmp")), [])

    def test_corrupt_cache_header_is_rebuilt_from_valid_source(self):
        self.assertEqual(self.read_surface(), "first")
        database, = self.cache.glob("*.sqlite")
        for damaged in (b"damaged local cache", b""):
            with self.subTest(damaged=damaged):
                database.write_bytes(damaged)
                self.assertEqual(self.read_surface(), "first")

    def test_failed_build_leaves_no_published_or_partial_database(self):
        self.source.write_bytes(gzip.compress(b"not a SQLite database"))
        rows, error, _source_hash = packet_evidence._morphology(self.source, {"7:201"}, self.cache)
        self.assertEqual(rows, {})
        self.assertIn("could not be projected", error)
        self.assertEqual(list(self.cache.glob("*.sqlite")), [])
        self.assertEqual(list(self.cache.glob("*.tmp")), [])

    def test_unusable_cache_path_qualifies_missing_morphology(self):
        self.cache.write_text("a file occupies the cache directory")
        packet = {"review_inventory": {"context_refs": ["7:201"]}}
        packet_evidence.attach_context_evidence({"global": packet},
            {"7:201": {"arabic_uthmani": "مُبْصِرُونَ"}}, self.source, self.cache)
        self.assertEqual(packet["context_evidence"][0]["arabic_uthmani"], "مُبْصِرُونَ")
        self.assertEqual(packet["context_evidence_coverage"]["missing_morphology_refs"], ["7:201"])
        self.assertTrue(packet["context_evidence_coverage"]["morphology_error"])

    def test_provenance_is_identical_for_source_copies_at_different_paths(self):
        packets = []
        for name in ("machine-a", "machine-b"):
            directory = self.root / name
            directory.mkdir()
            source = directory / "source.gz"
            source.write_bytes(self.source.read_bytes())
            packet = {"review_inventory": {"context_refs": ["7:201"]}}
            packet_evidence.attach_context_evidence({"global": packet},
                {"7:201": {"arabic_uthmani": "مُبْصِرُونَ"}}, source, directory / "cache")
            packets.append(packet)
        self.assertEqual(packets[0], packets[1])
        coverage = packets[0]["context_evidence_coverage"]
        self.assertEqual(coverage["morphology_source"], "qac-morphology/qac.sqlite.gz")
        self.assertEqual(coverage["morphology_source_sha256"], hashlib.sha256(self.source.read_bytes()).hexdigest())

    def test_cli_source_failure_stops_before_any_batch_unit_is_prepared(self):
        argv = ["workflow.py", "prepare", "--ayah", "29:38-39",
                "--qac-morphology", str(self.root / "missing.gz"), "--qac-cache-dir", str(self.cache)]
        error = StringIO()
        with patch.object(sys, "argv", argv), patch.object(workflow, "_prepare_batch") as prepare_batch, redirect_stderr(error):
            self.assertEqual(workflow.main(), 1)
        prepare_batch.assert_not_called()
        self.assertIn("QAC source preflight failed", error.getvalue())

    def test_production_preflight_checks_the_full_qac_schema(self):
        connection = sqlite3.connect(":memory:")
        try:
            connection.execute("CREATE TABLE qac_morphemes (qac_ref TEXT)")
            self.source.write_bytes(gzip.compress(connection.serialize()))
        finally:
            connection.close()
        args = workflow._parser().parse_args(["prepare", "--ayah", "29:38",
            "--qac-morphology", str(self.source), "--qac-cache-dir", str(self.cache)])
        with self.assertRaisesRegex(workflow.WorkflowError, "QAC source preflight failed"):
            workflow._preflight_qac(args)
        args.allow_missing_qac_morphology = True
        workflow._preflight_qac(args)


if __name__ == "__main__":
    unittest.main()
