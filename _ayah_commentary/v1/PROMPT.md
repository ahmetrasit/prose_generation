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
- **`candidate`** — discretionary. Topics with `status: narrowed` are the
  non-primary pressures on a word, and in the cases measured so far **every one
  of them is `candidate`, none are `must_integrate`**. A commentary that honours
  only its obligations will be competent and complete, but may leave the
  ayah's live pressure underdeveloped. Read the `candidate` topics before
  deciding; surprise alone does not justify inclusion.
- **`ledger_only`** — set aside by review, and rare. The topic either duplicates
  another (`duplicate_of_topic_id`) or its claim is contradicted by the bundle
  (`blocking_evidence`). It does not enter your commentary and does not enter the
  findings index. It is not yours to rehabilitate.

Each topic also carries `reader_payoff`, stating what the reader gains. Use it as
a test: if you cannot make that payoff land, the topic is not yet written.

When this prompt says "activated reading" below, read it in this operational
sense: every `must_integrate` topic, plus every `candidate` topic you admit
because it adds a distinct reader payoff. `candidate` topics are not silently
dropped, but they are admitted by payoff, not by surprise or by branch count.

Branch inventories, reader walks, channel review, and the channel generated
output manifest nominate material that has no topic. That material is admissible
when it is in the bundle. If `channel_generated_outputs` lists quran-data files
and your run gives you file access, you may read only those listed files when a
channel-family or path detail is necessary. Do not browse the repository
generally. If your run is hermetic and the files are not inlined, treat the
manifest as awareness and do not invent their contents.

`root_lexicon` is full, not branch-filtered. It carries Turkish dictionary/gloss
records for QAC roots in this ayah after mapping them to Furuq `root_XXXXXX`
IDs. When the QAC-to-Furuq root map marks a root as split, non-dominant Furuq
targets are included as additional root entries and recorded in coverage. If
multiple QAC roots map to the same Furuq root in this ayah, that shared entry
lists its source roots in `qac_roots_ar` / `qac_root_mappings`; use those fields
for evidence attribution when present, not the legacy single `root_ar` alone.
Dictionary/gloss branches are evidence support, not independent obligations,
unless tied to this ayah's word, topic, reader payoff, or cited relation. Full
field means all distinct reader payoffs from the activated material; it does not
oblige you to turn every dictionary branch into prose.

## You must not select

This is the defining constraint of this level.

Layer 3 is allowed — required — to build a thesis, and a thesis excludes. You are
the opposite. **You carry the full field.** Every operationally activated reading
appears here: all `must_integrate` topics, plus the `candidate` topics you admit
because they add a distinct reader payoff. That includes readings no surah thesis
could use, and readings that pull in different directions.

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
- **A word from another ayah is not in front of the reader.** When a later ayah
  is what makes a reading here visible, cite that ayah by reference and give its
  word its own full span before leaning on it. Describing a neighbouring ayah in
  your own words does not ground it — it asks the reader to recognise something
  they have not been shown.

An ungrounded reveal is a rejected output even when every claim in it is true and
traceable.

That last bullet carries most of the weight in practice. Measured on a full-surah
run, the paragraphs a reader finds hardest to follow are precisely the paragraphs
whose evidence rows are marked inference rather than bundle-traceable — the
reader-walk material about neighbouring ayahs. It reads as abstract because it
has no word to enter through, not because the thought is difficult. Give it a
word.

## Make the local surprise explicit

Do not make the reader infer which of many lexical observations is the finding.
When secondary resonances cohere, the prose must contain a clear **surprise
turn**:

1. keep the ayah's primary reading recoverable;
2. enter through this ayah's own word;
3. state the coherent secondary line;
4. say what it does to the primary reading and what becomes newly visible.

Use one of two relations in your planning and findings index:

- **`supports-primary`** — the secondary line makes the primary more concrete,
  integrated, or forceful without changing its frame;
- **`shifts-primary`** — the primary remains true, but the secondary line
  changes its frame, scale, agency, temporality, or consequence.

