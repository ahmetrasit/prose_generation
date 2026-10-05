# Luna for OCR: recommendation and token budget

**Pilot completed:** [measured results and the 786-page priority recommendation](luna-pilot/README.md). Both efforts failed the Bint al-Shāṭiʾ/al-Khūlī preservation checks. The 48 drafts used 3.120M input and 62,740 output tokens in total. A [structured Bint al-Shāṭiʾ alternative](luna-pilot/SOURCE_ALTERNATIVES.md) was subsequently acquired. The estimates and proposal below are retained as the pre-run plan, not the current quality conclusion.

**Luna is a reasonable candidate to test. Neither low nor medium is yet validated for these Arabic, Urdu and Ottoman-script scans.** The local Tesseract failure does not predict Luna's performance. Use the exact requested model, `gpt-6-luna`, and compare low/medium on identical page images before choosing a production setting.

Luna accepts images and supports both efforts. Official API guidance recommends starting at low for extraction. For this collection, my proposed starting point is **low for clean transcription**, with medium tested on difficult layouts, footnotes and mixed scripts. That is a hypothesis, not an accuracy result. Higher effort must not become permission to reconstruct unclear words, modernize spelling or supply remembered Qur'anic wording. [Model capabilities](https://developers.openai.com/api/docs/models/gpt-6-luna), [extraction effort guidance](https://developers.openai.com/api/docs/guides/deployment-checklist)

## Estimate for all 12,026 pages

These are **planning scenarios, not measured Luna usage**. [estimate_luna.py](estimate_luna.py) reads the geometry of every target PDF page; [luna_estimate.json](luna_estimate.json) records assumptions and arithmetic. It makes no model calls.

| Component | Full collection |
|---|---:|
| Image + short instruction input, one direct call per page | **96–114 million tokens** |
| Input with an illustrative native-agent tool cycle, four pages per fresh agent | **293–341 million tokens** |
| Visible transcription output, either method | **11–22 million tokens** |
| Extra reasoning if it averages 250 tokens/page | **3.01 million output tokens** |
| Extra reasoning if it averages 1,000 tokens/page | **12.03 million output tokens** |
| Extra reasoning if it averages 3,000 tokens/page | **36.08 million output tokens** |

The reasoning rows are **sensitivity examples, not predictions for low or medium**, and are alternatives, not cumulative charges. Reasoning counts toward output usage; the exact count is available in the response usage. There is no fixed low-to-medium multiplier. [Reasoning-token accounting](https://developers.openai.com/api/docs/guides/reasoning)

Image assumptions: render geometry at 300 dpi, cap the longest side at 3,500 pixels, retain the full page, use 32×32-pixel patch counting, and illustrate multipliers from 1.0 to 1.2. This yields 92.12 million raw patches before the multiplier. **The fetched official vision table did not explicitly specify GPT-6 Luna's resizing/multiplier**, so this is a transparent sizing proxy, not an established Luna billing formula. The pilot must measure actual image input usage and verify fine text is still readable. Avoid confusing low reasoning with low image detail; OCR needs fine detail. [Image sizing and OCR guidance](https://developers.openai.com/api/docs/guides/images-vision)

Native-agent assumptions: four pages per fresh agent, a hypothetical 10,000-token harness, three model passes, images present in two passes, and the generated transcription visible again on the completion pass. No parent conversation is inherited. The actual harness, tool calls and cache behavior may differ substantially. Repeated source reads, retries, review passes and long running agent histories are excluded. A full independent transcription pass roughly doubles page processing before reconciliation; targeted review costs less but offers a different assurance level.

Visible output assumptions by source group:

| Group | PDF pages | Assumed tokens/page | Total visible output |
|---|---:|---:|---:|
| Arabic works | 2,161 | 800–1,600 | 1.73–3.46M |
| Badawi–Haleem, Arabic/English | 1,095 | 900–1,700 | 0.99–1.86M |
| English Tawbah | 110 | 600–1,000 | 0.07–0.11M |
| Iṣlāḥī, all nine Urdu volumes | 5,821 | 1,000–2,000 | 5.82–11.64M |
| Tarama, often two printed pages per PDF page | 2,839 | 900–1,800 | 2.56–5.11M |

Output density ranges are estimates based on the observed language/layout classes, not exact tokenizer counts or a claim that the corrupt local OCR captured all text. The paired pilot must replace these assumptions with measured visible and reasoning output, separately.

For scale only, standard API rates are **$0.10/M input and $0.50/M output**. The direct-call scenario is roughly **$15–23 before reasoning, retries and review**; the native-agent scenario is roughly **$35–45 if all input were uncached**, also before those additions. Every extra 1,000 reasoning tokens/page adds about **$6.01** at that output rate. Cached input, cache writes, batch pricing and subscription usage are separate: these API equivalents are **not a quote for the user's Codex subscription**. [Current Luna pricing](https://developers.openai.com/api/docs/models/gpt-6-luna)

## Proposed paired pilot

Use **24 identical pages at low and medium: 48 page transcriptions**. Cover both Bint al-Shāṭiʾ volumes, al-Khūlī, ʿAbduh, Muqātil, Ibn Khālawayh, Farāhī, Badawi–Haleem, English Tawbah, Urdu volumes 1/2/6/9 and three Tarama volumes. Include short pages, dense body pages, notes and mixed scripts. At four pages per fresh agent this is twelve narrowly scoped agents. Proportional planning input is roughly 1.2–1.4M tokens plus any pilot-specific overhead; visible output roughly 45–90k, with reasoning measured separately.

Give each agent only its page images, page identities and a transcription brief. Use no parent history and no source-text lookup. Do not show one effort's transcript to the other. Scripts handle rendering, paths, page counts, checksums, output validation and resumability. The agent's task is only to read the assigned images and save the transcription.

Measure omitted/added lines, wrong words and negations, verse/page/citation numbers, footnote placement, reading order, orthographic changes and harakāt. Compare with image-checked reference passages; agreement between two model outputs is not proof. Report quality by language and work, so good English cannot hide bad Urdu. Require all page regions accounted for and no invented reconstruction. Use `[?]` only for genuinely unreadable stretches, with coordinates/review notes, not to conceal a failed OCR pass.

Choose low only for source classes where it passes the checks; pay for medium only where it measurably improves them. If both fail a source class, escalate that class to another engine or review. Neither effort setting alone establishes near-zero data loss. **The proposed pilot has now run; its results are linked above. Production transcription remains pending.**
