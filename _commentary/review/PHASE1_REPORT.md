# Phase 1 report: what v3–v15, the quran-slm distance and the sister repos show

Written 2026-09-28. Read `EXECUTIVE_SUMMARY.md` first for the short version.

This report answers the user's questions of 2026-09-28 with evidence only; designs are Phase 2's job:

- **Q1.** Is what we have the most we can do, or are there significant opportunities not yet harvested?
- **Q2.** Is "training data" enough? (a) Where does the model's own knowledge already suffice, so data need not be
  pushed? (b) Are there enough labelled examples to train or tune a retriever or distance model?
- **Q3.** Could a step built on top of v5 (Luna-generated) with more data processing work?
- **Q4.** What significantly different, non-iterative method is possible?
- **Q5.** What distance measure in quran-slm would serve script-based discovery before synthesis?

## 0. How this was done

- **Eleven read-only agents** (Opus, Claude Code), each told to read `NORTH_STAR.md` first and to score its scope on
  the same thirteen North Star criteria (NS1–NS13, §1):
  - eight version readers: v3+v4, v5+v8, v6+v7 with the side products, v9, v10, v11+v12, v13+v14, v15;
  - one agent on the quran-slm distance;
  - one agent sweeping the sister repos;
  - one agent collecting dilution metrics (numbers only).

  None of them started a model run or edited a file. Their full reports are in `review/phase1/agents/*.json`, and
  the scripts behind their numbers are in `review/phase1/scripts/`.
- **My own reading.** I compared prose myself, with no comparison agents, as the "compare myself" rule asks:
  1:6 in v5, the context-only arm, the dictionary arm and v15; 18:96 and 18:86 across arms; 29:38 across every
  version that ran it. I also re-checked the claims this report leans on most:
  - the cold arm's evidence clause;
  - the "no value" labels on 18:86;
  - Lisan's eye-film entry;
  - v5's 2,844 discovery files;
  - the quran-roots lessons.
- **Evidence standard.** Numbers come from ledgers, run logs, status files or the agents' counting scripts. "Recorded"
  means written in a repo file. "Inference" means a conclusion drawn from records. Every verdict about quality is
  either quoted from a file or marked as mine. No reader outside the project has judged any output.
- **Test cases.** The named cases (Fatiha, 4:34, 5:6, 18:86, 18:96, 29:38, S100, S103) are used here only as
  evaluation targets. Nothing in this review should enter a pipeline prompt.

## 1. The yardstick

| id | North Star criterion (short) |
|---|---|
| NS1 | ground: the plain sense, never disorienting |
| NS2 | what Turkish loses; grammar only when it matters to a reading |
| NS3 | local resonance within the ayah, its window and surah |
| NS4 | surah image chains, disclosed progressively; existing chains extended, never rediscovered |
| NS5 | Quran-loaded words and where the canonical translation departs |
| NS6 | the Quran explaining it (QeQ), after the latent readings, never suppressing a surprise |
| NS7 | supported non-canonical readings, explained and connected, never catalogued; a root's branches as one concept |
| NS8 | no premature pruning: activation → coalition → maturation → reinforcement → reread → prose |
| NS9 | containment: readings coexist; never "not X but Y" |
| NS10 | checkable: dictionary branch plus trigger; every Arabic quotation sourced; memory marked |
| NS11 | no invention; nothing lost silently |
| NS12 | surah commentary: images, their interactions, convergence on purpose |
| NS13 | economics: ~$1/ayah production aim, $5 test ceiling; bulk input dilutes synthesis |

The two user cases added during this review are tracked throughout:

- **29:38 as-sabīl** (a neighbour-activated rare branch). The eye-film branch of س ب ل is reached through zayyana
  and mustabṣirīn.
- **ḥamaʾ and nafakha** (Quran-loaded words against the literal canonical reading). They cover 18:86 and 18:96.

## 2. The versions, one by one

Costs are Opus list-price equivalents through `claude -p`, unless marked Luna, Sol or Astra.

### v3–v4 (2026-08-28 to 09-03): Luna lanes plus accounting

- **What they were.**
  - v3: three Luna-max scope reviewers (micro, macro, global) → a reconciler → a merge writer → an editorial pass.
    Lane packets were 0.75–2.4 MB, backed by about 33k lines of Python.
  - v4: the same without the state machine, adding immutable per-finding sentences and provenance ledgers.
- **Added:**
  - an explicit two-key contract (branch facet plus an independent trigger), later adopted by the North Star;
  - an exhaustive branch review, so rare senses were at least considered. The 29:38 eye film reached v3's prose
    explicitly.
- **Lost:**
  - v3's S1 run finished 0 of 7 ayat: 99 repair turns, 37 of them caused by the repair itself rewriting content.
  - v4's hardening tripled the prose (1,361 → 5,008 words for 29:38) and inflated the apparatus about 150-fold
    (2 MB index against a 45 KB prose).
  - v4 had zero discoveries beyond the docket at 29:38, against 954 facet decisions.
  - The merge writer was forbidden to combine findings.
  - Provenance labels (`legacy_unbound`) were used as filters.
  - Worked Fatiha answers (CHANNELS.md) sat in every prompt.
- **Lesson.** Conservation machinery bought traceability, not understanding. "Every record lands in the prose"
  produces a catalogue.

### v5 and v8 (09-03 to 09-23): the Luna harvest

- **What it was.**
  - Three Luna-max lanes with discovery JSON plus lane prose → a Sol-max consolidator and editorial (S1 on Astra) →
    a Luna middle layer → a Luna invitation.
  - About 2.2 MB of prompts per ayah.
  - v8 moved discovery to the Batch API on paper; it was never run.
