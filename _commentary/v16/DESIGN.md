# Commentary v16

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
