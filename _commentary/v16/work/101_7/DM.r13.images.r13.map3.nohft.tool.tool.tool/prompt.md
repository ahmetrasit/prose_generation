Focus: 101:7. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/101_7/D.r13/context.md =====
# 101:7 — focus

فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ

Anchor translation (canonical reading, reference only):

o, hoşnut edici bir yaşam içinde olacaktır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَهُوَ |  |  | RSLT;PRON |
| 2 | فِى | فِى |  | P |
| 3 | عِيشَةٍ | عِيشَة | ع ي ش | N |
| 4 | رَّاضِيَةٍ | رَاضِيَة | ر ض و | ADJ |


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
- 101:6 فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ
- 101:7 ◀ focus فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ
- 101:8 وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ
- 101:9 فَأُمُّهُۥ هَاوِيَةٌۭ
- 101:10 وَمَآ أَدْرَىٰكَ مَا هِيَهْ
- 101:11 نَارٌ حَامِيَةٌۢ


===== _commentary/v16/work/101_7/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع ي ش (root_001067) — identity root of عِيشَةٍ (w3)

- **B001** yaşam ve yaşayış durumu — yaşam · yaşadı · Tanrı ona hoşnut olacağı bir yaşam verdi · yaşayış biçimi · iyi bir yaşayış · övgüye değer bir yaşayış · dar ve sıkıntılı yaşam · durumu iyi olan kimse
  العيش الحياة (maqayis;ayn;sihah); العيش الحياة المختصة بالحيوان (mufradat); عيشة صالحة وراضية وصدق وسوء وضنك (maqayis;sihah;tahdhib;mufradat); رجل عائش حاله حسنة (maqayis;tahdhib)
- **B002** geçim araçları, ortamı ve geçinme uğraşı — yaşamı sağlayan yiyecek ve içecek · geçim kaynağı · geçim kaynakları · geçim aracı veya geçinilen yer · gündüz, geçim arama zamanı · yeryüzü, geçim sağlanan yer · geçim · geçinme yollarını sağlamak için çabalama · geçinebilecek kadar olanağa sahip olma · geçim · o topluluğun geçimliği süttür
  المعيشة ما يعاش به (maqayis;ayn;tahdhib); المطعم والمشرب وما يكون به الحياة (maqayis;ayn;tahdhib); كل شيء يعاش به أو فيه فهو معاش (maqayis;ayn); كل شيء يعاش به فهو معاش (tahdhib); ما يتعيش منه (mufradat); التعيش تكلف أسباب المعيشة (sihah); يتعيشون إذا كانت لهم بلغة من عيش (maqayis;tahdhib)

## ر ض و (root_000569) — identity root of رَّاضِيَةٍ (w4)

- **B001** hoşnut olma ve kabul etme — hoşnut olmak; kabul etmek · hoşnut · kabul edilmiş; kendisinden hoşnut olunan · kendisinden hoşnut olunan kişi · hoşnutluk · onu kabul edip uygun buldu · onu seçip uygun buldu · ondan hoşnut oldu; onu kabul etti · hoşnutluk adı · beğenilen bir yaşayış · onu arkadaş olarak kabul etti · ondan hoşnut oldu; onu uygun buldu · beğenilen; kabul edilen · kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması · Tanrı'nın kulu buyruğa uyan ve yasaktan kaçınan biri olarak görmesi
  أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضا مقصور (ayn)؛ رضيت الشيء وارتضيته فهو مرضي ومرضو ورضيت عنه رضا (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو ورضا العبد عن الله ورضا الله عن العبد (mufradat)
- **B002** hoşnutluk; yoğun hoşnutluk — hoşnutluk; yoğun hoşnutluk · hoşnutluk
  الرضوان اسم موضوع من الرضا (ayn)؛ الرضوان الرضا وكذلك الرضوان بالضم والمرضاة مثله (sihah)؛ الرضوان الرضا الكثير (mufradat)
- **B003** karşılıklı hoşnutluk ve kabul — karşılıklı hoşnutluk · birbiriyle hoşnutlaşma · birbirlerinden hoşnut olduklarını karşılıklı gösterdiler
  المراضاة من اثنين (ayn)؛ مصدر راضيته رضاء ومراضاة (sihah;tahdhib)؛ إذا تراضوا بينهم أي أظهر كل واحد منهم الرضا بصاحبه ورضيه (mufradat)
- **B004** başkasını hoşnut etme veya hoşnutluğunu isteme — onu kendimden hoşnut ettim · onu hoşnut ettim · uğraşarak onu hoşnut ettim · ondan hoşnutluk göstermesini istedim; o da beni hoşnut etti
  أرضيته عني ورضيته بالتشديد أيضا فرضي وترضيته أرضيته بعد جهد واسترضيته فأرضاني (sihah)
- **B005** karşılıklı çekişmede üstün gelme — karşılıklı çekişmede ona üstün geldim
  قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه لأنه من الواو (sihah)
- **B006** söz dinleyen, seven veya güvence veren — söz dinleyen; seven; güvence veren
  الرضي المطيع والرضي المحب والرضي الضامن (tahdhib)
- **B007** bir dağ adı ve kadın adları — bir dağ adı; bir kadın adı · o dağın adına bağlılık bildiren biçim · bir kadın adı
  رضوى جبل (maqayis;ayn;sihah)؛ ومن أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)

