# Layer 3 Channel Commentary with Layer 2.5 Handoff

## Authority Boundary

The network/v12 channel files and their branch identities are already reviewed.
This workflow reuses them as settled evidence. It performs no second admission,
rejection, scoring, or review pass.

Layer 3 has a compositional task: turn recurring reviewed resonances into a
surprising whole-surah secondary reading. Layer 2.5 has a disclosure task:
stage that reading through unchanged Layer-2 ayah prose as its members become
available.

## Inputs

The compact bundle carries:

| field | purpose |
| --- | --- |
| `reviewedChannels` | reviewed channel meaning, synthesis, and source keys |
| `text` | Arabic reading order |
| `anchorInventory` | Quran occurrence and root identity |
| `motifAnchorMap` | reviewed root/branch citations joined to occurrences |
| `primaryFloor` | canonical Turkish primary translation |
| `primaryBranchMap` | mechanical primary/non-primary classification |
| `coverage` | compact provenance and identity audit |

Instantiation adds only canonical Layer-2 prose. It does not repeat Layer-2
evidence or findings indexes.

## One Authored Pass

The writer:

1. derives the primary-grounded whole-surah argument;
2. composes related reviewed channels into coherent reader-facing images;
3. writes the completed surprising secondary reading;
4. derives each image's maturity in Quran reading order;
5. writes Layer-2.5 insertion prose and placement metadata;
6. accounts for every reviewed source as integrated or apparatus-only.

`apparatus-only` means valid reviewed evidence was not rendered in this prose
composition. It is not rejection.

## Outputs

Authored:

- `{N}.surah.prose.md`
- `{N}.surah.thesis.md`
- `{N}.surah.channels.integrated.json`
- `{N}.ayah-channel-overlays.json`
- `{N}.surah.exclusions.md`
- `{N}.surah.evidence.md`
- `{N}.channel.friction.md`

Deterministically rendered after validation:

- `{N}.ayah-channel-overlays.preview.md`

The cold Layer-2 prose remains canonical and unchanged.

## Verification

The workspace verifies:

- every member belongs to a resolved reviewed QAC/root/branch mapping;
- every `primaryStatus` agrees with `primaryBranchMap`;
- every reviewed source is accounted for exactly once;
- maturity never runs backward or recalls unseen members;
- integration and base prose paths are SHA-256 bound;
- overlay placement anchors exist in the declared base paragraph;
- the preview is rendered from validated JSON rather than authored separately.
