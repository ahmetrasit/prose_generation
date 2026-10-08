Focus: 89:19. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_19/D.r13/context.md =====
# 89:19 — focus

وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا

Anchor translation (canonical reading, reference only):

Ve mirası tamamen yiyip tüketiyorsunuz.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَتَأْكُلُونَ | أَكَلَ | ء ك ل | CONJ;V;PRON |
| 2 | ٱلتُّرَاثَ | تُّرَاث | و ر ث | DET;N |
| 3 | أَكْلًا | أَكْل | ء ك ل | N |
| 4 | لَّمًّا | لَّمّ | ل م م | ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 89 — full text (context; no pericope)

- 89:1 وَٱلْفَجْرِ
- 89:2 وَلَيَالٍ عَشْرٍۢ
- 89:3 وَٱلشَّفْعِ وَٱلْوَتْرِ
- 89:4 وَٱلَّيْلِ إِذَا يَسْرِ
- 89:5 هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ
- 89:6 أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ
- 89:7 إِرَمَ ذَاتِ ٱلْعِمَادِ
- 89:8 ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ
- 89:9 وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ
- 89:10 وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ
- 89:11 ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ
- 89:12 فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ
- 89:13 فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ
- 89:14 إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
- 89:15 فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ
- 89:16 وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
- 89:17 كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ
- 89:18 وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 89:19 ◀ focus وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا
- 89:20 وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
- 89:21 كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا
- 89:22 وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- 89:23 وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- 89:24 يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
- 89:25 فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- 89:26 وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ
- 89:27 يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- 89:28 ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- 89:29 فَٱدْخُلِى فِى عِبَٰدِى
- 89:30 وَٱدْخُلِى جَنَّتِى


===== _commentary/v16/work/89_19/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء ك ل (root_000043) — identity root of وَتَأْكُلُونَ (w1)

- **B001** yeme, yiyecek ve yeme rolleri — yemek yemek · yiyecek · bir öğünlük yeme veya tek lokma · çok yiyen, obur · birlikte yemek yiyen kişi · başkasını doyuran kişi · yenilen şey, yiyecek · yenmek üzere hazırlanmış yiyecek
  الأكل معروف؛ أكلت الطعام أكلا ومأكلا؛ الأكل تناول المطعم؛ الأكلة المرة واللقمة؛ رجل أكول كثير الأكل؛ أكيلك الذي يؤاكلك؛ المؤكل المطعم
- **B002** ağaç ve ekin ürünü — ağacın meyvesi veya verimi
  أكل الشجرة ثمرها؛ الأكل ثمر النخل والشجر؛ أكل بستانك دائم وأكله ثمره؛ والأكل لما يؤكل قال تعالى أكلها دائم
- **B003** verilen pay ve geçimlik — dünya payı ve geniş geçimliği olan · yöneticilerin verdiği tahsisatlar · kişiye ayrılmış, hesabı sorulmayan pay
  الأكل حظ الرجل وما يعطاه من الدنيا؛ المأكلة ما جعل للإنسان لا يحاسب عليه؛ فلان ذو أكل إذا كان ذا حظ من الدنيا ورزق واسع؛ الأكل الطعمة؛ يعبر به عن النصيب
- **B004** malı harcama veya ele geçirme [kalıp] — malı harcamak veya tüketerek elden çıkarmak · insanların mallarını alıp onları sömürmek
  يستأكل قوما أي يأكل أموالهم؛ فلان يستأكل الضعفاء أي يأخذ أموالهم؛ يعبر بالأكل عن إنفاق المال؛ أكل المال بالباطل صرفه إلى ما ينافيه الحق
- **B005** ateşin tüketmesi, beslenmesi ve harlanması — ateş odunu yakıp tüketti · ateşi odunla besledi · ateş iyice harlandı · öfkesinden alevlendi · kılıç keskinliğinden parladı
  أكلت النار الحطب وآكلتها؛ ائتكلت النار إذا اشتد التهابها؛ الرجل إذا اشتد غضبه يأتكل؛ تأكل السيف أي توهج من الحدة؛ وعلى طريق التشبيه قيل أكلت النار الحطب
- **B006** aşınma, bozulma ve kaşıntı — beden veya baş kaşıntısı · dişlerde aşınma veya çürüme · deride işlenince ortaya çıkan ince kusurlu yer · gebe deve, yavrusunun çıkan tüyünden kaşınıp rahatsız oldu · aşınıp bozulmak
  الأكال الحكاك؛ الأكل في الأديم مكان رقيق؛ بأسنانه أكل؛ والأكال أن يتأكل عود أو شيء؛ في جسدي إكلة من الأكال؛ تأكل كذا فسد؛ أصابه إكال في رأسه وفي أسنانه
