# Sol OCR diagnostic and recommendations — 2026-10-05

**Sol substantially improves these priority transcriptions, but a single Sol pass does not meet the requested near-lossless, diplomatic-text requirement.** Use it as a candidate transcriber and image-based correction tool within a checked workflow. No page from this experiment is accepted for production. The most economical starting point for Bint al-Shāṭiʾ remains the acquired structured text; al-Khūlī still needs recognition and correction.

**Later experiment:** the [al-Khūlī follow-up](../khuli-followup/README.md) now tests disagreement detection and fresh crop readings on these same six pages, and checks the proposed digital editions. Blind crop readings worsen normalized Khūlī excerpt word error from 9.2% to 18.9%; cropping alone has not demonstrated reliable correction. The recommendations below describe the next step as understood before that follow-up; use its findings when deciding what to scale.

## What was tested

Six native agents ran `gpt-6-sol`, one page per fresh agent, on exactly the six priority images evaluated in the [Luna pilot](../luna-pilot/README.md): Bint v1 PDF pp50/100, Bint v2 pp49/98, and al-Khūlī pp92/100. Native logs verify **medium reasoning** for all six; no effort override was supplied. Agents received no inherited conversation, existing OCR, digital edition or reference answers. The [brief](BRIEF.md) retained the earlier transcription requirements, adapted to one page and with explicit original-detail image forwarding. Images were unchanged; each agent viewed its assigned image twice at original detail. No crops were used.

The [manifest](manifest.json) freezes image/assignment/reference hashes and candidate paths. One al-Khūlī agent encountered two capacity errors before completing on its third turn with the same assignment and model. No model substitution occurred. The six draft texts and six valid review files are under the sources' ignored `raw/ocr-candidates/sol-pilot-2026-10-05/` directories. Only the report, instructions, scripts and compact evidence are versioned.

**This compares configurations, not model family in isolation.** Luna had four images per agent and low/medium effort; Sol had one image and medium effort. The experiment cannot separate the gains from model capacity, isolated-page handling and other run variability. No claim that Sol alone caused every improvement is warranted.

