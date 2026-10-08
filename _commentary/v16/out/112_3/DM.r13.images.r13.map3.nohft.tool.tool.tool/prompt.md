Focus: 112:3. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/112_3/D.r13/context.md =====
# 112:3 — focus

لَمْ يَلِدْ وَلَمْ يُولَدْ

Anchor translation (canonical reading, reference only):

Doğurmadı ve doğurulmadı.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | لَمْ | لَم |  | NEG |
| 2 | يَلِدْ | وَلَدَ | و ل د | V |
| 3 | وَلَمْ | لَم |  | CONJ;NEG |
| 4 | يُولَدْ | وَلَدَ | و ل د | V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 112 — full text (context; no pericope)

- 112:1 قُلْ هُوَ ٱللَّهُ أَحَدٌ
- 112:2 ٱللَّهُ ٱلصَّمَدُ
- 112:3 ◀ focus لَمْ يَلِدْ وَلَمْ يُولَدْ
- 112:4 وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ


===== _commentary/v16/work/112_3/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## و ل د (root_001683) — identity root of يَلِدْ (w2)

- **B001** ana babadan doğan kişi veya kişiler — birinin çocuğu; bir veya birden çok doğmuş kişi · çocuklar · doğmuş çocuk; yeni doğan · kim olduğunu bilmiyorum · birbirlerinden çocuk sahibi olup çoğaldılar
  أصل صحيح وهو دليل النجل والنسل؛ الولد وهو للواحد والجميع (maqayis)؛ الولد قد يكون واحدا وجمعا؛ الوليد الصبي (sihah)؛ الولد اسم يجمع الواحد والكثير والذكر والأنثى؛ الوليد الصبي حين يولد (tahdhib)؛ الولد المولود؛ الابن والابنة؛ جمع الولد أولاد (mufradat)
- **B002** öz ana baba — öz baba · öz ana · ana baba
  الوالد الأب والوالدة الأم وهما الوالدان (sihah)؛ يقال لأم الرجل هذه والدة (tahdhib)؛ الأب يقال له والد والأم والدة ويقال لهما والدان (mufradat)
- **B003** çocuğu dünyaya getirme — kadın çocuğunu dünyaya getirdi · doğum; çocuğu dünyaya getirme · doğum zamanı geldi · gebe koyun · koyunun doğumunu üstlendik · birbirlerinden çocuk sahibi olup çoğaldılar
  ولدت المرأة تلد ولادا وولادة؛ أولدت حان ولادها (sihah)؛ الولادة فهو وضع الوالدة ولدها؛ شاة والد وهي الحامل؛ ولدناها أي ولينا ولادتها (tahdhib)؛ يوم ولدت؛ يوم ولد (mufradat)
- **B004** yeni doğmuş çocuk veya köle — yeni doğmuş erkek çocuk; erkek köle · kız çocuk; kadın köle
  الوليدة الأنثى والجمع ولائد (maqayis)؛ الوليد الصبي والعبد والجمع ولدان وولدة؛ الوليد الصبية والأمة والجمع الولائد (sihah)؛ الوليد الصبي حين يولد؛ يقال للأمة وليدة وإن كانت مسنة (tahdhib)؛ الوليد يقال لمن قرب عهده بالولادة؛ الوليدة مختصة بالإماء في عامة كلامهم (mufradat)
- **B005** bir şeyden nedenle türeme veya sonradan oluşturulma — bir şeyin başka bir şeyden bir nedenle ortaya çıkması · sonradan oluşturulmuş, uydurulmuş veya katışıksız olmayan · katışıksız sayılmayan dil veya kişi
  تولد الشيء عن الشيء حصل عنه (maqayis)؛ عربية مولدة ورجل مولد إذا كان عربيا غير محض (sihah)؛ المولد من الكلام مولدا إذا استحدثوه؛ كتاب مولد أي مفتعل؛ بينة مولدة وليست بمحققة (tahdhib)؛ تولد الشيء من الشيء حصوله عنه بسبب من الأسباب (mufradat)
- **B006** yaşıt — yaşıt; aynı yaşta olan kimse
  اللدة نقصانه الواو لأن أصله ولدة (maqayis)؛ لدة الرجل تربه؛ وهما لدان والجمع لدات ولدون (sihah)؛ اللدة مختصة بالترب يقال فلان لدة فلان وتربه (mufradat)
- **B007** çok büyük bir durum ya da pek bol bir şey [kalıp] — çok büyük veya ağır bir durum yahut çok bol bir şey için söylenen kalıp söz
  أمر لا ينادى وليده؛ قيل ذلك لكل أمر عظيم ولكل شيء كثير (sihah)؛ هو أمر لا ينادى وليده؛ أمر جليل شديد؛ أصله في الغارة؛ طعام لا ينادى وليده؛ عشب لا ينادى وليده (tahdhib)

===== _commentary/v16/out/s112/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 112:3, and ## Buluşmalar) =====
## Birde duran sayı

Sure aynı kelimeyle açılır ve aynı kelimeyle kapanır. Birinci ayetin sonunda {ar:أَحَدٌ, tr:ehad, gloss:bir, source:112:1} olumlu bir sayı olarak durur; dördüncü ayetin sonunda {ar:أَحَدٌۢ, tr:ehad, gloss:hiç kimse, source:112:4} olumsuzluğun altında yeniden gelir. Bu iki kullanım arasında sure, bir ikincinin ortaya çıkabileceği her yolu tek tek kapatır. Bunu görmek için kelimenin nasıl işlediğine bakmak gerekir. Arapça bu kelimeyi sayının başlangıcı olarak tarif eder: {ar:أحد بمعنى الواحد وهو أول العدد, tr:ehad bi-ma'na'l-vâhid ve hüve evvelü'l-aded, gloss:ehad "bir" anlamındadır, sayının ilkidir, source:"ء ح د,B001"}. Sayı dizisinde bu birin arkasından hemen ikincisi gelir: {ar:أحد واثنان وأحد عشر, tr:ehad ve'snân ve ehad aşer, gloss:bir, iki, on bir, source:"ء ح د,B003"}. Kelime ayrıca bir çiftin üyesini anlatmak için de kullanılır: {ar:أما أحدكما, tr:emmâ ehadükümâ, gloss:ikinizden biri ise, source:"ء ح د,B004"}; burada "bir", iki kişilik bir bütünün parçasıdır. Aynı aile tek başına kalmayı da adlandırır: {ar:استأحد الرجل انفرد, tr:iste'hade'r-racül infarade, gloss:adam yalnız kaldı, tekleşti, source:"ء ح د,B005"}. Kelime nitelemesiz bir sıfat olarak yalnız Allah için kullanılır: {ar:يستعمل مطلقا وصفا في وصف الله تعالى, tr:yüsta'melü mutlakan vasfen fî vasfillâhi teâlâ, gloss:mutlak olarak yalnız Allah'ı niteleyen bir sıfattır, source:"ء ح د,B001"}. Kelimenin ailesinden gelen bir imge, o kelimenin ayetteki anlamının yanında duyulur, onun yerine geçmez. Birinci ayetteki "bir" her şeyden önce Allah'ın birliğini söyler; aile ise bu birin, sayılmaya başlayıp ikiye geçmeyen bir sayı olduğunu ve bir çiftin yarısı olmadığını duyurur.

