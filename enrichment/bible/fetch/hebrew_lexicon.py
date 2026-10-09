#!/usr/bin/env python3
"""Open Scriptures Hebrew Lexicon (github.com/openscriptures/HebrewLexicon, CC BY 4.0) for the Bible pass's root and
cognate layer (enrichment/bible/hebrew.py). Three XML files cached once under corpus/HEBLEX/raw/; kind `lexicon`, so
the intertext index never holds it. Then run `hebrew.py build`.

  python3 -B enrichment/bible/fetch/hebrew_lexicon.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from enrichment.bible.fetch.ref_common import Source  # noqa: E402

FILES = ("LexicalIndex.xml", "BrownDriverBriggs.xml", "HebrewStrong.xml")
BASE = "https://raw.githubusercontent.com/openscriptures/HebrewLexicon/master/"
META = {"id": "HEBLEX", "title": "Open Scriptures Hebrew Lexicon: Lexical Index, Brown-Driver-Briggs, Strong's",
        "author": "Open Scriptures (BDB 1906 and Strong 1890, digitised)", "death_ah": None, "kind": "lexicon",
        "gelenek": ["tevrat"], "tradition": "Hebrew Bible (lexicon)", "language": "he",
        "edition": "openscriptures/HebrewLexicon master", "access": "yerel", "locator": "lexicon",
        "licence": "CC BY 4.0 (Open Scriptures); local research copy",
        "notes": "FOR THE BIBLE PASS ONLY, via hebrew.py: WLC lemma (Strong's + augment letter, as in morphhb) -> "
                 "lexicon entry -> root; BDB entry heads keep cognate glosses but this digital edition replaces the "
                 "Arabic, Syriac, Ethiopic … script with a placeholder word ('Arabic'), so a cited cognate word "
                 "itself is not available here.",
        "coverage": "Hebrew and Biblical Aramaic lexicon entries; BDB fully tagged only in part",
        "urls": [BASE + f for f in FILES]}


def main() -> None:
    src, failed = Source("HEBLEX"), []
    for f in FILES:
        st, body = src.fetch(BASE + f, f)
        if st != 200 or not body:
            print(f"FETCH FAILED: HEBLEX {f} (status {st})", file=sys.stderr)
            failed.append(f)
    if failed:
        raise SystemExit(f"HEBLEX incomplete: {', '.join(failed)}")
    src.update_source(META, urls=META["urls"])
    print(f"HEBLEX: {len(FILES)} files in {src.raw}")


if __name__ == "__main__":
    main()
