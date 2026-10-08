Focus: 88:11. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_11/D.r13/context.md =====
# 88:11 — focus

لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ

Anchor translation (canonical reading, reference only):

Orada boş söz duymazsın.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | لَّا | لَا |  | NEG |
| 2 | تَسْمَعُ | سَمِعَ | س م ع | V |
| 3 | فِيهَا | فِى |  | P;PRON |
| 4 | لَٰغِيَةً | لَٰغِيَة | ل غ و | N |


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
- 88:11 ◀ focus لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ
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
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_11/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س م ع (root_000741) — identity root of تَسْمَعُ (w2)

- **B001** duymak ve dikkatle dinlemek — sesi kulakla algılamak · işitme gücü veya duyma eylemi · duyma eylemi veya duyulan şey · dikkatle dinlemek · duymaya çalışarak kulak vermek · beni dinle ve söylediklerime kulak ver · dinle · söylenenleri çokça dinleyen kimse · işiten kimse · kendi kulağımla duydum; görmeyle ilgili aktarılmış yorum kaynakta reddedilir
  إيناس الشيء بالأذن (maqayis)؛ سمعت الشيء سمعا (maqayis;sihah;mufradat)؛ الاستماع الإصغاء (sihah;mufradat)؛ سماع أي اسمع (maqayis;sihah)؛ السمع سمع الإنسان وغيره (tahdhib)
- **B002** kulak ve kulak açıklığı — kulak veya işitme yeri · kulak veya kulak açıklığı · kulak açıklığı veya işitme yeri · kulak · iki kulak veya iki işitme yeri
  السمع الأذن وهي المسمعة (ayn;tahdhib)؛ المسمعة خرقها (ayn)؛ المسمع خرق الأذن (tahdhib;mufradat)؛ السامعة الأذن (sihah)؛ المسمعان الأذنان (sihah;tahdhib)
- **B003** anlayıp kabul etmek ve uymak — sözü anlayıp kabul etmek ve ona uymak
  تارة عن الفهم وتارة عن الطاعة (mufradat)؛ فهمنا وارتسمنا (mufradat)؛ فهمنا وهم لا يفهمون (mufradat)؛ لم يستعملوا هذه الحواس استعمالا يجدي عليهم (tahdhib)
- **B004** duyurmak veya kavratmak — duymasını sağlamak veya kavratmak · başkasına duyuran kimse
  سمعه الصوت وأسمعه (sihah)؛ السميع المسمع (sihah;tahdhib)؛ أسمعهم أي أفهمهم (mufradat)؛ فعلت ذلك تسمعتك وتسمعة لك أي لتسمعه (tahdhib)
- **B005** adı yayılıp tanınmak — yaymak, tanınır kılmak veya adını öne çıkarmak · güzel ün ve iyi ad · duyulup yayılan ve konuşulan şey · insanlar duysun diye yapılan gösteriş · insanların haberi birbirinden duyup yayması
  السمع الذكر الجميل (maqayis;sihah)؛ السماع ما سمعت به فشاع (ayn;tahdhib)؛ سمعت بالشيء إذا أشعته (maqayis)؛ فعله رياء وسمعة (ayn;sihah)؛ سمع به أي شهره (sihah)؛ سمعت بفلان في الناس إذا نوهت بذكره (tahdhib)
- **B006** kötü söz işittirip sövmek [kalıp] — sövmek ve hoşlanmayacağı sözleri yüzüne söylemek · sövmek veya duymaz olmasını dilemek
  أسمعه الحديث وسمعه أي شتمه (sihah)؛ أسمعت فلانا إذا سببته (mufradat)؛ أسمعك الله أي جعلك الله أصم (mufradat)؛ سمعت بالرجل تسميعا إذا نددت به وشهرته وفضحته (tahdhib)؛ أسمعته القبيح وشتمته (tahdhib)
- **B007** kulağa hoş gelen ezgili ses — şarkı veya kulağa hoş gelen güzel ses · kadın şarkıcı
  المسمعة المغنية (maqayis;sihah)؛ السماع الغناء (ayn)؛ السماع اسم ما استلذت الأذن من صوت حسن (tahdhib)؛ المسمعة القينة المغنية (ayn)
