Focus: 88:12. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_12/D.r13/context.md =====
# 88:12 — focus

فِيهَا عَيْنٌۭ جَارِيَةٌۭ

Anchor translation (canonical reading, reference only):

Orada akan bir kaynak vardır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فِيهَا | فِى |  | P;PRON |
| 2 | عَيْنٌ | عَيْن | ع ي ن | N |
| 3 | جَارِيَةٌ | جَارِيَة | ج ر ي | ADJ |


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
- 88:12 ◀ focus فِيهَا عَيْنٌۭ جَارِيَةٌۭ
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


===== _commentary/v16/work/88_12/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع ي ن (root_001069) — identity root of عَيْنٌ (w2)

- **B001** gören göz — göz, görme organı
  العين الناظرة لكل ذي بصر (maqayis;ayn); العين: حاسة الرؤية (sihah); العين: التي يبصر بها الناظر (tahdhib); العين الجارحة (mufradat)
- **B002** gözle görüp kesin biçimde tanıma — gözle görerek, yüz yüze · yüz yüze görerek · bilerek, görüp emin olarak · gördükten sonra ayrıca iz aramam
  رأيت الشيء عيانا أي معاينة (maqayis); لا أطلب أثرا بعد عين أي بعد معاينة (ayn;sihah;tahdhib); عيانا أي مواجهة (tahdhib); فعلت ذلك عمد عين (sihah)
- **B003** koruyup gözetme — korumam altında, özenle gözeterek · gözümün önünde, korumam altında · gözetimimiz ve korumamız altında
  أنت على عيني، في الإكرام والحفظ جميعا (sihah); على عيني قصدت زيدا يريدون الإشفاق (tahdhib); فلان بعيني أي أحفظه وأراعيه (mufradat); بحيث نرى ونحفظ (mufradat)
- **B004** kötü bakışla zarar verme — gözüyle zarar verdi · gözü değen kimse · göz değmiş kimse · gözü sık değen kimse
  عنت الرجل إذا أصبته بعينك (maqayis); عنت الشيء بعينه فأنا أعينه عينا وهو معيون (ayn); عنت الرجل: أصبته بعينى، فأنا عائن (sihah); عان الرجل فلانا يعينه عينا إذا ما أصابه بالعين (tahdhib); عنته: أصبته بعيني (mufradat)
- **B005** haber toplayan gizli gözcü — gizli gözcü veya öncü · gizli gözcü · bizim için çevreyi yoklayıp haber getirdi
  العين الذي تبعثه يتجسس الخبر (maqayis); العين الذي تبعثه لتجسس الخبر (ayn); العين: الديدبان، والجاسوس (sihah); بعثنا عينا أي طليعة (tahdhib); قيل للمتجسس عين (mufradat)
- **B006** akan su kaynağı — akan su kaynağı · göz önünde akan su · su aktı veya kaynağı ortaya çıktı
  العين الجارية النابعة من عيون الماء (maqayis); عين الماء (ayn;sihah); العين الينبوع الذي ينبع من الأرض ويجري (tahdhib); لمنبع الماء: عين (mufradat); ماء معين أي ظاهر للعيون (mufradat)
- **B007** su sızdıran ince delik — su kabındaki ince veya delik sızıntı yeri · incelip su tutamaz olmuş su kabı · dikiş delikleri kapansın diye kaba su döktü
  عين السقاء (maqayis); تعين السقاء أي بلي ورق منه مواضع (ayn); بالجلد عين، وهي دوائر رقيقة (sihah); سقاء عين إذا رق فلم يمسك الماء (tahdhib); الثقب في المزادة تشبيها بها في الهيئة وفي سيلان الماء (mufradat)
- **B008** güneş yuvarlağı — güneşin gövdesi veya yuvarlağı
  عين الشمس مشبه بعين الإنسان (maqayis); عين الشمس صيخدها (ayn); العين: عين الشمس (sihah); طلعت العين وغابت العين، أي الشمس (tahdhib)
- **B009** göze benzer çukur, yer veya eğim — dizin önündeki çukur · kuyunun kaynak yeri veya çukuru · terazideki küçük eğim veya dengesizlik · yayda merminin yerleştiği bölüm
  عين الركية وهما عينان كأنهما نقرتان في مقدمها (maqayis); عين الركبة (ayn;sihah;tahdhib); في الميزان عين إذا رجحت إحدى كفتيه (tahdhib); عين القوس التي يقع فيها البندق (tahdhib)
