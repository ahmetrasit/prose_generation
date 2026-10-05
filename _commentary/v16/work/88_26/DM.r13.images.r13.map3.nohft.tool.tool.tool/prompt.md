Focus: 88:26. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_26/D.r13/context.md =====
# 88:26 — focus

ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم

Anchor translation (canonical reading, reference only):

Sonra onların hesabını görmek kesinlikle bize düşer.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ثُمَّ | ثُمّ |  | CONJ |
| 2 | إِنَّ | إِنّ |  | ACC |
| 3 | عَلَيْنَا | عَلَىٰ |  | P;PRON |
| 4 | حِسَابَهُم | حِسَاب | ح س ب | N;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 88 — full text (context; no pericope)

- 88:1 هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ
- 88:2 وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ
- 88:3 عَامِلَةٌۭ نَّاصِبَةٌۭ
- 88:4 تَصْلَىٰ نَارًا حَامِيَةًۭ
- 88:5 تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
- 88:6 لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
- 88:7 لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
- 88:8 وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ
- 88:9 لِّسَعْيِهَا رَاضِيَةٌۭ
- 88:10 فِى جَنَّةٍ عَالِيَةٍۢ
- 88:11 لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ
- 88:12 فِيهَا عَيْنٌۭ جَارِيَةٌۭ
- 88:13 فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ
- 88:14 وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ
- 88:15 وَنَمَارِقُ مَصْفُوفَةٌۭ
- 88:16 وَزَرَابِىُّ مَبْثُوثَةٌ
- 88:17 أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ
- 88:18 وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ
- 88:19 وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- 88:20 وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- 88:21 فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- 88:22 لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 88:23 إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- 88:24 فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ◀ focus ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_26/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ح س ب (root_000318) — identity root of حِسَابَهُم (w4)

- **B001** sayarak nicelik belirleme — nesneyi saymak ve niceliğini çıkarmak · sayma ve nicelik belirleme işlemi · sayma işlemi · sayı yoluyla belirleme · belirli sayı düzeni ve zaman ölçüsü · ölçmeden, denetlemeden veya kısmadan; beklenenden fazla · sayıp değerlendiren ve gözeten
  الأول العد؛ الحساب عدك الأشياء؛ حسبت الحساب؛ حسبته إذا عددته؛ الحساب استعمال العدد؛ الشمس والقمر بحسبان
- **B002** öyle olduğunu sanmak — öyle sanmak ve zihnen öyle olduğuna hükmetmek · sanı ve kesin olmayan yargı
  الحسبان الظن؛ حسبت كذا في معنى ظننت؛ حسبته صالحا أي ظننته؛ حسبت الشيء ظننته؛ الحسبان أن يحكم لأحد النقيضين
- **B003** gereksinimi karşılayacak kadar yetmek — bu sana yeter; bununla yetin · Tanrı bize yeter · bu bana yetti · ona yetecek veya onu hoşnut edecek kadar vermek · yeterli ya da bol armağan · ölçmeden, denetlemeden veya kısmadan; beklenenden fazla · soyluluk ile yeterlik arasında iki türlü yorumlanan şiir sözü
  الأصل الثاني الكفاية؛ حسبك هذا أي كفاك؛ حسبي كذا أي يكفيني؛ أحسبني الشيء أي كفاني؛ حسبنا الله أي كافينا هو؛ عطاء حسابا أي كافيا
- **B004** atalardan gelen saygınlık ve iyi işler birikimi — atalardan gelen saygınlık ve övünülecek işler · soylu, saygın veya eli açık kişi · soyluluk ya da yeterlik diye yorumlanan şiir sözü
  الحسب الذي يعد من الإنسان؛ الحسب الشرف الثابت في الآباء؛ حسب الرجل مآثر آبائه وأجداده؛ ما يعده الإنسان من مفاخر آبائه؛ الحسب الفعال الحسن له ولآبائه
