# Adversary Review Closure

## Architecture Invariant

Reviewed channel files and branch identities are input authority. This workflow
does not review them again.

Layer 3 composes reviewed sources into reader-facing whole-surah images. Layer
2.5 derives when those images may become visible in reading order.

## Closed Findings

| finding | resolution |
| --- | --- |
| downstream work was mislabeled reviewed | removed `reviewState`, `reviewDecision`, reviewer records, rejection lists, and `.reviewed.json`; output is `.integrated.json` |
| primary/non-primary labels were model judgments | compiled `primaryBranchMap`; validator derives and enforces `primaryStatus` |
| root-ID citations were ignored | Arabic-root and `root_NNNNNN` citations now compile through the same motif map |
| occurrence matching overstated exactness | renamed to `resolved`, `ambiguous-root`, and `unmatched` |
| validators did not mirror required/forbidden fields | dependency-free shape checks now reject missing and additional properties |
| overlay provenance was path-only | integration and every base prose file are SHA-256 bound |
| authored preview could drift from JSON | preview removed from model outputs and rendered deterministically after validation |
| non-Turkish runs could silently use Turkish contracts | instantiator accepts only `tr` |
| reviewed sources could disappear silently | `sourceCoverage` accounts for every source as integrated or apparatus-only |
| overlay could omit unchanged ayahs | overlay validator requires the complete non-zero ayah sequence |

## Verified

- 11 unit and integration tests pass.
- S1, S87, S100, and S103 bundles build and validate.
- S87 prompt contains no review-state, review-decision, reviewer, rejection-list,
  or `.reviewed.json` contract.
- S87 prompt size is 265,723 bytes; its inlined sources total 256,998 bytes.
- Repository-level `_channel/` files were not touched after the workspace move.

## Residual Work

- Run a real S87 Layer-3 authoring pass.
- Validate its integration and overlay JSON.
- Render and read the S87 preview to judge whether `emerging` hints clarify or
  clutter the existing local surprise prose.
- S1 and S100 have partial primary-branch coverage; uncovered member labels must
  remain `unknown`. S87 and S103 coverage is complete.
