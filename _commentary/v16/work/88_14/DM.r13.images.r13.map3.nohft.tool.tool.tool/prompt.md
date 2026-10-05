Focus: 88:14. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_14/D.r13/context.md =====
# 88:14 — focus

وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ

Anchor translation (canonical reading, reference only):

Konulmuş kadehler de vardır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَأَكْوَابٌ | أَكْوَاب | ك و ب | CONJ;N |
| 2 | مَّوْضُوعَةٌ | مَّوْضُوعَة | و ض ع | ADJ |


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
- 88:14 ◀ focus وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ
- 88:15 وَنَمَارِقُ مَصْفُوفَةٌۭ
- 88:16 وَزَرَابِىُّ مَبْثُوثَةٌ
- 88:17 أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ
- 88:18 وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ
- 88:19 وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- 88:20 وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- 88:21 فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- 88:22 لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 88:23 إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- 88:24 فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_14/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ك و ب (root_001328) — identity root of وَأَكْوَابٌ (w1)

- **B001** kulpsuz içme kabı — kulpu ya da kulağı olmayan içme kabı · kulpu ya da kulağı olmayan içme kapları
  الكوب القدح لا عروة له (maqayis;mufradat)؛ الكوب كوز لا عروة له (ayn;sihah)؛ الكوب الإبريق بلا عروة (jamhara)؛ الكوب الكوز المستدير الرأس الذي لا أذن له (tahdhib)
- **B002** davul, uzun saplı telli çalgı veya deriye geçirilmiş üfleme borularından oluşan eğlence çalgısı — davul veya küçük, ortası dar davul · uzun saplı telli çalgı · deri parçasına birleştirilip üflenerek çalınan borular
  الكوبة الطبل للعب (maqayis)؛ الكوبة الطبل الذي يلعب به (mufradat)؛ الكوبة الطبل (jamhara)؛ الطبل والطنبور (jamhara)؛ الكوبة الطبل الصغير المخصر (sihah)؛ الكوبة قصبات تجمع في قطعة أديم ويزمر فيها (ayn)
- **B003** satranç — satranç
  الكوبة الشطرنجة (ayn)
- **B004** üst üste getirip yapıştırmak — parçalarını birbirinin üzerine getirip yapıştırmak
  بعضها كُوب على بعض أي ألزق (ayn)
- **B005** kulpsuz içme kabından içmek — kulpsuz içme kabından içmek
  كاب يكوب إذا شرب بالكوب (tahdhib)
- **B006** ince boyunluluk ve iri başlılık — boynun inceliği ve başın büyüklüğü
  الكَوَب دقة العنق وعظم الرأس (tahdhib)

## و ض ع (root_001657) — identity root of مَّوْضُوعَةٌ (w2)

- **B001** bir şeyi indirip yerine koyma; konduğu yer — bir şeyi yerine koymak veya elden bırakmak · yer, konum · yerine konmuş şey · ev yapmak veya kurmak · yazılı kayıtları ortaya çıkarmak
  أصل واحد يدل على الخفض للشيء وحطه (maqayis)؛ الوضع مصدر قولك وضع يضع (ayn)؛ الموضع المكان ومصدر وضعت الشيء من يدي (sihah)؛ وضعت الشيء أضعه وضعا وهو ضد رفعته (tahdhib)؛ الوضع أعم من الحط ومنه الموضع (mufradat)
- **B002** doğumla yükü bırakma ve özel gebe kalma zamanı — kadının çocuğunu doğurması · adet öncesi temizlik sonunda gebe kalma
  وضعت المرأة ولدها (maqayis)؛ وضعت المرأة وضعا بالفتح أي ولدت (sihah)؛ وضعت المرأة فهي تضع وضعا وتضعا فهي واضع (tahdhib)؛ وضعت المرأة الحمل وضعا (mufradat)؛ ما حملته أمه وضعا أي ما حملته على حيض (tahdhib)
- **B003** hayvanın hızlı ya da özel yürüyüşle ilerlemesi — bineğin hızlı gitmesi veya koşması · sürücünün bineği hızlandırması · bu yürüyüşü güzel olan
  الدابة تضع في سيرها وضعا وهو سير سهل يخالف المرفوع (maqayis)؛ الدابة تضع السير وضعا وهو سير دون (ayn)؛ وضع البعير وغيره أي أسرع في سيره (sihah)؛ وضع البعير إذا عدا وأوضعته أنا (tahdhib)؛ وضعت الدابة تضع في سيرها وضعا أسرعت (mufradat)
- **B004** ticarette zarar ve sermaye indirimi — ticarette zarar etmek · sermayeden düşülen indirim veya eksilti
  وضع في تجارته يوضع خسر (maqayis)؛ الوضيعة ما تضعه من رأس مالك (ayn)؛ وضع الرجل في تجارته خسر (sihah)؛ الوضيعة الحطيطة وقد استوضع (tahdhib)؛ الوضيعة الحطيطة من رأس المال (mufradat)
- **B005** düşük konum ve kendini alçaltma — düşük konumlu kişi · aşağı konum, düşüklük · kendini alçaltarak boyun eğme
  الوضيع الرجل الدني (maqayis)؛ الوضاعة الضعة (ayn)؛ الوضيع الدنئ من الناس وفي حسبه ضعة (sihah)؛ رجل وضيع ضد الشريف والتواضع التذلل (tahdhib)؛ رجل وضيع بين الضعة في مقابلة رفيع (mufradat)
- **B006** yerleştirilmiş topluluk, kayıtlı asker ya da yük — başka bir yere taşınıp yerleştirilen topluluklar · bölgeye kaydedilen askerler veya topluluğun yükleri
  الوضائع قوم ينقلون من أرض إلى أرض (maqayis)؛ الوضيعة نحو وضائع كسرى (ayn)؛ الوضيعة واحدة الوضائع وهي أثقال القوم (sihah)؛ الوضيعة قوم من الجند يجعل أسماؤهم في كورة (tahdhib)
