# Network for 1:2 (img top-3)

Nodes: Counter({'A': 261, 'B': 37, 'M': 13, 'F': 4}); rare branches 27. Context zones: {'surah': 6, 'fatiha': 1, 'inter': 254}; people anchors: —.
Edges: {'rel': 47, 'lex': 119, 'kw': 294, 'root': 39, 'img': 444, 'hft': 65}.

## Hubs (rare branches of ≥3 roots point here)

### 27:60 [inter] — backbone hub, 3 roots, score 6.0
  أَمَّنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَأَنزَلَ لَكُم مِّنَ ٱلسَّمَآءِ مَآءً فَأَنۢبَتْنَا بِهِۦ حَدَآئِقَ ذَاتَ بَهْجَةٍ مَّا كَانَ لَكُمْ أَن تُنۢبِتُوا۟ شَجَرَهَآ أَءِلَٰهٌ مَّعَ ٱللَّهِ بَلْ هُمْ قَوْمٌ يَعْدِلُونَ
- ر ب ب B012 «belirli bir yeşil bitki türü» ربة نبات (rare, 3 src) @ رَبِّ — lex/src-rare: شجر → شَجَرَهَآ; img/inter: inter: ن ب ت B001 النبات الخارج من الأرض ← فَأَنۢبَتْنَا
- ر ب ب B013 «bol ve toplanmış su» ماء رَبَب كثير (rare, 2 src) @ رَبِّ — lex/image: ماء → مَآءً
- ر ب و B005 «besleyip büyütmek ve yetişmek» تغذية ونشوء (echo rare, 3 src) @ رَبِّ — rel/near_synonym: ن ب ت B006 (besleyip büyütmek ile çocuğun olgunlaşması) → فَأَنۢبَتْنَا تُنۢبِتُوا۟; img/inter: inter: ن ب ت B006 نشوء الإنسان وتربيته ← فَأَنۢبَتْنَا
- ع ل م B005 «deniz ya da suyu bol kuyu» ماء كثير مجتمع في عيلم (rare, 3 src) @ ٱلْعَٰلَمِينَ — lex/image: ماء → مَآءً

## Triangles (top 40)

- [4 kinds] ر ب و B005 «besleyip büyütmek ve yetişmek» تغذية ونشوء (echo rare, 3 src) @ رَبِّ
  - → 27:60 [inter]: rel/near_synonym: ن ب ت B006 (besleyip büyütmek ile çocuğun olgunlaşması) → فَأَنۢبَتْنَا تُنۢبِتُوا۟; img/inter: inter: ن ب ت B006 نشوء الإنسان وتربيته ← فَأَنۢبَتْنَا
  - → ٱلْعَٰلَمِينَ (w4): kw/shared: education (shared) — plain sense of ٱلْعَٰلَمِينَ; img/same: same: ع ل م B001 انكشاف الشيء للعارف
  - 27:60 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B005): ماء → مَآءً
- [4 kinds] ع ل م B005 «deniz ya da suyu bol kuyu» ماء كثير مجتمع في عيلم (rare, 3 src) @ ٱلْعَٰلَمِينَ
  - → 18:109 [inter]: lex/src-rare: بحر → ٱلْبَحْرُ; rel/near_synonym: ب ح ر B001 (deniz ve geniş su) → ٱلْبَحْرُ; kw/shared: sea (shared) → ٱلْبَحْرُ; img/inter: inter: ب ح ر B001 الماء الواسع الكثير ← ٱلْبَحْرُ
  - → رَبِّ (w3): img/same: same: ر ب ب B013 ماء رَبَب كثير
  - 18:109 [inter] ↔ رَبِّ (w3): rel (via ر ب ب B013): ب ح ر B001 (çok miktarda su) → ٱلْبَحْرُ
