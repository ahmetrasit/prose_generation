Focus: 88:4. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_4/D.r13/context.md =====
# 88:4 — focus

تَصْلَىٰ نَارًا حَامِيَةًۭ

Anchor translation (canonical reading, reference only):

Kızgın bir ateşte yanar.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | تَصْلَىٰ | يَصْلَى | ص ل ي | V |
| 2 | نَارًا | نَار | ن و ر | N |
| 3 | حَامِيَةً | حَامِيَة | ح م ي | ADJ |


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
- 88:4 ◀ focus تَصْلَىٰ نَارًا حَامِيَةًۭ
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
- 88:23 إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- 88:24 فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_4/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ص ل ي (root_000880) — identity root of تَصْلَىٰ (w1)

- **B001** ayakta durma, eğilme ve yere kapanmalı yükümlü tapınma — ayakta durma, eğilme ve yere kapanma bölümleri olan yükümlü tapınma
  الصلاة التي جاء بها الشرع من الركوع والسجود (maqayis)؛ الصلاة واحدة الصلوات المفروضة (sihah)؛ الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib)؛ الصلاة التي هي العبادة المخصوصة (mufradat)
- **B002** iyilik dileme; özneye göre esirgeme, övme veya aklama — iyilik dileme; özneye göre esirgeme, övme veya bağışlanma isteme · onun için iyilik dilemek, onu esirgemek ya da aklamak · Tanrı'nın kullarını esirgemesi, övmesi veya aklaması · göksel görevlilerin iyilik ve bağışlanma dilemesi · ölen kişi için iyilik dileme
  الصلاة وهي الدعاء (maqayis)؛ صلوات الرسول للمسلمين دعاؤه لهم وذكرهم (ayn)؛ الصلاة من الله تعالى الرحمة (sihah)؛ الصلاة من الملائكة دعاء واستغفار ومن الله سبحانه رحمة (tahdhib)؛ الصلاة الدعاء والتبريك والتمجيد (mufradat)
- **B003** ateşin veya benzer bir sıkıntının şiddetine uğramak; birini ateşe sokmak [kalıp] — ateşe girip yakıcı sıcağını çekmek · onu ateşe sokmak · ateşin başında ısınmak · bir işin ağır sıkıntısını çekmek · birinin kötülüğüne uğramak · onun sertliğini ve gücünü göze alamamak
  أحدهما النار وما أشبهها من الحمى (maqayis)؛ صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها (ayn)؛ صلي الرجل نارا إذا أدخلته النار (sihah)؛ من يصلى في النار أي يلزم النار (tahdhib)؛ صلي بالنار وبكذا أي بلي بها واصطلى بها (mufradat)
- **B004** ateş yakıtı; ateşte pişirme veya ısıyla düzeltme — ateşi tutuşturan ve başında ısınılan yakıt · ateşte pişirilmiş yiyecek · odun ya da ateş · eti ateşte pişirmek · ateşte pişmiş · değneği ateş üstünde döndürerek yumuşatıp doğrultmak · ateşin üstüne kurulan ocak taşları
  الصلاء ما يصطلى به وما يذكى به النار ويوقد (maqayis)؛ صليت اللحم صليا شويته (ayn;sihah;tahdhib)؛ صلى عصاه إذا أدارها على النار يثقفها (ayn;tahdhib)؛ الصلاء يقال للوقود وللشواء (mufradat)
