# Available inputs

Inventory date: 2026-09-27.

This document describes the data and saved artifacts present in this checkout, together with locally present source datasets in sibling repositories referenced by its code or source documentation. Entries identify material, location, and contents. They are grouped by file family rather than by individual file. Generated analyses, assembled packets, prose, and experimental variants are included as distinct artifact families.

Paths are relative to this repository's root. A path beginning with `../` is outside this repository, in a sibling checkout. `S` and `A` denote surah and ayah numbers; `sNNN` denotes a three-digit surah directory; `*` denotes a variable filename component. Some upstream run directories have unpadded names such as `s1`. Counts describe the local files on the inventory date. Coverage differs between families and between saved runs; a filename pattern does not imply that every ayah has a corresponding file.

## Quran text and word-level records

| Material | Location | Contents |
| --- | --- | --- |
| Uthmani Quran text | `../quran-data/data/text/quran-uthmani.tsv` | Arabic ayah text, in pipe-delimited `S:A` and text records, including prefatory `S:0` basmalah records. |
| Indexed Quran text and ayah counts | `../quran-slm/resources/source/quran_ayah_text_ar.tsv`; `quran_ayah_counts.tsv` in the same directory | Ayah text with global index, node ID, surah, ayah, and reference; a separate surah/ayah-count table. Corresponding manifest JSON files contain dataset metadata. |
| QAC morphology | `../quran-data/data/morphology/qac.sqlite.gz` | Compressed SQLite database. Word and morpheme records include references, word/morpheme indices, Arabic and Buckwalter surfaces and lemmas, stems, roots, part of speech, morphological features, measure, mood, aspect, voice, and source metadata. Tables include `qac_words` and `qac_morphemes`. |
| Word analyses, packaged by surah | `../quran-data/data/analysis/word-analysis/sNNN.jsonl.zst` | 114 compressed JSONL files. Ayah records contain `schema_version`, `prompt_version`, `ref`, `bundle_id`, and `words`. Word records include QAC alignment, displayed surface/root, gloss ranges, explanatory prose, topics, supporting anchors, and review/coverage fields. |
| Word analyses, individual ayah files | `../word_analysis/outputs/production/S-A.json` | Individual JSON records in the word-analysis family, including word explanations, topics, root/gloss information, QAC references, and review notes. |
| Variant readings | `../study/_project_corpus/qiraat.tsv` | 3,812 records with word reference, variant order, Arabic reading, transliteration, reader set, variant type, transmission type, explanatory note, and source. The word reference field is `tsv_word_ref`. |
| Root occurrence table | `../quran-slm/resources/source/qac_root_ayah.tsv` | Root/ayah records with occurrence counts, QAC references, word indices, surfaces, lemmas, parts of speech, measures, full ayah text, normalized text, and root sequence. |

## Dictionaries, lexical branches, and glosses

