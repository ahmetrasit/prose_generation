from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import tempfile
import unittest

from _commentary.v7 import authoring as a


def packet(lane="micro"):
    return {
        "identity": {"ayah_ref": "29:38", "lane": lane},
        "scope": {"lane": lane}, "focus": {"arabic": "فعل"},
        "focus_surface_evidence": {"morphology": ["full"]},
        "focus_word_alignment": {"qualification": "shared"},
        "context_morpheme_columns": ["surface", "root"],
        "context_evidence_coverage": {"complete": True},
        "candidate_inventory": [{
            "candidate_id": "c1", "kind": "word", "branch_refs": ["r/B1"],
            "candidate_specific_support_ids": ["s1"], "required_context_refs": ["29:41"],
        }],
        "support_registry": [{"support_id": "s1", "text": "source", "trust": "qualified"}],
        "branch_registry": [{"branch_ref": "r/B1", "semantic_detail": {
            "facets": [{"type": "extension", "statements": [
                {"type": "SOURCE_IMAGE", "image_ar": "العين", "image_en": "eye"},
                {"type": "definition", "statement": "particular form only"},
            ]}], "qualification": "attested form, not the ordinary focus sense"}}],
        "context_evidence": [{"ayah_ref": "29:41", "arabic": "العنكبوت", "morphemes": [["عنكبوت", "عنكب"]]}],
        "connection_registry": [
            {"connection_ref": "conn1", "connection_evidence_ref": "ev1", "qualification": "one"},
            {"connection_ref": "conn1", "reciprocal_evidence": [
                {"connection_evidence_ref": "ev2", "qualification": "opposite direction"}],
             "qualification": "two"},
        ],
    }


def discovery(lane="micro"):
    return {
        "schema_version": a.w.SCOPE_DISCOVERY_SCHEMA_VERSION, "ayah_ref": "29:38", "lane": lane,
        "findings": [{"finding_ref": f"{lane}:f1", "title": "An extension",
                      "reading": "The evidence connects through a particular form.\nA second paragraph.",
                      "evidence_refs": ["branch:r/B1", "connection:conn1"]}],
        "candidate_decisions": [{"candidate_id": "c1", "decision": "accept",
                                 "finding_refs": [f"{lane}:f1"], "reason": "Explained in full."}],
        "friction_notes": [],
    }


def read_args(path, **kwargs):
    defaults = dict(prompt=path, section=None, refs=None, block=None, start=0,
                    count=20, offset=None, limit=12000)
    return argparse.Namespace(**(defaults | kwargs))


class AuthoringTests(unittest.TestCase):
    def test_attachment_keeps_variants_qualifications_and_reciprocal_wrappers(self):
        p, d = packet(), discovery()
        original = copy.deepcopy(p)
        a.validate_discovery(d, p)  # No core-facet requirement for the extension.
        evidence = a.attached_evidence(d, p)
        records = {row["evidence_ref"]: row["record"] for row in evidence["records"]}
        self.assertEqual(records["branch:r/B1"], p["branch_registry"][0])
        self.assertEqual(records["context:29:41"], p["context_evidence"][0])
        self.assertEqual(records["support:s1"], p["support_registry"][0])
        self.assertEqual(records["connection:conn1"], p["connection_registry"])
        self.assertEqual(a.source_index(p)["connection:ev2"], [p["connection_registry"][1]])
        self.assertEqual(p, original)

    def test_handoffs_embed_verbatim_outputs_and_fail_on_missing_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            layout = a.w.Layout(ayah_ref="29:38", analysis_id="test", stem="29_38",
                                input=root / "input", raw=root / "raw", editorial=root / "editorial")
            layout.input.mkdir()
            layout.raw.mkdir()
            for lane in a.w.LANES:
                layout.scope_prompt(lane).write_text("instructions\n" + a.block("lane_packet_json", json.dumps(packet(lane))))
                layout.scope_discovery(lane).write_text(json.dumps(discovery(lane), indent=3) + "\n")
                layout.scope_prose(lane).write_text(f"{lane} prose\n\nSecond paragraph.\n")
            originals = {p: p.read_bytes() for p in layout.raw.iterdir()}
            path, prompt = a.render_handoff(layout, "canonical")
            for p, content in originals.items():
                self.assertIn(content.decode(), prompt)
                self.assertEqual(p.read_bytes(), content)
            self.assertEqual(path, layout.canonical_prompt())
            self.assertIn('"image_ar":"العين"', prompt)
            self.assertFalse(a.w.MARKER_RE.search(prompt))
            layout.consolidated_prose().write_text("First pass, unchanged.\n")
            _, editorial = a.render_handoff(layout, "editorial")
            self.assertIn("First pass, unchanged.\n", editorial)
            path.write_text("previous handoff")
            layout.scope_prose("global").unlink()
            with self.assertRaises(FileNotFoundError):
                a.render_handoff(layout, "canonical")
            self.assertEqual(path.read_text(), "previous handoff")

    def test_reader_preserves_selected_oversized_record_across_windows(self):
        p = packet()
        p["support_registry"].append({"support_id": "large", "text": "غ" * 30000, "tail": "retained"})
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "prompt.md"
            path.write_text("instructions\n" + a.block("lane_packet_json", json.dumps(p, ensure_ascii=False)))
            with self.assertRaisesRegex(a.w.WorkflowError, "--start 1 --count 1 --offset 0"):
                a.read_evidence(read_args(path, section="support_registry", start=1, count=1))
            offset, pieces = 0, []
            while offset is not None:
                result = a.read_evidence(read_args(path, section="support_registry", start=1,
                                                   count=1, offset=offset))
                pieces.append(result["text"])
                offset = result["next_offset"]
            self.assertEqual(json.loads("".join(pieces)), [p["support_registry"][1]])

    def test_authoring_input_read_does_not_require_source_appendix_traversal(self):
        content = 'first prose\n\n' + a.block("micro_discovery_json", '{"reading":"intact"}')
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "handoff.md"
            path.write_text("instructions\n" + a.block("authoring_inputs", content)
                            + "\n" + a.block("micro_source_evidence_json", '{"long":"source"}'))
            index = a.read_evidence(read_args(path))
            self.assertEqual(index["instructions"], "instructions")
            self.assertIn("authoring_inputs", index["blocks_characters"])
            result = a.read_evidence(read_args(path, block="authoring_inputs"))
            self.assertEqual(result["text"], content)
            self.assertIsNone(result["next_offset"])

    def test_invalid_evidence_reference_fails_without_semantic_substitution(self):
        d = discovery()
        d["findings"][0]["evidence_refs"].append("branch:absent/B1")
        with self.assertRaisesRegex(a.w.WorkflowError, "evidence does not exist"):
            a.validate_discovery(d, packet())


if __name__ == "__main__":
    unittest.main()
