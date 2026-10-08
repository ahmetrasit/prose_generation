# Enrichment v7: verse digests first, page writers after

Status 2026-10-07 evening: **decided workflow below (focus ayah only)**; everything after it is history. Supersedes
`enrichment/v6/PLAN.md`. Review that led here: `REVIEW_optimum_2026-10-07.md`.

## Decided workflow (user, 2026-10-07)

**Scope**
- Enrich the **focus ayah only**, from the reading's initial findings. The base is the r13 reading **without augment9**.
- Cited verses get **no digests and no blocks**. The sources' own links (`mentions`) carry those connections; later,
  a page link.

**Models (decided)**

| Step | Model | Unit |
|---|---|---|
| Tier 1 | **Luna max** | per source segment, 20k-character chunks |
| Tier 2 | **Sol high** | per focus ayah |
| Writer | Opus high or Astra high (open) | one call per ayah |

**Tier 1 (`digest.py`)**
- Material:
  - the ayah's verse-tied commentary segments;
  - the **quotation packet** (`--quotes`): works with no verse index that quote the ayah's own words.
- Surah-level segments are printed and reserved for the surah page.
- Checks: every segment answered; every anchor verbatim.
- Status: done for the own ayat of S1 and S87–114. Quotation packets are still to run, except for 103:1.

**Tier 2 (`merge.py`)**
- Input: all of the ayah's tier-1 notes, with the full-edition rule applied.
- Output: each distinct view once, with its holders, stances and disagreements.
- Check: every note is in at least one view.

**Writer** (focus mode; brief and `write.py` mode still to be written and shown to the user)
- Input:
  - the reading without augment9, with `[¶n]`;
  - the ayah's views;
  - all Turkish meals.
- Output:
  - one block per question, after the first paragraph that raises it, plus a closing group;
  - at most about 150 words per block and about 900 per ayah.
- Check: every view is cited in a block or listed as omitted with a reason.
- Render: blocks link to the views, the views to the notes and exact words, the notes to the locators. Strip check:
  removing the blocks gives the frozen page back byte for byte.

**Later**
- A word stage keyed by term or root: hadith collections, poetry, term encyclopaedias. Until then each page states
  they were not consulted.
- Surah-level material goes to the surah commentary page.

**Dropped**
- Cross-reference digests and blocks (`s103-1/tier2` and `pilot100-20261007` are not run).
- Writing against augment9.
- The paragraph × cited-verse ledger.
- Giving the writer the full tier-1 notes.

**Model trials on 103:1** (`work/s103-focus`; API-equivalent)
- **Haiku 5.5, tier 1 on the quotation packet:** 196 rows, check OK, $0.13; faithful in a 9-row spot check. Not
  tested on dense tafsir. Luna is kept for tier 1.
