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
- Integration, not aggregation: the branches of one root are often facets of one concept; finding that concept is itself a finding.
- Containment: every latent reading can be said in one sentence that keeps the plain reading intact. Never "not X but Y".
- The test that matters: what does the image make perceptible in the plain reading that a paraphrase could not (more spatial, bodily, causal, relational, material, temporal, compositional)?
- Readings coexist. Never declare one correct.

## What you have (below the line)

1. The text of the window.
2. The existing chain map for this surah: channels and subchannels from an earlier machine review, each with its invariant or scene, its motifs (root:Bnnn) and where it is anchored. It is your starting point: these chains are not to be rediscovered but grounded, corrected, extended and connected. It is unranked and partly noisy. (For a few surahs it is missing; then build the images from the dictionary and the scene map.)
3. The words of the window with roots, lemmas and parts of speech.
4. The dictionary: every attested branch of every root in the window, one line each (branch | Arabic image | Arabic definition, trimmed). Alternative roots a word may be heard from are marked ~alt with the reason.
5. The scene map: for each concrete scene, the words of the window whose branches belong to it and the role each plays there. Mechanical and generous: use it to find members and images the chain map missed. It is not a worklist; lines it lists need not mean anything.
6. For passages of long surahs: scene lines that run across the whole surah and touch this window.
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

# Window 1:1–7 (whole surah)

## Text

1:1| بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
1:2| ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
1:3| ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
1:4| مَٰلِكِ يَوْمِ ٱلدِّينِ
1:5| إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
1:6| ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
1:7| صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

## Existing chain map (earlier machine review; the starting point: ground, correct, extend, connect; unranked, partly noisy)

### 1. Devotional Dependence and Rule
invariant: A dependent community turns toward a sovereign divine addressee through worship, service, obedience, and petition.
- Subchannel A. Worship and Obedient Submission: Worshippers direct humble obedience to the one recognized as deity and organizing religious authority. | motifs: ء ل ه:B001, د ي ن:B001, ع ب د:B003 | at 1:1, 1:2, 1:4, 1:5
- Subchannel B. Sovereignty, Ownership, and Service: A lord and king possesses a domain, governs it, and stands over dependents whose service ranges from honored attendance to enslavement. | motifs: ر ب ب:B001, م ل ك:B003, م ل ك:B002, ع ب د:B001, د ي ن:B004, ع ب د:B006 | at 1:2, 1:4, 1:5
- Subchannel C. Petition for Aid and Direction: Dependents seek assistance and gentle direction toward an upright path, with compassionate benefaction as the answering function. | motifs: ع و ن:B001, ه د ي:B001, ص ر ط:B001, ق و م:B008, ر ح م:B001 | at 1:1, 1:3, 1:5, 1:6, 1:7

### 2. Benefaction, Welfare, and Praise
invariant: Good is conferred through compassion and maintenance, stabilized as welfare, and answered by praise or recognition.
- Subchannel A. Compassionate Provision and Nurture: A caregiver feels tenderness, nurtures a dependent over time, guards its affairs, and supplies or repairs what sustains a good condition. | motifs: ر ح م:B001, ن ع م:B001, ر ب ب:B002, ق و م:B004, غ ي ر:B001, ع و ن:B001 | at 1:1, 1:3, 1:2, 1:5, 1:6, 1:7
- Subchannel B. Patronage, Support, and Claimed Recognition: A patron supplies aid and the mainstay of another's life, then may present that support as a favor deserving praise. | motifs: ع و ن:B001, م ل ك:B005, ق و م:B009, ن ع م:B001, ر ب ب:B016, ح م د:B005 | at 1:2, 1:4, 1:5, 1:6, 1:7
- Subchannel C. Knowing and Articulating the Praiseworthy: Knowledge discerns a benefit or admirable quality and renders that recognition as praise, approval, or an honored name. | motifs: ح م د:B001, ع ل م:B001, ر ب ب:B003, ح م د:B003, ن ع م:B003 | at 1:2, 1:7

### 3. Declared Identity and Public Presence
invariant: Names, utterances, reputation, and bearing make identity or commitment socially legible.
- Subchannel A. Naming, Invocation, and Direct Address: A speaker identifies the addressee by name and turns that name into invocation, oath, or direct appeal. | motifs: س م و:B005, ء ل ه:B002 | at 1:1, 1:2
- Subchannel B. Assent, Certification, and Qualification: An utterance confirms a claim, delegates judgment, or narrows it through difference, exception, negation, and approximation. | motifs: ن ع م:B004, د ي ن:B007, غ ي ر:B005, ر ب ب:B015 | at 1:2, 1:4, 1:7
- Subchannel C. Reputation and Poetic Exchange: Public speech circulates praise or blame until it becomes a person's audible reputation and social eminence. | motifs: س م و:B008, س م و:B001, ه د ي:B011, ح م د:B003, ح م د:B005 | at 1:1, 1:2, 1:6
- Subchannel D. The Reputed Captain's Ceremonial Bearing: A maritime captain appears as a composed, publicly reputed leader whose station is marked by ceremonial scent. | motifs: ر ب ب:B017, ع ب د:B012, ه د ي:B010, س م و:B008, س م و:B002 | at 1:1, 1:2, 1:5, 1:6

### 4. Orientation, Passage, and Breakdown
invariant: Movement is organized by a course, a guide, and a state of passage, then tested by deviation, engulfment, or loss of mobility.
- Subchannel A. The Marked and Straight Route: A traveler receives guidance, reads landmarks, enters the center of a prepared road, and maintains a straight course that can also become an established manner of conduct. | motifs: ه د ي:B001, ه د ي:B002, ص ر ط:B001, ق و م:B008, ع ل م:B002, م ل ك:B006, ع ب د:B005, د ي ن:B005 | at 1:2, 1:4, 1:5, 1:6, 1:7
- Subchannel B. The Visible Leader at the Front: A conspicuous leader takes the foremost position and draws a herd or procession behind it. | motifs: ه د ي:B003, م ل ك:B008, س م و:B002, ر ب ب:B014, ع و ن:B006 | at 1:1, 1:2, 1:4, 1:5, 1:6
- Subchannel C. Engulfing and Penetrating Passage: An entity enters, cuts through, or is swallowed by another body or medium until it becomes hidden. | motifs: ص ر ط:B002, ض ل ل:B002, س م و:B003, ص ر ط:B003 | at 1:1, 1:6, 1:7
- Subchannel D. Halted, Supported, and Recovered Movement: A moving body weakens or stops, relies on external support, and may recover enough strength to resume at a different pace. | motifs: ع ب د:B011, ق و م:B016, ه د ي:B008, ع و ن:B005, ع ب د:B009 | at 1:5, 1:6
- Subchannel E. Disorientation, Forgetting, and the Stray: A traveler, object, memory, or animal loses its intended relation to a route, owner, or knower. | motifs: ض ل ل:B001, ض ل ل:B003, ض ل ل:B004, ض ل ل:B005, ه د ي:B009 | at 1:6, 1:7

### 5. Time, Measure, and Final Reckoning
invariant: Time is made intelligible by bounded spans and celestial positions, by pace within a duration, and by a culminating event of judgment.
- Subchannel A. Daylight, Zenith, and Celestial Marking: A daylight span is located by the sun at zenith and by visible signs in the overhead sky. | motifs: ي و م:B001, ق و م:B017, س م و:B004, ن ع م:B007, ع ل م:B002 | at 1:1, 1:2, 1:4, 1:6, 1:7
- Subchannel B. Duration, Pace, and Praised Attainment: An actor inhabits a duration, varies between delay and haste, intensifies effort, and reaches a praiseworthy limit without losing composure. | motifs: ي و م:B002, ع ب د:B009, ن ع م:B010, ح م د:B004, ه د ي:B010, ر ب ب:B007 | at 1:2, 1:4, 1:5, 1:6, 1:7
- Subchannel C. The Momentous Day of Rising and Account: A climactic event arrives, creation rises, and a sovereign conducts judgment, accounting, and recompense. | motifs: ي و م:B003, ق و م:B013, د ي ن:B002, م ل ك:B003 | at 1:4, 1:6

### 6. Property, Measure, and Legitimate Transfer
invariant: Goods and obligations move between parties through ownership, valuation, replacement, compensation, gift, or offering.
- Subchannel A. Credit, Price, and Livestock Property: Livestock is owned, priced, sold on credit, and monitored for loss within an active market. | motifs: د ي ن:B003, ق و م:B010, ق و م:B015, ق و م:B018, م ل ك:B002, ن ع م:B005, ض ل ل:B005, ع و ن:B002 | at 1:4, 1:5, 1:6, 1:7
- Subchannel B. Replacement, Indemnity, and Redress: A lost or injured claim is answered by a substitute, transfer, or assessed compensation rather than remaining without redress. | motifs: غ ي ر:B002, غ ي ر:B003, ق و م:B007, ض ل ل:B003, د ي ن:B002, م ل ك:B002 | at 1:4, 1:6, 1:7
- Subchannel C. Reciprocal Gift and Beneficent Transfer: A gift moves toward a valued recipient as an expression of affection, mercy, or benefit. | motifs: ه د ي:B004, ن ع م:B001, ر ح م:B001, م ل ك:B002 | at 1:1, 1:3, 1:4, 1:6, 1:7
- Subchannel D. Consecrated Offering: Livestock or goods are selected from owned wealth and directed toward the sanctuary as an act of worship. | motifs: ه د ي:B005, ن ع م:B005, ء ل ه:B001, ع ب د:B003 | at 1:1, 1:2, 1:5, 1:6, 1:7

