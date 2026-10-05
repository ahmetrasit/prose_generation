Focus: 88:23. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

===== _commentary/v16/prompts/r13/write.md =====
Write the Turkish reading of the focus Quranic ayah for a curious reader who
knows neither Arabic nor how lexical families work, and who already has the
plain meaning. Show what a translation cannot give: the supported latent
meanings and resonances of its words, heard through their attested senses, the
ayah's neighbours, its surah and the Quran. Work from the supplied evidence and
your own knowledge of Arabic and the Quran. This is your own
interpretation, not a catalogue: maps and readings by earlier readers are
proposals, and what their members reveal together is yours to find or correct.
A surprise is welcome when the evidence supports it. There is no length limit.

Themes lead; words serve them. First understand the ayah in its grammar and
situation. Then explore its words' attested senses within and across roots,
the chains they take part in, and Quran passages that share its words or stage
the same act, scene or stance without sharing a word; a partial finding may
gain its missing support from another. Let the themes emerge from what these
reveal together, not from the familiar reading. Write the reading as those
themes: a word, a family image or a Quran passage enters where it grounds,
expands, complicates or joins a theme, developed as far as that work needs.
Never list a family's senses for their own sake, but judge each attested sense
by what it does, not by the branch it is filed under. Where this ayah's words
take part in a surah chain, that chain can found a theme here even when
another ayah completes it, and so can a scene where two such chains meet.
Every image this ayah's own words take part in is developed here as far as the
word carries it: what the object is, how it works, what usage names it. The
scene it forms with other ayat's words belongs to the surah commentary; recall
it in a sentence, tied to the ayah whose words carry it, never as something
explained before.

Keep these guards:

- A family image is heard beside the word's meaning in this ayah, never in
  place of it; say so once, where the first one enters. Show where each
  image comes from: the word, the usage that carries the image, quoted in
  Arabic, then its work in the theme. Report usage as what speakers called
  or said, varying the grammar so that no formula recurs ("… denir",
  "Araplar … derlerdi"); never name a dictionary, and never make "the family"
  a speaker.
- Keep root identity, family images and your interpretive connections
  distinct. Same word, same root and analogy are different things; an echo
  root does not establish identity.
- Explain a concrete object or mechanism by its work before drawing its
  meaning; do not flatten it into a label.
- Never invent a sense, source, vowel, etymology, historical fact, citation or
  chronology.
- Where a key word lives in Turkish as a narrowed or shifted loanword, let the
  reader feel what the Turkish word no longer carries, once.
- When you use another Quran passage, assume the reader does not know it:
  give its speaker, its situation as the Quran itself tells it there and in
  the neighbouring ayat, and the wording the connection needs. Use no hadith, no exegetes' views and no
  report from outside the Quran (no occasion of revelation, no name the Quran
  does not give, no date): the Quran, the supplied dictionary and Arabic usage
  carry the reading.
- The prose never talks about its own sources or process and never hedges in
  the first person ("hafızadan", "bildiğim kadarıyla", "sözlük", the map, its
  chains, workflow language; branch IDs only in tag sources).
  A claim about Arabic that neither the supplied texts nor the Quran text can
  check goes in the ledger as memory.

Write continuous prose in `##` sections, one theme each, warm and direct:
explain, do not dramatize; no lists and no closing recap.

Every Arabic quotation (Quran or dictionary phrase) goes in the reader
tag, as normal prose, never in quotation marks or backticks, and every tag
ends with its source, so the reader can check it:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning, source:…}
- a dictionary phrase or a branch's sense: source:"<root letters>,<branch id>",
  e.g. source:"ق و م,B016";
- a Quran quotation: source:<surah:ayah>, e.g. source:72:16, the one ayah that
  holds the quoted words, no ranges;
- Arabic from your own memory that is not in the supplied dictionary:
  source:"memory".
A branch's sense given in Turkish without its Arabic, and a Quran passage named
without quoting it, carry the source alone: {source:"ق و م,B016"},
{source:15:41}. Never write a Quran reference outside a tag; quote the
surah's own words in tags too, and name its ayat in words ("dördüncü ayet"). The gloss gives
the ayah's word by its meaning here, a family image by that image. Copy Quran
Arabic from the supplied text or the lookup.

Output: the prose; then a line containing only
=== LEDGER ===
then, in plain English, one short line per item, a few words each:
- memory: <a claim about Arabic the texts cannot check>
- not written: <finding> - <why it could not found, reshape or join a theme>


===== _commentary/v16/prompts/r13/additions.md =====
No additions: write.md is the whole brief.


===== _commentary/v16/work/88_23/D.r13/context.md =====
# 88:23 — focus

إِلَّا مَن تَوَلَّىٰ وَكَفَرَ

Anchor translation (canonical reading, reference only):

Ancak kim yüz çevirir ve inkâr ederse,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | إِلَّا | إِلَّا |  | EXP |
| 2 | مَن | مَن |  | REL |
| 3 | تَوَلَّىٰ | تَوَلَّىٰ | و ل ي | V |
| 4 | وَكَفَرَ | كَفَرَ | ك ف ر | CONJ;V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 88 — full text (context; no pericope)

- 88:1 هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ
- 88:2 وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ
- 88:3 عَامِلَةٌۭ نَّاصِبَةٌۭ
- 88:4 تَصْلَىٰ نَارًا حَامِيَةًۭ
- 88:5 تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
- 88:6 لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
- 88:7 لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
- 88:8 وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ
- 88:9 لِّسَعْيِهَا رَاضِيَةٌۭ
- 88:10 فِى جَنَّةٍ عَالِيَةٍۢ
- 88:11 لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ
- 88:12 فِيهَا عَيْنٌۭ جَارِيَةٌۭ
- 88:13 فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ
- 88:14 وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ
- 88:15 وَنَمَارِقُ مَصْفُوفَةٌۭ
- 88:16 وَزَرَابِىُّ مَبْثُوثَةٌ
- 88:17 أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ
- 88:18 وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ
- 88:19 وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- 88:20 وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- 88:21 فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- 88:22 لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 88:23 ◀ focus إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- 88:24 فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_23/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## و ل ي (root_001684) — identity root of تَوَلَّىٰ (w3)

- **B001** aralıksız yakınlık — yakınlık ve bitişiklik · sana yakın veya yanında olan şey · bir eve bitişik olan ev
  أصل صحيح يدل على قرب؛ الولي القرب؛ جلس مما يليني أي يقاربني (maqayis)؛ دار فلان ولي دار فلان؛ الدار ولية أي قريبة (jamhara)؛ الولي القرب والدنو؛ كل مما يليك أي مما يقاربك (sihah)؛ الولي القرب (tahdhib)؛ الولاء والتوالي أن يحصل شيئان فصاعدا حصولا ليس بينهما ما ليس منهما؛ يستعار ذلك للقرب (mufradat)
- **B002** kesintisiz ardışıklık — kesintisiz sıra · araya kesinti girmeden peş peşe oluş · şeyleri veya işleri peş peşe getirme · iki şeyi peş peşe getirmek · peş peşe isabet eden üç ok
  يوالي بين رميتين أو فعلين؛ أصبته بثلاثة أسهم ولاء؛ على الولاء أي الشيء بعد الشيء (ayn)؛ واليت بين الشيئين؛ افعل هذا على الولاء أي مرتبا (maqayis)؛ واليت بين الشيئين موالاة وولاء (jamhara)؛ والى بينهما ولاء أي تابع؛ على الولاء أي متتابعة؛ توالى عليه شهران (sihah)؛ الموالاة المتابعة؛ بثلاثة أسهم ولاء أي تباعا؛ توالت إلي كتب فلان (tahdhib)؛ الولاء والتوالي أن يحصل شيئان فصاعدا حصولا ليس بينهما ما ليس منهما (mufradat)
