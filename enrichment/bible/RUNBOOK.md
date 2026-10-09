# Bible pathway after v16

This is the independent Bible enrichment implementation. Its helpers, prompts,
schema, source cache, index, packs, ledgers and outputs all live in this directory.
It imports no shared enrichment or v16 Python helpers. The old shared
`enrichment/v2/enrich.py --pass ehlikitap` commands are superseded **for Bible work
only**; the other enrichment workflow is unchanged.

The only upstream reads are completed v16 commentary, the optional frozen input
pack selected by the operator, the initial corpus seed, and accepted Islamic pages
when explicitly assembling a combined page. Combined pages are written here.
The Bible author never reads the Islamic enrichment pages or call directories.

Discovery adopts v16 Step 2b's operational protocol, adapted here for Bible
references and witnesses. **Ayah** research uses the frozen r13 reading from
2026-10-09 (`pack.py --ayah-base r13`, the paragraphs the v9 Islamic pages use;
S1/S87 pilot packs used augment9 commentary); an ayah is not split among writers. **Surah** research uses the original completed
r13 images and does not require the Qur'an-to-Qur'an image augment9s. This is the
user's confirmed scope in [DECISIONS.md](DECISIONS.md). Connections belonging only
to later augment prose are outside this pass and may receive a separate pass.
Discovery remains per image; the default route feeds one surah-page author.

**Session override, 2026-10-05:** the user authorized Sol max for surah writing,
one agent per image, all images in parallel. The opt-in `image_enrich.py` route
below implements this within the Bible pathway. The default whole-page Opus
route and ayah configuration retain their existing behavior.

## Production route from a Claude Code session (2026-10-09; read this first)

A cold orchestrator in Claude Code runs a surah S with these commands from the repository root. Codex readers
and image authors run through `codex exec` (no Codex parent session); ayah page authors are Opus high agents the
orchestrator spawns. Rules: the user's quota and production go; report expected vs actual cost per stage; commit
and push `enrichment/bible/` changes and the run's audit README after each stage (`git commit -- <paths>`);
never start a session twice (every runner skips finished work and prints `WARNING` for dead work); pass every
`WARNING`, `NOTE` and gap line to the user.

```sh
# 0. Sources (once per machine): lexicon, Hebrew root index, Bible index
python3 -B enrichment/bible/fetch/hebrew_lexicon.py && python3 -B enrichment/bible/hebrew.py build
python3 -B enrichment/bible/corpus.py build
# 1. Frozen pack: r13 ayah readings + original r13 images
python3 -B enrichment/bible/pack.py --surah S --ayah-base r13
# 2. Discovery: two readers (Luna max, Sol high), two turns each, packages carry the Semitic root table
python3 -B enrichment/bible/discovery.py --surah S --run-tag sSSS-YYYYMMDD --readers luna,sol --targets S:1,…,surah
python3 -B enrichment/bible/discovery_exec.py run --surah S --run-tag sSSS-YYYYMMDD --parallel 20   # background
python3 -B enrichment/bible/discovery_exec.py cost --surah S --run-tag sSSS-YYYYMMDD
python3 -B enrichment/bible/discovery_report.py --surah S --run-tag sSSS-YYYYMMDD --write
# 3. Merge, prefetch (Sefaria over the network), rebuild the index
python3 -B enrichment/bible/discovery.py --surah S --run-tag sSSS-YYYYMMDD --targets S:1,…,surah --merge --prefetch
python3 -B enrichment/bible/corpus.py build
# 4a. Surah page: one Sol max author per image via codex exec, then assemble
python3 -B enrichment/bible/image_enrich.py prepare --surah S --run-tag sSSS-YYYYMMDD
python3 -B enrichment/bible/image_enrich.py run --surah S --run-tag sSSS-YYYYMMDD --parallel 20      # background
python3 -B enrichment/bible/image_enrich.py assemble --surah S --run-tag sSSS-YYYYMMDD
# 4b. Ayah pages: prepare, then spawn one Opus high agent per call with the exact text of its spawn.md
python3 -B enrichment/bible/enrich.py spawn --surah S --target ayat
#     agent type: enrich-page-high (model opus, effort high; tools Read, Write, Edit, Bash)
python3 -B enrichment/bible/enrich.py finish --surah S --target S:A    # after each agent replies
```