Üçüncü ayet, bir ikincinin doğabileceği en yakın yolu kapatır. Doğurmak da doğmak da bir çift gerektirir. Arapça anne ile babayı ikil (dual) kalıpta tek bir ad altında toplar: {ar:الوالد الأب والوالدة الأم وهما الوالدان, tr:el-vâlid el-eb ve'l-vâlide el-üm ve hümâ'l-vâlidân, gloss:vâlid baba, vâlide anne; ikisi birlikte vâlidân'dır, source:"و ل د,B002"}. Doğan kişinin de yanında onunla birlikte doğmuş bir yaşıtı olur ve bu da ikil kalıpta söylenir: {ar:لدة الرجل تربه؛ وهما لدان, tr:lidetü'r-racül tirbühû; ve hümâ lidân, gloss:adamın lidesi yaşıtıdır; ikisine lidân denir, source:"و ل د,B006"}. Böylece {ar:لَمْ يَلِدْ وَلَمْ يُولَدْ, tr:lem yelid ve lem yûled, gloss:doğurmadı ve doğurulmadı, source:112:3} sözü, her iki yönde de ikinciyi dışarıda bırakır: doğurmak yeni bir ikinci getirir, doğmak ise önceden var olan bir ikinciyi gerektirir. Dördüncü ayet son yolu kapatır. {ar:كُفُوًا, tr:küfüven, gloss:denk, source:112:4} "benzer" demektir: {ar:الكفء المثل, tr:el-küf' el-misl, gloss:küf', eş ve benzerdir, source:"ك ف ء,B001"}, {ar:كل شيء ساوى شيئا حتى يكون مثله فهو مكافئ له, tr:küllü şey'in sâvâ şey'en hattâ yekûne mislehû fe-hüve mükâfiün leh, gloss:bir şeye eşitlenip onun benzeri olan her şey ona denktir, source:"ك ف ء,B001"}. Denk, birinciyle aynı ölçüye gelen ikincidir. Sonra kelime olumsuzluğun altında geri döner ve o zaman bütün türü kapsar: {ar:أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا, tr:ehad fi'n-nefyi li'stiğrâki cinsi'n-nâtıkîn ve lâ vâhid ve lâ'snân fe-sâiden, gloss:olumsuzlukta ehad konuşan varlıkların bütün türünü kuşatır: ne bir, ne iki, ne daha fazlası, source:"ء ح د,B002"}; tıpkı {ar:ما في الدار أحد, tr:mâ fi'd-dâri ehad, gloss:evde kimse yok, source:"ء ح د,B002"} sözünde olduğu gibi. Halka böyle kapanır: başta olumlu bir, ortada reddedilen çift, sonda içinde hiç kimse bulunmayan bir "hiç kimse".

Kur'an bu sayma işlemini açıkça sahneler. Allah, iki ilah edinmeyi yasaklarken sayıyı iki kez anar: {ar:لَا تَتَّخِذُوٓا۟ إِلَٰهَيْنِ ٱثْنَيْنِ ۖ إِنَّمَا هُوَ إِلَٰهٌۭ وَٰحِدٌۭ, tr:lâ tettehızû ilâheyni'sneyn, innemâ hüve ilâhün vâhid, gloss:iki ilah edinmeyin; O ancak tek bir ilahtır, source:16:51}. "Üç" diyenlere verilen cevapta sayı birin ötesine geçtiği anda reddedilir: {ar:وَمَا مِنْ إِلَٰهٍ إِلَّآ إِلَٰهٌۭ وَٰحِدٌۭ, tr:ve mâ min ilâhin illâ ilâhün vâhid, gloss:tek bir ilahtan başka ilah yoktur, source:5:73}. Allah kendini yaratıcı olarak anlattığı yerde insanlara ve hayvanlara eşler, yani çiftler yarattığını söyler ve hemen ardından kendisini bu düzenin dışına koyar: {ar:لَيْسَ كَمِثْلِهِۦ شَىْءٌۭ, tr:leyse ke-mislihî şey', gloss:O'nun benzeri gibi hiçbir şey yoktur, source:42:11}. Yaratılmışlar çift hâlinde var olur; O'nun bir benzeri yoktur. Peygambere yöneltilen soru da aynı denki arar ve bulamaz: {ar:هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا, tr:hel ta'lemü lehû semiyyâ, gloss:O'nun adaşı, dengi olan birini biliyor musun, source:19:65}. İnsanlara verilen buyruk da aynıdır: {ar:فَلَا تَجْعَلُوا۟ لِلَّهِ أَندَادًۭا, tr:fe-lâ tec'alû lillâhi endâdâ, gloss:Allah'a denkler koşmayın, source:2:22}.

Dördüncü ayetteki olumsuz "hiç kimse" Kur'an'da tekrar tekrar aynı işi görür. Kehf suresinin son ayetinde Peygambere, ilahın tek bir ilah olduğunu söylemesi emredilir ve ayet şu sözle kapanır: {ar:وَلَا يُشْرِكْ بِعِبَادَةِ رَبِّهِۦٓ أَحَدًۢا, tr:ve lâ yüşrik bi-ibâdeti rabbihî ehadâ, gloss:Rabbine kullukta hiç kimseyi ortak koşmasın, source:18:110}. Aynı surede Allah kendi hükmünden söz eder: {ar:وَلَا يُشْرِكُ فِى حُكْمِهِۦٓ أَحَدًۭا, tr:ve lâ yüşrikü fî hukmihî ehadâ, gloss:hükmüne hiç kimseyi ortak etmez, source:18:26}. Cin suresinde mescitlerin Allah'a ait olduğu söylenir: {ar:فَلَا تَدْعُوا۟ مَعَ ٱللَّهِ أَحَدًۭا, tr:fe-lâ ted'û maallâhi ehadâ, gloss:Allah'la birlikte hiç kimseye yalvarmayın, source:72:18}. Peygambere ise şunu söylemesi emredilir: {ar:وَلَآ أُشْرِكُ بِهِۦٓ أَحَدًۭا, tr:ve lâ üşrikü bihî ehadâ, gloss:O'na hiç kimseyi ortak koşmam, source:72:20}. Hemen ardından da şunu söylemesi emredilir: {ar:قُلْ إِنِّى لَن يُجِيرَنِى مِنَ ٱللَّهِ أَحَدٌۭ, tr:kul innî len yücîranî minallâhi ehad, gloss:de ki: beni Allah'a karşı hiç kimse koruyamaz, source:72:22}. Her birinde olumsuz ehad, birin karşısında durabilecek ikinci kişinin yerini boş bırakır.

Kaynaklar: 112:1 أَحَدٌ ء ح د B001; 112:1 أَحَدٌ ء ح د B003; 112:1 أَحَدٌ ء ح د B004; 112:1 أَحَدٌ ء ح د B005; 112:4 أَحَدٌۢ ء ح د B002; 112:3 يَلِدْ و ل د B002; 112:3 يُولَدْ و ل د B006; 112:4 كُفُوًا ك ف ء B001

## Nesil zinciri: denk eş, doğum, yaşıt ve mirasçı

Üçüncü ve dördüncü ayetin kelimeleri bir arada okununca, insan soyunun nasıl sürdüğünü gösteren eksiksiz bir sahne çıkar ortaya. Sahne bir denklikle başlar. Küf', evlilikte ve soyda dengi olan kişidir: {ar:فلان كفء لفلان في المناكحة أو في المحاربة, tr:fülânün küf'ün li-fülânin fi'l-münâkehati ev fi'l-muhârebe, gloss:falan, falanın evlilikte ya da savaşta dengidir, source:"ك ف ء,B001"}, {ar:هذا كفء له أي مثله في الحسب والمال والحرب, tr:hâzâ küf'ün lehû ey misluhû fi'l-hasebi ve'l-mâli ve'l-harb, gloss:bu onun dengidir, yani soyda, malda ve savaşta onun benzeridir, source:"ك ف ء,B001"}. Birbirine denk iki kişi evlenince anne ve baba olurlar; ikil kalıptaki vâlidân {source:"و ل د,B002"}. Sonra kadın doğurur ve doğumun bir vakti vardır: {ar:ولدت المرأة تلد ولادا وولادة؛ أولدت حان ولادها, tr:veledeti'l-mer'etü telidü vilâden ve vilâdeten; evledet hâne vilâdühâ, gloss:kadın doğurdu; doğum vakti geldi, source:"و ل د,B003"}. Doğan çocuk veleddir ve bu kelime erkeği de kızı da, biri de çoğu da kapsar: {ar:الولد اسم يجمع الواحد والكثير والذكر والأنثى, tr:el-veled ismün yecmeu'l-vâhide ve'l-kesîra ve'z-zekera ve'l-ünsâ, gloss:veled teki ve çoğu, erkeği ve dişiyi toplayan bir addır, source:"و ل د,B001"}. Kökün temel anlamı da soyun devam etmesidir: {ar:أصل صحيح وهو دليل النجل والنسل, tr:aslün sahîh ve hüve delîlü'n-necli ve'n-nesl, gloss:sağlam bir köktür; evladı ve nesli gösterir, source:"و ل د,B001"}. Yeni doğan, hayatı doğduğu andan itibaren ölçülen kişidir: {ar:الوليد الصبي حين يولد, tr:el-velîd es-sabiyyü hîne yûled, gloss:velîd, doğduğu andaki çocuktur, source:"و ل د,B004"}. Her doğanın bir de yaşıtlar kuşağı vardır {source:"و ل د,B006"}.

