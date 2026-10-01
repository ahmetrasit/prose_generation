Focus: 100:9. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/OZTURK/_projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. No other command or tool is available.

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


===== _commentary/v16/work/100_9/D.r13/context.md =====
# 100:9 — focus

۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ

Anchor translation (canonical reading, reference only):

Öyleyse bilmez mi ki mezarlarda olanlar dışarı çıkarıldığında,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | أَفَلَا | لَا |  | INTG;SUP;NEG |
| 2 | يَعْلَمُ | عَلِمَ | ع ل م | V |
| 3 | إِذَا | إِذَا |  | T |
| 4 | بُعْثِرَ | بُعْثِرَ | ب ع ث ر | V |
| 5 | مَا | مَا |  | REL |
| 6 | فِى | فِى |  | P |
| 7 | ٱلْقُبُورِ | قَبْر | ق ب ر | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 100 — full text (context; no pericope)

- 100:1 وَٱلْعَٰدِيَٰتِ ضَبْحًۭا
- 100:2 فَٱلْمُورِيَٰتِ قَدْحًۭا
- 100:3 فَٱلْمُغِيرَٰتِ صُبْحًۭا
- 100:4 فَأَثَرْنَ بِهِۦ نَقْعًۭا
- 100:5 فَوَسَطْنَ بِهِۦ جَمْعًا
- 100:6 إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ
- 100:7 وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ
- 100:8 وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ
- 100:9 ◀ focus ۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ
- 100:10 وَحُصِّلَ مَا فِى ٱلصُّدُورِ
- 100:11 إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ


===== _commentary/v16/work/100_9/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع ل م (root_001040) — identity root of يَعْلَمُ (w2)

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

## ب ع ث ر (root_000130) — identity root of بُعْثِرَ (w4)

- **B001** toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma — toprağı altüst edip gömülüyü ortaya çıkarmak; örtülü şeyi çıkarıp açığa kavuşturmak · gömülüyü ortaya çıkarmak için toprağı altüst etme
  بعثره بعثرة إذا قلب التراب عنه (ayn)؛ بعثر ما في القبور أثير وأخرج؛ بعثرت الشيء إذا استخرجته وكشفته (sihah)؛ قلب ترابها وأثير ما فيها (mufradat)
- **B002** eşyayı dağıtıp altüst etme [kalıp] — eşyasını ayırıp dağıtmak ve parçalarını birbirinin üstüne gelecek biçimde altüst etmek
  بعثر الرجل متاعه وبحثره إذا فرقه وبدده وقلب بعضه على بعض
- **B003** havuzu yıkıp altını üste çevirme [kalıp] — havuzunu yıkıp alt bölümünü üste gelecek biçimde ters çevirmek
  بعثرت حوضي أي هدمته وجعلت أسفله أعلاه

## ق ب ر (root_001195) — identity root of ٱلْقُبُورِ (w7)

- **B001** ölüyü gömme, ona gömü yeri sağlama ve gömü yeri — ölünün gömüldüğü yer; gömüt · ölüyü gömmek ve gömü yerine koymak · ölüyü gömü yerine koyma işi · ölüye gömü yeri sağlamak, gömülmesine izin vermek veya onu gömülecek duruma getirmek · ölü için gömü yeri hazırlama ve onu gömülmeye layık sayılanlar arasına koyma · onu gömmemize izin ver · ölüyü kendi eliyle gömen kimse · gömütlerin bulunduğu yer; mezarlık · gömüt yeri veya gömütlerin bulunduğu yer · gömme işi · ölüye gömü yeri veren · gömütler; mezarlıklar · mezarlığa veya gömüt yerine ilişkin · gömüt kazısında sana yardım eden kişi
  القبر قبر الميت (maqayis)؛ القبر مدفن الإنسان (tahdhib)؛ القبر مقر الميت (mufradat)؛ قبرت الميت أي دفنته (jamhara;sihah;tahdhib)؛ أقبرته جعلت له مكانا يقبر فيه (maqayis;mufradat)؛ المقبرة موضع القبور (ayn;jamhara;tahdhib;mufradat)
- **B002** gizli, alçakta veya içe gömülü kalma — çukurda ve gözden ırak arazi · ürünü yapraklarının arasında saklı duran hurma ağacı · hoş kokulu ağacın içinde gevşeyip aşınmış oyuk bölüm · üzerinde yarıksız ve deliksiz kapalı bir zarla doğan çocuk
  أصل صحيح يدل على غموض في شيء وتطامن (maqayis)؛ أرض قبور غامضة (maqayis;jamhara;tahdhib)؛ نخلة قبور وكبوس يكون حملها في سعفها (maqayis;jamhara;tahdhib)؛ القبر موضع متأكل مسترخى في العود الذي يتطيب به وهو جوفه (ayn)؛ ولد مقبورا لأن عليه جلدة مصمتة ليس فيها شق ولا ثقب (tahdhib)
- **B003** belirli bir kuş türünün adı — belirli bir kuş türünün tekil adı · aynı kuşun adı veya çoğul biçimi · aynı kuş adının değişik söylenişi · aynı kuş için kullanılan başka bir ad biçimi
  القبرة واحدة القبر وهو ضرب من الطير (sihah)؛ القنبراء لغة فيها (sihah)؛ يقال للقنبرة قبرة وقبر (tahdhib)
- **B004** burun ucu ve öfkeli gelişte burnun belirginleşmesi — burun ucu · çıkıntılı burnun baş kısmı için kullanılan küçültme biçimi · burnu öne çıkmış biçimde öfkeli gelmek · burnu kabarmış halde öfkeli gelmek
  جاء فلان رامعا قبراه ورامعا أنفه إذا جاء مغضبا (tahdhib)؛ جاءنا فخا قبراه (tahdhib)؛ القبراة أيضا طرف الأنف (tahdhib)؛ القبيرة تصغير القبرة وهي رأس القنفاء (tahdhib)