- **B005** Tanrı katında karşılığını beklemek — bir işi veya kaybı Tanrı katında değer hanesine yazıp karşılığını beklemek · Tanrı katında karşılık umularak yapılan iş
  احتسب فلان ابنه؛ احتسابك الأجر؛ احتسب فلان عند الله خيرا؛ احتسبت بكذا أجرا عند الله؛ احتسب ابنا له أي اعتد به عند الله؛ الحسبة فعل ما يحتسب به عند الله تعالى
- **B006** işi gözetme, kötü davranışı sorgulama ve kamusal denetim — kötü davranışından dolayı kınamak ve yaptığını sorgulamak · işi iyi çekip çevirmek ve gözetmek · kentte kamu düzenini ve davranışları gözeten görevli
  حسن الحسبة بالأمر إذا كان حسن التدبير؛ احتسب فلان على فلان أنكر عليه قبيحا عمله؛ احتسبت عليه كذا إذا أنكرته عليه؛ فلان محتسب البلد؛ حسن الحسبة في الأمر
- **B007** kısa ok veya yukarıdan gelen yıkıcı gönderim — kısa oklar veya atılan küçük nesneler · gökten gönderilen dolu, ateş, çekirge ya da yıkıcı şey
  الحسبان سهام صغار؛ حسبان من السماء بالبرد؛ حسبانا من السماء أي نارا تحرقها؛ حسبانا عذابا ولا أدري؛ الحسبان بالضم العذاب؛ أصاب الأرض حسبان أي جراد؛ الحسبان المرامي؛ نارا وعذابا
- **B008** yalıtık adlandırmalar — küçük yastık · deriden yapılmış veya baş altına konan yastık · birini yastığa oturtmak veya başına yastık koymak · yastıksız; bazı açıklamalarda ölü sargısına sarılmamış, gömülmemiş ya da onurlandırılmamış
  الحسبان جمع حسبانة وهي الوسادة الصغيرة؛ الحسبان سهام قصار؛ الحسبانة أيضا الوسادة الصغيرة؛ المحسبة وسادة من أدم؛ حسبته إذا وسدته؛ الحسبانة الوسادة الصغيرة
- **B009** deri veya tüyde karışık ak, kızıl ve koyu görünüm — derisi hastalıkla beyazlamış ya da tüyünde aklık, kızıllık ve koyuluk karışmış kişi veya deve · koyu zemin üstünde bozluk ya da kızıla çalan karalık
  الأحسب الذي ابيضت جلدته من داء؛ الأحسب من الناس والإبل وهو الأبرص؛ الحسبة غبرة في كدرة؛ الأحسب من الإبل فيه بياض وحمرة؛ الحسبة سواد يضرب إلى الحمرة
- **B010** yalıtık adlandırmalar — haberi sorup izini sürmek · birinin elinde ne olduğunu sınayıp öğrenmek
  بغير أن حسب المعطى أنه يعطيه؛ تحسبت الخبر أي استخبرت؛ احتسبت فلانا اختبرت ما عنده؛ يتحسب الأخبار أي يتحسسها ويطلبها

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:26, and ## Buluşmalar) =====
## Emek, ücret ve sayım

Üçüncü ayetteki ilk sıfat amaçlı yapılan iştir: {ar:كل فعل يكون من الحيوان بقصد, tr:küllü fi'lin yekûnu mine'l-hayevâni bi-kasd, gloss:canlıdan kasıtla çıkan her iş, source:"ع م ل,B001"}. Böyle bir iş karşılığında ücret beklenir: {ar:العمالة أجر ما عمل, tr:el-umâletü ecru mâ amel, gloss:umâle yapılan işin ücretidir, source:"ع م ل,B004"}. İkinci sıfatın kökü ise hem yorgunluğu hem de pay almayı anlatır: {ar:النصيب الحظ من الشيء, tr:en-nasîbu'l-hazzu mine'ş-şey', gloss:nasip bir şeyden düşen paydır, source:"ن ص ب,B005"}. Ayetteki anlam yorgunluktur. Yanında ise payın kendisi duyulur. Bu yüz çalışmış ve yorulmuştur, ama eline geçen tek şey yorgunluktur. Yedinci ayet bu kazancın neye yaradığını söyler: {ar:الغناء بالفتح الكفاية ولا يغني أي لا يكفي, tr:el-ğanâu bi'l-feth el-kifâye ve lâ yuğnî ey lâ yekfî, gloss:ğanâ yeterliliktir; lâ yuğnî yetmez demektir, source:"غ ن ي,B002"}.

