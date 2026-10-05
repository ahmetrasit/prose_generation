# Independent Astra review of S1 image discovery

Reviewed 2026-10-04/05, before the authorized revision3 run. Scope: the complete 14-section S1 `images.md`; RUNBOOK rules and Step 2b; current discovery brief, `discover.py`, `check_discovery.py`, and `augment_surah.py`; original and revision2 section-1 lists, comparison/report artifacts, and validation/protocol reviews. I read both complete revised lists and inspected original candidates and the saved purposive comparison sample. Substantive checks used local `missing.M.verses()` only. This is a review, not a complete semantic audit of all historical rows or a new discovery run. I launched no agents or model calls and changed no production files or historical outputs.

## Decision

Proceed with the already-authorized native Luna/Terra revision3 run after the small prompt and native-bookkeeping fixes below. Preserve two independent model sessions per section, maximum effort, exactly one memory-only append follow-up per same session, at most seven agents per batch, and fresh revision3 directories. No extra model review stage or Opus call is required or authorized.

The revised inclusion standard is substantially clearer than the original. Its success is not established by reducing the union from 745 to 176 candidates. It removes demonstrably invented links, but also loses direct, useful correspondences. The next version should preserve its requirement for an identifiable connection while explicitly sweeping subordinate details and repeated formulations. It should not impose a candidate quota or a desired reduction.

Three material issues precede a defensible full run: complete input packaging; durable native two-turn provenance; and an image-wide recall instruction that does not overfit the road test. The packaging defect was corrected by the orchestrator during this review and independently rechecked below. Before any later Opus handoff, also resolve merge eligibility, attempt selection, and how discovery rationales/accuracy findings are conveyed.

## Findings supported by the local text

### 1. Input packaging omitted the central mercy root — corrected during this review

The original `discover.sections()` regex required the source word to be a single token and captured only the first branch ID. Consequently section 4, “Rahim ve terbiye,” omitted the two `ٱلرَّحْمَٰنِ ٱلرَّحِيمِ` source items at 1:1 and 1:3, leaving **ر ح م absent from its roots metadata**. Section 5 had the same omission. Every item containing several B codes retained only the first; section 1's guidance member, for example, lost B002 and B003. The complete prose and whole surah still supplied these materials, but the package's advertised inventory was incomplete.

The orchestrator changed the parser to match the ayah, a potentially multiword phrase, the root letters, and the complete branch tail, and to reject malformed source items. My subsequent read-only check parsed all 14 sections, confirmed ر ح م and both mercy entries in sections 4 and 5, and confirmed `B001, B002, B003` for section 1's guidance entry. Rebuild only fresh revision3 packages from that corrected parser; retain historical packages unchanged. Buluşmalar remains the intentional source-line exception.

### 2. Precision improved in specific examples; direct recall still failed

The original Luna explanation for 103:1 invented “the repeated ground on which the path is walked”; the actual ayah is the oath by time. Its 99:7 explanation turned an atom's weight of good into “every small step,” which the cited wording does not supply. Revision2 properly drops these explanations. However, the original union also contains the following locally verified candidates that revision2 loses:

| Candidate | Canonical detail and specific section-1 connection |
|---|---|
| 38:22 | `وَٱهْدِنَآ إِلَىٰ سَوَآءِ ٱلصِّرَٰطِ`: the disputants ask David for guidance to the even way. This directly joins the section's request, guide, and middle-of-the-road details. |
| 37:118 | `وَهَدَيْنَٰهُمَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ`: Moses and Aaron are guided to the straight path, an explicit repeated formulation and named earlier guided people. |
| 36:66 | Sight is effaced and people race toward `ٱلصِّرَٰطَ` without seeing. A specific boundary on route-finding and visible landmarks. |
| 4:168–169 | Guidance to a way is denied **except** the way to Hell. The exception across the ayah boundary matters; it directly parallels section 1's contrary destination at 37:23. Keep separate TSV rows whose notes identify their dependency. |
| 25:34 | People are gathered on their faces toward Hell and described as further astray from the way; bodily direction and contrary destination meet. |
| 20:108 | People follow the caller with no deviation; an eschatological guide/follower scene and absence of crookedness. |
| 34:18–19 | Visible settlements, measured secure journeys, then a request to lengthen journeys and communal scattering. A concrete scene connecting landmarks, travel, and dispersal. |
| 18:2 | `قَيِّمًا` continues 18:1's absence of crookedness, supplying the actual uprightness term that revision2 wrongly attributes to 18:1. A specific textual parallel, even if graded below direct road scenes. |