## ECHO ر ض ي (root_000570) — for رَّاضِيَةٍ (w4): withheld observed target; not identity

- **B001** hoşnut olup uygun bulma — hoşnut olmak; gönlüne uygun bulmak · hoşnut olan · beğenilmiş, uygun bulunmuş · kendisinden hoşnut olunan · uygun bulunmuş; eski kök yapısını koruyan biçim · kendisinden hoşnut olunan adam; eski kök yapısını koruyan söyleyiş · hoşnutluk; hoşnutsuzluğun karşıtı · hoşnutluğu bildiren uzatılmış ad biçimi · hoşnutluk; çok güçlü hoşnutluk · hoşnutluk bildiren ad · iki tarafın birbirini uygun bulması · birbirini uygun bulma ve karşılıklı anlaşma · şeyi beğenip uygun buldum · onu beğenip seçtim · ondan hoşnut oldum · onu arkadaş olarak uygun buldum · ondan ya da onunla olmaktan hoşnut oldum · beğenilen, hoşnutluk veren yaşayış · onu benden hoşnut ettim · onu hoşnut ettim · uğraştıktan sonra onu hoşnut ettim · onun gönlünü yapmaya çalıştım, sonunda benden hoşnut oldu · birbirlerini uygun bulup anlaştılar · kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması · Tanrı'nın kulunu buyruklarına uyar ve yasaklarından kaçınır görmesi · beğenilmiş, uygun bulunmuş
  أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضوان من الرضا (ayn)؛ الرضوان الرضا والمرضاة مثله ورضيت الشيء وارتضيته (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو والرضوان الرضا الكثير (mufradat)
- **B002** çekişmede alt etme — o benimle çekişti, ben de onu o işte yendim
  قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه (sihah)
- **B003** dağ ve kadın adı ailesi — bir dağın ve bir kadının adı · söz konusu dağla ilgili veya o dağdan olan · bir kadın adı
  رضوى جبل (maqayis;ayn)؛ رضوى جبل بالمدينة والنسبة إليه رضوى (sihah)؛ من أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)
- **B004** buyruğa uyan, seven veya güvence veren — buyruğa uyan, seven ya da güvence veren
  الرَّضِيّ المطيع؛ الرَّضِيّ المحب؛ الرَّضِيّ الضامن (tahdhib)

===== _commentary/v16/out/s101/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 101:7, and ## Buluşmalar) =====
## Hoşnut yaşayış ve döşenmiş ev

