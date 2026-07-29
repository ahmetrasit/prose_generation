# Pass 3: Compose the Surah Reading

Write the Layer 3 reader experience from the reviewed system ledger.

## Audience

Assume the reader:

- has an ordinary translation-level understanding of the surah;
- knows no Arabic;
- knows no linguistic terminology;
- wants to understand how semantic structures beneath the primary reading can
  expand or shift that understanding.

## What the Prose Must Do

Begin inside a concrete scene, movement, or tension already present in the
ordinary reading. Then let the reviewed systems emerge as an ordered sequence
of recognitions.

The reading must:

- keep the primary reading visible throughout;
- make distant parts of the surah explain one another;
- deliver the ledger's `ahaMoments` through prose rather than announcing them;
- explain a wider semantic field in plain language and immediately state its
  interpretive payoff;
- move as one argument even when several systems contribute;
- end with a changed view of the surah, not a recap.

## What the Prose Must Not Do

Do not:

- summarize the surah;
- proceed ayah by ayah;
- create one section per channel or source;
- list roots, branches, candidates, or semantic fields;
- mention V11, V12, network-v3, Layer 2, evidence grades, confidence, prompts,
  schemas, agents, or review;
- say that a word "really means" a secondary image;
- smuggle a prohibited rejected predication back as metaphor;
- require the reader to understand Arabic before receiving the payoff;
- open with a methodological explanation.

Arabic words may appear only when a specific surface word is indispensable to
the recognition. Give its ordinary translated sense first. Never display root
skeletons or identifiers.

## Form

Write continuous, engaging prose in the packet's target language. A literary
title is allowed. Internal headings are discouraged; use them only if removing
them would make a long reading genuinely harder to follow.

Each paragraph must advance the system. A paragraph that could move anywhere
without changing the argument probably belongs in apparatus.

## Evidence Surface

After writing the prose, map every paragraph to:

- one or more reviewed system IDs;
- the packet source fragments supporting its claims;
- any structural inference;
- the primary element kept recoverable;
- the reader shift advanced there.

Evidence language stays out of the prose.

## Output

Write exactly:

1. `N.surah-reading.md`
2. `N.surah-reading.evidence.json`
3. `N.surah-reading.friction.md`

The evidence JSON must conform exactly to the inlined schema. Friction records
instruction or evidence limitations only; it is not a second commentary.