| Material | Location | Contents |
| --- | --- | --- |
| Furuq lexicon database | `../quran-data/data/lexicon/furuq.sqlite.zst` | Compressed SQLite lexicon containing roots, branch images, dictionary entries, lexical units and senses, Arabic source phrases, source references, and status/provenance fields. Tables include `roots`, `branch_images`, `dictionary_entries`, and `lexical_unit_senses`. |
| V4 lexicon database | `../quran-data/data/lexicon/v4.sqlite.gz` | A separately stored lexicon snapshot with the same principal table families: roots, branches, dictionary entries, and lexical senses. |
| Lexical handle registry | `../quran-data/data/lexicon/positive-handles.sqlite.gz` | Handles for roots, branches, lexical units, and forms; aliases; validation links; conflict records; build metadata. Records include source table/key, expression, morphological form, status, and checksum. |
| Turkish dictionary entries | `../quran-data/data/dictionary/tr/*_entry.json` | Root profiles and branch records containing Arabic branch images, definitions and source quotations; Turkish concept maps and glosses; contextual and lexical glosses; identity judgments; lexicalization scope; source synthesis; excluded glosses; neighboring distinctions; and occurrence evidence. Some filenames contain multiple root IDs separated by `--`. |
| Headword entries | `../quran-data/data/dictionary/tr/headwords/` | Dictionary records organized by headword, alongside the root-organized entry collection. |
| Supplemental dictionary entries | `../quran-data/data/dictionary/supplemental/entries/`; `registry.v1.json`; `source-names.v1.json` in the parent directory | Supplemental entries with Arabic headword/root, binding, source snapshot, sources, analyses, and senses; an entry registry; and named source records. |
| Dictionary manifests and Arabic-evidence records | `../quran-data/data/dictionary/tr/MANIFEST.json`; `ARABIC-EVIDENCE-UPDATES.json`; `SOURCE.md` in the same directory | Entry inventory and provenance; recorded Arabic branch/source-text updates with released and dictionary versions. |
| Root packets with source passages | `../dictionary/data/output/root_packets/` | JSON and Markdown root packets. JSON records include root identities, branches, dictionary sources and their `entry_text_clean`, lexical senses, branch/lexical links, QAC occurrences and ayah contexts, grammatical attachments, and Qnet records. There are 1,679 JSON packets in this directory. |
| Furuq root packets | `../dictionary/data/output/furuq/root_packets/` | A separate collection of root packets, including root IDs and Arabic root names, branch definitions, lexical senses, and dictionary-source material. |
| Dictionary entry creation artifacts | `../dictionary/v2/work/entry_creation/` | Root, Furuq, and headword subdirectories containing source/input material, entry fragments, output entries, and associated generation/review artifacts. Entry paths include `*/tr/output/*_entry.json` and `*/tr/fragments/*_entry.json`. |
| Gloss records in the data checkout | `../quran-data/data/translation/glosses/locales/tr/*.json` | Turkish branch-concept, contextual, and lexical glosses, with source-entry references, generation metadata, review references, and gloss evidence/error fields. |
| Gloss-generation records | `../dictionary/v2/gloss_generation/results/en/`; `../dictionary/v2/gloss_generation/results/tr/` | English and Turkish gloss records containing branch concepts, contextual and lexical glosses, facet coverage, semantic fit/error descriptions, losses, additions, collisions, and review provenance. |
| Reader dictionary catalogues | `../quran-apps/apps/tafsir-web/public/evidence/dictionary/tr.root-dictionary.*.json`; `shards/` in the same directory | Hashed dictionary catalogue snapshots and entry shards. Catalogue records include `entriesByRootId` and Arabic root names. |

## Identity mappings and alignment records

| Material | Location | Contents |
| --- | --- | --- |
| QAC/Furuq root mappings | `../quran-data/data/bridges/qac-furuq-v4-root-map.sqlite.gz`; `qac-furuq-v4-root-map.tsv` in the same directory | QAC roots and corresponding dictionary root IDs, including split mappings, occurrence counts, and dominant-target fields. SQLite objects include `qac_furuq_targets` and `qac_to_furuq`. |
| Dictionary root resolutions and aliases | `../quran-data/data/bridges/qac-dictionary-root-resolutions.json`; `qac-dictionary-reviewed-aliases.json` in the same directory | QAC root keys, dictionary root IDs, resolution records, aliases, and associated review metadata. |
| Word-specific root analyses | `../quran-data/data/bridges/qac-dictionary-word-root-analyses.json` | Alternative root analyses keyed by QAC root, lemma, or occurrence reference. Analyses include dictionary root ID, Arabic root, standing, and attribution text. |
| QAC/V4 form mappings | `../quran-data/data/bridges/qac-v4.sqlite.gz` | Morpheme-to-lexical-form mappings, including form handles, match status, confidence, and the stored `downstream_usable` field. |
| QAC/Masaq bridge and source units | `../quran-data/data/bridges/qac-masaq.sqlite.gz`; `../quran-data/data/bridges/qac-masaq/` | Bridge database; compressed source-unit TSV; attachment, trace, and QAC/Masaq decision tables; source metadata. `../quran-data/data/bridges/qac-masaq-audit.json` contains audit records. |
| Repository QAC/analysis crosswalks | `qac-masaq-mapping/output_all/` | `sNNN-qac-to-analysis.json`, `sNNN.qac-masaq-report.json`, and `manifest.json`. Crosswalks contain surah/release identity, word and morpheme counts, analysis-token counts, and QAC-word-to-analysis mappings. |
| Reader crosswalk snapshots | `../quran-apps/packages/content-compiler/crosswalks/` | Stored QAC/analysis, grammar/analysis, and QAC-root/Furuq crosswalk files, including `s001-qac-to-analysis.json`, plus a `qac-analysis-crosswalk-v3/` collection. |
| Frozen occurrence/root audit | `../latent_activation/_status/v12_cross_run/audits/frozen-qac-root-bridge-occurrences.tsv` | Word references; QAC and Masaq references; surfaces; frozen and corrected root values; alignment groups; root-correction status/rule; Furuq resolution fields. |
| Branch/root alignment and activation tables | `../quran-slm/resources/source/qac_branch_root_alignments.tsv`; `qac_additive_branch_root_activations.tsv`; `qac_attested_branch_roots.tsv`; `qac_no_branch_cards.tsv`; `qac_rootless_token_activations.tsv` in the same directory | Root/lemma-to-branch-root mappings, additive mappings, root membership, unresolved/no-card records, and token-level records for rootless tokens. Fields include references, branch-root keys, reason codes, and evidence branch IDs. |

