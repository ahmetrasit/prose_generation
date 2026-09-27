# Anchor scoring of the v13 outputs (2026-09-27, 17:00)

Scored by the orchestrator by reading (memory rule `compare-myself`: no comparison agents, no model cost). The anchor
set is `_commentary/v11/eval/s001_anchors.md` (frozen 2026-09-26, never a model input). Scale per anchor per arm, as
the anchor file defines it: **A** absent · **M** mentioned (named or cited, one clause, not connected) · **I**
integrated (explained to a non-Arabic reader, connected to the plain reading and to another finding, source visible).
Anchors scored: the gold items (G) that touch the ayah, the v11-only items for the ayah (the regression guard), and the
v5-only items and HFT readings that a v13 arm could plausibly carry. North-star examples (N) are credited, not required.

Purpose: to make "regression" a defined thing (an anchor that was I and becomes M or A) separate from "bloat" (words,
tags, paragraph length), so that a change to the prose step can be judged on both numbers instead of on feel.

## Form metrics

| file | words | tags | headings | bullets | paragraphs | median ¶ words | longest ¶ | distinct refs | memory marks | cost of the write call |
|---|---|---|---|---|---|---|---|---|---|---|
| 1:5 first run (`out`) | 3,275 | 66 | 8 | 0 | 29 | 112 | 195 | 43 | 2 | $1.28 |
| 1:5 v2 (`out-v2`) | 5,497 | 123 | 0 | 0 | 23 | 244 | 378 | 91 | 1 | $1.73 |
| 1:5 mixed (`out-mixed`) | 7,353 | 180 | 6 | 0 | 21 | 290 | **906** | 92 | 4 | $3.50 (6 parts) |
| 1:5 xhigh (`out-xhigh`) | 7,314 | 136 | 10 | 0 | 29 | 244 | 629 | 113 | 7 | $5.90 (4 parts) |
| 1:6 first run (`out`) | 3,231 | 71 | 6 | 10 | 52 | 59 | 156 | 50 | 1 | $1.74 |
| 1:6 v2 (`out-v2`) | 7,451 | 150 | 0 | 0 | 23 | 275 | **897** | 113 | 4 | $3.65 (2 parts) |

The v2 arm removed headings and bullets (fix: "no bullet tours") and the paragraphs grew to 250–900 words. A 900-word
paragraph is a catalogue in a different shape.

## 1:5 (four arms)

