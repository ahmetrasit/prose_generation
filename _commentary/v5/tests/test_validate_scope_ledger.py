from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).resolve().parents[1] / "validate_scope_ledger.py"
SPEC = importlib.util.spec_from_file_location("validate_scope_ledger", MODULE_PATH)
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


class ScopeLedgerValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.discovery = {
            "ayah_ref": "29:38",
            "lane": "macro",
            "findings": [
                {
                    "finding_ref": "macro:test",
                    "claim": "claim",
                    "mechanism": "mechanism",
                    "reader_payoff": "payoff",
                    "containment": "boundary",
                    "semantic_obligation_refs": ["obl_1"],
                    "branch_activations": [{"branch_ref": "root_1/B001"}],
                    "connection_refs": ["conn_1"],
                    "context_refs": ["29:41"],
                }
            ],
        }
        self.prose = (
            "İlk paragraf temel iddiayı ve sınırını açıkça kurar.\n\n"
            "İkinci paragraf bağlamdaki hareketi ayrıntılı biçimde açıklar."
        )
        self.ledger = {
            "schema_version": validator.SCHEMA_VERSION,
            "ayah_ref": "29:38",
            "lane": "macro",
            "findings": [
                {
                    "finding_ref": "macro:test",
                    "landings": [
                        {
                            "movement_refs": [
                                "discovery:claim",
                                "discovery:mechanism",
                                "discovery:reader_payoff",
                                "discovery:containment",
                            ],
                            "paragraph": 1,
                            "anchor": "temel iddiayı ve sınırını açıkça kurar",
                        },
                        {
                            "movement_refs": [
                                "obligation:obl_1",
                                "activation:0",
                                "connection:conn_1",
                                "context:29:41",
                            ],
                            "paragraph": 2,
                            "anchor": (
                                "İkinci paragraf bağlamdaki hareketi ayrıntılı biçimde açıklar"
                            ),
                        },
                    ],
                }
            ],
        }

    def test_accepts_complete_ordered_ledger(self) -> None:
        self.assertEqual(validator.validate(self.discovery, self.ledger, self.prose), [])

    def test_rejects_missing_movement(self) -> None:
        self.ledger["findings"][0]["landings"][1]["movement_refs"].pop()
        codes = {item.code for item in validator.validate(self.discovery, self.ledger, self.prose)}
        self.assertIn("movement_coverage", codes)

    def test_rejects_unknown_or_reordered_movement(self) -> None:
        refs = self.ledger["findings"][0]["landings"][1]["movement_refs"]
        refs[0] = "activation:99"
        codes = {item.code for item in validator.validate(self.discovery, self.ledger, self.prose)}
        self.assertIn("movement_coverage", codes)

    def test_rejects_anchor_in_wrong_paragraph(self) -> None:
        self.ledger["findings"][0]["landings"][0]["paragraph"] = 2
        codes = {item.code for item in validator.validate(self.discovery, self.ledger, self.prose)}
        self.assertIn("anchor_paragraph", codes)

    def test_rejects_heading_or_label_anchor(self) -> None:
        self.ledger["findings"][0]["landings"][0]["anchor"] = (
            "Yerleşmiş yapı yine de çökebilir:"
        )
        codes = {
            item.code
            for item in validator.validate(self.discovery, self.ledger, self.prose)
        }
        self.assertIn("anchor", codes)

    def test_rejects_short_anchor(self) -> None:
        self.ledger["findings"][0]["landings"][0]["anchor"] = "temel iddia burada"
        codes = {
            item.code
            for item in validator.validate(self.discovery, self.ledger, self.prose)
        }
        self.assertIn("anchor", codes)


if __name__ == "__main__":
    unittest.main()