Sahnenin ikinci yarısı zamandır. Dördüncü ayetteki {ar:يَكُن, tr:yekün, gloss:oldu, source:112:4} fiilinin kökü geçmiş zamanı anlatır: {ar:كان عبارة عما مضى من الزمان, tr:kâne ibâretün ammâ medâ mine'z-zamân, gloss:kâne, geçmiş zamanı anlatır, source:"ك و ن,B001"}. Aynı aile yaşlı adamı da bu fiille adlandırır: {ar:يقال للرجل إذا شاخ كُنْتِيّ؛ كأنه نسب إلى قوله كُنْتُ في شبابي كذا وكذا, tr:yükâlü li'r-racüli izâ şâhe küntiyy; ke-ennehû nüsibe ilâ kavlihî küntü fî şebâbî kezâ ve kezâ, gloss:adam yaşlanınca ona küntî denir, sanki "gençliğimde şöyleydim" deyişine nispet edilmiştir, source:"ك و ن,B005"}. Yaşlı adam, sözünü "ben … idim" diye kuran adamdır. Doğan yaşlanır, yaşlanan ölür, onun yerini de doğurduğu alır. Nesil, ölümlü bir türün kendini sürdürme biçimidir. Bu sahneye karşı ikinci ayetteki {ar:ٱلصَّمَدُ, tr:es-samed, gloss:Samed, source:112:2} kelimesinin bir anlamı durur: {ar:الصمد الدائم والدائم الباقي بعد فناء خلقه, tr:es-samed ed-dâim ve'd-dâim el-bâkî ba'de fenâi halkıh, gloss:Samed, daim olandır; daim olan da yarattıkları yok olduktan sonra kalandır, source:"ص م د,B007"}. Aynı tarifin somut imgesi soğukta ve kıtlıkta sütü kesilmeyen dişi devedir: {ar:ناقة مصماد وهي الباقية على القر والجدب الدائمة الرسل, tr:nâkatün mismâd ve hiye'l-bâkıyetü ale'l-karri ve'l-cedbi'd-dâimetü'r-risl, gloss:mismâd deve, soğuğa ve kıtlığa dayanan, sütü sürekli akan devedir, source:"ص م د,B007"}. Böylece üçüncü ayet Allah'ı nesil zincirinin dışına çıkarır: O'nu başlatan bir doğum yoktur, O'ndan sonra kalacak bir mirasçı da yoktur. Dördüncü ayet de zincirin başlangıç noktasını, yani denk eşi kaldırır.

Kur'an bu bağlantıyı açıkça kurar. Allah, cinleri O'na ortak koşan ve {ar:وَخَرَقُوا۟ لَهُۥ بَنِينَ وَبَنَٰتٍۭ بِغَيْرِ عِلْمٍۢ, tr:ve harakû lehû benîne ve benâtin bi-ğayri ilm, gloss:bilgisizce O'na oğullar ve kızlar uydurdular, source:6:100} diye anlatılan kimselere cevap verir: {ar:أَنَّىٰ يَكُونُ لَهُۥ وَلَدٌۭ وَلَمْ تَكُن لَّهُۥ صَٰحِبَةٌۭ, tr:ennâ yekûnü lehû veledün ve lem tekün lehû sâhibeh, gloss:O'nun eşi olmamışken nasıl çocuğu olur, source:6:101}. Buradaki "lem tekün lehû sâhibe", surenin dördüncü ayetindeki "lem yekün lehû küfüven" ile aynı kalıptadır: eş olmayınca çocuk da olmaz. Kur'an'ı dinleyen cinler de eşi ve çocuğu birlikte reddeder: {ar:مَا ٱتَّخَذَ صَٰحِبَةًۭ وَلَا وَلَدًۭا, tr:mettehaze sâhibeten ve lâ veledâ, gloss:ne eş edindi ne çocuk, source:72:3}. Saffât suresinde Allah, Peygambere Mekkelilere kızları O'na, oğulları kendilerine nasıl ayırdıklarını sormasını emreder {source:37:149}, ve iddia bir soy iddiası olarak adlandırılır: {ar:وَجَعَلُوا۟ بَيْنَهُۥ وَبَيْنَ ٱلْجِنَّةِ نَسَبًۭا, tr:ve cealû beynehû ve beyne'l-cinneti nesebâ, gloss:O'nunla cinler arasında bir soy bağı kurdular, source:37:158}. İnsan sahnesi ise bir yeminde topluca anılır: {ar:وَوَالِدٍۢ وَمَا وَلَدَ, tr:ve vâlidin ve mâ veled, gloss:doğurana ve doğurduğuna andolsun, source:90:3}. Surenin iki fiilinin iki yönü, yani doğuran ve doğurulan, insanlara yapılan bir uyarıda yan yana durur: {ar:لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ وَلَا مَوْلُودٌ هُوَ جَازٍ عَن وَالِدِهِۦ شَيْـًٔا, tr:lâ yeczî vâlidün an veledihî ve lâ mevlûdün hüve câzin an vâlidihî şey'â, gloss:babanın çocuğuna, çocuğun da babasına hiçbir fayda sağlayamayacağı gün, source:31:33}. İnsanlar arasındaki en güçlü bağ olan bu çift, o gün hiçbir şeyi taşıyamaz.

