# Translation

Translation here is a linguistic authoring layer, not a sequence of dictionary
glosses. It has three connected parts:

1. the complete ordered QAC morpheme spine;
2. each rooted stem's selected root and primary branch, plus a
   target-language card gloss; and
3. a fluent target-language ayah whose display words map back to QAC
   morphemes.

## Source policy

The Turkish V12 baseline is the primary reading scaffold. Its wording and
QAC-word mapping constrain the translation without forcing Turkish syntax on
another language.

Only the direct lexical branch that governs the primary reading becomes a card
anchor. Strong V12 findings may contain non-translational resonance branches;
those do not become primary translation branches.

Reviewed glosses under `dictionary/v2/gloss_generation/results/{language}`
supply controlled target-language wording for the selected branch. The card
gloss is occurrence-specific and may narrow that curated wording according to
the QAC form and local construction.

Particles, articles, pronouns, and affixes remain independent QAC cards but do
not receive invented root or branch IDs.

## Language model

QAC, root, and branch identities are shared across languages. Each language
authors its own:

- card glosses;
- fluent translation; and
- target-word-to-QAC mapping.

This lets word analysis join through QAC IDs and dictionary content join
through root and branch IDs without embedding either dataset in the
translation file.

## Current workflow

The runnable S1 pilot, schema, prompt, bundle builder, cold-agent
orchestration, and English output are under [`v1`](v1/README.md).
