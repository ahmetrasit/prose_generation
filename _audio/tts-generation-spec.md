# TTS Generation Spec

This workflow prepares finalized Turkish commentary in `quran-data` for
paragraph-level Google Gemini TTS. Preparation is offline; only the separate
`synthesize_tts_chunks.py` command contacts Google.

## Source layout

The supported source trees are:

```text
../quran-data/data/commentary/surah/detailed/tr/sNNN/<surah>.surah-reading.tr.md
../quran-data/data/commentary/ayah/detailed/tr/sNNN/<surah>_<ayah>.prose.tr.md
```

Surah preparation accepts either one `*.surah-reading.tr.md` file or its
`sNNN` directory. Ayah preparation accepts one `*_*.prose.tr.md` file or an
`sNNN` directory. An Ayah directory is sorted numerically by surah and ayah.
Evidence, friction, index, summary, and other Markdown files are not included
in Ayah speech preparation.

For Ayah sources, the canonical Arabic text is read from
`data/text/quran-uthmani.tsv`, keyed by the source file's `surah:ayah`
reference. Commentary preparation keeps the prose natural and does not add a
synthetic ayah label. The separate `ayah-recitation` collection creates one
joined request per ayah in the form:

```text
<Turkish surah name> <ayah number>: <canonical Arabic ayah text>
```

The original quran-data files are never modified.

## Inline annotation conversion

Ayah prose contains inline annotations such as:

```text
{ar:ٱلْحَمْدُ, tr:el-hamdü, gloss:o belirli hamd}
```

Preparation sends this to the clean text as:

```text
ٱلْحَمْدُ (o belirli hamd)
```

The `tr` transliteration is discarded. Both `gloss:` and the earlier
`:gloss:` spelling are accepted. Malformed or partially parsed annotation
markers fail preparation instead of leaking into a request.

## Offline preparation

From this repository root:

```bash
python3 _audio/scripts/prepare_tts_chunks.py \
  ../quran-data/data/commentary/surah/detailed/tr/s001 \
  --out-root ../quran-data/_audio/audio \
  --dry-run
```

```bash
python3 _audio/scripts/prepare_tts_chunks.py \
  ../quran-data/data/commentary/ayah/detailed/tr/s001 \
  --out-root ../quran-data/_audio/audio \
  --dry-run
```

Remove `--dry-run` when request files should be materialized. The default
artifact root is the local `./_audio/audio`; use the explicit quran-data
`--out-root` shown above when the prepared artifacts are approved for that
repository. Separate collections are used:

```text
../quran-data/_audio/audio/surah/S001/
../quran-data/_audio/audio/ayah/S001/
../quran-data/_audio/audio/ayah-recitation/S001/
```

For Surah sources, the first audio request begins with the visible title,
followed by the first prose paragraph. The `ayah` collection contains only
the converted analysis prose. The `ayah-recitation` collection contains one
joined audio request per ayah, for example:

```text
Fatiha 5: إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
```

Preparation reports cleaned spoken-character counts, an estimated input-token
cost, and a conservative maximum cost based on the provider's input/output
token limits for every prepared request. Gemini TTS pricing is token-based,
not character-based: `$1` per million input text tokens and `$20` per million
output audio tokens (25 audio tokens per second).

Replacing an existing collection is opt-in with both
`--replace-existing --prune`. Preparation refuses to overwrite any existing
collection by default, including when a single Ayah file would otherwise
replace a broader `ayah/SNNN` collection. The replacement flags remove stale
requests and audio derivatives before the new request set is used.

Each prepared collection contains:

```text
S001.md             # clean derived Markdown
chunks.jsonl        # paragraph metadata and hashes
manifest.json       # app/audit metadata
requests/           # one Google request JSON per audio unit
responses/          # reserved for service responses
originals/wav/      # reserved for returned WAV files
originals/mp3/      # reserved for MP3 derivatives
sections/wav/       # reserved for joined section WAV files
sections/mp3/       # reserved for joined section MP3 files
```

