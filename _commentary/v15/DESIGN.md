# v15: design

Written 2026-09-27, from scratch: from `NORTH_STAR.md` and the raw inputs listed in `AVAILABLE_INPUTS.md`.
No earlier workflow was consulted: no runbook, prompt, handoff, design, eval anchor or gold prose of v1–v14 was
read. The North Star is never a model input (it names test cases), and no prompt or inventory here uses its
examples.

v15 is one generic workflow for any ayah of any surah.

## 1. Why earlier workflows fell short, and what v15 changes

The North Star, read as a spec, pulls against itself in six places. v15 resolves each one by construction:

| Conflict | v15 |
|---|---|
| The ayah spec is a checklist ("every image", "each finding's QeQ", "each key word's loss"), and checklists produce catalogues. | **Record vs prose.** Completeness, anchors, QeQ notes, sources and set-aside items live in the record (JSON, shown by the app). The prose answers only to the reader: payoff decides, and a word budget applies. |
| No premature pruning, a compact funnel, and "bulk dilutes" cannot all hold across handoffs. Coalitions need one mind that sees all the words. | **One mind per unit.** The window reading and the ayah reading each do activation → coalition → maturation → payoff inside one Opus context. Everything upstream *supplies* (scripts, Luna data built once per branch or lemma) and nothing upstream *selects*. |
| One prompt with two stances loses one of them. | **Three stances, three steps.** Generative (Opus discover) → evidential (Luna evidence: annotates, never deletes) → communicative (Opus write). QeQ comes after the latent reading, as the North Star orders. |
| "No ranking" vs containment, payoff hierarchy and marked contradictions. | Phrased as an action: *never say which reading is correct; do decide which readings this reader needs here.* The primary reading is the ground, space follows payoff, and contradictions are stated, not hidden. |
| Progressive disclosure vs a standalone commentary per ayah. | The window reading hands each ayah an **allocation** (≤3 images it opens, advances or completes), never a touch-list. The writer re-grounds earlier images in one clause for readers who arrive directly. |
| The trigger rule stops discriminating at scale, and the payoff test is self-judged. | The payoff test is explicit in every record (`perceptible`). A different model (Luna) checks attestation, triggers and QeQ, and it can only annotate. |

## 2. What the inputs showed (checked 2026-09-27)

- **Supply is not the bottleneck.** The Furūq branch table (`quran-slm/resources/source/furuq_full_branches_ar.tsv`:
  18,785 branches, 3,329 roots; 10,932 QAC-attested) holds the rare senses latent readings need, at a median of
  5 branches per root and about 94 characters of image plus definition per branch. Every ayah's full index is
  small: 1:6 about 6k characters, 29:45 about 22k, 5:6 (60 words, 30 roots) about 50k.
