# Pass 1B: Review Concrete Channels and Resonances

Build Layer-3 channel briefs from the discovery hypotheses, typed primary
ground, complete Layer-2 findings index, local resonances, preserved boundaries,
activation cards, and bounded secondary material.

Do not write final reader prose.

## Admission Rule

A channel is a coherent secondary image or working system that recurs across
ayahs and changes the assembled surah. It must depend substantially on semantic
material that an ordinary translation does not select.

Test the concrete system, not an abstract paraphrase of its conclusion:

> If the secondary material were hidden, could a thoughtful reader still
> recover this concrete image, its participating members, and the same
> cross-ayah operation from the translation alone?

It is not enough that a broad conclusion such as "mercy supports guidance" or
"actions have consequences" is surface-derivable. A water-provisioning system,
a road made and maintained by repeated walking, or a gift-return circuit may
still qualify when that specific system and its surah-level work are secondary
dependent.

Non-derivability is necessary but not sufficient. The image must also make a
specific opening, transition, tension, ending, or distant relation in this surah
newly legible. Reject ornamental analogy, but do not call an image "portable"
merely because its broad moral can be stated elsewhere. Test whether this exact
network of members performs specific work here.

## Build Before Accounting

First construct every coherent candidate channel at its natural granularity.
Only after the channel field is stable should you write non-channel
dispositions. Do not let the accounting ledger determine the number or breadth
of channels.

The Layer-2 findings index is live typed evidence. `localResonances` mark
explicitly typed local surprise, but they are not necessarily exhaustive.
Inspect all findings for concrete image lines whose editorial index may not
carry a `surprise:` prefix, including grounded findings with a
`primaryRelation` and writer syntheses marked `inference`.

Every discovery hypothesis and typed local resonance must finally support at
least one channel or receive one non-channel disposition. Inputs can be
many-to-many.

## Granularity And Coexistence

Merge inputs only when they produce the same concrete image movement and the
same reader payoff. Shared ayahs, vocabulary, or a broad primary conclusion do
not justify merger. Water provisioning, protected passage, restored sight, and
structural repair must not disappear into one generic "supported path" merely
because they all touch guidance.

Do not rank channels or select one as the governing interpretation.
Incompatible channels may coexist when each has distinct anchors, operation,
and yield. Weak, remote, or counterpressured material may participate when its
limits are explicit in `claimPolicy`.

Use these non-channel reasons precisely:

- `local-only`: no recurrence beyond one ayah;
- `surface-image`: the concrete image itself, not merely its broad conclusion,
  is recoverable from the primary surface;
- `same-image-and-payoff`: another admitted member carries the same mechanism
  and reader gain; name that mechanism in the explanation;
- `fails-secondary-dependence`: the claimed system does not materially depend
  on secondary semantic evidence;
- `fails-whole-surah-yield`: recurrence exists but changes no specific
  surah-level relation;
- `unsupported`: the required anchors or evidence do not survive review.

Boilerplate explanations are not acceptable. Each explanation must identify
the concrete mechanism, missing recurrence, missing evidence, or already
represented payoff.

## Boundaries

A preserved rejection or boundary prohibits a local identity claim,
translation replacement, event claim, or sentence form. It does not erase the
surviving semantic contribution. Preserve the limit in `claimPolicy`, then ask
whether the contribution can still work across the surah without the prohibited
claim.

Do not turn boundaries into final prose or an evidence catalogue. Record only
what the composer must avoid or qualify.

## Reference Discipline

Use typed review-context identifiers for channel accounting and evidence. Do
not copy provenance `sourceRefs` into member or hinge `evidenceRefs`.

The permitted evidence-reference forms are:

- `finding:*` for Layer-2 findings;
- `resonance:*` for local resonances;
- `activation:*` for activation cards;
- `boundary:*` for preserved boundaries;
- `secondary:*` for bounded secondary material;
- primary-floor refs such as `primary-floor#1:1` only for surface-floor
  grounding fields.

For every local resonance used by a member or hinge, include both its exact
`resonanceRef` and paired `findingRef` in `evidenceRefs`. Provenance labels such
as `layer2-index-1-1#line-27` are not substitutes.

Set `briefId` to `{packetId}-briefs-v3`, using the packet id from the inlined
review context.

## Brief Shape

For each admitted channel, provide:

- a reader-facing name plus a concrete `imageSystem`;
- a `systemBoundary` saying what belongs and what would be mere topic overlap;
- all input refs it uses and the ordinary surface floor it preserves;
- `memberLandings` that keep each participating ayah's distinct concrete
  contribution recoverable;
- hinges that name the image movement between at least two members;
- the cross-ayah operation and reader before/after shift;
- the indispensable secondary gain;
- a `preludePromise` that can prepare the reader without resolving the system;
- a `postludePayoff` that can complete the recognition after the ayah readings.

Every accepted channel must have members in at least two ayahs. Every hinge must
connect at least two named members and preserve their distinct contributions.

There is no quota for channels, members, hinges, words, or length. Do not
compress significant findings to satisfy a shape target.

## Output

Write `N.channel-briefs.{language}.json` as a JSON object conforming exactly to
the inlined schema. Use the target language for reader-facing fields. Write no
other files.
