"""V6 delivery, restart, and completion checks using synthetic source evidence."""

import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from _commentary.v6 import discovery, reading


def packet_fixture():
    return {
        "identity": {"ayah_ref": "1:1", "lane": "global", "linguistic_source_ref": "1:1"},
        "focus": {"arabic_uthmani": "بِسْمِ", "qac_morphemes": [
            {"qac_ref": "1:1:1:1", "qac_word_ref": "1:1:1"}]},
        "candidate_inventory": [{"candidate_id": "c1", "support_ids": ["s1"],
            "branch_refs": ["root/B001"], "required_context_refs": ["4:1"],
            "required_branch_facets": [{"branch_ref": "root/B001", "facet_id": "F001"}],
            "semantic_obligations": [{"obligation_ref": "o1"}]}],
        "support_registry": [{"support_id": "s1", "text": json.dumps({"claim": "Source fact"})}],
        "branch_registry": [{"branch_ref": "root/B001", "root_ar": "س م و", "gloss": "source gloss",
            "boundary": "source boundary", "review_facets": [{"facet_id": "F001", "role": "core",
                "statements": {"statement": "exact facet"}}],
            "semantic_detail": {"long_source": 'بسم "\\\n' * 2400, "empty": [], "a/b~c": None}}],
        "connection_registry": [{"connection_ref": "conn1", "target_ref": "4:1",
            "required_context_refs": ["4:1"], "note": "An unranked comparison."}],
        "context_morpheme_columns": ["qac_ref", "surface_ar"],
        "context_evidence": [{"ayah_ref": "4:1", "morphemes": [["4:1:1:1", "يَا"]]}],
        "selected_context_units": [],
    }


def discovery_fixture():
    return {
        "schema_version": discovery.DISCOVERY_SCHEMA, "ayah_ref": "1:1", "lane": "global",
        "coverage_complete": True, "friction_notes": [],
        "candidate_decisions": [{"candidate_id": "c1", "decision": "accept", "reason": "Fixture reason",
            "finding_refs": ["global:fixture"], "branch_exclusions": [], "facet_exclusions": [],
            "context_exclusions": [], "semantic_obligation_exclusions": []}],
        "findings": [{"finding_ref": "global:fixture", "origin_candidate_id": "c1",
            "represented_candidate_ids": [], "title": "Fixture", "claim": "Fixture claim",
            "mechanism": "Fixture mechanism", "reader_payoff": "Fixture payoff", "containment": "Fixture boundary",
            "epistemic": {"status": "qualified", "source_trust": [], "reason": "Fixture qualification"},
            "support_ids": ["s1"], "connection_refs": ["conn1"], "context_refs": ["4:1"],
            "semantic_obligation_refs": ["o1"], "evidence_facts": [{"support_id": "s1",
                "source_pointer": "/support_registry/0/text/claim", "function": "trigger", "fact": "Source fact"}],
            "branch_activations": [{"branch_ref": "root/B001", "facet_id": "F001",
                "branch_gloss": "source gloss", "facet_statement": "exact facet",
                "application_mode": "contextual_resonance", "carrier_refs": ["1:1:1:1"],
                "trigger_refs": ["4:1:1:1"], "focus_return_refs": ["1:1:1:1"],
                "carrier": "Fixture carrier", "independent_trigger": "Fixture trigger",
                "activation": "Fixture contact", "resulting_reading": "Fixture result", "boundary": "Fixture limit"}]}],
    }


