# Comprehensive Qur'an Commentary Annotation Protocol

## Purpose

This document is the canonical instruction set for generating a **single comprehensive Markdown source** for a Qur'anic surah or ayah while preserving a readable prose commentary and storing additional evidence in machine-filterable `{...}` blocks.

The system is designed for an MD reader that can hide/show categories. Therefore the goal is **maximum structured information coverage with minimum redundant repetition**.

The output should let a reader inspect, in one place:

- the base commentary;
- rivāyah tafsir;
- dirāyah tafsir;
- asbāb al-nuzūl;
- hadith;
- qirāʾāt/readings where relevant;
- grammar and balāghah;
- naẓm / surah structure;
- historical and social context;
- semantic and reception history;
- Qur'an-to-Qur'an parallels;
- methodological limits;
- the project's own lexical/network synthesis;
- what appears new relative to a defined classical corpus;
- important alternatives that were considered but rejected or left uncertain.

The output must never blur these epistemic levels.

---

# 1. Fundamental design rule: `type` and `role` are different

Every added block must answer two independent questions:

1. **What kind of information is this?** → `type`
2. **Why is it included here?** → `role`

Example:

```text
{id:"S107-HAD-001", type:hadith, tradition:hadith, ayah:107:6, role:corroboration, relation:thematic, scholar:"Muslim", status:explicit, hadith_grade:sahih, priority:core, audience:general, prose:"...", source:"MUS-2986"}
```

The block is a **hadith** (`type`) whose function is **corroboration** (`role`). It is only **thematically** related to the ayah (`relation`); it is not falsely presented as a direct tafsir report.

---

# 2. Canonical one-line tag syntax

Use one physical line per annotation block:

```text
{id:"...", type:..., tradition:..., ayah:"...", role:..., relation:..., status:..., priority:..., audience:..., prose:"...", source:"..."}
```

## Syntax rules

- Use outer `{}`.
- Use `key:value` pairs separated by commas.
- Machine enum values may be unquoted if they contain only ASCII letters/underscores.
- Human-readable values containing spaces, punctuation, Arabic, semicolons, or multiple names must be double-quoted.
- `prose` must always be double-quoted.
- Escape literal double quotes inside a quoted value if needed.
- Do not use nested JSON objects or arrays inside a block.
- For multiple values in one field, use a pipe-delimited quoted string:
  - `source:"TAB-107|SUY-107"`
  - `checked_sources:"Tabari|IbnKathir|Suyuti|Zamakhshari|Razi|Baydawi|Biqai"`
- Use stable unique IDs. Recommended pattern:
  - `S<surah>-<category>-<NNN>`
  - examples: `S107-ASB-001`, `S107-HAD-003`, `S107-NOV-005`
- For a single ayah task, still use the surah number in the ID.

---

# 3. Controlled vocabulary: `type`

Use these canonical `type` values.

| type | Meaning |
|---|---|
| `tafsir` | Classical or later tafsir explanation tied directly to the ayah |
| `asbab` | Asbāb al-nuzūl / reported occasion of revelation |
| `hadith` | Prophetic hadith relevant to the ayah |
| `qiraat` | Qirāʾah/readings or reported Companion reading |
| `revelation_history` | Makkī/Madanī, chronology, division-of-revelation reports |
| `historical_context` | Social, material, legal, institutional, economic, or cultural context |
| `semantic_history` | How a word/interpretation was understood across periods/sources |
| `nazm` | Surah sequence, ayah adjacency, neighboring-surah relation, structural unity |
| `cross_quran` | Qur'an-to-Qur'an lexical/thematic/structural parallel |
| `method_note` | Methodological control, limitation, or distinction |
| `reader_note` | Short explanation needed by a non-specialist reader |
| `novelty` | Assessment of what is or is not found in the checked tradition |
| `modern_scholarship` | Modern academic or modern tafsir analysis, clearly separated from classical material |
| `source_note` | Source criticism, isnād caveat, textual/source provenance note |

### Optional future types

Only add these if the project actually needs them and the MD reader supports them:

- `fiqh`
- `kalam`
- `balagha`
- `grammar`
- `lexicon`
- `manuscript`

Normally grammar/balāghah/lexicon observations from a mufassir can remain `type:tafsir` and be distinguished by `role` and `relation`.

---

# 4. Controlled vocabulary: `tradition`