The preparation script does not obtain credentials, make network requests, or
create audio. Preparation and synthesis share a per-collection lock, so a
collection cannot be rewritten while its request set is being synthesized.
Section titles receive a final period only when used in `ttsText`; visible
titles remain unchanged. Changing Ayah reference construction changes the
prepared request set, so an existing collection must be prepared again before
any future TTS run; preparation never sends that new set automatically.

## TTS request configuration

The generated request shape is:

```json
{
  "audioConfig": {
    "audioEncoding": "LINEAR16",
    "pitch": 0,
    "speakingRate": 1
  },
  "input": {
    "prompt": "<commentary or strict recitation prompt>",
    "text": "<cleaned paragraph text>"
  },
  "voice": {
    "languageCode": "tr-TR",
    "modelName": "gemini-3.1-flash-tts-preview",
    "name": "Rasalgethi"
  }
}
```

The service endpoint is:

```text
https://texttospeech.googleapis.com/v1beta1/text:synthesize
```

The synthesis script validates every request, path, manifest entry, voice, and
audio configuration before obtaining credentials. It freezes the validated
request bodies, and computes a request-set SHA-256 digest over the billing
project plus the exact ordered, length-delimited POST bytes remaining after
cache inspection. Its confirmation cost is a strict upper bound: the number
of pending requests multiplied by the provider's maximum input and output
tokens, priced at the fixed token rates above. Actual ledger output cost is
derived from measured WAV duration; input usage remains explicitly estimated
because the REST response does not return it. Duplicate JSON keys are rejected.
It obtains `gcloud auth print-access-token` only after the exact digest,
maximum cost, and spending ceiling are confirmed. Preparation and synthesis
take the same per-collection OS lock, while distinct folders remain parallel.

Before any future remote run, validate the prepared request set locally. For
recitation, use the separate collection path:

```bash
python3 _audio/scripts/synthesize_tts_chunks.py \
  ../quran-data/_audio/audio/ayah-recitation/S001 \
  --dry-run
```

Use the `requestSetSha256`, `maximumCostUsd`, project, and counts printed by that
preflight. After reviewing them, send the batch with exact confirmations:

For a non-contiguous subset, use repeated exact chunk IDs rather than
`--limit`. For example, the seven joined recitation chunks of S1 are selected
with:

```bash
python3 _audio/scripts/synthesize_tts_chunks.py \
  ../quran-data/_audio/audio/ayah-recitation/S001 \
  --chunk-id sec-001-p-001 \
  --chunk-id sec-002-p-001 \
  --chunk-id sec-003-p-001 \
  --chunk-id sec-004-p-001 \
  --chunk-id sec-005-p-001 \
  --chunk-id sec-006-p-001 \
  --chunk-id sec-007-p-001 \
  --dry-run
```

`--chunk-id` selections are ordered canonically by `chunks.jsonl`, are mutually
exclusive with `--limit`, and produce a partial generation state until the
remaining chunks are synthesized.

```bash
python3 _audio/scripts/synthesize_tts_chunks.py \
  ../quran-data/_audio/audio/ayah-recitation/S001 \
  --chunk-id sec-001-p-001 \
  --chunk-id sec-002-p-001 \
  --chunk-id sec-003-p-001 \
  --chunk-id sec-004-p-001 \
  --chunk-id sec-005-p-001 \
  --chunk-id sec-006-p-001 \
  --chunk-id sec-007-p-001 \
  --confirm-remote <requestSetSha256> \
  --confirm-cost-usd <maximumCostUsd> \
  --max-cost-usd <approved-ceiling>
```

For a first paid canary, run preflight with `--limit 1` and use that preflight's
digest and cost; a later full-batch run must be preflighted and confirmed
again. `--force` additionally requires `--confirm-force` because it can resend
already-paid requests. A timeout or interrupted transport is recorded as an
unknown outcome; resending it requires the separate `--reconcile-unknown`
acknowledgement and a new exact preflight confirmation. Failures are recorded
and are not automatically retried. Preparation refuses to overwrite a
collection containing an unresolved outcome.
Preflight and preparation never start TTS generation.
