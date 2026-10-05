// Scoped workaround for https://github.com/naptha/tesseract.js/issues/1080.
// The v7 relaxed-SIMD build crashes with floating-point tessdata_best models.
// Only this pilot worker's feature detection is changed, not installed packages.
const path = require('node:path');
const modules = path.resolve(__dirname, '../../../../.scratch/ocr-reliability-20261005/node_modules');
const features = require.resolve('wasm-feature-detect', { paths: [modules] });
const detector = require(features);
require.cache[features].exports = { ...detector, relaxedSimd: async () => false };
require(path.join(modules, 'tesseract.js/src/worker-script/node/index.js'));