These labels belong in the findings index, not necessarily in reader prose. The
prose should make the relation unmistakable in natural language. A paragraph
that gives a surprising root image and moves on has not stated the surprise; it has
only exposed material. Connect the image back to what the ayah plainly says and
name the gain.

Do not manufacture coherence. Several live secondary readings may remain
separate pressures when they do not explain one another. Do not call a
restatement of the translation a secondary reading. Surprise is the payoff
test, not a license to admit unsupported material.

## Channel material is candidate evidence, not your output

The bundle may contain `channel_subchannels_anchored_here` and a
`channel_generated_outputs` manifest. They are first-pass discovery material,
not an accepted surah channel and not evidence that an image recurs.

Use them only when they help you notice a locally grounded resonance already
supported by this ayah's word evidence. State that local surprise and mark the
synthesis as inference. Do not name a surah-wide channel, assert recurrence or
maturity, import members from other ayahs, or state the surah's thesis. Those
tasks happen after every isolated ayah commentary exists.

## Before and after

Ayah level has something surah level cannot have: **the ayah existed before its
neighbours did.**

If the bundle contains v12 reader responses, they record exactly this — what the
ayah yielded in isolation (`stage_00`), and how that changed as neighbours were
revealed (`stage_01`, `stage_02`), including `changed_reading{before, after}` and
per-stage `status`/`confidence` movement.

If the bundle contains `v12_focus_trace_hermetic`, use it as the cheaper
replacement signal: a one-call reconstructed trace with `baseline_models`,
`context_deltas`, and `surprising_valid_outliers`. It is not a strict staged
reveal, so do not call it `stage_00` / `stage_01`; render its before/after value
as "what the ayah can yield on its own" and "what later context activates,
sharpens, revises, or leaves as a surprising but still anchored reading."
Outliers are not errors by default. They are the material most likely to be lost
in whole-surah synthesis, especially when the trace preserves a changed reading
or a secondary split-root branch.

Render this as reading experience, not as measurement:

> Bu âyet tek başına gösterildiğinde … Sonra hüsran açıldı, sonra istisna — ve
> iki okuma da yerine oturdu.

Never as: *"three readers at exploratory confidence converged on two models."*

If the reader walks record *retrospective surprises* — readings that only became
visible after a later ayah — those are the highest-value material at this level.
They are literally the shape of understanding arriving late.

If both staged reader responses and Hermetic Focus Trace are absent, record that
in the evidence coverage note, and mention it in friction only if a live
instruction depended on them. Do not infer their contents or mention the absence
in prose.

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
expect the wrong sense. If a prompt profile asks for a negation audit, label it
as a profile-specific style audit rather than friction.

### Negation also hides inside positive verbs

A contrastive frame is `not X but Y` even when every word in it is affirmative.
These forms pass a check for `değildir` / `yoktur` and still break containment
(`PRINCIPLES.md` §4), because the reader is handed a wrong reading to discard
before being given the right one. They are the most common way this prose goes
wrong.

Schematically, with `A` the reading being discarded and `B` the reading being
asserted:

| instead of | write |
| --- | --- |
| dar bir `A`'yı **aşarak** `B`'yi kurar | `B`'yi kurar |
| `A` **yerine** `B`'yi gösterir | `B`'yi gösterir |
| bir `A` olmaktan **öte**, `B`'dir | `B`'dir |
| yalnızca `A` **değil**, aynı zamanda `B` | hem `A` hem `B` |

Watch `aşarak`, `aşan`, `ötesinde`, `yerine`, `-den ziyade`, `-den çok`,
`sadece … değil`, and `bir X olmaktan öte`. If a sentence introduces a reading
only to move past it, cut the introduced reading and state what the word does.

The same three exceptions govern: keep the contrast when a misconception is live,
when the primary sense is at risk of replacement, or when the counter-evidence is
publishable. Then the discarded reading is the point, so name it in the evidence
surface rather than leaving it as a rhetorical foil.

## Arabic word surfaces

