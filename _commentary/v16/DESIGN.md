# Commentary v16

Current ayah brief: **r4** (runner default), discovery before themes and full coherent development. r5 adds
grounding for contributing passages; r6 (built, not run) replaces the cinematic register with a commentator's.
Both are described at the end.
Earlier sections preserve the design and results of r1-r3.

2026-09-29. One permitted Opus reading per ayah: what already writes coherent prose, plus assembled findings and a
valve for leftovers. Not the PHASE2 §3 design. That design's supply, bookkeeping rules and integration merge are
rejected by the user's E2 read and `review/adversary/REPORT.md`. v16 is the adversarial audit's next step (§6), with
v5's scope prose tested as a second source of assembled findings.

## Why

- **The base.** E1 (the v9 dictionary arm plus memory permission) writes coherent prose and restores the Quran reach
  (`review/EXPERIMENTS.md`). It lacks the concrete chains; on 1:6 that means the pulley and the supported gait.
- **Assembled findings, not atomized records.** The chains already exist upstream, in two assembled forms:
  - HFT and the channel reviews (the user's rule: use the existing chains);
  - v5's scope prose. v5's 1:6 macro lane assembles the well apparatus (müstakīm's upright, bearing part; the
    well-head timber; water made reachable). v5's S100 micro and global lanes cite 10–17 Quran passages outside the
    surah where the v9 dictionary arm cites 0–2.
- **Leave out v5's consolidation.** It requires every finding to land, which produces a catalogue. It also needs
  the ledgers (the 100:1 consolidator prompt is 759 KB).

## The call

- **Base, identical in every arm:**
  - the E1 prompt byte for byte: `v9/prompts/write_v10.md`, `context.md`, `01_dictionary.md`, and the evidence
    clause with "your own knowledge of Arabic and the Quran";
  - `prompts/additions.md`: three rules from `v9/prompts/writer_rules.md`: most candidates stay out; themed
    threads with a thesis; `## Ek Notlar`.
- **Arm H:**
  - the ayah's HFT records verbatim (`v9/input/v2/…/02_hft.md`);
  - the surah channel review's subchannels anchored in the ayah, verbatim, with their parent headers
    (`latent_activation/network/v3/reviews/sNNN/reader_a_pilot.md`, sliced to `work/…/H/channels.md`).
- **Arm V:**
  - v5 scope prose, `{micro,macro,global}.scope.tr.md`, as written by the scope agents;
  - no discovery JSON, ledgers or consolidated prose;
  - a lane whose gzip ratio is below 0.2 is left out. That lane is template-generated ledger text: 100:1 macro,
    254 KB at 0.058; 100:6 macro, 195 KB at 0.085. Natural prose sits at 0.28–0.38.
  - The evidence clause tells the writer that v5's boundary sentences are that reader's caution, not rules.
- **Model and settings:** Opus 5.5, effort high, `claude -p` in safe mode from a temp directory, no tools.
- **Afterwards:** `review/e0/checks/check.py` writes a record next to the reading. It never edits the prose, and a
  model never reads it.

## First test

| ayah | why | baselines already on disk |
|---|---|---|
| 1:6 | the user's pulley and supported-gait probes | E1 rep1/rep2, E2-B (blind), v9 cold and dictionary arms, v5 middle |
| 100:1 | the v9 bar; the 254 KB templated macro lane | E1 rep1/rep2, v9 cold and dictionary arms, v5 middle |
| 100:6 | same; the oath's answer (kanūd), a different stance | E1 rep1/rep2, v9 cold and dictionary arms, v5 middle |

**Calls and cost:** 2 arms × 3 ayat = 6 calls. `v16.py build` estimates $1.03–1.48 per call, $7.28 in total, at an
assumed 40k output tokens; E1 measured 15–30k. No call estimates at or above $5.

**Comparison:** I read the outputs myself against the baselines. The user's read decides.

**If the pulley or the gait still stays out of the threads:** add one same-session challenge turn ("is this
everything, or did you curate?"). If the chains still don't cross ayat: a surah-first pass.

## The dictionary (2026-09-29)

**The v9 file cuts the evidence.** `v9/prepare.py:307` clips every branch's early-source phrases at 220
characters. 603 of 1,791 branch lines in the v9 dictionaries (34%) are cut. Every run that read those files read
them cut: the v9 dictionary arm, E1, v16 H/V. On 1:6 the cut removed Tahdhīb's "القامة البكرة التي يستقى بها الماء"
and "النعامة الخشبة المعترضة ثم تعلق القامة" (the pulley hangs from the naʿāma crossbeam). That is the dictionary's
own join of ق و م (1:6) to ن ع م (1:7), the second key the pulley lacked.

**What the readings use.** Twelve readings were checked: the v9 dictionary arm, E1 rep1 and v16 H/V, each on 1:6,
100:1 and 100:6.

- 173 of 174 dictionary quotations come from `source_phrase_ar`. None comes from the pipeline's Arabic image, scope
  or "not" lines.
- Turkish 4-grams shared with the Turkish fields that were in the packet (definition 9, facets 4, gloss 2) sit at
  the level of fields never shown (source synthesis 6, per-sense glosses 5, scope note 5). The writers translate
  the Arabic; they do not reuse the dictionary's Turkish.

**Size by field** (S1 + S100 roots, 374 branches; share of the entry's text):

| field | share |
|---|---|
| neighbour distinctions | 35% |
| identity judgment | 11% |
| source synthesis | 8% |
| source phrases | 8% |
| gloss applicability and error profile | 8% |
| facets | 6% |
| definition | 4% |

**The v16 dictionary** (`dictionary.py`; same roots and order as v9). Per branch it keeps:

- the Turkish label;
- the per-sense Turkish glosses (`lexical_glosses`), which follow the source phrases sense by sense. The definition
  merges senses and adds verdicts: on ق و م B012 it buries the pulley among a sword hilt and a bed leg and ends on
  "tartışmalıdır";
- `[kalıp]` for collocation-bound branches, 15% of all branches. Their scope notes are formulaic negatives
  ("…yalın köke genellenmez"), and the source phrases already show the construction;
- the source phrases whole.

It drops everything else, including the root summary. It is 47% smaller than v9's clipped file (1:6: 32.4k → 17.0k
characters) and 51% smaller than v9 without clipping.

**Arms added:**

- **D:** the E1 base with the v16 dictionary and nothing else. Does the whole evidence alone bring the pulley back?
- **VD:** V with the v16 dictionary.

## The surah step (built 2026-09-29, not yet run)

**Why.** With the whole B012 line in hand, the 1:6 writer still left out the pulley. It sees the join; judged from
one ayah, a chain whose other members sit in other ayat does not earn a place. So the chains are settled once at
surah level, and every ayah call receives them.

**Surah call** (`v16.py surah --surah N [--run]`, brief `prompts/surah_map.md`, output
`out/sNNN/surah/map.md`). It reads:

- the surah text;
- the v16 surah dictionary (`dictionary.surah_section`): every root once, whole source phrases;
- the trimmed HFT of every ayah (`trim_hft`). It keeps the record name (class prefix and [label] removed), the
  changed reading, the mechanism, and trace steps as ayah, word, branch and contribution. It drops `before`,
  `containment`, the reader overview and the glosses the dictionary already carries. For S1: 196 KB → 108 KB;
- the whole channel review. The chains live there as well as in the HFT, and some (the well assembly) only there.

**What it writes.** A map in English, in two parts:

- `## Chains`: for each chain, its members as ayah, word, root and branch, and the dictionary's own phrase quoted
  exactly, plus Quran passages that stage it;
- `## Ayat`: which chains each ayah opens, advances or completes.

It carries no ranking, no strength labels and no must-include list. The brief names no known case (linted).

**Judgements.** At the user's instruction, every prompt that carries the HFT or the channel review (the surah call,
arm H) says they are earlier readers' proposals: ignore their judgements (grades, strength or confidence labels,
reading types, statements of what a reading may or may not do) and make your own.

**Arm DM.** D plus the surah map, described to the writer as a proposal, not an authority.

**Cost.** S1 surah call: about 119k tokens in, estimated $1.75. DM on 1:6: estimated $1.02 (actual $0.57).

**Provenance.** Every run now saves its exact prompt in `out/…/prompt.md`. The eight earlier runs were
backfilled from `work/`, and their character counts match the ledger.

## Rules

- One call per arm per ayah. No duplicates, no retries, no reruns: an existing `out/…/run.log.json` is never
  overwritten.
- A call starts only when its estimate is below $5, whatever it then costs.
- Every call is logged in `out/ledger.jsonl`.
- No run without the user's approval.

## Files

- `v16.py`: `build` writes `work/<S_A>/<arm>/prompt.md` and `packet.json` and prints sizes and estimates; `run`
  makes the calls (`--arm`, `--ayah`).
- `prompts/additions.md`: the three additions.
- `dictionary.py`: the v16 dictionary (arms D, VD and DM; `surah_section` for the surah call); run it with refs to compare sizes against v9.
- `prompts/surah_map.md`: the surah-call brief.
- `out/<S_A>/<arm>/`: the reading, `run.log.json` and `check.json`.

## Status