| tradition | Use |
|---|---|
| `rivayet` | Report-based tafsir: sahaba, tābiʿūn, transmitted explanations |
| `dirayet` | Analytical tafsir: language, rhetoric, theology, law, reasoning |
| `nazm` | Naẓm / structural tradition, especially Biqāʿī when directly sourced |
| `edebi` | Literary methodology, e.g. al-Khūlī as method rather than direct S107 opinion |
| `hadith` | Hadith layer |
| `historical` | Historical/reception/context layer |
| `project` | This project's own synthesis, reader notes, novelty assessment |
| `none` | When no tradition label is meaningful |

### Important

Do not attribute a direct verse interpretation to al-Khūlī or another methodological thinker unless the source actually contains that interpretation. If applying a method to the current ayah, use:

```text
tradition:edebi
relation:methodological
status:interpretive
```

---

# 5. Controlled vocabulary: `role`

The original four information jobs are expanded into the following roles.

| role | Function |
|---|---|
| `anchor` | Establish the ordinary/received contextual meaning |
| `early_attestation` | Show that an interpretation is attested early |
| `clarification` | Clarify wording, grammar, rhetoric, referent, or semantic distinction |
| `corroboration` | Independently support an interpretation/theme already present |
| `disagreement` | Preserve a genuine interpretive disagreement |
| `semantic_range` | Show multiple live senses of a word/expression |
| `historical_development` | Show how an interpretation changed, narrowed, broadened, or persisted |
| `historical_context` | Explain a social/material practice behind the text or interpretation |
| `asbab_context` | Present a reported occasion of revelation |
| `chronology` | Makkī/Madanī, revelation order, split-revelation discussion |
| `nazm` | Explain sequence, adjacency, surah unity, neighboring-surah relation |
| `constraint` | Prevent an overreading or clarify what the ayah probably does **not** mean |
| `contrast` | Give an opposite/positive/negative counter-scene |
| `interpretive_consequence` | Explain why a linguistic or historical distinction materially matters |
| `project_synthesis` | Explicitly mark a synthesis generated by this project |
| `novelty_assessment` | Compare a project claim to a declared checked source corpus |
| `methodological_note` | Explain admission/rejection criteria or epistemic level |
| `reader_orientation` | Give a concise prerequisite explanation for a non-specialist |
| `source_criticism` | Explain reliability/provenance limits of a report/source |
| `rejected_candidate` | Preserve an important considered but rejected connection |
| `intertext` | Show an especially relevant Qur'an/hadith textual intersection |

Do not create a new role merely because a sentence feels different. Reuse the closest canonical role.

---

# 6. Controlled vocabulary: `relation`

This field prevents a major category error: relevant evidence is not always direct tafsir.

| relation | Meaning |
|---|---|
| `direct_tafsir` | Source explicitly interprets the ayah/phrase |
| `asbab` | Source claims an occasion/circumstance of revelation |
| `direct_hadith_tafsir` | Prophetic report explicitly explains the verse |
| `thematic` | Relevant theme, but not direct verse interpretation |
| `lexical` | Word/root/usage relationship |
| `grammatical` | Syntax/morphology/preposition/reading relationship |
| `structural` | Naẓm, sequence, surah architecture |
| `historical` | Context/reception/history relationship |
| `comparative` | Comparison across sources/readings |
| `methodological` | Method/control rather than substantive verse claim |

### Rule

If a hadith discusses riyāʾ but does not say “this explains Q 107:6,” use:

```text
relation:thematic
```

not `direct_hadith_tafsir`.

---

# 7. Evidence/status fields

## `status`

Allowed values:

- `explicit` — directly stated in the cited source
- `reported` — source transmits the claim/report but truth/historicity is not established
- `disputed` — competing reports or positions exist
- `inferred` — conclusion inferred from evidence rather than stated verbatim
- `interpretive` — project or scholar's interpretive synthesis
- `weak` — only when weakness is actually established by source criticism
- `not_assessed` — reliability not evaluated

## `confidence`

Use only where useful:

- `high`
- `medium`
- `low`

`confidence` describes confidence in the **annotation claim**, not personal certainty about revelation.

## `historicity`

Use for historical/asbāb claims:

- `established`
- `probable`
- `uncertain`
- `contested`
- `not_applicable`

Be conservative. Most competing sabab reports should be `uncertain` or `contested`, not `established`.

