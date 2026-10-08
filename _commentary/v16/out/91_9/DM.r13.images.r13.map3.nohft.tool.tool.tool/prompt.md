Focus: 91:9. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/91_9/D.r13/context.md =====
# 91:9 — focus

قَدْ أَفْلَحَ مَن زَكَّىٰهَا

Anchor translation (canonical reading, reference only):

Onu arındıran gerçekten başarıya ulaşmıştır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | قَدْ | قَد |  | CERT |
| 2 | أَفْلَحَ | أَفْلَحَ | ف ل ح | V |
| 3 | مَن | مَن |  | REL |
| 4 | زَكَّىٰهَا | زَكَّىٰ | ز ك و | V;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 91 — full text (context; no pericope)

- 91:1 وَٱلشَّمْسِ وَضُحَىٰهَا
- 91:2 وَٱلْقَمَرِ إِذَا تَلَىٰهَا
- 91:3 وَٱلنَّهَارِ إِذَا جَلَّىٰهَا
- 91:4 وَٱلَّيْلِ إِذَا يَغْشَىٰهَا
- 91:5 وَٱلسَّمَآءِ وَمَا بَنَىٰهَا
- 91:6 وَٱلْأَرْضِ وَمَا طَحَىٰهَا
- 91:7 وَنَفْسٍۢ وَمَا سَوَّىٰهَا
- 91:8 فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا
- 91:9 ◀ focus قَدْ أَفْلَحَ مَن زَكَّىٰهَا
- 91:10 وَقَدْ خَابَ مَن دَسَّىٰهَا
- 91:11 كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ
- 91:12 إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
- 91:13 فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا
- 91:14 فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا
- 91:15 وَلَا يَخَافُ عُقْبَٰهَا


===== _commentary/v16/work/91_9/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ف ل ح (root_001175) — identity root of أَفْلَحَ (w2)

- **B001** yarmak veya kesip ayırmak — bir şeyi yarmak veya kesmek · toprağı sürmek üzere yarmak · toprağı sürmek üzere yarmak · demiri başka bir demirle yarmak veya kesmek · bir uzuvdaki yarıklar
  أصل يدل على شق (maqayis)؛ فلحت الأرض شققتها (maqayis;sihah;tahdhib)؛ فلحت الشيء إذا شققته أو قطعته (jamhara)؛ الحديد بالحديد يفلح أي يشق أو يقطع (maqayis;ayn;jamhara;sihah;tahdhib;mufradat)
- **B002** dudakta, özellikle alt dudakta yarık — dudaktaki yarık · alt dudağı yarık olan erkek · dudağında yarık bulunan kadın · dudaktaki yarığın kendisi
  الفلح الشق في الشفة (ayn;tahdhib)؛ الأفلح المشقوق الشفة السفلى (maqayis;jamhara;sihah;tahdhib)؛ امرأة فلحاء وعنترة الفلحاء لفلحة كانت به (maqayis;jamhara;sihah;tahdhib)
- **B003** çiftçi ve toprağı işleme işi — çiftçi, toprağı işleyen kimse · toprağı sürme ve çiftçilik işi
  سمي الأكار فلاحا لأنه يشق الأرض (maqayis;jamhara;sihah;tahdhib;mufradat)؛ الفلاحون الزراعون (ayn)؛ الفلاحة الحراثة أو صناعة الفلاح (jamhara;sihah;tahdhib)
- **B004** çiftçiye benzetilen ücretli taşıyıcı — çiftçiye benzetilerek adlandırılan ücretli taşıyıcı
  الفلاح المكاري وإنما قيل له فلاح تشبيها بالأكار (ayn;tahdhib)؛ وجعله ابن أحمر المكاري (jamhara)
- **B005** iyilik içinde kalma, amaca ulaşma ve kurtuluş — iyilik içinde kalma, başarı ve kurtuluş · iyilik içinde kalma ve başarı · başarmak, amacına ulaşmak veya iyilik elde etmek · dilediğin biçimde yaşa · işinde başarı kazan ve onu kendi başına yürüt · kurtuluşa ve kalıcı iyiliğe yönel · iyilik elde eden başarılı kişi · dünya hayatında kalıcılık, varlık ve saygınlık elde etme · son bulmayan yaşam, yoksulluksuz varlık, aşağılanmayan saygınlık ve bilgisizlikten uzak bilgi · şafak öncesi öğünü ya da gece ibadetinin kazancını kaçırmaktan korkmak
  الأصل الثاني الفلاح البقاء والفوز (maqayis)؛ الفلاح والفلح البقاء في الخير (ayn;tahdhib)؛ الفلح والفلاح البقاء (jamhara)؛ الفلاح الفوز والنجاة والبقاء (sihah)؛ أفلح وأنجح إذا أدرك مطلوبه (jamhara)؛ استفلحي بأمرك أي فوزي أو اظفري بأمرك (maqayis;sihah;tahdhib)؛ الفلاح الظفر وإدراك بغية (mufradat)
