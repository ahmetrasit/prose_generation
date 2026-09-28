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

# Window 5:1–11 (Covenants, lawful food, and purification)

## Text

5:1| يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَوْفُوا۟ بِٱلْعُقُودِ ۚ أُحِلَّتْ لَكُم بَهِيمَةُ ٱلْأَنْعَٰمِ إِلَّا مَا يُتْلَىٰ عَلَيْكُمْ غَيْرَ مُحِلِّى ٱلصَّيْدِ وَأَنتُمْ حُرُمٌ ۗ إِنَّ ٱللَّهَ يَحْكُمُ مَا يُرِيدُ
5:2| يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُحِلُّوا۟ شَعَٰٓئِرَ ٱللَّهِ وَلَا ٱلشَّهْرَ ٱلْحَرَامَ وَلَا ٱلْهَدْىَ وَلَا ٱلْقَلَٰٓئِدَ وَلَآ ءَآمِّينَ ٱلْبَيْتَ ٱلْحَرَامَ يَبْتَغُونَ فَضْلًۭا مِّن رَّبِّهِمْ وَرِضْوَٰنًۭا ۚ وَإِذَا حَلَلْتُمْ فَٱصْطَادُوا۟ ۚ وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ أَن صَدُّوكُمْ عَنِ ٱلْمَسْجِدِ ٱلْحَرَامِ أَن تَعْتَدُوا۟ ۘ وَتَعَاوَنُوا۟ عَلَى ٱلْبِرِّ وَٱلتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا۟ عَلَى ٱلْإِثْمِ وَٱلْعُدْوَٰنِ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
5:3| حُرِّمَتْ عَلَيْكُمُ ٱلْمَيْتَةُ وَٱلدَّمُ وَلَحْمُ ٱلْخِنزِيرِ وَمَآ أُهِلَّ لِغَيْرِ ٱللَّهِ بِهِۦ وَٱلْمُنْخَنِقَةُ وَٱلْمَوْقُوذَةُ وَٱلْمُتَرَدِّيَةُ وَٱلنَّطِيحَةُ وَمَآ أَكَلَ ٱلسَّبُعُ إِلَّا مَا ذَكَّيْتُمْ وَمَا ذُبِحَ عَلَى ٱلنُّصُبِ وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ ۚ ذَٰلِكُمْ فِسْقٌ ۗ ٱلْيَوْمَ يَئِسَ ٱلَّذِينَ كَفَرُوا۟ مِن دِينِكُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِ ۚ ٱلْيَوْمَ أَكْمَلْتُ لَكُمْ دِينَكُمْ وَأَتْمَمْتُ عَلَيْكُمْ نِعْمَتِى وَرَضِيتُ لَكُمُ ٱلْإِسْلَٰمَ دِينًۭا ۚ فَمَنِ ٱضْطُرَّ فِى مَخْمَصَةٍ غَيْرَ مُتَجَانِفٍۢ لِّإِثْمٍۢ ۙ فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
5:4| يَسْـَٔلُونَكَ مَاذَآ أُحِلَّ لَهُمْ ۖ قُلْ أُحِلَّ لَكُمُ ٱلطَّيِّبَٰتُ ۙ وَمَا عَلَّمْتُم مِّنَ ٱلْجَوَارِحِ مُكَلِّبِينَ تُعَلِّمُونَهُنَّ مِمَّا عَلَّمَكُمُ ٱللَّهُ ۖ فَكُلُوا۟ مِمَّآ أَمْسَكْنَ عَلَيْكُمْ وَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهِ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ سَرِيعُ ٱلْحِسَابِ
5:5| ٱلْيَوْمَ أُحِلَّ لَكُمُ ٱلطَّيِّبَٰتُ ۖ وَطَعَامُ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ حِلٌّۭ لَّكُمْ وَطَعَامُكُمْ حِلٌّۭ لَّهُمْ ۖ وَٱلْمُحْصَنَٰتُ مِنَ ٱلْمُؤْمِنَٰتِ وَٱلْمُحْصَنَٰتُ مِنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلِكُمْ إِذَآ ءَاتَيْتُمُوهُنَّ أُجُورَهُنَّ مُحْصِنِينَ غَيْرَ مُسَٰفِحِينَ وَلَا مُتَّخِذِىٓ أَخْدَانٍۢ ۗ وَمَن يَكْفُرْ بِٱلْإِيمَٰنِ فَقَدْ حَبِطَ عَمَلُهُۥ وَهُوَ فِى ٱلْءَاخِرَةِ مِنَ ٱلْخَٰسِرِينَ
5:6| يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا قُمْتُمْ إِلَى ٱلصَّلَوٰةِ فَٱغْسِلُوا۟ وُجُوهَكُمْ وَأَيْدِيَكُمْ إِلَى ٱلْمَرَافِقِ وَٱمْسَحُوا۟ بِرُءُوسِكُمْ وَأَرْجُلَكُمْ إِلَى ٱلْكَعْبَيْنِ ۚ وَإِن كُنتُمْ جُنُبًۭا فَٱطَّهَّرُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُم مِّنْهُ ۚ مَا يُرِيدُ ٱللَّهُ لِيَجْعَلَ عَلَيْكُم مِّنْ حَرَجٍۢ وَلَٰكِن يُرِيدُ لِيُطَهِّرَكُمْ وَلِيُتِمَّ نِعْمَتَهُۥ عَلَيْكُمْ لَعَلَّكُمْ تَشْكُرُونَ
5:7| وَٱذْكُرُوا۟ نِعْمَةَ ٱللَّهِ عَلَيْكُمْ وَمِيثَٰقَهُ ٱلَّذِى وَاثَقَكُم بِهِۦٓ إِذْ قُلْتُمْ سَمِعْنَا وَأَطَعْنَا ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
5:8| يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُونُوا۟ قَوَّٰمِينَ لِلَّهِ شُهَدَآءَ بِٱلْقِسْطِ ۖ وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ عَلَىٰٓ أَلَّا تَعْدِلُوا۟ ۚ ٱعْدِلُوا۟ هُوَ أَقْرَبُ لِلتَّقْوَىٰ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ خَبِيرٌۢ بِمَا تَعْمَلُونَ
5:9| وَعَدَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ ۙ لَهُم مَّغْفِرَةٌۭ وَأَجْرٌ عَظِيمٌۭ
5:10| وَٱلَّذِينَ كَفَرُوا۟ وَكَذَّبُوا۟ بِـَٔايَٰتِنَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَحِيمِ
5:11| يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱذْكُرُوا۟ نِعْمَتَ ٱللَّهِ عَلَيْكُمْ إِذْ هَمَّ قَوْمٌ أَن يَبْسُطُوٓا۟ إِلَيْكُمْ أَيْدِيَهُمْ فَكَفَّ أَيْدِيَهُمْ عَنكُمْ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ وَعَلَى ٱللَّهِ فَلْيَتَوَكَّلِ ٱلْمُؤْمِنُونَ

## Existing chain map (earlier machine review; the starting point: ground, correct, extend, connect; unranked, partly noisy)

### 1. [P1 5:1-11] Binding, Fulfillment, and Release
invariant: A binding structure governs conduct until it is faithfully completed or explicitly loosened.
- Subchannel A. Obligation as a Tied Structure: A compact is tightened into a durable bond and then brought to completion by performance. | motifs: و ف ي:B001, ع ق د:B002, ع ق د:B001, و ث ق:B002 | at 5:1, 5:7
- Subchannel B. Lawful Release Without Rupture: A restriction is deliberately loosened so that a previously bounded thing may pass into lawful use. | motifs: ح ل ل:B001, ح ل ل:B003, ح ر م:B006, و ث ق:B004 | at 5:1, 5:2, 5:4, 5:5, 5:1-2, 5:7

### 2. [P1 5:1-11] Boundary Marks and Visible Restraint
invariant: A protected status becomes legible by being physically marked or held close to the body.
- Subchannel A. The Marked Offering: A cord is twisted and placed as a visible neck-marker, making protected destination and status publicly recognizable. | motifs: ق ل د:B001, ق ل د:B002, خ ن ق:B002 | at 5:2, 5:3
- Subchannel B. Sanctuary as Held Conduct: Inviolability encloses action, while restraint keeps appetite and pursuit from crossing the marked limit. | motifs: ح ر م:B006, و ث ق:B002, خ ن ق:B002 | at 5:1-2, 5:7, 5:3

### 3. [P1 5:1-11] Purification Across Material Surfaces
invariant: Impurity is removed by a medium passing over exposed bodily surfaces.
- Subchannel A. Washing With Flowing Water: Water reaches the body and actively carries away what obstructs ritual cleanliness. | motifs: ط ه ر:B001, ط ه ر:B003, ط ه ر:B004, غ س ل:B001, م و ه:B001 | at 5:6
- Subchannel B. Clean Earth as a Transfer Medium: In water’s absence, a hand passes clean earth across face and hands to perform the same boundary-clearing function. | motifs: م س ح:B001, ص ع د:B004, و ج ه:B001, ي د ي:B001, ط ي ب:B001 | at 5:6

### 4. [P1 5:1-11] Captured Life and the Threshold of Edibility
invariant: Animal life becomes lawful food through controlled capture and a recognized terminal operation.
- Subchannel A. The Trained Predator Holds for Another: A trained hunting animal pursues, captures, and retains prey for the human recipient. | motifs: ج ر ح:B003, ص ي د:B001, ك ل ب:B002, م س ك:B001, ء ك ل:B001 | at 5:1-2, 5:4
- Subchannel B. Competing Modes of Death: Strangling, beating, falling, goring, and predation are tested against the possibility of a final, deliberate slaughter. | motifs: م و ت:B007, خ ن ق:B001, و ق ذ:B001, ر د ي:B003, ن ط ح:B005, س ب ع:B002, ذ ك و:B003, ذ ب ح:B001 | at 5:3

### 5. [P1 5:1-11] Intimacy as Fortification or Spillage
invariant: Sexual relation is distinguished by whether it is enclosed within a recognized and compensated bond or dispersed outside it.
- Subchannel A. Marriage Builds an Enclosure: Marriage establishes a protected sexual enclosure whose entry is marked by an acknowledged payment. | motifs: ح ص ن:B001, ح ص ن:B002, ح ص ن:B003, ء ج ر:B001, ح ل ل:B006 | at 5:5
- Subchannel B. Uncontained and Secret Access: Intimacy escapes public enclosure either as bodily spillage or as a concealed liaison. | motifs: س ف ح:B001, س ف ح:B002, خ د ن:B001, خ د ن:B002 | at 5:5

### 6. [P1 5:1-11] Justice Arrests Hostile Motion
invariant: Just judgment restrains forces that would otherwise bend testimony or extend violence.
- Subchannel A. Testimony Held to an Even Line: A witness produces judgment while equity prevents hatred from deflecting the measure. | motifs: ش ه د:B002, ق س ط:B001, ع د ل:B001, ع د ل:B002, ح ك م:B002 | at 5:8, 5:1
- Subchannel B. The Withheld Hand: Hatred generates intended aggression, but the reaching hand is intercepted and prevented from completing it. | motifs: ش ن ء:B001, ج ر م:B003, ع د و:B001, ب س ط:B004, ك ف ف:B002, ي د ي:B001 | at 5:2, 5:8, 5:11

### standalone: S14. [Whole-surah] A Bow Is Finished and Stress-Tested
- scene: A bow is softened and smoothed, fitted closely to its string, inspected for cracks, and drawn to test its strength and flexibility. | motifs: ب ن ي:B005, ذ و ق:B003, ك ت م:B003, م س ح:B013 | at 5:6, 5:12, 5:61, 5:95

### standalone: S15. [Whole-surah] Seed Is Covered, Raised, and Ripened
- scene: A cultivator opens fertile soil, covers seed, watches tender growth emerge into ears, and waits until the crop matures and fills with grain. | motifs: ء ر ض:B002, ف ل ح:B003, ك ف ر:B008, ش ك ر:B004, س ب ل:B008, ك ه ل:B002, ل ح م:B011 | at 5:3, 5:6, 5:12, 5:17, 5:35, 5:110

### standalone: S16. [Whole-surah] A Waterskin Is Stitched Leak-Tight
- scene: Hide is pierced, joined with a leather thong, reinforced at the sides, and stitched tightly enough to retain liquid. | motifs: ج و ب:B001, س ي ر:B003, خ م ر:B011, ك ل ب:B006, ك ت م:B004, م س ك:B005, ن ف ع:B002 | at 5:4, 5:61, 5:76, 5:90, 5:96, 5:109

### standalone: S17. [Whole-surah] A Reservoir Directs and Retains Water
- scene: A channel carries water into a constructed basin whose pit, hard floor, and stone or timber barrier retain it for later release. | motifs: ء ج ل:B007, ص ن ع:B006, ح ب س:B003, ء ت ي:B004, خ ل ق:B011, م س ك:B004, و ق ع:B008 | at 5:4, 5:5, 5:14, 5:17, 5:32, 5:91, 5:106

### standalone: S18. [Whole-surah] Milk Is Collected, Set, and Thickened
- scene: Abundant milk is gathered into a vessel, left overnight, thickened into a quiet curd or dense mixture, and reduced to a solid butter-like portion. | motifs: ق ل د:B008, ش ك ر:B003, ء و ل:B005, ب ي ت:B006, ص م م:B020, ض ر ب:B015, ك ع ب:B006, ر ب ب:B006 | at 5:2, 5:6, 5:71, 5:100, 5:106

### standalone: S19. [Whole-surah] A Herd Takes Its Appointed Watering Turn
- scene: A herder drives camels to a marked trough, passes them across it, waters them at the mouth, and returns them according to a recurring allotment. | motifs: ق س س:B004, د خ ل:B007, ق د س:B010, ص ف ح:B010, ق ب ل:B014, ق ل د:B007, ر ب ع:B004, ع ش ر:B006 | at 5:2, 5:5, 5:12, 5:13, 5:21, 5:26, 5:82

### standalone: S20. [Whole-surah] Sorcery Works Through Knots and Diversion
- scene: A practitioner ties threads into charged knots and uses the rite to divert perception from a thing’s proper face. | motifs: س ح ر:B002, ع ق د:B013, ع ق ل:B014 | at 5:1, 5:58, 5:110

### standalone: S21. [Whole-surah] A Sale Is Ratified Palm to Palm
- scene: Two parties complete a transaction by bringing bare hands together in a public handshake. | motifs: ص ف ح:B004, م س ح:B017, ل م س:B001 | at 5:6, 5:13

### standalone: S23. [P1 5:1-11] A Bloodied Standing Stone Redirects Slaughter
- scene: An animal is marked for sacrifice, stilled by a throat-cutting knife, and bled at an erected cult stone. | motifs: ش ع ر:B006, ذ ب ح:B003, س ك ن:B007, ن ص ب:B002 | at 5:2, 5:3, 5:89

### standalone: S24. [P1 5:1-11] A Wedding Moves From Contract to Household
- scene: A marriage is publicly contracted, the bride is conveyed to her husband, a bridal dwelling is raised, and a new household is established. | motifs: م ل ك:B004, ه د ي:B006, ب ن ي:B006, ب ي ت:B010, ء ه ل:B002 | at 5:2, 5:12, 5:15, 5:17

### standalone: S26. [P7 5:87-108] A Padded Garment Is Cut, Filled, and Hemmed
- scene: Cloth is cut with shears, given its first fold, tailored into shape, filled with cotton, sewn, and finished at the edge. | motifs: ق ر ض:B001, ق س م:B007, ق ط ع:B012, و ض ع:B008, ك ف ف:B004 | at 5:11, 5:12, 5:13, 5:33, 5:106

### standalone: S30. [Whole-surah] A Weak-Hocked Mount Cuts Off the Journey
- scene: A mount with a weak hock slows, stops from exhaustion, relies on its companion, and leaves the traveler unable to continue. | motifs: ح ل ل:B014, ق و م:B016, و ك ل:B005, ق ط ع:B006 | at 5:1, 5:11, 5:21, 5:33

### standalone: S32. [Whole-surah] Rain Descends, Travels, and Revives Ground
- scene: Rain moves between cloud and earth, descends and settles, runs from the country that received it into dry country, and raises living growth there. | motifs: س ب ل:B005, ص و ب:B001, ء ت ي:B005, ح ي ي:B002 | at 5:5, 5:12, 5:32, 5:49

### standalone: S33. [Whole-surah] A Hearth Pot Is Supported, Lowered, and Strained
- scene: A cooking pot rests on a third hearth stone, broth cooks over the fire, a cloth protects the hand when the pot is lowered, and liquid is poured through a cloth at serving. | motifs: ث ل ث:B007, ق د ر:B007, ج ع ل:B007, غ ل ل:B008 | at 5:6, 5:17, 5:64, 5:73

## Words (ref surface | root | lemma | pos)

