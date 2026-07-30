# Layer 3 Surah Reading

This is the active workflow for producing a surah-wide reading from completed
ayah-level commentary and reviewed latent semantic material.

The output is not a surah summary and not a catalogue of events or lexical
fields. It should give a reader with no Arabic or linguistic training
surprising recognitions that materially change how distant parts of the surah
explain one another while leaving the primary reading intact.

The retired files directly under `_channel/` do not govern this workflow.

## Files

```text
_channel/layer3/
  prompts/
    01-discover.md
    02-review.md
    03-compose.md
  schemas/
    source-packet-v2.schema.json
    discovery-hypotheses-v1.schema.json
    system-ledger-v2.schema.json
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
    N.discovery-hypotheses.json
    N.system-ledger.json
    N.surah-reading.md
    N.surah-reading.friction.md
```

`packets/` and `inputs/` are generated mechanically. `outputs/` are agent
outputs.

## Mechanical Boundary

`build_packet.py` joins sources by fixed paths and fixed projections. It does
not call a model or discover a channel.

The canonical packet contains:

- Quran text;
- complete accepted Layer-2 prose for every ayah;
- explicit Layer-2 rejection and counterpressure sections;
- the reviewed network-v3 channel source;
- selected integration and boundary sections from the V11 final report.

V12 is not repeated because the completed Layer-2 prose already consumes it.
Routine Layer-2 evidence maps and production friction are excluded.

Network-v3 is optional. The reviewed source is
`review/reader_a_pilot.md`; raw candidates and machine families are not
substituted when it is absent. V11 is also optional and is looked up in
`quran-data` before the `latent_activation` fallback. Missing optional inputs
produce warnings and never stop the workflow.

## Stage-Specific Input

The discovery call must not be anchored by the completed Layer-2 explanation or
by prior final synthesis. `instantiate.py discover` therefore creates a
mechanical view containing only:

- Quran surface rows;
- reviewed network activation cards;
- network and Quran coverage warnings.

The activation cards are deterministic projections of the reviewed source.
They retain active motifs, ayah anchors, and source references. Review labels,
parent titles, scene descriptions, invariants, surprising reach, and prewritten
synthesis are omitted.

The complete packet is inlined only for review and composition.

## Pass 1A: Discover

The discovery agent searches the stage-specific input for every materially
distinct cross-ayah hypothesis it can see.

It does not:

- rank, merge, select, reject, or certify;
- compare against Layer-2 prose;
- produce evidence ledgers or final system names;
- target any number or length;
- prefer easily defended hypotheses over risky ones.

Each hypothesis records only its proposed operation, its
`before -> hinge -> after` reader change, participating movements, and
activation references.

It writes `N.discovery-hypotheses.json`.

## Pass 1B: Review

The review agent receives the complete packet and the blind hypotheses.

It decides which hypotheses genuinely change the reader's model, which ones
support another shift, and which ones are only primary exposition, analogy, or
unsupported construction. It may merge, absorb, narrow, or reject.

There is no desired number of systems. The review does not create filler and
does not remove an earned system to meet a count.

The ledger assigns only editorial roles:

- `render`: an independent reader shift;
- `backbone`: connective structure;
- `support`: material absorbed into another system;
- `apparatus`: relevant to review but absent from reader prose.

It writes `N.system-ledger.json`.

## Pass 3: Compose

The composer receives the complete packet and reviewed ledger. It writes one
continuous argument rather than one section per system.

The primary reading remains reachable throughout. Every secondary semantic
detail immediately returns to what it changes for the reader. Source labels,
workflow vocabulary, roots, branch IDs, and rejected predications stay out of
the prose.

It writes:

- `N.surah-reading.md`;
- `N.surah-reading.friction.md`.

There are no word, paragraph, section, or system-count targets.

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

After discovery:

```sh
python3 _channel/layer3/scripts/validate.py hypotheses \
  _channel/layer3/outputs/s100/100.discovery-hypotheses.json \
  --packet _channel/layer3/packets/s100/100.source-packet.json

python3 _channel/layer3/scripts/instantiate.py review --surah 100
```

After review:

```sh
python3 _channel/layer3/scripts/validate.py ledger \
  _channel/layer3/outputs/s100/100.system-ledger.json \
  --packet _channel/layer3/packets/s100/100.source-packet.json \
  --hypotheses _channel/layer3/outputs/s100/100.discovery-hypotheses.json

python3 _channel/layer3/scripts/instantiate.py compose --surah 100
```

After composition:

```sh
python3 _channel/layer3/scripts/validate.py publication \
  --packet _channel/layer3/packets/s100/100.source-packet.json \
  --ledger _channel/layer3/outputs/s100/100.system-ledger.json \
  --prose _channel/layer3/outputs/s100/100.surah-reading.md
```

## Acceptance

A run is acceptable when:

- optional input gaps were reported mechanically;
- discovery was blind to full Layer-2 prose and prior synthesis;
- rendered systems produce material reader-model changes rather than detailed
  primary explanation;
- rejected predications do not return as core claims or metaphors;
- removing secondary resonances still leaves the primary reading recoverable;
- the final text reads as one engaging argument rather than a catalogue.
