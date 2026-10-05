# S1 revision4 batch 3

| Image | Model | Initial | Proposals | New | Repeats | Final | Check |
|---|---|---:|---:|---:|---:|---:|---|
| 11 | luna | 97 | 39 | 39 | 0 | 136 | findings |
| 11 | terra | 122 | 47 | 47 | 0 | 169 | findings |
| 12 | luna | 90 | 48 | 48 | 0 | 138 | findings |
| 12 | terra | 162 | 50 | 50 | 0 | 212 | findings |
| 13 | luna | 97 | 32 | 32 | 0 | 129 | findings |
| 13 | terra | 169 | 28 | 28 | 0 | 197 | findings |
| 14 | luna | 187 | 13 | 13 | 0 | 200 | findings |

Image 11 luna: 51 Arabic review flags; see sec11/luna/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: ['18:65'].
Recovered diagnostic: Script failed
Recovered diagnostic: Script error:
Recovered diagnostic: apply_patch verification failed: Failed to find expected lines in /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision4/sec11/luna/list.tsv:
Recovered diagnostic: Script failed
Recovered diagnostic: Script error:
Recovered diagnostic: apply_patch verification failed: Failed to find expected lines in /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision4/sec11/luna/list.tsv:
Recovered diagnostic: duplicate ref 23:21
Recovered diagnostic: bad field count at 27 3
Recovered diagnostic: bad ref at 27
Recovered diagnostic: bad basis at 27
Recovered diagnostic: bad field count at 59 3
Recovered diagnostic: bad ref at 59
Recovered diagnostic: bad basis at 59

Image 11 terra: 2 Arabic review flags; see sec11/terra/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].

Image 12 luna: 22 Arabic review flags; see sec12/luna/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: ['20:51'].

Image 12 terra: 23 Arabic review flags; see sec12/terra/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: ['20:51'].

Image 13 luna: 47 Arabic review flags; see sec13/luna/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].

Image 13 terra: 7 Arabic review flags; see sec13/terra/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].
Recovered diagnostic: duplicate 2:150 x2

Image 14 luna: 14 Arabic review flags; see sec14/luna/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].
Recovered diagnostic: duplicate ref 27 26:18
Recovered diagnostic: duplicate ref 149 26:29
Recovered diagnostic: duplicate ref 164 45:14
Recovered diagnostic: duplicate ref 188 20:82
Recovered diagnostic: duplicate ref 192 81:4

Image 11: 233 unique candidates; 72 named by both models. 36 separate context neighbours. Dry Opus estimate $3.64; no call.

Image 12: 273 unique candidates; 77 named by both models. 21 separate context neighbours. Dry Opus estimate $3.71; no call.

Image 13: 232 unique candidates; 94 named by both models. 17 separate context neighbours. Dry Opus estimate $3.52; no call.

Image 14: 315 unique candidates; 109 named by both models. 25 separate context neighbours. Dry Opus estimate $4.19; no call.

Both turns completed for every job in this batch. Input hashes, model/effort, unchanged initial rows, schema, unique final references and follow-up delivery are checked in native logs. Tool calls were reviewed before finishing.

All raw proposals remain intact. Repeated references do not change original grades. Arabic flags are review aids, not error counts. See validation_review.json where present; English meaning and relevance are not exhaustively verified.

Recorded incremental discovery estimate/charge: $0 on the Codex subscription. Token usage and all recovered diagnostics are in the JSON and native logs.
