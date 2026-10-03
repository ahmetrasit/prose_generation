# Stage 6 — onarim: apply the audit

Apply every fix in the audit's review.json to the records. Verify each fix against its sources before applying it
(`corpus.py get`); if a fix is wrong, do not apply it and say why. Add the missing blocks the audit asks for (with
your own research where it gives only a pointer), apply novelty changes, add duzeltme blocks for the errata.
Change nothing the audit did not ask for, except what a fix forces (ids, placement).

Write the full corrected annotations.jsonl into your stage directory, validate it
(`python3 enrichment/v2/validate.py --surah N --annotations <stage>/annotations.jsonl --out /nonexistent`) until it
passes, and write applied.json: [{"fix": index in review.json, "status": "applied"|"rejected", "why": …}].
Final message: applied / rejected counts and every rejection with its reason.