### 7. Household Continuity and Protected Belonging
invariant: Kinship is produced and maintained through gestation, nurture, marriage, covenant, and defense of household boundaries.
- Subchannel A. Kinship, Fosterage, and Continuing Care: A child belongs to a network of blood and acquired kin whose caregiver assumes responsibility for nurture and continuity. | motifs: ر ح م:B002, ر ب ب:B005, ر ب ب:B002, ق و م:B004 | at 1:1, 1:3, 1:2, 1:6
- Subchannel B. Gestation, Recent Birth, and Postpartum Vulnerability: The womb contains developing offspring, birth produces a newly delivered mother and new life, and the postpartum body remains vulnerable to pain or retained afterbirth. | motifs: ر ح م:B003, ر ب ب:B009, ر ح م:B004 | at 1:1, 1:3, 1:2
- Subchannel C. Marriage and Bride-Conveyance: A marriage contract establishes a new household relation and the bride is formally conveyed to her spouse, accompanied by affectionate transfer. | motifs: م ل ك:B004, ه د ي:B006, ر ح م:B002, ه د ي:B004 | at 1:1, 1:3, 1:4, 1:6
- Subchannel D. Covenant, Refuge, and Legal Protection: A named outsider or dependent receives protected standing through covenant, certification, and a rule of compensatory redress. | motifs: ر ب ب:B011, ه د ي:B007, د ي ن:B007, غ ي ر:B002, س م و:B005 | at 1:1, 1:2, 1:4, 1:6, 1:7
- Subchannel E. Protective Jealousy and Household Defense: Attachment to household and kin activates vigilance, bodily firmness, and visible anger against intrusion. | motifs: غ ي ر:B004, غ ض ب:B007, ع ب د:B007, ق و م:B001, ر ح م:B002 | at 1:1, 1:3, 1:5, 1:6, 1:7

### 8. Herd Formation, Wildlife, and Dispersal
invariant: Animal life is organized by gathering, classification, reproduction, leadership, pursuit, and scattering.
- Subchannel A. Herd, Livestock, and the Stray Margin: Domestic and wild animals gather into recognizable herds, are classified and led, and can fall outside the group as ownerless strays. | motifs: ر ب ب:B014, ع و ن:B006, ن ع م:B005, ع و ن:B002, م ل ك:B008, ض ل ل:B005 | at 1:2, 1:4, 1:5, 1:7
- Subchannel B. Hunt, Flight, and Scattered Routes: Hunters set out, the pursued group takes flight, and a once-coherent body disperses into people, animals, or routes going in different directions. | motifs: س م و:B006, ن ع م:B008, ع ب د:B010, ق و م:B001, ض ل ل:B003 | at 1:1, 1:5, 1:6, 1:7
- Subchannel C. Wildlife Generation and Exposure: New animal life emerges from reproductive enclosure into an open field populated by birds, herd animals, and predators. | motifs: ر ح م:B003, ن ع م:B006, ع ل م:B006, ع ل م:B007, ر ب ب:B009, ض ل ل:B005 | at 1:1, 1:3, 1:2, 1:7

### 9. Habitation, Water, and the Living Landscape
invariant: Habitation becomes viable when authority, residence, water, weather, and vegetation converge into a sustaining place.
- Subchannel A. Governed and Pleasant Settlement: A community establishes residence in a governed place, finds the site suitable, and remains there. | motifs: د ي ن:B006, ق و م:B006, ع و ن:B008, ن ع م:B011, ح م د:B002, ر ب ب:B007 | at 1:2, 1:4, 1:5, 1:6, 1:7
- Subchannel B. Water-Secured Encampment and Livelihood: A community locates abundant collected water, controls its encampment through that resource, and sustains livelihood by storing and distributing it. | motifs: ر ب ب:B013, ع ل م:B005, م ل ك:B007, ق و م:B009, غ ي ر:B001 | at 1:2, 1:4, 1:6, 1:7
- Subchannel C. Sky, Rain, Wind, and Enduring Growth: The overhead sky forms layered rainclouds, weather persists, a gentle southern wind moves through, and watered vegetation remains green. | motifs: س م و:B004, ر ب ب:B008, ر ب ب:B007, ن ع م:B009, ر ب ب:B012, ع و ن:B004, غ ي ر:B001 | at 1:1, 1:2, 1:5, 1:7

### 10. Structural Support and Working Materials
invariant: Stability is produced by cohesive material, load-bearing members, mechanical parts, and treatments that bind, coat, or repair.
- Subchannel A. Cohesion, Mainstay, and Upright Members: A structure or undertaking remains standing because material cohesion, a firm joint, and upright supporting members carry its load. | motifs: م ل ك:B001, م ل ك:B005, ق و م:B009, ق و م:B012, ر ب ب:B016, ع ب د:B007 | at 1:2, 1:4, 1:5, 1:6
- Subchannel B. Well and Water-Lifting Assembly: An upright timber and working components are arranged over a water source so a settlement can draw and control water. | motifs: ن ع م:B007, ق و م:B012, ع ل م:B005, ر ب ب:B013, م ل ك:B007 | at 1:2, 1:4, 1:6, 1:7
- Subchannel C. Thickening, Coating, and Repair: A thick material is worked to cohesion, applied as a coating or preservative, and used to repair containers, food, medicine, or transport surfaces. | motifs: ر ب ب:B006, م ل ك:B001, ع ب د:B005, غ ي ر:B001, ن ع م:B002 | at 1:2, 1:4, 1:5, 1:7

### 11. Bodily Integrity, Posture, and Injury
invariant: A living body is read through stance, proportion, strength, visible markers, pain, and loss of function.
- Subchannel A. Upright Stature and Balanced Strength: A body rises upright, displays proportion and firmness, and sustains its posture through balanced mature strength. | motifs: ق و م:B002, ق و م:B011, ع ب د:B007, ع و ن:B005, م ل ك:B001, غ ض ب:B005 | at 1:4, 1:5, 1:6, 1:7
- Subchannel B. Lesion, Swelling, and Localized Pain: A specific body part bears a visible lesion or swelling and becomes the site of persistent pain. | motifs: ع ل م:B004, غ ض ب:B006, ق و م:B019, ر ح م:B004 | at 1:1, 1:3, 1:2, 1:6, 1:7
- Subchannel C. Preserved Appearance with Failed Function: A body or limb remains visibly present yet fails in sight, gait, strength, or forward movement. | motifs: ق و م:B021, ق و م:B020, ه د ي:B009, ع ب د:B011, ن ع م:B013, غ ض ب:B006 | at 1:5, 1:6, 1:7
- Subchannel D. Bodily Markers of Maturity and Reproduction: Bodily marks, sexual maturity, reproductive capacity, and age make a living body classifiable. | motifs: ع و ن:B007, ر ح م:B003, ع و ن:B002, ع و ن:B005, ع ل م:B002 | at 1:1, 1:3, 1:2, 1:5

### 12. Conflict, Anger, and Defensive Order
invariant: Opposition escalates through rivalry and anger into combat, retaliation, defense, defeat, or compensatory settlement.
- Subchannel A. Rivalry, Resistance, and Repeated War: Competitors seek superiority, rise against one another, and turn repeated opposition into organized combat. | motifs: س م و:B007, ع و ن:B003, ق و م:B014, غ ض ب:B003, ق و م:B003, ح م د:B003 | at 1:1, 1:2, 1:5, 1:6, 1:7
- Subchannel B. Anger, Mourning, Vengeance, and Redress: Injury or loss provokes anger and grief, which can seek retaliatory vengeance or be redirected into compensatory settlement. | motifs: غ ض ب:B001, ع ب د:B008, غ ض ب:B002, ض ل ل:B003, غ ي ر:B002 | at 1:5, 1:7
- Subchannel C. Rout and Collective Dispersal: A group under pressure loses formation, turns away, and scatters along divergent routes. | motifs: ن ع م:B008, ع ب د:B010, ض ل ل:B003, ق و م:B014, س م و:B006 | at 1:1, 1:5, 1:6, 1:7
- Subchannel D. Hardness, Shielding, and the Cutting Edge: A defender combines bodily strength with hard natural or worked material to resist a penetrating blade. | motifs: غ ض ب:B008, ص ر ط:B003, غ ض ب:B004, ع ب د:B007 | at 1:5, 1:6, 1:7

### standalone: S1. The Divinatory Arrow Vessel
- scene: A leather container gathers and preserves a set of lot or gaming arrows as one portable object assembly. | motifs: ر ب ب:B010 | at 1:2

## Words (ref surface | root | lemma | pos)

1:1:1 بِسْمِ | س م و | ٱسْم | N
1:1:2 ٱللَّهِ | ء ل ه | ٱللَّه | PN
1:1:3 ٱلرَّحْمَٰنِ | ر ح م | رَّحْمَٰن | ADJ
1:1:4 ٱلرَّحِيمِ | ر ح م | رَّحِيم | ADJ
1:2:1 ٱلْحَمْدُ | ح م د | حَمْد | N
1:2:2 لِلَّهِ | ء ل ه | ٱللَّه | PN
1:2:3 رَبِّ | ر ب ب | رَبّ | N
1:2:4 ٱلْعَٰلَمِينَ | ع ل م | عَٰلَمِين | N
1:3:1 ٱلرَّحْمَٰنِ | ر ح م | رَّحْمَٰن | ADJ
1:3:2 ٱلرَّحِيمِ | ر ح م | رَّحِيم | ADJ
1:4:1 مَٰلِكِ | م ل ك | مَٰلِك | N
1:4:2 يَوْمِ | ي و م | يَوْم | N
1:4:3 ٱلدِّينِ | د ي ن | دِين | N
1:5:2 نَعْبُدُ | ع ب د | عَبَدَ | V
1:5:4 نَسْتَعِينُ | ع و ن | ٱسْتَعِينُ | V
1:6:1 ٱهْدِنَا | ه د ي | هَدَى | V
1:6:2 ٱلصِّرَٰطَ | ص ر ط | صِرَٰط | N
1:6:3 ٱلْمُسْتَقِيمَ | ق و م | مُّسْتَقِيم | ADJ
1:7:1 صِرَٰطَ | ص ر ط | صِرَٰط | N
1:7:3 أَنْعَمْتَ | ن ع م | أَنْعَمَ | V
1:7:5 غَيْرِ | غ ي ر | غَيْر | N
1:7:6 ٱلْمَغْضُوبِ | غ ض ب | مَغْضُوب | N
1:7:9 ٱلضَّآلِّينَ | ض ل ل | ضَآلّ | N