Official documentation confirms [Sol accepts image input](https://developers.openai.com/api/docs/models/gpt-6-sol); the [vision guide](https://developers.openai.com/api/docs/guides/images-vision) recommends original detail for fine-detail tasks where supported. Neither source establishes accuracy on these books. The local scan comparisons below determine the recommendation.

## Measured quality

The same eight frozen, supervisor-transcribed passages provide **440 reference words**. They are purposive diagnostic excerpts, not random pages or independently human-verified gold. Normalization removes harakāt, punctuation and some spelling distinctions; excerpt alignment allows a free prefix/suffix. The short Bint p100 comparison uses its entire body. These deliberately forgiving rates do not measure whole-book accuracy or diplomatic fidelity.

| Work | Luna low | Luna medium | Sol medium, one page per agent | Structured Bint export |
|---|---:|---:|---:|---:|
| Bint al-Shāṭiʾ, 234 reference words | 25 edits / **10.7%** | 22 / **9.4%** | 8 / **3.4%** | 8 / **3.4%** |
| Al-Khūlī, 206 reference words | 59 / **28.6%** | 86 / **41.7%** | 19 / **9.2%** | Not found |

Sol's normalized character edit rates are 15/1,207 (**1.2%**) for Bint and 35/1,104 (**3.2%**) for al-Khūlī. Word rates include joins/splits. Matching numerical rates for Sol and the Bint export do not mean the same errors or equivalent whole-book coverage. Full alignments and final artifact hashes are in [results.json](results.json); the references remain unchanged in [priority_references.json](../luna-pilot/priority_references.json). An interim al-Khūlī calculation was 8.7%; the final files, after the agent's last self-edit, give 9.2%, which is the reported result.

Sol repaired several serious Luna failures: it kept `الحاقة ٢٨`, the negation in `بل لا نعرف`, the wording `يغفر لمن يشاء`, the attribution to al-Zamakhsharī, Ibn al-Muʿtazz's name, and al-Khūlī's printed page labels. It also retained al-Khūlī p100's final paragraphs and transcribed the previously omitted footnote.

Material defects remain. The supervisor viewed all six original-detail images and checked these examples:

| Scan | Printed text or feature | Sol result | Consequence |
|---|---|---|---|
| Bint v1 PDF p50 | `الثرى`; list includes `١٣٥` | `المُثْرِي`; omits `١٣٥` | Changes a lexical claim and loses a verse locator |
| Bint v1 PDF p50 | `المبعث`; later `المفسرون` | `البعث`; `المعاصرون` | Fluent substitutions remain outside obvious scan damage |
| Bint v1 PDF p100 | `قبلهما`; `لا يغادر` | `قبلها`; `لا تغادر` | Changes wording even on the very short page |
| Bint v2 PDF p49 | `ومعها آيات`; `قرينة صارفة لمن البشر` | `ومنها آيات`; `قرينة صارفة من البشر` | The measured attribution passages match, but other wording on the same page changes |
| Bint v2 PDF p98 | `واستغشى ثوبه وبثوبه ، تغطى به` | `واستغشى ثوبه وتغطى به` | Drops a lexical construction |
| Al-Khūlī PDF p92, printed p90 | `فى عبور الأجيال`; `فإنه نواة وجهت` | `في عصره والأجيال`; `فإنه إذا وجهت` | Rewrites the argument despite getting the author's name right |
| Al-Khūlī PDF p100, printed p98 | `وتعاجز الدنيا`; `تؤيد الذى أسلفنا فى المنزع النقدى` | `وتناجز الدنيا`; `تزيد الذي أسلفناه في النزوع النقدي` | Remaining substitutions; two other spans are explicitly `[?]` |

Printed harakāt are still lost. Bint p100 has prominent marks on words such as `يُجْزَ`, `يُحَاسَبْ`, `مُحْضَرًا` and the closing quotation; Sol mostly emits unmarked text. Its four Bint files contain 50, 4, 46 and 25 combining marks, compared with zero in Luna low and 3–4 per page in Luna medium. Counts show a change in behavior, **not diacritic accuracy**: added or misplaced marks also count. Sol also systematically modernizes many printed undotted yeh spellings, which the normalized metric conceals.

All agents declared `complete: true`; that means attempted coverage, not a verified edition. Several incorrect words are presented without `[?]`. Neither that flag nor model agreement is an acceptance rule.

## Actual usage and priority projection

Final native counters for all six agents, including the capacity-retry session:

| Counter | Tokens |
|---|---:|
| Input | **1,161,883** |
| Cached input, already included above | 1,040,000 |
| Output | **16,806** |
| Reasoning, already included in output | 8,167 |
| Non-reasoning output | 8,639 |

These are agent-session tokens, including instructions, history and repeated image/tool rounds. They exclude the supervising agent's research, review and reporting. They are not raw image/text token requirements and are not a subscription invoice.

Scaling this exact inefficient native-agent setup by each source's own sample yields the following **one-pass scenario**, before any correction or acceptance review:

| Work | Sample basis | Pages | Input | Output |
|---|---|---:|---:|---:|
| Bint al-Shāṭiʾ | Four pages, including one unusually short page | 418 | 73.67M | 0.958M |
| Al-Khūlī | Two pages, including capacity retries | 368 | 84.07M | 1.406M |
| Total | Six purposive pages | **786** | **157.74M** | **2.364M** |

About 141.41M of the projected input is cached; 1.166M of output is reasoning. Cache behavior, page density and tool rounds vary. This is **not a production budget recommendation**. Whole-book re-OCR of Bint is especially wasteful given its available digital text. A lean scripted model request containing only the relevant image/region, instructions and necessary candidate text would avoid much agent overhead, but that architecture's actual usage and quality have not been measured here. Native agents demonstrate recognition behavior; they need not be the production request wrapper.

## Recommended work

1. **Bint al-Shāṭiʾ: reconcile the structured edition with the scans.** Map every export record to a PDF page, explicitly handle missing prefaces/front matter/end matter, and check edition differences. The acquired export has 373 records versus 418 PDF pages; those counts are not interchangeable. Use Sol on missing regions and disputed readings, with the scan as the authority. Preserve export text and corrections separately so every intervention is reviewable. See the [source and coverage audit](../luna-pilot/SOURCE_ALTERNATIVES.md).
2. **Al-Khūlī: test recognition on small page regions with a separate correction pass.** Use deterministic crops with page/region coordinates, overlap at boundaries and a coverage map. A fresh request must see only its page or region. Reconcile recognition candidates against the image, checking names, negations, numbers and footnotes explicitly. Cropping and the correction pass are recommended next experiments; they were not tested in this six-page run, so their improvement is not yet demonstrated.
3. **Measure preservation before scaling.** Add diacritic-sensitive and spelling-sensitive comparisons to the normalized search metric. Build independently checked reference pages across each work's layouts. Require all regions accounted for and all flagged spans adjudicated; inspect apparently agreeing text as well, because models can share a wrong reading. Human image review is needed for a defensible near-lossless claim on critical passages; sampling alone cannot certify every character in 786 pages.
4. **Make the data useful while retaining its status.** Keep immutable scans, raw witnesses, draft recognitions, correction history and stable PDF-page locators. Store accepted diplomatic text separately from normalized search text. Index drafts only with an explicit unverified status; verify quoted evidence against the image until its text is accepted. Small routing summaries can choose pages to retrieve, while exact passages and adjacent context supply evidence.
5. **Use scripts for production orchestration.** Scripts should render, submit bounded requests, checkpoint, map regions, detect page gaps and write importer files. Reserve agent reasoning for difficult recognition/reconciliation and QA. Prepare a measured request budget after the revised method passes the pilot; do not extrapolate the failed transcription wrapper into a bulk run.

This is still **both a data and workflow repair**. A stronger model helps, but source acquisition, edition/page alignment, image handling and acceptance checks determine whether the final corpus preserves the evidence. The full 12,026-page scope remains pending; accepted pages remain zero.

## Reproducibility

- `prepare.py` derives the six assignments from the frozen Luna manifest and refuses to overwrite an existing Sol manifest. It does not launch models.
- `measure.py` verifies hashes, reads local native session counters, validates the six output pairs and compares the frozen excerpts. It does not launch models or alter candidate text. Run `python3 -B enrichment/v2/audits/2026-10-05-ocr-reliability/sol-pilot/measure.py` from the repository root.
- `results.json` captures exact session/model/effort records, final usage, tool-call metadata and artifact hashes without embedding full session logs or image data.
- Candidates remain under `raw/ocr-candidates/`; no source `raw/ocr/` production file was created or overwritten.
