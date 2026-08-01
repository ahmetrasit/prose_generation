import argparse
import base64
from decimal import Decimal
import hashlib
import io
import json
import sys
import tempfile
import unittest
from unittest import mock
import wave
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import prepare_tts_chunks as prepare  # noqa: E402
import synthesize_tts_chunks as synth  # noqa: E402


class SynthesizeTtsChunksTest(unittest.TestCase):
    def build_collection(self, directory):
        source = prepare.QURAN_DATA_ROOT / "data/commentary/surah/detailed/tr/s001"
        files = prepare.collect_source_files(source, "surah")
        artifacts = prepare.build_artifacts(
            source,
            "surah",
            files,
            "S001",
            Path(directory).resolve(),
            "surah",
        )
        prepare.write_artifacts(artifacts)
        return artifacts["outDir"]

    def test_preflight_is_offline_and_confirmation_is_exact(self):
        with tempfile.TemporaryDirectory() as directory:
            collection = self.build_collection(directory)
            preflight = synth.preflight_collection(collection, limit=1)

            self.assertEqual(len(preflight["remoteChunks"]), 1)
            self.assertEqual(preflight["ttsChars"], 511)
            self.assertEqual(len(preflight["requestBodies"]), 12)

            args = argparse.Namespace(
                confirm_remote="wrong-digest",
                confirm_cost_usd=preflight["maximumCostUsd"],
                max_cost_usd=Decimal("1"),
                force=False,
                confirm_force=False,
            )
            with self.assertRaises(PermissionError):
                synth.require_remote_confirmation(args, preflight)

    def test_request_digest_covers_exact_frozen_post_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            collection = self.build_collection(directory)
            first = synth.preflight_collection(collection, limit=1)
            body = first["requestBodies"][first["targetChunks"][0]["chunkId"]]
            project = synth.DEFAULT_PROJECT_ID.encode("utf-8")
            expected = hashlib.sha256(
                len(project).to_bytes(8, "big")
                + project
                + len(body).to_bytes(8, "big")
                + body
            ).hexdigest()
            self.assertEqual(first["requestDigest"], expected)

            request_path = collection / first["targetChunks"][0]["request"]
            request_path.write_bytes(request_path.read_bytes() + b"\n")
            second = synth.preflight_collection(collection, limit=1)
            self.assertNotEqual(first["requestDigest"], second["requestDigest"])

    def test_duplicate_json_keys_are_rejected(self):
        with self.assertRaises(ValueError):
            synth.strict_json_loads('{"text":"one", "text":"two"}')

    def test_limit_must_be_positive_and_within_collection(self):
        with tempfile.TemporaryDirectory() as directory:
            collection = self.build_collection(directory)
            for limit in (0, 13):
                with self.subTest(limit=limit):
                    with self.assertRaises(ValueError):
                        synth.preflight_collection(collection, limit=limit)

    def test_exact_chunk_selection_is_noncontiguous_and_canonical(self):
        with tempfile.TemporaryDirectory() as directory:
            collection = self.build_collection(directory)
            preflight = synth.preflight_collection(
                collection,
                chunk_ids=["sec-001-p-003", "sec-001-p-001"],
            )

            self.assertEqual(
                [chunk["chunkId"] for chunk in preflight["targetChunks"]],
                ["sec-001-p-001", "sec-001-p-003"],
            )
            self.assertEqual(preflight["selection"], "chunk_ids")
            self.assertEqual(len(preflight["remoteChunks"]), 2)
            self.assertEqual(len(preflight["requestBodies"]), 12)
            self.assertEqual(
                synth.preflight_summary(preflight, True)["targetChunkIds"],
                ["sec-001-p-001", "sec-001-p-003"],
            )

            with self.assertRaises(ValueError):
                synth.preflight_collection(
                    collection,
                    limit=1,
                    chunk_ids=["sec-001-p-001"],
                )
            with self.assertRaises(ValueError):
                synth.preflight_collection(
                    collection,
                    chunk_ids=["sec-001-p-001", "sec-001-p-001"],
                )
            with self.assertRaises(ValueError):
                synth.preflight_collection(
                    collection,
                    chunk_ids=["sec-999-p-001"],
                )

    def test_manifest_and_chunk_identity_are_bound_to_collection(self):
        with tempfile.TemporaryDirectory() as directory:
            collection = self.build_collection(directory)
            manifest = synth.load_manifest(collection / "manifest.json")
            chunks = synth.load_jsonl(collection / "chunks.jsonl")
            chunks[0]["surahId"] = "S002"
            with self.assertRaises(ValueError):
                synth.validate_manifest_and_chunks(collection, manifest, chunks)

    def test_noncanonical_chunk_paths_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            collection = self.build_collection(directory)
            chunks = synth.load_jsonl(collection / "chunks.jsonl")
            chunks[0]["request"] = "../outside.json"
            with self.assertRaises(ValueError):
                synth.validate_chunk_paths(collection, chunks[0])

    def test_symlinked_artifact_aliases_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            collection = self.build_collection(directory)
            target = collection / "alias-target"
            target.mkdir()
            alias = collection / "alias"
            alias.symlink_to(target, target_is_directory=True)
            with self.assertRaises(ValueError):
                synth.safe_relative_path(collection, "alias/file.json", "test")

    def test_symlinked_collection_path_is_rejected_before_resolution(self):
        with tempfile.TemporaryDirectory() as directory:
            collection = self.build_collection(directory)
            alias = Path(directory) / "collection-alias"
            alias.symlink_to(collection, target_is_directory=True)
            with self.assertRaises(ValueError):
                synth.preflight_collection(alias, limit=1)

    def test_unknown_remote_outcome_requires_explicit_reconciliation(self):
        with tempfile.TemporaryDirectory() as directory:
            collection = self.build_collection(directory)
            chunks = synth.load_jsonl(collection / "chunks.jsonl")
            chunks[0]["remoteOutcome"] = "unknown"
            synth.write_jsonl(collection / "chunks.jsonl", chunks)
            synth.update_manifest(
                collection / "manifest.json",
                {chunk["chunkId"]: chunk for chunk in chunks},
            )
            with self.assertRaises(ValueError):
                synth.preflight_collection(collection, limit=1)
            preflight = synth.preflight_collection(
                collection,
                limit=1,
                reconcile_unknown=True,
            )
            self.assertEqual(len(preflight["remoteChunks"]), 1)

    def test_preparation_refuses_to_erase_unknown_remote_outcome(self):
        with tempfile.TemporaryDirectory() as directory:
            collection = self.build_collection(directory)
            chunks = synth.load_jsonl(collection / "chunks.jsonl")
            chunks[0]["remoteOutcome"] = "unknown"
            synth.write_jsonl(collection / "chunks.jsonl", chunks)
            synth.update_manifest(
                collection / "manifest.json",
                {chunk["chunkId"]: chunk for chunk in chunks},
            )

            source = prepare.QURAN_DATA_ROOT / "data/commentary/surah/detailed/tr/s001"
            files = prepare.collect_source_files(source, "surah")
            artifacts = prepare.build_artifacts(
                source,
                "surah",
                files,
                "S001",
                Path(directory).resolve(),
                "surah",
            )
            with self.assertRaises(ValueError):
                prepare.write_artifacts(artifacts)

    def test_preparation_and_synthesis_share_collection_lock(self):
        with tempfile.TemporaryDirectory() as directory:
            collection = self.build_collection(directory)
            with synth.CollectionLock(collection):
                with self.assertRaises(RuntimeError):
                    with prepare.CollectionLock(collection):
                        pass

    def test_manifest_paragraph_character_count_is_verified(self):
        with tempfile.TemporaryDirectory() as directory:
            collection = self.build_collection(directory)
            manifest = synth.load_manifest(collection / "manifest.json")
            chunks = synth.load_jsonl(collection / "chunks.jsonl")
            manifest["sections"][0]["paragraphs"][0]["ttsCharCount"] += 1
            with self.assertRaises(ValueError):
                synth.validate_manifest_and_chunks(collection, manifest, chunks)

    def test_nonfinite_cost_is_rejected(self):
        with self.assertRaises(Exception):
            synth.decimal_argument("NaN")
        with self.assertRaises(Exception):
            prepare.cost_argument("Infinity")

    def test_redirect_handler_never_returns_a_followup_request(self):
        handler = synth.NoRedirectHandler()
        self.assertIsNone(handler.redirect_request(None, None, 302, "Found", {}, "https://example.com"))

    def test_only_observed_generic_provider_error_is_retryable(self):
        self.assertTrue(
            synth.is_retryable_known_error(
                {
                    "error": {
                        "code": 400,
                        "status": "INVALID_ARGUMENT",
                        "message": "Request contains an invalid argument.",
                    }
                }
            )
        )
        self.assertFalse(
            synth.is_retryable_known_error(
                {
                    "error": {
                        "code": 400,
                        "status": "INVALID_ARGUMENT",
                        "message": "Policy rejection",
                    }
                }
            )
        )

    def test_remote_attempt_automatically_creates_terminal_ledger_entries(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            collection = self.build_collection(root)
            preflight = synth.preflight_collection(collection, limit=1)
            wav_buffer = io.BytesIO()
            with wave.open(wav_buffer, "wb") as handle:
                handle.setnchannels(synth.CHANNELS)
                handle.setsampwidth(synth.BYTES_PER_SAMPLE)
                handle.setframerate(synth.SAMPLE_RATE)
                handle.writeframes(b"\0\0" * 240)
            response = {
                "audioContent": base64.b64encode(wav_buffer.getvalue()).decode("ascii")
            }
            args = argparse.Namespace(
                force=False,
                ledger_dir=root / "ledger",
                project_id=synth.DEFAULT_PROJECT_ID,
                limit=1,
                chunk_ids=None,
            )

            with mock.patch.object(synth, "get_authorized_token", return_value="token"), \
                    mock.patch.object(synth, "synthesize", return_value=response), \
                    mock.patch.object(synth, "materialize_original_mp3"), \
                    mock.patch.object(synth, "build_section_derivatives"):
                result = synth.process_collection(
                    preflight, args, synth._REMOTE_AUTHORIZATION
                )

            self.assertEqual(result, 0)
            ledger_path = next((root / "ledger").glob("*.jsonl"))
            entries = [json.loads(line) for line in ledger_path.read_text().splitlines()]
            self.assertEqual([entry["event"] for entry in entries], ["attempted", "synthesized"])
            self.assertEqual(entries[0]["attemptId"], entries[1]["attemptId"])
            self.assertTrue(entries[0]["possibleNewSpend"])
            self.assertTrue(entries[1]["newSpend"])


if __name__ == "__main__":
    unittest.main()
