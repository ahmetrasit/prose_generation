Focus: 87:12. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. No other command or tool is available.

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


===== _commentary/v16/work/87_12/D.r13/context.md =====
# 87:12 — focus

ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ

Anchor translation (canonical reading, reference only):

O, büyük ateşte yanacaktır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ٱلَّذِى | ٱلَّذِى |  | REL |
| 2 | يَصْلَى | يَصْلَى | ص ل ي | V |
| 3 | ٱلنَّارَ | نَار | ن و ر | DET;N |
| 4 | ٱلْكُبْرَىٰ | كُبْرَىٰ | ك ب ر | DET;ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 87 — full text (context; no pericope)

- 87:1 سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى
- 87:2 ٱلَّذِى خَلَقَ فَسَوَّىٰ
- 87:3 وَٱلَّذِى قَدَّرَ فَهَدَىٰ
- 87:4 وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ
- 87:5 فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ
- 87:6 سَنُقْرِئُكَ فَلَا تَنسَىٰٓ
- 87:7 إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ
- 87:8 وَنُيَسِّرُكَ لِلْيُسْرَىٰ
- 87:9 فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ
- 87:10 سَيَذَّكَّرُ مَن يَخْشَىٰ
- 87:11 وَيَتَجَنَّبُهَا ٱلْأَشْقَى
- 87:12 ◀ focus ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ
- 87:13 ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- 87:14 قَدْ أَفْلَحَ مَن تَزَكَّىٰ
- 87:15 وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ
- 87:16 بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- 87:17 وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- 87:18 إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ
- 87:19 صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ


===== _commentary/v16/work/87_12/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ص ل ي (root_000880) — identity root of يَصْلَى (w2)

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

## ن و ر (root_001564) — identity root of ٱلنَّارَ (w3)

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

## ك ب ر (root_001281) — identity root of ٱلْكُبْرَىٰ (w4)

- **B001** küçüğün karşıtı olan büyüklük — büyük · pek büyük · daha büyük veya en büyük
  أصل صحيح يدل على خلاف الصغر (maqayis)؛ كبر كل شيء عظمه (ayn)؛ الكبر ضد الصغر (jamhara)؛ كبر بالضم يكبر أي عظم فهو كبير وكبار (sihah)؛ الكبير والصغير من الأسماء المتضايفة (mufradat)
- **B002** bir işin ana payı ve başlıca yükü — işin büyük bölümü veya ağır yükü · onun işinin en önemli bölümü
  والكبر معظم الأمر (maqayis)؛ كبر كل شيء عظمه (ayn)؛ كبر الشيء معظمه (jamhara)؛ كبر الشيء أيضا معظمه (sihah)؛ كبر الشيء معظمه بالكسر (tahdhib)؛ والذي تولى كبره إشارة إلى من أوقع حديث الإفك (mufradat)
- **B003** gözünde büyütüp hayrete düşmek — onu gözünde büyüttü ve ona hayret etti · onu gözlerinde büyüttüler
  أكبرت الشيء استعظمته (maqayis)؛ أكبرت الشيء أكبره إكبارا إذا عظم في صدرك وعجبت منه (jamhara)؛ أكبرت الشيء استعظمته (sihah)؛ أكبرنه أعظمنه (tahdhib)؛ أكبرت الشيء رأيته كبيرا (mufradat)
- **B004** yaşlanma ve zamanla eskime — adam yaşlandı · yaşlılık veya eskilik hali
  ومن الباب الكبر وهو الهرم (maqayis)؛ الكبرة السن يقال علته كبرة (ayn)؛ بلغ فلان الكبر في السن (jamhara)؛ الكبر في السن وقد كبر الرجل أي أسن (sihah)؛ الكبر مصدر الكبير في السن من الناس والدواب (tahdhib)؛ يقال فلان كبير أي مسن (mufradat)؛ السهم والنصل العتيق الذي أفسده الوسخ قد علته كبرة (ayn)؛ للسيف والنصل العتيق الذي قدم علته كبرة (tahdhib)
- **B005** saygınlık ve önderlikte yüksek konum — kuşaktan kuşağa soylu ve saygın biçimde · onların başı veya en bilgilisi · sizin öğreticiniz veya başınız · önder veya en büyük ata
  الرفعة في الشرف (ayn)؛ ورثوا المجد كابرا عن كابر (maqayis;jamhara;sihah;tahdhib;mufradat)؛ كبيرهم أعلمهم كأنه كان رئيسهم (tahdhib)؛ إنه لكبيركم أي رئيسكم (mufradat)؛ الكابر السيد والكابر الجد الأكبر (tahdhib)
- **B006** ululuk ve kendini üstün görme — büyüklük taslama ve kendini üstün görme · ululuk ve boyun eğmeme; Tanrı'ya özgü yücelik · büyüklendi ve kendini üstün gösterdi · gerçeği inatla reddedip büyüklük tasladı
  الكبر العظمة وكذلك الكبرياء (maqayis)؛ الكبرياء اسم للتكبر والعظمة (ayn)؛ تكبر إذا تعظم (jamhara)؛ الكبر بالكسر العظمة وكذلك الكبرياء (sihah)؛ يتكبرون أي يرون أنهم أفضل الخلق (tahdhib)؛ الكبر الحالة التي يتخصص بها الإنسان من إعجابه بنفسه (mufradat)
- **B007** ağır cezalık büyük günah — ağır cezalık büyük günah · ağır cezalık büyük günahlar
  الكبر الإثم الكبير من الكبيرة (ayn)؛ الكبيرة من الذنوب والجمع كبائر (jamhara)؛ كبيرة من الكبائر يعني الذنوب (ayn)؛ الكبيرة متعارفة في كل ذنب تعظم عقوبته (mufradat)؛ إثم كبير (mufradat)
- **B008** soy yakınlığı veya aile içi doğum sırası — soyda en yakın olan veya en büyük evlat · babasının son çocuğu; başka aktarımda en büyük çocuğu
  الولاء للكبر يراد به أقعد القوم في النسب (maqayis)؛ الكبر أكبر ولد الرجل (ayn)؛ فلان كبرة ولد أبويه إذا كان آخرهم (sihah)؛ كبرة ولد أبيه بمعنى عجزة أي آخرهم (tahdhib)؛ هو صغرة ولد أبيه وكبرتهم أي أكبرهم (tahdhib)
- **B009** Tanrı'yı en büyük diye yüceltme — Tanrı'yı en büyük diye yüceltme · Tanrı en büyüktür
  التكبير في الصلاة وغيرها تفعيل من قولهم الله أكبر (jamhara)؛ التكبير التعظيم (sihah)؛ قول المصلي الله أكبر وكذلك قول المؤذن (tahdhib)؛ التكبير يقال لتعظيم الله تعالى بقولهم الله أكبر (mufradat)
- **B010** bir işin birine ağır ve güç gelmesi [kalıp] — bize çok ağır ve güç geldi
  إذا أردت الأمر العظيم قلت كبر علينا كبارة (ayn)؛ فإذا أردت الأمر العظيم قلت كبر علينا كبارة (sihah)؛ كبر الأمر يكبر كبارة (tahdhib)؛ تستعمل الكبيرة فيما يشق ويصعب (mufradat)؛ كبر على المشركين ما تدعوهم إليه (mufradat)
- **B011** üstünlük yarışına girip yenmek [kalıp] — benimle üstünlük yarışına girdi, ben de onu yendim
  كابرني فكبرته أي غلبته (ayn)
