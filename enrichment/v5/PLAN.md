# Enrichment v5: packet → extract → write

Status 2026-10-06: built and dry-run on real data; **pilot prepared, nothing spawned**. Every spawn needs the user's go.

## Why v5

Checked on 1:6, 87:6 and 100:1 against `corpus.sqlite`:

- **Corpus retrieval is checkable; memory is not.** All corpus anchors exist. About 75–80% of the memory attributions sampled were correct. The misses were exactly the details that matter: who said which technical point, and exact translator wording.
- **Agentic search wastes most of its input.** Both 1:6 corpus runs together cited about 565k tokens of source text, but the agents accumulated 64–104M input tokens. On 100:1, each Sol agent accumulated 2.3–7.3M tokens and cited 10–30k.
- **A script finds the same material for indexed families.** Segments indexed to the page's cited verses hold 90–100% of everything the agents cited for ten families on 1:6, and 100% (rivayet) and 98% (meal) on 100:1.
- **Discovery is luck-dependent where the index is weak.** Hadith, poetry, rhetoric, wujuh, academic and modern coherence are not verse-indexed. Bayani, qiraat and historical are only partly indexed.
  - Corpus agents missed corpus-held items: Thawbān at IBNMAJAH:277, an Imruʾ al-Qays witness, Wāḥidī on 2:190–194.
  - Memory agents missed others the corpus agents found: *kenūd* (al-Muthaqqib, Mufaḍḍaliyyāt), ḍ-b-ḥ witnesses.
- **High vs max is mostly run variance.** The two efforts share few cited segments (meal 1:6: 11 of about 110).
- **A rule flaw excluded Islāḥī.** v4 dropped his *Tadabbur* because the held text is an English translation, and that cost the actual 87:7 reading. v5 allows labelled translations (`common.TRANSLATION_OK`).

## Design

| Route | Families | Steps |
|---|---|---|
| `extract` | indexed families with packet > 60k tokens | packet (script) → Luna extractors, one fresh context per ≤120k-token chunk → Sol writer reads the extracts |
| `direct` | indexed, packet ≤ 60k | packet → Sol writer reads the whole packet |
| `+search` | bayani, qiraat, historical | the writer may also keyword-search the roster |
| `search` | hadith, poetry, rhetoric, wujuh, academic, modern-coherence | Astra memory **leads** (search terms only, never published) → `leads.py` searches the roster by script → Sol writer reads the candidates, searches further, writes |

Rules carried over from v4: corpus-only attribution, exact locators and anchors, 1 ledger row per paragraph, frozen bytes preserved. New:

- **Extractor coverage:** every packet segment gets a coverage row (`extracted` / `not_relevant` / `unreadable`).
- **Extractor quotes:** every extract is a verbatim quote, checked by script. Quotes, not summaries, so the extractor doesn't silently paraphrase away disagreements, preferences or gradings.
- **Packet scope:** writers may `get` any packet segment for context or anchors.

## Files

