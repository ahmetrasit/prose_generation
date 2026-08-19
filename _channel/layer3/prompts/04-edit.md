# Pass 2B: Editorial Revision Of Prelude And Postlude

Revise the Layer-3 draft editorially without reducing its interpretive yield or
changing its admission and evidentiary judgments.

Set `phase` to `editorial`, `revisionOf` to the draft's `compositionId`, and
`compositionId` to `{packetId}-composition-v2`.

## Preserve The Semantic Contract

Keep the primary footing and every admitted channel, concrete member, hinge,
claim boundary, and distinct reader payoff. Do not rank, disambiguate, merge, or
drop them during revision. Merge prose only when it performs the same image work
and gives the same reader payoff.

Do not add channels from the selected Layer-2 prose. Do not convert local-only
material into a surah-wide claim.

## Keep The Two Reader Moments Distinct

The prelude must still prepare rather than resolve:

- retain one compact surface foothold;
- retain one concrete promise per admitted channel;
- remove proofs, exhaustive member sequences, and completed payoffs that arrived
  too early.

The postlude must still complete and reinforce:

- retain every channel, member image, and hinge;
- make the cross-ayah operation and whole-surah gain unmistakable;
- let the ending return to the primary surah with changed understanding.

Do not turn either surface into an ayah-by-ayah retelling. Do not make the
prelude a compressed copy of the postlude.

## Editorial Standard

Rewrite as fluent, contemporary prose for a regular reader. Remove analyst
shorthand, workflow language, stiff technical calques, defensive repetition,
and evidence-catalogue rhythm. Explain a concrete effect before naming any
technical term that remains necessary.

Use reader-facing subtitles only at real changes of movement. Create continuity:
each section should inherit an image, question, tension, relation, or motion and
carry it somewhere new. Keep distinct findings recoverable without repeatedly
announcing another image.

Keep each non-obvious image attached to the text for a regular reader. On first
use in either surface, give at least one light ayah/word anchor such as
"1:6'daki yol isteği" or "1:7'deki iyiliğe ulaştırılanlar". If the image depends
on a specific Arabic word rather than a whole surface phrase, include a compact
structured span after the ordinary Turkish sense:
`1:6'daki yol, {ar:ٱلصِّرَٰطَ, tr:es-sırât, gloss:yol}`. These anchors must feel
like orientation inside the prose, not footnotes, evidence labels, or a return
to ayah-by-ayah retelling.

Remove duplicated headings, paragraphs, closing recaps, and stray draft tails.
Do not compress merely to shorten the text. There is no length or section quota.

Update every evidence span so it occurs exactly once in the revised surface.
The evidence map must continue to cover exactly the required primary groundings,
prelude promises, postlude channels, postlude members, and postlude hinges.

## Output

Write `N.surah-composition.{language}.json` as a JSON object conforming exactly
to the inlined schema. Write no other files.
