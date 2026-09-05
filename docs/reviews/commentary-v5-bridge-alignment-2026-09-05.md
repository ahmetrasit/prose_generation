The word-analysis/QAC join now uses the accepted mappings in the frozen
`quran-data/data/bridges/qac-masaq.sqlite.gz` release. The earlier ordered
resolver imposed exclusive morpheme ownership on a many-to-many identity model.
That left the separate pronoun analysis in 29:38 unresolved even though the
source bridge explicitly links both `لَهُمُ` and its component `هُمُ`.

All 23 analysis entries in 29:38 now have accepted links. The complete expression
maps to `29:38:9:1–2`; its pronoun analysis maps to `29:38:9:2`. Original analysis
identities, wording, topic decisions and source obligations remain unchanged.

The shared adapter verifies release checksums, SQLite version, release metadata,
the complete word-analysis source tree, each focus's released analysis, and its
canonical QAC rows. Compressed databases use the streamed disk cache and one
verified connection per process. Bundles carry stable logical provenance and
checksums. Preparation checks the complete mapping against that bridge before
accepting overlaps; an arbitrary reused reference or a bridge label alone does
not authorize a join. Legacy spans retain their earlier strict validator.

Each V5 word candidate receives an explicit `word_alignment` with the analysis
identity, canonical morpheme refs and acceptance/exclusion status. Three concise
prompt lines explain that whole-expression/component analyses may overlap and
that shared morphology alone does not make their semantic claims duplicates.

Independent inspection of actual rendered prompts also uncovered an inherited
omission in the preparer: analysis IDs were incorrectly bounded by the length
of the analysis array. Sparse source IDs therefore caused late topics to be
excluded. The corrected preparer uses bridge-verified analysis identities in
their own namespace. V5 now refuses preparation when the delivered word-topic
inventory differs from the source. This restores 19 topics in 5:3, 46 in 12:31,
and 45 in 24:31: 110 unique topics, or 155 including saved package copies.
These are restored agent inputs; no claim is made that a new prose finding was
generated or evaluated in this repair.

All 3,086 saved ayah inputs were migrated, along with 69 surah coverage summaries
and the existing package manifest. A subsequent pass found zero stale bundle or
surah mappings. Of 42,140 analysis entries, 42,138 have accepted links. The two
remaining entries are copies of the single upstream duplicate `17:28:12`, which
the bridge explicitly excludes as a source defect. Its analysis and exclusion
reason remain visible. Excluded entries are never assigned guessed QAC links.

An independent comparison against Git checked all 3,155 ayah/surah JSON files:
every field outside derived spans and alignment coverage was preserved. The
inventory contains 144,237 word topics and no word entries without topics.
Agent outputs and saved prompts were not edited.

The full preparation sweep covered 5,322 saved focus/configuration pairs,
including pericope copies and every numbered canonical focus with whole-surah
context. The audit decoded the actual serialized lane packets and checked topic
delivery, full word/topic support fields, and exact QAC links against the source.
Its five sparse-ID failures were rechecked after the correction. **All 5,318
supported configurations pass.** The four existing native basmala focuses 5:0,
12:0, 18:0 and 22:0 still require their numbered host inputs assembled in one
context root. Their use as context in existing numbered packages remains valid.
The merged results retain the initial sparse-ID errors and their successful
rechecks; the sweep's unaffected successful evidence checks remain applicable.

Fresh generation independently covered a complete surah 100 root, including its
prefatory unit, and a 29:28–44 pericope package. All 29 new inputs passed actual
preparation and serialized evidence-delivery checks. Supplemental checks passed:
8 bridge integration regressions, 34 builder tests, 74 V3 preparation tests and
89 V5 tests. The measured largest lane was about 7.5 MB, within the 16 MB file
guard; this does not establish single-turn model-context fit or semantic quality.

The adjacent JSON records code hashes and exact audit counts. Full configuration
results are in `commentary-v5-bridge-preparation-2026-09-05.jsonl.gz`. Repeat the
inventory migration audit and preparation checks with the commands documented
in `_commentary/v5/README.md`.