The already-reported loss of 4:125 is also a defensible thematic omission: following Abraham's religion supplies an earlier exemplar and an enacted way. It is less direct than 38:22. These distinctions matter more than list size.

Do not insert this table into revision3 agents' prompts or append it to their outputs. That would turn review checks into supplied candidates and contaminate an independent rerun. Use it as an explicit, purposive post-run retention check; do not call it a measured recall rate. Existing commentary citations likewise measure input coverage, not independent retrieval. The prompt examples 2:108/103:1 are already exposed cases.

### 3. Correct references, quotations, and explanations are separate properties

I confirmed the historical report's substantive checks against local Arabic: 20:53 has paths but not the quoted `تهتدوا`; 4:118 has God cursing Satan, not Satan cursing himself; 26:63 describes striking and splitting the sea, while the dry-path wording is at 20:77; 79:19 contains the guidance invitation previously assigned to 79:18. Revision2's Terra 40:28 explanation transfers Pharaoh's fear from 40:26 to the believing man and changes its content. All of these can coexist with a valid ayah reference and a plausible candidate.

I also confirmed revision2's 42:15 conjunction mismatch, 19:43 case/form mismatch, 23:74 phrase reversal, 33:67 added `عن`, 4:51 unmarked skipped words, and 18:1/18:2 conflation. The original Terra 4:169 note also calls Hell the “withheld way”; the canonical exception says it is the only way retained, so this note needs logical correction before reuse even though the candidate is excellent.

Do not delete a useful candidate merely because its quotation or explanation is wrong. Preserve the model row, record the correction in an audit sidecar, and let canonical Arabic govern a later verdict. Conversely, passing the quotation checker does not validate speaker, causation, negation, or interpretive relevance. English-only mistakes such as 40:28 are invisible to it.

## Minimal prompt changes, with exact text

Keep the existing six discovery lenses, four-field TSV, no target length, image-defined scope, and requirement to explain a specific connection. The following short insertions/replacements are enough; a new schema or a third model turn is unnecessary.

**A. Insert after the six discovery lenses, before inclusion grading:**

> Before grading candidates, work through every distinct scene, object, action, relation, and secondary dictionary sense actually developed in the section. For each, recall direct formulations, repeated occurrences elsewhere, nonlexical parallels, and relevant reversals. Do not let the title, the first scene, or the ayat already quoted stand in for the whole section. The same ayah may qualify for more than one image, for different stated reasons. For a Buluşmalar section, also consider the particular meetings between images that its prose develops. Do this review internally; output only the TSV rows.

Reason: sections such as water, ownership, and the four destinations have several independent branches. “Every candidate meeting this standard” does not itself tell a model to inspect every branch before filtering. This clause strengthens recall without accepting root co-occurrence as evidence.

**B. Replace the strong/medium/weak definitions with:**

> - strong: a direct, specific correspondence to an identifiable feature of this image, including a secondary feature actually developed in the prose;
> - medium: a specific correspondence whose interpretive bridge you can state explicitly;
> - weak: a plausible, specific correspondence whose uncertainty you identify explicitly; uncertainty does not excuse a generic connection.

Reason: “central to the image” can disfavor a well-supported minor branch. Medium is the proper home for an articulated indirect link; the candidate need not alter the commentary or be its best example. Discovery gathers passages for judgment; it does not decide which deserve new prose.

**C. Add immediately after the contrast definition:**

> Contrast describes the kind of relationship, not a lower confidence level. Use it when the principal link is a reversal or boundary; explain any uncertainty in the note. Whenever an otherwise graded row also makes a contrast, include contrast among its bases. Neither model agreement nor a follow-up origin makes a candidate stronger.

Reason: 37:23 is strong for Luna and contrast for Terra; the merge takes strong. That is acceptable as a reported discovery label only if the reversal survives and nobody treats the fourth category as weak confidence. Retain both model labels. No need to migrate to a fifth TSV field now.

