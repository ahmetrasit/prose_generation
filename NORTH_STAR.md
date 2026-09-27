# North star

Written 2026-09-26 from the user's own statements (`ultimate goal.txt`, README "Who this is for",
`COMMENTARY_SPEC.md`, `PRINCIPLES.md`, `_commentary/v9/DESIGN.md`, `latent_activation/main goal.txt`, and the V11
conversations); revised 2026-09-27 for v13 from the user's answers after the v12 S1 run and a review of v1–v12.
Every workflow decision is judged against this page. It is never a model input (it names test cases).

## The reader

One reader: a curious Turkish speaker with almost no Arabic grammar, whose Arabic arrives through loanwords, and
whose theological loanwords (oku, ibadet, âlem, salât …) have shifted, narrowed or lost their meaning in Turkish.
Canonical meanings are easy to find elsewhere; they are only the anchor. **The goal is what cannot be found
otherwise.**

**Success:** the reader understands the ayah and the surah better after reading than before, and is never
disoriented.

## The question

What would al-Khūlī / Bint al-Shāṭiʾ (a word through all its Quranic uses and all its root's attested senses),
al-Biqāʿī (*naẓm*: an ayah through its neighbours and its surah's purpose) and the Quran-explains-the-Quran
tradition produce today, with a dictionary of every attested branch of every root and with AI agents? Their
ultimate explanation of the Quran is the target, applied systematically and without timidity: a supported surprise
is the aim, and rigour comes from exact evidence, not from caution.

The underlying view: tafsir and translation disambiguate, but the language keeps several meanings alive at once.
Each secondary layer reveals an image woven in the background, and these layers usually converge on the surah's
main theme from several sides, each audible to a reader in a condition (the thirsty hear water, the lost hear
guidance, the one who lives life as a journey hears the road).

## The products

1. **Ayah commentaries**, one per ayah.
2. **A surah commentary**, one per surah, of any length: the surah's images (chains) with each ayah explained
   within them, then how the images interact. Not a canonical summary (the pericope summaries in quran-notes did
   not show the network).

Turkish first; English and German later from the same analysis (analyse once, render per language; the Furūq v4
dictionary is language-agnostic, the language-specific dictionary entries exist only for Turkish). Out of scope
here: the per-word gloss product (up to three glosses with error profiles and a "check the other glosses" flag)
and the word panel belong to the translation app; audio comes after the prose is settled.

## What an ayah commentary carries

- **Ground:** the plain sense, never disorienting.
- **What the target language loses:** what each key Turkish word loses or adds against the Arabic concept (iqraʾ is
  more than "oku"); and grammar the reader cannot hear in Turkish (the two articles of aṣ-ṣirāṭ al-mustaqīm) only
  when it matters to a reading, explained once, here. Not a grammar-focused prose.
- **Local resonance:** latent readings activated within the ayah and within its window and surah (5:6: mirfaq
  leaning, kaʿb and the Kaʿba "qiyāman", then "qawwāmīn" in 5:8).
- **The image chains opened through its words:** every surah image that touches the ayah's words is made possible
  here, disclosed progressively across the ayat (1:6 introduces the road through naʿbudu and ʿālamīn; 1:7 assembles
  the traveller).
- **Quran-loaded words:** a word the Quran uses with one recurring role, and the places where the canonical
  translation departs from that role (ḥamaʾ: mud as human fabric, seen by an observer, so 18:86 too; nafakha:
  animating in 19 of 20 uses, so 18:96 is more than blowing the bellows).
- **The Quran explaining it (QeQ), after the latent readings:** for each finding, what the rest of the Quran does:
  supports, expands, shifts or contradicts it; and passages that work on the ayah's own main axes. QeQ rests on
  canonical readings, so it never suppresses a surprise reading; a conflict is explained, and a finding the Quran
  contradicts is marked. QeQ that touches no axis of the ayah is left out.

## What the surah commentary carries

The images that run through the surah, what each ayah and word contributes, how the images **interact** (not silos:
the traveller on the road is also the one kept alive by water in the desert; the herd led by its rabb), their
convergence on the surah's movement and purpose, and the surah read anew through them. Holistic, but the reader's
feet stay on the ground.

## The "aha"

Non-canonical but supported readings, **explained and connected, never catalogued**: Fatiha as a traveller's prayer
(way-marks in ʿālamīn, the road's middle and the lead animal in mālik, the trodden road in naʿbudu, the road that
swallows its travellers in ṣirāṭ, the stray whose rabb is unknown in ḍāllīn), the water that keeps the traveller
alive (rain, gathered water, the well and its pulley), the herd led by its rabb; S100's running horses becoming part
of the surah's argument; ṣalāh heard beside "the one who comes second in a race" among those who tried to outrun
(29:39–45).

## How a branch becomes heard

- **Branch-agnostic.** Branches have no order. Any attested branch can be heard when it is activated by the ayah's
  own words, the neighbouring words, the surah's words, or the words of the Quran passages that explain the ayah.
- **The dictionary is the guard and the supplier:** it prevents hallucinated senses and modern-Arabic or
  majority-reading drift, and it supplies the rare senses a model will not recall (the eye disease in as-sabīl).
  A sense recalled from memory that the dictionary does not attest is marked, never silently used.
- **No premature pruning** (the central risk, not hallucination). Discovery keeps partial, strange and minor
  activations, combines fragments across branches and roles, lets a completed image strengthen its weak parts, and
  only then asks what it shows about the primary reading: activation → coalition → maturation → reciprocal
  reinforcement → rereading the primary meaning → prose. No early plausibility filter, no confidence scoring during
  discovery, no verdict on a chain from one of its members.
- **The payoff test comes at synthesis:** what does this resonance make perceptible in the direct reading that a
  plain paraphrase could not (more spatial, bodily, causal, relational, material, temporal, compositional)? Space in
  the prose follows that payoff: functional hierarchy, not epistemic downgrading.
- **Integration, not aggregation:** readings explain one another; the branches of one root are usually facets of one
  concept (S103 ʿ-ṣ-r: retention under compression), and finding the concept is the finding.

## Guardrails

- **No disambiguation.** Readings coexist; nothing is ranked or declared the correct one.
- **Containment.** Every latent reading is stateable in a sentence that keeps the primary reading intact
  (never "not X but Y").
- **Checkable.** A finding's anchor is the dictionary branch plus its trigger (the activating word). A passage where
  the Quran tells the same scene openly strengthens it; its absence never removes it. Every Arabic quotation carries
  its source (`source:S:A` or `source:root Bnnn`), which the reader app shows on hover and links to the dictionary.
- **No invention.** No invented senses, sources, etymologies or chronology.
- **Nothing lost silently.** Exclusions are handed forward, counter-evidence is kept, retrieval labels order and never
  filter.

## Building on what exists

- The dictionary: every attested branch of every root (Turkish entries; Furūq v4 language-agnostic), with the
  reviewed alternative root analyses.
- The surah channel reviews (quran-data `channels/network-v3/sNNN/review`, 110 surahs): the image chains, grounded,
  extended, corrected and connected, never rediscovered. HFT (90 surahs) is a shortcut, not a requirement.
- The reciprocal inter-ayah lists (quran-data `analysis/inter-ayah/reciprocal`, from GPT runs): incomplete and
  sometimes misleading; best used at the end as a missing-passage check, after the writer's own reasoning.
- Word analysis (per word; the per-lemma-and-form summaries in progress), QAC morphology, qirāʾāt.

## Economics

Opus 5.5 at effort high is required for synthesis: Sonnet, lower effort, Luna, Sol and Astra (v5's S1) did not reach
it; Luna follows worklists and discovers, but does not synthesize. The cost is made affordable by the process, not by a
weaker model: steps that work as a funnel (each output compact, constrained and non-redundant, and the only input the
next step needs beyond a small core), Luna upstream only for steps that need no synthesis, the Batch API and a cached
shared surah prefix. Input is cheap when it helps thinking without diluting attention (bulk input measurably diluted
synthesis: 4:34 cold Opus scored above Opus with the dictionary or the full package); thinking is welcome; output is
welcome when it earns its place. The workflow is worth running only if it materially exceeds v5 on this reader's
criterion. Tests may cost up to $5 per ayah (the user's subscription); production aims toward ~$1 per ayah on average
through the API.

## Lessons that shaped this page (v1–v12)

- Asking one prompt for two stances loses one of them: QeQ and grammar are evidence-bound, latent resonance is
  generative; each version tilted toward one (v11/v12 audited the chains away; the gold is latent-rich and QeQ-light).
- An editor cannot recover findings rejected upstream (v5); worklists and "every record must reach the prose" turn
  discovery into accounting and prose into a catalogue (V9 findings lane, v3, v7).
- Luna's discovery gaps were instruction-fixable (a registry label treated as disqualifying); its synthesis was not.
- Bulk evidence re-read by every step made v5 expensive (2 MB lane packets, composition re-reading discovery).
- The first cold Opus brief (two keys: a dictionary branch plus an independent trigger; HFT articulated, not audited)
  and the 5:6 / 4:34 cold arm (a 68-line brief on context only, $1.4–1.5) produced the latent readings the later
  auditing briefs lost.
