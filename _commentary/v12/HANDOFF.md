# V12 handoff (2026-09-26)

For a new session picking this up cold. Read in this order:
1. `NORTH_STAR.md` (repo root): the reader, the question, three layers, guardrails, economics. Every decision is judged
   against it.
2. This file: rules, state, decisions, remaining work.
3. `README.md` (design and evidence), `NOTES.md` (status and the **known-answer checks** — never put NOTES.md or
   anything from it into a model's input).
4. The root-dossier repo: `/Volumes/OZTURK/_projects/root-dossier/README.md` and `RUNBOOK.md`.

## Standing instructions from the user

- The image chains already exist (HFT in `bundles/`, channel reviews in quran-data `network-v3/sNNN/review`). They
  are inputs to ground, correct, connect and go beyond. Never design or run a pass that rediscovers them.
- **Root dossiers are descriptive only.** A dossier groups a root's occurrences by context as the ayat state it and
  lists the ayat. It never says what a use means, signifies, contrasts with or "shows". Interpretation belongs to
  the v12 writer. (The user rejected an ن ف خ example that said the verb "gives life and ends it".)
- Fully automated. The orchestrator reads a runbook and starts or stops runs. Every step validates, repairs or
  salvages itself and records it. No hand fixes of inputs or outputs.
- Ask before any Opus run the user has not asked for. Nothing may cost $5 or more per ayah.
- Luna and Sol always run at maximum reasoning. Never restart a running agent. **The user runs Luna** (root-dossier)
  **and the dictionary workflow** themselves.
- Keep known answers and test-surah material out of every model-facing prompt and input. S1, S29 (29:39, 29:41,
  29:45), S100, 18:86 and the micro roots are test cases.
- When the user asks for an agent of a given model, use that model: design assessments go to an Opus 5.5 agent,
  code reviews to Sonnet.
- Work on `main`; commit and push after each major step (both repos).

## State

**v12** (`_commentary/v12/`):
- Built: `inputs.py`, `run.py`, `prompts/write.md`, `prompts/surah.md`, README, NOTES.
- Smoke-tested with stubbed model calls: inputs, the check/repair/strip loop, render, surah-pass input assembly.
- A Sonnet code review found 2 high and 5 medium issues; all are fixed (commit `e1db28897`).
- **No v12 Opus call has been made.**
- Evidence per ayah:
  - from V9/V11: `context.md`, `01_dictionary.md`, `digest_v2.md`;
  - new in v12: `hft.md` (script-checked HFT traces), `channels.md`, `neighbours.md`;
  - `usage.md` (root dossiers), which is absent until dossiers exist.
- Inputs are 123–337 KB per ayah; Arabic is about 1 token per byte.

**Shared code fix:** quran-data stores 11 roots as merged envelopes (`root_001210--root_001211_entry.json`: ق ر ء,
ش ي ء, ج ي ء, م ر ء, ب ر ء, ب د ء …). V9 `prepare.py` and V11 `verify_src.py` missed them. Both now read every
entry file (commit `4f31e2ba9`).

**root-dossier** (`/Volumes/OZTURK/_projects/root-dossier`, private GitHub `ahmetrasit/root-dossier`, `main`):
- Built and stub-tested; review fixes are in commit `a446dd2`:
  - QAC word ids, and branches by full ref;
  - the QAC–MASAQ bridge;
  - disputed roots;
  - patches, checks, salvage and the map export;
  - atomic locks.
- **No Luna session has run.**
- **The current `prompts/stage_a.md`, schema, `check.py` and `deliver.py` are the pre-descriptive design and must
  be rewritten (below) before any run.**

## Decisions already made

- v12 replaces v11. V11 stays frozen as the baseline, and its outputs are arm B of comparisons. The v11 seed pass
  is dropped (it rediscovered HFT).
- Word analysis: use the per-word summaries (`word_analysis/outputs/production`, 6,236 ayat), not the 1.2M
  CRITICAL rows.
- The dossier workflow is a standalone repo.
- Occurrences are anchored by QAC word id (`S:A:W`). Branches are named by full ref (`root_001529/B001`), because
  merged envelopes repeat branch ids across their two roots.
- The canonical branch map records the branch of the plain Ḥafṣ reading. Latent readings are not mapped; they
  belong to the writer.
- Micro list (`lists/micro.txt`): ح م ء, ن ف خ, ر ب ب, ص ل و, ع ر ش, and و س م for the disputed-root path (ism).
- Stoplist, per lemma: ٱللَّه (the name), قَالَ, كَانَ, شَىْء, كُلّ, جَآءَ. These get script-only dossiers. Other
  lemmas of the same roots (ilāh, qawl, makān, shāʾa, kalāla …) keep full dossiers.
- Dictionary gaps: the user runs the dictionary repo's Furūq workflow, in this order:
  1. export ب ن و (`root_001959`), which is already reviewed;
  2. write و ل ه (`root_005296`), ح ي و (`root_005544`, kept separate; its duplicate route into ح ي ي is corrected)
     and ه ي د (`root_005125`);
  3. add al-Tahdhīb's etymological variant under ء ل ه.
- ك ي ف and ل و ت are grammatical headwords (`headword_000001`, `headword_000002`). The dossier resolver must load
  them.
- Minor analyses (disputed roots) become one note per lemma, not one mapping per occurrence. The dominant root's
  map is never changed.

## Decisions waiting for the user's go

1. The **descriptive rewrite** of the dossier (the target shape is below).
2. Word analysis: a descriptive per-root digest of its cross-occurrence notes, placed inside the single Luna pass,
   tested with and without it on the micro run. The user wants word analysis to inform the grouping. An Opus review
   argued for leaving it out, because its per-ayah notes repeat what the concordance shows.
3. Sampling that keeps every distinct use. Sample by signature (number, definiteness, suffix person, iḍāfa partner,
   governing verb and preposition, vocative, negation), list a form whole up to about 120 occurrences, allow pinning
   test ayat, and add a cheap assign pass for unlisted occurrences. The current even spacing misses all of rabb's
   telling uses: arbāb (3:64, 9:31, 12:39), Yūsuf's master (12:23, 12:41, 12:42, 12:50), 79:24, 106:3, 114:1.
4. Grammar facts: one line per occurrence from quran-roots attachment-enrichment, joined through the bridge, with
   partner roots taken from QAC. Luna's corrections are exported as a review list for quran-roots.

## Target shape of a dossier (descriptive)

```
ن ف خ — 20 occurrences, 5 contexts (all root_001529/B001 "blowing air into something")
- God breathing His spirit into Ādam: 15:29:3, 38:72:3, 32:9:3
- God breathing His spirit into Maryam: 21:91:4, 66:12:7
- ʿĪsā breathing into a bird shaped from clay, by God's permission: 3:49:18, 5:110:34
- the Horn being blown: 6:73:16, 18:99:7, 20:102:2, 23:101:2, 27:87:2, 36:51:1, 39:68:1, 39:68:16, 50:20:1, 69:13:2, 69:13:5, 78:18:2
- people told to blow (on the iron, at the barrier): 18:96:10
```

- **Luna writes, per group:**
  - a plain context label: who does what, to what, where, as the ayah says;
  - the QAC ids;
  - the plain-reading branch;
  - optionally, exact repeated wording (checked verbatim).
- **Exceptions** are recorded only for a second branch in the plain text, a variant reading, or a branch different
  from the group's.
- **The script adds** counts, forms per group (for example "the Horn: 11 passive verbs + 1 noun"), the branch of
  every occurrence, and the branches never used as the plain sense.
- **Not allowed:** a summary, `beyond`, `brings`, contrast or echo texts, or any claim about meaning.
- **usage.md for an ayah** lists each root's groups, with this ayah's group marked: about 1–2 KB per root, capped at
  about 10 KB per ayah, with a switch to turn it off.

## Remaining work, in order

1. **Dossier rewrite** (after the user's go; scripts and prompts only):
   - `prompts/stage_a.md`: descriptive groups, examples from roots outside the test sets;
   - `check.py`: every occurrence in exactly one group, one branch per group, exceptions only;
   - `deliver.py`: new usage.md with size caps;
   - `run.py` and `build.py`, plus whichever of the waiting decisions (2–4 above) the user approves;
   - resolvers: the headwords, and Furūq-only roots by name once the transfers land (quran-slm's root list lacks
     them; ask that transferred records carry the root name);
   - the lemma-level stoplist;
   - minor analyses as one note per lemma.
2. **Micro run** (the user runs it): `cd /Volumes/OZTURK/_projects/root-dossier && python3 run.py all --list
   lists/micro.txt --parallel 6`. Compare with the known answers in NOTES.md, through an automatic scorer kept in
   prose_generation (set containment of ids per group).
3. **Connect the dossiers to v12:**
   - `digest_v2.md`'s usage section becomes a pointer for roots that have a dossier;
   - `hft.md` trace steps are annotated with each word's plain branch and group;
   - `write.md` describes usage.md and makes it the source for cross-occurrence patterns (context.md word notes are
     this ayah's angle);
   - add the usage.md switch and cap.
4. **Pilot:** 51 roots (`lists/pilot.txt`), then all roots.
5. **v12 test runs** (each needs the user's go):
   - the S29 probe, `python3 _commentary/v12/run.py ayah 29:39,29:41,29:45 --parallel 3` (≈ $11), with usage.md on
     and off; it can also run now, without dossiers;
   - S1 in full plus the surah pass (≈ $24), then an Opus judge and the user's blind read of 1:4, 1:6, 1:7 and the
     surah reading against v11 and v5 (`_commentary/v11/eval/s001_anchors.md` is the regression guard);
   - S100, if S1 passes.
6. **Not built:**
   - a whole-surah map for long surahs (the surah pass now runs per passage window);
   - production through the Messages API in batch mode with a shared cached surah prefix (toward about $1 per
     ayah);
   - small open points: a `source:ق ر ء B001` tag matches either root of a merged envelope; the Chains and New
     ledger families are not rendered (by design, for the surah pass).

## Data traps (learned the hard way)

- **MASAQ vs QAC numbering.** word_analysis `aligned_qac_word_ref`, qiraat.tsv, root-disputes.tsv and
  attachment-enrichment `word_unit_id` (`q:15:29:5`) are MASAQ-numbered (clitics split). QAC's id for that word is
  15:29:3. Always join through `quran-data/data/bridges/qac-masaq.sqlite.gz`, sorted numerically.
- **Merged dictionary envelopes** repeat branch ids across their two roots.
- **The study dispute table is root-wide and noisy.** It applies ism's w-s-m dispute to samāʾ, and ḥ-y-w to all 189
  ح ي ي words. Reviewed, lemma-scoped records in quran-data `qac-dictionary-word-root-analyses.json` take
  precedence. Recommendation to the user: move the roughly 20 meaningful disputes into that reviewed format.
- **Grammar-facts partner roots contain errors** (وَلَهَا → و ل ي; فَإِذَا → أ ذ ي). Take partner roots from QAC.
- **digest_v2 omits the occurrences of common forms** ("common form, not listed"; e.g. ṣirāṭ).
- **Arabic is about 1 token per byte through `claude -p`.** Input bills at about $8/M as a one-hour cache write,
  output at $20/M.

## Reviews done this session (reports were in the conversation; scratch files are not kept)

- **Sonnet code review of every v12 script**, v9/v11 dependencies and root-dossier: all findings fixed.
- **Sonnet design review** of the dossier. Its useful points are merged below; its examples had wrong ids (MASAQ)
  and wrong branches.
- **Opus 5.5 design assessment.** Its lasting recommendations, with the interpretive parts dropped:
  - disjoint groups, one branch each;
  - a closed, part-of-speech-neutral set of context roles (who, what, to, from, by, of, gov, qual, how, when,
    before, then, speech, scene), used only to state what the ayat say;
  - signature sampling and an assign pass;
  - grammar-facts lines with a correction export;
  - a usage.md cap of about 2 KB per root and 10 KB per ayah;
  - the digest pointer and the hft annotation;
  - a known-answer scorer;
  - grammatical number in the form cells (ʿurūsh occurs only in the ruin formula).

## Commands

```
python3 _commentary/v12/inputs.py 29:45            # evidence only, prints sizes
python3 _commentary/v12/run.py ayah 29:39,29:41,29:45 --parallel 3
python3 _commentary/v12/run.py surah 1 --parallel 7
python3 _commentary/v12/run.py status 1
cd /Volumes/OZTURK/_projects/root-dossier
python3 build.py index ; python3 build.py packets --list lists/micro.txt
python3 run.py all --list lists/micro.txt --parallel 6 ; python3 run.py status --list lists/micro.txt
python3 deliver.py ayah 15:29 ; python3 deliver.py map --out out/activation_map.tsv
```
