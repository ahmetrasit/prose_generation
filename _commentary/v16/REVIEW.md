# v16 review: independent read-only audit (2026-09-29)

This review was written by an Opus subagent at the user's request. It was read-only: no model runs and no file
edits. The main session saved it here. It spot-checked two claims before saving: D's and VD's prompts contain no
ن ع م entry, and D says "Bağ sözlükten değil" (reading line 65). Both hold.

## 1. Verdict

1. **Only the surah call had the full pulley evidence.**
   - E1 and D saw one isolated B012 line among 21 ق و م branches.
   - H, V and VD saw a well chain whose upstream authors had already abstracted the pulley: "upright mechanical
     component" / "taşıyan parça".
2. **The cause differs by call.**
   - Ayah writers: a data and design problem. The chain's other members are not in their input, and no assembled
     finding names the pulley as a pulley.
   - Surah call: model judgement. It kept chains of the same evidential type and dropped this one. A brief that
     permits dropping and has no rule against folding a mechanism into an abstract function made that easier.
3. **One DESIGN.md inference is unsupported.** "The writer sees the join and does not use it" (D/VD) does not hold:
   D had no ن ع م entry, and its prose says of 1:6→1:7 "Bağ sözlükten değil".
4. **Scripts are sound for what ran.**
   - Verified: the 1:6 slice is complete, `trim_hft` is lossless, D's dictionary has v9's roots and branches, and
     `prompt.md` sizes match the ledger.
   - Latent major bugs:
     - parallel D/VD/DM runs crash, or silently mix dictionaries;
     - the never-rerun guard fails on interrupted calls;
     - the stream parser discards text when no `result` event arrives;
     - the surah dictionary mislabels identity roots as ECHO in longer surahs.
5. **The writing brief contradicts itself.**
   - It is contradictory on memory.
   - Its "don't quietly translate" rules produce one disclaimer per image (4–5 per reading).
   - Verdict-carrying data (word notes, "yanlış sayılmış") reaches every writer.

## 2. Pulley

### Evidence per configuration (from `out/…/prompt.md` and `e1/1_6/rep*/prompt.md`)

| config | B012 line | ن ع م B007 | channel 10B | HFT water/well | other members (ع ل م B005, ر ب ب B013, م ل ك B007) |
|---|---|---|---|---|---|
| E1 rep1/2 | clipped (Ayn man-shaped + Ṣiḥāḥ «القامة البكرة بأداتها» survive; Tahdhīb cut); definition "…tartışmalıdır", facet "…yanlış sayılmıştır" | no | no | no | no |
| H | same clipped | only as channel motif "ostrich-shaped well timber" and HFT «طيران النعامة وتفرق القوم» (B008) | yes, verbatim: "An upright timber and working components…"; motif "upright mechanical component"; ran without the judgements note | none (0 of 14 records use B012 or B007) | only as channel motif labels |
| V | clipped | no dictionary entry; v5 macro: "en‘amte ailesinde … kuyu başı kerestesi" | no | no | v5 macro assembles them, B012 as "taşıyan parça", wrapped in a disclaimer |
| D | whole, incl. Tahdhīb crossbeam line; glosses include "…fakat yanlış sayılmış yorum" | no (1:6 roots only) | no | no | no |
| VD | whole | no (v5 macro only) | no | no | v5 macro only |
| Surah call | whole | yes | yes (last input, after 108k chars of HFT) | none on B012 or B007 | all present |
| DM | whole | no | no | no | only via the map, which has no well chain |

No reading in any of the seven uses B012 in any sense (pulley, sword hilt or bed leg).

### Causes, ranked

1. **The chain is absent from single-ayah inputs** (data/design: E1, D, VD, DM). Linking النعامة to أنعمت needs
   memory. D did not make the link: "Bağ sözlükten değil".
2. **Upstream findings abstract the pulley away** (data: H, V, VD, surah).
   - Channel 10B says "upright mechanical component". Naʿāma is the crossbeam («الخشبة المعترضة»), so the proposed
     scene is also mechanically off.
   - v5 has "taşıyan parça" and adds disclaimers.
   - HFT has no record on either branch.
