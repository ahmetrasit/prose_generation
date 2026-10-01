Focus: 107:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/OZTURK/_projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. No other command or tool is available.

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


===== _commentary/v16/work/107_2/D.r13/context.md =====
# 107:2 — focus

فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ

Anchor translation (canonical reading, reference only):

İşte yetimi itip kakan odur.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَذَٰلِكَ | ذَٰلِك |  | CONJ;DEM |
| 2 | ٱلَّذِى | ٱلَّذِى |  | REL |
| 3 | يَدُعُّ | يَدُعُّ | د ع ع | V |
| 4 | ٱلْيَتِيمَ | يَتِيم | ي ت م | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 107 — full text (context; no pericope)

- 107:1 أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ
- 107:2 ◀ focus فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ
- 107:3 وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 107:4 فَوَيْلٌۭ لِّلْمُصَلِّينَ
- 107:5 ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ
- 107:6 ٱلَّذِينَ هُمْ يُرَآءُونَ
- 107:7 وَيَمْنَعُونَ ٱلْمَاعُونَ


===== _commentary/v16/work/107_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## د ع ع (root_000477) — identity root of يَدُعُّ (w3)

- **B001** itme — sert ve kaba itme · sertçe itmek · yetimi itip azarlamak · ateşe doğru zorla sürmek
  الدَّعّ الدفع (maqayis;tahdhib)؛ دَعَعته أدَعُّه دَعًّا أي دفعته (sihah)؛ دفع في جفوة (ayn)؛ الدفع الشديد (mufradat)
- **B002** sallayarak doldurma — kabı sallayarak doldurma · bir şeyi doldurmak veya hareket ettirerek sıkıştırmak · ağzına kadar dolu büyük çanak · selin vadiyi doldurması
  الدعدعة تحريك المكيال ليستوعب الشيء (maqayis)؛ دعدعت الشيء ملأته وجفنة مدعدعة (sihah)؛ دعدع مكيالا أو جوالقا حتى يكتنز (tahdhib)
- **B003** hayvanı seslenerek yönlendirme — küçükbaş hayvanı seslenerek çağırma veya azarlama · keçilere seslenip onları yönlendirmek · çobanın keçileri yönlendirmek için çıkardığı geleneksel çağrı
  الدعدعة زجر الغنم (maqayis)؛ للمعز خاصة دعدعت بها إذا دعوتها (sihah)؛ يقول الراعي للمعزى داع داع وهو زجر لها (tahdhib)
- **B004** tökezleyeni ayağa kalkmaya çağırma — tökezleyene söylenen 'kalk, toparlan' sözü
  قولك للعاثر دع دع (maqayis)؛ أن تقول للعاثر دع دع أي قم فانتعش (sihah;tahdhib)؛ أصله أن يقال للعاثر دع دع (mufradat)
- **B005** kıvrılarak yavaş koşma — kıvrıla kıvrıla yavaş koşma
  الدعدعة عدو في التواء (maqayis)؛ عدا عدوا فيه بطء والتواء (sihah)؛ عدو في التواء وبطء (tahdhib)
- **B006** kısa boylu adam — 
  دعداع فإن صح فهو من الإبدال من دحداح (maqayis)؛ الدعداع والدحداح الرجل القصير (tahdhib)
- **B007** iki hurma arasındaki açıklık veya seyrek hurmalar — 
  الدعاع ما بين النخلتين؛ الدعاع النخل المتفرق؛ رواه بعضهم في ذعاع النخل بالذال
- **B008** yazın su barındıran, sığırların yediği bitki — yazın su tutan ve sığırların yediği bir bitki
  الدعدع نبت يكون فيه ماء في الصيف يأكله البقر
- **B009** küçük çocuklar ve bakmakla yükümlü olunan küçükler — bir erkeğin küçük çocukları ve bakımına bağlı küçükler · bakımına bağlı küçüklerin sayısı çoğalmak
  الدعاع عيال الرجل الصغار؛ أدع الرجل إذا كثر دعاعه
- **B010** yabani bitki tohumu — yabani bir bitkinin tohumu · kuraklıkta yenen siyah tohum; ona benzeyen siyah karınca · bu tohumu ve başka bir yabani tohumu yemek için toplayan adam
  الدعاع حب شجرة برية؛ الدعاعة حبة سوداء؛ نملة سوداء تشاكل هذه الحبة؛ رجل دعاع فثاث

## ي ت م (root_001692) — identity root of ٱلْيَتِيمَ (w4)

- **B001** babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu olma — insanda babasız, hayvanda annesiz kalma · babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu · çocuk babasını yitirip babasız kaldı · Tanrı onu babasız bıraktı · çocukları babasız bıraktı · babasını yitirmiş çocuklar · babasını yitirmiş çocuklar · çocukları babasız kalmış kadın · çocukları babasız kalmış kadın · onları babasız bıraktı · çocukken kendisini yetiştiren kişiye nispetle, büyüdüğünde de babasını yitirmiş çocuk diye anılan kişi · babasını yitirmiş çocuklar topluluğu
  اليتم في الناس من قبل الأب وفي سائر الحيوان من جهة الأم (maqayis)؛ يتم الصبي إذا صار يتيما وأيتمه الله (jamhara)؛ أيتمت المرأة فهي موتم (jamhara;sihah)؛ يتمهم الله تيتيما (sihah)؛ اليتيم الذي مات أبوه حتى يبلغ (tahdhib)؛ انقطاع الصبي عن أبيه قبل بلوغه وفي سائر الحيوانات من قبل أمه (mufradat)
- **B002** tek kalmış ya da benzeri zor bulunan şey — tek başına veya eşi zor bulunan · tek başına duran veya benzeri olmayan şiir dizesi · tek ve eşi zor bulunan inci · tek başına duran kumluk veya dişil varlık
  لكل منفرد يتيم وبيت من الشعر يتيم (maqayis)؛ اليتيم الفرد (jamhara)؛ كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة (sihah)؛ الرملة المنفردة وكل منفرد ومنفردة يتيم ويتيمة (tahdhib)؛ كل منفرد يتيم ودرة يتيمة وبيت يتيم (mufradat)
- **B003** dalgınlık ve gerekeni eksik yapma — dalgınlık ve gerekeni eksik yapma · gidişinde dalgınlık veya eksik davranış yok
  اليتم الغفلة والتقصير وما في سيره يتم أي ما فيه غفلة ولا تقصير (jamhara)؛ أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره (tahdhib)
- **B004** yavaşlama veya gecikme — gidişinde yavaşlama var · yavaşlama ve gecikme
  في سيره يتم أي إبطاء (sihah)؛ اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه (tahdhib)
- **B005** evlilikle sona erip ermediği tartışmalı kadın adlandırması [kalıp] — evlenene dek, başka bir aktarıma göre ise evlendikten sonra da babasını yitirmiş çocuk adıyla anılan kadın · kadınların babasını yitirmiş çocuk adıyla anılabileceğini bildiren söz
  المرأة تدعى يتيما ما لم تتزوج فإذا تزوجت زال عنها اسم اليتم؛ يقال للمرأة يتيمة لا يزول عنها اسم اليتم أبدا (tahdhib)

## ECHO د ع و (root_000478) — for يَدُعُّ (w3): withheld observed target; not identity

