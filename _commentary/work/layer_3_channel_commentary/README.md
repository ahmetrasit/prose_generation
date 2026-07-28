# Layer 3 Channel Commentary Workspace

This workspace implements one combined authoring pass:

1. Layer 3 writes the primary-grounded surah argument and the surprising
   whole-surah reading produced by recurring secondary channels.
2. Layer 2.5 stages those channels through unchanged Layer-2 ayah prose.

The source channel files and branch identities are already reviewed. This
workflow does not review, admit, reject, rank, or score them again.

## Boundaries

Read-only project sources:

- `bundles/sNNN/*.json`
- `_translation/v1/`
- `_commentary/outputs/sNNN-default/*.prose.*.md`
- `_channel/` and upstream channel data

All new files are written beneath this workspace:

- `generated/bundles/`
- `generated/inputs/`
- future model outputs and rendered previews

## Architecture

`scripts/build_channel_bundle.py` compiles the already-reviewed channel report
into a compact bundle with Quran occurrence joins and a primary-branch map.

`scripts/instantiate_channel.py` adds only canonical Layer-2 prose. It does not
repeat Layer-2 evidence or findings indexes.

The model authors seven files, including
`{S}.surah.channels.integrated.json`. The integration record has no review
fields. `scripts/check_channel_integration.py` validates its identities,
coverage, and derived maturity.

`scripts/check_channel_overlays.py` hash-binds the integration and base prose.
`scripts/render_channel_preview.py` then produces the merged preview
deterministically.

## S87

```sh
python3 _commentary/work/layer_3_channel_commentary/scripts/build_channel_bundle.py \
  --surah 87

python3 _commentary/work/layer_3_channel_commentary/scripts/instantiate_channel.py \
  --surah 87 --layer2-label default.v2.5.6-sol-high --date 2026-07-28
```

Generated S87 prompt:

`generated/inputs/s087/87.channel.prompt.md`

## Tests

```sh
PYTHONPYCACHEPREFIX=/tmp/pycache python3 -m unittest discover \
  -s _commentary/work/layer_3_channel_commentary/tests -v
```
