# Phase 2 report: designs, critiques and a recommendation

Written 2026-09-28, after Phase 1 (`PHASE1_REPORT.md`, `EXECUTIVE_SUMMARY.md`).

## 0. What was done

- **Nine read-only agents; no Luna or Opus pipeline runs.**
  - Five independent proposers:
    - A, a step on top of v5;
    - B, a non-iterative method;
    - C1, a branch-level distance;
    - C2, loaded words, parallels and a harvest sheet;
    - D, knowledge-aware supply.
  - Three critics: cost; North Star fit and the watch cases; dilution and pruning.
  - One completeness critic.

  The proposers built and measured prototypes with free local scripts. The critics re-ran or extended those scripts
  and tested them on independent data. Agent reports are in `phase2/agents/`, scripts in `phase2/scripts/`, and three
  sample supplies in `phase2/samples/`.
- **The first launch was stopped about two minutes in,** before any result. The user's correction on late lexicons
  (the dictionary principle, §5) had changed a premise. The relaunch carried that principle as a binding rule. Four
  agents were later cut off by an interruption or the session limit and were restarted automatically. No result was
  lost.
- **The user's rulings during Phase 2:**
  1. A collocation-bound branch whose construction is absent goes to an *echo tier*. It is shown as a marked
     construction-level echo ("in the phrase X this root means Y"), never stated as the word's sense here.
  2. A loaded word whose role is construction-bound (nafakha: *fīhi min rūḥī*) is stated as a *usage-role statement*
     ("in 5 of its uses the same verb breathes life into a formed body"), never as a transferred sense.
- **Phase 1 claims corrected by Phase 2.** I verified each one and marked it in the Phase 1 documents:
  - **ḥamaʾ.** The ḥamaʾ recall at 18:86 is not memory evidence. The shared v10/v11 brief's citation example is
    literally "(15:26, 15:28, 15:33)".
  - **Memory phrases.** The phrases memory quotes are real: 12 of 14 are attested in the six early entries. "ḍalla
    l-māʾu fī l-laban" is Tahdhīb's order.
  - **Rare senses.** "105 of 109 rare senses only when fed" was a detector artefact. Hand labels give memory 35%
    recall at B001–B003 and 3% at B004+; 0 of 60 never-activated branches; 1 of 56 collocation-bound branches.
  - **Thinking collapse.** It is not a size threshold. v11/v12/v13 runs at 140–380k kept 42–138k thinking tokens.
    The collapse belongs to the full Luna package under the no-memory brief.
  - **Memory permission.** It is confounded with v11's "collect every finding" ledger (all permitted, fed runs had it).

## 1. Bottom line

1. **All five designs converge on one shape:**
   - a free script supply per ayah;
   - an Opus reading allowed to use memory, with memory marked;
   - script checks afterwards;
   - a chain map before the ayah calls and a surah layer after them;
   - no stage between discovery and writing that can drop anything.

   What remains undecided is how many Opus calls per ayah: one, two in sequence, or two parallel readings plus an
   integration. That is a question for a cheap experiment, not for argument.
2. **Scripts should annotate, never order, score or withhold.**
   - The only ordering with a claimed gain was C1's neighbour activation (+0.04 MRR on v12 labels). It fails on an
     independent test of exactly the 29:38 kind: 3,398 HFT surprise cases outside the named surahs. There C1 scores
     MRR 0.296–0.332, against 0.355–0.393 for random order and 0.371 for plain dictionary order.
   - What works are typed, explained paths. The dictionary's own definition of the eye film names the spider, and
     29:41 ranks first of 6,235 ayat by that link. Other examples:
     - rare-word bridges (ghishāwa at 2:7 and 45:23);
     - concordance grouped by construction (nafakha: *fī ṣ-ṣūr* ×10, *fīhi min rūḥī* ×5);
     - formula echoes (ن ف خ and س و ي co-occur exactly in 15:29, 18:96, 32:9, 38:72);
     - a parallels union across lenses.