- **B005** gömülme üzerinden ölüm, gizlilik ve ölü hükmünde olma — ölmek · gömülerde saklı olanların dirilişte veya sırlar açığa çıkarken ortaya çıkarılması · gömülmüşçesine gizli · bilgisizliğe gömülmüş · ölü hükmünde olanlar
  حتى زرتم المقابر كناية عن الموت (mufradat)؛ إذا بعثر ما في القبور إشارة إلى حال البعث (mufradat)؛ أحوال الإنسان ما دام في الدنيا مستورة كأنها مقبورة (mufradat)؛ الكافر والجاهل ما دام في الدنيا فهو مقبور (mufradat)؛ من في القبور أي الذين هم في حكم الأموات (mufradat)

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 100:9, and ## Buluşmalar) =====
## Toprağı altüst etmek

Dördüncü ayetin fiili tozu havaya kaldırmanın yanında toprağı ayakla eşelemeyi de anlatır: {ar:أثار الثور التراب إذا بحثه بقوائمه, tr:esâra's-sevru't-turâbe izâ behasehû bi-kavâimih, gloss:boğa toprağı ayaklarıyla eşeleyince "toprağı kaldırdı" denir, source:"ث و ر,B002"}. Aynı fiil toprağı sürmeyi de karşılar: {ar:أثرت الأرض إثارة, tr:esartu'l-arda isâraten, gloss:toprağı alt üst ettim, sürdüm, source:"ث و ر,B002"}. Kökün hayvanı da tarlayı süren öküzdür: {ar:والثور البقر الذي يثار به الأرض, tr:ve's-sevru'l-bakaru'llezî yusâru bihi'l-ard, gloss:"sevr", toprağın onunla sürüldüğü sığırdır, source:"ث و ر,B004"}. Kökün özü saklı duran bir şeyin fışkırmasıdır: {ar:أصل انبعاث الشيء, tr:aslu'nbi'âsi'ş-şey', gloss:bir şeyin harekete geçip fırlamasının aslı, source:"ث و ر,B001"}. Bu fışkırmanın örnekleri arasında çekirgeler de sayılır: {ar:وثار الجراد, tr:ve sâra'l-cerâd, gloss:çekirgeler havalandı, source:"ث و ر,B001"}. Toynaklar toprağa vurdukça yüzey dağılır, alttaki toprak üste çıkar ve havaya karışır.