- **B010** belirli yönden gelen bulut veya dinmeyen yağmur — kıblenin sağından gelen bulut · günlerce dinmeyen yağmur
  العين السحاب ما جاء من ناحية القبلة (maqayis); العين من السحاب ما أقبل عن يمين القبلة (ayn); العين: ما عن يمين قبلة العراق (sihah;tahdhib); العين: مطر أيام لا يقلع (sihah;tahdhib)
- **B011** hemen elde bulunan para — elde hazır bulunan para · altın para, eldeki para
  العين وهو المال العتيد الحاضر (maqayis); عين غير دين أي مال حاضر (ayn); العين: الدينار؛ العين: المال الناض (sihah); العين: النقد (tahdhib); قيل للذهب: عين (mufradat)
- **B012** ertelenmiş ödemeli alımla para edinme — önceden verilen para veya para sağlamak için yapılan satış · malı ödemesi ertelenmiş olarak satın aldı
  العينة السلف (maqayis;ayn;sihah); تعين فلان من فلان عينة (ayn); اعتان الرجل، إذا اشترى الشئ بنسيئة (sihah); عين التاجر يعين تعيينا وعينة قبيحة (tahdhib); سميت عينة لحصول النقد لطالب العينة (tahdhib)
- **B013** şeyin bizzat kendisi ve belirlenmiş olanı — şeyin bizzat kendisi · tam kendisi, yerine başkası değil · bir şeyi topluluk içinden belirleyip ayırma
  عين الشيء نفسه (maqayis;sihah;tahdhib); خذ درهمك بعينه (maqayis); تعيين الشئ: تخصيصه من الجملة (sihah); دراهمك بأعيانها وهي أعيان دراهمك (tahdhib); ذات الشيء (mufradat)
- **B014** bir şeyin en iyi ve seçkin bölümü — bir şeyin en iyi ve seçkin bölümü
  عينة كل شيء خياره (maqayis); العينة: خيار الشيء (tahdhib); عين الشئ: خياره (sihah); عينة المال أيضا: خياره (sihah); العين تشبيها بها في كونها أفضل الجواهر (mufradat)
- **B015** önde gelen kişiler veya anne baba bir kardeşler — topluluğun önde gelen seçkin kişileri · anne baba bir kardeşler veya aynı kadının çocukları
  أعيان القوم أي أشرافهم (maqayis;sihah;tahdhib); هؤلاء أعيان إخوتهم (maqayis); الأعيان: الأخوة بنو أب واحد وأم واحدة (sihah); أعيان بني الأم يتوارثون (tahdhib); أعيان القوم لأفاضلهم، وأعيان الإخوة (mufradat)
- **B016** geniş ve güzel gözlü olma — geniş ve güzel gözlü · gözlerinin güzelliğiyle adlandırılan yaban sığırı · geniş ve güzel gözlü kadınlar · göz benzeri küçük kare desenli kumaş
  توصف البقرة بسعة العين فيقال بقرة عيناء (maqayis); العين بقر الوحش (ayn;sihah;tahdhib); العين عظم سواد العين في سعتها (ayn); رجل أعين واسع العين (sihah;tahdhib); قاصرات الطرف عين؛ وحور عين (mufradat)
- **B017** kimse veya orada bulunan insanlar — orada hiç kimse yok · ev halkı veya orada bulunanlar · bir topluluk içinde
  ما بها عين متحركة الياء تريد أحدا له عين (maqayis); ما بها عائن، وكذلك ما بها عين، أي أحد (sihah); العين، بالتحريك: أهل الدار (sihah); العين: أهل الدار (tahdhib); جاء فلان في عين، أي في جماعة (sihah)

## ج ر ي (root_000240) — identity root of جَارِيَةٌ (w3)

- **B001** bir yol boyunca akıp, koşup ya da ilerleyerek gitme — hızlı ilerleyiş ve kendi yatağında akış · aktı, koştu ya da yol aldı · suyun akışı · at koşusu · akıtmak ya da harekete geçirmek · akış, gidiş yolu ya da koşu yeri · denizde yol alan gemi · gökte yol alan güneş · suyu akan pınar · denizde yol alan gemiler · çeşitli koşu biçimleri olan at · kötücül ayartıcının sizi kendi işi doğrultusunda sürüklemesine ya da kendine aracı kılmasına izin vermeyin
  أصل واحد وهو انسياح الشيء (maqayis)؛ جرى الماء يجري جرية وجريا وجريانا (maqayis;sihah;mufradat)؛ الخيل تجري والرياح تجري والشمس تجري جريا (ayn;tahdhib)؛ الجارية السفينة والجارية الشمس (maqayis;sihah)