## Grammar records

All paths in this table are outside the repository, under `../quran-data/data/grammar/`.

| Material | Location | Contents |
| --- | --- | --- |
| Syntactic attachments | `attachments/attachments.tsv` | Ayah-keyed dependency records with dependent/head word and unit IDs, relation, surface/root/form information, clause references, status, confidence, evidence, and reason. |
| Clause boundaries | `attachments/clauses.tsv` | Clause spans, types, parent/linked clauses, quotation boundaries, and status/evidence fields. |
| Referents and implicit material | `attachments/cross_references.tsv`; `ellipsis.tsv`; `implicit_arguments.tsv` in the same directory | Candidate/resolved antecedents, referenced words and clauses, ellipsis records, implicit subjects/agents/arguments, agreement, and accompanying explanations. |
| Verb and noun instances | `attachments/verb_instances.tsv`; `attachments/noun_instances.tsv` | Occurrence-level grammar, root and form, subjects/objects, prepositions, attachment IDs, noun modifiers, and clause/frame information. |
| Verb and noun pattern summaries | `attachments/verb_valency_frames.tsv`; `attachments/noun_governing_patterns.tsv` | Root/form-level counts and profiles of objects, prepositions, complements, construct relationships, adjectives, and sample references. |
| Translation-support and issue records | `attachments/translation_support.tsv`; `attachments/review_issues.tsv`; `attachments/merge_stats.json` | Recorded readings, scope, force, construction, linked grammar units, translation-instruction text, evidence/status fields, review issues, and merge statistics. |
| Contextual profiles | `contextual/*_v2.tsv` | Root/form-keyed profiles for roles, valency, referents, discourse, polarity, collocations, argument supplements, and referent supplements; contextual and collocation summaries. Fields include counts, distributions, ratios, sample references, source/batch metadata, and low-occurrence markers. |
| Contextual extraction metadata | `contextual/extraction_manifest.json` | Source and extraction metadata for the contextual-profile collection. |

## Branch networks, channels, and inter-ayah relations

