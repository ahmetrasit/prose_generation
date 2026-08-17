# Ayah Commentary Rewrite Prompt — layer 2 (v2)

Read `PROMPT.md` (v2) in this directory first. It governs composition,
pedagogy, voice, and output. This file modifies only the task framing.

---

## Task

You are given:

1. The input bundle for one ayah, including the explicit coverage state of HFT,
   reader, and channel material.
2. The existing Layer-2 prose, evidence, and index for the same ayah.

These are the complete rewrite inputs. Do not read or depend on Layer 3 briefs,
outputs, exclusions, channel adjudications, or a later surah thesis. Layer 3 may
eventually consume this rewrite; it does not govern or enrich it. If any
instruction here conflicts with `PROMPT.md` (v2), the v2 prompt governs.

**Rewrite the prose** using the composition model in `PROMPT.md` (v2). The
existing prose is your starting material — it contains findings, word analysis,
and secondary readings that have already been derived from the bundle. Do not
discard them. Reorganize them.

## What to keep

- **Every finding the existing prose carries.** If the original mentions a
  secondary branch, a retrospective surprise, or an HFT-derived reading, it
  must survive in the rewrite. You are reorganizing, not re-selecting.
- **Coverage.** If the original covers a `must_integrate` topic, the rewrite
  covers it too. Check the existing index against the bundle. Account for every
  surface word under the v2 prompt's complete-but-proportionate word treatment;
  compact integration is allowed, silent disappearance is not.
- **Coexistence.** Preserve every materially distinct local resonance, including
  ones that pull in different directions. Reorganization may not choose a
  governing resonance or collapse several live lines into one.
- **Register and voice.** Follow the v2 prompt's voice rules. The existing
  prose's voice may differ; the rewrite adopts the v2 register.

## What to change

- **Structure.** Use the four composition movements as an internal sequence:
  opening → word-built development → local resonances → closing. They are not
  mandatory headings or equal-size paragraphs. The existing prose may walk
  through words serially and mention secondary images in passing. Reorganize it
  so every member of the resonance set is prepared and lands explicitly.
- **Pedagogy.** The existing prose likely mentions secondary branches as
  analyst's shorthand ("kelimenin bağlı olduğu alan da X'i taşır"). The
  rewrite must teach the reader that the word carries more than the translation
  gave, show what opens, and explain what changes. See "Your reader does not
  know how Arabic words work" in `PROMPT.md` (v2).
- **Proportionate development.** The existing prose may give each word equal
  weight. Preserve complete word coverage while giving sustained development to
  words that ground, create tension, or prepare a resonance. Other words remain
  live inside phrases or clauses. Space follows explanation cost, not rank. Give
  every significant finding enough room to make its mechanism and reader payoff
  clear; never compress it merely to shorten the rewrite.
- **Resonance visibility.** If the existing prose buries coherent secondary
  images inside word-by-word exposition, make each one explicit in the local
  resonance movement. Do not promote the most vivid image over the others.

## What to add

If the bundle contains channel or HFT material that the existing prose did not
surface — a subchannel synthesis, a context delta, an outlier — evaluate it
under the v2 composition model. Carry every materially distinct local resonance
that survives grounding, containment, and reader payoff. Treat first-pass
channel material as nomination rather than an established recurring system, and
mark the writer's local synthesis as inference. If material does not survive,
retain the rejection or limitation in evidence and friction.

## What not to do

- Do not re-derive findings from scratch when the existing prose already has
  them. The existing prose was written from the same bundle. Use it.
- Do not import new material from outside the bundle. The bundle is the
  evidence boundary.
- Do not name surah-wide systems, assert maturity, or state a thesis. The
  existing prose may not have done this either, but verify.
- Do not rank resonances, select a master image, or use source convergence as a
  confidence vote.
- Do not force a resonance that is not there. If the existing prose has no
  coherent secondary image and the bundle does not support one, the rewrite
  uses the no-resonance composition (opening → word-built → closing) without
  reducing grammatical, lexical, formal, or sound depth.

## Output

Same as `PROMPT.md` (v2): prose, evidence surface, index, and friction. The
friction report should note what changed structurally from the original and
whether any findings or resonances were gained or lost. The rewritten findings
index must reconcile against the original: every original reading remains, and
every new reading or `surprise:<id>` row must trace to the supplied bundle. Any
unexplained loss is a failed rewrite, not an editorial choice.