Yedinci ayet, tartıları ağır geleni {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:o, hoşnut bir yaşayış içindedir, source:101:7} diye anlatır. Îşe, yaşamaktır: {ar:العيش الحياة, tr:el-ayş el-hayât, gloss:ayş, hayattır, source:"ع ي ش,B001"}. Bu iki kelime dilde zaten birlikte anılır ve aynı sırada tersleri de sayılır: {ar:عيشة صالحة وراضية وصدق وسوء وضنك, tr:îşetun sâliha ve râdiye ve sıdk ve sû' ve dank, gloss:iyi, hoşnut, gerçek, kötü ve dar yaşayış, source:"ع ي ش,B001"}. Ayş aynı zamanda insanın onunla yaşadığı ve içinde yaşadığı şeydir: {ar:المطعم والمشرب وما يكون به الحياة, tr:el-mat'am ve'l-meşrab, gloss:yemek, içecek ve hayatın onunla sürdüğü şey, source:"ع ي ش,B002"}; {ar:كل شيء يعاش به أو فيه فهو معاش, tr:kullu şey'in yu'âşu bihî ev fîh, gloss:onunla ya da içinde yaşanan her şey maâştır, source:"ع ي ش,B002"}. Râdiye, öfkenin karşıtıdır, {ar:أصل واحد يدل على خلاف السخط, tr:aslun vâhid yedullu alâ hılâfi's-suht, gloss:hoşnutsuzluğun zıddını gösteren tek kök, source:"ر ض و,B001"}; bol hoşnutluktur {source:"ر ض و,B002"} ve iki taraflıdır: {ar:المراضاة من اثنين, tr:el-murâdât mini'sneyn, gloss:karşılıklı hoşnutluk iki kişi arasındadır, source:"ر ض و,B003"}. Ayetin tuhaf görünen yapısı, yaşayışın kendisinin hoşnut olması, bu iki taraflılığı hissettirir: yaşayış hem hoşnut eder hem hoşnut olur.

Surenin öbür kelimeleri bu yaşayışın evini döşer. Ferâş, döşenmiş yataktır ve kelimenin örnekleri cennetin döşekleridir: {ar:يقال للمفروش فرش وفراش؛ وفرش مرفوعة؛ فرش بطائنها من إستبرق, tr:ve furuşin merfû'a, gloss:serilene ferş ve firâş denir; yükseltilmiş döşekler; astarları kalın ipekten döşekler, source:"ف ر ش,B002"}. Mebsûs, evin içine serilmiş halılardır: {ar:وزرابي مبثوثة, tr:ve zerâbiyyu mebsûse, gloss:ve serilmiş halılar, source:"ب ث ث,B001"}. Ihn kökü, hazır yemeği ve içeceği, bir yerde yerleşik kalmayı da adlandırır: {ar:العاهن الطعام الحاضر والشراب الحاضر, tr:el-âhin et-taâmu'l-hâdır, gloss:âhin, hazır yemek ve hazır içecektir, source:"ع ه ن,B001"}; {ar:عهن بالمكان أقام به, tr:ahene bi'l-mekân, gloss:o yerde kaldı, yerleşti, source:"ع ه ن,B001"}. Ümm kökü de nimeti, iyi hali anlatır: {ar:الإمة النعمة, tr:el-imme en-ni'me, gloss:imme, nimettir, source:"ء م م,B010"}. Bu aile imgesinde, dördüncü ve beşinci ayetlerde dağılmayı anlatan kelimeler, başka bir okumada yedinci ayetin evinin eşyalarıdır.

Kur'an yedinci ayetin sözlerini aynen başka bir sahnede tekrarlar. Hâkka suresinde, kitabı sağından verilen {ar:فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ, tr:fe-emmâ men ûtiye kitâbehû bi-yemînih, gloss:kitabı sağından verilene gelince, source:69:19} sevinçle kitabını gösterir ve {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:o hoşnut bir yaşayış içindedir, source:69:21}, {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüce bir bahçede, source:69:22}; meyveleri sarkmış, yakındır {source:69:23}. Aynı surede öbür taraf {ar:وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِشِمَالِهِۦ, tr:ve emmâ men ûtiye kitâbehû bi-şimâlih, gloss:kitabı solundan verilene gelince, source:69:25} diye açılır. Gâşiye suresinde yüzler {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdiye, gloss:çabalarından hoşnuttur, source:88:9}, ve onların halıları serilidir: {ar:وَزَرَابِىُّ مَبْثُوثَةٌ, tr:ve zerâbiyyu mebsûse, gloss:ve serilmiş halılar, source:88:16}; mebsûs kelimesi burada dördüncü ayetteki ile aynı kalıptadır. Fecr suresinde huzura ermiş can {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irci'î ilâ rabbiki râdiyeten mardiyye, gloss:Rabbine hoşnut ve hoşnut olunmuş olarak dön, source:89:28} diye çağrılır; iki taraflı hoşnutluk burada iki kelimeyle söylenir. Hoşnut yaşayışın zıddı da Kur'an'dadır: Tâhâ suresinde Allah, zikrinden yüz çevirene {ar:فَإِنَّ لَهُۥ مَعِيشَةًۭ ضَنكًۭا, tr:fe-inne lehû maîşeten dankâ, gloss:onun için dar bir geçim vardır, source:20:124} olduğunu söyler.