Reader and listener editions need different surfaces. In authored prose, mark
Arabic lexical items with a structured span when the Arabic word itself matters:

```text
{ar:ٱلْقَلَمِ, tr:el-kalem, gloss:kalem}
```

Here `ar` is the Arabic surface form for TTS and exact display, `tr` is the
Turkish-readable transliteration, and `gloss` is the target-language meaning.
The reading edition may render this as `el-kalem (ٱلْقَلَمِ), "kalem"`; the
listener edition may keep only the Arabic surface form where the TTS voice should
pronounce Arabic. The word here is only a format illustration — it is not from
any surah you will be given, and it carries no reading.

Use the span at first mention of an ayah word, and again the first time each
later paragraph takes that word up. **A paragraph that discusses a word carries
that word's full span.** A bare transliteration is not enough to open one. Within
a single paragraph, once the full span has been given, the Turkish label alone is
enough.

This is not a formatting preference. The measured failure is front-loading: every
span lands in the opening paragraph, and each paragraph after it discusses its
word by transliteration alone. The reader loses track of which Arabic word is on
the table exactly where the analysis gets dense, and the prose reads as abstract
when it is in fact specific.

A later renderer may hide repeated `ar` or `gloss` fields; the authored file must
carry enough structure for the reading, display, and TTS editions to be produced
from it.

Do not display roots as spaced Arabic letters or letter-by-letter
transliteration in prose. Anchor root discussion to the surface word instead:
`{ar:ٱلْقَلَمِ, tr:el-kalem, gloss:kalem} kelimesinin bağlı
olduğu kök alanı...`, not `q-l-m kökü...`. Raw roots, branch IDs, and root
skeletons belong in the evidence surface.

## Structure

There is no fixed section list, and section headers named after evidence layers
are forbidden. Let the ayah's own shape decide. A single-word ayah and a
twelve-word ayah do not have the same shape.

What tends to work: open with what the ayah *says or does* in plain Turkish, then
show the material shape that makes it happen. Grammar labels are support, not
the first experience. Do not open a paragraph with "isim cümlesi", "edat",
"tamlama başı", "yalın hâl", or similar technical scaffolding unless the same
sentence has already given the reader a concrete meaning to hold. The rule is
meaning first, label second, **within the same sentence**: say what the ayah or
the word does in plain Turkish, then name the construction that does it. A
grammatical label may appear in an opening sentence; it may not be the first
thing the reader has to hold. Then explain what the grammar forces, what the form
and lexicon open, what later context clarifies, and what the other layers could
not carry.

Do not use that as a template if the ayah resists it.

### Reader movement and revision

Open by giving the reader the ayah's act or reachable meaning in plain Turkish.
A paragraph may begin with the ayah's surface, a concrete image, or a
reader-facing claim. It may not begin by asking the reader to hold a bare
technical label or a stack of abstract terms.

During revision, check that each paragraph advances one governing movement.
Several observations may serve that movement, but lexical or grammatical detail
must return to what the ayah says, does, or makes the reader perceive. If two
independent reader consequences have accumulated, separate them.

When several grammatical or lexical observations explain one another, give them
a whole-ayah gathering movement. This is synthesis, not recap: show what the
observations make the ayah do together.

When that synthesis uses secondary resonances, make its relation to the primary
reading explicit. The reader should be able to point to one sentence and say:
"this is the secondary line, and this is how it supports or shifts what the
ayah plainly says." Do not rely on paragraph order or repeated imagery to imply
the relation.

Concrete lexical images should make an evidence-supported relation visible.
Compress them around a shared action or shape when the evidence permits, while
keeping the local sense intact. Such compression is interpretive synthesis, not
a claim that every derivative possesses one historical essence; mark the
synthesis as inference in the evidence surface.

Use Turkish lexical or cultural associations only when the bundle supports the
relation. Distinguish cognates, semantic shifts, and reception associations.

Later context should return explicitly to the focus ayah. Sound usually
reinforces a movement already established in meaning rather than arriving as a
technical appendix; when sound itself organizes the ayah, say the audible event
first and the phonetic mechanism second.

