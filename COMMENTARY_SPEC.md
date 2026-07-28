# Commentary Specification

Governs ayah-level (layer 2) and surah-level (layer 3) commentary. Both consume
the same input bundle and obey the same evidence rules; they differ in what
question they answer and in whether they are allowed to select.

[`PRINCIPLES.md`](PRINCIPLES.md) governs this file. Sources and formats are in
[`docs/SOURCES.md`](docs/SOURCES.md); channel rules in
[`docs/CHANNELS.md`](docs/CHANNELS.md).

Status: draft, 2026-07-27. Derived from rejected S103 attempts; **not yet
validated against a passing output.**

---

## 1. What commentary is for

The reader understands the ayah better after reading the prose than before.
Nothing else is a success criterion.

The reader must never be shown which layer a claim came from, how many readers
converged, confidence labels, ablation records, row counts, branch identifiers,
or schema names. That apparatus belongs in the evidence surface
(`PRINCIPLES.md` §12).

The reader must also not be *destabilised*. A latent reading that is true,
contained, and fully traceable can still leave the reader less certain of what
the ayah says than before — that is a failure, and grounding
(`PRINCIPLES.md` §5) is what prevents it.

---

## 2. The two levels

|  | layer 3 — surah | layer 2 — ayah |
| --- | --- | --- |
| question | what is this surah's argument, and what runs through it? | what happens in this ayah, on its own? |
| selection | **must select** — a thesis excludes | **must not select** — carries the full field |
| time | none; the whole is present at once | **has a before and an after** |
| pass condition | says something no ayah-by-ayah reading could produce | holds what the surah thesis had to drop |

These are not two sizes of one output. A surah reading that decomposes back into
its ayahs has failed. An ayah reading that is a slice of the surah thesis has
failed.

The split is also where no-disambiguation is structurally guaranteed. Building a
thesis requires excluding readings. With one level, excluded readings would be
lost. With two, the thesis lives at surah level and the complete field survives
at ayah level. Neither cancels the other; they answer different questions.

### 2.1 The surah argument rests on the primary reading

An argument that holds only under latent readings is not yet an argument. State
it from the primary reading first; latent readings then perturb, deepen, or
recolour it. If removing every latent reading collapses the thesis, the thesis is
not ready.

This does not demote channels — see `docs/CHANNELS.md` §4. The argument and the
channels are separate outputs on separate axes, and for some surahs (S100) the
channel is the more valuable finding.

### 2.2 Channel increments are not thesis slices

Layer 2 may carry a **channel increment** — a resonance entered through this
ayah's own word and bounded by the channel's maturity at this position. That is
permitted, and it is the mechanism that keeps layer 3 from arriving cold.

Layer 2 may **not** carry the surah's thesis. The difference is testable: an
increment is anchored in lexis present in this ayah and says only what has
matured by here; a thesis is anchored in the assembly and says what is only
visible from outside.

**The increment requires a ledger, and no surah has one.** Maturity is computed
nowhere, and an increment unbounded by maturity is just a channel claim. Until
adjudication runs, layer 2 may use review material to connect words inside this
ayah but may not name a channel as an established image of the surah.

Disclosure rules and the interim state: `docs/CHANNELS.md` §3 and §3.1.

---

## 3. Depth model (build-time only)

Evidence enters at six depths. **Depths never appear in output.** They govern
what may be written and keep the primary reading structurally protected.

```
D0  what the grammar forces           QAC + attachments
D1  what the local form selects       word_analysis `used`      ← the primary reading
D2  what colors it                    word_analysis `narrowed`
D3  what activates under context      v12 models + trajectory
D4  what corroborates                 inter-ayah clusters
D5  apparatus                         variants, shawādhdh, sound
```

Depth is distance from the grammatical floor — not confidence, not rank. Ranking
readings forces a winner, which is disambiguation under another name
(`PRINCIPLES.md` §3). Two readings at the same depth coexist; nothing at D3 can
displace D1, because they are not on the same axis.

Depth does inform **grounding**: material further from the floor needs more
ground laid before it can be spoken.

---

## 4. Known failure modes

Observed during S103 development. Each produced output that was rejected.

| failure | symptom |
| --- | --- |
| aggregation-as-synthesis | clustering ayah readings, naming the cluster, calling it surah commentary |
| provenance-as-structure | sections titled by which layer they came from |
| list reformatting | N source readings become N prose sections in a different language |
| decorated primary | one latent branch used as seasoning; the rest of the latent field unused |
| latent-only thesis | a surah argument that collapses if the latent layer is removed |
| imported citation | a correct reference the writer knew but the bundle did not contain |
| sample-as-whole | reading one of eighteen word records, then writing as if from all |
| ungrounded reveal | a contained, traceable reading delivered before the reader had ground for it |

---

## 5. Output contract

Per ayah and per surah:

- **prose** — continuous, single voice, no provenance markers, no headers named
  after evidence layers, and no wrapper labels such as `=== THE PROSE ===` when
  the prose is written to its own file;
- **evidence surface** — separate, addressable per phrase, holding refs, branch
  IDs, counter-evidence, coverage, and an explicit mark on every claim that is
  inference rather than bundle-traceable.

The prose must be readable end to end with the evidence surface closed.

Arabic lexical items in authored prose should use structured surface spans so one
text can render for both reading and listening editions:

```text
{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar}
```

Use the span at first mention of an ayah word, and again when the prose returns
to that word after moving to another word or another paragraph. A renderer may
collapse repeated fields later; the authored source should preserve `ar`, `tr`,
and `gloss` whenever the word is doing fresh interpretive work.

For reader display, render transliteration first, with Arabic in parentheses and
the gloss nearby. For TTS, render the Arabic surface form. For Turkish-only
display, render the gloss. Raw root skeletons, branch IDs, and letter-by-letter
root transliterations belong in the evidence surface, not in reader prose.

Prose should begin from reader meaning, then bring in grammar. A sentence may say
"Âyet önce hamdi Allah'a verir; bunu fiille değil, sabit bir ad cümlesiyle
yapar." It should not make the reader cross a technical threshold before knowing
what is happening.

Layer 3 additionally emits:

- **thesis** — one sentence;
- **channel candidates** — members, the system they form, what becomes legible,
  and rejected motifs with reasons. Input to adjudication, not a ledger: prose
  writers do not establish channels (`PRINCIPLES.md` §2), and maturity is
  computed by the adjudication pass (`docs/CHANNELS.md` §6);
- **exclusions** — activated readings the thesis could not carry, handed to
  layer 2.

---

## 6. Input bundle

One bundle per ayah; a surah bundle is the ordered set of its ayah bundles plus
surah-scope material. Built by `scripts/build_bundle.py`; shape in
`bundles/schema.json`; sources, formats, gotchas, and the coverage requirement in
[`docs/SOURCES.md`](docs/SOURCES.md).
