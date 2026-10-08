Focus: 99:5. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/99_5/D.r13/context.md =====
# 99:5 — focus

بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا

Anchor translation (canonical reading, reference only):

Çünkü Rabbin ona vahyetmiştir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | بِأَنَّ | أَنّ |  | P;ACC |
| 2 | رَبَّكَ | رَبّ | ر ب ب | N;PRON |
| 3 | أَوْحَىٰ | أَوْحَىٰٓ | و ح ي | V |
| 4 | لَهَا |  |  | P;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 99 — full text (context; no pericope)

- 99:1 إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا
- 99:2 وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا
- 99:3 وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا
- 99:4 يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا
- 99:5 ◀ focus بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
- 99:6 يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
- 99:7 فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
- 99:8 وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ


===== _commentary/v16/work/99_5/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر ب ب (root_000532) — identity root of رَبَّكَ (w2)

- **B001** sahip olup yönetme — Tanrı; sahip, buyruğu geçen yönetici veya düzenleyici · bir şeyin sahibi · evin sahibi veya ev işlerini yöneten kadın · sahiplik, egemenlik ve yönetim yetkisi
  الرب: الله تبارك وتعالى؛ ورب كل شيء مالكه (jamhara); رب كل شئ: مالكه؛ وقد قالوه في الجاهلية للملك؛ رببت القوم: سستهم (sihah); يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح (tahdhib); الرب مصدر مستعار للفاعل؛ لا يقال الرب مطلقا إلا لله؛ رب الدار ورب الفرس (mufradat); فالرب المالك والخالق والصاحب؛ والله جل ثناؤه الرب (maqayis)
- **B002** adım adım yetiştirip tamamlama — yapılan iyiliği eksiksiz kılmak · mülkü gözetip iyileştirmek · çocuğunu yetiştirmek · bir şeyi aşama aşama olgunlaştırma · yetiştirme anlamındaki değişmeli söyleyiş
  رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها (jamhara); رب الضيعة أي أصلحها وأتمها؛ رب فلان ولده؛ رباه (sihah); رب الشيء أي أصلحه؛ رب فلان الصنيعة إذا أتمها وأصلحها (tahdhib); التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام؛ ربه ورباه ورببه (mufradat); رب فلان ضيعته إذا قام على إصلاحها؛ رببت الصبي أربه (maqayis); ربته تربيتا إذا رببه (maqayis-rbt)
- **B003** Tanrı bilgisiyle yetiştiren bilgin — Tanrı bilgisine sahip bilgin ve öğretici
  الرباني: المتأله العارف بالله تعالى (sihah); الرباني: العالم؛ العلماء بالحلال والحرام؛ حكماء علماء؛ العالم المعلم الذي يغذو الناس بصغار العلوم (tahdhib); الرباني... يرب العلم؛ يرب نفسه بالعلم؛ منسوب إلى الرب (mufradat); الربي العارف بالرب (maqayis)
- **B004** büyük insan topluluğu — büyük topluluk; on bin kişilik topluluk · tek birlik hâlinde birleşmiş beş kabile · insanları toplayan kişi veya toplanma yeri
  الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا (sihah); الربيون: الألوف؛ الربيون: الجماعات الكثيرة؛ الربة: عشرة آلاف؛ الربان: الجماعة (tahdhib); يجوز أن يضم الربرب إلى الباب الثالث لتجمعه (maqayis)
- **B005** bakımla kurulan üvey aile bağı — üvey oğul veya bakım altında yetişen erkek çocuk · üvey kız veya bakım altında yetişen kız çocuk · bakıcı kadın; evde sütü için beslenen dişi hayvan · çocuğun bakımını üstlenen üvey baba veya üvey anne
  الراب: زوج الأم؛ الرابة: امرأة الأب؛ ربيب الرجل: ابن امرأته من غيره؛ الربيبة: الحاضنة (sihah); الربيب: ابن امرأة الرجل من غيره؛ ربيبة الرجل: بنت امرأته من غيره؛ راب ورابة (tahdhib); الراب والرابة بأحد الزوجين إذا تولى تربية الولد؛ الربيب والربيبة بذلك الولد (mufradat); ربيب الرجل ابن امرأته؛ الراب الذي يقوم على أمر الربيب (maqayis)
- **B006** koyu öz veya yağ tortusu — koyu meyve özü veya yağ tortusu · koyu özle işlenmiş veya güçlendirilmiş · koyu meyve özüyle hazırlanmış yiyecekler
  رب السمن والزيت: ثفله الأسود؛ سقاء مربوب إذا أصلح بالرب (jamhara); الرب: الطلاء الخاثر؛ سقاء مربوب؛ المرببات الأنبجات (sihah); رب فلان نحيه إذا جعل فيه الرب ومتنه به؛ نحي مربوب (tahdhib); رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب (mufradat); هذا سقاء مربوب بالرب؛ الرب للعنب وغيره لأنه يرب به الشيء (maqayis)
- **B007** bir yerde kalıp sürme — bir yerde kalıp ayrılmamak · develerin sürekli kaldığı yer · bulut sürüp gitti · dişi deve erkeğe bağlandı · bir şeye yaklaşma
  رب بالمكان وأرب إذا أقام به (jamhara); مرب الإبل حيث لزمته؛ أربت الإبل؛ أربت الناقة؛ أربت الجنوب والسحابة أي دامت؛ الأرباب الدنو (sihah); أرب فلان بالمكان إذا أقام به فلم يبرحه؛ مرب الإبل أي حيث لزمته (tahdhib); أربت السحابة: دامت؛ أرب فلان بمكان كذا (mufradat); الأصل الآخر لزوم الشيء والإقامة عليه؛ أربت السحابة؛ الإرباب الدنو (maqayis)
