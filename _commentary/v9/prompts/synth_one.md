# V9 synthesis — discover across the lines, plan, and write the reading (one session)

You write one Turkish reading of one Quranic ayah. Several narrow discovery passes have already examined the ayah's
evidence; their results are in `package.md`. Your task is the part none of them could do: **find what becomes
understandable only when these findings are read together**, develop those relationships, then build and write the
reading. You do this in one session: first the connected readings and the plan, then the reading.

## What the reading is for

The reader already has the plain meaning (the anchor translation). The reading develops the ayah's supported
**latent meanings and resonances** — senses the dictionaries attest for its words' roots, how the Quran uses those
words elsewhere, how the ayah is built, how it joins its surah and related ayat, and the Fatiha (recited in every
prayer) — in the spirit of al-Khūlī (a word read through its Quranic usage) and al-Biqāʿī (an ayah read through its
neighbours and its surah), not limited to them. Success needs both interpretive richness and a readable argument that
develops it. A reading whose main argument would stand unchanged without the latent and intertextual material has
failed, however well written.

These are established methods of Quranic interpretation, applied here more systematically than a single reader can:
al-Biqāʿī's *naẓm* (Naẓm al-durar reads each ayah through its neighbours and its surah) and al-Khūlī's literary
exegesis (a word read through all its Quranic uses and its root's attested senses). A reading built this way is
legitimate interpretation within that tradition, and surprising results are what the methods exist to find. The
familiar interpretation is one reading among the possible ones, not the measure of the others; do not tone a
supported reading down because it is unusual. Rigour comes from the evidence and from saying exactly what it
establishes, not from caution.

## What you are given (all below; do not open files or run commands)

- `context.md` — the ayah with its words and anchor translation, the Fatiha, the whole surah.
- `package.md` — section 1: the lexical network (ids H, L, F, T, J, G); section 2: four discovery lines — local
  language (L..), Quranic usage (U-..), surah context (S-..), related passages (R-..), and extra findings (….X..):
  readings, **open observations** (a precise link whose decisive support is missing in its own line), notes and
  rejected misreadings; section 3: the text of cited ayat. `support` and `relevance` are separate judgments by the
  discovery passes; they rank, they do not decide. You decide each finding's contribution to the whole reading.

## Principles

- **Two keys.** A latent reading needs a sense or usage the sources attest and a specific feature of the ayah or its
  context that activates it. An open observation becomes a reading when another line supplies its missing key —
  look for that.
- **Kind of claim is not importance.** Contextual meaning, attested association and literary inference are different
  kinds of claim, not a ranking. A resonance can be the centre of a section while remaining a resonance. State a
  necessary boundary once, at its first use, then develop the positive reading.
- **Source images are evidence.** The images the dictionaries and the cited scenes give can carry the interpretation;
  develop their relationships. Added analogies are optional aids.
- **Convergence is the discovery.** When findings from different lines meet on one word, image or scene, what they
  show together is the finding; mentioning one of them does not develop it.
- **Usage patterns are judged, not counted.** Several occurrences in one episode are one context; different forms stay
  distinct; a pattern colours this occurrence only where something here activates it.
- **Earlier labels and scores are hints.** Do not exclude a supported link because it is unusual or was scored low in
  its own line; do not include one only because it scored high.

## Steps

1. **Read** the ayah, the anchor translation, the whole package and the texts it cites.
2. **Connected readings** — before any central claim. Find the relationships across lines (network ↔ usage ↔ surah
   ↔ related passages ↔ Fatiha) and within them. For each connected reading: what it reads, its members (ids), both
   keys, what the members reveal together that no single one shows, core or peripheral, and exclusions with specific
   reasons. Include open observations you complete, and say what completed them.
3. **Tensions** — oppositions inside the ayah, constructions it leaves open, gaps between the ayah and its context, and
   tensions the connected readings create (as many as the ayah has; it may be a sequence rather than a conflict).
4. **Question and central claim** — the claim must accommodate the core connected readings; revise it if it sidelines
   them.
5. **Sections** (3–8), chosen by contribution: each with a claim, the connected readings it develops, 2–6 ordered
   steps (observation → relationship → inference → consequence, with ids and the detail of each that does the work),
   what it adds beyond earlier sections, and alternatives kept or resolved.
6. **Write the reading** from that plan (next section).
7. **Check before returning:** which connected readings are developed in the body; did any core reading become a
   mention, a disclaimer or a note; would the argument stand without the latent and intertextual material?

## Writing the reading

- One short opening paragraph with the plain meaning and the interpretive question (no heading); one `##` section per
  planned section; `## Kapanış` (what the sections establish together, and how the reader now returns to the ayah —
  a responsibility only where the body has earned it); `## Ek Notlar` (two-key findings that are peripheral, one
  sentence each).
- Each paragraph does one inferential task (a step, part of one, or adjacent steps that form one); the next paragraph
  advances the claim. Members of one connected reading are developed together: say what their combination shows.
- For every other ayah you quote, name what in its scene, wording, speakers or outcome does the work. A quotation that
  only repeats the paragraph's theme does not belong; several passages are welcome when each adds a distinct step.
- Word each claim for what it is: "ayet … der" (the ayah), "sözlükler bu kökte … kaydeder" (an attested sense), "Kur'an
  bu kelimeyi … kullanır" (usage), "bu iki bulgu yan yana gelince …" (inference). Locate uncertainty exactly; never use
  vague softeners (belki, hafifçe, bir ölçüde, denebilir ki, sınırlı bir yankı, uzak bir ihtimalle, bir bakıma), and
  never end a paragraph on a disclaimer.
- Vivid, exact Turkish for a non-specialist: concrete nouns and strong verbs; untangle possessive and verbal-noun
  chains; clear referents for "bu", "o", "burada"; varied sentence length; no default connectors ("böylece", "bu
  yüzden", "bir başka") at every paragraph start. Paragraphs may end on an inference, a tension, a consequence or an
  image. Do not mention your method or sources (no package, lines, ids, judges or scripts).
- There is no length limit: give each section the space its discoveries need.

## Arabic tags and citations (checked by scripts)

- Arabic doing interpretive work: `{ar:ARABIC, tr:transliteration, gloss:Türkçe karşılık}`; repeat the tag in each
  paragraph where the word works again. The gloss is a short meaning, not an explanation.
- Copy ARABIC exactly from `context.md` or `package.md` (ayah texts, the ayah's words, dictionary source phrases,
  quoted excerpts). A script checks every quote; Arabic outside a tag is not allowed.
- No comma inside `ar` or `tr`, no colon inside `gloss`, no curly braces elsewhere. The same Arabic always gets the
  same `tr`. After a quotation from another ayah cite `(S:A)`, one reference per ayah, never a range; no reference for
  words of the focus ayah itself. One blank line before and after every `##` heading.

## Output — your final message, in exactly this shape, nothing before or after

===== S_A.plan.md =====
## Connected readings
### R1: <short name>
reading: <one or two sentences>
members: <ids>
keys: <attested sense or usage; activating feature>
together: <what they reveal together>
weight: core
excluded: <id: reason; or none>

## Tensions
- <one sentence>

## Question and central claim
question: <one sentence>
claim: <one or two sentences>

## Section 1: <title>
claim: <one sentence>
develops: R1, R3
steps:
- 1. <observation → relationship → inference → consequence> [ids]
adds: <one sentence>
alternatives: <retained / resolved / excluded, with reasons>
===== S_A.reading.tr.md =====
(the reading)
===== S_A.harvest.md =====
(each ## section title with the ids it used; the Ek Notlar ids; ids set aside, each with a reason)

S_A is the ayah reference with an underscore (for example 12_4 for 12:4), given in the launch message; use the real
reference in all three marker lines. Do not write files.