3. **The dictionary principle cannot be enforced by script before synthesis.**
   - All four construction detectors miss most real constructions: 44–79% false "absent" on the root-dossier
     placements.
   - The pipeline should therefore push the dictionary's scope note and construction phrase for every branch and
     every chain member, and let Opus apply them. Opus does: the 4:34 dictionary arm restricted "travel" to fī l-arḍ
     unprompted.
   - Script flags go to the record and to the user, never into deletion or repair.
4. **18:86 and 18:96 are stance problems, not supply problems.** The ḥamaʾ passages were in every run and were still
   called "a root similarity, not an equation". The brief needs one generic loaded-word lens (a usage echo with Quran
   references), and the writer must not be fed dismissive prose.
5. **Contamination is wider than known:**
   - the brief example "(15:26, 15:28, 15:33)";
   - v15's scene inventory, which lists "film over the eye", "lead animal", "stray" and "follower" as roles;
   - CHANNELS.md in v3–v5.

   29:38 is clean only in the briefs; any design using the scene paths is answer-fed there too. Every input layer
   needs a lint.
6. **The largest change is methodological,** and it is what stops the iteration:
   - a frozen scorecard;
   - replicates strong enough to detect a lost item (≥3 of 4, not "1 of 2");
   - handover-isolated replicates;
   - retention counted as assembled readings, not branch ids;
   - seeded blind ayat;
   - a contamination lint;
   - a blind read by the user.
7. **Cost is reachable.**
   - One or two Opus calls per ayah through the Batch API cost about $0.7–1.0 per ayah. The parallel-readings design
     costs about $1.75.
   - Tests on the CLI cost about $1.2–2.0 per ayah.
   - The CLI's 64K-per-response cap forces the longest ayat and long-surah commentaries onto the API.
   - The Batch runner has never been built, and the CLI showed no prefix reuse across calls.

## 2. Answers to the user's questions

- **Q1. Is this the most we can do?**
  - **No.** The recurring losses are known and structural:
    - verdict inputs;
    - chains judged from one member;
    - set-asides nobody reads;
    - selectors hiding what they drop;
    - records-to-prose handovers.
  - Several free layers were never used:
    - the dictionary's `branch_kind`;
    - early-source phrases for every branch;
    - definitional joins;
    - root- and construction-level concordance;
    - grammar collocation profiles;
    - the parallels union;
    - Turkish gloss losses.
  - What is not yet shown: that any design beats the v5 bar on this reader's criterion. That needs the experiments in
    §8.
- **Q2a. Where does the model's own knowledge suffice?**
  - **Memory suffices for:**
    - Quran references and thematic cross-surah parallels;
    - primary senses and the early, famous secondary senses (B001–B003: 35%), with real early phrases;
    - grammar and Turkish drift;
    - the construction scope of famous cases.
  - **Data must supply:**
    - minor and rare branches (B004+: 3%; never-activated: 0 of 60) with their early phrases;
    - construction scope in general (1 of 56 collocation branches recalled; *arḍ kanūd* was applied to *insān*);
    - root-level counts and dominant roles (nafakha);
    - partners in other ayat;
    - marking, which memory never does unprompted.
  - **Policy:** push every non-plain branch with its phrase. A fitted "memory score" gate saves only 12–22% of
    tokens and drops exactly the rare cases. Allow memory, mark it, and verify it against the six early entries and
    the construction scope.
  - **Still open:** whether memory permission alone, without v11's ledger, restores outside-surah reach (experiment
    E1).
- **Q2b. Enough labelled examples to train?**
  - **For a branch-pair reranker, yes:** about 30k independent v12 pairs. But a learned metric does not beat plain
    NeoAraBERT (0.503 vs 0.521), and its learning curve is flat from 10% of the data. The features are the
    bottleneck, not the labels.
  - **For the surprise class, no:**
    - the gold for complementary roles, contrasts and loaded words is S1- and 29:38-sized;
    - the inter-ayah labels are canonical-biased (18:86 → 15:26/28/33 "no value"; 5:6 → 5:95/5:97 "no value");
    - the channel reviews are circular with the current ranks.
  - **A usable held-out test set exists:** the 3,398 HFT surprise cases. So does a held-out ayah-level protocol:
    19 sealed surahs in the feedback-reranker splits.
  - **Blocked:** a cross-encoder fine-tune cannot be tested until the broken quran-slm Python environment (no torch)
    is repaired.
