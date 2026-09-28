# Ayah reading

You are reading ayah 1:3 with every branch of every one of its words open, inside its neighbourhood and its surah. You produce the record from which its commentary will be written: everything you hear, each finding anchored and contained, each with what it makes perceptible. You do not write the commentary; you output JSON.

## Who this is for

One reader: a curious Turkish speaker with almost no Arabic grammar. Their Arabic arrives through loanwords, and those loanwords, theological ones above all, have shifted, narrowed or lost their meaning in Turkish. Canonical meanings are easy for them to find elsewhere; they are only the anchor. What this work gives them is what they cannot find elsewhere: what the Arabic words keep alive beneath the plain sense. Success: after reading, they understand the ayah and the surah better than before, and they are never disoriented.

## How a sense becomes heard

- Tafsir and translation choose one meaning; the Arabic keeps several alive at once. Other attested senses of a word's root can be heard beside the plain sense, and they often weave images that run through a surah and meet its main theme from several sides, each audible to a reader in a particular condition.
- Every attested branch of every root is open. Branches have no order. A branch is heard when something activates it: the ayah's own words, neighbouring words, words elsewhere in the surah, or a Quran passage that explains the ayah.
- The dictionary is both guard and supplier. Use the branches given (and the full entries you may read). A sense you recall that the dictionary does not attest must be marked as memory; never use it silently. No invented senses, sources, etymologies or chronology.
- Do not prune early. Keep partial, strange and minor activations. Combine fragments across words, branches and roles. Let a completed image strengthen its weak members. Only then ask what it shows about the plain reading. No plausibility filter, no confidence scores, no verdict on an image from one of its members.
- Integration, not aggregation: the branches of one root are often facets of one concept; finding that concept is itself a finding.
- Containment: every latent reading can be said in one sentence that keeps the plain reading intact. Never "not X but Y".
- The test that matters: what does this make perceptible in the plain reading that a paraphrase could not (more spatial, bodily, causal, relational, material, temporal, compositional)? Space in the commentary will follow that payoff; it is a matter of function, not of certainty.
- Readings coexist. Never declare one correct.

## What you have (below the line)

1. The ayah in its neighbourhood (±7 ayat; the focus is marked).
2. Its words with roots, lemmas and parts of speech.
3. The dictionary for its roots, one line per branch (branch | Arabic image | Arabic definition, trimmed). Alternative roots are marked ~alt with the reason.
4. Scene lines touching its words: first in the neighbourhood, then scenes that reach elsewhere in the surah (each with at most a few far words, those adding roles the neighbourhood lacks first, and a file listing every member). Members of one scene activate one another: several words supplying different parts of one scene are themselves an activation. Mechanical and generous: an ordering aid, not a worklist.
5. The plan from the window reading: the images this ayah should open, advance or complete, the images earlier ayat opened, and the window's movement. Use it; you are not bound by it. If the ayah opens an image the plan missed, record it.
6. The concordance for its lemmas: every use (lemmas used up to 30 times) or a use profile (frequent lemmas).
7. Variant readings.
8. Turkish loanword cards for its lemmas: what the Turkish reader hears, what the Arabic keeps.

You may read more from the paths listed at the end. Read only what a specific question needs; do not read in bulk.

## The record

- ref: 1:3.
- ground: the plain sense in two to four sentences, as a careful translator would give it.
- findings: every latent reading, local resonance, image member, root concept, Quran-loaded word, variant and grammar point you hear. For each:
  - id (F1, F2, …); kind: latent | image | local_resonance | concept | loaded_word | variant | grammar;
  - anchor: the word (ref S:A:W, surface) and the dictionary branch (root with spaces, branch Bnnn) the finding stands on (branch may be empty for grammar);
  - triggers: the words (ref, surface) that activate it and how (shared scene, sound, shared root, syntax, a neighbouring or explaining passage);
  - statement: one containment sentence (plain reading kept);
  - perceptible: what it makes perceptible in the plain reading;
  - image: the plan's image id, a new id you give, or "";
  - memory: true if any part rests on a sense the dictionary does not attest;
  - for_prose: lead | support | record. Lead: this ayah's commentary should make it perceptible; support: it can serve a lead finding; record: kept here, not needed in this ayah's prose. Decide by payoff for this reader in this ayah, respecting the plan.