| File | Role |
|---|---|
| `common.py` | paths, routes, rates, verse extraction, translation rule, verbatim check |
| `ranges.py` | overlay for segments whose text runs past their indexed ayah (`index/range_overlay.jsonl`; corpus untouched). Narrow rule: «…} {N}». Today: 81 WAHIDI-ASBAB segments (e.g. v1p55#2 now spans 2:190–195). Ibn Kathīr's parenthesised numbers are footnotes, not verse markers. |
| `packet.py` | `plan --unit U` shows routes/sizes for all families; `build` writes `segments.jsonl`, `chunk-NN.txt`, `manifest.json`. Whole segments; a per-ayah slice is skipped where the FULL copy covers that verse. |
| `read.py` | the agents' only access: `input`, `chunk`, `extracts`, `get`, `search` (search routes only), `candidates` |
| `leads.py` | memory leads → roster FTS candidates (`leads/candidates.txt`); leads without hits stay listed |
| `prepare.py` | run directories, inputs (byte-identical to v4), packets, one spawn text per agent, `work/<run>.json` with stages |
| `check.py` | `extract DIR`, `write DIR LANE`, `assemble RUN --lane L`; never edits agent files |
| `account.py` | native Codex usage → per-request cost at each model's rate (reproduces the saved 100:1 costs to the cent) |
| `evaluate.py` | `reference` (from v4 runs + hand-checked extras; agents never see `eval/`) and `score RUN`: packet / extracted / cited recall, new segments, costs; `REVIEW-*.md` puts reference and v5 blocks side by side per paragraph for finding-level judgement |
| `briefs/` | extract, write, leads, search |

## Pilot (`work/pilot-20261007.json`, 14 agents)

| Unit / family | Why | Agents |
|---|---|---|
| 100:1 rivayet (436 segments, ~168k tokens, 2 chunks) | same packet written two ways: from extracts and directly. Measures what the extractor loses, and what each costs | 2 Luna, 2 Sol |
| 100:1 meal (2,553 segments, ~205k, 2 chunks) | translator wording through an extractor | 2 Luna, 1 Sol |
| 1:6 grammar (1,057 segments, ~361k, 4 chunks) | heavy page, forced extraction | 4 Luna, 1 Sol |
| 100:1 poetry (search) | non-indexed: memory leads plus search; known answers are *kenūd*, ḍ-b-ḥ, Imruʾ al-Qays v1p71#2 | 1 Astra (leads), 1 Sol |

Order:

1. **Stage 1:** spawn the extractors and the leads agent, each with its spawn file's exact text.
2. For each finished packet family: `check.py extract DIR`. For poetry: `leads.py DIR`.
3. **Stage 2:** spawn the writers.
4. `check.py write DIR LANE`.
5. `account.py pilot-20261007`, then `evaluate.py score pilot-20261007`.
6. Read the REVIEW files.

Estimated agent cost: **about $3–5** (8 Luna chunks about $0.05 each, 4 extract-lane writers about $0.3–0.5 each, rivayet direct about $1, poetry about $1.2). Parent excluded.

What the pilot decides:

- **Extractor recall.** Reference segments quoted, measured against the reference segments in the packet, plus findings lost when the rivayet extract lane is compared with the rivayet direct lane. Below about 90% at the finding level means the extractor is the gatekeeper risk; next try Sol at low effort as the extractor.
- **Writer cost per family**, by route, against v4 Sol high on the same family:

  | Family | v4 Sol high |
  |---|---|
  | 100:1 rivayet | $0.98 |
  | 100:1 meal | $1.82 |
  | 1:6 grammar | $0.82 |
  | 100:1 poetry | $0.77 |

- **Search route:** whether memory leads plus search recover the known poetry witnesses, and whether it is any cheaper.

## Per-ayah projection (19 families, 1:6-sized page; to be replaced by measurements)

| Scenario | Estimate |
|---|---|
| Today: corpus Sol high / Astra mix / corpus Sol max | $19.8 / $26.6 / $32.0 |
| Sol reads packets directly | no saving on heavy pages (about $13 of packet reading on 1:6) |
| Luna extracts, Sol writes; search families as in v4 | about $12–14 |
| plus cheaper search families | about $7–9 |
| plus 6–8 grouped writers instead of 19 | about $4–5 |

## Known limits and next steps

- **Luna's context window is unknown.** A chunk ends near 155k tokens of context. If an extractor fails on length, lower `CHUNK_TOKENS` in `common.py`; packets rebuild without any model.
- **Meal packets are mostly near-duplicate renderings** (1:6: 13.8k segments, about 1.2M tokens). Collapsing identical renderings per verse is the next large saving.
- **The reference set is not a gold standard.** It is what two v4 agents happened to cite. New v5 material is judged, not counted as error.
- **The range overlay covers only one pattern;** other editions' range errors are unknown.
- **Memory leads remain unverified** until a writer reads the passage. Leads are never published.
- **Untracked (`.gitignore`):** packets' `chunk-*.txt` and `segments.jsonl` are reproducible with `packet.py`; so is `eval/reference.json`, with `evaluate.py reference`.