- **B002** alışılmış yol ve davranış düzeni — kişinin alışkanlık edindiği ve sürekli izlediği yol
  للعادة الإجريا (maqayis)؛ الإجريا طريقته التي يجري عليها من عادته (ayn)؛ الإجريا الجري والعادة مما تأخذ فيه (sihah)؛ الإجرياء الوجه الذي نأخذ فيه (tahdhib)؛ الإجريا العادة التي يجري عليها الإنسان (mufradat)
- **B003** başkası adına iş gören, haber götüren ya da güvence veren kimse — başkası adına iş gören, haber götüren ya da güvence veren kimse · başkası adına iş görecek birini tutmak · kötücül ayartıcının sizi kendi işi doğrultusunda sürüklemesine ya da kendine aracı kılmasına izin vermeyin
  الجري الوكيل (maqayis;tahdhib)؛ الجري الرسول (ayn;tahdhib;mufradat)؛ الجري الضامن (tahdhib)؛ استجريت أي اتخذت وكيلا (maqayis;sihah;tahdhib)؛ لا يستجرينكم الشيطان (maqayis;sihah;tahdhib;mufradat)
- **B004** genç kız ve ona bağlı genç kızlık çağı — genç kız ya da hizmette çalıştırılan genç kadın · genç kızlık çağı · genç kızlık durumu
  الجارية من النساء لأنها تستجرى في الخدمة (maqayis)؛ الجارية مصدرها الجراء (ayn)؛ جارية بينة الجراية والجراء (sihah;tahdhib)؛ أيام جرائها أي صباها (maqayis;ayn;sihah)
- **B005** kuş kursağı — 
  الجرية وهي الحوصلة أصلها قرية (maqayis)؛ الجرية مثل القرية هي الحوصلة (sihah)؛ الجرية والقرية والنوطة لحوصلة الطائر (tahdhib)؛ يقال للحوصلة جرية لأنها مجرى الطعام (mufradat)
- **B006** sürekli verilen geçimlik ya da kalıcı yarar — düzenli görev ödeneği · onun için sürekli verildi ya da sürüp gitti · ona sürekli olarak verdim · yararı süren bağış
  الجراية الجاري من الوظائف (sihah)؛ الأرزاق جارية والأعطيات دارة (tahdhib)؛ جرى عليه ذلك الشيء ودر له بمعنى دام له (tahdhib)؛ أجريت له كذا أي أدمت له (tahdhib)؛ صدقة جارية (tahdhib)
- **B007** birlikte ilerleyip birbirine ayak uydurma — yanında koşmak ya da ona ayak uydurmak · söyleşide ona ayak uydurmak ve karşılık vermek
  جاراه مجاراة وجراء أي جرى معه (sihah)؛ جاراه في الحديث وتجاروا فيه (sihah)
- **B008** senin yüzünden ya da senin için — senin yüzünden ya da senin için
  فعلت ذلك من جراك ومن جرائك أي من أجلك (sihah)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:12, and ## Buluşmalar) =====
## Yüz: kurumuş toprak, yumuşamış toprak

İkinci ve sekizinci ayetler aynı iki kelimeyle başlar, "yüzler, o gün" der ve yalnızca bir sıfatta ayrılır. Birinci sıfat خاشعة'dır. Bu kelime alçalıp sinmeyi anlatır: {ar:أصل واحد يدل على التطامن, tr:aslun vâhidun yedullü ale't-tatâmün, gloss:alçalıp çökmeyi gösteren tek bir kök, source:"خ ش ع,B001"}. Araplar aynı kelimeyi toprak için de kullanır: {ar:بلدة خاشعة مغبرة, tr:beldetun hâşiatun muğberra, gloss:tozlu ve çökük bir yer, source:"خ ش ع,B002"}; {ar:إذا يبست الأرض ولم تمطر قيل قد خشعت, tr:izâ yebiseti'l-ardu ve lem tumtar kîle kad haşaat, gloss:yer kuruyup yağmur almayınca haşaat denir, source:"خ ش ع,B002"}; {ar:قف خاشع لاطئ بالأرض, tr:kuffun hâşiun lâtiun bi'l-ard, gloss:yere yapışmış alçak sırt, source:"خ ش ع,B002"}. Ayetin anlamı eğik ve ezik bir yüzdür. Yanında ise yağmur görmemiş, tozlanmış, yere yapışmış bir toprak duyulur.