- **B006** orucu sürdürmeye güç veren şafak öncesi öğün — şafak öncesi öğün · şafak öncesi öğünü ya da gece ibadetinin kazancını kaçırmaktan korkmak
  الفلاح السحور (maqayis;ayn;sihah;tahdhib)؛ سمي فلاحا لأن الإنسان تبقى معه قوته على الصوم (maqayis)؛ لأن به بقاء الصوم (sihah;tahdhib)؛ سمي السحور الفلاح (mufradat)
- **B007** alışverişi çekici gösterme; yalanla kandırma ve alaya alma — satış ve alışverişi satıcıya ve alıcıya çekici göstermek · satış ve alışverişi satıcıya ve alıcıya çekici göstermek · onları kandırıp gerçeğe aykırı söz söylemek · başkasını daha yüksek bedel vermeye kandırmak için kiracının bedeli artırması · kandırma ve alaya alma
  فلحت للقوم وبالقوم أفلح فلاحة وهو أن يزين البيع والشراء للبائع والمشتري (tahdhib)؛ فلحت بهم تفليحا إذا مكر بهم وقال لهم غير الحق (tahdhib)؛ الفلح النجس وهو زيادة المكتري ليزيد غيره فيغر به (tahdhib)؛ التفليح المكر والاستهزاء (tahdhib)

## ز ك و (root_000637) — identity root of زَكَّىٰهَا (w4)

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

===== _commentary/v16/out/s091/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 91:9, and ## Buluşmalar) =====
## Tarla: yarılan, sulanan, büyüyen toprak ve hiçbir şey bitirmeyen kum

