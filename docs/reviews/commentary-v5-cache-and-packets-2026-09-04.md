**V5 cache, packet readability, and QAC provenance — 2026-09-04**

This follow-up changes preparation code and instructions after `6f73a182`.
Existing agent outputs and saved prompts remain untouched. No semantic agents
were run.

QAC now streams into a local, Git-ignored SQLite cache instead of inflating the
118 MB database into Python memory and deserializing another in-memory copy.
The compressed source is hashed on each use. Cache entries are keyed by that
SHA-256, built under a per-source lock, integrity-checked, and published by
atomic replacement. Queries use read-only connections with bounded page caches.
The first use still decompresses; subsequent ayat and separate processes reuse
the disk copy. Each distinct source version occupies approximately 118 MB on
disk. `--qac-cache-dir` selects the cache location.

New scope packets are v4. They contain complete evidence records without the
generic `$v5_ref` encoding or shared-string table. Existing semantic IDs still
connect candidates, supports, branches, and context ayat. Repeated wording is
explicitly not independent corroboration. The decoder remains available for
historical v3 packets.

The earlier instrumented probes found 624 shared values and 2,193 reference
occurrences in 29:38-plus-Fatiha global, and 1,559 shared values and 5,824
reference occurrences in 73:20 global. New prompts have zero such lookups.

| Preparation | Previous peak RSS | Revised peak RSS | Previous global prompt | Revised global prompt |
| --- | ---: | ---: | ---: | ---: |
| 29:38 plus Fatiha | 470 MB | 78–87 MB | 1.859 MB | 2.228 MB |
| 73:20 | 528 MB | 164 MB | 6.017 MB | 7.236 MB |

These are local instrumented process peaks, excluding prompt-file writes;
they are not steady-state allocations. The 78 MB observation included initial
cache creation. Warm QAC projection took approximately 0.12 and 0.22 seconds
in the two full preparation probes. Timings vary with filesystem and competing
work; repeated source hashing and queries still have a cost.

Direct comparisons loaded the committed preparation implementation separately
and exercised both versions against the same real inputs. All **14
configurations / 42 lane packets** had exactly equal evidence after accounting
only for the packet version and deliberate provenance-field changes. Every
required context retained Arabic and morphology. Each of the five 29:38
configurations retained all 92 candidates and 269 connections. The larger
prompts preserve source wording locally rather than silently dropping evidence.

The additional review findings are also addressed:

- QAC provenance uses the stable logical name `qac-morphology/qac.sqlite.gz`
  and SHA-256 of the compressed source bytes. The machine-specific source path
  is no longer serialized there; missing-evidence qualifications are path-free.
- Production CLI preparation checks the source once before a batch and checks
  required context morphology before writing each focus's prompts. Failure
  prevents handoffs. Explicitly exploratory runs may use
  `--allow-missing-qac-morphology`; their results report degraded coverage and
  enumerate missing references. The production runbook forbids that override.

The code boundary review also covered simultaneous cache creation, same-size
and same-mtime source replacement, damaged/empty cache files, failed builds,
and source copies at different paths. These checks support the implementation;
they do not establish semantic quality. A fresh agent run is still needed to
evaluate complete reading, unusual connections, and preservation in prose.
