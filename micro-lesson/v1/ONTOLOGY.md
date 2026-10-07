# Ontology and annotation guide

The ontology covers the linguistic reading scope at launch: Quranic Arabic
reading distinctions, word formation and inflection, syntax, discourse, lexical
semantics, and Arabic–Turkish gloss interpretation. It contains 297 concepts
across 30 overlapping topics. Every concept has a Turkish label, definition,
attachment boundary, introduction and illustrative example. Seven routes cover
all concepts; routes are suggestions rather than compulsory course order.

Completeness here means an authored home for the ordinary and advanced phenomena
in these areas, including all QAC part-of-speech families, morphological feature
families, phrase types and published syntactic relation families, and every fit
category in the dictionary gloss contract. It does not mean every possible example,
every root copied into this file, or an external scholarly certification. New
linguistic evidence can refine a definition without making concept discovery a
routine production stage. There are no placeholder concepts awaiting definitions.

Specialized recitation certification, productive modern Arabic, historical
reconstruction without sources, and theological/legal taxonomies are outside this
micro-lesson curriculum. Relevant supported linguistic observations in those
passages still attach to the ordinary reading concepts. Qiraat have a concept for
their evidenced linguistic effect; an unsupported reading is deferred.

## Graph and annotation semantics

Like the useful aspect of Gene Ontology, this is a graph with multiple annotation
points and multiple paths, not a folder tree with exactly one destination. It does
not implement GO's biological relations, evidence codes or an OWL reasoner.

- Topic `parents`: navigation within a directed acyclic hierarchy. A topic may
  have more than one parent, and a concept may belong to more than one topic.
- Concept `broader`: a wider teaching area containing this specific distinction.
  This is pedagogical inclusion, not a claim that a word or grammatical entity is
  biologically or formally a subtype of another. Several broader concepts are allowed.
- `requires`: a suggested dependency for explaining the concept at this depth.
  The actual lesson can teach that foundation itself and omit the reminder.
- `helped_by`: useful background that is not needed to understand every example.
  These links are not hierarchy edges and may be reciprocal where learning is helpful.

No relation automatically grants mastery. Topic ancestry is available for browsing
and finding related lessons, but it does not create direct lesson annotations.
Do not copy all `broader`, `requires`, or `helped_by` links into an output.

A lesson has `concepts: [{id, role}, ...]`. Any number of meaningful direct tags
may come from the same or different categories. At least one is `teaches`; several
are allowed. `reinforces` means the wording practices a skill without introducing its
general principle. Roles describe the content, not the current reader’s mastery. `contrasts` marks an explicitly contrasted concept. No single primary tag
is required, and the engine's name does not restrict the concepts it can use.

One coherent observation is not the same as one ontology concept. “The imperative
form here functions as prayer” can teach imperative form, speech function and
Turkish rendering together without becoming three separate lessons.

## How to attach a lesson

1. Name what the reader will notice or understand from the final wording.
2. Search the full INDEX.md by keyword, Turkish label or the ontology aliases.
   Search outside the authoring engine's category too.
3. Read the candidate definitions and `boundary_tr`. Prefer the most precise
   concept, using several when the observation actually teaches several skills.
4. Add a broader concept only if the general principle is also explicitly taught.
   A concrete suffix lesson does not automatically teach all of pronoun grammar.
5. Assign one role per concept. Mere mention is not annotation. Comparing two words
   does not automatically mean the two curriculum concepts are contrasted.
6. Inspect actual assumed knowledge and choose reminder IDs. A concept explained
   here is not a required prerequisite. Reader state is applied later by the app.

Dictionary `root/branch`, lexical-unit and gloss locators identify what the lesson
is about lexically. Concept tags identify the reusable learning involved. Keep both
without turning each dictionary branch into a duplicate curriculum concept. A new
lexical instance can be worth teaching even after its general concepts are learned.

## Reading the example texts

Catalog examples are short **illustrative teaching examples**, including ordinary
constructed Arabic combinations, pattern placeholders and hypothetical gloss
comparisons. They are not all Quran quotations. They explain a concept before a
learner returns to the actual passage. Production lessons need their own supplied
evidence and must label dictionary examples as such. The worked fixtures under
examples/ retain exact source paragraphs and Arabic evidence separately.

## Coverage and routing

The tables below are an editorial navigation aid, not a validator or a command to
emit a lesson for every feature. Corpus tags describe analysis; lesson tags describe
what the wording teaches. A single source tag can support several different lessons.

### QAC part-of-speech families

