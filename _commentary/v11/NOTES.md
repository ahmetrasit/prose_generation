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

## Built 2026-09-26 (user: "build it"; user asked to wait before any model call)
REVIEW.md plan, items 1–5 + arms. No model call made yet.
- `seeds_input.py` (script): window evidence = branch table (every branch of every root; ~57 KB for S1), compact HFT,
  surface staging (dictionary synonym/same-field neighbours widen each branch's image words; S1 finds 16:5–10,
  7:50–55, 14:32–37, 30:50–55 …), definitional links; pairs off by default. Long surahs: pericopes ±7 ayat overlap
  (so 29:39 sābiqīn ↔ 29:45 ṣalāh (ص ل و B006 "second in a race") ↔ 29:58 fall in one window).
- `lines/digest.py --v2` → digest_v2.md (ref — review note; strong→weak; "no value" rows dropped; no openings).
- `prompts/seeds.md`, `prompts/write_s.md` (Limits family, seeds check, loss / position / disclosure, 4-field tags
  with `source`), `prompts/surah_s.md` (one section per core chain, explicit provenance, maqṣūd, next surah).
- `verify_src.py`: each tag checked against its declared source (S:A or `root Bnnn`), --fix.
- `run.py --arm B|D|S|S0|Srep`, step `seeds`; `surah` now runs chains; CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000;
  ledger entries get paragraph pointers [¶ n] (non-B arms).
- `eval/s001_anchors.md`: frozen anchors (G gold 26+6, V5/V11 per-ayah lists, N north-star).
Reviewer check (same session): fixed the S1 leak (the seed prompt's Fatiha example → S103 ʿaṣr; writer source
example → 29:45 ص ل و B006), seeds_for reads wrapped members and appends the members' branch lines (quotable),
verify_src accepts ~ flags, staging counts own-root non-primary senses (score / roots^0.3; S1 top: 11:40–45,
16:5–10, 20:76–81, 6:139–144 …), definitional links print the matching phrase.
Simplified test (reviewer; D, S0, Srep dropped): 1) `run.py seeds 1 --arm S` (≈ $1.3) → read the sheet against the
gold (gate); 2) `run.py surah 1 --arm S` (≈ $15, incl. chains); 3) Opus judge vs current v11 and v5 with
eval/s001_anchors.md (≈ $8); 4) the user reads 1:4, 1:6, 1:7 blind. ≈ $25 total. Each step needs the user's go.
Pending the user's yes: seed probe on S29 window 38–63 (≈ $1.3).

## Long surahs (80–110 ayat; cross-pericope echoes) — design reviewed 2026-09-26, not built
Order: window seed passes first (pericopes ±7, split at story boundaries, e.g. keep 18:60–82 whole) → one
whole-surah **map** call (surah text + recurrence index + window seed sheets) → writers get window seeds + map chains
through their ayah. Recurrence index (script, surah-internal only; Quran-wide parallels already reach writers via
digest): repeated phrases ≥ 2 words, Quran-rare roots recurring in the surah, non-primary branches of one identity
root; ≥ 2 non-adjacent pericopes; cap ~60 lines; each window also gets its own index lines. Map brief: a return
counts only if the second occurrence changes the first (answer, reversal, completion, escalation); ~8–12 core chains,
the rest an ungraded note list; no S18 example in any brief. Deferred: latent recurrence matching, two-tier chains
pass (window chains → surah pass; loses ledger findings no window chain took up — record it), Luna filter.
Test later: S18 seeds + map only (≈ $8–12) against frozen known echoes (rashad 18:10/24/66, ḥattā idhā 18:71/74/77/
86/90/93, cave/wall/barrier); count core chains vs notes.

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
4. Cost at scale (user-approved direction, 2026-09-26): production via the Messages API in batch mode, shared
   surah prefix first + explicit cache_control marker + ayah part last, one fresh call per ayah (README "Production").

## Results so far (details in README.md)
- S1 v11 (done): 7 ayat $11.92 + chains $1.06 (18 chains). vs v5 (`compare_s001_v5.md`): 53% of v5 prose refs also
  in v11; v11 525 ledger refs. v5-only = concept-level Quran search (mercy in practice, book of deeds/scale,
  misdirected help) and limiting verses (57:15/6:70 vs dīn-as-debt, 2:256, 7:186/18:17 vs ḍāllīn self-caused).
  Proposal (not applied): writer ledger adds a "concept" search and a "limits/counter-verses" section.
- Root cause of the v5-only refs (checked 2026-09-26): every one is in v5's global input (connection_registry,
  from 09_inter_ayah review rows) AND in v11's digest — but the digest keeps only ref + 60 chars of opening Arabic,
  dropping the review label and the one-line note that says why the ayah is related (e.g. 3:159 "makes mercy visible
  in relational gentleness"; 57:15 "refusal of ransom"). ~90% of the digest is this reasonless list.
  Proposal (not applied): digest lines = ref + label + note (no Arabic opening; Opus quotes from memory, verified);
  add 02_hft.md as seeds where the surah has HFT (S1, S100, 18, 29, 5, 103 have it; 4:34 not). Earlier dhft test
  (1:2, 103:1) was under the v10 reading-only prompt, not v11's ledger — untested in v11.
- 1:4/1:6/1:7 ran 2 turns (output > the per-turn cap; the continuation re-bills ~33k tokens as cache write, ~$0.5).
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
