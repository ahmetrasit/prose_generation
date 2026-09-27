# v13 design (2026-09-27; nothing built yet)

Judged against `NORTH_STAR.md` (revised 2026-09-27). This page decomposes the targets, maps the data to them, and
defines the workflow and its first test. Known answers and test-surah material never enter a model input; prompt
examples never come from the test cases (S1, S29, S100, 18:83–99, 5:6, 4:34, the micro roots).

## 1. Why v13

Each version pulled the prose toward one dimension and lost another (v1–v12 review, 2026-09-27):

| version | gained | lost |
|---|---|---|
| v5 (Luna lanes → Sol/Astra consolidation) | dictionary breadth; most gold ingredients present | "refuses to assemble them"; catalogue feel; bulk re-reading (2 MB packets) made it expensive |
| V9 cold Opus (two keys, HFT articulated) | the latent images (29:38: eye film, kohl) | $6.9 agentic reading |
| V9 findings lane (Luna records → writers) | recall | accounting: "every record must reach the prose" → catalogue |
| w10 cold arm (5:6, 4:34; 68-line brief, context only) | local resonance within ayah and surah (mirfaq, kaʿb → Kaʿba "qiyāman" → "qawwāmīn") at $1.4–1.5 | rare senses beyond memory; unchecked lexical claims |
| v11 / v12 (ledger, QeQ first, chains judged per ayah) | QeQ, syntactic naẓm, Turkish loss (the user: "loved it") | the latent chains, audited away one word at a time; a surah pass with a reject list |
| gold (S1 bulgular, Fable) | graded surah channels, cross-definitions, sensory images | little QeQ or grammar |

The root cause is one prompt asked to hold two stances (generative latent discovery; evidence-bound QeQ), plus bulk
input that dilutes synthesis (4:34: cold Opus 8 anchors, with the dictionary 5, with the full package 5). v13
separates the stances into steps of a funnel whose outputs are compact and non-redundant.

## 2. Targets and the data that serves each

| target (NORTH_STAR) | data | notes |
|---|---|---|
| ground: plain sense | QAC words, anchor translation, the surah text | exact |
| what Turkish loses (lexical; grammar only when it matters) | focus word analysis (per word; per-lemma-and-form summaries when ready), the focus dictionary (the concept's breadth), QAC morphology | word notes today carry v5-era "topics": one test arm without them |
| local resonance (ayah, window, surah) | focus dictionary; the window scan (every branch of the other roots); pairs (script image partners per focus branch: same ayah / ±7 / surah) | the scan is complete; pairs only order candidates |
| image chains | channel reviews (110 surahs); HFT where it exists (90); the surah network (step N) | articulated, grounded, connected; never rediscovered |
| Quran-loaded words | exact concordance of the focus lemmas (every use with its clause), script | replaces the root dossiers for this target (their grouping never states the pattern) |
| QeQ (support / expand / shift / contradict) | the Quran (the model's knowledge plus the surah text), the V11 digest's related passages, then the reciprocal inter-ayah lists as a final missing-passage check | QeQ after the latent readings; never suppresses a surprise reading |
| checkability | Quran text, dictionary branch lines, verify scripts (`_commentary/v11/verify_src.py`, v12 checks) | every tag verified; a memory sense the dictionary lacks is marked |

## 3. The funnel

```
per window (fixed)       per ayah                       per surah               per ayah           per surah
0 script packet  ──▶  1 Opus activations  ──▶  N Opus network  ──▶  2 Opus QeQ  ──▶  3 Opus prose (TR)
                                                                                    S Opus surah prose (TR)
```

All model steps: Opus 5.5, effort high, no tools, one call, `claude -p` in tests, the Batch API in production. Each step
reads the previous step's records plus a small core, never the raw bulk again. Records are English (language-neutral);
only steps 3 and S are per language.

### Step 0 — packet (script, per window)
Fixed windows so that the ayat of a window share an identical prefix (cached): a short surah (≤ 40 ayat) is one
window; a long surah uses its pericopes (quran-data `surah_pericopes.jsonl`) widened by 7 ayat on each side, and an
ayah uses the window of its own pericope. Prompt layout: the shared window part first, the ayah part last.
- Shared (per window): the window's text; the scan: every branch of every root in the window, one line each (root,
  Bnnn, Turkish gloss, Arabic image; from v12 `inputs.branch_table`); the channel review's index and its sub-channels
  anchored in the window; the Fatiha.
- Per ayah: the ayah, its QAC words and word analysis; the focus dictionary in compact form (per branch: gloss, Arabic
  image, first classical phrase with its source: the quotable Arabic); pairs for each focus branch (V9
  `prepare.section_pairs`); the concordance of each focus lemma with at most 60 uses (every use: ref and the clause
  around the word; frequent lemmas: counts only); HFT records for the ayah where they exist.

### Step 1 — activations (Opus, per ayah)
Stance: discovery. No pruning, no verdicts, no confidence, no prose. Brief outline:
- any attested branch may be heard when activated by the ayah's words, the window's or the surah's words (the four
  trigger scopes; the QeQ scope is added in step 2); two keys: the branch and its activating word;