- **B003** bir işi üstlenip yönetme — yönetim ve yetki alanı · bir yeri veya işi yöneten kişi · başkasının işlerinden sorumlu kişi · bir işi üstlenmek
  الولاية مصدر الوالي (ayn)؛ كل من ولى أمر آخر فهو وليه (maqayis)؛ الولاية الإمارة (jamhara)؛ ولي الوالي البلد؛ تولى العمل أي تقلد؛ الولاية بالكسر السلطان (sihah)؛ الولاية التي بمنزلة الإمارة؛ ولي اليتيم الذي يلي أمره؛ ولي المرأة؛ وليت فلانا عمل ناحيته؛ توليت الأمر توليا (tahdhib)؛ الولاية تولي الأمر؛ حقيقته تولي الأمر (mufradat)
- **B004** yakın durup destek olma — dost, seven veya destekleyen kişi · destekçi, anlaşmalı dost veya yakın yoldaş · birini sevip destekleme veya kayırma · birini sevmek, desteklemek veya kayırmak
  المولى الحليف والولي؛ الموالاة اتخاذ المولى (ayn)؛ المولى الصاحب والحليف والناصر؛ كل هؤلاء من الولي وهو القرب (maqayis)؛ الولي خلاف العدو (jamhara)؛ الولى ضد العدو؛ المولى الناصر والحليف؛ الموالاة ضد المعاداة (sihah)؛ الولي التابع المحب؛ الولاية من النصرة والنسب؛ الولاية على الإيمان؛ المولى في الدين؛ الناصر؛ والى فلان فلانا إذا أحبه؛ فيواليه أي يحابيه (tahdhib)؛ يستعار للقرب من حيث الدين والصداقة والنصرة والاعتقاد؛ الولاية النصرة (mufradat)
- **B005** özel yakınlık ve bağlılık bağı — özgür bırakan, özgür bırakılan, soy yakını veya komşu gibi bağlı kişi · özgür bırakma ilişkisine bağlı özel hak ve mensubiyet · soy yakınları veya özgür bırakma bağıyla bağlı kişiler · nimet veya özgür bırakma bağı kuran kişi
  الموالي بنو العم؛ المولى المعتق والحليف والولي؛ الولي ولي النعم (ayn)؛ المولى المعتق والمعتق والصاحب والحليف وابن العم والناصر والجار؛ الولاء ولاء المعتق (maqayis)؛ المولى المعتق والمعتق وابن العم والناصر والجار؛ الولي الصهر؛ بينهما ولاء أي قرابة؛ الولاء ولاء المعتق (sihah)؛ المولى العصبة؛ المولى الحليف؛ المولى المعتق؛ ابن العم والعم والأخ والابن والعصبات كلهم؛ مولى النعمة؛ المعتق؛ يجب عليك أن تنصره وترثه (tahdhib)
- **B006** yüzünü veya dikkatini yöneltme — yüzünü bir şeye çevirmek · yüzünü o yöne dönmüş veya ona uyan kişi · kulağını veya dikkatini bir şeye vermek
  موليها أي مستقبلها بوجهه (sihah)؛ التولية تكون إقبالا؛ فول وجهك أي وجه وجهك نحوه؛ هو مستقبلها؛ متوليها أي متبعها وراضيها (tahdhib)؛ وليت سمعي كذا ووليت عيني كذا ووليت وجهي كذا أقبلت به عليه (mufradat)
- **B007** dönüp yüz çevirme [kalıp] — arkasını dönüp kaçarak uzaklaşmak · birinden yüz çevirmek ve ilgiyi kesmek
  ولى الرجل أي أدبر (ayn)؛ تولى عنه أي أعرض؛ ولى هاربا أي أدبر (sihah)؛ التولية تكون انصرافا؛ وليتم مدبرين؛ التولي يكون بمعنى الإعراض (tahdhib)؛ إذا عدي بعن اقتضى معنى الإعراض وترك قربه؛ التولي قد يكون بالجسم وقد يكون بترك الإصغاء والائتمار (mufradat)
- **B008** daha uygun ve hak sahibi olma — bir şeye daha uygun, daha layık veya daha hak sahibi olmak · iki daha haklı veya daha uygun kişi
  فلان أولى بكذا أي أحرى به وأجدر (maqayis)؛ فلان أولى بكذا أي أحرى به وأجدر (sihah)؛ فلان أولى بهذا الأمر أي أحق به؛ الأوليان أي الأحقان (tahdhib)
- **B009** yaklaşan kötü sonuç tehdidi — tehdit ve uyarı sözü; sana kötü şey yaklaştı
  أولى تهدد ووعيد؛ معناه قاربه ما يهلكه؛ أولى تحسير له على ما فاته (maqayis)؛ أولى لك تهدد ووعيد؛ معناه قاربه ما يهلكه؛ قارب أن يزيد (sihah)؛ أولى لك تهدد ووعيد؛ قاربك ما تكره؛ يحسره على ما فاته (tahdhib)
- **B010** önceki yağmuru izleyen yağmur — önceki yağmurdan sonra gelen yağmur · erken mevsim yağmurunu izleyen yağmur adı · toprağa izleyen yağmurun yağması · iyilik ardından gelen yağmur veya iyilik
  الولي المطر الذي يكون بعد الوسمي؛ وليت الأرض وليا فهي مولية (ayn)؛ الولي المطر يجيء بعد الوسمي سمي بذلك لأنه يلي الوسمي (maqayis)؛ الولي المطرة بعد الوسمي؛ وليت الأرض فهي مولية (jamhara)؛ الولي المطر بعد الوسمي؛ وليت الأرض وليا (sihah)؛ الولي المطر الذي يأتي بعد المطر؛ وليت الأرض وليا؛ أمطرني ولية منك (tahdhib)
- **B011** deve sırtı alt örtüsü — deve sırtında semer altında kullanılan örtü · semer altı örtüleri
  الولية الحلس والولايا جمعه (ayn)؛ الولية شبيهة بالبرذعة تطرح على ظهر البعير؛ الجمع ولايا (jamhara)؛ الولية البرذعة؛ التي تكون تحت البرذعة؛ الجمع الولايا (sihah)؛ الولية البرذعة وجمعها الولايا؛ البرذعة التي تحت الرحل (tahdhib)
- **B012** ele geçirip hedefe ulaşma [kalıp] — bir şeyi ele geçirmek veya ona üstün gelmek · hedefe varmak veya ona önce ulaşmak
  استولى فلان على شيء إذا صار في يده؛ استولى الفرس على الغاية أي بلغها (ayn)؛ استولى على الأمد أي بلغ الغاية (sihah)؛ استولى أحدهما على الغاية إذا سبق الآخر إليها؛ استيلاؤه على الأمد أن يغلب عليه بسبقه؛ استولى فلان على مالي إذا غلب عليه (tahdhib)
- **B013** birine iyi ya da kötü şey yöneltme [kalıp] — birine iyilik yapmak veya bir şeyi ona ulaştırmak · birine iyilik veya kötülük yöneltmek
  أوليته الشيء فوليه؛ أوليته معروفا (sihah)؛ أوليت فلانا شرا وأوليته خيرا؛ أوليته معروفا أسديته إليه (tahdhib)
- **B014** aldığı fiyatla devretme — satın alınan malı bilinen aynı fiyatla başkasına devretme
  التولية في البيع أن تشتري سلعة بثمن معلوم ثم توليها رجلا آخر بذلك الثمن (tahdhib)
- **B015** küçük sürü hayvanlarını ayırma — küçük sürü hayvanlarını büyüklerinden ayırmak · yavru develeri analarından ayırıp alıştırma
  للموالاة معنى ثالث؛ والوا حواشي نعمكم من الجلة أي اعزلوا صغارها عن كبارها؛ توالي ربعي السقاب؛ تواليه أن يفصل عن أمه (tahdhib)