## `hadith_grade`

Allowed values:

- `sahih`
- `hasan`
- `daif`
- `mawdu`
- `not_assessed`

Never infer a grade merely because a later tafsir quotes the report. If no independent grading was checked, use `not_assessed`.

---

# 8. Resonance strength: `connection`

Use this field especially for the project's lexical/network analysis.

| connection | Meaning |
|---|---|
| `direct` | Direct contextual/lexical support for the ayah meaning |
| `strong` | Strongly illuminating parallel without being the primary meaning |
| `resonant` | Legitimate secondary resonance; must not replace contextual meaning |
| `speculative` | Possible but weak/insufficiently constrained |
| `rejected` | Considered and rejected |
| `not_applicable` | Field does not apply |

### Example

- `māʿūn = common loaned household objects` → `connection:direct`
- `māʿūn / maʿīn → flowing-water image in S107` → `connection:resonant`
- unsupported root resemblance without semantic/contextual bridge → `connection:speculative` or `rejected`

---

# 9. Novelty field: `classical_attestation`

This is mandatory for `type:novelty`.

Allowed values:

- `explicit` — same connection/claim is explicitly present in checked classical sources
- `partial` — important portion is present, but current synthesis adds material
- `building_blocks_only` — ingredients exist separately; synthesis was not found
- `none_found_in_checked_sources` — no parallel found in the explicitly listed corpus
- `not_checked`
- `not_applicable`

Always include:

```text
checked_sources:"..."
```

### Absolute-negative prohibition

Never write:

> “This does not exist in classical tafsir.”

Write:

> “No explicit parallel was found in the checked sources: ...”

The checked corpus may later expand and change the result.

---

# 10. Display-control fields

## `priority`

- `core` — reader should normally see it when the layer is enabled
- `extended` — useful supporting information
- `research` — audit trail, novelty, qiraat detail, rejected candidates, technical source criticism

## `audience`

- `general`
- `advanced`
- `research`

These fields are independent. Example: a hadith can be `priority:extended` but `audience:general`.

---

# 11. Optional metadata fields

Use only when applicable:

- `scholar:"..."`
- `transmitter:"..."`
- `term:"..."`
- `scope:"..."`
- `source_ref:"..."`
- `canonical:true|false` for qiraat/readings
- `origin:"..."` for a report's earliest traceable source
- `attested_in:"..."` for later repetitions
- `reason:"..."` for rejection or confidence assignment
- `note:"..."`

Do not create empty fields.

---

# 12. Source registry

Every output file must end with a source registry.

Use short stable source IDs in blocks, then define them once at the end:

```markdown
## Kaynak kayıtları

- **TAB-107** — al-Tabari, *Jamiʿ al-bayan*, Q 107. URL...
- **KASH-107** — al-Zamakhshari, *al-Kashshaf*, Q 107. URL...
- **MUS-2986** — Sahih Muslim 2986. URL...
```

### Source principles

1. Prefer primary/classical text over a modern summary when accessible.
2. A later work repeating an earlier report is not a new independent witness.
3. Preserve transmitter/origin when it materially affects interpretation.
4. Do not multiply full blocks merely because five later books repeat the same report.
5. If later sources materially modify, grade, narrow, or expand the report, create separate blocks.

---

# 13. Minimum research corpus

For a comprehensive pass, check the following **when relevant and accessible**.

## A. Qur'an first

- exact ayah context;
- same word/root elsewhere in Qur'an;
- strong phrase-level parallels;
- neighboring ayahs and surah structure;
- neighboring surahs where naẓm is relevant.

## B. Rivāyah tafsir core

At minimum:

- al-Tabari
- Ibn Kathir
- al-Suyuti, *al-Durr al-manthur*

Also inspect earlier/other report collectors if a disagreement matters.

## C. Dirāyah tafsir core

At minimum:

- al-Zamakhshari
- Fakhr al-Din al-Razi
- al-Baydawi

Add al-Qurtubi, Ibn ʿAtiyya, Abu Hayyan, al-Alusi, etc. when they materially contribute.

## D. Naẓm

- al-Biqaʿi, especially for surah purpose, internal sequence, and neighboring-surah relations.

## E. Asbāb al-nuzūl

- al-Wahidi
- al-Suyuti / transmitted asbāb material
- compare multiple attributions rather than selecting one silently.

## F. Hadith

Prefer verified primary collections.

