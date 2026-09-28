# v14 — Turkish ayah commentary from a frozen synthesis handover

Write the finished commentary for a curious Turkish reader with almost no Arabic. Their Arabic loanwords have
narrowed or shifted. Anchor the reader in what the ayah says, then make its supported surprises intelligible.
The reader should be able to explain the connections and reread the ayah with a changed understanding.

## Use each input for its particular job

- `ayah.md`: the focus text, anchor translation, morphology and word notes. Notes are prior proposals; they do not
  select the only reading. Use grammar when it changes what the reader can hear.
- `window_text.md`: the actual surrounding Quranic text. Ground the ayah in the movement before and after it;
  do not rely on an image plan as a substitute for reading the local scene.
- `synthesis.md`: findings, QeQ annotations, additional QeQ findings and axis readings, relevant images and meetings.
  F/Q/A are source records; E_F is the QeQ annotation of that F; I is an image; I_M is a meeting of images.
  Navigation groups overlap and are not an outline. Every source record occurs once. A touch/meet entry singles
  out this ayah's member. Develop/assemble entries retain wider membership. Related source records supply the
  attested branch, trigger and concrete connection.
- `dictionary.md`: the complete focus-root branches, for the concept and what Turkish loses. `branches.md`: other
  cited branches, for cross-word connections and exact quotations. A first classical phrase is an excerpt, not the
  whole entry. Do not pretend an absent quotation was supplied.
- `concordance.md`: evidence for counts and recurring uses. State the scope correctly: root, lemma, form and stop-
  lemma exclusions differ. Frequent roots have counts only; do not claim a complete contextual survey from them.
  Do not copy a conflicting count from another record.
- `passages.md`: exact complete ayat for the supplied QeQ leads, concordance uses and local window. Use these
  to check the proposed connection and to copy Quranic quotations. This file has the same spelling as the verifier;
  remembered quotations inside analysis records or previous prose are not the quotation authority. Complete ayat
  are not a complete surrounding narrative. Do not invent missing context or claim it was retrieved.
- If `source_access.md` is supplied instead, use its lookup command before developing cross-references. Retrieve
  the cited ayat and enough adjacent context to understand them, then copy their exact Arabic when quoting.
- `variants.md`: supplied alternative readings. Explain a variant when it changes a consequential reading; phonetic
  differences alone need no tour. Do not invent a variant from memory.
- `previous.md`: the immediately preceding commentary as actually written, if available. Build on its delivered
  explanations and avoid retelling them. More distant, unsupplied prose cannot be assumed to have explained anything.
  The network's disclosure plan is an intention, not evidence of delivery.

## Compose explanations

First understand the plain sense and how the ayah follows its neighbours. Then choose a connected movement of
thought. Several findings, image members, meetings and Quranic passages can do one explanatory job. Group them
around that job. Do not translate the records one by one or write a paragraph for every ID.

Build an argument the reader can follow across the whole commentary. Use a few short, meaningful headings at its
real turning points. A heading identifies what is being understood, not a root or a list of images. Each section
should develop a question raised by the ayah or the preceding explanation; paragraphs should carry consequences
forward. Do not finish one isolated image and start another merely because it is next in the evidence index.

For each substantial reading, show the word and attested sense, activating detail, how the details work together,
and what this makes perceptible in the plain reading. Sustain the physical mechanism, place, action or relationship
until its consequence becomes visible. A thematic label alone does not explain it. An image meeting needs the
relationship between its images and what that relationship shows, rather than adjacent descriptions.

Space follows this payoff. There is no item cap and no word target. Compress repeated definitions, quotations and
parallel examples; retain the inferential bridge that lets a new reader follow. A small contribution can be one
clause inside a larger explanation. A dictionary sense of a related noun is not the translation of this verb.

Every image touching the ayah needs a meaningful local contribution or an explicit deferral. Follow meet, touch,
develop, assemble as depth and continuity guidance. Assembly shows members acting together; it does not require
reciting a list of every member. If several images form one mechanism, explain them together.
The plan's role is guidance for progressive disclosure, not a ban on explaining how this ayah's working part
actually works. Look for further supported relationships among the supplied branches and image meetings. Carry a
surprising connection through its physical or relational consequence instead of stopping at its label. A new
bridge must use an attested sense, a visible activating detail and a consequence for this ayah's primary reading.

Preserve Turkish lexical losses, grammar that matters, local resonance, loaded-word patterns and independent QeQ
axes as well as images. A finding outside an image remains eligible for full treatment. Bold or partial findings
are not weakened merely because they are unusual. Readings coexist and keep the primary reading intact.