- **B005** av yakalamak için kurulan kapan — av veya zararlı canlılar için kurulan kapanlar · av yakalamak için kurulan kapan · birini yok oluşa düşürecek bir düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis)؛ المصلاة أن تنصب شركا ونحوه (ayn)؛ المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib)
- **B006** sırtın ortası ve kuyruk dibinin iki yanı — sırtın ortası veya kuyruk dibi ile kuyruk sokumunun iki yanı · kuyruk dibinin iki yanı · doğumda kuyruk dibi bölgesinin açılması · devenin yavrusunun kuyruk dibi bölgesine inmesi ve doğumun yaklaşması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn)؛ انفرج صلاها (ayn)؛ الصلوين مكتنفا الذنب (tahdhib)؛ أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها (tahdhib)
- **B007** yarışta önderin hemen ardındaki ikinci at — yarışta önderin hemen ardındaki ikinci at · atın önder atın hemen ardından gelmesi
  أتى الفرس على أثر الفرس السابق قيل قد صلى وجاء مصليا (ayn)؛ المصلى تالي السابق (sihah)؛ السابق الأول والمصلي الثاني (tahdhib)
- **B008** tapınma yeri, özellikle Yahudi tapınağı — Yahudi tapınakları veya genel olarak tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn)؛ الصلوات كنائس اليهود (tahdhib)؛ يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B009** üzerinde madde dövülen geniş taş — üzerinde koku maddesi veya başka maddeler dövülen geniş taş · üzerinde madde dövülen geniş taş
  الصلاية الفهر (sihah)؛ الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib)؛ الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B010** iri başaklı deve yemi bitkisi — iri başaklı, develere yem olan bitki · bu iri başaklı bitkinin yetiştiği yer
  الصليان نبت على فعلان ويقال فعليان له سنمة عظيمة (ayn)؛ الصليان نبت له سبطة عظيمة (tahdhib)؛ تسميها العرب خبزة الإبل (ayn;tahdhib)

## ن و ر (root_001564) — identity root of نَارًا (w2)

- **B001** ışık ve aydınlatma — ışık, aydınlık · ışık vermek, aydınlanmak veya aydınlatmak · aydınlatma; günün ağarması
  النور الضياء والفعل نار وأنار ونورا وإنارة واستنار أي أضاء (ayn)؛ النور: الضياء؛ أنار الشئ واستنار بمعنى أي أضاء؛ التنوير: الإنارة؛ التنوير: الإسفار (sihah)؛ أصل صحيح يدل على إضاءة واضطراب وقلة ثبات؛ النور والنار سميا بذلك من طريقة الإضاءة (maqayis)
- **B002** yanan ateş ve ateşle yapılan hayvan damgası — yanan ateş · ateşler · devenin ateşle yapılmış damgası · hayvanın soyu damgasından belli olur
  النار مؤنثة وهي من الواو؛ الجمع نور ونيران (sihah)؛ ما نار هذه الناقة أي ما سمتها؛ نجارها نارها؛ سماتها (sihah)؛ النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة (maqayis)
- **B003** ateşi uzaktan görüp ona yönelmek [kalıp] — ateşe doğru yönelmek · ateşi uzaktan görüp seçmek
  تنورت نارا قصدت إليها (ayn)؛ تنورت النار من بعيد: تبصرتها (sihah)؛ تنورت النار تبصرتها (maqayis)
- **B004** ağaç çiçeği ve çiçeklenme — ağaç çiçeği · ağaç çiçekleri; tek bir ağaç çiçeği · ağaç çiçek açtı · ağacın çiçek açması
  النور نور الشجر؛ تنوير الشجرة إزهارها؛ النوار نور الشجر (ayn)؛ تنوير الشجرة: إزهارها؛ نورت الشجرة وأنارت أي أخرجت نورها؛ النوار نور الشجر (sihah)؛ ومنه النور نور الشجر ونواره؛ أنارت الشجرة أخرجت النور (maqayis)
- **B005** yol gösteren belirgin işaret ve yüksek yapı — yol gösteren belirgin işaret · arazinin sınırları ve belirgin işaretleri · yol gösteren, üstünde ışık bulunan veya çağrı yapılan yüksek yapı
  المنارة مفعلة من الإنارة؛ كانوا ينورون في الجاهلية ليهتدى ويقتدى بها؛ المنارة الشمعة ذات السراج؛ المنارة ما يوضع عليه للمسرجة؛ المنارة للمؤذن (ayn)؛ المنار: علم الطريق؛ ضرب المنار على طريقه ليهتدى بها؛ المنارة التي يؤذن عليها؛ المنارة ما يوضع فوقها السراج (sihah)؛ المنارة مفعلة من الاستنارة؛ منار الأرض حدودها وأعلامها سميت لبيانها وظهورها (maqayis)
