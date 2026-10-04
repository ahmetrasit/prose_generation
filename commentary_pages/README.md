# Commentary Pages reader

Static, public reader for generated Qur'an commentary prose.

## Design

- `build.py` scans every `_commentary/vN` directory that exists at build time. A newly pushed `v9`, `v17`, etc. is discovered automatically.
- Only prose-shaped Markdown inside output/result trees is published. Prompts, runbooks, logs, ledgers, raw responses, checks, packets and partial outputs are excluded.
- Accepted enrichment pages from every `enrichment/vN/out` directory are included.
- The newest `enrichment/vN/schema.json` is copied into the site. The browser builds annotation fields and enum filters from that schema and also learns legacy fields from the document being viewed.
- Display preferences are stored only in the reader's browser `localStorage`.
- Comparison mode shows two versions of the same surah/ayah with the same display settings.

## Local validation

```bash
python3 commentary_pages/test_build.py
cat commentary_pages/app.part*.jsfrag > /tmp/commentary-app.js
node --check /tmp/commentary-app.js
python3 commentary_pages/build.py --root . --output commentary_pages/_site
```

The generated `_site/` directory is a build artifact and should not be committed.
