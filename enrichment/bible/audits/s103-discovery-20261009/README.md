# S103 Bible discovery — Luna max + Sol high via codex exec (2026-10-09)

First run of the Claude Code route (DECISIONS.md, 2026-10-09). Base: the frozen r13 readings of 103:1–3 (the
paragraphs the v9 Islamic pages use) and the 15 original r13 image sections. Every package carried its
Semitic root table (`hebrew.py`).

- 36 reader sessions (18 targets × Luna max, Sol high), each two turns in one session (`codex exec`, then the
  fixed follow-up with `codex exec resume`). All 36 finished; 34 `ok`, 2 `accepted` after a follow-up repair.
- 5,415 candidate connections (Luna 2,039, Sol 3,376) in 19 handoffs (3 ayat, 15 images, the combined surah).
  By kind: motif 4,417, soydas (shared root / cognate) 511, yorum_gelenegi 210, karsi_anlati 160, paralel 117.
- Cost (API-equivalent, counted from each session's rollout): **$8.91** (Luna $0.93, Sol $7.97) against an
  expected $18.90. Per target and reader: `report.md`.
- Four locator-only corrections were accepted (`repairs.accepted.json`), each verified against the local
  WLC/SBLGNT/KJV text, with no change to grade, kind, basis or explanation. They were accepted by the Claude Code
  orchestrator under the user's production go and are listed here for the user's review:
  - 103:1 Luna, first turn, line 64: `WLC:Num.16.48` → `WLC:Num.17.13` (English → Hebrew numbering);
  - sec4 Luna, first turn, line 49: `WLC:Wisd.3.1` → `Wisdom of Solomon 3:1` (not a WLC book; as in S87 wave2);
  - sec9 Luna, follow-up, line 10: `WLC:Ps.120.8` → `WLC:Ps.120.7`;
  - sec5 Luna, follow-up, line 38: `SBLGNT:Jude.3` → `SBLGNT:Jude.1.3`.
- Tool policy: every session passed the automatic review (`policy_review.json` per session). 35 notes were
  recorded: readers checked or reordered their own TSV with short local python/perl scripts, one read the
  clock and waited on a command, one used a scratch file in the system temp directory. No network, repository
  script, model or other-file access.
- Operational note: an early wait loop timed out while the first runner was still working, and a second runner
  was started; `discovery_exec.py` now takes a per-session lock. The ledger shows exactly one finish per session
  (36) plus the two follow-up repair records.

Runtime evidence (packages, prompts, turn streams, rollouts' paths, tool calls, run logs) is under
`work/s103/discovery/s103-20261009/` (not versioned, as for S1/S87); this directory keeps the report, repairs and
this summary.
