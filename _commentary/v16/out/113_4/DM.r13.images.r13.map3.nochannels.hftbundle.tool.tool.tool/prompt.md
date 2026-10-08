Focus: 113:4. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/113_4/D.r13/context.md =====
# 113:4 — focus

وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ

Anchor translation (canonical reading, reference only):

ve düğümlere üfleyenlerin kötülüğünden;

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَمِن | مِن |  | CONJ;P |
| 2 | شَرِّ | شَرّ | ش ر ر | N |
| 3 | ٱلنَّفَّٰثَٰتِ | نَّفَّٰثَٰت | ن ف ث | DET;N |
| 4 | فِى | فِى |  | P |
| 5 | ٱلْعُقَدِ | عُقْدَة | ع ق د | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 113 — full text (context; no pericope)

- 113:1 قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ
- 113:2 مِن شَرِّ مَا خَلَقَ
- 113:3 وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ
- 113:4 ◀ focus وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ
- 113:5 وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ


===== _commentary/v16/work/113_4/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ش ر ر (root_000787) — identity root of شَرِّ (w2)

- **B001** iyinin karşıtı olan kötülük — kötülük; iyinin karşıtı · kötülük etme veya kötü olma durumu · kötülüğü çok olan adam · kötü kimseler · birini kötülüğe bağladı; onu kötü saydı · kusur veya hoş karşılanmayan şey
  الشَّرّ خلاف الخير (maqayis;jamhara)؛ الشر السوء (ayn)؛ الشر نقيض الخير (sihah)؛ الشر الذي يرغب عنه الكل (mufradat)؛ رجل شرير كثير الشر (maqayis;jamhara;sihah;mufradat)؛ أشررت فلانا إذا نسبته إلى الشر (maqayis;sihah;mufradat)؛ الشُّرّ العيب (sihah)؛ الشر بالضم خص بالمكروه (mufradat)
- **B002** güneşe serip kurutmak — güneşe serip kuruttu · güneşte kuruması için serdi · kurutulacak şeylerin serildiği yaygı · süt ürünü veya tahıl kurutma yaygısı · kurutma yaygıları veya kurutulmuş et parçaları
  الشر بسطك الشيء في الشمس (maqayis;ayn)؛ شررت اللحم والثوب وأشررته إذا بسطته ليجف (jamhara)؛ شررت الثوب بسطته في الشمس (sihah)؛ شررت الأقط أشره إذا جعلته على خصفة ليجف (sihah)؛ الإشرارة ما يبسط عليه الشيء (maqayis)؛ الإشرار ما يبسط عليه الأقط والبر ليجف (ayn)؛ الأشارير قطع قديد (sihah)
- **B003** kıvılcım — ateşten sıçrayan kıvılcımlar · kıvılcımlar topluluğu · tek kıvılcım · tek kıvılcım
  الشرارة والجمع الشرار (maqayis)؛ الشرر ما تطاير من النار الواحدة شررة (maqayis)؛ الشرارة والشرر ما تطاير من النار (ayn)؛ شرار النار فيقال شررة وشرارة (jamhara)؛ الشرارة واحدة الشرار وهو ما يتطاير من النار وكذلك الشرر (sihah)؛ شرار النار ما تطاير منها (mufradat)
- **B004** kesip parçalamak — bir şeyi kesip yardı · kesip parçalama; ısırılan şeyi ağızdan silkeleyip çıkarma
  شرشر الشيء إذا قطعه (maqayis)؛ الشرشرة أن تنفض الشيء من فيك بعد عضك إياه (maqayis)؛ شرشره أي قطع شراشره (ayn)؛ شرشرة الشيء تشقيقه وتقطيعه (sihah)
- **B005** yağı damlayan pişmiş et [kalıp] — yağı damlayan pişmiş et · yağı damlayan pişmiş et
  الشواء الشرشار الذي يتقاطر دسمه (maqayis)؛ شواء شرشر يتقاطر دسمه (sihah)
- **B006** kuyrukların sarkan uçları veya ağırlıklar — kuyrukların sarkan ve salınan uçları · ağırlıklar
  شراشر الأذناب ذباذبها (maqayis;sihah)؛ الشراشر الأثقال الواحدة شرشرة (sihah)
- **B007** kendini bütün isteğiyle vermek — kendini, isteğini ve bütün ilgisini ona verdi
  ألقى عليه شراشره إذا ألقى عليه نفسه حرصا ومحبة (maqayis)؛ ألقى علي شراشره أي ألقى علي نفسه حرصا (ayn)؛ ألقى عليه شراشره أي نفسه حرصا ومحبة (sihah)؛ جمع ما انتشر من هممه لهذا الشيء وشغل همومه كلها به (maqayis)
- **B008** görünür kılmak — 
  أشررت الشيء إذا أبرزته وأظهرته (maqayis)؛ أشررت الشيء أظهرته (sihah)؛ يحتمل أنها نسبت الأصابع إلى الشر بالإشارة إليه (mufradat)
- **B009** yüz çevresinde dolaşan ısırmayan sivrisinek benzeri böcek — yüz çevresinde dolaşan, ısırmayan sivrisinek benzeri böcekler · bu türden tek böcek
  الشران شيء تسميه العرب الأذى شبه البعوض يغشى وجه الإنسان لا يعض الواحدة شرانة (ayn)؛ الشران شبيه بالبعوض يغشى وجه الإنسان ولا يعض وربما سموه الأذى (sihah)
- **B010** gençlik canlılığı ve atılganlığı [kalıp] — gençliğin canlılığı, güçlü isteği ve atılganlığı
  شرة الشباب نشاطه ولهذا باب تراه (jamhara)؛ شرة الشباب حرصه ونشاطه (sihah)
- **B011** çekişme — çekişme; ağız dalaşı
  المشارة المخاصمة (sihah)
- **B012** adı belirtilen bir bitki — kaynakta adı verilen bir bitki
  الشرشر نبت يقال له الشرشر بالكسر (sihah)

## ن ف ث (root_001527) — identity root of ٱلنَّفَّٰثَٰتِ (w3)

- **B001** ağızdan, çoğu kez az tükürükle, hafifçe püskürtüp çıkarma — ağızdan az tükürükle hafifçe püskürtme · okuyup üfleyen kişinin az tükürükle püskürtmesi · büyücü kadınların düğümlere üflemesi · yılanın zehrini ağzından püskürtmesi · ağızdan ya da diş aralarından püskürülüp atılan diş temizleme çubuğu artığı
  نفث الراقي ريقه وهو أقل من التفل (maqayis;jamhara)؛ النفث شبيه بالنفخ وهو أقل من التفل (sihah;tahdhib)؛ قذف الريق القليل (mufradat)؛ السواحر والنفاثات في العقد (jamhara;sihah;tahdhib;mufradat)؛ الحية تنفث السم (jamhara;sihah;mufradat)؛ نفاثة السواك ما بقي في الأسنان فينفثه (maqayis;jamhara;sihah;tahdhib;mufradat)
- **B002** yaranın dışarı çıkardığı kan [kalıp] — yaranın dışarı çıkardığı kan
  دم نفيث نفثه الجرح أي أظهره (maqayis)؛ دم نفيث إذا نفثه الجرح أي أظهره (jamhara)؛ دم نفيث إذا نفثه الجرح (sihah)؛ دم نفيث نفثه الجرح (mufradat)
- **B003** içte birikenin sonunda dışa vurulması [kalıp] — İçinde biriken kişi onu sonunda dışa vurur.
  لا بد للمصدور أن ينفث (maqayis;jamhara;sihah;mufradat)
- **B004** içine doğmak [kalıp] — içime doğdu; bana esinlendi
  نفث في روعي أي أوحى إلي (tahdhib)
- **B005** şiir — şiir; ağızdan çıkarılan söz ürünü
  النفث فتفسيره في الحديث أنه الشعر (tahdhib)؛ سمي الشعر نفثا لأنه كالشيء ينفثه الإنسان من فيه مثل الرقية (tahdhib)

## ع ق د (root_001034) — identity root of ٱلْعُقَدِ (w5)

- **B001** uçları birleştirip düğümleme — ipi düğümleyip bağlamak · yapıda kemer oluşturmak · düğüm yeri veya üzerine düğüm atılan nokta · dizideki düğüm yerleri · gerdanlık
  عقد البناء والجمع أعقاد وعقود (maqayis)؛ عقدت الحبل أعقده عقدا وقد انعقد (maqayis)؛ عقدت الحبل عقدا ونحوه فانعقد (ayn)؛ عقدت الحبل والبيع والعهد فانعقد (sihah)؛ عقدت الحبل فهو معقود (tahdhib)؛ العقد الجمع بين أطراف الشيء (mufradat)؛ عقد القلادة ما يكون طوار العنق (maqayis;ayn)؛ المعاقد مواضع العقد من النظام (maqayis;ayn;tahdhib)
- **B002** bağlayıcı bir söz veya işlemi kesinleştirme — andı bağlayıcı biçimde kesinleştirmek · bağlayıcı sözler ve yükümlülükler · karşılıklı bağlayıcı söz vermek · evlilik bağını kurup kesinleştirme · satışı bağlayıcı kılıp kesinleştirme
  عاقدته مثل عاهدته وهو العقد والجمع عقود (maqayis)؛ العقد عقد اليمين (maqayis)؛ عقدة النكاح وكل شيء وجوبه وإبرامه (maqayis)؛ عقدة البيع إيجابه (maqayis)؛ عقد اليمين أن يحلف يمينا لا لغو فيها (ayn)؛ عقدة النكاح وجوبه وعقدة البيع وجوبه (ayn)؛ المعاقدة المعاهدة (sihah)؛ العقود العهود وهي أوكد العهود (tahdhib)؛ عقد فلان اليمين إذا وكدها (tahdhib)؛ يستعار ذلك للمعاني نحو عقد البيع والعهد (mufradat)؛ العقدة اسم لما يعقد من نكاح أو يمين أو غيرهما (mufradat)
- **B003** koyulaşıp katılaşma — balı koyulaştırmak · koyulaşıp katılaşmış bal · balla koyulaştırılan yemek · katılaşıp sertleşmek
  أعقدت العسل وانعقد وعسل عقيد ومنعقد (maqayis)؛ اعتقد الشيء صلب (maqayis;ayn)؛ عقد الكرم إذا رأيت عوده قد يبس ماؤه وانتهى (maqayis)؛ أعقدت العسل فانعقد (ayn)؛ اليعقيد طعام يعقد بالعسل (ayn;tahdhib)؛ عقد الرب وغيره أي غلظ فهو عقيد (sihah)؛ أعقدت العسل ونحوه فهو معقد وعقيد (tahdhib)؛ عسل عقيد وكذلك عقيد عصير العنب (tahdhib)
