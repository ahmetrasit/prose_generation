Focus: 87:7. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/87_7/D.r13/context.md =====
# 87:7 — focus

إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ

Anchor translation (canonical reading, reference only):

Ancak Allah'ın dilediği dışında. Kuşkusuz O, açık olanı ve gizli kalanı bilir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | إِلَّا | إِلَّا |  | EXP |
| 2 | مَا | مَا |  | REL |
| 3 | شَآءَ | شَآءَ | ش ي ء | V |
| 4 | ٱللَّهُ | ٱللَّه | ء ل ه | PN |
| 5 | إِنَّهُۥ | إِنّ |  | ACC;PRON |
| 6 | يَعْلَمُ | عَلِمَ | ع ل م | V |
| 7 | ٱلْجَهْرَ | جَهْر | ج ه ر | DET;N |
| 8 | وَمَا | مَا |  | CONJ;REL |
| 9 | يَخْفَىٰ | يَخْفَىٰ | خ ف ي | V |


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
- 87:7 ◀ focus إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ
- 87:8 وَنُيَسِّرُكَ لِلْيُسْرَىٰ
- 87:9 فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ
- 87:10 سَيَذَّكَّرُ مَن يَخْشَىٰ
- 87:11 وَيَتَجَنَّبُهَا ٱلْأَشْقَى
- 87:12 ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ
- 87:13 ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- 87:14 قَدْ أَفْلَحَ مَن تَزَكَّىٰ
- 87:15 وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ
- 87:16 بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- 87:17 وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- 87:18 إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ
- 87:19 صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ


===== _commentary/v16/work/87_7/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ش ي ء (root_000831) — identity root of شَآءَ (w3)

- **B001** varlık, olgu ya da konu — şey; varlık, olgu ya da konu · şeyler; varlıklar, olgular ya da konular · hiçbir şey yok; istenen bir şey yok
  الشيء واحد الأشياء (ayn); الشئ والجمع أشياء (sihah); أشياء جمع شيء (tahdhib); الذي يصح أن يعلم ويخبر عنه (mufradat)
- **B002** isteme ve gerçekleşmesini dileme — isteme; bir şeyin olmasını dileme · istedi, olmasını diledi · Tanrı'nın istemesiyle · Tanrı isterse
  المشيئة مصدر شاء يشاء (ayn); المشيئة الإرادة وقد شئت الشئ أشاؤه (sihah); الشيئة مصدر شاء يشاء مشيئة (tahdhib); المشيئة عند أكثر المتكلمين كالإرادة وفي الأصل إيجاد الشيء وإصابته (mufradat)
- **B003** bir işe ya da hedefe sevk etmek — adamı o işe yöneltti · onu zorlayıp getirdi · seni oraya getirir
  شيأت الرجل على الامر حملته عليه; وأشاءه لغة في أجاءه أي ألجأه; يشيئك إلى مخة عرقوب بمعنى يجيئك
- **B004** yaradılışı bozuk ve çirkin — Tanrı yüzünü çirkinleştirsin diye beddua etti · yaradılışı bozuk, görünüşü çirkin
  شيأ الله وجهه إذا دعا عليه بالقبح (maqayis); رجل مشيأ الخلق قبيح المنظر (jamhara); المشيأ المختلف الخلق القبيح وقد شيأ الله خلقه أي قبحه (tahdhib)
- **B005** özlem duymak; beğenip sevinmek [kalıp] — bu bende özlem uyandırdı · onu beğendim ve sevindim
  شاءني الشيء مثل شاعني إذا شاقني (jamhara); شؤت به أعجبت به وسررت (tahdhib)
- **B006** dikkat vererek dinlemek — kulak verip dinledim
  اشتأيت أي استمعت
- **B007** uzağı görebilen at — uzağı görebilen; at için
  الشيئان بوزن الشيعان البعيد النظر وينعت به الفرس
- **B008** genç hurma fidanları — genç hurma fidanları · tek bir genç hurma fidanı
  الإشاء الصغار من النخل واحدها أشاءة
- **B009** yakınma ve şaşma ünlemi — Eyvah, ne haldeyim! · Vay, ne güzel!
  ياشيء مالي معناه الأسف والتلهف والحزن; يتعجب بشيء وهيء وفيء ويقول يا شيما أي ما أحسن هذا

## ش ي ء (root_000832) — identity root of شَآءَ (w3)

- **B001** isteme ve dileme — isteme; olmasını dileme · isteme, dileme · istedi, olmasını diledi
  للشيئة مصدر شاء يشاء مشيئة (tahdhib)
- **B002** yüzü veya yaradılışı bozuk ve çirkin — Tanrı yüzünü çirkinleştirsin diye beddua etti · yüzü veya yaradılışı bozuk ve çirkin
  شَيَّأ الله وجهه إذا دعا عليه بالقبح؛ وجه مشيأ (maqayis); المشيأ المختلف الخلق، القبيح، وقد شَيَّأ الله خلقه أي قبحه؛ المشيأ مثل المؤبن (tahdhib)
- **B003** uzağı görebilen at — uzağı görebilen; at için
  الشيئان بوزن الشيعان: البعيد النظر، وينعت به الفرس (tahdhib)
- **B004** beğenip sevinmek [kalıp] — onu beğendim ve sevindim
  شؤت به: أعجبت به وسررت (tahdhib)
- **B005** dikkat vererek dinlemek — kulak verip dinledim
  اشتأيت أي استمعت (tahdhib)
- **B006** genç hurma fidanları — genç hurma fidanları · tek bir genç hurma fidanı
  الإشاء الصغار من النخل، واحدها أشاءة (tahdhib)
- **B007** yakınma ve şaşma ünlemleri — Eyvah, ne haldeyim! · Eyvah, ne haldeyim! · Vay!; şaşma ünlemi · Vay, ne güzel!
  يافيء مالي، وياشيء مالي، وياهيء مالي، معناه كله الأسف والتلهف والحزن؛ يا شيء مالي ويا شي مالي يهمز ولا يهمز؛ من يتعجب بشيء وهيء وفيء؛ يا شيما أي ما أحسن هذا (tahdhib)

## ء ل ه (root_000047) — identity root of ٱللَّهُ (w4)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## ع ل م (root_001040) — identity root of يَعْلَمُ (w6)

- **B001** bilme ve gerçeğini kavrama — bilgi; bir şeyi gerçeğiyle kavrama · bir şeyi bilmek ve tanımak · haberinden haberdar olmak · bildirmek, haberdar etmek · öğretmek, öğrenmesini sağlamak · öğrenmek, kavramaya yönelmek · bilmek; buyrukta bil ki · bilgi yarışında yenmek · bilen ve bildiğine göre davranan kişi · bilgili, bilgi sahibi · çok bilgili, çok bilen · son derece bilgili kişi
  العلم نقيض الجهل (maqayis;ayn;tahdhib)؛ علمت الشيء عرفته (sihah;tahdhib)؛ إدراك الشيء بحقيقته (mufradat)؛ ما علمت بخبرك أي ما شعرت به (ayn;tahdhib)؛ أعلمته بكذا وعلمته تعليما (ayn)؛ التعليم تنبيه النفس لتصور المعاني (mufradat)؛ تعلم بمعنى اعلم (maqayis;sihah;tahdhib)؛ عالمت الرجل فعلمته (sihah;tahdhib)
- **B002** ayırt edici ve yol gösterici işaret — ayırt edici işaret · bayrak, sancak · yol gösteren belirgin dağ · kumaşın kenar işareti veya deseni · yol gösteren iz veya belirti · savaşta kendine ayırt edici işaret takmak · kumaşı işaretlemek · işaret olarak kullanılan kına · sarığı tanıtıcı bir biçimde sarmak · tanınmış ve öne çıkan kişi · son saatin yaklaştığını gösteren belirti
  أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره (maqayis)؛ العلامة وهي معروفة (maqayis)؛ العلم الراية والجمع أعلام (maqayis;sihah;tahdhib)؛ العلم الجبل الطويل والجميع الأعلام (ayn)؛ العلم الجبل (sihah;mufradat)؛ المعلم الأثر يستدل به على الطريق (sihah;tahdhib)؛ علم الثوب ورقمه في أطرافه (sihah;tahdhib;mufradat)؛ أعلم الفارس إذا كانت له علامة في الحرب (maqayis;sihah;tahdhib)؛ العلام الحناء (maqayis;sihah;tahdhib;mufradat)؛ علمت عمتي أعلمها علما (tahdhib)
- **B003** evren ve bütün yaratılmışlar — evren veya yaratılmışlar bütünü · bütün yaratıklar veya varlık sınıfları · evrenler, varlık dünyaları
  العالمون كل جنس من الخلق فهو في نفسه معلم وعلم (maqayis)؛ العالم الخلق والجمع العوالم (sihah)؛ العالمين رب الجن والإنس ورب الخلق كلهم (tahdhib)؛ العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به (mufradat)؛ أصناف الخلائق (mufradat)
- **B004** üst dudak yarığı — üst dudaktaki yarık · üst dudağı yarık kişi veya deve · üst dudağını yarmak
  العلم الشق في الشفة العليا والرجل أعلم (maqayis)؛ الأعلم الذي انشقت شفته العليا (ayn)؛ علم الرجل يعلم علما إذا صار أعلم وهو المشقوق الشفة العليا (sihah)؛ علمت الرجل أعلمه علما إذا شققت شفته العليا (tahdhib)؛ البعير يقال له أعلم لعلم في مشفره الأعلى (tahdhib)؛ الشق في الشفة العليا علم (mufradat)
- **B005** deniz ya da suyu bol kuyu — deniz · suyu bol kuyu
  العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء (maqayis)؛ العيلم الركية الكثيرة الماء (sihah)؛ العيلم البئر الكثيرة الماء (tahdhib)
- **B006** doğan veya atmaca türü yırtıcı kuş — doğan veya atmaca · çevik ve zeki adam
  العلام الصقر؛ العلامي الرجل الخفيف الذكي مأخوذ من العلام؛ العلام الباشق (tahdhib)
- **B007** erkek sırtlan — erkek sırtlan
  العيلام الذكر من الضباع (sihah)؛ العيلام الضبعان وهو ذكر الضباع (tahdhib)

## ج ه ر (root_000269) — identity root of ٱلْجَهْرَ (w7)

- **B001** açıkça duyurma ve yüksek sesle söyleme — açıkça duyurma ve açığa vurma · sözü yüksek sesle söylemek · okumayı yüksek sesle yapmak · işi açıkça yapmak ve saklamamak · yüksek ya da gür sesli · alışkanlıkla yüksek sesle konuşan
  جهرت بالكلام أعلنت به؛ رجل جهير الصوت أي عاليه (maqayis)؛ جهر بكلامه وصلاته وقراءته؛ كلام جهير وصوت جهير أي عال (ayn)؛ الجهر ضد السر؛ رجل جهير الصوت إذا كان غليظه (jamhara)؛ جهر بالقول رفع به صوته؛ إجهار الكلام إعلانه؛ المجاهرة بالعداوة المبادأة بها (sihah)؛ ظهور الشيء بإفراط حاسة السمع؛ ولا تجهر بصلاتك؛ كلام جوهري وجهير ورجل جهير يقال لرفيع الصوت (mufradat)