Üçüncü ayet bu toprağın nasıl yorulduğunu gösterir: {ar:عَامِلَةٌۭ نَّاصِبَةٌۭ, tr:âmiletun nâsıba, gloss:çalışıp didinmiş ve bitkin, source:88:3}. Bitkinlik, ayakta durup çalışmaktan gelir: {ar:النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي, tr:en-nasabu'l-anâ ve ma'nâhu enne'l-insâne lâ yezâlü muntasiben hattâ yu'yî, gloss:yorgunluktur; insanın tükenene dek ayakta kalmasıdır, source:"ن ص ب,B004"}. Aynı kelime yüze çökmüş kederi de anlatır: {ar:الحزن إذا أثر فيه, tr:el-huznu izâ essera fîh, gloss:iz bırakan keder, source:"ن ص ب,B004"}. Beşinci ayette bu kurumuş yüz sulanır: {ar:تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:tuskâ min aynin âniye, gloss:kaynamış bir pınardan içirilir, source:88:5}. Sulamak, birine içecek vermektir: {ar:السقي والسقيا أن يعطيه ما يشرب, tr:es-sakyu ve's-sukyâ en yu'tıyehû mâ yeşrab, gloss:içecek vermek, source:"س ق ي,B001"}. Kuru toprağı diriltmesi gereken su burada yakan sudur. Toprağı canlandıran düzen tersine dönmüştür.

Kur'an kurumuş toprağın suyla dirilişini aynı kelimeyle anlatır. Allah ayetlerini sayarken şöyle der: {ar:تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:tera'l-arda hâşiaten fe-izâ enzelnâ aleyhe'l-mâe'htezzet ve rabet, gloss:yeri çökük görürsün; üstüne su indirince kıpırdar ve kabarır, source:41:39}. Aynı ayet hemen ardından {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39} der. Diriltilmekten şüphe edenlere de sahne aynı sözlerle kurulur: {ar:وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ, tr:ve tera'l-arda hâmideten, gloss:yeri kupkuru ve cansız görürsün, source:22:5}. Buradaki cansız toprak sıfatı, çökük toprağın tanımında geçen kelimedir: {ar:أرض خاشعة هامدة, tr:ardun hâşiatun hâmide, gloss:çökük ve cansız toprak, source:"خ ش ع,B002"}. Sağır edici çığlığın geldiği gün anlatılırken toz da yüzlere konar: {ar:فَإِذَا جَآءَتِ ٱلصَّآخَّةُ, tr:fe-izâ câeti's-sâhha, gloss:kulakları sağır eden geldiğinde, source:80:33}; {ar:وَوُجُوهٌۭ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌۭ, tr:ve vucûhun yevmeizin aleyhâ ğabera, gloss:o gün birtakım yüzlerin üstünde toz vardır, source:80:40}. Burada tozlu toprak ile tozlu yüz aynı resimde birleşir.

Altıncı ayetteki yiyecek, yüzün halini adında taşır. Yüzün eğikliği şöyle açıklanır: {ar:الخشوع الضراعة؛ إذا ضرع القلب خشعت الجوارح, tr:el-huşûu'd-darâa; izâ dara'a'l-kalbu haşaati'l-cevârih, gloss:huşu boyun eğmektir; kalp boyun eğince organlar da eğilir, source:"خ ش ع,B001"}. Bu açıklamadaki "boyun eğmek" kelimesi, yiyecek adı ضريع ile aynı köktendir: {ar:ضرع الرجل ضراعة إذا ذل, tr:dara'a'r-raculu darâaten izâ zell, gloss:adam alçalınca dara'a denir, source:"ض ر ع,B002"}. Aynı kök incelmiş bedeni de anlatır: {ar:لضارع الجسم أي نحيف ضعيف, tr:le-dâriu'l-cism ey nahîfun daîf, gloss:bedeni zayıf ve cılız, source:"ض ر ع,B003"}. Yiyecekle boyun eğme arasındaki bağ kök birliğinden gelir. Yüzün eğikliğine bağlanması ise kelimelerin açıklamasındandır.