| anchor | first | v2 | mixed | xhigh | note |
|---|---|---|---|---|---|
| G003 ʿ-b-d trodden road → 1:6 | I | I | I | I | all: B005 + 16:69 + 36:61/3:51; v2/mixed/xhigh add 36:72, 67:15, 25:63 |
| G009 mālik ↔ mamlūk | I | I | I | I | all: B001 + 16:75; v2 adds د ي ن B004 madīn; xhigh adds 39:29, 12:41 |
| G012 ilāh defined through ʿabada | M | I | I | I | first: one sentence with ء ل ه B001; the others build the "name → sen" approach on it. **The handoff's "G012 missed by every version" is wrong.** |
| G024 ʿ-b-d anger ↔ maghḍūb | I | I | I | I | first: B008 + 40:60; v2: 4:172, 43:81 double reading, 5:54 → 1:7's two "üzerlerine"; mixed: 7:150; xhigh: 48:26, 2:178, 17:33 |
| G026 ʿāna herd ↔ herd/leader | I | I | I | I | first: ʿāna + ʿabādīd + 74:50 + 6:153; v2 adds the stray "rabbi bilinmeyen"; mixed: four-root hunt scene (rabrab, mālik leader, samā hunters, 105:3); xhigh: 11:56, 81:4 |
| G023 water coalition (1:5 part) | M | M | I | M | echo of ʿayn spring only, except mixed: "gök, bulut, toplanmış su, kuyu" + mālik B007 + ʿayn B010 + palm B004 |
| G029 prayer standing (bonus) | A | M | I | A | |
| v11-1 iyyā construction in 3 persons (29:56, 2:172) | A | I | I | I | first explains fronting but cites no parallel |
| v11-2 gathering scenes (34:40, 10:28, 28:63) | A | I | A | I | xhigh has all three |
| v11-3 fronted object as reply (39:64) | M | I | I | I | |
| v11-4 ʿabd = mamlūk | I | I | I | I | |
| v11-5 26:22 ʿabbadta; 16:75 | I | I | I | I | |
| v11-6 every istiʿāna with patience | I | I | I | I | first: 2:45, 7:128, 12:18, 19:65; v2/xhigh count the six uses; mixed resolves the tension with 16:127 |
| v11-7 performative in ṣalāt; 40:60 | M | I | I | M | xhigh has the qudsī hadith (marked memory) but not 40:60 |
| v11-8 Abraham 26:71 naʿbudu aṣnāman | I | I | I | I | |
| v5 3:79 (no prophet asks to be served) | A | I | A | A | |
| HFT help as gift, not wage | M | I | I | I | benefaction circuit + 16:53 / 76:9 |
| HFT formed for service | I | I | I | I | |
| HFT present provision against debt | A | I | I | I | ʿayn B011 naqd ḥāḍir + dīn as debt; mixed/xhigh add 12:20 dirhams, 9:111 |
| HFT obstacle-breaking aid (18:95) | M | A | I | I | xhigh: the radm as a separating wall → 1:7's ghayr, 57:13 |
| HFT ḥarb ʿawān, renewed war | I | I | I | I | v2: 28:17–18; mixed/xhigh: 2:250 Ṭālūt |
| HFT watchful-eye aid (ʿayn) | M | I | I | I | first: "bizzat sen" only; the others: B003 ḥifẓ, 52:48, Yaʿqūb's eyes |
| **I / M / A of 22** | **10 / 7 / 5** | **19 / 2 / 1** | **20 / 0 / 2** | **18 / 2 / 2** | |

Regressions first → v2 (I → M or A): **none**. v2 → mixed: v11-2, 3:79 lost. v2 → xhigh: G029, v11-7 partly, 3:79 lost.

Beyond the anchors, all four carry the broken-down mount (B011) with 16:7 and 9:92, talāḥuq al-quwwa (B005), muẓāhara
as "arka çıkma", the ʿawān middle → 25:67 qawām → 1:7's two exclusions, 21:112's order, 67:22, and istiwāʾ across three
roots. v2 adds the 16:75 → 16:76 sequence (owned slave → burden → ṣirāṭ mustaqīm) and the ship with its captain
(rabbāniyy). Mixed adds the four-root traveller scene (samā horse-back, mālik forelegs, tar, breakdown, tahādī walk,
ʿimād from two roots, provisions, recovery) and the full ship. Xhigh adds the audience scene (12:88), the adak sequence
(22:36, 22:33, 5:2) and marks three hadith/tradition items as from memory.

## 1:6 (two arms)

