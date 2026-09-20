# Fâtiha concise editorial layer

This directory contains a shorter, exhaustive-by-source-paragraph edition of
the seven completed Turkish V5 ayah editorials from analysis
`s001-fresh-20260910`.

## Citation contract

A source paragraph is a non-heading Markdown block in the corresponding file
under `_commentary/v5/editorial/s001-fresh-20260910/s001/`. Paragraphs are
numbered from 1 independently inside each ayah file; headings do not consume a
number. A citation such as `(1:4 ¶12, ¶15, ¶16, ¶17)` therefore identifies the
exact editorial paragraphs used at that point in the concise prose.

Every reader-facing prose paragraph has at least one such citation, and every
one of the 492 source paragraphs is cited at least once. This establishes
paragraph-level provenance only. It does not prove that every semantic unit
inside a cited paragraph survived: the current layer is a compact digest and
must not be treated as a lossless replacement for the editorial prose.

## Files

- `1_1/1_1.prose.concise.tr.md`
- `1_2/1_2.prose.concise.tr.md`
- `1_3/1_3.prose.concise.tr.md`
- `1_4/1_4.prose.concise.tr.md`
- `1_5/1_5.prose.concise.tr.md`
- `1_6/1_6.prose.concise.tr.md`
- `1_7/1_7.prose.concise.tr.md`

The source files total 492 prose paragraphs and 64,566 whitespace-delimited
words. This layer is about 10,200 words: substantially shorter, but too
compressed to warrant a claim of detail-complete preservation. It remains an
ayah-by-ayah digest rather than the selective whole-surah synthesis in
`_surah_commentary/v2/outputs/s001/`.

## Validation

Run both checks from the repository root:

```sh
python3 -B _commentary/v5/validate_concise.py \
  --analysis-id s001-fresh-20260910 --surah 1 --ayah-count 7
python3 -B _commentary/v5/validate_prose.py \
  _commentary/v5/concise/s001-fresh-20260910/s001/*/*.prose.concise.tr.md
```

The concise validator checks stable paragraph numbering, citation syntax,
complete source-paragraph coverage, ayah identity, bounds, and that each output
is shorter than its source. These are mechanical checks; semantic preservation
still depends on editorial review against the cited source paragraphs.
