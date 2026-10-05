# Bible pathway readiness — 2026-10-05

**Local implementation and offline checks are ready for a live pilot. Production
content readiness is still pending that pilot.** S1 page preflight correctly
reports `ready: false` because no native Bible discovery sessions have completed.
No production Bible annotations have been accepted and no model calls were made
as part of this repair.

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

- **27 Bible regression tests passed**, using temporary fixtures and mocked HTTP.
- **7 existing Quran-discovery tests passed**, with their implementation unchanged.
- All Bible Python modules parse and have no imports of shared workflow helpers.
- Actual Hebrew `בראשית` searches resolve WLC verses; Greek `πατερ` searches resolve
  SBLGNT verses. Displayed passages preserve Hebrew pointing and Greek accents.
- Ezekiel 1:8 displays the written `וידו` in the main stream and its `וִידֵ֣י`
  reading separately at word position 1. Across WLC, 3,657 verses contain some kind
  of note; not all of those notes contain alternate words.
- S1's independent pack contains the surah base and all seven augment9 ayah bases.
  Discovery packages for ayah 1:1 and all 14 surah sections are prepared under
  `work/s001/discovery/readiness-20261005/`: 30 potential sessions, none started.

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

## What remains before production use

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