Dokuzuncu ayet karşı tarafı tek bir kelimeyle kurar: {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdiye, gloss:çabasından hoşnut, source:88:9}. Çaba, kazanç getiren iştir: {ar:كل عمل من خير أو شر فهو السعي؛ السعي العمل أي الكسب, tr:küllü amelin min hayrin ev şerrin fe-huve's-sa'y; es-sa'yu'l-amel ey el-kesb, gloss:iyi ya da kötü her iş sa'ydir; sa'y kazançtır, source:"س ع ي,B002"}. Hoşnutluk iki yönlüdür: {ar:ورضا العبد عن الله ورضا الله عن العبد, tr:ve rıda'l-abdi anillâhi ve rıdallâhi ani'l-abd, gloss:kulun Allah'tan ve Allah'ın kuldan razı olması, source:"ر ض و,B001"}. Bu yüz dönüp kendi emeğine bakar ve gördüğünden memnun kalır. Öteki yüzün emeği ise üstünde yorgunluk olarak kalmıştır.

On birinci ayetteki kelimenin bir başka kolu, hesaba geçmeyen şeyi anlatır: {ar:ألغيت هذه الكلمة أي رأيتها باطلا وفضلا وحشوا وما يلغى من الحساب, tr:elğaytü hâzihi'l-kelimete ey raeytühâ bâtılen ve fadlen ve haşven ve mâ yulğâ mine'l-hısâb, gloss:bu sözü boş ve fazlalık saydım; hesaptan düşülen şey, source:"ل غ و,B001"}. Yirmi altıncı ayet de bir sayımla kapanır: {ar:الحساب عدك الأشياء, tr:el-hısâbu addüke'l-eşyâ', gloss:hesap şeyleri tek tek saymandır, source:"ح س ب,B001"}. Bahçede boş söz işitilmez. Hesapta da boş olan sayılmaz. Sayım ise surenin sonunda yalnızca "Bize" aittir.

Kur'an emeğin hesabını açıkça anlatır. Musa'nın ve İbrahim'in sayfalarında bulunduğu bildirilen sözler arasında şunlar vardır: {ar:وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ, tr:ve en leyse li'l-insâni illâ mâ seâ, gloss:insan için çabaladığından başkası yoktur, source:53:39}; {ar:وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ, tr:ve enne sa'yehû sevfe yurâ, gloss:çabası görülecektir, source:53:40}; {ar:ثُمَّ يُجْزَىٰهُ ٱلْجَزَآءَ ٱلْأَوْفَىٰ, tr:summe yuczâhu'l-cezâe'l-evfâ, gloss:sonra karşılığı tam olarak verilecektir, source:53:41}. Ahireti isteyip onun için çabalayanların çabası {ar:فَأُو۟لَٰٓئِكَ كَانَ سَعْيُهُم مَّشْكُورًۭا, tr:fe-ülâike kâne sa'yuhum meşkûrâ, gloss:işte onların çabası karşılık görür, source:17:19} diye anılır. Bahçe halkına, gümüş kaplarla ve kadehlerle ağırlandıktan sonra şöyle denir: {ar:وَكَانَ سَعْيُكُم مَّشْكُورًا, tr:ve kâne sa'yukum meşkûrâ, gloss:çabanız karşılık gördü, source:76:22}. Büyük felaket geldiğinde çaba yeniden hatırlanır: {ar:يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ, tr:yevme yetezekkeru'l-insânu mâ seâ, gloss:insanın çabaladığı şeyi hatırlayacağı gün, source:79:35}. Boşa giden emek için ise şöyle denir: {ar:فَجَعَلْنَٰهُ هَبَآءًۭ مَّنثُورًا, tr:fe-cealnâhu hebâen mensûrâ, gloss:onu dağılmış toza çevirdik, source:25:23}. Başka bir yerde de {ar:ٱلَّذِينَ ضَلَّ سَعْيُهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَهُمْ يَحْسَبُونَ أَنَّهُمْ يُحْسِنُونَ صُنْعًا, tr:ellezîne dalle sa'yuhum fi'l-hayâti'd-dünyâ ve hum yahsebûne ennehum yuhsinûne sun'â, gloss:dünya hayatında çabaları boşa gidip de güzel iş yaptıklarını sananlar, source:18:104} diye anlatılırlar. Buradaki "sanmak" fiili hesap ile aynı köktendir. Bu insanlar yanlış saymıştır.