| anchor | first | v2 | note |
|---|---|---|---|
| G001 ʿ-l-m marks join the guidance spine | I | I | both: B002 "athar … yahdī ilayh" + 16:16; v2 adds ʿālamūn B003, ism B005, the "sign and its reader" section |
| G002 m-l-k middle of the road | I | I | B006 + 38:22 |
| G003 ʿ-b-d trodden road | I | I | B005 + 16:69 |
| G014 q-w-m standing vs ḍ-l-l buried | M | I | v2: ḍ-l-l B002 + 32:10 in a life arc (womb → stature → buried → raised) and noon vs shadow |
| G016 ṣ-r-ṭ swallowing vs ḍ-l-l | I | I | B002/B003; v2 adds 37:24, 19:71–72 |
| G017 q-w-m resurrection ↔ dīn day | I | I | B013 + 83:6 + 39:68; v2 adds 78:38, 43:61 |
| G018 ḥ-m-d place found good ↔ arrival | M | I | first: 7:43 only; v2: ḥ-m-d B004 + 7:43 + 10:9–10 |
| G019 n-ʿ-m agreeable land ↔ route | I | I | B011 + q-w-m B006; v2 adds 9:21, dīn B006 madīna, rabb B007 |
| G020 n-ʿ-m going on foot | A | M | |
| G021 h-d-y gift ↔ n-ʿ-m | I | I | B004 + 27:35 + 49:17; v2 adds B005 hady, 5:95, 48:25, 48:2, 76:3, 27:36, 14:7 |
| G023 water (q-w-m pulley, ʿ-l-m well) | M | M | first: frozen water only. v2: the well of 12:19, the frame, frozen vs run-off (و ل ه B003), 72:16. Neither joins 1:1–1:4's members (rain, gathered water, ʿaylam, mālik B007). **v2 also uses B012 as a sword hilt in the contest paragraph.** |
| G029 prayer standing | I | I | B002 qawma + 2:238 / 3:39 |
| v11-1 38:22 unique; balance 17:35, 26:182; dīnār qāʾim | I | I | first: 38:22 + B015 + 55:9; v2 adds 17:35, 26:182, 83:3–6, B010 |
| v11-2 hādī goes in front; staff 20:18 | I | I | |
| v11-3 istiqāma = yielding and continuing; qawma | I | I | 41:30; v2 adds 11:112 |
| v11-4 7:16, 15:41 ambush | I | I | v2 adds 7:17, 7:86 |
| v11-5 traveller uses 28:22, 20:10 | A | I | v2: 28:22, 20:10, 6:71 ḥayrān, 93:7 |
| v11-6 4:68–69 rafīq; 37:118 | I | I | |
| v11-7 23:74; 37:22–23 | M | I | |
| v11-8 ṣirāṭ 45×, never plural; 6:153 subul | I | I | both count 45 / 33 |
| v5 2:255 qayyūm | I | M | **the one regression**: first ties al-ḥayy al-qayyūm to rabb B007 iqāma; v2 has only 20:111 |
| v5 17:97 raised on their faces | A | I | |
| v5 49:17 guidance as favour | I | I | |
| v5 variant definiteness (two articles) | I | I | v2 finds the third definite pair, 7:16 |
| v5 surah-root-horizon (1:4 standing → 1:6) | I | I | |
| HFT restored sight (ʿayn qāʾima B021) | I | I | 36:66, 22:46; v2 adds 7:179 |
| HFT gift-return circuit | I | I | |
| HFT embodied supported guidance (B008) | I | I | both: tahādī walk, 20:18, Sulaymān's staff 34:14 |
| HFT calm bearing (B010) | I | I | 25:63 |
| HFT incisive passage (sword B003) | I | I | v2 assembles a whole weapon: sword, hilt B012, spear B008, arrow-tip, shield gh-ḍ-b B008, 57:25 |
| **I / M / A of 30** | **23 / 4 / 3** | **27 / 3 / 0** | |

North-star examples: the stray whose rabb is unknown is absent from the first 1:6 and integrated in v2 (11:56 forelock);
the staging passage 28:21–24 is absent from the first and integrated in v2 (28:22, 28:25, 28:27); 20:49–54 is in
neither; the water system is assembled in neither.

## What the scores say

1. **v2 has no content regression against the first run.** 1:5: 10 → 19 integrated, nothing lost. 1:6: 23 → 27,
   one loss (2:255). The fixes did what they were meant to do on recall.
2. **The "first-run 1:6 is the richest" judgment is about form, not content.** The first 1:6 has 6 headings, 52
   paragraphs of median 59 words, and a closing reread; v2 has no headings and 23 paragraphs of median 275 words, the
   longest 897. The reader is disoriented by shape, not by a missing anchor. So "regression" in this project has two
   axes that must be scored separately: anchors (recall) and form (headings, paragraph length, word count, tags).
3. **Effort above high buys little on anchors.** 1:5 mixed and xhigh score 20 and 18 against v2's 19 at 2× and 3.4×
   the cost. Their gains are scenes (the four-root traveller, the full ship, the adak sequence), not anchors, and they
   come with 600–900-word paragraphs.
4. **The water system is assembled nowhere**, and no prose change will fix that while the network assigns its
   assembly to 1:4 and gives 1:6 `touch`. The gold puts the well-frame at 1:6. This is a disclosure-plan defect.
