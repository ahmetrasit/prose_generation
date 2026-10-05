# Adversarial review of the A–F change plan (2026-10-05)

Read-only review of grup.py at 19ef9ed09, groups.json, the briefs, and the S1/S87 plans. No model was called.
Scratch scripts are in /private/tmp/claude-502/adv/ (m1–m6). Material was rebuilt with `group_items` (read-only DB).

## 0. Verdict
- **Build:** B (inline material for Astra), F's line format and its pointer-completeness check, and a narrowed D.
- **Drop:** A, C and E as written.
- **Replace the core:** units should not place blocks at all. A per-group unit extracts positions without the base.
  Then one placement call per page reads the full page once, together with every group's lines for that page.
  That call places them, merges the same position across groups with all pointers kept, and marks what the base
  already says.
- **Why:** this removes the digest instead of shrinking it. It is the only design here that removes cross-group
  duplication; F only reorders it. It also costs less than A–F (§4).

## 1. Measurements

| | S1 | S87 |
|---|---|---|
| unit start context (plan.json) | 4.92M | 4.55M |
| of which digest | 1.82M (37%) | 3.06M (67%) |
| digest of each page, once | 75k | 169k |
| digest re-read factor | 24× | 18× |
| full numbered pages | 253k | 519k |
| [¶] paragraphs | 253 | 519 |
| digest tokens per [¶] (augment prose and "Ayrıca" lines included) | ~295 | ~326 |
| units touching page 1:1 | 28 units, 22 groups, 329 segments, 1.1M chars | |

**Cross-group repetition on 1:1.** I counted segments of the 1:1 material holding Arabic marker strings. This is a
keyword proxy, so it overcounts passing mentions, but the order of magnitude holds.

| position (base ¶) | groups | sources | segments |
|---|---|---|---|
| ism < sumuww (¶5) | 9 | 25 | 39 |
| ism < wasm/sima (¶5) | 10 | 25 | 33 |
| ism = musammā | 9 | 21 | 31 |
| elided verb: abdaʾu/aqraʾu, mutaʿallaq (¶1–2) | 12 | 34 | 69 |
| meaning of the bāʾ | 9 | 16 | 18 |
| basmala an ayah of the Fātiḥa | 7 | 14 | 28 |

So the same position reaches **5–12 independent units**. Under the current brief, each unit writes its own block.

**Output is mostly thinking.** In the dosya2 trial, measured output was 131.7k tokens. The records themselves were
only about 17k of that (REVIEW_grup §3.1). Shorter record text therefore saves little money. A format change is
worth making for granularity and pointers, not for cost.

## 2. A–F, one by one

### A. Claims index — drop
- **Its size is underestimated 2–3×.** An exact anchor (~15 tokens) plus the paragraph's claims (40–60 Turkish
  words, ~70–90 tokens) is about 100 tokens per [¶].
  - S1: 26k (3.3k per page; the surah page alone is 7.5k).
  - S87: 54k (2.7k per page), not 1–1.5k.
  - Summed over units, S87 comes to about 0.97M, not under 0.5M. Add 20 index calls of about 0.7M input.
- **New silent path.** The index is a model's paraphrase of the frozen base, and every unit sees the page only
  through it. A claim it leaves out, typically one in an augment block or an "Ayrıca" reference line, cannot be
  matched by any unit. Nothing checks the index's claim coverage, only its anchors.
- **Ordering dependency.** One failed index call blocks every unit of that page.
- **The anchor half needs no model.** A script can take an exact anchor (the first words of the ¶) straight from
  PACK/numbered.

### B. Inline material for Astra — build
- It removes Codex truncation of reads, which is a real silent path: finish only detects it afterwards. It also
  removes the read turns.
- **Traps:**
  - Feed the prompt through stdin. `codex exec "$(cat prompt.md)"` passes the 300k-token prompts (S87 meal is
    roughly 0.7M characters, Arabic at 2 bytes each) through the argument list, and macOS caps that at 1 MB
    (ARG_MAX).
  - Tell the agent not to re-read the copies on disk.
  - Corpus tool outputs still pass through the shell. Keep `--chars` below the Codex cap; corpus.py already marks
    its own cuts.
- The Opus path keeps the files.

### C. Ayah-only meal units plus a verdict unit — drop
- The S87 meal unit is 309k only because of the digest (124k material + 169k digest). Without the digest it is
  about 135k: one unit, as now.
- The split also costs:
  - 19 extra units of fixed overhead;
  - the cross-ayah view the meal brief needs ("judge patterns, not slips");
  - one more ordering dependency.