Sekizinci ayette öteki sıfat gelir: {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vucûhun yevmeizin nâime, gloss:o gün birtakım yüzler yumuşak ve mutlu, source:88:8}. Bu kelime yumuşamayı ve tazeliği anlatır: {ar:نعم الشيء صار ناعما لينا, tr:neime'ş-şey'u sâra nâimen leyyinâ, gloss:şey yumuşak ve esnek oldu, source:"ن ع م,B002"}; {ar:نعمة العيش حسنه وغضارته, tr:na'metü'l-ayşi husnühû ve ğadâratüh, gloss:yaşamın tazeliği ve güzelliği, source:"ن ع م,B002"}. Aynı kök rüzgârların en nemlisine de ad verir: {ar:النعامى ريح الجنوب لأنها أبل الرياح وأرطبها, tr:en-neâmâ rîhu'l-cenûb li-ennehâ eballü'r-riyâhi ve ertabuhâ, gloss:rüzgârların en ıslağı ve en nemlisi olan güney rüzgârı, source:"ن ع م,B009"}. Bu yüzün toprağında akan bir pınar vardır: {ar:العين الجارية النابعة من عيون الماء, tr:el-aynü'l-câriyetü'n-nâbiatü min uyûni'l-mâ', gloss:su gözelerinden kaynayıp akan pınar, source:"ع ي ن,B006"}. Dokuzuncu ayetteki hoşnutluk {ar:أصل واحد يدل على خلاف السخط, tr:aslun vâhidun yedullü alâ hılâfi's-saht, gloss:öfkenin karşıtını gösteren kök, source:"ر ض و,B001"} diye tanımlanır. On üçüncü ayetteki sedirler ise sevinçten adlandırılmıştır: {ar:السرير الذي يجلس عليه من السرور, tr:es-serîru'llezî yuclesu aleyhi mine's-surûr, gloss:üstüne oturulan sedir adını sevinçten alır, source:"س ر ر,B011"}; {ar:السرور أمر خال من الحزن, tr:es-surûru emrun hâlin mine'l-hazen, gloss:sevinç kederden boş bir haldir, source:"س ر ر,B010"}. Üçüncü ayetteki yorgunluk iz bırakan bir kederdi. Burada sedirin adı, kederden boş olan bir sevinçtir.

Yirminci ayette göz toprağın kendisine çevrilir. Arapçada iyi toprağın sıfatı yumuşaklıktır: {ar:أرض أريضة لينة طيبة, tr:ardun erîdatun leyyinatun tayyibe, gloss:yumuşak ve verimli toprak, source:"ء ر ض,B002"}. Bu, nâime'nin tanımındaki yumuşaklığın aynısıdır. Göğe verilen adlardan biri de bulut ve yağmurdur: {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tüsemmi's-sehâbe semâen ve'l-matara semâ', gloss:Araplar buluta da yağmura da gök der, source:"س م و,B004"}. Böylece göğe ve yere yöneltilen bakış, iki yüzün farkını da gösterir: yere su iner ya da inmez.

Kur'an iki yüzü başka yerlerde de aynı sözlerle karşı karşıya koyar. Güzel davrananlar için {ar:وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌۭ وَلَا ذِلَّةٌ, tr:ve lâ yerhaku vucûhehum katerun ve lâ zille, gloss:yüzlerini ne toz ne aşağılanma bürür, source:10:26} denir. İyilerin yüzü için {ar:تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ, tr:ta'rifu fî vucûhihim nadrate'n-naîm, gloss:yüzlerinde nimetin tazeliğini tanırsın, source:83:24} denir. Burada nimet kelimesi nâime ile aynı köktendir. O günün yüzleri {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ, tr:vucûhun yevmeizin nâdıra, gloss:o gün birtakım yüzler taptaze, source:75:22} ve {ar:وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ, tr:ve vucûhun yevmeizin bâsira, gloss:birtakım yüzler de asık, source:75:24} diye ikiye ayrılır. Sabredenlere verilen karşılık da surenin iki kelimesini bir arada söyler: {ar:وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا, tr:ve lakkâhum nadraten ve surûrâ, gloss:onlara tazelik ve sevinç kavuşturdu, source:76:11}. Üçüncü ayetteki yorgunluk bahçede ortadan kaldırılır. Pınarlı bahçelerdeki takva sahipleri için {ar:لَا يَمَسُّهُمْ فِيهَا نَصَبٌۭ, tr:lâ yemessuhum fîhâ nasab, gloss:orada onlara yorgunluk dokunmaz, source:15:48} denir. Bahçe halkı da aynı sözü kendisi söyler: {ar:لَا يَمَسُّنَا فِيهَا نَصَبٌۭ وَلَا يَمَسُّنَا فِيهَا لُغُوبٌۭ, tr:lâ yemessunâ fîhâ nasabun ve lâ yemessunâ fîhâ luğûb, gloss:burada bize ne yorgunluk dokunur ne bitkinlik, source:35:35}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:2 خَٰشِعَةٌ خ ش ع B002; 88:3 نَّاصِبَةٌ ن ص ب B004; 88:5 تُسْقَىٰ س ق ي B001; 88:6 ضَرِيعٍ ض ر ع B002; 88:6 ضَرِيعٍ ض ر ع B003; 88:8 نَّاعِمَةٌ ن ع م B002; 88:8 نَّاعِمَةٌ ن ع م B009; 88:9 رَاضِيَةٌ ر ض و B001; 88:12 عَيْنٌ ع ي ن B006; 88:13 سُرُرٌ س ر ر B010; 88:13 سُرُرٌ س ر ر B011; 88:18 ٱلسَّمَآءِ س م و B004; 88:20 ٱلْأَرْضِ ء ر ض B002