- **Scale, the first version to finish whole surahs:**
  - 909 numbered ayat plus 33 basmalas, in S1, 5, 12, 17, 18, 19, 31, 32 and 87–114 (14.6% of the Quran);
  - 2,844 discovery JSON files, all valid;
  - 64,063 findings, 96,140 anchored branch activations and 84,062 candidate decisions with reasons;
  - 942 editorials, all passing the validator.
- **Cost.** About $0.6–0.7 per ayah at Luna/Sol rates (S12). S1 on Astra was an estimated $27–49 per ayah.
- **Recorded verdicts:**
  - v11 REVIEW: v5 "contains the ingredients of nearly all 26 [S1 gold items]. It then refuses to assemble them."
  - v13 DESIGN: "most gold ingredients present"; "catalogue feel".
  - Astra comparison: "Luna is already supplying valuable discoveries… an expensive editor… cannot legitimately
    recover rejected findings."
- **Failure points:**
  - a registry label (`unresolved`) was read as disqualifying; one instruction fixed about 90% of that gap;
  - lanes were misrouted;
  - the consolidator saw only prose, so the eye film survived without its lexical chain;
  - the 29:38 global lane used 0 of 253 inter-ayah rows, and Luna/Sol editorials cite a median 3.7% of the pushed
    rows;
  - the landing ledger produced accounting prose (100:1 macro scope: 31,163 words).
- **My reading of 1:6 (middle layer, 4,861 words).** It holds nearly every North Star image:
  - way-marks, the road's middle and the lead animal;
  - the road that swallows its traveller;
  - the stray animal;
  - water, the well and the crossbeam.

  But it reads as a defensive catalogue: almost every paragraph ends in a disclaimer ("… anlamına gelmez").

### v6–v7 and the side products (09-05 to 09-07; July to September)

- **v6:** lossless paging of 2 MB packets. Every page reached the agent, and it still did not read them: "helper
  delivery counters… indicated full inspection" while material was omitted. Restoring v5's semantics turned 9 of 15
  findings into placeholders.
- **v7:**
  - Pilot 1, with specific fields and an explicit "look for uncandidate readings", found 5 independent Quran parallels.
  - Pilot 2, with one free-text field and 1.1 MB handoffs, lost all of them and introduced a verse misattribution.
- **Surah products:**
  - 57 legacy channel-first surah readings: 2,511 hypotheses and 391 channel briefs, from lean 36 KB cards;
  - 36 editorial-v1 surah readings built only from v5 editorials;
  - S1/S87 channel drafts.

  No semantic verdict is recorded on any of them.
- **Never run:** the progressive-disclosure design (Layer 2.5: latent → emerging → mature → complete per ayah),
  which the user's own 1:6/1:7 example describes.
- **Translation v1.** Pushed gloss error profiles moved the Turkish off the memorized canonical. No rendering was
  accepted.

### v9 (09-24 to 09-26): seven architectures in 36 hours, and the controlled arms

- **Lanes:**
  - pilot Opus reader (user: "great / excellent");
  - agentic cold Opus on a 600 KB package ($6.9);
  - Luna findings lane (29:38: 397 items, 627 records, ≈$0.87 Luna);
  - a script typed network that recovered 17 of 19 cold-Opus links on 29:38 in 13 s;
  - a bounded Luna meaning pass (≈$0.10);
  - Sol lanes;
  - "V9 lines".
