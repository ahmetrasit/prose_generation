# Bible pathway decisions

## 2026-10-05 — original surah images are the Bible research target

The user agreed to continue S1 and start S87 using the **original completed r13
image commentary** for the surah Bible pass. The surah image augment9s is not a
prerequisite for this pass.

- The image augment9s adds Qur'an-to-Qur'an references and explanatory prose.
  The Bible pass independently checks connections against available Hebrew,
  Greek and other identified witnesses for the original image commentary.
- Bible research on the original images is valid, but does not claim coverage
  of ideas introduced only by the later augment prose. Those additions may
  receive a separate, focused Bible pass later. That pass has not been launched.
- Keep the current S1 discovery and author work. Resume the interrupted native
  sessions on the same frozen base; do not discard or relabel their evidence.
- Start S87 Bible discovery on the already prepared original-image pack. The
  earlier instruction to wait for S87's image augment was superseded by the
  explicit agreement to resume S1 and start S87 on this basis.
- The ayah pathway remains different: it uses completed augment9 ayah
  commentaries. S87's pack has all 19 of these, alongside its 18 original image
  sections. Both readers' jobs for all 37 targets are prepared.
- The session's surah authors use Sol (`gpt-6-sol`) at max effort, one agent per
  image, in parallel. Discovery uses the configured Luna/Terra max pair. No
  alternative model is silently substituted after a capacity error.
- Frozen inputs and paragraph anchors remain authoritative. A later combined
  presentation with the Qur'anic augment must verify both layers explicitly;
  do not swap a frozen base or its provenance to pretend it was read earlier.

All implementation, source caches, run records and outputs remain under
`enrichment/bible/`. The shared enrichment pathway and v16 are read-only inputs.

## 2026-10-09 — r13 ayah base, Hebrew root layer, Luna/Sol readers, Claude Code route

The user asked to complete this pathway and run it on S103 from the Claude Code enrichment session, "based on
frozen paragraphs", using Hebrew/Semitic characteristics to reveal parallel or related readings that explain the
ayah, or discrepancies between what the ayah says and the Bible's version. On augment9 the user said: "it will be
added when exists, but it will not be part of the enrichment".

- **Ayah base = the frozen r13 reading** (`pack.py --ayah-base r13`): the same file the v9 Islamic pages use
  (`_commentary/v16/out/S_A/*/S_A.reading.tr.md`, never an augment). Paragraph numbers were checked to agree
  with v9's on all 26 r13 pages of S1, S87 and S103, so Bible and Islamic blocks anchor to the same paragraphs.
  Augment9 packs (S1, S87 pilots) keep their behaviour; `base.json` records `ayah_base`. The surah target stays
  the original r13 images (2026-10-05 decision).
- **Hebrew root layer** (`hebrew.py`, Open Scriptures Hebrew Lexicon, CC BY 4.0): WLC lemma → lexicon entry →
  root, BDB heads, every occurrence; Arabic root → Hebrew/Aramaic roots by regular sound correspondences, kept
  only when the lexicon has them, labelled "BDB cites an Arabic cognate" or "sound correspondence only". Each
  target gets a deterministic Semitic root table of every Arabic root its frozen text cites; discovery readers and
  authors use it, and authors must record one decision per root (`root_verdicts.jsonl`, checked).
- **Readers Luna max + Sol high** for new attempts (`discovery.py --readers luna,sol`, fixed per attempt in
  `readers.json`), replacing Terra explicitly: Terra has no saved rate, and the user requires every Codex run's
  API-equivalent cost to be reported ("codex usage is counted"). Earlier attempts stay Luna/Terra.
- **Claude Code route:** `discovery_exec.py` runs the same two-turn protocol through `codex exec` (turn 2 with
  `codex exec resume` in the same session, verified to append to the same rollout file), with an automatic
  tool-policy review before finish; `image_enrich.py run` runs the Sol max image authors the same way. Ayah page
  authors stay Opus high, spawned by the orchestrator with the generated `spawn.md` text.