Bu sahnelerin en yakını, kitabı sağından verilen kişinin sevincidir: {ar:إِنِّى ظَنَنتُ أَنِّى مُلَٰقٍ حِسَابِيَهْ, tr:innî zanentu ennî mulâkin hısâbiyeh, gloss:hesabıma kavuşacağımı zaten biliyordum, source:69:20}. Ardından surenin dokuzuncu ve onuncu ayetlerindeki sözler gelir: {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:artık o hoşnut bir yaşayıştadır, source:69:21}; {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüce bir bahçede, source:69:22}. Kitabı solundan verilen ise {ar:وَلَمْ أَدْرِ مَا حِسَابِيَهْ, tr:ve lem edri mâ hısâbiyeh, gloss:keşke hesabımın ne olduğunu bilmeseydim, source:69:26} der. Teraziler tartıldığında ağır gelen de {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:o hoşnut bir yaşayıştadır, source:101:7} diye anılır. Hesap kökü yetecek kadar vermeyi de anlatır: {ar:عطاء حسابا أي كافيا, tr:atâen hısâben ey kâfiyen, gloss:yeterli bir bağış, source:"ح س ب,B003"}. Kur'an bunu takva sahiplerinin karşılığı için söyler: {ar:جَزَآءًۭ مِّن رَّبِّكَ عَطَآءً حِسَابًۭا, tr:cezâen min rabbike atâen hısâbâ, gloss:Rabbinden bir karşılık; yeterli bir bağış, source:78:36}. Birinin emeği "yetmez" diye biter. Ötekinin karşılığı "yeter" diye verilir.

Kaynaklar: 88:3 عَامِلَةٌ ع م ل B001; 88:3 عَامِلَةٌ ع م ل B004; 88:3 نَّاصِبَةٌ ن ص ب B004; 88:3 نَّاصِبَةٌ ن ص ب B005; 88:7 يُغْنِى غ ن ي B002; 88:9 لِّسَعْيِهَا س ع ي B002; 88:9 رَاضِيَةٌ ر ض و B001; 88:11 لَٰغِيَةً ل غ و B001; 88:26 حِسَابَهُم ح س ب B001; 88:26 حِسَابَهُم ح س ب B003

## Hatırlatıcı, gözetmen değil