- **B001** seslenerek kendine yöneltme — seslenmek; çağırmak · yemeğe çağırma · belirtilen yeri amaçlayıp oraya gitmek
  أصل واحد وهو أن تميل الشيء إليك بصوت وكلام يكون منك؛ دعوت أدعو دعاء؛ الدعوة إلى الطعام بالفتح؛ دعا فلانا مكان كذا إذا قصد ذلك المكان كأن المكان دعاه
- **B002** hak veya aidiyet ileri sürme — soy bağı ileri sürme · kendisi veya başkası adına hak iddia etme · savaşta soyunu söyleyerek kendini tanıtma · öz babasından başkasına bağlanan kişi
  الادعاء أن تدعي حقا لك أو لغيرك (maqayis)؛ الادعاء في الحرب الاعتزاء (maqayis)؛ الدعوة ادعاء الولد الدعي غير أبيه ويدعيه غير أبيه (ayn)؛ الدعوة في النسب بالكسر (maqayis)
- **B003** sütün devamını çekmek için memede bırakılan pay [kalıp] — sonraki sütü çekmek için memede bırakılan süt payı
  داعية اللبن ما يترك في الضرع ليدعو ما بعده
- **B004** Tanrı'nın birine istemediği bir sıkıntıyı vermesi [kalıp] — Tanrı'nın birinin başına hoşlanmadığı bir sıkıntıyı getirmesi
  دعا الله فلانا بما يكره أي أنزل به ذلك
- **B005** birbiri ardından çökme veya yıkma — duvarların birbiri ardından çökmesi · yapıları üzerlerine birbiri ardından yıkmak
  تداعت الحيطان وذلك إذا سقط واحد وآخر بعده؛ داعيناها عليهم إذا هدمناها واحدا بعد آخر
- **B006** dönemin olaylara yön veren değişimleri [kalıp] — dönemin değişimleri ve getirdiği olaylar
  دواعي الدهر صروفه كأنها تميل الحوادث
- **B007** gizli cevabı buldurmaya yönelik bilmeceleşme — gizli cevabı buldurmak için karşılıklı sorulan bilmeceler · sana bir bilmece sorayım
  لبنى فلان أدعية يتداعون بها وهي مثل الأغلوطة كأنه يدعو المسؤول إلى إخراج ما يعميه عليه
- **B008** evde hiç kimsenin bulunmaması — evde hiç kimse yok
  ما بالدار دَعْوِيّ أي ما بها أحد كأنه ليس بها صائح يدعو بصياحه

===== _commentary/v16/out/s107/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 107:2, and ## Buluşmalar) =====
## Yalan söyleyen kumaş ve yarıda kalan koşu

