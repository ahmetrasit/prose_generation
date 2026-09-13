# Pass 1A: Blind Cross-Ayah Image-System Discovery

Search for text-bound secondary images or working systems that recur across the
surah and can change how a regular reader sees the assembled text.

Do not write commentary, a surah summary, a primary-grounded thesis, evidence
review, or final channel briefs. This pass opens materially distinct
possibilities. Later review decides what qualifies.

## Input Boundary

Use only the inlined discovery input:

- Quran surface anchors and typed primary-floor lines;
- mechanically projected activation cards from reviewed Network material;
- coverage warnings.

The input intentionally excludes Layer-2 prose, Layer-2 findings, Layer-2
boundaries, V11 prose, prior Layer-3 synthesis, and outside sources. Do not
reconstruct those materials from memory or provenance paths.

Activation cards are search signals, not translations, conclusions, rankings,
or ready-made prose plans.

## What To Discover

A useful hypothesis is a concrete image or system, not an abstract topic or
moral conclusion. Rain, collected water, a well, irrigation, growth, and
settlement may form a provisioning system. "Care," "mercy," or "guidance" by
themselves do not describe an image system.

For each possible system, establish:

- the concrete scene, material process, spatial relation, bodily action, social
  arrangement, or exchange that holds it together;
- at least two ayahs in which different members of that system become active;
- what each ayah contributes to the same system;
- the boundary that keeps the system coherent rather than merely thematic;
- what transition, opening, ending, agency relation, or distant movement in
  this surah becomes newly legible.

Use the image-deletion test: if all concrete image language can be removed and
the hypothesis still says materially the same thing, it is too abstract.

## Divergent Search

Move card by card before converging. Test materially different families such as
movement and passage, water and provisioning, cultivation and repair, gift and
return, embodiment and support, marking and visibility, belonging and
dispersal, accounting and exchange, shelter and formation, or conflict and
resistance whenever the supplied cards license them. This list directs search;
it does not license an unsupported family.

One activation card may support several hypotheses. Related cards need not be
forced into one hypothesis. Preserve competing and countervailing systems when
their concrete mechanisms or reader payoffs differ.

Do not favor the broadest, safest, or easiest-to-defend account. Weak or remote
possibilities may remain hypotheses when they are anchored, bounded, and create
a distinct reader movement. Do not rank, merge, certify, reject, or narrow in
this pass.

## Reader Delta

The eventual reader knows a normal translation but has no Arabic or linguistic
training. Record:

- `before`: what the translated surface already allows;
- `hinge`: the precise secondary image relation that unsettles or extends it;
- `after`: the changed surah-level recognition.

The `after` field must preserve the concrete system. Do not translate it into a
generic claim such as "the surah is about care."

## Coverage

After opening hypotheses, account once for every supplied activation card in
`activationCardCoverage`.

- List every hypothesis that used the card.
- If none used it, state which concrete family was tested and why no coherent
  cross-ayah hypothesis formed.
- Coverage is a search audit, not a rejection ledger. A card with no hypothesis
  is not thereby declared false or valueless.

Do not compress significant hypotheses. There is no quota for hypotheses,
members, words, or length. The output should be as large or small as the
supplied material warrants.

## Output

Write `N.discovery-hypotheses.{language}.json` as a JSON object conforming
exactly to the inlined schema. Use the target language for reader-facing fields
and concise English only for fixed keys. Write no other files.