- **Q3. A step on top of v5?**
  - **Yes, but the value is not in v5's Luna work.**
    - 89.5% of v5's 96k activations reuse a branch that HFT (64%), the channel reviews (16%) or v12 had already
      nominated.
    - A script union of those sources reproduces 98% of v5's branches.
    - Only 25% of the readings assembled in candidates v5 rejected survive as readings.
  - **Do not rerun v5's Luna lanes elsewhere** (about $3k).
  - **Use v5 in two ways:**
    - as a label-free relay of its upstream sources, with every branch flagged by `branch_kind`;
    - on the 909 v5 ayat, as one more *reading stream*: v5's middle prose, integrated with a permitted fresh reading.
      This is the cheapest Q3 test.
  - **Tier 3 needs a decision:** 24 long surahs with about 3,113 ayat have no HFT and no v5.
- **Q4. A significantly different method?**
  - **Methodology first:** see point 6 of the bottom line. Every version since v11 was replaced before its
    measurement ran, and decisions were made on single runs whose citations overlap only about 60%.
  - **Architecture:** synthesize free, anchor afterward.
    - The model writes from finished readings, not atomized records.
    - A script computes what it left out and returns it once.
    - QeQ comes structurally after the latent reading.
  - **Three alternatives nobody has tried:**
    - one session with staged supply (cold reading, then rare branches and joins, then the chain slice, then compose);
    - an agentic "pull" arm like the v9 29:38 pilot the user called "great / excellent" (≈$1.7);
    - a whole short surah in one call (progressive disclosure and NS12 natively).
- **Q5. A better distance?**
  - **Not a better single distance.**
    - The current fused similarity finds near-synonyms. It is at chance on the surprise class.
    - The new neighbour-activation ordering is at or below chance there as well.
  - **Replace ordering with typed path annotations:**
    - the definitional cross-reference;
    - a rare-lemma bridge;
    - concordance grouped by construction, including same-root recurrence, which quran-slm excludes by design;
    - formula and co-occurrence echoes;
    - phrase and word echoes (kaʿbayn ~ al-Kaʿba);
    - the construction guard as a label.
  - Each annotation carries its path in words, and similarity is kept only as a silent tie-breaker. §6 has the
    tables and the new distance ideas still to test.

## 3. The recommended design (a candidate to test, not a v16 yet)

| stage | who | what |
|---|---|---|
| S0 supply | script, free | See the supply list below. |
| S1 chain map | Opus high, per short surah or pericope | Grounds, extends and connects the existing chains (never rediscovers them). Chain members shown with scope notes. No set-asides. Returns a per-ayah disclosure plan (opens / advances / completes). A lean index keeps input bounded. |
| S2 reading and writing | Opus high | **Arm F1:** one call reads, does QeQ after the latent readings, and writes. **Arm F2:** a latent reading, then a second call that does QeQ from memory after it and composes the commentary; no independent canonical reading ever reaches the writer. **Arm B:** parallel memory and lexicon readings plus an integration; built only if experiment E2 shows integration adds recall beyond noise. The brief rules for all arms are listed below. |
| S3 checks | script | Every Arabic quotation sourced. Memory phrases attested against the six early entries. Construction flags sent to the record and the user, never deleted. An unused index of left-out sentences and paths, counted as readings, not branch ids. Disclosure-plan check. Negation-frame rate. |
| S4 return | same Opus session (tested as an option) | One turn: the unused sentences and paths, plus the flags phrased "name the construction this sense belongs to, or mark it as a phrase-level echo". Never "drop". |
| S5 surah | Opus high | Short surahs: one call. Long surahs: pericope, then surah, through the API. Reads a chain-bounded unused list (chain members never mentioned), not the whole index. |