- Sahih al-Bukhari
- Sahih Muslim
- Sunan / Musnad material when relevant

Record grade only when actually verified.

## G. Qirāʾāt/readings

- canonical qirāʾāt where meaning/syntax changes;
- Companion reading reports only if clearly labeled as such.

## H. Lexicon

Use the project's own lexical hierarchy. For this project, Maqāyīs remains primary where specified, with other early lexica used according to the project's established lexical protocol.

## I. Historical/social context

Only include claims supported by identifiable sources. Do not reconstruct premodern society from imagination.

## J. Modern scholarship

Optional. Use only where it adds:

- reception history;
- chronology discussion;
- literary structure;
- historical/linguistic context;
- source criticism.

Always keep it separate from classical attestation.

---

# 14. Required research workflow

## Step 1 — Establish scope

Input may be:

- one ayah;
- ayah range;
- entire surah;
- an existing commentary `.md` to enrich.

Record:

```text
surah_number
ayah_scope
base_file
output_language
```

If a base commentary exists, treat it as authoritative project prose unless instructed otherwise.

## Step 2 — Preserve the base prose

If the task says to keep the prose:

- do not silently rewrite it;
- do not delete project findings because classical tafsir does not contain them;
- add tagged blocks immediately after the most relevant paragraph or argument;
- if the base prose contains a factual error discovered during research, add a `method_note`/`source_note` identifying the conflict rather than silently altering the prose unless explicitly authorized.

## Step 3 — Build a claim map

For every major claim in the prose, classify it as one or more of:

- contextual ayah meaning;
- grammar/rhetoric;
- lexical/root resonance;
- Qur'an-to-Qur'an relation;
- structural/nazm claim;
- historical claim;
- theological/legal implication;
- project synthesis.

This claim map drives source retrieval.

## Step 4 — Build a source/evidence matrix

For each claim, note:

```text
claim
supporting_sources
contradicting_sources
early_attestation
later_development
hadith_relation
historical_context
novelty_status
confidence
```

Do not write the final annotations until disagreements and duplicate reports are visible in this matrix.

## Step 5 — Research historical setting

Check:

- Makkī/Madanī disagreement;
- reported revelation chronology;
- asbāb al-nuzūl;
- named persons/events;
- material/social practices needed to understand the passage.

Keep these distinct. “Makkī/Madanī” is not the same thing as “sabab al-nuzūl.”

## Step 6 — Research hadith

Search for:

1. direct prophetic tafsir of the ayah;
2. hadith using the same key expression;
3. hadith providing a strong positive/negative counter-scene;
4. hadith combining two motifs that the surah combines.

Assign `relation` honestly.

## Step 7 — Research semantic/reception history

For important terms, determine:

- earliest reported senses;
- competing early senses;
- which senses persist in dirāyah works;
- whether later tafsir narrows/broadens the range;
- whether modern translations tend to choose only one branch.

Do not assume a single “traditional meaning” where the tradition is visibly plural.

## Step 8 — Research naẓm

Check:

- why one ayah follows another;
- whether the surah has identifiable halves/turns;
- relation to preceding/following surah;
- whether classical naẓm sources already observe project structural claims.

## Step 9 — Perform novelty audit

For every major project synthesis:

1. search the declared classical corpus;
2. decide among:
   - `explicit`
   - `partial`
   - `building_blocks_only`
   - `none_found_in_checked_sources`
3. list `checked_sources`;
4. explain exactly which component is old and which combination appears new.

Do not use “new” merely because a modern phrasing sounds original.

## Step 10 — Preserve meaningful failed candidates

If a candidate connection is important enough that a future researcher may ask about it, preserve it as:

```text
{id:"...", type:method_note, tradition:project, ayah:"...", role:rejected_candidate, relation:lexical, status:interpretive, connection:rejected, priority:research, audience:research, reason:"...", prose:"...", source:"..."}
```

Do not record trivial dead ends.

## Step 11 — Deduplicate

If Tabari reports Ibn Abbas and later works merely repeat the same report:

- make one substantive block;
- identify later attestations in `attested_in` or source list;
- create additional blocks only if a later source changes the interpretation or evaluates it differently.

The target is **maximum information coverage, not maximum quotation count**.

## Step 12 — Insert annotations locally

Place an annotation where it helps the exact prose claim.

Preferred order when several blocks attach to the same point:

