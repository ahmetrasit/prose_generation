# Adversarial review: why the v8 enrichment attempts failed (2026-10-08)

Scope: enrichment/v8 (q.py, sift.py, briefs), runs luna-test-95_1, root-filter-eval, sift-103_1, sift2-103_1,
sift2h-103_1, sift3-103_1; enrichment/v7/PLAN.md and v7 tier-2 outputs; the 103:1 r13 reading. No model was run.
Measurements were made with local Python over `RUN/index.sqlite` and `RUN/sift/out`. Scratch script:
`/private/tmp/claude-502/.../scratchpad/load.py`.

Tags: **[V]** = verified here by code, data or measurement. **[I]** = inference.

## Verdict

The failure is not a brief, model or claim-map problem. **v8 used a relevance filter for a job that needs
aggregation, on a scope that has no bound.**

- The 103:1 page retells six Qurʾān stories and cites 37 verses. Almost everything the tradition says about those
  verses is "relevant" under any honest definition. A filter therefore keeps most of it, whichever model runs it.
- What the writer needs is positions and their holders. Raw notes repeat each position 5 to 30 times.
- The project had already measured and built the right layer for this the day before: tier 2, distinct views with
  their holders, Sol high, reusable per verse. v8 went around it.
- The orchestrator's next proposal (Luna groups the core notes by position, per claim) is the configuration v7
  already tested and rejected: Luna over-merges when it consolidates.

The problem can be fixed within Opus 5.5, $7, no trimming and the writer deciding what to search. It needs one
scope rule stated by the user (§4).

## 1. Root causes, ranked by severity

### R1 (critical) Filtering cannot shrink this input, because the input is relevant but redundant
- **[V]** Five gates gave the same keep rate:
  - sift pass 1 kept 6,991 of 9,288 notes (75%);
  - pass 2 (Luna map + Luna grades) marked 4,861 cited-verse notes core;
  - pass 3 (Opus map + Luna grades) marked 4,739 core;
  - Haiku on 5 chunks gave near-identical grades;
  - the root filter kept 70%.

  Core + context in pass 2 (≈6,600) is about pass 1's keep count, so the grades only relabelled the same set.
  The number is a property of the material, not of any model or brief.