## Dictionary: every branch of every root (branch | image | definition)

### س م و — 381 uses; here: 1:1:1 بِسْمِ
B001 | العلو والارتفاع | سمو الشيء وعلوه، وارتفاع البصر، وعلو الحسيب والشريف، ورفعة الذكر.
B002 | الشخص المرتفع الظاهر | الشيء أو الشخص الذي يرتفع فيلوح من بعيد، وسماوة الهلال أو كل شيء بمعنى شخصه العالي الظاهر.
B003 | تطاول الفحل على الشول | سما الفحل إذا تطاول أو سطا على شوله، أي علاها وتخللها.
B004 | السماء وما علا فأظل | السماء لما علا وأظل، والسقف، والسحاب، والمطر، والنبات المنسوب إلى المطر، وظهر الفرس أو أعلى الشيء.
B005 | الاسم تنويه ودلالة | الاسم والتسمية والتسمي والأسامي، والسمي بمعنى الموافق في الاسم أو النظير المستحق للاسم.
B006 | الخروج للصيد | سما القوم أو استموا إذا خرجوا للصيد، والسماة الصيادون، وما لحق بذلك من طلب الوحش وآلة الصياد.
B007 | المساماة والمباراة | تسامى القوم إذا تباروا، والمساماة بمعنى المفاخرة والمباراة والمعارضة، ومن لا يسامى إذا لا يقدر على …
B008 | الصيت الحسن المنتشر | سماه بمعنى صوته أو صيته في الخير لا في الشر.

### و س م ~alt (documented alternative analysis) — 2 uses; here: 1:1:1 بِسْمِ
B001 | أثر وسم ظاهر يجعل الشيء معروفا | وسم الشيء أو الدابة بسمة أو كي أو قطع أذن، والميسم أو المكواة، وكل علامة حسية للتعريف أو التمييز.
B002 | سمة يرى بها الناظر دلالة الحال | التوسم والتفرس، ورؤية أثر الخير أو الشر في الشخص، والآيات للمتوسمين بوصفهم ناظرين في السمة الدالة.
B003 | مطر أول يسم الأرض بالنبات | الوسمي، وهو المطر الأول أو مطر أول السنة أو الربيع الأول، وتسميته لأنه يسم الأرض بالنبات، والأرض …
B004 | موسم معلم يجتمع إليه الناس | موسم الحج ومواسم أسواق العرب، والمجمع أو الوقت المعلم الذي يجتمع إليه الناس، ووسم الناس بمعنى شهدوا …
B005 | حسن عليه أثر الجمال | الوسامة، والوسيم والوسيمة، وذات ميسم، أي الحسن أو أثر الجمال والعتق الظاهر على الشخص.
B006 | وسمة يخضب بورقها | الوسم أو الوسمة اسم شجرة أو نبات ورقه خضاب، والعظلم الذي يختضب به.

### ء ل ه — 2851 uses; here: 1:1:2 ٱللَّهِ; 1:2:2 لِلَّهِ
B001 | التعبد والمعبود | أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.
B002 | اسم الله في القسم والنداء | اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه …

### و ل ه ~alt (documented alternative analysis) — 0 uses; here: 1:1:2 ٱللَّهِ; 1:2:2 لِلَّهِ
B001 | الوَلَه والحيرة | ذهاب العقل أو اضطرابه من شدة الوجد، والحيرة، والحنين إلى المفقود أو المحبوب في الرجل والمرأة …
B002 | تَوْلِيه الوالدة عن ولدها | التوليه المتعدي: التفريق بين المرأة أو الوالدة وولدها حتى تصير والهة، وخاصة في البيع أو السبي
B003 | ماء مُولَه ذاهب | الماء أو العين إذا أرسل ماؤها في الصحراء فذهب
B004 | المُولَه العنكبوت | اسم المُولَه للعنكبوت كما في رواية الصحاح

### ر ح م — 339 uses; here: 1:1:3 ٱلرَّحْمَٰنِ; 1:1:4 ٱلرَّحِيمِ; 1:3:1 ٱلرَّحْمَٰنِ; 1:3:2 ٱلرَّحِيمِ
B001 | الرَّحْمَة والرقة | الرقة والعطف والرأفة والإحسان إلى المرحوم والمرحمة والتراحم والترحم وأسماء الرحمن والرحيم من جهة …
B002 | الرَّحِم والقرابة | الرَّحِم بمعنى القرابة القريبة وأسباب النسب وصلة الرحم وقطعها والأرحام.
B003 | رَحِم الأنثى | رَحِم المرأة أو الأنثى بوصفه بيت منبت الولد ووعاءه في البطن.
B004 | وجع الرَّحِم بعد الولادة | الرحوم والراحم والرواحم وما قيل في الناقة أو الشاة أو المرأة إذا اشتكت رحمها أو أصابه داء أو ورم أو …

### ح م د — 63 uses; here: 1:2:1 ٱلْحَمْدُ
B001 | الحمد خلاف الذم | الحمد والثناء على الفعل المحمود والشكر على النعمة وكثرة حمد الله
B002 | وجود الشيء محمودا | إيجاد الشخص أو الموضع محمودا مرضيا بعد تجربة وسؤال الرضا للأمر
B003 | المحمود كثير الخصال | الوصف أو الاسم لمن حمد أو كثرت خصاله المحمودة مثل محمود ومحمد وأحمد وحميد
B004 | حماداك الغاية المحمودة | صيغة حماداك وحماديات في معنى الغاية والقصارى وما يحمد بلوغه
B005 | يتحمد بالمنة | التحمد على الناس بمعنى المن وطلب الحمد على الإحسان أو الإنفاق
B006 | أحمد إليك الله | صيغة أحمد إليك الله ونحوها في حمد الله مع المخاطب أو شكر أياديه

### ر ب ب — 980 uses; here: 1:2:3 رَبِّ
B001 | ربوبية وملك وسيادة | الرب بمعنى الله تعالى، ومالك الشيء، وسيده المطاع، وصاحبه، ورب الدار والدابة والملك
B002 | إصلاح وتربية وإتمام | رب الشيء إذا أصلحه وأتمه وقام عليه، ورب النعمة والصنيعة والضيعة والولد والصبي، والتربية حالا فحالا
B003 | علم رباني | الرباني والربانيون بمعنى العلماء والحكماء وأهل العلم بالرب أو من يرب العلم ونفسه به
B004 | ربة وجماعات كثيرة | الربة والجماعات الكثيرة، والربيون إذا فسروا بالألوف أو الجماعات، ورباب القبائل لاجتماعهم
B005 | ربيب وربيبة ورابة | الربيب والربيبة للولد المربوب من زوج سابق، والراب والرابة لمن يقوم على أمره، والحاضنة
B006 | رُبّ خاثر وإصلاح به | الرُّبّ الطلاء الخاثر أو ثفل السمن والزيت، والسقاء والنحي والأديم والدواء والطعام إذا جعل فيه …
B007 | لزوم وإقامة ودوام | رب أو أرب بالمكان إذا أقام، ومرب الإبل ومرابها، وأربت السحابة أو الجنوب إذا دامت، والإرباب بمعنى …
B008 | رباب السحاب | الرباب والربابة للسحاب، والسحاب المتعلق أو المركب بعضه على بعض، وما سمي بذلك لتربية النبات أو دوام …
B009 | شاة رُبّى وحداثة | الشاة الرُّبّى والرباب لقرب العهد بالولادة أو لزوم البيت للبن، وربان الشيء بمعنى حدثانه وطراءته، …
B010 | ربابة تجمع القداح | الربابة للجلدة أو الوعاء الذي تجمع فيه القداح أو سهام الميسر، وجماعة السهام نفسها
B011 | ربابة عهد وميثاق | الربابة والرباب للعهد والميثاق والجوار، والأربة للمعاهدين، والرباب للعشور إذا جعل كالعهد
B012 | ربة نبات | الربة والربب لضرب من الشجر أو النبت أو البقلة التي تبقى خضراء
B013 | ماء رَبَب كثير | الربب للماء الكثير، ويقال للعذب، من جهة اجتماع الماء
B014 | رَبْرَب قطيع | الربرب لقطيع بقر الوحش، وقيل لجماعة البقر أو الإبل
B015 | حرف رب وربما | رب وربما وربت وربه كحرف خافض أو حرف معنى للتقليل، ودخول ما أو التاء أو الهاء عليه
B016 | رُبَى حاجة وعقدة ونعمة | الربى بمعنى الحاجة، والرابة، والعقدة المحكمة، والنعمة والإحسان
B017 | رباني الملاحين | الرباني لرئيس الملاحين

### ع ل م — 854 uses; here: 1:2:4 ٱلْعَٰلَمِينَ
B001 | انكشاف الشيء للعارف | العلم نقيض الجهل وإدراك الشيء ومعرفته والشعور بالخبر والتعلم والتعليم والإعلام والمغالبة بالعلم
B002 | أثر يميز الشيء ويهدي إليه | العلامة والعلم والراية والجبل والمعلم ومعالم الطريق والحدود وعلم الثوب ورقمه وتعليم الفارس والثوب …
B003 | الخلق عالم يدل على صانعه | العالم والعالمون بمعنى الخلق أو أصناف الخلائق أو كل جنس من الخلق لأنه معلم في نفسه ودال
B004 | شق ظاهر في الشفة العليا | العلم والشق في الشفة العليا ووصف الرجل أو البعير بالأعلم إذا كان الشق أو العلم في الموضع الأعلى
B005 | ماء كثير مجتمع في عيلم | العيلم بمعنى البحر أو البئر الكثيرة الماء
B006 | طائر جارح يسمى العلام | العلام بمعنى الصقر أو الباشق وما نسب إليه من العلامي
B007 | ذكر الضباع يسمى العيلام | العيلام بمعنى ذكر الضباع