3. **Surah call: model judgement, plus a brief gap.**
   - The brief gave a path: members "need not" translate; a dictionary join is "the strongest evidence".
   - The model kept rare and [kalıp] chains, but folded the water members into mainstay (chain 12) and weather
     (chain 10).
   - Licences to drop: "Choose the chains that are the surah's own; not every proposal is one" (undefined) and the
     "lets a listener hear" gate.
4. **Selection pressure and disclosure cost** (instruction; moderate).
   - Pressure: additions.md:3 "most candidates … stay out".
   - Disclosure cost: write_v10:38–39 and :61–62.
   - Not an exclusion rule: writers used many other related-noun senses.
5. **Verdict-carrying data** (weak to moderate).
   - The context.md word note "wide root family narrows to upright quality".
   - B012's gloss "fakat yanlış sayılmış yorum".
6. **Clipping** (E1, H, V). It removed the join, not the pulley. D and VD show that restoring it is not sufficient.
7. **Two keys.** No prompt contains that rule; it is not a cause.
8. **Memory contradiction** (I1). It matters where the naʿāma→anʿamta link needs memory (D, VD).

### Judgement

- **Ayah writers:** an instruction and data problem. A writer given one isolated tool-part and no chain is
  defensible in leaving it out.
- **Surah call:** model judgement. The dictionary attests every member and states the join outright, as well as it
  supports chains that were kept.
- **Honest limit:** no dictionary phrase links istiqāma to the pulley or its straightness. The pulley is an
  interpretation (an echo), and a writer could legitimately keep it in Ek Notlar.
- **Unverifiable:** no thinking was saved, so the reasons are inferred.

## 3. Script bugs

| id | severity | where | problem | fix |
|---|---|---|---|---|
| S1 | major (latent) | v16.py:84–91; dictionary.py:47–53 | Packets are built in worker threads that share one SQLite connection (reproduced: `ProgrammingError`). `section()` monkeypatches `P.dict_lines`, so a D-family arm could silently get v9's clipped lines. Triggers with `run --arm D/VD/DM` over several ayat. | Build sequentially in the main thread and parallelise only `call_opus`; pass the formatter as a parameter. |
| S2 | major (latent) | dictionary.py:69 | A root's label comes from its first occurrence: S18 has 4 roots mislabelled (e.g. ق ل ل as ECHO, though it is the identity root of 18:22), S2 has 15. S1 and S100 are unaffected. | Rank identity > alternative > echo per root. |
| S3 | major for scale-up | v16.py:123–125 | Ranges ("2:67-71"), bare lists ("12:10,15") and `### X1.` blocks are missed. S1 and S100 are clean. | Expand ranges and bare lists; map X blocks through their spans. |
| S4 | major | v16.py:240/248, 330/338 | The guard checks only `run.log.json`; an interrupted call allows a second paid call. | Write a started marker or ledger row before calling. |
| S5 | major | v16.py:221–226 | With no `result` event, joined texts are dropped, and the guard then forbids a rerun. | Write the partial text and log `status: partial`. |
| S6 | minor (unverified) | v16.py:218/223 | `"".join` is right for a max-tokens continuation (the first message hit a 64k cap), but the event shape is assumed. `joined_turns` is spurious when `result` is absent. | Log message ids; compute `joined_turns` from them. |
| S7 | minor | v16.py:164–168 | DM does not check that the map is complete. | Require `## Chains`, or a complete ledger row. |
| S8 | minor | v16.py:190–191 | The estimate ignores continuation re-caching ($1.75 estimated, $2.85 actual). The gate still holds (worst case $3.41). | — |
| S9 | minor | v16.py:273–282 | `trim_hft` drops the preamble note on older root maps. Some judgement phrases remain inside trace text. | — |
| S10 | minor | — | The prompt says "(write.md)" for write_v10.md. DM's "surah_map.md" collides with the brief's name. An empty "## Standalone Subchannels" heading appears for 1:6. The ledger has no prompt hash or CLI version. | — |