Dokuzuncu ayet aynı hareketi mezarlara taşır: {ar:أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ, tr:e-fe-lâ ya'lemu izâ bu'sira mâ fi'l-kubûr, gloss:bilmez mi ki kabirlerde olan şey altüst edilip çıkarıldığında, source:100:9}. "Bu'sira" ile dördüncü ayetin "eserne"si ayrı köklerdendir. Ama bu fiil Arapçada tam da dördüncü ayetin fiiliyle açıklanır: {ar:بعثر ما في القبور أثير وأخرج, tr:bu'sira mâ fi'l-kubûr: usîra ve uhrice, gloss:kabirlerdekiler "bu'sira" oldu, yani kaldırılıp çıkarıldı, source:"ب ع ث ر,B001"}. Bir başka açıklama, toprağın çevrilmesini daha da açık söyler: {ar:قلب ترابها وأثير ما فيها, tr:kulibe turâbuhâ ve usîra mâ fîhâ, gloss:toprağı ters çevrildi ve içindekiler kaldırıldı, source:"ب ع ث ر,B001"}. Kalıplaşmış bir söyleyiş bu altüst oluşun tam resmini çizer: {ar:بعثرت حوضي أي هدمته وجعلت أسفله أعلاه, tr:ba'sertu havdî, ey hedemtuhû ve ce'altu esfelehû a'lâh, gloss:havuzumu "ba'sere" ettim, yani yıktım, altını üstüne getirdim, source:"ب ع ث ر,B003"}. Bir yük de aynı biçimde dağıtılabilir: {ar:بعثر الرجل متاعه وبحثره إذا فرقه وبدده وقلب بعضه على بعض, tr:ba'sera'r-raculu metâ'ahû ve bahserahû izâ ferrakahû ve beddedehû ve kalebe ba'dahû alâ ba'd, gloss:adam eşyasını dağıtıp saçınca ve birbirine katınca "ba'sere" denir, source:"ب ع ث ر,B002"}. Kabir hem bir duraktır, {ar:القبر مقر الميت, tr:el-kabru makarru'l-meyyit, gloss:kabir, ölünün karar kıldığı yerdir, source:"ق ب ر,B001"}, hem de bir saklanma yeridir: {ar:أصل صحيح يدل على غموض في شيء وتطامن, tr:aslun sahîhun yedullu alâ gumûdın fî şey'in ve tatâmun, gloss:bir şeydeki kapalılığa ve çöküklüğe delalet eden sağlam bir kök, source:"ق ب ر,B002"}. Ayet "kabirlerdeki kimseler" demez, "kabirlerde olan şey" der. Bu "mâ" kelimesi kabirlerin içindekini, bir yüke ya da gömülü bir hazineye benzer biçimde, bir içerik olarak gösterir.

İkinci ayetin kökü bu sahneye beklenmedik bir yerden katılır. Ateşi çıkaran kök, bir şeyi örtüp gizlemeyi de anlatır: {ar:واريت الشيء أي أخفيته وتوارى هو أي استتر, tr:vâraytu'ş-şey', ey ahfeytuh, ve tevârâ huve, ey isteter, gloss:"vâraytu", yani onu gizledim; "tevârâ", yani o gizlendi, source:"و ر ي,B005"}. Kur'an bu kökü ilk gömme sahnesinde kullanır. Kardeşini öldüren Âdem oğluna, Allah toprağı eşeleyen bir karga gönderir: {ar:فَبَعَثَ ٱللَّهُ غُرَابًا يَبْحَثُ فِى ٱلْأَرْضِ لِيُرِيَهُۥ كَيْفَ يُوَٰرِى سَوْءَةَ أَخِيهِ, tr:fe-be'asa'llâhu ğurâben yebhasu fi'l-ardı li-yuriyehû keyfe yuvârî sev'ete ahîh, gloss:Allah, kardeşinin cesedini nasıl örteceğini ona göstermek için toprağı eşeleyen bir karga gönderdi, source:5:31}. Karganın toprağı eşelemesi için kullanılan fiil ("yebhasu"), boğanın toprağı ayaklarıyla kaldırmasını anlatan söyleyişteki fiille ("behasehû") aynıdır. Gömmek, toprağı açıp sonra kapatmaktır. Dokuzuncu ayet bu işi tersine işletir: toprak yeniden açılır ve örtülen şey dışarı çıkar. Gizleyen ve ateşi çıkaran aynı kökün iki anlamı, böylece surenin başında ve sonunda iki ayrı yerde iş görür.

Onuncu ayetin fiili de toprakla başlar: {ar:أصل التحصيل استخراج الذهب أو الفضة من الحجر أو من تراب المعدن, tr:aslu't-tahsîli istihrâcu'z-zehebi evi'l-fiddati mine'l-haceri ev min turâbi'l-ma'den, gloss:"tahsîl"in aslı, altını ya da gümüşü taştan veya maden toprağından çıkarmaktır, source:"ح ص ل,B002"}. Bu işi yapan kişinin de bir adı vardır: {ar:المحصلة المرأة التي تحصل تراب المعدن, tr:el-muhassılatu'l-mer'etu'lletî tuhassılu turâbe'l-ma'den, gloss:"muhassıla", maden toprağını ayıklayan kadındır, source:"ح ص ل,B002"}. Maden toprağı kazılır, yıkanır, elenir ve içindeki değerli metal ayrılır. Görüntünün sırası, sure ayetlerinin sırasıyla örtüşür: önce toprak kaldırılır, ardından içindeki değerli olan ayrılır.

Kur'an bu sahneyi başka surelerde de kurar. Göğün yarılıp denizlerin taştığı anlatılırken şöyle denir: {ar:وَإِذَا ٱلْقُبُورُ بُعْثِرَتْ, tr:ve izâ'l-kubûru bu'siret, gloss:kabirler altüst edildiğinde, source:82:4}. Bunu hemen bilgi izler: {ar:عَلِمَتْ نَفْسٌ مَّا قَدَّمَتْ وَأَخَّرَتْ, tr:alimet nefsun mâ kaddemet ve ahharat, gloss:her can neyi öne sürüp neyi geride bıraktığını bilir, source:82:5}. Bizim surede aynı fiil "bilmez mi" sorusunun içinde geçer. Başka bir surede yer sarsılır ve {ar:وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا, tr:ve ahraceti'l-ardu eskâlehâ, gloss:yer ağırlıklarını dışarı çıkardı, source:99:2}. Bir başkasında yer uzatılır, {ar:وَأَلْقَتْ مَا فِيهَا وَتَخَلَّتْ, tr:ve elkat mâ fîhâ ve tehallet, gloss:içindekini atıp boşaldı, source:84:4}. Bu son ifadede de "mâ fîhâ", yani "içindeki" söz konusudur. Hac suresinde bu sahne açık bir hükümdür: {ar:وَأَنَّ ٱللَّهَ يَبْعَثُ مَن فِى ٱلْقُبُورِ, tr:ve enna'llâhe yeb'asu men fi'l-kubûr, gloss:ve Allah kabirlerdekileri diriltecektir, source:22:7}. Musa'nın Firavun'a söylediği sözlerin arasında toprağın üç işlevi tek ayette sayılır: {ar:مِنْهَا خَلَقْنَٰكُمْ وَفِيهَا نُعِيدُكُمْ وَمِنْهَا نُخْرِجُكُمْ تَارَةً أُخْرَىٰ, tr:minhâ halaknâkum ve fîhâ nu'îdukum ve minhâ nuhricukum târaten uhrâ, gloss:sizi ondan yarattık, sizi oraya döndüreceğiz ve sizi bir kez daha oradan çıkaracağız, source:20:55}. Kökün "havalanan çekirge" anlamı da diriliş sahnesinde Kur'an'ın kendi benzetmesiyle karşılanır: {ar:يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ كَأَنَّهُمْ جَرَادٌ مُّنتَشِرٌ, tr:yahrucûne mine'l-ecdâsi ke-ennehum cerâdun munteşir, gloss:kabirlerden yayılmış çekirgeler gibi çıkarlar, source:54:7}. Toprağı sürmek ise Kur'an'da dünyaya yapılan yatırımın ölçüsüdür. Eski kavimler hakkında {ar:وَأَثَارُوا۟ ٱلْأَرْضَ وَعَمَرُوهَآ أَكْثَرَ مِمَّا عَمَرُوهَا, tr:ve esârû'l-arda ve amerûhâ ekser mimmâ amerûhâ, gloss:toprağı sürdüler ve onu bunların imar ettiğinden daha çok imar ettiler, source:30:9} denir. İsrailoğullarından boğazlanması istenen inek de {ar:لَّا ذَلُولٌ تُثِيرُ ٱلْأَرْضَ, tr:lâ zelûlun tusîru'l-ard, gloss:toprağı sürmeye koşulmamış, source:2:71} diye tarif edilir.

Kaynaklar: 100:4 فَأَثَرْنَ ث و ر B002; 100:4 فَأَثَرْنَ ث و ر B004; 100:4 فَأَثَرْنَ ث و ر B001; 100:9 بُعْثِرَ ب ع ث ر B001; 100:9 بُعْثِرَ ب ع ث ر B003; 100:9 بُعْثِرَ ب ع ث ر B002; 100:9 ٱلْقُبُورِ ق ب ر B001; 100:9 ٱلْقُبُورِ ق ب ر B002; 100:2 فَٱلْمُورِيَٰتِ و ر ي B005; 100:10 وَحُصِّلَ ح ص ل B002; 5:31; 82:4; 82:5; 99:2; 84:4; 22:7; 20:55; 54:7; 30:9; 2:71

## Özü kabuğundan ayırmak

Onuncu ayetin fiili bir ayıklama işidir: {ar:وَحُصِّلَ مَا فِى ٱلصُّدُورِ, tr:ve hussıle mâ fi's-sudûr, gloss:ve göğüslerde olan ayıklanıp ortaya konduğunda, source:100:10}. Fiilin aslı üç ayrı ayıklamayı tek bir tanıma toplar: {ar:التحصيل إخراج اللب من القشور كإخراج الذهب من حجر المعدن والبر من التبن, tr:et-tahsîlu ihrâcu'l-lubbi mine'l-kuşûr, ke-ihrâci'z-zehebi min haceri'l-ma'deni ve'l-burri mine't-tibn, gloss:"tahsîl", özü kabuklardan çıkarmaktır; altını maden taşından, buğdayı samandan çıkarmak gibi, source:"ح ص ل,B002"}. İşin kendisi bir ayırt etmedir: {ar:التحصيل تمييز ما يحصل, tr:et-tahsîlu temyîzu mâ yahsul, gloss:"tahsîl", elde kalanı ayırt etmektir, source:"ح ص ل,B002"}. Geriye kalan şey ise ötekiler gidince sabit kalandır: {ar:حصل يحصل حصولا أي بقي وثبت وذهب ما سواه من حساب أو عمل, tr:hasale yahsulu husûlen, ey bekıye ve sebete ve zehebe mâ sivâhu min hısâbin ev amel, gloss:"hasale", yani hesapta ya da işte geri kalanlar gidip kendisi kaldı ve sabitlendi, source:"ح ص ل,B001"}. Bu bir hesabın son satırıdır: {ar:أظهر ما فيها وجمع أو إظهار الحاصل من الحساب, tr:azhara mâ fîhâ ve ceme'a ev izhâru'l-hâsıli mine'l-hısâb, gloss:içindekini açığa çıkardı ve topladı; ya da hesaptan kalan toplamı ortaya koymak, source:"ح ص ل,B001"}. Ayetteki fiil edilgen ve şeddelidir. Bu kalıp işin emekle, adım adım yapıldığını duyurur. Ayıklayanın adı anılmaz, yalnızca ayıklanan şey öne çıkar. Aynı kökün kuş dünyasında da bir karşılığı vardır: {ar:حوصلة الطائر لأنه يجمع فيها, tr:havsaletu't-tâiri li-ennehû yecma'u fîhâ, gloss:kuşun kursağı; çünkü yediklerini orada toplar, source:"ح ص ل,B004"}. Göğüs de böyle bir kursaktır, yıllar boyunca içine alınanların biriktiği bir kap. Kur'an'da göğüs insanın içini taşıyan kaptır: {ar:الصدر للإنسان والجمع صدور, tr:es-sadru li'l-insâni ve'l-cem'u sudûr, gloss:insanın göğsü; çoğulu "sudûr", source:"ص د ر,B001"}.

Sekizinci ayetteki sevgi kelimesinin ailesi bu ayıklama sahnesinde yerini alır. Kelimenin yanında tane duyulur: {ar:الحب والحبة في الحنطة والشعير وبزور الرياحين, tr:el-habbu ve'l-habbetu fi'l-hıntati ve'ş-şa'îri ve buzûri'r-reyâhîn, gloss:buğdayda, arpada ve kokulu bitki tohumlarında tane, source:"ح ب ب,B001"}. Kalbin içinde de bir tane vardır: {ar:حبة القلب سويداؤه ويقال ثمرته, tr:habbetu'l-kalbi suveydâuhû ve yukâlu semeratuh, gloss:kalbin tanesi onun kara noktasıdır, meyvesi de denir, source:"ح ب ب,B004"}. Bu tane kalbin en içindedir: {ar:حبة القلب هي العلقة السوداء التي تكون داخل القلب, tr:habbetu'l-kalbi hiye'l-alakatu's-sevdâu'lletî tekûnu dâhile'l-kalb, gloss:kalbin tanesi, kalbin içindeki kara pıhtıdır, source:"ح ب ب,B004"}. İki kök harman yerinde buluşur: {ar:الحصالة ما يبقى في الأندر من الحب بعد ما يرفع الحب وهو الكناسة, tr:el-husâletu mâ yebkâ fi'l-enderi mine'l-habbi ba'de mâ yurfe'u'l-habbu ve huve'l-kunâse, gloss:"husâle", tane kaldırıldıktan sonra harmanda kalan süprüntüdür, source:"ح ص ل,B003"}. Bu yan yana gelişler şunu duyurur: insanın şiddetle bağlandığı sevgi, göğsün içindeki tanedir ve ayıklanacak olan da odur. Harman savrulunca tane bir yana, saman öbür yana gider.

Surenin son kelimesi bu ayıklamanın hangi bilgiye dayandığını söyler: {ar:الخبرة المعرفة ببواطن الأمر, tr:el-hibratu'l-ma'rifetu bi-bevâtıni'l-emr, gloss:"hibre", işin iç yüzünü bilmektir, source:"خ ب ر,B001"}. Aynı kökte içi dışından ayıran bir karşıtlık da vardır: {ar:المخبر خلاف المنظر, tr:el-mahbaru hılâfu'l-manzar, gloss:"mahber" (iç yüz), "manzar"ın (görünüşün) karşıtıdır, source:"خ ب ر,B001"}. Dokuzuncu ile onuncu ayet aynı kalıpla kurulmuştur: "kabirlerde olan" ve "göğüslerde olan". Kabir kelimesinin bir açıklaması iki ayeti doğrudan birbirine bağlar: {ar:أحوال الإنسان ما دام في الدنيا مستورة كأنها مقبورة, tr:ahvâlu'l-insâni mâ dâme fi'd-dunyâ mesturatun ke-ennehâ makbûra, gloss:insan dünyada oldukça halleri örtülüdür, sanki gömülüdürler, source:"ق ب ر,B005"}. Önce bedenler topraktan çıkar, sonra göğüslerde gömülü olan ayıklanır. Düz bir anlatım "kalpteki her şey açığa çıkacak" demekle yetinirdi. Bu görüntü ise o açığa çıkışı bir işçilik olarak gösterir: kabuk soyulur, tane ayrılır, hesap son satırına kadar indirilir.

Kur'an göğüslerdekinin sınanmasını Uhud'dan sonra, inananlara indirilen ayette anlatır. Bir kısmı huzurlu bir uykuya dalmışken bir kısmı kendi derdine düşmüştü ve {ar:يُخْفُونَ فِىٓ أَنفُسِهِم مَّا لَا يُبْدُونَ لَكَ, tr:yuhfûne fî enfusihim mâ lâ yubdûne lek, gloss:sana açmadıklarını içlerinde gizliyorlardı, source:3:154}. Ayet şöyle sürer: {ar:وَلِيَبْتَلِىَ ٱللَّهُ مَا فِى صُدُورِكُمْ وَلِيُمَحِّصَ مَا فِى قُلُوبِكُمْ, tr:ve li-yebteliya'llâhu mâ fî sudûrikum ve li-yumahhısa mâ fî kulûbikum, gloss:Allah göğüslerinizdekini sınasın ve kalplerinizdekini arıtsın diye, source:3:154}. "Mâ fî sudûrikum" ifadesi bizim ayetin ifadesiyle aynıdır. Yanında yer alan "arıtma" fiili de bir ayıklama işidir. Allah'ın elçisine şunu söylemesi de buyrulur: {ar:قُلْ إِن تُخْفُوا۟ مَا فِى صُدُورِكُمْ أَوْ تُبْدُوهُ يَعْلَمْهُ ٱللَّهُ, tr:kul in tuhfû mâ fî sudûrikum ev tubdûhu ya'lemhu'llâh, gloss:de ki: göğüslerinizdekini gizleseniz de açığa vursanız da Allah onu bilir, source:3:29}. Kalplerinde hastalık olanlara {ar:أَمْ حَسِبَ ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌ أَن لَّن يُخْرِجَ ٱللَّهُ أَضْغَٰنَهُمْ, tr:em hasibe'llezîne fî kulûbihim maradun en len yuhrica'llâhu adğânehum, gloss:kalplerinde hastalık olanlar, Allah'ın kinlerini dışarı çıkarmayacağını mı sandılar, source:47:29} diye sorulur. Gecenin yıldızı üzerine yeminle başlayan surede ise o gün kısaca {ar:يَوْمَ تُبْلَى ٱلسَّرَآئِرُ, tr:yevme tublâ's-serâir, gloss:gizlilerin sınandığı gün, source:86:9} diye anılır. Ayıklamanın inceliği de zerre ölçüsüyle verilir: {ar:فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًا يَرَهُۥ, tr:fe-men ya'mel miskâle zerratin hayran yerah, gloss:kim zerre ağırlığınca hayır işlerse onu görür, source:99:7}.

Kaynaklar: 100:10 وَحُصِّلَ ح ص ل B002; 100:10 وَحُصِّلَ ح ص ل B001; 100:10 وَحُصِّلَ ح ص ل B003; 100:10 وَحُصِّلَ ح ص ل B004; 100:10 ٱلصُّدُورِ ص د ر B001; 100:8 لِحُبِّ ح ب ب B001; 100:8 لِحُبِّ ح ب ب B004; 100:11 لَّخَبِيرٌ خ ب ر B001; 100:9 ٱلْقُبُورِ ق ب ر B005; 3:154; 3:29; 47:29; 86:9; 99:7

## Görmek, bilmek, içini bilmek

Surenin ikinci yarısı üç bilme biçimini sırayla dizer. Yedinci ayette insan tanıktır, dokuzuncu ayette bilip bilmediği sorulur, on birinci ayette ise Rabbinin onlardan haberdar olduğu söylenir. Tanıklığın kökü hazır bulunmak ve görmektir: {ar:الشهود والشهادة الحضور مع المشاهدة, tr:eş-şuhûdu ve'ş-şehâdetu'l-huzûru me'a'l-muşâhede, gloss:"şuhûd" ve "şehâdet", görerek hazır bulunmaktır, source:"ش ه د,B001"}. Tanıklık üç şeyi bir arada tutar: {ar:الشهادة يجمع الحضور والعلم والإعلام, tr:eş-şehâdetu yecma'u'l-huzûra ve'l-ilme ve'l-i'lâm, gloss:şahitlik, hazır bulunmayı, bilmeyi ve bildirmeyi bir araya getirir, source:"ش ه د,B002"}. Tanıklık aynı zamanda bir haberdir: {ar:الشهادة خبر قاطع, tr:eş-şehâdetu haberun kâtı', gloss:şahitlik kesin bir haberdir, source:"ش ه د,B002"}. Kökün ailesinde tanığın aleti de vardır: {ar:الشاهد اللسان, tr:eş-şâhidu'l-lisân, gloss:"şâhid", dildir, source:"ش ه د,B005"}. Dokuzuncu ayetin bilme fiili ise bir şeyi gerçeğiyle kavramaktır: {ar:إدراك الشيء بحقيقته, tr:idrâku'ş-şey'i bi-hakîkatih, gloss:bir şeyi hakikatiyle kavramak, source:"ع ل م,B001"}. Bu fiil de haberle bağlantılıdır: {ar:ما علمت بخبرك أي ما شعرت به, tr:mâ alimtu bi-haberik, ey mâ şa'artu bih, gloss:"haberini bilmedim", yani farkına varmadım, source:"ع ل م,B001"}. Son ayetin kelimesi bu iki bilgiyi bir araya getirir: {ar:الخبير العالم, tr:el-habîru'l-âlim, gloss:"habîr", bilendir, source:"خ ب ر,B001"}.Bu bilgi deneyerek kazanılır: {ar:الخبرة الاختبار, tr:el-hibratu'l-ihtibâr, gloss:"hibre", sınayarak denemektir, source:"خ ب ر,B001"}. Ulaştığı yer de işin iç yüzüdür: {ar:الخبرة المعرفة ببواطن الأمر, tr:el-hibratu'l-ma'rifetu bi-bevâtıni'l-emr, gloss:"hibre", işin iç yüzünü bilmektir, source:"خ ب ر,B001"}. Altıncı ayetteki insan kelimesinin kökü de bu sıralamanın başına bir duyu ekler: {ar:آنست الشيء إذا رأيته وآنسته إذا سمعته, tr:ânestu'ş-şey'e izâ raeytehû ve ânestuhû izâ semi'teh, gloss:bir şeyi gördüğünde de işittiğinde de "ânestu" dersin, source:"ء ن س,B002"}. Kök görmekten bilmeye kadar uzanır: {ar:آنست منه رشدا علمته, tr:ânestu minhu ruşden, alimtuh, gloss:"ondan bir olgunluk sezdim", yani onu öğrendim, source:"ء ن س,B002"}. Su başı deyimi de aynı yolu izler. Çok göletten içen kişi, işleri deneye deneye {ar:حتى خبرها, tr:hattâ haberahâ, gloss:sonunda iç yüzlerini öğrendi, source:"ن ق ع,B008"} diye anılır.

Bu yolun sure içinde aldığı biçim şöyledir. Yedinci ayette insan hazırdır ve görmektedir. Kendi nankörlüğüne tanıktır, yani bilgisi gözünün önündedir. Dokuzuncu ayet buna rağmen bir soru sorar: {ar:أَفَلَا يَعْلَمُ, tr:e-fe-lâ ya'lem, gloss:bilmez mi, source:100:9}. Bu soru, görmekle bilmek arasındaki boşluğu açığa çıkarır. İnsan kendi halini görür ama bu halin nereye varacağını hakikatiyle kavramaz. Sure soruya cevap vermez. Cevabın yerine Rabbin bilgisini koyar: {ar:إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍ لَّخَبِيرٌ, tr:inne rabbehum bihim yevme'izin le-habîr, gloss:şüphesiz Rableri o gün onlardan tamamen haberdardır, source:100:11}. Ayet "yaptıklarından" demez, "onlardan" der. Bilginin konusu insanın kendisidir. "Habîr" kelimesi görünüşe değil iç yüze bakar. Böylece surenin bilgi sırası, insanın kendi dışını görmesinden Rabbin onun içini bilmesine doğru ilerler.

Kur'an aynı kuruluşu bir başka surede de kullanır. Allah sözü gizlenen ile açığa vurulanı bir tutar: {ar:وَأَسِرُّوا۟ قَوْلَكُمْ أَوِ ٱجْهَرُوا۟ بِهِۦٓ ۖ إِنَّهُۥ عَلِيمٌ بِذَاتِ ٱلصُّدُورِ, tr:ve esirrû kavlekum evi'cherû bih, innehû alîmun bi-zâti's-sudûr, gloss:sözünüzü gizleyin ya da açığa vurun; O, göğüslerin içindekini bilendir, source:67:13}. Ardından bir soru gelir: {ar:أَلَا يَعْلَمُ مَنْ خَلَقَ وَهُوَ ٱللَّطِيفُ ٱلْخَبِيرُ, tr:e-lâ ya'lemu men halak, ve huve'l-latîfu'l-habîr, gloss:yaratan bilmez mi? O, en ince şeyi bilen ve her şeyden haberdar olandır, source:67:14}. Göğüsler, "bilmez mi" sorusu ve "habîr" bu iki ayette de bu sırayla dizilir. Ancak soru orada yaratanın bilgisi üzerine sorulur, bizim surede ise insanın bilgisi üzerine. Bir başka yerde insan kendi kendisinin tanığıdır: {ar:يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍ بِمَا قَدَّمَ وَأَخَّرَ, tr:yunebbeu'l-insânu yevme'izin bimâ kaddeme ve ahhar, gloss:o gün insana öne sürdüğü ve geride bıraktığı bildirilir, source:75:13}; {ar:بَلِ ٱلْإِنسَٰنُ عَلَىٰ نَفْسِهِۦ بَصِيرَةٌ, tr:beli'l-insânu alâ nefsihî basîra, gloss:aslında insan kendi kendine karşı bir göz, bir tanıktır, source:75:14}; {ar:وَلَوْ أَلْقَىٰ مَعَاذِيرَهُۥ, tr:ve lev elkâ meâzîreh, gloss:mazeretlerini ortaya dökse bile, source:75:15}. Kökün "dil" anlamı da o günün tanıklığında yer alır: {ar:يَوْمَ تَشْهَدُ عَلَيْهِمْ أَلْسِنَتُهُمْ وَأَيْدِيهِمْ وَأَرْجُلُهُم بِمَا كَانُوا۟ يَعْمَلُونَ, tr:yevme teşhedu aleyhim elsinetuhum ve eydîhim ve erculuhum bimâ kânû ya'melûn, gloss:o gün dilleri, elleri ve ayakları yaptıklarına dair aleyhlerine tanıklık eder, source:24:24}. Bedenin kendi derisine sorduğu soru da kaydedilir: {ar:وَقَالُوا۟ لِجُلُودِهِمْ لِمَ شَهِدتُّمْ عَلَيْنَا ۖ قَالُوٓا۟ أَنطَقَنَا ٱللَّهُ ٱلَّذِىٓ أَنطَقَ كُلَّ شَىْءٍ, tr:ve kâlû li-culûdihim lime şehidtum aleynâ, kâlû entakanâ'llâhu'llezî entaka kulle şey', gloss:derilerine "neden aleyhimize tanıklık ettiniz" derler; onlar da "her şeyi konuşturan Allah bizi konuşturdu" der, source:41:21}. İnsanın içine dair bilgi en yakın yerden gelir: {ar:وَلَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ وَنَعْلَمُ مَا تُوَسْوِسُ بِهِۦ نَفْسُهُۥ ۖ وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ, tr:ve le-kad halakna'l-insâne ve na'lemu mâ tuvesvisu bihî nefsuh, ve nahnu akrabu ileyhi min habli'l-verîd, gloss:insanı biz yarattık ve nefsinin ona ne fısıldadığını biliriz; biz ona şah damarından daha yakınız, source:50:16}. Görünüşte iman edip sıkıntı gelince dönen kişi için de şu sorulur: {ar:أَوَلَيْسَ ٱللَّهُ بِأَعْلَمَ بِمَا فِى صُدُورِ ٱلْعَٰلَمِينَ, tr:e-ve-leysa'llâhu bi-a'leme bimâ fî sudûri'l-âlemîn, gloss:Allah, âlemlerin göğüslerinde olanı en iyi bilen değil midir, source:29:10}. Yerin kendisi de o gün bir haberci olur: {ar:يَوْمَئِذٍ تُحَدِّثُ أَخْبَارَهَا, tr:yevme'izin tuhaddisu ahbârahâ, gloss:o gün yer haberlerini anlatır, source:99:4}. Haberlerini anlatan bu yer, kabirleri altüst edilen yerdir. "Ahbâr" kelimesi de surenin son kelimesiyle aynı köktendir.

Kaynaklar: 100:7 لَشَهِيدٌ ش ه د B001; 100:7 لَشَهِيدٌ ش ه د B002; 100:7 لَشَهِيدٌ ش ه د B005; 100:9 يَعْلَمُ ع ل م B001; 100:11 لَّخَبِيرٌ خ ب ر B001; 100:6 ٱلْإِنسَٰنَ ء ن س B002; 100:4 نَقْعًا ن ق ع B008; 67:13; 67:14; 75:13; 75:14; 75:15; 24:24; 41:21; 50:16; 29:10; 99:4

## Buluşmalar

İlk buluşma, surenin açılış sahnesinde koşan at ile şafak baskını arasındadır. Koşanların tanımı zaten baskın yapanlardır: {ar:العادية الخيل المغيرة, tr:el-âdiyetu'l-haylu'l-muğîra, gloss:"âdiye", baskın yapan atlardır, source:"ع د و,B001"}. Sekizinci ayetin "şedd" kelimesi de iki görüntüyü aynı anda taşır. Bir yanda koşudur, öbür yanda düşmana saldırıdır: {ar:شد على العدو إذا حمل عليه, tr:şedde ale'l-aduvvi izâ hamele aleyh, gloss:düşmana saldırdığında "şedde" denir, source:"ش د د,B003"}. Aynı sahnede ateş görüntüsü de yer alır. Soluk soluğa koşan hayvanların ayakları taşlara çarparak kıvılcım çıkarır. Birinci ayetin kelimesi bir yandan bu soluğu, bir yandan da yanmış çakmak taşını adlandırır. Koşu, kıvılcım ve sabah tek bir hareketin ardışık parçalarıdır.

Surenin iki yarısını birbirine bağlayan asıl buluşma, dördüncü ayetin tozu ile dokuzuncu ayetin kabirleri arasındadır. Toynakların toprağı kaldırması ile kabirlerin altüst edilmesi aynı fiille açıklanır: "bu'sira", "usîra" demektir. Böylece surenin ilk yarısındaki sabah baskını, ikinci yarısındaki altüst oluşun bir ön provası olur. Kur'an da kabirlerden çıkışı bir koşu olarak anlatır: {ar:يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًا كَأَنَّهُمْ إِلَىٰ نُصُبٍ يُوفِضُونَ, tr:yevme yahrucûne mine'l-ecdâsi sirâ'an ke-ennehum ilâ nusubin yûfidûn, gloss:kabirlerden hızla çıkacakları, sanki dikili bir hedefe koşuyorlarmış gibi seğirtecekleri gün, source:70:43}. Bir başka yerde de {ar:يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًا, tr:yevme teşakkaku'l-ardu anhum sirâ'â, gloss:yerin yarılıp onların hızla çıktığı gün, source:50:44} denir. Surenin başında koşanlar atlardır. Sonunda ise koşanlar kabirlerden çıkan insanlardır. Bu insanların gittiği yer de beşinci ayetteki gibi bir topluluğun ortasıdır, ama bu kez bütün insanların toplandığı yerdir.

Ateş ile kabir de aynı kökte buluşur. İkinci ayetin "ateşi çıkarmak" fiili ile gömmenin "örtmek" fiili aynı köktendir. Kur'an ateşi dirilişe delil olarak da kullanır. Çakılan ateşe dair soru dirilişi inkâr edenlere sorulur. Yeşil ağaçtan çıkan ateş de çürümüş kemikleri kimin dirilteceğini soran kişiye verilen cevaptır. Tahtanın içinde gizli duran ateş çakılınca dışarı çıkar, toprağın içinde gizli duran insan da altüst edilince dışarı çıkar. Yağmur sahnesi de aynı yere varır. İyi toprak ile kıt ürün veren toprağı karşılaştıran ayetten hemen önce şöyle denir: {ar:كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:kezâlike nuhrici'l-mevtâ le'allekum tezekkerûn, gloss:ölüleri de böyle çıkarırız; belki düşünüp öğüt alırsınız, source:7:57}. Kenûd toprak bitki bitirmez. Ama sonunda kabirleri altüst edilecek olan da aynı topraktır.

Biriktirilen mal ile göğsün ayıklanması da bir sahnede buluşur. Onuncu ayetin fiilinin aslı, altını maden toprağından ayırmaktır. Biriktirenin malı ise toplanmış altın ve gümüştür. Kur'an bu iki şeyi ateşte birleştirir: {ar:وَٱلَّذِينَ يَكْنِزُونَ ٱلذَّهَبَ وَٱلْفِضَّةَ وَلَا يُنفِقُونَهَا فِى سَبِيلِ ٱللَّهِ, tr:ve'llezîne yeknizûne'z-zehebe ve'l-fiddate ve lâ yunfikûnehâ fî sebîli'llâh, gloss:altın ve gümüşü yığıp Allah yolunda harcamayanlar, source:9:34}; {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhuhum ve cunûbuhum ve zuhûruhum, gloss:o gün bunlar cehennem ateşinde kızdırılır ve alınları, yanları ve sırtları onlarla dağlanır, source:9:35}. Malın bağlılığı ile göğsün içindekinin çıkarılması da tek bir ayette bir aradadır: {ar:إِن يَسْـَٔلْكُمُوهَا فَيُحْفِكُمْ تَبْخَلُوا۟ وَيُخْرِجْ أَضْغَٰنَكُمْ, tr:in yes'elkumûhâ fe-yuhfikum tebhalû ve yuhric adğânekum, gloss:onları (mallarınızı) sizden isteyip ısrar etseydi cimrilik ederdiniz ve O da kinlerinizi dışarı çıkarırdı, source:47:37}. Sevgi kelimesinin "kalbin tanesi" anlamı da bu buluşmayı kelimenin içinden kurar. İnsanın şiddetle bağlandığı mal göğsün içindeki tanedir, harman savrulduğunda ayrılacak olan da odur. Beşinci ayetin kökü de aynı sahnede iki yönde işler. Mal toplayan, yumruğunu sıkan kişi sonunda toplanma gününde toplananlardan biri olur. Onuncu ayetin fiili de bir toplamadır.

Sabah baskını ile malı esirgeme de bir Kur'an sahnesinde birleşir. Bir bahçenin sahipleri ürünü sabahleyin devşireceklerine yemin ederler: {ar:إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ, tr:iz aksemû le-yasrimunnehâ musbihîn, gloss:onu sabaha girerken mutlaka devşireceklerine yemin ettiklerinde, source:68:17}. Onlar uyurken {ar:فَطَافَ عَلَيْهَا طَآئِفٌ مِّن رَّبِّكَ وَهُمْ نَآئِمُونَ, tr:fe-tâfe aleyhâ tâifun min rabbike ve hum nâimûn, gloss:onlar uykudayken Rabbinden bir bela bahçeyi sardı, source:68:19}. Bahçe {ar:فَأَصْبَحَتْ كَٱلصَّرِيمِ, tr:fe-asbahat ke's-sarîm, gloss:sabaha kapkara kesilmiş halde girdi, source:68:20}. Habersiz sahipler ise {ar:فَتَنَادَوْا۟ مُصْبِحِينَ, tr:fe-tenâdev musbihîn, gloss:sabaha girerken birbirlerine seslendiler, source:68:21}. Konuştukları şey şudur: {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌ, tr:en lâ yedhulennehe'l-yevme aleykum miskîn, gloss:bugün oraya hiçbir yoksul yanınıza girmesin, source:68:24}. Bu sahnede bir sabah seferi, yoksula kapanan bir el ve Rabbin cevabı vardır. Sabah baskını yapan, sonunda baskına uğrayan olur. Bizim surede de "yalnız yiyen" kenûd, "sabah" sözüyle başlayan bir surenin sonunda Rabbinin bilgisi karşısında durur.

Su başı ile toprağın altüst edilmesi aynı günün anlatımında buluşur. Yerin sarsıldığı ve ağırlıklarını dışarı attığı gün, insanların {ar:يَصْدُرُ, tr:yasduru, gloss:sudan döner gibi döner, source:99:6} günüdür. Fiil onuncu ayetin göğüs kelimesiyle aynı köktendir. Kabirden çıkış, gömülü olanın açılması ve sudan dönüş tek bir anda birleşir. İnsanlar amellerini görmek için bölük bölük döner.

Tanıklık ile Rab sözü ise yedinci ayetin iki okumasını bir araya getirir. Âdem oğullarının "Rabbiniz değil miyim" sorusuna "evet, tanık olduk" diye cevap verdiği sahnede, insan kendi Rabbine dair kendisi üzerine tanıktır. Bizim surede de aynı insan, Rabbine karşı nankörlüğü üzerine tanıktır. Birinci ayetin atının tanığı ise koşusudur ve onun öne geçtiğine tanıklık eder. Aynı kelime atta lehte, insanda aleyhte işler.

Bu buluşmalar surenin hareketini dışarıdan içeriye doğru taşır. Sure, gözle görülen ve kulakla işitilen şeylerle başlar: soluk, kıvılcım, sabah ışığı, toz ve kalabalık. Sonra göze görünmeyen bir yere, göğüsteki taneye ulaşır. Toynakların kaldırdığı toprak kabirlerin toprağına, baskının sabahı toplanma gününe, yağmurun beklendiği tarla kabirlerini açan yere dönüşür. Malın düğümü ve yumulmuş el de toplanıp ayıklanan bir göğse dönüşür. Bu yolun her aşamasında bilgi de derinleşir: önce hazır bulunan ve gören bir tanık vardır, sonra sorulan ama cevaplanmayan bir bilgi, en sonda da içini bilen bir Rab.

