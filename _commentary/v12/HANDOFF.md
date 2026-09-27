# V12 handoff (updated 2026-09-27)

For a new session picking this up cold. Read in this order:
1. `NORTH_STAR.md` (repo root): the reader, the question, three layers, guardrails, economics. Every decision is judged
   against it.
2. This file: rules, state, decisions, remaining work, data traps.
3. `RUNBOOK.md` (how runs are started and watched), `README.md` (design and evidence), `NOTES.md` (status log).
4. The root-dossier repo: `/Volumes/OZTURK/_projects/root-dossier/README.md` and `RUNBOOK.md`.
Known answers are in `eval/` (never a model input). Treat every handoff line, this one included, as a claim to check
against the code and the data.

## Standing instructions from the user

- The image chains already exist (HFT in `latent_activation/focus_trace/runs`, channel reviews in quran-data
  `network-v3/sNNN/review`). They are inputs to ground, correct, connect and go beyond. Never design or run a pass that
  rediscovers them.
- **Root dossiers are descriptive only.** A dossier groups a root's occurrences by the context the ayat state and gives
  each group its plain-reading branch. It never says what a use means, signifies, contrasts with or "shows".
  Interpretation belongs to the v12 writer.
- Fully automated. The orchestrator reads a runbook and starts or stops runs. Every step validates, repairs or salvages
  itself and records it. No hand fixes of inputs or outputs.
- Ask before any Opus run the user has not asked for. **Cost rule:** a v12 call starts only when its estimate is below
  $5; once started it is never stopped or retried.
- Luna and Sol always run at maximum reasoning. Never restart a running agent. **The user runs Luna** (root-dossier)
  **and the dictionary workflow** themselves.
- Keep known answers and test-surah material out of every model-facing prompt and input. S1, S29 (29:39, 29:41,
  29:45), S100, 18:86 and the micro roots are test cases.
- When the user asks for an agent of a given model, use that model: design assessments go to an Opus 5.5 agent, code
  reviews to Sonnet.
- Work on `main`; commit and push after each major step (both repos).

## State

**v12** (`_commentary/v12/`): built and stub-tested; **no Opus call has been made.**
- Evidence per ayah: `context.md`, `digest_v2.md` (V9/V11); `01_dictionary.md` rebuilt fresh at every prep (V11's
  package copy is built once and never refreshed); `hft.md` (from `focus_trace/runs`,
  traces checked by script, steps marked with the plain branch and usage group when a dossier exists), `channels.md`,
  `neighbours.md`, `usage.md` (root dossiers; absent until dossiers exist); with usage.md, a v12 copy of
  `digest_v2.md` whose usage blocks for those roots are pointers.
- Inputs 189–354 KB per ayah; estimates $2.7–4.0 per ayah at 1 token per byte (`run.py … --estimate`).
- `run.py`: estimate gate, no retry, repair costs counted, `--no-usage`, `--tag` (arms), `DOSSIER_OUT` (dossier arms).

**root-dossier** (`/Volumes/OZTURK/_projects/root-dossier`, private GitHub `ahmetrasit/root-dossier`, `main`):
rewritten descriptive and stub-tested end to end (grouping → repair → assign → hapax → final → usage.md → v12 inputs);
**no Luna session has run.** See its README for the design.

## Decisions made

- v12 replaces v11 (frozen as the baseline; its outputs are arm B of comparisons). The v11 seed pass is dropped.
- The dossier workflow is a standalone repo. Occurrences are anchored by QAC word id (`S:A:W`); branches by full ref.
- Descriptive dossier: groups by stated context, one branch per group, exceptions only (another branch, a genuine
  two-branch ambiguity, a variant reading), optional verbatim repeated wording, one branch per minor-analysis lemma.
  The script adds counts, forms, the branch map and the branches never used plainly. A lint flags interpretive words.
- One grouping pass; stage B is dropped. Word analysis (local senses only, never topics or payoffs) is an arm of the
  micro run (`--wa`, `out-wa/`), scored against the plain arm. It is not delivered to v12 separately: the writer
  already gets this ayah's word notes in `context.md`, and the other occurrences' senses are what the dossier groups.
- Sampling: whole up to 250 occurrences per root; above that small form cells whole and signature sampling for the
  large ones; an assign pass groups every remaining occurrence (new groups allowed). Every occurrence ends in a group.
- Stop lemmas: ٱللَّه, قَالَ, كَانَ, شَىْء, كُلّ, جَآءَ (script-only). Roots occurring once: batched labels (20 per session).
- Disputed roots: reviewed records, plus study rows that name the disputed words; whole-root rows left out.
- Grammatical headwords ك ي ف and ل و ت are loaded as branches (their senses).
- Grammar facts (attachment enrichment) and a fixed set of context roles: not used.
- HFT is read from `latent_activation/focus_trace/runs` (90 surahs), exact file name `S_A.focus_trace.json`.
- Word analysis for v12 is the per-word summaries, not the 1.2M CRITICAL rows.