Birinci ayetin fiili {ar:يُكَذِّبُ, tr:yükezzibu, gloss:yalanlar, source:107:1}, doğruluğun karşıtı olan bir kökten gelir: {ar:الكذب خلاف الصدق, tr:el-kezibu hılâfu's-sıdk, gloss:yalan, doğruluğun karşıtıdır, source:"ك ذ ب,B001"}. Bu yalanın yalnız sözle sınırlı olmadığı da belirtilir: {ar:يقال في المقال والفعال, tr:yukâlu fi'l-makâli ve'l-fi‘âl, gloss:hem söz hem fiil için söylenir, source:"ك ذ ب,B001"}. Kök bunu bir eşyayla gösterir: {ar:الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله, tr:el-kezzâbetu sevbun yunkaşu bi-levni sıbġin ke-ennehû muvaşşâ, ve zâlike li-ennehû yekzibu bi-hâlih, gloss:"kezzâbe", boyayla desen basılan ve işlemeliymiş gibi görünen kumaştır; böyle denir çünkü hâliyle yalan söyler, source:"ك ذ ب,B009"}. Kumaşın işleyişi şöyledir: Desen ipliğin içine dokunmamış, yüzeye boyanmıştır. Göz orada ilmek okur, ama ilmek yoktur. Kumaş bir şey söylemez; yalanı kendi hâliyle söyler.

Aynı kök bir de yarıda kalan hareketleri adlandırır. Bunlar kalıplaşmış deyimlerdir ve bir başlangıcın verdiği sözü devamın tutmamasını anlatır. Hücum eden biri için {ar:حمل فلان ثم كذب أي لم يصدق في الحملة, tr:hamele fulânun summe kezebe, ey lem yasduk fi'l-hamle, gloss:filan saldırdı sonra "kezebe", yani hücumunda sadık kalmadı, source:"ك ذ ب,B004"} denir. Dişi deve için {ar:كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم, tr:kezebe lebenu'n-nâka izâ zunne en yedûme müdde fe-lem yedum, gloss:bir süre sürmesi beklenen deve sütü sürmeyince "sütü yalan söyledi" denir, source:"ك ذ ب,B006"} denir. Yabani hayvan için {ar:كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه, tr:kezebe'l-vahşiyyu izâ cerâ şavtan summe vekafe li-yanzura mâ verâeh, gloss:yabani hayvan bir koşu koşup ardına bakmak için durduğunda "kezebe" denir, source:"ك ذ ب,B007"} denir. Kökün karşı yüzü de aynı deyimlerdedir: {ar:حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف, tr:hamele fulânun alâ fulânin fe-mâ kezebe hattâ ta‘ane ev darabe, ey mâ vekaf, gloss:filan filana saldırdı ve mızrağı saplayana ya da vurana kadar durmadı, source:"ك ذ ب,B004"}; {ar:ما كذب فلان أن فعل كذا أي ما لبث, tr:mâ kezebe fulânun en fe‘ale kezâ, ey mâ lebis, gloss:filan şunu yapmakta gecikmedi, source:"ك ذ ب,B005"}. Surenin açılışındaki öteki kök, aynı hayvanın doğru söyleyen hâlini verir: {ar:أرأت الناقة إذا أظهرت الحمل حتى يرى صدق حملها, tr:er'eti'n-nâka izâ azhareti'l-hamle hattâ yurâ sıdku hamlihâ, gloss:dişi deve gebeliğini belli ettiğinde, gebeliğinin doğruluğu görülsün diye "er'et" denir, source:"ر ء ي,B010"}. Böylece birinci ayetin iki fiilinde birer dişi deve vardır. Birinin sütü yalan söyler, ötekinin karnı doğruyu gösterir.

Ayetin söylediği "dini yalanlayan"dır. Bu imge o anlamın yanında şunu duyurur: yalanlama yalnızca ağızdan çıkan bir cümle değildir. Yüzeyi içini, başlangıcı devamını tutmayan bir hayatın biçimidir. Sure bu adamla tartışmaz. Kumaştaki boya gibi, sütü kesilen deve gibi ortaya kendi hâliyle çıkan işlerini gösterir. İnkâr edilen şeyin kökü de bu boyanın tam karşılığını taşır: {ar:دينت الحالف أي نويته فيما حلف, tr:dayyentü'l-hâlif, ey neveytühû fîmâ halef, gloss:yemin edeni niyetine bıraktım, yani yemininde onu niyetine göre tuttum, source:"د ي ن,B007"}; {ar:دينت الرجل تديينا إذا وكلته إلى دينه, tr:dayyentü'r-racule tedyînen izâ vekeltehû ilâ dînih, gloss:adamı kendi dinine havale ettiğinde, source:"د ي ن,B007"}. Bu sözler bir insanın yüzeyine göre değil, içindeki niyete göre tutulmasını anlatır. Yalanlanan din, boyanın altına bakan hükümdür.

İkinci ayetin başındaki {ar:فَ, tr:fe, gloss:işte, demek ki, source:107:2} edatı itip kakmayı yalanlamanın sonucu ve görünür belgesi yapar. Dördüncü ve beşinci ayetlerde boyanın üzerine basıldığı desen ortaya çıkar. Kökün bir kolu namazı görünen parçalarıyla sayar: {ar:الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح, tr:es-salâtu mine'l-mahlûkîn el-kıyâmu ve'r-rükû‘u ve's-sücûdu ve'd-du‘âu ve't-tesbîh, gloss:yaratılmışlardan namaz; kıyam, rükû, secde, dua ve tesbihtir, source:"ص ل و,B003"}. Bu parçalar yerindedir. Ama ayet, namazda bir şeyi unutmaktan söz etmez. O durum ayrıca adlandırılır: {ar:سها الرجل في صلاته إذا غفل عن شيء منها, tr:sehe'r-racülu fî salâtihî izâ ġafele an şey'in minhâ, gloss:adam namazında bir parçasından gafil kaldığında "namazında yanıldı" denir, source:"س ه و,B001"}. Ayet ise şöyle der: {ar:عَن صَلَاتِهِمْ سَاهُونَ, tr:an salâtihim sâhûn, gloss:namazlarından gafildirler, source:107:5}. "An" edatı içeride değil, uzakta olmayı bildirir. Mü'minûn suresi içerideki hâli aynı kalıpla verir: {ar:ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ, tr:ellezîne hum fî salâtihim hâşi‘ûn, gloss:onlar ki namazlarında saygıyla eğilmişlerdir, source:23:2}. Bu surenin adamları namazı kılarken namazın dışındadır, tıpkı ipliğe girmemiş boya gibi. Altıncı ayet yüzeyin adını koyar: {ar:الرواء حسن المنظر, tr:er-ruvâu husnü'l-manzar, gloss:"ruvâ", güzel görünüştür, source:"ر ء ي,B006"}. Aynı ayet koşunun biçimini de verir: göz çekilince namaz bırakılır {source:"ر ء ي,B005"}. Yabani hayvanın durup ardına bakması gibi bu namaz da yolda durup seyirciye bakar. Yetimin kökü de bu yavaşlayan adımı bilir: {ar:في سيره يتم أي إبطاء, tr:fî seyrihî yutmun, ey ibtâ’, gloss:yürüyüşünde ağırlık, yani gecikme var, source:"ي ت م,B004"}.

Kuran yüzeyle altı arasındaki bu ayrılığı birkaç sahnede kurar. Bakara suresinde Allah mü'minlere sadakalarını başa kakarak ve incitmeyle boşa çıkarmamalarını söyler. Gösteriş için harcayanı bir kayaya benzetir: {ar:فَمَثَلُهُۥ كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا, tr:fe-meseluhû ke-meseli safvânin aleyhi turâbun fe-esâbehû vâbilun fe-terakehû saldâ, gloss:onun durumu, üstünde biraz toprak bulunan düz bir kayaya benzer; sağanak vurunca onu çıplak bırakır, source:2:264}. Toprak, tohumun tutacağı bir yer gibi görünür. Yağmur gelince altındaki taş ortaya çıkar. Münâfikûn suresinde Allah Peygamber'e münafıkların görünüşünü anlatır: {ar:وَإِذَا رَأَيْتَهُمْ تُعْجِبُكَ أَجْسَامُهُمْ, tr:ve izâ raeytehum tu‘cibuke ecsâmuhum, gloss:onları gördüğünde gövdeleri hoşuna gider, source:63:4}. Hemen ardından bu gövdeleri {ar:كَأَنَّهُمْ خُشُبٌۭ مُّسَنَّدَةٌۭ, tr:ke-ennehum huşubun musennede, gloss:sanki dayatılmış kütüklerdir, source:63:4} diye niteler. Kütükler ayakta durur, ama kendi içlerinden değil, arkalarındaki desteğe yaslanarak. Bakara suresi iyiliği görünen bir duruştan ayırarak başlar: {ar:لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ, tr:leyse'l-birra en tuvellû vucûhekum kıbele'l-meşrıkı ve'l-maġrib, gloss:iyilik yüzlerinizi doğuya ve batıya çevirmeniz değildir, source:2:177}. Sonra malı yetimlere ve yoksullara vermeyi, namazı ve zekâtı sayar ve bunları yapanları kökün karşıtıyla adlandırır: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟, tr:ülâike'llezîne sadakû, gloss:işte doğru olanlar onlardır, source:2:177}. Yarıda kalan verme Necm suresinde bir "gördün mü" ile gösterilir. Allah Peygamber'e sorar: {ar:أَفَرَءَيْتَ ٱلَّذِى تَوَلَّىٰ, tr:e-fe-raeyte'llezî tevellâ, gloss:yüz çevireni gördün mü, source:53:33}, {ar:وَأَعْطَىٰ قَلِيلًۭا وَأَكْدَىٰٓ, tr:ve a‘tâ kalîlen ve ekdâ, gloss:azıcık verdi, sonra kesti, source:53:34}. Yolunu tutan namaz ise Meâric suresinde iki kez adlandırılır: {ar:ٱلَّذِينَ هُمْ عَلَىٰ صَلَاتِهِمْ دَآئِمُونَ, tr:ellezîne hum alâ salâtihim dâimûn, gloss:onlar ki namazlarını sürdürürler, source:70:23}, {ar:وَٱلَّذِينَ هُمْ عَلَىٰ صَلَاتِهِمْ يُحَافِظُونَ, tr:ve'llezîne hum alâ salâtihim yuhâfizûn, gloss:onlar ki namazlarını korurlar, source:70:34}. Beyyine suresi boyasız kumaşı tarif eder: namaz ve zekât, dini yalnızca Allah'a ayırmanın içinde emredilmiştir: {ar:مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:muhlisîne lehu'd-dîn, gloss:dini yalnız O'na özgü kılarak, source:98:5}.

Kaynaklar: 107:1 يُكَذِّبُ ك ذ ب B001; 107:1 يُكَذِّبُ ك ذ ب B009; 107:1 يُكَذِّبُ ك ذ ب B004; 107:1 يُكَذِّبُ ك ذ ب B005; 107:1 يُكَذِّبُ ك ذ ب B006; 107:1 يُكَذِّبُ ك ذ ب B007; 107:1 أَرَءَيْتَ ر ء ي B010; 107:1 بِٱلدِّينِ د ي ن B007; 107:2 ٱلْيَتِيمَ ي ت م B004; 107:5 صَلَاتِهِمْ ص ل و B003; 107:5 سَاهُونَ س ه و B001; 107:6 يُرَآءُونَ ر ء ي B006; 107:6 يُرَآءُونَ ر ء ي B005

## Gözden kaçan: yetim, sönük yıldız, kalbi gitmiş namaz

Yetimin tanımı önce bir kopukluktur: {ar:انقطاع الصبي عن أبيه قبل بلوغه, tr:inkıtâ‘u's-sabiyyi an ebîhi kable bulûġih, gloss:çocuğun ergenliğe ermeden babasından kopması, source:"ي ت م,B001"}. Ama kökün bir açıklaması adı başkalarının bakışına bağlar: {ar:أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره, tr:aslu'l-yutmi'l-ġafle, ve bihî yusemme'l-yetîm, li-ennehû yuteġâfelu an birrih, gloss:yetimliğin aslı gaflettir; yetime bu yüzden yetim denir, çünkü ona iyilik yapmaktan gaflet edilir, source:"ي ت م,B003"}. Bu tanım bir başka biçimde de geçer: {ar:اليتم الغفلة والتقصير, tr:el-yutmu'l-ġafletu ve't-taksîr, gloss:yetimlik gaflet ve eksik bırakmaktır, source:"ي ت م,B003"}. Bir başka açıklama gecikmeyi öne çıkarır: {ar:اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه, tr:el-yutmu'l-ibtâ’, ve minhu uhize'l-yetîm, li-enne'l-birra yubtiu anh, gloss:yetimlik gecikmedir; yetim adı buradan alınmıştır, çünkü iyilik ona geç ulaşır, source:"ي ت م,B004"}. Kök bu yalnızlığa bir değer de verir: {ar:كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة, tr:küllü şey'in müfredin yeizzu nazîruhû fe-huve yetîm, ve durretun yetîme, gloss:benzeri az bulunan her tek şey yetimdir; tek inciye "yetim inci" denir, source:"ي ت م,B002"}. Beşinci ayetteki kelime ise başka bir köktendir, ama aynı sözle tanımlanır: {ar:السهو الغفلة عن الشيء وذهاب القلب عنه, tr:es-sehvu'l-ġafletu ani'ş-şey' ve zehâbu'l-kalbi anh, gloss:sehv, bir şeyden gaflet etmek ve kalbin ondan gitmesidir, source:"س ه و,B001"}. İki kök aynı değildir. Yalnızca bir tanımda, gaflette buluşurlar. Yetim başkalarının gafletiyle adını alır, beşinci ayettekiler ise gafletin kendisidir.

Bu ikinci kök, gözün atladığı şeyi gökyüzünden de verir: {ar:السها كويكب صغير, tr:es-suhâ kuveykebun saġîr, gloss:Suhâ küçük bir yıldızcıktır, source:"س ه و,B005"}; {ar:السها خفي جدا فيسهى عن رؤيته, tr:es-suhâ hafiyyun ciddâ fe-yushâ an ru'yetih, gloss:Suhâ pek gizlidir, onu görmekten gaflet edilir, source:"س ه و,B005"}. Sahnenin işleyişi buradadır: Göz parlak olana gider, sönük ve tek olanın üzerinden geçer. Sönük yıldız parlakların arasında kaybolur. Tek inci kabuğunda görülmez. Babası ölmüş çocuğu ise onu gözünün önünde tutacak kimse kalmamıştır. Kök iyi bir gözden kaçırmayı da tanır: {ar:المساهاة حسن المخالقة, tr:el-musâhâtu husnü'l-muhâlaka, gloss:"müsâhât", güzel geçinmektir, source:"س ه و,B003"}; {ar:كأن الإنسان يسهو عن زلة إن كانت من غيره, tr:ke-enne'l-insâne yeshû an zelletin in kânet min ġayrih, gloss:sanki insan, başkasından gelen bir sürçmeyi görmezden gelir, source:"س ه و,B003"}. Surenin adamları yanlış şeyi gözden kaçırır. Başkasının kusuruna değil, yetime ve kendi namazlarına karşı gaflettedirler.

İkinci ayette yetimin adı, ona karşı gösterilen gafleti zaten taşır. İtip kakmak bu gafletin ele dönüşmüş hâlidir. Üçüncü ayette yoksulun yemeği hiç anılmaz ve bu da gözden kaçan bir boşluktur. Beşinci ayette aynı gaflet bu kez yetime değil, adamların kendi namazlarına yönelir; kalp oradan da gitmiştir. Altıncı ayet ise tersini ekler: Her şeyi gözden kaçıranlar kendilerinin gözden kaçmasını istemez. Sönük yıldız gibi atlanmamak için parlamaya çalışırlar.

Zâriyât suresinde Allah yemin ettikten sonra tahminle konuşanları anlatırken aynı kalıbı kullanır: {ar:قُتِلَ ٱلْخَرَّٰصُونَ, tr:kutile'l-harrâsûn, gloss:kahrolsun tahminle konuşanlar, source:51:10}, {ar:ٱلَّذِينَ هُمْ فِى غَمْرَةٍۢ سَاهُونَ, tr:ellezîne hum fî ġamratin sâhûn, gloss:onlar ki bir gaflet seli içinde dalgındırlar, source:51:11}. "Ellezîne hum... sâhûn" yapısı aynıdır. Orada gaflet, insanı örten bir suyun içinde kalmaktır. Duhâ suresinde Allah Peygamber'e kendi yetimliğini hatırlatır ve yetimi görülen biri olarak anar: {ar:أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ, tr:elem yecidke yetîmen fe-âvâ, gloss:seni yetim bulup barındırmadı mı, source:93:6}. Bu bulunuşun karşılığı da bir emirdir: {ar:فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ, tr:fe-emme'l-yetîme fe-lâ takhar, gloss:yetimi ezme, source:93:9}. Tevbe suresinde Allah münafıkları anlatır. Burada unutma unutulmayla karşılanır, kapanan el de gafletin dışarıdan nasıl göründüğünü verir: {ar:وَيَقْبِضُونَ أَيْدِيَهُمْ ۚ نَسُوا۟ ٱللَّهَ فَنَسِيَهُمْ, tr:ve yakbidûne eydiyehum, nesu'llâhe fe-nesiyehum, gloss:ellerini sıkı tutarlar; Allah'ı unuttular, O da onları unuttu, source:9:67}.

Kaynaklar: 107:2 ٱلْيَتِيمَ ي ت م B001; 107:2 ٱلْيَتِيمَ ي ت م B003; 107:2 ٱلْيَتِيمَ ي ت م B004; 107:2 ٱلْيَتِيمَ ي ت م B002; 107:5 سَاهُونَ س ه و B001; 107:5 سَاهُونَ س ه و B005; 107:5 سَاهُونَ س ه و B003

## Zayıfın üstündeki eller: itmek, teşvik etmek, kaldırmak, önüne geçmek

İkinci ve üçüncü ayetler zayıfların bedenleri üzerinde bir dizi hareket kurar. İlki itmektir: {ar:يَدُعُّ, tr:yedu‘‘u, gloss:itip kakar, source:107:2}. Kök bu hareketi kabalığıyla birlikte tanımlar: {ar:الدفع الشديد, tr:ed-def‘u'ş-şedîd, gloss:sert itiş, source:"د ع ع,B001"}; {ar:دفع في جفوة, tr:def‘un fî cefve, gloss:kabalıkla itmek, source:"د ع ع,B001"}. Bu bir dürtme değildir. İten bedenin çocuğun bedenine çarpıp onu kapıdan uzaklaştırmasıdır. Aynı kök hayvan sürmeyi de adlandırır: {ar:الدعدعة زجر الغنم, tr:ed-da‘da‘atu zecru'l-ġanem, gloss:"da‘da‘a", koyunu bağırarak sürmektir, source:"د ع ع,B003"}. Yetim bir sürü gibi kovulur. Ama aynı ses yukarı doğru da çağırır: {ar:أن تقول للعاثر دع دع أي قم فانتعش, tr:en tekûle li'l-âsiri da‘ da‘, ey kum fe'nte‘iş, gloss:sürçüp düşene "da‘ da‘" demek, yani kalk ve kendine gel, source:"د ع ع,B004"}. Bir kök hem düşüren itişi hem kaldıran çağrıyı barındırır.

Üçüncü ayetin fiili ters yöndeki itiştir: {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ ta‘âmi'l-miskîn, gloss:yoksulun yemeğine teşvik etmez, source:107:3}. Kök bunu {ar:حض يحض حضا وهو الحث على الخير, tr:hadda yehuddu haddan, ve huve'l-hassu ale'l-hayr, gloss:"hadd", hayra doğru sürmektir, source:"ح ض ض,B001"} diye tanımlar. Karşılıklı biçimi de vardır: {ar:والمحاضة أن يحث كل واحد منهما صاحبه, tr:ve'l-muhâddatu en yehusse küllü vâhidin minhumâ sâhibeh, gloss:"muhâdda", ikisinden her birinin ötekini sürmesidir, source:"ح ض ض,B001"}. Aynı kök yeryüzünün en alt yerini de adlandırır: {ar:الحضيض قرار الأرض عند سفح الجبل, tr:el-hadîdu karâru'l-ardı inde safhi'l-cebel, gloss:"hadîd", dağ eteğinde yerin en dip noktasıdır, source:"ح ض ض,B002"}. Bu anlam fiilin anlamının yanında duyulur. Teşvik, en dipte yatana doğru yapılan bir itiştir.

Yoksulun kökü onu bu dipte, hareketsiz yatar hâlde gösterir: {ar:السكون ذهاب الحركة, tr:es-sükûnu zehâbu'l-hareke, gloss:sükûn, hareketin gitmesidir, source:"س ك ن,B001"}; {ar:المسكين الفقير وقد يكون بمعنى الذلة والضعف, tr:el-miskînu'l-fakîr, ve kad yekûnu bi-ma‘ne'z-zilleti ve'd-da‘f, gloss:miskin fakirdir; düşkünlük ve güçsüzlük anlamına da gelir, source:"س ك ن,B006"}; {ar:تمسكن إذا خضع لله وهي المسكنة للذلة, tr:temeskene izâ hada‘a li'llâh, ve hiye'l-meskenetu li'z-zille, gloss:Allah'a boyun eğdiğinde "temeskene" denir; meskenet düşkünlük içindir, source:"س ك ن,B006"}. Yoksul, ihtiyacın durdurduğu kişidir. Beşinci ayetin kelimesi de bu durgunlukla tanımlanır: {ar:السهو السكون, tr:es-sehvu's-sükûn, gloss:sehv durgunluktur, source:"س ه و,B002"}. Böylece sahnede iki durgunluk yan yana durur. Biri yerde yatan yoksulun bedeni, öteki namazda kıpırtısız kalmış kalptir. Yedinci ayet son hareketi ekler: {ar:وَيَمْنَعُونَ, tr:ve yemne‘ûne, gloss:ve engel olurlar, alıkoyarlar, source:107:7}. Kök bunu bir bedenin araya girmesi olarak tanımlar: {ar:المنع أن تحول بين الرجل وبين الشيء الذي يريده, tr:el-men‘u en tehûle beyne'r-racüli ve beyne'ş-şey'i'llezî yurîdüh, gloss:men‘, adamla istediği şeyin arasına girmektir, source:"م ن ع,B002"}. Aynı kök, araya girmenin iyi yüzünü de taşır: {ar:المنعة جمع مانع أي من يمنعه من عشيرته, tr:el-men‘atu cem‘u mâni‘, ey men yemne‘uhû min aşîretih, gloss:"men‘a", koruyucuların çoğuludur; yani soyundan onu koruyanlar, source:"م ن ع,B003"}; {ar:يحوطهم وينصرهم, tr:yehûtuhum ve yensuruhum, gloss:onları çepeçevre sarar ve onlara yardım eder, source:"م ن ع,B003"}. Babasını yitiren çocuk bu koruyucu halkayı da yitirmiştir. Onun halkası olabilecek adamlar ise aynı kökün fiilini, onunla istediği şey arasına girmek için kullanır.

Sahne surenin sırasıyla kurulur. İkinci ayetteki geniş zaman itmeyi bir alışkanlık olarak gösterir. Üçüncü ayet en küçük yükümlülüğü bile düşürür. Adam kendi elinden vermeyi bırakmak bir yana, başkasını doyurmaya yönelten tek bir söz de söylemez. Beşinci ayet durgunluğu namaz kılanın içine taşır. Yedinci ayet itilen yetimden sonra bir duvar diker.

Kuran itişi itenin üzerine çevirir. Tûr suresinde Allah hüküm gününü anlatır: {ar:يَوْمَ يُدَعُّونَ إِلَىٰ نَارِ جَهَنَّمَ دَعًّا, tr:yevme yuda‘‘ûne ilâ nâri cehenneme da‘‘â, gloss:cehennem ateşine itildikçe itilecekleri gün, source:52:13}. Ardından onlara {ar:هَٰذِهِ ٱلنَّارُ ٱلَّتِى كُنتُم بِهَا تُكَذِّبُونَ, tr:hâzihi'n-nâru'lletî kuntum bihâ tükezzibûn, gloss:işte yalanladığınız ateş budur, source:52:14} denir. Fecr suresinde Allah, rızkı daraltılınca Rabbi kendisini aşağıladı diyen insanı azarlar {source:89:16}. Azar, surenin çiftini çoğul ve karşılıklı biçimde verir: {ar:كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ, tr:kellâ bel lâ tükrimûne'l-yetîm, gloss:hayır, asıl siz yetime ikram etmiyorsunuz, source:89:17}, {ar:وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ tehâddûne alâ ta‘âmi'l-miskîn, gloss:yoksulun yemeği için birbirinizi teşvik etmiyorsunuz, source:89:18}. Duhâ suresi iki yasakla aynı elleri durdurur: {ar:فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ, tr:fe-emme'l-yetîme fe-lâ takhar, gloss:yetimi ezme, source:93:9}, {ar:وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ, tr:ve emme's-sâile fe-lâ tenhar, gloss:isteyeni azarlama, source:93:10}. Teşvikin tersine dönmüş hâli Nisâ suresindedir: {ar:ٱلَّذِينَ يَبْخَلُونَ وَيَأْمُرُونَ ٱلنَّاسَ بِٱلْبُخْلِ, tr:ellezîne yebhalûne ve ye'mürûne'n-nâse bi'l-buhl, gloss:cimrilik eden ve insanlara cimriliği emredenler, source:4:37}. Kalem suresindeki bahçe sahipleri ürünü sabah erkenden devşirmeye yemin eder {source:68:17}. Sonra fısıldaşarak yola çıkarlar: {ar:فَٱنطَلَقُوا۟ وَهُمْ يَتَخَٰفَتُونَ, tr:fe'ntalekû ve hum yetehâfetûn, gloss:fısıldaşarak yola koyuldular, source:68:23}. Fısıldaştıkları şey kapıya konan bir engeldir: {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌۭ, tr:en lâ yedhulenne'hâ'l-yevme aleykum miskîn, gloss:bugün oraya hiçbir yoksul yanınıza girmesin, source:68:24}. Karşılıklı teşvik burada yoksula karşı bir fısıltıya dönmüştür. Aynı surede Allah Peygamber'e boyun eğmemesi gereken kişiyi bu kökle niteler: {ar:مَّنَّاعٍۢ لِّلْخَيْرِ مُعْتَدٍ أَثِيمٍ, tr:mennâ‘in li'l-hayri mu‘tedin esîm, gloss:hayra hep engel olan, sınırı aşan, günahkâr, source:68:12}. Beled suresinde sarp yokuş {ar:فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ, tr:fe-le'ktehame'l-akabe, gloss:ama o sarp yokuşa atılmadı, source:90:11} ile açılır. Yokuşun içinde surenin iki zayıfı yere en yakın hâlleriyle durur: {ar:يَتِيمًۭا ذَا مَقْرَبَةٍ, tr:yetîmen zâ makrabe, gloss:yakınlığı olan bir yetim, source:90:15}, {ar:أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ, tr:ev miskînen zâ metrabe, gloss:ya da toprağa düşmüş bir yoksul, source:90:16}. Yokuş karşılıklı bir sürmeyle tamamlanır: {ar:وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ, tr:ve tevâsav bi'l-merhame, gloss:birbirlerine merhameti öğütlediler, source:90:17}.

Kaynaklar: 107:2 يَدُعُّ د ع ع B001; 107:2 يَدُعُّ د ع ع B003; 107:2 يَدُعُّ د ع ع B004; 107:3 يَحُضُّ ح ض ض B001; 107:3 يَحُضُّ ح ض ض B002; 107:3 ٱلْمِسْكِينِ س ك ن B001; 107:3 ٱلْمِسْكِينِ س ك ن B006; 107:5 سَاهُونَ س ه و B002; 107:7 وَيَمْنَعُونَ م ن ع B002; 107:7 وَيَمْنَعُونَ م ن ع B003

## Evin içi: küçükler, ev halkı, raftaki kaplar

Surenin altında bir ev durur. İtişi adlandıran kök bir adamın küçük çocuklarını da adlandırır: {ar:الدعاع عيال الرجل الصغار, tr:ed-di‘â‘u iyâlu'r-racüli's-sıġâr, gloss:"di‘â‘", adamın küçük çoluk çocuğudur, source:"د ع ع,B009"}; {ar:أدع الرجل إذا كثر دعاعه, tr:edea'r-racül izâ kesüra di‘â‘uh, gloss:adamın küçükleri çoğaldığında "edea" denir, source:"د ع ع,B009"}. Yetim, böyle bir evin bakıcısını yitirmiş çocuktur: {ar:اليتيم الذي مات أبوه حتى يبلغ, tr:el-yetîmu'llezî mâte ebûhu hattâ yebluġ, gloss:yetim, ergenliğe erinceye kadar babası ölmüş olandır, source:"ي ت م,B001"}. Yoksulun kökü oturulan evi, ev halkını ve evi ayakta tutan erzakı adlandırır: {ar:سكنت داري وأسكنتها غيرى, tr:sekentü dârî ve eskentuhâ ġayrî, gloss:evimde oturdum ve onu başkasına oturttum, source:"س ك ن,B002"}; {ar:السكن أهل الدار, tr:es-sekenu ehlu'd-dâr, gloss:"seken", evin halkıdır, source:"س ك ن,B003"}; {ar:قيل للقوت سكن لأن المكان به يسكن, tr:kîle li'l-kûti seken, li-enne'l-mekâne bihî yuskan, gloss:azığa "seken" denmiştir, çünkü bir yerde onunla oturulur, source:"س ك ن,B010"}. Beşinci ayetin kökü evin önünü ve eşya rafını verir: {ar:السهوة وهي كالصفة تكون أمام البيت, tr:es-sehve ve hiye ke's-suffe tekûnu emâme'l-beyt, gloss:"sehve", evin önündeki sundurma gibi bir yerdir, source:"س ه و,B004"}; {ar:السهوة أربعة أعواد أو ثلاثة يعارض بعضها على بعض يوضع عليها شيء من الأمتعة, tr:es-sehvetu erba‘atu a‘vâdin ev selâsetun yu‘âradu ba‘duhâ alâ ba‘d, yûda‘u aleyhâ şey'un mine'l-emti‘a, gloss:"sehve", birbirine çaprazlanmış üç dört sopadır, üstüne eşya konur, source:"س ه و,B004"}.

Yedinci ayetin kelimesi bu rafta duran şeylerin adıdır: {ar:ٱلْمَاعُونَ, tr:el-mâ‘ûn, gloss:gündelik yardım eşyası, ufak iyilik, source:107:7}. Kök onu tek tek sayar: {ar:ويقال هو أسقاط البيت نحو الفأس والقدر والدلو, tr:ve yukâlu huve eskâtu'l-beyt, nahve'l-fe'si ve'l-kıdri ve'd-delv, gloss:evin ufak tefek eşyası olduğu da söylenir: balta, tencere, kova gibi, source:"م ع ن,B005"}; {ar:الماعون اسم جامع لمنافع البيت, tr:el-mâ‘ûnu'smun câmi‘un li-menâfi‘i'l-beyt, gloss:mâûn, evin işe yarar şeylerinin toplu adıdır, source:"م ع ن,B005"}; {ar:كل ما يستعار من قدوم وسفرة وشفرة, tr:küllü mâ yusta‘âru min kadûmin ve sufratin ve şefra, gloss:keser, sofra bezi, bıçak gibi ödünç istenen her şey, source:"م ع ن,B005"}. Aynı kök evin kendisini de adlandırır: {ar:المعان المباءة والمنزل, tr:el-ma‘ânu'l-mebâetu ve'l-menzil, gloss:"me‘ân", konaklanan yer ve evdir, source:"م ع ن,B006"}. Bu eşyanın küçüklüğünü de söyler: {ar:المعن الشيء اليسير الهين, tr:el-ma‘nu'ş-şey'u'l-yesîru'l-heyyin, gloss:"ma‘n", az ve kolay şeydir, source:"م ع ن,B003"}. Bunlar komşunun kapıya gelip istediği şeylerdir: bir tencere, bir kova, bir bıçak. Verilince evden bir şey eksilmez, çoğu zaman geri de gelir. Onları esirgeyen el kökte adıyla anılır: {ar:رجل منوع ومناع إذا كان بخيلا ممسكا, tr:racülun menû‘un ve mennâ‘un izâ kâne bahîlen mümsikâ, gloss:cimri ve eli sıkı olan adama "menû‘" ve "mennâ‘" denir, source:"م ن ع,B001"}.

Bu evin kapları doldurmak içindir. İtişi adlandıran kök aynı zamanda bir ölçeği sarsarak doldurmayı da adlandırır: {ar:الدعدعة تحريك المكيال ليستوعب الشيء, tr:ed-da‘da‘atu tahrîku'l-mikyâli li-yesta‘ibe'ş-şey', gloss:"da‘da‘a", ölçeği sarsmaktır ki konan şey içine sığsın, source:"د ع ع,B002"}; {ar:دعدع مكيالا أو جوالقا حتى يكتنز, tr:da‘da‘a mikyâlen ev cuvâlikan hattâ yektenize, gloss:ölçeği ya da çuvalı iyice dolup sıkışıncaya kadar sarstı, source:"د ع ع,B002"}; {ar:دعدعت الشيء ملأته وجفنة مدعدعة, tr:da‘da‘tu'ş-şey'e mele'tühû, ve cefnetun müda‘da‘a, gloss:şeyi doldurdum; ağzına kadar dolu büyük tabak, source:"د ع ع,B002"}. İşleyiş şudur: Tahıl ölçeğe dökülür, ölçek sallanır, taneler yerleşir, açılan boşluğa daha fazlası girer. Tabak kenarına kadar dolar. Kabın içine giren de üçüncü ayetin kelimesidir: {ar:الطعم ذوقه والطعام اسم جامع لكل ما يؤكل, tr:et-ta‘mu zevkuhû ve't-ta‘âmu'smun câmi‘un li-külli mâ yü'kel, gloss:tat onun tadılmasıdır; yemek, yenen her şeyin toplu adıdır, source:"ط ع م,B001"}. Kök isteyeni ve vereni yan yana koyar: {ar:استطعمه سأله أن يطعمه وأطعمته الطعام, tr:istat‘amehû se'elehû en yut‘imeh, ve et‘amtühu't-ta‘âm, gloss:ondan yemek istedi, yani doyurmasını diledi; ona yemek yedirdim, source:"ط ع م,B002"}. Ev sahibini de adlandırır: {ar:رجل طاعم حسن الحال ومطعام كثير القرى, tr:racülun tâ‘imun hasenu'l-hâl, ve mit‘âmun kesîru'l-kırâ, gloss:"tâ‘im" hâli vakti yerinde adamdır; "mit‘âm" konuğunu çokça ağırlayandır, source:"ط ع م,B004"}. Mâûn bu kapları ödenmesi gereken bir iyilik olarak da sayar: {ar:الماعون المعروف كله والقصعة والقدر والفأس, tr:el-mâ‘ûnu'l-ma‘rûfu küllühû ve'l-kas‘atu ve'l-kıdru ve'l-fe's, gloss:mâûn bütün iyiliktir; çanak, tencere ve baltadır, source:"م ع ن,B005"}. Esirgemek ise vermenin tersidir: {ar:خلاف الإعطاء, tr:hılâfu'l-i‘tâ’, gloss:vermenin karşıtı, source:"م ن ع,B001"}.

Ayetler sırasıyla okununca evin kurulduğu görülür. İkinci ayette bir kök iki şey söyler. Duyulan anlam "iter"dir, ama aynı harfler küçük çocukları ve ağzına kadar sarsılarak doldurulan tabağı da adlandırır. Ölçeği sarsıp doldurabilecek el, babasız çocuğu kapıdan iter. Üçüncü ayette yemek ve yoksul gelir. Yoksulun kökü ev ve ev halkıdır. Evi ayakta tutan azık, evi olmayana ulaşmaz. Beşinci ayetin kökünde, kullanılmayan eşyanın üstünde durduğu raf duyulur. Yedinci ayet o raftaki şeylerin adını verir.

Kuran bu kapları doldurulmuş hâlde gösterir. İnsan suresinde Allah iyileri anlatır: {ar:وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا, tr:ve yut‘imûne't-ta‘âme alâ hubbihî miskînen ve yetîmen ve esîrâ, gloss:yemeği, kendileri ona düşkünken yoksula, yetime ve esire yedirirler, source:76:8}. Yâsîn suresinde kapların bir gerekçeyle reddedildiği görülür. Kâfirlere Allah'ın verdiği rızıktan harcamaları söylenince, inananlara şu cevabı verirler: {ar:أَنُطْعِمُ مَن لَّوْ يَشَآءُ ٱللَّهُ أَطْعَمَهُۥٓ, tr:e-nut‘imu men lev yeşâu'llâhu et‘ameh, gloss:Allah dileseydi doyuracağı kimseyi biz mi doyuracağız, source:36:47}. Kehf suresinde Mûsâ ile Allah'ın kullarından biri {ar:عَبْدًۭا مِّنْ عِبَادِنَآ, tr:abden min ibâdinâ, gloss:kullarımızdan bir kul, source:18:65} bir kasabaya varır: {ar:ٱسْتَطْعَمَآ أَهْلَهَآ فَأَبَوْا۟ أَن يُضَيِّفُوهُمَا, tr:istat‘amâ ehlehâ fe-ebev en yudayyifûhumâ, gloss:halkından yemek istediler, onlar ise ikisini konuk etmeye yanaşmadılar, source:18:77}. Kul, yıkılmak üzere olan bir duvarı ücretsiz doğrultur. Sonra sebebini açıklar: {ar:وَأَمَّا ٱلْجِدَارُ فَكَانَ لِغُلَٰمَيْنِ يَتِيمَيْنِ فِى ٱلْمَدِينَةِ وَكَانَ تَحْتَهُۥ كَنزٌۭ لَّهُمَا وَكَانَ أَبُوهُمَا صَٰلِحًۭا, tr:ve emme'l-cidâru fe-kâne li-ġulâmeyni yetîmeyni fi'l-medîne, ve kâne tahtehû kenzun lehumâ, ve kâne ebûhumâ sâlihâ, gloss:duvara gelince, şehirde iki yetim oğlanındı; altında onlara ait bir hazine vardı ve babaları iyi bir adamdı, source:18:82}. Kimseyi doyurmayan bir kasabada iki yetimin malı Allah tarafından saklanmıştır. Bu, surenin adamlarının kendi rafını sakladığı sahnenin tersidir. Yûsuf suresinde, kökün fiilinin bir ölçeğin üzerine düştüğü bir cümle vardır. Kardeşler babalarına dönüp şöyle der: {ar:يَٰٓأَبَانَا مُنِعَ مِنَّا ٱلْكَيْلُ, tr:yâ ebânâ müni‘a minne'l-keyl, gloss:babamız, ölçek bizden esirgendi, source:12:63}. Mutaffifîn suresi dolu ölçeğin karşıtını aynı beddua kelimesiyle anar: {ar:وَيْلٌۭ لِّلْمُطَفِّفِينَ, tr:veylun li'l-mutaffifîn, gloss:ölçüyü eksik tutanların vay hâline, source:83:1}. Bunlar {ar:ٱلَّذِينَ إِذَا ٱكْتَالُوا۟ عَلَى ٱلنَّاسِ يَسْتَوْفُونَ, tr:ellezîne izektâlû ale'n-nâsi yestevfûn, gloss:insanlardan ölçüp aldıklarında tam alanlar, source:83:2}, {ar:وَإِذَا كَالُوهُمْ أَو وَّزَنُوهُمْ يُخْسِرُونَ, tr:ve izâ kâlûhum ev vezenûhum yuhsirûn, gloss:onlara ölçüp tarttıklarında ise eksik verenlerdir, source:83:3}. Nisâ suresi mirasın bölüşüldüğü anda evin kapısını açık tutar. Bölüşüme yakınlar, yetimler ve yoksullar geldiğinde {ar:فَٱرْزُقُوهُم مِّنْهُ وَقُولُوا۟ لَهُمْ قَوْلًۭا مَّعْرُوفًۭا, tr:fe'rzukûhum minhu ve kûlû lehum kavlen ma‘rûfâ, gloss:ondan onlara da verin ve onlara güzel söz söyleyin, source:4:8} denir. Buradaki "ma‘rûf", mâûnun "bütün iyilik" diye açıklandığı kelimedir.

Kaynaklar: 107:2 يَدُعُّ د ع ع B009; 107:2 يَدُعُّ د ع ع B002; 107:2 ٱلْيَتِيمَ ي ت م B001; 107:3 طَعَامِ ط ع م B001; 107:3 طَعَامِ ط ع م B002; 107:3 طَعَامِ ط ع م B004; 107:3 ٱلْمِسْكِينِ س ك ن B002; 107:3 ٱلْمِسْكِينِ س ك ن B003; 107:3 ٱلْمِسْكِينِ س ك ن B010; 107:5 سَاهُونَ س ه و B004; 107:7 ٱلْمَاعُونَ م ع ن B005; 107:7 ٱلْمَاعُونَ م ع ن B006; 107:7 ٱلْمَاعُونَ م ع ن B003; 107:7 وَيَمْنَعُونَ م ن ع B001

## Buluşmalar

Görme imgesi ile gözden kaçma imgesi tek bir cümlede buluşur: Suhâ yıldızı {ar:خفي جدا فيسهى عن رؤيته, tr:hafiyyun ciddâ fe-yushâ an ru'yetih, gloss:pek gizlidir, onu görmekten gaflet edilir, source:"س ه و,B005"}. Surenin beşinci ayetindeki kökle altıncı ayetindeki kök bu cümlede yan yana durur. Gözden kaçırmak ile göze görünmek tek bir görme alanının iki ucudur. Adamlar sönük olanı, yani yetimi, yoksulu ve kendi namazlarındaki kalbi atlar. Kendilerinin ise atlanmamasını isterler. Alak suresindeki sahne bu buluşmaya namazı ve yarıda kalan yolu ekler. Bir "gördün mü" ile açılır, namaz kılan bir kulu engelleyeni gösterir, onun yalanlayıp yüz çevirdiğini söyler ve görenin Allah olduğunu hatırlatarak kapanır {source:96:9} {source:96:13} {source:96:14}. Burada bakış imgesi ile yalanın yüzey ve yol imgesi birbirinin içindedir. İnsanların gözü için kılınan namaz, gözü hiç ayrılmayan birinin önünde kılınmaktadır.

İtiş ile ateş Tûr suresinde tek harekette birleşir. Yetimi iten, ateşe itilir {source:52:13}, ve ona yalanladığı ateşin bu olduğu söylenir {source:52:14}. Böylece birinci ve ikinci ayetin iki fiili, yalanlamak ve itmek, dördüncü ayetin ateşini taşıyan kökle bir araya gelir. Hâkka suresinde ateş fiili ile teşvik etmeme aynı kişinin hesabında yan yana yazılır {source:69:31} {source:69:34}. Bu kez evin ocağı ile zayıfın üstündeki eller birbirine bağlanır. Teşvik edilmeyen yemek, pişirilmeyen ocağın karşılığında ateşe katlanmaya dönüşür.

Bütün imgeleri tek bir ağızdan dile getiren sahne Müddessir suresindedir. Cennet halkı suçlulara sorar: {ar:مَا سَلَكَكُمْ فِى سَقَرَ, tr:mâ selekekum fî sakar, gloss:sizi Sakar'a ne soktu, source:74:42}. Cevap bu surenin kelime dizisini ateşin içinden verir: {ar:قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ, tr:kâlû lem neku mine'l-musallîn, gloss:dediler ki: namaz kılanlardan değildik, source:74:43}, {ar:وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ, tr:ve lem neku nut‘imu'l-miskîn, gloss:yoksulu doyurmazdık, source:74:44}, {ar:وَكُنَّا نَخُوضُ مَعَ ٱلْخَآئِضِينَ, tr:ve künnâ nehûdu ma‘a'l-hâidîn, gloss:dalıp gidenlerle birlikte biz de dalardık, source:74:45}, {ar:وَكُنَّا نُكَذِّبُ بِيَوْمِ ٱلدِّينِ, tr:ve künnâ nükezzibu bi-yevmi'd-dîn, gloss:din gününü yalanlardık, source:74:46}. Namaz, doyurmak, gaflete dalmak ve hesabı yalanlamak burada tek bir itirafta toplanır ve bu itiraf ateşin içinden yapılır. Bu suredeki boş namaz, kapalı kap, gözden kaçırılan yoksul ve inkâr edilen hesap, orada bir hikâyenin sırası olarak geri döner.

Ev, su ve borç imgeleri tek bir kelimede, mâûnda buluşur. Aynı ad tencereyi ve kovayı {source:"م ع ن,B005"}, vadiden akan suyu {source:"م ع ن,B001"} ve itaatle zekâtı {source:"م ع ن,B005"} taşır. Rafta duran kap, yataktan akan su ve ödenmesi gereken pay tek bir şeyin üç görünüşüdür. Barındırma fiili de bu buluşmayı Kuran'da iki kez kurar. Yetim için {source:93:6}, Meryem oğlu ve annesi için kullanılır; ikincisinde barınak yerleşme ile akan suyun bir arada olduğu yerdir {source:23:50}. İtişin kökü de evle ellerin buluştuğu yerdir. Aynı harfler bir adamın küçük çocuklarını {source:"د ع ع,B009"}, sarsılarak doldurulan tabağı {source:"د ع ع,B002"} ve kapıdan kovan itişi {source:"د ع ع,B001"} taşır. Esirgemenin kökü de eli sıkı adamı {source:"م ن ع,B001"} ve babasız çocuğun yitirdiği koruyucu halkayı {source:"م ن ع,B003"} birlikte taşır.

Borç imgesi ile dışa dönük namaz imgesi Meâric suresinde birlikte sahnelenir. Esirgeyen insan, namazını sürdürenler, malındaki bilinen hak ve din gününü doğrulamak aynı dizide yer alır {source:70:21} {source:70:24} {source:70:26}. Tevbe suresindeki döngüde de pay, dua ve huzur birbirine bağlanır {source:9:103}. Bu sure, aynı halkaların çözülmüş hâlidir.

Surenin hareketi bu buluşmalarla taşınır. Sure bir bakış emriyle ve yalanlanan bir hesapla başlar. Bakışı önce bir evin kapısına götürür: Yetimi iten el, yoksulun yemeği için açılmayan ağız. Sonra namaz yerine geçer ve orada ateşi de taşıyan bir ada beddua düşer. Ardından seyircinin gözüne, en sonunda yeniden evin rafındaki küçük kaplara döner. Bir uçta "gördün mü" ile gösteriş vardır, yani bakış ve bakılmak. Öbür uçta din ile mâûn vardır, yani hesap ve küçük borç. İki uç da itaatte buluşur. Ortadaki ad, namaz kılanlar, hem halkayı kuracak ibadeti hem de halka kopunca gelen ateşi kökünde taşır.

