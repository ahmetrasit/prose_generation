# S87 Bible discovery — completed native turns

All 74 sessions now pass discovery validation. The [final batch report](report.md)
marks all 37 targets ready for merging: 7,664 candidate connections, comprising
3,523 image connections and 4,141 ayah connections. The 4,977 first-pass rows gained
2,687 distinct follow-up proposals. These are discovery candidates; source
verification and page authorship remain later stages.

The user approved the [three wave2 corrections](repairs-wave2.accepted.json):
`2Chron` becomes `2Chr` in two locators, and Wisdom of Solomon loses its incorrect
WLC edition prefix. Raw files, grades and explanations are preserved. The
[wave2 manifest](repairs-wave2.manifest.json) records the replacement/additional
files under `repairs-wave2/`. Both final artifact chains were reconstructed from
the immutable native-turn archive plus these files and verified against their
accepted hashes. No new model calls were needed. No S87 page authors have started.

## Native-turn checkpoint before wave2 acceptance

All 74 independent Luna/Terra max sessions have completed their two turns: 18
original r13 image sections and 19 completed augment9 ayah commentaries, with one
reader of each model per target. The second turn was the single fixed, same-session,
memory-only follow-up. Every native tool history was inspected. Reader judgments
and citation wording are proposals for the later original-source verifier.

At this earlier checkpoint, 72 sessions passed acceptance. Two completed sessions remained
partial because of three malformed follow-up locators. Their protocol histories
pass; the raw failures are preserved. The
[batch report](report.before-wave2.md) records the exact state and does not permit
merging or page writing yet. No S87 page authors have started.

The user approved [nine wave1 corrections](repairs-wave1.accepted.json), which
were applied without changing grades, explanations or raw records. Their exact
files are retained under `repairs-wave1/` and listed in its
[manifest](repairs-wave1.manifest.json). The
[three wave2 corrections](repairs-wave2.proposed.md) were a separate proposal;
their subsequent approval and acceptance are recorded above.

`completed-turns.evidence.tar.gz` contains all 74 completed job directories,
native events and tool histories, frozen prompts/packages, first-pass snapshots,
raw follow-ups, validations, acceptance/failure logs, repair records, the batch
report, and the frozen Bible-owned S87 commentary pack. The
[manifest](completed-turns.manifest.json) records every member's SHA256. Every
accepted job's artifact chain was verified before compression, and every archive
member was reread and hashed afterward. This is the immutable checkpoint before
wave2; later corrections must preserve it and add their own acceptance records.

The [original-image decision](../../DECISIONS.md) governs the surah scope. Corpus
fetching, source verification, gap handling and authorship remain later stages.