- **B008** taşıma kabının sap veya denge parçası — kova veya su kabının yükü dengeleyen sapı ya da halkası · büyük su kabının iki yanı veya yük sepetinin iki taşıyıcı tahtası · kovaya sap takmak veya saplarını yükü hafifletecek biçimde bağlamak
  المسمع كالأذن للغرب (maqayis)؛ مسمع الدلو والغرب عروة في وسطه (ayn;sihah)؛ المسمع من المزادة ما جاوز خرت العروة إلى الظرف (ayn)؛ المسمعان جانبا الغرب (tahdhib)؛ المسمع عروة في داخل الدلو (tahdhib)؛ حلقة مسمع الغرب (mufradat)
- **B009** ayak bağı veya hareket kısıtlayıcı bağ — ayak bağı veya bağlama aracı · iki ayak bağı ve bir boyun bağıyla bağlanmış
  من أسماء القيد المسمع؛ ولي مسمعان وزمارة؛ مسمعا مزمرا أي مقيدا مسوجرا
- **B010** kurt ile sırtlan arasında sayılan yırtıcı — kurt ile sırtlan arasında sayılan yırtıcı veya onların yavrusu · o yırtıcıdan bile daha keskin işiten
  السمع ولد الذئب من الضبع (maqayis;tahdhib)؛ السمع سبع بين الذئب والضبع (ayn)؛ السمع سبع مركب (sihah)؛ أسمع من السمع الأزل (sihah)
- **B011** duyulsun ama bana ulaşmasın — duyulsun ama bana ulaşmasın
  اللهم سمعا لا بلغا (sihah)؛ سمع لا بلغ معناه يسمع ولا يبلغ (tahdhib)؛ أسمع بالدواهي ولا تبلغني (tahdhib)
- **B012** küçük başlı, ince uzun veya çevik atılgan kimse — küçük başlı, ince uzun, çevik atılgan veya kötü
  السمعمع الصغير الرأس (sihah;tahdhib)؛ السمعمع من الرجال المنكمش الماضي (tahdhib)؛ الشيطان الخبيث يقال له سمعمع (tahdhib)؛ السمعمع من الرجال الدقيق الطويل (tahdhib)؛ امرأة سمعمعة (tahdhib)
- **B013** bakıp dinlediği hâlde göremeyince tahmin eden kadın — dinleyip baktığı hâlde bir şey göremeyince tahmin eden kadın
  امرأة سمعنة نظرنة (sihah;tahdhib)؛ إذا تسمعت أو تبصرت فلم تر شيئا تظنته تظنيا (sihah)؛ إذا سمعت أو تبصرت فلم تر شيئا تظنت تظنيا (tahdhib)
- **B014** kimsenin görüp duymadığı boş arazide [kalıp] — kimsenin görüp duymadığı boş arazide
  تخرج بين سمع الأرض وبصرها؛ ليس معها أحد يسمع كلامها أو يبصرها إلا الأرض القفر؛ لقيته يمشي بين سمع الأرض وبصرها أي بأرض خلاء ما بها أحد
- **B015** öküz koşumundaki iki uzun çubuk — toprak sürmek için iki öküzün bağlandığı düzenekteki iki uzun çubuk
  السميعان من أدوات الحراثين؛ عودان طويلان في المقرن الذي يقرن به الثوران لحراثة الأرض
- **B016** beyin — beyin
  أم السمع وأم السميع الدماغ؛ نقبن الحرة السوداء عنهم كنقب الرأس عن أم السميع

## ل غ و (root_001361) — identity root of لَٰغِيَةً (w4)

- **B001** dikkate alınmayan veya geçersiz kılınan şey — dikkate alınmayan, hesaba katılmayan şey · içten bağlanılmamış, bağlayıcı olmayan yemin · kan bedelinin hesabına katılmayan deve yavruları · bir şeyi geçersiz kılmak veya bir sözü boş ve gereksiz saymak · onu sayıdan çıkarmak ve hesaba katmamak · içten bağlanmadan yemin etmek · ciddi ve amaçlı olmayan koşu
  اللغو ما لا يعتد به من أولاد الإبل في الدية (maqayis;sihah;mufradat)؛ لغو الأيمان ما لم تعقدوه بقلوبكم وما لا عقد عليه (maqayis;sihah;tahdhib;mufradat)؛ ألغيت هذه الكلمة أي رأيتها باطلا وفضلا وحشوا وما يلغى من الحساب (ayn;tahdhib)؛ ألغيت الشيء: أبطلته وألغاه من العدد: ألقاه منه (sihah;tahdhib)؛ فرسك لملاغي الجري إذا كان جريه غير جري جد (tahdhib)