- **B008** katmanlı asılı bulut kümesi — beyaz olabilen, katmanlı veya aşağıda asılı bulut
  الرباب: سحاب أبيض؛ الواحدة ربابة (sihah); الربابة: السحابة التي قد ركب بعضها بعضا؛ جمعها رباب (tahdhib); الرباب: السحاب، سمي بذلك لأنه يرب النبات (mufradat); سمي السحاب ربابا؛ السحاب المتعلق دون السحاب يكون أبيض ويكون أسود (maqayis)
- **B009** başlangıçtaki tazelik — yeni doğurmuş veya sütü için evde tutulan koyun · bir şeyin yeni ve taze dönemi · gençliğin ilk ve taze dönemi
  الربى: الشاة التي وضعت حديثا؛ قرب العهد بالولادة؛ بربانه أي بحدثانه وجدته وطراءته (sihah); الربى: أول الشباب؛ الربان من كل شيء: حدثانه؛ الشاة فهي ربى (tahdhib); الشاة الربي التي تحتبس في البيت للبن؛ التي وضعت حديثا (maqayis)
- **B010** kura oklarını toplayan kap — kura oklarını bir arada tutan deri veya bez kap
  الربابة: قطعة من أدم تجمع فيها القداح (jamhara); الربابة شبيهة بالكنانة تجمع فيها سهام الميسر؛ جماعة السهام (sihah); الربابة: جماعة السهام؛ الجلدة التي تجمع فيها السهام (tahdhib); لما يجمع فيه القدح ربابة (mufradat); الخرقة التي يجعل فيها القداح ربابة (maqayis)
- **B011** bağlayıcı söz ve güvence — tarafları birleştiren bağlayıcı söz veya sözleşme · sözleşmeye bağlı taraflar · bağlayıcı söz; söz gibi bağlayıcı vergi payı
  الربابة: العهد والمعاهدون أربة (jamhara); الربابة: العهد والميثاق؛ الأربة أهل الميثاق (sihah); الرباب: العهد؛ الرباب: العشور (tahdhib); العقد في موالاة الغير: الربابة (mufradat); الربابة وهو العهد؛ للمعاهدين أربة؛ الرباب العشور (maqayis)
- **B012** belirli bir yeşil bitki türü — belirli bir bitki, yumuşak ot veya küçük ağaç türü
  الربة: ضرب من الشجر أو النبت (jamhara); الربة بالكسر: ضرب من النبت، والجمع الربب (sihah); الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف (tahdhib)
- **B013** bol ve toplanmış su — çok miktarda su; bazen bol tatlı su
  الربب، بالفتح: الماء الكثير، ويقال العذب (sihah); الربب وهو الماء الكثير سمي بذلك لاجتماعه (maqayis)
- **B014** yaban sığırı sürüsü — yaban sığırı sürüsü; bazen sığır veya deve topluluğu
  الربرب: القطيع من بقر الوحش (sihah); الربرب: جماعة البقر، وكذلك الإبل (tahdhib); الربرب القطيع من بقر الوحش؛ يجوز أن يضم إلى الباب الثالث لتجمعه (maqayis)
- **B015** azlık bildiren ilgeç — belirsiz adla azlık bildiren ilgeç; nice az · eylem önünde bazen veya kimi zaman · azlık ilgecinin sonuna ses eklenmiş ağız biçimi · belirsiz öğe eklenmiş azlık ilgeci biçimi
  رب: كلمة؛ ربما؛ ربت في معنى رب (jamhara); رب حرف خافض؛ ربما؛ ربت؛ ربه رجلا (sihah); رب من حروف المعاني؛ رب للتقليل؛ ربما؛ ربتما؛ تزيد في رب هاء (tahdhib); رب لاستقلال الشيء، ولما يكون وقتا بعد وقت، نحو ربما (mufradat); رب فكلمة تستعمل في الكلام لتقليل الشيء؛ ولا يعرف لها اشتقاق (maqayis)
- **B016** gereksinim, sıkı düğüm veya iyilik — gereksinim · sıkıca bağlanmış düğüm · iyilik ve başkasına yarar sağlama
  الربى: الحاجة؛ الربى: الرابة؛ الربى: العقدة المحكمة؛ الربى: النعمة والإحسان (tahdhib)
- **B017** gemicilerin başı — gemicilerin başı, kaptan
  رباني: رئيس الملاحين (tahdhib)

## و ح ي (root_001633) — identity root of أَوْحَىٰ (w3)

- **B001** bilgiyi ya da sözü gizlice iletme — bilgiyi ya da sözü gizlice iletme · sözü başkalarından gizleyerek ona söylemek · güvenilir bir elçi göndermek ya da aracısız konuşmak
  أصل يدل على إلقاء علم في إخفاء إلى غيرك (maqayis)؛ كل ما ألقيته إلى غيرك (maqayis;sihah)؛ إعلام في خفاء (tahdhib)؛ يكون بالكلام على سبيل الرمز والتعريض (mufradat)
- **B002** işaret veya simgeyle anlatma — işaret veya beden hareketiyle anlatma · ona işaret etmek · bir haberi işaretle anlatmak ya da hafif sesle söylemek
  الوحي الإشارة (maqayis;sihah)؛ من الناس إشارة (jamhara)؛ أومأ إليهم وأشار (jamhara;tahdhib)؛ رمز أو أشار (mufradat)
- **B003** yazma ve yazılı metin — yazı, kitap, ileti veya yazma · yazmak · taşa yazmak · kitabı yazmak
  الوحي الكتاب والرسالة (maqayis)؛ وحي يحي وحيا أي كتب (ayn)؛ وحى في الحجر إذا كتب فيه (jamhara)؛ وحى وأوحى أي كتب (sihah)؛ وحيت الكتاب أي كتبته (tahdhib)؛ بالكتابة (mufradat)
- **B004** Tanrı'nın seçilmiş kuluna bildirimi — Tanrı'nın seçilmiş kuluna bilgi ulaştırması
  أوحى الله تعالى ووحى (maqayis)؛ من الله نبأ وإلهام (jamhara)؛ أوحى الله إلى أنبيائه (sihah)؛ إما إلهاما وإما رؤيا وإما أن ينزل عليه كتابا (tahdhib)؛ الكلمة الإلهية التي تلقى إلى أنبيائه وأوليائه (mufradat)