5. **G012 is present in every 1:5 arm** (M in the first, I in the other three). The handoff is corrected.

## How to use this file

A write-only arm (new tag, step 1 and QeQ seeded from `out-v2`, network from `out-v2`) is scored against the v2
column here. A change is accepted only if no anchor drops from I, and the form metrics move toward the first run:
target ≈ 3,000–4,000 words, headings back, median paragraph under 150 words, no paragraph over 300, tags ≈ 60–90.

## v3 (write-only arm, 18:05) and the v14 Sol candidate for 1:6

v3 = step 1 and QeQ from `out-v2`, network from `out-v2`, the ranked-budget must-land (8 jobs each), the new write
brief with form targets, four new inputs, written sequentially (1:6 saw the new 1:5). Opus 5.5 high, one part each.
Sol = `_commentary/v14/out-sol-max/s001/1_6` (gpt-6-sol, effort max, v14 harness, v2's 1:5 as previous prose; no
cost accounting available). Same scale, same anchors, scored by reading.

| file | words | tags | headings | paragraphs | median ¶ | longest ¶ | cost | anchors I / M / A |
|---|---|---|---|---|---|---|---|---|
| 1:5 v3 | 4,249 | 86 | 7 | 25 | 168 | 230 | $2.41 | **16 / 4 / 2** (v2: 19 / 2 / 1; first: 10 / 7 / 5) |
| 1:6 v3 | 5,039 | 83 | 7 | 29 | 175 | 275 | $2.71 | **19 / 8 / 3** (v2: 27 / 3 / 0; first: 23 / 4 / 3) |
| 1:6 Sol (v14) | 4,971 | 27 | 0 | 44 | 113 | 151 | unknown | **23 / 6 / 1** |

Form: v3 hits every target (headings back, no paragraph over 275 words, tags in range) at 55–70% of v2's cost, and
progressive disclosure worked: 1:6 refers back to 1:5's trodden road, herd, ship and breakdown scene in clauses instead
of retelling them. Sol has the best paragraphing but no headings and only 27 checkable tags in 5K words (most passages
are cited by reference only, so the verifier sees a fifth of the claims).

Recall: **v3 regressed against v2**, mildly on 1:5 and clearly on 1:6.

- 1:5 v3, dropped from I: G029 prayer standing (A), HFT help-as-gift (M), HFT provision-against-debt (A), HFT
  watchful eye (M). Everything else held, including all eight v11 items and 3:79.
- 1:6 v3, dropped from I: G021 gift ↔ benefaction (M: hadiyya and bride are there, the 49:17 / anʿamta link is not),
  v11-5 traveller uses 28:22 and 20:10 (A), v11-6 4:69 rafīq (M), v11-7 23:74 (M), 49:17 (A), gift-return circuit
  (M), B010 calm bearing (A), 2:255 (M). Gained: G014 stays I, 17:97 I.
- Sol 1:6 keeps G021, the gift-return circuit, 4:68–69, B010 and 49:17 that v3 lost, but loses 17:97 and 20:10.

Where the losses come from, by reading the inputs: (a) the passages QeQ tagged `staging` are no longer obligations,
and the writer skipped exactly the traveller-guidance stagings (28:22, 20:10, 6:71, 23:74) and 4:69; (b) the two
images demoted from `assemble` to touch for 1:6 (I15 bride, I16 gift/offering) carried G021 and the gift-return
circuit; the writer gave them one paragraph without the anʿamta link; (c) the smaller HFT items of 1:5 (watching eye,
present provision) sit in the ʿayn echo, which the brief's payoff rule now rightly treats as a clause.

So the ranked budget bought form at the price of recall: −3 to −4 anchors on 1:5, −8 on 1:6. The trade is not
acceptable as it stands for 1:6 (below the first run). Next single lever: **attach passages to jobs**. For each job,
list the staging passages QeQ tagged on the findings that image absorbs (the network line names them), ranked and
capped at three per job; the flat "evidence" list goes. And demote surplus assemblies to `develop` only when the image
has three or more of the ayah's words as members (I16 has two at 1:6), else touch. Rescore on 1:6 alone ($2.7).