Doğumun ardından ölümün geldiğini Kur'an, sonradan "oğul" diye anılacak olanın ağzından da söyletir. Allah Yahya için {ar:يَوْمَ وُلِدَ وَيَوْمَ يَمُوتُ وَيَوْمَ يُبْعَثُ حَيًّۭا, tr:yevme vülide ve yevme yemûtü ve yevme yüb'asü hayyâ, gloss:doğduğu gün, öleceği gün ve diri olarak kaldırılacağı gün, source:19:15} der. Beşikteki İsa da kendisi için aynı sırayı söyler: {ar:يَوْمَ وُلِدتُّ وَيَوْمَ أَمُوتُ, tr:yevme vülidtü ve yevme emût, gloss:doğduğum gün ve öleceğim gün, source:19:33}. Mirasçıya neden ihtiyaç duyulduğunu ise Zekeriya'nın duası gösterir. Yaşlanmış, karısı kısır bir adam Rabbine yalvarır: {ar:وَهَنَ ٱلْعَظْمُ مِنِّى وَٱشْتَعَلَ ٱلرَّأْسُ شَيْبًۭا, tr:vehene'l-azmu minnî ve'şteale'r-re'sü şeybâ, gloss:kemiğim zayıfladı, başım ağarmış saçla tutuştu, source:19:4}. Kendisinden sonra yakınlarının ne yapacağından korkar ve bir veli ister {source:19:5}. O veli de {ar:يَرِثُنِى, tr:yerisünî, gloss:bana mirasçı olsun, source:19:6}. Başka bir surede aynı dua şöyle geçer: {ar:رَبِّ لَا تَذَرْنِى فَرْدًۭا وَأَنتَ خَيْرُ ٱلْوَٰرِثِينَ, tr:rabbi lâ tezernî ferden ve ente hayru'l-vârisîn, gloss:Rabbim beni tek başıma bırakma; sen mirasçıların en hayırlısısın, source:21:89}. Ölümlü insan yalnız kalmaktan korkar ve çocuk ister; seslendiği Rab ise mirasçıya ihtiyacı olmayan, bizzat kendisi mirasçı olandır: {ar:إِنَّا نَحْنُ نَرِثُ ٱلْأَرْضَ وَمَنْ عَلَيْهَا, tr:innâ nahnü nerisü'l-arda ve men aleyhâ, gloss:yeryüzüne ve üzerindekilere biz vâris oluruz, source:19:40}. İnsan ömrünün bütün eğrisi tek bir ayette anlatılır: {ar:خَلَقَكُم مِّن ضَعْفٍۢ ثُمَّ جَعَلَ مِنۢ بَعْدِ ضَعْفٍۢ قُوَّةًۭ ثُمَّ جَعَلَ مِنۢ بَعْدِ قُوَّةٍۢ ضَعْفًۭا وَشَيْبَةًۭ, tr:halakaküm min da'fin sümme ceale min ba'di da'fin kuvvaten sümme ceale min ba'di kuvvetin da'fen ve şeybeh, gloss:sizi zayıflıktan yarattı, sonra zayıflığın ardından güç verdi, sonra gücün ardından zayıflık ve yaşlılık verdi, source:30:54}. Nesillerin birbirinin yerine geçmesi de Allah'ın elindedir: {ar:إِن يَشَأْ يُذْهِبْكُمْ وَيَسْتَخْلِفْ مِنۢ بَعْدِكُم مَّا يَشَآءُ كَمَآ أَنشَأَكُم مِّن ذُرِّيَّةِ قَوْمٍ ءَاخَرِينَ, tr:in yeşe' yüzhibküm ve yestahlif min ba'diküm mâ yeşâü kemâ enşeeküm min zürriyyeti kavmin âharîn, gloss:dilerse sizi götürür, sizi başka bir kavmin soyundan var ettiği gibi ardınızdan dilediğini yerinize getirir, source:6:133}. Samed'in "yarattıkları yok olduktan sonra kalan" anlamı da Kur'an'daki karşılığını bulur: {ar:كُلُّ مَنْ عَلَيْهَا فَانٍۢ, tr:küllü men aleyhâ fân, gloss:yeryüzündeki herkes yok olucudur, source:55:26}, {ar:وَيَبْقَىٰ وَجْهُ رَبِّكَ, tr:ve yebkâ vechü rabbik, gloss:Rabbinin yüzü kalır, source:55:27}. Nesil zinciri, ölümün kaçınılmaz olduğu yerde işler; Samed ise bu zincirin dışında kalandır.

Kaynaklar: 112:4 كُفُوًا ك ف ء B001; 112:3 يَلِدْ و ل د B002; 112:3 يَلِدْ و ل د B003; 112:3 يُولَدْ و ل د B001; 112:3 يُولَدْ و ل د B004; 112:3 يُولَدْ و ل د B006; 112:4 يَكُن ك و ن B001; 112:4 يَكُن ك و ن B005; 112:2 ٱلصَّمَدُ ص م د B007

## İçi boş olmayan dolu beden

Samed'in en somut anlamı fiziksel bir niteliktir. Samed, baştan sona dolu olan, içinde boşluk bulunmayan şeydir: {ar:المصمت الذي ليس بأجوف والصمدة صخرة راسية, tr:el-musmet ellezî leyse bi-ecvef ve's-samdetü sahratün râsiyeh, gloss:içi boş olmayan dolu şey; samde, yere sağlamca oturmuş kayadır, source:"ص م د,B002"}. Aynı aile yarığı olmayan sert toprağı da adlandırır: {ar:المصمد الصلب الذي ليس فيه خدد والشديد من الأرض, tr:el-musmed es-sulb ellezî leyse fîhi hudad ve'ş-şedîdü mine'l-ard, gloss:musmed, içinde yarık bulunmayan sert şey ve toprağın sert olanıdır, source:"ص م د,B002"}. Kökte bir şişenin ağzını kapatan tıpa da vardır: {ar:الصماد عفاص القارورة وصمدتها صمدا, tr:es-simâd ifâsu'l-kârûre ve samedtühâ samden, gloss:simâd şişenin tıpasıdır; onu tıpaladım, source:"ص م د,B003"}. Tıpalı şişenin ağzından ne bir şey girer ne bir şey çıkar.

Üçüncü ayet hemen bu kelimenin arkasından gelir ve çıkışın iki yönünü sayar: O'ndan bir şey çıkmaz ({ar:لَمْ يَلِدْ, tr:lem yelid, gloss:doğurmadı, source:112:3}), O da bir şeyden çıkmamıştır ({ar:وَلَمْ يُولَدْ, tr:ve lem yûled, gloss:ve doğurulmadı, source:112:3}). Doğum, içinde bir şey taşıyan bir bedenin bu taşıdığını dışarı bırakmasıdır: {ar:الولادة فهو وضع الوالدة ولدها؛ شاة والد وهي الحامل, tr:el-vilâde fe-hüve vad'u'l-vâlideti veledehâ; şâtün vâlid ve hiye'l-hâmil, gloss:doğum, annenin çocuğunu bırakmasıdır; gebe koyuna şâtün vâlid denir, source:"و ل د,B003"}. Aynı kökten gelen tevellüd, bir şeyin başka bir şeyden çıkıp oluşmasıdır: {ar:تولد الشيء عن الشيء حصل عنه, tr:tevelleda'ş-şey'ü ani'ş-şey' hasale anh, gloss:bir şey öbüründen doğdu, ondan meydana geldi, source:"و ل د,B005"}. Dördüncü ayetteki denk kelimesinin kökü ise içi boş kabın bir başka işleyişini anlatır: {ar:كفأت الإناء إذا كببته, tr:kefe'tü'l-inâe izâ kebebtühû, gloss:kabı ters çevirip boşalttım, source:"ك ف ء,B002"}. Böylece sahne fiziksel terimlerle işler. İçi boş bir beden bir şey taşır ve taşıdığını dışarı bırakabilir: ya doğurur ya da devrilip boşalır. Dolu bir bedenin ise verecek bir içi de, içinden çıktığı bir başka iç de yoktur. İkinci ayetin "Samed" sözünden sonra üçüncü ayetin "doğurmadı ve doğurulmadı" sözünün gelmesi, bu imgeyi ardı ardına okutur. Sade bir açıklama "Allah'ın çocuğu yoktur" der ve orada kalır. İmge ise bu yokluğun nedenini gösterir: doğurmak bir iç gerektirir, Samed'in içi yoktur.

