# Ayah Commentary Rewrite Prompt — layer 2 (v2)

Read `PROMPT.md` (v2) in this directory first. It governs composition,
pedagogy, voice, and output. This file modifies only the task framing.

---

## Task

You are given:

1. The input bundle for one ayah (with HFT and channel data).
2. The existing Layer-2 prose, evidence, and index for the same ayah.

**Rewrite the prose** using the composition model in `PROMPT.md` (v2). The
existing prose is your starting material — it contains findings, word analysis,
and secondary readings that have already been derived from the bundle. Do not
discard them. Reorganize them.

## What to keep

- **Every finding the existing prose carries.** If the original mentions a
  secondary branch, a retrospective surprise, or an HFT-derived reading, it
  must survive in the rewrite. You are reorganizing, not re-selecting.
- **Coverage.** If the original covers a `must_integrate` topic, the rewrite
  covers it too. Check the existing index against the bundle.
- **Register and voice.** Follow the v2 prompt's voice rules. The existing
  prose's voice may differ; the rewrite adopts the v2 register.

## What to change

- **Structure.** Reorganize around the 4-part composition model: opening →
  word-built development → local resonance → closing. The existing prose likely
  walks through words serially and mentions secondary images in passing. The
  rewrite should build toward the resonance.
- **Pedagogy.** The existing prose likely mentions secondary branches as
  analyst's shorthand ("kelimenin bağlı olduğu alan da X'i taşır"). The
  rewrite must teach the reader that the word carries more than the translation
  gave, show what opens, and explain what changes. See "Your reader does not
  know how Arabic words work" in `PROMPT.md` (v2).
- **Selectivity.** The existing prose likely gives each word equal weight. The
  rewrite is selective: words that ground, create tension, or prepare the
  resonance get development; others land in clauses within other paragraphs.
- **Resonance prominence.** If the existing prose buries a coherent secondary
  image inside word-by-word exposition, the rewrite moves it to position 3 and
  builds toward it.

## What to add

If the bundle contains channel or HFT material that the existing prose did not
surface — a subchannel synthesis, a context delta, an outlier — evaluate it
under the v2 composition model. If it forms or strengthens a coherent local
resonance, the rewrite should carry it. If it does not survive grounding and
containment, note it in friction.

## What not to do

- Do not re-derive findings from scratch when the existing prose already has
  them. The existing prose was written from the same bundle. Use it.
- Do not import new material from outside the bundle. The bundle is the
  evidence boundary.
- Do not name surah-wide systems, assert maturity, or state a thesis. The
  existing prose may not have done this either, but verify.
- Do not force a resonance that is not there. If the existing prose has no
  coherent secondary image and the bundle does not support one, the rewrite
  uses the no-resonance composition (opening → word-built → closing).

## Output

Same as `PROMPT.md` (v2): prose, evidence surface, index, and friction. The
friction report should note what changed structurally from the original and
whether any findings were gained or lost.
