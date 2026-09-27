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

- quran-data `2f01f7e05` maps the other minor alternatives (إِلَٰه, the ibn family, حَيَوٰة, حَيَوَان); root-dossier lets a
  reviewed pair define its scope (ح ي و now 77 words, not the table's ḥayy); names from the quran-apps catalogue.
- One package per root (user decision): every occurrence in one grouping session; micro run = 7 sessions per arm plus
  repairs. Work folders rebuilt (reviewed alternatives in 01_dictionary.md).

## 2026-09-27 (evening): first real Luna run — 10-root test (IN PROGRESS)
- Run: `cd /Volumes/OZTURK/_projects/root-dossier && python3 run.py all --list lists/test10.txt --parallel 10`
  (plain arm only; started 22:33; log `logs/test10.run.log`; outputs in `out/`, NOT yet committed). Roots: the micro
  seven (ح م ء, ن ف خ, ر ب ب, ص ل و, ع ر ش, و س م, و ل ه) + Fātiḥa ع و ن, غ ض ب, ص ر ط. The run started with the old
  code (one automatic retry, two repairs); the rules changed during it (below).
- 9 of 10 done by 22:42 (no failures, no salvage; repairs only for و ل ه and ص ر ط). ر ب ب (980 occurrences, one
  321 KB package) still running at 23:20: Luna builds a Python classifier over quran.txt (regex for رب forms, own
  word numbering skipping pause marks, rule groups such as "cosmos" = rabb al-ʿālamīn, hand cases for Yūsuf's master
  12:23/12:41/12:42/12:50); read nothing outside its folder.
- Score (`python3 _commentary/v12/eval/score_dossiers.py`): 0 mixed groups; all expected branches; both repeated
  phrases recorded; ḥamaʾ records the variant ḥāmiya; Luna split 18:42 (garden on trellises, B003) from the towns on
  their roofs, which corrected the answer key.
- Fragmentation (groups ≈ one per ayah: ص ر ط 34/45, ص ل و 52/99, غ ض ب 17/24, ع و ن 10/11): user decision — keep
  (avoid over-consolidation); check ر ب ب's result for it.
- Fixed after the run (future runs only): minor-lemma `b` = the branch the disputed derivation draws on, lemma copied
  exactly (و ل ه's first answer used `none` and transliterated lemmas; its repair set B001 but kept a contradicting
  note); repairs keep unflagged minor b/note; lint flags only "reveals that/how" ("revealed" cost ص ر ط a repair).
- User rules (memory `no-reruns`): never rerun a failed session or run (report instead); at most one repair session
  (root-dossier REPAIRS = 1, no session retry; v12 one tag-repair call). Examples in prompts never from test roots.
- When ر ب ب finishes: check its status (repairs, salvage, residual, id mismatches from its own numbering), its
  groups (constructions vs stated contexts; fragmentation; the rabb classes in known_dossiers.json), rescore, read
  usage.md for 1:2, 1:5, 1:6, 1:7, then commit root-dossier `out/` + `lists/test10.txt` and write the user one short
  summary (what works, what to fix). If it failed: report, do not rerun.

## Next
1. Finish the 10-root test (above): summary to the user; the word-analysis arm only if the user asks.
2. S29 probe (needs the user's go), usage on and off.
3. Pilot (54 roots), then S1 in full with the surah pass.
