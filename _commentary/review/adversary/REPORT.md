# Adversarial audit of the 2026-09-28 review

Written 2026-09-28 by an independent auditor (an Opus subagent), using only reading and local counting scripts: no
model calls and no subagents. The harness kept it from writing files, so the main session saved this report
unchanged in substance. Paths are relative to `_commentary/` unless they start with `/`.

## Verdict

The review solved the wrong problem well. The user's problem is **synthesis**: one coherent, deep reading that holds
the discoveries together. The review treated it as **loss**: readings that "die between stages". It then optimized
retention and built instruments to measure retention.

Retention pressure is the mechanism the North Star already names as the cause of catalogue prose
(NORTH_STAR.md:134). The repo held the counter-evidence from the start: the praised 29:38 pilot, the cold arms, and
the quran-roots lesson "synthesize free, anchor afterward". The review quoted that evidence (PHASE1_REPORT.md:640–643)
and then built the opposite.

## 1. Root causes, ranked

### 1. Misframing: recall and plumbing instead of synthesis

- The review's thesis: "finding readings is not the bottleneck; losing them afterwards is" (EXECUTIVE_SUMMARY.md).
- The North Star's demand: "Integration, not aggregation… finding the concept is the finding" (NORTH_STAR.md:93) and
  "never catalogued" (:71).
- Every remedy adds retention pressure:
  - E2: "never drop a reading", "keeps its place", "Keep each reading's evidence" (e2_integrate.md:11–19);
  - E0: never withhold;
  - the trace: branch ids carried.
- The user asked why the pulley was missing. The answer was another branch-id table (discovery/TRACE_TABLES.md).

### 2. Metrics that reward the failure

- **E2 recall** is the share of the inputs' own references and Arabic quotations that reappear (e2_score.py:5–9). It
  measures copying.
- **Measured:**
  - 58% (1:6), 64% (4:34) and 58% (18:86) of integrated sentences are near-verbatim (≥ 0.8) copies of input
    sentences;
  - integration thinking was 2.3–6.2k tokens, against 45k for the 4:34 cold arm.
- **The return turn** cost $3.85 of E2's $8.38 and changed nothing in 6 of 6 cases.
- **The Phase 1 scorecard** rates almost every version "P" on never-catalogued, and v13–v14 "S" on three criteria,
  although v13 out-v2 1:6 (7,451 words, one scene per paragraph) is the clearest catalogue in the repo.
- **No instrument measures coherence.** Surface counts don't either: the pilot has 43 Arabic tags per 1,000 words,
  against 31 in E2 4:34. So far only the user's read has been a valid judge.

### 3. The repo's positive evidence was set aside

- **The pilot: "great / excellent"** (v9/DESIGN.md:118). E4 was called "cannot be reproduced faithfully"
  (EXPERIMENTS.md:173) and never approximated, although its shape is codified in v9/prompts/writer_rules.md.
- **The quran-roots LESSONS** (/Volumes/OZTURK/_projects/quran-roots/_corpus/activation/LESSONS.md):
  - lines 23–31: schema-first pipelines suppress discovery; generation and compliance share one budget; free dialogue
    about 10/10 against 2–4/10;
  - lines 48–52: the concrete/rural class is the pipelines' blind spot, which is exactly the pulley and the gait.
- **The North Star lesson** that the cold brief and the 4:34 cold arm "produced the latent readings the later
  auditing briefs lost" (NORTH_STAR.md:138). The review demoted it by recounting anchors (PHASE1_REPORT.md:353–380).
- **The review's own inference:** "A small, targeted supply beats both" (PHASE1_REPORT.md:435). E0 then built
  39k–708k-token pages.

### 4. The material that holds the user's items was kept out of every model run

- **The user's standing rule:** HFT and the channel reviews hold the chains; never rediscover them.
- **Neither E1 nor E2 received them.** E1 is the v9 dict arm plus permission; E2 merges two readings and has no
  dictionary.
- **1:6:**
  - The supported gait (ه د ي B008) is an HFT hypothesis ("base_embodied_supported_motion",
    v9/input/v2/s001/1_6/02_hft.md:16–22).
  - The pulley (ق و م B012) is in the S1 review's "Well and Water-Lifting Assembly" subchannel.
  - v13 act.md F15 and F16 had assembled both.
  - The E2 1:6 integration prompt contains 0 occurrences of البكرة, القامة or التهادي.
- **Chain data was treated as contamination:**
  - B2 "answer-fed" probes;
  - lint work;
  - "Do not flatten a well, a support…" deleted from the brief as an S1 leak (PHASE1_REPORT.md:178).

  Benchmark hygiene was put above the product.

### 5. Accounting rules inside the writing brief

**Rules added during synthesis:**

- per-use echo clauses;
- tags and sources on every quotation;
- [bellek] marks;
- keep evidence;
- never drop.