- **B012** tek yüzlü davul — tek yüzlü davul
  الكبر طبل له وجه (ayn)؛ الكبر الطبل الذي له وجه واحد (tahdhib)؛ الكبر الطبل وجمعه كبار (tahdhib)
- **B013** günün yükseldiği vakit [kalıp] — günün yükseldiği vakit
  أكبر النهار وشباب النهار أي حين ارتفع النهار (tahdhib)

## ECHO ص ل و (root_000879) — for يَصْلَى (w2): withheld observed target; not identity

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 87:12, and ## Buluşmalar) =====
## Ölçüp biçmek: ok, tulum ve kura

İkinci ve üçüncü ayet dört fiili sıralar: {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:elleẕî halaka fe-sevvâ, gloss:yaratıp düzene koyan, source:87:2}, {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:velleẕî kaddera fe-hedâ, gloss:ölçüp yol gösteren, source:87:3}. Arapçada bu fiiller bir zanaatkârın işinin adımlarıdır. خلق, kökünde ölçüp biçmektir: {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhû et-takdîru'l-mustakîm, gloss:halkın aslı doğru ölçüdür, source:"خ ل ق,B001"}. Bu tanım ikinci ayetin fiilini üçüncü ayetin fiiline bağlar. Ölçülüp yontulmuş ok da bu köktendir: {ar:سهم مخلق أملس مستو, tr:sehmun muhallakun emlesu mustevin, gloss:yontulmuş düzgün ve doğru ok, source:"خ ل ق,B008"}. Bu tanımda ikinci ayetin öbür fiili olan سوّى'nin kökü de vardır. سوّى eğri olanı doğrultmaktır: {ar:استوى من اعوجاج, tr:istevâ min i'vicâc, gloss:eğrilikten doğruldu, source:"س و ي,B002"}. قدّر, bir şeyi nasıl düzleyip hazır edeceğini düşünmektir: {ar:التروية والتفكير في تسوية أمر وتهيئته, tr:et-terviyetu ve't-tefkîru fî tesviyeti emrin ve teh'iyetih, gloss:bir işi nasıl düzleyip hazırlayacağını uzun uzun düşünmek, source:"ق د ر,B005"}. Aynı kök bir şeyin vardığı ölçüyü de bildirir: {ar:مبلغ الشيء وكنهه ونهايته, tr:mebleğu'ş-şey'i ve kunhuhû ve nihâyetuh, gloss:bir şeyin vardığı yer ve özü ve sonu, source:"ق د ر,B001"}. Sonra هدى gelir. Bu kelime okun önde giden ucudur: {ar:هادي السهم نصله, tr:hâdi's-sehmi naslu, gloss:okun hâdîsi temrenidir, source:"ه د ي,B003"}. Değnek de taşıyanın önünden gittiği için bu adı alır: {ar:العصا هاديا لأنها تتقدمه, tr:el-asâ hâdiyen li-ennehâ tetekaddemuh, gloss:değnek önünden gittiği için hâdî adını alır, source:"ه د ي,B003"}. Rab ise bir şeyi düzeltip adım adım tamamlayandır: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye bir şeyi halden hale geçirerek tamamlanma sınırına kadar oluşturmaktır, source:"ر ب ب,B002"}.

Değneği doğrultmanın bir yolu da ateştir. Bu işin fiili, on ikinci ayetteki "ateşe girer" fiilinin kendisidir: {ar:صلى عصاه إذا أدارها على النار يثقفها, tr:salâ asâhu iẕâ edârahâ ale'n-nâri yuŝakkıfuhâ, gloss:değneğini ateşin üstünde çevirip doğrulttu, source:"ص ل ي,B004"}. Ölçmek, doğrultmak ve uç takmak, ikinci ve üçüncü ayetin düz anlamının yanında bir yapım sahnesi kurar. Yapılan şey yalnızca var edilmez, bir yöne de çevrilir. "Yol gösterdi" fiili okun ucunun bir hedefe dönmesi gibi duyulur.

Aynı ölçüp biçme bir deri üzerinde de yapılır. خلق'in ilk örneği, su tulumu için deriyi kesmeden önce ölçmektir: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme iẕâ kaddertuhû kable'l-kat', gloss:deriyi kesmeden önce ölçtüğümde halaktu derim, source:"خ ل ق,B001"}. İkinci ayetin fiili ile üçüncü ayetin fiili burada tek bir hareketin iki adı olur. Bitmiş kabın yapısını dokuzuncu ayetteki نفع kökü anlatır: {ar:النفع في المزادة في جانبيها يشق الأديم فيجعل في جانبيها في كل جانب نفعة, tr:en-nif'u fi'l-mezâdeti fî cânibeyhâ yuşakku'l-edîmu fe-yuc'alu fî cânibeyhâ fî kulli cânibin nif'a, gloss:su kırbasının iki yanına deri yarılıp her yana nif'a denen bir parça konur, source:"ن ف ع,B002"}. Bu yanlar on birinci ayetteki kelimenin köküyle anılır: {ar:الجنبتان ناحيتا كل شيء, tr:el-canbetân nâhiyetâ kulli şey', gloss:her şeyin iki yanı, source:"ج ن ب,B001"}. Deri yağla terbiye edilir. Bu da "Rab" kelimesinin ailesindendir: {ar:رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب, tr:rabebtu'l-edîme bi's-semni ve'd-devâe bi'l-asel ve sikâun merbûb, gloss:deriyi yağla ilacı balla terbiye ettim; terbiye edilmiş tulum, source:"ر ب ب,B006"}. Tulum çalkalanır: {ar:جهرت السقاء مخضته, tr:cehertu's-sikâe mehadtuhû, gloss:tulumu çalkaladım, source:"ج ه ر,B010"}. Kullanıldıkça da aşınıp düzleşir: {ar:أخلق الشيء وخلق إذا بلي؛ إذا أخلق املاس وذهب زئبره, tr:ahleka'ş-şey'u ve haleka iẕâ beliye iẕâ ahleka imlâsse ve ẕehebe zi'biruh, gloss:bir şey eskiyince ahleka denir; eskiyince düzleşir ve tüyü gider, source:"خ ل ق,B009"}. Beş kök tek bir nesnede, ölçülen, yanları eklenen, terbiye edilen ve eskiyen bir tulumda buluşur. Kur'an bu nesneyi bir sahnede kullanmaz. Ama aynı kelime ailesi yaratılışı bir zanaat olarak duyurur, ve bu zanaatta ölçü kesmeden önce gelir.