- **B006** ürkmek, kaçınmak ve uzaklaştırmak — kötülükten veya erkeklerden uzak duran iffetli kadın · ürkek ve insandan kaçan ceylanlar · kuşku verici durumdan uzak duran kadınlar · eşinden ürküp kaçınan kısrak veya inek · bir şeyden ürküp uzaklaşmak · birini söz veya davranışla ürkütüp uzaklaştırmak · ürkme, kaçınma ve uzaklaşma
  امرأة نوار وهي العفيفة النافرة عن الشر والقبيح؛ التي تكره الرجال؛ بقرة نوار تنفر من الفحل؛ نرت فلانا أي أنفرته (ayn)؛ النور أيضا: النفر من الظباء؛ نسوة نور أي نفر من الربية؛ الواحدة نوار وهي الفرور؛ فرس وديق نوار؛ نرت من الشئ؛ نرت غيري أي نفرته (sihah)؛ امرأة نوار أي عفيفة تنور أي تنفر من القبيح؛ نارت نفرت؛ نرت فلانا نفرته؛ النوار النفار (maqayis)
- **B007** topluluklar arası düşmanlık ve kin — topluluklar arasında çıkan düşmanlık ve kin
  النائرة الكائنة تقع بين القوم (ayn)؛ بينهم نائرة أي عداوة وشحناء (sihah)
- **B008** göz boyası ve dövme için kullanılan duman karası — göz boyası veya dövme için kullanılan fitil ya da yağ dumanı karası · deriyi veya diş etini iğneleyip üzerine duman karası ya da göz boyası serpmek
  النؤور دخان الفتيلة يتخذ كحلا أو وشما (ayn)؛ النوور: النيلج، وهو دخان الشحم يعالج به الوشم؛ وقد نور ذراعه إذا غرزها بإبرة ثم ذر عليها النوور (sihah)؛ مما شذ عن هذا الأصل النؤور دخان الفتيلة يتخذ كحلا ووشما؛ نورت اللثة غرزتها بإبرة ثم جعلت في الغرز الإثمد (maqayis)
- **B009** bedene sürülen özel karışım ve onu sürünme — bedene sürülen özel karışım · özel karışımı bedenine sürmek
  النورة يطلى بها (ayn)؛ تنور الرجل: تطلى بالنورة (sihah)
- **B010** bir işi karışık gösterip yanıltmak [kalıp] — bir işi birine karışık gösterip onu yanıltmak
  فلان ينور على فلان إذا شبه عليه أمرا؛ ليست الكلمة بعربية محضة؛ امرأة كانت تسمى نورة (ayn)
- **B011** açıkça seçilen veya belirgin biçimde çıkan şey — yolun belirgin oluğu · kumaşın belirgin işareti veya çizgisi · çift hayvanının boynundaki boyunduruk ve takımı · gücü başkasının iki katı olan adam
  النون والياء والراء كلمة تدل على وضوح شيء وبروزه؛ أخدود الطريق الواضح منه نير؛ نير الثوب علمه؛ النير الخشبة على عنق الفدان؛ ما ننكر أن يكون أصل هذا كله الواو فيرجع إلى ما ذكرناه في باب النور والنار (maqayis)

## ح م ي (root_000358) — identity root of حَامِيَةً (w3)

