Focus: 101:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/101_6/D.r13/context.md =====
# 101:6 — focus

فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ

Anchor translation (canonical reading, reference only):

Tartıları ağır gelen kişiye gelince,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَأَمَّا | أَمَّا |  | REM;EXL |
| 2 | مَن | مَن |  | COND |
| 3 | ثَقُلَتْ | ثَقُلَتْ | ث ق ل | V |
| 4 | مَوَٰزِينُهُۥ | مِيزَان | و ز ن | N;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 101 — full text (context; no pericope)

- 101:1 ٱلْقَارِعَةُ
- 101:2 مَا ٱلْقَارِعَةُ
- 101:3 وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ
- 101:4 يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ
- 101:5 وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ ٱلْمَنفُوشِ
- 101:6 ◀ focus فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ
- 101:7 فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ
- 101:8 وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ
- 101:9 فَأُمُّهُۥ هَاوِيَةٌۭ
- 101:10 وَمَآ أَدْرَىٰكَ مَا هِيَهْ
- 101:11 نَارٌ حَامِيَةٌۢ


===== _commentary/v16/work/101_6/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ث ق ل (root_000202) — identity root of ثَقُلَتْ (w3)

- **B001** ağırlık — bir şeyin ağır gelmesi, hafif olmaması · ağırlık, maddi ya da soyut ağır gelme niteliği · ağır, ağırlık taşıyan
  ضد الخفة (maqayis;sihah)؛ ثقل ثقلا فهو ثقيل والثقل رجحان الثقيل (ayn;tahdhib)؛ الثقل والخفة متقابلان وأصله في الأجسام ثم في المعاني (mufradat)
- **B002** ağır yükler — yolcunun eşyası ve beraberindeki taşınır yük · yükler, eşyalar veya yerin çıkardığı ağır şeyler · yüklerinizi taşır
  أثقال الأرض كنوزها وأجساد بني آدم (maqayis;sihah;mufradat)؛ متاع المسافر وحشمه وجمعه أثقال (ayn;sihah;tahdhib)؛ تحمل أثقالكم أي أحمالكم الثقيلة (mufradat)
- **B003** günah yükü — kişiyi ağırlaştıran günahlar ve sorumluluklar · günah yüküyle ağırlaşmış kimse
  الأثقال الآثام (ayn)؛ حاملة أوزار وخطايا (ayn)؛ أوزارهم وأوزار من أضلوا وهي الآثام (tahdhib)؛ أثقالهم آثامهم التي تثقلهم وتثبطهم (mufradat)
- **B004** ölçü ağırlığı — bilinen ağırlık ölçüsü veya tartı ağırlığı · bir şeyin ağırlığı kadar ölçü · ona ağırlığını ver · hayvanı tartıp ağırlığını yokladı · ağırlığı eksik olmayan dinar
  المثقال وزن معلوم قدره ومثقال الشيء ميزانه من مثله (ayn;tahdhib)؛ أعطه ثقله أي وزنه وثقلت الشاة (sihah;tahdhib)؛ المثقال ما يوزن به وهو اسم لكل سنج (mufradat)
- **B005** değer ağırlığı — kıymetli, korunmuş veya itibarlı şey · büyük önemleri sebebiyle birlikte anılan iki varlık ya da değerli iki emanet · büyük değeri ve etkisi olan söz
  سمي الجن والإنس الثقلين (maqayis;sihah;tahdhib)؛ كل شيء نفيس مصون ثقل ويقال للسيد العزيز ثقل (tahdhib)؛ قولا ثقيلا يعني عظم قدره وجلالة خطره وقول له وزن (tahdhib)؛ الثقيل في الإنسان يستعمل في المدح (mufradat)
- **B006** ağırlık ve halsizlik — içte, bedende veya yemekten sonra duyulan ağırlık ve gevşeklik · bastıran uyku hali · hastalık onu ağırlaştırdı · uyku ona ağır bastı · ağırlaşmış, yavaş veya gücünü aşan yük altında kalmış · ağırdan alma, yavaşlama ve ayak sürüme · sözün kulağa hoş gelmemesi veya kabulünün ağır gelmesi
  أجد في نفسي ثقلة (maqayis)؛ الثقلة نعسة غالبة وأثقله المرض واستثقله النوم والمثقل البطيء والتثاقل من التباطؤ (ayn)؛ وجدت ثقلة في جسدي أي ثقلا وفتورا (sihah)؛ الثقلة ما وجد الإنسان من ثقل الطعام وأصبح ثاقلاء أثقله المرض (tahdhib)؛ اثاقلتم إلى الأرض (mufradat)