| Source family | Teaching attachment candidates |
|---|---|
| N, PN, ADJ | ML:C003 `noun_verb_particle`, ML:C062 `proper_noun`, ML:C010 `noun_adjective` |
| PRON, DEM, REL | ML:C076 `independent_pronoun`, ML:C008 `attached_pronoun`, ML:C084 `demonstrative`, ML:C085 `relative_pronoun` |
| V, IMPN | ML:C089 `perfect`, ML:C090 `imperfect`, ML:C091 `imperative_form`, ML:C218 `verbal_noun_imperative` |
| T, LOC | ML:C164 `time_adverb`, ML:C165 `place_adverb` |
| P | ML:C004 `preposition`, ML:C159 `prepositional_attachment` |
| EMPH, IMPV, PRP | ML:C198 `lam_emphasis`, ML:C200 `imperative_lam`, ML:C199 `purpose_particles` |
| CONJ, SUB | ML:C170 `coordination`, ML:C172 `nominalized_clause`, ML:C171 `relative_clause` |
| ACC, PREV | ML:C149 `inna`, ML:C211 `preventive_ma` |
| AMD, RET | ML:C196 `bal_lakin` |
| ANS, AVR | ML:C206 `answer_particles`, ML:C209 `aversion` |
| CAUS, RSLT | ML:C289 `causal_fa`, ML:C178 `result_fa` |
| CERT, FUT | ML:C197 `qad`, ML:C095 `future_marking` |
| CIRC, COM | ML:C286 `circumstantial_clause`, ML:C166 `comitative` |
| COND, EQ | ML:C173 `conditional`, ML:C214 `equalization` |
| EXH, EXL, INT | ML:C208 `exhortation`, ML:C290 `explication_amma`, ML:C210 `explanation_particle` |
| EXP, RES | ML:C167 `exception`, ML:C169 `restriction_exception`, ML:C215 `restriction_innama` |
| INC, REM, SUP | ML:C288 `inceptive_particle`, ML:C287 `resumption`, ML:C212 `supplemental_particle` |
| INTG, NEG, PRO | ML:C205 `interrogative_particles`, ML:C014 `negation`, ML:C201 `prohibitive_la` |
| SUR, VOC, INL | ML:C213 `surprise_particle`, ML:C156 `vocative_construction`, ML:C050 `disconnected_letters` |

### Morphology and syntax

| Source feature/relation | Teaching attachment candidates |
|---|---|
| Root, lemma, segments | ML:C016 `root_word`, ML:C051 `stem_lemma`, ML:C001 `word_parts`, ML:C053 `clitic_stack` |
| Person, number, gender | ML:C009 `person_number`, ML:C054 `grammatical_gender`, ML:C056 `dual`, ML:C057 `sound_masculine_plural`, ML:C058 `sound_feminine_plural`, ML:C059 `broken_plural` |
| Definite/indefinite | ML:C007 `definiteness`, ML:C063 `article_definiteness`, ML:C064 `generic_article`, ML:C065 `indefiniteness`, ML:C066 `tanwin_limits` |
| NOM, ACC, GEN | ML:C067 `nominative`, ML:C068 `accusative`, ML:C069 `genitive`, ML:C070 `case_letters`, ML:C071 `diptote`, ML:C072 `estimated_case`, ML:C073 `indeclinable` |
| Aspect and mood | ML:C089 `perfect`, ML:C090 `imperfect`, ML:C091 `imperative_form`, ML:C093 `tense_aspect`, ML:C097 `indicative`, ML:C098 `subjunctive`, ML:C099 `jussive` |
| Voice and participles/VN | ML:C102 `active_voice`, ML:C103 `passive_voice`, ML:C126 `active_participle`, ML:C127 `passive_participle`, ML:C022 `verbal_noun` |
| Measures and irregular surfaces | ML:C112 `form_i`, ML:C121 `form_x`, ML:C122 `rare_triliteral_forms`, ML:C123 `quadriliteral`, ML:C124 `quadriliteral_derived`, ML:C125 `pattern_sound_change` |
| Pronoun, emphatic and vocative suffixes | ML:C080 `subject_suffix`, ML:C079 `object_suffix`, ML:C078 `possessive_pronoun`, ML:C081 `prepositional_pronoun`, ML:C101 `emphatic_nun`, ML:C156 `vocative_construction` |
| adj, poss, pred, app, spec, cpnd | ML:C010 `noun_adjective`, ML:C011 `idafa`, ML:C141 `predicate`, ML:C154 `apposition`, ML:C161 `specification_tamyiz`, ML:C296 `compound_number` |
| subj, pass, obj, subjx, predx | ML:C144 `subject`, ML:C145 `passive_subject`, ML:C157 `direct_object`, ML:C147 `kana`, ML:C149 `inna` |
| impv, imrs, pro | ML:C200 `imperative_lam`, ML:C285 `imperative_result`, ML:C201 `prohibitive_la` |
| gen, link, conj, sub, cond, rslt | ML:C006 `genitive_after_preposition`, ML:C159 `prepositional_attachment`, ML:C170 `coordination`, ML:C171 `relative_clause`, ML:C173 `conditional`, ML:C178 `result_fa` |
| circ, cog, prp, com | ML:C160 `circumstantial_hal`, ML:C162 `cognate_accusative`, ML:C163 `purpose_accusative`, ML:C166 `comitative` |
| Particle dependency families | ML:C217 `multiple_function_word`, ML:C229 `scope` |
| S, NS, VS, CS, PP, SC | ML:C138 `clause_roles`, ML:C139 `nominal_clause`, ML:C143 `verbal_clause`, ML:C173 `conditional`, ML:C159 `prepositional_attachment`, ML:C172 `nominalized_clause` |

