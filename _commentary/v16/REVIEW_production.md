# Production review: v16 r13 + augment8, and enrichment v2 (Fable 5.1, 2026-10-04)

A read-only review of the two runbooks, the briefs (map3, r13 images, r13 writer, augment8, enrichment common +
zengin, schema card) and the saved runs, before production on S87–S114. Scripts were read only where a finding
needed it. Nothing was changed. The decisions at the end were agreed with the user on 2026-10-04 and are the
work list for the next session.

The purpose, as the user states it: the r13 prose is the frozen baseline; augment and enrichment build on it for
an advanced reader who wants to write a next-generation tafsir (NGT). Completeness and verifiability come before
cost.

## 1. Verdict

Nothing blocks production. The layering is consistent (v16: Quran + dictionary only; augment8: Quran only;
enrichment: the literature), the frozen-base and never-rerun rules match in both pipelines, the augment8 brief
and its parser agree on every verdict form, the pack's base-hash guard handles the augment3→augment8 switch, and
the runbook commands rebuild byte-identical prompts.

The findings below are ranked. Items 1–3 are worth fixing before S88 starts.

## 2. Findings

### 2.1 The 87:6 hand correction is lost for production
The 19:22→19:23 tag fix (2026-10-03) was applied only to the augment3 output, which is superseded. The reading
`out/87_6/DM.r13…/87_6.reading.tr.md` still carries `source:19:22` twice (verified), so augment8 and the
enrichment pack will build on the wrong tag. Neither runbook has a place for reading-level corrections.
Decision: a `corrections.json` beside the reading, applied by augment.py after apply and respected by pack.py;
the raw model output stays untouched as now. Apply the 87:6 fix before its augment8 run.

### 2.2 Every refused lookup was `cd … && python3 missing.py …`
Tally over the saved runs (tool_calls.json):
- images: S1 2 refused of 16 calls, S87 6/33, S88 5/36, S89 4/14, S90 1/27, S91 1/20, S92 1/29, S93 2/18,
  S94 2/19, S95 1/12, S100 2/16, S107 2/15;
- readings: 8 refused over 44 r13 readings; in **87:3 both lookups were refused**, so that writer never read a
  passage it had not been given;