- **B007** gebelikte ağırlaşma — kadının gebelik yüküyle ağırlaşması · gebeliği ağırlaşmış kadın
  اثقلت المرأة فيه مثقل (ayn)؛ أثقلت المرأة فهي مثقل أي ثقل حملها في بطنها (sihah)؛ المثقل من النساء التي قد ثقلت من حملها (tahdhib)
- **B008** dolgun kalçalı ağırbaşlı kadın [kalıp] — dolgun kalçalı veya mecliste ağırbaşlı kadın
  امرأة ثقال أي ذات مآكم وكفل (ayn;sihah;tahdhib)؛ هذه امرأة ثقال وهذه امرأة رزان أي رزينة في مجلسها (tahdhib)
- **B009** işitme ağırlığı [kalıp] — kulağında ağırlık var, işitmesi zayıf
  في أذنه ثقل إذا لم يجد سمعه كأنه يثقل عن قبول ما يلقى إليه (mufradat)

## و ز ن (root_001645) — identity root of مَوَٰزِينُهُۥ (w4)

- **B001** tartarak veya yaklaşık ölçüp biçerek niceliği belirleme — bir şeyi tartmak veya ölçüsünü belirlemek · hurma ürününün miktarını yaklaşık kestirmek · bir şeyin ağırlık ölçüsü · bir dirhem ağırlığında gelmek · bir kimse için veya ona karşı bir şeyi tartmak · kendisi için tartılanı teslim almak
  وزنت الشيء وزنا؛ الزنة قدر وزن الشيء (maqayis)؛ الوزن ثقل شيء بشيء مثله؛ وزن الشيء إذا قدره؛ وزن ثمر النخل إذا خرصه (ayn;tahdhib)؛ وزنت الشئ وزنا وزنة؛ هذا يزن درهما (sihah)؛ الوزن معرفة قدر الشيء؛ ما يقدر بالقسط والقبان (mufradat)
- **B002** tartı aracı ve adil değerlendirme ölçütü — terazi · teraziler ve tartı ağırlıkları · hesapta adil ve denk değerlendirme
  بناء يدل على تعديل واستقامة (maqayis)؛ الميزان ما وزنت به (ayn)؛ الميزان معروف (sihah)؛ الموازين واحدها ميزان وهو المثاقيل؛ الآلة التي يوزن بها الأشياء ميزان؛ الميزان العدل (tahdhib)؛ مراعاة المعدلة؛ الوزن يومئذ الحق فإشارة إلى العدل في محاسبة الناس (mufradat)
- **B003** iki şeyi denk veya karşılıklı konumda tutma — iki şeyi karşılaştırıp birbirine denklemek · bu, ötekiyle aynı ölçüde veya onun hizasındadır · dağın yanı veya hizası · bu, ötekiyle zihinde denk tutulur
  هذا يوازن ذلك أي هو محاذيه (maqayis)؛ وازنت بين الشيئين؛ هذا يوازن هذا إذا كان على زنته أو كان محاذيه؛ هو وزن الجبل أي ناحية منه؛ هو زنة الجبل أي حذاءه (sihah)؛ هذا في وزن هذا؛ قام في النفس مساويا لغيره (tahdhib)
- **B004** günün tam ortasına gelmesi [kalıp] — gün ortalandı
  قام ميزان النهار إذا انتصف النهار (maqayis;mufradat)؛ قام ميزان النهار أي انتصف (sihah)
- **B005** sağlam yargı ve kararlı yöneliş [kalıp] — sağlam ve ağırbaşlı düşünceli · yargısı güçlü ve aklı sağlam · kendini o işe hazırlayıp kararlılıkla yönelmek
  وزين الرأى معتدله؛ راجح الوزن إذا نسبوه إلى رجاحة الرأي وشدة العقل (maqayis)؛ رجل وزين الرأي وقد وزن وزانة إذا كان متثبتا (ayn;tahdhib)؛ فلان وزين الرأي أي رزينه (sihah)؛ أوزن فلان نفسه على الأمر إذا وطن نفسه عليه (tahdhib)