- **Similarity is not scene.** The quran-slm distance matrices (character 3–5-gram TF-IDF, multilingual-E5-small
  and NeoAraBERT over each branch's Arabic image, definition and phrases, fused by reciprocal rank) find
  near-synonyms across roots: the same concept in two roots ranks 1–8. The parts of one scene rank far apart:
  among Fatiha's 124–141 branches, known scene partners rank anywhere from 2 to 92, and a top-3 pair list both
  misses real partners and admits generic ones. The distance finds a scene only when the definitions name it
  (a race: rank 5). Hence the new scene index (§3). The matrices are not used.
- **The channel reviews** (`network-v3/sNNN/review/reader_a_pilot.md`, 110 surahs, median 88 KB) contain real
  chains, but as an unranked taxonomy: S1 has 12 parent channels and about 40 subchannels, many of them noise.
  v15 shows only their titles, motifs and places, to the window reading, as a missing-chain check.
- **Turkish losses have no source.** The Turkish dictionary's gloss error profiles judge each gloss against its
  own branch ("namaz" for the ritual branch and "okumak" for the reading branch both lose nothing). Loanword
  drift is recorded nowhere. Hence Luna loanword cards (§3).
- **Concordance must be pulled or digested.** Fatiha's 18 roots have about 1.1M characters of full concordance
  (rabb alone: 871 ayat). Low-frequency lemmas (≤30 uses) are pushed as keyword-in-context lines; frequent ones
  get a Luna use profile, with every use available to pull.
- **Word alignment:** QAC word indices skip standalone pause marks (ۖ ۗ ۚ …). Counting them misaligns 18,025 of
  49,968 rooted occurrences; skipping them gives 0 mismatches and the standard 77,430 words.
- **Pericope boundaries can cut a trigger from its word** (a pericope boundary falls inside some neighbourhoods).
  So the ayah reading always sees a sliding ±7 window within the surah, whatever the pericopes.
- **Not used:** word-analysis prose (it carries "must_integrate" obligations: a worklist in disguise), HFT and
  v12 walks (earlier readers' hypotheses), bundles (about 0.8 MB per ayah), the grammar translation-support
  table (translation risks, not reading-relevant grammar; Opus reads the Arabic), embeddings, Hebrew Bible,
  and all earlier prose.

## 3. Data layer (built once, reused everywhere)

| Data | Built by | Source | Size |
|---|---|---|---|
| `data/quran.tsv`, `words.tsv` (77,430 words: root, lemma, POS), `lemmas.tsv` (4,657 lemmas with every use), `branches.tsv` (18,785 branches + Turkish concept gloss) | `build.py base` (5 s) | Quran text, QAC root table, Furūq table, Turkish entries | 16 MB, not committed |
| Alternative roots per word | script | the reviewed word-root analyses, plus qirāʾāt letter exchanges (ص/س/ز, ط/ت, ض/ظ) that land on an attested root | inline |
| **Scene index** (new): each branch → 1–4 scenes from a closed inventory of 140 concrete scenes (`data/frames_inventory.json`), each with the role the referent plays | Luna, 60 branches per job | branch image, definition and phrases (+ Qnet keywords as hints) | 178 jobs for the whole Quran |
| **Scene lines** (new): for a set of ayat, each scene with the words whose branches belong to it and their roles, ordered by distinct words, then roles | script | scene index | inline in packets |
| **Loanword cards** (new): per lemma, the Turkish loanwords, their modern senses, drift, what the reader hears, what the Arabic keeps (tied to branch ids), false friends | Luna, 25 lemmas per job | branch index | 187 jobs |
| **Use profiles** (new): per lemma with ≥31 uses, groups of uses by role, the dominant role with its count, uses outside it, collocates (descriptive only; an even sample of 400 above that) | Luna, 1 lemma per job | concordance | 295 jobs |
| Pull files: classical entries per root, every use of a frequent lemma | `build.py pull` | root packets (`entry_text_clean`), `lemmas.tsv` | per scope, not committed |

Scene tags are generous and multi-label, so they only order candidates; retrieval labels order and never filter.
A scene's parts come from different words. That is exactly what similarity misses and what an image is.

## 4. Stages (per surah)

| Step | Who | Reads | Writes | Stance |
|---|---|---|---|---|
| 0. data | scripts + Luna (once) | raw sources | §3 | supply |
| 1. window reading | Opus 5.5, effort high | window text, words, full branch index, scene lines (window, plus surah-wide ones for long surahs), channel titles, variants | `window.json`: images (members with ref + root Bnnn + role; containment; perceptible; interactions; movement), root concepts, movement, plan (≤3 images per ayah), other activations | generative |
| 2. ayah reading | Opus 5.5, effort high | ayah ±7, words, branch index (+alternatives), scene lines touching its words, its plan entry, concordance or profiles, variants, loanword cards | `record.json`: ground, findings (anchor, triggers, containment statement, perceptible, image, memory flag, lead/support/record), loaded words, losses, grammar, variants, reread, disclosed, set aside | generative |
| 3. evidence | Luna max | the record, cited branches with their classical phrases, concordance, related-passage list, the Quran text | `evidence.json`: per finding, attestation, trigger, QeQ (supports / expands / shifts / contradicts with refs), contradiction flag; missing passages | evidential; annotates only |
| 4. commentary | Opus 5.5, effort high, no tools | record, evidence, plan, Turkish glosses of the cited branches | `commentary.tr.md`, about 700 words, cap 1,100, `{{ar:…}}` for Arabic | communicative |
| 5. checks | scripts | outputs | anchors valid, containment wording, budget, a source for every Arabic quotation (`src:S:A:W` or `src:root Bnnn`) | — |
| 6. surah commentary | Opus 5.5, effort high, no tools | surah text, window reading(s), each ayah's ground, lead findings and reread | `surah.tr.md` | communicative |

Windows: a surah of up to 40 ayat, or one without pericope records, is one window. A longer one is read per
pericope, with surah-wide scene lines (≥3 words) that touch the pericope. The ayah reading's neighbourhood is
always ±7 ayat, crossing pericope boundaries.

Opus steps may read `v15/data` (Read, Grep, Glob only). They run in safe mode from a fresh temp directory, so no
CLAUDE.md, memory, skills or hooks reach them.

## 5. Rules kept by code

- Never rerun a completed unit. Never retry a failed one automatically; `--repair` allows one further attempt.
- Every call is logged in `out/ledger.jsonl`.
- Per-ayah Opus spend is capped at the $5 gate (`--max-budget-usd`). Window and surah passes have their own $5 caps.
- Luna runs `gpt-6-luna` at max reasoning, read-only sandbox, ephemeral, skill search off.

## 6. Parameters (`config.json`)

- Ayah prose: target 700 words, cap 1,100, at most 3 images.
- Neighbourhood: ±7.
- Keyword-in-context lines: lemmas with ≤30 uses, ±3 words.
- Definitions trimmed to 100 characters in packets. No branch is ever dropped: frequent roots keep their
  definitions, because they are where readers hear only one sense.

## 7. How to run

```
python3 build.py base                          # once (5 s)
python3 build.py jobs frames --surahs 1        # also: loanwords, profiles
python3 run.py luna frames --parallel 3        # Luna data for the scope (also loanwords, profiles)
python3 run.py window --surah 1                # Opus window reading(s)
python3 run.py discover --ref 1:6              # Opus ayah reading
python3 run.py evidence --ref 1:6              # Luna evidence notes
python3 run.py write --ref 1:6                 # Opus Turkish commentary
python3 check.py record --ref 1:6 && python3 check.py prose --ref 1:6
python3 run.py surah --surah 1                 # after all ayat
python3 run.py status --surahs 1
```

Any step takes `--dry` to show the prompt size and command without calling a model.

## 8. Evaluation

Judge by the reader criterion, on named cases and on blind ayat together: similar performance on any ayah must
be shown, not assumed. The mechanical checks (§4, step 5) run on every output. Comparisons are done directly
(no comparison agents).