**There is no length limit.** Write what the ayah's own work takes. A three-word
ayah with a dense lexical field can run long and that is correct. Length is a
consequence, never a target, and it is never a reason to leave something out —
carrying the full field outranks brevity at this level. Compression still
matters: repetition does not discharge coverage, and surprise alone does not
justify a candidate reading.

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
- **Skipping the walk when present.** `reader_s{NNN}_{a,b}_ayah_walk.md` is where
  much of the latent material actually is. When reader walks are present, a
  commentary written without them will be a well-phrased primary reading and will
  be rejected. When they are absent, record the absence in coverage, and mention
  it in friction only if a live instruction depended on them.

## Pass condition

Someone who already knows this ayah well reads your text and learns something
they could not have got from a translation plus a dictionary — the thing they
learn does not depend on having read the rest of the surah — and at no point are
they unsure what the ayah says.

## The findings index

Alongside the prose, emit a flat list of every reading this ayah carries, one
line each. It lets a later layer — or a reader in a hurry — see the whole field
without reading the whole commentary.

It is a table of contents for the field. It is **not** a summary, and it is not
somewhere to put things.

**Compress the prose, never the field.** A summary drops whatever is least
interesting, and this level is precisely the one forbidden to decide what is
least interesting. So the index shortens how each reading is *said*, and shortens
nothing about how many there are. A dense ayah has a long index; that is correct.

Two rules make that concrete, and both are checked mechanically:

- **Every `must_integrate` topic appears exactly once**, under its own
  `topic_id`. Same obligation the prose already carries, in a form that can be
  counted.
- **The index may not carry a reading the prose does not carry.** Write it last,
  from the finished prose. A line with no home in the prose means the prose is
  incomplete — fix the prose, not the index.

`ledger_only` topics are excluded. `candidate` topics you admitted belong here
exactly like obligatory ones; the index does not distinguish them, because by the
time a reading is in your commentary it is no longer discretionary.

Add one synthesis line for every coherent local surprise the prose carries:

```text
- `surprise:<short-stable-id>` — <the secondary line and its reader payoff> [supports-primary] [inference]
- `surprise:<short-stable-id>` — <the secondary line and its reader payoff> [shifts-primary] [inference]
```

Use a short lowercase ASCII id derived from the image or movement, not a network
candidate id. The relation marker is required and says what the surprise does to
the primary reading. `[inference]` is normally required because connecting
several readings is the writer's synthesis. These surprise lines do not replace
the individual topic/ref lines whose field they synthesize.

If no secondary material survives evidence, grounding, coherence, and
containment, write no `surprise:` line and say why in the evidence coverage
note. Do not invent a weak surprise to satisfy the format.

### Format

One line per reading, in the target language. No headers, no grouping, no prose
between lines.

```text
- `<ref>` — <one clause: what the reading is>
- `<ref>` — <one clause> [inference]
```

`<ref>` is whatever the bundle calls the thing: a `topic_id`, a `root:branch`
pair, a QAC morpheme ref, a walk identifier, or a local `surprise:<id>`. Append
`[inference]` when the reading is your own — reader-walk abduction, a
review-informed connection, a structural observation — keeping a ref if one
exists. The marker is that literal ASCII token, not a translation of it, so that
it can be counted.

`[supports-primary]` and `[shifts-primary]` are likewise literal ASCII markers
and appear only on `surprise:` synthesis rows.

Order the lines as the ayah's own words run, then the readings belonging to no
single word. One clause per line: if a line wants a semicolon, it is two lines.

## Output

Continuous prose, in the target language, single voice, no provenance markers.

Separately — never interleaved — an evidence surface mapping phrases to bundle
refs, marking inference distinctly from bundle-traceable claims, plus a coverage
note stating what was missing.

Separately again, the findings index described above.

Also write a friction report naming every point where the instructions were
ambiguous, contradictory, unsatisfiable, or silent. Profile-specific style audits
may be included there when the prompt profile asks for them, but they should be
labelled as style audit rather than friction.
