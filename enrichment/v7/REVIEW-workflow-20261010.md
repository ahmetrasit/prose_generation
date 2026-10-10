# Tier 1 and enrichment workflow review — 2026-10-10

Reviewed at `ab261386e`, before starting workflow changes. Scope: corpus freshness and
selection; full segment and quotation preparation; completion and provenance checks;
recheck supplements; native/scripted execution, recovery and session archival; v9
material/link readers, maps, translations, page preparation and rendering. Superseded
v7 retag/consolidation/writer stages and the separate Bible pipeline are outside this
change. This is a code review, not an audit of every generated note or scholarly claim.
No enrichment/model jobs were launched. Existing generated work remains in place.

## Findings and changes to make

| Priority | Finding | Consequence | Resolution |
|---|---|---|---|
| High | `recheck.check_chunk` enforces CHECK, but `digest.valid_output_locs`, `merge.supplements` and `checked_before` do not. | A rejected note can reach a map and suppress an unanswered pair. Reproduced with an isolated fixture. | Share the chunk-specific row rules between checkers and readers. |
| High | Completion ignores repair streams/records; the merge cache ignores completion changes. | A successful same-session repair can remain excluded; a cached line can remain readable while its agent resumes. | Read the latest same-session repair state and include run state in the cache key. |
| High | Map updates compare only note IDs; refresh changes saved claims without remapping. | A changed claim/stance with the same ID silently keeps its old position; removed/invalid notes stay in saved maps. | Detect content changes and missing notes; block automatic update/refresh/assembly pending an explicit new map run. Preserve evidence. |
| High | Page readiness checks only existence of run.json; assembled-map freshness considers timestamps but not unfinished agents or saved-row changes. | A failed/running map can look ready. | Check recorded completion, repairs and row changes before assembly/page preparation. Keep agent self-checks usable before completion. |
| High | Zero shell commands is treated as proof of a $0 startup failure. | An agent can write files or spend tokens without shell commands and then be launched again. | Retry only evidenced failures before thread creation, with zero usage and no completed items. |
| Medium | Recheck report counts all planned pairs and counts recorded failures as done. | An unstarted fixture reported one pair checked with zero runs. | Report planned, completed and validated work separately; count only validated completed lines. |
| Medium | Named-surah markers are interpreted as the segment's surah. | `[البقرة: 2]` in a surah-90 segment selects 90:2. Reproduced. | Resolve named surahs and reject unrelated/unknown labels; retain explicit S:A and numeric markers. |
| Medium | Recheck input omits corpus provenance and the earlier notes' anchors, mentions and tags. | Agents miss source-quality cautions and cannot inspect the full earlier note when avoiding duplicates. | Deliver selected provenance and complete existing rows; fingerprint rendered input. |
| Medium | Recheck selection omits the existing full-verse plus explicit-citation fallback. | Repeated verses without unique windows lose a preparation route already supported in Tier 1. | Apply that conservative fallback to digested segments and report its counts. |
| Medium | Repair scripts for recheck, maps and translations hardcode another machine's paths and truncate checker output. | Repairs fail locally or miss problems; changed sources cause an impossible repair loop. | Share portable same-session repair handling, preserve all problems, stop on rebuild-only failures and save repair results. |
| Medium | Tier-1/recheck check commands can report errors with exit status zero; bad chunk/model selections are insufficiently checked. | Automation can advance despite a failed check. | Return failure and print every problem; validate requested scope, chunk and model. |
| Medium | Link stamps summarize non-Quran text by length; linked lookups claim named notes are already in maps. | Same-length source corrections can leave links looking current; new notes may still await map updates. | Hash actual segment content and use wording that distinguishes available notes from assembled maps. |
| Medium | Supplement readers disagree when the original digest is unavailable. | Verse-row readers return valid supplements that segment-row readers omit. | Make both readers retain valid supplemental evidence while explicitly distinguishing it from full-segment coverage. |
| Medium | Translation readers accept unfinished/malformed/partial outputs; newer partial output can replace a complete translation. | Pages can consume text the translation checker rejects. | Validate per-question assignments, shapes, hashes and completion; preserve complete current translations. |
| Medium | Renderer does not itself run writer/meal checks. | Direct rendering can publish structurally invalid blocks while passing the frozen-page strip check. | Validate blocks before writing rendered artifacts. |

