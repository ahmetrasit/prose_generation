# Ayah Commentary Prompt — layer 2 (v2)

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

## Your reader does not know how Arabic words work

This is the single most important thing about your audience. Your reader does
not know that an Arabic word carries an entire family of related meanings — that
the same root can mean a road walked smooth, a slave, and an act of worship,
and that all three are live in the same verb. They do not know that a
translation picks one branch and silences the others. They do not know that the
silenced branches can form coherent images when read together across the words
of one ayah.

**You must teach this as you go.** Not with terminology — not "polysemy," not
"branch," not "root field." Show the reader that this word carries more than
what the translation gave them. Show them what opens when that second meaning is
heard. Show them what changes in the ayah when two words' secondary meanings
meet.

If you mention a secondary reading without first making the reader understand
that the word has this capacity, the reading will feel like decorative ambiguity
— strange pressure with no payoff. The reader will think you are being poetic
rather than revealing something real.

A secondary reading mentioned but not explained is worse than a secondary reading
not mentioned at all.

## Composition

Before writing, identify the ayah's **local resonance**: the coherent secondary
image or shift that emerges when branches of different words in this ayah are
read together. Look for it in `channel_subchannels_anchored_here`,
`v12_focus_trace_hermetic` (especially `context_deltas` and
`surprising_valid_outliers`), and `v12_reader_walks` (especially
`retrospective_surprises`). When these sources converge on the same image, the
finding is strong.

Not every ayah has a resonance worth surfacing. Some ayahs' main contribution is
a grammatical force, a form selection, a sound pattern, or a single dense word.
When there is no coherent secondary image, the composition still works — the
word-built development serves the primary reading and the closing consolidates
what the ayah does. Do not force a surprise that is not there.

When a resonance exists, organize the prose around it:

### 1. Opening — what the ayah plainly says

Establish the ordinary scene and the reader's first footing. What does a
competent translation already give? Say it in one or two paragraphs. No
technical apparatus, no secondary meanings yet. This paragraph is grounding:
when the surprise arrives later, the reader will not lose their footing because
you gave them solid ground here.

### 2. Word-built development — selective, not exhaustive

Walk through the key words, but **selectively**. Not every word deserves its
own paragraph. Not every grammatical observation belongs. Each word you develop
should do one of three things:

- **ground the primary reading** — make the reader feel the ayah's plain
  meaning more precisely than a translation could;
- **create tension** — show the reader that a word carries more than what they
  heard, that the translation chose one meaning and set others aside;
- **prepare the resonance** — lay the ground so the later surprise feels
  earned, not announced.

A word that does none of these three things can be handled in a clause within
another paragraph. It does not need its own section.

`must_integrate` topics from `word_analysis` must all appear in the commentary.
But appearing does not mean getting a dedicated paragraph — a `must_integrate`
topic can land in a sentence within a paragraph organized around something else.
What matters is that the reading is present and the `reader_payoff` is
delivered, not that each topic gets equal architectural weight.

When you introduce a word's secondary meaning, **first show the reader that
the word has this capacity**. Not "bu kelimenin bağlı olduğu alan da X'i
taşır" — that is analyst's shorthand the reader cannot use. Instead: "Çeviriler
burada tek bir anlam verir ve durur. Ama Arapça kelime bu anlamla bitmez; aynı
kök, başka bir yaşantıyı, başka bir ilişkiyi de taşır — ve bu ikinci anlam
âyetin içinde sessizce çalışır." Show the word opening. Show what the reader
can now hear.

### 3. Local resonance — what the words reveal together

This is the payoff. When branches of different words in this ayah form one
coherent image, say what that image is and what it changes.

Do not present this as a separate "channel section" or label it as a secondary
reading. It is part of the continuous prose. Enter through one of the ayah's own
words that the reader has already met in the development section. Show how this
word's secondary meaning meets another word's secondary meaning, and what
picture emerges.

Then say what changed. What can the reader now see that a flat translation hid?
What does this ayah do that was invisible before?

If the resonance supports the primary reading, say so: the ayah's plain meaning
is not replaced but deepened. If it shifts it, say what shifts: the reader's
understanding of what the ayah is doing has changed direction.

**What you must not do:**

- Name the image as an established surah-wide system. Not "bu sûrede bir yol
  imgesi sürüyor." You are writing in isolation; you do not know whether this
  image recurs. Keep it local.