- **B006** kısa boylu, kimi kullanımda aklı başında kadın — kısa boylu kız · kısa boylu, aklı başında kadın · kısa boylu kadın
  جارية موزونة فيها قصر (ayn;tahdhib)؛ امرأة موزونة قصيرة عاقلة؛ الوزنة المرأة القصيرة (tahdhib)
- **B007** toplumsal değer; eksiksiz ağırlıktaki para [kalıp] — bizim yanımızda hiçbir değeri ve saygınlığı yok · onlara hiçbir değer ve saygınlık tanımayız · tam ağırlıktaki dirhem
  درهم وازن أي تام (sihah)؛ ما لفلان عندنا وزن أي قدر لخسته؛ فلا نقيم لهم يوم القيامة وزنا (tahdhib)؛ فلا نقيم لهم يوم القيامة وزنا (mufradat)
- **B008** ölçülü ve dengeli yaratılmış şey [kalıp] — ölçülü ve dengeli yaratılmış şey
  بناء يدل على تعديل واستقامة (maqayis)؛ وأنبتنا فيها من كل شيء موزون؛ قيل هو المعادن كالفضة والذهب؛ كل ما أوجده الله وأنه خلقه باعتدال (mufradat)

===== _commentary/v16/out/s101/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 101:6, and ## Buluşmalar) =====
## Terazi: ağır kefe, hafif kefe