- **B004** mal veya taşınmaz edinip elde tutma — mal biriktirip edinmek · edinilmiş mülk veya taşınmaz
  العقدة الضيعة والجمع عقد (maqayis;ayn)؛ اعتقد فلان عقدة أي اتخذها (maqayis)؛ اعتقد مالا وأخا أي اقتناه (maqayis)؛ اعتقدت مالا جمعته (ayn)؛ اعتقد ضيعة ومالا أي اقتناها (sihah)؛ كل ما يعتقده الإنسان من العقار فهو عقدة له (tahdhib)
- **B005** sık ve köklü ağaçlık ya da otlak [kalıp] — sık, köklü ve hayvanları beslemeye yeterli ağaçlık alan · bitkisi kesintisiz biçimde birleşmiş çayırlık
  العقدة من الشجر ما يكفي المال سنته (maqayis)؛ العقدة من الشجر ما اجتمع وثبت أصله (maqayis)؛ المكان الذي يكثر شجره عقدة (maqayis)؛ العقدة المكان الكثير الشجر أو النخل (sihah)؛ العقدة من الأرض البقعة الكثيرة الشجر (tahdhib)؛ في أرض بني فلان عقدة تكفيهم سنتهم (tahdhib)؛ روضة عقدة إذا اتصل نبتها (tahdhib)؛ العقدة من المرعى هي الجنبة (tahdhib)
- **B006** bir düşünceye gönülden bağlanıp onda kararlı kalma — bir şeye gönülden bağlanıp vazgeçmemek · dostluk ve sevginin yerleşmesi · gönülde yerleşmiş inanç
  عقد قلبه على كذا فلا ينزع عنه (maqayis)؛ اعتقد الإخاء ثبت (maqayis)؛ عقد قلبه على شيء لم ينزع عنه (ayn)؛ اعتقد الإخاء والمودة بينهما أي ثبت (ayn)؛ اعتقد كذا بقلبه (sihah)؛ ليس له معقود أي عقد رأى (sihah)؛ منه قيل لفلان عقيدة (mufradat)
- **B007** konuşmanın tutulması veya anlaşılmaz duruma gelmesi [kalıp] — dil tutulması veya konuşma tutukluğu · konuşması tutuk erkek · kapalı ve güç anlaşılır söz
  عقد الرجل إذا كانت في لسانه عقدة فهو أعقد (maqayis)؛ عقد فلان كلامه إذا عماه وأعوصه (maqayis)؛ رجل أعقد وقد عقد يعقد عقدا أي في لسانه عقدة (ayn)؛ رجل أعقد وعقد للذي في لسانه عقدة (sihah)؛ كلام معقد أي مغمض (sihah)؛ رجل أعقد إذا كان في لسانه رتج (tahdhib)؛ عقد لسانه احتبس وبلسانه عقدة أي في كلامه حبسة (mufradat)
- **B008** kumun yığılıp sıkışması veya bulutun düğüm gibi kümelenmesi [kalıp] — yığılmış veya yağmurla nemlenip sıkışmış kum · bulutun yapı kemeri gibi kümelenmesi
  عقد الرمل ما تراكم واجتمع والجمع أعقاد (maqayis;ayn)؛ أعطش من عقد الرمل وأشرب من عقد الرمل (maqayis)؛ تعقد السحاب إذا صار كأنه عقد مضروب مبني (ayn;maqayis)؛ العقد ما تعقد من الرمل أي تراكم (sihah)؛ تعقد الرمل والخيط وغيرهما (sihah)؛ العقدة من الرمل المتعقد بعضه على بعض (tahdhib)؛ العقد ترطب الرمل من كثرة المطر (tahdhib)
- **B009** üzüm salkımı — üzüm salkımı · üzüm salkımı adının bir söyleyiş biçimi
  العنقود معروف وهو من العقد كأنه شيء عقد بعضه ببعض (maqayis)؛ العنقود واحد عناقيد العنب والعنقاد لغة فيه (sihah)
- **B010** hayvanda kıvrık uzuv görünümü ve buna bağlı özel durumlar — kuyruğunu düğümleyerek gebeliğini belli eden dişi deve · boynunu büken veya kuyruk ucunu kıvıran dişi ceylan · boynuzu ya da kuyruğu kıvrık teke veya ceylan · köpeklerin çiftleşmesi · çiftleşme sırasında ucu şişen köpek penisi
  ناقة عاقد إذا عقدت (maqayis)؛ ظبية عاقد إذا كانت تلوى عنقها (maqayis)؛ الأعقد من التيوس والظباء الذي في قرنه عقدة أو عقد (maqayis)؛ تعاقدت الكلاب إذا تعاظلت (maqayis)؛ ظبية عاقد تعقد طرف ذنبها (ayn)؛ الأعقد من التيوس والظباء الذي في قرنه عقدة (ayn)؛ العقداء من الشاء التي ذنبها كأنه معقود (sihah)؛ العاقد الناقة التي قد أقرت باللقاح (sihah)؛ تيس وكلب أعقد ملتوي الذنب وتعاقدت الكلاب تعاظلت (mufradat)؛ الذنب الأعقد المعوج (tahdhib)؛ العاقد من الظباء الذي ثنى عنقه (tahdhib)؛ عقدت فم الرحم على الماء (tahdhib)
- **B011** sağlam ve toplu beden yapısı [kalıp] — sırtı sağlam dişi deve · sağlam yapılı ya da kısa ve işe dayanıklı erkek deve
  ناقة معقودة القرى أي موثقة الظهر (maqayis)؛ جمل عقد أي ممر الخلق (maqayis)؛ للقصير أعقد لأنه كأنه عقدة والعقد القصار (maqayis)؛ ناقة معقودة القرا موثقة الظهر وجمل عقد (sihah)؛ ناقة معقودة القرا إذا كانت وثيقة الظهر (tahdhib)؛ العقد الجمل القصير الصبور على العمل (tahdhib)
- **B012** öfkenin düğümlenmesi ve çözülmesiyle anlatılan huy durumu [kalıp] — öfkesi yatışmak · öfkelenip kötülüğe hazırlanmak · geçimsiz ve yumuşak huylu olmayan alçak kişi
  للرجل قد تحللت عقده إذا سكن غضبه (maqayis)؛ عقد ناصيته إذا غضب فتهيأ للشر (maqayis)؛ لئيم أعقد إذا لم يكن سهل الخلق (maqayis)؛ إذا سكن غضبه قد تحللت عقده (sihah)؛ عقد فلان ناصيته إذا غضب وتهيأ للشر (tahdhib)
- **B013** düğüme bağlanan büyü uygulaması — ipliklere düğüm atıp üfleyen büyücü kadınlar · düğüm büyüsü yapan büyücü
  المعقد الساحر (maqayis)؛ يعقد سحر البابليين طرفها (maqayis)؛ النفاثات في العقد من السواحر اللواتي يعقدن في الخيوط (maqayis)؛ النفاثات في العقد جمع عقدة وهي ما تعقده الساحرة (mufradat)؛ أصله من العزيمة ولذلك يقال لها عزيمة كما يقال لها عقدة (mufradat)؛ قيل للساحر معقد (mufradat)
- **B014** parmakları bükerek sayma [kalıp] — parmak eklemlerini bükerek saymak
  الحاسب يعقد بأصابعه إذا حسب (tahdhib)
- **B015** kuşak düğümü kadar yakın [kalıp] — kuşak düğümü kadar yakın, çok yakın konumda
  هو مني معقد الإزار يراد به قرب المنزلة (sihah)
- **B016** yer çevresi, yapı örtüşmesi veya üzerine kapanma — kuyunun çevresindeki koruma alanı · kuyu duvar örgüsünün alttan dışa, üstten içe taşması · vadinin topluluğun üzerine kapanıp onları yok etmesi
  إذا أطبق الوادي على قوم فأهلكهم عقد عليهم (maqayis)؛ العاقد حريم البئر وما حوله (sihah)؛ التعقد في البئر أن يخرج أسفل الطي ويدخل أعلاه إلى جراب البئر (tahdhib)
- **B017** boynunu yöneltip birine sığınma [kalıp] — birine sığınmak
  عقد فلان عنقه إلى فلان وعكدها إذا لجأ إليه (tahdhib)

## ECHO ش ر ي (root_000792) — for شَرِّ (w2): withheld observed target; not identity

- **B001** bedel karşılığında alıp satma — satmak veya bedelini verip almak · satın almak · alış ve satış
  شريت الشيء واشتريته إذا أخذته من صاحبه بثمنه (maqayis); شرى يشري شرى وشراء وهو شار إذا باع (ayn); شريت الشيء إذا بعته وإذا اشتريته أيضا (sihah); الشراء والبيع يتلازمان (mufradat); شريت بمعنى بعت وشريت أي اشتريت (tahdhib)
- **B002** eş ve denk — benzeri ve dengi · eş ve benzer
  هذا شروى هذا أي مثله (maqayis); شرواها أي مثلها (maqayis); شروى الشيء مثله (sihah); هذا شرواه وشرية أي مثله (tahdhib)
- **B003** bir şeyin yanları ve uçları [kalıp] — bir şeyin yanları ve uçları · büyük nehrin yanı
  أشراء الشيء نواحيه الواحد شرى (maqayis); أشراء الحرم نواحيه الواحد شرى (sihah); أشراء الحرم نواحيه وشرى الفرات ناحيته (tahdhib)
- **B004** acı elma bitkisi veya çekirdekten yetişen palmiye — acı elma bitkisi veya bu bitkinin topluluğu · çekirdekten yetişen palmiye ağacı
  الشَّرى يقال إنه الحنظل (maqayis); الشرية النخلة التي تنبت من النواة (maqayis); الشري بالتسكين الحنظل (sihah); الشرى أيضا شجر الحنظل (sihah); الحنظل هو الشري واحدته شرية (tahdhib)
- **B005** çalılık ve aslanlarıyla tanınan yer — çalılığı ve aslanı bol yer veya yol · çalılık bölgenin aslanları
  الشرى موضع كثير الدغل والأسد (maqayis); الشرى طريق في سلمى كثير الأسد (sihah); ما هم إلا أسود الشرى (tahdhib); شرى مأسدة بعينها وبه غياض وآجام (tahdhib)
- **B006** yaylık ağaç veya atardamar — yay yapımında kullanılan ağaç veya odun · atan veya ince beden damarları
  الشريان من شجر القسى (maqayis); الشريان شجر يتخذ منه القسى (sihah); الشريان واحد الشرايين وهي العروق النابضة (sihah); الشريان من الشجر الذي يتخذ منه القسي (tahdhib); الشريانات عروق رقاق في جسد الإنسان (tahdhib)