- [4 kinds] ح م د B004 «övülesi işin varılabilecek en ileri sınırı» حماداك الغاية المحمودة (rare, 6 src) @ ٱلْحَمْدُ
  - → 16:75 [inter]: rel/near_synonym: ح س ن B005 (gücünün ve çabasının sonu) → حَسَنًا; img/inter: inter: ح س ن B005 حُسَيْناء الغاية والجهد ← حَسَنًا
  - → رَبِّ (w3): kw/shared: completion (shared) — plain sense of رَبِّ; img/same: same: ر ب ب B016 رُبَى حاجة وعقدة ونعمة
  - 16:75 [inter] ↔ رَبِّ (w3): lex (via ر ب و B003): اكثر → أَكْثَرُهُمْ
- [3 kinds] ر ب و B007 «baba tarafından yakın hane halkının arasına gelmek» أهل البيت من بني الأعمام (echo rare, 1 src, sole) @ رَبِّ
  - → 71:28 [inter]: lex/image: بيت → بَيْتِىَ; rel/near_synonym: ب ي ت B002 (baba tarafı hane halkı ile genel ev halkı) → بَيْتِىَ
  - → لِلَّهِ (w2): img/same: same: ء ل ه B002 اسم الله في القسم والنداء
  - 71:28 [inter] ↔ لِلَّهِ (w2): lex (via ء ل ه B002): اغفر → ٱغْفِرْ
- [3 kinds] ر ب ب B013 «bol ve toplanmış su» ماء رَبَب كثير (rare, 2 src) @ رَبِّ
  - → 18:109 [inter]: rel/near_synonym: ب ح ر B001 (çok miktarda su) → ٱلْبَحْرُ; img/inter: inter: ب ح ر B001 الماء الواسع الكثير ← ٱلْبَحْرُ
  - → ٱلْعَٰلَمِينَ (w4): img/same: same: ع ل م B005 ماء كثير مجتمع في عيلم
  - 18:109 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B005): بحر → ٱلْبَحْرُ
- [3 kinds] ر ب ب B004 «büyük insan topluluğu» ربة وجماعات كثيرة (rare, 3 src) @ رَبِّ
  - → 14:8 [inter]: rel/near_synonym: ج م ع B002 (toplanmış insan grubu) → جَمِيعًا; img/inter: inter: ج م ع B002 جماعة اجتمعت أو أخلاط ضمتها الجهة ← جَمِيعًا
  - → ٱلْعَٰلَمِينَ (w4): img/same: same: ع ل م B005 ماء كثير مجتمع في عيلم
  - 14:8 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B002): جميع → جَمِيعًا
- [3 kinds] ء ل ه B002 «Yaratıcıya özgü ad ile seslenme ve ant biçimleri» اسم الله في القسم والنداء (rare, 5 src) @ لِلَّهِ
  - → 10:9 [inter]: rel/thematic: ء م ن B003 (yakarışın kabulünü isteyen karşılık) → ءَامَنُوا۟ بِإِيمَٰنِهِمْ
  - → ٱلْعَٰلَمِينَ (w4): img/same: same: ع ل م B001 انكشاف الشيء للعارف
  - 10:9 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B002): ويهدي → يَهْدِيهِمْ
- [3 kinds] ء ل ه B002 «Yaratıcıya özgü ad ile seslenme ve ant biçimleri» اسم الله في القسم والنداء (rare, 5 src) @ لِلَّهِ
  - → 9:112 [inter]: rel/thematic: ء م ن B003 (yakarışın kabulünü isteyen karşılık) → ٱلْمُؤْمِنِينَ
  - → ٱلْعَٰلَمِينَ (w4): img/same: same: ع ل م B001 انكشاف الشيء للعارف
  - 9:112 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B002): معروفا → بِٱلْمَعْرُوفِ
- [2 kinds] ر ب ب B013 «bol ve toplanmış su» ماء رَبَب كثير (rare, 2 src) @ رَبِّ
  - → 27:60 [inter]: lex/image: ماء → مَآءً
  - → ٱلْعَٰلَمِينَ (w4): img/same: same: ع ل م B005 ماء كثير مجتمع في عيلم
  - 27:60 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B005): ماء → مَآءً
- [2 kinds] ر ب ب B013 «bol ve toplanmış su» ماء رَبَب كثير (rare, 2 src) @ رَبِّ
  - → 29:63 [inter]: lex/image: ماء → مَآءً
  - → ٱلْعَٰلَمِينَ (w4): img/same: same: ع ل م B005 ماء كثير مجتمع في عيلم
  - 29:63 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B005): ماء → مَآءً