**S0 supply, built by script.** Everything is descriptive: no grades, counts-as-verdicts, sorting by popularity or
"present: no".

- the surah text, or window plus same-surah list for S2;
- the word table;
- every branch of every root in the ayah, with image, early phrase (never gated), Turkish gloss, `branch_kind`, and
  the dictionary's scope note with the construction phrase;
- the [plain] mark (root-dossier) where it exists;
- typed path annotations:
  - definitional joins;
  - bridges through rare words (in 30 or fewer ayat);
  - concordance grouped by construction for roots with 40 or fewer uses;
  - partner counts by form;
  - formula echoes;
  - the parallels union (root, lemma, phrase, word echo, loaded role, text map);
- the channel subchannels touching the ayah, members with scope notes;
- the label-free HFT/v12/v5 relay where it exists;
- qirāʾāt and alternative roots;
- Turkish gloss losses.

**Kept out of the prompt:**

- quran-slm pair lists (they can go in a lookup);
- v15 scene paths (until the inventory is rebuilt blind);
- any guard verdict computed by a heuristic.

**Brief rules for every S2 arm:**

- memory is permitted and marked;
- no audit instructions;
- no named cases (a lint enforces this);
- a coalition of words is an activation;
- a loaded word is stated as the Quran's usage, with references;
- a collocation-bound sense is a phrase-level echo unless its construction is in the text;
- QeQ comes after the latent readings and never cancels a reading;
- containment is one positive sentence;
- no caps.

**What each proposal contributes:**

- **D:** the permission clause, the root-level concordance, verification against the early entries, and the rule that
  presence verdicts stay out of the prompt.
- **B:** the full branch index with phrases, the definitional joins, the unselected index, the integration arm, and
  the methodology.
- **A:** the relay adapters, the Turkish-loss layer, the chain map and surah layer, and the Tier model.
- **C2:** the [plain] mark, loaded roles as counts, and the parallels union.
- **C1:** the construction-grouped concordance, rare-lemma bridges and definitional pointers. Its ordering is dropped.

**Cost:**

| | per ayah |
|---|---|
| production, one call (F1) or two (F2), Batch API | about $0.7–1.0 |
| production, arm B | about $1.75 |
| tests on the CLI | about $1.2–2.0 |

- The output shape is still unmeasured (20–50k tokens) because of the ledger confound; gate at 50k and measure in
  the first calls.
- Ayat of 40 words or more (109 of them), the 2:282 class and long-surah commentaries go through the API.

## 4. What the critics killed or changed

