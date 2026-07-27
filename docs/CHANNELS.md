# Channels

A **channel** is a coherent image that runs across a surah, assembled from
branches that the primary reading does not select.

Channels are the main vehicle for the surprise this project exists to deliver,
and they are also the main disorientation risk. This document defines what a
channel is, when it may be spoken, and how layers 2 and 3 divide it between
them.

Status: specification, 2026-07-27. The maturity model is new and has not yet been
validated against a completed surah.

---

## 1. What a channel is

Membership requires all four:

1. **Lexical anchor.** Each member is a specific branch of a specific root at a
   specific `qacMorphemeRef`. A channel is never an impression about a surah; it
   is a set of citable branch activations.
2. **Non-primary.** Members are branches layer 1 did *not* select. A channel
   assembled from primary branches is a paraphrase of the translation.
3. **Coherence.** The members form one system, not one topic. Rain, water
   collection, grass, a well, and a pulley for drawing water are a system: they
   describe a working irrigation. Five words that all mention water are a topic.
4. **Explanatory yield.** The channel makes something legible that was not
   legible before — an unattached ayah attaches, a flat word becomes loaded, a
   closing turn becomes necessary rather than decorative.

A set that satisfies 1–3 and fails 4 is a **motif**. Motifs are recorded and not
rendered.

### The Fātiḥa water channel

Non-primary branches across the surah give rain, water collection, grass, a
well, and the crossbeam-and-pulley used to draw water. Together they are a
provisioning system, and `Rabb` — nurturer, sustainer — is the right name for
its agent because the surah has already named him that way. What the channel
yields: `الْعَالَمِينَ` stops being an abstract "worlds" and becomes the full extent
of what is provisioned; sustenance stops being asserted and becomes depicted.

### The Fātiḥa path channel

`na'budu` carries `mu'abbad` — a road that exists *because* it has been walked
over and over. `الْعَالَمِينَ` carries sign, landmark — waymarks. `صراط` carries a road
that does not merely run straight but takes its traveler into itself and moves
him along it. `أنعمت` carries the station where a traveler is received. `ضالين`
carries the ownerless animal that has strayed with no keeper, and being buried
and lost.

What the channel yields: the surah's second half stops being a sequence of
requests and becomes one picture — a traveler who can only move if helped, a
guide who goes ahead, signs made legible, a road made by a community's repeated
walking, and at the end the precise danger being prayed against.

### S100

Under the primary reading the running horses of the opening oath have nothing to
do with the rest of the surah. The channel is what attaches them — and because
the attachment is not visible without it, S100 is the case that makes layer 3
non-optional.

---

## 2. Maturity

A channel is not available for use the moment it is detectable. It has a
**maturity** at each point in the reading, determined by how much of it the
reader has actually been given.

| maturity | state | may be spoken |
| --- | --- | --- |
| `latent` | one member placed | no |
| `emerging` | two or more members placed and their relation is statable in one sentence | yes, as a *hint*, entered through this ayah's word |
| `mature` | enough members placed that the system's shape is visible | yes, as a *reading* |
| `complete` | all members placed | layer 3 |

Maturity is a property of a channel **at a position in the surah**, not of the
channel. The same channel is `latent` at 1:2 and `mature` at 1:7. It is computed
over the reading order, not over the evidence.

Two rules follow:

- **Availability is not permission.** That a branch is in the bundle at 1:1 does
  not license mentioning the channel at 1:1. The evidence exists all at once; the
  reader does not.
- **Maturity never runs backwards.** A channel that reached `mature` at 1:6 is
  not re-hinted at 1:7. It is extended.

---

## 3. Disclosure protocol

### Layer 2 (per ayah)

The rules below govern the case where **an adjudicated ledger exists**. No surah
has one yet. Where only the first-pass review exists, see §3.1 — maturity is
undefined there, and an undefined maturity is not a permissive one.

May mention a channel only at `emerging` or above, and then under three
constraints:

1. **Enter through this ayah's own word.** The channel is reached from a lexical
   item present here, never announced from outside. "Bu âyette yol imgesi
   sürüyor" is an announcement. "`na'budu`nun çağrıştırdığı `mu'abbad`…" is an
   entry.
2. **Say only what has matured.** Not the channel's eventual shape — its shape
   *as of here*. Withholding the rest is not a loss; it is the mechanism.