- **B005** ses, özellikle hafif veya uzayan ses — ses, özellikle hafif veya uzayan ses · haberi işaretle ya da hafif sesle iletmek · ses · gök gürültüsünün uzayan hafif sesi
  الوحي الصوت (maqayis)؛ الوحى مثال الوغى الصوت (sihah)؛ وحاة الرعد وهو صوته الممدود الخفي (sihah)؛ الوحاة الصوت (tahdhib)؛ بصوت مجرد عن التركيب (mufradat)
- **B006** hız, acele ve hızlandırma — hızlı · hız · acele, acele · acele et · onu hızlandırdı · çabuk gelen ölüm · hayvanını hızla kesmek
  الوحي السريع (maqayis)؛ الوحاء السرعة (jamhara;tahdhib)؛ الوحي الوحي يعني البدار البدار (sihah)؛ توح يا هذا أي أسرع (sihah;tahdhib)؛ وحاه توحية أي عجله (sihah)؛ وحى فلان ذبيحته إذا ذبحه ذبحا وحيا (tahdhib)؛ أمر وحي (mufradat)
- **B007** yardım isteme, sorma veya salmak için çağırma — onlardan yardım istemek · ona sorup bilgi istemek · köpeği salmak için çağırmak
  استوحيناهم أي استصرخناهم (sihah)؛ استوحيته أي استفهمته (tahdhib)؛ استوحيت الكلب إذا دعوته لترسله (tahdhib)
- **B008** özel adlandırma kümesi — yoksulluktan sonra hükümdar olmak · yönetiminde zulmetmek · ateş · hükümdar
  أوحى الإنسان إذا صار ملكا بعد فقر؛ أوحى الإنسان ووحى وأحى إذا ظلم في سلطانه؛ الوحى النار؛ يقال للملك وحى؛ الوحى النار فكأنه مثل النار ينفع ويضر
- **B009** ağlama ve ölünün ardından ağıt yakma — ağlama · babasının ardından ağlamak · ölünün ardından ağıt yakmak
  الإيحاء البكاء؛ فلان يوحي أباه أي يبكيه؛ النائحة توحي الميت تنوح عليه
- **B010** taşa kazınmış yazı benzetmeleri [kalıp] — sırrını güvenle saklayan kişi için söylenen söz · taşa kazınmış yazı kadar apaçık
  وحي في حجر يضرب مثلا لمن يكتم سره؛ هو كالوحي في الحجر إذا نقر فيه نقرا

## ECHO ر ب و (root_000537) — for رَبَّكَ (w2): withheld observed target; not identity

- **B001** artmak veya yükselmek — bir şey arttı veya yükseldi · toprak suyla kabarıp arttı · yükselen veya fazla köpük · olağandan daha şiddetli yakalayış · onun üzerine çıktı veya üstünde bulundu
  ربا الجرح والأرض والمال وكل شيء يربو إذا زاد (ayn)؛ ربا الشيء يربو ربوا إذا ارتفع (jamhara)؛ ربا الشيء يربو ربوا أي زاد (sihah;tahdhib)؛ ربت أي زادت، وزبدا رابيا، وأخذة رابية (tahdhib;mufradat)؛ أربى عليه أي أشرف عليه (mufradat)
- **B002** yükselmiş arazi — yükselmiş arazi · çevresinden yüksek yer · arazideki yükselti
  الرابية ما ارتفع من الأرض، والربوة لغات أرض مرتفعة (ayn)؛ الربو والربوة والرباوة واحد وهو العلو من الأرض (jamhara)؛ الرابية الربو وهو ما ارتفع من الأرض، وكذلك الربوة (sihah)؛ الرباوة والرابية والرباة كل ذلك ما ارتفع من الأرض (tahdhib)؛ ربوة وربوة وربوة ورباوة، وسميت الربوة رابية (mufradat)
- **B003** belirli işlem biçimleriyle sınırlı anapara fazlalığı — belirli alışveriş veya borç biçimlerinde anaparayı aşan fazlalık · işlemdeki anapara fazlalığının özel adı veya bir söyleyiş biçimi · mal bu işlemde fazlalıkla arttı · anaparaya fazlalık eklenen işleme girdi
  ربا المال يربو في الربا أي يزداد، والربا في كتاب الله حرام، والربية هي الربا خاصة (ayn)؛ الربا في البيع، والربية لغة في الربا (sihah)؛ الربا ربوان، فالحرام كل قرض يؤخذ به أكثر منه (tahdhib)؛ الربا الزيادة على رأس المال، لكن خص في الشرع بالزيادة على وجه دون وجه (mufradat)
- **B004** soluğu yükselip sıkışmak — yüksek ve sıkışık soluma · soluğu sıkıştı · at koşu ya da ürkme yüzünden şişip soluksuz kaldı · soluğu yükselip tıkanmış
  ربا فلان أي أصابه نفس في جوفه ودابة بها ربو (ayn)؛ أصابه ربو من مشي أو عدو إذا علت أنفاسه (jamhara)؛ الربو النفس العالي، وربا الفرس إذا انتفخ من عدو أو فزع (sihah)؛ أخذها الربو وهو البهر (tahdhib)؛ الربو الانبهار سمي بذلك تصورا لتصعده (mufradat)
- **B005** besleyip büyütmek ve yetişmek — onu besleyip büyüttü · onların arasında yetişti · çocuğu besleyip büyüttü, çocuk gelişti
  ربيته وتربيته أي غذوته (ayn)؛ ربوت في بني فلان وربيت أي نشأت فيهم، وربيته تربية وتربيته أي غذوته، هذا لكل ما ينمي كالولد والزرع (sihah)؛ ربيت الولد فربا من هذا (mufradat)