5:1:3 ءَامَنُوٓا۟ | ء م ن | ءَامَنَ | V
5:1:4 أَوْفُوا۟ | و ف ي | أَوْفَىٰ | V
5:1:5 بِٱلْعُقُودِ | ع ق د | عُقُود | N
5:1:6 أُحِلَّتْ | ح ل ل | أَحَلَّ | V
5:1:8 بَهِيمَةُ | ب ه م | بَهِيمَة | N
5:1:9 ٱلْأَنْعَٰمِ | ن ع م | نَّعَم | N
5:1:12 يُتْلَىٰ | ت ل و | تَلَىٰ | V
5:1:14 غَيْرَ | غ ي ر | غَيْر | N
5:1:15 مُحِلِّى | ح ل ل | مُحِلِّى | N
5:1:16 ٱلصَّيْدِ | ص ي د | صَيْد | N
5:1:18 حُرُمٌ | ح ر م | حَرَام | N
5:1:20 ٱللَّهَ | ء ل ه | ٱللَّه | PN
5:1:21 يَحْكُمُ | ح ك م | حَكَمَ | V
5:1:23 يُرِيدُ | ر و د | أَرَادَ | V
5:2:3 ءَامَنُوا۟ | ء م ن | ءَامَنَ | V
5:2:5 تُحِلُّوا۟ | ح ل ل | أَحَلَّ | V
5:2:6 شَعَٰٓئِرَ | ش ع ر | شَعَٰٓئِر | N
5:2:7 ٱللَّهِ | ء ل ه | ٱللَّه | PN
5:2:9 ٱلشَّهْرَ | ش ه ر | شَهْر | N
5:2:10 ٱلْحَرَامَ | ح ر م | حَرَام | ADJ
5:2:12 ٱلْهَدْىَ | ه د ي | هَدْي | N
5:2:14 ٱلْقَلَٰٓئِدَ | ق ل د | قَلَٰٓئِد | N
5:2:16 ءَآمِّينَ | ء م م | آمِّين | N
5:2:17 ٱلْبَيْتَ | ب ي ت | بَيْت | N
5:2:18 ٱلْحَرَامَ | ح ر م | حَرَام | ADJ
5:2:19 يَبْتَغُونَ | ب غ ي | ٱبْتَغَىٰ | V
5:2:20 فَضْلًۭا | ف ض ل | فَضْل | N
5:2:22 رَّبِّهِمْ | ر ب ب | رَبّ | N
5:2:23 وَرِضْوَٰنًۭا | ر ض و | رِضْوَٰن | N
5:2:25 حَلَلْتُمْ | ح ل ل | حَلَلْ | V
5:2:26 فَٱصْطَادُوا۟ | ص ي د | ٱصْطَادُ | V
5:2:28 يَجْرِمَنَّكُمْ | ج ر م | يَجْرِمَ | V
5:2:29 شَنَـَٔانُ | ش ن ء | شَنَـَٔان | N
5:2:30 قَوْمٍ | ق و م | قَوْم | N
5:2:32 صَدُّوكُمْ | ص د د | صَدَّ | V
5:2:34 ٱلْمَسْجِدِ | س ج د | مَسْجِد | N
5:2:35 ٱلْحَرَامِ | ح ر م | حَرَام | ADJ
5:2:37 تَعْتَدُوا۟ | ع د و | ٱعْتَدَىٰ | V
5:2:38 وَتَعَاوَنُوا۟ | ع و ن | تَعَاوَنُ | V
5:2:40 ٱلْبِرِّ | ب ر ر | بِرّ | N
5:2:41 وَٱلتَّقْوَىٰ | و ق ي | تَقْوَى | N
5:2:43 تَعَاوَنُوا۟ | ع و ن | تَعَاوَنُ | V
5:2:45 ٱلْإِثْمِ | ء ث م | إِثْم | N
5:2:46 وَٱلْعُدْوَٰنِ | ع د و | عُدْوَٰن | N
5:2:47 وَٱتَّقُوا۟ | و ق ي | ٱتَّقَىٰ | V
5:2:48 ٱللَّهَ | ء ل ه | ٱللَّه | PN
5:2:50 ٱللَّهَ | ء ل ه | ٱللَّه | PN
5:2:51 شَدِيدُ | ش د د | شَدِيد | N
5:2:52 ٱلْعِقَابِ | ع ق ب | عِقَاب | N
5:3:1 حُرِّمَتْ | ح ر م | حَرَّمَ | V
5:3:3 ٱلْمَيْتَةُ | م و ت | مَيْتَة | N
5:3:4 وَٱلدَّمُ | د م و | دَم | N
5:3:5 وَلَحْمُ | ل ح م | لَحْم | N
5:3:6 ٱلْخِنزِيرِ | خ ن ز ر | خِنزِير | N
5:3:8 أُهِلَّ | ه ل ل | أُهِلَّ | V
5:3:9 لِغَيْرِ | غ ي ر | غَيْر | N
5:3:10 ٱللَّهِ | ء ل ه | ٱللَّه | PN
5:3:12 وَٱلْمُنْخَنِقَةُ | خ ن ق | مُنْخَنِقَة | N
5:3:13 وَٱلْمَوْقُوذَةُ | و ق ذ | مَوْقُوذَة | N
5:3:14 وَٱلْمُتَرَدِّيَةُ | ر د ي | مُتَرَدِّيَة | N
5:3:15 وَٱلنَّطِيحَةُ | ن ط ح | نَّطِيحَة | N
5:3:17 أَكَلَ | ء ك ل | أَكَلَ | V
5:3:18 ٱلسَّبُعُ | س ب ع | سَّبُع | N
5:3:21 ذَكَّيْتُمْ | ذ ك و | ذَكَّيْ | V
5:3:23 ذُبِحَ | ذ ب ح | ذُبِحَ | V
5:3:25 ٱلنُّصُبِ | ن ص ب | نُصُب | N
5:3:27 تَسْتَقْسِمُوا۟ | ق س م | تَسْتَقْسِمُ | V
5:3:28 بِٱلْأَزْلَٰمِ | ز ل م | أَزْلَٰم | N
5:3:30 فِسْقٌ | ف س ق | فِسْق | N
5:3:31 ٱلْيَوْمَ | ي و م | يَوْم | T
5:3:32 يَئِسَ | ي ء س | يَئِسَ | V
5:3:34 كَفَرُوا۟ | ك ف ر | كَفَرَ | V
5:3:36 دِينِكُمْ | د ي ن | دِين | N
5:3:38 تَخْشَوْهُمْ | خ ش ي | خَشِىَ | V
5:3:39 وَٱخْشَوْنِ | خ ش ي | خَشِىَ | V
5:3:40 ٱلْيَوْمَ | ي و م | يَوْم | T
5:3:41 أَكْمَلْتُ | ك م ل | أَكْمَلْ | V
5:3:43 دِينَكُمْ | د ي ن | دِين | N
5:3:44 وَأَتْمَمْتُ | ت م م | أَتَمَّ | V
5:3:46 نِعْمَتِى | ن ع م | نِعْمَة | N
5:3:47 وَرَضِيتُ | ر ض و | رَّضِىَ | V
5:3:49 ٱلْإِسْلَٰمَ | س ل م | إِسْلَٰم | PN
5:3:50 دِينًۭا | د ي ن | دِين | N
5:3:52 ٱضْطُرَّ | ض ر ر | ٱضْطُرَّ | V
5:3:54 مَخْمَصَةٍ | خ م ص | مَخْمَصَة | N
5:3:55 غَيْرَ | غ ي ر | غَيْر | N
5:3:56 مُتَجَانِفٍۢ | ج ن ف | مُتَجَانِف | N
5:3:57 لِّإِثْمٍۢ | ء ث م | إِثْم | N
5:3:59 ٱللَّهَ | ء ل ه | ٱللَّه | PN
5:3:60 غَفُورٌۭ | غ ف ر | غَفُور | N
5:3:61 رَّحِيمٌۭ | ر ح م | رَّحِيم | ADJ
5:4:1 يَسْـَٔلُونَكَ | س ء ل | سَأَلَ | V
5:4:3 أُحِلَّ | ح ل ل | أَحَلَّ | V
5:4:5 قُلْ | ق و ل | قَالَ | V
5:4:6 أُحِلَّ | ح ل ل | أَحَلَّ | V
5:4:8 ٱلطَّيِّبَٰتُ | ط ي ب | طَيِّبَٰت | N
5:4:10 عَلَّمْتُم | ع ل م | عَلَّمَ | V
5:4:12 ٱلْجَوَارِحِ | ج ر ح | جَوَارِح | N
5:4:13 مُكَلِّبِينَ | ك ل ب | مُكَلِّبِين | N
5:4:14 تُعَلِّمُونَهُنَّ | ع ل م | عَلَّمَ | V
5:4:16 عَلَّمَكُمُ | ع ل م | عَلَّمَ | V
5:4:17 ٱللَّهُ | ء ل ه | ٱللَّه | PN
5:4:18 فَكُلُوا۟ | ء ك ل | أَكَلَ | V
5:4:20 أَمْسَكْنَ | م س ك | أَمْسَكَ | V
5:4:22 وَٱذْكُرُوا۟ | ذ ك ر | ذَكَرَ | V
5:4:23 ٱسْمَ | س م و | ٱسْم | N
5:4:24 ٱللَّهِ | ء ل ه | ٱللَّه | PN
5:4:26 وَٱتَّقُوا۟ | و ق ي | ٱتَّقَىٰ | V
5:4:27 ٱللَّهَ | ء ل ه | ٱللَّه | PN
5:4:29 ٱللَّهَ | ء ل ه | ٱللَّه | PN
5:4:30 سَرِيعُ | س ر ع | سَرِيع | N
5:4:31 ٱلْحِسَابِ | ح س ب | حِسَاب | N
5:5:1 ٱلْيَوْمَ | ي و م | يَوْم | T
5:5:2 أُحِلَّ | ح ل ل | أَحَلَّ | V
5:5:4 ٱلطَّيِّبَٰتُ | ط ي ب | طَيِّبَٰت | N
5:5:5 وَطَعَامُ | ط ع م | طَعَام | N
5:5:7 أُوتُوا۟ | ء ت ي | آتَى | V
5:5:8 ٱلْكِتَٰبَ | ك ت ب | كِتَٰب | N
5:5:9 حِلٌّۭ | ح ل ل | حِلّ | N
5:5:11 وَطَعَامُكُمْ | ط ع م | طَعَام | N
5:5:12 حِلٌّۭ | ح ل ل | حِلّ | N
5:5:14 وَٱلْمُحْصَنَٰتُ | ح ص ن | مُحْصَنَٰت | N
5:5:16 ٱلْمُؤْمِنَٰتِ | ء م ن | مُّؤْمِنَٰت | N
5:5:17 وَٱلْمُحْصَنَٰتُ | ح ص ن | مُحْصَنَٰت | N
5:5:20 أُوتُوا۟ | ء ت ي | آتَى | V
5:5:21 ٱلْكِتَٰبَ | ك ت ب | كِتَٰب | N
5:5:23 قَبْلِكُمْ | ق ب ل | قَبْل | N
5:5:25 ءَاتَيْتُمُوهُنَّ | ء ت ي | آتَى | V
5:5:26 أُجُورَهُنَّ | ء ج ر | أَجْر | N
5:5:27 مُحْصِنِينَ | ح ص ن | مُّحْصِنِين | N
5:5:28 غَيْرَ | غ ي ر | غَيْر | N
5:5:29 مُسَٰفِحِينَ | س ف ح | مُسَٰفِحِين | N
5:5:31 مُتَّخِذِىٓ | ء خ ذ | مُتَّخِذ | N
5:5:32 أَخْدَانٍۢ | خ د ن | أَخْدَان | N
5:5:34 يَكْفُرْ | ك ف ر | كَفَرَ | V
5:5:35 بِٱلْإِيمَٰنِ | ء م ن | إِيمَٰن | N
5:5:37 حَبِطَ | ح ب ط | حَبِطَ | V
5:5:38 عَمَلُهُۥ | ع م ل | عَمَل | N
5:5:41 ٱلْءَاخِرَةِ | ء خ ر | آخِر | N
5:5:43 ٱلْخَٰسِرِينَ | خ س ر | خَٰسِرِين | N
5:6:3 ءَامَنُوٓا۟ | ء م ن | ءَامَنَ | V
5:6:5 قُمْتُمْ | ق و م | قَامَ | V
5:6:7 ٱلصَّلَوٰةِ | ص ل و | صَلَوٰة | N
5:6:8 فَٱغْسِلُوا۟ | غ س ل | ٱغْسِلُ | V
5:6:9 وُجُوهَكُمْ | و ج ه | وَجْه | N
5:6:10 وَأَيْدِيَكُمْ | ي د ي | يَد | N
5:6:12 ٱلْمَرَافِقِ | ر ف ق | مَرَافِق | N
5:6:13 وَٱمْسَحُوا۟ | م س ح | ٱمْسَحُ | V
5:6:14 بِرُءُوسِكُمْ | ر ء س | رَأْس | N
5:6:15 وَأَرْجُلَكُمْ | ر ج ل | رِجْل | N
5:6:17 ٱلْكَعْبَيْنِ | ك ع ب | كَعْبَيْن | N
5:6:19 كُنتُمْ | ك و ن | كَانَ | V
5:6:20 جُنُبًۭا | ج ن ب | جُنُب | N
5:6:21 فَٱطَّهَّرُوا۟ | ط ه ر | تَطَهَّرْ | V
5:6:23 كُنتُم | ك و ن | كَانَ | V
5:6:24 مَّرْضَىٰٓ | م ر ض | مَّرِيض | N
5:6:27 سَفَرٍ | س ف ر | سَفَر | N
5:6:29 جَآءَ | ج ي ء | جَآءَ | V
5:6:30 أَحَدٌۭ | ء ح د | أَحَد | N
5:6:33 ٱلْغَآئِطِ | غ و ط | غَآئِط | N
5:6:35 لَٰمَسْتُمُ | ل م س | لَمَسُ | V
5:6:36 ٱلنِّسَآءَ | ن س و | نِسَآء | N
5:6:38 تَجِدُوا۟ | و ج د | وَجَدَ | V
5:6:39 مَآءًۭ | م و ه | مَآء | N
5:6:40 فَتَيَمَّمُوا۟ | ي م م | تَيَمَّمُ | V
5:6:41 صَعِيدًۭا | ص ع د | صَعِيد | N
5:6:42 طَيِّبًۭا | ط ي ب | طَيِّب | ADJ
5:6:43 فَٱمْسَحُوا۟ | م س ح | ٱمْسَحُ | V
5:6:44 بِوُجُوهِكُمْ | و ج ه | وَجْه | N
5:6:45 وَأَيْدِيكُم | ي د ي | يَد | N
5:6:48 يُرِيدُ | ر و د | أَرَادَ | V
5:6:49 ٱللَّهُ | ء ل ه | ٱللَّه | PN
5:6:50 لِيَجْعَلَ | ج ع ل | جَعَلَ | V
5:6:53 حَرَجٍۢ | ح ر ج | حَرَج | N
5:6:55 يُرِيدُ | ر و د | أَرَادَ | V
5:6:56 لِيُطَهِّرَكُمْ | ط ه ر | طَهَّرَ | V
5:6:57 وَلِيُتِمَّ | ت م م | أَتَمَّ | V
5:6:58 نِعْمَتَهُۥ | ن ع م | نِعْمَة | N
5:6:61 تَشْكُرُونَ | ش ك ر | شَكَرَ | V
5:7:1 وَٱذْكُرُوا۟ | ذ ك ر | ذَكَرَ | V
5:7:2 نِعْمَةَ | ن ع م | نِعْمَة | N
5:7:3 ٱللَّهِ | ء ل ه | ٱللَّه | PN
5:7:5 وَمِيثَٰقَهُ | و ث ق | مِّيثَٰق | N
5:7:7 وَاثَقَكُم | و ث ق | وَاثَقَ | V
5:7:10 قُلْتُمْ | ق و ل | قَالَ | V
5:7:11 سَمِعْنَا | س م ع | سَمِعَ | V
5:7:12 وَأَطَعْنَا | ط و ع | أَطَاعَ | V
5:7:13 وَٱتَّقُوا۟ | و ق ي | ٱتَّقَىٰ | V
5:7:14 ٱللَّهَ | ء ل ه | ٱللَّه | PN
5:7:16 ٱللَّهَ | ء ل ه | ٱللَّه | PN
5:7:17 عَلِيمٌۢ | ع ل م | عَلِيم | N
5:7:19 ٱلصُّدُورِ | ص د ر | صَدْر | N
5:8:3 ءَامَنُوا۟ | ء م ن | ءَامَنَ | V
5:8:4 كُونُوا۟ | ك و ن | كَانَ | V
5:8:5 قَوَّٰمِينَ | ق و م | قَوَّٰمِين | N
5:8:6 لِلَّهِ | ء ل ه | ٱللَّه | PN
5:8:7 شُهَدَآءَ | ش ه د | شَهِيد | N
5:8:8 بِٱلْقِسْطِ | ق س ط | قِسْط | N
5:8:10 يَجْرِمَنَّكُمْ | ج ر م | يَجْرِمَ | V
5:8:11 شَنَـَٔانُ | ش ن ء | شَنَـَٔان | N
5:8:12 قَوْمٍ | ق و م | قَوْم | N
5:8:15 تَعْدِلُوا۟ | ع د ل | عَدَلَ | V
5:8:16 ٱعْدِلُوا۟ | ع د ل | عَدَلَ | V
5:8:18 أَقْرَبُ | ق ر ب | أَقْرَب | N
5:8:19 لِلتَّقْوَىٰ | و ق ي | تَقْوَى | N
5:8:20 وَٱتَّقُوا۟ | و ق ي | ٱتَّقَىٰ | V
5:8:21 ٱللَّهَ | ء ل ه | ٱللَّه | PN
5:8:23 ٱللَّهَ | ء ل ه | ٱللَّه | PN
5:8:24 خَبِيرٌۢ | خ ب ر | خَبِير | N
5:8:26 تَعْمَلُونَ | ع م ل | عَمِلَ | V
5:9:1 وَعَدَ | و ع د | وَعَدَ | V
5:9:2 ٱللَّهُ | ء ل ه | ٱللَّه | PN
5:9:4 ءَامَنُوا۟ | ء م ن | ءَامَنَ | V
5:9:5 وَعَمِلُوا۟ | ع م ل | عَمِلَ | V
5:9:6 ٱلصَّٰلِحَٰتِ | ص ل ح | صَّٰلِحَٰت | N
5:9:8 مَّغْفِرَةٌۭ | غ ف ر | مَّغْفِرَة | N
5:9:9 وَأَجْرٌ | ء ج ر | أَجْر | N
5:9:10 عَظِيمٌۭ | ع ظ م | عَظِيم | ADJ
5:10:2 كَفَرُوا۟ | ك ف ر | كَفَرَ | V
5:10:3 وَكَذَّبُوا۟ | ك ذ ب | كَذَّبَ | V
5:10:4 بِـَٔايَٰتِنَآ | ء ي ي | ءَايَة | N
5:10:6 أَصْحَٰبُ | ص ح ب | أَصْحَٰب | N
5:10:7 ٱلْجَحِيمِ | ج ح م | جَحِيم | N
5:11:3 ءَامَنُوا۟ | ء م ن | ءَامَنَ | V
5:11:4 ٱذْكُرُوا۟ | ذ ك ر | ذَكَرَ | V
5:11:5 نِعْمَتَ | ن ع م | نِعْمَة | N
5:11:6 ٱللَّهِ | ء ل ه | ٱللَّه | PN
5:11:9 هَمَّ | ه م م | هَمَّ | V
5:11:10 قَوْمٌ | ق و م | قَوْم | N
5:11:12 يَبْسُطُوٓا۟ | ب س ط | بَسَطَ | V
5:11:14 أَيْدِيَهُمْ | ي د ي | يَد | N
5:11:15 فَكَفَّ | ك ف ف | كَفَّ | V
5:11:16 أَيْدِيَهُمْ | ي د ي | يَد | N
5:11:18 وَٱتَّقُوا۟ | و ق ي | ٱتَّقَىٰ | V
5:11:19 ٱللَّهَ | ء ل ه | ٱللَّه | PN
5:11:21 ٱللَّهِ | ء ل ه | ٱللَّه | PN
5:11:22 فَلْيَتَوَكَّلِ | و ك ل | تَوَكَّلْ | V
5:11:23 ٱلْمُؤْمِنُونَ | ء م ن | مُؤْمِن | N

## Dictionary: every branch of every root (branch | image). A long window, so images only: each branch's definition and classical phrases are in /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/branches.tsv (Grep the root, e.g. "ق و م\tB012"); full entries in data/entries/

### ء م ن — 879 uses; here: 5:1:3 ءَامَنُوٓا۟; 5:2:3 ءَامَنُوا۟; 5:5:16 ٱلْمُؤْمِنَٰتِ; 5:5:35 بِٱلْإِيمَٰنِ; 5:6:3 ءَامَنُوٓا۟; 5:8:3 ءَامَنُوا۟; 5:9:4 ءَامَنُوا۟; 5:11:3 ءَامَنُوا۟; 5:11:23 ٱلْمُؤْمِنُونَ
B001 | سكون القلب في أمن وثقة
B002 | تصديق يطمئن إليه القلب
B003 | قول آمين طلبا للاستجابة

### و ف ي — 66 uses; here: 5:1:4 أَوْفُوا۟
B001 | التمام الوافي بلا نقص
B002 | قبض النفس على وجه التوفي
B003 | البلوغ إلى علو والإشراف منه
B004 | الموافاة إتيان الموعد والاجتماع عليه
B005 | الميفى غطاء التنور وبيت الآجر

### ع ق د — 7 uses; here: 5:1:5 بِٱلْعُقُودِ
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

### ح ل ل — 51 uses; here: 5:1:6 أُحِلَّتْ; 5:1:15 مُحِلِّى; 5:2:5 تُحِلُّوا۟; 5:2:25 حَلَلْتُمْ; 5:4:3 أُحِلَّ; 5:4:6 أُحِلَّ; 5:5:2 أُحِلَّ; 5:5:9 حِلٌّۭ; 5:5:12 حِلٌّۭ
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

### ب ه م — 3 uses; here: 5:1:8 بَهِيمَةُ
B001 | الإبهام والاستغلاق
B002 | الخلو من العلامة والاختلاط
B003 | الحي غير المميز
B004 | صغار الأنعام
B005 | الصخرة والشجاع الذي لا يؤتى
B006 | إبهام الكف
B007 | البهمى والمرعى
B008 | ملازمة الموضع

### ن ع م — 140 uses; here: 5:1:9 ٱلْأَنْعَٰمِ; 5:3:46 نِعْمَتِى; 5:6:58 نِعْمَتَهُۥ; 5:7:2 نِعْمَةَ; 5:11:5 نِعْمَتَ
B001 | حسن الحال والنعمة
B002 | اللين والنعومة ورفاه العيش
B003 | مدح الشيء بنعم
B004 | الجواب بنعم والتصديق
B005 | مال الأنعام والإبل
B006 | النعام والنعامة الطائر
B007 | ما سمي نعامة تشبيها بالهيئة
B008 | طيران النعامة وتفرق القوم
B009 | النعامى ريح لينة
B010 | زاد وأنعم في الفعل
B011 | موافقة المكان وطيب المقام
B012 | المشي على القدم وابتذالها
B013 | نعم الله بك عينا وقرة العين