### D. Untied citing segments become pointers — narrow it
As written it would hit groups whose material is all citing segments:

| group | S1 | S87 |
|---|---|---|
| akademik (all citing) | 122 segments, 175k | 89 segments, 118k |
| beyani-huli (required voice) | 10 segments, 20k | 12 segments, 12.8k |

On S87, beyani-huli's citing segments are where the required bayānī voice comes from (REVIEW_grup §1.2). Making
them pointers recreates that loss. The real waste is index pages:
- S1 modern-bati: 51 of its 66 citing segments (62.5k of 73k tokens) have more than 0.15 verse references per word,
  i.e. Study Quran index pages (sampled: STUDYQURAN:p4051 is a list of divine names with verse numbers).
- S87: 18 of 23 (20k tokens).

A deterministic index-page filter, printed and recorded as "listed, not read: index page", removes about 85% of the
problem. It involves no model judgment and leaves akademik and bayānī untouched. The 0.15 threshold should be
checked by eye once.

### E. Errata unit — drop
- 130 of S87's 133 candidates are "arabic outside tags": bare Arabic words in the prose, mostly cosmetic.
- 2 are dictionary-branch quote mismatches. Checking those needs PROJE or the lexica, which are not_read (user
  decision).
- 1 is a Qur'an quote.
- **Instead:** a script triages the formatting flags, and the 3 substantive ones go to that page's placement call
  (or to the user).

### F. Theme lines expanded by script — keep the format and the check, not the theory
- **Good:**
  - One line per position, with all locators in `k`, is finer-grained.
  - "Every kullanildi/tekrar locator appears in some kept k" closes a current loss. Today a `tekrar` segment's
    pointer appears in no record.
  - Expansion needs no schema change. `check_records` takes plain dicts and `gelenek` is set by default.
  - If a script fills `capa` from the numbered page, the capa-mismatch drop path disappears entirely.
- **Does not solve the core problem:**
  - Within a unit, "a repeat adds a locator" is the current `tekrar` rule under another name.
  - Across units, the ¶5 sumuww position still yields up to 9 lines from 9 groups, each with partial `k`.
  - Free slugs written by independent agents ("ism-kok", "ism-istikak", "sumuw-vasm") have no shared vocabulary.
    I cannot test agreement without runs, and nothing in the design forces it. Even when the keys match, the result
    is 9 adjacent near-identical sentences: reordered, not deduplicated.
- **Silent defaults.**
  - `iliski` by material type is wrong for a thematic hadith quoted inside a tied tafsir.
  - `kat:ek` is wrong for a primary point.
  - Every defaulted field must be listed per record (provenance) and counted by finish (priority 1).
- **Hidden arguments.** "A distinctive argument becomes its own arastirma line" hides it by default. Use `ek`.

