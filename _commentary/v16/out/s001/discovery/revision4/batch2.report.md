# S1 revision4 batch 2

| Image | Model | Initial | Proposals | New | Repeats | Final | Check |
|---|---|---:|---:|---:|---:|---:|---|
| 7 | terra | 88 | 17 | 17 | 0 | 105 | findings |
| 8 | luna | 69 | 19 | 19 | 0 | 88 | findings |
| 8 | terra | 95 | 31 | 31 | 0 | 126 | findings |
| 9 | luna | 77 | 25 | 25 | 0 | 102 | findings |
| 9 | terra | 117 | 13 | 13 | 0 | 130 | findings |
| 10 | luna | 74 | 28 | 28 | 0 | 102 | findings |
| 10 | terra | 157 | 21 | 21 | 0 | 178 | findings |

Image 7 terra: 21 Arabic review flags; see sec7/terra/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].

Image 8 luna: 19 Arabic review flags; see sec8/luna/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].

Image 8 terra: 1 Arabic review flags; see sec8/terra/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].

Image 9 luna: 16 Arabic review flags; see sec9/luna/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].
Recovered diagnostic: duplicate reference: 7:58

Image 9 terra: 3 Arabic review flags; see sec9/terra/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].

Image 10 luna: 8 Arabic review flags; see sec10/luna/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].
Recovered diagnostic: Script failed
Recovered diagnostic: Script error:
Recovered diagnostic: apply_patch verification failed: Failed to find expected lines in /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision4/sec10/luna/list.tsv:
Recovered diagnostic: Script failed
Recovered diagnostic: Script error:
Recovered diagnostic: apply_patch verification failed: Failed to find expected lines in /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision4/sec10/luna/list.tsv:

Image 10 terra: 0 Arabic review flags; see sec10/terra/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].
Recovered diagnostic: duplicate ayah reference: 40:80 at line 85
Recovered diagnostic: duplicate ayah reference: 11:65 at line 125
Recovered diagnostic: duplicate ayah reference: 14:50 at line 128
Recovered diagnostic: duplicate ayah reference: 43:64 at line 146

Image 7: 201 unique candidates; 85 named by both models. 38 separate context neighbours. Dry Opus estimate $3.22; no call.

Image 8: 144 unique candidates; 70 named by both models. 14 separate context neighbours. Dry Opus estimate $2.28; no call.

Image 9: 145 unique candidates; 87 named by both models. 33 separate context neighbours. Dry Opus estimate $2.51; no call.

Image 10: 197 unique candidates; 83 named by both models. 13 separate context neighbours. Dry Opus estimate $2.82; no call.

Both turns completed for every job in this batch. Input hashes, model/effort, unchanged initial rows, schema, unique final references and follow-up delivery are checked in native logs. Tool calls were reviewed before finishing.

All raw proposals remain intact. Repeated references do not change original grades. Arabic flags are review aids, not error counts. See validation_review.json where present; English meaning and relevance are not exhaustively verified.

Recorded incremental discovery estimate/charge: $0 on the Codex subscription. Token usage and all recovered diagnostics are in the JSON and native logs.
