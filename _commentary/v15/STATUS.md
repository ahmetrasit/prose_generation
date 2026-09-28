# v15 status (2026-09-28)

Where v15 stands after its first three test units (Fatiha, 4:34, 5:6): what the runs showed, what is still missing,
and what adding or removing data or instructions would do. Numbers come from the two ledgers
(`out/ledger.jsonl`, `out-nocap/ledger.jsonl`), the outputs themselves, and dry builds of the packets (scripts only,
no model calls). The design is in `DESIGN.md`.

## Bottom line

- v15 runs end to end and is built for any ayah. It has been run on Fatiha (all 7 ayat and the surah
  commentary), 4:34 and 5:6.
- Without output caps, 4:34 and 5:6 roughly match the depth of the cold arm, the best earlier single call. On top
  of that, v15 gives every Arabic quotation a source, finds surprises the dictionary backs, and keeps the Turkish
  layer, at 55–70% of the cold arm's length.
- **Not yet shown:**
  - that this holds on blind ayat;
  - that it beats v5, the North Star's bar;
  - that the surah commentary works for a long surah;
  - that the cost can come down to about $1 per ayah.
- **Largest content gap:** passages from the same surah, and a few beyond it, that the ayah reading never brings up.
- **Largest data defect:** 11 roots whose branch numbers are ambiguous.

## 1. Where we are

### Built

| Layer | State |
|---|---|
| Base tables | 77,430 words, 4,657 lemmas, 3,329 roots, 19,604 branches (the Furūq table plus 819 branches found only in the Turkish dictionary) |
| Scene index (Luna) | Whole Quran: 11,337 of the 11,372 branches of Quran roots tagged (193 jobs); Luna returned 35 with no scene. All 142 inventory scenes are used; 8.3% of branches also needed a scene Luna added. |
| Loanword cards (Luna) | 74 lemmas: only those of Fatiha, 4:34 and 5:6 (out of 4,657) |
| Use profiles (Luna) | 39 of the 295 lemmas with 31 or more uses |
| Pipeline | window reading → ayah reading → Luna evidence → Turkish commentary → checks → surah commentary. The scripts were reviewed by Sonnet and fixed. Gates of $5 per call and $5 per ayah; no reruns; at most one repair. |

### Run

| Unit | Output | Opus cost |
|---|---|---|
| Fatiha (capped) | window; 7 ayah commentaries of 705–828 words; surah commentary of 3,453 words | $8.74 in all, about $1.25 per ayah |
| 4:34, capped / uncapped | 1,042 / 1,893 words; 19/19 and 49/49 quotations sourced | ayah $1.98 / $2.41; window 4:19–35 $1.68 / $1.74 |
| 5:6, capped / uncapped | 845 / 1,658 words; 28/28 and 44/44 sourced | ayah $1.95 / $2.12; window 5:1–11 $1.61 / $1.64 |

- Spend: 30 Opus calls, $23.86; 247 Luna calls, on the subscription. No call failed and none needed a repair.
- The dearest call so far cost $1.74 and the dearest ayah $2.41, both under the $5 gates.
- Time per ayah: the reading takes 2–5 minutes, Luna's evidence 6–14 and the writing 1–4. Ayat can run in parallel.
- The capped outputs are in `out/` and the uncapped ones in `out-nocap/`. Everything is committed and pushed.

## 2. Findings

### From the inputs

1. **Supply is not the bottleneck.** The dictionary holds the rare senses that latent readings need. The uncapped 5:6
   took *mirfaq* as leaning straight from it, and 4:34 took the husband's *nushūz* as harshness and beating.
2. **Similarity is not a scene.** In the quran-slm distance matrices, the parts of one scene rank anywhere from 2 to 92
   against each other, so v15 does not use them. The Luna scene index replaces them. It generalises: a random sample
   and the whole Quran needed an added scene at the same rate (8.4%).
3. **The channel reviews are a good starting map, but unranked.** They never say how the chains interact or which
   ayah should carry which chain. The window reading adds both.
4. **Nothing records what Turkish loses,** hence the loanword cards.

### From the runs

1. **The caps were why v15 was thin.**
   - Without them, 4:34 grew by 82% and 5:6 by 96%.
   - Both gained links within their surahs, and 5:6 now makes the North Star's own example.
   - Sourcing stayed complete.
   - Writing cost rose by $0.27–0.32 per ayah. The readings behind the prose barely changed (31–36 findings, 11–13 of
     them leads), so the caps had only limited what reached the prose.
2. **Most links come from the ayah reading.** A script traced every passage the uncapped prose cites:
   - 4:34 cites 25 passages: 18 were already in its reading's record, 4 came only from Luna's evidence notes, and 3
     only from the window reading.
   - 5:6 cites 19: 18 from the record and 1 from the evidence notes.