- **B002** gözle açıkça görme ve görünür olma — örtüsüz ve göz önünde · göze göründü ve belirdi · onu göz önünde açıkça görmek
  إعلان الشيء وكشفه (maqayis)؛ اجتهر القوم فلانا أي نظروا إليه عيانا جهارا؛ كل شيء بدا فقد جهر (ayn)؛ رأيته جهرة؛ عيانا يكشف ما بيننا وبينه (sihah)؛ ظهور الشيء بإفراط حاسة البصر؛ رأيته جهارا؛ نرى الله جهرة؛ أرنا الله جهرة (mufradat)
- **B003** göze büyük ve gösterişli görünme — görenin gözünde büyük görünmek · güzelliği ve görünüşüyle beni hayran bıraktı · gösterişli ve güzel görünüşlü · orduyu gözümde çok ve büyük gördüm
  جهرت الشيء إذا كان في عينك عظيما؛ وجهرت الرجل؛ رأيت جهر فلان أي هيئته؛ جهير بين الجهارة إذا كان ذا منظر (maqayis)؛ رجل جهير إذا كان في الجسم والمنظر مجتهرا (ayn)؛ جهرني الرجل إذا راعك جماله وهيئته؛ رجل جهير ذو رواء؛ أجهرت الجيش واجتهرته معناه كثروا في عيني (jamhara)؛ جهرت الرجل واجتهرته إذا رأيته عظيم المرآة؛ رجل جهير بين الجهارة أي ذو منظر؛ ما أحسن جهره أي ما يجتهر من هيئته وحسن منظره (sihah)؛ من رآه جهره معنى جهره عظم في عينيه؛ جهرت الجيش واجتهرتهم إذا كثروا في عينك (tahdhib)؛ رجل جهير يقال لمن يجهر لحسنه (mufradat)
- **B004** güneşte görememe; kimi kullanımda şaşılık — güneşte göremeyen; başka aktarımda şaşı · güneş gözünü kamaştırdı
  العين الجهراء التي لا تبصر في الشمس (maqayis)؛ جهرته الشمس إذا أسدرت بصره؛ كبش أجهر إذا سدر في الشمس (jamhara)؛ الأجهر الذي لا يبصر في الشمس؛ كبش أجهر بين الجهر ونعجة جهراء (sihah)؛ كبش أجهر ونعجة جهراء وهي التي لا تبصر في الشمس؛ الجهرة الحولة ورجل أجهر وامرأة جهراء في عيونهما حول (tahdhib)
- **B005** sabahleyin gafil avlayarak varma — onlara sabahleyin gafilken vardık · sabah vakti
  جهرنا بني فلان أي صبحناهم على غرة؛ أتيناهم صباحا والصباح جهر (maqayis)؛ جهرنا بني فلان أي صبحناهم على غرة (sihah)
- **B006** insan topluluğu — insan topluluğu
  يقال للجماعة الجهراء (maqayis)؛ كيف جهراؤكم أي عند جماعتكم (sihah)
- **B007** geniş ve yayvan tepe — geniş ve yayvan tepe
  يقال إن الجهراء الرابية العريضة (maqayis)
- **B008** kuyuyu boşaltıp temizleyerek suyunu açığa çıkarma [kalıp] — kuyuyu boşaltıp çamurunu temizleyerek suyunu açığa çıkarmak · kuyuyu temizleyip suyunu görünür hale getirmek · temizlenmiş ve suyu açığa çıkarılmış kuyu
  جهرت البئر إذا نزفت ماءها (jamhara)؛ جهرت البئر واجتهرتها أي نقيتها وأخرجت ما فيها من الحمأة؛ جهرت الركية إذا كان ماؤها قد غطى الطين فنقى ذلك حتى يظهر الماء ويصفو (sihah)؛ جهرت البئر واجتهرتها إذا نزحتها؛ نزفوا مياه الآبار (tahdhib)؛ جهر البئر واجتهرها إذا أظهر ماءها (mufradat)
- **B009** bilinmeyen araziyi katetme [kalıp] — araziyi yolunu bilmeden geçtik
  جهرنا الأرض سلكناها من غير معرفة (sihah)
- **B010** tulumu çalkalama; süt için yağı alınmış ya da sulandırılmamış olma [kalıp] — süt tulumunu çalkalamak · yağı alınmış ya da su katılmamış süt
  جهرت السقاء مخضته؛ لبن جهير لم يمذق بماء (sihah)؛ جهرت السقاء إذا مخضته؛ الجهير اللبن الذي أخرج زبده (tahdhib)
- **B011** nefesi tutup ses akışıyla çıkarılan harf [kalıp] — nefesi tutup ses akışıyla çıkarılan harf
  الحروف المجهورة عند النحويين تسعة عشر؛ سمي الحرف مجهورا لأنه أشبع الاعتماد في موضعه ومنع النفس أن يجري معه حتى ينقضي الاعتماد بجرى الصوت (sihah)

## خ ف ي (root_000428) — identity root of يَخْفَىٰ (w9)

- **B001** gizli kalma ya da gizleme — şey gizli kaldı, görünmedi · şeyi ve onun haberini sakladı · şeyi gizledi ve sakladı · gizlilik ve saklılık hâli · gizlilik, görünmezlik · gizlenip gözden uzaklaştı · bir aktarıma göre gizlendi · gizlenen kişi · onunla gizlice buluştum
  خفي الشيء يخفى وأخفيته وهو في خفية وخفاء إذا سترته (maqayis); أخفيت الصوت إخفاء وفعله اللازم اختفى والخافية ضد العلانية ولقيته خفيا أي سرا (ayn); خفيت الشئ أخفيه كتمته وأخفيت الشئ سترته وكتمته واستخفيت منك أي تواريت (sihah); خفي الشيء خفية استتر وأخفيته أوليته خفاء وذلك إذا سترته ويقابل به الإبداء والإعلان (mufradat)
- **B002** örten ya da gizli kalan şey — gizli ya da örtülü şey · örtü veya örten giysi · kanadın iç tüyleri; hurma göbeğine yakın yapraklar · görünmeyen varlık · kanadın iç tüylerinden biri · bedende gizlendiğine inanılan görünmeyen varlık · kuyu, koruluk veya gizli yer · bu adla anılan iki aslan yatağı · su tulumunun üzerine atılan örtüler · kadının sesi ile yerdeki ayak izi
  الخوافي سعفات يلين قلب النخلة والخافي الجن (maqayis); الخفا مقصور الشيء الخافي والموضع الخافي والخفاء رداء تلبسه المرأة وكل شيء غطيت به شيئا فهو خفاء والخفية غيضة والخفية بئر والخوافي من الجناحين (ayn); الخافي الجن والخافية ما يخفى في البدن من الجن والخفية الركية والخوافى ما دون الريشات العشر والخوافي من السعف (sihah); الخفاء ما يستر به كالغطاء والخوافي جمع خافية وهي ما دون القوادم من الريش (mufradat)
- **B003** gizliliği giderip açığa çıkarma — gizli olan açığa çıktı, sır belli oldu · şeyi açığa çıkardı · şeyin gizliliğini giderip onu gösterdi · yağmur fareleri yuvalarından çıkardı · gizli şeyi çıkarıp ortaya koydu · kefenleri çıkardığı için mezar soyguncusu
  الأصل الآخر الإظهار وخفيت الشيء بغير ألف إذا أظهرته وخفا المطر الفأر من حجرتهن أخرجهن (maqayis); الخفا إخراجك الشيء الخفي وإظهاركه وخفيت الخرزة من تحت التراب أخفيها خفيا (ayn); وخفيته أيضا أظهرته وهو من الأضداد وخفى المطر الفأر إذا أخرجهن واستخفيت الشئ أي استخرجته وأخفيها أي أزيل عنها خفاءها (sihah); وخفيته أزلت خفاه وذلك إذا أظهرته (mufradat)
- **B004** belli belirsiz şimşek çakması — şimşek belli belirsiz ve zayıfça çaktı
  خفا البرق خفوا إذا لمع ويكون ذلك في أدنى ضعف (maqayis); وخفا البرق يخفو خفوا ويخفى خفيا أي ظهر من الغيم (ayn); خفا البرق يخفو خفوا وخفوا إذا لمع لمعانا خفيا (jamhara); وخفا البرق يخفو خفوا ويخفى خفيا إذا لمع لمعا ضعيفا معترضا في نواحى الغيم (sihah)

## و ل ه (root_005296) — documented alternative for ٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 87:7, and ## Buluşmalar) =====
## Gökten otlağa: bulut, ilk yağmur ve kararan ot

Surenin ilk beş ayeti bir bitkinin bütün ömrünü kısa tutarak anlatır. Dördüncü ayet {ar:وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ, tr:velleẕî ahrace'l-mer'â, gloss:otlağı çıkaran O'dur, source:87:4} der, beşinci ayet ise {ar:فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ, tr:fe-ce'alehû ğuŝâen ahvâ, gloss:sonra onu kapkara bir sel döküntüsüne çevirdi, source:87:5} diye biter. İki ayet arasında otu topraktan çıkaran şeyin, yani yağmurun adı geçmez. Bu eksik halkayı surenin başka kelimelerinin aileleri tamamlar. Burada ve sonraki bölümlerde, bir kelimenin kök ailesinden gelen görüntü kelimenin kendi ayetindeki anlamının yanında duyulur, hiçbir zaman onun yerine geçmez. Birinci ayetteki "ad" yine addır, "Rab" yine Rab'dir. Aile görüntüsü, bu anlamın arkasında Arapçayı bilen kulağa ayrıca ulaşan sahnedir.