## İki pınar ve kaplar

Surede iki pınar vardır ve ikisi de aynı adı taşır. Beşincisi {ar:مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:min aynin âniye, gloss:son noktasına varmış sıcak bir pınardan, source:88:5}, on ikincisi ise {ar:فِيهَا عَيْنٌۭ جَارِيَةٌۭ, tr:fîhâ aynun câriye, gloss:orada akan bir pınar vardır, source:88:12}. Ad aynıdır, değişen yalnızca sıfattır. Birinde su sıcaklığın sonuna varmıştır. Ötekinde hareket halindedir: {ar:جرى الماء يجري جرية وجريا وجريانا, tr:cera'l-mâu yecrî cireten ve ceryen ve cereyânâ, gloss:su aktı, source:"ج ر ي,B001"}. Kaynayan suyun durduğu bir yer vardır, ama akan su yenilenir. Kur'an bu iki pınarı aynı surede, birkaç ayet arayla yan yana koyar. Biri günahkârların dolaştığı {ar:حَمِيمٍ ءَانٍۢ, tr:hamîmin ân, gloss:son noktasına varmış kaynar su, source:55:44} ve diğeri Rabbinin makamından korkanların iki bahçesinde akan sudur: {ar:فِيهِمَا عَيْنَانِ تَجْرِيَانِ, tr:fîhimâ aynâni tecriyân, gloss:ikisinde de akan iki pınar vardır, source:55:50}.

Beşinci ayetteki sıfatın harfleri, Arapçada kap anlamına gelen kelimenin çoğuluyla da aynıdır: {ar:الإناء معروف وجمعه آنية والأواني, tr:el-inâu ma'rûfun ve cem'uhû âniyetun ve'l-evânî, gloss:kap bilinir; çoğulu âniye ve evânîdir, source:"ء ن ي,B004"}. Ayetteki anlam sıcaklıktır. Yanında ise kapların adı duyulur. On dördüncü ayet bu kapları bahçeye koyar: {ar:وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ, tr:ve ekvâbun mevdûa, gloss:konmuş kadehler, source:88:14}. Kevb kulpsuz bir kadehtir: {ar:الكوب القدح لا عروة له, tr:el-kûbü'l-kadahu lâ urvete leh, gloss:kevb kulpsuz kadehtir, source:"ك و ب,B001"}. Konmuş olmak, kaldırılmışın karşıtıdır: {ar:وضعت الشيء أضعه وضعا وهو ضد رفعته, tr:vada'tü'ş-şey'e edauhû vad'an ve huve zıddü rafa'tüh, gloss:bir şeyi koydum; kaldırdım'ın zıddı, source:"و ض ع,B001"}. Kadehler el altında hazır durur, istenmeden önce oradadır. Kur'an aynı iki kelimeyi, yani kapların adını ve kadehleri, sabredenlerin karşılığını anlatırken yan yana getirir: {ar:وَيُطَافُ عَلَيْهِم بِـَٔانِيَةٍۢ مِّن فِضَّةٍۢ وَأَكْوَابٍۢ كَانَتْ قَوَارِيرَا۠, tr:ve yutâfu aleyhim bi-âniyetin min fiddatin ve ekvâbin kânet kavârîrâ, gloss:çevrelerinde gümüş kaplar ve billur kadehler dolaştırılır, source:76:15}. Aynı ses bir yerde kaynayan pınarın sıfatıdır, başka bir yerde bahçenin gümüş kapları.

Bahçe halkı da içirilir. Fiil iki tarafta da aynıdır, değişen kaynaktır: {ar:وَيُسْقَوْنَ فِيهَا كَأْسًۭا كَانَ مِزَاجُهَا زَنجَبِيلًا, tr:ve yuskavne fîhâ ke'sen kâne mizâcuhâ zencebîlâ, gloss:orada zencefil katkılı bir kadehten içirilirler, source:76:17}; {ar:عَيْنًۭا فِيهَا تُسَمَّىٰ سَلْسَبِيلًۭا, tr:aynen fîhâ tusemmâ selsebîlâ, gloss:orada Selsebil denen bir pınardan, source:76:18}; {ar:يُسْقَوْنَ مِن رَّحِيقٍۢ مَّخْتُومٍ, tr:yuskavne min rahîkın mahtûm, gloss:mühürlü saf bir içkiden içirilirler, source:83:25}. Bahçenin pınarı insanın elinde akar: {ar:عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا, tr:aynen yeşrabu bihâ ibâdullâhi yufeccirûnehâ tefcîrâ, gloss:Allah'ın kullarının içtiği ve diledikleri yere fışkırttıkları bir pınar, source:76:6}. Kadehler de bu pınardan doldurulur: {ar:بِأَكْوَابٍۢ وَأَبَارِيقَ وَكَأْسٍۢ مِّن مَّعِينٍۢ, tr:bi-ekvâbin ve ebârîka ve ke'sin min maîn, gloss:kadehler ibrikler ve akan pınardan doldurulmuş kâse ile, source:56:18}. Buradaki "maîn" kelimesi gözle görünen akar suyu anlatır: {ar:ماء معين أي ظاهر للعيون, tr:mâun maînun ey zâhirun li'l-uyûn, gloss:gözlere açık akan su, source:"ع ي ن,B006"}. Allah, Peygamber'e bu suyun kimden geldiğini sormasını söyler: {ar:قُلْ أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًۭا فَمَن يَأْتِيكُم بِمَآءٍۢ مَّعِينٍۭ, tr:kul e-raeytum in asbaha mâukum ğavran fe-men ye'tîkum bi-mâin maîn, gloss:de ki suyunuz yere çekilse size akar suyu kim getirir, source:67:30}.