- [2 kinds] ر ب ب B004 «büyük insan topluluğu» ربة وجماعات كثيرة (rare, 3 src) @ رَبِّ
  - → 27:15 [inter]: lex/image: كثيرا → كَثِيرٍ
  - → ٱلْعَٰلَمِينَ (w4): img/same: same: ع ل م B005 ماء كثير مجتمع في عيلم
  - 27:15 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B005): كثيرا → كَثِيرٍ
- [2 kinds] ر ب ب B012 «belirli bir yeşil bitki türü» ربة نبات (rare, 3 src) @ رَبِّ
  - → 27:60 [inter]: lex/src-rare: شجر → شَجَرَهَآ; img/inter: inter: ن ب ت B001 النبات الخارج من الأرض ← فَأَنۢبَتْنَا
  - → ٱلْعَٰلَمِينَ (w4): img/same: same: ع ل م B002 أثر يميز الشيء ويهدي إليه
  - 27:60 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B005): ماء → مَآءً
- [2 kinds] ر ب ب B012 «belirli bir yeşil bitki türü» ربة نبات (rare, 3 src) @ رَبِّ
  - → 74:31 [inter]: lex/src-rare: لعدا → عِدَّتَهُمْ
  - → لِلَّهِ (w2): img/same: same: ء ل ه B001 التعبد والمعبود
  - 74:31 [inter] ↔ لِلَّهِ (w2): lex (via ء ل ه B002): تريد → أَرَادَ
- [2 kinds] ع ل م B005 «deniz ya da suyu bol kuyu» ماء كثير مجتمع في عيلم (rare, 3 src) @ ٱلْعَٰلَمِينَ
  - → 27:60 [inter]: lex/image: ماء → مَآءً
  - → رَبِّ (w3): img/same: same: ر ب ب B013 ماء رَبَب كثير
  - 27:60 [inter] ↔ رَبِّ (w3): lex (via ر ب ب B012): شجر → شَجَرَهَآ
- [2 kinds] ع ل م B005 «deniz ya da suyu bol kuyu» ماء كثير مجتمع في عيلم (rare, 3 src) @ ٱلْعَٰلَمِينَ
  - → 29:63 [inter]: lex/image: ماء → مَآءً
  - → رَبِّ (w3): img/same: same: ر ب ب B013 ماء رَبَب كثير
  - 29:63 [inter] ↔ رَبِّ (w3): lex (via ر ب ب B006): نحي → فَأَحْيَا
- [2 kinds] ر ب ب B005 «bakımla kurulan üvey aile bağı» ربيب وربيبة ورابة (rare, 4 src) @ رَبِّ
  - → 9:108 [inter]: lex/root: رجل → root ر ج ل: رِجَالٌ; lex/src-rare: يقوم → تَقُمْ تَقُومَ
  - → ٱلْحَمْدُ (w1): img/same: same: ح م د B003 المحمود كثير الخصال
  - 9:108 [inter] ↔ ٱلْحَمْدُ (w1): lex (via ح م د B003): رجل → root ر ج ل: رِجَالٌ
- [2 kinds] ر ب ب B005 «bakımla kurulan üvey aile bağı» ربيب وربيبة ورابة (rare, 4 src) @ رَبِّ
  - → 9:108 [inter]: lex/root: رجل → root ر ج ل: رِجَالٌ; lex/src-rare: يقوم → تَقُمْ تَقُومَ
  - → لِلَّهِ (w2): img/same: same: ء ل ه B001 التعبد والمعبود
  - 9:108 [inter] ↔ لِلَّهِ (w2): lex (via ء ل ه B001): رجل → root ر ج ل: رِجَالٌ
- [2 kinds] ر ب ب B005 «bakımla kurulan üvey aile bağı» ربيب وربيبة ورابة (rare, 4 src) @ رَبِّ
  - → 9:108 [inter]: lex/root: رجل → root ر ج ل: رِجَالٌ; lex/src-rare: يقوم → تَقُمْ تَقُومَ
  - → ٱلْعَٰلَمِينَ (w4): img/same: same: ع ل م B002 أثر يميز الشيء ويهدي إليه
  - 9:108 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B001): رجل → root ر ج ل: رِجَالٌ
