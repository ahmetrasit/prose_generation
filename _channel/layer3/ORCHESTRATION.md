# Layer 3 Surah Reading

This is the active workflow for producing a surah-wide reading from ayah-level
commentary and latent semantic evidence.

It does not summarize the surah, choose a hidden meaning over the primary
reading, or turn candidate channels into a catalogue. Its output should let a
reader with no Arabic or linguistic training experience a small number of
surah-wide systems that change how the primary reading is understood.

This workflow was designed independently of the retired files directly under
`_channel/`.

## Directory Contract

```text
_channel/layer3/
  ORCHESTRATION.md
  prompts/
    01-discover.md
    02-review.md
    03-compose.md
  schemas/
    source-packet-v1.schema.json
    system-candidates-v1.schema.json
    system-ledger-v1.schema.json
    prose-evidence-v1.schema.json
  scripts/
    common.py
    build_packet.py
    instantiate.py
    validate.py
  packets/sNNN/
    N.source-packet.json
  inputs/sNNN/
    N.discover.prompt.md
    N.review.prompt.md
    N.compose.prompt.md
  outputs/sNNN/
    N.system-candidates.json
    N.system-ledger.json
    N.surah-reading.md
    N.surah-reading.evidence.json
    N.surah-reading.friction.md
```

`packets/` and `inputs/` are generated. `outputs/` is agent-authored.

## Governing Distinctions

### Primary reading and resonance

The ordinary reading is the floor and must remain recoverable. A secondary
semantic field may support, recolour, or reorganize that floor. It may not
replace it.

Write:

> The dust remains dust, while the word's wider field of settled matter lets
> the later overturning of hidden contents echo behind it.

Do not write:

> The dust really means water.

### Rejected predication and retained material

A rejected claim has two parts:

1. the evidence or semantic branch that made the claim thinkable;
2. the sentence that asserted what that evidence meant here.

Rejection applies to the sentence unless the source explicitly invalidates the
evidence identity itself. The branch may still contribute as structural
support, contrast, boundary, or shared operation in a larger system.

Every reused rejected claim must therefore record:

- `retainedContribution`: what remains usable;
- `prohibitedForm`: what must not be asserted;
- a non-core role in the reviewed system.

This is evidence preservation, not resurrection of the rejected reading.

### Comprehensive and reader-facing

Discovery is comprehensive. The prose is selective.

The discovery agent reads every available source and searches weak as well as
strong material. Only systems that explain one another and produce a genuine
reader shift enter the prose. The first pilot does not maintain an exhaustive
source-audit table.

### Integration and aggregation

A system is not a topic shared by several ayahs. It is an operation whose
stages make the participating ayahs newly legible.

Examples of operations:

- received force becomes directed action, then visible trace;
- nurture becomes yield, barrenness, or residue;
- accumulation becomes enclosure, then inversion and exposure;
- trace becomes testimony, then measured return.

If the members can be reordered without changing the finding, they are probably
a list rather than a system.

## Source Packet

The packet builder reads:

- Quran surface text;
- every Layer-2 prose and evidence file for the surah;
- Layer-2 index and friction files when present;
- all compacted network-v3 candidates, families, and semantic path families;
- the network-v3 reader review;
- V12 publication findings when present;
- V11 recall-first artifacts when present.

V11 lookup checks `quran-data` first and then
`../latent_activation/v11/run/sNNN/`. The fallback and every missing source are
recorded in packet coverage and printed as warnings. Missing V11, network-v3,
or V12 material never prevents a packet from being built. Layer-2 prose and
evidence plus Quran text are the minimum runnable input.

Compaction removes graph-edge duplication and bulky build diagnostics. It does
not select by score: every available network candidate, family, and semantic
path family is retained. Retrieval scores remain ordering metadata only.

Layer-2 friction is carried as production context, never as Quran evidence.

## Pass 1: Discover

The discovery agent receives only the source packet, the discovery prompt, and
the candidate schema.

