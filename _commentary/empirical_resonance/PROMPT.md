# Empirical Resonance Prompt

Read `../../PRINCIPLES.md` and `../../COMMENTARY_SPEC.md` first. They govern evidence,
containment, grounding, and the separation of prose from apparatus. This prompt
defines an additional support layer; it does not replace ayah commentary.

You are given a hermetic input packet for one ayah, an ayah window, or a
pericope. The packet may include completed Layer 2 prose/evidence and may include
modern empirical source notes. Write an empirical resonance note that helps a
reader check whether a concrete feature of the ayah has a disciplined modern
explanatory analogue.

## Task

Identify empirically discussable hooks in the given ayah material and write only
the findings that can be responsibly supported from the supplied sources.

The output is not an apologetic proof, not a miracle claim, not tafsir, and not a
fiqh ruling. It is a reader aid: "this wording or situation may be read alongside
this body of knowledge, with this strength and these limits."

## Inputs You May Use

Use only material inside the packet:

- ayah text, translation, token notes, and local context ayat;
- optional Layer 2 prose, evidence, and findings;
- candidate hooks;
- research source entries and their cited claims;
- explicit exclusions and source gaps.

Do not use memory for empirical claims. Do not cite a paper, statistic, doctrine,
experiment, or historical fact unless it is supplied in the packet. If you know a
likely claim but it is not sourced in the packet, put it in `Source Gaps`.

## What Counts As A Hook

A hook is a concrete ayah feature that can responsibly meet an empirical domain:

- body part, sensation, perception, cognition, emotion, memory, sleep, aging, or
  illness;
- social practice, testimony, debt, contract, household relation, inheritance,
  power, coercion, status, reputation, or group behaviour;
- physical process, weather, ecology, animal behaviour, agriculture, navigation,
  astronomy, material culture, or built environment;
- legal or institutional procedure that can be compared with evidence about risk,
  incentives, record-keeping, error, intimidation, or social access.

Do not create a hook from a vague moral word alone. The ayah must give you an
observable phenomenon, mechanism, practice, or scene.

## Strength Labels

Every finding must carry exactly one strength label:

- `established`
- `well_supported`
- `plausible`
- `contested`
- `speculative`
- `unsupported`

Use `SCHEMA.md` for the meanings. These labels are for the reader's follow-up
judgment. They are not an audit layer and do not appear as confidence theatre.

Normally, `speculative` and `unsupported` claims do not enter the prose. Record
them under `Source Gaps` unless there is a strong reason to explain why a popular
claim should be rejected.

## Writing Rules

Write in disciplined prose. No fluff, no praise language, no inflated certainty.

Good claim forms:

- "This resonates with..."
- "The supplied sources make a limited comparison possible..."
- "A cautious reader can connect this with..."
- "The evidence supports the narrower claim that..."
- "This does not show..."

Forbidden claim forms:

- "Science proves the ayah..."
- "The ayah predicted..."
- "This is definitely why..."
- "Modern research confirms the Qur'an..."
- "Men are X / women are Y" when the source only supports contextual, social, or
  task-specific differences.

Where a finding touches gender, race, class, disability, crime, sexuality,
mental health, or medical risk, be stricter than usual. State the population and
context. Avoid biological or psychological essentialism unless the supplied
sources are unusually strong and directly relevant.

## Method

1. Read the ayah material and optional Layer 2 output.
2. List candidate hooks, but keep only those grounded in explicit ayah material.
3. Match hooks to supplied source claims.
4. Assign the weakest honest strength label justified by the source set.
5. Write reader-facing prose that preserves the ayah's primary meaning and uses
   empirical material as resonance, not replacement.
6. Emit a findings table with sources and limits.
7. Record missing or rejected items in `Source Gaps`.

## Required Output

Use this exact section order.

```markdown
## Empirical Resonance

<Continuous prose. Use compact source markers such as [src01] only where needed.
Do not turn every finding into a separate miniature essay if they naturally
belong together.>

## Findings

| id | ayah hook | domain | strength | claim | sources | limits |
| --- | --- | --- | --- | --- | --- | --- |
| er01 | ... | ... | well_supported | ... | src01, src02 | ... |

## Source Gaps

- <Hook or popular claim that could not be responsibly written from the supplied
  packet, with the reason. Write `None.` if there are no gaps.>

## References

- src01: <authors/institution>. (<year>). <title>. <venue/publisher>. <DOI or URL if supplied>.
```

## Acceptance Checks

Before finalizing, check:

- Every empirical claim has at least one source ID.
- Every cited source ID has a full entry in `References`.
- Every finding has one strength label.
- No claim says or implies proof, prediction, or replacement of tafsir.
- No finding exceeds its source population, domain, or time period.
- Layer 2 prose, if supplied, is used for anchoring and wording only, not as
  empirical evidence.
- Unsourced but tempting material appears only in `Source Gaps`.
