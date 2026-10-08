Surah: 92. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md and hft.md (both are earlier readers' proposals: ignore their judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S92 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

===== _commentary/v16/prompts/map3/surah_map.md (adapted) =====
Read the surah as one text and write its map of image chains: the lexical images that run through several of
its ayat and join them into one scene, process or movement. A later writer will read one ayah at a time, with
only that ayah's own dictionary. The map lets that writer hear what the ayah's words carry in the surah as a
whole, including senses whose evidence sits under the words of other ayat.

Your evidence is the surah text, the dictionary of every root in the surah (each branch with the classical
dictionaries' own phrases), earlier readers' channel review (channels.md) and activation hypotheses (hft.md),
and your own knowledge of Arabic and the Quran. Where a member or passage comes from memory rather than from
the dictionary or the text, say so. Do not delegate, browse or inspect files; run only the command the header describes.

The channel review and the HFT records are proposals by earlier readers. Ignore their judgements: grades,
strength or confidence labels, reading types, words such as "surprising", "exploratory" or "latent", and every
statement of what a reading may or may not do. Make your own judgement from the surah's words, the dictionary
phrases and the Quran. Do not rediscover what they already assembled: start from their chains, test each one
against the dictionary phrases and the text, and join, extend, split or correct them. Where their wording
abstracts a member, go back to the dictionary phrase and name what it actually says.

A chain belongs on the map when its members are senses the dictionary attests for words that stand in the surah,
and together they make one image or process that the surah's wording or sequence lets a listener hear. A member
need not be the sense that translates its word in its own ayah; a chain is heard across the surah, not in one
word. A chain may join a sense and its reversal as well as the parts of one scene. Mark a member attested only
inside a fixed expression [fixed expression]; add no other label to a member or a chain, and where a source
records a phrase and rejects it, say so of that phrase alone. When the dictionary itself joins two of the
surah's words in one phrase, quote that phrase: it is the strongest evidence a chain can have. Keep a scene at
the level of its objects, their parts and their operation. When proposals share members, do not fold one into
another's more abstract function unless nothing concrete is lost. Carry every chain that meets this test,
however unusual; leave out proposals that do not.

Write the map in English, with Arabic quoted exactly (surah wording from the text, dictionary phrases from the
dictionary). It is working material for the writer, not commentary prose.

1. `## Chains`. For each chain, a `###` heading naming the image. One paragraph on what the image is and how it
   moves through the surah. Then its members, one line each: the ayah ref, the word as it stands in the text,
   the root and branch id, the dictionary's own phrase quoted exactly, and what this member contributes to the
   image. Add Quran passages outside the surah, with exact refs, where they stage or confirm the chain; for
   each, name the speaker and the situation in a few words, and include the ayah that opens its scene when the
   passage continues one.
2. `## Interactions`. Where chains meet: a shared member, a dictionary phrase that joins members of two chains,
   a Quran passage that stages two chains together, or one chain's scene needing another's. One line each: the
   chains, where they meet, the evidence.
3. `## Ayat`. For each ayah in order: the chains its words take part in, what its words add to each, and in one
   line the whole scene each chain makes across the surah, so that a writer who sees only this ayah sees the
   scene, not a fragment.
4. `## Not carried`. Each channel subchannel and each HFT record you did not carry into a chain: one short line
   each, its name and why, no prose.

No ranking and no labels of strength or confidence. No list of what a writer must include. There is no length
target and no required number of chains or members.

===== _commentary/v16/work/s092/surah.r2.hftbundle/text.md =====
# Surah 92

- 92:1 وَٱلَّيْلِ إِذَا يَغْشَىٰ
- 92:2 وَٱلنَّهَارِ إِذَا تَجَلَّىٰ
- 92:3 وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ
- 92:4 إِنَّ سَعْيَكُمْ لَشَتَّىٰ
- 92:5 فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
- 92:6 وَصَدَّقَ بِٱلْحُسْنَىٰ
- 92:7 فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
- 92:8 وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
- 92:9 وَكَذَّبَ بِٱلْحُسْنَىٰ
- 92:10 فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- 92:11 وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
- 92:12 إِنَّ عَلَيْنَا لَلْهُدَىٰ
- 92:13 وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- 92:14 فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- 92:15 لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- 92:16 ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- 92:17 وَسَيُجَنَّبُهَا ٱلْأَتْقَى
- 92:18 ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- 92:19 وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- 92:20 إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- 92:21 وَلَسَوْفَ يَرْضَىٰ


===== _commentary/v16/work/s092/surah.r2.hftbundle/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ل ي ل (root_001392): 92:1 وَٱلَّيْلِ

- **B001** gündüzün karşıtı olan gece ve onun karanlığı — gündüzün karşıtı olan gece · gece karanlığı · tek bir gece · geceler · geceler · geceler · çok karanlık ve çetin gece · çok karanlık gece · uzun ya da şiddeti pekiştirilmiş gece · ayın en karanlık ve son gecesi
  الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)
- **B002** geceye girme ya da geceleyin iş görüp yol alma — geceye göre karşılıklı işlem yapma · geceye girmek · gece yol alan veya gece yolculuğuna dayanabilen kimse
  عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)
- **B003** bugüne göre belirlenen en yakın gece — bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece
  إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)
- **B004** bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı — bir kadın adı · şarap için kullanılan örtülü ad
  وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)

## غ ش و (root_001088): 92:1 يَغْشَىٰ

- **B001** örtme ve perdeleme — bir şeyin üstünü örtmek · örtü · gözü veya gönlü örten perde · göz perdesi · örtmek veya görüşü engellemek · giysisiyle örtünmek · giysisiyle örtünmek · eyer örtüsü
  أصل صحيح يدل على تغطية شيء بشيء (maqayis)؛ الغشاوة ما غشي القلب من رين الطبع (ayn)؛ الغشاء الغطاء وغشاوة أي غطاء وتغطيته واستغشى بثوبه (sihah)؛ الغشاوة ما غشي القلب من الطبع والغشاء الغطاء وغاشية السرج غطاؤه والرجل يستغشي ثوبه (tahdhib)؛ الغشاوة ما يغطى به الشيء واستغشوا ثيابهم (mufradat)
- **B002** her yanı saran büyük olay — dünyanın sonu ve hesap günü · herkesi kuşatan ağır karşılık veya bela · karnında ağır bir hastalığa tutuldu
  الغاشية القيامة لأنها تغشى الخلق بإفزاعها ورماه الله بغاشية وهو داء يأخذ كأنه يغشاه (maqayis)؛ الغاشية القيامة لأنها تغشى بإفزاعها ورماه الله بغاشية وهي داء يأخذ في الجوف (sihah)؛ غاشية من عذاب الله أي عقوبة مجللة تعمهم وغاشية اسم من أسماء القيامة وداء يأخذه في جوفه (tahdhib)؛ الغاشية كل ما يغطي الشيء ونائبة تغشاهم وتجللهم وكناية عن القيامة (mufradat)
- **B003** gelip uğrama — yanına gelmek · bir yere gelmek · bir kimsenin ziyaretçileri ve gelip gidenleri
  غشيه غشيانا أي جاءه (sihah)؛ الغاشية السؤال الذين يغشونك وغاشية الرجل من ينتابه من زواره وأصدقائه (tahdhib)؛ غشيت موضع كذا أتيته (mufradat)
- **B004** kadınla cinsel ilişkiyi dolaylı anlatma — kadınla birlikte olmak; cinsel ilişkiyi dolaylı anlatır · eşiyle birlikte olmak; cinsel ilişkiyi dolaylı anlatır
  الغشيان غشيان الرجل المرأة (maqayis)؛ غشيها غشيانا جامعها (sihah)؛ الغشيان كناية عن إتيان الرجل المرأة وتغشى امرأته (tahdhib)؛ غشيت موضع كذا أتيته وكني بذلك عن الجماع وغشاها وتغشاها (mufradat)
- **B005** bilincini yitirip bayılma — bilincini yitirip bayılmak · baygınlık; ölüm baygınlığı · baygın, bilinci kapalı
  غشي عليه غشية وغشيا وغشيانا فهو مغشي عليه (sihah)؛ غشي عليه فهو مغشي عليه وهي الغشية وكذلك غشية الموت (tahdhib)؛ غشي على فلان إذا نابه ما غشي فهمه (mufradat)
- **B006** kamçı veya kılıçla vurma — bir kimseye kamçıyla vurmak · üzerine kamçı veya kılıç darbesi indirmek
  غشيت الرجل بالسوط ضربته (sihah)؛ غشيته سوطا أو سيفا ككسوته وعممته (mufradat)
- **B007** hayvanın başını veya yüzünü kaplayan aklık — başı bütünüyle ak at · yüzü bütünüyle ak keçi · keçinin yüzünü kaplayan aklık
  الأعشى من الخيل وغيرها ما ابيض رأسه كله وعنزة غشواء بينة الغشا (sihah)؛ الغشواء من المعزى التي يغشى وجهها كله بياض (tahdhib)

## ECHO غ ش ي (root_001089): for 92:1 يَغْشَىٰ: withheld observed target; not identity

- **B001** örtüp kapatma ve örten şey — bir şeyin üstünü örtüp kapatmak · örtü; kaplayıcı tabaka · bir şeyi, gözü veya gönlü örten perde · görüşü kapatan perde · kılıcın ve yük semerinin örtüsü · eyer örtüsü · görmemek ve işitmemek için giysisine bürünmek · giysisine bürünmek · bir şeyi başka bir şeyin üstünü örter duruma getirmek · bir şeyi örten şey · üstten kaplayan örtüler
  يدل على تغطية شيء بشيء (maqayis)؛ الغشاء الغطاء (maqayis;sihah;tahdhib)؛ غاشية السيف والرحل غطاؤه (ayn)؛ غاشية السرج غطاؤه (tahdhib)؛ جعل على بصره غشوة وغشاوة أي غطاء (sihah)؛ يستغشي ثوبه كي لا يسمع ولا يرى (ayn;tahdhib)؛ الغشاوة ما يغطى به الشيء (mufradat)
- **B002** herkesi kuşatan son gün veya ağır yıkım — dünyanın son bulup herkesin yeniden diriltileceği gün · Tanrı'dan gelen, herkesi kuşatan ağır ceza
  الغاشية القيامة لأنها تغشى الخلق بإفزاعها (maqayis;sihah)؛ الغاشية القيامة (ayn)؛ الغاشية اسم من أسماء القيامة في القرآن (tahdhib)؛ غاشية من عذاب الله أي عقوبة مجللة تعمهم (tahdhib)؛ نائبة تغشاهم وتجللهم (mufradat)
- **B003** içini tutan hastalığa uğrama [kalıp] — kişinin içini tutan bir hastalığa uğraması
  رماه الله بغاشية وهو داء يأخذ كأنه يغشاه (maqayis)؛ رماه الله بغاشية وهي داء يأخذ في الجوف (sihah)؛ رماه الله بغاشية وهو داء يأخذه في جوفه (tahdhib)
- **B004** kadınla cinsel birleşmeyi örtmeceli anlatma — erkeğin kadınla cinsel birleşmesi · kadınla cinsel birleşmeye girmek · karısıyla cinsel birleşmeye girmek
  الغشيان غشيان الرجل المرأة (maqayis)؛ الغشيان إتيان الرجل المرأة (ayn)؛ غشيها غشيانا جامعها (sihah)؛ الغشيان كناية عن إتيان الرجل المرأة (tahdhib)؛ كني بذلك عن الجماع يقال غشاها وتغشاها (mufradat)
- **B005** birine veya bir yere gelme ve gelip gidenler — yanına gelmek · bir yere gelmek · iyilik umarak gelenler ve ziyaretçiler · bir kişinin ziyaretçileri ve dostları
  الغاشية الذين يغشونك يرجون فضلك (ayn)؛ غشيه غشيانا أي جاءه (sihah)؛ الغاشية السؤال الذين يغشونك يرجون فضلك ومعروفك (tahdhib)؛ غاشية الرجل من ينتابه من زواره وأصدقائه (tahdhib)؛ غشيت موضع كذا أتيته (mufradat)
- **B006** kırbaç veya kılıçla vurma [kalıp] — adama kırbaçla vurmak
  غشيت الرجل بالسوط ضربته (sihah)؛ غشيته سوطا أو سيفا ككسوته وعممته (mufradat)
- **B007** kavrayışı kapanıp bayılma — bilinci kapanıp bayılmak · baygınlık · baygın; bilinci kapalı · ölümü andıran baygınlık
  غشي عليه غشية وغشيا وغشيانا فهو مغشي عليه (sihah)؛ غشي عليه فهو مغشي عليه وهي الغشية وكذلك غشية الموت (tahdhib)؛ غشي على فلان إذا نابه ما غشي فهمه (mufradat)
- **B008** hayvanın yüzünü veya başını kaplayan beyazlık — yüzü bütünüyle beyaz keçi · başı bütünüyle beyaz, gövdesi başka renkte hayvan
  الأعشى من الخيل وغيرها ما ابيض رأسه كله من بين جسده (sihah)؛ عنز غشواء بينة الغشا (sihah)؛ الغشواء من المعزى التي يغشى وجهها كله بياض (tahdhib)

## ن ه ر (root_001559): 92:2 وَٱلنَّهَارِ

- **B001** bol su taşıyan doğal akarsu yatağı — taşkın suyun aktığı doğal akarsu yatağı · akarsu yatakları · akarsular veya akarsu yatakları · akarsu yatağı sağlam bir güzergah edindi · su aktı ve kendine bir yatak açtı · bol sulu veya geniş akarsu · suyun kazıp açtığı yatak yeri · kuyu kazısı suya ulaştı
  النهر مجرى الماء الفائض (mufradat)؛ النهر واحد الأنهار وجمعه أنهار ونهر (ayn;sihah;tahdhib;maqayis)؛ سمي النهر لأنه ينهر الأرض أي يشقها (maqayis)؛ استنهر النهر أخذ مجراه (ayn;tahdhib;maqayis)؛ نهر الماء أو أنهر الماء جرى (sihah;tahdhib;maqayis)؛ نهر نهر كثير الماء (sihah;tahdhib;maqayis;mufradat)؛ حفرت البئر حتى نهرت أي بلغت الماء (tahdhib)
- **B002** şafaktan gün batımına aydınlık gündüz — şafaktan güneş batımına kadar süren aydınlık gündüz · aydınlık gündüz süreleri · gündüz vaktinde baskın yapan kimse · gündüzün aydınlığına girdik
  النهار ضياء ما بين طلوع الفجر إلى غروب الشمس (ayn;tahdhib;maqayis)؛ النهار ضد الليل (sihah)؛ الوقت الذي ينتشر فيه الضوء (mufradat)؛ النهار اسم لكل يوم (tahdhib)؛ النهار يجمع على نهر (sihah;tahdhib;maqayis)؛ رجل نهر صاحب نهار (ayn;sihah;tahdhib;maqayis;mufradat)
- **B003** bir şeyi açma veya genişletme — genişlik veya aydınlıkla birlikte genişlik · kanı açıp serbest bırakarak akıttı · yaranın veya yarığın açıklığını genişletti · genişledi · evlerin önleri arasında atık bırakılan açık alan · bağırsağı çözüldü ve akarsu gibi boşaldı · tehlikeler; birleşik bir türetme olarak açıklanan biçim
  أصل صحيح يدل على تفتح شيء أو فتحه (maqayis)؛ أنهرت الدم فتحته وأرسلته (maqayis)؛ أنهرت الدم أي أسلته (sihah;mufradat)؛ أنهرت الطعنة وسعتها وأنهر فتقها (sihah;tahdhib)؛ نهر من نهر الفتق (maqayis)؛ استنهر الشيء اتسع (sihah)؛ المنهرة فضاء يكون بين أفنية القوم (maqayis;sihah;mufradat)؛ أنهر بطنه إذا جاء بطنه مثل مجيء النهر (tahdhib)؛ النهر السعة تشبيها بنهر الماء وفي ضياء وسعة (mufradat;sihah;tahdhib)
- **B004** sert sözle azarlayıp engelleme [kalıp] — onu sert sözle azarlayıp engelledi
  نهرت الرجل نهرا وانتهرته انتهارا زجرته بكلام عن شر (ayn)؛ نهره وانتهره أي زبره (sihah)؛ نهرته وانتهرته إذا استقبلته بكلام تزجره (tahdhib)؛ النهر والانتهار الزجر بمغالظة (mufradat)
- **B005** bazı kuşların yavrusu — türü aktarıma göre değişen bir kuş yavrusu
  النهار فرخ القطا والغطاط والعقاب ونحوه وثلاثة أنهرة (ayn)؛ النهار فرخ الحبارى (sihah;tahdhib;mufradat)؛ النهار فرخ بعض الطير مما لا يعرج على مثله ولا معنى له (maqayis)
- **B006** fırsat kollayıp gizlice kapma — fırsat kollayıp ani biçimde gizlice kapma
  النهر الدغرة وهي الخلسة (tahdhib)
- **B007** kişi, yer ve yıldızlara ait özel adlar — belirli bir topluluktan bir şairin adı · bir yer adı · sularının bolluğu nedeniyle iki yıldız için kullanılan ortak ad
  نهار بن توسعة اسم شاعر من تميم (sihah)؛ نهروان بلد (sihah)؛ العرب تسمي العواء والسماك الأنهرين لكثرة مائهما (tahdhib)
- **B008** bulut — bulut
  الناهُور السحاب (tahdhib)

## ج ل و (root_000256): 92:2 تَجَلَّىٰ

- **B001** örtülünün açığa çıkması veya çıkarılması — örtülü şeyi açığa çıkarmak · açık, belirgin; açık kanıt · haber benim için açıklığa kavuştu · hastalığı gidermek veya kaygıyı dağıtmak · ortaya çıkmak, görünür olmak · örtücü durum dağılıp açılmak · birbirimizin hali karşılıklı olarak ortaya çıktı · sarığı alından katlayarak kaldırmak
  انكشاف الشيء وبروزه (maqayis)؛ أمر جلي واضح وأجل لنا هذا الأمر أي أوضحه وجلا الله عنك المرض (ayn)؛ الجلي نقيض الخفي وجلا لي الخبر وجلوت أي أوضحت وكشفت وانجلى عنه الهم وتجالينا (sihah)؛ أصل الجلو الكشف الظاهر والتجلي قد يكون بالذات وبالأمر والفعل (mufradat)
- **B002** kılıcı parlatma ve göz boyasıyla görüşü berraklaştırma — kılıcı parlatıp temizlemek · görüşü berraklaştırdığı kabul edilen göz boyası · görüşü göz boyasıyla berraklaştırmak
  جلوت السيف جلاء (maqayis;mufradat)؛ جلا الصيقل السيف واجتلاه (ayn;tahdhib)؛ الجلا مقصور الإثمد لأنه يجلو البصر (ayn)؛ جلوت بصري بالكحل والجلا كحل (sihah;tahdhib)
- **B003** gelini törende gösterme veya gösterilmiş gelini görme [kalıp] — gelini düğünde görünür biçimde sunmak · sunulmuş gelini görmek
  جلوت العروس جلوة وجلاء (maqayis;mufradat)؛ الماشطة تجلو العروس وقد جليت على زوجها واجتلاها زوجها أي نظر إليها (ayn;tahdhib)؛ جلوت العروس جلاء وجلوة واجتليتها إذا نظرت إليها مجلوة (sihah)
- **B004** yerleşimden ayrılma veya çıkarılma — yurttan veya yerleşimden ayrılma · onları ülkeden çıkarmak · yurdundan ayrılmış topluluk; yönetim korumasında özel vergi ödeyen topluluk · çevresinde toplanılan şeyin yanından açılıp dağılmak
  جلا القوم عن منازلهم جلاء وأجليتهم (maqayis)؛ الجلاء أن يجلو قوم عن بلادهم والجالية أهل الذمة (ayn)؛ الجلاء الخروج من البلد والجالية الذين جلوا عن أوطانهم (sihah)؛ أجليت القوم عن منازلهم فجلوا عنها أي أبرزتهم عنها (mufradat)
- **B005** ön saç çizgisinin gerilemesi — ön saçları çekilmiş kişi; ön saçların çekilmesi · geniş ve güzel alın · başın ön kısımları ve saçsız bölgeleri
  رجل أجلى إذا ذهب شعر مقدم رأسه وهو الجلا (maqayis)؛ الجبهة الجلواء والرجل أجلى (ayn)؛ انحسار مقدم الرأس (jamhara)؛ الجلاء انحسار الشعر عن مقدم الرأس والمجالي مقادم الرأس (sihah)؛ فهو أجلى مع الجلا (tahdhib)؛ رجل أجلى انكشف بعض رأسه عن الشعر (mufradat)
- **B006** adı ve konumu herkesçe bilinen kişi [kalıp] — herkesçe tanınan, durumu gizli olmayan kişi
  هو ابن جلا إذا كان لا يخفى أمره لشهرته (maqayis)؛ أنا ابن جلا أي أنا ابن الواضح الأمر المشهور (ayn)؛ الجلا الأمر الواضح المكشوف وأنا ابن جلا (jamhara)؛ كأنه يقال له جلا الأمور وكشفها (sihah)؛ هو ابن جلا للرجل إذا كان عالي الشرف لا يخفى مكانه (tahdhib)؛ فلان ابن جلا أي مشهور (mufradat)
- **B007** açık gök ve aydınlanan gündüz — bulutsuz, açık gök · bir gündüzlük aydınlık süre · gündüzün güneşi belirginleştirmesi
  السماء جلواء أي مصحية (maqayis;sihah;mufradat)؛ جلاء يوم واحد أي بياض يوم (ayn;tahdhib)؛ والنهار إذا جلاها إذا بين الشمس (tahdhib)
- **B008** başı kaldırıp bakışı hedefe yöneltme — başı ve gözleri kaldırıp bakışı ava yöneltmek · bir şeye gözeterek ve beklentiyle bakmak
  البازي يجلي إذا آنس الصيد فرفع طرفه ورأسه وتجليت الشيء نظرت إليه (ayn)؛ جلى ببصره تجلية إذا رمى به كما ينظر الصقر إلى الصيد (sihah)؛ التجلي النظر بالأشراف (tahdhib)
- **B009** gelin gösteriminde verilen armağan [kalıp] — eşinin gelin gösterimi sırasında ona bir hizmetçi armağan etmesi
  جلاها زوجها وصيفا أي أعطاها وما جلوتها بالكسر (sihah)؛ جلى فلان امرأته وصيفا حين اجتلاها أي أعطاها وصيفا عند جلوتها وما جلوتها بالكسر (tahdhib)

## خ ل ق (root_000434): 92:3 خَلَقَ

- **B001** ölçüp sınırlarını belirleme — ölçüp sınırlarını belirlemek · ölçüp biçme
  أحدهما تقدير الشيء؛ خلقت الأديم للسقاء إذا قدرته (maqayis)؛ خلقت الأديم قدرته (ayn)؛ خلقت الشيء إذا قدرته (jamhara)؛ الخلق: التقدير؛ خلقت الأديم إذا قدرته قبل القطع (sihah)؛ الخلق في كلام العرب على ضربين... والآخر التقدير؛ خلقت الأديم إذا قدرته وقسته (tahdhib)؛ الخلق أصله: التقدير المستقيم (mufradat)
- **B002** var etme ve ortaya çıkarma — yaratmak, var etmek · yaratan, var eden · yaratan, var eden; özellikle Tanrı için kullanılan ad · yaratılanlar, insanlar · yaratılmış varlık ya da varlıklar topluluğu
  الخالق الصانع (ayn)؛ الخلق مصدر خلق الله الخلق يخلقهم خلقا (jamhara)؛ هم خليقة الله (sihah)؛ الخالق والخلاق؛ الخلق ابتداع الشيء على مثال لم يسبق إليه (tahdhib)؛ يستعمل في إبداع الشيء من غير أصل ولا احتذاء؛ ويستعمل في إيجاد الشيء من الشيء (mufradat)
- **B003** tam ve dengeli dış biçim — dış görünüş ve beden yapısı · beden yapısı tam ve dengeli · yapısı tamamlanmış ve ölçülü · biçimi belirmiş ve oluşumu tamamlanmış
  رجل مختلق تام الخلق؛ المختلق من كل شيء ما اعتدل (maqayis)؛ رجل خليق أي تم خلقه؛ المختلق من كل شيء ما اعتدل (ayn)؛ رجل خليق ومختلق أي تام الخلق معتدل؛ مضغة مخلقة أي تامة الخلق (sihah)؛ رجل خليق إذا تم خلقه؛ مخلقة قد بدا خلقها وغير مخلقة لم تصور (tahdhib)؛ خص الخلق بالهيئات والأشكال والصور المدركة بالبصر (mufradat)
- **B004** huy ve iç karakter — huy, iç karakter · doğal huy ve yaradılıştan eğilim · iyi huyluluk ve iyi geçim · insanlarla huyuna göre geçinmek · bir huyu edinmeye veya öyle görünmeye çalışmak
  الخلق وهي السجية (maqayis)؛ الخليقة الخلق والخليقة الطبيعة (ayn)؛ الخلق: خلق الإنسان الذي طبع عليه؛ حسن الخلق؛ كريم الخليقة (jamhara)؛ الخليقة: الطبيعة؛ الخلقة: الفطرة؛ الخلق والخلق: السجية (sihah)؛ الطبيعة والخليقة والسليقة بمعنى واحد؛ خالق الناس بخلق حسن أي عاشرهم؛ الخلق الدين؛ الخلق المروءة (tahdhib)؛ خص الخلق بالقوى والسجايا المدركة بالبصيرة (mufradat)
- **B005** bir şeye yaraşır ve uygun olma — yaraşır, uygun · bunu yapması ne kadar beklenir · iyiliğe veya o işe çok uygun
  فلان خليق بكذا وأخلق به؛ هو ممن يقدر فيه ذلك (maqayis)؛ مخلقة للخير أي جدير به؛ خليق له أي جدير به؛ ما أخلقه أي ما أشبهه (ayn)؛ فلان خليق بكذا أي جدير به؛ مخلقة لذلك أي مجدرة له (sihah)؛ خليق بذاك أي حري؛ أخلق به أن يفعل؛ مخلقة للخير (tahdhib)؛ فلان خليق بكذا أي كأنه مخلوق فيه ذلك (mufradat)
- **B006** iyilikten düşen pay — pay, özellikle iyilikten düşen pay · iyilikten veya öte dünyadaki karşılıktan payı yok
  الخلاق النصيب لأنه قد قدر لكل أحد نصيبه (maqayis)؛ الخلاق النصيب من الحظ الصالح؛ ليس له خلاق أي ليس له رغبة في الخير ولا في الآخرة (ayn)؛ لا خلاق له أي لا نصيب له في الخير؛ الخلاق النصيب (jamhara)؛ الخلاق: النصيب؛ لا خلاق له في الآخرة (sihah)؛ الخلاق النصيب من الحظ الصالح؛ النصيب من الخير؛ الخلاق الدين (tahdhib)؛ الخلاق ما اكتسبه الإنسان من الفضيلة بخلقه (mufradat)
- **B007** uydurup yalan üretme — söz uydurmak ve çarpıtmak · zihninde yalan kurup ortaya atmak · yanlış kişiye bağlanmış, uydurma · uydurma öyküler ve asılsız anlatılar
  الخلق خلق الكذب وهو اختلاقه واختراعه وتقديره في النفس؛ وتخلقون إفكا (maqayis)؛ الخلق الكذب (ayn)؛ اختلق فلان كلاما إذا زوره؛ وتخلقون إفكا (jamhara)؛ خلق الإفك واختلقه وتخلقه أي افتراه؛ قصيدة مخلوقة أي منحولة (sihah)؛ تقدرون كذبا؛ أحاديث الخلق وهي الخرافات من الأحاديث المفتعلة؛ اختلاق (tahdhib)؛ كل موضع استعمل الخلق في وصف الكلام فالمراد به الكذب؛ إن هذا إلا اختلاق (mufradat)
- **B008** engebesiz ve düz olma — yüzeyini düzeltmek ve pürüzsüzleştirmek · engebesiz, düz ve yoğun · düz ve engebesiz kaya · alnın veya gözler arasının düz bölümü · yayılıp düzleşmek · düzeltilmiş ve yüzeyi engebesiz
  الأصل الثاني ملاسة الشيء؛ صخرة خلقاء أي ملساء؛ اخلولق السحاب استوى؛ رسم مخلولق إذا استوى بالأرض؛ السهم المصلح مخلق لأنه يصير أملس (maqayis)؛ الأخلق الأملس؛ صخرة خلقاء أي مصمتة؛ خليقاء الجبهة مستواها؛ خليقاء الغار الأعلى باطنه؛ اخلولق السحاب أي استوى (ayn)؛ خلقت الحبل والوتر وغيرهما تخليقا إذا ملسته؛ صخرة خلقاء ملساء؛ جبل أخلق؛ ضربه على خلقاء متنه (jamhara)؛ الأخلق الأملس المصمت؛ المخلق القدح إذا لين؛ صخرة خلقاء؛ اخلولق السحاب؛ اخلولق الرسم أي استوى بالأرض (sihah)؛ الأخلق الأملس من كل شيء؛ خليقاء الجبهة مستواها؛ خلقاء الغار الأعلى؛ سهم مخلق أملس مستو؛ الخلقة السحابة المستوية (tahdhib)
- **B009** kullanımdan yıpranıp eskime — kullanımdan yıpranıp tüyünü yitirmek · eski ve yıpranmış giysi · her yanı yıpranmış veya parçalanmış giysi · birine eski ve yıpranmış bir giysi vermek · istemekten yüzünü eskitmek
  أخلق الشيء وخلق إذا بلي؛ إذا أخلق املاس وذهب زئبره؛ ثوب خلق (maqayis)؛ خلق الثوب يخلق خلوقة أي بلي؛ أخلقني فلان ثوبه؛ ثوب أخلاق ممزق من جوانبه (ayn)؛ أخلق الثوب إخلاقا وخلق خلوقة وخلوقا فهو خلق؛ ثوب أخلاق (jamhara)؛ ملحفة خلق وثوب خلق أي بال؛ خلق الثوب أي بلى؛ أخلقته ثوبا إذا كسوته ثوبا خلقا؛ ثوب أخلاق (sihah)؛ خلق الثوب يخلق خلوقة وأخلق إخلاقا؛ أخلق فلان فلانا أي أعطاه ثوبا خلقا؛ ثوب أخلاق؛ جبة خلق (tahdhib)
- **B010** sürülen hoş koku karışımı — sürülen hoş koku karışımı · hoş koku karışımı sürmek veya sürünmek
  الخلوق معروف وهو الخلاق أيضا (maqayis)؛ الخلوق من الطيب؛ فعله التخليق والتخلق (ayn)؛ الخلوق ضرب من الطيب؛ خلقته أي طليته بالخلوق فتخلق به (sihah)؛ الخلوق من الطيب معروف؛ تخلقت المرأة بالخلوق وخلقت غيرها؛ خلق المسجد بالخلوق (tahdhib)
- **B011** su tutan kaya oyuğu veya yeni kuyu — su tutan kaya oyuğu veya yeni kuyu · yeni kazılmış kuyular
  الخلائق نقر في الصفا (ayn)؛ الخليقة نقر في صخرة يجتمع فيه ماء السماء (jamhara)؛ قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها تسميها العرب الخلائق؛ دحلان خلقها الله في بطون الأرض؛ الخليقة البئر ساعة تحفر؛ الخلق الآبار الحديثات الحفر (tahdhib)
- **B012** kapalı üreme yolu — üreme yolu kapalı kadın
  امرأة خلقاء رتقاء لأنها مصمتة كالصفاة الخلقاء (ayn)؛ الخلق: المرأة الرتقاء (jamhara)؛ قيل للمرأة الرتقاء: خلقاء (sihah)؛ يقال للمرأة الرتقاء: خلقاء لأنها مصمتة كالصفاة الخلقاء (tahdhib)

## ذ ك ر (root_000516): 92:3 ٱلذَّكَرَ

- **B001** erkek cinsiyet ve erkek yavru doğurma — erkek · erkek üreme organı · erkeğin üreme organı çevresindeki organlar · erkekler veya erkeklik · erkek yavru doğurdu · çoğunlukla erkek yavru doğuran dişi · erkek yapılı kadın veya dişi deve · gebe için kolay doğum ve erkek çocuk dileği
  الذكر خلاف الأنثى (sihah;tahdhib;mufradat)؛ الذكورة والذكور والذكران جمع الذكر (ayn;tahdhib;mufradat)؛ أذكرت ولدت ذكرا والمذكار تلد الذكور (maqayis;ayn;sihah;tahdhib;mufradat)
- **B002** sert, keskin ve güçlü olma — demirin en sert ve kuru türü · keskin ve sağlam kılıç · kılıcın veya erkeğin keskinliği · kalın ve sert otlar · güçlü, yiğit ve onurlu adam · çetin ve korkutucu gün, yol veya felaket · şiddetli yağmur, sağlam söz veya güçlü şiir · tehlikeli, yalnız erkeklerin geçtiği veya sert ot bitiren ıssız ova
  سيف مذكر ذو ماء وذو ذكر صارم (maqayis;sihah;mufradat)؛ الذكر من الحديد أيبسه وأشده (ayn;sihah;tahdhib)؛ ذكور البقل ما غلظ منه (maqayis;sihah;tahdhib;mufradat)؛ رجل ذكر قوي شجاع ويوم وطريق وداهية ومطر ذكر للشدة (tahdhib)
- **B003** akılda tutma ve yeniden hatırlama — hatırladı veya aklında tuttu · aklında · hatırlama · ezberlemek için çalışma · belleği güçlü, yiğit veya iyi anılan adam
  ذكرت الشيء خلاف نسيته (maqayis;sihah)؛ الذكر الحفظ للشيء وهو مني على ذكر (ayn;tahdhib)؛ ذكر بالقلب والتذكر طلب ما فات (ayn;tahdhib;mufradat)
- **B004** bir şeyi sözle anma [kalıp] — sözle anma · insanların arkasından kusurlarını söyleme
  ثم حمل عليه الذكر باللسان (maqayis)؛ الذكر جري الشيء على لسانك (ayn;tahdhib)؛ ذكرته بلساني وبقلبي (sihah)؛ كل قول يقال له ذكر وذكر باللسان (mufradat)؛ يذكر الناس أي يغتابهم ويذكر عيوبهم (tahdhib)
- **B005** Tanrı'yı kulluk amacıyla anma — kulluk amacıyla anma, yakarış, övgü, şükretme ve itaat · Tanrı'yı kulluk, övgü ve yakarışla anma
  الذكر الصلاة والدعاء والثناء (ayn;tahdhib)؛ الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة (tahdhib)؛ ولذكر الله أكبر واذكروا الله (mufradat)
- **B006** indirildiğine inanılan kutsal kitap — dinin ayrıntılarını bildiren kutsal kitap
  الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر (ayn;tahdhib)؛ القرآن والكتب المتقدمة والزبور من بعد الذكر (mufradat)
- **B007** onur, iyi ün ve saygınlık — onur, iyi ün ve övgü · belleği güçlü, yiğit veya iyi anılan adam
  الذكر العلاء والشرف (maqayis)؛ الذكر الشرف والصوت (ayn;tahdhib)؛ الذكر الصيت والثناء وذي الذكر أي ذي الشرف (sihah)؛ وإنه لذكر لك ولقومك أي شرف (mufradat)
- **B008** hakkı gösteren yazılı belge [kalıp] — hakkı gösteren yazılı belge · yazılı hak belgeleri
  ذكر الحق الصك وجمعه ذكور حقوق (ayn;tahdhib)؛ يقال ذكور حق (ayn;tahdhib)
- **B009** hatırlatma, hatırlamayı sağlayan araç ve sıkça anma — hatırlatma, öğüt alma veya sıkça anma · hatırlatıcı · hatırlatma · ona o şeyi hatırlattı
  الذكرى اسم للتذكير والتذكير مجاوز (ayn)؛ التذكرة ما تستذكر به الحاجة (sihah)؛ الذكرى بمعنى الذكر وبمعنى التذكير (tahdhib)؛ التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر (mufradat)

## ء ن ث (root_000058): 92:3 وَٱلْأُنثَىٰٓ

- **B001** disi olma — erkegin karsiti olan disi · disiler toplulugu · siirde gelen disiler cogulu · kadinin kiz cocuk dogurmasi · adet olarak kiz doguran kadin · kadinlikta tam ve olgun sayilan kadin · disi yaratilisinda erkek
  الأنثى خلاف الذكر (maqayis;sihah;tahdhib;mufradat)؛ يجمع على إناث (sihah)؛ الإناث جماعة الأنثى ويجيء أناثى (tahdhib)؛ آنثت المرأة إذا ولدت أنثى (sihah)؛ هذه امرأة أنثى إذا مدحت بأنها كاملة من النساء (tahdhib)؛ المؤنث ذكر في خلق الأنثى (tahdhib)
- **B002** yumusak ve zayif is gorur olma — yumusak veya zayif is gorur demir · kesmeyen veya keskinligi iyi olmayan kilic · isinde yumusamak ve sert davranmamak · yumusak, edilgin veya kadinsil erkek
  سيف أنيث الحديد إذا كانت حديدته أنثى (maqayis)؛ الأنيث ما كان من الحديد غير ذكر (sihah)؛ سيف أنيث وهو الذي ليس بقطاع (tahdhib)؛ أنثت في أمرك أي لنت له (tahdhib)؛ الأنيث من الرجال المخنث (tahdhib)؛ لما يضعف عمله أنثى وحديد أنيث (mufradat)؛ المنفعل يقال له أنيث (mufradat)
- **B003** testisler veya kulaklar icin ikil ad — testisler · kulaklar
  الأنثيان الخصيتان (maqayis;tahdhib)؛ الأنثيان الخصيان (sihah)؛ الأنثيان أيضا الأذنان (maqayis;sihah)؛ الأنثيان الأذنان (tahdhib)؛ الخصية لتأنيث لفظ الأنثيين وكذلك الأذن (mufradat)
- **B004** yumusak ve bitirgen toprak — yumusak, iyi bitki veren arazi · bitkisi hizli ve bol cikan yer · bitki vermeye yatkin kolay arazi · bitki bitiren yer veya nitelik
  أرض أنيثة حسنة النبات (maqayis)؛ أرض أنيثة تنبت البقل سهلة (sihah)؛ مكان أنيث إذا أسرع نباته وكثر (tahdhib)؛ أرض مئناث سهلة خليقة بالنبات (tahdhib)؛ أرض أنيثة أي سهلة (tahdhib)؛ الأنيث الذي ينبت النبت (tahdhib)؛ أرض أنيث سهل أو بجودة إنباتها (mufradat)
- **B005** dilbilgisel disillestirme — adi veya soz hukumunu disil yapmak · onu disil yapti, o da disil hukum kazandi
  تأنيث الاسم خلاف تذكيره (sihah)؛ أنثته فتأنث (sihah)؛ إذا قلت للشيء تؤنثه فالنعت بالهاء (tahdhib)؛ لما شبه في حكم اللفظ بعض الأشياء بالذكر وبعضها بالأنثى (mufradat)
- **B006** kadinsi adli putlar — kadinsi adlarla anilan putlar veya ibadet nesneleri · cansiz ve edilgin varliklar · bir topluluga ait put diye adlandirma
  إن يدعون من دونه إلا إناثا (tahdhib;mufradat)؛ مواتا مثل الحجر والخشب والشجر (tahdhib)؛ سموا الأوثان إناثا لقولهم اللاتي والعزى ومناة (tahdhib)؛ كانوا يقولون للصنم أنثى بني فلان (tahdhib)؛ أسماء معبوداتهم مؤنثة (mufradat)؛ المنفعل يقال له أنيث (mufradat)
- **B007** renk veren kadin kokusu — giysiye renk veren kadin kokusu
  المؤنث من الطيب طيب النساء مثل الخلوق والزعفران وما يلون الثياب؛ ذكورة الطيب ما لا لون له مثل الغالية والكافور والمسك والعود والعنبر
- **B008** iki Arap kabilesinin adi — iki Arap kabilesi icin ortak ad
  الأنثيان من أحياء العرب بجيلة وقضاعة

## س ع ي (root_000709): 92:4 سَعْيَكُمْ

- **B001** hedefe doğru hızlı ve amaçlı ilerleme — hızlı yürüme, hafif koşma veya amaçlı gidiş · hızlı yürümek, hafifçe koşmak veya yönelmek · anma çağrısına yönelmek veya gitmek · iki kutsal durak arasındaki özel ibadet yürüyüşü
  السعي عدو ليس بشديد (ayn)؛ سعى الرجل يسعى سعيا أي عدا (sihah)؛ السعي والذهاب بمعنى واحد وليس هذا باشتداد؛ سعى إذا مشى وسعى إذا عدا وسعى إذا قصد (tahdhib)؛ السعي المشي السريع وهو دون العدو؛ وخص المشي فيما بين الصفا والمروة بالسعي (mufradat)
- **B002** bir işte çalışıp kazanma ve çaba gösterme — iş, kazanç ve ciddi çaba · çalışmak, kazanmak ve bir işi yürütmek · ailesinin geçimi için çalışmak · çalışma ve iş yürütme
  كل عمل من خير أو شر فهو السعي؛ السعي العمل أي الكسب (ayn)؛ إذا عمل وكسب (sihah)؛ أصل السعي التصرف في كل عمل؛ السعي يكون في الصلاح ويكون في الفساد؛ المرء يسعى لغاريه أي يكسب (tahdhib)؛ يستعمل للجد في الأمر خيرا كان أو شرا (mufradat)
- **B003** bir topluluğun işini yürüten yetkili görevli — vergi toplama görevi · atanmış yönetici veya vergi toplama görevlisi · atanmış yöneticiler veya vergi toplama görevlileri · vergi toplamakla görevlendirilmek · bir din topluluğunun başkanı ve yetkili temsilcisi
  السعاية في أخذ الصدقات (maqayis)؛ الساعي الذي يولى قبض الصدقات والجمع سعاة (ayn)؛ من ولى شيئا على قوم فهو ساع عليهم وأكثر ما يقال ذلك في ولاة الصدقة (sihah)؛ الساعي الذي يقوم بأمر أصحابه عند السلطان؛ عامل الصدقات ساع؛ ساعي اليهود والنصارى هو رئيسهم؛ من ولى عملا على قوم فهو ساع عليهم (tahdhib)؛ خصت السعاية بأخذ الصدقة (mufradat)
- **B004** birini üst makama kötüleyerek ihbar etme — üst makama kötüleyerek ihbar etme · birini yöneticiye kötüleyerek ihbar etmek · üst makama söz taşıyan ihbarcı
  السعاية أن تسعى بصاحبك إلى وال أو من فوقه (ayn)؛ سعى به إلى الوالي إذا وشى به (sihah)؛ الساعي الذي يسعى بصاحبه إلى سلطانه؛ القتات والساعي والماحل واحد؛ الساعي مثلث بإهلاكه ثلاثة نفر (tahdhib)؛ خصت السعاية بالنميمة (mufradat)
- **B005** özgürlük bedelini çalışarak ödeme — köleleştirilmiş kişinin özgürlüğü için çalışması · özgürlük bedelini çalışarak kazanma · özgürlük sözleşmesinin bedelini çalışarak ödemek · köleleştirilmiş kişiyi kendi bedeli için çalıştırmak · kalan özgürlük bedelini çalışarak ödeyen kişi
  سعاية العبد إذا كوتب أن يسعى فيما يفك رقبته (maqayis)؛ السعاية ما يستسعى فيه العبد من ثمن رقبته (ayn)؛ سعى المكاتب في عتق رقبته سعاية؛ استسعيت العبد في قيمته (sihah)؛ استسعاء العبد إذا عتق بعضه ورق بعضه؛ يستسعى في ثلثي رقبته (tahdhib)؛ خصت السعاية بكسب المكاتب لعتق رقبته (mufradat)
- **B006** övünç getiren soylu ve cömert iş — cömertlikle kazanılan onurlu iş ve başarı · övünç veren onurlu işler ve başarılar · barış için bedel üstlenen uzlaştırıcılar
  المسعاة في الكرم والجود (maqayis)؛ المسعاة في الكرم والجود (ayn)؛ المسعاة واحدة المساعي في الكرم والجود (sihah)؛ أصحاب الحمالات لحقن الدماء وإطفاء النائرة سعاة؛ مآثر أهل الشرف والفضل مساعي واحدتها مسعاة (tahdhib)؛ المسعاة بطلب المكرمة (mufradat)
- **B007** köleleştirilmiş kadınla ilişki veya onu cinsel kazanca zorlama — köleleştirilmiş bir kadınla evlilik dışı cinsel ilişkiye girmek · köleleştirilmiş kadınlarla sınırlı evlilik dışı ilişki veya onları cinsel kazanca zorlama
  ساعي الرجل الأمة إذا فجر بها؛ لا تكون المساعاة إلا في الإماء خاصة (maqayis)؛ يقال في الأمة خاصة قد ساعاها؛ لا تكون المساعاة إلا في الإماء؛ إماء ساعين في الجاهلية (sihah)؛ المساعاة الزنى؛ لا تكون في الحرائر إنما تكون في الإماء؛ مساعاة الأمة إذ ساعاها مالكها فضرب عليها ضريبة تؤديها بالزنى (tahdhib)؛ خصت المساعاة بالفجور (mufradat)
- **B008** aynı uğraşta rakibini yenme — benimle aynı uğraşta yarıştı, ben de onu yendim
  ساعانى فلان فسعيته أسعيه إذا غلبته فيه (sihah)

## ECHO س و ع (root_000760): for 92:4 سَعْيَكُمْ: withheld observed target; not identity

- **B001** zamanın sürmesi ve belirli bir zaman kesiti — şimdiki zaman ya da gece ve gündüzden bir bölüm · dünyanın sona erip insanların yeniden dirileceği gün · zaman bölümleri · kısacık bir zaman · gecenin sakinleşmesinden bir süre sonra · gecenin sakinleşmesinden bir süre sonra · zaman dilimi başına işlem yapma · bir çalışanı zaman dilimi başına tutmak · çetin bir zaman kesiti
  استمرار الشيء ومضيه (maqayis)؛ الساعة سميت بذلك (maqayis)؛ الساعة الوقت الحاضر (sihah)؛ الساعة القيامة (ayn;sihah;tahdhib)؛ الساعة جزء من آخر الليل والنهار (tahdhib)؛ جاءنا بعد سوع من الليل وبعد سواع (maqayis;sihah;tahdhib)؛ عاملته مساوعة (maqayis;sihah)؛ ساوعت الأجير إذا استأجرته ساعة بعد ساعة (tahdhib)؛ ساعة سوعاء أي شديدة (sihah)
- **B002** gözetimsiz bırakıp başıboş gitmesine yol açma — develeri kendi yönlerine gidecek biçimde gözetimsiz bırakmak · bir şeyi kaybetmek · gözetimsiz kaldığı için kendi yönüne gitmek · başıboş gitmek veya yavrusunu gözetimsiz bırakmak · kaybolmuş ve gözetimsiz kalmış · otlakta kendi başına uzaklaşan dişi deve · yavrusunu yırtıcıya açık biçimde bırakan dişi deve · malını savuran adam · malı savuran kişi
  أسعت الإبل إساعة إذا أهملتها (maqayis;sihah;tahdhib)؛ ساعت فهي تسوع (maqayis;sihah;tahdhib)؛ ضائع سائع (maqayis;sihah;tahdhib)؛ ناقة مسياع تذهب في المرعى (maqayis;sihah;tahdhib)؛ رجل مسياع مضياع للمال (sihah;tahdhib)؛ ناقة مسياع تدع ولدها حتى يأكله السبع (tahdhib)
- **B003** eski anlatılarda geçen belirli bir putun özel adı — eski anlatılarda tapınılan belirli bir putun özel adı
  سواع اسم صنم في زمن نوح (ayn;tahdhib)؛ سواع اسم صنم كان لقوم نوح ثم صار لهذيل (sihah)
- **B004** saman karıştırılmış çamur — saman karıştırılmış çamur
  السياع الطين فيه التبن (maqayis)
- **B005** boşalma öncesi salgı — boşalma öncesi salgı · boşalmadan önce çıkan salgı · boşalma öncesi salgıyla ilgilenme buyruğu
  السواعي مأخوذ من السواع وهو المذي وهو السوعاء (tahdhib)؛ السوعاء المذي الذي يخرج قبل النطفة (tahdhib)؛ سع سع إذا أمرته أن يتعهد سوعاءه (tahdhib)
- **B006** ölüp yok olanlar — ölüp yok olmuş kimseler
  الساعة الهلكى (tahdhib)

## ش ت ت (root_000775): 92:4 لَشَتَّىٰ

- **B001** dağılma ve dağıtma — dağılmak; dağılma · dağıtmak, dağınık hale getirmek · topluluğum işimi dağıttı · şu şey gönlümü dağıttı · yayılıp dağılmak · dağılıp yayılmak · ayrı kişiler veya dağınık parçalar halinde · dağınıklık ve ayrılık · dağılmış, dağınık · dağınık bir iş veya durum · çeşitli, birbirinden farklı · aynı soydan olmayan insanlar
  أصل يدل على تفرق وتزيل (maqayis)؛ الشت مصدر الشيء الشتيت وهو المتفرق (ayn)؛ شت يشت شتاتا وهو التفرق (jamhara)؛ أمر شت أي متفرق (sihah)؛ يصدر الناس أشتاتا أي متفرقين (tahdhib)؛ الشت تفريق الشعب (mufradat)
- **B002** güzel ve aralıklı diş dizisi [kalıp] — dişleri güzel, düzgün ve aralıklı ağız
  ثغر شتيت مفلج حسن (maqayis)؛ ثغر شتيت مفلج حسن (ayn)؛ ثغر شتيت أي مفلج (sihah)
- **B003** iki şey arasındaki büyük uzaklık ve uyuşmazlık — ne kadar uzak ve farklılar · ikisi birbirinden ne kadar uzak ve farklı · aralarında ne büyük uzaklık ve ayrılık var
  شتان ما هما (maqayis;ayn;sihah;tahdhib;mufradat)؛ شتان ما بينهما (maqayis;sihah;mufradat)؛ تباعد ما بينهما (tahdhib)؛ ارتفاع الالتئام بينهما (mufradat)

## ع ط و (root_001028): 92:5 أَعْطَىٰ

- **B001** elle uzanıp alma — elle alma · bir şeyi elle alma · yapraklara erişmek için ön ayaklarını kaldıran ceylan
  العطو التناول باليد (maqayis;ayn;tahdhib)؛ عطوت الشيء تناولته باليد (sihah)؛ الظبي العاطي الرافع يديه إلى الشجرة ليتناول من الورق (ayn)؛ الظباء تتطالل إذا رفعت أيديها لتتناول ورق الشجر (tahdhib)
- **B002** verme, karşılıklı elden geçirme ve verilen şey — verme, elden uzatma · karşılıklı elden verme veya el değiştirme · kılıcı sırayla birbirine verip elde tutma veya sallama · verilen şey · birine verilen şey · birine verilen şeyler · verilen şeylerin çoğul adı · çok veren kimse · malı ne çok veriyor!
  منه اشتق الإعطاء والمعاطاة المناولة والعطاء اسم لما يعطى وهي العطية (maqayis)؛ العطاء اسم لما يعطى وأعطية وأعطيات (ayn)؛ أعطاه مالا يعطيه إعطاء والاسم العطاء والعطية الشيء المعطى (sihah)؛ الإعطاء مأخوذ من هذا والمعاطاة المناولة والعطاء اسم لما يعطى (tahdhib)؛ المعاطاة أن يستقبل رجل رجلا ومعه سيف فيقول أرني سيفك فيعطيه فيهزه هذا ساعة وهذا ساعة (tahdhib)
- **B003** birinin işini görüp istediğini uzatma — çocuğun yakınlarının işini görüp istediklerini uzatması · onun işini görüp bakımını üstlenme · işimi görüyor
  عاطى الصبي أهله إذا عمل وناول ما أرادوا (maqayis)؛ هو يعطيني ويعاطيني إذا كان يخدمك (sihah)؛ عطيته وعاطيته أي خدمته وقمت بأمره ومن يعطيك أي من يتولى خدمتك (tahdhib)
- **B004** hakkı olmadan el uzatma ve gözü pekçe işe girişme — hakkı olmayan veya alınması uygun görülmeyen şeye el uzatma · bir işe girip onunla uğraşma · gözü pekçe eyleme girişip deveyi yaralama · aracı, dayanağı veya yeterliği olmadan erişilmez işe kalkışma
  التعاطي تناول ما ليس له بحق ويتعاطى ظلم فلان وفتعاطى فعقر وعاط بغير أنواط (maqayis)؛ تعاطاه تناوله وفلان يتعاطى كذا أي يخوض فيه وفتعاطى فعقر (sihah)؛ التعاطي تناول ما لا يجوز تناوله وفتعاطى الشقي عقر الناقة فبلغ ما أراد وتعاطيه جرأته ويتعاطى معالي الأمور ورفيعها ويتعاطى أمرا قبيحا (tahdhib)
- **B005** insanlardan bir şey isteme — bir şey verilmesini isteme · bir şey verilmesini isteme · insanlardan bir şey isteme
  استعطى وتعطى سأل العطاء (sihah)؛ يستعطي الناس بكفه وفي كفه استعطاء إذا سألهم وطلب إليهم (tahdhib)
- **B006** direnmeden uyma ve kolay bükülme — devenin direnmeyip yönlendirmeye uyması · kolay bükülen yumuşak yay · gerilirken direnmeyen yumuşak yay · boyun eğip başını biniciye çevir
  أعطى البعير إذا انقاد ولم يستعصب (sihah)؛ قوس عطوى مواتية سهلة (sihah)؛ قوس معطية لينة ليست بكزة ولا ممتنعة (tahdhib)؛ أعط فيعوج رأسه إلى راكبه (tahdhib)
- **B007** karşılıklı çekişmede yenme — karşılıklı çekişmede onu yenme
  تعاطينا فعطوته أي غلبته (sihah)

## و ق ي (root_001677): 92:5 وَٱتَّقَىٰ, 92:17 ٱلْأَتْقَى

- **B001** araya engel koyarak zarardan koruma — bir şeyi koruyucu bir engelle zarardan saklamak · koruma; zararı önleyen araç veya engel · bir şeyi korumaya yarayan araç ya da engel · zarardan koruyan şey · zararı savan koruyucu · kadının saçı ile dış örtüsü arasına koyduğu koruyucu bez · koruyucu şeyler
  دفع شيء عن شيء بغيره (maqayis)؛ كل ما وقى شيئا فهو وقاء له ووقاية (ayn;jamhara;tahdhib)؛ حفظ الشيء مما يؤذيه ويضره (mufradat)؛ وقاية المرأة وهي الخرقة التي بين جلبابها وشعرها (jamhara)
- **B002** korkulan şeyden ya da yanlış davranıştan kendini koruma — kendini korkulan ya da zarar verecek şeyden korumak · bir şeyi kendine koruyucu yapmak · Tanrı'ya karşı gelmekten sakınmak · kişinin kendini korktuğu şeyden ve yanlış davranıştan koruması · sakınma ve kendini koruma · sakınan ve kendini yanlış davranıştan koruyan kimse · sakınma; kendini kötülükten koruma · sakınıp kendini koruma · kendini yanlış davranışlardan koruyan kimse · sakınan ve kendini yanlış davranıştan koruyan kimse
  اتق الله توقه أي اجعل بينك وبينه كالوقاية (maqayis)؛ التقوى في الأصل وقوى فعلى من وقيت (ayn;tahdhib)؛ التقوى جعل النفس في وقاية مما يخاف (mufradat)؛ حفظ النفس عما يؤثم (mufradat)؛ اتقى تقية وتقاة (sihah)
- **B003** hafif topallama ve toynak ağrısıyla yürümekten çekinme — hafif topallama · topallayan, toynak ağrısıyla yürümekten çekinen veya ayağını sert zeminden sakınan at · hayvanın sırtında yara açmayan eyer · aksayışını gözet ve ağırdan al
  الوقى هو الظلع اليسير (maqayis)؛ فرس واق إذا كان ظالعا (ayn)؛ ق على ظلعك أي الزمه (sihah)؛ فرس واق إذا كان يهاب المشي من وجع يجده في حافره (sihah)؛ سرج واق إذا لم يكن معقرا (sihah;tahdhib)؛ لا تقي بالجدجد أي لا تشتكي حزونة الأرض (tahdhib)
- **B004** kırk gümüş para ağırlığındaki, yağda yedi birimlik biçimi bulunan ölçü — kırk gümüş para ağırlığına eşit bilinen ölçü · yağ için yedi temel ağırlık birimine eşit ölçü · bu ağırlık ölçüsü adının çoğul biçimleri
  الأوقية في الحديث أربعون درهما (sihah;tahdhib)؛ الوقية وزن من أوزان الدهن وهي سبعة مثاقيل (tahdhib)؛ اللغة الجيدة أوقية وجمعها أواقي وأواق (tahdhib)
- **B005** örümcek kuşu — örümcek kuşu; aynı kuş adının uzun ve kısalmış biçimleri
  الواقي الصرد (sihah;tahdhib)؛ الواق بكسر القاف بلا ياء (sihah)؛ قيل للصرد واق لأنه لا ينبسط في مشيه (tahdhib)

## ص د ق (root_000852): 92:6 وَصَدَّقَ

- **B001** sözün inançla ve gerçekle uyuşması — doğruluk; sözün inançla ve gerçekle uyuşması · konuşurken doğruyu söylemek · birine doğru söz söylemek veya onun sözünü doğru saymak · doğruluğa sürekli bağlı ve kuşkusuz onaylayan kimse · çok doğru sözlü kimse
  الصدق خلاف الكذب (maqayis;ayn;sihah;tahdhib)؛ الصدق والكذب أصلهما في القول (mufradat)؛ الصدق مطابقة القول الضمير والمخبر عنه معا (mufradat)
- **B002** nesnenin sağlamlığı veya düzgünlüğü — bir nesnedeki sertlik veya düzgünlük · sert ve güçlü nesne ya da mızrak
  شيء صدق أي صلب (maqayis)؛ رمح صدق (maqayis)؛ الصدق الصلب والمستوي (sihah;tahdhib)
- **B003** tamlık, iyilik ve güvenilirlik — iyi, güvenilir ve erdemli kişi ya da topluluk · bir şeyde tamlık ve kusursuzluk · övülmeye değer, iyi ve sağlam durum
  رجل صدق (maqayis;ayn;sihah;tahdhib)؛ الصدق الكامل من كل شيء (ayn;tahdhib)؛ في مقعد صدق وقدم صدق ومدخل صدق ومخرج صدق ولسان صدق (mufradat)
- **B004** sözü veya beklentiyi doğrulayıp gerçekleştirme — savaşta gereğini yerine getirip sebat etmek · atılımında veya koşusunda verdiği sözü tutan · tahmini gerçekleşmek veya tahminini gerçekleştirmek · bir sözün veya durumun doğruluğunu ortaya koyma ve onaylama · öncekini doğrulayan ve destekleyen · sözü doğru kabul edip onaylayan kimse · doğruluğa sürekli bağlı ve kuşkusuz onaylayan kimse
  صدقوهم القتال (maqayis;sihah;tahdhib)؛ صدق في القتال إذا وفى حقه (mufradat)؛ صدق ظني (mufradat)؛ لقد صدق عليهم إبليس ظنه أي حقق ظنه (tahdhib)؛ مصدق لما معهم (mufradat)
- **B005** içten sevgiye dayalı dostluk — dost veya yakın arkadaş · içten sevgiye dayalı arkadaşlık ve dostluk kurma
  الصداقة مشتقة من الصدق في المودة (maqayis)؛ الصداقة مصدر الصديق (ayn;tahdhib)؛ الصداقة والمصادقة المخالة (sihah)؛ الصداقة صدق الاعتقاد في المودة (mufradat)
- **B006** mal vererek yardım etme veya haktan vazgeçme — iyilik amacıyla maldan verilen yardım veya bu adla anılan yükümlü pay · bir hakkından bağışlayarak vazgeçmek · mali yardım veren kimse · hayvanlara ilişkin yardım paylarını toplayan görevli · mali yardım veren erkekler ve kadınlar
  الصدقة ما يتصدق به المرء عن نفسه وماله (maqayis)؛ المتصدق المعطي للصدقة (ayn;sihah;tahdhib)؛ المصدق الذي يأخذ صدقات الغنم (maqayis;sihah;tahdhib)؛ الصدقة ما يخرجه الإنسان من ماله على وجه القربة (mufradat)؛ من تجافى عنه (mufradat)
- **B007** kadına belirlenen evlilik hakkı olan mal — kadına verilen veya belirlenen evlilik hakkı olan mal · kadının evlilikte aldığı mal veya kadınlara ait bu tür mallar · kadına evlilik hakkı olarak mal belirlemek
  الصداق صداق المرأة (maqayis)؛ الصداق والصدقة والصدقة المهر (ayn)؛ الصداق والصداق مهر المرأة (sihah)؛ صداق المرأة وصدقة المرأة (tahdhib)؛ صداق المرأة وصداقها وصدقتها ما تعطى من مهرها (mufradat)

## ح س ن (root_000323): 92:6 بِٱلْحُسْنَىٰ, 92:9 بِٱلْحُسْنَىٰ

- **B001** akla, eğilime veya duyulara göre güzel ve beğenilir olma — güzel ve beğenilir olma; güzellik · güzel olmak · güzel erkek · güzel kadın · güzel kadın · çok güzel kadın · çok güzel · güzel yanlar ve iyi nitelikler · bedenin güzel yeri
  الحسن ضد القبح (maqayis;sihah)؛ حسن الشيء فهو حسن (ayn)؛ الحسن نعت لما حسن (tahdhib)؛ كل مبهج مرغوب فيه (mufradat)؛ مستحسن من جهة العقل ومستحسن من جهة الهوى ومستحسن من جهة الحس (mufradat)؛ رجل حسن وامرأة حسناء وحسانة (maqayis)؛ الحسان الحسن جدا (ayn)؛ المحاسن ضد المساوىء (maqayis;ayn;sihah;tahdhib)
- **B002** bir şeyi güzelleştirme, işi iyi yapma veya başkasına iyilik etme — bir şeyi güzelleştirmek · birine iyilik etmek · işini iyi ve ustalıkla yapmak · iyilik etme veya işi iyi yapma · iyilik eden veya işini iyi yapan kimse · sürekli iyilik eden kimse · güzel bulmak; beğenmek
  أحسنت إليه وبه (sihah)؛ وهو يحسن الشيء أي يعمله (sihah)؛ حسنت الشيء تحسينا زينته (sihah)؛ أحسن يا هذا فإنك محسان (tahdhib)؛ الإحسان ضد الإساءة (tahdhib)؛ أحسنت بفلان أي أحسنت إليه (tahdhib)؛ الإحسان يقال على وجهين الإنعام على الغير وإحسان في فعله (mufradat)؛ الإحسان فوق العدل (mufradat)
- **B003** kişiye ulaşan sevindirici iyilik, karşılık veya iyi sonuç — kişiye ulaşan iyilik, bolluk veya ödül · iyi son veya en güzel karşılık; sonsuz mutluluk yurdu, utkı ya da inancı uğruna ölme · iki iyi sonuçtan biri: utkı ya da inancı uğruna ölme · kötü işleri gideren iyi işler, özellikle beş günlük tapınma
  للذين أحسنوا الحسنى وزيادة أي الجنة وهي ضد السوءى (ayn)؛ الحسنة خلاف السيئة (sihah)؛ الحسنى خلاف السوأى (sihah)؛ الحسنى هي الجنة وضد الحسنى السوءى (tahdhib)؛ إحدى الحسنيين يعني الظفر أو الشهادة (tahdhib)؛ حسنة أي نعمة (tahdhib)؛ أي غنيمة وخصب (tahdhib)؛ الحسنة يعبر عنها عن كل ما يسر من نعمة (mufradat)؛ خصب وسعة وظفر (mufradat)؛ من ثواب وما أصابك من سيئة أي من عقاب (mufradat)
- **B004** yer, gök cismi ve beden bölümü adları ile kum tepesine oturma kullanımı — bir dağın, kum sırtının, kumluğun veya kum tepesinin adı · ön kolun bileğe yakın yarısı · ay · yüksek dağ · temiz ve yüksek bir kum tepesine oturmak · iki yerin veya iki kum sırtının birlikte anılışı
  الحسن جبل وحبل من حبال الرمل (maqayis)؛ الحسن من الذراع النصف الذي يلي الكوع (maqayis)؛ حسن اسم رملة لنبي سعد (ayn)؛ الحاسن القمر (sihah)؛ الحسن اسم رملة لبنى سعد (sihah)؛ الحسن نقا في ديار بني تميم (tahdhib)؛ أحسن الرجل إذا جلس على الحسن وهو الكثيب النقي العالي (tahdhib)؛ الحسين الجبل العالي (tahdhib)
- **B005** bir işteki en yüksek çabası ve erişebileceği son sınır — bir işi yaparken gösterebileceği en yüksek çaba ve erişebileceği son sınır · bir işi yaparken gösterebileceği en yüksek çaba ve erişebileceği son sınır
  حُسَيْناؤه أن يفعل كذا وحُسَيْناه مثله أي جهده وغايته (tahdhib)

## ي س ر (root_001694): 92:7 فَسَنُيَسِّرُهُۥ, 92:7 لِلْيُسْرَىٰ, 92:10 فَسَنُيَسِّرُهُۥ

- **B001** kolaylık; kolay ve hazır duruma gelme ya da getirme — kolaylık, güçlüğün karşıtı · kolay olan, güç olmayan · kolaylaşıp hazır duruma gelmek · kolaylaştırıp hazırlamak · birine anlayış gösterip kolaylık sağlamak · kolay olan · kolay, güç olmayan
  اليسر: ضد العسر (maqayis;mufradat)؛ الميسور: ضد المعسور، وتيسر واستيسر بمعنى تهيأ (sihah)؛ تيسر واستيسر أي تسهل وتهيأ، وأيسرت المرأة وتيسرت في كذا أي سهلته وهيأته (mufradat)؛ ياسره أي ساهله (sihah)
- **B002** az miktar veya kısa süre — az miktar veya kısa süre
  اليسير: القليل، وشيء يسير أي هين (sihah)؛ واليسير يقال في الشيء القليل (mufradat)
- **B003** maddi bolluk ve varlıklı olma — maddi bolluk ve varlıklılık · varlıklılık ve maddi güç · varlıklılık · varlıklı duruma gelmek
  الميسرة والميسرة: السعة والغنى؛ واليسار واليسارة: الغنى، وقد أيسر الرجل أي استغنى (sihah)؛ الميسرة واليسار عبارة عن الغنى (mufradat)
- **B004** sol el veya sol yön — sol el veya sol yön · soldaki, sağın karşıtı · sol taraf · sola yönelip ilerlemek · iki elini de kullanabilen kişi
  اليسار لليد، تياسروا إذ أخذوا ذات اليسار، وياسروا (maqayis)؛ الأيسر: نقيض الأيمن، والميسرة خلاف الميمنة، واليسار خلاف اليمين، والياسر نقيض اليامن، ورجل أعسر يسر للذي يعمل بكلتا يديه (sihah)
- **B005** yumuşak başlı ve harekette uyumlu olma — yumuşak başlı ve çabuk uyum gösteren · hafif bacaklar · hayvanın bacaklarını iyi aktarması
  اليسرات: القوائم الخفاف؛ فرس حسن التيسور أي حسن نقل القوائم؛ رجل يسر ويسر أي حسن الانقياد (maqayis)؛ ليسر خفيف ويسر أي لين الانقياد سريع المتابعة يوصف به الإنسان والفرس (ayn)؛ اليسرات: القوائم الخفاف، ودابة حسن التيسور أي حسن نقل القوائم (sihah)
- **B006** koyunların süt ve yavru bakımından çoğalması [kalıp] — koyunların sütü ve yavrusu çoğalmak
  يسرت الغنم إذا كثر لبنها ونسلها (maqayis;sihah)
- **B007** fal oklarıyla oynanan paylaştırmalı talih oyunu — fal oklarıyla oynanan geleneksel talih oyunu · fal okları oyununa katılmak için toplananlar · fal oklarıyla oynayan kişi · fal oklarıyla oynayan kişi · topluluğun deveyi kesip parçalarını paylaştırması · deveyi kesip oyun düzenine göre paylaştırmak
  الأيسار: القوم يجتمعون على الميسر، واحدهم يسر؛ والميسر: القمار (maqayis)؛ الميسر: قمار العرب بالأزلام؛ الياسر: اللاعب بالقداح؛ اليسر والياسر بمعنى والجمع أيسار؛ يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها (sihah)
- **B008** ayrı avuç çizgileri veya uyluk damgası — avuç içindeki birbirine bitişmeyen çizgiler · uyluklardaki damga
  اليسرة: أسرار الكف إذا كانت غير ملزقة (maqayis;sihah)؛ اليسرة أيضا: سمة في الفخذين (sihah)
- **B009** aşağı doğru burma veya yüz hizasına saplama — sağ eli gövdeye çekerek aşağı doğru burma · yüz hizasına yöneltilen saplama
  اليسر: الفتل إلى أسفل، وهو أن تمد يمينك نحو جسدك؛ والطعن اليسر: حذاء وجهك (sihah)
- **B010** yer ve kişi adı kullanımları — bir yerin adı · çöl bölgesindeki bir geçidin adı · anlatıda geçen bir kişinin adı
  يسر: مكان (maqayis)؛ اليسر أيضا: دخل لنبى يربوع بالدهناء (sihah)؛ يسار الكواعب هو اسم عبد (sihah)
- **B011** genç erkek — genç erkek, delikanlı
  اليسار: الفتى (maqayis)

## ب خ ل (root_000089): 92:8 بَخِلَ

- **B001** eldeki varlıkları haksız yere esirgeme — cimrilik; eldeki varlıkları haksız yere esirgeme · cimrilik etmek; verilmesi gerekeni esirgemek · cimrilik eden kişi · sık sık cimrilik eden; cimri · cimriliği huy edinmiş kişi · cimri diye nitelenen kişi · tek bir cimrilik davranışı · kişinin kendi varlıklarını esirgemesi · başkasına ait varlıklar konusunda esirgeyici davranma; daha ağır kınanan biçim
  البخل والبخل؛ رجل بخيل وباخل؛ فهو بخال (maqayis); بخل بخلا وبخلا فهو بخيل بخال مبخل؛ والبخلة بخل مرة واحدة (ayn); البخل إمساك المقتنيات عما لا يحق حبسها عنه؛ ويقابله الجود؛ البخل ضربان بخل بقنيات نفسه وبخل بقنيات غيره (mufradat)

## غ ن ي (root_001110): 92:8 وَٱسْتَغْنَىٰ, 92:11 يُغْنِى

- **B001** maddi bolluk ve ihtiyaçtan bağımsızlık — maddi zenginlik, bolluk ve ihtiyaçsızlık · varlıklı, zengin · zenginleşmek veya başkasına ihtiyaç duymayacak duruma gelmek · ona ihtiyaç duymamak · onunla yetinip başka bir şeye ihtiyaç duymamak · bir şeye ihtiyaç duymama durumu · zenginlik ve bolluk · gönül tokluğu ve az şeye ihtiyaç duyma · zengin etmek veya yoksunluğunu gidermek · Kur'an'la yetinip başka bir şeye ihtiyaç duymamak
  الغنى في المال (maqayis;tahdhib)؛ الغنى مقصور في المال واستغنى الرجل أصاب غنى (ayn;tahdhib)؛ الغنى مقصور اليسار وتغنى الرجل أي استغنى (sihah)؛ الغني ذو الوفر (ayn;tahdhib)؛ عدم الحاجات وقلة الحاجات وكثرة القنيات (mufradat)؛ تغنيت وتغانيت بمعنى استغنيت (maqayis;tahdhib)
- **B002** ihtiyacı karşılayıp yarar sağlama ve yerini tutma — yeterlilik, ihtiyacı karşılama ve yarar · onun yerine yetmek, ihtiyacını karşılamak ve yarar sağlamak · bu sana yetmez ve yarar sağlamaz · yeterli ve ihtiyacı karşılayan · birinin yerini tutan yeterlilik ve işlev · zararını benden uzak tut
  الغناء بالفتح الكفاية ولا يغني أي لا يكفي (maqayis)؛ الغناء الاستغناء والكفاية ورجل مغن أي مجزئ (ayn)؛ ما يغني عنك هذا أي ما يجزئ وما ينفع والغناء بالفتح النفع (sihah)؛ الإجزاء والكفاية ورجل مغن أي مجزئ كاف (tahdhib)؛ أغناني كذا وأغنى عنه كذا إذا كفاه (mufradat)
- **B003** sesle ezgi söyleme, dinleme ve ezgili okuma — şarkı söyleme, ezgili seslendirme ve dinleti · şarkı; ezgili söylenen parça · şarkı söylemek · şarkı söylemek veya sesi ezgili ve duygulu kullanmak · Kur'an'ı hüzünlü, yumuşak ve ezgili bir sesle okumak
  الغناء من الصوت والأغنية اللون من الغناء (maqayis)؛ الغناء ممدود في الصوت وغنى يغني أغنية وغناء (ayn)؛ الأغنية الغناء والجمع الأغاني والغناء بالكسر من السماع (sihah)؛ الغناء الصوت ممدود والتطريب وتحزين القراءة وترقيقها (tahdhib)؛ غنى أغنية وغناء (mufradat)
- **B004** bir yerde uzun süre kalıp yaşama — bir yerde oturmak ve uzun süre kalmak · sanki daha dün orada hiç yaşamamıştı · bir topluluğun oturduğu evler ve yurtlar · oturma eylemi veya oturulan yer
  غني القوم في دارهم أقاموا ومغانيهم منازلهم (maqayis)؛ غني القوم في المحلة طال مقامهم فيها وكأن لم يغن بالأمس أي كأن لم يكن (ayn)؛ غنى بالمكان أي أقام وغني أي عاش والمغنى واحد المغاني (sihah)؛ غني القوم في دارهم إذا طال مقامهم والمغاني المنازل (tahdhib)؛ غنى في مكان كذا إذا طال مقامه فيه والمغنى للمصدر وللمكان (mufradat)
- **B005** süsten bağımsız sayılan; bazen genç, güzel veya evli kadın — eşi veya güzelliği sayesinde süse ihtiyaç duymadığı düşünülen; ayrıca genç, güzel ya da evli kadın · bu niteliklerle anılan kadınlar; bazı kullanımlarda genç, güzel, evli ya da genel olarak kadınlar
  الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي (maqayis)؛ الغانية الشابة المتزوجة غنيت بزوجها وغنيت بجمالها عن الزينة (ayn)؛ الغانية الجارية التي غنيت بزوجها وقد تكون التي غنيت بحسنها وجمالها (sihah)؛ الغواني ذوات الأزواج أو الشواب أو الجارية الحسناء أو كل امرأة (tahdhib)؛ الغانية المستغنية بزوجها عن الزينة أو بحسنها عن التزين (mufradat)
- **B006** evlenme ve evlendirme — evlenme; bekâr kişi için koruyucu sayılan evlilik · gelinleri evlendirme
  الأغناء إملاكات العرائس (tahdhib)؛ الغنى التزويج (tahdhib)؛ الغنى حصن للعزب أي التزويج (tahdhib)

## ك ذ ب (root_001290): 92:9 وَكَذَّبَ, 92:16 كَذَّبَ

- **B001** sözde veya davranışta doğruluğa aykırılık — sözde veya davranışta doğruluğa aykırılık; yalan · yalancı; çok yalan söyleyen kişi · uydurma söz; yalanlar · özürlere kaçınılmaz olarak yalan karışır
  الكذب خلاف الصدق (maqayis;jamhara); الكذاب لغة في الكذب (ayn); كذب كذبا فهو كاذب وكذاب وكذوب (sihah); يقال في المقال والفعال (mufradat)
- **B002** yalan sayma veya yalancı bulma — yalanlama; yalan sayma · birini yalancı saymak veya ona yalan söylediğini bildirmek · birini yalancı bulmak veya yalanını ortaya çıkarmak · seni yalancı saymıyorum
  كذبت فلانا نسبته إلى الكذب وأكذبته وجدته كاذبا (maqayis); كذبته جعلته كاذبا (ayn); كذبت بالحديث كذابا وتكذيبا (jamhara); أكذبت الرجل ألفيته كاذبا وكذبته إذا قلت له كذبت (sihah); كذبته نسبته إلى الكذب (mufradat)
- **B003** onu üstlen; sana düşer [kalıp] — şunu üstlen; sana düşer veya onu yapmalısın
  كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك (maqayis); كذب عليكم الحج أي وجب عليكم ودونكم الحج (ayn); كذب عليك كذا وكذا في معنى الإغراء (jamhara); كذب عليكم الحج أي وجب (sihah); كذب عليك الحج قيل معناه وجب فعليك به (mufradat)
- **B004** hamlede duraksamak; olumsuzda sonuna kadar ilerlemek [kalıp] — saldırıya geçti ama duraksadı veya korktu · saldırıya geçti ve vuruncaya kadar durmadı; korkmadı
  حمل فلان ثم كذب أي لم يصدق في الحملة (maqayis); حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف (jamhara); حمل فلان فما كذب أي ما جبن (sihah); حمل فلان على قرنه فكذب (mufradat)
- **B005** gecikmeden yapmak [kalıp] — yapmakta gecikmedi; hemen yaptı
  ما كذب فلان أن فعل كذا أي ما لبث (maqayis;sihah)
- **B006** sütün kesilmesi veya beklenenden önce tükenmesi [kalıp] — dişi devenin sütü kesildi veya umulduğu kadar sürmedi
  كذب لبن الناقة ذهب وفيه نظر وقياسه صحيح (maqayis); كذب لبن الناقة أي ذهب (sihah); كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم (mufradat)
- **B007** koşup arkasına bakmak için durmak [kalıp] — yaban hayvanı bir mesafe koşup arkasına bakmak için durdu
  كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه (jamhara)
- **B008** iç benlik — iç benlik; kişinin kendisi
  الكذوب النفس (jamhara)
- **B009** dokuma bezemesi sanısı veren boyalı kumaş — dokuma bezemesi sanısı veren boyalı veya desenli kumaş
  الكذابة ثوب يصبغ بألوان الصبغ كأنه موشي (ayn); الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله (mufradat)

## ع س ر (root_001012): 92:10 لِلْعُسْرَىٰ

- **B001** güçlük ve çetinlik — güçlük, çetinlik; kolaylığın karşıtı · zorlaşmak, çetin hale gelmek · zor, çetin · zor ve çetin gün · kolaylaşmayan zor işler · zor olan veya kolay olanın karşıtı
  أصل صحيح واحد يدل على صعوبة وشدة (maqayis); العسر نقيض اليسر (maqayis;ayn;sihah;tahdhib;mufradat); أمر عسير ويوم عسير (maqayis;ayn;sihah;tahdhib;mufradat); العسرى الأمور التي تعسر ولا تتيسر (tahdhib)
- **B002** para darlığı — para darlığı, maddi sıkıntı · maddi darlık, parasızlık · maddi sıkıntı içinde olan kimse · varlıktan maddi darlığa düşmek
  الإقلال أيضا عسرة (maqayis); العسر قلة ذات اليد (ayn); العسرة قلة ذات اليد وكذلك الإعسار (tahdhib); العسرة تعسر وجود المال (mufradat); أعسر الرجل إذا صار من ميسرة إلى عسرة (maqayis)
- **B003** darlıktaki borçluyu sıkıştırmak — darlıktaki borçludan borcu katılıkla istemek · darlık zamanında benden bir şey istemek · alacak istemede ve işte katı davrananlar
  عسرته أنا أعسره إذا طالبته بدينك وهو معسر ولم تنظره إلى ميسرته (maqayis); عسرت الغريم أعسره إذا طلبت منه الدين على عسرته (sihah); عسرت الغريم أعسره عسرا إذا أخذته على عسرة ولم ترفق به (tahdhib); عسرني الرجل طالبني بشيء حين العسرة (mufradat)
- **B004** karşı çıkıp işi güçleştirmek — karşı çıkma ve dolambaçlılık · iş ona dolambaçlı ve güç gelmek · ona karşı çıkmak veya işi ona güçleştirmek · iş dolambaçlı ve güç hale gelmek · birbirlerine işi güçleştirmek · birinden elde edilmesi güç olan şeyi istemek
  العسر الخلاف والالتواء (maqayis;ayn); عسرت عليه تعسيرا إذا خالفته (maqayis); عسر عليه الأمر أي التاث (sihah); عسرت على فلان الأمر تعسيرا (tahdhib); استعسرت فلانا إذا طلبت معسوره (tahdhib); تعاسر القوم طلبوا تعسير الأمر (mufradat)
- **B005** sol taraf ve sola özgü olma — sol taraf · solak, sol eliyle çalışan · iki elini de kullanabilen · soluma gelmek · sol yanında fazla tüy veya beyazlık bulunan kartal · sol kanadında beyazlık bulunan güvercin
  العسرى خلاف اليسرى (maqayis;sihah); الذي يعمل بشماله أعسر (maqayis); رجل أعسر بين العسر وامرأة عسراء (sihah;tahdhib); عقاب عسراء ريشها من الجانب الأيسر أكثر من الأيمن (sihah); حمام أعسر وعقاب عسراء بجناحه من يساره بياض (sihah;tahdhib)
- **B006** güç doğum yapmak — kadının doğumu güçleşmek · doğumu güç olsun ve kız doğursun diye beddua etmek
  أعسرت المرأة إذا عسر عليها ولادها (maqayis;sihah;tahdhib); أعسرت وآنثت (maqayis;tahdhib); أيسرت وأذكرت (maqayis;tahdhib)
- **B007** o yıl gebe kalmayan deve — o yıl çiftleştiği halde gebe kalmayan deve
  العسير الناقة التي اعتاطت واعتاصت فلم تحمل عامها (maqayis); العسير الناقة إذا اعتاطت عامها فلم تحمل (sihah); تفسير الليث للعسير أنها الناقة التي اعتاطت غير صحيح (tahdhib)
- **B008** hazır olmadan zorlayıp kullanmak veya almak — eğitilmeden binilen deve · eğitilmeden önce binilen deve · zorla almak · oğlu istemediği halde malından almak · sözü hazırlamadan doğaçlama söylemek
  الناقة التي تركب قبل أن تراض عوسرانية (maqayis); العسير الناقة التي لم ترض وقد اعتسرتها إذا ركبتها قبل أن تراض (sihah); اعتسره مثل اقتسره (sihah); العسير الناقة التي ركبت قبل تذليلها (tahdhib); يعتسر الرجل من مال ولده معناه يأخذ من ماله وهو كاره (tahdhib); اعتسرت الكلام إذا اقتضبته قبل أن تزوره وتهيئه (tahdhib)
- **B009** koşarken kuyruğunu kaldırmak — koşarken kuyruğunu kaldırıp büken deve · koşarken kuyruğunu kaldıran deve · koşarken kuyruklarını kaldıran veya büken develer ya da kurtlar
  العاسر من النوق إذا عدت رفعت ذنبها (maqayis); عسرت الناقة بذنبها إذا شالت به (sihah); العاسرة من النوق فهي التي إذا عدت رفعت ذنبها (tahdhib); عواسر الذئاب التي تعسل في عدوها وتكسر أذنابها (tahdhib); ناقة عوسرانية إذا كان من دأبها تكسير ذنبها ورفعه إذا عدت (tahdhib)
- **B010** uğursuz gün [kalıp] — uğursuz gün
  يوم أعسر أي مشئوم (tahdhib)
- **B011** dağınık veya art arda ilerleme — dağınık halde veya birbiri ardınca
  ذهبت الإبل عساريات وعشاريات إذا انتشرت وتفرقت (tahdhib); جاءوا عساريات وعسارى أي بعضهم في إثر بعض (tahdhib)
- **B012** cin topluluğu veya yer adı — bir cin topluluğunun adı · cin topluluğu, cinlerin yaşadığı arazi veya yer adı
  العسرة قبيلة من قبائل الجن (tahdhib); عسر قبيلة من الجن (tahdhib); عسر أرض يسكنها الجن (tahdhib); عسر موضع (tahdhib)
- **B013** çubuk atıp dikili çubuğu çıkarma oyunu — dikili çubuğa başka çubuk atıp onu yerinden çıkarma oyunu
  العسر لعبة لهم ينصبون خشبة ثم ترمى بخشبة أخرى وتقلع (tahdhib)

## م و ل (root_001457): 92:11 مَالُهُۥٓ, 92:18 مَالَهُۥ

- **B001** varlık; edinme, çoğalma ve başkasına kazandırma — kişinin sahip olduğu değerli varlık · kişinin sahip olduğu değerli varlıklar · göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri · varlık sahibi veya çok varlıklı kimse · kendine kalıcı varlık edinmek · varlığı çoğalmak veya varlık sahibi duruma gelmek · birini varlık sahibi yapmak veya ona değerli varlık vermek · mal sözcüğünün küçültme biçimi · ne çok varlığı var!
  تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)
- **B002** örümcek için tartışmalı bir ad — 
  إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)

## ر د ي (root_000558): 92:11 تَرَدَّىٰٓ

- **B001** taş atma ve taş kırma taşı — ona taş attı · taşı bir kaya ya da kazmayla vurarak kırdı · atmak veya başka taşları kırmak için kullanılan taş · atılan taş · kaya · kayalar · bir topluluk adına taş atarak karşı koydu
  رديته بالحجارة أرديه رميته (maqayis); المردى حجر يرمى به (sihah); المرداة الحجر الذي يرمى به (tahdhib); المرداة حجر تكسر بها الحجارة فترديها (mufradat)
- **B002** atın özel hızlı gidişi, insanın tek ayaklı sekmesi ve karganın sekmesi — at koşu ile sert yürüyüş arasında hızla gitti · eşeğin bağlandığı yerle yuvarlandığı yer arasındaki koşusu · çocuk bir ayağını kaldırıp ötekiyle sıçradı · genç kızlar oyun oynarken tek ayak üzerinde sektiler · karga sekerek yürüdü · deve ve filin ağır, sert basan bacakları
  ردى الفرس أسرع (maqayis); ردى الفرس بين العدو والمشى الشديد (sihah); الجواري يردين إذا رفعت إحداهن رجلها ومشت على رجل (tahdhib); الغراب يردي إذا حجل (tahdhib)
- **B003** düşerek ya da başka yolla ölme, yok olma veya yok etme — ölüm ve yok oluş · öldü veya yok oldu · onu öldürdü veya yok etti · uçuruma yuvarlanma ve ölüm tehlikesine girme · kuyuya düştü · dağdan aşağı yuvarlandı · nereye gittiğini bilmiyorum · kendini ölüm tehlikelerine atan kişi · kötü ve tiksindirici şey
  الردى وهو الهلاك (maqayis); أرداه الله أهلكه (maqayis); ردى في البئر وتردى إذا سقط في بئر (sihah); التردي هو التهور في مهواة (tahdhib); الردى الهلاك والتردي التعرض للهلاك (mufradat)
- **B004** omuz giysisi, onu giyme ve örten ya da bezeyen şey — omuzlara alınan dış giysi · omuz giysisini giydi · omuz giysisini güzel taşıma biçimi · iyiliği bol ve eli açık · borcu veya yükümlülüğü az · boyna bağlı bir yükümlülük olarak borç · askılarıyla omuzda taşınan kılıç · çapraz takılan kuşak · genç kız çapraz kuşak taktı · gençliğin güzelliği, canlılığı ve esenliği
  الرداء الذي يلبس (maqayis); تردى وارتدى بمعنى أي لبس الرداء (sihah); يسمى الدين رداء (tahdhib); كل ما زينك فهو رداؤك (tahdhib)
- **B005** belirli bir ölçünün üstüne ekleme — ellinin üzerine çıktı · ellinin üstüne ekledi · artış veya eklenen pay · verdiğin ek pay · sözüne yaptığın ek
  أردى على الخمسين إذا زاد عليها (maqayis); رديت على الخمسين وأرديت أي زدت (sihah); الردى الزيادة (tahdhib); ردى عطائك أي زيادتك في العطية (tahdhib)
- **B006** yumuşakça razı etmeye çalışma ve idare etme — adamı yumuşakça razı etmeye çalıştı veya idare etti · gemin ağızlık parçası için yumuşakça pazarlık edilir
  يرادى على فأس اللجام (maqayis;sihah;tahdhib); فليس هذا من الباب لأن هذا مقلوب ومعناه يراود (maqayis); راداه بمعنى داراه (sihah); راديت الرجل وداجيته وداليته وفانيته بمعنى واحد (tahdhib)

## ه د ي (root_001583): 92:12 لَلْهُدَىٰ

- **B001** doğru yolu gösterme ve doğruya yönelme — doğru yol, doğruyu gösterme ve açıklama · ona yolu gösterip tanıttım · doğru yolu kabul edip buldu · yol gösteren, doğruya çağıran kimse
  الهدى نقيض الضلالة؛ هدي فاهتدى (ayn;tahdhib)؛ الهدى الرشاد والدلالة؛ هداه الله للدين هدى؛ أولم يبين لهم؛ هديته الطريق والبيت هداية أي عرفته (sihah)؛ الهدى البيان وإخراج شيء إلى شيء والطاعة والورع؛ دله على الطريق (tahdhib)؛ الهداية دلالة بلطف؛ تعريف الطرق؛ التوفيق (mufradat)؛ التقدم للإرشاد؛ هديته الطريق هداية؛ الهدى خلاف الضلالة (maqayis)
- **B002** yön, izlenen yol ve tutum — işin yönü, doğrultusu ve amacı · bir kimsenin gidişi, tutumu ve yöntemi · onun benzeri veya onu yeniden yapma
  خذ في هديتك أي فيما كنت فيه من الحديث أو العمل ولا تعدل عنه؛ هدية أمره وسيرته؛ هدى هدي فلان أي سار سيرته (sihah)؛ هدية أمره أي جهة أمره؛ هديت به أي قصدت به؛ هديه أي سمته؛ ليس لهذا الأمر هدية ولا قبلة ولا دبرة ولا وجهة؛ هدياها أي مثلها أو أعاودك (tahdhib)؛ هدية فلان وهديه أي طريقته (mufradat)؛ نظر فلان هدي أمره أي جهته؛ ما أحسن هديته أي هديه؛ رميت بآخر هدياه أي قصده (maqayis)
- **B003** bir şeyin ilk veya öndeki bölümü — bir şeyin ilki veya öndeki bölümü · atların boyunları ya da ilk sırası; yaban hayvanlarının öncüleri · okun ucu ve koyunun boynu
  الهادي من كل شيء أوله؛ هوادي الخيل أعناقها أو أول رعيل؛ العصا هاديا لأنها تتقدمه؛ الدليل يسمى هاديا لتقدمه (ayn)؛ هادي السهم نصله؛ الهادي العنق؛ هوادي الخيل أعناقها أو أول رعيل؛ الهاديات أوائل الوحش (sihah)؛ الهادية من كل شيء أوله وما تقدم منه؛ هادية الشاة الرقبة؛ هوادي الخيل أعناقها أو أول رعيل؛ هاديات الوحش أوائلها (tahdhib)؛ هوادي الوحش متقدماتها الهادية لغيرها (mufradat)؛ كل متقدم لذلك هاد؛ هوادي الخيل أعناقها؛ هاديها أول رعيل؛ الهادية العصا لأنها تتقدم ممسكها (maqayis)
- **B004** incelik göstergesi armağan verme — yakınlık ve incelik göstergesi armağan · armağan gönderdi veya verdi · karşılıklı armağanlaşma · armağanın sunulduğu tabak · sık sık armağan veren kimse
  الهدية ما أهديت إلى ذي مودة من بر (ayn)؛ الهدية واحدة الهدايا؛ أهديت له وإليه؛ المهدى ما يهدى فيه؛ التهادي أن يهدي بعضهم إلى بعض؛ المهداء الذي من عادته أن يهدي (sihah)؛ أهديت الهدية إهداء؛ امرأة مهداء؛ المهدى الطبق الذي يهدى عليه (tahdhib)؛ الهدية مختصة باللطف؛ المهدى الطبق؛ المهداء من يكثر إهداء الهدية (mufradat)؛ الهدية ما أهديت من لطف إلى ذي مودة؛ المهدي الطبق تهدى عليه (maqayis)
- **B005** kutsal yere adanan hayvan, mal veya eşya — kutsal bölgeye adanan hayvan, mal veya eşya · adanmış sunu adından genişleyen deve adı
  الهدي والهدي ما أهديت إلى مكة؛ كل شيء تهديه من مال أو متاع فهو هدي (ayn)؛ الهدي ما يهدى إلى الحرم من النعم؛ مالى هدي؛ حتى يبلغ الهدى محله (sihah)؛ أهديت الهدي إلى بيت الله؛ الهدي خفيف وعليه هدية أي بدنة؛ ما يهدى إلى مكة من النعم وغيره من مال أو متاع؛ العرب تسمي الإبل هديا (tahdhib)؛ الهدي مختص بما يهدى إلى البيت؛ فما استيسر من الهدي؛ هديا بالغ الكعبة (mufradat)؛ الهدي والهدي ما أهدي من النعم إلى الحرم قربة إلى الله تعالى (maqayis)
- **B006** gelini eşinin yanına götürme — gelini eşinin yanına götürdü · gelinin eşinin yanına götürülmesi · eşine götürülen gelin
  الهداء مصدر قولك هديت المرأة إلى زوجها؛ وهي مهدية وهدي (sihah)؛ هديت العروس فأنا أهديها هداء؛ أهدى الرجل امرأته جمعها إليه وضمها؛ المرأة سميت هديا لأنها كالأسيرة عند زوجها أو لأنها تهدى إلى زوجها (tahdhib)؛ الهدي يقال في العروس؛ هديت العروس إلى زوجها (mufradat)؛ الهدى العروس وقد هديت إلى بعلها هداء (maqayis)
- **B007** dokunulmaz sığınmacı; kimi açıklamalarda tutsak — dokunulmaz sığınmacı; kimi açıklamalarda tutsak
  الرجل الذي له حرمة كحرمة هدي البيت؛ يقال للأسير أيضا هدي (sihah)؛ الهدي الرجل ذو الحرمة وهو أن يأتي القوم يستجيرهم أو يأخذ منهم عهدا؛ يقال للأسير أيضا الهدي (tahdhib)؛ وقيل الهدي الأسير (maqayis)
- **B008** sallanarak, gerektiğinde başkalarına dayanarak yürüme — güçsüzlükten iki kişiye dayanarak yürümek · yürürken sağa sola sallandı
  التهادي مشي في تمايل يمينا وشمالا كمشي النساء والإبل الثقال (ayn)؛ يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله؛ المرأة إذا تمايلت في مشيتها قيل تهادى (sihah)؛ يهادى بين اثنين معناه يعتمد عليهما من ضعفه وتمايله؛ هي تهادى إذا تمايلت في مشيها (tahdhib)؛ يهادي بين اثنين إذا مشى بينهما معتمدا عليهما؛ تهادت المرأة إذا مشت مشي الهدي (mufradat)؛ جاء فلان يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما (maqayis)
- **B009** bön, güçsüz ve ağır kimse — bön, güçsüz, ağır ve uyuşuk adam
  الهداء الرجل البليد الضعيف (ayn)؛ رجل هداء وهدان للثقيل الوخم (tahdhib)
- **B010** sakin, ölçülü ve düzgün ilerleyiş — sakinlik ve güzel, telaşsız tutum
  الهدي السكون؛ ما هدى هدي مهزوم؛ لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن (ayn)؛ الهدي السكون؛ لم يسرع إسراع المنهزم ولكن على سكون وحسن هدي (tahdhib)
- **B011** övgü veya yergi şiiri sunma ve şiirle yergileşme — birine övgü veya yergi şiiri sunma · şiirle karşılıklı yergileşme
  الإهداء أن تهدي إلى إنسان مديحا أو هجاء شعرا (ayn)؛ هاداني فلان الشعر وهاديته أي هاجاني وهاجيته (tahdhib)

## ECHO ه د د (root_001580): for 92:12 لَلْهُدَىٰ: withheld observed target; not identity

- **B001** agir kirip yikma — kirip yikmak, sarsip bozmak · agir yikim ve kirilma · kirilip yikilmak · bir felaketin kisiyi sarsip gucunu kirmasi · yer cokmesi ya da yikima benzer agir olay
  أصل صحيح يدل على كسر وهضم وهدم (maqayis)؛ الهد الهدم الشديد (ayn;tahdhib)؛ هددت الحائط إذا هدمته (jamhara)؛ هد البناء يهده هدا كسره وضعضعه (sihah;tahdhib)؛ انهد الجبل أي انكسر (sihah)؛ الهدة الخسوف والهد الهدم (tahdhib)؛ هد ركني إذا بلغ منه وكسره (tahdhib)
- **B002** zayif ve korkak kisi — zayif veya korkak adam · korkak veya zayif adam · korkak adam · korkak topluluk · birini zayif saymak · zayif olmayan
  الهد من الرجال الضعيف كأنه هد (maqayis)؛ رجل هد جبان (jamhara)؛ رجل هد وأهد بمعنى الجبن والضعف (jamhara)؛ الهد الرجل الضعيف (sihah;tahdhib)؛ الهد بالكسر الجبان الضعيف (sihah;tahdhib)؛ استهددت فلانا أي استضعفته (tahdhib)
- **B003** cömert ve guclu kisi — cömert, degerli veya guclu adam · adam gucu ve dayanikliligiyla ovulmek · adami dayanikli diye ovmek
  الهد من الرجال الجواد الكريم (maqayis;tahdhib)؛ الهد الكريم الهاد لماله (maqayis)؛ فلان يهد إذا أثني عليه بالجلد والقوة (sihah)؛ لهد الرجل إذا أثني عليه بالجلد والشدة (tahdhib)؛ هد الرجل جلد الرجل (tahdhib)
- **B004** siddetli ugultu — duvar, kose veya dag dusmesinin siddetli sesi · deniz tarafindan duyulan siddetli ugultu · gok gurultusu · ses ve ugultu · kumru veya erkek devenin gurleyis ugultusu
  الهدة صوت وقع الحائط (maqayis;sihah)؛ الهدة صوت تسمعه من سقوط ركن أو ناحية جبل (ayn;tahdhib)؛ الهاد صوت شديد يسمعه أهل السواحل (ayn;sihah;tahdhib)؛ ما سمعنا العام هادة أي رعدا (jamhara)؛ هدهد الحمام صوت (maqayis)؛ الفحل يهدهد في هديره (ayn;sihah;tahdhib)؛ الهديد والغديد الصوت (tahdhib)
- **B005** ibibik kusu — ibibik kusu · ibibik veya guvercine benzetilen kus adlari
  الهدهد معروف (maqayis;tahdhib)؛ الهدهد طائر والهداهد مثله (sihah)؛ الهداهد طائر يشبه الحمام (tahdhib)؛ هداهد تصغير هدهد (tahdhib)
- **B006** uyutmak icin sallama [kalıp] — cocugu uyusun diye sallamak
  هدهدت المرأة ابنها حركته لينام (maqayis;sihah)؛ الهدهدة تحريك الأم ولدها لينام (tahdhib)؛ يهدهد الصبي (tahdhib)
- **B007** ovgu yeterlik kalibi — bir erkegi 'ona diyecek yok' anlaminda oven kalip
  مررت برجل هدك من رجل كقولهم حسبك من رجل (maqayis)؛ هدك فلان من رجل أي حسبك به (jamhara)؛ مررت برجل هدك من رجل معناه أثقلك وصف محاسنه (sihah)؛ مررت برجل هدك من رجل فهو بمعنى حسبك وهو مدح (tahdhib)
- **B008** agir basarak yurume [kalıp] — yururken yere cok sert basmak
  فلان يهد الأرض في مشيه إذا جاء يطأ وطأ شديدا (jamhara)
- **B009** sarp inisli gecit — sarp inisli tepe veya zorlu gecit
  أكمة هدود صعبة المنحدر وربما تردت الإبل منها (jamhara)؛ الهدود العقبة الشاقة (tahdhib)
- **B010** gozdagi vererek korkutma — gozdagi verme ve korkutma · korkutma ve gozdagi verme · gozdagi verme · uzaktan savrulan gozdagi
  التهديد التخويف وكذلك التهدد (sihah)؛ التهدد والتهديد والتهداد من الوعيد (tahdhib)؛ يقال للوعيد من وراء وراء الفديد والهديد (tahdhib)
- **B011** kesinlesmemis sani [kalıp] — kisinin icine kesinlesmemis bir sani gibi belirmek
  يقال يهدهد إلي كذا إذا شبه للإنسان في نفسه بالظن ما لم يثبته ولم يعقد عليه التشبيه (tahdhib)
- **B012** uzun boylu adam — uzun boylu adam
  الهديد الرجل الطويل (tahdhib)

## ء خ ر (root_000019): 92:13 لَلْءَاخِرَةَ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## ء و ل (root_000067): 92:13 وَٱلْأُولَىٰ

- **B001** başlangıç ve öncelik — ilk; önde gelen · ilk olan kadın ya da dişil şey · ilkler; öncekiler · topluluğun önünde bulunma · sürünün önünde giden dişi ya da erkek deve · önceki yıl · her şeyden önce
  الأول وهو مبتدأ الشيء؛ ناقة أولة وجمل أول إذا تقدما الإبل (maqayis)؛ أول في اللغة على الحقيقة ابتداء الشيء؛ جاء فلان في أولية الناس إذا جاء في أولهم (tahdhib)
- **B002** sonuca dönme ve varma — geri dönmek; sonunda bir duruma varmak · hükmü sahiplerine geri vermek · bedeni zayıflamak · sözün sonucu veya anlamının açıklanması · açıklamak; anlamına döndürmek · onunla ilgili ödülü gözetmek ve aramak
  آل يؤول أى رجع؛ تأويل الكلام وهو عاقبته وما يؤول إليه (maqayis)؛ التأويل تفسير ما يؤول إليه الشئ؛ آل أي رجع (sihah)؛ آل يؤول أي رجع وعاد؛ التأويل المرجع والمصير (tahdhib)
- **B003** aile ve bağlı çevre — kişinin ailesi, ev halkı ve yakınları · onun izleyicileri ve bağlıları · kişinin sığındığı ev halkı · kişinin kökü ve bağlı olduğu aile
  آل الرجل أهل بيته؛ لأنه إليه مآلهم وإليهم مآله (maqayis)؛ آل الرجل أهله وقرابته (jamhara)؛ آل الرجل أهله وعياله؛ وآله أيضا أتباعه (sihah)؛ إلة الرجل أهل بيته؛ إيلة الرجل فهم أصله الذين يؤول إليهم (tahdhib)
- **B004** iyi yönetip düzene koyma — iyi yönetme ve gözetme · yöneticinin halkını iyi yönetip gözetmesi · malını düzeltip iyi yönetmek · düzeltme ve iyi yönetme · Tanrı işini toparlayıp düzeltsin
  الإيالة السياسة؛ آل الرجل رعيته يؤولها إذا أحسن سياستها (maqayis)؛ الايالة السياسة؛ آل الأمير رعيته يؤولها أولا وإيالا؛ آل ما له أي أصلحه وساسه (sihah)؛ ألت الشيء جمعته وأصلحته؛ أول الله عليك أمرك أي جمعه (tahdhib)
- **B005** koyulaşıp pıhtılaşma — sütün koyulaşıp pıhtılaşması · katranın veya balın koyulaşıp katılaşması · pıhtılaşmış süt
  آل اللبن أي خثر؛ لا يخثر إلا آخر أمره؛ آل القطران إذا خثر (maqayis)؛ آل القطران أو العسل إذا أعقد بالنار (jamhara)؛ آل القطران والعسل أي خثر؛ الآيل اللبن الخاثر (sihah)
- **B006** görünür siluet ve dış uçlar — görünür siluet; uzaktan beliren görüntü · adamın görünen silueti · dağın uçları ve yanları
  آل الرجل شخصه؛ آل كل شيء؛ آل الجبل أطرافه ونواحيه (maqayis)؛ الآل السراب؛ آل كل شيء شخصه (jamhara)؛ الآل الشخص؛ الآل الذي تراه في أول النهار وآخره كأنه يرفع الشخوص وليس هو السراب (sihah)
- **B007** içinde bulunulan durum — içinde bulunulan durum
  الآلة الحالة (maqayis)؛ والآلة الحالة (jamhara)؛ والآلة الحالة يقال هو بآلة سوء (sihah)
- **B008** araç ve taşıyıcı düzen — araç · çadır direkleri ve taşıyıcı ağaçları · cenaze veya ölüyü taşıyan sedye
  آل الخيمة العمد (maqayis)؛ الآلة الأداة؛ خشبات تبنى عليها الخيمة؛ الآلة الجنازة (sihah)
- **B009** erkek yabani dağ keçisi — erkek yabani dağ keçisi
  الأيل الذكر من الوعول؛ لأنه يؤول إلى الجبل يتحصن (maqayis)؛ الايل أيضا الذكر من الاوعال (sihah)
- **B010** içecek olgunlaştırma kabı — içecek olgunlaştırma kabı
  الإيال على فعال وعاء يجمع فيه الشراب اياما حتى يجود (maqayis)
- **B011** kumda yetişen yem bitkisi — kumda yetişen bir yem bitkisi
  التأويل نبت يعتلفه الحمار؛ التأويل اسم بقلة يولع بها بقر الوحش تنبت في الرمل (tahdhib)

## و ل ي (root_001684): 92:16 وَتَوَلَّىٰ (also echo for 92:13 وَٱلْأُولَىٰ)

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

## ن ذ ر (root_001488): 92:14 فَأَنذَرْتُكُمْ

- **B001** tehlikeyi bildirerek sakındırma — uyarı amacıyla korkulacak bir şeyi bildirme · bir topluluğa korkulacak bir durumu haber verip sakındırmak · uyaran kişi veya uyarının kendisi · uyaranlar ya da uyarılar · birbirini korkutucu bir tehlikeye karşı uyarmak · düşmandan haberdar olup hazırlık ve sakınma durumuna geçmek · ani tehlikeyi haber veren kişi için kullanılan temsil · önceden ceza veya sonuç bildiren kişinin gerekçesini tamamladığını anlatan söz · ordunun düşman durumunu bildiren öncü gözcüsü
  الإنذار الإبلاغ ولا يكاد يكون إلا في التخويف؛ تناذروا خوف بعضهم بعضا؛ النذير المنذر والجمع النذر (maqayis)؛ الانذار الابلاغ ولايكون إلا في التخويف؛ النذير المنذر؛ تناذر القوم كذا أي خوف بعضهم بعضا؛ نذر القوم بالعدو إذا علموا (sihah)؛ الإنذار الإعلام بالشيء الذي يحذر منه؛ أنذرت القوم مسير عدوهم إليهم فنذروا أي علموا فتحرزوا؛ أنا النذير العريان (tahdhib)؛ الإنذار إخبار فيه تخويف؛ النذير المنذر؛ النذر جمعه؛ وقد نذرت أي علمت ذلك وحذرت (mufradat)
- **B002** kendine adak yükümlülüğü koyma — kişinin kendi üzerine sonradan gerekli kıldığı adak yükümlülüğü · kendi üzerine bir şeyi gerekli kılmak veya şarta bağlı söz vermek · Tanrı için kendi üzerine bir yükümlülük almak · kendi üzerine adak yükümlülüğü almak · adak yoluyla ibadethane hizmetine ayrılan çocuk
  النذر وهو أنه يخاف إذا أخلف؛ النذر أيضا ما يجب كأنه نذر أي أوجب (maqayis)؛ النذر واحد النذور؛ نذرت لله كذا؛ نذر على نفسه نذرا (sihah)؛ النذر ما ينذره الإنسان فيجعله على نفسه نحبا واجبا؛ نذرت على نفسي أي أوجبت؛ النذر ما كان وعدا على شرط (tahdhib)؛ النذر أن توجب على نفسك ما ليس بواجب لحدوث أمر؛ نذرت لله أمرا (mufradat)
- **B003** yaralama için gereken tazminat — yaralamalarda ödenmesi gereken tazminat veya kan bedeli · kemiği açığa çıkaran yara için gereken tazminat
  نذر الموضحة في الحديث منه (maqayis)؛ ما يجب في الجراحات من الديات نذرا؛ أهل العراق يسمونه الأرش؛ النذور لا تكون إلا في الجراح صغارها وكبارها؛ لي قبل فلان نذر إذا كان جرحا واحدا له عقل؛ نصف نذر الموضحة (tahdhib)

## ن و ر (root_001564): 92:14 نَارًا

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

## ل ظ ي (root_001357): 92:14 تَلَظَّىٰ

- **B001** saf alev ve ateşin alevlenip harlanması — ateş; saf alev · ateşin tutuşup alevlenmesi · alevlenmek, parlayıp harlanmak · ateş tutuşup alevlendi
  اللظى النار (sihah)؛ التظاء النار التهابها وتلظيها تلهبها (sihah)؛ تلظت النار تلظيا إذا التهبت (tahdhib)؛ اللظى اللهب الخالص (tahdhib;mufradat)؛ نارا تلظى أي تتوهج وتتوقد (tahdhib)؛ لظيت النار تلظى لظى (tahdhib)؛ لظيت النار وتلظت (mufradat)
- **B002** tam çekimlenmeyen, ateşin ve öte dünyadaki ateşli ceza yerinin özel adı — ateşin ya da öte dünyadaki ateşli ceza yerinin tam çekimlenmeyen özel adı
  لظى اسم من أسماء النار معرفة لا ينصرف (sihah)؛ لظى من أسماء النار وهي معرفة لا تنون لأنها لا تنصرف (tahdhib)؛ لظى غير مصروفة اسم لجهنم (mufradat)
- **B003** birine karşı öfkeden parlamak [kalıp] — birine karşı yoğun öfkeden parlamak
  فلان يتلظى على فلان تلظيا إذا توقد عليه من شدة الغضب (tahdhib)
- **B004** şiddetli sıcaklık — şiddetli sıcaklık
  جعل ذو الرمة اللظى شدة الحر (tahdhib)

## ص ل ي (root_000880): 92:15 يَصْلَىٰهَآ

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

## ECHO ص ل و (root_000879): for 92:15 يَصْلَىٰهَآ: withheld observed target; not identity

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

## ش ق و (root_000808): 92:15 ٱلْأَشْقَى

- **B001** mutluluğun karşıtı olan mutsuzluk — mutsuzluk, bahtsızlık · mutsuz, bahtsız kimse · Tanrı onu mutsuzluğa düşürdü
  الشقوة خلاف السعادة (maqayis)؛ الشقاء والشقاوة بالفتح: نقيض السعادة (sihah)؛ الشقاوة: خلاف السعادة، والشقاوة الأخروية والدنيوية (mufradat)
- **B002** güçlük çekme ve zorluğa dayanma — güçlük, sıkıntı ve yorucu uğraş · bu işte yoruldum ve güçlük çektim · zorluğa katlanma, uğraşıp dayanma ve savaşta boğuşma · onunla uğraştım ve güçlüğüne katlandım · o işle uğraşıp güçlüğünü çektim
  أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (maqayis;sihah)؛ الشقاء: الشدة والعسر، وشاقيته أي صابرته، وشاقيت ذلك الأمر بمعنى عانيته، والمشاقاة: المعالجة في الحرب وغيرها (tahdhib)؛ يوضع الشقاء موضع التعب، وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)
- **B003** karşılıklı uğraşta ötekini yenme [kalıp] — benimle çekişti, ben de o işte onu yendim
  شاقاني فلان فشقوته أشقوه، أي غلبته فيه (sihah)
- **B004** uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı — uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı; bu tür dağ sırtları
  الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)

## ECHO ش ق ي (root_000809): for 92:15 ٱلْأَشْقَى: withheld observed target; not identity

- **B001** bedbahtlık ve bedbaht duruma düşürme — bedbaht olmak · bedbahtlık · bedbahtlık · bu dünyada veya ölümden sonraki yaşamda bedbahtlık · onu bedbaht duruma düşürmek
  الشقوة خلاف السعادة (maqayis)؛ شقي شقاء وشقوة وأصل الشقاء والشقوة (ayn)؛ الشقاء والشقاوة نقيض السعادة وأشقاه الله (sihah)؛ شقي شقاء وشقاوة وشقوة (tahdhib)؛ الشقاوة خلاف السعادة (mufradat)
- **B002** zorluk ve yorucu uğraş — güçlük, zorluk ve yorucu sıkıntı · bir işte yorulmak veya güçlük çekmek · uğraşma, yaşayarak sürdürme ve katlanma · bir işle uğraşmak ve ona katlanmak
  أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (sihah)؛ الشقاء الشدة والعسر وشاقيت ذلك الأمر بمعنى عانيته (tahdhib)؛ يوضع الشقاء موضع التعب وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)
- **B003** biriyle karşılıklı uğraşıp mücadele etme — biriyle ilişki kurup ona karşı direnmek veya onunla uğraşmak · benimle çekişti, ben de onu o işte yendim
  المشاقاة المعاناة والممارسة (maqayis;sihah)؛ شاقاني فلان فشقوته أي غلبته فيه (sihah)؛ شاقيت فلانا مشاقاة إذا عاشرته وعاشرك (tahdhib)؛ شاقيته أي صابرته والمشاقاة المعالجة في الحرب وغيرها (tahdhib)
- **B004** kolay çıkılan, oturmaya elverişli uzun dağ sırtı — kolay çıkılan ve oturmaya elverişli uzun dağ sırtı
  الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)

## ج ن ب (root_000262): 92:17 وَسَيُجَنَّبُهَا

- **B001** bedenin veya şeyin yanı ve bitişik çevresi — insanın veya hayvanın böğrü · yan, taraf · evin önü veya topluluğun yerleşimine bitişik çevre · vadinin, ordunun veya ırmağın iki yanı · devenin böğür derisinden alınan parça · ordunun sağ ve sol kanadı
  أصل الجنب الجارحة وجمعه جنوب (mufradat)؛ الجنب للإنسان وغيره (maqayis)؛ الجانب والجوانب معروفة والجنبتان ناحيتا كل شيء (ayn)؛ الجنب معروف والجانب الناحية (sihah)؛ جنبتا الوادي ناحيتاه وجناب القوم ما حولهم (tahdhib)؛ جنب الإنسان والدابة معروف وأعطني جنبة جلد جنب بعير (jamhara)
- **B002** yanında yakın bulunma ve eşlik etme — yaklaşması ve ilişki kurması kolay · yol arkadaşı veya yakın eşlikçi · Tanrı'ya yakınlıkta veya Tanrı'nın buyruğu ve yolu üzerinde · kardeşin hakkında, özellikle onu çekiştirme konusunda
  رجل لين الجانب والجنب أي سهل القرب (ayn;tahdhib)؛ الصاحب بالجنب صاحبك في السفر (sihah)؛ الجنب القرب وفي قرب الله وجواره (tahdhib)؛ في أمره وحده الذي حده لنا (mufradat)
- **B003** uzak durma veya uzaklaştırma — uzak durmak, sakınmak veya bırakmak · birini bir şeyden uzaklaştırmak veya kötülükten korumak · beni ve çocuklarımı putlara tapmaktan uzak tut · insanlardan ayrı bir yerde durma · akrabalıkta, soyda veya yerleşimde uzak olan yabancı · başka bir topluluktan gelip akrabalığı bulunmayan komşu · uzaktan ve yabancı olarak · birini iyilikten yoksun bırakmak
  الأصل الآخر البعد والجنابة (maqayis)؛ جنبته عن كذا فاجتنب أي تجنبه وجنبته أي دفعت عنه مكروها (ayn)؛ الجناب مصدر جانبته مجانبة وهو من المباعدة (jamhara)؛ جانبه وتجانبه وتجنبه واجتنبه كله بمعنى وجنبته الشيء أي نحيته عنه (sihah)؛ أجنب تباعد والجنابة ضد القرابة (tahdhib)؛ جنبته عن كذا أي أبعدته واجتنبوا عبارة عن تركهم إياه (mufradat)
- **B004** cinsel ilişki sonrası arınma gerektiren dinsel durum — cinsel ilişkiden sonra arınana dek dinsel kısıt altında bulunan kişi · cinsel ilişki sonrası arınma gerektiren duruma girmek
  الجنب الذي يجامع أهله مشتق من هذا لأنه يبعد عن الصلاة والمسجد (maqayis)؛ أجنب الرجل إذا أصابته الجنابة (ayn;jamhara;sihah;tahdhib)؛ رجل جنب وامرأة جنب وقوم جنب (jamhara;sihah;tahdhib)؛ سميت الجنابة بذلك لكونها سببا لتجنب الصلاة في حكم الشرع (mufradat)
- **B005** yanında yönlendirerek götürme — hayvanı veya atı yanında yürütmek · tutsağı yürütmek veya hayvanın yanına bağlamak · yanda çekilerek götürülen hayvan · yarış atının yanında yedek bir at koşturma yasağı
  جنبت الدابة إذا قدتها إلى جنبك وكذلك جنبت الأسير (maqayis;jamhara)؛ الجنيبة كل دابة تقاد والجنيب الأسير مشدود إلى جنب الدابة (ayn)؛ جنبت الدابة إذا قدتها إلى جنبك ومنه خيل مجنبة (sihah)؛ جنبت الفرس أجنبه جنبا إذا قدته والجنيبة الدابة تقاد (tahdhib)؛ من جنبت الفرس كأنما سأله أن يقوده عن جانب الشرك (mufradat)
- **B006** güneyden esen yel — güney yeli · yelin güneyden esmesi veya topluluğun bu yele girip ona tutulması · güney yelinin sürüklediği bulut
  مما شذ عن الباب ريح الجنوب (maqayis)؛ الجنوب ريح تجيء عن يمين القبلة وقد جنبت الريح (ayn)؛ الجنوب ريح معروفة (jamhara)؛ الجنوب الريح التي تقابل الشمال (sihah)؛ الجنوب من الرياح حارة ومهبها ما بين مهبي الصبا والدبور (tahdhib)؛ الجنوب يصح أن يعتبر فيها معنى المجيء من جانب الكعبة (mufradat)
- **B007** böğür bölgesini tutan ağrı veya hastalık — böğrü ağrımak veya akciğer zarı hastalığına tutulmak · vurarak böğrünü incitmek veya kırmak · devenin aşırı susuzluktan akciğeri böğrüne yapışacak ölçüde hastalanması
  الجنب أن يشتد عطش البعير حتى تلتصق رئته بجنبه (maqayis)؛ أجنب فلان إذا أخذته ذات الجنب والجنيب الذي يشتكي جنبه (ayn)؛ جنب الرجل إذا اشتكى جنبه (jamhara)؛ المجنوب الذي به ذات الجنب وجنب البعير من شدة العطش (sihah)؛ ذات الجنب علة صعبة وجنب جنبا إذا اشتكى جنبه (tahdhib)؛ جنب شكا جنبه (mufradat)
- **B008** develerde sütün azalması veya tükenmesi — topluluğun develerinde sütün azalması veya tükenmesi · süt kıtlığı yaşanan yıl
  جنب القوم إذا قلت ألبانهم (maqayis;sihah)؛ جنب بنو فلان إذا لم يكن في إبلهم لبن (ayn;tahdhib)؛ جنب الرجل إذا قلت ألبان إبله (jamhara)؛ جنب بنو فلان إذا لم يكن في إبلهم اللبن (mufradat)
- **B009** çok miktarda iyilik veya kötülük [kalıp] — pek çok iyilik veya kötülük
  المجنب الخير الكثير كأنه إلى جنب الإنسان (maqayis)؛ شرا مجنبا وخيرا مجنبا أي كثيرا (ayn)؛ خيرا مجنبة ومجنبا وشرا مجنبا أي كثيرا (jamhara)؛ المجنب بالفتح الشيء الكثير وخيرا مجنبا وشرا مجنبا (sihah)؛ المجنب الخير الكثير والمجنب يقال في الشر إذا كثر (tahdhib)؛ جنب فلان خيرا وجنب شرا (mufradat)
- **B010** yazın kalan köklü küçük bitkiler — yazın kalan, köklü küçük bitki veya çalı
  الجنبة اسم يقع على عامة الشجر يترك في الصيف (ayn)؛ الجنبة ضرب من النبت (jamhara)؛ الجنبة اسم لكل نبت يتربل في الصيف (sihah)؛ الجنبة اسم واحد لنبوت كثيرة هي كلها عروة (tahdhib)
- **B011** yanı koruyan kalkan veya örtü — kişinin yanında taşıdığı kalkan veya koruyucu örtü
  سمي الترس مجنبا لأنه إلى جنب الإنسان (maqayis)؛ المجنب الترس (ayn;sihah;tahdhib)؛ المجنب الترس ويقال المجنب والمجنب الستر أيضا (jamhara)
- **B012** atın bacaklarında doğuştan ölçülü açıklık — atın bacaklarının doğuştan birbirinden ayrı durması, fakat aşırı ayrık olmaması
  التجنيب انحناء وتوتير في رجل الفرس (sihah)؛ المجنب من الخيل البعيد ما بين الرجلين من غير فجج والتجنيب بالجيم في الرجلين (tahdhib)؛ التجنيب الروح في الرجلين وذلك إبعاد إحدى الرجلين عن الأخرى خلقة (mufradat)

## ء ت ي (root_000009): 92:18 يُؤْتِى

- **B001** gelmek, ulaşmak — gelmek veya ulaşmak · ona gitmek veya yanına varmak · geciktiğini düşünüp gelmesini istemek
  أتى يأتي أتيا (jamhara)؛ الإتيان المجئ (sihah)؛ أتاني فلان إتيانا وأتيا وأتية وأتوة (tahdhib;maqayis)؛ الإتيان مجيء بسهولة (mufradat)
- **B002** vermek; getirip sunmak — vermek; bir şeyi getirip sunmak
  آتى يؤتي إيتاء في معنى أعطى (jamhara)؛ آتاه إيتاء أي أعطاه وآتاه أيضا أي أتى به (sihah)؛ الإتياء الإعطاء (tahdhib)؛ الإيتاء الإعطاء (mufradat;maqayis)
- **B003** uygun yoldan ele almak ve elverişli hale gelmek — işin uygun yönü ve tutulacak yolu · uyma ve razı olma · bir şeyin ona elverişli hale gelmesi · ihtiyacını uygun yoldan ve incelikle yürütmek
  أتيت الأمر من مأتاته (sihah;maqayis)؛ آتيته على ذلك الأمر مواتاة إذا وافقته وطاوعته (sihah)؛ آتيت فلانا على أمره مؤاتاة وهو حسن المطاوعة (maqayis)؛ تأتى له الشيء أي تهيأ (sihah)؛ تأتى فلان لحاجته إذا ترفق لها (tahdhib)
- **B004** su kanalı açmak ve akışı yönlendirmek — su kanalı; suyu tutan odun ve yaprak birikintisi · bu suya yol açıp akışını yönlendirmek
  أت لمائك أي سهل له سبيلا وذلك السبيل الأتي (jamhara)؛ الأتي الجدول يؤتيه الرجل إلى أرضه (sihah)؛ كل جدول ماء أتي (tahdhib)؛ أت لهذا الماء أي سهل جريه (maqayis)؛ الأتي ما وقع في النهر من خشب أو ورق مما يحبس الماء (maqayis)
- **B005** başka bölgeden gelen sel [kalıp] — yağmur alan başka bir bölgeden gelen sel
  الأتي السيل بعينه يأتيك من بلد مطر من غير بلدك (jamhara)؛ سيل أتي وأتاوي إذا جاءك ولم يصبك مطره (sihah)؛ المسيل الذي يأتي من بلد قد مطر فيه إلى بلد لم يمطر فيه أتي (tahdhib)؛ السيل المار على وجهه أتي وأتاوي (mufradat)؛ الأتي أيضا السيل الذي يأتي من بلد غير بلدك (maqayis)
- **B006** topluluğa yabancı kimse [kalıp] — içinde bulunduğu topluluğa mensup olmayan yabancı adam
  رجل أتي وأتاوي وهو الغريب (jamhara)؛ الاتي أيضا والاتاوى الغريب (sihah)؛ إنما هو أتي فينا (tahdhib)؛ به شبه الغريب فقيل أتاوي (mufradat)؛ رجل أتي أي غريب في قوم ليس منهم وأتاوي كذلك (maqayis)
- **B007** gelişip bol ürün vermek — ekin ve hurmanın gelişmesi, ürünü ve bol verimi · çalkalanan tulumun yağının ortaya çıkması
  أتاء هذا النخل أي ثمره وكذلك الزرع (jamhara)؛ الاتاء البركة والنماء وحمل النخل (sihah)؛ جاء أتوه (sihah;mufradat)؛ إتاء النخلة ريعها وزكاؤها وكثرة ثمارها (tahdhib)؛ الإتاء نماء الزرع والنخل وأتى الماء إتاء أي كثر (maqayis)
- **B008** ödenen vergi; rüşvet — vergi veya baş vergisi; rüşvet · ona rüşvet vermek
  الإتاوة الخراج أو الجزية يؤديه القوم إلى الملك (jamhara)؛ الاتاوة الخراج والجمع الاتاوي (sihah)؛ الإتاوة الخراج وجمعها الأتاوى والإتاوات (tahdhib)؛ أتوته أتوة إذا رشوته إتاوة وهي الرشوة (tahdhib)
- **B009** devenin ön ayaklarını geri getirişi [kalıp] — devenin yürürken ön ayaklarını geri getirişi
  ما أحسن أتو قوائم الناقة وأتيها في السير (jamhara)؛ ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير (sihah)؛ ما أحسن أتو يديها وأتي يديها يعني رجع يديها (tahdhib)
- **B010** işlek ana yol, son sınır ve karşı hizası — yarışın son sınırı; işlek ana yol veya yol kavşağı · yarışın son sınırı veya yolun ana kesimi · bir evin karşısında veya aynı hizasında
  الميتاء والميداء آخر الغاية حيث ينتهي إليه جري الخيل (sihah)؛ الميتاء الطريق العامر ومجتمع الطريق (sihah)؛ داري بميتاء دار فلان وميداء دار فلان أي تلقاء داره ومحاذية لها (sihah)؛ طريق ميتاء مسلوك وميتاء الطريق وميداؤه محجته (tahdhib)
- **B011** felakete uğramak, kaybetmek veya düşmanca ele geçirilmek [kalıp] — ölüm, ağır hastalık, bela veya kırığa uğramak · malı yok olmak · uğruna öldürülmek, götürülmek veya yenilmek · düşman yaklaşmış olmak
  أتى على فلان أتو أي موت أو بلاء أصابه (tahdhib)؛ الأتو المرض الشديد أو كسر يد أو رجل أو موت (tahdhib)؛ أتي على يد فلان إذا هلك له مال (tahdhib)؛ يؤتى دونه أي يذهب به ويغلب عليه (tahdhib)؛ أتي فلان إذا أطل عليه العدو (tahdhib)؛ الإتيان يقال في الخير وفي الشر (mufradat)
- **B012** dişi devenin çiftleşmek istemesi [kalıp] — dişi devenin çiftleşmek için erkek deve istemesi
  استأتت الناقة استئتاء مهموز أي ضبعت وأرادت الفحل (sihah)
- **B013** etkili ve işini yürüten adam [kalıp] — etkili ve işini yürütebilen adam
  رجل أتي إذا كان نافذا (maqayis)

## ز ك و (root_000637): 92:18 يَتَزَكَّىٰ

- **B001** büyüyüp artma — büyümek, artmak ve verim kazanmak · büyüme ve artış · gelişmiş ve artışı belirgin · Tanrı onu büyütüp artırdı · ekin büyüyüp arttı · kişi bolluğa kavuşup rahat yaşadı
  أصل يدل على نماء وزيادة (maqayis)؛ زكا الزرع يزكو زكاء ازداد ونما وكل شيء ازداد ونما فهو يزكو زكاء (ayn)؛ زكا الزرع يزكو زكاء ممدود أي نما (sihah)؛ كل شيء يزداد ويسمن فهو يزكو زكاء (tahdhib)؛ أصل الزكاة النمو الحاصل عن بركة الله تعالى (mufradat)
- **B002** ahlaken arınıp düzgünleşme — arınmak ve düzgünleşmek · temiz, doğru ve kötülükten sakınan · arındırıp düzeltmek · arındırma, düzeltme ve iyiliklerle geliştirme · iç temizliği ve ahlaki düzgünlük · kendini övmek veya sözle temiz saymak · dinen uygun ve sonu zarar vermeyen yiyecek · temizlik ve düzgünlük
  الطهارة زكاة المال؛ زكاة لأنها طهارة (maqayis)؛ والزكاة الصلاح؛ رجل زكي تقي (ayn)؛ معناه صلاحا؛ ما صلح؛ أي يصلح (tahdhib)؛ بزكاء النفس وطهارتها؛ حلالا لا يستوخم عقباه (mufradat)
- **B003** yoksula verilmesi gereken mal payı — yoksullara verilmesi gereken mal payı · malının gereken payını ödemek · malından karşılıksız vermek
  زكاة المال (maqayis;ayn;sihah;tahdhib)؛ زكى ماله تزكية أي أدى عنه زكاته؛ وتزكى أي تصدق (sihah)؛ ما يخرج الإنسان من حق الله تعالى إلى الفقراء (mufradat)
- **B004** yakışmamak [kalıp] — ona yakışmamak veya durumuna uygun düşmemek
  أمر لا يزكو بفلان أي لا يليق به (maqayis;sihah)؛ وهذا الأمر لا يزكو أي لا يليق (ayn)؛ هذا الأمر لا يزكو بفلان أي لا يليق به (tahdhib)
- **B005** çift olma — çift veya iki öğeli · tek veya çift · avuçtaki çift mi tek mi · avuçtaki şey için tek-çift söylemek
  الزكا الزوج وهو الشفع (maqayis)؛ وزكا الشفع يقال خسا أو زكا (sihah)؛ العرب تقول للفرد خسا وللزوجين اثنين زكا؛ هو يخسي ويزكي إذا قبض على شيء في كفه وقال أزكا أم خسا (tahdhib)

## ء ح د (root_000017): 92:19 لِأَحَدٍ

- **B001** tek ve eşi olmayan olma — bir tane; tek ve eşsiz · yalnız bir, yalnız bir
  أحد فرع والأصل الواو وحد (maqayis); أحد بمعنى الواحد وهو أول العدد (sihah); قل هو الله أحد (sihah;mufradat); يستعمل مطلقا وصفا في وصف الله تعالى وأصله وحد (mufradat); أحد أحد (sihah)
- **B002** hiç kimse — olumsuzlukta hiç kimse
  لا أحد في الدار؛ ما في الدار أحد (sihah); أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا (mufradat); فما منكم من أحد عنه حاجزين (sihah;mufradat)
- **B003** bir sayısı, onlu kuruluşları ve on bire çıkarma — saymanın başlangıcındaki bir · on bir, on bir dişil biçimi ve yirmi bir · onları on bire çıkarmak
  أحد واثنان وأحد عشر وإحدى عشرة (sihah); الواحد المضموم إلى العشرات نحو أحد عشر وأحد وعشرين (mufradat); فأحدهن أي صيرهن أحد عشر (sihah)
- **B004** iki kişiden biri, ilk olan ve haftanın ilk günü — ikinizden biri · Pazar günü · Pazar günleri
  أن يستعمل مضافا أو مضافا إليه بمعنى الأول (mufradat); أما أحدكما (mufradat); يوم الأحد أي يوم الأول (mufradat); يوم الأحد يجمع على آحاد (sihah)
- **B005** tek başına kalma ve birer birer gelme — tek başına kalmak; işi yalnız üstlenmek · birer birer, ayrı ayrı
  ما استأحدت بهذا الأمر أي ما انفردت به (maqayis); استأحد الرجل انفرد (sihah); جاءوا آحاد أحاد (sihah)
- **B006** Medine'deki belirli bir dağın özel adı — Medine'deki dağın özel adı
  أحد جبل بالمدينة (sihah)

## ع ن د (root_001052): 92:19 عِندَهُۥ

- **B001** doğruyu bile bile geri çevirerek karşı koyma ve sınırı aşma — azıp sınırı aşmak ve doğruyu bile bile geri çevirmek · bildiği şeyi kabul etmeyi bile bile reddetme · birine karşı durup onunla boy ölçüşmek; kimi zaman onun yaptığının benzerini yapmak · zorbalık eden ve doğruya uymaktan yüz çeviren kimse · doğruyu kabul etmeyip karşı çıkan kimse · devenin yulara yüklenip onu yöneten kişiyi çekmesi
  أصل صحيح واحد يدل على مجاوزة وترك طريق الاستقامة (maqayis)؛ عند الرجل إذا طغى وعتا وجاوز قدره (maqayis;ayn)؛ المعاندة أن يعرف الرجل الشيء ويأبى أن يقبله (maqayis;ayn;tahdhib)؛ خالف ورد الحق وهو يعرفه (sihah)؛ العنيد المعرض عن طاعة الله تعالى (tahdhib)؛ استعند البعير إذا غلب قائده على الزمام (maqayis)؛ عاند البعير خطامه أي عارضه (tahdhib)
- **B002** ortak doğrultudan yana sapıp ayrı durma — yoldan ya da amaçlanan yönden sapıp uzaklaşmak · bir yana çekilip topluluğa karışmayan · tek başına yaşayıp insanlara karışmayan adam · sürünün bir yanında durup öteki develere karışmayan deve · canlılığı ve gücü yüzünden yoldan yana sapan dişi deve · düz doğrultudan yana sapmış yol · yan, taraf · sağa sola yönelen saplama vuruşu · öteki kura oklarından başka bir yönde çıkarak kazanan ok · dirseği göğüsten uzakta duran
  العنود من الإبل الذي لا يخالط الإبل إنما هو في ناحية (maqayis;ayn;tahdhib)؛ رجل عنود لا يخالط الناس (maqayis;ayn)؛ طريق عاند أي مائل (maqayis)؛ العند بالتحريك الجانب (sihah)؛ العاند البعير الذي يجور عن الطريق ويعدل عن القصد (sihah)؛ قدح عنود وهو الذي يخرج فائزا على غير وجهة سائر القداح (tahdhib)
- **B003** sıvının yana yönelerek veya kesilmeden akması [kalıp] — kanı fışkırıp bir türlü dinmeyen damar · kanın yana doğru akması · kanı yaralıdan uzağa doğru akan yara · kusmanın art arda sürüp kesilmemesi · bol yağmur taşıyan bulut
  العرق العاند الذي يتفجر منه الدم فلا يكاد يرقأ (maqayis)؛ عند العرق سال ولم يرقأ وهو عرق عاند (sihah)؛ أعند في قيئه إذا لم ينقطع (maqayis)؛ أعند الرجل في قيئه إذا أتبع بعضه بعضا (sihah;tahdhib)؛ عند الدم إذا سال في جانب (tahdhib)؛ سحابة عنود كثيرة المطر (tahdhib)
- **B004** yakınında veya birinin değerlendirmesinde bulunma — bir şeyin yer veya zaman bakımından yakınında · birinin görüşünde, değerlendirmesinde, gözünde veya katında
  عند فحضور الشيء ودنوه (sihah)؛ عند لفظ موضوع للقرب (mufradat)؛ يستعمل في المكان وفي الاعتقاد وفي الزلفى والمنزلة (mufradat)؛ عند حرف صفة يكون موضعا لغيره ولفظه نصب (tahdhib)؛ في التقريب شبه اللزق (tahdhib)؛ مال عن الناس كلهم إليه حتى قرب منه ولزق به (maqayis)
- **B005** başka seçenek, kaçınma payı veya çıkış yolu — başka bir seçenek, kaçınma payı veya çıkış yolu · bir işe ulaşma yolu ya da başka seçenek
  ما عنه عِنْدَد أي ما عنه ميل ولا حيدودة (maqayis)؛ مالي منه عِنْدَد ومُعْلَنْدَد أي بد (sihah;tahdhib)؛ العندد الحيلة (tahdhib)؛ ما وجدت إلى كذا معلنددا أي سبيلا (sihah)
- **B006** sözü dinleyeni almaya veya tutmaya yönelten buyruk — onu al; ona bağlı kal
  وقد يغرى بها تقول عندك زيدا أي خذه (sihah)؛ العرب تأمر من الصفات بعليك وعندك ودونك وإليك (tahdhib)

## ن ع م (root_001525): 92:19 نِّعْمَةٍ

- **B001** iyi yaşam durumu ve başkasına ulaştırılan iyilik — bağış, iyilik veya elverişli yaşam durumu · iyi durum ve esenlik · bolluk ve rahatlık · bol ve rahat yaşam · iyiliği başkasına ulaştırma
  أصل واحد يدل على ترفه وطيب عيش وصلاح (maqayis)؛ نعم ينعم نعمة فهو نعم ناعم (ayn;tahdhib)؛ النعمة اليد والصنيعة والمنة وما أنعم به عليك (sihah)؛ نعمة الله منه وعطاؤه (tahdhib)؛ النعمة الحالة الحسنة والإنعام إيصال الإحسان إلى الغير (mufradat)
- **B002** yumuşamak, rahat yaşamak veya rahat yaşatmak — yumuşamak · yumuşak; rahat yaşayan · rahat ve bolluk içinde yaşayan kadın · çocuklarını bolluk içinde yaşattı · rahat ve bolluk içindeki yaşam
  نعم الشيء صار ناعما لينا (sihah)؛ نعمة العيش حسنه وغضارته (tahdhib)؛ نعم فلان أولاده ترفهم (maqayis)؛ طعام ناعم وجارية ناعمة (mufradat)؛ فهو نعم ناعم بين المنعم (ayn)
- **B003** övgü ve beğeni bildirmek — ne güzel; övgü bildirir · bu ne güzel · öyleyse ne güzel, yerinde olur
  نعم ضد بئس (maqayis)؛ نعم وبئس فعلان ماضيان ... فنعم مدح وبئس ذم (sihah)؛ نعما ... المعنى نعم الشيء هي (tahdhib)؛ نعم كلمة تستعمل في المدح بإزاء بئس (mufradat)
- **B004** evet diyerek onaylamak veya söz vermek — evet; doğru; olur · ona evet dedi
  نعم جواب الواجب ضد لا (maqayis)؛ نعم عدة وتصديق وجواب الاستفهام (sihah)؛ نعم يكون تصديقا ويكون عدة (tahdhib)؛ نعم كلمة للإيجاب (mufradat)
- **B005** develer ve geniş anlamda otlayan evcil hayvanlar — develer; deve varlığı · deve, sığır ve koyun topluluğu
  النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم (maqayis)؛ النعم واحد الأنعام وهي المال الراعية وأكثر ما يقع هذا الاسم على الإبل (sihah)؛ النعم لم يريدوا بها إلا الإبل فإذا قالوا الأنعام أرادوا بها الإبل والبقر والغنم (tahdhib)؛ النعم مختص بالإبل وجمعه أنعام (mufradat)
- **B006** devekuşu — devekuşu; erkek veya dişi birey · devekuşu türü veya topluluğu
  النعامة معروفة لنعمة ريشها (maqayis)؛ النعامة من الطير يذكر ويؤنث والنعام اسم جنس (sihah)؛ النعام الظليم والنعامة الأنثى (tahdhib)؛ النعامة سميت تشبيها بالنعم في الخلقة (mufradat)
- **B007** devekuşuna benzetilerek ad verilen şeyler — devekuşuna benzetilen kuyu kirişi, gölgelik, beden bölümü veya yol · Ay'ın konak yerlerinden biri
  على معنى التشبيه النعامة وهي كالظلة تجعل على رءوس الجبل (maqayis)؛ النعامة الخشبة المعترضة على الزرنوقين والنعائم منزل من منازل القمر (sihah)؛ النعامة الخشبة المعترضة على الزرنوقين وابن النعامة عرق الرجل ومحجة الطريق (tahdhib)؛ النعامة المظلة في الجبل وعلى رأس البئر تشبيها بالنعامة في الهيئة والنعائم من منازل القمر (mufradat)
- **B008** bir topluluğun dağılıp gücünü yitirmesi [kalıp] — dağıldılar, ayrıldılar veya güçlerini yitirdiler · hızla yola koyulup gittiler · yenilip dağıldılar
  شالت نعامتهم إذا تفرقوا (maqayis)؛ للقوم إذا ارتحلوا أو تفرقوا قد شالت نعامتهم (sihah)؛ خفت نعامتهم أي استمر بهم السير وشالت نعامتهم إذا تفرقت كلمتهم أو ذهب عزهم (tahdhib)
- **B009** yumuşak esen nemli güney rüzgarı — yumuşak esen nemli güney rüzgarı
  النعامي الريح اللينة (maqayis)؛ النعامى ريح الجنوب لأنها أبل الرياح وأرطبها (sihah)؛ من أسماء الجنوب النعامى (tahdhib)؛ النعامى الريح الجنوب الناعمة الهبوب (mufradat)
- **B010** daha da artırmak veya ileri dereceye götürmek — artırdı; daha ileri götürdü · onu iyice ince öğüttü
  فعل كذا وأنعم أي زاد (sihah;mufradat)؛ أنعم أفضل وزاد وأنعما أي زادا على ذلك ودققت دواء فأنعمت دقه أي بالغت وزدت (tahdhib)
- **B011** bir yeri kendine uygun bulup orada kalmak [kalıp] — bir yere geldi, orayı uygun bulup kaldı
  أتيت أرض بني فلان فتنعمتني إذا وافقته (maqayis)؛ أتيت أرض فلان فتنعمتني إذا وافقته (sihah)؛ أتيت أرضا فنعمتني أي وافقتني وأقمت بها (tahdhib)
- **B012** birine yaya gitmek ve ayakları yürüyerek kullanmak [kalıp] — ona yaya gitti veya onu yürüyerek aradı · ayaklarını yürümekle eskitti; hafif yürüdü
  تنعمت زيدا طلبته كأنه أراد أعمل إليه نعامته وهي باطن قدمه (maqayis)؛ تنعمت فلانا أتيته على غير دابة وتنعم فلان قدميه أي ابتذلهما (tahdhib)؛ تنعم فلان إذا مشى مشيا خفيفا فمن النعمة (mufradat)
- **B013** birini göz sevinci saymak veya bunun için dua etmek [kalıp] — Tanrı seni gözlere sevinç kaynağı kılsın · göz sevinci ve hoşnutluğu
  نعم ونعمى عين ونعمة عين أي قرة عين (maqayis)؛ نعمة العين قرتها ونعم عين ونعام عين ونعامة عين ونعمة عين ونعمى عين كله بمعنى (sihah)؛ نعمك الله عينا ونعم الله بك عينا ونعمى عين ونعام عين (tahdhib)؛ نعم الله بك عينا ونعم ونعمة عين ونعمى عين ونَعام عين (mufradat)

## ج ز ي (root_000244): 92:19 تُجْزَىٰٓ

- **B001** iyiliğe ya da kötülüğe denk karşılık verme — birine yaptığını iyilikle ya da kötülükle karşılama · birine yaptığının karşılığını verme · yapılana verilen iyi ya da kötü karşılık · çok geçmeden öç alma karşılığı · iyi işlerin ve yerine getirilmesi gereken yükümlülüklerin karşılıkları
  جزى يجزي جزاء أي كافأ بالإحسان وبالإساءة (ayn)؛ جزيته بما صنع جزاء وجازيته (sihah)؛ الجزاء يكون ثوابا ويكون عقابا؛ جزيت فلانا بما صنع جزاء؛ جزاء العطاس؛ الجوازي معناها الجزاء (tahdhib)؛ الجزاء ما فيه الكفاية من المقابلة إن خيرا فخير وإن شرا فشر؛ جزيته بكذا وجازيته (mufradat)؛ مكافأته إياه؛ جزيت فلانا أجزيه جزاء وجازيته مجازاة (maqayis)
- **B002** yerini tutup yükümlülüğü karşılama — yeterlilik ve bir işi başkası adına yerine getirme · bu işi benim yerime görüp tamamlama · bir koyunun senin adına yükümlülüğü karşılaması · yeterli olan ve başkasının yerini tutan kimse · birinin alacağını ya da borcunu ödeme
  فلان ذو غناء وجزاء (ayn)؛ جزى عني هذا الأمر أي قضى؛ جزت عنك شاة؛ رجل جازيك أي حسبك (sihah)؛ الجزاء أيضا القضاء؛ لا تقضي فيه نفس عن نفس شيئا؛ جزيت فلانا حقه؛ جزيته قرضه؛ صدقتك جزت عنك؛ هذا رجل حسبك وناهيك وكافيك وجازيك (tahdhib)؛ الجزاء الغناء والكفاية؛ لا يجزي والد عن ولده؛ جازيك فلان أي كافيك (mufradat)؛ قيام الشيء مقام غيره؛ ينوب مناب كل أحد؛ جزى عني هذا الأمر يجزي كما تقول قضى يقضي (maqayis)
- **B003** alacağı talep etme — borcumu ondan isteme · alacağını isteyen veya borcun ödenmesini talep eden kimse
  تجازيت ديني تقاضيته (ayn)؛ تجازيت ديني على فلان إذا تقاضيته؛ المتجازي المتقاضي (sihah)؛ أمرت فلانا يتجازى ديني أي يتقاضاه؛ أهل المدينة يسمون المتقاضي المتجازي (tahdhib)؛ تجازيت ديني على فلان أي تقاضيته؛ أهل المدينة يسمون المتقاضي المتجازي (maqayis)
- **B004** koruma statüsüne bağlı tarihsel vergi — koruma statüsündeki topluluklardan alınan tarihsel vergi · koruma statüsüne bağlı tarihsel vergiler
  الجزية ما يؤخذ من أهل الذمة والجمع الجزى (sihah)؛ الجزية جزية الناس التي تؤخذ من أهل الذمة؛ الجزية الخراج المجعول على الذمي سميت جزية لأنها قضاء منه لما عليه (tahdhib)؛ الجزية ما يؤخذ من أهل الذمة وتسميتها بذلك للاجتزاء بها عن حقن دمهم (mufradat)
- **B005** karşılık vermede üstün gelme [kalıp] — karşılık verme yarışında ötekine üstün gelme
  جازيته فجزيته أي غلبته (sihah)

## ECHO ج ز ز (root_000242): for 92:19 تُجْزَىٰٓ: withheld observed target; not identity

- **B001** saç, yün veya bitkiyi kırkıp kesme — saçı, yünü veya bitkiyi kırkıp kesmek · kırkma aleti · yünü kırkılan koyunlar
  جززت الصوف جزا (maqayis); الجز جز الشعر والصوف وغيره (ayn); جززت البر والنخل والصوف أجزه جزا والمجز ما يجز به (sihah); الجز جز الشعر والصوف والحشيش ونحوه وقد جززت الكبش والنعجة (tahdhib)
- **B002** kesim ya da hasat vaktinin gelmesi — kırkım, hasat veya ürün toplama zamanı · ağaç ürününün, ekinin veya koyunun kesim ya da kırkım vaktinin gelmesi · topluluğun koyunlarını kırkma ya da ekinini biçme vaktinin gelmesi · ekinin biçilecek duruma gelmesi
  هذا زمن الجزاز والجزاز (maqayis); الجزاز كالحصاد يقع على الحين والأوان وأجز النخل مثل أحصد البر (ayn); هذا زمن الجزاز والجزاز أي زمن الحصاد وصرام النخل وأجز النخل والبر والغنم واستجز البر (sihah); الجزاز كالحصاد واقع على الحين والأوان وأجز النخل حان له أن يجز وأجز القوم إذا حان أن تجز غنمهم (tahdhib)
- **B003** yeni kırkılmış yün veya kesimden kalan parça — henüz kullanılmamış kırkılmış yün · bir koyundan bir yılda kırkılan yün · deri veya başka bir şey kesilince düşen ya da fazla kalan parça · bir tutam yün
  الجزيزة خصلة من صوف والجمع جزائز والجزازة ما سقط من الأديم (maqayis); الجزز الصوف الذي لم يستعمل بعد ما جز وصوف كل شاة جزة والجزاز ما فضل من الأديم (ayn); الجزة صوف شاة والجزازة ما سقط من الأديم والجزيزة خصلة من الصوف (sihah); الجزز الصوف الذي لم يستعمل بعدما جز وهذه جزة هذه الشاة والجزاز ما فضل من الأديم (tahdhib)
- **B004** asılan boyalı yün süsü veya süs boncuğu — deve üzerindeki yolcu bölmesine bağlanan veya asılan boyalı yün tutamları · deve üzerindeki yolcu bölmesine asılan boyalı yün tutamları · deve üzerindeki yolcu bölmesinden sarkan boyalı yün parçası · insanı süslemek için kullanılan bir boncuk türü
  الجزائر عهون تشد على الهوادج (ayn); الجزجزة وهي عهنة تعلق من الهودج (sihah); الجزاجز خصل العهن والصوف المصبوغة تعلق على هوادج الظعائن وهي الثكن والجزائز وقيل الجزيز ضرب من الخرز (tahdhib)
- **B005** hurmanın kuruması veya hurmadaki kuruluk — hurmanın kuruması · hurmanın kuruması · hurmadaki kuruluk veya kuruma durumu
  جز التمر يجز بالكسر جزوزا أي يبس وأجز مثله وتمر فيه جزوز (sihah); قد جز التمر إذا يبس يجز جزوزا وتمر فيه جزوز (tahdhib)
- **B006** rivayette bir çıkış yeri olarak anılan yer adı — rivayette bir çıkış yeri olarak anılan yer adı
  جزة اسم أرض يقال إن الدجال يخرج منها (ayn); جزة اسم أرض منها يخرج الدجال فيما روي (tahdhib)

## ب غ ي (root_000138): 92:20 ٱبْتِغَآءَ

- **B001** bir şeyi arayıp istemek; başkası için aramak veya arayışına yardım etmek — bir şeyi aramak ve istemek · bir şeyi çaba göstererek aramak · ihtiyaç; aranan veya istenen şey · bir şeyi birisi için aramak · birinin bir şeyi aramasına yardım etmek veya onu arayan duruma getirmek
  طلب الشيء؛ بغيت الشيء إذا طلبته؛ البغية الحاجة؛ أبغيتك الشيء إذا أعنتك على طلبه (maqayis)؛ البغية مصدر الابتغاء؛ بغيت الشيء وابتغيته طلبته (ayn)؛ بغى ضالته؛ ابتغيت الشيء وتبغيته إذا طلبته (sihah)؛ البغي طلب تجاوز الاقتصاد؛ الابتغاء خص بالاجتهاد في الطلب (mufradat)
- **B002** uygun, mümkün veya hak edilmiş olmak — uygun olmak; mümkün olmak; hak edilmiş olmak
  ما ينبغي لك أن تفعل كذا؛ بغيته فانبغى (maqayis)؛ لا ينبغي لك أن تفعل كذا وما انبغى لك (ayn)؛ ينبغي لك أن تفعل كذا هو من أفعال المطاوعة (sihah)؛ ينبغي مطاوع بغى؛ لا يتسخر ولا يتسهل له؛ على معنى الاستئهال (mufradat)
- **B003** haddi aşarak haksızlık etmek — haddi aşma, haksızlık ve baskı · birine karşı haddini aşıp haksızlık etmek · haddini aşan ve haksızlık eden kişi · birbirine haksızlık etmek
  جنس من الفساد؛ أن يبغي الإنسان على آخر؛ البغي الظلم (maqayis)؛ البغي الظلم والباغي الظالم (ayn)؛ البغي التعدي؛ بغى الرجل على الرجل استطال؛ كل مجاوزة في الحد وإفراط على المقدار فهو بغي؛ تباغوا أي بغى بعضهم على بعض (sihah)؛ البغي على ضربين؛ تجاوز الحق إلى الباطل؛ بغى تكبر (mufradat)
- **B004** yaranın şişip bozulması veya içinde irin kalmış halde kapanması [kalıp] — yaranın şişip ilerleyerek bozulması · yaranın içinde irinli bozukluk kalmış halde kapanması
  بغى الجرح إذا ترامى إلى فساد (maqayis)؛ بغى الجرح ورم وترامى إلى فساد؛ برئ جرحه على بغى وفيه شيء من نغل (sihah)؛ بغى الجرح تجاوز الحد في فساده (mufradat)
- **B005** evlilik dışı cinsel ilişki ve buna bağlı kişi adları — kadının evlilik dışı cinsel ilişkiye girmesi · evlilik dışı cinsel ilişki; cinsel ahlaka aykırı davranış · evlilik dışı cinsel ilişkiye giren kadın; bu adla anılan kadın köle · kadın köleler veya evlilik dışı cinsel ilişkiye giren kadınlar · evlilik dışı cinsel ilişkiden doğan çocuk
  البغي الفاجرة؛ بغت تبغي بغاء وهي بغي (maqayis)؛ بغى بغاء أي فجر؛ البغية من الزنى؛ البغايا الجواري (ayn)؛ بغت المرأة بغاء أي زنت فهي بغي والجمع بغايا؛ خرجت المرأة تباغي أي تزاني؛ الأمة يقال لها بغي (sihah)؛ بغت المرأة بغاء إذا فجرت (mufradat)
- **B006** göğün şiddetli, bol ve gereğinden fazla yağdırması [kalıp] — göğün şiddetli veya gereğinden fazla yağmur yağdırması · göğün en şiddetli ve bol yağmuru
  بغي المطر وهو شدته ومعظمه؛ بغي السماء أي معظم مطرها (maqayis)؛ بغت السماء اشتد مطرها؛ بغي السماء أي معظم مطرها (sihah)؛ بغت السماء تجاوزت في المطر حد المحتاج إليه (mufradat)
- **B007** atın koşarken çalımlı ve neşeli davranması [kalıp] — atın koşarken çalımlı ve neşeli davranması
  اختيال الفرس ومرحه بغي؛ لا يقال فرس باغ (maqayis)؛ البغي في عدو الفرس اختيال ومرح؛ لا يقال فرس باغ (ayn)؛ البغي اختيال ومرح في الفرس؛ لا يقال فرس باغ (sihah)
- **B008** ordudan önce ilerleyen öncüler — ordudan önce ilerleyen öncüler · öncü topluluğun tek bir üyesi
  البغايا الطلائع الواحدة بغية أيضا (ayn)؛ البغايا أيضا الطلائع التي تكون قبل ورود الجيش (sihah)

## و ج ه (root_001630): 92:20 وَجْهِ

- **B001** yüz ve bir şeyin öne bakan yanı — yüz; bir şeyin öne bakan veya görünen yanı · kötü bir yüz ifadesiyle bakmak
  الوجه مستقبل لكل شيء (maqayis); الوجه مستقبل كل شيء (ayn;tahdhib); وجه الإنسان وغيره معروف (jamhara); الوجه معروف (sihah); أصل الوجه الجارحة (mufradat)
- **B002** yön ve hedef; o yöne sevk etme veya yolu belli etme — yön, taraf · yönelinen yön veya hedef · bir şeyi belirli bir yöne çevirmek veya göndermek · tek bir yöne çevrilmiş · bir şeye doğru yönelmek · rüzgarın çakılı bir yöne sürüklemesi · yolu yürüyerek izini belirginleştirmek · perdeyi yırtacak bir yöne gitmek veya perdeyi yerinden kaldırmak
  الوجهة كل موضع استقبلته (maqayis); الجهة النحو (ayn;tahdhib); الوجهة القبلة وشبهها (ayn;tahdhib); ضل وجهة أمره إذا ضل قصده (jamhara); وجهته في حاجة ووجهت وجهي لله وتوجهت نحوك وإليك (sihah); وجهت الريح الحصا إذا ساقته ووجهوا للناس الطريق إذا وطئوه وسلكوه (tahdhib); للمقصد جهة ووجهة (mufradat)
- **B003** karşı karşıya gelme ve doğrudan yüzüne söyleme — birinin karşısına çıkmak, onunla yüz yüze gelmek · karşılaşma, yüzleşme · karşında, tam karşı tarafta
  واجهت فلانا جعلت وجهي تلقاء وجهه (maqayis;mufradat); الوجاه والتجاه ما استقبل شيء شيئا (ayn;tahdhib); المواجهة استقبالك الرجل بكلام (ayn;tahdhib); واجهت الرجل بكلام حسن أو قبيح (jamhara); المواجهة المقابلة وقعدت وجاهك أي قبالتك (sihah)
- **B004** yüzün varlığın kendisini temsil etmesi — 
  ربما عبر عن الذات بالوجه (maqayis); قيل ذاته وكل شيء هالك إلا هو (mufradat)
- **B005** amaç edinip yönelme; ibadette içtenlikle bağlanma — 
  وجهي إليك (maqayis); ضل وجهة أمره إذا ضل قصده (jamhara); وجهت وجهي لله سبحانه (sihah); الوجه الذي يؤتى منه وما أريد به الله وأخلصوا العبادة لله وأسلمت وجهي لله (mufradat)
- **B006** toplumsal itibar, yüksek mevki ve önde gelen kişi — topluluğun önderi · yerleşimin ileri gelenleri · itibarlı, yüksek mevkili · toplumsal itibar ve mevki · itibarlı ve yüksek mevkili olmak · onu itibarlı ve yüksek mevkili kılmak
  وجيه بين الجاه والجاه مقلوب (maqayis); وجوه القوم سادتهم ورجل وجيه عند السلطان (jamhara); صار وجيها أي ذا جاه وقدر ووجوه البلد أشرافه (sihah); جاه فيهم أي منزلة وقدر (tahdhib); فلان وجه القوم وفلان وجيه ذو جاه (mufradat)
- **B007** günün başı, ilk saatleri [kalıp] — günün başı, ilk saatleri
  وجه النهار أوله (jamhara); أتيته بوجه نهار وشباب نهار وصدر نهار أي في أوله (tahdhib); وجه النهار أي صدر النهار (mufradat)
- **B008** sözün veya işin doğru yönü ve ona uygun düzenleme — sözün amaçlanan yönü · doğru görüş · aklına bir görüş gelmek · bir şeyi doğru yolundan saptırmak · işi gerektiği gibi düzenleyip her şeyi yerine koymak · hiçbir işi doğru yapamayan ahmak; ayrıca tuvaletini yapmayı bile beceremeyen kişi
  وجه الكلام السبيل التي تقصدها به وصرفت الشيء عن وجهه أي عن سننه (jamhara); هذا وجه الرأي أي هو الرأي نفسه وأحمق ما يتوجه (sihah); دبر الأمر على وجهه الذي ينبغي وأحمق ما يتوجه أي ما يحسن أن يأتي الغائط (tahdhib); أحمق ما يتوجه أي لا يستقيم في أمر من الأمور (mufradat)
- **B009** yaşlanıp ömrünün son dönemine girmek — yaşlanıp ömrünün son dönemine girmek
  توجه الشيخ ولى وأدبر (maqayis); توجه الشيخ إذا ولى وكبر (sihah); إذا كبر سنه قد توجه (tahdhib)
- **B010** doğumda ellerin veya ön ayakların önce çıkması — elleri veya ön ayakları önce çıkan yavru · yavruyu elleri veya ön ayakları önce çıkacak biçimde doğurmak
  للمهر إذا خرجت يداه من الرحم وجيه (maqayis); للولد إذا خرجت يداه من الرحم أولا وجيه (sihah); أوجهت به أمه حين ولدته إذا خرج يداه أولا (tahdhib)
- **B011** kurucu uzun ünlü ile ana uyak harfi arasındaki harf — kurucu uzun ünlü ile ana uyak harfi arasındaki harf
  التوجيه هو الحرف الذي بين ألف التأسيس وبين القافية (sihah); الصاد توجيه بين التأسيس والقافية (tahdhib); التوجيه في الشعر الحرف الذي بين ألف التأسيس وحرف الروي (mufradat)
- **B012** hıyar veya kavunun altını kazıp yana yatırma — hıyar veya kavunun altını kazıp yana yatırma
  التوجيه أن تحفر تحت القثاءة أو البطيخة ثم تضجعها (maqayis)
- **B013** yüzüne vurma ve yüzüne vurulmuş olma — birinin yüzüne vurmak · yüzüne vurulmuş
  وجهت فلانا ضربت وجهه فهو موجوه (tahdhib)
- **B014** yanına gelen kişiyi geri çevirmek — yanına gelen kişiyi geri çevirmek
  أتى فلان فلانا فأوجهه وأوجأه إذا رده (tahdhib)
- **B015** iki yüzlü nesne; içiyle dışı uyuşmayan kişi [kalıp] — iki yüzü bulunan kumaş · içiyle dışı uyuşmayan iki yüzlü kimse
  كساء موجه له وجهان؛ رجل ذو وجهين إذا لقي بخلاف ما في قلبه (jamhara)

## ر ب ب (root_000532): 92:20 رَبِّهِ

- **B001** sahip olup yönetme — Tanrı; sahip, buyruğu geçen yönetici veya düzenleyici · bir şeyin sahibi · evin sahibi veya ev işlerini yöneten kadın · sahiplik, egemenlik ve yönetim yetkisi
  الرب: الله تبارك وتعالى؛ ورب كل شيء مالكه (jamhara); رب كل شئ: مالكه؛ وقد قالوه في الجاهلية للملك؛ رببت القوم: سستهم (sihah); يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح (tahdhib); الرب مصدر مستعار للفاعل؛ لا يقال الرب مطلقا إلا لله؛ رب الدار ورب الفرس (mufradat); فالرب المالك والخالق والصاحب؛ والله جل ثناؤه الرب (maqayis)
- **B002** adım adım yetiştirip tamamlama — yapılan iyiliği eksiksiz kılmak · mülkü gözetip iyileştirmek · çocuğunu yetiştirmek · bir şeyi aşama aşama olgunlaştırma · yetiştirme anlamındaki değişmeli söyleyiş
  رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها (jamhara); رب الضيعة أي أصلحها وأتمها؛ رب فلان ولده؛ رباه (sihah); رب الشيء أي أصلحه؛ رب فلان الصنيعة إذا أتمها وأصلحها (tahdhib); التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام؛ ربه ورباه ورببه (mufradat); رب فلان ضيعته إذا قام على إصلاحها؛ رببت الصبي أربه (maqayis); ربته تربيتا إذا رببه (maqayis-rbt)
- **B003** Tanrı bilgisiyle yetiştiren bilgin — Tanrı bilgisine sahip bilgin ve öğretici
  الرباني: المتأله العارف بالله تعالى (sihah); الرباني: العالم؛ العلماء بالحلال والحرام؛ حكماء علماء؛ العالم المعلم الذي يغذو الناس بصغار العلوم (tahdhib); الرباني... يرب العلم؛ يرب نفسه بالعلم؛ منسوب إلى الرب (mufradat); الربي العارف بالرب (maqayis)
- **B004** büyük insan topluluğu — büyük topluluk; on bin kişilik topluluk · tek birlik hâlinde birleşmiş beş kabile · insanları toplayan kişi veya toplanma yeri
  الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا (sihah); الربيون: الألوف؛ الربيون: الجماعات الكثيرة؛ الربة: عشرة آلاف؛ الربان: الجماعة (tahdhib); يجوز أن يضم الربرب إلى الباب الثالث لتجمعه (maqayis)
- **B005** bakımla kurulan üvey aile bağı — üvey oğul veya bakım altında yetişen erkek çocuk · üvey kız veya bakım altında yetişen kız çocuk · bakıcı kadın; evde sütü için beslenen dişi hayvan · çocuğun bakımını üstlenen üvey baba veya üvey anne
  الراب: زوج الأم؛ الرابة: امرأة الأب؛ ربيب الرجل: ابن امرأته من غيره؛ الربيبة: الحاضنة (sihah); الربيب: ابن امرأة الرجل من غيره؛ ربيبة الرجل: بنت امرأته من غيره؛ راب ورابة (tahdhib); الراب والرابة بأحد الزوجين إذا تولى تربية الولد؛ الربيب والربيبة بذلك الولد (mufradat); ربيب الرجل ابن امرأته؛ الراب الذي يقوم على أمر الربيب (maqayis)
- **B006** koyu öz veya yağ tortusu — koyu meyve özü veya yağ tortusu · koyu özle işlenmiş veya güçlendirilmiş · koyu meyve özüyle hazırlanmış yiyecekler
  رب السمن والزيت: ثفله الأسود؛ سقاء مربوب إذا أصلح بالرب (jamhara); الرب: الطلاء الخاثر؛ سقاء مربوب؛ المرببات الأنبجات (sihah); رب فلان نحيه إذا جعل فيه الرب ومتنه به؛ نحي مربوب (tahdhib); رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب (mufradat); هذا سقاء مربوب بالرب؛ الرب للعنب وغيره لأنه يرب به الشيء (maqayis)
- **B007** bir yerde kalıp sürme — bir yerde kalıp ayrılmamak · develerin sürekli kaldığı yer · bulut sürüp gitti · dişi deve erkeğe bağlandı · bir şeye yaklaşma
  رب بالمكان وأرب إذا أقام به (jamhara); مرب الإبل حيث لزمته؛ أربت الإبل؛ أربت الناقة؛ أربت الجنوب والسحابة أي دامت؛ الأرباب الدنو (sihah); أرب فلان بالمكان إذا أقام به فلم يبرحه؛ مرب الإبل أي حيث لزمته (tahdhib); أربت السحابة: دامت؛ أرب فلان بمكان كذا (mufradat); الأصل الآخر لزوم الشيء والإقامة عليه؛ أربت السحابة؛ الإرباب الدنو (maqayis)
- **B008** katmanlı asılı bulut kümesi — beyaz olabilen, katmanlı veya aşağıda asılı bulut
  الرباب: سحاب أبيض؛ الواحدة ربابة (sihah); الربابة: السحابة التي قد ركب بعضها بعضا؛ جمعها رباب (tahdhib); الرباب: السحاب، سمي بذلك لأنه يرب النبات (mufradat); سمي السحاب ربابا؛ السحاب المتعلق دون السحاب يكون أبيض ويكون أسود (maqayis)
- **B009** başlangıçtaki tazelik — yeni doğurmuş veya sütü için evde tutulan koyun · bir şeyin yeni ve taze dönemi · gençliğin ilk ve taze dönemi
  الربى: الشاة التي وضعت حديثا؛ قرب العهد بالولادة؛ بربانه أي بحدثانه وجدته وطراءته (sihah); الربى: أول الشباب؛ الربان من كل شيء: حدثانه؛ الشاة فهي ربى (tahdhib); الشاة الربي التي تحتبس في البيت للبن؛ التي وضعت حديثا (maqayis)
- **B010** kura oklarını toplayan kap — kura oklarını bir arada tutan deri veya bez kap
  الربابة: قطعة من أدم تجمع فيها القداح (jamhara); الربابة شبيهة بالكنانة تجمع فيها سهام الميسر؛ جماعة السهام (sihah); الربابة: جماعة السهام؛ الجلدة التي تجمع فيها السهام (tahdhib); لما يجمع فيه القدح ربابة (mufradat); الخرقة التي يجعل فيها القداح ربابة (maqayis)
- **B011** bağlayıcı söz ve güvence — tarafları birleştiren bağlayıcı söz veya sözleşme · sözleşmeye bağlı taraflar · bağlayıcı söz; söz gibi bağlayıcı vergi payı
  الربابة: العهد والمعاهدون أربة (jamhara); الربابة: العهد والميثاق؛ الأربة أهل الميثاق (sihah); الرباب: العهد؛ الرباب: العشور (tahdhib); العقد في موالاة الغير: الربابة (mufradat); الربابة وهو العهد؛ للمعاهدين أربة؛ الرباب العشور (maqayis)
- **B012** belirli bir yeşil bitki türü — belirli bir bitki, yumuşak ot veya küçük ağaç türü
  الربة: ضرب من الشجر أو النبت (jamhara); الربة بالكسر: ضرب من النبت، والجمع الربب (sihah); الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف (tahdhib)
- **B013** bol ve toplanmış su — çok miktarda su; bazen bol tatlı su
  الربب، بالفتح: الماء الكثير، ويقال العذب (sihah); الربب وهو الماء الكثير سمي بذلك لاجتماعه (maqayis)
- **B014** yaban sığırı sürüsü — yaban sığırı sürüsü; bazen sığır veya deve topluluğu
  الربرب: القطيع من بقر الوحش (sihah); الربرب: جماعة البقر، وكذلك الإبل (tahdhib); الربرب القطيع من بقر الوحش؛ يجوز أن يضم إلى الباب الثالث لتجمعه (maqayis)
- **B015** azlık bildiren ilgeç — belirsiz adla azlık bildiren ilgeç; nice az · eylem önünde bazen veya kimi zaman · azlık ilgecinin sonuna ses eklenmiş ağız biçimi · belirsiz öğe eklenmiş azlık ilgeci biçimi
  رب: كلمة؛ ربما؛ ربت في معنى رب (jamhara); رب حرف خافض؛ ربما؛ ربت؛ ربه رجلا (sihah); رب من حروف المعاني؛ رب للتقليل؛ ربما؛ ربتما؛ تزيد في رب هاء (tahdhib); رب لاستقلال الشيء، ولما يكون وقتا بعد وقت، نحو ربما (mufradat); رب فكلمة تستعمل في الكلام لتقليل الشيء؛ ولا يعرف لها اشتقاق (maqayis)
- **B016** gereksinim, sıkı düğüm veya iyilik — gereksinim · sıkıca bağlanmış düğüm · iyilik ve başkasına yarar sağlama
  الربى: الحاجة؛ الربى: الرابة؛ الربى: العقدة المحكمة؛ الربى: النعمة والإحسان (tahdhib)
- **B017** gemicilerin başı — gemicilerin başı, kaptan
  رباني: رئيس الملاحين (tahdhib)

## ECHO ر ب و (root_000537): for 92:20 رَبِّهِ: withheld observed target; not identity

- **B001** artmak veya yükselmek — bir şey arttı veya yükseldi · toprak suyla kabarıp arttı · yükselen veya fazla köpük · olağandan daha şiddetli yakalayış · onun üzerine çıktı veya üstünde bulundu
  ربا الجرح والأرض والمال وكل شيء يربو إذا زاد (ayn)؛ ربا الشيء يربو ربوا إذا ارتفع (jamhara)؛ ربا الشيء يربو ربوا أي زاد (sihah;tahdhib)؛ ربت أي زادت، وزبدا رابيا، وأخذة رابية (tahdhib;mufradat)؛ أربى عليه أي أشرف عليه (mufradat)
- **B002** yükselmiş arazi — yükselmiş arazi · çevresinden yüksek yer · arazideki yükselti
  الرابية ما ارتفع من الأرض، والربوة لغات أرض مرتفعة (ayn)؛ الربو والربوة والرباوة واحد وهو العلو من الأرض (jamhara)؛ الرابية الربو وهو ما ارتفع من الأرض، وكذلك الربوة (sihah)؛ الرباوة والرابية والرباة كل ذلك ما ارتفع من الأرض (tahdhib)؛ ربوة وربوة وربوة ورباوة، وسميت الربوة رابية (mufradat)
- **B003** belirli işlem biçimleriyle sınırlı anapara fazlalığı — belirli alışveriş veya borç biçimlerinde anaparayı aşan fazlalık · işlemdeki anapara fazlalığının özel adı veya bir söyleyiş biçimi · mal bu işlemde fazlalıkla arttı · anaparaya fazlalık eklenen işleme girdi
  ربا المال يربو في الربا أي يزداد، والربا في كتاب الله حرام، والربية هي الربا خاصة (ayn)؛ الربا في البيع، والربية لغة في الربا (sihah)؛ الربا ربوان، فالحرام كل قرض يؤخذ به أكثر منه (tahdhib)؛ الربا الزيادة على رأس المال، لكن خص في الشرع بالزيادة على وجه دون وجه (mufradat)
- **B004** soluğu yükselip sıkışmak — yüksek ve sıkışık soluma · soluğu sıkıştı · at koşu ya da ürkme yüzünden şişip soluksuz kaldı · soluğu yükselip tıkanmış
  ربا فلان أي أصابه نفس في جوفه ودابة بها ربو (ayn)؛ أصابه ربو من مشي أو عدو إذا علت أنفاسه (jamhara)؛ الربو النفس العالي، وربا الفرس إذا انتفخ من عدو أو فزع (sihah)؛ أخذها الربو وهو البهر (tahdhib)؛ الربو الانبهار سمي بذلك تصورا لتصعده (mufradat)
- **B005** besleyip büyütmek ve yetişmek — onu besleyip büyüttü · onların arasında yetişti · çocuğu besleyip büyüttü, çocuk gelişti
  ربيته وتربيته أي غذوته (ayn)؛ ربوت في بني فلان وربيت أي نشأت فيهم، وربيته تربية وتربيته أي غذوته، هذا لكل ما ينمي كالولد والزرع (sihah)؛ ربيت الولد فربا من هذا (mufradat)
- **B006** uyluk kökü ve iç yanlardaki iki çıkıntılı et parçası — uyluk kökü veya kasık eti · uyluk köklerinin iç yanlarındaki iki çıkıntılı et parçası
  الأربية أصل الفخذ، وهما أربيتان (sihah)؛ الأربيتان لحمتان ناتئتان في أصول الفخذين من باطن (mufradat)
- **B007** baba tarafından yakın hane halkının arasına gelmek [kalıp] — kendi topluluğundaki baba tarafından yakın hane halkının arasına geldi
  جاء فلان في أربية قومه، أي في أهل بيته من بني الأعمام ونحوهم، ولا تكون الأربية من غيرهم (sihah)

## ع ل و (root_001042): 92:20 ٱلْأَعْلَىٰ

- **B001** yukarı yükselme ve yüksekte olma — yukarı olma; aşağı karşıtı yükseklik · bir yerde yükselmek · günün yükselmesi · yükselip uzaklaşmak
  أصل واحد يدل على السمو والارتفاع (maqayis)؛ العلو أصل البناء (ayn)؛ علا في المكان يعلو علوا (sihah)؛ العلو ضد السفل والعلو الارتفاع (mufradat)
- **B002** saygınlıkta yüksek mevki — saygınlık ve yüksek mevki · değeri yüksek kimse veya nitelik · en üstün ve en yüksek değerde olan · saygın ve yüksek mevki sahibi · toplumun seçkinleri · kazanılmış yüksek onur dereceleri
  العلاء فالرفعة (maqayis;ayn)؛ رجل عالي الكعب أي شريف (maqayis;ayn)؛ العلاء والعلاء الرفعة والشرف (sihah)؛ العلي هو الرفيع القدر (mufradat)
- **B003** kibirli üstünlük taslama — kınanan büyüklük taslama · yeryüzünde kibirlenip taşkınlık etmek · kibirli ve kendini üstün görenler
  العلو فالعظمة والتجبر (maqayis;ayn)؛ علا ملك في الأرض أي طغى وتعظم (ayn)؛ علا في الأرض تكبر (sihah)؛ علا يقال في المحمود والمذموم (mufradat)
- **B004** yapı içinde üstün gelip bastırma [kalıp] — onu yenip bastırmak · kişiyi yenmek · kılıçla vurmak · işi üstlenip tek başına yürütmek · ata binmek
  من قهر أمرا فقد اعتلاه واستعلى عليه (maqayis)؛ علوت الرجل غلبته (sihah)؛ استعلى الرجل أي علا واستعلاه أي علاه (sihah)؛ الاستعلاء قد يكون طلب العلو المذموم وقد يكون طلب العلاء (mufradat)
- **B005** üst yan ve yukarıdanlık [kalıp] — evin üst kısmı; altının karşıtı · yukarıdan · üstten veya yukarıdan · yukarıdan · rüzgarın avın üstünde kalan yönü
  أسفل الشيء وأعلاه (maqayis)؛ جئتك من أعلى ومن علا ومن عال ومن عل (maqayis)؛ علو الدار نقيض سفلها (sihah)؛ علاوة الريح وسفالتها (sihah;mufradat)؛ علاوة الشيء أعلاه (mufradat)
- **B006** gel diye çağırma — gel; buraya yönel
  تعال فهو من العلو كأنه قال اصعد إلي (maqayis)؛ لا يستعمل هذا إلا في الأمر خاصة (maqayis)؛ التعالي الارتفاع تقول منه إذا أمرت تعال (sihah)؛ تعال أصله أن يدعى الإنسان إلى مكان مرتفع (mufradat)
- **B007** yüksek yer adları — dağ başı veya yüksek yer · yüksek bölge veya yukarıdaki yerleşim · yüksek yerler veya oraların halkı · üst oda · iyi kimselere ait çok yüksek yer veya kayıt
  العلياء رأس كل جبل أو شرف (maqayis)؛ العالية من محال العرب من الحجاز (maqayis)؛ العلية غرفة (maqayis;sihah)؛ العلياء كل مكان مشرف (sihah)؛ لفي عليين (maqayis;mufradat)؛ العلية اسما للغرفة (mufradat)
- **B008** üstüne eklenen veya üst parça — tam yükten sonra üste konan ek yük · baş ve boyun · bir şeyin üst kısmı · kitabın başlığı; başta ve üstte yer alan ad
  العلاوة ما يحمل على البعير بعد تمام الوقر (maqayis)؛ رأس الرجل وعنقه علاوة (maqayis)؛ علوان الكتاب من العلو لأنه أول الكتاب وأعلاه (maqayis)؛ العلاوة ما عليت به على البعير بعد تمام الوقر (sihah)؛ علاوة الشيء أعلاه (mufradat)
- **B009** belirli araç ve parça adları — örs · kurutulmuş süt ürünü konan taş · mızrağın uç kısmına yakın bölümü · oyun oklarının yedincisi ve en değerlisi · kova ipini makaraya geri alan kişi · sağ yandan süt hayvanına yaklaşan kişi · ipi makaradaki yerine kaldırmak
  العلاة وهي السندان (maqayis)؛ العلاة حجر يجعل عليه الأقط والعلاة السندان (sihah)؛ عالية الرمح ما دخل في السنان إلى ثلثه (sihah)؛ المعلى السابع من القداح (maqayis;sihah;mufradat)؛ المعلي الذي يمد الدلو (maqayis)
- **B010** uzun ve iri yapılı — uzun iri kimse veya iri deve · sağlam yapılı dişi deve · uzun, iri ve sağlam yaratılışlı
  ناقة عليان أي طويلة جسيمة ورجل عليان طويل (maqayis)؛ يقال للناقة علاة تشبه بها في صلابتها (maqayis;sihah)؛ يقال رجل عليان وكذلك المرأة (sihah)؛ العليان البعير الضخم (mufradat)
- **B011** bedensel halden kurtulup esenleşme [kalıp] — lohusalıktan temizlenip esenliğe kavuşmak · hastalıktan kurtulmak
  للمرأة إذا طهرت من نفاسها قد تعلت (maqayis)؛ لا يقال إلا للنفساء (maqayis)؛ تعلت المرأة من نفاسها أي سلمت وتعلى الرجل من علته (sihah)
- **B012** ilgeç ve kalıplaşmış görev sözü — üzerinde, üzerine veya benzeri ilgeç görevi · şunu al · bana şunu ver · onun yanından veya üstünden
  جئت من عليك أي من عندك (maqayis)؛ على لها ثلاثة مواضع (sihah)؛ لفظة مشتركة للاسم والفعل والحرف (sihah)؛ على حرف خافض وقد يكون اسما (sihah)؛ عليك زيدا أي خذه (sihah)

## ر ض و (root_000569): 92:21 يَرْضَىٰ

- **B001** hoşnut olma ve kabul etme — hoşnut olmak; kabul etmek · hoşnut · kabul edilmiş; kendisinden hoşnut olunan · kendisinden hoşnut olunan kişi · hoşnutluk · onu kabul edip uygun buldu · onu seçip uygun buldu · ondan hoşnut oldu; onu kabul etti · hoşnutluk adı · beğenilen bir yaşayış · onu arkadaş olarak kabul etti · ondan hoşnut oldu; onu uygun buldu · beğenilen; kabul edilen · kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması · Tanrı'nın kulu buyruğa uyan ve yasaktan kaçınan biri olarak görmesi
  أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضا مقصور (ayn)؛ رضيت الشيء وارتضيته فهو مرضي ومرضو ورضيت عنه رضا (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو ورضا العبد عن الله ورضا الله عن العبد (mufradat)
- **B002** hoşnutluk; yoğun hoşnutluk — hoşnutluk; yoğun hoşnutluk · hoşnutluk
  الرضوان اسم موضوع من الرضا (ayn)؛ الرضوان الرضا وكذلك الرضوان بالضم والمرضاة مثله (sihah)؛ الرضوان الرضا الكثير (mufradat)
- **B003** karşılıklı hoşnutluk ve kabul — karşılıklı hoşnutluk · birbiriyle hoşnutlaşma · birbirlerinden hoşnut olduklarını karşılıklı gösterdiler
  المراضاة من اثنين (ayn)؛ مصدر راضيته رضاء ومراضاة (sihah;tahdhib)؛ إذا تراضوا بينهم أي أظهر كل واحد منهم الرضا بصاحبه ورضيه (mufradat)
- **B004** başkasını hoşnut etme veya hoşnutluğunu isteme — onu kendimden hoşnut ettim · onu hoşnut ettim · uğraşarak onu hoşnut ettim · ondan hoşnutluk göstermesini istedim; o da beni hoşnut etti
  أرضيته عني ورضيته بالتشديد أيضا فرضي وترضيته أرضيته بعد جهد واسترضيته فأرضاني (sihah)
- **B005** karşılıklı çekişmede üstün gelme — karşılıklı çekişmede ona üstün geldim
  قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه لأنه من الواو (sihah)
- **B006** söz dinleyen, seven veya güvence veren — söz dinleyen; seven; güvence veren
  الرضي المطيع والرضي المحب والرضي الضامن (tahdhib)
- **B007** bir dağ adı ve kadın adları — bir dağ adı; bir kadın adı · o dağın adına bağlılık bildiren biçim · bir kadın adı
  رضوى جبل (maqayis;ayn;sihah)؛ ومن أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)

## ECHO ر ض ي (root_000570): for 92:21 يَرْضَىٰ: withheld observed target; not identity

- **B001** hoşnut olup uygun bulma — hoşnut olmak; gönlüne uygun bulmak · hoşnut olan · beğenilmiş, uygun bulunmuş · kendisinden hoşnut olunan · uygun bulunmuş; eski kök yapısını koruyan biçim · kendisinden hoşnut olunan adam; eski kök yapısını koruyan söyleyiş · hoşnutluk; hoşnutsuzluğun karşıtı · hoşnutluğu bildiren uzatılmış ad biçimi · hoşnutluk; çok güçlü hoşnutluk · hoşnutluk bildiren ad · iki tarafın birbirini uygun bulması · birbirini uygun bulma ve karşılıklı anlaşma · şeyi beğenip uygun buldum · onu beğenip seçtim · ondan hoşnut oldum · onu arkadaş olarak uygun buldum · ondan ya da onunla olmaktan hoşnut oldum · beğenilen, hoşnutluk veren yaşayış · onu benden hoşnut ettim · onu hoşnut ettim · uğraştıktan sonra onu hoşnut ettim · onun gönlünü yapmaya çalıştım, sonunda benden hoşnut oldu · birbirlerini uygun bulup anlaştılar · kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması · Tanrı'nın kulunu buyruklarına uyar ve yasaklarından kaçınır görmesi · beğenilmiş, uygun bulunmuş
  أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضوان من الرضا (ayn)؛ الرضوان الرضا والمرضاة مثله ورضيت الشيء وارتضيته (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو والرضوان الرضا الكثير (mufradat)
- **B002** çekişmede alt etme — o benimle çekişti, ben de onu o işte yendim
  قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه (sihah)
- **B003** dağ ve kadın adı ailesi — bir dağın ve bir kadının adı · söz konusu dağla ilgili veya o dağdan olan · bir kadın adı
  رضوى جبل (maqayis;ayn)؛ رضوى جبل بالمدينة والنسبة إليه رضوى (sihah)؛ من أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)
- **B004** buyruğa uyan, seven veya güvence veren — buyruğa uyan, seven ya da güvence veren
  الرَّضِيّ المطيع؛ الرَّضِيّ المحب؛ الرَّضِيّ الضامن (tahdhib)



===== _commentary/v16/work/s092/surah.r2.hftbundle/channels.md =====
(source: latent_activation/network/v3/reviews/s092/reader_a_pilot.md)

# S092 Semantic Channel Discovery

## Parent Channels

### 1. Covering, Disclosure, and Surface Legibility
- Semantic invariant: A field or surface changes according to whether it is covered, exposed, clarified, marked, or made misleading to sight.
- Surface relation: direct; 92:1 joins night with covering in `الليل` and `يغشى`, and 92:2 answers with day and disclosure in `النهار` and `تجلى`.
- Surprising reach: Visibility extends into animal facial markings, route beacons, and surfaces whose outward appearance conceals their condition.

#### Subchannel A. Night as an Enveloping Cover
- Reading type: surface-primary
- Scene or process: Darkness advances over a field as a layer that conceals what had been visible.
- Active motifs: night and darkness `ل ي ل:B001/m01`; covering layer over sight or surface `غ ش و:B001/m01`, `غ ش ي:B001/m01`; encompassing cover `غ ش و:B002/m01`
- Ayah anchors: 92:1 (`ل ي ل`: `الليل`; `غ ش و`: `يغشى`)
- Synthesis: Night supplies the dark setting, while covering supplies the operation by which visibility is progressively overtaken.

#### Subchannel B. Daybreak as Unveiling
- Reading type: mixed
- Scene or process: Day opens, darkness recedes, and the face of time becomes bright and manifest.
- Active motifs: daylight opening `ن ه ر:B002/m01`; disclosure after concealment `ج ل و:B001/m01`; clear white spread of day `ج ل و:B007/m01`; emitted light `ن و ر:B001/m01`; opening face of day `و ج ه:B007/m01`
- Ayah anchors: 92:2 (`ن ه ر`: `النهار`; `ج ل و`: `تجلى`); 92:14 (`ن و ر`: `نارا`); 92:20 (`و ج ه`: `وجه`)
- Synthesis: Disclosure clears the field, light fills it, and the day's exposed front replaces the night's cover.

#### Subchannel C. Visible Mark, Beacon, and Orientation
- Reading type: latent/lexical
- Scene or process: A surface is visibly marked or elevated so that an observer can recognize it and orient by it.
- Active motifs: white marking over an animal's face `غ ش و:B007/m01`, `غ ش ي:B008/m01`; conspicuous route beacon `ن و ر:B005/m01`; front presented to an observer `و ج ه:B001/m02`
- Ayah anchors: 92:1 (`غ ش و`: `يغشى`); 92:14 (`ن و ر`: `نارا`); 92:20 (`و ج ه`: `وجه`)
- Synthesis: Facial whiteness supplies a readable mark, the presented front gives it an orientation, and the beacon scales visible recognition into route guidance.

#### Subchannel D. Double-Faced and Deceptive Surfaces
- Reading type: latent/lexical
- Scene or process: An outward face presents one condition while concealing a different interior or material state.
- Active motifs: person or object with two faces `و ج ه:B015/m01`; hypocritical double-facing `و ج ه:B015/m02`; multicolored cloth that misstates its condition `ك ذ ب:B009/m01`; worn surface beneath appearance `خ ل ق:B009/m01`
- Ayah anchors: 92:20 (`و ج ه`: `وجه`); 92:9 and 92:16 (`ك ذ ب`: `كذب`); 92:3 (`خ ل ق`: `خلق`)
- Synthesis: The visible face becomes an interface of deception when color or presentation no longer corresponds to the concealed condition.

### 2. Time, Sequence, and Change of State
- Semantic invariant: Events acquire order through beginning, succession, delay, promptness, culmination, and the transition from emergence to cessation.
- Surface relation: direct; 92:1-2 alternate night and day, 92:13 juxtaposes first and last, and 92:16 presents a decisive turning away.
- Surprising reach: Temporal order reaches tonight-deixis, delayed resale, immediate action, milk cessation, crop withering, and interpretation by final outcome.

#### Subchannel A. First, Last, and Unbroken Succession
- Reading type: mixed
- Scene or process: A series begins with a leading member, continues without interruption, and reaches a later or final member.
- Active motifs: beginning and precedence `ء و ل:B001/m01`; lastness after the first `ء خ ر:B001/m01`; foremost guide `ه د ي:B003/m01`; uninterrupted succession `و ل ي:B002/m01`; entitlement by priority `و ل ي:B008/m01`
- Ayah anchors: 92:13 (`ء و ل`: `الأولى`; `ء خ ر`: `الآخرة`); 92:12 (`ه د ي`: `الهدى`); 92:16 (`و ل ي`: `تولى`)
- Synthesis: Precedence opens the series, the guide occupies its front, succession carries it onward, and lastness closes it.

#### Subchannel B. Delay, Promptness, and Deferred Transfer
- Reading type: latent/lexical
- Scene or process: An expected act either occurs without waiting or is postponed into a later transaction.
- Active motifs: delay to a later time `ء خ ر:B002/m01`; acting without lingering `ك ذ ب:B005/m01`; readiness for an act `ء ت ي:B003/m04`; deferred resale `و ل ي:B014/m01`
- Ayah anchors: 92:13 (`ء خ ر`: `الآخرة`); 92:9 and 92:16 (`ك ذ ب`: `كذب`); 92:18 (`ء ت ي`: `يؤتي`); 92:16 (`و ل ي`: `تولى`)
- Synthesis: Readiness and promptness compress the interval before action, while deferment and resale relocate completion to a later time.

#### Subchannel C. Return, Interpretation, and Realized Outcome
- Reading type: latent/lexical
- Scene or process: An affair is returned to its import and judged by the event in which its promise or meaning culminates.
- Active motifs: return to a final state `ء و ل:B002/m01`; interpretation by final import `ء و ل:B002/m02`; realization of promise or prediction `ص د ق:B004/m01`; sound reading of an affair `و ج ه:B008/m01`
- Ayah anchors: 92:13 (`ء و ل`: `الأولى`); 92:6 (`ص د ق`: `صدق`); 92:20 (`و ج ه`: `وجه`)
- Synthesis: Interpretation identifies what speech leads to, and fulfillment makes that final import visible as an event.

#### Subchannel D. Night Activity and Temporal Deixis
- Reading type: latent/lexical
- Scene or process: Action is situated within the night, while "tonight" locates the nearest night relative to the speaker's present.
- Active motifs: undertaking or travel by night `ل ي ل:B002/m01`; entry into nighttime `ل ي ل:B002/m02`; the night nearest the present day `ل ي ل:B003/m01`; daylight as its temporal opposite `ن ه ر:B002/m01`
- Ayah anchors: 92:1 (`ل ي ل`: `الليل`); 92:2 (`ن ه ر`: `النهار`)
- Synthesis: Night functions both as a setting for action and as a deictic interval defined against the present day.

#### Subchannel E. Emergence, Cessation, and Withering
- Reading type: latent/lexical
- Scene or process: Produce or milk appears and grows, then ceases, dries, or passes out of its productive phase.
- Active motifs: emerging crop or palm yield `ء ت ي:B007/m01`; organic increase `ز ك و:B001/m01`; milk that unexpectedly ceases `ك ذ ب:B006/m01`; ripe produce beginning to wither `و ل ي:B016/m01`
- Ayah anchors: 92:18 (`ء ت ي`: `يؤتي`; `ز ك و`: `يتزكى`); 92:9 and 92:16 (`ك ذ ب`: `كذب`); 92:16 (`و ل ي`: `تولى`)
- Synthesis: Emergence and increase form the productive phase, while failed duration and withering form its terminal reversal.

### 3. Route, Orientation, and Turning
- Semantic invariant: A participant locates and follows a course through routes, axes, facing, directional signs, and reversals of approach.
- Surface relation: direct; 92:12 names guidance, 92:16 turns away, and 92:20 seeks a face as its governing direction.
- Surprising reach: Orientation includes junctions, front-rear and upper-left axes, face-level thrusts, repulse, and road markers.

#### Subchannel A. Road, Junction, and Proper Approach
- Reading type: mixed
- Scene or process: A traveler enters a traversable road from an appropriate side and chooses a course at its junction.
- Active motifs: course or bearing `ه د ي:B002/m01`; route and intended direction `و ج ه:B002/m01`; traveled road `ء ت ي:B010/m01`; road junction `ء ت ي:B010/m02`; approach from the proper side `ء ت ي:B003/m01`
- Ayah anchors: 92:12 (`ه د ي`: `الهدى`); 92:20 (`و ج ه`: `وجه`); 92:18 (`ء ت ي`: `يؤتي`)
- Synthesis: The road supplies the traversable space, the junction creates choice, and guidance selects the proper approach and bearing.

#### Subchannel B. Front, Side, Rear, Upper, and Left
- Reading type: latent/lexical
- Scene or process: A body or object is mapped through a stable coordinate frame used to locate movement and relation.
- Active motifs: face or front `و ج ه:B001/m01`; side or flank `ج ن ب:B001/m02`; rear or hindpart `ء خ ر:B003/m01`; upper direction `ع ل و:B005/m01`; left side `ع س ر:B005/m01`; leftward direction `ي س ر:B004/m01`
- Ayah anchors: 92:20 (`و ج ه`: `وجه`; `ع ل و`: `الأعلى`); 92:17 (`ج ن ب`: `سيجنبها`); 92:13 (`ء خ ر`: `الآخرة`); 92:10 (`ع س ر`: `العسرى`; `ي س ر`: `نيسره`)
- Synthesis: Front, rear, side, height, and laterality form one coordinate system for describing bodies, objects, and courses.

#### Subchannel C. Facing, Turning Away, and Repulse
- Reading type: mixed
- Scene or process: A participant faces a target, turns toward or away from it, or actively drives an approaching party back.
- Active motifs: face-to-face encounter `و ج ه:B003/m01`; turning toward a target `و ل ي:B006/m01`; turning away `و ل ي:B007/m01`; repelling an arrival `و ج ه:B014/m01`; decisive penetration or effectiveness `ء ت ي:B013/m01`
- Ayah anchors: 92:20 (`و ج ه`: `وجه`); 92:16 (`و ل ي`: `تولى`); 92:18 (`ء ت ي`: `يؤتي`)
- Synthesis: Facing establishes engagement, turning changes the relation, and repulse makes that reversal an imposed outcome.

#### Subchannel D. Guidance by Beacon and Visible Course
- Reading type: mixed
- Scene or process: A raised visible sign identifies a course and lets a traveler maintain direction.
- Active motifs: gentle guidance to a way `ه د ي:B001/m01`; route beacon or boundary marker `ن و ر:B005/m01`; intended direction `و ج ه:B002/m01`; traveled thoroughfare `ء ت ي:B010/m01`
- Ayah anchors: 92:12 (`ه د ي`: `الهدى`); 92:14 (`ن و ر`: `نارا`); 92:20 (`و ج ه`: `وجه`); 92:18 (`ء ت ي`: `يؤتي`)
- Synthesis: The beacon makes the route perceptible, guidance relates the traveler to it, and the visible course sustains directed movement.

#### Subchannel E. Alignment, Lateral Deviation, and Separation
- Reading type: latent/lexical
- Scene or process: A participant leaves a common line, moves into a side position, and increases the distance from the former route or group.
- Active motifs: lateral deviation from road or group `ع ن د:B002/m01`; widening distance between two things `ش ت ت:B003/m01`; leftward course `ي س ر:B004/m02`; side position `ج ن ب:B001/m03`
- Ayah anchors: 92:19 (`ع ن د`: `عنده`); 92:4 (`ش ت ت`: `شتى`); 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:17 (`ج ن ب`: `سيجنبها`)
- Synthesis: Deviation breaks alignment, side placement gives the new course a direction, and increasing distance converts a momentary turn into separation.

### 4. Endeavor, Fitness, and Resistance
- Semantic invariant: An action succeeds or fails according to effort, suitability, readiness, ease, and the way a body or object yields to force.
- Surface relation: direct; 92:4 names divergent endeavor, and 92:7 and 92:10 contrast prepared ease with hardship.
- Surprising reach: Capacity extends into entitlement, pliant bows, compliant mounts, balanced stance, material hardness, and obstructed childbirth.

#### Subchannel A. Divergent Work and Purposeful Exertion
- Reading type: surface-primary
- Scene or process: Participants direct effort toward different aims, producing distinct kinds and outcomes of work.
- Active motifs: work and earning `س ع ي:B002/m01`; purposeful exertion `س ع ي:B002/m03`; divergent kinds and intentions `ش ت ت:B001/m02`; seeking a desired end `ب غ ي:B001/m01`
- Ayah anchors: 92:4 (`س ع ي`: `سعيكم`; `ش ت ت`: `شتى`); 92:20 (`ب غ ي`: `ابتغاء`)
- Synthesis: Seeking supplies the goal, exertion supplies the operation, and divergence explains why apparently similar effort leads in different directions.

#### Subchannel B. Suitability, Readiness, and Entitlement
- Reading type: latent/lexical
- Scene or process: A participant or object is judged appropriate for a task, becomes ready, and thereby acquires priority.
- Active motifs: inherent suitability `خ ل ق:B005/m01`; fit with a person's condition `ز ك و:B004/m01`; propriety or feasibility `ب غ ي:B002/m01`; readiness `ء ت ي:B003/m04`; entitlement or worthiness `و ل ي:B008/m01`
- Ayah anchors: 92:3 (`خ ل ق`: `خلق`); 92:18 (`ز ك و`: `يتزكى`; `ء ت ي`: `يؤتي`); 92:20 (`ب غ ي`: `ابتغاء`); 92:16 (`و ل ي`: `تولى`)
- Synthesis: Suitability relates capacity to task, readiness marks entry into action, and entitlement names the priority that follows from fit.

#### Subchannel C. Ease, Hardship, and Obstruction
- Reading type: surface-primary
- Scene or process: A course is either opened and prepared or twisted, resisted, and made arduous.
- Active motifs: opened ease and preparedness `ي س ر:B001/m01`; difficulty `ع س ر:B001/m01`; resistance and complication `ع س ر:B004/m01`; arduous sustained handling `ش ق و:B002/m02`
- Ayah anchors: 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:10 (`ع س ر`: `العسرى`); 92:15 (`ش ق و`: `الأشقى`)
- Synthesis: Ease opens the operation, resistance twists or delays it, and hardship names the resulting burden.

#### Subchannel D. Yielding Form and Controlled Motion
- Reading type: latent/lexical
- Scene or process: A body or implement responds to force through softness, flexion, balanced stance, or calm movement.
- Active motifs: pliant bow or compliant mount `ع ط و:B006/m01`; agile yielding movement `ي س ر:B005/m01`; wide balanced stance `ج ن ب:B012/m01`; calm composed gait `ه د ي:B010/m01`; softness `ء ن ث:B002/m01`; hardness and cutting strength `ذ ك ر:B002/m01`
- Ayah anchors: 92:5 (`ع ط و`: `أعطى`); 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:17 (`ج ن ب`: `سيجنبها`); 92:12 (`ه د ي`: `الهدى`); 92:3 (`ء ن ث`: `الأنثى`; `ذ ك ر`: `الذكر`)
- Synthesis: Softness and hardness define material poles, while stance, flexion, and gait show how form channels force.

#### Subchannel E. Condition, Disposition, Soundness, and Incapacity
- Reading type: latent/lexical
- Scene or process: An underlying condition or character makes a person sound and ready, weak and slow, or left without an available alternative.
- Active motifs: present condition or circumstance `ء و ل:B007/m01`; inward disposition and habitual character `خ ل ق:B004/m01`; complete soundness and fitness `ص د ق:B003/m01`; dullness or bodily weakness `ه د ي:B009/m01`; absence of any workable option `ع ن د:B005/m01`
- Ayah anchors: 92:13 (`ء و ل`: `الأولى`); 92:3 (`خ ل ق`: `خلق`); 92:6 (`ص د ق`: `صدق`); 92:12 (`ه د ي`: `الهدى`); 92:19 (`ع ن د`: `عنده`)
- Synthesis: Circumstance supplies the external state, disposition supplies the internal tendency, and soundness or incapacity determines whether action can proceed.

### 5. Transfer, Wealth, and Financial Settlement
- Semantic invariant: Value moves or stops moving through request, grant, possession, charity, substitution, repayment, levy, and release.
- Surface relation: direct; 92:5 gives, 92:8 withholds and claims independence, 92:11 tests wealth's utility, and 92:18-19 join wealth, purification, favor, and recompense.
- Surprising reach: Exchange reaches debt collection, tribute, resale, fixed weights, ransom labor, and payment that substitutes for another condition.

#### Subchannel A. Request, Grant, and Benefaction
- Reading type: mixed
- Scene or process: A need is sought, a transferable good is handed over, and the recipient enters a better condition.
- Active motifs: seeking a desired thing `ب غ ي:B001/m01`; requesting a gift `ع ط و:B005/m01`; handing over a grant `ع ط و:B002/m01`; bestowal `ء ت ي:B002/m01`; benefaction `ح س ن:B002/m03`; favor received `ن ع م:B001/m02`
- Ayah anchors: 92:20 (`ب غ ي`: `ابتغاء`); 92:5 (`ع ط و`: `أعطى`); 92:18 (`ء ت ي`: `يؤتي`); 92:6 and 92:9 (`ح س ن`: `الحسنى`); 92:19 (`ن ع م`: `نعمة`)
- Synthesis: Seeking establishes need, giving transfers the object, and benefaction names the favorable change produced.

#### Subchannel B. Wealth, Withholding, and Claimed Independence
- Reading type: surface-primary
- Scene or process: A holder accumulates property, restrains its circulation, and treats abundance as freedom from need.
- Active motifs: possessed wealth `م و ل:B001/m01`; withholding what should circulate `ب خ ل:B001/m01`; wealth and needlessness `غ ن ي:B001/m01`; material affluence `ي س ر:B003/m01`; financial straitness `ع س ر:B002/m01`
- Ayah anchors: 92:11 and 92:18 (`م و ل`: `ماله`); 92:8 (`ب خ ل`: `بخل`; `غ ن ي`: `استغنى`); 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:10 (`ع س ر`: `العسرى`)
- Synthesis: Accumulation creates apparent capacity, withholding closes transfer, and straitness exposes its opposite.

#### Subchannel C. Charity, Purification, and Productive Increase
- Reading type: mixed
- Scene or process: Property leaves the holder as alms, purifies the giver, and reappears lexically as growth and yield.
- Active motifs: charitable transfer `ص د ق:B006/m01`; obligatory alms `ص د ق:B006/m02`; purification `ز ك و:B002/m01`; organic increase `ز ك و:B001/m01`; emerging produce `ء ت ي:B007/m01`; reverent self-protection `و ق ي:B002/m01`
- Ayah anchors: 92:6 (`ص د ق`: `صدق`); 92:18 (`ز ك و`: `يتزكى`; `ء ت ي`: `يؤتي`); 92:5 and 92:17 (`و ق ي`: `اتقى`, `الأتقى`)
- Synthesis: Redistribution removes private possession, purification describes its effect, and growth recasts subtraction as productive increase.

#### Subchannel D. Recompense, Sufficiency, and Substitution
- Reading type: mixed
- Scene or process: An act is answered by an equivalent return, or one payment or person stands in for another and discharges the claim.
- Active motifs: recompense for an act `ج ز ي:B001/m01`; substitute that suffices `ج ز ي:B002/m01`; charity discharging its owner `ج ز ي:B002/m03`; utility and sufficiency `غ ن ي:B002/m01`
- Ayah anchors: 92:19 (`ج ز ي`: `تجزى`); 92:8 and 92:11 (`غ ن ي`: `استغنى`, `يغني`)
- Synthesis: Recompense matches an earlier act, while sufficiency and substitution close an obligation without reproducing the original object.

#### Subchannel E. Debt, Levy, Resale, and Monetary Unit
- Reading type: latent/lexical
- Scene or process: A quantified obligation is collected, paid as tax, or transferred through a deferred resale.
- Active motifs: collecting a debt `ج ز ي:B003/m01`; demand pressed against an insolvent debtor `ع س ر:B003/m01`; imposed levy `ج ز ي:B004/m01`; tribute paid `ء ت ي:B008/m01`; resale at a known price `و ل ي:B014/m01`; fixed monetary weight `و ق ي:B004/m01`; deferment `ء خ ر:B002/m01`
- Ayah anchors: 92:19 (`ج ز ي`: `تجزى`); 92:10 (`ع س ر`: `العسرى`); 92:18 (`ء ت ي`: `يؤتي`); 92:16 (`و ل ي`: `تولى`); 92:5 and 92:17 (`و ق ي`: `اتقى`, `الأتقى`); 92:13 (`ء خ ر`: `الآخرة`)
- Synthesis: Debt and levy define what is due, the monetary unit measures it, and resale or deferment governs when and to whom it passes.

#### Subchannel F. Redemption Labor and Manumission
- Reading type: latent/lexical
- Scene or process: An enslaved person works toward a fixed price so accumulated value can substitute for bondage and secure release.
- Active motifs: labor toward the price of freedom `س ع ي:B005/m01`; monetary means `م و ل:B001/m01`; payment discharging a condition `ج ز ي:B002/m01`; transferred grant `ع ط و:B002/m01`
- Ayah anchors: 92:4 (`س ع ي`: `سعيكم`); 92:11 and 92:18 (`م و ل`: `ماله`); 92:19 (`ج ز ي`: `تجزى`); 92:5 (`ع ط و`: `أعطى`)
- Synthesis: Labor produces the price, property carries it, transfer makes it available, and substitution converts payment into release.

### 6. Promise, Record, and Binding Obligation
- Semantic invariant: A verbal or written commitment binds participants by promise, vow, record, surety, pact, or injunction.
- Surface relation: direct; 92:6 enacts affirmation, 92:14 warns, and 92:19 frames a claim that is not being repaid.
- Surprising reach: Obligation includes a title deed, assessed surety, self-imposed vow, protected alliance, and idiomatic commands to adhere.

#### Subchannel A. Promise, Fulfillment, and Vow
- Reading type: mixed
- Scene or process: A commitment is declared, made binding, and realized in the act that fulfills it.
- Active motifs: fulfillment of promise `ص د ق:B004/m02`; self-imposed vow `ن ذ ر:B002/m01`; verbal affirmation `ن ع م:B004/m01`; binding injunction `ك ذ ب:B003/m01`
- Ayah anchors: 92:6 (`ص د ق`: `صدق`); 92:14 (`ن ذ ر`: `أنذرتكم`); 92:19 (`ن ع م`: `نعمة`); 92:9 and 92:16 (`ك ذ ب`: `كذب`)
- Synthesis: Declaration creates the commitment, vow or injunction binds it, and fulfillment makes it effective in action.

#### Subchannel B. Certificate, Claim, and Evidentiary Record
- Reading type: latent/lexical
- Scene or process: A claim is fixed in a document and preserved as a reference for truth, debt, or entitlement.
- Active motifs: title deed or certificate of right `ذ ك ر:B008/m01`; truthful statement `ص د ق:B001/m01`; debt claim `ج ز ي:B003/m01`; entitlement `و ل ي:B008/m01`
- Ayah anchors: 92:3 (`ذ ك ر`: `الذكر`); 92:6 (`ص د ق`: `صدق`); 92:19 (`ج ز ي`: `تجزى`); 92:16 (`و ل ي`: `تولى`)
- Synthesis: The document preserves the claim, truthful statement supplies its asserted content, and entitlement defines the right it records.

#### Subchannel C. Pact, Surety, and Protected Alliance
- Reading type: latent/lexical
- Scene or process: Parties establish a durable relation through pact, guaranty, patronage, and loyal aid.
- Active motifs: pact and covenant `ر ب ب:B011/m01`; guarantor or obedient loyal party `ر ض و:B006/m01`; obedient, loving, or guaranteeing trusted person `ر ض ي:B004/m01`; legal patronage `و ل ي:B005/m01`; protected person under a pledge `ه د ي:B007/m01`
- Ayah anchors: 92:20 (`ر ب ب`: `ربه`); 92:21 (`ر ض و`: `يرضى`); 92:16 (`و ل ي`: `تولى`); 92:12 (`ه د ي`: `الهدى`)
- Synthesis: Pact defines the bond, surety secures performance, patronage gives it standing, and loyalty sustains it.

#### Subchannel D. Exhortation, Adherence, and Urging
- Reading type: latent/lexical
- Scene or process: A speaker directs another person toward an act by urging him to take hold of it and treat it as binding.
- Active motifs: idiomatic injunction to adhere `ك ذ ب:B003/m01`; exhortation to take or hold `ع ن د:B006/m01`; summons to come `ع ل و:B006/m01`; spoken declaration `ذ ك ر:B004/m01`
- Ayah anchors: 92:9 and 92:16 (`ك ذ ب`: `كذب`); 92:19 (`ع ن د`: `عنده`); 92:20 (`ع ل و`: `الأعلى`); 92:3 (`ذ ك ر`: `الذكر`)
- Synthesis: Declaration names the duty, exhortation puts it before the hearer, and the summons turns obligation into directed action.

### 7. Hazard, Protection, and Ruin
- Semantic invariant: A threatening force becomes perceptible, is met by protective action, or proceeds into injury, destruction, and compensable loss.
- Surface relation: direct; 92:14-17 joins warning, blazing fire, exposure, and avoidance, while 92:11 names a terminal fall.
- Surprising reach: The same field reaches a side-shield, hoof-protecting gait, cautery, cooking fire, a wound tariff, pleurisy, and the straightening of wood by heat.

#### Subchannel A. Warning, Vigilance, and Protective Barrier
- Reading type: mixed
- Scene or process: Notice of danger awakens caution, after which a person interposes a barrier, withdraws, or is moved beyond the threatened area.
- Active motifs: danger-warning `ن ذ ر:B001/m01`; protective barrier `و ق ي:B001/m01`; self-protective caution `و ق ي:B002/m01`; removal from harm `ج ن ب:B003/m01`; side-shield `ج ن ب:B011/m01`
- Ayah anchors: 92:14 (`ن ذ ر`: `أنذرتكم`); 92:5 and 92:17 (`و ق ي`: `اتقى`, `الأتقى`); 92:17 (`ج ن ب`: `سيجنبها`)
- Synthesis: Warning makes the hazard known, caution changes conduct, and withdrawal or a physical shield prevents contact with the harmful force.

#### Subchannel B. Ignition, Flame, and Scorching Exposure
- Reading type: mixed
- Scene or process: Fire is kindled, rises as a pure flame, and becomes an environment whose heat is entered or endured.
- Active motifs: kindled fire and branding flame `ن و ر:B002/m01`; pure rising flame `ل ظ ي:B001/m01`; named consuming fire `ل ظ ي:B002/m01`; entering and suffering fire `ص ل ي:B003/m01`; severe heat `ل ظ ي:B004/m01`
- Ayah anchors: 92:14 (`ن و ر`: `نارا`; `ل ظ ي`: `تلظى`); 92:15 (`ص ل ي`: `يصلاها`)
- Synthesis: Ignition supplies the fire, flame names its active form, and exposure completes the sequence as direct bodily encounter with destructive heat.

#### Subchannel C. Cooking, Cautery, and Heat-Straightening
- Reading type: latent/lexical
- Scene or process: Controlled heat transforms a material by roasting it, marking it, or making a bent implement straight and usable.
- Active motifs: fire used for roasting and straightening `ص ل ي:B004/m01`; fire-branding of livestock `ن و ر:B002/m02`; intense working heat `ل ظ ي:B004/m02`
- Ayah anchors: 92:14 (`ن و ر`: `نارا`; `ل ظ ي`: `تلظى`); 92:15 (`ص ل ي`: `يصلاها`)
- Synthesis: Heat is not only destructive: under control it cooks, brands, and corrects form by changing material through sustained exposure.

#### Subchannel D. Fall, Affliction, and Bodily Collapse
- Reading type: mixed
- Scene or process: A person or possession is overtaken by calamity, loses stability, and descends into illness, breakage, disappearance, or death.
- Active motifs: falling into a pit or ruin `ر د ي:B003/m01`; arrival of illness or destruction `ء ت ي:B011/m01`; pleuritic side-affliction `ج ن ب:B007/m01`; internal disease that overtakes the body `غ ش ي:B003/m01`; swoon or loss of awareness `غ ش و:B005/m01`, `غ ش ي:B007/m01`; misery and sustained suffering `ش ق و:B002/m01`, `ش ق ي:B001/m01`, `ش ق ي:B002/m02`
- Ayah anchors: 92:11 (`ر د ي`: `تردى`); 92:18 (`ء ت ي`: `يؤتي`); 92:17 (`ج ن ب`: `سيجنبها`); 92:1 (`غ ش و`: `يغشى`); 92:15 (`ش ق و`: `الأشقى`)
- Synthesis: Calamity arrives, bodily integrity or footing fails, and the resulting descent ranges from localized pain to terminal ruin.

#### Subchannel E. Wound, Assessment, and Restitution
- Reading type: latent/lexical
- Scene or process: A bodily wound creates a measurable liability that must be assessed and discharged through compensation.
- Active motifs: wound swelling or progressing toward corruption `ب غ ي:B004/m01`; unstaunched lateral blood-flow `ع ن د:B003/m01`; injury carrying a fixed indemnity `ن ذ ر:B003/m01`; recompense for an incurred act `ج ز ي:B001/m02`; measured equivalence `خ ل ق:B001/m03`; payment that settles a claim `ج ز ي:B003/m02`
- Ayah anchors: 92:20 (`ب غ ي`: `ابتغاء`); 92:19 (`ع ن د`: `عنده`; `ج ز ي`: `تجزى`); 92:14 (`ن ذ ر`: `أنذرتكم`); 92:3 (`خ ل ق`: `خلق`)
- Synthesis: Injury is converted into an obligation by assessment, and equivalence turns bodily loss into a compensable legal amount.

#### Subchannel F. Blow, Projectile, and Forceful Impact
- Reading type: latent/lexical
- Scene or process: An attacker directs force through a blow or thrown stone, producing fracture, displacement, or defensive response.
- Active motifs: stone thrown to strike or break `ر د ي:B001/m01`; side blow causing bodily injury `ج ن ب:B007/m02`; lash or sword laid upon a person `غ ش و:B006/m01`, `غ ش ي:B006/m01`; violent overtaking `ء ت ي:B011/m02`; defensive interposition `و ق ي:B001/m02`
- Ayah anchors: 92:11 (`ر د ي`: `تردى`); 92:17 (`ج ن ب`: `سيجنبها`; `و ق ي`: `الأتقى`); 92:1 (`غ ش و`: `يغشى`); 92:18 (`ء ت ي`: `يؤتي`)
- Synthesis: Projectile and blow are concrete delivery mechanisms of harm, while overtaking names their force and protection supplies the opposed response.

#### Subchannel G. Fury and Violent Outbreak
- Reading type: latent/lexical
- Scene or process: Anger heats inwardly, breaks into aggressive conduct, and culminates in a blow delivered by hand, whip, or sword.
- Active motifs: anger figured as blazing heat `ل ظ ي:B003/m01`; aggressive transgression `ب غ ي:B003/m02`; lash or sword-strike `غ ش و:B006/m02`, `غ ش ي:B006/m02`; presumptuous violent undertaking `ع ط و:B004/m02`
- Ayah anchors: 92:14 (`ل ظ ي`: `تلظى`); 92:20 (`ب غ ي`: `ابتغاء`); 92:1 (`غ ش و`: `يغشى`); 92:5 (`ع ط و`: `أعطى`)
- Synthesis: Heat supplies the shape of rage, transgression removes restraint, and the strike turns inward fury into an outward harmful event.

### 8. Reproduction, Marriage, and Household Formation
- Semantic invariant: Biological pairing and social transfer create offspring, spouses, lineage, and the domestic relations that sustain them.
- Surface relation: direct; 92:3 names creation of male and female, while 92:5, 92:18, and 92:20 supply giving, transfer, and lordly nurture.
- Surprising reach: The field includes estrus, difficult delivery, the opening at the tail during birth, bride-unveiling, dowry, stepchildren, milk increase, and coerced sexual commerce.

#### Subchannel A. Sexed Creation and Pair Formation
- Reading type: mixed
- Scene or process: Living beings are differentiated as male and female and brought into a reproductive pairing.
- Active motifs: creative bringing-into-being `خ ل ق:B002/m01`; completed bodily formation `خ ل ق:B003/m03`; male sex and masculine member `ذ ك ر:B001/m01`; female sex and reproductive femininity `ء ن ث:B001/m01`; mating or sexual covering `غ ش و:B004/m01`, `غ ش ي:B004/m01`; female animal seeking the male `ء ت ي:B012/m01`
- Ayah anchors: 92:3 (`خ ل ق`: `خلق`; `ذ ك ر`: `الذكر`; `ء ن ث`: `الأنثى`); 92:1 (`غ ش و`: `يغشى`); 92:18 (`ء ت ي`: `يؤتي`)
- Synthesis: Sex differentiation supplies the pair, desire brings the animals or persons together, and covering expresses the reproductive union.

#### Subchannel B. Pregnancy, Delivery, and Postpartum Recovery
- Reading type: latent/lexical
- Scene or process: Conception proceeds through difficult labor, bodily opening and presentation, then recovery after birth.
- Active motifs: sexual union `غ ش و:B004/m02`; obstructed or difficult delivery `ع س ر:B006/m01`; hands-first fetal presentation `و ج ه:B010/m01`; birth opening beside the tail `ص ل ي:B006/m01`; rising after childbirth `ع ل و:B011/m01`
- Ayah anchors: 92:1 (`غ ش و`: `يغشى`); 92:10 (`ع س ر`: `العسرى`); 92:20 (`و ج ه`: `وجه`; `ع ل و`: `الأعلى`); 92:15 (`ص ل ي`: `يصلاها`)
- Synthesis: Union initiates reproduction, difficult presentation and bodily opening define the delivery crisis, and rising afterward marks restoration.

#### Subchannel C. Bride, Dowry, and Wedding Transfer
- Reading type: latent/lexical
- Scene or process: A bride is adorned and led into a new household while gifts and an agreed marital payment formalize the union.
- Active motifs: unveiled and adorned bride `ج ل و:B003/m01`; bride-unveiling gift `ج ل و:B009/m01`; bride conducted to her husband `ه د ي:B006/m01`; marriage as protection and sufficiency `غ ن ي:B006/m01`; woman made sufficient by marriage or beauty `غ ن ي:B005/m03`; bridal payment `ص د ق:B007/m01`; bestowed gift `ع ط و:B002/m02`
- Ayah anchors: 92:2 (`ج ل و`: `تجلى`); 92:12 (`ه د ي`: `الهدى`); 92:8 and 92:11 (`غ ن ي`: `استغنى`, `يغني`); 92:6 (`ص د ق`: `صدق`); 92:5 (`ع ط و`: `أعطى`)
- Synthesis: Adornment makes the bride publicly legible, guidance conducts her between households, and dowry and gift complete the social transfer.

#### Subchannel D. Lineage, Stepchildren, and Domestic Nurture
- Reading type: latent/lexical
- Scene or process: A household identifies descent, incorporates dependents, and raises children under sustained care and authority.
- Active motifs: kin and household dependents `ء و ل:B003/m01`; stepchild under a guardian's care `ر ب ب:B005/m01`; legal family patronage `و ل ي:B005/m02`; rearing and corrective nurture `ر ب ب:B002/m01`; remembered lineage `ذ ك ر:B009/m01`
- Ayah anchors: 92:13 (`ء و ل`: `الأولى`); 92:20 (`ر ب ب`: `ربه`); 92:16 (`و ل ي`: `تولى`); 92:3 (`ذ ك ر`: `الذكر`)
- Synthesis: Descent locates the child, patronage establishes belonging, and repeated nurture turns kinship into a functioning household relation.

#### Subchannel E. Milk, Offspring, and Household Increase
- Reading type: latent/lexical
- Scene or process: Successful reproduction appears as abundant offspring, renewed milk, and the productive sufficiency of the herd-dependent home.
- Active motifs: easy increase of milk and offspring `ي س ر:B006/m01`; productive livestock wealth `ن ع م:B005/m01`; new mother or newly productive ewe `ر ب ب:B009/m01`; material sufficiency `غ ن ي:B001/m01`
- Ayah anchors: 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:19 (`ن ع م`: `نعمة`); 92:20 (`ر ب ب`: `ربه`); 92:8 and 92:11 (`غ ن ي`: `استغنى`, `يغني`)
- Synthesis: Birth creates the new animal, lactation converts reproduction into nourishment, and herd increase becomes household sufficiency.

#### Subchannel F. Sexual Coercion and Exploitative Gain
- Reading type: latent/lexical
- Scene or process: Authority turns sexual access into compelled labor and extracts income from another person's body.
- Active motifs: coercive sexual transgression `ب غ ي:B005/m01`; broker who imposes a sexual levy `س ع ي:B007/m01`; compelled sexual covering `غ ش و:B004/m03`
- Ayah anchors: 92:20 (`ب غ ي`: `ابتغاء`); 92:4 (`س ع ي`: `سعيكم`); 92:1 (`غ ش و`: `يغشى`)
- Synthesis: Sexual union is recast as an imposed transaction: coercion supplies control, brokerage organizes the act, and extracted gain identifies its exploitative outcome.

### 9. Presence, Settlement, and Dispersal
- Semantic invariant: Persons and groups are positioned relative to a place or one another through nearness, arrival, residence, estrangement, departure, and scattering.
- Surface relation: indirect; 92:19 places a claim `عنده`, 92:16 turns away, and 92:20 directs purpose toward a face or presence.
- Surprising reach: Spatial relation extends to the stranger inside another people, the side-companion, a weaned child leaving the breast, a migrating household, and a crowd broken into individuals.

#### Subchannel A. Nearness, Side-by-Side Presence, and Attendance
- Reading type: mixed
- Scene or process: A person stands in another's presence or alongside a companion, establishing proximity without yet implying kinship or ownership.
- Active motifs: presence and possession at one's side `ع ن د:B004/m01`; nearness beside a companion `ج ن ب:B002/m01`; facing presence `و ج ه:B003/m01`; person placed next to another `و ل ي:B001/m02`
- Ayah anchors: 92:19 (`ع ن د`: `عنده`); 92:17 (`ج ن ب`: `سيجنبها`); 92:20 (`و ج ه`: `وجه`); 92:16 (`و ل ي`: `تولى`)
- Synthesis: Side, face, and immediate placement give three spatial descriptions of attendance, turning abstract relation into embodied proximity.

#### Subchannel B. Arrival, Visitation, and Residence
- Reading type: latent/lexical
- Scene or process: A traveler arrives, enters a settled place, becomes a guest or resident, and receives the provisions associated with staying.
- Active motifs: arrival and coming `ء ت ي:B001/m01`; entry from abroad `ء ت ي:B006/m01`; visitation or repeated attendance `غ ش و:B003/m01`, `غ ش ي:B005/m01`; pleasant settled dwelling `ن ع م:B011/m01`; residence that removes need `غ ن ي:B004/m01`; household lodging and care `ر ب ب:B007/m01`
- Ayah anchors: 92:18 (`ء ت ي`: `يؤتي`); 92:1 (`غ ش و`: `يغشى`); 92:19 (`ن ع م`: `نعمة`); 92:8 and 92:11 (`غ ن ي`: `استغنى`, `يغني`); 92:20 (`ر ب ب`: `ربه`)
- Synthesis: Coming becomes residence when the entrant is received, lodged, and provisioned, transforming a passing stranger into a situated member or guest.

#### Subchannel C. Migration, Weaning, and Dispersal
- Reading type: latent/lexical
- Scene or process: A formerly gathered unit separates as a person departs, a child is weaned, or a people scatter into distinct locations.
- Active motifs: scattering into separate groups `ش ت ت:B001/m01`; individual separation from a collective `ء ح د:B005/m01`; weaning and withdrawal from nursing `ن ع م:B008/m01`; difficult departure or forced removal `ع س ر:B011/m01`; open departure into view `ج ل و:B004/m01`; young livestock separated from their mothers `و ل ي:B015/m01`
- Ayah anchors: 92:4 (`ش ت ت`: `شتى`); 92:19 (`ء ح د`: `أحد`; `ن ع م`: `نعمة`); 92:10 (`ع س ر`: `العسرى`); 92:2 (`ج ل و`: `تجلى`); 92:16 (`و ل ي`: `تولى`)
- Synthesis: Weaning provides the intimate model of separation, departure enacts it spatially, and scattering scales the same transition from one person to an entire group.

#### Subchannel D. Stranger, Neighbor, and Household Boundary
- Reading type: latent/lexical
- Scene or process: A community distinguishes the nearby outsider from kin and negotiates whether that person remains foreign, becomes a neighbor, or enters the household.
- Active motifs: stranger outside lineage or home `ج ن ب:B003/m02`; entrant from another people `ء ت ي:B006/m02`; side-neighbor and companion `ج ن ب:B002/m02`; household affiliation `ء و ل:B003/m02`; residence under care `ر ب ب:B007/m02`
- Ayah anchors: 92:17 (`ج ن ب`: `سيجنبها`); 92:18 (`ء ت ي`: `يؤتي`); 92:13 (`ء و ل`: `الأولى`); 92:20 (`ر ب ب`: `ربه`)
- Synthesis: Foreignness is relational rather than fixed: proximity makes the outsider a neighbor, and reception or affiliation can carry that person across the domestic boundary.

### 10. Weather, Water, Growth, and Pastoral Provision
- Semantic invariant: Atmospheric and hydraulic forces feed land, plants, and herds, converting movement of water into growth, yield, nourishment, and sometimes scarcity.
- Surface relation: indirect; 92:1-2 supplies the night-day cycle, 92:18 names purifying increase, and 92:19 names favor and livestock provision.
- Surprising reach: The cycle includes a flood arriving from rain elsewhere, a southern wind, a channel blockage, perennial rootstock, camel fodder, curdled milk, and a year when udders go dry.

#### Subchannel A. Rain, Wind, Cloud, and Incoming Flood
- Reading type: latent/lexical
- Scene or process: Wind and cloud carry weather across territory, rain falls, and runoff reaches a place that may not itself have received the storm.
- Active motifs: rain-bearing seeking and overflow `ب غ ي:B006/m01`; flood arriving from another region `ء ت ي:B005/m01`; cloud driven over a place `و ل ي:B010/m01`; rain-bearing cloud and downpour `ر ب ب:B008/m01`; named rain-cloud `ن ه ر:B008/m01`; soft moist southern wind `ن ع م:B009/m01`; southern wind and its cloud `ج ن ب:B006/m01`; side-driving rain or runoff `ع ن د:B003/m02`
- Ayah anchors: 92:20 (`ب غ ي`: `ابتغاء`; `ر ب ب`: `ربه`); 92:18 (`ء ت ي`: `يؤتي`); 92:16 (`و ل ي`: `تولى`); 92:2 (`ن ه ر`: `النهار`); 92:19 (`ن ع م`: `نعمة`; `ع ن د`: `عنده`); 92:17 (`ج ن ب`: `سيجنبها`)
- Synthesis: Mobile air carries cloud, rainfall generates runoff, and the arriving flood connects distant weather to local water supply.

#### Subchannel B. Stream, Basin, and Irrigation Control
- Reading type: latent/lexical
- Scene or process: Flowing water is directed through a channel into a basin, measured, released, or obstructed to regulate irrigation.
- Active motifs: flowing stream or river `ن ه ر:B001/m01`; channel cut or opened for flow `ن ه ر:B003/m01`; watercourse guided into a basin `ء ت ي:B004/m01`; constructed irrigation channel `خ ل ق:B011/m01`; abundant collected water `ر ب ب:B013/m01`
- Ayah anchors: 92:2 (`ن ه ر`: `النهار`); 92:18 (`ء ت ي`: `يؤتي`); 92:3 (`خ ل ق`: `خلق`); 92:20 (`ر ب ب`: `ربه`)
- Synthesis: The stream supplies moving water, the cut channel gives it a route, and basin control turns natural flow into a managed agricultural mechanism.

#### Subchannel C. Rootstock, Blossom, and Vegetative Renewal
- Reading type: latent/lexical
- Scene or process: A persistent rootstock survives adverse conditions, sends out growth, flowers, and renews the plant's visible life.
- Active motifs: plant with enduring root `ج ن ب:B010/m01`; fertile root and branching growth `ر ب ب:B012/m01`; tree blossom `ن و ر:B004/m01`; camel-fodder plant in bloom `ص ل ي:B010/m01`; thriving and purified growth `ز ك و:B001/m01`; female or fruit-bearing plant `ء ن ث:B004/m01`
- Ayah anchors: 92:17 (`ج ن ب`: `سيجنبها`); 92:20 (`ر ب ب`: `ربه`); 92:14 (`ن و ر`: `نارا`); 92:15 (`ص ل ي`: `يصلاها`); 92:18 (`ز ك و`: `يتزكى`); 92:3 (`ء ن ث`: `الأنثى`)
- Synthesis: Durable root and fertile stock carry life through dormancy, blossom makes renewal visible, and thriving growth becomes the plant's completed state.

#### Subchannel D. Yield, Harvest, and Productive Increase
- Reading type: mixed
- Scene or process: Cultivated growth matures into fruit, grain, or another return that can be gathered and treated as increase.
- Active motifs: crop and palm yield `ء ت ي:B007/m01`; growth that becomes abundant `ز ك و:B001/m02`; soil prepared beneath a gourd or melon `و ج ه:B012/m01`; successful acquisition of the sought return `ب غ ي:B001/m02`; beneficent provision `ن ع م:B001/m02`
- Ayah anchors: 92:18 (`ء ت ي`: `يؤتي`; `ز ك و`: `يتزكى`); 92:20 (`و ج ه`: `وجه`; `ب غ ي`: `ابتغاء`); 92:19 (`ن ع م`: `نعمة`)
- Synthesis: Cultivation channels growth toward a sought return, harvest makes that return available, and increase gives the yield its economic and beneficent value.

#### Subchannel E. Herd, Milk, and Subsistence
- Reading type: latent/lexical
- Scene or process: Herd animals graze, reproduce, give milk, and become a store of nourishment and wealth for their keepers.
- Active motifs: livestock as provision and property `ن ع م:B005/m02`; herd management and animal keeping `ر ب ب:B014/m01`; lactating abundance `ي س ر:B006/m02`; freedom from need through herd wealth `غ ن ي:B001/m02`; camel-fodder pasture `ص ل ي:B010/m02`; milk or butter preparation `ك ذ ب:B006/m01`
- Ayah anchors: 92:19 (`ن ع م`: `نعمة`); 92:20 (`ر ب ب`: `ربه`); 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:8 and 92:11 (`غ ن ي`: `استغنى`, `يغني`); 92:15 (`ص ل ي`: `يصلاها`); 92:9 and 92:16 (`ك ذ ب`: `كذب`)
- Synthesis: Pasture sustains the herd, breeding and lactation produce food, and managed animals convert the landscape into recurring household subsistence.

#### Subchannel F. Scarcity, Drying, and Pastoral Dispersal
- Reading type: latent/lexical
- Scene or process: Failed pasture or a hard year reduces milk, weakens household sufficiency, and forces animals or people to disperse.
- Active motifs: year of little camel milk `ج ن ب:B008/m01`; hardship and constrained supply `ع س ر:B001/m02`; separation and scattering `ش ت ت:B001/m03`; need after lost sufficiency `غ ن ي:B001/m03`
- Ayah anchors: 92:17 (`ج ن ب`: `سيجنبها`); 92:10 (`ع س ر`: `العسرى`); 92:4 (`ش ت ت`: `شتى`); 92:8 and 92:11 (`غ ن ي`: `استغنى`, `يغني`)
- Synthesis: Environmental shortfall appears first in milk and provision, then in movement as the settled pastoral unit breaks apart in search of sustenance.

### 11. Truth, Memory, and Verbal Performance
- Semantic invariant: Speech presents, preserves, challenges, or artistically shapes what a community is asked to regard as true and memorable.
- Surface relation: direct; 92:3 names mention, 92:6 and 92:9 oppose truth and denial, and 92:14 performs warning.
- Surprising reach: Verbal action extends from recollection and public rebuke to reputation, sung recitation, exchanged satire, rhyme structure, and blessing.

#### Subchannel A. Truthful Assertion, Denial, and Fabrication
- Reading type: surface-primary
- Scene or process: A proposition is asserted as corresponding to reality, rejected as false, or deliberately fashioned into a deceptive account.
- Active motifs: truthful statement `ص د ق:B001/m01`; false statement or act `ك ذ ب:B001/m01`; attribution of falsehood `ك ذ ب:B002/m01`; deceitful inner self `ك ذ ب:B008/m01`; fabricated discourse `خ ل ق:B007/m01`
- Ayah anchors: 92:6 (`ص د ق`: `صدق`); 92:9 and 92:16 (`ك ذ ب`: `كذب`); 92:3 (`خ ل ق`: `خلق`)
- Synthesis: Assertion offers correspondence, denial contests it, and fabrication explains how an alternative verbal world can be deliberately made.

#### Subchannel B. Recollection, Mention, and Reminder
- Reading type: mixed
- Scene or process: Something absent from immediate awareness is retained, recalled inwardly, voiced, and made available to others as a reminder.
- Active motifs: inward recollection after forgetting `ذ ك ر:B003/m01`; spoken mention and naming `ذ ك ر:B004/m01`; object or act that prompts memory `ذ ك ر:B009/m01`; scholar who cultivates sacred knowledge `ر ب ب:B003/m01`
- Ayah anchors: 92:3 (`ذ ك ر`: `الذكر`); 92:20 (`ر ب ب`: `ربه`)
- Synthesis: Memory moves from preservation in the mind to articulation on the tongue, while a reminder renews the subject's presence for a wider audience.

#### Subchannel C. Rebuke, Accusation, and Public Denunciation
- Reading type: latent/lexical
- Scene or process: A speaker confronts another with severe words, attributes wrongdoing or falsehood, and may carry the accusation to authority.
- Active motifs: harsh verbal rebuke `ن ه ر:B004/m01`; reporting a person to a ruler `س ع ي:B004/m01`; charging another with falsehood `ك ذ ب:B002/m02`; adverse public mention `ذ ك ر:B004/m02`
- Ayah anchors: 92:2 (`ن ه ر`: `النهار`); 92:4 (`س ع ي`: `سعيكم`); 92:9 and 92:16 (`ك ذ ب`: `كذب`); 92:3 (`ذ ك ر`: `الذكر`)
- Synthesis: Rebuke attacks conduct directly, accusation gives the attack a propositional form, and denunciation transports it into a public or governmental forum.

#### Subchannel D. Praise, Honor, and Lasting Renown
- Reading type: latent/lexical
- Scene or process: Worthy action is voiced as praise and accumulates into honor, elevated rank, and remembered reputation.
- Active motifs: honorable mention and renown `ذ ك ر:B007/m01`; manifest public fame `ج ل و:B006/m01`; elevated social rank `ع ل و:B002/m01`; pursuit of noble deeds `س ع ي:B006/m01`; beauty or excellence `ح س ن:B001/m02`; acknowledged beneficence `ن ع م:B003/m01`
- Ayah anchors: 92:3 (`ذ ك ر`: `الذكر`); 92:2 (`ج ل و`: `تجلى`); 92:20 (`ع ل و`: `الأعلى`); 92:4 (`س ع ي`: `سعيكم`); 92:6 and 92:9 (`ح س ن`: `الحسنى`); 92:19 (`ن ع م`: `نعمة`)
- Synthesis: Excellence gives praise its object, noble action earns it, and repeated mention converts a momentary commendation into durable social standing.

#### Subchannel E. Song, Poem, Blessing, and Rhyme
- Reading type: latent/lexical
- Scene or process: Language is patterned for vocal performance, whether as song, exchanged verse, praise, satire, prayer, or metrical closure.
- Active motifs: sung and modulated voice `غ ن ي:B003/m01`; poem offered or exchanged `ه د ي:B011/m01`; rhyme orientation and closing sound `و ج ه:B011/m01`; spoken blessing and praise `ص ل ي:B002/m01`; oral recitation `ذ ك ر:B004/m03`
- Ayah anchors: 92:8 and 92:11 (`غ ن ي`: `استغنى`, `يغني`); 92:12 (`ه د ي`: `الهدى`); 92:20 (`و ج ه`: `وجه`); 92:15 (`ص ل ي`: `يصلاها`); 92:3 (`ذ ك ر`: `الذكر`)
- Synthesis: Voice animates the words, verse and rhyme give them form, and blessing or praise supplies the social purpose of the performance.

### 12. Governance, Rank, and Collective Conflict
- Semantic invariant: Organized groups assign authority and rank, gather intelligence, enforce or resist power, and manage escalation between rivals.
- Surface relation: indirect; 92:20 names lordship and elevation, 92:4 names purposeful action, and 92:14 issues a public warning.
- Surprising reach: Authority includes an alms collector, household service, a ship captain, advance scouts, an informer, failed cavalry charge, feud, and blood-price conciliation.

#### Subchannel A. Lordship, Stewardship, and Corrective Rule
- Reading type: mixed
- Scene or process: A superior possesses responsibility for a domain, directs its affairs, and restores or develops what is under care.
- Active motifs: ownership and sovereign lordship `ر ب ب:B001/m01`; gradual repair and nurture `ر ب ب:B002/m02`; assumption of public authority `و ل ي:B003/m01`; dignitary who represents a people `و ج ه:B006/m01`
- Ayah anchors: 92:20 (`ر ب ب`: `ربه`; `و ج ه`: `وجه`); 92:16 (`و ل ي`: `تولى`)
- Synthesis: Lordship supplies standing, stewardship converts standing into care, and public office makes that relation operative over a household or community.

#### Subchannel B. Public Office, Collection, and Service
- Reading type: latent/lexical
- Scene or process: An appointed official administers a group, collects what is due, and performs the practical service attached to office.
- Active motifs: governor or public collector `س ع ي:B003/m01`; collector and distributor of alms `ص د ق:B006/m02`; attendance and household service `ع ط و:B003/m01`; delegated administration `و ل ي:B003/m02`; office grounded in precedence `ء و ل:B004/m01`
- Ayah anchors: 92:4 (`س ع ي`: `سعيكم`); 92:6 (`ص د ق`: `صدق`); 92:5 (`ع ط و`: `أعطى`); 92:16 (`و ل ي`: `تولى`); 92:13 (`ء و ل`: `الأولى`)
- Synthesis: Appointment creates jurisdiction, service performs its daily work, and collection converts public obligation into administered resources.

#### Subchannel C. Captain, Vanguard, and Directed Company
- Reading type: latent/lexical
- Scene or process: A leader occupies the front or command position and directs a company through a shared course.
- Active motifs: captain of sailors `ر ب ب:B017/m01`; leader or foremost guide `ه د ي:B003/m01`; command over an undertaking `و ل ي:B003/m03`; forward rank and precedence `ء و ل:B001/m03`
- Ayah anchors: 92:20 (`ر ب ب`: `ربه`); 92:12 (`ه د ي`: `الهدى`); 92:16 (`و ل ي`: `تولى`); 92:13 (`ء و ل`: `الأولى`)
- Synthesis: The vanguard makes direction visible, command coordinates the company, and the captain embodies both functions in a moving collective.

#### Subchannel D. Scouts, Informer, and Mobilizing Alert
- Reading type: latent/lexical
- Scene or process: Advance observers detect a threat, information is carried inward, and an alarm moves the group from ignorance to readiness.
- Active motifs: scouts preceding an army `ب غ ي:B008/m01`; informer reporting to authority `س ع ي:B004/m02`; warning that awakens caution `ن ذ ر:B001/m02`; foremost guide or advance element `ه د ي:B003/m02`
- Ayah anchors: 92:20 (`ب غ ي`: `ابتغاء`); 92:4 (`س ع ي`: `سعيكم`); 92:14 (`ن ذ ر`: `أنذرتكم`); 92:12 (`ه د ي`: `الهدى`)
- Synthesis: Scouts acquire the information, the informer transmits it, and warning turns intelligence into collective preparation.

#### Subchannel E. Transgression, Arrogance, and Coercive Power
- Reading type: latent/lexical
- Scene or process: An actor exceeds a legitimate boundary, rejects correction, and uses superior position to compel others.
- Active motifs: aggressive transgression beyond right `ب غ ي:B003/m01`; obstinate rejection of truth `ع ن د:B001/m01`; arrogant elevation over others `ع ل و:B003/m01`; presumptuous seizure of what is not due `ع ط و:B004/m01`; coercive harshness `ع س ر:B008/m01`
- Ayah anchors: 92:20 (`ب غ ي`: `ابتغاء`; `ع ل و`: `الأعلى`); 92:19 (`ع ن د`: `عنده`); 92:5 (`ع ط و`: `أعطى`); 92:10 (`ع س ر`: `العسرى`)
- Synthesis: Boundary crossing begins the abuse, arrogance legitimates it in the actor's own view, and coercion converts claimed superiority into force over another.

#### Subchannel F. Contest, Overtaking, and Dominance
- Reading type: latent/lexical
- Scene or process: Rival actors engage in the same undertaking until one surpasses the other and gains control of the object or goal.
- Active motifs: competitive striving and victory `س ع ي:B008/m01`; prevailing in reciprocal recompense `ج ز ي:B005/m01`; prevailing in a contest of taking `ع ط و:B007/m01`; victory in a contest of placation `ر ض و:B005/m01`, `ر ض ي:B002/m01`; victory through sustained struggle `ش ق و:B003/m01`, `ش ق ي:B003/m01`; reaching and possessing the goal `و ل ي:B012/m01`; overcoming and mastery `ع ل و:B004/m01`
- Ayah anchors: 92:4 (`س ع ي`: `سعيكم`); 92:19 (`ج ز ي`: `تجزى`); 92:5 (`ع ط و`: `أعطى`); 92:21 (`ر ض و`: `يرضى`); 92:15 (`ش ق و`: `الأشقى`); 92:16 (`و ل ي`: `تولى`); 92:20 (`ع ل و`: `الأعلى`)
- Synthesis: Shared effort creates the contest, overtaking resolves relative position, and possession or mastery names the victor's resulting control.

#### Subchannel G. Charge, Courage, and Repulse
- Reading type: latent/lexical
- Scene or process: A combatant advances into contact or falters, while the opposing force receives, turns back, or strikes the charge.
- Active motifs: failed charge or cowardly halt `ك ذ ب:B004/m01`; charge made good in action `ص د ق:B004/m03`; repulse from the front `و ج ه:B014/m01`; face-level thrust `ي س ر:B009/m02`; forceful effective penetration `ء ت ي:B013/m01`; defensive barrier `و ق ي:B001/m03`
- Ayah anchors: 92:9 and 92:16 (`ك ذ ب`: `كذب`); 92:6 (`ص د ق`: `صدق`); 92:20 (`و ج ه`: `وجه`); 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:18 (`ء ت ي`: `يؤتي`); 92:5 and 92:17 (`و ق ي`: `اتقى`, `الأتقى`)
- Synthesis: Courage is tested by whether advance reaches contact; penetration fulfills the charge, while repulse and protection describe the counterforce.

#### Subchannel H. Feud, Mediation, and Reconciliation
- Reading type: latent/lexical
- Scene or process: Hostility persists between groups until a mediator spends effort, reputation, or compensation to restore alliance.
- Active motifs: active feud and enmity `ن و ر:B007/m01`; noble effort toward peace `س ع ي:B006/m02`; friendship and mutual aid `و ل ي:B004/m01`; sincere social bond `ص د ق:B005/m02`; recompense that settles retaliation `ج ز ي:B001/m03`
- Ayah anchors: 92:14 (`ن و ر`: `نارا`); 92:4 (`س ع ي`: `سعيكم`); 92:16 (`و ل ي`: `تولى`); 92:6 (`ص د ق`: `صدق`); 92:19 (`ج ز ي`: `تجزى`)
- Synthesis: Feud keeps injury socially active, mediation redirects competitive action toward settlement, and compensation permits hostility to become renewed alliance.

### 13. Gait, Handling, Pursuit, and Ascent
- Semantic invariant: Bodies and animals are distinguished by how they advance, are guided, negotiate terrain, pursue a target, or reach a positional goal.
- Surface relation: direct; 92:4 names directed movement, 92:7 and 92:10 contrast ease and difficulty, 92:12 names guidance, and 92:20 names elevation.
- Surprising reach: Motion includes a swaying assisted walk, camel foreleg return, lateral leading, hoof tenderness, display gait, second place in a race, mountain ledges, a hunter's trap, and a stone-throwing game.

#### Subchannel A. Purposeful Walking and Assisted Gait
- Reading type: mixed
- Scene or process: A person or animal advances toward a goal, sometimes with a rapid walk and sometimes by leaning on companions through weakness.
- Active motifs: purposeful rapid walking `س ع ي:B001/m01`; travel on foot without a mount `ن ع م:B012/m01`; swaying walk assisted by two others `ه د ي:B008/m01`; weak heavy movement `ه د ي:B009/m02`; easy and tractable movement `ي س ر:B005/m01`; laborious or uneven walking `ع س ر:B009/m01`; bounding gait between walk and run `ر د ي:B002/m01`
- Ayah anchors: 92:4 (`س ع ي`: `سعيكم`); 92:19 (`ن ع م`: `نعمة`); 92:12 (`ه د ي`: `الهدى`); 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:10 (`ع س ر`: `العسرى`); 92:11 (`ر د ي`: `تردى`)
- Synthesis: Intention supplies the route, while ease, assistance, and uneven propulsion distinguish the bodily mechanisms by which the traveler advances.

#### Subchannel B. Equine Display, Stance, and Controlled Motion
- Reading type: latent/lexical
- Scene or process: A horse displays energy in its run yet remains usable through balanced stance, compliance, and composed movement.
- Active motifs: proud playful running `ب غ ي:B007/m01`; wide-set balanced legs `ج ن ب:B012/m01`; pliant response to the handler `ع ط و:B006/m01`; calm well-formed gait `ه د ي:B010/m01`; bounding or heavy-footed motion `ر د ي:B002/m02`
- Ayah anchors: 92:20 (`ب غ ي`: `ابتغاء`); 92:17 (`ج ن ب`: `سيجنبها`); 92:5 (`ع ط و`: `أعطى`); 92:12 (`ه د ي`: `الهدى`); 92:11 (`ر د ي`: `تردى`)
- Synthesis: Display gives the animal visible vigor, conformation stabilizes it, and compliance turns raw motion into a controlled riding gait.

#### Subchannel C. Camel Foreleg Return and Lateral Leading
- Reading type: latent/lexical
- Scene or process: A camel returns its forelegs rhythmically while a handler takes hold and leads it beside the body.
- Active motifs: returning camel forelegs in travel `ء ت ي:B009/m01`; taking hold by hand `ع ط و:B001/m01`; leading an animal alongside `ج ن ب:B005/m01`; deliberate animal progression `س ع ي:B001/m02`
- Ayah anchors: 92:18 (`ء ت ي`: `يؤتي`); 92:5 (`ع ط و`: `أعطى`); 92:17 (`ج ن ب`: `سيجنبها`); 92:4 (`س ع ي`: `سعيكم`)
- Synthesis: Foreleg return defines the animal's propulsion, hand contact establishes control, and side-leading coordinates handler and camel as one moving unit.

#### Subchannel D. Hoof Pain and Protective Gait
- Reading type: latent/lexical
- Scene or process: A horse senses painful ground or a tender hoof, shortens its step, and relies on careful handling or protective tack.
- Active motifs: hoof-protecting hesitation and slight lameness `و ق ي:B003/m01`; animal led beside the handler `ج ن ب:B005/m02`; calm non-panicked movement `ه د ي:B010/m02`; difficult or compromised gait `ع س ر:B009/m02`
- Ayah anchors: 92:5 and 92:17 (`و ق ي`: `اتقى`, `الأتقى`); 92:17 (`ج ن ب`: `سيجنبها`); 92:12 (`ه د ي`: `الهدى`); 92:10 (`ع س ر`: `العسرى`)
- Synthesis: Pain changes the step before it stops movement entirely; caution, lateral control, and composure together protect the affected hoof.

#### Subchannel E. Race, Second Place, and Overtaking
- Reading type: latent/lexical
- Scene or process: Racers pursue one finish, occupy ordered positions, and may overtake until one reaches the goal first and another follows at the leader's flank.
- Active motifs: competitive striving `س ع ي:B008/m02`; second racer following the winner `ص ل ي:B007/m01`; reaching and possessing the finish `و ل ي:B012/m02`; victory in reciprocal contest `ج ز ي:B005/m02`; victory in taking `ع ط و:B007/m02`
- Ayah anchors: 92:4 (`س ع ي`: `سعيكم`); 92:15 (`ص ل ي`: `يصلاها`); 92:16 (`و ل ي`: `تولى`); 92:19 (`ج ز ي`: `تجزى`); 92:5 (`ع ط و`: `أعطى`)
- Synthesis: One course creates comparable effort, overtaking changes relative order, and the named second-place position preserves the race's embodied geometry.

#### Subchannel F. Mountain Ascent, Ledge, and Refuge
- Reading type: latent/lexical
- Scene or process: A traveler climbs from lower ground, uses a long accessible ledge, and reaches a high place that can serve as seat or refuge.
- Active motifs: long climbable mountain ledge `ش ق و:B004/m01`, `ش ق ي:B004/m01`; physical ascent and elevation `ع ل و:B001/m01`; retreat to a mountain place `ء و ل:B009/m01`; difficult exertion `ش ق و:B002/m02`
- Ayah anchors: 92:15 (`ش ق و`: `الأشقى`); 92:20 (`ع ل و`: `الأعلى`); 92:13 (`ء و ل`: `الأولى`)
- Synthesis: Difficulty belongs to the climb, the ledge provides a practicable path and resting place, and elevation yields the protected destination.

#### Subchannel G. Hunter, Quarry, and Snare
- Reading type: latent/lexical
- Scene or process: A hunter exposes or sights quarry, gives chase, and uses a snare to arrest an animal that may run and then turn to look back.
- Active motifs: quarry brought into the open `ج ل و:B008/m01`; trap or snare set for prey `ص ل ي:B005/m01`; wild animal running then stopping `ك ذ ب:B007/m01`; taking hold of the catch `ع ط و:B001/m02`; purposeful pursuit `س ع ي:B001/m03`
- Ayah anchors: 92:2 (`ج ل و`: `تجلى`); 92:15 (`ص ل ي`: `يصلاها`); 92:9 and 92:16 (`ك ذ ب`: `كذب`); 92:5 (`ع ط و`: `أعطى`); 92:4 (`س ع ي`: `سعيكم`)
- Synthesis: Exposure creates sight of the quarry, pursuit closes distance, and the snare converts moving prey into a graspable catch.

#### Subchannel H. Throwing Game and Stone Target
- Reading type: latent/lexical
- Scene or process: Players cast stones or missiles toward a target, combining measured difficulty, projectile force, and the possibility of entrapment or a scored hit.
- Active motifs: throwing game or difficult cast `ع س ر:B013/m01`; stone projectile used to strike `ر د ي:B001/m02`; catching device or target snare `ص ل ي:B005/m02`; hand taking and casting `ع ط و:B001/m03`
- Ayah anchors: 92:10 (`ع س ر`: `العسرى`); 92:11 (`ر د ي`: `تردى`); 92:15 (`ص ل ي`: `يصلاها`); 92:5 (`ع ط و`: `أعطى`)
- Synthesis: The hand launches the stone, distance and obstruction create difficulty, and contact with target or snare resolves the throw.

### 14. Bodily Form, Marking, and Lifecycle
- Semantic invariant: The body is recognized through its proportion, paired parts, visible marks, movement disposition, and transitions from birth through maturity and age.
- Surface relation: direct; 92:3 names created sex, 92:20 names the face and elevation, and 92:2 supplies visible disclosure.
- Surprising reach: Bodily legibility includes baldness, tattoo pigment, facial blows, tooth spacing, paired organs, birth anatomy, postpartum recovery, aging, skittishness, and composed bearing.

#### Subchannel A. Balanced Form, Stature, and Beauty
- Reading type: mixed
- Scene or process: A body is shaped in proportion, presents a recognizable front, and is evaluated for stature, symmetry, and beauty.
- Active motifs: bodily formation and proportion `خ ل ق:B003/m01`; visible face and front `و ج ه:B001/m01`; beauty and excellence of form `ح س ن:B001/m03`; tall substantial stature `ع ل و:B010/m01`
- Ayah anchors: 92:3 (`خ ل ق`: `خلق`); 92:20 (`و ج ه`: `وجه`; `ع ل و`: `الأعلى`); 92:6 and 92:9 (`ح س ن`: `الحسنى`)
- Synthesis: Formation establishes the body's proportions, face gives it a public front, and stature and beauty express how the completed form is socially perceived.

#### Subchannel B. Head, Baldness, Facial Mark, and Blow
- Reading type: latent/lexical
- Scene or process: The head and face become identifying surfaces through exposed scalp, whitened or darkened marks, tattoo pigment, and injury.
- Active motifs: bald or uncovered scalp `ج ل و:B005/m01`; soot pigment used for tattoo or kohl `ن و ر:B008/m01`; blow delivered to the face `و ج ه:B013/m01`; face as visible bodily surface `و ج ه:B001/m02`
- Ayah anchors: 92:2 (`ج ل و`: `تجلى`); 92:14 (`ن و ر`: `نارا`); 92:20 (`و ج ه`: `وجه`)
- Synthesis: Exposure makes the head legible, pigment fixes a sign on the skin, and a blow turns the same public surface into the site of injury.

#### Subchannel C. Paired Organs, Sides, and Body Lines
- Reading type: latent/lexical
- Scene or process: Anatomy is organized through bilateral pairs, lateral sides, and longitudinal lines that locate parts relative to the body's center.
- Active motifs: paired bodily organs `ء ن ث:B003/m01`; paired unit or twinning `ز ك و:B005/m02`; bodily side and flank `ج ن ب:B001/m01`; lengthwise body line `ي س ر:B008/m01`; back and tail-side anatomy `ص ل ي:B006/m02`
- Ayah anchors: 92:3 (`ء ن ث`: `الأنثى`); 92:18 (`ز ك و`: `يتزكى`); 92:17 (`ج ن ب`: `سيجنبها`); 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:15 (`ص ل ي`: `يصلاها`)
- Synthesis: Pairing gives bilateral structure, side and line provide coordinates, and the back-tail region shows how those coordinates locate a concrete anatomical zone.

#### Subchannel D. Tooth Spacing, Smile, and Adorned Beauty
- Reading type: latent/lexical
- Scene or process: Separated teeth become visible in the face and contribute to a smiling or conventionally beautiful appearance.
- Active motifs: spaced or separated teeth `ش ت ت:B002/m01`; beautiful visible form `ح س ن:B001/m04`; face as presentation surface `و ج ه:B001/m03`; beauty sufficient without adornment `غ ن ي:B005/m02`
- Ayah anchors: 92:4 (`ش ت ت`: `شتى`); 92:6 and 92:9 (`ح س ن`: `الحسنى`); 92:20 (`و ج ه`: `وجه`); 92:8 and 92:11 (`غ ن ي`: `استغنى`, `يغني`)
- Synthesis: Tooth spacing is a small structural feature whose visibility in the face becomes a marker of beauty and self-sufficient adornment.

#### Subchannel E. Birth-Newness, Recovery, and Old Age
- Reading type: latent/lexical
- Scene or process: A life stage begins in recent birth, passes through restoration after bodily crisis, and turns toward decline in old age.
- Active motifs: recent birth and newness `ر ب ب:B009/m02`; recovery after childbirth or illness `ع ل و:B011/m02`; old age and life's turning away `و ج ه:B009/m01`; first stage and later succession `ء و ل:B001/m04`; final stage `ء خ ر:B001/m02`
- Ayah anchors: 92:20 (`ر ب ب`: `ربه`; `ع ل و`: `الأعلى`; `و ج ه`: `وجه`); 92:13 (`ء و ل`: `الأولى`; `ء خ ر`: `الآخرة`)
- Synthesis: Newness identifies proximity to birth, recovery restores upright life, and aging reframes temporal succession as a visible bodily turn.

#### Subchannel F. Skittishness, Chastity, and Composed Bearing
- Reading type: latent/lexical
- Scene or process: A person or animal responds to approach either by recoiling and preserving distance or by remaining calm in an orderly posture.
- Active motifs: skittish recoil and chaste avoidance `ن و ر:B006/m01`; calm dignified bearing `ه د ي:B010/m03`; pliant controlled movement `ع ط و:B006/m02`; removal from improper contact `ج ن ب:B003/m03`
- Ayah anchors: 92:14 (`ن و ر`: `نارا`); 92:12 (`ه د ي`: `الهدى`); 92:5 (`ع ط و`: `أعطى`); 92:17 (`ج ن ب`: `سيجنبها`)
- Synthesis: Recoil preserves bodily and social distance, while composure and controlled motion express the positive form of guarded bearing.

### 15. Crafted Matter, Implements, and Bearing Layers
- Semantic invariant: Raw or prepared materials are shaped, layered, contained, marked, or hardened so that they can bear, cover, divide, grind, preserve, or adorn.
- Surface relation: indirect; 92:3 names making, 92:5 names hand transfer, 92:14-15 supplies fire, and 92:20 names upper placement and visible surface.
- Surprising reach: The field includes a grinding slab, sealed stone, bier or tent frame, saddle underlay, gaming-arrow case, deceptive textile, tattoo soot, depilatory paste, thick syrup, and a vessel for maturing drink.

#### Subchannel A. Stone Impact, Grinding, and Hard Surface
- Reading type: latent/lexical
- Scene or process: Stone is selected for density and flatness, then used as a projectile, breaking implement, grinding bed, or resistant working surface.
- Active motifs: stone cast to strike or fracture `ر د ي:B001/m03`; broad grinding slab `ص ل ي:B009/m02`; hard straight material `ص د ق:B002/m01`; smooth solid stone surface `خ ل ق:B008/m01`
- Ayah anchors: 92:11 (`ر د ي`: `تردى`); 92:15 (`ص ل ي`: `يصلاها`); 92:6 (`ص د ق`: `صدق`); 92:3 (`خ ل ق`: `خلق`)
- Synthesis: Density carries impact, breadth permits grinding, and smooth hardness makes stone a stable material for both force and preparation.

#### Subchannel B. Smooth Barrier, Seal, and Structural Closure
- Reading type: latent/lexical
- Scene or process: A continuous hard surface is made smooth and without opening, allowing it to seal, obstruct, or protect an enclosed space.
- Active motifs: smooth unbroken surface `خ ل ق:B008/m02`; stone-like closure without aperture `خ ل ق:B012/m01`; solid straight implement `ص د ق:B002/m02`; protective side barrier `ج ن ب:B011/m02`
- Ayah anchors: 92:3 (`خ ل ق`: `خلق`); 92:6 (`ص د ق`: `صدق`); 92:17 (`ج ن ب`: `سيجنبها`)
- Synthesis: Smoothness removes gaps, solidity resists penetration, and side placement converts the material property into a functional barrier.

#### Subchannel C. Carrying Frame, Upper Load, and Saddle Layer
- Reading type: latent/lexical
- Scene or process: A frame or animal back receives a sequence of bearing layers, with an underlay below and an added load above.
- Active motifs: carrying frame or tent pole `ء و ل:B008/m01`; upper added burden `ع ل و:B008/m01`; saddlecloth beneath the riding gear `و ل ي:B011/m01`; shoulder garment or covering `ر د ي:B004/m01`
- Ayah anchors: 92:13 (`ء و ل`: `الأولى`); 92:20 (`ع ل و`: `الأعلى`); 92:16 (`و ل ي`: `تولى`); 92:11 (`ر د ي`: `تردى`)
- Synthesis: The frame or body bears the assembly, the underlayer cushions contact, and the upper addition completes a stable vertical stack.

#### Subchannel D. Lot Vessel, Marked Arrows, and Division
- Reading type: latent/lexical
- Scene or process: Marked arrows are gathered in a container, drawn for a game or allotment, and used to divide a slaughtered animal.
- Active motifs: leather vessel holding lot-arrows `ر ب ب:B010/m01`; gambling arrows and division of the carcass `ي س ر:B007/m01`; named elevated lot-arrow `ع ل و:B009/m01`; hand drawing or taking a lot `ع ط و:B001/m04`
- Ayah anchors: 92:20 (`ر ب ب`: `ربه`; `ع ل و`: `الأعلى`); 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:5 (`ع ط و`: `أعطى`)
- Synthesis: The case preserves the set, the hand selects an arrow, and the mark on the lot determines how a shared carcass is apportioned.

#### Subchannel E. Garment, Wear, Dye, and Surface Renewal
- Reading type: latent/lexical
- Scene or process: Cloth is worn on the body, loses its nap through use, and receives dye or scent that renews its visible surface.
- Active motifs: worn cloth stripped of its nap `خ ل ق:B009/m01`; shoulder garment and sash `ر د ي:B004/m02`; feminine perfume or dye that colors cloth `ء ن ث:B007/m01`
- Ayah anchors: 92:3 (`خ ل ق`: `خلق`; `ء ن ث`: `الأنثى`); 92:11 (`ر د ي`: `تردى`)
- Synthesis: Wearing degrades the fabric, while dye and scent transform the used textile and give its surface a renewed social presentation.

#### Subchannel F. Polishing, Pigment, Perfume, and Body Treatment
- Reading type: latent/lexical
- Scene or process: A substance is ground or prepared, then applied to metal, eye, skin, hair, or cloth to polish, color, scent, mark, or remove hair.
- Active motifs: polish and eye-clearing kohl `ج ل و:B002/m02`; soot used as kohl or tattoo pigment `ن و ر:B008/m02`; depilatory coating `ن و ر:B009/m01`; prepared perfume paste `خ ل ق:B010/m01`; feminine scent that colors cloth `ء ن ث:B007/m02`; grinding stone for aromatic material `ص ل ي:B009/m03`
- Ayah anchors: 92:2 (`ج ل و`: `تجلى`); 92:14 (`ن و ر`: `نارا`); 92:3 (`خ ل ق`: `خلق`; `ء ن ث`: `الأنثى`); 92:15 (`ص ل ي`: `يصلاها`)
- Synthesis: Grinding prepares the material, application changes a receiving surface, and the result ranges from clearer sight and luster to durable color, scent, or bodily alteration.

#### Subchannel G. Heating, Thickening, and Viscous Compound
- Reading type: latent/lexical
- Scene or process: Milk, oil residue, honey, tar, or another liquid is heated or left until it coagulates into a thick preparation used in food, medicine, or material treatment.
- Active motifs: liquid curdling at its final state `ء و ل:B005/m01`; thick syrup or prepared residue `ر ب ب:B006/m01`; heating and roasting process `ص ل ي:B004/m02`; measured preparation before action `خ ل ق:B001/m04`
- Ayah anchors: 92:13 (`ء و ل`: `الأولى`); 92:20 (`ر ب ب`: `ربه`); 92:15 (`ص ل ي`: `يصلاها`); 92:3 (`خ ل ق`: `خلق`)
- Synthesis: Time and heat alter consistency, measurement controls the preparation, and thickening turns a mobile liquid into a preservable or applicable compound.

#### Subchannel H. Beverage Vessel and Maturation
- Reading type: latent/lexical
- Scene or process: A drink is enclosed in a vessel for several days so that time and containment improve or complete it.
- Active motifs: vessel in which drink matures `ء و ل:B010/m01`; liquid reaching a thickened or completed state `ء و ل:B005/m02`; enclosing cover `غ ش و:B001/m03`; pleasant consumption and ease `ن ع م:B002/m01`
- Ayah anchors: 92:13 (`ء و ل`: `الأولى`); 92:1 (`غ ش و`: `يغشى`); 92:19 (`ن ع م`: `نعمة`)
- Synthesis: The vessel fixes the liquid in place, covering protects the interval, and elapsed time changes the drink toward a valued finished state.

#### Subchannel I. Cord Twisting, Flexion, and Tension
- Reading type: latent/lexical
- Scene or process: Fibers are turned downward into a cord, then tension and controlled yielding make the line or bow usable.
- Active motifs: downward twisting of fibers `ي س ر:B009/m01`; smooth finished cord `خ ل ق:B008/m03`; pliant bow under force `ع ط و:B006/m04`; measured shaping before use `خ ل ق:B001/m06`
- Ayah anchors: 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:3 (`خ ل ق`: `خلق`); 92:5 (`ع ط و`: `أعطى`)
- Synthesis: Twist binds separate fibers, smoothing gives the cord a continuous surface, and controlled flexion stores force without structural failure.

### 16. Measure, Number, and Degree
- Semantic invariant: Entities and actions are rendered comparable by weight, count, sequence, amount, or intensity.
- Surface relation: direct; 92:3 presents a pair, 92:13 orders first and last, 92:19 negates any single claimant, and 92:21 closes with a future degree of satisfaction.
- Surprising reach: Quantification includes an ounce weight, the one-versus-pair distinction in a hand game, Sunday as first day, very small amounts, surplus beyond measure, and an idiom for utmost effort.

#### Subchannel A. Estimation, Weight, and Measured Unit
- Reading type: latent/lexical
- Scene or process: Material is estimated before use and expressed through an established unit so that portions or values can be compared.
- Active motifs: prior estimation and measurement `خ ل ق:B001/m05`; fixed ounce weight `و ق ي:B004/m01`; slight measured amount `ي س ر:B002/m01`
- Ayah anchors: 92:3 (`خ ل ق`: `خلق`); 92:5 and 92:17 (`و ق ي`: `اتقى`, `الأتقى`); 92:7 and 92:10 (`ي س ر`: `نيسره`)
- Synthesis: Estimation creates a scale, the named weight stabilizes it, and small or monetary amounts become commensurable within that system.

#### Subchannel B. One, Pair, and Multitude
- Reading type: mixed
- Scene or process: A set is distinguished as undivided one, any single member, a pair, or a gathered plurality.
- Active motifs: absolute oneness `ء ح د:B001/m02`; individual under an unrestricted negative `ء ح د:B002/m01`; single member `ء ح د:B003/m02`; paired or even unit `ز ك و:B005/m03`; gathered multitude `ر ب ب:B004/m02`
- Ayah anchors: 92:19 (`ء ح د`: `أحد`); 92:18 (`ز ك و`: `يتزكى`); 92:20 (`ر ب ب`: `ربه`)
- Synthesis: One names indivisibility or an individual, pairing creates the smallest relation, and multitude scales those units into a collective.

#### Subchannel C. Littleness, Sufficiency, and Excess
- Reading type: latent/lexical
- Scene or process: An amount is judged as slight, enough for the need, or greater than the expected measure.
- Active motifs: small amount or short duration `ي س ر:B002/m02`; sufficient replacement `غ ن ي:B002/m02`; increase beyond measure `ر د ي:B005/m01`; abundant good or evil `ج ن ب:B009/m01`; intensified addition `ن ع م:B010/m01`
- Ayah anchors: 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:8 and 92:11 (`غ ن ي`: `استغنى`, `يغني`); 92:11 (`ر د ي`: `تردى`); 92:17 (`ج ن ب`: `سيجنبها`); 92:19 (`ن ع م`: `نعمة`)
- Synthesis: Littleness locates the lower bound, sufficiency marks functional adequacy, and surplus names the point at which addition exceeds the ordinary measure.

#### Subchannel D. Utmost Effort and Intensified Action
- Reading type: latent/lexical
- Scene or process: An action is carried to its limit, with effort or repetition indicating maximal degree rather than a different kind of act.
- Active motifs: utmost exertion or limit `ح س ن:B005/m01`; intensified continuation `ن ع م:B010/m02`; excess in word or gift `ر د ي:B005/m02`; arduous sustained effort `ش ق ي:B002/m01`
- Ayah anchors: 92:6 and 92:9 (`ح س ن`: `الحسنى`); 92:19 (`ن ع م`: `نعمة`); 92:11 (`ر د ي`: `تردى`); 92:15 (`ش ق و`: `الأشقى`)
- Synthesis: Effort supplies the base action, continuation magnifies it, and excess marks performance carried beyond its ordinary stopping point.

#### Subchannel E. First-Day Naming and Day-Opening
- Reading type: mixed
- Scene or process: A calendrical day is designated as the first member of a weekly sequence and is recognized through the opening face of daylight.
- Active motifs: first position and Sunday `ء ح د:B004/m01`; opening of the day `و ج ه:B007/m01`; daylight interval `ن ه ر:B002/m02`
- Ayah anchors: 92:19 (`ء ح د`: `أحد`); 92:20 (`و ج ه`: `وجه`); 92:2 (`ن ه ر`: `النهار`)
- Synthesis: Ordinal naming locates Sunday within the cycle, while the opening face of day gives firstness a recurring perceptible form.

### 17. Naming, Grammar, and Designation
- Semantic invariant: Language classifies referents and relations by gender, particle, proper name, or a descriptive label transferred from one entity to another.
- Surface relation: direct; 92:3 grammatically and lexically contrasts male and female, 92:19 uses the indefinite individual, and 92:20 uses relational expressions of face, lordship, and elevation.
- Surprising reach: The field includes grammatical feminization, quantification under negation, prepositional government, named mountains and tribes, a woman's name tied to night, and a youth designated Yasar.

#### Subchannel A. Grammatical Gender and Sexed Designation
- Reading type: mixed
- Scene or process: A referent is classified as masculine or feminine through lexical designation, morphological marking, and agreement.
- Active motifs: grammatical feminization of a word `ء ن ث:B005/m01`; masculine designation `ذ ك ر:B001/m03`; female designation `ء ن ث:B001/m02`; visible form that motivates classification `خ ل ق:B003/m02`
- Ayah anchors: 92:3 (`ء ن ث`: `الأنثى`; `ذ ك ر`: `الذكر`; `خ ل ق`: `خلق`)
- Synthesis: Biological designation supplies the semantic contrast, while morphological marking extends that contrast into the grammar of names and descriptions.

#### Subchannel B. Particles, Prepositions, and Scope
- Reading type: latent/lexical
- Scene or process: Function words set relation, frequency, affirmation, and the scope of reference without naming a concrete participant.
- Active motifs: particle of reduction or recurrence `ر ب ب:B015/m01`; preposition of upper relation or obligation `ع ل و:B012/m01`; locative and relational adverb `ع ن د:B004/m02`; affirmative response particle `ن ع م:B004/m02`; unrestricted individual under negation `ء ح د:B002/m02`
- Ayah anchors: 92:20 (`ر ب ب`: `ربه`; `ع ل و`: `الأعلى`); 92:19 (`ع ن د`: `عنده`; `ن ع م`: `نعمة`; `ء ح د`: `أحد`)
- Synthesis: The particles do not supply scene objects; they organize how often, where, under what relation, and over what range a proposition applies.

#### Subchannel C. Proper Names, Mountains, Places, and Peoples
- Reading type: latent/lexical
- Scene or process: Ordinary lexical material becomes fixed as the name of a person, mountain, settlement, tribe, celestial marker, or other recognized entity.
- Active motifs: Mount Uhud `ء ح د:B006/m01`; names derived from beauty for places and bodies `ح س ن:B004/m01`; named places, persons, and stars from day or river language `ن ه ر:B007/m01`; Mount Radwa and women's names `ر ض و:B007/m01`, `ر ض ي:B003/m01`; Layla and a wine epithet `ل ي ل:B004/m01`; Yusr or Yasar as place and person `ي س ر:B010/m01`; named jinn-tribe or place `ع س ر:B012/m01`; tribal designation "the two females" `ء ن ث:B008/m01`
- Ayah anchors: 92:19 (`ء ح د`: `أحد`); 92:6 and 92:9 (`ح س ن`: `الحسنى`); 92:2 (`ن ه ر`: `النهار`); 92:21 (`ر ض و`: `يرضى`); 92:1 (`ل ي ل`: `الليل`); 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:10 (`ع س ر`: `العسرى`); 92:3 (`ء ن ث`: `الأنثى`)
- Synthesis: Descriptive words lose some compositional force when conventionalized as names, yet their source images continue to resonate with the named person, place, or group.

#### Subchannel D. Metonymic Title and Analogical Naming
- Reading type: latent/lexical
- Scene or process: A salient feature supplies a title for a person, object, group, or place, allowing shape, position, or reputation to stand for the whole.
- Active motifs: public figure named by manifest fame `ج ل و:B006/m01`; dignitary called the face of a people `و ج ه:B006/m02`; young man designated Yasar `ي س ر:B011/m01`
- Ayah anchors: 92:2 (`ج ل و`: `تجلى`); 92:20 (`و ج ه`: `وجه`); 92:7 and 92:10 (`ي س ر`: `نيسره`)
- Synthesis: A conspicuous property is promoted into a label, so public visibility, bodily front, or youth becomes a compact act of social classification.

### 18. Acceptance, Favor, and Social Bond
- Semantic invariant: Persons move from displeasure or need into accepted, beneficial, and mutually sustaining relations.
- Surface relation: direct; 92:19 denies repayment for a prior favor and 92:20-21 joins seeking the Lord's face with eventual satisfaction.
- Surprising reach: Acceptance includes placating an offended party, reciprocal consent, eye-delight, gift exchange, luxury, and the bestowal of either good or harm.

#### Subchannel A. Contentment and Abundant Satisfaction
- Reading type: surface-primary
- Scene or process: Aversion ceases, an outcome is accepted, and satisfaction may expand into an abundant settled state.
- Active motifs: acceptance opposed to displeasure `ر ض و:B001/m01`, `ر ض ي:B001/m01`; abundant or sought satisfaction `ر ض و:B002/m01`; favorable settled condition `ن ع م:B001/m03`
- Ayah anchors: 92:21 (`ر ض و`: `يرضى`); 92:19 (`ن ع م`: `نعمة`)
- Synthesis: Acceptance removes resistance, favor makes the state positively good, and abundant satisfaction describes its stable culmination.

#### Subchannel B. Mutual Consent, Placation, and Reconciliation
- Reading type: latent/lexical
- Scene or process: Two parties display consent, or one works to remove the other's anger until a shared settlement becomes possible.
- Active motifs: reciprocal consent `ر ض و:B003/m01`; effort to placate another `ر ض و:B004/m01`; negotiated acceptance `ر ض ي:B001/m02`; pliant yielding `ع ط و:B006/m03`; restored alliance `و ل ي:B004/m02`
- Ayah anchors: 92:21 (`ر ض و`: `يرضى`); 92:5 (`ع ط و`: `أعطى`); 92:16 (`و ل ي`: `تولى`)
- Synthesis: Placation addresses displeasure, mutual consent confirms that it has ended, and renewed alliance gives the agreement a durable social form.

#### Subchannel C. Favor, Blessing, and Eye-Delight
- Reading type: mixed
- Scene or process: A benefactor confers good that improves another's condition and is received as blessing, relief, or delight.
- Active motifs: beneficent favor and good condition `ن ع م:B001/m04`; blessing and delight to the eye `ن ع م:B013/m01`; gracious act beyond strict justice `ح س ن:B002/m03`; need answered by favor `ر ب ب:B016/m01`; blessing or prayer for another `ص ل ي:B002/m02`; good or harm assigned to a recipient `و ل ي:B013/m01`
- Ayah anchors: 92:19 (`ن ع م`: `نعمة`); 92:6 and 92:9 (`ح س ن`: `الحسنى`); 92:20 (`ر ب ب`: `ربه`); 92:15 (`ص ل ي`: `يصلاها`); 92:16 (`و ل ي`: `تولى`)
- Synthesis: Need opens the relation, bestowal changes the recipient's condition, and blessing or eye-delight voices the experienced value of the gift.

#### Subchannel D. Friendship, Gift Exchange, and Alliance
- Reading type: latent/lexical
- Scene or process: Sincere attachment is enacted through mutual gifts, aid, covenant, and repeated acts of loyalty.
- Active motifs: sincere friendship `ص د ق:B005/m03`; loving aid and alliance `و ل ي:B004/m03`; gift sent to a beloved recipient `ه د ي:B004/m01`; covenant joining allies `ر ب ب:B011/m02`; personal gift and handover `ع ط و:B002/m03`
- Ayah anchors: 92:6 (`ص د ق`: `صدق`); 92:16 (`و ل ي`: `تولى`); 92:12 (`ه د ي`: `الهدى`); 92:20 (`ر ب ب`: `ربه`); 92:5 (`ع ط و`: `أعطى`)
- Synthesis: Affection motivates giving, exchange makes attachment reciprocal, and alliance or covenant stabilizes friendship beyond a single generous act.

#### Subchannel E. Ease, Luxury, and Comfortable Sufficiency
- Reading type: latent/lexical
- Scene or process: Adequate provision softens bodily and social life until need recedes and residence becomes pleasant.
- Active motifs: softness and luxurious living `ن ع م:B002/m02`; material self-sufficiency `غ ن ي:B001/m04`; pleasant fit with a place `ن ع م:B011/m02`; satisfied acceptance `ر ض و:B001/m02`
- Ayah anchors: 92:19 (`ن ع م`: `نعمة`); 92:8 and 92:11 (`غ ن ي`: `استغنى`, `يغني`); 92:21 (`ر ض و`: `يرضى`)
- Synthesis: Provision removes need, softness expresses the bodily result, and contentment confirms that the condition and dwelling are experienced as enough.

### 19. Worship, Offering, and Sacred Movement
- Semantic invariant: Devotion is embodied through oriented prayer, movement toward a sacred destination, and transfer of an offering into consecrated use.
- Surface relation: indirect; 92:12 names guidance, 92:15 names entry into fire through a root also carrying prayer, and 92:18-20 joins giving, purification, purpose, face, and lordship.
- Surprising reach: The devotional scene includes synagogue or church, prayer posture, ritual direction, sacrificial livestock, gambling lots repurposed as a division mechanism, and the pilgrim's traveled approach.

#### Subchannel A. Prayer, Worship Place, and Sacred Direction
- Reading type: latent/lexical
- Scene or process: Worshippers orient themselves toward a designated direction and perform the standing, bowing, and prostration of obligatory prayer in a sacred place.
- Active motifs: prescribed prayer practice `ص ل ي:B001/m01`; designated places of worship `ص ل ي:B008/m01`; sacred direction and ritual course `ه د ي:B002/m02`; face turned toward a destination `و ج ه:B002/m03`
- Ayah anchors: 92:15 (`ص ل ي`: `يصلاها`); 92:12 (`ه د ي`: `الهدى`); 92:20 (`و ج ه`: `وجه`)
- Synthesis: Direction organizes the body, the worship place organizes the assembly, and prayer turns both into a repeated devotional act.

#### Subchannel B. Consecrated Offering and Sacrificial Division
- Reading type: latent/lexical
- Scene or process: Livestock or property is led toward a sanctuary as an offering, slaughtered or transferred, and divided among designated participants.
- Active motifs: offering led to the sanctuary `ه د ي:B005/m01`; livestock supplied for sacrifice `ن ع م:B005/m03`; lot-arrows dividing a carcass `ي س ر:B007/m02`; vessel holding the lots `ر ب ب:B010/m02`; gift transferred in devotion `ع ط و:B002/m04`
- Ayah anchors: 92:12 (`ه د ي`: `الهدى`); 92:19 (`ن ع م`: `نعمة`); 92:7 and 92:10 (`ي س ر`: `نيسره`); 92:20 (`ر ب ب`: `ربه`); 92:5 (`ع ط و`: `أعطى`)
- Synthesis: Guidance brings the animal to sacred space, transfer changes its status into an offering, and division distributes the consecrated material.

#### Subchannel C. Pilgrimage Route and Purposeful Approach
- Reading type: mixed
- Scene or process: A traveler intends a sacred destination, follows a recognized public route, and performs purposeful movement within the pilgrimage.
- Active motifs: directed walking and ritual course `س ع ي:B001/m04`; gentle guidance to the route `ه د ي:B001/m02`; traveled road and meeting of routes `ء ت ي:B010/m01`; destination-oriented face `و ج ه:B002/m04`; offering accompanying the approach `ه د ي:B005/m02`
- Ayah anchors: 92:4 (`س ع ي`: `سعيكم`); 92:12 (`ه د ي`: `الهدى`); 92:18 (`ء ت ي`: `يؤتي`); 92:20 (`و ج ه`: `وجه`)
- Synthesis: Intention gives the movement devotional purpose, the public road makes approach possible, and guidance and offering bind travel to the sacred destination.

## Standalone Subchannels

### S1. Ostrich, Speed, and Analogical Form
- Reading type: latent/lexical
- Scene or process: The ostrich is recognized as a concrete bird, while its height, speed, leg shape, track, or distant silhouette supplies names for otherwise unrelated objects and places.
- Active motifs: ostrich as bird `ن ع م:B006/m01`; collective departure figured through the ostrich `ن ع م:B008/m02`; objects named ostrich by shape or speed `ن ع م:B007/m02`
- Ayah anchors: 92:19 (`ن ع م`: `نعمة`)
- Synthesis: A single vivid animal image radiates analogically: bodily shape, rapid travel, and visual outline motivate names for a well-beam, mountain canopy, foot-part, road, and celestial station.

### S2. Inauspicious Day, Omen-Bird, and Foreboding
- Reading type: latent/lexical
- Scene or process: A difficult day is interpreted as ominous, with a named bird acting as a concrete sign through which foreboding is read.
- Active motifs: inauspicious difficult day `ع س ر:B010/m01`; shrike named as an omen-bearing bird `و ق ي:B005/m01`; anxious expectation of harm `ن ذ ر:B001/m03`
- Ayah anchors: 92:10 (`ع س ر`: `العسرى`); 92:5 and 92:17 (`و ق ي`: `اتقى`, `الأتقى`); 92:14 (`ن ذ ر`: `أنذرتكم`)
- Synthesis: Hardness colors the day as adverse, the bird gives apprehension a visible sign, and warning translates foreboding into caution.

### S3. Stealthy Incursion and Sudden Taking
- Reading type: latent/lexical
- Scene or process: A taker approaches without open confrontation, makes a swift lateral incursion, and seizes an object before resistance can form.
- Active motifs: stealth or snatching action `ن ه ر:B006/m01`; hand seizure or taking `ع ط و:B001/m05`; quick purposeful approach `س ع ي:B001/m05`; sideward deviation from the expected line `ع ن د:B002/m01`
- Ayah anchors: 92:2 (`ن ه ر`: `النهار`); 92:5 (`ع ط و`: `أعطى`); 92:4 (`س ع ي`: `سعيكم`); 92:19 (`ع ن د`: `عنده`)
- Synthesis: Deviation conceals the approach, sudden motion reduces the interval for response, and taking completes the incursion as possession.


===== _commentary/v16/work/s092/surah.r2.hftbundle/hft.md =====
# HFT: earlier activation hypotheses, per focus ayah of surah 92

Note: HFT used an older root map; a trace step on a root the gateway now withholds is an echo, not identity.

# Focus 92:1

## covering field
- reading: An oath by night precisely in its active phase of laying a veil over an unstated and therefore potentially total field.
- mechanism: Night is not merely a clock interval or a lack of daylight. It acts as a spreading layer over an unspecified field, so the verse foregrounds an operation of concealment whose reach remains deliberately open.
- trace:
  - 92:1 **وَٱلَّيْلِ** ل ي ل B001: Night supplies the dark temporal field and functions as the agentive setting of the clause.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A veil laid over something supplies the concrete operation by which night changes the field.

## arriving visitor
- reading: Night is caught arriving upon the world, its covering understood as an advancing visitation.
- mechanism: The clause can be felt kinetically: night enters and comes upon its destination like a visitor. Covering is then an arrival that progressively occupies a place, not an instantaneous switch from light to dark.
- trace:
  - 92:1 **وَٱلَّيْلِ** ل ي ل B002: Entering or undertaking something by night gives the noun a threshold-crossing, processual force.
  - 92:1 **يَغْشَىٰ** غ ش و B003: Coming upon or visiting supplies the motion by which the night reaches and occupies its unstated object.

## perceptual saturation
- reading: Night can overtake both objects and observer, temporarily covering the very faculty by which distinctions are made.
- mechanism: As the night covers, it can saturate the perceiver as well as the scene. The omitted object allows a double reach: the visible world is veiled and the observer's capacity to discriminate within it is reduced.
- trace:
  - 92:1 **وَٱلَّيْلِ** ل ي ل B001: Night's intensified darkness supplies the environmental pressure that can exceed mere background dimness.
  - 92:1 **يَغْشَىٰ** غ ش و B002: An enveloping event that takes people over expands the cover from local veil to total saturation.
  - 92:1 **يَغْشَىٰ** غ ش و B007: The non-dominant mapped branch in which understanding is overcome makes perceptual loss a live secondary effect.

## intimate enclosure
- reading: Covering also carries a contained, exploratory resonance of intimate joining under the privacy of night.
- mechanism: At the branch edge, covering can signify intimate joining rather than simple occlusion. The objectless verb leaves this as a latent bodily resonance: night gathers two sides into a shared enclosure.
- trace:
  - 92:1 **وَٱلَّيْلِ** ل ي ل B001: Night supplies the enclosing darkness within which ordinary separations of visibility are suspended.
  - 92:1 **يَغْشَىٰ** غ ش و B004: The intimate coming-over branch changes covering from hiding one thing to joining bodies within one enclosure.

## counterphase disclosure
- reading: Night is the covering phase of a reversible cycle whose paired operation is active disclosure and surface clarification.
- mechanism: The matched next oath turns night-covering into one half of a reversible surface process: night overlays and day opens, reveals, and can even be heard as polishing the same field into visibility.
- trace:
  - 92:1 **يَغْشَىٰ** غ ش و B001: The focus verb supplies the veiling operation that needs a counter-operation.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: Daylight opening out supplies the temporal counterphase to the night veil.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Disclosure and appearance provide the inverse surface operation: what was covered becomes manifest.
  - 92:2 **تَجَلَّىٰ** ج ل و B002: Polishing sharpens disclosure into an active clearing of the surface rather than passive daylight.

## generated complement
- reading: At an exploratory register, night's covering can also shelter differentiated joining and the hidden precondition of emergence.
- mechanism: The immediately following created pair gives the intimate branch of covering a generative rather than merely erotic direction. Night's enclosure can be carried as a joining of differentiated counterparts from which formed life becomes thinkable.
- trace:
  - 92:1 **يَغْشَىٰ** غ ش و B004: The intimate coming-over branch supplies the bodily joining that the next created pair can redirect toward generation.
  - 92:3 **خَلَقَ** خ ل ق B002: Creative bringing-into-being supplies an emergent outcome for the otherwise private enclosure.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: The male counterpart supplies one differentiated side of the created pairing.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The female counterpart completes the differentiated pair and keeps joining from collapsing into sameness.

## hidden divergence
- reading: Night supplies one visible cover over many hidden and increasingly divergent courses of action.
- mechanism: The cover spreads across one scene, yet the striving beneath it moves toward different objects and separates. Uniform darkness is therefore not uniformity of action; it is the common surface under which trajectories diverge.
- trace:
  - 92:1 **يَغْشَىٰ** غ ش و B001: A common veil supplies the apparently uniform surface over the scene.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement toward an object supplies distinct trajectories continuing beneath the cover.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion supplies the result: covered actors are not merged but move apart.

## path dependent cover
- reading: The shared cover becomes path-dependent: it can be traversed as opening protection or tightened into deceptive, crooked enclosure.
- mechanism: The paired conduct sequences turn the covered field into a path-dependent medium. Giving, self-protection, and enacted verification align movement with opening and ease; withholding, denial, and crooked difficulty make the same hidden interval constrictive.
- trace:
  - 92:1 **يَغْشَىٰ** غ ش و B001: The veil supplies the common medium whose practical effect can differ by the actor's course.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Passing something into another's hand supplies outward flow rather than enclosure around the self.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing oneself within protection distinguishes a sheltering boundary from a blinding cover.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Making a promise real in action supplies alignment between an unseen commitment and a visible course.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening and ease after constriction supply the first trajectory's widening passage.
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding supplies the opposing motion of closing resources around the self.
  - 92:9 **وَكَذَّبَ** ك ذ ب B009: A garment whose appearance misstates its condition makes denial function as a deceptive surface-cover.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Crookedness and obstruction supply the constricted trajectory produced on the opposing side.

## failed material cover
- reading: Night's veil raises a sharper distinction: concealment may look like safety, but an accumulated material cover cannot arrest a fall.
- mechanism: Wealth and claimed self-sufficiency resemble a portable cover, but the fall tests that cover and finds it unable to suffice. The focus veil is thereby split into genuine shelter and mere possession-based camouflage.
- trace:
  - 92:1 **يَغْشَىٰ** غ ش و B001: The covering veil supplies the protective appearance against which material sufficiency is tested.
  - 92:11 **يُغْنِى** غ ن ي B002: Sufficiency supplies the precise function that possessions fail to perform at the decisive moment.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated property supplies the attempted material layer of security.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: A fall into ruin supplies the event that pierces the attempted cover and reveals its insufficiency.

## guided bounded interval
- reading: Night is a bounded hidden passage in which direction can be supplied subtly before the destination becomes visible.
- mechanism: Guidance supplies a subtle direction inside reduced visibility, while the first and the last bound the interval. Night's cover is thus neither directionless nor terminal: it is a traversable span held between origin and outcome.
- trace:
  - 92:1 **وَٱلَّيْلِ** ل ي ل B003: The night nearest the day supplies a bounded temporal interval rather than endless darkness.
  - 92:1 **يَغْشَىٰ** غ ش و B001: The veil supplies reduced visibility within the interval.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward a road supplies orientation that does not depend on full visual exposure.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B002: Deferral to a later time supplies the far boundary and preserves delayed outcome.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Return to an eventual issue links beginning with outcome and prevents the covered interval from becoming a dead end.

## counterlight warning
- reading: Night becomes a contrast field where a hostile light can disclose consequence more violently than ordinary day.
- mechanism: The later warning introduces fire as a counterlight inside the covered field. Darkness is not identical with safety or the absence of manifestation; flame can tear through it as an exposing, painful disclosure.
- trace:
  - 92:1 **يَغْشَىٰ** غ ش و B001: The night veil supplies the dark field in which an opposed light can become starkly visible.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: A warning that awakens caution gives the counterlight a revelatory and anticipatory function.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies literal illumination that is dangerous rather than reassuring.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure blazing flame gives the counterlight an active force capable of piercing the covered scene.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Encounter with heat turns visible flame into bodily contact rather than distant spectacle.
  - 92:15 **ٱلْأَشْقَى** ش ق و B002: Hardship and suffering supply the experiential cost of that counter-disclosure.

## chosen opacity
- reading: The natural veil becomes a model for a second, culpably chosen cover: a false surface maintained by turning away.
- mechanism: Denial and turning away convert environmental covering into chosen opacity. The unusual image of a garment that lies by its appearance makes rejection resemble wearing a misleading surface and then directing the face away from disclosure.
- trace:
  - 92:1 **يَغْشَىٰ** غ ش و B001: The literal veil supplies the external model that can be internalized as deliberate opacity.
  - 92:16 **كَذَّبَ** ك ذ ب B009: A garment that misrepresents its own condition supplies a striking image of falsity as a worn surface.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning away supplies the agent's directional act that keeps the deceptive covering in place.

## sheltering margin
- reading: Covering can also be a sheltering margin that holds danger aside while generosity permits inner clearing and growth.
- mechanism: Keeping danger to one side and placing oneself in protection revalue cover as shelter. Giving wealth then feeds purification and growth inside that protected margin, so enclosure need not blind or hoard; it can preserve a vulnerable process until it matures.
- trace:
  - 92:1 **يَغْشَىٰ** غ ش و B001: The focus veil supplies a neutral enclosing layer whose value can be revised from obscuring to sheltering.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Removal and separation to the side supply the protective spacing between person and danger.
  - 92:17 **ٱلْأَتْقَى** و ق ي B002: Putting oneself within a guard supplies intentional protective enclosure.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving supplies outward transfer, preventing the sheltering boundary from becoming possessive closure.
  - 92:18 **مَالَهُۥ** م و ل B001: Property supplies the material that crosses the boundary rather than being accumulated as a false cover.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply the living process enabled within the protected margin.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purification supplies the inner clearing that distinguishes shelter from concealment of corruption.

## unseen nontransaction
- reading: Night becomes a moral laboratory: human spectators and repayment ledgers are covered, yet an upward, non-transactional orientation remains active.
- mechanism: The negation of any nearby person's repayable favor, followed by seeking the highest Lord's face, turns night-covering into an ethics of action without a human audience. Public faces and reciprocal ledgers disappear under the veil, but direction does not: giving remains aimed beyond the covered social field.
- trace:
  - 92:1 **وَٱلَّيْلِ** ل ي ل B002: Action undertaken by night supplies the practical setting of conduct performed outside ordinary visibility.
  - 92:1 **يَغْشَىٰ** غ ش و B001: The veil removes the surrounding human field from view and makes motive harder to stage publicly.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive negation removes every human counterparty from the motive structure.
  - 92:19 **عِندَهُۥ** ع ن د B004: Nearness and presence locate the absent claim in the giver's immediate social surroundings.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: A received benefit supplies the social debt that the clause denies as the act's motive.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Reciprocal recompense supplies the ledger-like exchange explicitly excluded from the giving.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Active seeking restores directed motion after human repayment has been removed.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and orientation supply the unseen aim that persists despite social invisibility.
  - 92:20 **رَبِّهِ** ر ب ب B001: Sovereignty relocates the act's reference point beyond nearby human ownership and obligation.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Height supplies the vertical direction beyond the socially covered horizontal field.

## deferred contentment
- reading: Night is a temporary interval of withheld visibility across which a still-unseen satisfaction can remain operative.
- mechanism: The closing promise of future satisfaction gives the arriving night a nonterminal horizon. What is covered now need not be absent or lost; satisfaction can remain deferred beyond the interval of invisibility.
- trace:
  - 92:1 **وَٱلَّيْلِ** ل ي ل B003: A night defined in relation to the neighboring day supplies a temporary, bounded delay.
  - 92:1 **يَغْشَىٰ** غ ش و B003: Coming upon or visiting makes the cover an arriving phase that can also pass onward.
  - 92:21 **يَرْضَىٰ** ر ض و B002: Abundant or sought satisfaction supplies the positive state held beyond the present covered interval.

## color neutral cover
- reading: The verb profiles total surface coverage; darkness is supplied by night, while the covering operation itself is color-neutral.
- mechanism: 
- trace:
  - 92:1 **يَغْشَىٰ** غ ش و B007: Whiteness covering an entire face supplies the paradox that the verb profiles surface replacement rather than darkness alone.
  - 92:2 **تَجَلَّىٰ** ج ل و B002: Polishing the surface supplies a neighboring contrast in which visibility also changes through treatment of an exterior layer.

## hidden steep terrain
- reading: The cover makes the world into hidden steep terrain where impaired awareness, direction, and falling become one somatic problem.
- mechanism: 
- trace:
  - 92:1 **يَغْشَىٰ** غ ش و B005: Loss of awareness supplies the bodily vulnerability of moving when the field is covered.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into ruin supplies the realized danger latent in covered movement.
  - 92:12 **لَلْهُدَىٰ** ه د ي B009: The split-root image of a difficult descent supplies an unexpected terrain model against which subtle direction becomes urgent.

## prayer fire hinge
- reading: At the branch edge, night is a morally unassigned enclosure in which orientation can diverge radically, from disciplined worship to consuming heat.
- mechanism: 
- trace:
  - 92:1 **وَٱلَّيْلِ** ل ي ل B002: Doing or entering an affair by night supplies the hidden temporal container for the branch bifurcation.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B001: Obligatory worship supplies one possible form of sustained orientation within a covered interval.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Encountering fire and its heat supplies the sharply opposed bodily orientation carried by the same root inventory.


# Focus 92:2

## opening disclosure
- reading: The verse presents daybreak as an active threshold in which a field of visibility opens and the day comes forth within its own opening.
- mechanism: A bounded interval opens in light while what was hidden becomes perceptible; the day is both the arriving field of visibility and the participant that comes forth within it.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: The daylight-opening branch supplies the expanding lit interval and makes it the temporal substrate of disclosure.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: The uncovering branch supplies emergence after concealment and makes the predicate an event of disclosure.

## optical polish
- reading: Day acts as a clearing operation upon perception, making other things discriminable as it manifests.
- mechanism: Daylight works like a polishing operation: obscurity is removed from the visual field until forms can be distinguished. Manifestation is thus produced clarity, not merely added brightness.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: The lit-day branch supplies illumination as the material in which visual distinctions become available.
  - 92:2 **تَجَلَّىٰ** ج ل و B002: The polishing-and-sight-clearing branch supplies removal of visual impedance and functions as the mechanism of manifestness.

## hydraulic corridor
- reading: Daylight makes its own corridor, cutting and widening a course through what had been visually closed.
- mechanism: The advance of day can be pictured as a flowing course that cuts and widens a corridor through obscurity. Visibility is spatially made by passage rather than switched on all at once.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B001: The river-course branch supplies directed flow that cuts a traversable channel and models daylight's advance.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B003: The widening-until-flow branch supplies spatial expansion and makes openness an effect of passage.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: The manifestation branch converts the imagined channel's opening into an observable disclosure.

## public display
- reading: The day presents itself in a scene of display and regard, making manifestation an encounter between appearance and gaze.
- mechanism: Manifestation has a social-visual structure: something formerly withheld is displayed, and an observer's gaze rises to meet it. Day is staged presence, not only illumination.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: The opening day branch supplies the public interval in which presentation can occur.
  - 92:2 **تَجَلَّىٰ** ج ل و B003: The ceremonial-display branch supplies a transition from withheld to presented and gives manifestation a social staging.
  - 92:2 **تَجَلَّىٰ** ج ل و B008: The searching-gaze branch supplies an implied witness and makes visibility relational rather than purely physical.

## expulsive clearance
- reading: Manifestation is a replacement event: day spreads by clearing another occupancy from the field.
- mechanism: The day becomes manifest by making room: its expansion dislodges what occupied the visual field. Disclosure is simultaneously arrival and evacuation.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B003: The opening-and-widening branch supplies the production of room in which the day can spread.
  - 92:2 **تَجَلَّىٰ** ج ل و B004: The departure-and-expulsion branch supplies displacement and makes clearance the underside of manifestation.

## cover countermotion
- reading: Day manifests by actively reversing a cover, so disclosure carries the remembered pressure of what had enclosed the field.
- mechanism: The preceding covering scene supplies the negative operation that the focus reverses. Day's manifestation now reads as a countermotion that peels back a comprehensive cover rather than as an isolated sunrise.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: The opening-day branch supplies the positive expansion that answers the prior contraction of visibility.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: The uncovering branch supplies the focus-side reversal from hiddenness to appearance.
  - 92:1 **وَٱلَّيْلِ** ل ي ل B001: The night-versus-day branch supplies the paired dark interval and makes the focus one pole of an alternation.
  - 92:1 **يَغْشَىٰ** غ ش و B001: The dominant covering branch supplies a layer placed over the field and gives disclosure something concrete to undo.
  - 92:1 **يَغْشَىٰ** غ ش و B001: The non-dominant mapped covering branch independently reinforces concealment as an operation, not merely a dark condition.

## created pairing
- reading: Day's disclosure individuates one phase of a created complementary order; opposition remains, but it is also productive pairing.
- mechanism: The created male-female pair recasts night and day as differentiated complements within an intentionally measured order. The focus event is not simply victory over night; manifestation is one phase becoming distinct within a productive pair.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: The daylight-opposed-to-night branch supplies one member of the temporal pair.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: The manifestation branch makes differentiation perceptible as one member emerges distinctly.
  - 92:3 **خَلَقَ** خ ل ق B001: The measuring-and-proportioning branch supplies ordered differentiation and functions as the pair's formative logic.
  - 92:3 **خَلَقَ** خ ل ق B002: The bringing-into-being branch supplies generativity and makes the paired order produced rather than accidental.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: The male member branch supplies one explicitly differentiated pole of the created pair.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The female member branch supplies the complementary pole and keeps difference from collapsing into solitary dominance.

## divergent trajectories
- reading: Day manifests as a differentiating field: under its openness, purposeful and drifting motions disclose how far apart they lead.
- mechanism: The disclosed day becomes a diagnostic field in which motions separate. Directed striving and the non-dominant image of aimless going coexist, while dispersion gives those motions visible distance from one another.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B003: The widening branch supplies an open field broad enough for trajectories to separate.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: The disclosure branch makes divergent motions legible rather than leaving them latent.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: The purposeful-motion branch supplies directed trajectories toward sought ends.
  - 92:4 **سَعْيَكُمْ** س ع ي B002: The non-dominant mapped branch supplies ungoverned going as a live counter-trajectory to purposeful striving.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: The dispersion branch supplies separation as the result visible in the opened field.
  - 92:4 **لَشَتَّىٰ** ش ت ت B003: The distance-between-things branch turns qualitative difference into a spatially widening gap.

## ease hardship channels
- reading: The focus's opening becomes a model of path formation: disclosure shows conduct widening into ease or curling into resistance, with each route becoming easier to continue.
- mechanism: The focus's opening and clearing becomes a two-channel process. Giving, self-protection, enacted truth, and the good align with an opening into ease; withholding, claimed self-sufficiency, denial, and crooked resistance align with a channel that becomes difficult even while one is being conducted into it.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B003: The widening-until-flow branch supplies the channel geometry through which conduct can become progressively easier or more obstructed.
  - 92:2 **تَجَلَّىٰ** ج ل و B002: The clearing branch supplies reduced impedance and functions as the perceptual analogue of facilitation.
  - 92:5 **أَعْطَىٰ** ع ط و B002: The handing-over branch supplies outward transfer and initiates the open, circulating path.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: The self-in-protection branch supplies a boundary that preserves the traveler without stopping movement.
  - 92:6 **وَصَدَّقَ** ص د ق B003: The stable-completion branch supplies structural soundness and keeps the easier channel from being mere convenience.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B001: The good-versus-ugly branch supplies the valued attractor toward which the open path is oriented.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: The opening-after-difficulty branch supplies facilitation as an unfolding process, not just a destination label.
  - 92:8 **بَخِلَ** ب خ ل B001: The withholding branch supplies arrested outward flow and begins the constricted counter-channel.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: The claimed-independence branch supplies closure to need and relation, reinforcing the blocked path.
  - 92:9 **وَكَذَّبَ** ك ذ ب B001: The truth-opposition branch supplies refusal of what disclosure makes available and turns perceptual clearing into ethical resistance.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B001: The repeated facilitation branch supplies the paradox that even movement toward hardship can be made progressively self-reinforcing.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: The crookedness-and-obstruction branch supplies the geometry of a path that resists straight passage.

## fall gradient
- reading: An opened channel also reveals gradient: motion can be smoothly conducted toward a fall that stored wealth cannot dam.
- mechanism: The hydraulic corridor acquires a terminal gradient. Accumulated means cannot make the traveler self-sufficient when the channel tips toward a fall; manifestation exposes not only a route but where its slope carries what enters it.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B001: The flowing river-course branch supplies directed movement whose endpoint depends on gradient.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: The disclosure branch makes the otherwise hidden direction and destination of the flow visible.
  - 92:11 **يُغْنِى** غ ن ي B002: The sufficiency branch supplies the expected protective capacity that the sentence explicitly negates.
  - 92:11 **مَالُهُۥٓ** م و ل B001: The wealth-accumulation branch supplies stored means that prove unable to arrest the movement.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: The falling-to-destruction branch supplies the channel's downward terminus and turns flow into descent.

## oriented time
- reading: Day manifests as an oriented temporal arc whose phases disclose direction from beginning toward outcome, while clarity still requires discernment.
- mechanism: Guidance and the first-last span turn the manifested day into oriented time. Its opening has a beginning, a direction, and an outcome; yet the non-dominant guidance branch keeps open the epistemic risk that an apparent direction can be mentally projected.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: The dawn-to-sunset interval branch supplies a finite temporal span capable of bearing direction.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: The disclosure branch makes direction and outcome readable within the temporal span.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: The gentle-direction branch supplies a route toward truth and functions as the positive orientation of disclosed time.
  - 92:12 **لَلْهُدَىٰ** ه د ي B011: The non-dominant mapped branch supplies imagined projection and preserves uncertainty about whether every seeming clarity is genuine guidance.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: The later-after-earlier branch supplies a terminal pole for the oriented interval.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: The beginning-and-precedence branch supplies the initial pole from which the interval unfolds.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: The return-to-outcome branch folds beginning toward consequence and makes temporal disclosure teleological.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: The non-dominant succession branch supplies phase following phase and makes the day a sequence rather than a frozen state.

## searing disclosure
- reading: The manifest day also prefigures severe exposure: light can warn, strip shelter, and become painful to meet.
- mechanism: The later fire sequence prevents brightness from being treated as automatically gentle. Light can disclose by heat, warning, and exposure; the same perceptual opening that clarifies may become unbearable to the one who meets it.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: The daylight branch supplies brightness as the shared material capable of being either clarifying or severe.
  - 92:2 **تَجَلَّىٰ** ج ل و B007: The clear-day branch supplies whitened openness and links manifestation directly to an exposed sky.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: The fear-awakening warning branch supplies a communicative function for severe disclosure.
  - 92:14 **نَارًا** ن و ر B001: The illumination branch supplies continuity between daylight visibility and fiery visibility.
  - 92:14 **نَارًا** ن و ر B002: The kindled-fire branch changes the shared light from a neutral medium into an active source of heat.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: The pure-blazing-flame branch intensifies exposure into contact with concentrated heat.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: The dominant fire-contact branch supplies the receiver's bodily encounter with disclosed heat.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B001: The non-dominant mapped fire-contact branch independently reinforces encounter rather than distant observation.
  - 92:15 **ٱلْأَشْقَى** ش ق و B002: The severity-and-suffering branch supplies the affective cost of a disclosure that cannot be comfortably received.

## relational gaze
- reading: Manifestation opens an encounter: turning away from disclosed reality and being protectively turned aside are visibly different orientations.
- mechanism: The focus's implied gaze becomes an encounter with possible orientations. One can face what manifests, turn the face away, or be conducted to the side and protected from a harmful exposure.
- trace:
  - 92:2 **تَجَلَّىٰ** ج ل و B008: The searching-gaze branch supplies the perceiver whose orientation becomes ethically consequential.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: The disclosure branch supplies the presented reality toward or away from which the gaze can turn.
  - 92:16 **كَذَّبَ** ك ذ ب B002: The imputing-falsehood branch supplies an active rejection of what the disclosure presents.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B006: The face-turning-toward branch supplies the positive orientation latent inside the same relational root.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: The turning-away branch supplies refusal as a spatial reversal of the gaze.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: The distancing-to-the-side branch supplies protective separation from the harmful field.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B005: The leading-to-the-side branch supplies an external agentive redirection rather than mere self-withdrawal.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: The harm-deflecting branch supplies the purpose of being moved aside and distinguishes protection from denial.

## circulating growth
- reading: Its river becomes a model of giving: what is released moves through a widened channel and returns as visible purification and growth.
- mechanism: The focus's river-channel image is activated by giving, a branch that explicitly channels water, and growth. Wealth ceases to be a static possession and becomes a current whose outward passage opens space for purification and increase.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B001: The river-course branch supplies abundant outward flow as the material model for transferred wealth.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B003: The widening-through-flow branch supplies the paradox that release enlarges the channel rather than depleting it.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: The manifestation branch makes the internal effect of circulation visible as a changed state.
  - 92:18 **يُؤْتِى** ء ت ي B002: The giving branch supplies the explicit outward transfer that starts circulation.
  - 92:18 **يُؤْتِى** ء ت ي B004: The water-channeling branch supplies a concrete conduit and directly activates the focus's river-course potential.
  - 92:18 **يُؤْتِى** ء ت ي B005: The incoming flood branch supplies movement across social boundaries and keeps the current from being privately enclosed.
  - 92:18 **مَالَهُۥ** م و ل B001: The accumulated-wealth branch supplies what is released into the channel.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: The growth-and-increase branch supplies the generative result of circulation.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: The purification branch supplies inward clearing as the simultaneous result of outward transfer.

## maturation to acceptance
- reading: Day models maturation: a hidden capacity is grown, refined, brought to readiness, and finally received in a settled state.
- mechanism: Manifestation stretches from an instant into maturation. Growth advances toward ripeness, nurture carries it toward completion, and acceptance names the condition reached; the day is the interval in which a latent state becomes ready to appear.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: The full daylight interval supplies duration for a state to develop rather than flash into existence.
  - 92:2 **تَجَلَّىٰ** ج ل و B002: The repeated polishing branch supplies incremental refinement that culminates in clarity.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: The growth branch supplies development from a smaller latent state toward visible increase.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B002: The non-dominant mapped ripeness-for-cutting branch supplies a threshold at which developed potential becomes ready for disclosure.
  - 92:20 **رَبِّهِ** ر ب ب B002: The nurture-repair-completion branch supplies the sustained agency carrying development toward wholeness.
  - 92:20 **رَبِّهِ** ر ب ب B005: The non-dominant mapped nourishment-and-growth branch reinforces maturation as a living process rather than an abstract sequence.
  - 92:21 **يَرْضَىٰ** ر ض و B001: The satisfaction-over-agitation branch supplies the settled terminal state of the developmental process.
  - 92:21 **يَرْضَىٰ** ر ض و B001: The non-dominant mapped acceptance branch independently supplies reception of what has reached manifest readiness.

## nonreciprocal orientation
- reading: The day becomes an image of motive made public: action is disclosed by the direction it faces once human repayment is removed.
- mechanism: The public-display baseline is stripped of a human exchange audience and redirected. What becomes visible is action facing beyond reciprocal favor toward a highest direction; manifestation is exposure of orientation, completed not by repayment but by acceptance.
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: The opened day supplies the public field in which orientation and motive can become visible.
  - 92:2 **تَجَلَّىٰ** ج ل و B008: The searching-gaze branch supplies directed attention and allows manifestation to be read as an orientation test.
  - 92:19 **لِأَحَدٍ** ء ح د B002: The exhaustive-negation branch removes every human counterparty from the motive structure.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: The favor-and-good-condition branch supplies the social benefit that might otherwise demand return.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: The act-for-recompense branch supplies the reciprocal economy that the clause excludes.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: The seeking branch supplies intentional direction after reciprocal motive has been removed.
  - 92:20 **وَجْهِ** و ج ه B002: The direction-and-destination branch supplies the vector toward which disclosed action faces.
  - 92:20 **وَجْهِ** و ج ه B007: The front-of-day branch loops the directional image directly back into the focus's daytime field.
  - 92:20 **رَبِّهِ** ر ب ب B001: The lordship branch supplies the non-human authority before whom motive is exposed.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: The elevation branch supplies vertical priority and redirects the gaze beyond horizontal exchange.
  - 92:21 **يَرْضَىٰ** ر ض و B001: The satisfaction branch supplies acceptance as the endpoint replacing human repayment.

## daylight rebuke
- reading: Daylight behaves like a public rebuke: its manifestness checks denial by making evasion conspicuous.
- mechanism: 
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B004: The harsh-rebuke branch supplies forceful checking and makes daylight's arrival socially confrontive.
  - 92:2 **تَجَلَّىٰ** ج ل و B006: The open-notoriety branch supplies public undeniability and turns rebuke into exposure.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: The warning-that-awakens-caution branch supplies the rebuke's intended alerting function.
  - 92:16 **كَذَّبَ** ك ذ ب B002: The imputing-falsehood branch supplies the denial that public manifestness confronts.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: The turning-away branch supplies the evasive response against which the rebuking exposure presses.

## hatching display
- reading: Daybreak can be carried as a natal image: a nurtured living interval breaks concealment and is presented to view.
- mechanism: 
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B005: The bird-chick branch supplies a newly emerged living form and makes daybreak analogous to hatching.
  - 92:2 **تَجَلَّىٰ** ج ل و B003: The ceremonial-presentation branch supplies movement from protected concealment into witnessed presence.
  - 92:3 **خَلَقَ** خ ل ق B002: The bringing-into-being branch supplies the generative transition behind emergence.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B004: The fertile-ground branch supplies an ecological matrix in which emergence can be nurtured.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: The growth branch supplies development preceding the moment of visible emergence.
  - 92:20 **رَبِّهِ** ر ب ب B002: The nurture-to-completion branch supplies sustained care carrying the latent form toward display.

## visibility snatch
- reading: At the threshold of manifestation, day seems to snatch the visible field out from under night's cover.
- mechanism: 
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B006: The sudden-snatch branch supplies abrupt acquisition and makes the transition feel seized rather than gradual.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: The uncovering branch constrains the object of the imagined snatch to visibility itself.
  - 92:1 **يَغْشَىٰ** غ ش و B001: The prior cover branch supplies the enclosure from which visibility is suddenly recovered.

## tempered edge
- reading: Daylight can be imagined as a tempered, polished edge that cuts open the field and sharply separates what had blended together.
- mechanism: 
- trace:
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B003: The cut-and-widen branch supplies an incision-like opening through which visibility spreads.
  - 92:2 **تَجَلَّىٰ** ج ل و B002: The blade-polishing branch supplies a sharpened reflective edge and makes disclosure an act of discrimination.
  - 92:14 **نَارًا** ن و ر B002: The kindled-fire branch supplies heat as the material condition for tempering the imagined edge.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B004: The fire-straightening branch supplies shaping by heat and turns brightness into a refining operation.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: The non-dominant cutting branch supplies the decisive separation made possible by the polished edge.


# Focus 92:3

## agent event ambiguity
- reading: The wording can hold the Originator and the proportioned event of originating together without forcing an early choice between them.
- mechanism: The originating branch of خلق supports an agentive hearing, while its measuring branch supports a processive hearing. The oath can therefore bear witness by the Originator, by the measured creative event, or by a deliberate resonance between them.
- trace:
  - 92:3 **خَلَقَ** خ ل ق B002: Originating and bringing into being supplies the live agentive pole of the construction.
  - 92:3 **خَلَقَ** خ ل ق B001: Measuring and proportioning before execution supplies the eventive pole, creation as an enacted process.

## cooriginated pair
- reading: Their opposition is itself a jointly originated relation: differentiated, co-dependent, and equally derivative from one act.
- mechanism: Both opposed sex terms are coordinated under one originating act. Their difference is real, but neither pole is self-grounding or prior: the pair is co-originated as a relation.
- trace:
  - 92:3 **خَلَقَ** خ ل ق B002: Bringing into being makes one creative act the common source of both terms.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: Male in explicit opposition to female supplies one pole of the created relation.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: Female in explicit opposition to male supplies the other pole under the same governing act.

## measured embodiment
- reading: Creation measures, differentiates, and completes embodied forms; the pair displays a formative operation.
- mechanism: The measuring-before-action and completed-form branches turn creation from a bare existential verb into proportioning that arrives at perceptible form. Sexed difference is heard as formed embodiment rather than only a verbal classification.
- trace:
  - 92:3 **خَلَقَ** خ ل ق B001: Prior measuring and apportioning supplies the formative operation.
  - 92:3 **خَلَقَ** خ ل ق B003: Complete, balanced, visible form supplies the embodied result of that operation.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: The male term makes the measured distinction bodily and concrete.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The female term completes the visibly differentiated embodiment.

## trait polarity
- reading: The pair also activates a non-ranked material field of force, yielding, and fertility that creation apportions, while resisting a literal stereotype about persons.
- mechanism: Hardness, sharp force, softness, yielding, and fertility form a cross-material polarity around the explicit pair. Carried cautiously, the line can image creation apportioning different capacities without ranking them or claiming that every person embodies a fixed sex-coded trait.
- trace:
  - 92:3 **خَلَقَ** خ ل ق B001: Apportioning supplies the distribution of contrasting capacities.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B002: Hard, sharp, forceful materiality supplies one lexical extension of the male pole.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B002: Softness and yielding supply a contrasting lexical extension of the female pole.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B004: Easy fertile ground adds receptivity that produces growth, not mere weakness.

## cover reveal cycle
- reading: The pair participates in a larger grammar of created difference: poles emerge within one order and need not be read as isolated or antagonistic substances.
- mechanism: Night covers; day opens into light and becomes manifest. Placed after these enacted opposites, the male-female pair is no longer only a static taxonomy: it becomes another created differentiation whose poles belong to one ordered world of concealment, emergence, and recurrence.
- trace:
  - 92:3 **خَلَقَ** خ ل ق B001: Proportioning anchors the pair as an ordered created differentiation.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: Male opposed to female supplies one jointly created pole.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: Female opposed to male supplies the corresponding pole.
  - 92:1 **وَٱلَّيْلِ** ل ي ل B001: Night as darkness opposed to day supplies the first surrounding polarity.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A cover rising over and concealing something makes the first polarity an active process.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: Day opening through illumination supplies the counter-process to covering.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Uncovering and manifestation completes the movement from concealment to appearance.

## conjugal continuation
- reading: The created pair can also be heard as a generative relation by which originating continues through embodied life.
- mechanism: The covering root carries a branch for conjugal intercourse, while manifestation carries a bridal-unveiling branch. Together they activate the possibility that male and female are not only finished products of creation but a relation through which created life continues.
- trace:
  - 92:3 **خَلَقَ** خ ل ق B002: Originating life anchors the proposed movement from created pair to continuing generation.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: The explicit male term supplies one participant in the generative relation.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The explicit female term supplies the other participant in the generative relation.
  - 92:1 **يَغْشَىٰ** غ ش و B004: Conjugal covering supplies the relational and reproductive bridge into the focus pair.
  - 92:2 **تَجَلَّىٰ** ج ل و B003: Bridal unveiling supplies a complementary social image of pair formation.

## trait polarity decoupled
- reading: Sexed embodiment is created, but moral difference is pursued: either member of the pair can give, guard, verify, withhold, or deny.
- mechanism: The focus inventories tempt a hard-male/soft-female extension, but the next units locate consequential difference in diverse striving and opposed actions: giving or withholding, guarding or self-exempting, making truth effective or denying it. The context redistributes firmness and yielding across ethical acts and prevents bodily difference from becoming moral destiny.
- trace:
  - 92:3 **خَلَقَ** خ ل ق B004: Inner disposition makes a character reading possible and therefore available for contextual revision.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B002: Hard and forceful masculinity supplies the polarity that could otherwise be moralized.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B002: Softness and yielding supply the contrasting polarity that the action sequence refuses to rank by sex.
  - 92:4 **سَعْيَكُمْ** س ع ي B002: Work, earning, and conduct relocate consequential difference into what people do.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion supplies the divergence of enacted trajectories after the jointly created pair.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing something over supplies a chosen outward act rather than an inherited bodily trait.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Putting oneself within protection supplies deliberate self-positioning.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Making promise and action real assigns firmness to ethical enactment rather than to sex.
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding supplies the opposed chosen contraction.
  - 92:9 **وَكَذَّبَ** ك ذ ب B001: Contradicting truth supplies the opposed epistemic and ethical act.

## aptitude feedback
- reading: Created readiness remains live and directional: conduct can be met by facilitation that makes a chosen path progressively fit.
- mechanism: The aptness branch of خلق is activated by repeated causative easing toward opposed ends. Ease opens and makes movement compliant; hardship obstructs and twists. Creation can therefore include readiness that later conduct channels and reinforces, not only a finished allocation at birth.
- trace:
  - 92:3 **خَلَقَ** خ ل ق B005: Fitness, likelihood, and preparedness supply the focus-side capacity to be made apt for a trajectory.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening and ease after difficulty supply one facilitated destination.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B005: Light, compliant movement supplies the mechanism by which a path becomes easier to inhabit.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B001: The same easing operation governing the hard destination makes facilitation morally neutral in itself.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Opposition, twisting, and induced difficulty supply the constricted trajectory.

## agentive origin strengthened
- reading: The later speaking guide, owner of both temporal bounds, and Lord-completer becomes the strongest abductive candidate for that agent, alongside the oath by creation as event.
- mechanism: Later first-person responsibility for guidance and possession of ending and beginning, followed by the Lord as sovereign and completer, supplies the otherwise unexpressed agent of خلق. This strengthens the relative-agent hearing of ما without erasing the processive oath.
- trace:
  - 92:3 **خَلَقَ** خ ل ق B002: Originating and bringing into being supplies the predicate whose agent is contextually recovered.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle direction toward path and truth supplies explicit first-person purposive agency.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: Lateness after what is first supplies one temporal bound claimed by the speaker.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Beginning and precedence supply the other temporal bound claimed by the same speaker.
  - 92:20 **رَبِّهِ** ر ب ب B001: Lordship, possession, and sovereignty identify a plausible originating agent.
  - 92:20 **رَبِّهِ** ر ب ب B002: Nurturing, repairing, and completing connect lordship to the formative work of creation.

## counterformation fire
- reading: Created form is the beginning of a vulnerable history: subsequent direction can expose it to destructive re-processing or carry it aside under protection.
- mechanism: The focus completes and balances form; the later sequence introduces falling into ruin, kindled pure flame, fire that can straighten or process material, and being moved aside under protection. Fire becomes a startling counter-formative process: created form is not merely finished but enters trajectories of deformation or preservation.
- trace:
  - 92:3 **خَلَقَ** خ ل ق B003: Complete and balanced visible form supplies the material baseline exposed to later processes.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into destruction reverses the movement toward completed form.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies the active material medium of the counter-process.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure, intensely kindled flame intensifies the material transformation.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B004: Kindling heat and straightening a thing by fire supplies the counter-formative operation.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Moving away and separating supplies preservation by removal from the transforming medium.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Repelling harm by a protection supplies the preserving counter-arrow.

## nontransactional gift
- reading: It can also be heard as the primordial non-transactional giving of differentiated life, later echoed by giving that refuses a human repayment ledger.
- mechanism: Originating both poles without any stated counterpayment is retrospectively illuminated by wealth being given for purification, with no human favor to settle, solely seeking the Lord's face. Creation can be heard as non-transactional donation, and ethical giving as participation in that originating generosity rather than repayment within a human ledger.
- trace:
  - 92:3 **خَلَقَ** خ ل ق B002: Bringing beings into existence supplies the originating act reread as prior donation.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving and handing over supplies the human echo of originating generosity.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purity and rightness make giving transformative for the giver rather than a purchase from the recipient.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matching an act with its recompense supplies the transactional mechanism that the syntax negates.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking supplies the giver's single non-human orientation.
  - 92:20 **وَجْهِ** و ج ه B004: Face as the self or essence supplies the sought end beyond social return.
  - 92:20 **رَبِّهِ** ر ب ب B001: Lordship and ownership identify the source toward whom the non-transactional act is oriented.

## measured cut
- reading: The pair can be imaged as a measured differentiation brought to its proper cut: distinction emerges through proportion, threshold, and separation.
- mechanism: 
- trace:
  - 92:3 **خَلَقَ** خ ل ق B001: Measuring and proportioning before cutting supplies the focus-side design operation.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: Male opposed to female supplies one result of the differentiation.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: Female opposed to male supplies the other result of the differentiation.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Cutting a thing supplies the latent execution of the prior measure.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B002: Ripeness and the time for cutting add a temporal threshold to differentiation.

## birth passage
- reading: Creation can flicker as risky passage into sexed life, negotiating closure, difficult orientation, and emergence rather than naming only a finished result.
- mechanism: 
- trace:
  - 92:3 **خَلَقَ** خ ل ق B012: An imperforate solid closure supplies the blocked passage at the focus anchor.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The explicit female term keeps the anatomical activation attached to the focus.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B006: Difficult childbirth supplies the obstructed transition from formation to emergence.
  - 92:18 **يُؤْتِى** ء ت ي B007: The coming forth of growth and offspring supplies successful emergence.
  - 92:20 **وَجْهِ** و ج ه B010: Hands-first birth supplies a concrete abnormal orientation within the passage.

## language tracks or fabricates
- reading: A contained second register asks whether naming and grammatical marking disclose created difference or fabricate a persuasive surface.
- mechanism: 
- trace:
  - 92:3 **خَلَقَ** خ ل ق B007: Fabricating speech supplies a counterfeit mode of making set against real originating.
  - 92:3 **خَلَقَ** خ ل ق B002: Actual bringing into being supplies the reality against which verbal fabrication is tested.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B004: Naming and mention on the tongue supply discursive presentation.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B005: Grammatical feminization supplies formal sex-marking within language.
  - 92:6 **وَصَدَّقَ** ص د ق B001: Truthful speech supplies correspondence between naming and what is.
  - 92:9 **وَكَذَّبَ** ك ذ ب B009: A garment that lies through its apparent condition supplies deceptive presentation by visible form.

## catchment fertility growth
- reading: The focus can momentarily image creation as an open generative ecology: containment, fertile reception, routed flow, emergence, and nurtured increase.
- mechanism: 
- trace:
  - 92:3 **خَلَقَ** خ ل ق B011: A rock hollow that receives and retains rain supplies the generative catchment.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B004: Soft fertile land whose vegetation quickly thrives supplies the receptive field.
  - 92:18 **يُؤْتِى** ء ت ي B004: A watercourse and the opening of its route connect stored water to the field.
  - 92:18 **يُؤْتِى** ء ت ي B007: The emergence of growth and offspring supplies the catchment's output.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Increase and growth supply the expanding result.
  - 92:20 **رَبِّهِ** ر ب ب B005: Nourishment and development complete the non-dominant growth chain.

## rights ledger exceeded
- reading: The pair can cast a faint rights-and-obligations ledger, while the culminating giver exceeds that ledger by acting without a human debt to collect.
- mechanism: 
- trace:
  - 92:3 **خَلَقَ** خ ل ق B001: Apportioning supplies the allocation structure from which rights and obligations could arise.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B008: A written instrument of right supplies the juridical ledger image.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The female member of the explicit pair keeps the legal afterimage relational rather than male-isolated.
  - 92:18 **مَالَهُۥ** م و ل B001: Possessing and accumulating property supplies what can enter a social ledger.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Collecting and settling a debt supplies the exact reciprocal accounting mechanism.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive negation removes every human claimant from the stated motive.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking redirects the act beyond repayment within the human ledger.


# Focus 92:4

## directed divergence
- reading: The addressees are already moving toward sought ends, but their trajectories fan apart and may finish very far from one another.
- mechanism: Each striving is a vector toward something sought, while the collective field fans into separated courses and endpoints. Diversity therefore concerns direction and destination, not merely a list of unlike activities.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful going supplies the directed motion that makes each striving a vector rather than static effort.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Scattering separates the plural vectors into distinct courses.
  - 92:4 **لَشَتَّىٰ** ش ت ت B003: Distance between two things turns difference of course into potentially radical separation of ends.

## social economies
- reading: People inhabit divergent economies of effort: earning, governing, reconciling, and giving organize communal life in materially different ways.
- mechanism: The verse can inventory rival social economies: ordinary acquisition, administration over people and resources, and generosity or peacemaking. Their separation is institutional as well as personal because each mode distributes power, wealth, and repair differently.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B002: Work, earning, and active conduct supply the economic substrate of the plural striving.
  - 92:4 **سَعْيَكُمْ** س ع ي B003: Agency or office over a group makes some striving an entrusted public function.
  - 92:4 **سَعْيَكُمْ** س ع ي B006: Noble generosity and peacemaking supply a reparative social use of effort.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Separation keeps these social deployments from collapsing into a morally neutral category of busyness.

## agency polarity
- reading: Strivings can differ at the deeper level of who owns the laboring body and whether effort releases agency or extracts it.
- mechanism: The same lexical field can hold opposite ownership structures. One laborer earns toward release from bondage; another captive body is made to earn for an owner. The verse can therefore expose not only different deeds but radically different possession of agency within work.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B005: Earning toward manumission makes striving a labor process whose sought end is recovered freedom.
  - 92:4 **سَعْيَكُمْ** س ع ي B007: The specialized coercive arrangement makes striving an imposed revenue mechanism over an enslaved woman's body.
  - 92:4 **لَشَتَّىٰ** ش ت ت B003: Far-apartness holds emancipation and extraction as opposed agency regimes rather than adjacent examples.

## aim and drift
- reading: The field ranges from deliberate pursuit to neglected drift; difference can arise from the presence or failure of orientation itself.
- mechanism: A live tension appears between directed pursuit and motion released without care. Some striving is governed by an aim; some becomes drift because its bearer or resources are left loose. Diversity may thus register different degrees of orientation, not only different chosen goals.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement supplies the strongly oriented pole of striving.
  - 92:4 **سَعْيَكُمْ** س ع ي B002: The non-dominant branch of neglect and wandering loose supplies an exploratory pole of unguided motion and wasted holdings.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Scattering describes what motion becomes when a common orientation no longer holds it together.

## constructive spacing
- reading: Some plurality may be productively spaced: distinct acts can avoid overlap and become clearer precisely because they do not merge.
- mechanism: Difference need not mean collision or ruin. As spacing prevents overlap and can produce a fine ordered row, distinct works may remain non-identical yet become mutually legible. The verse can describe a patterned plurality as well as a moral bifurcation.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B002: The broad field of work supplies the multiple units whose relation is being patterned.
  - 92:4 **لَشَتَّىٰ** ش ت ت B002: Gapped teeth supply a bodily image in which non-overlap creates ordered and potentially attractive spacing.

## visibility phase change
- reading: Strivings pass through hidden and revealed phases; disclosure can uncover divergence that was already operating under a common cover.
- mechanism: The night covers and the day opens into disclosure. Placed before the focus assertion, that alternation makes striving phase-dependent in visibility: concealed trajectories continue to operate, then disclosure separates what darkness made look alike.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement keeps the human trajectories active across both phases of visibility.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Scattering names the differences that concealment can blur and disclosure can expose.
  - 92:1 **وَٱلَّيْلِ** ل ي ل B001: Night and its darkness supply the temporal field in which distinctions are difficult to see.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A covering that rises over a thing supplies active concealment rather than mere absence of light.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: Day opening with illumination supplies the counter-phase in which the field becomes traversable and visible.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Uncovering and appearing convert daylight into disclosure of previously covered differences.

## created pairing
- reading: Difference can also be structured pairing: unlike courses may be measured, relational, and generative without becoming the same.
- mechanism: Measured creation followed by a paired contrast activates a non-chaotic account of difference. The focus predicate can mark designed differentiation in which unlike poles are relational and generative, even while their courses remain distinct.
- trace:
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Separation supplies the formal difference that the preceding created pair can organize.
  - 92:4 **لَشَتَّىٰ** ش ت ت B002: Ordered spacing keeps differentiation from being reduced to destructive fracture.
  - 92:3 **خَلَقَ** خ ل ق B001: Measuring and proportioning supply an ordering operation behind created difference.
  - 92:3 **خَلَقَ** خ ل ق B002: Bringing creation into being makes the paired distinction part of an originated structure.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: The male as one pole supplies half of an explicitly relational contrast.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The female as the other pole completes the created pair without erasing difference.

## self reinforcing routes
- reading: Divergence is dynamically produced: initial postures recruit facilitation, so each route becomes easier to continue, including an easy descent into difficulty.
- mechanism: The mirrored sequences turn divergent striving into path dependence. Giving, self-protection, and enacted verification enter one channel; withholding, claimed independence, and denial enter another. The repeated facilitation makes each selected course increasingly compliant to motion, strikingly even when the destination is hardship.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful going supplies the moving subject that can be channeled into an increasingly traversable route.
  - 92:4 **لَشَتَّىٰ** ش ت ت B003: Distance between courses supplies the widening divergence produced by repeated route selection.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing something outward supplies the first route's opening act.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing oneself within protection supplies a governing restraint rather than unbounded motion.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Making a promise true in action turns assent into a stable behavioral commitment.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B001: The good opposed to the ugly supplies the valued horizon of the first route.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B005: Lightness and compliance in motion make the selected route easier to continue.
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding closes the second route against outward transfer.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed self-sufficiency supplies the posture that treats guidance and relation as unnecessary.
  - 92:9 **وَكَذَّبَ** ك ذ ب B001: Contradicting truth supplies the second route's cognitive and verbal closure.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: The same compliance-in-motion branch makes the adverse route easy to keep traversing rather than approving its end.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Twisting, opposition, and obstruction supply a destination whose internal structure is difficulty despite easy approach.

## flow and stock economies
- reading: They instantiate rival material systems: circulation keeps value relational, while retention mistakes accumulated stock for the power to stop a fall.
- mechanism: Giving and withholding generate opposite topologies of possession. One economy releases holdings into relation; the other seals them into a stock treated as self-sufficiency. The later fall is a stress test showing that accumulated property cannot redirect a terminal trajectory.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B002: Work and earning supply the production process whose proceeds may circulate or be retained.
  - 92:4 **سَعْيَكُمْ** س ع ي B006: Generous undertaking supplies the outward, reparative deployment of what work acquires.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Transfer by giving opens the circulating economy.
  - 92:8 **بَخِلَ** ب خ ل B001: Miserly retention closes the rival economy around the holder.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B002: Sufficiency supplies the mistaken conversion of stored means into imagined independence.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Possessing and multiplying wealth supplies the stock that is tested for rescue capacity.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into destruction supplies the terminal event that stored wealth fails to arrest.

## guided temporal field
- reading: The routes diverge inside a field where direction is supplied and both origin and outcome remain encompassed; plurality does not entail absence of guidance.
- mechanism: Guidance supplies a direction within the scattered field, while possession of the later and the first spans the whole temporal extent of every course. Divergent motion is therefore neither directionless nor outside a containing order; its freedom operates inside an offered orientation and an owned horizon.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful going supplies trajectories capable of receiving or refusing direction.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Scattering supplies the plural field that guidance addresses without erasing its plurality.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward road and truth supplies an available directional signal.
  - 92:12 **لَلْهُدَىٰ** ه د ي B002: Direction, manner, and intended course turn guidance from information into an orientation for motion.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: Laterness supplies the far temporal end of the containing horizon.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Beginning and precedence supply the near temporal origin of the same horizon.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Return to outcome and final issue folds the apparent first term toward consequence, joining origin to end.

## approach avoidance reversal
- reading: A traveler can face away yet move toward the danger, while another is moved sideways to safety; divergence must be read by actual endpoint, not posture alone.
- mechanism: Warning makes a blazing endpoint visible, yet denial and turning away do not produce distance from it: the one who turns away comes into contact with its heat. Conversely, the protected person is actively led to the side. Divergence becomes an approach-avoidance geometry in which apparent orientation and actual endpoint can reverse.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful going supplies the approach trajectories whose apparent and actual directions can differ.
  - 92:4 **لَشَتَّىٰ** ش ت ت B003: Distance between two things supplies the geometry of contact with or removal from the endpoint.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: A warning that awakens caution makes the dangerous endpoint available to practical response.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies the visible terminal hazard.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure rising flame intensifies the endpoint from an abstract warning into active consuming heat.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Meeting fire and its heat supplies actual contact, not merely sight of the hazard.
  - 92:15 **ٱلْأَشْقَى** ش ق و B001: Wretchedness opposed to flourishing characterizes the traveler whose route reaches the flame.
  - 92:16 **كَذَّبَ** ك ذ ب B001: Contradiction of truth blocks the warning from correcting the route.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning the back supplies an apparent movement away that paradoxically terminates in contact.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B005: Leading something to the side supplies active lateral removal from the dangerous line.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Repelling harm by protection supplies the reason lateral displacement functions as rescue.

## giving as transformative flow
- reading: The generous path changes the very economy of striving: value flows outward, while growth and purification return as transformation of the agent.
- mechanism: Wealth is made to pass outward through giving, and the adjoining reflexive growth-purification returns the change to the giver. The economic vector is therefore metabolic rather than subtractive: released property becomes a channel through which the agent is increased and clarified.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B002: Work and earning supply the acquired value that can be redirected through action.
  - 92:4 **سَعْيَكُمْ** س ع ي B006: Noble generosity supplies the outward social purpose of the redirected earning.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving supplies the transfer that moves wealth beyond the possessor.
  - 92:18 **يُؤْتِى** ء ت ي B004: A watercourse and the clearing of its passage supply a material analogy for giving as opened flow.
  - 92:18 **مَالَهُۥ** م و ل B001: Possessed and multiplied wealth supplies the stock entering the opened channel.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase reverse the expectation that outward transfer only diminishes the giver.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purity and soundness locate the return of the flow in the agent's transformed condition.

## emancipatory vs extractive economy
- reading: The paths can instantiate opposed political economies of the body: wealth and labor may be arranged to release agency or to monetize captivity.
- mechanism: The focus lexicon already holds labor toward manumission beside coerced revenue from an enslaved woman. The context's repeated giving, protection, transfer of wealth, and purification selectively activates the emancipatory pole while leaving the extractive pole as its live structural opposite.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B005: Labor earning the price of release supplies an economy in which work moves a captive person toward freedom.
  - 92:4 **سَعْيَكُمْ** س ع ي B007: Coerced sexual earning supplies the opposed economy in which ownership extracts revenue from captivity.
  - 92:4 **لَشَتَّىٰ** ش ت ت B003: Far-apartness keeps liberation and exploitation as opposed regimes within the same labor vocabulary.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Giving activates release of possession rather than extraction from another.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B001: Protection from harm gives the outward transfer an anti-extractive orientation.
  - 92:18 **يُؤْتِى** ء ت ي B002: The later act of giving reinforces relinquishment of control over wealth.
  - 92:18 **مَالَهُۥ** م و ل B001: Owned wealth supplies the transferable asset whose deployment can either loosen or intensify domination.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purification marks release from an extractive relation as transformative rather than merely transactional.

## nonreciprocal motive
- reading: Outwardly similar giving can be far apart at the level of motive: one settles a human account, while another refuses to make generosity a repayment.
- mechanism: The exhaustive negation of any person's present favor and the denial of repayment remove the generous act from a debt ledger. Divergent striving now includes hidden motive architecture: an outwardly identical transfer may close an exchange account or break reciprocity by acting without human claim.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B002: Active conduct supplies the outward deed whose motive can vary beneath an identical form.
  - 92:4 **سَعْيَكُمْ** س ع ي B006: Noble generosity supplies the non-reciprocal candidate that the ledger language tests.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive negation removes every human creditor rather than merely one named person.
  - 92:19 **عِندَهُۥ** ع ن د B004: Presence with a person supplies the relational location where an outstanding favor would be held.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: Benefit and good condition supply the prior value that could create a reciprocal obligation.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Answering an act with its recompense supplies the exchange loop being negated.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Collecting and settling a debt sharpens the rejected model of generosity as account closure.

## delegated stewardship
- reading: Some striving may be entrusted administration: its divergence lies in whether office serves possession and extraction or repair under a higher sovereignty.
- mechanism: The focus branch of office over people combines with giving, correct orientation, sovereignty, and nurturing completion. Human striving can thus be read as delegated administration: resources and persons are not privately mastered but handled under a higher ordering whose criterion is repair.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B003: An appointed agent or officer over people supplies the institutional form of striving.
  - 92:4 **سَعْيَكُمْ** س ع ي B006: Generosity and peacemaking supply the reparative criterion for exercising office.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving supplies the administrator's outward disposition of resources.
  - 92:20 **وَجْهِ** و ج ه B008: The sound face or right aspect of an affair supplies a criterion of correct administration.
  - 92:20 **رَبِّهِ** ر ب ب B001: Sovereignty and ownership place the human office beneath a higher authority.
  - 92:20 **رَبِّهِ** ر ب ب B002: Repair, nurture, and completion define authority as cultivation rather than mere control.

## telic reintegration
- reading: Visible diversity can hide telic unity, and visible similarity can hide radical divergence: what finally separates striving is the face it seeks and the horizon in which it expects satisfaction.
- mechanism: Seeking supplies telic pressure, face supplies orientation, lordship supplies a sustaining relation, height supplies a vertical horizon, and satisfaction supplies an affective completion. Surface-diverse acts can therefore converge through one sought orientation, while surface-similar acts can remain far apart because they seek different faces.
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful going supplies action whose unity or divergence is determined by what it seeks.
  - 92:4 **لَشَتَّىٰ** ش ت ت B003: Far-apartness relocates decisive difference from visible form to ultimate orientation.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking supplies the explicit aim that organizes the preceding acts.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and orientation turn the sought face into a vector-bearing horizon.
  - 92:20 **رَبِّهِ** ر ب ب B002: Nurture, repair, and completion supply a relation capable of integrating diverse acts over time.
  - 92:20 **رَبِّهِ** ر ب ب B007: Abiding and continuance make the orientation durable rather than episodic.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Elevation supplies the vertical dimension of the sought horizon.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Satisfaction opposed to displeasure supplies affective arrival rather than material repayment.
  - 92:21 **يَرْضَىٰ** ر ض و B002: Abundant or sought satisfaction expands the terminal state beyond a momentary reward.

## motion interrupted by denial
- reading: They may also differ kinetically: one becomes smoothly self-continuing, while another advances in deceptive bursts and stalls.
- mechanism: 
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful going supplies the motion whose continuity is under examination.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Scattering permits trajectories to differ in rhythm and continuity as well as endpoint.
  - 92:9 **وَكَذَّبَ** ك ذ ب B007: The image of a wild animal running and then stopping supplies a burst-stall pattern for denial-shaped effort.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: Compliance and lightness in motion provide the contrasting possibility of a route that becomes easy to continue.

## legible spacing
- reading: A strange but live material model treats gaps as punctuation: separation can make distinct works readable and prevent them from collapsing into one another.
- mechanism: 
- trace:
  - 92:4 **لَشَتَّىٰ** ش ت ت B002: Separated teeth supply an ordered row whose gaps prevent crowding and preserve distinction.
  - 92:4 **سَعْيَكُمْ** س ع ي B002: Plural works supply the units that can be spaced into a legible pattern.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B008: Separate bodily lines and marks reinforce differentiation as inscription rather than disintegration.
  - 92:2 **تَجَلَّىٰ** ج ل و B002: Polishing and clarification supply the inferential effect of spacing: distinct marks become readable.

## composite material
- reading: At the edge of the packet's branch space, heterogeneous striving resembles straw dispersed through clay: separation may become load-bearing when a forming process binds the pieces.
- mechanism: 
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B004: Clay mixed with straw supplies a composite in which heterogeneous pieces are distributed through one material.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Scattering supplies the dispersion of fibers within the composite.
  - 92:3 **خَلَقَ** خ ل ق B008: Smoothing and leveling a surface supplies the transformation by which a dispersed mixture becomes coherent material.

## guidance by rupture
- reading: A contained split-root activation suggests that guidance may also alter what can be traversed, breaking a barrier or route so that trajectories physically separate.
- mechanism: 
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful going supplies the traveler whose route depends on the state of the terrain.
  - 92:4 **لَشَتَّىٰ** ش ت ت B003: Far-apartness supplies the route divergence that a material intervention could amplify.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication supplies the dominant model of guidance as a sign toward a road.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Severe breaking and demolition supply the exploratory alternative of guidance by opening or closing terrain.

## institutional routing
- reading: Some striving is institutional routing: the same channels of office and warning can protect a community or be turned into accusation and coercive exposure.
- mechanism: 
- trace:
  - 92:4 **سَعْيَكُمْ** س ع ي B003: Public agency supplies an institution that can collect, govern, and act for a group.
  - 92:4 **سَعْيَكُمْ** س ع ي B004: Denunciation to a ruler supplies the opposed use of institutional channels to endanger another person.
  - 92:4 **لَشَتَّىٰ** ش ت ت B003: Far-apartness marks the moral distance between stewardship and weaponized reporting.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: Warning that awakens caution supplies a responsible communicative function distinct from denunciation.
  - 92:20 **رَبِّهِ** ر ب ب B001: Sovereignty supplies the authority toward which institutional speech and action are routed.


# Focus 92:5

## transfer and shield
- reading: The person couples outward release with inward protection: an open hand governed by a guardrail.
- mechanism: One motion releases something outward by handover; the other places the self behind a protective moral barrier. The pairing makes generosity and caution complementary operations rather than reckless openness versus withholding.
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing over and giving supplies the outward transfer and functions as the release phase.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing the self in protective caution supplies guarded self-positioning and functions as the regulating phase.

## protective service
- reading: Giving can be need-attending service that makes protection available while the giver also preserves a protective boundary.
- mechanism: Giving is not exhausted by transfer of an object: it can be responsive attendance that supplies what another needs. Beside it, guarding makes care bounded and protective, so provision can shelter another without dissolving the giver's own moral boundary.
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B003: Serving by attending and handing over what is needed supplies relational care and functions as the provision of protection.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B001: A barrier that wards off harm supplies concrete shelter and functions as the boundary governing the service.

## bold reach with guardrail
- reading: It also permits an exploratory image of entering costly action boldly while guarding that action from overreach.
- mechanism: A latent action geometry pairs committed reach with restraint: the agent enters a demanding affair but installs protection against the same reach becoming trespass or overextension.
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B004: Taking on or reaching boldly into an affair supplies expansion and functions as committed initiative with a live risk of overreach.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Putting the self in protective caution supplies restraint and functions as the guardrail on initiative.

## selective permeability
- reading: Giving and guarding are coordinated boundary operations: release what should pass outward while shielding the self from harmful capture.
- mechanism: The covering/revealing alternation and the later divergence of purposeful movement recast the two focus verbs as regulation of a boundary. Giving opens a passage outward; guarding controls what may cross or harm the self. The agent is selectively permeable, not simply open or closed.
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handover supplies an outward crossing and functions as deliberate opening.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B001: A harm-blocking barrier supplies closure and functions as selective boundary control.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A covering that rises over and conceals supplies the closed pole and makes guarded enclosure spatially visible.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Disclosure and appearance supply the open pole and make release a movement into visibility.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful motion toward an object supplies directed agency and functions as the motion passing through the regulated boundary.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion supplies divergent outcomes and functions as the reason boundary choices matter.

## good made operational
- reading: The gift materially verifies the good, while guarded enactment begins to make that direction easier to inhabit.
- mechanism: The next sequence makes the gift an enactment that verifies the good rather than a detachable token. Guarding stabilizes that enacted commitment, and repeated easing describes feedback in which a chosen act becomes an increasingly traversable path.
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B002: Concrete handover supplies the deed and functions as material verification.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Protective moral caution supplies maintained orientation and functions as stabilization of the deed.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Making a promise true in action supplies performative verification and functions as the bridge from belief to gift.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: Doing a beautiful or good act supplies the valued object and functions as the quality made operational.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening into ease after difficulty supplies reduced resistance and functions as path feedback after enacted commitment.

## security relocated
- reading: Giving releases the reserve that only impersonates safety; guarded orientation, not retained wealth, becomes the operative protection.
- mechanism: The mirrored counter-sequence exposes retention as failed protection: withholding allies with claimed self-sufficiency, opens toward hardship, and accumulated wealth cannot avail at the fall. Against that chain, giving relocates security from the held asset to the guarded orientation of the agent.
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handover supplies release of possession and functions as withdrawal of trust from the stockpile.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B001: Warding harm with a barrier supplies real protection and functions as the alternative location of security.
  - 92:8 **بَخِلَ** ب خ ل B001: Miserly withholding supplies the closed-hand counteraction and functions as attempted preservation by retention.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B002: Sufficiency supplies the claim of needing no support and functions as the false security premise.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B001: Difficulty and severity supply the counter-path's resistance and function as the consequence toward which retention is eased.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated wealth supplies the retained reserve and functions as the tested but ineffective shield.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into destruction supplies terminal exposure and functions as the event wealth fails to prevent.

## beginning to outcome
- reading: Giving and guarding are threshold acts that enter and maintain a guided course from its first movement toward its later outcome.
- mechanism: Guidance supplies a route, while the pairing of latter and former supplies temporal span. The focus verbs can therefore be read as entry operations: transfer and guarding do not merely describe a settled type but initiate a trajectory whose beginning and outcome remain connected.
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handover supplies a decisive outward act and functions as entry into a trajectory.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Self-protective caution supplies continuing regulation and functions as what keeps the trajectory oriented.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward a road supplies direction and functions as the route connecting act to outcome.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: Latter-ness after what is first supplies the far endpoint and functions as temporal extension.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: The beginning and precedence of a thing supplies the near endpoint and functions as the point of departure.

## guarding becomes separation
- reading: Self-guarding participates in a two-sided process that later appears spatially as the agent being placed away from harm.
- mechanism: Warning identifies the harm, meeting fire gives that harm contact geometry, and 92:17 turns protection outward: the one marked by the same guarding root is passively placed to the side. Active self-guarding in 92:5 and effected separation in 92:17 become two phases of one protection relation.
- trace:
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Putting the self in protective caution supplies the active phase and functions as inward preparation.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: A warning that awakens caution supplies hazard recognition and functions as activation of the guard.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies the concrete harm and functions as the object from which distance is required.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Encountering the fire and its heat supplies harmful contact and functions as the inverse of successful protection.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Being made separate and distant supplies spatial removal and functions as the externally effected barrier.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Warding harm by protection recurs in the superlative designation and functions as identity continuity with the focus guard.

## outflow transforms giver
- reading: The outflow of wealth also acts back on the giver, loosening possession and enabling purification or growth.
- mechanism: The later giving echo specifies wealth as the outflow and places reflexive purification or growth beside it. What leaves the giver is not only transferred; its release loops back as a change in the giver's own condition.
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing over supplies the initial outflow and functions as the focus action later specified.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving and bestowal supplies a lexical echo and functions as the later specification of the focus transfer.
  - 92:18 **مَالَهُۥ** م و ل B001: Possessed and accumulated wealth supplies the released material and functions as what must cease to hold the giver.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply positive self-change and function as the return generated through outflow.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purity and soundness supply removal of contamination and function as release from possessive capture.

## gift guarded from debt
- reading: The giver releases the benefit without installing a creditor identity and guards the act from capture by repayment, aiming it beyond exchange.
- mechanism: The negated repayable favor closes the horizontal ledger, while the exception redirects seeking toward a higher face or direction and delayed satisfaction. The focus guard can now protect the gift itself from capture by repayment, prestige, or creditor identity.
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B002: Giving supplies the transferable benefit and functions as the act whose exchange status is contested.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B001: A protective barrier supplies insulation and functions as guarding the gift from reciprocal capture.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive scope under negation supplies ledger-wide exclusion and functions as removal of every human claimant.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: A favor or good condition supplies the possible social debt and functions as the item denied as motive.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matching an act with its recompense supplies reciprocity and functions as the exchange mechanism explicitly negated.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking an object supplies positive aim and functions as the replacement for repayment motive.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and orientation supply a vector beyond the ledger and function as the gift's governing aim.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Satisfaction opposed to displeasure supplies eventual settling and functions as a non-priced completion of the act.

## service as cultivation
- reading: It can also open an ongoing service relation that protects conditions for growth while remaining subordinate to a higher nurturing.
- mechanism: The service branch of the focus gift meets later images of growth and nurturing completion. Giving can therefore be carried as sustained attendance that clears conditions for development, nested under rather than equated with the Lord's completing nurture.
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B003: Attending to a person's affairs and handing over what is needed supplies sustained service and functions as cultivation rather than one-off transfer.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B001: A harm-blocking barrier supplies protected conditions and functions as the enclosure within which service can foster growth.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply developmental change and function as the result toward which service tends.
  - 92:20 **رَبِّهِ** ر ب ب B002: Nurturing, repair, and completion supply formative care and function as the higher process under which the giver's service is placed.

## contest frame canceled
- reading: The focus gift can be heard as exiting the contest itself, refusing both repayment and victory in reciprocal scorekeeping.
- mechanism: 
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B007: Outdoing another in mutual dealing supplies a competitive gift-frame and functions as the latent possibility later canceled.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B005: Prevailing in reciprocal recompense supplies matching competitive exchange and functions as the frame placed under negation.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matching an act with repayment supplies ordinary reciprocity and functions as the ledger from which rivalry would draw its score.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking an object supplies redirected desire and functions as the noncompetitive aim replacing victory in exchange.

## reach with guarded footing
- reading: As a contained body-image, it depicts extending forward while testing one's footing: restraint is what lets initiative move without becoming a fall.
- mechanism: 
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B001: Taking or reaching by hand supplies forward extension and functions as the body's initiative.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B003: A guarded gait that spares a hurting hoof supplies cautious contact and functions as risk-sensitive footing.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B005: Light compliant movement supplies low-friction advance and functions as the gait produced when reach and caution align.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling toward destruction supplies failed footing and functions as the embodied counter-outcome.


# Focus 92:6

## correspondent verification
- reading: He actively brought avowal and inward commitment into correspondence with the good as a governing criterion.
- mechanism: Correspondence between avowal, inward commitment, and what is the case turns the clause into active verification of goodness as a criterion, not mere repetition of a claim.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B001: Truth as correspondence supplies the alignment among speech, inward commitment, and reality that makes the verb an act of verification.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B001: Goodness or beauty opposed to ugliness supplies the definite criterion with which the verifier aligns.

## performative fulfillment
- reading: He made the good true in conduct, confirming it by performing what benefits and exceeds bare fairness.
- mechanism: The two focus roots form a performative circuit: the good is confirmed by being realized as skillful or beneficent conduct.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B004: Confirmation and fulfillment make verification something completed in deed.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: Beneficent, skillful action gives the fulfillment a concrete mode and beneficiary.

## firm bestward alignment
- reading: He set himself firmly and straight toward the utmost good, treating it as an orientation to inhabit.
- mechanism: The material image of solidity and straightness combines with an utmost limit to produce a firm vector toward the best, so assent becomes durable orientation.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B002: Solidity and straightness turn confirmation into a stable, non-crooked bearing.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B005: The utmost effort or limit gives that bearing an extreme bestward endpoint.

## relinquished right
- reading: He certified the good by surrendering a claim and turning that release into benefit.
- mechanism: A derivationally wider but focus-internal reading makes confirmation materially costly: one verifies the good by loosening one's claim over a right or possession for another's benefit.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B006: Charity and relinquished right supply the concrete act by which a claimed good can be verified.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: Beneficent action directs the relinquishment toward enacted good rather than mere loss.

## sincere affiliation
- reading: He entered sincere allegiance with the good, letting truth become a companioning loyalty.
- mechanism: Confirmation becomes affiliation: the reader does not only judge goodness true but takes it as a sincere companion and object of loyal counsel.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B005: Sincere friendship and counsel make truth a relation of loyalty rather than an isolated proposition.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B001: Goodness and beauty supply the value with which the subject forms that sincere affiliation.

## visibility test
- reading: Verification is fidelity to the good across concealment and disclosure, with revelation exposing whether inward and outward alignment held.
- mechanism: Alternating cover and disclosure turns correspondent verification into fidelity under changing visibility: concealment withholds evidence, while disclosure tests whether inner, spoken, and actual alignment endured.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B001: Correspondence supplies the alignment that can persist or fail when visibility changes.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B001: Goodness remains the criterion being held through both phases.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A covering that rises over and hides supplies the low-visibility phase of the test.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Disclosure and appearance supply the phase in which the prior alignment becomes inspectable.

## measured trajectory
- reading: He fixed divergent striving into a measured bestward trajectory by treating the utmost good as its orienting limit.
- mechanism: Measured formation followed by purpose-driven but divergent striving recasts focus-level firmness as selection of a trajectory: the good is the limit that prevents purposeful motion from dispersing.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B002: Straight solidity supplies the stabilizing geometry of the chosen trajectory.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B005: The utmost limit supplies the trajectory's bestward endpoint.
  - 92:3 **خَلَقَ** خ ل ق B001: Measuring and proportioning supply an ordered field rather than undifferentiated motion.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement toward an object supplies directed human motion within that field.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion supplies the competing possibility that purposeful movements diverge.

## giving verifies
- reading: His giving and restraint perform the endorsement: he makes the good credible by transferring benefit and governing exposure to harm.
- mechanism: Giving and self-protective restraint immediately operationalize fulfillment and beneficence: confirmation is evidenced by what leaves the hand and by what the self refuses to expose to harm.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B004: Fulfillment makes confirmation answerable to completed action.
  - 92:6 **وَصَدَّقَ** ص د ق B006: Charity and relinquished right make giving a root-internal form of verification.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: Beneficent action identifies the enacted quality of the good.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing something over supplies the outward transfer that realizes beneficence.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing the self within protection supplies disciplined restraint alongside outward giving.

## path made pliant
- reading: He took a firm bestward bearing, and that alignment became the threshold at which the route opened and motion grew compliant.
- mechanism: The firm bestward bearing of the focus is answered by an opening and a light, compliant motion; confirmation is not arrival but the alignment after which a route becomes traversable.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B002: Straight firmness supplies a stable bearing before movement is eased.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B005: The utmost good supplies the limit toward which the route runs.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening and ease after difficulty supply the route's newly traversable condition.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B005: Lightness and compliance in motion supply the felt mechanics of facilitation.

## mirrored feedback
- reading: Confirmation and denial are rival path-making postures: each relation to the same good progressively opens one mode of movement and constricts another.
- mechanism: The exact denial mirror and the paired ease/difficulty results make confirmation a path-forming stance: acceptance and rejection of the same good feed back into opposite conditions of movement.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B001: Truth as the contrary of lying supplies one pole of the mirrored stance.
  - 92:9 **وَكَذَّبَ** ك ذ ب B001: Falsehood as the contrary of truth supplies the explicit negative pole.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B001: The repeated goodness branch holds the object constant while the stance reverses.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B001: Facilitation retains the opening mechanism but now governs the opposite destination.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B001: Difficulty and severity supply the constricted destination paired with denial.

## wealth as failed ballast
- reading: Confirming the good loosens wealth's claim before retained property becomes useless ballast at the moment of collapse.
- mechanism: Accumulated property promises sufficiency but fails at the fall; this sharpens relinquished-right confirmation into release from a possession that cannot bear the possessor's weight.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B006: Relinquishing wealth or a right supplies the focus-anchored alternative to retention.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: Beneficent action makes release productive rather than merely dispossessive.
  - 92:11 **يُغْنِى** غ ن ي B002: Sufficiency supplies the rescue-function that wealth is asked, and fails, to perform.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Acquiring and accumulating property supplies the retained mass whose adequacy is tested.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into destruction supplies the terminal load-test under which retained wealth cannot suffice.

## whole course
- reading: He trusted and enacted the goodness of a guided course whose beginning, direction, and eventual fulfillment belong together.
- mechanism: Gentle direction joined to beginning, latter end, and eventual outcome expands الْحُسْنَىٰ from a detached prize into the quality and limit of an entire guided course.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B004: Fulfillment supplies the realization of what a course promises at its end.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B005: The utmost limit lets the good name the course's terminal measure.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward a road or truth supplies the course's directional guidance.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: Latter position after a first supplies one temporal boundary of the course.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Beginning and precedence supply the course's other temporal boundary.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Return to an eventual outcome connects first orientation with realized end.

## spatial shielding
- reading: He aligned himself with the good in a way that changed his bearing and, through that bearing, his exposure to an engulfing field.
- mechanism: Flame, turning away, being moved aside, and protection translate focus-level alignment into a spatial-thermal mechanism: relation to the good determines orientation and hence exposure.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B002: Straight solidity supplies the stable orientation from which exposure can be understood.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B001: Goodness supplies the pole toward which the stable orientation is directed.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies the hazardous field of exposure.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure, blazing flame intensifies that field from generic fire to engulfing heat.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning away supplies the negative change of orientation.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Removal and separation to the side supply spatial displacement from the hazard.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Repelling harm by protection supplies the function accomplished by that displacement.

## nonexchange gift
- reading: He made the good true through a gift that releases both property and the claim to human repayment, purifying transfer from leverage.
- mechanism: Transfer of property, purification, negated human repayment, and seeking the highest sustaining presence turn charitable confirmation into a non-exchange gift: its truth lies partly in refusing to convert benefit into leverage.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B006: Charity and relinquishment of a right supply the focus-internal act of releasing a claim.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: Beneficent action makes the released claim produce good for another.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving and delivery supply the outward transfer.
  - 92:18 **مَالَهُۥ** م و ل B001: Possessed and accumulated property identifies what is transferred.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purity and rectitude make motive-cleansing part of the transfer's mechanism.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase preserve the paradox that relinquished wealth can produce a different kind of increase.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Repayment corresponding to an act supplies the exchange ledger that the syntax negates.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking supplies the positive motive that replaces human recompense.
  - 92:20 **وَجْهِ** و ج ه B004: Face as self or essence makes the sought object presence rather than a transferable counterpayment.
  - 92:20 **رَبِّهِ** ر ب ب B002: Nurturing, repairing, and completing supply the sustaining relation toward which the gift is directed.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Height and elevation place that sustaining relation above the horizontal economy of repayment.

## deferred satisfaction
- reading: He commits to the good before satisfaction is available, trusting a fulfillment whose affective adequacy arrives later.
- mechanism: Future satisfaction gives fulfillment a delayed affective closure: one confirms the good before its felt adequacy arrives, so verification includes trust across temporal lag.
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B004: Fulfillment supplies the promise-to-realization arc across the temporal delay.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B005: The utmost limit supplies the not-yet-reached horizon of the good.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Satisfaction opposed to displeasure supplies the eventual felt recognition of adequacy.
  - 92:21 **يَرْضَىٰ** ر ض و B003: Mutual satisfaction keeps open a relational, not merely private, form of closure.

## firmness fertility coupling
- reading: The focus can image a firmness that enters fertile receptivity and thereby becomes generative beneficence rather than sterile hardness.
- mechanism: 
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B002: Solidity and straightness supply a conventionally hard material pole inside the focus.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: Beneficent action requires the firm orientation to become productive for another.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B002: The male branch's hardness and sharpness externalize the hard pole activated near focus-level solidity.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B004: Easy fertile earth supplies a receptive and generative counter-pole rather than mere softness.

## guidance as settling
- reading: He was gently settled into a firm, trusting relation with the good, as though guidance stabilized both judgment and affect.
- mechanism: 
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B002: Solidity supplies the stable condition reached by embodied settling.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B001: Pleasing goodness supplies the attractive and reassuring quality of what is trusted.
  - 92:12 **لَلْهُدَىٰ** ه د ي B006: Rocking a child to sleep supplies the non-dominant embodied image of gentle settling.

## irrigated good
- reading: He confirms good by opening a channel: held resource is released, circulates, nourishes, and appears again as growth.
- mechanism: 
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B006: Charity and relinquishment supply the release of a held resource.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: Beneficent action supplies the good produced beyond the giver.
  - 92:18 **يُؤْتِى** ء ت ي B004: A watercourse and the opening of its way supply the channel through which a released resource moves.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply the downstream effect of successful circulation.
  - 92:20 **رَبِّهِ** ر ب ب B005: Nourishment and development from the non-dominant mapped root supply the ecological function sustained by the flow.

## relational allegiance
- reading: He allied himself sincerely with the good; turning away becomes relational rupture, while eventual satisfaction can be heard as restored reciprocity.
- mechanism: 
- trace:
  - 92:6 **وَصَدَّقَ** ص د ق B005: Sincere friendship, affection, and counsel supply the focus-level relation of allegiance.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B001: Goodness and beauty supply the value to which allegiance is given.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning away supplies the relational rupture that clarifies allegiance by its opposite.
  - 92:21 **يَرْضَىٰ** ر ض و B003: Mutual satisfaction supplies a possible relational closure to sustained allegiance.


# Focus 92:7

## opening readiness
- reading: We will actively fit him for, and make him ready to enter, the opening called al-yusrā.
- mechanism: The doubled root couples operation and endpoint: the subject is not merely handed an easy result but rendered ready for an opening whose character is itself y-s-r.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: An opening that becomes easy and ready after difficulty supplies both the causative preparation and the quality of its endpoint.

## pliant trajectory
- reading: We will make his movement compliant and fluent toward an easy course.
- mechanism: The construction can describe induced fluency of motion: the subject becomes light, responsive, and able to follow a course rather than merely receiving reduced difficulty.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B005: Light, pliant, quickly following movement turns the causative-plus-goal syntax into a model of acquired fluency along a route.

## capacity of means
- reading: The promise expands the subject's means until a spacious, sustainable mode of action becomes available.
- mechanism: Yusr can be carried as ample means or capacity, so facilitation may enlarge what the subject is able to sustain instead of simply lowering the task's cost.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B003: Prosperity and amplitude of means supply a capacity-building sense for both the operation and the destination.

## occlusion to affordance
- reading: The subject is prepared to perceive and enter an opening as it emerges from occlusion into usable visibility.
- mechanism: Covering followed by opening and disclosure makes yusr dynamic: facilitation can be the conversion of a hidden or unusable route into a visible affordance.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Ready opening anchors the focus as a transition into usability.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A cover rising over and concealing something supplies the initial state in which a route can exist without being usable.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B003: Opening and widening until flow becomes possible supplies the transition from obstruction to passage.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Disclosure and appearance make the opened route perceptible, not merely objectively present.

## diverse striving channel
- reading: The focus describes the channeling of divergent effort until the subject moves fluently along one selected trajectory.
- mechanism: Purposeful motion is already divergent; making someone pliant toward yusr therefore channels a particular striving until movement along that route becomes fluent.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B005: Pliant, quick-following movement supplies the focus's kinetic mechanism.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement toward a sought object supplies an already directed human trajectory.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion prevents 'striving' from being one neutral road and makes selective channeling necessary.

## practices prepare path
- reading: Outward transfer, self-protection, and enacted trust make the subject congruent with a route that is then opened and readied.
- mechanism: Transfer outward, protective self-placement, and enacted verification of the good form a practical configuration to which the focus responds by opening a congruent route.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Readiness after resistance supplies the responsive opening produced in the focus.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing something over supplies outward transfer as the first path-forming act.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing oneself within protection supplies active boundary-setting rather than passive fear.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Realizing a promise in action turns assent into a performed commitment.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: Doing what is good gives the commitment a practical rather than merely aesthetic endpoint.

## direction neutral fitting
- reading: The verb names efficient fitting to a destination; 92:7 is good because the subject is fitted to al-yusrā, not because facilitation is always good.
- mechanism: The same causative y-s-r operation points toward opposed endpoints. Facilitation is therefore direction-neutral fitting or increasing accessibility; moral and experiential value lies in the endpoint and in the dispositions with which the subject becomes aligned.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Ready opening supplies the operation whose positive value initially seems intrinsic.
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding supplies the opposed practical disposition before the mirrored causative.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed self-sufficiency closes the subject around existing means and helps define the contrary alignment.
  - 92:9 **وَكَذَّبَ** ك ذ ب B002: Assigning falsity to the good supplies a repudiated endpoint rather than a mere factual error.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B001: The good as the contrary of ugly identifies what the second subject refuses.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B001: The exact same readiness-making operation reappears, proving that its directional efficiency can serve a contrary endpoint.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Opposition, twisting, and induced difficulty give the mirrored endpoint a path-like resistance rather than simple discomfort.

## guided course against fall
- reading: Yusr is a guided, controllable course that prevents motion from becoming an ungoverned fall, even where the terrain remains demanding.
- mechanism: The route model acquires vertical stakes: fluent guidance toward yusr is contrasted with uncontrolled descent, while a non-dominant mapped branch keeps the image of a difficult slope live.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B005: Light, well-following movement anchors facilitation as controlled locomotion.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into ruin supplies the uncontrolled terminal motion against which fluent routing matters.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward a road or truth supplies a directional aid rather than forced transport.
  - 92:12 **لَلْهُدَىٰ** ه د ي B009: The non-dominant mapped image of a difficult descent adds exploratory topographic pressure: guidance is meaningful on terrain that can pitch downward.

## whole arc preparation
- reading: The future promise can name a progressive preparation whose governance spans the first step, successive adjustments, and the final issue.
- mechanism: Firstness, succession, and the later end stretch facilitation across a whole temporal arc: readiness can be progressively formed from inception through outcome.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Becoming ready supplies a process capable of unfolding through time.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B002: Deferral to a later time supplies the far end of the process.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: The beginning and precedence of a thing supply the process's near end.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: The non-dominant mapped image of one thing following another supplies incremental succession between beginning and end.

## protective side routing
- reading: Ease can mean being given a traversable corridor that routes the subject to the side of an exposure zone altogether.
- mechanism: Fire defines an exposure zone, contact realizes its danger, and protective side-leading creates a safe corridor. The focus's opening can therefore be spatial rerouting around harm, not merely subjective relief.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: A ready opening supplies the traversable corridor in the focus.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies the material hazard around which a route must be organized.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Meeting fire and its heat defines failure as contact rather than mere awareness of danger.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B005: Leading something to the side supplies an active lateral rerouting operation.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Repelling harm through protection gives the side movement its functional purpose.

## released means become growth
- reading: Yusr as ample capacity is formed through releasing resources into a circulation that increases and purifies the giver.
- mechanism: The prosperity baseline is reversed from storage to circulation: means are handed outward, and their release is followed by increase and purification. Capacity grows through expenditure rather than enclosure.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B003: Amplitude of means anchors the focus's exploratory prosperity reading.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving or delivering supplies the outward movement that prevents means from being modeled as hoarded stock.
  - 92:18 **مَالَهُۥ** م و ل B001: Possessing and accumulating wealth supplies the stock that is deliberately released.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply the productive result that follows circulation.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purification prevents growth from being reduced to greater quantity alone.

## nontransactional orientation
- reading: The opened route is sustained by a non-reciprocal, upward-facing aim rather than by expectation of repayment.
- mechanism: A horizontal repayment ledger is negated and replaced by active seeking toward a high-facing direction. Yusr becomes an orientation that organizes action without requiring reciprocal return.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Ready opening anchors the focus as a direction that can organize action.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matching an act with recompense supplies the transactional mechanism that the surrounding negation excludes.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Active seeking supplies motive and forward pressure after reciprocal payment is removed.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and orientation turn seeking into a vector rather than an unspecified desire.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Elevation gives the vector a vertical ordering beyond horizontal exchange.

## nurtured completion to satisfaction
- reading: Ease is a cultivated maturation whose success appears when the subject can finally receive and inhabit the outcome with satisfaction.
- mechanism: Cultivation and completion connect the focus's readiness to the final future satisfaction: ease is a maturation into a condition the subject can inhabit with acceptance.
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Becoming ready supplies an unfinished developmental state rather than an instant reward.
  - 92:20 **رَبِّهِ** ر ب ب B002: Repair, nurture, and bringing to completion supply the developmental agency between opening and fulfillment.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Acceptance rather than displeasure supplies the experiential completion of the prepared course.

## lateralized route
- reading: The verse may also project that change spatially as routing the subject into a designated side or corridor, while refusing to make leftness itself good or bad.
- mechanism: 
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B004: The left side and leftward direction supply a lateral schema for the focus's goal construction.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B005: The opposed endpoint also carries left-sidedness, blocking an easy equation of lateral side with moral value.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B005: Leading something to one side shows that protective transformation can be represented as lateral routing.

## lot without ledger
- reading: The subject is prepared for a favorable share or distribution whose value is precisely that it is not governed by reciprocal debt collection.
- mechanism: 
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B007: Lots and the division of a slaughtered animal into shares supply the focus's latent allotment mechanism.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Collecting and settling a debt supplies the ledger model that the verse's negation refuses.
  - 92:20 **رَبِّهِ** ر ب ب B010: The form-distant image of a container gathering lots reinforces an allocation apparatus while remaining deliberately quarantined from the source word's ordinary reading.

## fecund ease
- reading: Ease can be imagined as a cultivated fecundity in which released means generate more life, capacity, and usable output.
- mechanism: 
- trace:
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B006: Productive increase in milk and offspring supplies a fecund, output-generating model of yusr.
  - 92:18 **يُؤْتِى** ء ت ي B007: Emergence of growth and produce supplies output after giving rather than depletion.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Increase and growth generalize the productive mechanism beyond a single material image.
  - 92:19 **نِّعْمَةٍ** ن ع م B005: Livestock wealth provides a context-side material bridge to the focus's productive-livestock image.
  - 92:20 **رَبِّهِ** ر ب ب B014: A gathered herd supplies the social-material unit within which fecund increase becomes sustained abundance.


# Focus 92:8

## closed autonomy
- reading: A person closes what should circulate and interprets that closure as exemption from need.
- mechanism: A possession that ought to pass outward is held inside, while need itself is disavowed. Withholding and self-sufficiency therefore form one closure mechanism rather than two unrelated defects, although the focus alone leaves open whether felt independence licenses retention or retention manufactures felt independence.
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding possessions from an outlet where they should not be withheld supplies the closed material boundary.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Wealth or reduced need supplies the inward claim that makes the closed boundary appear sufficient.

## retained proxy
- reading: He keeps a possession in place so that it can impersonate the relations and supports he refuses to need.
- mechanism: The retained possession is not merely accumulated; it is appointed as a substitute for whatever relation, recipient, or support the subject declines. بخل secures the proxy by preventing its departure, and استغناء names confidence that the proxy can stand in for what has been excluded.
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Wrongful retention keeps the would-be substitute under the subject's control.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B002: Sufficing and standing in for something supplies the proxy relation assigned to the retained asset.

## covered dependency
- reading: Self-sufficiency may be the covering performance by which stinginess keeps an unacknowledged dependency out of view.
- mechanism: The opening alternation of covering and disclosure turns self-sufficiency from a transparent condition into a possibly occluding presentation. Withholding seals the dependency inside; the claim of no need is the cover whose adequacy remains exposed to a later unveiling.
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding from a rightful outlet supplies the sealed interior whose dependencies can be hidden.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed wealth or needlessness supplies the content presented as complete.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A cover rising over and concealing a thing supplies the occluding function assigned to the sufficiency claim.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Uncovering and appearance supply the counter-operation that can expose the dependency retained beneath the claim.

## relational exemption
- reading: An individual attempts to opt out of relation inside a created order presented through coordinated difference.
- mechanism: Measured creation is displayed through differentiated counterparts. Against that field, استغناء can be heard not only as financial independence but as an attempted exemption from constitutive relation, while بخل is the practical refusal to let anything cross between self and counterpart.
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding what should reach another supplies the enacted refusal of relation.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Reduced or absent need supplies the claimed exemption from dependence.
  - 92:3 **خَلَقَ** خ ل ق B001: Measured formation supplies an ordered field in which difference is constituted rather than self-originating.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: The male counterpart supplies one side of an explicitly differentiated pair.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The female counterpart supplies the other side, making isolated completeness less natural as a reading of the world.

## forecast hardens path
- reading: Withholding is a wager against the good whose repetition lowers friction toward an increasingly constricted route.
- mechanism: The mirrored sequences bind allocation to a forecast about the good and then to increasing ease of motion. Giving accompanies making the good credible and a lightened route; withholding and self-sufficiency accompany discrediting it and a route that twists into difficulty. بخل thus becomes an enacted prediction that release will not be made good, and repeated action makes that prediction easier to inhabit.
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Wrongful withholding supplies the allocation decision whose implicit forecast is being reconstructed.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Self-sufficiency supplies the internal rationale that retained stock is enough without an outward return.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing something over supplies the opposite allocation against which focus withholding becomes legible.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Making a promise or action real supplies the positive expectation that can support release.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B005: Lightness and compliant movement supply the low-friction trajectory paired with the giving sequence.
  - 92:9 **وَكَذَّبَ** ك ذ ب B002: Assigning a thing to falsehood supplies the rejected forecast paired with withholding.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: The repeated lightening of motion supplies path dependence even when the destination is adverse.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Twisting, opposition, and induced difficulty supply the shape of the path made easier to follow.

## proxy fails at fall
- reading: The person has appointed wealth to answer in his place, but the text immediately stages the condition under which that proxy cannot answer.
- mechanism: The return of غ ن ي under negation tests the focus claim in its availing sense. The retained wealth has been treated as a stand-in; at the moment of falling it cannot stand in for the person, so the focus self-sufficiency becomes proleptic irony rather than a durable state.
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding keeps the asset available as the subject's chosen reserve and proxy.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B002: Sufficing or standing in for another supplies the precise proxy claim made in the focus.
  - 92:11 **يُغْنِى** غ ن ي B002: The same availing function returns under explicit negation, supplying the failed test of the proxy.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated wealth identifies the retained stock asked to perform the availing function.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: A fall into ruin supplies the boundary condition at which the substitute ceases to work.

## compressed horizon
- reading: The focus actor mistakes the present inventory for the terminal horizon and therefore withholds against a future he has edited out.
- mechanism: Guidance supplies direction, while the later and the first stretch evaluation across the whole temporal arc and toward an outcome. Against that arc, بخل plus استغناء looks like horizon compression: present stock is treated as terminally sufficient, so deferred direction and consequence are discounted.
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Present retention supplies the locally certain gain privileged by the compressed horizon.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Current enoughness supplies the claim that no later orientation or provision is needed.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward a road or truth supplies direction beyond the actor's present inventory.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B002: Deferral to a later time supplies the future interval excluded by presentist sufficiency.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Return to an eventual outcome supplies the terminal reckoning that current retention cannot define.

## self shield vs separation
- reading: The actor tries to manufacture immunity from retained resources, but the later spatial grammar separates self-withdrawal from effective protection.
- mechanism: The warning sequence distinguishes turning away from actually being placed at a safe distance. استغناء can therefore be read as a self-made shield: retained means are expected to remove exposure, but withdrawal only changes orientation; effective separation and protection arise through a different relation.
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Retained possession supplies the material from which the actor tries to make a private shield.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B002: A thing's capacity to suffice or spare another supplies the expected protective function of the shield.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: A warning that awakens caution supplies explicit exposure to danger rather than assumed immunity.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies the harmful field from which safe distance would have to be real.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning the back and withdrawing supplies orientation away from danger without guaranteeing distance from it.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Being removed, kept apart, or made distant supplies actual separation rather than a posture of withdrawal.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Repelling harm by protection supplies the successful function that retained wealth only pretends to perform.

## release grows giver
- reading: Withholding conserves the object while stunting the holder; release is the apparent loss through which the giver grows or becomes sound.
- mechanism: The later subject gives his own wealth and undergoes reflexive growth or purification. This reverses the conservation logic of بخل: transfer is not depletion of the self but a means or manifestation of its increase, while retention preserves the object at the cost of arresting the holder.
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Keeping possessions from their due outlet supplies the conservation strategy that the later sequence reverses.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Possessive enoughness supplies the mistaken equation between keeping the asset and preserving the self.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving and conveying supplies the outward transfer that appears to reduce the inventory.
  - 92:18 **مَالَهُۥ** م و ل B001: Acquired or abundant wealth identifies the very substance released rather than an abstract kindness.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply the counterintuitive gain occurring on the giver's side of the transfer.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purification and soundness supply a second reflexive transformation enabled or displayed by release.

## closed ledger
- reading: The miser permits no uncompensated passage and calls a fully settled human ledger self-sufficiency; the counter-gift leaves that bilateral ledger altogether.
- mechanism: The later gift is detached from a human favor awaiting settlement and redirected toward a sought end. This activates a transactional reading of focus closure: بخل releases nothing without an equivalent entry, while استغناء seeks a balance sheet on which no unpriced dependence remains. The counter-model gives without making the recipient a debtor or a prior benefactor a creditor.
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Wrongful withholding supplies the refusal to release value without a balancing claim.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B002: Sufficing or replacing supplies the closed ledger's demand that every relation be made equivalent and dispensable.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Totalizing negation excludes any human party from occupying the creditor position.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: A favor or good condition supplies the value that might otherwise create a reciprocal claim.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Collecting and settling a debt supplies the bilateral accounting operation explicitly excluded from the gift.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking a thing supplies a motive that directs the transfer beyond repayment.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and orientation supply the non-bilateral endpoint toward which the released value is aimed.

## premature satisfaction
- reading: The focus actor forces satisfaction too early by closing his hand, while the closing sequence imagines enoughness as something that can arrive after the hand opens.
- mechanism: The focus actor produces present needlessness by retaining, whereas the closing actor is promised future satisfaction after release. استغناء and رضا become rival temporal forms of enoughness: one is seized in advance by closure, the other arrives after exposure to loss and is compatible with acceptance rather than self-exemption.
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Retention supplies the immediate technique for forcing an experience of enoughness.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed absence of need supplies the premature satisfaction secured in the present.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Contentment opposed to discontent supplies the later state that does not require denial of need.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Acceptance as the contrary of discontent independently preserves the closing state's receptive rather than self-sealing quality.

## sung sufficiency
- reading: Self-sufficiency is also a refrain the withholder performs until retained wealth sounds like a complete world.
- mechanism: 
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding supplies the material conduct for which the vocal performance provides a refrain.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B003: Song and vocal modulation supply the image of repeatedly making closure sound like completeness.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B004: A matter running on the tongue supplies verbal circulation for the self-sufficiency refrain.
  - 92:6 **وَصَدَّقَ** ص د ق B001: Truthful speech supplies one evaluative pole for the voiced claim.
  - 92:9 **وَكَذَّبَ** ك ذ ب B001: Falsehood supplies the opposite pole and allows the refrain to be heard as self-persuasion rather than report.

## hydraulic withholding
- reading: The person blocks a channel: the apparent conservation upstream prevents the growth that circulation would produce downstream and in the giver.
- mechanism: 
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding from a due outlet supplies the obstruction at the center of the flow model.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B003: Opening and widening until something flows supplies the inverse operation to withholding.
  - 92:18 **يُؤْتِى** ء ت ي B004: A watercourse and the clearing of its path supply the channel through which the later transfer can move.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply the downstream result of restored circulation.

## drift as autonomy
- reading: Self-sufficiency may misname abandonment to an increasingly frictionless drift after relation has been withheld.
- mechanism: 
- trace:
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed needlessness supplies the appearance of autonomous motion.
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding relation and resource supplies the practical severance that leaves the actor to himself.
  - 92:4 **سَعْيَكُمْ** س ع ي B002: Neglect and going off without a governed direction supply the alternative image of what self-directed striving may become.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: Light, compliant motion supplies the unsettling possibility that drift can become increasingly easy.

## wealth dwelling
- reading: The person moves into retained wealth as a dwelling, only for the later fall to reveal that the enclosure has no reliable floor.
- mechanism: 
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Retained possessions supply the walls and contents of the imagined enclosure.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B004: Settled dwelling and prolonged residence supply the image of taking up habitation inside what has been retained.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into ruin supplies the loss of footing that tests whether the enclosure was ever a stable home.


# Focus 92:9

## declarative falsification
- reading: He actively classifies the good or beautiful itself as false.
- mechanism: The clause stages more than uncertainty: an agent actively assigns falsehood to the good or beautiful as such.
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B002: Declaring a thing or its bearer false supplies the clause's active verdict.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B001: Goodness or beauty opposed to ugliness supplies what the verdict repudiates.

## performative betrayal
- reading: His conduct makes the good's practical claim fail.
- mechanism: The denial can be enacted: the agent makes the charge of beneficent conduct fail by refusing to carry it through.
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B004: A charge that proves false by not being carried through turns denial into failed performance.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B002: Beneficent, skillful action supplies the good whose practical realization is withheld.

## failed best expectation
- reading: He treats the best attainable end as an expectation that will not hold.
- mechanism: The clause can register anticipatory distrust: the best attainable end is treated like a provision expected to last but assumed to fail.
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B006: Milk that fails an expectation of continuance supplies a material image of disappointed reliance.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B005: The utmost effort or limit lets حُسْنَىٰ function as the best attainable end.

## occlusion of visible good
- reading: Denial can be an active occlusion of a good that has become available to sight.
- mechanism: The opening cover-and-disclosure cycle recasts denial as an overlay placed upon goodness that can become visible, not simply as absence of evidence.
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B002: The active assignment of falsehood anchors the reader's proposed re-covering.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B001: Goodness and beauty provide the potentially perceptible object being covered.
  - 92:1 **وَٱلَّيْلِ** ل ي ل B001: Night's darkness supplies the scene in which visibility is withdrawn.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A covering that rises over and conceals something supplies the occlusive operation.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: Day opening through light supplies the contrary condition of visibility.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Uncovering and appearance make disclosure an event rather than a static property.

## divergent striving without measure
- reading: He rejects the orienting limit by which scattered effort could become coherent.
- mechanism: Measured creation, paired differentiation, purposeful movement, and dispersed pursuits activate حُسْنَىٰ as an orienting limit; denying it leaves effort active but without a common measure.
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B004: Failure to carry a charge through lets denial appear as striving that does not fulfill its direction.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B005: The utmost limit supplies a possible common endpoint for otherwise divergent striving.
  - 92:3 **خَلَقَ** خ ل ق B001: Measuring and proportioning supply an ordered background for differentiated existence.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: The masculine side supplies one pole of the explicitly paired differentiation.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The feminine side supplies the other pole without erasing distinction.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement toward an object makes striving directional.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Scattering supplies the loss of convergence among those directed movements.

## good verified in transfer
- reading: He falsifies the good in practice by withholding and treating himself as relationlessly sufficient.
- mechanism: The matched sequences make confirmation and denial materially testable: giving and self-protection enact confirmation of beneficent good, while withholding and claimed self-sufficiency enact its falsification.
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B004: A charge made false by failure to carry it through anchors denial as counter-performance.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B002: Benefiting another and exceeding bare justice identify the practical content at stake.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing something over supplies the outward transfer that realizes the good.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing oneself within protection supplies the inward discipline paired with giving.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Realizing a promise or deed makes confirmation performative rather than merely verbal.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: The repeated object identifies beneficent action as what the positive sequence verifies.
  - 92:8 **بَخِلَ** ب خ ل B001: Stinginess supplies the withheld transfer that materially contradicts beneficence.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed self-sufficiency supplies the posture that makes relation and gift seem unnecessary.

## facilitated path dependence
- reading: Denial is a hinge that makes a self-obstructing course progressively easier to travel.
- mechanism: The repeated facilitation formula around opposed destinations turns the focus stance into path formation: denial becomes an entry condition through which obstruction grows easy to follow.
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B004: A charge that fails in execution anchors the stance as a trajectory, not an isolated statement.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B005: The utmost limit supplies the destination from which the failing trajectory diverges.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening into ease supplies the positive path's increasing traversability.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: Lightness and compliance in motion make even the negative path easy to enter and continue.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Twisting, opposition, and obstruction supply the paradoxical destination of that facilitated motion.

## substitute that proves false
- reading: His declaration displaces trust onto wealth, which then becomes the provision that actually fails expectation.
- mechanism: Claimed self-sufficiency precedes the focus, but wealth later fails to suffice at the fall; falsehood rebounds from the rejected best onto the material substitute trusted instead.
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B006: A provision that disappears instead of lasting supplies the focus's expectation-failure image.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B001: The rejected good supplies the displaced object of reliance.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Self-sufficiency supplies the initial claim that no external good is needed.
  - 92:11 **يُغْنِى** غ ن ي B002: Actual sufficiency is explicitly tested and found absent at the decisive moment.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated wealth identifies the concrete substitute expected to provide sufficiency.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into destruction supplies the event at which the substitute's promise fails.

## guidance as gifted direction and end
- reading: He rejects a gifted direction whose beginning, route, and best horizon have been made available.
- mechanism: Gentle indication toward a road, followed by possession of first and last, activates حُسْنَىٰ as a disclosed direction and terminal horizon rather than an unsupported promise.
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B002: Declaring something false anchors rejection of the offered direction.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B005: The ultimate limit lets the good function as the road's horizon.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward road and truth supplies disclosed direction rather than coercion.
  - 92:12 **لَلْهُدَىٰ** ه د ي B004: A gift sent toward one held in affection lets guidance be received as offered relation.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: Lateness after the first supplies the far end of the temporal span.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Beginning and precedence supply the near end from which the guided course opens.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Return to outcome makes the beginning root also carry the course's eventual issue.

## denial turns away from warning
- reading: He turns away from the good in a way that disables warning and leaves him oriented toward exposure.
- mechanism: Warning is meant to awaken protective caution, but the focus verb is later repeated beside bodily turning away; denial therefore becomes an orientation that converts available warning into exposure, opposite being moved aside and protected.
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B002: The focus verdict supplies the act whose directional consequences are unfolded.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B001: The good supplies what the warned agent turns away from.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: Warning that frightens in order to wake caution supplies a still-open protective function.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies the danger to which the warning points.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure blazing flame intensifies the warned exposure.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Meeting fire and its heat turns danger from a distant sign into contact.
  - 92:16 **كَذَّبَ** ك ذ ب B002: Repetition of the focus verb carries its denial directly into the later characterization.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning the back and withdrawing gives the repeated denial a bodily direction.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Being distanced and kept apart supplies the contrary spatial outcome.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Repelling harm through protection completes the warning-to-safety alternative.

## nonreciprocal beautiful excess
- reading: He rejects the beautiful excess by which giving escapes repayment, grows the giver, and reaches satisfaction through a higher orientation.
- mechanism: The closing sequence makes the good an economy of excess rather than equivalence: wealth is given for purifying growth, not to settle another person's favor, but toward a higher face and nurturing sovereignty, ending in acceptance and satisfaction.
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B004: Failure to carry a charge through anchors denial as refusal to enact this non-reciprocal good.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B002: Benefiting another beyond bare justice supplies the focus ideal's gratuitous excess.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving supplies the outward movement by which the non-reciprocal good becomes actual.
  - 92:18 **مَالَهُۥ** م و ل B001: Accumulated wealth supplies what is released rather than retained as self-sufficiency.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase make relinquishment productive rather than merely subtractive.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: A favor or good condition supplies the possible social debt that the clause negates.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matching an act with its recompense supplies the exchange model explicitly left behind.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking supplies the positive aim that replaces repayment as motive.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and orientation give that seeking a vector beyond the human exchange partner.
  - 92:20 **رَبِّهِ** ر ب ب B002: Nurturing, repair, and completion supply the relation within which released wealth becomes growth.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Elevation supplies the higher orientation that exceeds horizontal repayment.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Satisfaction opposed to resentment supplies the affective completion of the gift trajectory.

## counterfeit beauty surface
- reading: He may counterfeit beauty through a surface that conceals its contrary until disclosure.
- mechanism: 
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B009: A patterned cloth that lies through its condition supplies counterfeit appearance.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B001: Beauty opposed to ugliness supplies the attractive surface being counterfeited.
  - 92:1 **يَغْشَىٰ** غ ش و B001: Covering and concealment supply the overlay that lets appearance mask condition.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Disclosure supplies the event in which the counterfeiting surface can be exposed.
  - 92:20 **وَجْهِ** و ج ه B015: Two-facedness supplies the social analogue of a surface that presents incompatible orientations.

## interrupted animal motion
- reading: Denial can be pictured as striving that breaks, looks back, turns away, and converts momentum into a fall before the best limit.
- mechanism: 
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B007: Running and then stopping to look back supplies an interrupted trajectory within the focus verb.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B005: The utmost limit supplies the endpoint not reached by the interrupted motion.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement establishes the broader field in which interruption matters.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: Compliant light motion supplies momentum after the focus hinge.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: A fall into destruction supplies the kinetic course's eventual collapse.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning back and withdrawing confirms reversal rather than arrival.

## guidance threat split
- reading: He rejects a gently indicated horizon until the same directional address is encountered in the register of threat.
- mechanism: 
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B002: Active falsification supplies the resistant reception of what is offered.
  - 92:9 **بِٱلْحُسْنَىٰ** ح س ن B005: The ultimate limit supplies the direction's intended horizon.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: The dominant mapped branch supplies gentle indication toward road and truth.
  - 92:12 **لَلْهُدَىٰ** ه د ي B010: The non-dominant mapped branch supplies warning and threat as a harsher register.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: Warning that awakens caution gives the harsher register contextual traction.


# Focus 92:10

## ready for hard course
- reading: We will make him ready and easy-moving for the hard course; the person, not the hardship, is what becomes facilitated.
- mechanism: Ease here need not be the quality of the destination. The causative can make the person ready, available, or low-resistance for a destination that remains hard.
- trace:
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B001: Ease and ready opening supply the causative preparation that makes the person traversable toward an endpoint.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B001: Difficulty and severity keep the destination objectively hard even while access to it is made easy.

## means reversal
- reading: He is made to enter a narrowing of means in which claimed capacity becomes insolvency and exposure to demand.
- mechanism: The same line can stage a reversal of material capacity: a person is conducted from the posture of ample means into inability, exposure, and creditor-like pressure.
- trace:
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B003: Prosperity and breadth of means supply the starting capacity that the verse can reverse.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B002: Straitness and insolvency turn عسرى into loss of usable means rather than undifferentiated pain.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B003: Pressure upon an insolvent debtor gives the endpoint a social mechanism of demand arriving when capacity has failed.

## compliance into entanglement
- reading: Resistance is lowered in the traveler while the route becomes more entangled: ease describes compliance with harm, not relief from it.
- mechanism: Facilitation can remove resistance without improving the result. The person becomes behaviorally compliant and therefore moves more readily into an increasingly tangled course.
- trace:
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: Light, pliant following supplies reduced resistance and smooth continuation as the operative kind of ease.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Opposition, twisting, and complication supply the self-entangling structure into which that compliance feeds.

## repeated operator channels divergence
- reading: يسر names a polarity-neutral channeling operation: opposite patterns of striving can each be made progressively easier to continue toward opposite ends.
- mechanism: Covering and disclosure frame striving that is both directed and dispersed; the exact يسر construction at 92:7 then shows the same facilitative operator feeding the opposite course. Facilitation is therefore better read as channel formation than as a synonym for beneficence.
- trace:
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B001: Ready opening supplies the repeated operation by which a course becomes increasingly available.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B001: Severity preserves the negative polarity of this endpoint despite the shared facilitative operator.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A covering laid over something supplies the phase in which a trajectory can form without yet being visible.
  - 92:1 **يَغْشَىٰ** غ ش و B007: The split-root image of understanding being overcast extends concealment from the scene to the agent's own recognition.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Uncovering and appearance supply the later disclosure of the course that prior action has opened.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement toward an objective supplies directed striving as the material being channeled.
  - 92:4 **سَعْيَكُمْ** س ع ي B002: The non-dominant split image of heedless wandering keeps open a rival mode in which motion continues without lucid orientation.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion supplies the branching of human efforts into genuinely divergent trajectories.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: The mirrored ready-opening construction supplies the positive channel against which 92:10 functions as an opposed channel.

## actions train affordances
- reading: The authority ratifies a behavioral feedback loop: withholding, self-sufficiency, and denial train the person into ever easier compliance with an increasingly difficult course.
- mechanism: The opposed action clusters before the two facilitation formulas behave like training inputs. Giving, self-protection, and enacted truth open one set of affordances; withholding, claimed self-sufficiency, and active falsification train the agent to follow the entangled course with less friction.
- trace:
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: Pliant, quick-following movement supplies the learned ease with which a practiced pattern continues.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Mutual opposition and complication supply the worsening structure generated by the negative pattern.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Concrete transfer and giving supply an outward act that opens rather than seals circulation.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing oneself within protection supplies anticipatory restraint rather than presumed immunity.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Realizing a promise in action supplies behavioral confirmation rather than merely holding a proposition.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B001: Goodness opposed to ugliness supplies the positive valuation toward which the first action cluster is fitted.
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding supplies the closure that begins the contrary feedback loop.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed independence supplies the belief that removes perceived need for correction or protection.
  - 92:9 **وَكَذَّبَ** ك ذ ب B002: Attributing falsehood supplies an active rejection that rehearses and stabilizes the contrary course.

## hoarded means become straitened
- reading: The difficult course is the maturation of hoarded sufficiency into straitened means: what was kept as protection becomes unable to protect at the fall.
- mechanism: The local sequence joins withholding and claimed independence to a focus-root reversal from means to straitness, then declares that wealth cannot suffice at the fall. The hard course is materially legible as a strategy of security turning into incapacity.
- trace:
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B003: Abundant means supply the capacity the hoarder imagines he possesses and can preserve.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B002: Insolvency and narrow means supply the concrete reversal hidden inside the difficult destination.
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding supplies the attempted method of retaining capacity.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Self-sufficiency supplies the agent's mistaken diagnosis of his own material independence.
  - 92:11 **يُغْنِى** غ ن ي B002: Sufficing capacity, explicitly negated in the source construction, supplies the failure of the security strategy.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Possessed wealth supplies the stored resource that proves unable to perform when needed.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into ruin supplies the event at which nominal possession is exposed as unusable means.

## low friction descent
- reading: Ease can be the terrifying removal of resistance on a steep downward course: the traveler moves smoothly precisely because he is falling.
- mechanism: Light, compliant motion in the focus is followed by a fall, while the split inventory for guidance supplies both gentle road-direction and a branch-distant steep descent. Read topographically, facilitation can be loss of friction: it accelerates rather than rescues the traveler on a downward grade.
- trace:
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: Light, readily following movement supplies the reduced resistance that can become dangerous on a descent.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Twisting complication supplies rough terrain and loss of controllable alignment rather than a merely painful endpoint.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: A fall into destruction supplies the immediate kinetic consequence of the facilitated course.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle direction toward a road supplies the dominant route-reading against which the dangerous route can be perceived.
  - 92:12 **لَلْهُدَىٰ** ه د ي B009: The non-dominant split image of a difficult steep descent supplies the surprising terrain on which ease becomes acceleration.

## fire corridor and side exit
- reading: The line routes a person into an exposure corridor, opposed later by a causative side-movement that keeps the protected person away from its flame.
- mechanism: The later fire sequence gives the difficult course a routed endpoint. Meeting heat realizes one corridor, while being moved aside and protected realizes its spatial opposite; 92:10 is thus one operation in a two-route architecture.
- trace:
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B001: Readiness and opening supply access into the corridor rather than mitigation of what the corridor contains.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B001: Severity supplies the corridor's hard polarity before its fiery realization is disclosed.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies the concrete hazard toward which the hard course can terminate.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure leaping flame intensifies the endpoint from generic difficulty to active exposure.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Encountering fire and its heat supplies bodily arrival within the dangerous corridor.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B001: The second split target independently preserves contact with heat, strengthening exposure rather than a ritual reading here.
  - 92:15 **ٱلْأَشْقَى** ش ق و B002: Hardship and arduous suffering lexically couple the exposed traveler to the focus destination.
  - 92:15 **ٱلْأَشْقَى** ش ق و B002: The alternate mapped root repeats severity and toil, keeping both split targets aligned with the hard corridor.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Being distanced and kept apart supplies a lateral exit from the fire corridor.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Repelling harm by protection supplies the functional result of that side-routing.

## hard share in a debt ledger
- reading: The person is allocated the hard share in a ledger where retained means become collectible liability, while unreciprocated giving exits the human debt cycle.
- mechanism: The focus inventories join allotted shares to pressure on an insolvent debtor. The later giver transfers wealth for purification while negating any human favor to be repaid; this activates two economies, one of possessive allocation and collectible liability and another that exits reciprocal accounting.
- trace:
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B007: Lots and division into shares supply an allocation mechanism by which the person receives the hard share.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B003: Pressing an insolvent debtor supplies liability becoming demand at the point of failed means.
  - 92:18 **يُؤْتِى** ء ت ي B002: Active giving supplies transfer out of possession rather than accumulation within the ledger.
  - 92:18 **مَالَهُۥ** م و ل B001: Possessed wealth supplies the material being released and contrasts with wealth retained as security.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purity and rectification supply a purpose for giving that is not equivalent exchange.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive negation supplies the exclusion of every human claimant from the giver's motive.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: A benefit or favor supplies the social credit whose repayment is explicitly denied as motive.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Debt collection and full recovery supply the reciprocal ledger from which the later giving is detached.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: The non-dominant split image of cutting supplies a branch-distant severance of the return obligation.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking an object supplies the positive motive that replaces collection from human debtors.

## harm becomes subjectively easy
- reading: Facilitation may change the person affectively: denial and turning train him to experience the objectively entangled course as natural and easy.
- mechanism: Denial and turning away can progressively remove the felt friction of the hard course. The final acceptance imagery makes affect itself part of the surah's endpoint logic, allowing a dangerous reading in which facilitation is accommodation to harm rather than objective relief.
- trace:
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: Pliancy and quick following supply subjective ease and habitual compliance.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Objective complication remains in place while the person's resistance to it diminishes.
  - 92:16 **كَذَّبَ** ك ذ ب B002: Charging the truth with falsehood supplies cognitive rehearsal that suppresses corrective friction.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning away supplies the bodily and attentional maneuver by which warning ceases to interrupt the course.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Satisfaction and acceptance supply the broader possibility that an endpoint includes a transformed affective relation to one's course.
  - 92:21 **يَرْضَىٰ** ر ض و B001: The alternate mapped root independently preserves acceptance, so the affective cue is not confined to one split target.

## blocked fruition
- reading: The person is made productive in motion yet directed toward blocked fruition: activity multiplies, but nothing viable is brought forth.
- mechanism: 
- trace:
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B006: Abundant milk and offspring supply productive potential and visible increase.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B006: Difficult childbirth supplies a process that reaches fruition only through obstruction and pain.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B007: Failure to conceive supplies the stronger possibility that apparent productive capacity never bears fruit.
  - 92:3 **خَلَقَ** خ ل ق B002: Bringing creation into being supplies the larger generative frame for the dormant reproductive contrast.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B004: Easy fertile earth supplies the ecological image of a medium capable of receiving and producing.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase reactivate fruition as the outcome that distinguishes the two trajectories.

## downward face vector
- reading: It applies an orienting force: the unready person is torqued into a downward vector, opposite the later seeking of the elevated face.
- mechanism: 
- trace:
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B009: Downward twisting or a face-level thrust supplies an oriented force rather than undirected ease.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B008: Riding or taking before readiness supplies coercive application of that force to an unprepared subject.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into ruin supplies the downward continuation of the focus force.
  - 92:20 **وَجْهِ** و ج ه B001: Face and forward aspect supply the orientation against which a face-level or away-from-face vector can be imagined.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Height and elevation supply the opposed vertical pole that makes the facilitated motion legibly downward.


# Focus 92:11

## non substituting capital
- reading: At irreversible collapse, owned capital cannot spare, replace, or stand in for its owner; the denial concerns substitution, not merely usefulness.
- mechanism: The availing-and-replacing branch of the first focus root is denied to acquired property at the falling-into-ruin branch of the final root. Possessions cannot function as a proxy for the possessor across irreversible collapse.
- trace:
  - 92:11 **يُغْنِى** غ ن ي B002: Sufficing, benefiting, and standing in for another supply the exact function that the focus negates.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Acquired property supplies the stock that is expected, but fails, to serve as substitute.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: A fall into ruin supplies the irreversible threshold at which substitution is exposed as impossible.

## dependency exposed
- reading: The collapse disproves a category error: having wealth never made the owner self-sufficient, even while it made him appear so.
- mechanism: The near-doubling of wealth and independence constructs an attempted identity: the owner treats having property as being without need. Descent reveals that the two are not equivalent, because possession cannot remove the owner's terminal dependence.
- trace:
  - 92:11 **يُغْنِى** غ ن ي B001: Wealth and freedom from need supply the identity the owner implicitly expects property to confer.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated possessions materialize the attempted self-sufficient identity.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Ruin functions as the stress test that uncovers dependence beneath apparent independence.

## habitation outlived
- reading: The owner's settled world survives only as evidence that he once inhabited it; its very staying power shows why it cannot accompany or avail him.
- mechanism: Property stabilizes a household and records that its owner once dwelt there, but it remains spatially fixed when the owner departs. The possessive expression becomes ironic: what was 'his' turns into a surviving habitation-marker that cannot accompany him.
- trace:
  - 92:11 **يُغْنِى** غ ن ي B004: Long dwelling and former habitation turn sufficiency into the stable place a life leaves behind.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Possessions furnish and mark the settled place but remain exterior to the departing owner.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Disappearance toward an unknown direction breaks the link between owner and fixed habitation.

## headlong trajectory
- reading: The owner is already moving headlong; wealth can add means to motion but cannot brake the trajectory when it becomes ruinous.
- mechanism: The focus can stage not only a passive fall but an already accelerated course. Wealth may finance movement, yet it supplies neither steering nor braking and therefore cannot alter the destination of headlong momentum.
- trace:
  - 92:11 **تَرَدَّىٰٓ** ر د ي B002: Rushing, bounding, and heavy gait supply an embodied trajectory rather than a motionless terminal state.
  - 92:11 **يُغْنِى** غ ن ي B002: The denied capacity to avail becomes, functionally, a denied capacity to arrest or redirect the course.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated means can propel activity but do not themselves provide orientation or restraint.

## cover exposure
- reading: Wealth first conceals dependence like a mantle; the fall is also an unveiling in which apparent sufficiency is exposed as non-protective.
- mechanism: The opening alternation between concealment and disclosure activates the mantle branch of the focus descent root. Wealth can operate as a social covering that makes dependence look like sufficiency; collapse is the moment the cover is stripped and its inability to protect becomes visible.
- trace:
  - 92:1 **وَٱلَّيْلِ** ل ي ل B001: Darkness supplies an environment in which underlying condition can remain unseen.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A covering that rises over and hides something supplies the active veil in the mechanism.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: Daylight opening supplies the counter-movement from concealment to inspectability.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Disclosure and emergence make the hidden inadequacy of the covering manifest.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B004: A worn mantle and what clings to the shoulders anchor the covering image directly in the focus clause.
  - 92:11 **يُغْنِى** غ ن ي B002: Denied sufficiency distinguishes an impressive cover from actual protection.

## measured divergent striving
- reading: The fall is the resolution of a directed course: wealth may be what striving accumulated, yet accumulation cannot steer the striver away from the course he made.
- mechanism: Measured formation, purposeful work, and divergent courses recast the focus fall as the terminus of a trajectory rather than an isolated accident. Wealth stores the yield of striving, but stored yield cannot determine the direction in which the striver's course resolves.
- trace:
  - 92:3 **خَلَقَ** خ ل ق B001: Measuring and proportioning supply a designed field within which different courses can be compared.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement toward an objective supplies direction and agency to the trajectory.
  - 92:4 **سَعْيَكُمْ** س ع ي B002: Work, earning, and transaction connect the course to the production of wealth without equating proceeds with direction.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion supplies multiple outcomes and prevents one undifferentiated model of striving.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B002: Bounding motion anchors the contextual courses in the focus body's own movement.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Acquired property becomes the stored residue of work, not a steering mechanism.

## outgoing shield
- reading: Money cannot substitute for its owner as retained stock, but before collapse it can be converted through giving into a protective pattern of action.
- mechanism: Giving, self-protection, enacted truth, beneficence, and opened ease form a conversion chain. Money does not avail as retained stock or substitute, but it can be translated through outward transfer into protective conduct and a newly opened course.
- trace:
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing something over supplies the outward transfer that breaks mere possession.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing oneself within protection supplies the function toward which giving is ordered.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Making a promise true in action prevents assent from remaining an inert claim.
  - 92:6 **وَصَدَّقَ** ص د ق B006: A monetary due or charitable transfer links enacted truth directly to material wealth.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: Doing what is good supplies the qualitative transformation of the transferred asset.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: An opening into ease after difficulty supplies the changed course produced by the conversion.
  - 92:11 **يُغْنِى** غ ن ي B002: Denied availing blocks the shortcut in which retained property itself performs the protective work.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Owned stock is the same material whose function changes only when it enters action.

## withheld independence
- reading: The hoard was never self-sufficiency: withholding enacted a false independence whose terminal non-availing merely makes the contradiction undeniable.
- mechanism: The direct recurrence of the self-sufficiency root after withholding turns the focus into an internal contradiction. The one who withholds because he imagines himself beyond need makes wealth carry a function it cannot perform; terminal non-availing reveals a failure already present in the posture of possession.
- trace:
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding supplies the practical form taken by the claim of independence.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed wealth and freedom from need supply the posture that the focus later tests.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B002: The availing sense turns the claim of independence into an expectation that possessions can suffice for the self.
  - 92:11 **يُغْنِى** غ ن ي B002: The repeated root now negates the very sufficiency claimed earlier.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Possessive wealth identifies the hoard on which the self-sufficiency claim depends.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Ruin is the final disclosure of the hoard's prior inability to abolish need.

## deceptive mantle
- reading: He has wrapped himself in possessions as a status-garment; at the crisis, the garment's promise of independence is revealed as a constricting lie.
- mechanism: A garment that misrepresents its wearer's condition activates the focus mantle branch, while twisting difficulty supplies constriction. Wealth becomes a status-garment that advertises independence but cannot protect the wearer; wrapping oneself in it can even tighten the difficult course.
- trace:
  - 92:9 **وَكَذَّبَ** ك ذ ب B009: A garment whose appearance lies about its condition supplies a concrete model of deceptive exterior display.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Twisting, obstruction, and imposed difficulty turn the apparent covering into constriction rather than shelter.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B004: Putting on a mantle anchors the garment mechanism in the focus verb while remaining a coexisting, form-distant reading.
  - 92:11 **يُغْنِى** غ ن ي B002: Denied sufficiency exposes the difference between looking protected and actually being protected.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Visible possessions supply the wearable social exterior in the analogy.

## guided descent
- reading: Wealth cannot orient or escort the owner along the whole route from beginning to outcome; the terminal fall reveals a prior absence of guidance on a steep course.
- mechanism: The split guidance inventory places gentle direction beside a steep descent, and the following first/later language expands the time horizon. The focus fall becomes a path-condition with an origin, direction, and outcome; wealth has no directional or escorting capacity across that whole arc.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle direction toward a road supplies the positive alternative to uncontrolled descent.
  - 92:12 **لَلْهُدَىٰ** ه د ي B009: The non-dominant mapped inventory contributes a difficult downhill passage, giving the path a steep topography.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: What comes after supplies the far endpoint against which present possessions are tested.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Return to outcome or eventual resolution binds beginning and end into one trajectory.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into a pit or ruin anchors the steep contextual route in the focus event.
  - 92:11 **يُغْنِى** غ ن ي B002: Non-availing means that wealth cannot serve as guide, escort, or replacement across the route.

## race and lateral escape
- reading: He is on a directed, accelerating course; wealth cannot steer or shield him, while turning and being moved aside describe the genuine alternatives to impact.
- mechanism: A runner following another, a turn away, and movement to the side activate the focus's rushing gait. The sequence becomes a race-like spatial system of following, orientation, and lateral removal: wealth cannot change lane or brake, whereas direction determines whether the moving person enters danger or is shifted aside.
- trace:
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B007: The runner immediately behind the leader supplies a sequential course in which position follows prior motion.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning away supplies the decisive reorientation within the moving course.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Being kept apart or moved away supplies lateral escape from the dangerous line.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B011: A shield positioned at the side makes lateral removal protective rather than merely distant.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B002: Rushing and bounding gait anchor the race-like motion in the focus body.
  - 92:11 **يُغْنِى** غ ن ي B002: Denied availing becomes a denied ability of property to steer, shield, or alter position.

## possession to purification
- reading: Wealth fails as a possessed proxy but gains a different, non-proprietary efficacy when given: the asset leaves the owner while the resulting growth or purification returns to the self.
- mechanism: The same wealth root moves from a possessed subject in the focus to the object of an outgoing gift. Growth and purification attach to that release, creating a grammatical and functional reversal: held wealth cannot substitute for the self, while wealth relinquished can participate in changing the self.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving supplies the outgoing verbal force that reverses the focus's possessive relation.
  - 92:18 **مَالَهُۥ** م و ل B001: The repeated wealth root is now transferred rather than retained, making the contrast materially exact.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply a return that occurs in the person rather than in the retained stock.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purification and repair specify the self-transforming quality of that return.
  - 92:11 **مَالُهُۥٓ** م و ل B001: In the focus, the same material is marked as the owner's stock and denied proxy power.
  - 92:11 **يُغْنِى** غ ن ي B002: Non-substitution defines what release does not mean: the asset never becomes a replacement for its owner.

## excess vs growth
- reading: The fall can begin when addition exceeds measure: hoarded increase is sterile surplus, whereas wealth released into giving becomes growth, nurture, and upward maturation.
- mechanism: A rare focus branch for increase beyond measure is separated from contextual images of organic growth, nurture, and elevation. The result is two non-equivalent increases: accumulation can become sterile surplus that precipitates collapse, while released wealth can nourish a rising transformation.
- trace:
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth supplies an internally developing increase rather than mere addition to a stock.
  - 92:20 **رَبِّهِ** ر ب ب B002: Nurture, repair, and completion give the increase a formative process and intended completion.
  - 92:20 **رَبِّهِ** ر ب ب B005: The non-dominant mapped branch adds feeding and development, sharpening the organic alternative to hoarding.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Elevation supplies the upward vector of matured growth.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B005: Increase beyond the proper measure anchors sterile excess directly in the focus's polysemous final root.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated property is the material capable of being mistaken for growth simply because its quantity rises.

## noncompensatory economy
- reading: The verse complex rejects wealth as an equivalence machine: it cannot pay in place of the owner, and even virtuous giving is not a purchase, repayment, or exchange for a commensurate return.
- mechanism: The compensation root repeats the focus's exact logic of one thing standing in for another, but the context denies that the gift is repayment for a prior benefit. This separates two economies: possessed wealth cannot pay in place of the self, and released wealth is not a debt-settlement that purchases an equivalent return.
- trace:
  - 92:19 **نِّعْمَةٍ** ن ع م B001: A benefit or favorable condition supplies the possible prior claim that might demand repayment.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Reciprocal recompense supplies the transaction that the context explicitly excludes from the gift.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B002: One thing standing in for another directly mirrors the proxy function denied to wealth in the focus.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Collecting and discharging debt sharpens the excluded model of moral bookkeeping.
  - 92:11 **يُغْنِى** غ ن ي B002: Sufficing and replacing provide the focus-side proxy logic that compensation echoes.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Property is the tempting payment instrument, but neither ownership nor transfer purchases a substitute self.

## vertical reorientation
- reading: The answer to descent is not a stronger pile of assets but a reoriented act: wealth leaves the self along an upward-directed purpose while the self is formed toward completion.
- mechanism: Seeking, direction, formative completion, and height create a counter-vector to the focus descent. Wealth itself cannot reverse downward motion; what changes the course is the direction toward which wealth is released and the larger formative relation in which that act is placed.
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Active seeking supplies intentional propulsion rather than passive possession.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and orientation supply the axis along which the released wealth now moves.
  - 92:20 **وَجْهِ** و ج ه B004: The face as the self makes orientation relational rather than merely geometric.
  - 92:20 **رَبِّهِ** ر ب ب B002: Formative care, repair, and completion supply the process that can redirect a life rather than merely its assets.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Height supplies the explicit upward counter-vector to falling.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Descent into ruin provides the downward vector that money alone cannot reverse.
  - 92:11 **يُغْنِى** غ ن ي B002: Denied availing prevents the upward turn from being attributed to the asset itself.

## acceptance not satiation
- reading: The sequence distinguishes two kinds of enough: private accumulation cannot abolish dependence, while released wealth opens toward a relational acceptance that possession could never manufacture.
- mechanism: The closing acceptance field revises the meaning of enough. Accumulation seeks self-sufficiency by eliminating need, but the final state is relational acceptance after wealth has been released; satisfaction is received and participated in, not manufactured by possessing more.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B001: Acceptance in contrast to displeasure supplies an affective endpoint different from material satiation.
  - 92:21 **يَرْضَىٰ** ر ض و B003: Mutual satisfaction makes the endpoint relational rather than a solitary abolition of need.
  - 92:21 **يَرْضَىٰ** ر ض و B004: The non-dominant mapped branch adds obedience, love, and guarantee, thickening acceptance into a bond.
  - 92:11 **يُغْنِى** غ ن ي B001: Freedom from need supplies the rival model in which satisfaction is achieved by private abundance.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated property is the attempted means of satiation whose terminal inability the focus exposes.

## spider support
- reading: Possession resembles a self-spun enclosure: intricate and owner-made, yet too fragile to catch its maker when he falls; giving opens rather than reinforces it.
- mechanism: 
- trace:
  - 92:11 **مَالُهُۥٓ** م و ل B002: The rare spider association supplies a fragile, self-produced structure as an analogy for property.
  - 92:18 **مَالَهُۥ** م و ل B002: The repeated association occurs where wealth is released, suggesting an opening of the enclosure.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into ruin tests whether the self-made support can bear the weight of its maker.
  - 92:11 **يُغْنِى** غ ن ي B002: Denied availing marks the fragile structure as incapable of catching or replacing the owner.

## stone in furnace
- reading: The owner and his hard assets enter a furnace-like test as cast stone: apparent solidity offers no insulation and becomes material to be struck, heated, and leveled.
- mechanism: 
- trace:
  - 92:11 **تَرَدَّىٰٓ** ر د ي B001: Throwing, striking, and rock supply the hard material cast into the ordeal.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Acquired assets supply the apparent material solidity whose protective value is tested.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies the surrounding medium of the material test.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure intense flame raises the test from incidental heat to consuming exposure.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B004: Applying fire to level or prepare a thing supplies a transformative material operation.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B009: A stone used for pounding closes the branch-to-branch circuit with the focus rock image.


# Focus 92:12

## assumed orientation
- reading: The speaker emphatically assumes responsibility for making a truth-directed way discernible and traversable.
- mechanism: The guidance branch supplies gentle indication, clarification, and enabling toward a way or truth; the syntax presents that orienting work as an emphatically assumed responsibility.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication and enabling toward a true way supplies the clause's core orienting action and makes عَلَيْنَا sound responsibility-bearing.

## course not map
- reading: Guidance is the directed course and practical bearing of travel, whose orientation the speaker undertakes.
- mechanism: If هُدَىٰ profiles a course and manner of proceeding, the clause concerns governance of trajectory: what is 'upon us' is the directional shape of the movement, not merely delivery of a map.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B002: The course, manner, and intended-direction image turns guidance into the practical bearing of a journey and assigns that bearing to the clause's عَلَيْنَا.

## preceding lead
- reading: What is undertaken is to go ahead as a leading edge, so the traveler follows an already opened line.
- mechanism: Guidance can operate from in front: an advance edge enters the route first and thereby gives following motion its line. The clause then promises precedential presence rather than rearward instruction.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B003: The leading-front image supplies an advance presence whose going-before makes the route followable.

## gracious dispatch
- reading: Guidance is a gracious dispatch whose movement toward the addressee is undertaken at the source.
- mechanism: Guidance becomes a directed transfer rather than a possession held at the source. عَلَيْنَا marks source-side commitment to dispatch the gift; it does not make the recipient a creditor.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B004: The graciously sent gift supplies a source-to-recipient trajectory and recasts guidance as beneficent transmission.

## timed disclosure
- reading: Guidance can hold a stable direction through periods of cover and disclose the way in phases.
- mechanism: Covering, daylight's opening, and disclosure make guidance temporally textured. Direction can remain real while visibility is occluded, then become manifest at the fitting phase; guidance is continuity across changing access, not uninterrupted glare.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle clarification anchors the model in guidance while allowing disclosure to be paced rather than maximal at every moment.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A cover rising over and concealing something supplies the phase in which the route persists without full visibility.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: Daylight opening into illumination supplies expanded perceptual access to the route.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Uncovering and manifestation turn the second phase into active disclosure rather than mere chronological daylight.

## calibrated divergence
- reading: Guidance is a common orienting responsibility capable of addressing differently constituted and diverging strivings.
- mechanism: Measured creation, purposeful movement, and dispersed outcomes recast guidance as calibration across heterogeneous trajectories. One orienting responsibility need not flatten the created differences among those moving.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B002: Course and intended direction anchor guidance as trajectory-management rather than a uniform verbal message.
  - 92:3 **خَلَقَ** خ ل ق B001: Measuring and proportioning a thing supplies differentiation by design rather than accidental variation.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful motion toward an object makes the surrounding diversity a set of directed trajectories.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion supplies the real divergence that an orienting mechanism must address without erasing.

## responsive easing
- reading: Guidance can answer enacted orientation by opening the route and making continued movement along it more tractable.
- mechanism: Giving, self-placement within protection, and enacted verification are followed by an opening after difficulty and tractable movement. Guidance therefore includes responsive enabling: a practiced orientation becomes increasingly traversable.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Guidance as indication plus divine enabling anchors the shift from communicated direction to assisted traversal.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing something over supplies an outward practice that begins to embody the chosen direction.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing oneself within protection supplies deliberate self-positioning, not passive receipt.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Making a promise or claim true in action supplies verification that stabilizes the orientation.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening into ease after difficulty supplies the path-level response to the enacted disposition.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B005: Light, compliant motion makes enabling bodily and kinetic: movement increasingly follows the chosen line.

## channelized descent
- reading: Guidance can truthfully expose the fork and its ends while chosen dispositions become self-reinforcing trajectories, including a frictionless approach to a hard fall.
- mechanism: Withholding, claimed sufficiency, and rejection establish an opposed orientation; easing then means reduced resistance along that chosen line, even as the line bends into hardship and finally a fall. Guidance discloses a bifurcating field without coercively preventing every destructive course.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B002: Course and intended direction anchor the model in the focus word as trajectory rather than guaranteed arrival.
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding supplies the first embodied commitment of the opposed course.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B002: The image of self-sufficing adequacy closes the actor against dependence on further orientation.
  - 92:9 **وَكَذَّبَ** ك ذ ب B002: Assigning falsity to the thing or its bearer makes rejection an active directional judgment.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: Tractable motion explains how an adverse course can become easy to continue without becoming good.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Crooked resistance and complication supply the destination produced by the apparently easy continuation.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into ruin supplies the terminal geometry of the self-reinforcing adverse trajectory.

## temporal stewardship
- reading: Guidance is stewardship of orientation across the full arc from beginning through return and outcome.
- mechanism: The immediately following claim spans beginning, later end, return, and even administration. It grounds the responsibility for direction in command of the whole temporal arc: guidance can orient from origin through outcome rather than intervene at one isolated point.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B002: The intended course anchors guidance as an arc whose beginning and outcome can be jointly governed.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: Laterness after a first point supplies the far end of the temporal span.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Beginning and precedence supply the near end from which the guided course opens.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Return to final outcome folds destination back into the first/latter pair and makes direction teleological.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B003: The non-dominant mapped image of administering an affair adds stewardship to temporal possession.

## warning as guidance
- reading: Guidance may remain gentle in aim while using an unmistakably severe advance signal to expose where a course ends.
- mechanism: Warning awakens caution, fire can be perceived from afar as a visible marker, and pure flame fixes the boundary's consequence. The gentle way-showing of the focus can therefore include an alarming advance disclosure; severity of signal need not cancel beneficence of function.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward truth anchors warning as a way-showing function rather than an independent threat theme.
  - 92:12 **لَلْهُدَىٰ** ه د ي B010: The split-root threatening image pressure-tests the tonal range of guidance and activates its severe warning register.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: A warning that frightens in order to awaken caution supplies the preventive purpose of the severe signal.
  - 92:14 **نَارًا** ن و ر B003: Fire sighted from a distance makes the danger an advance landmark rather than only a later punishment.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure, fiercely kindled flame supplies the real boundary condition that gives the warning urgency.

## orientation and siding
- reading: Guidance can be a bodily reorientation: facing, refusing to face, or being led onto the safe side of a danger.
- mechanism: Turning the face, turning away, being led laterally, and being protected turn abstract direction into bodily orientation. Rejection is an enacted reversal of facing; rescue is a guided displacement to the safe side of danger.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B002: Intended direction anchors the bodily turn and lateral displacement as concrete operations of guidance.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B006: Turning the face toward something supplies the positive bodily geometry of orientation.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning one's back and withdrawing supplies the same geometry reversed by refusal.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B005: Leading something to the side supplies active rerouting away from the dangerous line.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Repelling harm through protection gives the lateral rerouting its preservative function.

## nontransactional gift circuit
- reading: Guidance is an unpriced gift that reorients reception into generative giving without creating a human repayment claim.
- mechanism: The focus gift-image is activated by wealth being given, growth or purification, denial of a compensable prior favor, and desire directed toward a face. Guidance is a non-transactional transmission that redirects its recipient into further giving rather than closing a debt ledger.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B004: A gracious gift sent toward someone supplies the incoming transfer whose effects can continue through the recipient.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving rather than merely arriving makes the recipient's answering movement an intentional outgoing transfer.
  - 92:18 **مَالَهُۥ** م و ل B001: Possessed and accumulated wealth supplies the material that is released rather than retained.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase make giving generative rather than a simple subtraction from a fixed stock.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matching an act with recompense supplies the transactional logic that the surrounding negation suspends.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking makes the gift's downstream movement purposive rather than socially repayable.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and orientation give the seeking a non-human endpoint and turn generosity into reorientation.

## cultivated satisfaction
- reading: Guidance is a cultivated, desire-engaging course whose horizon is elevated relational satisfaction.
- mechanism: Seeking a face, lordly cultivation toward completion, ascent, and eventual satisfaction make guidance developmental and relational. The directed course is not exhausted by compliance; it matures a seeker toward an elevated encounter and acceptance.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B002: Course, bearing, and intended direction anchor the model in a sustained trajectory toward an end.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Active seeking supplies the traveler's desire-driven participation in the course.
  - 92:20 **وَجْهِ** و ج ه B001: The face as what fronts and receives approach gives guidance a relationally encountered terminus.
  - 92:20 **رَبِّهِ** ر ب ب B002: Cultivating, repairing, and bringing to completion supplies the developmental work performed along the route.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Elevation supplies the vertical transformation of the directed and cultivated seeker.
  - 92:21 **يَرْضَىٰ** ر ض و B003: Mutual satisfaction supplies a relational completion more reciprocal than bare arrival.

## supported walker
- reading: Guidance may accompany and partially bear an unstable traveler until movement becomes easier and a fall can be avoided.
- mechanism: 
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B008: Supported, swaying walking turns guidance into accompaniment that bears some of the traveler's weight.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B005: Light and compliant movement supplies the bodily effect of successful support.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: The fall into ruin supplies the kinetic danger against which supportive guidance matters.

## custody of the protected
- reading: For a moment the clause profiles custodial responsibility for the protected traveler whom guidance must lead out of harm's line.
- mechanism: 
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B007: The protected person or captive shifts the object under responsibility from guidance-content to a vulnerable traveler held in custody.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B005: Leading something to the side supplies the custodian's concrete act of removing the vulnerable subject from danger.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Protection that repels harm supplies the purpose of the custodial obligation.

## devotional offering
- reading: The root briefly lets guidance resemble a devotional offering whose directed transfer toward the sacred center is itself a way.
- mechanism: 
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B005: An offering dispatched toward a sacred center supplies a devotional direction in which transfer itself traces the route.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving supplies the concrete act by which possessed material is sent away from the giver.
  - 92:18 **مَالَهُۥ** م و ل B001: Accumulated wealth supplies the material capable of becoming a devoted transfer.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking supplies the intention that directs the transfer beyond ordinary exchange.
  - 92:20 **وَجْهِ** و ج ه B004: The face standing for the self supplies the personal divine terminus of the devotional dispatch.
  - 92:20 **رَبِّهِ** ر ب ب B001: Lordship and sovereignty identify the sacred relation toward which the offering-image is oriented.

## escorted transition
- reading: Guidance can be imagined as an escorted transition into a transformed relation, with the guide responsible for the passage.
- mechanism: 
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B006: The bride being led supplies an escorted passage from one social state into a new bond.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: The male member of the created pair supplies the relational polarity that makes the transition image legible.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The female member of the created pair keeps the branch activation tied to the packet's own paired social imagery.
  - 92:20 **وَجْهِ** و ج ه B003: Face-to-face encounter supplies the relational arrival toward which escorted transition can move.
  - 92:21 **يَرْضَىٰ** ر ض و B003: Mutual satisfaction supplies a relationally completed state rather than mere arrival at a location.

## split root collapse
- reading: The split root briefly recasts guidance as responsibility to expose a treacherous descent and the collapse hidden in its load-bearing structure.
- mechanism: 
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Severe breaking and collapse make guidance load-bearing: it must reveal or dismantle the support whose failure would ruin the traveler.
  - 92:12 **لَلْهُدَىٰ** ه د ي B009: A difficult descent gives the guided way a hazardous gradient rather than a neutral surface.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into ruin activates the split-root descent and collapse images immediately before the focus claim.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: Caution-awakening warning supplies the preventive response to a route whose structure can fail.


# Focus 92:13

## temporal merism
- reading: The reversed first/later endpoints claim every temporal position between origin and aftermath within one undivided possession.
- mechanism: Later-than-first and beginning/precedence form an endpoint pair. Their reversed order prevents the first term from controlling the sequence and turns the pair into a merism for the whole temporal field under one possession.
- trace:
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: Its later-or-other-than-first image supplies the terminal pole and opens the span beyond a single named realm.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Its beginning-and-precedence image supplies the initial pole, completing an all-time merism.

## defer return loop
- reading: What is deferred and what it finally returns or resolves into are both held; futurity is a governed return rather than an external territory.
- mechanism: A deferred phase is paired with a branch in which a thing returns, becomes, or reaches its outcome. The lexical order can therefore be carried as a loop from delay to eventual return, not only as two static epochs.
- trace:
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B002: Its postponement-to-a-later-time image makes the first pole an interval of deferral.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Its return-to-outcome image converts the other pole into arrival at a resulting meaning or end.

## rightful charge
- reading: The verse also asserts the rightful charge to order, sustain, and adjudicate both the first and later phases.
- mechanism: Possession is thickened into jurisdiction: setting affairs right, taking charge, and having the superior claim explain what it means for both temporal poles to be 'ours.' This coexists with, rather than replaces, the temporal merism.
- trace:
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: Its later-than-first image fixes the farther phase over which charge extends.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B004: Its governing-and-repairing image turns bare title into active ordering of affairs.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B003: Its assuming-charge image supplies custodial authority to the possessive construction.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B008: Its priority-and-superior-right image makes the claim one of rightful entitlement, not merely control.

## covered and disclosed time
- reading: They are also alternating regimes of hiddenness and manifestation, so invisibility does not mark anything as outside the stated possession.
- mechanism: Covering and disclosure recode temporal distance as visibility. The later pole can be absent or screened, while a branch of the first pole is a visible outline; both the hidden future and manifest edge remain within the same possessive field.
- trace:
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: Its later-or-absent image supplies the temporally distant pole that can be experienced as hidden.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B006: Its visible-outline image supplies the manifest edge opposed to temporal absence.
  - 92:1 **يَغْشَىٰ** غ ش و B001: Its covering layer supplies the operation that renders a phase present but unseen.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Its uncovering-and-appearing image supplies the reverse operation by which an occluded phase becomes manifest.

## divergent routes under management
- reading: The claim includes administration of path-dependence itself: divergent striving is progressively routed without being collapsed into one outcome.
- mechanism: Divergent striving is followed by the same making-easy formula for opposed destinations. Against the focus inventory of governance and charge, ownership becomes route-management: chosen vectors remain distinct, yet each is made increasingly traversable within one jurisdiction.
- trace:
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B004: Its ordering-and-repairing image supplies active management rather than inert possession.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B003: Its taking-charge image makes both trajectories answerable to one administration.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Its purposeful-motion image supplies agents moving toward sought ends.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Its dispersion image splits the motion into genuinely different vectors.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Its opening into ease after difficulty supplies positive route-conditioning toward the easy destination.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B001: The same opening-into-ease image, now governing the hard destination, makes tractability distinct from desirability.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Its twisting-and-complication image preserves the adverse character of the destination even as its route becomes easy to follow.

## failed private title and guidance duty
- reading: It contrasts failing private property with custodial sovereignty: the one whose title spans both phases also assumes the work of indicating their paths.
- mechanism: The failure of 'his wealth' at the fall is followed by guidance being 'upon us' and both temporal poles being 'ours.' The pronoun sequence makes private title fail exactly where divine title appears, while the prepositional shift from burden to possession frames sovereignty as carrying a directional duty.
- trace:
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B004: Its governance-and-repair image gives the possessive claim an administrative content.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B003: Its assuming-charge image connects title to responsibility for the affair.
  - 92:11 **يُغْنِى** غ ن ي B002: Its sufficiency image supplies the human claim that is explicitly shown unable to suffice.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Its accumulation-of-wealth image supplies the private holding contrasted with the focus's comprehensive title.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Its fall-into-destruction image supplies the threshold where accumulated property loses protective force.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Its gentle indication toward path and truth supplies the operative content of what is assumed 'upon us.'

## temporal axis as orientation
- reading: They can also mark where one is oriented within a governed field of approach, withdrawal, contact, and protective distance.
- mechanism: Fire-contact, turning away, lateral removal, and protection convert the first/later axis into a geometry of approach and withdrawal. The non-dominant focus mapping to adjacency and facing keeps this model anchored while the later context occurrence of و ل ي makes the latent orientation audible.
- trace:
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B003: Its rearward image spatializes the later pole as a position behind.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Its adjacency-without-gap image turns the other pole into regulated proximity.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B006: Its turning-toward image supplies a directional front to the focus pair.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Its meeting-the-fire-and-heat image establishes dangerous contact as one endpoint of the geometry.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Its turning-away image supplies an agentive reversal of orientation.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Its removal-to-the-side image supplies protective displacement from the contact zone.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Its warding-off-harm image gives the lateral displacement its protective function.

## nonreciprocal gift economy
- reading: Because both present holding and later return fall within one title, giving can cease to be repayment or purchase and become a reorientation of entrusted wealth.
- mechanism: Giving wealth for growth, negating a repayable favor, seeking a higher face, and awaiting satisfaction reorganize possession into a non-bilateral economy. If first and later already share one ultimate title, a human transfer need not purchase a human counter-transfer; its vector can pass through divine ownership toward deferred contentment.
- trace:
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B002: Its deferral image supplies the interval between present relinquishment and later satisfaction.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B013: Its granting-or-assigning image recasts first-phase holdings as allocations rather than absolute private title.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B014: Its transfer-at-known-cost image supplies a transactional ledger that the following negated repayment will interrupt.
  - 92:18 **يُؤْتِى** ء ت ي B002: Its giving image supplies the outward transfer that begins the mechanism.
  - 92:18 **مَالَهُۥ** م و ل B001: Its accumulated-wealth image identifies what is relinquished from apparent private possession.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Its growth-and-increase image makes relinquishment productive rather than merely subtractive.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: Its benefaction image supplies the possible human favor whose creditor claim is denied.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Its debt-collection-and-settlement image supplies the bilateral account from which the gift is released.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Its seeking image redirects the transfer toward a non-human objective.
  - 92:20 **وَجْهِ** و ج ه B002: Its direction-and-destination image supplies the gift's reoriented vector.
  - 92:20 **رَبِّهِ** ر ب ب B001: Its lordship-and-ownership image identifies the comprehensive title through which the transfer is reclassified.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Its satisfaction-versus-displeasure image supplies the deferred non-monetary arrival of the sequence.

## rear runner and first rank
- reading: It also levels competitive rank: both the leader and the one following behind remain inside the same ultimate claim.
- mechanism: 
- trace:
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B003: Its rearward image supplies the position of the one behind.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Its precedence image supplies the first-ranked position.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B008: Its priority-and-superior-right image intensifies firstness as rank rather than only time.
  - 92:4 **سَعْيَكُمْ** س ع ي B008: Its rivalry-in-striving image supplies a competitive course on which positions separate.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B007: Its runner-following-the-leader image links the rear position directly to a first-ranked predecessor.

## successive rains and growth
- reading: As a contained ecological analogy, they become successive provisions whose delayed arrival nourishes growth without leaving the provider's domain.
- mechanism: 
- trace:
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B002: Its deferred-later image supplies the interval before the following provision arrives.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B010: Its late-rain-following-an-earlier-rain image materializes succession as a seasonal second arrival.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Its growth-and-increase image supplies the living result of successive provision.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B006: Its heavy-rain image supplies the material intensity of provision.
  - 92:20 **رَبِّهِ** ر ب ب B008: Its cloud image supplies the carrier from which the rain sequence descends.


# Focus 92:14

## announced blaze
- reading: An alarm deliberately makes an actively intensifying blaze present to the hearers so that caution can begin before contact.
- mechanism: A speech act discloses a feared object in order to awaken caution; the object is burning fire intensified as a self-flaring, pure blaze.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: Warning that awakens fear and caution supplies both the speech act and its intended vigilance.
  - 92:14 **نَارًا** ن و ر B002: Burning, flickering fire supplies the concrete danger announced by the warning.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure flame flaring and kindling turns the warned-of object into an ongoing event.

## distant beacon
- reading: The warning functions as advance sight: a remote blaze becomes a present negative beacon before the addressees arrive.
- mechanism: The verbal warning and the visible fire duplicate one another as distance-crossing signals: speech lets the addressees see in advance what the blazing landmark would otherwise reveal only on approach.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: The warning carries knowledge of danger across distance before the hearers reach it.
  - 92:14 **نَارًا** ن و ر B003: Sighting fire from afar supplies the anticipatory visual geometry of the warning.
  - 92:14 **نَارًا** ن و ر B005: A conspicuous beacon or boundary marker makes the fire a negative landmark.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: The pure active flame is what keeps the distant landmark perceptible and urgent.

## recoil signal
- reading: The warning is a motion-producing signal intended to turn the addressed group away before the blaze is encountered.
- mechanism: The utterance seeks a bodily as well as cognitive response. Its successful effect is not merely believing that fire exists but recoiling from the route toward it.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: Fear-awakening warning initiates the desired response to danger.
  - 92:14 **نَارًا** ن و ر B006: Aversion, flight, and lack of steadiness supply recoil as the warning's functional target.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: The fiercely flaring flame supplies the pressure that makes recoil intelligible.

## affective conflagration
- reading: The blaze may simultaneously stage concentrated hostility or anger, without displacing the literal fire.
- mechanism: Alongside literal combustion, the fire can register as social or affective heat: antagonism becomes an agent-like blaze directed toward a collective.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: The warning establishes a speaker-to-group relation in which hostile heat can be announced.
  - 92:14 **نَارًا** ن و ر B007: Enmity flaring between groups supplies a social analogue for the fire.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B003: Burning with intense anger supplies an affective personification of the active blaze.

## beacon uncovered
- reading: The wider sequence makes warning itself an act of unveiling: it carries a hidden future danger across darkness into present visibility.
- mechanism: The opening alternation of darkness covering and day opening into disclosure recruits the focus fire into a concealment/revelation system. The warning is an unveiling act, and the blaze is the visible fact that defeats cover.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: The warning performs disclosure early enough to awaken caution.
  - 92:14 **نَارًا** ن و ر B005: The beacon image makes fire the conspicuous landmark revealed by the warning.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Flaring pure flame supplies the self-displaying phenomenon that resists concealment.
  - 92:1 **وَٱلَّيْلِ** ل ي ل B001: Night and its darkness establish the perceptual field in which a warning-beacon matters.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A covering that rises over and hides something supplies the obstacle overcome by disclosure.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: Day opening through light supplies the counter-movement from occlusion to visibility.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Uncovering and appearance make explicit the revelatory function assigned to the warning.

## divergent paths common boundary
- reading: One negative landmark is announced to people on genuinely divergent, purpose-driven routes; common danger does not erase the plurality of their striving.
- mechanism: Measured differentiation followed by purpose-driven yet scattered striving changes the plural كُمْ. The hearers need not be one homogeneous mass: one blazing landmark can bound many differently directed paths.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: A single warning reaches the internally diverse plural addressees.
  - 92:14 **نَارًا** ن و ر B005: The visible landmark supplies a common boundary for otherwise divergent routes.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: The singular active blaze supplies the shared terminal danger.
  - 92:3 **خَلَقَ** خ ل ق B001: Measuring and proportioning make difference patterned rather than accidental.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement toward an object supplies trajectories, not merely static moral types.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion and scattering separate those trajectories while leaving the warning common to them.

## warning inside feedback fork
- reading: The warning enters a dynamic fork before conduct becomes self-easing: it tries to provoke protective recoil while another trajectory is still reversible.
- mechanism: The mirrored behavioral bundles and mirrored facilitation formulas turn the warning from a static verdict into an intervention at a feedback fork. Giving, self-guarding, and enacted truth open a path; withholding, self-exemption, and denial coil into difficulty. The warning seeks recoil before either route becomes easy to continue.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: The caution-awakening speech act functions as an interruptible choice point rather than post hoc notice.
  - 92:14 **نَارًا** ن و ر B006: Aversion and flight supply the behavioral correction the warning attempts to produce.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: The intensifying blaze supplies the endpoint made progressively harder to evade.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing something over begins the outward-moving behavioral bundle.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing oneself within protection makes guarding an enacted route rather than a label.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Realizing a promise in action supplies behavioral confirmation rather than merely verbal assent.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening and ease after difficulty supply the positive track's increasing traversability.
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding reverses the outward transfer and begins the opposed behavioral bundle.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed self-sufficiency closes the person against dependence and warning.
  - 92:9 **وَكَذَّبَ** ك ذ ب B001: Contradiction of truth blocks the alarm's informational route.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Twisting, opposition, and imposed difficulty supply the negative track's obstructive shape.

## fall toward visible blaze
- reading: The warning is a map of descent: it makes visible now the active blaze toward which unsupported falling tends.
- mechanism: Failed sufficiency removes the imagined support beneath wealth, and تَرَدَّىٰ supplies a downward terminal movement. The focus warning then acts like advance topography: it shows the blaze at the end of a fall before the fall occurs.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: Advance warning maps the danger before the addressee enters the terminal movement.
  - 92:14 **نَارًا** ن و ر B003: Fire sighted from afar makes the destination perceptible in advance.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: The active blaze supplies a terminal hazard rather than an inert place.
  - 92:11 **يُغْنِى** غ ن ي B002: Sufficiency and adequacy are explicitly negated as supports at the decisive moment.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated wealth supplies the failed material support.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into destruction supplies the downward trajectory whose endpoint the warning reveals.

## warning as route guidance
- reading: The warning itself guides by placing a blazing negative landmark on the hearers' map.
- mechanism: The explicit claim of guidance immediately before the focus changes warning from guidance's harsh opposite into one of its instruments. The blaze is a negative road-sign: knowing where not to go is itself direction.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: Fear-awakening notice becomes the route-correcting mode taken by guidance.
  - 92:14 **نَارًا** ن و ر B005: A beacon and road landmark let the warned-of fire mark a direction to avoid.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward road and truth supplies the governing guidance function.
  - 92:12 **لَلْهُدَىٰ** ه د ي B002: Direction, course, and intended bearing make the fire-sign operational within a route.

## temporal telescope
- reading: The warning makes the later blaze perceptually first: remoteness in time no longer protects the hearer from present knowledge.
- mechanism: Ownership of the later and the first collapses the hearers' temporal escape routes. A delayed outcome can be brought into the first present moment of warning; sighting fire from afar becomes temporal as well as spatial.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: Advance warning transfers knowledge from a feared later event into the present.
  - 92:14 **نَارًا** ن و ر B003: Sighting fire from afar supplies the model for perceiving an outcome before arrival.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: The presently active verbal blaze makes the remote outcome grammatically immediate.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B002: Deferral to a later time supplies the temporal distance traversed by warning.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Return to a thing's outcome links beginning, present course, and eventual end.

## selective contact geometry
- reading: The warning is universal but contact is selective; the decisive contrast is not hearing versus silence but misdirected turning versus protective distance.
- mechanism: The universal plural warning is followed by exclusive contact, denial and turning away, then being put to the side under protection. This supplies a geometry of orientation: the alarm should cause recoil from the fire, but turning away from the alarm misdirects that recoil; successful guarding appears as enforced distance from the blaze.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: The warning is universally delivered to awaken caution before selective contact is described.
  - 92:14 **نَارًا** ن و ر B006: Recoil and flight supply the intended direction of response to the announced fire.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: The active pure flame remains the fixed danger around which distances are organized.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Meeting fire and its heat defines the prohibited contact relation.
  - 92:16 **كَذَّبَ** ك ذ ب B002: Assigning the message to falsehood blocks the warning's capacity to redirect movement.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning the back and withdrawing supplies the crucial but misoriented motion.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Being distanced and kept apart supplies the successful spatial outcome.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Ward against harm explains why separation from the fire is protective rather than accidental.

## competing transformations
- reading: The blaze becomes one mode of transformation set against another: consuming and marking heat versus giving that purifies and grows the giver.
- mechanism: The later sequence couples transfer of wealth with reflexive growth and purification. Against it, the focus supplies fire that consumes, marks, and intensifies. The two sequences become competing transformations: closed possession tends toward destructive exposure, while release of possession changes and enlarges the giver.
- trace:
  - 92:14 **نَارًا** ن و ر B002: Burning fire and its capacity to brand supply the destructive, marking transformation.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Self-intensifying pure flame gives the destructive process active continuity.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving and transfer initiate the opposed generative transformation.
  - 92:18 **مَالَهُۥ** م و ل B001: Accumulated wealth supplies the material released rather than retained as failed security.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase make giving productive rather than merely subtractive.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purity and rectification give the transformation an ethical and internal dimension.

## nonreciprocal ledger
- reading: It also sounds like notice of an account that no human favor, repayment, or ordinary compensation can discharge.
- mechanism: Focus branches activate warning as binding liability or wound-compensation and fire as a brand. The later negation of any person's favor being repaid, followed by exclusive seeking of the sovereign's face, changes that liability image: ordinary interpersonal exchange cannot settle the announced account.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B002: Binding oneself to an otherwise non-obligatory undertaking supplies an obligation register.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B003: Compensation legally due for a wound supplies the announced-liability image.
  - 92:14 **نَارًا** ن و ر B002: Fire used for branding supplies a visible sanction or settled mark.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive negation removes every human creditor from the motive structure.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: Benefit and good condition supply the favor that could otherwise create reciprocal debt.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Answering an act with its recompense supplies the ordinary reciprocal ledger being negated.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Collecting and fully satisfying a debt sharpens the settlement mechanism.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking redirects motive away from repayment toward a chosen end.
  - 92:20 **وَجْهِ** و ج ه B004: Face as the self or essence supplies the non-human endpoint of the redirected account.
  - 92:20 **رَبِّهِ** ر ب ب B001: Sovereignty and ownership relocate the ultimate claim beyond interpersonal exchange.

## opposed bearings
- reading: It is one pole in an orientational field: warning marks the bearing to refuse, while seeking the highest face supplies the positive bearing.
- mechanism: Seeking, face/direction, sovereignty, and above form an upward intentional vector. The focus fire-beacon becomes its negative counterpart: the warning gives one bearing to avoid while the later phrase gives the bearing actively sought.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: The warning communicates a negative bearing early enough for reorientation.
  - 92:14 **نَارًا** ن و ر B005: A beacon or boundary marker makes the fire the visible direction not to follow.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: The active blaze keeps the negative landmark dynamically salient.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Active seeking supplies intentional movement toward the opposed goal.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and orientation turn motive into a bearing.
  - 92:20 **رَبِّهِ** ر ب ب B001: Sovereignty identifies the personal goal governing that bearing.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B005: The upper direction gives the sought vector a vertical dimension.

## affective heat to satisfaction
- reading: The closing satisfaction gives that heat a coexisting affective opposite: the sequence can move from flaring antagonism toward settled acceptance without making them the same agent's emotion.
- mechanism: The closing satisfaction stands opposite the focus branches of flaring enmity and burning anger. This does not identify one subject for both states; it activates an affective spectrum in which blazing hostility and settled acceptance are rival terminal climates.
- trace:
  - 92:14 **نَارًا** ن و ر B007: Enmity flaring among people supplies the social heat at one end of the spectrum.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B003: A person burning with anger supplies an affective reading of the active blaze.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Satisfaction as the opposite of displeasure supplies the cool, settled counter-state.

## guidance threat split
- reading: As a contained split-root echo, the warning can be heard as guidance's threatening edge: the route is disclosed partly by showing its catastrophe.
- mechanism: 
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: The explicit fear-awakening warning anchors the split-root threat echo in the focus.
  - 92:14 **نَارًا** ن و ر B005: The beacon image keeps the outlier tied to route-guidance rather than free-floating menace.
  - 92:12 **لَلْهُدَىٰ** ه د ي B010: The non-dominant mapped branch of threat and warning lets guidance cast a severe cautionary shadow.

## compensation brand
- reading: It resembles formal notice of a liability whose fiery sanction leaves a visible mark.
- mechanism: 
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B003: Compensation owed for a wound supplies the image of formally incurred liability.
  - 92:14 **نَارًا** ن و ر B002: Branding by burning fire turns liability into an embodied and publicly legible mark.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: The pure blazing flame supplies the material force that makes the mark consequential.

## destructive bloom
- reading: As a contained material analogy, the fire can 'flower' into destructive visibility, opposed by the nourished growth activated through giving and purification.
- mechanism: 
- trace:
  - 92:14 **نَارًا** ن و ر B004: Tree blossom and bloom supply the shape of an unfolding, outward-opening fire.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure flaring flame converts bloom into a destructive rather than fertile unfolding.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase provide the living counter-process to the flame's destructive flowering.
  - 92:20 **رَبِّهِ** ر ب ب B005: The non-dominant nourishment and development branch extends the contrast between cultivated growth and consuming bloom.


# Focus 92:15

## fire contact identity
- reading: The exclusivity clause identifies extreme wretchedness by the direct ordeal of meeting and enduring the feminine object as consuming heat.
- mechanism: The heat-encounter branches of the split ṣ-l-y mapping combine with both experiential hardship and wretchedness in the split sh-q-w mapping. The clause therefore identifies an extreme condition through exclusive, endured contact, not merely by attaching a moral adjective to an otherwise unspecified person.
- trace:
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Direct exposure to fire or heat supplies the event undergone by the exclusive subject.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B001: The non-dominant split target independently preserves meeting, enduring, or being cast into heat.
  - 92:15 **ٱلْأَشْقَى** ش ق و B002: Difficulty, fatigue, and strenuous endurance make the superlative an experienced extremity.
  - 92:15 **ٱلْأَشْقَى** ش ق و B001: Wretchedness opposed to happiness supplies the subject's affective and existential pole.

## heat straightening
- reading: The heat can also be carried as an ordeal that works upon its subject, painfully straightening or remaking what would not otherwise yield.
- mechanism: A fire-use branch does more than burn: heat can roast or straighten a resistant object. Combined with the hardship branch of sh-q-w, this permits a process reading in which contact is a coercive remaking under heat rather than only arrival at a location.
- trace:
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B004: Kindling and turning an object over fire to straighten it supply a material transformation process.
  - 92:15 **ٱلْأَشْقَى** ش ق و B002: Hardship and toil make that heated transformation coercive and painful.

## extremal struggle
- reading: The most wretched can be heard as the extremal outcome of a contest or sustained struggle that culminates in exposure.
- mechanism: The sh-q-w inventories include mutual grappling and prevailing in a hardship contest. Joined to the ṣ-l-y fire encounter, that branch turns the subject from a static type into the terminal participant of a struggle whose finishing condition is exposure.
- trace:
  - 92:15 **ٱلْأَشْقَى** ش ق و B003: A contest of hardship and its prevailing party supply a relational field for the superlative.
  - 92:15 **ٱلْأَشْقَى** ش ق و B003: Mutual endurance, handling, and overcoming make wretchedness an outcome of sustained grappling.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: The heat encounter supplies the struggle's terminal exposure.

## cover reveal exposure
- reading: The subject is the one left fully exposed to heat when concealment gives way to disclosure.
- mechanism: The opening alternation between a cover laid over things and their disclosure recasts ṣ-l-y as exposure after concealment. The most wretched is not only one who reaches heat, but one left uncovered to it when the cycle turns from veiling to manifestation.
- trace:
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Meeting heat supplies the focus event whose degree of exposure is being revised.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A covering that rises over and conceals an object supplies the initial protected or obscured state.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Uncovering and appearance reverse the cover and make direct exposure possible.

## divergent striving endpoint
- reading: The most wretched is the furthest endpoint within divergent courses of striving, a condition reached or made visible through movement.
- mechanism: Measured formation is followed by purposeful movement that disperses into separated courses. This sequence activates the process latent in the focus superlative: al-ashqā becomes an extremal endpoint produced or disclosed among divergent strivings, not an unexplained essence.
- trace:
  - 92:15 **ٱلْأَشْقَى** ش ق و B002: Hardship as sustained practice gives the focus superlative a process that can intensify over a course.
  - 92:3 **خَلَقَ** خ ل ق B001: Measuring and proportioning supply formed differentiation without requiring moral fixity.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful motion toward a sought end supplies trajectory rather than static classification.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion and separation split the trajectories into genuinely different courses.

## facilitated path dependence
- reading: The focus is the terminal phase of a self-reinforcing course: denial is made progressively easier until hardship and heat become the path's fluent destination.
- mechanism: The paired biographies are each followed by facilitation, even when the goal is hardship. Ease here functions as reduced resistance along a chosen course: withholding, claimed self-sufficiency, and denial become a momentum that smoothly conducts the subject toward the arduous condition named in al-ashqā and finally toward heat-contact.
- trace:
  - 92:15 **ٱلْأَشْقَى** ش ق و B002: Hardship and toil connect the focus superlative to the difficult destination of the negative course.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening and ease after obstruction establish facilitation as a path-making operation.
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding supplies the initiating contraction of the negative trajectory.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed independence supplies the self-sealing premise that removes felt need for another course.
  - 92:9 **وَكَذَّبَ** ك ذ ب B002: Assigning falsehood to the good closes the course epistemically as well as materially.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: Lightness and compliance in motion supply the paradoxical smoothness of movement toward difficulty.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Twisting, opposition, and imposed difficulty make the destination a condition that compounds resistance.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B001: Enduring or being cast into heat supplies the terminal event of the facilitated negative course.

## fall into contact
- reading: The subject collapses into the heat-contact after the support expected from accumulated wealth fails.
- mechanism: Claimed sufficiency is tested at the moment accumulated wealth cannot substitute for the person, and the person falls toward ruin. Sequentially, that collapse supplies motion into the focus heat encounter: ṣ-l-y becomes the receiving endpoint of a downward failure rather than an isolated later scene.
- trace:
  - 92:11 **يُغْنِى** غ ن ي B002: Sufficiency and adequacy establish the function that wealth is said to fail.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated possession supplies the support that proves unable to arrest the movement.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into ruin supplies a downward transition toward an endpoint.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Direct heat-contact receives the falling trajectory as its terminal condition.

## guided whole span
- reading: The exception marks the adverse endpoint of a fully spanned course for which direction was made available.
- mechanism: Gentle indication toward a way is asserted before both the later and the first are enclosed in one ownership claim. The focus exception is therefore read inside an available route and a complete temporal span: the final exposure is not an arbitrary gate but an endpoint after direction has been supplied.
- trace:
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward a road or truth supplies an available directional alternative.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: Laterness after a first point supplies the far temporal endpoint.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Beginning and precedence supply the near temporal endpoint, enclosing the whole course with laterness.
  - 92:15 **ٱلْأَشْقَى** ش ق و B001: The wretched pole marks the adverse endpoint reached within that guided span.

## blazing antecedent resolution
- reading: The object is the immediately warned blazing fire, and yaṣlāhā is direct entry into or endurance of its heat; the other branches survive only as echoes.
- mechanism: Warning raises vigilance, an explicitly kindled fire is introduced, and its flame is described as pure and intensely burning immediately before yaṣlāhā. This resolves the feminine object pronoun backward and sharply selects the fire-contact branch while leaving the focus-only alternatives as subordinate resonances.
- trace:
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: A fear-arousing warning supplies anticipatory orientation toward a specified danger.
  - 92:14 **نَارًا** ن و ر B002: A kindled fire supplies the feminine antecedent and the material source of heat.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure, intensely kindled flame specifies the fire's active consuming condition.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Entering, suffering, or directly meeting heat realizes the warned object's effect on the focus subject.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B001: The parallel split target confirms combustion and endured heat as the selected event family.

## denial turning definition
- reading: The most wretched is one who repeatedly makes the good false and reorients away from it, thereby enacting the path into exposure.
- mechanism: The following relative clause gives the extreme subject an operational profile: he assigns falsehood and turns his face away. Wretchedness is thus enacted as a coupled epistemic and directional refusal, and fire-contact is the consequence of sustained orientation rather than an opaque personal essence.
- trace:
  - 92:15 **ٱلْأَشْقَى** ش ق و B001: The opposed-to-happiness state supplies the focus category that the following actions specify.
  - 92:16 **كَذَّبَ** ك ذ ب B002: Attributing falsehood supplies the active epistemic refusal.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning away supplies the bodily and directional completion of that refusal.

## boundary sorting
- reading: The focus is the exposed side of a sorting boundary: one trajectory is admitted into contact while the guarded trajectory is actively conducted aside.
- mechanism: The same feminine object is met by one superlative and actively kept to the side of another. Avoidance is not mere absence: lateral displacement and protective shielding form the inverse operation of ṣ-l-y. The focus becomes one side of a boundary mechanism that routes trajectories into contact or away from it.
- trace:
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Direct heat-contact supplies the inward or exposed side of the boundary.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Removal, separation, and keeping apart supply active displacement to the safe side.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B005: Leading something toward the side gives the avoidance a directed spatial operation.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Repelling harm by a protection supplies the functional reason for lateral removal.

## unreciprocated release from snare
- reading: The focus can carry a contained systemic-capture reading: the most wretched is caught in a closed circuit of possession and return, while gift without debt opens the circuit.
- mechanism: The positive subject releases accumulated wealth for purification, disclaims any human favor awaiting repayment, and seeks another direction. That sequence activates the focus root's snare branch: the negative course can be modeled as capture inside a self-sealing economy of possession and return, while unreciprocated giving breaks the loop and turns elsewhere.
- trace:
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B005: A set snare supplies the focus-anchored image of capture in a mechanism that closes around its subject.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving transfers possession outward and supplies the loop-breaking act.
  - 92:18 **مَالَهُۥ** م و ل B001: Accumulated wealth supplies the material that can be hoarded inside or released from the circuit.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purity and rectification make release transformative rather than merely subtractive.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive negation removes every human claimant from the exchange relation.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Collecting and settling a debt supplies the reciprocal obligation explicitly denied by the construction.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking supplies a positive motive and target beyond repayment.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and orientation turn the released actor out of the closed human circuit.

## two modes of transformation
- reading: The focus heat is the coercive counterpart to voluntary purification and growth: refusal ends in being worked upon by heat, while release permits nurtured completion.
- mechanism: The baseline heat-straightening image is answered by voluntary purification and nurturing completion on the protected course. This produces two coexisting modes of change: release of wealth permits growth and rectification, whereas refusal culminates in a coercive encounter with heat that works upon what would not yield.
- trace:
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B004: Heating and straightening a resistant object supply coercive material transformation.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply an internally fruitful mode of transformation.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purification and rectification make the positive change ethical as well as generative.
  - 92:20 **رَبِّهِ** ر ب ب B002: Nurture, repair, and completion supply an agentive process that brings voluntary purification to maturity.

## satisfaction polarity
- reading: Al-ashqā names the negative affective terminus of a whole course, opposed not merely to safety but to eventual acceptance and settled satisfaction.
- mechanism: The final movement into acceptance and absence of displeasure answers the focus branch that defines wretchedness against happiness. The focus is therefore not only thermal pain; it is one affective endpoint of the surah's trajectory, opposed to a future condition in which striving comes to rest in satisfaction.
- trace:
  - 92:15 **ٱلْأَشْقَى** ش ق و B001: Wretchedness as the contrary of happiness supplies the negative affective endpoint.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Satisfaction contrary to displeasure supplies the answering positive endpoint.
  - 92:21 **يَرْضَىٰ** ر ض و B001: The non-dominant split target adds acceptance to the positive pole, sharpening the contrast with wretchedness.

## race pursuit echo
- reading: A contained kinetic echo appears: the subject has tailed a leading course so closely that continued following carries him into the terminal heat.
- mechanism: 
- trace:
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B007: The racer immediately behind the leader supplies close following as a latent motion pattern.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B006: The parallel split target confirms second-place pursuit close to the leader's rear.
  - 92:15 **ٱلْأَشْقَى** ش ق و B003: Prevailing and being measured within a hardship contest supply the competitive field.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B002: One thing following another extends the race image into the immediately subsequent directional action.

## difficult passage body echo
- reading: At the level of contained body imagery, the event also echoes an arduous passage through constriction, with the subject painfully worked through a threshold.
- mechanism: 
- trace:
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B006: The back-and-haunch region, including what opens and receives in birth, supplies a bodily passage image inside the focus root.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B005: The parallel split target preserves the same anatomy and birth-related opening.
  - 92:15 **ٱلْأَشْقَى** ش ق و B002: Difficulty, toil, and undergoing a matter make the passage arduous.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B006: Obstructed or difficult birth reactivates the focus anatomy as a constricted transition.
  - 92:20 **وَجْهِ** و ج ه B010: Hands-first birth adds orientation and emergence to the bodily passage mechanism.

## mercy countercurrent
- reading: The combustion reading remains dominant, but a mercy countercurrent makes the exclusion tragic and ironic: the most wretched is precisely where blessing, forgiveness, or merciful address is most urgently lacking.
- mechanism: 
- trace:
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B002: Supplication, blessing, and mercy supply a beneficent semantic current under the fire-selected verb.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B002: The split counterpart independently preserves prayer, praise, forgiveness, and purification.
  - 92:12 **لَلْهُدَىٰ** ه د ي B004: A gift sent with affection keeps benevolent outreach active before the warning.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Satisfaction rather than displeasure supplies the positive endpoint against which the mercy countercurrent is felt.


# Focus 92:16

## verdict withdrawal
- reading: The clause depicts one coupled refusal: he invalidates what addresses him and then embodies that judgment by withdrawing.
- mechanism: Declaring the claim or its bearer false licenses withdrawal from attention and compliance; the second verb enacts the first rather than merely adding another fault.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B002: Attribution of falsehood supplies the verbal verdict that licenses disengagement.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Averting and retreating make the verdict operative as refusal of attention or compliance.

## failed charge
- reading: Denial can also be a failed performance: he makes his own charge or undertaking false by abandoning it.
- mechanism: The person proves an entrusted undertaking false by not carrying it through; withdrawal can therefore be read as abdication from a charge, not only departure from a proposition.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B004: A charge that fails because it is not carried through supplies the performative sense of falsification.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B003: Assuming management or charge keeps live the responsibility from which the subject can defect.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Withdrawal supplies the act by which the charge is left unfulfilled.

## counter orientation
- reading: He performs a counter-reality and reorients himself: away from the address, but implicitly toward another face, object, or allegiance.
- mechanism: A stance can falsify reality without a spoken lie, and turning away from one address necessarily redirects face, attention, or allegiance elsewhere.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B009: A deceptive appearance supplies nonverbal falsification by the state one presents.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B006: Turning the face or attention toward something supplies the usually unstated destination of reorientation.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Averting supplies the explicit departure pole of the same directional movement.

## cover disclosure
- reading: The subject attempts a temporary concealment-and-escape operation inside a world whose counter-rhythm is disclosure.
- mechanism: The night-cover and day-disclosure pair converts denial into a contest over visibility. Falsification tries to place a cover over what is there, and withdrawal tries to escape its address, but disclosure makes concealment a phase rather than a final condition.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B009: Deception by displayed condition lets denial function as a covering appearance.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Retreat supplies the attempted spatial escape from what may become visible.
  - 92:1 **وَٱلَّيْلِ** ل ي ل B001: Darkness supplies the temporal medium in which concealment can seem stable.
  - 92:1 **يَغْشَىٰ** غ ش و B001: An overlying cover supplies the operative image for suppression of visibility.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: Daylight opening out supplies the counter-process that defeats enclosure.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Uncovering and manifestation supply the terminal exposure of what denial covered.

## counter formation
- reading: Denial becomes anti-generative: it remakes the account of an articulated order and then withdraws from its relational demand.
- mechanism: Measured making and a generated pair activate denial as counter-formation: it substitutes an invented account for a received differentiation, while withdrawal breaks relation to the paired order rather than merely disputing a sentence.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B002: Assigning falsehood supplies the act of relabeling what has been presented.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Withdrawal supplies severance from the relation or order being named.
  - 92:3 **خَلَقَ** خ ل ق B001: Measured proportion supplies an already articulated order against which the counter-account operates.
  - 92:3 **خَلَقَ** خ ل ق B007: Inventing false speech supplies the shadow-mode of making that connects formation to falsification.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: One member of the created pair supplies the first relational pole.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The other member supplies complementarity rather than an isolated unit.

## purposeful divergence
- reading: Turning away is itself energetic and directional: denial becomes a counter-striving whose product is increasing separation.
- mechanism: Purposeful movement plus dispersal makes withdrawal an active trajectory. The subject is not inert after denial; falsification organizes a course that increases distance and proves its charge false by where it goes.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B004: Failure to carry a charge through supplies the evaluative test of the subject's course.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Withdrawal supplies the direction taken by the failed performance.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Intentional motion toward an object prevents the retreat from being read as mere passivity.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion supplies the divergent result of differently directed effort.
  - 92:4 **لَشَتَّىٰ** ش ت ت B003: Distance between two things supplies the widening separation produced by the course.

## performative truth
- reading: He fails to make the claimed good true in conduct and exits the practices through which assent would become protective, generous, and path-opening.
- mechanism: Giving, self-protection, enacted truthfulness, good action, and opening ease form a practical chain. Against it, focus denial is failure to realize the good in action, and withdrawal is refusal to enter the giving-protecting circuit.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B004: A charge made false by failed execution supplies the negative counterpart to enacted truth.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Refusal of attention and compliance removes the subject from the practical chain.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Transfer to another supplies the outward act by which assent becomes material.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing oneself within protection supplies disciplined receptivity rather than self-exemption.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Realizing a promise in deed supplies the positive performative opposite of focus falsification.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: Doing what is good supplies the quality embodied by the practical sequence.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening after constriction supplies the path-effect of enacted confirmation.

## closed circuit
- reading: The subject builds a closed economy of refusal: withholding supports self-sufficiency, self-sufficiency supports denial, denial supports withdrawal, and that course becomes easy until its stored shield fails at the fall.
- mechanism: Withholding and claimed self-sufficiency close circulation; repeated denial gives that closure a verdict, and facilitation toward difficulty turns it into a self-reinforcing path. Accumulated wealth then cannot arrest the fall, so withdrawal is exposed as failed insulation.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B002: Declaring the good false supplies the judgment that rationalizes closure.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Withdrawal supplies the attempt to become inaccessible to claim, need, and consequence.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: Light, compliant movement supplies the feedback by which a chosen course becomes easier to continue.
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding supplies the material closure that precedes the repeated denial.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed independence supplies the imagined reason no relation or response is needed.
  - 92:9 **وَكَذَّبَ** ك ذ ب B002: The repeated attribution of falsehood explicitly binds the focus verb to this closed trajectory.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Twisting, opposition, and imposed difficulty supply the shape of the path produced by closure.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated property supplies the store expected to make the subject self-sufficient.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: A fall ending in ruin supplies the event that stored wealth cannot block.

## guidance refusal
- reading: The clause describes active map-refusal: an offered direction is first discredited and then deliberately left.
- mechanism: Gentle indication toward a path makes the focus a refusal of available orientation rather than the behavior of someone left without a route. Denial rejects the map; turning away redirects attention from it.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B002: Declaring the indication false supplies rejection of the map's reliability.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B006: Turning attention toward an object supplies the positive directional capacity being misused.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Averting supplies the chosen direction away from the offered indication.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward path and truth supplies an available orientation rather than coercion.

## returning sequence
- reading: Turning away enters a temporal chain: what looks like exit proceeds without a gap and returns as outcome within a field containing both beginning and end.
- mechanism: First-and-last totality, the return of a thing to its outcome, and the split root's image of unbroken succession make turning away paradoxically non-escapist: the act enters a sequence that carries it toward an owned end.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B004: A course tested by whether it proves true supplies the temporal evaluation of the act.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B002: Continuous succession supplies the chain that withdrawal inadvertently joins.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: Lateness after a beginning supplies the terminal pole of the temporal field.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Beginning and precedence supply the initial pole from which the course departs.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Return to outcome supplies the arc by which an apparent exit reaches its consequence.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: The non-dominant mapped root contributes succession and directly echoes the focus root's process image.

## distance reversed
- reading: His distancing action is itself reversed: by denying the warning that could preserve distance, he moves from aversion to contact with the warned heat.
- mechanism: Warning offers caution at a distance; the warned fire can be perceived from afar, yet the identified subject is the one who meets its heat. Thus the focus's chosen aversion from warning reverses into proximity to what was warned.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B002: Declaring the warning false disables its protective force for the subject.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning away supplies chosen distance from the warning.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B001: Nearness without an interval supplies the reversed spatial result.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: A warning that awakens caution supplies the opportunity to maintain protective distance.
  - 92:14 **نَارًا** ن و ر B003: Perceiving fire from afar supplies warning-distance before contact.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure, kindled flame supplies the concentrated object of the warning.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Meeting fire and its heat supplies forced contact after chosen aversion.
  - 92:15 **ٱلْأَشْقَى** ش ق و B002: Hardship and suffering supply the condition of the subject specified by the following focus clause.

## mirrored relative
- reading: He is the inverse of the giving subject: he turns himself away from truth and remains exposed, while the other sends wealth outward and is turned away from danger.
- mechanism: The adjacent relative-clause portraits invert agency and circulation. The focus subject actively turns away after denying; the contrasting subject gives wealth into circulation and is passively turned aside from danger while growing or purifying.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B004: Failed enactment supplies the negative mirror of a gift that materially realizes commitment.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Active self-withdrawal supplies one side of the agency reversal.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Being placed at a distance supplies the protected counterpart to self-directed withdrawal.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Repelling harm through protection supplies the result of the contrasting orientation.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving supplies outward transfer instead of self-enclosure.
  - 92:18 **مَالَهُۥ** م و ل B001: Possessed wealth supplies the same material that can either circulate or be treated as insulation.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth through the transfer supplies an expanding rather than closed economy.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purification supplies an inward transformation coupled to outward giving.

## exchange orientation
- reading: Turning away is a transfer of face and allegiance: the subject rejects the higher source-relation and becomes available to lower calculations of possession, credit, and return.
- mechanism: The absence of a repayable favor cancels horizontal debt, while seeking a face, lordly formation, and height establishes a vertical orientation. This makes focus withdrawal relationally thick: denial falsifies the source of good, and turning away redirects face and allegiance toward a lower exchange economy.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B002: False attribution supplies misrecognition of the claim or source to which response is due.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B006: Turning face and attention supplies the focus subject's capacity for redirected orientation.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B004: Alliance and support supply the social attachment implicated by directional turning.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive negation removes every human creditor from the motive structure.
  - 92:19 **عِندَهُۥ** ع ن د B004: Nearness and presence locate the supposed social account with another person.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: A favorable condition or benefit supplies the debt that is explicitly denied.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Reciprocating an act supplies the horizontal exchange motive being excluded.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking an object supplies the active vector of the alternative orientation.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and destination supply the axis along which face and purpose are set.
  - 92:20 **رَبِّهِ** ر ب ب B001: Lordship and ownership supply the higher relation that displaces human credit.
  - 92:20 **رَبِّهِ** ر ب ب B002: Nurturing and bringing to completion supply a non-transactional source of formation.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B002: Elevation and honor supply the vertical terminus of the quest.

## acceptance terminus
- reading: The pair is also affective closure: the subject refuses reception and exits the relation that could culminate in acceptance and satisfaction.
- mechanism: The final image of acceptance reveals the affective opposite of the focus. Declaring false is refusal to accept what addresses one, and turning away closes the relation before mutual satisfaction can form.
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B002: Declaring false supplies an adjudicative rejection rather than receptive assent.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B006: Facing, following, or accepting supplies the unrealized receptive pole within the focus root.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Averting supplies the actual closure against that receptive pole.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Acceptance opposed to displeasure supplies the final affective state missing from denial.
  - 92:21 **يَرْضَىٰ** ر ض و B003: Mutual satisfaction supplies a relational completion that withdrawal prevents.

## failed yield
- reading: As a contained material analogy, his denial is a yield that fails its promise and his turning is ripeness tipping into desiccation; withheld wealth does not grow because circulation has been arrested.
- mechanism: 
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B006: A yield that disappears instead of lasting supplies denial as failed material promise.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B016: Ripeness tipping into drying or color change supplies withdrawal as a transition out of living yield.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B002: Sufficiency supplies the expectation that the stored yield will be enough.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated wealth supplies the stock whose durability is trusted.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth supplies the live counter-process to depletion and arrested circulation.

## procession to fire
- reading: Turning away fixes the subject as a follower in a facilitated procession: he leaves the address but not the course whose next stage is contact with fire.
- mechanism: 
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B004: A charge tested by whether it carries through supplies the criterion for the whole course.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B002: Unbroken succession supplies the procession that continues after apparent retreat.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement supplies directed participation rather than accidental drift.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B005: Light, compliant motion supplies the ease with which the procession continues.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B006: The non-dominant mapped branch of following the race-leader supplies a positional image immediately beside the fire sense.

## severed patronage
- reading: As a contained legal-social reading, he falsifies and severs a bond of allegiance or obligation, unlike the giver whose act is free of human debt and repayment.
- mechanism: 
- trace:
  - 92:16 **كَذَّبَ** ك ذ ب B001: Falsehood in action supplies breach of the relation's claimed terms.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B005: Patronage and affiliated dependence supply the bond from which withdrawal can secede.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive negation clears the positive giver of every human creditor.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: Benefit supplies the favor around which social obligation would normally form.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Repayment supplies the dominant exchange relation explicitly denied as motive.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: The non-dominant mapped image of cutting supplies a contained analogy for severing the bond itself.


# Focus 92:17

## passive completion of self guarding
- reading: The most self-guarding person is made to occupy a removed position; granted deliverance completes a practiced placing of the self under protection.
- mechanism: An inwardly acquired habit of guarding is paired with an outward causative relocation. The subject does not merely avoid danger by personal effort; another agency completes that effort by putting the subject in a removed position.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Removal to a side supplies the passive spatial operation performed on the subject.
  - 92:17 **ٱلْأَتْقَى** و ق ي B002: Placing oneself under protective caution supplies the subject's prior disposition.

## safe flank and side shield
- reading: The protected subject is assigned to a safe flank and screened at the boundary, so lateral placement and interposition coexist with distance.
- mechanism: Side, shield, and barrier branches create layered geometry. Safety is not only more distance from an unnamed object but assignment to a screened flank where the boundary itself bears the exposure.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B001: The bodily flank and spatial edge supply a lateral safe-side geometry.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B011: A cover or shield stationed at the side turns that geometry into active screening.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: A guard interposed against harm supplies the barrier function of the screened flank.

## guarded escort at the edge
- reading: Safety may be a conducted passage along the field's edge, with proximity controlled by an escort and a guarded gait.
- mechanism: The two branches permit controlled proximity: a guarded subject can be conducted along the edge of danger rather than abandoned or exposed to it. Safety then lies in guided adjacency and calibrated movement.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B005: Leading or keeping a being alongside supplies an escort rather than a bare expulsion.
  - 92:17 **ٱلْأَتْقَى** و ق ي B003: A guarded gait around painful ground supplies cautious movement within that escort.

## alternating exposure boundary
- reading: The subject is kept on the unexposed side of an alternating cover-and-disclosure boundary, making protection dynamic rather than static.
- mechanism: The opening cover-and-disclosure cycle turns the baseline safe flank into a moving exposure boundary. As a surface is successively covered, opened, and disclosed, the protected subject is held on the side that does not become exposed to the threatening field.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B001: A spatial side supplies the flank on which exposure can be controlled.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: An interposed guard supplies continuity of protection while visibility changes.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A cover laid over a thing supplies the obscured phase of the boundary.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B003: Opening and widening until passage or flow supplies expansion of the exposed field.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Disclosure supplies the visible phase against which protected placement becomes legible.

## divergent striving becomes route sorting
- reading: The focus is one endpoint of a route-sorting system: divergent strivings become divergent courses, and the self-guarding course is laterally separated from the destructive one.
- mechanism: Purposeful movement is declared dispersed and far apart. The focus-side operation therefore reads as the terminal sorting of trajectories: one course is made to run on a protected flank rather than merely receiving an isolated exemption.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Removal and separation supply the operation that sorts one trajectory away from another.
  - 92:17 **ٱلْأَتْقَى** و ق ي B002: Self-protective caution identifies the disposition carried by the protected trajectory.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement toward an objective supplies trajectories rather than static moral labels.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion supplies the branching of the trajectories.
  - 92:4 **لَشَتَّىٰ** ش ت ت B003: Distance between two things supplies the widening separation between their endpoints.

## active guarding completed by facilitation
- reading: The superlative compresses a history of giving, guarding, and verified action, while the passive future marks a completion that the actor cannot perform alone.
- mechanism: Giving opens the hand, active self-guarding places the actor behind protection, fulfilled action makes the affirmed good operative, and facilitation opens a traversable course. The focus passive then completes this active sequence by relocating the same kind of subject beyond the hazard.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Being removed to the side supplies the externally completed outcome of the earlier actions.
  - 92:17 **ٱلْأَتْقَى** و ق ي B002: Self-placement under protection supplies the disposition named in superlative form at the focus.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing something over supplies the release of possession that begins the active sequence.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Active self-guarding supplies the earlier practice later condensed into the focus superlative.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Making a promise or action true supplies enacted verification rather than assent alone.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening into ease after difficulty supplies the traversable course that precedes final removal.

## gentle guidance and steep counterroute
- reading: Protection becomes guided topography: careful footing follows a gently indicated contour while the unprotected counterroute steepens into descent.
- mechanism: The split inventory places gentle path-direction beside a form-distant image of a difficult descent. Together with the focus branches of removal and guarded footing, they activate a topographic reading in which one subject is conducted onto a safe contour while a counterroute drops away.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Lateral removal supplies the transfer from one contour or route to another.
  - 92:17 **ٱلْأَتْقَى** و ق ي B003: Guarded footing supplies careful passage over injurious terrain.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward a path supplies the positive steering force.
  - 92:12 **لَلْهُدَىٰ** ه د ي B009: The non-dominant split image of a difficult descent supplies a deliberately form-distant counterroute.

## first and later as two stage protection
- reading: Protection spans two times: self-guarding begins the trajectory in the first domain, and passive removal consummates it in the later domain.
- mechanism: Beginning, eventual outcome, and delay make the focus future legible as the later phase of a process whose first phase is self-guarding. Protection can begin as present orientation and reach its outcome as externally effected removal.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Future removal supplies the process's later completed phase.
  - 92:17 **ٱلْأَتْقَى** و ق ي B002: Self-guarding supplies a first phase already active in the subject.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B002: Deferral to a later time supplies temporal distance before completion.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: The beginning of a thing supplies the process's first phase.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Return to an eventual outcome supplies continuity between the first phase and its consummation.

## warning contact and agency reversal
- reading: The warned and self-guarding subject is effectively turned aside from the blazing fire, while the subject who turns himself away from warning paradoxically makes contact with it.
- mechanism: Warning awakens caution, the formerly unspecified feminine object becomes a blazing fire, and the preceding subject is defined by contact with its heat. The decisive reversal is agential: the denier voluntarily turns away yet reaches the fire, whereas the self-guarding subject is passively turned aside from it.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Effective removal from a harmful object supplies the successful directional reversal.
  - 92:17 **ٱلْأَتْقَى** و ق ي B002: Protective caution supplies the disposition capable of receiving and acting on warning.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: A warning that frightens and wakes caution supplies the signal preceding protection.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies the concrete hazardous object later resumed by the feminine pronoun.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure, intensely kindled flame supplies the hazard's active reach.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Meeting fire and its heat supplies the contact state opposed to focus removal.
  - 92:15 **ٱلْأَشْقَى** ش ق و B001: The non-dominant mapped image of wretchedness supplies the contrasting superlative subject.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Voluntary turning away supplies the failed self-directed motion reversed by passive protective motion.

## regenerative transfer forms the protected self
- reading: The subject becomes and remains maximally self-guarding through regenerative transfer: wealth exits, while the giver grows and is purified.
- mechanism: Wealth moves outward while the giver undergoes inward growth and purification. The focus superlative is therefore not only an antecedent rank; it is formed and renewed through a transfer that appears as loss at the boundary but growth in the subject.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Removal supplies the outward separation that is paired with inward transformation.
  - 92:17 **ٱلْأَتْقَى** و ق ي B002: Self-protective formation supplies the subject changed by the transfer.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving supplies the outward transfer rather than mere arrival.
  - 92:18 **مَالَهُۥ** م و ل B001: Possessed wealth supplies the material that crosses the subject's boundary.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Increase and growth supply the non-depleting result of the outward transfer.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purification supplies the qualitative remaking of the giver.

## release from side bound repayment
- reading: The subject is side-set without a human patron at his side: protection coincides with release from the creditor-debtor network rather than dependence on it.
- mechanism: The denial of any benefactor present with the giver and awaiting repayment removes the ordinary social shield of patronage. Side-nearness in the focus is reconfigured: the subject is not protected by a creditor or patron at his side but is freed from the reciprocal claim itself.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B002: Nearness and companionship at one's side supply the social adjacency being reconfigured.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: A protective barrier poses the question of what, or who, actually shields the subject.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive negation removes every candidate human patron or creditor.
  - 92:19 **عِندَهُۥ** ع ن د B004: Presence and nearness supply the image of a claim held with the giver.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: Benefit and good condition supply the favor that could create reciprocal obligation.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Answering an act with its recompense supplies the reciprocity explicitly denied.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Collecting and satisfying a debt sharpens the denied relation into a creditor-debtor mechanism.

## away motion receives a positive vector
- reading: The displacement is a reorientation: lateral escape from fire is governed by a sought, elevated direction and completed by nurturing sovereignty.
- mechanism: Seeking, direction, nurturing sovereignty, and elevation give the focus removal a positive vector. The subject is not merely pushed into marginal space away from fire; the safe side is selected by orientation toward a higher face and an completing, nurturing lordship.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B001: A side or direction supplies the lateral component of the new vector.
  - 92:17 **ٱلْأَتْقَى** و ق ي B002: Protective self-orientation supplies the subject's readiness to follow that vector.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Active seeking supplies directed desire rather than aimless flight.
  - 92:20 **وَجْهِ** و ج ه B002: A direction or orientation supplies the vector's positive endpoint.
  - 92:20 **رَبِّهِ** ر ب ب B002: Nurturing, repairing, and bringing to completion supply the agency that can finish the protective movement.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Elevation supplies a vertical component to the otherwise lateral movement.

## guarding terminates in contentment
- reading: Caution is transitional: passive removal breaks the danger relation so that the protected subject can pass from vigilance into settled contentment.
- mechanism: The two future clauses form a sequence from defensive relocation to positive contentment. Maximal caution is not an endless anxious condition; once the threatening relation is broken, guarding can yield to acceptance and settled satisfaction.
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Removal from the harmful relation supplies the necessary negative phase.
  - 92:17 **ٱلْأَتْقَى** و ق ي B002: Protective caution supplies the provisional defensive posture.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Acceptance in place of displeasure supplies the positive state that follows defense.

## windward flank of an engulfing flame
- reading: A material hazard map flickers into view: the protected subject is shifted to a windward flank outside an engulfing flame front.
- mechanism: 
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B006: A directional wind and what it drives supply plume movement across a field.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: An interposed barrier supplies protection from the moving hazard.
  - 92:1 **يَغْشَىٰ** غ ش و B002: An engulfing cover supplies the spatial spread of the hazard.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies the material source carried through the field.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Intensely kindled flame supplies the dangerous plume front.

## perennial reserve reverses scarcity
- reading: Generosity behaves like perennial forage rather than depletion: released stock enters a growth cycle that side-sets the giver from a sterile scarcity regime.
- mechanism: 
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B008: Loss of herd milk supplies the scarcity regime from which protection is imagined.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B010: Rooted perennial forage that remains through scarcity supplies a regenerative reserve.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Preservation behind a guard supplies the reserve's protective function.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B006: Milk-yield and flock growth supply the productive regime opposed to dryness.
  - 92:18 **مَالَهُۥ** م و ل B001: Accumulated wealth supplies the stock that can be hoarded or released.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply regeneration after wealth leaves the giver.

## reserve runner kept out of the consuming race
- reading: The protected figure is withheld as a guarded reserve runner on the side, escaping a contest whose track consumes those committed to it.
- mechanism: 
- trace:
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B005: A led animal or spare horse kept alongside supplies the reserve-runner position.
  - 92:17 **ٱلْأَتْقَى** و ق ي B003: Guarded movement that avoids injuring the hoof supplies controlled expenditure in the course.
  - 92:4 **سَعْيَكُمْ** س ع ي B008: Contending in purposeful motion supplies the competitive field.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B007: Lots, gaming, and division of a slaughtered animal supply a consuming contest with assigned shares.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B007: A runner following the leader supplies a race-order image at the point of fire-contact.


# Focus 92:18

## transfer as reflexive purification
- reading: The person transfers owned wealth in a way that recursively cleans and rectifies the giver.
- mechanism: Possessed wealth is deliberately granted away, and the reflexive final verb makes the release act back upon the giver as purification and rectification.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B002: The granting-and-giving branch supplies the outward transfer that initiates the mechanism.
  - 92:18 **مَالَهُۥ** م و ل B001: The acquisition-and-possession branch marks the object as wealth held as one's own and therefore genuinely relinquished.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: The purity-and-rectitude branch supplies the reflexive inward result of the outward gift.

## release as increase
- reading: Giving is a release whose paradoxical product is increase and growth in the giver.
- mechanism: The apparent subtraction of wealth is recoded as productive release: what leaves possession becomes yield, while the giver enters a process of growth rather than mere depletion.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B007: The yield-and-produced-increase branch makes the act of giving capable of being imaged as releasing a return or crop.
  - 92:18 **مَالَهُۥ** م و ل B001: The wealth-possession branch supplies the stock whose reduction would ordinarily look like loss.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: The growth-and-increase branch turns relinquishment into the giver's productive enlargement.

## wealth as routed flow
- reading: Wealth is a current whose deliberate routing through the giver opens a channel of growth.
- mechanism: Wealth can be carried as a moving medium rather than a static hoard: giving clears or directs its course, and unobstructed circulation permits growth.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B004: The watercourse-and-cleared-flow branch supplies the material image of routing wealth through rather than retaining it.
  - 92:18 **مَالَهُۥ** م و ل B001: The possession branch supplies what can either pool as stock or be put into circulation.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: The growth branch supplies the flourishing made possible by the reopened course.

## proper access and fittingness
- reading: Purification also lies in finding wealth's fitting outlet and becoming congruent with that rightly routed act.
- mechanism: The giver does not merely surrender an amount; the giver finds the proper outlet for wealth, and this apt handling makes the act congruent with the person the giver is becoming.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B003: The proper-access, tact, and readiness branch supplies an apt way of bringing the wealth to its destination.
  - 92:18 **مَالَهُۥ** م و ل B001: The possession branch makes wealth the entrusted material whose outlet must be found.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B004: The suitability-and-fittingness branch makes the resulting act something that befits and reshapes the giver.

## integrity across hidden and manifest
- reading: The verse can depict an act whose inward efficacy survives both concealment and manifestation.
- mechanism: The opening alternation between covering and disclosure makes the gift readable across two visibility regimes. Its purifying force need not be produced by social display; the same transfer can remain operative when covered and when manifest.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B002: The giving branch anchors the visibility experiment in the actual transfer named by the focus ayah.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: The purification branch supplies an inward effect that can persist independently of whether the act is seen.
  - 92:1 **يَغْشَىٰ** غ ش و B001: The covering branch supplies concealment as one environmental regime for the giving.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: The disclosure-and-appearance branch supplies the opposite regime in which the same act becomes visible.

## giving as route selecting protection
- reading: The gift is a route-selecting practice through which the giver repeatedly enters a protective, self-rectifying course.
- mechanism: Divergent striving turns giving into a route-selecting practice rather than an isolated donation. The nearby coupling of handing over with self-protection lets the focus act be read as a repeated outward maneuver that also places the self within a guard.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B002: The granting branch supplies the concrete act by which a route is chosen.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: The rectification branch makes the chosen route transformative of the actor.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: The purposeful-motion branch frames conduct as directed movement toward a sought destination.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: The dispersion branch supplies genuinely diverging courses rather than interchangeable good deeds.
  - 92:5 **أَعْطَىٰ** ع ط و B002: The handing-over branch closely echoes the focus transfer and locates it in the selected course.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: The self-in-protection branch supplies the reflexive protective function paired with giving.

## claim made true in matter
- reading: Giving one's own wealth is the material event that verifies and realizes the claimed good.
- mechanism: Giving wealth becomes a material verification of what the giver affirms as good. The transfer moves truth from speech or assent into fulfilled action, with the wealth serving as the matter in which the claim is tested.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B002: The granting branch supplies the performed act that can verify a prior affirmation.
  - 92:18 **مَالَهُۥ** م و ل B001: The possession branch supplies costly material evidence rather than a costless verbal claim.
  - 92:6 **وَصَدَّقَ** ص د ق B004: The fulfillment-in-action branch turns affirmation into realized conduct.
  - 92:6 **وَصَدَّقَ** ص د ق B006: The wealth-and-right charity branch binds truthful realization specifically to material giving.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: The enacted-good branch supplies the quality that the transfer embodies rather than merely names.

## cleared flow becomes a habituated corridor
- reading: The gift reopens a course and trains the giver into an increasingly passable, productive trajectory.
- mechanism: The focus's watercourse and growth images become dynamic under the paired facilitation scenes. Giving clears a course and makes movement increasingly light and productive; the opposed course bends into obstruction and difficulty.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B004: The cleared-watercourse branch supplies the focus-level channel whose condition can change through use.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: The growth branch supplies the productive consequence of an opened course.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: The opening-and-ease-after-hardship branch supplies a corridor that becomes passable.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B006: The milk-yield and growth branch reinforces the surprising link between ease, flow, and productive increase.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: The twisting-and-obstruction branch supplies the opposed corridor produced by resistance.

## purification as depossession of self sufficiency
- reading: Purification is also de-possession of the fantasy that owned wealth can constitute or secure an independent self.
- mechanism: Withholding attempts to convert possessed wealth into independence, but the same wealth fails at the moment of collapse. The focus gift therefore purifies not merely by losing an object but by loosening the giver's false identification of possession with self-sufficiency.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B002: The giving branch supplies the counter-movement to withholding.
  - 92:18 **مَالَهُۥ** م و ل B001: The possession branch supplies the wealth around which a false independent self can be organized.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: The purification branch becomes removal of a possessive self-relation, not only accumulation of merit.
  - 92:8 **بَخِلَ** ب خ ل B001: The withholding branch supplies the opposed act of closing possession upon oneself.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: The self-sufficiency branch supplies the claim that retained wealth can make the holder independent.
  - 92:11 **مَالُهُۥٓ** م و ل B001: The repeated wealth-possession branch brings the focus object into the scene of its failure.
  - 92:11 **يُغْنِى** غ ن ي B002: The sufficiency-and-availing branch is explicitly negated, exposing possession's inability to substitute for the self.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: The falling-into-ruin branch supplies the limiting event at which retained wealth cannot avail.

## proper access becomes guided trajectory
- reading: The fitting transfer is an entry into a guided course oriented toward an outcome the giver does not own.
- mechanism: The focus branch of approaching by a proper access expands into a guided trajectory with an end or outcome. Giving is not only fitting at the point of transfer; it is entry onto a directed course whose terminus exceeds the possessor.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B003: The proper-access branch supplies the apt entry into the trajectory.
  - 92:18 **يُؤْتِى** ء ت ي B010: The road, junction, and far-limit branch extends giving from an access point into a traveled course and endpoint.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: The gentle direction-to-the-way branch supplies guidance along the course.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: The return-to-outcome branch supplies a terminus toward which the fitting gift can be read as moving.

## giving marks protective separation
- reading: Giving manifests and cultivates the purified alignment of a person being kept apart from harm, without becoming a purchase.
- mechanism: The one kept to the side away from the fire is immediately characterized by giving wealth to become purified. This makes giving an embodied alignment with protective separation, while stopping short of treating the gift as a payment that purchases escape.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B002: The granting branch supplies the behavior by which the protected figure is characterized.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: The purification branch supplies the inward alignment associated with being kept apart from harm.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: The distancing-and-keeping-apart branch supplies separation from the preceding danger.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B011: The side-shield branch gives the separation a concrete protective image.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: The warding-off-harm branch identifies the figure whose conduct the focus relative clause unfolds.

## release from the human repayment ledger
- reading: The giver initiates a one-way release whose purification depends partly on freedom from human repayment claims.
- mechanism: The following negation removes a backward-facing human claim: no one's prior favor is held with the giver as a debt to be repaid. The focus transfer is therefore not settlement of an exchange ledger but an initiating release without a human counterclaim.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B002: The granting branch supplies the outward transfer whose transactional status is being tested.
  - 92:18 **مَالَهُۥ** م و ل B001: The possession branch makes the transfer a real release of what stood within the giver's holdings.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: The purification branch locates the return within transformation of the giver rather than repayment by another person.
  - 92:19 **لِأَحَدٍ** ء ح د B002: The exhaustive-negation branch removes every human creditor from the stated motive.
  - 92:19 **عِندَهُۥ** ع ن د B004: The near-presence and holding-at branch supplies the image of an obligation standing on someone's account with the giver.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: The favor-and-good-condition branch supplies the possible prior benefit that the negation excludes.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: The recompense branch supplies the exchange relation explicitly denied as the gift's backward cause.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: The debt-collection branch sharpens the excluded model of giving as settling an account.

## growth reoriented toward a higher face
- reading: The giver grows by reorienting possession away from self-enlargement toward a personal, nurturing, higher end.
- mechanism: The next ayah gives the release a vector: seeking, direction or face, nurturing completion, growth, and height converge. The focus growth is not self-enlargement or replenishment of one's holdings; it is growth produced by orienting possession beyond the self toward a higher, nurturing end.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B002: The granting branch supplies the outward movement that receives a direction.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: The increase branch supplies growth whose kind and destination the context revises.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: The purity branch keeps the growth ethical and reflexive rather than merely quantitative.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: The seeking branch supplies deliberate pursuit as the gift's forward motive.
  - 92:20 **وَجْهِ** و ج ه B002: The direction-and-orientation branch gives the transfer a vector beyond the giver.
  - 92:20 **وَجْهِ** و ج ه B004: The face-as-self branch makes that vector personal rather than an abstract upward motion.
  - 92:20 **رَبِّهِ** ر ب ب B002: The nurturing, repairing, and completing branch supplies the agency toward which the giver's growth is oriented.
  - 92:20 **رَبِّهِ** ر ب ب B005: The non-dominant mapped growth-and-nourishment branch unexpectedly resonates with the focus increase and makes growth received rather than self-produced.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: The height-and-elevation branch supplies the upward scale of the sought end.

## nontransactional release opens into satisfaction
- reading: Nontransactional release can mature into settled acceptance and contentment without reversing into repayment.
- mechanism: The future satisfaction closes the sequence without restoring the human exchange ledger. What looks like immediate depletion opens into acceptance or deep contentment, so purification need not be imagined as permanent self-denial.
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B002: The granting branch supplies the initial release whose eventual affective horizon is disclosed.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: The growth branch allows the apparent loss to mature into fullness rather than remain deprivation.
  - 92:21 **يَرْضَىٰ** ر ض و B001: The satisfaction-opposed-to-displeasure branch supplies the eventual settled condition.
  - 92:21 **يَرْضَىٰ** ر ض و B002: The abundant-or-sought satisfaction branch gives the ending a fullness proportionate to the earlier release.

## torrent crossing the social boundary
- reading: Giving is abundance crossing from the socially or materially supplied side toward an outside, dry, or separated side, with growth generated by the crossing.
- mechanism: 
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B005: The elsewhere-arriving torrent branch supplies abundance moving from a supplied region into one that did not receive rain.
  - 92:18 **يُؤْتِى** ء ت ي B006: The outsider-among-another-people branch turns the transfer into movement across a social boundary.
  - 92:18 **مَالَهُۥ** م و ل B001: The wealth branch supplies the abundance capable of crossing that boundary.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: The growth branch supplies flourishing on the far side of transfer and in the giver.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: The separation, estrangement, and keeping-apart branch supplies the boundary that the torrent-outsider image crosses.

## a pair that refuses balanced exchange
- reading: Purification happens by entering a two-term relation through giving while refusing to reduce that relation to equal exchange.
- mechanism: 
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B002: The giving branch supplies the event that places two human positions into relation.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B005: The pair-and-even branch supplies the surprising two-term structure without deciding that the terms are equal.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: The male-in-contrast-to-female branch supplies one side of an explicitly created pair.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The female-in-contrast-to-male branch supplies the complementary side of that pair.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: The negated recompense branch prevents the giver-receiver pair from collapsing into balanced quid pro quo.

## cutting a web of claims
- reading: Wealth is also a web of possessive and reciprocal claims, and giving without repayment cuts strands that bind the giver.
- mechanism: 
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B002: The granting branch supplies the motion by which the giver passes out of an entangling possession.
  - 92:18 **مَالَهُۥ** م و ل B002: The reported spider branch supplies the strange but explicit image of wealth as a web of attachments.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: The purification branch supplies release from entanglement as the effect on the giver.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: The debt-collection branch supplies the social claims that would otherwise form the web's strands.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: The non-dominant cutting branch supplies the surprising severing of the repayment strands.

## levy inverted into free orientation
- reading: The payment-like exterior is inverted: with no human collector or debt, the wealth is freely released toward a chosen higher direction.
- mechanism: 
- trace:
  - 92:18 **يُؤْتِى** ء ت ي B008: The imposed-levy branch supplies the outwardly payment-like form that the context can invert.
  - 92:18 **مَالَهُۥ** م و ل B001: The wealth branch supplies the material that could superficially resemble a levy.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: The purification branch relocates the act's effect within the giver rather than in compliance with a collector.
  - 92:19 **لِأَحَدٍ** ء ح د B002: The exhaustive-negation branch removes any human claimant who could impose the payment.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B004: The financial-payment branch supplies the transactional model that the negated clause disallows.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: The seeking branch replaces imposed extraction with a deliberately pursued end.
  - 92:20 **وَجْهِ** و ج ه B002: The direction branch supplies the freely chosen orientation of the now de-coerced transfer.


# Focus 92:19

## human debt ledger
- reading: The sentence performs a total ledger-clearing: not even one person's prior benefaction is being answered by this act.
- mechanism: A bestowed benefit can remain present with its recipient as another person's credit. The focus construction clears the giver's whole interpersonal ledger: no such credit is present and no matching return is being made.
- trace:
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive anyone extends the negation across every possible human claimant.
  - 92:19 **عِندَهُۥ** ع ن د B004: Proximity and presence make a prior favor something that could still stand with him as an outstanding credit.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: Bestowed benefaction supplies the antecedent good that could generate obligation.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matched requital supplies the return that the negated favor would otherwise demand.

## no substitute discharge
- reading: No favor in his account is serving as substitute payment, discharging a due, or satisfying a collectible human claim.
- mechanism: A favor could function as consideration that discharges an obligation or as a collectible debt. The negation excludes both substitution and collection, so the act is not a device for closing someone else's account.
- trace:
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive anyone leaves no creditor for whom a discharge could operate.
  - 92:19 **عِندَهُۥ** ع ن د B004: Presence with him spatializes the place where a claim or countervalue would be held.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: A bestowed favor provides the possible consideration in the transaction.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B002: Standing in and sufficing recasts recompense as substitute performance or discharge.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Debt collection keeps live the sharper legal image of a claim being pursued and settled.

## no surplus balancing
- reading: It also denies an equalizing response to any extra increment that a person had previously placed above what was due.
- mechanism: A favor can be imagined as surplus added beyond what was due. If recompense restores equivalence, the focus negation says the giver is not balancing an earlier surplus bestowed by anyone.
- trace:
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive negation prevents any person from being the source of the supposed surplus.
  - 92:19 **نِّعْمَةٍ** ن ع م B010: Adding and going further supplies the exploratory image of favor as an increment beyond baseline obligation.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matching requital would bring that prior increment back into balance.

## unveiled motive ledger
- reading: The focus also functions as disclosure: beneath the visible transfer there is no concealed human repayment ledger.
- mechanism: Covering followed by disclosure turns the focus's legal negation into an exposure of motive: a visible gift could cover a hidden debt, but the sentence brings the absence of that debt into view.
- trace:
  - 92:19 **عِندَهُۥ** ع ن د B004: Presence with him supplies the potentially hidden internal account.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Requital identifies the concealed transactional motive whose absence is disclosed.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A cover rising over and concealing something models the outward gift masking an inward account.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Disclosure and appearance model the focus sentence as uncovering what actually drives the act.

## noncommensurate striving
- reading: This striving is not calibrated as a wage-like counter-act within the many divergent economies of human effort.
- mechanism: Measurement, earning activity, and dispersed strivings make recompense look like an operation that measures one act against another. The focus removes this giver's act from that human commensuration system.
- trace:
  - 92:19 **نِّعْمَةٍ** ن ع م B001: A bestowed favor is the candidate input to a measured exchange.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matching an act with its requital supplies the commensurating operation.
  - 92:3 **خَلَقَ** خ ل ق B001: Estimating and measuring supplies the image of calibrated equivalence.
  - 92:4 **سَعْيَكُمْ** س ع ي B002: Work and earning place human action inside an economy of effort and return.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion prevents the diverse strivings from collapsing into one uniform exchange pattern.

## forward protective verification
- reading: The transfer faces forward: it enacts truth and enters a protective path toward ease, while refusing a backward human claim.
- mechanism: Giving is sequenced with self-protection, enacted verification of the good, and opening into ease. This reverses the focus's denied backward arrow: the transfer does not look back to a human favor but works forward as truthful, protective movement.
- trace:
  - 92:19 **نِّعْمَةٍ** ن ع م B001: Prior benefaction supplies the backward-looking cause that the focus excludes.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matched return defines the retrospective transaction being reversed.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handover and giving supply the outward act whose direction is at issue.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing oneself in protection gives the act a prospective rather than compensatory function.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Fulfilling a promise in action makes giving verification rather than repayment.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B001: The good opposed to ugliness supplies the value being verified.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening into ease supplies the forward consequence of the protective trajectory.

## freedom not self sufficiency
- reading: The giver's freedom is the opposite of self-enclosed wealth: he is free of human patronage precisely while letting wealth go.
- mechanism: The stingy figure claims independence while retaining wealth, yet wealth cannot avail at the fall. Against that pattern, the focus's absence of human debt becomes relational freedom rather than possessive self-sufficiency.
- trace:
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive anyone clears every human patron or creditor from the giver's motive.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B002: Sufficing or availing distinguishes genuine release from dependence from merely possessing means.
  - 92:8 **بَخِلَ** ب خ ل B001: Stinginess supplies the rival strategy of securing oneself by withholding.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed wealth and independence name the rival's apparent freedom.
  - 92:11 **يُغْنِى** غ ن ي B002: Sufficiency and availing are explicitly negated for wealth at the crisis point.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated wealth supplies the retained asset that fails to liberate its holder.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: Falling into ruin supplies the event at which possessive independence proves false.

## horizontal debt vertical response
- reading: The verse may deny every human debt while leaving the giver responsive to guidance understood as direction or gift.
- mechanism: Guidance and gift coexist in the same context-root inventory, while the context assigns guidance to a non-human علينا. The focus can therefore clear horizontal repayment without making the act causeless: responsiveness to guidance remains live even when response to a human benefactor is denied.
- trace:
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive anyone supplies the cleared field of personal claimants.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: Bestowed favor names the antecedent whose human ownership is denied.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Requital marks the horizontal response that is excluded.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle direction toward the way supplies a possible antecedent for the giver's course.
  - 92:12 **لَلْهُدَىٰ** ه د ي B004: A gift sent to one beloved makes guidance itself available as a non-commercial giving image.

## first last transaction loop
- reading: It denies an entire human time-loop in which an earlier benefactor becomes the owner of the giver's later action.
- mechanism: A favor normally begins a transaction and delayed recompense closes it. The context's first, later, and return-to-outcome images enlarge that chronology, strengthening the claim that no human first cause owns the giver's later act.
- trace:
  - 92:19 **نِّعْمَةٍ** ن ع م B001: A prior benefaction supplies the possible beginning of the interpersonal loop.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Requital supplies the later act that would close the loop.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B002: Deferral to a later time sharpens the temporal gap between favor and repayment.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Beginning and precedence supply the first end of the transaction.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Return to outcome supplies the closure toward which an act tends.

## cosmic consequence not social repayment
- reading: It denies repayment to a human benefactor while remaining compatible with a larger moral consequence, protection, or reward.
- mechanism: Warning, encounter with fire, turning away, and being kept aside establish a consequence system larger than interpersonal exchange. Since recompense can include good or evil return, the focus now distinguishes cosmic consequence from social repayment rather than denying every consequence.
- trace:
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Reward or punishment within requital supplies the broad consequence category that needs differentiation.
  - 92:14 **فَأَنذَرْتُكُمْ** ن ذ ر B001: Warning that awakens caution announces consequential stakes.
  - 92:14 **نَارًا** ن و ر B002: Kindled fire supplies the punitive pole of consequence.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Encountering fire and its heat makes consequence experiential rather than merely contractual.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning away supplies the antecedent orientation of the punitive path.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Being distanced and kept apart supplies the positive figure's opposite outcome.
  - 92:17 **ٱلْأَتْقَى** و ق ي B002: Self-protection connects the protected figure to the earlier forward-looking path.

## transformative outflow
- reading: No value returns from a human creditor, but the outward loss of wealth can coincide with inward growth and purification.
- mechanism: Wealth moves outward through giving while growth and purification occur in the giver. The focus therefore separates reciprocal return from transformative return: nothing comes back from a human beneficiary, yet the act changes and enlarges its source.
- trace:
  - 92:19 **نِّعْمَةٍ** ن ع م B010: Adding and going further lets favor be tested against a different, non-equivalent kind of increase.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matched requital supplies the reciprocal return explicitly excluded.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving supplies the outward movement of value.
  - 92:18 **مَالَهُۥ** م و ل B001: Possessed wealth supplies what leaves the giver's control.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply a return that is generative rather than paid by another person.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purity and rectification locate the act's effect in transformation of the giver.

## direction over exchange
- reading: It clears a horizontal exchange so that the act can be read positively as directed seeking toward the highest Lord.
- mechanism: The exception after the focus supplies a vector: seeking, face or direction, lordship, and elevation reroute the act away from a nearby human creditor toward a higher object. Motivation becomes orientation rather than exchange.
- trace:
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive anyone clears every person from the destination of repayment.
  - 92:19 **عِندَهُۥ** ع ن د B004: Nearness and presence locate the rejected human center of account.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Requital supplies the exchange vector being displaced.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Active seeking supplies purposive motion beyond the cleared human ledger.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and orientation give the act a destination rather than a counterparty.
  - 92:20 **وَجْهِ** و ج ه B004: Face as self or essence preserves the personal object of seeking without making it a commercial creditor.
  - 92:20 **رَبِّهِ** ر ب ب B001: Lordship and sovereignty identify the non-human pole toward which the act is directed.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Elevation turns the horizontal account into an upwardly oriented relation.

## satisfaction not equivalence
- reading: The anticipated completion is satisfaction or acceptance rather than an equivalent counterpayment from a beneficiary.
- mechanism: Matched recompense closes an account by equivalence, whereas future satisfaction or acceptance is qualitative and potentially abundant. The final cue prevents no-repayment from becoming no-outcome.
- trace:
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matched requital supplies the finite equivalence that closes a debt.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B002: Sufficing and settling sharpen the image of a completed account.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Satisfaction opposed to displeasure supplies an open qualitative endpoint in place of exact repayment.

## pastoral anti harvest
- reading: The giver is not shearing a beneficiary's prior bounty for yield; the act releases wealth without harvesting a human return.
- mechanism: 
- trace:
  - 92:19 **نِّعْمَةٍ** ن ع م B005: Grazing livestock materializes the favor as a productive herd-like asset.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: The non-dominant cutting and shearing branch turns repayment into taking yield off an asset.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B006: Increase and productive flow in sheep activate the herd's capacity to yield.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase make harvesting that yield materially imaginable.

## no side accounts
- reading: The giver has no distributed patronage network stored in person-by-person side accounts that his gift must service.
- mechanism: 
- trace:
  - 92:19 **لِأَحَدٍ** ء ح د B005: Individual-by-individual distribution atomizes the possible patrons.
  - 92:19 **عِندَهُۥ** ع ن د B002: Sideward standing and separation picture each patron's claim as a side account.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Debt collection gives those side accounts a concrete social claim.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion multiplies the field into distinct, potentially competing accounts.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B001: Side and flank imagery reinforces the spatial model while the context's passive removal breaks the network.


# Focus 92:20

## exclusive vector
- reading: The phrase excludes every rival purpose except a live pursuit whose entire heading is fixed on the authority and incomparable rank of his Lord.
- mechanism: Pursuit supplies motion, face supplies orientation, lordship supplies the governing endpoint, and highest rank removes competing lower termini. The phrase therefore organizes desire spatially and hierarchically, not merely as an inward sentiment.
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking and pursuit make ابتغاء an active, sustained motion toward an object rather than a passive preference.
  - 92:20 **وَجْهِ** و ج ه B002: Orientation and direction give the pursuit its heading and make وجه function as a destination-bearing term.
  - 92:20 **رَبِّهِ** ر ب ب B001: Lordship, ownership, and authority identify the personal governing endpoint named by ربه.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B002: Nobility and high rank make الأعلى a hierarchy-setting qualifier that subordinates rival ends.

## encounter over reward
- reading: The sought good is non-transferable: direct orientation toward and encounter with the Lord himself displaces reward as the phrase's center.
- mechanism: The face can be the presented front, direct facing, and the self represented by the face. Those coexisting branches turn the object of pursuit from a transferable benefit into encounter with the Lord's own presence, while الأعلى preserves the asymmetry of that encounter.
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Pursuit keeps the relation desiderative and unfinished: the seeker is moving toward, not already possessing, the object.
  - 92:20 **وَجْهِ** و ج ه B001: Face and front supply a presented presence rather than an abstract benefit.
  - 92:20 **وَجْهِ** و ج ه B003: Facing and confronting make the pursued relation direct and face-to-face.
  - 92:20 **وَجْهِ** و ج ه B004: The self-or-essence branch allows وجه to point beyond a visible surface to the Lord himself.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Rising and height keep the encounter vertically asymmetrical rather than reciprocal between equals.

## nurtured ascent
- reading: Seeking the Most High can also mean entering the care by which the Lord repairs, grows, and raises the seeker toward completion.
- mechanism: The dominant lord branch repairs and completes stage by stage; the split mapped root adds rearing and growth; الأعلى adds rising. Together they permit a developmental reading in which the sought Lord is also the one who raises and completes the seeker.
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Pursuit supplies the seeker's active participation in a developmental movement.
  - 92:20 **رَبِّهِ** ر ب ب B002: Repair, nurture, and completion make lordship an ongoing formative process rather than a title alone.
  - 92:20 **رَبِّهِ** ر ب ب B005: The non-dominant nurture-and-growing branch reinforces stagewise formation while remaining explicitly split-root evidence.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Rising and being high convert الأعلى from a static epithet into the upward limit of the formative motion.

## status relocation
- reading: The verse may also dismantle patronage and prestige-seeking by relocating the quest for a favorable face to the only unsurpassable authority.
- mechanism: The phrase can relocate the economy of standing: instead of seeking a favorable face among human notables, the seeker directs the need for recognition toward the Lord whose rank exceeds every social hierarchy.
- trace:
  - 92:20 **وَجْهِ** و ج ه B006: Status and eminence activate وجه as the socially recognized face or standing one might otherwise court.
  - 92:20 **رَبِّهِ** ر ب ب B001: Lordship and authority relocate the source of recognized standing away from human patrons.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B002: High rank makes the Lord's standing categorically superior to the social ranks displaced by the exception.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking makes status not a possession but the contested object whose direction is being reassigned.

## visibility invariant orientation
- reading: Exclusive purpose is a visibility-invariant orientation: whether the deed is hidden or exposed, its face remains turned toward the same Lord.
- mechanism: The covering of 92:1 and disclosure of 92:2 place the focus face between hiddenness and visibility. The pursued orientation can remain constant even while the deed's outward face alternates between concealed and manifest.
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Sustained pursuit supplies the continuity that can survive changing conditions of visibility.
  - 92:20 **وَجْهِ** و ج ه B001: Face and outward front provide the visible surface whose appearance can be covered or disclosed.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A covering that rises over and hides something supplies the concealed phase of the mechanism.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Uncovering and appearance supply the revealed phase without requiring a change in underlying direction.

## directed amid scatter
- reading: ابتغاء وجه ربه is the focusing operation that turns scattered motion into a coherent trajectory and exposes movement without a true destination.
- mechanism: The context supplies diverse striving, while the split mapping of س ع ي keeps both purposeful motion and aimless going live. ابتغاء plus وجه becomes the discriminator between mere movement and movement with an integral destination.
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking and pursuing specify intentional movement toward a desired object.
  - 92:20 **وَجْهِ** و ج ه B002: Orientation and destination distinguish a vector from undirected motion.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Purposeful movement toward an object supplies the strong, directed pole of striving.
  - 92:4 **سَعْيَكُمْ** س ع ي B002: The non-dominant image of neglected, aimless going supplies a live counter-pole inside the split mapping.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion and scattering distribute the contextual strivings across divergent trajectories.

## course made traversable
- reading: Seeking the Lord's face is also a course enacted by giving and truthfulness, a course that becomes progressively open while its contrary twists into obstruction.
- mechanism: Giving and enacted truth lead into the opening of ease, while the opposed sequence leads into difficulty and crooked resistance. The proper-course branch of وجه lets purpose and action form a feedback loop: the chosen orientation is embodied in deeds, and the course then becomes more or less traversable.
- trace:
  - 92:20 **وَجْهِ** و ج ه B008: The proper aspect or course makes وجه the sound management and traversable way of an affair.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Giving supplies the concrete outward act by which an orientation becomes a course.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Fulfilling truth in action makes the claimed orientation behaviorally real.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening and ease after difficulty supply increased traversability along the enacted course.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B004: Crookedness, opposition, and obstruction supply the counter-course produced around the rejected orientation.

## guided pursuit
- reading: The seeker actively pursues a heading already gently indicated and undertaken by the Lord; agency remains real but responsive.
- mechanism: The pursuit is not self-authored navigation. Contextual guidance supplies gentle direction to the path; the focus supplies active seeking and a face as heading; lordship supplies the party who undertakes that guidance.
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking supplies the responsive motion of the seeker along a path.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and destination give the guided motion a determinate heading.
  - 92:20 **رَبِّهِ** ر ب ب B001: Lordship and authority identify the guide whose claim governs the route.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward road and truth supplies the route that precedes the seeker's response.

## first last priority
- reading: The exception is not delayed compensation but priority: across the entire first-to-last span, the highest Lord has the first and overriding claim on the act.
- mechanism: The context brackets later and first, while the split mapping of الأولى activates priority and entitlement. الأعلى then converts temporal comprehensiveness into an order of claims: the Lord who encompasses first and last also has the highest prior claim on purpose.
- trace:
  - 92:20 **رَبِّهِ** ر ب ب B001: Lordship and authority make temporal possession relevant as a claim upon the seeker's purpose.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B002: Highest rank translates the temporal bracket into a hierarchy of claims.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: Laterness after the first supplies one boundary of the complete temporal span.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Beginning and precedence supply the other boundary of the temporal span.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B008: The non-dominant priority-and-entitlement branch changes firstness from chronology into precedence of claim.

## turning and distance
- reading: It names a bodily and existential reorientation: turn toward this face, and the whole field of approach, avoidance, and protection is rearranged.
- mechanism: Turning away, being moved aside, and protection establish a spatial field of facing and distance. In that field, seeking the Lord's face is a positive turn that determines both what the seeker approaches and what the seeker is kept away from.
- trace:
  - 92:20 **وَجْهِ** و ج ه B002: Orientation and direction make the focus phrase the positive heading within the spatial contrast.
  - 92:20 **وَجْهِ** و ج ه B003: Direct facing supplies the approach relation opposed to turning away.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning the back and withdrawing provide the explicit counter-orientation.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Distancing and putting aside supply the protective relocation away from danger.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Repelling harm by protection gives the distancing a functional rather than merely geometric purpose.

## wealth into growth
- reading: The gift changes the medium of increase: accumulated wealth leaves the hand and becomes purified growth within a lordly process of completion and ascent.
- mechanism: The immediate context joins giving, accumulated wealth, and purification-growth. The focus joins lordly nurture to rising. This permits a conversion model: what leaves the possessor as wealth becomes formative increase in the seeker under the Most High.
- trace:
  - 92:20 **رَبِّهِ** ر ب ب B002: Repair, nurture, and completion provide the formative process into which relinquished wealth is converted.
  - 92:20 **رَبِّهِ** ر ب ب B005: The split-root nurture-and-growth image reinforces development while remaining a secondary activation.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B001: Rising and height make the resulting formation an ascent rather than mere replacement.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving supplies the outward transfer that begins the conversion.
  - 92:18 **مَالَهُۥ** م و ل B001: The taking and accumulation of wealth supply the stored quantity that is deliberately released.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply the positive result that counters material depletion.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purity and soundness keep the increase qualitative rather than equating it with more possessions.

## reciprocity ledger severed
- reading: The gift exits the whole human credit system: it neither settles a beneficiary's debt nor purchases a patron's face, leaving only pursuit of the highest Lord as its live claim.
- mechanism: Exhaustive negation removes every nearby human creditor, while favor and recompense supply the ledger that is denied. The following إلا leaves one surviving orientation. Seeking the Lord's face is therefore not one motive among social exchanges but the severance of compensatory patronage.
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking supplies the sole positive purpose remaining after reciprocal motives are removed.
  - 92:20 **وَجْهِ** و ج ه B006: Status and eminence expose the human faces and patrons whose recognition could otherwise function as repayment.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B002: Highest rank relocates recognition beyond the hierarchy of human benefactors and beneficiaries.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive scope under negation removes every possible human claimant from the ledger.
  - 92:19 **عِندَهُۥ** ع ن د B004: Nearness and presence locate the denied claim in the seeker's immediate social relation.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: Favor and good condition provide the benefit that could have created reciprocal obligation.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Matching an act with its recompense supplies the general exchange mechanism that the negation cancels.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Collecting and satisfying a debt sharpens recompense into a ledger of outstanding claims.

## desire arrives as contentment
- reading: The pursuit has a non-possessive arrival: the seeker comes to رضا, a state in which desire rests because its orientation has become sufficient.
- mechanism: The focus is grammatically open pursuit; the following verse supplies satisfaction and acceptance. The sequence lets رضا answer ابتغاء without turning the sought face into a commodity: desire reaches repose through alignment rather than acquisition.
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking and pursuit supply an open desiderative motion awaiting resolution.
  - 92:20 **وَجْهِ** و ج ه B002: Orientation makes resolution a matter of arriving in right alignment rather than possessing an object.
  - 92:21 **يَرْضَىٰ** ر ض و B001: Satisfaction as the opposite of displeasure supplies repose and acceptance at the end of pursuit.

## anti surplus increase
- reading: The giver also refuses to make another person finance his increase: wealth is released from debt-producing surplus and redirected toward growth sought from the Lord alone.
- mechanism: 
- trace:
  - 92:20 **رَبِّهِ** ر ب ب B003: Usurious surplus activates the possibility of increase extracted through an exchange, which the surrounding gift can reverse.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking redirects the desired increase away from extraction from another person.
  - 92:18 **مَالَهُۥ** م و ل B001: Accumulated wealth supplies the capital whose ordinary logic would be preservation or increase.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase provide a non-extractive alternative form of gain.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B003: Debt collection supplies the financial-social mechanism explicitly denied by the preceding clause.

## irrigating gift
- reading: Giving can be imagined as opening a channel: possession ceases to dam the resource, and directed release irrigates growth under the Lord's sustaining care.
- mechanism: 
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B006: The main downpour image supplies abundant release rather than measured reciprocal payment.
  - 92:20 **وَجْهِ** و ج ه B002: Orientation and direction keep the imagined flow attached to the focus phrase's destination.
  - 92:20 **رَبِّهِ** ر ب ب B008: A persistent low cloud that nurtures plants supplies the sustaining source of the ecological mechanism.
  - 92:18 **يُؤْتِى** ء ت ي B004: A watercourse and the opening of its channel recast giving as enabling flow.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase supply the irrigated result of the released flow.

## deed as advance party
- reading: The gift becomes an advance party of the self, sent ahead toward the Lord's face and testing the direction in which the giver's larger life will follow.
- mechanism: 
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B008: Scouting advance parties supply an anticipatory movement sent before a larger arrival.
  - 92:20 **وَجْهِ** و ج ه B001: Face and front provide the forward edge or meeting point toward which the advance movement travels.
  - 92:18 **يُؤْتِى** ء ت ي B002: Giving supplies the deed that can be imaginatively dispatched ahead of the giver.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Beginning and precedence reinforce the temporal logic of something going first.

## prayer fire contact bifurcation
- reading: The branch field suggests two rival contacts: active facing can become worshipful attachment to the Lord's face or culminate in involuntary encounter with consuming heat.
- mechanism: 
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking supplies the chosen approach that determines what kind of contact is pursued.
  - 92:20 **وَجْهِ** و ج ه B003: Facing and encounter make contact, rather than abstract belief, the shared mechanism.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B001: Prayer as binding worship supplies one sustained mode of approach and attachment.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Meeting fire and its heat supplies the destructive counter-mode of direct contact.

## reciprocal face satisfaction
- reading: As an exploratory resonance, the sought face-to-face relation may close in mutual consonance: pursuit is answered by a رضى that can be imagined as relational rather than solitary.
- mechanism: 
- trace:
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Pursuit supplies one party's movement into the relation.
  - 92:20 **وَجْهِ** و ج ه B003: Direct facing supplies the interpersonal geometry in which reciprocity can be imagined.
  - 92:21 **يَرْضَىٰ** ر ض و B003: Mutual satisfaction and conciliation activate a two-sided closure rather than solitary contentment alone.


# Focus 92:21

## emphatic delayed acceptance
- reading: He is emphatically promised a not-yet but certain passage from displeasure or unresolvedness into settled acceptance.
- mechanism: The core branch opposes satisfaction to displeasure, so the minimal clause promises a reversal from unresolved affect into settled acceptance; delay belongs to the transition, not to uncertainty about it.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B001: The core contrast between satisfaction and displeasure supplies the endpoint of the promised state change.

## acceptive ratification
- reading: The subject will come to accept and ratify an otherwise unstated outcome as one with which he can rest.
- mechanism: The acceptance side of the split root inventory lets the event function as ratification of an encountered outcome, not merely the onset of a pleasant emotion.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B001: The non-dominant mapped inventory preserves acceptance as the opposite of displeasure and supports an outcome-ratifying sense.

## sought fullness
- reading: He will reach a sought and ample sufficiency of satisfaction.
- mechanism: The branch of abundant or specially sought approval amplifies the endpoint: the clause can promise fullness of satisfaction, not bare cessation of complaint.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B002: The branch of abundant or sought approval expands the scale of the future satisfaction.

## relational settlement
- reading: An unstated relation may reach consent or concord, registered through the subject's becoming satisfied.
- mechanism: Although the focus form is not morphologically reciprocal, the mutual-consent branch activates a relational endpoint around it: one party's satisfaction may register a settlement whose counterpart is left implicit.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B003: The branch of reciprocal consent supplies a possible two-party horizon for the otherwise objectless verb.

## veil to disclosure
- reading: Future satisfaction is the affective consequence of a veil-to-disclosure transition: what cannot yet be seen will become acceptable when it is shown.
- mechanism: Night and covering establish an obscured phase; day and disclosure answer it with opened visibility. The focus future can therefore be read as satisfaction arriving when a presently covered consequence becomes manifest.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B001: Settled acceptance remains the focus endpoint whose timing is reinterpreted by the contextual alternation.
  - 92:1 **وَٱلَّيْلِ** ل ي ل B001: Night as the dark counter-state to day establishes the first, obscured phase.
  - 92:1 **يَغْشَىٰ** غ ش و B001: A cover rising over and hiding a thing makes concealment an active operation.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B002: Day opening through light supplies the counter-phase of access and visibility.
  - 92:2 **تَجَلَّىٰ** ج ل و B001: Disclosure after concealment provides the release point that can enable satisfaction.

## designed difference relational fit
- reading: Relational satisfaction can be a designed fit across real difference, with concord rather than homogeneity as its endpoint.
- mechanism: Measured creation coordinates two explicitly unlike poles. This activates the relational baseline as fit across difference: satisfaction need not erase distinction but can mark concord between differentiated terms.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B003: Reciprocal consent supplies the possible relational settlement reached across difference.
  - 92:3 **خَلَقَ** خ ل ق B001: Measuring and apportioning a thing presents differentiation as designed rather than accidental.
  - 92:3 **ٱلذَّكَرَ** ذ ك ر B001: The male term contributes one pole of the explicit opposition.
  - 92:3 **وَٱلْأُنثَىٰٓ** ء ن ث B001: The female term contributes the coordinated opposite pole.

## divergent striving to arrival
- reading: The subject arrives at satisfaction as the resolution of a directed course selected from genuinely divergent strivings.
- mechanism: Purposeful movement toward an aim is declared dispersed into different courses. Against that field, يَرْضَىٰ becomes a trajectory-closing arrival: satisfaction is where one course finally resolves, not an uncaused mood.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B001: Acceptance supplies the terminal state into which a course of striving may resolve.
  - 92:4 **سَعْيَكُمْ** س ع ي B001: Goal-directed movement turns the promised state into the endpoint of a course.
  - 92:4 **لَشَتَّىٰ** ش ت ت B001: Dispersion separates the available courses and makes their eventual outcomes non-equivalent.

## enacted path opens
- reading: Full satisfaction is the eventual fit produced along a path where giving, guardedness, enacted truth, and goodness are answered by opening and ease.
- mechanism: Passing something outward, placing the self under protection, realizing truth in deed, and doing the good are followed by an opening into ease. The ample satisfaction of the focus becomes the cultivated fit of an enacted path whose next movement is made open.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B002: Abundant or sought approval supplies the full endpoint generated by the positive sequence.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Handing something over initiates an outward transfer rather than retention.
  - 92:5 **وَٱتَّقَىٰ** و ق ي B002: Placing oneself within protection supplies a disciplined boundary for the path.
  - 92:6 **وَصَدَّقَ** ص د ق B004: Making a promise or claim real in action turns assent into operative commitment.
  - 92:6 **بِٱلْحُسْنَىٰ** ح س ن B002: The performance of good gives the affirmed good a behavioral form.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening and ease after difficulty supplies the pathway response to those acts.

## false sufficiency collapses
- reading: The promised رضا is durable sufficiency after the collapse of hoarded, self-declared sufficiency; it cannot be manufactured or secured by accumulated wealth.
- mechanism: Withholding closes the outward transfer while claimed self-sufficiency and denial misread what can sustain the subject. Facilitation then opens precisely onto difficulty, and accumulated wealth proves unable to suffice at the fall. The focus satisfaction is thereby distinguished from present complacency and from purchased security.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B001: Settled acceptance becomes the durable state contrasted with self-deceiving present sufficiency.
  - 92:8 **بَخِلَ** ب خ ل B001: Withholding blocks the transfer that opened the positive path.
  - 92:8 **وَٱسْتَغْنَىٰ** غ ن ي B001: Claimed independence supplies a rival, self-generated version of contentment.
  - 92:9 **وَكَذَّبَ** ك ذ ب B001: Contradiction of truth marks that claimed sufficiency as a misreading rather than a stable endpoint.
  - 92:10 **فَسَنُيَسِّرُهُۥ** ي س ر B001: Opening after resistance explains how a chosen course can become increasingly accessible even when its destination is adverse.
  - 92:10 **لِلْعُسْرَىٰ** ع س ر B001: Difficulty and severity name the adverse destination made accessible.
  - 92:11 **يُغْنِى** غ ن ي B002: Adequacy is the capacity explicitly denied to the subject's wealth at the decisive moment.
  - 92:11 **مَالُهُۥٓ** م و ل B001: Accumulated wealth supplies the stored resource that fails to secure its holder.
  - 92:11 **تَرَدَّىٰٓ** ر د ي B003: A fall into ruin supplies the event at which false sufficiency is exposed.

## guided temporal wholeness
- reading: The delay is a guided interval whose beginning and outcome lie within one encompassing order, making رضا an assured arrival rather than a lucky turn.
- mechanism: Gentle indication supplies direction, while the first and the last place both temporal ends within one domain and the return-to-outcome branch folds beginning toward consequence. The delayed رضا becomes arrival within an already held and guided whole.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B001: Acceptance is recast as arrival at the end of an oriented temporal course.
  - 92:12 **لَلْهُدَىٰ** ه د ي B001: Gentle indication toward a path supplies orientation rather than coercive transport.
  - 92:13 **لَلْءَاخِرَةَ** ء خ ر B001: The later or last term establishes the far temporal boundary.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B001: Beginning and precedence establish the near temporal boundary.
  - 92:13 **وَٱلْأُولَىٰ** ء و ل B002: Return toward final outcome turns the temporal pair into a course with a meaningful terminus.

## separation from consuming contact
- reading: Satisfaction is also embodied relief: the subject has been relocated outside a relation of consuming contact and held within protection.
- mechanism: Kindled flame becomes pure consuming heat, and misery is defined by entering into contact with it after denial and turning away. The guarded subject is instead moved aside and warded from harm. رضا thus gains a spatial and bodily substrate: satisfaction as no longer being exposed to consumption.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B001: The affective endpoint is grounded in a preceding change of exposure and location.
  - 92:14 **نَارًا** ن و ر B002: A kindled fire supplies the dangerous medium from which the later subject is separated.
  - 92:14 **تَلَظَّىٰ** ل ظ ي B001: Pure, actively burning flame intensifies the medium into something consuming.
  - 92:15 **يَصْلَىٰهَآ** ص ل ي B003: Meeting fire and its heat defines the adverse relation as direct contact.
  - 92:15 **ٱلْأَشْقَى** ش ق و B001: Wretchedness opposed to flourishing names the condition produced by that contact.
  - 92:16 **وَتَوَلَّىٰ** و ل ي B007: Turning away supplies the orientation that precedes the adverse exposure.
  - 92:17 **وَسَيُجَنَّبُهَا** ج ن ب B003: Being made separate and distant provides the positive subject's spatial reversal.
  - 92:17 **ٱلْأَتْقَى** و ق ي B001: Warding off harm supplies the protective function of that separation.

## release becomes growth
- reading: Giving converts stored wealth into personal growth and purification, so satisfaction is the ripened surplus of release rather than reimbursement for depletion.
- mechanism: Wealth is actively transferred outward while the giver reflexively grows and is purified. The focus's abundant satisfaction becomes the surplus generated by release: what leaves as possession returns as enlargement of the person rather than of the store.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B002: Abundant satisfaction supplies the eventual surplus that possession alone could not provide.
  - 92:18 **يُؤْتِى** ء ت ي B002: Active giving makes value leave the subject's possession and enter relation.
  - 92:18 **مَالَهُۥ** م و ل B001: Accumulated property supplies the material stock being released.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase relocate gain from the stock to the giver's developing state.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B002: Purification makes the gain qualitative as well as expansive.

## human reciprocity weakened
- reading: Human repayment is explicitly cleared from the mechanism; if the focus remains relational, its decisive counterpart and source of satisfaction lie beyond the human favor-debt ledger.
- mechanism: Exhaustive negation removes any favor held with any human party that needs repayment. This weakens the baseline's unrestricted mutual-consent reading: the later satisfaction cannot be explained as balancing a human ledger or purchasing another person's approval.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B003: The possible mutual-consent horizon is retained but narrowed by the cancellation of human debt.
  - 92:19 **لِأَحَدٍ** ء ح د B002: Exhaustive scope under negation removes every candidate human creditor.
  - 92:19 **عِندَهُۥ** ع ن د B004: Proximity or possession locates the alleged favor in the subject's social account before it is denied.
  - 92:19 **نِّعْمَةٍ** ن ع م B001: A benefaction supplies the putative credit that could have motivated repayment.
  - 92:19 **تُجْزَىٰٓ** ج ز ي B001: Counterbalancing an act with its return supplies the transactional loop that the negation breaks.

## directed nurturing completion
- reading: The subject reaches satisfaction as his upward-directed seeking is nurtured to completion—possibly as concord between seeker and sought, but certainly not as human repayment.
- mechanism: Seeking establishes an intentional vector toward a face or direction; lordship adds nurture and completion, and highest rank lifts the vector beyond the canceled human ledger. The future satisfaction becomes arrival into aligned relation. Mutual approval remains a coexisting possibility, but the grammar explicitly guarantees only the seeker's satisfaction.
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B001: Settled acceptance names the seeker's assured endpoint.
  - 92:21 **يَرْضَىٰ** ر ض و B003: Mutual consent keeps a two-sided concord reading live without making it grammatically explicit.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Deliberate seeking supplies the vector that precedes the promised arrival.
  - 92:20 **وَجْهِ** و ج ه B002: Direction and orientation give the seeking a determinate bearing.
  - 92:20 **وَجْهِ** و ج ه B003: Face-to-face encounter adds a relational endpoint alongside bare direction.
  - 92:20 **رَبِّهِ** ر ب ب B002: Nurturing, repair, and completion provide a process by which the seeker can be brought to fullness.
  - 92:20 **ٱلْأَعْلَىٰ** ع ل و B002: Elevation and honor place the sought relation above ordinary social exchange.

## adversarial settlement
- reading: رضا can register that a contested matter has finally been decided and no longer holds the subject in struggle.
- mechanism: 
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B005: The rare overcoming idiom turns satisfaction into the resolution of a contested matter.
  - 92:4 **سَعْيَكُمْ** س ع ي B008: Competitive striving supplies agents pressing against one another toward an outcome.
  - 92:5 **أَعْطَىٰ** ع ط و B007: Dominance within mutual dealing gives the positive act a latent contestive edge.
  - 92:15 **ٱلْأَشْقَى** ش ق و B003: Prevailing through arduous contest supplies a contextual echo of the rare focus branch.

## hydraulic circulation
- reading: As a contained material analogy, satisfaction is systemic equilibrium reached when value is released into an opened channel and allowed to circulate.
- mechanism: 
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B001: Settled acceptance supplies the equilibrium state to be explained by the material analogy.
  - 92:2 **وَٱلنَّهَارِ** ن ه ر B001: Running water cutting a channel supplies the basic image of directed circulation.
  - 92:5 **أَعْطَىٰ** ع ط و B002: Passing value outward keeps the system from closing around retained stock.
  - 92:7 **فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ** ي س ر B001: Opening after obstruction supplies the transition from blockage to flow.
  - 92:18 **يُؤْتِى** ء ت ي B004: A watercourse and the clearing of its way make the flow mechanism materially explicit.

## implied satisfier
- reading: The subject is brought to satisfaction by the nurturing completion of the one he seeks, though the verb itself states only his resulting state.
- mechanism: 
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B004: The causative and appeasing branch raises the possibility of an unexpressed satisfier behind the intransitive result.
  - 92:20 **ٱبْتِغَآءَ** ب غ ي B001: Seeking establishes the subject as moving toward something he does not produce for himself.
  - 92:20 **رَبِّهِ** ر ب ب B002: Nurture and completion supply a plausible contextual agency that brings the seeker to the resulting state.

## nurtured ripening
- reading: As a contained organic analogy, satisfaction ripens from growth that is fed and brought to fullness over time.
- mechanism: 
- trace:
  - 92:21 **يَرْضَىٰ** ر ض و B002: Abundant satisfaction supplies the mature fullness at the end of the analogy.
  - 92:18 **يَتَزَكَّىٰ** ز ك و B001: Growth and increase make the giver's inner change developmental.
  - 92:20 **رَبِّهِ** ر ب ب B005: The non-dominant mapped branch of feeding and development supplies nurture across the interval before fullness.