**D. Replace the current quotation instruction with:**

> Keep Arabic quotations short and quote only words you remember as belonging to the cited ayah. If exact wording is uncertain, explain the connection in English instead of reconstructing a quotation. Explicitly label a root, dictionary form, or wording from the source section as such. Never combine words from different ayat into one quotation; mark omitted words. Check the speaker, action, negation, and ayah boundary in your remembered context. If a neighbour is needed to complete the claim, name that ayah and describe the cited row's own contribution separately.

Reason: the task is memory-only discovery, so it should not encourage long quotations that cannot be checked within the model's permitted workflow. This is not a request to allow retrieval or to discard plausible candidates for lack of a full quote.

**E. Preserve the two-turn protocol; use this bounded follow-up text:**

> Review your remembered coverage for qualifying omissions under the same inclusion and grading rules, checking the section's distinct scenes and secondary details, repeated formulations, specific indirect parallels, reversals, and necessary passage continuations. Append only previously unlisted ayah references using the same TSV schema. Keep existing bytes unchanged. Zero additions is valid. Do not read any files, retrieve sources, or run scripts; a file-write tool or a literal append-only shell write solely to save the rows is permitted. Do not regrade, sort, or rewrite the existing list. Return only a brief completion notice.

Reason: the revision2 follow-up was already markedly better than the original unqualified “comprehensive & exhaustive” reminder. This is a coverage sweep, not pressure to add rows. The explicit file-write exception avoids treating an append heredoc as prohibited computation. Snapshot the first turn before sending it. Do not perform a third corrective model turn.

**F. State the tool boundary once in the native initial wrapper:**

> Work from memory after reading only this run's prompt.md and package.md. You may write list.tsv and, during this first turn only, inspect or format-check that same output. Do not read other runs, source datasets, repository instructions beyond what is already supplied, or external material, and do not spawn agents or call models. The follow-up will prohibit all file reads and permit only appending output. Do not read list.tsv before creating it.

This makes the revised first-turn policy explicit, prevents repeating the missing-file diagnostics, and distinguishes local formatting from semantic retrieval. If the actual native wrapper uses an even narrower allowed tool set, record that exact policy and audit against it consistently.

## Applicability to all 14 sections

These are coverage and scope checks, not candidate quotas or an extra retrieval package. Reference anchors below are already in the source commentary, except the illustrative cloud check 24:43; I verified representative anchors locally. They should not be supplied as new seeds to agents.

| Section | What the prompt must allow | What it must not invent |
|---|---|---|
| 1. Trodden road | Guide/follower, middle, signs, habitual walking, dispersal, and opposite destinations; minor details alongside the headline. | A road or footstep in every verse about good conduct. |
| 2. Ownership and servant | Domestic/property relations, compelled versus chosen service, subjugation of animals, human/divine ownership; 16:75 is a direct scene. | Treating every occurrence of “Lord” or “servant” as equally specific. |
| 3. Accounting day | Ruler, standing, debt and term, scales, equivalent payment, blood-money, forgetting testimony; 21:47 and 2:282 ground different branches. | Requiring literal road imagery, or merging dīn and dayn into one word/sense. |
| 4. Womb and upbringing | Womb, kinship, growth over stages, nursing, foster care, teaching, protection; 17:24 connects mercy and upbringing. | A physical womb attributed to God, or rejecting non-womb upbringing because it lacks ر ح م. |
| 5. Completed/bitterly recalled favour | Completion, giving, gratitude, naming benefits, and claiming credit; 48:2 and 26:22 illuminate different sides. | Restricting the image to every occurrence of niʿma or excluding contrary gifts because they are not beneficial. |
| 6. Approval and anger | Descent, faces, bodily signs, approval/anger, and opposing outcomes; 20:81 is a specific anchor. | Importing red cheeks, swelling, or blood into verses that only name anger. |
| 7. Name, brand, sign | Recognition, naming, rising visibility, markings, invocation, and unsupported names; 68:16 is literal branding. | Treating the dictionary's alternative derivations as interchangeable Quranic etymological assertions. |
| 8. Sky | Day, noon/shadow, crescent/stations, celestial worship and its rejection; 41:37 supplies the worship boundary. | Reducing all sky imagery to navigation or calling every high thing divine. |
| 9. Water | Layered cloud, wind, vegetation, rain's visible trace, plentiful water, well, traveller's provision and support; 24:43 concretely stages piled cloud without the section's root. | Inferring a pulley or beam in every watering verse; suppressing a nonlexical cloud parallel. |
| 10. Herd | Ownership, marking, leader, pasture, journeys, straying, wild herds; 16:6 is actual herd movement. | Calling every plural community a herd without a particular supporting relation. |
| 11. Support and standing | Failed mount, weak traveller, help, bodily support, firm structure, upright stance, calm walking; 18:77 stages repair of a standing structure. | Restricting support to ع و ن, or attributing two helpers to a verse that has none. |
| 12. Disappearance | Going out of sight, earth/burial, mixing, forgetting, lost objects or false partners, and destined passage; 32:10 is literal loss in earth. | Reading every ض ل ل occurrence as physical disappearance or every death as the same scene. |
| 13. Led to a home | Sacrificial animal, bride, gift, asylum, protection, passage, arrival and obstruction; 9:6 supplies actual protected conveyance. | Collapsing its four distinct branches into ritual sacrifice or assuming a rejected gift never physically arrived. |
| 14. Meetings | Particular combinations named in the prose: favour/upbringing/enslavement, water/way, judgment/scales, sky/lordship, etc. | An unconstrained union of all verses relevant to any S1 word; equally, demanding every candidate contain two motifs when it specifically completes a stated meeting. |

