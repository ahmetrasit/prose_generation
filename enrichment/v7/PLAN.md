# Enrichment v7: verse digests first, page writers after

Status 2026-10-07: **Luna vs Sol digest test running** (`work/test-20261007`). Supersedes `enrichment/v6/PLAN.md`.

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

**Stage 2: page writers.** They run once every digest a page needs exists.
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

## Step 1: Luna vs Sol (running)

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