- **B006** uyluk kökü ve iç yanlardaki iki çıkıntılı et parçası — uyluk kökü veya kasık eti · uyluk köklerinin iç yanlarındaki iki çıkıntılı et parçası
  الأربية أصل الفخذ، وهما أربيتان (sihah)؛ الأربيتان لحمتان ناتئتان في أصول الفخذين من باطن (mufradat)
- **B007** baba tarafından yakın hane halkının arasına gelmek [kalıp] — kendi topluluğundaki baba tarafından yakın hane halkının arasına geldi
  جاء فلان في أربية قومه، أي في أهل بيته من بني الأعمام ونحوهم، ولا تكون الأربية من غيرهم (sihah)

===== _commentary/v16/out/s099/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 99:5, and ## Buluşmalar) =====
## Sarsılan ve yükünü dışarı atan yer

Surenin ilk iki ayeti bir nesneyi ve onun nasıl çalıştığını gösterir. Nesne yerdir: üzerinde durduğumuz, göğün karşısında aşağıda kalan gövde {ar:الأرض التي نحن عليها, tr:el-arzu’lletî nahnu aleyhâ, gloss:üzerinde bulunduğumuz yer, source:"ء ر ض,B001"}. Önce sarsılır: {ar:إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا, tr:izâ zulziletil-arzu zilzâlehâ, gloss:yer kendi sarsıntısıyla sarsıldığında, source:99:1}. Zelzele, yatışmayan çalkantıdır {ar:الزلزلة: الاضطراب, tr:ez-zelzele: el-ıdtırâb, gloss:zelzele, çalkalanmadır, source:"ز ل ز ل,B001"}; kelimenin tanımı da tam bu iki kelimeyle verilir, yerin sarsılmasıyla. Fiilin ardından gelen "kendi sarsıntısı" sarsılmanın yere ait, ona göre ölçülmüş olduğunu söyler: yer, taşıyabileceği en büyük sarsıntıyla sarsılır.

Bu kelime ailelerinden gelen imgeler, kelimenin kendi ayetindeki anlamının yanında duyulur, onun yerine geçmez; aşağıdaki bütün bölümlerde böyle okunmalıdır.

Sarsıntının işi ikinci ayette görünür: {ar:وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا, tr:ve ahracetil-arzu eskâlehâ, gloss:ve yer ağırlıklarını dışarı çıkardığında, source:99:2}. Çıkmak girmenin tersidir ve bir şeyin durduğu yerden, karargâhından belirmesidir {ar:خرج خروجا برز من مقره أو حاله, tr:harace hurûcen beraze min makarrihî ev hâlih, gloss:durduğu yerden ya da hâlinden çıkıp belirdi, source:"خ ر ج,B001"}; çıkarmak da çoğunlukla somut nesneler için söylenir {source:"خ ر ج,B002"}. Neyin çıktığını ise yerin ağırlıkları söyler: {ar:أثقال الأرض كنوزها وأجساد بني آدم, tr:eskâlul-arz künûzuhâ ve ecsâdu benî âdem, gloss:yerin ağırlıkları hazineleri ve Âdemoğullarının bedenleridir, source:"ث ق ل,B002"}. Aynı kelime yolcunun yüküne, ağırlığına da denir {source:"ث ق ل,B002"}. Yer bir kap gibi içinde ağır şeyler taşımıştır; sarsıntı onları yerinden oynatır, çıkarma onları içeriden dışarıya geçirir. Sahne, içi boşalmış ve içindekileri yüzeyine bırakmış bir yerle kapanır. Sade bir anlatım "kıyamet kopar, ölüler dirilir" der; ayetler ise ölülerin dirilişini yerin bir yükü indirmesi olarak, ağırlığın yer değiştirmesi olarak gösterir.

Yere yapışan ağırlık bu sahneye bir derinlik daha katar. Yer kelimesinden türeyen bir fiil yere yapışıp kalmayı anlatır {ar:التأرض أيضا التثاقل إلى الأرض, tr:et-teerruzu eyzan et-tesâkulu ilel-arz, gloss:yere yapışmak, yere doğru ağırlaşmaktır, source:"ء ر ض,B006"}; ağırlık kökü de yavaşlık, yere çöküş demektir {ar:المثقل البطيء والتثاقل من التباطؤ, tr:el-muskal el-batî’ ve’t-tesâkul minet-tebâtu’, gloss:ağırlaşmış olan yavaştır, ağırlaşmak ağırdan almaktır, source:"ث ق ل,B006"}. Kur’an bu ağırlaşmayı, sefere çağrılıp yerinden kıpırdamayan müminlere Allah’ın sorduğu soruda kullanır: {ar:مَا لَكُمْ إِذَا قِيلَ لَكُمُ ٱنفِرُوا۟ فِى سَبِيلِ ٱللَّهِ ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ, tr:mâ lekum izâ kîle lekumu’nfirû fî sebîlillâhi’ssâkaltum ilel-arz, gloss:size ne oluyor ki Allah yolunda sefere çıkın denince yere ağırlaşıp kaldınız, source:9:38}. Ayetlerini verdiği hâlde yere saplanan adam için de {ar:أَخْلَدَ إِلَى ٱلْأَرْضِ, tr:ahlede ilel-arz, gloss:yere saplanıp kaldı, source:7:176} denir. Surenin yeri bu yapışkan ağırlığı tutmuştur. Sarsıntı bunu tersine çevirir: aynı kelimenin bir kullanımı yerde oyalanmadan hızla kalkmayı anlatır {ar:فقام عجلان وما تأرضا, tr:fekâme acelâne ve mâ teerradâ, gloss:aceleyle kalktı, yerde oyalanmadı, source:"ء ر ض,B006"}. Bunu sağlayan, beşinci ayetteki vahyin hız anlamıdır {ar:الوحي السريع, tr:el-vahyu’s-serî’, gloss:vahy, hızlı olandır, source:"و ح ي,B006"}. Kur’an da emrin tek bir göz kırpması olduğunu söyler: {ar:وَمَآ أَمْرُنَآ إِلَّا وَٰحِدَةٌ كَلَمْحٍۭ بِٱلْبَصَرِ, tr:ve mâ emrunâ illâ vâhidetun kelemhın bil-basar, gloss:emrimiz bir tekten ibarettir, göz kırpması gibi, source:54:50}; diriliş günü de {ar:يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًا, tr:yevme teşakkakul-arzu anhum sirâan, gloss:yer üzerlerinden yarılır, hızla çıkarlar, source:50:44} diye anlatılır.

