# Commentary v10 — semantic prototype

The target is Turkish prose that changes how a reader understands the focus
ayah: connected image chains, Quranic resonances and consequential comparisons
made intelligible to someone who does not know Arabic. Finding counts and
citation counts do not measure that achievement.

This version consists of local evidence preparation and two prompts. A reader
proposes connected readings in a plain brief. Preparation retrieves their
complete original sources. A writer develops the reading for the reader. The
writer can also receive the broader evidence directly. Luna Max and Sol Max
are the intended first candidates; the prompts are also usable with Opus.
**Comparable prose quality and total cost savings remain unproved.**

There is no model runner, retry cascade, coverage ledger or automated semantic
acceptance gate. Preparation never starts an agent. The production default is
unchanged. See the [pilot report](experiments/2026-09-25/REPORT.md) for actual
results and [design notes](DESIGN.md) for the semantic choices.

## Local preparation

Run from the repository root. Defaults use the sibling `quran-data` and
`quran-slm` checkouts. Python 3.14 supplies the zstd reader for ayat without a
saved bundle; NumPy enables retrieval from the existing rank matrices.

Prepare the reader's evidence and prompt:

```bash
python3 -m _commentary.v10.prepare --ayah 18:86 \
  --out _commentary/v10/work/18_86-reader
```

Inspect `sizes.json` and `reader.prompt.md` before any separately authorized
model run. Save the resulting brief as Markdown, starting `Focus: 18:86`.
Then prepare the writer's prompt from the sources cited in that brief:

```bash
python3 -m _commentary.v10.prepare \
  --evidence _commentary/v10/work/18_86-reader/evidence.json \
  --brief path/to/reading-brief.md \
  --out _commentary/v10/work/18_86-writer
```

Omit `--brief` to prepare a direct writer with the broader evidence. Output
directories must be new. Byte counts describe prompt size, not billed tokens.
Work artifacts and decompression caches are ignored by Git.

## Evidence choices

- `--upstream auto` uses available HFT, reviewed subnetworks and reader walks.
  Missing HFT or an ayah bundle is allowed.
- `--upstream no-hft` retains the other upstream readings. `--upstream none`
  omits all three kinds of upstream interpretation, keeping canonical linguistic
  analysis, dictionary sources, Quranic text and scripted network candidates.
- Selecting a source reading retrieves the whole chain and its cited branches.
  Separate subnetworks can contribute to one mechanism, including S1's weather,
  gathered water, well and means of access.
- Rare roots receive complete Quranic usage panels, including different
  derivatives. These panels survive reduction even when the brief overlooks
  them. Common roots receive counts, lemma distinctions and selected contextual
  comparisons; exhaustive occurrence lists remain on disk.
- Every writer receives the full surah and Fatiha. External references receive
  two neighbouring ayat on each side. A brief can cite additional references
  when this starting window is inadequate. Earlier inter-ayah relevance verdicts
  stay in the archive and do not appear in model input.
- Three distinct neighbouring roots per focus branch are retrieved from the
  existing rank ensemble by default. Whole supplied chains are preserved
  independently of that limit. `--network-k 0` exposes the full catalog; missing
  rank data also falls back to it with a warning. Inspect size before use.

Numbered ayat are supported. Source preparation has been exercised without HFT
and without a focus bundle, including 2:255. That establishes source access,
not interpretation quality. Long-surah input can still be large, and similarity
retrieval can miss complementary images. No 2,000-ayah production run is ready.

The next useful step is a small prose comparison when model quota permits.
Judge whether the main discoveries develop a changed understanding, whether
Arabic and citations support the reading, and whether repetitions obscure it.
Measure the whole workflow, including failed calls, before claiming savings.
Tell the user before starting another agent; do not impose an automatic time
cutoff on Luna Max.