- **B002** batıl veya çirkin söz — batıl veya çirkin söz · çirkin ya da açık saçık söz · onu batıl veya çirkin söze yöneltmek · haftalık toplu ibadet konuşması sırasında söz söylemek
  لغا يلغو لغوا يعني اختلاط الكلام في الباطل (ayn;tahdhib)؛ لغا يلغو لغوا أي قال باطلا (sihah)؛ كل كلام قبيح لغوا (mufradat)؛ لاغية كلمة قبيحة أو فاحشة (ayn;tahdhib)؛ قال قتادة باطلا ومأثما وقال مجاهد شتما (tahdhib)؛ استلغوني أرادوني على اللغو (tahdhib)
- **B003** ses ve gürültü — konuşma sesini yükselterek şaşırtmak · ses ve gürültü · köpek havlaması · kuş sesleri
  والغوا فيه يعني رفع الصوت بالكلام ليغلطوا المسلمين (ayn)؛ اللغا: الصوت مثل الوغا ونباح الكلب لغو أيضا (sihah)؛ لغوى الطير أصواتها (tahdhib)؛ اللغا صوت العصافير ونحوها من الطيور (mufradat)
- **B004** bir şeye düşkün olup onunla sürekli meşgul olma — bir şeye düşkün olmak ve onunla sürekli meşgul olmak · bir içeceği çok tüketmek · bir topluluğun dili veya aynı anlamı farklı sözlerle anlatma biçimi · kendilerine sormadan konuşmalarını dinleyip dil kullanımlarını öğrenmek
  لغى بالأمر إذا لهج به ويقال إن اشتقاق اللغة منه (maqayis)؛ اللغة واللغات اختلاف الكلام في معنى واحد (ayn;tahdhib)؛ لغي به أي لهج به ولغي بالشراب أكثر منه واللغة أصلها لغى أو لغو (sihah)؛ لغي فلان بفلان إذا أولع به ولغي فلان بالماء إذا أكثر منه واستلغهم اسمع من لغاتهم (tahdhib)؛ لغي بكذا أي لهج به ومنه قيل للكلام الذي يلهج به فرقة فرقة لغة (mufradat)
- **B005** doğru olandan sapmak — doğru olandan sapmak
  لغا فلان عن الصواب أي مال عنه (tahdhib)
- **B006** umduğunu bulamama veya birini başarısızlığa uğratma — haftalık toplu ibadet konuşması sırasında konuşup umduğunu bulamamak · onu umduğundan yoksun bırakıp başarısızlığa uğratmak
  من تكلم يوم الجمعة والإمام يخطب فقد لغا أي خاب؛ وألغيته أي خيبته (tahdhib)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:11, and ## Buluşmalar) =====
## Kulağa gelen: haber, susan sesler, işitilmeyen söz

