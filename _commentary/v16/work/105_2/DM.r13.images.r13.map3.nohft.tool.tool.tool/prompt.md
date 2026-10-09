Focus: 105:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/105_2/D.r13/context.md =====
# 105:2 — focus

أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ

Anchor translation (canonical reading, reference only):

Onların planını boşa çıkarmadı mı?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | أَلَمْ | لَم |  | INTG;NEG |
| 2 | يَجْعَلْ | جَعَلَ | ج ع ل | V |
| 3 | كَيْدَهُمْ | كَيْد | ك ي د | N;PRON |
| 4 | فِى | فِى |  | P |
| 5 | تَضْلِيلٍ | تَضْلِيل | ض ل ل | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 105 — full text (context; no pericope)

- 105:1 أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ
- 105:2 ◀ focus أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ
- 105:3 وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ
- 105:4 تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ
- 105:5 فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ


===== _commentary/v16/work/105_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج ع ل (root_000248) — identity root of يَجْعَلْ (w2)

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

## ك ي د (root_001334) — identity root of كَيْدَهُمْ (w3)

- **B001** bir şeyi yoğun çabayla işleme — bir şeyi yoğun çabayla işleme ve onunla uğraşma · onu yoğun çabayla ele alıp işlemek
  يدل على معالجة لشيء بشدة (maqayis)؛ الكيد المعالجة (maqayis)؛ كل شيء تعالجه فأنت تكيده (maqayis;sihah)
- **B002** dolaylı ve gizli düzen kurma — dolaylı düzen ve tuzak · gizli ve aldatıcı düzen · birine tuzak kurmak · karşılıklı tuzak kurma yarışı · onlara kötülük etmeye kesin karar vermek · cezaya götüren süre tanıma ve erteleme
  يسمون المكر كيدا (maqayis)؛ الكيد من المكيدة وقد كاده يكيده مكيدة (ayn)؛ الكيد المكر وكاده يكيده كيدا ومكيدة وكذلك المكايدة (sihah)؛ الكيد ضرب من الاحتيال وقد يكون مذموما وممدوحا والاستدراج والمكر (mufradat)؛ لأريدن بها سوءا (mufradat)؛ الإملاء والإمهال المؤدي إلى العقاب (mufradat)
- **B003** can çekişerek can verme [kalıp] — can çekişmek ve canını vermek üzere olmak
  هو يكيد بنفسه أي يجود بها (maqayis;sihah;mufradat)؛ رأيته يكيد بنفسه أي يسوق سياقا (ayn)
- **B004** karşılaşılmayan savaş [kalıp] — savaşla karşılaşmamak
  الكيد الحرب يقال خرجوا ولم يلقوا كيدا أي حربا (maqayis)؛ ربما سمي الحرب كيدا يقال غزا فلان فلم يلق كيدا (sihah)
- **B005** karganın var gücüyle bağırması — karganın var gücüyle bağırması
  صياح الغراب بجهد (maqayis)؛ يسمى اجتهاد العرب في صياحه كيدا (sihah)
- **B006** ateşi yavaş ve güçlükle çıkarma [kalıp] — çakmak taşının ateşi yavaşça ve güçlükle çıkarması
  أن يخرج الزند النار ببطء وشدة (maqayis)؛ كاد الزند إذا تباطأ بإخراج ناره (mufradat)
- **B007** kusma ve kusmuk — kusma veya kusmuk
  الكيد القيء (maqayis)؛ وكذلك القيء (sihah)
- **B008** aybaşı görme için seyrek bir ad — kimi zaman aybaşı görme anlamında kullanılan ad
  ربما سموا الحيض كيدا (maqayis)

## ض ل ل (root_000913) — identity root of تَضْلِيلٍ (w5)

- **B001** doğru yoldan ve amaçtan sapma ya da başkasını saptırma — doğru yoldan, amaçtan veya doğruluktan sapmak · doğru yoldan ve doğruluktan sapma · doğru yoldan veya amaçtan sapmış kimse · sapmada direnen, çok sapmış kimse · iyilikten uzak, yanlış ve boş işlere dalmış kimse · asılsız ve yanlış düşünceler · birini doğru yoldan saptırmak · bir kimseyi sapmış saymak · yanlışlığın ve sapmanın içine düşülen yer · yolun bulunamadığı şaşırtıcı arazi · o işi yanlış ve sağduyusuz bir tutumla yapmak
  كل جائر عن القصد ضال؛ الضلال والضلالة بمعنى (maqayis); ضل إذا جار عن القصد؛ لا يوفق لخير صاحب غوايات وبطالات (ayn); الضلال ضد الهدى؛ ضل في الأمر إذا لم يهتد له؛ ضل في الأرض إذا لم يهتد للسبيل (jamhara); الضلال والضلالة ضد الرشاد؛ رجل ضليل ومضلل أي ضال جدا (sihah); الإضلال في كلام العرب ضد الهداية والإرشاد؛ ضل الكافر غاب عن الحجة؛ ضل فلان عن القصد إذا جار (tahdhib)
- **B002** gizlenerek, karışıp eriyerek veya gömülerek gözden yitme — gizlenip gözden kaybolmak · ölüyü gömüp gözden kaldırmak · bir sıvının ötekine karışıp içinde kaybolması · kaya altında güneş görmeyen su
  أضل الميت إذا دفن؛ ضل اللبن في الماء ثم استهلك (maqayis); ضل الشيء إذا خفي وغاب؛ أئذا ضللنا في الأرض أي خفينا وغبنا (jamhara); أضل الميت إذا دفن؛ أضل عنه أي أخفى عليه وأغيب؛ أئذا ضللنا في الأرض أي خفينا وغبنا (sihah); أصل الضلال الغيبوبة؛ ضل الماء في اللبن؛ أضلت بنو قيس عميدها أي دفنته (tahdhib)
- **B003** bir şeyi yitirme veya yerini bulamama; özel olarak kanın karşılıksız kalması — bir şeyin kaybolması, yitip gitmesi veya yok olması · devesini ya da başka bir hayvanını kaybetmek · evin, ibadet yerinin ya da başka bir yerin konumunu bulamamak · bir işin elinden kaçması ve ona güç yetirememek · kanı yerde kalmak, öcü alınmamak · yitme veya yok olma
  أضللت بعيري إذا ذهب منك؛ ضللت المسجد والدار إذا لم تهتد لهما (maqayis); ضللت مكاني إذا لم تهتد له؛ أضل بعيره إذا أفلت فذهب (ayn); ذهب فلان ضلة إذا لم يدر أين ذهب؛ ذهب دمه ضلة إذا لم يثأر به (jamhara); أضللت بعيري إذا ذهب منك؛ ضللت المسجد والدار إذا لم تعرف موضعهما (sihah); أضللت الشيء إذا ضاع منك؛ ضللت الشيء أضله إذا جعلته في مكان ولم تدر أين هو (tahdhib)
