# v14 input audit — before and after the Sol trial

Judgment: the funnel does not need a broad rewrite for this trial. The writer handover needed an outcome-based
revision. The inherited upstream has specific gaps to fix and test separately before production.

| Stage/input | Useful job | Audit finding and disposition |
|---|---|---|
| Discovery window scan | Every attested branch can supply a rare activation | Keep the search space; no evidence-based reason yet to prune it. Focus branches overlap the focus dictionary but the dictionary adds definitions/quotable phrases. |
| Discovery channel review | Existing surah images, mechanisms and interactions | Keep. It is not identical to HFT; no automatic deduplication by vocabulary. |
| Discovery HFT | Prior mechanisms and trace steps | Material overlap with channel reviews is possible; first-run discovery succeeded with both. Test removal separately. Labels must never become pruning rules. |
| Pairs | Candidate navigation through the scan | Compact references, not duplicate definitions; first safe ablation candidate, not a justified removal yet. |
| Focus word notes | Morphology and prior local readings | Small, but legacy topics can select/narrow a reading. Keep in frozen experiment; interpret as proposals. |
| Concordance | Counts and Quran-loaded patterns | Writer never received it in v13 despite being told to use it. Included explicitly in v14. Root threshold >60 still hides clauses for a rare focus lemma inside a frequent root; future builder should separate root and lemma coverage. |
| Network | Cross-ayah coalition and disclosure | Relevant image entries remain. Synthesis projects touch/meet to local members; assemble/develop retain wider membership. Meetings are represented once as their own connected evidence. Full network stays archived. |
| QeQ legacy digest | Variant readings and related-passage leads | Inherited QeQ prompt does not name these jobs. Its usage counts also conflict with the newer concordance (1:6 h-d-y 308/316; q-w-m 643/660). Do not merge totals. Future QeQ should receive the variant/leads sections and an explicit count authority. Frozen QeQ output is unchanged in this trial. |
| Writer act/QeQ/network | Findings and their relationships | Replaced by one synthesis index, preserving F, E_F, Q, A, image and meeting records. No separate mustland list. All tags on one ref are preserved. No same-word exclusion. |
| Writer dictionary/branches | Concepts, Turkish losses and exact source text | Retained. The 1:6 packet has 35 focus entries and 65 other-root entries, with no duplicated branch IDs between these two files. Analysis records reuse their evidence for proposed connections; that is functional overlap, not a demonstrated reason to drop source definitions. Branch existence is not enough to validate a semantic inference. Only first classical phrases are supplied, so some usable quotations remain unavailable. Full source expansion should be selective, not blanket bulk. |
| Writer Quran window | Immediate narrative/argument and word partners | Missing from v13 writer; now supplied (613 bytes for 1:6). |
| QeQ passage text | Exact quotation and enough context to assess the proposed connection | Most QeQ entries give references and English descriptions, not retrieved Arabic. For example, 28:22 has no Arabic quotation in this frozen packet; 17:35 has only the balance phrase in an activation. The concordance supplies clauses for the road root but not the frequent guidance/standing roots. Verification after generation catches citation failures but cannot supply missing context before interpretation. Retrieve the passages actually being developed in a future arm; do not pad the packet with every parallel citation. |
| Writer variants | Consequential alternative readings | Added only the variant section (355 bytes for 1:6), with instructions to use only meaningful differences. |
| Writer preceding prose | What was actually explained, and how to continue it | One immediate predecessor, not every previous essay. It is 49,245 bytes for 1:6. Its benefit remains unproved until comparison. |
| Reciprocal list | Final missing-passage check | File exists but no consuming stage exists. It is not sent or billed in this trial. Preserve for a late check; do not put canonically dismissive labels into discovery. |
| Surah commentary | Full image assembly, interactions and deferred material | Not implemented in v13 or this focused v14 change. Handforward is preserved and visible, but not yet consumed by a surah writer. |

Measured writer input: 201,665 bytes, versus v13's recorded 151,835 (+32.8%). The input is not advertised as cheaper.
Most growth buys actual preceding prose. `input_audit.py` produces exact per-file sizes and later citation diagnostics.
A missing citation is not proof an input was unused; internal model use cannot be measured by a script. Discovery
necessarily explores material that will not reach the final prose. The economic target is avoidable duplication and
unrequested repeated synthesis, not forcing all supplied evidence into the result.

After a candidate, inspect whether earlier prose avoided repetition, whether the recovered inputs changed an
explanation, and whether unsupported or unused source material accumulated. Do not credit input inclusion as a
quality gain. The selected Sol trial changes writer model too, so it cannot establish an Opus cost/quality improvement.

## Observed after the single Sol trial

The candidate uses correct scoped concordance counts and builds on the supplied 1:5 traveller. Phonetic variants
are explicitly left out because they do not change an interpretation. This shows plausible utility, not causal
proof that each entire input was necessary. Four flagged Quranic spellings were copied from the concordance's
forms: future retrieval and the verifier need one exact-text convention. Many QeQ references still lack retrieved
passage context, and uncommon meanings may require more than the first classical phrase.

The most concrete avoidable cost is now output: 44,781 of 87,110 response bytes (51.4%) are accounting JSON, often
repeating entire paragraphs. Use smaller sufficient evidence anchors and narrower claims in a future arm. The
account's 180 “connected” items are self-assessments, not independent proof. Full preceding prose adds 49.2 KB of
input and should be tested against a compact, verified record of what the reader has already been told.

The complete comparison and acceptance limits are in [COMPARISON.md](COMPARISON.md). The raw response and frozen
input have not been edited, and there has been no second generation or repair call.