The section-13 warning is especially useful: its own prose says the gift cannot reach its destination, while 27:36 narrates arrival followed by rejection. A discovery agent must distinguish the commentary's interpretive “arrival” from literal arrival. The later verdict brief already has a conflict mechanism; discovery should identify a boundary without silently rewriting the source commentary.

## Necessary bookkeeping and code fixes

These fit the orchestrator's planned local native helpers. They require no script-launched model, new model stage, or alteration of old outputs.

1. **Make the native protocol executable and unambiguous.** Step 2b still documents `--go`/`codex exec` and an assumed `gpt-6-terra`, contrary to the actual authorized native `gpt-5.6-terra`. Update that section, suppress or explicitly block discovery's legacy `--go` for new runs, and keep local preparation/validation/merge operations separate from model execution. Record exact initial wrapper and follow-up text, source/package/prompt hashes, run tag, requested and observed model/effort, native agent/session identity, turn completion evidence, follow-up delivery identity, and cumulative/per-turn usage. “No evidence” must remain unknown, never a clean protocol result. No inferred substitute model if the requested Terra alias cannot actually run.

2. **Enforce first-turn snapshot and append provenance.** Save immutable `turn1.list.tsv` before follow-up; compare final bytes against it, then parse only the suffix for additions. `merge()` currently classifies turns by physical line number versus count of valid first-turn rows, which fails with blank/malformed lines. Derive provenance from the snapshot, not that arithmetic. Duplicate references must be reported and block a clean merge; dict-comprehension deduplication currently silently keeps the last row.

3. **Differentiate missing, empty, invalid, partial, and complete.** `parse_rows()` currently returns two empty lists for a missing file. I confirmed `check_discovery.check()` therefore reports zero schema errors and zero findings for a nonexistent file. A missing deliverable is an error; an intentionally written empty list is separately representable. Reject blank explanations. A `run.log.json` alone does not mean a successful run: current `merge()` accepts any status, ignores its `bad` rows, and `--status` prints “done” solely from log existence. Require complete expected model runs, two-turn/append evidence, schema validity and an explicit disposition of protocol findings for a production merge. Preserve error artifacts without passing them as a clean union. Accuracy findings can accompany a discovery list; they must not vanish behind `status: ok`.

4. **Validate the handoff file and bind its attempt.** `augment_surah.section_list()` trusts a TSV header and `zip`, and `build()` silently groups unknown tiers that its fixed tier iteration never renders. Validate required columns, field counts, duplicate refs, canonical outside-surah refs, tier/bases, and list identity. The default still points at the original `discovery/sec1.merged.tsv`, not revision2 or revision3. A future authorized handoff must select the explicit revision3 merged file (or an explicit run tag), record its hash and source hash, and refuse unintended fallback. No new Opus directory or `started.json` should be created merely to estimate it.