| Material | Location | Contents |
| --- | --- | --- |
| Arabic branch-card tables | `../quran-slm/resources/source/corpus_branches_ar.tsv`; `quranic_branches_ar.tsv`; `furuq_full_branches_ar.tsv` in the same directory | Node/root/branch identifiers, Arabic branch image, Arabic definition, source phrase and references, corpus origin, and status fields. The full Furuq table also records QAC attestation, subset class, and dictionary-source families. Manifest JSON files accompany the collections. |
| Branch catalogue | `../quran-slm/artifacts/corpus_network/catalog.json` | 10,932 indexed branch cards with node IDs, root/branch IDs, Arabic roots, source rows, corpus/subset metadata, and catalogue/snapshot hashes. |
| Character and E5 representations | `../quran-slm/artifacts/corpus_network/` | `character_directional_rank.u16le`, `e5_directional_rank.u16le`, `character_tfidf.npz`, `e5_embeddings.npy`, metadata JSON, manifests, build report, and `surah_resources/`. Rank files contain unsigned 16-bit directional rank matrices; NPZ/NPY files contain stored numerical representations. |
| NeoAraBERT representations | `../quran-slm/artifacts/corpus_ensemble/` | `neoarabert_directional_rank.u16le`, `neoarabert_embeddings.npy`, associated metadata, manifest, and build report. |
| Branch keywords | `../quran-roots/_corpus/activation/Qnet/v2/network/incidence_full/branch_keywords.tsv` | Root ID, branch ID, keyword type, keyword, and replicate vote count. |
| Network candidate and path records | `../latent_activation/network/v3/experiments/corpus_neo_adaptive/sNNN/` | Channel candidates in JSONL/TSV, review bundles, candidate graphs, family memberships, similarity edges, sparse paths, path families, branch inventories, and summary records. Related candidate snapshots also exist under `../latent_activation/network/v3/output/`. |
| Network review texts | `../latent_activation/network/v3/reviews/sNNN/reader_a_pilot.md` | Generated parent-channel and subchannel descriptions, semantic invariants, surface relations, surprising-reach descriptions, reading types, scenes/processes, motifs, ayah anchors, and synthesis text. |
| Network copies in the data checkout | `../quran-data/data/analysis/channels/network-v3/sNNN/` | Candidate/family/path artifacts and `review/reader_a_pilot.md` copies. There are 110 review Markdown files in this collection. |
| Passage boundaries | `../quran-data/data/analysis/channels/network-v3/pericopes/surah_pericopes.jsonl`; `../latent_activation/network/v3/pericopes/` | Passage/pericope records with surah, ayah start/end, labels, and associated metadata. |
| Inter-ayah relation records | `../quran-data/data/analysis/inter-ayah/focus_S_A_cutoff_100.tsv`; `../quran-slm/inter-ayah/outputs/focus_S_A_cutoff_100.tsv` | Headerless TSV records with relation label, related ayah reference, and explanatory note. The data-checkout collection contains 6,236 focus files. |
| Reciprocal relation records | `../quran-data/data/analysis/inter-ayah/reciprocal/` | Inter-ayah records with forward/reverse relation information and source/provenance fields. |

## Saved activation analyses and root dossiers

| Material | Location | Contents |
| --- | --- | --- |
| V12 full-surah packets | `../quran-data/data/analysis/ayah-activation/v12-tr/sNNN/full_context_packet.json` | 114 JSON packets containing surah context, root/branch inventories, and missing-inventory records. |
| V12 ayah walks | `../quran-data/data/analysis/ayah-activation/v12-tr/sNNN/full_context_control/*ayah_walk.md` | 118 Markdown files containing ayah-indexed activated readings, lexical evidence, reading changes, retrospective surprises, and, in some files, Turkish prose synthesis. |
| V12 wider-context ayah walks | `../quran-data/data/analysis/ayah-activation/v12-tr-11ayah/sNNN/full_context_control/*ayah_walk.md` | 114 Markdown files in the ayah-walk family, with the wider-context run's readings and explanations. |
| Whole-surah Turkish readings | `../quran-data/data/analysis/ayah-activation/v12-tr/sNNN/full_context_control/*butuncul-okuma.md` | Turkish ayah readings and context expansions with branch references. Filenames include both padded and unpadded surah numbers. |
| Staged focus packets and responses | `../quran-data/data/analysis/ayah-activation/v12-tr/sNNN/focus_S_A/` | A limited set of staged packets and `responses/reader_*/stage_NN.json` outputs, including some `left_first/` and `right_first/` variants. Response fields include models, status/confidence, mechanisms, activation traces, structural cues, abductive moves, before/after readings, minimal triggers, and ablations. |
| Cross-run publication records | `../quran-data/data/analysis/ayah-activation/v12-cross-run/tr/S_ayah_findings_publication.json` | 114 surah JSON files with ayah references, Turkish baselines, findings, language/protocol fields, and source references. |
| Cross-run working records | `../latent_activation/_status/v12_cross_run/sNNN/` | Ayah rosters, anchor maps, anchor occurrences, branch evidence, claims, claim sources, source findings, coverage tables, decisions, publication variants, manifests, and self-audits. |
| Hermetic Focus Trace packets and responses | `../latent_activation/focus_trace/runs/sNNN/packets/S_A.packet.json`; `readers/reader_*/S_A*.focus_trace.json` under the same run directory | Focus/context packets and generated baseline models, context deltas, surprising-valid-outlier records, reading changes, mechanisms, and activation steps. Steps include source references, word indices, mapped root/branch IDs, phrases, and roles. Both padded and unpadded surah directory names occur. |
| Copied Focus Trace artifacts | `../quran-data/data/analysis/commentary-inputs/focus-trace-hermetic/tr/runs/` | A separately stored collection of Focus Trace packets, reader JSON, and selected run metadata, with padded surah directory names. |
| V11 surah activation artifacts | `../latent_activation/v11/run/`; `../quran-data/data/analysis/commentary-inputs/v11-surah-activation/run/` | Surah text/passage packets, candidate bridges, activation packets, mechanism notes, secondary expansions, discovery rankings, final reports, and whole-surah reading texts. |
| Root dossier packets | `../root-dossier/packets/`; `../root-dossier/index.tsv` | Root directories containing occurrence/source material in `A.md`, word-analysis variants in `A_wa.md`, metadata JSON, and a root index. |
| Root dossier results | `../root-dossier/out/final/*.json` | 123 saved root JSON records. Fields include root identity, word count, stage, groups of occurrence IDs with labels and branches, exceptions, activation assignments, and completion status. |
| Root occurrence/branch assignments | `../root-dossier/out/activation_map.tsv` | QAC word and ayah references, surface, lemma, morphology, root, role, branch, alternative/variant fields, note, group, basis, and stage. |