- **B001** ısınma ve ısıtma — ısındı, sıcaklığı arttı · demiri ateşte ısıttı · at koşudan ısınıp terledi · altın ve gümüşü ısıtma, bu işlemden iyi çıkma
  حمي الشيء يحمى حميا إذا سخن (ayn)؛ الحامية الحارة (ayn)؛ حمى النهار وحمي التنور أي اشتد حره (sihah)؛ أحميت الحديد في النار فهو محمى (sihah)؛ الحمي الحرارة المتولدة من الجواهر المحمية كالنار والشمس ومن القوة الحارة في البدن (mufradat)؛ حمي الفرس إذا عرق يحمى حميا وحمى الشد مثله (ayn;tahdhib)؛ هذا الذهب والفضة لحسن الحماء أي خرج من الحماء حسنا (ayn;tahdhib)
- **B002** koruma ve uzak tutma — onu korudu, yaklaşanı savdı · otlatmaya kapalı korunan yer · yeri korunan ve girilmez alan yaptı · hastaya zararlı yiyeceği yasakladı · hasta sakıncalı yiyeceklerden uzak durdu · insanlar ondan sakınıp uzak durdu · onu savundu ve korudu · yanındakileri ya da kendini koruyan kişi veya topluluk
  حميت القوم حماية وكل شيء دفعت عنه فقد حميته (ayn)؛ الحمى موضع فيه كلأ يحمى من الناس أن يرعى (ayn;tahdhib)؛ حميته حماية إذا دفعت عنه (sihah)؛ هذا شيء حمى أي محظور لا يقرب (sihah)؛ حميت المريض حمية منعته أكل ما يضره (ayn)؛ حاميت عنه محاماة وحماء (sihah)؛ تحاماه الناس أي توقوه واجتنبوه (sihah)؛ حمى أهله في القتال حماية (tahdhib)
- **B003** gücenme ve öfkelenme — onuruna yedirememe, gücenme ve öfke · ona öfkelendi · onurlu, aşağılanmayı kabul etmeyen
  حميت من هذا الشيء أحمى منه حمية أي أنفت أنفا وغضبا (ayn)؛ حميت عن كذا حمية ومحمية إذا أنفت منه وداخلك عار وأنفة (sihah)؛ حميت عليه غضبت (sihah)؛ حمى فلان أنفه يحميه حمية ومحمية (tahdhib)؛ عبر عن القوة الغضبية إذا ثارت وكثرت بالحمية (mufradat)
- **B004** kocanın yakınları — kocanın babası, erkek kardeşi ya da başka bir erkek yakını · kadının kocası tarafından gelen yakınları · kadının kayınvalidesi · kocanın erkek yakınıyla baş başa kalmak ölüm kadar tehlikelidir
  الحمو أبو الزوج وأخو الزوج وكل من ولي الزوج من ذي قرابته فهم أحماء المرأة وأم زوجها حماتها (ayn;tahdhib)؛ حماة المرأة أم زوجها (sihah;tahdhib)؛ كل شيء من قبل الزوج مثل الأب والأخ فهم الأحماء واحدهم حما (sihah)؛ الأحماء من قبل الزوج والأختان من قبل المرأة (tahdhib)؛ الحمو الموت (tahdhib)؛ أحماء المرأة كل من كان من قبل زوجها (mufradat)
- **B005** dokunulmaz sayılan damızlık erkek deve — binilmeyen, kırkılmayan ve otlaktan alıkonmayan damızlık erkek deve · damızlık geçmişi nedeniyle sırtı dokunulmaz sayılan erkek deve
  الحامي الفحل من الإبل الذي طال مكثه عندهم (sihah)؛ إذا لقح ولد ولده فقد حمى ظهره فلا يركب ولا يجز له وبر ولا يمنع من مرعى (sihah)؛ ولا حام قيل هو الفحل إذا ضرب عشرة أبطن كأن يقال حمى ظهره فلا يركب (mufradat)
