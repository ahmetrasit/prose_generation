Focus: 1:3. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/1_3/D.r13/context.md =====
# 1:3 — focus

ٱلرَّحْمَٰنِ ٱلرَّحِيمِ

Anchor translation (canonical reading, reference only):

Merhameti sınırsızdır, merhamet edendir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ٱلرَّحْمَٰنِ | رَّحْمَٰن | ر ح م | DET;ADJ |
| 2 | ٱلرَّحِيمِ | رَّحِيم | ر ح م | DET;ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 1 — full text (context; no pericope)

- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ◀ focus ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ


===== _commentary/v16/work/1_3/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر ح م (root_000552) — identity root of ٱلرَّحْمَٰنِ (w1)

- **B001** acıma duygusuyla esirgeyip iyilik etme — ona acıyıp onu esirgemek · acıma duygusu ve bu duygunun yönelttiği iyilik · özellikle güçsüze acıyıp onu esirgeme · acıma, iyilik ve gözetme · birbirine acıyıp birbirini esirgemek · onun Tanrı'nın esirgemesine erişmesini dilemek · esirgemesi her şeyi kuşatan Tanrı adı · çok esirgeyen ve bol bol iyilik eden · acınıp esirgenen kimse · acıma ve esirgeme görmüş kimse · acıyan ve esirgeyenlerin en üstünü · ana babasına daha iyi davranan ve daha yakınlık gösteren · acıma ve esirgeme ya da başkasının acımasına konu olma durumu
  أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)
- **B002** yakın soy bağı — yakın soy bağı · soy ve yakınlık bağları · soy bağını sürdürmek ya da koparmak
  الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)
- **B003** döl yatağı — dişinin döl yatağı · döl yatakları
  سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)
- **B004** döl yatağı hastalığı ve doğum sonrası bozukluk — doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi · döl yatağı ağrımak ya da hastalanmak · koyunun doğumdan sonra yavru zarını atamaması · döl yatağı şişmiş koyun ya da koyun sürüsü
  شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 1:3, and ## Buluşmalar) =====
## Rahim ve terbiye: çocuğun evi ve onu kemale erdiren

Birinci ayetteki iki sıfat {ar:ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:er-rahmâni'r-rahîm, gloss:merhameti bol olan, merhamet eden, source:1:1}, ana karnındaki rahimle aynı köktendir. Rahim, içinde çocuğun büyüdüğü bir evdir: {ar:الرحم بيت منبت الولد ووعاؤه في البطن, tr:er-rahimu beytü menbiti'l-veledi ve vi'âühû fi'l-batn, gloss:rahim, karındaki çocuğun bittiği yer olan ev ve onun kabıdır, source:"ر ح م,B003"}. Bu evin bedeli de vardır: {ar:الرحوم الناقة التي تشتكي رحمها بعد النتاج, tr:er-rahûmu'n-nâkatü'lletî teştekî rahimehâ ba'de'n-nitâc, gloss:rahûm, doğurduktan sonra rahminden acı çeken dişi devedir, source:"ر ح م,B004"}. Merhamet, bu yakınlıktan doğan bir incelik olarak tanımlanır, ama orada kalmaz, bir iyiliğe dönüşür: {ar:الرحمة رقة تقتضي الإحسان إلى المرحوم, tr:er-rahmetü rikkatün tektedi'l-ihsâne ile'l-merhûm, gloss:rahmet, merhamet edilene iyilik etmeyi gerektiren bir inceliktir, source:"ر ح م,B001"}. Bu iyilik özellikle zayıfa yönelir: {ar:ورحمة الضعيف والتعطف عليه, tr:ve rahmetü'd-da'îfi ve't-teattufu aleyh, gloss:zayıfa merhamet etmek ve ona şefkatle eğilmek, source:"ر ح م,B001"}. Akrabalık da aynı kelimeyle anılır, çünkü akrabalar tek bir rahimden çıkmıştır: {ar:استعير الرحم للقرابة لكونهم خارجين من رحم واحدة, tr:üstüîre'r-rahimu li'l-karâbe, gloss:rahim kelimesi akrabalık için ödünç alındı, çünkü akrabalar tek bir rahimden çıkmıştır, source:"ر ح م,B002"}.

İkinci ayetteki "Rab" kelimesi rahimden sonraki aşamayı, yani büyütmeyi taşır: {ar:رب فلان ولده؛ رباه, tr:rabbe fülânün veledeh, gloss:falanca çocuğunu büyüttü, source:"ر ب ب,B002"}. Büyütmenin nasıl işlediği de tarif edilir: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiyetü, ve hüve inşâü'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi halden hale geçirerek tamamlanma sınırına kadar yetiştirmektir, source:"ر ب ب,B002"}. Çocuğu doğuranın dışında birinin büyütmesi de aynı köktendir: {ar:الراب والرابة بأحد الزوجين إذا تولى تربية الولد, tr:er-râbbü ve'r-râbbe, gloss:râb ve râbbe, eşlerden birinin çocuğunun terbiyesini üstlenen üvey ebeveyndir, source:"ر ب ب,B005"}, {ar:الربيبة: الحاضنة, tr:er-rabîbetü'l-hâdına, gloss:rabîbe, çocuğa bakan dadıdır, source:"ر ب ب,B005"}. Yeni doğurmuş koyun da bu köktendir: {ar:الشاة الربي التي تحتبس في البيت للبن, tr:eş-şâtü'r-rubbâ, gloss:rubbâ, sütü için evde alıkonan koyundur, source:"ر ب ب,B009"}. Büyütme öğretmeye de uzanır: {ar:العالم المعلم الذي يغذو الناس بصغار العلوم, tr:el-âlimü'l-muallimü'llezî yağzu'n-nâse bi-sığâri'l-ulûm, gloss:insanları önce bilginin küçük parçalarıyla besleyen öğretici âlim, source:"ر ب ب,B003"}. Bu cümle "Rab" ile ikinci ayetteki "âlemîn" kelimesinin kökünü yan yana getirir.

