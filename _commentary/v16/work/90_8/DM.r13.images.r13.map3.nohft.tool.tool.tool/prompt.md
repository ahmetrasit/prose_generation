Focus: 90:8. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/90_8/D.r13/context.md =====
# 90:8 — focus

أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ

Anchor translation (canonical reading, reference only):

Ona iki göz vermedik mi?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | أَلَمْ | لَم |  | INTG;NEG |
| 2 | نَجْعَل | جَعَلَ | ج ع ل | V |
| 3 | لَّهُۥ |  |  | P;PRON |
| 4 | عَيْنَيْنِ | عَيْن | ع ي ن | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 90 — full text (context; no pericope)

- 90:1 لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ
- 90:2 وَأَنتَ حِلٌّۢ بِهَٰذَا ٱلْبَلَدِ
- 90:3 وَوَالِدٍۢ وَمَا وَلَدَ
- 90:4 لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِى كَبَدٍ
- 90:5 أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ
- 90:6 يَقُولُ أَهْلَكْتُ مَالًۭا لُّبَدًا
- 90:7 أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ
- 90:8 ◀ focus أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ
- 90:9 وَلِسَانًۭا وَشَفَتَيْنِ
- 90:10 وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ
- 90:11 فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ
- 90:12 وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ
- 90:13 فَكُّ رَقَبَةٍ
- 90:14 أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ
- 90:15 يَتِيمًۭا ذَا مَقْرَبَةٍ
- 90:16 أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ
- 90:17 ثُمَّ كَانَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ وَتَوَاصَوْا۟ بِٱلصَّبْرِ وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ
- 90:18 أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ
- 90:19 وَٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا هُمْ أَصْحَٰبُ ٱلْمَشْـَٔمَةِ
- 90:20 عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ


===== _commentary/v16/work/90_8/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج ع ل (root_000248) — identity root of نَجْعَل (w2)

- **B001** bir şeyi yapıp var etme — bir şeyi yapmak, yaratmak veya var etmek
  جعلت الشيء صنعته (maqayis)؛ جعل جعلا صنع صنعا (ayn)؛ جعل خلق؛ خلقنا (tahdhib)؛ يجري مجرى أوجد (mufradat)
- **B002** birini veya şeyi belirli bir duruma getirme — bir şeyi belirli bir duruma, niteliğe veya konuma getirmek · bir şeyi belirli bir duruma getirmek
  جعله الله نبيا أي صيره (sihah)؛ جعل صير؛ جعلته أحذق الناس؛ صيرهم؛ صيرته (tahdhib)
- **B003** öyle adlandırma ya da öyle olduğunu söyleme; başka yorumda öyle kılma — 
  جعلوا الملائكة إناثا أي سموهم (sihah)؛ جعل قال؛ أي قلناه؛ وقال غيره صيرناه (tahdhib)
- **B004** bir eylemi yapmaya başlama — bir şeyi yapmaya başlamak
  تقول جعل يقول ولا تقول صنع يقول (maqayis)؛ جعل يأكل وجعل يصنع كذا (ayn)؛ جعل فلان يصنع كذا كقولك طفق وعلق يفعل (tahdhib)؛ يجري مجرى صار وطفق فلا يتعدى نحو جعل زيد يقول (mufradat)
- **B005** iş karşılığı belirlenen ücret veya ortaklaşa kararlaştırılan ödeme — bir iş karşılığında belirlenen ücret, ödeme veya ödül · önemli bir iş için ortaklaşa kararlaştırılan ödemeler · ona bir ödeme veya armağan ayırmak
  الجعل والجعالة والجعلية ما يجعل للإنسان على الأمر يفعله (maqayis)؛ الجعل ما جعلت لإنسان أجرا له على عمل يعمله؛ الجعالات ما يتجاعل الناس بينهم (ayn)؛ الجعل ما جعل للانسان من شئ على الشئ يفعله؛ الجعالة؛ الجعيلة مثله (sihah)؛ الجعل في العطية؛ الجعالة بالفتح من الشيء تجعله للإنسان؛ ما جعلته للإنسان أجرا على عمله (tahdhib)
- **B006** kısa veya küçük hurma ağaçları — kısa veya küçük hurma ağaçları; tekili bu ağaçlardan biri
  الجعل النخل يفوت اليد والواحدة جعلة (maqayis)؛ الجعل واحدها جعلة وهي النخل الصغار (ayn)؛ الجعل النخل القصار الواحدة جعلة (sihah)؛ الجعل قصار النخل (tahdhib)
- **B007** sıcak tencereyi indirme bezi ve onunla indirme — sıcak tencereyi ateşten indirmeye yarayan koruyucu bez · tencereyi koruyucu bezle ateşten indirmek
  الجعال الخرقة التي تنزل بها القدر عن الأثافي (maqayis)؛ الجعال والجعالة خرقة تنزل بها القدر عن رأس النار يتقى بها من الحر (ayn)؛ الجعال الخرقة التي تنزل بها القدر عن النار؛ أجعلت القدر (sihah)؛ الجعال الخرقة التي تنزل بها القدور؛ أجعلت القدر إجعالا إذا أنزلتها بالجعال (tahdhib)
- **B008** kara küçük yer hayvanı ve bunlarla dolu su — kara renkli küçük bir yer hayvanı · bu hayvanların çokça bulunduğu su
  الجعل دابة من هوام الأرض (ayn)؛ الجعل دويبة؛ جعل الماء بالكسر أي كثر فيه الجعلان (sihah)؛ الجعل دابة سوداء من دواب الأرض تجمع جعلانا؛ ماء مجعل وجعل إذا تهافتت فيه الجعلان (tahdhib)
- **B009** dişinin çiftleşmek için erkeği istemesi — çiftleşmek isteyen dişi köpek · dişinin çiftleşmek için erkeği istemesi
  كلبة مجعل إذا أرادت السفاد (maqayis)؛ أجعلت الكبة واستجعلت فهي مجعل إذا أرادت السفاد وكذلك سائر السباع (sihah)؛ أجعلت الكلبة والسباع كلها إذا اشتهت الفحل؛ استجعلت أيضا بمعناه (tahdhib)
- **B010** deve kuşu yavrusu — deve kuşu yavrusu
  الجعول ولد النعام (maqayis)؛ الجعول الرأل ولد النعام (tahdhib)
- **B011** belirtilmemiş bir yer adı — kimliği belirtilmemiş bir yer adı
  الجَعْلة اسم مكان (maqayis)
- **B012** kısa, şişman ve inatçı olma — kısa, şişman ve inatçı kişi
  الجعل القصر مع السمن واللجاج (tahdhib)