Kur’an bu sahneyi başka yerlerde de kurar. Gök yarıldığında {source:84:1} yer de uzatılır ve {ar:وَأَلْقَتْ مَا فِيهَا وَتَخَلَّتْ, tr:ve elkat mâ fîhâ ve tehallet, gloss:içindekini atar ve boşalır, source:84:4}; kaplar kabristanlar için {ar:وَإِذَا ٱلْقُبُورُ بُعْثِرَتْ, tr:ve izel-kubûru bu‘siret, gloss:kabirler altüst edildiğinde, source:82:4} denir ve nankör insana {ar:أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ, tr:efelâ ya‘lemu izâ bu‘sire mâ fil-kubûr, gloss:kabirlerdekiler altüst edilip çıkarıldığında bilmez mi, source:100:9} diye sorulur. Sarsıntının adı bu kökle Allah’ın insanlara hitabında geçer: {ar:إِنَّ زَلْزَلَةَ ٱلسَّاعَةِ شَىْءٌ عَظِيمٌ, tr:inne zelzeletes-sâati şey’un azîm, gloss:Saatin sarsıntısı büyük bir şeydir, source:22:1}. Yerin çalkalanması başka kelimelerle de söylenir {source:56:4}, {source:73:14}, {source:79:6}, {source:89:21}, {source:69:14}. Bedenlerin yerin içindeki yükler olduğunu dirilişi inkâr edenlere verilen cevap gösterir: {ar:قَدْ عَلِمْنَا مَا تَنقُصُ ٱلْأَرْضُ مِنْهُمْ, tr:kad alimnâ mâ tenkusul-arzu minhum, gloss:yerin onlardan neyi eksilttiğini biliyoruz, source:50:4}. Âdem ile eşine yeryüzüne inerken söylenen söz de yeri hem mesken hem çıkış yeri yapar: {ar:فِيهَا تَحْيَوْنَ وَفِيهَا تَمُوتُونَ وَمِنْهَا تُخْرَجُونَ, tr:fîhâ tahyevne ve fîhâ temûtûne ve minhâ tuhracûn, gloss:orada yaşarsınız, orada ölürsünüz ve oradan çıkarılırsınız, source:7:25}. Boşalan yerin son hâli de {ar:وَتَرَى ٱلْأَرْضَ بَارِزَةً, tr:ve teral-arda bârizeten, gloss:yeri çırılçıplak, ortada görürsün, source:18:47} sözüyle verilir.

Kaynaklar: 99:1 زُلْزِلَتِ ز ل ز ل B001; 99:1 زِلْزَالَهَا ز ل ز ل B001; 99:1 ٱلْأَرْضُ ء ر ض B001; 99:1 ٱلْأَرْضُ ء ر ض B006; 99:2 وَأَخْرَجَتِ خ ر ج B001; 99:2 وَأَخْرَجَتِ خ ر ج B002; 99:2 أَثْقَالَهَا ث ق ل B002; 99:2 أَثْقَالَهَا ث ق ل B006; 99:5 أَوْحَىٰ و ح ي B006

## Konuşturulan yer: soru, gizli bildirim, haber

Üçüncü, dördüncü ve beşinci ayet üç adımlı bir konuşma kurar. İnsan sorar: {ar:مَا لَهَا, tr:mâ lehâ, gloss:ona ne oluyor, source:99:3}. Yer cevap verir: {ar:يَوْمَئِذٍ تُحَدِّثُ أَخْبَارَهَا, tr:yevmeizin tuhaddisu ahbârahâ, gloss:o gün haberlerini anlatır, source:99:4}. Cevabın kaynağı da söylenir: {ar:بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا, tr:bi-enne rabbeke evhâ lehâ, gloss:çünkü Rabbin ona vahyetmiştir, source:99:5}.

Her adımın kelimesi kendi işleyişini taşır. Haber sormak bir kelimeyle söylenir {ar:الاستخبار السؤال عن الخبر, tr:el-istihbâr es-suâlu anil-haber, gloss:istihbar haberi sormaktır, source:"خ ب ر,B001"}; insanın "ona ne oluyor" sorusu tam da dördüncü ayetin vereceği şeyi ister. Haber ise işin içyüzüdür {ar:المخبر خلاف المنظر, tr:el-mahber hilâful-manzar, gloss:iç, dış görünüşün karşıtıdır, source:"خ ب ر,B001"}. Anlatmak, kulak yoluyla ya da vahiy yoluyla insana ulaşan sözdür {ar:كل كلام يبلغ الإنسان من جهة السمع أو الوحي يقال له حديث, tr:kullu kelâmin yeblugul-insâne min cihetis-sem‘i evil-vahyi yukâlu lehû hadîs, gloss:insana duyma ya da vahiy yoluyla ulaşan her söze hadis denir, source:"ح د ث,B003"}: bu tek tanım üçüncü ayetin insanını, dördüncünün anlatmasını ve beşincinin vahyini birleştirir. Aynı kök, daha önce olmayan bir şeyin olmasını da anlatır {ar:الحدوث كون الشيء بعد أن لم يكن, tr:el-hudûs kevnuş-şey’i ba‘de en lem yekun, gloss:hudus, bir şeyin yokken var olmasıdır, source:"ح د ث,B001"}: hiç konuşmamış yer şimdi konuşur.

