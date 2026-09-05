**V5 bundle migration and preparation audit — 2026-09-05**

The previous review overstated bulk readiness. It exercised representative
preparations and compared transported evidence, but did not inventory every
stored input against the consumer's span contract. It also did not distinguish
a valid join inventory from a complete one. Passing code tests did not establish
that old generated bundles had been migrated.

Of 2,236 existing numbered canonical bundles, 742 lacked the required skip
count and 30 had invalid or reused QAC lineage. Another 280 bundles passed
that contract while still containing unresolved analytic words. These were
inherited input/resolver problems, not regressions in the QAC cache.

The repair uses one shared resolver for ayah, prefatory, whole-surah, and
pericope generation. It aligns against the whole ordered ayah and returns a
join only when every optimal alignment agrees on that span. It preserves QAC
word boundaries and attaches elided morphemes to their own preceding surface.
Matching handles annotation-derived spelling variants, contracted articles,
typed contractions and suffixes, and hamza spellings without rewriting source
words or upstream identifiers. Final maqsura and consonantal waw remain
distinct: `إلى` must not match `إلا`, and `وَٰحد` must not match `أحد`.

`scripts/migrate_bundle_spans.py` regenerates only the deterministic spans and
their coverage. It validates proposed joins before writing, preserves unrelated
fields, refreshes copied surah coverage, and updates existing package manifests
with explicit migration provenance. New manifests bind the alignment module's
content hash as well as the bundle builder. Migration also detects stale
implementation records when the derived bundle contents are unchanged.

The original inventory contained 3,082 ayah files: 2,304 canonical files
(including 68 prefatory units) and 778 copies in 38 pericope collections. All
3,082 were migrated, along with 69 surah coverage summaries and the existing
pericope manifest. Independent comparison against Git confirmed that every
other field in those ayah and surah files was preserved. Saved prompts and
agent outputs were not edited.

Actual preparation additionally exposed missing mandatory host basmala inputs
for the s005, s012, s018 and s022 package collections. These four inputs were
generated with the existing basmala builder. Their word analysis and QAC records
exactly match canonical 1:1; their host-conditioned evidence is loaded from the
existing sources. They support numbered package focuses. Their own prefatory
focus still requires a complete host context, as it does for every S:0 run;
those four surahs currently store their numbered inputs in pericope collections
rather than canonical whole-surah directories.

The full preparation sweep also exposed a producer/validator mismatch at 53:1,
69:21 and 88:9. The earlier `demote_unresolved_mandatory_candidates` option retained
unresolved word topics as optional review entries while preserving their source
obligations, but the validator still required those entries to be mandatory.
The validator now recognizes the explicit non-adjudicable state. Unresolved
citations, source obligations, and selection-ineligibility remain intact;
strict preparation without that authoring option still rejects unresolved
mandatory topics. This repair changes code, not the source analyses.

All 3,086 current input files pass the strict span contract. Across 42,140
analytic word rows, 42,025 resolve and 115 remain explicitly qualified in 93
files, including copied packages. The canonical subset contains 73 unresolved
rows in 57 files. Eighteen unresolved rows have competing optimal alignments;
20 rows in 16 files have no upstream TSV morpheme rows for their ayah. The
remaining rows include overlapping or differently segmented analytic units and
unmatched spellings. These are not silently assigned guessed identities.

For 29:38, the new resolver joins 22 of 23 analytic units. The additional
standalone `هُمُ` overlaps the earlier `لَهُمُ` analysis and remains qualified.
The prepared discovery inventory still contains all 92 candidates and 269
connections. Every new lane packet exposes `focus_word_alignment`; the prompt
instructs agents to inspect the available Arabic and morphology, preserve the
source reading, and qualify an uncertain carrier rather than infer a QAC join
from upstream numbering.

Independent QAC comparison checked all 3,086 embedded inventories against the
canonical database: refs, surfaces, POS, roots, lemmas, morpheme roles and
morphological features all matched, including the complete ordered row sets.
An exhaustive small-sequence comparison checked the alignment algorithm against
all valid ordered assignments for 256 source/target pairs. Focused regressions
cover repeated analytic units, the contracted article before the later `لَ` in
49:3, spelling distinctions, and elided suffix boundaries.

Fresh generation was also exercised independently of migration: a complete
surah 100 root (including 100:0) and a 29:28–44 pericope package. All 29 resulting
units passed actual preparation in their appropriate context configurations.

`prepare --check-only` assembles and renders the same three prompts and applies
the same evidence and size checks before returning `checked`. It creates no
prompt files or agent handoffs. `_commentary/v5/audit_preparation.py` applies
that path to the full saved inventory and optionally every numbered canonical
focus with its whole surah as context. JSONL results retain failures and actual
prompt sizes. This is a repeatable input/readiness audit, not a semantic-quality
test or a claim that a model can consume an entire large packet in one turn.

The completed sweep covered **5,318 original focus/configuration pairs**:
2,304 native canonical units, 778 pericope copies, and 2,236 numbered canonical
focuses with explicit whole-surah context. It initially recorded 37 failures:
31 package checks encountered the missing host input before it was generated,
and six checks exposed the three unresolved-topic contract mismatches. Every
failed configuration was rechecked after repair; all 5,318 now pass. The four
new host-context inputs retain the separate S:0 layout qualification described
above. The full results are retained in
`commentary-v5-preparation-2026-09-05.jsonl.gz`; the adjacent migration JSON
contains counts, code hashes, QAC cross-check results and remaining input gaps.

The largest measured prompts were 3,738,580 bytes in micro and 3,253,506 bytes
in macro (73:20 with whole-surah context), and 7,459,475 bytes in global (22:5
in its pericope package). No checked lane exceeded 16 MB. Supplemental checks
passed: 34 bundle-builder tests, 74 preparation tests and 89 V5 tests. The
inventory checks and independent source comparisons are the primary evidence.

Complete inline evidence records are retained. The prompt-size increase from
removing generic `$v5_ref` lookups remains a deliberate reading-cost tradeoff.
The 16 MB guard is a file-size bound, not a model-context guarantee. Linux/macOS
remain the supported preparation platforms.