1. anchor/direct tafsir
2. disagreement/semantic range
3. asbāb/history
4. hadith
5. naẓm/cross-Qur'an
6. reader consequence
7. method constraint
8. novelty assessment

This is not rigid; local coherence matters more.

## Step 13 — Add source registry and audit note

End the file with:

- source registry;
- grading/source-criticism note;
- checked classical corpus for novelty audit;
- date/version if desired.

---

# 15. Special rules by information category

## A. Asbāb al-nuzūl

Never convert a report into a historical fact merely because it appears in al-Wahidi or al-Suyuti.

When multiple named individuals are given:

```text
status:reported
historicity:contested
role:asbab_context
```

Explain the conflict in `prose`.

Do not select the most vivid story and suppress competing reports.

## B. Hadith

Distinguish:

- direct tafsir;
- thematic parallel;
- interpretive corroboration.

Use the hadith's own grade/source when verified.

Do not quote long hadith text unnecessarily. Summarize accurately and keep a source reference.

## C. Qirāʾāt

Distinguish:

- canonical qirāʾah;
- shādhdh reading;
- Companion explanatory reading/report.

Use `canonical:true|false` only when classification is actually known.

If not assessed, say so.

## D. Historical context

Examples of good historical context:

- what an object in an early explanation physically was;
- what “borrowing a pot/axe/bucket” implies about shared daily life;
- legal/social status relevant to orphan property;
- institutional history of zakat if directly relevant.

Bad historical context:

- imagined scenes with no source;
- modern sociological claims projected backward;
- precise dates/locations derived only from literary intuition.

## E. Semantic history

Do not flatten early disagreement into one translation.

Preferred structure:

```text
term
reported early senses
named authorities
later persistence/change
interpretive consequence
```

## F. Project resonance

Always distinguish:

1. contextual meaning;
2. historically attested interpretive range;
3. broader lexical family;
4. project synthesis.

A root-family image can be real without being “what the ayah means.”

---

# 16. What counts as useful comprehensiveness?

Include information if it adds at least one distinct unit of value:

- a new early witness;
- a genuinely different interpretation;
- a source-critical distinction;
- a historical setting needed to understand the language;
- a hadith that creates a meaningful thematic bridge;
- a grammatical/rhetorical observation;
- a structural/nazm observation;
- evidence for or against a project synthesis;
- a historical change in interpretation;
- an interpretive consequence useful to the reader;
- a rejected candidate worth preserving for audit.

Do **not** add a full block merely because another later commentator repeats the same information unchanged.

---

# 17. Reader-facing prose rules

- Preserve the language and tone of the base commentary.
- New `prose` fields should normally be in the same language as the base file.
- Explain Arabic technical terms briefly for non-Arabic readers.
- Do not make every annotation read like an academic footnote; it should explain why the information matters.
- Avoid saying “the scholars say” when the source is actually one scholar or one report.
- Name disagreement where disagreement exists.
- Keep historical uncertainty visible.
- Avoid apologetic or polemical language.

---

# 18. Quality-control checklist

Before saving the output, verify all items below.

## Base-text integrity

- [ ] Original prose preserved if preservation was requested.
- [ ] No paragraph silently deleted.
- [ ] Existing `{ar:..., tr:..., gloss:..., source:...}` lexical tags preserved.
- [ ] Headings/order preserved unless restructuring was requested.

## Annotation syntax

- [ ] Every new annotation is exactly one `{...}` block.
- [ ] Every annotation has a unique `id`.
- [ ] Every annotation has `type`, `ayah`, `role`, `relation`, `status`, `prose`, `source` unless genuinely inapplicable.
- [ ] Enum values use the canonical vocabulary.

## Evidence integrity

- [ ] Asbāb reports are not stated as certain history without support.
- [ ] Thematic hadith are not labeled direct tafsir.
- [ ] Hadith grades are not invented.
- [ ] Canonical vs noncanonical reading reports are distinguished.
- [ ] Historical context is sourced.
- [ ] Conflicting early reports are preserved rather than silently harmonized.

## Novelty integrity

- [ ] Every novelty claim names `checked_sources`.
- [ ] No absolute “not found anywhere in classical tafsir” claim.
- [ ] `building_blocks_only` is used when classical ingredients exist separately.
- [ ] Lexical resonance is not presented as contextual translation.

## Redundancy