Vahiy, bir bilginin gizlice başkasına bırakılmasıdır {ar:إعلام في خفاء, tr:i‘lâmun fî hafâ’, gloss:gizlice bildirmek, source:"و ح ي,B001"}; işaretle {ar:الوحي الإشارة, tr:el-vahyu el-işâra, gloss:vahy, işarettir, source:"و ح ي,B002"}, gök gürültüsünün uzun ve gizli sesi gibi bir sesle {ar:وحاة الرعد وهو صوته الممدود الخفي, tr:vahâtur-ra‘d ve huve savtuhul-memdûdul-hafiyy, gloss:gök gürültüsünün uzayan gizli sesi, source:"و ح ي,B005"}, ya da taşa yazarak {ar:وحى في الحجر إذا كتب فيه, tr:vahâ fil-hacer izâ ketebe fîh, gloss:taşa yazdığında "vahâ" denir, source:"و ح ي,B003"}. Bu son anlam sahneyi somutlaştırır: yer, üzerine yazılmış bir yüzeydir ve kendisine yazılanı okur. Söz kökünün bir kullanımı da dilsiz bir şeyin hâliyle "söylemesini" kaydeder {ar:امتلأ الحوض وقال قطني, tr:imtele’el-havdu ve kâle katnî, gloss:havuz doldu ve "yeter" dedi, source:"ق و ل,B014"}; insanın sorusunda geçen fiil, dili olmadan konuşan bir şeyi de adlandırabilir. Gönderen ise {ar:رَبَّكَ, tr:rabbeke, gloss:Rabbin, source:99:5}, sözü dinlenen sahiptir {ar:يكون الرب: السيد المطاع, tr:yekûnu’r-rabb: es-seyyidu’l-mutâ‘, gloss:rab, sözü dinlenen efendidir, source:"ر ب ب,B001"}.

Sade bir anlatım "yer olanları gösterir" der; ayetler ise sessiz bir maddenin gizli bir emirle dile geldiği, insanın da dinleyen olduğu bir konuşma kurar. Kur’an yerin Rabbine kulak verişini başka bir sahnede de gösterir: içindekini atıp boşaldıktan hemen sonra yer {ar:وَأَذِنَتْ لِرَبِّهَا وَحُقَّتْ, tr:ve ezinet li-rabbihâ ve hukkat, gloss:Rabbine kulak verdi ve buna layık kılındı, source:84:5}. Yaratılışta Allah göğe ve yere seslenir, yer de cevap verir: {ar:قَالَتَآ أَتَيْنَا طَآئِعِينَ, tr:kâletâ eteynâ tâiîn, gloss:ikisi "isteyerek geldik" dediler, source:41:11}; ardından {ar:وَأَوْحَىٰ فِى كُلِّ سَمَآءٍ أَمْرَهَا, tr:ve evhâ fî kulli semâin emrehâ, gloss:her göğe işini vahyetti, source:41:12}. Surenin ikilisi bir hayvana yönelik olarak da geçer: {ar:وَأَوْحَىٰ رَبُّكَ إِلَى ٱلنَّحْلِ, tr:ve evhâ rabbuke ilen-nahl, gloss:Rabbin bal arısına vahyetti, source:16:68}. Vahyin bir konuşma türü olduğunu da Kur’an söyler: Allah insanla {ar:إِلَّا وَحْيًا أَوْ مِن وَرَآئِ حِجَابٍ, tr:illâ vahyen ev min verâi hicâb, gloss:ancak vahiyle ya da perde arkasından, source:42:51} konuşur. Allah’ın vahyine ağır söz de denir: Peygambere {ar:إِنَّا سَنُلْقِى عَلَيْكَ قَوْلًا ثَقِيلًا, tr:innâ senulkî aleyke kavlen sakîlâ, gloss:sana ağır bir söz bırakacağız, source:73:5}.

Dilsiz şeylerin konuşturulması ateş ehlinin sahnesinde açıkça kurulur. Kulakları, gözleri ve derileri onların aleyhine şahitlik eder {source:41:20}; onlar derilerine sorar, deriler cevap verir: {ar:قَالُوٓا۟ أَنطَقَنَا ٱللَّهُ ٱلَّذِىٓ أَنطَقَ كُلَّ شَىْءٍ, tr:kâlû entakanallâhullezî entaka kulle şey’, gloss:"her şeyi konuşturan Allah bizi konuşturdu" dediler, source:41:21}. Bu, üçüncü ve dördüncü ayetin soru ve cevap biçimidir. Aynı günde ağızlar mühürlenir ve eller konuşur {source:36:65}, diller, eller ve ayaklar yaptıklarına şahitlik eder {source:24:24}. Yazılı kayıt da konuşur: {ar:هَٰذَا كِتَٰبُنَا يَنطِقُ عَلَيْكُم بِٱلْحَقِّ, tr:hâzâ kitâbunâ yentıku aleykum bil-hakk, gloss:bu kitabımız aleyhinize gerçeği söyler, source:45:29}. Suçlular kitabın önünde surenin sorusunun biçimiyle sorar: {ar:مَالِ هَٰذَا ٱلْكِتَٰبِ لَا يُغَادِرُ صَغِيرَةً وَلَا كَبِيرَةً إِلَّآ أَحْصَىٰهَا, tr:mâli hâzel-kitâbi lâ yugâdiru sagîraten ve lâ kebîraten illâ ahsâhâ, gloss:bu kitaba ne oluyor, küçük büyük bırakmadan hepsini saymış, source:18:49}. Haberlerin insana ulaşması da aynı gündedir: {ar:يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍۭ بِمَا قَدَّمَ وَأَخَّرَ, tr:yunebbeul-insânu yevmeizin bimâ kaddeme ve ahhar, gloss:o gün insana öne sürdüğü ve geride bıraktığı haber verilir, source:75:13}; altüst edilen kabirlerin sahnesi de haber köküyle kapanır: {ar:إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍ لَّخَبِيرٌ, tr:inne rabbehum bihim yevmeizin le-habîr, gloss:Rableri o gün onlardan elbette haberdardır, source:100:11}. Yok edilen kavimler için söylenen {ar:وَجَعَلْنَٰهُمْ أَحَادِيثَ, tr:ve cealnâhum ehâdîs, gloss:onları anlatılan hikâyeler yaptık, source:23:44} sözü de anlatmanın ve haberin aynı şey olduğunu gösterir.

