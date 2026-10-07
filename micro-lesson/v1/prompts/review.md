# Review the linguistic correctness of finished lessons

Read every displayable lesson in the supplied ayah-based `page-output.json`.
Decide whether what the lesson teaches is linguistically correct. Review the
finished sentences, Arabic examples and Turkish readings in a fresh context.
Do not adopt the author's earlier reasoning or confidence as evidence.

This prompt is self-contained. The authoring instructions and their output
contracts do not apply to this review. Do not edit the lesson file during review.

## Inputs and evidence

Start with the finished lessons. Consult the relevant verse, morpheme analysis,
dictionary entry or other linguistic source when needed to assess a claim. The
original commentary can clarify the local context; it does not prove the claim.
Use the supplied evidence locations and read only the material the question needs.
There is no need to load the engine drafts, generation history or full ontology.

For lexical claims, consult the applicable root branch and lexical unit, including
their definitions, boundaries, Turkish glosses and per-gloss error profiles where
relevant. Interpret the profile in this occurrence: an appropriate contextual
narrowing is not automatically an error. A reviewed source label or morphological
annotation is useful evidence, not a guarantee that every associated claim is true.
If evidence conflicts or does not settle a material question, report uncertainty.

## What to assess

- Arabic forms and readings: spelling or vowels that affect the claimed form,
  segmentation, derivation, pronunciation, and connected versus pause readings.
- Grammatical claims: part of speech, subject/object and other syntactic roles,
  case, mood, tense/aspect, voice, agreement, pronoun reference, and what each
  particle, stem or suffix contributes.
- Meaning: the local Arabic sense, Turkish explanation or translation, root and
  word relationships, and distinctions between related words or constructions.
- Generalizations: whether a local observation has become a false general rule,
  or a possible interpretation, etymology or historical claim is stated as fact.

Read the actual assertion, not just its supporting anchor. For example, an isolated
verb cannot be translated as negative when an omitted particle supplies negation;
the meaning of a stem cannot be assigned to its pronoun suffix. A correct quotation
elsewhere in the record does not repair either claim in the teaching sentence.

Accept legitimate spelling/transliteration conventions and supported reading
variants. Do not mark a recognized, appropriately qualified grammatical analysis
wrong merely because another analysis is possible. A short explanation need not
list every exception, but its wording must not teach a materially false rule.
Flag ambiguous wording only when it produces a materially incorrect understanding,
not merely because another phrasing would sound better.

Generation procedure, provenance compliance, ontology placement, paragraph
attachment, ranks, prerequisites, style and discovery completeness are outside
this review. A grammatical assignment made in the lesson prose is in scope;
whether its ontology tag is the best attachment is not. Do not invent additional
lessons or review deferred drafts as though they were displayable content.

## Compact result

Return one line per displayable lesson, in the supplied order, using its exact ID:

```text
lesson_id | ok
lesson_id | flag | incorrect claim | correction and brief linguistic basis
lesson_id | uncertain | claim in question | exact unresolved question or needed evidence
```

- `ok`: no linguistic error found in the lesson's claims after reading them in
  context; no explanation is needed. This is not a guarantee of infallibility.
- `flag`: identify a concrete error and give the smallest supported correction.
  Include a compact source locator when it supplies the decisive evidence. If
  the false claim should be removed, say so instead of inventing a replacement.
- `uncertain`: identify a material question you cannot settle. Missing evidence
  alone is not proof that the claim is false; an unresolved claim is not `ok`.

If one lesson has several issues, keep one line and separate the issues with
semicolons. Use `flag` if any error is established, and explicitly retain any
additional unresolved question on that line. Use Turkish for issue descriptions
and corrections. Give no preamble, scores, whole-page verdict, rewritten page,
or generation audit. Already deferred opportunities need no result line.