### ت ل و — 63 uses; here: 5:1:12 يُتْلَىٰ
B001 | اتباع وتتابع
B002 | تلاوة متبوعة
B003 | بقية تتلو ما قبلها
B004 | ذمة أو حق يتبع صاحبه
B005 | ترك بعد صحبة
B006 | ولد يتلو أمه
B007 | صوت يتلو صوتا
B008 | آخر رمق
B009 | قول كذب على غيره

### غ ي ر — 154 uses; here: 5:1:14 غَيْرَ; 5:3:9 لِغَيْرِ; 5:3:55 غَيْرَ; 5:5:28 غَيْرَ
B001 | الصلاح والمنفعة بالميرة والسقي والإصلاح
B002 | الغَيْر في الدية
B003 | تغيير الصورة أو إبدال الشيء بغيره
B004 | الغَيْرة على الأهل
B005 | السوى والخلاف والاستثناء والنفي

### ص ي د — 6 uses; here: 5:1:16 ٱلصَّيْدِ; 5:2:26 فَٱصْطَادُوا۟
B001 | طلب الممتنع وأخذه
B002 | رفع الرأس وترك الالتفات
B003 | الصيدانة المنفرة
B004 | الصاد من المعدن
B005 | حجارة القدور والغلظ
B006 | اسم الحرف صاد
B007 | تلقّي الشيء بالقبول

### ح ر م — 83 uses; here: 5:1:18 حُرُمٌ; 5:2:10 ٱلْحَرَامَ; 5:2:18 ٱلْحَرَامَ; 5:2:35 ٱلْحَرَامِ; 5:3:1 حُرِّمَتْ
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

### ء ل ه — 2851 uses; here: 5:1:20 ٱللَّهَ; 5:2:7 ٱللَّهِ; 5:2:48 ٱللَّهَ; 5:2:50 ٱللَّهَ; 5:3:10 ٱللَّهِ; 5:3:59 ٱللَّهَ; 5:4:17 ٱللَّهُ; 5:4:24 ٱللَّهِ; 5:4:27 ٱللَّهَ; 5:4:29 ٱللَّهَ; 5:6:49 ٱللَّهُ; 5:7:3 ٱللَّهِ; 5:7:14 ٱللَّهَ; 5:7:16 ٱللَّهَ; 5:8:6 لِلَّهِ; 5:8:21 ٱللَّهَ; 5:8:23 ٱللَّهَ; 5:9:2 ٱللَّهُ; 5:11:6 ٱللَّهِ; 5:11:19 ٱللَّهَ; 5:11:21 ٱللَّهِ
B001 | التعبد والمعبود
B002 | اسم الله في القسم والنداء

### و ل ه ~alt (documented alternative analysis) — 0 uses; here: 5:1:20 ٱللَّهَ; 5:2:7 ٱللَّهِ; 5:2:48 ٱللَّهَ; 5:2:50 ٱللَّهَ; 5:3:10 ٱللَّهِ; 5:3:59 ٱللَّهَ; 5:4:17 ٱللَّهُ; 5:4:24 ٱللَّهِ; 5:4:27 ٱللَّهَ; 5:4:29 ٱللَّهَ; 5:6:49 ٱللَّهُ; 5:7:3 ٱللَّهِ; 5:7:14 ٱللَّهَ; 5:7:16 ٱللَّهَ; 5:8:6 لِلَّهِ; 5:8:21 ٱللَّهَ; 5:8:23 ٱللَّهَ; 5:9:2 ٱللَّهُ; 5:11:6 ٱللَّهِ; 5:11:19 ٱللَّهَ; 5:11:21 ٱللَّهِ
B001 | الوَلَه والحيرة
B002 | تَوْلِيه الوالدة عن ولدها
B003 | ماء مُولَه ذاهب
B004 | المُولَه العنكبوت

### ح ك م — 210 uses; here: 5:1:21 يَحْكُمُ
B001 | المنع والرد للإصلاح
B002 | الحكم والقضاء بين الناس
B003 | الحكمة والعلم المصيب
B004 | الإحكام والإتقان والوثاقة
B005 | التفويض والتحكيم
B006 | حكمة اللجام
B007 | الرجوع والإرجاع عن الشيء

### ر و د — 148 uses; here: 5:1:23 يُرِيدُ; 5:6:48 يُرِيدُ; 5:6:55 يُرِيدُ
B001 | الإرادة والمشيئة
B002 | المراودة على الفعل
B003 | طلب الشيء وارتياده
B004 | التردد والاختلاف جيئة وذهابا
B005 | الرفق والمهل
B006 | أدوات الإدارة والدوران
B007 | عوار العين الرائد
B008 | الجارية الرود الشابة

### ش ع ر — 40 uses; here: 5:2:6 شَعَٰٓئِرَ
B001 | الشَّعر النابت وما عليه زغب
B002 | نبات كثيف كالشَّعر
B003 | حبة الشعير وما يشبهها
B004 | شعار يلاصق الجسد
B005 | علم دقيق وفطنة
B006 | علامة مشعرة وشعيرة نسك
B007 | قريض وشاعر
B008 | أسماء مخصوصة منقولة

### ش ه ر — 21 uses; here: 5:2:9 ٱلشَّهْرَ
B001 | الشهر المعلوم بالهلال
B002 | شهرة الشيء وظهوره
B003 | شَهْر السيف وإظهاره

### ه د ي — 316 uses; here: 5:2:12 ٱلْهَدْىَ
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

### ق ل د — 4 uses; here: 5:2:14 ٱلْقَلَٰٓئِدَ
B001 | فتل الشيء وليه على الشيء
B002 | قلادة في العنق علامة أو زينة
B003 | تقلد السيف وحمله على البدن
B004 | إلزام الأمر وجعله في العنق
B005 | وسم السوء بالهجاء كقلادة لازمة
B006 | مقاليد تحفظ وتفتح ما تحتها
B007 | حظ الماء ونوبة السقي أو المطر
B008 | جمع الماء أو اللبن في وعاء
B009 | إغلاق البحر على من في جوفه
B010 | تقليد السيف ضربا للعنق

### ء م م — 119 uses; here: 5:2:16 ءَآمِّينَ
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

### ب ي ت — 73 uses; here: 5:2:17 ٱلْبَيْتَ
B001 | المأوى والمسكن
B002 | أهل البيت وعياله
B003 | بيت الشعر
B004 | عمل الليل وتدبيره
B005 | قوت ليلة
B006 | شيء بات ليلة
B007 | القبر بيت
B008 | بيت الشرف
B009 | جوار بيت بيت
B010 | بيت الزواج

### ب غ ي — 96 uses; here: 5:2:19 يَبْتَغُونَ
B001 | طلب الشيء وابتغاؤه
B002 | الانبغاء والمطاوعة لما يليق أو يتيسر
B003 | تجاوز الحد بالعدوان والظلم
B004 | فساد الجرح وتجاوزه
B005 | البغاء والفجور الجنسي
B006 | شدة المطر ومعظمه
B007 | اختيال الفرس ومرحه في العدو
B008 | البغايا الطلائع

### ف ض ل — 104 uses; here: 5:2:20 فَضْلًۭا
B001 | الزيادة والبقية
B002 | الدرجة والفضيلة
B003 | الإحسان والعطية
B004 | ادعاء الفضل
B005 | التوشح بالثوب

### ر ب ب — 980 uses; here: 5:2:22 رَّبِّهِمْ
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

### ر ض و — 73 uses; here: 5:2:23 وَرِضْوَٰنًۭا; 5:3:47 وَرَضِيتُ
B001 | الرضا خلاف السخط
B002 | الرضوان والمرضاة اسم للرضا الكثير أو المطلوب
B003 | المراضاة والتراضي رضا متبادل
B004 | الإرضاء طلب رضا الغير وإزالة سخطه
B005 | راضاني فرضوته غلبة في ذلك
B006 | الرضي صفة للمطيع أو المحب أو الضامن
B007 | رضوى ورضيا أعلام من المادة

### ج ر م — 66 uses; here: 5:2:28 يَجْرِمَنَّكُمْ; 5:8:10 يَجْرِمَنَّكُمْ
B001 | القطع والصرام
B002 | مخلفات الصرام وثمره اليابس
B003 | الكسب والإكساب
B004 | الذنب والجناية
B005 | لا جرم تحقيقا ولزوما
B006 | تمام الزمن وانقطاعه
B007 | جرم البدن وقدره
B008 | جرم الصوت وخروجه
B009 | صفاء اللون
B010 | الحر والبلد الحار
B011 | جرم وجارم أسماء قبائل

### ش ن ء — 3 uses; here: 5:2:29 شَنَـَٔانُ; 5:8:11 شَنَـَٔانُ
B001 | البغضة والعداوة
B002 | التقزز والتباعد
B003 | إقرار الحق وإخراجه
B004 | وصف البغيض أو القبيح

### ق و م — 660 uses; here: 5:2:30 قَوْمٍ; 5:6:5 قُمْتُمْ; 5:8:5 قَوَّٰمِينَ; 5:8:12 قَوْمٍ; 5:11:10 قَوْمٌ
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

### ص د د — 42 uses; here: 5:2:32 صَدُّوكُمْ
B001 | إعراض وصرف
B002 | جانبان مائلان
B003 | مقابلة وقرب
B004 | طريق إلى الماء
B005 | جبل حاجز
B006 | ضجيج وجلبة
B007 | صديد الجرح
B008 | دويبة صغيرة
B009 | اسم امرأة
B010 | ماء مسمى
B011 | تصفيق
B012 | ستر المرأة
B013 | كحل المرآة

### س ج د — 92 uses; here: 5:2:34 ٱلْمَسْجِدِ
B001 | التطامن والذل
B002 | موضع السجود ومصلاه
B003 | أعضاء السجود وأثره
B004 | طأطأة الرأس والانحناء
B005 | إدامة النظر وفتور الطرف
B006 | دراهم الصور المسجود لها
B007 | الإسجاد والجزية

### ع د و — 106 uses; here: 5:2:37 تَعْتَدُوا۟; 5:2:46 وَٱلْعُدْوَٰنِ
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

### ع و ن — 11 uses; here: 5:2:38 وَتَعَاوَنُوا۟; 5:2:43 تَعَاوَنُوا۟
B001 | الإعانة والمظاهرة
B002 | العَوان بين السنين
B003 | الحرب العَوان
B004 | النخلة العَوانة القديمة
B005 | استواء الخلقة وتلاحق القوة
B006 | العانة قطيع الحمر
B007 | عانة الرجل
B008 | النسبة إلى عانة

### ب ر ر — 32 uses; here: 5:2:40 ٱلْبِرِّ
B001 | صدق يمضي القول والعمل
B002 | خير وطاعة متسعة
B003 | صلة وإحسان ضد العقوق
B004 | صوت وجلبة باللسان
B005 | يابسة وصحراء
B006 | حب وحنطة
B007 | ثمر الأراك
B008 | غلبة وعلو

### و ق ي — 258 uses; here: 5:2:41 وَٱلتَّقْوَىٰ; 5:2:47 وَٱتَّقُوا۟; 5:4:26 وَٱتَّقُوا۟; 5:7:13 وَٱتَّقُوا۟; 5:8:19 لِلتَّقْوَىٰ; 5:8:20 وَٱتَّقُوا۟; 5:11:18 وَٱتَّقُوا۟
B001 | دفع الضرر بوقاية
B002 | جعل النفس في وقاية
B003 | توقي الدابة من وجع الحافر
B004 | الأوقية وزن معلوم
B005 | الواقي اسم للصرد

### ء ث م — 48 uses; here: 5:2:45 ٱلْإِثْمِ; 5:3:57 لِّإِثْمٍۢ
B001 | البطء والتأخر عن الخير
B002 | التأثم كف عن الإثم
B003 | الأثام عقوبة الإثم
B004 | تحميل الإثم وعده عليه
B005 | الإثم اسما للخمر

### ش د د — 102 uses; here: 5:2:51 شَدِيدُ
B001 | شد العقد والوثاق
B002 | شدة القوة والصلابة
B003 | شد الحملة والعدو
B004 | بلوغ الأشد
B005 | شد النهار وارتفاعه
B006 | شدة البخل

### ع ق ب — 80 uses; here: 5:2:52 ٱلْعِقَابِ
B001 | العَقَب الأبيض الشديد
B002 | مؤخر القدم والأثر
B003 | الرجوع على العقب
B004 | العَقِب من الولد
B005 | الخلف والتعاقب
B006 | آخر الشيء وعاقبته
B007 | العقوبة بعد الذنب
B008 | التعقب والمراجعة
B009 | العود مرة بعد مرة
B010 | العقبة بدلا وضمانا
B011 | بقية الشيء وأثره
B012 | العقبة الصعبة والناشز
B013 | العقاب الجارح والراية
B014 | يعقوب واليعقوب
B015 | اصفرار النبت ويبس العود

### م و ت — 165 uses; here: 5:3:3 ٱلْمَيْتَةُ
B001 | ذهاب القوة والحياة
B002 | إذهاب القوة بالإماتة
B003 | أرض موات ومتاع لا روح فيه
B004 | مُوتان واقع في الناس أو المال
B005 | موت الولد للوالد أو الناقة
B006 | موتان الفؤاد
B007 | الميتة بلا ذكاة
B008 | ميتة الحال وواحدة الموت
B009 | الموتة جنون وغشية
B010 | استماتة في الأمر والموت
B011 | إظهار الموت والخشوع كذبا
B012 | سكون وخمود كنوم أو بلى
B013 | الخضوع للحق
B014 | استبانة موت الصيد

### د م و — 10 uses; here: 5:3:4 وَٱلدَّمُ
B001 | الدم المعروف
B002 | خروج الدم والجرح الدامي
B003 | حمرة الدم والتدمية
B004 | استدماء الرفق ونزف الأنف

### ل ح م — 12 uses; here: 5:3:5 وَلَحْمُ
B001 | اللحم المعروف
B002 | لحم البدن وشهوة اللحم
B003 | إطعام اللحم ورزق الصيد
B004 | القتل حتى يصير المقتول لحما
B005 | لأم الشيء وإلصاقه
B006 | لحمة الثوب والنسيج
B007 | لحمة النسب والولاء
B008 | الشجة تبلغ اللحم وتلتحم
B009 | قشر اللحم عن العظم
B010 | تمكين عرض الإنسان كأنه لحم
B011 | استلحام الزرع وظهور حبه
B012 | الفتل الشديد والتداخل المحكم
B013 | استلحام الطريق واتباعه
B014 | النشوب والالتصاق بالقوم أو المكان

### خ ن ز ر — 5 uses; here: 5:3:6 ٱلْخِنزِيرِ
B001 | الخنزير المعروف
B002 | التَّخَنْزُر كفعل الخنازير

### ه ل ل — 5 uses; here: 5:3:8 أُهِلَّ
B001 | الهلال في أول ظهوره
B002 | الثوب الرقيق المفكك
B003 | انصباب المطر والدمع
B004 | رفع الصوت بالإهلال
B005 | بريق يظهر على السحاب أو الوجه
B006 | النكوص والفزع
B007 | هَلْ أداة استخبار وتنبيه
B008 | هَلا وحَيهَل للحث والنداء
B009 | ماء كثير صاف

### خ ن ق — 1 uses; here: 5:3:12 وَٱلْمُنْخَنِقَةُ
B001 | خنق العنق
B002 | مخنقة العنق
B003 | مضيق خانق
B004 | داء الخناق
B005 | تخنيق الحوض

### و ق ذ — 1 uses; here: 5:3:13 وَٱلْمَوْقُوذَةُ
B001 | ضرب مثخن يوجع أو يميت
B002 | ثقل الدنف والإشراف
B003 | نعاس يثقل ويغلب
B004 | ضرع ناقة يؤثر فيه الرضاع أو الصرار
B005 | تسكين وإثخان يمنع
B006 | موضع ضربة موقذة

### ر د ي — 6 uses; here: 5:3:14 وَٱلْمُتَرَدِّيَةُ
B001 | الرمي بالحجر والصخرة
B002 | الترامي في العدو والقفز
B003 | السقوط إلى الهلاك
B004 | الرداء وما يلازم المنكبين
B005 | الزيادة على القدر
B006 | المراودة والمداراة

### ن ط ح — 1 uses; here: 5:3:15 وَٱلنَّطِيحَةُ
B001 | اصطدام بقرن أو مقابلة تصادم
B002 | حيوان يستقبل وجهك في الزجر
B003 | علامة نطيح يتشاءم بها
B004 | شدائد تنطح صاحبها
B005 | نطيحة ماتت من النطح
B006 | ناطح في مثل لا مال له

### ء ك ل — 109 uses; here: 5:3:17 أَكَلَ; 5:4:18 فَكُلُوا۟
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

### س ب ع — 28 uses; here: 5:3:18 ٱلسَّبُعُ
B001 | العدد سبعة وما يتفرع منه
B002 | السبع الحيوان المفترس
B003 | الوقيعة والاغتياب كأذى السبع
B004 | المسبع: وصف ملتبس بين الإهمال والسباع والنسب
B005 | فعل سبعة: المبالغة في الأخذ والشر

### ذ ك و — 1 uses; here: 5:3:21 ذَكَّيْتُمْ
B001 | حدّة الفهم
B002 | إذكاء النار
B003 | تمام الذبح
B004 | تمام السن
B005 | ضوء ذكاء
B006 | إرسال العيون

### ذ ب ح — 9 uses; here: 5:3:23 ذُبِحَ
B001 | شق الحلق للذبح
B002 | فتح الشيء وشقه
B003 | موضع الذبح وآلته ومقام القربان
B004 | مذابح الماء في الأرض
B005 | ذُباح الأصابع
B006 | ذُبحة الحلق وخنقه
B007 | نبات الذبح والذباح
B008 | سعد الذابح
B009 | أثر الذبح على الحلق واللحية

### ن ص ب — 32 uses; here: 5:3:25 ٱلنُّصُبِ
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

### ق س م — 33 uses; here: 5:3:27 تَسْتَقْسِمُوا۟
B001 | حسن موزع في الوجه
B002 | حر الهاجرة
B003 | إفراز النصيب وتقسيم الشيء
B004 | يمين مقسومة على أهلها
B005 | طلب القسم بالأزلام
B006 | بال مقسم بين وجوه الأمر
B007 | طي القسامي أول الثوب
B008 | هدنة قسامة

### ز ل م — 2 uses; here: 5:3:28 بِٱلْأَزْلَٰمِ
B001 | قداح الاستقسام
B002 | القدح المبري المصقول
B003 | نحافة الهيئة وخفتها
B004 | زوائد دقيقة متدلية أو خلف الظلف
B005 | عبودية محضة على القد والحذو
B006 | الأزلم الجذع للدهر الباقي
B007 | الزلم واحد الوبار
B008 | ملء الحوض
B009 | تقليل العطاء
B010 | قطع الرأس أو الأنف
B011 | الذهاب السريع والارتحال
B012 | انتصاب الشيء وارتفاع النهار

### ف س ق — 54 uses; here: 5:3:30 فِسْقٌ
B001 | الخروج عن الطاعة
B002 | خروج الرطبة من قشرها
B003 | الفأرة الفويسقة

### ي و م — 405 uses; here: 5:3:31 ٱلْيَوْمَ; 5:3:40 ٱلْيَوْمَ; 5:5:1 ٱلْيَوْمَ
B001 | وقت النهار المحدود
B002 | مدة من الزمان
B003 | كائنة اليوم وشدته
B004 | أيام النعم والوقائع الإلهية
B005 | يوم مضاف إلى إذ

### ي ء س — 13 uses; here: 5:3:32 يَئِسَ
B001 | انقطاع الرجاء
B002 | اليأس بمعنى العلم

