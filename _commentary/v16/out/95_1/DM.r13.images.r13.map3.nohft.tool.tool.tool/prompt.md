Focus: 95:1. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/95_1/D.r13/context.md =====
# 95:1 — focus

وَٱلتِّينِ وَٱلزَّيْتُونِ

Anchor translation (canonical reading, reference only):

İncire ve zeytine andolsun.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَٱلتِّينِ | تِّين | ت ي ن | P;DET;N |
| 2 | وَٱلزَّيْتُونِ | زَّيْتُون | ز ي ت | CONJ;DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 95 — full text (context; no pericope)

- 95:1 ◀ focus وَٱلتِّينِ وَٱلزَّيْتُونِ
- 95:2 وَطُورِ سِينِينَ
- 95:3 وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ
- 95:4 لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ
- 95:5 ثُمَّ رَدَدْنَٰهُ أَسْفَلَ سَٰفِلِينَ
- 95:6 إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۢ
- 95:7 فَمَا يُكَذِّبُكَ بَعْدُ بِٱلدِّينِ
- 95:8 أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ


===== _commentary/v16/work/95_1/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ت ي ن (root_000190) — identity root of وَٱلتِّينِ (w1)

- **B001** yenilebilir incir meyvesi — taze veya kuru yenilen bilinen incir meyvesi · tek bir incir meyvesi
  التين وهو معروف (maqayis)؛ والتين ثمر معروف (jamhara)؛ التين هذا الذي يؤكل رطبا ويابسا الواحدة تينة (sihah)؛ هو تينكم هذا وزيتونكم (tahdhib)؛ هما المأكولان (mufradat)
- **B002** yer veya dağ adı — yer, dağ veya bölgesel mekan adı
  والتين جبل (maqayis;jamhara)؛ جبلان بالشأم (sihah)؛ مسجدان بالشام (tahdhib)؛ التين جبال ما بين حلوان إلى همذان (tahdhib)؛ قيل هما جبلان (mufradat)
- **B003** kurt için ad — bazı konuşma biçimlerinde kurt için kullanılan ad
  وقد سمي الذئب تِينانا في بعض اللغات (jamhara)

## ز ي ت (root_000656) — identity root of وَٱلزَّيْتُونِ (w2)

- **B001** zeytin meyvesinden çıkarılan yağ — zeytin meyvesinden çıkarılan bilinen yağ ve sıkılmış öz
  الزيت معروف (maqayis;jamhara)؛ الزيت دهنه (sihah)؛ الزيت عصارة الزيتون (tahdhib;mufradat)؛ الدهن الذي يستخرج منه زيت (tahdhib)
- **B002** zeytin ağacı, meyvesi veya topluluğu — zeytin ağacı, meyvesi veya bunların topluluğu · tek bir zeytin ağacı veya tek bir zeytin meyvesi
  الزيتون معروف والواحدة زيتونة (sihah)؛ يقال للشجرة نفسها زيتونة ولثمرها زيتونة والجميع الزيتون (tahdhib)؛ زيتون وزيتونة نحو شجر وشجرة (mufradat)
- **B003** yemeğe yağ katmak ya da birine veya kendine yağ sürmek — yemeğe yağ katmak veya yemeği yağla hazırlamak · başa yağ sürmek · yağ katılmış veya yağla hazırlanmış · yağ katılmış ya da üzerine yağ sürülmüş · kendine yağ sürmek · kendine yağ sürmüş kimse · kendine yağ sürmüş kimseyi küçülterek anlatan biçim
  زته إذا دهنته بالزيت (maqayis)؛ طعام مزيت إذا كان فيه الزيت (jamhara)؛ زت الطعام إذا جعلت فيه الزيت وطعام مزيت ومزيوت (sihah)؛ زت الثريد وزت رأس فلان وازدات فلان إذا ادهن بالزيت (tahdhib)؛ زات طعامه وزات رأسه وازدات ادهن (mufradat)
- **B004** bir topluluğa yağı katık yapmak veya sağlamak ya da yağı bağış olarak istemek — topluluğun katığını zeytinden çıkarılan yağ yapmak · onlara zeytinden çıkarılan yağ sağlamak · zeytinden çıkarılan yağı bağış olarak istemek
  زت القوم جعلت أدمهم الزيت؛ زيتهم إذا زودتهم الزيت؛ جاءوا يستزيتون أي يستوهبون الزيت
- **B005** zeytin yağını satan veya sıkıp çıkaran kişi — zeytin yağını satan veya zeytini sıkıp yağ çıkaran kişi
  يقال للذي يبيعه ويعتصره زيات