- keep partial and strange activations; combine fragments across roots and roles; let a completed image reread its
  parts (a well needs its rope and pulley);
- loaded words: from the concordance, the lemma's recurring role and the uses where the canonical reading departs
  from it;
- the channel review and HFT are strong input to articulate and extend;
- a sense from memory the dictionary does not attest is flagged `memory`.

Record (one per finding, compact):
`F<n> | kind: local|window|surah|chain|loaded|cross-definition | words: S:A:W … | branches: root Bnnn … | trigger:
S:A:W (scope) … | with: F<m> … | shows: what it makes perceptible in the plain reading (1–2 sentences) | anchor:
Arabic copied from the branch line or the Quran`

### Step N — surah network (Opus, per surah)
Input: every ayah's step-1 records (compact), the channel review, the surah text. Output: the surah's images, each
with its members (ayah, word, branch, role: source, conduit, guide, container, loss, reversal …), where images meet
and what the meeting shows, the movement they draw, and the step-1 findings each image absorbs. For a long surah:
the images of the whole surah, then their interactions (no per-passage commentary).

### Step 2 — QeQ (Opus, per ayah)
Input: the ayah's step-1 records, the network entries touching its words, the ayah core and the window text; the
reciprocal list only in a closing part of the brief ("after your own reasoning, check these for passages you missed").
Output, by finding id: supports | expands | shifts | contradicts, with passages and one sentence each; a contradiction
is explained, never used to drop a finding silently (the finding is marked); new QeQ findings on the ayah's main axes
(same record form, kind `qeq`), including branches activated by the words of those passages (the fourth scope).

### Step 3 — the ayah commentary (Opus, per ayah, per language)
Input: the step-1 and step-2 records, the network entries, the ayah core, the dictionary lines of the cited branches
(for tags). Stance: synthesis. The payoff test decides space (functional hierarchy); integration, not a catalogue;
progressive disclosure of the chains (what the reader has met in earlier ayat is built on, not repeated). Sections as
the prose needs: the plain sense and what Turkish loses; the local resonances; the chains through this ayah's words;
loaded words; QeQ woven where it works; contradictions stated. The v10 cold brief's writing rules carry over
(concrete detail makes the next detail necessary; no defensive disclaimers; show where an image comes from).

### Step S — the surah commentary (Opus, per surah, per language)
Input: the network, the step-2 results, the surah text. The images, each ayah explained within them, then their
interaction, the surah's movement and purpose, feet on the ground.

## 4. Checks and rules (carried from v12)
- Scripts check every record: ids exist, branch refs exist for that root, anchors occur verbatim in the branch line or
  the Quran; prose tags verified by source; one repair call at most; unverifiable tags reduced to plain text and counted.
- Estimate gate: a call starts only below $5; never stopped, never retried; an output that had a call is never
  called again; no hand fixes of inputs or outputs.

## 5. Economics (estimates; the test measures)

| step | input | output | claude -p (subscription-equivalent) | API batch |
|---|---|---|---|---|
| 1 activations | 120–280K (window part cached after the first ayah) | ~55K | $2.1–3.3; ~$1.3–1.6 cached | $0.80–1.10; ~$0.55–0.70 cached |
| 2 QeQ | 30–60K | ~25K | ~$0.6 | ~$0.35 |
| 3 prose | 20–40K | ~40K | ~$0.8 | ~$0.45 |
| N + S (shared) | | | | ~$0.1–0.2 per ayah |
| **per ayah** | | | **~$2.7–4.7** | **~$1.3–1.9** |

Batch caching is best effort. Thinking may grow with the larger step-1 input.

## 6. First test (needs the user's go)
- Ayat: 1:4, 1:5, 1:6, 1:7 (network over S1: step 1 on all seven ayat), 18:86 and 18:96 (loaded words: ḥamaʾ,
  nafakha), 5:6 (regression against the cold reading the user liked). 18:86, 18:96 and 5:6 use the channel review's
  window excerpt in place of a network.
