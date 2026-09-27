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

Preserve Turkish lexical losses, grammar that matters, local resonance, loaded-word patterns and independent QeQ
axes as well as images. A finding outside an image remains eligible for full treatment. Bold or partial findings
are not weakened merely because they are unusual. Readings coexist and keep the primary reading intact.

QeQ passages serve explanations. Staging and same-word describe evidence; neither requires every passage to be
quoted or demotes it. A definition, construction, scene or consequence may be indispensable under either tag or
no tag. Use enough evidence to do the job; distinguish an unused finding from an unused parallel citation.
Support, expansion and shifts remain beside the latent reading; absent staging is not counter-evidence. Explain
actual contradictions and retain their evidence even if the associated reading is deferred.

Natural, precise Turkish. Headings may follow the argument. No bullet inventories, numbered root tours, internal
IDs or workflow language in reader prose. Explain terminology on first use. End by rereading the ayah through
the developed connections. Avoid defensive paragraph endings and automatic qualifications.

## Checkable Arabic

Every Arabic quotation uses exactly `{ar:ARABIC, tr:transliteration, gloss:Türkçe karşılık, source:SOURCE}`.
SOURCE is a single Quranic ref or a spaced Arabic root plus branch ID. Several sources may be comma-separated.
Use exact Quranic Arabic and copy dictionary Arabic from supplied branch lines. No commas inside ar/tr, no colon
inside gloss, no other fields or curly braces in prose. Transliteration and gloss must not turn a resonance into
a claim about the contextual translation. Quote long passages in parts. Sources are checked.

## Separate prose from its account

After the commentary, write `===== SYNTHESIS =====` on a line, then one JSON object (no code fence):

    {
      "schema": 2,
      "bundles": [
        {"id": "B1", "items": ["F1", "E_F1", "I1"], "level": "connected",
         "evidence": ["A short exact anchor identifying the explanatory paragraph"],
         "payoff": "One short sentence naming the explanatory relationship"}
      ],
      "deferred": [
        {"items": ["F2"], "destination": "surah commentary", "reason": "The specific reason for deferral"},
        {"items": "remaining", "destination": "surah commentary review",
         "reason": "Explain why the remaining material was not developed here"}
      ]
    }

Use actual input IDs; the example specifies format only. Each item gets one disposition. Supply one to three exact
anchors per bundle, each 20–240 characters and occurring in only one prose paragraph. A script retrieves those
full paragraphs for review. Do not repeat entire paragraphs in this account. Keep each payoff within 240 characters;
the explanation belongs in the prose. These metadata limits do not limit the length or scope of the commentary.

A bundle may join many items but claims only what its identified paragraphs support. If its explanation spans
several paragraphs, give an anchor for each relevant part. Do not mark a QeQ annotation as connected solely because
its parent finding was discussed; its explanatory contribution must also be present. Levels: mentioned names a detail; explained gives its origin
and consequence; connected explains how details work together and change the reading. These are claims for
independent review, not a quality score. Do not claim an entire image is connected because one member appears.
Give separate reasons for significant deferrals; remaining accounts for residual fragments without forcing a long
bookkeeping output. Every deferred, merely mentioned or unreported item and unused passage candidate is preserved
by script. No omitted finding disappears, and inclusion alone does not mean success.
