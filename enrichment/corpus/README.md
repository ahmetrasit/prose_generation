# Enrichment corpus (shared, local)

Every source the enrichment workflow may cite lives here, one directory per work, under a short
upper-case work ID (`TAB`, `RAZI`, `MEAL-OKUYAN`, `ELMALILI` …). Bulk data is git-ignored (see `.gitignore`);
only `source.json` is versioned. The older `enrichment/v1/corpus/` (16 tafsirs for 86:17–114, hadith) is read
in place through adapters; nothing there is moved.

## Contract for every source directory

```
enrichment/corpus/<ID>/
  source.json        identity and provenance (versioned)
  segments.jsonl     the searchable text, one JSON object per line (git-ignored)
  raw/               downloads exactly as fetched (git-ignored)
```

### `source.json`

```json
{
  "id": "TAB",
  "title": "Jāmiʿ al-bayān ʿan taʾwīl āy al-Qurʾān",
  "author": "al-Ṭabarī",
  "death_ah": 310,
  "kind": "tafsir | hadith | lexicon | maani | wujuh | qiraat | ulum | nazm | isari | meal | translation | tafsir_tr | reference | poetry | sira | modern",
  "tradition": "free text: sunni-rivaya, mutazili, imami, ishari, bayani, reformist, ottoman, academic …",
  "language": "ar | tr | en | de",
  "edition": "what edition / version the text is, as far as known",
  "access": "yerel | hafiza",
  "locator": "ayah | page | hadith | entry | section",
  "coverage": "e.g. 1-114 | 86:17-114:6 | 93,94,99,… | whole book",
  "urls": ["where it was fetched from"],
  "fetched_at": "ISO date",
  "files": {"raw/…": "sha256"},
  "lineage": "optional: shared lineage, e.g. diyanet-1 for DİB current / TDV / Kur'an Yolu",
  "relay": "optional: source text a translation was made from, e.g. ASAD-EN",
  "licence": "terms as stated by the host; local research copy only",
  "notes": "identity caveats, misattributions found, merged verse groups, OCR quality …"
}
```

`access: hafiza` is a pointer to a work that is not held locally (licensed books such as Neuwirth or Sinai).
It has a `source.json` and no `segments.jsonl`; anything cited from it is model memory and is marked so.

### `segments.jsonl`

One object per searchable unit, in reading order:

```json
{"seg": "TAB:107:3", "s": 107, "a": 3, "a_end": 3, "page": null, "head": "optional heading/lemma", "text": "…"}
```

- `seg` is the citation locator used in annotation blocks: `<ID>:<surah>:<ayah>` for per-ayah sources,
  `<ID>:p<page>` (or `<ID>:v<vol>p<page>`) for paginated books, `<ID>:<book>:<number>` for hadith,
  `<ID>:<entry>` for lexicon entries (root or headword in Arabic script). It must be unique within the source.
- `s`, `a`, `a_end` are filled whenever the unit is tied to an ayah or ayah range (merged verse groups:
  `a`..`a_end`, the text once, never copied into each ayah). Leave them null when unknown.
- `text` is clean UTF-8 text. Arabic stays in logical order; when a PDF's Arabic extraction is unreliable,
  say so in `source.json.notes` and keep the Turkish/English text intact.

`enrichment/v2/tools/corpus.py` builds one full-text index over all `segments.jsonl` files and serves
`get` (by locator) and `search` (by words, with source filters).