- Reference arm: the existing w10 cold readings (`_commentary/v9/lines/work/S_A/synth/w10-opus-cold/`), no cost.
- Funnel arm cost (claude -p): step 1 × 10 ≈ $25, network S1 ≈ $2, steps 2–3 × 7 ≈ $10: about **$37**.
- Measured: cost per step, the S1 anchors and the micro-root known answers (never shown to the models), the user's
  blind read against the cold reading and v12.

## 7. What is reused, dropped, deferred
- Reused: v12 `inputs.py` (context, `section_dictionary`, `branch_table`, channels, HFT resolution, windows), V9
  `prepare.section_pairs`, v11/v12 verification and render, v12 `run.py` gates (estimate, lock, never twice, status).
- Dropped: root dossiers as a v13 input (loaded words come from the concordance; revisit only if step 1 misses ḥamaʾ
  and nafakha); Luna as a nominator; per-ayah chain verdicts; the reject list.
- Deferred: the per-lemma-and-form word-analysis summaries (use the current word notes until ready); the Batch API
  runner (built before production, possibly before the test); English and German; audio; the gloss product.

## 8. Changes after the Opus design review (2026-09-27, before the first run)
- Known-answer leak removed from the step-1 and network briefs (a well completed by its rope and pulley, the road's
  way-marks and traveller, the traveller kept alive by water: S1 gold chains); the v10 phrase "a well, a support …" in
  the prose brief made neutral.
- Step 1 (`prompts/act.md`): `image:` (the concrete picture) replaces `shows:` (no payoff test during discovery);
  kinds `fragment`, `loss`, `grammar` added; a `memory:` field; records limited to findings in which a focus word takes
  part (partners elsewhere by reference), so the ayat of a window do not each rediscover the surah's chains.
- Step N (`prompts/net.md`) gets the window scan and matures images (members added from the scan, marked `N-added`);
  every unabsorbed finding is listed (`unplaced`), and each image carries a disclosure plan (meet / develop / assemble)
  for the ayah commentaries.
- Step 2 (`prompts/qeq.md`) annotates findings, never whole images; "no open staging" is never a contradiction; it gets
  the V11 digest (variant readings, related passages) and the concordance besides the reciprocal list.
- Step 3 gets the focus dictionary (for what Turkish loses) besides the cited branch lines.
- Sizes: the focus dictionary is one line per branch with its definition (`branch_table`; the fuller
  `section_dictionary` is 3× larger); the scan is gloss and image only; pairs keep `root Bnnn ← where` (the scan has
  their glosses). 18:96's step-1 input fell from 594 KB to 350 KB (estimate $4.84).
- Caching: the first ayah of a window starts alone, the rest 60 s later (v12 missed the cache on 1:2 and 1:5).
- Records failing a check are flagged, never dropped.
- Not yet addressed: long surahs (a network per window plus a surah merge; step S per image section); per-stage anchor
  tracing (every step's output is kept, so a lost finding can be traced by reading); the 5:6 dilution arm (scan vs
  focus dictionary only) joins the later tests.
- Test order (user): steps 1–3 on 1:4–7 and 18:96 (step 1 also on 1:1–3 for the S1 network), then the user checks;
  later 18:86, 5:6, 4:34, 29:38, 29:41. Budget $30–50 (v12 ayat wrote 59–102K output tokens).

## 9. Production note: caching (measured 2026-09-27, first step-1 calls)
- `claude -p` caches only an identical whole message: the staggered start gave 0 cache reads (1:2, 1:5 read 0 after
  1:1 had started). The shared-prefix saving therefore needs the production path on the Messages / Batch API with an
  explicit `cache_control` breakpoint right after the shared part (brief + window.md), the ayah's files after it; the
  brief and window part must be byte-identical across the ayat of a window. In tests the stagger is useless (remove it
  or keep it harmless).
- Batch caching is best effort: submit the first ayah of each window (or a prefix-warming request) before the rest,
  and measure `cache_read_input_tokens` per call.
- Measured sizes: about 0.44 tokens per byte of packet (1:1: 60,035 tokens for 136,352 bytes); step-1 output 15–32K
  tokens at effort high (thinking 8–21K); step-1 cost $0.65–1.12 per ayah via `claude -p` without any cache hit.

## 10. Effort max, measured (18:96 step 1, 2026-09-27)
- The max arm spent its whole output on thinking: 256,000 output tokens, all thinking, no final message
  (`out-max/s018/18_96/act.raw.txt`); 42.9 min, 645K cache-write tokens (continued turns), **$10.28**, against $2.24
  for effort high (47.6K output, 33K thinking, 7.6 min). The estimate ($3.82) could not foresee it; started calls are
  never stopped (user rule). Not rerun. Effort high stays the setting; V9 saw the same on a large input.