### م ل ك — 206 uses; here: 1:4:1 مَٰلِكِ
B001 | قوة الشيء وتماسكه | شد العجين وإحكام عجنه؛ تقوية الشيء؛ صلابة النبعة؛ التماسك الذي يقوم به الجدار أو النفس
B002 | المِلْك والتصرف | ملك الشيء والمال وما ملكت اليد؛ جعل الشيء ملكا لغيره؛ المملوك والعبد وملك اليمين؛ حسن الملكة إلى …
B003 | المُلك والسلطان | المَلِك والملوك؛ المُلك والسلطان والعز؛ ملك الناس وسياسة الرعية؛ المملكة؛ الملكوت وخاصة ملك الله
B004 | الإملاك والتزويج | عقد التزويج والإملاك؛ شهدنا إملاك فلان؛ ملك الرجل المرأة بمعنى تزوجها
B005 | مِلاك الأمر وعِماده | ما يقوم به الأمر ويعتمد عليه؛ القلب ملاك الجسد
B006 | مَلَك الطريق والوادي | وسط الطريق أو الوادي وحده ومعظمه؛ موضع يجتنب أو يلزم بحسب التعبير
B007 | الماء مَلَك الأمر | الماء الذي به يملك المسافر أو القوم أمرهم؛ المياه التي يقوم بها النزول والمعيشة
B008 | المتقدم القائد في الحيوان | يعسوب النحل؛ هادي الدابة وقوائمها؛ ما يتقدم الإبل والشاء ويتبعه سائره
B009 | المَلَك من الملائكة | لفظ المَلَك والملائكة الوارد في المصادر مع بيان أصله من الملأك والألوك والرسالة

### ي و م — 405 uses; here: 1:4:2 يَوْمِ
B001 | وقت النهار المحدود | اليوم المعروف: وقت من طلوع الشمس إلى غروبها، وهو الواحد من الأيام وجمعه أيام.
B002 | مدة من الزمان | اليوم بمعنى مدة من الزمان أي مدة كانت، أو بمعنى الدهر في بعض الاستعمال.
B003 | كائنة اليوم وشدته | استعارة اليوم للأمر العظيم، والكائنة إذا نزلت، واليوم الشديد، والأيام بمعنى الوقائع.
B004 | أيام النعم والوقائع الإلهية | أيام الله وما في معناها من أيام النعم والوقائع التي يذكر بها، من عفو أو نعمة أو عذاب نزل بقوم.
B005 | يوم مضاف إلى إذ | تركيب يوم مع إذ في يومئذ للدلالة على وقت مشار إليه في السياق، مع جواز الإعراب أو البناء بحسب …

### د ي ن — 101 uses; here: 1:4:3 ٱلدِّينِ
B001 | الطاعة والانقياد | الدين بمعنى الطاعة والانقياد والتعبد والملة والشريعة وما يتدين به
B002 | الحساب والجزاء | الدين بمعنى الحكم والحساب والجزاء والمكافأة والقضاء
B003 | الدين المالي | الدين المالي والقرض والاستقراض والمداينة والبيع إلى أجل وما يؤخذ أو يعطى دينا
B004 | الإذلال والملك | الإذلال والقهر والملك والاستعباد والحمل على المكروه والعبد المدين والأمة المدينة
B005 | العادة والشأن | الدين بمعنى العادة والشأن والحال المعهود والدأب
B006 | مدينة الطاعة | المدينة بمعنى المصر والموضع الذي تقام فيه طاعة ذوي الأمر
B007 | التصديق والتفويض | التديين بمعنى تصديق الرجل في القضاء أو الحلف أو تفويضه إلى دينه

### ع ب د — 275 uses; here: 1:5:2 نَعْبُدُ
B001 | الرق والملك | العبد المملوك وخلاف الحر ومن يصح بيعه وابتياعه وجموع العبيد والأعبد والعبدى والمعبدة
B002 | الانتساب إلى الله عبدا | إطلاق العبد على الإنسان حرا أو رقيقا منسوبا إلى الله وعلى الخلق عبيدا لله بالإيجاد وعلى جماعة عباد …
B003 | العبادة والطاعة الخاضعة | عبادة الله والتنسك والطاعة مع الخضوع والتوحيد وعبادة الطاغوت بمعنى طاعته والخضوع لملك أو دنيا
B004 | التعبيد والاستعباد | عبدت الرجل واستعبدته وأعبدته وتعبدت فلانا إذا اتخذته عبدا أو صيرته كالعبد أو ذللته حتى يعمل عمل …
B005 | التذليل والتسوية | الطريق المعبد المسلوك المذلل والبعير أو الجمل المعبد المهنوء بالقطران والسفينة المعبدة المقيرة
B006 | التكريم والتعظيم | المعبد بمعنى المكرم والمعظم والمخدوم
B007 | القوة والصلابة | العبدة بمعنى القوة والصلابة والشدة والبقاء والسمن في الناقة وقوة الثوب
B008 | الأنفة والغضب | العبد والعبدة بمعنى الأنفة والحمية والغضب والحزن والوجد والندم عند فوات الشيء
B009 | قلة اللبث وسرعة العدو | ما عبد أن فعل أي ما لبث وعبد يعدو إذا أسرع بعض الإسراع
B010 | التفرق في الوجوه | العباديد والعبابيد للفرق من الناس أو الأشياء أو الطرق المتفرقة الذاهبة في كل وجه
B011 | العطب والانقطاع | أعبد بفلان أو أعبد به بمعنى أبدع به إذا كلت راحلته أو عطبت أو ذهبت ويدخل فيه البعير المتعبد الممتنع …
B012 | صَلاءة الطيب | العبدة اسما لصَلاءة الطيب

### ع و ن — 11 uses; here: 1:5:4 نَسْتَعِينُ
B001 | الإعانة والمظاهرة | العون والمعونة والإعانة والاستعانة والتعاون والتظاهر على الأمر
B002 | العَوان بين السنين | العوان لما كان نصفا أو متوسطا في السن كالبقرة والمرأة والفرس
B003 | الحرب العَوان | الحرب العوان التي قوتل فيها مرة بعد مرة أو سبقتها حرب أولى
B004 | النخلة العَوانة القديمة | العوانة للنخلة القديمة
B005 | استواء الخلقة وتلاحق القوة | المتعاونة في المرأة أو البرذون إذا اعتدل الخلق أو لحقت القوة والسن
B006 | العانة قطيع الحمر | العانة للقطيع من حمر الوحش وجمعها عانات وعون
B007 | عانة الرجل | عانة الرجل للشعر النابت على فرجه وما يتصل بحلقه
B008 | النسبة إلى عانة | عانة موضع أو قرية وينسب إليها بالخمر العانية

### ه د ي — 316 uses; here: 1:6:1 ٱهْدِنَا
B001 | دلالة بلطف إلى الطريق والحق | الهدى والهداية بمعنى الرشاد والدلالة والبيان وتعريف الطريق أو الحق والدين والاهتداء والتوفيق الإلهي …
B002 | جهة الأمر وسيرته وقصده | هدي الأمر أو هديته بمعنى جهته ووجهته وقصده وسيرته وطريقته وسمته وما يلازم ذلك من لزوم الحديث أو …
B003 | المتقدم الهادي وأوائل الشيء | الهادي أو الهادية بمعنى أول الشيء وما تقدم منه كأعناق الخيل وأول رعيلها وأوائل الوحش ورقبة الشاة …
B004 | بعثة لطف وهدية إلى ذي مودة | الهدية والهدايا والإهداء بمعنى العطية اللطيفة إلى ذي مودة والتهادي بين الناس والمهدى الطبق والمهداء …
B005 | الهدي المهدى إلى الحرم | الهدي أو الهدي المشدد والمخفف بمعنى ما يهدى إلى مكة أو الحرم أو بيت الله من النعم أو المال أو …
B006 | العروس المهدية إلى زوجها | هديت المرأة أو العروس إلى زوجها وهداؤها وكونها مهدية أو هدي في معنى مفعول
B007 | هدي الحرمة والأسير | الهدي للرجل ذي الحرمة المستجير أو الآخذ عهدا قبل أن يجار وللأسير في بعض الأقوال
B008 | مشي التهادي مع الاعتماد والتمايل | يهادي بين اثنين إذا مشى معتمدا عليهما من ضعف وتمايل وتهادت المرأة إذا تمايلت في مشيتها ومشي النساء …
B009 | الهداء البليد الضعيف | الهداء أو الهدان للرجل البليد الضعيف أو الثقيل الوخم
B010 | هدي السكون وحسن الهيئة | الهدي بمعنى السكون وترك إسراع المنهزم مع حسن الهدي أو الهيئة
B011 | إهداء الشعر ومهاداته | إهداء المديح أو الهجاء شعرا إلى إنسان ومهاداته الشعر بمعنى مهاجاته

### ص ر ط — 45 uses; here: 1:6:2 ٱلصِّرَٰطَ; 1:7:1 صِرَٰطَ
B001 | الطريق المستقيم | الصراط والسراط والزراط بمعنى الطريق، وخاصة الطريق المستقيم
B002 | الغيبة في المرور والبلع | سرط الطعام بمعنى بلعه وغيبته في المرور، وما يتصل بسهولة الابتلاع وسعة الحلق
B003 | السيف القاطع الماضي في الضربة | إطلاق السراط على السيف القاطع النافذ الماضي في الضريبة