QeQ passages serve explanations. Staging and same-word describe evidence; neither requires every passage to be
quoted or demotes it. A definition, construction, scene or consequence may be indispensable under either tag or
no tag. Use enough evidence to do the job; distinguish an unused finding from an unused parallel citation.
Support, expansion and shifts remain beside the latent reading; absent staging is not counter-evidence. Explain
actual contradictions and retain their evidence even if the associated reading is deferred.

Distinguish a repeated example from a distinct explanation inside the same source record. A record may combine
a traveller scene, a different application of a word, and a limiting case. Discussing one does not deliver the
others. Preserve consequential differences, or name the omitted component in the separate partial-use notes.
Do not add citations just to consume the reference list. Explain why a passage changes the reading wherever it
does work; similar parallels can share one explanation. Previous prose can carry a relationship already delivered,
but an intended network role cannot stand in for prose the reader has actually seen.

Natural, precise Turkish. No bullet inventories, numbered root tours, internal
IDs or workflow language in reader prose. Explain terminology on first use. End by rereading the ayah through
the developed connections. Avoid defensive paragraph endings and automatic qualifications.

## Checkable Arabic

Every Arabic quotation uses exactly `{ar:ARABIC, tr:transliteration, gloss:Türkçe karşılık, source:SOURCE}`.
SOURCE is a single Quranic ref or a spaced Arabic root plus branch ID. Several sources may be comma-separated.
Use exact Quranic Arabic and copy dictionary Arabic from supplied branch lines. No commas inside ar/tr, no colon
inside gloss, no other fields or curly braces in prose. Transliteration and gloss must not turn a resonance into
a claim about the contextual translation. Quote long passages in parts. Sources are checked.

Anchor the lexical hinges of the explanation, not just the opening ayah. When a paragraph depends on a word's
unfamiliar sense, a cross-root definition, or the wording of a Quranic construction, show the short exact phrase
doing that work in a source-bearing tag and explain it in Turkish. A bare reference cannot show a reader which
word carries the inference. Tags are local to the paragraph where the Arabic does interpretive work; an earlier
tag does not anchor a later new inference. Quote only the needed words, not a whole passage for every parallel.
For narrative context that adds no wording-dependent claim, a clear Turkish account with its reference can suffice.
There is no tag quota. Use readable Turkish transliteration (ş, ç, c, ğ, â, î, û as appropriate); avoid scholarly
letter symbols that this reader cannot sound out. Exact tags establish the wording, not the truth of an inference.

## Keep a compact trace after the prose

After the commentary, write `===== SYNTHESIS =====` on a line, then one JSON object (no code fence):

    {
      "schema": 3,
      "links": [
        {"items": ["F1", "I1"], "at": ["A short exact anchor identifying the paragraph"]}
      ],
      "partial": [
        {"items": ["E_F1"], "at": ["A short exact anchor locating the part actually used"],
         "remaining": "The distinct component left unexplained", "destination": "surah commentary"}
      ],
      "deferred": [
        {"items": ["F2"], "destination": "surah commentary", "reason": "The specific reason for deferral"},
        {"items": "remaining", "destination": "surah commentary review",
         "reason": "Explain why the remaining material was not developed here"}
      ]
    }

Use actual input IDs; the example supplies format only. Each ID occurs once across links, partial and deferred.
A link locates relevant prose for independent review; it does not rate its quality or certify completeness. Do not
write quality levels, self-evaluations or payoff summaries. The explanation belongs in the commentary.

Group related IDs at the same prose locations. Supply one to three exact anchors per row, each 20–120 characters
and found in only one prose paragraph. Use the shortest identifying span; the script retrieves the full paragraph.
Give additional anchors only where the explanation needs several paragraphs. Never copy whole paragraphs here.

Use partial when a multi-part record contributes one component while another consequential component remains
unexplained. Name that omitted component and where it should be reconsidered; its mere passage number is not an
explanation of what is missing. An image's distant members intentionally reserved for later ayat need not all be
repeated here. Judge partial use against this ayah's explanatory contribution. Omitted parallel citations that add
no distinct explanation are recorded automatically and need no model-written list.

Deferrals preserve wholly unused records, including real counter-evidence. Give specific reasons for significant
deferrals; remaining collects residual items, not unacknowledged omissions inside linked records. Keep each reason
or remaining note 10–240 characters. These are metadata limits, never prose limits. The entire source inventory
is retained, and the review may reject a fluent commentary even when every ID has a valid location.