3. **Misses are of two kinds.**
   - Some never came up anywhere before the writing step: 4:3, 4:81, 4:90 (in this run), 5:89, 5:91 and 35:10. That is a
     supply gap.
   - Others came up, but the writer left them out: 4:129–130, which Luna flagged, and the *qiyāman* of 5:97, which was
     in both the record and the evidence. That is the writer choosing by payoff.
4. **Supply is not use.**
   - Fatiha's scene lines showed the well, and the window reading still set it aside ("no neighbouring word
     activates").
   - The window prompt now says that a coalition of words is itself an activation. This was already in force for 4:34
     and 5:6, whose window plans placed 7 and 5 images.
   - The Fatiha window was run before that change.
5. **One run is a noisy measure.** 4:90 appeared in the capped 4:34 but not in the uncapped one.
6. **Long surahs need input limits to stay runnable** (§4).
7. **The mechanical checks work.** In every output, every Arabic quotation resolved to a source, every anchor was
   valid, and the containment wording was checked.

## 3. What we miss

### Not yet shown

- **Blind ayat.** None have been run, so "any ayah" is still a design claim, not a result.
- **The v5 comparison.** The North Star sets v5 as the bar: v15 is "worth running only if it materially exceeds v5".
  v5's Fatiha prose exists (`_commentary/v5/middle/s001-fresh-20260910/s001/`), so this needs no new runs.
- **The North Star's other named cases:**
  - S100's running horses;
  - 29:39–45, ṣalāh and the race;
  - 18:86 *ḥamaʾ* and 18:96 *nafakha*;
  - S103 *ʿaṣr*.
- **A reader's judgement.** Every verdict so far is mine, judged against the North Star.
- **A surah commentary for a long surah.** Only Fatiha has one.

### Content

- Parallels from the same surah (and a few beyond it) that never come up (§2, runs 3).
- Fatiha was written under the caps, and its window reading predates the coalition instruction.

### Data

- **11 roots have ambiguous branch numbers.**
  - The Furūq table has two entries for each of ب د ء, ب ر ء, ب ك ي, ب و ء, ج ي ء, د ر ء, ش ي ء, ض و ء, ط ف ء,
    ق ر ء and م ر ء. Both entries number their branches from B001. Together these roots are used 1,007 times in the
    Quran.
  - v15's key, "root Bnnn", cannot tell the two entries apart. The 5:6 packet shows two different B001s for ج ي ء
    (coming, and overcoming by coming often).
  - The two entries' scene tags are merged, and a source link cannot say which entry it means.
  - The source table has an id that is unique (`quranic:root_000090:B001`).
  - No output has cited these roots yet. One of them is ق ر ء, the root of *iqraʾ*, which is the North Star's own
    example of what Turkish loses.
- **The scenes Luna added are scattered.**
  - There are 704 ids, and 587 of them are used by a single branch.
  - 494 branches have only an added scene, so they can never join a coalition.
  - Near-duplicates abound, such as `new.body_genitals` and `new.body_genitalia`.
- **Loanword cards and use profiles cover only these three units.** Any other ayah needs those Luna jobs first. For
  the whole Quran that is about 184 card jobs and 256 profile jobs: roughly 3 hours at 15 concurrent, going by the
  ledger timings.
- **`DESIGN.md` §2–3 still gives the first counts:** 18,785 branches and 140 scenes, where there are now 19,604 and
  142.

### Economics and later products

- **Cost per ayah:** from $1.25 (Fatiha, capped) to $2.3–2.5 (long surahs, uncapped, including the share of the
  window). 83% of the Quran's ayat (5,189 of 6,236) are in long surahs.
- **Whole-Quran projection:** about $14k at today's rates through the CLI, against the North Star's production aim of
  about $1 per ayah.
- **What would lower it:** the Batch API (half price) and a cached shared surah prefix. v15 uses neither.
  - The writing and surah steps use no tools, so they could move to the Batch API as they are.
  - The two readings use file tools, so batching them needs either a multi-turn loop or the pulled data put into the
    packet.
- **English and German:** the records are already in English, so one new writing step per language would do. Each
  language would need its own loanword cards.

## 4. What adding or removing data and instructions does

The Opus instructions are short (25–56 lines) and the data packets are large: 22k characters for the 1:6 reading, up
to 152k for 5:6. So what an agent does changes most with the data, and with the few instruction lines that say what to make of a
kind of data.

The North Star records the other side of this: bulk input measurably diluted synthesis. On 4:34, a cold Opus scored
above an Opus that was given the dictionary or the full package.

### Already observed

| Change | Effect |
|---|---|
| Output caps removed (instruction) | prose 82–96% longer; more links within the surah; the North Star's 5:6 example made; sourcing unchanged; writing costs $0.27–0.32 more per ayah |
| Images-only dictionary for frequent roots (data removed) | rare senses lost, so it was reverted: rare senses live in the definitions |
| Scene index (data added) | Fatiha's road, herd and well surfaced mechanically, but the well was still set aside until an instruction said what a coalition means |
| "A coalition is itself an activation" (instruction added) | in force for 4:34 and 5:6; not yet tested on Fatiha |
| Input limits for long surahs (data trimmed from packets) | made 4:34 and 5:6 runnable under the gate; their effect on quality was never isolated |

