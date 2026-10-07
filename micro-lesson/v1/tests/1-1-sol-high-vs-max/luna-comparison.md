# Luna Max: completed pilot assessment

Luna completed the workflow and produced useful, grounded observations. In this run it did not match either Sol condition's breadth of discovery, especially Arabic–Turkish gloss analysis. Its learner-facing prose also needs substantial editing for a Turkish-speaking beginner. Low token cost is a real advantage, but this output is not an equivalent substitute for the fuller Sol passes.

Read [Luna's lessons](luna-max/lessons.md), [its assembled JSON](luna-max/page-output.json), and [its own notes](luna-max/run-notes.md). The original outputs are unchanged. The earlier [High–Max comparison](sol-comparison.md) remains applicable.

## Completion and cost

Luna returned p01–p27 in every discovery output and the assembled page. It produced 13 grammar, 17 semantics and 4 mapping candidates, becoming 32 displayed lessons and 2 deferrals. There are displayed lessons in 26 paragraphs: p05's candidate was merged into p06. It attached 46 distinct ontology concepts. It did not establish an ontology gap.

| Recorded usage | Luna Max |
|---|---:|
| Uncached input | 855,742 |
| Cached input | 10,015,744 |
| Total input | 10,871,486 |
| Non-reasoning output | 46,116 |
| Thinking output | 114,132 |
| Total output, including thinking | 160,248 |
| Largest individual request input | 243,336 |
| Standard API-equivalent cost | $0.2659 |
| Priority/Fast API-equivalent estimate | $0.5317 |
| Start-to-finish wall time | 84m 43s, interrupted and resumed |

The existing session was resumed after a server restart at about 16:54 UTC, with the original task and model settings preserved. Timing includes that interruption and recovery; this is not a clean latency comparison. Recorded usage includes both portions of the run, but may omit any in-flight generation not reported at interruption. See [luna-costs.json](luna-costs.json) for the recorded totals and calculation.

Luna's Standard rates are $0.10/M uncached input, $0.01/M cached input and $0.50/M output; Fast is 2×. At the Priority/Fast estimate, the components are $0.1711 uncached input, $0.2003 cached input, $0.0461 non-reasoning output and $0.1141 thinking. No recorded request reaches the long-context price threshold. These are API-price estimates, not billing records. [Official Luna pricing](https://developers.openai.com/api/docs/models/gpt-6-luna).

Thinking is already included in output and is separated here only to show its cost share. It is not charged a second time. Parent preparation and comparison work are excluded. [Official reasoning usage documentation](https://developers.openai.com/api/docs/guides/reasoning).

## What Luna handled well

- **Specific review scope.** It traced the 552 repair to B004 and the 1064 repair to B005 instead of rejecting all branches of those roots. The local entry reviews confirm those scopes. It also recognized source-attribution qualifications affecting 745 B005/B007. Relevant review files are under `../dictionary/v2/work/entry_creation/<root_id>/tr/review/output/root_review.json`; these are distinct from the unavailable gloss-review response paths. This is a useful example of resolving an evidence question within ordinary source reading.
- **Qualified etymologies.** It retains the documented ism alternatives and attributes the Allah/w-l-h proposal instead of assigning that root image directly to the ayah.
- **Some clear recognition lessons.** The paired -hâ suffixes in p03, bihâ's reference to the names in p10, and the distinction between “yardım isteriz” and “yardımı istenen” in p23 are worthwhile. The latter explicitly annotates the grammatical contrast rather than treating every annotation identically.
- **Specific historical deferrals.** Turkish mevsim and rahmet histories remain open with concrete questions. Their Arabic dictionary meanings are not used as substitutes for dated Turkish attestations.

## What it missed or weakened

**Discovery is substantially thinner, not merely less repetitive.** Four mapping candidates leave many supplied gloss tradeoffs unexplored. Examples include p09's “adaş” versus “the peer deserving that name,” p12's physical marking versus the added implications of sealing, p14's first-rain scope, and p26's “aile” versus lineage. Both Sol runs find several of these. Luna's p09 does teach namesake/peer semantics, but does not explain the cost of the particular Turkish gloss as a mapping lesson could. Its p26 names the kinship sense without teaching the supplied broadening risk in “aile.” These are concrete differences in teaching value, rather than an inference from lesson totals.

Useful grammar opportunities are also absent: noun–adjective agreement in the actual basmala; ism as object versus subject in p07's two quotations; the prohibition in the letter; and the function of -nâ in edhilnâ. At p21 Luna teaches the human/divine uses of rahîm but leaves out the explicit bi’l-mü’minîn phrase that shows where the recipient relation is expressed. Its numerous empty-engine notes often repeat a template claiming there is no distinct opportunity, even where these examples remain available.

**Learner prose exposes internal evidence identifiers.** Many sentences begin with B001/B002/B004 or refer to “p20,” “QAC,” and “lemma.” Those belong in evidence references or author notes. For example, p20's mapping lesson says “B001 … glossunu dışlar” and then refers to “p20’deki” wording. That asks a beginner to understand the authoring apparatus before understanding Arabic.

**Terminology is insufficiently introduced.** The page uses “genitif,” “Form V etken ism-i fâil,” “çekimli muzâri,” and “ism-i mefûl,” while every reminder list is empty. Twelve of 32 lessons are level 3. The run notes say necessary distinctions are supplied locally, but the wording does not consistently support that claim. Turkish reading aids also shift toward academic/English conventions such as `dhukira`, `wa-udhkurū`, and `shakhsun`, despite the supplied Turkish readings.

**The Rahmân/Rahîm treatment needs another editorial decision.** The p20 lesson usefully avoids a universal pattern formula and reports the dictionary's separate lexical glosses. Its key calls them “different branches,” however, and it teaches C018 even though both uses are explicitly in the same B001 branch. This is a lexical-unit/facet distinction within a branch. The adjacent mapping lesson protects “merhametle dolu” by calling it a contextual description, without explaining what independently supports “dolu” or giving the reader the missing good-action facet as a usable positive clarification. It should distinguish the supported contextual description from the commentary's stronger pattern claim more clearly.

**Some evidence precision is lost.** The p20 exclusion locator points to `reviewed_glosses.excluded[merhamet]`, but that prepared object has no `excluded` field; the exclusion is in `branch.excluded_glosses`. The underlying evidence exists, but the locator is wrong. Luna also uses the 19:65 sky quotation in p08, where it would need a clearer local attachment or an explicit connection to the following paragraph.

Luna does not identify Max's B002 person-versus-situation conflict at 15:75. Nor does it preserve the p06 historical claim about Turkish isim as a deferred opportunity or specifically explain its rejection. These omissions matter when the workflow is expected to retain worthwhile unresolved questions.

## Judgment for this workflow

| Condition | Displayed lessons | Deferred | Standard estimate | Priority/Fast estimate |
|---|---:|---:|---:|---:|
| Sol High | 64 | 4 | $2.59 | $5.18 |
| Sol Max | 70 | 8 | $2.90 | $5.80 |
| Luna Max | 32 | 2 | $0.27 | $0.53 |

Luna demonstrates useful source handling and can author selected lessons. This run does not support treating it as a replacement for Sol for comprehensive discovery and beginner-ready assembly. Its recorded cost is about one tenth of High's, but the resulting teaching coverage differs materially. Max's strongest extra value over High remains evidence reconciliation and some finer contrasts; High still contributes valuable observations Max misses. All three need linguistic editing before publication.

No new pipeline stage, automated completeness test, hash mechanism, or mandatory reviewer is implied by this assessment. The gaps are in discovery choices, final wording, source interpretation and ontology attachment—the work the existing engines and assembly already own.