- **B007** av olmuş veya yenmek için ayrılmış hayvan — yırtıcının yiyip bıraktığı av · kurdun yediği koyun veya başka av · yenmek için ayrılıp beslenen koyun · ürünü yenmek üzere ayrılmış hurma ağaçları
  أكيل الذئب الشاة وغيرها؛ أكيلة الأسد فريسته؛ الأكولة من الشاء التي ترعى للأكل لا للنسل والبيع؛ الأكولة الشاة التي تعزل للأكل وتسمن؛ أكيلة السبع؛ الأكولة من الغنم ما يؤكل
- **B008** arkadan çekiştirip saygınlığı zedeleme [kalıp] — birinin saygınlığını arkadan çekiştirerek zedelemek · insanları sürekli arkalarından çekiştiren
  فلان ذو أكلة في الناس إذا كان يغتابهم؛ ذو أكلة وإكلة إذا كان يغتاب الناس؛ تأكل لحومنا وتغتابنا؛ أكل فلان فلانا اغتابه وكذا أكل لحمه
- **B009** söz taşıyarak arayı bozma [kalıp] — aralarında söz taşıyıp onları birbirine düşürmek · ara bozucu söz taşıyıcı
  آكلت بين القوم أفسدت؛ المؤكل النمام؛ الإيكال بين الناس السعي بينهم بالنمائم؛ آكلت بين القوم أي حرشت وأفسدت
- **B010** biçime bağlı adlandırmalar [kalıp] — bana yapmadığım veya almadığım şeyi yükledin · onu senin erişimine bıraktım
  أكلتني ما لم آكل أي ادعيته علي؛ آكلتني أيضا أي ادعيته علي؛ آكلتك فلانا إذا أمكنته منه؛ أليس قبيحا أن تؤكلني ما لم آكل
- **B011** bir başla doyacak kadar az topluluk [kalıp] — tek bir hayvan başının doyuracağı kadar az topluluk
  ما هم إلا أكلة رأس؛ هم أكلة رأس أي هم قليل يشبعهم رأس واحد؛ عبارة عن ناس من قلتهم يشبعهم رأس
- **B012** biçime bağlı adlandırmalar [kalıp] — ipliği çok, sık dokulu ve güçlü kumaş · akıl ve sağlam görüş sahibi kişi
  ثوب ذو أكل أي كثير الغزل؛ رجل ذو أكل ذو رأي وعقل؛ ثوب ذو أكل إذا كان كثير الغزل صفيقا؛ رجل ذو أكل إذا كان ذا عقل ورأي؛ ثوب ذو أكل كثير الغزل كذلك
- **B013** yemek yenilen kap veya yer — içinde yemek yenilen çanak veya tencere · kendisinden yemek yenilen yer
  المئكل إناء يؤكل فيه؛ المئكلة قصعة تشبع الرجلين والثلاثة؛ المأكلة والمأكلة الموضع الذي منه يؤكل؛ المئكلة ضرب من البرام وضرب من الأقداح وكل ما أكل فيه
- **B014** ete işleyen kesici veya vurucu araç [kalıp] — et kesen bıçak; ayrıca sivri sopa veya kamçı
  للسكين آكلة اللحم؛ آكلة اللحم عصا محددة؛ الأصل في هذا أنها السكين؛ قيل في آكلة اللحم إنها السياط

## و ر ث (root_001639) — identity root of ٱلتُّرَاثَ (w2)

- **B001** mirasın mirasçıya geçmesi — miras · miras, miras kalan mal · miras, kalıt · miras; atadan kalan köken veya kalıntı · miras yoluyla geçiş · miras · miras · miras almak, mirasçısı olmak · mirasçıları · kuşaktan kuşağa miras almak
  أن يكون الشيء لقوم ثم يصير إلى آخرين بنسب أو سبب (maqayis)؛ ورثت أبي وورثت الشيء من أبي (sihah)؛ ورث فلان أباه، ورثت فلانا مالا إذا مات مورثك فصار ميراثه لك (tahdhib)؛ الوراثة والإرث انتقال قنية إليك عن غيرك من غير عقد، وإرث أبيكم أي أصله وبقيته (mufradat)