Arapçada içmek de beslenmenin bir parçası sayılır: {ar:أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء, tr:aslun fî tezevvuki'ş-şey'i ve't-taâmu huve'l-me'kûlu ve'l-it'âmu yekau hatta'l-mâ', gloss:tatma kökü; yemek yenendir; doyurmak suya bile uzanır, source:"ط ع م,B001"}. Böylece beşinci ve altıncı ayetler tek bir sofradır: içecek kaynar sudur, yemek de ضريع. Son ayetlerdeki azap kelimesinin kökü ise tatlı suyu da adlandırır: {ar:عذب الماء عذوبة فهو عذب طيب, tr:azube'l-mâu uzûbeten fe-huve azbun tayyib, gloss:su tatlılaştı; o tatlı ve hoş sudur, source:"ع ذ ب,B001"}. Bu anlam ayetteki cezanın yanında duyulur. Aynı harfler bir yerde tatlı su, başka bir yerde azaptır. Tatlı suyu bekleyen yüz, kaynar suyla karşılaşır.

Kaynaklar: 88:5 تُسْقَىٰ س ق ي B001; 88:5 ءَانِيَةٍ ء ن ي B003; 88:5 ءَانِيَةٍ ء ن ي B004; 88:6 طَعَامٌ ط ع م B001; 88:12 عَيْنٌ ع ي ن B006; 88:12 جَارِيَةٌ ج ر ي B001; 88:14 أَكْوَابٌ ك و ب B001; 88:14 مَّوْضُوعَةٌ و ض ع B001; 88:24 ٱلْعَذَابَ ع ذ ب B001

## Göz: yere atılan bakış ve serbest bakış

