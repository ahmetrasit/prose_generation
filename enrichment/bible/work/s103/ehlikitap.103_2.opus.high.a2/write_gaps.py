"""Format-only helper: my gap notes plus the prefetch report's missing list copied verbatim."""
import json
from pathlib import Path

D = Path(__file__).resolve().parent
PRE = json.loads(Path("/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/discovery/s103-20261009/prefetch.json").read_text())

missing_sources = [
    "Peshitta (Syriac Bible) is not in the intertext corpus: the Syriac ḥsar (Luke 9:24-25) and ḥusrānā (Phil 3:7-8) are reported only through Corpus Coranicum (CORPUSCORANICUM-INTERTEXT:103:2:178, :179), not checked in a Syriac witness.",
    "Septuagint is not in the corpus (e.g. the Greek of Ps 8:6, Ps 49:12, Dan 5:27 could not be compared).",
    "Patristic and Syriac homiletic texts are not in the corpus; no Christian interpretation of the parallels (Luke 9:25, Luke 12, Dan 5) is cited.",
    "Targum, midrash and classical commentary on the WLC verses were not fetched (prefetch limitation: related_fetched false); absent interpretations are unfetched, not nonexistent.",
    "Modern studies on Qur'anic 'loss' vocabulary beyond what Corpus Coranicum quotes (Torrey 1892 itself, Robinson 2003, Neuwirth) are not held locally.",
    "BDB in this edition shows Arabic script only as a placeholder: for אנש 'be inclined, friendly, social' and for אישׁ the Arabic words themselves cannot be read.",
    "Prefetch report: works the discovery readers named that the corpus does not hold (copied verbatim): " + " | ".join(PRE["missing"]),
]
missing_sources += PRE["missing"]

not_found = [
    "Sirach 11:19: SEFARIA:Ben_Sira.11.19 exists but under Sefaria's Hebrew numbering is a different saying; the rich man's 'I have found rest' saying (Greek Sir 11:18-19) is not in the corpus; SEFARIA:Ben_Sira.11.17, SEFARIA:Ben_Sira.11.18, SEFARIA:Ben_Sira.11.20 NOT FOUND.",
    "SEFARIA:Pirkei_Avot.1.13 NOT FOUND (only needed to confirm the Hillel sequence 1:12-14).",
    "SEFARIA:Pirkei_Avot.3.13 NOT FOUND (needed to confirm the speaker of 3:16; the block therefore names no rabbi).",
    "Didache 1.1 / Didache 1:1, Epistle of Barnabas 18:1, Gospel of Thomas 3, Gospel of Thomas 63: discovery candidates for this page with no corpus text (prefetch gaps).",
]
gaps = {"missing_sources": missing_sources, "not_found": not_found, "unresolved": [],
        "notes": ["Three early shell calls joined a corpus get with another command by ';' (against the one-at-a-time rule); the lookup audit may read the extra tokens (python3, word, the tool paths) as locators. They are recorded in verdicts.jsonl as non-passages."]}
(D / "gaps.json").write_text(json.dumps(gaps, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(missing_sources), len(not_found))