- **B002** miras bırakmak veya emeksizce kazandırmak — miras bırakmak, miras yoluyla kazandırmak · malına miras payıyla dahil etmek · emeksizce elde etmek
  يصير إلى آخرين بنسب أو سبب (maqayis)؛ أورثه الشيء أبوه، ورثه توريثا أي أدخله في ماله على ورثته (sihah)؛ أورث الرجل ولده مالا، ورثت فلانا من فلان أي جعلت ميراثه له (tahdhib)؛ أورثني الله كذا، لكل من حصل له شيء من غير تعب، خول شيئا مهنئا (mufradat)
- **B003** maddi olmayan mirasın aktarılması — peygamberlik, bilgi veya erdemin maddi olmayan mirası · bilgiyi bir öncekinden edinmek · kitabı veya bilgisini miras yoluyla devralmak · peygamberlerin bilgi mirasçıları
  وراثة النبوة والعلم والفضيلة دون المال؛ العلماء ورثة الأنبياء؛ ورثت علما من فلان أي استفدت منه (mufradat)
- **B004** her şeyden sonra kalıp mülkün kendisine dönmesi — her şeyden sonra kalan ve her şeyin döndüğü varlık · ölümüne dek yanında kalan · göklerin ve yerin sonunda Tanrı'ya kalan mülkiyeti · yer ve üzerindekiler yok olduktan sonra kalıp mülkü geri almak
  الوارث صفة من صفات الله وهو الباقي الدائم (tahdhib)؛ يبقى ويفنى من سواه فيرجع ما كان ملك العباد إليه (tahdhib)؛ الأشياء كلها صائرة إلى الله (mufradat)
- **B005** koru karıştırıp ateşi tutuşturmak [kalıp] — ateşin korunu karıştırıp tutuşturmak · ateşin korunu karıştırıp tutuşturmak
  الورثة: لغة في ورثت النار وأرثتها إذا حركت جمرها لتشتعل (jamhara)

## ل م م (root_001378) — identity root of لَّمًّا (w4)

- **B001** dağınık olanı bütünüyle bir araya getirip düzenleme [kalıp] — dağınıklığını giderip toparladı · insanları bir araya toplayan ev · bölükleri birleşmiş kalabalık birlik · hepsini sonuna kadar aldı · kendi payıyla arkadaşının payını birlikte yiyiş
  لممت شعثه إذا ضممت ما كان متشعثا منتشرا (maqayis)؛ لم الله شعثه أي أصلح وجمع ما تفرق من أموره (sihah)؛ داركم لمومة أي تلم الناس وتربهم وتجمعهم (sihah)؛ كتيبة ملمومة كثر عددها واجتمع المقنب فيها إلى المقنب (maqayis)؛ كتيبة ململمة وملمومة أي مجتمعة مضموم بعضها إلى بعض (sihah)؛ لممته أجمع حتى أتيت على آخره (sihah)
- **B002** yanına gelip yakınında bulunma veya bir sınıra yaklaşma — yanına gelip yakınında bulundu · ergenliğe yaklaşmış oğlan · o sonuca ulaşmadan yaklaşır · bizi ara sıra ziyaret eder
  ألممت بالرجل إلماما إذا نزلت به وضاممته (maqayis)؛ الإلمام النزول وقد ألم به أي نزل به (sihah)؛ غلام ملم أي قارب البلوغ (sihah)؛ ما يقتل حبطا أو يلم أي يقرب من ذلك (sihah)؛ فلان يزورنا لماما أي في الأحايين (sihah)
- **B003** küçük yanlış veya yanlışı işlemeden ona yaklaşma — küçük yanlışlar veya yanlışı işlemeden ona yaklaşma · küçük yanlışlara bulaştı veya yanlışa yaklaştı
  اللمم ليس بمواقعة الذنب وإنما هو مقاربته ثم ينحجز عنه (maqayis)؛ اللمم وهو صغار الذنوب (sihah)؛ مقاربة المعصية من غير مواقعة (sihah)
- **B004** görünmeyen bir varlığın dokunmasına bağlanan zihinsel etkilenme — görünmeyen bir varlığın dokunması sayılan etki · hafif akıl bozukluğu · böyle bir etkilenmesi bulunan adam
  أصابت فلانا من الجن لمة وذلك كالمس (maqayis)؛ اللمم أيضا طرف من الجنون (sihah)؛ رجل ملموم أي به لمم (sihah)؛ أصابت فلانا من الجن لمة وهو المس (sihah)