- **B006** kara ve kötü kokulu balçık — kara ve kötü kokulu balçık · kara balçık, akarsu ya da kuyudan çıkarılan balçık · balçıklı pınar · kuyunun balçığını çıkardı
  الحمأ الطين الأسود المنتن (ayn)؛ يسمى الطين الذي نبث من النهر الحمأة (ayn)؛ عين حمئة أي ذات حمأة (ayn;mufradat)؛ الحمأة والحمأ طين أسود منتن (mufradat)؛ حمأت البئر أخرجت حمأتها وأحمأتها جعلت فيها حما (mufradat)
- **B007** sokucu hayvan zehrinin yakıcı etkisi — sokan ya da ısıran canlının zehri ve yakıcı etkisi · akrebin zehri ve verdiği zarar, iğnesi değil
  الحُمَة سم كل شيء يلدغ أو يلسع (ayn;tahdhib)؛ حمة العقرب سمها وضرها (sihah)؛ الحمة مخففة حرارة السم وليست كما تسمي العامة حمة العقرب إبرتها (jamhara)؛ هي فوعة السم أي حرارته وفورته (jamhara)؛ بسم العقرب الحمة والحمة (tahdhib)
- **B008** etkinin keskinliği ve şiddeti — içkinin ilk yükselişi, sıcaklığı ve içene yayılan etkisi · ağrının kabaran keskinliği · şeyin sertliği ve şiddeti
  الحميا بلوغ الخمر من شاربها (ayn)؛ حميا الكأس أول سورتها (sihah)؛ حموة الألم سورته (sihah)؛ حميا الكأس يعني سورتها (tahdhib)؛ الحميا دبيب الشراب (tahdhib)؛ حميا الشيء حدته وشدته (tahdhib)؛ حميا الكأس سورتها وحرارتها (mufradat)
- **B009** bacağın içindeki kabarık kas parçası — bacağın içindeki kabarık et ya da kas parçası · atın bacağının eninde bulunan iki et parçası
  الحمأة لحمة منتبرة في باطن الساق (ayn)؛ الحماة عضلة الساق (sihah)؛ في ساق الفرس حماتان وهما اللحمتان اللتان في عرض الساق (sihah)؛ الحماة لحمة منتبرة في باطن الساق (tahdhib)؛ الحماتان اللحمتان اللتان في عرض الساق (tahdhib)
- **B010** toynağın iki yan kenarı — toynağın ortadaki bölümünün sağ ve solundaki iki parça · toynağın sağ ve sol yan kenarları
  الحاميتان ما عن يمين السنبك وشماله (sihah;tahdhib)؛ الحوامي وهي حروفها من عن يمين وشمال (tahdhib)
- **B011** kuyu duvarını ören ağır taşlar — kuyu duvarını örmekte kullanılan taş · kuyu örgüsünü sağlamlaştıran büyük ve ağır kayalar
  الحامية الحجارة يطوى بها البئر (ayn;tahdhib)؛ الحوامي عظام الحجارة وثقالها (tahdhib)؛ الحوامي صخر عظام تجعل في مآخير الطي (tahdhib)؛ حجارة الركية كلها حوام (tahdhib)
- **B012** kararıp kara bir görünüm alma — karardı, kara bir görünüm aldı · üst üste yığılmış kara bulut
  احمومى الشيء فهو محموم واحمومى الليل والسحاب وذلك من السواد (ayn)؛ احمومى الشيء فهو محموم يوصف به الأسود من نحو الليل والسحاب (tahdhib)؛ المحمومي من السحاب الأسود المتراكم (tahdhib)

## ECHO ص ل و (root_000879) — for تَصْلَىٰ (w1): withheld observed target; not identity

- **B001** ateşin yakıcı sıcaklığına maruz kalma ve ateşle işleme — ateşe girip onun yakıcı sıcaklığını çekmek · ateşin yanında ısınmak · eti ateşte pişirmek · ateşte pişirilmiş · birini ateşe atıp yakmak · ateşi besleyen yakacak; ateşte pişirme · değneği ateşte yumuşatıp düzeltmek · bir işin güçlüğünü ve yorgunluğunu çekmek · onun sertliğine kimse yanaşamaz
  صليت العود بالنار (maqayis); اصطليت بالنار (maqayis;sihah); الصلا النار وصلى الكافر نارا (ayn); صليت اللحم شويته (ayn;sihah;tahdhib); الصلاء يقال للوقود وللشواء (mufradat); صلي بالأمر إذا قاسى حره وشدته (sihah;tahdhib)
