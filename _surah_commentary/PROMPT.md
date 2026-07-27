# Surah Commentary Prompt — layer 3

Read `../PRINCIPLES.md` and `../COMMENTARY_SPEC.md` first. They govern. Channel
rules are in `../docs/CHANNELS.md`. This file is the task.

---

## Task

You are given the input bundles for every ayah of one surah. Write commentary
that makes a reader understand **what this surah is doing as a whole**.

You produce two things on two different axes, and they must not be confused:

- **the argument** — what the surah does as an assembly;
- **the channels** — the images that run through it, and what each ayah and each
  particular word contributes to them.

## The argument

**What is the argument?**

Not what each ayah means — that is layer 2's job. You are after the shape of the
assembly: each ayah's *function* rather than its content, where the surah turns,
what is marked or asymmetric about its structure, and what the whole does that no
part does.

### The pass condition, stated first because everything depends on it

**Your text must say something that an ayah-by-ayah reading could not produce.**

If every claim in your draft decomposes back into individual ayahs, you have
written a summary, not a surah reading. Delete it and start again.

The test is concrete. For S103 it is the reciprocity turn: `تواصوا` is Form VI,
so half the exception's conditions cannot be met alone, so the surah's escape
from a universal verdict is structurally unavailable to a solitary person. No
single ayah says that. It is visible only in the shape.

Find that thing. If you cannot find it, say you cannot find it. A surah
commentary that admits it has no thesis is worth more than one that dresses a
summary as an argument.

### The argument must rest on the primary reading

State it such that it holds with **every latent reading removed**. Then let
latent readings deepen, recolour, or perturb it.

If deleting the latent layer collapses your thesis, the thesis is not ready. This
rule exists because it was violated: a first S103 attempt built the surah level
entirely out of latent readings and produced prose that explained nothing to
someone who already knew the surah.

## The channels

A channel is a coherent image running across the surah, assembled from branches
the primary reading does not select. Full definition, membership test, maturity
model, and ledger shape: `../docs/CHANNELS.md`.

**Do not treat channels as a hazard to the argument.** They are a separate axis
and both are real. For S100 the channel *is* the finding — the running horses are
unattached under the primary reading and only the channel attaches them. A surah
reading that reports only the argument there has withheld the thing worth
knowing.

The error to avoid is not *having* channels; it is letting a channel stand in for
an argument, or an argument suppress a channel.

**You consume channels; you do not establish them.** Writing prose and admitting
evidence are different acts, and a writer admits the channels they want to write
about (`PRINCIPLES.md` §2). Adjudication is a separate pass with its own reader.

Two states:

- **An adjudicated ledger exists.** Use its admitted channels and their members.
  Its rejected candidates stay rejected — you may not readmit one because it
  would improve your prose.
- **Only the first-pass review exists** (`channel_review`, every surah but four).
  This is evidence, not authority. You may build a channel reading from it and
  you must mark every channel claim as your own reading in the evidence surface,
  distinct from bundle-traceable claims.

In both states, **candidate members you find and the motifs you reject are part
of your output** — with `qacMorphemeRef`/`rootId`/`branchId` and the reason. They
are input to adjudication, not a ledger.

## You must select

This is the defining constraint of this level, and the exact inverse of layer 2.

A thesis excludes. You will have far more activated readings than one argument
can carry, and carrying all of them produces a list, which is not an argument.
Choose.

**Then record what you excluded.** The exclusions are handed to layer 2, which is
obliged to carry them. Nothing is lost by selecting here, because the other level
does not select. That is why you are allowed to.

An exclusion list is part of your output, not an appendix.

## Integration is the work

You will receive N activated readings. If your output has N sections, you have
reformatted, not integrated.

Multiple branches of one root are usually **facets of one concept**, not separate
readings. Collapse them. In S103, eight `ع ص ر` branches — press, rain-cloud,
husk, choking throat, withholding, refuge, yield — are one idea: *retention under
compression*. Seeing that made `خسر` legible as leakage and made the surah's
ending on `صبر` structurally necessary rather than a pious sign-off.

The collapse is the finding. The list is not.

Ask constantly: **do these images explain each other, or merely sit next to each
other?** If a paragraph could be moved elsewhere without damage, it is sitting,
not explaining.

## Grounding

Your reader arrives here having read the ayahs. Everything you name should be
something they have already met once, in place, through its own ayah — that is
what the layer-2 channel increments are for.

Layer 3 is a recognition, not an introduction. If your prose has to teach a
resonance from scratch in order to use it, either the channel was seeded too late
at layer 2 or it is not ready.

The reader must not finish your text less sure of what the surah plainly says.

## Useful structural probes

Not a checklist. Things that have paid off:

- What is each ayah's *function* — premise, verdict, exception, oath, turn?
- Where does the surah pivot, and on what word?
- What is grammatically marked — a definite generic, a missing verb, a repeated
  rather than shared verb, an emphatic stack, a locative where a future was
  expected?
- Do the first and last words relate? (S103 opens on `عصر`, closes on `صبر` —
  compression and retention, two sides of one physics.)
- Is the verdict present or future, description or threat?
- What does the ordering of a list do that the list's content does not?
- What does the surah's opening have to do with anything? If the answer under the
  primary reading is "nothing", look for a channel.

## Failure modes for this level specifically

- **Aggregation.** Clustering the ayah readings, naming the cluster, presenting
  the name as a thesis. A cluster with a title is a set, not an argument.
- **Channel/argument conflation.** Either direction: a channel presented as the
  argument, or the argument presented as if it exhausted the surah.
- **Latent-only thesis.** See above; enforce `restsOn: primary`.
- **Sequence as structure.** "First it says X, then Y, then Z" is a paraphrase in
  disguise.
- **Unseeded reveal.** A channel stated here that layer 2 never prepared.

## Output

Continuous prose, in the target language, single voice, no provenance markers, no
headers named after evidence layers.

Plus, as separate artifacts:

- **thesis** — one sentence;
- **channel candidates** — for each channel you read: members with
  `qacMorphemeRef`/`rootId`/`branchId`, the system they form, what becomes
  legible because of it, and the motifs you rejected with reasons. This is input
  to adjudication (`../docs/CHANNELS.md` §6), not a ledger. Do not compute
  maturity;
- **exclusions** — activated readings this thesis could not carry, handed to
  layer 2;
- **evidence surface** — phrase-to-ref mapping and coverage note.

## Note on available evidence

Channels have a surah-scope source: the `network/v3` review in the bundle. It is
first-pass and single-reader, so it is evidence rather than authority — but
channel membership is no longer pure inference.

The **argument** has no such artifact. Nothing upstream evidences what the surah
does as an assembly; it is derived from the ayah bundles. Treat every structural
claim as your own inference and mark it as such in the evidence surface, distinct
from claims traceable to a bundle.
