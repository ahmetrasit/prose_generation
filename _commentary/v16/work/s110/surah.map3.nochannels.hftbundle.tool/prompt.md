Surah: 110. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), hft.md (its records are earlier readers' proposals: ignore their judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S110 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

===== _commentary/v16/prompts/map3/surah_map.md (adapted) =====
Read the surah as one text and write its map of image chains: the lexical images that run through several of
its ayat and join them into one scene, process or movement. A later writer will read one ayah at a time, with
only that ayah's own dictionary. The map lets that writer hear what the ayah's words carry in the surah as a
whole, including senses whose evidence sits under the words of other ayat.

Your evidence is the surah text, the dictionary of every root in the surah (each branch with the classical
dictionaries' own phrases), earlier readers' activation hypotheses (hft.md),
and your own knowledge of Arabic and the Quran. Where a member or passage comes from memory rather than from
the dictionary or the text, say so. Do not use tools, delegate, browse or inspect files.

The HFT records are proposals by earlier readers. Ignore their judgements: grades,
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
4. `## Not carried`. Each HFT record you did not carry into a chain: one short line
   each, its name and why, no prose.

No ranking and no labels of strength or confidence. No list of what a writer must include. There is no length
target and no required number of chains or members.

===== _commentary/v16/work/s110/surah.r2.nochannels.hftbundle/text.md =====
# Surah 110

- 110:1 إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلْفَتْحُ
- 110:2 وَرَأَيْتَ ٱلنَّاسَ يَدْخُلُونَ فِى دِينِ ٱللَّهِ أَفْوَاجًۭا
- 110:3 فَسَبِّحْ بِحَمْدِ رَبِّكَ وَٱسْتَغْفِرْهُ ۚ إِنَّهُۥ كَانَ تَوَّابًۢا


===== _commentary/v16/work/s110/surah.r2.nochannels.hftbundle/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج ي ء (root_000281): 110:1 جَآءَ

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · geliş; varış · bir kez geliş veya geliş biçimi · sık sık iyilik getiren · iyi ki geldin
  جاء يجيء مجيئا (maqayis;mufradat)؛ جاء فلان يجيء جيئة إذا جاء مرة واحدة وجيئة حسنة (jamhara)؛ المجئ: الاتيان، جاء يجئ جيئة، وجئت مجيئا حسنا (sihah)؛ المجيء كالإتيان لكن المجيء أعم ويقال في الأعيان والمعاني ولمن قصد مكانا أو عملا أو زمانا (mufradat)
- **B002** gelip gitmede üstün gelmek [kalıp] — benimle sık gelme yarışına girdi, ben de onu geçtim
  جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ وجاءانى على فاعلنى فجئته أجيئه، أي غالبني بكثرة المجئ فغلبته (sihah)
- **B003** suyun biriktiği çukur veya yer — suyun biriktiği yer veya büyük çukur · tuzlu ya da idrar karışmış kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره ويقال هي جيئة (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون، والموضع الذي يجتمع فيه الماء، والحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ جية من ماء أي ماء ناقع خبيث (tahdhib)
- **B004** bir şeyi getirmek veya hazır bulundurmak — sık sık iyilik getiren · bir şeyi getirmek veya hazır bulundurmak · onu getirmek
  أجأته، أي جئت به (sihah)؛ جاءه بكذا وأجاءه، وجاء بكذا: استحضره (mufradat)
- **B005** birini bir şeye zorlamak [kalıp] — onu belirli bir şeye zorlamak · seni buna gerek duyar duruma düşürmek
  أجأته إلى كذا بمعنى ألجأته واضطررته إليه (sihah)؛ أجاءها المخاض إلى جذع النخلة، قيل: ألجأها، وإنما هو معدى عن جاء (mufradat)
- **B006** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح، يقال: جاءت جائية الجراح (tahdhib)

## ج ي ء (root_000282): 110:1 جَآءَ

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## ن ص ر (root_001510): 110:1 نَصْرُ

- **B001** yardım edip üstün gelmesini sağlama — yardım etti ve düşmana karşı üstün gelmesini sağladı · yardım, destek · iyi ve etkili yardım · yardımcı, destekçi · yardımcı, destekçi · yardımcılar, destekçiler · düşmanına karşı kendisine yardım etmesini istedi · birbirlerine yardım ettiler, dayanıştılar
  النصر والنصرة العون (mufradat)؛ عون المظلوم (ayn;tahdhib)؛ نصره الله على عدوه ينصره نصرا (sihah)؛ آتاهم الظفر على عدوهم (maqayis)؛ النصير الناصر (ayn;sihah;tahdhib)؛ التناصر التعاون (mufradat)
- **B002** zulmedene karşı koyup hakkını alma — zulmeden kişiden hakkını aldı, öcünü aldı
  انتصر انتقم وهو منه (maqayis)؛ انتصر الرجل انتقم من ظالمه (ayn)؛ وانتصر منه انتقم (sihah)؛ انتصر الرجل إذا امتنع من ظالمه (tahdhib)؛ الانتصاف والانتقام منه (tahdhib)؛ إذا أصابهم البغي هم ينتصرون (mufradat)
- **B003** bir ülkeye veya toprağa gelmek [kalıp] — belirtilen ülkeye veya toprağa geldim
  نصرت بلد كذا إذا أتيته (maqayis)؛ نصرت أرض بني فلان أي أتيتها (tahdhib)
- **B004** toprağı sulayıp yeşerten, insanları ferahlatan yağmur — yağmur · eksiksiz ve doyurucu yağmur · yağmur ülkeyi suladı veya yeşertti · toprağa yağmur yağdı · halk yağmura kavuşup rahatladı
  يسمى المطر نصرا (maqayis)؛ نصر الغيث البلاد أرواها (ayn)؛ نصر الغيث الأرض أي غاثها (sihah)؛ النصرة المطرة التامة (tahdhib)؛ نصر الغيث البلاد إذا أنبتها (tahdhib)؛ نصر القوم إذا أغيثوا (tahdhib)
- **B005** iyilik veya armağan verme — armağan, veriş
  النصر العطاء (maqayis;sihah)؛ أصل صحيح يدل على إتيان خير وإيتائه (maqayis)
- **B006** Hristiyanlık ve Hristiyan olma ya da yapma — Hristiyan oldu, Hristiyanlığı benimsedi · onu Hristiyan yaptı · Hristiyan erkek, Hristiyan · Hristiyan kadın · Hristiyanlar
  تنصر دخل في النصرانية (ayn;tahdhib)؛ نصره جعله نصرانيا (sihah)؛ رجل نصراني وامرأة نصرانية (sihah)؛ النصارى قيل سموا بذلك لقوله كونوا أنصار الله (mufradat)؛ انتسابا إلى قرية يقال لها نصرانة (mufradat)
- **B007** uzaktan gelip su toplanma yerine ulaşan su yatağı — uzaktan gelip su toplanma yerine ulaşan su yatakları · bu tür su yatağı için olası tekil ad · bu tür su yatağı için diğer olası tekil ad
  النواصر من الشعاب ما جاء من مكان بعيد إلى الوادي؛ النواصر مسايل المياه واحدها ناصرة؛ تجيء من مكان بعيد حتى تقع في مجتمع الماء

## ء ل ه (root_000047): 110:1 ٱللَّهِ, 110:2 ٱللَّهِ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 110:1 ٱللَّهِ, 110:2 ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ف ت ح (root_001124): 110:1 وَٱلْفَتْحُ

- **B001** fiziksel açma, açılma ve geniş açıklık — fiziksel açma ve kapalılığı giderme · kapıyı, kilidi veya kapalı eşyayı açmak · açılmak; çiçeğin açması · geniş ve açık kapı · ağzı geniş, tıpasız ve kılıfsız şişe · açıklık veya gedik · idrar yolu geniş dişi deve
  خلاف الإغلاق ونقيض الإغلاق (maqayis;ayn;jamhara;sihah;tahdhib;mufradat)؛ فتحت الباب وغيره فتحا (maqayis;sihah)؛ كل شيء انكشف عن شيء فقد انفتح عنه ومنه تفتح النور (jamhara)؛ باب فتح أي واسع مفتوح (maqayis;ayn;sihah;tahdhib;mufradat)؛ قارورة فتح واسعة الرأس والفتحة الفرجة والفتوح الناقة الواسعة الإحليل (sihah;tahdhib)
- **B002** sonrasını başlatan ilk bölüm veya eylem — bir şeyin başlangıcı ve ilk bölümü · kitabın açılış bölümü · kutsal metindeki bölümlerin başlangıçları · ibadeti başlatan ilk yüceltme sözü · bir şeye başlamak ve girişmek
  فواتح القرآن أوائل السور (maqayis;ayn;tahdhib)؛ كل ما بدأت به فقد استفتحته وبه سميت الحمد فاتحة الكتاب (jamhara)؛ فاتحة الشيء أوله (sihah)؛ فاتحة كل شيء مبدؤه الذي يفتح به ما بعده وافتتح فلان كذا إذا ابتدأ به (mufradat)؛ افتتاح الصلاة التكبيرة الأولى (ayn)
- **B003** uyuşmazlığı hükümle çözüme bağlama — çekişen taraflar arasında hüküm vermek · hüküm ve yargı işi · hükmeden ve karar veren · hükmeden yargıç
  الفتح والفتاحة الحكم والله الفاتح أي الحاكم (maqayis)؛ الفتح أن تحكم بين قوم يختصمون إليك والفتاح الحاكم (ayn)؛ فتح فلان بين بني فلان إذا حكم بينهم والفتاح العليم (jamhara)؛ افتح بيننا أي احكم والفتاحة الحكم (sihah)؛ الفتاح الحكومة والقاضي لأنه يفتح مواضع الحق (tahdhib)؛ فتح القضية فتاحا فصل الأمر فيها وأزال الإغلاق عنها (mufradat)
- **B004** üstün gelerek zafere ulaşma — zafer, üstün gelme veya savaşta ele geçirme · düşman ülkesini yenerek ele geçirmek · Tanrı'dan birine karşı zafer istemek
  الفتح النصر والإظفار واستفتحت استنصرت (maqayis)؛ الفتح افتتاح دار الحرب والفتح النصرة واستفتحت الله سألته النصر (ayn)؛ الاستفتاح الاستنصار والفتح النصر (sihah)؛ إن تستنصروا فقد جاءكم النصر (tahdhib)؛ يحتمل النصرة والظفر والاستفتاح طلب الفتح أو الفتاح وطلب الظفر (mufradat)
- **B005** kaynaktan çıkıp akan su — kaynaktan çıkan veya akarsuda ilerleyen su · nehir suyuyla sulanan ekin veya hurmalık · mevsim yağmurlarının ilki
  الفتح الماء يخرج من عين أو غيرها (maqayis)؛ الفتح الماء يجري من عين أو غيرها (sihah)؛ الفتح النهر وما جرى في الأنهار من الماء وما سقي فتحا وأول مطر الوسمي الفتوح (tahdhib)
- **B006** kapalıyı açan araç — kapıyı, kilidi veya başka bir kapalı şeyi açan anahtar · kilitli olanı açmaya yarayan araç · bilinmeyene erişmeyi sağlayan yollar
  المفاتيح جمع المفتاح الذي يفتح به المغلاق (ayn)؛ المفتاح معروف (jamhara)؛ المفتاح مفتاح الباب وكل مستغلق (sihah)؛ الذي يفتح به المغلاق مفتح بكسر الميم ومفتاح (tahdhib)؛ المفتح والمفتاح ما يفتح به ومفاتح الغيب ما يتوصل به إلى غيبه (mufradat)
- **B007** servet saklanan yer veya içindeki servet — servet saklanan yer veya gömü · servet depoları, gömüler veya bunlardaki mallar
  المفتح الخزانة ومفاتحه الكنوز وصنوف أمواله (ayn)؛ المفتح الكنز ومفاتحه كنوزه (jamhara)؛ المفتح الخزانة ومفاتحه كنوزه وخزائنه وما في الخزائن من مال (tahdhib)؛ مفاتح خزائنه وقيل الخزائن أنفسها (mufradat)
- **B008** güçlüğü giderme ve bilgiyi erişilir kılma [kalıp] — kaygıyı veya sıkıntıyı gidermek · bir şeyi bildirip kavratmak · anlaşılması güç bir bilgi alanını açıklığa kavuşturmak · okuyan kişiye takıldığı yeri söylemek
  الفتح أن تفتح على من يستقرئك (ayn)؛ إزالة الإغلاق والإشكال وما يدرك بالبصيرة كفتح الهم وإزالة الغم وفقر يزال بإعطاء المال وفتح المستغلق من العلوم وفتح عليه كذا إذا أعلمه ووقفه عليه (mufradat)
- **B009** serveti veya bilgisiyle böbürlenme — serveti veya bilgisiyle böbürlenme
  الفتحة تفتح الإنسان بما عنده من أموال أو أدب يتطاول به (ayn)؛ الفتحة التيه والتكبر وأحسبها مولدة (jamhara)؛ الفتحة تفتح الإنسان بما عنده من ملك أو أدب يتطاول به (tahdhib)

## ر ء ي (root_000531): 110:2 وَرَأَيْتَ

- **B001** gözle ya da içsel kavrayışla görme — gözle ya da içsel kavrayışla görmek · görme, gözle algılama · kendi gözüyle görme · yeni ayı görebilmek için dikkatle bakmaya çalıştık
  نظر وإبصار بعين أو بصيرة (maqayis)؛ رأيت بعيني رؤية ورأيته رأي العين (ayn;tahdhib)؛ الرؤية بالعين (sihah)؛ الرؤية إدراك المرئي بالحاسة (mufradat)
- **B002** düşünüp bir görüşe varma — bilmek, sanmak veya öyle olduğuna inanmak · görüş, kanı veya değerlendirme · düşünüp taşınmak ve bir görüşe varmak · ağır ağır ve dikkatle düşünme · bir görüşe varmak için düşünme · adamın görüşünü sordu · onunla görüş alışverişinde bulundu · gözle gördüğünün gereğince öyle sandı
  الرأي ما يراه الإنسان في الأمر (maqayis)؛ الرأي رأي القلب (ayn;tahdhib)؛ بمعنى العلم تتعدى إلى مفعولين ورأى في الفقه رأيا (sihah)؛ الرأي اعتقاد النفس والروية والتروية التفكر (mufradat)؛ استرأيت الرجل في الرأي أي استشرته (tahdhib)
- **B003** uykuda görülen düş — uykuda görülen düş · uykuda görülen düşler
  الرؤيا معروفة والجمع رؤى (maqayis)؛ رأيت رؤيا حسنة (ayn)؛ رأى في منامه رؤيا وجمع الرؤيا رؤى (sihah)؛ لا تجمع الرؤيا وتجمع الرؤيا رؤى (tahdhib)؛ الرؤيا ما يرى في المنام (mufradat)
- **B004** karşı karşıya gelip görünür olma — topluluk birbirini gördü · görünmek üzere karşıma çıktı · birbirine bakar ve karşılıklı konumda
  تراءى القوم إذا رأى بعضهم بعضا (maqayis)؛ تراءى القوم رأى بعضهم بعضا وتراءى لي فلان (ayn)؛ قوم رئاء وبيوتهم رئاء وتراءى الجمعان (sihah)؛ تراءينا أي تلاقينا فرأيته ورآني وداري ترى دار فلان (tahdhib)؛ تراءا الجمعان أي تقاربا وتقابلا ومنازلهم رئاء (mufradat)
- **B005** başkaları görsün diye yapma — başkaları görsün diye yapma · işini başkalarına gösteriş için yaptı · gösteriş yapmaya zorlandı veya özendi
  وراءى فلان يرائي وفعل ذلك رئاء الناس وهو أن يفعل شيئا ليراه الناس (maqayis)؛ فلان مراء والاسم الرياء وفعل ذلك رياء وسمعة (sihah)؛ يرآءون الناس إذا أبصرهم الناس صلوا وإذا لم يروهم تركوا الصلاة (tahdhib)؛ فعل ذلك رئاء الناس أي مراءاة (mufradat)
- **B006** görünüş, belirti ve yansıtıcı yüzey — ayna · aynada yüzüne baktı · güzel ve parlak dış görünüş · göze güzel görünen durum veya donanım · yüzde beliren budalalık belirtisi
  الرئي ما رأت العين من حال حسنة والرواء حسن المنظر والمرآة معروفة (maqayis)؛ المرآة التي ينظر فيها والري ما أريت القوم من حسن الشارة والهيئة والرواء حسن المنظر (ayn)؛ المرآة التي ينظر فيها والمرآة المنظر الحسن والرواء حسن المنظر ورأوة الحمق (sihah)؛ الرئي المنظر والرواء حسن المنظر والمرآة التي ينظر فيها ورأوة أي نظرة ودمامة (tahdhib)؛ المرآة ما يرى فيه صورة الأشياء (mufradat)
- **B007** aybaşı sonu izi ve denetleme bezi — aybaşı sonrası hafif sarı, beyaz veya bulanık iz · aybaşı belirtisi olarak görülen iz
  الترئية والترية ما تراه الحائض من صفرة بعد دم حيض أو أمارات الحيض (maqayis)؛ الترية الخرقة التي تعرف بها المرأة حيضها من طهرها والماء الأصفر عند انقطاع الدم (jamhara)؛ الترية الشيء الخفي اليسير من الصفرة والكدرة (sihah)؛ الترية ما تراه المرأة من بقية حيضها من صفرة أو بياض (tahdhib)
- **B008** kişiye görünen görünmez yoldaş — kişiye alışıp onunla ilişki kuran görünmez varlık · görünmez yoldaşı ona göründü
  الرئي جني يتعرض للرجل يريه كهانة وطبا (ayn)؛ به رئي من الجن أي مس (sihah)؛ رئي من الجن وهو الذي يعتاد الإنسان من الجن وأرأى إذا صار له رئي من الجن (tahdhib)؛ مع فلان رئي من الجن (mufradat)
- **B009** akciğer ve ona gelen zarar — akciğer · akciğerine vurdu veya sapladı · akciğerinden yakındı
  الرئة موضع الريح والنفس وجمعها الرئات والرئين (ayn)؛ الرئة مهموزة وتجمع على رئين ورأيته أي أصبت رئته (sihah)؛ أرأى إذا اشتكى رئته (tahdhib)؛ الرئة العضو المنتشر عن القلب ورئته إذا ضربت رئته (mufradat)
- **B010** meme gelişmesiyle gebeliğin belli olması — dişi devenin gebeliği memesi gelişince belli oldu · dişi koyunun gebeliği memesi büyüyünce belli oldu
  أرأت الناقة إذا أرأى ضرعها أنها أقربت وأنزلت (ayn)؛ أرأت الشاة إذا عظم ضرعها قبل ولادها (sihah)؛ إذا استبان حمل الشاة وعظم ضرعها قيل أرأت (tahdhib)؛ أرأت الناقة إذا أظهرت الحمل حتى يرى صدق حملها (mufradat)
- **B011** görünür yere dikilen bayrak — dikili bayrak veya görünür işaret · bayrağı dikti
  الراية من رايات الأعلام (ayn)؛ الراية العلم لا تهمزها العرب وأصلها الهمز (tahdhib)؛ الراية العلامة المنصوبة للرؤية (mufradat)
- **B012** gösterip görmesini sağlama — bakması için aynayı ona tuttu · ona gösterip görmesini sağladı · ver, uzat · Tanrı onu düşmanını sevindirecek bir duruma düşürdü
  أرني يا فلان ثوبك لأراه وأرنا للمعاطاة (ayn)؛ أريته الشيء فرآه (sihah)؛ رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها وأرى الله الناس بفلان (tahdhib)؛ أرنا وبما أراك الله أي بما علمك (mufradat)
- **B013** söyler misin, bir düşün — söyler misin, bir düşün · söyleyin bakalım, bir düşünün
  أرأيتك وأنت تقول أخبرني (tahdhib)؛ يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه (mufradat)

## ECHO ر و ي (root_000615): for 110:2 وَرَأَيْتَ: withheld observed target; not identity

- **B001** suya kanma ve susuzluğun giderilmesi — susuzluğu sona erinceye kadar su içmek · suya kanmak · suya kanmışlık; susuzluğun sona ermesi · suya kanmış, susuzluğu kalmamış · tatlı ve içeni iyice kandıran bol su · bol sulu pınar
  خلاف العطش (maqayis)؛ رويت من الماء ريا وارتويت وترويت (sihah)؛ روي فلان من الماء يروى ريا فهو ريان (tahdhib)؛ ماء رواء وروى (sihah;tahdhib;mufradat)؛ عين رية (sihah)
- **B002** başkaları için su çekip getirme — ailesine su getirip taşımak · topluluk için su çekmek · su çekmede kullanılan yük hayvanı veya su çeken kişi · su taşımaya yarayan büyük tulum · su taşıma işini meslek edinen kimse · hacıların sonraki günler için su tedarik ettiği gün
  رويت على أهلي أروي ريا (maqayis;sihah;tahdhib)؛ رويت القوم أرويهم إذا استقيت لهم (sihah;tahdhib)؛ الراوية البعير أو البغل أو الحمار الذي يستقى عليه (sihah)؛ الراوية هو البعير الذي يستقى عليه الماء والرجل المستقي أيضا راوية (tahdhib)؛ يوم التروية سمي به لأنهم يرتوون فيه من الماء (sihah;tahdhib)
- **B003** anlatı veya şiir aktarma — anlatıyı veya şiiri aktarmak · anlatı veya şiir aktaran kimse · çok sayıda şiir ya da anlatı aktaran kimse · birine şiiri tekrar ederek ezberletmek
  رويت الحديث والشعر رواية فأنا راو (sihah)؛ روى فلان حديثا وشعرا يرويه رواية فهو راو (tahdhib)؛ روى فلان فلانا شعرا إذا رواه له حتى حفظه للرواية عنه (tahdhib)؛ الذي يأتي القوم بعلم أو خبر فيرويه كأنه أتاهم بريهم من ذلك (maqayis)
- **B004** enine boyuna düşünüp değerlendirme — enine boyuna düşünme; değerlendirme · bir mesele üzerinde düşünüp değerlendirmek
  الرَّوِيَّة التفكر في الأمر (sihah)؛ رويت في الأمر إذا نظرت فيه وفكرت (sihah)؛ روأت في الأمر وريأت فكرت (tahdhib)
- **B005** birinden beklenen ihtiyaç veya talep [kalıp] — birinden beklenen ihtiyaç veya talep
  لنا قبلك روية أي حاجة (sihah)؛ لنا عند فلان روية وأشكلة وهما الحاجة (tahdhib)
- **B006** geriye kalan bölüm veya miktar — borçtan ya da başka bir şeyden kalan miktar
  الرَّوِيَّة البقية من الدين ونحوه (sihah)؛ بقيت منه روية أي بقية مثل التلية (tahdhib)
- **B007** yük bağlama ipi — yükü veya su tulumlarını yük hayvanına bağlayan ip · yükü veya su tulumlarını özel iple hayvana bağlamak · su tulumlarını yük hayvanına bağlayan ip
  الرِّوَاء حبل يشد به المتاع على البعير (sihah)؛ رويته على الرجل إذا شددته على ظهر البعير (sihah)؛ الرِّوَاء الحبل الذي يروى به على الراوية إذا عكمت المزادتان (tahdhib)؛ يقال له المروى وجمعه مراوى (tahdhib)
- **B008** yapıya göre dolgunlaşma veya suya kavuşma [kalıp] — ipin lifleri kalınlaşıp bükümü sıkılaşmak · eklemler dengeli ve dolgun hale gelmek · sırtı semirip dolgunlaşmış at · kurak yere dikildikten sonra kökten sulanmak
  ارتوى الحبل غلظت قواه (sihah)؛ ارتوت مفاصل الرجل اعتدلت وغلظت (sihah)؛ ارتوت مفاصل الدابة إذا اعتدلت وغلظت (tahdhib)؛ فرس ريان الظهر إذا سمن متناه (tahdhib)؛ ارتوت النخلة إذا غرست في قفر ثم سقيت في أصلها (tahdhib)
- **B009** hoş ve güzel dış görünüş — hoş dış görünüş; görünen güzellik · kökeni tartışmalı bir görünüş güzelliği biçimi
  رجل له رُوَاء أي منظر (sihah)؛ من لم يهمز رئيا جعله من روي كأنه ريان من الحسن (mufradat)
- **B010** hoş koku — hoş koku; bir şeyin güzel kokusu
  طيبة الرِّيَا إذا كانت عطرة الجرم (tahdhib)؛ ريا كل شيء طيب رائحته (tahdhib)
- **B011** dişi dağ keçisi — dağ keçisi; özellikle dişisi, bazı kullanımlarda erkeği de · çok sayıda dağ keçisi; dağ keçileri topluluğu · kadın adı
  الإِرْوِيَّة الأنثى من الوعول (sihah)؛ أروى أيضا اسم امرأة (sihah)؛ الأُرْوِيَّة الأنثى من الوعول (tahdhib)؛ يقال للأنثى أروية وللذكر أروية (tahdhib)؛ لا تجمع بين الأروى والنعام (tahdhib)
- **B012** bayrak — bayrak; sancak
  الرَّايَة العلم (sihah)
- **B013** temel uyak harfi — şiir boyunca değişmeyen temel uyak harfi
  الرَّوِيّ حرف القافية (sihah)؛ قصيدتان على روي واحد (sihah)
- **B014** iri damlalı güçlü yağmur bulutu — iri damlalı, sert yağan yağmur bulutu
  الرَّوِيّ سحابة عظيمة القطر شديدة الوقع (sihah)
- **B015** topluluğun ağır yükümlülüklerini üstlenen ileri gelenler — topluluk adına kan bedeli ve ağır yükümlülükleri üstlenen ileri gelenler
  يقال لسادة القوم الروايا (tahdhib)؛ شبه السيد الذي تحمل الديات عن الحي بالبعير الراوية (tahdhib)؛ روايا الثقل حوامل ثقل الديات (tahdhib)

## ء ن س (root_000059): 110:2 ٱلنَّاسَ

- **B001** insan türü ve bu türden bir kişi — insanlar; insan topluluğu · insan; insan türü · insan topluluğunun bir üyesi; insana veya insanlara ait · insanlar; insan toplulukları · insanlar; halk · evde hiç kimse yok · belirli bir ağızda insan ve onun çoğulu
  الإنس خلاف الجن وسموا لظهورهم (maqayis;mufradat)؛ الإنس البشر والواحد إنسي والجمع أناسي (sihah)؛ الإنس جماعة الناس والأناسي جماع (tahdhib)
- **B002** görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma — bir şeyi görmek ve fark etmek · sesi işitmek · onda olgunluk belirtisi görmek ve bunu anlamak · ürken yabani hayvanın birini sezip çevreye bakınması · çevreye bakıp birinin olup olmadığını araştırmak
  آنست الشيء إذا رأيته وآنسته إذا سمعته (maqayis)؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته (sihah)؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه (tahdhib)؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا (mufradat)
- **B003** yabancılık duymadan yakınlık ve rahatlık hissetme — yakınlık ve rahatlık; yabancılık duymama · birine alışıp onun yanında sevinmek · biriyle yakınlık kurmak ve onsuz kendini yalnız hissetmek · yakın arkadaş; rahatlık veren kişi veya şey · yakınlıktan ve söyleşiden hoşlanan genç kadın · insana alışık, saldırgan olmayan köpek · gece yolcusuna veya konaklayana güven veren ateş · sahibine güven veren bütün silahlar; zırh, miğfer, koruyucu örtü ve kalkan gibi savunma donanımları
  الأنس أنس الإنسان بالشيء إذا لم يستوحش منه (maqayis)؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به (sihah)؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور (tahdhib)؛ الأنس خلاف النفور ولكل ما يؤنس به (mufradat)
- **B004** insana dönük yan — bir şeyin insana bakan veya en yakın olan yanı · yayın okçuya bakan yüzü · hayvanın biniciye yakın olan yanı
  الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها (sihah)؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى (tahdhib)؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي (mufradat)
- **B005** göz bebeğinde görülen küçük yansıma — göz bebeğinde görülen küçük görüntü veya yansıma · göz bebeklerinde görülen küçük görüntüler · parmak ucu; eldeki parmak ucunu anlatan kullanım
  إنسان العين صبيها الذي في السواد (maqayis)؛ إنسان العين المثال الذي يرى في السواد أي سواد العين (sihah)؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة (tahdhib)
- **B006** belirli sözlerde kişinin kendisi veya seçilmiş yakını — kendin; kendi durumun nasıl · onun seçkin yakını ve sırdaşı · yakınım, içten dostum ve görüşme arkadaşım
  كيف ابن إنسك إذا سأله عن نفسه (maqayis)؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي (sihah)؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه (tahdhib)؛ قيل ابن إنسك للنفس (mufradat)
- **B007** girişten önce izin ve kabul arama — 
  حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل (tahdhib)؛ حتى تستأنسوا أي تجدوا إيناسا (mufradat)

## د خ ل (root_000464): 110:2 يَدْخُلُونَ

- **B001** içeri girmek veya içeri sokmak — bir yere, zamana veya işe girmek · içeri girme veya giriş · başkasını ya da bir şeyi içeri sokmak · bir şeyin içine azar azar girmek · girme eylemi veya giriş yeri
  أصل مطرد منقاس وهو الولوج (maqayis)؛ دخل يدخل دخولا (maqayis)؛ ادخل في غار وتدخل فيه (ayn)؛ دخلت الدار وغيرها وأدخلت غيري (jamhara)؛ دخلت البيت وادخل وتدخل الشيء (sihah)؛ الدخول نقيض الخروج ويستعمل في المكان والزمان والأعمال (mufradat)
- **B002** eşiyle cinsel birleşmede bulunmak [kalıp] — eşiyle cinsel birleşmede bulunmak
  دخل بامرأته كناية عن الإفضاء إليها (mufradat)
- **B003** içte kalan yan — bir işin veya kişinin iç yüzü · giysinin bedene bakan iç kenarı · saklı tutulan iş veya açılan gizli iç yüz
  الدخلة باطن أمر الرجل وأنا عالم بدخلته (maqayis)؛ الدخلة بطانة من الأمر وعالم بدخلة أمرهم (ayn)؛ دخلل أمري إذا بثثته مكتومك (jamhara)؛ داخلة الإزار طرفه الذي يلي الجسد وداخلة الرجل باطن أمره (sihah)
- **B004** içten bozan kusur — içteki kusur, bozukluk veya kuşku · antları hile ve aldatma aracı yapmak · içten kusurlu, zayıf veya zihni bozuk · içi çürümüş palmiye · böcekçe yenmiş veya kurtlanmış yiyecek
  الدخل العيب في الحسب وكالدغل (maqayis)؛ دخل فلان وهو مدخول إذا كان في عقله دخل ونخلة مدخولة عفنة الجوف (maqayis)؛ عيب في الحسب وفي هذا الأمر دخل ودغل ودخل حسبه أو عقله (ayn)؛ في أمره دخل أي فساد (jamhara)؛ الدخل العيب والريبة ومكرا وخديعة ومدخول في عقله ونخلة مدخولة (sihah)؛ الدخل كناية عن الفساد والعداوة المستبطنة كالدغل ومدخول كناية عن بله في عقله وفساد في أصله (mufradat)
- **B005** sonradan araya katılan kimse — özel işlere alınan veya bir topluluğa dışarıdan katılan kimse · kişinin özel işlerine aldığı yakın kimse · bilmediği işlere zorla karışan kimse
  دخيلك الذي يداخلك في أمورك وبنو فلان في بني فلان دخيل (maqayis)؛ دخيلك الذي تدخله في أمورك ودخلل والمتدخل في الأمور المتكلف فيها (ayn)؛ فلان دخيل في بني فلان إذا كان من غيرهم (jamhara)؛ هم دخل في بني فلان ودخيل الرجل ودخلله الذي يداخله في أموره (sihah)؛ وعن الدعوة في النسب (mufradat)
- **B006** gelir — gelir veya içeri giren kazanç
  الدخل ما دخل ضيعة الإنسان من المنالة (ayn)؛ الدخل خلاف الخرج (sihah)
- **B007** develeri yeniden ya da araya katarak sulama — develeri ikinci kez suya götürme veya susuz deveyi sürüye katma
  الدخال في الورد أن تشرب الإبل ثم ترد إلى الحوض (maqayis)؛ سقيت الإبل دخالا إذا حملتها على الحوض ثانية والدخال في وجه آخر أن تحملها على الحوض بمرة واحدة عراكا (ayn)؛ أورد الرجل إبله دخالا (jamhara)؛ الدخال في الورد أن يشرب البعير ثم يرد من العطن إلى الحوض (sihah)؛ الدخال في الإبل أن يدخل إبل في أثناء ما لم تشرب لتشرب معها ثانيا (mufradat)
- **B008** iç içe geçme ve arada kalma — eklemlerin birbirine geçmesi · bir sinir üzerinde toplanmış et parçası · bir ana renge karışmış başka renkler · kuşun sırtıyla karnı arasındaki tüyler · ağaç köklerinin arasına girmiş ot
  كل لحمة مجتمعة دخلة والدخل من ريش الطائر ما بين الظهران والبطنان والدخل من الكلأ ما دخل منه في أصول الشجر (maqayis)؛ الدخلة في اللون تحليط من ألوان في لون والدخال مداخلة المفاصل بعضها في بعض (ayn)؛ كل لحمة مجتمعة على عصب فهي دخلة (jamhara)؛ الدخل من الكلأ ما دخل منه في أصول الشجر (sihah)
- **B009** sık ağaçlıkta barınan küçük kuş — oyuklarda ve sık ağaç altında barınan küçük kuş · bu küçük kuş adının bir çoğul biçimi · bu küçük kuş adının öteki çoğul biçimi
  بذلك سمي هذا الطائر دخلا (maqayis)؛ الدخل صغار الطير مأواها الغيران وبطون الأودية تحت شجر ملتف والجميع الدخاخيل (ayn)؛ الدخل طائر صغير وجمع دخل دخاخيل (jamhara)؛ الدخل طائر صغير والجمع الدخاليل (sihah)؛ الدخل طائر سمي بذلك لدخوله فيما بين الأشجار الملتفة (mufradat)
- **B010** taze palmiye meyvesi için küçük örgü sepet — taze palmiye meyvesi konan küçük örgü sepet
  الدوخلة سفيفة من خوص صغيرة يجعل فيها الرطب (ayn)؛ الدوخلة هذا المنسوج من الخوص يجعل فيه الرطب (sihah)؛ الدوخلة معروفة (mufradat)

## د ي ن (root_000504): 110:2 دِينِ

- **B001** boyun eğerek uyma ve buna dayalı inanç düzeni — boyun eğme, kulluk ve inanç düzeni · ona boyun eğdi ve buyruğuna uydu · gerçek inanç yolu · hükümdarın buyruğu ya da yargısı
  أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل (maqayis)؛ فالدين الطاعة (maqayis;sihah)؛ الدين لله طاعته والتعبد له (tahdhib)؛ الدين كالملة اعتبارا بالطاعة والانقياد للشريعة (mufradat)
- **B002** yargılayıp hesap görerek karşılığını verme — hesap, yargı ve yapılanın karşılığı · hesap ve karşılık günü · hesaba çekilip karşılığı verilecek olanlar · yargılayan ve karşılığını veren · hükümdarın buyruğu ya da yargısı · kendini alçalttı ya da hesaba çekti
  يوم الدين أي يوم الحكم والحساب والجزاء (maqayis)؛ الدين الجزاء والمكافأة (sihah)؛ الدين الحساب ومنه مالك يوم الدين ومالك يوم الجزاء (tahdhib)؛ غير مدينين أي غير مجزيين (mufradat)
- **B003** borç alıp verme ve vadeli ödeme ilişkisi — borç ve vadeli ödeme yükümlülüğü · onunla borç alıp verme işlemi yaptı · ona ödünç verdi · ödünç aldı ve borçlandı · borçlu veya çok borçlanmış kişi · onu vadeli olarak sattım
  الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء (maqayis)؛ الدين واحد الديون وتداينوا تبايعوا بالدين (sihah)؛ دنت الرجل أقرضته وأدنت الرجل إذا أقرضته (tahdhib)؛ التداين والمداينة دفع الدين (mufradat)
- **B004** zorla alçaltıp egemenliği altına alma — onu alçalttı, boyunduruk altına aldı ve köleleştirdi · topluluğu alçalttım ve köleleştirdim · onu mülk edindim veya buyruğum altına aldım · köleleştirilmiş erkek · köleleştirilmiş kadın · kendini alçalttı ya da hesaba çekti · kalbini alçaltan şey; ayrıca alışkanlık, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz
  العبد مدين كأنهما أذلهما العمل ويا دين قلبك أي أذل (maqayis)؛ دانه دينا أي أذله واستعبده ودينته ملكته (sihah)؛ غير مدينين غير مملوكين ودنت القوم أدينهم إذا أذللتهم (tahdhib)؛ المدين والمدينة العبد والأمة (mufradat)
- **B005** alışılmış davranış ve öteden beri bilinen hal — alışkanlık, olağan iş ve öteden beri bilinen hal · kalbinin alışkanlığı; ayrıca alçaltma, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz
  العادة يقال لها دين (maqayis)؛ الدين بالكسر العادة والشأن (sihah)؛ الدين أيضا العادة (tahdhib)؛ الحال والأمر الذي تعهده (maqayis)
- **B006** kent — kent; yöneticilerin buyruğuna uyulan yer olarak açıklanan büyük yerleşim
  المدينة كأنها مفعلة سميت بذلك لأنها تقام فيها طاعة ذوي الأمر (maqayis)؛ ومنه سمى المصر مدينة (sihah)؛ جعل بعضهم المدينة من هذا الباب (mufradat)
- **B007** kişiyi sözüne ve vicdani sorumluluğuna göre değerlendirme — onu vicdani yükümlülüğüyle baş başa bıraktı · yargıda veya Tanrı'yla arasındaki konuda sözünü doğru kabul etti · yeminini kendi niyetine göre değerlendirdi
  دينت الرجل تديينا إذا وكلته إلى دينه (sihah)؛ دينت الرجل في القضاء وفيما بينه وبين الله أي صدقته (tahdhib)؛ دينت الحالف أي نويته فيما حلف وهو التديين (tahdhib)

## ف و ج (root_001184): 110:2 أَفْوَاجًا

- **B001** insan topluluğu — insan topluluğu · insan toplulukları · çok sayıda insan topluluğu · çok sayıda insan topluluğu · insan toplulukları · art arda gelen topluluklar · grup grup, art arda
  كلمة تدل على تجمع؛ الفوج الجماعة من الناس والجمع أفواج وجمع الجمع أفاوج وأفاويج (maqayis)؛ الفوج القطيع من الناس والجميع الأفواج (ayn)؛ الفوج من الناس الجماعة والجمع أفواج وجمع أفواج أفاوج وأفاويج (jamhara)؛ الفوج الجماعة من الناس والجمع فؤوج وأفواج وجمع الجمع أفاوج وأفاويج (sihah)؛ جماعات كثيرة والفوج قطيع من الناس وجمعه أفواج والفيوج جماعة والفيج الجماعة من الناس وأفائج وأفاوج يجمع أفواج أي فوجا بعد فوج (tahdhib)؛ الفوج الجماعة المارة المسرعة وجمعه أفواج (mufradat)
- **B002** iki yükselti arasındaki geniş açıklık — iki yükselti arasındaki geniş açıklık · yükseltiler arasındaki geniş açıklıklar · geniş düz arazi
  الفائجة متسع ما بين كل مرتفعين من غلظ أو رمل (sihah)؛ الفوائج متسع ما بين كل مرتفعين من غلظ أو رمل والفائج البساط الواسع من الأرض (tahdhib)

## س ب ح (root_000666): 110:3 فَسَبِّحْ

- **B001** Tanrı'yı yücelterek anma ve kulluk — dua ve anma biçimindeki gönüllü kulluk · Tanrı'yı sözle, eylemle veya niyetle yüceltme ve anma
  السُّبحة وهي الصلاة (maqayis)؛ التسبيح يكون في معنى الصلاة (ayn)؛ سبح الرجل تسبيحا إذا عظم الله ومجده (jamhara)؛ السبحة التطوع من الذكر والصلاة (sihah)؛ السبحة من الصلاة التطوع (tahdhib)؛ التسبيح عاما في العبادات قولا كان أو فعلا أو نية (mufradat)
- **B002** Tanrı'yı her türlü eksiklikten uzak sayma — Tanrı her türlü kötülük ve eksiklikten uzaktır · Tanrı'yı her türlü kötülük ve eksiklikten uzak sayarak yüceltme · şaşma veya söz konusu kişiyi bir iddiadan uzak tutma sözü · her türlü kötülükten ve kendisine yakışmayan nitelikten uzak olan Tanrı
  التسبيح وهو تنزيه الله من كل سوء (maqayis)؛ سبحان الله تنزيه لله (ayn)؛ سبحان تنزيه وتبرئة (jamhara)؛ التسبيح التنزيه (sihah)؛ سبحان في اللغة تنزيه لله عز وجل عن السوء (tahdhib)؛ التسبيح تنزيه الله تعالى (mufradat)
- **B003** Tanrı'nın yüzünün görkemi, büyüklüğü ve ışığı — Tanrı'nın yüzünün görkemi, büyüklüğü ve ışığı · yere kapanma yerleri
  السبحات جلال الله وعظمته (maqayis)؛ سبحات وجه ربنا يعني جلاله وعظمته ونوره (ayn)؛ سبحات وجهه نور وجهه (jamhara)؛ سبحات وجه ربنا أي جلالته (sihah)؛ سبحات وجهه نور وجهه؛ السبحات مواضع السجود (tahdhib)
- **B004** yüzerek veya akıcı biçimde hızla ilerleme — yüzme ve su ya da havada hızla ilerleme · yıldızların yörüngede akıp ilerlemesi · ön ayaklarını ileri uzatarak koşan at · yörüngede ya da koşuda hızla akıp gidenler
  السَّبح والسباحة العوم في الماء (maqayis)؛ السبح مصدر كالسباحة سبح السابح في الماء (ayn)؛ سبح الرجل وغيره في الماء سبحا وسباحة (jamhara)؛ السباحة العوم (sihah)؛ النجوم تسبح في الفلك؛ السابح من الخيل يمد يديه في الجري (tahdhib)؛ السبح المر السريع في الماء وفي الهواء (mufradat)
- **B005** iş ve geçim için zaman ve hareket imkânı — serbest zaman, geçim için hareket ve gidip gelme imkânı · yeryüzünde uzaklara gitmek · sözü uzatıp çok konuşmak
  أصلان أحدهما جنس من العبادة والآخر جنس من السعي (maqayis)؛ سبحا طويلا أي فراغا للنوم (ayn)؛ السبح الفراغ والتصرف في المعاش والمنقلب والجيئة والذهاب (sihah)؛ فراغا وتصرفا؛ اضطرابا ومعاشا؛ منقلبا طويلا (tahdhib)؛ سرعة الذهاب في العمل (mufradat)
- **B006** anma sözlerini saymaya yarayan boncuk dizisi — Tanrı'yı anma sözlerini saymaya yarayan boncuk dizisi
  السبحة خرزات يسبح بعدها (ayn)؛ السبحة بالضم خرزات يسبح بها (sihah)؛ الخرزات التي يعد بها المسبح تسبيحه السبحة وهي كلمة مولدة (tahdhib)؛ الخرزات التي بها يسبح سبحة (mufradat)
- **B007** çocuk deri giysisi; güçlü ve sıkı örtü — çocuklar için deriden yapılmış gömlek veya giysi · güçlü, sağlam ve sıkı örtü
  السبحة قميص يعمل للصبيان من جلود وسلف رقيق والجمع سباح (jamhara)؛ السبحة بفتح السين وجمعها سباح ثياب من جلود؛ السباح قمص للصبيان من جلود؛ كساء مسبح أي قوي شديد (tahdhib)
- **B008** kutsal kent veya hac bölgesindeki bir vadinin adı — kutsal kent ya da hac sırasında durulan bölgedeki bir vadinin adı
  سَبّوحة البلد الحرام ويقال واد بعرفات (sihah)

## ح م د (root_000355): 110:3 بِحَمْدِ

- **B001** yermenin karşıtı olan, iyilik için teşekkürü de kapsayan övgü — yermenin karşıtı olan övgü; iyilik için teşekkür de içerebilir · birini, yaptığı övülesi bir işten dolayı övmek · övgü; yerginin karşıtı · Tanrı'yı güzel sözlerle çokça övme · onun için övgü ve teşekkür · övülecek bir iş yapmak ya da sonunda övgü kazanmak · her şeyi çokça, kimi zaman olduğundan fazla öven kimse · çok öven kimse · seni överek başlarım
  الحمد نقيض الذم (maqayis;ayn;jamhara;sihah;tahdhib)؛ الحمد الثناء (ayn;tahdhib;mufradat)؛ الحمد أعم من الشكر (sihah;mufradat)؛ التحميد كثرة حمد الله بحسن المحامد (ayn;tahdhib)
- **B002** deneyip övülesi ya da uygun bulma — birini deneyip övgüye değer bulmak · bir yeri yerleşmeye ya da otlatmaya elverişli bulmak · bu işi benim için uygun buluyor musun? · idrar kanalını yıkamayı sizin için uygun bulmak
  أحمدت فلانا إذا وجدته محمودا (maqayis;ayn;sihah;tahdhib)؛ أحمدت الأرض إذا رضيت سكناها أو مرعاها (jamhara;sihah)؛ هل تحمد لي هذا الأمر أي هل ترضاه لي (tahdhib)
- **B003** övülen veya birçok övülesi niteliği bulunan kimse — övülen, övgüye değer · çokça övülen, birçok övülesi niteliği bulunan · övülmeye daha çok layık olan ya da daha çok öven · övülen; bağlama göre öven
  رجل محمود ومحمد إذا كثرت خصاله المحمودة (maqayis;sihah)؛ محمد كأنه حمد مرة بعد أخرى (jamhara)؛ فلان محمود إذا حمد ومحمد إذا كثرت خصاله المحمودة (mufradat)؛ الحميد بمعنى المحمود (tahdhib;mufradat)
- **B004** övülesi işin varılabilecek en ileri sınırı — yapabileceğinin en ilerisi ve övülecek olanı · aktarılan sözde kadınlarda övülebilecek niteliklerin en ileri derecesi
  حماداك أن تفعل كذا أي غايتك وفعلك المحمود (maqayis)؛ حماداك أن تفعل كذا أي حمدك (ayn;tahdhib)؛ حماداك في معنى قصاراك (jamhara;sihah)؛ حماديات النساء معناه غاية ما يحمد منهن (tahdhib)؛ حماداك أي غايتك المحمودة (mufradat)
- **B005** iyiliğini başa kakıp kendine pay çıkarma [kalıp] — iyiliğini insanların başına kakıp bununla övgü beklemek
  فلان يتحمد علي أي يمن (sihah)؛ من أنفق ماله على نفسه فلا يتحمد به إلى الناس (sihah;tahdhib)
- **B006** muhatabı katarak övme veya iyilikleri teşekkürle anma [kalıp] — seninle birlikte Tanrı'yı övmek veya onun iyiliklerini sana teşekkürle anmak
  أحمد إليك الله أي معك (ayn;tahdhib)؛ أشكر إليك أياديه ونعمه (tahdhib)

## ر ب ب (root_000532): 110:3 رَبِّكَ

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

## ECHO ر ب و (root_000537): for 110:3 رَبِّكَ: withheld observed target; not identity

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

## غ ف ر (root_001096): 110:3 وَٱسْتَغْفِرْهُ

- **B001** koruyucu biçimde örtme — örtme ve koruyucu biçimde kaplama · başı koruyan zincir örgülü zırh başlığı · baş yağı bulaşmasın diye başörtüsünün altına konan bez · yay kirişinin geçtiği çentiği örten yama · alttaki bulutu örten üst bulut · eşyayı bir kaba koymak · boyanın kumaşı kiri daha iyi gizler duruma getirmesi · işi gereken biçimde örtüp düzeltmek · enseden sarkan saçı örtmek
  الغفر الستر (maqayis)؛ أصل الغفر التغطية (ayn)؛ الغفر: التغطية (sihah)؛ الغفر: إلباس ما يصونه عن الدنس (mufradat)؛ المغفر وقاية للرأس (ayn)؛ المغفر: زرد ينسج من الدروع على قدر الرأس (sihah)؛ اغفروا هذا الأمر بغفرته أي استروه بما يجب أن يستر به (mufradat)
- **B002** suçu bağışlayıp cezadan koruma — suçu bağışlama ve ceza sonucundan koruma · suçu bağışlayıp cezasını kaldırma · Tanrı'nın suçu bağışlayıp kulunu cezadan koruması · suçu bağışlama · Tanrı'nın onun suçunu bağışlaması · onu bağışlamak · Tanrı'dan bağışlanma dilemek · suçu bağışlamak · çok bağışlayan · sürekli ve çok bağışlayan · içlerinde kimsenin suçunu bağışlayan yok
  الغفران والغفر بمعنى (maqayis)؛ الله الغفور الغفار يغفر الذنوب مغفرة وغفرانا وغفرا (ayn)؛ استغفر الله لذنبه ومن ذنبه فغفر له ذنبه مغفرة وغفرا وغفرانا (sihah)؛ المغفرة من الله هو أن يصون العبد من أن يمسه العذاب (mufradat)
- **B003** yüzeyi kaplayan ince tüy veya kumaş havı — kumaşın havı kalkıp yüzünü kaplamak · kumaş havı ya da bedendeki ince tüy · ince tüy · enseden aşağı sarkan saç · enseden sarkan saçı örtmek
  غفر الثوب إذا ثار زئبره وهو من الباب لأن الزئبر يغطي وجه الثوب (maqayis)؛ غفر الثوب إذا ثار زئبره غفرا (ayn)؛ الغفر أيضا شعر كالزغب يكون على ساق المرأة والجبهة ونحو ذلك؛ والغفر أيضا زئبر الثوب (sihah)
- **B004** yaranın veya hastanın yeniden kötüleşmesi [kalıp] — yara yeniden kötüleşti · hasta yeniden kötüleşti
  الغفر النكس في المرض (maqayis)؛ غفر الجرح يغفر غفرا: نكس، وكذلك المريض (sihah)
- **B005** dağ keçisi yavrusu ve annesi — dağ keçisi yavrusu · yavrunun annesi olan dişi dağ keçisi · dağ keçisi yavrusunun annesi
  الغفر ولد الأروية وأمه مغفر (maqayis)؛ الغفر ولد الأروية؛ والمغفر الأروية ويقال لها أم غفر (ayn)؛ الغفر بالضم: ولد الأروية، والجمع الأغفار، وأمه مغفرة (sihah)
- **B006** Ay'ın konaklarından olan üç küçük yıldız — Ay'ın konaklarından olan üç küçük yıldız
  الغفر من منازل القمر (ayn)؛ الغفر: ثلاثة أنجم صغار ينزلها القمر، وهي من الميزان (sihah)
- **B007** ağaçtan çıkan veya toplanan ürün — ağaçtan çıkan ürün; reçine benzeri madde veya tatlı kurt · ağaçtan çıkan ve toplanan ürünler · ağaç ürünlerini aramaya çıkmak · ağaç ürünü toplamaya çıkmak
  المغفور فشىء يشبه بالصمغ يخرج من العرفط (maqayis)؛ المغفور دود يخرج من العرفط حلو يضيح بالماء فيشرب؛ وصمغ الإجاصة مغفور (ayn)؛ ما أحسن مغافير هذا الرمث؛ خرجنا نتمغفر؛ خرجنا نتغفر، إذا خرجوا يجتنونه من شجرة (sihah)
- **B008** bütün topluluğun kalabalık ve eksiksiz gelişi [kalıp] — bütün topluluk, kalabalık ve kimse eksik olmadan · bütün toplulukla birlikte · hep birlikte ve kalabalık olarak
  جاء القوم جماء الغفير أي بلفهم ولفيفهم (ayn)؛ جاءوا جماء غفيراء؛ والجماء الغفير، وجم الغفير، وجماء الغفير، أي جاءوا بجماعتهم: الشريف والوضيع، ولم يتخلف أحد، وكانت فيهم كثرة (sihah)

## ك و ن (root_001332): 110:3 كَانَ

- **B001** gerçekleşme, bulunma ve olma bildirimi — gerçekleşip ortaya çıkmak veya hazır bulunmak · geçmişte bir durumu bildirmek · oluş; gerçekleşme · olma, oluş · sonradan gerçekleşen iş · yüklemi pekiştiren ek söz · birini geliş kapsamı dışında tutan bağlı söz · var edip gerçekleşmesini sağlamak
  الكون الحدث يكون بين الناس ومصدر من كان يكون؛ الكينونة في مصدر كان؛ الكائنة الأمر الحادث (ayn); كان عبارة عما مضى من الزمان؛ حدوث الشيء ووقوعه؛ كان الأمر أي مذ خلق؛ تقع زائدة للتوكيد؛ لا يكون زيدا تعني الاستثناء؛ كونه فتكون أحدثه فحدث (sihah); أصل يدل على الإخبار عن حدوث شيء إما في زمان ماض أو زمان راهن؛ كان الشيء يكون كونا إذا وقع وحضر (maqayis)
- **B002** bulunma yeri ve konum değeri — bulunulan yer · yerler · konum, düzey veya bulunulan yer · birinin yanında güçlü konumu olan · yerleşmek veya güç kazanmak · birinin yanında şu yer veya düzeyde bulunmak
  المكان اشتقاقه من كان يكون؛ تمكن (ayn;maqayis); فلان مني مكان هذا؛ موضع العمامة (ayn); المكانة المنزلة؛ مكين عند فلان بين المكانة؛ المكان والمكانة الموضع؛ تمكن (sihah)
- **B003** birini güvenceyle üstlenme — başkası için güvence üstlenme · birini üstlenmek · birine güvence olmak
  الكيانة الكفالة؛ كنت على فلان أكون كونا أي تكفلت به؛ اكتنت به اكتيانا مثله (sihah); كنت على فلان أكون عليه إذا كفلت به؛ اكتنت أيضا اكتيانا (maqayis)
- **B004** boyun eğme — boyun eğme
  الاستكانة الخضوع (sihah)
- **B005** gençliğini anan yaşlı kişi — gençken şöyleydim diye anlatan yaşlı kişi
  يقال للرجل إذا شاخ كُنْتِيّ؛ كأنه نسب إلى قوله كُنْتُ في شبابي كذا وكذا (sihah)
- **B006** kötü durumda gece geçirme [kalıp] — geceyi kötü durumda geçirmek
  الكينة في قولهم بات فلان بكينة سوء أي بحال سوء فأصله الكون فعلة من الكون (maqayis)

## ت و ب (root_000189): 110:3 تَوَّابًۢا

- **B001** yanlistan Tanri'ya donus — yanlisindan donup Tanri'ya yoneldi · yanlistan donme, pismanlikla birakma · yanlistan donme eylemi · Tanri'ya tam bir donus · Tanri'ya donen kisi · Rabbine sikca donen kul · yaraticiniza donun
  كلمة واحدة تدل على الرجوع (maqayis)؛ التوب مصدر تاب يتوب توبا (jamhara)؛ التوبة الرجوع من الذنب (sihah)؛ تاب عاد إلى الله ورجع وأناب (tahdhib)؛ التوب ترك الذنب على أجمل الوجوه (mufradat)
- **B002** Tanri'nin donusu kabul etmesi — Tanri onun donusunu kabul etti ve bagisladi · kullarin donusunu cokca kabul eden Tanri · Tanri kulunun donusunu kabul edendir
  وقد تاب الله عليه وفقه لها (sihah)؛ تاب الله عليه أي عاد عليه بالمغفرة (tahdhib)؛ تاب الله عليه أي قبل توبته (mufradat)؛ التواب من صفات الله هو الذي يتوب على عباده (tahdhib)؛ يقال ذلك لله تعالى لكثرة قبوله توبة العباد (mufradat)
- **B003** donuse cagirma — ondan yanlisindan donmesini istedi veya bunu teklif etti
  استتابه سأله أن يتوب (sihah)؛ استتبت فلانا أي عرضت عليه التوبة مما اقترف (tahdhib)
- **B004** hafifletmeye dondurme — sizi hafifletmeye dondurdu veya onceki yasagi serbest kildi
  فتاب عليكم أي رجع بكم إلى التخفيف (tahdhib)؛ أي أباح لكم ما كان حظر عليكم (tahdhib)

## ECHO ت ب ب (root_000172): for 110:3 تَوَّابًۢا: withheld observed target; not identity

- **B001** kayıp ve yok oluş — kayıp, yok oluş ve kaybın sürmesi · kayba uğradı veya yok oldu · elleri kayba uğradı; gücü boşa çıktı · ona yok oluş ve kayıp olsun · ona yok oluş diledim · kayba uğratma veya yok etme
  التباب الخسران (maqayis)؛ تبا للكافر أي هلاكا له (maqayis)؛ تبت يداه تبا وتبابا أي خسرت (jamhara)؛ التباب الخسران والهلاك (sihah)؛ تببوهم تتبيبا أي أهلكوهم (sihah)؛ التب الخسار وتبا لفلان على الدعاء (tahdhib)؛ وما زادوهم غير تتبيب أي تخسير (maqayis;tahdhib;mufradat)؛ التب والتباب الاستمرار في الخسران (mufradat)
- **B002** düzene girip süreklilik kazanma [kalıp] — iş hazır olup düzene girdi ve belli oldu · o şey onun için sürdü · açık, belirgin ve düzgün yol
  استتب الأمر إذا تهيأ (maqayis;sihah)؛ استتب أمر فلان إذا اطرد واستقام وتبين (tahdhib)؛ الطريق المستتب الواضح البين المستقيم (tahdhib)؛ استتب لفلان كذا أي استمر (mufradat)
- **B003** yaşlılık ve bedensel yıpranma — zayıf veya yaşlı adam · zayıf erkekler topluluğu · yaşlı kadın · sırtı yara olmuş eşek veya deve · yaşlandı
  رجل تاب ضعيف والجميع الإتباب؛ التابة الكبيرة ورجل تاب أي كبير؛ حمار تاب الظهر إذا دبر وجمل تاب كذلك؛ تبتب إذا شاخ
- **B004** kesmek — kesti
  تب إذا قطع



===== _commentary/v16/work/s110/surah.r2.nochannels.hftbundle/hft.md =====
# HFT: earlier activation hypotheses, per focus ayah of surah 110

Note: HFT used an older root map; a trace step on a root the gateway now withholds is an echo, not identity.

# Focus 110:1

## arrival aperture
- reading: A threshold mechanism in which enabling aid becomes present and a blocked field becomes traversably open.
- mechanism: Aid becomes present, then a formerly closed state is rendered open. The coordination keeps enabling support and opened outcome distinguishable rather than reducing both nouns to one generic victory label.
- trace:
  - 110:1 **جَآءَ** ج ي ء B001: Coming and arrival supply the threshold at which aid becomes present rather than remaining a static possession.
  - 110:1 **نَصْرُ** ن ص ر B001: Aid that makes someone prevail supplies the enabling force of the event.
  - 110:1 **ٱللَّهِ** ء ل ه B002: The fixed divine name identifies the aid's source and prevents an unnamed human actor from absorbing that role.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B001: Opening a closure and widening an aperture supply the changed state paired with the arriving aid.

## adjudicated redress
- reading: Victory can also be a divinely authorized redress that closes oppression by settling what had remained judicially locked.
- mechanism: The paired nouns can describe a juridical event: divine redress arrives and an unresolved conflict is decisively opened by adjudication. This coexists with, rather than cancels, the military-prevailing reading.
- trace:
  - 110:1 **جَآءَ** ج ي ء B001: Arrival supplies the moment at which a previously pending settlement takes effect.
  - 110:1 **نَصْرُ** ن ص ر B002: Redress after oppression recasts aid as the restoration of a wronged party.
  - 110:1 **ٱللَّهِ** ء ل ه B002: The fixed divine name locates the authority of the redress beyond the disputants.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B003: Judgment that resolves a closed dispute supplies the decisive settlement paired with redress.

## gifted inner opening
- reading: Aid may arrive as a divine gift that relieves an inward closure and makes knowledge, guidance, or possibility accessible.
- mechanism: Aid is not only force against an opponent; it can arrive as a presented gift whose effect is to remove an inward obstruction and disclose a way forward.
- trace:
  - 110:1 **جَآءَ** ج ي ء B004: Bringing or presenting something lets the arrival be heard as the presentation of an effective good.
  - 110:1 **نَصْرُ** ن ص ر B005: Granting a gift supplies the beneficent substance of the arriving aid.
  - 110:1 **ٱللَّهِ** ء ل ه B001: Worship and the worshipped one keep the gift relationally directed toward devotion rather than mere advantage.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B008: Relief, insight, and disclosure supply the inward effect of the granted aid.

## hydraulic relief
- reading: Divine aid behaves like relieving water: it arrives through tributaries, gathers, and becomes effective when an outlet is opened.
- mechanism: As a material analogy, distant channels bring relieving rain into a gathering place and an opened outlet releases it. The coherence across جاء، نصر، and فتح makes this more than a free-standing water theme, though it remains branch-distant from the surface construction.
- trace:
  - 110:1 **جَآءَ** ج ي ء B003: A hollow where water gathers supplies the receiving basin of the material mechanism.
  - 110:1 **نَصْرُ** ن ص ر B004: Rain that relieves and makes land grow supplies aid as life-giving water.
  - 110:1 **نَصْرُ** ن ص ر B007: Tributary channels arriving from afar supply the conveyance that gathers relief at the threshold.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B005: Water released from an outlet supplies the transition from gathered potential to distributed effect.

## publicly legible threshold
- reading: Its arrival becomes recognizable by a public social change: cohorts of humans visibly traverse the newly opened field.
- mechanism: The threshold in 110:1 acquires a public diagnostic in 110:2: it is seen and sensed through human cohorts, so the opening is socially legible rather than an invisible transfer of power.
- trace:
  - 110:1 **جَآءَ** ج ي ء B001: Arrival supplies the event whose occurrence needs a perceptible marker.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B001: A widened opening supplies the changed condition that can become visible in what passes through it.
  - 110:2 **وَرَأَيْتَ** ر ء ي B001: Seeing by eye or insight supplies direct recognition of the event's manifested effect.
  - 110:2 **ٱلنَّاسَ** ن و س B002: Sensing or detecting a thing makes the human presence function as evidence rather than background population.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Groups of people supply repeated, collective units through which the opening becomes publicly legible.

## permeable communal entry
- reading: Opening means a boundary becoming permeable enough for formerly estranged people to enter a shared practice of obedience in groups.
- mechanism: The conquest-like opening is revised into permeability: estranged humans can cross an enlarged threshold into a domain of obedience. Success is measured by access and participation, not by keeping an enemy outside.
- trace:
  - 110:1 **نَصْرُ** ن ص ر B001: Prevailing aid supplies the power that removes the prior barrier.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B001: A widened aperture supplies the permeable boundary through which the social result occurs.
  - 110:2 **ٱلنَّاسَ** ن و س B003: Sociability that removes estrangement recasts the people as a relation newly made possible by the opening.
  - 110:2 **يَدْخُلُونَ** د خ ل B001: Literal entry into an interior supplies the crossing action.
  - 110:2 **دِينِ** د ي ن B001: Obedience and willing compliance supply the domain entered rather than a territory merely occupied.
  - 110:2 **أَفْوَاجًا** ف و ج B002: The broad gap reinforces the opening as an aperture enlarged enough for collective passage.

## inward entry with surface risk
- reading: The opening permits both outward passage and possible inward assent, while leaving a diagnostic gap in which display or hidden corruption can coexist with the visible success.
- mechanism: Visible entry has two live depths. It can be an inner opening into entrusted commitment, but the same publicly seen movement can stop at display; the success of 110:1 therefore cannot be exhausted by counting visible entrants.
- trace:
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B008: Inner opening by guidance or disclosure supplies the possible depth beneath outward passage.
  - 110:2 **وَرَأَيْتَ** ر ء ي B005: Showing oneself before people supplies the live possibility that a visible entry is performative.
  - 110:2 **يَدْخُلُونَ** د خ ل B003: The inward or secret dimension supplies a depth not settled by exterior observation.
  - 110:2 **يَدْخُلُونَ** د خ ل B004: Hidden corruption supplies a contrary interior state that may coexist with successful outward entry.
  - 110:2 **دِينِ** د ي ن B007: Assent and entrustment supply the positive inward realization of entry.

## source destination circuit
- reading: What comes from Allah remains oriented back toward Allah as people enter divine obedience; the event resists appropriation as human capital.
- mechanism: The repeated divine name links source and destination: aid is of Allah, and the entered obedience is of Allah. Victory is thus a circuit returning bestowed capacity toward worship, not an asset transferred into human ownership.
- trace:
  - 110:1 **نَصْرُ** ن ص ر B005: Aid as a granted good supplies what moves from source toward social effect.
  - 110:1 **ٱللَّهِ** ء ل ه B001: The worshipped one supplies the divine source to whom the aid already belongs.
  - 110:2 **دِينِ** د ي ن B001: Obedience supplies the relational mode into which the social movement enters.
  - 110:2 **ٱللَّهِ** ء ل ه B001: The repeated worshipped one supplies the destination of that obedience and closes the circuit.

## inhabited accountable order
- reading: The settlement opens an accountable order that groups can enter and inhabit, so justice becomes a social arrangement rather than a terminating verdict.
- mechanism: The baseline juridical settlement becomes an inhabitable order. Redress and judgment do not merely end a dispute; cohorts enter a city-like domain of obedience and reckoning, turning verdict into durable social form.
- trace:
  - 110:1 **نَصْرُ** ن ص ر B002: Redress after oppression supplies the justice claim behind the new order.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B003: Adjudication supplies the decisive settlement from which an accountable order can begin.
  - 110:2 **يَدْخُلُونَ** د خ ل B001: Entry into an interior makes the settled order something people inhabit.
  - 110:2 **دِينِ** د ي ن B002: Accounting and recompense supply the order's answerability rather than mere allegiance.
  - 110:2 **دِينِ** د ي ن B006: The city of obedience supplies a civic-spatial image for the domain entered.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Human cohorts supply the population by which the verdict becomes social order.

## opening as postvictory beginning
- reading: The opening begins a post-victory formation in which worship, repair, maturation, and a praiseworthy end still have to unfold.
- mechanism: The opening is not the end-state but the beginning that opens what follows: worship, a praiseworthy aim, nurture, completion, and growth. The conqueror's task changes from obtaining the event to being formed after it.
- trace:
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B002: An opening beginning that unlocks what follows makes victory the first phase rather than the finish.
  - 110:3 **فَسَبِّحْ** س ب ح B001: Worship through glorification and prayer supplies the first discipline opened by the event.
  - 110:3 **بِحَمْدِ** ح م د B004: The praiseworthy end supplies a telos beyond simply obtaining victory.
  - 110:3 **رَبِّكَ** ر ب ب B002: Nurture, repair, and completion supply the formative work required after opening.
  - 110:3 **رَبِّكَ** ر ب ب B005: The non-dominant split image of nourishment and growth extends completion into an exploratory organic process.

## antiboast guard
- reading: The opening is also an attributional test: its visibility can feed self-display, so its proper completion requires praise redirected to the Lord and protection from self-credit.
- mechanism: A publicly visible opening carries a semantic shadow of display and self-credit. Glorification, praise, and seeking protective forgiveness function as a guard against converting divine aid into the victor's boast.
- trace:
  - 110:1 **ٱللَّهِ** ء ل ه B001: The worshipped one fixes the proper object of devotion and attribution.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B009: Boastful display of wealth or learning supplies the dangerous shadow carried by an achieved opening.
  - 110:2 **وَرَأَيْتَ** ر ء ي B005: Showing oneself before people makes public visibility the setting in which self-display can arise.
  - 110:3 **فَسَبِّحْ** س ب ح B002: Declaring transcendence and clearing from fault redirects the event away from human self-magnification.
  - 110:3 **بِحَمْدِ** ح م د B005: Claiming praise by conferring a favor names the precise appropriation risk that praise of the Lord reverses.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B002: Covering a fault and protecting its bearer from its effect supplies remediation for the victor's attributional failure.

## open then protect
- reading: Success is selective permeability: the boundary opens for entry but must also be protected against harms that openness can carry inward.
- mechanism: فتح and غفر create a controlled-boundary paradox. The aperture must open for entry, yet opening also permits hidden corruption or an alien element to mingle; protective covering is therefore part of governing, not undoing, permeability.
- trace:
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B001: A widened aperture supplies the necessary but potentially vulnerable boundary condition.
  - 110:2 **يَدْخُلُونَ** د خ ل B004: Hidden corruption supplies a possible adverse interior effect of successful entry.
  - 110:2 **يَدْخُلُونَ** د خ ل B005: An outsider who mingles with a group supplies the permeability risk without negating genuine entrants.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B001: Covering that preserves and protects supplies the counter-operation that makes openness governable.

## event within enduring return
- reading: A punctual opening occurs inside enduring lordship and begins repeated reorientation; the event is real but not self-sufficient or terminal.
- mechanism: The punctual coming of 110:1 is nested within continuity in 110:3. The opening starts what follows, while enduring lordship and the solicitation of return prevent the event from closing history into a completed triumph.
- trace:
  - 110:1 **جَآءَ** ج ي ء B001: Arrival supplies the bounded event that occurs at a threshold in time.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B002: An opening beginning supplies the event's forward-facing rather than terminal aspect.
  - 110:3 **رَبِّكَ** ر ب ب B007: Abiding, residence, and continuance supply durable lordship around the punctual event.
  - 110:3 **كَانَ** ك و ن B001: Occurrence and presence in time make the closing description explicitly temporal.
  - 110:3 **تَوَّابًۢا** ت و ب B003: Calling another to repent supplies an ongoing invitation to return after the opening.

## social irrigation
- reading: The opening distributes divine relief into social growth: cohorts move through it as differentiated flows through a widened, life-giving channel.
- mechanism: The baseline water network acquires a social-ecological extension: rain and tributaries reach an opened channel, cohorts move through a broad gap like distributed flow, and the result is nurture and growth. The people are not equated with water; flow is the reader-supplied analogy linking the packet's material branches.
- trace:
  - 110:1 **جَآءَ** ج ي ء B003: The water-gathering hollow supplies the catchment into which distant relief converges.
  - 110:1 **نَصْرُ** ن ص ر B004: Relieving rain that causes growth supplies the life-giving input.
  - 110:1 **نَصْرُ** ن ص ر B007: Tributaries bringing water from afar supply convergence and distribution.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B005: Water released through an opening supplies controlled outflow from the achieved threshold.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Human groups supply the distributed social units carried by the analogy.
  - 110:2 **أَفْوَاجًا** ف و ج B002: A broad gap supplies the channel widened for grouped passage.
  - 110:3 **فَسَبِّحْ** س ب ح B004: Running or swimming supplies movement through a medium rather than static accumulation.
  - 110:3 **رَبِّكَ** ر ب ب B008: Rain-bearing cloud supplies an upstream ecological counterpart to the rain-relief branch.
  - 110:3 **رَبِّكَ** ر ب ب B005: The split image of nourishment and growth supplies the downstream effect of distributed flow.

## victory becomes report
- reading: As a contained split-root afterimage, victory also becomes transmissible narrative: an arrival that can be carried beyond those who directly saw it.
- mechanism: 
- trace:
  - 110:1 **جَآءَ** ج ي ء B001: Arrival supplies the event that can subsequently become reportable.
  - 110:1 **نَصْرُ** ن ص ر B001: Prevailing aid supplies the event-content carried into public memory.
  - 110:2 **وَرَأَيْتَ** ر ء ي B003: The split-root image of transmitting news or poetry supplies a secondary movement from witnessed event to narrated event.

## wound drainage and relapse
- reading: As a contained wound analogy, redress opens and releases accumulated injury, while the command that follows guards against relapse after the dramatic relief.
- mechanism: 
- trace:
  - 110:1 **جَآءَ** ج ي ء B006: Collected matter from a wound supplies the image of injury that has accumulated to a point of release.
  - 110:1 **نَصْرُ** ن ص ر B002: Redress after oppression supplies the social injury for which release would count as relief.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B001: Opening a closure supplies drainage or exposure of what had been trapped.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B004: Relapse of illness or wound supplies the warning that opening and relief do not eliminate the need for aftercare.

## opening as cutover
- reading: As a contained split-root shadow, the opening is a cutover: it begins a new orientation by severing continuity with the configuration that preceded it.
- mechanism: 
- trace:
  - 110:1 **جَآءَ** ج ي ء B001: Arrival supplies the threshold at which the transition takes effect.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B002: An opening beginning supplies the new phase initiated at the threshold.
  - 110:3 **تَوَّابًۢا** ت و ب B004: The split-root cutting image supplies a contained severance of the prior order that makes return a genuine reorientation.


# Focus 110:2

## visible successive ingress
- reading: A witnessed and still-unfolding transfer carries successive human cohorts across a boundary into God's order of worship and obedience.
- mechanism: Direct perception, boundary crossing, obedience, and grouped succession combine into a process rather than a census: human cohorts are visibly passing from outside to inside an order of worship.
- trace:
  - 110:2 **وَرَأَيْتَ** ر ء ي B001: Supplies sensory or insightful witnessing and makes the transition an observed event.
  - 110:2 **ٱلنَّاسَ** ن و س B001: Keeps the moving collectivity specifically human and publicly manifest.
  - 110:2 **يَدْخُلُونَ** د خ ل B001: Provides literal passage across a boundary into an interior.
  - 110:2 **دِينِ** د ي ن B001: Defines the entered domain functionally as worship, obedience, and submission.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Segments the influx into bands arriving one after another rather than isolated persons.

## public threshold private interior
- reading: The verse certifies public boundary crossing while leaving inward integration open; visible membership and interior condition coexist without becoming identical.
- mechanism: Visible appearance and sensory detection establish public ingress, but entering also creates an interior that sight does not automatically disclose. The scene therefore distinguishes observable inclusion from inward integration.
- trace:
  - 110:2 **وَرَأَيْتَ** ر ء ي B006: Foregrounds visible appearance and the surface available to an observer.
  - 110:2 **ٱلنَّاسَ** ن و س B002: Contributes recognition through sight, sensation, or hearing as the public evidence.
  - 110:2 **يَدْخُلُونَ** د خ ل B003: Introduces an inward or secret dimension that is not exhausted by visible crossing.
  - 110:2 **يَدْخُلُونَ** د خ ل B005: Adds the social ambiguity of a newcomer mixing among established insiders.

## social order recomposed
- reading: The verse depicts serial social incorporation: formerly external groups become familiar participants in a practiced and organized order.
- mechanism: Cohorts do not merely add private convictions. Newcomers mix with insiders, estrangement can become familiarity, and repeated practice places them within an ordered social world; the influx recomposes the community that receives it.
- trace:
  - 110:2 **ٱلنَّاسَ** ن و س B003: Supplies familiarity overcoming estrangement as a possible effect of incorporation.
  - 110:2 **يَدْخُلُونَ** د خ ل B005: Figures entrants as newcomers who mix into an existing people or affair.
  - 110:2 **دِينِ** د ي ن B005: Makes habitual practice, not a momentary declaration, part of the entered order.
  - 110:2 **دِينِ** د ي ن B006: Contributes the civic image of a place structured by authority and obedience.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Makes incorporation collective and serial, so each cohort changes the receiving whole.

## opening causes ingress
- reading: Groups traverse an access newly made possible; their visible ingress is the enacted consequence of an arrived opening.
- mechanism: The prior arrival and release of closure give the focus entry a causal prehistory. What is seen in 110:2 is not spontaneous crowd motion but the downstream passage made possible when a closed approach becomes traversable.
- trace:
  - 110:1 **جَآءَ** ج ي ء B001: Supplies the arrival or occurrence that initiates the temporal threshold.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B001: Supplies release of closure and widening of an entrance as the enabling condition.
  - 110:2 **يَدْخُلُونَ** د خ ل B001: Realizes the enabled condition as actual passage into the interior.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Shows the opened route being used serially by successive groups.

## aid shifts agency
- reading: Human cohorts genuinely enter, but their movement is seen as the manifestation of aid whose source and destination exceed both entrants and observer.
- mechanism: Aid is explicitly manifested before the crowd scene, and the same divine referent marks both the source of that aid and the destination's ownership. The people's movement remains real agency, but it is nested inside an event not possessed by either crowd or observer.
- trace:
  - 110:1 **نَصْرُ** ن ص ر B001: Contributes aid that also makes its result manifest, reframing what the observer sees.
  - 110:1 **ٱللَّهِ** ء ل ه B001: Locates the antecedent aid in the same divine source toward whom worship is directed.
  - 110:2 **ٱللَّهِ** ء ل ه B001: Marks the entered religious domain as belonging to the worshipped one rather than to the witness.
  - 110:2 **وَرَأَيْتَ** ر ء ي B001: Makes the crowd's ingress evidence perceived by the witness, not an achievement authored by sight.

## released water cascade
- reading: The groups form a released cascade, distributing through newly opened channels while remaining actual human cohorts entering the divine order.
- mechanism: Rain-like relief, water issuing from an outlet, a carried water supply, and a broad pass align into a material analogy: cohorts move through the opened terrain like released water finding channels. This sharpens succession into a cascading, distributed influx.
- trace:
  - 110:1 **نَصْرُ** ن ص ر B004: Supplies rain and relief as the initiating influx in the material analogy.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B005: Supplies water bursting from its outlet as the release mechanism.
  - 110:2 **وَرَأَيْتَ** ر ء ي B002: The non-dominant mapped root contributes carrying and delivering water to the observed cascade.
  - 110:2 **يَدْخُلُونَ** د خ ل B001: Anchors the analogy back to actual ingress rather than free-standing water imagery.
  - 110:2 **أَفْوَاجًا** ف و ج B002: Contributes the broad gap or open stretch through which the influx can spread.

## spectacle decentered
- reading: The witness is made answerable to what is seen: the crowd spectacle must be de-centered, exonerated from self-credit, and answered with praise.
- mechanism: A highly visible mass event can become an occasion for display or self-credit. The following acts of exoneration and praise redirect the witness away from possessing the spectacle and toward a response that clears the divine source and assigns praiseworthiness beyond the observer.
- trace:
  - 110:2 **وَرَأَيْتَ** ر ء ي B005: Introduces the live danger that public visibility can be converted into performance before people.
  - 110:3 **فَسَبِّحْ** س ب ح B002: Supplies exoneration and transcendence as a corrective to appropriating the visible success.
  - 110:3 **بِحَمْدِ** ح م د B001: Supplies explicit praise rather than blame and directs the event's evaluation.
  - 110:3 **بِحَمْدِ** ح م د B005: Makes self-credit through a received favor a diagnostic counterpressure within the praise response.

## entry begins cultivation
- reading: Crossing is an intake point: successive newcomers enter a domain in which habit, repair, nurture, and completion still have to unfold.
- mechanism: The following address to lordship activates repair, nurture, completion, and growth. Joined to newcomers mixing into a habitual order, this makes boundary crossing the beginning of formation rather than proof that formation is finished.
- trace:
  - 110:2 **يَدْخُلُونَ** د خ ل B005: Supplies newcomers mixing among a people, creating the social material that requires formation.
  - 110:2 **دِينِ** د ي ن B005: Makes durable habit the post-entry form that cannot be completed at the threshold.
  - 110:3 **رَبِّكَ** ر ب ب B002: Supplies repair, upbringing, and completion as the work that follows ingress.
  - 110:3 **رَبِّكَ** ر ب ب B005: The non-dominant mapped root adds feeding and growth, making formation organic and ongoing.

## visible shell vulnerable interior
- reading: Visible entry forms only the public shell of a vulnerable interior; the climax remains open to protective covering and release from consequences.
- mechanism: The request for protective covering after the visible influx intensifies the baseline split between appearance and interior. Entry exposes new inner relations and possible consequences; protective attention is needed precisely where sight alone might declare completion.
- trace:
  - 110:2 **وَرَأَيْتَ** ر ء ي B006: Supplies the visible surface that can make the event look self-evidently complete.
  - 110:2 **يَدْخُلُونَ** د خ ل B003: Supplies the inward and secret dimension created by entry.
  - 110:2 **يَدْخُلُونَ** د خ ل B004: Keeps latent interior disorder available as a risk, not as an accusation against the cohorts.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B001: Supplies a covering that protects what it encloses, turning forgiveness into protective care.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B002: Adds protection from consequences and makes vulnerability live after the public threshold.

## entry as recurrent return
- reading: Entry can initiate a repeated rhythm of access, turning, straightening, and continuation; the cohorts arrive, but their orientation remains renewable.
- mechanism: Temporal occurrence, a summons toward repentance, continued preparedness, and the focus branch of bringing animals back for another watering create a return-loop. Entry can be reread as recurrent access and reorientation, not a single irreversible crossing.
- trace:
  - 110:2 **يَدْخُلُونَ** د خ ل B007: Supplies a concrete pattern of being brought in again for another watering.
  - 110:2 **دِينِ** د ي ن B005: Translates repeated access into a sustained habitual orientation.
  - 110:3 **كَانَ** ك و ن B001: Places the event within temporal occurrence rather than outside process and duration.
  - 110:3 **تَوَّابًۢا** ت و ب B003: Supplies an active summons for another to turn, making return relational rather than merely private.
  - 110:3 **تَوَّابًۢا** ت و ب B002: The non-dominant mapped root contributes straightening, readiness, and continuation to the return-loop.

## observer as mirror
- reading: The entering people fill and alter the observer's field of vision like an image in a mirror or pupil, so seeing becomes an ethically disciplined transformation of the witness.
- mechanism: 
- trace:
  - 110:2 **وَرَأَيْتَ** ر ء ي B006: Contributes mirror and visible appearance, turning the witness's sight into a reflective surface.
  - 110:2 **ٱلنَّاسَ** ن و س B005: Contributes the human image in the eye, locating the multitude within the observer's visual field.
  - 110:3 **فَسَبِّحْ** س ب ح B002: Makes exoneration the discipline applied to a perception that could otherwise center its human witness.

## wide pass into ordered city
- reading: The cohorts also disclose the geometry of incorporation: an opened broad approach conducts human groups into an ordered civic-religious interior.
- mechanism: 
- trace:
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B001: Supplies the opening and widening of an approach before the movement begins.
  - 110:2 **أَفْوَاجًا** ف و ج B002: Contributes a broad passage between raised boundaries as the geometry of mass ingress.
  - 110:2 **يَدْخُلُونَ** د خ ل B001: Anchors the topography in actual crossing from outside to inside.
  - 110:2 **دِينِ** د ي ن B006: Supplies the ordered city as a social interior organized by authority and obedience.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Preserves the primary human-cohort sense within the spatial analogy.

## whole crowd under cover
- reading: Successive batches are gathered into a whole crowd under protective care, extending attention from public numbers to every concealed interior.
- mechanism: 
- trace:
  - 110:2 **ٱلنَّاسَ** ن و س B001: Supplies the manifest human total whose members are entering.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Distributes that total into successive groups without erasing their collectivity.
  - 110:2 **يَدْخُلُونَ** د خ ل B003: Keeps each entrant's hidden interior within the scope of the crowd scene.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B008: Reassembles the successive cohorts as the crowd in its entirety.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B001: Places that entire collectivity, including unseen interiors, under a protective covering.


# Focus 110:3

## dual reorientation
- reading: A sequenced reorientation: clear false attribution, refill speech with Lord-directed praise, seek protective pardon, and do so within an already active summons to return.
- mechanism: Tasbih first clears false attribution, praise fills that cleared space with gratitude directed through the Lord, and seeking forgiveness asks protection from whatever residue remains. The final temporal predicate makes return an established availability rather than a one-time exception.
- trace:
  - 110:3 **فَسَبِّحْ** س ب ح B002: Supplies distancing and absolution, functioning as the removal of an improper attribution before praise.
  - 110:3 **بِحَمْدِ** ح م د B001: Supplies commendation and gratitude for benefaction, functioning as the positive content of the response.
  - 110:3 **رَبِّكَ** ر ب ب B001: Supplies ownership and governing authority, locating both the praised action and the responder under the Lord.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B002: Supplies pardon as shielding from consequence, making the second imperative protective rather than merely verbal.
  - 110:3 **كَانَ** ك و ن B001: Supplies temporal being and established predication, extending the final assurance across time.
  - 110:3 **تَوَّابًۢا** ت و ب B003: Supplies an active summons to return, making the closing predicate relationally inviting rather than inert.

## credit disownership
- reading: Praise is also an act of disowning credit: benefaction may pass through the addressee, but it cannot become a claim of merit over others.
- mechanism: The praise inventory includes the social act of claiming credit through a favor. The genitive relation to the Lord reverses that possibility: the addressee is not to convert benefaction into a claim on others, and istighfar cleans the residual desire to own the praise.
- trace:
  - 110:3 **بِحَمْدِ** ح م د B005: Supplies praise claimed on the strength of a benefaction, functioning here as the credit economy that the construction redirects.
  - 110:3 **رَبِّكَ** ر ب ب B001: Supplies possession and mastery, assigning the praise-bearing benefaction to the Lord rather than the human responder.
  - 110:3 **فَسَبِّحْ** س ب ح B002: Supplies disavowal and clearing, functioning as refusal of self-credit.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B002: Supplies release from an offense and its consequence, covering the moral residue of appropriation.

## processual repair
- reading: The ayah sketches recurring maintenance: keep moving through praise, submit to stagewise repair, and seek protection precisely because improvement can relapse.
- mechanism: Coursing movement, stagewise nurture, protection against relapse, temporal persistence, and the split-root image of a matter becoming settled combine into a maintenance loop. The ayah then asks for motion through praise and repair, not a single ceremonial endpoint.
- trace:
  - 110:3 **فَسَبِّحْ** س ب ح B004: Supplies coursing or swimming motion, functioning as a processual image for sustained praise.
  - 110:3 **رَبِّكَ** ر ب ب B002: Supplies repair, nurture, and completion by stages, making lordship an ongoing formative action.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B004: Supplies relapse after improvement, functioning as the risk that continued forgiveness guards against.
  - 110:3 **كَانَ** ك و ن B001: Supplies temporal persistence, keeping the mechanism active beyond one moment.
  - 110:3 **تَوَّابًۢا** ت و ب B002: Supplies a matter becoming ready, straight, and continuous, functioning as an exploratory image of stabilized return.

## arrival anti triumphalism
- reading: The favorable event is itself the ethical hazard: victory must be received by surrendering its credit and seeking pardon for the almost automatic conversion of aid into self-merit.
- mechanism: The arrival of divinely owned aid and victorious opening turns the focus sequence into an anti-triumphal protocol. At the exact point success could be appropriated, tasbih clears the human claim, praise restores agency to the Lord, and istighfar treats self-credit as a live moral residue.
- trace:
  - 110:3 **فَسَبِّحْ** س ب ح B002: Supplies disavowal, functioning as the clearing of triumphalist self-attribution.
  - 110:3 **بِحَمْدِ** ح م د B005: Supplies the temptation to claim praise through a favor, functioning as the social danger exposed by success.
  - 110:3 **رَبِّكَ** ر ب ب B001: Supplies mastery and possession, returning ownership of the achieved opening to the Lord.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B002: Supplies shielding from an offense's consequence, functioning as repair for the appropriation of success.
  - 110:1 **جَآءَ** ج ي ء B001: Supplies arrival and occurrence, locating the focus response after an event received rather than manufactured.
  - 110:1 **نَصْرُ** ن ص ر B001: Supplies aid that makes its recipient manifest, creating both the achievement and its attribution problem.
  - 110:1 **ٱللَّهِ** ء ل ه B001: Supplies the worshiped source, fastening aid and the response to the same divine center.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B004: Supplies victory as an opening, making triumph the immediate pressure under which praise must be purified.

## opening is threshold
- reading: Praise and forgiveness inaugurate the long work created by victory: the opening is a beginning, and the commands are its repeatable maintenance discipline.
- mechanism: An opening that begins what follows, followed by people entering in groups, revises the focus ayah from closing liturgy into operating rhythm. Praise and forgiveness become the practices that keep an opened passage governable while repeated entry continues.
- trace:
  - 110:3 **فَسَبِّحْ** س ب ح B001: Supplies recurring worship and remembrance, functioning as the continuing practice after the threshold opens.
  - 110:3 **رَبِّكَ** ر ب ب B002: Supplies stagewise administration and nurture, functioning as aftercare for what enters.
  - 110:3 **كَانَ** ك و ن B001: Supplies temporal predication, extending the response from an inaugural moment into duration.
  - 110:3 **تَوَّابًۢا** ت و ب B002: Supplies settled continuity, functioning exploratorily as the stable rhythm needed after entry begins.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B002: Supplies a beginning that opens what comes next, converting the apparent culmination into a threshold.
  - 110:2 **يَدْخُلُونَ** د خ ل B001: Supplies actual ingress, giving the opened threshold a continuing human traffic.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Supplies grouped arrival, making the traffic serial and socially consequential rather than instantaneous.

## visible entry hidden interior
- reading: The visible influx is real but epistemically incomplete; the focus ayah disciplines the witness not to turn a mass spectacle into total knowledge of hearts.
- mechanism: The context offers a visible human scene but also branch images of inwardness, hidden corruption, and entrusted assent. That split makes the focus commands an epistemic check: the witness can see entry, yet cannot certify every interior, so praise avoids overclaiming and istighfar covers the gap between public appearance and inward reality.
- trace:
  - 110:3 **بِحَمْدِ** ح م د B002: Supplies finding something satisfactory after testing, functioning as a standard the visible crowd alone may not exhaust.
  - 110:3 **فَسَبِّحْ** س ب ح B002: Supplies clearing and disavowal, functioning as restraint against claiming knowledge beyond what was seen.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B001: Supplies protective covering, giving the unseen interior a non-exposing treatment rather than a triumphant verdict.
  - 110:2 **وَرَأَيْتَ** ر ء ي B001: Supplies ocular and discerning sight, establishing both the reality and the limit of the witness's evidence.
  - 110:2 **ٱلنَّاسَ** ن و س B001: Supplies manifest human appearance, intensifying the public visibility of the event.
  - 110:2 **يَدْخُلُونَ** د خ ل B003: Supplies inwardness and private disposition, opening a layer that mass entry does not make fully visible.
  - 110:2 **يَدْخُلُونَ** د خ ل B004: Supplies concealed impairment, preserving the possibility that an outwardly successful scene contains unresolved interior difficulty.
  - 110:2 **دِينِ** د ي ن B007: Supplies assent and entrustment, functioning as an inward relation deeper than spatial entry alone.

## spectacle anti riya
- reading: The commands actively break the economy of public performance: the larger and more visible the success, the more urgently praise must leave the human audience and return to the Lord.
- mechanism: Boastful opening, people-facing display, visible humanity, and grouped crowds create an audience economy. The focus sequence interrupts it: tasbih disavows the performance, Lord-directed praise relocates the gaze, and istighfar treats the wish to be seen as an offense that can arise inside genuine success.
- trace:
  - 110:3 **بِحَمْدِ** ح م د B005: Supplies praise sought through benefaction, functioning as the performer's desired social return.
  - 110:3 **فَسَبِّحْ** س ب ح B002: Supplies disavowal and distancing, functioning as withdrawal from the crowd's gaze.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B002: Supplies forgiveness and shielding from consequence, treating performative self-display as a reparable danger.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B009: Supplies self-opening through boastful display, turning victory into a possible stage for exhibition.
  - 110:2 **وَرَأَيْتَ** ر ء ي B005: Supplies action calibrated to people's gaze, naming the audience-facing distortion activated by being publicly witnessed.
  - 110:2 **ٱلنَّاسَ** ن و س B001: Supplies visible human presence, furnishing the audience before whom success could be performed.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Supplies crowds in groups, magnifying the social scale of the gaze.

## pastoral reception
- reading: The crowds become a pastoral charge: praise prevents gatekeeping ownership, forgiveness shelters incomplete entrants, and the Lord's returning activity models patient incorporation.
- mechanism: People cease estrangement, outsiders mix into an inside, enter obedience, and arrive as groups. Against that social movement, Lordship activates nurture and foster-care, forgiveness activates protective covering, and the return predicate activates an invitation. The focus ayah can therefore train the addressee as a receiving caretaker, not only as a private penitent.
- trace:
  - 110:3 **رَبِّكَ** ر ب ب B002: Supplies stagewise nurture and repair, functioning as the pattern for caring for entrants after arrival.
  - 110:3 **رَبِّكَ** ر ب ب B005: Supplies fostered-child and caregiver relations, making reception familial and developmental rather than merely numerical.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B001: Supplies a protective cover, functioning as shelter for the vulnerability and incompleteness of new entrants.
  - 110:3 **تَوَّابًۢا** ت و ب B003: Supplies the act of inviting another to return, making the closing predicate hospitable and outward-facing.
  - 110:2 **ٱلنَّاسَ** ن و س B003: Supplies familiarity that removes estrangement, functioning as the social transformation required for reception.
  - 110:2 **يَدْخُلُونَ** د خ ل B005: Supplies an outsider mixing into a people or affair, giving entry the friction of incorporation.
  - 110:2 **دِينِ** د ي ن B001: Supplies obedience and willing compliance, naming the relation entrants are moving into.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Supplies groups of people, scaling the need for nurture from an individual encounter to collective reception.

## collective accounting
- reading: Victory settles no personal ledger: the addressee must surrender praise-credit, refuse moral surplus, and remain a petitioner for remission inside the very judgment that vindicates the cause.
- mechanism: Vindication, adjudicative opening, reckoning, and debt activate a legal-economic reading of the response. The addressee must not book victory as moral profit: praise-credit is relinquished, the non-dominant surplus branch of رب is refused, and istighfar keeps the apparent victor answerable rather than placing him above the ledger.
- trace:
  - 110:3 **بِحَمْدِ** ح م د B005: Supplies a claim to praise based on benefaction, functioning as the credit the apparent victor might try to collect.
  - 110:3 **رَبِّكَ** ر ب ب B003: Supplies transactional surplus through the split mapping, functioning exploratorily as the moral profit that must not accrue to the addressee.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B002: Supplies protection from liability and consequence, placing the victor back among those needing remission.
  - 110:1 **نَصْرُ** ن ص ر B002: Supplies vindication of the wronged, giving victory a justice-bearing rather than merely celebratory force.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B003: Supplies a decisive judgment that opens a closure, functioning as the adjudicative event behind the response.
  - 110:2 **دِينِ** د ي ن B002: Supplies reckoning and recompense, placing the whole event within an account that exceeds human victory.
  - 110:2 **دِينِ** د ي ن B003: Supplies financial debt, functioning as the concrete analogy for an unsettled moral account.

## hydraulic return cycle
- reading: The commands circulate the influx: aid flows through an opening, entrants return in rounds, and praise plus forgiveness keep the movement from stagnating into ownership.
- mechanism: Rain-like aid, water issuing through an opening, quenching, re-entry for a second drink, and a broad passage activate a hydraulic cycle. Focus branches answer with coursing tasbih, cloudlike nurture and covering, and continuing return. The social influx can thus be imagined as a flow that must circulate through praise and forgiveness rather than pool as possessed success.
- trace:
  - 110:3 **فَسَبِّحْ** س ب ح B004: Supplies swimming and coursing motion, functioning as the movement of the response through an influx.
  - 110:3 **رَبِّكَ** ر ب ب B008: Supplies layered cloud and persistent rain that nurtures growth, making lordship the sustaining medium of the flow.
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B001: Supplies shielding cover, including cloudlike cover, functioning as containment after release.
  - 110:3 **تَوَّابًۢا** ت و ب B002: Supplies readiness and continuing regularity, functioning as the cycle's non-terminal recurrence.
  - 110:1 **نَصْرُ** ن ص ر B004: Supplies rain as relief, converting aid into the first water-bearing trigger.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B005: Supplies water bursting from its outlet, giving the opening a released-flow mechanism.
  - 110:2 **وَرَأَيْتَ** ر ء ي B001: Supplies quenching as the opposite of thirst through the split mapping, making the witnessed event provision as well as spectacle.
  - 110:2 **يَدْخُلُونَ** د خ ل B007: Supplies a second entry into drinking, functioning as an image of recurrent rather than single ingress.
  - 110:2 **أَفْوَاجًا** ف و ج B002: Supplies a broad gap or passage, functioning as the channel through which the influx moves.

## post victory relapse
- reading: Seeking forgiveness is prescribed because success is an improvement vulnerable to relapse; the most dangerous regression may begin after the wound appears healed.
- mechanism: 
- trace:
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B004: Supplies relapse after improvement, functioning as the precise danger that post-success istighfar prevents.
  - 110:3 **كَانَ** ك و ن B001: Supplies temporal persistence, keeping prophylactic return available after the first improvement.
  - 110:3 **تَوَّابًۢا** ت و ب B002: Supplies continuing straightness after readiness, functioning as the maintained condition opposed to relapse.
  - 110:1 **نَصْرُ** ن ص ر B001: Supplies achieved aid and manifestation, establishing the improvement whose durability is at issue.
  - 110:1 **وَٱلْفَتْحُ** ف ت ح B004: Supplies victorious opening, intensifying the sense that a favorable state has already been reached.

## counted waves
- reading: Each incoming group renews the response, as if every wave were another count in an indefinitely repeated discipline of praise and forgiveness.
- mechanism: 
- trace:
  - 110:3 **فَسَبِّحْ** س ب ح B006: Supplies units used to count tasbih, functioning as a material image of repeatable response.
  - 110:3 **كَانَ** ك و ن B001: Supplies temporal extension, making the counted response durable rather than exhausted by one group.
  - 110:3 **تَوَّابًۢا** ت و ب B002: Supplies regular continuation, functioning as the cadence linking one unit of response to the next.
  - 110:1 **جَآءَ** ج ي ء B002: Supplies overcoming through abundant coming, creating successive pressure rather than a single arrival.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Supplies discrete human groups, functioning as the social units to which the recurring discipline answers.

## collective cover
- reading: Istighfar also casts a protective, answerable cover over the entire mixed social body generated by the influx, including relations the witness cannot individually govern.
- mechanism: 
- trace:
  - 110:3 **وَٱسْتَغْفِرْهُ** غ ف ر B008: Supplies the idiom of the entire crowd arriving without remainder, making istighfar resonate with the total collective field.
  - 110:3 **رَبِّكَ** ر ب ب B004: Supplies a large assembled multitude, placing the crowd within the semantic reach of lordship.
  - 110:2 **ٱلنَّاسَ** ن و س B001: Supplies manifest humanity, grounding the collective resonance in actual people.
  - 110:2 **يَدْخُلُونَ** د خ ل B008: Supplies interpenetrating parts and what lies between them, functioning as the complex interior relations formed by mass incorporation.
  - 110:2 **أَفْوَاجًا** ف و ج B001: Supplies groups of people, activating the crowd-scale branch at the focus root.