- **B002** başkası için iyilik dileme; esirgeme, övme ve değer verme — başkası için iyilik ve esenlik dileme · biri için iyilik dilemek, onu övmek veya esirgenmesini istemek · Tanrı'nın esirgemesi, övmesi, bağışlaması ve değer vermesi · meleklerin bağışlanma ve iyilik dilemesi
  الصلاة وهي الدعاء (maqayis;sihah); صلوات الرسول للمسلمين دعاؤه لهم (ayn); الصلاة من الله تعالى الرحمة (maqayis;sihah;tahdhib); صلوات الله حسن ثنائه عليهم وقيل مغفرته لهم (ayn); صلاة الملائكة الاستغفار (ayn;tahdhib;mufradat); صلاة الله للمسلمين تزكيته إياهم (mufradat)
- **B003** ayakta durma, eğilme ve yere kapanma bölümleri olan kurallı tapınma — namaz · namazı bütün gerek ve koşullarını yerine getirerek kılmak
  الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة (maqayis); الصلاة واحدة الصلوات المفروضة (sihah); الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib); الصلاة التي هي العبادة المخصوصة أصلها الدعاء (mufradat); إقامة الصلاة (mufradat)
- **B004** yakalamak için kurulan tuzak — av için kurulan tuzak · avı veya başka hedefleri yakalayan tuzaklar · birini yıkıma düşürmek için gizlice düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis); المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد (ayn); المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib); صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة (tahdhib)
- **B005** sırtın ortası ve kuyruk kökünün iki yanı — sırtın orta bölümü veya kuyruk kökünün iki yanı · kuyruk kökünün iki yanı · doğum sırasında kuyruk kökü çevresinin açılması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn); كل أنثى إذا ولدت انفرج صلاها (ayn); الصلوين وهما مكتنفا الذنب من الناقة وغيرها (tahdhib); أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها وقرب نتاجها (tahdhib)
- **B006** yarışta birincinin hemen ardındaki ikinci — yarışta birincinin ardından gelen ikinci · yarışta liderin hemen ardından ikinci gelmek
  قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه (ayn); المصلى تالي السابق (sihah); السابق الأول والمصلي الثاني (tahdhib); يكون عند صلا الأول (tahdhib)
- **B007** tapınma yeri; kilise — Yahudilerin kiliseleri veya bir din topluluğunun tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn); الصلوات كنائس اليهود (tahdhib); قيل إنها مواضع صلوات الصابئين (tahdhib); يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B008** üzerinde dövme yapılan geniş taş — üzerinde malzeme dövülen geniş taş · dövme taşı
  الصلاية الفهر (sihah); الصلاءة بالهمز مثله (sihah); الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib); الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B009** iri başaklı, develerin otladığı bir bitki — iri başaklı, develerin otladığı bir bitki · bu bitkinin yetiştiği arazi
  الصليان نبت (ayn;tahdhib); له سنمة عظيمة كأنها رأس القصبة (ayn); له سبطة عظيمة كأنها رأس القصبة (tahdhib); تسميها العرب خبزة الإبل (ayn;tahdhib)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:4, and ## Buluşmalar) =====
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

## Eğilmek ve yanmak

