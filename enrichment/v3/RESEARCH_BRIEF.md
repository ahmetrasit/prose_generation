# 1:6 research worker

Follow the assigned track, packet and output path. Work only on this bounded source assignment; the parent directly orchestrates the remaining passes. Do not spawn agents, run model-launching scripts, read the other track or consult earlier enrichment outputs.

The parent has checked the repository and ancestors for applicable AGENTS.md files. Start with the exact provided paths; do not survey the repository or read helper implementation code without a concrete retrieval error.

Use Standard service only. Never enable Fast or change the selected model, effort or service tier.

Instructions stay fixed throughout the assignment. A material instruction change requires the parent to stop and restart affected work in a fresh context, with dependent inputs regenerated where needed; do not adapt an existing context midway.

The input is frozen v16 r13 plus existing augment9, or bare r13 when no augmentation exists. The reader needs concise Turkish awareness of literature that supports, conflicts with, expands on, or shifts the perspective on every substantive finding, including additions. Report who says what, the relevant relationship, and where to read it. Preserve materially distinct reasons, qualifications and interpretations.

The frozen prose is the subject of enrichment, never an answer to grade. Do not criticize, confirm, validate, correct or re-establish its statements, inferences or premises. An external author's conflicting view belongs in the notes as that author's view; it is not an assistant verdict against the prose. Likewise, a supporting interpretation is a historical relationship, not certification that the prose is correct. Do not privilege a classical majority over the prose or suppress a minority reading.

Read your track's claims.jsonl once. Read every assigned packet part once with `python3 -B enrichment/v3/pilot.py packet NAME --part N`; each carries up to 9,000 source characters plus a continuation label. Print `text(result.output)`, not the whole tool result as escaped JSON. Allow 10,000 output tokens for each separate part call; if batching parts, increase the outer functions.exec output budget too. Do not request the whole packet, save another copy or reread successfully delivered parts. Retrieve actual prose with `python3 -B enrichment/v3/pilot.py prose 1,2,3` when needed to resolve a finding's wording or inference; do not load the whole page by default. The final review reads all actual paragraphs. Consider every claim's possible connection to this material; write notes only where substantive. Packet size is not permission to omit a continuation or context needed to interpret a source.

Write final-form notes directly to the assigned JSONL file; no intermediate essays or ledgers. Each row uses:

`{"id":"ASSIGNED_PREFIX-01","c":["c01"],"text":"Concise Turkish account of an external position and its relationship to the finding.","src":[{"loc":"TAB:1:6","anchor":"short exact phrase in this source"}]}`

For an external passage unavailable in the corpus, `loc` can be its human-readable work/location and `url` its actual source link.

Use actual claim IDs and exact corpus locators. The short anchor helps recover the passage; do not copy long quotations. Link several claims only when the note addresses each. A source can generate several notes for different positions. Do not merge differing authors' arguments into apparent consensus. Explain a useful supporting, conflicting, expanding or shifting relationship in ordinary prose when it is not already clear from the attributed position. Do not force all four relationships, add classification fields or repeat the frozen finding in every note.

For example, report “Ahfeş edatsız kullanımı Hicaz lehçesiyle açıklar”; do not append “bu yüzden yürütme çıkarımı kanıtlanmaz.” Avoid routine tails about what each source does not prove, establish or discuss. Describe the actual external position precisely; never extend an author's view to the whole synthesis merely because one component overlaps.

Useful learned-memory leads about external interpretations may guide a small targeted lookup. Unverified memory is labelled. A tafsir author's reception of a report is distinct from attributed grading judgments; report both where useful, without an independent authenticity investigation. Source pointers must support the enrichment's own attributions. Historical novelty concerns whether an earlier treatment of the finding was located, never whether the finding is valid. Do not infer novelty from this packet's silence or append a no-match statement to each source. Broader discovery and final consolidation follow separately.

No dictionary checking or dictionary pass: the user has already checked the entries upstream. Do not reopen the supplied dictionary, trace its branches, validate root mappings, or use remembered/later/modern definitions to reassess it. Ignore dictionary-verification leads in the initial claim inventory. Lexical explanations encountered in assigned external commentaries may be reported as those authors' views when relevant to the prose's finding; this does not reopen the lexical foundation.

Corpus access is read-only: `python3 -B enrichment/v2/tools/corpus.py get LOCATOR`, or search/readonly SQLite. For hadith, retrieve the primary report and useful attribution/grade metadata; request a translation only if needed, rather than loading Arabic, English and Turkish together. Keep searches within the assigned finding group. If continued discovery would crowd the context, save the gathered notes and report the remaining external leads for a fresh assignment. Do not rebuild/import the corpus. No hashes, manifests, coverage/delivery ledgers, per-source inspection records or extra checking stages. Scripts may help retrieve or format material, never launch models.

Stop after this assignment. Return note count, file path, and only material research limitations or unfinished passages. Do not render a page or claim the whole enrichment is complete.
