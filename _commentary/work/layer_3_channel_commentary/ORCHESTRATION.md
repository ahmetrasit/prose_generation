# Layer 3 and Layer 2.5 Orchestration

## 1. Compile

Build the compact channel bundle inside the workspace:

```sh
python3 scripts/build_channel_bundle.py --surah S
python3 scripts/check_channel_bundle.py generated/bundles/sSSS/S.channel.json \
  --surah S
```

Compilation preserves reviewed source meaning and joins stable root/branch
citations to Quran occurrences. It does not review channel content.

## 2. Instantiate

```sh
python3 scripts/instantiate_channel.py --surah S \
  --layer2-label LABEL --date YYYY-MM-DD
```

The prompt receives:

- compact reviewed-channel bundle;
- Arabic text and canonical primary floor;
- primary-branch map;
- unchanged Layer-2 prose only.

Layer-2 evidence and findings indexes are deliberately not repeated.

## 3. Author

The combined pass writes seven artifacts:

- `{S}.surah.prose.md`
- `{S}.surah.thesis.md`
- `{S}.surah.channels.integrated.json`
- `{S}.ayah-channel-overlays.json`
- `{S}.surah.exclusions.md`
- `{S}.surah.evidence.md`
- `{S}.channel.friction.md`

The integration record composes already-reviewed sources and derives maturity.
It contains no review decision or reviewer state.

## 4. Validate

```sh
python3 scripts/check_channel_integration.py \
  OUTPUT/{S}.surah.channels.integrated.json \
  --bundle generated/bundles/sSSS/{S}.channel.json

python3 scripts/check_channel_overlays.py \
  OUTPUT/{S}.ayah-channel-overlays.json \
  --integration OUTPUT/{S}.surah.channels.integrated.json
```

Validation checks:

- compiled QAC/root/branch membership;
- primary/non-primary status;
- complete source coverage;
- ordered, non-regressing maturity;
- integration and base-prose hashes;
- paragraph and phrase placement anchors.

## 5. Render Preview

```sh
python3 scripts/render_channel_preview.py \
  OUTPUT/{S}.ayah-channel-overlays.json \
  --integration OUTPUT/{S}.surah.channels.integrated.json
```

The preview is generated, never authored. Layer-2 prose is reproduced unchanged;
Layer-2.5 additions are visibly delimited after their selected paragraphs.