- [2 kinds] ر ب و B003 «belirli işlem biçimleriyle sınırlı anapara fazlalığı» زيادة الربا في المعاملة (echo rare, 4 src) @ رَبِّ
  - → 74:31 [inter]: lex/src-rare: يزداد → وَيَزْدَادَ
  - → لِلَّهِ (w2): img/same: same: ء ل ه B002 اسم الله في القسم والنداء
  - 74:31 [inter] ↔ لِلَّهِ (w2): lex (via ء ل ه B002): تريد → أَرَادَ
- [2 kinds] ء ل ه B002 «Yaratıcıya özgü ad ile seslenme ve ant biçimleri» اسم الله في القسم والنداء (rare, 5 src) @ لِلَّهِ
  - → 18:2 [inter]: rel/thematic: ء م ن B003 (yakarışın kabulünü isteyen karşılık) → ٱلْمُؤْمِنِينَ
  - → ٱلْحَمْدُ (w1): img/same: same: ح م د B001 الحمد خلاف الذم
  - 18:2 [inter] ↔ ٱلْحَمْدُ (w1): rel (via ح م د B004): ح س ن B005 (gücünün ve çabasının sonu) → حَسَنًا
- [2 kinds] ر ب ب B015 «azlık bildiren ilgeç» حرف رب وربما (rare, 5 src) @ رَبِّ
  - → 39:29 [inter]: lex/src-rare: رجلا → رَّجُلًا وَرَجُلًا لِّرَجُلٍ
  - → ٱلْحَمْدُ (w1): img/same: same: ح م د B002 وجود الشيء محمودا
  - 39:29 [inter] ↔ ٱلْحَمْدُ (w1): lex (via ح م د B003): رجل → root ر ج ل: رَّجُلًا وَرَجُلًا لِّرَجُلٍ
- [2 kinds] ر ب ب B015 «azlık bildiren ilgeç» حرف رب وربما (rare, 5 src) @ رَبِّ
  - → 39:29 [inter]: lex/src-rare: رجلا → رَّجُلًا وَرَجُلًا لِّرَجُلٍ
  - → لِلَّهِ (w2): img/same: same: ء ل ه B002 اسم الله في القسم والنداء
  - 39:29 [inter] ↔ لِلَّهِ (w2): lex (via ء ل ه B001): رجل → root ر ج ل: رَّجُلًا وَرَجُلًا لِّرَجُلٍ
- [2 kinds] ر ب ب B015 «azlık bildiren ilgeç» حرف رب وربما (rare, 5 src) @ رَبِّ
  - → 39:29 [inter]: lex/src-rare: رجلا → رَّجُلًا وَرَجُلًا لِّرَجُلٍ
  - → ٱلْعَٰلَمِينَ (w4): img/same: same: ع ل م B001 انكشاف الشيء للعارف
  - 39:29 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B001): رجل → root ر ج ل: رَّجُلًا وَرَجُلًا لِّرَجُلٍ
- [2 kinds] ر ب و B001 «artmak veya yükselmek» زيادة وعلو (echo rare, 5 src) @ رَبِّ
  - → 27:14 [inter]: lex/image: وعلو → وَعُلُوًّا
  - → ٱلْعَٰلَمِينَ (w4): img/same: same: ع ل م B001 انكشاف الشيء للعارف
  - 27:14 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B004): عليا → root ع ل و: وَعُلُوًّا
- [2 kinds] ر ب و B002 «yükselmiş arazi» أرض مرتفعة (echo rare, 5 src) @ رَبِّ
  - → 27:14 [inter]: lex/src-rare: علو → وَعُلُوًّا
  - → ٱلْعَٰلَمِينَ (w4): img/same: same: ع ل م B002 أثر يميز الشيء ويهدي إليه
  - 27:14 [inter] ↔ ٱلْعَٰلَمِينَ (w4): lex (via ع ل م B004): عليا → root ع ل و: وَعُلُوًّا
