#!/usr/bin/env python3
"""Check discovery references and Arabic wording locally, without model calls.

Unmatched spans are review findings, not automatic rejection: notes may name
roots or dictionary forms. This checks wording, not the truth of the explanation.
"""
import argparse
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

import discover as D

ARABIC = re.compile(r"[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+(?:[ \t]+[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+)*")


def normalize(text):
    text = unicodedata.normalize("NFKD", text).replace("ٱ", "ا").replace("ـ", "")
    return " ".join("".join(c for c in text if c.isspace() or
                            (unicodedata.category(c).startswith("L") and
                             "ARABIC" in unicodedata.name(c, ""))).split())


def check(path, surah, verses):
    rows, bad = D.parse_rows(path, surah, verses)
    normalized = {ref: normalize(text) for ref, text in verses.items()}
    findings = []
    for row in rows:
        for match in ARABIC.finditer(row["note"]):
            wording = normalize(match.group())
            if not wording or f" {wording} " in f" {normalized[row['ref']]} ":
                continue
            elsewhere = [ref for ref, text in normalized.items()
                         if f" {wording} " in f" {text} "] if len(wording.split()) >= 2 else []
            findings.append({"line": row["line"], "ref": row["ref"], "arabic": match.group(),
                             "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form",
                             "matching_refs": elsewhere[:20], "matching_ref_count": len(elsewhere)})
    counts = Counter(row["ref"] for row in rows)
    return {"file": str(path), "rows": len(rows), "schema_errors": bad,
            "duplicates": {ref: n for ref, n in counts.items() if n > 1},
            "arabic_findings": findings,
            "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. "
                      "No semantic or relevance validation."}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", type=Path)
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    report = check(args.path, args.surah, D.M.verses())
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(f"{args.path}: {report['rows']} rows; {len(report['schema_errors'])} schema errors, "
          f"{len(report['duplicates'])} duplicate refs, {len(report['arabic_findings'])} Arabic spans to review")
    if report['schema_errors'] or report['duplicates']:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