- loaded_words: words the Quran uses with one recurring role (read it from the concordance: the role, and how many uses keep it), and where a usual translation departs from that role here.
- losses: for the key Turkish words the reader will meet for this ayah (from the loanword cards and your knowledge of Turkish; memory true for what the cards do not give): what the Turkish word loses or adds against the Arabic here.
- grammar: only grammar the Turkish reader cannot hear and that matters to a reading here, one line each; else empty.
- variants: variant readings that open or support a reading, one line each; else empty.
- reread: the plain reading read anew with the findings heard together, three to six sentences.
- disclosed: the image ids this ayah's commentary will make audible (so later ayat can build on them).
- set_aside: activations you considered and did not keep, each with why. Nothing is lost silently.

Do not audit your own findings for plausibility; the payoff test is the only test here. Evidence from the rest of the Quran will be gathered separately after this reading. Analysis in English; Arabic as in the text. Output only the JSON object required by the schema.

---

# Ayah 1:3

## The ayah in its neighbourhood (1:1–7)

1:1| بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
1:2| ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
1:3| ٱلرَّحْمَٰنِ ٱلرَّحِيمِ  ◀ focus
1:4| مَٰلِكِ يَوْمِ ٱلدِّينِ
1:5| إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
1:6| ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
1:7| صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

## Its words (ref surface | root | lemma | pos)

1:3:1 ٱلرَّحْمَٰنِ | ر ح م | رَّحْمَٰن | ADJ
1:3:2 ٱلرَّحِيمِ | ر ح م | رَّحِيم | ADJ

## Dictionary for its roots (branch | image | definition | tr: Turkish gloss)

### ر ح م — 339 uses; here: 1:3:1 ٱلرَّحْمَٰنِ; 1:3:2 ٱلرَّحِيمِ
B001 | الرَّحْمَة والرقة | الرقة والعطف والرأفة والإحسان إلى المرحوم والمرحمة والتراحم والترحم وأسماء الرحمن والرحيم من جهة …
B002 | الرَّحِم والقرابة | الرَّحِم بمعنى القرابة القريبة وأسباب النسب وصلة الرحم وقطعها والأرحام.
B003 | رَحِم الأنثى | رَحِم المرأة أو الأنثى بوصفه بيت منبت الولد ووعاءه في البطن.
B004 | وجع الرَّحِم بعد الولادة | الرحوم والراحم والرواحم وما قيل في الناقة أو الشاة أو المرأة إذا اشتكت رحمها أو أصابه داء أو ورم أو …

## Scene lines touching its words, in the neighbourhood