- **B005** kulak memesini geçip omuzlara yaklaşan saç — kulak memesini geçip omuzlara yaklaşan saç · bu uzunluktaki saçlar
  اللمة بكسر اللام الشعر إذا جاوز شحمة الأذنين (maqayis)؛ لأنه شام المنكبين وقاربهما (maqayis)؛ اللمة بالكسر الشعر يجاوز شحمة الأذن فإذا بلغت المنكبين فهي جمة (sihah)
- **B006** başa gelen ağır olay ve zamanın sertliği — dünyada başa gelen ağır olay · zamanın ağır olayları ve sertliği
  الملمة النازلة من نوازل الدنيا (maqayis)؛ الملمة النازلة من نوازل الدنيا (sihah)؛ حادثات اللمة فهو الدهر ويقال الشدة (sihah)؛ صروف الدهر أو دولاتها اللمة من لماتها (sihah)
- **B007** kötülük verdiğine inanılan bakış [kalıp] — kötülük verdiğine inanılan göz
  العين اللامة الأصل ملمة لما قرنت بالسامة قيل لامة وهي التي تصيب بالسوء (maqayis)؛ العين اللامة التى تصيب بسوء (sihah)؛ أعيذه من كل هامة ولامة (sihah)
- **B008** sert ve yuvarlak kaya [kalıp] — sert, yuvarlak kaya · yuvarlak, sert kaya
  صخرة ململمة أي صلبة مستديرة وملمومة أيضا (maqayis)؛ صخرة ملمومة وململمة أي مستديرة صلبة (sihah)
- **B009** filin uzun burnu [kalıp] — filin uzun burnu
  ململمة الفيل خرطومه (sihah)
- **B010** Yemen halkı için belirlenmiş durak yeri — Yemen halkı için belirlenmiş durak olan yer · Yemen halkı için belirlenmiş durak olan yer
  يلملم وألملم موضع وهو ميقات أهل اليمن (sihah)

## ECHO ك ل ل (root_001315) — for وَتَأْكُلُونَ (w1): withheld observed target; not identity

- **B001** körelip güçten düşme — körelmek, yorulup güçten düşmek · körleşmiş, yorgun veya etkisiz · bineğini yorup güçten düşürmek
  خلاف الحدة وكل السيف واللسان والطرف (maqayis)؛ الكليل السيف الذي لا حد له ولسان كليل والكال المعيي (ayn)؛ كللت من المشي وكل السيف والريح والطرف واللسان (sihah)؛ الكليل السيف ولسان كليل والكال المعيي وثقل سمعه وكل بصره (tahdhib)؛ كل الرجل في مشيته والسيف عن ضريبته واللسان عن الكلام (mufradat)
- **B002** bakımı başkasına yük olan — bakımı ve geçimi sahibine yük olan · yetim veya yakın aile desteği bulunmayan kişi · sahibinin taşıdığı, ona yük olan tapınma nesnesi · bakmakla yükümlü olduğum kişiler · yakınlarının geçim yükünü üstlenir duruma gelmek
  الكُلّ العيال واليتيم (maqayis)؛ الكل اليتيم والكل الرجل الذي لا ولد له والكل أيضا الذي هو عيال وثقل (ayn)؛ الكل العيال والثقل والكل اليتيم والكل الذي لا ولد له ولا والد (sihah)؛ الكل الثقيل الروح واليتيم والوكيل والذي هو عيال وثقل على صاحبه (tahdhib)
- **B003** bütün, tüm — bütün, tüm, tamamı
  كل اسم موضوع للإحاطة مضاف أبدا (maqayis)؛ كل لفظه واحد ومعناه جمع (sihah)؛ يقع كل على اسم منكور موحد فيؤدي معنى الجماعة وكلهم للإحاطة (tahdhib)؛ لفظ كل هو لضم أجزاء الشيء ويفيد معنى التمام (mufradat)
- **B004** üstsoy ve altsoy dışı mirasçılık — ana baba ve çocuk dışındaki yan kol mirasçılığı · yan koldan değil, doğrudan hakla miras almak · uzak kuzen · soy bakımından daha uzak olmak
  الكلالة هم الرجال الورثة وبنو العم الأباعد ومن مات وليس له ولد ولا والد (maqayis)؛ الكل النسب البعيد (ayn)؛ لم يرثه كلالة أي لم يرثه عن عرض والكلالة بنو العم الأباعد (sihah)؛ الكلالة من القرابة ما خلا الوالد والولد (tahdhib)؛ الكلالة اسم لما عدا الولد والوالد من الورثة (mufradat)
