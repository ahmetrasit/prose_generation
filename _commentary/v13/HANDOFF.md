# v13 handoff (2026-09-27, 15:10)

For a session picking this up cold. Read in this order: `NORTH_STAR.md` (repo root, revised today: the targets),
this file, `DESIGN.md` (the design, the Opus review changes §8, caching §9, effort max §10), then the code
(`packet.py`, `run.py`, `prompts/`). Doubt every line here; check it against the code and the outputs.

## Standing rules (the user's)

- Opus 5.5 at effort **high** (max failed: §10 of DESIGN; xhigh under test). Luna is not used in v13.
- A call starts only when its estimate is below $5; a started call is never stopped. **Never twice:** a step that had
  a call for an ayah in an arm is never called again (no `--force`). A call refused before any work (e.g. the
  subscription's session limit, 429, $0) may be restarted only with the user's go; set-aside files keep a suffix
  (`*.refused-429.*`, `*.cap64k.*`, `qeq.truncated.md`). At most one repair call per output.
- Known answers (S1 gold `latent_activation/s1-bulgular-tr.md`, `_commentary/v11/eval/s001_anchors.md`,
  `_commentary/v12/eval/`) never enter a model input; prompt examples never come from test material (S1, S29, S100,
  18:83–99, 5:6, 4:34, the micro roots). The first draft of `act.md` leaked the S1 water/road chains; fixed.
- Do comparisons yourself; do not spawn comparison agents (memory `compare-myself`). Commit and push before and
  after runs (main, both repos). Ask before unrequested Opus runs.

## What v13 is (built and tested today)

A funnel of Opus calls on a script packet (DESIGN.md §3):
- `packet.py` (step 0, scripts): per window (short surah = one window; long = pericope ± 7) `window.md` (text, the
  scan: every branch of every root, `Bnnn gloss | image`, the channel review excerpt); per ayah `ayah.md` (V9
  context focus part), `dictionary.md` (focus roots, one line per branch with definition), `pairs.md` (V9 image pairs,
  compacted), `concordance.md` (focus roots with ≤ 60 uses, every use with its clause), `hft.md`, `reciprocal.md`.
- `run.py`: `act` (step 1, activations: English records F<n>, no verdicts), `net` (surah network I<n> with a
  disclosure plan naming every member ayah and a role), `qeq` (step 2: annotates findings, tags `staging` /
  `same-word`, fourth-scope findings Q<n>, axis pass A<n>; references only), `write` (step 3: Turkish commentary +
  a coverage block against `mustland.md`, which a script builds from the network and the QeQ tags; unlanded items go
  to `handforward.md`), `seed` (reuse another arm's step-1 records), `status`. Options: `--tag` (arm folder
  `out-TAG/`), `--effort`, `--network-from TAG`, `--max-cost`. Output in parts: the system prompt caps a response at
  ~60K tokens; the model ends a part with `===== CONTINUE =====` and the runner resumes the session.
- Token accounting per call in each `*.status.json` (cache write/read, output, thinking, responses, minutes).
  **Cost of a call written in parts = the last part's `total_cost_usd`** (the CLI reports a resumed session's running
  total; fixed 15:05, all statuses recomputed).

## Snapshot of the test arms

| arm | what | ayat | state | cost |
|---|---|---|---|---|
| `out/` | first run, effort high, original briefs | step 1 on 1:1–7 + 18:96; network S1 (15 images); QeQ + prose on 1:4–7, 18:96 | done | $26.93 |
| `out-max/` | effort max | 18:96 step 1 | **failed**: 256K output, all thinking, 64K CLI cap per response (retried 4× inside the call) | $10.28 |
| `out-v2/` | fixes A–H (disclosure every member ayah; mustland + coverage; QeQ tags + axis pass; no reversals; no bullet tours; `scene` kind) | step 1 reused; network S1 (25 images); QeQ + prose 1:4–7, 18:96 | done (QeQ first cut off at the 64K cap on 1:4/1:6/1:7 → QeQ trimmed → redone) | $34.46 incl. set-aside calls |
| `out-xhigh/` | xhigh throughout, new briefs | 1:5 (network from v2) | step 1 done ($3.15), QeQ done ($4.96, 187K output), **prose running at 15:10** | $11.58 so far |
| `out-mixed/` | high step 1 (reused), xhigh network/QeQ/prose | 1:5 | done: network $3.05, QeQ $4.87, prose $3.50 (6 parts) | $11.42 |

All v13 testing: ≈ $95 (claude -p list prices; no cache hits).

Measured: 0.44 tokens per byte of packet; step 1 at high $0.65–2.24 (1:1–7: $0.65–1.43); QeQ at high $1.3–1.7;
prose at high $1.3–3.6; the S1 network $1.8–2.8; xhigh QeQ ≈ 3.5× high (≈ 185K output). `claude -p` gives no
shared-prefix cache hits (DESIGN §9): production needs the API with `cache_control` after the window part.

## Findings

### What went right
- **Discovery works.** Step 1 found nearly every gold and anchor item in every tested ayah (the road's way-marks,
  middle and trodden surface; the herd and the stray whose rabb is unknown; the water system including the 1:6
  well-frame, ق و م B012; the womb; cross-definitions such as mālik ↔ ʿabd; the balance), plus new ones. The losses
  happen after it.
- **18:96 found the Quran-loaded word unaided** (nafakha: 12 Horn, 5 breath into a shaped body, one craft use here;
  the shape → blow → make order of 15:29 / 32:9; "körükleyin" adds a tool the Arabic does not name; zubar's black
  mud linked to ḥamaʾ). No earlier version had this.