- kin.birth_nursing [7 words, 4 roles] here: ٱلرَّحْمَٰنِ 1:3:1: ر ح م B003 womb, ر ح م B004 birth · ٱلرَّحِيمِ 1:3:2: ر ح م B003 womb, ر ح م B004 birth | with: ٱللَّهِ 1:1:2 mother child separation · ٱلرَّحْمَٰنِ 1:1:3 womb, birth · رَبِّ 1:2:3 foster child · +2 more (all: data/scenes/s001/kin.birth_nursing.md)
- emotion.love [7 words, 3 roles] here: ٱلرَّحْمَٰنِ 1:3:1: ر ح م B001 mercy · ٱلرَّحِيمِ 1:3:2: ر ح م B001 mercy | with: ٱللَّهِ 1:1:2 longing · ٱلرَّحْمَٰنِ 1:1:3 mercy · ٱهْدِنَا 1:6:1 affection · +2 more (all: data/scenes/s001/emotion.love.md)
- kin.lineage [6 words, 3 roles] here: ٱلرَّحْمَٰنِ 1:3:1: ر ح م B002 kin tie · ٱلرَّحِيمِ 1:3:2: ر ح م B002 kin tie | with: ٱلرَّحْمَٰنِ 1:1:3 kin tie · رَبِّ 1:2:3 tribe · ٱلْمُسْتَقِيمَ 1:6:3 clan · +1 more (all: data/scenes/s001/kin.lineage.md)
- body.illness [7 words, 2 roles] here: ٱلرَّحْمَٰنِ 1:3:1: ر ح م B004 pain · ٱلرَّحِيمِ 1:3:2: ر ح م B004 pain | with: ٱلرَّحْمَٰنِ 1:1:3 pain · ٱلصِّرَٰطَ 1:6:2 disease · ٱلْمُسْتَقِيمَ 1:6:3 pain, disease · +2 more (all: data/scenes/s001/body.illness.md)
- body.innards [5 words, 2 roles] here: ٱلرَّحْمَٰنِ 1:3:1: ر ح م B003 belly · ٱلرَّحِيمِ 1:3:2: ر ح م B003 belly | with: ٱلرَّحْمَٰنِ 1:1:3 belly · مَٰلِكِ 1:4:1 heart · +1 more (all: data/scenes/s001/body.innards.md)
- divine.lordship [13 words, 5 roles] here: ٱلرَّحْمَٰنِ 1:3:1: ر ح م B001 mercy · ٱلرَّحِيمِ 1:3:2: ر ح م B001 mercy | with: ٱللَّهِ 1:1:2 worship · ٱلرَّحْمَٰنِ 1:1:3 mercy · رَبِّ 1:2:3 lord · مَٰلِكِ 1:4:1 lord · يَوْمِ 1:4:2 mercy judgment · ٱلدِّينِ 1:4:3 worship · نَعْبُدُ 1:5:2 worship · ٱلْمُسْتَقِيمَ 1:6:3 judgment · ٱلْمَغْضُوبِ 1:7:6 judgment · +2 more (all: data/scenes/s001/divine.lordship.md)

## Scenes of its words that reach beyond the neighbourhood (at most 10 far words each, new roles first; every member in the file named)

(none)

## Plan from the window reading

- completes: I3 The womb and the one who raises stage by stage — A womb holds growing young. Kin are bound by the tie of the womb. A newly delivered mother stays home to nurse, and a caregiver takes charge of a child and raises it stage by stage until it is complete.. Members: ٱلرَّحْمَٰنِ 1:1:3 B001 tenderness and kindness toward the one shown mercy; ٱلرَّحِيمِ 1:1:4 B003 the womb as the house where offspring grows; ٱلرَّحِيمِ 1:1:4 B002 the kinship tie that comes from the womb; رَبِّ 1:2:3 B002 the one who puts a thing right and completes it, raising it 'stage by stage' (tarbiya ḥālan fa-ḥālan); رَبِّ 1:2:3 B005 the fosterer (rābb, rābba) who takes charge of the rabīb, the child in their care; رَبِّ 1:2:3 B009 the ewe that has just given birth and stays home for its milk (minor); ٱلرَّحْمَٰنِ 1:3:1 B001 mercy named again, after the rabb; ٱلرَّحِيمِ 1:3:2 B003 the womb heard again around the rabb. Perceptible: In Turkish, rahmet has become an abstract pity or rain. Here mercy becomes bodily and connected to kin: the tenderness of a womb toward what grows inside it. Rabb is placed between two mentions of the mercy names (1:1, 1:3), so lordship is heard wrapped in womb-tenderness: an owner who also raises, stage by stage, over time.
- note: Mercy named again after rabb wraps lordship in womb-tenderness: the owner of 1:2 is also the one who carries and raises.