- `discovery_exec.py` runs start → turn 1 (`codex exec`) → snapshot → the fixed follow-up as turn 2 in the same
  session (`codex exec resume <thread>`, which appends to the same rollout file) → audit → an automatic tool-policy
  review (reads of its own prompt/package, writes of list.tsv/followup.tsv only; no network, scripts or other
  files) → finish with the API-equivalent cost in `run.log.json`. A session with policy violations is not
  finished; review its `policy_review.json` and decide (a fresh run tag, or `discovery_native.py finish
  --reviewed` with `--protocol-finding` as appropriate).
- Each target's Semitic root table lists every Arabic root its frozen text cites (dictionary labels
  `source:"ع ص ر,B006"` and the images' Kaynaklar roots) with the Hebrew/Biblical Aramaic roots that correspond
  to it (`hebrew.py`). Authors write one `root_verdicts.jsonl` line per root (`used`, `no_qualifying_parallel`,
  `false_friend`, `no_hebrew_cognate`); `verdicts.py` refuses a call that skips one.
- Expected costs (API-equivalent, before calibration): Luna reader ≈ $0.05, Sol high reader ≈ $1, Sol max image
  author ≈ $1.5, Opus high ayah author: see `enrich.py build` (no calibration yet). Record actuals in the
  audit README.
- `hebrew.py root ROOT | cognates 'ع ص ر' | word WLC:Book.C.V` are allowed in the authors' tool grammars.

## Texts and evidence

- WLC is the primary Hebrew Bible witness (including Torah). Its main text is the
  written/ketiv stream. Qere and other notes retain their word positions in
  `variant_notes`; they are never extra words inserted into the verse.
- SBLGNT is the primary Greek New Testament witness. These are identified editions,
  not claims to possess lost original manuscripts.
- Search Hebrew with `--src WLC` and Greek with `--src SBLGNT`. Pointing and accents
  are normalized for search; returned text preserves them. Search matches word
  prefixes, not roots or lemmas. Check inflected forms and surrounding verses.
  For roots and lemmas use `hebrew.py` (WLC lemmas from morphhb mapped through the
  Open Scriptures Lexical Index; BDB heads; Arabic → Hebrew/Aramaic correspondences).
- English KJV is a finding aid. A canonical Bible parallel cannot be accepted with
  KJV as its only textual witness. Match the actual Hebrew/Greek edition's verse
  numbering; English and Hebrew numbering are not assumed identical.
- Jewish interpretation is fetched through the Bible-owned Sefaria importer.
  Corpus Coranicum supplies selected contextual passages and editorial information.
  Tradition is assigned per segment, not per mixed collection. Background material
  is restricted to scholarship, source notes and method notes.
- `nusha` identifies the cited witness. Use `tercume` for an explicitly identified
  translation; `uygulanmaz` is for background/method notes without a scriptural
  witness. An available original witness must support a claimed textual reading.
- Full Peshitta, Septuagint and patristic collections are not currently present.
  Some Syriac excerpts occur in Corpus Coranicum. Explicitly record unavailable
  witnesses and untranslated/unverified candidates in `gaps.json`.

## 1. Prepare the Bible-owned corpus and frozen commentary

Run from the repository root with Python 3.10+ and `requests`; SQLite must support
FTS5. The setup used here was checked with Python 3.14.

```sh
python3 -B enrichment/bible/corpus.py seed
python3 -B enrichment/bible/fetch/bible_text.py wlc
python3 -B enrichment/bible/corpus.py build
python3 -B enrichment/bible/pack.py --surah 1
```

`seed` copies eligible cached sources once from `enrichment/corpus`; existing
Bible-owned sources are retained. The WLC step reparses the cached XML with the
correct variant handling. On a checkout without the bulk originals, run
`python3 -B enrichment/bible/fetch/bible_text.py all` before indexing (downloads).

`pack.py` freezes its own copies directly from completed v16 r13 surah output and
augment9 ayah output. When multiple outputs exist, explicitly select an existing
frozen pack with `--from-pack PATH`. For example, the verified S1 setup used
`--from-pack enrichment/v2/work/s001/pack`; that source pack is read-only.
Missing augment9 ayah bases are recorded and cannot produce ayah pages.