## Waiting on the user

1. The micro run (two arms), in the root-dossier repo.
2. The go for the S29 probe (estimate ≈ $11; with usage.md on and off, ≈ $22).
3. Dictionary: reviewed word-root records (quran-data `qac-dictionary-word-root-analyses.json`) for the words that
   should reach the four Furūq roots, which have no QAC occurrence and bind no word in their entries: ٱللَّه and إِلَٰه →
   و ل ه (root_005296); حَيَوٰة and حَيَوَان → ح ي و (root_005544; the study table catches ḥayy instead); ٱبْن and its
   plurals → ب ن و (root_001959); whatever should reach ه ي د (root_005125; nothing does now). Both workflows read those
   records automatically (v12 through V9 `word_roots`: 01_dictionary.md, neighbours.md; root-dossier through
   `corpus.disputes`). Names now resolve by fallback (`v9/extra_names.py`: gateway, reviewed analyses, the dictionary
   repo's furuq root packets); a name field in quran-data would remove the dependency on the dictionary repo.
   Done for ٱللَّه (quran-data `ae9e79c54`: reviewed alternative و ل ه root_005296/B001, from the Tahdhīb via
   Ebû'l-Heysem) — this also settles al-Tahdhīb's variant: it lives as that alternative, not inside ء ل ه. The study
   table's ع ل ي, ز ك ي, م ن و, ر ب ي are weak-letter spellings of their dominant roots (one dictionary entry each).
4. The ~20 meaningful study disputes, moved into the reviewed format (named-word rows are kept meanwhile: د ي ن → د و ن
   100 words, ص ل و → ص ل ي 82, ن ب ء → ن ب و 75, س م و → و س م 70, ء ب و → ء ب ي 53 …).

## Remaining work, in order

1. Micro run (user) → `python3 _commentary/v12/eval/score_dossiers.py` on `out/final` and `out-wa/final`; read the
   `KEY.md` pages; decide the word-analysis arm; adjust prompts if labels interpret or groups mix.
2. Pilot (54 roots), then all roots.
3. v12 test runs (each needs the user's go): the S29 probe (usage on/off); S1 in full plus the surah pass, then an Opus
   judge and the user's blind read against v11 and v5 (`_commentary/v11/eval/s001_anchors.md`); S100 if S1 passes.
4. Not built: a whole-surah map for long surahs (the surah pass runs per passage window); production through the
   Messages API batch with a shared cached surah prefix; headwords in V9's `01_dictionary.md` (V9 `prepare.py` does
   not load them; V11 is frozen, so only a v12 copy would change); a `source:ق ر ء B001` tag matches either root of a
   merged envelope.

## Data traps (learned the hard way)

- **MASAQ vs QAC numbering.** word_analysis `aligned_qac_word_ref`, qiraat.tsv, root-disputes.tsv and attachment
  enrichment are MASAQ-numbered (clitics split): word analysis's 15:29:5 is QAC's 15:29:3. Always join through
  `quran-data/data/bridges/qac-masaq.sqlite.gz`, sorted numerically.
- **Merged dictionary envelopes** repeat branch ids across their two roots.
- **The study dispute table is root-wide and noisy**: a row whose note names no word applies the dispute to the whole
  dominant root (āya → ء و ي on all 382, dūna → د ي ن 144, māʾ → م ء ي 61, nasiya → ء ن س 45 …).
- **HFT**: `bundles/` holds 64 of the 90 surahs; `runs/s100/readers/reader_hft_a/` also holds model-comparison files
  (`100_1.5.5-high.focus_trace.json` …) — read the exact name only.
- **Furūq transfers without names**: new quran-data entries carry only a root id; quran-slm's name list lacks them.
- **Grammar-facts partner roots contain errors** (وَلَهَا → و ل ي; فَإِذَا → أ ذ ي). Take partner roots from QAC.
- **digest_v2 omits the occurrences of common forms** ("common form, not listed").
- **Tokens:** Opus 5.5 has a 1M context; V11's 100:7 billed input at exactly $8/M (one-hour cache write) and output at
  $20/M, at ≈ 0.6 tokens per byte of its inputs; the estimate uses 1.0 until calibrated.

## Reviews

- 2026-09-26: Sonnet code review of every v12 script, v9/v11 dependencies and root-dossier (all fixed); Sonnet and
  Opus design reviews of the dossier (their interpretive parts dropped).
- 2026-09-27: own review of both workflows against the data (NOTES.md); Sonnet code review of the scripts of both
  workflows after the rewrite (see NOTES.md).