Sure bu görüntüyü bir çerçeve içinde kurar. Birinci ayet rahimle açılır. İkinci ayet büyüten Rabbi anar. Üçüncü ayet, "âlemlerin Rabbi" sözünün hemen ardından iki sıfatı tekrar eder: {ar:ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:er-rahmâni'r-rahîm, gloss:merhameti bol olan, merhamet eden, source:1:3}. Böylece büyütme iki yandan rahimle sarılır. Düz bir meal "Rahman, Rahim" deyip geçer. Görüntü ise bu merhametin bir yer ve bir süre içinde işlediğini gösterir: Önce bir ev, sonra halden hale bir büyütme ve sonunda tamamlanma vardır. Altıncı ayet bu evin işlerini ayakta tutanı da hatırlatır: {ar:قوام أهل بيته وقيام أهل بيته؛ الذي يقيم شأنهم, tr:kıvâmü ehli beytihî, gloss:ev halkının işlerini ayakta tutan, source:"ق و م,B004"}. Yedinci ayetteki "en'amte" kelimesinin ailesinde rahat içinde büyütülen çocuklar vardır: {ar:نعم فلان أولاده ترفهم, tr:na''ame fülânün evlâdehû, gloss:falanca çocuklarını bolluk içinde büyüttü, source:"ن ع م,B002"}. Aynı ayetteki "gayr" kelimesinin ailesinde eve getirilen erzak ({ar:الغِيرة بالكسر: الميرة, tr:el-gıyretü bi'l-kesr: el-mîre, gloss:esreli gıyre erzaktır, source:"غ ي ر,B001"}) ve evi kıskançlıkla korumak ({ar:الغَيرة بالفتح مصدر قولك غار الرجل على أهله, tr:el-gayretü bi'l-feth, gloss:üstünlü gayre, adamın ailesini kıskanıp korumasıdır, source:"غ ي ر,B004"}) vardır. Bu iki kelime ayetteki "değil" anlamının yanında, bir evin beslenmesini ve korunmasını duyurur.

Kur'an bu evi açıkça sahneler. Rahim, Allah'ın şekil verdiği yerdir: {ar:هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ, tr:hüvellezî yusavvirukum fi'l-erhâmi keyfe yeşâ', gloss:sizi rahimlerde dilediği gibi biçimlendiren O'dur, source:3:6}. Akrabalık bağı da Allah'ın adıyla birlikte anılır: {ar:وَٱتَّقُوا۟ ٱللَّهَ ٱلَّذِى تَسَآءَلُونَ بِهِۦ وَٱلْأَرْحَامَ, tr:vettekullâhellezî tesâelûne bihî ve'l-erhâm, gloss:adını anarak birbirinizden dilekte bulunduğunuz Allah'tan ve akrabalık bağlarından sakının, source:4:1}. Üvey çocuk da "rabîbe" kelimesiyle anılır: {ar:وَرَبَٰٓئِبُكُمُ ٱلَّٰتِى فِى حُجُورِكُم, tr:ve rabâibükümü'llâtî fî hucûriküm, gloss:kucağınızda büyüyen üvey kızlarınız, source:4:23}. Bu ailenin en yoğun sahnesi, Rabbin ana babayla ilgili hükmüdür: {ar:وَقَضَىٰ رَبُّكَ أَلَّا تَعْبُدُوٓا۟ إِلَّآ إِيَّاهُ وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًا, tr:ve kadâ rabbüke ellâ ta'büdû illâ iyyâhü ve bi'l-vâlideyni ihsânâ, gloss:Rabbin, yalnız O'na kulluk etmenizi ve ana babaya iyilik etmenizi hükmetti, source:17:23}. Ardından şu gelir: {ar:وَٱخْفِضْ لَهُمَا جَنَاحَ ٱلذُّلِّ مِنَ ٱلرَّحْمَةِ وَقُل رَّبِّ ٱرْحَمْهُمَا كَمَا رَبَّيَانِى صَغِيرًۭا, tr:vahfid lehümâ cenâha'z-zülli mine'r-rahmeti ve kul rabbi'rhamhümâ kemâ rabbeyânî sağîrâ, gloss:merhametten onlara alçakgönüllülük kanadını indir ve "Rabbim, onlar beni küçükken nasıl büyüttülerse sen de onlara öyle merhamet et" de, source:17:24}. Bu iki ayette "iyyâ" kelimesi, kulluk, alçalma, rahmet ve "rabbeyânî" kelimesindeki büyütme birlikte bulunur. Fâtiha'nın birinci, ikinci ve beşinci ayetlerinin kelimeleri burada bir ailenin içinde konuşur.

Musa'nın çocukluğu da bu görüntüyü sahneler. Allah Musa'nın annesine vahyeder: {ar:أَنْ أَرْضِعِيهِ ۖ فَإِذَا خِفْتِ عَلَيْهِ فَأَلْقِيهِ فِى ٱلْيَمِّ, tr:en erdı'îh, fe-izâ hıfti aleyhi fe-elkîhi fi'l-yemm, gloss:onu emzir; onun için korkarsan onu suya bırak, source:28:7}. Çocuk rahimden ayrılır ve anne boşlukla kalır: {ar:وَأَصْبَحَ فُؤَادُ أُمِّ مُوسَىٰ فَٰرِغًا, tr:ve asbaha fuâdü ümmi Mûsâ fârigâ, gloss:Musa'nın annesinin yüreği bomboş kaldı, source:28:10}. Kız kardeşi bir ev önerir: {ar:هَلْ أَدُلُّكُمْ عَلَىٰٓ أَهْلِ بَيْتٍۢ يَكْفُلُونَهُۥ لَكُمْ, tr:hel edüllüküm alâ ehli beytin yekfulûnehû leküm, gloss:size onu sizin için büyütecek bir ev halkı göstereyim mi, source:28:12}. Sonunda çocuk annesine geri verilir: {ar:فَرَدَدْنَٰهُ إِلَىٰٓ أُمِّهِۦ كَىْ تَقَرَّ عَيْنُهَا, tr:fe-radednâhü ilâ ümmihî key tekarra aynühâ, gloss:gözü aydın olsun diye onu annesine geri verdik, source:28:13}. Allah aynı olayı Musa'ya anlatırken büyütmenin asıl gözetenini söyler: {ar:وَلِتُصْنَعَ عَلَىٰ عَيْنِىٓ, tr:ve li-tusna'a alâ aynî, gloss:gözümün önünde yetiştirilesin diye, source:20:39}. Firavun'un {ar:أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا, tr:e-lem nurabbike fînâ velîdâ, gloss:seni küçükken aramızda biz büyütmedik mi, source:26:18} sözü bu yüzden yarım bir iddiadır. Çocuğun asıl büyütülmesi annesinin göğsünde ve Rabbin gözü önünde olmuştur. Büyütme öğretmeye uzandığında Kur'an şunu söyler: {ar:وَلَٰكِن كُونُوا۟ رَبَّٰنِيِّۦنَ بِمَا كُنتُمْ تُعَلِّمُونَ ٱلْكِتَٰبَ, tr:ve lâkin kûnû rabbâniyyîne bimâ küntüm tu'allimûne'l-kitâb, gloss:kitabı öğretmenizden dolayı rabbâniler olun, source:3:79}. Rahman da bir öğretici olarak anılır: {ar:ٱلرَّحْمَٰنُ, tr:er-rahmân, gloss:Rahman, source:55:1}, {ar:عَلَّمَ ٱلْقُرْءَانَ, tr:allemel-kur'ân, gloss:Kur'an'ı öğretti, source:55:2}, {ar:خَلَقَ ٱلْإِنسَٰنَ, tr:halaka'l-insân, gloss:insanı yarattı, source:55:3}, {ar:عَلَّمَهُ ٱلْبَيَانَ, tr:allemehü'l-beyân, gloss:ona açıklamayı öğretti, source:55:4}.

Kaynaklar: 1:1 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ ر ح م B001, B002, B003, B004; 1:2 رَبِّ ر ب ب B002, B003, B005, B009; 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ ر ح م B001, B003; 1:6 ٱلْمُسْتَقِيمَ ق و م B004; 1:7 أَنْعَمْتَ ن ع م B002; 1:7 غَيْرِ غ ي ر B001, B004

## Tamamlanan nimet ve başa kakılan nimet

Bir iyilik bir el ile uzatılır: {ar:النعمة اليد والصنيعة والمنة وما أنعم به عليك, tr:en-ni'metü'l-yedü ve's-sanî'atü ve'l-minnetü ve mâ en'ame bihî aleyk, gloss:nimet el, iyilik, lütuf ve sana verilen şeydir, source:"ن ع م,B001"}. Nimet vermek, iyiliği başkasına ulaştırmaktır: {ar:النعمة الحالة الحسنة والإنعام إيصال الإحسان إلى الغير, tr:en-ni'metü'l-hâletü'l-hasene ve'l-in'âmü îsâlü'l-ihsâni ile'l-gayr, gloss:nimet güzel haldir; in'âm, iyiliği başkasına ulaştırmaktır, source:"ن ع م,B001"}. Aynı fiil bir işi sonuna kadar ve fazlasıyla yapmayı da anlatır: {ar:أنعم أفضل وزاد, tr:en'ame efdale ve zâd, gloss:en'ame, fazlasını verdi ve artırdı demektir, source:"ن ع م,B010"}. Bu kullanım günlük işlerde de görülür: {ar:دققت دواء فأنعمت دقه أي بالغت وزدت, tr:dekaktü devâen fe-en'amtü dakkahû, gloss:ilacı dövdüm ve iyice, sonuna kadar dövdüm, source:"ن ع م,B010"}. İkinci ayetteki "Rab" kelimesi iyiliği tamamlamayı anlatır: {ar:رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها, tr:rabbe'r-racülü'n-ni'mete yerubbühâ, gloss:adam nimeti tamamladı, source:"ر ب ب,B002"}, {ar:رب فلان الصنيعة إذا أتمها وأصلحها, tr:rabbe fülânüni's-sanî'ate, gloss:falanca iyiliğini tamamlayıp düzene koydu, source:"ر ب ب,B002"}. Nimetin kendisi de aynı köktendir: {ar:الربى: النعمة والإحسان, tr:er-rubbâ: en-ni'metü ve'l-ihsân, gloss:rubbâ nimet ve iyiliktir, source:"ر ب ب,B016"}.

Alan kişinin cevabı hamddır. Hamd şükürden daha geniştir: {ar:الحمد أعم من الشكر, tr:el-hamdü eammü mine'ş-şükr, gloss:hamd şükürden daha kapsamlıdır, source:"ح م د,B001"}. Hamdın bir biçimi, verenin iyiliklerini başkalarının yanında saymaktır: {ar:أحمد إليك الله أي معك, tr:ahmedü ileyke'llâh, gloss:seninle birlikte Allah'a hamd ederim, source:"ح م د,B006"}, {ar:أشكر إليك أياديه ونعمه, tr:eşkürü ileyke eyâdîhi ve niamah, gloss:onun iyiliklerini ve nimetlerini sana anlatarak şükrederim, source:"ح م د,B006"}. Aynı kökte bunun tersi de vardır, iyiliği alanın başına kakmak: {ar:فلان يتحمد علي أي يمن, tr:fülânün yetehammedü aleyye, gloss:falanca bana iyiliğini başıma kakıyor, source:"ح م د,B005"}. Kendine harcadığını başkalarının yanında öne sürmek de böyle anılır: {ar:من أنفق ماله على نفسه فلا يتحمد به إلى الناس, tr:men enfeka mâlehû alâ nefsihî fe-lâ yetehammedü bihî ile'n-nâs, gloss:malını kendine harcayan, bunu insanlara karşı iyilik diye öne sürmesin, source:"ح م د,B005"}.

Sure bu sahneyi dikkat çekici bir sırayla kurar. Birinci ayetteki merhamet iyiliğin kaynağıdır, çünkü rahmet iyilik etmeyi gerektiren bir inceliktir. İkinci ayet cevabı en başa koyar: {ar:ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:el-hamdü lillâhi rabbi'l-âlemîn, gloss:hamd âlemlerin Rabbi Allah'adır, source:1:2}. Hamd edilen burada iyiliği tamamlayan Rab olarak anılır. Nimetin kendisi ise ancak yedinci ayette adıyla geçer: {ar:أَنْعَمْتَ عَلَيْهِمْ, tr:en'amte aleyhim, gloss:onlara nimet verdin, source:1:7}. Teşekkür, sayılan iyilikten önce gelir. Düz bir meal "hamd" ile "nimet" arasındaki bu bağı göstermez. Görüntü ise iyiliğin elden ele geçişini gösterir: Bir el uzanır, iyilik sonuna kadar götürülür, alan da verenin iyiliklerini başkalarının yanında sayar. Yedinci ayetteki nimet ayrıca bir yol nimetidir. Kendilerine nimet verilenler, yolları istenen kişilerdir. Nimetin tamamlanması da o yolda yürümekle olur.

Kur'an nimetin tamamlanmasını ile yola iletmeyi birçok yerde birlikte anar. Peygambere açık bir fetih verildiği bildirilir: {ar:إِنَّا فَتَحْنَا لَكَ فَتْحًۭا مُّبِينًۭا, tr:innâ fetahnâ leke fethan mübînâ, gloss:biz sana apaçık bir fetih verdik, source:48:1}. Bunun ardından şu gelir: {ar:وَيُتِمَّ نِعْمَتَهُۥ عَلَيْكَ وَيَهْدِيَكَ صِرَٰطًۭا مُّسْتَقِيمًۭا, tr:ve yütimme ni'metehû aleyke ve yehdiyeke sırâtan müstakîmâ, gloss:sana nimetini tamamlasın ve seni dosdoğru bir yola iletsin, source:48:2}. Burada Fâtiha'nın yedinci ve altıncı ayetleri tek cümlede birleşir. Kıblenin Mescid-i Haram'a çevrilmesi emredildiğinde de aynı ikili görülür: {ar:وَلِأُتِمَّ نِعْمَتِى عَلَيْكُمْ وَلَعَلَّكُمْ تَهْتَدُونَ, tr:ve li-ütimme ni'metî aleyküm ve lealleküm tehtedûn, gloss:size nimetimi tamamlayayım ve yolu bulasınız diye, source:2:150}. Bu ayette tamamlanan nimet yüzü bir eve döndürmekle birliktedir. Dinin kemale ermesi de aynı fiille söylenir: {ar:ٱلْيَوْمَ أَكْمَلْتُ لَكُمْ دِينَكُمْ وَأَتْمَمْتُ عَلَيْكُمْ نِعْمَتِى, tr:el-yevme ekmeltü leküm dîneküm ve etmemtü aleyküm ni'metî, gloss:bugün dininizi kemale erdirdim ve size nimetimi tamamladım, source:5:3}. Yakup oğlu Yusuf'a nimetin bir soy boyunca tamamlandığını anlatır: {ar:وَيُتِمُّ نِعْمَتَهُۥ عَلَيْكَ وَعَلَىٰٓ ءَالِ يَعْقُوبَ كَمَآ أَتَمَّهَا عَلَىٰٓ أَبَوَيْكَ مِن قَبْلُ, tr:ve yütimmü ni'metehû aleyke ve alâ âli Ya'kûbe kemâ etemmehâ alâ ebeveyke min kabl, gloss:daha önce iki atana tamamladığı gibi sana ve Yakup ailesine nimetini tamamlayacak, source:12:6}. Bu ayet, nimetin yedinci ayetteki "onlar" gibi bir topluluğa ait olduğunu gösterir. İbrahim'in cevabı da aynı sıradadır: {ar:شَاكِرًۭا لِّأَنْعُمِهِ ۚ ٱجْتَبَىٰهُ وَهَدَىٰهُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:şâkiran li-en'umih, ictebâhü ve hedâhü ilâ sırâtın müstakîm, gloss:onun nimetlerine şükrederdi; onu seçti ve dosdoğru bir yola iletti, source:16:121}. Nimeti başkalarının yanında anlatmak, Peygambere emredilen bir şeydir: {ar:وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ, tr:ve emmâ bi-ni'meti rabbike fe-haddis, gloss:Rabbinin nimetini ise anlat, source:93:11}. Kulluk da nimete verilen cevap olarak gösterilir: {ar:فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ, tr:fe'l-ya'büdû rabbe hâze'l-beyt, gloss:bu evin Rabbine kulluk etsinler, source:106:3}, {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ellezî at'amehüm min cû'in ve âmenehüm min havf, gloss:onları açlıktan doyuran ve korkudan emin kılan, source:106:4}. Yolun sonunda hamd yeniden duyulur. Cennettekiler şöyle der: {ar:ٱلْحَمْدُ لِلَّهِ ٱلَّذِى هَدَىٰنَا لِهَٰذَا, tr:el-hamdü lillâhi'llezî hedânâ li-hâzâ, gloss:bizi buna ileten Allah'a hamd olsun, source:7:43}. Onların son sözü surenin ikinci ayetidir: {ar:وَءَاخِرُ دَعْوَىٰهُمْ أَنِ ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve âhiru da'vâhüm eni'l-hamdü lillâhi rabbi'l-âlemîn, gloss:dualarının sonu "hamd âlemlerin Rabbi Allah'adır" sözüdür, source:10:10}. Fâtiha'nın başta söylediği söz, yolun sonunda yeniden söylenir. Başa kakılan nimetin sahnesi ise Firavun'un sarayındadır. Firavun büyüttüğünü iddia eder, Musa da {ar:وَتِلْكَ نِعْمَةٌۭ تَمُنُّهَا عَلَىَّ, tr:ve tilke ni'metün temünnühâ aleyye, gloss:başıma kaktığın o nimet, source:26:22} diye cevap verir. Bu, "yetehammedü aleyye" sözünün sahnesidir.

Kaynaklar: 1:1 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ ر ح م B001; 1:2 ٱلْحَمْدُ ح م د B001, B005, B006; 1:2 رَبِّ ر ب ب B002, B016; 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ ر ح م B001; 1:7 أَنْعَمْتَ ن ع م B001, B010

## Buluşmalar

Görüntülerin en sık buluştuğu yer "na'büdü" kelimesidir. Aynı sıfat, "müzellel", hem çiğnenmiş yolu hem de katranlanmış deveyi anlatır. Beşinci ayetin kulu, ayakların düzlediği yolun yüzeyiyle aynı kelimeden konuşur. Altıncı ayet hemen ardından bu yolu ister. Kulluk ile yol arasındaki bağı Kur'an da açıkça kurar: {ar:وَأَنِ ٱعْبُدُونِى ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ, tr:ve eni'budûnî, hâzâ sırâtun müstakîm, gloss:bana kulluk edin; işte bu dosdoğru yoldur, source:36:61}. Bu cümlede ikinci görüntü ile birinci görüntü tek bir şeyin iki adıdır. Uysallaşmış kul yolun kendisidir, yürünen yol da kulluğun kendisidir.

Sürü ile yol, başıboş devede buluşur. Başıboş deve "Rabbi bilinmeyen" ve "mâliki bilinmeyen" deve olarak tanımlanır. Böylece ikinci ve dördüncü ayetlerin sahiplik adları, yedinci ayetin son kelimesinin tanımına girer. "Hâdî" kelimesi hem yolcunun önünden giden kılavuzu hem de sürünün başındaki öncüyü adlandırır. Kur'an bu iki sahneyi tek bir akışta anlatır: Sürünün otlağa gidiş ve dönüşünün güzelliğinden hemen sonra şöyle der: {ar:وَعَلَى ٱللَّهِ قَصْدُ ٱلسَّبِيلِ وَمِنْهَا جَآئِرٌۭ, tr:ve alellâhi kasdü's-sebîli ve minhâ câir, gloss:doğru yol Allah'a varır; yollardan bazısı ise yana sapar, source:16:9}. Sürü ile eve götürülen kurbanlık da aynı yerde buluşur. Kurbanlık sürüden ("neam") ayrılır, üzerinde ad söylenir ve Eve ulaştırılır. Kur'an bu sahneyi şu sözle kapatır: {ar:لِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ, tr:li-tükebbirullâhe alâ mâ hedâküm, gloss:sizi yola ilettiği için Allah'ı yüceltesiniz diye, source:22:37}. Burada sürü, ad, uysallaştırma ve hidayet aynı pasajda bir aradadır.

Rahim ile tamamlanan nimet "Rab" kelimesinde birleşir. Aynı fiil hem çocuğu büyütmeyi hem de nimeti tamamlamayı anlatır ve her ikisi de "tamamlanma sınırına kadar" yürür. Bu ikisini Kur'an'da bir sarayın içinde, bir tartışmanın ortasında görmek mümkündür. Firavun {ar:أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا, tr:e-lem nurabbike fînâ velîdâ, gloss:seni küçükken aramızda biz büyütmedik mi, source:26:18} diye büyütmeyi bir alacak gibi öne sürer. Musa kendi geçmişinden şöyle söz eder: {ar:قَالَ فَعَلْتُهَآ إِذًۭا وَأَنَا۠ مِنَ ٱلضَّآلِّينَ, tr:kâle fealtühâ izen ve ene mine'd-dâllîn, gloss:dedi ki: onu yaptığımda ben yolunu bilmeyenlerden idim, source:26:20}. Ardından şöyle der: {ar:فَوَهَبَ لِى رَبِّى حُكْمًۭا وَجَعَلَنِى مِنَ ٱلْمُرْسَلِينَ, tr:fe-vehebe lî rabbî hukmen ve cealenî mine'l-mürselîn, gloss:Rabbim bana hikmet verdi ve beni elçilerden kıldı, source:26:21}. Son olarak da başa kakılan nimeti ve köleleştirmeyi tek cümlede adlandırır {source:26:22}. Bu kısa konuşmada büyütme, başa kakılan nimet, zorla köle edinme, "dâllîn" kelimesi ve gerçek Rabbin verdiği şey bir arada bulunur. Böylece beş görüntü birbirinden ayrılarak tek bir sahnede görünür: Sahte büyüten ile gerçek Rab, başa kakılan iyilik ile tamamlanan iyilik, zorla köle edilen halk ile kendi isteğiyle kul olan elçi.

Rıza ve gazap ile hesap günü bir sahnede buluşur. "Allah'ın günleri", bazılarına azabın, bazılarına da bağışlamanın indiği günlerdir. Hesap gününün yüzleri bu ikiliği taşır: Biri yumuşamış ("nâime"), öbürü üstüne toz inmiş bir yüzdür. Gazap ile yol da buluşur: {ar:وَمَن يَحْلِلْ عَلَيْهِ غَضَبِى فَقَدْ هَوَىٰ, tr:ve men yahlil aleyhi gadabî fe-kad hevâ, gloss:kimin üzerine gazabım inerse o düşmüştür, source:20:81}. Bu düşüşün karşısında "sonra yolunu bulan" kişi durur {source:20:82}. Gazaba uğrayan, yolda tökezleyip yere kapanan kişidir. Yolu bulan ise doğrulup dimdik yürüyen kişidir. Bu dimdik yürüyüş, dayanmak ve doğrulmak görüntüsüyle de birleşir: {ar:أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:e-fe men yemşî mükibben alâ vechihî ehdâ em men yemşî seviyyen alâ sırâtın müstakîm, gloss:yüzüstü kapanarak yürüyen mi yolu daha iyi bulur, yoksa dosdoğru bir yolda dimdik yürüyen mi, source:67:22}.

Hesap günü ile terazi, borç ile gözden kaybolmak tek bir ayette yan yana durur. Borç ayetinde borç, vade, tanığın unutması ("en tadılle") ve "akvem" sıfatı bir aradadır {source:2:282}. Burada unutkanlık bir kaybolma olarak, düzgün yazı da bir dik durma olarak görünür. Terazi ile gök de "kâme mîzânü'n-nehâr" sözünde buluşur. Öğle güneşi tepede dikildiğinde gündüzün terazisi dengeye gelir. Aynı kök hem eğilmeyen teraziye hem de hesap gününde ayağa kalkan insanlara ad verir. Ölçüde hile yapanlar sahnesi bunları bir araya getirir. Eksik tartanlar, insanların âlemlerin Rabbi için ayağa kalkacağı güne bağlanır {source:83:6}.

Su ile yol, Musa'nın Medyen yolculuğunda buluşur. Musa önce yolun ortasına iletilmeyi diler {source:28:22}. Sonra kuyuya varır ve başkalarına su verir. Ardından gölgeye çekilip Rabbine muhtaç olduğunu söyler {source:28:24}. Kiriş ("neâme") ve ondan sarkan makara ("kâme") yedinci ve altıncı ayetin kelimelerini kuyunun ağzında birleştirir. Musa'nın sahnesi de aynı kelimeleri bir yolcunun hayatında birleştirir: Yol, su ve gölge. İbrahim'in sözü bu buluşmayı surenin sırasıyla dile getirir. Âlemlerin Rabbini anlatırken önce {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:ellezî halakanî fe-hüve yehdîn, gloss:beni yaratan, bana yolu gösteren O'dur, source:26:78} der, sonra yedirip içireni anar {source:26:79} ve sonunda din gününde bağışlanmayı umar {source:26:82}. Yaratma, yola iletme, su verme ve din günü, bir insanın ağzında sırayla dizilir.

Gök ile yol ve sahiplik de İbrahim'in gece sahnesinde buluşur. Ufuktan yükselen yıldız, ay ve güneş birer "semâve", yani yükselen birer şekildir. İbrahim her birine "bu benim Rabbim" der. Hiçbirinin Rab olmadığını batışlarından anlar ve yola iletilmezse yolunu yitirmiş kavimden olacağını söyler {source:6:77}. Ad ve damga görüntüsü bu sahneye bir ayrım ekler: Yükselen her şey bir işarettir, fakat işaret, işaret ettiği şeyin kendisi değildir. Güneşe tapanlar bu ayrımı kaçırır ve yoldan alıkonur {source:27:24}.

Bütün bu buluşmalar surenin hareketini taşır. Sure tanıtan bir adla, yani yükseltilmiş bir işaretle başlar. İkinci ve üçüncü ayetler, rahimde biçimlendiren, büyüten, bulutla bitkiyi besleyen ve nimeti tamamlayan Rabbi anar. Hamd, iyiliğin adı geçmeden önce cevap olarak söylenir. Dördüncü ayet, bir hükümdarın elinde toplanan mülkü ve bir günü, yani borcun kapandığı, terazinin eğilmediği ve insanların ayağa kalktığı günü getirir. Beşinci ayette konuşan değişir. Sahip olunan, sahibine doğrudan seslenir. Kendi isteğiyle boyun eğer, ama bineği yorulmuş bir yolcu olduğu için yardım ister. Altıncı ayette bu yolcu, önden giden bir kılavuzla ve iki yanından tutularak, başkalarının düzlediği yolda yürümeyi ve sürünün öncüsünün ardından gitmeyi diler. Yolun bir kuyusu ve bir varış evi vardır. Yedinci ayet bu yolu bir topluluğa bağlar. Yolu yitirmenin iki yüzünü de gösterir: Birinde gazap iner ve yüz kızarır, öbüründe hayvan sahibinden kopar ve izi kaybolur. Böylece sure, işaretinden tanınan sahipten başlayıp, sahibini tanımayan başıboş devede biter. Arada istenen tek şey, yolun sonundaki eve götürülmektir.

