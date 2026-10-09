Focus: 104:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/104_6/D.r13/context.md =====
# 104:6 — focus

نَارُ ٱللَّهِ ٱلْمُوقَدَةُ

Anchor translation (canonical reading, reference only):

Allah'ın tutuşturulmuş ateşidir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | نَارُ | نَار | ن و ر | N |
| 2 | ٱللَّهِ | ٱللَّه | ء ل ه | PN |
| 3 | ٱلْمُوقَدَةُ | مُوقَدَة | و ق د | DET;ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 104 — full text (context; no pericope)

- 104:1 وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ
- 104:2 ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ
- 104:3 يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ
- 104:4 كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ
- 104:5 وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ
- 104:6 ◀ focus نَارُ ٱللَّهِ ٱلْمُوقَدَةُ
- 104:7 ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ
- 104:8 إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ
- 104:9 فِى عَمَدٍۢ مُّمَدَّدَةٍۭ


===== _commentary/v16/work/104_6/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن و ر (root_001564) — identity root of نَارُ (w1)

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

## ء ل ه (root_000047) — identity root of ٱللَّهِ (w2)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ق د (root_001672) — identity root of ٱلْمُوقَدَةُ (w3)

- **B001** ateşin tutuşması, yakılması ve alevli görünümü — ateş tutuştu ve yandı · tutuştu, yanmaya başladı · alevlendi, harlayarak yandı · ateşi yaktı · ateşi yakmaya girişti veya yakılmasını istedi · yanma; ortaya çıkan alev · ateşin kendisi veya görünen alevi
  كلمة تدل على اشتعال نار (maqayis)؛ وقدت النار واتقدت وتوقدت وأوقدتها (maqayis)؛ وقدت النار وقودا ووقدا (ayn;sihah;mufradat)؛ أوقدتها واستوقدتها (sihah;mufradat)؛ الوقود بالضم الاتقاد (sihah)؛ الوقد نفس النار أو ما ترى من لهبها (maqayis;ayn)؛ الوقود لما حصل من اللهب (mufradat)
- **B002** yakacak odun ve ateşlik yakıt — yakacak odun; ateş için hazırlanmış yakıt
  الوقود الحطب (maqayis)؛ وقود النار أي حطبها (ayn)؛ الوقود بالفتح الحطب (sihah)؛ الوقود للحطب المجعول للوقود (mufradat)
- **B003** ateş yakılan yer — ateş yakılan yer, ocak · ateşin bulunduğu veya yakıldığı yer
  الموقد والمستوقد موضع النار (ayn)؛ الموضع موقد مثال مجلس (sihah)
- **B004** yazın en şiddetli sıcağı ve sıcak dönemi — şiddetli sıcak; on gün ya da yarım ay süren sıcak dönem · yazın en şiddetli sıcağı
  وقدة الصيف أشده حرا (maqayis;ayn;mufradat)؛ الوقدة أشد من الحر وهي عشرة أيام أو نصف شهر (sihah)
- **B005** ateş gibi hızla parlayıp şiddetlenme [kalıp] — çabuk kıvılcım çıkaran ateş çubuğu · etkinlikte canlı ve kararlı gönül · öfkeden parladı, öfkesi şiddetlendi · savaşı başlattı veya körükledi
  زند ميقاد سريع الوري وقلب وقاد سريع التوقد في النشاط والمضاء (ayn)؛ اتقد فلان غضبا (mufradat)؛ يستعار وقد واتقد للحرب كاستعارة النار والاشتعال (mufradat)
- **B006** ateş gibi ışıldamak [kalıp] — toynağın küçük parıltısı ışıldadı · mücevher ve altın ateş gibi ışıldadı
  وقد الحافر إذا تلألأ بصيصه وفي كل شيء (ayn)؛ يستعار ذلك للتلألؤ فيقال اتقد الجوهر والذهب (mufradat)

## و ل ه (root_005296) — documented alternative for ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

===== _commentary/v16/out/s104/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 104:6, and ## Buluşmalar) =====
## İnsanlar arasında yakılan ateş

