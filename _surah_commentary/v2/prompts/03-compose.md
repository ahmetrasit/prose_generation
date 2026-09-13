# Pass 2A: Compose Prelude And Postlude Drafts

Write the complete Layer-3 draft from the reviewed channel briefs. Produce two
reader surfaces from one accepted semantic model: a pre-surah orientation and a
post-surah synthesis.

Set `phase` to `draft`, `revisionOf` to `null`, and `compositionId` to
`{packetId}-composition-draft-v2`.

## Argument And Channels

The primary argument and the secondary channels are different axes. Establish
only the compact surface footing needed for orientation. Do not let the primary
argument suppress the images, and do not make a secondary channel replace the
primary reading.

Do not retell the surah in ayah order. Do not write one paragraph or primary
claim per ayah. If the prose can be decomposed into a sequence of ayah summaries,
it has failed at Layer 3.

## Prelude: Promise Without Resolution

The prelude prepares the reader to notice what the ayah-level readings will make
visible.

- Give one compact primary-grounded foothold for the whole surface.
- Let every admitted channel appear once as a concrete image, tension, question,
  or motion to watch for.
- Preserve controlled incompleteness. Do not prove the channel, enumerate all
  member ayahs, discharge every hinge, or state the full postlude payoff.
- Do not present a catalogue. Let the promises form one anticipatory movement.

The prelude is not a shortened postlude. It should make the reader attentive
without replacing the experience of the ayah commentaries.

## Postlude: Completed Recognition

The postlude reinforces and assembles what the reader has encountered locally.

- Every admitted channel, member landing, and hinge must become visible in
  ordinary reader language.
- Preserve each materially distinct image and payoff. Do not collapse water,
  passage, sight, repair, gift, belonging, or another admitted mechanism into a
  generic thesis merely because they meet in the same surah movement.
- Trace how the image changes distant ayahs and why the opening, transition, or
  ending now works differently.
- Return naturally to the surah's primary force at the end, showing what has
  become newly visible rather than listing findings.

## Selected Layer-2 Reader Prose

The composition input includes reader-facing Layer-2 prose only for ayahs that
participate in admitted channels. Use it to recall concrete language and create
recognizable reinforcement. It is not permission to import every local reading,
form new channels, or follow the ayahs chronologically. Only material admitted
by the channel briefs may enter Layer 3.

## Prose Movement

Write fluent contemporary prose for a regular reader. Meaning comes before
terminology. Use short reader-facing subtitles only at genuine changes of
movement. Each section should inherit a concrete image, relation, question, or
motion from the preceding section and carry it somewhere new.

Do not preserve brief boundaries as prose units. Do not give each channel or
hinge an isolated paragraph merely to satisfy accounting. Distinct gains must
remain recoverable inside one developing composition.

Keep the reader oriented to where images come from. When a non-obvious image or
system first becomes active in either surface, attach it lightly to at least one
representative ayah number and surface word or phrase, for example "1:6'daki yol
isteği" or "1:7'deki iyiliğe ulaştırılanlar". If the image depends on a specific
Arabic word rather than a whole surface phrase, include a compact structured
span after the ordinary Turkish sense:
`1:6'daki yol, {ar:ٱلصِّرَٰطَ, tr:es-sırât, gloss:yol}`. Do not assume the reader
has memorized the Layer-2 ayah commentaries. Use these anchors as reader-facing
orientation, not as footnotes or apparatus.

Arabic words may appear when they provide that necessary attachment point; give
the ordinary translated sense first. Never present a secondary contribution as
the word's real translation, a hidden replacement meaning, or a historical
event.

Treat every `claimPolicy` as a silent writing boundary. Include a brief
containment correction only when a prohibited claim would otherwise be a likely
reader mistake.

Do not display roots, branch IDs, finding refs, resonance refs, activation refs,
source labels, packet IDs, schema names, confidence labels, workflow vocabulary,
or agent vocabulary in either reader surface. Ayah numbers and surface-word
anchors are allowed and expected; they are not evidence apparatus.

There is no paragraph, word, channel, or length quota. Give every significant
image enough room. Do not inflate light material.

## Evidence Map

Return one JSON envelope conforming to the inlined schema.

- `primaryGroundings`: exactly one compact grounding span from each surface;
- `preludeChannelPromises`: exactly one anticipatory span for every channel;
- `postludeChannelLandings`: the operation and gain of every channel;
- `postludeMemberLandings`: one exact span for every concrete member;
- `postludeHingeLandings`: one exact span for every hinge.

Each recorded span must occur exactly once in its designated surface. Evidence
mapping is not a reason to repeat or isolate prose.

Use `friction` only for unresolved publication risks.

## Output

Write `N.surah-composition.draft.{language}.json` as a JSON object conforming
exactly to the inlined schema. Use the target language for reader-facing fields.
Write no other files.