- **B007** devenin tuzcul otu otlaması ve orada konaklaması — tuzcul otu otlayan veya yanında konaklayan dişi deve · tuzcul bitkiyi otlayan develer · tuzcul yemlik bitki veya develerin kaldığı otlak
  الواضعات الإبل تأكل الخلة (maqayis)؛ ناقة واضعة للتي ترعاها وأصحاب الوضيعة أصحاب حمض (sihah)؛ إبل واضعة أي مقيمة في الحمض (tahdhib)؛ الحمض يقال له الوضيعة والجمع وضائع (tahdhib)
- **B008** kumaşa pamuk serip dikme — kumaşa pamuk koyma veya sonra giysiyi dikme
  الخياط يوضع القطن على الثوب توضيعا (ayn)؛ التوضيع خياطة الجبة بعد وضع القطن (sihah)؛ الخياط يوضع القطن توضيعا على الثوب (tahdhib)
- **B009** baş örtüsünü çıkarıp baş örtüsüz kalma [kalıp] — baş örtüsünü çıkardığı için baş örtüsüz kadın
  وضعت المرأة خمارها وامرأة واضع أي لا خمار عليها (sihah)؛ امرأة واضع بغير هاء إذا وضعت خمارها (tahdhib)
- **B010** saklaması için birine bırakma [kalıp] — bir şeyi saklaması için birinin yanına bırakmak
  وضعت عند فلان وضيعا أي استودعته وديعة (sihah)؛ يقال للوديعة وضيع وقد وضعت عند فلان وضيعا إذا استودعته وديعة (tahdhib)
- **B011** karşılıklı anlaşma ve görüşme — bir işte karşılıklı anlaşmak ve onu görüşmek · karşılıklı para koymalı sözleşme veya satışı bırakma
  المواضعة أن تواضع أخاك أمرا فتناظره فيه (ayn)؛ المواضعة المراهنة والمواضعة متاركة البيع وواضعته في الأمر (sihah)؛ المواضعة أن تواضع صاحبك أمرا تناظره فيه (tahdhib)
- **B012** sağlamlık eksikliği ve kusurlu yumuşama — işi veya yapısı sağlam olmayan, kadınsı sayılan kişi · kadın konuşmasına benzetilen yumuşama · alt bacağını yayarak yürüyen kusurlu at
  الرجل الموضع الذي ليس بمستحكم الأمر (maqayis)؛ في كلامه توضيع إذا كان فيه تأنيث كلام النساء (ayn)؛ رجل موضع أي مطرح ليس بمستحكم الخلق (sihah)؛ يقال في فلان توضيع أي تخنيث وفلان موضع إذا كان مخنثا (tahdhib)؛ فرس موضع إذا كان يفترش وظيفه وهو عيب (tahdhib)
- **B013** binmek için devenin boynunu alçaltma — binmek için devenin boynunu veya başını alçaltması
  الاتضاع أن تخفض رأس البعير لتضع قدمك على عنقه فتركب (sihah)؛ اتضع فلان بعيره إذا كان قائما فطامن من عنقه ليركبه (tahdhib)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:14, and ## Buluşmalar) =====
## İki pınar ve kaplar

Surede iki pınar vardır ve ikisi de aynı adı taşır. Beşincisi {ar:مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:min aynin âniye, gloss:son noktasına varmış sıcak bir pınardan, source:88:5}, on ikincisi ise {ar:فِيهَا عَيْنٌۭ جَارِيَةٌۭ, tr:fîhâ aynun câriye, gloss:orada akan bir pınar vardır, source:88:12}. Ad aynıdır, değişen yalnızca sıfattır. Birinde su sıcaklığın sonuna varmıştır. Ötekinde hareket halindedir: {ar:جرى الماء يجري جرية وجريا وجريانا, tr:cera'l-mâu yecrî cireten ve ceryen ve cereyânâ, gloss:su aktı, source:"ج ر ي,B001"}. Kaynayan suyun durduğu bir yer vardır, ama akan su yenilenir. Kur'an bu iki pınarı aynı surede, birkaç ayet arayla yan yana koyar. Biri günahkârların dolaştığı {ar:حَمِيمٍ ءَانٍۢ, tr:hamîmin ân, gloss:son noktasına varmış kaynar su, source:55:44} ve diğeri Rabbinin makamından korkanların iki bahçesinde akan sudur: {ar:فِيهِمَا عَيْنَانِ تَجْرِيَانِ, tr:fîhimâ aynâni tecriyân, gloss:ikisinde de akan iki pınar vardır, source:55:50}.

Beşinci ayetteki sıfatın harfleri, Arapçada kap anlamına gelen kelimenin çoğuluyla da aynıdır: {ar:الإناء معروف وجمعه آنية والأواني, tr:el-inâu ma'rûfun ve cem'uhû âniyetun ve'l-evânî, gloss:kap bilinir; çoğulu âniye ve evânîdir, source:"ء ن ي,B004"}. Ayetteki anlam sıcaklıktır. Yanında ise kapların adı duyulur. On dördüncü ayet bu kapları bahçeye koyar: {ar:وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ, tr:ve ekvâbun mevdûa, gloss:konmuş kadehler, source:88:14}. Kevb kulpsuz bir kadehtir: {ar:الكوب القدح لا عروة له, tr:el-kûbü'l-kadahu lâ urvete leh, gloss:kevb kulpsuz kadehtir, source:"ك و ب,B001"}. Konmuş olmak, kaldırılmışın karşıtıdır: {ar:وضعت الشيء أضعه وضعا وهو ضد رفعته, tr:vada'tü'ş-şey'e edauhû vad'an ve huve zıddü rafa'tüh, gloss:bir şeyi koydum; kaldırdım'ın zıddı, source:"و ض ع,B001"}. Kadehler el altında hazır durur, istenmeden önce oradadır. Kur'an aynı iki kelimeyi, yani kapların adını ve kadehleri, sabredenlerin karşılığını anlatırken yan yana getirir: {ar:وَيُطَافُ عَلَيْهِم بِـَٔانِيَةٍۢ مِّن فِضَّةٍۢ وَأَكْوَابٍۢ كَانَتْ قَوَارِيرَا۠, tr:ve yutâfu aleyhim bi-âniyetin min fiddatin ve ekvâbin kânet kavârîrâ, gloss:çevrelerinde gümüş kaplar ve billur kadehler dolaştırılır, source:76:15}. Aynı ses bir yerde kaynayan pınarın sıfatıdır, başka bir yerde bahçenin gümüş kapları.

Bahçe halkı da içirilir. Fiil iki tarafta da aynıdır, değişen kaynaktır: {ar:وَيُسْقَوْنَ فِيهَا كَأْسًۭا كَانَ مِزَاجُهَا زَنجَبِيلًا, tr:ve yuskavne fîhâ ke'sen kâne mizâcuhâ zencebîlâ, gloss:orada zencefil katkılı bir kadehten içirilirler, source:76:17}; {ar:عَيْنًۭا فِيهَا تُسَمَّىٰ سَلْسَبِيلًۭا, tr:aynen fîhâ tusemmâ selsebîlâ, gloss:orada Selsebil denen bir pınardan, source:76:18}; {ar:يُسْقَوْنَ مِن رَّحِيقٍۢ مَّخْتُومٍ, tr:yuskavne min rahîkın mahtûm, gloss:mühürlü saf bir içkiden içirilirler, source:83:25}. Bahçenin pınarı insanın elinde akar: {ar:عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا, tr:aynen yeşrabu bihâ ibâdullâhi yufeccirûnehâ tefcîrâ, gloss:Allah'ın kullarının içtiği ve diledikleri yere fışkırttıkları bir pınar, source:76:6}. Kadehler de bu pınardan doldurulur: {ar:بِأَكْوَابٍۢ وَأَبَارِيقَ وَكَأْسٍۢ مِّن مَّعِينٍۢ, tr:bi-ekvâbin ve ebârîka ve ke'sin min maîn, gloss:kadehler ibrikler ve akan pınardan doldurulmuş kâse ile, source:56:18}. Buradaki "maîn" kelimesi gözle görünen akar suyu anlatır: {ar:ماء معين أي ظاهر للعيون, tr:mâun maînun ey zâhirun li'l-uyûn, gloss:gözlere açık akan su, source:"ع ي ن,B006"}. Allah, Peygamber'e bu suyun kimden geldiğini sormasını söyler: {ar:قُلْ أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًۭا فَمَن يَأْتِيكُم بِمَآءٍۢ مَّعِينٍۭ, tr:kul e-raeytum in asbaha mâukum ğavran fe-men ye'tîkum bi-mâin maîn, gloss:de ki suyunuz yere çekilse size akar suyu kim getirir, source:67:30}.

