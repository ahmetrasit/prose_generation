# Luna Max pilot run notes

This is one independent Luna Max run on the shared page `1:1` packet. The stages ran sequentially in the requested order: grammar, semantics, mapping, then assembly. All 27 paragraph IDs were returned by each discovery engine and are present in the assembled page. `completed_engines` contains all three engines. There is no lesson quota; each empty engine paragraph carries a local explanation in its raw JSON. The assembled p05 image observation was joined to p06, so p05 has no standalone display lesson.

## Counts

- Raw grammar discovery: 13 lessons; 15 empty paragraph results.
- Raw semantics discovery: 17 lessons; 10 empty paragraph results.
- Raw mapping discovery: 4 lessons; 23 empty paragraph results; 2 deferred records.
- Assembled page: 32 display lessons; 2 deferred items; level distribution L1: 2, L2: 18, L3: 12.
- Paragraph lesson counts: p01=1, p02=1, p03=2, p04=1, p05=0, p06=1, p07=1, p08=1, p09=1, p10=2, p11=1, p12=1, p13=1, p14=2, p15=1, p16=1, p17=1, p18=1, p19=1, p20=3, p21=1, p22=1, p23=2, p24=1, p25=1, p26=1, p27=1.
- Two editorial merges: the p01 mapping note into its grammar lesson, and p05’s B002 image into the p06 name-branch lesson. The absorbed full IDs are recorded in `page-output.json` and `lessons.md`.
- All display lessons use empty `reminder_ids`; wording supplies their necessary Arabic distinctions locally.

## Evidence choices and limits

- QAC identifies the focus `ism` as s-m-w. The word-specific analysis also records w-s-m as a qualified alternative for exactly `ٱسْم`; the WSM image is not presented as the verse word’s meaning. The 19:65 `samāwāt` comparison stays with its own QAC root and branch.
- For root `س م و`, reviewer notes warn that a broad source synthesis overgeneralizes some B005/B007 details. The lessons therefore quote individual B002/B005/B008 examples and restrict each statement to the cited branch phrase. The namesake/peer wording remains source-bounded.
- The Allah word analysis identifies `ء ل ه` as primary and records a `و ل ه` alternative attributed to Abu’l-Haytham. The latter is taught only as an attributed etymological proposal. Its local export has no finalized entry or reviewed gloss file, so no W-L-H root image is assigned to Allah in the verse.
- The B001 mercy branch describes tenderness/compassion together with the resulting care and good action. Its semantic profile explicitly excludes standalone `merhamet` as an explanatory gloss because it may omit the good-action result. The p20 lesson applies that exclusion to the exact one-word gloss while retaining the commentary’s broader phrase “merhametle dolu” as a contextual description. Root552’s repair flag concerns B004, not the B001/B003 branches used here.
- The p14 WSM B004 branch supports a marked, communal gathering time/place for the Arabic *mawsim al-ḥājj* phrase. The Turkish development from that sense to current “mevsim” lacks dated Turkish attestations in this packet. The p25 claim about historical narrowing of Turkish “rahmet” also lacks dated attestations. Both trajectories are deferred with exact questions; supported current branch distinctions remain displayable.
- Root001650’s source-entry review passed. The root001064 B001 aid/support branch supports p23; its repair note concerns B005 and does not govern B001. Some referenced review-response locators are absent locally; the prepared branch content and available claim-specific review scope were used instead of treating a file-level flag as a blanket rejection.

## Editorial decisions

The main withheld readings are explicit: `al-aʿlā` is not assigned the `ism` root; the w-s-m alternative for `ism` is not spread to `samāwāt`; `Raḥmān/Raḥīm` patterns are not treated as fixed semantic formulas; and the w-l-h image is not assigned to Allah as a local meaning. Turkish histories of `mevsim` and `rahmet` are deferred rather than inferred from Arabic dictionaries.

The final lessons separate grammatical form, lexical branch, and Turkish rendering where each adds an independently reusable observation. The `rahmān/rahīm` wording avoids pattern-as-meaning formulas; QAC’s root evidence, not sound resemblance, supports root comparisons. The `samiyy`, sun-`ilāhah`, and womb/kinship examples remain dictionary illustrations, clearly anchored as such. Empty raw results explain why a paragraph’s available material offered no second distinct lesson from that engine’s perspective. No ontology gap was found and no IDs were invented. No independent editorial review is claimed.