- **The controlled arms.** 56 one-call arms over 17 ayat, all using the same 68-line brief (v10's `write.md`):
  - cold (context only);
  - dict;
  - dhft;
  - dslim;
  - ledger;
  - full package;
  - Sol and Luna writers.

  They are the basis of the "dilution" lesson (§4.3).
- **Recorded:**
  - cold Opus > Sol > Luna writer;
  - the findings lane turned the writer into an accountant (9,289 words, 262 of 274 readings used, paragraphs in
    harvest order);
  - Sol and Luna writers rejected kohl and the night path "on literal grounds";
  - notes printed without their source phrase never reached a writer.
- **29:38.** The dictionary-fed runs found the eye film, and the best tied it two ways:
  - to the spider-house parable of 29:41, because the dictionary's own definition compares the film to spider weaving;
  - to kohl, through zayyana.

### v10 (09-25): one evening, and a lasting brief

- **The pipeline.** A Luna curator followed by a writer. No prose came out of it.
- **The curator's one run:**
  - it reorganized HFT without extending it;
  - it used 0 of 338 retrieval-only candidates;
  - it repeated an upstream "no value" verdict on 15:26/28/33 for 18:86.
- **What lasted.** Its 68-line writer brief became the cold arm.
- **Known answers leaked into the brief.** "Do not flatten a well, a support…" is the S1 answer.

### v11–v12 (09-26): one Opus call per ayah, then auditing

- **v11:**
  - one Opus call per ayah on context + dictionary + a script digest, returning a ledger and then the reading;
  - about $1.1–1.9 per ayah;
  - recorded as "the best prose and the best Quran-explains-Quran engine the project has produced", and "structurally
    unable" to form cross-ayah coalitions (9 of 26 gold items missed; 7 of those 9 are architecture).
- **v11 arm S, the surah seed pass.** One coalition-first call, $1.64 for S1, assembled the herd, the waymarks and
  trodden road, the rain, and soft-against-hard. It was dropped under the "never rediscover" rule, although its
  value was assembly, staging and limits. The seed writers were never run.
- **v12:**
  - added HFT, channels, neighbours and root dossiers to every ayah call (127–232 KB);
  - asked the writer for per-ayah chain verdicts;
  - cost about $2.99 per ayah.
- **What v12 lost.** It rejected the water-secured encampment, the well-and-lifting assembly and the lead animal
  ("1:4'te tutmaz", "No Quranic scene"). The inputs held the chains; the stance threw them out.
- **What v12 gained:**
  - full source checking (0 missing, 0 unsourced);
  - Turkish loss as a family (27 mentions vs 3);
  - the Usage and Limits families;
  - a 5,125-word surah commentary.

### v13–v14 (09-27): stance separation, then the handover wall

- **v13:**
  - generative step 1 (act) → the surah network → QeQ → write;
  - step 1 "found nearly every gold and anchor item": the road, herd, water system with the well-frame (ق و م B012),
    womb, and cross-definitions;
  - it found nafakha as a loaded word unaided, from concordance counts (20 uses: 12 horn, 5 breath into a formed
    body, 2 ʿĪsā, 1 craft);
  - $3.7–6.8 per ayah; xhigh 1:5 cost $14; effort max failed twice.
- **Every handover contract traded recall against form (§4.2).**
- **v14:**
  - Sol and Astra writers on v13's frozen upstream;
  - Astra retained more than Sol;
  - blind 29:38 with Astra carried the tent seam → eye film → spider-house reading.
- **The composition trial failed.** Sol selecting, then Astra writing, gave the clearest prose (1,221 words), but
  Sol's selection kept 19 of 169 records and dropped the eye film. The writer had "no cue that the relationship was
  there".
- **No Opus control was run,** so Opus against Astra is untested on matched inputs.

### v15 (09-27 to 09-28): from scratch

- **Stages.** Window reading → ayah reading → Luna evidence → write → checks → surah step.
- **Luna data:**
  - a scene index for the whole Quran (193 jobs);
  - loanword cards for 74 lemmas;
  - use profiles for 39 of 295 lemmas.
- **Uncapped runs:**
  - 4:34: 1,893 words;
  - 5:6: 1,658 words;
  - every quotation sourced;
  - the 5:6 North Star example made (mirfaq leaning, kaʿb → Kaʿba, qumtum → qawwāmīn);
  - about $2.3–2.5 per ayah.
- **Against the cold arm.** Roughly its depth, with fewer same-surah parallels: 4:34 14 against 28–32; 5:6 6 against
  17.
- **What the agent verified:**
  - most cited passages come from the ayah reading (15–16 of 18–22);
  - the evidence step adds 2–4 passages and one quotable classical phrase;
  - the writer adds nothing new;
  - 5:91 and 35:10 were in the reading packet and never used;
  - the Fatiha well was set aside at the window step, and its fragments stayed scattered over five ayah records that
    nothing reassembles;
  - 48% of Opus spend is 1-hour cache writes at 2× on prompts used once.
- **Data defects:**
  - 11 roots with ambiguous "root Bnnn" keys, including ق ر ء;
  - 704 ad-hoc scene ids, 587 of them used once;
  - scene roles that mirror the North Star examples.

### Scorecard (each agent's own ratings; S strong, P partial, W weak, – absent, ? not evidenced)

| version | NS1 | NS2 | NS3 | NS4 | NS5 | NS6 | NS7 | NS8 | NS9 | NS10 | NS11 | NS12 | NS13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v3–v4 | P | W | P | W | – | P | W | W | P | P | P | – | W |
| v5–v8 | P | W | P | P | W | P | P | W | P | P | P | W | P |
| v6–v7 + side | P | W | P | P | W | P | P | W | P | P | W | P | W |
| v9 | P | W | S | W | P | P | P | P | P | P | P | – | P |
| v10 | P | – | S | P | P | P | P | P | P | P | P | – | W |
| v11–v12 | S | P | P | W | P | P | P | W | P | S | P | P | P |
| v13–v14 | S | S | S | P | P | P | P | P | P | S | P | – | W |
| v15 | S | S | P | P | P | P | P | P | S | S | P | P | P |

Different agents rated different versions, so compare columns loosely. What the grid does show:

- NS7, NS8 and NS12 never rise above partial.
- NS13 is weak wherever the Opus funnel grew.
- No version is strong on NS4, NS5 or NS6.

## 3. My side-by-side reading

### 1:6 in four configurations

| run | words | what it has | what it lacks |
|---|---|---|---|
| v5 middle (Luna) | 4,861 | nearly every image: waymarks, road's middle, lead animal, swallowing road, stray, water/well/crossbeam | integration; each paragraph fenced by disclaimers |
| cold arm (context only, $0.35) | 1,421 | the strongest Quran web: 37:118, 48:2, 6:153 (one road vs sübül), 18:1–2, 11:112, 41:30, 7:16–17 (Iblīs sitting on the road), 36:61 and 3:51 read back into 1:5; famous lexical images (swallowing, hādī, hadiyya → 1:7) | no surah chain needing rare senses (waymarks, trodden road, well) |
| dictionary arm ($0.64) | 1,643 | deepest lexicon: the staff that goes ahead, water that "stands" (freezes), the full-weight dinar, qawma in prayer, hedy as someone's gait → 1:7 | outside-surah Quran reach (brief said "only the supplied evidence") |
| v15 ($1.00) | 767 | the chain (naʿbudu's trodden road), yuhādā beyna-thnayn → nastaʿīn, the Turkish-loss layer (hidayet/hediye, istikamet, kıyam/kıyamet/kıymet) | the thinnest Quran web |

Each configuration returns a different, largely separate slice of what the North Star asks for. Together they cover
nearly all of it. That is a finding about method, not a verdict on one version (§6, item 4).

### The watch cases

- **29:38 (sabal, the eye film).**
  - Found by every dictionary-fed run: v3 legacy, the v9 pilot, Sol and the lines arms, the v14 Astra blind run.
  - The best runs tie it to 29:41's spider house and to kohl.
  - No context-only run exists for 29:38, so whether pretraining alone reaches it is untested.
  - Lisan has the sense ("السبل داء في العين شبه غشاوة كأنها نسج العنكبوت بعروق حمر", after al-Jawharī).
  - Mechanism: every branch of every root in the ayah must be visible, and one reader must see the neighbours'
    senses (seeing, adorning) together with the rare branch.
- **18:86 (ḥamaʾ).**
  - Every Opus run, including the cold arm, cites 15:26, 15:28 and 15:33.
  - **Correction (Phase 2, verified).** The shared v10/v11 writer brief's citation-format example is literally
    "e.g. (15:26, 15:28, 15:33)" (write_v10.md:59, write_v11.md:112). The recall is therefore contaminated and says
    nothing about memory.
  - The difference is framing. The cold arm calls it "a root similarity, not an equation". The full-package arm
    comes closest to the user's reading: Iblīs refuses "looking at exactly this material" (15:33), 18:50 retells
    the moment, and vecede makes Dhū l-Qarnayn the observer.
  - No run states the full reading.
  - The canonical-relevance labels actively suppress it. The inter-ayah reviewer marked 15:26, 15:28 and 15:33
    "no value" for 18:86 ("belongs to the creation account and does not clarify the observed western setting").
- **18:96 (nafakha).**
  - 15:29, 38:72 and 32:9 (animating) appear only in the full-package arm and in v13, where the concordance counts
    were pushed.
  - The cold arm reaches 3:49 and 18:99 only.

## 4. Cross-cutting findings

### 4.1 Discovery is not the bottleneck; readings die after they are found

| where a reading died | version | evidence |
|---|---|---|
| provenance or registry label used as a filter | v3, v5, v6 | `legacy_unbound` excluded; "registry=unresolved" disqualified 9 of 12 Failed Stability branches until one instruction fixed it |
| worklist crowds out discovery | v4, v7 p2 | 0 discoveries against 954 facet decisions (29:38) |
| pushed bulk ignored | v5, v7, v10 | 0 of 253 rows; 0 of a 542 KB connection registry; 0 of 338 candidates |
| writer re-judges and rejects | v9 (Sol, Luna) | kohl and the night path rejected "on literal grounds" |
| merge drops thin items | v9 | notes printed without the source phrase never reached writers |
| upstream verdict echoed | v10 | "no value" on the ḥamaʾ passages repeated |
| architecture cannot see the partner | v11 | 7 of 9 S1 misses: the member branch belongs to another ayah's root |
| chain judged from one member; grounding as filter | v12 | water, well and lead animal rejected "1:4'te tutmaz", "No Quranic scene" |
| records → prose handover | v13, v14 | first run dropped items; v2 catalogue; v3 lost 8 anchors on 1:6; composition dropped the eye film |
| early set-aside, no reassembly | v15 | the Fatiha well set aside at the window; fragments scattered over 5 records |

On the other side, discovery kept succeeding:

- v5's Luna lanes held the ingredients of nearly all 26 S1 gold items;
- v13 step 1 found nearly every anchor;
- v9 Luna found kohl, the eye film and the worn road;
- the v11 seed pass assembled the S1 systems in one call.

**Inference.** The unharvested value is not in more discovery. It is in (a) not killing readings between stages and
(b) a synthesis that can select without losing supported surprises.

### 4.2 The handover wall

v13 and v14 tried every kind of records-to-prose contract on the same upstream (1:5 and 1:6):

| contract | recall | form | recorded |
|---|---|---|---|
| no contract (first run) | 23/30 anchors (1:6) | best form | "things found, then dropped" |
| must-land list (v2) | 27/30 | 7,451 words, 897-word paragraphs | catalogue |
| ranked budget, ≤2 assemblies (v3) | 19/30 | form restored | recall loss |
| budget plus fixes (v4) | 22/30 | serial tour, 17 "develops" | still one anchor short |
| lossless index plus lookup, Astra (v14) | high | 6,500 words, excursions | touring |
| cheap selector → strong writer (v14 composition) | lost the eye film | 1,221 words, clearest | "consequential exclusion" |

No contract achieved both. The structural cause: one writer must select *and* compose from a large set of atomized
records, and any mechanical selection rule is blind to payoff. The user's sense of an "iterative limit" is visible
here: each fix moved the problem along the same trade-off curve.

### 4.3 Dilution re-examined: stance and permission matter more than size, except at very large sizes

The North Star's dilution sentence ("4:34 cold Opus scored above Opus with the dictionary or the full package")
rests on one ayah. The records weaken it in four ways:

1. **Instruction confound.**
   - Only the cold arm's evidence clause says "and your own knowledge of Arabic and the Quran".
   - Every other arm is told "Work only from the supplied evidence" (write_v10.md, line 3).
   - Result: the dictionary-fed arms (dict and dhft, 14 runs) cite **0–3 passages outside the surah**, with zero in 10
     of 14, including 6 of the 7 Fatiha ayat, 4:34 and 100:1. The cold arms cite 3–28.
   - v11's README already called this "mostly an instruction artefact".
   - Phase 2 D quantified the confound:

     | group | outside-surah passages cited (median, range) |
     |---|---|
     | dictionary-fed arms *with* memory permission (v11 brief, n=16) | 30 (12–47) |
     | the same inputs without permission (n=24) | 1.5 (zero in 10 runs) |
     | cold arm | 10.5 |

     Within the permitted group, input size does not predict outside reach (Spearman −0.03).
2. **Noise floor.**
   - The only true repeat (4:34 cold vs cold2) shares 28 of 47 cited passages (Jaccard 0.596) and scored 8 against 6
     anchors.
   - The dictionary arm sits inside that band (0.52–0.54). The cold-vs-fed gap (8 against 5) is about the size of
     sampling noise.
   - An arm with far more input than the cold arm (dict + slim Luna, 225k tokens) scored highest (9), while the full
     package (318k) scored 5. Size alone does not predict recall.
3. **Thinking collapses only at very large inputs.**
   - It collapses for full packages: 4:34 45k → 9k thinking tokens; 5:6 42k → 8k; 18:96 29k → 11k (packages of
     140k–420k billed tokens).
   - It does not fall on 18:86 or 103:1–3.
   - The dictionary alone *raised* thinking in 8 of 12 ayat.
   - v12 gave the writer 2–5× v11's input and thinking did not fall.
4. **What does hurt is stance.**
   - verdict-carrying inputs: v10's "no value" labels; v12's "never the plain sense" line;
   - audit instructions: v12's per-ayah chain verdicts;
   - obligation lists: v3, v4, v9, v13 v2.
   - v13's step 1 took a 60–161k-token packet and still found nearly every anchor: dilution is a synthesis-stage
     problem.

**Inference.**

- Bulk input costs money at any size (claude -p bills it at 2×).
- It costs thinking above roughly 150–300k tokens.
- Below that, what dilutes synthesis is pre-judged content, audit instructions and the lack of permission to use the
  model's own knowledge.
- Supply without an instruction saying what to make of it is inert: the Fatiha well sat in v15's scene lines and was
  set aside until the coalition line was added.

### 4.4 Pretraining against data (Q2a)

| the model supplies it (push nothing, verify after) | evidence |
|---|---|
| Quran text and references | v11/v12 S1: 0 missing, 0 wrong-ayah after the check |
| famous classical images and their phrases | the cold arm quoted 7 dictionary phrases it never saw (ṭarīq muʿabbad, saraṭa, ḍālla, arḍ kanūd, al-ʿaṣrān, ikhrāj al-lubb); against the full six early entries, 12 of its 14 non-Quran Arabic tags are attested (Phase 2 D) |
| ~~small famous concordances~~ | withdrawn: the ḥamaʾ recall at 18:86 is contaminated by the brief's citation example "(15:26, 15:28, 15:33)" |
| thematic cross-surah parallels | inter-ayah memory follow-up: 299,667 suggestions, 48% strong, only 68 overlapping retrieval; 92.5% cross-surah |
| same-surah parallels, when attention allows | the cold arm cites 2–3× the same-surah passages of v15 |
| grammar, Turkish drift, mechanism schemas | v13/v15 records ("good, better than v12"); the well needs its rope and pulley |

| data must supply it | evidence |
|---|---|
| rare branch senses | sabal eye film, ʿayn = sun disk, ʿalam = waymark mountain, ʿaylam, the husband's nushūz as harshness. Phase 2 D annotated by hand every lexical claim of 13 cold readings (344 latent branches). Cold recall is 11.9% (dictionary-fed at least 19.2%): 35% for branch positions B001–B003 but 3% for B004+; 21% for branches with 4–6 early sources, 4–5% with 1–3; **0 of 60** never-activated branches; 1 of 56 collocation branches. (Phase 1's "105 of 109 only when fed" was an Arabic-script detector artefact: senses given in Turkish were missed.) |
| counts and dominant roles of mid-frequency words | nafakha as animating only with concordance counts |
| quotable classical phrases | 33% of Arabic tags in dictionary-fed runs are dictionary phrases vs 1% cold; mirfaq's leaning phrase reached v15's writer only through the evidence step |
| cross-ayah coalitions | the partner branch belongs to another ayah's root (v11: 7 of 9 misses) |
| a check on memory | **corrected:** memory's quoted phrases are real (12 of 14 attested in the early entries; ḍalla l-māʾu fī l-laban is Tahdhīb's order, Maqāyīs has the other; the 2 unmatched are constructed grammar examples). Phase 1 checked against truncated packet text. What memory lacks is marking (recall marks 0 in every cold run) and construction scope (arḍ kanūd applied to insān at 100:6). |