Sure göze değil kulağa seslenerek başlar. "Sana geldi mi" diye sorulan şey bir haberdir. Haber de kulaktan ulaşan sözdür: {ar:كل كلام يبلغ الإنسان من جهة السمع أو الوحي يقال له حديث, tr:küllü kelâmin yeblüğu'l-insâne min cihetí's-sem'i evi'l-vahyi yukâlü lehû hadîs, gloss:insana işitme ya da vahiy yoluyla ulaşan her söze hadîs denir, source:"ح د ث,B003"}. Kur'an aynı açılışı başka yerlerde de kullanır ve ardından her seferinde bir kıssa gelir: {ar:وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ, tr:ve hel etâke hadîsü Mûsâ, gloss:Musa'nın haberi sana geldi mi, source:20:9}; {ar:هَلْ أَتَىٰكَ حَدِيثُ ضَيْفِ إِبْرَٰهِيمَ ٱلْمُكْرَمِينَ, tr:hel etâke hadîsü dayfi İbrâhîme'l-mükramîn, gloss:İbrahim'in ağırlanan misafirlerinin haberi sana geldi mi, source:51:24}; {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْجُنُودِ, tr:hel etâke hadîsü'l-cunûd, gloss:orduların haberi sana geldi mi, source:85:17}. Bunlarda anlatılan şey geçmişte kalmıştır. Bu surede ise henüz gelmemiş bir gün, gelmiş bir haber gibi anlatılır. Kelimenin bir kolu, haberlerde ibret olarak anlatılan insanlara da ad verir: {ar:فجعلناهم أحاديث أي أخبارا يتمثل بهم, tr:fe-cealnâhum ehâdîse ey ahbâran yütemesselü bihim, gloss:onları örnek gösterilen haberler yaptık, source:"ح د ث,B004"}. Bu anlam surenin haberinin yanında duyulur: haberi dinleyen, kendisi de bir haber olabilir.

İkinci ayetteki eğiklik sesleri de kapsar: {ar:خشعت الأصوات أي سكنت, tr:haşaati'l-asvâtu ey sekenet, gloss:sesler kısıldı yani dindi, source:"خ ش ع,B001"}. Kur'an bu susuşu Sur'a üfürülen günün sahnesinde gösterir. Herkes çağırıcının ardından sapmadan yürür: {ar:وَخَشَعَتِ ٱلْأَصْوَاتُ لِلرَّحْمَٰنِ فَلَا تَسْمَعُ إِلَّا هَمْسًۭا, tr:ve haşaati'l-asvâtu li'r-Rahmâni fe-lâ tesmeu illâ hemsâ, gloss:sesler Rahman'a karşı kısılır; bir fısıltıdan başkasını işitmezsin, source:20:108}. Bu ayetteki "işitmezsin" sözü, on birinci ayetteki ile harfi harfine aynıdır: {ar:لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ, tr:lâ tesmeu fîhâ lâğiye, gloss:orada boş bir söz işitmezsin, source:88:11}. Böylece iki ayrı sessizlik ortaya çıkar. Birinde sesler korkudan kısılır. Ötekinde kulak çirkin sözden korunur. İşitmek, sesi kulakla yakalamaktır: {ar:إيناس الشيء بالأذن, tr:înâsu'ş-şey'i bi'l-üzün, gloss:bir şeyi kulakla fark etmek, source:"س م ع,B001"}. Bu kelime anlamayı ve söz dinlemeyi de içerir: {ar:تارة عن الفهم وتارة عن الطاعة, tr:târaten ani'l-fehmi ve târaten ani't-tâa, gloss:kimi zaman anlamayı kimi zaman itaati anlatır, source:"س م ع,B003"}. Bahçede işitilmeyen kelime de tek tek tanımlanır: {ar:لاغية كلمة قبيحة أو فاحشة, tr:lâğiyetun kelimetun kabîhatun ev fâhişe, gloss:çirkin ya da hayasız söz, source:"ل غ و,B002"}. Kökün bir kolu, anlamsız gürültüyü ve köpek havlamasını da anlatır: {ar:اللغا: الصوت مثل الوغا ونباح الكلب لغو أيضا, tr:el-leğâ es-savtu misle'l-vağâ ve nubâhu'l-kelbi lağvun eydan, gloss:gürültü; köpek havlaması da lağvdır, source:"ل غ و,B003"}. Kur'an bahçenin bu sessizliğini sık sık anlatır ve yerine konan sözü de söyler: {ar:لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا, tr:lâ yesmeûne fîhâ lağven illâ selâmâ, gloss:orada boş söz değil yalnız selam işitirler, source:19:62}; {ar:لَا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا تَأْثِيمًا, tr:lâ yesmeûne fîhâ lağven ve lâ te'sîmâ, gloss:orada ne boş söz işitirler ne günaha sokan söz, source:56:25}; {ar:إِلَّا قِيلًۭا سَلَٰمًۭا سَلَٰمًۭا, tr:illâ kîlen selâmen selâmâ, gloss:yalnızca selam selam diye bir söz, source:56:26}; {ar:لَّا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا كِذَّٰبًۭا, tr:lâ yesmeûne fîhâ lağven ve lâ kizzâbâ, gloss:orada ne boş söz işitirler ne yalan, source:78:35}.

Yirmi birinci ayette haber çizgisi döner: {ar:فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ, tr:fe-zekkir innemâ ente müzekkir, gloss:hatırlat; sen yalnızca hatırlatansın, source:88:21}. Hatırlatmak önce bir şeyi dile getirmektir: {ar:الذكر جري الشيء على لسانك, tr:ez-zikru ceryü'ş-şey'i alâ lisânik, gloss:zikir bir şeyin dilinden akmasıdır, source:"ذ ك ر,B004"}. Dinleyende ise unutmanın karşıtını uyandırmaktır: {ar:ذكرت الشيء خلاف نسيته, tr:zekertü'ş-şey'e hılâfe nesîtüh, gloss:hatırladım unuttum'un zıddıdır, source:"ذ ك ر,B003"}. Sure "sana geldi mi" diye başlamış, "sen hatırlatansın" diye bu çizgiyi kapatır. Habere ilk muhatap olan kişi, aynı haberi başkalarının kulağına ulaştıran olur.

Kaynaklar: 88:1 أَتَىٰكَ ء ت ي B001; 88:1 حَدِيثُ ح د ث B003; 88:1 حَدِيثُ ح د ث B004; 88:2 خَٰشِعَةٌ خ ش ع B001; 88:11 تَسْمَعُ س م ع B001; 88:11 تَسْمَعُ س م ع B003; 88:11 لَٰغِيَةً ل غ و B002; 88:11 لَٰغِيَةً ل غ و B003; 88:21 فَذَكِّرْ ذ ك ر B004; 88:21 مُذَكِّرٌ ذ ك ر B003

## Emek, ücret ve sayım

Üçüncü ayetteki ilk sıfat amaçlı yapılan iştir: {ar:كل فعل يكون من الحيوان بقصد, tr:küllü fi'lin yekûnu mine'l-hayevâni bi-kasd, gloss:canlıdan kasıtla çıkan her iş, source:"ع م ل,B001"}. Böyle bir iş karşılığında ücret beklenir: {ar:العمالة أجر ما عمل, tr:el-umâletü ecru mâ amel, gloss:umâle yapılan işin ücretidir, source:"ع م ل,B004"}. İkinci sıfatın kökü ise hem yorgunluğu hem de pay almayı anlatır: {ar:النصيب الحظ من الشيء, tr:en-nasîbu'l-hazzu mine'ş-şey', gloss:nasip bir şeyden düşen paydır, source:"ن ص ب,B005"}. Ayetteki anlam yorgunluktur. Yanında ise payın kendisi duyulur. Bu yüz çalışmış ve yorulmuştur, ama eline geçen tek şey yorgunluktur. Yedinci ayet bu kazancın neye yaradığını söyler: {ar:الغناء بالفتح الكفاية ولا يغني أي لا يكفي, tr:el-ğanâu bi'l-feth el-kifâye ve lâ yuğnî ey lâ yekfî, gloss:ğanâ yeterliliktir; lâ yuğnî yetmez demektir, source:"غ ن ي,B002"}.

Dokuzuncu ayet karşı tarafı tek bir kelimeyle kurar: {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdiye, gloss:çabasından hoşnut, source:88:9}. Çaba, kazanç getiren iştir: {ar:كل عمل من خير أو شر فهو السعي؛ السعي العمل أي الكسب, tr:küllü amelin min hayrin ev şerrin fe-huve's-sa'y; es-sa'yu'l-amel ey el-kesb, gloss:iyi ya da kötü her iş sa'ydir; sa'y kazançtır, source:"س ع ي,B002"}. Hoşnutluk iki yönlüdür: {ar:ورضا العبد عن الله ورضا الله عن العبد, tr:ve rıda'l-abdi anillâhi ve rıdallâhi ani'l-abd, gloss:kulun Allah'tan ve Allah'ın kuldan razı olması, source:"ر ض و,B001"}. Bu yüz dönüp kendi emeğine bakar ve gördüğünden memnun kalır. Öteki yüzün emeği ise üstünde yorgunluk olarak kalmıştır.

On birinci ayetteki kelimenin bir başka kolu, hesaba geçmeyen şeyi anlatır: {ar:ألغيت هذه الكلمة أي رأيتها باطلا وفضلا وحشوا وما يلغى من الحساب, tr:elğaytü hâzihi'l-kelimete ey raeytühâ bâtılen ve fadlen ve haşven ve mâ yulğâ mine'l-hısâb, gloss:bu sözü boş ve fazlalık saydım; hesaptan düşülen şey, source:"ل غ و,B001"}. Yirmi altıncı ayet de bir sayımla kapanır: {ar:الحساب عدك الأشياء, tr:el-hısâbu addüke'l-eşyâ', gloss:hesap şeyleri tek tek saymandır, source:"ح س ب,B001"}. Bahçede boş söz işitilmez. Hesapta da boş olan sayılmaz. Sayım ise surenin sonunda yalnızca "Bize" aittir.

Kur'an emeğin hesabını açıkça anlatır. Musa'nın ve İbrahim'in sayfalarında bulunduğu bildirilen sözler arasında şunlar vardır: {ar:وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ, tr:ve en leyse li'l-insâni illâ mâ seâ, gloss:insan için çabaladığından başkası yoktur, source:53:39}; {ar:وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ, tr:ve enne sa'yehû sevfe yurâ, gloss:çabası görülecektir, source:53:40}; {ar:ثُمَّ يُجْزَىٰهُ ٱلْجَزَآءَ ٱلْأَوْفَىٰ, tr:summe yuczâhu'l-cezâe'l-evfâ, gloss:sonra karşılığı tam olarak verilecektir, source:53:41}. Ahireti isteyip onun için çabalayanların çabası {ar:فَأُو۟لَٰٓئِكَ كَانَ سَعْيُهُم مَّشْكُورًۭا, tr:fe-ülâike kâne sa'yuhum meşkûrâ, gloss:işte onların çabası karşılık görür, source:17:19} diye anılır. Bahçe halkına, gümüş kaplarla ve kadehlerle ağırlandıktan sonra şöyle denir: {ar:وَكَانَ سَعْيُكُم مَّشْكُورًا, tr:ve kâne sa'yukum meşkûrâ, gloss:çabanız karşılık gördü, source:76:22}. Büyük felaket geldiğinde çaba yeniden hatırlanır: {ar:يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ, tr:yevme yetezekkeru'l-insânu mâ seâ, gloss:insanın çabaladığı şeyi hatırlayacağı gün, source:79:35}. Boşa giden emek için ise şöyle denir: {ar:فَجَعَلْنَٰهُ هَبَآءًۭ مَّنثُورًا, tr:fe-cealnâhu hebâen mensûrâ, gloss:onu dağılmış toza çevirdik, source:25:23}. Başka bir yerde de {ar:ٱلَّذِينَ ضَلَّ سَعْيُهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَهُمْ يَحْسَبُونَ أَنَّهُمْ يُحْسِنُونَ صُنْعًا, tr:ellezîne dalle sa'yuhum fi'l-hayâti'd-dünyâ ve hum yahsebûne ennehum yuhsinûne sun'â, gloss:dünya hayatında çabaları boşa gidip de güzel iş yaptıklarını sananlar, source:18:104} diye anlatılırlar. Buradaki "sanmak" fiili hesap ile aynı köktendir. Bu insanlar yanlış saymıştır.

Bu sahnelerin en yakını, kitabı sağından verilen kişinin sevincidir: {ar:إِنِّى ظَنَنتُ أَنِّى مُلَٰقٍ حِسَابِيَهْ, tr:innî zanentu ennî mulâkin hısâbiyeh, gloss:hesabıma kavuşacağımı zaten biliyordum, source:69:20}. Ardından surenin dokuzuncu ve onuncu ayetlerindeki sözler gelir: {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:artık o hoşnut bir yaşayıştadır, source:69:21}; {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüce bir bahçede, source:69:22}. Kitabı solundan verilen ise {ar:وَلَمْ أَدْرِ مَا حِسَابِيَهْ, tr:ve lem edri mâ hısâbiyeh, gloss:keşke hesabımın ne olduğunu bilmeseydim, source:69:26} der. Teraziler tartıldığında ağır gelen de {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:o hoşnut bir yaşayıştadır, source:101:7} diye anılır. Hesap kökü yetecek kadar vermeyi de anlatır: {ar:عطاء حسابا أي كافيا, tr:atâen hısâben ey kâfiyen, gloss:yeterli bir bağış, source:"ح س ب,B003"}. Kur'an bunu takva sahiplerinin karşılığı için söyler: {ar:جَزَآءًۭ مِّن رَّبِّكَ عَطَآءً حِسَابًۭا, tr:cezâen min rabbike atâen hısâbâ, gloss:Rabbinden bir karşılık; yeterli bir bağış, source:78:36}. Birinin emeği "yetmez" diye biter. Ötekinin karşılığı "yeter" diye verilir.

Kaynaklar: 88:3 عَامِلَةٌ ع م ل B001; 88:3 عَامِلَةٌ ع م ل B004; 88:3 نَّاصِبَةٌ ن ص ب B004; 88:3 نَّاصِبَةٌ ن ص ب B005; 88:7 يُغْنِى غ ن ي B002; 88:9 لِّسَعْيِهَا س ع ي B002; 88:9 رَاضِيَةٌ ر ض و B001; 88:11 لَٰغِيَةً ل غ و B001; 88:26 حِسَابَهُم ح س ب B001; 88:26 حِسَابَهُم ح س ب B003

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

