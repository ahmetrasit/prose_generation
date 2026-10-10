import json
D = '/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap.103_3.opus.high.a2/'
P = json.load(open('/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/discovery/s103-20261009/prefetch.json', encoding='utf-8'))
page = ['1 Clement 34:2', '1 Clement 38.1-2', '1 Clement 38:2', 'Didache 1:3', 'Didache 4.1', 'Didache 4.2',
        'Ignatius, Letter to Polycarp 1:2', 'Ignatius, Letter to Polycarp 3:1', 'Justin Martyr, First Apology 67',
        'Shepherd of Hermas, Mandate 5.1', 'Tertullian, Apology 39', '1 Maccabees 2:50', '2 Maccabees 7:2',
        'Sirach 29:15', 'Targum Onkelos on Genesis 15:6']
missing = [
 'Peshitta (Syriac Old and New Testament): not in the intertext corpus; Syriac cognates of ʾmn, ṣbr, ḥqq, wṣy not checked',
 'Septuagint: not in the corpus; the Greek of Hab 2:3-4 behind Heb 10:37-38 not compared',
 'Patristic and Syriac homiletic texts (Ephrem, Jacob of Serugh, Church Fathers): not in the corpus; no Christian reading of Gen 15:6, Hab 2:4 or 1 Thess 1:3 cited',
 'Apostolic Fathers (1 Clement, Didache, Ignatius, Hermas), Justin, Tertullian: not in the corpus',
 'Apocrypha in Greek (1-2 Maccabees, Sirach Greek numbering, Wisdom in Greek): not in the corpus; Sefaria gives Ben Sira partly as bracketed reconstruction and Wisdom only in modern Hebrew translation',
 'Targumim on Genesis (Onkelos 15:6, Pseudo-Jonathan 49:2): not in the corpus',
 "Midrash (Genesis Rabbah 98 on Jacob's deathbed) not fetched",
 'Full BDB cognate notes: this lexicon edition is abridged; Arabic cognate notes absent for most roots of the table',
] + ['prefetch gap (discovery list, not in corpus): ' + m + (' [this page]' if m in page else '') for m in P['missing']]
gaps = {
 'missing_sources': missing,
 'not_found': ['SEFARIA:Targum_Jonathan_on_Genesis.49.2 (requested for the deathbed Shema scene; NOT FOUND)'],
 'unresolved': [],
}
json.dump(gaps, open(D + 'gaps.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(missing))
