# V11 working notes (handoff, 2026-09-26)

## Standing instructions from the user
- Do not change the v11 workflow until the user agrees (proposals only).
- Tell the user and get confirmation before any new Opus run the user has not asked for.
- Nothing may cost $5 or more per ayah.
- Commit and push after each major step (work on main).
- GPT agents (Luna/Sol) always at max reasoning; never restart running agents.

## In progress
- S1 (Fatiha) v11 run + chains pass, started as a detached process:
  `python3 _commentary/v11/run.py surah 1 --parallel 7; python3 _commentary/v11/run.py chains 1`
  Log: `_commentary/v11/out/s001.run.txt`; outputs `_commentary/v11/out/s001/`. Check the log; if a run failed,
  rerun only that ayah with `run.py all 1:N` (then `chains 1`).

## Next steps agreed
1. Compare S1 v11 (ledgers + chains) with Astra's v5 findings indexes in quran-data:
   `quran-data/data/commentary/ayah/detailed/tr/s001/1_N.index.tr.md` (v5 prose there is byte-identical to
   `_commentary/v5/editorial/s001-fresh-20260910/s001/1_N/1_N.prose.editorial.tr.md`). Report findings-level
   differences (what each has that the other lacks), not prose.
2. Proposal (not applied): the surah commentary must explain every chain explicitly — one section per chain naming
   its ayat, words and roles and what the chain shows — instead of a compressed summary (user: "too compressed, I
   cannot follow what is coming from where"). Also consider telling ayah writers to assume the surah reading exists
   (every S100 ayah reading re-tells the raid scene).
3. Blind read by the user of v11 vs the best earlier setup on a few ayat.
4. Cost at scale: `claude -p` bills input as a 1-hour cache write; direct API/batch would cut it.

## Results so far (details in README.md)
- S1 v11 (done): 7 ayat $11.92 + chains $1.06 (18 chains). vs v5 (`compare_s001_v5.md`): 53% of v5 prose refs also
  in v11; v11 525 ledger refs. v5-only = concept-level Quran search (mercy in practice, book of deeds/scale,
  misdirected help) and limiting verses (57:15/6:70 vs dīn-as-debt, 2:256, 7:186/18:17 vs ḍāllīn self-caused).
  Proposal (not applied): writer ledger adds a "concept" search and a "limits/counter-verses" section.
- S100 (11 ayat): $11.14 + chains $1.21. Validation vs cold / dictionary-only Opus (100:1, 100:6, 100:10): they
  cite almost nothing the v11 ledger lacks (2:36, 81:18, 47:4).
- S100 vs v5 (quran-data `…/s100/100_N.index.tr.md`): v11 covers v5's substantive points; v5 outside-surah refs
  5–19 per ayah vs v11 33–70. v5-only: the "ḍabḥan = at dawn" reading (not in our qirāʾāt source; v11 left it out),
  some HFT mechanism images (sprouting shoot, hoarded seed, sediment in the chest, spark as small dawn), echo-root
  items. v11-only: e.g. 100:1 38:31–33 (Solomon's horses, "ḥubb al-khayr"), ʿād/ʿādūn = transgressor across the
  Quran, sister oath-openings (79/51/77/37) vs 100/103 answers.
- 18:86 v11: $2.96 (219k input: dictionary 148 KB + digest); ledger 62 findings, 77 refs; 14/16 known anchors
  (missing 18:74 nukr, 34:12). New: "ḥattā idhā … qulnā" with 11:40 and 21:69. v5 18:86 has no creation/Iblis
  layer; v10 has no 18:86 prose. Comparison paths: v5 `quran-data/.../s018/18_86.prose.tr.md`; V9 arms in
  `_commentary/v9/lines/work/18_86/synth/*`; v11 `_commentary/v11/out/s018/18_86/`.