Two more signals:

- **Where recall ends.** 42% of the 11,637 Quranic branches were never activated by any HFT or v12 reader. The rate
  is 64% for roots with 0–1 words, falling to 13% for roots over 100. Minor branches of rare roots are where memory
  runs out.
- **Canonical bias in labels.** The inter-ayah labels are canonical: they suppress exactly the loaded-word links
  (18:86 → 15:26/28/33 "no value"; 18:96 → 15:29/38:72 "medium").

**Inference.** A small, targeted supply beats both "cold" and "full package":

- the ayah's and window's rare branches with their classical phrases and their `branch_kind`;
- counts and dominant roles for lemmas the model half-knows;
- permission to use memory, with memory marked and verified.

Verifying memory means checking the dictionary's branch and its construction scope, not only that a sense is
attested somewhere. Model memory, like Lisān, tends to fold collocation-bound senses into the root (§5).

### 4.5 Labelled data (Q2b)

| set | size | independence from the current ranks | use |
|---|---|---|---|
| v12 cross-run findings | 12,807 findings; ~30k strong cross-root branch pairs; 479 reject pairs | independent; LLM readers; primary-sense bias (49.5% of targets are B001) | train/evaluate a pair reranker, grouped by surah |
| inter-ayah reviews | 623,600 graded retrieved pairs + 299,667 memory pairs | partly circular; canonical-biased | ayah reranker (pilot positive: NDCG@20 0.745 → 0.853); a bias probe |
| feedback-reranker splits | train 38 surahs, validation 8, 11 reserved, 19 sealed blind | held-out protocol ready | evaluation harness for any new measure |
| HFT traces | 216,787 steps (word → branch → role); 90 of 114 surahs; S2, S4 and 22 more missing | low–moderate coupling | trigger → branch silver labels; chain seeds |
| v5 discovery | 96,140 anchored activations, 84,062 decisions | independent; Luna judgments | weak labels |
| root-dossier map | 25,203 occurrence → plain-branch rows, 123 roots | independent | plain vs latent branch; loaded words |
| channel reviews | 110 surahs; 50,577 motif citations | **circular** (44% of motif pairs are top-10 neighbours in the current affinity, vs 4% random) | recall check only |
| gold | S1 ledger 26 items / 62 pairs; 29:38 19 links; v11 S1 anchors 78; v13 hand scores 52; v14 1:6 criteria 15; North Star cases | independent (S1 is in-sample for the current weights; v15's scene inventory knew the examples) | evaluation only |

**Answer so far.**

- There is enough to train and evaluate a *pair reranker* at scale, with held-out surahs.
- There is not enough gold for the "aha" layer (complementary roles, loaded words, contrasts). A learned metric on
  S1 alone did not generalize (root-group-held-out 5 of 54).
- Any learned model must stay an ordering, never a filter, and must be scored on independent gold.

### 4.6 The quran-slm distance (Q5)

- **How it is built:**
  - nodes are dictionary branch cards (10,932 Quranic; 18,785 with Furūq);
  - the text is only the Arabic image, definition and classical phrases (66% of characters are phrases);
  - three signals (multilingual-E5-small, NeoAraBERT, character 3–5-gram TF-IDF) become directional ranks over all
    *other-root* cards;
  - they are fused as 0.35 E5 + 0.35 Neo + 0.30 char, by symmetric reciprocal rank;
  - the 70/30 dense/char split was calibrated on the S1 water path, so S1 is in-sample.
- **What it measures.** Near-synonymy.
  - Across the Quran (1,500 sampled sources, Luna scene tags as labels), its top 10 is ≈45× enriched for "same
    scene, same role" but only ≈6.7× for "same scene, other role".
  - Other-role scene partners sit at median rank 2,703.
  - Examples: pulley ↔ rain-water is 64/81 locally (6,654 globally); the lead animal ↔ the stray is 77 of 144.
- **Blind spots by construction:**
  - same-root pairs are excluded, so it cannot relate a root's branches (NS7) or recurrence (NS5);
  - no contrast or complement: S1's standing ↔ disappearing and soft ↔ hard rank 21–82;
  - alternative/qirāʾāt roots (س ر ط, و ل ه) are absent from the surah views;
  - multi-scene cards are averaged: the well pulley shares a card with sword hilts and bed legs;
  - hubness: E5 never puts 786 cards in anyone's top 10.
- **Where it works, and v15 threw this away:**
  - As a *conditional branch selector*: given two words already linked by context, it picks which branches cohere
    (MRR 0.540, Neo alone 0.558, latent–latent pairs 0.503, random 0.145, on independent v12 data).
  - Luna scene tags score 0.31 on that task, dictionary neighbour links 0.25.
- **Complementary signals that exist locally:**
  - Luna scene roles (the only complementarity signal);
  - QAC co-occurrence (74,185 root pairs co-occur in an ayah);
  - grammar co-argument frames and collocation profiles (unused by every version);
  - dictionary neighbour relations (29,912, including 678 polarity pairs and 229 antonyms);
  - shared-component mentions (a card naming ماء or بئر: pulley ↔ well rank 1);
  - Qnet keywords;
  - qirāʾāt letter exchanges and metathesis (758 metathesis pairs);
  - root-dossier roles;
  - v12 co-citations.
- **The agent's candidate metrics:**

  | id | metric |
  |---|---|
  | M1 | context gate, then similarity picks the branches |
  | M2 | scene-role complementarity |
  | M3 | clause-level ("micro-motif") embeddings |
  | M4 | shared-component graph |
  | M5 | heterogeneous typed graph with meta-paths |
  | M6 | learned pair metric |
  | M7 | ayah-level Pareto parallels |
  | M8 | set-conditioned coalition growth |
  | M9 | usage-role concentration for loaded words |

  Phase 2 tests them.

### 4.7 Economics

- **Cost structure.** `claude -p` bills input as a 1-hour cache write at 2× ($8/M) and output at $20/M.
  - In cold arms, 88–94% of cost is output, mostly thinking.
  - In package arms, 86–90% is input.
  - In v15, 48% of all Opus spend is cache writes on prompts used once.
- **Opus per ayah, measured:**

  | run | per ayah |
  |---|---|
  | cold arm (median; range) | $0.44 ($0.32–1.58) |
  | dictionary arm (median) | $0.62 |
  | full package (median) | $1.96 |
  | v11 | $1.1–1.9 |
  | v12 | $2.99 |
  | v13 | $3.7–6.8 |
  | v15 Fatiha | $1.25 |
  | v15 long surahs | $2.3–2.5 |

- **Never built, three times over:** the Batch API (half price) plus a cached shared prefix, designed in v8, v11 and
  v13.
- **Inference.** A design of one or two Opus calls with compact inputs lands at about $0.3–1.0 per ayah through Batch.
  The North Star's ~$1 aim is reachable without a weaker synthesis model.
- **Effort above high does not pay.** xhigh gave more scenes, not anchors, at 2–3.4× the cost. Max failed on the
  CLI's 64K output cap twice ($5.71, $10.28).

### 4.8 Process lessons

- **Every version since v11 was replaced before its planned measurement ran:**
  - arm S writers;
  - the Opus judge;
  - the blind read;
  - the S29 probe;
  - the `--no-usage` arm;
  - v13's 5:6 dilution arm;
  - the v14 Opus control.

  Decisions rest on single samples, while two identical runs share only about 60% of their citations.
- **Contamination:**
  - CHANNELS.md (worked Fatiha answers) was embedded in v3–v5 prompts;
  - v10's brief named "a well, a support";
  - v15's scene inventory roles mirror the North Star examples.

  S1 cannot validate discovery.
- **Writer self-accounting took 20–51% of output** (v14) and overstated coverage (180 of 192 items "connected").
- **Recording gaps.** Model and cost provenance is missing for the surah products, v3–v4, Luna runs and v14's
  Sol/Astra.

## 5. What the sister repos add

### The dictionary principle (user correction, 2026-09-28)

**Late compilations are not sense evidence.** Lisān al-ʿArab, Lane and al-Qāmūs fold collocation-bound senses into
the root's senses. The user's example is ḍaraba:

- its bare root image is a single strike;
- "travelling" belongs only to the construction ḍaraba fī l-arḍ;
- Lisān lists it among the root's senses ("ضرب في الأرض … إذا سار فيها مسافرا").

That construction-to-root drift is exactly what the project's own dictionary, built from the earliest dictionaries,
prevents. The dictionary encodes the guard on every branch as `lexicalization_scope.branch_kind`:

| branch_kind | branches |
|---|---|
| bare | 3,326 |
| mixed_non_bare | 5,653 |
| non_bare | 749 |
| collocation | 1,803 |
| unresolved | 242 |

For ض ر ب, B001 (striking) is `bare`, while B002 (going about the earth) is `collocation`: "yalın köke yolculuk
anlamı yüklenmez". So are the parable (B003), refraining (B004), staying the hand (B005) and the stallion (B011).

**This guard is unharvested.**

- v3–v5 carried `lexicalization_scope` in their branch registries.
- v9–v15, the quran-slm cards and v15's scene index never used it. The card for ض ر ب B002 contains "الضرب في الأرض"
  and is tagged as travel, so any ḍaraba occurrence can pick up a travel partner without its construction.
- When Opus is shown the entry, it applies the constraint. The 4:34 dictionary arm writes: "Yolculuk anlamı
  'yeryüzünde' gibi bir tamamlayıcı ister".

**Model memory carries the same drift risk as Lisān.** Verification of a memory-sourced sense must therefore check
the branch kind and whether the construction is present, not merely whether the sense is attested somewhere.

### Other material

- **Classical lexicons nobody has used,** in `quran-roots/_corpus/lexicons/cache/`. Given the principle above, only the
  early, construction-aware material may count as evidence. The late compilations are at most secondary witnesses
  (for example, for an exegete quoted on a specific ayah, with the construction shown). Never branch evidence and
  never a sense supplier.

  | source | coverage | status under the dictionary principle |
  |---|---|---|
  | Majāz al-Qurʾān (Abū ʿUbayda, d. 209) | 1,308 ayah-keyed glosses | early; glosses a Quranic phrase in its construction: usable as construction-level evidence |
  | Lisān al-ʿArab | 9,411 entries, 19.4M characters; 6,133 marked Quran quotations; cites al-Farrāʾ, al-Zajjāj, Abū ʿUbayda, Mujāhid and Ibn ʿAbbās | late compilation; folds collocations into root senses: not a sense source; at most a witness for the early glosses it quotes |
  | Lane | 60,221 entries | late and English: not evidence |
  | al-Qāmūs | 10,370 entries | late: not evidence |
  | Asās al-Balāgha | 3,823 entries | late (al-Zamakhsharī); separates literal from figurative, but judge it under the same principle |
  | al-ʿAskarī's al-Furūq | 919 near-synonym contrasts | a secondary aid for NS2/NS5 contrasts, not a sense source |

  The sabal eye film does not need Lisān: it is al-Jawharī's (Ṣiḥāḥ) definition, already among the dictionary's six
  early sources.

- **Per-ayah citations inside the early entries (unindexed):**
  - Mufradāt: 8,056 ayah references to about 3,900 loci;
  - Tahdhīb: 3,239;
  - ʿAyn: 530 marked Quran quotations;
  - Majāz al-Qurʾān: 1,308 ayah-keyed entries.

  Together they give a script-built "what the early lexicographers said about this ayah's words" file. Each citation
  shows its construction, so collocation-bound senses stay bound. Lisān's 6,133 quotations may only point to the
  early glosses they repeat.
- **Maqāyīs aṣl statements.** 473 roots declared "one aṣl", 205 "two". A citable single concept per root for NS7.
- **No classical tafsir, munāsabāt (al-Biqāʿī) or iʿrāb text exists locally.**
- **Unused ready layers:**

  | layer | size | serves |
  |---|---|---|
  | grammar translation-support records | 24,935 rows | NS2 grammar that matters |
  | contextual collocation profiles | 33,552 rows | NS5; ḥamaʾ collocates with ṣalṣāl/masnūn 3 of 3; nafakha with rūḥ 5 of 9 |
  | Turkish gloss error profiles | 55k glosses with loses/adds/collision | NS2 |
  | adjacent-ayah bridges | 36,493 typed items, 114 surahs | NS3 |
  | water secondary-resonance sweep | 259 targets | an image-first precedent |

- **quran-roots activation lineage (July; NEW to this repo).** It holds recorded lessons that match the user's
  diagnosis:
  - "Schema-first pipelines suppress exactly the discovery they exist to harvest";
  - "synthesize free, anchor afterward";
  - a mandatory exhaustiveness challenge turn;
  - free dialogue ≈10/10 S1 gold, schema pipelines 2–4/10;
  - Qnet decompose/recompose on Sonnet ≈10/14 with 0 unanchored spans;
  - the definitional cross-reference detector called "the highest-yield cue class… a weekend of code", never built.
    A scratch prototype found 33 S1 hits, including ض ل ل B005 "لا يعرف ربها" ↔ ر ب ب.
- **Gaps and defects:**
  - HFT is missing for 24 surahs, including S2 and S4, so 4:34 has none;
  - channel reviews are missing for S108, S110, S113 and S114;
  - the dictionary S1 audit found 11 of 157 branch definitions needing correction, all unrepaired.

## 6. Unharvested opportunities, ranked by evidence and cost

| # | opportunity | evidence | cost | serves |
|---|---|---|---|---|
| 1 | Stop killing readings between stages: no verdict inputs, no per-member chain verdicts, set-asides and record-level fragments handed forward, a visible index of anything unselected | §4.1; v12, v14 composition, v15 window | instructions + scripts | NS8, NS11 |
| 2 | Permission to use memory, marked and verified by script, in every synthesis call | §4.3 confound; v11 0-missing checks | free | NS6, NS10 |
| 3 | Targeted supply instead of bulk: rare branches with classical phrases, counts and dominant roles, a parallels list | §4.4 | scripts | NS3, NS5, NS6 |
| 4 | Use complementary configurations together (e.g. a cold Quran-memory reading plus a rare-branch reading plus a chain reading) and integrate once | §3 (1:6 four-way); cold vs cold2 overlap 0.6; v11 "ledger captures most of the union" | Phase 2 | NS3–NS7 |
| 5 | Re-synthesize the v5 harvest (909 ayat, 96k anchored activations, including rejects with reasons) with Opus from a ~16 KB digest per ayah | §2 v5 | ~$0.5–1/ayah est. | Q3 |
| 6 | A coalition-first surah step (v11 arm S) plus progressive-disclosure overlays (Layer 2.5): never run end to end | §2 v6–v7, v11 | one Opus call per surah | NS4, NS8, NS12 |
| 7 | Script discovery layer: definitional cross-reference detector, loaded-word detector (collocation profiles + dossiers), IDF + phrase + ayah-map parallels, typed contrasts | §4.6, §5 | scripts | NS3–NS7 |
| 8 | Per-ayah early-citation file (Mufradāt, Tahdhīb, ʿAyn, Maqāyīs, Majāz), each citation with its construction; late compilations (Lisān, Lane, Qāmūs) never as sense evidence | §5 | ~1 day scripting | NS10, NS7, NS2 |
| 8b | The `branch_kind` guard (bare / mixed / non-bare / collocation): a collocation-bound branch is activatable only where its construction is present. Apply it in the scene index, the distance, script discovery and memory verification | §5 dictionary principle | scripts (grammar attachments give the constructions) | NS10, NS11, NS1 |
| 9 | Batch API plus no 1-hour cache writes on single-use prompts | §4.7 | engineering | NS13 (≈½ cost) |
| 10 | Unused layers for NS2/NS3: grammar translation-support, gloss error profiles, adjacent-ayah bridges, Maqāyīs aṣl | §5 | scripts | NS2, NS3, NS7 |
| 11 | A fixed blind scorecard with two replicates per decision, frozen before the next change | §4.8 | small | process |
| 12 | Data fixes: 11 ambiguous roots, 704 scattered scene ids, 11 unrepaired dictionary definitions, HFT gaps (24 surahs) | §2 v15, §5 | scripts + a few Luna jobs | NS10, NS4 |
| 13 | Untested model questions: an Opus control on v14's handover; the v10 five-arm design (Luna → Opus, Opus brief → Sol) | §2 v10, v14 | small runs | NS13 |

## 7. Preliminary answers (Phase 2 tests them)

- **Q1.** No. The system is at a local optimum of one method (one pipeline, tuned by trial on a few named cases,
  each fix moving along a recall–form trade-off). It is not at the limit of what the data and models allow. Large,
  cheap opportunities are untouched (§6), several of them already built or designed and never run.
- **Q2a.** The model covers Quran references, famous lexicon, small famous concordances, grammar, Turkish drift and
  thematic parallels. Data must supply rare branches, counts, classical phrases, cross-ayah partners and
  verification. Verification includes the `branch_kind` guard, because memory, like the late lexicons, folds
  collocation-bound senses into the root. The inter-ayah labels show why canonical relevance must never gate a
  reading.
- **Q2b.** There is enough labelled data to train and evaluate a pair or ayah reranker with held-out surahs. There
  is not enough gold for complementary roles, contrasts or loaded words; those need a small curated set.
- **Q3.** Plausible, with conditions:
  - read v5's discovery JSON, including rejects, not its prose;
  - use a compact deterministic digest;
  - drop "every finding must land";
  - integrate with Opus;
  - add the cross-ayah partners v5's per-ayah lanes could not see.

  The v14 composition failure shows what happens without a visible index of what the selector left out.
- **Q4.** Candidate directions that the evidence supports, for Phase 2 to design and critique:
  - "synthesize free, anchor afterward" with a small targeted supply;
  - several complementary cheap readings integrated once;
  - surah-first: coalitions, then per-ayah disclosure.
- **Q5.** Not a better single similarity but a typed, context-conditioned proximity:
  - candidates from Quranic context;
  - the existing similarity to choose branches;
  - complementary-role, shared-component, contrast, sound-echo and loaded-word edges for what similarity misses;
  - every candidate carrying its path as its explanation;
  - ordering, never filtering.

## Appendix: files

- `review/phase1/agents/*.json`: the eleven agent reports (structured; every claim with its file evidence).
- `review/phase1/scripts/`: the counting and checking scripts the agents wrote (read-only), plus the dilution metrics
  (`metrics.tsv`: 165 runs, 17 ayat), cited-passage overlaps (`overlaps.tsv`) and Arabic-tag source classes
  (`tags.tsv`). The scripts reference the session scratch paths they ran from.