### Dictionary and Turkish mapping

| Source content | Teaching attachment candidates |
|---|---|
| Branch and lexical-unit scope | ML:C018 `semantic_branch`, ML:C246 `branch_applicability`, ML:C245 `lexical_unit`, ML:C026 `collocation` |
| Facets: core, specialization, source variant | ML:C247 `semantic_facets`, ML:C270 `gloss_facet_scope` |
| Concept/contextual/lexical gloss | ML:C260 `concept_context_gloss`, ML:C245 `lexical_unit` |
| fit: none; preserves | ML:C261 `gloss_preservation` |
| fit: narrowing; loses | ML:C028 `semantic_narrowing`, ML:C262 `gloss_omission`, ML:C267 `contextual_narrowing_valid` |
| fit: broadening; adds | ML:C029 `semantic_broadening`, ML:C263 `gloss_addition` |
| fit: displacement | ML:C030 `semantic_shift` |
| fit: drifted_loanword | ML:C266 `drifted_loanword`, ML:C032 `translation_history` |
| collision; excluded glosses | ML:C264 `gloss_collision`, ML:C269 `excluded_gloss` |
| Neighbor distinctions | ML:C033 `sense_boundary`, ML:C253 `near_synonym`, ML:C254 `antonym`, ML:C257 `semantic_field` |
| Qualified identity/etymology; root profile | ML:C258 `root_relation_qualified`, ML:C284 `etymology_usage`, ML:C025 `root_image_limits` |
| No compact equivalent; structural mismatch | ML:C268 `conceptual_gap`, ML:C279 `explanatory_gloss`, ML:C272 `case_translation`, ML:C274 `word_order_translation` |

Discourse coverage additionally includes scope, focus, address shifts, repetition,
parallelism, contextual generality, questions as speech acts, figurative imagery
and its limits. These are teaching categories; QAC tags alone do not prove their
presence or interpretation.

## Editorial maintenance

The catalog is available before lesson production; ordinary constructions must
not be sent to a future “ontology discovery” queue. An exceptional genuinely new
distinction is saved with its supported draft and proposed parents, then edited
into the catalog before that lesson is finalized. First check whether it is a new
example of an existing skill rather than a new skill.

Keep IDs when clarifying wording without changing a concept's identity. If splitting
or replacing a concept changes what it means to know it, make an explicit editorial
mapping for prior annotations and learner states; never silently transfer mastery
to all new children. Reminder IDs derive from concept IDs, so new concepts need no
duplicated message authoring. Update the route and index alongside a new concept.

The original C001–C036 IDs remain stable. Broad original concepts are still useful
when their general distinction is actually taught, with precise descendants and
other related concepts now available for narrower lessons.

## Source orientation

The coverage inventory was compared with the official Quranic Arabic Corpus
[tagset](https://corpus.quran.com/documentation/tagset.jsp),
[morphological features](https://corpus.quran.com/documentation/morphologicalfeatures.jsp),
[syntactic relations](https://corpus.quran.com/documentation/syntaxrelation.jsp),
[phrase types](https://corpus.quran.com/documentation/phrasetags.jsp), and
[grammar guide](https://corpus.quran.com/documentation/grammar.jsp).
These guide coverage and terminology, not automatic semantic formulas.

Dictionary references, relative to the repository root, are
`../dictionary/v2/schema/encyclopedia-entry.schema.json`,
`../dictionary/v2/gloss_generation/README.md`, and the particular branch and
reviewed gloss records selected for a passage. The dictionary supplies lexical
boundaries and existing Turkish analysis; the ontology organizes learning.
