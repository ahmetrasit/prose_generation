# Combined Layer 3 + Layer 2.5 - Implemented Plan

Status: implemented, 2026-07-28.

This lane consumes reviewed network channels and cold Layer-2 prose in one
hermetic pass. It writes the whole-surah argument, surprising completed channel
reading, reviewed structured channel plan, and story-building ayah overlays.

## 1. Input Boundary

`bundles/s{NNN}/{N}.channel.json` contains:

| field | purpose |
| --- | --- |
| `reviewedChannels` | reviewed parent/subchannel meaning, active motifs, synthesis, and ayah refs |
| `text` | Arabic reading order |
| `anchorInventory` | exact QAC morpheme/root identities |
| `motifAnchorMap` | deterministic root -> branch -> motif -> anchor join |
| `primaryFloor` | canonical Layer-1 translation when complete |
| `coverage` | compact source and identity audit |

The bundle excludes per-ayah coverage duplication, pericopes, raw network
outputs, `butuncul_okuma`, and Layer-2 artifacts.

`scripts/instantiate_channel.py` adds only the canonical Layer-2 prose files.
Evidence and findings indexes are not repeated because exact channel identity is
already carried by the bundle and reader grounding is judged against the prose
that will receive the additions.

## 2. Reviewed Channel Handling

The upstream review is not re-adjudicated. Its synthesis is preserved. The
builder removes only redundant `scene_or_process` and prose-form
`ayah_anchors`, because synthesis, structured `ayah_refs`, and the typed anchor
map already carry those functions.

Standalone reviewed channels are retained rather than becoming empty parents.

Every `root:branch/motif` citation is compiled into `motifAnchorMap`. Downstream
members use `qacMorphemeRef + rootId + branchId`; ambiguous and unmatched
mappings remain visible but cannot become exact members.

## 3. One Authored Pass

The combined writer:

1. derives the primary-grounded surah argument;
2. integrates reviewed subchannels into the smallest coherent reader-facing
   channel systems;
3. writes the completed surprising channel reading;
4. derives maturity from exact members in reading order;
5. places Layer-2.5 additions into the unchanged ayah prose;
6. emits both structured plans and a merged preview.

This removes the redundant channel-draft and independent-adjudication passes.
Maturity and placement are designed together, so the completed channel prose
and its gradual disclosure cannot drift into different readings.

## 4. Outputs

- `{N}.surah.prose.md`
- `{N}.surah.thesis.md`
- `{N}.surah.channels.reviewed.json`
- `{N}.ayah-channel-overlays.json`
- `{N}.ayah-channel-overlays.preview.md`
- `{N}.surah.exclusions.md`
- `{N}.surah.evidence.md`
- `{N}.channel.friction.md`

The cold Layer-2 prose remains canonical. Overlay JSON is the authored Layer-2.5
handoff; preview markdown is the human review surface.

## 5. Commands

```sh
python3 scripts/build_channel_bundle.py --surah 87
python3 scripts/check_channel_bundle.py bundles/s087/87.channel.json --surah 87
python3 scripts/instantiate_channel.py --surah 87 \
  --layer2-label default.v2.5.6-sol-high --date 2026-07-28
```

After the authored pass:

```sh
python3 scripts/check_channel_plan.py \
  _commentary/outputs/s087-default/87.surah.channels.reviewed.json \
  --state reviewed --bundle bundles/s087/87.channel.json
python3 scripts/check_channel_overlays.py \
  _commentary/outputs/s087-default/87.ayah-channel-overlays.json \
  --plan _commentary/outputs/s087-default/87.surah.channels.reviewed.json
```

## 6. Acceptance

- Bundle builds and prompt instantiation are deterministic.
- Every reviewed citation resolves through the motif map or stays explicitly
  unmatched.
- No ambiguous anchor becomes a plan member.
- Combined plans are reviewed, carry reviewed maturity, and validate.
- Overlay insertions agree with plan maturity and exact base prose placement.
- Layer-2 prose, including local surprise readings, is never rewritten.