- Assert maturity or channel status. No maturity has been adjudicated.
- State the surah's thesis.

### 4. Closing — what the reader now sees

One paragraph. Consolidate what the ayah does — both its plain sense and what
the word-built analysis revealed. The reader should finish with a clear,
strengthened understanding: "So this ayah is not only asking for direction; the
words have shown a supported passage, a carried way, a road that holds its
traveler."

This paragraph is where you make the return trip to the primary reading. The
reader left solid ground, traveled through word meanings, saw a secondary image,
and now comes back to what the ayah says — but they see more in it.

### When there is no resonance

Some ayahs will not have a coherent secondary image worth surfacing. The
channel material may be sparse, the HFT may show no strong outliers, or the
secondary branches may not form a coherent picture.

In that case, skip step 3. The composition becomes: opening → selective
word-built development serving the primary reading → closing consolidation.
The commentary is still valuable — a strong primary reading with precise word
analysis is better than a forced surprise. Record in the friction report that no
coherent secondary resonance survived grounding and containment.

## What counts as an activated reading

The bundle's `word_analysis` topics carry `commentary_obligation`:

- **`must_integrate`** — obligatory. Every one appears in your commentary.
- **`candidate`** — discretionary. Topics with `status: narrowed` are
  non-primary pressures on a word. A commentary that honours only its obligations
  will be competent, complete, and hold no surprise at all. Read the `candidate`
  topics before deciding.

Beyond `word_analysis`, these bundle fields carry activated readings:

- **`v12_focus_trace_hermetic`** — `baseline_models`, `context_deltas`, and
  `surprising_valid_outliers`. Outliers are not errors. They are the material
  most likely to be lost in whole-surah synthesis, especially secondary
  split-root activations.
- **`v12_reader_walks`** and **`v12_reader_walks_wide`** — retrospective
  surprises are the highest-value material at this level. They are literally
  the shape of understanding arriving late.
- **`v12_cross_run_publication`** — compact coverage/priority check. Do not
  copy as prose; use as a coverage audit.
- **`channel_subchannels_anchored_here`** — reviewed subchannel readings
  anchored at this ayah: parent channel context, synthesis, active motifs, and
  ayah anchors. Use as a primary source for identifying the local resonance.
- **`channel_generated_outputs`** — lists external quran-data files (candidate
  graphs, family inventories, path families). If your run gives file access,
  read only listed files when channel detail is necessary. These are
  candidate/family/path evidence, not an adjudicated channel ledger.
- **Branch inventories** — support explanations; they create no standalone
  prose obligation.

## Enrichment mode

If the bundle contains `layer3_channel_briefs` — adjudicated channel findings
with identified members, maturity, and payoffs — use them as your resonance
planning source instead of deriving surprise targets from raw
`channel_subchannels_anchored_here`. The briefs tell you which image this ayah
participates in and what its local contribution is. Your job shifts from
*finding* the resonance to *making it land* for a reader who does not yet see
it.

Even in enrichment mode, the composition model and pedagogical rules are the
same. The reader still does not know how Arabic polysemy works. The word-built
development still prepares the resonance. You still may not name a surah-wide
system — the brief tells you the system exists, but the reader discovers it
ayah by ayah, not from a label.

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

## Keep the reader's feet on the ground

Grounding (`PRINCIPLES.md` §5) is a hard constraint here, not a matter of tone.

- The primary reading stays reachable at every point. The reader must never lose
  track of what the ayah plainly says.
- Every resonance enters through a word already in front of the reader, in a form
  they have already been given. Nothing is announced from above.
- Containment is at sentence level: `X — as Y`, never `not X but Y`.

An ungrounded reveal is a rejected output even when every claim in it is true and
traceable.

## Before and after

Ayah level has something surah level cannot have: **the ayah existed before its
neighbours did.**

If the bundle contains `v12_focus_trace_hermetic`, use it as the primary
before/after signal: `baseline_models` for what the ayah yields alone,
`context_deltas` for what later context activates, and
`surprising_valid_outliers` for what remains anchored but unexpected.

Render this as reading experience, not as measurement:

> Bu âyet tek başına gösterildiğinde … Sonra hüsran açıldı, sonra istisna — ve
> iki okuma da yerine oturdu.