class ReadingTests(unittest.TestCase):
    def test_large_record_spans_bounded_batches_without_losing_values(self):
        packet = packet_fixture()
        plan = reading.make_plan(packet, analysis_id="fixture", batch_budget=8000)
        reloaded = json.loads(reading.encode(packet))
        self.assertEqual(plan, reading.make_plan(reloaded, analysis_id="fixture", batch_budget=8000))
        self.assertTrue(any(b.get("record_pages") for b in plan["batches"]))
        pieces, strings = {}, {}
        for batch in plan["batches"]:
            self.assertLessEqual(batch["evidence_bytes"], 8000)
            for page in reading.batch_pages(packet, plan, batch):
                self.assertLessEqual(len(reading.encode(page)), 8000)
                for row in page["records"]:
                    pointer = row["source_pointer"]
                    source = reading.resolve(packet, pointer)
                    if "string_fragment" in row:
                        info = row["string_fragment"]
                        self.assertEqual(row["value"], source[info["start"]:info["end"]])
                        strings.setdefault(pointer, []).append((info["start"], row["value"]))
                    else:
                        self.assertNotIn(pointer, pieces)
                        self.assertEqual(row["value"], source)
                        pieces[pointer] = row["value"]
        for pointer, fragments in strings.items():
            self.assertEqual(''.join(v for _, v in sorted(fragments)), reading.resolve(packet, pointer))
        self.assertIn("/connection_registry/0", pieces)  # No candidate nominates this connection.
        self.assertIn("/branch_registry/0/semantic_detail/empty", pieces)
        self.assertIn("/branch_registry/0/semantic_detail/a~1b~0c", pieces)

    def test_duplicate_identities_and_missing_dependencies_fail_preparation(self):
        packet = packet_fixture()
        packet["branch_registry"].append(copy.deepcopy(packet["branch_registry"][0]))
        with self.assertRaisesRegex(reading.ReadingError, "duplicate"):
            reading.make_plan(packet, analysis_id="fixture")
        packet = packet_fixture()
        packet["context_evidence"] = []
        with self.assertRaisesRegex(reading.ReadingError, "context record"):
            reading.make_plan(packet, analysis_id="fixture")

    def test_numeric_and_identity_pointers_resolve_encoded_support_text(self):
        packet = packet_fixture()
        self.assertEqual(reading.resolve(packet, "/support_registry/s1/text/claim"), "Source fact")
        self.assertEqual(reading.resolve(packet, "/branch_registry/root~1B001/gloss"), "source gloss")


class CompletionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.packet = packet_fixture()
        self.plan = reading.make_plan(self.packet, analysis_id="fixture")
        self.plan["instructions_sha256"] = hashlib.sha256(b"Fixture instructions").hexdigest()
        self.plan_path = self.root / "input" / "global.reading.json"
        self.plan_path.parent.mkdir()
        self.plan_path.write_bytes(reading.encode(self.plan))
        self.plan_path.with_name("global.packet.json").write_bytes(reading.encode(self.packet))
        self.plan_path.with_name("global.discovery.prompt.md").write_bytes(b"Fixture instructions")
        self.session = discovery.Session(self.plan_path, raw_root=self.root / "raw")
        self.session.init()

    def deliver_batches(self):
        for bid in self.session.batches:
            for n in range(1, len(self.session.batch_pages(bid)) + 1):
                self.session.read(bid, None, n)
            self.session.complete(bid)

    def deliver_catalogs(self):
        for kind in ("branches", "connections"):
            for n in range(1, len(self.session.catalog_view(kind)) + 1):
                self.session.read(None, kind, n)

    def completed_work(self):
        self.deliver_batches()
        self.deliver_catalogs()
        work = self.session.load_work()
        work["cross_batch_review"] = "Fixture cross-batch review"
        work["discovery"] = discovery_fixture()
        self.session.save(work)
        return work

    def test_restart_preserves_unfinished_leads_and_precise_remaining_pages(self):
        bid = next(iter(self.session.batches))
        self.session.read(bid, None, 1)
        work = self.session.load_work()
        work["leads"] = [{"lead_id": "L1", "note": "Keep this unfinished comparison", "status": "open"}]
        self.session.save(work)
        resumed = discovery.Session(self.plan_path, raw_root=self.root / "raw")
        self.assertEqual(resumed.load_work(), work)
        self.assertNotIn(1, resumed.status()["next_unread_pages"])
        self.assertEqual(resumed.status()["open_lead_ids"], ["L1"])
        with self.assertRaisesRegex(discovery.DiscoveryError, "unfinished"):
            resumed.finish()
        self.assertFalse(resumed.output_path.exists())

    def test_missing_pages_and_early_catalog_reads_do_not_allow_completion(self):
        bid = next(b for b in self.session.batches if len(self.session.batch_pages(b)) > 1)
        self.session.read(bid, None, 1)
        with self.assertRaisesRegex(discovery.DiscoveryError, "every page"):
            self.session.complete(bid)
        self.deliver_catalogs()
        self.assertEqual(self.session.load_work()["catalog_pages"], {})
        self.deliver_batches()
        with self.assertRaisesRegex(discovery.DiscoveryError, "catalog"):
            self.session.finish()
        self.assertFalse(self.session.output_path.exists())

    def test_changed_evidence_instructions_or_plan_cannot_resume(self):
        for name in ("global.packet.json", "global.discovery.prompt.md", "global.reading.json"):
            with self.subTest(name=name):
                path = self.plan_path.with_name(name)
                original = path.read_bytes()
                if name.endswith("packet.json"):
                    value = copy.deepcopy(self.packet); value["focus"]["arabic_uthmani"] = "changed"
                    path.write_bytes(reading.encode(value))
                elif name.endswith("reading.json"):
                    value = copy.deepcopy(self.plan); value["batches"].pop()
                    path.write_bytes(reading.encode(value))
                else:
                    path.write_bytes(b"Different instructions")
                with self.assertRaises(reading.ReadingError):
                    discovery.Session(self.plan_path, raw_root=self.root / "raw")
                path.write_bytes(original)

    def test_finish_preserves_exact_agent_wording_and_refuses_changed_output(self):
        work = self.completed_work()
        self.session.finish()
        original = self.session.output_path.read_bytes()
        self.assertEqual(json.loads(original), work["discovery"])
        self.session.finish()
        self.assertEqual(self.session.output_path.read_bytes(), original)
        work["discovery"]["findings"][0]["title"] = "Changed after finalization"
        self.session.save(work)
        for action in (self.session.check, self.session.finish):
            with self.assertRaisesRegex(discovery.DiscoveryError, "different final"):
                action()
        self.assertEqual(self.session.output_path.read_bytes(), original)

    def test_unresolved_lead_must_remain_in_final_friction_notes(self):
        work = self.completed_work()
        work["leads"] = [{"lead_id": "L1", "note": "Uncertain contact", "source_pointers": ["/focus"],
            "status": "unresolved", "resolution": "The comparison remains uncertain", "finding_refs": []}]
        self.session.save(work)
        with self.assertRaisesRegex(discovery.DiscoveryError, "friction_notes"):
            self.session.finish()
        work["discovery"]["friction_notes"].append(work["leads"][0]["resolution"])
        self.session.save(work)
        self.session.finish()

    def test_context_listing_does_not_replace_a_grounded_trigger(self):
        result = discovery_fixture()
        result["findings"][0]["branch_activations"][0]["trigger_refs"] = ["1:1:1:1"]
        with self.assertRaisesRegex(discovery.DiscoveryError, "context_exclusions"):
            discovery.validate_discovery(self.packet, result)

    def test_exact_source_and_candidate_obligation_checks(self):
        for mutate in (
            lambda r:r["candidate_decisions"].clear(),
            lambda r:r["findings"][0]["semantic_obligation_refs"].clear(),
            lambda r:r["findings"][0]["branch_activations"][0].update(facet_statement="paraphrase"),
            lambda r:r["findings"][0]["branch_activations"][0].update(focus_return_refs=["1:1"]),
            lambda r:r["findings"][0]["evidence_facts"][0].update(source_pointer="/focus/arabic_uthmani"),
        ):
            result = discovery_fixture(); mutate(result)
            with self.assertRaises(discovery.DiscoveryError):
                discovery.validate_discovery(self.packet, result)

    def test_uncandidate_finding_is_allowed(self):
        packet, result = copy.deepcopy(self.packet), discovery_fixture()
        packet["candidate_inventory"] = []
        result["candidate_decisions"] = []
        result["findings"][0].update(origin_candidate_id=None, semantic_obligation_refs=[])
        discovery.validate_discovery(packet, result)

    def test_basmala_alias_uses_its_named_context_host_only(self):
        packet, result = copy.deepcopy(self.packet), discovery_fixture()
        packet["identity"] = {"ayah_ref": "2:1", "lane": "global", "linguistic_source_ref": "2:1"}
        packet["focus"]["qac_morphemes"] = [{"qac_ref": "2:1:1:1", "qac_word_ref": "2:1:1"}]
        packet["context_evidence"] = [{"ayah_ref": ref, "linguistic_source_ref": "1:1",
            "morphemes": [["1:1:1:1", "بِ"]]} for ref in ("29:0", "87:0")]
        packet["candidate_inventory"][0]["required_context_refs"] = ["29:0"]
        result["ayah_ref"] = "2:1"
        result["findings"][0]["context_refs"] = ["29:0"]
        result["findings"][0]["branch_activations"][0].update(
            carrier_refs=["2:1:1:1"], trigger_refs=["1:1:1:1"], focus_return_refs=["2:1:1:1"])
        discovery.validate_discovery(packet, result)


if __name__ == "__main__":
    unittest.main()
