# S1 revision4 continued checks

All22 agents have completed their current turns; no workers remain active. Nine jobs completed both turns successfully, two failed structural validation, and eleven completed their initial turn and await the fixed follow-up. The two prepared repairs still await a user decision. No new follow-ups, repairs, merges or Opus calls were performed.

| Image | Model | Initial rows | Arabic flags | New structural failures |
|---|---|---:|---:|---:|
| 7 | terra | 88 | 21 | 0 |
| 8 | terra | 95 | 1 | 0 |
| 9 | terra | 117 | 3 | 0 |
| 10 | luna | 74 | 1 | 0 |
| 10 | terra | 157 | 0 | 0 |
| 11 | luna | 97 | 36 | 0 |
| 11 | terra | 122 | 2 | 0 |
| 12 | terra | 162 | 23 | 0 |
| 13 | luna | 97 | 40 | 0 |
| 13 | terra | 169 | 7 | 0 |
| 14 | terra | 144 | 4 | 0 |

All eleven initial lists pass schema, reference existence and duplicate checks. Model/effort, input hashes and unchanged snapshots were verified. Observed tool use stayed within own inputs and own output.

## Content findings

- Image11 Luna,18:94: Arabic paraphrase is presented as quotation; the verse says على أن تجعل, not فاجعل.
- Image13 Luna,5:95: an extra definite article in الهديا; canonical text has هديا.
- Image10 Terra,7:40: English wording reverses the conditional order of entry and the camel passing through the needle.
- Image9 Terra,7:57: rain-grown fruit is an analogy for resurrection; the note blurs that distinction.
- Image13 Terra,93:7: searching is an unmarked interpretive gloss.

These findings are in turn1.validation_review.json files beside the raw outputs. Flags are not error counts. Multiword Arabic excerpts and three deterministic sample rows per list were checked; meaning, relevance, grades and derivations are not exhaustively validated.

## Recovered first-turn diagnostics

- Image10 luna: Script failed
- Image10 luna: Script error:
- Image10 luna: apply_patch verification failed: Failed to find expected lines in /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision4/sec10/luna/list.tsv:
- Image10 luna: Script failed
- Image10 luna: Script error:
- Image10 luna: apply_patch verification failed: Failed to find expected lines in /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision4/sec10/luna/list.tsv:
- Image10 terra: duplicate ayah reference: 40:80 at line 85
- Image10 terra: duplicate ayah reference: 11:65 at line 125
- Image10 terra: duplicate ayah reference: 14:50 at line 128
- Image10 terra: duplicate ayah reference: 43:64 at line 146
- Image11 luna: Script failed
- Image11 luna: Script error:
- Image11 luna: apply_patch verification failed: Failed to find expected lines in /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision4/sec11/luna/list.tsv:
- Image11 luna: Script failed
- Image11 luna: Script error:
- Image11 luna: apply_patch verification failed: Failed to find expected lines in /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision4/sec11/luna/list.tsv:
- Image11 luna: duplicate ref 23:21
- Image11 luna: bad field count at 27 3
- Image11 luna: bad ref at 27
- Image11 luna: bad basis at 27
- Image11 luna: bad field count at 59 3
- Image11 luna: bad ref at 59
- Image11 luna: bad basis at 59
- Image13 terra: duplicate 2:150 x2

The image6 Terra and image7 Luna structural failures remain recorded as partial. Their exact repair proposals and raw outputs are preserved. No new model cost was incurred by these checks.