3. **Do not state the surah's thesis.** A channel increment is anchored in this
   ayah's lexis and bounded by maturity. A thesis is neither. Carrying an
   increment is permitted; carrying the thesis is the forbidden move
   (`COMMENTARY_SPEC.md` §2).

Worked example — the path channel across 1:6–1:7.

At 1:6, `emerging`. Two members are placed and their relation is one sentence:

> Yol imgesi, `na'budu` kelimesinin çağrıştırdığı `mu'abbad` — yani üzerinde
> tekrar tekrar yürüne yürüne meydana gelen yol — ile daha önce geçen yol
> işaretlerinin (`âlemîn`) birleşmesinden doğar: bir yol ve onun yolcusu
> görünür olur.

At 1:7, `mature`. `أنعمت` adds the station where the traveler is received, and
only now is the whole configuration sayable:

> `En'amte`, yolcunun vardığı ve karşılandığı konak anlamını da taşır. Böylece
> ancak yardımla yürüyebilen bir yolcuya yaratıcının önden giderek yol
> göstermesi (`mâlik`), yol işaretlerinin belirginliği (`âlemîn`), yolun bir
> topluluk tarafından yürüne yürüne açılması (`na'budu`) ve yolun yalnızca
> dosdoğru değil, yolcusunu içine alıp ilerleten bir yol oluşu (`sırât`) tek bir
> görüntüde toplanır. `Dâllîn` ise sahibi olmayan, yolunu kaybetmiş hayvan ve
> toprağa gömülüp kaybolma imgeleriyle yolcunun en büyük tehlikesini öne çıkarır
> ve duayı, neyden korunmak istendiğiyle tamamlar.

Note what the 1:7 passage does *not* do: it does not state a thesis about the
Fātiḥa, and every element it names is a word the reader has already met.

### 3.1 Before a ledger exists

Today every surah is in this state: `network/v3` review only, first-pass and
single-reader (§5.1). Maturity is not computed anywhere, so the pacing mechanism
above is unavailable.

| | layer 2 | layer 3 |
| --- | --- | --- |
| may use the review to connect words within its own scope | yes | yes |
| may name a channel as an established image of the surah | **no** | yes, marked as the writer's reading |
| may compute or assert maturity | no | no |
| emits channel candidates for adjudication | no | yes |

The asymmetry is deliberate. Layer 3's whole job is the surah as an assembly and
its output is already marked as inference; layer 2's reader meets one ayah alone,
has no way to discount a channel claim, and is the reader grounding exists to
protect (`PRINCIPLES.md` §5).

This state ends when the adjudication pass runs — `PLAN.md` action 6.

### Layer 3 (per surah)

Receives channels at `complete`. States the whole: the channel's members, the
system they form, its relation to the surah's argument, and each ayah's
contribution to it.

By the time the reader arrives, every member has already been met once, in
place, through its own ayah. Layer 3 is a recognition, not an introduction. That
is the entire reason the layer-2 seeding exists.

---

## 4. Channels and the argument are different outputs

A channel is an image running through a surah. The argument is what the surah
does as an assembly. **Both are real and they are different axes.** Neither may
stand in for the other.

The argument must rest on the primary reading: state it such that it holds with
every latent reading removed, then let channels deepen and recolour it. If
deleting the channels collapses the thesis, the thesis is not ready. This rule
exists because it was violated — a first S103 attempt built the surah level
entirely out of latent readings and explained nothing to a reader who already
knew the surah.

The inverse error is to let the argument suppress the channel. For S100 the
channel *is* the finding; a surah reading that reports only the argument has
withheld the thing worth knowing.

Layer 3 therefore emits both, distinctly. See `_surah_commentary/PROMPT.md`.

---

## 5. What exists upstream

Channels are **not** discovered in this repository. `latent_activation/network/v3`
does it deterministically — a branch-level top-k graph mined from the surah-local
SLM affinity matrix, with Qnet labels attached only *after* clustering, so the
candidates are discovery rather than classification. Generation is complete:
89,199 dense candidates and 4.16M sparse paths across 111 eligible surahs.

A blind review pass then turns candidates into readable channels, one markdown
report per surah, structured as parent channel → subchannel with `Semantic
invariant`, `Surprising reach`, `Active motifs`, `Ayah anchors`, and `Synthesis`.
110 surahs have one; S108, S110, S113, S114 do not.