### ك ف ر — 525 uses; here: 5:3:34 كَفَرُوا۟; 5:5:34 يَكْفُرْ; 5:10:2 كَفَرُوا۟
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

### د ي ن — 101 uses; here: 5:3:36 دِينِكُمْ; 5:3:43 دِينَكُمْ; 5:3:50 دِينًۭا
B001 | الطاعة والانقياد
B002 | الحساب والجزاء
B003 | الدين المالي
B004 | الإذلال والملك
B005 | العادة والشأن
B006 | مدينة الطاعة
B007 | التصديق والتفويض

### خ ش ي — 48 uses; here: 5:3:38 تَخْشَوْهُمْ; 5:3:39 وَٱخْشَوْنِ
B001 | الخوف والخشية مع الهيبة
B002 | العلم على سبيل المجاز
B003 | الكراهة في إسناد الخشية
B004 | الحشف واليبس

### ك م ل — 5 uses; here: 5:3:41 أَكْمَلْتُ
B001 | تمام الشيء وكماله

### ت م م — 22 uses; here: 5:3:44 وَأَتْمَمْتُ; 5:6:57 وَلِيُتِمَّ
B001 | بلوغ الشيء تمامه
B002 | التميمة المعلقة
B003 | الشيء الصلب الشديد
B004 | بلوغ الأجل والمقدار
B005 | ترديد التاء في الكلام
B006 | تتميم الأيسار
B007 | قطعة تتم النسج
B008 | البلوغ إلى الكسر والهلاك
B009 | النسبة إلى تميم

### س ل م — 140 uses; here: 5:3:49 ٱلْإِسْلَٰمَ
B001 | السلامة والبراءة من الآفات
B002 | السلام اسما وتحية ودارا
B003 | الانقياد والاستسلام لله أو للأمر
B004 | الصلح والمسالمة ضد الحرب
B005 | السلم في البيع والسلف
B006 | السلم مرقاة وسببا
B007 | السلام حجارة صلبة
B008 | السلم شجر وقرظ للدباغة
B009 | السليم الملدوغ تفاؤلا أو استسلاما
B010 | السلامى عظام ومفاصل
B011 | السلم دلو بعروة واحدة
B012 | تسليم الشيء وتخليته
B013 | أخذه سلما أي أسره

### ض ر ر — 74 uses; here: 5:3:52 ٱضْطُرَّ
B001 | الضُّرّ والنقص خلاف النفع
B002 | المضارّة والضِّرار
B003 | الضرورة والاضطرار
B004 | الضَّرّة والمزاحمة الزوجية
B005 | الدنوّ المزاحم وضفة الوادي
B006 | الضَّرّة كلحمة مجتمعة أو مال مجموع
B007 | الضَّرير قوّة وصبر
B008 | النفي بمعنى عدم الزيادة

### خ م ص — 2 uses; here: 5:3:54 مَخْمَصَةٍ
B001 | ضمور البطن ودقته
B002 | خلاء البطن من الطعام
B003 | أخمص القدم الداخل
B004 | الخميصة الكساء الأسود المعلّم
B005 | خمص البطن عن المال عفة
B006 | خمصة الأرض اللينة
B007 | التخامص تجاف عن الشيء
B008 | تخامص ظلمة الليل
B009 | انخماص ورم الجرح

### ج ن ف — 2 uses; here: 5:3:56 مُتَجَانِفٍۢ
B001 | الميل عن الاستقامة في الحكم والقصد والأمر
B002 | ميل الخلقة واعوجاج الجسد
B003 | جنفاء أو جنفى اسم موضع
B004 | جنافي يميل في مشيه اختيالا
B005 | اللجاج في جناف قبيح أي مجانبة الأهل

### غ ف ر — 234 uses; here: 5:3:60 غَفُورٌۭ; 5:9:8 مَّغْفِرَةٌۭ
B001 | ستر يصون الشيء ويغطيه
B002 | ستر الذنب وصون صاحبه من أثره
B003 | زئبر أو شعر يغطي السطح
B004 | نكس المرض أو الجرح
B005 | ولد الأروية وأمه
B006 | منزل قمري من ثلاثة أنجم
B007 | مغافير الشجر الحلوة
B008 | جماء الغفير: الجماعة كلها

### ر ح م — 339 uses; here: 5:3:61 رَّحِيمٌۭ
B001 | الرَّحْمَة والرقة
B002 | الرَّحِم والقرابة
B003 | رَحِم الأنثى
B004 | وجع الرَّحِم بعد الولادة

### س ء ل — 129 uses; here: 5:4:1 يَسْـَٔلُونَكَ
B001 | السؤال والطلب
B002 | السُّؤل المطلوب
B003 | قضاء المسألة
B004 | السؤال المتبادل

### ق و ل — 1722 uses; here: 5:4:5 قُلْ; 5:7:10 قُلْتُمْ
B001 | إخراج القول بالنطق
B002 | اللسان آلة القول
B003 | كثرة القول في صاحبه
B004 | القيل صاحب القول النافذ
B005 | قول ما لم يكن أو نسبته
B006 | اجترار القول إلى النفس
B007 | القول الفاشي بين الناس
B008 | عود القال لضرب القلة
B009 | المقاولة في الأمر
B010 | اقتالة الحكم على غيره
B011 | قول يجري مجرى الظن
B012 | قول في النفس لم يظهر
B013 | القول اعتقاد ومذهب
B014 | قول الشيء دلالته
B015 | العناية الصادقة بالشيء
B016 | قول الشيء حده
B017 | القول إلهام يلقي معنى

### ط ي ب — 50 uses; here: 5:4:8 ٱلطَّيِّبَٰتُ; 5:5:4 ٱلطَّيِّبَٰتُ; 5:6:42 طَيِّبًۭا
B001 | الطَّيِّب خلاف الخبيث
B002 | سبي طيبة لا غدر فيه
B003 | الاستطابة تطهير من الخبث
B004 | الأطيبان الأكل والنكاح
B005 | طيبة اسم المدينة
B006 | النفس تطيب بالشيء
B007 | الطيب ما يتطيب به
B008 | المطايبة مزاح
B009 | طوبى مستطاب الجنة

### ع ل م — 854 uses; here: 5:4:10 عَلَّمْتُم; 5:4:14 تُعَلِّمُونَهُنَّ; 5:4:16 عَلَّمَكُمُ; 5:7:17 عَلِيمٌۢ
B001 | انكشاف الشيء للعارف
B002 | أثر يميز الشيء ويهدي إليه
B003 | الخلق عالم يدل على صانعه
B004 | شق ظاهر في الشفة العليا
B005 | ماء كثير مجتمع في عيلم
B006 | طائر جارح يسمى العلام
B007 | ذكر الضباع يسمى العيلام

### ج ر ح — 4 uses; here: 5:4:12 ٱلْجَوَارِحِ
B001 | شق الجلد وإحداث الجرح
B002 | اكتساب العمل واجتراحه
B003 | الجوارح الصائدة
B004 | القدح في الشاهد واللسان
B005 | الاستجراح عيب وفساد
B006 | جارحة المال والنتاج

### ك ل ب — 6 uses; here: 5:4:13 مُكَلِّبِينَ
B001 | الكلب الحيوان النباح
B002 | تكلِيب الكلاب للصيد
B003 | داء الكَلَب وشبه الجنون
B004 | الحرص والتكالب والشر
B005 | كلبة الزمان والبرد واليبس
B006 | سير الخرز بين الأديم
B007 | الكلاب والكلوب الماسك
B008 | أسماء منقولة من الكلب

### م س ك — 27 uses; here: 5:4:20 أَمْسَكْنَ
B001 | إمساك الشيء وحبسه
B002 | إمساك المال بخلا
B003 | مسكة تبقي الرمق
B004 | موضع يمسك الماء أو يثبت
B005 | جلد يمسك ما فيه
B006 | مسكة في المعصم
B007 | المسك الطيب
B008 | إمساك النار في التراب
B009 | ماسكة رحم
B010 | الماسكة على الولد
B011 | إمساك قوائم الفرس
B012 | حسكة مسكة
B013 | المسكان للعربان

### ذ ك ر — 292 uses; here: 5:4:22 وَٱذْكُرُوا۟; 5:7:1 وَٱذْكُرُوا۟; 5:11:4 ٱذْكُرُوا۟
B001 | الذكر خلاف الأنثى
B002 | صلابة الذكر وحدته وشدته
B003 | استحضار الشيء بعد النسيان أو مع الحفظ
B004 | جريان الذكر على اللسان
B005 | ذكر الله عبادة وثناء ودعاء
B006 | الذكر كتاب منزل أو كتاب دين
B007 | ذكر المرء شرف وصيت
B008 | ذكر الحق صك ووثيقة حق
B009 | الذكرى والتذكرة ما يذكّر

### س م و — 381 uses; here: 5:4:23 ٱسْمَ
B001 | العلو والارتفاع
B002 | الشخص المرتفع الظاهر
B003 | تطاول الفحل على الشول
B004 | السماء وما علا فأظل
B005 | الاسم تنويه ودلالة
B006 | الخروج للصيد
B007 | المساماة والمباراة
B008 | الصيت الحسن المنتشر

### و س م ~alt (documented alternative analysis) — 2 uses; here: 5:4:23 ٱسْمَ
B001 | أثر وسم ظاهر يجعل الشيء معروفا
B002 | سمة يرى بها الناظر دلالة الحال
B003 | مطر أول يسم الأرض بالنبات
B004 | موسم معلم يجتمع إليه الناس
B005 | حسن عليه أثر الجمال
B006 | وسمة يخضب بورقها

### س ر ع — 23 uses; here: 5:4:30 سَرِيعُ
B001 | خلاف البطء
B002 | الأوائل المتقدمون
B003 | ما أسرع ذلك
B004 | القضيب الرطب الناعم
B005 | ديدان الأساريع
B006 | طرائق الأساريع
B007 | شكر العنب
B008 | أوتار السرعان
B009 | رابية الرمل
B010 | عصبة الظبي
B011 | كنية النار

### ح س ب — 109 uses; here: 5:4:31 ٱلْحِسَابِ
B001 | العد والحساب
B002 | الحسبان والظن
B003 | الكفاية والإغناء
B004 | الحسب والمآثر
B005 | الاحتساب عند الله
B006 | الحسبة والنظر في الأمر
B007 | المرامي والحسبان النازل
B008 | المحسبة والوسادة
B009 | لون الأحسب والأحسبية
B010 | التحسب والاستخبار

### ط ع م — 48 uses; here: 5:5:5 وَطَعَامُ; 5:5:11 وَطَعَامُكُمْ
B001 | ذوق الشيء وتناوله
B002 | إطعام الغير وطلب الطعام
B003 | استطعام الكلام وفتح القراءة
B004 | رزق ومعاش وحسن حال
B005 | إدراك الثمر وأخذ الطعم
B006 | آلة الصيد التي تطعم صاحبها
B007 | سمن الحيوان وطعم الشحم
B008 | طعم العقل والقيمة
B009 | مستطعم الفرس وطلب جريه
B010 | إطعام الغصن وقبول الوصل
B011 | القدرة على الشيء
B012 | الأخذ بالمطعمة عند الخنق
B013 | التطاعم بالفم
B014 | تتابع الخلق

### ء ت ي — 549 uses; here: 5:5:7 أُوتُوا۟; 5:5:20 أُوتُوا۟; 5:5:25 ءَاتَيْتُمُوهُنَّ
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

### ك ت ب — 319 uses; here: 5:5:8 ٱلْكِتَٰبَ; 5:5:21 ٱلْكِتَٰبَ
B001 | ضم شيء إلى شيء
B002 | نظم الحروف واسم المكتوب
B003 | إثبات يوجب حكما أو قدرا
B004 | إدخال الاسم في سجل أو زمرة
B005 | مكاتبة العبد على عتقه

### ح ص ن — 18 uses; here: 5:5:14 وَٱلْمُحْصَنَٰتُ; 5:5:17 وَٱلْمُحْصَنَٰتُ; 5:5:27 مُحْصِنِينَ
B001 | حفظ داخل حصن محيط
B002 | عفة الفرج المحفوظة
B003 | إحصان بعقد أو حرمة
B004 | حصان الخيل الحامي أو الممسك

### ق ب ل — 294 uses; here: 5:5:23 قَبْلِكُمْ
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

### ء ج ر — 108 uses; here: 5:5:26 أُجُورَهُنَّ; 5:9:9 وَأَجْرٌ
B001 | جزاء العمل والكراء
B002 | جبر الكسر على عوج
B003 | سطح بلا سترة

### س ف ح — 4 uses; here: 5:5:29 مُسَٰفِحِينَ
B001 | صب السائل وإراقته
B002 | سفاح بلا عقد
B003 | سفح الجبل
B004 | السفيح القدح الذي لا نصيب له
B005 | السفيحان كالجوالقين
B006 | السفيح الكساء الغليظ
B007 | سعة في الإبط والضلوع
B008 | رجل سفاح للكلام

### ء خ ذ — 273 uses; here: 5:5:31 مُتَّخِذِىٓ
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

### خ د ن — 2 uses; here: 5:5:32 أَخْدَانٍۢ
B001 | المصاحبة والمخاللة
B002 | مصاحبة الشهوة

### ح ب ط — 16 uses; here: 5:5:37 حَبِطَ
B001 | انتفاخ البطن من أكل مستوبل
B002 | بطلان العمل وفساده
B003 | انتفاخ الهيئة والبطانة
B004 | نكس الجرح وبقاء أثره
B005 | ذهاب ماء البئر
B006 | هدر دم القتيل
B007 | الانحطاط والسقوط

### ع م ل — 360 uses; here: 5:5:38 عَمَلُهُۥ; 5:8:26 تَعْمَلُونَ; 5:9:5 وَعَمِلُوا۟
B001 | الفعل المقصود والعمل
B002 | إعمال الشيء واستعماله
B003 | ولاية العمل والقيام عليه
B004 | أجر العمل ورزق العامل
B005 | المعاملة بين الناس
B006 | العملة العاملون بالأيدي
B007 | التعمل بمعنى التعني
B008 | المطبوع على العمل
B009 | عامل الرمح
B010 | الجارحة العاملة
B011 | الطريق المعمل
B012 | بنو العمل من المشاة

### ء خ ر — 250 uses; here: 5:5:41 ٱلْءَاخِرَةِ
B001 | الآخرية بعد الأول أو غيره
B002 | التأخير إلى وقت لاحق
B003 | المؤخر والخلف
B004 | الدار الآخرة

### خ س ر — 65 uses; here: 5:5:43 ٱلْخَٰسِرِينَ
B001 | النقص العام
B002 | خسارة التجارة
B003 | إخسار الكيل والميزان
B004 | الضلال والهلاك
B005 | الخنسرى والخيسرى والخناسر

### ص ل و — 99 uses; here: 5:6:7 ٱلصَّلَوٰةِ
B001 | ملاقاة النار وحرها
B002 | الدعاء والثناء والرحمة
B003 | العبادة المخصوصة
B004 | الشرك المنصوبة
B005 | الصَّلا من الظهر والجنب
B006 | تلو السابق في السباق
B007 | مواضع الصلاة ودور العبادة
B008 | الصَّلاية حجر الدق
B009 | الصِّليان نبت ترعاه الإبل

### غ س ل — 4 uses; here: 5:6:8 فَٱغْسِلُوا۟
B001 | تطهير الشيء بإسالة الماء وإزالة الدرن
B002 | ماء الغسل وما يغسل به أو فيه
B003 | فحل يكثر الضراب ولا يلقح
B004 | غسلين منغسل من أبدان أهل النار
B005 | حرارة وشدة منسوبة إلى عسلين أو غسلين

### و ج ه — 78 uses; here: 5:6:9 وُجُوهَكُمْ; 5:6:44 بِوُجُوهِكُمْ
B001 | الوجه والمستقبل
B002 | الجهة والوجهة
B003 | المواجهة والتقابل
B004 | الوجه عن الذات
B005 | القصد والتوجه
B006 | الوجاهة والجاه
B007 | وجه النهار وصدره
B008 | وجه الأمر وصوابه
B009 | توجه الشيخ
B010 | الولادة باليدين أولا
B011 | توجيه القافية
B012 | توجيه النبات
B013 | ضرب الوجه
B014 | الرد عن الوجه
B015 | ذو وجهين

### ي د ي — 120 uses; here: 5:6:10 وَأَيْدِيَكُمْ; 5:6:45 وَأَيْدِيكُم; 5:11:14 أَيْدِيَهُمْ; 5:11:16 أَيْدِيَهُمْ
B001 | اليَد الجارحة
B002 | اليَد القوّة
B003 | اليَد النعمة
B004 | اليَد المالكة
B005 | اليَد السلطان
B006 | اليَد المستسلمة
B007 | اليَد المناولة
B008 | بين اليَدين
B009 | ما كسبت اليَدان
B010 | سقوط اليَد في الندم
B011 | أيادي سبأ
B012 | يَد الدهر
B013 | يَد الشيء
B014 | اليَدِي الواسع
B015 | اليَدِي الصنّاع
B016 | اليَد الناصرة
B017 | اليَد للأكل

### ر ف ق — 5 uses; here: 5:6:12 ٱلْمَرَافِقِ
B001 | اللين ولطافة الفعل
B002 | الصحبة والمرافقة
B003 | المرفق والمنفعة
B004 | المرفق والاتكاء
B005 | الرفاق وشد البعير
B006 | انفتال المرفق عن الجنب
B007 | انسداد أحاليل الناقة
B008 | التمهل والانتظار
B009 | الامتلاء والثبات
B010 | اسم بلد

### م س ح — 4 uses; here: 5:6:13 وَٱمْسَحُوا۟; 5:6:43 فَٱمْسَحُوا۟
B001 | إمرار اليد على الشيء وإزالة أثره
B002 | المسح كناية عن الجماع
B003 | القطع والضرب بالسيف
B004 | محو الخلقة في العين والوجه
B005 | اسم المسيح لعيسى بين التعريب والمسح
B006 | مسحة الحسن والملك والكرم
B007 | المسيح عرق ظاهر
B008 | فضة ملساء ونقش ممحو
B009 | الأرض المستوية الملساء
B010 | مساحة الأرض وذرعها
B011 | قطع الأرض سيرا
B012 | ذوائب الشعر والماشطة
B013 | القوس الممسوحة عند التليين
B014 | البلاس والمسح الخشن
B015 | تسوية الجسد أو نقص لحمه
B016 | الملاينة المخادعة في القول والمعاشرة
B017 | المصافحة في البيع
B018 | التمساح دابة الماء والمارد
B019 | المس الخفيف بلا إدماء أو عرك
B020 | استلال السيف من غمده

### ر ء س — 18 uses; here: 5:6:14 بِرُءُوسِكُمْ
B001 | الرأس والأعلى
B002 | الرئاسة والصدارة
B003 | جمع السيل وحمله
B004 | رِئاس الأمر ومن رأسه
B005 | رِئاس السيف
B006 | الرمي في الرأس

### ر ج ل — 73 uses; here: 5:6:15 وَأَرْجُلَكُمْ
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

### ك ع ب — 4 uses; here: 5:6:17 ٱلْكَعْبَيْنِ
B001 | نتو العظم وارتفاعه
B002 | البيت المربع المرتفع
B003 | نتوء الثدي وبلوغه
B004 | التربيع والطي الشديد
B005 | العقدة بين أنبوبي القصب والرمح
B006 | قطعة السمن الجامدة
B007 | ملء الشيء حتى يتمتلئ
B008 | عذرة الجارية المختومة
B009 | ارتفاع الجد والشرف
B010 | انطلاق المضار غير المبالِي

### ك و ن — 1390 uses; here: 5:6:19 كُنتُمْ; 5:6:23 كُنتُم; 5:8:4 كُونُوا۟
B001 | وقوع الشيء وحضوره في زمان
B002 | المكان والمكانة من الكون
B003 | الكفالة والقيام على فلان
B004 | الخضوع بالاستكانة
B005 | الشيخ المنسوب إلى كُنْتُ
B006 | حالة السوء بكينة