Pack rebuilds are refused while any Bible discovery or page call is active. Source
mutation and index rebuilds are refused while a Bible page call is active. Frozen
input hashes are checked again before acceptance. `--force` on `pack.py` replaces
only the Bible pack and does not bypass the active-call guard.

## 2. Prepare and complete native discovery

```sh
python3 -B enrichment/bible/discovery.py --surah 1 --run-tag pilot1 --targets 1:1,surah
```

This writes packages and prompts, with **no model calls**. `1:1` uses the full frozen
augment9 ayah text; `surah` selects every image section of the frozen surah text.
The configured discovery readers remain Luna max and Terra max. Their exact model
identifiers are in `discovery.py`; the runner must provide them. Do not silently
substitute another model. Use a unique native task name for every session.
Packages also include the word/root/branch labels from the frozen surah commentary
(the target ayah's members for an ayah, the selected image's members for a section).
These labels are context, not dictionary definitions or proof of cross-language
cognacy. The brief requires coverage of every developed detail and secondary
sense, with a concrete connection and no target list length.

Use at most seven native agents at once unless the user explicitly changes the
limit for this Bible run. Complete their fixed follow-ups, audits and reporting
before the next already-authorized batch. v16 S1 revision4's concurrency exception
does not apply here. A discovery go does not start the page author. Scripts never
launch either model stage. This implementation update does not run a live pilot.

For each prepared target and model:

```sh
python3 -B enrichment/bible/discovery_native.py start --surah 1 --run-tag pilot1 --target 1:1 --model luna --task bible_pilot1_1_1_luna
```

An orchestrator launches the native agent with the exact generated `spawn.md`,
using an independent context and the specified model/effort. After its first turn:

```sh
python3 -B enrichment/bible/discovery_native.py snapshot --surah 1 --run-tag pilot1 --target 1:1 --model luna
```

Deliver the generated `followup.txt` to **that same session**. It writes new
proposals to `followup.tsv` without modifying `list.tsv`. After the second turn:

```sh
python3 -B enrichment/bible/discovery_native.py audit --surah 1 --run-tag pilot1 --target 1:1 --model luna
python3 -B enrichment/bible/discovery_native.py finish --surah 1 --run-tag pilot1 --target 1:1 --model luna --reviewed
```

Before passing `--reviewed`, inspect `tool_calls.json` for adherence to the supplied
inputs and the no-retrieval/no-other-agents rules. The flag is an operator audit
attestation. Record any violation with `--protocol-finding "specific violation"`;
it blocks the run. Recoverable tool diagnostics remain visible in the report.
Finish verifies the session model and effort, two completed turns,
follow-up delivery, frozen inputs and first-turn bytes. It consolidates unique
proposals, preserving distinct reasons and link kinds. An empty delivered TSV is
valid; a missing TSV, overwritten first turn or failed session is not.

New sessions use `bible-separate-proposals-v2`. Deliver `followup.txt` verbatim
once, to the same fresh-context native session. During that turn, only a write
of `followup.tsv` is allowed: no reads, retrieval, research scripts or other
agents. Consolidation never changes first-turn bytes or an existing connection's
grade. Exact repeated connections retain the first occurrence; each repeat and
the retained phase/line are recorded in `consolidation.json`. Distinct reasons for
one reference remain separate connections and reach the verifier. Legacy run
histories cannot be upgraded in place; prepare a fresh tag.

Finish retains native event evidence, raw and consolidated wording reviews,
diagnostics and hashes. `check_discovery.py` checks edition-qualified references
and Hebrew/Greek wording against the local text; it identifies matching WLC
variant readings separately and may flag adjacent verse wording. Flags require
review of roots, forms, orthography, witnesses and boundaries. They neither prove
nor disprove the semantic connection. No model calls occur during checking.

