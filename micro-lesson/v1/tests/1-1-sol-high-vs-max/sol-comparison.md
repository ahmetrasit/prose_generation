# 1:1 pilot: Sol High versus Sol Max

Both completed the full 27-paragraph base reading. Max's strongest observed gain was reconciling dictionary evidence and distinguishing more local opportunities. It was not consistently more accurate at grammatical explanation. Neither output should be published untouched. This is one qualitative pilot, not a measured general ranking of the models.

Read the actual outputs: [High lessons](sol-high/lessons.md), [Max lessons](sol-max/lessons.md). Their JSON pages and three discovery outputs are in the same folders. This comparison leaves those results unchanged. Luna Max is not included in this Sol comparison; its completed results are assessed in [the Luna comparison](luna-comparison.md).

## Recorded usage and estimated cost

These are the completed agents' cumulative usage totals from their local rollout records, not token estimates from file sizes. Full metadata and arithmetic are in [sol-costs.json](sol-costs.json). Input accumulates across tool calls, which repeatedly carry the growing context; it is not the size of the shared packet alone. Non-reasoning output includes tool calls, JSON authoring and other generated text, not just the learner-facing prose.

| Measure | Sol High | Sol Max |
|---|---:|---:|
| Uncached input tokens | 188,411 | 221,246 |
| Cached input tokens | 8,113,152 | 8,536,832 |
| Total input tokens | 8,301,563 | 8,758,078 |
| Non-reasoning output tokens | 39,367 | 52,986 |
| Reasoning output tokens | 19,728 | 22,003 |
| Total output tokens, including reasoning | 59,095 | 74,989 |
| Cache-write input tokens | 0 | 0 |
| Largest individual request input | 176,120 | 210,946 |
| Agent elapsed time | 20m 13s | 18m 13s |
| Standard API-equivalent cost | $2.5904 | $2.8997 |
| Priority/Fast API-equivalent estimate | $5.1808 | $5.7995 |