- **The first-run 1:6 is the richest 1:6 so far** (the Opus comparison): the gold's hidden road branches in one
  explained picture; the best Turkish-loss layer (sırat bridge vs sword, hidayet, doğru/istikamet, the two
  articles); arrested standing; prayer standing and the Rising. v12's QeQ strength is largely kept.
- The network assembles the images v12 lost (road, herd, water, womb, benefaction circuit, swallowing passage).
- Checks hold: every Arabic tag verified against its source, no internal ids in the prose, no unknown branches.
- The fixes land what the first run dropped: 28:22 (Mūsā asking for the road), 20:52, 16:15, 17:35 now appear;
  coverage 100%; no bullet lists.

### What went wrong
- **The prose step lost what the funnel had found** (first run, all five ayat): disclosure plans skipped member ayat;
  assembly points did not assemble (1:7's water in one sentence); QeQ's open stagings dropped; QeQ "none/shifts"
  turned into caveats or even reversals; root tours in bullet lists; image meetings unstated.
- **Fix A overshot:** the must-land list grew to 49–144 items per ayah (55 of 88 for 1:5 were tagged passages), and
  the v2 prose grew to 5.3–7.9K words (from 3.2–4.5K): catalogue pressure, the opposite of the north star. Tagging
  was too liberal (63–77 tags per ayah) and "use every tagged passage" too strict.
- **The water system still does not land as a system.** Even listed as must-land, 1:6 used ق و م B012 as a sword
  hilt; the well that appears is Yūsuf's (12:19).
- **The 64K output cap of the CLI** (not the model): effort max spent all of it on thinking (failed); the first
  trimmed-less QeQ at high hit it on thinking alone (the part protocol cannot help when thinking fills a response).
  The QeQ trim (references only; reciprocal check postponed; loss/grammar/fragment not annotated; no "none" lines)
  brought it back to 44–59K.
- **Cost:** ≈ $4.5–7 per ayah via claude -p for the three per-ayah steps at high (v2), far from ~$1; xhigh roughly
  doubles-to-triples QeQ. The estimate function is calibrated for input (0.45 t/b) but not for output growth.
- Operational slips (fixed): the runner imported its own `run.py` instead of v12's; a watcher with `exit` in its loop;
  a launch line that scoped variables to the first background group; cost double-counting over parts.

## Where we are against the north star

| target | state |
|---|---|
| Ground (plain sense, not disorienting) | good (all arms) |
| What Turkish loses (lexical; grammar when it matters) | good, better than v12 |
| Local resonance (ayah, window, surah) | good (step 1 + prose) |
| Image chains through the ayah's words, progressive disclosure | found and planned; landing now forced but bloated; the water system still not assembled as one scene; true progressive disclosure is not possible while the ayat are written in parallel without the earlier prose |
| Quran-loaded words | found for 18:96 (nafakha) from the concordance; 18:86 (ḥamaʾ) not yet tested |
| QeQ after the latent readings (support / expand / shift / contradict; never suppress) | works; staging passages now land; the reciprocal final check is postponed and not built |
| Surah commentary (images, ayat explained within them, interactions) | **not built** (step S) |
| Economics (~$1 per ayah; Opus high) | not met (≈ $4.5–7 via claude -p; ≈ half via batch, less with prefix caching) |
| Long surahs | not addressed (network per window + merge; step S per image) |
| English / German | not started (the analysis records are English; only steps 3/S are per language) |

## Overall assessment

The funnel's split is right: generative discovery (step 1) and the network are strong and recover what v11/v12
audited away, and 18:96 shows the loaded-word target is reachable. The weak joint is the handover from records to
prose. The first run under-delivered (things found, then dropped); the v2 fix over-delivered (everything forced in,
catalogue-sized). The next change should make the prose step select by payoff from a short, ranked must-land list,
not land everything. Quality is near or above every earlier version for 1:6 on content; length and cost are the
problems now, not discovery. Whether xhigh on synthesis helps is still open (the mixed 1:5 prose is done; the xhigh
prose was running at handoff time): compare the three 1:5 versions (`out-v2`, `out-mixed`, `out-xhigh`) before
deciding; xhigh costs ≈ 2–3× on QeQ.

## Next steps (in order)

1. When `out-xhigh` 1:5 prose finishes: compare the three 1:5 versions yourself (content: gold items for 1:5 in
   `s001_anchors.md`; length; readability; cost) and report to the user.
2. Correct the must-land rule (proposed, not yet agreed): only `staging` passages are must-land (`same-word` are
   suggestions); `touch` = one clause; full treatment only where the ayah `develops` or `assembles`; cap ≈ 25 items,
   ranked by the network (assemble > develop > meeting > staging > touch). Tag less in QeQ (only real stagings).
3. Decide the synthesis effort (high vs xhigh) from step 1's comparison.
4. Then the remaining test ayat (user's list): 18:86, 5:6, 4:34, 29:38, 29:41 (5:6 with the dilution arm: scan vs
   focus dictionary only).
5. Build step S (surah commentary) and the reciprocal final missing-passage check; the Batch API runner with
   `cache_control` after the window part; an output-aware estimate.

## Traps

- The CLI caps one response at 64K output tokens whatever `CLAUDE_CODE_MAX_OUTPUT_TOKENS` says; thinking counts.
- The subscription session limit (429) fails calls instantly at $0 and can cut a running call's continuation.
- `total_cost_usd` of a resumed session is cumulative (take the last); token usage is per response (sum).
- `claude -p` caches only identical whole messages; a staggered start buys nothing.
- `import run` inside v13 finds v13's own `run.py`; v12's runner is loaded by path.
- In a shell line `a && b && (x) & (y) &`, variables set before `(x)` exist only in the first background group.