Üçüncü bir nesne, kura okudur. "Rab" kelimesinin ailesinde okların saklandığı torba vardır: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-ribâbe şebîhetun bi'l-kinâneti tucmeu fîhâ sihâmu'l-meysir, gloss:ribâbe meysir oklarının toplandığı sadağa benzer torbadır, source:"ر ب ب,B010"}. Bu tanım sekizinci ayetteki "kolaylaştırırız" fiilinin kökünü, meysiri, de içerir. Meysir bir oyundur ve adı paylaştırmadan gelir: {ar:يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها, tr:yasera'l-kavmu'l-cezûra ey ictezerûhâ ve'ktesemû a'dâehâ, gloss:topluluk deveyi kesip parçalarını paylaştı, source:"ي س ر,B007"}. Okların en büyük payı alanı birinci ayetteki "en yüce" kelimesinin kökündendir: {ar:المعلى السابع من القداح, tr:el-muallâ es-sâbiu mine'l-kıdâh, gloss:muallâ okların yedincisidir, source:"ع ل و,B009"}. Okun gövdesi yontulup yumuşatılır: {ar:المخلق القدح إذا لين, tr:el-muhallak el-kıdhu iẕâ luyyine, gloss:muhallak yumuşatılmış ok gövdesidir, source:"خ ل ق,B008"}. Pay da aynı köktendir: {ar:الخلاق النصيب لأنه قد قدر لكل أحد نصيبه, tr:el-halâk en-nasîb li-ennehû kad kuddira li-kulli ehadin nasîbuh, gloss:halâk paydır çünkü herkesin payı ölçülmüştür, source:"خ ل ق,B006"}. Her şeyin bir ölçüsü ve bir vadesi vardır: {ar:لكل شيء مقدار وأجل, tr:li-kulli şey'in mikdârun ve ecel, gloss:her şeyin bir miktarı ve süresi vardır, source:"ق د ر,B001"}. İkinci ve üçüncü ayetteki ölçüp biçme bu sahnede paylaştırmaya döner. On altıncı ve on yedinci ayetteki seçim de bir pay seçimidir.