- **[V] Redundancy is large.** Examples:
  - Claim 8c (al-muʿṣirāt in 78:14): 143 core notes. They hold about 4 or 5 positions: clouds; winds; the heavens;
    "about to press, like a girl near menstruation"; *min* = *bi*. The same early authorities recur: Ibn ʿAbbās,
    Mujāhid, Qatāda, al-Farrāʾ, etc.
  - Claim 12a (who forgot in 12:42, and *biḍʿ*): 447 core notes. They hold about 2 positions on the pronoun
    (cupbearer, Joseph) and a handful of numbers for *biḍʿ*.
  - Claim 19b (the 309 years): 409 core notes. The one question the page actually commits to (the number as God's
    statement, or as the People of the Book's report, per Qatāda and the Ibn Masʿūd reading) has 2 positions and a
    few dozen notes. The rest is the qirāʾa of *miʾatin sinīna*, solar against lunar years, and why the sleepers
    guessed "a day".
- **[V]** The tier-2 test on 103:1's own notes already measured the compression: 393 rows became 102 views. On
  100:1, 308 rows became 85 views.
- **[I]** A filter can never remove redundancy, and a grade has no slot for "same as #37". Each of the three
  iterations changed the filter, not the operation, so the result could not change.

### R2 (critical) The scope has no bound: the page's points about cited verses are its own associations, and the tradition is silent on them
- **[V]** 103:1 is a lexical essay on the root ʿ-ṣ-r. Of its 37 cited verses, only 12:36, 12:49, 78:14 and 2:266
  contain the root. The page itself says so ("kelimenin kendisi geçmez", "Kur'an'ın kelimesi başaktır, asr değil").
- **[V]** In pass 3:
  - Core notes on the 32 cited verses without the root: 4,057 notes, 1.05M characters. That is 76% of all core
    characters.
  - Only 221 of those 4,057 notes (5%) mention the root, *afternoon*, *pressing* or 103 at all. Most of them are on
    11:114, 79:46 and 6:52 (the afternoon-prayer identifications).
  - The other 95% explain the cited verse's own story or wording: the Cave sleepers, the garden owners, Joseph's
    dreams, the spending parables.
- **[V]** The inversion: the page's most original claims are its dictionary senses from Lisān (5a, 9a, 14c, 17c,
  17e, 20b, 20c). They get **no** core note, because the lexicon and word stage is not in tier 1. Retelling claims
  get hundreds:
  - 21b (2:266 "read in the series on spending"): 686 core notes;
  - 13a ("one calendar" in the Joseph story, the page's own construction): 536.
- **[V]** The brief sets the bound open. `briefs/sift.md` makes core any note that "explains the cited verse on the
  very point the claim uses it for", or that "the writer needs in order to state such a position correctly", and it
  adds "when in doubt, choose core". The Opus claim map, though better, still contains retelling claims: 12a, 12c,
  16a, 16c, 19a, 19b. Under those rules the whole tafsir of the verse qualifies.
- **[V]** The requirement itself has flip-flopped:
  - 2026-10-07 (v7 PLAN, "decided workflow"): focus ayah only; cited verses get no digests and no blocks; "giving the
    writer the full tier-1 notes" is dropped.
  - 2026-10-08 (v8): per-cited-verse sift, with full tier-1 notes to the writer.

  Nobody wrote down what a cited-verse block is a complete map **of**. Without that, "complete" means a mini-tafsir
  of 37 verses.

### R3 (high) The unit is wrong for a "map"
- **[V]** A tier-1 row is one claim, from one source, at one locator. The same position travels through 10 to 25
  compilers (Ṭabarī → Thaʿlabī → Baghawī → Qurṭubī → Durr …) and through editions (MAWARDI and MAWARDI-FULL,
  BAGHAWI and BAGHAWI-FULL, three Wāḥidī works).
- **[I]** A map is questions × positions × holders. Handing the writer rows makes it do tier 2's job inside a
  context of about 400k tokens, on every page, and never reuse the result.

### R4 (high) Cost comes from context held across turns, and the sift design maximises it
- **[V]** Pass-3 core notes, rendered as the writer would read them, come to about 408k tokens (`sift.tokens`).
  Pass-2 core in full is 1.24M characters.
- Opus 5.5 rates: $4 per million input tokens, $20 per million output, $0.20 per million cache reads (cache writes
  assumed at 1.25 × input).
- **[I]** With about 450k tokens in context, cost before any search or writing:
  - cache reads over 30 turns ≈ $2.7;
  - writing the cache ≈ $2.3;
  - output ≈ $2–3.

  That is $7–8 at 30 turns and $10–17 at 50–80 turns. This matches the orchestrator's $13–17. The cap fails
  **because** the input was never compressed.

### R5 (high) Process: iterating on symptoms, measuring late, ignoring the project's own results
- **[V]** The root-filter report (same day, before the sift) already showed that any relevance gate on 103:1 keeps
  49–70% of cited-verse notes, and explained why: quoting a whole phrase pulls in the whole verse. It proposed menu
  pointers instead of a gate. Three sift passes were run anyway.
- **[V]** The blame moved from the brief, to Luna at the claim-map step, to "relevant but repetitive". It was not
  checked against the one number that settles it: how many notes the writer actually cites.
  - The 95:1 Opus-alone writer cited 161 notes for the whole page, about 7 per block (24 blocks).
  - A whole-page budget is therefore hundreds of notes, never thousands.
- **[V]** The new proposal ("Luna groups core notes by position per claim") repeats a configuration that v7 already
  rejected. On 2026-10-07, Luna as consolidator "over-merges (buried 26 distinct rows on 100:1)"; Sol high kept the
  distinct views. The proposal is also per page, so it is never reused, unlike per-verse tier 2.
- **[V]** The pilot choice biased the earlier test: 95:1 had only 44% tier-1 coverage of its cited verses, so the
  rejection of the Luna gatherer and the Opus-alone reference say little about pages with full coverage.

### R6 (medium) The user's per-reference idea was executed faithfully in form, but given the wrong output
- **[V]** Pass 1 matched the idea: one agent per cited verse, reading the whole page and then every note on that
  verse. That topology is sound for recall, and the grades were stable across models.
- **[I]** The distortion is in what the agent produced: a grade per note (filtering) instead of the positions on the
  page's questions about that verse (aggregation). Pass 2 moved further from the idea:
  - it put a page-wide claim map between the agent and the page;
  - it biased the agent toward core.

## 2. Evidence table [V]

| Measure | Value |
|---|---|
| Notes on cited verses / on 103:1 | ≈8,300 (2.35M chars) / 410 (105k chars): 22× the focus material |
| Kept: pass 1 / pass 2 core / pass 3 core / root filter B | 75% / 4,861 / 4,739 / 70% |
| Core chars on the 32 cited verses without the root | 1.05M of 1.38M (76%) |
| Of those core notes, any mention of the root, afternoon or pressing | 221 of 4,057 (5%) |
| Claims with no core note (pass 3) | 10, mostly the page's Lisān-sourced senses |
| 8c: core notes / distinct positions | 143 / ≈4–5 |
| 19b: core notes / positions on the page's actual point | 409 / 2 |
| Tier-2 compression (103:1 own notes, 100:1, 87:6) | 393→102, 308→85, 205→88 views |
| Notes cited by the 95:1 Opus-alone writer | 161 for 24 blocks |
| Pass-3 core in writer format | ≈408k tokens |

## 3. Is the $7 cap compatible with "no trimming" and a "complete map"?

- **Not** if a complete map means every position on every cited verse.
  - That is the tafsir of 37 verses. Even compressed to tier-2 views, it is ≈500k+ characters.
  - It contradicts the user's own ceiling of about 60 words per cited-verse block.
  - This reading of the constraints must give.
- **Yes** if:
  - completeness is required for the **questions the page commits to**;
  - each cited verse's full map lives one click away, on that verse's own tier-2 views or enrichment page. Every
    verse is eventually its own focus ayah, so nothing is lost; the details are only linked.

  This is the block principle as the user wrote it ("details one click away"). It is linking, not trimming.

## 4. The simplest design that would work

1. **Scope rule (the user decides once).**
   - A focus-ayah block maps every position on the question.
   - A cited-verse block maps only the reading the paragraph commits to: a sense, a referent, a reading, or "true
     length". It is ≤60 words, holders included, and links to that verse's views.
   - Where the page draws its own association (the Cave as ʿaṣr), the ledger says `no_match: the tradition does not
     make this link`. That is a finding, not a failure.
2. **Corpus layer, once per verse, reused by every page.** Retag + tier 2 by cell (verse word × type), Sol high, as
   already built in v7 (`retag.py`, `merge.py`). It is not Luna: Luna over-merges.
   - Check 1: every row is in a view.
   - Check 2: anchors are verbatim.
3. **Writer: one Opus 5.5 agent.**
   - Reads: the page; the focus ayah's tier-2 views (≈40k chars for 103:1); and a per-paragraph menu of cited-verse
     cells with counts (≈45–95k chars, per the root-filter estimate).
   - Pulls cell views, then tier-1 ids, as it decides (q.py extended to views).
   - Never receives raw notes in bulk.

### Cost estimate [I, grounded in the measurements above]

**Writer**

| Item | Estimate |
|---|---|
| Context held from the start | ≈40–55k tokens |
| Pulls over the run | ≈80–120k tokens |
| Turns | ≈40–60 |
| Cache reads | ≈5M tokens, ≈$1.0 |
| Cache writes | ≈$0.9 |
| Output including thinking | 80–150k tokens, $1.6–3.0 |
| **Total** | **≈$3.5–5 per page** |

Anchors for this estimate: the 95:1 Opus-alone writer was estimated at $2.18. The 1:1 page cost $12.5 in 88 turns
over 1.09M characters of raw corpus, which shows what raw context does to cost.

**Corpus layer** (API-equivalent; $0 actual on the subscription):
- ≈$0.25 per 300 rows;
- ≈$7–10 for 103:1's cited verses, built once and amortised across the Qurʾān (≈$0.37 per verse in the v7 plan).

**Unmeasured risk:** whether Opus pulls the right cells. Test it on 103:1 against the claims listed above, in
particular 8c, 12a, 19b and 11:114/6:52.

## 5. What not to do next

- Do not run a fourth page-level filter or grader, with any model.
- Do not use Luna to consolidate.
- Do not give the writer core notes in full.
- Do not test on a page without full tier-1 coverage of its cited verses.