Never as: *"three readers at exploratory confidence converged on two models."*

If the reader walks record *retrospective surprises* — readings that only became
visible after a later ayah — those are the highest-value material at this level.

**If both staged reader responses and Hermetic Focus Trace are absent, say so.**
Do not infer what they would have contained.

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

Containment (`PRINCIPLES.md` §4) is phrased as a prohibition, so it is tempting
to discharge it by narrating what is *not* happening. And the `reader_payoff`
fields in the bundle are themselves written as analyst's shorthand. Do not
inherit that register.

In Turkish, stacked `-maz / -mez / değildir / yoktur` constructions read as
hedging and break the flow. Turkish carries contrast through `zaten`, `hem… hem`,
`-ken`, `ayrıca`, and through simple juxtaposition.

| instead of | write |
| --- | --- |
| Bu âyet bir şey bildirmez, bir şey ister. | Bu âyet bir istektir. |
| Türkçede bunun karşılığı yoktur. | Türkçe burada tek bir "ilet" ile yetinir. |
| Âyet yolun düz olduğunu ileri sürmüyor; hangi yol olduğunu söylüyor. | Âyet hangi yol olduğunu söyler: o yol, o bilinen dosdoğru olan. |

Use an explicit negative only to correct a likely misconception, protect the
primary sense from replacement, or preserve live counter-evidence. If no
explicit negative is needed, say in the friction report that there was no live
misconception requiring one.

## Arabic word surfaces

Mark Arabic lexical items with a structured span when the Arabic word matters:

```text
{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar}
```

`ar` is the Arabic surface form for TTS, `tr` is the Turkish-readable
transliteration, `gloss` is the target-language meaning.

Use the span at first mention of an ayah word, and again when the prose returns
to that word after another word or another paragraph. Inside one short local
sequence, a Turkish label or transliteration is enough.

Do not display roots as spaced Arabic letters or letter-by-letter transliteration
in prose. Anchor root discussion to the surface word:
`{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar} kelimesinin bağlı
olduğu kök alanı...`, not `ʿ-d-w kökü...`. Raw roots, branch IDs, and root
skeletons belong in the evidence surface.

## Structure notes

Section headers named after evidence layers are forbidden. Let the ayah's shape
decide. A single-word ayah and a twelve-word ayah do not have the same shape.

Do not open a paragraph with "isim cümlesi", "edat", "tamlama başı", "yalın
hâl", or similar technical scaffolding unless the same sentence has already
given the reader a concrete meaning to hold. Prefer: "Âyet önce hamdi Allah'a
verir; bunu fiille değil, sabit bir ad cümlesiyle yapar."

**There is no length limit.** Write what the ayah's own work takes. Length is a
consequence, never a target, and it is never a reason to leave something out —
carrying the full field outranks brevity at this level.

Absence goes in the coverage note, never in the prose. If a source is missing,
the reader does not learn that; the reviewer does.

## Failure modes

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
- **Skipping the walk.** Reader walks are where the latent material actually is.
  A commentary written without them will be a well-phrased primary reading and
  will be rejected.
- **Burying the surprise in word analysis.** The channel synthesis or HFT outlier
  identifies a coherent secondary image. The prose spends twelve paragraphs on
  word-by-word grammar, then mentions the image in passing. The finding was
  present but not organized around.
- **Decorative ambiguity.** A secondary branch is mentioned in passing — the
  reader does not know why it matters, does not know the word carries multiple
  meaning families, and cannot tell whether the author is revealing something
  real or being poetic. Strange pressure with no payoff. This is a failure of
  pedagogy, not of content.

## Pass condition

Someone who already knows this ayah well reads your text and learns something
they could not have got from a translation plus a dictionary — the thing they
learn does not depend on having read the rest of the surah — and at no point are
they unsure what the ayah says.

A secondary condition: a reader who does *not* know this ayah well finishes the
text understanding both what the ayah plainly says and why certain words carry
more than the translation showed. They should not feel confused by unexplained
secondary meanings or wonder why the author mentioned something strange.

## Output

Continuous prose, in the target language, single voice, no provenance markers.

Separately — never interleaved — an evidence surface mapping phrases to bundle
refs, marking inference distinctly from bundle-traceable claims, plus a coverage
note stating what was missing.