- **B005** çevresini kuşak gibi saran oluşum — taç veya süslü baş kuşağı · Ay'ın konaklarından biri, Akrep takımyıldızının başı · bir yerin çevresini dolaşan örtümsü bulut · çiçeklerle çevrili çayır · çevresi küçük bulut parçalarıyla sarılı bulut · başına taç takmak
  إطافة شيء بشيء والإكليل منزل من منازل القمر والسحاب يدور بالمكان (maqayis)؛ الإكليل شبه عصابة مزينة بالجواهر والإكليل من منازل القمر وروضة مكللة حفت بالنور (ayn)؛ الإكليل شبه عصابة ويسمى التاج إكليلا والإكليل منزل والسحاب كأن غشاء ألبسه وروضة مكللة وسحاب مكلل (sihah)؛ الغمام المكلل السحابة تكون حولها قطع والإكليل شبه عصابة والإكليل منزل (tahdhib)؛ الإكليل سمي بذلك لإطافته بالرأس (mufradat)
- **B006** ev biçimli ince koruyucu örtü — böceklerden koruyan ev biçimli ince örtü, cibinlik · mezar üzerine küçük kule veya kubbe biçimli yapı yükseltmek
  الكلة غشاء من ثوب يتوقى به من البعوض (ayn)؛ الكلة الستر الرقيق يخاط كالبيت يتوقى فيه من البق (sihah)؛ الكلة من الستور ما خيط فصار كالبيت والتكليل رفعها ببناء مثل الكلل وهي الصوامع والقباب (tahdhib)
- **B007** göğüs — göğüs · göğüs
  الكلكل الصدر (maqayis)؛ الكلكل الصدر (ayn)؛ الكلكل والكلكال الصدر (sihah)؛ الكلكل فهو الصدر (tahdhib)؛ الكلكل الصدر (mufradat)
- **B008** kısa, kalın ve güçlü yapılı erkek [kalıp] — kısa, kalın, güçlü ve toplu yapılı erkek
  الكلكل القصير (maqayis)؛ الكلكل الرجل الضرب ليس بجد طويل والمربوع المجتمع الخلق (ayn)؛ رجل كلكل قصير غليظ مع شدة (sihah)؛ رجل كلكل وكلاكل وكوألل قصر وغلظ مع شدة (tahdhib)
- **B009** topluluklar, kümeler — topluluklar, kümeler
  الكلاكل من الجماعات كالكراكر من الخيل (ayn)؛ الكلاكل هي الجماعات كالكراكر (tahdhib)
- **B010** saldırıda ilerleme veya korkup geri durma; itaatsizlik — saldırıda durmadan ileri gitmek · savaşta korkup geri durmak · ona itaat etmemek, karşı gelmek
  كلل حمل ولعله أن يكون من المتضادات (maqayis)؛ المكلل الجاد حمل فكلل مضى قدما وقد يكون كلل بمعنى جبن (sihah)؛ المكلل الذي يحمل فلا يرجع حتى يقع بقرنه وكلل فلان فلانا لم يطعه (tahdhib)
- **B011** dişleri görünerek gülümseme ve bulutun şimşekle gülümser gibi olması — dişleri görünerek gülümsemek · bulutun içinden beyaz şimşek çakmak
  انكلت المرأة إذا ضحكت (maqayis)؛ انكل الرجل انكلالا تبسم وتنكل عن غر عذاب وانكلال الغيم بالبرق (sihah)؛ انكلت المرأة إذا تبسمت وانكل السحاب بالبرق إذا تبسم بالبرق (tahdhib)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:19, and ## Buluşmalar) =====
## Pay, sofra ve ağzına kadar dolan kap