- 2026-09-29: packets built for the first test.
- 2026-09-29: first test run with approval. 6 of 6 calls ok, $4.79 in total, no reruns (`out/ledger.jsonl`).

  | ayah | arm | words | cost | thinking | refs | negation /1000 |
  |---|---|---|---|---|---|---|
  | 1:6 | E1 (reference) | 1,962 | – | – | 15 | 10.7 |
  | 1:6 | H | 1,684 | $0.92 | 18.7k | 22 | 10.7 |
  | 1:6 | V | 2,278 | $1.45 | 19.6k | 29 | 6.6 |
  | 100:1 | E1 | 1,567 | – | – | 21 | 7.7 |
  | 100:1 | H | 1,846 | $0.89 | 10.3k | 21 | 7.0 |
  | 100:1 | V | 1,556 | $0.47 | 5.6k | 20 | 6.4 |
  | 100:6 | E1 | 1,594 | – | – | 19 | 4.4 |
  | 100:6 | H | 1,473 | $0.55 | 4.8k | 15 | 8.8 |
  | 100:6 | V | 1,648 | $0.52 | 5.9k | 20 | 5.5 |

  "refs" counts distinct ayah references, S100's own included. `check.py`: every tag is sourced in all six, and
  there is no unmarked memory.

  **My reading, against E1 rep1 and the v9 arms:**

  - Every run is above the v9 dictionary arm, but most of that margin is E1's memory permission.
  - **Above E1:**
    - 1:6 H: the supported gait (yuhādā bayna-thnayn) becomes a thread tied to nastaʿīn.
    - 1:6 V:
      - hady as someone's gait, followed (6:90, 19:43);
      - the qāʾim dinar and the balance (26:182, 55:9), which frame 1:7's two sides;
      - 7:43 closes on 1:2.
    - 100:6 V: 16:83 ("know, then deny": the rope is cut after it was bound) and the four inne…la- verdicts
      as the surah's architecture.
  - **Level with E1:**
    - 100:1 H and V;
    - 100:6 H.
    - V's "what is inside comes out" thread on 100:1 (breath, flint, earth, graves, breasts) is the best
      integration in the set.
  - **Missing everywhere: the pulley.** It was in both 1:6 inputs (the channel subchannel "Well and
    Water-Lifting Assembly"; v5 macro's well apparatus) and was dropped both times. The rural blind spot
    persists in a single call.
  - The Ek Notlar valve works: leftovers go there instead of into hedged paragraphs. V has the lowest negation
    rate on all three ayat.
- 2026-09-29: arms D and VD on 1:6, run with approval: D $0.77 (23.5k thinking), VD $1.22 (12.1k thinking).

  **The pulley is still absent in both.** The whole B012 source line, including "النعامة الخشبة المعترضة ثم تعلق
  القامة", was in both prompts. The cut dictionary was therefore not the only cause.
  *Corrected after REVIEW.md:* D and VD had no ن ع م entry (1:6 roots only), so the join's other end was not in
  their input. D says of 1:6→1:7 "Bağ sözlükten değil". "The writer sees the join and does not use it" was wrong.
  Only the surah call had every member.

  **Otherwise:**

  - **D** (dictionary only, no findings, the cheapest input at about 20k tokens) is as strong as V:
    - the qāʾim dinar and "the day's balance stood";
    - the balance's two pans read into 1:7;
    - hady as the offering that reaches its place (2:196) and the bride conveyed;
    - 4:68 and 4:69 as fellow travellers;
    - 11:56's forelock with hādī as the neck.
  - **VD:**
    - a new thread of the guide ahead, the support at the side (yuhādā), then upright walking (67:22, 4:175);
    - 72:16 (istaqāmū → abundant water) in Ek Notlar: the Quran's own join of istiqāma and water, parked outside
      the threads.
- 2026-09-29: the S1 surah call and DM on 1:6, run with approval: surah $2.85 (70.8k output, 44.6k thinking),
  DM $0.57.

  **Failure: the map is incomplete.** The answer ran past the CLI's per-message output cap, so `claude -p` continued
  in a second turn, and `--output-format json` returned only that last message. `map.md` starts in the middle of
  chain 14. Chains 1–13 are lost, and no transcript survives because calls run without session persistence. The
  `## Ayat` part survived whole.

  **Fixed.** `call_opus` now reads `--output-format stream-json --verbose`, joins every assistant message in order,
  keeps the raw stream (`run.stream.jsonl`), sets `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`, and logs `joined_turns`.
  Tested on a synthetic two-turn stream; not yet on a real call.

  **The pulley: no well chain in the map.** The 1:6 entry of the surviving `## Ayat` part lists eleven chains: the
  road, being made known, two ways out of sight, the led mount, the lone traveller, worship, mainstay, the Day,
  journey's end, rearing, gathered and scattered. Water appears only as "weather" (cloud and rain) and "mainstay"
  («ملك أمر أي يقوم به الأمر»). The surah reader had the whole B012 line and the channel review's "Well and
  Water-Lifting Assembly", and still left the pulley out. Counting the E1 base, seven configurations have now
  declined it: E1, H, V, D, VD, the surah map, and DM.

  **DM, even on the partial map, brings in surah chains D lacked:**

  - in the threads: naʿbudu as the road worn smooth ("kulluk yolcuyu yola uysal kılar"), and «قوام الأمر ملاكه» tied
    to 1:4's mālik;
  - in the threads: 35:34 and 35:35 dār al-muqāma, the same root as müstaqīm, as the end of the road;
  - in Ek Notlar: «ملك الدابة قوائمها وهاديها» (1:4's root naming 1:6's two roots as the mount's legs and neck).
- 2026-09-29: independent read-only review, saved as `REVIEW.md`. Main points:
  - The pulley is a data and design gap for the ayah writers: the chain's members are not in their input, and the
    upstream chains abstract the pulley into "upright component".
  - For the surah call it is model judgement, eased by brief gaps: no rule against folding a mechanism into its
    function, and no record of what was not carried.
  - Five latent script bugs (S1–S5) and brief contradictions: memory (I1), a disclaimer per image (I2),
    verdict-carrying word notes (I7).
  - Fixes are not applied yet.

## Brief r2 and script fixes (2026-09-29, after REVIEW.md; no model run)

**Two briefs.**

- **r1** is every run so far. Every r1 packet (H, V, D, VD, the surah call) still rebuilds byte for byte against
  the prompt it ran with, in `out/…/prompt.md`.
- **r2** is the revision. Its outputs go to `out/<S_A>/<arm>.r2/` and `out/sNNN/surah.r2/`.
  - Arms: H, V, D, DM, all on the v16 dictionary. VD is V under r2.

**Fixes**, keyed to REVIEW.md:

| id | fix | where |
|---|---|---|
| I1 | "Work from the supplied evidence and your own knowledge of Arabic and the Quran. Where a sense, phrase or passage comes from memory rather than from the supplied dictionary or text, say so briefly where you use it." | prompts/r2/write.md |
| I2 | The two "don't quietly translate" rules become one framing: "Family images are heard beside the word's meaning in this ayah, not in place of it. Make that clear once, where the first such image enters; afterwards let the images work without repeating the qualification." Glosses: "the ayah's word by its meaning here, a family image by that image." | write.md |
| I4 | "A finding that ties this ayah to another ayah or to a chain belongs in a thread, not here." | prompts/r2/additions.md |
| I5, I6 | Dropped "Use headings only when…", "concordance panels" and "Without a brief…". Supplied readings and maps are "proposals, not authorities". | write.md |
| I7 | context.md is built without its "## Word notes" section. | `clean_context` |
| I8 | The dictionary header no longer claims the glosses follow source-phrase order. | dictionary.py (r2 header) |
| I9 | The surah brief now says: "where their wording abstracts a member, go back to the dictionary phrase"; "keep a scene at the level of its objects, their parts and their operation; … do not fold one into another's more abstract function unless nothing concrete is lost"; "carry every chain that meets this test, however unusual". It ends with `## Not carried` (each subchannel and HFT record not carried, and why), and puts the channel review before the HFT. | prompts/r2/surah_map.md |
| I10 | "a well, a support" becomes "a concrete object, mechanism". | write.md |
| S1 | Packets are built in the main thread; only calls run in parallel. dictionary.py no longer patches v9. | v16.py, dictionary.py |
| S2 | Surah dictionary: a root is headed under its strongest role, with other roles listed. S18's ق ل ل is now identity. | dictionary.py |
| S3 | Anchors: ranges and bare continuation numbers are parsed; `### X` cross-pericope blocks are matched by their pericope spans. Empty section headings are dropped (r2). | v16.py |
| S4 | `started.json` is written before a call; a started or finished call blocks any other. | v16.py |
| S5, S6 | A stream without a result event keeps its text as `partial`; assistant message ids are logged (`text_messages`). | v16.py |
| S7 | DM refuses a map without `## Chains` and `## Ayat`. | v16.py |
| S8 | The estimate adds re-caching per 64k of output; the surah call assumes 80k output. S1 surah: $3.51. | v16.py |
| S9 | The HFT root-map note is kept (r2). | v16.py |
| S10 | r2 file names match the evidence clause (write.md, map.md). The ledger records the brief, prompt sha256 and CLI version. | v16.py |

**Not changed.** I3 ("most candidates … stay out") is kept on purpose: it is the adversarial audit's own
anti-catalogue rule.

**Tests.** Without model calls: r1 rebuilds identical; the r2 lint is clean. Anchor parsing was checked on six
real formats. The partial-stream path, the started-call guard and X-block slicing (7:150) were each tested.

## r2 test: the S1 surah call (repair) and DM on 1:6 (2026-09-29, with approval)

| call | cost | output | thinking | result |
|---|---|---|---|---|
| S1 surah r2 | $4.24 (est. $3.51) | 121.8k | 94.8k | complete map, 9,960 words: 19 chains, `## Ayat`, `## Not carried` |
| DM r2, 1:6 | $0.76 (est. $1.19) | 21.7k | 10.7k | 2,337 words |

The first DM attempt was skipped by the map check. The map opens with a "# Map…" title before `## Chains`, and the
check wanted `## Chains` first. The check was relaxed (it now finds both headings anywhere), a note row was logged,
and DM ran.

**The map carries the pulley.**

- Chain 9 is "The well and its rig: the crossbeam, the pulley hung from it, the brimming well, the water that keeps
  the camp". It quotes the dictionary's join «النعامة الخشبة المعترضة ثم تعلق القامة». Its members are 1:7 ن ع م
  B007, 1:6 ق و م B012, 1:2 ع ل م B005 and 1:4 م ل ك B007.
- The 1:6 entry of `## Ayat` lists 14 chains, including "Advances 9: the pulley hung from the beam".
- `## Not carried` gives a reason for every subchannel and HFT record left out, and catches HFT errors: senses
  credited to س م و that belong to و س م.

**DM r2 still does not use the pulley.** The writer had the map, with the pulley under 1:6, and developed about
eight of the 14 chains:

- the guide ahead;
- the trodden road, ṭarīq muʿabbad (from the root of naʿbudu);
- walking held between two (tahādā, with the hadith);
- standing, from qawma to qiyāma (83:6 → 1:2);
- the coin that does not tip and the day's balance, read into 1:7's two sides;
- the four conveyances (offering, bride, gift, the one who seeks refuge), with 5:97 "qiyāman li-n-nās", where the
  Kaʿba, hady and ق و م meet;
- the stray camel whose owner (rabb) is unknown, joined to 1:2;
- the eye that stands but does not see (22:46);
- two ways out of sight: swallowed by the road, dissolved into the ground.

Chain 9 (the well), 10 (settling), 12 (fitting out), 14 (price) and 18 (the gathered) stay out.

**My reading.** DM r2 is the strongest 1:6 reading so far: the most surah chains woven into the threads, the fewest
disclaimers, and memory marked. The r2 brief fixes show:

- negation 3.85 per 1,000 words (D 8.7, DM r1 8.9);
- six "hafızadan" marks;
- three Ek Notlar items (DM r1 had six).

`check.py` counts three quotations as "unsourced unmarked". Two are hadith marked "(hafızadan, Buhârî)"; the checker
recognises only [bellek]. One is a compressed dictionary phrase.

**Conclusion on the pulley.** Data and assembly now deliver it to the ayah writer as a surah finding with its
dictionary join. The writer ranks it below the other 13 chains for 1:6. The pulley is a chain across four ayat that
belongs to the surah; the ayah reading chooses. It would appear naturally in a surah-level commentary (the layer
the North Star calls the surah argument), which reads the map as a whole.

**DM r2 on 1:7** ($0.80, 14.7k thinking, 2,023 words). The map says 1:7 completes chain 9 with the naʿāma
crossbeam. The writer does not take it up. From the map it uses:

- the naʿam herd against the stray camel "lā yuʿrafu rabbuhā", which returns 1:2's rabb (chain 2);
- nuʿāmā, the moist south wind (chain 8);
- ghayr as rain that sets things right and as "ḥaṭṭa ʿanhu raḥlahu" (chains 8 and 10);
- anʿamtu arḍan, "the land suited me and I stayed" (chain 10);
- the ghaḍba rock (chain 16);
- two ways out of sight (chain 17).

Its own find is 8:53, "lam yaku mughayyiran niʿmatan anʿamahā ʿalā qawmin ḥattā yughayyirū": niʿma, anʿama,
ʿalā and the ghayr root in one sentence. It reads غَيْرِ as the boundary crossed by a change from within. Memory
is marked throughout.

**Across both ayat.** The well chain reaches both writers from the map, and both rank other chains higher. This
is now a stable judgement of the ayah writer, not missing data.

## 29:38, the watch case (2026-09-29, with approval)

The DM path needs a surah map, and S29 has 69 ayat with HFT for only four of them. So only the two arms that need
no map ran:

| arm | cost | words | refs | neg/1000 | eye film (sebel) | notes |
|---|---|---|---|---|---|---|
| D r2 (dictionary only) | $0.88 | 2,689 | 36 | 3.35 | **no**, though its dictionary carries «داء في العين شبه غشاوة كأنها نسج العنكبوت» | 29:41, shaṭana as a well-rope and turning from one's heading, ṣadd as the blocking mountain wall joined to Thamūd's carved houses, 27:24's twin sentence, 17:59 mubṣira, 14:45, 7:201 |
| H r2 (+ HFT, channel subchannels) | $0.99 | 2,525 | 34 | 2.38 | **yes**: sebel's film "like spider's weave" set beside 29:41 "evlerin en çürüğü"; the section closes on "gözün üstüne gerilmiş ince bir ağ" | ʿamal → ṭarīq muʿmal (the trodden road of their own works), ʿĀd → ʿādī (old roads), 27:24 vs "kānū mustabṣirīn", 17:59 and 41:17, 16:63, three tafsir readings of mustabṣirīn kept together, ʿaql/ʿiqāl marked as memory |

**Against the v9 pilot** (4,011 words, the user's "great / excellent"). H covers the pilot's movements:

- two ways of appearing (tabayyana / zayyana);
- the veiled eye;
- their own trodden road;
- dwellings that could not keep them standing;
- "they were seeing";
- the ʿĀd name.

It lacks the pilot's kohl (the pilot's eye section is "Sürmelenmiş ve Perdelenmiş Göz"), and it gives the eye film
one paragraph where the pilot gives a section.

**The eye film is activated by a neighbour.** It came from the assembled chains (HFT), not from the dictionary
alone. That supports reading HFT and channels in the surah or pericope map. A pericope map for long surahs is not
built yet.

## Brief r3 (2026-09-29, user feedback; built, not run)

The user read DM r2 (1:6, 1:7) and H r2 (29:38):

- "hafızadan aktarıyorum" and "bildiğim kadarıyla" do not belong in reader prose;
- the prose should be cinematic (a filmmaker's perspective) with hooks, and is too dry now;
- 1:6 reads like a catalogue, not a synthesis;
- a very basic ledger of what was not written, and why, is enough;
- otherwise everything is good.

**r3** (`prompts/r3/write.md`, `prompts/r3/additions.md`; DM reads the r2 S1 map):

- **Filmmaker's eye.** Open on a concrete moment; move from wide shot to close-up and back; cut between scenes the
  words connect; open each section with a hook; end it on an image that carries forward. The drama comes only from
  the evidence. A dictionary phrase enters as something seen or heard in the scene, not as "sözlükler şöyle der".
- **Scenes, not words.** Each section is a scene where several of the ayah's words act together, never one section
  per word or root. One controlling question or image opens the reading and returns at its end. From the map,
  choose the few chains that make this ayah's scene; the rest go to the ledger. A chain an earlier ayah opened is
  recalled in a sentence and not explained again.
- **No source talk in the prose.** Memory is written plainly in the prose and listed in the ledger (the North Star's
  "marked, never silently used" is kept in the ledger).
- **Turkish loss.** Where a key word lives in Turkish as a narrowed or shifted loanword, the reader feels what the
  Turkish word no longer carries, once.
- **No Ek Notlar.** The output ends with `=== LEDGER ===`, then `- memory: …` and `- not written: … - why` lines.
  `run_one` splits this into `ledger.md`.

**Checks.** r1 and r2 packets rebuild identical. The r3 briefs name no known case. The ledger split was tested on a
synthetic output.

## r3 test (2026-09-29, with approval): 1:6 DM, 1:7 DM, 29:38 H; $2.80

| reading | words | sections | branches quoted | refs outside the surah | neg/1000 | source talk |
|---|---|---|---|---|---|---|
| 1:6 r2 → r3 | 2,337 → 1,559 | 6 → 5 | 22 → 12 (r3 ⊂ r2) | 16 → 7 | 3.85 → 4.49 | 7 → 0 |
| 1:7 r2 → r3 | 2,023 → 1,427 | 5 → 5 | 21 → 13 (r3 ⊂ r2) | 14 → 4 | 4.45 → 4.20 | 14 → 0 |
| 29:38 r2 → r3 | 2,525 → 1,711 | 5 → 6 | 16 → 13 (10 shared) | 13 → 12 | 2.38 → 3.51 | 9 → 0 |

Word counts are prose only: the ledger is split off. "Source talk" counts hafıza, bildiğim and "sözlükler şöyle".

**Gains.**

- Every reading opens on a scene with a controlling question and returns to it at the end:
  - 1:6: the standing prayer row. Why does someone standing still ask for a road?
  - 1:7: the six-beat madd on ed-dâllîn, then "âmîn". What is a road known by?
  - 29:38: doors carved in rock on the caravan road. Is seeing enough to keep one on the road?
- Sections end on hooks.
- The Turkish-loss layer arrived: hidayete ermek, istikamet as mere direction, sırat as the bridge; nimet, dalâlet,
  gazap; mesken abonesi, sebil as a kiosk.
- New finds:
  - 1:6: 42:52 contrasted with the direct object;
  - 1:7: 20:81; a sound hook;
  - 29:38: the aṭlāl, 35:8, 46:26, 15:76, and basīra as the blood trail of wounded game.
- 29:38 keeps the eye film inside the spider-house scene.
- The ledgers work. They give reasons, including for the pulley ("one ayah cannot carry them"), and for dropping
  the ʿAdī b. Ḥātim Jews/Christians gloss ("would narrow the images into a label").

**Misses** (the cost of selecting fewer things on 1:6 and 1:7):

- 1:6 lost:
  - the trodden road ṭarīq muʿabbad (a North Star aha item);
  - 36:61 and 43:64, where worship itself is the straight road;
  - 41:30;
  - 37:23, the road to the fire;
  - 22:46, the blind eye;
  - the fixed dinar and noon balance, cut to one line.
- 1:7 lost:
  - 8:53 and 13:11, favour changed only when a people change within: the best find of r2;
  - 2:40 and 2:61, one people in both groups;
  - 2:90, wrath upon wrath;
  - ghayr as rain and as change;
  - anʿamtu arḍan.
- The rule against re-explaining held only partly: 1:7 retells the swallowing road and the sırat bridge.
- 29:38 dropped ʿamal as a trodden road (the ledger calls it "too thin") and 14:45; otherwise it is equal to r2.

**Against v5's S1** (the middle and editorial layers of 1:6 and 1:7).

- v5's breadth is far larger:
  - 60 and 72 Quran passages outside the surah, against 7 and 4 in r3 and 16 and 14 in r2;
  - chains v16's ayah readings do not carry: waymarks (ʿālamīn), the well and crossbeam apparatus, and water in 1:6
    and 1:7.
- v16 quotes far more early-source Arabic (12–13 branches per reading against v5's 2–5), integrates instead of
  cataloguing (v5 1:6 middle: 31 "değildir / anlamına gelmez / söylemez"), and stays at 1,400–2,300 words against
  4,861 to 11,249.
- 7:16 (Iblīs sitting on the straight road) is in 1:6 r2, r3 and v5 (v5 by reference only). It is in no 1:7.

## 1:5 DM r3, Opus 5.5 against Fable 5.1 (2026-09-29, with approval)

`v16.py --model fable` was added. Fable writes to `<arm>.<brief>.fable/`; the estimate uses Fable rates (cache write
$20/M, output $50/M). Both runs had an identical prompt.

| | Opus 5.5 | Fable 5.1 |
|---|---|---|
| cost | $0.75 | $1.20 |
| output / thinking tokens | 22.5k / 16.4k | 9.0k / 4.0k |
| time | 236 s | 131 s |
| prose words (check.py) | 1,184 | 899 |
| sourced tags | 94% (2 unmarked) | 100% |
| neg/1000 | 2.53 | 1.11 |
| refs outside S1 | 5:2, 6:153, 16:75, 26:22 | 7:128, 16:75, 23:47, 26:22, 36:71, 36:72 |
| dictionary authors named in the prose | 8 | 0 |

**Shared, from the map.** Both readings carry:

- the turned face (from speaking about Him to speaking to Him);
- ʿabd as the owned one against 1:2's rabb and 1:4's mālik;
- ibadet narrowed in Turkish to ritual;
- ṭarīq muʿabbad, the road smoothed by many feet (the trodden road 1:6 r3 lost);
- the tarred camel;
- 26:22, Pharaoh's enslaving;
- uʿbida bihi, the traveller whose mount gave out;
- ʿawn as a back under the load;
- taʿāwun against ʿabādīd (scattering along diverging roads);
- the hadith qudsi on the prayer divided in two;
- closing on 1:6.

**Opus only.** 5:2, "cooperate", set against "yalnız"; 6:153, the scattering roads.

**Fable only.**

- 23:47 "wa-qawmuhumā lanā ʿābidūn": Pharaoh's court fronts "lanā" just as the ayah fronts iyyāka, so "yalnız sana"
  becomes a refusal of every other claimed owner.
- 7:128 "istaʿīnū bi-llāhi wa-ṣbirū": Moses gives the enslaved people the ayah's second verb.
- 36:71 and 36:72, "mālikūn" and "dhallalnāhā": ownership and being made tractable, tied to the tarred camel and
  to 1:4. The camel is tarred against mange, so being owned and being cared for meet in one hide.
- muavin as the Turkish trace of ʿawn.
- The ayah as the surah's hinge.
- Tighter and plainer, with no author names in the prose.

**My reading.** Fable writes the stronger 1:5: sharper cross-passage joins and cleaner prose, on a quarter of Opus's
thinking, at 1.6× the cost. One ayah is not a verdict.

## Brief r4: discovery and coherent development (2026-09-29)

The user identified two remaining deviations from v9: the writer is cast as an accountant of supplied findings,
and "choose the few" preselects how much can enter. The agreed criterion is that everything coherent contributes:
major themes carry the reading, and other findings expand, build, complicate or connect those themes. A finding
stays outside only after exploring whether it can contribute, or because its evidence fails.

`prompts/r4/write.md` and `additions.md` restore the writer's discovery responsibility. Connected readings come
before the outline or controlling question. Consequential findings can enlarge or reshape a theme, or establish
another major theme. There is no target number, omission proportion or length limit. Supporting findings receive
the development their contribution needs. The cinematic treatment, Turkish-loss layer, source accuracy rules
and separate memory/omissions ledger remain. Omissions must explain why a finding could not contribute, rather
than appealing to length or the initial scene. r4 is the default ayah brief; r1-r3 remain unchanged.

**Authorized trial:** DM r4 on 1:5 and 1:6, each one `gpt-6-astra` call at max reasoning effort through the Codex
subscription. `run_astra.py` is build-only unless passed `--run`; it preserves an exclusive started marker, exact
prompt, command, raw stream, response, usage and split prose/ledger. Outputs are in `out/<S_A>/DM.r4.astra/`.
The CLI does not report USD cost, so these subscription runs record null cost and estimate rather than borrowing
Opus prices. The existing under-$5 estimated-cost gate remains in the Claude runner.

**Evidence control:** the local upstream checkout lacks v9's root-resolution gateway. These runs use the exact
evidence in the saved DM r3 prompts, including the r2 S1 map, and replace only the two writing briefs. The builder
asserts byte-identical evidence and saves source/prompt/evidence hashes in `work/<S_A>/DM.r4/packet.json`. No earlier
reading, result, assessment, known-case list or this design document is supplied to the writer. This comparison
changes both brief and model; it cannot isolate the effect of either.

Command (requires NumPy, as does the existing v16 packet module):

```sh
python3 -B _commentary/v16/run_astra.py --ayah 1:5 --ayah 1:6 --run
```

Status: all four calls completed; results and checks below.

**Effort preference (user, while these calls were running):** future Astra runs use **high**, now the default in
`run_astra.py`. The user explicitly asked to let the current two max-effort calls continue unchanged. Their command
and started records preserve `max`; `--effort max` can reproduce that setting only when explicitly requested.

**Additional trial authorized by the user:** run 1:5 and 1:6 at high effort in parallel while both max runs
continue. High outputs use `out/<S_A>/DM.r4.astra.high/`; max keeps `DM.r4.astra/`. Both read the identical r4
prompt. Output paths include effort, and exclusive started markers prevent overwriting or duplicate calls.

### r4 results: Astra max and high

| ayah | effort | prose words | elapsed | output tokens | reasoning tokens |
|---|---|---:|---|---:|---:|
| 1:5 | max | 2,449 | 15m 12s | 30,206 | 24,008 |
| 1:6 | max | 2,951 | 16m 59s | 33,745 | 26,223 |
| 1:5 | high | 2,215 | 4m 55s | 9,494 | 3,742 |
| 1:6 | high | 3,071 | 6m 51s | 13,452 | 5,600 |

All four completed in one call each, with separate ledgers and no tool use. Each high/max pair has an identical
prompt hash. Earlier runs and the raw new responses are preserved. Output tokens include reasoning; word counts
are whitespace counts of prose including the Arabic reader tags, matching the runner's convention.

**Reading observations.** All four develop the well and pulley within larger themes. On 1:5 the apparatus makes
shared help concrete; high extends this through Moses helping at the watering place while remaining in need
(28:23–26). On 1:6 the well develops the relation between guidance, support and a functioning structure; high
connects Moses's request for guidance (28:22) to water, assistance, reception and the household that follows.
Both 1:6 readings develop the balance, value/compensation, disappearance and final dwelling as further aspects
of the journey rather than excluding them because an initial road scene cannot carry them. The ledgers explain
remaining omissions by evidence or lack of an additional consequence. These are observations, not a user quality
verdict or a controlled estimate of the brief's effect. The high/max pair controls the prompt, but is one sample
per setting, with no replicates.

**Validation.** Python syntax, unchanged r1-r3 prompts, frozen evidence, identical paired prompts, exclusive-run
guards, response/prose identity and `git diff --check` passed. All four pass `v5/validate_prose.py`; `v9/verify_ar.py`
finds 8, 10, 9 and 13 exact Arabic quotations respectively, with no missing, fixable or wrong-ayah tags. These are
quotation and formatting checks, not validation of every interpretation or paraphrase.

The comprehensive legacy `review/e0/checks/check.py` cannot run on this machine: it uses unavailable absolute
`/Volumes/OZTURK/_projects/...` paths. Each run preserves its failure in `check.error.log`, with this limitation
recorded in `validation.json`. No claim of full source-check success is made.

**Manual reference flag:** high 1:6, the opening paragraph under "Yolun sonunda ayağa kalkmak", describes taking
full measure and giving short measure but cites 83:1. Those details are in 83:2 and 83:3. The flag is saved in
that run's `validation.json`; the raw generated reading has not been edited. Ledger references to the same
paraphrase share that citation issue.

## Brief r5: make contributing passages intelligible (2026-09-29)

The user approved one additive paragraph, preserving r4's discovery and synthesis behavior:

> When another Quranic passage contributes to the reading, assume the reader does
> not know it. Introduce the speaker or actor, the relevant situation, and the
> wording needed to understand the connection, within the developing prose.
> Preserve any concrete verbal detail that does interpretive work.

This is the only change in `prompts/r5/write.md`; `additions.md` is byte-identical to r4.
No case-specific example, consolidation pass, selection quota or additional writer stage is introduced.
r4 remains the default; the trial selects r5 explicitly.

**Authorized trial:** Astra high on 1:5 and 1:6 (DM), and 29:38 (H), running concurrently.
The saved r3 evidence is unchanged in all three packets; the DM evidence hashes also match r4.
Outputs use `out/1_5/DM.r5.astra.high/`, `out/1_6/DM.r5.astra.high/` and
`out/29_38/H.r5.astra.high/`, preserving every earlier run. The writers receive no previous prose or assessment.

```sh
python3 -B _commentary/v16/run_astra.py --brief r5 --arm DM --ayah 1:5 --ayah 1:6 --effort high --run
python3 -B _commentary/v16/run_astra.py --brief r5 --arm H --ayah 29:38 --effort high --run
```

All three Astra high calls completed successfully, with separate ledgers and no tool use:

| ayah | arm | prose words | elapsed | output tokens | reasoning tokens |
|---|---|---:|---|---:|---:|
| 1:5 | DM | 1,911 | 6m 50s | 13,485 | 8,406 |
| 1:6 | DM | 3,025 | 7m 5s | 13,976 | 6,024 |
| 29:38 | H | 3,053 | 6m 14s | 12,295 | 4,660 |

All pass the prose-format check and Arabic-quotation check (13, 9 and 9 exact tags respectively;
no missing, fixable or wrong-ayah tags). Raw responses are preserved and match the split prose.
The comprehensive legacy source check remains blocked by the unavailable absolute source path,
as in r4; `validation.json` records that limitation. Quotation checks do not validate every interpretation.
The same Sol 5.6 reviewer has been asked to compare these readings with the previous prose using
only the North Star and prose files, with the same rubric.

**Additional authorized trial:** 1:5 with `gpt-6.1-sol` at max effort, using the byte-identical r5 DM
prompt supplied to Astra high. `run_astra.py --model` supports this model while retaining the existing
Astra default and historical output paths. The new output is isolated in
`out/1_5/DM.r5.gpt-6.1-sol.max/`.

```sh
python3 -B _commentary/v16/run_astra.py --brief r5 --arm DM --ayah 1:5 --model gpt-6.1-sol --effort max --run
```

The two GPT-6.1 Sol calls on 1:5 (r5 DM, high and max) and one on 29:38 (r3 H, high) completed:

| ayah | brief | effort | prose words | elapsed | output tokens | reasoning tokens | format check |
|---|---|---|---:|---|---:|---:|---|
| 1:5 | r5 DM | high | 2,537 | 12m 49s | 17,400 | 10,876 | ok; 9 exact tags |
| 1:5 | r5 DM | max | 3,134 | 28m 41s | 35,832 | 27,861 | error: malformed tag, line 51 (المعبدة السفينة المقيرة outside the tag) |
| 29:38 | r3 H | high | 892 | 4m 55s | 7,690 | 5,178 | ok; 9 exact tags |

29:38 Sol keeps the eye film (sebel) beside the spider's house (29:41).

## Brief r6: a commentator, not a storyteller (2026-09-30)

**User's read of the r5 prose (Astra and Sol):** close to the North Star in substance, but the style is too
fictional.

**My diagnosis** (agreed by the user). The cause is r3's filmmaker's-eye paragraph, which GPT follows more
literally than Opus did:

- Sections open on a present-tense tableau with no speaker, not on the ayah: 7 of 8 sections in 1:6 Astra r5
  ("Asa, onu tutan kişinin önündedir." "Kuyu suyla doludur."), 6 of 8 in 1:5 Sol max.
- "Let a dictionary phrase enter as something seen or heard in the scene" plus the ban on source talk hides
  provenance. An attested sense (uʿbida bihi) reads as narration ("Bir yolcu, bineği yorulduğu için yolda kalır").
- "End a section on an image that carries into the next" gives aphoristic closers ("Duvar hâlâ duvardır.").
- r4's "develop consequences" with no length limit turns themes into lessons: 1:6 into 4:5 and 6:151, 1:5 into
  Dhū al-Qarnayn's teamwork and 3:159.
- Under the film rule, r5's introduced passages become retold stories.
- "sahne" is 2.3–3.3 per 1,000 words in GPT r5, 0–0.8 in Opus r3. Opus r3 had the same paragraph, but anchored its
  openings in the real act of recitation and named the source in the next sentence.

**r6** (`prompts/r6/`) keeps r4's discovery and r5's grounding paragraph. It changes only the style passages:

- The filmmaker paragraph is replaced by a commentator's register:
  - vividness from exact material detail, never from staging;
  - each section opens on the ayah's words or a Quran passage;
  - no present-tense tableaux of unnamed people, animals, objects or places;
  - no attested sense narrated as an event;
  - a family image is attributed to its word in the sentence where it enters, and only then developed;
  - a passage is introduced as far as the connection needs, not retold;
  - no aphoristic section endings;
  - no lesson beyond what the ayah or passage draws.
- "Each section as a scene" becomes "around a thesis", in write.md and additions.md.
- "Inside the scene" becomes "in the sentence where it enters".
- The final check asks whether the reader can always tell the ayah, a family image, another passage and the
  writer's inference apart.

No word or section caps. The brief names no known case.

**Cleanup (user-approved, 2026-09-30).** An audit of the draft found four conflicts:

- additions.md asked for "the Fatiha" in every section while write.md forbade a formulaic Fatiha paragraph; 29:38
  Astra r5 closes on a 1:6/1:5 section.
- Two opening rules. The leftover "opening image returns at the end" rule produced bookend closings.
- "Develop their consequences" was undefined, and GPT read it as lessons.
- "Avoid 'sözlükler şöyle der'" can be read against attribution.

It also found rules repeated 3–5 times: the revisable outline, chains as proposals, not a catalogue, provenance,
introducing passages, no invention.

**Fixes in r6:**

- the Fatiha only where it connects;
- one opening rule (the ayah's words, a passage, or an attested detail named as such);
- a controlling question may return at the end, but no bookended image;
- consequence means "for how the ayah is read";
- images are attributed to the word's family, not to "the dictionaries";
- each rule is said once;
- additions.md is folded into write.md and now reads "No additions: write.md is the whole brief." The runner's
  two-file structure is unchanged.

Content and discovery rules are unchanged. r5's two files total 1,408 words; r6 has 1,137 (−19%).

**Built, not run.** `run_astra.py --brief r6` built `work/{1_5,1_6}/DM.r6/` and `work/29_38/H.r6/` from the frozen r3
evidence. The evidence hashes match r5, and the prompts differ from r5 only in the two briefs. A trial needs the
user's approval.

**r6 trial, 1:5 DM, gpt-6.1-sol high (2026-09-30, user-approved): failed, no output.** The call was rejected before
generation: "The 'gpt-6.1-sol' model is not supported when using Codex with a ChatGPT account." This machine has
codex-cli 0.159.0; the ten earlier Astra and Sol runs used 0.159.1. Not retried (no-rerun rule). The started
marker in `out/1_5/DM.r6.gpt-6.1-sol.high/` blocks another call until the user decides.

**r6 trial, 1:5 DM, Opus 5.5 high (2026-09-30, user-approved; from now on Opus only unless the user says
otherwise).** $1.23 (estimate $1.16), 46.5k output, 33.4k thinking, 467 s, 2,489 prose words, 6 sections.
Same frozen evidence as Opus r3 and Fable r3.

- `check.py` runs on this machine: 83 tags, 95% sourced. The four unsourced tags are the constructed form
  na'buduke, the hadith twice (memory, listed in the ledger) and 26:22 in non-Uthmani spelling.
- 21 refs outside S1 (Opus r3 4, Fable r3 6, Sol r5 high 37).
- New and on-axis:
  - 3:64: "do not take one another as rabbs";
  - 4:172: istinkāf from being ʿabd;
  - 19:93: all come to ar-Raḥmān as ʿabd;
  - 3:51, 19:36 and 43:64: "worship Him; this is a straight path", the 1:5→1:6 hinge;
  - 12:18: Allāhu l-mustaʿān;
  - 2:45: help sought through prayer;
  - 40:60: asking and "yastakbirūna ʿan ʿibādatī", which explains the second iyyāka;
  - the dictionary join of dīn: «دانه دينا أي أذله واستعبده» (1:4→1:5);
  - mutaʿabbid, the resisting camel, and ʿabad (wounded pride) as a tension inside the root.
- Style: opens on the ayah, no staged tableaux ("sahne" once), commentator register.
- Weaknesses:
  - two list blocks (a bullet list of 1:1–1:4 roots, a numbered 36:60–62);
  - a closing recap paragraph;
  - one containment sentence reads as meta.
- Sol's 43:12–14, 36:74–75, 18:95 and 39:29 are absent. The well and pulley are declined in the ledger ("chains
  that do not run through 1:5's words"), and 2:68 ʿawān is declined as forced.

## Brief r7: a minimal core for Opus (2026-09-30, drafted; not run)

**Why.** The user's best synthesis came from cold Opus with minimal instructions, and r6 on Opus showed that the
long craft section is not needed. `prompts/r7/write.md` is 425 words against r6's 1,130. It keeps:

- the task and reader;
- the evidence framing (maps are proposals; "not a catalogue"; no length limit);
- the guards:
  - a family image beside the meaning, not in its place, with its provenance;
  - identity, family and analogy kept distinct, and echo roots are not identity;
  - a mechanism explained by its work, not flattened into a label;
  - no invention;
  - the Turkish loss, once;
  - other passages introduced for a reader who does not know them;
  - no source talk, memory to the ledger;
- one form line (continuous prose in `##` sections; explain, do not dramatize; no lists, no closing recap);
- format and ledger.

It drops the discovery and theme methodology, openings and closings, the controlling question, the self-check,
and the Fatiha and chronology rules (chronology is folded into "never invent"). `additions.md` is a one-line
stub. Frozen evidence as r6 (hashes match); 1:5 DM r7 prompt 70,551 characters, Opus estimate $1.15.

**r6 on Fable 5.1, 1:5 DM (user-approved reference point):** estimate $2.90, running.

## 1:5 DM: r6 and r7 × Opus 5.5 and Fable 5.1 (2026-09-30, user-approved; identical frozen evidence)

| | cost | thinking | words (check.py) | tags (sourced) | Quran refs outside S1 | dictionary authors named | first-person hedges |
|---|---:|---:|---:|---:|---:|---:|---:|
| Opus r6 | $1.23 | 33.4k | 2,489 | 83 (95%) | 21 | 0 | ~3 |
| Fable r6 | $1.61 | 7.7k | 1,770 | 46 (98%) | 11 | 8 | ~2 |
| Opus r7 | $0.76 | 13.7k | 1,843 | 42 (98%) | 7 | 29 | ~9 |
| Fable r7 | $1.93 | 11.0k | 2,647 | 52 (100%) | 17 | 12 | ~11 |

The last two columns are rough regex counts.

**Brief.**

- r7 brought back source talk in both models: dictionary authors named in the prose, and first-person hedges ("bu
  bağı ben kuruyorum, sözlük değil"). The "beside, not instead" disclaimer repeats.
- Fable r7 organises by root ("Kul olmak: na'budu", "Sırtını vermek: nesteîn"), which r6 forbids.
- r6's attribution, register and structure rules therefore do work, for both models.
- Discovery split by model:
  - Opus fell from 21 refs to 7 under r7, with thinking cut from 33k to 14k;
  - Fable rose from 11 to 17.

**Model.**

- Fable finds the sharpest joins:
  - r6: 28:17 against 25:55 (ẓahīr, beside anʿamta);
  - r7: 43:81 (the early reading of ʿābidīn as "disdainers", from the anafa branch), 67:15 (al-arḍa dhalūlan,
    the earth made tractable to walk on), 17:1 (bi-ʿabdihi at the highest honour, beside al-muʿabbad
    al-mukarram), 11:123 (uʿbudhu wa-tawakkal ʿalayh, the ayah's own order) and "avene" as a Turkish pejorative
    shift.
- Opus is more thorough and careful. Fable has one slip in each reading:
  - r6: "yürünmüş yol ile yürünecek yol aynı kökten", although ع ب د ≠ ص ر ط;
  - r7: "Rahman adı bir önceki ayette", but 1:3 is not 1:4.
- 7:16 (Iblīs on the straight path) is in the map's road chain, which includes 1:5's B005. None of the four uses
  it, and no ledger mentions it. Only Astra r4 max and Sol r5 max used it on 1:5.

**My reading.**

- Content: Fable r7 ≥ Opus r6 > Fable r6 > Opus r7.
- Style: Opus r6 > Fable r6 > the r7 readings.
- Neither brief is best for both models. Next: a middle brief (r8): r7's core plus r6's discovery paragraph, the
  attribution line (the word's family, not the dictionaries or their authors), thesis sections rather than one
  per word, and no first-person hedging.

## Why 7:16 stayed out of 1:5 (2026-09-30)

7:16 («لأقعدن لهم صراطك المستقيم», Iblīs sitting on the straight path) is in the S1 map's chain 1, and chain 1
includes 1:5's ع ب د B005. None of the four r6/r7 readings uses it, and no ledger mentions it. Run thinking is not
recorded (the stream's thinking blocks are empty), so the causes are inferred from the inputs and outputs.

1. **The map strips the passage to its road image.** 7:16 is the last of six bare lines in chain 1's Quran list,
   glossed "someone sitting in ambush on the road". The speaker is not named. Nothing records that the ambush
   follows a refusal to bow out of pride (7:11–7:12).
2. **The map never carries the pride branch.** ع ب د B008 (العبد الأنف والحمية, wounded pride) is in no chain.
   `## Not carried` covers only subchannels and HFT records, not dictionary branches, so the omission is silent.
   The writers found B008 in the dictionary themselves, but the map gave them no link from it to 7:16.
3. **Chain 1 belongs to 1:6.** `## Ayat` lists 1:6 as "Core of 1", and 1:5 only as "Advances 1: the road
   smoothed by treading". A 1:5 writer treats the rest of the chain as 1:6's material.
4. **Quran recall is anchored on the root.** Every passage the four writers attach to the pride pole shares
   ع ب د: 4:172, 40:60, 43:81, 19:93. Iblīs's refusal (2:34, 7:12, 38:74–76) shares no word with 1:5. The two
   GPT runs that did use 7:16 on 1:5 (Astra r4 max, Sol r5 max) reached it through the scene (7:12, "ana khayrun
   minhu"), not the root.
5. **The ledger records only what was considered,** so a passage never considered leaves no trace.

**Fixes.**

- **In r8, general, no case named:**
  - look for passages "that stage the same act, scene or stance without sharing a word";
  - "a chain that a neighbouring ayah opens or completes can still be heard here, where this ayah's words take
    part in it";
  - the ledger's "not written" includes "passages the map lists".
- **For the surah-map brief later:**
  - a Quran line should name the speaker and the situation;
  - `## Not carried` should also cover dictionary branches.

## Brief r8: the middle brief (2026-09-30, user-approved; running)

`prompts/r8/write.md`, 612 words. It is r7's core plus:

- r6's discovery paragraph, with the scene-level Quran search and the neighbouring-chain sentence above;
- attribution to the word's family, with no dictionary or lexicographer named in the prose;
- thesis sections, never one per word or root;
- no first-person hedging;
- the ledger covering map passages.

It names no known case. Frozen evidence as before (1:5 and 1:6 hashes match r5 and r6).

Runs in parallel, one call each: 1:5 and 1:6 × Opus 5.5 and Fable 5.1. Estimates: Opus $1.15 and $1.19, Fable
$2.88 and $2.96. All four completed.

### r8 results (2026-09-30)

| run | cost | thinking | words (check.py) | tags | Arabic outside tags | branches cited | Quran refs outside S1 | dictionary names |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1:5 Opus r8 | $0.87 | 18.3k | 2,150 | 25 | **18** (Quran in «») | 15 | 20 | 0 |
| 1:5 Fable r8 | $2.03 | 11.7k | 2,636 | 48 | 0 | **0** | 27 | 0 |
| 1:6 Opus r8 | $1.38 | 38.0k | 2,770 | 44 | 0 | 19 | 25 | 0 |
| 1:6 Fable r8 | $1.78 | 7.4k | 2,261 | 37 | 0 | 11 | 21 | 0 |

**7:16.**

- Both 1:6 readings use it: Opus with "Âdem'e secde etmeyi reddedip kovulan İblis", Fable with "yolun kenarında
  değil üstünde".
- The 1:5 readings still do not.
- The user's reading holds: 1:6 carries it (7:16 contains aṣ-ṣirāṭ al-mustaqīm verbatim), so its absence on 1:5
  is a division of material between ayat, not a loss.

**Pulley.** Both 1:6 r8 ledgers decline map chain 9:

- Opus: "a technical apparatus with no bearing on road, guidance or straightness";
- Fable: "yields no reading of the request for a road".

This is stable across Opus r2–r8 and Fable. It is a writer's judgement; the user decides whether the surah
commentary carries it.

**Brief effect (r7→r8, 1:5).**

- Refs: Opus 7→20, Fable 17→27.
- Dictionary and lexicographer names: 29/21→0.
- Thesis sections are restored. First-person hedging is rare ("aşağıda döneceğim", "diye çevirdiğim").
- The scene-level line brought in passages that share no word with the ayah:
  - Opus: 39:29, 67:15, 16:69 (dhululan read of the paths or of the bees);
  - Fable: 39:29, 12:39 (arbāb mutafarriqūn beside ʿabādīd), 17:23–24 (lā taʿbudū illā iyyāhu, then janāḥ
    adh-dhull), 5:54, 66:4 and 28:35 (the ẓahīr "back"), and 21:112 (Rabb, ar-Raḥmān, al-mustaʿān together).

**Faults.**

1. Opus 1:5 puts 18 Quran quotations in «» outside the reader tag. r8's shorter format paragraph lost r6's
   "every Arabic quotation … in the tag".
2. Fable 1:5 quotes no dictionary Arabic at all: every family image is given in Turkish only, so it is less
   checkable. It probably reads "names no dictionary" as "quote no dictionary".
3. Fable 1:5 gives 2:172 as addressed to the Children of Israel; it is addressed to the believers.
4. Fable 1:6 ends on a recap paragraph and has "Bu bir benzetmedir".

**1:6 against earlier readings.**

- Both r8 readings exceed Opus r2 and r3 in reach and integration.
- Opus: the direct double object against 6:161 and 37:118; 48:2 (guidance promised in the middle of victory);
  the three failures of standing (the spent mount, still water, the intact but blind eye) against istiqāma as
  uprightness in motion; 5:16's subul as-salām complicating 6:153.
- Fable: 28:22, 3:8, 2:2 as the answer to the request, 37:23 (the same verb and noun without the adjective),
  36:66 (eyes wiped out, racing to the road) with the blind man's staff, 6:161's dīnan qiyaman, and 3:101.
- Against Astra r5 (40 refs, with the pulley), r8 is narrower but exact and checkable (100% of tags sourced on
  1:6).

**Next brief fix (r8.1):**

- every Arabic quotation (Quran, hadith, dictionary phrase) goes in the reader tag;
- a family image enters with its own Arabic phrase, only the dictionary's name is omitted;
- end on what the reading established, not a summary.

## Why the pulley stays out: reconstructed follow-ups (2026-09-30, user-approved)

The v16 calls run without session persistence and their thinking is not recorded, so they cannot be resumed.
`followup.py` makes one new Opus call with the run's exact prompt, its own full response, and two questions:

1. why the pulley stayed out;
2. what instruction would have brought it in where it contributes.

The answers are post-hoc accounts by the same model on the same evidence, not replays. Outputs are in
`out/1_6/DM.{r8,r3}.followup-pulley/answer.md`. Cost $0.50 and $0.43.

**Opus 1:6 r8's own account:**

- It tested the image against the plain meaning, not beside it. It says "I simply never tried the image".
- It read the map's "rare or technical" as "peripheral".
- Its sections (road, walking, arrival, scale) had no room for a vertical apparatus.
- It skipped the brief's rule to explain a mechanism by its work first.
- It missed the dictionary's own join of qāma and naʿāma, and 28:22→28:23, where Moses asks for guidance and
  arrives at the water of Madyan; the map lists only 28:23.

**Opus 1:6 r3's own account:**

- The controlling image (road, guide, posture) excluded a fixed, vertical object. It never checked whether the
  pulley serves the same operation.
- It dismissed chain 9 together with five other chains under one reason, pushed by "choose the few".
- The map's "rare or technical", plus ayn's rejected variant, made the whole chain feel unsafe.
- It feared inventing a well scene.
- It read "Advances", not "Core", as permission to drop the chain.
- What it would now write: the qāma is an upright that exists to turn and draw, set against its own section on
  standing that freezes; it hangs from the beam of 1:7's favour; the water lifted keeps the affair standing (1:4).

**Folded into r9 (general, no case named):**

- explore a dictionary phrase that joins this ayah's root with another root of the surah;
- judge a chain member by the scene it makes with the others;
- exclusion is allowed only when the evidence fails, or after trying: for a mechanism, explain its work, then
  look for a neighbouring ayah, another root of the surah or a Quran scene that gives the work a place;
- rarity, technicality, a mismatch with the plain meaning, or not fitting the planned sections are not reasons;
- decide each finding on its own, with its own ledger line naming the failed evidence or what was tried.

With the four format and ending fixes, r9 is 761 words. Prompts are built for 1:5 and 1:6, evidence hashes match
r8, and Opus estimates are $1.15 and $1.19. Not run.

**For the surah-map brief (not yet revised):**

- no evaluative labels ("rare" describes frequency, not reliability);
- flag a doubtful source phrase by itself, so it does not taint the sound members of its chain;
- mark dictionary-joined links;
- give Quran lines their speaker and situation, and include the preceding ayah where it starts the scene (28:22
  before 28:23);
- give each ayah's entry the scene its chain members complete, not a bare fragment;
- add an interactions section;
- make `## Not carried` cover dictionary branches.

## r9 on 1:6, Opus 5.5 (2026-09-30, user-approved)

$1.74 (estimate $1.19; the CLI used 3 turns, 37.7k output, 17.9k thinking), 1,077 s. Same map and evidence as
r8, so any change from r8 comes from the writer brief.

| 1:6 | words (check.py) | tags | sourced | dictionary tags | branches | refs outside S1 | Arabic outside tags | "sözlük" in prose |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Opus r3 | 1,559 | 40 | 95% | 23 | 18 | 7 | 0 | 1 |
| Opus r8 | 2,770 | 44 | 100% | 16 | 19 | 25 | 0 | 0 |
| Opus r9 | 3,868 | 84 | 98.8% | 56 | 32 | 21 | 0 | 9 |

**Pulley: in the prose for the first time in an Opus reading.**

- The reading quotes the dictionary join «القامة البكرة التي يستقى بها الماء؛ النعامة الخشبة المعترضة ثم تعلق
  القامة» and explains the rig: posts, crossbeam, pulley, rope, water drawn up.
- It then reads it: the pulley cannot work without the beam it hangs from, as 1:7 hangs the straight road on
  "those You favoured"; "Doğruluk nimete asılıdır".
- It is one paragraph, framed "Bu bir benzetmedir". The water chain is not developed (1:2's brimming well, 1:4's
  water that keeps the affair standing).
- 28:22 is used for "the middle of the road", but 28:23 (arrival at the water of Madyan) is dismissed in a batch
  ledger line of 30 map-listed passages "whose members are not 1:6's words". That is inconsistent with using the
  pulley.

**Other gains over r8:**

- the root's sense of standing still: قامت دابته, قام الماء جمد, and 2:20 (the hypocrites in the storm "stand
  still" when it goes dark), against istiqāma as uprightness that keeps moving;
- the arrow's tip (هادي السهم) with the unbending shaft (رمح قويم), labelled an analogy;
- هدى هدي فلان with 6:90 ("follow their guidance");
- 47:17 (guidance increased for the guided);
- «ملك الدابة قوائمها وهاديها», 1:4's root naming 1:6's two roots as the mount's legs and neck;
- the ending: the surah opens with «هديته الطريق والبيت» and closes on those who «ضللت المسجد والدار».

**Lost from r8:** 48:2, 37:118, 6:161, 19:43, 11:56, 5:16.

**Ledger:** 27 "not written" lines against r8's 20, 8 of them stating what was tried. Map-listed passages are
still batched in one line.

**Faults:**

- "sözlük" appears 9 times ("Sözlük bunu şöyle açıklar"). r9 bans naming a dictionary but no longer bans the
  "sözlükler şöyle der" register that r6 banned.
- "Bu bir benzetmedir" appears twice.
- The last paragraph partly summarises.
- One unsourced tag: the hadith qudsi, listed as memory.

**Next writer-brief fix (r10, not drafted):**

- say the family's image, not what "the dictionary says";
- one ledger line per map-listed passage as well.

**Map brief draft** (`prompts/map_r3/surah_map.md`, not wired, not run). The r2 map brief itself asked for "Say
plainly when a member is a rare sense … and keep it", the source of chain 9's "All these senses are rare or
technical". The draft:

- keeps only [fixed expression], and bans rare, technical and marginal;
- flags a doubtful phrase by itself;
- marks [dictionary join];
- gives Quran passages their speaker, situation and opening ayah;
- adds `## Interactions`;
- makes `## Ayat` name each chain's whole scene and says opens, advances and completes describe position, not
  importance;
- extends `## Not carried` to dictionary branches.

## Brief r10: r7 plus themes first (2026-09-30; built, not run)

**Why.**

- r9 slid back toward a catalogue on 1:6. Inventory transitions ("aynı aile", "bir kolu", "ailesinde", "sözlük",
  "de vardır") were 10.6 per 1,000 words, against r8's 4.7. Paragraphs with 3+ tags: 14 of 35, against 2 of 46.
- Two r9 rules caused it: "try every finding before excluding" and "quote every family image". They made
  inclusion the easier choice.
- The user's principle is that themes are the focus, and words support, expand and grow them. The user asked to
  go back to the minimal brief and build on it rather than add rules.

**r10 = r7 (425 words) + the following, 623 words in all:**

1. A theme-first paragraph: grammar and situation first; then discovery (senses across roots, chains, passages
   sharing words or staging the same act, scene or stance, partial findings supporting each other); themes
   emerge from that, not from the familiar reading; a theme is what the words show, not a lesson; a word, image
   or passage enters where it grounds, expands, complicates or joins a theme; no family walked through for its
   own sake; rarity or another ayah's chain is no reason to omit an image that works for a theme.
2. Family images carry their Arabic phrase, and the prose speaks of the word's family, never of what
   dictionaries say. This fixes r7's author names, r8 Fable's missing Arabic and r9's "sözlük".
3. No first-person hedging (r7).
4. One theme per `##` section (r7 Fable's per-root sections).
5. Every Arabic quotation in the reader tag, never in quotation marks (r8 Opus 1:5).
6. The ledger reason reads "did no work for a theme".

Dropped from r8 and r9: the exclusion procedure, dictionary joins, ledger rules for map passages, and the ending
rule.

**Adversarial read.**

- Theme-first risks familiar themes, or lessons, decorated with words. It is countered by "not from the familiar
  reading" and "not a lesson drawn from them".
- r7's weak discovery on Opus (7 refs) is countered by the discovery sentence inside the theme paragraph.
- It names no known case.

The 1:6 prompt is built with the evidence hash unchanged. Opus estimate $1.19.

### r10 on 1:6, Opus 5.5 (2026-09-30, user-approved)

$1.30 (estimate $1.19), 48.6k output, 32.2k thinking, 497 s. Same map and evidence as r8 and r9.

| 1:6 Opus | words | sections | tags | sourced | dictionary tags | refs outside S1 | inventory transitions /1k | paragraphs with 3+ tags | "sözlük" | pulley |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| r8 | 2,770 | 6 | 44 | 100% | 16 | 25 | 4.7 | 2/46 | 0 | no |
| r9 | 3,868 | 6 | 84 | 98.8% | 56 | 21 | 10.6 | 14/35 | 9 | yes |
| r10 | 3,186 | 7 | 77 | 97.4% | 45 | 23 | **4.1** | 13/38 | 0 | no |

**Themes.** Each section carries one theme, and family images from different roots are joined inside it:

- **Kulluk edenlerin yol istemesi.** 36:61–62 and 3:51 equate worship with the straight road. 37:118 and 48:2
  show guidance still promised to prophets. The construction without ilā is contrasted with 17:9.
- **Önden giden.** The staff, the guide, horses' necks, the herd's front runners, 20:10, and هدى هدي فلان with
  6:90 and 19:43. The arrowhead leads, but reaches its mark only with an unbent shaft (رمح قويم), a join across
  two roots that is labelled as such.
- **Yere serili yolun ayakta durması.** Why a lying road is called "standing"; the walker's istiqāma; 67:22,
  11:112, 41:30, 83:6.
- **Donmayan, kaçmayan adım.** Standing-still failures of ق و م (the halted mount, frozen water, the eye that
  stands but does not see) against the routed man's flight in ه د ي (الهدي السكون). The guided step lies between
  the two, with 25:63 and يهادي بين اثنين. This is a genuine synthesis of two families into one theme.
- **Terazinin dili.** 17:35, the day's balance at noon, the dinar and القوام العدل. 1:7's two groups read as two
  deviations, with كل جائر عن القصد ضال. 7:16–17's four sides, and 6:153 with Ibn Masʿūd's line-drawing hadith:
  the balance's tongue resisting a pull from both sides.
- **Yolda dokunulmazlık, yolun sonunda kabul.** The hady, the garland, 5:2, the refuge-seeker, the bride
  received, the gift, and hidāya/hadiyya as luṭf. This answers 7:16: the road where one is ambushed is also a
  road on which the walker is inviolable. 5:97 joins the two roots.
- **İçine alan yol.** sarita as swallowing, the traveller shrinking from view, 37:23–24, the Turkish sırat
  köprüsü; closing on ḍalla as milk dissolving in water against the road that carries its traveller home.

**Pulley: out again.**

- The ledger groups ق و م B012 with the sword grip and bed legs: "would have been walking the family".
- Chain 9 is placed among chains that "belong to other ayat and did no work for this ayah's themes".
- Under themes first, an image enters only when a theme needs it. With the current map, no theme brings well and
  water to 1:6. This is now a map-side question (interactions), not a writer-brief one.

**Faults.**

- A corrupted tag: «وكاda الظل يعقل», with Latin letters inside the Arabic.
- A garbled transliteration: "süripa" for surita.
- Two unsourced tags: the Bukhari hadith (listed as memory) and the corrupted line.
- The ledger again batches passages and chains.

**Lost from r9:** 2:20 (qāmū in the dark), 47:17, 28:22, «ملك الدابة قوائمها وهاديها», 2:255.

## Step 0 of REVIEW_r7_r10.md (2026-09-30, user-approved; no model calls)

- **`scorecard.py`.** A fixed, mechanical scorecard. Columns: words; sections; paragraphs with 3+ tags; tags and
  share sourced; dictionary tags per 1k; sentences opening "Aile…"; "sözlük"; "denir"; refs outside the surah;
  Arabic outside tags; Latin letters inside `ar:`; unsourced; ledger "not written" lines; probes. The probes are
  1:5 Iblīs's refusal, 1:6 well/pulley, well water and 7:16, and 1:7 crossbeam. They are read as probes, never
  tuned for, and never named in briefs.
- **`scorecard.py --diff`.** A map-use diff: for each map chain with a member in the reading's ayah, which of
  this ayah's members were quoted (from check.json's cited branches), how many of other ayat's members were
  quoted, and which listed passages were used. This replaces writer-side accounting of the map.
- **`packets.py`.** Controlled packets:
  - `map`: the saved r2 map prompt with only the brief swapped (37 changed lines; text, dictionary, channels and
    HFT byte-identical);
  - `writer`: a saved writer prompt with the map section replaced by a new map with `## Not carried` stripped,
    optionally with the dictionary's branch labels dropped (`--no-labels`; per-sense glosses and phrases kept).
  - Test builds on the r2 map: 1:6 r10 prompt 76,438 → 66,680 characters stripped, 65,023 without labels.
- **`prompts/map3/surah_map.md`** (716 words; r2 is 585). It is r2 plus the reviewer's lines:
  - "a chain may join a sense and its reversal";
  - [fixed expression] as the only label, and a rejected source phrase flagged by itself;
  - Quran passages with speaker, situation and scene-opening ayah;
  - `## Interactions`;
  - `## Ayat` naming each chain's whole scene, without the ownership verbs;
  - Not carried one short line per item.
  - My earlier map_r3 draft was removed.
- **`prompts/r10_1/write.md`** (643 words). r10 with the reviewer's three replacements, and the GPT-only "not a
  lesson" line cut. Frozen prompts built for 1:5 and 1:6. The 1:5 r10 frozen prompt was built too, for step 2.

**Baseline scorecard** (current map):

| run | words | paras 3+ tags | dict tags /1k | Aile openings | sözlük | denir | refs | Arabic outside tags | Latin in ar | probes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1:5 r6 | 2,489 | 12/39 | 11.2 | 4 | 0 | 3 | 17 | 2 | 0 | Iblīs - |
| 1:5 r7 | 1,843 | 7/22 | 13.6 | 0 | 8 | 1 | 7 | 0 | 0 | Iblīs - |
| 1:5 r8 | 2,150 | 3/23 | 6.5 | 12 | 0 | 0 | 20 | 18 | 0 | Iblīs - |
| 1:6 r8 | 2,770 | 2/46 | 5.8 | 5 | 0 | 13 | 25 | 0 | 0 | pulley -, 7:16 Y |
| 1:6 r9 | 3,868 | 14/35 | 14.5 | 1 | 9 | 4 | 21 | 0 | 0 | pulley Y, 7:16 Y |
| 1:6 r10 | 3,186 | 13/38 | 14.1 | 15 | 0 | 4 | 23 | 0 | 1 | pulley -, 7:16 Y |

**Map-use diff for 1:6 r10:** chain 9's 1:6 member B012 is not used, 0/3 of its other members, and neither
28:23 nor 22:45. Chain 1's passages 16:9 and 16:16 are not used; 6:153, 20:10, 36:61 and 7:16 are.

**Step 1 cost.**

- The standard estimate for the map3 call is $3.51. It assumes 80k output.
- The r2 map measured 121.8k output ($4.24, +21%).
- At 122k output the formula gives $4.35. At 130k (three turns) it gives $5.46.
- The new brief adds Interactions and scene lines but shortens Not carried.
- Awaiting the user's decision.

## Step 1: the S1 map with the map3 brief, without HFT (2026-09-30, user-approved)

The user dropped HFT from this run to keep the cost under the gate; it can be re-added. `packets.py map --no-hft`
removes the hft.md section and adapts the HFT lines of the brief and header in the packet only. Estimate $2.79
(80k out; $4.39 at 130k out). Actual **$4.30**: 133.0k output, 104.8k thinking, 3 turns, 1,187 s, 10,059 words.
Output in `out/s001/surah.map3.nohft/map.md` (69.2k characters).

**Read before any writer call.**

- **Labels.** No "rare", "technical", "minor" or "marginal". `[fixed expression]` appears 13 times (31 in r2).
- **Quran lines** carry speaker, situation and scene-opening ayah, e.g. "6:153 … (scene opens 6:151 …)" and
  "28:21–24 — Mūsā fleeing alone toward Madyan … 28:22 «عسى ربي أن يهديني سواء السبيل»".
- **`## Interactions`** has 22 lines. Most are lexical joins (Road × Worship, Owner × Debt, Day × Debt 83:1–6,
  Womb × Owner × Worship 17:23–24, Standing × Led 5:97). Two bear on the well:
  - "Water × Standing: «الماء ملاك الأشياء» — water as mainstay";
  - "Road × Mount: 28:21–24".
  There is no Road × Water or Mount × Water line (the traveller's water).
- **`## Ayat`** gives whole scenes. 1:6's entry lists 12 chains, including "Water: قامة, the pulley. Scene:
  layered cloud … the full well with crossbeam and pulley, water that keeps the traveller, water lost in the
  desert". The r2 map had "the pulley hung from the beam".
- **Chains** (18):
  - merged: the well and rain into one "Water: … the well below"; the balance into "Debt, weight and
    blood-price";
  - new: "The worshipped one and the humbled worshipper", "The sky of worship: sun, crescent, zenith, sphere"
    (6:77 Ibrāhīm), "Favour completed and praise returned", "The days of Allah";
  - the ع ب د pride branch B008 is now carried, in "Soft and hard".
- **`## Not carried`** is 2.8k characters (9.8k in r2).

**Losses against the r2 map** (n=1: missing HFT or run variance, cannot say which):

- **7:16 is gone from the map entirely.** Iblīs is named nowhere, so the pride branch has no Iblīs scene.
- **The eye chain is gone.** «عين قائمة» is absent; r8, r9 and r10 all used it.
- The fitting-out and gathering chains are dissolved into others.
- The water chain's own passage still opens at 28:23. 28:22 appears only under "the failing mount".

**Step 2 packets** (r10 unchanged, new map without `## Not carried`): 1:6 est $1.19, 1:5 est $1.15. Awaiting
approval.

## End-of-discovery passage check (2026-09-30, user design)

The agent runs `missing.py` itself, once, when discovery is complete and before it writes its output. It passes
the Quran refs it will use. The script returns the reciprocal list's strong passages (directional review, cross-
surah, focus-side "strong") not among them, each with its canonical Arabic and without the list's notes. The full
list never enters the context.

- **Instruction.** The list is not authoritative and may be incomplete; judge each passage; add only what
  supports or sharpens; also add any other passage you recall. It lives in the packet header (trusted) as well as
  in the script's output.
- **Once only.** A marker file in the call's temp cwd, written only after the answer is ready.
- **Size.** 46 strong passages for 1:6 (with 7:16); 210 for S1 (with 7:16). "Strong in both directions" would
  drop 7:16.
- **Runner.**
  - `call_opus(allow=…)` enables only `Bash(python3 …/missing.py *)` under `dontAsk` and `--safe-mode`, in a
    temp cwd.
  - The output is the text after the last tool call; the text before it is a fallback.
  - Tool calls and results go to `tool_calls.json`.
  - `packets.audit()` checks every command run against a strict whole-string pattern.
  - The estimate includes the tool result: 1:6 writer $1.30, S1 map $3.08.
- **Code review.** Sonnet, read-only: 9 findings, all fixed; re-review verdict "ready", then 2 nits fixed.
- **Permission test** (`permtest.py`, Opus, $0.15; `out/permtest/run.log.json`). The allowed command ran. All
  eight variants were refused with "Permission to use Bash has been denied … don't ask mode": `;`, `&&`, `$( )`,
  backticks, `>`, `| tee`, newline plus a second command, and a plain other command. No "HACKED" text in any
  tool output. The strongest evidence is the harness's own: the result event lists all 8 in
  `permission_denials`, and each tool result carries `non_execution_kind: "permission-rule"` (refused before any
  shell ran). Scope: these 8 patterns on CLI 2.1.283 with this `--allowedTools` syntax, not a general proof
  (`||`, `<( )` and quoting tricks are untested); `packets.audit()` stays as the backstop.
- **Instructions in tool output.** The test model said it ignored the instructions inside the script's output as
  untrusted text, which is why the instruction set was added to the packet header. On the first real run, watch
  whether it also under-uses the listed passages themselves. The `call_opus` isinstance guards are defence in
  depth: the crash was in permtest.py's own ungated parser, not in `call_opus`.

### First runs with the check (2026-09-30, user-approved; parallel, one call each)

| run | cost (est.) | refs passed | passages returned | added from the list | audit |
|---|---|---:|---:|---|---|
| 1:6 writer, r10 + map3.nohft + check | $1.11 ($1.30) | 23 | 37 | 7:16, 37:118, 48:2, 6:161, 4:68, 19:43, 10:25 | ok |
| S1 map, map3.nohft + check | $2.42 ($3.08) | 115 | 184, but only a 2 KB preview seen (≈17) | — | ok |

**1:6 writer.**

- The check brought 7:16 back, and the writer judged: it added 7 and left 30. It also recalled the hadith
  «اللهم اهدني وسددني … واذكر بالهدى هدايتك الطريق والسداد سداد السهم», which joins the road and the arrow.
- Pulley still out. The ledger says "map chains Herd, Sky, Water … belong to other ayat's work", the exit clause
  REVIEW_r7_r10 flagged in r10; r10_1 replaces it.
- Scorecard: 3,130 words, 6 sections, paragraphs with 3+ tags 11/29, 27 refs outside the surah, "Aile"
  openings 10, "denir" 9, 2 Arabic outside tags (root names), 3 unsourced (hadith from memory).

**S1 map.**

- 78.8k output, 2 turns, cheaper than map3.nohft (133k).
- **The tool output (43.2 KB) exceeded the CLI's inline limit.** The agent saw a 2 KB preview and a file path it
  cannot read, so the check was largely ineffective on the map.
- This draw recalled 7:16 itself (among the 115 refs passed), with its setting: "(Iblis vowing to God) «لأقعدن
  لهم صراطك المستقيم» — an ambush on the road".
- A separate well chain is back ("The well-head: crossbeam, pulley, and water that keeps a thing standing").
- Still absent: Iblīs's refusal as the ع ب د pride pole, and the «عين قائمة» eye.

**Fix.** `missing.py` builds its answer within a 20 KB byte budget, in steps:

1. full Arabic;
2. each ayah's opening 6 words;
3. refs only, grouped by surah, most widely listed first;
4. the most widely listed refs, with a count of the rest.

1:6 stays at 11.7 KB with full Arabic. S1 now gets all 210 refs as refs only (1.6 KB); the worst case over all
lists is 19.8 KB (32:3). The first fix (opening words above 24k characters) was rejected in review: it bounded
only S1, and the CLI limit is in bytes. The graded version was reviewed "correct, ready".

**Dir names.** `packets.py map --tag check2` writes `surah.map3.nohft.tool.check2`. A writer's dir name is built
from its map dir plus its own flags, so the r10_1 writer on that map is `DM.r10_1.map3.nohft.tool.check2.tool`:
the first `.tool` is the map's check, the second the writer's. `--tag` is refused for `writer` (Sonnet review nit).

### S1 map with the fixed check: a safety stop (2026-09-30, user-approved; `surah.map3.nohft.tool.check2`)

$3.31 (est. $3.08), 76.1k output, 1,693 s.

- **The check worked.** The map passed 75 refs; all 192 returned refs reached it (1.6 KB). It added 42 of them,
  7:16 among them («لأقعدن لهم صراطك المستقيم», "an ambush set on the road"). 7:11–12 are cited.
- **The output was stopped by the model's safeguards** in the "Tenderness and hardness" chain (anger: hard rock,
  thick skin, blood boiling in the heart, swelling around the eye). The stream has `system/informational`
  "Opus 5.5's safeguards stopped the response above · continuing once with that noted". On the continuation the
  model wrote a note ("I can't give you the full map …") instead of the rest.
  - About 12 chains are complete. Missing: ten planned chains (the well-head among them), and all of
    `## Interactions`, `## Ayat` and `## Not carried`.
  - Earlier map3 runs wrote the same anger material without a stop; it reads as a false positive.
- **The runner logged it "ok"** (with `map_complete: False`) and exited 0, so the chained r10_1 writer started on
  this map, including the model's note. The user stopped the writer about 2 minutes in, before its check call
  (`out/1_6/DM.r10_1.map3.nohft.tool.check2.tool`, prompt only; ledger "stopped"). Not rerun.
- **Fixes.**
  - `call_opus` records a safeguards stop (`safety_stop`), and the status becomes "safety-stop".
  - `packets.call` exits non-zero on any status other than "ok", or on an incomplete map, so a chained call
    stops.
  - `writer_packet` refuses an incomplete map.

### The check with medium passages (user, 2026-09-30)

The reciprocal list's medium tier holds some of 1:6's closest passages: 38:22 «واهدنا إلى سواء الصراط», 20:135
«أصحاب الصراط السوي ومن اهتدى», 90:10 «وهديناه النجدين». The last 1:6 writer used 6 of the 61 medium
passages. Ayah calls now get strong and medium, strong first, with no labels shown. The map call stays on strong:
its medium union is 424 more refs.

**Size.**
- The CLI cut the 24,514-character, 44,228-byte answer, although `BASH_MAX_OUTPUT_LENGTH` is documented at 30,000
  characters. The cut is byte-based and undocumented, so the setting is not relied on. 11.7 KB passed whole.
- The answer stays within 20 KB: passages in list order with their full Arabic as long as they fit, the rest as
  refs only, by surah. Opening words were dropped, because the relevant part is often at the end (38:22 opens
  «إذ دخلوا على داوود»).
- 1:6: 107 passages, 77 with text (38:22, 20:135 and 90:10 among them), 30 as refs. S1: 85 with text, 125 as refs
  (before: refs only).

### r10_1 on 1:6 with the check, strong + medium (2026-09-30, user-approved; `DM.r10_1.map3.nohft.tool.tool`)

$1.13 (est. $1.37), 3,003 words, 7 sections. Map: `surah.map3.nohft.tool`. The S1 map rerun was skipped (user).

- **Check.** It passed 23 refs and got 93 back. It added 13: 37:118, 15:41, 10:25, 5:16, 11:56, 17:9, 90:10, 38:22,
  17:35, 23:74, 29:69, 49:17, 47:17. Seven of those are medium-tier, 38:22 and 90:10 among them.
  - 38:22 does real work twice: the verb with and without إلى (grammar), and "do not exceed, lead us to the middle
    of the road" (balance).
- **7:16** is now a section of its own, "Pusu kurulan yol". It opens with Iblīs's refusal to bow to Adam, so the
  reader knows who sits on the road. Then 7:17, then 15:41 as God's answer. 37:23 («فاهدوهم إلى صراط الجحيم»)
  shows that the verb and the noun alone guarantee nothing.
- **Pulley.** Still out. The ledger: "B012 the well pulley … would not have served the road, standing or balance
  themes here". The exit clause is gone; the decline is now a judgement on the themes.
- **Scorecard against r10.** "Aile" openings 10 → 0. "denir" 9 → 32: the brief's "… denir" turned into the new
  tic. "X için … denir" runs line up senses (the balance section), and once it is wrongly used for a Quran quote
  (41:17). Paragraphs with 3+ tags 11/29 → 13/25.

## Sonnet 5.5 trials, r11 and r11_1 (2026-09-30, user-approved)

**Runner.** `packets.py writer --model sonnet --effort <level>` (Sonnet 5.5, $4/M cache write, $10/M output); a
non-default model or effort writes to `<dir>.<model>.<effort>/` on the same prompt. `call_opus` takes `effort`.
Reviewed (Sonnet).

| run (same prompt as the Opus r10_1 run on that ayah) | cost (est.) | time | words | refs outside S1 | result |
|---|---|---|---:|---:|---|
| 1:5 Sonnet high | $0.40 ($0.67) | 154 s | 1,698 | 26 | ok |
| 1:5 Sonnet max | **$3.23** ($0.67) | 2,041 s | 0 | – | **failed**: 4 turns of thinking only, each cut at the CLI's 64k cap for Sonnet (although `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`), then "API Error: … exceeded the 64000 output token maximum". Never called the check. Thinking is encrypted (signature only), so its content cannot be read. Not rerun. |
| 1:6 Sonnet high | $0.42 ($0.68) | 161 s | 1,717 | 15 | ok |

**Sonnet high against Opus.** Cheaper (a third) and fast, accurate on sources (96–100% tagged), sometimes a sharper
join: 2:133 / 26:71 (na'budu in other mouths) on 1:5; on 1:6 the Madyan well, 28:22 → 28:24 ("İstenen şey bir
yöndü, verilen şey su ve gölge oldu"), the road–water join no Opus run made, and hady as the inviolable refugee.
But half the depth, first-person hedging against the brief (about six times on 1:6), and more slips (dīn read as a
branch of ع ب د; 1:4 said to name qiyāma; garbled sentences). Not a replacement writer; possibly a cheap discovery
pass. Max effort is unusable as is.

**The check runs early, not at the end.** Thinking before / after the missing.py call: Opus r10 6.4k / 10.4k, Opus
r10_1 4.8k / 11.9k, Sonnet 1:6 0.2k / 8.9k, Sonnet 1:5 1.6k / 7.9k. The list feeds discovery instead of checking it.
A two-step runner (draft, then the list, one revision) would fix this; the user kept the tool as is for now.

**Correction.** `surah.map3.nohft.tool/map.md` does carry "Trodden road / Well-head: 28:22–24" in `## Interactions`
(the note above was about map3.nohft). The road–water gap is the writer's, not the map's.

**r11** (`prompts/r11/`): r10_1 with four edits: no "do not use tools" (it contradicted the header's check line);
usage "in varied wording" instead of the "… denir" example; "a scene where two such chains meet" can found a theme;
the ledger says why an omission "could not found, reshape or join a theme".

**r11 on 1:6, Opus high, with the whole S1 dictionary** (`--surah-dict`, user's choice; the header said the other
roots serve only resonances within the focus ayah): $1.86 (est. $1.67), 503 s, 3,071 words, 37 refs, 97% sourced.
- New: 4:68–69 (the Quran's own 1:6 → 1:7 order, "rafīqā"), 2:142 (istiqāma is not a compass direction), 25:63,
  83:1–6 with the scale, 93:7, 6:87 / 6:90, 3:101, 32:10. Ends on a synthesis, not a recap. Ledger reasons are real.
- The surah dictionary was read (the ledger declines «الزم ملك الطريق أي وسطه», «شالت نعامتهم», العباديد) but no
  prose quote came from it: every other-root phrase used was already in the map.
- Still no water, well or herd: it uses 28:22 and stops before the well.
- "denir" 32 → 11, but "Araplar … derlerdi" 16; "Tanrı" 9 times; the hadith qudsi's speaker confused; 83:1 cited for
  83:4–5.
- **`--surah-dict` was removed again** (user): +64% cost, nothing in the prose.

**r11_1** (`prompts/r11_1/`, 688 words; built for 1:5 and 1:6, not run): r11 plus "varying the grammar so that no
formula recurs" and "give its actual speaker …; cite a Quran passage by the exact ayah that holds those words, and
put a hadith's source in the ledger". Sonnet review: ready.

**The map's water chain** is clear as an inventory (scene line, eight members, the naʿāma–qāma join, 28:22–24, two
interaction lines) but hard to turn into prose: it gives no payoff, does not explain the pulley by its work, keeps
the road link in one interaction line, places the chain at 1:1 ("Scene as at 1:1"), and carries a doubtful ayn
phrase. A map4 brief could add, per chain, what it makes perceptible through its operation and its road link,
without verdicts. Not built.

## Images step: the surah commentary draft (2026-09-30, user-approved)

**Design.** One Opus call per surah (`packets.py images --map …`, brief `prompts/images1/surah_images.md`) reads the
surah text and the map (without `## Not carried`) and writes, in Turkish with reader tags, one section per image
(the scene by its operation, what it makes perceptible, what each ayah's words add, the Quran passages with
speaker and situation, a `Kaynaklar:` line with ayah, word, root and branch), then `## Buluşmalar`, then a ledger
(`not developed`, `memory`). `writer --images …` gives an ayah writer the images in place of the map; the header
says they are already explained at surah level, so the writer recalls an image briefly and develops what its
ayah's words add. The writer refuses incomplete images, a missing ledger, or a `--map` other than the images' map.

**Sessions.** From this run on `call_opus` keeps each session (`--session-id`, a per-call cwd under
`$TMPDIR/v16_sessions/`); `resume.py <run dir> "question" [--go]` asks diagnostic follow-ups in that session (no
tools; logged as arm `followup`; never part of a reading). Code reviewed (Sonnet 5.5 high, read-only).

| call | cost (est.) | output / thinking | result |
|---|---|---|---|
| S1 images | $2.54 ($2.24) | 88.0k / 32.8k | 10,840 words, 13 images + Buluşmalar; rain and well merged; pulley explained by its work; Buluşmalar: "Yol ile kuyu, Mûsâ'nın Medyen yolculuğunda tek bir sahnede durur" |
| 1:6 r11_1 + map (control) | $1.79 ($1.37) | 61.4k / 44.2k | 3,280 words, 33 refs, 96% sourced; 72:16 (istiqāma on the road → abundant water) in the prose; pulley declined ("belong to other ayat's words"); "Araplar … derlerdi" persists (12) |
| 1:6 r11_1 + images | $1.55 ($1.42) | 40.8k / 22.5k | 3,539 words, 36 refs, 93% sourced; best synthesis so far (6:71, 47:5–6 ʿarrafahā, 20:50, 81:28–29, closing on 7:43); **no water at all, and no ledger line for it**; one source leak ("Daha önceki bir okumada anılan…") |

**Reading.** The images step works as the surah commentary: it carries the road–water scene no ayah reading has.
As writer input it raises quality and halves thinking, but the writer leaves shared images to the surah level,
silently. Open decision for the user: accept that division, or add a counterweight to the header's "recall
briefly" line so that an image this ayah's words take part in is developed here as far as its words carry it.

## Decision: complementary commentaries (user, 2026-10-01)

- **Surah commentary** = the images step (`images1`): the surah's shared images (water and the well, the herd, the
  trodden road, the balance …) and where they meet.
- **Ayah commentary** = r11_1 fed the images (`writer --images`): it develops what its own words add and recalls a
  shared image briefly. No revert: on 1:6 it is the strongest reading (6:71, 47:5–6, the close on 7:43), with the
  least re-telling of surah images and half the thinking. Its known weak points (one source leak, 93% sourced) are
  recorded, not tuned: the ayah brief is no longer pushed (user).
- Per surah: map, then images, then the ayah readings. Long surahs (output caps, pericope-level maps/images) are an
  open design question.

## v5 comparison on 1:6 and r12 (user, 2026-10-01)

**v5 vs v16 on 1:6.** v5's editorial (11,249 words) was read against the v16 1:6 reading and the S1 images. The
synthesis is v16's; v5 is a catalogue of family chains with heavy disclaimers and some echo-root links (هدد). Two
discovery losses are real: (1) Quran passages: v5 had a Quran-wide lane; 33 of its 60 passages are nowhere in v16,
among them 72:16, 27:35, 31:19, 41:17, 49:17, 2:186, 43:10, 2:255, 4:5; v16 has 18 v5 lacks (4:66–69, 47:5–6, 15:41,
81:28–29 …). (2) The map silently dropped ق و م B021 (the eye whose pupil is whole but sees nothing), which v5
developed with 36:66 and 41:17; it was in the writer's dictionary. The 1:6 check (missing.py) did show most v5
passages, but cut at 20 KB: 72:16, 41:17, 39:18/23, 19:76 came as bare refs after 67 passages with text; refs the
writer declared and then dropped were never offered back. v5's pipeline cost ~$20–45 per ayah (its own estimate);
v16 ~$2.3 per S1 ayah.

**Inputs (S1, measured).** Ayah call: images.md 73–90%, dictionary 4–22%, brief ~4%, context ~2% (no HFT, no
channels: the channel review reaches the ayah only through map → images; the map is nohft). Map call: dictionary
69%, channels 28%. Images call: map 96%. S29 extrapolation: map ~536k input (dictionary 484k = 90%), over the gate
as one call; images several calls; the ayah call ~$1.5 with sliced images, ~$2.4 with all of them.

**r12** (user): r11_1 and images1 with
- every reader tag ending in its source: `source:"<root letters>,<branch id>"`, `source:<surah:ayah>`,
  `source:"hadis"` (collection in the ledger), `source:"memory"`; source-only tags for a branch sense or a passage
  named without its Arabic ({source:15:41});
- missing.py: refs only, by tier (own list strong, medium; other side's list strong, medium; own weak; other side
  weak), "no value" and counterevidence left out; `missing.py text <refs>` for verse Arabic, as often as needed;
  once per ayah; the images step runs it per ayah of the surah; the map call keeps strong only;
- the ayah writer reads only the images whose Kaynaklar members cite its ayah, plus ## Buluşmalar (S1: 27% of the
  images tokens for 1:3, 75% for 1:6);
- check.py item 6 verifies declared sources (branch exists and holds the quoted Arabic; ayah exists and holds it)
  for readings and for images.md.
Not done (user, cost): a revision pass after the draft (+$0.3–1.5 per call; the 1:6 log shows the check already
runs before the prose is written).

## S1 images r12 and the augment step (user, 2026-10-01)

**S1 images r12** ($3.09, est. $2.95; 92.6k output, 22.3k thinking; 14 turns): 13,021 words, 12 images + Buluşmalar.
370 declared sources, every checkable one verified (342 ok, 22 source-only ok; 5 hadis, 1 memory); 98.6% of quotes
sourced. The check ran once per ayah (1.6–2.5 KB each); a first combined shell loop was refused by the permission
mode (not run; the audit lists it). The `text` lookup was used mostly to copy exact Arabic for refs already chosen;
listed passages came in from the strong tiers (90:10, 11:56, 15:41, 16:121, 20:50, 25:63, 26:16–23, 7:43 …), the
medium and other-side tiers were not looked up (72:16, 27:35, 31:19, 41:17, 2:186 absent). The well (with the pulley
and 28:22–24) is now inside "Yaslanmak ve ayakta durmak", the rain inside "Rahim ve terbiye" (ledger). Quoting with
sources pushes toward listing dictionary lines.

**Augment step** (`augment.py`, prompts/augment1): after a writer, one Sonnet 5.5 high call gets the commentary with
numbered paragraphs, its ledger, and every listed passage not cited, with its Arabic; it may add passages from its
own knowledge and writes ledger lines only for those. It returns insertions as data; the script applies only anchors
found once, at a sentence end, outside tags, and asserts that removing them restores the original byte for byte.
Output in <run dir>/augment.augment1/. Est. S1 images $1.14 (928 passages, ~185k tokens), 1:6 ~$0.35. Reviewed.

## 1:6 r12, S1 augment1, and r12_1 (user, 2026-10-01)

**S1 augment1** ($1.29; 48.0k output of which 38.7k thinking): 24/24 insertions applied, all sources verified, the
original byte-identical. All 24 from the list (13 strong, 7 medium, 4 other side, 1 weak); about 14 real joins
(18:82, 14:41, 55:9, 6:71, 43:37, 27:63, 49:17, 31:19 …), 4–6 catalogue-leaning (21:107, 7:30, 2:138, 18:17); 72:16,
27:35, 41:17, 2:186 passed over; memory search: 2 ignored lines only. User: 24 of 928 is too low for the cost;
augment runs at ayah level from now on, and adds to the ayah readings only.

**1:6 r12** ($1.57; 41.3k / 25.4k): 2,852 words; all 62 checkable sources verified. New: the arrowhead (هادي السهم
نصله) with the straight shaft (رمح قويم), the qibla/direction branch (ليس لهذا الأمر هدية ولا قبلة) with 2:142 and
16:9. Weak: "Önceki ayetler … anlatmıştı" presents the surah commentary as earlier ayat; spear given as the arrow's
shaft; long ledger; 72:16 declined with a reason.

**r12_1** (user): no hadith, tafsir or outside report in the prose (a passage's situation as the Quran tells it in
its context; hadith and tafsir may come later); terse ledgers; a recalled image is tied to the ayah whose words
carry it and restated, never as "explained before" (`recall_rule`, images description). augment2: a paragraph that
already cites passages is as open to additions as one that cites none; same no-hadith rule. The audit now lists
commands refused by the permission mode as denied, not run. Not reverted to r11 for length (user agreed): r12 is
r11_1 plus sources; the length drop is one run and likely the sliced images.

## Opus progress review and r13 (user, 2026-10-01)

An Opus review (read-only) found the work circling on the ayah brief (~20 calls on 1:6, each fix growing a new tic:
"denir" → "Araplar … derlerdi" → "Sözlük"), while the map → images → ayah architecture moves forward. Decisions
(user): freeze the ayah brief as **r13** = r12_1 + (a) option C: an image the ayah's own words take part in is
developed in the reading as far as the word carries it (object, work, naming usage); the scene it forms with other
ayat's words is the surah commentary's, recalled in a sentence tied to its ayah; (b) style lines: no "sözlük"/map/
chain talk, the surah's own words in tags, its ayat named in words; (c) "Work from the supplied evidence and your own
knowledge" restored; (d) the writer gets only the `text` lookup, the list goes to augment; (e) the writer is built
from the D arm plus the sliced images (no r2 map needed). Stop tuning on 1:6; validate on S100 end to end. The Luna
thematic lists wait. packets.py map/images take --surah (surahs with v9 HFT and channel files only).

## S100 and S107 end to end with r13 (user, 2026-10-01)

| surah | map | images | readings | augments | total | per ayah |
|---|---|---|---|---|---|---|
| S100 (11 ayat) | $1.64 | $2.73 | 11, $12.06 | 11, $5.03 | $21.47 | $1.95 |
| S107 (7 ayat) | $1.57 | $1.98 (repair run; first attempt hit the session limit at $0) | 7, $6.00 | 7, $2.66 | $12.21 | $1.74 |

All readings clean: no Arabic outside tags, every checkable source verified except three (a quote of 100:8 tagged
38:32; one wrong branch in 100:3; a single-letter quote in 107:2 the checker cannot match). "denir" persists (2–12
per reading). The process-word flag catches "zincir" used as an ordinary word (oath chains, the Quran's chains):
noisy, kept for the record. 100:1 reaches the North Star "horses as argument" unprompted (16:7–8 breath spent for
the rider against 100:6 ingratitude; chest breath against 100:10). Augments: 5–16 insertions per ayah, all applied,
all sources verified.

**S1 with r13** (user, 2026-10-01): images $3.92 (14,105 words, 413 tags all verified, no untagged Arabic, no bare
refs, no process talk: the r12_1 style faults are gone); readings 1:1–1:7 $10.72 (one wrong branch in 1:2; "denir"
3–17); augment3: a first attempt hit the session limit at $0 (kept as augment.augment3.session-limit-0usd), the
repair run completed.
