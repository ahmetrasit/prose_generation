# V12 status log

Start with `HANDOFF.md` (rules, state, decisions, remaining work); the orchestrator's procedure is `RUNBOOK.md`.
Known answers are in `eval/` — never put `eval/` or this file into a model's input.

## 2026-09-26
- Built `inputs.py`, `run.py`, `prompts/write.md`, `prompts/surah.md`; smoke-tested with stubbed model calls; a Sonnet
  review's 2 high and 5 medium findings fixed (`e1db28897`). Dictionary: merged envelopes read by V9 `prepare.py` and
  V11 `verify_src.py` (`4f31e2ba9`).
- root-dossier repo built (stage A/B design), stub-tested; no Luna run.

## 2026-09-27
- Review of both workflows against the data (handoff claims doubted and checked):
  - the old sampling left 13 pilot-ayah occurrences and all of rabb's telling uses unread;
  - the study dispute table applied rows that name no word to whole roots (āya → ء و ي on 382 words …);
  - HFT: 90 surahs in `latent_activation/focus_trace/runs`, only 64 in `bundles/` (v12 read bundles);
  - the writer could retry a $4 failed call and did not count repair calls;
  - the known answers expected interpretation, and missed Yūsuf's throne (12:100).
- v12: HFT read from `focus_trace/runs` (identical to bundles where both exist); cost rule (a call starts only below
  the $5 estimate, never retried; estimate calibrated on finished calls; repair costs counted); `--estimate`,
  `--no-usage`, `--tag`; `RUNBOOK.md`; usage.md described as a descriptive concordance in the briefs; digest pointer
  for dossier roots; hft.md steps marked with the plain branch and usage group; `DOSSIER_OUT` for dossier arms;
  known answers as id sets (`eval/known_dossiers.json`) with a scorer (`eval/score_dossiers.py`).
- root-dossier rewritten descriptive: one grouping pass (stage B dropped; word analysis as an arm, `--wa`), budget and
  signature sampling, assign pass, one-occurrence batches, stop lemmas, headwords, disputes limited to named words,
  one branch per minor lemma, new usage.md (≤ 2 KB per root, ≤ 10 KB per ayah), known answers out of reach of the
  packets (Luna sees only quran.txt in its working directory). Stub-tested end to end.
- quran-data now has the four Furūq entries (ب ن و root_001959, ه ي د root_005125, و ل ه root_005296, ح ي و
  root_005544), but no root names for them (neither in the entries nor in quran-slm's list) and no reviewed word-root
  records pointing at them, so nothing reaches them yet.

- The four Furūq roots: names by fallback in V9 `prepare.py`, V11 `verify_src.py` (tags citing them verify) and
  root-dossier; root-dossier gives them tier-M dossiers from the study table (و ل ه 2,815 words: ٱللَّه, إِلَٰه; ب ن و 60;
  ح ي و 36, the wrong lemmas; ه ي د none); usage.md now lists a minor root's branches beside each word's minor analysis
  (so 29:41's ٱللَّهِ shows و ل ه's four branches); write.md allows quoting usage.md's branch lines. HFT predates the
  four roots and cannot cite them.

- quran-data `ae9e79c54` adds a reviewed alternative for ٱللَّه (و ل ه B001, Tahdhīb). Found: V11's prep builds
  `01_dictionary.md` once and never refreshes it, so v12 was reading dictionary input frozen at its first build; v12 now
  rebuilds it into its work folder at every prep (1:2 38.7 → 42.8 KB with و ل ه). All work folders rebuilt.
- root-dossier: spelling-twin lookup table (11 merged envelopes, 20 duplicate branches), weak-letter minor roots
  labelled, usage.md shows the dispute note and points to 01_dictionary.md for reviewed alternatives.

## Next
1. Micro run, two arms (the user runs Luna; root-dossier RUNBOOK), then score both.
2. S29 probe (needs the user's go), usage on and off.
3. Pilot (54 roots), then S1 in full with the surah pass.