| proposal element | verdict | why |
|---|---|---|
| C1 neighbour-activation ordering, "N kinds" scores, 3-path limit | dropped | below random on the independent HFT surprise set (verified by the completeness check); 26% of displayed paths go through generic words (الشيء 175×); the eye film's headline activator was لقوم 29:35 |
| Every pre-synthesis construction verdict (B "present: no", C1 echo-only, C2 withholding, A's S4 repair) | dropped from prompts | detectors miss 44–79% of real constructions |
| A's "[N readings]" sorting and "(not used above)" headers | dropped | popularity labels act as verdicts; the lead animal sat on line 99 as "[1 readings]" |
| A's digest as the packet base (238 atomized items) | changed | it rebuilds the records-to-prose wall; v5 enters as a reading stream instead |
| D's memory-score push gate | dropped | on independent cases it pushes phrases for only 44%; phrase-for-all costs only +12–22% |
| C2 "THIS OCCURRENCE DEPARTS" flags | changed to counts and refs | 40–50% precision |
| C2's section C bulk (57–63% of long sheets; threshold tuned on the kohl edge) | dropped | C1-style annotations cover it at about half the size |
| Scene-tag paths and lenses (C1, C2) | dropped until a blind rebuild | the v15 inventory lists the answers as roles |
| B's parallel five-call primary as the default | moved to a test arm | about $1.75 per ayah; its integrator would read the memory reading's canonical verdicts ("not an equation") |
| "Size ≥140k collapses thinking" caps | kept only as cost limits | not a size effect (see §0) |
| "1 of 2 replicates" success criteria | replaced | passes an item that lands 30% of the time with p = 0.51 |

## 5. The dictionary principle in practice

- **The guard exists in the data.** Every branch has `lexicalization_scope.branch_kind`:

  | branch_kind | branches |
  |---|---|
  | bare | 3,326 |
  | mixed | 5,653 |
  | non-bare | 749 |
  | collocation | 1,803 |
  | unresolved | 242 |

- **Where drift was measured:**
  - v5: 5,463 activations of collocation-bound branches, 87% with no construction cue;
  - v15: 12 of 271 finding anchors;
  - the channel reviews: up to 36% of subchannels (an upper bound, from low-recall detectors);
  - quran-slm and scene links: 19–20% of top pairs rest on an absent construction; ḍaraba at 4:34 gets 40 travel
    partners through B002;
  - readings independent readers rejected carry 2.7× more such branches than accepted ones.
- **Detection by script is weak.** Across detectors, 44–79% of real constructions are missed, especially
  derived-form constructions (tawallā) and semantic frames (dhikr "by the tongue"). A form-aware guard (QAC measure
  and voice plus the governed preposition) is the next script to build.
- **Therefore:**
  - push the dictionary's scope note and construction phrase;
  - let Opus apply the user's echo-tier rule;
  - flag afterwards for review;
  - never delete.
- **Not resolved by the rulings:**
  - derived-form and semantic-frame constructions (110 of the 397 root-dossier placements);
  - whether Majāz al-Qurʾān, an early source outside the six, counts as construction-level evidence.

## 6. Q5 detail: what was tested

**Independent evaluation sets:**

- **v12 strong/reject pairs.** Biased toward primary senses: 49.5% of targets are B001.
- **The HFT surprise set.** 3,398 non-B001 outliers activated by neighbours, named surahs excluded. A seeded
  74-case sample was used.
- **Recorded parallels** for 4:34 and 5:6.
- **In-sample only:** the S1 gold ledger and the 29:38 links.

| measure | v12 NA (latent MRR) | HFT surprise set | 29:38 eye film | notes |
|---|---|---|---|---|
| quran-slm fused (current) | 0.549 | ≈ random | 3rd of 8 senses | best as a conditional branch selector on v12 (0.52 Neo) |
| C1 typed union / convergence | 0.594–0.606 | 0.296–0.332 vs random 0.355–0.393 | 1st of 8 (±3 window) | ordering does not transfer; dropped |
| learned metric (12 features) | 0.503 (T1) | – | – | flat learning curve; features are the bottleneck |
| definitional cross-reference (IDF) | 0.470 | not yet scored as path existence | links 29:41, rank 1 of 6,235 | kept as annotation |
| rare-lemma bridge | 0.523 (directional) | – | ghishāwa: 2:7, 45:23 | kept as annotation |
| construction-grouped concordance | – | – | – | nafakha by construction; kaʿb → Kaʿba at 5:95/5:97 |

**Parallels union (C2)** against the recorded parallels:

| case | recall |
|---|---|
| 4:34, same surah, at 10 per lens | 0.55 (0.62 outside ±7), against 0.18–0.27 for single lenses |
| 5:6 | 1.0 |
| 18:86 | 1.0 |
| 18:96, whole Quran | 0.75 |

Previously missing parallels found: 4:90 (by phrase), 2:238 and 4:81 (by word echo), 5:95/5:97.

**Not solved by any script:**

- contrasts: 0 of 62 S1 contrast pairs, even with the dictionary's polarity relations;
- zayyana ↔ the eye film;
- the user's night-shelter link (بيت ↔ عشو, 43:36), which is absent from every 29:38 supply.

**New distance methods still to test, all free unless noted:**

- path existence against a random-root base rate on the HFT surprise set (the next honest test);
- co-citation in the early entries: Mufradāt's 8,056 and Tahdhīb's 3,239 ayah references filed under branches, a
  construction-scoped activation signal that satisfies the dictionary principle;
- HFT co-activation, split by surah;
- a form-aware construction guard;
- clause-level ("micro-motif") embeddings (partly tested with July clause vectors: comparable, not better);
- personalised PageRank over a typed graph;
- a blind rebuild of the scene inventory (Luna, about 193 jobs, needs approval);
- a cross-encoder (needs the Python environment repaired).

## 7. Other Phase 2 findings

- **29:38.** The ayah's own fa-ṣaddahum has ص د د B013 (kohl on a mirror, Tahdhīb) and B012 (a woman's screen or veil,
  Tahdhīb). Both are bare and both sit next to the eye film. The dictionary's ز ي ن branches (beauty, beautifying,
  adornments) attest no "coating" sense, so a coating reading is memory-sourced and must be marked. These are
  evaluation notes only, never pipeline rules.