### A loss in the current brief (not in the plan)
The brief says "Do not restate the base", and `yeni_yok` means "nothing beyond the base". A source that attests the
base's own claim therefore leaves the page. In the author's ¶5 example, the Basran sumuww line
(WAHIDI-BASIT:v1p439) is exactly such a pointer. Under priority 2 the advanced reader wants it ("it has been
discussed; here is where"). Whatever is built, attestations of the base should become compact pointer lines, not
disappear into kapsam.

## 3. Is the per-group unit right?
- **For reading, yes.** One page's material is up to 0.7M tokens (1:1: 1.1M chars), so no per-page or per-theme
  call can read the sources. Source-first reading, grouped by tradition, is forced by volume.
- **For writing, no.** "Every theme once per paragraph, with all pointers" is a per-page property. Units that never
  see each other cannot produce it, and F's sort key cannot either.
- **Placement is also done in the wrong place.** Each of the 28 units touching 1:1 pays for a digest so it can
  choose a ¶. The page is then effectively read 28 times at 30% fidelity, instead of once in full.
- **The fix:** split reading from placing.

## 4. Alternative: extract, then place (X)

### Stage 1: per group unit
- Packing is the same as now, so the budget, required voices, `unit: surah` and kapsam all carry over.
- Inputs: the material plus page headings only (deterministic, S1 4k / S87 8k). No digest.
- The agent writes one line per position:
  `{"pg","w","t","f","k","a","m"}`
  - `w` is the ayah word(s) as QAC refs from binding.json (e.g. 1:1:1), or "ayah" or "surah". This is a closed
    vocabulary that independent agents will agree on.
  - `m` is at most ~40 words.
  - A repeat within the unit adds its locator to `k`. Distinct positions or holders are never merged.
- kapsam is one line per segment, as now, minus `yeni_yok`: whether the base already says something is not stage
  1's call.
- One check command: locators resolve, `w` is valid, the required voice is present on each page or a reason is
  given. No ¶, no capa.

### Stage 2: per page (S1 8 calls, S87 20)
- Inputs: the full numbered page once, plus all stage-1 lines for the page, sorted by the script by `w` then `t`.
- Output:
  - per line: ¶ and `kat`, plus an `islev` override relative to the base (destek/oncul/itiraz);
  - per cluster of the same position across groups: the ids and one new `m` naming every holder;
  - the base's ¶ claims that no line touches. These become the oncul unit's input in place of 20 digests, which
    makes oncul feasible (REVIEW_grup §3.2).
- The script then:
  - checks that every input id is accounted for exactly once (placed, merged, moved to another page, or rejected as
    `elenen` with a reason);
  - unions `k` and `a`, so no pointer can be dropped by a merge;
  - fills capa from the ¶;
  - expands the lines to full records with every default recorded, then validates and renders with the existing
    code.
- The original lines stay in provenance.

### Tokens
Start contexts come from plan.json and the scripts. ctx×turns assumes 6+2·pages turns for the current design,
6+pages for A–F and 5 for X, so treat it as a sensitivity figure only. The $ column is at Opus rates with the same
output rule for every design (0.5 × material + 15k per call).

| | current | A–F | X |
|---|---|---|---|
| S1 calls | 46 | 62 | 54 |
| S1 start context | 4.92M | 4.08M | **3.44M** |
| S1 ctx×turns | 75M | 38M | **17M** |
| S1 $ (Opus) | ~87 | ~81 | **~71** |
| S87 calls | 28 | 68 | 48 |
| S87 start context | 4.55M | 3.46M | **2.31M** |
| S87 ctx×turns | 160M | 49M | **12M** |
| S87 $ (Opus) | ~79 ($4.1/ayah) | ~66 | **~45 ($2.4/ayah)** |
| largest unit S1 / S87 | 205k / 309k | 156k / 141k | 130k / 144k (meal) |

- The stage-2 calls are 42–86k tokens; the biggest are the S1 surah page and 1:1.
- S1 stays above $10 per ayah in every design, because thinking over 2.4M tokens of material dominates.

### Failure modes of X
1. **Over-merging:** the nuance of one holder is lost in a cluster's sentence. Mitigations:
   - merge only identical positions, and the `m` names every holder;
   - pointers are kept by construction (script union);
   - originals stay in provenance;
   - spot-check clusters of three or more.
2. **Misplacement.** Same risk as now, but judged from the full page rather than a 30% digest.
3. **Stage 1 cannot see the base, so it writes positions the base already holds.** This is intended: they become
   pointer lines. Expect more lines, the very ones priority 2 asks for.
4. **Stage 2 waits for all of a surah's stage-1 units.** The current merge waits the same way.
5. **Some arguments are framed against the base's reading (`itiraz`).** Stage 2 decides these, from the argument
   carried in `m`. It may open a locator.

### Build cost
- A stage-1 brief: grup.md minus anchoring and minus "do not restate", plus the line format. Shorter than now.
- The line expander. F needs it anyway.
- A placement prepare/finish: prompt build, id accounting, k/a union, capa fill.
- `merge` and `render` are reused.
- A, C and E are not built. The total is about F alone plus one prepare/finish pair, fewer moving parts than A–F.

## 5. Ranked recommendation
1. **Now, independent of design:**
   - B (stdin, no re-reads);
   - narrowed D (index-page filter, recorded);
   - pointer completeness for `tekrar` and attestations (end the `yeni_yok` pointer loss);
   - record every default.
2. **Build X:** the stage-1 brief, the expander and the placement step. Drop A, C and E (errata by script triage,
   with the 3 substantive ones sent to stage 2 or the user).
3. **Test first, with 4–5 Astra units, on 1:1, the page with the heaviest overlap:**
   - Stage 1: rivayet.u02 (1:1 only), dirayet-cami.u03 (1:1, 57 segments) and dirayet-kesşaf.u01 (1:1–1:4).
   - Stage 2 on 1:1.
   - Compare with zengin.1_1.opus.high (53 records) on four counts:
     - reference points recovered;
     - clusters formed and pointers per cluster;
     - attestation lines;
     - mis-merges found by hand.
   - Optional fifth unit: dirayet-kesşaf.u01 under the current grup.md, as the head-to-head on duplication and
     tokens.
   - Then S87 nazm-bikai (whole surah) plus stage 2 on 87:1, to test the required voice with no digest.
4. **Keep the plan's evidence rule:** every Astra run records its tokens and truncations against these estimates.
