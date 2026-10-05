// Run after sample_pdfs.py. This is an OCR pilot, never an ingestion command.
// Dependencies/models are local under .scratch/ocr-reliability-20261005/.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '../../../..');
const scratch = path.join(root, '.scratch/ocr-reliability-20261005');
const { createWorker } = require(path.join(scratch, 'node_modules/tesseract.js'));
const samples = JSON.parse(fs.readFileSync(path.join(__dirname, 'samples.json')));
const sha = data => crypto.createHash('sha256').update(data).digest('hex');
const languages = {
  BINTSHATI: 'ara', KHULI: 'ara', 'FARAHI-NIZAM': 'ara',
  'IBNKHALAWAYH-MUKHTASAR': 'ara', 'MUQATIL-WUJUH': 'ara',
  'ISLAHI-TADABBUR': 'urd', TARAMA: 'tur+ara', 'MEAL-AKDEMIR': 'tur+ara',
  'NOLDEKE-GDQ': 'deu+ara', 'BADAWI-HALEEM': 'eng+ara',
  'SINAI-KEYTERMS': 'eng+ara', 'ZAMMIT-COMPARATIVE': 'eng+ara',
};

async function main() {
  const results = [];
  const models = Object.fromEntries(['ara', 'urd', 'tur', 'eng', 'deu'].map(lang => {
    const data = fs.readFileSync(path.join(scratch, 'tessdata', `${lang}.traineddata`));
    return [lang, { bytes: data.length, sha256: sha(data) }];
  }));
  let worker, current;
  try {
    const jobs = [];
    for (const file of samples.files) {
      for (const sample of file.samples.filter(s => s.image)) {
        if (file.source === 'TARAMA') {
          const mid = Math.floor(sample.image.width / 2);
          for (const [side, left, width] of [['left', 0, mid], ['right', mid, sample.image.width - mid]]) {
            jobs.push({ file, sample, side, rectangle: { left, top: 0, width, height: sample.image.height } });
          }
        } else jobs.push({ file, sample, side: 'whole' });
      }
    }
    jobs.sort((a, b) => languages[a.file.source].localeCompare(languages[b.file.source]));
    for (const { file, sample, side, rectangle } of jobs) {
      const lang = languages[file.source];
      if (lang !== current) {
        if (worker) await worker.terminate();
        worker = await createWorker(lang, 1, {
          langPath: path.join(scratch, 'tessdata'), gzip: false, cacheMethod: 'none',
          workerPath: path.join(__dirname, 'ocr_worker.cjs'),
        });
        await worker.setParameters({ tessedit_pageseg_mode: '3', user_defined_dpi: '300' });
        current = lang;
      }
      const started = Date.now();
      const { data } = await worker.recognize(path.join(root, sample.image.path),
        rectangle ? { rectangle } : {}, { text: true, blocks: true, tsv: true });
      const base = path.join(root, sample.image.path.replace('.300dpi.png', `.${side}.tesseract`));
      fs.writeFileSync(`${base}.txt`, data.text);
      fs.writeFileSync(`${base}.json`, JSON.stringify(data));
      const words = (data.tsv || '').split('\n').slice(1).map(line => line.split('\t'))
        .filter(c => c[0] === '5' && c.length >= 12 && c.slice(11).join('\t').trim());
      const row = {
        source: file.source, pdf: file.path, pdf_sha256: file.sha256,
        pdf_page: sample.pdf_page, region: side, rectangle: rectangle || null,
        image: sample.image, language: lang, psm: 3, engine_mode: 1,
        elapsed_seconds: (Date.now() - started) / 1000,
        chars: data.text.length, words: words.length,
        engine_confidence: data.confidence,
        words_below_80: words.filter(c => Number(c[10]) < 80).length,
        warning: 'Engine confidence is not an accuracy measurement. This page has not passed a quotation-quality gate.',
        text_path: path.relative(root, `${base}.txt`), text_sha256: sha(data.text),
        layout_path: path.relative(root, `${base}.json`),
      };
      results.push(row);
      console.log(`${file.source} ${side}: ${row.chars} chars; confidence ${row.engine_confidence}; ${row.elapsed_seconds}s`);
      fs.writeFileSync(path.join(__dirname, 'ocr_results.json'), JSON.stringify({
        schema_version: 1, created_at: new Date().toISOString(),
        status: results.length === jobs.length ? 'pilot_complete' : 'pilot_running',
        tesseract_js: require(path.join(scratch, 'node_modules/tesseract.js/package.json')).version,
        tesseract_js_core: require(path.join(scratch, 'node_modules/tesseract.js-core/package.json')).version,
        core_variant: 'SIMD; relaxed SIMD disabled for float-model crash documented in upstream issue 1080',
        models_repository: 'https://github.com/tesseract-ocr/tessdata_best',
        models_commit: 'e12c65a915945e4c28e237a9b52bc4a8f39a0cec', models,
        results,
      }, null, 2) + '\n');
    }
  } finally {
    if (worker) await worker.terminate();
  }
}
main().catch(error => { console.error(error); process.exitCode = 1; });