## Assembled bundles in this repository

| Material | Location | Contents |
| --- | --- | --- |
| Ayah bundles | `bundles/sNNN/S_A.ayah.json` | 2,578 saved JSON bundles across 113 surah directories. Bundles contain ayah text, morphology, word analysis, word/morpheme alignment, root lexicon, branch inventories, activation records, inter-ayah rows, channel material, passage metadata, and source coverage. Some records represent prefatory basmalahs. |
| Passage-scoped ayah bundles | `bundles/sNNN-pericopes/p*/S_A.ayah.json` | 778 saved ayah bundles in eight surah passage collections, with passage-scoped context and related metadata. |
| Surah bundles | `bundles/sNNN/S.surah.json` | 70 saved surah JSON files containing ayah references and bundle-file lists, whole-surah text/context, channel review, passage boundaries, generated channel outputs, and coverage. |
| Layer-2 bundle projections | `bundles-layer2/sNNN/S_A.ayah.json` | 637 saved bundles across 32 surah directories. These contain the ayah-bundle fields with differentiated branch payloads and recorded branch-policy metadata. |
| Nontier bundle collection | `bundles-nontier/s018/S_A.ayah.json` | 110 S18 ayah bundles with the nontier branch payload. |
| Bundle aliases and experimental copies | `_commentary/work/s*-nontier-bundles/`; `_commentary/work/hft-*/` | Per-ayah symbolic links to passage bundles, plus saved S100 bundles with different Focus Trace response variants. |

The ayah-bundle field families present in the repository include:

| Field family | Contents |
| --- | --- |
| `text`, `surah`, `ayah`, `ayahRef`, `unit_kind`, `surface_ref`, `linguistic_source_ref` | Arabic text, unit identity, and, where present, separate surface and linguistic-source references. |
| `qac_morphemes`, `word_morpheme_spans`, `word_analysis` | Morphological records, alignment spans, and explanatory word analyses. |
| `root_lexicon`, `branch_inventories` | Dictionary/gloss records and root/branch inventories. |
| `v12_reader_responses`, `v12_reader_walks`, `v12_reader_walks_wide` | Staged and ayah-walk activation records. |
| `v12_focus_trace_hermetic`, `v12_cross_run_publication`, `butuncul_okuma_line` | Focus Trace records, cross-run findings, and whole-surah-reading extracts. |
| `inter_ayah_rows`, `pericope`, `channel_subchannels_anchored_here`, `channel_generated_outputs` | Related-ayah records, passage membership, anchored channel descriptions, and saved channel-output references/content. |
| `coverage`, `schema_version`, `generated_at` | Source-presence and mapping records, schema identity, and generation metadata. |

## Prepared commentary packets and saved analyses

The paths below are inside this repository. Version and experiment directories contain different subsets of the listed file families.