### س ر ط ~alt (reading sirāṭa (ibdāl)) — 0 uses; here: 1:6:2 ٱلصِّرَٰطَ; 1:7:1 صِرَٰطَ
B001 | ابتلاع يغيب في الحلق | سرط الطعام واسترطه وسرعة الابتلاع بلا مضغ ووصف الآكل السريع
B002 | طريق يسترط سالكه | السراط بمعنى الطريق الواضح أو المستسهل والمنهاج الواضح، ولغة السين في الصراط
B003 | حلوى تسترط | السرطراط والسرطراط للفالوذج، وما سمي بذلك لاستلذاذ أكله وإساغته
B004 | قطع يمضي في الضريبة | السراط أو السراطي للسيف القاطع والقطع
B005 | أخذ يبتلع وقضاء يدفع | مثل الأخذ سريطى أو سريط والقضاء ضريطى أو ضريط، في حب الأخذ وكراهة الإعطاء
B006 | حيوان ماء يسمى السرطان | السرطان من خلق الماء
B007 | برج السماء المسمى السرطان | السرطان برج في السماء أو من بروج السماء
B008 | داء يسمى السرطان | داء السرطان في قائمة الدابة أو رسغها، وما ذكر للإنسان في حلقه

### ق و م — 660 uses; here: 1:6:3 ٱلْمُسْتَقِيمَ
B001 | جماعة الناس والرجال | القوم بمعنى الرجال دون النساء في الأصل، وجماعة الرجل وشيعته وعشيرته، وقد تدخل النساء تبعا أو يستعار …
B002 | انتصاب وقيام بالبدن | قام قياما، والقومة مرة الانتصاب، والقيام في الصلاة أو الذكر، وقيام الشجر والنبت على أصله، ووقوف …
B003 | عزم ونهوض إلى الأمر | القيام بمعنى العزم على الشيء واعتناق الأمر والنهوض إليه
B004 | رعاية وحفظ وولاية | القيام على الشيء أو بالأمر بمعنى الحفظ والمراعاة والمواظبة والسياسة والولاية، والقيم والقوام والقيوم
B005 | إقامة وإدامة وتوفية حق | إقامة الشيء وإدامته، وإقامة الصلاة أو الكتاب بمعنى توفية الحق والشرائط والعمل
B006 | مقام وإقامة في موضع | الإقامة بالمكان، والمقام أو المقامة لموضع القدمين أو موضع الإقامة أو زمانها أو المجلس والجماعة …
B007 | نيابة وقيام مقام غيره | قيام شخص أو شيء مقام غيره، وأن يجعل شيء مكان شيء أو يقوم مقامه
B008 | استقامة واعتدال واستواء | استقامة الطريق أو الإنسان أو الأمر، والاعتدال والاستواء، والقويم والقيم والدين المستقيم وعدل الكلام
B009 | قوام وعماد ومعاش | القيام أو القوام لما يقوم به الشيء ويثبت، وعماد الأمر ونظامه وملاكه، وما يقيم العيش والجسم والمعاش
B010 | قيمة وتقويم وتسعير | القيمة ثمن الشيء، وتقويم السلعة أو المتاع، والتقاوم أو الاستقامة بمعنى بيان القيمة
B011 | قامة وقوام الجسم والطول | القامة مقدار طول الإنسان أو قامته، والقوام والقومية وحسن الطول، وانتصاب القامة
B012 | آلة قائمة وجزء قائم | القامة للبكرة أو أداتها عند البئر، وقائم السيف، وقائمة السرير والخوان والدابة، والخشبة التي يمسكها …
B013 | قيامة وبعث وقيام الساعة | القيامة يوم البعث، وقيام الساعة، وقيام الخلق أو الناس لربهم
B014 | مقاومة ومنازلة | قاومه في الأمر أو المصارعة، وتقاوموا في الحرب أو فيما بينهم بمعنى قام بعضهم لبعض أو نازله
B015 | وزن سواء ومقدار معتدل | الدنانير القوم أو القيم، والدينار القائم إذا كان مثقالا سواء لا يرجح
B016 | جمود ووقوف وكلال | قيام الماء بمعنى جمود، وقيام الدابة بمعنى وقوفها أو كلالها وعجزها عن السير
B017 | انتصاف النهار وقائم الظهيرة | قيام قائم الظهيرة أو ميزان النهار إذا قامت الشمس وانتصف النهار وكاد الظل يعقل
B018 | نفاق السوق | قامت السوق إذا نفقت وراجت
B019 | وجع قائم بالعضو | قام بي ظهري أو قامت بي عيناي، أي أوجعني العضو
B020 | قوام في قوائم الشاة | القوام داء يأخذ الشاة في قوائمها فتقوم منه
B021 | عين قائمة ذاهبة البصر | العين القائمة إذا ذهب بصرها وبقيت الحدقة صحيحة

### ن ع م — 140 uses; here: 1:7:3 أَنْعَمْتَ
B001 | حسن الحال والنعمة | النعمة والنعمى والنعماء والنعيم والإنعام، بمعنى حسن الحال وطيب العيش والمن والعطاء والإحسان الموصل …
B002 | اللين والنعومة ورفاه العيش | نعم الشيء إذا لان، والناعم والمنعم والمناعم، والتنعم وطيب العيش والترف، والطعام أو الشخص الموصوف …
B003 | مدح الشيء بنعم | نعم المقابلة لبئس، ونعم الشيء، ونعما، وفبها ونعمت، حيث تكون اللفظة فعلا أو صيغة مدح واستحسان.
B004 | الجواب بنعم والتصديق | نعم حرفا أو كلمة جواب، للتصديق والإيجاب والعدة، وما اتصل بذلك مثل أنعم له أي قال له نعم.
B005 | مال الأنعام والإبل | النعم والأنعام، خصوصا الإبل، وبالتوسيع الإبل والبقر والغنم والبهائم الراعية حيث نصت المصادر على ذلك.
B006 | النعام والنعامة الطائر | النعامة والنعام للطائر المعروف، ذكرا أو أنثى، وما يذكر من جنسه وصفاته المباشرة.
B007 | ما سمي نعامة تشبيها بالهيئة | المسميات المشبهة بالنعامة في الهيئة أو البعد أو السرعة، مثل خشبة البئر والظلة على رأس الجبل وباطن …
B008 | طيران النعامة وتفرق القوم | شالت نعامتهم وخفت نعامتهم وأضحوا نعاما ونحوها، حيث يدل التعبير على الارتحال أو التفرق أو ذهاب العز …
B009 | النعامى ريح لينة | النعامى، وهي ريح الجنوب اللينة أو الأرطب والأبل في الهبوب.
B010 | زاد وأنعم في الفعل | فعل كذا وأنعم بمعنى زاد، وأنعم في الدق أو الإحسان بمعنى بالغ وزاد، وأنعما في الخبر بمعنى زادا على …
B011 | موافقة المكان وطيب المقام | أتيت أرضا فتنعمتني أو فنعمتني، إذا وافقت الشخص وأقام بها أو طاب له النزول.
B012 | المشي على القدم وابتذالها | تنعمت فلانا إذا أتيته على غير دابة أو طلبته ماشيا، وتنعم القدمين أي ابتذلهما، وما قرب منه من المشي …
B013 | نعم الله بك عينا وقرة العين | نعم الله بك عينا، ونعمك عينا، ونعمى عين، ونعمة عين، ونعم عين، ونعام عين، بمعنى قرة العين والإكرام …

### غ ي ر — 154 uses; here: 1:7:5 غَيْرِ
B001 | الصلاح والمنفعة بالميرة والسقي والإصلاح | ميرة الأهل ونفعهم، وسقي الأرض أو القوم بالغيث، وإصلاح الرحال أو شأن الراحلة.
B002 | الغَيْر في الدية | اسم الغَيْر أو الغِيرة للدية، وأخذ الدية بدل القود.
B003 | تغيير الصورة أو إبدال الشيء بغيره | تغيير الشيء فتغيره، وتغير الحال، وتبديل الشيء بغيره، ودفع المنكر بغيره من الحق، والمبادلة والبدل.
B004 | الغَيْرة على الأهل | الغَيْرة المفتوحة على الأهل، ووصف الرجل أو المرأة بالغيور وغيران وغيرى، ولغة الغار في الغيرة.
B005 | السوى والخلاف والاستثناء والنفي | كون الشيء سوى غيره وخلافه، واستعمال غير صفة أو اسما أو أداة استثناء، ومعنى لا، ونفي صورة أو ذات، …

### غ ض ب — 24 uses; here: 1:7:6 ٱلْمَغْضُوبِ
B001 | اشتداد السخط وثورانه للانتقام | الغضب ضد الرضا، وغضب عليه، وأوصاف غضبان وغضوب وغضبة بمعنى كثير الغضب أو سريع الغضب، ووصف الغضب …
B002 | الغضب لشخص حي أو به بعد موته | التعبير غضبت لفلان إذا كان حيا وغضبت به إذا كان ميتا.
B003 | المراغمة والمخالفة | غاضبه ومغاضبا بمعنى راغمه ومراغما لقومه.
B004 | صلابة الصخرة وتماسكها | الغضبة بمعنى الصخرة الصلبة أو المتراكمة أو المستديرة في الجبل.
B005 | غلظ الجسم وشدة الحمرة | رجل غضاب أي غليظ الجلد، ورجل غضب أو أحمر غضب بمعنى أحمر غليظ أو شديد الحمرة.
B006 | تورم العين وما حولها | الغضب أو غضبت عين الرجل بمعنى بخصة في الجفن الأعلى أو ورم ما حول العين أو تحتها.
B007 | العبوس والضجر والعظم في وصف الحيوان أو الشخص | غضوب صفة للعبوس أو الضجر، كناقة غضوب أو امرأة غضوب، ويدخل فيه الغضوب للحية العظيمة كما في Maqayis.
B008 | جلد صلب أو مطوي كدرقة | الغضبة أو الغضب للجلد الصلب: جلد المسن من الوعول، جلد السلحفاة، وقطعة من جلد البعير تطوى كدرقة.