- **B007** şimşeğin yayılıp art arda parlaması [kalıp] — şimşek buluta yayıldı veya art arda parladı · şimşek art arda parladı
  شرى البرق إذا استطار (maqayis); شري البرق في السحاب يشرى شرى إذا تفرق فيه (ayn); شرى البرق إذا كثر لمعانه (sihah); شري البرق إذا تفرق في وجه الغيم (tahdhib); شري البرق إذا تتابع لمعانه واستشرى مثله (tahdhib)
- **B008** taşkın biçimde sürme, yinelenme veya büyüme — öfkesinden çılgına döndü · bir işte inatla diretti ve ileri gitti · karşılıklı inatlaşma ve çekişme · yolunda hızlandı veya durmadan ilerledi · dişi devenin dizgini durmadan çırpındı · gözyaşları durmadan aktı · aralarındaki işler büyüyüp ağırlaştı
  شرى الرجل إذا استطير غضبا (maqayis); شرى البعير في سيره إذا أسرع (maqayis); استشرى الرجل إذا لج في الأمر (maqayis); شرى زمام الناقة إذا كثر اضطرابه (maqayis); شري فلان غضبا إذا استطار غضبا (sihah); استشرى أي لج في سننه (sihah); استشرى فلان في الغي إذا لج فيه (tahdhib); المشاراة الملاجة (tahdhib); شريت عينه بالدمع أي لجت وتابعت الهملان (tahdhib); استشرت أمور بينهم تفاقمت وعظمت (tahdhib); أشريته به فشري مثل أغريته به فغري (tahdhib)
- **B009** yakıcı küçük kırmızı deri kabarcıkları — yakıcı küçük kırmızı deri kabarcıklarıyla görülen hastalık · derisinde yakıcı küçük kabarcıklar çıktı
  شري جلده من الشرى وهي خراج صغار لها لذع شديد (sihah); الشري داء يأخذ في الرجل أحمر كهيئة الدراهم (tahdhib); شرى جلده شرى وهو شر (tahdhib)
- **B010** havuzu veya yemek kabını doldurmak [kalıp] — havuzu veya büyük yemek kabını doldurmak
  أشريت الحوض وأشريت الجفنة إذا ملأتهما (sihah); أشرى حوضه ملأه وأشرى جفانه إذا ملأها للضيفان (tahdhib)
- **B011** kendini Tanrı uğruna sattığını söyleyen topluluk — kendilerini Tanrı uğruna sattıklarını söyleyen ayrılıkçı topluluk · bu topluluğun bir üyesi · bu topluluğa katılmak
  الشراة الخوارج الواحد شار سموا بذلك لقولهم إنا شرينا أنفسنا في طاعة الله (sihah); الشراة الخوارج سموا أنفسهم شراة لأنهم أرادوا أنهم باعوا أنفسهم لله (tahdhib); يسمى الخوارج بالشراة متأولين فيه ومن الناس من يشري نفسه (mufradat)
- **B012** Tanrı seni sıkıntıya ve aşağılanmaya uğratsın [kalıp] — Tanrı seni sıkıntıya ve aşağılanmaya uğratsın
  لحاه الله وشراه (tahdhib); شراه الله وعظاه وأورمه وأرغمه (tahdhib)

===== _commentary/v16/out/s113/images.r13.map3.nochannels.hftbundle.tool.tool/images.md (only the images that cite 113:4, and ## Buluşmalar) =====
## Bulut, yağmur ve kaya çukuru

Surenin kelimeleri, kök ailelerinden dinlendiğinde, bulutla başlayıp kayadaki bir çukurla biten bütün bir yağmur sahnesini taşır. Rab kelimesinin kökü alçakta asılı duran bulutun adıdır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb, summiye bi-zâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi büyüttüğü için bu adı almıştır, source:"ر ب ب,B008"}; büyük bulutun altında sarkan, ak ya da kara bir buluttur bu: {ar:السحاب المتعلق دون السحاب يكون أبيض ويكون أسود, tr:es-sehâbu'l-muteallaku dûne's-sehâb yekûnu ebyada ve yekûnu esved, gloss:bulutun altında asılı duran bulut; ak da olur kara da, source:"ر ب ب,B008"}. Bulut yerinde durur: {ar:أربت السحابة: دامت, tr:erabbeti's-sehâbe: dâmet, gloss:bulut kalıcı oldu, source:"ر ب ب,B007"}. Halk kökü onun düzgünce yayılışını adlandırır: {ar:اخلولق السحاب استوى, tr:iḣlevlaka's-sehâbu'stevâ, gloss:bulut düzgünce yayıldı, source:"خ ل ق,B008"}. Ukad kökü yığılışını: {ar:تعقد السحاب إذا صار كأنه عقد مضروب مبني, tr:teakkade's-sehâbu izâ sâra ke-ennehû akdun madrûbun mebnî, gloss:bulut, kurulmuş bir kemer gibi olduğunda "teakkade" denir, source:"ع ق د,B008"}. Sonra felak kökü bulutun yağmurla yarılmasını söyler: {ar:فلق الأرض بالنبات والسحاب بالمطر, tr:felaka'l-arda bi'n-nebâti ve's-sehâbe bi'l-matar, gloss:toprağı bitkiyle, bulutu yağmurla yardı, source:"ف ل ق,B003"}. Gök çiseler ve gāsık "akan" olur: {ar:غسقت السماء أرشت, tr:ğasakati's-semâu erasşet, gloss:gök çiseledi, source:"غ س ق,B004"}, {ar:الغاسق بمعنى السائل, tr:el-ğāsiku bi-ma'ne's-sâil, gloss:gāsık, akan anlamındadır, source:"غ س ق,B004"}.

Su aşağı iner. Felak kökü iki tepe arasındaki alçak yerin de adıdır: {ar:الفلق المطمئن من الأرض بين الربوتين, tr:el-felaku'l-mutmainnu mine'l-ardı beyne'r-rabveteyn, gloss:felak, iki tümsek arasındaki çukur yerdir, source:"ف ل ق,B004"}. Su orada toplanır, dağdaki bir oyuğa dolar: {ar:الوقب في الجبل نقرة يجتمع فيها الماء, tr:el-vakbu fi'l-cebel nukratun yectemiu fîhe'l-mâ', gloss:vakb, dağda suyun toplandığı oyuktur, source:"و ق ب,B001"}. Vekab fiili de bu oyuğa girmektir: {ar:وقب الشيء دخل في وقبة, tr:vekabe'ş-şey'u dehale fî vakbe, gloss:şey bir oyuğa girdi, source:"و ق ب,B002"}. İkinci ayetin halk kökü aynı oyuğu neredeyse aynı sözle adlandırır: {ar:الخليقة نقر في صخرة يجتمع فيه ماء السماء, tr:el-ḣalîka nakrun fî sahratin yectemiu fîhi mâu's-semâ', gloss:halîka, kayada gök suyunun toplandığı oyuktur, source:"خ ل ق,B011"}; o oyukların bulunduğu kaya da bu kökle düzdür: {ar:صخرة خلقاء أي ملساء, tr:sahratun ḣalkâ' ey melsâ', gloss:halkâ kaya, yani pürüzsüz kaya, source:"خ ل ق,B008"}. Rab kökü toplanan bol suyun adıdır: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabab ve huve'l-mâu'l-kesîr, summiye bi-zâlike li-ictimâih, gloss:rabab bol sudur; toplandığı için bu adı almıştır, source:"ر ب ب,B013"}. Sahnenin sonunda bir ters dönüş de vardır: {ar:إذا أطبق الوادي على قوم فأهلكهم عقد عليهم, tr:izâ etbaka'l-vâdî alâ kavmin fe-ehlekehum akade aleyhim, gloss:vadi bir topluluğun üstüne kapanıp onları helak ettiğinde "akade aleyhim" denir, source:"ع ق د,B016"}.

Bu imge üçüncü ayetin girişini başka bir duyuyla duyurur. Gecenin tepelere "döküldüğü" yukarıda görülmüştü; burada {ar:إِذَا وَقَبَ, tr:izâ vekab, gloss:içeri girdiğinde, source:113:3}, suyun kayadaki oyuğa girip onu doldurması gibi işitilir. Akan şey alçak olan her yeri bulur ve oraya yerleşir. Aynı su toprağı yarıp bitki çıkarır, oyukta toplanıp içilir, ama vadi bir topluluğun üstüne kapandığında öldürür. İkinci ayetin "yarattığı şeylerin şerri" bu sahnede kendi başına kötü bir madde olarak değil, hayat veren bir şeyin yön değiştirmesi olarak görünür. Kur'an da yağmuru bu iki yüzüyle sahneler. "Görmedin mi" diye başlayan bir işaret ayetinde Allah bulutun sürülüp birleştirilişini, yığılışını ve içinden yağmurun çıkışını anlatır: {ar:يُزْجِى سَحَابًۭا ثُمَّ يُؤَلِّفُ بَيْنَهُۥ ثُمَّ يَجْعَلُهُۥ رُكَامًۭا فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَٰلِهِۦ, tr:yuzcî sehâben summe yuellifu beynehû summe yec'aluhû rukâmen fe-tera'l-vedka yaḣrucu min ḣilâlih, gloss:bir bulutu sürer, sonra parçalarını birleştirir, sonra üst üste yığar; yağmurun aralarından çıktığını görürsün, source:24:43}. Aynı ayet dolunun kime ineceğini de söyler: {ar:فَيُصِيبُ بِهِۦ مَن يَشَآءُ وَيَصْرِفُهُۥ عَن مَّن يَشَآءُ, tr:fe-yusîbu bihî men yeşâu ve yasrifuhû an men yeşâ', gloss:onu dilediğine isabet ettirir, dilediğinden de çevirir, source:24:43}. Sığınmanın işleyişi buradadır: aynı bulutun zararı birine iner, birinden çevrilir; çeviren de bulutun Rabbidir. Hak ile batılın bir örneğinde gökten inen su vadileri ölçüleri kadar doldurur: {ar:أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا, tr:enzele mine's-semâi mâen fe-sâlet evdiyetun bi-kaderihâ, gloss:gökten su indirdi, vadiler kendi ölçülerince aktı, source:13:17}; köpük gider, insanlara yarayan yerde kalır. Münafıkları anlatan bir örnekte de yağmur karanlığı birlikte getirir: {ar:أَوْ كَصَيِّبٍۢ مِّنَ ٱلسَّمَآءِ فِيهِ ظُلُمَٰتٌۭ وَرَعْدٌۭ وَبَرْقٌۭ, tr:ev ke-sayyibin mine's-semâi fîhi zulumâtun ve ra'dun ve berk, gloss:ya da gökten boşanan, içinde karanlıklar, gök gürültüsü ve şimşek bulunan bir sağanak gibi, source:2:19}. Gecenin dökülüşü ile yağmurun dökülüşü bu sahnede tek bir gökten iner.

Kaynaklar: 113:1 بِرَبِّ ر ب ب B008; 113:1 بِرَبِّ ر ب ب B007; 113:2 خَلَقَ خ ل ق B008; 113:4 ٱلْعُقَدِ ع ق د B008; 113:1 ٱلْفَلَقِ ف ل ق B003; 113:3 غَاسِقٍ غ س ق B004; 113:1 ٱلْفَلَقِ ف ل ق B004; 113:3 وَقَبَ و ق ب B001; 113:3 وَقَبَ و ق ب B002; 113:2 خَلَقَ خ ل ق B011; 113:2 خَلَقَ خ ل ق B008; 113:1 بِرَبِّ ر ب ب B013; 113:4 ٱلْعُقَدِ ع ق د B016

## Uçları bağlamak, parçaları ayırmak: düğüm ve yarık

Dördüncü ayet bir el işini adlandırır: {ar:وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ, tr:ve min şerri'n-neffâsâti fi'l-ukad, gloss:düğümlere üfleyen kadınların şerrinden, source:113:4}. Düğüm, bir şeyin uçlarını bir araya getirmektir: {ar:العقد الجمع بين أطراف الشيء, tr:el-akdu'l-cem'u beyne etrâfi'ş-şey', gloss:akd, bir şeyin uçlarını bir araya getirmektir, source:"ع ق د,B001"}; ip çekilir, bağlanır ve tutar: {ar:عقدت الحبل أعقده عقدا وقد انعقد, tr:akadtu'l-hable a'kıduhû akden ve kadi'n'akad, gloss:ipi düğümledim, o da düğümlendi, source:"ع ق د,B001"}. Surenin ilk ayetinin kökü ise bunun tam tersini yapar: yarar ve parçaları birbirinden ayırır {source:"ف ل ق,B001"}; bir şeyde açıklık ve ayrılık bırakır: {ar:أصل صحيح يدل على فرجة وبينونة في الشيء, tr:aslun sahîhun yedullu alâ furcetin ve beynûnetin fi'ş-şey', gloss:bir şeydeki açıklığı ve ayrılığı gösteren sağlam bir köktür, source:"ف ل ق,B001"}. İki kök arasında bir köken bağı yoktur; bağ, iki işlemin birbirinin tersi olmasındadır. Sure, işi yarmak olan Rabbe sığınmakla açılır ve iplere düğüm atan kadınlara ulaşır.

Bu düğümün nasıl işlediğini kökün kendisi söyler: {ar:النفاثات في العقد من السواحر اللواتي يعقدن في الخيوط, tr:en-neffâsâtu fi'l-ukad mine's-sevâhiri'llâtî ya'kıdne fi'l-ḣuyût, gloss:düğümlere üfleyenler, ipliklere düğüm atan büyücü kadınlardandır, source:"ع ق د,B013"}. İplik alınır, uçları birbirine dolanır, düğüm atılır ve üstüne üflenir. Büyünün kendisine de düğüm denir: {ar:أصله من العزيمة ولذلك يقال لها عزيمة كما يقال لها عقدة, tr:asluhû mine'l-azîme, ve li-zâlike yukâlu lehâ azîmetun kemâ yukâlu lehâ ukde, gloss:aslı kararlı niyettendir; bu yüzden ona "azîme" dendiği gibi "ukde" de denir, source:"ع ق د,B013"}. Düğüm, bir niyeti iplikte sabitler; çözülmedikçe tutar. Üfleme ile düğüm aynı ifadede yan yana durur: {ar:السواحر والنفاثات في العقد, tr:es-sevâhiru ve'n-neffâsâtu fi'l-ukad, gloss:büyücü kadınlar, düğümlere üfleyenler, source:"ن ف ث,B001"}. Sade bir anlam "büyücülerin şerrinden" der ve işi bir etiketle kapatır. Ayetin sözü ise eli ve ağzı gösterir: düğüm atan el ve düğüme üfleyen ağız. Sure bunu yarma işinin Rabbinin karşısına koyar: biri bağlayıp kapatır, öbürü yarıp açar.

Düğüm insanları birbirine bağlayan bir bağın da adıdır: {ar:عقدة النكاح وكل شيء وجوبه وإبرامه, tr:ukdetu'n-nikâh ve kullu şey'in vucûbuhû ve ibrâmuh, gloss:nikâh düğümü; her şeyin bağlayıcı ve kesin kılınması, source:"ع ق د,B002"}. Kur'an bu bağı aynı kelimeyle anar; boşanma hükümlerinde Allah {ar:ٱلَّذِى بِيَدِهِۦ عُقْدَةُ ٱلنِّكَاحِ, tr:ellezî bi-yedihî ukdetu'n-nikâh, gloss:nikâh düğümü elinde olan, source:2:237} der. Büyünün işini de yine Kur'an söyler. Allah, şeytanların okuduklarına uyanları ve Babil'de iki melek Hârût ile Mârût'tan öğrenilen şeyi anlatırken şöyle der: {ar:فَيَتَعَلَّمُونَ مِنْهُمَا مَا يُفَرِّقُونَ بِهِۦ بَيْنَ ٱلْمَرْءِ وَزَوْجِهِۦ, tr:fe-yeteallemûne minhumâ mâ yuferrikûne bihî beyne'l-mer'i ve zevcih, gloss:o ikisinden kişiyle eşinin arasını ayıracakları şeyi öğrenirler, source:2:102}. Büyücünün düğümü, nikâh düğümünü çözmek için atılır; bağlamak burada ayırmanın aracıdır. Aynı ayet sınırı da koyar: {ar:وَمَا هُم بِضَآرِّينَ بِهِۦ مِنْ أَحَدٍ إِلَّا بِإِذْنِ ٱللَّهِ, tr:ve mâ hum bi-dârrîne bihî min ehadin illâ bi-iznillâh, gloss:Allah'ın izni olmadıkça onunla kimseye zarar veremezler, source:2:102}. Düğümün tutup tutmayacağı onu atanın elinde değildir; sığınma, iznin sahibine yönelir.

