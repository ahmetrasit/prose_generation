# Measured 1:1 usage and stored sizes — 2026-10-07

An ayah-based page is not one micro-lesson. Here it is the complete 1:1 base commentary: 27 paragraphs, 57 cited/discussed ayat, and 31 branches across six root families. Sol Max assembled 70 micro-lessons. This unusually extensive evidence packet is one observed case, not a per-ayah average or an estimate for all Quran ayat.

## Recorded full-run tokens

| Run | Input, cumulative | Of which cached | Uncached input | Output excluding thinking | Thinking | Output including thinking |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| sol-high | 8,301,563 | 8,113,152 | 188,411 | 39,367 | 19,728 | 59,095 |
| sol-max | 8,758,078 | 8,536,832 | 221,246 | 52,986 | 22,003 | 74,989 |
| luna-max | 10,871,486 | 10,015,744 | 855,742 | 46,116 | 114,132 | 160,248 |

These are totals across the complete multi-call agent run: reading, three linguistic perspectives, assembly, tool-call text and artifact authoring. Cached input is already included in input; thinking is already included in total output. Do not add either subset again. Parent preparation, comparison and later editorial corrections are excluded. Luna includes its recorded interrupted/resumed work; unreported interrupted generation may be absent.

For the default Sol Max, the largest individual request had **210,946 input tokens**. Cumulative input is 8.758 million because the model processes context repeatedly across calls, mostly from cache. Neither 221,246 uncached tokens nor 210,946 peak request tokens is the token count of the source packet alone. The 52,986 non-thinking output tokens also include drafts, tool arguments and writing artifacts; they are not the size of the final lesson file. Thinking usage is recorded in run metadata, not stored inside the lesson file.

Sources: [Sol recorded usage](sol-costs.json), [Luna recorded usage](luna-costs.json). Their dollar estimates and service-tier limitations are preserved there; this document adds no billing assumptions.

## Stored files

Logical UTF-8 byte sizes (decimal KB = 1,000 bytes), measured locally:

| Output | Displayable lessons | Assembled JSON, bytes | Readable Markdown, bytes |
| --- | ---: | ---: | ---: |
| sol-high | 64 | 139,806 | 83,697 |
| sol-max | 70 | 128,752 | 64,838 |
| luna-max | 32 | 63,511 | 37,539 |
| sol-max-edited | 70 | 130,839 | 64,953 |

The shared `input/` directory totals **1,527,786 bytes** (about 1.53 MB), including repeated representations of commentary and dictionary evidence. It excludes workflow prompts and the ontology. The original commentary alone is **34,906 bytes**.

Original Sol Max teaching sentences alone, joined with newlines, occupy **16,750 bytes** (1,842 whitespace-delimited words); the rest of its 128,752-byte JSON supplies anchors, readings, evidence, ontology attachments and editorial/deferred material. The edited copy's teaching sentences occupy 17,018 bytes. Word counts are not token counts, especially for Turkish and Arabic. The pilot did not record exact model-token counts for individual stored files, so none are inferred from byte counts here.

## Keeping subsequent runs lean

Prepare the relevant semantic evidence once, and consult full sources when a specific question requires them. Avoid repeatedly reading entire output files or all projections of a dictionary branch when only one paragraph or claim is at issue. A readable rendering is a view of the assembled output, not another independent authoring pass. The runbook now makes the compact evidence selection explicit.

Observe usage alongside commentary length, relevant branches, cited ayat and final lessons on several varied passages before estimating production totals. Use usage metadata already provided by the execution environment; no separate tracking service, token gate, hashes or new reviewer stage is needed. Cost improvements from the revised instructions have not yet been measured.