- **18:96.** The formula echo "fa-idhā sawwaytuhu wa-nafakhtu" (15:29, 38:72; 32:9) against "ḥattā idhā sāwā … qāla
  nfukhū" was found by script and recorded nowhere before.
- **18:86.** The dictionary's ʿayn B008 (the sun disk) and the qirāʾa ḥāmiya (root ح م ي) are in the supply. The
  observer reading still depends on the writer's stance.
- **The Fatiha items the user values.** The lead animal (م ل ك B008), water as mainstay (B007), naʿīm as halt and
  walking (ن ع م B011/B012) and water that stands (ق و م B016) are collocation-bound and have no construction at their
  ayat. Under the ruling they stay as marked echoes.
- **Chains and relays.** The existing chains and the HFT relay carry construction drift too: 13% of HFT surprise
  branches are collocation-bound. Chain members must carry scope notes.

## 8. Experiment plan (every model run needs the user's approval)

| step | what | model runs | cost | decides |
|---|---|---|---|---|
| E0 | Build supply v0, checks, lint (all input layers) and a frozen scorecard. The user audits 60 dossier placements and 30+30 `branch_kind` labels. Score path existence on the HFT surprise set. Build one Tier-3 digest. Size 2:282. | none | $0 | the free layer, and which annotations earn their place |
| E1 | Isolation arm: dictionary-fed, memory permitted, no ledger; 6 ayat that already have cold and dict arms × 2 replicates | 12 Opus (claude -p) | ≈ $8–15 | permission vs ledger (Q2a); the real output shape for every cost model |
| E2 | Integration pilot on existing readings (cold + dict) for 18:86, 4:34, 1:6 × 2 replicates, order swapped, plus one return turn | 12 Opus | ≈ $8–12 | whether integrating finished readings adds recall without a catalogue |
| E3 | Paired arms F1 vs F2 (plus B if E2 passes) on 29:38, 18:86, 18:96 and 4 seeded blind ayat (19:70, 19:73, 19:75, 88:17); the decisive handover replicated 4×; with S1 maps | ≈ 40–60 Opus | ≈ $40–70 | the production arm |
| E4 | Positive control: the v9 29:38 pilot configuration (agentic pull) vs the compact supply, on 29:38 and 2 blind ayat × 2 | ≈ 12 Opus | ≈ $15–25 | whether compact supply loses what the praised configuration found |
| E5 | Batch smoke test: 3–5 requests sharing a surah prefix | API | ≈ $1–3 | whether the production cost figures hold |
| E6 | One blind short surah end to end (S88: map, 26 ayat, surah commentary), read blind against v5 | ≈ 30 Opus | ≈ $40–80 on the CLI | NS12, progressive disclosure, the v5 bar |
| optional | Luna-HFT validation for Tier 3 (12 calls); blind scene-inventory rebuild (about 193 jobs) | Luna | ≈ $1; ≈ $4 list-equivalent | Tier 3 depth; scene paths |