- maps: none.
The tool line (`packets.tool_line`) never says to run the command exactly as written. One clause ("run it exactly
as written, alone: no cd, no &&, no ;") removes a wasted turn per call and the 87:3 case. It changes the prompts
of future builds only (as `TOOL_BRIEF` already did for maps from S96).
The open item "CLI exit code on a refusal" is effectively answered: all refused runs ended with result subtype
`success`, `is_error` false, so exit 0 is near certain; the first `--go` still confirms it (runbook, Setup).

### 2.3 The two runbooks disagree on two rules
- Background runs: v16 says a batch in the background needs its own go; enrichment says the go for a run covers
  the background.
- Commits: v16 says commit and push the new out/ dirs after each step; enrichment says commit only when asked.
Decision: one wording in both. **Commit (and push) after every completed step**, in both pipelines; the user
wants this (a recent SSD loss). It is not too much: each step's outputs are a few files, and `work/` stays
uncommitted. Background: say in the go whether the run is foreground or background; a go for a run covers the
background when the user says so.

### 2.4 Enrichment ayah pages are the uncalibrated and probably dominant cost
The surah page's rate per 1k base words will not transfer: most of a call is research overhead, not base length.
Program scale (S1 + S87–S114 = 295 ayat, 28 surahs; Opus 5.5 high):

| Step | Per unit | Program |
|---|---|---|
| map + image prose | ~$7 per surah | ~$200 |
| readings | ~$1.1 per ayah | ~$320 |
| augment8 (ayat) | ~$1.6–2.8 per ayah | ~$500–800 |
| augment on the surah commentary (new, §3) | ~$20–45 per surah | ~$600 |
| enrichment surah page | ~$7 per surah | ~$200 |
| enrichment ayah page | unknown; guess $3–6 | ~$900–1,800 |

Wall time: an enrichment page is 25–30 min; S87's 19 ayah pages at `--parallel 2` are about 5 hours. Run one
ayah page first (87:8 is the only ayah with an augment8 base today) and treat its cost as the program's number.

### 2.5 S87's frozen bases carry known checker findings
The S87 image prose has 61 Arabic strings outside tags; 13 of its readings have bare Arabic too (status.py). They
are final once enrichment starts and become errata candidates on every page. Decide before S87's enrichment:
accept as is, or hand-tag with the corrections log of §2.1.

### 2.6 Both S107 enrichment pages are on the old brief
The accepted S107 surah page is Astra max under the first brief; the Opus trial is also pre-change. Decision:
a fresh S107 surah page (~$7), in the new order of §4.

### 2.7 Small, no action
- `augment.py` line 36 still names sonnet as `MODEL` in a stale comment; the production dir name
  `augment.augment8.opus` depends on that constant (model != MODEL adds the suffix). Do not "fix" it without
  renaming the dirs; a comment is enough.
- Enrichment blocks may anchor to an augment8 addition (capa quoting it) while a reader can hide augment8
  additions; such a block then dangles. A rendering question for the reader app, not the pipeline.
- v16 calls write the prompt cache at the 1-hour rate (`ephemeral_1h_input_tokens`, verified on 87:8), enrichment
  at the 5-minute rate. On 87:8 the cache write is 12% of the reading's cost and 31% of the augment's; the
  5-minute rate would save about a tenth per call, but a thinking turn longer than five minutes forces a rewrite,
  so the gain is uncertain. One measured trial, not a blind switch.
- Cache read rates verified from the ledger: Opus 5.5 $0.20/MTok (S100 enrichment: 11.13M reads).

## 3. Redundancy: the surah commentary, the ayah readings, and the two enrichment levels

### 3.1 Data
Outside-surah Quran references (source tags), by where they appear:

| | S1 | S87 | S100 |
|---|---|---|---|
| cited by the surah commentary | 162 | 174 | 95 |
| cited by some ayah reading (union) | 269 | 424 | 208 |
| in the surah commentary only | 74 | 50 | 38 |
| offered to the image writer by its inline list check (distinct, unused at the time) | 945 | 1,887 | 1,121 |
| of those: strong tier | 177 | 349 | 164 |
| of those: taken into the final commentary | 29 | 51 | 18 |
| of those: later used by some reading | 114 | 236 | 80 |

87:8 augment8 (Opus) added 80 distinct references: 27 already in the S87 images, 34 in some reading.

S100 enrichment surah page (Opus high, accepted): 63 blocks; 23 surah-wide or on a range (nuzul, esbab,
kaynak_notu, nazm, meal verdict, yenilik/oncul on the image synthesis …), 40 on a single ayah; kat: 15 temel,
40 ek, 8 arastirma.

### 3.2 Reading
- The surah commentary carries passages no reading has, so the ayah augments cannot stand in for it.
- Its only QeQ pass today is the inline list check at the end of the image call: the writer sees the lists as
  bare references, after discovery, with ~16k words still to write, and takes about 3% of them. The readings
  moved that job to augment8 on purpose. **The surah commentary is the least cross-checked prose in the
  pipeline.** The images in synthesis (the meetings section above all) exist only there; the readings recall
  each scene in one sentence, so a passage that stages a surah-wide scene is never judged against the scene's
  full development. For an NGT writer that is a gap, not a redundancy. The user's plan to augment the surah
  commentary is right.
- The ayah augments re-judge overlapping lists (S87: 2,709 listed over 19 ayat, 1,887 distinct; ~30% repeat
  judgements) against different paragraphs. By the augment5 decision this is intended; keep.
- Enrichment: the two levels overlap only in the single-ayah blocks of the surah page (40 of 63 on S100). The
  23 surah-wide blocks and the antecedent audit of the images have no other home. The surah page is ~5% of a
  surah's enrichment cost. Keep both levels; change the order (§4).

### 3.3 Why the surah augment cannot be one augment8 call
The augment8 guarantee is a verdict for every listed passage. A surah's list is the union of its ayat's lists
plus neighbours: S1 1,372, S87 2,251, S100 1,395 passages, i.e. 450k–750k output tokens at 330 per passage.
Even the strong tier alone (S87 349) is over the practical output cap (~60k used by 87:8; 128k hard).

Options weighed:
- **One call per image section** (chosen). Each `## ` section names its member ayat in its `Kaynaklar:` line,
  so its list is the union of those ayat's lists with the Arabic (a few hundred passages) and augment8 applies
  unchanged, with every guarantee and warning. S87 has 18 sections, S100 11, S107 ~7. ~$2 per call. The
  `## Buluşmalar` section is its own call. It relaxes the one-call-per-prose rule; an image is the surah
  commentary's own prose unit.
- One call per surah commentary with a derived list (the ayah augments' prose verdicts + conflicts + own
  knowledge): fits one call, $3–5 per surah, but never judges the raw list and the audit trail is thinner.
  Rejected.

Script rule agreed: **a surah commentary whose whole list fits under the output cap runs as one call; otherwise
one call per image section.** Small surahs stay at one call. Section-local paragraph numbers map to page
numbers in the script. `pack.py` takes the augmented images file as the surah base when it exists, as it already
does for ayat (additions unnumbered under ¶n).

## 4. Order per surah (agreed)

map → image prose → readings → augment8 on the ayat → augment on the surah commentary → **one** pack build →
enrichment **ayah pages first**, **surah page last**.

- The surah page, run last, reads the accepted ayah records: a point already on an ayah page is cited by id,
  not repeated; the surah meal verdict builds on the ayah pages' alignments instead of re-aligning 16 meals for
  every ayah. This removes most of the overlapping single-ayah blocks, keeps the pages consistent, and ends the
  "pack rebuilt since the call" failure class (one pack build per surah, after v16 is complete). The surah page
  gives up its independence from the ayah pages; agreed.
- Enrichment never starts on a surah before every v16 step of that surah is done.
- The inline list check in the image call becomes redundant once the surah augment exists, but removing it
  changes the image prompt mid-campaign (S87–S95 images are built). Leave it.

## 5. Fable 5.1 instead of Opus 5.5

Prices (verified against the ledger for Opus): Opus 5.5 $4 / $20 per MTok, cache write (1h) $8, cache read
$0.20; Fable 5.1 $10 / $50, cache write (1h) $20, cache read $0.25.

Evidence from the paired runs in DESIGN.md (1:5 r3; 1:5 r6/r7): Fable used a quarter to a half of Opus's
thinking tokens, so a call cost 1.3–2.5× Opus, not 2.5×. It found the sharpest cross-passage joins and wrote
cleaner prose, and made one factual slip per reading (a root identity; an ayah number). Every brief since r8 was
tuned on Opus; Fable tends to do worse on prescriptive prompts written for earlier models. Enrichment's Opus
choice was made for verifiable quotes and no false positives.

Projection for the same token profile: reading 87:8 $0.90 → ~$1.45–2.2; augment8 87:8 $1.64 → ~$2.5–3.5; S100
enrichment page $6.7 → ~$12–14; map/images $4 → ~$7–10.

Recommendation and decision: Opus 5.5 high stays production for map, images, readings and enrichment. Fable
is tried on **augment8**, the one step where discovery is the whole job and every output is checked
mechanically: one run on 87:8 (~$3), its own dir (`augment.augment8.fable`), scored against the 21-key-passage
benchmark (Opus 15, Sol 18) and the warning counts. `augment.py` needs `fable` in its `--model` choices
(`v16.MODELS` already defines it). If it beats Opus on coverage without new slips, augment8 moves to Fable;
the Fable rates are already in `v16.MODELS` for the estimate.

## 6. Work list (agreed 2026-10-04; nothing done yet)

1. `packets.tool_line`: "run it exactly as written, alone: no cd, no &&, no ;" (changes future prompts only).
2. Reading-level `corrections.json`: applied by `augment.py` after apply, respected by `pack.py`; apply the
   87:6 19:22→19:23 fix; log it.
3. Both runbooks: commit and push after every completed step; one wording for background runs.
4. `augment.py`: `fable` in `--model`; run augment8 on 87:8 with Fable (own dir); compare; decide.
5. Surah-commentary augment: `augment.py` accepts the images file; one call when the list fits, else one call
   per image section (+ Buluşmalar); section→page paragraph mapping; additions marked as for ayat;
   `pack.py` takes the augmented images as the surah base.
6. Enrichment order: ayah pages first, surah page last, the surah call reading the accepted ayah records
   (brief and `enrich.py build` change; confirm the brief wording with the user before editing).
7. One pack build per surah, after all v16 steps; runbooks updated to the order of §4.
8. Calibrate: one enrichment ayah page (87:8) before any surah's ayah pages.
9. S87 bases: decide on the 61 bare-Arabic strings in the images and the 13 readings before S87's enrichment.
10. Fresh S107 enrichment surah page in the new order.
11. Optional, measured: `FORCE_PROMPT_CACHING_5M` for v16 calls, one trial against the 1h rate.

Each item needs its own go before it runs; instruction-file edits are shown to the user first.

## 7. Surah augment before the readings; economy of the section passes (user, 2026-10-04, agreed)

**Order revised:** map → image prose → **augment on the surah commentary (per section)** → readings → augment8
on the ayat → one pack build → enrichment ayah pages → surah page. The section lists come from the per-ayah
cross-reference lists, so the surah pass does not depend on the readings.

- The writer's slices come from the augmented images: the surah pass's **prose additions are included, its
  reference lines ("Ayrıca") are stripped** (reference lists in the evidence are the catalogue tic r9–r13 fought;
  the ayah augment restores references at the reading level).
- **The ayah augment does not get cheaper.** Its list is built from the cross-reference lists and the reading's
  citations, and every listed passage is judged against every paragraph. On 87:8, 27 of the 80 passages augment8
  added were already in the S87 images; the reading needed them anyway. Absorbed passages become "cited"
  verdicts instead of prose additions. Excluding surah-judged passages from the ayah list would be a loss.
- Readings of S1, S87, S100, S107 were written on unaugmented slices; from S88 on they see augmented ones.
  Recorded here; no rerun.

**Economy.** 87:8 augment8 ($1.64): prompt cache write 31% (64k tokens, 1h rate), thinking 51% (42k), additions
and verdict text 16% (verdict lines ~4%). Verdicts by tier on 87:8 (new relevant = prose + ref):
strong 7 of 16; medium 19 of 34 (and 4 of the 7 list prose additions); weak 5 of 22; named 2 of 7; neighbours
10 of 44; own knowledge 18. **No tier can be dropped without a real loss.**
- Opus 5.5 high for the section passes (and, expected, for the ayat): Fable charges the cache write 2.5× whatever
  it thinks, and the verdict discipline fixes the output volume; net 1.5–1.8× per call, +$500–900 over the ~570
  augment calls of the program. The 87:8 Fable trial stays a $3 information purchase, not a switch.
- A section (~900 words, ~8 paragraphs) should cost $1.5–3; S87 (18 sections) $35–50; program ~$500–700.
- 5-minute cache: one measured trial (cuts the write share by about a third when no turn exceeds five minutes).
- `## Buluşmalar`: its raw list is the whole union; it gets a derived list (the passages the image-section passes
  judged prose or ref) plus own knowledge.
- Sol 6.1 on the subscription ($0 cash) is not recommended: +204% on 87:8, 33 split references, 9 mismatches,
  and the additions would become the frozen base for enrichment.

Work list additions: 5a. `packets.writer_packet` slices from the augmented images, prose additions kept,
reference lines stripped, recorded in packet.json; 5b. Buluşmalar derived list; 5c. DESIGN note on the
slice inconsistency before S88.

## 8. Lists as seed vs memory-only augment (user question, 2026-10-04; open, test agreed in principle)

The user needs all tiers (good findings come from the weak tier too) and asked whether the list could be only a
seed, with the agent (Fable) doing the exhaustive QeQ work from memory, which would make Fable affordable.

Reviewer's position: not without a test, and the evidence leans against memory alone.
- On 87:8, Opus found 43 new relevant passages through the list and 18 from its own knowledge (a floor for
  memory, since the own pass only had to find what the list lacked).
- DESIGN.md, "Why 7:16 stayed out of 1:5": four Opus and Fable readings missed a mapped passage; recall from
  memory is anchored on the root, scene-level links do not come up, and a passage never considered leaves no
  trace. augment7→augment8 added the neighbours tier because the own pass missed neighbours of cited passages.
  Image writers given refs-only lists took ~3%.
- The list is not the expensive part: thinking is ~51% of a call, the whole prompt write ~31%, the list with its
  Arabic perhaps a third of that write. Dropping the list saves ~a tenth of an Opus call and removes the
  verdict-per-passage guarantee (a miss becomes silence).
- Fable with the list ≈ 1.5–1.8× Opus (the cache write is 2.5×; thinking halves or quarters). Fable without the
  list ≈ $0.9 vs $1.64, with unauditable coverage.

**Test (three arms on 87:8, own dirs, ~$6):** Opus with list (exists: 61 relevant hits, 15/21 benchmark);
Fable with list (~$3); Fable without list (~$1, a trial brief without the list and the per-listed-passage verdict
form; shown to the user before it runs). Metric: of the 61 list-derived hits and the 21 benchmark passages, how
many each Fable arm reaches, what it adds, and whether any addition carries a wrong root, ayah number or quote.
≥90% with no slips: the list becomes a droppable seed and the program moves to Fable. Otherwise the list stays
on every call, all tiers with their Arabic, and the model is Opus.

## 9. The four-arm test on 87:8 (2026-10-04, run with the user's go)

Arms: Opus 5.5 high with the list (the saved augment8 run, baseline); Fable 5.1 high with the same list
(`augment.augment8.fable`, prompt byte-identical); Opus and Fable without any list, on the trial brief
`prompts/augment8m/augment.md` (augment8 minus the list; the own-knowledge pass made the whole job, with the
scene clause, neighbours of added passages and the ledger's left-out passages; Arabic only from the lookup).
Benchmark: the 21 key passages of the augment6/7 review. "Recall" = the baseline's 69 relevant verdicts.

| Arm | Cost | Output (thinking) | Recall of baseline | Benchmark /21 | Refs added | New vs baseline | Words | Check |
|---|---|---|---|---|---|---|---|---|
| Opus + list (baseline) | $1.64 | 55.2k (42.0k) | 100% | 13 | 80 | – | +1,539 | ok |
| Fable + list | $2.62 | 30.6k (21.7k) | 53% | 6 | 60 | 21 | +752 | 1 process word |
| Opus, no list | $1.09 | 36.8k (25.1k) | 60% | 16 | 82 | 33 | +1,346 | ok (2 lookups refused: `cd &&`) |
| Fable, no list | $2.43 | 31.9k (23.4k) | 47% | 15 | 66 | 32 | +1,099 | ok (1 addition without a verdict) |

- All four: 144 distinct refs, 20 of 21 benchmark passages (73:2 found by none). Fable no-list alone found
  20:44, 35:18 and 76:3; 35:18 had been in no run before.
- **Fable with the list is worse and dearer:** it rejected 8 passages the baseline found relevant (92:5–10,
  94:5–6, 20:7, 20:114 among the 32 it never took) and wrote half the words, at 1.6× the cost.
- **List and memory are complementary.** The memory arms reach more of the benchmark (built from review misses,
  which are scene-level finds) but miss 40–53% of what the list surfaces (74:1–10, 20:27–34, 91:8–12 …), and
  their audit trail is thin (4–5 "not relevant" lines: what was weighed and dropped is invisible).
- Fable no-list costs 2.2× Opus no-list for 15 vs 16 benchmark and lower recall. Every quote in every arm
  verified (check.py); content-level slips were not read.

**Conclusion (reviewer):** keep the list, all tiers with Arabic; keep Opus 5.5 high; revise augment8 →
**augment9** by folding augment8m's own-knowledge pass into augment8 (the scene clause, neighbours of every
added passage, the ledger's left-out passages, the per-paragraph minimum kept). Expected ~$2 per ayah. Fable is
not adopted for augment. The brief revision is shown to the user before it runs. The `cd &&` refusals recurred
in two arms: work-list item 1 first.
