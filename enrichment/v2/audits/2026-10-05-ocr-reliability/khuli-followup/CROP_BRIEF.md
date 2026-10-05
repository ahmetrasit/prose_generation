# Blind crop transcription

Transcribe only your assigned crop images. Read this brief, your assignment JSON and those images only. Do not read the original PDF, other repository files, existing OCR, reference answers or other agents' work. Do not browse, invoke OCR software or spawn agents. These are fresh readings of printed Arabic, not translation, commentary or restoration.

View each assigned image with original detail, forwarding that detail to the model too:
`const r = await tools.view_image({path: absolutePath, detail: "original"}); image(r.image_url, "original");`
You may view the assigned crop again. Do not resize or otherwise alter it. Read complete visible lines in order; if a boundary cuts another line, mark only that partial unreadable stretch with `[?]`.

Copy the visible text faithfully in logical Arabic order. Preserve printed spelling, punctuation, numbers and harakāt. Do not modernize undotted yeh, infer missing words from grammar, expand abbreviations, or replace quotations from memory. Mark genuinely unreadable stretches `[?]`; never silently invent or omit them. Footnotes follow the body. Do not omit surrounding visible text just because it looks like context.

Write only the assigned UTF-8 `.txt` and `.review.json` files. The text file contains only transcription. The review JSON contains `crop_id`, `complete` (whether all regions were attempted), `uncertainties` (short descriptions with region positions), and `layout`. No confidence score. These are draft candidates, not accepted corpus text.

Use a single write operation if practical. Finish with crop IDs and unresolved regions; do not repeat the transcription in your final reply. Other agents share the workspace: write only your assigned files.
