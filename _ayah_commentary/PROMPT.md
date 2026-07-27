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

## Structure

There is no fixed section list, and section headers named after evidence layers
are forbidden. Let the ayah's own shape decide. A single-word ayah and a
twelve-word ayah do not have the same shape.

What tends to work: open with what the ayah *is* materially (how many words, what
kind of act), then what the grammar forces, then what the form and lexicon open,
then the before/after, then what the other layers could not carry.

Do not use that as a template if the ayah resists it.

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
