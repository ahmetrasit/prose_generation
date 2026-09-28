# 29:38 — Sol synthesis → Astra prose: clearer, but a failed treatment

The new commentary is substantially easier to follow. It develops a connected explanation in 1,221 reader
words instead of 5,131, and all 18 Arabic quotations pass the exact source check. It also loses the earlier
commentary's strongest supported lexical relationship: the tent seam in the sight family, the web-like eye film
in the road family, and their interaction with the nearby spider-house. That loss was already present in Sol's
synthesis. Under the stopping rule frozen in [COMPOSITION_TRIAL.md](COMPOSITION_TRIAL.md), this treatment fails.
It is not accepted, and no prompt revision or further generation starts automatically.

Read the immutable [new commentary](out-sol-astra-composition-29-38/s029/29_38/29_38.reading.tr.md),
[Sol synthesis](out-sol-astra-composition-29-38/s029/29_38/composition.json), and
[earlier Astra commentary](out-astra-blind-29-38/s029/29_38/29_38.reading.tr.md).
The primary agent performed the comparison; no comparison agent was used.

## What was tested

The user specified **Sol 6 max for interpretive synthesis, then a fresh Astra 6 max for Turkish prose**.
Each stage generated once, with no inherited conversation, interruption, retry, repair or manual prose edit.
The ten source files are byte-identical to the earlier arm: the same discovery/QeQ records, dictionary,
concordance, word notes, Quran snapshot and surrounding text. No new upstream call was made. Both arms retain
the standalone scope: the 29:21–51 window, no window network and no preceding reader prose.

This is a development comparison on the deliberately reused 29:38, not a blind generalization result. The
generation briefs contain no target answer or named desired image. Previous commentary, the review, the North
Star and the predeclared evaluation never entered either generation. The whole process changed: an additional
Sol synthesis stage, a selected handover and a prose-only writer. The result cannot isolate a model effect or
prove that a particular prompt line caused the loss.

The setup was committed before Sol as `79d7e934e`; the completed Sol handover was committed before Astra as
`b42a5ef5a`. The two responses and all inputs remain checksum-bound. The earlier commentary is unchanged.

## Comparable measurements

| Measure | Earlier Astra | Sol → Astra |
| --- | ---: | ---: |
| Raw words, including Arabic tags and metadata | 6,509 | 1,374 |
| Reader words, replacing each tag with its Turkish gloss | 5,131 | 1,221 |
| Prose paragraphs | 60 | 15 |
| Median / maximum reader words per paragraph | 85 / 111 | 78 / 109 |
| Headings, including title | 6 | 0 |
| Exact Arabic quotations | 140 | 18 |
| Quran / dictionary quotations | 89 / 51 | 18 / 0 |
| Distinct quoted dictionary branches | 50 | 0 |
| Distinct cited ayat, expanding ranges | 137 | 30 |
| Distinct written reference starts, before range expansion | 121 | 30 |
| Writer inventory JSON | 19,251 bytes | None by design |

The reader-word reduction is 76.2%. The improvement is principally fewer developments and a sustained argument;
individual paragraphs have not become dramatically shorter. No word cap was imposed. Zero dictionary quotations
is descriptive evidence of the change in content, not a failed quotation quota. Removing the inventory task also
removes its previous format failure; it does not establish semantic success.

The complete counts, hash checks and measurement definitions are in
[comparison.metrics.json](out-sol-astra-composition-29-38/s029/29_38/comparison.metrics.json).

## What improves

The opening gives the plain sense and immediately establishes the two audiences: people who found their own
works persuasive, and later listeners who can see what those works came to. That relationship returns through
the passage and governs the ending. The reader has a reason to follow each development even without headings.

Paragraph 7 develops a useful reversal already present in the baseline: the constructed *ayah* advertises its
makers' power; their destruction becomes an *ayah* exposing the limits of that confidence. Paragraph 11 connects
the people who saw a promising cloud with the later view in which only their dwellings remain. Paragraph 14's
Pharaoh tower makes the problem of a supposedly authoritative vantage point concrete. These are explanations,
not a list of references. Their improved prominence is a gain, not a newly discovered reading.

The former excursions through the tribe name's root, the crow, divorce, stones, cosmetics and the extended well
apparatus disappear. Their absence is generally helpful: the reader no longer has to carry a succession of
associations whose effect on the ayah is unclear. The account remains careful about deeds being broader than
buildings, apparent beauty being distinct from goodness, and sight being distinct from sound judgment.

The rescue correction survives: the text explicitly says the ruined settlements do not imply that everyone was
killed, and cites the rescue of the prophets and believers. It does not reproduce the problematic punishment
assignments. It presents the possibilities in *mustabsirin* without forcing a single psychological gloss.

## The consequential regression

The baseline's prose paragraphs 39–40 (blocks 44–45 when headings are counted) explain more than a fragile house.
The seam joins material into a shelter; the eye film resembles a spider's web; covering changes function when
it moves from around the person to in front of the eye. Protection becomes obstruction. The road and sight words
of 29:38 participate in the spider-house of 29:41 through attested dictionary senses, while their contextual
meanings remain intact.

The new paragraph 8 retains only the ordinary comparison between impressive dwellings and misplaced reliance.
It never develops the seam or the film. The later discussion of seeing and judging does not recover their
material relationship. This is not a loss inferred from missing IDs: the earlier explanation performs an
interpretive operation that the complete new text does not perform.

The loss can be located precisely:

1. **Available to Sol:** the full research contains F74 and F75, their E_F74/E_F75 expansions, and the exact branches
   `ب ص ر B006` and `س ب ل B010`. The research itself already links the two findings. The rare senses are present
   in the frozen dictionary; they are not missing inputs.