### ض ل ل — 191 uses; here: 1:7:9 ٱلضَّآلِّينَ
B001 | الضلال عن الهدى والقصد | الجور عن القصد وترك الهدى والرشد والوقوع في الغواية والباطل والتيه عن الطريق
B002 | الغيبوبة والخفاء | خفاء الشيء وغيبوبته واندثاره في غيره أو في الأرض ودفن الميت حتى يغيب
B003 | فقدان الشيء | ذهاب الشيء من صاحبه أو عدم الاهتداء إلى موضعه في المتحرك والثابت والمكان وذهاب الدم بلا ثأر
B004 | ضياع الحفظ | نسيان الشيء وغياب الحفظ عن صاحبه أو غياب الشيء عن الحفظ
B005 | الضالّة في المضيعة | البهيمة ولا سيما الإبل إذا بقيت في مضيعة لا يعرف ربها والذكر والأنثى فيها سواء

## Scene map in this window (mechanical, generous; for what the chain map missed)

- travel.route [9 words, 9 roles] ٱلْعَٰلَمِينَ 1:2:4: ع ل م B002 waymark · مَٰلِكِ 1:4:1: م ل ك B006 main course · نَعْبُدُ 1:5:2: ع ب د B005 road surface, ع ب د B010 fork · ٱهْدِنَا 1:6:1: ه د ي B001 guide, ه د ي B002 direction, ه د ي B003 guide · ٱلصِّرَٰطَ 1:6:2: ص ر ط B001 road, س ر ط~alt B002 road · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B008 road · صِرَٰطَ 1:7:1: ص ر ط B001 road, س ر ط~alt B002 road · أَنْعَمْتَ 1:7:3: ن ع م B007 road, ن ع م B012 traveller · ٱلضَّآلِّينَ 1:7:9: ض ل ل B001 stray, ض ل ل B003 stray
- trade.sale [6 words, 6 roles] ٱللَّهِ 1:1:2: و ل ه~alt B002 sale separation · لِلَّهِ 1:2:2: و ل ه~alt B002 sale separation · ٱلدِّينِ 1:4:3: د ي ن B003 bargain · نَعْبُدُ 1:5:2: ع ب د B001 goods · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B007 price, ق و م B010 price, ق و م B018 market · غَيْرِ 1:7:5: غ ي ر B003 exchange
- body.limbs [7 words, 5 roles] بِسْمِ 1:1:1: س م و B004 back · مَٰلِكِ 1:4:1: م ل ك B008 leg · ٱهْدِنَا 1:6:1: ه د ي B003 neck · ٱلصِّرَٰطَ 1:6:2: س ر ط~alt B008 joint · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B012 leg, ق و م B019 back, ق و م B020 leg · صِرَٰطَ 1:7:1: س ر ط~alt B008 joint · أَنْعَمْتَ 1:7:3: ن ع م B007 foot, ن ع م B012 foot
- time.age [5 words, 6 roles] بِسْمِ 1:1:1: و س م~alt B004 appointed time · يَوْمِ 1:4:2: ي و م B002 duration, ي و م B004 epoch, ي و م B005 appointed time · نَعْبُدُ 1:5:2: ع ب د B009 delay · نَسْتَعِينُ 1:5:4: ع و ن B002 age, ع و ن B004 old age · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B006 appointed time
- wealth.property [8 words, 4 roles] رَبِّ 1:2:3: ر ب ب B016 need · مَٰلِكِ 1:4:1: م ل ك B002 wealth, م ل ك B007 provision · ٱهْدِنَا 1:6:1: ه د ي B005 wealth · ٱلصِّرَٰطَ 1:6:2: س ر ط~alt B005 stinginess · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B009 provision · صِرَٰطَ 1:7:1: س ر ط~alt B005 stinginess · أَنْعَمْتَ 1:7:3: ن ع م B001 provision · غَيْرِ 1:7:5: غ ي ر B001 provision
- kin.birth_nursing [7 words, 4 roles] ٱللَّهِ 1:1:2: و ل ه~alt B002 mother child separation · ٱلرَّحْمَٰنِ 1:1:3: ر ح م B003 womb, ر ح م B004 birth · ٱلرَّحِيمِ 1:1:4: ر ح م B003 womb, ر ح م B004 birth · لِلَّهِ 1:2:2: و ل ه~alt B002 mother child separation · رَبِّ 1:2:3: ر ب ب B005 foster child · ٱلرَّحْمَٰنِ 1:3:1: ر ح م B003 womb, ر ح م B004 birth · ٱلرَّحِيمِ 1:3:2: ر ح م B003 womb, ر ح م B004 birth
- war.battle [7 words, 4 roles] ٱللَّهِ 1:1:2: و ل ه~alt B002 captive · لِلَّهِ 1:2:2: و ل ه~alt B002 captive · نَعْبُدُ 1:5:2: ع ب د B004 captive · نَسْتَعِينُ 1:5:4: ع و ن B003 battle · ٱهْدِنَا 1:6:1: ه د ي B007 captive · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B014 confrontation · أَنْعَمْتَ 1:7:3: ن ع م B008 rout
- body.strength [6 words, 4 roles] مَٰلِكِ 1:4:1: م ل ك B001 firmness · نَعْبُدُ 1:5:2: ع ب د B007 strength · نَسْتَعِينُ 1:5:4: ع و ن B005 strength · ٱهْدِنَا 1:6:1: ه د ي B008 frailty, ه د ي B009 frailty · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B011 build, ق و م B014 strength · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B005 firmness
- pastoral.herding [6 words, 4 roles] رَبِّ 1:2:3: ر ب ب B007 fold, ر ب ب B014 herd · مَٰلِكِ 1:4:1: م ل ك B008 lead animal · نَسْتَعِينُ 1:5:4: ع و ن B006 herd · ٱهْدِنَا 1:6:1: ه د ي B003 lead animal · أَنْعَمْتَ 1:7:3: ن ع م B005 herd · ٱلضَّآلِّينَ 1:7:9: ض ل ل B005 stray
- know.perceiving [5 words, 4 roles] بِسْمِ 1:1:1: و س م~alt B002 perceiving · رَبِّ 1:2:3: ر ب ب B003 knowing · ٱلْعَٰلَمِينَ 1:2:4: ع ل م B001 knowing · ٱهْدِنَا 1:6:1: ه د ي B009 ignorance · ٱلضَّآلِّينَ 1:7:9: ض ل ل B004 forgetting
- war.arms [5 words, 4 roles] مَٰلِكِ 1:4:1: م ل ك B001 shaft · ٱهْدِنَا 1:6:1: ه د ي B003 arrow · ٱلصِّرَٰطَ 1:6:2: ص ر ط B003 sword, س ر ط~alt B004 sword · صِرَٰطَ 1:7:1: ص ر ط B003 sword, س ر ط~alt B004 sword · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B008 shield
- animal.wild [4 words, 4 roles] رَبِّ 1:2:3: ر ب ب B014 wild cattle · ٱلْعَٰلَمِينَ 1:2:4: ع ل م B007 hyena · نَسْتَعِينُ 1:5:4: ع و ن B006 wild ass · أَنْعَمْتَ 1:7:3: ن ع م B006 ostrich
- ritual.prayer [4 words, 4 roles] ٱللَّهِ 1:1:2: ء ل ه B001 worship, ء ل ه B002 call · لِلَّهِ 1:2:2: ء ل ه B001 worship, ء ل ه B002 call · ٱلدِّينِ 1:4:3: د ي ن B001 worship · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B002 standing, ق و م B003 standing, ق و م B005 prayer performance
- rule.ownership [4 words, 6 roles] رَبِّ 1:2:3: ر ب ب B001 owner · مَٰلِكِ 1:4:1: م ل ك B002 possession · ٱلدِّينِ 1:4:3: د ي ن B004 master · نَعْبُدُ 1:5:2: ع ب د B001 servant, ع ب د B002 servant, ع ب د B004 servitude, ع ب د B006 service
- speech.praise_blame [4 words, 4 roles] بِسْمِ 1:1:1: س م و B007 boasting · ٱلْحَمْدُ 1:2:1: ح م د B001 praise, ح م د B003 praise, ح م د B005 boasting, ح م د B006 thanks · ٱهْدِنَا 1:6:1: ه د ي B011 blame · أَنْعَمْتَ 1:7:3: ن ع م B003 praise
- water.well [4 words, 4 roles] رَبِّ 1:2:3: ر ب ب B013 abundant water · ٱلْعَٰلَمِينَ 1:2:4: ع ل م B005 well · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B012 pulley · أَنْعَمْتَ 1:7:3: ن ع م B007 beam
- emotion.love [7 words, 3 roles] ٱللَّهِ 1:1:2: و ل ه~alt B001 longing · ٱلرَّحْمَٰنِ 1:1:3: ر ح م B001 mercy · ٱلرَّحِيمِ 1:1:4: ر ح م B001 mercy · لِلَّهِ 1:2:2: و ل ه~alt B001 longing · ٱلرَّحْمَٰنِ 1:3:1: ر ح م B001 mercy · ٱلرَّحِيمِ 1:3:2: ر ح م B001 mercy · ٱهْدِنَا 1:6:1: ه د ي B004 affection
- kin.lineage [6 words, 3 roles] ٱلرَّحْمَٰنِ 1:1:3: ر ح م B002 kin tie · ٱلرَّحِيمِ 1:1:4: ر ح م B002 kin tie · رَبِّ 1:2:3: ر ب ب B004 tribe · ٱلرَّحْمَٰنِ 1:3:1: ر ح م B002 kin tie · ٱلرَّحِيمِ 1:3:2: ر ح م B002 kin tie · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B001 clan
- dwelling.settlement [5 words, 3 roles] بِسْمِ 1:1:1: و س م~alt B004 market · ٱلدِّينِ 1:4:3: د ي ن B006 town · نَسْتَعِينُ 1:5:4: ع و ن B008 town · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B006 dwelling place, ق و م B018 market · أَنْعَمْتَ 1:7:3: ن ع م B011 dwelling place
- motion.gather_scatter [5 words, 3 roles] بِسْمِ 1:1:1: و س م~alt B004 gathering · رَبِّ 1:2:3: ر ب ب B004 crowd · نَعْبُدُ 1:5:2: ع ب د B010 dispersal · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B001 crowd · أَنْعَمْتَ 1:7:3: ن ع م B008 dispersal
- motion.passage [5 words, 3 roles] ٱللَّهِ 1:1:2: و ل ه~alt B003 vanishing · لِلَّهِ 1:2:2: و ل ه~alt B003 vanishing · ٱلصِّرَٰطَ 1:6:2: ص ر ط B002 being swallowed, ص ر ط B003 penetrating, س ر ط~alt B004 penetrating · صِرَٰطَ 1:7:1: ص ر ط B002 being swallowed, ص ر ط B003 penetrating, س ر ط~alt B004 penetrating · ٱلضَّآلِّينَ 1:7:9: ض ل ل B002 vanishing
- sky.bodies [5 words, 3 roles] بِسْمِ 1:1:1: س م و B002 moon · ٱلصِّرَٰطَ 1:6:2: س ر ط~alt B007 constellation · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B017 zenith · صِرَٰطَ 1:7:1: س ر ط~alt B007 constellation · أَنْعَمْتَ 1:7:3: ن ع م B007 constellation
- speech.calling [5 words, 3 roles] بِسْمِ 1:1:1: س م و B005 naming · ٱللَّهِ 1:1:2: ء ل ه B002 call · ٱلْحَمْدُ 1:2:1: ح م د B003 naming · لِلَّهِ 1:2:2: ء ل ه B002 call · أَنْعَمْتَ 1:7:3: ن ع م B004 answer, ن ع م B013 call
- rule.covenant [4 words, 3 roles] ٱللَّهِ 1:1:2: ء ل ه B002 oath · لِلَّهِ 1:2:2: ء ل ه B002 oath · رَبِّ 1:2:3: ر ب ب B011 covenant · ٱلدِّينِ 1:4:3: د ي ن B007 witness
- war.protection [4 words, 3 roles] رَبِّ 1:2:3: ر ب ب B011 protection pact · نَسْتَعِينُ 1:5:4: ع و ن B001 ally · ٱهْدِنَا 1:6:1: ه د ي B007 protected client · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B002 ally
- animal.reptile_fish [3 words, 3 roles] ٱلصِّرَٰطَ 1:6:2: س ر ط~alt B006 crab · صِرَٰطَ 1:7:1: س ر ط~alt B006 crab · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B007 snake, غ ض ب B008 turtle
- body.mouth_throat [3 words, 3 roles] ٱلْعَٰلَمِينَ 1:2:4: ع ل م B004 lip · ٱلصِّرَٰطَ 1:6:2: ص ر ط B002 throat, س ر ط~alt B001 swallowing, س ر ط~alt B008 throat · صِرَٰطَ 1:7:1: ص ر ط B002 throat, س ر ط~alt B001 swallowing, س ر ط~alt B008 throat
- dwelling.building [3 words, 3 roles] بِسْمِ 1:1:1: س م و B004 roof · مَٰلِكِ 1:4:1: م ل ك B001 wall · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B009 pillar
- kin.household [3 words, 3 roles] رَبِّ 1:2:3: ر ب ب B002 provision, ر ب ب B005 dependant · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B004 provision · غَيْرِ 1:7:5: غ ي ر B004 protection
- plant.growth_decay [3 words, 4 roles] بِسْمِ 1:1:1: س م و B004 growth, و س م~alt B003 growth, و س م~alt B006 leaf · رَبِّ 1:2:3: ر ب ب B002 growth, ر ب ب B012 greenness · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B002 root
- rule.obedience [3 words, 3 roles] ٱلدِّينِ 1:4:3: د ي ن B001 obedience · نَعْبُدُ 1:5:2: ع ب د B003 submission · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B003 defiance
- speech.news [3 words, 3 roles] بِسْمِ 1:1:1: س م و B008 report · ٱلْعَٰلَمِينَ 1:2:4: ع ل م B001 message · مَٰلِكِ 1:4:1: م ل ك B009 messenger
- travel.open_land [3 words, 3 roles] بِسْمِ 1:1:1: س م و B006 waste · مَٰلِكِ 1:4:1: م ل ك B007 water source · ٱلضَّآلِّينَ 1:7:9: ض ل ل B001 getting lost, ض ل ل B005 waste
- war.vengeance [3 words, 3 roles] غَيْرِ 1:7:5: غ ي ر B002 blood money · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B001 vengeance, غ ض ب B002 vengeance · ٱلضَّآلِّينَ 1:7:9: ض ل ل B003 unavenged blood
- body.illness [7 words, 2 roles] ٱلرَّحْمَٰنِ 1:1:3: ر ح م B004 pain · ٱلرَّحِيمِ 1:1:4: ر ح م B004 pain · ٱلرَّحْمَٰنِ 1:3:1: ر ح م B004 pain · ٱلرَّحِيمِ 1:3:2: ر ح م B004 pain · ٱلصِّرَٰطَ 1:6:2: س ر ط~alt B008 disease · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B019 pain, ق و م B020 disease · صِرَٰطَ 1:7:1: س ر ط~alt B008 disease
- pastoral.livestock_wealth [7 words, 2 roles] رَبِّ 1:2:3: ر ب ب B014 livestock · نَعْبُدُ 1:5:2: ع ب د B007 livestock · ٱهْدِنَا 1:6:1: ه د ي B005 livestock · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B020 livestock · أَنْعَمْتَ 1:7:3: ن ع م B005 livestock · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B007 livestock · ٱلضَّآلِّينَ 1:7:9: ض ل ل B003 lost animal, ض ل ل B005 lost animal
- body.innards [5 words, 2 roles] ٱلرَّحْمَٰنِ 1:1:3: ر ح م B003 belly · ٱلرَّحِيمِ 1:1:4: ر ح م B003 belly · ٱلرَّحْمَٰنِ 1:3:1: ر ح م B003 belly · ٱلرَّحِيمِ 1:3:2: ر ح م B003 belly · مَٰلِكِ 1:4:1: م ل ك B005 heart
- motion.pace [5 words, 2 roles] نَعْبُدُ 1:5:2: ع ب د B009 haste · ٱهْدِنَا 1:6:1: ه د ي B008 slowness, ه د ي B009 slowness, ه د ي B010 slowness · ٱلصِّرَٰطَ 1:6:2: س ر ط~alt B001 haste · صِرَٰطَ 1:7:1: س ر ط~alt B001 haste · أَنْعَمْتَ 1:7:3: ن ع م B012 slowness
- trade.gift [5 words, 2 roles] ٱلْحَمْدُ 1:2:1: ح م د B005 favour · رَبِّ 1:2:3: ر ب ب B016 favour · نَسْتَعِينُ 1:5:4: ع و ن B001 favour · ٱهْدِنَا 1:6:1: ه د ي B004 gift · أَنْعَمْتَ 1:7:3: ن ع م B001 gift
- emotion.grief_joy [4 words, 2 roles] ٱللَّهِ 1:1:2: و ل ه~alt B001 grief · لِلَّهِ 1:2:2: و ل ه~alt B001 grief · نَعْبُدُ 1:5:2: ع ب د B008 grief · أَنْعَمْتَ 1:7:3: ن ع م B013 gladness
- animal.small [3 words, 2 roles] ٱللَّهِ 1:1:2: و ل ه~alt B004 spider · لِلَّهِ 1:2:2: و ل ه~alt B004 spider · مَٰلِكِ 1:4:1: م ل ك B008 bee
- emotion.pride [3 words, 2 roles] بِسْمِ 1:1:1: س م و B001 honour, س م و B007 pride, س م و B008 honour · نَعْبُدُ 1:5:2: ع ب د B006 honour, ع ب د B008 pride · غَيْرِ 1:7:5: غ ي ر B004 honour
- quantity.more_less [3 words, 2 roles] ٱلْحَمْدُ 1:2:1: ح م د B004 completion · رَبِّ 1:2:3: ر ب ب B002 completion · أَنْعَمْتَ 1:7:3: ن ع م B010 increase
- ritual.idols_lots [3 words, 2 roles] ٱللَّهِ 1:1:2: ء ل ه B001 cult · لِلَّهِ 1:2:2: ء ل ه B001 cult · رَبِّ 1:2:3: ر ب ب B010 lot
- rule.kingship [3 words, 2 roles] رَبِّ 1:2:3: ر ب ب B001 king · مَٰلِكِ 1:4:1: م ل ك B003 king · ٱلدِّينِ 1:4:3: د ي ن B004 dominion
- trade.debt [3 words, 2 roles] ٱلدِّينِ 1:4:3: د ي ن B003 debt · ٱلصِّرَٰطَ 1:6:2: س ر ط~alt B005 repayment · صِرَٰطَ 1:7:1: س ر ط~alt B005 repayment
- travel.departure_return [3 words, 2 roles] رَبِّ 1:2:3: ر ب ب B007 lodging · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B006 lodging · أَنْعَمْتَ 1:7:3: ن ع م B008 departure, ن ع م B011 lodging
- travel.mount [3 words, 2 roles] نَعْبُدُ 1:5:2: ع ب د B011 exhaustion · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B016 exhaustion · غَيْرِ 1:7:5: غ ي ر B001 saddle
- water.rain_cloud [3 words, 2 roles] بِسْمِ 1:1:1: س م و B004 cloud, و س م~alt B003 rain · رَبِّ 1:2:3: ر ب ب B007 cloud, ر ب ب B008 cloud · غَيْرِ 1:7:5: غ ي ر B001 rain
- animal.birds [2 words, 2 roles] ٱلْعَٰلَمِينَ 1:2:4: ع ل م B006 bird of prey · أَنْعَمْتَ 1:7:3: ن ع م B006 bird
- body.eye [2 words, 3 roles] ٱلْمُسْتَقِيمَ 1:6:3: ق و م B019 eye, ق و م B021 blindness · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B006 eyelid
- craft.dyeing [2 words, 2 roles] بِسْمِ 1:1:1: و س م~alt B006 dye · ٱلْعَٰلَمِينَ 1:2:4: ع ل م B002 marking
- emotion.anger [2 words, 3 roles] نَعْبُدُ 1:5:2: ع ب د B008 anger · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B001 anger, غ ض ب B002 anger, غ ض ب B003 enmity, غ ض ب B007 irritability
- food.eating [2 words, 2 roles] ٱلصِّرَٰطَ 1:6:2: ص ر ط B002 swallowing, س ر ط~alt B001 gulp, س ر ط~alt B003 swallowing · صِرَٰطَ 1:7:1: ص ر ط B002 swallowing, س ر ط~alt B001 gulp, س ر ط~alt B003 swallowing
- hunt.chase [2 words, 2 roles] بِسْمِ 1:1:1: س م و B006 hunter · ٱلْعَٰلَمِينَ 1:2:4: ع ل م B006 falcon
- kin.marriage [2 words, 3 roles] مَٰلِكِ 1:4:1: م ل ك B002 divorce, م ل ك B004 contract · ٱهْدِنَا 1:6:1: ه د ي B006 bride conveyance
- land.mountain [2 words, 2 roles] ٱلْعَٰلَمِينَ 1:2:4: ع ل م B002 mountain · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B004 rock
- law.judgment [2 words, 3 roles] ٱلدِّينِ 1:4:3: د ي ن B002 verdict, د ي ن B007 testimony · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B013 judgment
- life.growing_up [2 words, 2 roles] رَبِّ 1:2:3: ر ب ب B009 youth · نَسْتَعِينُ 1:5:4: ع و ن B002 maturity, ع و ن B005 maturity
- pastoral.animal_care [2 words, 3 roles] بِسْمِ 1:1:1: و س م~alt B001 brand · نَعْبُدُ 1:5:2: ع ب د B005 tar coating, ع ب د B011 taming
- pastoral.breeding [2 words, 2 roles] بِسْمِ 1:1:1: س م و B003 mating · رَبِّ 1:2:3: ر ب ب B009 newborn
- posture.upright [2 words, 5 roles] ٱهْدِنَا 1:6:1: ه د ي B010 bearing · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B002 standing, ق و م B005 setting upright, ق و م B008 straight, ق و م B011 erect, ق و م B016 standing
- ritual.sanctuary [2 words, 2 roles] بِسْمِ 1:1:1: و س م~alt B004 pilgrim · ٱهْدِنَا 1:6:1: ه د ي B005 sanctuary
- rule.leadership [2 words, 3 roles] رَبِّ 1:2:3: ر ب ب B017 chief · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B004 chief, ق و م B006 council, ق و م B007 deputy
- sign.marking [2 words, 2 roles] بِسْمِ 1:1:1: س م و B005 sign, و س م~alt B001 mark, و س م~alt B002 sign · ٱلْعَٰلَمِينَ 1:2:4: ع ل م B002 mark, ع ل م B003 sign, ع ل م B004 mark
- time.day_night [2 words, 3 roles] يَوْمِ 1:4:2: ي و م B001 daylight, ي و م B005 day · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B017 noon
- tool.vessel [2 words, 2 roles] رَبِّ 1:2:3: ر ب ب B010 basket · ٱهْدِنَا 1:6:1: ه د ي B004 vessel
- travel.sea [2 words, 2 roles] رَبِّ 1:2:3: ر ب ب B017 steering · نَعْبُدُ 1:5:2: ع ب د B005 ship
- water.gathered [2 words, 2 roles] رَبِّ 1:2:3: ر ب ب B013 pool · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B016 stagnant water
- food.sweet_fat [3 words, 1 roles] رَبِّ 1:2:3: ر ب ب B006 sweet dish · ٱلصِّرَٰطَ 1:6:2: س ر ط~alt B003 sweet dish · صِرَٰطَ 1:7:1: س ر ط~alt B003 sweet dish
- tool.implement [3 words, 1 roles] بِسْمِ 1:1:1: و س م~alt B001 device · نَعْبُدُ 1:5:2: ع ب د B012 device · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B012 device
- craft.coating [2 words, 1 roles] رَبِّ 1:2:3: ر ب ب B006 coating · نَعْبُدُ 1:5:2: ع ب د B005 coating
- land.desert_sand [2 words, 1 roles] ٱللَّهِ 1:1:2: و ل ه~alt B003 desert · لِلَّهِ 1:2:2: و ل ه~alt B003 desert
- motion.up_down [2 words, 1 roles] بِسْمِ 1:1:1: س م و B001 height, س م و B002 height · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B011 height
- posture.leaning [2 words, 1 roles] ٱهْدِنَا 1:6:1: ه د ي B008 support · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B009 support
- water.spring_stream [2 words, 1 roles] ٱللَّهِ 1:1:2: و ل ه~alt B003 flow · لِلَّهِ 1:2:2: و ل ه~alt B003 flow
- weather.wind [2 words, 1 roles] رَبِّ 1:2:3: ر ب ب B007 wind · أَنْعَمْتَ 1:7:3: ن ع م B009 wind
- divine.lordship [13 words, 5 roles] ٱللَّهِ 1:1:2: ء ل ه B001 worship · ٱلرَّحْمَٰنِ 1:1:3: ر ح م B001 mercy · ٱلرَّحِيمِ 1:1:4: ر ح م B001 mercy · لِلَّهِ 1:2:2: ء ل ه B001 worship · رَبِّ 1:2:3: ر ب ب B001 lord · ٱلرَّحْمَٰنِ 1:3:1: ر ح م B001 mercy · ٱلرَّحِيمِ 1:3:2: ر ح م B001 mercy · مَٰلِكِ 1:4:1: م ل ك B003 lord · يَوْمِ 1:4:2: ي و م B004 mercy judgment · ٱلدِّينِ 1:4:3: د ي ن B001 worship · نَعْبُدُ 1:5:2: ع ب د B003 worship · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B013 judgment · ٱلْمَغْضُوبِ 1:7:6: غ ض ب B001 judgment
- moral.guidance_error [5 words, 3 roles] ٱهْدِنَا 1:6:1: ه د ي B001 right guidance · ٱلصِّرَٰطَ 1:6:2: ص ر ط B001 right guidance, س ر ط~alt B002 right guidance · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B008 rectitude · صِرَٰطَ 1:7:1: ص ر ط B001 right guidance, س ر ط~alt B002 right guidance · ٱلضَّآلِّينَ 1:7:9: ض ل ل B001 straying
- moral.good_evil [3 words, 2 roles] ٱلْحَمْدُ 1:2:1: ح م د B002 good, ح م د B003 good · ٱلْمُسْتَقِيمَ 1:6:3: ق و م B008 righteousness · أَنْعَمْتَ 1:7:3: ن ع م B001 good, ن ع م B003 good
- moral.truth_falsehood [2 words, 1 roles] ٱلدِّينِ 1:4:3: د ي ن B007 confirmation · أَنْعَمْتَ 1:7:3: ن ع م B004 confirmation

