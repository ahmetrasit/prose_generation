# Commentary v16

Current ayah brief: **r4**, discovery before themes and full coherent development, described at the end.
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