**What the output shows:**

- the hedges "burada ancak yankı olarak duyulur" (1_6_B.tr.md:45), "yalnızca aileden gelen bir yankıdır" (:51) and
  "Hediye ayetteki fiilin anlamı değildir" (:73);
- 4:34 B turned the cold arm's argument into bulleted dictionary quotations (lines 13–14, 56–58; 28 bullets
  against 0).

**The user's rulings are fair,** including "an echo enters the prose only with a warrant… otherwise it stays in the
record". They are selection rules, satisfiable by one confident containment sentence per image, as the pilot does:
"Burada yol yol, alıkoymak alıkoymaktır… Onları uyandıran da âyetin kendisidir."

**Also removed.** E2 deleted write_v10.md:20, "The aim is main themes and important image chains, not every possible
finding" (confirmed by a sentence diff).

### 6. Instruments before product

- About 28k lines of Python (e0 14.6k; phase1/2 13.2k) and 169 MB in e0/. No page was read by a model.
- E0 was built while the E2 blind read was pending (commit order: E1/E2 at 19:30, E0 at 21:57).
- The measured cache-write rate is $8.0/M (dict arm log: $0.643 = 22,591 output tokens at $20/M + 23,793
  cache-write tokens at $8/M). At that rate, input alone costs:
  - 4:34 page, 336k tokens: about $2.69;
  - 5:6, 460k: about $3.68;
  - 18:86, 198k: about $1.58.

### 7. Misreading intent, and overclaiming

- **Misreading intent:**
  - The user said "not a dictionary explainer". E0 is a script-built one: every branch, scope notes, 53–655
    "definitional pointers" per ayah.
  - The user was asked to rule on instrument parameters.
- **Overclaims:**
  - "It genuinely integrates" (EXPERIMENTS.md:88). Its one new tension resolution reuses the dict arm's own ʿAyn
    quote.
  - "Integration… works mechanically" (:103).
  - "Close to final" for an architecture of which only E1/E2 ever ran.
  - The 4:34 blind pair was chosen by recall 0.71 against 0.70, leaving out the cold arm, the recorded best.

### 8. Process waste

- About 25 subagents and 700- and 400-line reports.
- E1 ($9.65) answered a question about citation counts nobody asked.
- Half of E1/E2 spend went to duplicate replicates. Phase 2 also planned "≥3 of 4" replicates and a handover
  "replicated 4×". This conflicts with the no-duplicates rule; I could not establish whether the rule predates
  E1/E2.

## 2. The reviewer's claims

| # | claim | verdict |
|---|---|---|
| 1 | Discovery is not the bottleneck; readings die between stages | **Half true as fact, wrong as diagnosis.** The coalitions exist upstream. But "32/32 activated" means the act stage enumerated every branch, which is not discovery. Readings die at synthesis: a writer given atomized material lists it (v13 out-v2) or drops the concrete class (dict arm, E1, E2). The cure is an integrating mind with assembled images and a leftover valve. Discovery is untested where no HFT exists (24 surahs, S4 included). |
| 2 | Scripts annotate, never order or withhold; rich supply | **First half right, second half wrong.** "Never withhold from the writer" produced noise above budget. The North Star asks for a funnel (NORTH_STAR.md:120–125). Completeness belongs in a record after the prose (pilot harvest, v15 record). |
| 3 | E2 integration works | **Wrong.** The metric measures retention, the output is mostly splicing with shallow thinking, and the inputs lacked the user's items. The user preferred the input on 4:34. On 1:6 the integration helped a short ayah but is far from the North Star. |
| 4 | Brief rules | **Mostly harmful as writing rules.** Containment and memory permission hold. Echo and usage-role rules become selection plus one sentence per image. Sourcing, memory checks and construction flags go after writing (check.py; v15 attached sources by script). |
| 5 | Architecture "close to final" | **Unsupported.** Only E1/E2 ran. S0 was never read by a model, and S1 and S5 never ran. S0 breaks the budget on long ayat. What holds: memory permission (E1) and checks after writing. |

## 3. E0 verdict

**Harmful as writer input:**

- **Size:** 39k–708k tokens.
- **Atomized** rather than assembled.
- **Noisy.** In e0/supply/out/1_6.md:
  - the pulley branch points to «للبكره» → ب ك ر (morning, virgin) and «والخوان» → خ و ن (betrayal) (lines
    119–120);
  - function words link to 1:7's غير (lines 83, 99, 124);
  - "cancer" → 79:10.
  - Only 16 of 53 pointers land in the ayah or window; 4:34 has 655.
- **Hedging primed:** scope notes like "tartışmalı yorum genelleştirilmez" (line 452).
- **The well chain is buried** at line ~449 among 40 subchannels.

**Keep, after writing only:**

