import json
CALL = '/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap.103_1.opus.high/'
p = json.load(open('/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/discovery/s103-20261009/prefetch.json'))
page = [
 'Didache 1:5 (prefetch gap; not in intertext corpus)',
 'Didache 4:5 (prefetch gap; not in intertext corpus)',
 'Didache 8:3 (prefetch gap; not in intertext corpus)',
 'Gregory of Tours, Glory of the Martyrs 1.95 (prefetch gap; patristic Latin texts not in corpus)',
 'Gregory of Tours, Glory of the Martyrs 94 (prefetch gap)',
 'Protevangelium of James 8 (prefetch gap; Christian apocrypha not in corpus)',
 'Tertullian, On Prayer 25 (prefetch gap; patristic texts not in corpus)',
 '1 Maccabees 2:31 (prefetch gap)',
 '1 Maccabees 2:38 (prefetch gap)',
 'Tobit 4:9 (prefetch gap)',
 'Tobit 4:7 Greek witness (SEFARIA:Book_of_Tobit.4.7 is a Hebrew version with different content)',
 'Sirach 4:31 Greek witness (SEFARIA:Ben_Sira.4.31 Hebrew text carries a different saying)',
 'Babylonian Talmud, Berakhot 26b and Babylonian Talmud, Ta\'anit 23a under these names (prefetch gap; resolved through SEFARIA:Berakhot.26b and SEFARIA:Taanit.23a)',
 'Jacob of Serugh, memra on the Sleepers of Ephesus (Syriac homilies not in corpus)',
 'Peshitta (Syriac Bible) for Genesis 40:11 and Genesis 41 (not in corpus)',
 'Septuagint (Greek Old Testament) for Genesis 40-41, Ben Sira (not in corpus)',
 'Targum Onkelos and Targum Pseudo-Jonathan on Genesis 40:11, 41:49 (not fetched)',
 'Rashi on Genesis 40:11 and on Leviticus 23:36 (not fetched)',
 'Jerusalem Talmud Taanit 3:9 (Honi cave-sleep variant; not fetched)',
 'Patristic commentary on Psalm 90:4 beyond 2 Peter (not in corpus)',
]
missing = page + ['prefetch: ' + m for m in p['missing']]
gaps = {
 'missing_sources': missing,
 'not_found': [
  'SEFARIA:Rashi_on_Leviticus.23.36',
  'SEFARIA:Onkelos_Genesis.40.11',
  'SEFARIA:Targum_Jonathan_on_Genesis.40.11',
  'SEFARIA:Rashi_on_Genesis.40.11',
  'SEFARIA:Onkelos_Genesis.41.49',
  'SEFARIA:Ben_Sira.4.30',
  'SEFARIA:Ben_Sira.4.32',
  'SEFARIA:Book_of_Tobit.4.8',
  'SEFARIA search for the Aramaic form ועצרית returned no result',
 ],
 'unresolved': [
  'Didache 1:5 (memory-only block S103-INC-MTF-010)',
  'Didache 4:5 (memory-only block S103-INC-MTF-010)',
  'Gregory of Tours, Glory of the Martyrs 1.95 (memory-only block S103-INC-PRL-001)',
  'Gregory of Tours, Glory of the Martyrs 94 (memory-only block S103-INC-PRL-001)',
  'Sirach 4:31 (memory-only block S103-TEV-MTF-016)',
  'SEFARIA:Onkelos_Genesis.40.11 (memory-only block S103-TEV-SYD-003: Onkelos renders שׂחט with Aramaic עצר)',
 ],
 'prefetch_limitation': p.get('limitation'),
 'notes': [
  'Verse numbering resolved: reader refs WLC:Dan.6.10 -> WLC:Dan.6.11; WLC:Ps.141.3 -> WLC:Ps.141.2; WLC:Ps.90.5 -> 90.4; WLC:Ps.90.7 -> 90.6; WLC:Ps.90.11 -> 90.10; Joel 4:13 is KJV 3:13.',
  'Wording findings reviewed: עצר absent from the main text of Lev 23:36, Joel 1:14/2:15 (noun עֲצֶרֶת/עֲצָרָה), 1Kgs 8:35 (בְּהֵעָצֵר), Gen 16:2, 20:18, Isa 66:9, Job 12:15, Deut 11:17, 1Sam 21:8, 2Kgs 4:24, Judg 13:15, Num 17:13, 2Chr 7:13 reflects inflected forms of the root, confirmed with hebrew.py root; צבר in Gen 41:49, Job 27:16, Ps 39:7 likewise appears as יצבר.',
 ],
}
json.dump(gaps, open(CALL + 'gaps.json', 'w'), ensure_ascii=False, indent=1)
print(len(missing))