İğneleyicinin işi insanlar arasında bir ateş yakmaktır; surenin ateşi buna karşılık gelir. {ar:نَارُ, tr:nâr, gloss:ateş, source:104:6} kelimesinin kökünde topluluk içinde patlak veren düşmanlığın adı vardır {ar:بينهم نائرة أي عداوة وشحناء, tr:beynehüm nâiratün ey adâvetün ve şahnâ', gloss:aralarında "naire" var, yani düşmanlık ve kin, source:"ن و ر,B007"}. {ar:ٱلْمُوقَدَةُ, tr:el-mûkade, gloss:tutuşturulmuş, source:104:6} kelimesinin kökü öfke ve savaş için de kullanılır {ar:اتقد فلان غضبا, tr:ittekade fülânün ğadaben, gloss:falan öfkeden tutuştu, source:"و ق د,B005"}; savaş ateş gibi yakılır {ar:يستعار وقد واتقد للحرب كاستعارة النار والاشتعال, tr:yüsteâru vekade ve'tteka de li'l-harb, gloss:tutuşmak savaş için de ödünç alınır, source:"و ق د,B005"}. Atılmanın kökü ise nefretle ayrılmayı ve açıkça savaş ilan etmeyi bilir {ar:نابذ فلان فلانا إذا فارقه عن قلى, tr:nâbeze fülânün fülânen izâ fârakahû an kılâ, gloss:ondan nefretle ayrıldı, source:"ن ب ذ,B002"}, {ar:نابذه الحرب كاشفه, tr:nâbezehü'l-harbe kâşefeh, gloss:ona açıkça savaş ilan etti, source:"ن ب ذ,B002"}. Son ayetteki {ar:عَمَدٍۢ, tr:amed, gloss:direkler, source:104:9} kelimesinin kökünde öfkenin acı olarak duyulması bile vardır {ar:عمد توجع من حزن أو غضب أو سقم, tr:amed teveccu'un min huznin ev ğadabin ev sekam, gloss:hüzünden, öfkeden ya da hastalıktan acı duymak, source:"ع م د,B015"}.

İlk ayetin kusur kollayan sözü bir kıvılcımdır; insanlar arasında kin tutuşur. Dördüncü ayetin atılışında aile imgesi olarak nefretle ayrılmanın sesi duyulur. Altıncı ayette yakılan ateş ise insanların değil, Allah'ındır. İğneleyicinin insanlar arasında yaktığı ateşe, sahibi Allah olan, tutuşturulmuş bir ateş karşılık verir.

Kuran savaşı yakılan ateş olarak anar. Maide suresinde Allah, "Allah'ın eli bağlıdır" diyen Yahudileri anlatır ve aralarına düşmanlık ve kin bıraktığını söyleyip ekler: {ar:كُلَّمَآ أَوْقَدُوا۟ نَارًۭا لِّلْحَرْبِ أَطْفَأَهَا ٱللَّهُ, tr:küllemâ evkadû nâran li'l-harbi atfeehallâh, gloss:savaş için ne zaman ateş yaksalar Allah onu söndürdü, source:5:64}. İnsanların yaktığı ateşi Allah söndürür; bu surede ise ateşi yakan Allah'tır. Muhammed suresinde Allah, maldan istenen bir payın içteki kini nasıl dışarı çıkaracağını söyler: {ar:إِن يَسْـَٔلْكُمُوهَا فَيُحْفِكُمْ تَبْخَلُوا۟ وَيُخْرِجْ أَضْغَٰنَكُمْ, tr:in yes'elkümûhâ fe-yuhfiküm tebhalû ve yuhric adğâneküm, gloss:sizden onu isteyip zorlasa cimrilik edersiniz ve kinlerinizi dışarı çıkarır, source:47:37}. Mal ile kin bu ayette bağlanır. Enfal suresinde Allah Peygambere hıyanetten korktuğu bir topluluk için {ar:فَٱنۢبِذْ إِلَيْهِمْ عَلَىٰ سَوَآءٍ, tr:fenbiz ileyhim alâ sevâ', gloss:onlara açıkça antlaşmayı at, source:8:58} der; atma fiili orada bir bağı açıkça koparmaktır.

Kaynaklar: 104:1 لُّمَزَةٍ ل م ز B001; 104:6 نَارُ ن و ر B007; 104:6 ٱلْمُوقَدَةُ و ق د B005; 104:9 عَمَدٍ ع م د B015; 104:4 لَيُنۢبَذَنَّ ن ب ذ B002

## Toplanan su, çiçeklenen ekin, kuru saplar

Surenin kelimeleri neredeyse eksiksiz bir doğa sürecini de taşır. Toplama fiilinin kökünde her yerden akıp birikmiş sel vardır {ar:استجمع السيل اجتمع من كل موضع, tr:istecme'a's-seyl ictema'a min külli mevdı', gloss:sel her yerden toplandı, source:"ج م ع,B010"}. Sayma fiilinin kökünde ise suyun toplandığı yer ve kesilmeyen kaynak {ar:العد مجتمع الماء, tr:el-idd mücteme'u'l-mâ', gloss:"idd" suyun toplandığı yerdir, source:"ع د د,B004"}, {ar:الماء العد الدائم الذي لا انقطاع له, tr:el-mâü'l-idd ed-dâim ellezî lâ inkıtâ'a leh, gloss:"idd" su, kesintisi olmayan sürekli sudur, source:"ع د د,B004"}. Bu tanımlarda "toplanmak", "sürekli" ve "kesilmeyen besleme" birlikte geçer; adamın mala yüklediği süreklilik, suyun dilinde zaten vardır. Son ayetin iki kelimesi de bu sahneye girer: bir nehrin başka bir nehirle beslenip kabarması {ar:مد النهر ومده نهر آخر, tr:medde'n-nehrü ve meddehû nehrün âhar, gloss:nehir kabardı, başka bir nehir onu besledi, source:"م د د,B003"}, selin önünü taş ve toprakla kesip suyu bir yerde toplamak {ar:عمدت السيل تعميدا إذا سددت وجه جريته حتى يجتمع في موضع بتراب أو حجارة, tr:ammedtü's-seyle ta'mîden izâ sedette vechü cerayetihî hattâ yectemi'a fî mevdı', gloss:selin akışını toprak ya da taşla kesip bir yerde toplanmasını sağladım, source:"ع م د,B013"}, ve yağmurla ıslanıp avuçta topaklanan toprak {ar:عمدت الأرض إذا رسخ فيها المطر إلى الثرى وتعقد في كفك, tr:amidet'il-ardu izâ rasaha fîhe'l-matar, gloss:yağmur toprağa işleyip avucunda topaklandı, source:"ع م د,B010"}. Bent bir direk gibi suyu tutar ve toplar.

Su ekini getirir. Yedinci ayetin fiilinin kökü ekinin baş göstermesini ve hurmanın tomurcuk vermesini anlatır {ar:طلع الزرع إذا بدا; وأطلعت النخلة إذا أخرجت طلعها, tr:tala'a'z-zer'u izâ bedâ ve atla'ati'n-nahletü, gloss:ekin baş gösterdi, hurma tomurcuğunu çıkardı, source:"ط ل ع,B005"}. Ateşin kökü ağacın çiçek açması için de kullanılır {ar:تنوير الشجرة: إزهارها, tr:tenvîru'ş-şecera izhâruhâ, gloss:ağacın "tenvir"i çiçek açmasıdır, source:"ن و ر,B004"}. Sonra sıcak gelir: tutuşma kökü yazın en sıcak günlerini adlandırır {ar:وقدة الصيف أشده حرا, tr:vakdetü's-sayf eşeddühû harran, gloss:yazın "vakde"si en sıcak zamanıdır, source:"و ق د,B004"}. Kırıcının kökü kıtlık yılını {ar:الحطمة السنة الشديدة لأنها تحطم كل شيء, tr:el-hutame es-senetü'ş-şedîde, gloss:hutame her şeyi kırdığı için şiddetli kıtlık yılıdır, source:"ح ط م,B003"}, sanma fiilinin kökü de gökten inip bahçeyi yakan ateşi, doluyu ya da çekirgeyi bilir {ar:حسبانا من السماء أي نارا تحرقها, tr:husbânen mine's-semâ' ey nâran tuhrikuhâ, gloss:gökten bir "husban", yani onu yakan bir ateş, source:"ح س ب,B007"}. Geriye kalan kırılmış kuru saplardır {ar:الحطام ما تكسر من اليبس, tr:el-hutâm mâ tekessera mine'l-yebs, gloss:hutam kurumuş şeyden kırılandır, source:"ح ط م,B001"}; aynı kelime dünyanın süsü ve malı için de söylenir {ar:حطام الدنيا عرضها وأثرها وزينتها, tr:hutâmü'd-dünyâ arazuhâ ve eseruhâ ve zînetühâ, gloss:dünya kırıntısı onun geçici malı ve süsüdür, source:"ح ط م,B009"}.

Sure kendi anlamında yalnızca toplama, sayma, sanma, atılma ve ateşi söyler. Bu süreç, kelimelerin ailesinde duyulur ve yığılan malı bir mevsim gibi gösterir: kesilmeyecek sanılan bir kaynak, kabaran bir nehir, çiçek, sonra sıcak, kıtlık, gökten ateş ve kuru sap. Kuran bu süreci malın çoğaltılmasının benzetmesi olarak açıkça kurar. Hadid suresinde Allah {ar:وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ ۖ كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا, tr:ve tekâsürun fi'l-emvâli ve'l-evlâd, ke-meseli ğaysin a'cebe'l-küffâra nebâtühû sümme yehîcü fe-terâhü musfarran sümme yekûnü hutâmâ, gloss:mallarda ve evlatlarda çoğalma yarışı; bitkisi ekincileri hayran bırakan bir yağmur gibi, sonra kurur, sararmış görürsün, sonra kırık saplara döner, source:57:20} der. "Hutam", surenin ateşinin adıyla aynı köktendir. Zümer suresinde Allah gökten indirdiği suyu {ar:فَسَلَكَهُۥ يَنَٰبِيعَ فِى ٱلْأَرْضِ, tr:fe-selekehû yenâbî'a fi'l-ard, gloss:onu yerde kaynaklara yürüttü, source:39:21} der, ekin çıkarır, sararır ve {ar:ثُمَّ يَجْعَلُهُۥ حُطَٰمًا, tr:sümme yec'alühû hutâmâ, gloss:sonra onu kırıntıya çevirir, source:39:21}. Vakıa suresinde Allah ekenlere sorar ve {ar:لَوْ نَشَآءُ لَجَعَلْنَٰهُ حُطَٰمًۭا فَظَلْتُمْ تَفَكَّهُونَ, tr:lev neşâü le-ce'alnâhü hutâmen fe-zaltüm tefekkehûn, gloss:dileseydik onu kırıntı yapardık da şaşakalırdınız, source:56:65} der. Kehf suresinde dünya hayatı suyla karışan bitkiye benzetilir ve {ar:فَأَصْبَحَ هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ, tr:fe-asbaha heşîmen tezrûhü'r-riyâh, gloss:rüzgârların savurduğu çer çöpe döndü, source:18:45}. Aynı surede iki bahçe sahibinin hikâyesi bu sürecin bütününü bir mal sahibinin başından geçirir: bahçenin arasından bir nehir akıtılmıştır, sahibi onun yok olmayacağını sanır ve arkadaşı ona Rabbinin {ar:وَيُرْسِلَ عَلَيْهَا حُسْبَانًۭا مِّنَ ٱلسَّمَآءِ فَتُصْبِحَ صَعِيدًۭا زَلَقًا, tr:ve yursile aleyhâ husbânen mine's-semâi fe-tusbiha sa'îden zelekâ, gloss:üzerine gökten bir "husban" gönderip onu kaygan bir toprağa çevirebileceğini, source:18:40} söyler. Bu "husban", surenin sanma fiiliyle aynı köktendir. Sonunda ürün kuşatılır ve adam {ar:فَأَصْبَحَ يُقَلِّبُ كَفَّيْهِ عَلَىٰ مَآ أَنفَقَ فِيهَا, tr:fe-asbaha yukallibü keffeyhi alâ mâ enfeka fîhâ, gloss:harcadıklarına yanıp avuçlarını ovuşturur hale geldi, source:18:42}. Avuç orada boş kalır. Taha suresinde de dünyanın süsü bir çiçektir: Allah Peygambere {ar:وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ زَهْرَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا, tr:ve lâ temüddenne ayneyke ilâ mâ metta'nâ bihî ezvâcen minhüm zehrete'l-hayâti'd-dünyâ, gloss:onlardan bazı kesimlere dünya hayatının çiçeği olarak verdiğimiz şeylere gözlerini dikme, source:20:131} der. Kehf suresi de aynı dersi çıkarır: {ar:ٱلْمَالُ وَٱلْبَنُونَ زِينَةُ ٱلْحَيَوٰةِ ٱلدُّنْيَا, tr:el-mâlü ve'l-benûne zînetü'l-hayâti'd-dünyâ, gloss:mal ve oğullar dünya hayatının süsüdür, source:18:46}.

Kaynaklar: 104:2 جَمَعَ ج م ع B010; 104:2 وَعَدَّدَهُۥ ع د د B004; 104:9 مُّمَدَّدَةٍۭ م د د B003; 104:9 عَمَدٍ ع م د B013; 104:9 عَمَدٍ ع م د B010; 104:7 تَطَّلِعُ ط ل ع B005; 104:6 نَارُ ن و ر B004; 104:6 ٱلْمُوقَدَةُ و ق د B004; 104:4 ٱلْحُطَمَةِ ح ط م B003; 104:3 يَحْسَبُ ح س ب B007; 104:4 ٱلْحُطَمَةِ ح ط م B001; 104:4 ٱلْحُطَمَةِ ح ط م B009

## Sürü: damgalanan, ağıla kapatılan, sürülen

Arapların dilinde mal çoğu zaman sürüdür {ar:كانت أموال العرب أنعامهم, tr:kânet emvâlü'l-Arabi en'âmehüm, gloss:Arapların malları hayvanlarıydı, source:"م و ل,B001"}. Bu kapıdan surenin kelimeleriyle kurulmuş bir çoban sahnesi açılır. Sürü bir araya toplanır ve sayılır; ikinci ayetin iki fiili bunu yapar. Hayvanlar sahibinin ateş damgasını taşır: devenin "nâr"ı onun damgasıdır {ar:ما نار هذه الناقة أي ما سمتها, tr:mâ nâru hâzihi'n-nâka ey mâ simetühâ, gloss:bu devenin ateşi nedir, yani damgası nedir, source:"ن و ر,B002"}. Hayvanlar dağda taştan bir ağılda tutulur ve bu ağılın adı sekizinci ayetteki kelimenin kökündendir, tanımında da "mal" geçer {ar:الوصيدة حجرة تجعل للمال في الجبل, tr:el-vasîde hucratün tüc'alü li'l-mâli fi'l-cebel, gloss:vasîde, dağda mal için yapılan bir ağıldır, source:"و ص د,B003"}. Sesçe komşu bir kökte ağılın, içindekini kuşattığı için böyle adlandırıldığı söylenir {ar:الحظيرة أصيدة سميت بذلك لاشتمالها على ما فيها, tr:el-hazîra esîdetün summiyet bi-zâlike li-iştimâlihâ alâ mâ fîhâ, gloss:ağıla içindekini kuşattığı için "esîde" denir, source:"ء ص د,B002"}; bu komşu kök bir yankıdır, aynı kökün kanıtı değildir.

Sürüyü kırıcının adı taşıyan acımasız çoban sürer: hayvanlara merhameti az olan, onları birbirine çarptırıp ezen kişiye "hutame" denir ve çobanların en kötüsü odur {ar:شر الرعاء الحُطَمَة, tr:şerru'r-ri'â'i'l-hutame, gloss:çobanların en kötüsü hutamedir, source:"ح ط م,B004"}, {ar:رجل حَطِم وحُطَمَة إذا كان قليل الرحمة للماشية يهشم بعضها ببعض, tr:racülün hatimün ve hutame izâ kâne kalîle'r-rahmeti li'l-mâşiye, gloss:hayvana merhameti az olup onları birbirine vurarak ezen adam, source:"ح ط م,B004"}. Önüne geleni çiğneyen yoğun deve sürüsüne de, aslanın sürü içinde yaptığı kırıma da aynı ad verilir {ar:حُطَمَة الأسد في المال عيثه وفرسه, tr:hutametü'l-esedi fi'l-mâl, gloss:aslanın maldaki hutamesi, onun yaptığı kırım ve parçalamadır, source:"ح ط م,B006"}. Binicinin topuğundaki demir mahmuz birinci ayetin kökündendir {ar:والمهمز والمهماز حديدة في مؤخر خف الرائض, tr:ve'l-mihmez ve'l-mihmâz hadîdetün fî mu'ahhari huffi'r-râid, gloss:mahmuz, at terbiyecisinin ayakkabısının arkasındaki demirdir, source:"ه م ز,B003"}; sürülen hayvanın bitkin düşmesi de surenin ilk kelimesinin kökündendir {ar:الكال المعيي, tr:el-kâll el-mu'yî, gloss:yorgun düşen, source:"ك ل ل,B001"}. Kökte kalabalık bölükler de vardır {ar:الكلاكل من الجماعات كالكراكر من الخيل, tr:el-kelâkil mine'l-cemâ'ât, gloss:kalabalık topluluklar, at bölükleri gibi, source:"ك ل ل,B009"}. Sahipleri tarafından ihmal edilmiş zayıf koyuna da atılma kökünden ad verilir {ar:يقال للشاة المهزولة التي يهملها أهلها نبيذة, tr:yükâlü li'ş-şâti'l-mehzûle nebîze, gloss:sahiplerinin ihmal ettiği zayıf koyuna "nebîze" denir, source:"ن ب ذ,B009"}. Sürü sahipleri de çadır halkıdır, otlağa göçerler {ar:كانوا أهل عمد ينتقلون إلى الكلأ, tr:kânû ehle amedin yentekılûne ile'l-kele', gloss:otlağa göçen direk, yani çadır halkıydılar, source:"ع م د,B004"}.

Sure bu sahneyi sahibine çevirir. Malı sürü olan adam atılır, üzerine ateş kapanır ve kapatılır. Damgalayan damgalanır, ağıl kuran ağıla kapatılır, sürüsünü ezerek süren çobanın adı ateşin adıdır. Kuran sürmeyi cehenneme yürüyüş olarak anlatır. Meryem suresinde Allah {ar:وَنَسُوقُ ٱلْمُجْرِمِينَ إِلَىٰ جَهَنَّمَ وِرْدًۭا, tr:ve nesûku'l-mücrimîne ilâ cehenneme virdâ, gloss:suçluları susuz bir sürü gibi cehenneme süreriz, source:19:86} der; "vird", suya inen sürüdür. Zümer suresinde {ar:وَسِيقَ ٱلَّذِينَ كَفَرُوٓا۟ إِلَىٰ جَهَنَّمَ زُمَرًا, tr:ve sîka'llezîne keferû ilâ cehenneme zümerâ, gloss:inkâr edenler bölük bölük cehenneme sürülür, source:39:71}, Kaf suresinde {ar:وَجَآءَتْ كُلُّ نَفْسٍۢ مَّعَهَا سَآئِقٌۭ وَشَهِيدٌۭ, tr:ve câet küllü nefsin me'ahâ sâikun ve şehîd, gloss:her can yanında bir sürücü ve bir tanıkla gelir, source:50:21}. Damga da Kuran'da vardır: Kalem suresinde mal ve oğullar sahibi hemmâz için Allah {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:se-nesimühû ale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16} der; "hurtum" bir hayvanın burnu için kullanılan kelimedir. Tevbe suresinde altın ve gümüş biriktirip infak etmeyenler için Allah kızdırılmış hazineyi damgaya çevirir: {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhühüm ve cünûbühüm ve zuhûruhüm, gloss:o gün bunlar cehennem ateşinde kızdırılır da alınları, yanları ve sırtları onlarla dağlanır, source:9:35}, {ar:هَٰذَا مَا كَنَزْتُمْ لِأَنفُسِكُمْ, tr:hâzâ mâ kenaztüm li-enfüsiküm, gloss:işte kendiniz için biriktirdiğiniz, source:9:35}. Al-i İmran suresinde dünyanın cazip kılınan şeyleri arasında {ar:وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ, tr:ve'l-hayli'l-müsevvemeti ve'l-en'âmi ve'l-hars, gloss:salma ve nişanlı atlar, hayvanlar ve ekinler, source:3:14} sayılır. Neml suresinde ise ezip geçen kalabalık bir ordudur: karınca ötekilere {ar:لَا يَحْطِمَنَّكُمْ سُلَيْمَٰنُ وَجُنُودُهُۥ وَهُمْ لَا يَشْعُرُونَ, tr:lâ yahtımenneküm Süleymânü ve cünûdühû ve hüm lâ yeş'urûn, gloss:Süleyman ve orduları farkında olmadan sizi ezmesin, source:27:18} der; ezici kalabalığın fiili ateşin adıyla aynı köktendir.

Kaynaklar: 104:2 مَالًا م و ل B001; 104:2 جَمَعَ ج م ع B001; 104:2 وَعَدَّدَهُۥ ع د د B001; 104:6 نَارُ ن و ر B002; 104:8 مُّؤْصَدَةٌۢ و ص د B003; 104:8 مُّؤْصَدَةٌۢ ء ص د B002; 104:4 ٱلْحُطَمَةِ ح ط م B004; 104:4 ٱلْحُطَمَةِ ح ط م B006; 104:1 هُمَزَةٍ ه م ز B003; 104:1 لِّكُلِّ ك ل ل B001; 104:1 لِّكُلِّ ك ل ل B009; 104:4 لَيُنۢبَذَنَّ ن ب ذ B009; 104:9 عَمَدٍ ع م د B004

## Ocak ve yutan ateş

Dördüncü ve yedinci ayet arasındaki ateş bir ocak gibi kurulur. {ar:ٱلْمُوقَدَةُ, tr:el-mûkade, gloss:tutuşturulmuş, source:104:6} kökü ateşin tutuşmasını {ar:كلمة تدل على اشتعال نار, tr:kelimetün tedüllü alâ iştiâli nâr, gloss:ateşin alevlenmesini gösteren bir kelime, source:"و ق د,B001"}, yakıtı {ar:الوقود الحطب, tr:el-vekûd el-hatab, gloss:vekûd odundur, source:"و ق د,B002"} ve ocağın yerini {ar:الموقد والمستوقد موضع النار, tr:el-mevkıd ve'l-müstevkad mevdı'u'n-nâr, gloss:ateşin yeri, source:"و ق د,B003"} adlandırır. "Mûkade" edilgendir: biri onu yakmıştır, ateş kendiliğinden değil tutuşturulmuş olarak durur. Dördüncü ayetin atılışı bu sahnede ocağa yakıt atmaya benzer; Arapçada atma fiili hurmayı ya da kuru üzümü bir kaba atıp üstüne su dökmek için de kullanılır {ar:يأخذ تمرا أو زبيبا فينبذه أي يلقيه في وعاء أو سقاء ويصب عليه الماء, tr:ye'huzü temran ev zebîben fe-yenbizühû, gloss:hurma ya da üzüm alıp bir kaba atar ve üstüne su döker, source:"ن ب ذ,B006"}. Büyük kazana da toplama kökünden ad verilir {ar:قدر جامعة وهي العظيمة, tr:kidrun câmi'atün ve hiye'l-azîme, gloss:büyük kazana "câmia" denir, source:"ج م ع,B012"}. Kalıcılık kökü ise ocak taşlarını, uzun süre yerinde kaldıkları için, "kalıcılar" diye anar {ar:خوالد للأثافي والحجارة لطول مكثها, tr:havâlid li'l-esâfî ve'l-hicâra li-tûli mekshihâ, gloss:ocak taşlarına uzun süre kaldıkları için "havâlid" denir, source:"خ ل د,B001"}. Kendisini kalıcı sanan adamın kelimesinde kalıcı olanlar ateşin altındaki taşlardır.

Yedinci ayetin {ar:ٱلْأَفْـِٔدَةِ, tr:el-ef'ide, gloss:yürekler, source:104:7} kelimesinin kökü sıcaklık ve kızgınlık bildirir {ar:أصل صحيح يدل على حمى وشدة حرارة, tr:aslün sahîhun yedüllü alâ hummâ ve şiddeti harâra, gloss:ateşli sıcaklık ve şiddetli harareti gösterir, source:"ف ء د,B001"}; eti kızartmak ve ekmeği sıcak külde pişirmek bu köktendir {ar:فأدت اللحم شويته ولحم فئيد أي مشوي, tr:fe'edtü'l-lahme şeveytüh, gloss:eti kızarttım; "feîd" kızarmış ettir, source:"ف ء د,B001"}, {ar:فأدت الخبزة مللتها أو خبزتها في الملة, tr:fe'edtü'l-hubzete melletühâ, gloss:ekmeği sıcak külde pişirdim, source:"ف ء د,B001"}. Arapça bu kökü doğrudan altıncı ayetin fiiliyle açıklar {ar:افتأد القوم إذا أوقدوا نارا والفئيد النار نفسها, tr:ifte'ede'l-kavmü izâ evkadû nâran, gloss:topluluk ateş yaktığında "ifte'ede" denir; feîd ateşin kendisidir, source:"ف ء د,B001"}.

Ateşin adı onu bir yiyici yapar. {ar:ٱلْحُطَمَةِ, tr:el-hutame, gloss:ezip kıran, source:104:4} ateşe karşılaştığı her şeyi kırdığı için verilmiştir {ar:سميت النار الحُطَمَة لحطمها ما تلقى, tr:summiyeti'n-nâru'l-hutame li-hatmihâ mâ telkâ, gloss:ateşe, karşılaştığını kırdığı için hutame denmiştir, source:"ح ط م,B002"}. Aynı ad çok yiyen kişiye de verilir ve Arapça bu adı açıkça cehenneme benzetmeye bağlar {ar:قيل للأكول حُطَمَة تشبيها بالجحيم, tr:kîle li'l-ekûli hutame teşbîhen bi'l-cahîm, gloss:obur kişiye cehenneme benzetilerek hutame denmiştir, source:"ح ط م,B008"}; öğütüp sindiren organlara da bu kökten ad verilir {ar:يقال للجوارس حاطوم وهاضوم, tr:yükâlü li'l-cevâris hâtûm ve hâdûm, gloss:öğüten organlara hâtûm ve hâdûm denir, source:"ح ط م,B008"}. Ateş, aldığını parçalayan bir midedir. Yedinci ayetin fiilinin bir dalı ise yemenin tersini, kusmayı adlandırır {ar:أطلع الرجل إطلاعا إذا قاء, tr:atla'a'r-racülü izâ kâe, gloss:adam kustu, source:"ط ل ع,B011"}. Bu dal ayetin anlamına girmez; aile imgesi olarak, yutulanın yukarı doğru çıkışını, ateşin içten yukarı yükselişinin yanında duyurur.

Kuran mal sahiplerini yakıt olarak anar. Al-i İmran suresinde Allah {ar:إِنَّ ٱلَّذِينَ كَفَرُوا۟ لَن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُم مِّنَ ٱللَّهِ شَيْـًۭٔا ۖ وَأُو۟لَٰٓئِكَ هُمْ وَقُودُ ٱلنَّارِ, tr:inne'llezîne keferû len tuğniye anhüm emvâlühüm ve lâ evlâdühüm minallâhi şey'â, ve ülâike hüm vekûdü'n-nâr, gloss:inkâr edenlere malları da evlatları da Allah'a karşı bir yarar sağlamaz; ateşin yakıtı onlardır, source:3:10} der. Bakara suresinde Kuran'dan şüphe edenlere ve Tahrim suresinde müminlere aynı ateş anılır: {ar:وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:vekûdühe'n-nâsü ve'l-hicâra, gloss:yakıtı insanlar ve taşlardır, source:66:6}. Enbiya suresinde Allah putperestlere {ar:إِنَّكُمْ وَمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ حَصَبُ جَهَنَّمَ, tr:inneküm ve mâ ta'büdûne min dûnillâhi hasabü cehennem, gloss:siz ve Allah'tan başka taptıklarınız cehennemin çırasısınız, source:21:98} der. Mümin suresinde zincirlerle sürüklenenler {ar:فِى ٱلْحَمِيمِ ثُمَّ فِى ٱلنَّارِ يُسْجَرُونَ, tr:fi'l-hamîmi sümme fi'n-nâri yuscerûn, gloss:kaynar suda, sonra ateşte yakılırlar, source:40:72}. Buruc suresinde ateşin kendisi yakıtla tanımlanır: {ar:ٱلنَّارِ ذَاتِ ٱلْوَقُودِ, tr:en-nâri zâti'l-vekûd, gloss:yakıtı bol ateş, source:85:5}. Nisa suresinde pişme açıkça söylenir: {ar:كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا, tr:küllemâ nadıcet cülûdühüm beddelnâhüm cülûden ğayrahâ, gloss:derileri pişip bittikçe onları başka derilerle değiştiririz, source:4:56}. Aynı surede yenen mal ateşe dönüşür: {ar:إِنَّ ٱلَّذِينَ يَأْكُلُونَ أَمْوَٰلَ ٱلْيَتَٰمَىٰ ظُلْمًا إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا, tr:inne'llezîne ye'külûne emvâle'l-yetâmâ zulmen innemâ ye'külûne fî butûnihim nârâ, gloss:yetimlerin mallarını haksızca yiyenler karınlarına ancak ateş yerler, source:4:10}. Kaf suresinde Allah cehenneme sorar ve o doymaz: {ar:يَوْمَ نَقُولُ لِجَهَنَّمَ هَلِ ٱمْتَلَأْتِ وَتَقُولُ هَلْ مِن مَّزِيدٍۢ, tr:yevme nekûlü li-cehenneme heli'mtele'ti ve tekûlü hel min mezîd, gloss:o gün cehenneme "doldun mu" deriz, o da "daha var mı" der, source:50:30}. Ra'd suresinde ise insanlar süs ya da eşya elde etmek için madenin üstüne ateş yakar: {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ ٱبْتِغَآءَ حِلْيَةٍ أَوْ مَتَٰعٍۢ زَبَدٌۭ مِّثْلُهُۥ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâri'btiğâe hilyetin ev metâ'in zebedün mislüh, gloss:süs ya da eşya elde etmek için ateşte üzerine yaktıkları şeyden de onun gibi bir köpük çıkar, source:13:17}; köpük gider, insanlara yarayan yerde kalır. Mal için yakılan ateşte bile kalıcı olan, yarar olandır.

Kaynaklar: 104:6 ٱلْمُوقَدَةُ و ق د B001; 104:6 ٱلْمُوقَدَةُ و ق د B002; 104:6 ٱلْمُوقَدَةُ و ق د B003; 104:3 أَخْلَدَهُۥ خ ل د B001; 104:2 جَمَعَ ج م ع B012; 104:4 لَيُنۢبَذَنَّ ن ب ذ B006; 104:7 ٱلْأَفْـِٔدَةِ ف ء د B001; 104:4 ٱلْحُطَمَةِ ح ط م B002; 104:4 ٱلْحُطَمَةِ ح ط م B008; 104:7 تَطَّلِعُ ط ل ع B011

## Tutuşan yürek

{ar:ٱلْأَفْـِٔدَةِ, tr:el-ef'ide, gloss:yürekler, source:104:7} kelimesi kalbin bir adıdır, ama sıcaklık yönüyle anılan adıdır: kalbe, tutuşma anlamı göz önünde tutulduğunda "fuâd" denir {ar:الفؤاد كالقلب لكن يقال له فؤاد إذا اعتبر فيه معنى التفؤد أي التوقد, tr:el-fuâdü ke'l-kalb lâkin yükâlü lehû fuâdun izâ'tübira fîhi ma'ne't-tefe'üd ey et-tevakkud, gloss:fuad kalp gibidir, ama içinde tutuşma anlamı gözetildiğinde fuad denir, source:"ف ء د,B002"}. Tanımdaki "tevakkud", altıncı ayetin {ar:ٱلْمُوقَدَةُ, tr:el-mûkade, gloss:tutuşturulmuş, source:104:6} kelimesinin köküdür {ar:وقدت النار واتقدت وتوقدت وأوقدتها, tr:vekadeti'n-nâru vetteka det ve tevakkadet ve evkadtühâ, gloss:ateş tutuştu, alevlendi, ben onu yaktım, source:"و ق د,B001"}. Tutuşturulmuş ateş, tutuşmayla adlanan organa çıkar. Ayetin sırası bunu yapar: önce ateşin sıfatı, hemen ardından onun ulaştığı yer.

Kalp aynı zamanda üçüncü ayetteki sanının oturduğu yerdir. {ar:أَخْلَدَهُۥ, tr:ahledeh, gloss:onu kalıcı kıldı, source:104:3} kelimesinin kökünden "hald", kalpte yerleşik olduğu için akıl ve gönül demektir {ar:الخلد البال وسمي بذلك لأنه مستقر في القلب ثابت, tr:el-haled el-bâl ve summiye bi-zâlike li-ennehû müstekırrun fi'l-kalbi sâbit, gloss:"haled" gönüldür; kalpte sabit durduğu için böyle denmiştir, source:"خ ل د,B004"}, {ar:وقع ذلك في خلدي أي في قلبي, tr:veka'a zâlike fî haledî ey fî kalbî, gloss:bu benim içime, yani kalbime düştü, source:"خ ل د,B004"}. Sanı kalpte doğdu; ateş kalbe çıkar. Kalbin kökü bir de avı kalbinden vurmayı ve kalp hastalığını {ar:فأدته فهو مفؤود أصبت فؤاده وكذلك إذا أصابه داء فؤاده, tr:fe'edtühû fe-hüve mef'ûd, gloss:onu kalbinden vurdum; kalp hastalığına tutulan da "mef'ûd"dur, source:"ف ء د,B003"}, korkudan zayıflamış yüreği {ar:المفؤود الضعيف الفؤاد الجبان مثل المنخوب, tr:el-mef'ûd ed-da'îfü'l-fuâd el-cebân, gloss:yüreği zayıf, korkak kişi, source:"ف ء د,B004"} adlandırır. Son ayetin kökü de kalbi hüzün ve hastalıkla çökertilmiş olarak anar {ar:القلب الذي يعمده الحزن والسقيم الذي يعمده السقم, tr:el-kalbü'llezî ya'midühü'l-huzn, gloss:hüznün çökerttiği kalp ve hastalığın çökerttiği hasta, source:"ع م د,B008"}. Yürek tutuşan, vurulan, zayıflayan ve çöken bir organ olarak dört kelimenin ailesinde görünür. Surenin ilk kelimesinin kökünde göğüs, kalbin barındığı yer olarak geçer {ar:الكلكل الصدر, tr:el-kelkel es-sadr, gloss:kelkel göğüstür, source:"ك ل ل,B007"}; ilk ayetin kökündeki şeytan dürtüsü de kalbe çöker.

Dışarıda toplanan mala, en içteki organa ulaşan ateş karşılık verir. Kuran malı ve kalbi aynı ölçüye koyar. Şuara suresinde İbrahim duasında hesap gününü anar: {ar:يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ, tr:yevme lâ yenfe'u mâlün ve lâ benûn, gloss:malın da oğulların da yarar vermediği gün, source:26:88}, {ar:إِلَّا مَنْ أَتَى ٱللَّهَ بِقَلْبٍۢ سَلِيمٍۢ, tr:illâ men etallâhe bi-kalbin selîm, gloss:ancak Allah'a temiz bir kalple gelen müstesna, source:26:89}. Değer, toplanan şeyde değil kalptedir. İsra suresinde Allah {ar:إِنَّ ٱلسَّمْعَ وَٱلْبَصَرَ وَٱلْفُؤَادَ كُلُّ أُو۟لَٰٓئِكَ كَانَ عَنْهُ مَسْـُٔولًۭا, tr:inne's-sem'a ve'l-basara ve'l-fuâde küllü ülâike kâne anhü mes'ûlâ, gloss:kulak, göz ve yürek, bunların her biri ondan sorumludur, source:17:36} der; bilmediği şeyin ardına düşmeyi yasaklayan ayettir ve "fuad" sorguya açıktır. Mutaffifin suresinde Allah kazancın kalplerin üstünü kapladığını söyler: {ar:كَلَّا ۖ بَلْ ۜ رَانَ عَلَىٰ قُلُوبِهِم مَّا كَانُوا۟ يَكْسِبُونَ, tr:kellâ bel râne alâ kulûbihim mâ kânû yeksibûn, gloss:hayır, kazandıkları kalplerinin üstünü pas gibi kaplamıştır, source:83:14}. Adiyat suresinde insan {ar:وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ, tr:ve innehû li-hubbi'l-hayri le-şedîd, gloss:o mal sevgisinde çok şiddetlidir, source:100:8} diye anlatılır ve kabirler deşildiğinde {ar:وَحُصِّلَ مَا فِى ٱلصُّدُورِ, tr:ve hussıle mâ fi's-sudûr, gloss:göğüslerdekiler ortaya dökülür, source:100:10}. Hac suresinde içi eriten sıcaklık söylenir: {ar:يُصْهَرُ بِهِۦ مَا فِى بُطُونِهِمْ وَٱلْجُلُودُ, tr:yusharu bihî mâ fî butûnihim ve'l-cülûd, gloss:onunla karınlarındakiler ve derileri eritilir, source:22:20}. İbrahim suresinde o günün yürekleri boştur: {ar:وَأَفْـِٔدَتُهُمْ هَوَآءٌۭ, tr:ve ef'idetühüm hevâ', gloss:yürekleri bomboştur, source:14:43}.

Kaynaklar: 104:7 ٱلْأَفْـِٔدَةِ ف ء د B002; 104:6 ٱلْمُوقَدَةُ و ق د B001; 104:3 أَخْلَدَهُۥ خ ل د B004; 104:7 ٱلْأَفْـِٔدَةِ ف ء د B003; 104:7 ٱلْأَفْـِٔدَةِ ف ء د B004; 104:9 عَمَدٍ ع م د B008; 104:1 هُمَزَةٍ ه م ز B005; 104:1 لِّكُلِّ ك ل ل B007

## Aşağı atılan, yukarı çıkan ve hedefini bulan ateş

Surenin dikey bir sahnesi vardır ve bir avcının nişanı ile aynı hareketi paylaşır. Adam aşağı atılır; atma kökünün özü fırlatıp bırakmaktır {ar:أصل صحيح يدل على طرح وإلقاء, tr:aslün sahîhun yedüllü alâ tarhin ve ilkâ', gloss:atıp bırakmayı gösterir, source:"ن ب ذ,B001"}. Ateş ise yukarı çıkar. {ar:تَطَّلِعُ, tr:tattali'u, gloss:çıkıp vurur, üstüne tırmanır, source:104:7} fiilinin kökü güneşin ve yıldızın doğuşudur {ar:طلعت الشمس والكوكب طلوعا ومطلعا, tr:tala'ati'ş-şemsü ve'l-kevkeb, gloss:güneş ve yıldız doğdu, source:"ط ل ع,B001"}; görünmek ve belirmek {ar:أصل واحد صحيح يدل على ظهور وبروز, tr:aslün vâhidün sahîhun yedüllü alâ zuhûrin ve burûz, gloss:görünüp ortaya çıkmayı gösterir, source:"ط ل ع,B001"}. Bir dağın tepesine tırmanmak ve tepeden aşağıya bakılan yerin dehşeti de bu köktendir {ar:طلعت الجبل أي علوته, tr:tala'tü'l-cebele ey alevtüh, gloss:dağa çıktım, yani üstüne yükseldim, source:"ط ل ع,B006"}, {ar:هول المطلع, tr:hevlü'l-muttala', gloss:tepeden bakılan yerin dehşeti, source:"ط ل ع,B006"}. Bir kabı ağzına kadar doldurmak da {ar:قدح طلاع ممتلىء, tr:kadahun tılâ'un mümteli', gloss:ağzına kadar dolu kap, source:"ط ل ع,B007"}. Ayetteki yapı da önemlidir: fiil "alâ" edatıyla gelir ve Arapçada aynı yapı bir topluluğun üstüne baskın yapmak için kullanılır {ar:طلع علينا فلان يطلع طلوعا إذا هجم, tr:tala'a aleynâ fülânün izâ hecem, gloss:falan üstümüze çıkageldi, yani baskın yaptı, source:"ط ل ع,B002"}. Ateş doğan bir güneş gibi belirir, bir tırmanıcı gibi yükselir, bir baskıncı gibi üstlerine gelir ve kabı doldurur gibi yükselir. Ateşin kökünde de kararsızca kıpırdayan ışık vardır {ar:أصل صحيح يدل على إضاءة واضطراب وقلة ثبات, tr:aslün sahîhun yedüllü alâ idâetin ve ıdtırâbin ve kılleti sebât, gloss:aydınlanma, çalkalanma ve sabit durmamayı gösterir, source:"ن و ر,B001"}.

Bu yükseliş bir hedefe yöneliktir. Beşinci ayetin {ar:أَدْرَىٰكَ, tr:edrâke, gloss:sana bildirdi, source:104:5} fiilinin kökü avcının ustalığını da taşır: avın yerini daha görmeden kollamak ve onu bir siper hayvanının ardından gizlice yaklaşarak aldatmak {ar:تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته, tr:tedarreytü's-sayde izâ nazartü eyne hüve ve lem erahü ba'd, gloss:avı henüz görmeden nerede olduğunu kolladım ve ona sinsice yaklaştım, source:"د ر ي,B003"}, {ar:الدرية الدابة التي يستتر بها الذي يرمي الصيد, tr:ed-dariyye ed-dâbbetü'lletî yesteteru bihe'llezî yermi's-sayd, gloss:avcının ardına saklandığı hayvan, source:"د ر ي,B003"}, nişan alıştırması yapılan halka {ar:الدريئة الحلقة التي يتعلم عليها الطعن, tr:ed-darî'e el-halkatü'lletî yute'allemu aleyhe't-ta'n, gloss:mızrak atmanın öğrenildiği halka, source:"د ر ي,B005"} ve bir yeri seçip baskın için ona yönelmek {ar:ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة, tr:iddarâ benû fülânin mekâne kezâ ey i'temedûhü bi-ğazvin ev ğâra, gloss:falan oğulları bir yeri seçip baskınla ona yöneldiler, source:"د ر ي,B002"}. Bu açıklamadaki "i'temedûhü", son ayetteki direklerin köküdür; o kökte kasten yönelmek de vardır {ar:العمد والتعمد خلاف السهو, tr:el-amd ve't-ta'ammüd hilâfü's-sehv, gloss:kasıt, yanılmanın zıddıdır, source:"ع م د,B001"}. İlk ayetin kökü güçlü atan yayı adlandırır {ar:قوس همزي شديدة الدفع للسهم, tr:kavsün hemezâ şedîdetü'd-def'i li's-sehm, gloss:oku güçlü iten yay, source:"ه م ز,B003"}; yedinci ayetin kökü düşmanı gözetlemek için önden gönderilen öncüleri {ar:الطليعة قوم يبعثون ليطلعوا طلع العدو, tr:et-talî'a kavmün yüb'asûne li-yattali'û tal'a'l-adüvv, gloss:düşmanın durumunu gözetlemek için gönderilen topluluk, source:"ط ل ع,B004"}; yüreklerin kökü avı kalbinden vurmayı {ar:فأدت الصيد إذا أصبت فؤاده, tr:fe'edtü's-sayde izâ esabtü fuâdeh, gloss:avı kalbinden vurdum, source:"ف ء د,B003"}. Aynı kökün bir dalı tersini de söyler: atıcının oku hedefin üstünden aşıp gider {ar:وأطلع الرامي أي جاز سهمه من فوق الغرض, tr:ve atla'a'r-râmî ey câze sehmühû min fevki'l-ğaraz, gloss:atıcı "atla'a" etti, yani oku hedefin üstünden geçti, source:"ط ل ع,B010"}. Surenin yükselişi aşmaz: {ar:عَلَى ٱلْأَفْـِٔدَةِ, tr:ale'l-ef'ide, gloss:yüreklerin üzerine, source:104:7} durur. Bunlar fiilin ayetteki anlamının yanında duyulan aile imgeleridir; ayetin kendisi ateşin yüreklere ulaştığını söyler.

Yükseliş, sekizinci ayette yukarıdan kapanan örtüyle biter: {ar:إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ, tr:innehâ aleyhim mü'sade, gloss:o, üzerlerine kapatılmıştır, source:104:8}; "aleyhim" yedinci ayetteki "alâ"yı tekrar eder. Kökün anlamı kapıyı kapatıp sıkıca örtmektir {ar:أوصدت الباب وآصدته أي أطبقته وأحكمته ومؤصدة مطبقة, tr:evsadtü'l-bâbe ve âsadtühû ey atbaktühû ve ahkemtüh, gloss:kapıyı kapadım, sıkıca örttüm; mü'sade üstü kapatılmış demektir, source:"و ص د,B001"}.

Kuran ateşe atılmayı ve ateşin onlara yönelişini başka yerlerde canlandırır. Furkan suresinde Allah {ar:إِذَا رَأَتْهُم مِّن مَّكَانٍۭ بَعِيدٍۢ سَمِعُوا۟ لَهَا تَغَيُّظًۭا وَزَفِيرًۭا, tr:izâ raethüm min mekânin ba'îdin semi'û lehâ teğayyuzan ve zefîrâ, gloss:onları uzaktan görünce, onun öfkeyle köpürüşünü ve uğultusunu duyarlar, source:25:12} der; ateş görür ve hedefine yönelir, ardından {ar:وَإِذَآ أُلْقُوا۟ مِنْهَا مَكَانًۭا ضَيِّقًۭا مُّقَرَّنِينَ دَعَوْا۟ هُنَالِكَ ثُبُورًۭا, tr:ve izâ ülkû minhâ mekânen dayyikan mukarranîne de'av hünâlike sübûrâ, gloss:bağlanmış olarak onun dar bir yerine atıldıklarında orada yok olmayı dilerler, source:25:13}. Mülk suresinde {ar:إِذَآ أُلْقُوا۟ فِيهَا سَمِعُوا۟ لَهَا شَهِيقًۭا وَهِىَ تَفُورُ, tr:izâ ülkû fîhâ semi'û lehâ şehîkan ve hiye tefûr, gloss:oraya atıldıklarında onun hırıltısını duyarlar, o kaynar, source:67:7}, {ar:تَكَادُ تَمَيَّزُ مِنَ ٱلْغَيْظِ, tr:tekâdü temeyyezü mine'l-ğayz, gloss:öfkeden neredeyse çatlayacaktır, source:67:8}. Yukarı yol kapalıdır: Hac suresinde {ar:كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَا مِنْ غَمٍّ أُعِيدُوا۟ فِيهَا, tr:küllemâ erâdû en yahrucû minhâ min ğammin u'îdû fîhâ, gloss:kederden oradan çıkmak istedikçe oraya geri döndürülürler, source:22:22}, Secde suresinde de aynı söz {source:32:20}. Atılmanın kendisi Kasas suresinde Firavun ve ordusu için anlatılır: {ar:فَأَخَذْنَٰهُ وَجُنُودَهُۥ فَنَبَذْنَٰهُمْ فِى ٱلْيَمِّ, tr:fe-ehaznâhü ve cünûdehû fe-nebeznâhüm fi'l-yemm, gloss:onu ve ordularını yakalayıp denize attık, source:28:40}. Aynı surede Firavun yükselmeyi ve tutuşturmayı tek cümlede ister: {ar:فَأَوْقِدْ لِى يَٰهَٰمَٰنُ عَلَى ٱلطِّينِ فَٱجْعَل لِّى صَرْحًۭا لَّعَلِّىٓ أَطَّلِعُ إِلَىٰٓ إِلَٰهِ مُوسَىٰ, tr:fe-evkıd lî yâ Hâmânü ale't-tîni fec'al lî sarhan le'allî ettali'u ilâ ilâhi Mûsâ, gloss:Haman, benim için çamurun üstünde ateş yak, bana bir kule yap; belki Musa'nın ilahına çıkıp bakarım, source:28:38}. İnsanın yaktığı ateşle kurulan kule yukarı çıkmak içindir; bu surede ise tutuşturulmuş ateşin kendisi yükselir. Saffat suresinde cennetteki bir kişi dünyadaki arkadaşını arar: {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettala'a fe-raâhü fî sevâi'l-cahîm, gloss:yukarıdan baktı ve onu cehennemin ortasında gördü, source:37:55}. Aynı fiil orada tepeden aşağı bakmaktır.

Kaynaklar: 104:4 لَيُنۢبَذَنَّ ن ب ذ B001; 104:7 تَطَّلِعُ ط ل ع B001; 104:7 تَطَّلِعُ ط ل ع B002; 104:7 تَطَّلِعُ ط ل ع B006; 104:7 تَطَّلِعُ ط ل ع B007; 104:7 تَطَّلِعُ ط ل ع B010; 104:7 تَطَّلِعُ ط ل ع B004; 104:6 نَارُ ن و ر B001; 104:5 أَدْرَىٰكَ د ر ي B003; 104:5 أَدْرَىٰكَ د ر ي B005; 104:5 أَدْرَىٰكَ د ر ي B002; 104:9 عَمَدٍ ع م د B001; 104:1 هُمَزَةٍ ه م ز B003; 104:7 ٱلْأَفْـِٔدَةِ ف ء د B003; 104:8 مُّؤْصَدَةٌۢ و ص د B001

## Buluşmalar

İlk ayetteki iki kelime iki imgeyi aynı anda taşır: el ve dil. İtme ifadesi ile gıyap ve huzur ifadesi aynı iki kelimeyi birleştirir. Mümtehine suresindeki ayet, ellerin ve dillerin birlikte kötülükle uzatılmasını {source:60:2} söyleyerek bu ikisini tek sahnede toplar. Sıkan, iten, kusur arayan ve arkadan dürten kişi, ikinci ayette malın üstüne kapanan yumruğa dönüşür. Kökte o yumruğun sonu bukağıdır, ellerin boyna toplanması {source:"ج م ع,B008"}. Hakka suresinde malının işe yaramadığını söyleyen adam bukağılanır {source:69:30}. Toplayan el ile bağlanan el, aynı kökün iki ucudur.

Sayma ile yaslanma üçüncü ayetin bir tek fiilinde buluşur: "yahsebü" hem saymanın hem yeterliğin köküdür, kalıcılık fiili de sanarak yaslanmak diye açıklanır. Tevbe suresindeki {ar:خَٰلِدِينَ فِيهَا ۚ هِىَ حَسْبُهُمْ, tr:hâlidîne fîhâ, hiye hasbühüm, gloss:orada kalıcı olarak; o onlara yeter, source:9:68} sözü, adamın mala yüklediği iki şeyi, kalıcılığı ve yeterliği, ateşe verir. Aynı iki imge su sahnesiyle de buluşur: sayma kökündeki kesilmeyen su, adamın sandığı süreklilik; kırıcının kökündeki tükenen mal, bu sürekliliğin sonu. Kehf suresindeki bahçe sahibi bu yolu baştan sona yürür: bahçesinin arasından nehir akar, bahçenin yok olmayacağını sanır, sanma fiiliyle aynı kökten bir "husban" bahçeyi vurur ve avuçları boş kalır {source:18:40}. Hadid suresi aynı yolu mal çoğaltma yarışının benzetmesi yapar ve "hutam" ile bitirir {source:57:20}.

Kalıcılık ile ocak arasında bir buluşma daha vardır: kalıcılık kökünde "kalıcılar" diye anılan tek şey ocak taşlarıdır. Kendini kalıcı sanan adam, ateşin altında yıllarca kalan taşların adını taşıyan bir fiille konuşur. Kalıcılık kökünün bir dalı da kalbe gider: sanı, kalpte yerleşik olan gönüle düşer. Ocak ile yürek de iki kez birleşir: yürek tutuşmayla adlandırılır ve yüreklerin kökü ateş yakmanın fiiliyle açıklanır. Altıncı ve yedinci ayetler bu yüzden bir sıfat ile onun yerini ardı ardına söyler: tutuşturulmuş ateş, tutuşmayla adlanan yüreğe çıkar. Sanının oturduğu yer, ateşin vardığı yerdir.

Sürü ile kapalı yapı sekizinci ayetin kelimesinde buluşur: aynı kök mal için dağda yapılan taş ağılı ve üstü kapatılmış ateşi adlandırır. Sürüyü ağıla kapatan adam, kapatılmış bir ateşin içindedir. Sürü ile ateş damgada buluşur: devenin ateşi damgasıdır, Tevbe suresinde biriktirilen hazine kızdırılıp alınlara basılır {source:9:35}, Kalem suresinde mal ve oğullar sahibi hemmâz burnundan damgalanır {source:68:16}. Bu son ayet ilk imge ile sürüyü birbirine bağlar: iğneleyen dil, mal ve damga aynı adamdadır.

Yükselen ateş ile avcı, aynı kökün iki dalında buluşur: ateşin yükselişini anlatan fiil, okun hedefin üstünden aşmasını da adlandırır ve bu ateş aşmaz, yüreklerin üstünde durur. Avcının kolladığı yer yürektir; yüreklerin kökü avı kalbinden vurmaktır. Bilmek ile avcılık da beşinci ayetin fiilinde aynı köktür: görmeden kollamak ve bilmek. Sanan adam ile içini bilen ateş arasındaki mesafeyi, "ne bildirdi" sorusu kapatır ve cevabı Allah'ın ateşi olarak verir.

Surenin hareketi bu buluşmalarla taşınır. İlk iki ayette her şey adamın elindedir: sıkan, iten, toplayan, sayan bir el ve onu yaralayan bir dil. Üçüncü ayette bu el bir sanıya dayanır ve kalbe yerleşir. Dördüncü ayetten sonra yön tersine döner: el açılır ve atılan adamın kendisidir; topladığı malın adı kırıntı olur, saydığı sayı onu saymaz, dayandığı direkler onu tutar, sürüsünü kapattığı ağıl üzerine kapanır. Ateş aşağıdan yükselir ve sanının oturduğu yüreğe ulaşır. İlk ayetteki kuşatma kelimesinden son ayetteki direklere kadar sure, dışarıya uzanan bir elden içeriye kapanan bir yapıya doğru ilerler.