Kökün başka iki düğümü de aynı tutma işini gösterir. Öfke bağlanır ve zarara hazırlanır: {ar:عقد فلان ناصيته إذا غضب وتهيأ للشر, tr:akade fulânun nâsiyetehû izâ ğadibe ve teheyyee li'ş-şerr, gloss:biri öfkelenip kötülüğe hazırlandığında "perçemini düğümledi" denir, source:"ع ق د,B012"}; öfke dinince de düğümleri çözülür: {ar:إذا سكن غضبه قد تحللت عقده, tr:izâ sekene ğadabuhû kad tehallelet ukaduh, gloss:öfkesi dinince düğümleri çözüldü denir, source:"ع ق د,B012"}. Tanımın kendisi düğüm ile şerri tek cümlede birleştirir. Dil de düğümlenir: {ar:عقد لسانه احتبس وبلسانه عقدة أي في كلامه حبسة, tr:akade lisânuhû ihtebese, ve bi-lisânihî ukde ey fî kelâmihî hubse, gloss:dili düğümlendi, yani tutuldu; dilinde düğüm var, yani konuşmasında tutukluk var, source:"ع ق د,B007"}. Kur'an bu düğümün Rab tarafından çözülmesini Musa'nın duasında gösterir. Firavun'a gönderilen Musa Rabbine şöyle yalvarır: {ar:قَالَ رَبِّ ٱشْرَحْ لِى صَدْرِى, tr:kâle rabbi'şrah lî sadrî, gloss:dedi ki: Rabbim, göğsümü aç, source:20:25}, {ar:وَٱحْلُلْ عُقْدَةًۭ مِّن لِّسَانِى, tr:vahlul ukdeten min lisânî, gloss:dilimden düğümü çöz, source:20:27}, {ar:يَفْقَهُوا۟ قَوْلِى, tr:yefkahû kavlî, gloss:sözümü anlasınlar, source:20:28}. Göğüs açılır, düğüm çözülür ve söz anlaşılır hâle gelir; yarmanın ve açmanın Rabbi düğümü çözen olarak çağrılır.

Felak kökünün içinde de tersine dönmüş bir bağ vardır: {ar:الفلق أيضا مقطرة السجان, tr:el-felaku eyden mıktaratu's-seccân, gloss:felak, gardiyanın ayak tomruğudur da, source:"ف ل ق,B005"}. Yarılmış bir kütüğün iki parçası bir tutsağın ayaklarını sıkıştırır; yarık burada bir bağdır. Çözmek de her zaman iyi değildir. Allah yeminleri bozmaya karşı uyarırken kendi eğirdiği ipliği söken bir kadını örnek verir: {ar:كَٱلَّتِى نَقَضَتْ غَزْلَهَا مِنۢ بَعْدِ قُوَّةٍ أَنكَٰثًۭا, tr:ke'lletî nekadat ğazlehâ min ba'di kuvvetin enkâsâ, gloss:ipliğini sağlamca eğirdikten sonra çözüp lime lime eden kadın gibi, source:16:92}. Hangi düğümün atılacağı, hangisinin çözüleceği, düğümün kime bağladığına göre değişir. Dördüncü ayetin düğümleri zarar için atılmıştır; onlara karşı çağrılan Rab, kapatanı yarandır.

Kaynaklar: 113:4 ٱلْعُقَدِ ع ق د B001; 113:1 ٱلْفَلَقِ ف ل ق B001; 113:4 ٱلْعُقَدِ ع ق د B013; 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B001; 113:4 ٱلْعُقَدِ ع ق د B002; 113:4 ٱلْعُقَدِ ع ق د B012; 113:4 ٱلْعُقَدِ ع ق د B007; 113:1 ٱلْفَلَقِ ف ل ق B005

## Ağıza karşı ağız: emredilen sığınma ve düğüme üfleme

Surede iki ağız işi karşı karşıya durur. İlk ayette dile bir söz emredilir: {ar:قُلْ, tr:kul, gloss:de, source:113:1}. Söz, dil ile dışarı çıkarılmış harflerdir {source:"ق و ل,B001"}, ve dilin kendisi bu kökten "söyleme aleti" diye adlandırılır: {ar:المقول اللسان, tr:el-mikvelu'l-lisân, gloss:mikvel, dildir, source:"ق و ل,B002"}. Söylenen söz ise sığınmanın kalıbıdır: {ar:أعوذ بالله أي ألجأ إلى الله عوذا وعياذا, tr:eûzu billâh ey elceu ilallâhi avzen ve iyâzâ, gloss:"eûzu billâh", yani Allah'a sığınırım, source:"ع و ذ,B001"}. Dördüncü ayette ise büyücü kadınlar düğümlere üfler; bu üfleme ağızdan çıkan az bir tükürüktür: {ar:قذف الريق القليل, tr:kazfu'r-rîki'l-kalîl, gloss:az bir tükürüğü fırlatmak, source:"ن ف ث,B001"}.

İki işi birbirine yaklaştıran şey, aynı fiilin her iki tarafta da söylenmesidir. Koruyucu bir okuma yapan da üfler: {ar:نفث الراقي ريقه وهو أقل من التفل, tr:nefese'r-râkî rîkahû ve huve ekallu mine't-tefl, gloss:okuyup üfleyen tükürüğünü üfledi; bu, tükürmekten daha azdır, source:"ن ف ث,B001"}. Ağızdan çıkan şey söz de olabilir: {ar:سمي الشعر نفثا لأنه كالشيء ينفثه الإنسان من فيه مثل الرقية, tr:summiye'ş-şi'ru nefsen li-ennehû ke'ş-şey'i yenfusuhu'l-insânu min fîhi misle'r-rukye, gloss:şiire "nefs" denmiştir, çünkü insanın ağzından üflediği bir şey gibidir, okuma gibi, source:"ن ف ث,B005"}. Sığınma kökü de koruyucu okumanın adını verir: {ar:العوذة ما يعاذ به من الشيء ومنه قيل للتميمة والرقية عوذة, tr:el-ûze mâ yuâzu bihî mine'ş-şey', ve minhu kîle li't-temîmeti ve'r-rukyeti ûze, gloss:ûze, bir şeyden kendisiyle sığınılan şeydir; muskaya ve okumaya ûze denmesi bundandır, source:"ع و ذ,B002"}. Büyücünün düğümü de bir şey olarak bağlanır: {ar:النفاثات في العقد جمع عقدة وهي ما تعقده الساحرة, tr:en-neffâsâtu fi'l-ukad, cem'u ukde ve hiye mâ ta'kıduhe's-sâhira, gloss:düğümlere üfleyenler; ukad, büyücü kadının bağladığı düğümün çoğuludur, source:"ع ق د,B013"}.

Böylece iki ağız aynı hareketi yapar: içten bir şey çıkar ve bir yere yönelir. Fark ağzın işinde değil, sözün kime yöneldiğindedir. Büyücünün nefesi düğüme gider ve orada hapsolur; emredilen söz ise Rabbe yönelir ve O'na sığınır. Sure, okunduğunda kendisi bir ûze olur: kendisiyle sığınılan bir söz. Ama bu söz bir ipliğe bağlanmaz, boyna asılmaz; dille söylenir ve söyleyeni Rabbine bağlar. "Eûzu" birinci tekil şahısla söylenir; sığınma, birinin onu kendi ağzıyla söylemesiyle gerçekleşir. Kökün karşı ucunda ise sözü tutulan dil durur: {ar:رجل أعقد وعقد للذي في لسانه عقدة, tr:raculun a'kadu ve akidun li'llezî fî lisânihî ukde, gloss:dilinde düğüm olan adama "a'kad" ve "akid" denir, source:"ع ق د,B007"}. Düğüme üfleyen ağız sözü düğümler; emredilen ağız sözü açar.

Kur'an bu kalıbı birçok kez bir ağza koyar. Allah Peygambere emreder: {ar:وَقُل رَّبِّ أَعُوذُ بِكَ مِنْ هَمَزَٰتِ ٱلشَّيَٰطِينِ, tr:ve kul rabbi eûzu bike min hemezâti'ş-şeyâtîn, gloss:de ki: Rabbim, şeytanların dürtmelerinden sana sığınırım, source:23:97}, {ar:وَأَعُوذُ بِكَ رَبِّ أَن يَحْضُرُونِ, tr:ve eûzu bike rabbi en yahdurûn, gloss:Rabbim, yanıma gelmelerinden de sana sığınırım, source:23:98}. Emir, Rab ve sığınma burada da aynı sıradadır. Ardından gelen sure aynı sözle açılır: {ar:قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ, tr:kul eûzü bi-rabbi'n-nâs, gloss:de ki: insanların Rabbine sığınırım, source:114:1}. Şeytanın dürtmesine karşı verilen emir, sığınmanın işitilen bir söz olduğunu açıkça söyler: {ar:فَٱسْتَعِذْ بِٱللَّهِ ۚ إِنَّهُۥ سَمِيعٌ عَلِيمٌ, tr:festeiz billâh, innehû semîun alîm, gloss:Allah'a sığın; O işitendir, bilendir, source:7:200}. Kur'an okunmadan önce de aynı söz emredilir {source:16:98}. Kur'an'ın anlattığı insanlar da tehdit anında bu sözü söyler. Musa Firavun'un çevresine karşı {ar:إِنِّى عُذْتُ بِرَبِّى وَرَبِّكُم مِّن كُلِّ مُتَكَبِّرٍۢ, tr:innî uztu bi-rabbî ve rabbikum min kulli mutekebbir, gloss:her büyüklenenden benim de Rabbim, sizin de Rabbiniz olana sığındım, source:40:27} der; taşlanma tehdidinde de aynı sözü tekrarlar {source:44:20}. Meryem karşısına bir insan kılığında çıkan ruha {ar:إِنِّىٓ أَعُوذُ بِٱلرَّحْمَٰنِ مِنكَ, tr:innî eûzu bi'r-rahmâni mink, gloss:senden Rahman'a sığınırım, source:19:18} der. Yusuf kapılar üstüne kilitlendiğinde, {ar:وَغَلَّقَتِ ٱلْأَبْوَٰبَ, tr:ve ğallekati'l-ebvâb, gloss:kapıları sıkıca kapadı, source:12:23}, tek cümleyle çıkış arar: {ar:مَعَاذَ ٱللَّهِ ۖ إِنَّهُۥ رَبِّىٓ, tr:meâzallâh, innehû rabbî, gloss:Allah'a sığınırım; o benim efendimdir, source:12:23}. Nuh da oğlu için yaptığı isteğin ardından Rabbine {ar:رَبِّ إِنِّىٓ أَعُوذُ بِكَ, tr:rabbi innî eûzu bik, gloss:Rabbim, sana sığınırım, source:11:47} der. Her birinde sığınma, tehlikenin tam ortasında ağızdan çıkan bir cümledir.

Büyünün ağız ve iple yürüyen işini de Kur'an, Musa'nın Firavun'un büyücüleriyle karşılaşmasında gösterir. Büyücüler "önce sen mi atarsın, biz mi" diye sorar {source:20:65}; Musa "siz atın" der ve {ar:فَإِذَا حِبَالُهُمْ وَعِصِيُّهُمْ يُخَيَّلُ إِلَيْهِ مِن سِحْرِهِمْ أَنَّهَا تَسْعَىٰ, tr:fe-izâ hibâluhum ve isıyyuhum yuḣayyelu ileyhi min sihrihim ennehâ tes'â, gloss:bir de baktı ki ipleri ve değnekleri büyülerinden ötürü ona koşuyormuş gibi görünüyor, source:20:66}. Büyünün aracı iplerdir. Musa içinde bir korku duyar {source:20:67}, ve ona söylenen söz sınırı çizer: {ar:وَلَا يُفْلِحُ ٱلسَّاحِرُ حَيْثُ أَتَىٰ, tr:ve lâ yuflihu's-sâhiru haysu etâ, gloss:büyücü nereye gelirse gelsin başarıya ulaşamaz, source:20:69}.

Kaynaklar: 113:1 قُلْ ق و ل B001; 113:1 قُلْ ق و ل B002; 113:1 أَعُوذُ ع و ذ B001; 113:1 أَعُوذُ ع و ذ B002; 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B001; 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B005; 113:4 ٱلْعُقَدِ ع ق د B013; 113:4 ٱلْعُقَدِ ع ق د B007

## Sığınılana bağlanmak: tutunmak, bağlanan boyun, ahit

Bu surede sığınmak uzaklaşmak değil, yapışmaktır. Surenin ilk iki asıl kelimesi tek bir ifadede birleşir: {ar:عاذ فلان بربه يعوذ عوذا إذا لجأ إليه واعتصم به, tr:âze fulânun bi-rabbihî yeûzu avzen izâ lecee ileyhi va'tesame bih, gloss:biri Rabbine sığındı, yani O'na yöneldi ve O'na sımsıkı tutundu, source:"ع و ذ,B001"}. Sığınmak bir başkasına yönelip ona asılmaktır: {ar:العوذ الالتجاء إلى الغير والتعلق به, tr:el-avzu'l-iltica'u ile'l-ğayri ve't-tealluku bih, gloss:avz, bir başkasına sığınıp ona tutunmaktır, source:"ع و ذ,B001"}. Kökün daha somut bir dalı bu tutunmayı bedende gösterir: {ar:كل شيء لصق بشيء أو لازمه, tr:kullu şey'in lesıka bi-şey'in ev lâzemeh, gloss:bir şeye yapışan ya da ondan ayrılmayan her şey, source:"ع و ذ,B004"}; {ar:أطيب اللحم عوذه وهو ما عاذ بالعظم ولزمه, tr:etyebu'l-lahmi ûzuhû ve huve mâ âze bi'l-azmi ve lezimeh, gloss:etin en lezzetlisi kemiğe sığınıp ondan ayrılmayan kısmıdır, source:"ع و ذ,B004"}. Rab kökünün de bir dalı aynı yerinden ayrılmamayı adlandırır: {ar:الأصل الآخر لزوم الشيء والإقامة عليه, tr:el-aslu'l-âḣaru luzûmu'ş-şey'i ve'l-ikâmetu aleyh, gloss:öbür asıl, bir şeyden ayrılmamak ve onun üzerinde kalmaktır, source:"ر ب ب,B007"}; {ar:أرب فلان بالمكان إذا أقام به فلم يبرحه, tr:erabbe fulânun bi'l-mekân izâ ekâme bihî fe-lem yebrahh, gloss:biri bir yerde kalıp oradan ayrılmadığında "erabbe" denir, source:"ر ب ب,B007"}. İki tanım aynı "ayrılmamak" kelimesiyle kurulur.

Sade bir anlam "korunma isterim" der ve sığınanla sığınılan arasına bir mesafe koyar. Bu imgede {ar:أَعُوذُ بِرَبِّ, tr:eûzu bi-rabbi, gloss:Rabbe sığınırım, source:113:1} sözü etin kemiğe yapışması gibi bir yakınlığı duyurur: sığınan, sığındığından ayrılmayacak kadar ona bitişir. Düğüm kökü de sığınmayı bir bağlama olarak adlandırır: {ar:عقد فلان عنقه إلى فلان وعكدها إذا لجأ إليه, tr:akade fulânun unukahû ilâ fulânin ve akedehâ izâ lecee ileyh, gloss:biri bir başkasına sığındığında "boynunu ona bağladı" denir, source:"ع ق د,B017"}. Bu ifadeyi açıklayan fiil, sığınmayı açıklayan fiilin aynısıdır. Boyun her iki kökte de bir yer olarak belirir. Sığınma kökü atın boynunda gerdanlığın durduğu yeri adlandırır: {ar:معوذ الفرس موضع القلادة, tr:muavvazu'l-feres mevdiu'l-kılâde, gloss:atın muavvazı gerdanlığın yeridir, source:"ع و ذ,B005"}; düğüm kökü de boynu çeviren gerdanlığı: {ar:عقد القلادة ما يكون طوار العنق, tr:ıkdu'l-kılâde mâ yekûnu tavâra'l-unuk, gloss:gerdanlık dizisi, boynu çevreleyendir, source:"ع ق د,B001"}.

Rab kökü bir bağlılık ahdinin de adıdır ve onu düğüm kelimesiyle tanımlar: {ar:العقد في موالاة الغير: الربابة, tr:el-akdu fî muvâlâti'l-ğayr: er-rabâbe, gloss:bir başkasına bağlılıktaki düğüm: rabâbe, source:"ر ب ب,B011"}; {ar:الربابة: العهد والميثاق؛ الأربة أهل الميثاق, tr:er-rabâbe: el-ahdu ve'l-mîsâk; el-ribbe ehlu'l-mîsâk, gloss:rabâbe ahit ve antlaşmadır; ribbe antlaşma ehlidir, source:"ر ب ب,B011"}. Düğüm de ahitlerin en sağlamıdır: {ar:العقود العهود وهي أوكد العهود, tr:el-ukûdu'l-uhûd ve hiye evkedu'l-uhûd, gloss:ukûd ahitlerdir ve ahitlerin en sağlamıdır, source:"ع ق د,B002"}. Rab kökü sağlam atılmış bir düğümü bile adlandırır: {ar:الربى: العقدة المحكمة, tr:er-ribbâ: el-ukdetu'l-muhkeme, gloss:ribbâ, sağlam atılmış düğümdür, source:"ر ب ب,B016"}. Yakınlık da düğümle ölçülür: {ar:هو مني معقد الإزار يراد به قرب المنزلة, tr:huve minnî ma'kıde'l-izâr, yurâdu bihî kurbu'l-menzile, gloss:o bana peştamalımın düğümü kadar yakındır, yani konumca çok yakındır, source:"ع ق د,B015"}. Dördüncü ayetin düğümleri zarar için iplere atılır; bu imgede ise sığınan, kendini Rabbine sağlam bir düğümle bağlar. Bir düğüme karşı bir başka düğüm durur.

Kur'an bu tutunmayı bir ip ve bir kulp olarak sahneler. Allah müminlere önce kendisinden hakkıyla sakınmalarını emreder {source:3:102}, sonra şöyle der: {ar:وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا وَلَا تَفَرَّقُوا۟, tr:va'tesımû bi-hablillâhi cemîan ve lâ teferrakû, gloss:hep birlikte Allah'ın ipine sımsıkı tutunun ve ayrılmayın, source:3:103}. Tutunmayı söyleyen fiil, Rabbe sığınmayı açıklayan ifadedeki fiilin aynısıdır; ipe tutunmanın karşısında da ayrılmak durur. Ayet devam eder: {ar:فَأَلَّفَ بَيْنَ قُلُوبِكُمْ, tr:fe-ellefe beyne kulûbikum, gloss:kalplerinizin arasını birleştirdi, source:3:103}; ve {ar:وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍۢ مِّنَ ٱلنَّارِ فَأَنقَذَكُم مِّنْهَا, tr:ve kuntum alâ şefâ hufratin mine'n-nâri fe-enkazekum minhâ, gloss:ateşten bir çukurun kenarındaydınız, sizi oradan kurtardı, source:3:103}. Allah inanç üzerine konuşurken bağı yarılmaz bir kulp olarak tarif eder: {ar:فَقَدِ ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ لَا ٱنفِصَامَ لَهَا, tr:fe-kadi'stemseke bi'l-urveti'l-vuskâ lenfisâme lehâ, gloss:kopması olmayan en sağlam kulpa tutunmuştur, source:2:256}. Yarma bu bağa işlemez. Ters örneği cinler anlatır: {ar:وَأَنَّهُۥ كَانَ رِجَالٌۭ مِّنَ ٱلْإِنسِ يَعُوذُونَ بِرِجَالٍۢ مِّنَ ٱلْجِنِّ فَزَادُوهُمْ رَهَقًۭا, tr:ve ennehû kâne ricâlun mine'l-insi yeûzûne bi-ricâlin mine'l-cinni fe-zâdûhum rahakâ, gloss:insanlardan bazı adamlar cinlerden bazı adamlara sığınırlardı; bu da onların yükünü artırdı, source:72:6}. Aynı fiil, yanlış sığınılana yöneldiğinde tutunanı ağırlaştırır. Ahit düğümlerine bağlılık da açık bir emirdir: {ar:يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَوْفُوا۟ بِٱلْعُقُودِ, tr:yâ eyyuhe'llezîne âmenû evfû bi'l-ukûd, gloss:ey inananlar, düğümlerinize, ahitlerinize bağlı kalın, source:5:1}. Dördüncü ayetin kelimesiyle aynı kökten olan bu düğümler bozulmak için değil, tutulmak için atılmıştır.

Kaynaklar: 113:1 أَعُوذُ ع و ذ B001; 113:1 أَعُوذُ ع و ذ B004; 113:1 بِرَبِّ ر ب ب B007; 113:4 ٱلْعُقَدِ ع ق د B017; 113:1 أَعُوذُ ع و ذ B005; 113:4 ٱلْعُقَدِ ع ق د B001; 113:1 بِرَبِّ ر ب ب B011; 113:4 ٱلْعُقَدِ ع ق د B002; 113:1 بِرَبِّ ر ب ب B016; 113:4 ٱلْعُقَدِ ع ق د B015

## İçeride tutulan, dışarı çıkan

Surenin birçok kelimesi, içeride tutulan bir şeyin dışarı çıkışını adlandırır. Üfleme kökü, göğsü sıkışan için bir zorunluluk söyler: {ar:لا بد للمصدور أن ينفث, tr:lâ budde li'l-masdûri en yenfus, gloss:göğsü dolan, mutlaka üfleyip boşaltır, source:"ن ف ث,B003"}. Yılan zehrini üfler: {ar:الحية تنفث السم, tr:el-hayyetu tenfusu's-semm, gloss:yılan zehir üfler, source:"ن ف ث,B001"}. Yara kanı dışarı verir: {ar:دم نفيث نفثه الجرح أي أظهره, tr:demun nefîsun nefesehu'l-curhu ey azharah, gloss:yaranın üfleyip çıkardığı, yani ortaya koyduğu kan, source:"ن ف ث,B002"}. Üçüncü ayetin kökü de yaranın akıntısını adlandırır: {ar:غسق الجرح غسقانا إذا سال منه ماء أصفر, tr:ğasaka'l-curhu ğasakânen izâ sâle minhu mâun asfar, gloss:yaradan sarı su aktığında "ğasaka" denir, source:"غ س ق,B004"}; ve ateşte olanların derisinden damlayanı: {ar:الغساق ما تقطر من جلود أهل النار, tr:el-ğassâku mâ tekattara min culûdi ehli'n-nâr, gloss:ğassâk, ateş ehlinin derilerinden damlayandır, source:"غ س ق,B002"}. Şer kökü ateşten uçuşan kıvılcımı: {ar:الشرر ما تطاير من النار الواحدة شررة, tr:eş-şeraru mâ tetâyera mine'n-nâr, el-vâhidetu şerara, gloss:şerar, ateşten uçuşandır; tekili şerara, source:"ش ر ر,B003"}; ve yukarıda görülen "çıkarıp göstermek" anlamını taşır: {ar:أشررت الشيء أظهرته, tr:eşrartu'ş-şey'e azhartuh, gloss:şeyi ortaya koydum, source:"ش ر ر,B008"}. Yaranın kanını "ortaya koyan" fiil ile bu fiil aynıdır.

Öfke de önce bağlanır, sonra çıkar: {ar:عقد ناصيته إذا غضب فتهيأ للشر, tr:akade nâsiyetehû izâ ğadibe fe-teheyyee li'ş-şerr, gloss:öfkelenip kötülüğe hazırlandığında perçemini düğümledi denir, source:"ع ق د,B012"}. Haset de bir istek olarak içeride durur, sonra bir çabaya dönüşür: {ar:وربما كان مع ذلك سعي في إزالتها, tr:ve rubbemâ kâne mea zâlike sa'yun fî izâletihâ, gloss:bazen bununla birlikte onu gidermeye çalışmak da olur, source:"ح س د,B001"}. Sözün de içeride tutulan bir hâli vardır: {ar:في نفسي قول لم أظهره, tr:fî nefsî kavlun lem uzhirh, gloss:içimde ortaya koymadığım bir söz var, source:"ق و ل,B012"}.

Bu imge surenin iki "izâ" cümlesine bir yön verir. Üçüncü ayette karanlık içeri girer: {ar:إِذَا وَقَبَ, tr:izâ vekab, gloss:içeri girdiğinde, source:113:3}. Beşinci ayette haset dışarı çıkar: {ar:إِذَا حَسَدَ, tr:izâ hased, gloss:haset ettiğinde, source:113:5}. Biri dışarıdan içeriye, öbürü içeriden dışarıya bir eşik geçişidir ve sığınma tam bu eşiklere yönelir. Karanlık henüz girmemişken, haset henüz çabaya dönmemişken zarar beklemededir; tehlike geçiş anındadır. Düğümlenen öfke ile düğüme üflenen nefes de aynı eşikte durur: tutulan şey bir yere bırakılır. Emredilen söz ise bunların karşısında konuşanın kendi çıkarışıdır. "Kul" emri, içeride duran sığınma sözünü dışarı çıkarır; zehir, irin ve kıvılcım dışarı çıkarken sığınan da kendi sözünü çıkarır.

Kur'an bu çıkışı düşmanca yakınlar hakkında Allah'ın müminlere uyarısında sahneler: {ar:قَدْ بَدَتِ ٱلْبَغْضَآءُ مِنْ أَفْوَٰهِهِمْ وَمَا تُخْفِى صُدُورُهُمْ أَكْبَرُ, tr:kad bedeti'l-bağdâu min efvâhihim ve mâ tuḣfî sudûruhum ekber, gloss:öfke ağızlarından taşmıştır; göğüslerinin sakladığı ise daha büyüktür, source:3:118}. Ağızdan çıkan, göğüste tutulanın bir parçasıdır. Ayetler devam eder: {ar:وَإِذَا خَلَوْا۟ عَضُّوا۟ عَلَيْكُمُ ٱلْأَنَامِلَ مِنَ ٱلْغَيْظِ ۚ قُلْ مُوتُوا۟ بِغَيْظِكُمْ, tr:ve izâ ḣalev addû aleykumu'l-enâmile mine'l-ğayz, kul mûtû bi-ğayzikum, gloss:yalnız kaldıklarında size karşı öfkeden parmak uçlarını ısırırlar; de ki: öfkenizle ölün, source:3:119}. Öfke içeride tutulur ve onun karşısına yine emredilen bir "de ki" konur. Hemen ardından gelen ayette ise iyiliğin onları üzdüğü söylenir {source:3:120}. Kıvılcım ve akıntı Kur'an'da ateşin sahnesine aittir. Ayırma Günü'nü anlatan ayetlerde ateş için {ar:إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ, tr:innehâ termî bi-şerarin ke'l-kasr, gloss:o, saray gibi kıvılcımlar atar, source:77:32} denir; azgınların içeceği de {ar:هَٰذَا فَلْيَذُوقُوهُ حَمِيمٌۭ وَغَسَّاقٌۭ, tr:hâzâ fe'l-yezûkûhu hamîmun ve ğassâk, gloss:işte bu; tatsınlar onu: kaynar su ve irin, source:38:57} olur; başka bir yerde de yalnızca {ar:إِلَّا حَمِيمًۭا وَغَسَّاقًۭا, tr:illâ hamîmen ve ğassâkâ, gloss:kaynar su ve irinden başka, source:78:25}. Şer kelimesinin akrabası kıvılcım, gāsık kelimesinin akrabası irin, böylece ateşte dışarı atılanın adları olarak Kur'an'da geçer. Ayetteki şer de gāsık da bu anlamlarda değildir; ama aynı köklerden çıkan bu sözler, içeride tutulan zararın bir gün dışarı atılacağını yanlarında duyurur.

Kaynaklar: 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B003; 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B001; 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B002; 113:3 غَاسِقٍ غ س ق B004; 113:3 غَاسِقٍ غ س ق B002; 113:2 شَرِّ ش ر ر B003; 113:2 شَرِّ ش ر ر B008; 113:4 ٱلْعُقَدِ ع ق د B012; 113:5 حَسَدَ ح س د B001; 113:1 قُلْ ق و ل B012

## Yeni doğurmuş dişi ve yavrusu

Surenin ilk ayetindeki iki kelime, aynı hayvanı aynı anında adlandırır: yeni doğurmuş dişiyi. Sığınma kökü onu doğumdan sonraki ilk günleriyle anar: {ar:كل أنثى عائذ إذا وضعت مدة سبعة أيام, tr:kullu unsâ âizun izâ vada'at muddete seb'ati eyyâm, gloss:her dişi doğurduğunda yedi gün boyunca "âiz"dir, source:"ع و ذ,B003"}; {ar:العوذ الحديثات النتاج من الظباء والإبل والخيل واحدتها عائذ, tr:el-ûzu'l-hadîsâtu'n-nitâc mine'z-zıbâi ve'l-ibili ve'l-ḣayl, vâhidetuhâ âiz, gloss:ûz, ceylanlardan, develerden ve atlardan yeni doğurmuş olanlardır; tekili âizdir, source:"ع و ذ,B003"}. Rab kökü de yeni doğurmuş koyunu adlandırır: {ar:الربى: الشاة التي وضعت حديثا, tr:er-ubbâ: eş-şâtu'lletî vada'at hadîsen, gloss:rubbâ, yeni doğurmuş koyundur, source:"ر ب ب,B009"}; sütü için evde tutulan koyundur bu: {ar:الشاة الربي التي تحتبس في البيت للبن, tr:eş-şâtu'r-rubbâ elletî tuhtebesu fi'l-beyti li'l-leben, gloss:rubbâ koyun, sütü için evde alıkonulandır, source:"ر ب ب,B009"}.

Bu iki adın çevresinde köklerin geri kalanı bir doğum ve büyütme sürecini tamamlar. Düğüm kökü rahmin tohumu tutuşunu adlandırır: {ar:عقدت فم الرحم على الماء, tr:akadet feme'r-rahimi ale'l-mâ', gloss:rahmin ağzını suyun üzerine düğümledi, source:"ع ق د,B010"}. Halk kökü tamamlanmış ceninin adıdır: {ar:مضغة مخلقة أي تامة الخلق, tr:mudğatun muḣallaka ey tâmmetu'l-ḣalk, gloss:muhallak et parçası, yani yaratılışı tamamlanmış olan, source:"خ ل ق,B003"}. Rab kökü doğandan sonrasını üstlenir: çocuğu emziren ve bakan kadın, {ar:الربيبة: الحاضنة, tr:er-rabîbe: el-hâdına, gloss:rabîbe, çocuğa bakan kadındır, source:"ر ب ب,B005"}; üvey çocuğun işini üstlenen, {ar:الراب الذي يقوم على أمر الربيب, tr:er-râbbu'llezî yekûmu alâ emri'r-rabîb, gloss:râb, rabîbin işini üstlenendir, source:"ر ب ب,B005"}; ve çocuğu büyütmek: {ar:رب فلان ولده؛ رباه, tr:rabbe fulânun veledeh, rabbâh, gloss:biri çocuğunu büyüttü, source:"ر ب ب,B002"}.

İlk ayette sığınan ile sığınılan arasındaki ilişki bu sahnede bir doğumun hemen sonrası olarak duyulur. Doğumdan sonraki günlerde yavru en savunmasız hâlindedir ve büsbütün doğurana bağlıdır; doğuran da onu emzirip büyütmek için alıkonur. "Eûzu" ile "rab" kelimeleri ailelerinde bu iki tarafın adlarını taşır. Sade bir anlam "Rabbe sığınırım" der; bu imge sığınmayı yeni doğmuş bir canlının, onu dünyaya getiren ve büyüten varlığa duyduğu ihtiyaç kadar yakın kılar. Kelimelerin anlamı yine sığınmak ve Rabdir; doğum sahnesi bu anlamların yanında durur.

Kur'an bu sahnenin bütün adımlarını tek bir kıssada verir. İmran'ın karısı Rabbine şöyle seslenir: {ar:رَبِّ إِنِّى نَذَرْتُ لَكَ مَا فِى بَطْنِى مُحَرَّرًۭا, tr:rabbi innî nezertu leke mâ fî batnî muharraran, gloss:Rabbim, karnımdakini sana adanmış olarak adadım, source:3:35}. Doğum gelir: {ar:فَلَمَّا وَضَعَتْهَا, tr:fe-lemmâ vada'athâ, gloss:onu doğurunca, source:3:36}; ve doğurur doğurmaz annenin söylediği söz bir sığınmadır: {ar:وَإِنِّىٓ أُعِيذُهَا بِكَ وَذُرِّيَّتَهَا مِنَ ٱلشَّيْطَٰنِ ٱلرَّجِيمِ, tr:ve innî uîzuhâ bike ve zurriyyetehâ mine'ş-şeytâni'r-racîm, gloss:onu da soyunu da kovulmuş şeytandan sana sığındırırım, source:3:36}. Kökün yeni doğurmuş dişiyi adlandırdığı o günlerde anne, yavrusunu Rabbe sığındırır. Ardından Rab büyütmeyi üstlenir: {ar:فَتَقَبَّلَهَا رَبُّهَا بِقَبُولٍ حَسَنٍۢ وَأَنۢبَتَهَا نَبَاتًا حَسَنًۭا وَكَفَّلَهَا زَكَرِيَّا, tr:fe-tekabbelehâ rabbuhâ bi-kabûlin hasenin ve enbetehâ nebâten hasenen ve keffelehâ zekeriyyâ, gloss:Rabbi onu güzel bir kabulle kabul etti, güzel bir bitki gibi büyüttü ve Zekeriya'yı ona bakıcı yaptı, source:3:37}. Büyüme bir bitkinin büyümesi olarak söylenir ve çocuğun işini üstlenen bir bakıcı belirir. Rahim, doğum, Rabbe sığındırma ve Rabbin büyütmesi aynı sahnededir. Diriltilmekten şüphe edenlere hitap eden ayet de rahimdeki tutuluşu ve dışarı çıkarılışı birlikte anar: {ar:وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى, tr:ve nukırru fi'l-erhâmi mâ neşâu ilâ ecelin musemmâ, gloss:dilediğimizi belirli bir süreye kadar rahimlerde tutarız, source:22:5}.

Kaynaklar: 113:1 أَعُوذُ ع و ذ B003; 113:1 بِرَبِّ ر ب ب B009; 113:4 ٱلْعُقَدِ ع ق د B010; 113:2 خَلَقَ خ ل ق B003; 113:1 بِرَبِّ ر ب ب B005; 113:1 بِرَبِّ ر ب ب B002

## Uydurulan ve yayılan söz

Surenin söz ve yaratma kelimeleri, kök ailelerinde uydurulmuş sözü de adlandırır. "Kul" emrinin kökü olmamış bir şeyi söylemeyi anlatır: {ar:تقول باطلا أي قال ما لم يكن, tr:tekavvele bâtılen ey kâle mâ lem yekun, gloss:asılsız söz uydurdu, yani olmamış olanı söyledi, source:"ق و ل,B005"}; {ar:تقول عليه أي كذب عليه, tr:tekavvele aleyhi ey kezebe aleyh, gloss:onun hakkında söz uydurdu, yani onun adına yalan söyledi, source:"ق و ل,B005"}. Aynı kök insanlar arasında yayılan sözü de adlandırır: {ar:القالة القول الفاشي في الناس, tr:el-kâle el-kavlu'l-fâşî fi'n-nâs, gloss:kâle, insanlar arasında yayılan sözdür, source:"ق و ل,B007"}. İkinci ayetin halk kökü söz için kullanıldığında yalan demektir: {ar:خلق الإفك واختلقه وتخلقه أي افتراه, tr:ḣaleka'l-ifke vaḣtelekahû ve teḣallekahû ey efterâh, gloss:yalanı yarattı, uydurdu; yani onu düzdü, source:"خ ل ق,B007"}; {ar:كل موضع استعمل الخلق في وصف الكلام فالمراد به الكذب, tr:kullu mevdiin ustumile'l-ḣalku fî vasfi'l-kelâmi fe'l-murâdu bihi'l-kezib, gloss:halk kelimesinin söz için kullanıldığı her yerde kastedilen yalandır, source:"خ ل ق,B007"}. Dördüncü ayetin kelimeleri de söze uzanır: ağızdan üflenen söz {source:"ن ف ث,B005"} ve anlaşılmaz kılınmış, düğümlenmiş söz: {ar:كلام معقد أي مغمض, tr:kelâmun muakkad ey muğmad, gloss:düğümlü söz, yani kapalı söz, source:"ع ق د,B007"}. Şer kökü de birine kötülük isnat etmeyi adlandırır: {ar:أشررت فلانا إذا نسبته إلى الشر, tr:eşrartu fulânen izâ nesebtuhû ile'ş-şerr, gloss:birini kötülüğe nispet ettiğimde "eşrartu" derim, source:"ش ر ر,B001"}; arkasından da çekişme gelir {source:"ش ر ر,B011"}.

Bu ailede sözün bir zarar yolu belirir: olmamış bir şey söylenir, birine isnat edilir, dilden dile yayılır, anlaşılmaz kılınır ve sonunda birine kötülük yakıştırılıp çekişme doğar. İkinci ayetin anlamı Allah'ın yaratmasıdır ve bu yalan anlamı orada değildir; ama kök ailesinde yanında durarak yaratılmışların şerrinin bir türünü, insan ağzının uydurduğu şeyi akla getirir. Bu yolun karşısında surenin ilk kelimesi durur. "Kul", bir uydurma değil, emredilmiş bir sözdür; söyleyen onu kendinden düzmez, kendisine söylenmesi emredileni söyler ve onu bir insana değil, Rabbe yöneltir.

Kur'an emredilmiş söz ile uydurulmuş sözü aynı kökle karşı karşıya koyar. Allah Elçisinin doğruluğu hakkında şöyle der: {ar:وَلَوْ تَقَوَّلَ عَلَيْنَا بَعْضَ ٱلْأَقَاوِيلِ, tr:ve lev tekavvele aleynâ ba'da'l-ekâvîl, gloss:eğer o bize karşı bazı sözler uydurmuş olsaydı, source:69:44}. Uydurmanın fiili, "kul" emrinin kökünden gelir ve emredilen sözün tam karşıtıdır. İbrahim kavmine putlara tapınmalarını bu kökle anlatır: {ar:إِنَّمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ أَوْثَٰنًۭا وَتَخْلُقُونَ إِفْكًا, tr:innemâ ta'budûne min dûnillâhi evsânen ve taḣlukûne ifkâ, gloss:siz Allah'ı bırakıp yalnızca putlara tapıyor ve yalan uyduruyorsunuz, source:29:17}. Allah'ın yaratmasını anlatan fiil burada insanın yalan yaratmasını anlatır. Elçiye karşı çıkan ileri gelenler ise aynı suçlamayı tersine çevirir: {ar:إِنْ هَٰذَآ إِلَّا ٱخْتِلَٰقٌ, tr:in hâzâ ille'ḣtilâk, gloss:bu bir uydurmadan başka bir şey değil, source:38:7}. Bir iftiranın dilden dile geçişini de Allah müminlere hitap ederek gösterir: {ar:إِذْ تَلَقَّوْنَهُۥ بِأَلْسِنَتِكُمْ وَتَقُولُونَ بِأَفْوَاهِكُم مَّا لَيْسَ لَكُم بِهِۦ عِلْمٌۭ, tr:iz telakkavnehû bi-elsinetikum ve tekûlûne bi-efvâhikum mâ leyse lekum bihî ilm, gloss:onu dillerinizle birbirinizden alıyor, hakkında bilginiz olmayan şeyi ağızlarınızla söylüyordunuz, source:24:15}. Söz dilden alınır, ağızdan verilir; kökün "yayılan söz" dalının sahnesi budur. Yusuf'un kardeşlerinin hasedi de uydurulmuş bir anlatıya varır: {ar:فَأَكَلَهُ ٱلذِّئْبُ, tr:fe-ekelehu'z-zi'b, gloss:onu kurt yedi, source:12:17}, ve gömlekte sahte kan getirirler: {ar:وَجَآءُو عَلَىٰ قَمِيصِهِۦ بِدَمٍۢ كَذِبٍۢ, tr:ve câû alâ kamîsihî bi-demin kezib, gloss:gömleğinin üstünde yalan bir kanla geldiler, source:12:18}. Babanın cevabı Allah'tan yardım istemektir: {ar:وَٱللَّهُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ, tr:vallâhu'l-musteânu alâ mâ tesıfûn, gloss:anlattığınız şeye karşı yardımı istenecek olan Allah'tır, source:12:18}. Uydurulan söze karşı da söylenecek söz, yönü Allah'a dönük bir sözdür.

Kaynaklar: 113:1 قُلْ ق و ل B005; 113:1 قُلْ ق و ل B007; 113:2 خَلَقَ خ ل ق B007; 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B005; 113:4 ٱلْعُقَدِ ع ق د B007; 113:2 شَرِّ ش ر ر B001; 113:2 شَرِّ ش ر ر B011

## Buluşmalar

Gece ile yarılıp çıkarılış ilk buluşmadır. Sabah, yarılıp çıkarılan şeylerin bir örneğidir: karanlık yarılır ve ışık açığa konur; tohum yarılır ve filiz çıkar. Göğün kuruluşunu anlatan ayet ikisini aynı fiille birleştirir; gece karartılır ve kuşluk dışarı çıkarılır {source:79:29}. Kur'an aynı çıkarılışı insanlar için de söyler: {ar:ٱللَّهُ وَلِىُّ ٱلَّذِينَ ءَامَنُوا۟ يُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ, tr:allâhu veliyyu'llezîne âmenû, yuḣricuhum mine'z-zulumâti ile'n-nûr, gloss:Allah inananların dostudur; onları karanlıklardan aydınlığa çıkarır, source:2:257}. Üçüncü ayetin karanlığına giren kişi, ilk ayetin Rabbine sığındığında bu çıkarılışın içine girer. Gece ile yağmur da birbirine dökülür: gece tepelere bir sıvı gibi boşalır, gök çiseler, ve aynı kök hem gecenin dökülüşünü hem göğün çiselemesini taşır. Felakın iki tepe arasındaki alçak yeri, gecenin döküldüğü tepelerin eteğidir; karanlık da su da oraya iner.

Şafağın iplikleri ile büyücünün iplikleri ikinci buluşmadır. Oruç ayetinde tan, beyaz ipliğin siyah iplikten ayrılmasıdır {source:2:187}; dördüncü ayette ise büyücüler ipliklere düğüm atar. Aynı malzeme iki zıt işleme uğrar: Rabbin sabahı iplikleri birbirinden ayırır, büyücünün eli iplikleri birbirine bağlar. Sure bu iki işlemi baştan ve sondan çerçeveler: ayıran Rab ilk ayettedir, bağlayan el dördüncüde. Musa'nın duasında da bir düğüm çözülür ve söz açığa çıkar {source:20:27} {source:20:28}; düğümü çözen Rab, sözü açılan kul. Böylece düğüm imgesi ile ağız imgesi aynı duada buluşur: dilin düğümü çözüldüğünde ağız konuşur, düğüme üfleyen ağız ise sözü bağlar.

Ağız ile ışık üçüncü buluşmadır. Namaz emrinde gecenin koyulaşmasının ardından sabahın okunuşu gelir {source:17:78}: karanlığın sonunda bir ağız okur. İnkâr edenler ise ağızlarıyla ışığa üfler: {ar:يُرِيدُونَ لِيُطْفِـُٔوا۟ نُورَ ٱللَّهِ بِأَفْوَٰهِهِمْ وَٱللَّهُ مُتِمُّ نُورِهِۦ, tr:yurîdûne li-yutfiû nûrallâhi bi-efvâhihim vallâhu mutimmu nûrih, gloss:Allah'ın nurunu ağızlarıyla söndürmek isterler; Allah ise nurunu tamamlayandır, source:61:8}. Bu ayette üç imge birden durur: ışığa karşı üfleyen ağızlar, söndürülmek istenen ışık ve o ışığı tamamlayan Allah. Düğüme üfleyen ağız ışığa karşı çalışır; emredilen ağız ışığın yanında durur. Işığı tamamlayan, nimeti tamamlayan Rabdir; hasetçinin sökmek istediği nimet ile inkârcının söndürmek istediği ışık aynı "tamamlama" fiiliyle korunur.

Musa'nın denizden geçişi dört imgeyi tek bir sahnede tutar. Gece yürüyüşü emredilir {source:26:52}; ordu güneş doğarken yetişir {source:26:60}; yanındakiler yakalandıklarını söyler {source:26:61}; Musa "Rabbim benimledir" der {source:26:62}; ve deniz felak kökünün fiiliyle yarılır {source:26:63}. Gece, korkulan ordu, Rabbe tutunan bir cümle ve yarılıp açılan bir yol aynı anlatıdadır. Sığınmanın bir uzaklaşma değil bir yakınlık olduğu da burada görünür: Musa'nın sözü "Rabbim benimledir"dir.

İmran'ın karısının kıssası doğum, sığınma ve büyüme imgelerini birleştirir. Rahimdekini adayan anne doğurur, doğurduğunu Rabbe sığındırır ve Rab onu bir bitki gibi büyütür {source:3:36} {source:3:37}. Burada sığınma kökü yeni doğurmuş dişinin adını taşırken, rab kökü hem doğan yavruyu büyütmeyi hem bir şeyi aşama aşama tamamlamayı taşır; tohumdan filiz çıkaran yarma da büyümenin ilk adımıdır. Rabbin bir çocuğu büyütmesi ile bir nimeti tamamlaması aynı köke aittir; Yakup'un Yusuf'a söylediği "nimetini sana tamamlayacak" sözü {source:12:6} bu yüzden doğumla başlayan büyütmenin sonucunu söyler.

Yusuf'un kıssası haset, göz ve uydurulmuş söz imgelerini birbirine bağlar. Bir rüya görülür ve anlatılmaması istenir, çünkü görülen bir nimet kardeşlerde tuzak doğurur {source:12:5}. Babanın yakınlığına bakan kardeşler o yakınlığın kendilerine kalmasını ister {source:12:9}; isteği bir plana, planı bir yalana dönüştürürler {source:12:18}. Hasedin sonucu bir babanın gözlerinde görünür {source:12:84}. Hasetçinin "haset ettiği an", gördüğü nimeti sökmek için harekete geçtiği andır ve bu an kendi arkasından uydurulan bir sözü getirir.

Surenin hareketi bu buluşmalarla görünür hâle gelir. İlk ayetin Rabbi yarar, açar ve çıkarır; ikinci ayette bu çıkarılmış şeylerin bütünü vardır. Üçüncü ayette karanlık dışarıdan içeri girer ve kapatır; dördüncü ayette bir el ipliğin uçlarını bağlar ve bir ağız onu nefesle mühürler; beşinci ayette içeride tutulan bir istek dışarı çıkar ve tamamlanmış bir nimeti sökmeye yönelir. Zarar her seferinde Rabbin işinin tersini yapar: O açarken karanlık kapatır, O ayırırken büyücü bağlar, O tamamlarken hasetçi söker. Sığınılan da sırf bu yüzden, her biri bu ters işlerden birinin karşısında duran "felakın Rabbi"dir. Kapsam da daralarak ilerler: önce bütün yaratılmışlar, sonra bir zaman olarak gece, sonra bir zanaatı olan kadınlar, en sonda tek bir hasetçi ve onun tek bir anı. Bu daralmanın karşısında ilk kelime sabit durur: emredilmiş bir söz, ağızdan çıkıp Rabbe yönelen ve söyleyeni O'na bağlayan bir sığınma.