### ج ن ب — 33 uses; here: 5:6:20 جُنُبًۭا
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

### ط ه ر — 31 uses; here: 5:6:21 فَٱطَّهَّرُوا۟; 5:6:56 لِيُطَهِّرَكُمْ
B001 | النقاء وزوال الدنس
B002 | طهر النساء من الحيض
B003 | التطهر بالماء والغسل
B004 | الطهور الذي يطهر غيره
B005 | تنزيه النفس والعمل عن القبيح
B006 | تطهير المكان المقدس من الرجس
B007 | الأطهر بمعنى الأحل والأنزه

### م ر ض — 24 uses; here: 5:6:24 مَّرْضَىٰٓ
B001 | الخروج عن الصحة والاعتدال
B002 | مرض القلب والدين
B003 | القيام على المريض
B004 | إضعاف الأمر وقصور الحركة
B005 | إظلام الشيء ونقص صفائه
B006 | مقاربة الإصابة دون بلوغها
B007 | التعريض في القول

### س ف ر — 12 uses; here: 5:6:27 سَفَرٍ
B001 | كشف الغطاء وإزالة الساتر
B002 | إسفار الضوء والوجه
B003 | الخروج في السفر والمسافرون
B004 | الكتاب يكشف المكتوب
B005 | السفير يزيل الوحشة
B006 | السِّفار في أنف البعير
B007 | انحسار يظهر أثرا أو قلة
B008 | أسماء الحيوان المنكشف في الأرض

### ج ي ء — 278 uses; here: 5:6:29 جَآءَ
B001 | المجيء والحصول
B001 | المجيء والغلبة بالمجيء
B002 | المغالبة بكثرة المجيء
B002 | الجِيأة مجتمع الماء
B003 | مجتمع الماء في هبطة أو حول حصن
B003 | جائية الجراح
B004 | الإتيان بالشيء واستحضاره
B005 | الإلجاء والاضطرار
B006 | الجائية من الجراح

### ء ح د — 85 uses; here: 5:6:30 أَحَدٌۭ
B001 | الأَحَدِيَّة والوَحْدَة
B002 | استغراق النفي
B003 | الواحد في العد والتركيب
B004 | الأول والإضافة
B005 | الانفراد والتفرق آحادا
B006 | جبل أُحُد

### غ و ط — 2 uses; here: 5:6:33 ٱلْغَآئِطِ
B001 | اطمئنان وغور في الأرض
B002 | دخول وغيبوبة في الشيء
B003 | كناية الحدث والتبرز
B004 | انخفاض بانثناء

### ل م س — 5 uses; here: 5:6:35 لَٰمَسْتُمُ
B001 | المس باليد والبشرة
B002 | طلب الشيء والتماسه
B003 | كناية الجماع
B004 | بيع الملامسة
B005 | اللُّماسة حاجة قريبة

### ن س و — 59 uses; here: 5:6:36 ٱلنِّسَآءَ
B001 | جماعة النساء

### و ج د — 107 uses; here: 5:6:38 تَجِدُوا۟
B001 | إلفاء الشيء وإصابته
B002 | ثبوت الشيء في الوجود
B003 | السعة والجدة والغنى
B004 | وجدان الحزن والمحبة
B005 | الموجدة والغضب

### م و ه — 63 uses; here: 5:6:39 مَآءًۭ
B001 | الماء المعروف وأصل اسمه
B002 | ظهور الماء ودخوله وكثرته
B003 | إيصال الماء بالسقي والصب
B004 | ماء الفحل في الرحم
B005 | كسوة المعدن بماء الذهب أو الفضة
B006 | رونق كالماء في الوجه والكلام والثمر
B007 | صفاء الماوية كالبلور والمرآة
B008 | كثرة ماء القلب على جهة البلادة

### ي م م — 11 uses; here: 5:6:40 فَتَيَمَّمُوا۟
B001 | قصد الشيء وتعمده
B002 | التيمم للصلاة بمسح الوجه واليدين بالتراب
B003 | اليم ماء عظيم
B004 | اليمام طير
B005 | اليمامة واليمة أسماء مواضع وأعلام

### ص ع د — 9 uses; here: 5:6:41 صَعِيدًۭا
B001 | ارتفاع وصعود إلى فوق
B002 | إصعاد في البلاد والوجوه
B003 | عقبة كؤود ومشقة
B004 | صعيد وجه الأرض
B005 | ناقة صعود تعطف على ولد
B006 | صعدة قناة مستقيمة
B007 | صعداء نفس يرتفع
B008 | زيادة وعلو إلى فوق
B009 | تصعيد بالنار وتغيير

### ج ع ل — 346 uses; here: 5:6:50 لِيَجْعَلَ
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

### ح ر ج — 15 uses; here: 5:6:53 حَرَجٍۢ
B001 | التجمع والالتفاف
B002 | الضيق والحرج
B003 | الإثم والتحرج
B004 | التحريم والحظر
B005 | حيرة العين وثباتها
B006 | السرير والمحفة
B007 | الناقة الضامرة والطويلة
B008 | الودعة والقلادة
B009 | نصيب الكلب من الصيد
B010 | الحبال المنصوبة
B011 | الثياب المبسوطة على حبل
B012 | لزوم القتال

### ش ك ر — 75 uses; here: 5:6:61 تَشْكُرُونَ
B001 | عرفان النعمة وحمد المنعم
B002 | الكفاية باليسير وظهور أثره
B003 | الامتلاء والغزر وكثرة اللبن
B004 | خروج الشكير والنبات الغض
B005 | اشتداد الوقوع والهيجان
B006 | كناية الفرج والنكاح
B007 | أسماء قبائل

### و ث ق — 34 uses; here: 5:7:5 وَمِيثَٰقَهُ; 5:7:7 وَاثَقَكُم
B001 | الثقة والسكون إلى المعتمد
B002 | الإحكام والوثاقة
B003 | الإيثاق والوثاق الذي يشد به
B004 | الميثاق والعهد المؤكد

### س م ع — 185 uses; here: 5:7:11 سَمِعْنَا
B001 | إدراك الأصوات بالأذن
B002 | الأذن وموضع السمع
B003 | الفهم والامتثال
B004 | إسماع الغير
B005 | الصيت والشيوع بين الناس
B006 | إسماع القبيح والشتم
B007 | السماع المستلذ والغناء
B008 | مِسمع الدلو والغرب
B009 | المِسمع قيد والقيد مسمعان
B010 | السَّمْع ولد الذئب والضبع
B011 | سَمْع لا بَلَغ
B012 | سَمْعَمَع في الهيئة والخبث
B013 | سَمْعَنَة نَظَرْنَة في التظنّي
B014 | بين سمع الأرض وبصرها
B015 | السميعان من أدوات الحراثين
B016 | أم السمع الدماغ

### ط و ع — 129 uses; here: 5:7:12 وَأَطَعْنَا
B001 | الانقياد والطاعة
B002 | الموافقة والمطاوعة
B003 | الاستطاعة والإطاقة
B004 | تكلف الاستطاعة
B005 | التطوع والتبرع
B006 | تسهيل النفس للأمر
B007 | تهيؤ المرعى والثمر

### ص د ر — 46 uses; here: 5:7:19 ٱلصُّدُورِ
B001 | الصدر الجارحة وما يتصل بها
B002 | المقدّم والأعلى والأول
B003 | الصُّدور عن المورد
B004 | الأصل الذي تصدر عنه الأفعال
B005 | المصادرة على مال
B006 | الطائفة من الشيء

### ش ه د — 160 uses; here: 5:8:7 شُهَدَآءَ
B001 | الحضور مع المشاهدة
B002 | البيان بعلم
B003 | صيغة الإشهاد والذكر
B004 | الشهادة بالموت والحضور
B005 | اللسان الشاهد
B006 | الخارج عند الولادة والإدراك
B007 | الشَّهْد في الشمع
B008 | العلامة الشاهدة

### ق س ط — 25 uses; here: 5:8:8 بِٱلْقِسْطِ
B001 | العدل والإنصاف
B002 | الجور والميل عن الحق
B003 | النصيب والقسمة
B004 | الميزان المستقيم
B005 | اعوجاج الرجلين ويبسهما
B006 | عود البخور والدواء
B007 | المكيال والمقدار
B008 | قوس القزح
B009 | جماعات متفرقة
B010 | تقتير النفقة
B011 | الغبار

### ع د ل — 28 uses; here: 5:8:15 تَعْدِلُوا۟; 5:8:16 ٱعْدِلُوا۟
B001 | العدل في الحكم والسيرة
B002 | المعادلة والمثل
B003 | العِدل فدية وقيمة
B004 | العِدل حمل يوازن حملا
B005 | إقامة الشيء واعتداله
B006 | العدول والميل عن الوجه
B007 | جعل العَديل لله
B008 | المعادلة بين أمرين

### ق ر ب — 96 uses; here: 5:8:18 أَقْرَبُ
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

### خ ب ر — 52 uses; here: 5:8:24 خَبِيرٌۢ
B001 | العلم بالخبر وباطن الأمر
B002 | لين الأرض ومائها
B003 | إصلاح الأرض بالمخابرة
B004 | الغزر في المزادة والناقة
B005 | اللِّين في النبات والوبر والزبد
B006 | القسمة في الشاة واللحم

### و ع د — 151 uses; here: 5:9:1 وَعَدَ
B001 | وعد يفتح رجاء الموعود بقول
B002 | وعيد يخص الشر والتهدد
B003 | موعد يحد الوعد بزمان أو مكان
B004 | مواعدة يتبادل فيها الطرفان الوعد
B005 | وعيد الفحل هدير قبل الصيال
B006 | أمارة واعدة يرجى منها حال آت

### ص ل ح — 180 uses; here: 5:9:6 ٱلصَّٰلِحَٰتِ
B001 | الصلاح ضد الفساد والطلاح
B002 | الصلح إزالة النفار بين الناس
B003 | الصلاح للشيء ملاءمته
B004 | صالح وما قاربه علما لشخص
B005 | صلاح والصلح علمان لمواضع

### ع ظ م — 128 uses; here: 5:9:10 عَظِيمٌۭ
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

### ك ذ ب — 282 uses; here: 5:10:3 وَكَذَّبُوا۟
B001 | خلاف الصدق
B002 | نسبة الشيء أو صاحبه إلى الكذب
B003 | كذب عليك بمعنى الزم وعليك به
B004 | صدق الحملة أو كذبها
B005 | ما كذب أن فعل أي ما لبث
B006 | كذب لبن الناقة إذا ذهب ولم يدم
B007 | كذب الوحشي إذا جرى ثم وقف
B008 | النفس الكذوب
B009 | الكذابة ثوب يكذب بحاله

### ء ي ي — 382 uses; here: 5:10:4 بِـَٔايَٰتِنَآ
B001 | تمهل وانتظار
B002 | تعمد آية الشخص
B003 | علامة ظاهرة
B004 | أي للسؤال والتعيين
B005 | إيا عماد للضمير
B006 | أيان للزمان
B007 | كأين لعدد كثير
B008 | أي وأيا للنداء
B009 | أي مفسرة
B010 | إي افتتاح للقسم

### ص ح ب — 97 uses; here: 5:10:6 أَصْحَٰبُ
B001 | الصُّحبة والملازمة
B002 | الحفظ بالمصاحبة
B003 | الإصحاب والانقياد
B004 | جعل الشيء مصاحبا واستصحابه
B005 | بلوغ الابن صاحبا
B006 | أديم مُصحَب عليه الشعر
B007 | طُحلب يعلو الماء
B008 | لون أَصحَب إلى الحمرة

### ج ح م — 26 uses; here: 5:10:7 ٱلْجَحِيمِ
B001 | تأجج النار وشدة حرها
B002 | احتدام الحرب والموت
B003 | العين المتوقدة أو الجاحظة
B004 | تلهب الوجه بالغضب
B005 | قلة الحياء

### ه م م — 9 uses; here: 5:11:9 هَمَّ
B001 | انعقاد الهم في النفس
B002 | هم يذيب ويقلق
B003 | ذوب وجريان بعد جمود
B004 | كثرة ماء وصوب
B005 | دبيب الهوام
B006 | ذوب الكبر
B007 | مطر خفيف وهبوب لين
B008 | تردد صوت في الصدر
B009 | تنويم بصوت رقيق
B010 | تخلل الشعر بالأصابع
B011 | طلب وتتبع
B012 | نفاد لا يبقى معه شيء
B013 | كفاية في المدح
B014 | حسن مشية الناقة

### ب س ط — 25 uses; here: 5:11:12 يَبْسُطُوٓا۟
B001 | النشر والامتداد ضد القبض
B002 | الأرض والبساط المبسوط
B003 | السعة والزيادة والفضل
B004 | مد اليد وإطلاقها
B005 | انبساط اللسان والوجه والمعاشرة
B006 | السرور والإراحة النفسية
B007 | السير في البلاد والتنزه
B008 | الناقة المخلاة مع ولدها
B009 | بحر البسيط في العروض
B010 | قبول العذر
B011 | الطول والبعد ومدى اليد
B012 | البساطة وعدم التركيب
B013 | القتب المبسوط غير المفروق

### ك ف ف — 15 uses; here: 5:11:15 فَكَفَّ
B001 | كف اليد
B002 | الكف والمنع
B003 | الضم والإغلاق
B004 | الحاشية والطرف
B005 | الكفّة الحاوية
B006 | الإحاطة بالجميع
B007 | الكفاف بلا فضل
B008 | كف البصر
B009 | مد الكف للسؤال
B010 | استكفاف النظر
B011 | كفّة لكفّة
B012 | الاستكفاف حول الشيء
B013 | قصر أسنان البعير
B014 | دارات الوشم
B015 | الكف في العروض
B016 | المماثلة والاكتفاء

### و ك ل — 70 uses; here: 5:11:22 فَلْيَتَوَكَّلِ
B001 | تسليم الأمر إلى غيره
B002 | الاعتماد والتوكل
B003 | العاجز الذي يكل أمره
B004 | تبادل الاتكال والتضييع
B005 | تأخر الدابة واتكالها في السير
B006 | القائم بالأمر كفاية وحفظا

## Scene map in this window (mechanical, generous; for what the chain map missed)