## Selection limits and operational decisions

- Recheck is a screened pass for **unnamed verses**, not an exhaustive missing-point
  audit. A verse already in a segment's `verses` or `mentions` is excluded even if a
  second point was missed. Common-only windows, short ambiguous quotations and
  interpretations without recognizable wording remain gaps. Correct the handoff's
  exhaustive-coverage claim; retain explicit limits and counts.
- One miss in 40 spot checks describes that sample. It does not establish a universal
  miss rate or validate the estimated recovery yield.
- Existing source hashes and complete legacy snapshots correctly protect Tier-1 reuse.
  Missing legacy inputs remain unresolved. Keep the whole-segment, edition and scope
  rules already fixed locally.
- The corpus `fresh` command already returns nonzero for stale inputs. Handoff commands
  should be sequential and stop on failure. Corpus rebuilds and private source transfer
  are separate operational actions; raw texts/database copies stay out of public Git.
- Context/cost estimates are estimates. Full oversized segments still stand alone;
  review the forecast before launch. Do not silently cut them to meet a target.
- `run_until_done` handles eligible startup retries, not semantic output repair. A
  finished session still requires the stage checker and report. Make failures visible
  in its exit status and avoid a misleading unconditional success marker.
- Scope, launch quota and map-update costs still require the user's stage go. This
  review/change request authorizes code work, not a paid production run.
- The v9 runbook requests an independent Sonnet review. This environment exposes no
  Sonnet reviewer; do not claim that review took place. Code review here is performed
  locally, with isolated fixtures where authorized, and that limitation is reported.

## Verification record

Before edits, temporary fixtures reproduced CHECK bypass, false report completion,
and named-surah marker confusion. Subsequent verification is recorded below when
the changes are complete. No production plan/build/agent launch is needed for those
checks.

### Implemented and reviewed

The findings above are addressed in the shared validator/completion helpers, recheck
selection and inputs, portable repair wrappers/helper, cautious startup recovery,
map snapshots/assembly stamps, translation readers, page preparation and rendering.
The handoff and both runbooks describe the changed behavior. Saved production notes
and maps were not rewritten or removed.

Verification performed with temporary fixture databases/files (no model calls):

- The earlier Tier-1 integration fixture still passes: Arabic matching, index and
  overlay quotation routes, citation fallback, scope/split reproduction, verse ranges,
  mention links, changed metadata rejection and unresolved legacy input rejection.
- A wrong-CHECK supplement is rejected by the checker, merge and checked-before;
  a valid supplement is accepted after repair and excluded during a pending repair.
  Cache validity follows completion changes even when the output file is unchanged.
- Named-surah markers select only the correct surah; page/footnote numbers are
  excluded. An unstarted recheck reports zero pairs checked. Rendered inputs retain
  source metadata and the full earlier notes; plan/build share exact packing.
- Explicit citation plus full repeated-verse text produces a candidate without unique
  windows. Map input changes are detected with unchanged timestamps. Failed sessions
  block map consumption, completed repairs unblock it, and superseded maps are excluded.
- A newer incomplete translation does not replace an older complete current one;
  malformed/duplicate positions fail shared validation.
- Simulated portable repair accepts an unpadded number, restores an archived session,
  resumes the original thread, saves completion and cumulative cost, and clears its
  lock. Changed-source failures cause no resume. The simulation did not launch Codex.
- Retry fixtures distinguish a proven pre-session failure from sessions with a thread,
  usage or file-write events; zero shell commands is insufficient.
- Changed Python files parse, changed shell wrappers/runner pass `bash -n`, and
  `git diff --check` passes. No broad test suite or production model workflow ran.
- The read-only corpus freshness command reports:

  ```text
  enrichment/corpus/corpus.sqlite: current
  committed gz parts (2026-10-09T19:23:29-0400): hold this index
  ```

### Operational follow-up

Before launch, obtain a current recheck plan with the full-note inputs and explain
differences from the historical budget. Existing link indices need rebuilding because
the stamp now hashes actual segment content. Existing maps need the standard
check/update pass; changed or invalid saved notes are surfaced as rebuild requirements,
not silently retained as current evidence. A new production plan, all-note corpus
audit, live model repair, and independent Sonnet review were not performed here.