## Variant readings

1:4:1 مَٰلِكِ → مَالِكِ (māliki; canonical; mutawatir) Ḥafṣ, Kisāʾī, Yaʿqūb, Khalaf
1:4:1 مَٰلِكِ → مَلِكِ (maliki; Lvw; mutawatir) Nāfiʿ, Ibn Kathīr, Abū ʿAmr, Ibn ʿĀmir, ʿĀṣim (Shuʿba), Ḥamza
1:6:2 ٱلصِّرَٰطَ → السِّرَاطَ (as-sirāṭa; ibdāl; mutawatir) Sīn for ṣād
1:6:2 ٱلصِّرَٰطَ → الصؗرَاطَ (aṣᶻ-ṣᶻirāṭa; ibdāl; mutawatir) Intermediate ṣ/z sound (ishmām)
1:7:1 صِرَٰطَ → سِرَاطَ (sirāṭa; ibdāl; mutawatir) ṣād→sīn substitution; same surface meaning but phonetically closer to sabīl cognate
1:7:1 صِرَٰطَ → صِؗرَاطَ (ṣᶻirāṭa; ibdāl; mutawatir) ishmām (ṣ with z-color); transitional articulation between ṣ and s
1:7:4 عَلَيْهِمْ → عَلَيْهِمُۥ (ʿalayhimū; vhr|madd; mutawatir) lengthened pronoun vowel (silat al-mīm); phonetic variant
1:7:4 عَلَيْهِمْ → عَلَيْهُمْ (ʿalayhum; vhr; mutawatir) short ḍamma pronoun vowel instead of kasra
1:7:7 عَلَيْهِمْ → عَلَيْهُمْ (ʿalayhum; vhr; mutawatir) ḍamma pronoun-vowel variant; canonical

## Paths you may read

- classical entries per root: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/entries/<root letters without spaces>.md
- every use of a frequent lemma: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/kwic/
- the Quran text: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/quran.tsv; words: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/words.tsv; lemma index: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/lemmas.tsv
- the whole dictionary: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/branches.tsv