## 9. Decisions waiting on the user

1. **Construction guard scope.** Do derived-form constructions (tawallā) and semantic frames (dhikr "by the tongue")
   count as constructions?
2. **Majāz al-Qurʾān.** It is early and ayah-keyed but outside the six sources. May it serve as construction-level
   evidence?
3. **Production budget ceiling.** About $1 per ayah (F1/F2), or accept about $1.75 (arm B) if B wins in E3?
4. **Tier 3** (24 long surahs, about 3,113 ayat, no HFT). A thinner product, or Luna-HFT (about $71–143 and 27–37
   hours, after validation)?
5. **29:38 scoring.** Reward the "coating" reading of zayyana only when it is marked as memory, since the dictionary
   attests no coating sense?
6. **Reading time.** How many blind pairs per round can you read? This, not dollars, limits the replicates.
7. **Scene inventory.** Drop scene paths, or rebuild the inventory blind?
8. **Gold.** Add your v9 gap list (night shelter بيت ↔ عشو at 43:36; the ʿĀd / ع د د echo) to the frozen gold?
9. **API access** for the Batch smoke test (E5)?
10. **Approvals** for E1–E6, individually or as a set.

## 10. Decisions taken (user, 2026-09-28; completed after the E0 review)

| # | decision | ruling |
|---|---|---|
| — | collocation-bound sense without its construction | echo tier: a marked phrase-level echo, never the word's sense here |
| — | loaded word whose role is construction-bound (nafakha) | usage-role statement with references, never a transferred sense |
| 2 | Majāz al-Qurʾān | allowed as construction-level evidence, only quoted directly from the Majāz text (never through Lisān or other late compilations) |
| 3 | budget | up to about $2 per ayah, measured as the cost the CLI reports for the call(s). A 2–3× model upgrade (e.g. Fable) only after it is shown that ~$2 almost meets the goals and the model is the limiting factor |
| 4 | Tier 3 (no HFT) | if a must, HFT is generated later with Sol or Opus (the user: Luna cannot do it); not now |
| 5 | stretched readings (e.g. zayyana as "coating") | transparent: show how a native speaker or philologist may hear the actual and resonant meanings; no fabrication; a stretch is named as an echo, with its basis |
| 7 | scene tags | dropped from supplies; rebuild only if tests show scenes help |
| 8 | gold examples | probes, not must-finds: a workflow that misses a named example but brings other supported layers that deepen understanding is doing its job. **Exception:** the three watch cases (the 29:38 eye film in as-sabīl, ḥamaʾ as human fabric at 18:86, nafakha as animating at 18:96) stay must-finds |
| 9 | API access | none. Runs stay on the claude -p / codex subscriptions, so the 64K-per-response CLI cap applies and E5 cannot run |
| 1 | derived-form constructions | a derived verb form counts as the construction being present (tawallā, Form V, without ʿan = turning away); a context alone does not, though the writer may say "the context suggests…". Semantic frames (dhikr "by the tongue") remain open |
| 6 | blind-read capacity | 6 pairs per round |
| — | plain sense | "context alone does not count" governs latent readings only; the plain sense follows the canonical / root-dossier reading even when it rests on context |
| — | native hearing | the classical ear of the early lexicons; modern hearings are left out or labelled modern |
| — | when an echo reaches the prose | containment always (the echo stands beside the plain sense, never replaces it). An echo enters the prose only with a warrant: istiqrāʾ (the Quran's own usage, al-Khūlī / Bint al-Shāṭiʾ) or naẓm (the neighbours and the surah's aim, al-Biqāʿī). Without one it stays in the record |

## Appendix: files

- `phase2/agents/*.json`: the nine reports.
- `phase2/scripts/`: the proposers' and critics' scripts.
- `phase2/samples/`: B's 29:38 supply, C2's 18:96 sheet, D's 18:86 packet.
