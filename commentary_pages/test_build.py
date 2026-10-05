#!/usr/bin/env python3
import json
import tempfile
import unittest
from pathlib import Path

import build


class BuildSiteTests(unittest.TestCase):
    def write(self, root: Path, rel: str, text: str) -> Path:
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def test_scans_historical_current_future_and_enrichment(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.write(root, "_commentary/v11/out/s001/1_1/1_1.reading.tr.md", "# v11\n{ar:ا, tr:a, gloss:x}")
            self.write(root, "_commentary/v13/out-v3/s001/1_5/1_5.reading.tr.md", "# v13")
            self.write(root, "_commentary/v15/out/s001/1_1/commentary.tagged.tr.md", "# v15\n{ar:ب, tr:b, gloss:y}")
            self.write(root, "_commentary/v16/out/s001/1_1/augment.augment9.opus/1_1.reading.tr.md", "# v16 augment9")
            self.write(root, "_commentary/v16/out/s001/1_1/commentary.tr.md.prompt.md", "SECRET PROMPT")
            self.write(root, "_commentary/v17/out/s001/1_2/commentary.tr.md", "# future")
            self.write(root, "enrichment/v2/schema.json", json.dumps({"fields":{"tur":{"enum":"tur"}},"enums":{"tur":{"hadis":{"label":{"tr":"Hadis"}}}}}))
            self.write(root, "enrichment/v2/out/s001/1_1.md", '# enriched\n{tur:hadis, kat:temel, metin:"x", kaynak:"MUSLIM:1"}')

            out = root / "site"
            manifest = build.build(root, out)
            versions = {e["version"] for e in manifest["entries"]}
            self.assertTrue({"v11","v13","v15","v16","v17","enrichment-v2"}.issubset(versions))
            self.assertEqual(manifest["newest_commentary_version"], "v17")
            self.assertFalse(any("source_path" in e for e in manifest["entries"]))
            self.assertFalse(any("prompt" in e["content_path"].lower() for e in manifest["entries"]))
            self.assertTrue((out / "data" / "schema.json").exists())
            self.assertTrue((out / "app.js").exists())
            self.assertIn("out-v3", {e["variant"] for e in manifest["entries"] if e["version"] == "v13"})

    def test_newly_pushed_lower_number_version_is_still_discovered(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.write(root, "_commentary/v9/out/s001/1_1/commentary.tr.md", "# v9")
            self.write(root, "_commentary/v16/out/s001/1_1/commentary.tr.md", "# v16")
            manifest = build.build(root, root / "site")
            self.assertEqual({e["version"] for e in manifest["entries"]}, {"v9", "v16"})

    def test_final_enrichment_is_published_but_pending_placeholder_is_not(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.write(root, "_commentary/v16/out/1_1/DM.r13/augment.augment9.opus/1_1.reading.tr.md", "# v16 augment9")
            self.write(root, "enrichment/v1/out/1/1-1enriched.md", "<!-- Enrichment pending. Target: 1:1. -->\n")
            self.write(root, "enrichment/v1/out/1/1_enriched.md", '{type:hadith, priority:core, prose:"full enrichment", source:"X"}')
            self.write(root, "enrichment/v2/schema.json", json.dumps({"fields":{},"enums":{}}))

            manifest = build.build(root, root / "site")
            enrich = [e for e in manifest["entries"] if e["family"] == "enrichment"]
            self.assertEqual(len(enrich), 1)
            self.assertEqual(enrich[0]["version"], "enrichment-v1")
            self.assertEqual(enrich[0]["surah"], 1)
            self.assertIsNone(enrich[0]["ayah"])
            self.assertEqual(enrich[0]["scope"], "surah")
            self.assertEqual(enrich[0]["variant"], "enriched surah")
            self.assertTrue(any("augment9" in e["variant"] for e in manifest["entries"]))
            self.assertEqual(manifest["format"], 2)


if __name__ == "__main__":
    unittest.main()