- body.limbs [90 words, 32 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B010 neck, ع ق د B011 back, ع ق د B012 forelock, ع ق د B014 hand, ع ق د B017 neck · أُحِلَّتْ 5:1:6: ح ل ل B014 joint · بَهِيمَةُ 5:1:8: ب ه م B006 thumb · ٱلْأَنْعَٰمِ 5:1:9: ن ع م B007 foot, ن ع م B012 foot · شَعَٰٓئِرَ 5:2:6: ش ع ر B001 hair · ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B003 shoulder, ق ل د B010 neck · +84 more (all: data/scenes/s005/body.limbs.md)
- war.battle [80 words, 22 roles] بَهِيمَةُ 5:1:8: ب ه م B005 army · ٱلْأَنْعَٰمِ 5:1:9: ن ع م B008 rout · حُرُمٌ 5:1:18: ح ر م B005 retreat · ٱللَّهَ 5:1:20: و ل ه~alt B002 captive · ٱلشَّهْرَ 5:2:9: ش ه ر B003 charge · ٱلْبَيْتَ 5:2:17: ب ي ت B004 raid · +74 more (all: data/scenes/s005/war.battle.md)
- speech.calling [85 words, 21 roles] ءَامَنُوٓا۟ 5:1:3: ء م ن B003 answer · ٱلْأَنْعَٰمِ 5:1:9: ن ع م B004 answer, ن ع م B013 call · ٱلصَّيْدِ 5:1:16: ص ي د B003 chatter · يُرِيدُ 5:1:23: ر و د B002 summons · شَعَٰٓئِرَ 5:2:6: ش ع ر B006 call, ش ع ر B008 naming · يَجْرِمَنَّكُمْ 5:2:28: ج ر م B008 cry · +79 more (all: data/scenes/s005/speech.calling.md)
- know.perceiving [43 words, 20 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B006 knowing · بَهِيمَةُ 5:1:8: ب ه م B001 ignorance · ٱلْعِقَابِ 5:2:52: ع ق ب B008 perceiving · ٱضْطُرَّ 5:3:52: ض ر ر B007 judgment · قُلْ 5:4:5: ق و ل B011 conjecture, ق و ل B012 thought, ق و ل B013 belief, ق و ل B017 inspiration · أَمْسَكْنَ 5:4:20: م س ك B003 intellect · +37 more (all: data/scenes/s005/know.perceiving.md)
- war.arms [43 words, 18 roles] ٱلشَّهْرَ 5:2:9: ش ه ر B003 sword · ٱلْهَدْىَ 5:2:12: ه د ي B003 arrow · ٱلْعِقَابِ 5:2:52: ع ق ب B001 bowstring · أُهِلَّ 5:3:8: ه ل ل B001 spearhead · وَٱلْمُتَرَدِّيَةُ 5:3:14: ر د ي B001 stone missile, ر د ي B004 sword · أَكَلَ 5:3:17: ء ك ل B014 knife · +37 more (all: data/scenes/s005/war.arms.md)
- motion.passage [59 words, 17 roles] أَوْفُوا۟ 5:1:4: و ف ي B002 vanishing · أُحِلَّتْ 5:1:6: ح ل ل B008 channel, ح ل ل B011 dislodging · ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B009 being swallowed · شَنَـَٔانُ 5:2:29: ش ن ء B003 emerging · تَعْتَدُوا۟ 5:2:37: ع د و B004 passing through, ع د و B006 transmission, ع د و B007 obstruction, ع د و B008 succession · وَٱلْمُنْخَنِقَةُ 5:3:12: خ ن ق B003 passage · +53 more (all: data/scenes/s005/motion.passage.md)
- body.strength [68 words, 16 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B011 firmness · ٱلْهَدْىَ 5:2:12: ه د ي B008 frailty, ه د ي B009 frailty · ءَآمِّينَ 5:2:16: ء م م B006 fatness · يَجْرِمَنَّكُمْ 5:2:28: ج ر م B007 frame · قَوْمٍ 5:2:30: ق و م B011 build, ق و م B014 strength · ٱلْمَيْتَةُ 5:3:3: م و ت B001 loss of strength · +62 more (all: data/scenes/s005/body.strength.md)
- body.illness [56 words, 15 roles] ٱلصَّيْدِ 5:1:16: ص ي د B002 disease · ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B007 fever · قَوْمٍ 5:2:30: ق و م B019 pain, ق و م B020 disease · تَعْتَدُوا۟ 5:2:37: ع د و B006 contagion · وَٱلتَّقْوَىٰ 5:2:41: و ق ي B003 hoof pain · ٱلْمَيْتَةُ 5:3:3: م و ت B009 seizure · +50 more (all: data/scenes/s005/body.illness.md)
- trade.sale [72 words, 13 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B002 contract · غَيْرَ 5:1:14: غ ي ر B003 exchange · حُرُمٌ 5:1:18: ح ر م B007 loss · ٱللَّهَ 5:1:20: و ل ه~alt B002 sale separation · قَوْمٍ 5:2:30: ق و م B007 price, ق و م B010 price, ق و م B018 market · ٱلْبِرِّ 5:2:40: ب ر ر B001 bargain · +66 more (all: data/scenes/s005/trade.sale.md)
- travel.route [69 words, 13 roles] أَوْفُوا۟ 5:1:4: و ف ي B004 traveller · بَهِيمَةُ 5:1:8: ب ه م B001 road · يُتْلَىٰ 5:1:12: ت ل و B001 company · حُرُمٌ 5:1:18: ح ر م B009 hazard · يُرِيدُ 5:1:23: ر و د B003 guide, ر و د B004 traveller · ٱلْهَدْىَ 5:2:12: ه د ي B001 guide, ه د ي B002 direction, ه د ي B003 guide · +63 more (all: data/scenes/s005/travel.route.md)
- wealth.property [65 words, 13 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B004 wealth · ٱلْأَنْعَٰمِ 5:1:9: ن ع م B001 provision · حُرُمٌ 5:1:18: ح ر م B008 need · ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B006 treasure · فَضْلًۭا 5:2:20: ف ض ل B001 wealth, ف ض ل B003 generosity · شَدِيدُ 5:2:51: ش د د B006 stinginess · +59 more (all: data/scenes/s005/wealth.property.md)
- plant.growth_decay [43 words, 13 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B003 dry stalk, ع ق د B005 growth · بَهِيمَةُ 5:1:8: ب ه م B007 greenness · شَعَٰٓئِرَ 5:2:6: ش ع ر B001 down, ش ع ر B002 growth · قَوْمٍ 5:2:30: ق و م B002 root · ٱلْعِقَابِ 5:2:52: ع ق ب B015 withering · كَفَرُوا۟ 5:3:34: ك ف ر B010 leaf, ك ف ر B011 bloom · +37 more (all: data/scenes/s005/plant.growth_decay.md)
- travel.mount [58 words, 12 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B011 mount · أُحِلَّتْ 5:1:6: ح ل ل B013 load, ح ل ل B014 lameness · غَيْرَ 5:1:14: غ ي ر B001 saddle · يَحْكُمُ 5:1:21: ح ك م B006 halter · قَوْمٍ 5:2:30: ق و م B016 exhaustion · ٱلنُّصُبِ 5:3:25: ن ص ب B009 rider · +52 more (all: data/scenes/s005/travel.mount.md)
- kin.birth_nursing [53 words, 12 roles] أُحِلَّتْ 5:1:6: ح ل ل B010 birth · ٱللَّهَ 5:1:20: و ل ه~alt B002 mother child separation · ءَآمِّينَ 5:2:16: ء م م B001 nursing · رَّبِّهِمْ 5:2:22: ر ب ب B005 foster child · ٱلْمَيْتَةُ 5:3:3: م و ت B005 newborn · وَٱلْمَوْقُوذَةُ 5:3:13: و ق ذ B004 suckling · +47 more (all: data/scenes/s005/kin.birth_nursing.md)
- tool.implement [49 words, 12 roles] أُحِلَّتْ 5:1:6: ح ل ل B013 device · شَعَٰٓئِرَ 5:2:6: ش ع ر B003 knife · ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B006 key · وَٱلْمَوْقُوذَةُ 5:3:13: و ق ذ B001 club · ٱلنُّصُبِ 5:3:25: ن ص ب B006 handle · بِٱلْأَزْلَٰمِ 5:3:28: ز ل م B002 rod · +43 more (all: data/scenes/s005/tool.implement.md)
- body.wound [38 words, 12 roles] ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B010 wound · يَبْتَغُونَ 5:2:19: ب غ ي B004 swelling · ٱلْمَسْجِدِ 5:2:34: س ج د B003 scar · وَٱلدَّمُ 5:3:4: د م و B001 blood, د م و B002 bleeding, د م و B004 bleeding · وَلَحْمُ 5:3:5: ل ح م B005 wound closure, ل ح م B008 wound · وَٱلْمَوْقُوذَةُ 5:3:13: و ق ذ B001 wound, و ق ذ B006 impact site · +32 more (all: data/scenes/s005/body.wound.md)
- animal.wild [31 words, 12 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B010 gazelle · بَهِيمَةُ 5:1:8: ب ه م B003 wild cattle · ٱلْأَنْعَٰمِ 5:1:9: ن ع م B006 ostrich · حُرُمٌ 5:1:18: ح ر م B012 wolf · وَتَعَاوَنُوا۟ 5:2:38: ع و ن B006 wild ass · ٱلسَّبُعُ 5:3:18: س ب ع B002 predator · +25 more (all: data/scenes/s005/animal.wild.md)
- ritual.prayer [49 words, 11 roles] ءَامَنُوٓا۟ 5:1:3: ء م ن B003 call · ٱللَّهَ 5:1:20: ء ل ه B001 worship, ء ل ه B002 call · قَوْمٍ 5:2:30: ق و م B002 standing, ق و م B003 standing, ق و م B005 prayer performance · ٱلْمَسْجِدِ 5:2:34: س ج د B001 prostration, س ج د B002 prostration, س ج د B003 prostration, س ج د B004 bowing · ٱلْعِقَابِ 5:2:52: ع ق ب B009 recitation · قَبْلِكُمْ 5:5:23: ق ب ل B001 direction, ق ب ل B005 direction · +43 more (all: data/scenes/s005/ritual.prayer.md)
- body.eye [29 words, 11 roles] يُرِيدُ 5:1:23: ر و د B007 film over the eye · شَعَٰٓئِرَ 5:2:6: ش ع ر B005 vision · قَوْمٍ 5:2:30: ق و م B019 eye, ق و م B021 blindness · ٱلْمَسْجِدِ 5:2:34: س ج د B005 eyelid, س ج د B005 vision · أُهِلَّ 5:3:8: ه ل ل B003 weeping · وَطَعَامُ 5:5:5: ط ع م B010 eye mote · +23 more (all: data/scenes/s005/body.eye.md)
- pastoral.herding [29 words, 11 roles] أُحِلَّتْ 5:1:6: ح ل ل B011 driving · بَهِيمَةُ 5:1:8: ب ه م B004 flock · ٱلْأَنْعَٰمِ 5:1:9: ن ع م B005 herd · يُتْلَىٰ 5:1:12: ت ل و B006 follower · يُرِيدُ 5:1:23: ر و د B003 herdsman · ٱلْهَدْىَ 5:2:12: ه د ي B003 lead animal · +23 more (all: data/scenes/s005/pastoral.herding.md)
- law.judgment [48 words, 10 roles] أُحِلَّتْ 5:1:6: ح ل ل B004 sentence · يَحْكُمُ 5:1:21: ح ك م B002 verdict, ح ك م B005 judge · شَنَـَٔانُ 5:2:29: ش ن ء B003 admission · قَوْمٍ 5:2:30: ق و م B013 judgment · تَعْتَدُوا۟ 5:2:37: ع د و B005 claimant · تَسْتَقْسِمُوا۟ 5:3:27: ق س م B004 testimony · +42 more (all: data/scenes/s005/law.judgment.md)
- water.well [36 words, 10 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B016 well · ٱلْأَنْعَٰمِ 5:1:9: ن ع م B007 beam · رَّبِّهِمْ 5:2:22: ر ب ب B013 abundant water · قَوْمٍ 5:2:30: ق و م B012 pulley · أُهِلَّ 5:3:8: ه ل ل B001 water, ه ل ل B005 abundant water, ه ل ل B009 abundant water · ٱلْإِسْلَٰمَ 5:3:49: س ل م B011 bucket · +30 more (all: data/scenes/s005/water.well.md)
- dwelling.building [31 words, 10 roles] أَوْفُوا۟ 5:1:4: و ف ي B005 kiln · بِٱلْعُقُودِ 5:1:5: ع ق د B001 building · بَهِيمَةُ 5:1:8: ب ه م B001 door · حُرُمٌ 5:1:18: ح ر م B003 house · ءَآمِّينَ 5:2:16: ء م م B002 foundation · قَوْمٍ 5:2:30: ق و م B009 pillar · +25 more (all: data/scenes/s005/dwelling.building.md)
- tool.rope [30 words, 10 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B001 knot, ع ق د B013 knot · أُحِلَّتْ 5:1:6: ح ل ل B001 untying · ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B001 cord · شَدِيدُ 5:2:51: ش د د B001 tying · وَٱلْمُنْخَنِقَةُ 5:3:12: خ ن ق B001 noose · أَمْسَكْنَ 5:4:20: م س ك B001 bond, م س ك B005 strap · +24 more (all: data/scenes/s005/tool.rope.md)
- rule.obedience [53 words, 9 roles] يُتْلَىٰ 5:1:12: ت ل و B002 obedience · يَحْكُمُ 5:1:21: ح ك م B001 defiance · ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B004 submission · يَبْتَغُونَ 5:2:19: ب غ ي B003 rebellion · وَٱلْمَوْقُوذَةُ 5:3:13: و ق ذ B005 restraint · كَفَرُوا۟ 5:3:34: ك ف ر B007 defiance, ك ف ر B014 humility · +47 more (all: data/scenes/s005/rule.obedience.md)
- time.age [50 words, 9 roles] أَوْفُوا۟ 5:1:4: و ف ي B002 lifespan · أُحِلَّتْ 5:1:6: ح ل ل B004 appointed time · ءَآمِّينَ 5:2:16: ء م م B008 epoch · وَتَعَاوَنُوا۟ 5:2:38: ع و ن B002 age, ع و ن B004 old age · ٱلْعِقَابِ 5:2:52: ع ق ب B006 end · ٱلسَّبُعُ 5:3:18: س ب ع B001 week · +44 more (all: data/scenes/s005/time.age.md)
- horse.horsemanship [42 words, 9 roles] بَهِيمَةُ 5:1:8: ب ه م B005 rider · يَحْكُمُ 5:1:21: ح ك م B006 bridle · يَبْتَغُونَ 5:2:19: ب غ ي B007 rearing · تَعْتَدُوا۟ 5:2:37: ع د و B002 speed, ع د و B008 speed · وَتَعَاوَنُوا۟ 5:2:38: ع و ن B005 horse · وَٱلتَّقْوَىٰ 5:2:41: و ق ي B003 lean horse · +36 more (all: data/scenes/s005/horse.horsemanship.md)
- tool.vessel [36 words, 9 roles] أُحِلَّتْ 5:1:6: ح ل ل B013 vessel · ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B008 filling · ٱلْبَيْتَ 5:2:17: ب ي ت B006 skin bag · رَّبِّهِمْ 5:2:22: ر ب ب B010 basket · ٱلْإِسْلَٰمَ 5:3:49: س ل م B011 bucket · غَفُورٌۭ 5:3:60: غ ف ر B001 sack · +30 more (all: data/scenes/s005/tool.vessel.md)
- body.mouth_throat [35 words, 9 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B007 tongue · أُحِلَّتْ 5:1:6: ح ل ل B008 throat · يُتْلَىٰ 5:1:12: ت ل و B008 gasp · أَكَلَ 5:3:17: ء ك ل B006 teeth · ٱلسَّبُعُ 5:3:18: س ب ع B003 biting · عَلَّمْتُم 5:4:10: ع ل م B004 lip · +29 more (all: data/scenes/s005/body.mouth_throat.md)
- life.death [35 words, 9 roles] أَوْفُوا۟ 5:1:4: و ف ي B002 death · يُتْلَىٰ 5:1:12: ت ل و B008 dying · ٱلْبَيْتَ 5:2:17: ب ي ت B007 grave · يَجْرِمَنَّكُمْ 5:2:28: ج ر م B007 corpse · ٱلْمَيْتَةُ 5:3:3: م و ت B001 death, م و ت B002 killing, م و ت B004 death, م و ت B005 mourning, م و ت B007 corpse, م و ت B008 death, م و ت B010 dying, م و ت B011 corpse, م و ت B014 death · بِٱلْأَزْلَٰمِ 5:3:28: ز ل م B006 destruction · +29 more (all: data/scenes/s005/life.death.md)
- trade.debt [33 words, 9 roles] أُحِلَّتْ 5:1:6: ح ل ل B004 repayment · يُتْلَىٰ 5:1:12: ت ل و B003 balance, ت ل و B004 debt · وَرِضْوَٰنًۭا 5:2:23: ر ض و B006 surety · ٱلْعِقَابِ 5:2:52: ع ق ب B010 pledge · ٱلْإِسْلَٰمَ 5:3:49: س ل م B005 credit · وَٱذْكُرُوا۟ 5:4:22: ذ ك ر B008 written record · +27 more (all: data/scenes/s005/trade.debt.md)
- food.eating [32 words, 9 roles] أُحِلَّتْ 5:1:6: ح ل ل B010 eating · ٱلْبَيْتَ 5:2:17: ب ي ت B005 ration · يَجْرِمَنَّكُمْ 5:2:28: ج ر م B002 chewing · وَلَحْمُ 5:3:5: ل ح م B001 eating, ل ح م B002 appetite, ل ح م B003 feeding · وَٱلْمُنْخَنِقَةُ 5:3:12: خ ن ق B001 choking · أَكَلَ 5:3:17: ء ك ل B001 eating, ء ك ل B002 food · +26 more (all: data/scenes/s005/food.eating.md)
- trade.measure [28 words, 9 roles] أَوْفُوا۟ 5:1:4: و ف ي B001 full measure · قَوْمٍ 5:2:30: ق و م B010 appraisal, ق و م B015 standard coin · وَٱلتَّقْوَىٰ 5:2:41: و ق ي B004 weight · ٱلنُّصُبِ 5:3:25: ن ص ب B005 measure, ن ص ب B006 standard · تَسْتَقْسِمُوا۟ 5:3:27: ق س م B003 share · ٱلْخَٰسِرِينَ 5:5:43: خ س ر B003 cheating · +22 more (all: data/scenes/s005/trade.measure.md)
- craft.weaving [26 words, 9 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B001 knot · أُحِلَّتْ 5:1:6: ح ل ل B001 unravelling, ح ل ل B007 fabric · ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B001 twisting · وَلَحْمُ 5:3:5: ل ح م B006 weft, ل ح م B012 interlacing · تَسْتَقْسِمُوا۟ 5:3:27: ق س م B007 folded cloth · وَأَتْمَمْتُ 5:3:44: ت م م B007 weaving · +20 more (all: data/scenes/s005/craft.weaving.md)
- agri.orchard [24 words, 9 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B005 garden, ع ق د B009 grape cluster · يَجْرِمَنَّكُمْ 5:2:28: ج ر م B001 date cluster, ج ر م B002 date cluster · وَتَعَاوَنُوا۟ 5:2:38: ع و ن B004 palm · أَكَلَ 5:3:17: ء ك ل B002 fruit · فِسْقٌ 5:3:30: ف س ق B002 dates · غَفُورٌۭ 5:3:60: غ ف ر B007 tree · +18 more (all: data/scenes/s005/agri.orchard.md)
- land.mountain [24 words, 9 roles] أَوْفُوا۟ 5:1:4: و ف ي B003 highland · ٱلصَّيْدِ 5:1:16: ص ي د B005 mountain · صَدُّوكُمْ 5:2:32: ص د د B002 flank, ص د د B005 mountain · ٱلْعِقَابِ 5:2:52: ع ق ب B012 pass · بِرُءُوسِكُمْ 5:6:14: ر ء س B001 peak · صَعِيدًۭا 5:6:41: ص ع د B001 high ground, ص ع د B003 steep pass, ص ع د B008 height · +18 more (all: data/scenes/s005/land.mountain.md)
- pastoral.animal_care [23 words, 9 roles] حُرُمٌ 5:1:18: ح ر م B002 taming · ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B002 brand · يَجْرِمَنَّكُمْ 5:2:28: ج ر م B001 tending · وَٱلْمُنْخَنِقَةُ 5:3:12: خ ن ق B002 collar · وَٱلْمَوْقُوذَةُ 5:3:13: و ق ذ B004 tether · ٱلْكِتَٰبَ 5:5:8: ك ت ب B001 restraint · +17 more (all: data/scenes/s005/pastoral.animal_care.md)
- sound.sounds [15 words, 9 roles] بَهِيمَةُ 5:1:8: ب ه م B002 silence · يُتْلَىٰ 5:1:12: ت ل و B007 voice · صَدُّوكُمْ 5:2:32: ص د د B006 noise, ص د د B011 noise · أُهِلَّ 5:3:8: ه ل ل B003 impact · مُكَلِّبِينَ 5:4:13: ك ل ب B003 howl · صَعِيدًۭا 5:6:41: ص ع د B007 sigh · +9 more (all: data/scenes/s005/sound.sounds.md)
- pastoral.breeding [41 words, 8 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B010 mating · أُحِلَّتْ 5:1:6: ح ل ل B009 barrenness, ح ل ل B010 newborn · ٱلْمَيْتَةُ 5:3:3: م و ت B005 offspring · ٱلْجَوَارِحِ 5:4:12: ج ر ح B006 pregnancy · وَٱذْكُرُوا۟ 5:4:22: ذ ك ر B001 stallion · ٱلصَّلَوٰةِ 5:6:7: ص ل و B005 birth · +35 more (all: data/scenes/s005/pastoral.breeding.md)
- sky.bodies [32 words, 8 roles] ٱلْأَنْعَٰمِ 5:1:9: ن ع م B007 constellation · شَعَٰٓئِرَ 5:2:6: ش ع ر B008 star · ٱلشَّهْرَ 5:2:9: ش ه ر B001 moon · قَوْمٍ 5:2:30: ق و م B017 zenith · ذَكَّيْتُمْ 5:3:21: ذ ك و B005 sun · بِٱلْأَزْلَٰمِ 5:3:28: ز ل م B012 rising · +26 more (all: data/scenes/s005/sky.bodies.md)
- time.day_night [29 words, 8 roles] ٱلْبَيْتَ 5:2:17: ب ي ت B004 night · قَوْمٍ 5:2:30: ق و م B017 noon · ذَكَّيْتُمْ 5:3:21: ذ ك و B005 dawn · ٱلْيَوْمَ 5:3:31: ي و م B001 daylight, ي و م B005 day · كَفَرُوا۟ 5:3:34: ك ف ر B002 darkness · وُجُوهَكُمْ 5:6:9: و ج ه B007 morning · +23 more (all: data/scenes/s005/time.day_night.md)
- land.soil [26 words, 8 roles] ٱلصَّيْدِ 5:1:16: ص ي د B005 hard ground · يَجْرِمَنَّكُمْ 5:2:28: ج ر م B010 earth · ٱلْمَيْتَةُ 5:3:3: م و ت B003 barren soil · مُتَّخِذِىٓ 5:5:31: ء خ ذ B005 land · سَفَرٍ 5:6:27: س ف ر B001 dust · ٱلْغَآئِطِ 5:6:33: غ و ط B002 sinking · +20 more (all: data/scenes/s005/land.soil.md)
- speech.news [23 words, 8 roles] يُتْلَىٰ 5:1:12: ت ل و B009 rumour · عَلَّمْتُم 5:4:10: ع ل م B001 message · ٱسْمَ 5:4:23: س م و B008 report · ٱلْحِسَابِ 5:4:31: ح س ب B010 news seeking · سَفَرٍ 5:6:27: س ف ر B005 messenger · لِيَجْعَلَ 5:6:50: ج ع ل B003 statement · +17 more (all: data/scenes/s005/speech.news.md)
- kin.marriage [21 words, 8 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B002 contract · أُحِلَّتْ 5:1:6: ح ل ل B006 spouse · ٱلْهَدْىَ 5:2:12: ه د ي B006 bride conveyance · ٱلْبَيْتَ 5:2:17: ب ي ت B010 groom · ٱضْطُرَّ 5:3:52: ض ر ر B004 wife · ٱلطَّيِّبَٰتُ 5:4:8: ط ي ب B004 marriage · +15 more (all: data/scenes/s005/kin.marriage.md)
- water.gathered [21 words, 8 roles] ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B008 filling · ٱلْبَيْتَ 5:2:17: ب ي ت B006 stored liquid · فَضْلًۭا 5:2:20: ف ض ل B001 water level · رَّبِّهِمْ 5:2:22: ر ب ب B013 pool · قَوْمٍ 5:2:30: ق و م B016 stagnant water · صَدُّوكُمْ 5:2:32: ص د د B010 cistern · +15 more (all: data/scenes/s005/water.gathered.md)
- emotion.anger [20 words, 8 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B012 anger · ٱلصَّيْدِ 5:1:16: ص ي د B003 rage · وَرِضْوَٰنًۭا 5:2:23: ر ض و B004 appeasement · شَنَـَٔانُ 5:2:29: ش ن ء B001 enmity, ش ن ء B002 aversion, ش ن ء B004 enmity · ٱلسَّبُعُ 5:3:18: س ب ع B003 hostility · مُكَلِّبِينَ 5:4:13: ك ل ب B004 aggression · +14 more (all: data/scenes/s005/emotion.anger.md)
- food.cooking [17 words, 8 roles] فَضْلًۭا 5:2:20: ف ض ل B001 meal · ٱلْبِرِّ 5:2:40: ب ر ر B006 bread · ٱلْعِقَابِ 5:2:52: ع ق ب B011 broth · ٱلْمَيْتَةُ 5:3:3: م و ت B002 cooking, م و ت B007 meat · أَكَلَ 5:3:17: ء ك ل B001 meal, ء ك ل B007 meat, ء ك ل B011 meal, ء ك ل B013 pot · مَخْمَصَةٍ 5:3:54: خ م ص B002 hunger · +11 more (all: data/scenes/s005/food.cooking.md)
- light.light_dark [16 words, 8 roles] بَهِيمَةُ 5:1:8: ب ه م B002 darkness · أَكَلَ 5:3:17: ء ك ل B005 shining · ذَكَّيْتُمْ 5:3:21: ذ ك و B005 radiance · كَفَرُوا۟ 5:3:34: ك ف ر B001 shadow · مَخْمَصَةٍ 5:3:54: خ م ص B008 dimness · وَأَرْجُلَكُمْ 5:6:15: ر ج ل B012 light · +10 more (all: data/scenes/s005/light.light_dark.md)
- posture.upright [14 words, 8 roles] ٱلصَّيْدِ 5:1:16: ص ي د B002 rearing · ٱلْهَدْىَ 5:2:12: ه د ي B010 bearing · قَوْمٍ 5:2:30: ق و م B002 standing, ق و م B005 setting upright, ق و م B008 straight, ق و م B011 erect, ق و م B016 standing · ٱلنُّصُبِ 5:3:25: ن ص ب B001 upright · بِٱلْأَزْلَٰمِ 5:3:28: ز ل م B012 standing · صَعِيدًۭا 5:6:41: ص ع د B006 straight pole · +8 more (all: data/scenes/s005/posture.upright.md)
- colour.colours [13 words, 8 roles] بَهِيمَةُ 5:1:8: ب ه م B002 colour · ٱلْعِقَابِ 5:2:52: ع ق ب B015 yellow · وَٱلدَّمُ 5:3:4: د م و B003 red · مَخْمَصَةٍ 5:3:54: خ م ص B004 black · أَمْسَكْنَ 5:4:20: م س ك B011 white marking · ٱلْحِسَابِ 5:4:31: ح س ب B009 skin color · +7 more (all: data/scenes/s005/colour.colours.md)
- craft.wood [10 words, 8 roles] يُرِيدُ 5:1:23: ر و د B006 shaft · بِٱلْأَزْلَٰمِ 5:3:28: ز ل م B002 shaft making · وَٱمْسَحُوا۟ 5:6:13: م س ح B013 shaping · ٱلْكَعْبَيْنِ 5:6:17: ك ع ب B005 joint · ٱلْغَآئِطِ 5:6:33: غ و ط B004 bent wood · سَمِعْنَا 5:7:11: س م ع B008 wood, س م ع B015 beam · +4 more (all: data/scenes/s005/craft.wood.md)
- dress.garment [54 words, 7 roles] أُحِلَّتْ 5:1:6: ح ل ل B007 garment · ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B003 belt · صَدُّوكُمْ 5:2:32: ص د د B012 veil · وَٱلتَّقْوَىٰ 5:2:41: و ق ي B001 protective cloth · وَٱلْمُتَرَدِّيَةُ 5:3:14: ر د ي B004 cloak · وَأَيْدِيَكُمْ 5:6:10: ي د ي B013 sleeve, ي د ي B014 garment · +48 more (all: data/scenes/s005/dress.garment.md)
- war.protection [51 words, 7 roles] ءَامَنُوٓا۟ 5:1:3: ء م ن B001 refuge · أُحِلَّتْ 5:1:6: ح ل ل B006 neighbour right · حُرُمٌ 5:1:18: ح ر م B006 protection pact · ٱلْهَدْىَ 5:2:12: ه د ي B007 protected client · وَتَعَاوَنُوا۟ 5:2:38: ع و ن B001 ally · وَٱلتَّقْوَىٰ 5:2:41: و ق ي B001 protection · +45 more (all: data/scenes/s005/war.protection.md)
- dwelling.settlement [46 words, 7 roles] أُحِلَّتْ 5:1:6: ح ل ل B002 dwelling place · قَوْمٍ 5:2:30: ق و م B006 dwelling place, ق و م B018 market · وَتَعَاوَنُوا۟ 5:2:38: ع و ن B008 town · كَفَرُوا۟ 5:3:34: ك ف ر B012 village · وَٱلْمُحْصَنَٰتُ 5:5:14: ح ص ن B001 fortress · جُنُبًۭا 5:6:20: ج ن ب B001 outskirts · +40 more (all: data/scenes/s005/dwelling.settlement.md)
- water.spring_stream [40 words, 7 roles] ٱللَّهَ 5:1:20: و ل ه~alt B003 flow · صَدُّوكُمْ 5:2:32: ص د د B004 source · تَعْتَدُوا۟ 5:2:37: ع د و B009 channel · كَفَرُوا۟ 5:3:34: ك ف ر B011 spring · أُوتُوا۟ 5:5:7: ء ت ي B004 channel, ء ت ي B005 torrent · ٱلْمَرَافِقِ 5:6:12: ر ف ق B003 source, ر ف ق B009 overflow · +34 more (all: data/scenes/s005/water.spring_stream.md)
- emotion.pride [37 words, 7 roles] غَيْرَ 5:1:14: غ ي ر B004 honour · ٱلصَّيْدِ 5:1:16: ص ي د B002 arrogance · يَحْكُمُ 5:1:21: ح ك م B003 humility · ٱلشَّهْرَ 5:2:9: ش ه ر B002 reputation · ٱلْقَلَٰٓئِدَ 5:2:14: ق ل د B005 shame · فَضْلًۭا 5:2:20: ف ض ل B002 honour, ف ض ل B004 pride · +31 more (all: data/scenes/s005/emotion.pride.md)
- motion.gather_scatter [36 words, 7 roles] أَوْفُوا۟ 5:1:4: و ف ي B004 gathering · ٱلْأَنْعَٰمِ 5:1:9: ن ع م B008 dispersal · ءَآمِّينَ 5:2:16: ء م م B004 crowd · تَسْتَقْسِمُوا۟ 5:3:27: ق س م B003 separation · وَأَرْجُلَكُمْ 5:6:15: ر ج ل B006 swarm · بِٱلْقِسْطِ 5:8:8: ق س ط B009 scattered group · +30 more (all: data/scenes/s005/motion.gather_scatter.md)
- motion.pace [30 words, 7 roles] ٱلْأَنْعَٰمِ 5:1:9: ن ع م B012 slowness · ءَآمِّينَ 5:2:16: ء م م B008 delay · يَبْتَغُونَ 5:2:19: ب غ ي B007 running · أُهِلَّ 5:3:8: ه ل ل B008 haste · ٱلْءَاخِرَةِ 5:5:41: ء خ ر B002 waiting · وَأَرْجُلَكُمْ 5:6:15: ر ج ل B015 pace, ر ج ل B020 proceeding · +24 more (all: data/scenes/s005/motion.pace.md)
- motion.up_down [29 words, 7 roles] أَوْفُوا۟ 5:1:4: و ف ي B003 climbing · أُحِلَّتْ 5:1:6: ح ل ل B004 descending · ٱلشَّهْرَ 5:2:9: ش ه ر B003 raising · قَوْمٍ 5:2:30: ق و م B011 height · ٱلْمَسْجِدِ 5:2:34: س ج د B004 lowering · وَٱلْمُتَرَدِّيَةُ 5:3:14: ر د ي B003 falling · +23 more (all: data/scenes/s005/motion.up_down.md)
- rule.ownership [26 words, 7 roles] بِٱلْعُقُودِ 5:1:5: ع ق د B004 possession · ءَآمِّينَ 5:2:16: ء م م B014 servant · رَّبِّهِمْ 5:2:22: ر ب ب B001 owner · شَنَـَٔانُ 5:2:29: ش ن ء B003 release · ٱلْبِرِّ 5:2:40: ب ر ر B008 master · وَطَعَامُ 5:5:5: ط ع م B011 mastery · +20 more (all: data/scenes/s005/rule.ownership.md)
- further scenes, in order (every member in data/scenes/s005/<scene>.md): water.rain_cloud (25 words, 7 roles), sign.marking (22 words, 7 roles), quantity.more_less (44 words, 6 roles), rule.leadership (37 words, 6 roles), travel.departure_return (36 words, 6 roles), trade.gift (35 words, 6 roles), emotion.love (34 words, 6 roles), kin.lineage (33 words, 6 roles), ritual.sanctuary (30 words, 6 roles), animal.birds (29 words, 6 roles), animal.small (29 words, 6 roles), law.reckoning (23 words, 6 roles), dress.adornment (20 words, 6 roles), hunt.chase (20 words, 6 roles), motion.turning (19 words, 6 roles), agri.sowing_harvest (17 words, 6 roles), life.growing_up (16 words, 6 roles), speech.recitation (16 words, 6 roles), land.stone (11 words, 6 roles), land.valley (11 words, 6 roles), fire.heat (9 words, 6 roles), fire.kindling (9 words, 6 roles), water.thirst_drinking (8 words, 6 roles), water.washing (8 words, 6 roles), rule.covenant (69 words, 5 roles), pastoral.livestock_wealth (51 words, 5 roles), emotion.grief_joy (38 words, 5 roles), emotion.fear (33 words, 5 roles), kin.household (33 words, 5 roles), speech.praise_blame (31 words, 5 roles), weather.season (23 words, 5 roles), rule.kingship (21 words, 5 roles), food.sweet_fat (20 words, 5 roles), pastoral.grazing (20 words, 5 roles), speech.poetry (19 words, 5 roles), craft.metal (15 words, 5 roles), ritual.purity (14 words, 5 roles), ritual.sacrifice (11 words, 5 roles), sign.writing (11 words, 5 roles), ritual.idols_lots (38 words, 4 roles), law.boundary (28 words, 4 roles), pastoral.milking (22 words, 4 roles), craft.leather (16 words, 4 roles), dwelling.furnishing (15 words, 4 roles), weather.wind (15 words, 4 roles), agri.pressing (14 words, 4 roles), body.innards (14 words, 4 roles), dwelling.hearth (14 words, 4 roles), sign.counting (13 words, 4 roles), water.sea (12 words, 4 roles), trade.hire (11 words, 4 roles), posture.leaning (10 words, 4 roles), water.irrigation (10 words, 4 roles), quantity.full_empty (9 words, 4 roles), war.vengeance (9 words, 4 roles), race.horse_race (8 words, 4 roles), animal.reptile_fish (7 words, 4 roles), new.acceptance (4 words, 4 roles), pastoral.watering_herd (4 words, 4 roles), land.desert_sand (25 words, 3 roles), plant.desert (15 words, 3 roles), travel.open_land (10 words, 3 roles), travel.night (9 words, 3 roles), craft.dyeing (8 words, 3 roles), craft.clay (5 words, 3 roles), speech.secret (4 words, 3 roles), travel.sea (4 words, 3 roles), dwelling.tent_camp (10 words, 2 roles), hunt.trap (9 words, 2 roles), craft.coating (6 words, 2 roles), life.rising (6 words, 2 roles), horse.charge_raid (5 words, 2 roles), land.cave_pit (5 words, 2 roles), new.sexual_intercourse (4 words, 2 roles), new.spatial_position (3 words, 2 roles), position.middle (3 words, 2 roles), know.divination (2 words, 2 roles), new.sleep_state (2 words, 2 roles), new.social_encounter (2 words, 2 roles), drink.wine (5 words, 1 roles), new.softness_comfort (5 words, 1 roles), kin.orphan (4 words, 1 roles), new.created_world (4 words, 1 roles), new.skilled_craft (4 words, 1 roles), new.adversity (3 words, 1 roles), new.being_occurrence (3 words, 1 roles), new.body_sex (3 words, 1 roles), new.custom_habit (3 words, 1 roles), new.efficacy (3 words, 1 roles), new.intentional_action (3 words, 1 roles), new.major_event (3 words, 1 roles), new.sexual_continence (3 words, 1 roles), new.social_disavowal (3 words, 1 roles), new.task_preparation (3 words, 1 roles), new.use_application (3 words, 1 roles), new.volition (3 words, 1 roles), new.aversion (2 words, 1 roles), new.contest (2 words, 1 roles), new.creature_sequence (2 words, 1 roles), new.deliberation (2 words, 1 roles), new.ghoul (2 words, 1 roles), new.hardship (2 words, 1 roles), new.human_intercourse (2 words, 1 roles), new.material_solidity (2 words, 1 roles), new.mutual_consent (2 words, 1 roles), new.position_front_surface (2 words, 1 roles), new.state_selfhood (2 words, 1 roles), new.visible_appearance (2 words, 1 roles)
- abstract scenes, mostly the plain sense (every member in data/scenes/s005/<scene>.md): moral.good_evil (74 words, 10 roles), divine.lordship (63 words, 6 roles), moral.truth_falsehood (43 words, 6 roles), moral.guidance_error (15 words, 4 roles)

## Scenes of this window that reach elsewhere in the surah (at most 10 far words each, new roles first; every member in the file named)

- body.limbs [645 words in the surah, 59 roles] in this window: 90 words (animal part, ankle, appendage, arm, back, bone, crooked leg, elbow, face, facing, finger, flank, flesh, foot, forelock, grasp, hair, hand, head, heel, joint, leg, leg tendon, legs, neck, proportion, shoulder, skin, stature, thumb, vein, wrist) | beyond the neighbourhood, 555 words; roles missing here: body, body frame, chest, contact, creases, ear, foot edge, forearm, genital organ, genitalia, hair trimming, hands, haunch, head and neck, hindpart, hindtoe, leg muscle, neck joint, organ, ribs, scalp, side, skin contact, tail, tailbone, uneven hips, upper part: حَسَنًۭا 5:12:27 forearm · سَيِّـَٔاتِكُمْ 5:12:30 genitalia · جَنَّٰتٍۢ 5:12:32 ribs · وَٱصْفَحْ 5:13:28 flank, hand, hands · +551 more (all: data/scenes/s005/body.limbs.md)
- know.perceiving [516 words in the surah, 47 roles] in this window: 43 words (belief, conjecture, discernment, finding, guessing, hearing, ignorance, inquiry, inspiration, intellect, judgment, knowing, learning, noticing, perceiving, recollection, seeking, supposition, thought, understanding) | beyond the neighbourhood, 473 words; roles missing here: appearance, bewilderment, confusion, deception, deliberation, discovery, distinguishing, doubt, experience, expertise, forgetting, hidden knowledge, ignoring, impaired reason, impression, insight, inspection, intention, investigation, knowledge, loss of reason, opinion, recognising, testing, unknown, watcher, watching: جَنَّٰتٍۢ 5:12:32 impaired reason · بَعْدَ 5:12:39 insight · ضَلَّ 5:12:43 forgetting · تَزَالُ 5:13:18 recognising · +469 more (all: data/scenes/s005/know.perceiving.md)
- tool.implement [346 words in the surah, 38 roles] in this window: 49 words (bat, club, device, handle, hook, key, knife, mirror, pestle, pot lifter, restraint, rod) | beyond the neighbourhood, 297 words; roles missing here: axe, cane, cutter, cutting, equipment, filter, fire drill, gear, impact, implement, iron collar, ladle, lock, needle, point, scissors, scraping, sealing, skewer, sounding stone, staff, stick, stirring tool, weapon, whetstone, whip: وَنَسُوا۟ 5:13:12 staff · يَصْنَعُونَ 5:14:25 skewer · بِذُنُوبِكُم 5:18:11 ladle · يُوَٰرِى 5:31:9 fire drill · +293 more (all: data/scenes/s005/tool.implement.md)
- speech.calling [671 words in the surah, 42 roles] in this window: 85 words (address, addressing, affirmation, answer, call, chatter, cry, message, naming, negotiation, petition, question, questioner, quick speech, request, saying, signal, speaker, speech, summons, utterance) | beyond the neighbourhood, 586 words; roles missing here: alarm cry, announcement, articulation, command, consultation, conversation, discussion, entreaty, exclamation, greeting, imprecation, invocation, listening, mockery, provocation, refusal, silence, talk, urging, warning, whisper: لَعَنَّٰهُمْ 5:13:4 imprecation, invocation, address · وَٱصْفَحْ 5:13:28 refusal · يُنَبِّئُهُمُ 5:14:21 announcement, whisper · يَٰٓأَهْلَ 5:15:1 greeting · +582 more (all: data/scenes/s005/speech.calling.md)
- body.illness [436 words in the surah, 35 roles] in this window: 56 words (contagion, disease, fever, healer, healing, hoof pain, illness, itch, medicine, pain, physician, poison, seizure, skin disease, swelling) | beyond the neighbourhood, 380 words; roles missing here: affliction, bodily intolerance, cold, crisis, dehydration, derangement, dizziness, infection, infestation, injury, irritation, madness, patient, pus, recovery, respiratory disease, spasm, throbbing, tremor, venom: ٱلْأَرْضِ 5:17:27 tremor, disease, infection, derangement · دَامُوا۟ 5:24:8 dizziness · فَقَٰتِلَآ 5:24:13 madness · فَٱحْذَرُوا۟ 5:41:40 irritation · +376 more (all: data/scenes/s005/body.illness.md)
- body.innards [177 words in the surah, 23 roles] in this window: 14 words (belly, chest, defecation, heart) | beyond the neighbourhood, 163 words; roles missing here: afflicted heart, artery, body core, bowels, breast, excrement, heart cords, innards, inner heat, kidney, liver, lung, marrow, navel, omentum, ribs, settled heart, swallowing, womb: بَنِىٓ 5:12:5 ribs · وَأَقْرَضْتُمُ 5:12:24 bowels · فَٱفْرُقْ 5:25:9 heart, kidney · يُوَٰرِى 5:31:9 innards · +159 more (all: data/scenes/s005/body.innards.md)
- dwelling.building [256 words in the surah, 27 roles] in this window: 31 words (building, door, foundation, house, house cleaning, kiln, pillar, roof, square building, wall) | beyond the neighbourhood, 225 words; roles missing here: adjacent house, cover, demolition, door panel, dwelling place, fortress, high building, house dweller, oven, prison, ruins, storehouse, structural support, structure, tower, upper part, upper room: نَقْضِهِم 5:13:2 demolition · وَٱصْفَحْ 5:13:28 door panel · يَصْنَعُونَ 5:14:25 structure · بِإِذْنِهِۦ 5:16:14 tower · +221 more (all: data/scenes/s005/dwelling.building.md)
- body.wound [286 words in the surah, 28 roles] in this window: 38 words (bleeding, blood, cutting, fracture, harm, impact site, injury, menstrual blood, scar, swelling, wound, wound closure) | beyond the neighbourhood, 248 words; roles missing here: bite, blow, blunt blow, bruise, cautery mark, cut cord, gash, healing, incision, mutilation, piercing, severe blow, severing, sore, striking, wounding: نَقِيبًۭا 5:12:11 piercing, sore, wound · وَٱصْفَحْ 5:13:28 blunt blow · بَيْنَهُمُ 5:14:14 severing · جَبَّارِينَ 5:22:6 healing · +244 more (all: data/scenes/s005/body.wound.md)
- tool.vessel [282 words in the surah, 24 roles] in this window: 36 words (basket, bucket, case, container, filling, sack, skin bag, vessel, waterskin) | beyond the neighbourhood, 246 words; roles missing here: aperture, bowl, capacity, crosspiece, cup, drinking cup, handle, jar, leak, lid, pitcher, platter, pot, pouch, stopper: قَلِيلًۭا 5:13:24 jar · فَٱعْفُ 5:13:26 pot · بِإِذْنِهِۦ 5:16:14 handle · فَأَصْبَحَ 5:30:7 drinking cup · +242 more (all: data/scenes/s005/tool.vessel.md)
- war.battle [573 words in the surah, 36 roles] in this window: 80 words (army, battle, captive, charge, combat, confrontation, courage, defeat, enemy, fighter, infantry, killing, opponent, raid, raiders, rank, readiness, retreat, rout, victim, victory, volunteer) | beyond the neighbourhood, 493 words; roles missing here: army flank, challenge, combatants, conflict, engagement, incitement, muster, piercing, scout, spoils, valor, vanguard, warfare, warrior: نَقِيبًۭا 5:12:11 valor · وَٱصْفَحْ 5:13:28 challenge · جَمِيعًۭا 5:17:28 spoils, army, captive · فَقَٰتِلَآ 5:24:13 combatants · +489 more (all: data/scenes/s005/war.battle.md)
- body.strength [481 words in the surah, 30 roles] in this window: 68 words (build, capacity, effort, fatigue, fatness, firmness, frailty, frame, largeness, leanness, loss of strength, stamina, steadfastness, stiffness, strength, weakness) | beyond the neighbourhood, 413 words; roles missing here: body, body form, bulk, endurance, exertion, heaviness, large stature, lightness, muscle, physique, recovery, robustness, sturdiness, tall stature: بَنِىٓ 5:12:5 body form, fatness · حَسَنًۭا 5:12:27 exertion · قَٰسِيَةًۭ 5:13:7 endurance · فَقَٰتِلَآ 5:24:13 sturdiness · +409 more (all: data/scenes/s005/body.strength.md)
- food.cooking [157 words in the surah, 21 roles] in this window: 17 words (bread, broth, cooking, hunger, meal, meat, pot, roasting) | beyond the neighbourhood, 140 words; roles missing here: boiling pot, clove, dish, feast, food, leaven, mixture, pot support, predawn meal, reheated food, spice, spoiled food, wholesome food: ٱلزَّكَوٰةَ 5:12:20 wholesome food · يَصْنَعُونَ 5:14:25 roasting, feast · خِلَٰفٍ 5:33:20 spoiled food · تُفْلِحُونَ 5:35:13 predawn meal · +136 more (all: data/scenes/s005/food.cooking.md)
- craft.metal [72 words in the surah, 18 roles] in this window: 15 words (copper, iron, metal plating, silver, solder) | beyond the neighbourhood, 57 words; roles missing here: anvil, bellows, dross, forge, gold, heated iron, iron column, iron cutting, molten metal, nail, shaping, smith, smithing: قُلُوبَهُمْ 5:13:6 shaping · يُهْلِكَ 5:17:20 smith · قَدِيرٌۭ 5:17:42 smithing · فَٱذْهَبْ 5:24:10 gold · +53 more (all: data/scenes/s005/craft.metal.md)
- plant.growth_decay [440 words in the surah, 25 roles] in this window: 43 words (bloom, branch, down, dry stalk, garden, greenness, growth, leaf, plant, root, shoot, withering, young tree) | beyond the neighbourhood, 397 words; roles missing here: creeper, decay, dense growth, leaf growth, regrowth, revived earth, sap, sprout, thickening, tree, trees, undergrowth: وَعَزَّرْتُمُوهُمْ 5:12:23 tree, branch · جَنَّٰتٍۢ 5:12:32 trees, growth · ٱلْأَرْضِ 5:17:27 decay · جَمِيعًۭا 5:17:28 sprout · +393 more (all: data/scenes/s005/plant.growth_decay.md)
- land.soil [265 words in the surah, 20 roles] in this window: 26 words (barren soil, dust, earth, earth surface, ground, hard ground, land, sinking) | beyond the neighbourhood, 239 words; roles missing here: digging, earth barrier, fertile soil, field plot, fissure, heap, hollow, moisture, mud, ploughing, soil, wet soil: ٱلْأَرْضِ 5:17:27 earth, fertile soil · أَدْبَارِكُمْ 5:21:12 field plot · يَبْحَثُ 5:31:4 digging, earth, barren soil, mud · تُفْلِحُونَ 5:35:13 fissure, ploughing · +235 more (all: data/scenes/s005/land.soil.md)
- sound.sounds [122 words in the surah, 21 roles] in this window: 15 words (howl, hum, impact, noise, roar, sigh, silence, sound, voice) | beyond the neighbourhood, 107 words; roles missing here: bleating, clamor, clang, clapping, creak, cry, echo, gasp, instrument, listening, rattle, whisper: نَقْضِهِم 5:13:2 creak, cry · قَلِيلًۭا 5:13:24 rattle · وَٱصْفَحْ 5:13:28 clapping · يُنَبِّئُهُمُ 5:14:21 whisper · +103 more (all: data/scenes/s005/sound.sounds.md)
- wealth.property [585 words in the surah, 24 roles] in this window: 65 words (desired need, distribution, generosity, giving, greed, loss, need, petitioner, possession, provision, stinginess, treasure, wealth) | beyond the neighbourhood, 520 words; roles missing here: benefit, deficit, earning, gain, livelihood, lost animal, ownership, poverty, prosperity, withholding, worldly pursuit: ٱلزَّكَوٰةَ 5:12:20 prosperity, giving · بَعْدَ 5:12:39 benefit · يُحَرِّفُونَ 5:13:8 provision, poverty · خَآئِنَةٍۢ 5:13:21 deficit · +516 more (all: data/scenes/s005/wealth.property.md)
- motion.passage [441 words in the surah, 28 roles] in this window: 59 words (being swallowed, channel, dislodging, drawing out, emerging, entering, obstruction, opening, passage, passing through, penetrating, plunging, removal, succession, transmission, vanishing, withdrawal) | beyond the neighbourhood, 382 words; roles missing here: approach, approaching, arriving, becoming, cleavage, going and coming, hidden object, nonarrival, penetration, release, separation: بِرُسُلِى 5:12:22 release · بَعْدَ 5:12:39 separation · تَطَّلِعُ 5:13:19 entering, approach · فَٱفْرُقْ 5:25:9 cleavage · +378 more (all: data/scenes/s005/motion.passage.md)
- travel.mount [375 words in the surah, 23 roles] in this window: 58 words (dismounting, exhaustion, halter, lameness, leading, load, mount, rein, rider, saddle, taming, urging on) | beyond the neighbourhood, 317 words; roles missing here: dismount, driver, extra load, harness, injured camel, mount gait, overload, resisting restraint, rider position, riding, tether: أَعَجَزْتُ 5:31:14 rider position · وَجَٰهِدُوا۟ 5:35:9 overload · تُفْلِحُونَ 5:35:13 driver · وَعِندَهُمُ 5:43:3 resisting restraint · +313 more (all: data/scenes/s005/travel.mount.md)
- kin.lineage [333 words in the surah, 17 roles] in this window: 33 words (ancestor, clan, kin tie, lineage, tribe, unknown lineage) | beyond the neighbourhood, 300 words; roles missing here: childlessness, cousin, descendant, distant kin, family, heir, inheritance, kin, offspring, pure lineage, youngest: بَعْدَ 5:12:39 kin tie, distant kin · وَيُخْرِجُهُم 5:16:9 lineage, inheritance · تَرْتَدُّوا۟ 5:21:10 family · فَقَٰتِلَآ 5:24:13 cousin · +296 more (all: data/scenes/s005/kin.lineage.md)
- emotion.grief_joy [305 words in the surah, 16 roles] in this window: 38 words (contentment, gladness, grief, joy, sorrow) | beyond the neighbourhood, 267 words; roles missing here: consolation, delight, despair, disappointment, enjoyment, happiness, mourning, regret, relief, remorse, suffering: نَفْسِى 5:25:7 consolation · ٱلنَّٰدِمِينَ 5:31:25 regret · تُقَطَّعَ 5:33:16 despair, remorse · فِتْنَتَهُۥ 5:41:44 suffering, joy · +263 more (all: data/scenes/s005/emotion.grief_joy.md)
- quantity.more_less [302 words in the surah, 17 roles] in this window: 44 words (completion, decrease, deficit, excess, increase, remainder) | beyond the neighbourhood, 258 words; roles missing here: abundance, depletion, division, fragment, growth, intensity, large size, majority, maximum, outnumbering, part: بَنِىٓ 5:12:5 growth · حَسَنًۭا 5:12:27 maximum · كَثِيرًۭا 5:15:8 increase, outnumbering, abundance, excess · يَخَافُونَ 5:23:5 intensity, decrease · +254 more (all: data/scenes/s005/quantity.more_less.md)
- dress.garment [252 words in the surah, 18 roles] in this window: 54 words (belt, cloak, garment, hem, protective cloth, sleeve, veil) | beyond the neighbourhood, 198 words; roles missing here: apron, armour, chest grip, leather shirt, lining, rag, shoe, shroud, turban, undergarment, wrap: وَلَأُدْخِلَنَّكُمْ 5:12:31 lining · جَنَّٰتٍۢ 5:12:32 veil, shroud · وَنَسُوا۟ 5:13:12 rag · يَخَافُونَ 5:23:5 apron · +194 more (all: data/scenes/s005/dress.garment.md)
- animal.birds [202 words in the surah, 17 roles] in this window: 29 words (bird, bird of prey, claw, feather, partridge, young bird) | beyond the neighbourhood, 173 words; roles missing here: chirp, crest, divided crest, flight, flock, migrating bird, nestling, perch, scarecrow, tail, wing: لَعَنَّٰهُمْ 5:13:4 scarecrow · بِذُنُوبِكُم 5:18:11 tail · دَامُوا۟ 5:24:8 flight · قَٰعِدُونَ 5:24:16 nestling · +169 more (all: data/scenes/s005/animal.birds.md)
- agri.sowing_harvest [148 words in the surah, 17 roles] in this window: 17 words (barren ground, cultivation, grain, harvest, ploughing, sowing) | beyond the neighbourhood, 131 words; roles missing here: crop, crop remnant, ear, field effigy, furrow, grain husk, growth, kernel, ploughman, seed, sprout: ٱلزَّكَوٰةَ 5:12:20 crop · ٱلسَّبِيلِ 5:12:45 ear · لَعَنَّٰهُمْ 5:13:4 field effigy · يُحَرِّفُونَ 5:13:8 seed · +127 more (all: data/scenes/s005/agri.sowing_harvest.md)
- travel.route [514 words in the surah, 23 roles] in this window: 69 words (company, destination, direction, diversion, guide, halt, hazard, leader, main course, road, road surface, traveller, waymark) | beyond the neighbourhood, 445 words; roles missing here: distance, entrance, fork, getting lost, straggler, stray, trace, track, unfit traveller, way: بَنِىٓ 5:12:5 fork · بَعْدَ 5:12:39 distance · ضَلَّ 5:12:43 stray · فَٱذْهَبْ 5:24:10 way · +441 more (all: data/scenes/s005/travel.route.md)
- war.arms [375 words in the surah, 28 roles] in this window: 43 words (armour, arrow, arrow shaft, bow, bow end, bowstring, cutting, edge, knife, piercing, shaft, shield, spear, spear shaft, spearhead, stone missile, sword, sword sheath) | beyond the neighbourhood, 332 words; roles missing here: armour lining, broad blade, broken spear, old arrow, spear part, spear point, striking, sword pommel, weapon, weapon spine: قَلِيلًۭا 5:13:24 sword pommel · وَٱصْفَحْ 5:13:28 broad blade, sword · فَٱحْذَرُوا۟ 5:41:40 weapon · مَغْلُولَةٌ 5:64:5 armour, armour lining · +328 more (all: data/scenes/s005/war.arms.md)
- time.age [325 words in the surah, 19 roles] in this window: 50 words (age, appointed time, delay, duration, end, epoch, lifespan, old age, week) | beyond the neighbourhood, 275 words; roles missing here: beginning, continuance, ending, interval, later period, month, onset, past, time interval, year: جَنَّٰتٍۢ 5:12:32 onset · بَعْدَ 5:12:39 later period, interval · أَدْبَارِكُمْ 5:21:12 ending · سَنَةًۭ 5:26:6 year · +271 more (all: data/scenes/s005/time.age.md)
- motion.gather_scatter [294 words in the surah, 17 roles] in this window: 36 words (crowd, dispersal, gathering, scattered group, separation, spreading, swarm) | beyond the neighbourhood, 258 words; roles missing here: collecting, discard, discarding, dispersion, group, grouping, joining, placement, procession, scattering: عَشَرَ 5:12:10 gathering, grouping, dispersal · بِرُسُلِى 5:12:22 procession · وَنَسُوا۟ 5:13:12 discard · كَثِيرًۭا 5:15:8 scattering, gathering · +254 more (all: data/scenes/s005/motion.gather_scatter.md)
- law.judgment [383 words in the surah, 19 roles] in this window: 48 words (admission, claimant, decree, exemption, judge, judgment, sentence, testimony, verdict, witness) | beyond the neighbourhood, 335 words; roles missing here: compensation, exoneration, fairness, mediation, no liability, offense, pardon, penalty, punishment: وَٱصْفَحْ 5:13:28 pardon · نَذِيرٍۢ 5:19:19 compensation · لِلسُّحْتِ 5:42:4 no liability · خَلَتْ 5:75:8 exoneration · +331 more (all: data/scenes/s005/law.judgment.md)
- further scenes reaching beyond the neighbourhood (every member in data/scenes/s005/<scene>.md): agri.orchard (229), agri.pressing (65), animal.reptile_fish (51), animal.small (243), animal.wild (185), body.eye (223), body.mouth_throat (278), colour.colours (101), craft.clay (34), craft.coating (76), craft.dyeing (70), craft.leather (130), craft.weaving (149), craft.wood (84), divine.lordship (443), dress.adornment (176), drink.wine (52), dwelling.furnishing (135), dwelling.hearth (68), dwelling.settlement (245), dwelling.tent_camp (56), emotion.anger (177), emotion.fear (235), emotion.love (413), emotion.pride (265), fire.heat (63), fire.kindling (63), food.eating (193), food.sweet_fat (155), horse.charge_raid (48), horse.horsemanship (263), hunt.chase (110), hunt.trap (43), kin.birth_nursing (378), kin.household (216), kin.marriage (196), kin.orphan (75), know.divination (43), land.cave_pit (80), land.desert_sand (202), land.mountain (187), land.stone (76), land.valley (98), law.boundary (213), law.reckoning (155), life.death (274), life.growing_up (121), life.rising (64), light.light_dark (145), moral.good_evil (465), moral.guidance_error (146), moral.truth_falsehood (317), motion.pace (252), motion.turning (197), motion.up_down (182), new.ability_to_act (5), new.abstract_simplicity (4), new.acceptance (11), new.action_commencement (9), new.action_restraint (2), new.adjacent_dwellings (2), new.adversity (59), new.afterlife (9), new.agreement (5), new.animal_kinds (6), new.appointment (9), new.approximation (2), new.aversion (5), new.being_occurrence (32), new.body_sex (8), new.brain_anatomy (7), new.carrying_delivery (13), new.conduct_manner (13), new.contest (5), new.conviction (2), new.country_region (8), new.created_world (29), new.creature_sequence (8), new.custom_habit (6), new.deliberation (5), new.ear_anatomy (7), new.efficacy (17), new.female_anatomy (3), new.ghoul (6), new.grammar (9), new.grammar_case (2), new.grammar_particle (6), new.grammatical_particle (21), new.hair_grooming (4), new.handover (4), new.hardship (3), new.human_blemish (6), new.human_intercourse (3), new.imitation (13), new.indirect_speech (2), new.intentional_action (13), new.magic_charm (13), new.major_event (10), new.making (9), new.mind_deliberation (4), new.music_performance (7), new.mutual_consent (5), new.mutual_shirking (2), new.negative_scope (5), new.position_front_surface (3), new.proximity (5), new.search_pursuit (3), new.self_prompting (5), new.sequence_order (9), new.sexual_intercourse (13), new.sexual_relations (3), new.skilled_craft (15), new.sleep (5), new.sleep_state (3), new.social_disavowal (31), new.social_encounter (4), new.softness_comfort (10), new.solitude (5), new.sorcery (4), new.spatial_front (6), new.spatial_position (32), new.spatial_proximity (2), new.speech_impediment (4), new.state_existence (5), new.state_selfhood (3), new.suitability (9), new.task_preparation (17), new.unity (5), new.use_application (12), new.visitation_contest (13), new.volition (32), new.wrestling (13), pastoral.animal_care (144), pastoral.breeding (264), pastoral.grazing (190), pastoral.herding (209), pastoral.livestock_wealth (370), pastoral.milking (156), pastoral.watering_herd (102), plant.desert (101), position.middle (99), posture.leaning (96), posture.upright (89), quantity.full_empty (86), race.horse_race (80), ritual.idols_lots (262), ritual.prayer (337), ritual.purity (62), ritual.sacrifice (46), ritual.sanctuary (142), rule.covenant (412), rule.kingship (238), rule.leadership (278), rule.obedience (475), rule.ownership (274), sign.counting (115), sign.marking (230), sign.writing (133), sky.bodies (201), speech.news (330), speech.poetry (217), speech.praise_blame (313), speech.recitation (207), speech.secret (116), time.day_night (215), tool.rope (164), trade.debt (145), trade.gift (286), trade.hire (54), trade.measure (154), trade.sale (450), travel.departure_return (278), travel.night (46), travel.open_land (97), travel.sea (46), war.protection (274), war.vengeance (79), water.gathered (179), water.irrigation (44), water.rain_cloud (284), water.sea (105), water.spring_stream (331), water.thirst_drinking (121), water.washing (46), water.well (224), weather.season (99), weather.wind (133)

## Variant readings

5:2:6 شَعَٰٓئِرَ → تُحِلُّوا۟ (tuḥillū; Vr; mutawatir) Standard Hafs reading: Form IV jussive of ḥ-l-l
5:2:29 شَنَـَٔانُ → وَرُضْوَانًا (wa-ruḍwānan; vw; mutawatir) Canonical variant with ḍamma on rā' instead of kasra
5:2:38 وَتَعَاوَنُوا۟ → شَنْآنُ (shanʾānu; skn; mutawatir) Canonical variant with sukūn on nūn
5:2:40 ٱلْبِرِّ → إِنْ (in; in↔an; mutawatir) Canonical variant reading in (conditional: if they barred you) rather than an (that they b
5:3:3 ٱلْمَيْتَةُ → الْمَيِّتَةُ (al-mayyitatu; Gm; mutawatir) The geminated form mayyitah intensifies the quality of death
5:3:53 فِى → وَاخْشَوْنِ(ي) (wa-khshawnī(y); Vr; mutawatir) The Ten include the yāʾ suffix: wa-khshawnīy instead of wa-khshawnī. This adds a full pron
5:5:18 مِنَ → وَالْمُحْصِنَاتُ (wa-l-muḥṣinātu; Pss; mutawatir) Active participle variant: muḥṣināt (women who fortify themselves) vs muḥṣanāt (women who 
5:5:22 مِن → وَالْمُحْصِنَاتُ (wa-l-muḥṣinātu; Pss; mutawatir) Same variant as word 17: active vs passive participle
5:6:21 فَٱطَّهَّرُوا۟ → وَأَرْجُلِكُمْ (wa-arjulikum; CE; mutawatir) Genitive reading (jarr) links feet to the wiping (wa-msaḥū) rather than washing
5:6:44 بِوُجُوهِكُمْ → لَمَسْتُمُ (lamastumu; Vr; mutawatir) Form I instead of Form III
5:8:6 لِلَّهِ → قَوَّامِينَ (qawwāmīna; —; mutawatir) No recorded variants; the intensive faʿʿāl pattern is stable across all readings
5:8:15 تَعْدِلُوا۟ → شَنْآنُ (shanʾānu; skn; mutawatir) Canonical variant with sukūn on the nūn (shanʾān instead of shanaʾān)

## Paths you may read

- classical entries per root: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/entries/<root letters without spaces>.md
- every use of a frequent lemma: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/kwic/
- the Quran text: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/quran.tsv; words: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/words.tsv; lemma index: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/lemmas.tsv
- the whole dictionary: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/branches.tsv