Standard Sol prices checked on 2026-10-07 are $2/M uncached input, $0.20/M cached input, $2.50/M cache writes and $10/M output. Fast is 2× the applicable rates. No observed individual request reached the 272K long-context threshold; cumulative millions do not trigger that threshold. See [official Sol pricing](https://developers.openai.com/api/docs/models/gpt-6-sol).

Reasoning tokens are already included in output tokens and use the output price; they must not be added twice. Cached tokens are likewise part of total input. See [official reasoning usage documentation](https://developers.openai.com/api/docs/guides/reasoning).

| Cost component, Priority/Fast estimate | High | Max |
|---|---:|---:|
| Uncached input | $0.7536 | $0.8850 |
| Cached input | $3.2453 | $3.4147 |
| Non-reasoning output | $0.7873 | $1.0597 |
| Thinking | $0.3946 | $0.4401 |
| Total | **$5.1808** | **$5.7995** |

The native agent tool advertises Priority service for these models, so the second estimate reflects that configured availability. The rollout usage does not contain an invoice or confirm the returned service tier. These figures are API-price equivalents, not actual account charges. They exclude the parent agent's common preparation/comparison work and the Luna run.

Max cost approximately 11.9% more at either rate schedule, used 11.5% more reasoning tokens and 34.6% more non-reasoning output, and finished about two minutes sooner. A single concurrent run does not establish a latency advantage. Most of the estimated cost in both conditions comes from repeated cached input, not thinking.

## What each produced

| Measure | High | Max |
|---|---:|---:|
| Assigned paragraphs covered in all three engines and assembly | 27/27 | 27/27 |
| Grammar candidates in saved output | 30 | 34 |
| Semantics candidates in saved output | 44 | 43 |
| Mapping candidates in saved output | 29 | 33 |
| Assembled lessons | 64 | 70 |
| Deferred opportunities | 4 | 8 |
| Distinct ontology concepts attached | 65 | 82 |
| Average annotations per lesson | 3.55 | 3.29 |
| Lessons with reminders | 3 | 0 |

Counts describe the artifacts and are not quality scores. Max's eight deferrals are not eight independent discoveries: several separate the same Rahmân/Rahîm problem into individual-form, paired-form and imagery questions. Neither run established a missing ontology concept. That supports this page's coverage; it cannot establish complete coverage of every future passage.

## Shared strengths

Both distinguish the written basmala from a supplied action such as “I begin.” Both preserve the documented س م و / و س م alternatives for ism, the qualified Allah/ilâh derivation, and the alternative و ل ه explanation. Both keep root-family imagery separate from an occurrence's lexical meaning.

Both correctly allow a short local “ad” rendering even though the dictionary branch includes additional uses. They consult the branch-specific Turkish glosses rather than treating every recorded loss as a mistake in the verse. Both separate womb, kinship, organ illness and mercy uses, and withhold unsupported historical Turkish claims and fixed Rahmân/Rahîm formulas.

## Max's useful gains

- **A concrete source conflict at p14.** `root_001650/B002` defines reading signs in a person, whereas its reviewed `lu_009` gloss permits reading signs of a situation. Max keeps the supported 15:75 observation but defers the disputed branch-scope application. High applies the branch without flagging this discrepancy. The conflict is visible in the [supplied branch evidence](input/dictionary/root_001650-B002.json); it is not a missing ontology term.
- **More precise local contrasts.** At p07, `ismin_gorevi` compares ism as object in 87:1 and subject in 55:78; High teaches only the object example. At p11, `in_hi_illa` distinguishes negative in from conditional “if.” At p12, `isaretleyen_arac` distinguishes the marked entity from the marking instrument. High does not retain equivalent lessons for these contrasts.
- **Additional contextual reading.** At p10, `adlarla_cagir` distinguishes the one called from the names used to call him. At p22, `rahman_azap_baglaminda` uses 19:45 to constrain an over-simple gloss. These are distinct applications, not just more tags.
- **More explicit unresolved opportunities.** Max preserves the unsupported historical account of Turkish mevsim as a question. High teaches the contemporary contrast but does not record that historical opportunity as deferred.

## High's useful gains

- **Cross-verse root boundaries.** High independently consults the indexed entries and adds ihdinâ versus sacrificial hady (p04), Rabb versus a separate rearing action (p08), dâllîn versus a stray animal (p14), and en‘amte versus livestock (p27). These respond to the commentary's connections; Max does not cover them as separate lessons.
- **Different grammar opportunities.** High teaches the fronted object in iyyâka na‘budu (p15), the command/prohibition contrast in the letter (p13), and the nested possessive phrase “Allah'ın rahmetinin izleri” (p25). Max omits those particular lessons.
- **Better quoted scope in two contrasts.** High retains `لَمْ` in its “anılmadı” example and the prohibitive expression in its “üstünlük taslamayın” example. Max's corresponding learner-facing sentences drop the particles while retaining negative Turkish translations, as detailed below.

## Concrete problems remaining

**Max, p04 `anildi_edilgen`:** the sentence presents `ذُكِرَ` / `يُذْكَرِ` as “anıldı/anılmadı.” The second form is not negative by itself; the negative construction in 6:121 is `لَمْ يُذْكَرِ`. The full anchor contains lam, but the explanation strips it off while retaining its meaning. The supplied QAC record explicitly separates lam (NEG) from yudhkar (passive verb).

**Max, p13 `talu_baska_kok`:** it quotes only `تَعْلُوا۟` while giving “yükselmeyin/büyüklük taslamayın.” The prohibition belongs to the full `أَلَّا تَعْلُوا۟` construction. The full anchor again contains the missing particle. This is the same teaching-scope error in a second occurrence, not merely a spelling issue.

**High, p22 `upon-himself`:** the explanation says the suffix -hi in nafsihi supplies “kendi.” The stem nafs supplies self, and the suffix supplies the third-person reference. QAC 6:12:11:1–2 explicitly separates the noun from its 3MS pronoun. The current wording teaches the wrong division.

**High, some ontology attachments:** `ML:C248` means multiple related senses of one word. Using it for ihdinâ versus sacrificial hady, or en‘amte versus livestock, conflates distinct lexical items in one root family with polysemy of one word. Branch applicability and lexical-unit distinctions fit those lessons more directly. Both runs also attach `ML:C024` in places that merely name a common root without teaching the catalogue's required distinction between attested relation and resemblance.

**Both, beginner accessibility and repetition:** most lessons are level 2, but reminders are sparse. Max's p01 `adlari_niteleme`, for example, names “cer durumu” without explaining it or supplying a reminder. Several lessons recur to “this root image is not the meaning here”; some recurrence is justified by different lexical uses, but a reader still needs enough positive form-and-meaning teaching. High's p03 `ride-and-possessives` combines a plural imperative with a possessive-pronoun lesson; those are independently reusable observations. These are editorial issues inside the existing assembly step, not reasons to build another validation stage.

## Limits and lean improvements

The agents each ran all three perspectives and assembly in one continuing context. They are two independent full runs, not six isolated discovery calls. They used the same starting evidence and could consult the same indexed original sources. No comparative linguistic coaching was sent into either run. Their own final audits are not independent verification; this report is a focused editorial comparison, not an exhaustive linguistic certification.

The shared preparation missed listing 1:7 under p14 even though its prose explicitly discusses the seventh verse. That ayah was present elsewhere in the packet and High retrieved it. This omission is a real preparation gap and limits how strongly to interpret Max's missing dâllîn lesson. The input is left unchanged while Luna runs, preserving the same starting conditions.

The useful next refinements fit the existing runbook: resolve prose-only verse references during preparation; retain the minimum complete Arabic expression needed for the claimed Turkish meaning; distinguish stems from pronoun suffixes when teaching word parts; and apply each ontology term's actual boundary to the final sentence. These are linguistic reading instructions, not hashes, extra reviewers, schema gates or automated completeness tests.

For this pilot, Max's extra cost bought valuable evidence scrutiny and several finer contrasts. High remained competitive and found useful material Max missed. A blanket claim that Max is safer, or that High is sufficient for unattended publication, is not supported by these outputs.
