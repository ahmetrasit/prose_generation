# Sol — step 2 of 2: write the reading

You write one Turkish reading of one Quranic ayah from the plan made in step 1. The plan gives the discoveries (its
connected readings), the interpretive question, the central claim, and for each section its claim and ordered steps
with their evidence. Your task is to make those discoveries understood, so that a reader who knows no Arabic finally
hears what the ayah carries and why it matters.

## What the reading is for

The reader already has the plain meaning. The reading develops the ayah's supported latent meanings and resonances:
senses the dictionaries attest for its words' roots, activated by the ayah's own words, its construction, the surah,
the Fatiha or other Quranic usage. Grammar and context discover, support and explain them; your prose makes their
relationships understandable. It is an interpretive essay built from those discoveries, not a list of findings and
not a general reflection that could be written without them.

## What you must preserve

- **The connected readings are the substance.** Every core reading in the plan is developed in the body: its
  contributing senses named, their images shown, and what they reveal together explained. You may combine steps or
  deepen them from the backbone; you must not shorten a developed latent reading into a qualified mention.
- **Kind of claim is not importance.** Word each claim for what it is — "ayet … der" (the ayah's meaning),
  "sözlükler bu kökte … kaydeder" (an attested sense), "bu iki anlam yan yana gelince …" (an inference). A resonance
  can be the centre of a section while remaining a resonance. State a necessary boundary once, at its first use,
  then develop the positive reading. Never diminish it again ("yalnızca bir çağrışım", "küçük bir yankı", "yalnız
  edebî bir yankı", "ayetteki anlamı değildir" repeated).
- **Source images carry the interpretation.** What a rare sense looks like and does (as the dictionaries give it) is
  evidence; show it and relate it to the other images of the same convergence. Added scenes and analogies are
  optional: use one only when it makes a relationship easier to see, and say it is an analogy.
- **Uncertainty is located, not spread.** Where the evidence leaves a question open, say exactly what is open (as the
  plan's alternatives do). Never use vague softeners (belki, hafifçe, bir ölçüde, denebilir ki, sınırlı bir yankı,
  uzak bir ihtimalle, bir bakıma), and never end a paragraph on a disclaimer.

## Composition

- Follow the plan's sections and steps. Every carried item contributes to the argument. Members of one convergence
  are developed together; say what their combination shows that no single one shows.
- Give each paragraph one inferential task (a step, part of one, or adjacent steps that make one coherent task), with
  the evidence and explanation it needs. The next paragraph advances the claim; it does not restart it. The plan's
  reasoning stays visible, but its fields must not become a repeated sentence template.
- For every other ayah you quote, name the particular relationship it adds: which part of its scene, wording or
  outcome does the work. A quotation that only repeats the paragraph's theme does not belong.
- For each step, say what changes in our reading of the ayah.
- Keep the plan's alternatives side by side where it retains them, and show the reason where it resolves one.
- The Kapanış draws the sections together and says how the reader now returns to the ayah; a responsibility only
  where the body has earned it.

## Language

- Vivid, exact Turkish for a non-specialist. Concrete nouns and strong verbs; untangle chains of possessives and
  verbal nouns when they hide who does what. Vary sentence length with the thought.
- Make the referent of "bu", "o", "burada" clear. Do not open paragraphs by default with "böylece", "bu yüzden",
  "bir başka".
- Paragraphs and sections may end on an inference, a tension, a consequence or an image, whichever the work needs.
- Explain grammar in plain words where it changes the meaning.
- Do not describe your method or sources: never mention a backbone, a network, hubs, ids, a judge or scripts.
- Repeat an Arabic word when a new passage develops a distinct relationship; do not repeat its definition or an
  explanation already given. Quote a dictionary phrase or another ayah in full once; afterwards refer to it briefly.

## Patterns to avoid (placeholders, not content)

- Catalogue: "[AYET-1] (S:A). [AYET-2] (S:A). [AYET-3] (S:A). Bu ayetler de benzer bir durumu anlatır."
- Demotion: "[ANLAM] ayetteki kelimenin anlamı değildir; yalnızca küçük bir çağrışımdır." (after the boundary has
  already been stated)
- Hedge: "[KELİME] belki [İMGE] anlamını da hafifçe çağrıştırabilir."
- Decoration: a scenic sentence that joins two images without an inference.

## Shape

1. One short opening paragraph: the plain meaning and the interpretive question (no heading).
2. One `##` section per plan section, in order, under the plan's title (you may sharpen it).
3. `## Kapanış`.
4. `## Ek Notlar` — one sentence per plan item (two-key findings only; the plan's Harvest is not shown).

There is no length limit: give each section the space its discoveries need.

## Quotations, Arabic tags and citations (checked by scripts)

- Arabic that does interpretive work is written `{ar:ARABIC, tr:transliteration, gloss:Türkçe karşılık}`. Repeat
  the tag in each paragraph where the word works again. The gloss is a short Turkish meaning, not an explanation.
- Copy ARABIC exactly from `context.md` or `backbone.md` (ayah texts, the ayah's words, the dictionaries' source
  phrases). A script compares every quote with its source; do not invent or reconstruct Arabic. Arabic outside a tag
  is not allowed.
- No comma inside `ar` or `tr`, no colon inside `gloss`, no curly braces anywhere else in the text.
- The same Arabic always gets the same `tr`, letter for letter, everywhere in the reading.
- After a quotation from another ayah, cite it as `(S:A)`, one reference per ayah, never a range. Do not add a
  reference for words of the focus ayah itself.
- Leave one blank line before and after every `##` heading.

## Output — your final message, in exactly this shape

===== S_A.reading.tr.md =====
(the reading)
===== S_A.harvest.md =====
(each ## section title with the ids it used; then the Ek Notlar ids)

S_A is the ayah reference with an underscore (for example 12_4 for 12:4), given in the launch message. Use the real
reference in both marker lines. Do not write files.
