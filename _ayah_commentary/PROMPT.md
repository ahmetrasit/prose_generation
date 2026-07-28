# Ayah Commentary Prompt — layer 2

Read `../PRINCIPLES.md` and `../COMMENTARY_SPEC.md` first. They govern. This file
is the task.

---

## Task

You are given the input bundle for one ayah. Write commentary that makes a
reader understand **this ayah, on its own terms**.

An ayah is a unit people meet alone. It gets memorised, quoted, written on a
wall, encountered without its neighbours. Your reader may have no intention of
reading the whole surah. Write for that person.

Your reader has almost no Arabic grammar and reaches Arabic words through Turkish
loanwords that have shifted, narrowed, or lost their meaning. Assume nothing is
obvious. Assume also that they are not fragile — they want the real thing, and
they want to keep their footing while getting it.

## The question you answer

**What happens here?**

Not "what does the surah argue" — that is layer 3's job, and if you answer it you
have written the wrong document. Concretely, ayah level covers:

- what this ayah *does* as an act: asserts, suspends, answers, excepts, swears;
- what its grammar forces before any lexical content is weighed;
- **what each word contributes to building the ayah**, including everything the
  reader's languages cannot render — Turkish has no definite article, English
  cannot double one, and `الصِّرَاطَ الْمُسْتَقِيمَ` has two. That doubling is invisible
  in every translation your reader will ever see, and it is doing work;
- what its form selects, and what that selection excludes;
- what its sound does, if the bundle records it;
- what genre or pattern the reader recognises before understanding it;
- what it holds that a whole-surah reading has no room for.

## What counts as an activated reading

The bundle answers this; do not decide it yourself. Each `word_analysis` topic
carries `commentary_obligation`:

- **`must_integrate`** — obligatory. Every one appears in your commentary. This is
  the set "you must not select" refers to, and it is checkable.
- **`candidate`** — discretionary, and this is where the surprise lives. Topics
  with `status: narrowed` are the non-primary pressures on a word, and in the
  cases measured so far **every one of them is `candidate`, none are
  `must_integrate`**. A commentary that honours only its obligations will be
  competent, complete, and hold no surprise at all. Read the `candidate` topics
  before deciding.

Each topic also carries `reader_payoff`, stating what the reader gains. Use it as
a test: if you cannot make that payoff land, the topic is not yet written.

Branch inventories, reader walks, channel review, and the channel generated
output manifest nominate material that has no topic. That material is admissible
when it is in the bundle. If `channel_generated_outputs` lists quran-data files
and your run gives you file access, you may read only those listed files when a
channel-family or path detail is necessary. Do not browse the repository
generally. If your run is hermetic and the files are not inlined, treat the
manifest as awareness and do not invent their contents.

## You must not select

This is the defining constraint of this level.

Layer 3 is allowed — required — to build a thesis, and a thesis excludes. You are
the opposite. **You carry the full field.** Every activated reading in the bundle
that survives review appears here, including ones no surah thesis could use.
Including ones that pull in different directions.

If two activated readings do not reconcile, say both. Do not adjudicate, do not
rank, do not pick. Readings at the same depth coexist.

This is where the no-disambiguation guarantee actually lives. If you select, the
guarantee is gone and nothing else in the system restores it.

## Connect; do not catalogue

Your reader already has the catalogue. They cannot use it — assembling activated
readings into something that means anything is exactly the work that requires the
Arabic they do not have.

So a list of readings is not an answer, even a complete and correct one. Show the
readings meeting each other. Multiple branches of one root are usually facets of
one concept: find the concept (`PRINCIPLES.md` §8).

If your output has one section per activated reading, you have reformatted the
bundle.

## Keep the reader's feet on the ground

Grounding (`PRINCIPLES.md` §5) is a hard constraint here, not a matter of tone.

- The primary reading stays reachable at every point. The reader must never lose
  track of what the ayah plainly says.
- Every resonance enters through a word already in front of the reader, in a form
  they have already been given. Nothing is announced from above.
- Containment is at sentence level: `X — as Y`, never `not X but Y`.

An ungrounded reveal is a rejected output even when every claim in it is true and
traceable.

## Channel increments