- [2 kinds] ع ل م B004 «üst dudak yarığı» شق ظاهر في الشفة العليا (rare, 5 src) @ ٱلْعَٰلَمِينَ
  - → 92:20 [inter]: lex/src-rare: اعلي → ٱلْأَعْلَىٰ
  - → رَبِّ (w3): img/same: same: ر ب ب B003 علم رباني
  - 92:20 [inter] ↔ رَبِّ (w3): lex (via ر ب و B003): وجه → وَجْهِ
- [2 kinds] ح م د B004 «övülesi işin varılabilecek en ileri sınırı» حماداك الغاية المحمودة (rare, 6 src) @ ٱلْحَمْدُ
  - → 18:2 [inter]: rel/near_synonym: ح س ن B005 (gücünün ve çabasının sonu) → حَسَنًا
  - → لِلَّهِ (w2): img/same: same: ء ل ه B002 اسم الله في القسم والنداء
  - 18:2 [inter] ↔ لِلَّهِ (w2): rel (via ء ل ه B002): ء م ن B003 (yakarışın kabulünü isteyen karşılık) → ٱلْمُؤْمِنِينَ

## Convergence (rare branches by kinds of support; top 40)

- 5 kinds, 21 targets: ر ب و B005 «besleyip büyütmek ve yetişmek» تغذية ونشوء (echo rare, 3 src) @ رَبِّ — hft, img, kw, lex, rel
- 5 kinds, 19 targets: ع ل م B005 «deniz ya da suyu bol kuyu» ماء كثير مجتمع في عيلم (rare, 3 src) @ ٱلْعَٰلَمِينَ — hft, img, kw, lex, rel
- 5 kinds, 13 targets: ر ب ب B013 «bol ve toplanmış su» ماء رَبَب كثير (rare, 2 src) @ رَبِّ — hft, img, kw, lex, rel
- 4 kinds, 26 targets: ء ل ه B002 «Yaratıcıya özgü ad ile seslenme ve ant biçimleri» اسم الله في القسم والنداء (rare, 5 src) @ لِلَّهِ — img, kw, lex, rel
- 4 kinds, 25 targets: ر ب و B003 «belirli işlem biçimleriyle sınırlı anapara fazlalığı» زيادة الربا في المعاملة (echo rare, 4 src) @ رَبِّ — img, kw, lex, rel
- 4 kinds, 23 targets: ر ب ب B005 «bakımla kurulan üvey aile bağı» ربيب وربيبة ورابة (rare, 4 src) @ رَبِّ — img, kw, lex, rel
- 4 kinds, 19 targets: ح م د B004 «övülesi işin varılabilecek en ileri sınırı» حماداك الغاية المحمودة (rare, 6 src) @ ٱلْحَمْدُ — img, kw, lex, rel
- 4 kinds, 15 targets: ر ب ب B009 «başlangıçtaki tazelik» شاة رُبّى وحداثة (rare, 3 src) @ رَبِّ — img, kw, lex, rel
- 4 kinds, 15 targets: ر ب ب B011 «bağlayıcı söz ve güvence» ربابة عهد وميثاق (rare, 5 src) @ رَبِّ — hft, img, kw, lex
- 4 kinds, 14 targets: ر ب و B007 «baba tarafından yakın hane halkının arasına gelmek» أهل البيت من بني الأعمام (echo rare, 1 src, sole) @ رَبِّ — img, kw, lex, rel
- 4 kinds, 14 targets: ر ب ب B004 «büyük insan topluluğu» ربة وجماعات كثيرة (rare, 3 src) @ رَبِّ — img, kw, lex, rel
- 3 kinds, 21 targets: ر ب ب B015 «azlık bildiren ilgeç» حرف رب وربما (rare, 5 src) @ رَبِّ — img, kw, lex
- 3 kinds, 19 targets: ر ب و B001 «artmak veya yükselmek» زيادة وعلو (echo rare, 5 src) @ رَبِّ — img, kw, lex
- 3 kinds, 18 targets: ع ل م B004 «üst dudak yarığı» شق ظاهر في الشفة العليا (rare, 5 src) @ ٱلْعَٰلَمِينَ — img, kw, lex
- 3 kinds, 15 targets: ر ب ب B012 «belirli bir yeşil bitki türü» ربة نبات (rare, 3 src) @ رَبِّ — img, kw, lex
- 3 kinds, 15 targets: ر ب و B004 «soluğu yükselip sıkışmak» تصعد النفس وانتفاخه (echo rare, 5 src) @ رَبِّ — img, kw, lex
- 3 kinds, 11 targets: ر ب ب B008 «katmanlı asılı bulut kümesi» رباب السحاب (rare, 4 src) @ رَبِّ — hft, img, kw
- 3 kinds, 11 targets: ر ب ب B006 «koyu öz veya yağ tortusu» رُبّ خاثر وإصلاح به (rare, 5 src) @ رَبِّ — img, kw, lex
- 3 kinds, 10 targets: ر ب و B002 «yükselmiş arazi» أرض مرتفعة (echo rare, 5 src) @ رَبِّ — img, lex, rel
- 2 kinds, 16 targets: ر ب ب B007 «bir yerde kalıp sürme» لزوم وإقامة ودوام (rare, 5 src) @ رَبِّ — img, kw
- 2 kinds, 14 targets: ر ب و B006 «uyluk kökü ve iç yanlardaki iki çıkıntılı et parçası» نتوء أصل الفخذ (echo rare, 2 src) @ رَبِّ — img, kw
- 2 kinds, 12 targets: ع ل م B006 «doğan veya atmaca türü yırtıcı kuş» طائر جارح يسمى العلام (rare, 1 src, sole) @ ٱلْعَٰلَمِينَ — img, lex
- 2 kinds, 12 targets: ح م د B003 «övülen veya birçok övülesi niteliği bulunan kimse» المحمود كثير الخصال (rare, 6 src) @ ٱلْحَمْدُ — img, lex
- 2 kinds, 11 targets: ر ب ب B014 «yaban sığırı sürüsü» رَبْرَب قطيع (rare, 3 src) @ رَبِّ — img, rel
- 2 kinds, 10 targets: ع ل م B007 «erkek sırtlan» ذكر الضباع يسمى العيلام (rare, 2 src) @ ٱلْعَٰلَمِينَ — img, lex
- 2 kinds, 9 targets: ر ب ب B010 «kura oklarını toplayan kap» ربابة تجمع القداح (rare, 5 src) @ رَبِّ — hft, img
- 1 kinds, 10 targets: ر ب ب B017 «gemicilerin başı» رباني الملاحين (rare, 1 src, sole) @ رَبِّ — img