===== _commentary/v16/out/s095/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 95:1, and ## Buluşmalar) =====
## Yeminin yerleri: dağlar, Tûr ve güvenli belde

Sure üç ayet boyunca yemin eder ve yemin bir yerden ötekine geçer. {ar:وَٱلتِّينِ وَٱلزَّيْتُونِ, tr:ve't-tîni ve'z-zeytûn, gloss:incire ve zeytine andolsun, source:95:1} öncelikle iki meyveyi anar. Arapça incir adını bir dağa da verir: {ar:والتين جبل, tr:ve't-tînü cebel, gloss:Tîn bir dağdır, source:"ت ي ن,B002"}. İkisini birlikte de dağ olarak anar: {ar:قيل هما جبلان, tr:kîle hümâ cebelân, gloss:ikisinin iki dağ olduğu söylendi, source:"ت ي ن,B002"}. Kur'an bir yerde ağaçla dağı aynı ayette birleştirir: {ar:وَشَجَرَةًۭ تَخْرُجُ مِن طُورِ سَيْنَآءَ تَنۢبُتُ بِٱلدُّهْنِ وَصِبْغٍۢ لِّلْءَاكِلِينَ, tr:ve şeceraten tahrucü min tûri seynâe tenbütü bi'd-dühni ve sıbgın li'l-âkilîn, gloss:ve Tûr-ı Seyna'dan çıkan bir ağaç; yağ ve yiyenlere katık bitirir, source:23:20}. Burada anılan dağın adı, ikinci ayetteki {ar:وَطُورِ سِينِينَ, tr:ve tûri sînîn, gloss:ve Sînîn dağı, source:95:2} adına çok yakındır. Tûr, belirli bir dağın adıdır: {ar:الطور اسم جبل مخصوص وقيل اسم لكل جبل, tr:et-tûru ismü cebelin mahsûs ve kîle ismün li-külli cebel, gloss:Tûr belirli bir dağın adıdır; her dağın adı olduğu da söylenmiştir, source:"ط و ر,B005"}. Kur'an bu dağa ayrıca yemin eder: {ar:وَٱلطُّورِ, tr:ve't-tûr, gloss:Tûr'a andolsun, source:52:1}.

Kur'an'da Tûr, Allah'ın Musa ile konuştuğu yerdir. Musa süresini doldurup ailesiyle yola çıktığında olan şudur: {ar:ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا, tr:ânese min câbibi't-tûri nârâ, gloss:Tûr'un yanında bir ateş fark etti, source:28:29}. Ânese fiili, dördüncü ayetteki {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan, source:95:4} kelimesiyle aynı köke bağlanır: {ar:آنس من جانب يعني أبصر نارا, tr:ânese min câbib ya'nî ebsara nârâ, gloss:bir yandan fark etti yani bir ateş gördü, source:"ء ن س,B002"}. Ardından ağaçtan bir çağrı gelir: {ar:نُودِىَ مِن شَٰطِئِ ٱلْوَادِ ٱلْأَيْمَنِ فِى ٱلْبُقْعَةِ ٱلْمُبَٰرَكَةِ مِنَ ٱلشَّجَرَةِ, tr:nûdiye min şâtıi'l-vâdi'l-eymeni fi'l-buk'ati'l-mübâraketi mine'ş-şecera, gloss:vadinin sağ kıyısından, mübarek yerdeki ağaçtan seslenildi, source:28:30}. Musa kaçar ve {ar:إِنَّكَ مِنَ ٱلْءَامِنِينَ, tr:inneke mine'l-âminîn, gloss:sen güvende olanlardansın, source:28:31} sözüyle güvenceye alınır. Kur'an bu çağrıyı başka yerlerde de anar: {ar:وَنَٰدَيْنَٰهُ مِن جَانِبِ ٱلطُّورِ ٱلْأَيْمَنِ وَقَرَّبْنَٰهُ نَجِيًّۭا, tr:ve nâdeynâhü min câbibi't-tûri'l-eymeni ve karrabnâhü neciyyâ, gloss:ona Tûr'un sağ yanından seslendik ve fısıldaşmak için onu yaklaştırdık, source:19:52}. Peygamber'e {ar:وَمَا كُنتَ بِجَانِبِ ٱلطُّورِ إِذْ نَادَيْنَا, tr:ve mâ künte bi-câbibi't-tûri iz nâdeynâ, gloss:biz seslendiğimizde sen Tûr'un yanında değildin, source:28:46} denir. İsrailoğulları için Tûr bir buluşma yeridir: {ar:وَوَٰعَدْنَٰكُمْ جَانِبَ ٱلطُّورِ ٱلْأَيْمَنَ وَنَزَّلْنَا عَلَيْكُمُ ٱلْمَنَّ وَٱلسَّلْوَىٰ, tr:ve vâ'adnâküm câbibe't-tûri'l-eymene ve nezzelnâ aleykümü'l-menne ve's-selvâ, gloss:sizinle Tûr'un sağ yanında sözleştik ve size kudret helvası ve bıldırcın indirdik, source:20:80}. Aynı zamanda bir misak yeridir: {ar:وَإِذْ أَخَذْنَا مِيثَٰقَكُمْ وَرَفَعْنَا فَوْقَكُمُ ٱلطُّورَ, tr:ve iz ehaznâ mîsâkaküm ve refa'nâ fevkakümü't-tûr, gloss:sizden söz almış ve Tûr'u üstünüze kaldırmıştık, source:2:63}. Yeminin ikinci durağı böylece vahyin, ahdin ve korkudan güvene geçişin yeridir.

Üçüncü ayet en yakın yere gelir: {ar:وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ, tr:ve hâze'l-beledi'l-emîn, gloss:ve bu güvenli belde, source:95:3}. "Bu" kelimesi yeri işaret eder ve dinleyeni beldenin içine yerleştirir. Beled sınırlı ve içinde insanlar yaşayan bir yerdir: {ar:البلد المكان المحيط المحدود المتأثر باجتماع قطانه وإقامتهم فيه, tr:el-beledü'l-mekânü'l-muhîtu'l-mahdûdü'l-müteessiru bi'ctimâ'ı kuttânihî ve ikâmetihim fîh, gloss:beled sakinlerinin toplanması ve orada oturmasıyla şekillenen çevrili ve sınırlı yerdir, source:"ب ل د,B001"}. Fiil hali bir yerde oturup kalmaktır: {ar:بلد بالمكان أقام به فهو بالد, tr:beled bi'l-mekân ekâme bihî fe-hüve bâlid, gloss:bir yerde oturdu; o orada yerleşiktir, source:"ب ل د,B009"}. Emîn, korkunun karşıtıdır: {ar:الأمن ضد الخوف, tr:el-emnü ziddü'l-havf, gloss:emn korkunun karşıtıdır, source:"ء م ن,B001"}. Kişinin güven içinde oturduğu yer de bu köktendir: {ar:مأمنه منزله الذي فيه أمنه, tr:me'menühû menzilühü'llezî fîhi emnüh, gloss:me'meni güvenliğinin bulunduğu evidir, source:"ء م ن,B001"}. Kur'an bu beldenin güvenini İbrahim'in duasına bağlar: {ar:رَبِّ ٱجْعَلْ هَٰذَا ٱلْبَلَدَ ءَامِنًۭا, tr:rabbic'al hâze'l-belede âminâ, gloss:Rabbim, bu beldeyi güvenli kıl, source:14:35}. Aynı duada belde Ev ile anılır: {ar:عِندَ بَيْتِكَ ٱلْمُحَرَّمِ, tr:inde beytike'l-muharram, gloss:dokunulmaz Evinin yanında, source:14:37}. Ev'in kendisi de {ar:وَإِذْ جَعَلْنَا ٱلْبَيْتَ مَثَابَةًۭ لِّلنَّاسِ وَأَمْنًۭا, tr:ve iz ce'alne'l-beyte mesâbeten li'n-nâsi ve emnâ, gloss:Ev'i insanlar için bir dönüş yeri ve güven kıldık, source:2:125} diye anılır. Oraya girenin durumu da bellidir: {ar:وَمَن دَخَلَهُۥ كَانَ ءَامِنًۭا, tr:ve men dehalehû kâne âminâ, gloss:oraya giren güvende olur, source:3:97}. Bu Ev {ar:لَلَّذِى بِبَكَّةَ مُبَارَكًۭا, tr:lellezî bi-bekkete mübâreken, gloss:Bekke'deki mübarek Ev, source:3:96} diye tanıtılır. Peygamber de {ar:إِنَّمَآ أُمِرْتُ أَنْ أَعْبُدَ رَبَّ هَٰذِهِ ٱلْبَلْدَةِ ٱلَّذِى حَرَّمَهَا, tr:innemâ umirtü en a'büde rabbe hâzihi'l-beldeti'llezî harramehâ, gloss:bana yalnızca bu beldenin, onu dokunulmaz kılan Rabbine kulluk etmem emredildi, source:27:91} der. Bu beldenin adlarından biri de surenin altıncı ayetindeki iyi işlerle aynı köktendir: {ar:وصلاح مثل قطام اسم مكة, tr:ve salâhi misle katâmi ismü mekke, gloss:Salâh Mekke'nin bir adıdır, source:"ص ل ح,B005"}. Dîn kelimesinin kökünden ise şehir anlamındaki medîne gelir: {ar:المدينة كأنها مفعلة سميت بذلك لأنها تقام فيها طاعة ذوي الأمر, tr:el-medînetü keennehâ mef'ale sümmiyet bi-zâlike li-ennehâ tükâmü fîhâ tâ'atü zevi'l-emr, gloss:medine, içinde yöneticilere itaat edildiği için bu adı almıştır, source:"د ي ن,B006"}. Yemin edilen belde ile hesap günü anlamındaki din arasındaki bu bağ, kökte duyulan bir sestir.

Tûr kelimesinin kökü yerin sınırlarını da çizer. Bir evin önünde uzanan avlu tavârdır: {ar:طوار الدار وهو الذي يمتد معها من فنائها, tr:tavâru'd-dâr ve hüve'llezî yemtedü me'ahâ min finâihâ, gloss:evin tavârı onunla birlikte avlusundan uzanan kısımdır, source:"ط و ر,B001"}. Bir yerin etrafında dolaşıp ona yaklaşmak da bu köktendir: {ar:طار فلان يطور طورا أي كأنه يحوم حواليه ويدنو منه, tr:târa fülânün yetûru tavran ey keennehû yehûmü havâleyhi ve yednû minh, gloss:filan etrafında dolaşıp ona yaklaştı, source:"ط و ر,B002"}. Bir yerden uzak durmak da öyle: {ar:لا أطور به أي لا أقرب فناءه, tr:lâ etûru bihî ey lâ akrabu finâeh, gloss:onun avlusuna yaklaşmam, source:"ط و ر,B002"}. Sınırı aşmak için bir deyim vardır: {ar:عدا طوره أي جاز الحد الذي هو له من داره, tr:adâ tavrahû ey câze'l-hadde'llezî hüve lehû min dârih, gloss:tavrını aştı yani evinde kendisine düşen sınırı geçti, source:"ط و ر,B003"}. Sınırın ötesi yabanidir: {ar:للوحشي من الطير وغيرها طوري وطوارني فهو من هذا كأنه توحش فعدا الطور, tr:li'l-vahşiyyi mine't-tayri ve gayrihâ tûriyyün ve tuvârâniyy fe-hüve min hâzâ keennehû tevahhaşe fe-ade't-tavr, gloss:yabani kuşa ve başka yabani hayvana tûrî denir; sanki yabanileşip sınırı aşmıştır, source:"ط و ر,B006"}. Kimsesiz yer de bu kökle tarif edilir: {ar:ما بها طوري أي أحد, tr:mâ bihâ tûriyy ey ehad, gloss:orada kimse yok, source:"ط و ر,B007"}. İnsan kelimesinin kökü ise bu yabaniliğin karşısındadır: {ar:الإيناس خلاف الإيحاش والإنس خلاف الوحشة, tr:el-înâsü hilâfü'l-îhâş ve'l-ünsü hilâfü'l-vahşe, gloss:înas ürkütmenin karşıtıdır; üns yalnızlık ve yabanilik duygusunun karşıtıdır, source:"ء ن س,B003"}. Evcil köpeğe {ar:كلب أنوس نقيض العقور, tr:kelbün enûs nakîdu'l-akûr, gloss:enûs köpek ısıran köpeğin karşıtıdır, source:"ء ن س,B003"} denir. İnsan, görünür olduğu için bu adı alır: {ar:الإنس خلاف الجن وسموا لظهورهم, tr:el-insü hilâfü'l-cinn ve sümmû li-zuhûrihim, gloss:ins cinnin karşıtıdır ve görünür oldukları için böyle adlandırılmışlardır, source:"ء ن س,B001"}. Bu ses ailesinde surenin kelimeleri bir haritaya benzer. Ortada içinde oturulan güvenli belde vardır. Dağ sınırın ötesindedir. İnsan, adının kökünde yabaninin karşıtını taşır. Yedinci ayetin ba'd kelimesi, ayette "bundan sonra" anlamına gelirken, ailesinde yakının karşıtı olan uzaklığı da taşır: {ar:البعد خلاف القرب, tr:el-bu'du hilâfü'l-kurb, gloss:uzaklık yakınlığın karşıtıdır, source:"ب ع د,B001"}. Elyes ise evinden ayrılmayan kişiyi anar ve bu bir kınamadır: {ar:الأليس: الذي لا يبرح بيته, tr:el-elyes ellezî lâ yebrahu beyteh, gloss:elyes evinden ayrılmayandır, source:"ل ي س,B005"}.

Kur'an güvenli harem ile çevresini açıkça karşılaştırır: {ar:أَوَلَمْ يَرَوْا۟ أَنَّا جَعَلْنَا حَرَمًا ءَامِنًۭا وَيُتَخَطَّفُ ٱلنَّاسُ مِنْ حَوْلِهِمْ, tr:e-ve lem yerev ennâ ce'alnâ haramen âminen ve yütehattafü'n-nâsu min havlihim, gloss:görmezler mi ki biz güvenli bir harem kıldık, oysa çevrelerinde insanlar kapılıp götürülüyor, source:29:67}. Aynı ayet {ar:أَفَبِٱلْبَٰطِلِ يُؤْمِنُونَ وَبِنِعْمَةِ ٱللَّهِ يَكْفُرُونَ, tr:e-fe-bi'l-bâtıli yü'minûne ve bi-ni'metillâhi yekfürûn, gloss:batıla mı inanıyorlar da Allah'ın nimetini inkâr ediyorlar, source:29:67} diye devam eder. Güvenli beldeyi gösteren bu ayet, yedinci ayetin sorusuna yaklaşır. Kur'an yeminle başlayıp insanın yaratılışına geçen bir başka sure de anar. O surede beldeye yemin edilir, {ar:لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ, tr:lâ uksimü bi-hâze'l-beled, gloss:hayır, bu beldeye yemin ederim, source:90:1}, ve beldede yaşayan Peygamber'e {ar:وَأَنتَ حِلٌّۢ بِهَٰذَا ٱلْبَلَدِ, tr:ve ente hıllün bi-hâze'l-beled, gloss:sen bu beldede yaşıyorsun, source:90:2} denir. Ardından {ar:لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِى كَبَدٍ, tr:lekad halaknel insâne fî kebed, gloss:andolsun insanı zahmet içinde yarattık, source:90:4} gelir. Tîn suresi de aynı kuruluşla ilerler: "bu belde"ye yemin eder, ardından "andolsun insanı yarattık" der. Beled suresinde insan zahmet içinde, Tîn suresinde en güzel duruşta yaratılmıştır. Bu iki tasvir birbirini tamamlar.

Kaynaklar: 95:1 وَٱلتِّينِ ت ي ن B002; 95:1 وَٱلزَّيْتُونِ ز ي ت B002; 95:2 وَطُورِ سِينِينَ ط و ر B005; 95:4 ٱلْإِنسَٰنَ ء ن س B002; 95:3 ٱلْبَلَدِ ب ل د B001; 95:3 ٱلْبَلَدِ ب ل د B009; 95:3 ٱلْأَمِينِ ء م ن B001; 95:6 ٱلصَّٰلِحَٰتِ ص ل ح B005; 95:7 بِٱلدِّينِ د ي ن B006; 95:2 طُورِ ط و ر B001; 95:2 طُورِ ط و ر B002; 95:2 طُورِ ط و ر B003; 95:2 طُورِ ط و ر B006; 95:2 طُورِ ط و ر B007; 95:4 ٱلْإِنسَٰنَ ء ن س B001; 95:4 ٱلْإِنسَٰنَ ء ن س B003; 95:7 بَعْدُ ب ع د B001; 95:8 أَلَيْسَ ل ي س B005

## Meyve, yağ ve rızık

İncir ve zeytin her şeyden önce yenen şeylerdir. İncir {ar:التين هذا الذي يؤكل رطبا ويابسا, tr:et-tînü hâzellezî yü'kelü ratben ve yâbisâ, gloss:incir taze de kuru da yenen bu meyvedir, source:"ت ي ن,B001"} diye tanımlanır. Arapça ikisini birlikte de anar: {ar:هما المأكولان, tr:hüme'l-me'kûlân, gloss:ikisi yenen iki şeydir, source:"ت ي ن,B001"}. Zeytinden sıkılan yağ çıkar: {ar:الزيت عصارة الزيتون, tr:ez-zeyt usâratü'z-zeytûn, gloss:zeytinyağı zeytinin özsuyudur, source:"ز ي ت,B001"}. Ağaç da meyve de aynı adla anılır {source:"ز ي ت,B002"}. Yağın kullanımları ayrı ayrı adlandırılır. Tiridin içine katılır ve başa sürülür: {ar:زت الثريد وزت رأس فلان وازدات فلان إذا ادهن بالزيت, tr:zittü's-serîde ve zittü re'se fülânin ve'zdâde fülânün izedde'hene bi'z-zeyt, gloss:tiride yağ kattım; filanın başını yağladım; filan zeytinyağı süründü, source:"ز ي ت,B003"}. Bir topluluğun katığı ve azığı olur: {ar:زت القوم جعلت أدمهم الزيت؛ زيتهم إذا زودتهم الزيت, tr:zittü'l-kavme ce'altü üdümehümü'z-zeyt; zeyyetehüm izâ zevvedtehümü'z-zeyt, gloss:topluluğun katığını zeytinyağı yaptım; onlara azık olarak zeytinyağı verdim, source:"ز ي ت,B004"}. Onu sıkıp satan zeyyâttır {source:"ز ي ت,B005"}. Birinci ayetin iki kelimesi bir sofrayı, bir sıkımhaneyi ve yola çıkan bir kafilenin azığını gösterir.

Bu rızık surenin içinde devam eder. Takvîmin kökü insanı ayakta tutan geçimi adlandırır: {ar:القوام من العيش ما يقيمك ويغنيك, tr:el-kavâmu mine'l-ayşi mâ yükîmüke ve yugnîk, gloss:geçimde kavâm seni ayakta tutan ve muhtaç bırakmayandır, source:"ق و م,B009"}. Bu geçim iki dünyaya birden uzanır: {ar:قياما للناس أي قواما لهم يقوم به معاشهم ومعادهم, tr:kıyâmen li'n-nâs ey kıvâmen lehüm yekûmü bihî meâşühüm ve meâdühüm, gloss:insanlar için ayakta durma vesilesi; yani dünyadaki geçimleri ve dönüşleri onunla ayakta durur, source:"ق و م,B009"}. Altıncı ayetin memnûn kelimesinin kökü ise gökten inen yiyeceği adlandırır: {ar:المن والسلوى... ما أنعم الله به عليهم, tr:el-mennü ve's-selvâ... mâ en'amallâhu bihî aleyhim, gloss:kudret helvası ve bıldırcın; Allah'ın onlara nimet olarak verdiği şeyler, source:"م ن ن,B006"}. Kur'an bu yiyeceği Tûr'daki buluşmayla aynı ayette anar {source:20:80}. Böylece yemin edilen meyvelerden ücrete uzanan bir çizgi belirir. Meyve, yağ, gökten inen yiyecek ve insanı ayakta tutan geçim rızkın türleridir. "Kesilmeyen ücret" bu rızkın tükenmeyen biçimidir.

Kur'an zeytini Allah'ın verdikleri arasında sayar. Yağmurla bitenler arasında {ar:يُنۢبِتُ لَكُم بِهِ ٱلزَّرْعَ وَٱلزَّيْتُونَ, tr:yünbitü leküm bihi'z-zer'a ve'z-zeytûn, gloss:onunla size ekin ve zeytin bitirir, source:16:11} der. Bir başka ayette yağmurla çıkan bitkiler arasında {ar:وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُشْتَبِهًۭا وَغَيْرَ مُتَشَٰبِهٍ, tr:ve'z-zeytûne ve'r-rummâne müştebihen ve gayra müteşâbih, gloss:birbirine benzeyen ve benzemeyen zeytin ve nar, source:6:99} sayılır. İnsana kendi yiyeceğine bakması da söylenir: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânü ilâ ta'âmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Ardından sayılanlar arasında {ar:وَزَيْتُونًۭا وَنَخْلًۭا, tr:ve zeytûnen ve nahlâ, gloss:zeytin ve hurma, source:80:29} da vardır. Orada da Tîn suresindeki gibi insan ile zeytin bir arada durur. Zeytin ışığın misalinde de yer alır: {ar:يُوقَدُ مِن شَجَرَةٍۢ مُّبَٰرَكَةٍۢ زَيْتُونَةٍۢ, tr:yûkadü min şeceratin mübâraketin zeytûne, gloss:mübarek bir zeytin ağacından yakılır, source:24:35}. Aynı ayet {ar:يَكَادُ زَيْتُهَا يُضِىٓءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌۭ, tr:yekâdü zeytühâ yudîü velev lem temseshü nâr, gloss:ateş dokunmasa da yağı neredeyse ışık verir, source:24:35} der. Güvenli belde ile meyve, İbrahim'in duasında birleşir: {ar:رَبِّ ٱجْعَلْ هَٰذَا بَلَدًا ءَامِنًۭا وَٱرْزُقْ أَهْلَهُۥ مِنَ ٱلثَّمَرَٰتِ, tr:rabbic'al hâzâ beleden âminen verzuk ehlehû mine's-semerât, gloss:Rabbim, burayı güvenli bir belde kıl ve halkını meyvelerle rızıklandır, source:2:126}. Ekinsiz bir vadide de aynı dua edilir: {ar:وَٱرْزُقْهُم مِّنَ ٱلثَّمَرَٰتِ لَعَلَّهُمْ يَشْكُرُونَ, tr:verzukhüm mine's-semerâti leallehüm yeşkürûn, gloss:onları meyvelerle rızıklandır ki şükretsinler, source:14:37}. Güven ve rızık Kureyş için de birlikte anılır: {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ellezî et'amehüm min cû'in ve âmenehüm min havf, gloss:onları açlıktan doyuran ve korkudan güvende kılan, source:106:4}. Korkanlara {ar:أَوَلَمْ نُمَكِّن لَّهُمْ حَرَمًا ءَامِنًۭا يُجْبَىٰٓ إِلَيْهِ ثَمَرَٰتُ كُلِّ شَىْءٍۢ, tr:e-ve lem nümekkin lehüm haramen âminen yücbâ ileyhi semerâtü külli şey', gloss:onları her şeyin ürünlerinin toplanıp getirildiği güvenli bir haremde yerleştirmedik mi, source:28:57} diye cevap verilir.

Kur'an bu bolluğun tersine dönüşünü de bir misalle anlatır: {ar:قَرْيَةًۭ كَانَتْ ءَامِنَةًۭ مُّطْمَئِنَّةًۭ يَأْتِيهَا رِزْقُهَا رَغَدًۭا مِّن كُلِّ مَكَانٍۢ فَكَفَرَتْ بِأَنْعُمِ ٱللَّهِ فَأَذَٰقَهَا ٱللَّهُ لِبَاسَ ٱلْجُوعِ وَٱلْخَوْفِ, tr:karyeten kânet âmineten mutmainneten ye'tîhâ rizkuhâ rağaden min külli mekânin fe-keferat bi-en'umillâhi fe-ezâkahallâhu libâse'l-cû'i ve'l-havf, gloss:güvenli ve huzurlu bir kasaba; rızkı her yerden bolca geliyordu; Allah'ın nimetlerine nankörlük etti ve Allah ona açlık ve korku elbisesini tattırdı, source:16:112}. Bu misalde güven, rızık, nimetin inkârı ve düşüş tek bir ayette sırayla gelir.

Kaynaklar: 95:1 وَٱلتِّينِ ت ي ن B001; 95:1 وَٱلزَّيْتُونِ ز ي ت B001; 95:1 وَٱلزَّيْتُونِ ز ي ت B002; 95:1 وَٱلزَّيْتُونِ ز ي ت B003; 95:1 وَٱلزَّيْتُونِ ز ي ت B004; 95:1 وَٱلزَّيْتُونِ ز ي ت B005; 95:4 تَقْوِيمٍ ق و م B009; 95:6 مَمْنُونٍ م ن ن B006

## Buluşmalar

Bu imgelerin en sık buluştuğu yer dördüncü ayetteki takvîm kelimesidir. Dikilen bedenle doğrultulan mızrak aynı kelimede üst üste biner. Arapça bir yandan {ar:انتصاب القامة, tr:intisâbü'l-kâme, gloss:boyun dimdik dikilmesi, source:"ق و م,B011"} der, öbür yandan {ar:رمح قويم, tr:rumhun kavîm, gloss:doğru mızrak, source:"ق و م,B008"}. Ayakta duran insan bir ustanın doğrulttuğu sap gibidir. Altıncı ayette bu sap tamamlanır. Âmil, mızrağın temrene bitişen çalışan kısmıdır {source:"ع م ل,B009"}. Sâlihât, bozulmamış kalan iştir. Ecr hem işin ücretidir hem de, kökünün ailesinde, kemiğin eğri kaynamasının adıdır {source:"ء ج ر,B002"}. Doğruluk ile eğrilik ücret kelimesinde karşılaşır. Ustanın işi, sarrafın tezgâhı ile de kesişir. Aynı kök tam ayardaki altını {ar:دينار قائم, tr:dînârun kâim, gloss:tam ağırlıktaki dinar, source:"ق و م,B015"} diye anar. Redd ise sahte çıkıp sarrafa geri verilen dirhemdir {source:"ر د د,B003"}. Kusurlu iş geri çevrilir, ayarı bozuk para geri verilir. Beşinci ayet bu iki tezgâhta aynı hareketle okunur. Sekizinci ayetin ahkem kelimesi de iki sahneye aittir. Bir işi bozulmaktan korunacak biçimde sağlamlaştırmak ve adaletle hüküm vermek aynı kökten gelir.

İkinci buluşma beşinci ayetin yönündedir. Redd fiili mekânda bir düşüşü, zamanda bir dönüşü anlatır. Kur'an aynı fiili ömrün en düşkün çağı için kullanır {source:22:5}. Esfel kelimesi ateşin en alt katı için de kullanılır {source:4:145}. Bedenin yere inişi ile ömrün başa dönüşü, aynı fiilin iki ayrı ölçekte okunmasıdır. İki sahnenin buluştuğu ayet, Hac suresinin evreleri saydığı ayettir. Evreler sayılır, geri çevrilme anılır, sonra kurumuş toprağın canlanması gösterilir ve hepsi dirilişe şüpheyle bakanlara kanıt olarak sunulur. Böylece inişin sonunda takvîmin kökünden gelen kıyam bekler: {ar:يَوْمَ يَقُومُ ٱلنَّاسُ لِرَبِّ ٱلْعَٰلَمِينَ, tr:yevme yekûmü'n-nâsü li-rabbi'l-âlemîn, gloss:insanların âlemlerin Rabbi için ayağa kalkacağı gün, source:83:6}. Bu ayağa kalkış hâkimin huzurundadır. Redd ile hükmün aynı ayette durduğu sahne, insanların gerçek sahiplerine geri çevrildiği ve hükmün O'na ait olduğunun söylendiği ayettir {source:6:62}. Hüküm kelimesinin kökü de geri döndürmeyi anlatır {source:"ح ك م,B007"}. Beşinci ayetin aşağı indiren eli, sekizinci ayetin hükmeden eliyle aynıdır.

Üçüncü buluşma kesilmeyen ücret ile tükeniş arasındadır. Menn kökü ipin kesilmesini, ömrün ölümle bitişini ve yolcunun yorgunluktan yolda kalmasını adlandırır. Ücretin "kesilmemesi" bunların hepsine karşı durur. Dayanma imgesi aynı yere bağlanır. Güvenilir deve emûn ile kesilen süt (kezebe) aynı zıtlığın iki yanıdır. Güven kökünden gelen emîn, gevşemesinden korkulmayan binektir. Yalan kökünden gelen kezebe ise beklenen süreyi dolduramayan süttür. Böylece üçüncü ayetin güvenliği ile yedinci ayetin yalanlaması, dayanan ile tükenen olarak birbirinin karşısına düşer. Beşinci ayetteki iniş, ömrün ve dayanma gücünün kesildiği yerdir. Altıncı ayet, inişin içinden kesilmeyen bir çizgi çeker.

Dördüncü buluşma yaratılış ile dindir. Rum suresinde yüzü doğrultma emri, din, Allah'ın yaratışı ve kayyim kelimesi tek bir ayette birleşir {source:30:30}. Tîn suresi de bu kelimeleri dağıtarak ilerler. Dördüncü ayette yaratış ve doğrultma vardır, yedinci ayette din. Aradaki beşinci ayetin redd fiili, ailesinde dinden dönmeyi (irtidâd) taşır. Altıncı ayet ise bu doğrultuda kalanları sayar. İnfitâr suresi aynı sırayı daha kısa kurar: düzgün kılma ve dengelemenin ardından {ar:كَلَّا بَلْ تُكَذِّبُونَ بِٱلدِّينِ, tr:kellâ bel tükezzibûne bi'd-dîn, gloss:hayır, siz dini yalanlıyorsunuz, source:82:9} gelir. Halk kelimesinin kökü burada ikiye ayrılır. Allah'ın yaratması gerçek yapımdır. İnsanın uydurması ise yalanın yapımıdır {source:"خ ل ق,B007"}. Yedinci ayetin sorusu bu iki yapımı yüz yüze getirir.

Beşinci buluşma mekândadır. Yemin edilen belde güven ve rızık yeridir. İbrahim'in duasında güvenli belde ile meyveler bir aradadır {source:2:126}. Tûr'da Musa ateşi fark eder ve korkudan güvene çağrılır {source:28:31}. Bu yerler, insanın yaratılışını anlatan ayetlere bir zemin hazırlar. Belde kelimesinin ailesi ise aynı zemini öbür yüzüyle de gösterir. Çöken devenin göğsünü yere koyması, yere yapışan beden, mezar ve toprak bu ailededir. Kasaba misali, iki yüzü tek bir hikâyede gösterir. Güvenli ve rızkı bol bir kasaba nimeti inkâr eder ve açlık ile korku elbisesine bürünür {source:16:112}. Tîn suresinin hareketi de buna benzer. Güvenli beldede yemin edilir, insan en güzel duruşla dikilir, aşağıların en aşağısına geri çevrilir, iman edip işini sağlam yapanlar kesilmeyen ücretle bu inişin dışında kalır. Sonra yalanlamaya ne kaldığı sorulur ve hüküm verenlerin en iyisinin önünde "evet" cevabını bekleyen bir soruyla sure kapanır.