### Lifting the input limits (measured today by dry build)

I earlier said "about 250k characters". That figure predates the whole-Quran tags, and the table below replaces it.

| Packet | Now | Without limits | Where the growth is |
|---|---|---|---|
| 4:34 window | 117k characters | 514k | far scenes across the surah +216k, the window's scene map +92k, full definitions +89k |
| 5:6 window | 111k | 480k | the same pattern |
| 4:34 reading | 135k | 377k | far scenes +200k, scene lines of the neighbourhood +42k |
| 5:6 reading | 152k | 420k | far scenes +189k, scene lines of the neighbourhood +79k |
| Fatiha | unchanged | unchanged | the limits never bind in a short surah |

- **Context:** it fits, since Opus 5.5's context window is 1M tokens.
- **Gate:**
  - In the existing folders, the gate scales the dearest earlier call by prompt size. It would estimate the window
    call at about $7.3 and stop it, and the reading at $4.2–4.6, which would leave the writing over the $5 ayah limit.
  - In a new variant folder, the gate would fall back to list prices (about $3.4) and let the calls run.
  - By token prices, the calls would likely cost about $3 for the window and $2.5 for the reading, because cached
    input is cheap and output does not grow with input.
- **Risk: dilution.** Almost all of the growth is mechanical, generous scene lists about words far from the ayah.
- **Middle path:** restore full definitions in long windows (about +90k characters; that is where rare senses live)
  and keep the lists of far scenes limited. Those lists remain one read away.

### Other data

| Candidate | Expected effect | Cost | Risk |
|---|---|---|---|
| **Parallels list** (script): passages that share the ayah's rarer roots, from the same surah and from the whole Quran | Dry ranking. For 5:6: the same-surah top 30 holds 5:89 (#14), 5:91 (#16), 5:97 (#6) and 5:8 (#22), and the whole-Quran top 12 holds 35:10. For 4:34: the top 30 holds 4:128 (#3), 4:129 (#6), 4:19 (#19) and 4:3 (#30), but not 4:90 (#45), 4:81 (#72) or 4:130 (#115). Those three echo by phrase (*ʿalayhinna sabīlan* / *ʿalayhim sabīlan*), so a phrase match is needed as well. | +10–15k characters per reading, about $0.1 | It turns into a worklist if framed as one. Give it as supply, and never check coverage. |
| **Key the 11 roots by the source id** | correct anchors and source links; clean scene lines for those roots | a script and about 2 Luna jobs | none |
| **Merge the 704 added scenes** into additions to the inventory | 944 branches can join coalitions | a few Luna jobs and a script | every packet's scene lines change, so the window readings shift |
| **Loanword cards and profiles for the whole Quran** | needed before any other ayah can run; no effect on the outputs so far | about 440 Luna jobs, about 3 hours | none |
| **The quran-slm distances** | they find near-synonyms, not scenes; at most a list of contrasts for the Turkish layer | a script | noise |
| **HFT, the word-analysis prose, the bundles** (left out on purpose) | ready-made hypotheses and obligations | none | selection made upstream, worklists and bulk: the failure modes the North Star names |

### Removing data

| Candidate | Effect |
|---|---|
| The chain map | the chains get rediscovered, against the North Star; keep it |
| Luna's evidence step | the ayah loses its check against the dictionary and against how the rest of the Quran supports, extends or contradicts each finding, plus 1–4 links; saves 6–14 minutes and no money |
| The related-passage list in the evidence step | fewer missing passages are flagged; Luna also searches on its own |

### Instructions

- **Caps:** gone for good. Length and the number of images follow the ayah.
- **Missing passages:**
  - Telling the writer to weigh the passages Luna flags would bring back 4:129–130, but it pushes the writing step
    toward a checklist.
  - Supplying the parallels to the reading as data keeps one mind deciding.
- **Keep:**
  - containment (never "not X but Y");
  - anchors plus triggers;
  - the coalition line.
- **Never** add a line that names a North Star example. That would tune the prompts to the test cases rather than the
  method.

## 5. Decisions waiting on you

1. **Input limits:** keep them, lift all of them, or restore only the full definitions in long windows.
2. **Fatiha:** rerun it without caps, for about $10–12 of Opus.
3. **Next test:**
   - blind ayat (which ones, and how many);
   - the v5 comparison (no runs needed);
   - the named cases (S100 is a single window of 11 ayat).
4. **The 11-root fix:** the script needs no approval; re-tagging needs about 2 Luna jobs.
5. **The parallels list:** build it, then test it on 4:34 and 5:6 as a new variant (about $5–8 of Opus).
