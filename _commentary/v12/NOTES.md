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

## 2026-09-27 (evening): first real Luna run — 10-root test (DONE 23:31)
- Run: `cd /Volumes/OZTURK/_projects/root-dossier && python3 run.py all --list lists/test10.txt --parallel 10`
  (plain arm only; started 22:33; log `logs/test10.run.log`; outputs in `out/`, NOT yet committed). Roots: the micro
  seven (ح م ء, ن ف خ, ر ب ب, ص ل و, ع ر ش, و س م, و ل ه) + Fātiḥa ع و ن, غ ض ب, ص ر ط. The run started with the old
  code (one automatic retry, two repairs); the rules changed during it (below).
- 9 of 10 done by 22:42 (no failures, no salvage; repairs only for و ل ه and ص ر ط). ر ب ب (980 occurrences, one
  321 KB package) still running at 23:20: Luna builds a Python classifier over quran.txt (regex for رب forms, own
  word numbering skipping pause marks, rule groups such as "cosmos" = rabb al-ʿālamīn, hand cases for Yūsuf's master
  12:23/12:41/12:42/12:50); read nothing outside its folder.
- 23:08 (real clock; earlier "23:15/23:20" were elapsed-time misreadings): ر ب ب still running (34 min, 38 tool
  calls), refining hand cases — 2:258 (Ibrāhīm vs the king), 6:76–78 ("this is my Lord" of star, moon, sun), Yūsuf's
  master, 14:44. Background task in the old session; check with `python3 run.py status --list lists/test10.txt` and
  `ls -lt logs/ربب/` (a live `codex exec -m gpt-6-luna -s read-only` process = still running; never kill it).
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
- ر ب ب finished 23:31 (57 min; 2 sessions: 1 repair for 2 unplaced ids; 8.6M input tokens, 8.1M cached; 179K out).
  35 groups, 0 mixed with the known classes, branches B001/B003 rabbāniyyūn/B004 ribbiyyūn/B005 rabāʾib right.
  Found: the big groups are broad genres ("People refer to their Lord in statements, questions, and accounts of
  events", 209 ids) rather than stated contexts; membership errors (2:129:1, "Our Lord, raise among them a
  messenger", sits in "Prophets tell their people they are messengers from the Lord of the worlds", while 26:16 and
  43:46 sit in the 209 catch-all). usage.md for 1:2 (PER_ROOT 2000) shows 12 of 35 groups and hides the master /
  arbāb / Pharaoh groups. Dossiers are not authoritative for the writer (user, 2026-09-27).

## 2026-09-27 (night): next dossier run — remaining S1, 29:38-45, 18:83-99 (DONE 01:4x)
- User's plan (replacing "all of S1, S29, S100"): the remaining roots of S1 without ء ل ه (the user: do not include
  "Allah"; the whole root is skipped, so إِلَٰه and ٱللَّهُمَّ have no dossier either), then 29:38-45, then 18:83-99, in
  that order. `root-dossier/lists/next.txt`: 113 roots (14 + 49 + 50; 111 Luna sessions, 1 hapax batch for ر د م,
  ج ي ء script-only). Started 23:25 with
  `python3 run.py all --list lists/next.txt --parallel 10 > logs/next.run.log` (pool.map starts roots in list order).
  Largest packets: ء م ن 378 KB, ع ل م 325 KB, ق و م 255 KB, ء ت ي 237 KB. Expect several hours.
- Check: `python3 run.py status --list lists/next.txt`; never kill a live `codex exec -m gpt-6-luna` process.
- When it finishes: failures (report, no rerun), repairs/salvage/residual, lint flags, fragmentation on the big roots;
  commit root-dossier `out/` + `lists/next.txt`; one short summary to the user.

## 2026-09-27 (night): v12 takes the dossiers as a map, not a verdict (user decision)
- The user: the Opus writer must not treat the root dossiers as authoritative (errors are possible; ر ب ب showed
  some). Done: write.md says where each input comes from; usage.md separates script facts (occurrences, ids,
  counts, forms, dictionary branch lines) from the model's grouping (groups, labels, branches, exceptions, minor
  notes, the ▶ group, never-plain branches); the writer checks what it builds on and records dossier errors as
  `usage.md: …` ledger lines (kept off the reader's page; check.txt `dossier_corrections`, for root-dossier).
  "How large a group is" dropped (fragmentation accepted, sizes mean nothing). surah.md likewise.
- deliver.py: every group of every root is listed (PER_ROOT removed; ids abbreviated; PER_AYAH 60 KB as a safety cap);
  roots of the ayah without a dossier are named (ء ل ه by the user's choice). digest_v2.md is no longer replaced by
  pointers (its claim "every occurrence… see usage.md" was false under the old cap; the digest is small and
  script-made, a cross-check).
- run.py (v12): never twice — an ayah whose call started (writing/checking/done/failed) or a surah window whose pass
  started is never called again (the surah command used to rerun the surah pass every time); `--force` removed.
- Not changed (no rerun): the و ل ه minor note for ٱللَّه contradicts its branch (B001 vs "no branch states it").
- To do when the S1 roots are done: prep 1:1-7, read usage.md, check sizes and estimates, ask the user's go.

## 2026-09-27: v12 S1 run (first Opus run) — DONE
- The user's go: S1 if every ayah estimated below $5 (estimates $2.21-3.06). `run.py surah 1 --parallel 7`, 23:56-00:22.
- All 7 ayat done, no failure, no repair call, nothing stripped; verify all exact/fixed (0 missing, 0 bad-source).
  Costs $1.81-3.22 per ayah ($18.35) + surah pass $2.61 (1 repair) = $20.96. 1:5 cost $3.22 on a $2.61 estimate (102K
  output tokens; the output guess of 60K is low: calibrate).
- Ledgers 80-124 findings per ayah (new 7-12); readings 1,875-2,793 words; surah reading 5,125 words, 19 chains.
- 27 dossier corrections recorded by the writers (`out/s001/dossier_corrections.md`), many credible: 12:23 is not
  the king (ر ب ب); 1:4 mālik given B003 where the form carries B002 (م ل ك); ي و م "never plain" B005 while
  yawmaʾidhin is exactly it; 100:3 مغيرات is غ و ر, not غ ي ر (a QAC root question); the basmala / raḥmān-raḥīm
  formula and the calf scene split over several groups; ع ل م "Lord of the worlds" split in four groups.
- Render fix: any ledger line mentioning usage.md stays off the reader page (one mid-sentence mention on 1:6 leaked);
  pages re-rendered by script.
- Next: the user's read; an Opus judge and the blind read against v11/v5 (`_commentary/v11/eval/s001_anchors.md`)
  only on the user's go.

## 2026-09-27: dossier run next.txt — DONE (113 roots, 23:25-01:4x)
- 113 done, 0 failed; 54 used their one repair; 9 salvaged (1-5 items: ر س ل 5, ظ ل م 3, others 1); 0 lint.
  30.3M input tokens (22.0M cached), 3.9M output.
- Shape: splitting is the common failure (39 roots have more than one group per two uses: ر ح م 202 groups / 339,
  ج ع ل 252 / 346, ء م ر 140 / 248, ض ل ل 133 / 191 …); the three largest roots go the other way, one catch-all
  holding most uses (ء م ن 810 / 879, ع ل م 722 / 854, ق و م 383 / 660). Both reach v12 as a map, not a verdict.

## Next
1. Finish the 10-root test (above): summary to the user; the word-analysis arm only if the user asks.
2. S29 probe (needs the user's go), usage on and off.
3. Pilot (54 roots), then S1 in full with the surah pass.