## 4. Instruction issues

| id | severity | problem | fix (case-neutral) |
|---|---|---|---|
| I1 | major | write_v10:3 "Work only from the supplied evidence" and :42–43 contradict every evidence clause's "your own knowledge". There is no rule for marking memory. | "Work from the supplied evidence and your knowledge of Arabic and the Quran; where a sense or passage comes from memory rather than the dictionary, say so where you use it." |
| I2 | major | write_v10:38–39 and :61–62 produce one disclaimer per non-translating image (D and DM: 4–5 each), against :49–51 and :67. | "Family images are heard beside the word's meaning, not in place of it; say this once, then do not repeat it per image." |
| I3 | moderate | additions.md:3 "most candidates … stay out" is a proportion prior, not a criterion. | State only the payoff criterion. |
| I4 | moderate | The Ek Notlar valve collects the cross-ayah links that threads should develop (VD's 72:16, DM's led-mount body). | "A finding that ties this ayah to another ayah or chain belongs in a thread, not in Ek Notlar." |
| I5 | minor | write_v10:25 ("headings only when they help") vs additions' themed `##` sections. | — |
| I6 | minor | Stale references: "concordance panels", "Without a brief". | — |
| I7 | moderate | context.md word notes carry verdicts ("wide root family narrows to upright quality") to every writer, contradicting the judgements policy. | Drop them, or cover them with the judgements clause. |
| I8 | moderate | Verdict-bearing glosses ("…fakat yanlış sayılmış yorum"). dictionary.py:26–27 wrongly claims the glosses follow source-phrase order; they follow lexical-unit order. | Remove the claim; render verdicts as attributions. |
| I9 | moderate | Surah brief: no rule against folding a concrete mechanism into its function; "surah's own" undefined; HFT is 2.4× the channel review; no record of what was dropped. | "Keep a scene at the level of its object, parts and operation…"; end with `## Not carried` (each HFT record or subchannel not carried, one line why). |
| I10 | minor | write_v10:17 "Do not flatten a well, a support…" names a generic image matching a North Star item. | Replace with "a concrete object or mechanism". |

## 5. DESIGN.md claims checked

| claim | result |
|---|---|
| 603 of 1,791 v9 branch lines clipped (34%) | true |
| 47% smaller (32,352 → 17,043 chars) | true |
| v5 gzip ratios (templated macro 0.058 and 0.085; prose 0.28–0.38) | true (1:6 macro sits at 0.281, near the edge) |
| First test cost $4.79 | true |
| D, VD, surah and DM costs and thinking tokens | true |
| Backfilled prompts match the ledger | true (10 of 10) |
| HFT 196 KB → 108 KB | true only with mixed units: 196,181 bytes → 114,719 bytes = 107,838 chars |
| [kalıp] = 15% of branches | true for the whole dictionary (15.3%); 12.2% for S1+S100 roots |
| "DM on 1:6 about $0.8" | false: the ledger estimate was $1.02; actual $0.57 |
| Map cut at a per-message cap; `## Ayat` whole; 1:6 lists 11 chains | true (70,763 − 6,763 = 64,000) |
| "D/VD: the writer sees the join and does not use it" | not supported |
| v16 dictionary has the same roots and order as v9 | true |
| 374 branches in the size table | not reproduced (377 or 311, depending on what is counted) |

## 6. Contamination

- No known answers, no North Star text and no watch cases appear in any `out/…/prompt.md`.
- Near-miss: write_v10:17's "a well" (I10).

## 7. Could not verify

- The models' reasons: no thinking was saved.
- The real stream-json shape, and whether `CLAUDE_CODE_MAX_OUTPUT_TOKENS` lifts the 64k per-message cap.
- 173/174 quotations from `source_phrase_ar`; the Turkish 4-gram claim; the size-by-field table.
- Whether upstream authors saw North Star material.
- check.py beyond confirming it is read-only.