Kaynaklar: 101:7 عِيشَةٍ ع ي ش B001; 101:7 عِيشَةٍ ع ي ش B002; 101:7 رَّاضِيَةٍ ر ض و B001; 101:7 رَّاضِيَةٍ ر ض و B002; 101:7 رَّاضِيَةٍ ر ض و B003; 101:4 كَٱلْفَرَاشِ ف ر ش B002; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:5 كَٱلْعِهْنِ ع ه ن B001; 101:9 فَأُمُّهُۥ ء م م B010

## Anası: dipsiz çukur

Dokuzuncu ayet, tartıları hafif gelene bir ana verir: {ar:فَأُمُّهُۥ هَاوِيَةٌۭ, tr:fe-ummuhû hâviye, gloss:onun anası hâviyedir, source:101:9}. Ayetin anlamı, onun sığınağının ve varacağı yerin hâviye olduğudur. Ümm, besleyen ve büyütendir: {ar:فلانة تؤم فلانا أي تغذوه وتربيه, tr:fulânetun teummu fulânâ, gloss:filan kadın filanı besler ve büyütür, source:"ء م م,B001"}. Ümm aynı zamanda yanındakileri kendine toplayan her şeydir: {ar:كل شيء يضم إليه ما سواه مما يليه فإن العرب تسمى ذلك الشيء أما, tr:kullu şey'in yedummu ileyhi mâ sivâh, gloss:yanındakileri kendine katan her şeye Araplar ümm der, source:"ء م م,B002"}; {ar:كل شيء انضمت إليه أشياء فهو أم, tr:kullu şey'in indammet ileyhi eşyâ', gloss:başka şeylerin kendisine katıldığı her şey ümmdür, source:"ء م م,B002"}. Bir şeyin varlığının, büyümesinin ya da başlangıcının kaynağı olan her şey de böyle adlandırılır {source:"ء م م,B002"}.

Hâviye, dibine erişilemeyen her uçurumdur: {ar:الهاوية كل مهواة لا يدرك قعرها والهوة كل وهدة معمقة, tr:el-hâviye kullu mehvâtin lâ yudraku ka'ruhâ, gloss:hâviye, dibine erişilemeyen her çukurdur; huvve, derinleştirilmiş her çukurdur, source:"ه و ي,B002"}; düşmek, yukarıdan aşağı yuvarlanmaktır: {ar:هوى الشيء يهوي إذا خر من علو إلى سفل, tr:heve'ş-şey'u yehvî, gloss:şey yukarıdan aşağıya düştü, source:"ه و ي,B002"}. Kökün temelinde boşluk ile düşüş birdir: {ar:أصل صحيح يدل على خلو وسقوط, tr:aslun sahîh yedullu alâ hulüvvin ve sukût, gloss:boşluk ve düşüşü gösteren sağlam bir kök, source:"ه و ي,B001"}. Gökle yer arasındaki hava da, boş bir kalp de bu kökle anılır: {ar:الهَواء ما بين السماء والأرض وكل خال هواء, tr:el-hevâ' mâ beyne's-semâi ve'l-ard, gloss:hevâ, gökle yer arasındaki şeydir; her boş şey hevâdır, source:"ه و ي,B001"}; {ar:قلبه هَواء, tr:kalbuhû hevâ', gloss:kalbi bomboş, source:"ه و ي,B001"}. Düşmek ölmektir de: {ar:هوى فلان أي مات, tr:hevâ fulân, gloss:filan düştü, yani öldü, source:"ه و ي,B002"}; hâviye, cehennemin adlarından biridir {source:"ه و ي,B002"}.

Ümm ile hâviyeyi bir araya getiren bir deyim vardır: {ar:هوت أمه فهي هاوية أي ثاكلة, tr:hevet ummuhû fe-hiye hâviye, gloss:anası düştü, yani evladını yitirdi; o, hâviyedir, source:"ه و ي,B002"}. Arapçada bu söz bir beddua olarak kullanılır, "anası ağlasın" gibi {source:"memory"}. Böylece ayet iki sahneyi birden taşır. Biri: anası evladını yitirmiştir, çünkü o ölmüştür. Öbürü: çukur onun anasıdır ve bir ananın çocuğunu bağrına basması gibi onu içine alır. Çukur besleyen değil yutan bir anadır; toplayan ama bırakmayan. Karşısında yedinci ayetin adamı durur, onun bir hayatı, bir yaşayışı vardır {source:"ع ي ش,B001"}. Hayat ile evladını yitirmiş ana, ayetlerin karşıtlığını aile imgesinde de kurar.

Çukurun bir dibi yoktur. Dağın kökü, kazanların kayaya varıp durduğu anı adlandıran bir deyim taşır: {ar:أجبل القوم إذا حفروا فبلغوا المكان الصلب, tr:ecbele'l-kavm, gloss:topluluk kazdı ve sert yere vardı, source:"ج ب ل,B005"}. Dipsiz çukur bunun tersidir: duracak bir kaya yoktur, çünkü dağlar da yün olmuştur. On birinci ayetin hâmiyesi, bir kuyunun duvarını ören ağır taşları da adlandırır: {ar:الحامية الحجارة يطوى بها البئر, tr:el-hâmiye el-hıcâre yutvâ bihe'l-bi'r, gloss:hâmiye, kuyunun onlarla örüldüğü taşlardır, source:"ح م ي,B011"}; {ar:الحوامي عظام الحجارة وثقالها, tr:el-havâmî izâmu'l-hıcâre ve sikâluhâ, gloss:havâmî, taşların iri ve ağır olanlarıdır, source:"ح م ي,B011"}. Bu aile imgesinde çukurun duvarları ağır taştır, içine düşen ise hafif olandır.

Kur'an'da düşüş ve boşluk, bu kökün sahneleridir. Hac suresinde Allah, ona ortak koşanı {ar:فَكَأَنَّمَا خَرَّ مِنَ ٱلسَّمَآءِ فَتَخْطَفُهُ ٱلطَّيْرُ أَوْ تَهْوِى بِهِ ٱلرِّيحُ فِى مَكَانٍۢ سَحِيقٍۢ, tr:fe-ke-ennemâ harra mine's-semâi fe-tahtafuhu't-tayru ev tehvî bihi'r-rîhu fî mekânin sehîk, gloss:sanki gökten düşmüş, kuşlar onu kapıyor ya da rüzgâr onu uzak bir yere savuruyor, source:22:31} diye anlatır. İbrâhîm suresinde zalimler gözlerin donup kaldığı günde {source:14:42} anlatılır: {ar:وَأَفْـِٔدَتُهُمْ هَوَآءٌۭ, tr:ve ef'idetuhum hevâ', gloss:kalpleri bomboştur, source:14:43}. Tâhâ suresinde Allah İsrâiloğullarına {ar:وَمَن يَحْلِلْ عَلَيْهِ غَضَبِى فَقَدْ هَوَىٰ, tr:ve men yahlil aleyhi ğadabî fe-kad hevâ, gloss:kime gazabım inerse o düşmüştür, source:20:81} der; Necm suresinde altüst edilen kentler için {ar:وَٱلْمُؤْتَفِكَةَ أَهْوَىٰ, tr:ve'l-mu'tefikete ehvâ, gloss:altüst olanı da düşürdü, source:53:53} söylenir. Tevbe suresindeki sahne başka bir kökle kurulur ama aynı düşüşü gösterir: bina, çökecek bir yarın kenarına kurulmuştur, {ar:فَٱنْهَارَ بِهِۦ فِى نَارِ جَهَنَّمَ, tr:fe'nhâra bihî fî nâri cehennem, gloss:onunla birlikte cehennem ateşine yıkılıp gitti, source:9:109}. Kâf suresinde dipsizlik bir konuşmaya dönüşür: {ar:يَوْمَ نَقُولُ لِجَهَنَّمَ هَلِ ٱمْتَلَأْتِ وَتَقُولُ هَلْ مِن مَّزِيدٍۢ, tr:yevme nekûlu li-cehenneme heli'mtele'ti ve tekûlu hel min mezîd, gloss:o gün cehenneme "doldun mu" deriz, o da "daha var mı" der, source:50:30}. Nâziât suresinde Allah insanları ayırır, her birine bir sığınak verir: {ar:فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ, tr:fe-inne'l-cahîme hiye'l-me'vâ, gloss:işte cehennem, sığınak odur, source:79:39} ve {ar:فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ, tr:fe-inne'l-cennete hiye'l-me'vâ, gloss:işte cennet, sığınak odur, source:79:41}; ikisinin arasında, cennete gidenin nefsini {ar:وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve nehe'n-nefse ani'l-hevâ, gloss:ve nefsini hevadan alıkoydu, source:79:40} diye anılması, hâviye ile aynı kökü taşır.

O gün insan anası da elinden bırakır. Hac suresinde kıyametin sarsıntısında {ar:تَذْهَلُ كُلُّ مُرْضِعَةٍ عَمَّآ أَرْضَعَتْ, tr:tezhelu kullu murdı'atin ammâ erda'at, gloss:her emziren, emzirdiğini unutur, source:22:2}; Abese suresinde, kulakları sağır eden ses geldiğinde {source:80:33}, {ar:يَوْمَ يَفِرُّ ٱلْمَرْءُ مِنْ أَخِيهِ, tr:yevme yefirru'l-mer'u min ahîh, gloss:kişinin kardeşinden kaçtığı gün, source:80:34}, {ar:وَأُمِّهِۦ وَأَبِيهِ, tr:ve ummihî ve ebîh, gloss:anasından ve babasından, source:80:35}. Mü'minûn suresi bunu, terazi ayetlerinin hemen öncesinde söyler: {ar:فَلَآ أَنسَابَ بَيْنَهُمْ يَوْمَئِذٍۢ وَلَا يَتَسَآءَلُونَ, tr:fe-lâ ensâbe beynehum yevmeizin ve lâ yetesâelûn, gloss:o gün aralarında soy bağı kalmaz, birbirlerini de sormazlar, source:23:101}. Gerçek ana çocuğunu bırakınca, geriye o kişiyi kucaklayan tek ana olarak çukur kalır.

Kaynaklar: 101:9 فَأُمُّهُۥ ء م م B001; 101:9 فَأُمُّهُۥ ء م م B002; 101:9 هَاوِيَةٌ ه و ي B001; 101:9 هَاوِيَةٌ ه و ي B002; 101:7 عِيشَةٍ ع ي ش B001; 101:5 ٱلْجِبَالُ ج ب ل B005; 101:11 حَامِيَةٌ ح م ي B011

## Buluşmalar

İmgelerin ilk buluşma yeri dördüncü ve beşinci ayetlerdir. Bir darbe iner ve sıkı olanı dağıtır; bu dağılmanın iki yüzü vardır. Yünün atılması bir dövmedir {source:"ن ف ش,B001"}, dolayısıyla dağların yüne dönmesi, birinci ayetin vuruşunun eseridir. Aynı kelime, menfûş, geceleyin çobansız yayılan sürüyü de anlatır {source:"ن ف ش,B003"}; dağılan dağ ile dağılan sürü tek kelimede birleşir. Dördüncü ayetin ferâşı da hem serili yeri hem saçılan sürüyü taşır; bu iki anlamı bağlayan açıklama, ferşi beşş ile anlatır {source:"ف ر ش,B004"}. Yeryüzünü döşeyen serme işi ile kıyametteki saçılma aynı iki kelimeyle söylenir.

İkinci buluşma, pervane ile terazidir. Pervane hafifliğinden ötürü bu adı almıştır ve savruk adama ferâşe denir {source:"ف ر ش,B005"}; sekizinci ayetin hafifliği de akıl savrukluğudur {source:"خ ف ف,B004"}. Dördüncü ayetin pervane insanları, sekizinci ayetin tartıları hafif gelenleridir. Bu iki imge birlikte surenin hareketini taşır: hafif olan, ışığa doğru savrulur ve ateşe düşer. Pervanenin birbiri ardınca kandile düşüşü {source:"ف ر ش,B005"} ile topluluğun birbiri ardınca çukura düşüşü {source:"ه و ي,B002"} aynı hareketi verir; dokuzuncu ayetin ümm kelimesi hedefe yönelmeyi {source:"ء م م,B012"}, on birinci ayetin ateşi de o hedefin kendisini adlandırır. Böylece dördüncü ayetteki saçılma ile on birinci ayetteki ateş, surenin iki ucunda aynı sahnenin başı ve sonudur. Hâmiye kelimesinin insanların sakındığı korunmuş şeyi anlatan kolu {source:"ح م ي,B002"}, pervanenin yaptığının tersini gösterir.

Üçüncü buluşma, ana ile çukurdur ve bu ikisi yaşayışın karşısında durur. "Anası düştü" deyimi dokuzuncu ayetin iki kelimesini birlikte taşır {source:"ه و ي,B002"}; ümm kelimesinin toplayan, kendine katan anlamı {source:"ء م م,B002"} çukuru, düşeni içine alan yer yapar. Yedinci ayetin yaşayışı ise hayattır {source:"ع ي ش,B001"}; evladını yitirmiş ananın karşısında yaşayan biri. Nâziât suresinin iki sığınağı {source:79:39} {source:79:41} bu karşıtlığı Kur'an'ın kendi sözleriyle kurar.

Dördüncü buluşma çukur ile terazi, ve çukur ile dağlar arasındadır. Hâmiye kuyunun duvarını ören ağır taşlardır {source:"ح م ي,B011"}; içine düşen ise tartısı hafif gelendir. Dağlar en ağır, en kalın kütleydi {source:"ج ب ل,B003"} ve atılmış yünün içi boşluktur {source:"ن ف ش,B002"}; hâviyenin kökü de boşluktur {source:"ه و ي,B001"}. Kazıcıyı durduran kaya {source:"ج ب ل,B005"} yok olunca, çukurun dibi de yoktur. Terazide ağırlık değerse, dağların ağırlığının yüne dönmesi, kıyamet günü dünyanın ağır saydığı şeylerin ağırlıksızlaştığını, tek ağırlığın tartının kefesinde kaldığını gösterir.

Son buluşma, kapı ile ateş arasındadır. Surenin başındaki vuruş üç kez sorulur ve bir sahneyle cevaplanır; onuncu ayetteki soru ise hemen, kızgın bir ateşle cevaplanır. Hümeze suresi aynı soru ile aynı türden cevabı verir {source:104:5} {source:104:6}. Savaş günü imgesi de bu iki ucu birleştirir: başta kılıçların çarpışması {source:"ق ر ع,B002"}, sonda topluluk içinde patlak veren düşmanlık ve kızışan öfke {source:"ن و ر,B007"} {source:"ح م ي,B003"}. Böylece sure bir kapı vuruşuyla, bir uyarıyla açılır ve bir ateşle kapanır; aradaki her kelime, o vuruşun neyi dağıttığını, neyi tarttığını ve hafif olanı nereye düşürdüğünü gösterir.