What you may do with channel material depends on what exists. Check the bundle.

**State A — an adjudicated ledger exists.** Carry a channel **increment**: the
part of the channel that has matured by this ayah, entered through this ayah's
own word. Say only what has matured here — not the channel's eventual shape.
Withholding the rest is the mechanism, not a loss. A channel at `latent` maturity
is not mentioned at all.

Rules and a worked S1 example: `../docs/CHANNELS.md` §3.

**State B — only `channel_subchannels_anchored_here`.** This is today's state for
every surah. It is a first-pass, single-reader review: no accept/reject, no
second reader, no maturity. There is no maturity to bound you, so the increment
rule cannot be applied and you must not improvise a substitute.

Some bundles also include `channel_generated_outputs`, a manifest of generated
network-v3 files such as `channel_candidates.jsonl`, `channel_families.jsonl`,
`family_branch_inventory.tsv`, and semantic path-family summaries. These files
make channel candidates and families available for inspection, but they are not
an adjudicated channel ledger. They may clarify which candidate family or branch
connection a first-pass review is drawing on; they do not license naming an
established channel, asserting maturity, or choosing between live readings.

What you may do: let the material inform **how you connect this ayah's own
words** — it often shows which branches belong to one image.

What you may not do: name the channel as an established image of the surah. Not
"bu sûrede bir yol imgesi sürüyor". A channel claim asserted from a first-pass
review is exactly the unearned authority `PRINCIPLES.md` §2 forbids, and the
reader cannot tell the difference.

Mark any channel-informed connection as your own reading in the evidence surface.

Do not state the surah's thesis. An increment is anchored in this ayah's lexis
and bounded by maturity; a thesis is neither.

## Before and after

Ayah level has something surah level cannot have: **the ayah existed before its
neighbours did.**

If the bundle contains v12 reader responses, they record exactly this — what the
ayah yielded in isolation (`stage_00`), and how that changed as neighbours were
revealed (`stage_01`, `stage_02`), including `changed_reading{before, after}` and
per-stage `status`/`confidence` movement.

Render this as reading experience, not as measurement:

> Bu âyet tek başına gösterildiğinde … Sonra hüsran açıldı, sonra istisna — ve
> iki okuma da yerine oturdu.

Never as: *"three readers at exploratory confidence converged on two models."*

If the reader walks record *retrospective surprises* — readings that only became
visible after a later ayah — those are the highest-value material at this level.
They are literally the shape of understanding arriving late.

**If reader responses are absent, say so.** Do not infer what they would have
contained.

## What the others dropped

You are the terminus for every exclusion in the system (`PRINCIPLES.md` §6).

- Layer 3's thesis excluded readings. Those are yours; pick them up explicitly.
- Layer 1 selected one branch per rooted stem and rejected others
  (`consideredNotPrimary`). Those are yours too.

They are not errors and not leftovers. They are readings that a selection had no
room for.

## Voice — say what the word does

Write in positive predication. State what a word does and let what it does not do
be inferred.

Two forces in this project push the other way, and both must be resisted at the
sentence level. Containment (`PRINCIPLES.md` §4) is phrased as a prohibition, so
it is tempting to discharge it by narrating what is *not* happening. And the
`reader_payoff` fields in the bundle are themselves written that way — "deepens
the route *without replacing it*", "*do not* become the local sense". That is
analyst's register. Do not inherit it.

In Turkish this matters more than in English. Stacked `-maz / -mez / değildir /
yoktur` constructions read as hedging and break the flow. Turkish carries
contrast through `zaten`, `hem… hem`, `-ken`, `ayrıca`, and through simple
juxtaposition.

| instead of | write |
| --- | --- |
| Bu âyet bir şey bildirmez, bir şey ister. | Bu âyet bir istektir. |
| Türkçede bunun karşılığı yoktur. | Türkçe burada tek bir "ilet" ile yetinir. |
| Âyet yolun düz olduğunu ileri sürmüyor; hangi yol olduğunu söylüyor. | Âyet hangi yol olduğunu söyler: o yol, o bilinen dosdoğru olan. |
| Yolun doğru olması, üzerinde kimsenin beklemediği demek değildir. | Doğru yolun üzerinde de bekleyenler vardır. |
| Ayakta durmak, işlemeye devam etmek demek değildir. | Biçim yerinde kalırken işlev çekilebilir. |

