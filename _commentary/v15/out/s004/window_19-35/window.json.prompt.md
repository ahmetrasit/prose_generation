# Window reading

You are reading one window of the Quran (a whole short surah, or one passage of a long surah) to settle the images that run through it, before any ayah commentary is written. You write no commentary prose here; you produce the reading's record as JSON.

## Who this is for

One reader: a curious Turkish speaker with almost no Arabic grammar. Their Arabic arrives through loanwords, and those loanwords, theological ones above all, have shifted, narrowed or lost their meaning in Turkish. Canonical meanings are easy for them to find elsewhere; they are only the anchor. What this work gives them is what they cannot find elsewhere: what the Arabic words keep alive beneath the plain sense. Success: after reading, they understand the ayah and the surah better than before, and they are never disoriented.

## How a sense becomes heard

- Tafsir and translation choose one meaning; the Arabic keeps several alive at once. Other attested senses of a word's root can be heard beside the plain sense, and they often weave images that run through a surah and meet its main theme from several sides, each audible to a reader in a particular condition.
- Every attested branch of every root is open. Branches have no order. A branch is heard when something activates it: the ayah's own words, neighbouring words, words elsewhere in the surah, or a Quran passage that explains the ayah.
- The dictionary is both guard and supplier. Use the branches given (and the full entries you may read). A sense you recall that the dictionary does not attest must be marked as memory; never use it silently. No invented senses, sources, etymologies or chronology.
- Keep partial, strange and minor activations. Combine fragments across words, branches and roles. Let a completed image strengthen its weak members. Only then ask what the image shows about the plain reading. No confidence scores, no verdict on an image from one of its members.
- An image is a scene whose parts are supplied by different words. It is richer when its members fill different roles in the scene than when they repeat one role.
- Members of one scene activate one another: when several words of the window or the surah supply different parts of one scene, that coalition is itself an activation, even if no single word outside it points to the scene.
- Integration, not aggregation: the branches of one root are often facets of one concept; finding that concept is itself a finding.
- Containment: every latent reading can be said in one sentence that keeps the plain reading intact. Never "not X but Y".
- The test that matters: what does the image make perceptible in the plain reading that a paraphrase could not (more spatial, bodily, causal, relational, material, temporal, compositional)?
- Readings coexist. Never declare one correct.

## What you have (below the line)

1. The text of the window.
2. The existing chain map for this surah: channels and subchannels from an earlier machine review, each with its invariant or scene, its motifs (root:Bnnn) and where it is anchored. It is your starting point: these chains are not to be rediscovered but grounded, corrected, extended and connected. It is unranked and partly noisy. (For a few surahs it is missing; then build the images from the dictionary and the scene map.)
3. The words of the window with roots, lemmas and parts of speech.
4. The dictionary: every attested branch of every root in the window, one line each (branch | Arabic image | Arabic definition, trimmed). In a long window it lists images only: read the definition and classical phrases of a branch you use (Grep the root in the dictionary file named there). Alternative roots a word may be heard from are marked ~alt with the reason.
5. The scene map: for each concrete scene, the words of the window whose branches belong to it and the role each plays there. Mechanical and generous: use it to find members and images the chain map missed. It is not a worklist; lines it lists need not mean anything. Roles in it come from the full definitions, so a rare sense shows up here even when the dictionary line shows only the image.
6. For passages of long surahs: scenes of this window that reach elsewhere in the surah, each with at most a few far words (those adding roles the window lacks come first) and a file listing every member.
7. Variant readings.

You may read more from the paths listed at the end (full classical entries of a root, every use of a frequent lemma, the whole dictionary, the Quran text). Read only what a specific question needs; do not read in bulk.

## What to do

1. Start from the chain map. For each chain: ground it (each member is a word of this window plus a dictionary branch that carries the sense), correct it (members the dictionary does not carry, or that no word here supplies, come out), extend it (members the map missed: other words, other branches of the same words, scene lines), and connect it to the other chains. Chains that describe one scene become one image.
2. Add the images the chain map missed entirely.
3. Decide by payoff which images this window's commentary needs. A chain with nothing to make perceptible here is set aside with the reason; it is not lost.
4. Read how the images interact (one scene inside another, one agent in both, one causing or answering another) and how they converge on the window's movement and purpose.
5. Plan disclosure across the ayat, so the reader meets each image step by step.

## What to produce