## ع ي ن (root_001069) — identity root of عَيْنَيْنِ (w4)

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

===== _commentary/v16/out/s090/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 90:8, and ## Buluşmalar) =====
## Ölçüp biçmek: yaratma, güç ve pay

Dördüncü ayetin fiili {ar:خَلَقْنَا, tr:halaknâ, gloss:yarattık, source:90:4}, Arapçada önce bir zanaat işidir: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme izâ kaddertuhû kable'l-kat', gloss:deriyi kesmeden önce ölçüp biçtiğimde onu halakttım, source:"خ ل ق,B001"}. Bir başka söyleyiş de {ar:خلقت الأديم للسقاء إذا قدرته, tr:halaktu'l-edîme li's-sikâ izâ kaddertuh, gloss:deriyi su tulumu için ölçtüm, source:"خ ل ق,B001"}. Usta deriyi serer, üstüne tulumun şeklini çizer, sonra keser. Kelimenin özü de böyle tanımlanır: {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhu't-takdîru'l-mustekîm, gloss:yaratmanın aslı doğru ölçüdür, source:"خ ل ق,B001"}. Aynı kökten gelen "halâk" kelimesi ise payı adlandırır: {ar:الخلاق النصيب لأنه قد قدر لكل أحد نصيبه, tr:el-halâku'n-nasîb li-ennehû kad kuddira li-kulli ehadin nasîbuh, gloss:halâk paydır çünkü herkese payı ölçülmüştür, source:"خ ل ق,B006"}. Bu tek tanımda surenin üç kelimesi buluşur: yaratma, beşinci ayetin "kadara"sı ve beşinci ile yedinci ayetlerin "ehad"ı. Sekizinci ayetin {ar:أَلَمْ نَجْعَل, tr:e-lem nec'al, gloss:yapmadık mı, source:90:8} fiili de aynı işe bağlanır: {ar:جعل خلق؛ خلقنا, tr:ce'ale haleka; halaknâ, gloss:ce'ale yarattı demektir; yarattık, source:"ج ع ل,B001"}. Gözler, dil ve dudaklar ölçülerek kesilmiş parçalardır.