Rızık bir paydır: {ar:الرزق يقال للعطاء الجاري وللنصيب, tr:er-rızku yukâlu li'l-atâi'l-câri ve li'n-nasîb, gloss:rızık, akıp gelen bağış için de pay için de söylenir, source:"ر ز ق,B001"}. Her şeyin bir ölçüsü vardır: {ar:لكل شيء مقدار وأجل, tr:li-kulli şey'in mikdârun ve ecel, gloss:her şeyin bir ölçüsü ve bir süresi vardır, source:"ق د ر,B001"}. Kur'an da geçimi kendisinin bölüştürdüğünü söyler: {ar:نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ, tr:nahnu kasemnâ beynehum maîşetehum, gloss:aralarında geçimlerini biz bölüştürdük, source:43:32}, {ar:ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ, tr:Allâhu yebsutu'r-rızka li-men yeşâu ve yakdir, gloss:Allah rızkı dilediğine genişletir ve daraltır, source:13:26}. Beşinci ayetteki kasem kelimesinin kökü bu bölüştürmeyi adlandırır, mirasın sahiplerine ayrılmasını da içine alarak: {ar:إفراز النصيب وقسمة الميراث والغنيمة تفريقهما على أربابهما, tr:ifrâzu'n-nasîbi ve kısmetu'l-mîrâsi ve'l-ğanîmeti tefrîkuhumâ alâ erbâbihimâ, gloss:payı ayırmak; miras ve ganimeti bölmek, onları sahiplerine dağıtmaktır, source:"ق س م,B003"}. Kur'an'ın miras hükmü surenin sofrasını tek bir ayette kurar: {ar:وَإِذَا حَضَرَ ٱلْقِسْمَةَ أُو۟لُوا۟ ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينُ فَٱرْزُقُوهُم مِّنْهُ, tr:ve izâ hadara'l-kısmete ulu'l-kurbâ ve'l-yetâmâ ve'l-mesâkînu ferzukûhum minh, gloss:paylaştırmada akrabalar, yetimler ve yoksullar hazır bulunursa onlara da ondan rızık verin, source:4:8}. Paylaştırma, yetim, yoksul ve rızık: on altıncı ayetle on dokuzuncu ayet arasındaki bütün öğeler buradadır. Payın kendisi de konmuştur: {ar:نَصِيبًۭا مَّفْرُوضًۭا, tr:nasîben mefrûdâ, gloss:belirlenmiş bir pay, source:4:7}.

On sekizinci ayet bu sofraya kimin çağrılmadığını söyler: {ar:وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ tehâddûne alâ taâmi'l-miskîn, gloss:yoksulu doyurmaya birbirinizi teşvik etmiyorsunuz, source:89:18}. Fiilin kalıbı karşılıklıdır: {ar:والمحاضة أن يحث كل واحد منهما صاحبه, tr:ve'l-muhâdda en yehusse kullu vâhidin minhumâ sâhibeh, gloss:muhâdda, ikisinden her birinin ötekini teşvik etmesidir, source:"ح ض ض,B001"}. Kınanan şey yalnız tek tek kişilerin cimriliği değildir. Topluluğun birbirini yoksula yöneltmeyi bırakmasıdır. Yemek, birinin istediği şeydir: {ar:استطعمه سأله أن يطعمه, tr:istat'amehû seelehû en yut'imeh, gloss:ondan yemek istedi, source:"ط ع م,B002"}. Yoksul da zayıf düşmüş kişidir: {ar:المسكين الفقير وقد يكون بمعنى الذلة والضعف, tr:el-miskînu'l-fakîr, ve kad yekûnu bi-ma'ne'z-zilleti ve'd-da'f, gloss:miskin fakirdir; düşkünlük ve zayıflık anlamına da gelir, source:"س ك ن,B006"}. Aynı kök azığı, insanın yerinde kalabilmesini sağlayan şey olarak adlandırır: {ar:قيل للقوت سكن لأن المكان به يسكن, tr:kîle li'l-kûti sekenun li-enne'l-mekâne bihî yusken, gloss:azığa seken denir, çünkü bir yerde onunla oturulur, source:"س ك ن,B010"}. Yoksulun payını vermek, onun yerinde durabilmesini sağlamaktır. Kur'an aynı cümleyi başka iki sahnede tekrarlar. Biri dini yalanlayanın tarifidir: {ar:فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ, tr:fe-zâlike'llezî yeduu'l-yetîm, gloss:işte o, yetimi itip kakandır, source:107:2}, {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:yoksulu doyurmaya teşvik etmez, source:107:3}. Öteki kitabı sol eline verilen kişinin zincirlenme sebebidir {source:69:34}. Sarp yokuş da açlık gününde yakın bir yetimi ya da toprağa düşmüş bir yoksulu doyurmaktır: {ar:أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ, tr:ev it'âmun fî yevmin zî mesğabeh, gloss:ya da açlık gününde doyurmak, source:90:14}, {ar:يَتِيمًۭا ذَا مَقْرَبَةٍ, tr:yetîmen zâ makrabeh, gloss:yakını olan bir yetimi, source:90:15}, {ar:أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ, tr:ev miskînen zâ metrabeh, gloss:ya da toprağa düşmüş bir yoksulu, source:90:16}.

On dokuzuncu ayet sofranın öbür ucunu gösterir: {ar:وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا, tr:ve te'kulûne't-turâse eklen lemmâ, gloss:mirası silip süpürerek yiyorsunuz, source:89:19}. Miras, bir topluluğa ait olanın başkalarına geçmesidir: {ar:أن يكون الشيء لقوم ثم يصير إلى آخرين بنسب أو سبب, tr:en yekûne'ş-şey'u li-kavmin summe yasîra ilâ âharîne bi-nesebin ev sebeb, gloss:bir şeyin bir topluluğa ait olup sonra soy ya da başka bir sebeple başkalarına geçmesi, source:"و ر ث,B001"}. Miras geçerken paylara ayrılmalıdır. Lemm ise ayırmadan hepsini toplamaktır: {ar:لممته أجمع حتى أتيت على آخره, tr:lememtuhû ecmaa hattâ eteytu alâ âhirih, gloss:sonuna kadar hepsini toplayıp aldım, source:"ل م م,B001"}. Yemek fiili zayıfların malını yemeyi de anlatır: {ar:فلان يستأكل الضعفاء أي يأخذ أموالهم, tr:fulânun yeste'kilu'd-duafâe ey ye'huzu emvâlehum, gloss:falanca zayıfları yiyor, yani mallarını alıyor, source:"ء ك ل,B004"}. Kur'an yetimlerin malı için şöyle uyarır: {ar:وَلَا تَأْكُلُوٓا۟ أَمْوَٰلَهُمْ إِلَىٰٓ أَمْوَٰلِكُمْ, tr:ve lâ te'kulû emvâlehum ilâ emvâlikum, gloss:onların mallarını kendi mallarınıza katarak yemeyin, source:4:2}. O malın aslında ne olduğunu da gösterir: {ar:إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا, tr:innemâ ye'kulûne fî butûnihim nârâ, gloss:onlar karınlarına ancak ateş yerler, source:4:10}. Aynı fiil ateşin işidir: {ar:أكلت النار الحطب, tr:ekeleti'n-nâru'l-hatab, gloss:ateş odunu yedi, source:"ء ك ل,B005"}. Yiyen, yirmi üçüncü ayette getirilen ateşle karşılaşır. Miras da sonunda asıl sahibine döner: {ar:يبقى ويفنى من سواه فيرجع ما كان ملك العباد إليه, tr:yebkâ ve yefnâ men sivâhu fe-yerciu mâ kâne milke'l-ibâdi ileyh, gloss:O kalır, O'ndan başkası yok olur ve kulların mülkü O'na döner, source:"و ر ث,B004"}. Kur'an bunu şöyle söyler: {ar:إِنَّا نَحْنُ نَرِثُ ٱلْأَرْضَ وَمَنْ عَلَيْهَا وَإِلَيْنَا يُرْجَعُونَ, tr:innâ nahnu neriçu'l-arda ve men aleyhâ ve ileynâ yurceûn, gloss:yere ve üzerindekilere biz varis oluruz ve onlar bize döndürülür, source:19:40}. Bir başka ayet de göklerin ve yerin mirasının Allah'a ait olduğunu hatırlatarak harcamaya çağırır {source:57:10}.

Yirminci ayet yığılan malı bir kaba koyar: {ar:وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا, tr:ve tuhibbûne'l-mâle hubben cemmâ, gloss:malı aşırı bir sevgiyle seviyorsunuz, source:89:20}. Cemm bir ölçeğin ağzına kadar dolmasıdır: {ar:أعطيته جمام المكوك وجمامه إذا قارب أن يمتلئ, tr:a'taytuhû cumâme'l-mekkûki ve cimâmehû izâ kâraba en yemtelî', gloss:ölçeği ağzına kadar, neredeyse taşacak kadar doldurup verdim, source:"ج م م,B001"}. Suyun yığılmış kütlesi de böyle adlandırılır: {ar:جمة الماء معظمه ومجتمعه, tr:cemmetu'l-mâi mu'zamuhû ve muctemeuh, gloss:suyun cemmesi, en büyük ve toplanmış kısmıdır, source:"ج م م,B001"}. Sevgi kelimesinin kökü de dolmayı ve kabı adlandırır: {ar:وحببته فتحبب إذا ملأته للسقاء وغيره, tr:ve habebtuhû fe-tehabbebe izâ mele'tuhû li's-sikâi ve ğayrih, gloss:su tulumunu ve benzerini doldurdum, doldu, source:"ح ب ب,B006"}, {ar:الحب الجرة الضخمة, tr:el-hubb el-cerratu'd-dahme, gloss:hubb, iri küptür, source:"ح ب ب,B007"}. Aynı harfler tahılı da adlandırır: {ar:الحب والحبة في الحنطة والشعير, tr:el-habbu ve'l-habbe fi'l-hıntati ve'ş-şaîr, gloss:habb, buğday ve arpa tanesidir, source:"ح ب ب,B001"}. Ayette anlam aşırı sevgidir. Yanında ağzına kadar dolmuş bir küp duyulur, hem de yoksulun istediği tahılla dolu bir küp. On ikinci ayetteki çoğaltma fiili de bu yarışı taşır: {ar:المكاثرة والتكاثر التباري في كثرة المال والعز, tr:el-mukâsera ve't-tekâsur et-tebârî fî kesreti'l-mâli ve'l-izz, gloss:mal ve itibar çokluğunda yarışmak, source:"ك ث ر,B002"}. Kur'an bu dolduranı birkaç sahnede gösterir: {ar:أَلْهَىٰكُمُ ٱلتَّكَاثُرُ, tr:elhâkumu't-tekâsur, gloss:çoğaltma yarışı sizi oyaladı, source:102:1}. Bir diğeri malı toplayıp sayandır: {ar:ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ, tr:ellezî cemea mâlen ve addedeh, gloss:mal toplayıp onu sayan, source:104:2}, {ar:يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ, tr:yahsebu enne mâlehû ahledeh, gloss:malının kendisini ölümsüz kılacağını sanır, source:104:3}. Ateş de toplayıp istifleyeni çağırır: {ar:وَجَمَعَ فَأَوْعَىٰٓ, tr:ve cemea fe-ev'â, gloss:toplayıp kaba istifleyen, source:70:18}. Sevginin sofraya dönen biçimi de Kur'an'dadır: {ar:وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا, tr:ve yut'imûne't-taâme alâ hubbihî miskînen ve yetîmen ve esîrâ, gloss:yemeği, ona olan sevgilerine rağmen yoksula, yetime ve esire yedirirler, source:76:8}. Malın da: {ar:وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ, tr:ve âte'l-mâle alâ hubbihî zevi'l-kurbâ ve'l-yetâmâ ve'l-mesâkîn, gloss:malı, ona olan sevgisine rağmen akrabalara, yetimlere ve yoksullara veren, source:2:177}. Sevgi aynıdır, ama burada kap dolmaz, boşaltılır. Ağzına kadar dolmuş küpün sonu da Kur'an'da gösterilir. Kitabı sol eline verilen şöyle der: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ ۜ, tr:mâ ağnâ annî mâliyeh, gloss:malım bana hiçbir yarar sağlamadı, source:69:28}. Cehennem ise hiç dolmayan bir kaptır: {ar:يَوْمَ نَقُولُ لِجَهَنَّمَ هَلِ ٱمْتَلَأْتِ وَتَقُولُ هَلْ مِن مَّزِيدٍۢ, tr:yevme nekûlu li-cehenneme heli'mtele'ti ve tekûlu hel min mezîd, gloss:o gün cehenneme "doldun mu?" deriz, o da "daha yok mu?" der, source:50:30}.

Kaynaklar: 89:5 قَسَمٌۭ ق س م B003; 89:12 فَأَكْثَرُوا۟ ك ث ر B002; 89:16 فَقَدَرَ ق د ر B001; 89:16 رِزْقَهُۥ ر ز ق B001; 89:18 تَحَٰٓضُّونَ ح ض ض B001; 89:18 طَعَامِ ط ع م B002; 89:18 ٱلْمِسْكِينِ س ك ن B006; 89:18 ٱلْمِسْكِينِ س ك ن B010; 89:19 وَتَأْكُلُونَ ء ك ل B004; 89:19 وَتَأْكُلُونَ ء ك ل B005; 89:19 ٱلتُّرَاثَ و ر ث B001; 89:19 ٱلتُّرَاثَ و ر ث B004; 89:19 لَّمًّۭا ل م م B001; 89:20 حُبًّۭا ح ب ب B001; 89:20 وَتُحِبُّونَ ح ب ب B006; 89:20 حُبًّۭا ح ب ب B007; 89:20 جَمًّۭا ج م م B001

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

