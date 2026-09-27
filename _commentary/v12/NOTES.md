# V12 working notes (handoff)

Start with `HANDOFF.md` (rules, state, decisions, remaining work). This file keeps the status log and the
known-answer checks — never put it into a model's input.

## Standing instructions from the user
- Target: `NORTH_STAR.md`. Every workflow decision is judged against it.
- The image chains already exist (HFT, channel reviews): never design or run a pass that rediscovers them.
- Fully automated: the orchestrator reads the runbook and starts/stops runs; no hand fixes of inputs or outputs.
- Tell the user and get confirmation before any Opus run the user has not asked for; nothing may cost $5 or more
  per ayah. GPT agents (Luna/Sol) always at max reasoning; never restart running agents; the user runs Luna.
- Commit and push after each major step (work on main).

## Status (2026-09-26)
- Built: `inputs.py`, `run.py`, `prompts/write.md`, `prompts/surah.md`, README. Smoke-tested without model calls:
  inputs for 1:1, 1:7, 29:45, 18:86, 100:1; the check/repair loop (comma fix, wrong-source fix, repair rounds,
  last-resort strip) with a stub model; render on V11's 1:7 outputs; the S1 surah pass input assembly (≈ 265 KB).
- Not run yet: no v12 Opus call has been made.
- Word analysis: the per-word summaries (`word_analysis/outputs/production`, 6,236 ayat) are used, not the 1.2M
  CRITICAL rows (user decision; checked on ḥamaʾ: the summaries keep the cross-occurrence topic "rare mud field and
  echoes", the raw rows add only the voice detail, which the dossier's stage A reads from the ayat).
- The root-dossier workflow is a standalone repo: `/Volumes/OZTURK/_projects/root-dossier` (user decision; local
  git, no remote yet). Built and smoke-tested with a stub model (validation, two repair rounds, salvage, stage B
  provenance and restore, final, delivery into v12's usage.md). Pilot list: 51 roots (1:1–7, 18:86, 29:39, 29:41,
  29:45); micro list first: 5 roots (ḥamaʾ, nafakha, rabb, ṣalāh, ʿarsh). Stage A also writes the canonical branch
  map (one branch per occurrence for the plain Ḥafṣ reading). GitHub: ahmetrasit/root-dossier (private). No Luna
  session has run; the user runs it (root-dossier RUNBOOK.md).

- Dictionary fix (2026-09-26): quran-data stores some roots as merged envelopes (`root_001210--root_001211_entry.json`:
  ق ر ء, ش ي ء, ج ي ء, م ر ء, ب ر ء, ب د ء …, 11 files) plus supplemental roots; V9 `prepare.py` and V11
  `verify_src.py` only looked for single-id file names and missed them. Both now read every entry file (each root of
  an envelope keeps its own branches). 96:1's dictionary now has ق ر ء. Merged roots repeat branch ids across their
  two root ids, so a `source:ق ر ء B001` tag matches either root's B001; the root dossiers name branches by full ref.
- Root dossiers are now QAC-anchored (QAC word ids, full branch refs, the QAC–MASAQ bridge for word analysis and
  variant readings, disputed roots with the minor analysis mapped to the minor root's branch, compact patches). The
  micro list has 6 roots (و س م added for the disputed-root path, ism).

## Known-answer checks (kept here, out of the root-dossier repo, so no Luna session can read them)
- ḥamaʾ (ح م ء, key حمء): the dossier should say that its three noun uses are the material of man in S15's creation
  account — narrated (15:26), in God's words to the angels (15:28) and in Iblīs's refusal (15:33), always in the
  formula «مِّنْ حَمَإٍ مَّسْنُونٍ» with ṣalṣāl — and that 18:86, the only adjective, is the outlier (a spring seen by
  Dhū al-Qarnayn at the sunset), with the creation material as what the pattern brings in.
- nafakha (ن ف خ, micro list): two scenes should separate — the breath of life (into Ādam 15:29, 38:72, 32:9; into
  Maryam 21:91, 66:12; ʿĪsā into the clay bird 3:49, 5:110, which echoes Ādam's creation) and the trumpet of the Hour
  (e.g. 18:99, 39:68, 69:13); plus the bellows at 18:96. Voices: God speaking of His own breath vs narration of the
  trumpet.
- ʿarsh (ع ر ش, micro list): the Throne (istawā ʿalā l-ʿarsh …) vs human roofs and trellises (maʿrūshāt 6:141;
  yaʿrishūn 7:137, 16:68); the formula «خَاوِيَةٌ عَلَىٰ عُرُوشِهَا» (2:259, 18:42, 22:45) — roofs always in ruin scenes —
  and the Queen of Sheba's throne (27:23, 27:38–42) as a human throne tested.
- S29 probe (v12 writer): the race of 29:39 (not outstripping) with ṣalāh at 29:45 (ص ل و "the one who comes second
  in a race") and the houses of 29:41; in neither HFT nor the channel review.

## Next
1. Root-dossier pilot (Luna; the user runs it) → `usage.md` appears in v12 inputs automatically.
2. S29 probe, then S1 (README "Test plan"); each needs the user's go.
3. Open: the long-surah surah pass runs per passage window; a whole-surah map over the windows is not built
   (V11 NOTES "Long surahs").