Altıncı ve sekizinci ayetler iki kefeyi karşı karşıya koyar: {ar:فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ, tr:fe-emmâ men sekulet mevâzînuhû, gloss:tartıları ağır gelen kimseye gelince, source:101:6} ve {ar:وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ, tr:ve emmâ men haffet mevâzînuhû, gloss:tartıları hafif gelen kimseye gelince, source:101:8}. Tartmanın tanımı, bir şeyin ağırlığını benzeriyle karşılaştırmaktır: {ar:الوزن ثقل شيء بشيء مثله, tr:el-vezn siklu şey'in bi-şey'in mislih, gloss:vezn, bir şeyin ağırlığını benzeri olan bir şeyle ölçmektir, source:"و ز ن,B001"}. Ağır olan kefe aşağı iner: {ar:الثقل رجحان الثقيل, tr:es-sikal rüchânu's-sakîl, gloss:ağırlık, ağır olanın basıp inmesidir, source:"ث ق ل,B001"}. Miskal, benzerine karşı konan bilinen bir ağırlıktır {source:"ث ق ل,B004"}. Mîzân ise hem alet hem adalettir: {ar:الآلة التي يوزن بها الأشياء ميزان؛ الميزان العدل, tr:el-âletu elletî yûzenu bihe'l-eşyâ', gloss:şeylerin tartıldığı alet mîzândır; mîzân adalettir, source:"و ز ن,B002"}.

Bu imgenin düz anlatımın ötesinde gösterdiği şey, ağırlığın değer olmasıdır. Değerli ve korunan her şey ağır sayılır: {ar:كل شيء نفيس مصون ثقل, tr:kullu şey'in nefîsin masûnin sekal, gloss:değerli, korunan her şey sekaldir, source:"ث ق ل,B005"}; insanlar ve cinler "iki ağırlık" diye anılır: {ar:سمي الجن والإنس الثقلين, tr:summiye'l-cinnu ve'l-insu's-sekaleyn, gloss:cinler ve insanlar iki ağırlık diye adlandırıldı, source:"ث ق ل,B005"}. Yerin ağırlıkları, onun hazineleri ve Âdemoğullarının bedenleridir {source:"ث ق ل,B002"}. Hafiflik ise tersine değersizliktir: {ar:ما لفلان عندنا وزن أي قدر لخسته, tr:mâ li-fulânin indenâ vezn, gloss:filanın yanımızda bir ağırlığı yok, yani değeri yok, source:"و ز ن,B007"}. Hafif gelmek hem ağırlıkta hem halde hafifliktir, {ar:الخفة خفة الوزن وخفة الحال, tr:el-hiffe hiffetu'l-vezn ve hiffetu'l-hâl, gloss:hafiflik, ağırlığın ve halin hafifliğidir, source:"خ ف ف,B001"}, iyi amellerin azlığıdır {source:"خ ف ف,B003"}, akıl hafifliğidir, {ar:وخفة الرجل طيشه, tr:ve hiffetu'r-raculi tayşuh, gloss:adamın hafifliği onun savrukluğudur, source:"خ ف ف,B004"}, ve hafife alınmaktır: {ar:استخف به أهانه, tr:istehaffe bihî, gloss:onu hafife aldı, aşağıladı, source:"خ ف ف,B005"}. Hafif olan kolayca yerinden oynatılır ve peşe takılır: {ar:استخفه فلان إذا استجهله فحمله على اتباعه في غيه, tr:istehaffehû fulân, gloss:onu cahil yerine koydu ve sapkınlığında kendisine uymaya sürükledi, source:"خ ف ف,B004"}.

Surenin öbür kelimeleri bu teraziyi önceden kurar. Dördüncü ayetin pervanesi hafifliğinden dolayı bu adı almıştır: {ar:الفراش هذا الذي يطير وسمي بذلك لخفته؛ الفراشة الرجل الخفيف, tr:sumiye bi-zâlike li-hiffetih; el-ferâşe er-raculu'l-hafîf, gloss:pervane hafifliğinden ötürü böyle adlandırıldı; ferâşe hafif adamdır, source:"ف ر ش,B005"}; {ar:أطيش من فراشة, tr:etyaşu min ferâşe, gloss:pervaneden daha savruk, source:"ف ر ش,B005"}. Burada geçen savrukluk, sekizinci ayetin hafifliğini anlatan kelimenin ta kendisidir. Beşinci ayetin yünü içi boş liftir {source:"ن ف ش,B002"}; dağ ise iri, kalın gövdedir: {ar:ذو جبلة إذا كان غليظ الجسم, tr:zû cebeletin izâ kâne ğalîza'l-cism, gloss:iri gövdeli olan, source:"ج ب ل,B003"}. Yeryüzünün en ağır şeyi, en hafif şeye dönüşür. Dokuzuncu ayetin fiili hem hızlı bir düşüşü hem hızlı bir yükselişi anlatır: {ar:الهوي السريع إلى أسفل والهوي السريع إلى فوق, tr:el-huviyy es-serî' ilâ esfel ve'l-heviyy es-serî' ilâ fevk, gloss:aşağıya hızlı iniş ve yukarıya hızlı çıkış, source:"ه و ي,B002"}. Bir terazide hafif kefe yukarı kalkar; dokuzuncu ayette ise hafif kefenin sahibi aşağı düşer.

Kâria kelimesinin bir anlamı da ortaklar arasında paylaşılacak bir şey için kura çekmektir: {ar:أقرعت بين الشركاء في شيء يقتسمونه فاقترعوا عليه, tr:akra'tu beyne'ş-şurakâ', gloss:paylaşacakları bir şey için ortaklar arasında kura çektim, source:"ق ر ع,B004"}; {ar:الإقراع والمقارعة هي المساهمة, tr:el-ikrâ' ve'l-mukâra'a hiye'l-musâheme, gloss:kura çekmek, pay için ok atmaktır, source:"ق ر ع,B004"}. Bu adı taşıyan sureden sonra insanlar "fe-emmâ ... ve emmâ" ile iki paya ayrılır. Ama ayırma kura ile değil, iki şeyi karşı karşıya koyarak yapılır: {ar:وازنت بين الشيئين, tr:vâzentu beyne'ş-şey'eyn, gloss:iki şeyi tarttım, birbiriyle karşılaştırdım, source:"و ز ن,B003"}. Payı belirleyen tesadüf değil, ölçüdür. Kur'an'da kura çekilen iki sahne vardır: Sâffât suresinde Yûnus yüklü gemide {ar:فَسَاهَمَ فَكَانَ مِنَ ٱلْمُدْحَضِينَ, tr:fe-sâheme fe-kâne mine'l-mudhadîn, gloss:kura çekti ve kaybedenlerden oldu, source:37:141}; Âl-i İmrân suresinde Allah, Peygambere Meryem'in kimin himayesine gireceği için {ar:إِذْ يُلْقُونَ أَقْلَٰمَهُمْ أَيُّهُمْ يَكْفُلُ مَرْيَمَ, tr:iz yulkûne eklâmehum eyyuhum yekfulu Meryem, gloss:hangisinin Meryem'e bakacağı için kalemlerini atarlarken, source:3:44} orada olmadığını söyler.

Kur'an'da teraziyi açıkça kuran ayetler surenin kelimelerini aynen tekrarlar. A'râf suresinde Allah {ar:وَٱلْوَزْنُ يَوْمَئِذٍ ٱلْحَقُّ ۚ فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ, tr:ve'l-veznu yevmeizini'l-hakk, fe-men sekulet mevâzînuhû fe-ulâike humu'l-muflihûn, gloss:o gün tartı haktır; kimin tartıları ağır gelirse işte onlar kurtuluşa erenlerdir, source:7:8} ve {ar:وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُم, tr:ve men haffet mevâzînuhû fe-ulâike'llezîne hasirû enfusehum, gloss:kimin tartıları hafif gelirse, işte onlar kendilerini kaybedenlerdir, source:7:9} der. Mü'minûn suresi aynı çifti verir {source:23:102} ve hafif gelenlerin {ar:فِى جَهَنَّمَ خَٰلِدُونَ, tr:fî cehenneme hâlidûn, gloss:cehennemde ebedî kalıcıdırlar, source:23:103} olduğunu ekler. Enbiyâ suresinde Allah {ar:وَنَضَعُ ٱلْمَوَٰزِينَ ٱلْقِسْطَ لِيَوْمِ ٱلْقِيَٰمَةِ, tr:ve neda'u'l-mevâzîne'l-kıst li-yevmi'l-kıyâme, gloss:kıyamet günü için adalet terazilerini kurarız, source:21:47} der ve hardal tanesi ağırlığında bir şeyi bile getireceğini söyler. Kehf suresinde, ağırlıksızlığın değersizlik olduğu açıkça söylenir: {ar:فَلَا نُقِيمُ لَهُمْ يَوْمَ ٱلْقِيَٰمَةِ وَزْنًۭا, tr:fe-lâ nukîmu lehum yevme'l-kıyâmeti veznâ, gloss:kıyamet günü onlar için hiçbir tartı kurmayız, source:18:105}. Zilzâl suresinde yer {ar:وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا, tr:ve ahraceti'l-ardu eskâlehâ, gloss:yer ağırlıklarını dışarı çıkarır, source:99:2}, ve zerre ağırlığındaki her iyilik görülür: {ar:فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ, tr:fe-men ya'mel miskâle zerratin hayran yerah, gloss:kim zerre ağırlığında bir iyilik yaparsa onu görür, source:99:7}. Hafifliğin peşe takılmak olduğunu da Kur'an sahneler: Zuhruf suresinde Firavun {ar:فَٱسْتَخَفَّ قَوْمَهُۥ فَأَطَاعُوهُ, tr:fe'stehaffe kavmehû fe-etâûh, gloss:kavmini hafife aldı, onlar da ona uydular, source:43:54}; Rûm suresinde Allah Peygambere, kesin inanmayanların onu hafifletip yerinden oynatmamasını söyler {source:30:60}.

Kaynaklar: 101:6 ثَقُلَتْ ث ق ل B001; 101:6 ثَقُلَتْ ث ق ل B002; 101:6 ثَقُلَتْ ث ق ل B004; 101:6 ثَقُلَتْ ث ق ل B005; 101:6 مَوَٰزِينُهُۥ و ز ن B001; 101:6 مَوَٰزِينُهُۥ و ز ن B002; 101:6 مَوَٰزِينُهُۥ و ز ن B003; 101:8 مَوَٰزِينُهُۥ و ز ن B007; 101:8 خَفَّتْ خ ف ف B001; 101:8 خَفَّتْ خ ف ف B003; 101:8 خَفَّتْ خ ف ف B004; 101:8 خَفَّتْ خ ف ف B005; 101:4 كَٱلْفَرَاشِ ف ر ش B005; 101:5 ٱلْمَنفُوشِ ن ف ش B002; 101:5 ٱلْجِبَالُ ج ب ل B003; 101:9 هَاوِيَةٌ ه و ي B002; 101:1 ٱلْقَارِعَةُ ق ر ع B004

## Buluşmalar

İmgelerin ilk buluşma yeri dördüncü ve beşinci ayetlerdir. Bir darbe iner ve sıkı olanı dağıtır; bu dağılmanın iki yüzü vardır. Yünün atılması bir dövmedir {source:"ن ف ش,B001"}, dolayısıyla dağların yüne dönmesi, birinci ayetin vuruşunun eseridir. Aynı kelime, menfûş, geceleyin çobansız yayılan sürüyü de anlatır {source:"ن ف ش,B003"}; dağılan dağ ile dağılan sürü tek kelimede birleşir. Dördüncü ayetin ferâşı da hem serili yeri hem saçılan sürüyü taşır; bu iki anlamı bağlayan açıklama, ferşi beşş ile anlatır {source:"ف ر ش,B004"}. Yeryüzünü döşeyen serme işi ile kıyametteki saçılma aynı iki kelimeyle söylenir.

İkinci buluşma, pervane ile terazidir. Pervane hafifliğinden ötürü bu adı almıştır ve savruk adama ferâşe denir {source:"ف ر ش,B005"}; sekizinci ayetin hafifliği de akıl savrukluğudur {source:"خ ف ف,B004"}. Dördüncü ayetin pervane insanları, sekizinci ayetin tartıları hafif gelenleridir. Bu iki imge birlikte surenin hareketini taşır: hafif olan, ışığa doğru savrulur ve ateşe düşer. Pervanenin birbiri ardınca kandile düşüşü {source:"ف ر ش,B005"} ile topluluğun birbiri ardınca çukura düşüşü {source:"ه و ي,B002"} aynı hareketi verir; dokuzuncu ayetin ümm kelimesi hedefe yönelmeyi {source:"ء م م,B012"}, on birinci ayetin ateşi de o hedefin kendisini adlandırır. Böylece dördüncü ayetteki saçılma ile on birinci ayetteki ateş, surenin iki ucunda aynı sahnenin başı ve sonudur. Hâmiye kelimesinin insanların sakındığı korunmuş şeyi anlatan kolu {source:"ح م ي,B002"}, pervanenin yaptığının tersini gösterir.

Üçüncü buluşma, ana ile çukurdur ve bu ikisi yaşayışın karşısında durur. "Anası düştü" deyimi dokuzuncu ayetin iki kelimesini birlikte taşır {source:"ه و ي,B002"}; ümm kelimesinin toplayan, kendine katan anlamı {source:"ء م م,B002"} çukuru, düşeni içine alan yer yapar. Yedinci ayetin yaşayışı ise hayattır {source:"ع ي ش,B001"}; evladını yitirmiş ananın karşısında yaşayan biri. Nâziât suresinin iki sığınağı {source:79:39} {source:79:41} bu karşıtlığı Kur'an'ın kendi sözleriyle kurar.

Dördüncü buluşma çukur ile terazi, ve çukur ile dağlar arasındadır. Hâmiye kuyunun duvarını ören ağır taşlardır {source:"ح م ي,B011"}; içine düşen ise tartısı hafif gelendir. Dağlar en ağır, en kalın kütleydi {source:"ج ب ل,B003"} ve atılmış yünün içi boşluktur {source:"ن ف ش,B002"}; hâviyenin kökü de boşluktur {source:"ه و ي,B001"}. Kazıcıyı durduran kaya {source:"ج ب ل,B005"} yok olunca, çukurun dibi de yoktur. Terazide ağırlık değerse, dağların ağırlığının yüne dönmesi, kıyamet günü dünyanın ağır saydığı şeylerin ağırlıksızlaştığını, tek ağırlığın tartının kefesinde kaldığını gösterir.

Son buluşma, kapı ile ateş arasındadır. Surenin başındaki vuruş üç kez sorulur ve bir sahneyle cevaplanır; onuncu ayetteki soru ise hemen, kızgın bir ateşle cevaplanır. Hümeze suresi aynı soru ile aynı türden cevabı verir {source:104:5} {source:104:6}. Savaş günü imgesi de bu iki ucu birleştirir: başta kılıçların çarpışması {source:"ق ر ع,B002"}, sonda topluluk içinde patlak veren düşmanlık ve kızışan öfke {source:"ن و ر,B007"} {source:"ح م ي,B003"}. Böylece sure bir kapı vuruşuyla, bir uyarıyla açılır ve bir ateşle kapanır; aradaki her kelime, o vuruşun neyi dağıttığını, neyi tarttığını ve hafif olanı nereye düşürdüğünü gösterir.

