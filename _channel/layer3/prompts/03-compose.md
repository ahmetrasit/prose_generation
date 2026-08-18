# Pass 2: Compose the Layer 3 Reading

Write the Layer-3 surah reading from the reviewed channel briefs.

The reader knows a normal translation of the surah and has no Arabic or
linguistic training. Establish only the ordinary surface ground needed for the
argument, then make the changed understanding opened by the channels visible
in plain language.

## Channel Visibility

Every admitted channel must land in the prose. Every hinge in every admitted
channel must also land in the prose. A regular reader should be able to say:

- what ordinary surface scene is still being honored;
- what wider semantic contribution has entered;
- how that contribution moves across more than one ayah;
- what new understanding becomes possible.

Do not hide channels behind general summary. Do not enumerate technical
evidence. Make the resonance readable as part of the argument.

## Coexistence

This is not disambiguation. Do not choose one channel as the only correct
reading. Incompatible channels may live at the same time when the briefs admit
them. Write the coexistence as layered pressure, alternate but bounded
recognition, or simultaneous resonance rather than as a winner/loser decision.

Do not collapse channels merely because they touch the same ayah or image. Do
let them meet in one prose movement when each distinct reader gain remains
visible and the evidence map can still point to exact spans.

## Hinge Language

Meaning comes before terminology. Arabic words may appear only when a specific
surface word is indispensable; give its ordinary translated sense first.

Do not say a word "really means" the secondary contribution. Do not present a
secondary contribution as the translation, a hidden replacement meaning, or a
historical event. A useful movement is: the ordinary meaning remains in place,
while the wider field lets the scene resonate with another ayah. Use that
movement naturally rather than as a formula.

Selective word analysis may remain alive inside the prose when it helps the
reader feel the channel or local resonance. Keep it subtle: bring the word's
surface role or wider field into the sentence, then return to the reader's
changed understanding. Do not create a lexical note unless the channel depends
on it.

## Boundaries

Treat each `claimPolicy` as a silent writing boundary. If a prohibited claim
would be a likely reader mistake, include a short containment correction in
ordinary language. Otherwise, simply avoid the prohibited claim and let the
permitted resonance operate.

Do not display roots, branch IDs, finding refs, resonance refs, activation
refs, source labels, packet IDs, schema names, prompt names, confidence labels,
workflow vocabulary, or agent vocabulary in the prose.

## No Quota

There is no paragraph quota, channel quota, word target, minimum length, or
maximum length. If a significant channel or hinge needs room, write it fully.
If the material is light, do not inflate it.

Begin inside the argument, not with methodology. End inside the final changed
understanding, not with a recap or list of findings.

## Evidence Map

Return a JSON composition envelope, not a markdown-only reading.

The `prose` field is the publishable reading. The `evidenceMap` must identify
exact prose spans for:

- primary claims grounded in the typed primary floor;
- every admitted channel's operation and gain;
- every admitted hinge.

Each span must occur exactly once in `prose`. This is how the finalizer proves
that the reader-visible prose did not drop a channel or hinge.

Use `friction` for unresolved publication risks, not for notes that belong in
the prose.

## Output

Write `N.surah-composition.{language}.json` as a JSON object conforming exactly
to the inlined schema. Use the target language for reader-facing fields. Write
no other files.
