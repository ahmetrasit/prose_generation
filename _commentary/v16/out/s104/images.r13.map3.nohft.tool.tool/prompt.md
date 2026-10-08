Surah: 104. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (104:1 to 104:9), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s104/surah.r2/text.md =====
# Surah 104

- 104:1 وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ
- 104:2 ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ
- 104:3 يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ
- 104:4 كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ
- 104:5 وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ
- 104:6 نَارُ ٱللَّهِ ٱلْمُوقَدَةُ
- 104:7 ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ
- 104:8 إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ
- 104:9 فِى عَمَدٍۢ مُّمَدَّدَةٍۭ


===== _commentary/v16/out/s104/surah.map3.nohft.tool/map.md (without ## Not carried) =====
# Surah 104: map of image chains

## Chains

### 1. The pressing hand: squeeze, push, fist, throw, break

In the dictionary, هُمَزَة and لُمَزَة both begin as bodily pressure. The hand squeezes things in the palm, hard enough to crack nuts, and it pushes and strikes. The same hand closes into a fist on what it gathers (جمع الكف, a fistful). Then the movement reverses. The man becomes the thing "thrown from the hand" (نبذ) into the breaker of dry, hard things (حطم). The presser is pressed. The surah runs this as one movement: pressing (104:1), gathering (104:2), being thrown (104:4), breaking (104:4–5).

- 104:1 هُمَزَةٍ — ه م ز B001 — «تدل على ضغط وعصر» (maqayis); «همزت الشيء في كفي» (maqayis;sihah;mufradat); «همزت رأسه وهمزت الجوز بكفي» (tahdhib) — the hand as a press that crushes a head or cracks nuts in the palm.
- 104:1 هُمَزَةٍ — ه م ز B003 — «همزه أي دفعه وضربه» (sihah); «كل شيء دفعته فقد همزته» (tahdhib) — the push and the blow.
- 104:1 هُمَزَةٍ / لُّمَزَةٍ — ه م ز B003 and ل م ز B002 — «همزته ولمزته ولهزته ونهزته إذا دفعته» (tahdhib); «الأصل في الهمز واللمز الدفع» (tahdhib) — the dictionary joins the two words of 104:1 in one phrase: both are shoving.
- 104:1 لُّمَزَةٍ — ل م ز B002 — «لمزه إذا ضربه ودفعه» (sihah) — the second word repeats the blow.
- 104:2 جَمَعَ — ج م ع B005 — «جمع الكف وهو حين تقبضها وجمعة من تمر أي قبضة منه» (sihah); «ضربته بجمع يدي إذا ضممت كفك ثم ضربته بها» (jamhara) — the gathering hand is a closed fist, both the handful taken and the fist that strikes.
- 104:4 لَيُنۢبَذَنَّ — ن ب ذ B001 — «نبذت الشيء أنبذه نبذا إذا ألقيته من يدك» (jamhara;sihah); «النبذ طرحك الشيء من يدك أمامك أو خلفك» (tahdhib) — the hand opens, and now he is what it throws.
- 104:4 ٱلْحُطَمَةِ — ح ط م B001 — «الحَطْم كسرك الشيء اليابس كالعظام ونحوها» (ayn;tahdhib); «حطمت الشيء حَطْما كسرته» (maqayis;sihah;mufradat) — the end point of pressure: dry, hard things broken, the nut in the palm grown into bones.
- Quran 111:1–3 — God's word on Abu Lahab: his two hands perish (تبت يدا), his wealth and gains do not help him (ما أغنى عنه ماله وما كسب), he will burn in a fire of flame. Hands, wealth and fire in one sequence (from memory).
- Quran 60:2 — God describing hostile people: if they gain the upper hand, «ويبسطوا إليكم أيديهم وألسنتهم بالسوء». Hand and tongue are one aggression (see chain 2).
- Quran 75:3–4 — God answering man's supposition: «أيحسب الإنسان ألن نجمع عظامه بلى قادرين على أن نسوي بنانه». God gathers the bones that حطم breaks, down to the fingertips.

### 2. The slanderer's tongue, lips, eye and nape

This is the injury of 104:1 at the level of its instruments. The voice presses its sounds (الهمز في الكلام). The pusher pokes a brother at the nape, from behind. The لُمَزَة whispers with the mouth and points with the eye, to the face. One tahdhib phrase splits the pair: هَمّاز behind the back, لَمّاز in the person's presence. Together they cover the target from both sides. The surah's own word كُلّ names the reversal: a tongue and an eye (الطرف) gone dull, an edge lost. The devil's هَمْز, a fixed expression, puts the prod onto the heart, the place the fire reaches in 104:7.

- 104:1 هُمَزَةٍ — ه م ز B004 — «الهماز والهمزة الذي يهمز أخاه في قفاه من خلفه» (tahdhib); «الهمز مثل اللمز والهامز والهماز العياب والهمزة مثله» (sihah); «همز الإنسان اغتيابه» (mufradat) — the attack from behind, at the back of the neck.
- 104:1 هُمَزَةٍ / لُّمَزَةٍ — ه م ز B004 — «الهماز المغتابون في الغيب واللماز المغتابون في الحضرة» (tahdhib) — the dictionary joins both words: absence and presence, back and face.
- 104:1 لُّمَزَةٍ — ل م ز B001 — «اللمز كالغمز في الوجه تلمزه بفيك بكلام خفي» (ayn;tahdhib); «أصله الإشارة بالعين ونحوها» (sihah); «رجل لماز ولمزة أي عياب» (maqayis;sihah;mufradat); «اللمز الاغتياب وتتبع المعاب» (mufradat) — the face, the half-spoken word, the eye's signal, the hunting for faults.
- 104:1 هُمَزَةٍ — ه م ز B002 — «الهمز في الكلام كأنه يضغط الحرف» (maqayis) — speech itself as pressing: the voice squeezes the letter.
- 104:1 لِّكُلِّ — ك ل ل B001 — «خلاف الحدة وكل السيف واللسان والطرف» (maqayis); «كل الرجل في مشيته والسيف عن ضريبته واللسان عن الكلام» (mufradat); «الكليل السيف الذي لا حد له ولسان كليل» (ayn) — the reversal: the tongue and the eye, the tools of همز and لمز, made blunt. The surah names them that way in the word just before the slanderer.
- 104:1 هُمَزَةٍ — ه م ز B005 [fixed expression] — «همز الشيطان كالموتة تغلب على قلب الإنسان» (maqayis); «همزات الشيطان خطراته التي يخطرها بقلب الإنسان» (sihah) — the prod that lands on the heart.
- Quran 68:10–16 — God to the Prophet: do not obey «كل حلاف مهين همّاز مشاء بنميم», because «أن كان ذا مال وبنين»; then «سنسمه على الخرطوم». A slanderer, his wealth and his branding (68:10, 12–13, 15 from memory).
- Quran 9:58–59 — God on some hypocrites: «ومنهم من يلمزك في الصدقات», set against what they should have said, «حسبنا الله». لمز over how wealth is shared out.
- Quran 49:11–12 — God to the believers: «ولا تلمزوا أنفسكم» (49:11, from memory), then «ولا يغتب بعضكم بعضا أيحب أحدكم أن يأكل لحم أخيه ميتا». Backbiting staged as eating flesh (see chain 8).
- Quran 83:29–30 — God on the criminals who laughed at believers: «وإذا مروا بهم يتغامزون». This is the gesture the dictionary sets beside لمز («اللمز كالغمز»).
- Quran 68:51 — God to the Prophet: the deniers nearly make him slip «بأبصارهم». The eye as a weapon.
- Quran 23:97 — God teaching the Prophet to pray «رب أعوذ بك من همزات الشياطين» (from memory). The fixed expression.
- Quran 45:7 — «ويل لكل أفاك أثيم». The same opening formula (ويل لكل) against a sin of speech.

### 3. Kindled enmity: fire among people

The slanderer's work is a fire lit between people. The root of نار names feud (النائرة). The root of الموقدة names the kindling of war and the blaze of anger. عمد names anger as pain. نبذ names parting in hatred and declaring war. God's kindled fire (104:6) answers the fire the همزة لمزة kindled among people (104:1).

- 104:1 لُّمَزَةٍ — ل م ز B001 — «اللمز الاغتياب وتتبع المعاب» (mufradat) — the spark.
- 104:6 نَارُ — ن و ر B007 — «النائرة الكائنة تقع بين القوم» (ayn); «بينهم نائرة أي عداوة وشحناء» (sihah) — feud as the fire's own word.
- 104:6 ٱلْمُوقَدَةُ — و ق د B005 [fixed expression] — «اتقد فلان غضبا» (mufradat); «يستعار وقد واتقد للحرب كاستعارة النار والاشتعال» (mufradat); «قلب وقاد سريع التوقد في النشاط والمضاء» (ayn) — anger and war kindled.
- 104:9 عَمَدٍ — ع م د B015 — «العمد والضمد الغضب» (tahdhib); «عمد توجع من حزن أو غضب أو سقم» (mufradat) — anger felt as pain.
- 104:4 لَيُنۢبَذَنَّ — ن ب ذ B002 — «نابذ فلان فلانا إذا فارقه عن قلى» (jamhara); «نابذه الحرب كاشفه» (sihah) — parting in hatred, open war.
- Quran 5:64 — God on those who said God's hand is chained: «كلما أوقدوا نارا للحرب أطفأها الله» (from memory). War as a kindled fire.
- Quran 47:37 — God: if He asked you for your wealth and pressed you, «تبخلوا ويخرج أضغانكم». A demand on wealth brings hidden rancour out.
- Quran 8:58 — God to the Prophet, fearing treachery: «فانبذ إليهم على سواء». نبذ as openly casting off a pact.

### 4. Counted, reckoned, and thrown away as not worth counting

He draws scattered wealth together and counts it, or readies it as a reserve against what may come. The dictionary defines حسب with the very verb of counting (حسبته إذا عددته). So يحسب (104:3) sounds the count of عَدَّدَهُ (104:2) even while it means supposing. حَسَب is "what is counted of a man", his reckoned standing. Then mufradat explains نبذ through the counting root: thrown away «لقلة الاعتداد به», for being of little account. The word of his throwing also means a small scrap of wealth. In short: the wealth is counted, the man is thrown out uncounted. Elsewhere the Quran makes God the counter (19:94) and gives the fire's keepers a count (74:31).

- 104:2 جَمَعَ — ج م ع B001 — «جمعت الشئ المتفرق فاجتمع» (sihah); «الجمع ضم الشيء بتقريب بعضه من بعض» (mufradat) — scattered holdings drawn together.
- 104:2 مَالًا — م و ل B001 — «تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله» (tahdhib); «مال الرجل يمول ويمال إذا صار ذا مال» (sihah) — wealth acquired to keep (قنية).
- 104:2 وَعَدَّدَهُۥ — ع د د B001 — «عددت الشيء عدا أي أحصيته» (maqayis;ayn;sihah;tahdhib); «العديد الكثرة» (maqayis;ayn;sihah;tahdhib) — counted, and grown in number.
- 104:2 وَعَدَّدَهُۥ — ع د د B002 — «أعده لأمر كذا هيأه له» (sihah); «العدة ما أعد لأمر يحدث مثل الأهبة» (tahdhib) — readied as a reserve. From memory, the classical commentators also gloss عدّده as أعدّه لنوائب الدهر.
- 104:3 يَحْسَبُ — ح س ب B001 — «الحساب عدك الأشياء؛ حسبته إذا عددته؛ الحساب استعمال العدد» — the dictionary defines the verb of 104:3 by the counting of 104:2.
- 104:3 يَحْسَبُ — ح س ب B002 — «الحسبان الظن؛ حسبت كذا في معنى ظننت؛ الحسبان أن يحكم لأحد النقيضين» — the count turns into a supposition, a ruling for one of two opposites.
- 104:3 يَحْسَبُ — ح س ب B004 — «الحسب الذي يعد من الإنسان؛ ما يعده الإنسان من مفاخر آبائه» — standing, once more defined by counting.
- 104:3 يَحْسَبُ — ح س ب B005 — «احتسب ابنا له أي اعتد به عند الله؛ احتسبت بكذا أجرا عند الله» — the counting that counts with God: the reckoning he did not make.
- 104:4 لَيُنۢبَذَنَّ — ن ب ذ B001 — «النبذ إلقاء الشيء وطرحه لقلة الاعتداد به» (mufradat) — the dictionary explains the throwing through the counting root: he is discarded as not worth counting.
- 104:4 لَيُنۢبَذَنَّ — ن ب ذ B005 — «نبذ من مال أي شيء يسير» (maqayis) — the same word means a scrap of wealth: the counted heap answered by a scrap.
- Quran 19:93–95 — God: everyone in the heavens and earth comes as a servant; «لقد أحصاهم وعدهم عدا», and «وكلهم آتيه يوم القيامة فردا» (from memory). The one who counted is counted, and comes alone.
- Quran 74:30–31 — God on Saqar: «عليها تسعة عشر … وما جعلنا عدتهم إلا فتنة». The fire's keepers have a number. The scene opens with the man given wealth at 74:11–12.
- Quran 69:25–26 — the man handed his book in his left hand: «ولم أدر ما حسابيه». His reckoning was unknown to him (see chain 11).
- Quran 78:27 — God on the people of Hell: «إنهم كانوا لا يرجون حسابا».
- Quran 3:180 — God: «ولا يحسبن الذين يبخلون بما آتاهم الله من فضله هو خيرا لهم … سيطوقون ما بخلوا به». A supposition about withheld wealth.
- Quran 23:55–56 — God: «أيحسبون أنما نمدهم به من مال وبنين نسارع لهم في الخيرات بل لا يشعرون».
- Quran 34:35 — the affluent: «نحن أكثر أموالا وأولادا وما نحن بمعذبين».
- Quran 102:1–2 — «ألهاكم التكاثر حتى زرتم المقابر» (from memory). Out-counting each other until the grave.
- Quran 3:187 — God on those given the Book who «نبذوه وراء ظهورهم واشتروا به ثمنا قليلا» (from memory). Throwing something away for a small price.

### 5. Leaning on wealth: prop, sufficiency, permanence, and debris

خلد means remaining in one's state. Its other branch means clinging to the ground or leaning on something. One mufradat phrase joins it with supposition: «ركن إليها ظانا أنه يخلد فيها». حسب also names sufficiency (حسبك، حسبنا الله), so يحسب lets the listener hear "he takes it as his enough". عمد is the prop and the relied-upon chief. So he leans on wealth as a prop and as his "enough", supposing it will keep him. At the end the props are the columns of the fire (104:9). The dictionary's reply to خلود sits in the fire's own name: حطام الدنيا is «كل ما فيها من مال يفنى ولا يبقى». The surah sets the attribution نار الله (104:6) against the sufficiency he placed in wealth.

- 104:3 أَخْلَدَهُۥ — خ ل د B001 — «أصل واحد يدل على الثبات والملازمة» (maqayis); «دوام البقاء» (jamhara;sihah); «بقاؤه على الحالة التي هو عليها» (mufradat) — lasting, staying as one is.
- 104:3 أَخْلَدَهُۥ — خ ل د B002 [fixed expression] — «أخلد إلى كذا أي ركن إليه ورضي به» (ayn); «أخلد إلى الأرض إذا لصق بها» (maqayis;jamhara); «أخلد بالمكان أقام به وأخلد بصاحبه لزمه» (sihah) — clinging, leaning, settling.
- 104:3 يَحْسَبُ / أَخْلَدَهُۥ — خ ل د B002 — «ركن إليها ظانا أنه يخلد فيها» (mufradat) — the dictionary joins the two verbs of 104:3: leaning on a thing while supposing (ظانا) one will last in it.
- 104:3 يَحْسَبُ — ح س ب B003 — «حسبك هذا أي كفاك؛ حسبنا الله أي كافينا هو؛ عطاء حسابا أي كافيا» — the supposing verb shares its root with "enough". The dictionary's own phrase puts God in that place.
- 104:2 مَالًا / 104:3 مَالَهُۥٓ — م و ل B002 — «إن المولة العنكبوت وفيه نظر» (maqayis); «زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة» (sihah); «المولة اسم العنكبوت» (ayn) — maqayis and sihah record this sense and doubt it; ayn and tahdhib give it plainly. If heard, the thing he leans on bears the spider's name, whose house the Quran calls the frailest (29:41).
- 104:9 عَمَدٍ — ع م د B002 — «تعمد الشيء بعماد يمسكه ويعتمد عليه» (maqayis;ayn); «عمدت الشيء أسندته» (maqayis;mufradat) — the prop that holds a thing up.
- 104:9 عَمَدٍ — ع م د B006 — «عميد القوم سيدهم الذي يعتمدون عليه» (ayn); «العمدة ما يعتمد عليه» (sihah) — the one relied upon.
- 104:9 عَمَدٍ — ع م د B014 — «حلس به وعرس به وعمد به ولزب به إذا لزمه» (tahdhib) — holding fast to something, as أخلد بصاحبه لزمه. Clinging is turned around into being held.
- 104:4 ٱلْحُطَمَةِ — ح ط م B009 — «حطام الدنيا كل ما فيها من مال يفنى ولا يبقى» (tahdhib) — the dictionary joins مال with the denial of بقاء, the word خلود is defined by. The wealth he thought would keep him is what does not last, and its name is inside the name of the fire.
- Quran 7:176 — God on the man given signs who «أخلد إلى الأرض واتبع هواه». The same verb form, clinging to the earth.
- Quran 26:128–129 — Hud to 'Ad: «وتتخذون مصانع لعلكم تخلدون». Structures built in hope of lasting.
- Quran 89:6–8 — God: «ألم تر كيف فعل ربك بعاد إرم ذات العماد». The columns of a people that thought itself lasting (89:8 from memory).
- Quran 20:120 — Satan whispering to Adam: «هل أدلك على شجرة الخلد وملك لا يبلى». The first promise of permanence through possession.
- Quran 18:32–42 — the owner of two gardens says «ما أظن أن تبيد هذه أبدا» (18:35, from memory). After the ruin he says «يا ليتني لم أشرك بربي أحدا» (18:42). See chain 6 for the fire from the sky.
- Quran 28:76–78 — Qarun, whose keys weighed down a band of strong men, says «إنما أوتيته على علم عندي». God answers that He destroyed before him people «أكثر جمعا».
- Quran 9:59 — the hypocrites should have said «حسبنا الله». Sufficiency placed where it belongs.
- Quran 21:34 — God to the Prophet: «وما جعلنا لبشر من قبلك الخلد أفإن مت فهم الخالدون» (from memory).
- Quran 29:41 — God's parable of those who take protectors other than Him: «كمثل العنكبوت اتخذت بيتا وإن أوهن البيوت لبيت العنكبوت» (from memory).
- Quran 92:11 — «وما يغني عنه ماله إذا تردى» (from memory); 69:28 «ما أغنى عني ماليه» (from memory). The prop fails.

### 6. Water gathered, crop and flower, then heat, drought, and dry debris

This is one natural process the surah's words supply almost entirely. Floodwater gathers from every place. It collects in a source fed without break. A river swells, fed by another. A dam holds the water so it gathers in one place. Rain soaks the soil until it clumps in the hand. The crop appears and the tree flowers. Then come summer's worst heat, the drought year, and destruction from the sky (حسبان). What is left is الحطام, dry broken stalks. Again and again the dictionary joins water-gathering with جمع. The Quran stages this exact process as the parable of multiplied wealth (57:20) and of a garden owner who supposed it would never perish (18:32–42).

- 104:2 جَمَعَ — ج م ع B010 [fixed expression] — «استجمع السيل اجتمع من كل موضع» (sihah) — the flood gathering from every place. The phrase also carries the كل of 104:1.
- 104:2 وَعَدَّدَهُۥ — ع د د B004 — «العد مجتمع الماء» (maqayis;ayn); «العد بالكسر الماء الذي له مادة لا تنقطع» (sihah); «الماء العد الدائم الذي لا انقطاع له» (tahdhib) — the water that never fails. The dictionary joins عدّ with gathering (مجتمع), with unfailing supply (مادة, the root of 104:9's مُمَدَّدَة) and with lasting (دائم, the sense he gives أخلده).
- 104:9 مُّمَدَّدَةٍۭ — م د د B003 — «مد النهر ومده نهر آخر» (maqayis;jamhara;sihah;tahdhib;mufradat); «المد السيل وكثرة الماء أيام المدود» (sihah;tahdhib) — a river swelling, fed by another.
- 104:9 عَمَدٍ — ع م د B013 — «عمدت السيل تعميدا إذا سددت وجه جريته حتى يجتمع في موضع بتراب أو حجارة» (tahdhib) — the dam. The dictionary joins عمد and جمع: water held until it gathers.
- 104:9 عَمَدٍ — ع م د B010 — «عمد الثرى إذا بلله المطر وتعقد واجتمع من ندوته» (sihah); «عمدت الأرض إذا رسخ فيها المطر إلى الثرى وتعقد في كفك» (maqayis;tahdhib) — rain-soaked earth clumping in the hand, once more with اجتمع.
- 104:7 تَطَّلِعُ — ط ل ع B005 — «طلع الزرع إذا بدا؛ وأطلعت النخلة إذا أخرجت طلعها» (tahdhib) — the crop appearing, the palm putting out its spathe.
- 104:6 نَارُ — ن و ر B004 — «تنوير الشجرة: إزهارها؛ نورت الشجرة وأنارت أي أخرجت نورها» (sihah) — the blossom.
- 104:6 ٱلْمُوقَدَةُ — و ق د B004 — «وقدة الصيف أشده حرا» (maqayis;ayn;mufradat); «الوقدة أشد من الحر وهي عشرة أيام أو نصف شهر» (sihah) — summer's worst heat.
- 104:4 ٱلْحُطَمَةِ — ح ط م B003 — «الحطمة السنة الشديدة لأنها تحطم كل شيء» (maqayis); «أصابتهم حطمة أي سنة وجدب» (sihah) — the drought year, the reversal of the unfailing spring.
- 104:3 يَحْسَبُ — ح س ب B007 — «حسبانا من السماء أي نارا تحرقها؛ حسبان من السماء بالبرد؛ أصاب الأرض حسبان أي جراد» — fire, hail or locusts sent from the sky onto land. The supposing verb's root names the garden-burning fire.
- 104:4 ٱلْحُطَمَةِ — ح ط م B001 — «الحطام ما تكسر من اليبس» (sihah;tahdhib;mufradat) — the end state: dry things broken.
- 104:4 ٱلْحُطَمَةِ — ح ط م B009 — «حطام الدنيا عرضها وأثرها وزينتها» (tahdhib) — the same word for worldly goods and their show.
- Quran 57:20 — God: «اعلموا أنما الحياة الدنيا … وتكاثر في الأموال والأولاد كمثل غيث أعجب الكفار نباته ثم يهيج فتراه مصفرا ثم يكون حطاما». The multiplying of wealth staged as rain, crop, yellowing, حطام.
- Quran 39:21 — God: rain is led into springs (ينابيع), it brings out crops of many colours, they yellow, «ثم يجعله حطاما».
- Quran 18:45 — God's parable: water mingles with the plants of the earth, «فأصبح هشيما تذروه الرياح».
- Quran 18:32–42 — the parable of the two gardens with a river running between them (18:33, from memory). The owner supposes they will never perish (18:35). His companion says «ويرسل عليها حسبانا من السماء فتصبح صعيدا زلقا» (18:40), and the fruit is ruined (18:42, from memory). The owner's chain runs from water to حسبان.
- Quran 56:63–65 — God: «أفرأيتم ما تحرثون … لو نشاء لجعلناه حطاما» (from memory).
- Quran 20:131 — God to the Prophet: «ولا تمدن عينيك إلى ما متعنا به أزواجا منهم زهرة الحياة الدنيا». Worldly enjoyment as a flower, with مدّ of the eyes (see chain 14).

### 7. Herds: owned, counted, branded, penned, driven, trampled

The dictionary says that among the Arabs مال was herds. That opens a pastoral scene made of the surah's words. The herds are gathered and counted (104:2). They carry the owner's fire-brand: نار of a camel is its brand. They are kept in a stone pen in the mountains, and the dictionary names that pen with مؤصدة's root and the word مال. They are driven by الحُطَمَة, the pitiless herdsman who crushes the beasts against one another, "the worst of herdsmen". A dense herd crushes all before it, and a lion wreaks havoc among the herd. The rider's spur is المِهْماز, and the driven beast is spent (كالّ). The owners are tent people who move to pasture. The surah turns the scene on the owner: he is thrown in, the fire is over him, and he is shut in.

- 104:2 مَالًا — م و ل B001 — «كانت أموال العرب أنعامهم» (ayn); «مال أهل البادية النعم» (tahdhib) — wealth as camels and flocks.
- 104:2 جَمَعَ / وَعَدَّدَهُۥ — ج م ع B001; ع د د B001 — «جمعت الشئ المتفرق فاجتمع» (sihah); «عددت الشيء عدا أي أحصيته» — the herd rounded up and its head counted.
- 104:6 نَارُ — ن و ر B002 — «ما نار هذه الناقة أي ما سمتها؛ نجارها نارها» (sihah) — the fire-brand on the she-camel, the mark of ownership and stock.
- 104:8 مُّؤْصَدَةٌۢ — و ص د B003 — «الوصيدة كالحظيرة تتخذ للمال إلا أنها من الحجارة والحظيرة من الغصنة واستوصدت في الجبل» (sihah); «الوصيدة حجرة تجعل للمال في الجبل» (mufradat) — the dictionary joins مؤصدة's root with مال: a stone pen for livestock in the mountain.
- 104:8 مُّؤْصَدَةٌۢ — ء ص د B002 (echo root, which the dictionary marks as a withheld sound-family candidate, not identity) — «الحظيرة أصيدة سميت بذلك لاشتمالها على ما فيها» (maqayis) — the pen named for enclosing what is inside.
- 104:4 ٱلْحُطَمَةِ — ح ط م B004 — «رجل حَطِم وحُطَمَة إذا كان قليل الرحمة للماشية يهشم بعضها ببعض» (sihah); «شر الرعاء الحُطَمَة» (sihah;tahdhib); «سائق حَطِم يحطم الإبل لفرط سوقه» (mufradat) — the pitiless driver who crushes the beasts together.
- 104:4 ٱلْحُطَمَةِ — ح ط م B006 — «العكرة من الإبل حُطَمَة لأنها تحطم كل شيء تلقاه» (maqayis;sihah); «حُطَمَة الأسد في المال عيثه وفرسه» (ayn;tahdhib) — the dense herd that tramples, and the lion's havoc. The second phrase joins حطمة and مال.
- 104:1 هُمَزَةٍ — ه م ز B003 — «والمهمز والمهماز حديدة في مؤخر خف الرائض» (sihah) — the iron spur at the rider's heel.
- 104:1 لِّكُلِّ — ك ل ل B001 — «كللت من المشي» (sihah); «الكال المعيي» (ayn) — the beast worn out by driving.
- 104:1 لِّكُلِّ — ك ل ل B009 — «الكلاكل من الجماعات كالكراكر من الخيل» (ayn) — massed groups, like troops of horses.
- 104:4 لَيُنۢبَذَنَّ — ن ب ذ B009 — «يقال للشاة المهزولة التي يهملها أهلها نبيذة» — the thin ewe her owners neglect.
- 104:9 عَمَدٍ — ع م د B004 — «أهل عمود وأهل عماد أصحاب الأخبية لا ينزلون غيرها» (maqayis;ayn); «كانوا أهل عمد ينتقلون إلى الكلأ» (tahdhib) — tent people following the pasture: the herd-owner's world.
- Quran 19:86 — God: «ونسوق المجرمين إلى جهنم وردا». The criminals driven to Hell like a herd going down to water.
- Quran 39:71 — «وسيق الذين كفروا إلى جهنم زمرا» (from memory). Driven in droves.
- Quran 50:21 — every soul comes «معها سائق وشهيد» (from memory). A driver behind each soul.
- Quran 68:16 — God on the هَمّاز who has wealth and sons (68:11, 68:14): «سنسمه على الخرطوم». Branded on the snout like a beast.
- Quran 9:34–35 — God on those who hoard gold and silver: «يوم يحمى عليها في نار جهنم فتكوى بها جباههم وجنوبهم وظهورهم هذا ما كنزتم لأنفسكم». The hoarded wealth itself, heated, is the brand.
- Quran 3:14 — among the desires made attractive: «والخيل المسومة والأنعام والحرث» (from memory). Branded horses and herds counted as wealth.

### 8. The hearth that roasts, and the crusher that eats

The fire of 104:4–7 is laid out as a hearth: fuel (الوقود الحطب), a fire-place (الموقد), and the hearth-stones. The dictionary calls those stones الخوالد, "the lasting ones", because they remain long after the camp is gone. There is a great cauldron called جامعة. There is roasting meat and baking bread buried in hot ash, all from the root of الأفئدة. The man is cast into it as fuel is cast into a hearth, or as dates are cast into a vessel. الحُطَمَة is also the glutton, and the dictionary says the glutton is named after Hell. The digesting organ comes from the same root. So the fire is an eater that breaks down what it takes. The verb of 104:7 names the reversal: what was swallowed rising back out.

- 104:6 ٱلْمُوقَدَةُ — و ق د B001 — «كلمة تدل على اشتعال نار» (maqayis); «أوقدتها واستوقدتها» (sihah;mufradat); «الوقد نفس النار أو ما ترى من لهبها» (maqayis;ayn) — kindled, set burning, its flame.
- 104:6 ٱلْمُوقَدَةُ — و ق د B002 — «الوقود الحطب» (maqayis); «وقود النار أي حطبها» (ayn) — fuel, which is what 104:4 throws in.
- 104:6 ٱلْمُوقَدَةُ — و ق د B003 — «الموقد والمستوقد موضع النار» (ayn) — the hearth.
- 104:3 أَخْلَدَهُۥ — خ ل د B001 — «خوالد للأثافي والحجارة لطول مكثها» (ayn;sihah;mufradat) — what the dictionary calls lasting are the stones of a hearth.
- 104:2 جَمَعَ — ج م ع B012 — «قدر جماع وجامعة وهي العظيمة» (maqayis); «قدر جامعة وهي العظيمة» (sihah) — the great cauldron.
- 104:4 لَيُنۢبَذَنَّ — ن ب ذ B006 — «يأخذ تمرا أو زبيبا فينبذه أي يلقيه في وعاء أو سقاء ويصب عليه الماء» (tahdhib); «النبيذ التمر يلقى في الآنية» (maqayis) — نبذ as casting into a vessel.
- 104:7 ٱلْأَفْـِٔدَةِ — ف ء د B001 — «أصل صحيح يدل على حمى وشدة حرارة» (maqayis); «فأدت اللحم شويته ولحم فئيد أي مشوي» (maqayis;sihah;mufradat); «فأدت الخبزة مللتها أو خبزتها في الملة» (maqayis;sihah;tahdhib); «المفأد السفود أو ما يخبز ويشوى به والمفتأد موضع الوقود» (maqayis;sihah;tahdhib) — roasting on the skewer, bread buried in embers. The dictionary joins فأد with وقد (موضع الوقود).
- 104:7 ٱلْأَفْـِٔدَةِ / 104:6 ٱلْمُوقَدَةُ — ف ء د B001 — «افتأد القوم إذا أوقدوا نارا والفئيد النار نفسها» (tahdhib) — the dictionary glosses the heart's root by the verb of 104:6.
- 104:4 ٱلْحُطَمَةِ — ح ط م B002 — «سميت النار الحُطَمَة لحطمها ما تلقى» (maqayis;sihah); «الحُطَمَة النار وقيل باب من جهنم» (ayn); «للنار الشديدة حُطَمَة» (tahdhib) — the fire named for breaking whatever it meets.
- 104:4 ٱلْحُطَمَةِ — ح ط م B008 — «رجل حُطَمَة للكثير الأكل» (sihah;tahdhib); «قيل للأكول حُطَمَة تشبيها بالجحيم» (mufradat); «يقال للجوارس حاطوم وهاضوم» (tahdhib) — the eater, and the organs that grind and digest. The dictionary itself names the glutton after Hell.
- 104:7 تَطَّلِعُ — ط ل ع B011 — «وأطلع أي قاء؛ والطلعاء القيء» (sihah); «أطلع الرجل إطلاعا إذا قاء» (tahdhib) — the reversal of eating: what went down rises back up.
- Quran 3:10 — God: «إن الذين كفروا لن تغني عنهم أموالهم ولا أولادهم من الله شيئا وأولئك هم وقود النار». The owners of wealth are the fuel.
- Quran 2:24 — God to those who doubt the revelation (from memory), and 66:6, God to the believers: «وقودها الناس والحجارة». People and stones as fuel.
- Quran 21:98 — God to the idolaters: «إنكم وما تعبدون من دون الله حصب جهنم». They and what they served, thrown in as fuel.
- Quran 40:71–72 — God on deniers dragged in collars and chains (40:71, from memory): «في الحميم ثم في النار يسجرون». Stoked like fuel.
- Quran 4:56 — God: «كلما نضجت جلودهم بدلناهم جلودا غيرها». Skins cooked through and renewed.
- Quran 4:10 — God: «إن الذين يأكلون أموال اليتامى ظلما إنما يأكلون في بطونهم نارا». Wealth eaten turns into fire in the belly.
- Quran 50:30 — God speaking to Hell: «هل امتلأت وتقول هل من مزيد». The eater that is never full.
- Quran 49:12 — backbiting staged as eating a dead brother's flesh. The slanderer as an eater (see chain 2).
- From memory: Muhammad b. Kaʿb al-Quraẓī glossed 104:7 as the fire eating everything of him until it reaches his heart. This is the eater chain arriving at chain 9.

### 9. The kindled heart

الأفئدة are named for heat. Mufradat says the heart is called فؤاد when the sense of تفؤّد, «أي التوقد», is in view. So the kindled fire (الموقدة, 104:6) rises onto the organ named for kindling (104:7). The heart is also where the supposition of 104:3 sat: the word أخلده is also الخَلَد, «البال … مستقر في القلب». The heart is struck, as game is shot in the heart. It is crushed with grief, القلب العميد, from the root of 104:9's عَمَد. It is the target of the devil's هَمْز. The wealth gathered outside is answered by fire reaching the inmost organ.

- 104:7 ٱلْأَفْـِٔدَةِ — ف ء د B002 — «الفؤاد كالقلب لكن يقال له فؤاد إذا اعتبر فيه معنى التفؤد أي التوقد» (mufradat); «الفؤاد سمي بذلك لحرارته أو لتفؤده» (maqayis;tahdhib) — the dictionary joins أفئدة with the root of الموقدة.
- 104:6 ٱلْمُوقَدَةُ — و ق د B001 — «وقدت النار واتقدت وتوقدت وأوقدتها» (maqayis) — the kindled fire, and the kindled organ it reaches.
- 104:3 أَخْلَدَهُۥ — خ ل د B004 — «الخلد البال وسمي بذلك لأنه مستقر في القلب ثابت» (maqayis); «وقع ذلك في خلدي أي في قلبي» (jamhara) — the word for "made him last" also names the mind settled in the heart. The supposition sits where the fire arrives.
- 104:7 تَطَّلِعُ — ط ل ع B003 [fixed expression] — «اطلعت على باطن أمره» (sihah); «اطلع أشرف على الشيء» (ayn) — looking down onto something and knowing its inside.
- 104:7 ٱلْأَفْـِٔدَةِ — ف ء د B003 — «فأدته فهو مفؤود أصبت فؤاده وكذلك إذا أصابه داء فؤاده» (sihah); «فأدت الصيد إذا أصبت فؤاده» (tahdhib) — struck in the heart; heart disease.
- 104:7 ٱلْأَفْـِٔدَةِ — ف ء د B004 — «المفؤود الضعيف الفؤاد الجبان مثل المنخوب» (tahdhib) — the heart gone weak.
- 104:9 عَمَدٍ — ع م د B008 — «القلب العميد المعمود المشعوف الذي هده العشق» (maqayis;ayn); «القلب الذي يعمده الحزن والسقيم الذي يعمده السقم» (mufradat); «عمد المرض فدحه» (sihah) — the dictionary joins عمد with القلب: the heart crushed by grief and sickness.
- 104:1 هُمَزَةٍ — ه م ز B005 [fixed expression] — «همز الشيطان كالموتة تغلب على قلب الإنسان» (maqayis) — pressure that overpowers the heart.
- 104:1 لِّكُلِّ — ك ل ل B007 — «الكلكل الصدر» (maqayis;ayn;tahdhib;mufradat) — the chest that houses the heart.
- Quran 26:88–89 — Abraham's prayer: «يوم لا ينفع مال ولا بنون إلا من أتى الله بقلب سليم». Wealth set against the heart.
- Quran 17:36 — God: «إن السمع والبصر والفؤاد كل أولئك كان عنه مسؤولا». The heart is answerable, with كل beside فؤاد.
- Quran 83:14 — «كلا بل ران على قلوبهم ما كانوا يكسبون» (from memory). Earnings caked over the hearts.
- Quran 100:8–10 — God on man: «وإنه لحب الخير لشديد … وحصل ما في الصدور» (from memory). Love of wealth, then what is in the breasts brought out.
- Quran 22:19–20 — scalding water poured over their heads, «يصهر به ما في بطونهم والجلود» (from memory). The inside melted.

### 10. The fire that rises: thrown down, climbing, filling, shut above

This is the surah's vertical scene. He is thrown down (104:4). The fire rises (تطلع): as a sun rises, as a climber reaches the top of a mountain, as one comes upon a people to assail them. The dictionary's phrase for that last sense has the same preposition, على. It is also the filling of a vessel to the brim. The rising stops on the hearts, and the cover is shut over them, عليهم (104:8). The arrow that rises past its mark (أطلع الرامي) is the reversal: this rising does not overshoot.

- 104:4 لَيُنۢبَذَنَّ — ن ب ذ B001 — «أصل صحيح يدل على طرح وإلقاء» (maqayis) — downward.
- 104:7 تَطَّلِعُ — ط ل ع B001 [fixed expression] — «طلعت الشمس والكوكب طلوعا ومطلعا» (sihah); «أصل واحد صحيح يدل على ظهور وبروز» (maqayis) — rising as a luminary rises.
- 104:7 تَطَّلِعُ عَلَى — ط ل ع B002 [fixed expression] — «طلع علينا فلان يطلع طلوعا إذا هجم» (ayn); «طلعت على القوم إذا أتيتهم» (sihah) — coming upon with على, as an assault: the construction of 104:7.
- 104:7 تَطَّلِعُ — ط ل ع B006 [fixed expression] — «طلعت الجبل أي علوته؛ المطلع موضع الاطلاع من إشراف إلى انحدار» (sihah); «هول المطلع» (maqayis) — the climb, and the terror of looking down from the top.
- 104:7 تَطَّلِعُ — ط ل ع B007 [fixed expression] — «طلاع الأرض ملؤها حتى يطالع أعلى الأرض» (tahdhib); «قدح طلاع ممتلىء» (tahdhib) — filling to the brim.
- 104:7 تَطَّلِعُ — ط ل ع B010 [fixed expression] — «وأطلع الرامي أي جاز سهمه من فوق الغرض» (sihah) — the reversal: the arrow rising over its target. The fire's rising stops on its target.
- 104:6 نَارُ — ن و ر B001 — «أصل صحيح يدل على إضاءة واضطراب وقلة ثبات» (maqayis) — fire as light that never keeps still.
- 104:8 عَلَيْهِم مُّؤْصَدَةٌۢ — و ص د B001 — «أوصدت الباب وآصدته أي أطبقته وأحكمته ومؤصدة مطبقة» (mufradat) — the cover pressed shut from above.
- Quran 25:12–13 — God on the fire: «إذا رأتهم من مكان بعيد سمعوا لها تغيظا وزفيرا وإذا ألقوا منها مكانا ضيقا مقرنين دعوا هنالك ثبورا». The fire sees them, they are thrown into a narrow place, bound together.
- Quran 67:7–8 — «إذا ألقوا فيها سمعوا لها شهيقا وهي تفور تكاد تميز من الغيظ» (from memory). Thrown in, and the fire surges.
- Quran 22:22; 32:20 — «كلما أرادوا أن يخرجوا منها … أعيدوا فيها». The way up is closed.

### 11. Supposing, not knowing, knowing

The surah moves through three positions of knowledge. He supposes: يحسب is a count turned into a ruling for one of two opposites. The listener is told he does not know: وما أدراك. The dictionary's own example for this verb is «دريت الشيء والله أدرانيه», and نار الله follows in 104:6. Then the fire looks down onto the hearts and knows their inside (اطلع على باطن أمره). The reckoner did not know his reckoning. The fire knows what was in the heart.

- 104:3 يَحْسَبُ — ح س ب B002 — «حسبت كذا في معنى ظننت؛ الحسبان أن يحكم لأحد النقيضين» — supposition.
- 104:3 يَحْسَبُ — ح س ب B010 — «تحسبت الخبر أي استخبرت؛ احتسبت فلانا اختبرت ما عنده» — probing what is in someone. The fire does this to him.
- 104:5 أَدْرَىٰكَ — د ر ي B001 — «دريت الشيء والله أدرانيه» (maqayis); «دريته ودريت به أي علمت به وأدريته أي أعلمته» (sihah); «الدراية المعرفة المدركة بضرب من الحيل» (mufradat) — knowing and being made to know. The dictionary pairs the verb with God as the one who informs.
- 104:7 تَطَّلِعُ — ط ل ع B003 [fixed expression] — «أطلعني طلع هذا الأمر حتى علمته كله» (ayn); «اطلعت على باطن أمره» (sihah) — knowing a thing whole, from inside.
- Quran 74:11–31 — God on the man He created alone and gave «مالا ممدودا» (74:12). Then «سأصليه سقر وما أدراك ما سقر لا تبقي ولا تذر» (74:26–28, 74:27 from memory), «عليها تسعة عشر … وما جعلنا عدتهم إلا فتنة». The same sequence as 104: wealth, ما أدراك, the fire, a count.
- Quran 69:25–26 — the man handed his book in his left hand: «يا ليتني لم أوت كتابيه ولم أدر ما حسابيه». The dictionary's two verbs, درى and حسب, in one cry.
- Quran 90:5–7 — God on man: «أيحسب أن لن يقدر عليه أحد … أيحسب أن لم يره أحد», with «يقول أهلكت مالا لبدا» (90:6, from memory) between them. He supposes that no one sees.
- Quran 101:9–11 — «فأمه هاوية وما أدراك ما هيه نار حامية» (from memory). The same formula opening onto fire.
- Quran 28:78 — Qarun: «إنما أوتيته على علم عندي». Claimed knowledge about wealth.
- Quran 86:9 — «يوم تبلى السرائر» (from memory). What is hidden inside is tested.
- From memory: some classical commentators read تطلع على الأفئدة as the fire knowing what each heart holds, besides reaching it.

### 12. Stalking, aiming, and the shot to the heart

The root of أدراك carries the hunter's craft. He looks for where the game is before he sees it, approaches under cover of a decoy animal, and trains on a target ring. Another branch means choosing a place and making for it in a raid, and the dictionary glosses it with عمد's root (اعتمدوه). The root of همزة names a bow with a strong thrust. The root of الأفئدة names hitting game in the heart. طلع adds scouts sent out to spy on the enemy, and as reversal the arrow that overshoots. The fire's movement onto the hearts (104:7) can be heard as an aimed shot that finds its mark.

- 104:5 أَدْرَىٰكَ — د ر ي B003 — «تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته» (maqayis); «الدرية الدابة التي يستتر بها الذي يرمي الصيد» (maqayis) — stalking under cover.
- 104:5 أَدْرَىٰكَ — د ر ي B002 [fixed expression] — «ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة» (maqayis) — choosing a target for a raid. The dictionary joins درى with عمد's root.
- 104:9 عَمَدٍ — ع م د B001 — «عمدت فلانا إذا قصدت إليه» (maqayis); «العمد والتعمد خلاف السهو» (mufradat) — aimed on purpose, not by mistake.
- 104:5 أَدْرَىٰكَ — د ر ي B005 — «الدريئة الحلقة التي يتعلم عليها الطعن» (maqayis); «الدريئة مهموزة الحلقة التي يتعلم الرامي عليها» (tahdhib) — the target ring.
- 104:1 هُمَزَةٍ — ه م ز B003 — «قوس همزي شديدة الدفع للسهم» (maqayis) — the bow's strong thrust.
- 104:7 تَطَّلِعُ — ط ل ع B004 — «الطليعة قوم يبعثون ليطلعوا طلع العدو» (ayn) — scouts sent ahead to spy on the enemy.
- 104:7 ٱلْأَفْـِٔدَةِ — ف ء د B003 — «فأدت الصيد إذا أصبت فؤاده» (tahdhib); «الفأد مصدر فأدته إذا أصبت فؤاده» (maqayis) — the shot to the heart.
- 104:7 تَطَّلِعُ — ط ل ع B010 [fixed expression] — «ورمى فلان فأطلع وأشخص إذا مر سهمه برأس الغرض» (maqayis) — the reversal: the shot that flies over its mark.

### 13. The shut structure: encompassing, door and cover, columns, binding

The surah opens with a word of encompassing, كلّ «للإحاطة». The same root names a ring set around something and a light curtain sewn like a house. It closes with a structure. A door is shut and a cover pressed down over them (مؤصدة, «المطبق»). The threshold is named. Long columns stand, tent-poles and marble pillars, stretched lengthwise as a tent is stretched on ropes. One of the dictionary's own phrases under عمد is «وفي عمد من النار». The hands that gathered (جمع) have their own end in the root: الجامعة is the fetter «لأنها تجمع اليدين إلى العنق». The scene stays at the level of a closed tent or house. The shelter's words (the curtain against insects, the house's threshold) are turned into a prison.

- 104:1 لِّكُلِّ — ك ل ل B003 — «كل اسم موضوع للإحاطة مضاف أبدا» (maqayis); «لفظ كل هو لضم أجزاء الشيء ويفيد معنى التمام» (mufradat) — encompassing, gathering all the parts.
- 104:1 لِّكُلِّ — ك ل ل B005 — «إطافة شيء بشيء والإكليل منزل من منازل القمر والسحاب يدور بالمكان» (maqayis); «الإكليل سمي بذلك لإطافته بالرأس» (mufradat) — a ring set around, cloud circling a place.
- 104:1 لِّكُلِّ — ك ل ل B006 — «الكلة الستر الرقيق يخاط كالبيت يتوقى فيه من البق» (sihah); «الكلة من الستور ما خيط فصار كالبيت والتكليل رفعها ببناء مثل الكلل وهي الصوامع والقباب» (tahdhib) — a curtain sewn like a house, raised into domes. Shelter, turned in the surah into enclosure.
- 104:8 مُّؤْصَدَةٌۢ — و ص د B001 — «أصل يدل على ضم شيء إلى شيء» (maqayis); «أوصدت الباب أغلقته والموصد المطبق» (maqayis); «أوصدت الباب وآصدته إذا أغلقته فهو موصد ومطبقة» (sihah) — door shut, lid pressed down: one thing closed against another.
- 104:8 مُّؤْصَدَةٌۢ — و ص د B002 — «الوصيد فناء البيت والوصيد الباب» (ayn) — the threshold and door of the house.
- 104:8 مُّؤْصَدَةٌۢ — ء ص د B001 (echo root, marked in the dictionary as a withheld sound-family candidate, not identity) — «نار مُؤصدة أي مطبقة» (ayn); «شيء يشتمل على الشيء» (maqayis); «أصدت عليهم وأوصدته» (ayn) — the phrase gives the surah's own collocation, a fire shut over them. From memory: the text's hamzated مُؤْصَدَة is the reading of Ḥafṣ, Abū ʿAmr and Ḥamza, and some lexicographers derive it from آصد.
- 104:9 عَمَدٍ — ع م د B003 — «عمود الخباء من خشب قائم في الوسط» (ayn); «العمود عمود البيت وجمعه أعمدة وعمد» (sihah); «العمد أساطين الرخام وفي عمد من النار» (tahdhib) — the tent-pole, the house column, marble pillars. Tahdhib quotes «في عمد من النار».
- 104:9 مُّمَدَّدَةٍۭ — م د د B001 — «جر شيء في طول واتصال شيء بشيء في استطالة» (maqayis); «مددت الشيء ومددت الحبل فامتد» (maqayis;jamhara;sihah;tahdhib) — stretched lengthwise, as a rope is pulled taut.
- 104:2 جَمَعَ — ج م ع B008 — «الجامعة الغل لأنها تجمع اليدين إلى العنق» (sihah); «الجوامع الأغلال» (maqayis) — the fetter: the gathering hands gathered to the neck.
- Quran 90:19–20 — God on the companions of the left: «عليهم نار مؤصدة». The same phrase, with عليهم. The surah opens with «أيحسب» and wealth (90:5–7).
- Quran 18:29 — God: «إنا أعتدنا للظالمين نارا أحاط بهم سرادقها». The fire as a pavilion wall encircling them.
- Quran 29:54 — «وإن جهنم لمحيطة بالكافرين». Encompassing, the sense of كلّ.
- Quran 15:43–44 — Hell «لها سبعة أبواب» (from memory). The fire has doors.
- Quran 69:28–32 — the man who says «ما أغنى عني ماليه» (from memory). Then «خذوه فغلوه … ثم في سلسلة ذرعها سبعون ذراعا فاسلكوه» (69:30–31 from memory). The one who trusted his wealth is fettered and threaded on a long chain.
- Quran 17:29 — God's instruction: «ولا تجعل يدك مغلولة إلى عنقك». The miser's hand fettered to the neck.
- Quran 3:180 — «سيطوقون ما بخلوا به يوم القيامة». Withheld wealth worn as a collar.
- Quran 36:8 — «إنا جعلنا في أعناقهم أغلالا فهي إلى الأذقان» (from memory).
- Quran 25:13 — «ألقوا منها مكانا ضيقا مقرنين». Thrown into a tight place, bound together.
- Quran 89:7 — «إرم ذات العماد». Columns of a city meant to last (see chain 5).
- Quran 18:18 — the cave sleepers' dog «باسط ذراعيه بالوصيد» (from memory). The threshold, in a scene of sheltered enclosure, the reversal.
- From memory: the commentators read في عمد ممددة in several ways: as long bars that fasten the closed gates, as columns they are bound to, or as the fire's columns around them.

### 14. Extension: wealth stretched, respite stretched, columns stretched

مدد is the supply added to an army, food given, earth added to earth, and «مداد كلماته أي عددها وكثرتها». That phrase joins مدد with عدد, the root of 104:2. It is also the lengthening of a life and of a respite, «مده في غيه أمهله». At its plainest it is stretching. The man's wealth was "extended" and counted up. His time was extended. The surah ends on columns «مُمَدَّدَة». The sound joins the two ends: عَدَّدَهُ in 104:2 and مُمَدَّدَة in 104:9 both carry the doubled dal (from the text).

- 104:9 مُّمَدَّدَةٍۭ — م د د B002 — «أمددت الجيش بمدد» (maqayis;jamhara;sihah;tahdhib;mufradat); «أمددناهم بفاكهة وأمددت الإنسان بطعام» (sihah;mufradat); «مددت الأرض إذا زدت فيها ترابا أو سمادا ومداد كلماته أي عددها وكثرتها» (tahdhib) — supply added. The last phrase joins مدد and عدد.
- 104:9 مُّمَدَّدَةٍۭ — م د د B004 — «مد الله في عمره ومده في غيه أمهله وطول له» (sihah); «أمددت لك في الأجل أنسأتك فيه والمدة الأجل» (jamhara) — life and respite lengthened.
- 104:9 مُّمَدَّدَةٍۭ — م د د B001 — «مددت الشيء ومددت الحبل فامتد» — the bare physical stretch the surah ends on.
- 104:2 وَعَدَّدَهُۥ — ع د د B001 — «العديد الكثرة» (maqayis;ayn;sihah;tahdhib) — the count grown large.
- 104:2 وَعَدَّدَهُۥ — ع د د B004 — «العد بالكسر الماء الذي له مادة لا تنقطع» (sihah) — supply (مادة) that does not stop.
- Quran 74:11–12 — God on the man He created alone: «وجعلت له مالا ممدودا». Wealth "extended", answered by Saqar in 74:26.
- Quran 23:55–56 — «أيحسبون أنما نمدهم به من مال وبنين». يحسب, مدّ and مال in one line.
- Quran 19:77–79 — «أفرأيت الذي كفر بآياتنا وقال لأوتين مالا وولدا … كلا سنكتب ما يقول ونمد له من العذاب مدا». كلا, as in 104:4, and the punishment extended.
- Quran 19:75 — «فليمدد له الرحمن مدا». A respite extended to those in error.
- Quran 2:15 — «ويمدهم في طغيانهم يعمهون» (from memory).
- Quran 20:131 — «ولا تمدن عينيك إلى ما متعنا به أزواجا منهم زهرة الحياة الدنيا». The eyes stretched toward the flower of worldly life.
- Quran 56:30 — «وظل ممدود». The extended shade of the garden, the reversal of the extended columns.

### 15. Full body, delayed gray, broken by age

Three of the surah's words name stages of graying. To be مُخْلَد is to be the man on whom gray comes late. نَبْذ is a first sprinkling of gray. حَطِم is the man or horse broken by age. Behind them stand the full-bodied man in his prime, called مجتمع from 104:2's root, and the youth «الممتلئ شبابا» from 104:9's root. Heard across the surah, he supposes his wealth has made him مُخْلَد, slow to gray. The surah's next words give the sprinkle of gray and the breaking.

- 104:2 جَمَعَ — ج م ع B009 — «الرجل المجتمع الذي بلغ أشده» (sihah); «رجل جميع أي مجتمع في خلقه» (ayn) — the body complete, in its prime.
- 104:9 عَمَدٍ — ع م د B011 — «العمد الشاب الممتلئ شبابا» (tahdhib); «العمد الشاب الشديد الممتلئ شبابا» (ayn) — youth at full strength.
- 104:1 لِّكُلِّ — ك ل ل B008 [fixed expression] — «رجل كلكل قصير غليظ مع شدة» (sihah) — a stocky, strong man.
- 104:3 أَخْلَدَهُۥ — خ ل د B001 — «مخلد إذا أبطأ عنه الشيب» (maqayis;jamhara;sihah;mufradat) — in the dictionary, to be "made lasting" is to stay ungrayed.
- 104:4 لَيُنۢبَذَنَّ — ن ب ذ B005 — «في رأسه نبذ من شيب» (sihah); «نبذ من الشيب أي يسير» (maqayis) — the first gray in the head.
- 104:4 ٱلْحُطَمَةِ — ح ط م B005 — «حطمته السن إذا أسن وضعف» (sihah;tahdhib); «حطم فلانا أهله إذا كبر فيهم كأنهم صيروه شيخا محطوما» (tahdhib); «يقال للفرس إذا تهدم لطول عمره حَطِم» (maqayis;sihah) — broken by the years.
- Quran 30:54 — God: «ثم جعل من بعد قوة ضعفا وشيبة». Strength, then weakness and gray.
- Quran 19:4 — Zakariyya: «رب إني وهن العظم مني واشتعل الرأس شيبا». The bone weakened (cf. «كسرك الشيء اليابس كالعظام») and the head set alight with gray: aging staged as fire.
- Quran 36:68 — «ومن نعمره ننكسه في الخلق» (from memory).

### 16. The dependent orphan and the cast-off child

The surah's first word holds a sense set against the man who gathers. الكَلّ is the orphan, the childless man, the dependent who is a weight on whoever keeps him. The verb of his throwing names the foundling, the child its mother throws out on the road for someone to pick up. Heard together, the hoarder's wealth stands beside the dependent he does not carry. He himself is then thrown out like the foundling, with no one to take him up.

- 104:1 لِّكُلِّ — ك ل ل B002 — «الكل اليتيم والكل الرجل الذي لا ولد له والكل أيضا الذي هو عيال وثقل» (ayn); «الكل الثقيل الروح واليتيم والوكيل والذي هو عيال وثقل على صاحبه» (tahdhib) — the orphan, the dependent, the burden.
- 104:4 لَيُنۢبَذَنَّ — ن ب ذ B007 — «المنبوذ الصبي تلقيه أمه في الطريق» (sihah); «المنبوذ الولد الذي تنبذه والدته حين تلده فيلتقطه الرجل أو جماعة من المسلمين» (tahdhib) — the foundling.
- 104:4 لَيُنۢبَذَنَّ — ن ب ذ B009 — «يقال للشاة المهزولة التي يهملها أهلها نبيذة» — the neglected thin ewe, the same casting-off among the herd.
- Quran 89:17–20 — God: «كلا بل لا تكرمون اليتيم ولا تحاضون على طعام المسكين وتأكلون التراث أكلا لما وتحبون المال حبا جما» (89:17–19 from memory). كلا, the orphan, and wealth loved.
- Quran 107:1–2 — «أرأيت الذي يكذب بالدين فذلك الذي يدع اليتيم» (from memory).
- Quran 4:10 — those who eat orphans' wealth eat fire.
- Quran 16:76 — God's parable of two men, one of them «وهو كل على مولاه» (from memory). The word كَلّ itself, a weight on his master.
- Quran 37:145–146 — Yunus: «فنبذناه بالعراء وهو سقيم», then a gourd plant grown over him (37:146, from memory). Thrown out, then sheltered: the foundling's other ending.

### 17. The cushion thrown down for sitting

Two words in adjacent ayat both name the small cushion. حَسَب names it in 104:3, and مِنْبَذة in 104:4 is named for being thrown on the ground to be sat on. Here throwing is the gesture of comfort: a cushion tossed down for a seated man. The surah reverses that throw into the casting into the crusher.

- 104:3 يَحْسَبُ — ح س ب B008 — «الحسبانة الوسادة الصغيرة؛ حسبته إذا وسدته؛ المحسبة وسادة من أدم» — a small leather cushion, propping someone's head on it.
- 104:4 لَيُنۢبَذَنَّ — ن ب ذ B008 — «المنبذة الوسادة سميت منبذة لأنها تنبذ بالأرض أي تطرح للجلوس عليها» (tahdhib) — the cushion named for being thrown down to sit on.
- Quran 88:15–16 — in the garden, «ونمارق مصفوفة وزرابي مبثوثة» (from memory). Cushions set in rows, the throw of comfort kept in its place.

## Interactions

- Chain 1 (hand) / chain 2 (tongue): both are carried by ه م ز and ل م ز. «همزته ولمزته ولهزته ونهزته إذا دفعته» (tahdhib) is the push, «الهماز المغتابون في الغيب واللماز المغتابون في الحضرة» (tahdhib) the speech. Quran 60:2 stages hands and tongues together.
- Chain 1 (hand) / chain 13 (structure): ج م ع B005 «جمع الكف» and B008 «الجامعة الغل لأنها تجمع اليدين إلى العنق». The fist that gathered becomes the hands fettered. Quran 17:29 and 69:28–32 join wealth with the fettered hand or neck.
- Chain 1 (hand) / chain 8 (crusher): «همزت الجوز بكفي» (tahdhib) and «الحَطْم كسرك الشيء اليابس كالعظام» (ayn;tahdhib). Cracking in the palm, then breaking in the fire. Quran 75:3–4 gathers the bones and fingertips.
- Chain 2 (tongue) / chain 9 (heart): ه م ز B005 «همز الشيطان كالموتة تغلب على قلب الإنسان». The prod lands on the heart, where 104:7's fire lands.
- Chain 2 (tongue) / chain 7 (herds): Quran 68:10–16 stages the هَمّاز, his wealth (ذا مال وبنين) and the brand (سنسمه) together. ه م ز B003 «المهماز» is the herd-driver's spur.
- Chain 2 (tongue) / chain 8 (eater): Quran 49:12 stages backbiting as eating a brother's flesh. ح ط م B008 names the glutton «تشبيها بالجحيم».
- Chain 3 (enmity) / chain 8 (hearth): ن و ر B007 «النائرة» and و ق د B005 «اتقد فلان غضبا». The fire the slanderer kindled among people is answered by «نار الله الموقدة».
- Chain 4 (counting) / chain 5 (leaning): يحسب is both «حسبته إذا عددته» and «حسبك هذا أي كفاك». Mufradat's «ركن إليها ظانا أنه يخلد فيها» joins the supposition to the leaning.
- Chain 4 (counting) / chain 14 (extension): «مداد كلماته أي عددها وكثرتها» (tahdhib). The sound echo عَدَّدَهُ / مُمَدَّدَة (text). Quran 23:55 «أيحسبون أنما نمدهم به من مال».
- Chain 4 (counting) / chain 6 (water): «العد مجتمع الماء» (maqayis;ayn) puts the counted wealth's root on gathered water.
- Chain 4 (counting) / chain 11 (knowing): Quran 69:26 «ولم أدر ما حسابيه» joins درى and حسب. 74:27–31 joins ما أدراك with the fire's count (عدتهم).
- Chain 5 (leaning) / chain 6 (water): «الماء العد الدائم الذي لا انقطاع له» (tahdhib) is the lasting he supposes. «حطام الدنيا كل ما فيها من مال يفنى ولا يبقى» (tahdhib) is its end. Quran 57:20 and 18:32–42 stage both.
- Chain 5 (leaning) / chain 8 (hearth): خ ل د B001 «خوالد للأثافي والحجارة لطول مكثها». The only "lasting ones" in the root are hearth-stones.
- Chain 5 (leaning) / chain 9 (heart): خ ل د B004 «الخلد البال … مستقر في القلب ثابت». The thought of lasting sits in the heart the fire reaches.
- Chain 5 (leaning) / chain 13 (structure): ع م د B002/B006, the prop and the relied-upon, against B003, the columns of the fire. Quran 26:129 and 89:7 stage structures built to last.
- Chain 5 (leaning) / chain 15 (age): «مخلد إذا أبطأ عنه الشيب». The lasting he supposes is, in the dictionary, delayed gray.
- Chain 6 (water) / chain 8 (fire): ح س ب B007 «حسبانا من السماء أي نارا تحرقها» and و ق د B004 «وقدة الصيف أشده حرا». Fire and heat end the watered growth. Quran 18:40 sends حسبان onto the garden.
- Chain 7 (herds) / chain 13 (structure): و ص د B003 «الوصيدة حجرة تجعل للمال في الجبل» (mufradat). The pen built for his wealth, then the shut fire over him.
- Chain 7 (herds) / chain 8 (fire): ن و ر B002 «ما نار هذه الناقة أي ما سمتها». Quran 9:35 brands the hoarders with their own heated treasure, and 68:16 brands the هَمّاز.
- Chain 7 (herds) / chain 10 (rising): Quran 19:86 «ونسوق المجرمين إلى جهنم وردا». The driving ends in the throwing of 104:4.
- Chain 8 (hearth) / chain 9 (heart): «افتأد القوم إذا أوقدوا نارا» (tahdhib) and «يقال له فؤاد إذا اعتبر فيه معنى التفؤد أي التوقد» (mufradat). The dictionary joins الأفئدة and الموقدة twice.
- Chain 8 (eater) / chain 10 (rising): the commentary reported from memory (al-Quraẓī) has the fire eating until it reaches the heart. ط ل ع B011, vomit, is that rising reversed.
- Chain 9 (heart) / chain 12 (stalking): ف ء د B003 «فأدت الصيد إذا أصبت فؤاده». The heart as the hunter's mark.
- Chain 10 (rising) / chain 12 (stalking): ط ل ع B010, the arrow rising past its target, against the fire's rising that stops on the hearts. ط ل ع B004, the scouts.
- Chain 11 (knowing) / chain 12 (stalking): د ر ي B001 knowing and B003 «تدريت الصيد إذا نظرت أين هو ولم تره بعد» in one root. «ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة» joins درى and عمد.
- Chain 13 (structure) / chain 14 (extension): مُمَدَّدَة is at once the stretched columns (B001) and the extended respite (B004). Quran 19:79 «ونمد له من العذاب مدا».
- Chain 15 (age) / chain 8 (fire): Quran 19:4 «واشتعل الرأس شيبا». Graying staged as a fire kindled on the head.
- Chain 16 (orphan) / chain 8 (eater): Quran 4:10. The orphans' wealth eaten becomes fire in the belly.
- Chain 16 (orphan) / chain 4 (counting): Quran 89:17–20. كلا, the orphan neglected, and wealth loved «حبا جما».
- Chain 17 (cushion) / chain 4 (counting): the same two words, يحسب and لينبذن, carry the counting and throwing of chain 4 and the cushion of chain 17.

## Ayat

### 104:1 وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ
وَيْلٌ has no entry in the dictionary. From memory, it is the formula of doom over the one named.
- Chain 1 (hand): هُمَزَة and لُمَزَة as squeezing, pushing and striking. Scene: a hand that squeezes, pushes and closes into a fist on wealth is opened, and he is thrown from it into the breaker of dry things.
- Chain 2 (tongue): pressed speech, the poke at the nape, whispering lips and a signalling eye. كلّ names the dulled tongue and eye; همز names the devil's pressure on the heart. Scene: a man who presses others with speech behind them and with lip and eye to their faces, whose own tongue and eye the first word calls blunt, his prod reaching hearts as the fire later reaches his.
- Chain 3 (enmity): the slander that lights feud. Scene: the slanderer kindles a fire among people, and God's kindled fire rises onto his heart.
- Chain 7 (herds): هُمَزَة as the rider's spur; كلّ as the worn-out beast and massed troops. Scene: herds gathered, counted, branded with fire and penned in stone are crushed by the pitiless driver, and the owner is driven, branded and shut in like them.
- Chain 9 (heart): كلّ as the chest (الكلكل); همز as the devil's pressure on the heart. Scene: the kindled fire rises onto the hearts, organs named for burning where his supposition sat, and crushes them with grief.
- Chain 12 (stalking): هُمَزَة as the bow with a strong thrust. Scene: as a hunter stalks game and shoots it in the heart, the fire makes for its target and does not overshoot.
- Chain 13 (structure): كلّ as encompassing, a ring set around, a curtain sewn like a house. Scene: from the first word an encompassing; at the end a door shut and a cover pressed over them, held by long columns, the gathering hands bound to the neck.
- Chain 15 (age): كلّ as the stocky strong man [fixed expression]. Scene: a man in his full strength, whose gray he supposes delayed, is touched with gray and broken by age.
- Chain 16 (orphan): كلّ as the orphan and the dependent. Scene: beside the man who gathers stands the orphan he does not carry; he himself is thrown out like a foundling.

### 104:2 ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ
- Chain 1 (hand): جَمَعَ as the closed fist and the handful. Scene: the squeezing, pushing hand closes on wealth, opens, and he is thrown from it into the crusher.
- Chain 4 (counting): gathering scattered things, wealth taken to keep, counted and readied. Scene: wealth gathered and counted by a man who reckons, then he is thrown away as not worth counting.
- Chain 5 (leaning): مَال as the thing leaned on, and the disputed "spider". Scene: he leans on wealth as prop and as "enough", supposing it will keep him; it is the debris that does not last, and the props become the fire's columns.
- Chain 6 (water): «استجمع السيل اجتمع من كل موضع» [fixed expression]; «العد مجتمع الماء … الماء الذي له مادة لا تنقطع». Scene: water gathered from everywhere into an unfailing spring, then crop and flower, then summer heat, drought and fire from the sky leave dry broken stalks.
- Chain 7 (herds): مَال as herds; gathered and counted. Scene: herds gathered, counted, branded and penned are crushed by the pitiless driver, and the owner meets the same.
- Chain 8 (hearth): جَمَعَ names the great cauldron (جامعة). Scene: fuel thrown into a kindled hearth that roasts and bakes, an eater named after Hell breaking down what it takes, rising to the heart.
- Chain 13 (structure): the fetter «تجمع اليدين إلى العنق». Scene: encompassed from the first word, then shut in under a pressed cover, long columns, hands bound to neck.
- Chain 14 (extension): عَدَّدَهُ, the count grown large, echoed by مُمَدَّدَة at the end. Scene: wealth extended and counted up, a respite extended, ending in stretched columns.
- Chain 15 (age): جمع as the body complete in its prime. Scene: the full-bodied man who supposes his gray delayed is grayed and broken.

### 104:3 يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ
- Chain 4 (counting): يحسب is defined by counting and is supposition, reckoned standing, the reckoning with God he did not make. Scene: counted wealth, a reckoning man, a man thrown away as not worth counting.
- Chain 5 (leaning): أخلد as lasting and leaning, joined to supposition in «ركن إليها ظانا أنه يخلد فيها»; يحسب as "enough". Scene: leaning on wealth as prop and sufficiency, supposing it will keep him; it is wealth «يفنى ولا يبقى», and the props are the fire's columns.
- Chain 6 (water): حسبان, fire from the sky. Scene: gathered water, an unfailing spring, crop, then heat, drought and burning from the sky leave dry debris.
- Chain 8 (hearth): أخلد names the lasting hearth-stones. Scene: a kindled hearth with fuel thrown in, roasting and devouring, rising to the heart.
- Chain 9 (heart): أخلد as الخَلَد, the mind settled in the heart. Scene: the supposition sat in the heart, and the kindled fire rises onto that heart.
- Chain 11 (knowing): يحسب as supposition and as probing what is in someone. Scene: he supposes, the listener is told he does not know, the fire knows the inside of hearts.
- Chain 15 (age): مُخلَد as the man on whom gray comes late. Scene: in his prime he supposes himself spared from graying, then he is grayed and broken.
- Chain 17 (cushion): حسبانة, the small cushion. Scene: a cushion thrown down for sitting, reversed into his being thrown into the crusher.

### 104:4 كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ
كَلَّا has no entry in the dictionary; it breaks off the supposition of 104:3. Quran 19:79, 70:15 and 89:17 open their scenes with it too.
- Chain 1 (hand): لينبذن «ألقيته من يدك»; الحطمة as breaking dry, hard things. Scene: the hand that squeezed and gathered is opened, and he is thrown from it into the breaker.
- Chain 3 (enmity): نبذ as parting in hatred, open war. Scene: the feud he kindled comes back as a fire kindled for him.
- Chain 4 (counting): thrown «لقلة الاعتداد به»; نبذ as a scrap of wealth. Scene: he counted his wealth; he is thrown out uncounted, a scrap.
- Chain 5 (leaning): «حطام الدنيا كل ما فيها من مال يفنى ولا يبقى». Scene: the wealth he leaned on to last is the debris that does not last.
- Chain 6 (water): الحطمة as the drought year and dry broken stalks. Scene: water gathered, crop flowering, then heat and drought break it into الحطام.
- Chain 7 (herds): الحطمة as the pitiless driver, the trampling herd, the lion in the herd; نبذ as the neglected ewe. Scene: the herd-owner's herds driven and crushed, and he is driven, branded and penned.
- Chain 8 (hearth): نبذ as casting into a vessel; الحطمة as the fire and the glutton named after Hell. Scene: he is cast like fuel into a kindled hearth that roasts, devours, and rises to the heart.
- Chain 10 (rising): the downward throw. Scene: thrown down, the fire climbs onto the hearts, assailing and filling, and is shut over them.
- Chain 15 (age): نبذ as a sprinkle of gray; حطم as broken by age. Scene: the man in his prime, supposing his gray delayed, is grayed and broken.
- Chain 16 (orphan): المنبوذ, the foundling. Scene: beside the hoarder stands the orphan he did not carry, and he is thrown out like a foundling.
- Chain 17 (cushion): المنبذة, the cushion thrown down to sit on. Scene: the throw of comfort reversed into the throw into the crusher.

### 104:5 وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ
الحطمة repeats, and every chain of 104:4 that runs through الحطمة is named again here (1, 5, 6, 7, 8, 15).
- Chain 11 (knowing): أدراك, knowing and being made to know; «دريت الشيء والله أدرانيه». Scene: he supposes; the listener is told he does not know; the fire, God's, knows what is inside the hearts.
- Chain 12 (stalking): درى as stalking, as making for a target in a raid (with اعتمدوه), as the target ring. Scene: as a hunter stalks, aims and shoots game in the heart, the fire makes for the hearts and does not overshoot.

### 104:6 نَارُ ٱللَّهِ ٱلْمُوقَدَةُ
- Chain 3 (enmity): نار as feud (النائرة); الموقدة as anger and war kindled. Scene: the slanderer's fire among people answered by God's kindled fire.
- Chain 5 (leaning): ٱللَّهِ against the sufficiency he gave wealth («حسبنا الله أي كافينا هو»). Scene: leaning on wealth as his enough, he meets the fire of the One the phrase names as enough.
- Chain 6 (water): نار as blossom; الموقدة as summer's worst heat. Scene: gathered water, crop and flower, then heat, drought and fire from the sky leave dry debris.
- Chain 7 (herds): نار as the camel's brand. Scene: herds branded with fire and penned are crushed by the pitiless driver, and the owner is branded with his heated wealth.
- Chain 8 (hearth): fire kindled, its fuel, its hearth. Scene: fuel cast into a kindled hearth that roasts and bakes, an eater named after Hell rising to the heart.
- Chain 9 (heart): الموقدة, the root by which the dictionary names الفؤاد. Scene: the kindled fire rises onto the kindled organ where his supposition sat.
- Chain 10 (rising): نار as light that never keeps still. Scene: thrown down, the fire climbs onto the hearts and is shut over them.
- Chain 11 (knowing): ٱللَّهِ after «والله أدرانيه». Scene: what the listener does not know, God makes known; the fire knows the hearts.

### 104:7 ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ
- Chain 6 (water): تطلع as the crop appearing and the palm's spathe. Scene: gathered water, crop and flower, then heat and drought break it into dry stalks.
- Chain 8 (hearth): الأفئدة's root as roasting meat and bread in embers, «افتأد القوم إذا أوقدوا نارا»; تطلع as vomit, the reversal of eating. Scene: fuel cast into a kindled hearth, a devouring fire that eats until it reaches the heart.
- Chain 9 (heart): الأفئدة named «التوقد», struck, gone weak; تطلع على as looking down onto the inside. Scene: the kindled fire rises onto organs named for burning, where his supposition sat, and crushes them with grief.
- Chain 10 (rising): تطلع as a sun rising, climbing to an overlook, coming upon to assail «إذا هجم» (with على), filling to the brim, and as reversal the arrow overshooting. Scene: thrown down, the fire climbs up through him onto the hearts and fills, and the cover is shut above.
- Chain 11 (knowing): تطلع على as knowing a matter whole from inside. Scene: he supposed, the listener did not know, and the fire knows the hearts.
- Chain 12 (stalking): الأفئدة as the game hit in the heart; تطلع as scouts and as the arrow that overshoots. Scene: as a hunter stalks and shoots game in the heart, the fire makes for the hearts and does not miss.

### 104:8 إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ
- Chain 7 (herds): مؤصدة's root as the stone livestock pen «للمال». Scene: herds penned in stone and driven by the pitiless herdsman; the owner shut in as they were.
- Chain 10 (rising): عليهم مؤصدة, the cover from above. Scene: thrown down, the fire rises onto the hearts and fills, and is shut over them.
- Chain 13 (structure): door shut, lid pressed down, threshold; the echo root's «نار مؤصدة أي مطبقة» (marked in the dictionary as not identity). Scene: encompassed from the first word, then a door shut and a cover pressed over them, held by long stretched columns, hands bound to neck.

### 104:9 فِى عَمَدٍۢ مُّمَدَّدَةٍۭ
- Chain 3 (enmity): عمد as anger and its pain. Scene: the slanderer's kindled feud answered by God's kindled fire.
- Chain 5 (leaning): عمد as the prop, the relied-upon, holding fast. Scene: he leaned on wealth as his prop, supposing it would keep him; his props are now the fire's columns.
- Chain 6 (water): عمد as the dam that makes water gather and the rain-soaked earth; ممددة as the river swelling, fed by another. Scene: water gathered and fed without break, crop and flower, then heat and drought leave dry debris.
- Chain 7 (herds): عمد as tent people following pasture. Scene: the herd-owner's camp, herds branded, penned and driven; the owner shut in.
- Chain 9 (heart): «القلب العميد … الذي يعمده الحزن». Scene: the kindled fire rises onto the hearts and crushes them with grief.
- Chain 12 (stalking): عمد as aiming on purpose. Scene: the fire makes for the hearts as a hunter makes for his mark, and does not overshoot.
- Chain 13 (structure): عمد as tent-pole, house column, «في عمد من النار»; ممددة as stretched lengthwise like a rope. Scene: encompassed from the first word, a door shut and a cover pressed over them, long columns stretched, hands bound to neck.
- Chain 14 (extension): ممددة as supply added («مداد كلماته أي عددها»), respite lengthened, stretching; its sound answers عَدَّدَهُ. Scene: wealth extended and counted up, a respite extended, ending in stretched columns.
- Chain 15 (age): عمد as youth at full strength. Scene: the full-bodied man who supposes his gray delayed is grayed and broken.

