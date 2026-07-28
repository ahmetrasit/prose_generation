# Primary branch selection — layer 1, stage 0

You are given the complete candidate space for every rooted stem in one surah.
Select, for each stem, the one branch that governs its **primary reading**, and
record what you considered and did not choose.

This selection is **language-neutral**. It is shared by every target language, so
no target-language wording enters your output. If two languages disagree about
which branch is primary, one of them is wrong; this file is what makes that
disagreement impossible.

## What you are choosing

For each entry in `ayat[].rootedStems[]`:

- `branchIds` — normally exactly one branch from that stem's root in
  `roots[rootId].branchCandidates`;
- `lexicalUnitIds` — the lexical units in `roots[rootId].lexicalCandidates`
  whose `branchIds` include your selected branch and whose sense the occurrence
  actually realizes;
- `consideredNotPrimary` — every branch you weighed and rejected, each with a
  reason.

## The selection rule

Take the **direct lexical floor**: the sense the local form, construction, and
morphology select, as an ordinary competent reader of the Arabic would take it.

Not the richest branch. Not the most theologically loaded. Not the one that makes
the best commentary. Layer 1's whole job is to hold the primary reading still so
that later layers can perturb it; a branch chosen because it is interesting moves
the floor and there is nothing underneath it.

Use `morphology`, the ayah's `arabicText`, and `wordAnalysis.glossRange` when
present. `whatIsNotAr` states each branch's own boundary and is the fastest way
to eliminate a near neighbour.

### `v12Activated` is a candidate flag, not a recommendation

`branchCandidates[].v12Activated` records that the V12 run touched that branch in
this surah. The V12 v3 publication **flattens primary and resonance roles**, so
an activated branch is frequently a resonance the surah plays on rather than the
sense the word carries. Two recorded cases:

- `مَٰلِكِ` takes the "owner" branch. Its sovereignty branch is contextual —
  real, and not the floor.
- `عَٰلَمِينَ` takes the branch for created beings and worlds. The
  sign/landmark branch that V12 carried is explicitly non-translational
  resonance.

Both of those rejections belong in `consideredNotPrimary`. That is the point of
the field: the second one is the branch the Fātiḥa path channel runs on, and
until it was recorded it was being destroyed at this stage.

### `consideredNotPrimary` is not optional

Layer 2 is obliged to carry what layer 1 rejected. A rejection you do not write
down is evidence deleted, not a tidy output.

Record at minimum every branch marked `v12Activated` that you did not select.
Record any other branch you genuinely weighed. Do not pad the list with the
root's entire inventory — a branch that was never in contention was not
considered, and saying it was is false.

Each reason states why the occurrence does not realize that branch — one clause,
about this occurrence, not about the branch in general.

## Rules

- Emit exactly one anchor per rooted stem, in input order. Every
  `qacMorphemeRef` in the input appears exactly once.
- Use only branch ids and lexical unit ids present in that stem's root. Never
  invent one, and never carry one across roots — branch ids are scoped to their
  root, so `B002` means nothing without it.
- `consideredNotPrimary` and `branchIds` are disjoint.
- Select more than one branch only when the occurrence genuinely realizes both
  at the lexical floor. This is rare; a second branch is not how you record a
  resonance, `consideredNotPrimary` is.
- If the candidate space cannot support a responsible selection, put the stem in
  `unresolved` with a reason rather than guessing. An unresolved stem blocks the
  surah, which is correct: a guessed floor is worse than a stalled one.
- No target-language content anywhere in the output.

## Output

Write only this JSON artifact:

```json
{
  "schemaVersion": "primary-anchor-seed-v2",
  "surah": 103,
  "anchors": [
    {
      "qacMorphemeRef": "103:1:1:3",
      "branchIds": ["B001"],
      "lexicalUnitIds": ["lu_001"],
      "consideredNotPrimary": [
        { "branchId": "B004", "reason": "…" }
      ]
    }
  ],
  "unresolved": []
}
```

`lexicalUnitIds` may be empty when no candidate unit matches the occurrence.
`consideredNotPrimary` may be empty only when the root has one branch.
