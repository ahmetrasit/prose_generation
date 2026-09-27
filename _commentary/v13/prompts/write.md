# v13 step 3 — the ayah commentary (Turkish)

Write the finished Turkish commentary of the focus Quranic ayah. The reader is a curious Turkish speaker who knows
neither Arabic nor how lexical families and associations work, and whose theological loanwords (oku, ibadet, âlem,
din, nimet, hidayet …) have narrowed in Turkish. The familiar meaning is easy to find elsewhere; it is the anchor.
Let the reader hear what the ayah makes possible to hear, understand the ayah better afterwards, and never be
disoriented. This is an independent interpretation, not a catalogue, a translation with footnotes, or a report on an
analysis.

## The evidence

- **ayah.md**: the ayah, its words, the anchor translation, word notes.
- **findings** (`F<n>`): the latent readings found in the ayah, its window and its surah: local resonances, the ayah's
  part in the surah's images, Quran-loaded words, cross-definitions, concepts, and what Turkish loses.
- **qeq** : what the rest of the Quran does to each finding (supports, expands, shifts, contradicts), new findings
  (`Q<n>`) from the passages' own words, and the axis pass (`A<n>`: passages for the plain sense and grammar). It gives
  references only: quote the Quran's Arabic yourself, exactly, where a passage does its work (every quotation is
  checked against the canonical text).
- **network** (when present): the surah's images (`I<n>`), their members, how they interact, and a disclosure plan
  (where the reader first meets each image, where it develops, where it is assembled).
- **mustland.md** (made by script from the network and the QeQ tags): what this ayah must carry: each image with a
  member here and this ayah's role in it (for an image assembled here, all its members from every ayah), the meetings
  of images located at this ayah's words, and the QeQ passages tagged `staging` or `same-word`.
- **dictionary.md**: every branch of the focus roots (gloss | image | definition | first phrase), for what Turkish
  loses; **branches.md**: the dictionary lines of every other branch the findings cite. Quote dictionary Arabic only
  from these two.

The records are evidence, not an outline and not an obligation list.

## What the commentary carries

- **Ground**: what the ayah says in its plain sense, and what it receives from the ayah before and hands to the next.
- **What Turkish loses**: once, where the word first carries weight, what the key Turkish word loses or adds against
  the Arabic concept; grammar the reader cannot hear in Turkish only when a reading rests on it, explained here once.
- **The latent readings**: the local resonances of the ayah and its surah, developed into connected readings.
- **The surah's images through this ayah's words**: follow the disclosure plan. Where the reader first meets an image,
  let them sense it through this word; where it develops, add what this word brings; where it is assembled, let them
  see the whole picture. Do not retell an image the reader has already met in full; build on it.
- **Quran-loaded words**: where the Quran uses a word with one recurring role, show the pattern and what it does to
  this ayah, including where the familiar translation departs from it.
- **The Quran explaining it**: let other ayat supply the stages, contrasts and consequences that support, expand or
  shift a reading, where they do real work. A finding the Quran contradicts is not hidden: say plainly what the
  passage says and how the reading stands with it. A canonical reading of another passage never silences a latent
  one.

## What must land

Every item in mustland.md lands in the prose: `touch` in at least a sentence through this ayah's word; `develop` as a
real step; `assemble` as the whole image with every member, shown as one scene (not a sentence that names it); a
meeting as the crossing and what it shows; a tagged passage where it does its work. An item you cannot land honestly
is held, with the reason, in the coverage block (below); it goes on to the surah commentary.

## How to choose and write

- Space follows payoff: what does a reading make perceptible in the plain reading that a paraphrase could not (more
  spatial, bodily, causal, relational, material, temporal, compositional)? A reading with a small payoff can stay a
  sentence; nothing is weakened for being bold.
- Integration, not aggregation: let one reading explain another; several branches of one root are often facets of one
  concept. Readings coexist; nothing is ranked or declared correct, and every latent reading keeps the plain reading
  intact (never "not X but Y").
- First understand the ayah in its immediate grammar and scene; then develop the consequential resonances. Let a
  concrete detail make the next detail necessary: what changes, through what operation, with what consequence? Sustain
  an image's material specificity long enough for its consequence to become visible; do not flatten a physical
  mechanism, place or action into a generic label (care, connection, life, direction) before explaining its work.
- Show the non-Arabic reader where an image comes from: introduce the word, explain the attested sense or form, show
  its connection to another detail, then draw the reading. A dictionary sense of a related noun does not become the
  translation of this verb. A sense marked `memory` is not stated as the dictionary's.
- Natural, precise Turkish. Follow a question, image or developing insight, not the records' order. Headings only when
  they help the reader follow a real movement. No bullet lists and no numbered tours of a root's senses: state the
  concept, then only the facets that serve a reading. End by rereading the ayah, not by relisting.
- What QeQ adds (a "shifts", "expands" or "none") stands beside the latent reading in a clause at most; it never turns
  the reading into "only an echo" and never reverses it.
- Counts of uses come only from the concordance; any other count or grammar claim from memory is marked as such. Do
  not say an image "has been followed since the start of the surah" unless mustland.md shows earlier ayat carry it. No defensive disclaimers at the end of paragraphs; state a real
  qualification where the reader needs it. Internal labels (F/Q/I ids, branch ids), file names, confidence and
  workflow language do not belong in the prose.

## Arabic tags (checked by scripts)

Every tag has exactly four fields in this order: `{ar:ARABIC, tr:transliteration, gloss:Türkçe karşılık, source:…}`.
`source` is the ayah the Arabic is quoted from (`source:24:35`), or the dictionary branch it is copied from, as the root
in Arabic letters with spaces and the branch id (`source:ن و ر B005`); several items comma-separated. The Arabic must
occur in the declared source (Quran text exactly; dictionary Arabic copied from that branch's line in branches.md).
Cite Quran passages with exact refs, e.g. (2:255, 3:18), never ranges. Tags are normal prose, never inside backticks.
No comma inside `ar` or `tr`, no colon inside `gloss`, no other fields, no curly braces elsewhere. Quote a long ayah in
part. The same Arabic always gets the same `tr`. Transliteration and gloss explain what is discussed; they must not
quietly translate a lexical resonance as the word's contextual meaning.

Before returning, read as someone meeting these relations for the first time: can they restate what the ayah says,
explain how the main images work together, and reread the ayah with a changed understanding? Remove inventories,
unsupported bridges, repeated qualifications.

Return the Turkish commentary, then a line `===== COVERAGE =====`, then one line per mustland item:
`M<n> | landed ¶<paragraph number> | held: <reason>` (use one of the two).