Altıncı ayette yayılan yerin ailesinde verimli toprak vardır. Bu toprak dokuzuncu ayetin fiiliyle anılır: {ar:أرض أريضة أي زكية, tr:ardun erîdatun, ey zekiyye, gloss:erîde bir toprak, yani bereketle büyüyen toprak, source:"ء ر ض,B002"}. Bitkinin toprakta kök salıp çoğalması da yerin kökünden bir fiildir: {ar:تأرض النبت تمكن على الأرض فكثر, tr:te'arrada'n-nebtu: temekkene ale'l-ardı fe-kesura, gloss:bitki yere tutundu ve çoğaldı, source:"ء ر ض,B002"}. "Tahâ" fiili de toprağın yüzüne yayılmış bitkiyi anlatır: {ar:والبقلة المطحية النابتة على وجه الأرض قد افترشتها, tr:ve'l-baklatu'l-mathiyyetu en-nâbitetu alâ vechi'l-ard, kad efteraşethâ, gloss:yerin yüzünde biten ve onu döşek gibi kaplayan yayvan sebze, source:"ط ح و,B006"}. Göğün adı ise yağmurun da bitkinin de adıdır: {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tusemmi's-sehâbe semâen ve'l-matara semâ', gloss:Araplar buluta da yağmura da semâ der, source:"س م و,B004"}; {ar:سمي النبات سماء, tr:summiye'n-nebâtu semâ', gloss:bitkiye de semâ denmiştir, source:"س م و,B004"}. Bu adlarla beşinci ve altıncı ayetlerdeki ev bir tarlaya dönüşür. Tavandan su iner, döşeme yeşerir.

Tarlanın işlemesi suyun yolunu açmakla başlar. Üçüncü ayetteki gündüz kelimesi, toprağı yaran ırmakla aynı köktendir: {ar:سمي النهر لأنه ينهر الأرض أي يشقها, tr:summiye'n-nehru li-ennehû yenheru'l-ard, ey yeşukkuhâ, gloss:ırmağa nehr denmesi, toprağı yarmasındandır, source:"ن ه ر,B001"}. Sekizinci ayetteki fucûrun kökü suyun açıldığı yeri adlandırır: {ar:الفجرة موضع تفتح الماء, tr:el-fecretu mevdı'u tefettuhi'l-mâ', gloss:fecre, suyun açılıp aktığı yerdir, source:"ف ج ر,B001"}. Dokuzuncu ayetteki "efleha" fiili saban işidir: {ar:فلحت الأرض شققتها, tr:felahtu'l-arda: şakaktuhâ, gloss:toprağı sürdüm, yani yardım, source:"ف ل ح,B001"}. Çiftçinin adı da buradan gelir: {ar:سمي الأكار فلاحا لأنه يشق الأرض, tr:summiye'l-ekkâru fellâhan li-ennehû yeşukku'l-ard, gloss:çiftçiye fellâh denmesi, toprağı yarmasındandır, source:"ف ل ح,B003"}. Aynı ayetteki "zekkâhâ" ekinin büyümesidir: {ar:زكا الزرع يزكو زكاء ممدود أي نما, tr:zekâ'z-zer'u yezkû zekâen, ey nemâ, gloss:ekin zekâ etti, yani büyüdü, source:"ز ك و,B001"}; {ar:أصل الزكاة النمو الحاصل عن بركة الله تعالى, tr:aslu'z-zekâti'n-nemuvvu'l-hâsılu an bereketi'llâhi teâlâ, gloss:zekâtın aslı, Allah'ın bereketinden gelen büyümedir, source:"ز ك و,B001"}. On üçüncü ayetteki "sukyâ" bir tarlanın sudaki payıdır: {ar:كم سقى أرضك أي حظها من الشرب, tr:kem sakyu ardık, ey hazzuhâ mine'ş-şirb, gloss:toprağının sakyı ne kadar, yani su payı ne kadar, source:"س ق ي,B003"}. On dördüncü ayetteki "zenb" kelimesinin ailesinde yamaçlardaki su yolları vardır: {ar:المذانب مذانب التلاع وهي مسايل الماء فيها, tr:el-mezânibu mezânibu't-tilâ', ve hiye mesâyilu'l-mâi fîhâ, gloss:mezânib, yamaçlardaki su yataklarıdır, source:"ذ ن ب,B004"}. Aynı ayetteki "Rab" kelimesinin ailesinde ise bitkiyi besleyen bulut vardır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb: es-sehâb, summiye bi-zâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi beslediği için bu adı almıştır, source:"ر ب ب,B008"}. Kökün temel işi de budur: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi adım adım olgunluğa erdirmektir, source:"ر ب ب,B002"}.

Tarlanın tersi de surenin kelimelerinde durur. Onuncu ayetteki fiil, Arap dilinin açıkladığı türeyişle "dessese"ye götürür: toprağa itip gömmek. Kur'an'daki karşılığı, yukarıda anılan, toprağa gömme sahnesidir: {ar:أَمْ يَدُسُّهُۥ فِى ٱلتُّرَابِ, tr:em yedussuhû fi't-turâb, gloss:yoksa onu toprağa mı gömsün, source:16:59}. Çok derine itilen tohum filizlenmez. Fiil de büyümenin tam zıddı olarak tanımlanır: {ar:وهو نقيض زكا يزكو زكاء وزكاة وهو داس لا زاك, tr:ve huve nakîdu zekâ yezkû zekâen ve zekâten, ve huve dâsin lâ zâk, gloss:bu, büyümenin zıddıdır; o gömen biridir, büyüten değil, source:"د س و,B002"}. On dördüncü ayetteki suç fiili "akr", hiçbir şey bitirmeyen kumun adıdır: {ar:العاقر من الرمل ما لا ينبت شيئا, tr:el-âkiru mine'r-ramli mâ lâ yunbitu şey'â, gloss:âkir kum, hiçbir şey bitirmeyen kumdur, source:"ع ق ر,B017"}. Aynı fiil hurmanın büyüme noktasını kesip atmayı da anlatır: {ar:عقرت النخلة إذا قطعت رأسها كله مع الجمار, tr:ukırati'n-nahletu izâ kutı'a ra'suhâ kulluhû ma'a'l-cumâr, gloss:hurmanın başı, özüyle birlikte tümden kesilince "ukırat" denir, source:"ع ق ر,B007"}.

Kur'an bu tarlayı açıkça sahneler. Abese Suresi'nde Allah insana yemeğine bakmasını söyler: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:fe'l-yenzuri'l-insânu ilâ taâmih, gloss:insan yemeğine bir baksın, source:80:24}. Ardından üç adım sayılır: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:suyu bol bol döktük, source:80:25}; {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:summe şakakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26}; {ar:فَأَنۢبَتْنَا فِيهَا حَبًّۭا, tr:fe-enbetnâ fîhâ habbâ, gloss:orada tane bitirdik, source:80:27}. Dökmek, yarmak, bitirmek: dokuzuncu ayetteki sürme ve büyümenin adımları bunlardır. Nûh kavmine insanın kendisini bir bitki gibi anlatır: {ar:وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًۭا, tr:va'llâhu enbetekum mine'l-ardı nebâtâ, gloss:Allah sizi yerden bir bitki gibi bitirdi, source:71:17}. Bu yüzden nefsin büyütülmesi bir tarlanın büyümesiyle aynı işi görür. Kur'an iki toprağı yan yana koyar: {ar:وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ, tr:ve'l-beledu't-tayyibu yahrucu nebâtuhû bi-izni rabbih, gloss:iyi toprağın bitkisi Rabbinin izniyle çıkar, source:7:58}; {ar:وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًۭا, tr:ve'llezî habuse lâ yahrucu illâ nekidâ, gloss:kötü topraktan ise ancak cılız bir şey çıkar, source:7:58}. Mallarını harcayanlar için de iki örnek verir. Biri tepedeki bahçedir: {ar:كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ, tr:ke-meseli cennetin bi-rabvetin esâbehâ vâbilun fe-âtet ukulehâ dı'feyn, gloss:tepedeki bir bahçe gibi; sağanak ona isabet edince ürününü iki kat verir, source:2:265}. Öteki üzerinde biraz toprak olan kayadır: {ar:كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا, tr:ke-meseli safvânin aleyhi turâbun fe-esâbehû vâbilun fe-terakehû saldâ, gloss:üstünde toprak bulunan düz bir kaya gibi; sağanak onu çıplak bırakır, source:2:264}. Aynı yağmur bir yerde büyütür, öteki yerde altındaki kayayı ortaya çıkarır.

Semûd da bir tarla halkıdır. Salih onlara bunu hatırlatır: {ar:هُوَ أَنشَأَكُم مِّنَ ٱلْأَرْضِ وَٱسْتَعْمَرَكُمْ فِيهَا, tr:huve enşeekum mine'l-ardı ve'ste'marakum fîhâ, gloss:sizi yerden O yetiştirdi ve sizi orada imar ettirdi, source:11:61}. Onlar bahçelerin ve kaynakların içindedir: {ar:فِى جَنَّٰتٍۢ وَعُيُونٍۢ, tr:fî cennâtin ve uyûn, gloss:bahçeler ve pınarlar içinde, source:26:147}; {ar:وَزُرُوعٍۢ وَنَخْلٍۢ طَلْعُهَا هَضِيمٌۭ, tr:ve zurû'in ve nahlin tal'uhâ hedîm, gloss:ekinler ve tomurcukları yumuşacık hurmalar içinde, source:26:148}. Hurmalık içinde yaşayan bir kavmin suç fiili, hurmanın başını kesip atan fiille aynıdır. Kur'an büyümenin karşılığını da su yollarıyla anlatır: {ar:وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:ve zâlike cezâu men tezekkâ, gloss:işte bu, arınıp büyüyenin karşılığıdır, source:20:76}. Bu söz, Firavun'un tehdidi karşısında iman eden sihirbazların ağzındadır ve altından ırmaklar akan bahçeleri anlatır. Kalbin taşa dönmesi bile bu dille anlatılır: {ar:وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ, tr:ve inne mine'l-hicârati lemâ yetefecceru minhu'l-enhâr, gloss:taşların öylesi vardır ki içinden ırmaklar fışkırır, source:2:74}. Bu sözler İsrailoğullarına, kalpleri bu taşlardan da katı olduğu için söylenir. Düz bir anlatım dokuzuncu ve onuncu ayeti "nefsini arındıran" ve "nefsini kirleten" diye geçer. Fiillerin ailesi ise iki tarlayı gösterir: biri sürülmüş, sulanmış ve yeşermiş; öbürü gömülmüş ya da kum.

Kaynaklar: 91:3 ٱلنَّهَارِ ن ه ر B001; 91:5 ٱلسَّمَآءِ س م و B004; 91:6 ٱلْأَرْضِ ء ر ض B002; 91:6 طَحَىٰهَا ط ح و B006; 91:8 فُجُورَهَا ف ج ر B001; 91:9 أَفْلَحَ ف ل ح B001; 91:9 أَفْلَحَ ف ل ح B003; 91:9 زَكَّىٰهَا ز ك و B001; 91:10 دَسَّىٰهَا د س و B002; 91:13 وَسُقْيَٰهَا س ق ي B003; 91:14 بِذَنۢبِهِمْ ذ ن ب B004; 91:14 رَبُّهُم ر ب ب B002; 91:14 رَبُّهُم ر ب ب B008; 91:14 فَعَقَرُوهَا ع ق ر B007; 91:14 فَعَقَرُوهَا ع ق ر B017

## Suç ve topuğundaki

On dördüncü ve on beşinci ayetler bir bedenin arka ucunda kapanır. "Zenb" ile "ukbâ" ayrı köklerden gelir, ama ikisi de bir şeyin son ucunu adlandırır. Zenb kuyruktur: {ar:ذنب كل شيء آخره, tr:zenebu kulli şey'in âhiruh, gloss:her şeyin zenebi, onun son ucudur, source:"ذ ن ب,B002"}. Ukbâ da sondur: {ar:عاقبة كل شيء آخره والعقبى جزاء الأمر, tr:âkıbetu kulli şey'in âhiruh, ve'l-ukbâ cezâu'l-emr, gloss:her şeyin âkıbeti onun sonudur; ukbâ da bir işin karşılığıdır, source:"ع ق ب,B006"}. Günah, sonucuyla tanımlanır: {ar:يستعمل في كل فعل يستوخم عقباه, tr:yusta'melu fî kulli fi'lin yustevhamu ukbâh, gloss:sonu ağır gelen, sindirilemeyen her iş için kullanılır, source:"ذ ن ب,B001"}. Ceza da günahın ardından gelen ikinci şey olarak adını alır: {ar:سميت عقوبة لأنها تكون آخرا وثاني الذنب, tr:summiyet ukûbeten li-ennehâ tekûnu âhiran ve sâniye'z-zenb, gloss:cezaya ukûbe denmesi, en sonda ve günahın ikincisi olarak gelmesindendir, source:"ع ق ب,B007"}. İki kök tek bir cümlede de buluşur: {ar:العقاب العقوبة وقد عاقبته بذنبه, tr:el-ıkâbu'l-ukûbe, ve kad âkabtuhû bi-zenbih, gloss:ıkâb cezadır; onu günahıyla cezalandırdım, source:"ع ق ب,B007"}. Bu, on dördüncü ayetin "bi-zenbihim" sözüyle on beşinci ayetin "ukbâhâ" sözünün dilde birbirine bağlı iki parça olduğunu gösterir.

Suçu cezalandıran, malın sahibidir. On dördüncü ayet Rab der: {ar:رب كل شئ: مالكه, tr:rabbu kulli şey': mâlikuh, gloss:her şeyin rabbi, onun sahibidir, source:"ر ب ب,B001"}. On üçüncü ayette deve "Allah'ın devesi" diye anılmıştı. Sahibinin malına el uzatılmış, sahibi de karşılığı vermiştir. Gecenin fiili bu karşılığın biçimini verir: {ar:غاشية من عذاب الله أي عقوبة مجللة تعمهم, tr:ğâşiyetun min azâbi'llâh, ey ukûbetun mucellilatun teummuhum, gloss:Allah'ın azabından bir ğâşiye, yani onları baştan başa saran bir ceza, source:"غ ش و,B002"}. Ceza, on beşinci ayetin kökünden, gecenin örtüsüyle gelir.

On beşinci ayet sonucu hiç kimsenin geri çeviremeyeceğini söyler: {ar:وَلَا يَخَافُ عُقْبَٰهَا, tr:ve lâ yehâfu ukbâhâ, gloss:o, bunun sonundan korkmaz, source:91:15}. Ayetin öznesi, bir önceki ayetin öznesi olan Rabdir. Korku, bir işaretten zarar beklemektir: {ar:الخوف توقع مكروه عن أمارة مظنونة أو معلومة, tr:el-havfu tevakku'u mekrûhin an emâratin maznûnetin ev ma'lûme, gloss:korku, sanılan ya da bilinen bir işaretten hoşa gitmeyen bir şey beklemektir, source:"خ و ف,B001"}. Ama Allah'ın korkutması bir uyarıdır, kendisi korkmaz: {ar:التخويف من الله تعالى هو الحث على التحرز, tr:et-tahvîfu mina'llâhi teâlâ huve'l-hassu ale't-teharruz, gloss:Allah'ın korkutması, sakınmaya teşviktir, source:"خ و ف,B002"}. Kur'an deveyi tam olarak böyle bir korkutma olarak anar: {ar:وَمَا نُرْسِلُ بِٱلْءَايَٰتِ إِلَّا تَخْوِيفًۭا, tr:ve mâ nursilu bi'l-âyâti illâ tahvîfâ, gloss:işaretleri ancak korkutmak için göndeririz, source:17:59}. "Ukbâ" kökünün bir kolu, bir hükmün ardına düşüp hak arayanı adlandırır: {ar:المعقب الذي يتتبع عقب إنسان في طلب حق, tr:el-mu'akkıbu'llezî yetetebba'u akibe insânin fî talebi hakk, gloss:mu'akkıb, hak istemek için birinin topuğu ardınca izleyendir, source:"ع ق ب,B008"}; {ar:لا معقب لحكمه أي لا راد لقضائه, tr:lâ mu'akkıbe li-hukmih, ey lâ râdde li-kadâih, gloss:hükmünün ardına düşen yoktur, yani kararını geri çevirecek yoktur, source:"ع ق ب,B008"}. Kur'an bu sözü kendi diliyle söyler: {ar:وَٱللَّهُ يَحْكُمُ لَا مُعَقِّبَ لِحُكْمِهِۦ, tr:va'llâhu yahkumu lâ mu'akkibe li-hukmih, gloss:Allah hükmeder; O'nun hükmünün ardına düşüp onu bozacak yoktur, source:13:41}. Bir başka yerde aynı gerçeği şöyle söyler: {ar:لَا يُسْـَٔلُ عَمَّا يَفْعَلُ وَهُمْ يُسْـَٔلُونَ, tr:lâ yus'elu ammâ yef'alu ve hum yus'elûn, gloss:O yaptığından sorgulanmaz, onlar sorgulanır, source:21:23}.

Kur'an Semûd'un sonunu bu iki kelimeyle anlatır. Neml Suresi'nde dokuz kişilik çetenin tuzağı şöyle biter: {ar:فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ مَكْرِهِمْ أَنَّا دَمَّرْنَٰهُمْ وَقَوْمَهُمْ أَجْمَعِينَ, tr:fe'nzur keyfe kâne âkıbetu mekrihim, ennâ demmernâhum ve kavmehum ecma'în, gloss:tuzaklarının sonunun nasıl olduğuna bak: onları da kavimlerini de topyekûn yok ettik, source:27:51}. Ankebût Suresi'nde helak edilen kavimler toplu olarak anılır: {ar:فَكُلًّا أَخَذْنَا بِذَنۢبِهِۦ, tr:fe-kullen ehaznâ bi-zenbih, gloss:hepsini kendi günahıyla yakaladık, source:29:40}. Enfâl Suresi'nde de aynı bağ kurulur: {ar:فَأَهْلَكْنَٰهُم بِذُنُوبِهِمْ, tr:fe-ehleknâhum bi-zunûbihim, gloss:onları günahları yüzünden helak ettik, source:8:54}. Devenin biçilmesinden sonra Salih'in sözü, sonucu bir süreye bağlar: {ar:فَعَقَرُوهَا فَقَالَ تَمَتَّعُوا۟ فِى دَارِكُمْ ثَلَٰثَةَ أَيَّامٍۢ, tr:fe-akarûhâ fe-kâle temetta'û fî dârikum selâsete eyyâm, gloss:onu biçtiler; Salih de dedi ki: yurdunuzda üç gün daha yaşayın, source:11:65}; {ar:ذَٰلِكَ وَعْدٌ غَيْرُ مَكْذُوبٍۢ, tr:zâlike va'dun ğayru mekzûb, gloss:bu, yalanlanamayacak bir sözdür, source:11:65}. Yalanlayarak işe başlayan kavim, yalanlanamayan bir sözle karşılaşır.

Dokuzuncu ayet bu dilin öbür yüzünü taşır. Arınıp büyüyenin işi de sonucuyla tanımlanır, ama tersinden: {ar:حلالا لا يستوخم عقباه, tr:helâlen lâ yustevhamu ukbâh, gloss:helâl, yani sonu ağır gelmeyen, source:"ز ك و,B002"}. Günah sindirilemeyen bir sondur, arınmanın sonu ise kolay sindirilir. Düz bir anlatım son ayeti bir ek söz gibi okur. Bu imge ise onu surenin bedenine bağlar: suç arkada durur, karşılığı da onun ardından gelir ve ardından bir şey gelmeyen tek şey hükmün kendisidir.

Kaynaklar: 91:4 يَغْشَىٰهَا غ ش و B002; 91:9 زَكَّىٰهَا ز ك و B002; 91:14 رَبُّهُم ر ب ب B001; 91:14 بِذَنۢبِهِمْ ذ ن ب B001; 91:14 بِذَنۢبِهِمْ ذ ن ب B002; 91:15 يَخَافُ خ و ف B001; 91:15 يَخَافُ خ و ف B002; 91:15 عُقْبَٰهَا ع ق ب B006; 91:15 عُقْبَٰهَا ع ق ب B007; 91:15 عُقْبَٰهَا ع ق ب B008

## Arayanın eline geçen

Dokuzuncu ve onuncu ayetler iki arayışın sonucunu söyler. "Efleha" kalmayı ve aranana ulaşmayı anlatır: {ar:الفلاح والفلح البقاء في الخير, tr:el-felâhu ve'l-felahu el-bekâu fi'l-hayr, gloss:felâh ve felah, iyilik içinde kalıcı olmaktır, source:"ف ل ح,B005"}; {ar:أفلح وأنجح إذا أدرك مطلوبه, tr:efleha ve encaha izâ edreke matlûbeh, gloss:aradığına erişince "efleha" ve "encaha" denir, source:"ف ل ح,B005"}. "Hâbe" ise aranandan yoksun kalmaktır: {ar:سعى في أمر فخاب إذا حرم فلم يفد خيرا, tr:se'â fî emrin fe-hâbe izâ hurime fe-lem yufid hayran, gloss:bir iş için koştu ve eli boş kaldı, yani yoksun kaldı, hiçbir hayır elde edemedi, source:"خ ي ب,B001"}; {ar:الخيبة فوت الطلب, tr:el-hayebetu fevtu't-taleb, gloss:hayebe, aranan şeyi kaçırmaktır, source:"خ ي ب,B001"}. Kökün aslı bir somut nesneye dayanır: {ar:الأصل قولهم للقدح الذي لا يوري هو خياب, tr:el-aslu kavluhum li'l-kadhi'llezî lâ yûrî: huve hayyâb, gloss:aslı, ateş vermeyen çakmak çubuğuna "hayyâb" demeleridir, source:"خ ي ب,B002"}. Ateş çakan biri çubuğu sürter, sürter, ama kıvılcım çıkmaz. Elinde, ışık vermeyen bir çubukla kalır. Sure ışıkla açılmıştı. Onuncu ayetteki kişinin eli ise kıvılcımsız kalır.

Onuncu ayetin iki fiili dilde tek bir cümlede birleşir: {ar:خاب من دس نفسه أي أخملها وخسس حظها, tr:hâbe men dessâ nefseh, ey ahmelehâ ve hassese hazzahâ, gloss:nefsini gizleyen eli boş kalmıştır; yani onu sönük bırakmış ve payını küçültmüştür, source:"د س و,B002"}. Gizlenen nefsin payı küçülür. On ikinci ayetteki en bedbaht ise bir yorgunluğun da adıdır: {ar:يوضع الشقاء موضع التعب وكل شقاوة تعب وليس كل تعب شقاوة, tr:yuveda'u'ş-şekâu mevdı'a't-ta'ab, ve kullu şekâvetin ta'ab, ve leyse kullu ta'abin şekâve, gloss:şekâ, yorgunluk yerine kullanılır; her bedbahtlık yorgunluktur, ama her yorgunluk bedbahtlık değildir, source:"ش ق و,B002"}. En bedbaht kişi en çok çabalayandır, ama emeğinin sonu tükenişe çıkar.

Kur'an bu kelimeleri yan yana koyar. A'lâ Suresi'nde öğüt, ondan yararlanan ile kaçan arasında bölünür: {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yezzekkeru men yahşâ, gloss:içi titreyen öğüt alacak, source:87:10}; {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht ise ondan kaçınacak, source:87:11}. Birkaç ayet sonra bu surenin dokuzuncu ayetine çok yakın bir söz gelir: {ar:قَدْ أَفْلَحَ مَن تَزَكَّىٰ, tr:kad efleha men tezekkâ, gloss:arınıp büyüyen kurtuluşa ermiştir, source:87:14}. Hemen ardından gelen sure de bu kelimeyi tekrarlar: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}. Hesap günü insanlar iki yöne ayrılır: {ar:فَمِنْهُمْ شَقِىٌّۭ وَسَعِيدٌۭ, tr:fe-minhum şakıyyun ve se'îd, gloss:onlardan kimi bedbaht, kimi mutludur, source:11:105}. Cehennemdekiler de kendi bedbahtlıklarını itiraf eder: {ar:رَبَّنَا غَلَبَتْ عَلَيْنَا شِقْوَتُنَا, tr:rabbenâ ğalebet aleynâ şikvetunâ, gloss:Rabbimiz, bedbahtlığımız bizi yendi, source:23:106}. Eli boş kalmanın anlatıldığı yerlerde de aynı kalıp gelir. Mûsâ sihirbazlara şöyle seslenir: {ar:وَقَدْ خَابَ مَنِ ٱفْتَرَىٰ, tr:ve kad hâbe meni'fterâ, gloss:yalan uyduran eli boş kalmıştır, source:20:61}. Hesap gününde de: {ar:وَقَدْ خَابَ مَنْ حَمَلَ ظُلْمًۭا, tr:ve kad hâbe men hamele zulmâ, gloss:zulüm yüklenen eli boş kalmıştır, source:20:111}. Elçilerin yardım dilediği sahnede de: {ar:وَخَابَ كُلُّ جَبَّارٍ عَنِيدٍۢ, tr:ve hâbe kullu cebbârin anîd, gloss:her inatçı zorba eli boş kaldı, source:14:15}. Arınmanın kazancı ise arınanın kendisinedir: {ar:وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ, tr:ve men tezekkâ fe-innemâ yetezekkâ li-nefsih, gloss:arınıp büyüyen, ancak kendisi için arınıp büyür, source:35:18}. Düz bir anlatım "kurtuldu" ve "kaybetti" der. Bu kelimeler ise bir arayışı gösterir: biri iyilikte kalır, öbürünün elinde kıvılcım çıkarmayan bir çubuk, ötekinin payında da boşa giden bir yorgunluk kalır.

Kaynaklar: 91:9 أَفْلَحَ ف ل ح B005; 91:10 خَابَ خ ي ب B001; 91:10 خَابَ خ ي ب B002; 91:10 دَسَّىٰهَا د س و B002; 91:12 أَشْقَىٰهَا ش ق و B002

## Buluşmalar

İlk buluşma sekizinci ayette olur. "Fucûr" kelimesi aynı kökten üç sahneyi bir arada tutar: geceyi yaran şafağı, bentten fırlayan suyu ve din perdesini yırtmayı. Gökte yarılma ışık getirir, nefiste ise koruyucu örtüyü yırtar ve bir taşkın başlatır. Takvâ aynı ayette hem bir örtüdür hem de bir settir. Tek bir kelime bu iki imgeyi birlikte taşır: örten ve alıkoyan. Böylece surenin başındaki düzenli nöbet nefsin içine taşınır. Gece güneşin üstünü sırası gelince örter ve sırası gelince açılır. Nefis ise ya kendi örtüsünü yerinde tutar ya da onu yırtıp taşar.

İkinci buluşma on ikinci ayetteki "inbe'ase" fiilindedir. Bu fiil üç imgeyi birden toplar. Fucûru tanımlayan atılıştır, deveyi köstekinden çözüp kaldırmanın sonucudur ve Allah'ın elçi gönderişinin eşi olan bir fiildir. Deve sürücüsünün dilinde biri kaldırır, deve kalkar. Bu ayette ise kaldıran yoktur. Adam kendi kendine, köstekinden kurtulmuş bir hayvan gibi kalkar ve Allah'ın gönderdiği deveye yönelir. Elçi gönderilmiştir, deve gönderilmiştir. Taşkın olan ise kendini gönderir.

Üçüncü buluşma, on dördüncü ayetten on beşinciye geçen bedenin arka ucudur. "Akr" topuk kirişini keser. O kirişin adı on beşinci ayetteki "ukbâ" kelimesinin kökündendir. Günahın adı olan "zenb" de hayvanın arka ucunun adıdır. Devenin imgesi ile suçun ardından gelen sonucun imgesi böylece aynı noktada birleşir. Kavim devenin arkasına vurur; karşılık da onların "arkalarından", yani günahlarının ardından gelir. Kova ile günahın aynı kökten gelmesi bunu ölçüye bağlar. Devenin su payını çiğneyenler kendi kova paylarını alırlar.

Dördüncü buluşma "sevvâ" fiilindedir. Bu fiil göğün ve nefsin bitirilişini Semûd'un yerle bir edilişine bağlar. Altıncı ayetteki yayılmış yer bu iki ucun arasında durur. Kavim ovaya saray kurmuştu. Yayılan yere kurulan sarayları yayılmış bir yer gibi dümdüz olur. Gökten yağan su, sürülen toprak ve büyüyen ekin bu yere bağlıdır. Hurmanın başını kesmeyi ve hiçbir şey bitirmeyen kumu anlatan "akr" fiili, kavmin tarlasını bir çorak yere çevirir.

Bu buluşmalar birlikte surenin hareketini taşır. Sure, her cismin yerini bildiği bir gökle başlar: ışık yayılır, ay onu izler, gündüz açar, gece örter. Ardından gök ve yerden bir ev kurulur ve aynı el nefsi bu evin üçüncü yapısı olarak düzenler. Nefse iki lokma yutturulur: hem yırtan ve taşan hem de örten ve alıkoyan. Dokuzuncu ve onuncu ayetler bu iki lokmanın sonucunu iki tarla gibi gösterir: biri sürülmüş ve büyümüş, öbürü gömülmüş. Semûd ise yanlış yolu seçer. Sınırı aşar, kendi en bedbahtının ardına düşer, gönderilen deveyi arkasından biçer. Karşılık gece gibi üstlerine kapanır ve evleri ile birlikte onları yayılmış bir yer gibi dümdüz eder. Sure, gece ile gündüzün nöbetleşmesini de adlandıran bir kelimeyle kapanır. Ama bu son nöbette, hükmün ardından gelecek ve onu geri çevirecek hiçbir şey yoktur.

