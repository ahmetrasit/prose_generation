# V12 working notes (handoff)

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
- The root-dossier workflow is a standalone repo: `/Volumes/OZTURK/_projects/root-dossier` (user decision).

## Next
1. Root-dossier pilot (Luna; the user runs it) → `usage.md` appears in v12 inputs automatically.
2. S29 probe, then S1 (README "Test plan"); each needs the user's go.
3. Open: the long-surah surah pass runs per passage window; a whole-surah map over the windows is not built
   (V11 NOTES "Long surahs").