- **B016** taze hurmanın kurumaya dönmesi — taze hurmanın solup kurumaya başlaması · taze hurmadaki solgun kuruma rengi
  يقال للرطب إذا أخذ في الهيج قد ولى وتولى؛ توليه شهبته (tahdhib)

## ك ف ر (root_001307) — identity root of وَكَفَرَ (w4)

- **B001** örtmek, kapatmak — bir şeyi örtmek ve kapatmak · zırhının üstüne bir giysi geçirmek · silahlarıyla örtünmek veya silah kuşanmak · rüzgârın savurduğu toprakla örtülmüş kül · güneşin yıldızları görünmez kılması
  الستر والتغطية (maqayis)؛ كل شيء غطى شيئا فقد كفره (ayn;sihah;tahdhib)؛ كفرت الشيء أي سترته ورماد مكفور (sihah)؛ تكفر في السلاح (mufradat)؛ كفرت الشمس النجوم (mufradat)
- **B002** örten karanlık veya enginlik — karanlık gece, deniz, büyük ırmak, gün batımı veya bulut
  الكافر مغيب الشمس ويقال بل البحر والنهر العظيم كافر (maqayis)؛ الكافر الليل والبحر ومغيب الشمس والكافر النهر العظيم (ayn)؛ الكافر الليل المظلم والكافر البحر والنهر العظيم (sihah)؛ الليل كافر لأنه ستر بظلمته (tahdhib)؛ وصف الليل بالكافر لستره الأشخاص والكافر للسحاب (mufradat)
- **B003** dinî gerçeği reddetme — dinî gerçeği veya inancı reddetme · kalben bildiği gerçeği diliyle kabul etmeme · gerçeği bildiği hâlde inatla kabul etmemek · kalben reddederken diliyle inanmış görünmek · gerçeği hem kalple hem dille inkâr etmek
  الكفر ضد الإيمان سمى لأنه تغطية الحق (maqayis)؛ الكفر نقيض الإيمان والكفر أربعة أنحاء كفر الجحود وكفر المعاندة وكفر النفاق وكفر الإنكار (ayn)؛ الكفر ضد الإيمان (sihah)؛ الكفر نقيض الإيمان وكفر إنكار وكفر جحود وكفر معاندة وكفر نفاق وكفر هو شرك وكفر بكتاب الله ورسوله والتكذيب بالله (tahdhib)؛ أعظم الكفر جحود الوحدانية أو الشريعة أو النبوة (mufradat)
- **B004** nimeti yadsıma — nimeti yadsımak ve şükrünü yerine getirmemek · nimeti yadsıma ve şükretmeme · nimetleri aşırı biçimde yadsıyan kimse · iyilikleri karşılıksız ve teşekkürsüz kalan cömert adam
  كفران النعمة جحودها وسترها (maqayis)؛ الكفر نقيض الشكر كفر النعمة أي لم يشكرها (ayn)؛ الكفر أيضا جحود النعمة وهو ضد الشكر (sihah)؛ الكفر كفر النعمة وهو نقيض الشكر (tahdhib)؛ كفر النعمة وكفرانها سترها بترك أداء شكرها (mufradat)
- **B005** bağını reddedip uzaklaşmak — bir şeyle bağını reddedip ondan uzaklaşmak
  يكون الكفر أيضا بمعنى البراءة (tahdhib)؛ قد يعبر عن التبري بالكفر (mufradat)
- **B006** inançsız saymak — birini inançsız saymak veya öyle adlandırmak
  أكفرت الرجل أي دعوته كافرا لا تكفر أحدا (sihah)؛ أكفره إكفارا حكم بكفره (mufradat)
- **B007** itaatsizliğe zorlamak — itaat eden birini itaatsizliğe zorlamak
  إذا ألجأت مطيعك إلى أن يعصيك فقد أكفرته (ayn;tahdhib)
- **B008** tohumu örten çiftçi — tohumu toprakla örten çiftçi · tohumları toprakla örten çiftçiler
  يقال للزارع كافر لأنه يغطى الحب بتراب الأرض (maqayis)؛ الكافر الزارع لأنه يغطي البذر بالتراب (sihah)؛ الزراع لستره البذر في الأرض (mufradat)؛ الكفار الزراع (mufradat)
- **B009** günah yükünü giderme — günahı veya bozulan yeminin yükünü gideren karşılık · bozulan yeminin gerektirdiği yükümlülüğü yerine getirme · günahları örtüp etkisini silme
  الكفارة ما يكفر به من الخطيئة واليمين فيمحى به (ayn)؛ تكفير اليمين فعل ما يجب بالحنث فيها والاسم الكفارة والتكفير في المعاصي (sihah)؛ الكفارة ما يغطي الإثم والتكفير ستره وتغطيته حتى يصير بمنزلة ما لم يعمل (mufradat)
- **B010** çiçek veya meyve kılıfı — üzüm salkımının veya hurma çiçeğinin kılıfı · hurma çiçeğinin ya da meyvenin kılıfı · hurma ağacından çıkan kapalı çiçek kılıfları
  الكافور كم العنب قبل أن ينور وسمى كافورا لأنه كفر الوليع أي غطاه (maqayis)؛ الكافور كم العنب قبل أن ينور وكافوره ورقة الذي يستره والكافور الطلع والكفرى والكوافير (ayn)؛ الكافور الطلع ووعاء طلع النخل وكذلك الكفرى (sihah)؛ الكافور اسم أكمام الثمرة التي تكفرها والكافور أكمام الثمرة (mufradat)
- **B011** koku maddesi, su kaynağı veya bitki — güzel kokulu karışımlarda kullanılan madde · cennetteki bir su kaynağı · çiçeği papatyaya benzeyen bir bitki
  الكافور شيء من أخلاط الطيب والكافور عين ماء في الجنة والكافور نبات نوره كنور الأقحوان (ayn)؛ الكافور من الطيب (sihah)؛ الكافور الذي هو من الطيب (mufradat)
- **B012** uzak arazi; köy, uzak yer halkı veya mezar — insanlardan uzak, pek uğranmayan arazi · köy veya mezar · köyler veya uzak yerlerin halkı
  الكفر من الأرض ما بعد من الناس وأهل الكفور والقرى (maqayis)؛ الكافر من الأرض ما بعد عن الناس والكفور القرى (ayn)؛ الكفر أيضا القرية والكفر أيضا القبر (sihah)؛ الكافر من الأرض ما بعد عن الناس (tahdhib)
- **B013** dağ geçidi; iri dağ veya alçak duvar — dağ geçitleri · dağ geçidi veya iri dağ · alçak duvar
  الكفرات والكفر الثنايا من الجبال (maqayis)؛ الكفر الثنايا من الجبال (ayn)؛ الكفر العظيم من الجبال (sihah)؛ الكافر الحائط الواطىء (tahdhib)
- **B014** eğilerek boyun eğme gösterisi — başını eğmek veya elini göğsüne koyup eğilmek
  التكفير إيماء الذمي برأسه لا يقال سجد له وإنما يقال كفر له (ayn)؛ التكفير أن يخضع الإنسان لغيره يضع يده على صدره ويتطامن له (sihah)
- **B015** hükümdara taç giydirme veya taç — hükümdara taç giydirme veya tacın kendisi
  التكفير تتويج الملك بتاج والتكفير ههنا التاج نفسه (ayn)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:23, and ## Buluşmalar) =====
## Örten: Gâşiye, bahçe ve örtüsünü yitiren