- images: every image kept. For each: id (I1, I2, …); a short name; source ("chain map: <channel or subchannel title>" for each chain it grows from, joined by "; ", or "new"); the scene; its members (ref S:A:W, surface, root with spaces, branch Bnnn, role in the scene, memory true if the sense is not in the dictionary); the containment sentence; perceptible (what it makes perceptible in the plain reading); interactions with other images; movement (how it bears on the window's movement and purpose).
- concepts: roots whose branches are facets of one concept here (root, the concept, the branches it gathers).
- movement: the window's movement and purpose in a few sentences, read through the images.
- plan: one entry for every ayah of the window. opens: images whose first member becomes audible here; advances: images this ayah adds to; completes: images whose last member arrives here or that turn back on the plain sense here. At most 3 image ids per ayah across the three lists; an image not placed in an ayah stays in the record. Place each image where the text makes it most audible. note: one line on what this ayah's commentary should make perceptible.
- chains_set_aside: chains of the map you did not keep (title, why).
- other_activations: branches you heard activated that joined no image, one line each (ref, root Bnnn, what activates it).

Analysis in English; Arabic as in the text. Output only the JSON object required by the schema.

---

# Window 4:19–35 (Marriage rights and family arbitration)

## Text

4:19| يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا يَحِلُّ لَكُمْ أَن تَرِثُوا۟ ٱلنِّسَآءَ كَرْهًۭا ۖ وَلَا تَعْضُلُوهُنَّ لِتَذْهَبُوا۟ بِبَعْضِ مَآ ءَاتَيْتُمُوهُنَّ إِلَّآ أَن يَأْتِينَ بِفَٰحِشَةٍۢ مُّبَيِّنَةٍۢ ۚ وَعَاشِرُوهُنَّ بِٱلْمَعْرُوفِ ۚ فَإِن كَرِهْتُمُوهُنَّ فَعَسَىٰٓ أَن تَكْرَهُوا۟ شَيْـًۭٔا وَيَجْعَلَ ٱللَّهُ فِيهِ خَيْرًۭا كَثِيرًۭا
4:20| وَإِنْ أَرَدتُّمُ ٱسْتِبْدَالَ زَوْجٍۢ مَّكَانَ زَوْجٍۢ وَءَاتَيْتُمْ إِحْدَىٰهُنَّ قِنطَارًۭا فَلَا تَأْخُذُوا۟ مِنْهُ شَيْـًٔا ۚ أَتَأْخُذُونَهُۥ بُهْتَٰنًۭا وَإِثْمًۭا مُّبِينًۭا
4:21| وَكَيْفَ تَأْخُذُونَهُۥ وَقَدْ أَفْضَىٰ بَعْضُكُمْ إِلَىٰ بَعْضٍۢ وَأَخَذْنَ مِنكُم مِّيثَٰقًا غَلِيظًۭا
4:22| وَلَا تَنكِحُوا۟ مَا نَكَحَ ءَابَآؤُكُم مِّنَ ٱلنِّسَآءِ إِلَّا مَا قَدْ سَلَفَ ۚ إِنَّهُۥ كَانَ فَٰحِشَةًۭ وَمَقْتًۭا وَسَآءَ سَبِيلًا
4:23| حُرِّمَتْ عَلَيْكُمْ أُمَّهَٰتُكُمْ وَبَنَاتُكُمْ وَأَخَوَٰتُكُمْ وَعَمَّٰتُكُمْ وَخَٰلَٰتُكُمْ وَبَنَاتُ ٱلْأَخِ وَبَنَاتُ ٱلْأُخْتِ وَأُمَّهَٰتُكُمُ ٱلَّٰتِىٓ أَرْضَعْنَكُمْ وَأَخَوَٰتُكُم مِّنَ ٱلرَّضَٰعَةِ وَأُمَّهَٰتُ نِسَآئِكُمْ وَرَبَٰٓئِبُكُمُ ٱلَّٰتِى فِى حُجُورِكُم مِّن نِّسَآئِكُمُ ٱلَّٰتِى دَخَلْتُم بِهِنَّ فَإِن لَّمْ تَكُونُوا۟ دَخَلْتُم بِهِنَّ فَلَا جُنَاحَ عَلَيْكُمْ وَحَلَٰٓئِلُ أَبْنَآئِكُمُ ٱلَّذِينَ مِنْ أَصْلَٰبِكُمْ وَأَن تَجْمَعُوا۟ بَيْنَ ٱلْأُخْتَيْنِ إِلَّا مَا قَدْ سَلَفَ ۗ إِنَّ ٱللَّهَ كَانَ غَفُورًۭا رَّحِيمًۭا
4:24| ۞ وَٱلْمُحْصَنَٰتُ مِنَ ٱلنِّسَآءِ إِلَّا مَا مَلَكَتْ أَيْمَٰنُكُمْ ۖ كِتَٰبَ ٱللَّهِ عَلَيْكُمْ ۚ وَأُحِلَّ لَكُم مَّا وَرَآءَ ذَٰلِكُمْ أَن تَبْتَغُوا۟ بِأَمْوَٰلِكُم مُّحْصِنِينَ غَيْرَ مُسَٰفِحِينَ ۚ فَمَا ٱسْتَمْتَعْتُم بِهِۦ مِنْهُنَّ فَـَٔاتُوهُنَّ أُجُورَهُنَّ فَرِيضَةًۭ ۚ وَلَا جُنَاحَ عَلَيْكُمْ فِيمَا تَرَٰضَيْتُم بِهِۦ مِنۢ بَعْدِ ٱلْفَرِيضَةِ ۚ إِنَّ ٱللَّهَ كَانَ عَلِيمًا حَكِيمًۭا
4:25| وَمَن لَّمْ يَسْتَطِعْ مِنكُمْ طَوْلًا أَن يَنكِحَ ٱلْمُحْصَنَٰتِ ٱلْمُؤْمِنَٰتِ فَمِن مَّا مَلَكَتْ أَيْمَٰنُكُم مِّن فَتَيَٰتِكُمُ ٱلْمُؤْمِنَٰتِ ۚ وَٱللَّهُ أَعْلَمُ بِإِيمَٰنِكُم ۚ بَعْضُكُم مِّنۢ بَعْضٍۢ ۚ فَٱنكِحُوهُنَّ بِإِذْنِ أَهْلِهِنَّ وَءَاتُوهُنَّ أُجُورَهُنَّ بِٱلْمَعْرُوفِ مُحْصَنَٰتٍ غَيْرَ مُسَٰفِحَٰتٍۢ وَلَا مُتَّخِذَٰتِ أَخْدَانٍۢ ۚ فَإِذَآ أُحْصِنَّ فَإِنْ أَتَيْنَ بِفَٰحِشَةٍۢ فَعَلَيْهِنَّ نِصْفُ مَا عَلَى ٱلْمُحْصَنَٰتِ مِنَ ٱلْعَذَابِ ۚ ذَٰلِكَ لِمَنْ خَشِىَ ٱلْعَنَتَ مِنكُمْ ۚ وَأَن تَصْبِرُوا۟ خَيْرٌۭ لَّكُمْ ۗ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌۭ
4:26| يُرِيدُ ٱللَّهُ لِيُبَيِّنَ لَكُمْ وَيَهْدِيَكُمْ سُنَنَ ٱلَّذِينَ مِن قَبْلِكُمْ وَيَتُوبَ عَلَيْكُمْ ۗ وَٱللَّهُ عَلِيمٌ حَكِيمٌۭ
4:27| وَٱللَّهُ يُرِيدُ أَن يَتُوبَ عَلَيْكُمْ وَيُرِيدُ ٱلَّذِينَ يَتَّبِعُونَ ٱلشَّهَوَٰتِ أَن تَمِيلُوا۟ مَيْلًا عَظِيمًۭا
4:28| يُرِيدُ ٱللَّهُ أَن يُخَفِّفَ عَنكُمْ ۚ وَخُلِقَ ٱلْإِنسَٰنُ ضَعِيفًۭا
4:29| يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَأْكُلُوٓا۟ أَمْوَٰلَكُم بَيْنَكُم بِٱلْبَٰطِلِ إِلَّآ أَن تَكُونَ تِجَٰرَةً عَن تَرَاضٍۢ مِّنكُمْ ۚ وَلَا تَقْتُلُوٓا۟ أَنفُسَكُمْ ۚ إِنَّ ٱللَّهَ كَانَ بِكُمْ رَحِيمًۭا
4:30| وَمَن يَفْعَلْ ذَٰلِكَ عُدْوَٰنًۭا وَظُلْمًۭا فَسَوْفَ نُصْلِيهِ نَارًۭا ۚ وَكَانَ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرًا
4:31| إِن تَجْتَنِبُوا۟ كَبَآئِرَ مَا تُنْهَوْنَ عَنْهُ نُكَفِّرْ عَنكُمْ سَيِّـَٔاتِكُمْ وَنُدْخِلْكُم مُّدْخَلًۭا كَرِيمًۭا
4:32| وَلَا تَتَمَنَّوْا۟ مَا فَضَّلَ ٱللَّهُ بِهِۦ بَعْضَكُمْ عَلَىٰ بَعْضٍۢ ۚ لِّلرِّجَالِ نَصِيبٌۭ مِّمَّا ٱكْتَسَبُوا۟ ۖ وَلِلنِّسَآءِ نَصِيبٌۭ مِّمَّا ٱكْتَسَبْنَ ۚ وَسْـَٔلُوا۟ ٱللَّهَ مِن فَضْلِهِۦٓ ۗ إِنَّ ٱللَّهَ كَانَ بِكُلِّ شَىْءٍ عَلِيمًۭا
4:33| وَلِكُلٍّۢ جَعَلْنَا مَوَٰلِىَ مِمَّا تَرَكَ ٱلْوَٰلِدَانِ وَٱلْأَقْرَبُونَ ۚ وَٱلَّذِينَ عَقَدَتْ أَيْمَٰنُكُمْ فَـَٔاتُوهُمْ نَصِيبَهُمْ ۚ إِنَّ ٱللَّهَ كَانَ عَلَىٰ كُلِّ شَىْءٍۢ شَهِيدًا
4:34| ٱلرِّجَالُ قَوَّٰمُونَ عَلَى ٱلنِّسَآءِ بِمَا فَضَّلَ ٱللَّهُ بَعْضَهُمْ عَلَىٰ بَعْضٍۢ وَبِمَآ أَنفَقُوا۟ مِنْ أَمْوَٰلِهِمْ ۚ فَٱلصَّٰلِحَٰتُ قَٰنِتَٰتٌ حَٰفِظَٰتٌۭ لِّلْغَيْبِ بِمَا حَفِظَ ٱللَّهُ ۚ وَٱلَّٰتِى تَخَافُونَ نُشُوزَهُنَّ فَعِظُوهُنَّ وَٱهْجُرُوهُنَّ فِى ٱلْمَضَاجِعِ وَٱضْرِبُوهُنَّ ۖ فَإِنْ أَطَعْنَكُمْ فَلَا تَبْغُوا۟ عَلَيْهِنَّ سَبِيلًا ۗ إِنَّ ٱللَّهَ كَانَ عَلِيًّۭا كَبِيرًۭا
4:35| وَإِنْ خِفْتُمْ شِقَاقَ بَيْنِهِمَا فَٱبْعَثُوا۟ حَكَمًۭا مِّنْ أَهْلِهِۦ وَحَكَمًۭا مِّنْ أَهْلِهَآ إِن يُرِيدَآ إِصْلَٰحًۭا يُوَفِّقِ ٱللَّهُ بَيْنَهُمَآ ۗ إِنَّ ٱللَّهَ كَانَ عَلِيمًا خَبِيرًۭا

## Existing chain map (earlier machine review; the starting point: ground, correct, extend, connect; unranked, partly noisy)

### 4. Covenant Gives Intimacy Its Form (P2, 4:19-35)
invariant: Intimacy is constituted through both a binding relation and embodied access; neither operation substitutes for the other.
- Subchannel A. The Relation as Knot and Obligation: A permitted union is bound by contract, thickened into covenant, and assigned enforceable dues. | motifs: ع ق د:B002, و ث ق:B004, ن ك ح:B002, ح ل ل:B001, ف ر ض:B002 | at 4:33, 4:21, 4:22, 4:25, 4:19, 4:24
- Subchannel B. The Relation as Access and Joining: Partners pass toward one another, enter marital intimacy, and become joined within a paired relation. | motifs: ف ض و:B003, د خ ل:B002, ن ك ح:B001, ج م ع:B006, ز و ج:B002 | at 4:21, 4:23, 4:22, 4:25, 4:20

### 5. Sexual Access Enclosed and Compensated (P2, 4:19-35)
invariant: Legitimate access is protected by a boundary and accompanied by a recognized transfer rather than secret or unstructured taking.
- Subchannel A. Enclosure Against Uncontracted Spill: A prohibited kin circle and a chastity enclosure distinguish admitted intimacy from uncontracted sex and concealed companionship. | motifs: ح ر م:B011, ح ص ن:B003, ح ج ر:B001, س ف ح:B002, خ د ن:B002, ن ص ف:B006 | at 4:23, 4:24-25, 4:25
- Subchannel B. Recognized Transfer Rather Than Seizure: Property moves toward the partner as an assigned due, while taking it back or circulating wealth requires a recognized basis and mutual consent. | motifs: ء ج ر:B001, ف ر ض:B003, ء ت ي:B002, ء خ ذ:B001, ت ج ر:B001, ر ض و:B001 | at 4:24-25, 4:24, 4:20, 4:20-21, 4:29

### 6. Directional Disturbance and Household Repair (P2, 4:19-35)
invariant: Relational failure is a deviation from workable alignment; correction proceeds from identifying the tilt to separating pressure points and finally matching mediators.
- Subchannel A. Tilt Against Responsible Standing: Desire pulls a relation off line while responsible standing and apportioned obligation attempt to hold it in workable orientation. | motifs: م ي ل:B001, ق و م:B004, ف ض ل:B003, ن ص ف:B003, ب غ ي:B003 | at 4:27, 4:34, 4:32, 4:25
- Subchannel B. From Raised Resistance to Matched Mediation: Household recalcitrance produces separation at the shared bed, develops into a split between sides, and is answered by paired arbiters seeking concord. | motifs: ن ش ز:B004, ه ج ر:B001, ض ج ع:B002, ش ق ق:B004, ح ك م:B005, و ف ق:B002, ص ل ح:B002 | at 4:34, 4:35

### 7. Illicit Exchange Turns Back on the Taker (P2, 4:19-35)
invariant: When transfer loses a valid reciprocal basis, appropriation becomes self-directed destruction.
- Subchannel A. Exchange With or Without a Valid Basis: Wealth either circulates through consensual trade or is consumed through a void claim. | motifs: ء ك ل:B004, ب ط ل:B001, ت ج ر:B001, ر ض و:B001 | at 4:29
- Subchannel B. Appropriation as Self-Killing and Fire: An act against others' property returns as an act against the shared self and culminates in encounter with fire. | motifs: ق ت ل:B001, ن ف س:B011, ر ح م:B001, ع د و:B001, ظ ل م:B008, ص ل ي:B003 | at 4:29, 4:30

### standalone: S2. Obligation Scaled to Human Capacity (P2, 4:19-35)
- scene: Legal demand is adjusted to available means, feared hardship, and created weakness. | motifs: ط و ع:B003, ط و ل:B004, ع ن ت:B001, خ ف ف:B001, ض ع ف:B001, خ ل ق:B002 | at 4:25, 4:28

### standalone: S6. Marked Arrows Divide the Slaughtered Camel (Whole surah, 4:1-176)
- scene: Gaming arrows are gathered in a receptacle, managed and drawn by rank, and used to assign portions of a slaughtered camel to winner and loser. | motifs: د ب ر:B019, ر ب ب:B010, ر ق ب:B006, ن ف س:B016, ي س ر:B007, ف و ز:B001 | at 4:82, 4:1, 4:30, 4:169, 4:13, 4:73

### standalone: S7. The Bow Is Tested, Nocked, and Drawn (Whole surah, 4:1-176)
- scene: An archer checks the relation between bow and string, tests the bow's resilience, seats the string and arrow in their grooves, draws, and produces a shot. | motifs: ب ن ي:B005, ب ي ن:B008, ذ و ق:B003, ع ن ت:B006, ف و ق:B009, ن ز ع:B002, ر م ي:B003 | at 4:23, 4:94, 4:56, 4:25, 4:154, 4:59, 4:112

### standalone: S8. A Timed Watering Turn Makes Room for the Thirsty Animal (Whole surah, 4:1-176)
- scene: A herd approaches water on a scheduled turn, follows a lead animal, drinks while water is raised to its mouths, accommodates a still-thirsty camel, and departs. | motifs: ق ر ب:B008, س ل ف:B004, ق ب ل:B014, د خ ل:B007, ر ب ع:B004, ص د ر:B003 | at 4:17, 4:77, 4:22-23, 4:47, 4:23, 4:12, 4:90

### standalone: S10. Prepared Drink Moves from Mixture to Lost Sobriety (Whole surah, 4:1-176)
- scene: A beverage rests in a vessel, is reduced, stirred, diluted to break its force or allowed to sour, and can finally overpower sober awareness. | motifs: ء و ل:B010, ث ل ث:B008, خ و ض:B003, ق ت ل:B007, خ ل ل:B006, س ك ر:B001 | at 4:59, 4:11-12, 4:140, 4:29, 4:125, 4:43

### standalone: S11. Milk Flow Produces a Kinship Relation (Whole surah, 4:1-176)
- scene: Milk gathers before birth, refills and flows in intervals, is drawn by the nursing child, and makes co-nursed persons socially related. | motifs: د ف ع:B009, ر د د:B007, د ع و:B003, ر س ل:B006, ف و ق:B006, ر ض ع:B001, ر ض ع:B002 | at 4:6, 4:59, 4:117, 4:154, 4:23

### standalone: S12. Raised Plaster Makes a Fortress, Not an Escape from Death (Whole surah, 4:1-176)
- scene: Pieces are joined into a high enclosed building, fortified around an interior, and raised and finished with plaster into a conspicuous stronghold. | motifs: ب ن ي:B001, ب ر ج:B001, ج د ل:B009, ش ي د:B001, ح ص ن:B001, ق ص ر:B005 | at 4:23, 4:78, 4:107, 4:109, 4:24-25, 4:101

### standalone: S13. An Oath Is Sworn, Thickened, and Released (Whole surah, 4:1-176)
- scene: A speaker swears by the right hand, an oath may be distributed among claimants and made more stringent, and a formal release can undo its binding force. | motifs: ح ل ف:B001, ح ل ف:B002, ح ل ل:B005, غ ل ظ:B003, ق س م:B004, ي م ن:B003 | at 4:62, 4:19, 4:24, 4:21, 4:154, 4:8, 4:3, 4:24-25, 4:33, 4:36

### standalone: S14. The Final Breath Is Enclosed in a Grave-House (Whole surah, 4:1-176)
- scene: Death takes hold through bodily struggle and a last chest-breath, the life is seized, and the body is covered, buried, and lodged in a grave figured as a house. | motifs: م و ت:B001, ن ز ع:B016, ف و ق:B010, و ف ي:B002, ج ن ن:B009, غ ي ب:B009, ب ي ت:B007 | at 4:15, 4:18, 4:59, 4:154, 4:97, 4:13, 4:124, 4:34, 4:100

### standalone: S17. A Debt Follows Claim, Surety, Payment, and Discharge (P1, 4:1-18)
- scene: A creditor pursues an owned claim, liability may be formally assumed or redirected to a guarantor, payment satisfies the due, and discharge ends its pursuit. | motifs: د ي ن:B003, ح ق ق:B003, ت ب ع:B005, ح و ل:B010, ح م ل:B004, ق ب ل:B008, ق ض ي:B006, ب ر ء:B004 | at 4:11-12, 4:105, 4:27, 4:98, 4:112, 4:26, 4:65

### standalone: S23. Fire Assays Gold While Gilding Imitates It (Whole surah, 4:1-176)
- scene: Gold is tested by fire to distinguish sound metal from inferior material, while yellow metal or a thin coating can imitate gold closely enough to dazzle an observer. | motifs: ذ ه ب:B001, ذ ه ب:B002, ذ ه ب:B003, ش ب ه:B003, ف ت ن:B001, م و ه:B005 | at 4:19, 4:133, 4:157, 4:91, 4:101, 4:43

### standalone: S25. A Pot on Three Stones Is Brought to Doneness (P3, 4:36-57)
- scene: A cooking pot rests on a three-stone support over heat, a cloth protects the hand when it is lowered from the fire, and its contents reach full doneness. | motifs: ث ل ث:B007, ج ع ل:B007, ق د ر:B007, ن ض ج:B001 | at 4:11-12, 4:15, 4:19, 4:133, 4:149, 4:56

### standalone: S28. A Forward Sale Begins with Appraisal and Known Price (P2, 4:19-35)
- scene: Goods are appraised against a market price, money is advanced for deferred delivery, and a later transfer can preserve the disclosed original price. | motifs: ث م ن:B001, س ع ر:B003, س ل ف:B005, س ل م:B005, ق و م:B010, و ل ي:B014 | at 4:12, 4:10, 4:55, 4:22-23, 4:92, 4:5, 4:33

### standalone: S29. Set Work Generates an Owed Wage (P2, 4:19-35)
- scene: Laborers perform an assigned craft or task under a set fee, receive pay for the work, and may be maintained through continuing provision. | motifs: ء ج ر:B001, ج ع ل:B005, ع م ل:B004, ف ع ل:B003, ج ر ي:B006 | at 4:24-25, 4:19, 4:17, 4:30, 4:13

## Words (ref surface | root | lemma | pos)

4:19:3 ءَامَنُوا۟ | ء م ن | ءَامَنَ | V
4:19:5 يَحِلُّ | ح ل ل | حَلَلْ | V
4:19:8 تَرِثُوا۟ | و ر ث | وَرِثَ | V
4:19:9 ٱلنِّسَآءَ | ن س و | نِسَآء | N
4:19:10 كَرْهًۭا | ك ر ه | كَرْه | N
4:19:12 تَعْضُلُوهُنَّ | ع ض ل | تَعْضُلُ | V
4:19:13 لِتَذْهَبُوا۟ | ذ ه ب | ذَهَبَ | V
4:19:14 بِبَعْضِ | ب ع ض | بَعْض | N
4:19:16 ءَاتَيْتُمُوهُنَّ | ء ت ي | آتَى | V
4:19:19 يَأْتِينَ | ء ت ي | أَتَى | V
4:19:20 بِفَٰحِشَةٍۢ | ف ح ش | فَٰحِشَة | N
4:19:21 مُّبَيِّنَةٍۢ | ب ي ن | مُّبَيِّنَة | ADJ
4:19:22 وَعَاشِرُوهُنَّ | ع ش ر | عَاشِرُ | V
4:19:23 بِٱلْمَعْرُوفِ | ع ر ف | مَّعْرُوف | N
4:19:25 كَرِهْتُمُوهُنَّ | ك ر ه | كَرِهَ | V
4:19:26 فَعَسَىٰٓ | ع س ي | عَسَى | V
4:19:28 تَكْرَهُوا۟ | ك ر ه | كَرِهَ | V
4:19:29 شَيْـًۭٔا | ش ي ء | شَىْء | N
4:19:30 وَيَجْعَلَ | ج ع ل | جَعَلَ | V
4:19:31 ٱللَّهُ | ء ل ه | ٱللَّه | PN
4:19:33 خَيْرًۭا | خ ي ر | خَيْر | N
4:19:34 كَثِيرًۭا | ك ث ر | كَثِير | ADJ
4:20:2 أَرَدتُّمُ | ر و د | أَرَادَ | V
4:20:3 ٱسْتِبْدَالَ | ب د ل | ٱسْتِبْدَال | N
4:20:4 زَوْجٍۢ | ز و ج | زَوْج | N
4:20:5 مَّكَانَ | ك و ن | مَّكَان | N
4:20:6 زَوْجٍۢ | ز و ج | زَوْج | N
4:20:7 وَءَاتَيْتُمْ | ء ت ي | آتَى | V
4:20:8 إِحْدَىٰهُنَّ | ء ح د | إِحْدَى | N
4:20:9 قِنطَارًۭا | ق ن ط ر | قِنطَار | N
4:20:11 تَأْخُذُوا۟ | ء خ ذ | أَخَذَ | V
4:20:13 شَيْـًٔا | ش ي ء | شَىْء | N
4:20:14 أَتَأْخُذُونَهُۥ | ء خ ذ | أَخَذَ | V
4:20:15 بُهْتَٰنًۭا | ب ه ت | بُهْتَٰن | N
4:20:16 وَإِثْمًۭا | ء ث م | إِثْم | N
4:20:17 مُّبِينًۭا | ب ي ن | مُّبِين | ADJ
4:21:1 وَكَيْفَ | ك ي ف | كَيْف | INTG
4:21:2 تَأْخُذُونَهُۥ | ء خ ذ | أَخَذَ | V
4:21:4 أَفْضَىٰ | ف ض و | أَفْضَىٰ | V
4:21:5 بَعْضُكُمْ | ب ع ض | بَعْض | N
4:21:7 بَعْضٍۢ | ب ع ض | بَعْض | N
4:21:8 وَأَخَذْنَ | ء خ ذ | أَخَذَ | V
4:21:10 مِّيثَٰقًا | و ث ق | مِّيثَٰق | N
4:21:11 غَلِيظًۭا | غ ل ظ | غَلِيظ | ADJ
4:22:2 تَنكِحُوا۟ | ن ك ح | نَكَحَ | V
4:22:4 نَكَحَ | ن ك ح | نَكَحَ | V
4:22:5 ءَابَآؤُكُم | ء ب و | آبَاء | N
4:22:7 ٱلنِّسَآءِ | ن س و | نِسَآء | N
4:22:11 سَلَفَ | س ل ف | سَلَفَ | V
4:22:13 كَانَ | ك و ن | كَانَ | V
4:22:14 فَٰحِشَةًۭ | ف ح ش | فَٰحِشَة | N
4:22:15 وَمَقْتًۭا | م ق ت | مَقْت | N
4:22:16 وَسَآءَ | س و ء | سَآءَ | V
4:22:17 سَبِيلًا | س ب ل | سَبِيل | N
4:23:1 حُرِّمَتْ | ح ر م | حَرَّمَ | V
4:23:3 أُمَّهَٰتُكُمْ | ء م م | أُمّ | N
4:23:4 وَبَنَاتُكُمْ | ب ن ي | بَنَات | N
4:23:5 وَأَخَوَٰتُكُمْ | ء خ و | أُخْت | N
4:23:6 وَعَمَّٰتُكُمْ | ع م م | عَمَّٰت | N
4:23:7 وَخَٰلَٰتُكُمْ | خ و ل | خَٰلَٰت | N
4:23:8 وَبَنَاتُ | ب ن ي | بَنَات | N
4:23:9 ٱلْأَخِ | ء خ و | أَخ | N
4:23:10 وَبَنَاتُ | ب ن ي | بَنَات | N
4:23:11 ٱلْأُخْتِ | ء خ و | أُخْت | N
4:23:12 وَأُمَّهَٰتُكُمُ | ء م م | أُمّ | N
4:23:14 أَرْضَعْنَكُمْ | ر ض ع | أَرْضَعَتْ | V
4:23:15 وَأَخَوَٰتُكُم | ء خ و | أُخْت | N
4:23:17 ٱلرَّضَٰعَةِ | ر ض ع | رَّضَاعَة | N
4:23:18 وَأُمَّهَٰتُ | ء م م | أُمّ | N
4:23:19 نِسَآئِكُمْ | ن س و | نِسَآء | N
4:23:20 وَرَبَٰٓئِبُكُمُ | ر ب ب | رَبَٰٓئِب | N
4:23:23 حُجُورِكُم | ح ج ر | حُجُور | N
4:23:25 نِّسَآئِكُمُ | ن س و | نِسَآء | N
4:23:27 دَخَلْتُم | د خ ل | دَخَلَ | V
4:23:31 تَكُونُوا۟ | ك و ن | كَانَ | V
4:23:32 دَخَلْتُم | د خ ل | دَخَلَ | V
4:23:35 جُنَاحَ | ج ن ح | جُنَاح | N
4:23:37 وَحَلَٰٓئِلُ | ح ل ل | حَلَٰٓئِل | N
4:23:38 أَبْنَآئِكُمُ | ب ن ي | ٱبْن | N
4:23:41 أَصْلَٰبِكُمْ | ص ل ب | صُّلْب | N
4:23:43 تَجْمَعُوا۟ | ج م ع | جَمَعَ | V
4:23:44 بَيْنَ | ب ي ن | بَيْن | LOC
4:23:45 ٱلْأُخْتَيْنِ | ء خ و | أُخْت | N
4:23:49 سَلَفَ | س ل ف | سَلَفَ | V
4:23:51 ٱللَّهَ | ء ل ه | ٱللَّه | PN
4:23:52 كَانَ | ك و ن | كَانَ | V
4:23:53 غَفُورًۭا | غ ف ر | غَفُور | N
4:23:54 رَّحِيمًۭا | ر ح م | رَّحِيم | ADJ
4:24:1 وَٱلْمُحْصَنَٰتُ | ح ص ن | مُحْصَنَٰت | N
4:24:3 ٱلنِّسَآءِ | ن س و | نِسَآء | N
4:24:6 مَلَكَتْ | م ل ك | مَلَكَتْ | V
4:24:7 أَيْمَٰنُكُمْ | ي م ن | يَمِين | N
4:24:8 كِتَٰبَ | ك ت ب | كِتَٰب | N
4:24:9 ٱللَّهِ | ء ل ه | ٱللَّه | PN
4:24:11 وَأُحِلَّ | ح ل ل | أَحَلَّ | V
4:24:14 وَرَآءَ | و ر ي | وَرَآء | LOC
4:24:17 تَبْتَغُوا۟ | ب غ ي | ٱبْتَغَىٰ | V
4:24:18 بِأَمْوَٰلِكُم | م و ل | مَال | N
4:24:19 مُّحْصِنِينَ | ح ص ن | مُّحْصِنِين | N
4:24:20 غَيْرَ | غ ي ر | غَيْر | N
4:24:21 مُسَٰفِحِينَ | س ف ح | مُسَٰفِحِين | N
4:24:23 ٱسْتَمْتَعْتُم | م ت ع | ٱسْتَمْتَعَ | V
4:24:26 فَـَٔاتُوهُنَّ | ء ت ي | آتَى | V
4:24:27 أُجُورَهُنَّ | ء ج ر | أَجْر | N
4:24:28 فَرِيضَةًۭ | ف ر ض | فَرِيضَة | N
4:24:30 جُنَاحَ | ج ن ح | جُنَاح | N
4:24:33 تَرَٰضَيْتُم | ر ض و | تَرَٰضَ | V
4:24:36 بَعْدِ | ب ع د | بَعْد | N
4:24:37 ٱلْفَرِيضَةِ | ف ر ض | فَرِيضَة | N
4:24:39 ٱللَّهَ | ء ل ه | ٱللَّه | PN
4:24:40 كَانَ | ك و ن | كَانَ | V
4:24:41 عَلِيمًا | ع ل م | عَلِيم | N
4:24:42 حَكِيمًۭا | ح ك م | حَكِيم | ADJ
4:25:3 يَسْتَطِعْ | ط و ع | ٱسْتَطَاعَ | V
4:25:5 طَوْلًا | ط و ل | طَوْل | N
4:25:7 يَنكِحَ | ن ك ح | نَكَحَ | V
4:25:8 ٱلْمُحْصَنَٰتِ | ح ص ن | مُحْصَنَٰت | N
4:25:9 ٱلْمُؤْمِنَٰتِ | ء م ن | مُّؤْمِنَٰت | ADJ
4:25:12 مَلَكَتْ | م ل ك | مَلَكَتْ | V
4:25:13 أَيْمَٰنُكُم | ي م ن | يَمِين | N
4:25:15 فَتَيَٰتِكُمُ | ف ت ي | فَتَيَٰت | N
4:25:16 ٱلْمُؤْمِنَٰتِ | ء م ن | مُّؤْمِنَٰت | ADJ
4:25:17 وَٱللَّهُ | ء ل ه | ٱللَّه | PN
4:25:18 أَعْلَمُ | ع ل م | أَعْلَم | N
4:25:19 بِإِيمَٰنِكُم | ء م ن | إِيمَٰن | N
4:25:20 بَعْضُكُم | ب ع ض | بَعْض | N
4:25:22 بَعْضٍۢ | ب ع ض | بَعْض | N
4:25:23 فَٱنكِحُوهُنَّ | ن ك ح | نَكَحَ | V
4:25:24 بِإِذْنِ | ء ذ ن | إِذْن | N
4:25:25 أَهْلِهِنَّ | ء ه ل | أَهْل | N
4:25:26 وَءَاتُوهُنَّ | ء ت ي | آتَى | V
4:25:27 أُجُورَهُنَّ | ء ج ر | أَجْر | N
4:25:28 بِٱلْمَعْرُوفِ | ع ر ف | مَّعْرُوف | N
4:25:29 مُحْصَنَٰتٍ | ح ص ن | مُحْصَنَٰت | N
4:25:30 غَيْرَ | غ ي ر | غَيْر | N
4:25:31 مُسَٰفِحَٰتٍۢ | س ف ح | مُسَٰفِحَٰت | N
4:25:33 مُتَّخِذَٰتِ | ء خ ذ | مُتَّخِذ | N
4:25:34 أَخْدَانٍۢ | خ د ن | أَخْدَان | N
4:25:36 أُحْصِنَّ | ح ص ن | أَحْصَنَتْ | V
4:25:38 أَتَيْنَ | ء ت ي | أَتَى | V
4:25:39 بِفَٰحِشَةٍۢ | ف ح ش | فَٰحِشَة | N
4:25:41 نِصْفُ | ن ص ف | نِصْف | N
4:25:44 ٱلْمُحْصَنَٰتِ | ح ص ن | مُحْصَنَٰت | N
4:25:46 ٱلْعَذَابِ | ع ذ ب | عَذَاب | N
4:25:49 خَشِىَ | خ ش ي | خَشِىَ | V
4:25:50 ٱلْعَنَتَ | ع ن ت | عَنَت | N
4:25:53 تَصْبِرُوا۟ | ص ب ر | صَبَرَ | V
4:25:54 خَيْرٌۭ | خ ي ر | خَيْر | N
4:25:56 وَٱللَّهُ | ء ل ه | ٱللَّه | PN
4:25:57 غَفُورٌۭ | غ ف ر | غَفُور | N
4:25:58 رَّحِيمٌۭ | ر ح م | رَّحِيم | ADJ
4:26:1 يُرِيدُ | ر و د | أَرَادَ | V
4:26:2 ٱللَّهُ | ء ل ه | ٱللَّه | PN
4:26:3 لِيُبَيِّنَ | ب ي ن | بَيَّنُ | V
4:26:5 وَيَهْدِيَكُمْ | ه د ي | هَدَى | V
4:26:6 سُنَنَ | س ن ن | سُنَّة | N
4:26:9 قَبْلِكُمْ | ق ب ل | قَبْل | N
4:26:10 وَيَتُوبَ | ت و ب | تَابَ | V
4:26:12 وَٱللَّهُ | ء ل ه | ٱللَّه | PN
4:26:13 عَلِيمٌ | ع ل م | عَلِيم | N
4:26:14 حَكِيمٌۭ | ح ك م | حَكِيم | ADJ
4:27:1 وَٱللَّهُ | ء ل ه | ٱللَّه | PN
4:27:2 يُرِيدُ | ر و د | أَرَادَ | V
4:27:4 يَتُوبَ | ت و ب | تَابَ | V
4:27:6 وَيُرِيدُ | ر و د | أَرَادَ | V
4:27:8 يَتَّبِعُونَ | ت ب ع | ٱتَّبَعَ | V
4:27:9 ٱلشَّهَوَٰتِ | ش ه و | شَّهَوَٰت | N
4:27:11 تَمِيلُوا۟ | م ي ل | يَمِيلُ | V
4:27:12 مَيْلًا | م ي ل | مَيْل | N
4:27:13 عَظِيمًۭا | ع ظ م | عَظِيم | ADJ
4:28:1 يُرِيدُ | ر و د | أَرَادَ | V
4:28:2 ٱللَّهُ | ء ل ه | ٱللَّه | PN
4:28:4 يُخَفِّفَ | خ ف ف | خَفَّفَ | V
4:28:6 وَخُلِقَ | خ ل ق | خَلَقَ | V
4:28:7 ٱلْإِنسَٰنُ | ء ن س | إِنسَٰن | N
4:28:8 ضَعِيفًۭا | ض ع ف | ضَعِيف | N
4:29:3 ءَامَنُوا۟ | ء م ن | ءَامَنَ | V
4:29:5 تَأْكُلُوٓا۟ | ء ك ل | أَكَلَ | V
4:29:6 أَمْوَٰلَكُم | م و ل | مَال | N
4:29:7 بَيْنَكُم | ب ي ن | بَيْن | LOC
4:29:8 بِٱلْبَٰطِلِ | ب ط ل | بَٰطِل | N
4:29:11 تَكُونَ | ك و ن | كَانَ | V
4:29:12 تِجَٰرَةً | ت ج ر | تِجَٰرَة | N
4:29:14 تَرَاضٍۢ | ر ض و | تَرَاض | N
4:29:17 تَقْتُلُوٓا۟ | ق ت ل | قَتَلَ | V
4:29:18 أَنفُسَكُمْ | ن ف س | نَفْس | N
4:29:20 ٱللَّهَ | ء ل ه | ٱللَّه | PN
4:29:21 كَانَ | ك و ن | كَانَ | V
4:29:23 رَحِيمًۭا | ر ح م | رَّحِيم | N
4:30:2 يَفْعَلْ | ف ع ل | فَعَلَ | V
4:30:4 عُدْوَٰنًۭا | ع د و | عُدْوَٰن | N
4:30:5 وَظُلْمًۭا | ظ ل م | ظُلْم | N
4:30:7 نُصْلِيهِ | ص ل ي | أُصْلِي | V
4:30:8 نَارًۭا | ن و ر | نَار | N
4:30:9 وَكَانَ | ك و ن | كَانَ | V
4:30:12 ٱللَّهِ | ء ل ه | ٱللَّه | PN
4:30:13 يَسِيرًا | ي س ر | يَسِير | N
4:31:2 تَجْتَنِبُوا۟ | ج ن ب | ٱجْتَنَبُ | V
4:31:3 كَبَآئِرَ | ك ب ر | كَبِيرَة | N
4:31:5 تُنْهَوْنَ | ن ه ي | نَهَىٰ | V
4:31:7 نُكَفِّرْ | ك ف ر | كَفَّرَ | V
4:31:9 سَيِّـَٔاتِكُمْ | س و ء | سَيِّـَٔات | N
4:31:10 وَنُدْخِلْكُم | د خ ل | أُدْخِلَ | V
4:31:11 مُّدْخَلًۭا | د خ ل | مُّدْخَل | N
4:31:12 كَرِيمًۭا | ك ر م | كَرِيم | ADJ
4:32:2 تَتَمَنَّوْا۟ | م ن ي | يَتَمَنَّ | V
4:32:4 فَضَّلَ | ف ض ل | فَضَّلَ | V
4:32:5 ٱللَّهُ | ء ل ه | ٱللَّه | PN
4:32:7 بَعْضَكُمْ | ب ع ض | بَعْض | N
4:32:9 بَعْضٍۢ | ب ع ض | بَعْض | N
4:32:10 لِّلرِّجَالِ | ر ج ل | رِجَال | N
4:32:11 نَصِيبٌۭ | ن ص ب | نَصِيب | N
4:32:13 ٱكْتَسَبُوا۟ | ك س ب | ٱكْتَسَبَ | V
4:32:14 وَلِلنِّسَآءِ | ن س و | نِسَآء | N
4:32:15 نَصِيبٌۭ | ن ص ب | نَصِيب | N
4:32:17 ٱكْتَسَبْنَ | ك س ب | ٱكْتَسَبَ | V
4:32:18 وَسْـَٔلُوا۟ | س ء ل | سَأَلَ | V
4:32:19 ٱللَّهَ | ء ل ه | ٱللَّه | PN
4:32:21 فَضْلِهِۦٓ | ف ض ل | فَضْل | N
4:32:23 ٱللَّهَ | ء ل ه | ٱللَّه | PN
4:32:24 كَانَ | ك و ن | كَانَ | V
4:32:25 بِكُلِّ | ك ل ل | كُلّ | N
4:32:26 شَىْءٍ | ش ي ء | شَىْء | N
4:32:27 عَلِيمًۭا | ع ل م | عَلِيم | N
4:33:1 وَلِكُلٍّۢ | ك ل ل | كُلّ | N
4:33:2 جَعَلْنَا | ج ع ل | جَعَلَ | V
4:33:3 مَوَٰلِىَ | و ل ي | مَوَٰلِى | N
4:33:5 تَرَكَ | ت ر ك | تَرَكَ | V
4:33:6 ٱلْوَٰلِدَانِ | و ل د | وَالِد | N
4:33:7 وَٱلْأَقْرَبُونَ | ق ر ب | أَقْرَب | N
4:33:9 عَقَدَتْ | ع ق د | عَقَدَتْ | V
4:33:10 أَيْمَٰنُكُمْ | ي م ن | يَمِين | N
4:33:11 فَـَٔاتُوهُمْ | ء ت ي | آتَى | V
4:33:12 نَصِيبَهُمْ | ن ص ب | نَصِيب | N
4:33:14 ٱللَّهَ | ء ل ه | ٱللَّه | PN
4:33:15 كَانَ | ك و ن | كَانَ | V
4:33:17 كُلِّ | ك ل ل | كُلّ | N
4:33:18 شَىْءٍۢ | ش ي ء | شَىْء | N
4:33:19 شَهِيدًا | ش ه د | شَهِيد | N
4:34:1 ٱلرِّجَالُ | ر ج ل | رِجَال | N
4:34:2 قَوَّٰمُونَ | ق و م | قَوَّٰمِين | N
4:34:4 ٱلنِّسَآءِ | ن س و | نِسَآء | N
4:34:6 فَضَّلَ | ف ض ل | فَضَّلَ | V
4:34:7 ٱللَّهُ | ء ل ه | ٱللَّه | PN
4:34:8 بَعْضَهُمْ | ب ع ض | بَعْض | N
4:34:10 بَعْضٍۢ | ب ع ض | بَعْض | N
4:34:12 أَنفَقُوا۟ | ن ف ق | أَنفَقَ | V
4:34:14 أَمْوَٰلِهِمْ | م و ل | مَال | N
4:34:15 فَٱلصَّٰلِحَٰتُ | ص ل ح | صَّٰلِحَٰت | N
4:34:16 قَٰنِتَٰتٌ | ق ن ت | قَٰنِتَٰت | N
4:34:17 حَٰفِظَٰتٌۭ | ح ف ظ | حَٰفِظَٰت | N
4:34:18 لِّلْغَيْبِ | غ ي ب | غَيْب | N
4:34:20 حَفِظَ | ح ف ظ | حَفِظَ | V
4:34:21 ٱللَّهُ | ء ل ه | ٱللَّه | PN
4:34:23 تَخَافُونَ | خ و ف | خَافَ | V
4:34:24 نُشُوزَهُنَّ | ن ش ز | نُشُوز | N
4:34:25 فَعِظُوهُنَّ | و ع ظ | وَعَظْ | V
4:34:26 وَٱهْجُرُوهُنَّ | ه ج ر | ٱهْجُرْ | V
4:34:28 ٱلْمَضَاجِعِ | ض ج ع | مَضَاجِع | N
4:34:29 وَٱضْرِبُوهُنَّ | ض ر ب | ضَرَبَ | V
4:34:31 أَطَعْنَكُمْ | ط و ع | أَطَاعَ | V
4:34:33 تَبْغُوا۟ | ب غ ي | بَغَىٰ | V
4:34:35 سَبِيلًا | س ب ل | سَبِيل | N
4:34:37 ٱللَّهَ | ء ل ه | ٱللَّه | PN
4:34:38 كَانَ | ك و ن | كَانَ | V
4:34:39 عَلِيًّۭا | ع ل و | عَلِيّ | N
4:34:40 كَبِيرًۭا | ك ب ر | كَبِير | ADJ
4:35:2 خِفْتُمْ | خ و ف | خَافَ | V
4:35:3 شِقَاقَ | ش ق ق | شِقَاق | N
4:35:4 بَيْنِهِمَا | ب ي ن | بَيْن | N
4:35:5 فَٱبْعَثُوا۟ | ب ع ث | بَعَثَ | V
4:35:6 حَكَمًۭا | ح ك م | حَكَم | N
4:35:8 أَهْلِهِۦ | ء ه ل | أَهْل | N
4:35:9 وَحَكَمًۭا | ح ك م | حَكَم | N
4:35:11 أَهْلِهَآ | ء ه ل | أَهْل | N
4:35:13 يُرِيدَآ | ر و د | أَرَادَ | V
4:35:14 إِصْلَٰحًۭا | ص ل ح | إِصْلَٰح | N
4:35:15 يُوَفِّقِ | و ف ق | يُوَفِّقِ | V
4:35:16 ٱللَّهُ | ء ل ه | ٱللَّه | PN
4:35:17 بَيْنَهُمَآ | ب ي ن | بَيْن | LOC
4:35:19 ٱللَّهَ | ء ل ه | ٱللَّه | PN
4:35:20 كَانَ | ك و ن | كَانَ | V
4:35:21 عَلِيمًا | ع ل م | عَلِيم | N
4:35:22 خَبِيرًۭا | خ ب ر | خَبِير | ADJ

## Dictionary: every branch of every root (branch | image). A long window, so images only: each branch's definition and classical phrases are in /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/branches.tsv (Grep the root, e.g. "ق و م\tB012"); full entries in data/entries/

### ء م ن — 879 uses; here: 4:19:3 ءَامَنُوا۟; 4:25:9 ٱلْمُؤْمِنَٰتِ; 4:25:16 ٱلْمُؤْمِنَٰتِ; 4:25:19 بِإِيمَٰنِكُم; 4:29:3 ءَامَنُوا۟
B001 | سكون القلب في أمن وثقة
B002 | تصديق يطمئن إليه القلب
B003 | قول آمين طلبا للاستجابة

### ح ل ل — 51 uses; here: 4:19:5 يَحِلُّ; 4:23:37 وَحَلَٰٓئِلُ; 4:24:11 وَأُحِلَّ
B001 | حَلّ العقدة
B002 | حلول المكان
B003 | انحلال الحظر
B004 | حلول الوجوب
B005 | تحلة اليمين
B006 | حليل البيت
B007 | حُلّة الثياب
B008 | إحليل المخرج
B009 | إحلال اللبن
B010 | حِلّان الوليد
B011 | حلحلة الموضع
B012 | حلاحل السيد
B013 | حلال الرحل
B014 | حَلَل العرقوب
B015 | الحَلّ دهن السمسم

### و ر ث — 35 uses; here: 4:19:8 تَرِثُوا۟
B001 | انتقال ميراث من سابق إلى وارث
B002 | تمليك الشيء وإخلافه بلا عقد أو كلفة
B003 | انتقال علم أو كتاب أو فضيلة ميراثا
B004 | بقاء الوارث بعد فناء غيره ورجوع الملك إليه
B005 | إثارة جمر النار لتشتعل

### ن س و — 59 uses; here: 4:19:9 ٱلنِّسَآءَ; 4:22:7 ٱلنِّسَآءِ; 4:23:19 نِسَآئِكُمْ; 4:23:25 نِّسَآئِكُمُ; 4:24:3 ٱلنِّسَآءِ; 4:32:14 وَلِلنِّسَآءِ; 4:34:4 ٱلنِّسَآءِ
B001 | جماعة النساء

### ك ر ه — 41 uses; here: 4:19:10 كَرْهًۭا; 4:19:25 كَرِهْتُمُوهُنَّ; 4:19:28 تَكْرَهُوا۟
B001 | كراهة الشيء ومنافرة الرضا
B002 | مشقة يحملها الكاره
B003 | حمل الغير على ما يكرهه
B004 | شدة تنزل في الحرب والدهر
B005 | تصلب في الشخص والجمل
B006 | الكرهاء أعلى النقرة
B007 | أرض صلبة غليظة

### ع ض ل — 2 uses; here: 4:19:12 تَعْضُلُوهُنَّ
B001 | لحم صلب مكتنز في عصب
B002 | أمر شديد مستغلق يعيي صاحبه
B003 | داهية منكرة ضخمة الشأن
B004 | منع شديد وحبس يضيق الحق
B005 | نشوب الولد أو البيض وتعسر خروجه
B006 | ضيق وغصص بالكثرة أو الإشكال
B007 | أغصان ملتفة كثيرة
B008 | العَضَل جرذ أو ذكر فأر
B009 | عَضَل اسم قبيلة ومواضع
B010 | إعياء الراحلة من السير والعمل

### ذ ه ب — 56 uses; here: 4:19:13 لِتَذْهَبُوا۟
B001 | الذَّهَب المعدن
B002 | التذهيب والتمويه بالذَّهَب
B003 | الدَّهَش من رؤية الذَّهَب
B004 | الحُمْرَة إلى صُفْرَة
B005 | الذَّهْبَة والذِّهَاب من المطر
B006 | الذَّهَاب والمُضِيّ
B007 | المَذْهَب طريقا وموضعا وطريقة
B008 | الذَّهَب مكيالا
B009 | المَذْهَب وسوسة وشيطانا

### ب ع ض — 158 uses; here: 4:19:14 بِبَعْضِ; 4:21:5 بَعْضُكُمْ; 4:21:7 بَعْضٍۢ; 4:25:20 بَعْضُكُم; 4:25:22 بَعْضٍۢ; 4:32:7 بَعْضَكُمْ; 4:32:9 بَعْضٍۢ; 4:34:8 بَعْضَهُمْ; 4:34:10 بَعْضٍۢ
B001 | تجزئة الشيء وطائفته
B002 | البعوضة لصغرها وإيذائها

### ء ت ي — 549 uses; here: 4:19:16 ءَاتَيْتُمُوهُنَّ; 4:19:19 يَأْتِينَ; 4:20:7 وَءَاتَيْتُمْ; 4:24:26 فَـَٔاتُوهُنَّ; 4:25:26 وَءَاتُوهُنَّ; 4:25:38 أَتَيْنَ; 4:33:11 فَـَٔاتُوهُمْ
B001 | الإتيان والمجيء
B002 | الإيتاء والإعطاء
B003 | مأتى الأمر وتهيؤه
B004 | مجرى الماء وتسليك سبيله
B005 | السيل الآتي من غير البلد
B006 | الغريب الداخل في غير قومه
B007 | خروج النماء والنتاج
B008 | الإتاوة المؤداة
B009 | رجع يدي الناقة في السير
B010 | الميتاء طريق ومحاذاة
B011 | إتيان البلاء والهلاك
B012 | استئتاء الناقة
B013 | نَفاذ الرجل

### ف ح ش — 24 uses; here: 4:19:20 بِفَٰحِشَةٍۢ; 4:22:14 فَٰحِشَةًۭ; 4:25:39 بِفَٰحِشَةٍۢ
B001 | قبح ظاهر وشناعة
B002 | مجاوزة الحد والقدر
B003 | إفحاش القول والعمل
B004 | فاحشة الفجور والزنا وما يلحق بها
B005 | بخل جاوز القبح

### ب ي ن — 523 uses; here: 4:19:21 مُّبَيِّنَةٍۢ; 4:20:17 مُّبِينًۭا; 4:23:44 بَيْنَ; 4:26:3 لِيُبَيِّنَ; 4:29:7 بَيْنَكُم; 4:35:4 بَيْنِهِمَا; 4:35:17 بَيْنَهُمَآ
B001 | انفصال الشيء وافتراقه
B002 | الخلالة والوسط بين شيئين
B003 | الوصلة القائمة بين الأطراف
B004 | ظهور الشيء وانكشافه
B005 | كشف المعنى بالقول أو العلامة
B006 | بعد المسافة واتساع الفجوة
B007 | قطعة أرض تمتد في النظر
B008 | انفراج العضو أو الشيء عن ملاصقه
B009 | الحالب من جهة مخصوصة
B010 | الوقت الواقع أثناء حال أو فعل
B011 | حالة متوسطة بين طرفين
B012 | طلاق يقطع الرجعة
B013 | علامة الفراق المشؤومة

### ع ش ر — 27 uses; here: 4:19:22 وَعَاشِرُوهُنَّ
B001 | عدد العشرة
B002 | تمام التسعة بعاشر
B003 | جزء من عشرة
B004 | أخذ العشر من المال
B005 | عشرة عشرة
B006 | ورد الإبل في العاشر
B007 | حمل الناقة عشرة أشهر
B008 | نهيق بعشر ترجيعات
B009 | قطع وأعشار
B010 | طول عشر أذرع
B011 | اليوم العاشر من المحرم
B012 | مداخلة ومعاشرة
B013 | جماعة وعشيرة
B014 | شجر العشر
B015 | علامة كل عشر آيات
B016 | عشر بعد التسع
B017 | قوادم الريش

### ع ر ف — 70 uses; here: 4:19:23 بِٱلْمَعْرُوفِ; 4:25:28 بِٱلْمَعْرُوفِ
B001 | تتابع متصل كالشعر على عرف الفرس
B002 | عرف مرتفع ظاهر في الشيء
B003 | معرفة وتمييز بعد أثر أو علامة
B004 | عرف الرائحة والتطييب
B005 | معروف تستحسنه النفس والعقل والشرع
B006 | عريف يعرف القوم وتعرف به أحوالهم
B007 | عرفة وعرفات وتعريف الوقوف
B008 | تعريف الضالة والطلب حتى تعرف
B009 | اعتراف يقر أو ينقاد
B010 | نفس عروف تسكن وتصبر
B011 | عرفة قرحة في بياض الكف
B012 | عراف يدعي معرفة خفية أو خبر صنعة
B013 | معارف ظاهرة يعرف بها الوجه أو الأرض
B014 | اعرورف للشر تهيأ وتشزن

### ع س ي — 30 uses; here: 4:19:26 فَعَسَىٰٓ
B001 | رجاء القرب
B002 | الصلابة والغلظ
B003 | وَلِيُّ الشيخ وكبره
B004 | اشتداد ظلمة الليل
B005 | شمراخ النخل والبلح
B006 | رجاء عودة اللبن

### ش ي ء — 519 uses; here: 4:19:29 شَيْـًۭٔا; 4:20:13 شَيْـًٔا; 4:32:26 شَىْءٍ; 4:33:18 شَىْءٍۢ
B001 | الشيء المعلوم المخبر عنه
B001 | المشيئة
B002 | المشيئة المتعلّقة بالشيء
B002 | تشويه الخلق والوجه
B003 | حمل الشيء إلى الأمر
B003 | بعد النظر
B004 | تشويه الخلق وقبحه
B004 | الإعجاب والسرور
B005 | انجذاب النفس إلى الشيء
B005 | الاستماع
B006 | إصغاء السمع
B006 | صغار النخل
B007 | بعد النظر في الفرس
B007 | التلهف والتعجب
B008 | صغار النخل
B009 | نداء التلهف والتعجب

### ج ع ل — 346 uses; here: 4:19:30 وَيَجْعَلَ; 4:33:2 جَعَلْنَا
B001 | إحداث الشيء وصنعه
B002 | تصيير الشيء على حال
B003 | قول الشيء أو تسميته
B004 | الشروع في الفعل أو ملازمته
B005 | أجر مجعول على عمل
B006 | النخل الصغار أو القصار
B007 | خرقة إنزال القدر
B008 | دويبة الجعلان
B009 | اشتهاء الأنثى للفحل
B010 | فرخ النعام
B011 | الجَعْلة اسم مكان
B012 | قصر مع سمن ولجاج

### ء ل ه — 2851 uses; here: 4:19:31 ٱللَّهُ; 4:23:51 ٱللَّهَ; 4:24:9 ٱللَّهِ; 4:24:39 ٱللَّهَ; 4:25:17 وَٱللَّهُ; 4:25:56 وَٱللَّهُ; 4:26:2 ٱللَّهُ; 4:26:12 وَٱللَّهُ; 4:27:1 وَٱللَّهُ; 4:28:2 ٱللَّهُ; 4:29:20 ٱللَّهَ; 4:30:12 ٱللَّهِ; 4:32:5 ٱللَّهُ; 4:32:19 ٱللَّهَ; 4:32:23 ٱللَّهَ; 4:33:14 ٱللَّهَ; 4:34:7 ٱللَّهُ; 4:34:21 ٱللَّهُ; 4:34:37 ٱللَّهَ; 4:35:16 ٱللَّهُ; 4:35:19 ٱللَّهَ
B001 | التعبد والمعبود
B002 | اسم الله في القسم والنداء

### و ل ه ~alt (documented alternative analysis) — 0 uses; here: 4:19:31 ٱللَّهُ; 4:23:51 ٱللَّهَ; 4:24:9 ٱللَّهِ; 4:24:39 ٱللَّهَ; 4:25:17 وَٱللَّهُ; 4:25:56 وَٱللَّهُ; 4:26:2 ٱللَّهُ; 4:26:12 وَٱللَّهُ; 4:27:1 وَٱللَّهُ; 4:28:2 ٱللَّهُ; 4:29:20 ٱللَّهَ; 4:30:12 ٱللَّهِ; 4:32:5 ٱللَّهُ; 4:32:19 ٱللَّهَ; 4:32:23 ٱللَّهَ; 4:33:14 ٱللَّهَ; 4:34:7 ٱللَّهُ; 4:34:21 ٱللَّهُ; 4:34:37 ٱللَّهَ; 4:35:16 ٱللَّهُ; 4:35:19 ٱللَّهَ
B001 | الوَلَه والحيرة
B002 | تَوْلِيه الوالدة عن ولدها
B003 | ماء مُولَه ذاهب
B004 | المُولَه العنكبوت

### خ ي ر — 196 uses; here: 4:19:33 خَيْرًۭا; 4:25:54 خَيْرٌۭ
B001 | الميل إلى الخير النافع
B002 | فضل الصلاح والاصطفاء
B003 | طلب الخير بالاختيار والاستخارة
B004 | المال المسمى خيرا
B005 | الكرم والهبة
B006 | استدراج الحيوان من جحره

### ك ث ر — 167 uses; here: 4:19:34 كَثِيرًۭا
B001 | الكثرة ونماء العدد
B002 | المكاثرة والغلبة بالعدد
B003 | كثرة في صاحب أو كلام أو مطالب
B004 | الكوثر: خير كثير وفيض مخصوص
B005 | كوثر الغبار وتكوثره
B006 | الكثر جمار النخل
B007 | الكمثرة اجتماع الشيء

### ر و د — 148 uses; here: 4:20:2 أَرَدتُّمُ; 4:26:1 يُرِيدُ; 4:27:2 يُرِيدُ; 4:27:6 وَيُرِيدُ; 4:28:1 يُرِيدُ; 4:35:13 يُرِيدَآ
B001 | الإرادة والمشيئة
B002 | المراودة على الفعل
B003 | طلب الشيء وارتياده
B004 | التردد والاختلاف جيئة وذهابا
B005 | الرفق والمهل
B006 | أدوات الإدارة والدوران
B007 | عوار العين الرائد
B008 | الجارية الرود الشابة

### ب د ل — 44 uses; here: 4:20:3 ٱسْتِبْدَالَ
B001 | قيام شيء مقام شيء آخر
B002 | تغيير صورة الشيء
B003 | لحم الصدر
B004 | وجع اليدين والرجلين
B005 | بائع المأكولات

### ز و ج — 81 uses; here: 4:20:4 زَوْجٍۢ; 4:20:6 زَوْجٍۢ
B001 | قرين يضم إلى قرينه
B002 | زوج النكاح
B003 | جعل الشيء قرينا لآخر
B004 | لون أو صنف من أصناف الشيء
B005 | أشباه وقرناء يجمعهم شكل أو عمل
B006 | نمط يلقى على الهودج

### ك و ن — 1390 uses; here: 4:20:5 مَّكَانَ; 4:22:13 كَانَ; 4:23:31 تَكُونُوا۟; 4:23:52 كَانَ; 4:24:40 كَانَ; 4:29:11 تَكُونَ; 4:29:21 كَانَ; 4:30:9 وَكَانَ; 4:32:24 كَانَ; 4:33:15 كَانَ; 4:34:38 كَانَ; 4:35:20 كَانَ
B001 | وقوع الشيء وحضوره في زمان
B002 | المكان والمكانة من الكون
B003 | الكفالة والقيام على فلان
B004 | الخضوع بالاستكانة
B005 | الشيخ المنسوب إلى كُنْتُ
B006 | حالة السوء بكينة

### ء ح د — 85 uses; here: 4:20:8 إِحْدَىٰهُنَّ
B001 | الأَحَدِيَّة والوَحْدَة
B002 | استغراق النفي
B003 | الواحد في العد والتركيب
B004 | الأول والإضافة
B005 | الانفراد والتفرق آحادا
B006 | جبل أُحُد

### ق ن ط ر — 4 uses; here: 4:20:9 قِنطَارًۭا
B001 | القَنطرة المعروفة
B002 | القِنطار مقدار من ذهب أو فضة
B003 | قنطور وقنطوراء أسماء نسب

### ء خ ذ — 273 uses; here: 4:20:11 تَأْخُذُوا۟; 4:20:14 أَتَأْخُذُونَهُۥ; 4:21:2 تَأْخُذُونَهُۥ; 4:21:8 وَأَخَذْنَ; 4:25:33 مُتَّخِذَٰتِ
B001 | حوز الشيء وتناوله
B002 | المؤاخذة بالذنب
B003 | القبض والأسر
B004 | رقية تمسك وتحبس
B005 | أرض مأخوذة للنفس
B006 | موضع يمسك الماء
B007 | حال تأخذ في الجسم
B008 | أخذ القمر في منازله
B009 | الأخذ بالسيرة والشكل
B010 | الاتخاذ والاكتساب
B011 | أخذة المصارعة
B012 | مقبض الشيء المأخوذ به

### ب ه ت — 8 uses; here: 4:20:15 بُهْتَٰنًۭا
B001 | الدهش والحيرة حتى الانقطاع
B002 | الكذب الذي يبهت صاحبه أو سامعه

### ء ث م — 48 uses; here: 4:20:16 وَإِثْمًۭا
B001 | البطء والتأخر عن الخير
B002 | التأثم كف عن الإثم
B003 | الأثام عقوبة الإثم
B004 | تحميل الإثم وعده عليه
B005 | الإثم اسما للخمر

### ك ي ف — 83 uses; here: 4:21:1 وَكَيْفَ
(no branches in the dictionary)

### ف ض و — 1 uses; here: 4:21:4 أَفْضَىٰ
B001 | الفضاء المتسع
B002 | الإفضاء إلى الشيء
B003 | الإفضاء الزوجي
B004 | إفضاء المسلكين
B005 | الفَضا المختلط
B006 | الفَضا بلا حافظ
B007 | الإفضاء إلى الفقر
B008 | إفضاء الفم

### و ث ق — 34 uses; here: 4:21:10 مِّيثَٰقًا
B001 | الثقة والسكون إلى المعتمد
B002 | الإحكام والوثاقة
B003 | الإيثاق والوثاق الذي يشد به
B004 | الميثاق والعهد المؤكد

### غ ل ظ — 13 uses; here: 4:21:11 غَلِيظًۭا
B001 | ثخانة الجسم بعد رقة
B002 | خشونة وشدة في القول أو المعاملة
B003 | تشديد اليمين أو الحكم

### ن ك ح — 23 uses; here: 4:22:2 تَنكِحُوا۟; 4:22:4 نَكَحَ; 4:25:7 يَنكِحَ; 4:25:23 فَٱنكِحُوهُنَّ
B001 | البضاع والوطء
B002 | عقد الزوجية والتزوج
B003 | إيقاع التزويج للغير
B004 | الانتساب بالزوجية والكون ذا زوج
B005 | صيغة الخطبة والقبول بقول نكح
B006 | كثرة النكاح وشدته
B007 | تزويج تدفع إليه علة أو ظرف
B008 | اعتماد الشيء وغلبته على موضع

### ء ب و — 117 uses; here: 4:22:5 ءَابَآؤُكُم
B001 | الأبوة والتربية
B002 | خطاب الأب ومثله
B003 | داء الأَبْواء

### س ل ف — 8 uses; here: 4:22:11 سَلَفَ; 4:23:49 سَلَفَ
B001 | التقدم والسبق
B002 | السلافة والخلاصة الأولى
B003 | السلفة قبل الطعام
B004 | السلوف في أوائل الإبل
B005 | المال المقدم
B006 | سلف المصاهرة
B007 | السالفة من العنق
B008 | السلف الجراب
B009 | السلف القلفة
B010 | الأرض المسلوفة
B011 | سلفان الحجل
B012 | المرأة المسلف
B013 | السلفة بطانة الخف
B014 | السلوف من النصال

### م ق ت — 6 uses; here: 4:22:15 وَمَقْتًۭا
B001 | بغض شديد لقبيح
B002 | نكاح المَقْت

### س و ء — 167 uses; here: 4:22:16 وَسَآءَ; 4:31:9 سَيِّـَٔاتِكُمْ
B001 | القبح والرداءة
B002 | المساءة وما يسوء
B003 | الآفة والبرص
B004 | السوأة المستورة
B005 | التسوئة والعيب
B006 | ساء بمعنى بئس

### س ب ل — 176 uses; here: 4:22:17 سَبِيلًا; 4:34:35 سَبِيلًا
B001 | طريق ممتد يسلك
B002 | أهل الطريق وسالكوه
B003 | مال مجعول في طريق البر
B004 | إرخاء من علو إلى سفل
B005 | مطر سابل بين السحاب والأرض
B006 | شعر منسدل عند الفم واللحية
B007 | حافة أو مخرج متقدم
B008 | سنبلة الزرع الممتدة
B009 | قدح الميسر المسمى المسبل
B010 | غشاوة في العين تشبه النسج

### ح ر م — 83 uses; here: 4:23:1 حُرِّمَتْ
B001 | المنع والتحريم
B002 | التشديد ومنع اللين
B003 | الحرم والحريم المكاني
B004 | الإحرام بالنسك
B005 | الشهر الحرام والسلم الزمني
B006 | الحرمة والذمة والحق
B007 | الغلبة في القمار كمنع للطمع
B008 | الحرمان وفوات المطلوب
B009 | محارم الليل
B010 | الحريم ثوب المتنسك
B011 | المحارم والقرابة والنساء
B012 | الحِرمة شهوة الفحل
B013 | حرام الله يمين

### ء م م — 119 uses; here: 4:23:3 أُمَّهَٰتُكُمْ; 4:23:12 وَأُمَّهَٰتُكُمُ; 4:23:18 وَأُمَّهَٰتُ
B001 | الأم الوالدة والمربية
B002 | الأم أصلا وجامعا ومرجعا
B003 | أم الدماغ وما يصيبه
B004 | الأمة جماعة أو نوعا
B005 | الأمة دينا وطريقة
B006 | القامة والهيئة
B007 | الأمي على الجبلة غير الكاتب
B008 | الأمة حينا وزمانا
B009 | الإمام ومن يقتدى به
B010 | الإمة نعمة
B011 | الأمام قدام وقربا
B012 | القصد والتوجه والتيمم
B013 | الأمم اليسير الحقير
B014 | الأمة الوليدة
B015 | الأمة أو الآمة عيبا
B016 | أم حرف استفهام وإضراب

### ب ن ي — 184 uses; here: 4:23:4 وَبَنَاتُكُمْ; 4:23:8 وَبَنَاتُ; 4:23:10 وَبَنَاتُ; 4:23:38 أَبْنَآئِكُمُ
B001 | بناء الشيء بضم بعضه إلى بعض
B002 | البِنْية والهيئة المركبة
B003 | البِنْية للبيت الحرام ومكة
B004 | المَبْناة بيت أو غطاء من أدم
B005 | قوس بانية تلصق بوترها
B006 | بناء الرجل على أهله ودخوله بها
B007 | البُنُوَّة والنسب وما ينسب إلى منشأ
B008 | تسميات الابن والبنت للأشياء المتفرعة أو الصغيرة
B009 | البَواني أضلاع ودعائم يستقر بها الشيء
B010 | بناء الطعام للحم ونماؤه

### ب ن و ~alt (documented alternative analysis) — 0 uses; here: 4:23:4 وَبَنَاتُكُمْ; 4:23:8 وَبَنَاتُ; 4:23:10 وَبَنَاتُ; 4:23:38 أَبْنَآئِكُمُ
B001 | شيء يتولد عن شيء
B002 | ابن كذا: لقب لما يلابس شيئا أو يختص به

### ء خ و — 96 uses; here: 4:23:5 وَأَخَوَٰتُكُمْ; 4:23:9 ٱلْأَخِ; 4:23:11 ٱلْأُخْتِ; 4:23:15 وَأَخَوَٰتُكُم; 4:23:45 ٱلْأُخْتَيْنِ
B001 | الأخوّة والقرابة
B002 | الآخِيّة والرباط
B003 | التحرّي والقصد

### ع م م — 5 uses; here: 4:23:6 وَعَمَّٰتُكُمْ
B001 | قرابة الأب
B002 | عمامة الرأس والسيادة
B003 | سمة الرأس كالعمامة
B004 | الطول والتمام
B005 | الشمول والجماعة
B006 | رغوة كالعمامة
B007 | العُمية والعلو
B008 | الصميم الخالص
B009 | معبر من عيدان
B010 | الشخص البادي

### خ و ل — 8 uses; here: 4:23:7 وَخَٰلَٰتُكُمْ
B001 | التعهد والرعاية
B002 | الإعطاء والتمليك
B003 | الحشم والعبيد والنعم
B004 | الخؤولة والأخوال
B005 | الخَال شامة سوداء
B006 | الخَال ثوب أو خرقة معلقة
B007 | الخَال لواء الجيش
B008 | التفرق أخول أخول
B009 | الخَال في الدابة عرج أو غمز
B010 | توسم الخير في الإنسان
B011 | المخالفة في خالاني فلان

### ر ض ع — 11 uses; here: 4:23:14 أَرْضَعْنَكُمْ; 4:23:17 ٱلرَّضَٰعَةِ
B001 | مص اللبن من الثدي أو الضرع
B002 | صلة الرضاعة التي تقوم مقام القرابة
B003 | لؤم من يرضع ماشيتَه سرا
B004 | أسنان يشرب عليها الرضيع
B005 | صغار النخل

### ر ب ب — 980 uses; here: 4:23:20 وَرَبَٰٓئِبُكُمُ
B001 | ربوبية وملك وسيادة
B002 | إصلاح وتربية وإتمام
B003 | علم رباني
B004 | ربة وجماعات كثيرة
B005 | ربيب وربيبة ورابة
B006 | رُبّ خاثر وإصلاح به
B007 | لزوم وإقامة ودوام
B008 | رباب السحاب
B009 | شاة رُبّى وحداثة
B010 | ربابة تجمع القداح
B011 | ربابة عهد وميثاق
B012 | ربة نبات
B013 | ماء رَبَب كثير
B014 | رَبْرَب قطيع
B015 | حرف رب وربما
B016 | رُبَى حاجة وعقدة ونعمة
B017 | رباني الملاحين

### ح ج ر — 21 uses; here: 4:23:23 حُجُورِكُم
B001 | المنع والإحاطة
B002 | العقل الحاجز
B003 | الحَجَر الصلب
B004 | المكان المحوط
B005 | الحِجر والحضن
B006 | الدائرة حول الشيء
B007 | الفرس الأنثى المصونة

### د خ ل — 126 uses; here: 4:23:27 دَخَلْتُم; 4:23:32 دَخَلْتُم; 4:31:10 وَنُدْخِلْكُم; 4:31:11 مُّدْخَلًۭا
B001 | الولوج إلى داخل
B002 | الإفضاء الزوجي
B003 | الباطن والسريرة
B004 | فساد مستبطن
B005 | دخيل يخالط القوم أو الأمر
B006 | ما يدخل من كسب
B007 | إدخال الإبل في الشرب مرة أخرى
B008 | تداخل الأجزاء وما بين الداخل
B009 | طائر يدخل الغيران والشجر
B010 | دوخلة الخوص للرطب

### ج ن ح — 34 uses; here: 4:23:35 جُنَاحَ; 4:24:30 جُنَاحَ
B001 | الميل إلى ناحية أو جهة
B002 | الجناح جانبا ويدا وكنفا
B003 | الجناح ميل إلى الإثم
B004 | جنح الليل وإقباله
B005 | الجوانح أضلاع الصدر
B006 | السرعة كأنها بأجنحة
B007 | الاعتماد والانكباب بالجسد

### ص ل ب — 8 uses; here: 4:23:41 أَصْلَٰبِكُمْ
B001 | الشدة والصلابة
B002 | الظهر والفقار
B003 | الحمى الصالب
B004 | ودك العظم
B005 | الصلب للقتل
B006 | علامة الصليب
B007 | الحسب والعراقة

### ج م ع — 129 uses; here: 4:23:43 تَجْمَعُوا۟
B001 | ضم المتفرق حتى يصير شيئا مجموعا
B002 | جماعة اجتمعت أو أخلاط ضمتها الجهة
B003 | عزم محكم جمع الرأي بعد تفرقه
B004 | موضع أو يوم أو نداء يجمع الناس
B005 | قبضة الكف إذا ضمت الأصابع
B006 | اتصال الجماع والمجامعة
B007 | حال المرأة أو الأنثى التي بقي حملها أو عذرها معها
B008 | القيد الذي يجمع اليدين إلى العنق
B009 | اكتمال الشيء كله بلا تفرق أو نقص
B010 | استجماع القوة أو السير حتى تتلاحق أجزاؤه
B011 | نخل دقل اجتمع من النوى لا يعرف اسمه
B012 | عظم الشيء كأنه جامع ممتلئ
B013 | ممالأة واجتماع مع غيرك على أمر

### غ ف ر — 234 uses; here: 4:23:53 غَفُورًۭا; 4:25:57 غَفُورٌۭ
B001 | ستر يصون الشيء ويغطيه
B002 | ستر الذنب وصون صاحبه من أثره
B003 | زئبر أو شعر يغطي السطح
B004 | نكس المرض أو الجرح
B005 | ولد الأروية وأمه
B006 | منزل قمري من ثلاثة أنجم
B007 | مغافير الشجر الحلوة
B008 | جماء الغفير: الجماعة كلها

### ر ح م — 339 uses; here: 4:23:54 رَّحِيمًۭا; 4:25:58 رَّحِيمٌۭ; 4:29:23 رَحِيمًۭا
B001 | الرَّحْمَة والرقة
B002 | الرَّحِم والقرابة
B003 | رَحِم الأنثى
B004 | وجع الرَّحِم بعد الولادة

### ح ص ن — 18 uses; here: 4:24:1 وَٱلْمُحْصَنَٰتُ; 4:24:19 مُّحْصِنِينَ; 4:25:8 ٱلْمُحْصَنَٰتِ; 4:25:29 مُحْصَنَٰتٍ; 4:25:36 أُحْصِنَّ; 4:25:44 ٱلْمُحْصَنَٰتِ
B001 | حفظ داخل حصن محيط
B002 | عفة الفرج المحفوظة
B003 | إحصان بعقد أو حرمة
B004 | حصان الخيل الحامي أو الممسك

### م ل ك — 206 uses; here: 4:24:6 مَلَكَتْ; 4:25:12 مَلَكَتْ
B001 | قوة الشيء وتماسكه
B002 | المِلْك والتصرف
B003 | المُلك والسلطان
B004 | الإملاك والتزويج
B005 | مِلاك الأمر وعِماده
B006 | مَلَك الطريق والوادي
B007 | الماء مَلَك الأمر
B008 | المتقدم القائد في الحيوان
B009 | المَلَك من الملائكة

### ي م ن — 71 uses; here: 4:24:7 أَيْمَٰنُكُمْ; 4:25:13 أَيْمَٰنُكُم; 4:33:10 أَيْمَٰنُكُمْ
B001 | اليمن والبركة
B002 | اليد اليمنى والجهة اليمنى
B003 | يمين الحلف
B004 | يمين القوة والحق
B005 | اليمن البلد والانتساب
B006 | ملك اليمين وعقده
B007 | التيمن الموت

### ك ت ب — 319 uses; here: 4:24:8 كِتَٰبَ
B001 | ضم شيء إلى شيء
B002 | نظم الحروف واسم المكتوب
B003 | إثبات يوجب حكما أو قدرا
B004 | إدخال الاسم في سجل أو زمرة
B005 | مكاتبة العبد على عتقه

### و ر ي — 32 uses; here: 4:24:14 وَرَآءَ
B001 | داء يأكل الجوف أو يصيب الرئة
B002 | نار كامنة تخرج من الزند
B003 | زند يقدح نجاحا أو نصرة
B004 | شحم وار وسمن ظاهر
B005 | ستر الشيء وجعله وراء الظهور
B006 | الجانب الوراء: خلف أو أمام أو سوى
B007 | ولد الولد يأتي من وراء الابن
B008 | الورى: الخلق على ظهر الأرض
B009 | استيراء زند الضلالة

### ب غ ي — 96 uses; here: 4:24:17 تَبْتَغُوا۟; 4:34:33 تَبْغُوا۟
B001 | طلب الشيء وابتغاؤه
B002 | الانبغاء والمطاوعة لما يليق أو يتيسر
B003 | تجاوز الحد بالعدوان والظلم
B004 | فساد الجرح وتجاوزه
B005 | البغاء والفجور الجنسي
B006 | شدة المطر ومعظمه
B007 | اختيال الفرس ومرحه في العدو
B008 | البغايا الطلائع

### م و ل — 86 uses; here: 4:24:18 بِأَمْوَٰلِكُم; 4:29:6 أَمْوَٰلَكُم; 4:34:14 أَمْوَٰلِهِمْ
B001 | اتخاذ المال وكثرته
B002 | المُولة العنكبوت

### غ ي ر — 154 uses; here: 4:24:20 غَيْرَ; 4:25:30 غَيْرَ
B001 | الصلاح والمنفعة بالميرة والسقي والإصلاح
B002 | الغَيْر في الدية
B003 | تغيير الصورة أو إبدال الشيء بغيره
B004 | الغَيْرة على الأهل
B005 | السوى والخلاف والاستثناء والنفي

### س ف ح — 4 uses; here: 4:24:21 مُسَٰفِحِينَ; 4:25:31 مُسَٰفِحَٰتٍۢ
B001 | صب السائل وإراقته
B002 | سفاح بلا عقد
B003 | سفح الجبل
B004 | السفيح القدح الذي لا نصيب له
B005 | السفيحان كالجوالقين
B006 | السفيح الكساء الغليظ
B007 | سعة في الإبط والضلوع
B008 | رجل سفاح للكلام

### م ت ع — 70 uses; here: 4:24:23 ٱسْتَمْتَعْتُم
B001 | منفعة يتلذذ بها وينتفع بها
B002 | امتداد وارتفاع يبلغ غايته
B003 | شيء ينتفع به في الحوائج والبلاغ
B004 | عطاء المطلقة لتنتفع به
B005 | استمتاع النكاح والمتعة المؤجلة
B006 | انتفاع العمرة إلى الحج
B007 | إبقاء ممتد ليستمتع به
B008 | بلوغ الجودة أو الزيادة أو القوة
B009 | الذهاب بالشيء والاستغناء عنه

### ء ج ر — 108 uses; here: 4:24:27 أُجُورَهُنَّ; 4:25:27 أُجُورَهُنَّ
B001 | جزاء العمل والكراء
B002 | جبر الكسر على عوج
B003 | سطح بلا سترة

### ف ر ض — 18 uses; here: 4:24:28 فَرِيضَةًۭ; 4:24:37 ٱلْفَرِيضَةِ
B001 | أثر الحز والقطع في الشيء
B002 | إلزام محدد بحد معلوم
B003 | عطاء مقدر وموسوم
B004 | فرضة الماء والطرف المفتوح
B005 | اسم لشيء مقطوع الجوانب
B006 | كبر السن والجسم
B007 | تمر الفَرْض
B008 | خلو البدن من الستر
B009 | قراءة الجزء

### ر ض و — 73 uses; here: 4:24:33 تَرَٰضَيْتُم; 4:29:14 تَرَاضٍۢ
B001 | الرضا خلاف السخط
B002 | الرضوان والمرضاة اسم للرضا الكثير أو المطلوب
B003 | المراضاة والتراضي رضا متبادل
B004 | الإرضاء طلب رضا الغير وإزالة سخطه
B005 | راضاني فرضوته غلبة في ذلك
B006 | الرضي صفة للمطيع أو المحب أو الضامن
B007 | رضوى ورضيا أعلام من المادة

### ب ع د — 235 uses; here: 4:24:36 بَعْدِ
B001 | البعد عن القرب
B002 | البعد بعد القبل
B003 | إحداث البعد والمباعدة
B004 | البعد هلاكا ولعنا
B005 | الأباعد خلاف الأقارب
B006 | غير باعد وغير بعيد
B007 | بعيدات بين
B008 | بعد الرأي والغور
B009 | غير أبعد ولا طائل
B010 | بعد المعاداة

### ع ل م — 854 uses; here: 4:24:41 عَلِيمًا; 4:25:18 أَعْلَمُ; 4:26:13 عَلِيمٌ; 4:32:27 عَلِيمًۭا; 4:35:21 عَلِيمًا
B001 | انكشاف الشيء للعارف
B002 | أثر يميز الشيء ويهدي إليه
B003 | الخلق عالم يدل على صانعه
B004 | شق ظاهر في الشفة العليا
B005 | ماء كثير مجتمع في عيلم
B006 | طائر جارح يسمى العلام
B007 | ذكر الضباع يسمى العيلام

### ح ك م — 210 uses; here: 4:24:42 حَكِيمًۭا; 4:26:14 حَكِيمٌۭ; 4:35:6 حَكَمًۭا; 4:35:9 وَحَكَمًۭا
B001 | المنع والرد للإصلاح
B002 | الحكم والقضاء بين الناس
B003 | الحكمة والعلم المصيب
B004 | الإحكام والإتقان والوثاقة
B005 | التفويض والتحكيم
B006 | حكمة اللجام
B007 | الرجوع والإرجاع عن الشيء

### ط و ع — 129 uses; here: 4:25:3 يَسْتَطِعْ; 4:34:31 أَطَعْنَكُمْ
B001 | الانقياد والطاعة
B002 | الموافقة والمطاوعة
B003 | الاستطاعة والإطاقة
B004 | تكلف الاستطاعة
B005 | التطوع والتبرع
B006 | تسهيل النفس للأمر
B007 | تهيؤ المرعى والثمر

### ط و ل — 10 uses; here: 4:25:5 طَوْلًا
B001 | الطُّول والامتداد
B002 | حبل الطِّوَل
B003 | طول الزمان الطويل
B004 | الطَّوْل والقدرة
B005 | الطائل والغناء
B006 | التطاول والاستطالة
B007 | الإطالة والمطاولة
B008 | الطائلة والوتر

### ف ت ي — 21 uses; here: 4:25:15 فَتَيَٰتِكُمُ
B001 | الشباب والطراوة
B002 | الكناية بالفتى عن المملوك
B003 | الفتوة والكرم
B004 | تبيين الحكم والجواب
B005 | اختلاف الفتيان
B006 | القدح والمكيال

### ء ذ ن — 102 uses; here: 4:25:24 بِإِذْنِ
B001 | الأذن الجارحة وما يشبهها
B002 | الإصغاء وقبول المسموع
B003 | العلم والإعلام بالنداء
B004 | الإذن والترخيص بالأمر
B005 | التأذن بإيجاب الفعل

### ء ه ل — 127 uses; here: 4:25:25 أَهْلِهِنَّ; 4:35:8 أَهْلِهِۦ; 4:35:11 أَهْلِهَآ
B001 | جماعة القرب والانتماء
B002 | اتخاذ الأهل بالزواج
B003 | موضع الصلاح والاستحقاق
B004 | أنس المكان والعمران
B005 | تحية السعة والأنس
B006 | الإهالة المذابة

### خ د ن — 2 uses; here: 4:25:34 أَخْدَانٍۢ
B001 | المصاحبة والمخاللة
B002 | مصاحبة الشهوة

### ن ص ف — 7 uses; here: 4:25:41 نِصْفُ
B001 | الشطر والنصف
B002 | بلوغ النصف والوسط
B003 | النصفة والعدل
B004 | الخدمة والاستعمال
B005 | نصف العمر
B006 | النصيف الساتر
B007 | ناصفة الوادي
B008 | منصف الشراب
B009 | تناسق المحاسن

### ع ذ ب — 373 uses; here: 4:25:46 ٱلْعَذَابِ
B001 | العذوبة والطيب في الماء والمطعوم
B002 | العذوب امتناع الجسد عن الأكل والشرب
B003 | الكف والمنع والفطام عن الشيء
B004 | العذوب المكشوف للسماء
B005 | العذاب إيلام وعقوبة
B006 | العذبة طرف أو علاقة متدلية
B007 | العذبة شوائب الماء أو سطحه
B008 | العذبي كريم الأخلاق
B009 | العذابة والرحم والخرج بعد الولد

### خ ش ي — 48 uses; here: 4:25:49 خَشِىَ
B001 | الخوف والخشية مع الهيبة
B002 | العلم على سبيل المجاز
B003 | الكراهة في إسناد الخشية
B004 | الحشف واليبس

### ع ن ت — 5 uses; here: 4:25:50 ٱلْعَنَتَ
B001 | المشقة الشديدة والضرر الشاق
B002 | الإثم ومخافة الفجور
B003 | الإعنات والتعنّت
B004 | هيض العظم وكسره
B005 | العقبة الشاقة والأكمة العنوت
B006 | عنتوت القوس

### ص ب ر — 103 uses; here: 4:25:53 تَصْبِرُوا۟
B001 | حبس النفس عن الجزع
B002 | حبس القهر للقتل أو اليمين
B003 | تحمل الكفالة والملازمة
B004 | أعلى الشيء وجوانبه
B005 | حجر غليظ وأرض حصباء
B006 | الوقوع في شدة لا منفذ منها
B007 | شدة برد الشتاء
B008 | الصبر المر وعصارته
B009 | الصبار حمل الشجرة الحامض
B010 | سحاب أبيض متراكم
B011 | رقاقة الخوان وكومة الطعام
B012 | الإقصاص والقود
B013 | الجرأة على النار
B014 | انتظار الحكم
B015 | الصوم المسمى صبرا
B016 | بطن من غسان
B017 | الجبل ووسطه
B018 | سداد القارورة والبئر

### ه د ي — 316 uses; here: 4:26:5 وَيَهْدِيَكُمْ
B001 | دلالة بلطف إلى الطريق والحق
B002 | جهة الأمر وسيرته وقصده
B003 | المتقدم الهادي وأوائل الشيء
B004 | بعثة لطف وهدية إلى ذي مودة
B005 | الهدي المهدى إلى الحرم
B006 | العروس المهدية إلى زوجها
B007 | هدي الحرمة والأسير
B008 | مشي التهادي مع الاعتماد والتمايل
B009 | الهداء البليد الضعيف
B010 | هدي السكون وحسن الهيئة
B011 | إهداء الشعر ومهاداته

### س ن ن — 21 uses; here: 4:26:6 سُنَنَ
B001 | طريق جار وسيرة متبعة
B002 | صب سهل متصل
B003 | تحديد وصقل بالمسن
B004 | سن ناتئ وعمر ظاهر
B005 | حَمَأ مسنون وصورة مملسة
B006 | رعي يصقل ويقوي
B007 | إكباب بدفع أو عض
B008 | اندفاع واستنان
B009 | جزء حاد أو منفرد
B010 | سناسن عظام ونتوءات
B011 | سنائن ممتدة على وجه واحد

### ق ب ل — 294 uses; here: 4:26:9 قَبْلِكُمْ
B001 | مواجهة الشيء للشيء
B002 | تقدم الشيء أو إقباله
B003 | جهة الشيء وعنده
B004 | قبول الشيء برضا
B005 | جهة الصلاة المتوجه إليها
B006 | قبلة الفم والتقبيل
B007 | تلقي الخارج إلى اليد
B008 | ضمان الشيء والتكفل به
B009 | جماعة يقبل بعضها على بعض
B010 | أجزاء موصولة يقابل بعضها بعضا
B011 | إقبال العضو أو العلامة إلى جهة
B012 | ريح تقابل الدبور
B013 | طاقة على المقابلة
B014 | سقي على أفواه الإبل
B015 | ابتداء حاضر غير مهيأ
B016 | خرزة تقبل وجها إلى وجه

### ت و ب — 87 uses; here: 4:26:10 وَيَتُوبَ; 4:27:4 يَتُوبَ
B001 | الرجوع من الذنب إلى الله
B002 | عود الله على العبد بالتوبة والقبول
B003 | استدعاء التوبة من غيره
B004 | رجوع الله بالعبد إلى التخفيف والإباحة

### ت ب ع — 172 uses; here: 4:27:8 يَتَّبِعُونَ
B001 | التلو والقفو
B002 | اللَّحاق والإدراك
B003 | التقصي أثرا بعد أثر
B004 | الولاء والتتابع
B005 | المطالبة والطالب بالحق
B006 | التبعة اللازمة
B007 | ولد البقرة التابع لها
B008 | التابع الحسي
B009 | تُبَّع وملوكه
B010 | الجنية التابعة
B011 | اتباع النساء
B012 | الإحكام والتناسب

### ش ه و — 13 uses; here: 4:27:9 ٱلشَّهَوَٰتِ
B001 | نزوع النفس إلى المشتهى
B002 | التشهي بعد التشهي
B003 | الشهوة الخفية للمعاصي

### م ي ل — 6 uses; here: 4:27:11 تَمِيلُوا۟; 4:27:12 مَيْلًا
B001 | انحراف الشيء وعدوله إلى جانب
B002 | تردد بين وجهين
B003 | كتلة أو شجرة مائلة معتزلة
B004 | رجل أميل عن آلة الحرب أو ثبات الركوب
B005 | علامة الطريق ومقدار مد البصر
B006 | عود دقيق للكحل أو الجراحة
B007 | المال والقنية
B008 | المشطة الميلاء

### ع ظ م — 128 uses; here: 4:27:13 عَظِيمًۭا
B001 | الكبر والقوة
B002 | معظم الشيء
B003 | مستغلظ العضو
B004 | العظيمة النازلة
B005 | العَظْم الصلب
B006 | التعاظم والزهو
B007 | الاستعظام والهيبة
B008 | عظامة الردف
B009 | خشبة الرحل
B010 | الحرمة والشرف

### خ ف ف — 17 uses; here: 4:28:4 يُخَفِّفَ
B001 | خفة الثقل والحمل
B002 | خفة السير والارتحال
B003 | قلة المقدار والعدد
B004 | خفة الطيش والاضطراب
B005 | الاستخفاف إهانة واستهانة
B006 | الخُفّ والقدم الملبوسة
B007 | الخفوف للطاعة والانقياد
B008 | الإبل على خف واحد
B009 | خفخفة الصوت والحركة

### خ ل ق — 261 uses; here: 4:28:6 وَخُلِقَ
B001 | تقدير الشيء وقياسه
B002 | إبداع الخلق وإيجاده
B003 | تمام الخلقة واعتدال الصورة
B004 | السجية والطبيعة الباطنة
B005 | الجدارة والتهيؤ للشيء
B006 | الخلاق نصيب الخير
B007 | اختلاق الكذب والكلام
B008 | ملاسة السطح واستواؤه
B009 | بلى الثوب وذهاب وبره
B010 | الخلوق والتخليق بالطيب
B011 | نقرة أو بئر تمسك الماء
B012 | انسداد مصمت كالصخرة

### ء ن س — 97 uses; here: 4:28:7 ٱلْإِنسَٰنُ
B001 | ظهور الإنسان المخالف للتوحش والجن
B002 | إيناس الشيء برؤية أو إحساس أو سماع
B003 | الأنس الذي يزيل الوحشة
B004 | الجانب الإنسي المقبل على الإنسان
B005 | إنسان العين وصورة الإنسان في السواد
B006 | ابن الإنس للنفس والصفوة
B007 | الاستئناس قبل دخول البيوت

### ض ع ف — 52 uses; here: 4:28:8 ضَعِيفًۭا
B001 | خلاف القوة
B002 | زيادة الشيء بمثله
B003 | أثناء الشيء وجوفه
B004 | ضعف دابة الرجل
B005 | كثرة الضيعة وانتشارها

### ء ك ل — 109 uses; here: 4:29:5 تَأْكُلُوٓا۟
B001 | تناول المطعوم
B002 | غلة الشجر والزرع
B003 | النصيب والرزق المطعوم
B004 | استهلاك المال وأخذه
B005 | إطعام النار واشتعالها
B006 | التآكل والفساد والحكة
B007 | الفريسة والمعدة للأكل
B008 | أكل العرض والغيبة
B009 | الإفساد والنميمة بين الناس
B010 | الإدعاء على الغير والتمكين منه
B011 | قلة الجماعة بقدر رأس
B012 | قوة الشيء وتمام مادته
B013 | وعاء الأكل وموضعه
B014 | آلة تقطع اللحم

### ب ط ل — 36 uses; here: 4:29:8 بِٱلْبَٰطِلِ
B001 | ذهاب الشيء عن الحق والثبات
B002 | إبطال الشيء وإزالته
B003 | ادعاء الباطل وقول ما لا حقيقة له
B004 | البطل الشجاع المتعرض للمتالف
B005 | التعطل والبطالة عن النفع والعمل
B006 | ذهاب الدم هدرا بلا ثأر ولا دية
B007 | البطلة السحرة

### ت ج ر — 9 uses; here: 4:29:12 تِجَٰرَةً
B001 | التجارة وطلب الربح
B002 | الأرض المتجرة
B003 | الناقة الرائجة في البيع
B004 | الحذق بوجه الكسب

### ق ت ل — 170 uses; here: 4:29:17 تَقْتُلُوٓا۟
B001 | إماتة وإزهاق روح
B002 | إذلال وترويض حتى تلين الشدة
B003 | إحاطة علمية كأن الأمر مقهور
B004 | تدلل وتكسر في مشية أو طلب
B005 | تعريض شخص للقتل
B006 | قهر العشق أو الجن كقتل معنوي
B007 | كسر شدة الشراب بالماء
B008 | عدو أو قرين يقابل صاحبه
B009 | بقية النفس وبنية موثقة
B010 | دعاء بلعن أو إهلاك
B011 | مقاتلة ومحاربة بين طرفين
B012 | استماتة وإلقاء النفس في شدة
B013 | قاتل الشتوات بكفاية بردها

### ن ف س — 298 uses; here: 4:29:18 أَنفُسَكُمْ
B001 | خروج النسيم من الجوف
B002 | توسيع الكربة بالتنفيس
B003 | إصابة العين بالنفس
B004 | الدم السائل قوام النفس
B005 | خروج الولد ودم النفاس
B006 | نفس الشرب وجرعته
B007 | قدر دبغة يسيرة
B008 | ماء تقام به النفس
B009 | انفتاح الصبح والشيء كالنفس
B010 | شيء نفيس تتنافس فيه النفوس
B011 | النفس التي بها الحياة
B012 | عين الشيء وذاته
B013 | ما في النفس من عقل وروع
B014 | قوة النفس وخلقها
B015 | سعة ومسافة ومهلة
B016 | النافس سهم الميسر الخامس

### ف ع ل — 108 uses; here: 4:30:2 يَفْعَلْ
B001 | إحداث عمل
B002 | فَعال الخلق
B003 | فَعلة العمل
B004 | افتعال مختلق
B005 | فِعال بين اثنين
B006 | فَعال الفأس
B007 | مفعولات النحو

### ع د و — 106 uses; here: 4:30:4 عُدْوَٰنًۭا
B001 | مجاوزة الحد والظلم
B002 | العَدْو والحَضْر
B003 | العَدُوّ والعداوة
B004 | المجاوزة والاستثناء والصرف
B005 | العَدْوى في طلب الإنصاف
B006 | العَدْوى في انتقال الداء
B007 | العَوادي والعادية الشاغلة
B008 | العِداء في تعاقب الصيد
B009 | العَداء والعُدوة في الجانب والطوار
B010 | العَدْواء في صلابة المكان واضطرابه
B011 | العَدَوِيّة من نبات الصيف
B012 | العَنْدَأْوَة في الالتواء والعسر

### ظ ل م — 315 uses; here: 4:30:5 وَظُلْمًۭا
B001 | الظلمة وذهاب النور
B002 | وضع الشيء في غير موضعه
B003 | الظلامة وطلب الإنصاف
B004 | إيقاع الشيء في غير أوانه أو موضعه المحسوس
B005 | ماء الأسنان وبريق الثغر
B006 | الظليم ذكر النعام
B007 | شجر الظلام المتجاوز
B008 | المنع والحبس عن الحق

### ص ل ي — 25 uses; here: 4:30:7 نُصْلِيهِ
B001 | الصلاة عبادة لازمة
B002 | الدعاء والبركة والرحمة
B003 | ملاقاة النار وحرها
B004 | إيقاد الصلاء وتسوية الشيء بالنار
B005 | المَصالي أشراك وفخوخ
B006 | الصَّلا موضع الظهر والذنب
B007 | المصلي يتلو السابق
B008 | الصلوات مواضع عبادة
B009 | الصلاية حجر يدق عليه
B010 | الصِّليان نبت ترعاه الإبل

### ن و ر — 194 uses; here: 4:30:8 نَارًۭا
B001 | الضياء والإضاءة
B002 | النار المتقدة والسمة بها
B003 | تنور النار من بعيد
B004 | نور الشجر وزهره
B005 | المنار والمنارة الظاهرة
B006 | النِّفار وقلة الثبات
B007 | النائرة بين القوم
B008 | دخان الوشم والكحل
B009 | النُّورَة المطلية
B010 | التلبيس على الغير
B011 | وضوح النِّير وبروزه

### ي س ر — 44 uses; here: 4:30:13 يَسِيرًا
B001 | انفتاح وسهولة بعد عسر
B002 | قلة يسيرة
B003 | سعة وغنى
B004 | الجهة اليسرى واليد اليسرى
B005 | خفة وانقياد في الحركة
B006 | إدرار ونماء في الغنم
B007 | قداح وقمار وتقسيم جزور
B008 | خطوط منفصلة وعلامات في البدن
B009 | فتل إلى أسفل وطعن حذاء الوجه
B010 | موضع أو علم باسم يسر ويسار
B011 | فتى يسمى يسارا

### ج ن ب — 33 uses; here: 4:31:2 تَجْتَنِبُوا۟
B001 | الجنب جانب الجسد وناحية الشيء
B002 | الجنب قرب ومجاورة على الجانب
B003 | المجانبة إبعاد واعتزال وغربة
B004 | الجنابة حالة تجنب مواضع الصلاة
B005 | التجنيب قيادة شيء إلى الجنب
B006 | الجنوب ريح من جهة مخصوصة
B007 | داء الجنب وأثره في البدن
B008 | التجنيب قلة لبن الإبل
B009 | المجنب خير أو شر كثير
B010 | الجنبة نبت متوسط مستقل
B011 | المجنب وقاء إلى الجنب
B012 | التجنيب تباعد في هيئة القوائم

### ك ب ر — 161 uses; here: 4:31:3 كَبَآئِرَ; 4:34:40 كَبِيرًۭا
B001 | العظم خلاف الصغر
B002 | معظم الأمر
B003 | إعظام الشيء في الصدر
B004 | كبر السن والقدم
B005 | رفعة الشرف والرئاسة
B006 | العظمة والكبرياء
B007 | الإثم الكبير والذنوب الكبائر
B008 | كبر النسب والولادة
B009 | التكبير بقول الله أكبر
B010 | الكبر مشقة وثقل
B011 | المكابرة والغلبة
B012 | الكَبَر طبل
B013 | أكبر النهار

### ن ه ي — 56 uses; here: 4:31:5 تُنْهَوْنَ
B001 | الزجر والكف عن الفعل
B002 | الغاية التي ينتهي إليها الشيء
B003 | العقل الناهي عن القبيح
B004 | مستقر الماء عند منتهى السيل
B005 | الكفاية التي تنهي طلب غيرها
B006 | التناهي في السمن
B007 | الانقطاع عن طلب الحاجة
B008 | ارتفاع النهار أو الماء إلى النهاء
B009 | النَّهاء القوارير والزجاج
B010 | مقدار العدد ومبلغه

### ك ف ر — 525 uses; here: 4:31:7 نُكَفِّرْ
B001 | ستر وتغطية
B002 | غمر ساتر
B003 | حجب الحق
B004 | ستر النعمة
B005 | تبرؤ وتنصل
B006 | نسبة إلى الكفر
B007 | إلجاء إلى العصيان
B008 | تغطية البذر
B009 | محو الإثم بتغطيته
B010 | كمام الثمر
B011 | كافور طيب
B012 | موضع منقطع
B013 | ثنية مستورة
B014 | خضوع متطامن
B015 | تاج يغطي

### ك ر م — 47 uses; here: 4:31:12 كَرِيمًۭا
B001 | الشرف والجود المحمود
B002 | جودة النبات والغيث
B003 | الكَرْم المنظوم في العنق
B004 | العنب والكرمة
B005 | طبق على رأس الوعاء
B006 | مفاخرة الكرم والغلبة فيه
B007 | رأس الفخذ المستدير
B008 | هدية تطلب المكافأة
B009 | جواب الرضا والكرامة
B010 | العزيز الذي يكرم عليك

### م ن ي — 21 uses; here: 4:32:2 تَتَمَنَّوْا۟
B001 | تقدير الشيء وإنفاذ قضائه
B002 | المَنِيّ الذي تقدّر منه الخلقة
B003 | المَنِيّة موت مقدر
B004 | أمنية يصورها القلب
B005 | مِنًى موضع النسك
B006 | المَنَا معيار يوزن به
B007 | تلاوة تقرأ وتوضع مواضعها
B008 | مماناة تقيس فعلا بفعل
B009 | مَنِيّة الناقة أيام استبرائها
B010 | مقابلة وحذاء
B011 | ابتلاء يلزم الإنسان
B012 | مناة اسم صنم أو علم
B013 | أماني مختلقة لا حقيقة لها
B014 | مماناة قلة غيرة

### ف ض ل — 104 uses; here: 4:32:4 فَضَّلَ; 4:32:21 فَضْلِهِۦٓ; 4:34:6 فَضَّلَ
B001 | الزيادة والبقية
B002 | الدرجة والفضيلة
B003 | الإحسان والعطية
B004 | ادعاء الفضل
B005 | التوشح بالثوب

### ر ج ل — 73 uses; here: 4:32:10 لِّلرِّجَالِ; 4:34:1 ٱلرِّجَالُ
B001 | الرِّجل العضو
B002 | الرجل الذكر
B003 | المشي على الأرجل
B004 | زمان الرجل
B005 | بياض رجل الدابة
B006 | الرَّجْل من الجراد
B007 | الرِّجلة النبات
B008 | رِجْلة الماء
B009 | رجل القوس والميسم
B010 | الشعر الرَّجِل
B011 | الكلام المرتجل
B012 | ترجل النهار
B013 | نزول البئر بلا تدلية
B014 | إرسال الفصيل مع أمه
B015 | ارتجال الفرس
B016 | المرجل المنصوب
B017 | الرجيلاء في الولادة
B018 | الرِّجل جبار
B019 | القيام على رجل
B020 | ركوب الأمر بالرجلين

### ن ص ب — 32 uses; here: 4:32:11 نَصِيبٌۭ; 4:32:15 نَصِيبٌۭ; 4:33:12 نَصِيبَهُمْ
B001 | إقامة الشيء منتصبا بارزا
B002 | حجر منصوب للعبادة والذبح
B003 | علامة أو حجارة منصوبة للحد أو الحوض
B004 | تعب وعناء وبلاء ينهك الإنسان
B005 | حظ معين مرفوع لصاحبه
B006 | نصاب الشيء: أصله ومقداره الثابت
B007 | نصب الكلمة في الإعراب
B008 | مواجهة العداوة والحرب
B009 | غناء يرفع به الصوت
B010 | سير اليوم سيرا لينا

### ك س ب — 67 uses; here: 4:32:13 ٱكْتَسَبُوا۟; 4:32:17 ٱكْتَسَبْنَ
B001 | طلب الرزق والنفع وإصابته
B002 | إكساب غيره خيرا أو مالا
B003 | الكواسب الجوارح
B004 | الكُسب عصارة الدهن

### س ء ل — 129 uses; here: 4:32:18 وَسْـَٔلُوا۟
B001 | السؤال والطلب
B002 | السُّؤل المطلوب
B003 | قضاء المسألة
B004 | السؤال المتبادل

### ك ل ل — 377 uses; here: 4:32:25 بِكُلِّ; 4:33:1 وَلِكُلٍّۢ; 4:33:17 كُلِّ
B001 | الكَلال وخلاف الحدة
B002 | الكُلّ عيالا وثقلا
B003 | الكُلّ إحاطة وتماما
B004 | الكَلالة قرابة عارضة
B005 | الإكليل وما يحيط
B006 | الكِلّة سترا وبيتا
B007 | الكُلْكُل صدرا
B008 | الكُلْكُل قصر وغلظ
B009 | الكلاكل جماعات
B010 | الحمل بين المضي والإحجام
B011 | الانكلال تبسما ولمعا

### و ل ي — 232 uses; here: 4:33:3 مَوَٰلِىَ
B001 | قرب ودنو بلا فاصل
B002 | تتابع شيء بعد شيء
B003 | تولي الأمر والقيام عليه
B004 | محبة ونصرة وموالاة
B005 | ولاء قرابة وعتق وجوار
B006 | تولية الوجه والإقبال
B007 | الإدبار والإعراض
B008 | الأولوية والاستحقاق
B009 | أولى لك تهديد ووعيد
B010 | مطر يلي الوسمي
B011 | ولية تحت الرحل
B012 | استيلاء وبلوغ غاية
B013 | إيلاء وإسناد معروف أو شر
B014 | تولية البيع
B015 | موالاة صغار النعم عن كبارها
B016 | ولي الرطب وتولى إذا هاج

### ت ر ك — 43 uses; here: 4:33:5 تَرَكَ
B001 | التخلية عن الشيء
B002 | إبقاء الأثر بعد الترك
B003 | ترك الشيء على حال
B004 | تراك بمعنى اترك
B005 | متاركة بين طرفين
B006 | ما يتركه الميت
B007 | امرأة تركت بلا زواج
B008 | بيضة متروكة وما يشبهها
B009 | موضع تركه الناس أو السيل
B010 | جيل من الناس

### و ل د — 102 uses; here: 4:33:6 ٱلْوَٰلِدَانِ
B001 | مولود من نسل
B002 | أبوان من جهة الولادة
B003 | حدوث الولادة ووضع الحمل
B004 | صغير قريب العهد بالولادة أو مملوك
B005 | شيء حاصل عن شيء أو مستحدث منه
B006 | قرين في سن الولادة
B007 | أمر لا ينادى وليده

### ق ر ب — 96 uses; here: 4:33:7 وَٱلْأَقْرَبُونَ
B001 | الدنو وخلاف البعد
B002 | دنو الزمان وانقضاء الشيء
B003 | قرابة الرحم والنسب
B004 | حظوة المقربين وخاصة الملك
B005 | القربة والقربان إلى الله
B006 | القرب بالرعاية والقدرة
B007 | مقاربة الشيء وملابسته
B008 | ليلة القرب وطلب الماء
B009 | القربة وعاء الماء
B010 | قراب السيف ووعاؤه
B011 | القارب السفينة الصغيرة
B012 | دنو الولادة في الحيوان
B013 | الخيل والإبل المقربة
B014 | تقريب الفرس في العدو
B015 | قُرْب الفرس والخاصرة
B016 | القراب والمقاربة في المقدار

### ع ق د — 7 uses; here: 4:33:9 عَقَدَتْ
B001 | شد الأطراف وربطها
B002 | إلزام العهد وإبرامه
B003 | غلظ المائع وصلبه
B004 | اقتناء المال والضيعة
B005 | كثافة الشجر والمرعى
B006 | ثبات القلب والرأي
B007 | حبسة اللسان وتعقيد الكلام
B008 | تراكم الرمل وانقباض السحاب
B009 | عنقود متماسك
B010 | التواء عضو الحيوان
B011 | وثاقة البدن وقصره
B012 | انقباض الغضب والخلق
B013 | عقد السحر والعزائم
B014 | الحساب بعقد الأصابع
B015 | قرب معقد الإزار
B016 | إحاطة الموضع وإطباقه
B017 | لجأ بعنقه

### ش ه د — 160 uses; here: 4:33:19 شَهِيدًا
B001 | الحضور مع المشاهدة
B002 | البيان بعلم
B003 | صيغة الإشهاد والذكر
B004 | الشهادة بالموت والحضور
B005 | اللسان الشاهد
B006 | الخارج عند الولادة والإدراك
B007 | الشَّهْد في الشمع
B008 | العلامة الشاهدة

### ق و م — 660 uses; here: 4:34:2 قَوَّٰمُونَ
B001 | جماعة الناس والرجال
B002 | انتصاب وقيام بالبدن
B003 | عزم ونهوض إلى الأمر
B004 | رعاية وحفظ وولاية
B005 | إقامة وإدامة وتوفية حق
B006 | مقام وإقامة في موضع
B007 | نيابة وقيام مقام غيره
B008 | استقامة واعتدال واستواء
B009 | قوام وعماد ومعاش
B010 | قيمة وتقويم وتسعير
B011 | قامة وقوام الجسم والطول
B012 | آلة قائمة وجزء قائم
B013 | قيامة وبعث وقيام الساعة
B014 | مقاومة ومنازلة
B015 | وزن سواء ومقدار معتدل
B016 | جمود ووقوف وكلال
B017 | انتصاف النهار وقائم الظهيرة
B018 | نفاق السوق
B019 | وجع قائم بالعضو
B020 | قوام في قوائم الشاة
B021 | عين قائمة ذاهبة البصر

### ن ف ق — 111 uses; here: 4:34:12 أَنفَقُوا۟
B001 | ذهاب الشيء وانقطاعه
B002 | خروج المال في النفقة
B003 | سرب نافذ له مخرج
B004 | إظهار باب وإخفاء مخرج

### ص ل ح — 180 uses; here: 4:34:15 فَٱلصَّٰلِحَٰتُ; 4:35:14 إِصْلَٰحًۭا
B001 | الصلاح ضد الفساد والطلاح
B002 | الصلح إزالة النفار بين الناس
B003 | الصلاح للشيء ملاءمته
B004 | صالح وما قاربه علما لشخص
B005 | صلاح والصلح علمان لمواضع

### ق ن ت — 13 uses; here: 4:34:16 قَٰنِتَٰتٌ
B001 | طاعة دينية خاضعة
B002 | قيام طويل في الصلاة
B003 | دعاء قائم في الصلاة
B004 | إمساك مصلي عن الكلام

### ح ف ظ — 44 uses; here: 4:34:17 حَٰفِظَٰتٌۭ; 4:34:20 حَفِظَ
B001 | مراعاة الشيء وحراسته
B002 | ثبوت المحفوظ في النفس
B003 | ملازمة الأمر والمواظبة عليه
B004 | تيقظ المتحفظ وقلة غفلته
B005 | حفيظة الغضب والحمية
B006 | صون الحرم والعهد والعفة
B007 | طريق حافظ بين مستقيم

### غ ي ب — 60 uses; here: 4:34:18 لِّلْغَيْبِ
B001 | تستر الشيء عن العيون
B002 | منهبط يغيب فيه الشيء
B003 | أجمة يغاب فيها
B004 | ذكر الإنسان في غيبته
B005 | غيبة الزوج وحفظ الغيب
B006 | الغيب شك
B007 | غَيْب شحم الثرب
B008 | غيبان الشجرة عروق مستترة
B009 | تغييبه في القبر

### خ و ف — 124 uses; here: 4:34:23 تَخَافُونَ; 4:35:2 خِفْتُمْ
B001 | ذعر يتوقع المكروه
B002 | إدخال الخوف في الغير
B003 | مغالبة في الخوف
B004 | نقص يأخذ من الشيء
B005 | ظهور الخوف على الإنسان
B006 | خافة العسال والسقاء

### ن ش ز — 5 uses; here: 4:34:24 نُشُوزَهُنَّ
B001 | الارتفاع والنتوء
B002 | النهوض والانتقال عن المجلس
B003 | إنشاز العظام وتركيبها
B004 | نشوز الزوجين
B005 | الإغضاب والإقامة بالكلام
B006 | تشقيق الإبل ونقلها
B007 | الغلظ وثبات القوة

### و ع ظ — 25 uses; here: 4:34:25 فَعِظُوهُنَّ
B001 | تذكير مخوِّف يرق له القلب

### ه ج ر — 31 uses; here: 4:34:26 وَٱهْجُرُوهُنَّ
B001 | الانقطاع والمفارقة
B002 | الخروج من دار إلى دار
B003 | الكلام القبيح المهجور
B004 | هذيان المريض والنائم
B005 | حر الهاجرة ووقتها
B006 | التبكير والمضي أول الوقت
B007 | الربط بالهجار
B008 | المجاوزة في الحسن والتمام
B009 | الدأب والديدن الملازم
B010 | النبت اليابس المهجور
B011 | الحوض المقتطع للماء
B012 | الأعلام والمواضع
B013 | البعد بعد الحول

### ض ج ع — 3 uses; here: 4:34:28 ٱلْمَضَاجِعِ
B001 | لصوق الجنب بالأرض
B002 | مشاركة المضجع
B003 | الانطراح عن القيام بالأمر
B004 | خفض الشيء وإمالته
B005 | الأرض المنخفضة اللاصقة
B006 | البهيمة اللازمة ناحية ترعى والقطيع الكثير
B007 | السحاب المقيم المبطئ
B008 | ميل الممتلئ وتفريغه
B009 | صمغ نبات للغسل

### ض ر ب — 58 uses; here: 4:34:29 وَٱضْرِبُوهُنَّ
B001 | إيقاع شيء على شيء
B002 | السعي في الأرض
B003 | تصوير المثل وإظهاره
B004 | القبض عن الشيء والكف
B005 | الحجر على اليد
B006 | إلقاء غطاء أو حاجز على الشيء
B007 | الصنف والصيغة
B008 | المثل والنظير
B009 | السجية المضروبة
B010 | المال المضروب على أحد
B011 | ضرب الفحل الناقة
B012 | الحركة المضطربة والخفق
B013 | أثر البرد والمطر في الأرض والنبات
B014 | موضع الضرب وآلته وصنعته
B015 | الغليظ المخلوط من عسل أو لبن
B016 | شركة التجارة بالسفر
B017 | إلهاب الناس إلى الفعل
B018 | صفات ومشتقات متفرقة

### ع ل و — 70 uses; here: 4:34:39 عَلِيًّۭا
B001 | السمو والارتفاع
B002 | الرفعة والشرف
B003 | العظمة والتجبر
B004 | الغلبة والاستيلاء
B005 | الجهة العليا ومن فوق
B006 | نداء التعالي
B007 | المواضع العالية
B008 | الشيء المحمول على الأعلى
B009 | أسماء الأدوات والأجزاء المرتفعة
B010 | الطول والضخامة
B011 | السلامة من النفاس أو العلة
B012 | حرف عَلَى وما جرى مجراه

### ش ق ق — 28 uses; here: 4:35:3 شِقَاقَ
B001 | انصداع الشيء وانفتاحه
B002 | النصف والشق المقابل
B003 | ثقل يشق النفس
B004 | انصداع الجماعة بالخلاف
B005 | الشقة البعيدة
B006 | قطعة منشقة وثوب
B007 | فرجة بين الرمال ونباتها
B008 | شقشقة البعير والخطيب
B009 | ميل عن القصد إلى الشقين
B010 | صفة الفرس الأشق

### ب ع ث — 67 uses; here: 4:35:5 فَٱبْعَثُوا۟
B001 | إثارة الساكن من ركوده
B002 | إرسال المبعوث وتوجيهه
B004 | اندفاع القوم ومضيهم

### و ف ق — 4 uses; here: 4:35:15 يُوَفِّقِ
B001 | ملاءمة الشيئين واجتماعهما على وفاق
B002 | مصادفة الشيء والوقوع عليه موافقا
B003 | إصابة الخير بتوفيق من الله
B004 | قدر يساوي الحاجة أو النظير
B005 | حين يوافق الحدث وقته
B006 | إيقاع فوق السهم في الوتر

### خ ب ر — 52 uses; here: 4:35:22 خَبِيرًۭا
B001 | العلم بالخبر وباطن الأمر
B002 | لين الأرض ومائها
B003 | إصلاح الأرض بالمخابرة
B004 | الغزر في المزادة والناقة
B005 | اللِّين في النبات والوبر والزبد
B006 | القسمة في الشاة واللحم

## Scene map in this window (mechanical, generous; for what the chain map missed)

- body.limbs [95 words, 24 roles] يَحِلُّ 4:19:5: ح ل ل B014 joint · كَرْهًۭا 4:19:10: ك ر ه B005 head, ك ر ه B006 neck · تَعْضُلُوهُنَّ 4:19:12: ع ض ل B001 limb · ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B009 leg · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B011 hand, ع ر ف B013 face · وَيَجْعَلَ 4:19:30: ج ع ل B012 stature · +89 more (all: data/scenes/s004/body.limbs.md)
- war.battle [76 words, 23 roles] كَرْهًۭا 4:19:10: ك ر ه B004 hardship · ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B011 enemy · ٱللَّهُ 4:19:31: و ل ه~alt B002 captive · كَثِيرًۭا 4:19:34: ك ث ر B002 victory · سَلَفَ 4:22:11: س ل ف B001 rank · حُرِّمَتْ 4:23:1: ح ر م B005 retreat · +70 more (all: data/scenes/s004/war.battle.md)
- speech.calling [91 words, 22 roles] ءَامَنُوا۟ 4:19:3: ء م ن B003 answer · بِفَٰحِشَةٍۢ 4:19:20: ف ح ش B003 insult · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B008 summons · شَيْـًۭٔا 4:19:29: ش ي ء B007 cry, ش ي ء B009 cry · وَيَجْعَلَ 4:19:30: ج ع ل B003 naming · ٱللَّهُ 4:19:31: ء ل ه B002 call · +85 more (all: data/scenes/s004/speech.calling.md)
- travel.route [72 words, 19 roles] تَعْضُلُوهُنَّ 4:19:12: ع ض ل B010 traveller · لِتَذْهَبُوا۟ 4:19:13: ذ ه ب B007 way · ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B001 traveller, ء ت ي B010 road · أَرَدتُّمُ 4:20:2: ر و د B003 guide, ر و د B004 traveller · قِنطَارًۭا 4:20:9: ق ن ط ر B001 bridge · سَلَفَ 4:22:11: س ل ف B001 leader · +66 more (all: data/scenes/s004/travel.route.md)
- wealth.property [85 words, 17 roles] تَرِثُوا۟ 4:19:8: و ر ث B001 inheritance, و ر ث B002 provision · لِتَذْهَبُوا۟ 4:19:13: ذ ه ب B001 treasure · بِفَٰحِشَةٍۢ 4:19:20: ف ح ش B005 stinginess · وَعَاشِرُوهُنَّ 4:19:22: ع ش ر B004 wealth · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B005 generosity, ع ر ف B008 lost animal · تَأْخُذُوا۟ 4:20:11: ء خ ذ B005 possession, ء خ ذ B010 wealth · +79 more (all: data/scenes/s004/wealth.property.md)
- plant.growth_decay [51 words, 17 roles] تَعْضُلُوهُنَّ 4:19:12: ع ض ل B007 branch · وَعَاشِرُوهُنَّ 4:19:22: ع ش ر B014 growth · فَعَسَىٰٓ 4:19:26: ع س ي B002 thickening · وَيَجْعَلَ 4:19:30: ج ع ل B006 young tree · كَثِيرًۭا 4:19:34: ك ث ر B006 shoot · زَوْجٍۢ 4:20:4: ز و ج B004 plant kind · +45 more (all: data/scenes/s004/plant.growth_decay.md)
- kin.marriage [57 words, 16 roles] يَحِلُّ 4:19:5: ح ل ل B006 spouse · تَعْضُلُوهُنَّ 4:19:12: ع ض ل B004 marriage restraint · بِفَٰحِشَةٍۢ 4:19:20: ف ح ش B004 waiting period · مُّبَيِّنَةٍۢ 4:19:21: ب ي ن B012 divorce · زَوْجٍۢ 4:20:4: ز و ج B002 bride, ز و ج B002 groom, ز و ج B003 bride conveyance · تَنكِحُوا۟ 4:22:2: ن ك ح B002 contract, ن ك ح B003 contract, ن ك ح B004 spouse, ن ك ح B005 contract, ن ك ح B007 contract · +51 more (all: data/scenes/s004/kin.marriage.md)
- body.strength [61 words, 15 roles] كَرْهًۭا 4:19:10: ك ر ه B002 fatigue, ك ر ه B005 firmness · تَعْضُلُوهُنَّ 4:19:12: ع ض ل B001 muscle, ع ض ل B010 fatigue · وَيَجْعَلَ 4:19:30: ج ع ل B012 fatness · غَلِيظًۭا 4:21:11: غ ل ظ B001 bulk · وَبَنَاتُكُمْ 4:23:4: ب ن ي B002 body form, ب ن ي B010 fatness · أَيْمَٰنُكُمْ 4:24:7: ي م ن B004 strength · +55 more (all: data/scenes/s004/body.strength.md)
- war.arms [61 words, 15 roles] كَرْهًۭا 4:19:10: ك ر ه B004 sword · مُّبَيِّنَةٍۢ 4:19:21: ب ي ن B008 bow · سَلَفَ 4:22:11: س ل ف B014 arrow · أَصْلَٰبِكُمْ 4:23:41: ص ل ب B001 edge · غَفُورًۭا 4:23:53: غ ف ر B001 armour · مَلَكَتْ 4:24:6: م ل ك B001 shaft · +55 more (all: data/scenes/s004/war.arms.md)
- know.perceiving [60 words, 15 roles] تَرِثُوا۟ 4:19:8: و ر ث B003 knowledge · لِتَذْهَبُوا۟ 4:19:13: ذ ه ب B003 perceiving · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B003 knowing, ع ر ف B012 knowing · خَيْرًۭا 4:19:33: خ ي ر B003 discernment · بُهْتَٰنًۭا 4:20:15: ب ه ت B001 bewilderment · أُمَّهَٰتُكُمْ 4:23:3: ء م م B007 ignorance · +54 more (all: data/scenes/s004/know.perceiving.md)
- motion.passage [56 words, 15 roles] يَحِلُّ 4:19:5: ح ل ل B008 channel, ح ل ل B011 dislodging · تَعْضُلُوهُنَّ 4:19:12: ع ض ل B005 blocked emergence · لِتَذْهَبُوا۟ 4:19:13: ذ ه ب B006 passing through · ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B001 entering · ٱللَّهُ 4:19:31: و ل ه~alt B003 vanishing · أَفْضَىٰ 4:21:4: ف ض و B002 entering, ف ض و B003 entering, ف ض و B004 penetrating · +50 more (all: data/scenes/s004/motion.passage.md)
- kin.lineage [82 words, 14 roles] تَرِثُوا۟ 4:19:8: و ر ث B001 heir · تَعْضُلُوهُنَّ 4:19:12: ع ض ل B009 tribe · ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B006 clan · مُّبَيِّنَةٍۢ 4:19:21: ب ي ن B003 kin tie · قِنطَارًۭا 4:20:9: ق ن ط ر B003 ancestor · تَنكِحُوا۟ 4:22:2: ن ك ح B004 clan tie · +76 more (all: data/scenes/s004/kin.lineage.md)
- tool.implement [45 words, 14 roles] يَحِلُّ 4:19:5: ح ل ل B013 device · وَيَجْعَلَ 4:19:30: ج ع ل B007 pot lifter · سَلَفَ 4:22:11: س ل ف B010 implement · وَرَآءَ 4:24:14: و ر ي B002 fire drill · فَرِيضَةًۭ 4:24:28: ف ر ض B001 cutting tool · تَصْبِرُوا۟ 4:25:53: ص ب ر B018 plug · +39 more (all: data/scenes/s004/tool.implement.md)
- dwelling.building [40 words, 14 roles] قِنطَارًۭا 4:20:9: ق ن ط ر B001 bridge · حُرِّمَتْ 4:23:1: ح ر م B003 house · أُمَّهَٰتُكُمْ 4:23:3: ء م م B002 foundation · وَبَنَاتُكُمْ 4:23:4: ب ن ي B001 house, ب ن ي B003 square building, ب ن ي B009 pillar · حُجُورِكُم 4:23:23: ح ج ر B004 chamber · وَٱلْمُحْصَنَٰتُ 4:24:1: ح ص ن B001 wall · +34 more (all: data/scenes/s004/dwelling.building.md)
- trade.sale [64 words, 13 roles] ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B008 payment · ٱللَّهُ 4:19:31: و ل ه~alt B002 sale separation · ٱسْتِبْدَالَ 4:20:3: ب د ل B005 seller · تَأْخُذُوا۟ 4:20:11: ء خ ذ B010 profit · مِّيثَٰقًا 4:21:10: و ث ق B004 contract · سَلَفَ 4:22:11: س ل ف B005 price · +58 more (all: data/scenes/s004/trade.sale.md)
- kin.birth_nursing [56 words, 13 roles] يَحِلُّ 4:19:5: ح ل ل B010 birth · تَعْضُلُوهُنَّ 4:19:12: ع ض ل B005 labour · ٱللَّهُ 4:19:31: و ل ه~alt B002 mother child separation · وَمَقْتًۭا 4:22:15: م ق ت B002 offspring · أُمَّهَٰتُكُمْ 4:23:3: ء م م B001 nursing · أَرْضَعْنَكُمْ 4:23:14: ر ض ع B001 nursing, ر ض ع B002 foster child, ر ض ع B004 nursing · +50 more (all: data/scenes/s004/kin.birth_nursing.md)
- travel.mount [56 words, 13 roles] يَحِلُّ 4:19:5: ح ل ل B013 load, ح ل ل B014 lameness · تَعْضُلُوهُنَّ 4:19:12: ع ض ل B010 exhaustion · ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B009 mount · زَوْجٍۢ 4:20:4: ز و ج B006 saddle · تَأْخُذُوا۟ 4:20:11: ء خ ذ B001 rein · جُنَاحَ 4:23:35: ج ن ح B001 mount, ج ن ح B006 urging on · +50 more (all: data/scenes/s004/travel.mount.md)
- tool.vessel [41 words, 13 roles] يَحِلُّ 4:19:5: ح ل ل B013 vessel · أَفْضَىٰ 4:21:4: ف ض و B005 sack · وَبَنَاتُكُمْ 4:23:4: ب ن ي B004 skin bag · وَرَبَٰٓئِبُكُمُ 4:23:20: ر ب ب B010 basket · ٱسْتَمْتَعْتُم 4:24:23: م ت ع B003 container · فَرِيضَةًۭ 4:24:28: ف ر ض B005 cup · +35 more (all: data/scenes/s004/tool.vessel.md)
- quantity.more_less [65 words, 12 roles] يَحِلُّ 4:19:5: ح ل ل B005 decrease · تَعْضُلُوهُنَّ 4:19:12: ع ض ل B007 increase · بِبَعْضِ 4:19:14: ب ع ض B001 part · بِفَٰحِشَةٍۢ 4:19:20: ف ح ش B002 excess · وَعَاشِرُوهُنَّ 4:19:22: ع ش ر B002 completion · كَثِيرًۭا 4:19:34: ك ث ر B001 increase, ك ث ر B002 outnumbering, ك ث ر B004 abundance, ك ث ر B005 excess · +59 more (all: data/scenes/s004/quantity.more_less.md)
- body.illness [59 words, 12 roles] تَعْضُلُوهُنَّ 4:19:12: ع ض ل B002 disease · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B012 physician · ٱسْتِبْدَالَ 4:20:3: ب د ل B004 pain · أَصْلَٰبِكُمْ 4:23:41: ص ل ب B003 fever · أُجُورَهُنَّ 4:24:27: ء ج ر B002 healing · تَصْبِرُوا۟ 4:25:53: ص ب ر B008 medicine · +53 more (all: data/scenes/s004/body.illness.md)
- life.death [51 words, 12 roles] ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B011 death · فَعَسَىٰٓ 4:19:26: ع س ي B003 old age · ٱسْتَمْتَعْتُم 4:24:23: م ت ع B007 lifespan · ٱلْعَنَتَ 4:25:50: ع ن ت B001 dying · تَصْبِرُوا۟ 4:25:53: ص ب ر B004 grave side, ص ب ر B012 death · تَقْتُلُوٓا۟ 4:29:17: ق ت ل B001 death, ق ت ل B005 endangerment, ق ت ل B009 vitality, ق ت ل B012 self-endangerment · +45 more (all: data/scenes/s004/life.death.md)
- law.judgment [47 words, 12 roles] يَحِلُّ 4:19:5: ح ل ل B004 sentence · مُّبَيِّنَةٍۢ 4:19:21: ب ي ن B004 testimony, ب ي ن B011 witness · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B008 claimant, ع ر ف B009 testimony · وَإِثْمًۭا 4:20:16: ء ث م B003 sentence, ء ث م B004 verdict · حُجُورِكُم 4:23:23: ح ج ر B001 restraint · جُنَاحَ 4:23:35: ج ن ح B003 offense · +41 more (all: data/scenes/s004/law.judgment.md)
- ritual.prayer [45 words, 12 roles] ءَامَنُوا۟ 4:19:3: ء م ن B003 call · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B007 standing · ٱللَّهُ 4:19:31: ء ل ه B001 worship, ء ل ه B002 call · جُنَاحَ 4:23:35: ج ن ح B007 prostration · فَرِيضَةًۭ 4:24:28: ف ر ض B002 prescribed rite · قَبْلِكُمْ 4:26:9: ق ب ل B001 direction, ق ب ل B005 direction · +39 more (all: data/scenes/s004/ritual.prayer.md)
- body.wound [53 words, 11 roles] بِبَعْضِ 4:19:14: ب ع ض B002 bite · ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B011 fracture · مُّبَيِّنَةٍۢ 4:19:21: ب ي ن B008 severing · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B011 sore · أَفْضَىٰ 4:21:4: ف ض و B004 wound · تَبْتَغُوا۟ 4:24:17: ب غ ي B004 swelling · +47 more (all: data/scenes/s004/body.wound.md)
- pastoral.breeding [43 words, 11 roles] يَحِلُّ 4:19:5: ح ل ل B009 barrenness, ح ل ل B010 newborn · تَعْضُلُوهُنَّ 4:19:12: ع ض ل B005 birth · ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B012 mating · وَعَاشِرُوهُنَّ 4:19:22: ع ش ر B007 pregnancy · أَرْضَعْنَكُمْ 4:23:14: ر ض ع B001 suckling · حُجُورِكُم 4:23:23: ح ج ر B007 breeding mare · +37 more (all: data/scenes/s004/pastoral.breeding.md)
- land.mountain [28 words, 11 roles] مُّبَيِّنَةٍۢ 4:19:21: ب ي ن B007 highland · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B002 ridge · إِحْدَىٰهُنَّ 4:20:8: ء ح د B006 mountain · حُجُورِكُم 4:23:23: ح ج ر B003 rock · مُسَٰفِحِينَ 4:24:21: س ف ح B003 flank · ٱلْعَنَتَ 4:25:50: ع ن ت B005 pass · +22 more (all: data/scenes/s004/land.mountain.md)
- dwelling.settlement [26 words, 10 roles] يَحِلُّ 4:19:5: ح ل ل B002 dwelling place · وَيَجْعَلَ 4:19:30: ج ع ل B011 place · تَجْمَعُوا۟ 4:23:43: ج م ع B004 venue · وَٱلْمُحْصَنَٰتُ 4:24:1: ح ص ن B001 fortress · بِإِذْنِ 4:25:24: ء ذ ن B004 gate · تَجْتَنِبُوا۟ 4:31:2: ج ن ب B001 outskirts · +20 more (all: data/scenes/s004/dwelling.settlement.md)
- rule.obedience [77 words, 9 roles] كَرْهًۭا 4:19:10: ك ر ه B003 submission · ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B003 obedience · شَيْـًۭٔا 4:19:29: ش ي ء B003 compulsion · وَيَجْعَلَ 4:19:30: ج ع ل B012 obstinacy · كِتَٰبَ 4:24:8: ك ت ب B003 obligation · تَبْتَغُوا۟ 4:24:17: ب غ ي B003 rebellion · +71 more (all: data/scenes/s004/rule.obedience.md)
- dress.garment [38 words, 9 roles] يَحِلُّ 4:19:5: ح ل ل B007 garment · زَوْجٍۢ 4:20:4: ز و ج B004 garment kind · سَبِيلًا 4:22:17: س ب ل B004 hem · وَعَمَّٰتُكُمْ 4:23:6: ع م م B002 turban · دَخَلْتُم 4:23:27: د خ ل B003 lining · غَفُورًۭا 4:23:53: غ ف ر B001 cloak · +32 more (all: data/scenes/s004/dress.garment.md)
- land.soil [32 words, 9 roles] كَرْهًۭا 4:19:10: ك ر ه B007 barren soil · مُّبَيِّنَةٍۢ 4:19:21: ب ي ن B007 earth · كَثِيرًۭا 4:19:34: ك ث ر B005 dust · تَأْخُذُوا۟ 4:20:11: ء خ ذ B005 land · تَصْبِرُوا۟ 4:25:53: ص ب ر B005 gravel ground · سُنَنَ 4:26:6: س ن ن B005 mud · +26 more (all: data/scenes/s004/land.soil.md)
- agri.orchard [31 words, 9 roles] ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B007 date cluster · شَيْـًۭٔا 4:19:29: ش ي ء B006 palm, ش ي ء B008 palm · غَفُورًۭا 4:23:53: غ ف ر B007 tree · يَسْتَطِعْ 4:25:3: ط و ع B007 ripening fruit · تَصْبِرُوا۟ 4:25:53: ص ب ر B009 tamarind fruit · تَأْكُلُوٓا۟ 4:29:5: ء ك ل B002 fruit · +25 more (all: data/scenes/s004/agri.orchard.md)
- tool.rope [25 words, 9 roles] يَحِلُّ 4:19:5: ح ل ل B001 untying · مِّيثَٰقًا 4:21:10: و ث ق B003 binding · أُمَّهَٰتُكُمْ 4:23:3: ء م م B009 cord · وَأَخَوَٰتُكُمْ 4:23:5: ء خ و B002 tether · وَعَمَّٰتُكُمْ 4:23:6: ع م م B009 tying · وَرَبَٰٓئِبُكُمُ 4:23:20: ر ب ب B016 knot · +19 more (all: data/scenes/s004/tool.rope.md)
- food.cooking [24 words, 9 roles] وَعَاشِرُوهُنَّ 4:19:22: ع ش ر B009 meat · وَيَجْعَلَ 4:19:30: ج ع ل B007 pot · ٱسْتِبْدَالَ 4:20:3: ب د ل B005 food · أَفْضَىٰ 4:21:4: ف ض و B005 meal · أَصْلَٰبِكُمْ 4:23:41: ص ل ب B004 cooking · مَلَكَتْ 4:24:6: م ل ك B001 bread · +18 more (all: data/scenes/s004/food.cooking.md)
- time.day_night [21 words, 9 roles] وَعَاشِرُوهُنَّ 4:19:22: ع ش ر B011 day, ع ش ر B016 night · فَعَسَىٰٓ 4:19:26: ع س ي B004 darkness · ٱسْتَمْتَعْتُم 4:24:23: م ت ع B002 noon · فَتَيَٰتِكُمُ 4:25:15: ف ت ي B005 alternation · أَنفُسَكُمْ 4:29:18: ن ف س B009 dawn · كَبَآئِرَ 4:31:3: ك ب ر B013 forenoon · +15 more (all: data/scenes/s004/time.day_night.md)
- horse.horsemanship [48 words, 8 roles] لِتَذْهَبُوا۟ 4:19:13: ذ ه ب B004 horse · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B002 mane · أَرَدتُّمُ 4:20:2: ر و د B006 bridle · جُنَاحَ 4:23:35: ج ن ح B006 speed · تَبْتَغُوا۟ 4:24:17: ب غ ي B007 rearing · يَسْتَطِعْ 4:25:3: ط و ع B001 docility · +42 more (all: data/scenes/s004/horse.horsemanship.md)
- time.age [48 words, 8 roles] يَحِلُّ 4:19:5: ح ل ل B004 appointed time · مَّكَانَ 4:20:5: ك و ن B005 age · سَلَفَ 4:22:11: س ل ف B001 past, س ل ف B012 age · أُمَّهَٰتُكُمْ 4:23:3: ء م م B008 epoch · ٱسْتَمْتَعْتُم 4:24:23: م ت ع B007 delay · بَعْدِ 4:24:36: ب ع د B002 later period, ب ع د B007 interval · +42 more (all: data/scenes/s004/time.age.md)
- trade.gift [42 words, 8 roles] تَرِثُوا۟ 4:19:8: و ر ث B002 giver · ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B002 gift, ء ت ي B008 bribe · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B005 favour · وَيَجْعَلَ 4:19:30: ج ع ل B005 task reward · قَبْلِكُمْ 4:26:9: ق ب ل B004 recipient · كَرِيمًۭا 4:31:12: ك ر م B008 return gift · +36 more (all: data/scenes/s004/trade.gift.md)
- emotion.pride [40 words, 8 roles] بِفَٰحِشَةٍۢ 4:19:20: ف ح ش B001 shame · مَّكَانَ 4:20:5: ك و ن B004 humility · حُرِّمَتْ 4:23:1: ح ر م B006 honour · وَعَمَّٰتُكُمْ 4:23:6: ع م م B007 arrogance · يُخَفِّفَ 4:28:4: خ ف ف B005 humiliation · كَبَآئِرَ 4:31:3: ك ب ر B003 awe, ك ب ر B005 honour, ك ب ر B006 arrogance · +34 more (all: data/scenes/s004/emotion.pride.md)
- animal.birds [33 words, 8 roles] تَعْضُلُوهُنَّ 4:19:12: ع ض ل B005 egg · مُّبَيِّنَةٍۢ 4:19:21: ب ي ن B013 bird · وَعَاشِرُوهُنَّ 4:19:22: ع ش ر B017 feather · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B001 flock, ع ر ف B002 crest · وَيَجْعَلَ 4:19:30: ج ع ل B010 young bird · جُنَاحَ 4:23:35: ج ن ح B002 wing · +27 more (all: data/scenes/s004/animal.birds.md)
- motion.pace [32 words, 8 roles] أَرَدتُّمُ 4:20:2: ر و د B005 slowness · أُمَّهَٰتُكُمْ 4:23:3: ء م م B008 delay · جُنَاحَ 4:23:35: ج ن ح B006 haste · تَبْتَغُوا۟ 4:24:17: ب غ ي B007 running · طَوْلًا 4:25:5: ط و ل B007 waiting · يَسِيرًا 4:30:13: ي س ر B005 easy gait · +26 more (all: data/scenes/s004/motion.pace.md)
- sign.marking [32 words, 8 roles] مُّبَيِّنَةٍۢ 4:19:21: ب ي ن B004 sign, ب ي ن B005 sign · وَعَاشِرُوهُنَّ 4:19:22: ع ش ر B015 mark · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B003 trace, ع ر ف B008 description, ع ر ف B013 mark · وَخَٰلَٰتُكُمْ 4:23:7: خ و ل B005 mark, خ و ل B007 banner · حُجُورِكُم 4:23:23: ح ج ر B006 brand · تَمِيلُوا۟ 4:27:11: م ي ل B005 signpost · +26 more (all: data/scenes/s004/sign.marking.md)
- water.well [31 words, 8 roles] ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B007 abundant water · مُّبَيِّنَةٍۢ 4:19:21: ب ي ن B006 depth · حُرِّمَتْ 4:23:1: ح ر م B003 well · قَبْلِكُمْ 4:26:9: ق ب ل B007 drawer · لِّلرِّجَالِ 4:32:10: ر ج ل B013 shaft · قَوَّٰمُونَ 4:34:2: ق و م B012 pulley · +25 more (all: data/scenes/s004/water.well.md)
- motion.turning [29 words, 8 roles] ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B009 going back · أَرَدتُّمُ 4:20:2: ر و د B004 returning · بَعْدِ 4:24:36: ب ع د B007 return · قَبْلِكُمْ 4:26:9: ق ب ل B001 turning · تَمِيلُوا۟ 4:27:11: م ي ل B002 wavering · يَسِيرًا 4:30:13: ي س ر B009 twisting · +23 more (all: data/scenes/s004/motion.turning.md)
- pastoral.animal_care [27 words, 8 roles] تَأْخُذُوا۟ 4:20:11: ء خ ذ B007 treating mange · مِّيثَٰقًا 4:21:10: و ث ق B003 tether · حُرِّمَتْ 4:23:1: ح ر م B002 taming · أَصْلَٰبِكُمْ 4:23:41: ص ل ب B006 brand · كِتَٰبَ 4:24:8: ك ت ب B001 restraint · سُنَنَ 4:26:6: س ن ن B006 tending · +21 more (all: data/scenes/s004/pastoral.animal_care.md)
- motion.up_down [25 words, 8 roles] يَحِلُّ 4:19:5: ح ل ل B004 descending · سَلَفَ 4:22:11: س ل ف B014 height · أَصْلَٰبِكُمْ 4:23:41: ص ل ب B005 suspension · ٱسْتَمْتَعْتُم 4:24:23: م ت ع B002 rising · ٱلْعَنَتَ 4:25:50: ع ن ت B005 climbing · ٱلْمَضَاجِعِ 4:34:28: ض ج ع B004 lowering · +19 more (all: data/scenes/s004/motion.up_down.md)
- agri.sowing_harvest [21 words, 8 roles] ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B007 harvest · بِٱلْمَعْرُوفِ 4:19:23: ع ر ف B001 grain · سَلَفَ 4:22:11: س ل ف B010 ploughing · سَبِيلًا 4:22:17: س ب ل B008 ear · تَجْمَعُوا۟ 4:23:43: ج م ع B011 seed · نُكَفِّرْ 4:31:7: ك ف ر B008 sowing · +15 more (all: data/scenes/s004/agri.sowing_harvest.md)
- animal.wild [18 words, 8 roles] وَعَاشِرُوهُنَّ 4:19:22: ع ش ر B008 wild ass · وَيَجْعَلَ 4:19:30: ج ع ل B009 female beast, ج ع ل B010 ostrich · خَيْرًۭا 4:19:33: خ ي ر B006 hyena · حُرِّمَتْ 4:23:1: ح ر م B012 wolf · وَرَبَٰٓئِبُكُمُ 4:23:20: ر ب ب B014 wild cattle · غَفُورًۭا 4:23:53: غ ف ر B005 wild goat · +12 more (all: data/scenes/s004/animal.wild.md)
- craft.wood [16 words, 8 roles] فَعَسَىٰٓ 4:19:26: ع س ي B002 wood · أَرَدتُّمُ 4:20:2: ر و د B006 shaft · أَصْلَٰبِكُمْ 4:23:41: ص ل ب B005 board · فَرِيضَةًۭ 4:24:28: ف ر ض B001 notch · يَفْعَلْ 4:30:2: ف ع ل B003 woodwork, ف ع ل B006 shaft making · نَارًۭا 4:30:8: ن و ر B011 beam · +10 more (all: data/scenes/s004/craft.wood.md)
- water.spring_stream [44 words, 7 roles] ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B004 channel, ء ت ي B005 torrent · ٱللَّهُ 4:19:31: و ل ه~alt B003 flow · كَثِيرًۭا 4:19:34: ك ث ر B004 stream · فَرِيضَةًۭ 4:24:28: ف ر ض B004 water access · أَنفُسَكُمْ 4:29:18: ن ف س B009 overflow · نُكَفِّرْ 4:31:7: ك ف ر B011 spring · +38 more (all: data/scenes/s004/water.spring_stream.md)
- motion.gather_scatter [43 words, 7 roles] تَعْضُلُوهُنَّ 4:19:12: ع ض ل B006 crowd · بِبَعْضِ 4:19:14: ب ع ض B001 dispersal · وَعَاشِرُوهُنَّ 4:19:22: ع ش ر B002 gathering, ع ش ر B005 grouping, ع ش ر B009 dispersal · كَثِيرًۭا 4:19:34: ك ث ر B005 scattering, ك ث ر B007 gathering · ضَعِيفًۭا 4:28:8: ض ع ف B005 dispersion · لِّلرِّجَالِ 4:32:10: ر ج ل B006 swarm · +37 more (all: data/scenes/s004/motion.gather_scatter.md)
- animal.small [41 words, 7 roles] تَعْضُلُوهُنَّ 4:19:12: ع ض ل B008 rat · بِبَعْضِ 4:19:14: ب ع ض B002 insect · وَيَجْعَلَ 4:19:30: ج ع ل B008 beetle · ٱللَّهُ 4:19:31: و ل ه~alt B004 spider · مَلَكَتْ 4:24:6: م ل ك B008 bee · لِّلرِّجَالِ 4:32:10: ر ج ل B006 locust · +35 more (all: data/scenes/s004/animal.small.md)
- emotion.grief_joy [40 words, 7 roles] شَيْـًۭٔا 4:19:29: ش ي ء B004 joy, ش ي ء B005 joy, ش ي ء B007 sorrow, ش ي ء B009 sorrow · ٱللَّهُ 4:19:31: و ل ه~alt B001 grief · أَيْمَٰنُكُمْ 4:24:7: ي م ن B001 happiness · ٱسْتَمْتَعْتُم 4:24:23: م ت ع B001 enjoyment · أَنفُسَكُمْ 4:29:18: ن ف س B002 consolation · بِكُلِّ 4:32:25: ك ل ل B011 gladness · +34 more (all: data/scenes/s004/emotion.grief_joy.md)
- rule.ownership [39 words, 7 roles] تَرِثُوا۟ 4:19:8: و ر ث B002 possession, و ر ث B004 owner · كَرْهًۭا 4:19:10: ك ر ه B003 service · أُمَّهَٰتُكُمْ 4:23:3: ء م م B014 servant · كِتَٰبَ 4:24:8: ك ت ب B005 manumission · حَٰفِظَٰتٌۭ 4:34:17: ح ف ظ B001 custody · عَلِيًّۭا 4:34:39: ع ل و B004 mastery · +33 more (all: data/scenes/s004/rule.ownership.md)
- body.eye [34 words, 7 roles] لِتَذْهَبُوا۟ 4:19:13: ذ ه ب B003 vision · أَرَدتُّمُ 4:20:2: ر و د B007 film over the eye · تَأْخُذُوا۟ 4:20:11: ء خ ذ B007 eye · حُجُورِكُم 4:23:23: ح ج ر B006 eye rim · مُسَٰفِحِينَ 4:24:21: س ف ح B001 weeping · قَبْلِكُمْ 4:26:9: ق ب ل B011 pupil · +28 more (all: data/scenes/s004/body.eye.md)
- travel.departure_return [28 words, 7 roles] يَحِلُّ 4:19:5: ح ل ل B002 lodging · لِتَذْهَبُوا۟ 4:19:13: ذ ه ب B006 departure · ءَاتَيْتُمُوهُنَّ 4:19:16: ء ت ي B001 arrival, ء ت ي B006 guest · سَبِيلًا 4:22:17: س ب ل B002 absence · حَكِيمًۭا 4:24:42: ح ك م B007 return · تَرَكَ 4:33:5: ت ر ك B005 parting · +22 more (all: data/scenes/s004/travel.departure_return.md)
- rule.leadership [25 words, 7 roles] يَحِلُّ 4:19:5: ح ل ل B012 chief · أُمَّهَٰتُكُمْ 4:23:3: ء م م B009 leader · وَرَآءَ 4:24:14: و ر ي B003 counsel · حَكِيمًۭا 4:24:42: ح ك م B002 council, ح ك م B005 deputy · يَتَّبِعُونَ 4:27:8: ت ب ع B009 successor · عَلِيًّۭا 4:34:39: ع ل و B002 notable · +19 more (all: data/scenes/s004/rule.leadership.md)
- body.innards [24 words, 7 roles] وَعَاشِرُوهُنَّ 4:19:22: ع ش ر B009 heart · ٱسْتِبْدَالَ 4:20:3: ب د ل B003 chest · وَبَنَاتُكُمْ 4:23:4: ب ن ي B009 ribs · تَجْمَعُوا۟ 4:23:43: ج م ع B007 belly · وَرَآءَ 4:24:14: و ر ي B001 innards · ضَعِيفًۭا 4:28:8: ض ع ف B003 inside · +18 more (all: data/scenes/s004/body.innards.md)
- sky.bodies [23 words, 7 roles] تَأْخُذُوا۟ 4:20:11: ء خ ذ B008 moon · أَصْلَٰبِكُمْ 4:23:41: ص ل ب B006 constellation · يَتَّبِعُونَ 4:27:8: ت ب ع B008 star · تُنْهَوْنَ 4:31:5: ن ه ي B008 zenith · لِّلرِّجَالِ 4:32:10: ر ج ل B012 sunrise · وَٱلْأَقْرَبُونَ 4:33:7: ق ر ب B002 setting · +17 more (all: data/scenes/s004/sky.bodies.md)
- speech.praise_blame [21 words, 7 roles] بِفَٰحِشَةٍۢ 4:19:20: ف ح ش B003 blame · كَثِيرًۭا 4:19:34: ك ث ر B002 boasting · غَلِيظًۭا 4:21:11: غ ل ظ B002 stern speech · بَعْدِ 4:24:36: ب ع د B004 curse · يُخَفِّفَ 4:28:4: خ ف ف B005 reproach · يَفْعَلْ 4:30:2: ف ع ل B002 praise · +15 more (all: data/scenes/s004/speech.praise_blame.md)
- speech.recitation [21 words, 7 roles] تَرِثُوا۟ 4:19:8: و ر ث B003 transmission · مُّبَيِّنَةٍۢ 4:19:21: ب ي ن B011 pronunciation · كِتَٰبَ 4:24:8: ك ت ب B002 reading · يَتَّبِعُونَ 4:27:8: ت ب ع B004 reciting · نَصِيبٌۭ 4:32:11: ن ص ب B009 chanting · حَٰفِظَٰتٌۭ 4:34:17: ح ف ظ B002 memorising · +15 more (all: data/scenes/s004/speech.recitation.md)
- further scenes, in order (every member in data/scenes/s004/<scene>.md): position.middle (19 words, 7 roles), weather.season (19 words, 7 roles), dress.adornment (15 words, 7 roles), water.thirst_drinking (14 words, 7 roles), trade.debt (13 words, 7 roles), posture.upright (10 words, 7 roles), emotion.love (54 words, 6 roles), pastoral.livestock_wealth (50 words, 6 roles), war.protection (41 words, 6 roles), water.rain_cloud (33 words, 6 roles), body.mouth_throat (29 words, 6 roles), speech.news (29 words, 6 roles), pastoral.herding (27 words, 6 roles), emotion.anger (26 words, 6 roles), life.growing_up (24 words, 6 roles), water.gathered (23 words, 6 roles), trade.measure (21 words, 6 roles), emotion.fear (20 words, 6 roles), sign.counting (19 words, 6 roles), land.cave_pit (17 words, 6 roles), food.eating (16 words, 6 roles), light.light_dark (14 words, 6 roles), land.valley (13 words, 6 roles), fire.heat (7 words, 6 roles), fire.kindling (6 words, 7 roles), rule.kingship (29 words, 5 roles), craft.weaving (21 words, 5 roles), dwelling.furnishing (19 words, 5 roles), land.stone (17 words, 5 roles), agri.pressing (14 words, 5 roles), craft.metal (13 words, 5 roles), weather.wind (13 words, 5 roles), craft.leather (12 words, 5 roles), dwelling.tent_camp (12 words, 5 roles), sound.sounds (12 words, 5 roles), speech.secret (11 words, 5 roles), colour.colours (9 words, 5 roles), race.horse_race (9 words, 5 roles), war.vengeance (9 words, 5 roles), rule.covenant (49 words, 4 roles), ritual.idols_lots (38 words, 4 roles), kin.household (37 words, 4 roles), law.boundary (34 words, 4 roles), food.sweet_fat (27 words, 4 roles), land.desert_sand (27 words, 4 roles), pastoral.milking (23 words, 4 roles), pastoral.grazing (22 words, 4 roles), ritual.sanctuary (21 words, 4 roles), speech.poetry (21 words, 4 roles), sign.writing (18 words, 4 roles), plant.desert (14 words, 4 roles), hunt.chase (11 words, 4 roles), law.reckoning (11 words, 4 roles), trade.hire (11 words, 4 roles), dwelling.hearth (10 words, 4 roles), pastoral.watering_herd (10 words, 4 roles), posture.leaning (7 words, 4 roles), ritual.purity (5 words, 4 roles), travel.open_land (5 words, 4 roles), water.irrigation (11 words, 3 roles), craft.dyeing (10 words, 3 roles), travel.sea (7 words, 3 roles), quantity.full_empty (6 words, 3 roles), ritual.sacrifice (6 words, 3 roles), hunt.trap (4 words, 3 roles), travel.night (4 words, 3 roles), water.washing (4 words, 3 roles), life.rising (3 words, 3 roles), kin.orphan (22 words, 2 roles), new.spatial_position (12 words, 2 roles), know.divination (9 words, 2 roles), water.sea (9 words, 2 roles), drink.wine (7 words, 2 roles), new.sexual_intercourse (7 words, 2 roles), horse.charge_raid (5 words, 2 roles), craft.clay (3 words, 2 roles), new.ability_to_act (2 words, 2 roles), new.acceptance (2 words, 3 roles), new.companionship (2 words, 2 roles), new.pairing (2 words, 2 roles), new.sorcery (2 words, 2 roles), ritual.fasting (2 words, 2 roles), new.adversity (12 words, 1 roles), new.being_occurrence (12 words, 1 roles), new.volition (10 words, 1 roles), new.efficacy (7 words, 1 roles), new.separation (7 words, 1 roles), new.spatial_distance (7 words, 1 roles), new.task_preparation (7 words, 1 roles), new.women_group (7 words, 1 roles), new.sexual_continence (6 words, 1 roles), craft.coating (5 words, 1 roles), new.created_world (5 words, 1 roles), new.imitation (5 words, 1 roles), new.magic_charm (5 words, 1 roles), new.seeking (5 words, 1 roles), new.wrestling (5 words, 1 roles), new.entity (4 words, 1 roles), new.animal_kinds (3 words, 1 roles), new.country_region (3 words, 1 roles), new.eligibility (3 words, 1 roles), new.emotion_aversion (3 words, 1 roles), new.grammar_case (3 words, 1 roles), new.grammar_particle (3 words, 1 roles), new.human_blemish (3 words, 1 roles), new.spatial_front (3 words, 1 roles), new.action_commencement (2 words, 1 roles), new.agreement (2 words, 1 roles), new.appointment (2 words, 1 roles), new.contest (2 words, 1 roles), new.difficulty_burden (2 words, 1 roles), new.genital_anatomy (2 words, 1 roles), new.hair_grooming (2 words, 1 roles), new.making (2 words, 1 roles), new.mutual_consent (2 words, 1 roles), new.patience (2 words, 1 roles), new.search_pursuit (2 words, 1 roles), new.self_prompting (2 words, 1 roles), new.sexual_relations (2 words, 1 roles), new.suitability (2 words, 1 roles)
- abstract scenes, mostly the plain sense (every member in data/scenes/s004/<scene>.md): divine.lordship (47 words, 8 roles), moral.good_evil (71 words, 7 roles), moral.truth_falsehood (21 words, 5 roles), moral.guidance_error (16 words, 5 roles)

## Scenes of this window that reach elsewhere in the surah (at most 10 far words each, new roles first; every member in the file named)

- know.perceiving [614 words in the surah, 53 roles] in this window: 60 words (bewilderment, clarification, discernment, doubt, finding, ignorance, insight, knowing, knowledge, learning, noticing, perceiving, recognising, recollection, unknown) | beyond the neighbourhood, 554 words; roles missing here: appearance, belief, blocked perception, conjecture, deliberate ignoring, deliberation, distinguishing, error, experience, exploiting inattention, forgetting, guessing, hearing, hidden knowledge, ignoring, image, impaired reason, impression, induced unawareness, inexperience, inquiry, inspection, inspiration, intellect, intuition, investigation, judgment, loss of reason, misjudgment, omission, opinion, seeking, supposition, testing, thought, uncertainty, understanding, watcher: وَبَثَّ 4:1:13 investigation · وَقُولُوا۟ 4:5:13 conjecture, thought, belief, inspiration · وَٱبْتَلُوا۟ 4:6:1 recognising, ignoring · وَبِدَارًا 4:6:17 error · +550 more (all: data/scenes/s004/know.perceiving.md)
- body.limbs [808 words in the surah, 59 roles] in this window: 95 words (animal part, arm, back, body, elbow, face, flank, foot, forelock, genitalia, hair, hand, hand and foot, head, head and neck, joint, lap, leg, legs, limb, neck, organ, ribs, stature) | beyond the neighbourhood, 713 words; roles missing here: appendage, armpit, body frame, body skin, chest, crooked leg, ear, earlobe, extended leg, facing, figure, finger, forearm, genitals, grasp, hair trimming, hairline, handshake, haunch, hindquarter, hip, long fingers, nape, neck joint, proportion, scalp, shoulder, side, skin, skin contact, tail, uneven hips, upper part, vein, wrist: تُقْسِطُوا۟ 4:3:4 crooked leg · تَعْدِلُوا۟ 4:3:19 proportion · أَدْنَىٰٓ 4:3:26 chest · وَبِدَارًا 4:6:17 shoulder · +709 more (all: data/scenes/s004/body.limbs.md)
- body.illness [543 words in the surah, 38 roles] in this window: 59 words (contagion, disease, fever, healing, itch, madness, medicine, pain, physician, recovery, surgery, throbbing) | beyond the neighbourhood, 484 words; roles missing here: affliction, ailment, cold, cough, dehydration, derangement, diarrhea, discharge, disease site, dizziness, fainting, healer, hoof pain, infection, irritation, poison, pus, remedy, respiratory disease, seizure, skin disease, spasm, stupor, swelling, tremor, vomiting: ٱتَّقُوا۟ 4:1:3 hoof pain · حَسِيبًۭا 4:6:37 skin disease · حَضَرَ 4:8:2 pus, disease · بُطُونِهِمْ 4:10:10 ailment · +480 more (all: data/scenes/s004/body.illness.md)
- tool.implement [380 words in the surah, 40 roles] in this window: 45 words (axe, comb, cutting tool, device, fire drill, handle, impact, implement, knife, pestle, plug, point, pot lifter, probe) | beyond the neighbourhood, 335 words; roles missing here: bat, boring, equipment, firestick, gear, hook, key, leather tool, lock, mirror, needle, piercing, pin, pulley device, razor, restraint, scissors, seal, sheath, staff, stirrer, stirring tool, target, tray, tube, whetstone: وَقُولُوا۟ 4:5:13 bat · سَدِيدًا 4:9:15 plug, tray · فَوْقَ 4:11:12 gear · تَدْرُونَ 4:11:59 comb, target · +331 more (all: data/scenes/s004/tool.implement.md)
- motion.passage [574 words in the surah, 37 roles] in this window: 56 words (blocked emergence, channel, dislodging, emerging, entering, hidden object, obstruction, passing through, penetrating, plunging, removal, separation, succession, transmission, vanishing) | beyond the neighbourhood, 518 words; roles missing here: approaching, arriving, barrier, being swallowed, cleavage, commencing action, crossing, drawing out, escape, expulsion, extraction, fleeing, going and coming, insertion, interior, leaving, nonarrival, opening, passage, passing, reaching, release: بَلَغُوا۟ 4:6:5 nonarrival · سَدِيدًا 4:9:15 barrier · بُطُونِهِمْ 4:10:10 interior, entering · وَرَسُولَهُۥ 4:13:7 release · +514 more (all: data/scenes/s004/motion.passage.md)
- speech.calling [880 words in the surah, 42 roles] in this window: 91 words (address, addressing, answer, call, command, consultation, cry, digression, entreaty, greeting, insult, invocation, listening, naming, petition, questioner, speech, summons, talk, urging, utterance, warning) | beyond the neighbourhood, 789 words; roles missing here: affirmation, announcement, articulation, assertion, discussion, excuse, imprecation, informing, message, mockery, negotiation, pause, prayer, proclamation, question, request, saying, signal, speaker, whisper: وَقُولُوا۟ 4:5:13 utterance, speaker, saying, negotiation, signal, message · وَكَفَىٰ 4:6:35 assertion · تَدْرُونَ 4:11:59 informing · لَٰمَسْتُمُ 4:43:33 request · +785 more (all: data/scenes/s004/speech.calling.md)
- war.battle [743 words in the surah, 42 roles] in this window: 76 words (army, army flank, captive, charge, combatants, confrontation, defeat, enemy, faction, hardship, infantry, opponent, raid, raiders, rank, readiness, retreat, spoils, toil, victory, volunteer, war, warrior) | beyond the neighbourhood, 667 words; roles missing here: battle, breach, combat, combatant, conflict, courage, dawn raid, engagement, fighter, fighting, killing, muster, rout, siege, standard, stratagem, valor, vanguard, veteran: وَٱبْتَلُوا۟ 4:6:1 valor · حَلِيمٌۭ 4:12:88 battle · فَأَمْسِكُوهُنَّ 4:15:12 fighter · فَٱمْسَحُوا۟ 4:43:41 killing · +663 more (all: data/scenes/s004/war.battle.md)
- war.arms [503 words in the surah, 33 roles] in this window: 61 words (armour, arrow, bow, bow notch, edge, knife, old arrow, piercing, shaft, shield, spear, spear part, striking, sword, sword sheath) | beyond the neighbourhood, 442 words; roles missing here: aim, bow end, bow section, cutting, practice target, quiver, scabbard, sharpening, spear point, spear shaft, spear thrust, sword case, sword combat, sword pommel, unarmed fighter, weapon, weapon spine, weapons: قَلَّ 4:7:14 sword pommel · سَدِيدًا 4:9:15 aim · تَدْرُونَ 4:11:59 practice target · حُدُودُ 4:13:2 armour, edge, sharpening · +438 more (all: data/scenes/s004/war.arms.md)
- sound.sounds [147 words in the surah, 23 roles] in this window: 12 words (listening, noise, rustle, silence, voice) | beyond the neighbourhood, 135 words; roles missing here: bow sound, call, clang, cough, creak, cry, gasp, hum, impact, loud cry, rattle, ringing clay, roar, sigh, sound, thunder, voicing, whisper: تَعُولُوا۟ 4:3:28 cry · قَلَّ 4:7:14 rattle · سَعِيرًۭا 4:10:13 cough · فَوْقَ 4:11:12 gasp · +131 more (all: data/scenes/s004/sound.sounds.md)
- dwelling.building [318 words in the surah, 30 roles] in this window: 40 words (adjacent house, bridge, building, chamber, foundation, house, pillar, roof, square building, threshold, tower, upper part, upper room, wall) | beyond the neighbourhood, 278 words; roles missing here: demolition, door, door attachment, door brace, dwelling place, enclosure, hall, high building, house cleaning, house dweller, kiln, palace, roofed passage, storehouse, structural support, wall extension: حُوبًۭا 4:2:15 hall · سَدِيدًا 4:9:15 wall, door · يَتَوَفَّىٰهُنَّ 4:15:16 kiln · وَلَيْسَتِ 4:18:1 house dweller · +274 more (all: data/scenes/s004/dwelling.building.md)
- body.innards [229 words in the surah, 22 roles] in this window: 24 words (belly, chest, heart, innards, inside, omentum, ribs) | beyond the neighbourhood, 205 words; roles missing here: afflicted heart, artery, belly pain, body core, bowel waste, bowels, breast, defecation, heart-bound desire, kidney, liver, rib, settled heart, stomach, womb: ٱلْخَبِيثَ 4:2:6 bowels · حَلِيمٌۭ 4:12:88 breast · ٱلْغَآئِطِ 4:43:31 defecation · يَشْتَرُونَ 4:44:9 artery · +201 more (all: data/scenes/s004/body.innards.md)
- body.strength [548 words in the surah, 29 roles] in this window: 61 words (body form, build, bulk, capacity, effort, fatigue, fatness, firmness, frailty, freshness, large stature, leanness, muscle, strength, sturdiness) | beyond the neighbourhood, 487 words; roles missing here: body, exertion, lightness, loss of strength, recovery, robustness, soft body, stamina, steadfastness, stiffness, tall stature, toughness, vigor, weakness: تُقْسِطُوا۟ 4:3:4 stiffness · حُدُودُ 4:13:2 firmness, vigor · فَأَمْسِكُوهُنَّ 4:15:12 strength, steadfastness · ٱلْمَوْتُ 4:15:17 loss of strength · +483 more (all: data/scenes/s004/body.strength.md)
- dress.garment [289 words in the surah, 23 roles] in this window: 38 words (apron, cloak, garment, garment kind, hem, lining, turban, uncovered body, veil) | beyond the neighbourhood, 251 words; roles missing here: armour, belt, fastener, flag, leather shirt, protective cloth, rag, rain cloak, sandal, shoe, short tunic, shroud, sleeve, wrapping cloth: ٱتَّقُوا۟ 4:1:3 protective cloth · شُرَكَآءُ 4:12:71 belt · جَنَّٰتٍۢ 4:13:9 veil, shroud · وَأَيْدِيكُمْ 4:43:43 sleeve, garment · +247 more (all: data/scenes/s004/dress.garment.md)
- plant.growth_decay [499 words in the surah, 29 roles] in this window: 51 words (bloom, branch, dry stalk, fruit, greenness, growth, leaf, plant, plant kind, root, shoot, sprout, thickening, tree fruit, undergrowth, withering, young tree) | beyond the neighbourhood, 448 words; roles missing here: decay, dense growth, flower, freshness, frond, herb, leaf growth, regrowth, revived earth, sap, tree, trees: جَنَّٰتٍۢ 4:13:9 trees, growth · فَخُورًا 4:36:32 frond, bloom · ٱلْأَرْضُ 4:42:10 decay · حَدِيثًۭا 4:42:14 freshness · +444 more (all: data/scenes/s004/plant.growth_decay.md)
- time.age [469 words in the surah, 20 roles] in this window: 48 words (age, appointed time, delay, duration, epoch, interval, later period, past) | beyond the neighbourhood, 421 words; roles missing here: beginning, continuance, ending, endpoint, incident, lifespan, month, onset, perpetuity, starting time, time limit, year: أُو۟لُوا۟ 4:8:4 beginning, age · سَعِيرًۭا 4:10:13 onset · ٱلسُّدُسُ 4:11:27 perpetuity · خَٰلِدِينَ 4:13:14 lifespan · +417 more (all: data/scenes/s004/time.age.md)
- body.wound [373 words in the surah, 23 roles] in this window: 53 words (bite, bleeding, blood, crack, fracture, injury, severing, sore, swelling, wound, wounding) | beyond the neighbourhood, 320 words; roles missing here: bloodletting, blow, bruise, cautery mark, clotted blood, fatal wound, healing, incision, menstrual blood, mutilation, scar, striking: مِثْلُ 4:11:6 mutilation · جُلُودُهُم 4:56:10 striking · مُّطَهَّرَةٌۭ 4:57:17 menstrual blood · قَضَيْتَ 4:65:17 fatal wound · +316 more (all: data/scenes/s004/body.wound.md)
- food.cooking [190 words in the surah, 21 roles] in this window: 24 words (bread, clove, cooking, food, food heap, meal, meat, mixture, pot) | beyond the neighbourhood, 166 words; roles missing here: boiling pot, broth, cutting, dish, dried meat, feast, hunger, meal invitation, pot support, roasting, spoiled food, wholesome food: وَثُلَٰثَ 4:3:14 pot support, cooking · مَّرِيٓـًۭٔا 4:4:14 meal, feast · خَلْفِهِمْ 4:9:6 spoiled food · فَوْقَ 4:11:12 dish · +162 more (all: data/scenes/s004/food.cooking.md)
- craft.metal [74 words in the surah, 17 roles] in this window: 13 words (anvil, copper, gold, iron, score) | beyond the neighbourhood, 61 words; roles missing here: dross, hammering, iron column, metal plating, minting, molten metal, rust, shaping, silver, smith, smithing, steel pattern: ٱلْخَبِيثَ 4:2:6 dross · مَآءًۭ 4:43:37 metal plating · فَٱمْسَحُوا۟ 4:43:41 silver · قُلُوبِهِمْ 4:63:7 shaping · +57 more (all: data/scenes/s004/craft.metal.md)
- wealth.property [734 words in the surah, 28 roles] in this window: 85 words (allowance, benefit, desired need, generosity, giving, inheritance, lost animal, need, petitioner, possession, poverty, property, prosperity, provision, stinginess, treasure, wealth) | beyond the neighbourhood, 649 words; roles missing here: abundant provision, deficit, distribution, gain, livelihood, loss, ownership, share, sustenance, value, worldly pursuit: ٱلْقِسْمَةَ 4:8:3 distribution · ٱلسُّدُسُ 4:11:27 share · شُرَكَآءُ 4:12:71 ownership · مَّرْضَىٰٓ 4:43:22 loss · +645 more (all: data/scenes/s004/wealth.property.md)
- land.soil [303 words in the surah, 20 roles] in this window: 32 words (barren soil, dust, earth, fertile soil, fissure, gravel ground, hard ground, land, mud) | beyond the neighbourhood, 271 words; roles missing here: barren land, earth barrier, earth surface, field plot, ground, heap, level ground, retentive soil, revived earth, sinking, wet soil: ٱلْغَآئِطِ 4:43:31 sinking · صَعِيدًۭا 4:43:39 earth surface · نَزَّلْنَا 4:47:7 ground · أَدْبَارِهَآ 4:47:18 field plot · +267 more (all: data/scenes/s004/land.soil.md)
- motion.turning [278 words in the surah, 19 roles] in this window: 29 words (going back, return, returning, rotation, turning, twisting, wavering, withdrawal) | beyond the neighbourhood, 249 words; roles missing here: circling, coiling, deflection, departure, inclination, patrol, recurrence, retreat, reversal, steering, turning away: بِوُجُوهِكُمْ 4:43:42 steering, returning · لَيًّۢا 4:46:15 coiling, turning away, inclination · نَّطْمِسَ 4:47:14 reversal · فَنَرُدَّهَا 4:47:16 return, turning away, recurrence · +245 more (all: data/scenes/s004/motion.turning.md)
- food.eating [164 words in the surah, 17 roles] in this window: 16 words (appetite, eating, feeding, food, hunger, palatable food) | beyond the neighbourhood, 148 words; roles missing here: abstaining, chewing, gulp, morsel, nourishment, ration, scant food, snack, swallowing, taste, tasting: مَّرِيٓـًۭٔا 4:4:14 appetite, swallowing, eating · ٱلسُّفَهَآءَ 4:5:3 gulp · فَأَمْسِكُوهُنَّ 4:15:12 morsel · ٱلْبُيُوتِ 4:15:14 ration · +144 more (all: data/scenes/s004/food.eating.md)
- travel.route [606 words in the surah, 29 roles] in this window: 72 words (bridge, company, destination, deviation, direction, distance, diversion, exhaustion, fork, guide, halt, hazard, leader, main course, road, road surface, traveller, way, waymark) | beyond the neighbourhood, 534 words; roles missing here: caravan company, origin, pace, passage, path, straggler, stray, trace, unfit traveller, unmarked road: حَضَرَ 4:8:2 unfit traveller · خَلْفِهِمْ 4:9:6 straggler, road · لَّدُنْهُ 4:40:13 origin · ٱلضَّلَٰلَةَ 4:44:10 stray · +530 more (all: data/scenes/s004/travel.route.md)
- quantity.more_less [404 words in the surah, 22 roles] in this window: 65 words (abundance, completion, decrease, excess, growth, increase, intensity, large size, largeness, majority, outnumbering, part) | beyond the neighbourhood, 339 words; roles missing here: deficit, density, depletion, fragment, maximum, multitude, overwhelm, pile, remainder, small amount: تَعُولُوا۟ 4:3:28 deficit, excess · إِحْسَٰنًۭا 4:36:8 maximum · فَتِيلًا 4:49:14 small amount · فَرِيقٌۭ 4:77:18 fragment · +335 more (all: data/scenes/s004/quantity.more_less.md)
- tool.vessel [338 words in the surah, 23 roles] in this window: 41 words (basket, bucket, case, container, cup, handle, lid, sack, skin bag, stopper, vessel, vessel rim, waterskin) | beyond the neighbourhood, 297 words; roles missing here: aperture, bowl, capacity, crosspiece, emptying, filling, jar, pot, rim, small box: وَثُلَٰثَ 4:3:14 skin bag, filling · ٱلسُّفَهَآءَ 4:5:3 emptying · قَلَّ 4:7:14 jar · فَوْقَ 4:11:12 bowl · +293 more (all: data/scenes/s004/tool.vessel.md)
- agri.sowing_harvest [206 words in the surah, 18 roles] in this window: 21 words (cultivation, ear, grain, harvest, ploughing, seed, sowing, sprout) | beyond the neighbourhood, 185 words; roles missing here: barren ground, crop, crop remnant, fertile year, field effigy, furrow, grain husk, growth, harvest floor, threshing: وَبِدَارًا 4:6:17 threshing · ٱلْمَوْتُ 4:15:17 barren ground · ٱلْأَرْضُ 4:42:10 growth · لَّعَنَهُمُ 4:46:32 field effigy · +181 more (all: data/scenes/s004/agri.sowing_harvest.md)
- kin.birth_nursing [520 words in the surah, 22 roles] in this window: 56 words (birth, birth order, child, foster child, labour, midwife, mother child separation, newborn, nursing, offspring, postpartum recovery, pregnancy, womb) | beyond the neighbourhood, 464 words; roles missing here: afterbirth, barrenness, birth membrane, conception fluid, mother, postpartum remedy, pregnancy prevention, premature birth, wet nurse: رَقِيبًۭا 4:1:28 barrenness · حَضَرَ 4:8:2 afterbirth · فَأَمْسِكُوهُنَّ 4:15:12 birth membrane · نَزَّلْنَا 4:47:7 conception fluid · +460 more (all: data/scenes/s004/kin.birth_nursing.md)
- travel.mount [481 words in the surah, 22 roles] in this window: 56 words (dismounting, exhaustion, extra load, halter, lameness, leading, load, mount, rein, rider, saddle, taming, urging on) | beyond the neighbourhood, 425 words; roles missing here: animal gait, dismount, girth, injured camel, overload, provisioning camel, resisting restraint, riding, tether: بُطُونِهِمْ 4:10:10 girth · نَزَّلْنَا 4:47:7 dismount · ٱلسَّبْتِ 4:47:24 animal gait · عِندِ 4:78:16 resisting restraint · +421 more (all: data/scenes/s004/travel.mount.md)
- water.rain_cloud [394 words in the surah, 15 roles] in this window: 33 words (cloud, downpour, drizzle, lightning, rain, rain-wind) | beyond the neighbourhood, 361 words; roles missing here: abundant rain, drought, frost, rain-soaked earth, revived earth, runoff, thin cloud, thunder, torrent: نَزَّلْنَا 4:47:7 rain, runoff · جُلُودُهُم 4:56:10 frost · عَزِيزًا 4:56:19 revived earth, downpour · خَطَـًۭٔا 4:92:8 drought · +357 more (all: data/scenes/s004/water.rain_cloud.md)
- pastoral.breeding [363 words in the surah, 20 roles] in this window: 43 words (barrenness, birth, breeding mare, mating, newborn, offspring, pregnancy, stallion, suckling, weaning, young) | beyond the neighbourhood, 320 words; roles missing here: ancestry, fostering aid, labour, lost young, miscarriage, premature birth, rejected young, young animal, young goat: أَعْتَدْنَا 4:18:21 young goat · تَنَٰزَعْتُمْ 4:59:12 mating, ancestry · فَرِيقٌۭ 4:77:18 labour · دَرَجَةًۭ 4:95:22 fostering aid, pregnancy · +316 more (all: data/scenes/s004/pastoral.breeding.md)
- further scenes reaching beyond the neighbourhood (every member in data/scenes/s004/<scene>.md): agri.orchard (261), agri.pressing (73), animal.birds (243), animal.small (344), animal.wild (171), body.eye (287), body.mouth_throat (307), colour.colours (82), craft.clay (39), craft.coating (77), craft.dyeing (61), craft.leather (147), craft.weaving (154), craft.wood (126), divine.lordship (626), dress.adornment (246), drink.wine (64), dwelling.furnishing (178), dwelling.hearth (66), dwelling.settlement (272), dwelling.tent_camp (67), emotion.anger (195), emotion.fear (300), emotion.grief_joy (392), emotion.love (553), emotion.pride (427), fire.heat (79), fire.kindling (64), food.sweet_fat (160), horse.charge_raid (47), horse.horsemanship (298), hunt.chase (107), hunt.trap (49), kin.household (347), kin.lineage (514), kin.marriage (284), kin.orphan (178), know.divination (63), land.cave_pit (96), land.desert_sand (303), land.mountain (222), land.stone (114), land.valley (109), law.boundary (230), law.judgment (443), law.reckoning (173), life.death (493), life.growing_up (190), life.rising (60), light.light_dark (176), moral.good_evil (587), moral.guidance_error (191), moral.truth_falsehood (324), motion.gather_scatter (313), motion.pace (316), motion.up_down (225), new.abandonment (12), new.ability_to_act (13), new.abstract_agreement (2), new.abstract_equivalence (2), new.acceptance (4), new.action (7), new.action_commencement (10), new.adversity (138), new.agreement (13), new.animal_kinds (6), new.appointment (10), new.aversion (5), new.being_occurrence (114), new.calamity (6), new.carcass_sharing (2), new.classification (5), new.companionship (5), new.conduct_manner (9), new.contest (4), new.contiguous_sequence (7), new.country_region (6), new.created_world (27), new.derivation (18), new.desisting (3), new.difficulty_burden (7), new.disposition (4), new.ease_readiness (2), new.efficacy (35), new.eligibility (11), new.entity (17), new.expectation (3), new.form_change (3), new.genital_anatomy (3), new.grammar (10), new.grammar_case (12), new.grammar_particle (6), new.grammatical_particle (7), new.habit (5), new.hair_grooming (8), new.human_blemish (6), new.humanity (2), new.identity_essence (19), new.imitation (23), new.magic_charm (23), new.making (12), new.mutual_consent (4), new.negative_scope (4), new.open_sky (13), new.ordered_succession (16), new.pairing (5), new.patience (6), new.personal_trial (5), new.privy (2), new.proximity (8), new.reciprocal_action (7), new.replacement (3), new.resemblance (4), new.search_pursuit (6), new.seeking (10), new.self_prompting (13), new.separation (37), new.sexual_continence (7), new.sexual_intercourse (27), new.sexual_pursuit (7), new.sexual_relations (6), new.sleep (9), new.social_companionship (8), new.social_disavowal (38), new.social_encounter (8), new.social_separation (5), new.solitude (4), new.sorcery (3), new.spatial_distance (37), new.spatial_extent (23), new.spatial_front (6), new.spatial_position (114), new.speech_delirium (5), new.speech_indecency (5), new.spirit_companion (7), new.state_setting (12), new.suitability (19), new.swimming (3), new.task_preparation (35), new.unity (4), new.volition (33), new.women_group (20), new.workmanship (7), new.wrestling (23), pastoral.animal_care (187), pastoral.grazing (272), pastoral.herding (250), pastoral.livestock_wealth (466), pastoral.milking (218), pastoral.watering_herd (113), plant.desert (135), position.middle (146), posture.leaning (101), posture.upright (85), quantity.full_empty (102), race.horse_race (107), ritual.fasting (17), ritual.idols_lots (365), ritual.prayer (462), ritual.purity (83), ritual.sacrifice (51), ritual.sanctuary (139), rule.covenant (477), rule.kingship (293), rule.leadership (274), rule.obedience (658), rule.ownership (324), sign.counting (174), sign.marking (263), sign.writing (187), sky.bodies (228), speech.news (353), speech.poetry (234), speech.praise_blame (331), speech.recitation (244), speech.secret (117), time.day_night (251), tool.lamp (12), tool.rope (202), trade.debt (141), trade.gift (347), trade.hire (84), trade.measure (186), trade.sale (625), travel.departure_return (303), travel.night (54), travel.open_land (115), travel.sea (52), war.protection (261), war.vengeance (87), water.gathered (213), water.irrigation (80), water.sea (107), water.spring_stream (467), water.thirst_drinking (143), water.washing (41), water.well (250), weather.season (108), weather.wind (128)

## Variant readings

4:19:11 وَلَا → كُرْهًا (kurhan; vw; mutawatir) Ḍamma on kāf shifts from external compulsion (karh) to internal unwillingness (kurh)
4:19:26 فَعَسَىٰٓ → مُبَيَّنَةٍ (mubayyanatin; Pss; mutawatir) Passive participle: "made clear (by others)" vs active "making itself clear"
4:24:13 مَّا → وَأَحَلَّ (wa-aḥalla; Pss; mutawatir) Active voice: "and He (God) made lawful"
4:25:9 ٱلْمُؤْمِنَٰتِ → الْمُحْصِنَاتِ (al-muḥṣināti; Pss; mutawatir) Active participle reading
4:25:37 فَإِنْ → مُحْصِنَاتٍ (muḥṣinātin; Pss; mutawatir) Active participle: "self-fortifying" vs passive "being fortified"
4:25:46 ٱلْعَذَابِ → أَحْصَنَّ (ʾaḥṣanna; Pss; mutawatir) Active voice: "they fortified themselves" (chose chastity) vs passive "they were fortified
4:25:57 غَفُورٌۭ → الْمُحْصِنَاتِ (al-muḥṣināti; Pss; mutawatir) Active participle variant for the reference class
4:29:14 تَرَاضٍۢ → تِجَارَةٌ (tijāratun; CE; mutawatir) Nominative reading: tijāratun as subject of takūna (kāna tāmma = "there exists a trade") r
4:31:12 كَرِيمًۭا → مَدْخَلًا (madkhalan; vw; mutawatir) Fatḥa on mīm (madkhal, Form I noun of place) vs ḍamma (mudkhal, Form IV maṣdar)
4:32:23 ٱللَّهَ → وَسَلُوا (wa-salū; hmz|vw; mutawatir) Hamza elision: wa-salū for wa-sʾalū
4:33:13 إِنَّ → عَاقَدَتْ (ʿāqadat; Vr; mutawatir) Form III mufāʿala: mutual pact-making
4:34:27 فِى → اللهَ (allāha; CE; mutawatir) Accusative reading (allāha instead of allāhu)

## Paths you may read

- classical entries per root: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/entries/<root letters without spaces>.md
- every use of a frequent lemma: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/kwic/
- the Quran text: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/quran.tsv; words: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/words.tsv; lemma index: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/lemmas.tsv
- the whole dictionary: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/branches.tsv
