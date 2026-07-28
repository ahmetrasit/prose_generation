# Scripts

- `build_channel_bundle.py` — compile reviewed channel sources, occurrence joins,
  primary floor, and primary-branch map into `generated/bundles/`.
- `check_channel_bundle.py` — dependency-free compact-bundle validation.
- `instantiate_channel.py` — create the Layer 3 + 2.5 prompt using Layer-2 prose
  only; Turkish is the currently supported target language.
- `check_channel_integration.py` — validate composition, source coverage,
  identities, primary status, and derived maturity. It performs no channel
  review.
- `check_channel_overlays.py` — validate integration/base file hashes,
  insertion identity, maturity agreement, and placement.
- `render_channel_preview.py` — deterministically merge validated additions into
  a human-review preview without changing base prose.