- `check.py`;
- `textclean.py`;
- the Majāz mapping;
- `branch_kind` audit lists;
- the roughly 16 within-surah cross-definitions (ع ل م B002 "…ويهدي إليه" → 1:6; م ل ك B008 lead animal → هادي).

**Shelve:** the validator, the guard and the scorecard.

## 4. What produced the best prose

**The 29:38 pilot:**

1. Sections are images that cross words (the eye section joins sabīl, ṣadda, tabayyana and mustabṣirīn).
2. One controlling question opens and closes the reading (47:14).
3. The Quran supplies stages of the argument (43:36–37; 46:24–26).
4. Containment is stated once per image.
5. Leftovers have a valve: Ek Notlar plus a harvest written after the prose.
6. Discovery arrived assembled: HFT's "outlier_webbed_path… became the core of the eye section" (harvest.md:24).
7. One mind built and read the package in session. Whether the user steered it is unknown.

**The v9 cold 4:34 arm:**

- one vertical axis: ʿalā → nushūz as rising → ʿalayhinna → ʿAliyy;
- kavvām and nāshiz both upright, told apart by purpose;
- ṣ-l-ḥ returns;
- 0.9 dictionary mentions per 1,000 words;
- 45k thinking tokens.

**v15 out-nocap 4:34:**

- Turkish loss woven in;
- the fortress image (muḥṣanāt → ḥāfiẓāt li-l-ghayb);
- sources attached afterwards by script.

**What pushes toward catalogue:**

- must-land lists and coverage blocks (v13/prompts/write.md:59–71, 121–122);
- per-word quotas: "900–1,200 words per focus word" (:73–74), which produces word walks;
- in-writing source fields;
- atomized inputs;
- keep and never-drop rules;
- low-thinking merges.

**What allows synthesis:**

- "most candidates … stay out" (writer_rules.md:12);
- "a thread with a thesis" (:36);
- an Ek Notlar or record valve (:41; v15 opus_write);
- memory permission;
- assembled inputs;
- accounting after writing.

## 5. On OWN_REVIEW.md

**Right on:**

- the anti-pattern it optimized;
- accounting rules in the brief;
- the dismissed dilution lesson;
- instruments first.

**Wrong on three points:**

- It quotes pilot/29_38-v2/notes.md (a cold subagent run, $6.9, never rated by the user) as the pilot's notes. The
  praised pilot/29_38/ has no notes file.
- It proposes agentic sessions at $2–5 per ayah, over budget.
- Its 29:38 package is answer-fed via HFT, so it is usable as a prose reference only.

## 6. Recommended next step

Change one thing from what the user already calls coherent: add the assembled findings, and give leftovers a valve.

**Ayat.** 1:6 and 4:34. One run each, no duplicates, after approval.

**Input:**

- the exact E1 prompt (context, focus dictionary, write_v10 plus permission);
- the ayah's HFT records verbatim (1:6: v9/input/v2/s001/1_6/02_hft.md, about 9k tokens; S4 has none);
- the channel-review subchannels anchored in the ayah, verbatim from quran-data network-v3/sNNN/review/reader_a_pilot.md
  (1:6: about 12k tokens; 4:34: at most about 15k), with no scope notes and no typed links.

**Brief: three additions, all from writer_rules.md:**

1. Most candidates stay out; no paragraph per item; no word-by-word walk.
2. Themed sections, each a thread with a thesis that crosses words. A supplied chain running through this ayah is
   heard as one image.
3. `## Ek Notlar`: one sentence per real finding that fits no thread.

Check afterwards with check.py.

**Cost.** About $0.7–0.8 (1:6) and about $1.7 (4:34).

**Decision.** The user reads against E2-B (1:6) and the remembered 4:34.

- If the pulley or the supported gait is still missing from the threads, add a same-session fixed challenge turn
  ("is this everything, or did you curate?").
- If the chains still don't cross ayat, try a surah-first pass on S1.

**Confidence:**

- about 60% at least as coherent as the dict arm;
- about 35–45% that it also weaves in the pulley and the gait acceptably.

**Risks:**

- 37 of 44 S1 subchannels mention 1:6, so the slice may read as a checklist;
- the rural blind spot may persist in a single call.

## 7. Stop doing

- Retention, branch-id and anchor metrics, and trace tables as answers to "why".
- E0 pages as writer input; the four-arm input-format test; the validator, guard and contamination work.
- Merging finished readings for long ayat.
- Per-use accounting clauses in briefs.
- Replicates.
- Agent fleets and long reports before the user has seen new prose.
- Asking the user to rule on instrument parameters.

## Uncertainties

- Which 4:34 the user remembers (v9 cold or v15 out-nocap are the likely ones).
- Whether "a cold instance given only the dictionary" means the v9 dict arm, E1, or a test of the user's own.
- Whether the pilot was user-steered.
- Whether the no-duplicates rule predates E1/E2.
