# Pass 1B: Review Channels and Resonances

Build the Layer-3 channel briefs from the discovery hypotheses, typed primary
ground, complete Layer-2 findings index, local resonances, preserved
boundaries, activation cards, and bounded secondary material.

Do not write final reader prose.

## Admission Rule

A channel is a cross-ayah recognition that depends on secondary semantic
material. It must change how a regular reader understands the surah in a way
that cannot be reached from the ordinary translated surface alone.

For each possible channel, state the ordinary surface floor and ask:

> If every secondary semantic contribution were hidden, could a thoughtful
> reader still reach materially the same changed understanding from the
> translation and sequence alone?

If yes, the material may still be useful, but it is not a Layer-3 channel. If
no, identify what the secondary material makes newly thinkable and how distant
movements work together.

Non-derivability is necessary but not sufficient. A channel must also make a
specific feature, tension, transition, or ending of the surah newly legible. It
fails when it only adds ornament, a movable metaphor, or a moral topic that
could be transferred to many other texts without changing the reading.

## Handoff Discipline

The Layer-2 findings index is live. Use it as typed local evidence, not as
prose to copy. Local resonances are especially important because they mark
where an ayah already opens beyond its primary floor.

Account for every discovery hypothesis and every local resonance. Each input
may support more than one channel. Multiple inputs may support the same
channel. When an input does not become part of any channel, give it one
non-channel disposition.

Do not treat `merged` as a disposal category. If a hypothesis or resonance is
absorbed into a channel, include its input ref in that channel. If it is not
used, give the actual reason it did not become a channel.

## Coexistence

This is not disambiguation. Do not decide that one resonance is the correct
meaning and another is wrong. Do not rank channels. Do not collapse competing
channels unless they create the same reader movement. Incompatible channels may
coexist when each produces a distinct changed understanding and respects the
evidence boundaries.

Weak, remote, or counterpressured material may participate when it remains
bounded. Its uncertainty controls the `claimPolicy`; it does not automatically
remove the resonance from the field.

## Boundaries

A preserved rejection or boundary prohibits a local identity claim,
translation replacement, event claim, or sentence form. It does not erase the
surviving semantic contribution. Preserve the limit in `claimPolicy`, then ask
whether the contribution can still operate across the surah without requiring
the prohibited claim.

Do not turn boundaries into final prose or an evidence catalogue. Record only
what the composer must avoid or qualify.

## Brief Shape

For each admitted channel, provide:

- a reader-facing name;
- all input refs it uses;
- the ordinary surface floor and primary-floor refs;
- stable hinge IDs;
- each hinge's plain-language contribution, ayah refs, evidence refs, and
  claim policy;
- the cross-ayah operation;
- the reader's before/after shift;
- the indispensable gain that disappears if the secondary material is removed.

There is no quota for channels, hinges, paragraphs, words, or length. Do not
compress significant findings to satisfy a shape target.

## Output

Write `N.channel-briefs.{language}.json` as a JSON object conforming exactly to
the inlined schema. Use the target language for reader-facing fields. Write no
other files.