Opened by earlier ayat:
- 1:1 opened I2 The branded herd, its owner, its lead animal and the stray
- 1:1 opened I3 The womb and the one who raises stage by stage
- 1:2 opened I4 The master's household: owner, king and the owned one
- 1:2 opened I7 Gift gently sent, favor received, praise returned

Window movement: The surah moves from being named and marked (1:1, bismi, which can also be heard as wasm, the owner's brand) to an owner who raises (rabb) wrapped on both sides in womb-mercy (1:1–3). It then reaches the owner and king of a Day on which what is owed is settled (1:4). At 1:5 the owned ones stop speaking about the master and speak to him, declaring service and leaning on him for help. From that posture they ask to be led, held up and gifted onto a road already trodden smooth by the favored. That road takes its walker in (1:6–7). Their thanks were given at the start, and they ask not to become the stray beast in the waste whose owner no one knows. The surah's arc runs from the mark of belonging to the danger of being an unmarked stray, with praise answering a favor it only names at the end.

## Concordance for its lemmas

### رَّحْمَٰن — ر ح م — 57 uses in the Quran
use profile: {"root": "ر ح م", "lemma": "رَّحْمَٰن", "total": 57, "groups": [{"label": "Named in an identification, title, or formula", "count": 11, "refs": ["1:1:3", "1:3:1", "2:163:8", "20:90:13", "21:112:6", "25:60:8", "27:30:7", "55:1:1", "59:22:12", "67:29:3", "78:37:6"]}, {"label": "Grammatical subject or actor in an action, statement, or condition", "count": 16, "refs": ["19:61:5", "19:75:8", "19:88:3", "19:92:3", "19:96:8", "20:5:1", "20:109:9", "21:26:3", "25:59:14", "36:15:9", "36:23:7", "36:52:10", "43:20:4", "43:81:4", "67:19:11", "78:38:12"]}, {"label": "Target, recipient, or reference point of an act or attitude", "count": 20, "refs": ["13:30:17", "17:110:6", "19:18:4", "19:26:13", "19:44:8", "19:69:9", "19:78:6", "19:85:5", "19:87:8", "19:91:3", "19:93:9", "20:108:9", "21:42:7", "25:60:5", "36:11:7", "43:17:6", "43:33:10", "43:45:11", "50:33:3", "67:20:10"]}, {"label": "Source, possessor, or object within a linked noun phrase", "count": 10, "refs": ["19:45:8", "19:58:26", "21:36:15", "25:26:4", "25:63:2", "26:5:6", "41:2:3", "43:19:6", "43:36:5", "67:3:10"]}], "dominant": "no dominant role", "outside": [], "collocates": ["ٱلرَّحِيم — the Merciful", "وَلَد — child", "عَبْد — servant", "ذِكْر — remembrance", "عَهْد — covenant", "رَبّ — Lord", "ٱسْتَوَىٰ — be established", "ٱلْعَرْش — the Throne", "خَشِيَ — fear", "بِٱلْغَيْبِ — unseen", "وَعَدَ — promise", "ٱللَّه — Allah", "سَجَدَ — prostrate", "شَفَاعَة — intercession", "إِلَٰه — god or deity", "اِتَّخَذَ — take or claim as"]}
every use: data/kwic/رحم_رحمن_1ab85f.md

### رَّحِيم — ر ح م — 116 uses in the Quran
use profile: {"root": "ر ح م", "lemma": "رَّحِيم", "total": 116, "groups": [{"label": "Describes Allah or the Lord", "count": 114, "refs": ["1:1:4", "2:37:11", "2:143:45", "2:173:25", "4:29:23", "26:9:5", "33:43:13", "34:2:17", "36:58:5", "41:32:4"]}, {"label": "Describes the messenger toward the believers", "count": 1, "refs": ["9:128:14"]}, {"label": "Describes believers' relation to one another", "count": 1, "refs": ["48:29:9"]}], "dominant": "Describes Allah or the Lord in 114 of 116 uses", "outside": [{"ref": "9:128:14", "how": "Applied to the messenger; بِٱلْمُؤْمِنِينَ names the group toward whom the quality is directed."}, {"ref": "48:29:9", "how": "Plural description of the believers, followed by بَيْنَهُمْ to describe their relation within the group."}], "collocates": ["ٱللَّه (Allah)", "رَبّ (Lord)", "غَفُور (forgiving)", "ٱلتَّوَّاب (accepting repentance)", "رَءُوف (compassionate)", "ٱلْعَزِيز (mighty)", "ٱلرَّحْمَٰن (merciful)", "ٱلْمُؤْمِنِينَ (believers)"]}
every use: data/kwic/رحم_رحيم_2436e2.md

## Variant readings

(none)

## Turkish loanword cards

- رَّحْمَٰن (ر ح م) → Rahman: today Allah’a verilen, çok merhametli oluşunu bildiren ad / Erkek adı. Reader hears: Allah’ın çok merhametli oluşunu bildiren ad. Drift: Türkçede çoğunlukla Allah’ın adı ve kişi adı olarak kullanılır; genel bir sıfat kullanımı sınırlıdır. Arabic keeps: B001 Arapçada kök, merhamet ve şefkat bildiren başka biçimleri de kapsar.; B002 Arapça kök ailesinde yakın akrabalık anlamı da bulunur.; B003 Arapça kök ailesi döl yatağı anlamını da içerir.
- رَّحِيم (ر ح م) → Rahîm: today Allah’ın çok merhametli oluşunu bildiren adı / Erkek adı. Reader hears: Allah’ın merhametli oluşunu bildiren ad. Drift: Türkçede başlıca ilahî ad ve kişi adı olarak kullanılır; gündelik sıfat kullanımı sınırlıdır. Arabic keeps: B001 Arapça kök ailesi merhamet, şefkat ve iyilik etmeyi de kapsar.; B002 Türkçedeki ilahî ad, Arapçanın yakın akrabalık anlamını taşımaz.
- رَّحِيم (ر ح م) → rahim: today Kadın üreme organı; döl yatağı. Reader hears: Döl yatağı. Drift: Türkçede anatomik anlamla yerleşmiştir; Arapça kök ailesindeki yakın akrabalık anlamı Türkçe rahim sözcüğünde yaygın değildir. Arabic keeps: B002 Arapçada rahim, yakın soy bağı ve akrabalık ilişkisini de anlatır. False friend: Rahim döl yatağıdır; Rahîm ise dinî kullanımda 'çok merhametli' anlamlı addır.
- رَّحِيم (ر ح م) → rahmet: today Merhamet, acıma ve esirgeme / İyilik, nimet veya bereket. Reader hears: Merhamet, lütuf veya nimet. Drift: Türkçede merhamet ve iyilik anlamlarında kullanılır; çoğu zaman dinî dilde Allah’ın lütfunu anlatır. Arabic keeps: B002 Arapçada aynı kök yakın akrabalık ve soy bağını da anlatır.; B003 Arapçada kök ailesi döl yatağı anlamını da içerir.
- رَّحِيم (ر ح م) → merhamet: today Acıma, şefkat ve iyilik etme duygusu. Reader hears: Şefkat veya acıma duygusu. Drift: Türkçede çoğunlukla bir kişiye karşı duyulan şefkat ve acımayı anlatır; dinî bağlam dışında da yaygındır. Arabic keeps: B002 Arapça kök ailesi yakın akrabalık anlamını da taşır.; B003 Arapça kök ailesinde döl yatağına ilişkin anlamlar da bulunur.

## Paths you may read

- classical entries per root: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/entries/<root letters without spaces>.md
- every use of a frequent lemma: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/kwic/
- the Quran text: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/quran.tsv; words: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/words.tsv; lemma index: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/lemmas.tsv
- the whole dictionary: /Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/branches.tsv