2. **Absent from Sol's answer:** its 819-word explanation omits both relations, and its selection omits both
   findings and both branches. It selects 19 of 169 records, ten branches, 27 Quran passages and three concordance
   sections. No reason for this particular omission was requested or provided, so the internal reason is unknown.
3. **Absent from Astra's initial packet:** the compiler follows Sol's selection. It supplies the explanation and
   selected sources, along with compulsory counter-evidence, but no index of unselected findings or branches.
   The writer receives neither the missing relationship nor a cue naming it.
4. **Absent from the finished prose:** Astra makes no additional source lookup and follows the supplied argument.
   It preserves the valuable connections Sol did supply. It does not introduce the decisive regression at the
   prose stage, and it does not recover it there.

The [contemporaneous synthesis audit](out-sol-astra-composition-29-38/s029/29_38/synthesis.audit.json) records this
omission while Astra was still running. That audit was evaluation-only; no feedback or altered evidence was sent
to Astra. It remains unchanged as a record of what was knowable before the writer finished.

## Root cause exposed by this experiment

The old design encouraged exhaustive representation and produced a catalogue. This design successfully removes
that pressure, but does not reliably distinguish an expendable association from a consequential supported
surprise. Sol builds its argument chiefly from Quranic narrative and wording relationships, despite the generic
instruction to retain unusual readings when they contribute. This run shows the resulting selection failure;
it does not establish whether another model would make the same selection.

My handover design then makes that first selection decisive. Retaining an archive on disk is different from
making omitted evidence discoverable to the next stage. The helper can fetch a known item or branch key, but the
writer is not told what unselected material exists. Permission to investigate an omitted relationship cannot
help when the writer has no cue that the relationship was there. The structural gate checks schema and source
keys, not interpretive contribution. It therefore correctly accepts a structurally valid but substantively
insufficient synthesis.

This is an architectural limitation as well as an observed Sol omission. It would be unfair to blame the user's
model choice or to call Astra incapable on this evidence. It would also be misleading to call the trial a success
because it is shorter, fluent and source-correct. We shifted from excessive inclusion to consequential exclusion.

## Review against the frozen criteria

| Criterion | Finding |
| --- | --- |
| Orientation | Improved. Plain sense first; the two audiences and changing interpretation of visible works give a clear line of development. |
| Supported surprise | Failed. The shelter/seam/eye-film relation is lost in Sol and remains absent in Astra. The ordinary spider-house parallel is not equivalent. |
| Convergence and emphasis | Improved for the retained argument. The signs and sight sequences converge, but the relation carrying the distinctive lexical contribution disappears. |
| Earned scope | Mixed. Most detached excursions disappear; the reduction also removes the contribution explicitly protected by the pre-run criterion. |
| Grounding | The 18 exact-source tags and prose format pass. No frequency claims need checking. The questionable tribe-name root development is gone. Exact quotation checks do not certify interpretation. |
| QeQ and Turkish losses | Mixed. QeQ is better organized but still supplies most of the development. Amel and basiret distinctions survive; the narrowed Turkish use of ayet is made explicit. Ziynet's named Turkish comparison, sebil's fountain sense and the mesken/miskin relation disappear. These smaller omissions are not all equivalent in value. |
| Corrections and limitations | Retained in the matters the new prose develops. Rescue survives; buildings do not exhaust deeds; geographical roads are not identified with the contextual right path. Sequential/surah continuity remains untested. |
| Stage attribution | The decisive loss precedes the writer. Astra carries the supplied reasoning; no comparable new substantive regression was identified in rendering it. |

The source and format checks pass, but the predeclared semantic condition fails. There is no accepted pointer.
The independently recorded verdict and exact paragraph evidence are in
[independent.review.json](out-sol-astra-composition-29-38/s029/29_38/independent.review.json).

## Input use, execution and preservation

Sol received 171,674 bytes and made six Quran lookup calls returning 27,355 bytes: 36 distinct requested ayat,
98 distinct returned ayat with context. Astra received 66,379 bytes and made zero lookups. Its selected concordance
sections occupy about 26.2 KB of that packet, selected dictionary lines about 3.5 KB, and the composed explanation
with limits about 6.5 KB. The absence of dictionary quotations does not prove the ordinary glosses were unread;
the missing rare branches can, however, be traced directly to selection. Large research retention is not itself
evidence that its distinctive material reaches the reader.

All 30 ayat cited in the new prose are referenced in its supplied packet; every actual Arabic quotation is exact
against its declared frozen source. Neither stage produced an exhaustive inventory account. Sol's 7,168-byte JSON
still contains the explanation and source selection, so structural output has been reduced and relocated, not
eliminated from the whole process.

The observed claim-to-ingestion intervals were 6 minutes 21 seconds for Sol and 8 minutes 53 seconds for Astra.
These include retrieval and coordination and are not provider latency. Provider tokens and billing were not
exposed. Byte counts do not establish a cost saving, and cost is not a rejection reason for this authorized test.

Thirty offline tests passed before generation. There were no subsequent implementation changes. Final checks
confirm all 14 new frozen files, both prepared packets, four generation-code hashes, the baseline's 13 frozen
files, all ten copied sources, and 298 copied historical data files. The pre-run review plan and baseline candidate
are unchanged. Concurrent v15 work is outside this experiment.

The result justifies stopping this particular treatment under the agreed rule. It establishes neither that all
two-stage workflows fail nor that further prompting of this variant would succeed. The outputs are preserved
for inspection; no target-specific restoration or new model call is part of this result.