Yirmi birinci ayet Peygamber'in işini tek bir kelimeye indirir: hatırlatmak. "Ancak" sözü bu işin sınırını çizer. Hatırlatma, bir şeyin akla getirilmesini sağlayan şeydir ve tekrar edilir: {ar:التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر, tr:et-tezkiretü mâ yütezekkeru bihi'ş-şey' ve'z-zikrâ kesretü'z-zikr, gloss:tezkire bir şeyin hatırlandığı araçtır; zikra çok anmaktır, source:"ذ ك ر,B009"}. Yirmi ikinci ayet de bu işin olmadığı şeyi söyler: {ar:لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ, tr:leste aleyhim bi-musaytır, gloss:sen onların üstünde bir gözetmen değilsin, source:88:22}. Musaytır, bir şeyin başına konup onu gözeten ve yaptığını yazan kişidir: {ar:المسيطر والمصيطر المسلط على الشيء ليشرف عليه ويتعهد أحواله ويكتب عمله, tr:el-museytıru ve'l-musaytıru'l-musallatu ale'ş-şey'i li-yuşrife aleyhi ve yeteahhede ahvâlehû ve yektübe amelehû, gloss:bir şeyin başına konup onu gözeten halini kollayan ve işini yazan kişi, source:"س ط ر,B003"}; {ar:السيطرة مصدر المسيطر وهو كالرقيب الحافظ المتعهد للشيء, tr:es-saytaratu masdaru'l-museytır ve huve ke'r-rakîbi'l-hâfızı'l-müteahhidi li'ş-şey', gloss:bir şeyi bekleyen ve koruyan gözcü gibi olan, source:"س ط ر,B003"}. Bu yetkinin asıl sahipleri efendilerdir: {ar:المسيطرون الأرباب المسلطون, tr:el-museytırûne'l-erbâbü'l-musallatûn, gloss:başa geçirilmiş efendiler, source:"س ط ر,B003"}. Kökün aslı satırdır: {ar:أصل مطرد يدل على اصطفاف الشيء كالكتاب والشجر, tr:aslun muttaridun yedullü ale'stıfâfi'ş-şey'i ke'l-kitâbi ve'ş-şecer, gloss:yazı ve ağaç gibi şeylerin dizilişini gösteren kök, source:"س ط ر,B001"}; {ar:السطر سطر من كتب وسطر من شجر مغروس, tr:es-satru satrun min kütübin ve satrun min şecerin mağrûs, gloss:satır yazıdan bir satır ve dikilmiş ağaçtan bir sıradır, source:"س ط ر,B001"}. Gözetmen, kayıtları satır satır tutan kişidir. Bu kökün tanımında geçen diziliş kelimesi, on beşinci ayette yastıkların dizilişini anlatan kelimedir. Bu bağ kök birliğinden değil, kelimelerin açıklamasından gelir. Bahçede yastıkları dizen bir el vardır. Amelleri satıra dizen el de vardır, ama Peygamber'in eli değildir.