| Material | Location | Contents |
| --- | --- | --- |
| Instantiated commentary inputs | `_commentary/inputs/`; `_commentary/inputs-nontier/` | Ayah prompt Markdown containing assembled source material, with JSON manifests and saved experimental variants. |
| V3 prepared inputs and analyses | `_commentary/v3/inputs/`; `_commentary/v3/outputs/` | Bundle snapshots, dockets, prepared data, reader maps/views, adjudication records, synthesis packets, generated responses, and associated prompts/manifests. |
| V4 prepared inputs and analyses | `_commentary/v4/input/`; `raw/`, `editorial/`, `legacy/`, `stale/`, and `failed-artifacts/` under `_commentary/v4/` | Source and prefatory-basmalah bundle snapshots; docket and manifest JSON; micro/macro/global packets and prompts; generated analysis, composition, editorial, and recorded failed/stale variants. |
| V5 prompt inputs | `_commentary/v5/input/` | Saved discovery, composition, synthesis, canonical, editorial, and other prompt files, including embedded source/packet material and run-specific variants. |
| V5 generated analyses and prose | `_commentary/v5/raw/`; `middle/`; `editorial/`; `concise/`; `output/` under `_commentary/v5/` | Discovery JSON, scope ledgers and readings, synthesis/claim records, detailed prose, middle-length prose and claims, editorial prose, invitations, and concise variants. |
| V6 and V7 prepared experiments | `_commentary/v6/input/`; `_commentary/v7/input/`; `_commentary/v6/reviews/` | Saved packets, reading records, instantiated prompts, and reviews for selected experiments. |
| V9 source sections | `_commentary/v9/input/` | Numbered Markdown sections for ayah/word data, dictionary branches, Focus Trace, branch pairs, bridges, occurrence lists, concepts, Fatiha, surah context, inter-ayah relations, and other saved findings. |
| V9 line packets and records | `_commentary/v9/lines/work/S_A/` | `context.md`, local/usage/surah/related packets, `package.md`, `items.tsv`, JSONL records, `digest.md`, `digest_v2.md`, synthesis outputs, and run logs. Digests include variant readings, root occurrences, and related passages with recorded relation notes. |
| V9 Luna worklists and results | `_commentary/v9/luna/` | Worklists for dictionary, branch, Focus Trace, and global material; generated findings, merged records, readings, and run metadata. |
| V9 network experiments | `_commentary/v9/network/out/`; `_commentary/v9/pilot/` | Network JSON, worklists, maps, harvested findings, automatic-harvest variants, prose, and experiment records. |
| V10 evidence and map experiments | `_commentary/v10/work/`; `_commentary/v10/experiments/` | Evidence/packet JSON, maps and map checks, writer packets, reading briefs, previews, prompts, response schemas, responses, size/statistics records, and provider logs. |
| V11 ayah results and seed records | `_commentary/v11/out/` | Ayah findings, ledgers, Turkish readings, checks, run logs; a saved `arms/S/s001/seeds/all/` collection contains ayah text, seed inputs, generated seeds, and associated records. |
| V12 prepared inputs | `_commentary/v12/work/sNNN/S_A/` | Dictionary sections, Focus Trace records, channel descriptions, neighboring branch tables, root-usage dossiers, input-size tables, and window/context material where present. |
| V12 generated findings and prose | `_commentary/v12/out/` | Findings Markdown, ledgers, Turkish readings, checks, status JSON, and model/run logs. |
| V13/V14 ayah packets | `_commentary/v13/work/sNNN/S_A/`; `_commentary/v14/work/sNNN/S_A/` | `ayah.md`, `dictionary.md`, `pairs.md`, `concordance.md`, `hft.md`, `reciprocal.md`, and a `window` path record. Contents include focal text and word notes, lexical branches/source quotations, branch relationships, root counts and occurrence clauses, saved trace hypotheses, and reciprocal ayah records. |
| V13/V14 shared window packets | `_commentary/v13/work/sNNN/window_*/`; `_commentary/v14/work/sNNN/window_*/` | `window_text.md` contains Arabic passage text; `window.md` contains window text, branch listings, and channel-review material. |
| V13/V14 saved stage results | `_commentary/v13/out*/`; `_commentary/v14/out*/` | Activation and Quran-relation findings (`act.md`, `qeq.md`), network/synthesis records, findings inventories, selected assemblies, coverage records, continuation notes (`handforward.md`), Turkish readings, raw responses, checks, and status/provenance records. |
| V14 comparison snapshots | `_commentary/v14/out-sol-max/`; `out-sol-stable/`; `out-sol-argument/`; `out-astra-argument/` under `_commentary/v14/` | Saved model-comparison runs with frozen prompt/input copies, prior-ayah context, generated prose, structured synthesis accounts, source checks, reviews, metrics, source-lookup records, and experiment metadata. |
| V14 source extracts and text snapshots | `inputs/` directories inside `_commentary/v14/out*/`, including per-ayah `inputs/` | Depending on the run: `ayah.md`, `dictionary.md`, `branches.md`, `concordance.md`, `variants.md`, `window_text.md`, `passages.md`, `quran.tsv`, and `source_access.md`. These contain copied text/lexical extracts, variant-reading extracts, exact passage collections, a full text snapshot, or a description of the saved source interface. |