Raw discovery uses exactly six tab-separated fields: strength, tradition, kind,
reference, basis, explanation. Bible references must name their edition, e.g.
`WLC:Gen.22.2` or `SBLGNT:Matt.6.5`, and resolve in the local index. Named secondary
works may be proposed for prefetch. These are candidates, not verified evidence.
The live pilot added conservative book-name resolution: full names such as
`Hosea` and `James` resolve to the existing corpus codes `Hos` and `Jas`. The
explicit abbreviations `Is`, `Jon` and `Philem` resolve to `Isa`, `Jonah` and `Phlm`.
The edition, chapter and verse are never changed. Raw TSV bytes remain intact;
`raw_ref`, the resolver version and a `reference_alias` finding record each
resolution. Unknown books, nonexistent verses, wrong editions and ambiguous
references still fail. This is name resolution, not a passage correction.

Report a completed batch/target set before merging or continuing:

```sh
python3 -B enrichment/bible/discovery_report.py --surah 1 --run-tag pilot1 --targets 1:1 --write
```

The JSON and Markdown reports include initial/proposed/new/repeated/final counts,
grades, quotation findings, missing existing citations, failures, repairs,
diagnostics and usage, plus a dry handoff count when both readers pass. Missing
or partial runs produce a failing exit status. Report all findings, not just
structural failures. Reports live under the Bible attempt; reporting does not
select inputs, merge them, prefetch or launch a page author. Runtime `work/` and
`out/` remain ignored by Git; commit only intentionally versioned Bible files.

### Recorded repairs and new attempts

A malformed follow-up reference may be repaired only when both original turns
completed, the first turn is intact and all other protocol checks passed. First
prepare an exact reviewable proposal. Its JSON input is an array of objects with
`line`, six-field `before` and `after` arrays, and `reason`:

```sh
python3 -B enrichment/bible/discovery_repair.py propose --surah 1 --target 1:1 --run-tag pilot1 --model luna --changes enrichment/bible/work/repair-changes.json
```

Inspect `repair.proposed.json` and `followup.repair.proposed.tsv`. After explicit
approval of that exact correction, record the approval with the `accept` phase
and `--approval "approval record"` using the same target/tag/model. By default only
reference corrections or reference/basis swaps are supported; strength, tradition,
kind and explanation cannot change. Raw follow-up, failed log and failed validation remain
intact. The accepted correction has its own file and hash chain. No model is
rerun. Protocol failures, changes to judgements and missing files require a fresh
attempt, not this repair mechanism.

Two narrowly defined schema corrections can also be proposed, still requiring
explicit approval of the exact displayed rows. `--allow-schema-swap` permits an
exact transposition of the tradition/kind columns. `--allow-witness-tradition`
permits only the tradition label implied by an unchanged canonical witness
(`WLC` → `tevrat`, `SBLGNT` → `incil`). It cannot change the witness, kind, basis,
grade or explanation. These options are recorded in both proposal and acceptance
and checked again when merging; they never authorize a general rewrite.

The S1 pilot's explicitly approved first-turn exception is supported by the
Bible-owned `discovery_first_repair.py`. Before snapshot or follow-up, use its
`propose` phase with the same target/tag/model/changes arguments, inspect the
generated `turn1.tool_calls.json`, and accept only the exact approved proposal
with `--approval "approval record" --reviewed`. The user approved the thirteen
corrections recorded in `audits/pilot1-20261005/first-turn-repairs.proposed.json`.
Other first-turn failures still need either an explicit approved correction or
a fresh attempt. No judgement may be rewritten: only reference corrections,
reference/basis swaps, or an exact transposition of tradition/kind columns.

This preserves `list.tsv` unchanged until the ordinary two-turn consolidation,
and keeps the original bytes in both `turn1.original.tsv` and `turn1.list.tsv`.
The corrected first pass is separate (`turn1.accepted.tsv`). Snapshot validates
that accepted copy; consolidation and merge replay it with the raw bytes,
original failed validation, exact changes, approval and tool audit in the hash
chain. The correction record reaches both reports and verifier handoffs. A
corrected locator remains an unverified candidate, including named-work entries
whose original witness is unavailable. Never show a repaired first pass as an
unchanged native success.

## 3. Merge discovery, prefetch, rebuild the index

After both readers complete all selected targets:

```sh
python3 -B enrichment/bible/discovery.py --surah 1 --run-tag pilot1 --targets 1:1,surah --merge --prefetch
python3 -B enrichment/bible/corpus.py build
```