- [ ] Repeated reports are deduplicated.
- [ ] Later repetitions are listed as attestations rather than duplicated prose unless they add something.

## Reader usefulness

- [ ] Important technical distinctions have an `interpretive_consequence` where useful.
- [ ] The reader can understand why each block is present.
- [ ] General, advanced, and research layers are filterable through metadata.

---

# 19. Recommended output structure

```markdown
<!-- schema/version note -->

### Okuma katmanları
<short explanation of filtering and evidence levels>

{revelation_history block if relevant}

## Existing commentary heading 1

<original prose>

{tafsir block}
{asbab block}
{hadith block}
{reader_note block}

<original prose continues>

{novelty block near end of the relevant argument}

...

## Kaynak kayıtları

- **SOURCE-ID** — bibliographic description + URL/reference

### Kaynak-eleştiri notu
...
```

---

# 20. Generic examples

## Example 1 — Early disagreement

```text
{id:"SXXX-TAF-001", type:tafsir, tradition:rivayet, ayah:"XXX:Y", role:disagreement, relation:direct_tafsir, status:explicit, priority:core, audience:advanced, prose:"Erken kaynaklar burada iki ana açıklama taşır: ...", source:"TAB-XXX|SUY-XXX"}
```

## Example 2 — Asbāb with uncertainty

```text
{id:"SXXX-ASB-001", type:asbab, tradition:rivayet, ayah:"XXX:Y-Z", role:asbab_context, relation:asbab, status:reported, historicity:contested, confidence:low, priority:extended, audience:advanced, prose:"Ayetlerin nüzûlü farklı şahıslara bağlanmıştır...", source:"WAH-XXX|RAZI-XXX"}
```

## Example 3 — Thematic sahih hadith

```text
{id:"SXXX-HAD-001", type:hadith, tradition:hadith, ayah:"XXX:Y", role:corroboration, relation:thematic, status:explicit, hadith_grade:sahih, connection:strong, priority:extended, audience:general, prose:"Bu sahih hadis ayetin doğrudan tefsiri değildir; ancak ... temasını güçlü biçimde aydınlatır.", source:"MUS-0000"}
```

## Example 4 — Project novelty

```text
{id:"SXXX-NOV-001", type:novelty, tradition:project, ayah:"XXX:Y-Z", role:novelty_assessment, relation:lexical, status:interpretive, connection:resonant, classical_attestation:building_blocks_only, checked_sources:"Tabari|IbnKathir|Suyuti|Zamakhshari|Razi|Baydawi|Biqai", confidence:medium, priority:research, audience:research, prose:"Klasik kaynaklarda A ve B ayrı ayrı açıkça vardır; ancak A+B+C biçimindeki bütünleşik ağ taranan kaynaklarda açıkça bulunmadı. Bu nedenle yapıtaşları geleneksel, mevcut kombinasyon proje sentezidir.", source:"TAB-XXX|KASH-XXX|BIQAI-XXX"}
```

## Example 5 — Rejected candidate

```text
{id:"SXXX-MET-001", type:method_note, tradition:project, ayah:"XXX:Y", role:rejected_candidate, relation:lexical, status:interpretive, connection:rejected, priority:research, audience:research, reason:"Kök benzerliği mevcut fakat ayet bağlamı ve Kur'an içi kullanım bağlantıyı taşımıyor.", prose:"Bu aday incelendi ancak ana yoruma alınmadı...", source:"LEX-..."}
```

---

# 21. Codex execution instructions

Use the following procedure when Codex is given a surah/ayah and optionally an existing `.md` commentary.

## Inputs

Codex should accept:

```text
TARGET = SURA_NUMBER[:AYAH or AYAH_RANGE]
BASE_MD = optional path to existing commentary
OUTPUT_MD = desired output path
LANGUAGE = preserve base language unless explicitly changed
MODE = comprehensive
```

## Execution

