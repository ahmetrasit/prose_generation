# Isolated page transcription brief

Transcribe all four assigned page images directly. This is an OCR experiment, not commentary, translation, summarization or text restoration. The assignment JSON gives exact input images and output paths. The page number is the **PDF page**, not the printed page label.

Read only this brief, your assignment JSON and its four images. Do not read the original PDF, existing OCR, reference books, other agents' files or other repository content. Do not browse, invoke other models, spawn agents or run OCR software. Use `view_image` with `detail: "original"` on the supplied PNGs; you may view the same image again if needed. Batch independent image views in a single tool round when practical. Images must actually be viewed before transcription. No further cropping or resizing during this controlled comparison.

For each image, write a UTF-8 `.txt` at its assigned output path:

- Transcribe every visible textual region, including headers and printed page labels. Preserve the original language, spelling, punctuation, Arabic harakat and Latin transliteration marks. Arabic/Urdu text must be in logical reading order, never reversed visually.
- Follow the printed reading order. For page spreads, finish each printed page in its language's reading order. Place its footnotes after its body. Preserve dictionary entry boundaries and distinct columns. Use paragraphs/newlines rather than Markdown tables.
- Do not modernize, translate, silently correct, complete from memory or replace a printed Qur'anic quotation with a remembered canonical version. Copy what the image shows, including printed errors.
- Write `[?]` for genuinely unreadable stretches; never invent words. Mark only the unreadable span, not a readable whole paragraph. Do not use `[?]` as a substitute for completing a difficult page.
- If a page is actually blank, write an empty file and set `verified_blank` to true. A failed or incomplete transcription is not a blank page.
- The text file must contain only the transcription, without a preface, code fences or analysis.

Also write the assigned `.review.json` with `page_id`, `verified_blank`, `complete` (whether all regions were attempted), `uncertainties` (short descriptions and approximate region positions, not invented confidence scores), and `layout` (observed reading order). Record omissions or unresolved regions honestly. This is a draft, not an accepted corpus page.

Use one output write operation for the batch when practical. Do not reread the saved text merely to produce a final answer. Finish with the four page IDs and any unresolved regions; do not repeat the transcriptions in your final response. Other agents share the workspace: write only your eight assigned files.