The merge requires **both** completed, audited readers for every target; passing
only one model to `--merge` is an error. It replays consolidation and verifies
raw proposals, reviews, native evidence and any repair chain. It emits individual handoffs and
a real `surah.merged.tsv` after all surah sections complete. `selected.json`
explicitly selects each page's handoff; there is no implicit legacy fallback.
The TSV groups references while retaining all distinct connections, each with a
stable `connection_id` in its evidence. The adjacent `.merged.json` carries raw
review findings and provenance. The best reported grade is not verified confidence.

To combine completed attempts explicitly, pass `--selection PATH` to merge, where
PATH contains a JSON mapping such as `{"sec1":"first","sec2":"second"}`. Both
readers for a selected target must come from its specified attempt. The output
uses `--run-tag`; its handoff records the actual source attempts. A surah merge
still requires every section in one invocation. Use the same mapping when reporting.

Prefetch records candidate resolution, fetched locators, missing texts, retrieval
errors, list hashes and source hashes in `prefetch.json`. Errors block page start.
Unavailable secondary works remain explicit coverage gaps; the author must record
them. HTTP failures are retried on a later prefetch instead of becoming permanent
cached failures. Build the Bible index after all prefetch operations and before
starting any page authors. Run the merge/prefetch command for the complete set of
pages you intend to use together, since the report covers the selected set.

## 4. Write, validate and accept a Bible page

### Optional surah image authors (Sol max)

```sh
python3 -B enrichment/bible/image_enrich.py prepare --surah 1 --run-tag session-20261005
# Spawn every generated secK/spawn.md with its exact task name, gpt-6-sol/max,
# and an independent context. The script does not launch models.
python3 -B enrichment/bible/image_enrich.py finish --dir ABSOLUTE_CALL_DIRECTORY/sec1
# Finish every image, then assemble only if every image passes.
python3 -B enrichment/bible/image_enrich.py assemble --surah 1 --run-tag session-20261005
```

This opt-in pilot uses **available local witnesses**, not the network-prefetch
route above. Its `prefetch.json` explicitly records `network_attempted:false`;
missing secondary texts are unavailable in this run, not nonexistent or searched.
WLC/SBLGNT discovery verses must already resolve. Every missing ref must remain
in the image's gap ledger. This coverage limitation is retained in the accepted
page's provenance. A later source-expansion run requires a fresh snapshot.

Preparation freezes all audited discovery inputs, the current Bible index and
source hashes, and the commentary pack. Each agent receives just its image's
commentary with global paragraph numbers, the Arabic surah, its merged candidates
and review findings, and the Bible rules. The parent run locks source/index
mutation until assembly. Each agent verifies, researches and writes its section;
it cannot delegate or consult another author. Every image requires one successful
native completion, with an exact model/effort check and an auditable tool grammar.
An explicitly authorized same-session resume may retain an interrupted or failed
attempt: record its exact native failure history, unchanged model/inputs, resume
message and parent delivery proof. Failed attempts remain visible; they are never
counted as successful completions. Reading the agent's own generated preview and
checking the clock are operational activities, not additional research sources.
The same applies to a nonrecursive listing of the agent's own call directory.
An exact candidate-ID lookup with `sed -n '/BC-<20 lowercase hex digits>/p'`
is an allowed read of the agent's own files.
The agent's own preview also permits single-quoted, print-only ranges between
escaped numbered paragraph markers or text prefixes, optionally to end of file.
These ranges cannot execute commands, write files or read another directory.
Other sed scripts remain prohibited.
A single-quoted text search with only the fixed flags in "rg -n" may inspect one
file in the author's own directory or its own preview; extra options, shell
expressions and reads outside that scope remain prohibited.
The fixed form `tail -n <positive integer> <own file>` may read the end of one
file in the same scope; follow mode, byte counts and additional options are not
permitted.
An author's status acknowledgment to the parent operator can be retained only
with an individual `operator-messages.json` review binding its native call ID and
argument hash to the received plaintext, parent request and reason. This exception
does not permit consulting another author, and messages never count as source
evidence. Encrypted native bodies remain marked as such; the plaintext is the
operator's recorded observation. The author cannot write this review file.

