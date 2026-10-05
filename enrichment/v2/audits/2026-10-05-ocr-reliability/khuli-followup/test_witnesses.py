"""Protect omission detection and alignment coordinate accounting."""
import itertools
import runpy
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
align = runpy.run_path(str(HERE / "compare_witnesses.py"))["align"]
baseline = runpy.run_path(str(HERE.parent / "luna-pilot/measure.py"))["alignment"]


class WitnessAlignmentTests(unittest.TestCase):
    def test_short_sequences_preserve_both_witnesses(self):
        seqs = [list(x) for n in range(4) for x in itertools.product(("a", "b"), repeat=n)]
        for a in seqs:
            for b in seqs:
                for substring in (False, True):
                    result = align(a, b, substring=substring)
                    steps = result["steps"]
                    self.assertEqual(result["distance"], baseline(a, b, substring=substring)["distance"])
                    self.assertEqual(sum(s["op"] != "equal" for s in steps), result["distance"])
                    self.assertEqual([s["a_text"] for s in steps if s["a"] is not None], a)
                    self.assertEqual([s["b_text"] for s in steps if s["b"] is not None], b[result["start"]:result["end"]])

    def test_missing_sol_word_retains_gap_for_review(self):
        result = align(["before", "after"], ["before", "missing", "after"])
        changes = [s for s in result["steps"] if s["op"] != "equal"]
        self.assertEqual(len(changes), 1)
        self.assertEqual((changes[0]["op"], changes[0]["a_gap"], changes[0]["b_text"]), ("insert", 1, "missing"))


if __name__ == "__main__":
    unittest.main()
