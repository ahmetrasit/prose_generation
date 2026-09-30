# Adversarial review of v16, r7 to r10 (2026-09-30)

Opus 5.5 subagent, read-only, run at the user's request. Its full report is summarised below in its own
structure. Verified by me before relaying:

- sentences opening with "Aile/Ailenin" on 1:6: r8 5, r9 1, r10 14 (my regex; the reviewer counted 9, 4, 15);
- "… denir": r8 13, r10 4;
- ق و م B012's packet label is "düzeneğin dik, taşıyıcı veya tutulan parçası", bundled with a sword grip and bed
  legs;
- "judged mistaken" sits in chain 9's member line (map.md:215), not in `## Not carried`.

## 1. The trajectory

- r6→r7→r8 on 1:5 (Opus): confirmed. Refs 21→7→20, author names 0→29→0. Thinking moved with the brief.
- r9's catalogue slide: confirmed, caused by "quote every family image".
- r10 is different, not better. The inventory voice moved from "sözlük" to "Aile …" as narrator. Tag density is
  near r9 (13/38 paragraphs with 3+ tags, 45 dictionary tags against r8's 16).
- r10's real syntheses:
  - "Donmayan, kaçmayan adım";
  - the hady's inviolability answering 7:16.
- r10's losses in Quran grounding: 83:6's setting, 41:30's angels, 35:35, 4:68–69, 11:56, 5:16, 22:46, 2:255.
- Ranking on 1:6: r8 ≈ r10 > r9 for prose, r10 > r8 for checkability.
- "Five proven fixes" is overstated. Only the "sözlük" ban was tested in the cell where its fault occurred.
- No same-ayah baseline for r7 on 1:6, or for r9/r10 on 1:5. The tuning set is two ayat, with one probe.

## 2. r10 line by line

**Misfiring lines:**

- "A family is never walked through …": applied at branch level. It dropped B012, the pulley, filed with hilts
  and bed legs.
- "… if it does work for a theme": circular, and an exit clause.
- "Speak of the word's family": produced "Aile söyler" as narrator.
- "not a lesson": a GPT fix; cut it for Opus.
- The ledger reason "did no work for a theme" invites tautology, and "one line per item" is ignored under
  every brief.

**Missing:** North Star progressive disclosure, which r6 had and r10 dropped.

**Proposed r10.1 (three replacements, about +15 words):**

1. "Never list a family's senses for their own sake, but judge each attested sense by what it does, not by the
   branch it is filed under. Where this ayah's words take part in a surah chain, that chain can found a theme
   here even when another ayah completes it; a chain an earlier ayah opened is recalled briefly."
2. "Show where each image comes from: the word, the usage that carries the image, quoted in Arabic, then its
   work in the theme. Report usage as what speakers called or said ("… denir"); never name a dictionary, and
   never make "the family" a speaker."
3. Ledger: "- not written: <a finding you weighed and left out> - <what it would have made visible, and why that
   did not belong here>". Plus a mechanical map-use diff in the runner, instead of writer accounting.

## 3. Open root causes

- **Pulley.** In r10 the proximate cause is brief plus dictionary display: the abstract B012 label, the bundled
  senses, and the anti-walk rule applied to the branch. r10 already had the host theme ("standing that keeps
  working"). The map is a distal cause: no interactions, although it holds «والملك الماء يكون مع المسافر» and
  «الماء ملك أمر أي يقوم به الأمر». Its 1:6 entry shows only "hangs from the beam", so even r9 read the pulley as
  a structural analogy, with water in one closing sentence.
- **1:5.** The real gap is not 7:16 but Iblīs's refusal to bow (7:11–12, 2:34, 38:75) as the pole of ع ب د B008.
  The map owns it: B008 is in no chain, and its Quran lines are bare. So does root-anchored recall.
- **Discovery.** About 20–25 refs per Opus call. The levers are the map's Quran lists (speaker and situation)
  and the reciprocal inter-ayah lists fed to the map call.
- **Ledger batching.** Owned by the pipeline: automate a map-use diff.
- **Tag glitches.** Model decoding errors. Add a check for Latin letters inside `ar:` and for transliteration
  sanity.
- **Other slips:**
  - r9's "not X but Y" containment slip;
  - r10 overclaims: the routed man as a sense of the root, 7:17's four directions forced onto two pans, soft
    chronology for 48:2;
  - r8's ملك الدابة join given without Arabic.
- **Packet.** The map is about two-thirds of the prompt; 4 of 19 chains have no 1:6 member.

## 4. The map

- **(a) Strip Not carried from the writer packet:** yes. Little effect on the pulley expected.
- **(b) Minimal map brief:**
  - yes to Interactions, whole-scene ayah entries and "fixed expression" as the only label;
  - keep Quran passages with speaker, situation and the scene-opening ayah;
  - drop the ownership verbs, or say they describe position only;
  - do not extend Not carried to dictionary branches, because of the output budget.
- **(c) Rebuild:** confounded, because it redraws all 19 chains. Read the map before any writer call, and judge
  on several probes.
- **(d) "onlar":** a nit.
- **Cost risk.** The r2 map cost $4.24 (+21% over its estimate). Keep Not carried to one line per item.
- **Optional general line:** "A chain may join a sense and its reversal as well as the parts of one scene."

## 5. Next steps

- **Step 0 (no calls):**
  - a fixed scorecard: tag density, dictionary tags per 1k, "Aile" openings, refs and how many are introduced,
    Arabic outside tags, the map-use diff, and the probes read as probes;
  - the map-use diff script;
  - the builder change for (a);
  - a label-free dictionary variant (built, not run);
  - drafts of r10.1 and the map brief.
- **Step 1:** rebuild the S1 map (~$4.2–4.8) and read it.
- **Step 2:** r10 unchanged with the new map, on 1:6 and 1:5 (~$1.3 each).
- **Step 3:** only if water/pulley is still out, r10 with the label-free dictionary on 1:6 (~$1.3).
- **Step 4:** r10.1 on 1:6 or on a new ayah (~$1.3).
- **Step 5:** the S1 surah commentary (estimate first, ~$2–3).
- **Step 6:** generalisation: an S100 map plus 100:1 before any r11.

**Division of material (progressive disclosure):**

- 1:5: Iblīs's refusal as the pride pole;
- 1:6: the ambush on the road, and the qāma drawing the water that keeps the traveller's affair standing;
- 1:7: the naʿāma crossbeam;
- the surah commentary joins them.

## 6. Where the reviewer thinks I am wrong

- the r10 integration claim (the metric was gamed by the brief's own vocabulary);
- "five proven fixes";
- "the pulley is now a map question";
- treating the follow-ups as diagnosis (one detail is confabulated);
- tuning on two ayat with one probe;
- asking the writer to itemize the map;
- never attempting the surah commentary.