Beşinci ayet adamın sanısını söyler: {ar:أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ, tr:e-yahsebu en len yakdira aleyhi ehad, gloss:kimsenin ona güç yetiremeyeceğini mi sanıyor, source:90:5}. "Kadara" önce güçtür: {ar:قدر على الشيء قدرة أي ملك فهو قادر, tr:kadara ale'ş-şey'i kudreten ey meleke fe-huve kâdir, gloss:bir şeye güç yetirdi yani ona sahip oldu, source:"ق د ر,B003"}. Ama kökün altında ölçü yatar: {ar:مبلغ الشيء وكنهه ونهايته, tr:mebleğu'ş-şey'i ve kunhuhû ve nihâyetuh, gloss:bir şeyin vardığı yer ve özü ve sınırı, source:"ق د ر,B001"}. Allah'ın takdiri de bu ölçüyle tanımlanır: {ar:قضاء الله تعالى الأشياء على مبالغها ونهاياتها, tr:kadâullâhi te'âle'l-eşyâe alâ mebâliğihâ ve nihâyâtihâ, gloss:Allah'ın şeyleri ulaşacakları ölçüye ve sınıra göre belirlemesi, source:"ق د ر,B002"}. Fiil "ona karşı" ile kurulduğunda bir de rızkı daraltmayı anlatır: {ar:ومن قدر عليه رزقه أي ضيق عليه, tr:ve men kudira aleyhi rizkuhû ey duyyika aleyh, gloss:rızkı ona ölçülü verilen yani daraltılan, source:"ق د ر,B004"}. İnsanın kendi kurduğu hesap da aynı kökle anılır: {ar:التقدير من الإنسان التفكر في الأمر؛ فكر وقدر, tr:et-takdîru mine'l-insâni't-tefekkuru fi'l-emr; fekkera ve kaddera, gloss:insanın takdiri iş üzerine düşünmesidir; düşündü ve ölçtü, source:"ق د ر,B005"}. Adam, kendisini ölçecek ya da kendisine bir sınır çizecek kimse bulunmadığını sanır. Oysa dördüncü ayetin fiili onun zaten ölçülüp biçildiğini söylemiştir. Düz bir anlatımın kaçırdığı şey budur: "kimse bana güç yetiremez" sanısı, deri gibi ölçülüp kesilmiş bir varlığın ağzından çıkar.

Birinci ayetin yemin fiili {ar:لَآ أُقْسِمُ, tr:lâ uksimu, gloss:yemin ederim ki, source:90:1} de bu işin içine girer. Kökü bölüp paylaştırmayı anlatır: {ar:تجزئة شيء والنصيب قسم, tr:tecziyetu şey' ve'n-nasîbu kısm, gloss:bir şeyi parçalara ayırmak ve pay kısımdır, source:"ق س م,B003"}. Kök insanın kendi işini tartmasını da anlatır ve bunu "kadara" ile tanımlar: {ar:هو يقسم أمره قسما أي يقدره وينظر فيه كيف يفعل, tr:huve yaksimu emrahû kasmen ey yukaddiruhû ve yenzuru fîhi keyfe yef'al, gloss:işini bölüp tartıyor yani onu ölçüyor ve nasıl yapacağına bakıyor, source:"ق س م,B006"}. Böylece birinci, dördüncü ve beşinci ayetler tek bir işlemde buluşur: ölçmek ve paylaştırmak. Sanı ile sayım arasındaki fark da aynı fiilde durur. Kök hem saymayı ({ar:الحساب عدك الأشياء, tr:el-hisâbu addukel-eşyâ, gloss:hesap şeyleri saymandır, source:"ح س ب,B001"}) hem sanmayı bildirir. Adam saymak yerine sanır. "Ehad" kelimesinin olumsuz cümledeki işi de açıktır: {ar:أحد في النفي لاستغراق جنس الناطقين, tr:ehadun fi'n-nefyi li'stiğrâki cinsi'n-nâtıkîn, gloss:olumsuzlukta ehad konuşan türün tamamını kapsar, source:"ء ح د,B002"}. "Hiç kimse" demektir. Ama aynı kelime Kur'an'da Allah'ın adıdır: {ar:قُلْ هُوَ ٱللَّهُ أَحَدٌ, tr:kul huvallâhu ehad, gloss:de ki O Allah birdir, source:112:1}. Adamın "kimse" diye yok saydığı yerde kelime, onu ölçmüş olan Bir'i duyurur. Aynı surede {ar:لَمْ يَلِدْ وَلَمْ يُولَدْ, tr:lem yelid ve lem yûled, gloss:doğurmadı ve doğurulmadı, source:112:3} sözü de vardır. Bu, üçüncü ayetin doğuran ve doğurulan üzerine yeminini Bir'in karşısına koyar.

Kur'an aynı kalıbı Zünnûn için kurar. Allah onun öfkeyle gidişini anlatırken {ar:فَظَنَّ أَن لَّن نَّقْدِرَ عَلَيْهِ, tr:fe-zanne en len nakdira aleyh, gloss:ona güç yetiremeyeceğimizi sandı, source:21:87} der. Sanı, "len" ve "aleyhi" aynı sıradadır. Ardından gelen şey ise bir çağrıdır: {ar:فَنَادَىٰ فِى ٱلظُّلُمَٰتِ, tr:fe-nâdâ fi'z-zulumât, gloss:karanlıklar içinde seslendi, source:21:87}. Sanıyı aşan şey Rabbe dönüştür. Önceki sure, sınanan insanın iki halini anlatır. İkincisi şöyledir: {ar:فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ, tr:fe-kadara aleyhi rizkahû fe-yekûlu rabbî ehânen, gloss:rızkını ona ölçülü verince Rabbim beni aşağıladı der, source:89:16}. Fiil aynıdır, insan yine konuşur. Yaratma, ölçme ve yol gösterme başka bir surede tek bir dizide gelir: {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî haleka fe-sevvâ, gloss:yaratıp düzene koyan, source:87:2} ve {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:vellezî kaddera fe-hedâ, gloss:ölçüp yol gösteren, source:87:3}. Bu, surenin dördüncü, beşinci ve onuncu ayetlerinin sırasıdır. Musa da Firavun'a Rabbini {ar:ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:ellezî a'tâ kulle şey'in halkahû summe hedâ, gloss:her şeye yaratılışını verip sonra yol gösteren, source:20:50} diye tanıtır. İnsanın yaratılışı da aynı iki fiille anlatılır: {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe-kadderah, gloss:onu bir damladan yarattı ve ölçüsünü verdi, source:80:19}. Kendi ölçüsünü kuran adamın sonu da aynı fiille söylenir. Kendisine uzayıp giden mal verilen adam için {ar:إِنَّهُۥ فَكَّرَ وَقَدَّرَ, tr:innehû fekkera ve kaddera, gloss:o düşündü ve ölçtü, source:74:18} ve {ar:فَقُتِلَ كَيْفَ قَدَّرَ, tr:fe-kutile keyfe kaddera, gloss:kahrolası nasıl ölçtü, source:74:19} denir. "E-yahsebu" sorusu insana başka yerlerde de yöneltilir: {ar:أَيَحْسَبُ ٱلْإِنسَٰنُ أَلَّن نَّجْمَعَ عِظَامَهُۥ, tr:e-yahsebu'l-insânu ellen necme'a izâmeh, gloss:insan kemiklerini toplamayacağımızı mı sanıyor, source:75:3} ve {ar:أَيَحْسَبُ ٱلْإِنسَٰنُ أَن يُتْرَكَ سُدًى, tr:e-yahsebu'l-insânu en yutrake sudâ, gloss:insan başıboş bırakılacağını mı sanıyor, source:75:36}. Burada da "len" kalıbı vardır, ve sanının konusu Allah'ın gücünün sınırıdır. Son gün "ehad" kelimesi tersine döner: {ar:فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ, tr:fe-yevme'izin lâ yu'azzibu azâbehû ehad, gloss:o gün O'nun azabı gibi kimse azap edemez, source:89:25} ve {ar:وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ, tr:ve lâ yûsiku vesâkahû ehad, gloss:O'nun bağlaması gibi kimse bağlayamaz, source:89:26}. "Kimse bana güç yetiremez" diyen sanının karşısında, "kimse O'nun gibi bağlayamaz" sözü durur.

Kaynaklar: 90:4 خَلَقْنَا خ ل ق B001, B006; 90:8 نَجْعَل ج ع ل B001; 90:5 يَقْدِرَ ق د ر B001, B002, B003, B004, B005; 90:1 أُقْسِمُ ق س م B003, B006; 90:5 أَيَحْسَبُ ح س ب B001, B002; 90:7 أَيَحْسَبُ ح س ب B001, B002; 90:5 أَحَدٌۭ ء ح د B001, B002; 90:7 أَحَدٌ ء ح د B001, B002

## Gözetleyen göz

Yedinci ayetin sorusu görmekle ilgilidir: {ar:أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ, tr:e-yahsebu en lem yerahû ehad, gloss:onu hiç kimsenin görmediğini mi sanıyor, source:90:7}. Görmek duyuyla algılamaktır: {ar:الرؤية إدراك المرئي بالحاسة, tr:er-ru'yetu idrâku'l-mer'iyyi bi'l-hâssa, gloss:görme görüleni duyu ile algılamaktır, source:"ر ء ي,B001"}. Arapça "kimse yok" demek için "göz yok" da der: {ar:ما بها عين متحركة الياء تريد أحدا له عين, tr:mâ bihâ ayen, gloss:orada gözü olan kimse yok, source:"ع ي ن,B017"}. Bir başka söyleyiş de {ar:ما بها عائن، وكذلك ما بها عين، أي أحد, tr:mâ bihâ âin ve kezâlike mâ bihâ ayn ey ehad, gloss:orada gören yok ve göz yok yani kimse yok, source:"ع ي ن,B017"}. Dil "ehad" ile "ayn"ı aynı yere koyar. Böylece yedinci ayetin "kimse görmedi" sözü ile sekizinci ayetin {ar:أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ, tr:e-lem nec'al lehû ayneyn, gloss:ona iki göz vermedik mi, source:90:8} sorusu yan yana gelir. Adam gözü olan kimse bulunmadığını sanar, ve hemen ona verilmiş iki göz hatırlatılır. Gözü yapan, görmeyi bilmez mi? Göz kelimesinin ailesinde önce gören göz vardır: {ar:العين الناظرة لكل ذي بصر, tr:el-aynu'n-nâzıratu li-kulli zî basar, gloss:göz bakan her canlının bakan organıdır, source:"ع ي ن,B001"}. Koruyan göz de vardır: {ar:فلان بعيني أي أحفظه وأراعيه, tr:fulânun bi-aynî ey ehfazuhû ve urâ'îh, gloss:o benim gözümün önündedir yani onu korur ve gözetirim, source:"ع ي ن,B003"}. Haber toplayan göz, yani casus da vardır: {ar:العين الذي تبعثه يتجسس الخبر, tr:el-aynu'llezî teb'asuhû yetecessesu'l-haber, gloss:ayn haber toplamak için gönderdiğin casustur, source:"ع ي ن,B005"}.

Dördüncü ayetin "insân" kelimesinin ailesinde bir görüntü daha vardır: {ar:إنسان العين المثال الذي يرى في السواد أي سواد العين, tr:insânu'l-ayni'l-misâlu'llezî yurâ fi's-sevâd, gloss:gözün insanı gözün karasında görünen küçük suret, source:"ء ن س,B005"}. Birinin gözüne bakan, o gözün karasında kendi küçük suretini görür. Aynı kök görmeyi de bilir: {ar:آنست الشيء إذا رأيته وآنسته إذا سمعته, tr:âneztu'ş-şey'e izâ raeytuh, gloss:bir şeyi gördüğümde ya da duyduğumda onu ânestu, source:"ء ن س,B002"}. Kendini görülmez sanan insan, kelimenin ailesiyle duyulduğunda, bir gözün içinde görünen surettir.

Surenin öbür kelimeleri gözetleyenlerle doludur. On üçüncü ayetin {ar:رَقَبَةٍ, tr:rakabe, gloss:boyun, source:90:13} kelimesinin kökü beklemeyi ve gözetmeyi anlatır: {ar:رقبت الشيء أرقبه أي انتظرت والترقب تنظر الشيء وتوقعه, tr:rakabtu'ş-şey'e erkubuhû ey intazartu, gloss:bir şeyi gözettim yani bekledim; terakkub bir şeyi gözleyip ummaktır, source:"ر ق ب,B001"}. Bekçi de bu kökten gelir: {ar:الرقيب وهو الحافظ, tr:er-rakîbu ve huve'l-hâfız, gloss:rakîb koruyandır, source:"ر ق ب,B002"}. Gözetleme yeri de öyle: {ar:المرقبة هي المنظرة في رأس جبل أو حصن, tr:el-markabetu hiye'l-menzaratu fî ra'si cebelin ev hısn, gloss:markabe bir dağın ya da kalenin tepesindeki gözetleme yeridir, source:"ر ق ب,B003"}. On birinci ayetin geçidi bir dağdadır. Bu kökle duyulunca dağın tepesinde bir gözetleme yeri de belirir. Avcının siperi de bu kökle anılır: {ar:الرقيبة كل ما استترت به لترمي صيدا, tr:er-rakîbetu kullu mestetarte bihî li-termiye saydâ, gloss:rakîbe av vurmak için arkasına saklandığın her şeydir, source:"ر ق ب,B011"}. On ikinci ayetin {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ, tr:ve mâ edrâke me'l-akabe, gloss:sarp geçidin ne olduğunu sana ne bildirdi, source:90:12} sorusundaki fiilin ailesinde de bir avcı vardır: {ar:تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته, tr:tedarraytu's-sayde izâ nazartu eyne huve ve lem terahu ba'd, gloss:avın nerede olduğuna baktım ama onu henüz görmedim ve ona sinsice yaklaştım, source:"د ر ي,B003"}. Fiil, yedinci ayetteki görme fiilini kendi tanımında kullanır. Bilmek de bu kökle söylenir, ve bildiren Allah'tır: {ar:دريت الشيء والله أدرانيه, tr:deraytu'ş-şey'e vallâhu edrânîh, gloss:şeyi bildim ve onu bana Allah bildirdi, source:"د ر ي,B001"}. On dokuzuncu ayetin {ar:بِـَٔايَٰتِنَا, tr:bi-âyâtinâ, gloss:ayetlerimizi, source:90:19} kelimesi de uzaktan görülen bir işarettir: {ar:الآية العلامة, tr:el-âyetu'l-alâme, gloss:ayet işarettir, source:"ء ي ي,B003"} ve {ar:آية الرجل شخصه, tr:âyetu'r-raculi şahsuh, gloss:adamın ayeti uzaktan görünen bedenidir, source:"ء ي ي,B003"}. Kök birini bu görünen bedeninden hedef almayı da bilir: {ar:تآييته وتأييته إذا قصدت آيته وتعمدته, tr:teâyeytuhû izâ kasadtu âyetehû ve teammedtuh, gloss:onun görünen bedenini hedef alıp ona yöneldim, source:"ء ي ي,B002"}. Ayetleri inkâr edenler görülmesi gereken işaretleri örtenlerdir.

Bu görüntünün düz bir anlatımın veremeyeceği yanı şudur. Yedinci ayetteki sanı tek bir boşluk üstüne kuruludur: gözetleyen bir göz yoktur. Surenin kelimeleri ise bu boşluğu gözle, bekçiyle, tepe gözcüsüyle, siperdeki avcıyla doldurur. On ikinci ayet bu gözetimi hitap edilene çevirir: geçidin ne olduğunu insan kendisi göremez, bildirilmesi gerekir. Kur'an'da "ve mâ edrâke" sorusu çoğu kez ateşe açılır. Terazileri hafif gelen için {ar:وَمَآ أَدْرَىٰكَ مَا هِيَهْ, tr:ve mâ edrâke mâ hiyeh, gloss:onun ne olduğunu sana ne bildirdi, source:101:10} denir ve cevap {ar:نَارٌ حَامِيَةٌۢ, tr:nârun hâmiye, gloss:kızgın bir ateş, source:101:11} olur. Mal toplayıp sayan için {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ, tr:ve mâ edrâke me'l-hutame, gloss:hutamenin ne olduğunu sana ne bildirdi, source:104:5} denir ve cevap {ar:نَارُ ٱللَّهِ ٱلْمُوقَدَةُ, tr:nârullâhi'l-mûkade, gloss:Allah'ın tutuşturulmuş ateşi, source:104:6} olur. Bu surede aynı soru bir boyunu çözmeye ve bir ağzı doyurmaya açılır. Kitabı sol eline verilen adam ise o gün aynı fiili kendine çevirir: {ar:وَلَمْ أَدْرِ مَا حِسَابِيَهْ, tr:ve lem edri mâ hısâbiyeh, gloss:hesabımın ne olduğunu bilmeseydim, source:69:26}.

Kur'an'da görmenin sahneleri bu sanıyı tek tek bozar. Kulu namazdan alıkoyan adam için {ar:أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ, tr:e-lem ya'lem bi-ennallâhe yerâ, gloss:Allah'ın gördüğünü bilmiyor mu, source:96:14} denir. Önceki surede, helak edilen kavimlerin ardından {ar:إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ, tr:inne rabbeke le-bi'l-mirsâd, gloss:Rabbin gerçekten gözetleme yerindedir, source:89:14} denir. Allah insanı yarattığını, onun içinden geçeni bildiğini söyler ve {ar:وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ, tr:ve nahnu akrabu ileyhi min hableli'l-verîd, gloss:biz ona şah damarından daha yakınız, source:50:16} der. Ardından {ar:مَّا يَلْفِظُ مِن قَوْلٍ إِلَّا لَدَيْهِ رَقِيبٌ عَتِيدٌۭ, tr:mâ yelfızu min kavlin illâ ledeyhi rakîbun atîd, gloss:ağzından çıkan her sözün yanında hazır bir gözetleyici vardır, source:50:18} gelir. Söz, insan ve gözetleyici: altıncı ayetin "yekûlu"su da böyle bir rakîbin önünde söylenir. Ateşe sürülen Allah düşmanlarının kulakları, gözleri ve derileri onlara karşı tanıklık eder: {ar:شَهِدَ عَلَيْهِمْ سَمْعُهُمْ وَأَبْصَٰرُهُمْ وَجُلُودُهُم, tr:şehide aleyhim sem'uhum ve ebsâruhum ve culûduhum, gloss:kulakları ve gözleri ve derileri onlar aleyhine tanıklık etti, source:41:20}. Onlara söylenen söz sanıyı adlandırır: {ar:وَلَٰكِن ظَنَنتُمْ أَنَّ ٱللَّهَ لَا يَعْلَمُ كَثِيرًۭا مِّمَّا تَعْمَلُونَ, tr:ve lâkin zanentum ennallâhe lâ ya'lemu kesîran mimmâ ta'melûn, gloss:ama yaptıklarınızın çoğunu Allah'ın bilmediğini sandınız, source:41:22}. Verilen göz, sahibi aleyhine tanık olur. Yedinci ayetteki fiil başka bir surede tersine döner, bu kez gören yapanın kendisidir: {ar:فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ, tr:fe-men ya'mel miskâle zerratin hayran yerah, gloss:kim zerre ağırlığınca iyilik yaparsa onu görür, source:99:7}. Göze emanet etmek de Allah'ın sözünde vardır. Musa'ya, annesinin onu sandığa koyup suya bırakışını hatırlatırken {ar:وَلِتُصْنَعَ عَلَىٰ عَيْنِىٓ, tr:ve li-tusna'a alâ aynî, gloss:benim gözümün önünde yetiştirilesin diye, source:20:39} der. Verilip kullanılmayan göz de anılır: {ar:وَلَهُمْ أَعْيُنٌۭ لَّا يُبْصِرُونَ بِهَا, tr:ve lehum a'yunun lâ yubsırûne bihâ, gloss:gözleri vardır ama onlarla görmezler, source:7:179}. Semud da yol gösterilip körlüğü seçmiştir: {ar:وَأَمَّا ثَمُودُ فَهَدَيْنَٰهُمْ فَٱسْتَحَبُّوا۟ ٱلْعَمَىٰ عَلَى ٱلْهُدَىٰ, tr:ve emmâ semûdu fe-hedeynâhum fe'stehabbu'l-amâ ale'l-hudâ, gloss:Semud'a gelince onlara yol gösterdik ama körlüğü hidayete tercih ettiler, source:41:17}. Göz ile yol orada da birbirine bağlıdır: {ar:وَلَوْ نَشَآءُ لَطَمَسْنَا عَلَىٰٓ أَعْيُنِهِمْ فَٱسْتَبَقُوا۟ ٱلصِّرَٰطَ فَأَنَّىٰ يُبْصِرُونَ, tr:ve lev neşâu le-tamesnâ alâ a'yunihim fe'stebeku's-sırâta fe-ennâ yubsırûn, gloss:dileseydik gözlerini silerdik de yola koşuşurlardı ama nasıl görebilirlerdi, source:36:66}. Gözü veren de ayrıca anılır: {ar:وَجَعَلَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ, tr:ve ce'ale lekumu's-sem'a ve'l-ebsâra ve'l-ef'ide, gloss:size kulaklar ve gözler ve gönüller verdi, source:67:23}. Örtünün kalkışı da bir sahne olarak verilir: {ar:فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ, tr:fe-keşefnâ anke ğitâeke fe-basaruke'l-yevme hadîd, gloss:örtünü üstünden kaldırdık; bugün gözün keskindir, source:50:22}. Göz sonunda yakıcı olanı da görür: {ar:ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ, tr:summe le-teravunnehâ ayne'l-yakîn, gloss:sonra onu kesin bir gözle göreceksiniz, source:102:7}.

Kaynaklar: 90:7 يَرَهُۥٓ ر ء ي B001; 90:7 أَحَدٌ ء ح د B002; 90:8 عَيْنَيْنِ ع ي ن B001, B003, B005, B017; 90:4 ٱلْإِنسَٰنَ ء ن س B002, B005; 90:13 رَقَبَةٍ ر ق ب B001, B002, B003, B011; 90:12 أَدْرَىٰكَ د ر ي B001, B003; 90:19 بِـَٔايَٰتِنَا ء ي ي B002, B003

## Yapılmış beden ve ağzın iki yönlü işi

Sure bedeni parça parça adlandırır. Dördüncü ayetin "kebed"i, zorluk anlamının yanında içteki bir organın da adıdır: {ar:الأكباد جمع كبد وهي اللحمة السوداء في البطن, tr:el-ekbâdu cem'u kebid ve hiye'l-lahmetu's-sevdâu fi'l-batn, gloss:ekbâd kebidin çoğuludur ve o karındaki kara ettir, source:"ك ب د,B001"}. Yani ciğer. Aynı ayeti, kelimeyi dikliğe bağlayarak okuyan bir söyleyiş de vardır: {ar:خلقناه منتصبا معتدلا, tr:halaknâhu muntesıben mu'tedilâ, gloss:onu dik ve dengeli yarattık, source:"ك ب د,B009"}. Bir başka söyleyiş de {ar:الكبد الاستواء والاستقامة, tr:el-kebedu'l-istivâu ve'l-istikâme, gloss:kebed düzgünlük ve dikliktir, source:"ك ب د,B009"}. Yaratma fiilinin ailesi de tamlığı bilir: {ar:رجل خليق ومختلق أي تام الخلق معتدل, tr:raculun halîkun ve muhtelak ey tâmmu'l-halki mu'tedil, gloss:yaratılışı tam ve dengeli adam, source:"خ ل ق,B003"}. Ana karnındaki parça da öyle: {ar:مضغة مخلقة أي تامة الخلق, tr:mudğatun muhallaka ey tâmmetu'l-halk, gloss:yaratılışı tamamlanmış et parçası, source:"خ ل ق,B003"}. Sonra sekizinci ve dokuzuncu ayetler gelir: iki göz, bir dil, iki dudak. Dil konuşma organıdır: {ar:اللسان جارحة الكلام, tr:el-lisânu cârihatu'l-kelâm, gloss:dil konuşma organıdır, source:"ل س ن,B001"}. On üçüncü ayet çeneyi ve boynu getirir. "Fekk" çenedir: {ar:الفك اللحي, tr:el-fekku'l-lahy, gloss:fekk çene kemiğidir, source:"ف ك ك,B004"}. Bir başka söyleyiş de {ar:الفكان ملتقى الشدقين, tr:el-fekkâni multeka'ş-şidkayn, gloss:iki fekk iki yanağın buluştuğu yerdir, source:"ف ك ك,B004"}. Boyun da dikliğinden adını alır: {ar:الرقبة مؤخر أصل العنق, tr:er-rakabetu muahharu asli'l-unuk, gloss:rakabe boynun dibinin arkasıdır, source:"ر ق ب,B004"} ve {ar:اشتقاق الرقبة لأنها منتصبة, tr:iştikâku'r-rakabeti li-ennehâ muntesıba, gloss:rakabe dik durduğu için bu adı aldı, source:"ر ق ب,B004"}. Birinci ayetin "beled"i göğsü ({ar:البلدة الصدر وفلان واسع البلدة أي واسع الصدر, tr:el-beldetu's-sadr ve fulânun vâsi'u'l-belde, gloss:belde göğüstür ve göğsü geniş adama belde'si geniş denir, source:"ب ل د,B002"}), on altıncı ayetin "matrabe"si gerdanlık kemiklerini anar: {ar:الترائب موضع القلادة من الصدر, tr:et-terâibu mevdi'u'l-kılâdeti mine's-sadr, gloss:terâib göğüste gerdanlığın durduğu yerdir, source:"ت ر ب,B005"}. On sekizinci ayetin "meymene"si sağ elin adıyla kurulur: {ar:اليمين أصله الجارحة والميمنة ناحية اليمين, tr:el-yemînu asluhu'l-câriha ve'l-meymenetu nâhiyetu'l-yemîn, gloss:yeminin aslı eldir ve meymene sağ taraftır, source:"ي م ن,B002"}.

Bu sayımın düz bir anlatımın veremeyeceği yanı şudur: sure, kendini kimsenin görmediğini ve kimsenin ona güç yetiremeyeceğini sanan adamın bedenini, bir zanaatkârın tezgâhındaki parçalar gibi sayar. Gözler, dil ve dudaklar verilmiş araçlardır. Sorulacak şey bu araçların neye kullanıldığıdır.

Ağız bu bedenin en çok işleyen yeridir ve surede iki yönde çalışır. Dışarıya söz çıkar. Altıncı ayetin fiili dili kendi adıyla anar: {ar:المقول اللسان, tr:el-mikvelu'l-lisân, gloss:mikvel yani söyleyen dildir, source:"ق و ل,B002"}. "Yekûlu" ile "lisân" böylece aynı aletin işi ve adı olur. Dudak ağızdan ağıza konuşmayı adlandırır: {ar:المشافهة المخاطبة من فيك إلى فيه, tr:el-muşâfehetu'l-muhâtabetu min fîke ilâ fîh, gloss:müşafehe senin ağzından onun ağzına konuşmaktır, source:"ش ف ه,B002"}. Birçok ağzın içip neredeyse kuruttuğu su da dudak kökünün sözüdür: {ar:ماء مشفوة أي مطلوب مسؤول وهو الذي كثر عليه الناس وأنفدوه إلا أقله, tr:mâun meşfûh ey matlûbun mes'ûl, gloss:çok aranan ve istenen su ki insanlar üstüne üşüşüp azı dışında tüketmişlerdir, source:"ش ف ه,B003"}. İçeriye ise yemek girer. On dördüncü ayetin {ar:إِطْعَٰمٌۭ, tr:it'âm, gloss:doyurmak, source:90:14} kelimesi önce tatmaktır: {ar:الطعم ذوقه والطعام اسم جامع لكل ما يؤكل, tr:et-ta'mu zevkuh ve't-taâmu ismun câmi'un li-kulli mâ yu'kel, gloss:tat onun tadılmasıdır ve taam yenen her şeyin adıdır, source:"ط ع م,B001"}. Fiil iki kişi arasında işler: {ar:استطعمه سأله أن يطعمه وأطعمته الطعام, tr:istat'amehû seelehû en yut'imeh ve et'amtuhu't-taâm, gloss:ondan doyurmasını istedi ve ben ona yemek yedirdim, source:"ط ع م,B002"}. Biri ister, öbürü verir. Dil burada iki yönü birleştirir: {ar:استطعمني فلان الحديث إذا أرادك على أن تحدثه, tr:istat'amenî fulânun'l-hadîs, gloss:biri benden sözü tatmak istedi yani konuşmamı istedi, source:"ط ع م,B003"}. Söz de doyurulan bir şeydir. Kök bir yakınlık sahnesi de bilir: {ar:التطاعم إدخال الفم في الفم كما يفعل الحمام عند التقبيل, tr:et-tetâ'umu idhâlu'l-femi fi'l-fem, gloss:tetâum güvercinlerin öpüşürken yaptığı gibi ağzı ağza koymaktır, source:"ط ع م,B013"}. On üçüncü ayetin "fekk"i iki çenenin açılışını anlatır: {ar:فككت الشيء فانفك ككتاب مختوم تفك خاتمه وكما تفك الحنكين تفصل بينهما, tr:fekektu'ş-şey'e fe'nfekke ke-kitâbin mahtûm tefukku hâtemeh ve kemâ tefukku'l-hanekeyn, gloss:şeyi açtım ve açıldı; mühürlü bir mektubun mührünü açtığın ya da iki çeneyi birbirinden ayırdığın gibi, source:"ف ك ك,B001"}. Ters yüzü de vardır: {ar:أخذ فلان بمطعمة فلان إذا أخذ بحلقه يعصره, tr:ehaze fulânun bi-mat'ameti fulân izâ ehaze bi-halkıhî ya'suruh, gloss:birinin yemek yerinden tuttu yani boğazını tutup sıktı, source:"ط ع م,B012"}. Altıncı ayetin kökü sofralarda itişen adamı da adlandırır: {ar:يقال للمزاحم على الموائد المتهالك, tr:yukâlu li'l-muzâhimi ale'l-mevâid el-mutehâlik, gloss:sofralarda itişene mutehâlik denir, source:"ه ل ك,B012"}.

Surenin ağızla ilgili işleyişi buradan görünür. Altıncı ayette ağızdan övünme çıkar. On dördüncü ayette istenen şey başka ağızlara yemek koymaktır. Dil ve dudak doğru yöne çevrildiğinde ağız, boğazı sıkılan yoksulun ağzına doğru açılır.

Kur'an bedenin aynı çerçevesini başka bir yemin suresinde kurar: {ar:لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ, tr:lekad halaknâ'l-insâne fî ahseni takvîm, gloss:andolsun insanı en güzel biçimde yarattık, source:95:4}. Söz kalıbı dördüncü ayetle aynıdır, yalnız "kebed"in yerinde dik ve düzgün kuruluş vardır. Allah insanı annelerin karnından çıkardığını ve ona organlar verdiğini de söyler: {ar:وَٱللَّهُ أَخْرَجَكُم مِّنۢ بُطُونِ أُمَّهَٰتِكُمْ لَا تَعْلَمُونَ شَيْـًۭٔا, tr:vallâhu ahracekum min butûni ummehâtikum lâ ta'lemûne şey'â, gloss:Allah sizi hiçbir şey bilmezken annelerinizin karınlarından çıkardı, source:16:78}. İnsanın çıktığı su da terâib ile anılır: {ar:يَخْرُجُ مِنۢ بَيْنِ ٱلصُّلْبِ وَٱلتَّرَآئِبِ, tr:yahrucu min beyni's-sulbi ve't-terâib, gloss:bel ile göğüs kemikleri arasından çıkar, source:86:7}. Verilen organlar bir gün sahiplerine karşı konuşur: {ar:يَوْمَ تَشْهَدُ عَلَيْهِمْ أَلْسِنَتُهُمْ وَأَيْدِيهِمْ وَأَرْجُلُهُم, tr:yevme teşhedu aleyhim elsinetuhum ve eydîhim ve erculuhum, gloss:dillerinin ve ellerinin ve ayaklarının onlar aleyhine tanıklık edeceği gün, source:24:24}. Başka bir yerde de ağız mühürlenir: {ar:ٱلْيَوْمَ نَخْتِمُ عَلَىٰٓ أَفْوَٰهِهِمْ, tr:el-yevme nahtimu alâ efvâhihim, gloss:bugün ağızlarını mühürleriz, source:36:65}. Övünen ağız kapanır, el konuşur. Dilin düğümü de Kur'an'da bir duadır. Musa {ar:وَٱحْلُلْ عُقْدَةًۭ مِّن لِّسَانِى, tr:vahlul ukdeten min lisânî, gloss:dilimden düğümü çöz, source:20:27} ve {ar:يَفْقَهُوا۟ قَوْلِى, tr:yefkahû kavlî, gloss:sözümü anlasınlar, source:20:28} der. İkinci ayetin "hıll"i ile aynı kökten bir fiil, dil ve söz bir arada durur. İbrahim de yaratmayı, yol göstermeyi ve doyurmayı tek bir itirafta toplar: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:ellezî halakanî fe-huve yehdîn, gloss:beni yaratan ve bana yol gösteren O'dur, source:26:78} ve {ar:وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ, tr:vellezî huve yut'imunî ve yeskîn, gloss:beni yediren ve içiren O'dur, source:26:79}. Bu sıra surenin dördüncü, onuncu ve on dördüncü ayetleridir. Ağzın iki işi Kur'an'da birlikte de emredilir. Mirası paylaşırken yakınlar, yetimler ve yoksullar hazır bulunduğunda {ar:فَٱرْزُقُوهُم مِّنْهُ وَقُولُوا۟ لَهُمْ قَوْلًۭا مَّعْرُوفًۭا, tr:ferzukûhum minhu ve kûlû lehum kavlen ma'rûfâ, gloss:ondan onları rızıklandırın ve onlara güzel söz söyleyin, source:4:8}. Bir başka ölçü de verilir: {ar:قَوْلٌۭ مَّعْرُوفٌۭ وَمَغْفِرَةٌ خَيْرٌۭ مِّن صَدَقَةٍۢ يَتْبَعُهَآ أَذًۭى, tr:kavlun ma'rûfun ve mağfiretun hayrun min sadakatin yetbe'uhâ ezâ, gloss:güzel bir söz ve bağışlama ardından eziyet gelen sadakadan daha hayırlıdır, source:2:263}. Ters yüz de anılır: yetimlerin mallarını haksız yere yiyenler {ar:إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا, tr:innemâ ye'kulûne fî butûnihim nârâ, gloss:karınlarına ancak ateş yerler, source:4:10}. Yoksulun yemeğine teşvik etmeyen adamın orada {ar:وَلَا طَعَامٌ إِلَّا مِنْ غِسْلِينٍۢ, tr:ve lâ taâmun illâ min ğıslîn, gloss:irinden başka yemeği de yoktur, source:69:36}.

Kaynaklar: 90:4 كَبَدٍ ك ب د B001, B009; 90:4 خَلَقْنَا خ ل ق B003; 90:8 عَيْنَيْنِ ع ي ن B001; 90:9 وَلِسَانًۭا ل س ن B001; 90:9 وَشَفَتَيْنِ ش ف ه B002, B003; 90:13 فَكُّ ف ك ك B001, B004; 90:13 رَقَبَةٍ ر ق ب B004; 90:1 ٱلْبَلَدِ ب ل د B002; 90:16 مَتْرَبَةٍۢ ت ر ب B005; 90:18 ٱلْمَيْمَنَةِ ي م ن B002; 90:6 يَقُولُ ق و ل B002; 90:6 أَهْلَكْتُ ه ل ك B012; 90:14 إِطْعَٰمٌۭ ط ع م B001, B002, B003, B012, B013

## Buluşmalar

Görüntülerin en sık buluştuğu sahne yoldur. Onuncu ayetteki "necd" yolu kendi kendine yol gösterir, ateşin kökü de yüksek yerde yol gösterilsin diye yakılan ateşi anlatır. Sırt ile işaret ateşi aynı işi görür: gece yolcusuna nereye çıkacağını göstermek. Musa'nın sahnesi bu iki görüntüyü tek bir ayette taşır: dağın yanında görülen ateş ve {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidu ale'n-nâri hudâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10} umudu. Bu surede ise yolun sonundaki ateş bir işaret değildir, üstü kapatılmıştır. Yol sahnesiyle ateş sahnesi arasındaki fark, bir yolculuğun nasıl tersine döndüğünü gösterir. Atılmayan geçidin karşısında, içine dalınan bir ateş vardır: {ar:هَٰذَا فَوْجٌۭ مُّقْتَحِمٌۭ مَّعَكُمْ, tr:hâzâ fevcun muktehimun meakum, gloss:bu sizinle birlikte içeri dalan bir kalabalıktır, source:38:59}. Sabrın kökü de bu iki sahne arasında ikiye bölünür. Yokuşta kendini panikten tutan sabır vardır. Bir de kitabı gizleyenlerin {ar:فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ, tr:fe-mâ asberahum ale'n-nâr, gloss:ateşe karşı ne kadar dayanıklılar, source:2:175} sözündeki ateşe cüret vardır.

İkinci büyük buluşma boyunla kapak arasındadır. On üçüncü ayetin fiili Arapçada kapalıyı açmak olarak tanımlanır: {ar:فكاك الرهن وهو فتحه من الانغلاق, tr:fikâku'r-rahni ve huve fethuhû mine'l-inğılâk, gloss:rehnin fikâkı onu kapalılıktan açmaktır, source:"ف ك ك,B002"}. Yirminci ayetin fiili de kapamak olarak tanımlanır: {ar:أوصدت الباب أغلقته, tr:evsadtu'l-bâbe ağlaktuh, gloss:kapıyı kapattım yani kilitledim, source:"و ص د,B001"}. Sure açılan bir boyundan kapanan bir ateşe doğru ilerler, ve iki fiil birbirinin tam tersidir. Bu iki ucu Kur'an'da tek bir sahne birleştirir. Kitabı sol eline verilen adamın boynu bağlanır ve bunun sebebi yoksulun yemeğine teşvik etmemesidir: {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:ve yoksulun yemeğine teşvik etmiyordu, source:69:34}. Sol taraf, boyundaki halka ve doyurulmayan yoksul bir aradadır. Malının bir işe yaramadığını söyleyen ve gücünün yok olup gittiğini gören de aynı adamdır. Bu sahnede sağ ile sol, harcanan mal, kıtlık ve boyun görüntüleri aynı yerde durur. Altıncı ayetteki "tükettim" orada şu söze döner: {ar:هَلَكَ عَنِّى سُلْطَٰنِيَهْ, tr:heleke annî sultâniyeh, gloss:gücüm benden yok olup gitti, source:69:29}.

Üçüncü buluşma yeminle geçit arasındadır. Yeminin kefareti ayeti, surenin on üçüncü ve on dördüncü ayetlerini birlikte sayar. Yeminler düğümlenir, sonra on yoksul doyurulur ya da bir boyun çözülür. Birinci ayetin yemini, ikinci ayetin "hıll"i, geçidin iki işi, on sekizinci ayetin sağ eli ve on dokuzuncu ayetin örtme kökü, bir yeminin bağlanıp çözülmesinin bütün aşamalarını taşır. Kur'an'ın bahçe sahipleri ise yemini ters yönde kullanır: yoksulu dışarıda bırakmak için yemin ederler. Bu ikisinin karşı karşıya gelmesi, surenin açılış yemininin neye açıldığını gösterir. Bu yemin bir şehirle başlar, şehirdeki yoksulun ağzıyla devam eder.

Gözetleyen göz ile harcanan mal, gösteriş kelimesinde buluşur. Gösteriş için harcayan, insanların görmesini ister ama Allah'ın görmediğini sanır. Bu çelişki tek bir ayette sahnelenir: malını {ar:رِئَآءَ ٱلنَّاسِ, tr:riâe'n-nâs, gloss:insanlara gösteriş için, source:2:264} harcayanın emeği kayanın üstündeki toprak gibi yıkanır gider. Aynı misal yere yapışma görüntüsünü de taşır: toprak, kaya ve yağmurla çıplak kalan taş. Ölçme görüntüsü de aynı ayete girer: {ar:لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟, tr:lâ yakdirûne alâ şey'in mimmâ kesebû, gloss:kazandıklarından hiçbir şeye güç yetiremezler, source:2:264}. "Kimse bana güç yetiremez" sanısı, kendi kazancına güç yetirememekle biter. Ölçme ile yol da Kur'an'da tek bir dizide buluşur, ve bu dizi surenin sırasıdır: yaratan, ölçen, yol gösteren.

Soy ile kıtlık "yetim" kelimesinde buluşur. Babasından kopan çocuk, iyiliğin geç ulaştığı ve açlık gününde açlık çeken çocuktur. Dil bu ikisini tek bir örnekte birleştirir: {ar:يتيم ذو مسغبة أي ذو مجاعة, tr:yetîmun zû mesğabe ey zû mecâa, gloss:açlık sahibi yetim yani kıtlık içindeki yetim, source:"س غ ب,B001"}. Şehir ile kıtlık da kıtlık yılının tanımında buluşur: yıl bedevileri şehirlere atar. Kur'an'da doyurulan şehrin sahnesi de buradadır: {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ellezî at'amehum min cû'in ve âmenehum min havf, gloss:onları açlıktan doyuran ve korkudan güvenliğe kavuşturan, source:106:4}. Yere yapışma ile geçit, yükselme ile saplanmanın aynı ayette karşı karşıya geldiği sahnede buluşur: ayetlerle yükseltilebilecekken yere saplanan adam. Bu da on dokuzuncu ayetin ayetleri inkâr edenlerine bağlanır.

Bütün bu görüntüler birlikte surenin hareketini taşır. Hareket yere oturmuş bir şehirde başlar. İnsan zorluğun ortasında yaratılmıştır. Malı keçeleşmiştir, kendini görülmez ve ölçülmez sanır. Ona gözler, dil ve dudaklar verilmiş, önüne görünen iki sırt konmuştur. İstenen şey yukarıya atılmaktır. Bu atılış da yere yapışmış olana eğilmek, bir boynun düğümünü çözmek ve aç bir ağza yemek koymaktır. Böyle atılanlar bitkiler gibi birbirine bitişir, aynı rahimden çıkmış gibi birbirine acır ve sağ tarafa yerleşir. Ayetleri örtenlerin üstü ise, yolda yol gösterebilecek bir ateşle kapatılır. Mağara sahnesindeki eşikte köpek ön ayaklarını uzatmış yatar: {ar:وَكَلْبُهُم بَٰسِطٌۭ ذِرَاعَيْهِ بِٱلْوَصِيدِ, tr:ve kelbuhum bâsitun zirâ'ayhi bi'l-vasîd, gloss:köpekleri iki ön ayağını eşiğe uzatmıştı, source:18:18}. Aynı ayette uyuyanlar sağa ve sola çevrilir. Yirminci ayetin kökü, sağ ve sol ile o eşiği orada tek bir sahnede bir araya getirir.