1. Read this instruction file completely.
2. Read the entire base Markdown file if supplied.
3. Never infer that a truncated preview is the full file.
4. Identify the exact ayah/surah scope.
5. Create a claim map of the base prose.
6. Build a source/evidence matrix before editing.
7. Research the minimum corpus in Section 13.
8. Add information broadly, but deduplicate repeated reports.
9. Preserve original prose unless explicitly authorized to rewrite.
10. Insert structured blocks immediately where they are most relevant.
11. Add novelty assessments for every major project synthesis.
12. Add method constraints where a resonance could be mistaken for contextual meaning.
13. Add historical/asbāb uncertainty labels.
14. Add hadith grades only when verified.
15. Add/update source registry.
16. Run the full QC checklist in Section 18.
17. Save a new file; do not overwrite the original unless explicitly requested.
18. Produce a short machine-readable audit summary if desired:
    - number of base paragraphs preserved;
    - number of annotation blocks by `type`;
    - number of novelty claims;
    - number of disputed/uncertain historical reports;
    - source count;
    - unresolved items.

---

# 22. Copy/paste master prompt for Codex

Use this prompt after replacing the variables.

```text
You are enriching a Qur'anic commentary using the canonical annotation ontology in:
Tafsir_Comprehensive_Annotation_Instructions.md

TARGET: {{SURAH_OR_AYAH}}
BASE_MD: {{BASE_MD_PATH_OR_NONE}}
OUTPUT_MD: {{OUTPUT_PATH}}
MODE: comprehensive
LANGUAGE: preserve the language and prose voice of the base file

Primary objective:
Create one comprehensive Markdown research source that preserves the base commentary and adds machine-filterable annotation blocks for relevant tafsir, asbab al-nuzul, hadith, qiraat/readings, revelation history, historical context, semantic/reception history, nazm, Qur'an parallels, reader orientation, methodological constraints, and novelty assessment.

Non-negotiable rules:
1. Read the complete instruction file before working.
2. If BASE_MD exists, read the complete file and preserve its original prose unless a factual correction is explicitly authorized.
3. Never present a reported sabab al-nuzul as established historical fact merely because a classical book transmits it.
4. Never present a thematic hadith as direct tafsir unless the hadith explicitly interprets the verse.
5. Never invent hadith grades.
6. Distinguish canonical qiraat from Companion/noncanonical reading reports.
7. Do not let a root-family resonance replace the contextual ayah meaning.
8. For every major project synthesis, perform a novelty audit against an explicit checked classical corpus and use classical_attestation values exactly as defined.
9. Never claim that something is absent from all classical tafsir. Say only that no parallel was found in the checked sources.
10. Maximize distinct information coverage but deduplicate repeated reports.
11. Keep every new annotation as a one-line {...} block using the canonical enum vocabulary.
12. Add a complete source registry at the end.
13. Run the full QC checklist before saving.

Core classical corpus to check at minimum when relevant:
- Tabari
- Ibn Kathir
- Suyuti / al-Durr al-manthur
- Zamakhshari
- Fakhr al-Din al-Razi
- Baydawi
- Biqai
- al-Wahidi for asbab
- Bukhari/Muslim and other verified hadith sources as relevant
- additional classical sources when they materially clarify disagreement, chronology, qiraat, grammar, law, or reception history

Important distinction:
The output is not merely a tafsir summary. It is a layered research record. Explicitly distinguish:
A) contextual meaning,
B) early received interpretation,
C) later analytical development,
D) historical/reception context,
E) lexical/Qur'anic resonance,
F) project synthesis,
G) novelty relative to the checked corpus.

Before final save, report internally and verify:
- original base text preserved;
- all annotation IDs unique;
- all source IDs resolve in source registry;
- no ungraded historical report presented as fact;
- no thematic hadith mislabeled as direct tafsir;
- every novelty block has checked_sources;
- no duplicated reports that add no information;
- all resonance/constraint levels correctly marked.

Save the completed result to OUTPUT_MD.
```

---

# 23. Reference implementation

The current reference implementation is:

```text
S107_comprehensive_reference_v2.md
```

Use it to inspect:

- direct classical anchors;
- conflicting sabab reports;
- Makkī/Madanī disagreement;
- thematic sahih hadith;
- qiraat/Companion-reading labeling;
- semantic-history blocks for `sāhūn` and `māʿūn`;
- historical context for common household lending;
- `an salātihim` interpretive consequence;
- novelty assessments for the project's mirror, false-cloth, Suhā-star, house, water, fire, debt, and outward-prayer networks;
- constraints preventing lexical resonance from being mistaken for translation.

---

# 24. Versioning recommendation

Store a schema version in the top comment of generated files, e.g.:

```text
annotation_schema_version:2.0
```

If enum names or required fields change, increment the schema version and provide a migration note. Do not silently change the meaning of an existing enum.