Each image must pass schema, paragraph-scope, candidate/gap-coverage and actual
opened-evidence checks. Canonical rejection requires the original verse too.
Assembly refuses failed, missing or modified image results; it verifies each
image separately before combining evidence. A deterministic ID map prevents
collisions. Research verdicts keep their individual image scopes and decisions;
assembly does not regrade them. The original commentary remains byte-preserved.
The assembled page and immutable annotation/verdict/gap snapshots are accepted
under the normal Bible output path. Semantic and quotation review still matters.

### Default whole-page author (Opus high)

```sh
python3 -B enrichment/bible/enrich.py build --surah 1 --target 1:1
python3 -B enrichment/bible/enrich.py spawn --surah 1 --target 1:1
```

`build` reports preflight readiness and a cost estimate based solely on previous
Bible calls. Initially there is no calibration. `spawn` requires a matching
discovery handoff, completed prefetch, current index manifest and unchanged pack;
it writes a native page-agent brief, **without calling a model**.

The page author is the configured native Claude Opus agent at high effort. Use a
general-purpose native agent with the exact `spawn.md`; no shared agent definition
or hook is required. A single completed native transcript is mandatory. Missing
transcripts, mixed models and tool use outside the Bible call rules reject the
result. Accounting uses the Bible-local nominal rate snapshot; it is not a billing
quote. No legacy model CLI fallback is provided.

The agent writes `annotations.jsonl`, `verdicts.jsonl` and `gaps.json`, validates records, and renders
a preview inside its call directory. IDs are `S001-TEV-PRL-001` or
`S001-INC-MTF-001`, using the schema's actual type codes. After completion:

```sh
python3 -B enrichment/bible/enrich.py finish --surah 1 --target 1:1
```

Invalid records are reported and dropped. A result with every record dropped is a
failure. An intentionally empty page requires `gaps.json.no_findings_reason`.
Acceptance writes the page, an immutable copy of kept annotations and provenance
to `enrichment/bible/out/s001/`; accepted pages are never overwritten. Native
transcripts and local checks are retained in the Bible call directory.

Every distinct discovery `connection_id` needs an accepted, rejected, unresolved
or unavailable verdict, with a specific reason. Accepted connections name valid
paragraphs, opened evidence and kept annotation IDs. Both acceptance and rejection
of a WLC/SBLGNT discovery claim require the cited original verse as evidence.
Every additional `get` lookup, including context and missing passages, also needs
a research verdict. Search snippets alone are not opened evidence. The verifier
still does its own paragraph-by-paragraph research; discovery is a seed.

`verdicts.py --draft` checks structure while the author works. Final acceptance
checks actual corpus `get` results in the native transcript, missing connections,
unjudged lookups, dropped/missing annotation IDs and paragraph correspondence.
Unresolved/unavailable refs and prefetch gaps must appear in `gaps.json`. Empty
annotation output does not waive candidate coverage. `verdict_report.json` records
the checks; immutable verdict, gap and report copies accompany the accepted page
and are verified again when assembling a combined page. These checks establish
coverage and provenance, not semantic correctness; the live pilot still needs
editorial review of quotations, links and Turkish explanations.

Use `--trial` on finish to keep the result only in its call directory. A trial is
not an accepted page; the CLI currently has no trial-promotion command. Do not
start the same call twice. `--attempt 2` is a separate, explicitly chosen attempt.

## 5. Optional combined page

```sh
python3 -B enrichment/bible/enrich.py merge --surah 1 --target 1:1
```

This reads the accepted Islamic page, if present, and the accepted Bible page. It
requires identical frozen bases, verifies page/snapshot hashes and rejects
duplicate IDs. Legacy Islamic annotations are used only if they reproduce the
accepted page exactly. Accepted source descriptions are preserved. The combined
page and its provenance are written only to `enrichment/bible/out/`; the manifest
marks a page containing only one layer as partial. No publication is performed.

## Verification

```sh
python3 -B -m unittest enrichment.bible.test_workflow enrichment.bible.test_image_enrich -v
```

The tests use temporary packs, indexes, annotations and mocked fetches. They do
not call models, fetch online texts or write shared enrichment data. See
`READINESS_2026-10-05.md` for the current verified state and remaining live work.
