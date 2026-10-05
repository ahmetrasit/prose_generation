# S1 session-only Sol max augmentation

Completed all 14 image sections with native gpt-6-sol agents at max effort. The parent spawned every agent directly and sent the corrections in the same sessions. Opus remains the default; the runbook and workflow code were not changed. Token accounting was omitted at the user’s request.

The merged [images.md](images.md) contains **258 prose additions** and **73 paragraph reference lines**. The additions use 1947 distinct ayat, of which 1792 were not cited anywhere in the original source. There are 4471 image–ayah verdict records; the same ayah may be judged in several images. These are linguistic judgments, not a precision estimate.

| Image | Paragraphs | Discovery candidates | Context | Judgments incl. own | Prose | Ref lines | Ayat in additions |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | 1–8 | 170 | 46 | 294 | 17 | 8 | 215 |
| 2 | 9–14 | 242 | 25 | 312 | 18 | 6 | 253 |
| 3 | 15–22 | 293 | 35 | 361 | 17 | 8 | 294 |
| 4 | 23–27 | 193 | 25 | 288 | 24 | 5 | 209 |
| 5 | 28–31 | 291 | 31 | 388 | 9 | 4 | 314 |
| 6 | 32–36 | 270 | 29 | 325 | 25 | 5 | 202 |
| 7 | 37–41 | 201 | 38 | 362 | 19 | 5 | 225 |
| 8 | 42–44 | 144 | 14 | 223 | 16 | 3 | 142 |
| 9 | 45–50 | 145 | 33 | 260 | 17 | 6 | 148 |
| 10 | 51–54 | 197 | 13 | 235 | 15 | 4 | 164 |
| 11 | 55–58 | 233 | 36 | 321 | 10 | 4 | 172 |
| 12 | 59–61 | 273 | 21 | 361 | 17 | 3 | 195 |
| 13 | 62–65 | 232 | 17 | 323 | 21 | 4 | 207 |
| 14 | 66–73 | 315 | 25 | 418 | 33 | 8 | 355 |

## Review and remaining editorial questions

The parent read prose and reference drafts, checked selected Arabic ayat, and reviewed targeted corrections. Corrections addressed speakers and pronouns, simile framing, unsupported details, lexical claims, and missing paragraph references. This was not an independent ayah-by-ayah relevance audit.

All supplied ayat have verdicts, promised placements match applied additions, and stripping the marked additions recovers the original exactly. Existing report flags for nearby references were retained when they express different links. The remaining already-cited flags in sections 2 and 10 are explained in their run logs. The two mixed cited/ref/conflict decisions in section 3 are preserved explicitly because the existing helper only collects leading conflict statuses.

Four issues in the original prose remain for separate editorial treatment: see [source-review.md](source-review.md). The source was preserved. Read the detailed decisions in sec1/verdicts.md through sec14/verdicts.md; raw responses, snapshots, prompts and native-session records remain beside them.

Cross-image overlap is retained: these are independently augmented image sections, and a surah-level editorial pass may later compress repeated exposition. This session did not start the ayah-reading stage or change downstream defaults.

The original image-3 test remains separate; this is the fresh complete S1 run. All agent sessions remain available for follow-up.