**The quality is there.** Both reference channels in §1 were recovered by this
pipeline for S1, at finer resolution than the hand sketch:

> **Habitation, Water, and the Living Landscape** → *Water-Secured Encampment and
> Livelihood*: abundant fresh water `ر ب ب:B013`, water-rich well `ع ل م:B005`,
> water that secures command of camp `م ل ك:B007`, irrigation of land and people
> `غ ي ر:B001/m02` → *Sky, Rain, Wind, and Enduring Growth*

> **Movement/course** → landmark and boundary `ع ل م:B002/m02`, middle of the road
> or valley `م ل ك:B006/m01`, **paved or trodden road `ع ب د:B005/m01`**, leading
> animal followed by the group `م ل ك:B008` → swallowing `ص ر ط:B002`, burial
> `ض ل ل:B002` → *Disorientation, Forgetting, and the Stray*

The only member of the water channel not found anywhere in the corpus is the
pulley/crossbeam; `غ ي ر:B001/m02` "irrigation of land and people" is the nearest.

### 5.1 Why it is not yet a ledger

What exists is `reader_a_pilot.md` — **first-pass, single-reader** output.
`REVIEW_ORCHESTRATION.md` calls itself a prototype and lays out a staged order
(pilot S001 → calibrate on the short surahs → medium batch); what ran is the
first pass everywhere, so nothing has been adjudicated. Specifically missing:

| needed | present? |
| --- | --- |
| second reader / adjudication | no — one reader, no accept/reject |
| motif → member promotion decision | no — every motif is listed, none admitted |
| per-ayah maturity | **no** — and this is the interface to layer 2 |
| `yield` (what becomes legible) | partly — `Surprising reach` is close |
| `restsOn: primary\|latent` | no |
| machine-readable form | no — working ledgers are kept internal by instruction |
| motif identity that joins downstream | no — `mNN` is finer than `branchId` |

Until those exist, the review is **evidence, not authority**: it may inform a
writer, and it may not be rendered as an established channel
(`PRINCIPLES.md` §2). The bundle carries it with
`coverage.channel_review.review_status = "first-pass-single-reader"` so that
constraint travels with the data.

## 6. Recording

Per surah, a channel ledger holding for each channel:

- `channelId`, name, and one-sentence statement of the system;
- `members[]` — `qacMorphemeRef`, `rootId`, `branchId`, and what that member
  contributes;
- `maturityByAyah` — the maturity at each ayah in reading order, which is what
  layer 2 consults;
- `yield` — what becomes legible that was not;
- `restsOn` — `primary` or `latent`, for the argument's dependency;
- rejected candidate members, with the reason (fails coherence, fails yield);
- review state.

Until a channel is in the ledger it is a hypothesis and may not be rendered at
either layer. Network scores, activation ranks, and similarity output nominate
members; they do not admit them (`PRINCIPLES.md` §2).

---

## 7. Open

- **Maturity is unvalidated, and nothing computes it.** The four-step scale and
  the `emerging`-hint rule are a proposal from the Fātiḥa path example. No
  upstream artifact carries a per-ayah maturity column, so today it would have to
  be derived by the layer-3 writer from `Ayah anchors` in reading order. Whether
  `emerging` hints help or merely clutter needs testing against a whole surah.
- **Motif identity does not join.** The review cites `root:branch/mNN`. Only
  `root` and `branch` join to anything downstream; `mNN` is a morpheme-sense
  level that exists nowhere else in the system (`PRINCIPLES.md` §11). Either it
  gets promoted to a real identity with a crosswalk, or channel members must be
  recorded at branch granularity and the `mNN` detail treated as prose.
- **Surah-scope evidence is now partial, not absent.** The channel review is a
  genuine surah-scope artifact, so channel claims are no longer pure inference.
  The surah *argument* still is — nothing upstream evidences it — so the
  inference marking in `_surah_commentary/PROMPT.md` still applies to structural
  claims, but no longer to channel membership.
- **Four surahs have no review**: S108, S110, S113, S114.
- **Cross-surah channels** are out of scope. Whether an image running across
  surahs is the same object as a channel is unresolved.
- Whether branches with lexicon `status='review'` (e.g. `ع ص ر` B016) may serve
  as channel members is unresolved; they are currently invisible to every
  consumer.
