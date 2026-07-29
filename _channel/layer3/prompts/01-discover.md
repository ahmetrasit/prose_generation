# Pass 1: Discover Surah-Wide Systems

You are constructing the evidence architecture for a Layer 3 surah reading.
Do not write reader prose.

## Reader and Goal

The eventual reader knows no Arabic and no linguistics. The final reading must
begin from the ordinary reading and reveal secondary resonances that produce
recognition: the reader should see why distant parts of the surah now explain
one another.

This is not a summary, a commentary on each ayah in sequence, or a search for
the one correct hidden meaning.

## Method

1. Read all Layer-2 prose first to recover the ordinary movement and the local
   surprise already available to the reader.
2. Read Layer-2 evidence, V12 findings, network material, and V11 material as
   different evidence surfaces. Source labels do not determine truth.
3. Search for repeated **operations**, not merely repeated images or topics.
   An operation has direction and consequence: gathering becomes enclosure,
   enclosure becomes inversion, or nurture becomes yield.
4. Prefer systems in which later members explain earlier ones and earlier
   members prepare later ones.
5. Treat retrieval scores and strong/weak labels as ordering metadata. Never
   filter a finding merely because it is weak.
6. Treat a rejected predication locally. Record the rejected sentence in
   `prohibitedInference`; retain only the evidence contribution that survives
   without asserting it.
7. Keep the primary reading fully recoverable. A candidate that requires
   replacing an ordinary scene or word meaning fails containment.

## Candidate Standard

A useful system:

- spans at least two ayahs;
- has a governing operation, not only a topic label;
- has an ordered trajectory;
- explains why its members belong together;
- changes the reading of the whole surah;
- yields one or more precise "before -> after" reader shifts;
- can be stated without Arabic or technical vocabulary.

Generate enough candidates to preserve the field. Do not force them into a
predetermined number and do not rank them.

## Available Sources

Read every available source in the packet. Missing source families are recorded
in packet coverage; do not infer their contents and do not stop merely because
V11, V12, or network-v3 is absent. Record only limitations that materially
change what systems can be discovered.

Within each system, cite source fragments as precisely as the source permits:

- `source-id#100:8/finding-2`
- `source-id#C041`
- `source-id#F003`
- `source-id#PF0027`
- `source-id#paragraph-4`

The base before `#` must be a packet `sourceId`.

## Output

Write only `N.system-candidates.json`, conforming exactly to the inlined schema.
Use the target language for reader-facing fields and concise English only for
fixed enum values.