İkinci, üçüncü ve dördüncü ayetlerin kelimeleri, ibadetin duruşlarını da adlandırır. Eğik yüzü anlatan kelime rükû edeni de anlatır: {ar:الخاشع المستكين والراكع, tr:el-hâşiu'l-müstekînu ve'r-râki', gloss:hâşi boyun eğen ve rükû edendir, source:"خ ش ع,B001"}; {ar:الخاشع الراكع, tr:el-hâşiu'r-râki', gloss:hâşi rükû edendir, source:"خ ش ع,B001"}. Nâsıba, ayakta durup yorulmaktır: {ar:النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي, tr:en-nasabu'l-anâ ve ma'nâhu enne'l-insâne lâ yezâlü muntasiben hattâ yu'yî, gloss:insanın tükenene dek ayakta durması, source:"ن ص ب,B004"}. Ateşe girme fiilinin kökü, rükû ve secdeden oluşan namazı da adlandırır: {ar:الصلاة التي جاء بها الشرع من الركوع والسجود, tr:es-salâtü'lletî câe bihe'ş-şer'u mine'r-rukûi ve's-sucûd, gloss:dinin getirdiği rükû ve secdeden oluşan namaz, source:"ص ل ي,B001"}. Ayette bu üç kelimenin anlamı eğiklik, yorgunluk ve ateştir. Yanlarında ise rükû, kıyam ve namaz duyulur. Sure bu yüzlerin kim olduğunu söylemez. Ama kelimeler, eğilmiş ve ayakta yorulmuş bir bedeni ateşe bağlar.

Kur'an bu kelimelerin her birini ibadet için de kullanır. Kurtuluşa erenleri anlatırken {ar:ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ, tr:ellezîne hum fî salâtihim hâşiûn, gloss:namazlarında huşu içinde olanlar, source:23:2} der. Allah Peygamber'e {ar:فَإِذَا فَرَغْتَ فَٱنصَبْ, tr:fe-izâ ferağte fensab, gloss:boşaldığında kalk ve yorul, source:94:7} der. Önceki surede aynı kök birkaç ayet arayla iki anlamda kullanılır: {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâre'l-kübrâ, gloss:en büyük ateşe girecek olan, source:87:12}; {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve zekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını anıp namaz kılan, source:87:15}. Biri ateşe girer, öteki namaz kılar. Namaz da orada anmayla birlikte gelir. Anmanın namaz anlamı da vardır: {ar:الذكر الصلاة والدعاء والثناء, tr:ez-zikru's-salâtü ve'd-duâu ve's-senâ', gloss:zikir namaz dua ve övgüdür, source:"ذ ك ر,B005"}. Ölüm anındaki inkârcı için de şöyle denir: {ar:فَلَا صَدَّقَ وَلَا صَلَّىٰ, tr:fe-lâ saddeka ve lâ sallâ, gloss:ne doğruladı ne namaz kıldı, source:75:31}; {ar:وَلَٰكِن كَذَّبَ وَتَوَلَّىٰ, tr:ve lâkin kezzebe ve tevellâ, gloss:ama yalanladı ve yüz çevirdi, source:75:32}. Namaz kılmamak ve yüz çevirmek burada bir arada, tıpkı yirmi üçüncü ayetteki yüz çevirme gibi.

Bu sahnelerin en keskini, o günün eğik bakışını dünyadaki secde çağrısına bağlar: {ar:خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ ۖ وَقَدْ كَانُوا۟ يُدْعَوْنَ إِلَى ٱلسُّجُودِ وَهُمْ سَٰلِمُونَ, tr:hâşiaten ebsâruhum terhakuhum zilletün ve kad kânû yud'avne ile's-sucûdi ve hum sâlimûn, gloss:gözleri eğik ve kendilerini aşağılanma bürümüş; oysa sağlıklıyken secdeye çağrılıyorlardı, source:68:43}. Dünyada istenen eğilme gönüllü olabilirdi. O gün ise zorla gelir. İkinci ayetteki kelime bu iki eğilmeyi birlikte duyurur.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:3 نَّاصِبَةٌ ن ص ب B004; 88:4 تَصْلَىٰ ص ل ي B001; 88:4 تَصْلَىٰ ص ل ي B003; 88:21 فَذَكِّرْ ذ ك ر B005

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