- **Sonnet 5.5, tier 2:** 393 → 102 views, check OK, $0.78; distinct views kept (Bint al-Shāṭiʾ's reading,
  Biqāʿī's). About 2.5× Sol's cost, so **Sol is kept for tier 2**.

## Results of the test (2026-10-07)

| Tier | Model | Result | Cost (API-equivalent; actual $0 on Codex) |
|---|---|---|---|
| 1, per source segment (`digest.py`) | Luna max, 7 chunks | 163 segments → 1,221 rows. Read against the source for Ṭabarī, Naḥḥās, Islāḥī, Elmalılı, Bursevī, Qāshānī: faithful, correctly attributed; one small slip (the Baṣāʾir derivation given to Elmalılı). 3 anchors in c04 left failing; 5 of 7 runs over the 120k context cap (brief fixed since: write once, never stop while the check fails) | $0.76 (≈ $800 for the whole Quran) |
| 1 | Sol high | stopped by the user; c07 only: same content, slightly better merging and attribution | c07 $0.12 vs Luna $0.035 |
| 2, per ayah (`merge.py`) | Sol high | 308 → 85 views (100:1), 205 → 88 (87:6); every row covered; disagreements, reasons and minority views kept | $0.28 + $0.20 |
| 2 | Luna max | 64 and 72 views; every row covered, but distinct arguments were buried in broad views (26 rows on 100:1, e.g. al-Rāzī's horseshoe argument for horses, Abū Ṣāliḥ's authority argument for ʿAlī's camel reading) | $0.05 + $0.03 |

- Tier 1 cannot do the consolidation: most of it is across sources (the horse view sits in about 40 sources), and
  a tier-1 agent sees only its chunk.
- Tier-1 size is not reduced. Merging is tier 2's job, and merging earlier would lose detail tier 2 needs.
- Tier 2 renders compactly: source ids, the speaker only when he is not the author, `+` prefers, `-` rejects.
  That is ≈ 22–24k characters (≈ 5–6k tokens) per ayah.
- Proposed per ayah: tier 1 Luna ≈ $0.13 + tier 2 Sol ≈ $0.24 ≈ **$0.37**. Whole Quran ≈ $2.3k API-equivalent.

**Principle (user, 2026-10-07): keep it simple.** Agents get the right, complete input and the right instructions;
that is enough. There are no hashes, validation layers or second-model passes. Only two checks are kept, each a few
lines of script, because they catch failures that actually happened:
1. **Every segment answered.** In v5, Codex clipping made an agent skip half its input, and killed runs left
   files half-written.
2. **Every anchor verbatim in its segment.** Anchors become quotes in published prose.

## Why (measured 2026-10-07 from run records and corpus.sqlite)

- **Agent loops drove the cost.** v4 1:6 Sol high, $19.80:
  - re-reading context on every turn: 62%;
  - new input: 23%;
  - output: 14%.
- **The page's cross-references drove the volume.** Only 11–12% of what v4 cited was on the page's own ayah.
  Pages cite a median of 171 verses (S1/S87–114).
- **An ayah's own material is small.** Median by surah:
  - S100: 103k characters;
  - S87: 119k characters;
  - Fatiha: up to 1.12M characters.
- **Every verse is some page's own ayah eventually.** So reading each verse once and reusing the result is never
  wasted.

## Design

**Stage 1: digests.** A database of notes, one entry per source segment.
- Each entry carries the segment's verse range and is looked up by ayah. A passage covering 2:1–5 is read once.
- Kinds covered: tafsir, tafsir_tr, maani, nazm, isari, modern, qiraat, ulum, reference, sira.
- **Edition rule:** where a full edition exists (X-FULL), the short one (X) is not used for that verse.
- **Agent input:** whole sources packed into chunks of at most 40k characters, one fresh context per chunk, read in
  10k-character parts.
- **Agent output:** one line per segment, holding one row per point:

  | Field | Content |
  |---|---|
  | `verses` | the verse(s) the point is about |
  | `speaker` | who holds the view |
  | `stance` | holds / prefers / reports / rejects |
  | `claim` | one English line |
  | `anchor` | 5–25 exact words |
  | `mentions` | other verses the point quotes or names |

  A segment with nothing to record gets `none` and a reason.
- **Instructions:** one brief (`briefs/digest.md`) with a short guide per kind of source. The output format is the
  same for every source.
- **Meal:** a script table of distinct renderings per verse, with their translators. No model.
- **Later stages:** poetry, lexicon, wujuh and grammar are keyed by Arabic root; hadith by key term or matn.
- **Not yet covered:** surah-level segments (introductions, maqṣūd: segments with no ayah number). They will get a
  surah key.

**Stage 2: page writers** (`write.py`, brief `briefs/write.md`; user principle 2026-10-07).
- **The block is a map, not the account.** The enrichment is the reader's one-stop shop. From a block alone the
  reader knows:
  - which question the sources answer;
  - every position that bears on the paragraph's point, and who holds it;
  - the deciding reason or disagreement.

  The reader then decides whether that is enough or opens the details. Details are linked: block → tier-2 views
  (`<ayah>/vNNN`) → tier-1 notes (claim, exact words, locator) → the source passage. Every decision follows this
  principle.
- **Length ceilings:** own-ayah blocks ≈ 150 words; cited-verse blocks ≈ 60 words.
- **Topic blocks, not family sections.**
- **Minor variants are counted, not spelled out.**
- **`no_match` rows** stay in the ledger and are not shown to the reader.
- **Inputs, by script:**
  - the page with `[¶n]`;
  - the own ayah in full (notes and anchors), plus its views;
  - the views of each cited verse.

  The paragraph groups fit one context (`--budget` characters of cited views).
- **Checks:**
  - every (paragraph, cited verse) pair has exactly one ledger row;
  - the ids cited were in the input;
  - quoted Arabic is in the anchors of the cited notes.
- **Render:** blocks after each paragraph (after its augment blocks), linked to `views/<ayah>.md`. The strip
  check gives the frozen page back byte for byte.
- **Writer model:** Opus 5.5 high (agent `enrich-page-high`) or Astra high (Codex); a side-by-side decides.
- **Before the principle (kept for the record):** They run once every digest a page needs exists.
- A writer covers a group of paragraphs. It reads:
  - the page;
  - the own ayah's full text;
  - the digest entries for the verses those paragraphs cite.
- Every cited verse is covered: a block, or `no_match` with a reason. There is no cap.
- Writers make the connections between sources and verses.

## Files

| File | Role |
|---|---|
| `digest.py build RUN --ayat … --models model:effort …` | gathers segments, writes chunks, parts and spawn files, and `manifest.json` (every skip listed) |
| `digest.py check RUN [--model TAG] [--chunk N]` | the two checks (agents run it on their own chunk until `OK`) |
| `digest.py report RUN` | runs, API-equivalent cost, requests, peak context, rows, digest/source size |
| `run.sh RUN SPAWN…` | seven agents at a time via `enrichment/v5/run_codex.py`; commit and push after each batch |
| `briefs/digest.md` | the digest brief |

## Step 1: Luna vs Sol (done; results above)

- **Material:** the own material of 100:1 and 87:6: 163 segments, 7 chunks, 247k characters, 47 sources.
- **Models:** Luna `gpt-6-luna` max and Sol `gpt-6-sol` high. Same chunks, same brief, 14 agents in two batches.
- **Comparison, by reading:**
  - completeness: points one model has and the other misses, checked against the text;
  - correct attribution: speaker and stance;
  - compression;
  - cost.
- **Estimated cost (API-equivalent):** Luna ≈ $0.3–0.5, Sol ≈ $6–8. Actual cost is $0 (Codex).

## Next

1. Choose the digest model from step 1.
2. Pilot on 100:1: digests for the 32 verses it cites, the meal table, one page writer.
3. Digests for the S1/S87–114 scope, then writers.

## Open

- The writer model.
- Prose volume per page and per cross-reference block.
- Whether writers wait for the later stages (root, hadith).