Kur'an içinde bir şey taşıyan bedeni ve onun taşıdığını bırakmasını sahneler. İmran'ın karısı hamileyken taşıdığı çocuğu Rabbine adar ve onu {ar:مَا فِى بَطْنِى, tr:mâ fî batnî, gloss:karnımdaki, source:3:35} diye anar. Doğumdan sonra da şöyle der: {ar:فَلَمَّا وَضَعَتْهَا قَالَتْ رَبِّ إِنِّى وَضَعْتُهَآ أُنثَىٰ, tr:fe-lemmâ vadaathâ kâlet rabbi innî vada'tühâ ünsâ, gloss:onu doğurunca "Rabbim, onu kız doğurdum" dedi, source:3:36}. Burada kullanılan "vad'" fiili, doğumun tarifindeki fiilin ta kendisidir. İnsana anne babası hakkında verilen öğütte de aynı işlem iki adımda anlatılır: {ar:حَمَلَتْهُ أُمُّهُۥ كُرْهًۭا وَوَضَعَتْهُ كُرْهًۭا, tr:hamelethü ümmühû kurhen ve vadaathü kurhâ, gloss:annesi onu zahmetle taşıdı ve zahmetle doğurdu, source:46:15}. İnsan bedeninin bir içi olduğunu Kur'an başka bir yerde açıkça söyler: {ar:مَّا جَعَلَ ٱللَّهُ لِرَجُلٍۢ مِّن قَلْبَيْنِ فِى جَوْفِهِۦ, tr:mâ cealallâhü li-racülin min kalbeyni fî cevfih, gloss:Allah bir adamın içinde iki kalp yaratmadı, source:33:4}. "Cevf", Samed'in tarifinde yokluğu söylenen boşluğun kökünden gelir.

İçi olan bir beden yalnızca dışarı vermez, dışarıdan da alır. Allah, Mesih'in ilahlığı iddiasına cevap verirken anneyi ve oğlu birlikte anar: {ar:كَانَا يَأْكُلَانِ ٱلطَّعَامَ, tr:kânâ ye'külâni't-taâm, gloss:ikisi de yemek yerlerdi, source:5:75}. Bir doğuran ile bir doğurulan, yani üçüncü ayetin iki yönü, burada yemek yiyen iki beden olarak ilahlığın karşısına konur. Elçiler hakkında da şöyle denir: {ar:وَمَا جَعَلْنَٰهُمْ جَسَدًۭا لَّا يَأْكُلُونَ ٱلطَّعَامَ وَمَا كَانُوا۟ خَٰلِدِينَ, tr:ve mâ cealnâhüm ceseden lâ ye'külûne't-taâme ve mâ kânû hâlidîn, gloss:onları yemek yemeyen bedenler kılmadık; ölümsüz de değillerdi, source:21:8}. Allah ise bunun tam tersiyle anlatılır: {ar:وَهُوَ يُطْعِمُ وَلَا يُطْعَمُ, tr:ve hüve yut'imü ve lâ yut'am, gloss:O doyurur, kendisi doyurulmaz, source:6:14}. Cinleri ve insanları niçin yarattığını anlattığı yerde de şöyle der: {ar:وَمَآ أُرِيدُ أَن يُطْعِمُونِ, tr:ve mâ ürîdü en yut'imûn, gloss:beni doyurmalarını istemem, source:51:57}. Ne bir şey girer ne bir şey çıkar.

Kaynaklar: 112:2 ٱلصَّمَدُ ص م د B002; 112:2 ٱلصَّمَدُ ص م د B003; 112:3 يَلِدْ و ل د B003; 112:3 يَلِدْ و ل د B005; 112:4 كُفُوًا ك ف ء B002

## Sözle var olmak, doğumla değil

Surenin fiilleri üç kökten gelir: kavl (söz), vilâde (doğum) ve kevn (olmak). Kur'an, şeylerin nasıl var olduğunu anlatan formülünde tam olarak bu üç kökten ikisini kullanır ve üçüncüsünü bu formülün karşısına koyar. Burada söz konusu olan bir aile imgesi değildir; Kur'an pasajlarında aynı köklerin yan yana gelmesidir. Formül şudur: Allah bir işe hükmedince {ar:فَإِنَّمَا يَقُولُ لَهُۥ كُن فَيَكُونُ, tr:fe-innemâ yekûlü lehû kün fe-yekûn, gloss:ona yalnızca "ol" der, o da olur, source:2:117}. Kevn kökü bu işlemi kendi tanımında taşır: {ar:كونه فتكون أحدثه فحدث, tr:kevvenehû fe-tekevvene ahdesehû fe-hadese, gloss:onu var etti, o da var oldu; meydana getirdi, o da meydana geldi, source:"ك و ن,B001"}. Söz, harflerden oluşup dile getirilerek ortaya çıkandır: {ar:المركب من الحروف المبرز بالنطق, tr:el-mürekkeb mine'l-hurûf el-mübraz bi'n-nutk, gloss:harflerden oluşan ve dile getirilerek ortaya çıkarılan, source:"ق و ل,B001"}. Doğum kökü ise bir şeyin var olmasının öbür yolunu adlandırır: tevellüd, bir şeyin başka bir şeyden çıkarak meydana gelmesidir {source:"و ل د,B005"}, ve doğum bir bedenin eylemidir {source:"و ل د,B003"}.