Kur'an bu ölçmeyi yaratılışın kendisine uygular. Allah inkâr eden insan için {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe-kaddera, gloss:onu bir damladan yarattı ve ölçüsünü koydu, source:80:19} der, sonra {ar:ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ, tr:ŝumme's-sebîle yesserah, gloss:sonra yolu ona kolaylaştırdı, source:80:20} diye ekler. Bu iki ayet surenin ikinci, üçüncü ve sekizinci ayetlerinin fiillerini aynı sırayla verir. Başka bir yerde Allah {ar:وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا, tr:ve halaka kulle şey'in fe-kaddarahû takdîrâ, gloss:her şeyi yarattı ve ona tam ölçüsünü verdi, source:25:2} ve {ar:إِنَّا كُلَّ شَىْءٍ خَلَقْنَٰهُ بِقَدَرٍۢ, tr:innâ kulle şey'in halaknâhu bi-kader, gloss:biz her şeyi bir ölçüyle yarattık, source:54:49} der. Surenin son ayetinde adı geçen İbrahim, putları reddedip kavmine Âlemlerin Rabbini anlatırken bu ikiliyi kendi ağzından söyler: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:elleẕî halakanî fe-huve yehdîn, gloss:beni yaratan ve bana yol gösteren O'dur, source:26:78}. Pay kelimesi Kur'an'da tam bu surenin vardığı karşıtlıkla geçer. Hac ibadetleri anlatılırken yalnız bu dünyada verilmesini isteyen kişi için {ar:وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ, tr:ve mâ lehû fi'l-âhireti min halâk, gloss:onun ahirette hiçbir payı yoktur, source:2:200} denir. Önceki kavimler için {ar:فَٱسْتَمْتَعُوا۟ بِخَلَٰقِهِمْ, tr:fe'stemteû bi-halâkıhim, gloss:paylarından yararlandılar, source:9:69} denir, ayetin sonunda da yaptıkları dünyada ve ahirette boşa gider. Kura okları ve meysir müminlere yasaklanırken kullanılan kelimeler ise surenin iki kelimesini yan yana getirir: {ar:فَٱجْتَنِبُوهُ لَعَلَّكُمْ تُفْلِحُونَ, tr:fectenibûhu leallekum tuflihûn, gloss:ondan uzak durun ki kurtuluşa eresiniz, source:5:90}. On birinci ayetteki "uzak durmak" ve on dördüncü ayetteki "kurtuluşa ermek" burada aynı cümlededir. Başka bir yerde meysir için {ar:وَإِثْمُهُمَآ أَكْبَرُ مِن نَّفْعِهِمَا, tr:ve ismuhumâ ekberu min nef'ihimâ, gloss:günahları faydalarından büyüktür, source:2:219} denir. Oklarla kısmet aramak da sayılan yasaklar arasındadır: {ar:وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ, tr:ve en testaksimû bi'l-ezlâm, gloss:fal oklarıyla pay aramanız, source:5:3}. Kura okuyla alınan pay yasaklanır. Ölçüyü koyanın verdiği pay ise ahirette de geçerlidir.

Kaynaklar: 87:2 خَلَقَ خ ل ق B001; 87:2 خَلَقَ خ ل ق B008; 87:2 خَلَقَ خ ل ق B009; 87:2 خَلَقَ خ ل ق B006; 87:2 فَسَوَّىٰ س و ي B002; 87:3 قَدَّرَ ق د ر B005; 87:3 قَدَّرَ ق د ر B001; 87:3 فَهَدَىٰ ه د ي B003; 87:1 رَبِّ ر ب ب B002; 87:1 رَبِّ ر ب ب B006; 87:1 رَبِّ ر ب ب B010; 87:12 يَصْلَى ص ل ي B004; 87:9 نَّفَعَتِ ن ف ع B002; 87:11 يَتَجَنَّبُهَا ج ن ب B001; 87:7 ٱلْجَهْرَ ج ه ر B010; 87:1 ٱلْأَعْلَى ع ل و B009; 87:8 لِلْيُسْرَىٰ ي س ر B007

## Rahimde toplanan, düzene konan beden

İkinci ve üçüncü ayetteki fiillerin bedene ait anlamları da vardır. Altıncı ayetteki "okutacağız" fiilinin kökü, rahmin yavrunun üzerine kapanmasını anlatır. Bu anlam en açık haliyle olumsuz cümlelerde görülür: {ar:لم تضم رحمها على ولد, tr:lem tedumma rahimehâ alâ veled, gloss:rahmini bir yavrunun üzerine kapamadı, source:"ق ر ء,B004"}, {ar:ما قرأت الناقة سلى قط, tr:mâ karaeti'n-nâkatu selen katt, gloss:dişi deve hiç yavru zarı toplamadı, source:"ق ر ء,B004"}. خلق, biçimi ortaya çıkmış cenindir: {ar:مضغة مخلقة أي تامة الخلق, tr:mudğatun muhallakatun ey tâmmetu'l-halk, gloss:yaratılışı tamamlanmış et parçası, source:"خ ل ق,B003"}. Biçimi çıkmamış olan için {ar:غير مخلقة لم تصور, tr:ğayru muhallakatin lem tusavvar, gloss:biçimlenmemiş olan, source:"خ ل ق,B003"} denir. سوّى, kusursuz kılınmış bedendir: {ar:السوي الذي سوى الله خلقه لا دمامة فيه ولا داء, tr:es-seviyy elleẕî sevvallâhu halkahû lâ demâmete fîhi ve lâ dâ', gloss:seviyy Allah'ın yaratılışını düzgün kıldığı kişidir; onda ne çirkinlik ne hastalık vardır, source:"س و ي,B002"}. Aynı kök gençliğin doruğuna varmayı da anlatır: {ar:استوى الرجل إذا انتهى شبابه, tr:istevâ'r-raculu iẕe'ntehâ şebâbuh, gloss:adam gençliği tamamlanınca istevâ denir, source:"س و ي,B005"}. قدّر her şeyi kendi ölçüsüne koymaktır: {ar:يجعلها على مقدار مخصوص ووجه مخصوص حسبما اقتضت الحكمة, tr:yec'aluhâ alâ mikdârin mahsûsin ve vechin mahsûsin hasebe mekteḍati'l-hikme, gloss:onu hikmetin gerektirdiği özel bir miktara ve özel bir biçime koyar, source:"ق د ر,B002"}. Rab, çocuğu evre evre büyütendir: {ar:رببت الصبي أربه, tr:rabebtu's-sabiyye erubbuh, gloss:çocuğu büyüttüm, source:"ر ب ب,B002"}. On altıncı ayetteki الدنيا'nın kökü doğumun yaklaşmasını anlatır: {ar:أدنت الناقة إذا دنا نتاجها, tr:edneti'n-nâkatu iẕâ denâ nitâcuhâ, gloss:dişi devenin doğumu yaklaştı, source:"د ن و,B004"}. On ikinci ayetteki الكبرى'nın kökü de yaşlılığı verir: {ar:الكبر في السن وقد كبر الرجل أي أسن, tr:el-kiber fi's-sinn ve kad kebira'r-racul ey esenne, gloss:kiber yaştaki büyüklüktür; adam yaşlandı, source:"ك ب ر,B004"}. Bu kelimelerin hiçbiri ayetlerinde bedeni anlatmaz. Ama aileleri, surenin yaratma ve düzene koyma fiillerini bir insan ömrünün evreleri olarak da duyurur: rahimde toplanma, biçimlenme, düzgünleşme, olgunluk ve yaşlılık.

Kur'an ikinci ayetteki ikiliyi tam olarak cenin için kullanır. Allah insanın başıboş bırakılacağını sanmasını sorgulayan ayetlerde şöyle der: {ar:أَلَمْ يَكُ نُطْفَةًۭ مِّن مَّنِىٍّۢ يُمْنَىٰ, tr:e-lem yeku nutfeten min meniyyin yumnâ, gloss:o dökülen meniden bir damla değil miydi, source:75:37}, {ar:ثُمَّ كَانَ عَلَقَةًۭ فَخَلَقَ فَسَوَّىٰ, tr:ŝumme kâne alakaten fe-halaka fe-sevvâ, gloss:sonra bir alaka oldu; O da yarattı ve düzene koydu, source:75:38}. Bu kısa bölüm şu soruyla biter: {ar:أَلَيْسَ ذَٰلِكَ بِقَٰدِرٍ عَلَىٰٓ أَن يُحْۦِىَ ٱلْمَوْتَىٰ, tr:e-leyse ẕâlike bi-kâdirin alâ en yuhyiye'l-mevtâ, gloss:bunu yapan ölüleri diriltmeye kadir değil midir, source:75:40}. Üçüncü ayetteki "ölçmek" fiilinin kökü burada güç anlamıyla gelir, on üçüncü ayetteki "yaşamak" fiili de diriltme anlamıyla. Başka bir yerde insana {ar:ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ, tr:elleẕî halakake fe-sevvâke fe-adeleke, gloss:seni yaratan ve düzene koyup dengeleyen, source:82:7} denir. Yeniden dirilişten şüphe edenlere ise Allah şöyle seslenir: {ar:ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ, tr:ŝumme min mudğatin muhallakatin ve ğayri muhallaka, gloss:sonra biçimlenmiş ve biçimlenmemiş bir et parçasından, source:22:5}. Aynı ayet bazılarının ömrün en düşkün çağına geri itildiğini söyler ve sonra toprağa döner: {ar:فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:fe-iẕâ enzelnâ aleyhe'l-mâe'htezzet ve rabet, gloss:üzerine suyu indirdiğimizde titreşip kabarır, source:22:5}. Beden ile otlak tek bir ayette yan yana gelir. İnsanın yaratılışı başka bir yerde {ar:ثُمَّ سَوَّىٰهُ وَنَفَخَ فِيهِ مِن رُّوحِهِۦ, tr:ŝumme sevvâhu ve nefaha fîhi min rûhih, gloss:sonra onu düzene koydu ve ona kendi ruhundan üfledi, source:32:9} diye anlatılır. İki bahçe benzetmesinde, bahçesine güvenen adama arkadaşı şöyle der: {ar:أَكَفَرْتَ بِٱلَّذِى خَلَقَكَ مِن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ سَوَّىٰكَ رَجُلًۭا, tr:e-kefarte billeẕî halakake min turâbin ŝumme min nutfetin ŝumme sevvâke racülâ, gloss:seni topraktan sonra bir damladan yaratan sonra seni bir adam olarak düzene koyanı mı inkâr ettin, source:18:37}. Bu sözlerden birkaç ayet sonra o bahçe yıkılır, hemen ardından da dünya hayatının kuruyan ot benzetmesi gelir. Düzene konmuş beden ile kuruyan otlak Kur'an'da aynı uyarının iki yüzüdür.

Kaynaklar: 87:6 سَنُقْرِئُكَ ق ر ء B004; 87:2 خَلَقَ خ ل ق B003; 87:2 فَسَوَّىٰ س و ي B002; 87:2 فَسَوَّىٰ س و ي B005; 87:3 قَدَّرَ ق د ر B002; 87:1 رَبِّ ر ب ب B002; 87:16 ٱلدُّنْيَا د ن و B004; 87:12 ٱلْكُبْرَىٰ ك ب ر B004

## Damga: deriye basılan iz

Daha önce anılan ikinci türetme, birinci ayetteki "ad" kelimesini وسم köküne, yani damgaya bağlar. Bu kök kimliği tartışmalıdır, ama yolun sonundaki sahne açıktır: {ar:الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي, tr:el-vesmu eseru keyyin ve baîrun mevsûmun vusime bi-simetin yu'rafu bihâ min kat'ı uẕunin ev keyy, gloss:vesm dağlama izidir; damgalı deve kulak kesiği ya da dağlama gibi tanındığı bir işaretle işaretlenmiştir, source:"و س م,B001"}. Damgayı basan alet de bu köktendir: {ar:الميسم المكواة أو الشيء الذي يوسم به الدواب, tr:el-mîsem el-mikvâtu evi'ş-şey'u'lleẕî yûsemu bihi'd-devâbb, gloss:mîsem dağlama demiri ya da hayvanların işaretlendiği aletidir, source:"و س م,B001"}. "İz" diye çevrilen أثر, on altıncı ayetteki تُؤْثِرُونَ kelimesinin köküdür. Damganın sahibi rabdir: {ar:رب كل شئ: مالكه, tr:rabbu kulli şey'in mâlikuh, gloss:her şeyin rabbi sahibidir, source:"ر ب ب,B001"}. Ad, bu sahnede bir şeyin kime ait olduğunu gösteren ve onu ötekilerden ayıran işarettir. "Rabbinin adını tesbih et" emri, düz anlamının yanında, Rabbin işaretini her türlü kusurdan arınmış tutma emri olarak da duyulur.

Surenin başka kelimeleri aynı sahneye girer. On ikinci ayetteki "ateş" kelimesi damganın kendisi için de kullanılır: {ar:ما نار هذه الناقة أي ما سمتها؛ نجارها نارها, tr:mâ nâru hâẕihi'n-nâkati ey mâ simetuhâ nicâruhâ nâruhâ, gloss:bu devenin nârı nedir yani damgası nedir; soyu damgasından bellidir, source:"ن و ر,B002"}. Bu ifade ateş ile damganın kökünü tek cümlede birleştirir. On altıncı ayetteki kökün ailesinde devenin ayağına basılan iz de vardır: {ar:المئثرة حديدة يؤثر بها خف البعير ليعرف أثره في الأرض, tr:el-mi'ŝera hadîdetun yu'ŝeru bihâ huffu'l-baîri li-yu'rafe eseruhû fi'l-ard, gloss:mi'ŝera devenin tabanına iz basılan demirdir; böylece yerdeki izi tanınır, source:"ء ث ر,B008"}. İz, bir şeyden geriye kalandır: {ar:الأثر بقية ما يرى من كل شيء وما لا يرى بعد أن تبقى فيه علقة, tr:el-eser bakıyyetu mâ yurâ min kulli şey'in ve mâ lâ yurâ ba'de en tebkâ fîhi alaka, gloss:eser her şeyden görünen ya da görünmeyip bir ilişiği kalan artıktır, source:"ء ث ر,B003"}. Bu tanım on altıncı ayetin kökünü on yedinci ayetin köküne bağlar. Yedinci ayetteki "bilir" fiilinin kökü de ayırt edici işarettir: {ar:أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره, tr:aslun sahîhun vâhidun yedullu alâ eserin bi'ş-şey'i yetemeyyezu bihî an ğayrih, gloss:bir şeyi ötekilerden ayıran iz anlamında tek bir köktür, source:"ع ل م,B002"}. Damga yüzde de okunur: {ar:توسمت فيه الخير والشر أي رأيت فيه أثرا, tr:tevessemtu fîhi'l-hayra ve'ş-şerra ey raeytu fîhi eseren, gloss:onda iyiliği ya da kötülüğü sezdim yani onda bir iz gördüm, source:"و س م,B002"}. Bu ifade on yedinci ayetteki "hayırlı" kelimesinin kökünü de içerir.

Düz bir okuma, on altıncı ayetteki "tercih edersiniz" fiilini yalnızca bir eğilim olarak görür. Damga sahnesi, aynı kökün iz bırakmak ve izden tanınmak demek olduğunu duyurur. Tercih edilen şey kişide bir iz bırakır ve kişi o izden tanınır. Sure bu izi iki türlü gösterir: birinde Rabbin adı anılır, ötekinde ateş vardır.

Kur'an damgayı bir tehdit olarak kullanır. Allah Peygamber'e çok yemin eden, aşağılık, söz taşıyan kişiye uymamasını söyler. Bu kişi ayetler okunduğunda {ar:أَسَٰطِيرُ ٱلْأَوَّلِينَ, tr:esâtîru'l-evvelîn, gloss:öncekilerin masalları, source:68:15} der, ve hükmü şudur: {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:se-nesimuhû ale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. "Öncekiler" kelimesi surenin on sekizinci ayetindeki "ilk sayfalar"ın köküdür. İlk sayfaları masal sayan kişi damgalanır. Lut kavmini sabahleyin çığlık yakalayıp şehirlerinin altı üstüne getirildikten sonra şöyle denir: {ar:إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّلْمُتَوَسِّمِينَ, tr:inne fî ẕâlike le-âyâtin li'l-mutevessimîn, gloss:bunda işaretleri okuyanlar için ibretler vardır, source:15:75}. Yıkılmış bir yerden iz okumak, damganın öbür yüzüdür. Peygamber'in arkadaşları için de {ar:سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ, tr:sîmâhum fî vucûhihim min eseri's-sucûd, gloss:işaretleri yüzlerindedir; secdenin izinden, source:48:29} denir. Buradaki سيما başka bir köke yazılır, bu yüzden kök kimliği kurmaz. Ama yanındaki أثر, on altıncı ayetin köküdür, ve iz burada namazın bıraktığı izdir.

Kaynaklar: 87:1 ٱسْمَ و س م B001; 87:1 ٱسْمَ و س م B002; 87:12 ٱلنَّارَ ن و ر B002; 87:16 تُؤْثِرُونَ ء ث ر B008; 87:16 تُؤْثِرُونَ ء ث ر B003; 87:7 يَعْلَمُ ع ل م B002; 87:1 رَبِّ ر ب ب B001

## Uzaktan görülen ateş

On ikinci ayet bedbahtı {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:elleẕî yasle'n-nâra'l-kubrâ, gloss:o en büyük ateşe girecek olan, source:87:12} diye tanıtır. "Ateş" kelimesi ışıkla aynı köktendir: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûru ve'n-nâru summiyâ bi-ẕâlike min tarîkati'l-idâe, gloss:nur da nâr da aydınlatma yönünden bu adı almıştır, source:"ن و ر,B001"}. Arapça bir ateşe varmanın birkaç yolunu ayrı ayrı adlandırır. Uzakta görülen ateşe yönelinir: {ar:تنورت نارا قصدت إليها, tr:tenevvertu nâran kasadtu ileyhâ, gloss:bir ateşe yöneldim, source:"ن و ر,B003"}, {ar:تنورت النار من بعيد: تبصرتها, tr:tenevvertu'n-nâra min baîd tebassartuhâ, gloss:ateşi uzaktan seçtim, source:"ن و ر,B003"}. Ateş yol işareti olarak yakılır: {ar:كانوا ينورون في الجاهلية ليهتدى ويقتدى بها, tr:kânû yunevvirûne fi'l-câhiliyyeti li-yuhtedâ ve yuktedâ bihâ, gloss:cahiliyede yol bulunsun ve izlensin diye ateş yakarlardı, source:"ن و ر,B005"}. Bu ifade üçüncü ayetteki "yol gösterdi" fiilinin kökünü içerir. Yol işaretinin adı da {ar:المنار: علم الطريق, tr:el-menâr alemu't-tarîk, gloss:menâr yolun işaretidir, source:"ن و ر,B005"} diye verilir ve yedinci ayetteki "bilir" fiilinin köküne bağlanır. Ateşte ısınılır: {ar:الصلاء ما يصطلى به وما يذكى به النار ويوقد, tr:es-salâu mâ yustalâ bihî ve mâ yuẕkâ bihi'n-nâru ve yûkad, gloss:salâ ısınılan ve ateşin tutuşturulduğu şeydir, source:"ص ل ي,B004"}. Ya da kişi ateşe sokulur ve yakıcılığına katlanır: {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:saliye'l-kâfiru nâran fe-huve yaslâhâ ey kâsâ harrahâ ve şiddetehâ, gloss:kâfir ateşe girdi yani sıcaklığına ve şiddetine katlandı, source:"ص ل ي,B003"}. Et de ateşte kızartılır: {ar:صليت اللحم صليا شويته, tr:saleytu'l-lahme salyen şeveytuh, gloss:eti ateşte kızarttım, source:"ص ل ي,B004"}. الكبرى ise {ar:كبر كل شيء عظمه, tr:kibru kulli şey'in izamuh, gloss:her şeyin kibri onun büyüklüğüdür, source:"ك ب ر,B001"}.

يصلى fiili ص ل ي kökündendir. On beşinci ayetteki فَصَلَّىٰ ise ص ل و kökündendir. Harfleri aynı kalıba oturur ama iki ayrı köktür, ve aralarındaki yakınlık bir yankıdır, kimlik değildir. Yine de sure bu yankıyı iki karşıt kişiye bölüştürür. Biri ateşe girer, öbürü Rabbinin adını anıp namaz kılar. Ateşe varmanın yolları arasındaki fark burada önem kazanır. Uzaktan görülüp yol bulmak için yönelinen ateş ile içine sokulup katlanılan ateş aynı nesnedir, ama ona giden kişinin işi farklıdır.

Kur'an bu farkı surenin son ayetinde anılan Musa'nın hikâyesinde sahneler. Musa bir ateş görür ve ailesine şöyle der: {ar:ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:imkuŝû innî ânestu nâran leallî âtîkum minhâ bi-kabesin ev ecidu ale'n-nâri hudâ, gloss:burada kalın; ben bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösteren bulurum, source:20:10}. Başka bir anlatımda amacı ısınmaktır: {ar:لَّعَلَّكُمْ تَصْطَلُونَ, tr:leallekum tastalûn, gloss:belki ısınırsınız, source:27:7}. Bir başka anlatımda ateşi {ar:مِن جَانِبِ ٱلطُّورِ, tr:min cânibi't-tûr, gloss:Tur'un yanından, source:28:29} görür. Bu ifadede on birinci ayetteki kökün "yan" anlamı geçer. Ateşe vardığında kendisine seslenilir: {ar:أَنۢ بُورِكَ مَن فِى ٱلنَّارِ وَمَنْ حَوْلَهَا وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:en bûrike men fi'n-nâri ve men havlehâ ve subhânallâhi rabbi'l-âlemîn, gloss:ateşin içindeki ve çevresindeki kutlu kılındı; Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu seslenişte birinci ayetteki tesbih ateşin başında söylenir. Hikâyenin bir başka anlatımında ses ona şöyle der: {ar:وَأَنَا ٱخْتَرْتُكَ فَٱسْتَمِعْ لِمَا يُوحَىٰٓ, tr:ve ene'htertuke fe'stemi' li-mâ yûhâ, gloss:seni ben seçtim; vahyolunanı dinle, source:20:13}, ve sonra {ar:فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:fa'budnî ve ekımi's-salâte li-ẕikrî, gloss:bana kulluk et ve beni anmak için namazı kıl, source:20:14}. Musa'nın ateşe yolculuğu namaz ve anma ile biter. Bu, surenin on beşinci ayetindeki kişinin yaptığı iştir. Kur'an insanların yaktığı küçük ateşi de anar: {ar:أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ, tr:e-fe-raeytumu'n-nâra'lletî tûrûn, gloss:yaktığınız ateşi gördünüz mü, source:56:71}. Hükmü de verir: {ar:نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ, tr:nahnu cealnâhâ teẕkiraten ve metâan li'l-mukvîn, gloss:onu bir hatırlatma ve çölde kalanlara bir geçimlik yaptık, source:56:73}. Küçük ateş bir öğüttür. Surenin dokuzuncu ayetindeki öğütten yüz çeviren ise on ikinci ayetteki büyük ateşe girer.

Ateşe sokulmanın işleyişini Kur'an kızartma diliyle anlatır: {ar:كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا, tr:kullemâ nadicet culûduhum beddelnâhum culûden ğayrahâ, gloss:derileri piştikçe onları başka derilerle değiştiririz, source:4:56}. Allah ayetlere sırt çeviren biri için {ar:سَأُصْلِيهِ سَقَرَ, tr:se-uslîhi sekar, gloss:onu Sekar'a sokacağım, source:74:26} der, ve o ateşin niteliği şudur: {ar:لَا تُبْقِى وَلَا تَذَرُ, tr:lâ tubkî ve lâ teẕer, gloss:ne bir şey bırakır ne de bir şeyi kendi haline koyar, source:74:28}. Bu ifadede on yedinci ayetteki "kalıcı" kelimesinin kökü olumsuz bir fiilde geçer. Sekar'dakilere oraya neden girdikleri sorulduğunda cevapları şudur: {ar:قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ, tr:kâlû lem neku mine'l-musallîn, gloss:namaz kılanlardan değildik dediler, source:74:43}. Bir başka surede ateş için surenin kendi kelimeleri kullanılır: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}, {ar:وَسَيُجَنَّبُهَا ٱلْأَتْقَى, tr:ve se-yucennebuhe'l-etkâ, gloss:en sakınan ondan uzak tutulacaktır, source:92:17}. Bu surede en bedbaht öğütten uzak durur. Orada ise en sakınan ateşten uzak tutulur. Aynı fiil yön değiştirir. Ateşin büyüklüğü başka yerlerde de anılır: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4}. Bir başka yerde öğütten yüz çeviren için {ar:فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ, tr:fe-yuazzibuhullâhu'l-azâbe'l-ekber, gloss:Allah onu en büyük azapla cezalandırır, source:88:24} denir. Musa'ya ateşin başında gösterilen ise başka bir büyüklüktür: {ar:لِنُرِيَكَ مِنْ ءَايَٰتِنَا ٱلْكُبْرَى, tr:li-nuriyeke min âyâtine'l-kubrâ, gloss:sana en büyük ayetlerimizden göstermek için, source:20:23}.

Kaynaklar: 87:12 ٱلنَّارَ ن و ر B001; 87:12 ٱلنَّارَ ن و ر B003; 87:12 ٱلنَّارَ ن و ر B005; 87:12 يَصْلَى ص ل ي B004; 87:12 يَصْلَى ص ل ي B003; 87:12 ٱلْكُبْرَىٰ ك ب ر B001; 87:3 فَهَدَىٰ ه د ي B001; 87:15 فَصَلَّىٰ ص ل و B003

## Yükseklik: yükselten ad ve alçak hayat

Sure yükseklikle açılır. "Ad" kelimesinin س م و kökündeki asıl anlamı yükselmektir: {ar:أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى, tr:aslu ismin sumuvvun ve huve mine'l-uluvvi li-ennehû tenvîhun ve delâletun ale'l-ma'nâ, gloss:ismin aslı sümüvdür ve yücelikten gelir; çünkü bir şeyi anıp yükseltir ve anlamı gösterir, source:"س م و,B005"}. {ar:الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى, tr:el-ismu mâ yu'rafu bihî ẕâtu'ş-şey'i ve asluhû sumuvvun bihî rufia ẕikru'l-musemmâ, gloss:isim bir şeyin kendisinin tanındığı şeydir; aslı sümüvdür; adlandırılanın anılışı onunla yükselir, source:"س م و,B005"}. Kök, ufukta beliren bir karaltıyı da anlatır: {ar:سما لي شخص ارتفع حتى استثبته, tr:semâ lî şahsun irtefea hattâ'steŝbettuh, gloss:bir karaltı yükseldi de onu iyice seçtim, source:"س م و,B002"}. Ufuktan ayrılan hilali de anlatır: {ar:سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا, tr:semâvetu'l-hilâli şahsuhû iẕe'rtefea ani'l-ufuki şey'en, gloss:hilalin semâvesi ufuktan biraz yükseldiğinde görünen biçimidir, source:"س م و,B002"}. "En yüce" kelimesinin kökü aynı yükseklikle tanımlanır: {ar:أصل واحد يدل على السمو والارتفاع, tr:aslun vâhidun yedullu ale's-sumuvvi ve'l-irtifâ, gloss:yücelik ve yükseklik bildiren tek köktür, source:"ع ل و,B001"}. "Gel" demek olan تعال de bu köktendir: {ar:تعال أصله أن يدعى الإنسان إلى مكان مرتفع, tr:teâle asluhû en yud'a'l-insânu ilâ mekânin murtefi', gloss:teâlin aslı insanın yüksek bir yere çağrılmasıdır, source:"ع ل و,B006"}. On beşinci ayetteki "anmak" fiilinin kökü de şerefi taşır: {ar:الذكر العلاء والشرف, tr:eẕ-ẕikru'l-alâu ve'ş-şeref, gloss:zikir yücelik ve şereftir, source:"ذ ك ر,B007"}. Birinci ayetin "ad", "en yüce" ve on beşinci ayetin "andı" kelimeleri böylece aynı yöne, yukarıya bakar.

Tesbih bu yükseltmenin içeriğini verir: {ar:التسبيح وهو تنزيه الله من كل سوء, tr:et-tesbîh ve huve tenzîhullâhi min kulli sû', gloss:tesbih Allah'ı her kötülükten uzak tutmaktır, source:"س ب ح,B002"}. Aynı kökte ihtişam da vardır: {ar:سبحات وجه ربنا يعني جلاله وعظمته ونوره, tr:subuhâtu vechi rabbinâ ya'nî celâlehû ve azametehû ve nûrah, gloss:Rabbimizin yüzünün subuhâtı celali azameti ve nurudur, source:"س ب ح,B003"}. Bu ifade on ikinci ayetteki "ateş"in kökü olan nur kelimesini içerir. On ikinci ayetteki الكبرى'nın kökü Allah'ı yüceltme sözünü verir: {ar:التكبير يقال لتعظيم الله تعالى بقولهم الله أكبر, tr:et-tekbîr yukâlu li-ta'zîmillâhi teâlâ bi-kavlihimullâhu ekber, gloss:tekbir Allah'ı "Allah en büyüktür" diyerek yüceltmektir, source:"ك ب ر,B009"}. Aynı kök sahiplenilen büyüklüğü de verir: {ar:الكبر العظمة وكذلك الكبرياء, tr:el-kibr el-azametu ve keẕâlike'l-kibriyâ, gloss:kibir büyüklüktür; kibriyâ da öyle, source:"ك ب ر,B006"}. Yüksekliğin kendisi de bozulabilir: {ar:علا ملك في الأرض أي طغى وتعظم, tr:alâ melikun fi'l-ardi ey tağâ ve teazzama, gloss:bir hükümdar yeryüzünde yükseldi yani azdı ve büyüklük tasladı, source:"ع ل و,B003"}. Öbür uçta on altıncı ayetin الدنيا'sı durur. Bu kelime alçak olan ve daha az değerli olandır: {ar:يعبر بالأدنى تارة عن الأصغر وتارة عن الأول وتارة عن الأقرب, tr:yuabbaru bi'l-ednâ târaten ani'l-asğari ve târaten ani'l-evveli ve târaten ani'l-akrab, gloss:ednâ bazen daha küçük olanı bazen ilk olanı bazen en yakın olanı anlatır, source:"د ن و,B002"}. {ar:الدني من الرجال الضعيف الدون, tr:ed-deniyyu mine'r-ricâl ed-daîfu'd-dûn, gloss:insanların denîsi zayıf ve aşağı olandır, source:"د ن و,B003"}.

Surenin iki ucunda bu iki kelime durur. Birinci ayet "en yüce" ile başlar, on altıncı ayet "en alçak" ya da "en yakın" olanla bir seçimi gösterir. Düz bir anlatımda bunlar yalnızca iki sıfattır. Kök aileleri ise onları bir eksenin iki ucu olarak duyurur. Adı anılan Rab yükseltilir. Tercih edilen hayat ise adı gereği alçak ve yakındır.

Kur'an bu ekseni bir sahnede kurar. Musa'nın hikâyesini anlatan bölümde Firavun halkını toplayıp şöyle seslenir: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe-kâle ene rabbukumu'l-a'lâ, gloss:ben sizin en yüce rabbinizim dedi, source:79:24}. Bu, birinci ayetin iki kelimesinin bir yaratık tarafından sahiplenilmesidir, ve "yeryüzünde yükselip azmak" anlamının kendisidir. Aynı surede birkaç ayet sonra hüküm verilir: {ar:فَأَمَّا مَن طَغَىٰ, tr:fe-emmâ men tağâ, gloss:azana gelince, source:79:37}, {ar:وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:ve âŝera'l-hayâte'd-dunyâ, gloss:ve dünya hayatını tercih edene, source:79:38}. Yüksekliği sahiplenen ile yakın hayatı tercih eden aynı kişidir. Musa sihirbazlarla karşılaştığında içinde bir korku duyar ve Allah ona şöyle der: {ar:قُلْنَا لَا تَخَفْ إِنَّكَ أَنتَ ٱلْأَعْلَىٰ, tr:kulnâ lâ tehaf inneke ente'l-a'lâ, gloss:korkma; üstün olan sensin dedik, source:20:68}. Aynı sahnede iman eden sihirbazlar kendilerine {ar:فَأُو۟لَٰٓئِكَ لَهُمُ ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:fe-ulâike lehumu'd-derecâtu'l-ulâ, gloss:işte onlar için en yüce dereceler vardır, source:20:75} denir. Gökler için de {ar:تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى, tr:tenzîlen mimmen halaka'l-arda ve's-semâvâti'l-ulâ, gloss:yeri ve yüce gökleri yaratandan indirilmiştir, source:20:4} denir. Vahyin getiricisi için {ar:ذُو مِرَّةٍۢ فَٱسْتَوَىٰ, tr:ẕû mirretin fe'stevâ, gloss:güç sahibidir; doğrulup durdu, source:53:6} ve {ar:وَهُوَ بِٱلْأُفُقِ ٱلْأَعْلَىٰ, tr:ve huve bi'l-ufuki'l-a'lâ, gloss:o en yüksek ufuktaydı, source:53:7} denir. Ufukta yükselen bir karaltı, kökün kendi sahnesidir. Malını verip arınan kişinin amacı da şöyle anlatılır: {ar:إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ, tr:ille'btiğâe vechi rabbihi'l-a'lâ, gloss:yalnızca en yüce Rabbinin rızasını istemek için, source:92:20}. Adın yükseltilmesi bir mekânda da anlatılır: {ar:فِى بُيُوتٍ أَذِنَ ٱللَّهُ أَن تُرْفَعَ وَيُذْكَرَ فِيهَا ٱسْمُهُۥ يُسَبِّحُ لَهُۥ فِيهَا, tr:fî buyûtin eẕinallâhu en turfea ve yuẕkera fîhe'smuhû yusebbihu lehû fîhâ, gloss:Allah'ın yükseltilmesine ve içlerinde adının anılmasına izin verdiği evlerde onu tesbih ederler, source:24:36}. Bu tek ayet surenin birinci ve on beşinci ayetlerini, yani yükseltmeyi, adı, anmayı ve tesbihi bir arada tutar. Peygamber'e de {ar:وَرَفَعْنَا لَكَ ذِكْرَكَ, tr:ve rafa'nâ leke ẕikrak, gloss:senin anılışını yükselttik, source:94:4} denir. Allah'ın kendisi için ise {ar:فَتَعَٰلَى ٱللَّهُ ٱلْمَلِكُ ٱلْحَقُّ, tr:fe-teâlallâhu'l-meliku'l-hakk, gloss:gerçek hükümdar olan Allah yücedir, source:20:114} denir. Birinci ayetteki emrin bir benzeri başka bir yerde de geçer: {ar:فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ, tr:fe-sebbih bi'smi rabbike'l-azîm, gloss:büyük Rabbinin adıyla tesbih et, source:56:74}. Bir başka emir de okumayı, adı, Rabbi ve yaratmayı birleştirir: {ar:ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ, tr:ikra' bi'smi rabbike'lleẕî halak, gloss:yaratan Rabbinin adıyla oku, source:96:1}. Bu emirde surenin birinci, ikinci ve altıncı ayetlerinin kelimeleri bir aradadır.

Kaynaklar: 87:1 ٱسْمَ س م و B005; 87:1 ٱسْمَ س م و B002; 87:1 ٱلْأَعْلَى ع ل و B001; 87:1 ٱلْأَعْلَى ع ل و B006; 87:1 ٱلْأَعْلَى ع ل و B003; 87:15 وَذَكَرَ ذ ك ر B007; 87:1 سَبِّحِ س ب ح B002; 87:1 سَبِّحِ س ب ح B003; 87:12 ٱلْكُبْرَىٰ ك ب ر B009; 87:12 ٱلْكُبْرَىٰ ك ب ر B006; 87:16 ٱلدُّنْيَا د ن و B002; 87:16 ٱلدُّنْيَا د ن و B003

## Buluşmalar

İmgelerin çoğu, surenin son ayetinde adı geçen Musa'nın hikâyesinde buluşur. Musa uzakta bir ateş görür ve {ar:أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ecidu ale'n-nâri hudâ, gloss:ateşin başında bir yol gösteren bulurum, source:20:10} umuduyla ona yönelir. Uzaktan görülen ateşin sahnesi ile yol sahnesi burada aynı cümlededir. Ateşin başında önce seçim gelir: {ar:وَأَنَا ٱخْتَرْتُكَ, tr:ve ene'htertuk, gloss:seni ben seçtim, source:20:13}. Sonra namaz ve anma gelir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14}. Sonra gizli olan gelir: {ar:أَكَادُ أُخْفِيهَا, tr:ekâdu uhfîhâ, gloss:onu neredeyse gizli tutuyorum, source:20:15}. Başka bir anlatımda ateşin başında tesbih söylenir: {ar:وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve subhânallâhi rabbi'l-âlemîn, gloss:Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu sahnede surenin on ikinci ve on beşinci ayetleri arasındaki karşıtlık bir kişinin yolculuğunda çözülür. Aynı ateşe yaklaşan biri onun içine sokulmaz. Ateş ona yol, seçilmişlik, namaz ve anma verir. Surede bu iki son iki ayrı kişiye düşer: on ikinci ayetteki kişi ateşe girer, on beşinci ayetteki kişi namaz kılar. Kelimelerin harf benzerliği bu ayrılığı kulakta da duyurur.

İkinci büyük buluşma selin sahnesidir. Gökten inen suyun vadilerde {ar:بِقَدَرِهَا, tr:bi-kaderihâ, gloss:kendi ölçülerince, source:13:17} akması, ölçüp biçme sahnesini çağırır. Selin taşıdığı köpük, otlağın vardığı döküntüdür. İnsanların {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâr, gloss:ateşte üzerine yaktıkları şeyden, source:13:17} çıkan köpük ise ateşin sahnesine girer. Faydalı olanın yerde kalması da öğüdün ve kalıcılığın sahnesidir. Kurumuş otun tencerenin köpüğüyle aynı adı taşıması, bu iki köpüğün Arapçada zaten tek bir kelimede birleştiğini gösterir. Bu ayet surenin beşinci ayetinden on yedinci ayetine uzanan çizgiyi tek bir manzaraya sığdırır. Bir yanda giden döküntü, öbür yanda kalan fayda vardır.

Üçüncü buluşma, Musa'nın karşısındaki sihirbazların sahnesidir. Sihirbazlar secdeye kapanır. Firavun kendi azabının daha çetin ve {ar:وَأَبْقَىٰ, tr:ve ebkâ, gloss:ve daha kalıcı, source:20:71} olduğunu söyler. Sihirbazlar da onu {ar:لَن نُّؤْثِرَكَ, tr:len nu'ŝirak, gloss:seni asla tercih etmeyiz, source:20:72} diye reddeder, yalnızca {ar:هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:hâẕihi'l-hayâte'd-dunyâ, gloss:bu dünya hayatı, source:20:72} üzerinde hüküm verebileceğini söyler ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Sonra suçlu için {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:20:74} der, iman edenler için {ar:ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:ed-derecâtu'l-ulâ, gloss:en yüce dereceler, source:20:75} der, ve hepsini {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76} sözüyle bağlar. Bu birkaç ayette seçim, kalıcı hayat, yükseklik ve yarılan tarlanın kelimeleri birlikte konuşur. Firavun'un "en yüce" iddiası da başka bir anlatımda bu sahneye eklenir. Surenin ikinci yarısı, on üçüncü ayetten on yedinci ayete kadar, neredeyse kelimesi kelimesine Musa'nın hikâyesindeki bir topluluğun ağzından gelmiştir. Son ayetin Musa'nın sayfalarını anması da bu yüzden önem taşır.

Dördüncü buluşma ot ile seçimdir. Dünya hayatının kuruyan ota benzetildiği ayetin hemen ardından kalıcı iyi işlerin daha hayırlı olduğu söylenir. Dünya hayatı başka bir yerde bir {ar:زَهْرَةَ, tr:zehrate, gloss:çiçek, source:20:131} olarak anılır, ve aynı ayet {ar:خَيْرٌۭ وَأَبْقَىٰ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:20:131} diye biter. Otlağın sahnesi seçimin sahnesine bu yolla girer. Beşinci ayetteki ot ile on altıncı ayetteki tercih edilen hayat aynı nesnedir. Kalıcı olan ise ayıklanıp seçilen şeydir. Tarlanın sahnesi bu iki uç arasında bir yol açar. Kalıcı iyilik anlamına gelen kurtuluş kelimesi on dördüncü ayette, toprağı yaran çiftçinin kelimesiyle söylenir. Yabani ot kendi haline kalınca kurur ve selle gider. İşlenen toprağın ürünü ise büyür, hakkı verilir ve geriye kalan bir pay bırakır. Biri dünya tarlası, öbürü ahiret tarlasıdır.

Beşinci buluşma, yaratma fiillerinde zanaat ile bedenin birleşmesidir. İkinci ayetteki ikili hem yontulmuş oku hem de ceninin biçimlenmesini anlatır. Rahimden başlayan ayetin toprağın yağmurla titreşmesiyle bitmesi, beden ile otlağı da birbirine bağlar. Aynı aile, üçüncü ayetteki ölçmeyi pay ölçmeye de taşır, ve on altıncı ayetteki tercih bir pay seçimine döner. Değneği ateşte doğrultmanın fiili on ikinci ayetin fiilidir. Bu fiil aynı ateşin düzelten bir işi ile içine düşenin katlandığı bir işi olduğunu duyurur. Bu son bağ dilin yankısıdır, ayetin sözü değildir.

Bu buluşmalar surenin hareketini taşır. Sure tesbih emriyle ve yükseklikle açılır. Ölçen, yontan ve yol gösteren Rabbin işiyle devam eder. Yağmurun çıkardığı ve selin götürdüğü ot ile sona gelen bir ömür gösterir. Sonra sözün toplanıp unutulmamasına, sunulan öğüde ve öğüt karşısında ikiye ayrılan insanlara geçer. Biri ateşe girer ve ne ölü ne diri kalır. Öbürü arınır, Rabbinin adını anar ve namaz kılar, yani surenin başındaki emri yerine getirir. Ardından seçim gelir: yakın olan öne konmuştur, ama arkadan gelen daha hayırlı ve daha kalıcıdır. Sure, bu sözün ilk sayfalarda, ateşin başında namaz ve anma emrini alan Musa'nın ve Rabbinden kendisini puttan uzak tutmasını isteyen İbrahim'in sayfalarında yazılı olduğunu söyleyerek kapanır.

