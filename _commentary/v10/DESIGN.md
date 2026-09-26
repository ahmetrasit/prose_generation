# Why this v10

The desired product is an understanding of the focus ayah that a non-Arabic
reader could not obtain from a translation alone. An ordinary reading orients
the reader; latent images, Quranic reuse, contrasts and structural relations
do substantive interpretive work. The target is a developed reading with the
main consequential discoveries, not an inventory of every possible association.

HFT is an upstream attempt at the same problem. It can supply excellent
compositions of images, roles and transformations, and save rediscovery. It
cannot be a mandatory expensive prerequisite for another expensive synthesis.
The workflow therefore accepts existing HFT but uses the same downstream
reading-brief handoff when it is absent. It does not generate a replacement HFT
run as an extra mandatory stage.

We cannot recover Opus's private internal reasoning from its prose. We can test
whether an explicit division of observable work reproduces the useful result:
source interpretation, composition of interacting images, Quranic comparisons,
selection by explanatory consequence, and development for the reader. Those
artifacts should be judged by what they preserve and explain, not by resemblance
to a speculative account of how a particular model thinks.

## What the v5 comparison actually showed

The user identifies S1's v5 run as Astra Max and the comparison surahs as
Luna-generated. These are user-reported run descriptions, not inferred model
IDs for the upstream network reviews. Historical v5 orchestration defaults also
vary by stage; do not use the model label alone to explain quality differences.

The inspected samples were:

- [1:6 editorial](../v5/editorial/s001-fresh-20260910/s001/1_6/1_6.prose.editorial.tr.md):
  11,249 whitespace-delimited words, 92 paragraph blocks, 13 headings. There are
  developed local connections, including source, access and sustaining support.
  Extensive coverage and repeated qualifications make a long reader journey.
- [12:84 editorial](../v5/editorial/s012-p05-with-fatiha/s012/12_84/12_84.prose.editorial.tr.md):
  2,708 words. The contained grief, sealed vessel, source and hidden-water-channel
  connection is already substantive synthesis. The same grief/anger boundary is
  revisited, and the reader still has to consolidate several restatements.
- [100:1 editorial](../v5/editorial/s100-regular-20260911/s100/100_1/100_1.prose.editorial.tr.md):
  3,159 words. Breath as expenditure and the return toward inward disclosure
  give useful interpretive direction. Other material and animal details are
  accumulated faster than their individual necessity is established.
- [93:3 editorial](../v5/editorial/s093-regular-20260912/s093/93_3/93_3.prose.editorial.tr.md):
  2,920 words in 16 sections. Many images are introduced as another version of
  care or reassurance. The strongest alternatives need development and relative
  prominence, rather than equal passage through a catalogue.
- [18:86 editorial](../v5/editorial/s018-regular-20260912/s018/18_86/18_86.prose.editorial.tr.md):
  the creation association is briefly named, but the clay passages are not used
  to develop its Quranic significance. Therefore the precise problem is more
  than a completely absent dictionary association.

These observations concern the sampled passages, not every output in these
surahs. Word and heading counts describe packaging; they are not quality scores.
The saved three discovery prompts for 12:84 total 2,773,383 bytes before later
composition and consolidation. That is a measured input-size problem, not a
verified claim about billed tokens or all agents' total context consumption.

V10 consequently removes the requirement that each finding survive as its own
reader-facing item. Original findings remain reviewable, and source pointers
bring complete selected readings to the writer. Their inclusion does not by
itself establish successful synthesis. There is no per-finding coverage ledger.

## Retrieval and the interaction analogy

The useful analogue is a mechanism assembled from complementary roles. A source
of water, its storage, the device making it accessible, and its use are not
synonyms. Their relation explains something that a list of water words cannot.
The same is true of concealment, pressure, release and recognition. A rare
branch can be decisive as the part that completes the mechanism.

The existing quran-slm ensemble remains a candidate generator. V10 uses the
existing symmetric reciprocal-rank fusion: 0.35 E5, 0.35 NeoAraBERT and 0.30
character rank, offset 10. Same-root and zero-rank pairs do not become image
evidence. The default retrieves three distinct neighbouring roots for each
focus branch in the surah/Fatiha pool. This limits input transport; it does not
admit or reject interpretations. No new meaning is inferred from the score.

The critical modifications are downstream of distance:

1. Preserve a complete reviewed mechanism instead of splitting it into pairs.
2. Let separate subnetworks complete or challenge one another. Do not require
   every component to be independently salient at the focus ayah.