Kaynaklar: 99:3 وَقَالَ ق و ل B001; 99:3 وَقَالَ ق و ل B014; 99:4 أَخْبَارَهَا خ ب ر B001; 99:4 تُحَدِّثُ ح د ث B003; 99:4 تُحَدِّثُ ح د ث B001; 99:5 أَوْحَىٰ و ح ي B001; 99:5 أَوْحَىٰ و ح ي B002; 99:5 أَوْحَىٰ و ح ي B005; 99:5 أَوْحَىٰ و ح ي B003; 99:5 رَبَّكَ ر ب ب B001

## Toprağın, bulutun ve suyun çıkardığı bitki

Kur’an dirilişi sürekli olarak yerden bitki çıkmasına benzetir: yağmur yağar, toprak kıpırdar ve kabarır, bitki çıkarılır, "işte siz de böyle çıkarılacaksınız". Surenin kelimeleri bu dizinin parçalarını kendi anlamlarında taşır. Yer, bitkinin kök saldığı yumuşak, verimli topraktır {ar:أرض أريضة لينة طيبة, tr:arzun erîdatun leyyinetun tayyibe, gloss:yumuşak, iyi, verimli toprak, source:"ء ر ض,B002"}. Çıkma kökü yerin bitkisini yer yer çıkarmasını {ar:أرض مخرجة نبتها في مكان دون مكان, tr:arzun muharracetun nebtuhâ fî mekânin dûne mekân, gloss:bitkisi bir yerde çıkıp bir yerde çıkmayan toprak, source:"خ ر ج,B007"}, ürünü {ar:الخراج الغلة, tr:el-harâcu el-galle, gloss:harac üründür, source:"خ ر ج,B003"} ve bulutun ilk belirişini {source:"خ ر ج,B005"} adlandırır. Haber kökü yağmur suyunu toplayan alçak, yumuşak toprağı {ar:الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء, tr:el-habrâ’ el-arzus-sehletul-munhafidatu yecteme‘u fîhâ mâus-semâ’, gloss:gök suyunun toplandığı alçak, düz toprak, source:"خ ب ر,B002"}, çiftçiyi ve yerden çıkanın bir kısmı karşılığında ortakçılığı {ar:المزارعة ببعض ما يخرج من الأرض, tr:el-muzâraa bi-ba‘dı mâ yahrucu minel-arz, gloss:yerden çıkanın bir kısmı karşılığında ortakçılık, source:"خ ب ر,B003"} ve körpe bitkiyi {source:"خ ب ر,B005"} adlandırır. Rab kökü üst üste binmiş bulutu, bitkiyi büyüttüğü için verilen adla anar {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb: es-sehâb, summiye bi-zâlike li-ennehû yerubbun-nebât, gloss:rabâb buluttur, bitkiyi büyüttüğü için böyle adlandırılmıştır, source:"ر ب ب,B008"}; terbiye de bir şeyi hâlden hâle tamamlanmaya kadar yetiştirmektir {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâuş-şey’i hâlen fe-hâlen ilâ haddit-temâm, gloss:terbiye, bir şeyi hâlden hâle tamamına kadar geliştirmektir, source:"ر ب ب,B002"}; çok ve toplanmış su da bu köktendir {source:"ر ب ب,B013"}. Zerre kökü de toprağı yarıp çıkan filizi adlandırır {ar:ذر البقل إذا طلع من الأرض, tr:zerral-baklu izâ tala‘a minel-arz, gloss:sebze yerden baş verdiğinde "zerra" denir, source:"ذ ر ر,B004"}.

Bu imgede birinci ve ikinci ayetin yeri bir tarladır; çıkarması onun ürünüdür. Beşinci ayetteki Rab, kelimenin anlamında efendi ve sahiptir; yanında, bitkiyi aşama aşama büyüten bulutun adı da duyulur. Diriliş korkunç bir yıkım olduğu kadar tanıdık bir yetişmedir.

Kur’an üç imgeyi tek ayette birleştirir: rüzgârlar {ar:حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًا ثِقَالًا سُقْنَٰهُ لِبَلَدٍ مَّيِّتٍ فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ, tr:hattâ izâ ekallet sehâben sikâlen suknâhu li-beledin meyyitin fe-enzelnâ bihil-mâe fe-ahracnâ bihî min kullis-semerât, kezâlike nuhricul-mevtâ, gloss:ağır bulutları yüklendiklerinde onu ölü bir beldeye süreriz, oraya suyu indirir, onunla her türlü meyveyi çıkarırız; ölüleri de böyle çıkarırız, source:7:57}. Ağır bulut, çıkarılan meyve ve çıkarılan ölüler burada yan yanadır. Dirilişten şüphe edenlere gösterilen yer önce kupkurudur, su inince {ar:ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ, tr:ihtezzet ve rabet ve enbetet, gloss:titredi, kabardı ve bitirdi, source:22:5}; aynı söz Allah’ın ayetleri arasında da geçer ve {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰ, tr:innellezî ahyâhâ le-muhyil-mevtâ, gloss:onu dirilten elbette ölüleri de diriltir, source:41:39} sözüyle tamamlanır. Bulut sürülür ve yer diriltilir: {ar:كَذَٰلِكَ ٱلنُّشُورُ, tr:kezâliken-nuşûr, gloss:diriliş de böyledir, source:35:9}; dirilişi inkâr edenlere verilen cevapta {ar:كَذَٰلِكَ ٱلْخُرُوجُ, tr:kezâlikel-hurûc, gloss:çıkış da böyledir, source:50:11}; ve {ar:كَذَٰلِكَ تُخْرَجُونَ, tr:kezâlike tuhracûn, gloss:siz de böyle çıkarılırsınız, source:43:11}, {source:30:19}. Çıkarma fiili bitki için tekrar tekrar kullanılır {source:6:99}; yer de kendi suyunu ve otlağını verir {ar:أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا, tr:ahrace minhâ mâehâ ve mer‘âhâ, gloss:ondan suyunu ve otlağını çıkardı, source:79:31}; Rabbin övüldüğü surede de {ar:وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ, tr:vellezî ahracel-mer‘â, gloss:otlağı çıkaran, source:87:4} denir. Nuh da insanları yerin bitkisi olarak anar: {ar:وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًا, tr:vallâhu enbetekum minel-ardı nebâtâ, gloss:Allah sizi yerden bir bitki gibi bitirdi, source:71:17}.

