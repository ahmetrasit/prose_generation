# S103 Sol max image authors — accepted surah page (2026-10-09)

One Sol max author per original r13 image section (15), run through `codex exec` from the Claude Code session
(`image_enrich.py run`), on the S103 discovery handoffs (`../s103-discovery-20261009/`) and the local witnesses
(WLC, SBLGNT, KJV as finding aid, the Sefaria texts of the named Jewish works fetched for this run).

- Accepted page: `accepted/surah.ehlikitap.md` — **207 annotations** over the 15 images (motif 148, soydas 47,
  paralel 7, karsi_anlati 4, yorum_gelenegi 1), **4,479 verdicts** (accepted 763, rejected 3,347, unavailable 366,
  unresolved 3) covering all 4,325 image discovery connections plus the authors' own research lookups.
- Semitic root table: 67 root decisions across the images (used 44, no_qualifying_parallel 10, false_friend 8,
  no_hebrew_cognate 5), in `accepted/surah.ehlikitap.root_verdicts.jsonl`; 47 blocks are shared-root (soydas)
  blocks quoting the WLC wording, each naming its basis (BDB note or sound correspondence).
- Cost (API-equivalent, from the rollouts): **$54.27** against an expected $22 (≈ $3.6 per image; the S103 images
  carried 210–375 connections each). Per image: `result.json`.
- Six images failed their first finish and were fixed once (`image_enrich.py fix`, approval recorded in each
  run log; listed here for the user's review):
  - sec1, sec3, sec4, sec8, sec14: only operational reads outside the old grammar (listing the author's own
    preview, `image_enrich.py check --help`, print-only `sed -n '/ID/p; /ID/p'` searches of the author's own
    files). The grammar now allows exactly these; the sessions were re-audited with no model call.
  - sec9: two verdicts cited WLC:Exod.33.11 and WLC:Ezek.37.22 without opening them. One same-session fix turn
    (`codex exec resume`, the exact message in `fix-message.txt`) opened them and corrected the ledger; the
    failed log is preserved as `run.failed.json`.
- `image_enrich.py run` printed `sec14: WARNING started earlier without a completed turn` because sec14 was
  running as a pilot in another process at the time; it was finished by the pilot.

`evidence.tar.gz` holds every image directory (frozen inputs, prompts, turn streams, native events, tool calls,
deliverables, previews, run logs, fix records). The parent has not yet made an editorial review of the prose
and quotations; semantic review is still needed before publication.