Kur'an bu kaydı Allah'a bağlar. Önceki kavimlerin anlatıldığı surenin sonunda şöyle denir: {ar:وَكُلُّ صَغِيرٍۢ وَكَبِيرٍۢ مُّسْتَطَرٌ, tr:ve küllü sağîrin ve kebîrin mustatar, gloss:küçük büyük her şey satır satır yazılmıştır, source:54:53}. Buradaki "yazılmış" kelimesi musaytır ile aynı köktendir. Kur'an'da bu kelimenin geçtiği tek başka yer, inkârcılara sorulan bir sorudur: {ar:أَمْ عِندَهُمْ خَزَآئِنُ رَبِّكَ أَمْ هُمُ ٱلْمُصَۣيْطِرُونَ, tr:em indehum hazâinu rabbike em humu'l-musaytırûn, gloss:yoksa Rabbinin hazineleri onların yanında mı, yoksa gözetmenler onlar mı, source:52:37}. Gözetmenlik ne Peygamber'indir ne de onu reddedenlerin.

Kur'an bu sınırı başka yerlerde de çizer. Kaf suresinin sonunda Allah şöyle der: {ar:وَمَآ أَنتَ عَلَيْهِم بِجَبَّارٍۢ ۖ فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ, tr:ve mâ ente aleyhim bi-cebbârin fe-zekkir bi'l-Kur'âni men yehâfu vaîd, gloss:sen onları zorlayan değilsin; tehdidimden korkana Kur'an ile hatırlat, source:50:45}. Başka yerlerde de {ar:فَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ حَفِيظًا ۖ إِنْ عَلَيْكَ إِلَّا ٱلْبَلَٰغُ, tr:fe-mâ erselnâke aleyhim hafîzan in aleyke ille'l-belâğ, gloss:seni onların üstüne bekçi göndermedik; sana düşen yalnızca duyurmaktır, source:42:48} ve {ar:وَمَا جَعَلْنَٰكَ عَلَيْهِمْ حَفِيظًۭا ۖ وَمَآ أَنتَ عَلَيْهِم بِوَكِيلٍۢ, tr:ve mâ cealnâke aleyhim hafîzan ve mâ ente aleyhim bi-vekîl, gloss:seni onlara bekçi yapmadık; sen onların vekili de değilsin, source:6:107} denir. Cezalandırmak da Allah'ın işidir: {ar:إِن يَشَأْ يَرْحَمْكُمْ أَوْ إِن يَشَأْ يُعَذِّبْكُمْ ۚ وَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ وَكِيلًۭا, tr:in yeşe' yerhamkum ev in yeşe' yuazzibkum ve mâ erselnâke aleyhim vekîlâ, gloss:dilerse size merhamet eder, dilerse azap eder; seni onlara vekil göndermedik, source:17:54}. Zorlama da sorunun içinde reddedilir: {ar:أَفَأَنتَ تُكْرِهُ ٱلنَّاسَ حَتَّىٰ يَكُونُوا۟ مُؤْمِنِينَ, tr:e-fe-ente tukrihu'n-nâse hattâ yekûnû mu'minîn, gloss:inanan olsunlar diye insanları sen mi zorlayacaksın, source:10:99}.

Yirmi üçüncü ayetteki istisna bu sınırın içinden çıkar: {ar:إِلَّا مَن تَوَلَّىٰ وَكَفَرَ, tr:illâ men tevellâ ve kefer, gloss:ancak yüz çevirip inkâr eden, source:88:23}. Yüz çevirme fiilinin kökü bir göreve geçmeyi de anlatır: {ar:تولى العمل أي تقلد, tr:tevelle'l-amele ey tekalled, gloss:işi üstlendi yani göreve geçti, source:"و ل ي,B003"}. Ayetteki anlam sırt dönmektir: {ar:ولى الرجل أي أدبر, tr:vellâ'r-raculu ey edbar, gloss:adam arkasını döndü, source:"و ل ي,B007"}. Yanında ise başa geçme anlamı duyulur. Peygamber'e verilmeyen göreve karşılık, yüz çeviren kendisi için yüz çevirmeyi üstlenmiştir. Yirmi dördüncü ayet cezayı Peygamber'e değil Allah'a verir: {ar:فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ, tr:fe-yuazzibuhullâhu'l-azâbe'l-ekber, gloss:Allah da onu en büyük azapla cezalandırır, source:88:24}. Allah'ın adı kulluk edilenin adıdır: {ar:فالإله الله تعالى لأنه معبود, tr:fe'l-ilâhu'llâhu teâlâ li-ennehû ma'bûd, gloss:ilah Allah'tır çünkü kulluk edilendir, source:"ء ل ه,B001"}. Son iki ayette konuşan "Biz" olur ve iş bölümü tamamlanır: {ar:إِنَّ إِلَيْنَآ إِيَابَهُمْ, tr:inne ileynâ iyâbehum, gloss:dönüşleri şüphesiz Bize'dir, source:88:25}; {ar:ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم, tr:summe inne aleynâ hısâbehum, gloss:sonra hesapları da şüphesiz Bize düşer, source:88:26}. Kur'an aynı bölüşümü tek bir cümlede söyler. Allah Peygamber'e, vaat edilenin bir kısmını ona göstersin ya da canını alsın, şunu der: {ar:فَإِنَّمَا عَلَيْكَ ٱلْبَلَٰغُ وَعَلَيْنَا ٱلْحِسَابُ, tr:fe-innemâ aleyke'l-belâğu ve aleyne'l-hısâb, gloss:sana düşen yalnızca duyurmaktır, hesap ise Bize düşer, source:13:40}. Önceki sure de aynı sırayı izler: önce {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-zekkir in nefeati'z-zikrâ, gloss:hatırlatma fayda verirse hatırlat, source:87:9}, sonra {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yezzekkeru men yahşâ, gloss:içi titreyen öğüt alacak, source:87:10}, sonra {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht ondan kaçınacak, source:87:11} ve en büyük ateş gelir. Başka yerlerde de şöyle denir: {ar:وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ, tr:ve zekkir fe-inne'z-zikrâ tenfeu'l-mu'minîn, gloss:hatırlat; hatırlatma inananlara fayda verir, source:51:55}; {ar:كَلَّآ إِنَّهَا تَذْكِرَةٌۭ, tr:kellâ innehâ tezkira, gloss:hayır; bu bir hatırlatmadır, source:80:11}; {ar:فَمَن شَآءَ ذَكَرَهُۥ, tr:fe-men şâe zekerah, gloss:dileyen onu anar, source:80:12}.

Kaynaklar: 88:21 فَذَكِّرْ ذ ك ر B009; 88:21 مُذَكِّرٌ ذ ك ر B003; 88:22 لَّسْتَ ل ي س B001; 88:22 بِمُصَيْطِرٍ س ط ر B001; 88:22 بِمُصَيْطِرٍ س ط ر B003; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:23 تَوَلَّىٰ و ل ي B003; 88:23 تَوَلَّىٰ و ل ي B007; 88:23 وَكَفَرَ ك ف ر B003; 88:24 ٱللَّهُ ء ل ه B001; 88:26 حِسَابَهُم ح س ب B001

## Gelmek, sırt dönmek, dönüp varmak

Sure bir gelişle açılır. Gelmek, kolayca varmaktır: {ar:الإتيان مجيء بسهولة, tr:el-ityânu mecîun bi-suhûle, gloss:ityân kolayca gelmektir, source:"ء ت ي,B001"}. Bu geliş iyiliği de kötülüğü de getirebilir: {ar:الإتيان يقال في الخير وفي الشر, tr:el-ityânu yukâlü fi'l-hayri ve fi'ş-şerr, gloss:ityân hem hayır hem şer için söylenir, source:"ء ت ي,B011"}. İlk ayette iki geliş vardır. Haber gelir, haberin anlattığı şey de bir gelip örtmedir. Örtme fiili gelmek fiiliyle açıklanır: {ar:غشيت موضع كذا أتيته, tr:ğaşîtü mevdia kezâ eteytüh, gloss:falan yere ğaşîtü yani oraya geldim, source:"غ ش و,B003"}; {ar:غشيه غشيانا أي جاءه, tr:ğaşiyehû ğaşeyânen ey câeh, gloss:ona ğaşiye yani ona geldi, source:"غ ش و,B003"}. Böylece ilk ayetteki iki kelime birbirini açıklar. Kur'an iki gelişi aynı ayette yan yana koyar: {ar:أَوْ تَأْتِيَهُمُ ٱلسَّاعَةُ بَغْتَةًۭ وَهُمْ لَا يَشْعُرُونَ, tr:ev te'tiyehumu's-sââtu bağteten ve hum lâ yeş'urûn, gloss:ya da o saat onlar farkında değilken ansızın gelir, source:12:107}.

İkinci ayetteki yüz yönelimdir: {ar:الوجهة كل موضع استقبلته, tr:el-vichetü küllü mevdıin istakbeltehû, gloss:vichet yöneldiğin her yerdir, source:"و ج ه,B002"}. Yirmi üçüncü ayette ise yüz çevrilir ve sırt gösterilir. Fiil "-den" ile kullanıldığında yakınlığı terk edip yüz çevirmeyi anlatır: {ar:إذا عدي بعن اقتضى معنى الإعراض وترك قربه, tr:izâ uddiye bi-an iktedâ ma'na'l-i'râdi ve terke kurbih, gloss:-den ile kullanılınca yüz çevirmeyi ve yakınlığını bırakmayı gerektirir, source:"و ل ي,B007"}. Aynı fiilin bir yüzü yönelmektir: {ar:التولية تكون إقبالا, tr:et-tevliyetü tekûnu ikbâlen, gloss:tevliye yönelmek de olur, source:"و ل ي,B006"}. Kur'an yüz çevirmeyi azaba bağlar. Musa ve Harun'a Firavun'a şunu söylemeleri emredilir: {ar:إِنَّا قَدْ أُوحِىَ إِلَيْنَآ أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ, tr:innâ kad ûhiye ileynâ enne'l-azâbe alâ men kezzebe ve tevellâ, gloss:yalanlayan ve yüz çeviren için azap olduğu bize vahyedildi, source:20:48}.

Yirmi beşinci ayet, sırt dönenin bile nereye vardığını söyler. Dönüş, insanın yerleştiği yere geri gelmesidir: {ar:آب الرجل يؤوب إيابا إذا رجع إلى مستقره والمآب المرجع, tr:âbe'r-raculu yeûbu iyâben izâ raca'a ilâ mustakarrih ve'l-meâbu'l-merci', gloss:adam yerleştiği yere döndüğünde âbe denir; meâb dönülen yerdir, source:"ء و ب,B001"}; {ar:آب الغائب يؤوب أوبا أي رجع والمآب المرجع, tr:âbe'l-ğâibu yeûbu evben ey raca' ve'l-meâbu'l-merci', gloss:gaip olan döndü; meâb dönülen yerdir, source:"ء و ب,B001"}. Yüz çeviren adım adım yine "Bize" yürür. Yüz çevirmek gidilen yeri değiştirmez. Kökün bir kolu aynı dönüşün gönüllü yapılabileceğini gösterir: {ar:الأواب كالتواب وهو الراجع إلى الله تعالى, tr:el-evvâbu ke't-tevvâbi ve huve'r-râciu ilallâhi teâlâ, gloss:evvâb tövbekâr gibidir; Allah'a dönendir, source:"ء و ب,B002"}. Kur'an'da "en büyük azap" sözünün geçtiği öteki ayet de dönüşe bakar: {ar:لَعَلَّهُمْ يَرْجِعُونَ, tr:leallehum yerciûn, gloss:belki dönerler, source:32:21}. Yakın azap, dönüşün henüz insanın elinde olduğu bir zamana denk gelir.

Kur'an dönüşü başka yerlerde de anar. İnsanın kendini yeterli görüp azgınlaştığı söylendikten {source:96:7} sonra şöyle denir: {ar:إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ, tr:inne ilâ rabbike'r-ruc'â, gloss:dönüş şüphesiz Rabbinedir, source:96:8}. Başka bir ayette de {ar:وَإِلَيْنَا ٱلْمَصِيرُ, tr:ve ileyne'l-masîr, gloss:varış Bizedir, source:50:43} denir. Allah, Peygamber'e inkârcılar için üzülmemesini söylerken surenin son ayetlerinin sırasını izler: {ar:وَمَن كَفَرَ فَلَا يَحْزُنكَ كُفْرُهُۥٓ ۚ إِلَيْنَا مَرْجِعُهُمْ فَنُنَبِّئُهُم بِمَا عَمِلُوٓا۟, tr:ve men kefera fe-lâ yahzunke küfruhû ileynâ merciuhum fe-nunebbiuhum bimâ amilû, gloss:kim inkâr ederse inkârı seni üzmesin; dönüşleri Bizedir, yaptıklarını onlara haber veririz, source:31:23}; {ar:نُمَتِّعُهُمْ قَلِيلًۭا ثُمَّ نَضْطَرُّهُمْ إِلَىٰ عَذَابٍ غَلِيظٍۢ, tr:numettiuhum kalîlen summe nadtarruhum ilâ azâbin ğalîz, gloss:onları biraz yararlandırırız, sonra ağır bir azaba sürükleriz, source:31:24}. Burada inkâr, Bize dönüş, yapılan işin haberi ve azap sırayla gelir. Dönülen yer iki türlüdür: {ar:لِّلطَّٰغِينَ مَـَٔابًۭا, tr:li't-tâğîne meâbâ, gloss:azgınlar için bir dönüş yeri, source:78:22} ve {ar:فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ مَـَٔابًا, tr:fe-men şâe'ttehaze ilâ rabbihî meâbâ, gloss:dileyen Rabbine bir dönüş yolu tutar, source:78:39}. Gönüllü dönüş, dokuzuncu ayetin hoşnutluğuyla yapılır: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:ırci'î ilâ rabbiki râdiyeten mardiyye, gloss:Rabbine hoşnut ve hoşnut edilmiş olarak dön, source:89:28}.

Kaynaklar: 88:1 أَتَىٰكَ ء ت ي B001; 88:1 أَتَىٰكَ ء ت ي B011; 88:1 ٱلْغَٰشِيَةِ غ ش و B003; 88:2 وُجُوهٌ و ج ه B002; 88:23 تَوَلَّىٰ و ل ي B006; 88:23 تَوَلَّىٰ و ل ي B007; 88:25 إِيَابَهُمْ ء و ب B001; 88:25 إِيَابَهُمْ ء و ب B002; 88:26 حِسَابَهُم ح س ب B001

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

