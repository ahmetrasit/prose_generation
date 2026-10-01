Surah: 107. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (107:1 to 107:7), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/OZTURK/_projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/OZTURK/_projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

===== _commentary/v16/prompts/r13/surah_images.md =====
Write the Turkish commentary on the images of this surah for a curious reader
who knows neither Arabic nor how lexical families work, and who already has the
plain meaning. The map is an earlier reader's proposal: its chains, members,
passages and interactions are your material, not your verdicts. Correct a
member that does not hold, merge chains that are one image, and add what the
map missed from your own knowledge of Arabic and the Quran.

For each image:

- Show the scene through its operation: what the objects are, how they work,
  what the act does. Never flatten a mechanism into a label.
- Say what it makes perceptible in the surah that a plain paraphrase could not.
- Go through the surah in order and show what each ayah's words add to it.
- Bring in the Quran passages that stage it, with the speaker, the situation
  as the Quran itself tells it there and in the neighbouring ayat, and the
  wording the connection needs.

Then show where the images meet: a scene that holds two of them, and how
together they carry the surah's movement.

Develop every chain of the map, unless its members fail; a chain you leave out
goes in the ledger with its reason. A family image is heard beside the word's
meaning in its ayah, never in place of it; say so once. Keep root identity,
family images and your own connections distinct; an echo root does not
establish identity. Never invent a sense, source, citation or chronology. Use
no hadith, no exegetes' views and no report from outside the Quran (no occasion
of revelation, no name the Quran does not give, no date): the Quran, the map's
dictionary phrases and Arabic usage carry the commentary. Name
no dictionary or lexicographer in the prose, never mention the dictionary
("sözlük"), the map, its chains or your own process, and do not hedge in the
first person.

Write continuous prose: one `##` section per image, then a `## Buluşmalar`
section for the meetings; explain, do not dramatize; no lists and no closing
recap. Every Arabic quotation goes in the reader tag, and every tag ends with
its source, so the reader can check it:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning, source:…}
- a dictionary phrase or a branch's sense: source:"<root letters>,<branch id>",
  e.g. source:"ق و م,B016";
- a Quran quotation: source:<surah:ayah>, e.g. source:72:16, the one ayah that
  holds the quoted words, no ranges;
- Arabic from your own memory that is not in the map's dictionary phrases:
  source:"memory".
A branch's sense given in Turkish without its Arabic, and a Quran passage named
without quoting it, carry the source alone: {source:"ق و م,B016"},
{source:15:41}. Outside the `Kaynaklar:` lines, never write a Quran reference
outside a tag; quote the surah's own words in tags too, and name its ayat in
words ("dördüncü ayet"). End each image section with one line, `Kaynaklar:`, giving its
members as ayah, word, root and branch (e.g. 1:6 ٱلْمُسْتَقِيمَ ق و م B012).

Output: the prose; then a line containing only
=== LEDGER ===
then, in plain English, one short line per item, a few words each:
- not developed: <chain> - <why>
- memory: <a claim about Arabic that neither the map nor the Quran text can check>

===== _commentary/v16/work/s107/surah.r2/text.md =====
# Surah 107

- 107:1 أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ
- 107:2 فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ
- 107:3 وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 107:4 فَوَيْلٌۭ لِّلْمُصَلِّينَ
- 107:5 ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ
- 107:6 ٱلَّذِينَ هُمْ يُرَآءُونَ
- 107:7 وَيَمْنَعُونَ ٱلْمَاعُونَ