## Translation, ayah prose, and surah prose

| Material | Location | Contents |
| --- | --- | --- |
| Translation anchor inputs | `_translation/v1/anchors/input/*.anchor-input.json` | Root and branch records, rooted stems, ayah text, root-resolution metadata, word-analysis fields, and coverage. Saved scopes include S1, S87, S100, S100:1–5, S103, and S112. |
| Primary-anchor records | `_translation/v1/source/*.primary-anchors.json` | Surah identity and anchors associating QAC morpheme references with branch IDs and lexical-unit IDs. Saved scopes include S1, S87, S100:1–5, and S103. |
| Translation input bundles | `_translation/v1/input/en/`; `_translation/v1/input/tr/` | Ayah text, stored primary readings, grammar support, lexical cards, language-policy records, and source-release identity. |
| Authored translation records | `_translation/v1/authored/tr/s087.authored.json` | Authored glosses and ayah translations, language/surah identity, and missing-gloss records. |
| Assembled translations | `_translation/v1/output/en/`; `_translation/v1/output/tr/` | English and Turkish ayah translations and lexical cards, with cold-test and gloss-test variants where saved. |
| Ayah commentary | `_commentary/outputs/`; `_ayah_commentary/outputs/` | Turkish ayah prose, summaries, editorial variants, evidence files, indices, findings, friction notes, ledgers, and model/experiment variants. Exact companion files differ by ayah and run. |
| Channel drafts | `_channel/s001.draft.prose.md`; `_channel/s087.draft.prose.md` | Saved surah channel prose drafts. |
| Compiled channel material | `_commentary/work/layer_3_channel_commentary/` | Source/workspace records and generated channel bundles, including surah channel plans, channel evidence, and associated prose/review artifacts. |
| Surah source packets | `_surah_commentary/v2/packets/sNNN/S.source-packet*.json` | Source registry, ayah text/material, local boundaries, reviewed-channel records, secondary material, coverage, and warnings. There are 58 saved packet files. |
| Surah prompt snapshots | `_surah_commentary/v2/inputs/` | Saved discovery, composition, and review prompts with their embedded material. |
| Surah analyses and readings | `_surah_commentary/v2/outputs/`; `_surah_commentary/v2/runs/` | Channel briefs, discovery hypotheses, composition/evidence JSON, surah readings, editorial outlines/drafts/prose, prelude/postlude variants, friction records, prompts, and run metadata. `_channel/layer3` is a symbolic link to `_surah_commentary/v2`. |
| Copied commentary in the data checkout | `../quran-data/data/commentary/ayah/detailed/tr/`; `ayah/summary/tr/`; `surah/detailed/tr/` under `../quran-data/data/commentary/` | Separately stored ayah commentary and summaries, evidence/index/friction/findings files, surah readings, channel briefs, discovery hypotheses, channel JSON, and channel review/prose records. |
| Empirical-resonance outputs | `_commentary/empirical_resonance/outputs/s096/` | Two saved 96:15–16 Markdown responses, with empirical commentary, findings, source-gap discussion, and references. The accompanying schema document describes fields for ayat, word anchors, candidate topics, research sources, claims, and exclusions. |

## Other stored source material