- **B004** bir şeyi unutmak veya bellekte tutamamak [kalıp] — bir şeyi unutmak ya da belleğinde tutamamak
  ضللت الشيء أنسيته (jamhara); إن تضل أي إن تنس؛ أن تضل إحداهما أي تغيب عن حفظها أو يغيب حفظها عنها (tahdhib)
- **B005** sahibi bilinmeyen kayıp hayvan, özellikle deve — sahibi bilinmeyen kayıp hayvan, özellikle deve · sahibi bilinmeyen kayıp hayvanlar veya develer
  الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها الذكر والأنثى فيه سواء (ayn); الضالة ما ضل من البهيمة للذكر والأنثى (sihah); الضالة من الإبل التي بمضيعة لا يعرف لها مالك؛ الجميع الضوال (tahdhib)

===== _commentary/v16/out/s105/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 105:2, and ## Buluşmalar) =====
## Görmeye çağrı ve yanılan yargı

Sûre bir soruyla açılır ve bu soru okuru seyirci yerine koyar: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ, tr:elem tera keyfe feale rabbüke, gloss:Rabbinin ne yaptığını görmedin mi, source:105:1}. Olumsuz kurulmuş bu soru bir bilgi istemez, "evet" cevabını baştan varsayar; hitap edilen, olayı zaten bilen biri olarak konuşturulur. {ar:تَرَ, tr:tera, gloss:görürsün, source:105:1} fiilinin kökü önce gözün görmesidir, {ar:الرؤية بالعين, tr:er-ru'yetu bi'l-ayn, gloss:gözle görme, source:"ر ء ي,B001"}; ama iki nesne aldığında bilmek anlamına geçer, {ar:بمعنى العلم تتعدى إلى مفعولين, tr:bi-ma'ne'l-ilm teteaddâ ilâ mef'ûleyn, gloss:bilmek anlamında iki nesne alır, source:"ر ء ي,B002"}. Aynı kökten gelen "gördün mü?" sorusu ise bir dikkat çağrısıdır: {ar:يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه, tr:yecrî e-raeyte mecrâ ahbirnî ve küllü zâlike fîhi ma'ne't-tenbîh, gloss:"gördün mü" "bana haber ver" yerine geçer, hepsinde uyarma anlamı vardır, source:"ر ء ي,B013"}. Bu üç kat bir arada çalışır: olay bir sahne gibi göz önüne konur, gözle izlenmemiş olsa da gözle görülmüş kadar kesin bir bilgi sayılır ve dinleyenin dikkati ona çekilir. Kökün ettirgen biçimi bir adım daha atar: {ar:أريته الشيء فرآه, tr:ereytuhu'ş-şey'e fe-raâhu, gloss:ona şeyi gösterdim, o da gördü, source:"ر ء ي,B012"} ve {ar:وأرى الله الناس بفلان, tr:ve erallâhu'n-nâse bi-fulân, gloss:Allah insanlara falanca üzerinden (bir ibret) gösterdi, source:"ر ء ي,B012"}. Sûrede gösteren Rab, gösterilen ise filin sahipleridir; onlar bir sergi nesnesine dönüşür.

Bu sûrede kelimelerin kök ailesinden gelen imgeler, kelimenin kendi ayetindeki anlamının yerine geçmez, onun yanında duyulur: fil yine fildir, taş yine taştır; kök yalnızca arka planda ikinci bir ses verir. Bu ikinci ses burada şudur: sağlam görmeye çağrılan okurun karşısında, öbür tarafın kelimeleri yanılan görüşü taşır. {ar:ٱلْفِيلِ, tr:el-fîl, gloss:fil, source:105:1} kökünün bir dalı zayıf görüşü ve işaretleri yanlış okumayı adlandırır: {ar:رجل فَيِل الرأي, tr:raculun feyilu'r-ra'y, gloss:görüşü zayıf adam, source:"ف ي ل,B001"}, {ar:رجل فال أي ضعيف الرأي مخطئ الفراسة, tr:raculun fâl, ey daîfu'r-ra'y muhti'u'l-firâse, gloss:fâl adam, yani görüşü zayıf, sezgisi yanılan, source:"ف ي ل,B001"}. Bu ifadede "görüş" diye çevrilen kelime, {ar:تَرَ, tr:tera, gloss:görürsün, source:105:1} ile aynı köktendir. Böylece açılış ayetinin iki ucunda aynı kök iki zıt hâlde durur: okura "gör" denir, karşı tarafın adı ise görüşün çürüklüğünü fısıldar. Bu bir kök özdeşliği değil, bir aile imgesidir; fil kelimesi ayette yalnızca hayvanı söyler.