Use an explicit negative predicate only to correct a likely misconception,
protect the primary sense from replacement, or preserve live counter-evidence.
The instruction is to stop negation dominating, not to eliminate it. Prose with
almost no explicit correction can read evasive when the reader is likely to
expect the wrong sense. If no explicit negative is needed, say in the friction
report that there was no live misconception, replacement risk, or counter-evidence
requiring one.

## Arabic word surfaces

Reader and listener editions need different surfaces. In authored prose, mark
Arabic lexical items with a structured span when the Arabic word itself matters:

```text
{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar}
```

Here `ar` is the Arabic surface form for TTS and exact display, `tr` is the
Turkish-readable transliteration, and `gloss` is the target-language meaning.
The reading edition may render this as `el-âdiyât (ٱلْعَادِيَاتِ),
"koşup atılanlar"`; the listener edition may keep only the Arabic surface form
where the TTS voice should pronounce Arabic.

Use the span at first mention of an ayah word, and again whenever the prose
returns to that word after moving to another word or another paragraph. A later
renderer may hide repeated `ar` or `gloss` fields, but the authored file should
keep enough structure for reading, display, and TTS editions to be produced from
the same text. Inside one short local sequence, after a full span has just been
given, a Turkish label or transliteration is enough.

Do not display roots as spaced Arabic letters or letter-by-letter
transliteration in prose. Anchor root discussion to the surface word instead:
`{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar} kelimesinin bağlı
olduğu kök alanı...`, not `ʿ-d-w kökü...`. Raw roots, branch IDs, and root
skeletons belong in the evidence surface.

## Structure

There is no fixed section list, and section headers named after evidence layers
are forbidden. Let the ayah's own shape decide. A single-word ayah and a
twelve-word ayah do not have the same shape.

What tends to work: open with what the ayah *says or does* in plain Turkish, then
show the material shape that makes it happen. Grammar labels are support, not
the first experience. Do not open a paragraph with "isim cümlesi", "edat",
"tamlama başı", "yalın hâl", or similar technical scaffolding unless the same
sentence has already given the reader a concrete meaning to hold. Prefer:
"Âyet önce hamdi Allah'a verir; bunu fiille değil, sabit bir ad cümlesiyle
yapar." Then explain what the grammar forces, what the form and lexicon open,
what later context clarifies, and what the other layers could not carry.

Do not use that as a template if the ayah resists it.

**There is no length limit.** Write what the ayah's own work takes. A three-word
ayah with a dense lexical field can run long and that is correct. Length is a
consequence, never a target, and it is never a reason to leave something out —
carrying the full field outranks brevity at this level.

Absence goes in the coverage note, never in the prose. If a source is missing,
the reader does not learn that; the reviewer does.

## Failure modes for this level specifically

- **Slicing the surah thesis.** If your ayah commentary reads as one third of the
  surah reading, you have produced nothing new.
- **Selecting.** Choosing the most interesting activated reading and dropping the
  rest. This is the one unrecoverable error.
- **Cataloguing.** Correct, complete, unconnected. The reader is exactly where
  they started.
- **Ungrounded reveal.** True, contained, traceable, and delivered before the
  reader had ground for it.
- **Reporting the measurement.** Reader ids, stage numbers, confidence words,
  convergence counts. Render the experience; suppress the instrument.
- **Skipping the walk.** `reader_s{NNN}_{a,b}_ayah_walk.md` is where the latent
  material actually is. A commentary written without it will be a well-phrased
  primary reading and will be rejected.

## Pass condition

Someone who already knows this ayah well reads your text and learns something
they could not have got from a translation plus a dictionary — the thing they
learn does not depend on having read the rest of the surah — and at no point are
they unsure what the ayah says.

## Output

Continuous prose, in the target language, single voice, no provenance markers.

Separately — never interleaved — an evidence surface mapping phrases to bundle
refs, marking inference distinctly from bundle-traceable claims, plus a coverage
note stating what was missing.