===== _commentary/v16/out/s107/surah.map3.nohft.tool/map.md (without ## Not carried) =====
## Chains

### 1. The summoned look and the courted look
The surah opens with an order to look: أَرَءَيْتَ. It asks the listener to turn his eyes onto "the one who denies the دين" and to report what he sees. It closes with men who arrange their acts so that other people's eyes fall on them: يُرَآءُونَ. Both words come from one root, so the surah is framed by two directions of seeing. The listener is made to see through the denier, while the denier's kind performs to be seen. Form III (مُفَاعَلَة) makes the seeing two-way: they watch the people, and the people watch them. Their prayer switches on and off with that exchange of looks. The mirror and the "good appearance" senses give the object of this seeing: a surface held up for eyes.
- 107:1 أَرَءَيْتَ — ر ء ي B013 — "يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه" (mufradat); "أرأيتك وأنت تقول أخبرني" (tahdhib) — the opening is a call to attention and a request for a report. The listener is made a witness.
- 107:1 أَرَءَيْتَ — ر ء ي B001 — "نظر وإبصار بعين أو بصيرة" (maqayis) — the look is with the eye and with insight: see the man, see what he is.
- 107:6 يُرَآءُونَ — ر ء ي B005 — "وفعل ذلك رئاء الناس وهو أن يفعل شيئا ليراه الناس" (maqayis); "يرآءون الناس إذا أبصرهم الناس صلوا وإذا لم يروهم تركوا الصلاة" (tahdhib) — the act is done for other people's sight. The tahdhib phrase puts the surah's رؤية and صلاة into one sentence: the prayer exists only while eyes are on it.
- 107:6 يُرَآءُونَ — ر ء ي B004 — "تراءى القوم إذا رأى بعضهم بعضا" (maqayis) — mutual seeing, the field of faces that the form-III verb sets up.
- 107:6 يُرَآءُونَ — ر ء ي B006 — "الري ما أريت القوم من حسن الشارة والهيئة" (ayn); "المرآة ما يرى فيه صورة الأشياء" (mufradat) — what is shown is a good outward bearing, a picture in a mirror.
- 107:6 يُرَآءُونَ — ر ء ي B012 — "رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها" (tahdhib) — holding up a mirror for someone to look into. The display is an object held up for eyes.
- Quran: 96:9-14. God speaks to the Prophet about a man who forbids a servant to pray. The scene opens at 96:9 "أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ" with 96:10 "عَبْدًا إِذَا صَلَّىٰٓ" and closes at 96:14 "أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ". It has the same أرأيت + الذي opening, set against prayer, and the one who truly sees is God.
- Quran: 26:218-219. God to the Prophet: "ٱلَّذِى يَرَىٰكَ حِينَ تَقُومُ وَتَقَلُّبَكَ فِى ٱلسَّٰجِدِينَ". The one praying is seen by God; this is the opposite of praying for people's eyes.
- Quran: 4:142. God describing the hypocrites: "وَإِذَا قَامُوٓا۟ إِلَى ٱلصَّلَوٰةِ قَامُوا۟ كُسَالَىٰ يُرَآءُونَ ٱلنَّاسَ".
- Quran: 2:264. God to the believers: one who spends "رِئَآءَ ٱلنَّاسِ" is like a smooth rock with soil on it, which a downpour leaves "صَلْدًا". Display in giving.
- Quran: 53:33-34. God to the Prophet: "أَفَرَءَيْتَ ٱلَّذِى تَوَلَّىٰ وَأَعْطَىٰ قَلِيلًا وَأَكْدَىٰٓ". The أرأيت opening is again aimed at a man who gives a little and then stops.
- Quran: 76:9. The righteous, feeding others: "إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءً وَلَا شُكُورًا". Feeding that looks away from human eyes. 92:18-20 is similar: the giver "مَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍ تُجْزَىٰٓ إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ".

### 2. The painted cloth: a surface that tells what is not underneath
A dyed cloth looks embroidered but has no embroidery; the dictionary says it "lies by its state". The prayer of 107:4-6 is the same kind of object: the outward form of standing and bowing is there, while the heart has left it and the act faces spectators. The تكذيب of 107:1 and the رياء of 107:6 meet in this one image: a surface that reports something false. The reversal comes from the root of the word that is denied: judging a man by his intention, the inside that the surface hides.
- 107:1 يُكَذِّبُ — ك ذ ب B009 — "الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله" (mufradat) — the cloth whose pattern lies.
- 107:1 يُكَذِّبُ — ك ذ ب B001 — "الكذب خلاف الصدق" (maqayis;jamhara); "يقال في المقال والفعال" (mufradat) — falsehood lies in deeds as well as words. A performed prayer can lie.
- 107:6 يُرَآءُونَ — ر ء ي B006 — "الرواء حسن المنظر" (ayn;sihah) — the handsome outside that is put on show.
- 107:5 صَلَاتِهِمْ — ص ل و B003 — "الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح" (tahdhib) — the visible parts of the prayer, the "pattern" that can be dyed on.
- 107:1 بِٱلدِّينِ — د ي ن B007 — "دينت الحالف أي نويته فيما حلف وهو التديين" (tahdhib); "دينت الرجل تديينا إذا وكلته إلى دينه" (sihah) — reversal: a man is judged by his intention and handed over to what is inside him, not to his surface.
- Quran: 2:264 (as above). A rock covered with soil and then washed bare is a staged surface over nothing.
- Quran: 98:5. "وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ ... وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ". Pure intention, prayer and the due together: the undyed cloth.

### 3. Overlooked: the orphan, the faint star, the heart gone from the act
Two definitions in the dictionary match word for word: "اليتم الغفلة" and "السهو الغفلة". On one account the orphan is named for the heedlessness of other people, who neglect to do him good, and for the slowness with which kindness reaches him. The ساهون are the heedless themselves, men whose heart has left their own prayer. Among the السهو words is a star so faint that people overlook it. So the scene is one of small, single things that the eye passes over: the lone orphan, the dim star, the forgotten prayer. Its reversal is a good overlooking, letting another man's slip pass, and the call that lifts a man who has stumbled.
- 107:2 ٱلْيَتِيمَ — ي ت م B003 — "أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره" (tahdhib); "اليتم الغفلة والتقصير" (jamhara) — the orphan is the one people turn their attention away from.
- 107:2 ٱلْيَتِيمَ — ي ت م B004 — "اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه" (tahdhib) — kindness is late to arrive at him.
- 107:2 ٱلْيَتِيمَ — ي ت م B002 — "كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة" (sihah) — alone, rare, a single pearl. The thing overlooked is precious.
- 107:2 ٱلْيَتِيمَ — ي ت م B001 — "انقطاع الصبي عن أبيه قبل بلوغه" (mufradat) — cut off from the father, the one who would have kept him in view.
- 107:5 سَاهُونَ — س ه و B001 — "السهو الغفلة عن الشيء وذهاب القلب عنه" (ayn) — the heart leaves the thing.
- 107:5 سَاهُونَ — س ه و B005 — "السها خفي جدا فيسهى عن رؤيته" (maqayis); "السها كويكب صغير" (ayn) — a tiny star missed by the eye. This phrase joins the surah's سهو and رؤية.
- 107:5 سَاهُونَ — س ه و B003 — "المساهاة حسن المخالقة" (maqayis;ayn); "كأن الإنسان يسهو عن زلة إن كانت من غيره" (maqayis) — reversal: overlooking another man's slip is good company. The surah's ساهون overlook the wrong thing.
- 107:2 يَدُعُّ — د ع ع B004 — "أن تقول للعاثر دع دع أي قم فانتعش" (sihah;tahdhib) — reversal: the call to someone who has stumbled to rise.
- Quran: 51:10-11. God on the conjecturers: "ٱلَّذِينَ هُمْ فِى غَمْرَةٍ سَاهُونَ". The same participle, describing men sunk heedless in a flood.
- Quran: 93:6, 93:9. God to the Prophet: "أَلَمْ يَجِدْكَ يَتِيمًا فَـَٔاوَىٰ ... فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ". The orphan is found and sheltered: seen, not passed over.
- From memory: tafsir notes that the ayah says عَن صَلَاتِهِمْ, not فِي صَلَاتِهِمْ. Heedlessness *from* the prayer is blamed; a lapse *in* it is human. Compare 23:2 "ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ" (quoted from memory) and the dictionary's "سها الرجل في صلاته إذا غفل عن شيء منها" (ayn).

### 4. A course that does not hold
Several senses of ك ذ ب name a beginning that its continuation fails to bear out. A charge stops short of the strike. A she-camel's milk, expected to last, dries up. A wild animal runs one stretch, stops and looks back. The orphan's root adds a pace that slows down. The surah's prayer follows this shape: it is begun, but the heart leaves it, and according to the tahdhib it is dropped once no one is watching. The reversal is in the same root: charging without stopping until the blow lands, acting without delay. The ر ء ي root gives the truthful counterpart: the she-camel whose udder shows that her pregnancy is real.
- 107:1 يُكَذِّبُ — ك ذ ب B004 [fixed expression] — "حمل فلان ثم كذب أي لم يصدق في الحملة" (maqayis) — a charge that does not carry through.
- 107:1 يُكَذِّبُ — ك ذ ب B006 [fixed expression] — "كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم" (mufradat) — nourishment that was expected and then stopped.
- 107:1 يُكَذِّبُ — ك ذ ب B007 [fixed expression] — "كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه" (jamhara) — running, halting, looking back.
- 107:1 يُكَذِّبُ — ك ذ ب B004/B005 [fixed expression] — "حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف" (jamhara); "ما كذب فلان أن فعل كذا أي ما لبث" (maqayis;sihah) — reversal: no stopping, no delay.
- 107:1 أَرَءَيْتَ — ر ء ي B010 — "أرأت الناقة إذا أظهرت الحمل حتى يرى صدق حملها" (mufradat) — reversal on the same animal: the swollen udder shows the "truth" (صدق) of what it holds. Set against "كذب لبن الناقة" in the same source.
- 107:2 ٱلْيَتِيمَ — ي ت م B004 — "في سيره يتم أي إبطاء" (sihah) — a pace that drags.
- 107:5 سَاهُونَ — س ه و B001 — "سها الرجل في صلاته إذا غفل عن شيء منها" (ayn) — part of the act is dropped along the way.
- 107:6 يُرَآءُونَ — ر ء ي B005 — "إذا أبصرهم الناس صلوا وإذا لم يروهم تركوا الصلاة" (tahdhib) — the prayer breaks off when the eyes leave.
- Quran: 53:34. "وَأَعْطَىٰ قَلِيلًا وَأَكْدَىٰٓ". Giving that begins and then stops, under an أفرأيت opening (53:33).
- Quran: 70:23. In contrast, "ٱلَّذِينَ هُمْ عَلَىٰ صَلَاتِهِمْ دَآئِمُونَ": a prayer that holds its course.

### 5. Hands on the dependent: shove away, urge toward, call up, bar, shelter
107:2-3 sets a series of motions on the bodies of the weak. يَدُعُّ is a hard, rough shove that sends the orphan away from the door. يَحُضُّ, which this man fails to do, is the push in the other direction: driving others toward the food. In the same root as the shove, دعدعة is the shepherd's driving cry, and دع دع is the call that gets a stumbler back on his feet. 107:7 adds the barrier, standing between a man and what he wants. The reversal is the protecting band of kin who surround and defend him. The orphan has lost his منعة with his father, and the men who could be that protection use منع to keep things back.
- 107:2 يَدُعُّ — د ع ع B001 — "الدفع الشديد" (mufradat); "دفع في جفوة" (ayn) — a hard push, done roughly.
- 107:2 يَدُعُّ — د ع ع B003 — "الدعدعة زجر الغنم" (maqayis) — driving and scolding a flock. The orphan is driven off like animals.
- 107:2 يَدُعُّ — د ع ع B004 — "أن تقول للعاثر دع دع أي قم فانتعش" (sihah;tahdhib) — reversal: the same sound used to lift someone who has fallen.
- 107:3 يَحُضُّ — ح ض ض B001 — "حض يحض حضا وهو الحث على الخير" (tahdhib); "حضه على القتال حضا أي حثه وحضضه أي حرضه والتحاض التحاث والمحاضة أن يحث كل واحد منهما صاحبه" (sihah) — the push toward the good. Its reciprocal form has people urging one another along.
- 107:7 وَيَمْنَعُونَ — م ن ع B002 — "المنع أن تحول بين الرجل وبين الشيء الذي يريده" (tahdhib) — the body put between the needy man and the thing he wants.
- 107:7 وَيَمْنَعُونَ — م ن ع B003 — "المنعة جمع مانع أي من يمنعه من عشيرته" (sihah); "يحوطهم وينصرهم" (tahdhib) — reversal: men who form a protective ring around someone. This is what the fatherless child lacks.
- Quran: 52:13. The day of judgment: "يَوْمَ يُدَعُّونَ إِلَىٰ نَارِ جَهَنَّمَ دَعًّا". The shovers are themselves shoved, toward the fire.
- Quran: 89:17-18. God rebuking: "كَلَّا بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ". The same pair: orphan, then urging food for the poor. The form تحاضّون is mutual.
- Quran: 93:9-10. God to the Prophet: "فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ". Do not force or rebuff.
- Quran: 4:37. God on the misers: "ٱلَّذِينَ يَبْخَلُونَ وَيَأْمُرُونَ ٱلنَّاسَ بِٱلْبُخْلِ". The urging turned around, pushing others toward holding back.
- Quran: 68:17, 68:24. The garden owners swear to harvest at dawn, "أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌ". A barrier put up against the poor.

### 6. The house: its little ones, its people, its goods on the rack
Under the surface sits a household. The root of the shove names a man's small children, and the more of them he has, the more is asked of him. The root of the poor man names the house, the household and the provisions that let it stay in place. The root of ماعون names the dwelling and its everyday implements: axe, pot, bucket, bowl, knife, mat, the things that are lent. The root of ساهون names the porch in front of the house and the rack of sticks where goods are stored. The orphan is a child outside any such house. The men of 107:7 keep the house's lendable things on their rack.
- 107:2 يَدُعُّ — د ع ع B009 — "الدعاع عيال الرجل الصغار؛ أدع الرجل إذا كثر دعاعه" — the small dependents a man must keep. The shove's root names the very children owed care.
- 107:2 ٱلْيَتِيمَ — ي ت م B001 — "اليتيم الذي مات أبوه حتى يبلغ" (tahdhib) — the child whose provider has died.
- 107:3 ٱلْمِسْكِينِ — س ك ن B002 — "سكنت داري وأسكنتها غيرى" — living in a house, and lodging another person in it.
- 107:3 ٱلْمِسْكِينِ — س ك ن B003 — "السكن جزم العيال وهم أهل البيت"; "السكن أهل الدار" — the people of the house.
- 107:3 ٱلْمِسْكِينِ — س ك ن B010 — "قيل للقوت سكن لأن المكان به يسكن" — the food that lets a household stay where it is.
- 107:5 سَاهُونَ — س ه و B004 — "السهوة أربعة أعواد أو ثلاثة يعارض بعضها على بعض يوضع عليها شيء من الأمتعة" (ayn); "السهوة وهي كالصفة تكون أمام البيت" (maqayis) — the porch and the storage rack.
- 107:7 ٱلْمَاعُونَ — م ع ن B005 — "ويقال هو أسقاط البيت نحو الفأس والقدر والدلو" (ayn); "الماعون اسم جامع لمنافع البيت" (sihah); "كل ما يستعار من قدوم وسفرة وشفرة" (tahdhib) — the small working goods of the house, the kind that are lent.
- 107:7 ٱلْمَاعُونَ — م ع ن B006 — "المعان المباءة والمنزل" (sihah) — the dwelling itself.
- 107:7 ٱلْمَاعُونَ — م ع ن B003 — "المعن الشيء اليسير الهين" (sihah) — small and easy to give. That makes the withholding sharper.
- 107:7 وَيَمْنَعُونَ — م ن ع B001 — "رجل منوع ومناع إذا كان بخيلا ممسكا" (tahdhib) — the hand that keeps hold.
- Quran: 93:6. "أَلَمْ يَجِدْكَ يَتِيمًا فَـَٔاوَىٰ". The orphan taken into shelter.
- Quran: 90:11-16. The steep pass (opens 90:11 "فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ"): "أَوْ إِطْعَٰمٌ فِى يَوْمٍ ذِى مَسْغَبَةٍ يَتِيمًا ذَا مَقْرَبَةٍ أَوْ مِسْكِينًا ذَا مَتْرَبَةٍ". An orphan of one's own kin, a poor man in the dust.

### 7. Bowl, pot and the measure shaken full
The objects of feeding are vessels. One sense in the shove's root is shaking a measure or sack until it is packed to the top, and a great serving bowl filled to the brim. The bowl, pot and bucket are named again as ماعون. طعام is whatever is eaten, and its giving extends to water. The host is "the great giver of hospitality". In this scene the surah's men hold the pot and the bowl back while the orphan is pushed away from the door. The same root that gives "shove" gives "fill the bowl to overflowing".
- 107:2 يَدُعُّ — د ع ع B002 — "دعدعت الشيء ملأته وجفنة مدعدعة" (sihah); "دعدع مكيالا أو جوالقا حتى يكتنز" (tahdhib); "الدعدعة تحريك المكيال ليستوعب الشيء" (maqayis) — the bowl filled up, the measure shaken full.
- 107:3 طَعَامِ — ط ع م B001 — "الطعم ذوقه والطعام اسم جامع لكل ما يؤكل" (ayn) — what goes into the bowl.
- 107:3 طَعَامِ — ط ع م B002 — "استطعمه سأله أن يطعمه وأطعمته الطعام" (sihah); "استطعمه فأطعمه وأطعموا القانع ويطعمون الطعام" (mufradat) — asking to be fed, and feeding.
- 107:3 طَعَامِ — ط ع م B004 — "رجل طاعم حسن الحال ومطعام كثير القرى" (maqayis) — the host known for his hospitality.
- 107:7 ٱلْمَاعُونَ — م ع ن B005 — "الماعون المعروف كله والقصعة والقدر والفأس" (tahdhib) — bowl and pot, named as the decency that is owed.
- 107:7 وَيَمْنَعُونَ — م ن ع B001 — "خلاف الإعطاء" (maqayis;sihah) — the vessel not handed over.
- Quran: 76:8. "وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًا وَيَتِيمًا وَأَسِيرًا". The full bowl given to the same recipients.
- Quran: 74:44. The criminals in Saqar: "وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ".
- Quran: 36:47. The disbelievers: "أَنُطْعِمُ مَن لَّوْ يَشَآءُ ٱللَّهُ أَطْعَمَهُۥٓ". The bowl refused, with an argument.
- Quran: 83:1-3 (opens 83:1 "وَيْلٌ لِّلْمُطَفِّفِينَ"). Woe to those who short the measure. The measure that is not shaken full sits under the same woe.

### 8. Water: running, lent, held back
The root of ماعون names running water and the channels of a valley that carry it. It also names land soaked by that water and pasture through which it runs. The dictionary says water itself is called ماعون. The giving of طعام includes water. The root of مسكين names pasture rich enough that a herd need not move on. So the scene is water flowing down to a place where people and herds can settle, and the men of 107:7 holding back even this.
- 107:7 ٱلْمَاعُونَ — م ع ن B001 — "ماء معين أي جار" (maqayis;sihah;tahdhib); "المعنان مجاري الماء في الوادي" (maqayis;sihah); "أمعنت الأرض رويت وكلأ ممعون جرى فيه الماء" (maqayis;sihah;tahdhib) — water running in channels and soaking the ground.
- 107:7 ٱلْمَاعُونَ — م ع ن B005 — "يسمى الماء أيضا ماعونا" (sihah) — the withheld thing is water too.
- 107:3 طَعَامِ — ط ع م B001 — "أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء" (maqayis) — feeding reaches as far as giving water.
- 107:3 ٱلْمِسْكِينِ — س ك ن B010 — "مرعى مسكن إذا كان كثيرا لا يخرج إلى الظعن عنه" — pasture that lets a herd stay.
- 107:7 وَيَمْنَعُونَ — م ن ع B001 — "مناع للخير" (tahdhib;mufradat) — the one who keeps the good back.
- Quran: 67:30. God tells the Prophet to say: "أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًا فَمَن يَأْتِيكُم بِمَآءٍ مَّعِينٍ". أرأيتم and معين in one ayah: look, and see who supplies the running water.
- Quran: 23:50. Mary and her son "وَءَاوَيْنَٰهُمَآ إِلَىٰ رَبْوَةٍ ذَاتِ قَرَارٍ وَمَعِينٍ". Running water with a place of settled rest; refuge given to a mother and a fatherless child.
- From memory: the hadith, reported from Aisha in Ibn Majah, that names the things it is not lawful to withhold as water, salt and fire.

### 9. Hearth and burning
The root of المصلين and صلاتهم also names fire. It means warming oneself at a fire, roasting meat, the fuel, straightening a stick over the flame, and being thrown into fire and suffering its heat. The word for those who pray is the same root that names the fire. So 107:4 "فَوَيْلٌ لِّلْمُصَلِّينَ" lets the listener hear the heat that woe brings, falling on the very men named for prayer. In a home the fire is a hearth that comforts and cooks, the fire you settle beside. The men who keep back the household's goods turn the hearth sense into the burning sense.
- 107:4 لِّلْمُصَلِّينَ / 107:5 صَلَاتِهِمْ — ص ل و B001 — "الصلا النار وصلى الكافر نارا" (ayn); "صلي بالأمر إذا قاسى حره وشدته" (sihah;tahdhib) — being exposed to the fire and suffering its heat.
- same — ص ل و B001 — "اصطليت بالنار" (maqayis;sihah); "صليت اللحم شويته" (ayn;sihah;tahdhib); "الصلاء يقال للوقود وللشواء" (mufradat) — the hearth: warmth, fuel, roast meat.
- same — ص ل و B001 — "صليت العود بالنار" (maqayis) — fire that straightens a crooked stick.
- 107:3 ٱلْمِسْكِينِ — س ك ن B004 — "السكن النار التي يسكن بها" — the fire one settles beside.
- 107:4 فَوَيْلٌ — not in the dictionary. From memory: woe, ruin, a cry of disaster.
- Quran: 69:25-34. The man given his book in his left hand (opens 69:25). The command comes at 69:30-31, "خُذُوهُ فَغُلُّوهُ ثُمَّ ٱلْجَحِيمَ صَلُّوهُ", and the reason at 69:33-34, "إِنَّهُۥ كَانَ لَا يُؤْمِنُ بِٱللَّهِ ٱلْعَظِيمِ وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ". The form-II صلّوه is the fire sense of the surah's مصلّين, set against not urging food.
- Quran: 74:40-46. The people of the gardens ask "مَا سَلَكَكُمْ فِى سَقَرَ" (74:42). The answer is "لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ ... وَكُنَّا نُكَذِّبُ بِيَوْمِ ٱلدِّينِ". The surah's vocabulary, spoken from inside the fire.
- Quran: 83:10-11, 83:16-17. "وَيْلٌ يَوْمَئِذٍ لِّلْمُكَذِّبِينَ ٱلَّذِينَ يُكَذِّبُونَ بِيَوْمِ ٱلدِّينِ ... ثُمَّ إِنَّهُمْ لَصَالُوا۟ ٱلْجَحِيمِ ثُمَّ يُقَالُ هَٰذَا ٱلَّذِى كُنتُم بِهِۦ تُكَذِّبُونَ". Woe, denial of the دين, and صَالُو, all together.
- Quran: 92:14-16. "لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ". Opened at 92:8: "وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ وَكَذَّبَ بِٱلْحُسْنَىٰ".
- Quran: 4:10. "إِنَّ ٱلَّذِينَ يَأْكُلُونَ أَمْوَٰلَ ٱلْيَتَٰمَىٰ ظُلْمًا إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًا وَسَيَصْلَوْنَ سَعِيرًا". Orphan, food and fire in one ayah.
- Quran: 50:24-25. "أَلْقِيَا فِى جَهَنَّمَ كُلَّ كَفَّارٍ عَنِيدٍ مَّنَّاعٍ لِّلْخَيْرِ". The withholder thrown into the fire.

### 10. The due: debt, account, obedience, acknowledgment
الدين is what is owed: a debt between people, the reckoning and payment of deeds, and submission. Denying it means calling the creditor a liar. The surah closes on the ماعون, and the dictionary glosses both the first object and the last with one word, الطاعة. Under م ع ن it also records two opposite things done with a right: carrying it off, and acknowledging it and yielding. The verb اِنْقَادَ is the one Ibn Fāris uses to define الدين. So the surah moves from denying the account in 107:1 to keeping the small due in 107:7. In between, the orphan's claim is pushed away and the poor man's food goes unasked for.
- 107:1 بِٱلدِّينِ — د ي ن B002 — "يوم الدين أي يوم الحكم والحساب والجزاء" (maqayis); "الدين الجزاء والمكافأة" (sihah) — the account settled and paid.
- 107:1 بِٱلدِّينِ — د ي ن B003 — "داينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء" (maqayis); "دنت الرجل أقرضته" (tahdhib) — lending and owing.
- 107:1 بِٱلدِّينِ — د ي ن B001 — "أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل" (maqayis); "فالدين الطاعة" (maqayis;sihah) — yielding.
- 107:1 يُكَذِّبُ — ك ذ ب B002 — "كذبت فلانا نسبته إلى الكذب" (maqayis); "كذبت بالحديث كذابا وتكذيبا" (jamhara) — treating the report of the account as a lie.
- 107:1 يُكَذِّبُ — ك ذ ب B003 [fixed expression] — "كذب عليكم الحج أي وجب" (sihah); "كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك" (maqayis) — reversal inside the denier's own verb: "it is due upon you".
- 107:7 ٱلْمَاعُونَ — م ع ن B005 — "الماعون في الجاهلية كل منفعة وعطية وفي الإسلام الطاعة والزكاة" (sihah); "الماعون الطاعة" (tahdhib); "الماعون يفسر بالزكاة والصدقة" (ayn) — the small due and the alms.
- 107:7 ٱلْمَاعُونَ — م ع ن B004 — "أمعن بحقي ذهب به" (maqayis;sihah); "أمعن لي بحقي إذا أقر به وانقاد" (tahdhib) — making off with a right, or acknowledging it and yielding.
- 107:7 وَيَمْنَعُونَ — م ن ع B001 — "ضد العطية" (mufradat) — the due held back.
- Quran: 82:9. God to man: "كَلَّا بَلْ تُكَذِّبُونَ بِٱلدِّينِ". The exact phrase.
- Quran: 70:19-26. Man "إِذَا مَسَّهُ ٱلْخَيْرُ مَنُوعًا إِلَّا ٱلْمُصَلِّينَ ٱلَّذِينَ هُمْ عَلَىٰ صَلَاتِهِمْ دَآئِمُونَ وَٱلَّذِينَ فِىٓ أَمْوَٰلِهِمْ حَقٌّ مَّعْلُومٌ لِّلسَّآئِلِ وَٱلْمَحْرُومِ وَٱلَّذِينَ يُصَدِّقُونَ بِيَوْمِ ٱلدِّينِ". A point-by-point reversal of the surah: منوع, the مصلين, prayer kept up, the known right, and affirming the دين.
- Quran: 41:6-7. "وَوَيْلٌ لِّلْمُشْرِكِينَ ٱلَّذِينَ لَا يُؤْتُونَ ٱلزَّكَوٰةَ وَهُم بِٱلْءَاخِرَةِ هُمْ كَٰفِرُونَ". Woe, the due withheld, the account denied.
- Quran: 1:4. "مَٰلِكِ يَوْمِ ٱلدِّينِ" (cited in the dictionary, tahdhib).

### 11. Prayer turned outward: blessing that gives rest
The ص ل و root gives prayer as the set rite of standing, bowing and prostrating. It also gives prayer as a blessing asked for another person: the Prophet's prayer for the Muslims, God's mercy. One dictionary phrase, quoting 9:103, joins two of the surah's roots: the Prophet's صلاة over those who pay their alms is a سكن for them, a rest. So prayer, alms and the poor man's root belong to one movement: give the due, receive a prayer, find rest. The surah's men keep the outward rite, cut the prayer off from giving, and withhold the ماعون.
- 107:4 لِّلْمُصَلِّينَ / 107:5 صَلَاتِهِمْ — ص ل و B003 — "الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة" (maqayis) — the rite.
- same — ص ل و B002 — "الصلاة وهي الدعاء" (maqayis;sihah); "صلوات الرسول للمسلمين دعاؤه لهم" (ayn); "صلاة الله للمسلمين تزكيته إياهم" (mufradat) — prayer aimed at someone else's good.
- 107:3 ٱلْمِسْكِينِ — س ك ن B004 — "إن صلواتك سكن لهم"; "كل ما سكنت إليه من محبوب" — the rest that prayer gives. The phrase joins ص ل و and س ك ن.
- 107:7 ٱلْمَاعُونَ — م ع ن B005 — "الماعون يفسر بالزكاة والصدقة" (ayn) — the alms that this prayer answers.
- Quran: 9:103. God to the Prophet: "خُذْ مِنْ أَمْوَٰلِهِمْ صَدَقَةً تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا وَصَلِّ عَلَيْهِمْ إِنَّ صَلَوٰتَكَ سَكَنٌ لَّهُمْ".
- Quran: 98:5. The prayer and the zakat ordered together under "مُخْلِصِينَ لَهُ ٱلدِّينَ".
- Quran: 9:54. God on the hypocrites: "وَمَا مَنَعَهُمْ أَن تُقْبَلَ مِنْهُمْ نَفَقَٰتُهُمْ ... وَلَا يَأْتُونَ ٱلصَّلَوٰةَ إِلَّا وَهُمْ كُسَالَىٰ وَلَا يُنفِقُونَ إِلَّا وَهُمْ كَٰرِهُونَ". Lazy prayer and reluctant giving, held together by منع.
- Quran: 19:59. "أَضَاعُوا۟ ٱلصَّلَوٰةَ وَٱتَّبَعُوا۟ ٱلشَّهَوَٰتِ". Prayer let go.

### 12. Stillness and the low ground
The poor man's root means the end of movement and settling in place. The poor man is the one whom need has made still and humbled. The dictionary glosses سهو itself as السكون, stillness. The root of يحض names the bottom of the land at the foot of a mountain. The دين root holds being brought low and made subject. So the scene has a body lying low and unmoving on the ground and a heart gone still in prayer. Against them stand the push that should urge others toward food, and the call that lifts the stumbler.
- 107:3 ٱلْمِسْكِينِ — س ك ن B001 — "السكون ذهاب الحركة"; "استقر وثبت" — movement gone, settled in place.
- 107:3 ٱلْمِسْكِينِ — س ك ن B006 — "المسكين الفقير وقد يكون بمعنى الذلة والضعف"; "تمسكن إذا خضع لله وهي المسكنة للذلة" — poverty that lowers and weakens.
- 107:5 سَاهُونَ — س ه و B002 — "السهو السكون؛ جاء سهوا رهوا" — the dictionary defines the heedless word with the poor man's root: stillness.
- 107:3 يَحُضُّ — ح ض ض B002 — "الحضيض قرار الأرض عند سفح الجبل" (ayn;tahdhib) — the lowest resting ground.
- 107:1 بِٱلدِّينِ — د ي ن B004 — "دانه دينا أي أذله واستعبده" (sihah) — brought low and made subject.
- 107:2 يَدُعُّ — د ع ع B004 — "أن تقول للعاثر دع دع أي قم فانتعش" (sihah;tahdhib) — the upward call, the reversal.
- Quran: 90:16. "أَوْ مِسْكِينًا ذَا مَتْرَبَةٍ". The poor man lying in the dust, inside the steep-pass scene that opens at 90:11.
- Quran: 23:50. "ذَاتِ قَرَارٍ وَمَعِينٍ". Settled rest given as shelter.

## Interactions
- Chains 1 and 3: ر ء ي and س ه و meet in one dictionary phrase, "السها خفي جدا فيسهى عن رؤيته" (maqayis). Courting the eye and missing the faint thing are one field of sight.
- Chains 1 and 11: the tahdhib phrase for يُرَآءُونَ, "إذا أبصرهم الناس صلوا وإذا لم يروهم تركوا الصلاة", joins seeing and prayer. 96:9-14 stages أرأيت, prayer and God's seeing together.
- Chains 1 and 7: 76:8-9 puts feeding the miskin and orphan beside "لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءً وَلَا شُكُورًا". Feeding with no eye on the audience is the opposite of رياء.
- Chains 1 and 8: 67:30 has "أَرَءَيْتُمْ" and "بِمَآءٍ مَّعِينٍ" in one ayah. Seeing is directed at the running water that is ماعون.
- Chains 1 and 4: 53:33-34 has أفرأيت aimed at a man who "أَعْطَىٰ قَلِيلًا وَأَكْدَىٰٓ", giving that breaks off.
- Chains 2 and 4: ك ذ ب joins them. The lying cloth (B009) and the lying milk and charge (B004, B006) are one root's surface falsehood and broken course. يقال في المقال والفعال (mufradat).
- Chains 2 and 10: د ي ن B007 (judging by intention) and 98:5 "مُخْلِصِينَ لَهُ ٱلدِّينَ". The دين that is denied is the one that reads the inside of the act.
- Chains 3 and 5: د ع ع B004 "دع دع أي قم فانتعش" is the lifting call in chain 5 and the good counterpart to overlooking in chain 3. The orphan's name for neglect (ي ت م B003) is what the shove acts out.
- Chains 3 and 12: س ه و is defined both as الغفلة and as السكون. The heedless heart and the still poor man share a gloss.
- Chains 5 and 6: د ع ع holds both the shove (B001) and a man's small dependents (B009). م ن ع holds both the withholding hand (B001) and the protecting kin (B003) the fatherless child lacks.
- Chains 5 and 7: د ع ع B001 shove and B002 the bowl shaken full sit in one root. 89:17-18 and 69:34 stage "يحض على طعام المسكين" as the opposite of rebuffing the orphan.
- Chains 5 and 9: 52:13 "يُدَعُّونَ إِلَىٰ نَارِ جَهَنَّمَ دَعًّا" turns the shove onto the shover and sends him into the fire. 69:31-34 sets صَلُّوهُ beside "لَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ".
- Chains 6 and 7: م ع ن B005 names the household's pot, bowl, axe and bucket. The house of chain 6 and the vessels of chain 7 are the same objects.
- Chains 6 and 8: س ك ن B010, the food and pasture that let people stay, and م ع ن B006 dwelling with B001 running water. Settling depends on water and food.
- Chains 7 and 9: ص ل و B001 "الصلاء يقال للوقود وللشواء" and س ك ن B004 "السكن النار التي يسكن بها". The hearth cooks what the pot holds. 4:10 joins eating orphans' wealth with "سَيَصْلَوْنَ سَعِيرًا".
- Chains 9 and 10: 83:10-17 has ويل, "يُكَذِّبُونَ بِيَوْمِ ٱلدِّينِ" and "لَصَالُوا۟ ٱلْجَحِيمِ". 74:43-46 has المصلين, feeding the miskin and denying the Day of Din. Both set the whole surah inside the fire.
- Chains 10 and 11: 70:19-26 stages منوع, المصلين "عَلَىٰ صَلَاتِهِمْ دَآئِمُونَ", the known right in wealth, and "يُصَدِّقُونَ بِيَوْمِ ٱلدِّينِ" together. 9:103 joins the alms (ماعون as الزكاة) with صلاة.
- Chains 11 and 12: the س ك ن B004 phrase "إن صلواتك سكن لهم" joins prayer with the poor man's root. The rest that prayer gives is the opposite of the stillness of neglect.
- Chain 10 within itself: د ي ن B001 "جنس من الانقياد" and م ع ن B004 "أقر به وانقاد" share انقاد. The sihah/tahdhib "الطاعة" glosses both الدين and الماعون, the first and last objects of the surah.

## Ayat
- **107:1 أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ**
  - Chain 1: أَرَءَيْتَ is the summoned look, "tell me, look". Scene: the listener is made to look at a man whose kind, at the end, act only for people's eyes; the true seer is God.
  - Chain 2: يُكَذِّبُ carries the cloth whose dye lies; بِٱلدِّينِ carries judging by intention. Scene: a prayer standing as a dyed pattern over an empty inside, judged by what lies under it.
  - Chain 4: يُكَذِّبُ is the charge that stops and the milk that dries [fixed expressions], and أَرَءَيْتَ is the udder that shows its truth. Scene: a course begun (charge, milk, prayer) that does not hold, set against the one that does.
  - Chain 10: بِٱلدِّينِ is debt, account and submission, and يُكَذِّبُ is calling the creditor a liar, with "كذب عليك" = it is due on you [fixed expression]. Scene: the account is denied at the start and the small due is kept back at the end.
  - Chain 12: بِٱلدِّينِ is being brought low. Scene: the poor lying low and still, the heart still in prayer, the call to rise.
- **107:2 فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ**
  - Chain 5: يَدُعُّ is the rough shove and the herding cry; its دع دع is the lifting call. Scene: hands on the dependent — shoved away, not urged toward food, barred, with no protecting kin.
  - Chain 3: ٱلْيَتِيمَ is the one named for others' neglect, kindness slow to reach him, a single pearl. Scene: the orphan, the faint star and the prayer are all passed over by heedless eyes.
  - Chain 6: يَدُعُّ names a man's small dependents; ٱلْيَتِيمَ is the child whose provider has died. Scene: a house with its children, its people and its lendable goods on the rack, and the orphan outside it.
  - Chain 7: يَدُعُّ is also the bowl shaken full. Scene: pot and bowl kept back while the measure could be filled to the brim.
  - Chain 4: ٱلْيَتِيمَ is a dragging pace. Scene: a course that slows and breaks off.
- **107:3 وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ**
  - Chain 5: يَحُضُّ is the push toward the good, people urging one another. Scene: the orphan shoved away and the poor man's food not urged.
  - Chain 7: طَعَامِ is whatever is eaten, feeding, the generous host. Scene: feeding vessels — the full bowl, the pot — held back.
  - Chain 8: طَعَامِ reaches as far as water; ٱلْمِسْكِينِ is pasture that lets a herd stay. Scene: running water and settling, kept back.
  - Chain 6: ٱلْمِسْكِينِ is the house, its people and the food that lets them stay. Scene: the household and its goods.
  - Chain 9: ٱلْمِسْكِينِ is the fire one settles beside. Scene: the hearth's warmth turns into the fire of woe.
  - Chain 11: ٱلْمِسْكِينِ is the rest (سكن) that prayer gives. Scene: alms answered by a prayer that brings rest.
  - Chain 12: ٱلْمِسْكِينِ is stillness and lowness, and يَحُضُّ names the lowest ground. Scene: the poor man in the dust, the heart gone still.
- **107:4 فَوَيْلٌ لِّلْمُصَلِّينَ**
  - Chain 9: لِّلْمُصَلِّينَ carries the root's fire: warming, roasting, exposure to burning; ويل (from memory) is ruin. Scene: the name of those who pray sounds the fire their woe brings.
  - Chain 11: لِّلْمُصَلِّينَ is those who perform the rite and whose prayer should be blessing for others. Scene: prayer cut off from the alms and the rest it should bring.
  - Chain 1: prayer as an act for eyes. Scene: the summoned look and the courted look.
- **107:5 ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ**
  - Chain 3: سَاهُونَ is the heart gone from the thing, the faint star missed by the eye; reversed, overlooking a friend's slip. Scene: the overlooked orphan and the forgotten prayer.
  - Chain 12: سَاهُونَ = السكون. Scene: stillness of the poor body and the absent heart.
  - Chain 6: سَاهُونَ names the porch and the storage rack. Scene: house goods stacked on the rack, not lent.
  - Chain 4: a lapse in part of the prayer, عن rather than في (from memory). Scene: a course begun and dropped.
  - Chain 2 and Chain 9: صَلَاتِهِمْ is the visible rite and the root's fire. Scenes: the painted surface, and the hearth that turns to burning.
- **107:6 ٱلَّذِينَ هُمْ يُرَآءُونَ**
  - Chain 1: يُرَآءُونَ is acting for people's sight, mutual looking, the mirror held up. Scene: the listener summoned to look, the hypocrites courting eyes, God who sees.
  - Chain 2: يُرَآءُونَ is the handsome outside. Scene: the dyed cloth that lies by its state.
  - Chain 4: in the tahdhib, prayer dropped when unseen. Scene: a course that holds only under eyes.
- **107:7 وَيَمْنَعُونَ ٱلْمَاعُونَ**
  - Chain 6: ٱلْمَاعُونَ is the house's axe, pot, bucket and dwelling, small and easy to give; وَيَمْنَعُونَ is the tight-fisted hand. Scene: the household's lendable goods kept on the rack while the orphan is outside.
  - Chain 7: bowl and pot are not handed over. Scene: feeding vessels, the bowl that could be shaken full.
  - Chain 8: ٱلْمَاعُونَ is running water and water itself. Scene: water flowing down to settled pasture, kept back.
  - Chain 10: ٱلْمَاعُونَ is الطاعة and الزكاة, and a right carried off or acknowledged. Scene: the account denied at the start, the due withheld at the end.
  - Chain 5: وَيَمْنَعُونَ is standing between a man and what he wants, and, reversed, the protecting kin. Scene: shove, no urging, barrier.
  - Chain 11: the alms that prayer should answer. Scene: prayer, alms and rest belong together; here they are pulled apart.

