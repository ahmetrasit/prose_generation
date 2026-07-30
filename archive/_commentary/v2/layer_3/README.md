# Layer 3

Layer 3 consumes the compact channel registry produced by the shared compiler.
It writes complete cross-ayah image and meaning chains for one editorial
pericope.

The output unit is:

```text
{PERICOPE}.channels.prose.md
{PERICOPE}.channels.evidence.md
{PERICOPE}.channels.result.json
{PERICOPE}.channels.friction.md
```

Layer 3 may accept, merge, revise, or reject channel candidates. It must account
for every candidate and preserve the local Layer 2 findings regardless of its
channel decision.

For a long surah split into pericopes, run the shared registry reconciler before
surah-scope Layer 3. It merges channel identities across pericope boundaries
without rerunning Layer 2.