3. Add Quranic usage as a separate relation, including different derivatives and
   scene reuse. Rare concordances and frequent-root comparisons need different
   retrieval policies.
4. Keep identity, attributed derivation, echo, lexical image and interpretive
   inference distinct. Do not make frequency or a missing literal object a veto.

This does not prove the present distance is optimal. A future experiment can
compare retrieval channels separately, penalize generic hubs, and test whether
context-conditioned complementary-role links recover held-out image chains.
Matched background passages can test how often a putative coalition appears
without the focus context. Such controls would measure specificity; they would
not certify the interpretation as the author's unique intention. No new GNN,
Steiner-tree optimizer or biological-network algorithm is required before we
know whether the supplied mechanisms can be written well.

## Quality before expensive optimization

The first comparison should hold evidence constant and vary the synthesis
arrangement. A cheaper implementation cannot be considered a replacement merely
because it is longer, cites more ayat, or preserves more branch IDs.

| Arm | Input to writer | Question |
| --- | --- | --- |
| Direct Sol Max | Broad prepared evidence | Can Sol itself develop the main readings? |
| Luna Max → Sol Max | Brief plus complete selected original sources | What does semantic reduction gain or lose? |
| Direct Opus | Same broad evidence | What can the reference writer do with these inputs? |
| Luna Max → Opus | Same reduced packet as Sol | Is compression viable if Opus remains the synthesizer? |
| Opus brief → Sol Max | Opus brief plus originals | Is interpretive organization the expensive part? |

These are possible comparisons, not a batch to launch. First compare Sol and
Opus prose on one shared evidence packet when quota permits. Add a reduction
stage only when its contribution can be judged against that result. The local
script prepares prompts and never calls a model. The user's quota constraint
stopped new launches after two Luna map pilots. Existing cold Opus prose is a
qualitative reference, not a controlled comparison when its inputs differ.

Use calibration cases with known strengths and failure modes:

| Case | What must be examined |
| --- | --- |
| 1:2 | Weather, gathered water, well and working access as a connected image; correct lexical forms and limits |
| 12:84 | Preserve Luna's existing contained-grief/water mechanism; reduce restatement without flattening it |
| 93:3 | Turn the care-image catalogue into consequential developments of reassurance and response |
| 18:86 | Independently evaluate Quranic clay loading; keep the material and ethical boundary scenes connected |
| 29:38 | Develop sight/beautification/obstruction and dwelling/support relations without isolated keyword vetoes |
| 2:255 without HFT | Discovery quality and cost under common roots, long-surah context and no focus bundle |

Then test unseen cases, including long ayat and surahs without HFT. S1 alone is
an optimistic benchmark because its existing discoveries are unusually rich.
`no-hft` still has reviewed subnetworks and walks; `none` is a harder condition
and must be reported separately.

Human comparison should ask whether major distinct changes of understanding
survive, whether the images actually explain one another, whether the focus
stays intelligible, and whether every factual claim and Arabic comparison is
supported. A latent interpretation can be well explained without becoming the
lexical translation. Count invented meanings, incorrect forms and misleading
citations as substantive regressions. Citation quantity is diagnostic only;
each important cited passage must have a concrete role.

Record input, output, reasoning, cached tokens, elapsed time and every repair.
Compare total cost per accepted reading, including curator and failed runs.
Do not confuse smaller writer input with smaller total workflow cost. Local
decompression caching saves preparation work, not model tokens. CLI-reported
costs and API list-price equivalents do not measure subscription allowance.

## Current compromises

Local source handoffs have been checked, and two model pilots were attempted;
there is no accepted end-to-end prose result. The first 18:86 map echoed old
negative relevance verdicts about the clay passages. Those verdicts are now
removed from model input; that change has not been rerun through a model.
Removing a veto opens evaluation of a connection; it does not establish that
the connection is interpretively persuasive. The 93:3 attempt was stopped by
the assistant's 900-second runner timeout before returning a result. Its token
use is unknown. The runner and structured map requirement have since been
removed in favour of local preparation and a plain brief. Existing pilot
results therefore describe the earlier prototype, not the revised prompt.

Long-surah preparation can still be large. Bounded neighbours can miss a
complementary branch that is distant in embedding space. Complete source
subnetworks mitigate this when available. No-HFT preparation is implemented,
but comparable quality on long surahs remains unproved. These limits should be
resolved on a small benchmark before a 2,000-ayah production run.