Arapçada içmek de beslenmenin bir parçası sayılır: {ar:أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء, tr:aslun fî tezevvuki'ş-şey'i ve't-taâmu huve'l-me'kûlu ve'l-it'âmu yekau hatta'l-mâ', gloss:tatma kökü; yemek yenendir; doyurmak suya bile uzanır, source:"ط ع م,B001"}. Böylece beşinci ve altıncı ayetler tek bir sofradır: içecek kaynar sudur, yemek de ضريع. Son ayetlerdeki azap kelimesinin kökü ise tatlı suyu da adlandırır: {ar:عذب الماء عذوبة فهو عذب طيب, tr:azube'l-mâu uzûbeten fe-huve azbun tayyib, gloss:su tatlılaştı; o tatlı ve hoş sudur, source:"ع ذ ب,B001"}. Bu anlam ayetteki cezanın yanında duyulur. Aynı harfler bir yerde tatlı su, başka bir yerde azaptır. Tatlı suyu bekleyen yüz, kaynar suyla karşılaşır.

Kaynaklar: 88:5 تُسْقَىٰ س ق ي B001; 88:5 ءَانِيَةٍ ء ن ي B003; 88:5 ءَانِيَةٍ ء ن ي B004; 88:6 طَعَامٌ ط ع م B001; 88:12 عَيْنٌ ع ي ن B006; 88:12 جَارِيَةٌ ج ر ي B001; 88:14 أَكْوَابٌ ك و ب B001; 88:14 مَّوْضُوعَةٌ و ض ع B001; 88:24 ٱلْعَذَابَ ع ذ ب B001

## Alçalan ve yükselen

