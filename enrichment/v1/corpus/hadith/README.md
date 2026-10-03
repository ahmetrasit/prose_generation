# Hadith corpus (whole books, ara/eng/tur)

Source: fawazahmed0/hadith-api, edition files fetched from
https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/<lang>-<book>.json
(sunnah.com is behind a Cloudflare challenge and returns 403 to scripted requests.)
Fetched 2026-10-02. Books: bukhari muslim abudawud tirmidhi nasai ibnmajah malik.

Caveats
- Numbering follows this dataset's `hadithnumber`/`arabicnumber`; it can differ from sunnah.com or
  other editions (e.g. Muslim). Cite book + dataset number and quote the opening words of the matn.
- `grades` is filled only where the dataset carries them (see below); it is a secondary label.
  Protocol rule: never record a grade unless it was actually checked; otherwise `not_assessed`.
- Turkish text is the dataset's translation (translator not identified here).
- Musnad Ahmad, Bayhaqi, Tabarani etc. are not included.

## Search
- `python3 build_index.py` builds `hadith.sqlite` (FTS5; Arabic normalized, plus English and Turkish columns).
- `python3 search.py 'رياء' [--lang ara|eng|tur] [--book bukhari] [--n 10] [--chars 300] [--exact]`
- `python3 search.py --get bukhari 6499` prints one hadith in full (ar/en/tr, reference, grades).
- Matching is by word prefix, not by root: search each spelling variant (مراء, رياء, يراءون ...).
- Dataset numbers are not sunnah.com numbers (e.g. Muslim #2986 here is a different hadith than on sunnah.com).