Kaynaklar: 99:1 ٱلْأَرْضُ ء ر ض B002; 99:2 وَأَخْرَجَتِ خ ر ج B007; 99:2 وَأَخْرَجَتِ خ ر ج B003; 99:2 وَأَخْرَجَتِ خ ر ج B005; 99:4 أَخْبَارَهَا خ ب ر B002; 99:4 أَخْبَارَهَا خ ب ر B003; 99:4 أَخْبَارَهَا خ ب ر B005; 99:5 رَبَّكَ ر ب ب B008; 99:5 رَبَّكَ ر ب ب B002; 99:5 رَبَّكَ ر ب ب B013; 99:7 ذَرَّةٍ ذ ر ر B004

## Buluşmalar

Surenin hareketi bir yönden ötekine geçer: içeriden dışarıya, ağırdan hafife, büyükten küçüğe, sessizden konuşana, gizliden görünene. İmgeler bu hareketin farklı yüzlerini taşır ve birkaç sahnede üst üste biner.

İlk buluşma yerin boşalmasıyla doğumdur. İkinci ayetin iki kelimesi, {ar:وَأَخْرَجَتِ, tr:ve ahracet, gloss:ve çıkardı, source:99:2} ile {ar:أَثْقَالَهَا, tr:eskâlehâ, gloss:ağırlıkları, source:99:2}, hem gömülü yükü atan yeri hem doğuran bedeni anlatır. Kur’an bu iki sahneyi aynı ayetlerde tutar: Saatin sarsıntısı {source:22:1} ve her gebenin yükünü bırakması {source:22:2}; rahimden çocuğu çıkarmak ve suyla titreyip kabaran toprak {source:22:5}. Aynı ayet bitki imgesini de içerir; böylece boşalan yer, doğuran beden ve filiz veren tarla tek bir dirilişin üç görünüşü olur. Ağır bulutlarla meyveyi ve ölüleri çıkaran ayet {source:7:57} ağırlık imgesini de bu sahneye bağlar.

İkinci buluşma boşalan yerle konuşan yerdir. İnşikak suresinde sıra surenin sırasıyla aynıdır: yer içindekini atar ve boşalır {source:84:4}, sonra Rabbine kulak verir {source:84:5}. İkinci ayette yer yükünü çıkarır, beşinci ayette Rabbinin vahyini alır. Arada üçüncü ayetin sarsılmış insanı vardır: sarsıntı bedenine geçmiş, ağzından {ar:مَا لَهَا, tr:mâ lehâ, gloss:ona ne oluyor, source:99:3} sorusu çıkmıştır. Bu soru, sarsıntı imgesini konuşma imgesine bağlar; çünkü yer ona cevap verecektir. Suçluların kitabın önündeki sorusu {source:18:49} aynı biçimdedir ve ardından yaptıklarını hazır bulurlar: soru, haber ve görme bir sahnede toplanır.

Üçüncü buluşma konuşmayla göstermedir. Dördüncü ayette yerin anlattığı haber, işin içyüzüdür; anlatmak açığa vurmak, kılıcı parlatmaktır. Yerin içindekilerini çıkarması ile haberlerini anlatması aynı işlemdir: içeride olanın dışarı verilmesi. Kur’an bu iki çıkarışı yan yana koyar: kabirlerdeki altüst edilir ve göğüslerdeki ortaya dökülür {source:100:9}, {source:100:10}; kıyamet günü kitap çıkarılır ve açılmış bulunur {source:17:13}.

Dördüncü buluşma altıncı ayetin kendisidir. Sudan dönen kalabalık bir yöne yürür ve ayet varış yerini söyler: {ar:لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:li-yurav a‘mâlehum, gloss:amelleri kendilerine gösterilsin diye, source:99:6}. Yolun sonunda tutulan ayna vardır. Aynı kalabalık bölüklere serpilir ve zerre imgesi başlar; bölükler arasındaki uzaklık da iki payın imgesini açar. Bir kelime, {ar:أَشْتَاتًا, tr:eştâtâ, gloss:bölük bölük, source:99:6}, üç imgeyi birden taşır: sudan dönüş, serpilme ve ak ile kara kadar uzak iki pay.

Son buluşma zerrede olur. {ar:ذَرَّةٍ, tr:zerratin, gloss:zerre, source:99:8} hem serpilmenin en küçük birimidir hem terazideki en küçük ağırlık; kötülük sözünün yanında ateşten kopan kıvılcım, toprağı yarıp çıkan filiz ve güneşte yayılan ince ışık da duyulur. Ağırlık kökü burada çemberi kapatır: sure yerin bütün ağırlıklarıyla açılmış, aynı kökten bir miskalle biter. Lokman’ın oğluna söylediği söz {source:31:16} bu iki ucu birleştirir: yerin içinde gizli bir küçük ağırlık getirilir ve sözü {ar:إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌ, tr:innallâhe latîfun habîr, gloss:Allah en ince şeyi bilen, her şeyden haberdardır, source:31:16} diye biter. Haber kökü burada da durur: yerin anlattığı haberler, her şeyden haberdar olanın bildiğidir. Yer ağırlıklarını verir, haberlerini anlatır; insan da tek tek, en küçük ağırlığına kadar amelini görür.