5. **Preserve the specific bridge for the later reviewer.** `augment_surah.build()` currently supplies canonical Arabic, labels and bases but drops `explanations` entirely. That discards the reason a non-obvious medium/weak candidate was included. Include short, model-attributed rationales explicitly marked “unverified discovery rationale,” together with material review corrections/findings, and tell the reviewer to judge them against canonical text. Never silently replace the historical explanation or present it as authoritative. If preserving independent verdict judgment is an intentional reason to omit notes, make that explicit and retain an accessible audit companion; it is a real tradeoff, not an automatic safeguard supplied by canonical Arabic alone.

6. **Keep contextual additions separate from discovery quality.** The dry builder's ±2 neighbours are a deliberate later-review pool, not model discoveries. Its original 30 and revised 47 neighbour additions explain part of the 775→223 comparison. Report candidate versus contextual counts separately, never auto-promote neighbours, and preserve each linked reference. For known passage dependencies such as 18:1–2 or 4:168–169, flag missing continuations in the handoff audit; do not silently manufacture agent rows. Do not add ±2 around every new candidate indiscriminately just to repair recall.

7. **Freeze later execution metadata.** Before any eventually authorized Opus call, persist its source/list hashes, paragraph map, and exact listed refs. `finish()` currently rebuilds these from live files and only warns on a changed prompt. It must use the prepared snapshot or stop on a mismatch, so verdict completeness and paragraph placement are evaluated against what the agent actually saw. This is a pre-Opus fix, not a reason to postpone independent discovery once its own inputs are frozen.

## Checker limits and proportional verification

Retain the Arabic checker as a review aid. Its ordinary/Uthmani handling still flags legitimate forms such as guidance spellings, and it erases vowel distinctions; therefore it cannot certify fully exact quotation. Its conjunction allowance intentionally tolerates a dropped initial و/ف, so “no findings” also does not mean letter-for-letter reproduction. Do not expand normalization until different words or word order compare equal merely to lower the findings count. A canonical quotation sidecar generated locally after discovery is safer than asking agents to retrieve text or repairing raw lists.

The relevant local regression checks are small and concrete: all 14 source sections parse without dropped members; multiword mercy entries/all branches survive; missing files and duplicate/blank-note rows fail appropriately; blank lines do not corrupt turn provenance; a changed first-turn prefix is rejected; an unsuccessful/incomplete model run cannot yield a clean production merge; the handoff uses the requested attempt; known wrong-ayah wording such as 26:63/20:77 still flags while accepted orthographic differences remain reviewable. No need for another discovery pilot or automated semantic scoring stage.

For the first revision3 image and then each authorized batch, report the union, overlap, model-only and follow-up additions, tiers by model and phase, source-citation coverage, structural/protocol findings, quotation adjudications, and a small balanced substantive sample including weak/indirect candidates and plausible omissions. Counts should be descriptive. Record actual native usage and the $0 incremental subscription charge as such. Complete the prescribed report/commit/push batch boundary before the next batch. The full run's permission does not authorize Opus, and no new permission question is needed merely to continue its already-authorized discovery batches.

## Blocker disposition

- **Resolved during review:** lossy source-item parsing; independently rechecked.
- **Resolve before spawning revision3:** exact final prompt/wrapper, durable native preparation/snapshot/finish and audit rules, fresh attempt identity, and runbook/CLI directions that cannot accidentally launch scripts. Show instruction changes in the established user-visible change procedure; do not invent a second authorization gate over the already-authorized full discovery scope.
- **Resolve before publishing a clean merged handoff:** failed/missing/duplicate/schema handling, snapshot-based provenance, explicit accuracy findings and selected revision3 list hashes.
- **Resolve before any future Opus execution:** authorized scope, frozen packet metadata, rationale/review conveyance, explicit candidate/context counts and fresh estimates. No Opus execution belongs to the present run.

Nice-to-have only: migrate contrast to a separate schema dimension, optimize whole-Quran quotation scans, or assemble a broader benchmark across surahs. None is needed to complete the authorized 28-agent/two-turn discovery workflow.