## Bridges (linked to members of two or more hubs)


## Chain material (per hub: surah ayat its members touch, in surah order)

- 27:60 [inter]: 1:1 (ر ب ب B012, ر ب و B005) → 1:4 (ر ب ب B013, ع ل م B005) → 1:5 (ر ب و B005) → 1:6 (ر ب ب B013, ع ل م B005) → 1:7 (ر ب ب B012, ر ب و B005, ع ل م B005)

## Formula groups (other ayat sharing ≥2 focus roots; leaves, not members)


## HFT mechanisms and the hubs they touch

- b1_praise_as_tested_verdict [baseline_models] → —
- b2_stagewise_world_cultivation [baseline_models] → 27:60 [inter]
- b3_worlds_as_legibility_field [baseline_models] → —
- b4_credit_claim_reversal [baseline_models] → —
- c1_named_and_marked_praise [context_deltas] → —
- c2_gestational_lordship [context_deltas] → 27:60 [inter]
- c3_praise_at_the_end_of_account [context_deltas] → —
- c4_praise_performed_as_dependence [context_deltas] → 27:60 [inter]
- c5_worlds_as_navigable_signs [context_deltas] → 27:60 [inter]
- c6_praise_as_differential_diagnosis [context_deltas] → —
- o1_ecological_water_cycle [surprising_valid_outliers] → 27:60 [inter]
- o2_guidance_through_breakage [surprising_valid_outliers] → 27:60 [inter]
- o3_covenantal_bundle_of_worlds [surprising_valid_outliers] → —