It works recall-first:

1. recover the primary movement from the Layer-2 prose;
2. inventory repeated operations rather than repeated topics;
3. test whether weak and rejected-predication material gains a legitimate role
   inside a larger mechanism;
4. propose several system candidates;
5. note any missing source that materially limits discovery.

It writes `N.system-candidates.json`. It writes no reader prose.

## Pass 2: Review

The review agent receives the unchanged source packet and the discovered
candidates.

It does not choose which lexical reading is true. It tests proposed systems for:

1. primary containment;
2. recurrence across multiple ayahs;
3. explanatory order;
4. claim-scoped handling of weak and rejected material;
5. a specific whole-surah reader shift;
6. resistance to catalogue prose.

It may merge or split discovery candidates. Editorial disposition is not truth
ranking:

- `render`: carries part of the final reading;
- `backbone`: connects rendered systems without becoming a separate section;
- `support`: strengthens another system;
- `apparatus`: preserved but not verbalized.

It writes `N.system-ledger.json`. This is an interpretive working artifact, not
an exhaustive audit ledger.

## Pass 3: Compose

The composition agent receives the packet and reviewed ledger. It writes:

- one continuous `N.surah-reading.md`;
- one paragraph-addressed `N.surah-reading.evidence.json`;
- one production-only `N.surah-reading.friction.md`.

The prose begins inside the ordinary reading and creates an ordered sequence of
recognitions. It does not march ayah by ayah, announce channel names, list
roots, expose source labels, or explain the workflow.

When a word's wider semantic field matters, the prose states it in ordinary
language and immediately explains what changes for the reader. Arabic,
transliteration, grammar labels, and root terminology are optional apparatus,
not prerequisites.

## Commands

For S100:

```sh
python3 _channel/layer3/scripts/build_packet.py \
  --surah 100 \
  --layer2-dir _commentary/outputs/s100-default \
  --layer2-label default.v2.5.6-sol-high

python3 _channel/layer3/scripts/validate.py packet \
  _channel/layer3/packets/s100/100.source-packet.json

python3 _channel/layer3/scripts/instantiate.py discover --surah 100
```

After the discovery output exists:

```sh
python3 _channel/layer3/scripts/validate.py candidates \
  _channel/layer3/outputs/s100/100.system-candidates.json \
  --packet _channel/layer3/packets/s100/100.source-packet.json

python3 _channel/layer3/scripts/instantiate.py review --surah 100
```

After the reviewed ledger exists:

```sh
python3 _channel/layer3/scripts/validate.py ledger \
  _channel/layer3/outputs/s100/100.system-ledger.json \
  --packet _channel/layer3/packets/s100/100.source-packet.json \
  --candidates _channel/layer3/outputs/s100/100.system-candidates.json

python3 _channel/layer3/scripts/instantiate.py compose --surah 100
```

After composition:

```sh
python3 _channel/layer3/scripts/validate.py publication \
  _channel/layer3/outputs/s100/100.surah-reading.evidence.json \
  --packet _channel/layer3/packets/s100/100.source-packet.json \
  --ledger _channel/layer3/outputs/s100/100.system-ledger.json \
  --prose _channel/layer3/outputs/s100/100.surah-reading.md
```

## Acceptance

A completed run passes only when:

- packet generation warns about every absent optional source family;
- every rendered system spans more than one ayah;
- rejected predications are never used as core claims;
- every prose paragraph maps to reviewed systems and packet evidence;
- the prose contains no source IDs or workflow vocabulary;
- removing the secondary resonances still leaves the primary reading intact;
- the final reading produces at least one explicit before/after change in reader
  understanding that no isolated ayah commentary could produce.

## Current Scope

The workflow is immediately usable for short surahs such as S100. It does not
silently truncate long-surah packets. If a packet exceeds the model context,
add a lossless pericope inventory stage that preserves source and claim
coverage before composition.
