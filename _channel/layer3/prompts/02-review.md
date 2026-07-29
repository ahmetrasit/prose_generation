# Pass 2: Review and Integrate Surah Systems

You are reviewing system candidates for a Layer 3 surah reading. This is
claim-scoped structural review, not lexical disambiguation and not prose
composition.

## Review Question

Which candidate systems genuinely let separate parts of the surah explain one
another, while keeping the ordinary reading intact?

Do not ask which secondary meaning is "correct." Ask what role each supported
semantic contribution can legitimately play.

## Tests

For every resulting system, test:

1. **Containment:** Does the primary reading remain fully recoverable?
2. **Recurrence:** Does the system operate across multiple ayahs?
3. **Direction:** Is there a transformation or causal order?
4. **Explanation:** Do members explain one another rather than share a label?
5. **Yield:** Is the whole-surah shift unavailable to isolated ayah readings?
6. **Grounding:** Can a reader with no Arabic follow the shift from ordinary
   translated words and scenes?
7. **Boundary discipline:** Are weak and rejected predications used only in the
   roles their evidence permits?

You may merge, split, or narrow discovery systems. Preserve their IDs in
`candidateSystemIds`.

## Rejected-Predication Rule

For a claim with `upstreamStatus: "rejected-predication"`:

- it may not have `role: "core"`;
- `retainedContribution` must state what survives;
- `prohibitedForm` must state what the prose must not claim;
- the system must remain coherent if the prohibited form is removed.

Do not convert a rejected sentence into a poetic metaphor that makes the same
assertion less visibly.

## Disposition Is Editorial

Do not rank systems. Assign an editorial role:

- `render`: a system the final prose should make the reader experience;
- `backbone`: an operation that joins rendered systems but should not become a
  separate catalogue entry;
- `support`: legitimate evidence absorbed by another system;
- `apparatus`: preserved for audit but not useful in the final reading.

The prose architecture should normally contain two to four `render` systems.
More is allowed only when they form one ordered movement rather than sections.

## Required Reader Shift

Every rendered system needs at least one `ahaMoment` with:

- what an ordinary reader is likely to see before;
- what becomes visible after the system;
- the exact hinge that produces the change.

Generic statements such as "the surah is deeper" fail.

## Output

Write only `N.system-ledger.json`, conforming exactly to the inlined schema.
Use the target language for reader-facing fields and concise English only for
fixed enum values.
