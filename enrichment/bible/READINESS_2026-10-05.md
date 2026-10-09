# Bible pathway readiness — 2026-10-05 (updated 2026-10-09)

## 2026-10-09: Claude Code route, r13 ayah base, Hebrew root layer; S103 in production

The pathway now runs from a Claude Code session (RUNBOOK "Production route", DECISIONS 2026-10-09): ayah pages
on the frozen r13 readings (the v9 Islamic pages' paragraphs), a Hebrew/Aramaic root and cognate layer
(`hebrew.py`, Open Scriptures lexicon) with a per-target Semitic root table and a checked decision per Arabic
root, Luna max + Sol high readers through `codex exec` (`discovery_exec.py`), and Sol max image authors through
`codex exec` (`image_enrich.py run`). 89 distinct tests pass (65 workflow, 14 image, 10 Semitic/exec).
S103: discovery done (36 sessions, 5,415 connections, $8.91 API-equivalent; audits/s103-discovery-20261009),
prefetch of the named Jewish works done (2,582 candidates, 162 gaps, 0 errors; no per-verse Sefaria links),
surah page accepted (15 Sol max image authors, 207 annotations of which 47 shared-root blocks, 4,479 verdicts,
$54.27; audits/image-s103-s103-20261009). The three Opus high ayah pages are accepted (65, 48 and 65 blocks;
1,263 verdicts; $22.96; audits/ayah-s103-20261009), after an operator review of their extra tool use and two
no-model re-audits. Editorial review of the accepted prose is still to do.

The S87 surah pilot is now accepted: **18 Sol max image authors, 346 annotations
and 3,703 judgments** across all 73 original r13 commentary paragraphs. The
[accepted page and evidence](audits/image-s087-session-20261005/README.md) retain
all 3,523 image discovery connections and 180 additional research/context
decisions. The local snapshot supplied 1,605 distinct candidate references;
282 remained unavailable. Every image passed native execution, frozen-input,
source-evidence, coverage and placement checks. All final annotation prose and
278 tagged original-language quotations were reviewed; the original commentary
is preserved.

The S1 surah pilot is also accepted: **14 Sol max image authors, 340 annotations
and 4,030 judgments**, with the original r13 commentary preserved. See the
[accepted page and evidence](audits/image-s001-session-20261005/README.md).
Its 3,817 discovery connections came from the completed S1 two-reader discovery
pilot, which also covered all seven ayat. The page pilot used local witnesses;
313 distinct candidate references remained unavailable and no network expansion
was attempted. Missing evidence is retained in its gap ledger.

The [saved decision](DECISIONS.md) makes original completed r13 image commentary
the surah Bible target; image augment9s is optional and later additions can receive
a separate pass. Ayah enrichment still uses completed augment9 ayah commentary.
This session uses one Sol max author per image. The default page-author model is
unchanged for other runs. The current Bible suite passes 79 distinct tests
(65 shared Bible workflow tests and 14 image-author tests).

S87 discovery has completed all 148 turns across 18 images and 19 ayat
(74 Luna/Terra max sessions). All 74 now pass discovery validation, after the
user-approved nine wave1 and three wave2 locator corrections. The original raw
evidence and failed validations remain intact. The
[S87 audit](audits/s087-prepared-20261005/README.md) preserves the full batch and
repair history. Its 7,664 candidate connections cover all 37 targets. All 38
handoffs are now merged and selected: 18 images, 19 ayat and the combined surah.
The image-author archive preserves those handoffs and their discovery provenance.
S1 and S87 ayah page authors, broader source coverage and reader publication remain
separate work. Neither pilot has been published to the reader.

## Earlier implementation-readiness assessment (before the live pilot)

The following is the historical assessment made before native discovery began.

**Local implementation and offline checks are ready for a live pilot. Production
content readiness is still pending that pilot.** S1 page preflight correctly
reports `ready: false` because no native Bible discovery sessions have completed.
No production Bible annotations have been accepted and no model calls were made
as part of this repair.

The agreed v16 Step 2b alignment is now implemented within this directory: fuller
discovery coverage, both-reader enforcement, raw proposal/review provenance,
recorded reference repairs, reporting and complete per-connection verdicts. The
Hebrew/Greek corpus rules, frozen augment9 base and single author per page remain
the research design. See [the alignment record](STEP2B_ALIGNMENT_2026-10-05.md).

## Isolation

The implementation is in `enrichment/bible/`, with its own corpus, index, schema,
fetchers, pack builder, discovery lifecycle, page lifecycle, validators, renderer,
prompts, work directories and outputs. There are no imports from `enrichment/v2`
or `_commentary` helper modules.

The two Bible-specific entrypoints under `_commentary/v16/` delegate to this
implementation. Shared enrichment code, schemas, prompts and fetchers have no
diff from this work. Other ongoing enrichment work and its ledger were left alone.
The legacy shared Bible commands are superseded by the commands in this
directory's [runbook](RUNBOOK.md).

Before/after SHA-256 and modification-time checks found no changes in 93 upstream
input files: the shared Islamic and intertext indexes, shared WLC segments and the
shared S1 pack. Bible pack construction and optional assembly of accepted layers
read upstream files but write only Bible-owned files.

## Repairs and verification

| Finding | Implemented behavior |
| --- | --- |
| Hebrew reading notes inserted into verse text | Direct verse words form the ketiv stream; readings and note positions are separate. All 23,213 cached XML verses were checked for preservation of note word counts. The old recursive extraction affected 1,102 verses with words inside notes. |
| Bible IDs rejected; Islamic-only schema card | Own TEV/INC ID validation and generated Bible card; actual PRL/MTF type codes. |
| Ayah prompt named a nonexistent input | Prompts use the actual Bible-owned `numbered/1_1.md`, its Arabic input and matching schema. |
| Discovery used an earlier reading | Both discovery and page author use the same frozen augment9 ayah base. |
| Surah discovery had no page-level handoff | All completed image sections form `surah.merged.tsv` and an explicit selected handoff. |
| Follow-up could overwrite first-turn candidates | First-turn snapshot, separate follow-up proposals, unique consolidation, session auditing and hash checks. Distinct link reasons survive merging. |
| Failed discovery could be consumed | Matching native runner, target, model, effort, successful two-turn completion and reviewed audit are required. |
| Retrieval failures disappeared | Prefetch records resolutions, gaps and errors; errors block page start. Index/source/metadata hashes must match after prefetch. |
| Mixed collections inherited the wrong tradition | Segment-level classification for KJV and Corpus Coranicum; unsupported background material cannot become a scripture parallel. |
| English could stand in for an available original | Canonical Bible link records require an original witness alongside KJV; cited witness tags are checked. |
| Every record could fail while the page succeeded | All-dropped results fail. A deliberately empty page requires an explicit reason. |
| Mutable annotations or changed bases entered merges | Accepted annotation snapshots and page/base hashes are checked; duplicate IDs fail; accepted source descriptions survive the merge. |
| Shared run safeguards omitted Bible work | Dedicated active-call guards and frozen input checks protect Bible packs, discovery, sources and indexes. |
| Page output could lack trustworthy execution evidence | Exactly one completed native page transcript is required; wrong models and tool use outside the Bible call rules fail. |

Verification completed:

- **54 Bible regression tests passed**, using temporary fixtures, mocked native
  session evidence and mocked HTTP. The original repair suite contained 27 tests;
  the expanded suite covers the Step 2b protocol and verdict requirements too.
- The initial repair also passed **7 existing Quran-discovery tests**, with their
  implementation unchanged; this alignment modifies only Bible files.
- All Bible Python modules parse and have no imports of shared workflow helpers.
- Actual Hebrew `בראשית` searches resolve WLC verses; Greek `πατερ` searches resolve
  SBLGNT verses. Displayed passages preserve Hebrew pointing and Greek accents.
- Ezekiel 1:8 displays the written `וידו` in the main stream and its `וִידֵ֣י`
  reading separately at word position 1. Across WLC, 3,657 verses contain some kind
  of note; not all of those notes contain alternate words.
- S1's independent pack contains the surah base and all seven augment9 ayah bases.
  Discovery packages for ayah 1:1 and all 14 surah sections are prepared under
  `work/s001/discovery/readiness-20261005/`: 30 potential sessions, none started.
  Those are historical preparations. Fresh updated packages for the two ayah 1:1
  readers are in `work/s001/discovery/step2b-readiness-20261005/`, including 13
  lexical members from the frozen commentary. Neither session has started.
- The new report correctly marks those two sessions `prepared` and
  `ready_for_merge: false`; page preflight still refuses an absent completed
  discovery. Dry preparation and reporting made no model calls or source fetches.

## Available local material

The independent index contains **74,962 segments across 14 source registrations**;
some registrations are memory pointers without local text.

| Source | Local coverage |
| --- | --- |
| WLC | 23,213 Hebrew Bible verses, 39 books; ketiv and separate note apparatus |
| SBLGNT | 7,939 Greek New Testament verses, 27 books |
| KJV | 36,822 English verses, including apocryphal material; finding aid |
| Sefaria | Four previously cached Genesis 22-related passages; more must be prefetched for each candidate set |
| Corpus Coranicum intertexts | 242 entries; 50 classified as background material, rather than Jewish/Christian textual witnesses |

This is prefix text search with normalization, not morphological or lemma search.
Search the available Hebrew/Greek wording and its inflections. WLC includes the
Hebrew Bible beyond Torah; each edition retains its own verse numbering.

Full Peshitta, Septuagint and patristic/Syriac collections remain absent. Selected
Syriac excerpts in Corpus Coranicum do not constitute full coverage. Missing
witnesses and passages must remain explicit gaps; memory claims stay marked as
unverified. These gaps limit the comprehensiveness of enrichment, not the ability
to search the original-language texts already indexed.

## Earlier production checklist (historical)

This checklist records the pre-pilot state; the completed work is reported above.

1. Complete a two-reader, two-turn native discovery pilot for ayah 1:1. The
   configured Luna/Terra model identifiers must be available in the chosen native
   runner; no substitute model was used or tested here. To enrich the surah page,
   complete all its section sessions too.
2. Audit and merge the native sessions; prefetch the selected texts. Resolve any
   retrieval errors, retain coverage gaps and rebuild the Bible index.
3. Run one native Opus page author, inspect its original-language citations,
   edition numbering, Turkish explanations and placement, then finish validation
   and acceptance. Verify any combined page against its accepted layers.
4. Use the live page's coverage, rejected candidates, gaps and usage to decide
   whether broader runs are warranted. There is no Bible-specific cost calibration
   yet; the other enrichment workflow's costs are not used as Bible estimates.

No live Sefaria request, native model session, publication or broader rollout was
performed. The initial pre-repair findings remain in
[REVIEW_initial_2026-10-05.md](REVIEW_initial_2026-10-05.md).