İkinci ayetteki eğiklik önce gözdedir: {ar:الخشوع رميك ببصرك إلى الأرض, tr:el-huşûu remyüke bi-basarike ile'l-ard, gloss:huşu bakışını yere atmandır, source:"خ ش ع,B001"}; {ar:خشع ببصره إذا غضه, tr:haşaa bi-basarihî izâ ğaddah, gloss:gözünü indirdiğinde haşaa denir, source:"خ ش ع,B001"}. O gün yüz yukarı bakamaz, bakışı toprağa düşer. Kur'an bu bakışı birkaç sahnede gösterir. Mezarlardan çıkış için {ar:خُشَّعًا أَبْصَٰرُهُمْ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ, tr:huşşean ebsâruhum yahrucûne mine'l-ecdâs, gloss:gözleri eğik halde kabirlerden çıkarlar, source:54:7} denir. Sarsıntı günü için {ar:أَبْصَٰرُهَا خَٰشِعَةٌۭ, tr:ebsâruhâ hâşia, gloss:gözleri eğiktir, source:79:9} denir. Ateşe sunulan zalimler için ise eğiklik ile bakış bir arada anılır: {ar:يَنظُرُونَ مِن طَرْفٍ خَفِىٍّۢ, tr:yenzurûne min tarfin hafiyy, gloss:gizli bir göz ucuyla bakarlar, source:42:45}.

İki pınarın adı da gözdür: {ar:العين الناظرة لكل ذي بصر, tr:el-aynü'n-nâzıratü li-külli zî basar, gloss:gören her canlının bakan gözü, source:"ع ي ن,B001"}. Bu, ayetteki pınar anlamının yanında duyulur. On ikinci ayetteki pınarın suyu da göze açıktır: {ar:ماء معين أي ظاهر للعيون, tr:mâun maînun ey zâhirun li'l-uyûn, gloss:gözlere açık akan su, source:"ع ي ن,B006"}.

On yedinci ayet ise bugünün gözüne serbest bir bakış ister: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Bakmak düşünerek bakmak demektir: {ar:تأمل الشيء ومعاينته, tr:teemmülü'ş-şey'i ve muâyenetüh, gloss:bir şeyi düşünerek göz önünde tutmak, source:"ن ظ ر,B001"}; {ar:تقليب البصر والبصيرة لإدراك الشيء ورؤيته, tr:taklîbü'l-basari ve'l-basîreti li-idrâki'ş-şey'i ve ru'yetih, gloss:bir şeyi kavrayıp görmek için gözü ve gönül gözünü çevirmek, source:"ن ظ ر,B001"}. Bakmanın bir de boş kalan biçimi vardır: {ar:ينظرون إليك وهم لا يبصرون, tr:yenzurûne ileyke ve hum lâ yubsırûn, gloss:sana bakarlar ama görmezler, source:"ن ظ ر,B012"}. Ayetteki soru bu boşluğa karşı sorulur. Bakış dört yöne gönderilir: el altındaki deveye, yukarıya, karşıya ve aşağıya. Gök her yanıyla üstte olandır: {ar:السماء كل ما علاك فأظلك, tr:es-semâu küllü mâ alâke fe-ezallek, gloss:gök seni aşıp gölgeleyen her şeydir, source:"س م و,B004"}. Yer ise aşağıda kalıp göğün karşısında durandır. İkinci ayetteki bakış yere düşmüştü ve kalkamıyordu. On yedinci ayetten yirminci ayete kadar bakış her yöne serbestçe döner. Sure, o gün eğilecek gözün bugün henüz bakabildiğini hatırlatır.

Kur'an aynı soruyu başka yerlerde de sorar. Bir uyarıcıya ve toprak olduktan sonra diriltilmeye şaşanlara şöyle denir: {ar:أَفَلَمْ يَنظُرُوٓا۟ إِلَى ٱلسَّمَآءِ فَوْقَهُمْ كَيْفَ بَنَيْنَٰهَا, tr:e-fe-lem yenzurû ile's-semâi fevkahum keyfe beneynâhâ, gloss:üstlerindeki göğe bakmadılar mı onu nasıl kurduk, source:50:6}. Başka bir soru bakışı habere bağlar: {ar:أَوَلَمْ يَنظُرُوا۟ فِى مَلَكُوتِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:e-ve-lem yenzurû fî melekûti's-semâvâti ve'l-ard, gloss:göklerin ve yerin hükümranlığına bakmadılar mı, source:7:185}. Aynı ayet şöyle biter: {ar:فَبِأَىِّ حَدِيثٍۭ بَعْدَهُۥ يُؤْمِنُونَ, tr:fe-bi-eyyi hadîsin ba'dehû yu'minûn, gloss:bundan sonra hangi habere inanacaklar, source:7:185}. Dünyaya bakmak ile ilk ayetteki haber burada birleşir. Bakış diriltmeye de bağlanır: {ar:قُلْ سِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ بَدَأَ ٱلْخَلْقَ ۚ ثُمَّ ٱللَّهُ يُنشِئُ ٱلنَّشْأَةَ ٱلْءَاخِرَةَ, tr:kul sîrû fi'l-ardi fenzurû keyfe bedee'l-halka summallâhu yunşiu'n-neş'ete'l-âhira, gloss:de ki yeryüzünde gezin de yaratmayı nasıl başlattığına bakın; sonra Allah son yaratılışı yapacak, source:29:20}; {ar:فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ, tr:fenzur ilâ âsâri rahmetillâhi keyfe yuhyi'l-arda ba'de mevtihâ, gloss:Allah'ın rahmetinin izlerine bak; yeri ölümünden sonra nasıl diriltir, source:30:50}. Bahçede ise bakış yükseltilmiş yerlerden yapılır: {ar:عَلَى ٱلْأَرَآئِكِ يَنظُرُونَ, tr:ale'l-erâiki yenzurûn, gloss:koltuklar üstünde bakarlar, source:83:23}. Bakışın varacağı en uç yer de şudur: {ar:إِلَىٰ رَبِّهَا نَاظِرَةٌۭ, tr:ilâ rabbihâ nâzıra, gloss:Rablerine bakan, source:75:23}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:5 عَيْنٍ ع ي ن B001; 88:12 عَيْنٌ ع ي ن B001; 88:12 عَيْنٌ ع ي ن B006; 88:17 يَنظُرُونَ ن ظ ر B001; 88:17 يَنظُرُونَ ن ظ ر B012; 88:18 ٱلسَّمَآءِ س م و B004; 88:20 ٱلْأَرْضِ ء ر ض B001

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

