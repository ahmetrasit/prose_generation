# Commentary v5 editorial handoff

Continue as the same live consolidator for **@@AYAH_REF@@**. Revise the
first-pass prose under the editorial instructions below and write the editorial
prose output. Modify nothing else, except for the mechanical validator command
and any required monitor lifecycle event command supplied by the orchestrator.

This V5 editorial handoff modifies prose only. Any historical instruction in
embedded governing documents to create evidence surfaces, indexes, friction
reports, ledgers, manifests, landing maps, hashes, or audit artifacts does not
apply to this handoff. You may run the mechanical validator command named below;
that command is a prose-file format check, not an audit artifact. You may also
run the monitor lifecycle event command supplied by the orchestrator; it is
operational logging, not commentary evidence.

## Editorial Contract

Reshape the draft into fluent Turkish with directed, continuous attention while
preserving every distinct retained semantic movement. Treat its paragraph
boundaries, headings, and order as revisable.

Preservation binds supported findings, not factual mistakes. The scope prose
and ledgers already in this conversation are your complete evidence boundary.
Actively compare the draft with them and correct demonstrable errors in ayah
attribution, Arabic surface, case, syntax, morphology, lexical identity,
translation, or semantic detail, even when an error appears repeatedly in the
draft. Preserve the retained relation while correcting its expression. Do not
inspect upstream evidence, guess beyond the supplied inputs, add a finding, or
silently delete one.

Every resonance must preserve the ordinary reading intact and keep it
recoverable in the same explanation; a latent reading cannot replace it.

- Preserve every retained finding's carrier, independent trigger, contact,
  changed reading, concrete semantic detail, and boundary.
- Preserve useful section subtitles, or add short Turkish section subtitles
  when they make the editorial prose easier to follow. Mark each subtitle as a
  level-2 Markdown heading, for example `## Taşın Hafızası`, so downstream
  renderers can style it separately. Subtitles are reader prose, not wrappers;
  do not use generic labels such as `# PROSE`, `=== PROSE ===`, or XML-style
  prose wrappers.
- Preserve concrete images and secondary branches. Do not flatten a pathology,
  material image, repeated action, spatial relation, or before/after shift into
  a general theme.
- Keep each boundary attached to the interpretation it limits. A warning
  against literal translation does not authorize deleting the contextual
  resonance being bounded.
- No first-pass sentence is verbatim-immutable. Rewrite awkward, repetitive,
  malformed, or English-leaking sentences freely, but keep the underlying
  finding coverage.
- Revise complete explanatory passages. When an explanation moves, move its
  source construction, operative details, qualifications, and necessary
  paragraph-local Arabic anchors with it. Restore a displaced element where it
  participates in the reading.
- Build transitions from something the preceding passage has made intelligible.
  Show what the next action, source use, speaker, sound, grammatical relation,
  temporal turn, material process, contrast, or question changes. Where no
  supported continuity exists, make a deliberate cut by identifying the change
  of scale, time, speaker, question, or perspective instead of inventing a
  bridge.
- Complete every contextual excursion by returning to what it changes,
  clarifies, complicates, or leaves open in the focus reading.
- Build a multi-branch image from its contributing operations before stating
  the composite result. Do not replace its construction with a broad thematic
  summary or announce the result and then list its supports.
- Combine passages only when their sources, operations, effects, and limits
  remain distinguishable. Remove repeated wording only after confirming that
  it contributes no distinct operation, detail, interaction, change, or
  qualification.
- Preserve the project display tag syntax at Arabic anchor points:
  `{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}`. Tags are
  paragraph-local. A tag in an earlier paragraph does not cover a later
  paragraph. Repeated tags are required when the same Arabic item does
  interpretive work again in a new paragraph, because downstream TTS and reader
  masking depend on paragraph-local tags. Do not remove, deduplicate, reduce, or
  merge tags; do not convert tagged anchors to plain Arabic/transliteration, add
  QAC IDs, or invent another tag shape.