İkinci ayetin {ar:تَضْلِيلٍ, tr:tadlîl, gloss:saptırılma, yolunu kaybettirme, source:105:2} kelimesinin kökü yolda kaybolmanın yanında bir işte doğruyu bulamamayı da adlandırır: {ar:ضل في الأمر إذا لم يهتد له, tr:dalle fi'l-emr izâ lem yehtedi leh, gloss:bir işin yolunu bulamadığında "o işte saptı" denir, source:"ض ل ل,B001"}. Üçüncü ayetin kuşları, {ar:طَيْرًا, tr:tayran, gloss:kuşlar, source:105:3}, Arapçada fal bakılan şeydir: {ar:تطير من الشيء فاشتقاقه من الطير, tr:tetayyera mine'ş-şey', fe'ştikâkuhu mine't-tayr, gloss:bir şeyden uğursuzluk çıkardı; türeyişi kuştandır, source:"ط ي ر,B003"}, {ar:الطائر من الزجر في التشؤم والتسعد, tr:et-tâ'ir mine'z-zecr fi't-teşe'üm ve't-tese'ud, gloss:kuş, uğur ve uğursuzluk için okunan işarettir, source:"ط ي ر,B003"}. Burada kuşlar bir şeyin habercisi değildir; okunacak işaret olmaktan çıkıp doğrudan vurucunun kendisi olurlar. Dördüncü ayetin fiili {ar:تَرْمِيهِم, tr:termîhim, gloss:onları atıyordu, source:105:4} kökünde isabet etmeyen tahmini de taşır: {ar:رمى فلان يرمي إذا ظن ظنا غير مصيب, tr:ramâ fulânun yermî izâ zanne zannen gayra musîb, gloss:isabetsiz bir zanda bulunduğunda "attı" denir, source:"ر م ي,B009"}. Ayetteki atış ise hedefini bulur. Taşlar, {ar:بِحِجَارَةٍ, tr:bi-hicâratin, gloss:taşlarla, source:105:4}, aklı da adlandıran bir köktendir: {ar:العقل يسمى حجرا لأنه يمنع من إتيان ما لا ينبغي, tr:el-aklu yusemmâ hicran li-ennehû yemneu min ityâni mâ lâ yenbagî, gloss:akla "hicr" denir, çünkü yakışmayanı yapmaktan alıkoyar, source:"ح ج ر,B002"}. Kendilerini alıkoyacak "hicr"i olmayanlara, aynı kökün öbür anlamı, taş, iner.

Kur'an bu bağı kendisi sahneler. Fecr sûresinde Allah yeminlerini sıraladıktan sonra sorar: {ar:هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ, tr:hel fî zâlike kasemun li-zî hicr, gloss:bunda akıl sahibi için bir yemin var mı, source:89:5}; hemen ardından gelen ayet bu sûrenin açılış kalıbının aynısıdır: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ, tr:elem tera keyfe feale rabbüke bi-âd, gloss:Rabbinin Âd'a ne yaptığını görmedin mi, source:89:6}. Orada sahne Âd'dan Semûd'a ve Firavun'a uzanır ve {ar:فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ, tr:fe-sabbe aleyhim rabbüke sevta azâb, gloss:Rabbin üzerlerine bir azap kamçısı döktü, source:89:13} ile kapanır. "Hicr sahibi" ile "görmedin mi" yan yana durur: görmeye çağrılan, aklı olandır. İbrahim sûresinde Allah, yıkılmış zalimlerin yurtlarında oturanlara {ar:وَتَبَيَّنَ لَكُمْ كَيْفَ فَعَلْنَا بِهِمْ, tr:ve tebeyyene leküm keyfe fealnâ bihim, gloss:onlara ne yaptığımız size apaçık belli olmuştu, source:14:45} der; aynı "nasıl yaptı" burada açıkça görülmüş bir bilgi olarak geri gelir. En'âm sûresinde inkârcılara {ar:أَلَمْ يَرَوْا۟ كَمْ أَهْلَكْنَا مِن قَبْلِهِم, tr:elem yerav kem ehleknâ min kablihim, gloss:kendilerinden önce nice nesli helak ettiğimizi görmediler mi, source:6:6} denir; görmek yine tarihin bilgisi demektir.

Yanlış görmenin sahneleri de Kur'an'dadır. Âd kavmi vadilerine yönelen bulutu görür ve yanılır: {ar:قَالُوا۟ هَٰذَا عَارِضٌۭ مُّمْطِرُنَا, tr:kâlû hâzâ âridun mumtirunâ, gloss:"bu bize yağmur getirecek bir bulut" dediler, source:46:24}; ayetin devamı onun bir azap rüzgârı olduğunu söyler, sonraki ayet de sonucu gösterir: {ar:فَأَصْبَحُوا۟ لَا يُرَىٰٓ إِلَّا مَسَٰكِنُهُمْ, tr:fe-asbahû lâ yurâ illâ mesâkinuhum, gloss:sabaha yalnızca evleri görünür hâlde çıktılar, source:46:25}. Tûr sûresinde inkârcılar için {ar:وَإِن يَرَوْا۟ كِسْفًۭا مِّنَ ٱلسَّمَآءِ سَاقِطًۭا يَقُولُوا۟ سَحَابٌۭ مَّرْكُومٌۭ, tr:ve in yerav kisfen mine's-semâ'i sâkitan yekûlû sehâbun merkûm, gloss:gökten düşen bir parça görseler "üst üste yığılmış bulut" derler, source:52:44} denir. Firavun'un ailesi başlarına gelen kötülüğü {ar:يَطَّيَّرُوا۟ بِمُوسَىٰ وَمَن مَّعَهُۥٓ, tr:yettayyerû bi-mûsâ ve men meah, gloss:Musa'dan ve beraberindekilerden uğursuzluk çıkarırlar, source:7:131} ve Allah cevap verir: {ar:أَلَآ إِنَّمَا طَٰٓئِرُهُمْ عِندَ ٱللَّهِ, tr:elâ innemâ tâ'iruhum indallâh, gloss:bilin ki onların "kuşu" Allah katındadır, source:7:131}. Kuş falının düzeltildiği yer burasıdır: işaret insanın elinde değil, Allah katındadır. Mülk sûresinde inkârcılara {ar:أَوَلَمْ يَرَوْا۟ إِلَى ٱلطَّيْرِ فَوْقَهُمْ صَٰٓفَّٰتٍۢ وَيَقْبِضْنَ, tr:e-ve lem yerav ile't-tayri fevkahum sâffâtin ve yakbidn, gloss:üstlerinde kanat açıp kapayan kuşları görmediler mi, source:67:19} denir ve Nûr sûresinde aynı tekil hitap kuşları gösterir: {ar:أَلَمْ تَرَ أَنَّ ٱللَّهَ يُسَبِّحُ لَهُۥ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱلطَّيْرُ صَٰٓفَّٰتٍۢ, tr:elem tera ennallâhe yusebbihu lehû men fi's-semâvâti ve'l-ardi ve't-tayru sâffât, gloss:göklerde ve yerde olanların ve kanat çırpan kuşların Allah'ı tesbih ettiğini görmedin mi, source:24:41}. Bu sûrede kuşa bakmak bir kehanet değil, Rabbin işini görmektir.