İkinci ayetteki yüz başını eğmiştir: {ar:أصل واحد يدل على التطامن؛ تطامن وطأطا رأسه, tr:aslun vâhidun yedullü ale't-tatâmün; tetâmene ve ta'ta'e ra'sehû, gloss:alçalmayı gösteren kök; başını eğip indirdi, source:"خ ش ع,B001"}. Yemeğinin kökü de alçalmayı anlatır: {ar:ضرع الرجل ضراعة إذا ذل, tr:dara'a'r-raculu darâaten izâ zell, gloss:adam alçalınca dara'a denir, source:"ض ر ع,B002"}. Onuncu ayette ise bahçe yüksektedir: {ar:أصل واحد يدل على السمو والارتفاع, tr:aslun vâhidun yedullü ale's-sumuvvi ve'l-irtifâ', gloss:yükseliği ve yüksekte oluşu gösteren kök, source:"ع ل و,B001"}; {ar:العلاء فالرفعة, tr:el-alâu fe'r-rif'a, gloss:alâ yüksek mertebedir, source:"ع ل و,B002"}. On üçüncü ayette sedirler kaldırılmıştır. Kaldırılmak da aşağılanmanın karşıtıdır: {ar:الرفعة نقيض الذلة, tr:er-rif'atü nakîdu'z-zille, gloss:yükseklik aşağılanmanın zıddıdır, source:"ر ف ع,B002"}. On dördüncü ayetteki "konmuş" kelimesinin kökü insanın düşük konumunu da anlatır: {ar:رجل وضيع ضد الشريف والتواضع التذلل, tr:racülün vadîun zıddü'ş-şerîf ve't-tevâdu't-tezellül, gloss:vadî şerefli olanın zıddıdır; tevazu alçalmaktır, source:"و ض ع,B005"}. Bahçede alçak konulan şey insan değildir, hizmet eden kadehlerdir. İnsan yüksek sedirde oturur.

Aynı yükseklik ve alçaklık dünyada da göze gösterilir. Gök yüksekliktir: {ar:أصل يدل على العلو؛ سموت إذا علوت, tr:aslun yedullü ale'l-uluvv; semevtü izâ alevt, gloss:yükseliği gösteren kök; yükseldiğinde semevtü dersin, source:"س م و,B001"}. Yer ise aşağıda olandır: {ar:كل شيء يسفل ويقابل السماء, tr:küllü şey'in yesfülü ve yukâbilü's-semâ', gloss:aşağıda kalıp göğün karşısında duran her şey, source:"ء ر ض,B001"}. Yirmi dördüncü ayetteki azap "en büyük" olandır: {ar:أصل صحيح يدل على خلاف الصغر, tr:aslun sahîhun yedullü alâ hılâfi's-sığar, gloss:küçüklüğün karşıtını gösteren kök, source:"ك ب ر,B001"}. İki kökün öteki yüzü de duyulur. Yükseklik kökü kibirli büyüklenmeyi de anlatır: {ar:العلو فالعظمة والتجبر, tr:el-uluvvu fe'l-azametü ve't-tecebbür, gloss:ulüv büyüklenme ve zorbalıktır, source:"ع ل و,B003"}. "En büyük" kelimesinin kökü de kendini büyük görmeyi adlandırır: {ar:الكبر العظمة وكذلك الكبرياء, tr:el-kibru'l-azametü ve kezâlike'l-kibriyâ', gloss:kibir büyüklüktür; kibriya da öyledir, source:"ك ب ر,B006"}. Bu anlamlar ayetlerdeki anlamların yanında duyulur. Bahçedeki yükseklik verilmiş bir yüksekliktir. İnsanın kendi kendine verdiği yükseklik ise öteki yüzün yolunu açar ve onu "en büyük" azapla karşılaştırır.

Kur'an kıyameti bu iki hareketle adlandırır: {ar:إِذَا وَقَعَتِ ٱلْوَاقِعَةُ, tr:izâ vekaati'l-vâkıa, gloss:olacak olan olduğunda, source:56:1}; {ar:خَافِضَةٌۭ رَّافِعَةٌ, tr:hâfidatun râfia, gloss:alçaltan ve yükselten, source:56:3}. Dünyada da yükseltme Allah'ın işidir. Müminlere meclislerde yer açmaları ve kalkmaları söylendiğinde kalkmanın karşılığı şudur: {ar:يَرْفَعِ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ مِنكُمْ, tr:yerfaillâhullezîne âmenû minkum, gloss:Allah içinizden inananları yükseltir, source:58:11}. Ateşe sunulan zalimler ise {ar:خَٰشِعِينَ مِنَ ٱلذُّلِّ, tr:hâşiîne mine'z-zull, gloss:aşağılanmadan eğilmiş, source:42:45} diye anılır. O günün gözleri için de {ar:خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ, tr:hâşiaten ebsâruhum terhakuhum zille, gloss:gözleri eğik ve kendilerini aşağılanma bürümüş, source:70:44} denir. "En büyük azap" sözü Kur'an'da bir yerde daha geçer ve orada küçüğün karşısına konur: {ar:وَلَنُذِيقَنَّهُم مِّنَ ٱلْعَذَابِ ٱلْأَدْنَىٰ دُونَ ٱلْعَذَابِ ٱلْأَكْبَرِ لَعَلَّهُمْ يَرْجِعُونَ, tr:ve le-nuzîkannehum mine'l-azâbi'l-ednâ dûne'l-azâbi'l-ekberi leallehum yerciûn, gloss:belki dönerler diye onlara en büyük azaptan önce yakın azaptan tattıracağız, source:32:21}. Alt basamak bir uyarıdır, üst basamak sonun kendisidir. Önceki surede de ateş aynı ölçüyle anılır: {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâre'l-kübrâ, gloss:en büyük ateşe girecek olan, source:87:12}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:6 ضَرِيعٍ ض ر ع B002; 88:10 عَالِيَةٍ ع ل و B001; 88:10 عَالِيَةٍ ع ل و B002; 88:10 عَالِيَةٍ ع ل و B003; 88:13 مَّرْفُوعَةٌ ر ف ع B002; 88:14 مَّوْضُوعَةٌ و ض ع B005; 88:18 ٱلسَّمَآءِ س م و B001; 88:20 ٱلْأَرْضِ ء ر ض B001; 88:24 ٱلْأَكْبَرَ ك ب ر B001; 88:24 ٱلْأَكْبَرَ ك ب ر B006

## Döşenen oda, döşenen dünya

On üçüncü ayetten on altıncıya kadar bir oda döşenir. Dört eşya vardır ve her birine yapılmış bir işi gösteren bir sıfat verilir: {ar:فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ, tr:fîhâ sururun merfûa, gloss:orada kaldırılmış sedirler, source:88:13}; {ar:وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ, tr:ve ekvâbun mevdûa, gloss:konmuş kadehler, source:88:14}; {ar:وَنَمَارِقُ مَصْفُوفَةٌۭ, tr:ve nemâriku masfûfe, gloss:sıra sıra dizilmiş yastıklar, source:88:15}; {ar:وَزَرَابِىُّ مَبْثُوثَةٌ, tr:ve zerâbiyyu mebsûse, gloss:serilmiş halılar, source:88:16}. Bunlar kaldırmak, koymak, dizmek ve sermektir. On yedinci ayetten yirminciye kadar ise dünya döşenir: dört nesne ve edilgen dört fiil gelir. Deve yaratılmış, gök kaldırılmış, dağlar dikilmiş, yer düzlenmiştir. Aynı el hareketleri hem bir odayı hem bir dünyayı kurar.

Kaldırmak iki listede de geçer. Tanımı koymayı da içinde taşır: {ar:الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها, tr:er-ref'u yukâlü fi'l-ecsâmi'l-mevdûati izâ a'leytehâ an makarrihâ, gloss:konmuş cisimleri yerlerinden yukarı aldığında ref' denir, source:"ر ف ع,B001"}. Yapı için de kullanılır: {ar:في البناء إذا طولته, tr:fi'l-binâi izâ tavveltehû, gloss:binada yükselttiğinde, source:"ر ف ع,B001"}. Gök, bir evin tavanı gibi kaldırılmıştır: {ar:السماء سقف البيت وكل عال مطل سماء, tr:es-semâu sakfu'l-beyt ve küllü âlin mutıllin semâ', gloss:sema evin tavanıdır; yüksekten bakan her şey semadır, source:"س م و,B004"}. Dağların fiili olan dikmek, kadehlerin fiili olan koymak üzerinden tanımlanır: {ar:نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر, tr:nasbu'ş-şey'i vad'uhû vad'an nâti'en ke-nasbi'r-rumhi ve'l-binâi ve'l-hacer, gloss:bir şeyi dikmek onu çıkıntılı biçimde koymaktır; mızrak bina ve taş dikmek gibi, source:"ن ص ب,B001"}. Dikmenin aslında doğruluk vardır: {ar:أصل صحيح يدل على إقامة شيء وإهداف في استواء, tr:aslun sahîhun yedullü alâ ikâmeti şey'in ve ihdâfin fi'stivâ', gloss:bir şeyi dikip düzgünce yükseltmeyi gösteren kök, source:"ن ص ب,B001"}. Dağlar yerin kazıklarıdır: {ar:اسم لكل وتد من أوتاد الأرض إذا عظم وطال, tr:ismun li-külli vetedin min evtâdi'l-ardi izâ azume ve tâl, gloss:yerin kazıklarından büyüyüp uzayan her birinin adı, source:"ج ب ل,B001"}. Yer de düz bir dam gibi yayılmıştır: {ar:سطح الله الأرض سطحا بسطها, tr:satahallâhu'l-arda sathan besatahâ, gloss:Allah yeri düzledi yani yaydı, source:"س ط ح,B001"}; {ar:السطح ظهر البيت إذا كان مستويا, tr:es-sathu zahru'l-beyti izâ kâne müsteviyen, gloss:satıh evin düz olan damıdır, source:"س ط ح,B001"}; {ar:سطحت المكان جعلته في التسوية كسطح, tr:satahtü'l-mekâne cealtühû fi't-tesviyeti ke-sath, gloss:yeri bir dam gibi düz yaptım, source:"س ط ح,B001"}. Aynı kök çadır direğine de ad verir: {ar:المسطح عمود الخيمة الذي يجعل به لها سطحا, tr:el-mistahu amûdü'l-hayme'llezî yüc'alu bihî lehâ sathan, gloss:çadıra düz bir üst veren direk, source:"س ط ح,B003"}. Bu anlam ayetin yanında duyulduğunda dünya bir çadıra benzer: yükseltilmiş bir tavanı, kazıkları ve serilmiş bir zemini vardır.

İki listeyi birbirine bağlayan kelimeler de vardır. Yastıkların dizildiği sıra düz bir çizgidir: {ar:الصف أن تجعل الشيء على خط مستو, tr:es-saffu en tec'ale'ş-şey'e alâ hattın müstevin, gloss:saf bir şeyi düz bir çizgiye koymaktır, source:"ص ف ف,B001"}. Aynı kelime düz arazi için de kullanılır: {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsafu'l-müstevî mine'l-ardi keennehû alâ saffin vâhid, gloss:tek bir saf üstündeymiş gibi düz yer, source:"ص ف ف,B005"}. Halıların serilmesini anlatan fiil, canlıların yere yayılmasını da anlatır: {ar:بثت البسط, tr:bussetil-busut, gloss:halılar serildi, source:"ب ث ث,B001"}; {ar:خلق الخلق وبثهم في الأرض, tr:halaka'l-halka ve besse-hum fi'l-ard, gloss:yaratılmışları yarattı ve yeryüzüne yaydı, source:"ب ث ث,B001"}. Bu ikinci cümlede on yedinci ayetteki yaratma ile yirminci ayetteki yer bir aradadır. Yerin kökü kalın bir halıya da ad verir: {ar:الإراض بساط ضخم من وبر أو صوف, tr:el-irâdu bisâtun dahmun min veberin ev sûf, gloss:deve tüyünden ya da yünden kalın bir yaygı, source:"ء ر ض,B005"}. Bu, on altıncı ayetteki halıların hemen yanında duyulur.

Yaratmak da bir ustanın ilk hareketidir: ölçmek. {ar:خلقت الأديم للسقاء إذا قدرته, tr:halaktü'l-edîme li's-sikâi izâ kaddertüh, gloss:deriyi tulum yapmak için ölçtüm, source:"خ ل ق,B001"}; {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhû et-takdîru'l-müstakîm, gloss:yaratmanın aslı doğru ölçüdür, source:"خ ل ق,B001"}. Aynı kök düzleştirmeyi de anlatır: {ar:صخرة خلقاء ملساء, tr:sahratun halkâu melsâ', gloss:dümdüz ve kaygan kaya, source:"خ ل ق,B008"}. Böylece dört fiilin dördü de ölçüye ve düzlüğe dayanır: doğru ölçü, düzgünce dikmek, dam gibi düzlemek ve aynı ölçünün sırası. Kur'an da yaratmayı düzenlemeyle birlikte söyler. Önceki sure {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî halaka fe-sevvâ, gloss:yaratıp düzenleyen, source:87:2} der. İnsana da şöyle seslenilir: {ar:ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ, tr:ellezî halakake fe-sevvâke fe-adeleke, gloss:seni yaratıp düzenleyen ve dengeli kılan, source:82:7}.

Kur'an kaldırma ile koymayı yan yana koyar. Rahman nimetlerini sayarken şöyle der: {ar:وَٱلسَّمَآءَ رَفَعَهَا وَوَضَعَ ٱلْمِيزَانَ, tr:ve's-semâe rafeahâ ve vada'a'l-mîzân, gloss:göğü kaldırdı ve teraziyi koydu, source:55:7}; {ar:وَٱلْأَرْضَ وَضَعَهَا لِلْأَنَامِ, tr:ve'l-arda vada'ahâ li'l-enâm, gloss:yeri de yaratılmışlar için koydu, source:55:10}. Dirilişi inkâr edenlere sorulan soruda göğün yapısı şöyle anlatılır: {ar:رَفَعَ سَمْكَهَا فَسَوَّىٰهَا, tr:rafea semkehâ fe-sevvâhâ, gloss:tavanını yükseltip düzenledi, source:79:28}. Yerin döşenmesi de aynı resmi sürdürür: {ar:أَلَمْ نَجْعَلِ ٱلْأَرْضَ مِهَٰدًۭا, tr:e-lem nec'ali'l-arda mihâdâ, gloss:yeri bir döşek yapmadık mı, source:78:6}; {ar:وَٱلْجِبَالَ أَوْتَادًۭا, tr:ve'l-cibâle evtâdâ, gloss:dağları da kazıklar, source:78:7}; {ar:وَٱلْأَرْضَ فَرَشْنَٰهَا فَنِعْمَ ٱلْمَٰهِدُونَ, tr:ve'l-arda feraşnâhâ fe-ni'me'l-mâhidûn, gloss:yeri döşedik; ne güzel döşeyiciyiz, source:51:48}. Nuh da kavmine {ar:وَٱللَّهُ جَعَلَ لَكُمُ ٱلْأَرْضَ بِسَاطًۭا, tr:vallâhu ceale lekumu'l-arda bisâtâ, gloss:Allah yeri sizin için bir yaygı yaptı, source:71:19} der. Gök bir tavandır: {ar:وَجَعَلْنَا ٱلسَّمَآءَ سَقْفًۭا مَّحْفُوظًۭا ۖ وَهُمْ عَنْ ءَايَٰتِهَا مُعْرِضُونَ, tr:ve cealne's-semâe sakfen mahfûzan ve hum an âyâtihâ mu'ridûn, gloss:göğü korunmuş bir tavan yaptık; onlar ise onun işaretlerinden yüz çeviriyorlar, source:21:32}. Tur suresi de bir yemin olarak {ar:وَٱلسَّقْفِ ٱلْمَرْفُوعِ, tr:ve's-sakfi'l-merfû', gloss:yükseltilmiş tavana andolsun, source:52:5} der. Bu çadırın direği yoktur: {ar:ٱللَّهُ ٱلَّذِى رَفَعَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا, tr:Allâhullezî rafea's-semâvâti bi-ğayri amedin teravnehâ, gloss:gökleri görebileceğiniz direkler olmadan yükselten Allah, source:13:2}. Yayma fiili de iki yönde kullanılır: {ar:وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ, tr:ve besse fîhâ min külli dâbbe, gloss:orada her türlü canlıyı yaydı, source:31:10}. O gün ise yayılan insanlardır, halılar değil: {ar:يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ, tr:yevme yekûnu'n-nâsu ke'l-ferâşi'l-mebsûs, gloss:insanların saçılmış pervaneler gibi olacağı gün, source:101:4}. Bahçenin odası da başka yerlerde aynı kelimelerle döşenir: {ar:مُتَّكِـِٔينَ عَلَىٰ سُرُرٍۢ مَّصْفُوفَةٍۢ, tr:muttekiîne alâ sururin masfûfe, gloss:dizili sedirlere yaslanmış, source:52:20}; {ar:وَفُرُشٍۢ مَّرْفُوعَةٍ, tr:ve furuşin merfûa, gloss:yükseltilmiş döşekler, source:56:34}; {ar:إِخْوَٰنًا عَلَىٰ سُرُرٍۢ مُّتَقَٰبِلِينَ, tr:ihvânen alâ sururin mutekâbilîn, gloss:sedirler üstünde karşılıklı kardeşler olarak, source:15:47}.

Kaynaklar: 88:13 مَّرْفُوعَةٌ ر ف ع B001; 88:14 مَّوْضُوعَةٌ و ض ع B001; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:15 مَصْفُوفَةٌ ص ف ف B005; 88:16 مَبْثُوثَةٌ ب ث ث B001; 88:17 خُلِقَتْ خ ل ق B001; 88:17 خُلِقَتْ خ ل ق B008; 88:18 ٱلسَّمَآءِ س م و B004; 88:18 رُفِعَتْ ر ف ع B001; 88:19 نُصِبَتْ ن ص ب B001; 88:19 ٱلْجِبَالِ ج ب ل B001; 88:20 سُطِحَتْ س ط ح B001; 88:20 سُطِحَتْ س ط ح B003; 88:20 ٱلْأَرْضِ ء ر ض B005

## Deve: sürü, süt ve yolculuk

Bakılacak dört şeyin ilki devedir. Gök, dağlar ve yer uzaktadır. Deve ise insanın yanındadır, insan onun üstündedir. Arapçada deve bir servettir: {ar:الإبل معروفة ورجل آبل ومال مؤبل, tr:el-ibilu ma'rûfetun ve racülün âbilün ve mâlün muebbel, gloss:deve bilinir; develi adam ve deveden oluşan mal, source:"ء ب ل,B001"}. Kökün bir kolu devenin suya muhtaç kalmadan yaşı otla yetinmesini anlatır: {ar:أبلت الإبل والوحش اجتزأت بالرطب عن الماء, tr:ebeleti'l-ibilu ve'l-vahşu'ctezeet bi'r-ratbi ani'l-mâ', gloss:develer ve yaban hayvanları sudan vazgeçip yaş otla yetindi, source:"ء ب ل,B002"}. Altıncı ve yedinci ayetlerde hiçbir şeyin yetmediği insanlar vardır. On yedinci ayette ise azla yetinen bir hayvana bakılması istenir.

Surenin önceki kelimelerinde de devenin bedeni yan anlam olarak duyulur. Nâime'nin kökü sürüye ad verir: {ar:النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم, tr:en-neamu'l-ibilu limâ fîhi mine'l-hayri ve'n-ni'meti ve'l-en'âmu'l-behâim, gloss:neam devedir; içindeki hayır ve nimetten dolayı; en'âm hayvanlardır, source:"ن ع م,B005"}. Hâşia, yorgun düşmüş bir devenin hörgücünü anlatır: {ar:خشع سنام البعير إذا أنضي فذهب شحمه وتطأطأ شرفه, tr:haşaa senâmü'l-baîri izâ undiye fe-zehebe şahmuhû ve teta'tae şerefuh, gloss:yorulan devenin hörgücünün yağı gidip tepesi çöktü, source:"خ ش ع,B004"}. Âmile, çalışmaya yatkın soylu dişi deveye ad verir: {ar:اليعملة الناقة النجيبة المطبوعة على العمل, tr:el-ya'meletü'n-nâkatü'n-necîbetü'l-matbûatu ale'l-amel, gloss:çalışmaya yaratılışça yatkın soylu dişi deve, source:"ع م ل,B008"}. Ateşe girme fiilinin kökü bir bitkiye de ad verir: {ar:تسميها العرب خبزة الإبل, tr:tüsemmîhe'l-arabu hubzete'l-ibil, gloss:Araplar ona develerin ekmeği der, source:"ص ل ي,B010"}. Yemek, yağ ve deve tek bir cümlede birleşir: {ar:المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن, tr:el-mut'imu mine'l-ibili'llezî yûcedu fî muhhihî ta'mu'ş-şahm ve şâtun taûmun fîhâ ba'du's-simen, gloss:iliğinde yağ tadı bulunan deve; biraz semizliği olan koyun, source:"ط ع م,B007"}. Mevdûa'nın kökü tuzlu otlakta yayılan develeri anlatır: {ar:الواضعات الإبل تأكل الخلة, tr:el-vâdiâtü'l-ibilu te'kulu'l-hulle, gloss:vâdiât hulle otunu yiyen develerdir, source:"و ض ع,B007"}. Masfûfe ise kurban için sıraya dizilen develeri anlatır: {ar:البدن الصواف التي تصفف ثم تنحر, tr:el-budnü's-savâffu'lletî tusaffefu summe tunhar, gloss:sıraya dizilip sonra kesilen kurbanlık develer, source:"ص ف ف,B001"}. Kur'an aynı kelimeyi kurbanlık develer için kullanır: {ar:فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ, tr:fezkurusmallâhi aleyhâ savâff, gloss:sıraya dizilmişken üzerlerine Allah'ın adını anın, source:22:36}. O ayette sıra, anma ve doyurma bir aradadır. Ayet ardından {ar:وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ, tr:ve at'imu'l-kânia ve'l-mu'terr, gloss:yetineni ve isteyeni doyurun, source:22:36} der.

Süt de aynı kelimelerden geçer. Darî'in kökü memedir: {ar:الضرع لكل ذات خف أو ظلف, tr:ed-dar'u li-külli zâti huffin ev zılf, gloss:dar' tabanlı ve tırnaklı her hayvanın memesidir, source:"ض ر ع,B001"}. Merfûa'nın kökü sütünü memesinde tutan deveye ad verir: {ar:ناقة رافع إذا رفعت اللبأ في ضرعها, tr:nâkatun râfiun izâ rafeati'l-lebee fî dar'ihâ, gloss:ağız sütünü memesinde tutan dişi deveye râfi' denir, source:"ر ف ع,B007"}. Masfûfe'nin kökü tek sağımda kadehleri sıra sıra dolduran deveye ad verir: {ar:ناقة صفوف للتي تصف أقداحا من لبنها, tr:nâkatun safûfun li'lletî tesuffu akdâhan min lebenihâ, gloss:sütünden kadehleri sıra sıra dolduran dişi deve, source:"ص ف ف,B002"}. On dördüncü ayetteki kevb de böyle bir kadehtir. Besleme kelimesinin kökü sütten çıkan yağa ad verir: {ar:السمن سلاء اللبن, tr:es-semnu sulâü'l-leben, gloss:semn sütten eritilen yağdır, source:"س م ن,B002"}. Sulamanın kökü ise hem su hem süt taşıyan kırbayı anlatır: {ar:السقاء القربة للماء واللبن, tr:es-sikâü'l-kırbetü li'l-mâi ve'l-leben, gloss:su ve süt için kırba, source:"س ق ي,B004"}. Kur'an bu içirmeyi bir ibret olarak anlatır: {ar:نُّسْقِيكُم مِّمَّا فِى بُطُونِهِۦ مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:nuskîkum mimmâ fî butûnihî min beyni fersin ve demin lebenen hâlisan sâiğan li'ş-şâribîn, gloss:karınlarındakinden; fışkı ile kan arasından içenlerin boğazından kolayca geçen arı bir süt içiririz, source:16:66}. Buradaki fiil, beşinci ayetteki "içirilir" fiiliyle aynıdır. Kolay yutulan süt, cehennemdeki içeceğin tersidir: {ar:يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ, tr:yetecerrauhû ve lâ yekâdu yusîğuh, gloss:yudum yudum içer ama yutamaz, source:14:17}. "Kolayca geçen" ve "yutamaz" aynı köktendir.

Yolculuk da aynı kelimelerden duyulur. Surenin ilk fiili, yürüyen bir devenin ön ayaklarının salınımını anlatır: {ar:ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير, tr:mâ ahsene etve yedey hâzihi'n-nâka ey rac'a yedeyhâ fi's-seyr, gloss:bu devenin ön ayaklarını yürürken geri atışı ne güzel, source:"ء ت ي,B009"}. Son ayetten bir önceki ayetteki dönüş kelimesi de aynı salınımı ve gün boyu yürüyüşü anlatır: {ar:الأوب سرعة تقليب اليدين والرجلين في السير والتأويب أن تسير النهار أجمع وتنزل الليل, tr:el-evbü sur'atü taklîbi'l-yedeyni ve'r-ricleyni fi's-seyr ve't-te'vîbü en tesîra'n-nehâra ecmea ve tenzile'l-leyl, gloss:yürüyüşte el ve ayakları çabuk oynatmak; bütün gün yürüyüp gece konmak, source:"ء و ب,B003"}; {ar:كل راجع مع الليل فهو آئب, tr:küllü râciin mea'l-leyli fe-huve âib, gloss:gece olunca dönen herkes âibdir, source:"ء و ب,B006"}. Aradaki kelimeler de yürüyüşün türlerini adlandırır: {ar:نصب القوم ساروا يومهم وهو سير لين, tr:nasaba'l-kavmu sârû yevmehum ve huve seyrun leyyin, gloss:topluluk bütün gün yumuşak bir yürüyüşle yürüdü, source:"ن ص ب,B010"}; {ar:السعي عدو ليس بشديد, tr:es-sa'yu adven leyse bi-şedîd, gloss:sa'y şiddetli olmayan koşudur, source:"س ع ي,B001"}; {ar:مرفوع الناقة في سيرها خلاف الموضوع, tr:merfûu'n-nâkati fî seyrihâ hılâfu'l-mevdû', gloss:devenin yürüyüşünde merfû mevdûun zıddıdır, source:"ر ف ع,B003"}; {ar:وضع البعير وغيره أي أسرع في سيره, tr:vadaa'l-baîru ve ğayruhû ey esraa fî seyrih, gloss:deve hızlandı, source:"و ض ع,B003"}. Bunlar yan anlamlardır ve ayetlerin anlamının yerine geçmez. Ama surenin "geldi mi" ile başlayıp "dönüşleri" ile biten yolu, deve sürücülerinin bir günlük yürüyüşü anlattığı kelimelerle kurulmuştur.

Kur'an deveyi yaratılmış ve insana boyun eğdirilmiş bir nimet olarak anlatır: {ar:وَٱلْأَنْعَٰمَ خَلَقَهَا ۗ لَكُمْ فِيهَا دِفْءٌۭ وَمَنَٰفِعُ وَمِنْهَا تَأْكُلُونَ, tr:ve'l-en'âme halakahâ lekum fîhâ dif'un ve menâfiu ve minhâ te'kulûn, gloss:hayvanları yarattı; onlarda sizin için ısınma ve faydalar vardır ve onlardan yersiniz, source:16:5}; {ar:وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ, tr:ve tahmilu eskâlekum ilâ beledin lem tekûnû bâliğîhi illâ bi-şıkkı'l-enfus, gloss:ancak canınızı tüketerek varabileceğiniz bir yere yüklerinizi taşırlar, source:16:7}. Başka bir ayette Allah'ın kendi işi anlatılır: {ar:أَوَلَمْ يَرَوْا۟ أَنَّا خَلَقْنَا لَهُم مِّمَّا عَمِلَتْ أَيْدِينَآ أَنْعَٰمًۭا, tr:e-ve-lem yerav ennâ halaknâ lehum mimmâ amilet eydînâ en'âmen, gloss:ellerimizin işinden onlar için hayvanlar yarattığımızı görmediler mi, source:36:71}; {ar:وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ وَمِنْهَا يَأْكُلُونَ, tr:ve zellelnâhâ lehum fe-minhâ rakûbuhum ve minhâ ye'kulûn, gloss:onları kendilerine boyun eğdirdik; bir kısmına biner bir kısmından yerler, source:36:72}. Bu ayetteki "iş" kelimesi, üçüncü ayetteki âmile ile aynı köktendir, ama burada iş Allah'ındır. Boyun eğdirme fiili de aşağılanma kelimesiyle aynı köktendir, ama burada bir lütuf olarak hayvana uygulanır. Deve, surenin döşediği odayı da döşer: {ar:وَجَعَلَ لَكُم مِّن جُلُودِ ٱلْأَنْعَٰمِ بُيُوتًۭا, tr:ve ceale lekum min cülûdi'l-en'âmi buyûten, gloss:hayvanların derilerinden size evler yaptı, source:16:80}; {ar:وَمِنْ أَصْوَافِهَا وَأَوْبَارِهَا وَأَشْعَارِهَآ أَثَٰثًۭا وَمَتَٰعًا, tr:ve min asvâfihâ ve evbârihâ ve eş'ârihâ esâsen ve metâan, gloss:yünlerinden yapağılarından ve kıllarından ev eşyası ve kullanılacak şeyler, source:16:80}. Allah İbrahim'e insanları hacca çağırmasını söylerken develer de gelişin aracıdır: {ar:يَأْتُوكَ رِجَالًۭا وَعَلَىٰ كُلِّ ضَامِرٍۢ يَأْتِينَ مِن كُلِّ فَجٍّ عَمِيقٍۢ, tr:ye'tûke ricâlen ve alâ külli dâmirin ye'tîne min külli feccin amîk, gloss:yaya olarak ve her uzak yoldan gelen arık develer üstünde sana gelsinler, source:22:27}. Bakmanın yiyeceğe yöneltildiği yerde de hayvanlar anılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bu bakış {ar:مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ, tr:metâan lekum ve li-en'âmikum, gloss:size ve hayvanlarınıza bir yararlanma olarak, source:80:32} diye biter.

Kaynaklar: 88:1 أَتَىٰكَ ء ت ي B009; 88:2 خَٰشِعَةٌ خ ش ع B004; 88:3 عَامِلَةٌ ع م ل B008; 88:3 نَّاصِبَةٌ ن ص ب B010; 88:4 تَصْلَىٰ ص ل ي B010; 88:5 تُسْقَىٰ س ق ي B004; 88:6 ضَرِيعٍ ض ر ع B001; 88:6 طَعَامٌ ط ع م B007; 88:7 يُسْمِنُ س م ن B002; 88:8 نَّاعِمَةٌ ن ع م B005; 88:9 لِّسَعْيِهَا س ع ي B001; 88:13 مَّرْفُوعَةٌ ر ف ع B003; 88:13 مَّرْفُوعَةٌ ر ف ع B007; 88:14 مَّوْضُوعَةٌ و ض ع B003; 88:14 مَّوْضُوعَةٌ و ض ع B007; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:15 مَصْفُوفَةٌ ص ف ف B002; 88:17 ٱلْإِبِلِ ء ب ل B001; 88:17 ٱلْإِبِلِ ء ب ل B002; 88:25 إِيَابَهُمْ ء و ب B003; 88:25 إِيَابَهُمْ ء و ب B006

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