| Material | Location | Contents |
| --- | --- | --- |
| Hebrew Bible text and variants | `../quran-slm/resources/source/hebrew_bible_wlc_verses.tsv`; `hebrew_bible_wlc_variants.tsv`; `hebrew_bible_wlc_verse_map.tsv`; `hebrew_bible_wlc_manifest.json` in the same directory | Additional files in the referenced source-data directory: Hebrew verse text in pointed, unpointed, and consonantal forms; written/read variants; token and word IDs; versification mappings; paragraph/special-letter metadata; and source provenance. |
| Archived commentary experiments | `archive/`; `_commentary/outputs/archive/`; `_commentary/experiments/` | Earlier prompt/input snapshots, generated discovery and synthesis records, prose, evidence, editorial variants, manifests, and experiment reports. `archive/_commentary/v2/` includes V2 example and generated artifacts. |

## Schemas, prompts, reference cases, and provenance

These are stored specification, evaluation, and record artifacts. The descriptions below identify their contents without adopting their instructions or judgments.

| Material | Location | Contents |
| --- | --- | --- |
| Bundle and channel schemas | `bundles/schema.json`; `schemas/` | Ayah/surah bundle definitions; channel bundle, ayah-channel overlay, and surah-channel-plan definitions. |
| Versioned schemas | `_commentary/v3/schemas/`; `_surah_commentary/v2/schemas/`; `_translation/v1/schema/` | Definitions for prepared data, dockets, reader maps/views, adjudications, synthesis, source packets, channel briefs, discovery hypotheses, compositions, editorial outlines, translation anchors, authored translations, and translation layers. Additional response schemas are stored with individual run artifacts. |
| Commentary prompt collections | `_commentary/` and its version directories, particularly `prompts/` subdirectories; `_ayah_commentary/v2/` | Saved instructions and output contracts for discovery, source reading, composition, synthesis, review, editorial work, and other recorded stages. |
| Surah/channel/translation prompts | `_surah_commentary/PROMPT.md`; `_surah_commentary/v2/prompts/`; `_channel/PROMPT.md`; `_channel_review/PROMPT.md`; `_channel_integration/PROMPT.md`; `_surah_final/PROMPT.md`; `_translation/v1/prompts/` and its root prompt files | Prompt text and output-shape specifications for the corresponding artifact families. |
| Empirical-resonance specifications | `_commentary/empirical_resonance/SCHEMA.md`; `PROMPT.md`; `SOURCE_DISCOVERY_PROMPT.md`; `ORCHESTRATION.md` in the same directory | Packet/output fields, prompt text, source-record format, and orchestration specifications. |
| Evaluation reference cases | `_commentary/v5/benchmark/`; `_commentary/v8_batch/benchmark/`; `_commentary/v11/eval/`; `_commentary/v12/eval/`; `_commentary/v13/EVAL_ANCHORS.md`; `_commentary/v14/eval/` | Benchmark catalogues, anchor sheets, known-answer/dossier records, and regression inventories. V14 includes `regressions.json` and `regressions-v3.json`. |
| Version baseline manifest | `_commentary/v14/baseline.manifest.json` | Recorded baseline file paths, checksums, and snapshot metadata. |
| Reviews, comparisons, and operational records | Version-root review/comparison Markdown; `_commentary/v*/operations/`; per-run `*.check.json`, `*.status.json`, `*.manifest.json`, `*.log.jsonl`, and review/metrics files | Recorded assessments, validation results, model/effort settings, source paths and hashes, response metadata, timings/token data where recorded, run status, and provenance. |
| Project and source documentation | `README.md`, `NORTH_STAR.md`, `PRINCIPLES.md`, `COMMENTARY_SPEC.md`, `PROSE_EDITORIAL_GUIDE.md`, `PLAN.md`, `STATUS.md`, `ultimate goal.txt`, `docs/`, root audit/handoff documents, and version-level README/HANDOFF/design documents | Existing goals, editorial specifications, source descriptions, availability notes, implementation records, audits, and historical decisions. |
| Audio specifications | `_audio/tts-generation-spec.md`; `_audio/audio/ayah-recitation/README.md` | Text-to-speech and recitation-file specifications. No audio media files are present in `_audio/` in this snapshot. |

The directories `_words/`, `_curriculum/`, and `_ayah_surah_commentary/` contain no files in this snapshot. The root `test.output` entry is a broken symbolic link to an external agent log. Repository internals, dependency/runtime caches, credentials, and executable implementation files are outside this data-and-artifact inventory.