Kur'an aynı zamanda belirleyici gücün görünmediğini de söyler. Ahzâb sûresinde Allah mü'minlere, üzerlerine ordular geldiği günü hatırlatır: {ar:فَأَرْسَلْنَا عَلَيْهِمْ رِيحًۭا وَجُنُودًۭا لَّمْ تَرَوْهَا, tr:fe-erselnâ aleyhim rîhan ve cunûden lem teravhâ, gloss:üzerlerine bir rüzgâr ve sizin görmediğiniz ordular gönderdik, source:33:9}. Bu sûrede ise ordu görünür kılınır: kuşlar vardır, taşlar vardır, ve okura "görmedin mi" denir. Aynı kalıp başka ilahi işlerin üzerine de kurulur: {ar:أَلَمْ تَرَ إِلَىٰ رَبِّكَ كَيْفَ مَدَّ ٱلظِّلَّ, tr:elem tera ilâ rabbike keyfe medde'z-zıll, gloss:Rabbinin gölgeyi nasıl uzattığını görmedin mi, source:25:45}; Nuh da kavmine {ar:أَلَمْ تَرَوْا۟ كَيْفَ خَلَقَ ٱللَّهُ سَبْعَ سَمَٰوَٰتٍۢ طِبَاقًۭا, tr:elem teravâ keyfe halakallâhu seb'a semâvâtin tıbâkâ, gloss:Allah'ın yedi göğü kat kat nasıl yarattığını görmediniz mi, source:71:15} der. İki sûre sonra aynı kökün dikkat çağrısı yeniden açılır: {ar:أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ, tr:e-raeyte'llezî yukezzibu bi'd-dîn, gloss:dini yalanlayanı gördün mü, source:107:1}.

Kaynaklar: 105:1 تَرَ ر ء ي B001; 105:1 تَرَ ر ء ي B002; 105:1 تَرَ ر ء ي B013; 105:1 تَرَ ر ء ي B012; 105:1 ٱلْفِيلِ ف ي ل B001; 105:2 تَضْلِيلٍ ض ل ل B001; 105:3 طَيْرًا ط ي ر B003; 105:4 تَرْمِيهِم ر م ي B009; 105:4 بِحِجَارَةٍ ح ج ر B002

## Emekle kurulan düzen, yoldan çıkarılması ve iki "kılma"

Sûrenin iskeleti bir yapış ve iki kılmadır. {ar:فَعَلَ, tr:feale, gloss:yaptı, source:105:1} nasıl yapıldığı sorulan işi açar; {ar:يَجْعَلْ, tr:yec'al, gloss:kılmak, source:105:2} ve {ar:فَجَعَلَهُمْ, tr:fe-cealehum, gloss:onları ... kıldı, source:105:5} bu soruyu cevaplayan iki dönüştürmedir. Arada gönderme ve atma durur. Yapmak fiilinin kökü bir şeyi meydana getirmektir: {ar:أصل صحيح يدل على إحداث شيء من عمل وغيره, tr:aslun sahîhun yedullu alâ ihdâsi şey'in min amelin ve gayrih, gloss:bir işle ya da başka yolla bir şeyi meydana getirmeyi gösteren sağlam bir köktür, source:"ف ع ل,B001"}. Kılmak ise bir şeyi bir hâle sokmaktır: {ar:جعل صير, tr:ceale: sayyera, gloss:"ceale", "dönüştürdü" demektir, source:"ج ع ل,B002"}, {ar:جعله الله نبيا أي صيره, tr:cealehullâhu nebiyyen, ey sayyerah, gloss:Allah onu peygamber kıldı, yani o hâle getirdi, source:"ج ع ل,B002"}, ve yapıp ortaya koymaktır: {ar:جعلت الشيء صنعته, tr:cealtu'ş-şey'e: sana'tuh, gloss:şeyi "kıldım", yani yaptım, source:"ج ع ل,B001"}.

Bu iki kılmanın ilkinin nesnesi onların düzenidir: {ar:أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍ, tr:elem yec'al keydehum fî tadlîl, gloss:onların düzenini boşa çıkarmadı mı, source:105:2}. {ar:كَيْدَهُمْ, tr:keydehum, gloss:onların tuzağı, düzeni, source:105:2} kökü önce bir şey üzerinde güçle uğraşmaktır: {ar:يدل على معالجة لشيء بشدة, tr:yedullu alâ muâlecetin li-şey'in bi-şidde, gloss:bir şeyle sertçe uğraşmayı gösterir, source:"ك ي د,B001"}, {ar:كل شيء تعالجه فأنت تكيده, tr:küllu şey'in tuâlicuhû fe-ente tekîduh, gloss:uğraştığın her şeyi "keyd" edersin, source:"ك ي د,B001"}. Sonra bu emek gizli bir düzene, zarar vermeye kurulmuş bir hileye dönüşür: {ar:الكيد المكر وكاده يكيده كيدا ومكيدة, tr:el-keydu'l-mekr, ve kâdehû yekîduhû keyden ve mekîde, gloss:keyd, gizli tuzaktır, source:"ك ي د,B002"}, {ar:الكيد ضرب من الاحتيال, tr:el-keydu darbun mine'l-ihtiyâl, gloss:keyd bir tür hiledir, source:"ك ي د,B002"}, {ar:لأريدن بها سوءا, tr:le-urîdenne bihâ sû'â, gloss:ona mutlaka kötülük kastedeceğim, source:"ك ي د,B002"}. Kelime böylece bir yolculuğun emeğini ve onun bir hedefe kurulmuş kastını birlikte taşır.

İlk "kılma" bu emeği {ar:تَضْلِيلٍ, tr:tadlîl, gloss:saptırılma, source:105:2} içine yerleştirir. Kelime, birini ya da bir şeyi yoldan çıkarma eylemini anlatan bir mastardır; düzen kendiliğinden sapmaz, saptırılır. Kökün ilk resmi doğru yoldan ayrılmaktır: {ar:كل جائر عن القصد ضال, tr:küllu câ'irin ani'l-kasdi dâll, gloss:hedefe giden yoldan sapan herkes "dâll"dır, source:"ض ل ل,B001"}, {ar:ضل في الأرض إذا لم يهتد للسبيل, tr:dalle fi'l-ard izâ lem yehtedi li's-sebîl, gloss:yolu bulamadığında "yeryüzünde saptı" denir, source:"ض ل ل,B001"}. İkinci resim gidilen yeri bulamamaktır ve kullanımın kendi örneği bir mescit ile bir evdir: {ar:ضللت المسجد والدار إذا لم تهتد لهما, tr:daleltu'l-mescide ve'd-dâr izâ lem tehtedi lehumâ, gloss:mescide ve eve yolunu bulamadığında "onları kaybettim" dersin, source:"ض ل ل,B003"}; yanında sahibinin elinden kaçıp giden hayvan durur: {ar:أضل بعيره إذا أفلت فذهب, tr:edalle baîrahû izâ efleta fe-zeheb, gloss:devesi elinden kurtulup gidince "devesini kaybetti" denir, source:"ض ل ل,B003"}. Üçüncü resim gözden kaybolup erimektir: {ar:ضل اللبن في الماء ثم استهلك, tr:dalle'l-leben fi'l-mâ'i summe'stuhlik, gloss:süt suyun içinde kayboldu, sonra tükendi, source:"ض ل ل,B002"}, {ar:أضل الميت إذا دفن, tr:udille'l-meyyit izâ dufin, gloss:ölü gömülünce "kaybettirildi" denir, source:"ض ل ل,B002"}. Düzenin akıbeti bu üç adımda yürür: hedefe kurulmuş bir emek yoldan çıkarılır, hedefini bulamaz, sonunda suya karışan süt gibi iz bırakmadan erir. Dördüncü ayetin fiil kökü yola çıkmayı ve niyet edilen yönü de taşır: {ar:رمى الرجل إذا سافر, tr:ramâ'r-racul izâ sâfer, gloss:adam yolculuğa çıkınca "attı" denir, source:"ر م ي,B007"}, {ar:أين ترمي أي جهة تنوي, tr:eyne termî, ey cihetin tenvî, gloss:"nereye atıyorsun", yani hangi yöne niyetlisin, source:"ر م ي,B007"}. Yolculuğun yönünü söyleyen kök, sûrede kuşların onları "atmasında" geri döner.

İkinci kılma ise insanların kendisini nesne alır: {ar:فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ, tr:fe-cealehum ke-asfin me'kûl, gloss:onları yenmiş ekin yaprağı gibi kıldı, source:105:5}. İlk kılma onların yaptığı şeyi, ikincisi onları kendilerini dönüştürür. Onların "keyd"i, yani bir şeye güçle uğraşmaları, sûrenin sonunda Onun yapışının nesnesi olarak kalır.

Kur'an bu ilişkiyi defalarca kurar. Mü'min sûresinde Firavun'un meclisi, Musa'ya inananların oğullarını öldürmeyi emreder ve ayet şu hükümle kapanır: {ar:وَمَا كَيْدُ ٱلْكَٰفِرِينَ إِلَّا فِى ضَلَٰلٍۢ, tr:ve mâ keydu'l-kâfirîne illâ fî dalâl, gloss:kâfirlerin düzeni boşa gitmekten başka bir şey değildir, source:40:25}; keyd ve dalâl bu sûredeki gibi tek cümlede durur. Aynı sûrede Firavun göğün yollarına çıkmak ister ve hüküm aynı kalıpla verilir: {ar:وَمَا كَيْدُ فِرْعَوْنَ إِلَّا فِى تَبَابٍۢ, tr:ve mâ keydu fir'avne illâ fî tebâb, gloss:Firavun'un düzeni yıkımdan başka bir şeye varmaz, source:40:37}. Yusuf sûresinde Yusuf, kendisine kurulan tuzağın ortaya çıkışından sonra şöyle der: {ar:وَأَنَّ ٱللَّهَ لَا يَهْدِى كَيْدَ ٱلْخَآئِنِينَ, tr:ve ennallâhe lâ yehdî keyde'l-hâ'inîn, gloss:Allah hainlerin düzenini hedefine ulaştırmaz, source:12:52}; burada keyd'in yolunu bulmaması, "doğru yola iletmek" fiiliyle söylenir, sûrenin tadlîl'inin tam karşılığıdır. Daha önce de Rab onu kurulan tuzaktan çevirmişti: {ar:فَٱسْتَجَابَ لَهُۥ رَبُّهُۥ فَصَرَفَ عَنْهُ كَيْدَهُنَّ, tr:festecâbe lehû rabbuhû fe-sarafe anhu keydehunn, gloss:Rabbi duasını kabul etti ve onların tuzağını ondan çevirdi, source:12:34}. İbrahim'i yakmak isteyen kavim için Kur'an keyd'e karşı bir "kılma" koyar: {ar:وَأَرَادُوا۟ بِهِۦ كَيْدًۭا فَجَعَلْنَٰهُمُ ٱلْأَخْسَرِينَ, tr:ve erâdû bihî keyden fe-cealnâhumu'l-ahserîn, gloss:ona bir tuzak kurmak istediler, biz de onları en çok kaybedenler kıldık, source:21:70}, ve Sâffât sûresinde {ar:فَأَرَادُوا۟ بِهِۦ كَيْدًۭا فَجَعَلْنَٰهُمُ ٱلْأَسْفَلِينَ, tr:fe-erâdû bihî keyden fe-cealnâhumu'l-esfelîn, gloss:ona tuzak kurmak istediler, biz de onları en alçaklar kıldık, source:37:98}. Enfâl sûresi bunu bir ilahi sıfata bağlar: {ar:وَأَنَّ ٱللَّهَ مُوهِنُ كَيْدِ ٱلْكَٰفِرِينَ, tr:ve ennallâhe mûhinu keydi'l-kâfirîn, gloss:Allah kâfirlerin düzenini zayıflatandır, source:8:18}. Tûr sûresi keyd kuranları keyd'in nesnesi yapar: {ar:أَمْ يُرِيدُونَ كَيْدًۭا ۖ فَٱلَّذِينَ كَفَرُوا۟ هُمُ ٱلْمَكِيدُونَ, tr:em yurîdûne keydâ, fellezîne keferû humu'l-mekîdûn, gloss:yoksa bir tuzak mı kurmak istiyorlar? Asıl tuzağa düşürülenler inkâr edenlerdir, source:52:42}; birkaç ayet sonra {ar:يَوْمَ لَا يُغْنِى عَنْهُمْ كَيْدُهُمْ شَيْـًۭٔا, tr:yevme lâ yugnî anhum keyduhum şey'â, gloss:tuzaklarının kendilerine hiçbir yarar sağlamayacağı gün, source:52:46} gelir. Târık sûresinde iki keyd yüz yüze konur: {ar:إِنَّهُمْ يَكِيدُونَ كَيْدًۭا, tr:innehum yekîdûne keydâ, gloss:onlar bir tuzak kuruyorlar, source:86:15}, {ar:وَأَكِيدُ كَيْدًۭا, tr:ve ekîdu keydâ, gloss:ben de bir düzen kuruyorum, source:86:16}; A'râf sûresinde Allah {ar:إِنَّ كَيْدِى مَتِينٌ, tr:inne keydî metîn, gloss:benim düzenim sağlamdır, source:7:183} der. Yapma fiilinin Allah'a ait olduğu da açıkça söylenir: {ar:فَعَّالٌۭ لِّمَا يُرِيدُ, tr:fe''âlun limâ yurîd, gloss:dilediğini yapandır, source:85:16}. İbrahim sûresi ise sapmayı ve rüzgârı bir benzetmede birleştirir: {ar:أَعْمَٰلُهُمْ كَرَمَادٍ ٱشْتَدَّتْ بِهِ ٱلرِّيحُ فِى يَوْمٍ عَاصِفٍۢ, tr:a'mâluhum ke-ramâdin işteddet bihi'r-rîhu fî yevmin âsıf, gloss:yaptıkları, fırtınalı bir günde rüzgârın savurduğu kül gibidir, source:14:18}, ve aynı ayet {ar:ذَٰلِكَ هُوَ ٱلضَّلَٰلُ ٱلْبَعِيدُ, tr:zâlike huve'd-dalâlu'l-baîd, gloss:işte uzak sapkınlık budur, source:14:18} diye biter. Secde sûresinde inkârcılar dalâl kökünü yerin içinde kaybolmak anlamında kullanır: {ar:أَءِذَا ضَلَلْنَا فِى ٱلْأَرْضِ, tr:e-izâ dalelnâ fi'l-ard, gloss:biz yerin içinde kaybolup gittiğimizde mi, source:32:10}.

Kaynaklar: 105:1 فَعَلَ ف ع ل B001; 105:2 يَجْعَلْ ج ع ل B002; 105:5 فَجَعَلَهُمْ ج ع ل B001; 105:5 فَجَعَلَهُمْ ج ع ل B002; 105:2 كَيْدَهُمْ ك ي د B001; 105:2 كَيْدَهُمْ ك ي د B002; 105:2 تَضْلِيلٍ ض ل ل B001; 105:2 تَضْلِيلٍ ض ل ل B003; 105:2 تَضْلِيلٍ ض ل ل B002; 105:4 تَرْمِيهِم ر م ي B007

## Hiç karşılaşılmayan savaş

Sûrenin üç kökü Arapçada savaşı da adlandırır ve üçü de savaşın gerçekleşmediği bir sahneyi kurar. {ar:كَيْدَهُمْ, tr:keydehum, gloss:onların düzeni, source:105:2} kökü kalıplaşmış bir ifadede savaşın kendisidir ve bu ifadenin örneği tam olarak karşılaşılmayan bir savaştır: {ar:الكيد الحرب يقال خرجوا ولم يلقوا كيدا أي حربا, tr:el-keydu'l-harb, yukâlu harecû ve lem yelkav keyden, ey harbâ, gloss:keyd savaştır; "çıktılar ve keyd ile karşılaşmadılar", yani savaş görmediler denir, source:"ك ي د,B004"}, {ar:ربما سمي الحرب كيدا يقال غزا فلان فلم يلق كيدا, tr:rubbemâ summiye'l-harbu keydâ, yukâlu gazâ fulânun fe-lem yelka keydâ, gloss:savaşa bazen keyd denir; "falan sefere çıktı ama keyd görmedi" denir, source:"ك ي د,B004"}. Sûrede filin sahiplerinin karşısına hiçbir insan çıkmaz: ayetlerde iş görenler yalnızca Rab, kuşlar ve taşlardır. Savaşa gelen bir topluluk savaşacak kimse bulamaz.

{ar:سِجِّيلٍ, tr:siccîl, gloss:siccîl, source:105:4} kökü, sırayla dökülen kova üzerinden savaşın dönüşümlü talihini anlatır: {ar:الحرب سجال أي مرة منها سجل على هؤلاء ومرة على هؤلاء, tr:el-harbu sicâl, ey merraten minhâ seclun alâ hâ'ulâ'i ve merraten alâ hâ'ulâ', gloss:savaş "sicâl"dir, yani bir kova bunların üzerine, bir kova ötekilerin üzerine, source:"س ج ل,B002"}; bu yarışmanın kökü su çekmeye dayanır: {ar:تساجل الرجلان إذا تفاخرا وأصله من تساجلهما في الاستقاء, tr:tesâcele'r-raculân izâ tefâharâ, ve asluhû min tesâculihimâ fi'l-istikâ', gloss:iki adam övünme yarışına girince "tesâcele" denir; aslı su çekmede kova yarıştırmalarıdır, source:"س ج ل,B002"}. Sûrede ise taşlar {ar:عَلَيْهِمْ, tr:aleyhim, gloss:üzerlerine, source:105:3} gönderilir; kova yalnızca bir tarafa dökülür ve sıra hiçbir zaman öbür tarafa geçmez. Son ayetin {ar:كَعَصْفٍ, tr:ke-asf, gloss:ekin yaprağı gibi, source:105:5} kökü ise bir kavmi silip götüren savaşı adlandırır: {ar:الحرب تعصف بالقوم أي تذهب بهم وتهلكهم وأعصف الرجل أي هلك, tr:el-harbu ta'sifu bi'l-kavm, ey tezhebu bihim ve tuhlikuhum, ve a'safe'r-racul, ey helek, gloss:savaş kavmi "asf" eder, yani alıp götürür ve helak eder; "a'safe'r-racul" adam helak oldu demektir, source:"ع ص ف,B004"}. Onları alıp götüren "savaş" insanlarca yapılmamıştır. Düzen kelimesinin kökü kalıplaşmış bir ifadede can vermeyi de anlatır: {ar:هو يكيد بنفسه أي يجود بها, tr:huve yekîdu bi-nefsih, ey yecûdu bihâ, gloss:"canıyla keyd ediyor", yani can çekişiyor, source:"ك ي د,B003"}. Kurdukları düzenin adı, sonlarının adıyla aynı köktedir.

Kur'an insan eli değmeden kesilen savaşı başka sahnelerde de anlatır. Ahzâb sûresinde Allah mü'minlere, üzerlerine ordular geldiği gün {ar:فَأَرْسَلْنَا عَلَيْهِمْ رِيحًۭا وَجُنُودًۭا لَّمْ تَرَوْهَا, tr:fe-erselnâ aleyhim rîhan ve cunûden lem teravhâ, gloss:üzerlerine bir rüzgâr ve görmediğiniz ordular gönderdik, source:33:9} der; aynı anlatı {ar:وَكَفَى ٱللَّهُ ٱلْمُؤْمِنِينَ ٱلْقِتَالَ, tr:ve kefallâhu'l-mu'minîne'l-kıtâl, gloss:Allah mü'minleri savaşmaktan kurtardı, source:33:25} diye kapanır; aynı ayet gelenlerin {ar:لَمْ يَنَالُوا۟ خَيْرًۭا, tr:lem yenâlû hayrâ, gloss:hiçbir hayra erişemediler, source:33:25} geri döndüğünü söyler. Fetih sûresinde Allah, Mekke'nin göbeğinde iki tarafın ellerini birbirinden çektiğini hatırlatır: {ar:وَهُوَ ٱلَّذِى كَفَّ أَيْدِيَهُمْ عَنكُمْ وَأَيْدِيَكُمْ عَنْهُم بِبَطْنِ مَكَّةَ, tr:ve huve'llezî keffe eydiyehum anküm ve eydiyeküm anhum bi-batni mekke, gloss:Mekke'nin göbeğinde onların ellerini sizden, sizin ellerinizi onlardan çeken Odur, source:48:24}. Enfâl sûresinde, iki topluluğun karşılaştığı gün hakkında, öldürme ve atma Allah'a verilir: {ar:فَلَمْ تَقْتُلُوهُمْ وَلَٰكِنَّ ٱللَّهَ قَتَلَهُمْ, tr:fe-lem taktulûhum ve lâkinnallâhe katelehum, gloss:onları siz öldürmediniz, Allah öldürdü, source:8:17}. Âl-i İmrân sûresinde ise bir yaralanmanın ardından mü'minlere savaşın dönüşümlü talihi hatırlatılır: {ar:وَتِلْكَ ٱلْأَيَّامُ نُدَاوِلُهَا بَيْنَ ٱلنَّاسِ, tr:ve tilke'l-eyyâmu nudâviluhâ beyne'n-nâs, gloss:o günleri insanlar arasında döndürür dururuz, source:3:140}. Fil sûresinde bu dönüşüm yoktur: tek bir kova, tek bir tarafa dökülür. Kamer sûresinde verilen söz de bunu anlatır: {ar:سَيُهْزَمُ ٱلْجَمْعُ وَيُوَلُّونَ ٱلدُّبُرَ, tr:seyuhzemu'l-cem'u ve yuvellûne'd-dubur, gloss:o topluluk bozguna uğrayacak ve arkalarını dönüp kaçacaklar, source:54:45}.

Kaynaklar: 105:2 كَيْدَهُمْ ك ي د B004; 105:2 كَيْدَهُمْ ك ي د B003; 105:4 سِجِّيلٍ س ج ل B002; 105:5 كَعَصْفٍ ع ص ف B004

## Yakıt ve yiyen ateş

{ar:مَّأْكُولٍۭ, tr:me'kûl, gloss:yenmiş, source:105:5} kelimesinin kökü ateşin yemesini de söyler: {ar:أكلت النار الحطب وآكلتها؛ ائتكلت النار إذا اشتد التهابها؛ وعلى طريق التشبيه قيل أكلت النار الحطب, tr:ekeleti'n-nâru'l-hatab ve âkeltuhâ; i'tekeleti'n-nâru izâ işteedde'ltihâbuhâ; ve alâ tarîki't-teşbîh kîle ekeleti'n-nâru'l-hatab, gloss:ateş odunu yedi; alevi şiddetlenince ateş "kendini yedi"; benzetme yoluyla "ateş odunu yedi" denir, source:"ء ك ل,B005"}. {ar:عَصْفٍ, tr:asf, gloss:kuru ekin yaprağı, source:105:5}, kuruyup ufalanan yapraktır, {ar:ما على ساق الزرع من الورق الذي يبس فتفتت, tr:mâ alâ sâkı'z-zer'i mine'l-varaki'llezî yebise fe-tefettet, gloss:ekinin sapı üzerinde kuruyup ufalanan yapraklar, source:"ع ص ف,B001"}, yani ateşin ilk tuttuğu yakıt. Kuşların sıfatının kökü bir odun demetini adlandırır ve bir atasözünde bir yükün üstüne bir başka yük olarak geçer: {ar:الإبالة الحزمة من الحطب, tr:el-ibâletu'l-huzmetu mine'l-hatab, gloss:"ibâle", odun demetidir, source:"ء ب ل,B005"}, {ar:الإبالة الحزمة من الحطب وضغث على إبالة, tr:el-ibâletu'l-huzmetu mine'l-hatab, ve dıgsun alâ ibâleh, gloss:ibâle odun demetidir; "demetin üstüne bir tutam", source:"ء ب ل,B005"}. Düzenin kökü de kalıplaşmış bir ifadede ateşi geç veren çakmak ağacını anlatır: {ar:أن يخرج الزند النار ببطء وشدة, tr:en yuhrice'z-zendu'n-nâre bi-but'in ve şidde, gloss:çakmak ağacının ateşi yavaşça ve zorla çıkarması, source:"ك ي د,B006"}, {ar:كاد الزند إذا تباطأ بإخراج ناره, tr:kâde'z-zend izâ tebâta'e bi-ihrâci nârih, gloss:çakmak ağacı ateşini geç çıkarınca "kâde" denir, source:"ك ي د,B006"}. Siccîl de taş ve çamurun karışımı olarak açıklanır: {ar:السجيل حجر وطين مختلط وأصله فيما قيل فارسي معرب, tr:es-siccîlu hacerun ve tînun muhtalit, ve asluhû fîmâ kîle fârisiyyun mu'arrab, gloss:siccîl, karışık taş ve çamurdur; aslının, denildiğine göre, Arapçalaşmış Farsça olduğu söylenir, source:"س ج ل,B005"}, {ar:السجيل حجارة كالمدر وهو حجر وطين, tr:es-siccîlu hicâratun ke'l-meder, ve huve hacerun ve tîn, gloss:siccîl, kuru kesek gibi taşlardır; taş ve çamurdur, source:"س ج ل,B005"}. Kur'an da Lut kavmine yağan siccîl taşlarını bir başka yerde {ar:حِجَارَةًۭ مِّن طِينٍۢ, tr:hicâraten min tîn, gloss:çamurdan taşlar, source:51:33} diye anar.

Bu aile imgeleri bir tersine dönüş kurar. Onların keyd'i, yani emekle uğraşmaları, ateşi geç veren bir çakmak gibidir: güçle vurulur ama tutuşmaz. Sonunda yenilen ise kendileridir, ateşin kuru samanı yiyişi gibi. Bu bir aile imgesidir; ayet ateşten söz etmez, yalnızca "yenmiş" der. Kur'an ise ateşin yemesini açıkça kullanır: Âl-i İmrân sûresinde bazıları peygambere inanmak için {ar:حَتَّىٰ يَأْتِيَنَا بِقُرْبَانٍۢ تَأْكُلُهُ ٱلنَّارُ, tr:hattâ ye'tiyenâ bi-kurbânin te'kuluhu'n-nâr, gloss:bize ateşin yiyeceği bir kurban getirinceye kadar, source:3:183} şartını koyduklarını söyler. Bakara sûresinde Kur'an'a denk bir sûre getirmeye çağrılan inkârcılara, iki kez tekrarlanan "yapmak" fiilinin ardından, taşların ateşin yakıtı olduğu söylenir: {ar:فَإِن لَّمْ تَفْعَلُوا۟ وَلَن تَفْعَلُوا۟ فَٱتَّقُوا۟ ٱلنَّارَ ٱلَّتِى وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:fe-in lem tef'alû ve len tef'alû fetteku'n-nâre'lletî vekûduhe'n-nâsu ve'l-hicâra, gloss:yapamazsanız, ki asla yapamayacaksınız, yakıtı insanlar ve taşlar olan ateşten sakının, source:2:24}; Tahrîm sûresinde mü'minlere aynı uyarı gelir: {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:kû enfuseküm ve ehlîküm nâran vekûduhe'n-nâsu ve'l-hicâra, gloss:kendinizi ve ailenizi yakıtı insanlar ve taşlar olan ateşten koruyun, source:66:6}. Bakara sûresindeki bir benzetme de rüzgârı ve ateşi bir bahçenin üzerinde birleştirir: {ar:فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ, tr:fe-esâbehâ i'sârun fîhi nârun fehterakat, gloss:içinde ateş bulunan bir kasırga ona çarptı ve bahçe yandı, source:2:266}. Kasırga kelimesi "asf" ile aynı kökten değildir; ama rüzgârın ve ateşin bir ekini yok edişi, bu sûrenin son ayetindeki iki aile imgesinin bir arada sahnelenişidir.

Kaynaklar: 105:5 مَّأْكُولٍۭ ء ك ل B005; 105:5 كَعَصْفٍ ع ص ف B001; 105:3 أَبَابِيلَ ء ب ل B005; 105:2 كَيْدَهُمْ ك ي د B006; 105:4 سِجِّيلٍ س ج ل B005

## Buluşmalar

Sûrenin hareketi, açılıştaki görme çağrısı ile sondaki kırılmış ekin arasında kurulur ve imgeler bu yolda birbirine geçer. Görmenin imgesi ile düzenin imgesi aynı kökte buluşur: yolunu kaybetmeyi anlatan kök, bir işte doğruyu bulamamayı da anlatır. İkinci ayetteki düzen, hem bir yolda saptırılan bir yürüyüş hem de sağlıklı görmeyen bir aklın yanılmasıdır; okura "gör" denirken karşı tarafın düzeni "yolunu bulamaz". Fecr sûresinin "hicr sahibi" ile "Rabbinin ne yaptığını görmedin mi" sorusunu yan yana koyması, bu karşılaşmanın sahnesidir: akıl anlamındaki "hicr" ile taşın kökü aynıdır ve aklı olmayanlara taş iner.

Salınan sürüler, av ve fırtına tek bir sahnede durur. Göndermenin kökü hem otlağa salınan sürüleri hem gönderilen rüzgârları hem kısa bir oku adlandırır; üçüncü ayetin tek fiili, kuşların bölük bölük gelişini, rüzgârın esişini ve okun atılışını birlikte taşır. Atmanın kökü de iki yüzlüdür: ok ve taşla ava atmak ve iri damlalı bulutun yağması. Dördüncü ayetteki kuşlar, bir avcı gibi atar ve bir bulut gibi yağdırır. Mürselât sûresinin "gönderilenler" ile "şiddetle esenler"i ardışık koyması, göndermenin fırtınaya dönüşümünü sahneler; bu sûrede de gönderilen kuşlarla başlayan iş "asf" kelimesiyle biter.

Fırtına ile yazılmış taşlar siccîl kelimesinde buluşur. Kelime hem "salıverdiğim" hem "onlar için yazılmış olan" diye açıklanır: taşlar hem bir buluttan boşalan kovanın dökülüşü gibi iner hem de kimin için olduklarını taşır. Hûd ve Zâriyât sûrelerinin taş yağmuru, bu iki yüzü bir arada gösterir: yağdırılan siccîl taşları "Rabbinin katında işaretlenmiş"tir.

Savaş ile fırtına da siccîl'in kökünde birleşir: savaşın dönüşümlü talihi, su çekerken sırayla dökülen kovadan gelir. Fil sûresinde kova yalnızca bir tarafa, onların üzerine dökülür; fırtınanın boşalan kovası, savaşın sıra beklemeyen kovasıdır. Savaş ile ekin de "asf"ın kökünde buluşur: savaş bir kavmi silip götürür, rüzgâr şeyi kırıp asf gibi yapar ve rüzgârın insanları silip götürmesi bu kırılmaya benzetilerek söylenir.

Av ile ekin "yenmiş" kelimesinde iki ayrı sona ayrılır: yırtıcının yediği av ve ürünü alınıp içi yenmiş ekin. Ekin ile ateş de kuru yaprakta buluşur: kuruyup ufalanan yaprak, ateşin ilk yediği şeydir. Ağır ile hafifin yer değiştirmesi bu sahnelerin hepsinden geçer: en iri hayvan, en hafif kanatlıların avıdır ve sonunda en hafif şeye, ağırlığı olmayan bir yaprağa döner.

Bütün bu imgeleri birinci ve beşinci ayetler arasındaki fiiller bağlar. Rabbin "yapışı", kullanımdaki örneğiyle bir kırmadır; ilk "kılma" onların düzenini sapmaya, ikinci "kılma" onların kendilerini kırılmış ekine çevirir. Zümer sûresi bu yayı tek bir ayette gösterir: "görmedin mi" ile açılır, bir ekin çıkarır, sararmasını gösterir ve "onu kırıntı kılar". Fil sûresi aynı yayı bir topluluğun üzerine kurar: okur görmeye çağrılır, onların emeği yoldan çıkarılır, gökten bölük bölük salınan avcılar yazılmış taşlarını yağdırır ve sonunda geriye, ürünü yenmiş bir ekinin rüzgârla kırılmış yaprağı kalır.

