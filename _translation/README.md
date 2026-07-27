# Translation — layer 1

Translation here is the **spine**: a join key that anchors a fluent target
language to the Arabic, not a content surface and not a sequence of dictionary
glosses. It has three connected parts:

1. the complete ordered QAC morpheme spine;
2. each rooted stem's selected root and primary branch, plus a target-language
   card gloss; and
3. a fluent target-language ayah whose display words map back to QAC morphemes.

Its job in the system is to hold the primary reading **still**. Layers 2 and 3
perturb that reading; they can only do so because layer 1 fixes it and does not
move.

## Source policy

The Turkish V12 baseline is the primary reading scaffold. Its wording and
QAC-word mapping constrain the translation without forcing Turkish syntax on
another language.

Only the direct lexical branch that governs the primary reading becomes a card
anchor. Strong V12 findings may contain non-translational resonance branches;
those do not become primary translation branches — but they are **recorded as
rejected**, not discarded, and handed to the commentary layers
(`../PRINCIPLES.md` §6, decision D4 in [`v1/README.md`](v1/README.md)).

Reviewed glosses under `dictionary/v2/gloss_generation/results/{language}` supply
controlled target-language wording for the selected branch. The card gloss is
occurrence-specific and may narrow that curated wording according to the QAC form
and local construction.

Particles, articles, pronouns, and affixes remain independent QAC cards but do
not receive invented root or branch IDs.

## What joins later, and does not live here

Deliberately absent from the artifact, and joined downstream by ID:

| content | joins by |
| --- | --- |
| gloss alternatives (up to three per word) | `(rootId, branchId, language)`, narrowed by `qacWordRef` |
| error profiles — losses, additions, narrowings, collisions | same |
| the "check the other glosses" flag | computed at join time from the error profile against the selected occurrence gloss |
| word analysis | QAC crosswalk on `qacWordRef` |
| commentary and channels | `qacRef` / `ayahRef` |

Keeping these out is what makes layer 1 small, stable, and cheap to re-run when
`quran-data` releases. See decision D5.

## Language model

QAC, root, and branch identities are shared across languages. Branch **selection**
is shared too — it lives in `v1/source/sNNN.primary-anchors.json`, outside
`input/{language}/`, so two languages cannot disagree about which branch is
primary.

Each language authors its own card glosses, fluent translation,
target-word-to-QAC mapping, and language policy.

## Current workflow

The runnable pilot, schema, prompt, bundle builder, cold-agent orchestration,
recorded design decisions, and outputs are under [`v1`](v1/README.md).