Birinci ayet {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:yüce Rabbinin adını tesbih et, source:87:1} der. "Ad" anlamındaki اسم kelimesi س م و kökündendir ve bu kök gökyüzünü de verir. Araplar için {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tusemmi's-sehâbe semâen ve'l-matara semâen, gloss:Araplar buluta da yağmura da semâ der, source:"س م و,B004"}, ve aynı ad yağmurun bitirdiği ota da verilir: {ar:يسموا النبات سماء, tr:yusemmû'n-nebâte semâen, gloss:bitkiye de semâ derler, source:"س م و,B004"}. Ölçüt basittir: {ar:السماء كل ما علاك فأظلك, tr:es-semâu kullu mâ alâke fe-ezalleke, gloss:semâ senin üstüne çıkıp sana gölge salan her şeydir, source:"س م و,B004"}. Tek bir kök böylece başın üstündeki örtüden buluta, buluttan yağmura, yağmurdan topraktan çıkan ota kadar uzanan bütün dikey sütunu kapsar. "Rab" kelimesinin ailesi bu sütunun içinde belirli bir bulutu gösterir: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb sumiye bi-ẕâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi besleyip büyüttüğü için bu adı almıştır, source:"ر ب ب,B008"}. Bu, ötekilerin altında sarkan alçak buluttur: {ar:السحاب المتعلق دون السحاب, tr:es-sehâbu'l-muteallaku dûne's-sehâb, gloss:bulutların altında asılı duran bulut, source:"ر ب ب,B008"}. Aynı kök bulutun bir yerde durup gitmemesini de söyler: {ar:أربت السحابة: دامت, tr:erabbeti's-sehâbe dâmet, gloss:bulut durdu ve sürdü, source:"ر ب ب,B007"}. Aynı kalıp güney rüzgârı için de kullanılır: {ar:أربت الجنوب والسحابة أي دامت, tr:erabbeti'l-cenûbu ve's-sehâbe ey dâmet, gloss:güney rüzgârı da bulut da sürdü, source:"ر ب ب,B007"}. Bulutu süren bu rüzgârın adı olan cenûb, on birinci ayetteki يَتَجَنَّبُهَا kelimesiyle aynı köktendir: {ar:الجنوب ريح تجيء عن يمين القبلة, tr:el-cenûbu rîhun tecîu an yemîni'l-kıble, gloss:cenûb kıblenin sağ yanından gelen rüzgârdır, source:"ج ن ب,B006"}.

Bulut ilk belirdiğinde Arapça ona dördüncü ayetin fiilinden bir ad verir: {ar:الخروج السحاب أول ما يبدأ, tr:el-hurûc es-sehâbu evvele mâ yebdeu, gloss:hurûc bulutun ilk belirişidir, source:"خ ر ج,B005"}. Bulutun kenarlarında zayıf bir şimşek çakar. Bunu anlatan fiil, yedinci ayetteki يَخْفَىٰ ile aynı köktendir: {ar:خفا البرق يخفو خفوا ويخفى خفيا إذا لمع لمعا ضعيفا معترضا في نواحى الغيم, tr:hafe'l-berku yahfû hufuvven ve yahfî hafyen iẕâ leme'a lem'an daîfen mu'teridan fî nevâhi'l-ğaym, gloss:şimşek bulutun kenarlarında yan yan zayıfça parladığında hafâ denir, source:"خ ف ي,B004"}. Bu ışığı bütün gece gözleyen kişiyi ise on yedinci ayetteki أَبْقَىٰٓ kelimesinin kökü anlatır: {ar:بات فلان يبقي البرق أي ينظر إليه من أين يلمع, tr:bâte fulânun yubkı'l-berka ey yenzuru ileyhi min eyne yelma', gloss:falanca şimşeğin nereden çakacağına bakarak geceyi geçirdi, source:"ب ق ي,B005"}. Sonunda yağmur gelir ve adını verdiği hayattan alır: {ar:يسمى المطر حيا لأن به حياة الأرض, tr:yusemme'l-mataru hayâen li-enne bihî hayâte'l-ard, gloss:yağmura hayâ denir çünkü yerin hayatı onunladır, source:"ح ي ي,B002"}. On üçüncü ayetteki يَحْيَىٰ fiili ve on altıncı ayetteki ٱلْحَيَوٰةَ kelimesi bu köktendir. Yağmur yuvalarındaki fareleri de dışarı sürer. Bu sürüş yine "gizli" kökünden bir fiille söylenir, açıklaması da dördüncü ayetin fiiliyle yapılır: {ar:وخفا المطر الفأر من حجرتهن أخرجهن, tr:ve hafe'l-mataru'l-fe'ra min hucurâtihinne ahracehunne, gloss:yağmur fareleri deliklerinden çıkardı, source:"خ ف ي,B003"}.

اسم kelimesi için Arapçada kayıtlı ikinci bir türetme vardır. Bu türetme kelimeyi "damga" anlamındaki وسم köküne bağlar. Bu, kök kimliği değil, kayıtlı bir alternatiftir. Ama bu yoldan da aynı sahneye varılır, çünkü yılın ilk yağmurunun adı bu köktendir: {ar:سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة, tr:sumiye'l-vesmiyyu mine'l-matari vesmiyyen li-ennehû yesimu'l-arda bi'n-nebâti fe-yasîru fîhâ eseran fî evveli's-sene, gloss:ilk yağmura vesmî denir çünkü yeri bitkiyle damgalar ve yılın başında yerde bir iz olur, source:"و س م,B003"}. Yağmur toprağa yeşil bir iz basar.

Dördüncü ayetin fiili أخرج, somut bir şeyin bulunduğu yerden dışarı alınmasıdır: {ar:الإخراج أكثر ما يقال في الأعيان, tr:el-ihrâcu ekŝeru mâ yukâlu fi'l-a'yân, gloss:ihrâc çoğunlukla somut şeyler için söylenir, source:"خ ر ج,B002"}. Ot gerçekten topraktan çekilip çıkarılan bir şeydir. Aynı kökün ailesi ilk çıkışın görünüşünü de verir: {ar:أرض مخرجة نبتها في مكان دون مكان, tr:ardun muhrecetun nebtuhâ fî mekânin dûne mekân, gloss:otu bir yerde bitip başka yerde bitmeyen toprak, source:"خ ر ج,B007"}. İlk yeşil, toprağa yama yama düşer. Aynı ailede bir renk adı da vardır: {ar:الأخرج لون سواده أكثر من بياضه, tr:el-ahrecu levnun sevâduhû ekŝeru min beyâdih, gloss:karası akından çok olan renk, source:"خ ر ج,B007"}. المرعى ise tek kelimede otu, otlağın yerini ve otlamanın kendisini birlikte taşır: {ar:المرعى الرعي والموضع والمصدر, tr:el-mer'â er-ra'yu ve'l-mevdiu ve'l-masdar, gloss:mer'â hem ot hem yer hem otlamadır, source:"ر ع ي,B001"}.

Beşinci ayetteki جعل, bir şeyi bir halden başka bir hale çevirmektir: {ar:جعل صير, tr:ce'ale sayyera, gloss:ce'ale bir şeyi başka bir hale soktu demektir, source:"ج ع ل,B002"}. Otun çevrildiği şey olan غثاء, otun sonunu üç adımda anlatır: ot kurur, tadını yitirir, sel onu yığıp götürür. {ar:غثا السيل المرتع إذا جمع بعضه إلى بعض وأذهب حلاوته, tr:ğaŝe's-seylu'l-merte'a iẕâ ceme'a ba'dahû ilâ ba'din ve eẕhebe halâvetehû, gloss:sel otlağı üst üste yığıp tadını giderdiğinde ğaŝâ denir, source:"غ ث و,B002"}. Ot bu noktada {ar:يابسا بعد خضرته, tr:yâbisen ba'de hudratihî, gloss:yeşilliğinden sonra kurumuş olarak, source:"غ ث و,B002"} kalır. غثاء de {ar:الغثاء ما جاء به السيل من نبات قد يبس, tr:el-ğuŝâu mâ câe bihi's-seylu min nebâtin kad yebise, gloss:ğuŝâ selin getirdiği kurumuş bitkidir, source:"غ ث و,B001"}. Ardından gelen أحوى bir renktir: {ar:الأحوى الأسود من الخضرة, tr:el-ahvâ el-esvedu mine'l-hudra, gloss:ahvâ yeşilden kararmış olandır, source:"ح و ي,B006"}. Bir deve için de {ar:بعير أحوى إذا خالط خضرته سواد وصفرة, tr:baîrun ahvâ iẕâ hâlata hudratehû sevâdun ve sufra, gloss:yeşiline kara ve sarı karışmış deveye ahvâ denir, source:"ح و ي,B006"}. Rengin adı {ar:حُوَّة, tr:huvve, gloss:yeşile çalan koyu renk, source:"memory"} kelimesidir. Ayette kelime غثاء'nın sıfatı olarak durur. Ama tanımı hem gür yeşilin koyuluğunu hem de çürüyen otun kararmasını kapsar. Bu yüzden tek kelime otun iki ucunu, taze koyuluğu ve kapkara döküntüyü yan yana tutar. Kur'an gür yeşilin koyuluğunu başka bir yerde tek kelimeyle, cennet bahçeleri için verir: {ar:مُدْهَآمَّتَانِ, tr:müdhâmmetân, gloss:yeşillikten koyu kara görünen iki bahçe, source:55:64}.

Bu sahne surenin geri kalanında karşılık bulur. On üçüncü ayetteki "yaşamak" fiilinin ailesi diri otu {ar:الحي من النبات ما كان طريا يهتز, tr:el-hayyu mine'n-nebâti mâ kâne tariyyen yehtezzu, gloss:bitkinin dirisi taze olup titreşenidir, source:"ح ي ي,B002"} diye tanımlar. "Ölmek" fiilinin ailesi de {ar:الموتان الأرض لم تحي بعد بزرع ولا إصلاح, tr:el-mevtân el-ardu lem tuhye ba'du bi-zer'in ve lâ islâh, gloss:mevtân ekinle ya da bakımla henüz diriltilmemiş topraktır, source:"م و ت,B003"}. Otun yolculuğu böylece ölü topraktan titreşen yeşile, oradan kuru döküntüye uzanır. On üçüncü ayetin ateşteki adam için söylediği şey ise bu uçlardan hiçbirinde olmamaktır. "Rab" kelimesinin ailesinde bu yolculuğun karşısında duran bir bitki adı da vardır: {ar:اسم لعدة من النبات لا تهيج في الصيف, tr:ismun li-iddetin mine'n-nebâti lâ tehîcu fi's-sayf, gloss:yazın sararıp kurumayan birkaç bitkinin adı, source:"ر ب ب,B012"}. Kur'an dünya hayatı benzetmesinde tam da bu "sararıp kurumak" fiilini kullanır. Rab adının ailesindeki sararmayan ot bu sayede otlağın kaderinin karşısına konabilir. Bu bağı dil değil, okuma kurar.

Kur'an bu yolculuğu kendi sözleriyle sahneler. Allah kendini, rüzgârları rahmetinin önünde müjdeci olarak gönderen ve ağır bulutları ölü bir beldeye süren olarak anlatır, sonra şöyle der: {ar:فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:fe-enzelnâ bihi'l-mâe fe-ahracnâ bihî min kulli'ŝ-ŝemerât keẕâlike nuhrici'l-mevtâ leallekum teẕekkerûn, gloss:oraya suyu indirdik ve onunla her türlü üründen çıkardık; ölüleri de böyle çıkarırız; belki düşünüp hatırlarsınız, source:7:57}. Çıkarmak fiili burada hem bitkiye hem ölülere, sonunda da hatırlamaya bağlanır. Sure de dördüncü ayetteki çıkarmadan dokuzuncu ayetteki hatırlatmaya aynı yolla uzanır. Hemen sonraki ayet, iyi toprağın bitkisini {ar:بِإِذْنِ رَبِّهِۦ, tr:bi-izni rabbih, gloss:Rabbinin izniyle, source:7:58} çıkardığını söyler. Başka bir yerde Allah gökten bereketli su indirip onunla ölü bir beldeyi dirilttiğini anlatır ve {ar:كَذَٰلِكَ ٱلْخُرُوجُ, tr:keẕâlike'l-hurûc, gloss:çıkış da böyledir, source:50:11} der. Firavun Musa'ya {ar:فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:fe-men rabbukumâ yâ mûsâ, gloss:ikinizin Rabbi kimdir ey Musa, source:20:49} diye sorduğunda Musa'nın cevabı bu surenin ilk ayetlerindeki sırayı izler: {ar:رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:rabbunelleẕî a'tâ kulle şey'in halkahû ŝumme hedâ, gloss:Rabbimiz her şeye yaratılışını veren sonra yol gösterendir, source:20:50}. Birkaç ayet sonra gökten su indirilir ve {ar:فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ, tr:fe-ahracnâ bihî ezvâcen min nebâtin şettâ, gloss:onunla çeşit çeşit bitkiden çiftler çıkardık, source:20:53}. Surenin son ayetinde sayfaları anılan Musa, Rabbini tanıtırken aynı yaratma, yol gösterme ve çıkarma sırasını kullanır. Bir başka yerde yeryüzü için {ar:أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا, tr:ahrace minhâ mâehâ ve mer'âhâ, gloss:ondan suyunu ve otlağını çıkardı, source:79:31} denir.

Kur'an otun ikinci yarısını, yani kuruyup savrulmasını, dünya hayatının benzetmesi yapar. İki bahçe sahibinin hikâyesinden sonra Allah Peygamber'e şöyle der: {ar:وَٱضْرِبْ لَهُم مَّثَلَ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ, tr:vadrib lehum meŝele'l-hayâti'd-dunyâ ke-mâin enzelnâhu mine's-semâ, gloss:onlara dünya hayatının örneğini ver; gökten indirdiğimiz bir su gibidir, source:18:45}. Yerin bitkisi o suyla karışır, sonra {ar:هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ, tr:heşîmen teẕrûhu'r-riyâh, gloss:rüzgârların savurduğu kuru çöp, source:18:45} olur. Hemen sonraki ayet karşı kefeyi koyar: {ar:وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا, tr:ve'l-bâkıyâtu's-sâlihâtu hayrun inde rabbike sevâben, gloss:kalıcı iyi işler ise Rabbinin katında karşılık bakımından daha hayırlıdır, source:18:46}. Bu iki ayet, beşinci ayetteki döküntüyü on altıncı ve on yedinci ayetteki "dünya hayatı" ile "daha hayırlı ve daha kalıcı" ayrımına bağlayan köprüyü Kur'an'ın kendi ağzından kurar. Aynı benzetme başka bir yerde şu sözlerle gelir: {ar:ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا, tr:ŝumme yehîcu fe-terâhu musferran ŝumme yekûnu hutâmâ, gloss:sonra kurur da onu sapsarı görürsün sonra çer çöp olur, source:57:20}. Bir başka yerde aynı süreç {ar:ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ, tr:ŝumme yec'aluhû hutâmâ inne fî ẕâlike le-ẕikrâ, gloss:sonra onu çer çöpe çevirir; bunda elbette bir öğüt vardır, source:39:21} sözleriyle anlatılır. Bu cümle beşinci ayetteki "çevirdi" fiilini ve dokuzuncu ayetteki "öğüt" kelimesini bir arada tutar. Başka bir yerde yeryüzü süslenir, sahipleri ona güç yetirdiklerini sanır, sonra buyruk gelir: {ar:فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:fe-ce'alnâhâ hasîden ke-en lem teğne bi'l-ems, gloss:onu dün hiç yokmuş gibi biçilmiş hale getirdik, source:10:24}. Kelimenin kendisi de Kur'an'da bir topluluk için kullanılır. Bir önceki kavimden sonra yaratılan bir neslin hikâyesinde, onları yakalayan çığlığın ardından şöyle denir: {ar:فَجَعَلْنَٰهُمْ غُثَآءًۭ, tr:fe-ce'alnâhum ğuŝâen, gloss:onları sel döküntüsüne çevirdik, source:23:41}. Fiil de kelime de aynıdır, ama burada ot yerine insanlar vardır.

Kaynaklar: 87:1 ٱسْمَ س م و B004; 87:1 ٱسْمَ و س م B003; 87:1 رَبِّ ر ب ب B008; 87:1 رَبِّ ر ب ب B007; 87:1 رَبِّ ر ب ب B012; 87:11 يَتَجَنَّبُهَا ج ن ب B006; 87:4 أَخْرَجَ خ ر ج B005; 87:4 أَخْرَجَ خ ر ج B002; 87:4 أَخْرَجَ خ ر ج B007; 87:4 ٱلْمَرْعَىٰ ر ع ي B001; 87:5 فَجَعَلَهُۥ ج ع ل B002; 87:5 غُثَآءً غ ث و B002; 87:5 غُثَآءً غ ث و B001; 87:5 أَحْوَىٰ ح و ي B006; 87:7 يَخْفَىٰ خ ف ي B004; 87:7 يَخْفَىٰ خ ف ي B003; 87:17 أَبْقَىٰٓ ب ق ي B005; 87:13 يَحْيَىٰ ح ي ي B002; 87:13 يَمُوتُ م و ت B003

## Sel: köpük gider, su kalır

Beşinci ayetteki غثاء yalnızca kurumuş ot değildir, selin yüzünde yüzen şeydir de. Arapça onu iki ayrı kaba birden koyar: {ar:الغثاء غثاء السيل والقدر، ما يطفح ويتفرق من النبات اليابس وزبد القدر, tr:el-ğuŝâu ğuŝâu's-seyli ve'l-kıdr mâ yatfahu ve yetefarraku mine'n-nebâti'l-yâbisi ve zebedi'l-kıdr, gloss:ğuŝâ selin de tencerenin de ğuŝâsıdır; kuru bitkiden ve tencere köpüğünden yüzeye taşıp dağılandır, source:"غ ث و,B001"}. Kelime bir atasözü değeri de taşır: {ar:يضرب به المثل فيما يضيع ويذهب غير معتد به, tr:yudrabu bihi'l-meŝelu fî mâ yadîu ve yeẕhebu ğayra mu'teddin bih, gloss:kaybolup giden ve hesaba katılmayan şey için örnek olarak anılır, source:"غ ث و,B004"}. Selin öbür yüzü sudur. Surenin kelimelerinin aileleri suyun nerede toplanıp kaldığını gösterir.

İkinci ayetteki "yarattı" fiilinin ailesinde kayalardaki oyuklar vardır: {ar:الخليقة نقر في صخرة يجتمع فيه ماء السماء, tr:el-halîka nakrun fî sahratin yectemiu fîhi mâu's-semâ, gloss:halîka kayada gök suyunun toplandığı oyuktur, source:"خ ل ق,B011"}. Bu oyuklar şöyle de anlatılır: {ar:قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها تسميها العرب الخلائق, tr:kılâten tumsiku mâe's-sehâbi fî safâtin halakahallâhu fîhâ tusemmîhe'l-arabu'l-halâik, gloss:Allah'ın düz kayada yarattığı ve bulut suyunu tutan çukurlar; Araplar onlara halâik der, source:"خ ل ق,B011"}. Beşinci ayetteki أحوى'nın ailesinde selin doldurduğu kıvrımlı çukurlar vardır: {ar:الحوايا التي تكون في القيعان والرياض حفائر ملتوية يملؤها ماء السيل, tr:el-havâyâ elletî tekûnu fi'l-kîâni ve'r-riyâdi hafâiru multeviyetun yemleuhâ mâu's-seyl, gloss:havâyâ düzlüklerde ve çayırlarda selin doldurduğu kıvrımlı çukurlardır, source:"ح و ي,B008"}. "Rab" kelimesinin ailesinde bol su, toplandığı için bu adı alır: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabeb ve huve'l-mâu'l-keŝîr sumiye bi-ẕâlike li-ictimâih, gloss:rabeb boldur ve toplandığı için bu adı almıştır, source:"ر ب ب,B013"}. Yedinci ayetteki "açık" kelimesinin ailesinde kuyu temizlenir: {ar:جهرت الركية إذا كان ماؤها قد غطى الطين فنقى ذلك حتى يظهر الماء ويصفو, tr:cehertu'r-rakiyye iẕâ kâne mâuhâ kad ğattâhu't-tînu fe-nakkâ ẕâlike hattâ yezhera'l-mâu ve yesfû, gloss:suyunu çamur örtmüş kuyuyu su görünüp duruluncaya kadar temizledim, source:"ج ه ر,B008"}. Aynı ayetteki "bilir" fiilinin ailesinde de suyu bol kuyu vardır: {ar:العيلم البئر الكثيرة الماء, tr:el-aylem el-bi'ru'l-keŝîratu'l-mâ, gloss:aylem suyu bol kuyudur, source:"ع ل م,B005"}.

Dokuzuncu ayet öğütten "fayda verirse" diye söz eder, on yedinci ayet ahireti "daha kalıcı" diye niteler. Fayda, {ar:ما يستعان به في الوصول إلى الخيرات, tr:mâ yusteânu bihî fi'l-vusûli ile'l-hayrât, gloss:iyiliklere ulaşmak için yardım alınan şey, source:"ن ف ع,B001"} diye tanımlanır. Bu tanım on yedinci ayetteki "hayırlı" kelimesinin kökünü de taşır. Kalıcılık ise şudur: {ar:البقاء ثبات الشيء على حاله الأولى وهو يضاد الفناء, tr:el-bekâu ŝebâtu'ş-şey'i alâ hâlihi'l-ûlâ ve huve yudâddu'l-fenâ, gloss:bekâ bir şeyin ilk halinde sabit durmasıdır ve yok olmanın zıddıdır, source:"ب ق ي,B001"}. Bu tanımda on sekizinci ayetteki "ilk" kelimesi de vardır.

Kur'an'da bu iki yüzü bir sahnede toplayan benzetmeyi Allah verir. Gökten su iner, vadiler {ar:فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا, tr:fe-sâlet evdiyetun bi-kaderihâ, gloss:vadiler kendi ölçülerince akar, source:13:17}. Burada üçüncü ayetteki "ölçtü" fiilinin kökü geçer. Sel kabarık bir köpük taşır. İnsanların süs ya da eşya için ateşte erittikleri madenin de benzer bir köpüğü vardır. Sonra ayırım gelir: {ar:فَأَمَّا ٱلزَّبَدُ فَيَذْهَبُ جُفَآءًۭ ۖ وَأَمَّا مَا يَنفَعُ ٱلنَّاسَ فَيَمْكُثُ فِى ٱلْأَرْضِ, tr:fe-emme'z-zebedu fe-yeẕhebu cufâen ve emmâ mâ yenfau'n-nâse fe-yemkuŝu fi'l-ard, gloss:köpük atılıp gider; insanlara fayda veren ise yerde kalır, source:13:17}. Kelime farklıdır, orada غثاء değil زبد geçer. Ama sahne aynıdır. Surenin beşinci, dokuzuncu ve on yedinci ayetlere dağıttığı döküntü, fayda ve kalıcılık bu ayette tek bir selin içinde bir aradadır. Bu yan yana koyuş surenin kendi sözü değildir, ama bu ayet ona Kur'an'dan bir dayanak verir. Fayda verirse sunulan öğüt, kayadaki oyukta tutulan suya benzer. Çerçöp ise akıntıyla gidip hesaba katılmayan şeydir.

Kaynaklar: 87:5 غُثَآءً غ ث و B001; 87:5 غُثَآءً غ ث و B004; 87:9 نَّفَعَتِ ن ف ع B001; 87:17 أَبْقَىٰٓ ب ق ي B001; 87:2 خَلَقَ خ ل ق B011; 87:5 أَحْوَىٰ ح و ي B008; 87:1 رَبِّ ر ب ب B013; 87:7 ٱلْجَهْرَ ج ه ر B008; 87:7 يَعْلَمُ ع ل م B005

## Ölçüp biçmek: ok, tulum ve kura

İkinci ve üçüncü ayet dört fiili sıralar: {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:elleẕî halaka fe-sevvâ, gloss:yaratıp düzene koyan, source:87:2}, {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:velleẕî kaddera fe-hedâ, gloss:ölçüp yol gösteren, source:87:3}. Arapçada bu fiiller bir zanaatkârın işinin adımlarıdır. خلق, kökünde ölçüp biçmektir: {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhû et-takdîru'l-mustakîm, gloss:halkın aslı doğru ölçüdür, source:"خ ل ق,B001"}. Bu tanım ikinci ayetin fiilini üçüncü ayetin fiiline bağlar. Ölçülüp yontulmuş ok da bu köktendir: {ar:سهم مخلق أملس مستو, tr:sehmun muhallakun emlesu mustevin, gloss:yontulmuş düzgün ve doğru ok, source:"خ ل ق,B008"}. Bu tanımda ikinci ayetin öbür fiili olan سوّى'nin kökü de vardır. سوّى eğri olanı doğrultmaktır: {ar:استوى من اعوجاج, tr:istevâ min i'vicâc, gloss:eğrilikten doğruldu, source:"س و ي,B002"}. قدّر, bir şeyi nasıl düzleyip hazır edeceğini düşünmektir: {ar:التروية والتفكير في تسوية أمر وتهيئته, tr:et-terviyetu ve't-tefkîru fî tesviyeti emrin ve teh'iyetih, gloss:bir işi nasıl düzleyip hazırlayacağını uzun uzun düşünmek, source:"ق د ر,B005"}. Aynı kök bir şeyin vardığı ölçüyü de bildirir: {ar:مبلغ الشيء وكنهه ونهايته, tr:mebleğu'ş-şey'i ve kunhuhû ve nihâyetuh, gloss:bir şeyin vardığı yer ve özü ve sonu, source:"ق د ر,B001"}. Sonra هدى gelir. Bu kelime okun önde giden ucudur: {ar:هادي السهم نصله, tr:hâdi's-sehmi naslu, gloss:okun hâdîsi temrenidir, source:"ه د ي,B003"}. Değnek de taşıyanın önünden gittiği için bu adı alır: {ar:العصا هاديا لأنها تتقدمه, tr:el-asâ hâdiyen li-ennehâ tetekaddemuh, gloss:değnek önünden gittiği için hâdî adını alır, source:"ه د ي,B003"}. Rab ise bir şeyi düzeltip adım adım tamamlayandır: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye bir şeyi halden hale geçirerek tamamlanma sınırına kadar oluşturmaktır, source:"ر ب ب,B002"}.

Değneği doğrultmanın bir yolu da ateştir. Bu işin fiili, on ikinci ayetteki "ateşe girer" fiilinin kendisidir: {ar:صلى عصاه إذا أدارها على النار يثقفها, tr:salâ asâhu iẕâ edârahâ ale'n-nâri yuŝakkıfuhâ, gloss:değneğini ateşin üstünde çevirip doğrulttu, source:"ص ل ي,B004"}. Ölçmek, doğrultmak ve uç takmak, ikinci ve üçüncü ayetin düz anlamının yanında bir yapım sahnesi kurar. Yapılan şey yalnızca var edilmez, bir yöne de çevrilir. "Yol gösterdi" fiili okun ucunun bir hedefe dönmesi gibi duyulur.

Aynı ölçüp biçme bir deri üzerinde de yapılır. خلق'in ilk örneği, su tulumu için deriyi kesmeden önce ölçmektir: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme iẕâ kaddertuhû kable'l-kat', gloss:deriyi kesmeden önce ölçtüğümde halaktu derim, source:"خ ل ق,B001"}. İkinci ayetin fiili ile üçüncü ayetin fiili burada tek bir hareketin iki adı olur. Bitmiş kabın yapısını dokuzuncu ayetteki نفع kökü anlatır: {ar:النفع في المزادة في جانبيها يشق الأديم فيجعل في جانبيها في كل جانب نفعة, tr:en-nif'u fi'l-mezâdeti fî cânibeyhâ yuşakku'l-edîmu fe-yuc'alu fî cânibeyhâ fî kulli cânibin nif'a, gloss:su kırbasının iki yanına deri yarılıp her yana nif'a denen bir parça konur, source:"ن ف ع,B002"}. Bu yanlar on birinci ayetteki kelimenin köküyle anılır: {ar:الجنبتان ناحيتا كل شيء, tr:el-canbetân nâhiyetâ kulli şey', gloss:her şeyin iki yanı, source:"ج ن ب,B001"}. Deri yağla terbiye edilir. Bu da "Rab" kelimesinin ailesindendir: {ar:رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب, tr:rabebtu'l-edîme bi's-semni ve'd-devâe bi'l-asel ve sikâun merbûb, gloss:deriyi yağla ilacı balla terbiye ettim; terbiye edilmiş tulum, source:"ر ب ب,B006"}. Tulum çalkalanır: {ar:جهرت السقاء مخضته, tr:cehertu's-sikâe mehadtuhû, gloss:tulumu çalkaladım, source:"ج ه ر,B010"}. Kullanıldıkça da aşınıp düzleşir: {ar:أخلق الشيء وخلق إذا بلي؛ إذا أخلق املاس وذهب زئبره, tr:ahleka'ş-şey'u ve haleka iẕâ beliye iẕâ ahleka imlâsse ve ẕehebe zi'biruh, gloss:bir şey eskiyince ahleka denir; eskiyince düzleşir ve tüyü gider, source:"خ ل ق,B009"}. Beş kök tek bir nesnede, ölçülen, yanları eklenen, terbiye edilen ve eskiyen bir tulumda buluşur. Kur'an bu nesneyi bir sahnede kullanmaz. Ama aynı kelime ailesi yaratılışı bir zanaat olarak duyurur, ve bu zanaatta ölçü kesmeden önce gelir.

Üçüncü bir nesne, kura okudur. "Rab" kelimesinin ailesinde okların saklandığı torba vardır: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-ribâbe şebîhetun bi'l-kinâneti tucmeu fîhâ sihâmu'l-meysir, gloss:ribâbe meysir oklarının toplandığı sadağa benzer torbadır, source:"ر ب ب,B010"}. Bu tanım sekizinci ayetteki "kolaylaştırırız" fiilinin kökünü, meysiri, de içerir. Meysir bir oyundur ve adı paylaştırmadan gelir: {ar:يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها, tr:yasera'l-kavmu'l-cezûra ey ictezerûhâ ve'ktesemû a'dâehâ, gloss:topluluk deveyi kesip parçalarını paylaştı, source:"ي س ر,B007"}. Okların en büyük payı alanı birinci ayetteki "en yüce" kelimesinin kökündendir: {ar:المعلى السابع من القداح, tr:el-muallâ es-sâbiu mine'l-kıdâh, gloss:muallâ okların yedincisidir, source:"ع ل و,B009"}. Okun gövdesi yontulup yumuşatılır: {ar:المخلق القدح إذا لين, tr:el-muhallak el-kıdhu iẕâ luyyine, gloss:muhallak yumuşatılmış ok gövdesidir, source:"خ ل ق,B008"}. Pay da aynı köktendir: {ar:الخلاق النصيب لأنه قد قدر لكل أحد نصيبه, tr:el-halâk en-nasîb li-ennehû kad kuddira li-kulli ehadin nasîbuh, gloss:halâk paydır çünkü herkesin payı ölçülmüştür, source:"خ ل ق,B006"}. Her şeyin bir ölçüsü ve bir vadesi vardır: {ar:لكل شيء مقدار وأجل, tr:li-kulli şey'in mikdârun ve ecel, gloss:her şeyin bir miktarı ve süresi vardır, source:"ق د ر,B001"}. İkinci ve üçüncü ayetteki ölçüp biçme bu sahnede paylaştırmaya döner. On altıncı ve on yedinci ayetteki seçim de bir pay seçimidir.

Kur'an bu ölçmeyi yaratılışın kendisine uygular. Allah inkâr eden insan için {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe-kaddera, gloss:onu bir damladan yarattı ve ölçüsünü koydu, source:80:19} der, sonra {ar:ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ, tr:ŝumme's-sebîle yesserah, gloss:sonra yolu ona kolaylaştırdı, source:80:20} diye ekler. Bu iki ayet surenin ikinci, üçüncü ve sekizinci ayetlerinin fiillerini aynı sırayla verir. Başka bir yerde Allah {ar:وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا, tr:ve halaka kulle şey'in fe-kaddarahû takdîrâ, gloss:her şeyi yarattı ve ona tam ölçüsünü verdi, source:25:2} ve {ar:إِنَّا كُلَّ شَىْءٍ خَلَقْنَٰهُ بِقَدَرٍۢ, tr:innâ kulle şey'in halaknâhu bi-kader, gloss:biz her şeyi bir ölçüyle yarattık, source:54:49} der. Surenin son ayetinde adı geçen İbrahim, putları reddedip kavmine Âlemlerin Rabbini anlatırken bu ikiliyi kendi ağzından söyler: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:elleẕî halakanî fe-huve yehdîn, gloss:beni yaratan ve bana yol gösteren O'dur, source:26:78}. Pay kelimesi Kur'an'da tam bu surenin vardığı karşıtlıkla geçer. Hac ibadetleri anlatılırken yalnız bu dünyada verilmesini isteyen kişi için {ar:وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ, tr:ve mâ lehû fi'l-âhireti min halâk, gloss:onun ahirette hiçbir payı yoktur, source:2:200} denir. Önceki kavimler için {ar:فَٱسْتَمْتَعُوا۟ بِخَلَٰقِهِمْ, tr:fe'stemteû bi-halâkıhim, gloss:paylarından yararlandılar, source:9:69} denir, ayetin sonunda da yaptıkları dünyada ve ahirette boşa gider. Kura okları ve meysir müminlere yasaklanırken kullanılan kelimeler ise surenin iki kelimesini yan yana getirir: {ar:فَٱجْتَنِبُوهُ لَعَلَّكُمْ تُفْلِحُونَ, tr:fectenibûhu leallekum tuflihûn, gloss:ondan uzak durun ki kurtuluşa eresiniz, source:5:90}. On birinci ayetteki "uzak durmak" ve on dördüncü ayetteki "kurtuluşa ermek" burada aynı cümlededir. Başka bir yerde meysir için {ar:وَإِثْمُهُمَآ أَكْبَرُ مِن نَّفْعِهِمَا, tr:ve ismuhumâ ekberu min nef'ihimâ, gloss:günahları faydalarından büyüktür, source:2:219} denir. Oklarla kısmet aramak da sayılan yasaklar arasındadır: {ar:وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ, tr:ve en testaksimû bi'l-ezlâm, gloss:fal oklarıyla pay aramanız, source:5:3}. Kura okuyla alınan pay yasaklanır. Ölçüyü koyanın verdiği pay ise ahirette de geçerlidir.

Kaynaklar: 87:2 خَلَقَ خ ل ق B001; 87:2 خَلَقَ خ ل ق B008; 87:2 خَلَقَ خ ل ق B009; 87:2 خَلَقَ خ ل ق B006; 87:2 فَسَوَّىٰ س و ي B002; 87:3 قَدَّرَ ق د ر B005; 87:3 قَدَّرَ ق د ر B001; 87:3 فَهَدَىٰ ه د ي B003; 87:1 رَبِّ ر ب ب B002; 87:1 رَبِّ ر ب ب B006; 87:1 رَبِّ ر ب ب B010; 87:12 يَصْلَى ص ل ي B004; 87:9 نَّفَعَتِ ن ف ع B002; 87:11 يَتَجَنَّبُهَا ج ن ب B001; 87:7 ٱلْجَهْرَ ج ه ر B010; 87:1 ٱلْأَعْلَى ع ل و B009; 87:8 لِلْيُسْرَىٰ ي س ر B007

## Damga: deriye basılan iz

Daha önce anılan ikinci türetme, birinci ayetteki "ad" kelimesini وسم köküne, yani damgaya bağlar. Bu kök kimliği tartışmalıdır, ama yolun sonundaki sahne açıktır: {ar:الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي, tr:el-vesmu eseru keyyin ve baîrun mevsûmun vusime bi-simetin yu'rafu bihâ min kat'ı uẕunin ev keyy, gloss:vesm dağlama izidir; damgalı deve kulak kesiği ya da dağlama gibi tanındığı bir işaretle işaretlenmiştir, source:"و س م,B001"}. Damgayı basan alet de bu köktendir: {ar:الميسم المكواة أو الشيء الذي يوسم به الدواب, tr:el-mîsem el-mikvâtu evi'ş-şey'u'lleẕî yûsemu bihi'd-devâbb, gloss:mîsem dağlama demiri ya da hayvanların işaretlendiği aletidir, source:"و س م,B001"}. "İz" diye çevrilen أثر, on altıncı ayetteki تُؤْثِرُونَ kelimesinin köküdür. Damganın sahibi rabdir: {ar:رب كل شئ: مالكه, tr:rabbu kulli şey'in mâlikuh, gloss:her şeyin rabbi sahibidir, source:"ر ب ب,B001"}. Ad, bu sahnede bir şeyin kime ait olduğunu gösteren ve onu ötekilerden ayıran işarettir. "Rabbinin adını tesbih et" emri, düz anlamının yanında, Rabbin işaretini her türlü kusurdan arınmış tutma emri olarak da duyulur.

Surenin başka kelimeleri aynı sahneye girer. On ikinci ayetteki "ateş" kelimesi damganın kendisi için de kullanılır: {ar:ما نار هذه الناقة أي ما سمتها؛ نجارها نارها, tr:mâ nâru hâẕihi'n-nâkati ey mâ simetuhâ nicâruhâ nâruhâ, gloss:bu devenin nârı nedir yani damgası nedir; soyu damgasından bellidir, source:"ن و ر,B002"}. Bu ifade ateş ile damganın kökünü tek cümlede birleştirir. On altıncı ayetteki kökün ailesinde devenin ayağına basılan iz de vardır: {ar:المئثرة حديدة يؤثر بها خف البعير ليعرف أثره في الأرض, tr:el-mi'ŝera hadîdetun yu'ŝeru bihâ huffu'l-baîri li-yu'rafe eseruhû fi'l-ard, gloss:mi'ŝera devenin tabanına iz basılan demirdir; böylece yerdeki izi tanınır, source:"ء ث ر,B008"}. İz, bir şeyden geriye kalandır: {ar:الأثر بقية ما يرى من كل شيء وما لا يرى بعد أن تبقى فيه علقة, tr:el-eser bakıyyetu mâ yurâ min kulli şey'in ve mâ lâ yurâ ba'de en tebkâ fîhi alaka, gloss:eser her şeyden görünen ya da görünmeyip bir ilişiği kalan artıktır, source:"ء ث ر,B003"}. Bu tanım on altıncı ayetin kökünü on yedinci ayetin köküne bağlar. Yedinci ayetteki "bilir" fiilinin kökü de ayırt edici işarettir: {ar:أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره, tr:aslun sahîhun vâhidun yedullu alâ eserin bi'ş-şey'i yetemeyyezu bihî an ğayrih, gloss:bir şeyi ötekilerden ayıran iz anlamında tek bir köktür, source:"ع ل م,B002"}. Damga yüzde de okunur: {ar:توسمت فيه الخير والشر أي رأيت فيه أثرا, tr:tevessemtu fîhi'l-hayra ve'ş-şerra ey raeytu fîhi eseren, gloss:onda iyiliği ya da kötülüğü sezdim yani onda bir iz gördüm, source:"و س م,B002"}. Bu ifade on yedinci ayetteki "hayırlı" kelimesinin kökünü de içerir.

Düz bir okuma, on altıncı ayetteki "tercih edersiniz" fiilini yalnızca bir eğilim olarak görür. Damga sahnesi, aynı kökün iz bırakmak ve izden tanınmak demek olduğunu duyurur. Tercih edilen şey kişide bir iz bırakır ve kişi o izden tanınır. Sure bu izi iki türlü gösterir: birinde Rabbin adı anılır, ötekinde ateş vardır.

Kur'an damgayı bir tehdit olarak kullanır. Allah Peygamber'e çok yemin eden, aşağılık, söz taşıyan kişiye uymamasını söyler. Bu kişi ayetler okunduğunda {ar:أَسَٰطِيرُ ٱلْأَوَّلِينَ, tr:esâtîru'l-evvelîn, gloss:öncekilerin masalları, source:68:15} der, ve hükmü şudur: {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:se-nesimuhû ale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. "Öncekiler" kelimesi surenin on sekizinci ayetindeki "ilk sayfalar"ın köküdür. İlk sayfaları masal sayan kişi damgalanır. Lut kavmini sabahleyin çığlık yakalayıp şehirlerinin altı üstüne getirildikten sonra şöyle denir: {ar:إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّلْمُتَوَسِّمِينَ, tr:inne fî ẕâlike le-âyâtin li'l-mutevessimîn, gloss:bunda işaretleri okuyanlar için ibretler vardır, source:15:75}. Yıkılmış bir yerden iz okumak, damganın öbür yüzüdür. Peygamber'in arkadaşları için de {ar:سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ, tr:sîmâhum fî vucûhihim min eseri's-sucûd, gloss:işaretleri yüzlerindedir; secdenin izinden, source:48:29} denir. Buradaki سيما başka bir köke yazılır, bu yüzden kök kimliği kurmaz. Ama yanındaki أثر, on altıncı ayetin köküdür, ve iz burada namazın bıraktığı izdir.

Kaynaklar: 87:1 ٱسْمَ و س م B001; 87:1 ٱسْمَ و س م B002; 87:12 ٱلنَّارَ ن و ر B002; 87:16 تُؤْثِرُونَ ء ث ر B008; 87:16 تُؤْثِرُونَ ء ث ر B003; 87:7 يَعْلَمُ ع ل م B002; 87:1 رَبِّ ر ب ب B001

## Tesbih, anma, namaz: sureyi açan ve kapayan iş

Birinci ayetin emri olan {ar:سَبِّحِ ٱسْمَ رَبِّكَ, tr:sebbihi'sme rabbik, gloss:Rabbinin adını tesbih et, source:87:1} on beşinci ayette bir kişinin yaptığı iş olarak geri döner: {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve ẕekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını anıp namaz kıldı, source:87:15}. Arapça bu üç fiili, tesbihi, anmayı ve namazı, tek bir uygulama olarak ele alır. Tesbih nafile anma ve namazdır: {ar:السبحة التطوع من الذكر والصلاة, tr:es-subha et-tetavvuu mine'ẕ-ẕikri ve's-salât, gloss:subha nafile anma ve namazdır, source:"س ب ح,B001"}. {ar:التسبيح عاما في العبادات قولا كان أو فعلا أو نية, tr:et-tesbîhu âmmen fi'l-ibâdâti kavlen kâne ev fi'len ev niyye, gloss:tesbih söz iş ya da niyet olarak bütün ibadetler için genel bir addır, source:"س ب ح,B001"}. Anma namaz, dua ve övgüdür: {ar:الذكر الصلاة والدعاء والثناء, tr:eẕ-ẕikru's-salâtu ve'd-duâu ve's-senâ, gloss:zikir namaz dua ve övgüdür, source:"ذ ك ر,B005"}. Kur'an okumak da anmadır: {ar:الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة, tr:eẕ-ẕikru kırâetu'l-kur'âni ve't-tesbîhu ve'd-duâu ve'ş-şukru ve't-tâa, gloss:zikir Kur'an okumak tesbih dua şükür ve itaattir, source:"ذ ك ر,B005"}. Bu tanım altıncı ayetteki "okutacağız" fiilinin kökünü de içerir. Anma dilde dolaşan addır: {ar:الذكر جري الشيء على لسانك, tr:eẕ-ẕikru cerayu'ş-şey'i alâ lisânik, gloss:zikir bir şeyin dilinde dolaşmasıdır, source:"ذ ك ر,B004"}. Namazın kendisi bir dizi harekettir: {ar:الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح, tr:es-salâtu mine'l-mahlûkîn el-kıyâmu ve'r-rukûu ve's-sucûdu ve'd-duâu ve't-tesbîh, gloss:yaratılmışlar için namaz kıyam rükû secde dua ve tesbihtir, source:"ص ل و,B003"}. Namaz dua da demektir: {ar:الصلاة وهي الدعاء, tr:es-salâtu ve hiye'd-duâ, gloss:salât duadır, source:"ص ل و,B002"}. Aynı kök, Allah'ın kullarına yönelişini de anlatır: {ar:صلاة الله للمسلمين تزكيته إياهم, tr:salâtullâhi li'l-muslimîne tezkiyetuhû iyyâhum, gloss:Allah'ın Müslümanlara salâtı onları arındırmasıdır, source:"ص ل و,B002"}. Bu tanım on beşinci ayeti on dördüncü ayete bağlar. Kişinin namazı ile Allah'ın arındırması aynı kökün iki yönüdür.

Namaz bedensel bir iştir ve kelimelerin aileleri bedeni gösterir. Tesbih kökü secde yerlerini adlandırır: {ar:السبحات مواضع السجود, tr:es-subuhât mevâdiu's-sucûd, gloss:subuhât secde yerleridir, source:"س ب ح,B003"}. Namaz kökü sırtın ortasını adlandırır: {ar:الصلا وسط الظهر لكل ذي أربع وللناس, tr:es-salâ vasatu'z-zahri li-kulli ẕî erbain ve li'n-nâs, gloss:salâ dört ayaklının ve insanın sırtının ortasıdır, source:"ص ل و,B005"}. Yedinci ayetteki "açık" kelimesinin kökü sesli kılınan namazı ve okumayı anlatır: {ar:جهر بكلامه وصلاته وقراءته, tr:cehera bi-kelâmihî ve salâtihî ve kırâetih, gloss:sözünü namazını ve okumasını açıktan yaptı, source:"ج ه ر,B001"}. Böylece sure ibadeti iki uçta kurar. Birinci ayette bir emir olarak başlar, on beşinci ayette bir insanın hareketleri olarak tamamlanır. Arada okuma, öğüt ve unutmama vardır. Bunların hepsi aynı uygulamanın parçalarıdır.

Kur'an bu üçlüyü sık sık birlikte sahneler. Yükseltilmiş evlerde adın anılıp tesbih edildiği ayetin hemen ardından şöyle denir: {ar:رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ, tr:ricâlun lâ tulhîhim ticâratun ve lâ bey'un an ẕikrillâhi ve ikâmi's-salâti ve îtâi'z-zekât, gloss:ne ticaretin ne alışverişin Allah'ı anmaktan namazı kılmaktan ve zekâtı vermekten alıkoymadığı adamlar, source:24:37}. Bu ayette surenin on dördüncü ve on beşinci ayetlerindeki üç kelime aynı sırayla bulunur. Musa ateşin başında {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14} emrini alır. Aynı konuşmada kardeşini yardımcı olarak isterken amacını şöyle söyler: {ar:كَىْ نُسَبِّحَكَ كَثِيرًۭا, tr:key nusebbihake keŝîrâ, gloss:seni çokça tesbih edelim diye, source:20:33}, {ar:وَنَذْكُرَكَ كَثِيرًا, tr:ve neẕkurake keŝîrâ, gloss:ve seni çokça analım diye, source:20:34}. Peygamber'e de {ar:وَسَبِّحْ بِحَمْدِ رَبِّكَ قَبْلَ طُلُوعِ ٱلشَّمْسِ وَقَبْلَ غُرُوبِهَا, tr:ve sebbih bi-hamdi rabbike kable tulûi'ş-şemsi ve kable ğurûbihâ, gloss:güneş doğmadan ve batmadan önce Rabbini överek tesbih et, source:20:130} denir. Müminlere cuma günü namaza çağrıldıklarında {ar:فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ, tr:fe's'av ilâ ẕikrillâh, gloss:Allah'ı anmaya koşun, source:62:9} denir. Namaz bitince de {ar:وَٱذْكُرُوا۟ ٱللَّهَ كَثِيرًۭا لَّعَلَّكُمْ تُفْلِحُونَ, tr:veẕkurullâhe keŝîran leallekum tuflihûn, gloss:Allah'ı çokça anın ki kurtuluşa eresiniz, source:62:10} denir. Bu emirde on beşinci ayetteki anma, on dördüncü ayetteki kurtuluşa bağlanır. Başka bir yerde namazın işi şöyle anlatılır: {ar:إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۗ وَلَذِكْرُ ٱللَّهِ أَكْبَرُ, tr:inne's-salâte tenhâ ani'l-fahşâi ve'l-munker ve le-ẕikrullâhi ekber, gloss:namaz hayâsızlıktan ve kötülükten alıkoyar; Allah'ı anmak ise elbette en büyüktür, source:29:45}. Bu ayette "en büyük" sıfatı anmaya verilir. Surede ise aynı kökten gelen "en büyük" sıfatı ateşe verilir. Namaz kılanlar arasında bile bir ayrım vardır: {ar:فَوَيْلٌۭ لِّلْمُصَلِّينَ, tr:fe-veylun li'l-musallîn, gloss:yazıklar olsun o namaz kılanlara, source:107:4}, {ar:ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ, tr:elleẕîne hum an salâtihim sâhûn, gloss:onlar ki namazlarından gafildirler, source:107:5}. Gaflet, altıncı ayetteki unutmanın bir türüdür.

Kaynaklar: 87:1 سَبِّحِ س ب ح B001; 87:1 سَبِّحِ س ب ح B003; 87:15 وَذَكَرَ ذ ك ر B005; 87:15 وَذَكَرَ ذ ك ر B004; 87:15 فَصَلَّىٰ ص ل و B003; 87:15 فَصَلَّىٰ ص ل و B002; 87:15 فَصَلَّىٰ ص ل و B005; 87:7 ٱلْجَهْرَ ج ه ر B001

## Açık ve gizli: ses ve örtüden çıkan

Yedinci ayetin sonu {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ, tr:innehû ya'lemu'l-cehra ve mâ yahfâ, gloss:O açığa vurulanı da gizli kalanı da bilir, source:87:7} der. Bu cümle iki ayrı sahnede duyulur. Birincisi sestir. جهر sesi yükseltmektir: {ar:جهر بالقول رفع به صوته, tr:cehera bi'l-kavli rafea bihî savtah, gloss:sözü açıktan söyledi yani sesini yükseltti, source:"ج ه ر,B001"}. {ar:الجهر ضد السر, tr:el-cehru diddu's-sirr, gloss:cehr gizlinin zıddıdır, source:"ج ه ر,B001"}. Bu kök tek bir harfin söylenişine kadar iner: {ar:سمي الحرف مجهورا لأنه أشبع الاعتماد في موضعه ومنع النفس أن يجري معه, tr:sumiye'l-harfu mechûran li-ennehû eşbea'l-i'timâde fî mevdiihî ve menea'n-nefese en yecriye meah, gloss:harfe mechûr denir çünkü çıkış yerine tam dayanır ve nefesin onunla akmasını engeller, source:"ج ه ر,B011"}. خفي sesi kısmaktır: {ar:أخفيت الصوت إخفاء ... والخافية ضد العلانية ولقيته خفيا أي سرا, tr:ahfeytu's-savte ihfâen ve'l-hâfiyetu diddu'l-alâniye ve lekîtuhû hafiyyen ey sirran, gloss:sesi kıstım; hâfiye açıklığın zıddıdır; onunla gizlice karşılaştım, source:"خ ف ي,B001"}. On beşinci ayetteki anma iki yerde yaşar: {ar:ذكرته بلساني وبقلبي, tr:ẕekertuhû bi-lisânî ve bi-kalbî, gloss:onu dilimle ve kalbimle andım, source:"ذ ك ر,B004"}. Okuma da ezberden yapılır: {ar:قرأت القرآن عن ظهر قلب أو نظرت فيه, tr:kara'tu'l-kur'âne an zahri kalbin ev nazartu fîh, gloss:Kur'an'ı ezberden ya da bakarak okudum, source:"ق ر ء,B002"}. Bilmek de söylenenin farkında olmaktır: {ar:ما علمت بخبرك أي ما شعرت به, tr:mâ alimtu bi-haberike ey mâ şaartu bih, gloss:haberini bilmedim yani farkına varmadım, source:"ع ل م,B001"}. Bu sahnede yedinci ayet, altıncı ayetteki okumanın iki halini, yüksek sesle ve içten okumayı birlikte kucaklar. Okutulan söz dilde de olsa kalpte de olsa bilinir.

İkinci sahne örtüden çıkmaktır. "Gizli" kökü, Arapçada zıt anlamları birlikte taşıyan kelimelerden biridir: {ar:خفيت الشيء بغير ألف إذا أظهرته, tr:hafeytu'ş-şey'e bi-ğayri elifin iẕâ azhartah, gloss:elifsiz hafeytu bir şeyi açığa çıkardım demektir, source:"خ ف ي,B003"}. {ar:استخفيت الشئ أي استخرجته, tr:istahfeytu'ş-şey'e ey istahrectuh, gloss:bir şeyi çıkardım, source:"خ ف ي,B003"}. Bu ikinci açıklama dördüncü ayetin "çıkarmak" kökünü kullanır, ki o kökün temel anlamı şudur: {ar:خرج خروجا برز من مقره أو حاله, tr:harace hurûcen beraze min makarrihî ev hâlih, gloss:yerinden ya da halinden dışarı belirdi, source:"خ ر ج,B001"}. Örtülü olanın somut örnekleri de vardır: {ar:الخوافي سعفات يلين قلب النخلة, tr:el-havâfî saafâtun yelîne kalbe'n-nahle, gloss:havâfî hurmanın göbeğine yakın dallardır, source:"خ ف ي,B002"}. {ar:الخوافي جمع خافية وهي ما دون القوادم من الريش, tr:el-havâfî cem'u hâfiye ve hiye mâ dûne'l-kavâdimi mine'r-rîş, gloss:havâfî kanadın ön tüylerinin altında kalan tüylerdir, source:"خ ف ي,B002"}. Öbür uçta açık olan vardır: {ar:كل شيء بدا فقد جهر, tr:kullu şey'in bedâ fe-kad cehera, gloss:ortaya çıkan her şey açığa çıkmıştır, source:"ج ه ر,B002"}, ve temizlenip suyu görünen kuyu bu kökle anılır. Açıklığın bir tersi de vardır: {ar:العين الجهراء التي لا تبصر في الشمس, tr:el-aynu'l-cehrâ elletî lâ tubsiru fi'ş-şems, gloss:cehrâ göz güneşte göremeyen gözdür, source:"ج ه ر,B004"}. Fazla ışık da bir örtü olabilir. Dördüncü ayetle birlikte okununca yedinci ayetin ikilisi sabit iki durum olmaktan çıkar ve bir harekete dönüşür: yağmurla topraktan ot çıkar, deliklerden fareler çıkar. Gizli olan, Rabbin bildiği ve dilediğinde açığa çıkardığı şeydir.

Kur'an bu iki sahneyi açıkça kurar. Peygamber'e indirilen hitabın başında şöyle denir: {ar:وَإِن تَجْهَرْ بِٱلْقَوْلِ فَإِنَّهُۥ يَعْلَمُ ٱلسِّرَّ وَأَخْفَى, tr:ve in techer bi'l-kavli fe-innehû ya'lemu's-sirra ve ahfâ, gloss:sözü yüksek sesle söylesen de O gizliyi ve daha gizlisini bilir, source:20:7}. Bu, Musa'nın ateşi gördüğü sahneye geçmeden önceki ayetlerdendir. Aynı hikâyede ateşin başında {ar:إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا, tr:inne's-sâate âtiyetun ekâdu uhfîhâ, gloss:o saat gelecektir; onu neredeyse gizli tutuyorum, source:20:15} denir. Sesin ölçüsü bir emirle verilir: {ar:وَلَا تَجْهَرْ بِصَلَاتِكَ وَلَا تُخَافِتْ بِهَا وَٱبْتَغِ بَيْنَ ذَٰلِكَ سَبِيلًۭا, tr:ve lâ techer bi-salâtike ve lâ tuhâfit bihâ vebteğı beyne ẕâlike sebîlâ, gloss:namazında sesini ne yükselt ne de kıs; ikisinin arasında bir yol tut, source:17:110}. Anmanın sesi de belirlenir: {ar:وَٱذْكُر رَّبَّكَ فِى نَفْسِكَ تَضَرُّعًۭا وَخِيفَةًۭ وَدُونَ ٱلْجَهْرِ مِنَ ٱلْقَوْلِ, tr:veẕkur rabbeke fî nefsike tedarruan ve hîfeten ve dûne'l-cehri mine'l-kavl, gloss:Rabbini içinden yalvararak ve korkarak ve yüksek olmayan bir sesle an, source:7:205}. Duanın sesi de: {ar:ٱدْعُوا۟ رَبَّكُمْ تَضَرُّعًۭا وَخُفْيَةً, tr:ud'û rabbekum tedarruan ve hufye, gloss:Rabbinize yalvararak ve gizlice dua edin, source:7:55}. Allah için {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ مِنَ ٱلْقَوْلِ وَيَعْلَمُ مَا تَكْتُمُونَ, tr:innehû ya'lemu'l-cehra mine'l-kavli ve ya'lemu mâ tektumûn, gloss:O sözün açığını da bilir gizlediğinizi de bilir, source:21:110} ve {ar:يَعْلَمُ سِرَّكُمْ وَجَهْرَكُمْ, tr:ya'lemu sirrakum ve cehrakum, gloss:gizlinizi de açığınızı da bilir, source:6:3} denir. Örtüden çıkarma sahnesini ise Süleyman'a haber getiren hüdhüd anlatır. Hüdhüd bir kavmin güneşe secde ettiğini, şeytanın onları yoldan çevirdiğini söyler ve şöyle ekler: {ar:أَلَّا يَسْجُدُوا۟ لِلَّهِ ٱلَّذِى يُخْرِجُ ٱلْخَبْءَ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَيَعْلَمُ مَا تُخْفُونَ وَمَا تُعْلِنُونَ, tr:ellâ yescudû lillâhi'lleẕî yuhricu'l-hab'e fi's-semâvâti ve'l-ardi ve ya'lemu mâ tuhfûne ve mâ tu'linûn, gloss:göklerde ve yerde saklı olanı çıkaran ve gizlediğinizi de açıkladığınızı da bilen Allah'a secde etmesinler diye, source:27:25}. Bu tek ayette dördüncü ayetteki "çıkarmak" ile yedinci ayetteki gizli ve açık bir arada bulunur.

Kaynaklar: 87:7 ٱلْجَهْرَ ج ه ر B001; 87:7 ٱلْجَهْرَ ج ه ر B011; 87:7 ٱلْجَهْرَ ج ه ر B002; 87:7 ٱلْجَهْرَ ج ه ر B004; 87:7 يَخْفَىٰ خ ف ي B001; 87:7 يَخْفَىٰ خ ف ي B003; 87:7 يَخْفَىٰ خ ف ي B002; 87:15 وَذَكَرَ ذ ك ر B004; 87:6 سَنُقْرِئُكَ ق ر ء B002; 87:7 يَعْلَمُ ع ل م B001; 87:4 أَخْرَجَ خ ر ج B001

## Buluşmalar

İmgelerin çoğu, surenin son ayetinde adı geçen Musa'nın hikâyesinde buluşur. Musa uzakta bir ateş görür ve {ar:أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ecidu ale'n-nâri hudâ, gloss:ateşin başında bir yol gösteren bulurum, source:20:10} umuduyla ona yönelir. Uzaktan görülen ateşin sahnesi ile yol sahnesi burada aynı cümlededir. Ateşin başında önce seçim gelir: {ar:وَأَنَا ٱخْتَرْتُكَ, tr:ve ene'htertuk, gloss:seni ben seçtim, source:20:13}. Sonra namaz ve anma gelir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14}. Sonra gizli olan gelir: {ar:أَكَادُ أُخْفِيهَا, tr:ekâdu uhfîhâ, gloss:onu neredeyse gizli tutuyorum, source:20:15}. Başka bir anlatımda ateşin başında tesbih söylenir: {ar:وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve subhânallâhi rabbi'l-âlemîn, gloss:Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu sahnede surenin on ikinci ve on beşinci ayetleri arasındaki karşıtlık bir kişinin yolculuğunda çözülür. Aynı ateşe yaklaşan biri onun içine sokulmaz. Ateş ona yol, seçilmişlik, namaz ve anma verir. Surede bu iki son iki ayrı kişiye düşer: on ikinci ayetteki kişi ateşe girer, on beşinci ayetteki kişi namaz kılar. Kelimelerin harf benzerliği bu ayrılığı kulakta da duyurur.

İkinci büyük buluşma selin sahnesidir. Gökten inen suyun vadilerde {ar:بِقَدَرِهَا, tr:bi-kaderihâ, gloss:kendi ölçülerince, source:13:17} akması, ölçüp biçme sahnesini çağırır. Selin taşıdığı köpük, otlağın vardığı döküntüdür. İnsanların {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâr, gloss:ateşte üzerine yaktıkları şeyden, source:13:17} çıkan köpük ise ateşin sahnesine girer. Faydalı olanın yerde kalması da öğüdün ve kalıcılığın sahnesidir. Kurumuş otun tencerenin köpüğüyle aynı adı taşıması, bu iki köpüğün Arapçada zaten tek bir kelimede birleştiğini gösterir. Bu ayet surenin beşinci ayetinden on yedinci ayetine uzanan çizgiyi tek bir manzaraya sığdırır. Bir yanda giden döküntü, öbür yanda kalan fayda vardır.

Üçüncü buluşma, Musa'nın karşısındaki sihirbazların sahnesidir. Sihirbazlar secdeye kapanır. Firavun kendi azabının daha çetin ve {ar:وَأَبْقَىٰ, tr:ve ebkâ, gloss:ve daha kalıcı, source:20:71} olduğunu söyler. Sihirbazlar da onu {ar:لَن نُّؤْثِرَكَ, tr:len nu'ŝirak, gloss:seni asla tercih etmeyiz, source:20:72} diye reddeder, yalnızca {ar:هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:hâẕihi'l-hayâte'd-dunyâ, gloss:bu dünya hayatı, source:20:72} üzerinde hüküm verebileceğini söyler ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Sonra suçlu için {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:20:74} der, iman edenler için {ar:ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:ed-derecâtu'l-ulâ, gloss:en yüce dereceler, source:20:75} der, ve hepsini {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76} sözüyle bağlar. Bu birkaç ayette seçim, kalıcı hayat, yükseklik ve yarılan tarlanın kelimeleri birlikte konuşur. Firavun'un "en yüce" iddiası da başka bir anlatımda bu sahneye eklenir. Surenin ikinci yarısı, on üçüncü ayetten on yedinci ayete kadar, neredeyse kelimesi kelimesine Musa'nın hikâyesindeki bir topluluğun ağzından gelmiştir. Son ayetin Musa'nın sayfalarını anması da bu yüzden önem taşır.

Dördüncü buluşma ot ile seçimdir. Dünya hayatının kuruyan ota benzetildiği ayetin hemen ardından kalıcı iyi işlerin daha hayırlı olduğu söylenir. Dünya hayatı başka bir yerde bir {ar:زَهْرَةَ, tr:zehrate, gloss:çiçek, source:20:131} olarak anılır, ve aynı ayet {ar:خَيْرٌۭ وَأَبْقَىٰ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:20:131} diye biter. Otlağın sahnesi seçimin sahnesine bu yolla girer. Beşinci ayetteki ot ile on altıncı ayetteki tercih edilen hayat aynı nesnedir. Kalıcı olan ise ayıklanıp seçilen şeydir. Tarlanın sahnesi bu iki uç arasında bir yol açar. Kalıcı iyilik anlamına gelen kurtuluş kelimesi on dördüncü ayette, toprağı yaran çiftçinin kelimesiyle söylenir. Yabani ot kendi haline kalınca kurur ve selle gider. İşlenen toprağın ürünü ise büyür, hakkı verilir ve geriye kalan bir pay bırakır. Biri dünya tarlası, öbürü ahiret tarlasıdır.

Beşinci buluşma, yaratma fiillerinde zanaat ile bedenin birleşmesidir. İkinci ayetteki ikili hem yontulmuş oku hem de ceninin biçimlenmesini anlatır. Rahimden başlayan ayetin toprağın yağmurla titreşmesiyle bitmesi, beden ile otlağı da birbirine bağlar. Aynı aile, üçüncü ayetteki ölçmeyi pay ölçmeye de taşır, ve on altıncı ayetteki tercih bir pay seçimine döner. Değneği ateşte doğrultmanın fiili on ikinci ayetin fiilidir. Bu fiil aynı ateşin düzelten bir işi ile içine düşenin katlandığı bir işi olduğunu duyurur. Bu son bağ dilin yankısıdır, ayetin sözü değildir.

Bu buluşmalar surenin hareketini taşır. Sure tesbih emriyle ve yükseklikle açılır. Ölçen, yontan ve yol gösteren Rabbin işiyle devam eder. Yağmurun çıkardığı ve selin götürdüğü ot ile sona gelen bir ömür gösterir. Sonra sözün toplanıp unutulmamasına, sunulan öğüde ve öğüt karşısında ikiye ayrılan insanlara geçer. Biri ateşe girer ve ne ölü ne diri kalır. Öbürü arınır, Rabbinin adını anar ve namaz kılar, yani surenin başındaki emri yerine getirir. Ardından seçim gelir: yakın olan öne konmuştur, ama arkadan gelen daha hayırlı ve daha kalıcıdır. Sure, bu sözün ilk sayfalarda, ateşin başında namaz ve anma emrini alan Musa'nın ve Rabbinden kendisini puttan uzak tutmasını isteyen İbrahim'in sayfalarında yazılı olduğunu söyleyerek kapanır.