Sure bir soruyla açılır: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. Gâşiye "üstüne gelip örten" demektir. Kökün temel işi, bir şeyi başka bir şeyle kaplamaktır: {ar:أصل صحيح يدل على تغطية شيء بشيء, tr:aslun sahîhun yedullü alâ tağtiyeti şey'in bi-şey', gloss:bir şeyin başka bir şeyle örtülmesini gösteren sağlam kök, source:"غ ش و,B001"}. Kelimenin elle tutulur bir karşılığı da vardır. Eyerin üstüne atılan örtüye de bu ad verilir: {ar:وغاشية السرج غطاؤه, tr:ve ğâşiyetü's-serci ğıtâuhû, gloss:eyerin gâşiyesi onun örtüsüdür, source:"غ ش و,B001"}. Böyle bir örtü yukarıdan atılır, eyeri her yanından sarar ve altında kalanı gözden saklar. Kıyamet bu adla anıldığında aynı hareket bütün yaratılmışlara uygulanmış olur: {ar:الغاشية القيامة لأنها تغشى الخلق بإفزاعها, tr:el-ğâşiyetü'l-kıyâmetü li-ennehâ tağşe'l-halka bi-ifzâıhâ, gloss:Gâşiye kıyamettir çünkü yaratılmışları dehşetiyle örter, source:"غ ش و,B002"}. Örtü dışarıda da kalmaz. Aynı fiil, başa gelen bir şeyin aklı kapatmasını, yani bayılmayı da anlatır: {ar:غشي على فلان إذا نابه ما غشي فهمه, tr:ğuşiye alâ fülânin izâ nâbehû mâ ğaşiye fehmehû, gloss:başına gelen şey anlayışını örtünce falan bayıldı denir, source:"غ ش و,B005"}. Demek ki ilk ayetteki tek kelimede bir örtü duyulur: dışarıdan iner, her yanı kuşatır ve içeriye, akla kadar işler. Kelimeyi yalnızca "kıyamet" diye karşılamak bu hareketi kaybettirir.

Bu yazı boyunca geçerli bir kural var: Bir kelimenin akrabalarından gelen resimler, o kelimenin ayetteki anlamının yerine geçmez, o anlamın yanında duyulur. Gâşiye burada o günün adıdır. Eyer örtüsü ve baygınlık yalnızca bu adın nasıl işlediğini gösterir.

Örtünün ilk indiği yer yüzlerdir: {ar:وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ, tr:vucûhun yevmeizin hâşia, gloss:o gün birtakım yüzler eğik ve ezik, source:88:2}. Yüz, bir şeyin karşıya dönük ön tarafıdır: {ar:الوجه مستقبل كل شيء, tr:el-vechu müstakbelü külli şey', gloss:yüz her şeyin karşıya bakan önüdür, source:"و ج ه,B001"}. Kur'an bu sahneyi başka yerlerde açıkça kurar. Suçluların o gün zincirlere vurulduğu anlatılırken şöyle denir: {ar:سَرَابِيلُهُم مِّن قَطِرَانٍۢ وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:serâbîluhum min katırânin ve tağşâ vucûhehumu'n-nâr, gloss:gömlekleri katrandandır ve yüzlerini ateş örter, source:14:50}. Kötülük kazananlar için başka bir yerde verilen benzetme, örtüyü gecenin kendisinden yapar: {ar:كَأَنَّمَآ أُغْشِيَتْ وُجُوهُهُمْ قِطَعًۭا مِّنَ ٱلَّيْلِ مُظْلِمًا, tr:keennemâ uğşiyet vucûhuhum kıtaan mine'l-leyli muzlimâ, gloss:sanki yüzlerine karanlık geceden parçalar örtülmüş, source:10:27}.

Surenin ilk ve son adları tek bir ayette bir araya gelir. Yusuf kıssasının sonunda Allah, Peygamber'e insanların çoğunun inanmadığını söyledikten sonra sorar: {ar:أَفَأَمِنُوٓا۟ أَن تَأْتِيَهُمْ غَٰشِيَةٌۭ مِّنْ عَذَابِ ٱللَّهِ, tr:e-fe-eminû en te'tiyehum ğâşiyetun min azâbillâh, gloss:Allah'ın azabından örten bir şeyin kendilerine gelmesinden emin mi oldular, source:12:107}. Bu ayette surenin ilk fiili (gelmek), ilk adı (örten) ve yirmi dördüncü ayetteki azap aynı cümlededir. Kelimenin açıklaması da bunu söyler: {ar:غاشية من عذاب الله أي عقوبة مجللة تعمهم, tr:ğâşiyetun min azâbillâh ey ukûbetun mücellele teummuhum, gloss:hepsini saran ve kapsayan bir ceza, source:"غ ش و,B002"}. Duhan suresinde Allah, Peygamber'e şüphe içinde oyalananları gösterir ve göğün apaçık bir duman getireceği günü beklemesini söyler. O duman için de şöyle denir: {ar:يَغْشَى ٱلنَّاسَ ۖ هَٰذَا عَذَابٌ أَلِيمٌۭ, tr:yağşe'n-nâs hâzâ azâbun elîm, gloss:insanları örter; bu acı bir azaptır, source:44:11}. Azabın çabuk gelmesini isteyenler için de örtü dört yandan tamamlanır: {ar:يَوْمَ يَغْشَىٰهُمُ ٱلْعَذَابُ مِن فَوْقِهِمْ وَمِن تَحْتِ أَرْجُلِهِمْ, tr:yevme yağşâhumu'l-azâbu min fevkıhim ve min tahti ercülihim, gloss:azabın onları üstlerinden ve ayaklarının altından örteceği gün, source:29:55}. Eyer örtüsü yalnızca üstten sarardı. Burada örtü alttan da kapanır.

Onuncu ayet ikinci bir örtü getirir: {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüce bir bahçede, source:88:10}. Bu kökün aslı da örtmektir: {ar:أصل الجن ستر الشيء عن الحاسة, tr:aslu'l-cenni setru'ş-şey'i ani'l-hâsse, gloss:bir şeyi duyulardan gizlemek, source:"ج ن ن,B001"}. Bahçe adını ağaçlarının toprağı örtmesinden alır: {ar:كل بستان ذي شجر يستر بأشجاره الأرض, tr:küllü büstânin zî şecerin yesturu bi-eşcârihi'l-ard, gloss:ağaçlarıyla toprağı örten her bostan, source:"ج ن ن,B003"}. Ödül de bugün göze görünmeyen, örtülü bir şeydir: {ar:الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم, tr:el-cennetü mâ yasîru ileyhi'l-müslimûne fi'l-âhira ve huve sevâbun mestûrun anhumu'l-yevm, gloss:cennet bugün onlardan gizli olan ödüldür, source:"ج ن ن,B004"}. Aynı kökten kalkan da çıkar: {ar:المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك, tr:el-micennu't-türsü ve'l-cünnetü'd-dir'u ve küllü mâ vakâke fe-huve cünnetük, gloss:seni koruyan her şey senin kalkanındır, source:"ج ن ن,B008"}. Böylece surede iki örtü karşı karşıya durur. Biri yukarıdan iner ve ezer. Öteki aşağıdan büyür, gölgeler ve korur. Bahçe halkı bu ikinci örtüyü birincisinden kurtuluş olarak anar. Birbirlerine dönüp ailelerinin arasındayken nasıl korku içinde yaşadıklarını hatırladıktan sonra şöyle derler: {ar:فَمَنَّ ٱللَّهُ عَلَيْنَا وَوَقَىٰنَا عَذَابَ ٱلسَّمُومِ, tr:fe-mennallâhu aleynâ ve vekânâ azâbe's-semûm, gloss:Allah bize lütfetti ve bizi kavurucu azaptan korudu, source:52:27}. Burada "korumak" fiili, kalkanın tanımındaki fiilin ta kendisidir. Dördüncü ayetteki ateş sıfatı حامية'nin kökü de başka kullanımında korunan yeri anlatır: {ar:الحمى موضع فيه كلأ يحمى من الناس أن يرعى, tr:el-himâ mevziun fîhi keleun yuhmâ mine'n-nâsi en yur'â, gloss:otlu olup insanların otlatmasından korunan yer, source:"ح م ي,B002"}. Bu anlam ayetteki kızgın ateşin yanında duyulur: aynı harflerin koruyan yüzü ateşe girenler için kapanmıştır.

Yirmi üçüncü ayetteki inkâr da bir örtme fiilidir: {ar:كل شيء غطى شيئا فقد كفره, tr:küllü şey'in ğattâ şey'en fe-kad keferahû, gloss:bir şeyi örten her şey onu kefr etmiştir, source:"ك ف ر,B001"}. Kelime imanın karşıtı olarak da bu yüzden kullanılır: {ar:الكفر ضد الإيمان سمى لأنه تغطية الحق, tr:el-küfru zıddü'l-îmân summiye li-ennehû tağtiyetü'l-hak, gloss:küfür imanın zıddıdır; hakkı örttüğü için bu adı almıştır, source:"ك ف ر,B003"}. Tohumu toprakla örten çiftçiye de bu ad verilir: {ar:الكافر الزارع لأنه يغطي البذر بالتراب, tr:el-kâfiru'z-zâriu li-ennehû yuğattı'l-bezra bi't-turâb, gloss:kâfir tohumu toprakla örten ekincidir, source:"ك ف ر,B008"}. Çiftçinin örtüsünden bir bahçe çıkabilir; hakkı örtenin örtüsünden hiçbir şey bitmez. Kur'an inkârla göz üstündeki örtüyü aynı ayette birleştirir. Uyarılsalar da uyarılmasalar da inanmayacakları söylenenler için şöyle denir: {ar:وَعَلَىٰٓ أَبْصَٰرِهِمْ غِشَٰوَةٌۭ ۖ وَلَهُمْ عَذَابٌ عَظِيمٌۭ, tr:ve alâ ebsârihim ğışâvetun ve lehum azâbun azîm, gloss:gözlerinin üstünde bir perde vardır ve onlar için büyük bir azap vardır, source:2:7}. Buradaki perde, Gâşiye ile aynı köktendir. Hakkı örten, sonunda kendi gözünün de örtüldüğünü görür. Gece de surenin üç ayrı kökünde örtü olarak anılır: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylü kâfirun li-ennehû setera bi-zulmetih, gloss:gece karanlığıyla örttüğü için kâfirdir, source:"ك ف ر,B002"}; {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰ, tr:ve'l-leyli izâ yağşâ, gloss:örttüğü zaman geceye andolsun, source:92:1}; İbrahim'in gece karşısındaki anında ise {ar:فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ, tr:fe-lemmâ cenne aleyhi'l-leyl, gloss:gece onu örtünce, source:6:76}. Bunlar aynı kökten değildir. Üç ayrı kökün paylaştığı tek bir resimdir.

Son adım yirmi dördüncü ayettedir. Azap ceza demektir: {ar:العذاب العقوبة وقد عذبته تعذيبا, tr:el-azâbu'l-ukûbe ve kad azzebtühû ta'zîbâ, gloss:azap cezadır, source:"ع ذ ب,B005"}. Aynı kökün bir başka kolu ise örtüsüz kalmış insanı anlatır: {ar:العذوب الذي ليس بينه وبين السماء ستر وكذلك العاذب, tr:el-azûbu'llezî leyse beynehû ve beyne's-semâi sitr, gloss:kendisiyle gök arasında hiçbir örtü bulunmayan kimse, source:"ع ذ ب,B004"}. Bu anlam ayetteki cezanın yanında duyulduğunda resim tamamlanır. Azap gören hem ezici örtünün altında kalmış hem de kendisini koruyan bütün örtülerden soyulmuştur. Bahçedeki insanın üstünde ise ağaçlardan bir örtü vardır, onu ezen hiçbir şey yoktur.

Kaynaklar: 88:1 ٱلْغَٰشِيَةِ غ ش و B001; 88:1 ٱلْغَٰشِيَةِ غ ش و B002; 88:1 ٱلْغَٰشِيَةِ غ ش و B005; 88:2 وُجُوهٌ و ج ه B001; 88:4 حَامِيَةً ح م ي B002; 88:10 جَنَّةٍ ج ن ن B001; 88:10 جَنَّةٍ ج ن ن B003; 88:10 جَنَّةٍ ج ن ن B004; 88:10 جَنَّةٍ ج ن ن B008; 88:23 وَكَفَرَ ك ف ر B001; 88:23 وَكَفَرَ ك ف ر B002; 88:23 وَكَفَرَ ك ف ر B003; 88:23 وَكَفَرَ ك ف ر B008; 88:24 ٱلْعَذَابَ ع ذ ب B004; 88:24 ٱلْعَذَابَ ع ذ ب B005

## Ateş, kaynar su ve pişme

Dördüncü ayet şöyledir: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4}. Fiil, ateşin içine girip onun sıcaklığına katlanmayı anlatır: {ar:صلي الرجل نارا إذا أدخلته النار, tr:saliye'r-raculu nâran izâ edhaltehu'n-nâr, gloss:adamı ateşe soktuğunda saliye denir, source:"ص ل ي,B003"}. Fiili açıklayan cümlede, ateşe gireni surenin kendisi adlandırır: {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:salâ'l-kâfiru nâran fe-huve yaslâhâ ey kâsâ harrahâ ve şiddetehâ, gloss:kâfir ateşe girdi yani sıcaklığına ve şiddetine katlandı, source:"ص ل ي,B003"}. Dördüncü ayetteki fiil ile yirmi üçüncü ayetteki inkâr, bu cümlede birleşir. Ateşin sıfatı, demirin ateşte kızdırılmasını anlatan kelimedir: {ar:الحامية الحارة, tr:el-hâmiyetü'l-hârra, gloss:hâmiye sıcak olandır, source:"ح م ي,B001"}; {ar:أحميت الحديد في النار فهو محمى, tr:ahmeytü'l-hadîde fi'n-nâri fe-huve muhmâ, gloss:demiri ateşte kızdırdım; o kızgındır, source:"ح م ي,B001"}. Beşinci ayetteki pınarın sıfatı ise sıcaklığın en uç noktasıdır: {ar:حميم آن قد انتهى حره وعين آنية, tr:hamîmun ân kad intehâ harruhû ve aynun âniye, gloss:sıcaklığı son noktaya varmış kaynar su ve âniye pınar, source:"ء ن ي,B003"}; {ar:بلغ إناه من شدة الحر, tr:belağa inâhu min şiddeti'l-harr, gloss:sıcaklığın şiddetinden son noktasına vardı, source:"ء ن ي,B003"}. Surenin "âniye pınar" sözü, Arapçada böyle bir terkip olarak da kullanılır.

Bu kelimeler mutfakta da kullanılır ve o kullanım ayetin anlamının yanında duyulur. Ateşe girme fiili et kızartmayı da anlatır: {ar:صليت اللحم صليا شويته, tr:saleytü'l-lahme salyen şeveytüh, gloss:eti kızarttım, source:"ص ل ي,B004"}. Ateşin sıfatı kızmış fırın için de söylenir: {ar:حمى النهار وحمي التنور أي اشتد حره, tr:hamiye'n-nehâru ve hamiye't-tennûru ey iştedde harruh, gloss:gün ve tandır kızdı, sıcaklığı arttı, source:"ح م ي,B001"}. Pınarın sıfatının kökü yemeğin pişme anını adlandırır: {ar:انتظرنا إنى الطعام أي إدراكه, tr:intazarnâ inâ't-taâmi ey idrâkeh, gloss:yemeğin pişmesini bekledik, source:"ء ن ي,B003"}. Yiyecek adı ضريع'in kökü de tencerenin pişmek üzere olduğunu söyler: {ar:ضرعت القدر أي حان أن تدرك, tr:daraati'l-kıdru ey hâne en tudrik, gloss:tencerenin pişme vakti geldi, source:"ض ر ع,B007"}. Üçüncü ayetteki yorgunluk kelimesinin kökü de ocağın üstüne kurulan sacayağına ad verir: {ar:نصبت للقطاة شركا ونصبت للقدر نصبا, tr:nasabtü li'l-katâti şereken ve nasabtü li'l-kıdri nasbâ, gloss:bağırtlağa tuzak kurdum ve tencereye ayak kurdum, source:"ن ص ب,B001"}. Böylece dördüncü, beşinci ve altıncı ayetlerin kelimeleri bir mutfağın dilini konuşur: kızgın fırın, kızaran et, son kıvamına varan sıcaklık, pişmek üzere olan tencere. Kur'an bu dili ateş için açıkça kullanır: {ar:سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا۟ ٱلْعَذَابَ, tr:sevfe nuslîhim nâran küllemâ nadicet cülûduhum beddelnâhum cülûden ğayrahâ li-yezûku'l-azâb, gloss:onları ateşe sokacağız; derileri piştikçe azabı tatsınlar diye başka derilerle değiştireceğiz, source:4:56}. Bu ayette ateşe sokma fiili, pişme fiili ve tatma fiili bir aradadır. Mümin kıvamını beklemesin diye uyarılan yemeğin dili de aynıdır. Allah, müminlere Peygamber'in evlerine nasıl girileceğini öğretirken şöyle der: {ar:إِلَىٰ طَعَامٍ غَيْرَ نَٰظِرِينَ إِنَىٰهُ, tr:ilâ taâmin ğayra nâzırîne inâh, gloss:pişme vaktini gözetmeden bir yemeğe, source:33:53}. Bu tek ayette beşinci ayetteki pişme anının kökü, altıncı ayetteki yemek ve on yedinci ayetteki bakış kelimesi bir araya gelir.

Aynı iki komşu kelime, üçüncü ayetteki nâsıba ile dördüncü ayetteki taslâ, avcı dilinde de birbirine bağlanır. Kurmak fiili tuzak kurmayı anlatır, ve ateşe girme kökü tuzağın adıdır. Bu tuzak da kurmak fiiliyle tanımlanır: {ar:المصلاة أن تنصب شركا ونحوه, tr:el-maslâtü en tensibe şereken ve nahveh, gloss:maslât tuzak ve benzerini kurmaktır, source:"ص ل ي,B005"}. Bu yan anlamda emeğiyle yorulan yüz, kendi kurduğu tuzağa yürüyen kuş gibidir. Ayetteki anlam yine yorgunluk ve ateştir.

Kur'an bu ateşi başka yerlerde de aynı kelimelerle anar. Kâria suresinde terazisi hafif gelen için {ar:نَارٌ حَامِيَةٌۢ, tr:nârun hâmiye, gloss:kızgın bir ateş, source:101:11} denir. Önceki surede hatırlatmadan kaçan bedbaht {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâre'l-kübrâ, gloss:en büyük ateşe girecek olan, source:87:12} diye anılır. Leyl suresi ateşe gireni surenin yirmi üçüncü ayetindeki fiille tanımlar: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}; {ar:ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ, tr:ellezî kezzebe ve tevellâ, gloss:yalanlayıp yüz çeviren, source:92:16}. Kaynar su da başka yerlerde aynı sıfatla geçer: {ar:يَطُوفُونَ بَيْنَهَا وَبَيْنَ حَمِيمٍ ءَانٍۢ, tr:yetûfûne beynehâ ve beyne hamîmin ân, gloss:onunla son noktasına varmış kaynar su arasında dolaşırlar, source:55:44}. Kaynar sudan içirilenler için {ar:وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ, tr:ve sukû mâen hamîmen fe-kattaa em'âehum, gloss:kaynar su içirilip bağırsakları parçalanır, source:47:15} denir. Allah Peygamber'e "hak Rabbinizdendir, dileyen inansın, dileyen inkâr etsin" demesini söyledikten sonra yardım isteyenlere verilecek suyu anlatır: {ar:بِمَآءٍۢ كَٱلْمُهْلِ يَشْوِى ٱلْوُجُوهَ, tr:bi-mâin ke'l-mühli yeşvi'l-vucûh, gloss:yüzleri kavuran erimiş maden gibi bir su, source:18:29}. Buradaki "kavurmak" fiili, eti kızartmanın açıklamasında geçen fiildir. Kaynar su yüze dökülür ve onu pişirir. Zakkum ağacı günahkârın yiyeceğidir: {ar:كَٱلْمُهْلِ يَغْلِى فِى ٱلْبُطُونِ, tr:ke'l-mühli yağlî fi'l-butûn, gloss:erimiş maden gibi karınlarda kaynar, source:44:45}; {ar:كَغَلْىِ ٱلْحَمِيمِ, tr:ke-ğalyi'l-hamîm, gloss:kaynar suyun kaynaması gibi, source:44:46}. Kur'an bunu içenlerin nasıl içtiğini de söyler: {ar:فَشَٰرِبُونَ شُرْبَ ٱلْهِيمِ, tr:fe-şâribûne şurbe'l-hîm, gloss:susuzluk hastalığına tutulmuş develer gibi içerler, source:56:55}.

Kaynaklar: 88:3 نَّاصِبَةٌ ن ص ب B001; 88:4 تَصْلَىٰ ص ل ي B003; 88:4 تَصْلَىٰ ص ل ي B004; 88:4 تَصْلَىٰ ص ل ي B005; 88:4 حَامِيَةً ح م ي B001; 88:5 ءَانِيَةٍ ء ن ي B003; 88:6 ضَرِيعٍ ض ر ع B007; 88:23 كَفَرَ ك ف ر B003

## Hatırlatıcı, gözetmen değil

Yirmi birinci ayet Peygamber'in işini tek bir kelimeye indirir: hatırlatmak. "Ancak" sözü bu işin sınırını çizer. Hatırlatma, bir şeyin akla getirilmesini sağlayan şeydir ve tekrar edilir: {ar:التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر, tr:et-tezkiretü mâ yütezekkeru bihi'ş-şey' ve'z-zikrâ kesretü'z-zikr, gloss:tezkire bir şeyin hatırlandığı araçtır; zikra çok anmaktır, source:"ذ ك ر,B009"}. Yirmi ikinci ayet de bu işin olmadığı şeyi söyler: {ar:لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ, tr:leste aleyhim bi-musaytır, gloss:sen onların üstünde bir gözetmen değilsin, source:88:22}. Musaytır, bir şeyin başına konup onu gözeten ve yaptığını yazan kişidir: {ar:المسيطر والمصيطر المسلط على الشيء ليشرف عليه ويتعهد أحواله ويكتب عمله, tr:el-museytıru ve'l-musaytıru'l-musallatu ale'ş-şey'i li-yuşrife aleyhi ve yeteahhede ahvâlehû ve yektübe amelehû, gloss:bir şeyin başına konup onu gözeten halini kollayan ve işini yazan kişi, source:"س ط ر,B003"}; {ar:السيطرة مصدر المسيطر وهو كالرقيب الحافظ المتعهد للشيء, tr:es-saytaratu masdaru'l-museytır ve huve ke'r-rakîbi'l-hâfızı'l-müteahhidi li'ş-şey', gloss:bir şeyi bekleyen ve koruyan gözcü gibi olan, source:"س ط ر,B003"}. Bu yetkinin asıl sahipleri efendilerdir: {ar:المسيطرون الأرباب المسلطون, tr:el-museytırûne'l-erbâbü'l-musallatûn, gloss:başa geçirilmiş efendiler, source:"س ط ر,B003"}. Kökün aslı satırdır: {ar:أصل مطرد يدل على اصطفاف الشيء كالكتاب والشجر, tr:aslun muttaridun yedullü ale'stıfâfi'ş-şey'i ke'l-kitâbi ve'ş-şecer, gloss:yazı ve ağaç gibi şeylerin dizilişini gösteren kök, source:"س ط ر,B001"}; {ar:السطر سطر من كتب وسطر من شجر مغروس, tr:es-satru satrun min kütübin ve satrun min şecerin mağrûs, gloss:satır yazıdan bir satır ve dikilmiş ağaçtan bir sıradır, source:"س ط ر,B001"}. Gözetmen, kayıtları satır satır tutan kişidir. Bu kökün tanımında geçen diziliş kelimesi, on beşinci ayette yastıkların dizilişini anlatan kelimedir. Bu bağ kök birliğinden değil, kelimelerin açıklamasından gelir. Bahçede yastıkları dizen bir el vardır. Amelleri satıra dizen el de vardır, ama Peygamber'in eli değildir.

Kur'an bu kaydı Allah'a bağlar. Önceki kavimlerin anlatıldığı surenin sonunda şöyle denir: {ar:وَكُلُّ صَغِيرٍۢ وَكَبِيرٍۢ مُّسْتَطَرٌ, tr:ve küllü sağîrin ve kebîrin mustatar, gloss:küçük büyük her şey satır satır yazılmıştır, source:54:53}. Buradaki "yazılmış" kelimesi musaytır ile aynı köktendir. Kur'an'da bu kelimenin geçtiği tek başka yer, inkârcılara sorulan bir sorudur: {ar:أَمْ عِندَهُمْ خَزَآئِنُ رَبِّكَ أَمْ هُمُ ٱلْمُصَۣيْطِرُونَ, tr:em indehum hazâinu rabbike em humu'l-musaytırûn, gloss:yoksa Rabbinin hazineleri onların yanında mı, yoksa gözetmenler onlar mı, source:52:37}. Gözetmenlik ne Peygamber'indir ne de onu reddedenlerin.

Kur'an bu sınırı başka yerlerde de çizer. Kaf suresinin sonunda Allah şöyle der: {ar:وَمَآ أَنتَ عَلَيْهِم بِجَبَّارٍۢ ۖ فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ, tr:ve mâ ente aleyhim bi-cebbârin fe-zekkir bi'l-Kur'âni men yehâfu vaîd, gloss:sen onları zorlayan değilsin; tehdidimden korkana Kur'an ile hatırlat, source:50:45}. Başka yerlerde de {ar:فَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ حَفِيظًا ۖ إِنْ عَلَيْكَ إِلَّا ٱلْبَلَٰغُ, tr:fe-mâ erselnâke aleyhim hafîzan in aleyke ille'l-belâğ, gloss:seni onların üstüne bekçi göndermedik; sana düşen yalnızca duyurmaktır, source:42:48} ve {ar:وَمَا جَعَلْنَٰكَ عَلَيْهِمْ حَفِيظًۭا ۖ وَمَآ أَنتَ عَلَيْهِم بِوَكِيلٍۢ, tr:ve mâ cealnâke aleyhim hafîzan ve mâ ente aleyhim bi-vekîl, gloss:seni onlara bekçi yapmadık; sen onların vekili de değilsin, source:6:107} denir. Cezalandırmak da Allah'ın işidir: {ar:إِن يَشَأْ يَرْحَمْكُمْ أَوْ إِن يَشَأْ يُعَذِّبْكُمْ ۚ وَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ وَكِيلًۭا, tr:in yeşe' yerhamkum ev in yeşe' yuazzibkum ve mâ erselnâke aleyhim vekîlâ, gloss:dilerse size merhamet eder, dilerse azap eder; seni onlara vekil göndermedik, source:17:54}. Zorlama da sorunun içinde reddedilir: {ar:أَفَأَنتَ تُكْرِهُ ٱلنَّاسَ حَتَّىٰ يَكُونُوا۟ مُؤْمِنِينَ, tr:e-fe-ente tukrihu'n-nâse hattâ yekûnû mu'minîn, gloss:inanan olsunlar diye insanları sen mi zorlayacaksın, source:10:99}.

Yirmi üçüncü ayetteki istisna bu sınırın içinden çıkar: {ar:إِلَّا مَن تَوَلَّىٰ وَكَفَرَ, tr:illâ men tevellâ ve kefer, gloss:ancak yüz çevirip inkâr eden, source:88:23}. Yüz çevirme fiilinin kökü bir göreve geçmeyi de anlatır: {ar:تولى العمل أي تقلد, tr:tevelle'l-amele ey tekalled, gloss:işi üstlendi yani göreve geçti, source:"و ل ي,B003"}. Ayetteki anlam sırt dönmektir: {ar:ولى الرجل أي أدبر, tr:vellâ'r-raculu ey edbar, gloss:adam arkasını döndü, source:"و ل ي,B007"}. Yanında ise başa geçme anlamı duyulur. Peygamber'e verilmeyen göreve karşılık, yüz çeviren kendisi için yüz çevirmeyi üstlenmiştir. Yirmi dördüncü ayet cezayı Peygamber'e değil Allah'a verir: {ar:فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ, tr:fe-yuazzibuhullâhu'l-azâbe'l-ekber, gloss:Allah da onu en büyük azapla cezalandırır, source:88:24}. Allah'ın adı kulluk edilenin adıdır: {ar:فالإله الله تعالى لأنه معبود, tr:fe'l-ilâhu'llâhu teâlâ li-ennehû ma'bûd, gloss:ilah Allah'tır çünkü kulluk edilendir, source:"ء ل ه,B001"}. Son iki ayette konuşan "Biz" olur ve iş bölümü tamamlanır: {ar:إِنَّ إِلَيْنَآ إِيَابَهُمْ, tr:inne ileynâ iyâbehum, gloss:dönüşleri şüphesiz Bize'dir, source:88:25}; {ar:ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم, tr:summe inne aleynâ hısâbehum, gloss:sonra hesapları da şüphesiz Bize düşer, source:88:26}. Kur'an aynı bölüşümü tek bir cümlede söyler. Allah Peygamber'e, vaat edilenin bir kısmını ona göstersin ya da canını alsın, şunu der: {ar:فَإِنَّمَا عَلَيْكَ ٱلْبَلَٰغُ وَعَلَيْنَا ٱلْحِسَابُ, tr:fe-innemâ aleyke'l-belâğu ve aleyne'l-hısâb, gloss:sana düşen yalnızca duyurmaktır, hesap ise Bize düşer, source:13:40}. Önceki sure de aynı sırayı izler: önce {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-zekkir in nefeati'z-zikrâ, gloss:hatırlatma fayda verirse hatırlat, source:87:9}, sonra {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yezzekkeru men yahşâ, gloss:içi titreyen öğüt alacak, source:87:10}, sonra {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht ondan kaçınacak, source:87:11} ve en büyük ateş gelir. Başka yerlerde de şöyle denir: {ar:وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ, tr:ve zekkir fe-inne'z-zikrâ tenfeu'l-mu'minîn, gloss:hatırlat; hatırlatma inananlara fayda verir, source:51:55}; {ar:كَلَّآ إِنَّهَا تَذْكِرَةٌۭ, tr:kellâ innehâ tezkira, gloss:hayır; bu bir hatırlatmadır, source:80:11}; {ar:فَمَن شَآءَ ذَكَرَهُۥ, tr:fe-men şâe zekerah, gloss:dileyen onu anar, source:80:12}.

Kaynaklar: 88:21 فَذَكِّرْ ذ ك ر B009; 88:21 مُذَكِّرٌ ذ ك ر B003; 88:22 لَّسْتَ ل ي س B001; 88:22 بِمُصَيْطِرٍ س ط ر B001; 88:22 بِمُصَيْطِرٍ س ط ر B003; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:23 تَوَلَّىٰ و ل ي B003; 88:23 تَوَلَّىٰ و ل ي B007; 88:23 وَكَفَرَ ك ف ر B003; 88:24 ٱللَّهُ ء ل ه B001; 88:26 حِسَابَهُم ح س ب B001

## Gelmek, sırt dönmek, dönüp varmak

Sure bir gelişle açılır. Gelmek, kolayca varmaktır: {ar:الإتيان مجيء بسهولة, tr:el-ityânu mecîun bi-suhûle, gloss:ityân kolayca gelmektir, source:"ء ت ي,B001"}. Bu geliş iyiliği de kötülüğü de getirebilir: {ar:الإتيان يقال في الخير وفي الشر, tr:el-ityânu yukâlü fi'l-hayri ve fi'ş-şerr, gloss:ityân hem hayır hem şer için söylenir, source:"ء ت ي,B011"}. İlk ayette iki geliş vardır. Haber gelir, haberin anlattığı şey de bir gelip örtmedir. Örtme fiili gelmek fiiliyle açıklanır: {ar:غشيت موضع كذا أتيته, tr:ğaşîtü mevdia kezâ eteytüh, gloss:falan yere ğaşîtü yani oraya geldim, source:"غ ش و,B003"}; {ar:غشيه غشيانا أي جاءه, tr:ğaşiyehû ğaşeyânen ey câeh, gloss:ona ğaşiye yani ona geldi, source:"غ ش و,B003"}. Böylece ilk ayetteki iki kelime birbirini açıklar. Kur'an iki gelişi aynı ayette yan yana koyar: {ar:أَوْ تَأْتِيَهُمُ ٱلسَّاعَةُ بَغْتَةًۭ وَهُمْ لَا يَشْعُرُونَ, tr:ev te'tiyehumu's-sââtu bağteten ve hum lâ yeş'urûn, gloss:ya da o saat onlar farkında değilken ansızın gelir, source:12:107}.

İkinci ayetteki yüz yönelimdir: {ar:الوجهة كل موضع استقبلته, tr:el-vichetü küllü mevdıin istakbeltehû, gloss:vichet yöneldiğin her yerdir, source:"و ج ه,B002"}. Yirmi üçüncü ayette ise yüz çevrilir ve sırt gösterilir. Fiil "-den" ile kullanıldığında yakınlığı terk edip yüz çevirmeyi anlatır: {ar:إذا عدي بعن اقتضى معنى الإعراض وترك قربه, tr:izâ uddiye bi-an iktedâ ma'na'l-i'râdi ve terke kurbih, gloss:-den ile kullanılınca yüz çevirmeyi ve yakınlığını bırakmayı gerektirir, source:"و ل ي,B007"}. Aynı fiilin bir yüzü yönelmektir: {ar:التولية تكون إقبالا, tr:et-tevliyetü tekûnu ikbâlen, gloss:tevliye yönelmek de olur, source:"و ل ي,B006"}. Kur'an yüz çevirmeyi azaba bağlar. Musa ve Harun'a Firavun'a şunu söylemeleri emredilir: {ar:إِنَّا قَدْ أُوحِىَ إِلَيْنَآ أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ, tr:innâ kad ûhiye ileynâ enne'l-azâbe alâ men kezzebe ve tevellâ, gloss:yalanlayan ve yüz çeviren için azap olduğu bize vahyedildi, source:20:48}.

Yirmi beşinci ayet, sırt dönenin bile nereye vardığını söyler. Dönüş, insanın yerleştiği yere geri gelmesidir: {ar:آب الرجل يؤوب إيابا إذا رجع إلى مستقره والمآب المرجع, tr:âbe'r-raculu yeûbu iyâben izâ raca'a ilâ mustakarrih ve'l-meâbu'l-merci', gloss:adam yerleştiği yere döndüğünde âbe denir; meâb dönülen yerdir, source:"ء و ب,B001"}; {ar:آب الغائب يؤوب أوبا أي رجع والمآب المرجع, tr:âbe'l-ğâibu yeûbu evben ey raca' ve'l-meâbu'l-merci', gloss:gaip olan döndü; meâb dönülen yerdir, source:"ء و ب,B001"}. Yüz çeviren adım adım yine "Bize" yürür. Yüz çevirmek gidilen yeri değiştirmez. Kökün bir kolu aynı dönüşün gönüllü yapılabileceğini gösterir: {ar:الأواب كالتواب وهو الراجع إلى الله تعالى, tr:el-evvâbu ke't-tevvâbi ve huve'r-râciu ilallâhi teâlâ, gloss:evvâb tövbekâr gibidir; Allah'a dönendir, source:"ء و ب,B002"}. Kur'an'da "en büyük azap" sözünün geçtiği öteki ayet de dönüşe bakar: {ar:لَعَلَّهُمْ يَرْجِعُونَ, tr:leallehum yerciûn, gloss:belki dönerler, source:32:21}. Yakın azap, dönüşün henüz insanın elinde olduğu bir zamana denk gelir.

Kur'an dönüşü başka yerlerde de anar. İnsanın kendini yeterli görüp azgınlaştığı söylendikten {source:96:7} sonra şöyle denir: {ar:إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ, tr:inne ilâ rabbike'r-ruc'â, gloss:dönüş şüphesiz Rabbinedir, source:96:8}. Başka bir ayette de {ar:وَإِلَيْنَا ٱلْمَصِيرُ, tr:ve ileyne'l-masîr, gloss:varış Bizedir, source:50:43} denir. Allah, Peygamber'e inkârcılar için üzülmemesini söylerken surenin son ayetlerinin sırasını izler: {ar:وَمَن كَفَرَ فَلَا يَحْزُنكَ كُفْرُهُۥٓ ۚ إِلَيْنَا مَرْجِعُهُمْ فَنُنَبِّئُهُم بِمَا عَمِلُوٓا۟, tr:ve men kefera fe-lâ yahzunke küfruhû ileynâ merciuhum fe-nunebbiuhum bimâ amilû, gloss:kim inkâr ederse inkârı seni üzmesin; dönüşleri Bizedir, yaptıklarını onlara haber veririz, source:31:23}; {ar:نُمَتِّعُهُمْ قَلِيلًۭا ثُمَّ نَضْطَرُّهُمْ إِلَىٰ عَذَابٍ غَلِيظٍۢ, tr:numettiuhum kalîlen summe nadtarruhum ilâ azâbin ğalîz, gloss:onları biraz yararlandırırız, sonra ağır bir azaba sürükleriz, source:31:24}. Burada inkâr, Bize dönüş, yapılan işin haberi ve azap sırayla gelir. Dönülen yer iki türlüdür: {ar:لِّلطَّٰغِينَ مَـَٔابًۭا, tr:li't-tâğîne meâbâ, gloss:azgınlar için bir dönüş yeri, source:78:22} ve {ar:فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ مَـَٔابًا, tr:fe-men şâe'ttehaze ilâ rabbihî meâbâ, gloss:dileyen Rabbine bir dönüş yolu tutar, source:78:39}. Gönüllü dönüş, dokuzuncu ayetin hoşnutluğuyla yapılır: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:ırci'î ilâ rabbiki râdiyeten mardiyye, gloss:Rabbine hoşnut ve hoşnut edilmiş olarak dön, source:89:28}.

Kaynaklar: 88:1 أَتَىٰكَ ء ت ي B001; 88:1 أَتَىٰكَ ء ت ي B011; 88:1 ٱلْغَٰشِيَةِ غ ش و B003; 88:2 وُجُوهٌ و ج ه B002; 88:23 تَوَلَّىٰ و ل ي B006; 88:23 تَوَلَّىٰ و ل ي B007; 88:25 إِيَابَهُمْ ء و ب B001; 88:25 إِيَابَهُمْ ء و ب B002; 88:26 حِسَابَهُم ح س ب B001

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

