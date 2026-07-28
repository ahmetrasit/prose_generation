# Surah Commentary Prompt — layer 3

Read `../PRINCIPLES.md` and `../COMMENTARY_SPEC.md` first. They govern. Channel
rules are in `../docs/CHANNELS.md`. This file is the task.

---

## Task

You are given the **surah-scope bundle** and the **layer-2 commentary for every
ayah** of one surah. Write commentary that makes a reader understand **what this
surah is doing as a whole**.

You produce two things on two different axes, and they must not be confused:

- **the argument** — what the surah does as an assembly;
- **the channels** — the images that run through it, and what each ayah and each
  particular word contributes to them.

## What you are reading

**You read commentary, not source.** The raw ayah bundles are not given to you,
and that is the contract rather than a shortfall. Each ayah reading in front of
you was written by a separate agent that saw only that ayah's own bundle, in
isolation, knowing nothing of this surah or of any argument about it. That
isolation is the thing you depend on: those readings cannot have been
retro-fitted to a thesis, including the one you are about to build.

Per ayah you have the **prose** — what the reading says — and the **evidence
surface**, which carries the bundle refs, branch IDs, counter-evidence, coverage,
and an explicit mark on every claim that was the writer's own inference rather
than bundle-traceable. Where a layer-2 run produced a **findings index**, you
have that too: one line per reading the prose carries, which is the list your
exclusions are measured against. Its `surprise:<id>` rows make a second relation
explicit: which local secondary synthesis supports the primary reading and
which one shifts its frame.

Two rules follow, and they are hard:

- **Cite through the evidence surface.** Any `qacMorphemeRef`, `rootId`,
  `branchId`, or ayah reference you use at ayah level must appear in one of those
  evidence files or in the surah-scope bundle. A true claim you happen to know is
  still a violation (`PRINCIPLES.md` §1).
- **A reading that is not there is not available to you.** Say that it is
  missing; do not reconstruct it from the Arabic, and do not treat its absence as
  licence to infer (`PRINCIPLES.md` §7). If your argument needs something layer 2
  did not carry, that is a finding about the pipeline and belongs in friction.

Friction reports from layer 2 are deliberately withheld. They report on the
instructions, not on the ayahs.

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

A channel is a coherent recurring secondary system, assembled substantially from
non-primary branches, that changes the reading of participating ayahs and of the
surah as a whole. Full definition, membership test, maturity model, and plan
shape: `../docs/CHANNELS.md`.

Start from two independent inputs:

- the layer-2 `surprise:<id>` rows and their evidence mappings, which state what
  became newly visible inside individual ayahs without claiming recurrence;
- the surah-scope `network/v3` review and V12-derived material, which nominate
  non-primary branch resonances across ayahs.

Neither input automatically establishes a channel. Test whether specific
branch-level members recur, explain one another as a system, and produce a
whole-surah shift that no local reading alone could yield. A local surprise may
become a member, may support a member without being identical to it, or may
remain purely local.

**Do not treat channels as a hazard to the argument.** They are a separate axis
and both are real. For S100 the channel *is* the finding — the running horses are
unattached under the primary reading and only the channel attaches them. A surah
reading that reports only the argument there has withheld the thing worth
knowing.

The error to avoid is not *having* channels; it is letting a channel stand in for
an argument, or an argument suppress a channel.

**You propose channels; you do not admit them.** Writing channel prose and
accepting membership are different acts, and a writer must not silently admit
the system they want to write about (`PRINCIPLES.md` §2). Your structured
channel plan has `reviewState: "draft"` and goes to a separate review pass.

Candidate members you find and motifs you reject are both part of that draft,
with exact evidence refs and reasons. Mark the assembled system and its effects
as inference even when individual members are bundle-traceable.

## You must select

This is the defining constraint of this level, and the exact inverse of layer 2.

A thesis excludes. You will have far more activated readings than one argument
can carry, and carrying all of them produces a list, which is not an argument.
Choose.

**Then record what you excluded.** Layer 2's full field already preserves it.
Nothing is lost by selecting here because the other level did not select. Do
not request a thesis-aware Layer-2 rerun; that would destroy the isolation this
reading depends on.

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
something grounded in an ayah reading or the surah-scope bundle. Layer 2 has
prepared local surprises, but it has deliberately not prepared the cross-ayah
channel. Your draft must therefore record a disclosure path that a later
layer-2.5 pass can seed in reading order.

The final channel reading should become recognition rather than introduction
after that pass. For each ayah, record what member arrives there, what earlier
members can now be recalled, the channel's maturity, and the local reading shift.
Do not solve this by copying the finished channel explanation into every ayah.

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
- **Unseeded reveal.** A surah channel built from secondary members or local
  effects that layer 2 never prepared. A new name for already prepared material
  is not an unseeded reveal.

## Output

Continuous prose, in the target language, single voice, no provenance markers, no
headers named after evidence layers.

Write these separate artifacts:

- **`{S}.surah.prose.md`** — the whole-surah primary argument and the surprising
  channel reading as integrated reader prose. Keep the argument and channels
  distinguishable without turning either into a catalogue;
- **`{S}.surah.thesis.md`** — the primary-grounded thesis, one sentence;
- **`{S}.surah.channels.draft.json`** — a machine-readable draft conforming to
  `schemas/surah-channel-plan-v1.schema.json`. Give every channel and member a
  stable ID; record source candidates, exact evidence refs, both focus-ayah and
  whole-surah effects, rejected motifs, and `maturityByAyah` in reading order.
  Set `reviewState` to `draft`;
- **`{S}.surah.exclusions.md`** — activated readings this thesis could not carry,
  recorded against Layer 2's full field. Where a findings index exists, take it
  as the list you are excluding
  *from*: every line is either carried by your reading or named here. Where it
  does not, say so, and draw the exclusions from the layer-2 prose and evidence
  as best you can;
- **`{S}.surah.evidence.md`** — phrase-to-ref mapping and coverage note. The coverage
  note records what layer 2 did not hand you, including any ayah whose findings
  index is missing;
- **`{S}.surah.friction.md`** — prompt friction, including channel claims that
  could not be made reviewable.

## Note on available evidence

Channels have a surah-scope source: the `network/v3` review in the bundle. It is
first-pass and single-reader, so it is evidence rather than authority — but
channel membership is no longer pure inference.

Ayah-level claims have a source too: the layer-2 evidence surfaces, which are
where your refs come from. What they mark as inference stays inference when you
use it; you cannot promote another writer's guess by building on it.

The **argument** has no such artifact. Nothing upstream evidences what the surah
does as an assembly; it is derived from the ayah readings. Treat every structural
claim as your own inference and mark it as such in the evidence surface, distinct
from claims traceable to a bundle or to a layer-2 evidence surface.