- Use one consistent Turkish-readable transliteration for an identical Arabic
  surface. Preserve differences grounded in genuinely different Arabic forms
  or readings. Keep tag glosses short and ordinary; place lexical restrictions,
  activated images, mechanisms, and consequences in the prose.
- Reader-facing prose must be Turkish. Translate English phrases and analytic
  terminology rather than copying them. Internal IDs, lane names, and QAC or
  analysis coordinates stay out of reader prose.
- When editorial prose uses a non-focus ayah as a contextual trigger, contrast,
  echo, or source of resonance, make the Quran reference visible in the same
  sentence or clause, usually in compact parentheses such as `(29:41)`. If a
  single movement depends on several ayat, list every ayah explicitly, such as
  `(29:17, 29:25)` or `(1:6, 1:7)`. Do not use ayah interval shorthand such as
  `(1:6-1:7)`, `(1:6-7)`, or `(29:45-46)`. Do not replace ayah references with vague
  phrases like "sûrenin ilerleyen yerinde", "bir yerde", "başka yerde", or
  "sonlara doğru" unless the concrete reference is also visible there. Use the
  workflow/context reference visible to the reader: a host prefatory basmala
  acting as context is cited as `(S:0)`, while `(1:1)` is used only when Al-Fatiha
  1:1 itself is being discussed as a separate source or alias.
- Compatible findings may share a fluent passage, but none may become implicit
  or disappear.
- A single raw paragraph may contain multiple retained findings or branches.
  Treat each distinct claim, image, branch activation, or interpretive movement
  as a separate mandatory landing. Each one must remain explicit in editorial
  prose.
- Do not relocate tags as an inventory, append displaced anchors, or create a
  late recap to compensate for omissions elsewhere. Repair the explanation in
  the passage where the reader needs it. An ending may complete a movement; it
  must not substitute a catalogue of findings for their integration.

Before finishing, compare the editorial prose against the raw prose and confirm
that every raw finding and every distinct retained landing still appears once
as an explicit substantive landing. Also confirm that every paragraph-local
Arabic anchor still uses the project tag syntax. Then test every inter-ayah or
contextual comment: if a non-focus ayah is doing interpretive work, its Quran
reference must be visible beside that comment. Confirm that every passage has a
clear object of attention, a legible change, and either a supported continuation
or an intelligible cut; that every contextual excursion returns to the focus;
and that interacting branches remain distinguishable. If any retained landing
is missing, any explanation has been displaced into a recap, any tag syntax is
damaged, or any inter-ayah comment lacks its visible reference, revise before
you consider the unit complete.

## First-Pass Inputs

- prose: `@@PROSE_INPUT_PATH@@`

## Editorial Outputs

- prose: `@@PROSE_OUTPUT_PATH@@`

## Mechanical Validation

After writing the editorial prose file, run this validator on the editorial
prose file only:

```bash
python3 _commentary/v5/validate_prose.py @@PROSE_OUTPUT_PATH@@
```

If the validator returns nonzero, repair only the reported mechanical
file-contract issues in the editorial prose file, then rerun the validator.
You may do at most two repair/rerun cycles. After two cycles, accept the
editorial prose as-is and report the remaining validator findings in this
conversation. Mechanical repairs include tag syntax, unsupported or duplicate
tag fields, unresolved placeholders, wrapper labels, empty/non-renderable prose
wrappers, malformed braces, and Arabic script outside valid paragraph-local
tags. The validator lists every detected issue, including every Arabic-outside
span, in compact line-oriented output. Do not use validator failures to add new
evidence, drop findings, reopen evidence selection, create ledgers, create
hashes, write a separate validation report, validate scope prose, validate
first-pass prose, or launch another agent.

<editorial_instructions>
@@EDITORIAL_INSTRUCTIONS@@
</editorial_instructions>