Kur'an bu iki yolu açıkça birbirinin karşısına koyar. Bakara suresinde Allah, O'nun bir çocuk edindiğini söyleyenlere cevap verir: {ar:وَقَالُوا۟ ٱتَّخَذَ ٱللَّهُ وَلَدًۭا ۗ سُبْحَٰنَهُۥ, tr:ve kâlü'ttehazallâhü veleden sübhâneh, gloss:Allah çocuk edindi dediler; O bundan münezzehtir, source:2:116}. Bir sonraki ayette, O'nun gökleri ve yeri yoktan var eden olduğu söylenir ve yukarıdaki formül gelir {source:2:117}. Söz, kavl kökünden; çocuk, veled kökünden; formül de kevn kökündendir. Çocuğun yerine söz konmuştur. Meryem suresinde İsa'nın doğumu anlatıldıktan sonra Allah aynı şeyi söyler: {ar:مَا كَانَ لِلَّهِ أَن يَتَّخِذَ مِن وَلَدٍۢ ۖ سُبْحَٰنَهُۥٓ, tr:mâ kâne lillâhi en yettehıze min veled, sübhâneh, gloss:Allah'ın çocuk edinmesi olacak şey değildir; O münezzehtir, source:19:35}. Aynı ayet de formülle devam eder {source:19:35}. Meryem'in kendisi de soruyu tam bu kelimelerle sorar: {ar:رَبِّ أَنَّىٰ يَكُونُ لِى وَلَدٌۭ وَلَمْ يَمْسَسْنِى بَشَرٌۭ, tr:rabbi ennâ yekûnü lî veledün ve lem yemsesnî beşer, gloss:Rabbim, bana hiçbir insan dokunmamışken benim nasıl çocuğum olur, source:3:47}. Aldığı cevap, aynı ayette yine formüldür {source:3:47}. Babasız bir doğum sözden gelir. İsa ile Âdem'in karşılaştırıldığı yerde de aynı şey söylenir: {ar:خَلَقَهُۥ مِن تُرَابٍۢ ثُمَّ قَالَ لَهُۥ كُن فَيَكُونُ, tr:halakahû min türâbin sümme kâle lehû kün fe-yekûn, gloss:onu topraktan yarattı, sonra ona "ol" dedi, o da oldu, source:3:59}. Kitap ehline hitap eden ayette İsa'nın kendisi bir söz olarak adlandırılır: {ar:وَكَلِمَتُهُۥٓ أَلْقَىٰهَآ إِلَىٰ مَرْيَمَ, tr:ve kelimetühû elkâhâ ilâ meryem, gloss:Meryem'e ulaştırdığı sözü, source:4:171}; aynı ayette {ar:سُبْحَٰنَهُۥٓ أَن يَكُونَ لَهُۥ وَلَدٌۭ, tr:sübhânehû en yekûne lehû veled, gloss:O, bir çocuğu olmaktan münezzehtir, source:4:171} denir. En’âm suresinde de her şeyi yaratmış olmak, çocuk sahibi olmanın karşısına konur: {ar:وَخَلَقَ كُلَّ شَىْءٍۢ, tr:ve halaka külle şey', gloss:ve her şeyi O yarattı, source:6:101}. Bir başka ayet de bu karşıtlığı mantıksal sonucuna götürür: {ar:لَّوْ أَرَادَ ٱللَّهُ أَن يَتَّخِذَ وَلَدًۭا لَّٱصْطَفَىٰ مِمَّا يَخْلُقُ مَا يَشَآءُ, tr:lev erâdallâhü en yettehıze veleden la'stafâ mimmâ yahluku mâ yeşâ', gloss:Allah çocuk edinmek isteseydi, yarattıklarından dilediğini seçerdi, source:39:4}. O'nun edinebileceği her şey zaten yarattıklarındandır.

Bu ışıkta okununca sure bir sözle açılır (kul), doğum yoluyla var olmayı iki yönde birden reddeder ve olumsuzlanmış kevn ile kapanır: {ar:وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ, tr:ve lem yekün lehû küfüven ehad, gloss:hiçbir şey O'na denk olmadı, source:112:4}. Surenin "kul" sözü Allah'ın Peygambere verdiği bir emirdir, yaratıcı söz değildir; bu bağ surenin kendi cümlesinde değil, köklerin Kur'an'daki buluşmasında kurulur. Bağın gösterdiği şudur: şeyler O'ndan doğarak değil, O'nun sözüyle var olur ve var olmuş hiçbir şey O'na denk olmamıştır.

Kaynaklar: 112:1 قُلْ ق و ل B001; 112:3 يَلِدْ و ل د B005; 112:3 يَلِدْ و ل د B003; 112:4 يَكُن ك و ن B001

## Emredilen söz ve uydurulan söz

Sure bir emirle açılır: {ar:قُلْ, tr:kul, gloss:de, source:112:1}. Söz, dil aracılığıyla dışarı çıkarılan şeydir; kökte dilin kendisi de bu adı taşır: {ar:المقول اللسان, tr:el-mikvel el-lisân, gloss:mikvel, dildir, source:"ق و ل,B002"}. "Söylemek" fiili bir görüşü benimseyip onu savunmak için de kullanılır {source:"ق و ل,B013"}. Bu yüzden emredilen söz, kişinin arkasında durduğu bir inançtır. Aynı kökün bir de sahte karşılığı vardır: tekavvül, olmamış bir şeyi söylemek ve onu birine yakıştırmaktır: {ar:تقول باطلا أي قال ما لم يكن, tr:tekavvele bâtılen ey kâle mâ lem yekün, gloss:bâtıl söz uydurdu, yani olmamış olanı söyledi, source:"ق و ل,B005"}, {ar:تقول عليه أي كذب عليه, tr:tekavvele aleyhi ey kezebe aleyh, gloss:onun adına söz uydurdu, yani ona yalan isnat etti, source:"ق و ل,B005"}. "Mâ lem yekün", yani "olmamış olan", dördüncü ayetin fiilini taşır. Kökte insanlar arasında yayılan söz de vardır: {ar:القالة القول الفاشي في الناس, tr:el-kâle el-kavlü'l-fâşî fi'n-nâs, gloss:kâle, insanlar arasında yayılan sözdür, source:"ق و ل,B007"}. Surenin doğum fiillerinin kökü ise uydurulmuş sözü kendi adıyla anar: {ar:كتاب مولد أي مفتعل؛ بينة مولدة وليست بمحققة, tr:kitâbün müvelled ey müfteal; beyyinetün müvelledetün ve leyset bi-muhakkaka, gloss:müvelled kitap uydurma kitaptır; müvelled delil, doğrulanmamış delildir, source:"و ل د,B005"}. Böylece sahne bir sözler yarışmasıdır. Allah'ın çocuğu olduğuna dair bir söz insanlar arasında dolaşmaktadır; bu söz O'na isnat edilmiş, uydurulmuş bir sözdür. Peygambere de doğru sözü karşılık olarak söylemesi emredilir. Arapçada uydurulmuş söz için kullanılan kelime de "doğurulmuş" anlamına gelen kökten türemiştir.

Kur'an bu yarışmayı birçok yerde sahneler. Kehf suresinin başında Allah, O'nun çocuk edindiğini söyleyenleri uyarır: {ar:كَبُرَتْ كَلِمَةًۭ تَخْرُجُ مِنْ أَفْوَٰهِهِمْ ۚ إِن يَقُولُونَ إِلَّا كَذِبًۭا, tr:keburet kelimeten tahrucü min efvâhihim, in yekûlûne illâ kezibâ, gloss:ağızlarından çıkan söz ne büyük bir sözdür; yalandan başka bir şey söylemiyorlar, source:18:5}. Söz ağızdan dışarı çıkar ve yalandır. Saffât suresinde, Mekkelilerin kızları Allah'a ayırması anlatıldıktan sonra söz, doğum ve yalan iki ayette bir araya gelir: {ar:أَلَآ إِنَّهُم مِّنْ إِفْكِهِمْ لَيَقُولُونَ, tr:elâ innehüm min ifkihim le-yekûlûn, gloss:dikkat edin, onlar uydurmalarından ötürü söylüyorlar, source:37:151}, {ar:وَلَدَ ٱللَّهُ وَإِنَّهُمْ لَكَٰذِبُونَ, tr:velede'llâhü ve innehüm le-kâzibûn, gloss:"Allah doğurdu" diyorlar; onlar elbette yalancıdır, source:37:152}. Yûnus suresinde iddiaya verilen cevap, Allah'ın hiçbir şeye ihtiyacı olmadığını söyler ve sözle biter: {ar:أَتَقُولُونَ عَلَى ٱللَّهِ مَا لَا تَعْلَمُونَ, tr:e-tekûlûne alallâhi mâ lâ ta'lemûn, gloss:Allah hakkında bilmediğiniz şeyi mi söylüyorsunuz, source:10:68}. Tevbe suresinde Allah, Yahudilerin ve Hristiyanların sözünü aktarır ve onu kendisinden önceki sözlerin bir kopyası olarak gösterir: {ar:ذَٰلِكَ قَوْلُهُم بِأَفْوَٰهِهِمْ ۖ يُضَٰهِـُٔونَ قَوْلَ ٱلَّذِينَ كَفَرُوا۟ مِن قَبْلُ, tr:zâlike kavlühüm bi-efvâhihim, yudâhiûne kavle'llezîne keferû min kabl, gloss:bu, ağızlarıyla söyledikleri sözdür; daha önce inkâr edenlerin sözüne benzetiyorlar, source:9:30}. Elden ele dolaşan söz budur. Allah'a kızlar isnat edenlere de şöyle denir: {ar:إِنَّكُمْ لَتَقُولُونَ قَوْلًا عَظِيمًۭا, tr:inneküm le-tekûlûne kavlen azîmâ, gloss:siz gerçekten çok büyük bir söz söylüyorsunuz, source:17:40}. Meryem suresinde sözün ağırlığı evrene yansır. İddia önce aktarılır: {ar:وَقَالُوا۟ ٱتَّخَذَ ٱلرَّحْمَٰنُ وَلَدًۭا, tr:ve kâlü'ttehaze'r-rahmânü veledâ, gloss:Rahman çocuk edindi dediler, source:19:88}. Ardından {ar:لَّقَدْ جِئْتُمْ شَيْـًٔا إِدًّۭا, tr:lekad ci'tüm şey'en iddâ, gloss:çok çirkin bir şey ortaya attınız, source:19:89} denir ve gökler bu sözden ötürü neredeyse yarılacak hâle gelir {source:19:90}, {ar:أَن دَعَوْا۟ لِلرَّحْمَٰنِ وَلَدًۭا, tr:en deav li'r-rahmâni veledâ, gloss:Rahman'a çocuk isnat ettikleri için, source:19:91}. Cinler de, eşi ve çocuğu reddettikten hemen sonra kendi içlerindeki beyinsizin sözünü anarlar: {ar:وَأَنَّهُۥ كَانَ يَقُولُ سَفِيهُنَا عَلَى ٱللَّهِ شَطَطًۭا, tr:ve ennehû kâne yekûlü sefîhunâ alallâhi şatatâ, gloss:bizim beyinsizimiz Allah hakkında saçma sözler söylüyordu, source:72:4}.

Sözle kurulan sahte akrabalık sahnesi Kur'an'da insan ilişkileri üzerinden de gösterilir ve bu sahnede doğum, sözün karşısında gerçeğin ölçüsü olarak durur. Karısına "sen bana annem gibisin" diyerek ondan uzaklaşanlar için şöyle denir: {ar:إِنْ أُمَّهَٰتُهُمْ إِلَّا ٱلَّٰٓـِٔى وَلَدْنَهُمْ ۚ وَإِنَّهُمْ لَيَقُولُونَ مُنكَرًۭا مِّنَ ٱلْقَوْلِ وَزُورًۭا, tr:in ümmehâtühüm ille'llâî velednehüm, ve innehüm le-yekûlûne münkeran mine'l-kavli ve zûrâ, gloss:anneleri ancak onları doğuranlardır; onlar gerçekten çirkin ve yalan bir söz söylüyorlar, source:58:2}. Evlatlıklar hakkında da şöyle denir: {ar:ذَٰلِكُمْ قَوْلُكُم بِأَفْوَٰهِكُمْ ۖ وَٱللَّهُ يَقُولُ ٱلْحَقَّ, tr:zâliküm kavlüküm bi-efvâhiküm, vallâhü yekûlü'l-hakk, gloss:bu sizin ağzınızla söylediğiniz sözdür; Allah ise doğruyu söyler, source:33:4}. Söz bir akrabalık iddia eder, gerçek ise ona uymaz. Sözün yanlışlıkla birine isnat edilmesi de sahnelenir. Kıyamet günü Allah İsa'ya, insanlara kendisini ve annesini iki ilah edinmelerini söyleyip söylemediğini sorar; İsa şöyle cevap verir: {ar:مَا يَكُونُ لِىٓ أَنْ أَقُولَ مَا لَيْسَ لِى بِحَقٍّ, tr:mâ yekûnü lî en ekûle mâ leyse lî bi-hakk, gloss:hakkım olmayan bir şeyi söylemem bana yakışmaz, source:5:116}. Tekavvül fiilinin kendisi de Peygamber hakkında söylenen bir sözde geçer: {ar:وَلَوْ تَقَوَّلَ عَلَيْنَا بَعْضَ ٱلْأَقَاوِيلِ, tr:ve lev tekavvele aleynâ ba'da'l-ekâvîl, gloss:eğer bize karşı bazı sözler uydurmuş olsaydı, source:69:44}. Birkaç ayet sonra olumsuz ehad da gelir: {ar:فَمَا مِنكُم مِّنْ أَحَدٍ عَنْهُ حَٰجِزِينَ, tr:fe-mâ minküm min ehadin anhü hâcizîn, gloss:hiçbiriniz buna engel olamazdınız, source:69:47}. Uydurulmuş söze karşı emredilen söz de Peygamberin ağzından çıkar: {ar:قُلْ إِن كَانَ لِلرَّحْمَٰنِ وَلَدٌۭ فَأَنَا۠ أَوَّلُ ٱلْعَٰبِدِينَ, tr:kul in kâne li'r-rahmâni veledün fe-ene evvelü'l-âbidîn, gloss:de ki: Rahman'ın bir çocuğu olsaydı, ona ilk kulluk eden ben olurdum, source:43:81}. Bir başka yerde de emredilen söz şudur: {ar:قُلْ إِنَّمَا هُوَ إِلَٰهٌۭ وَٰحِدٌۭ, tr:kul innemâ hüve ilâhün vâhid, gloss:de ki: O ancak tek bir ilahtır, source:6:19}. Meryem suresi, İsa'nın kendi sözlerinden sonra onu doğru söz olarak adlandırır: {ar:ذَٰلِكَ عِيسَى ٱبْنُ مَرْيَمَ ۚ قَوْلَ ٱلْحَقِّ ٱلَّذِى فِيهِ يَمْتَرُونَ, tr:zâlike îse'bnü meryem, kavle'l-hakkı'llezî fîhi yemterûn, gloss:işte Meryem oğlu İsa; hakkında şüpheye düştükleri doğru söz budur, source:19:34}. Surenin "kul" emri bu sahnede yerini bulur: dolaşan sözün karşısına söylenecek söz, ikinci, üçüncü ve dördüncü ayettir.

Kaynaklar: 112:1 قُلْ ق و ل B001; 112:1 قُلْ ق و ل B002; 112:1 قُلْ ق و ل B013; 112:1 قُلْ ق و ل B005; 112:1 قُلْ ق و ل B007; 112:3 يَلِدْ و ل د B005

## Buluşmalar

Birde duran sayı ile içi boş olmayan dolu beden aynı işlemin iki yüzüdür. İçi olan bir beden ikinci bir varlık doğurur; doğum bir şeyden başka bir şeyin çıkması, yani birin ikiye bölünmesidir. Samed'in dolu oluşu ile ehad'in ikiye geçmeyişi, üçüncü ayette tek bir cümleye dönüşür: içinden bir şey çıkmayan, ikincisi de olmayandır. En’âm suresindeki ayet bu iki imgeyi ve nesil zincirini bir arada tutar: {ar:أَنَّىٰ يَكُونُ لَهُۥ وَلَدٌۭ وَلَمْ تَكُن لَّهُۥ صَٰحِبَةٌۭ, tr:ennâ yekûnü lehû veledün ve lem tekün lehû sâhibeh, gloss:O'nun eşi olmamışken nasıl çocuğu olur, source:6:101}. Eş bir ikincidir, çocuk bir başka ikincidir; ikisi de olmayınca sayı birde kalır. Yaratılmışların çift hâlinde var olması ile O'nun benzerinin olmaması da Şûrâ suresinde aynı ayette durur {source:42:11}.

Samed kelimesinin iki anlamı, yani içi boş olmayan dolu beden ve yarattıkları yok olduktan sonra kalan daim varlık, üçüncü ayette birlikte karşılık bulur: O'nda doğuracak bir iç yoktur ve ölen bir zincirde yeri yoktur. Enbiyâ suresinde elçiler hakkında söylenen söz bu iki imgeyi tek bir sahnede birleştirir: {ar:وَمَا جَعَلْنَٰهُمْ جَسَدًۭا لَّا يَأْكُلُونَ ٱلطَّعَامَ وَمَا كَانُوا۟ خَٰلِدِينَ, tr:ve mâ cealnâhüm ceseden lâ ye'külûne't-taâme ve mâ kânû hâlidîn, gloss:onları yemek yemeyen bedenler kılmadık; ölümsüz de değillerdi, source:21:8}. Yemek yiyen beden, yani içi olan beden, ölen bedendir. Mesih ile annesinin birlikte yemek yediğini söyleyen ayet de {source:5:75} doğuran ile doğurulanı içi olan iki beden olarak gösterir.

Kapısına gidilen efendi ile nesil zinciri, Meryem suresinde birbirine bağlanır. Çocuk olduğu iddia edilenler kapıya gelen kullardır: {ar:إِن كُلُّ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ إِلَّآ ءَاتِى ٱلرَّحْمَٰنِ عَبْدًۭا, tr:in küllü men fi's-semâvâti ve'l-ardı illâ âti'r-rahmâni abdâ, gloss:göklerde ve yerde olan herkes Rahman'a ancak kul olarak gelecektir, source:19:93}. Hemen önceki ayette {ar:وَمَا يَنۢبَغِى لِلرَّحْمَٰنِ أَن يَتَّخِذَ وَلَدًا, tr:ve mâ yenbeğî li'r-rahmâni en yettehıze veledâ, gloss:çocuk edinmek Rahman'a yakışmaz, source:19:92} denmiştir. Aynı iddiaya bir başka yerde verilen cevap da aynıdır: {ar:بَلْ عِبَادٌۭ مُّكْرَمُونَ, tr:bel ibâdün mükramûn, gloss:hayır, onlar ikram edilmiş kullardır, source:21:26}. Mesih'in kendisi de beşikte ilk sözünü bu yönde söyler: {ar:إِنِّى عَبْدُ ٱللَّهِ, tr:innî abdullâh, gloss:ben Allah'ın kuluyum, source:19:30}. Zincirde çocuk yerine konmak istenen, efendinin kapısındaki kuldur.

Efendi imgesi ile birde duran sayı, zirvedeki denkte buluşur. Soyda, malda ve savaşta denk olan kişinin yokluğunu dördüncü ayet olumsuz ehad ile söyler. Eşit rütbede ikinci bir ilah olsaydı neler olacağını anlatan ayetler {source:23:91} {source:17:42}, savaşta denk olanın tarifini sahneye dönüştürür. İsrâ suresindeki övgü {source:17:111} da surenin kalıbını hükümranlığa uygular.

Söz imgelerinin ikisi Bakara suresinde iki ayet arasında karşılaşır. Uydurulmuş söz {ar:وَقَالُوا۟ ٱتَّخَذَ ٱللَّهُ وَلَدًۭا, tr:ve kâlü'ttehazallâhü veledâ, gloss:Allah çocuk edindi dediler, source:2:116} ile başlar, yaratıcı söz {ar:يَقُولُ لَهُۥ كُن فَيَكُونُ, tr:yekûlü lehû kün fe-yekûn, gloss:ona "ol" der, o da olur, source:2:117} ile biter. Her iki ayet de aynı soruya cevap verir: şeyler Allah'tan doğarak mı, yoksa O'nun sözüyle mi var olur? Ahzâb suresindeki ayet de iki sözü yan yana koyar; bir yanda ağızla söylenen söz, öbür yanda {ar:وَٱللَّهُ يَقُولُ ٱلْحَقَّ, tr:vallâhü yekûlü'l-hakk, gloss:Allah doğruyu söyler, source:33:4}. Doğum kökünün uydurulmuş söz için de kullanılması, sözler yarışmasını nesil zincirine bağlar: "Allah doğurdu" diyenlerin sözü {source:37:152}, kendisi de "doğurulmuş", yani uydurulmuş bir sözdür.

Bu buluşmalar surenin hareketini taşır. Birinci ayet bir sözle açılır ve sayıyı bire koyar. İkinci ayet bütün yönelişi, kapısına gidilen, içi boş olmayan ve her şey yok olduktan sonra kalan tek bir efendiye çevirir. Üçüncü ayet bu efendiden çıkışı da efendinin bir şeyden çıkışını da kapatır ve nesil zincirini, uydurulmuş "doğurdu" sözüyle birlikte dışarıda bırakır. Dördüncü ayet olumsuz kevn ile hiçbir dengin hiçbir zaman var olmadığını söyler ve sureyi başladığı kelimeyle, bu kez içinde hiç kimse bulunmayan ehad ile kapatır.

