# Agreed family-memory workflow

Status: approved by the user on 2026-10-06. This is the default for subsequent family-memory enrichment assignments. The earlier corpus-retrieval plan remains historical context; its search instructions do not apply to these agents.

## Model and effort allocation

Use GPT-6 Astra with 19 independent agents, one per source family for the complete frozen ayah page. Keep Standard service and Fast disabled. Do not consolidate families by default.

| Effort | Families |
|---|---|
| Max — 10 agents | rivayet, kessaf, bayani, ishari, imami-mutazili, wujuh, meal, historical, academic, poetry |
| High — 9 agents | analytical, classical-coherence, modern-coherence, grammar, qiraat, rhetoric, modern-tafsir, turkish-tafsir, hadith |

The machine-readable default is [MEMORY_WORKFLOW_DECISION.json](MEMORY_WORKFLOW_DECISION.json). Grammar, kıraat, analytical and hadith are candidates for focused max follow-ups when requested or when an authorized run requires a specific unresolved issue to be addressed; this is not an automatic extra pass.

## Assignment and output

Each agent receives the whole frozen prose, including its existing augmentations, a source roster, and an explicit research purpose for its family. It identifies substantial findings internally, considers every roster work against them, and writes connected Turkish literature blocks for each paragraph with relevant recalled material. Preserve connections across paragraphs and distinct positions within a family. Meal research specifically looks for meaning narrowing or shifts, translator choices and consistent translation errors supported by concrete remembered examples.

Agents use training memory only: **no web search, repository search, corpus retrieval, source or dictionary checking, or access to other agents' outputs**. Use fresh contexts with only the necessary task material. Do not inherit the orchestration conversation. Keep each agent's files in its own family/run directory, with separate directories for different models or efforts.

Keep the established `blocks.jsonl` and paragraph `ledger.jsonl` format. Use `no_recall` when there is no substantive recollection. Distinguish remembered author positions from the agent's own application of a method. Attributions remain unverified; no-recall does not establish historical absence or novelty. Do not grade, confirm, correct or rewrite the frozen prose or its lexical foundation.

The parent assembles blocks after the original frozen paragraphs and their augmentations, linking genuinely shared blocks. Assembly must preserve the frozen prose byte for byte. Save native per-agent input, cached input, output and reasoning usage, together with clearly labelled API-equivalent costs.

## Basis and limits

The allocation was approved after the [complete 1:6 high/max comparison](work/1_6/family-memory-benchmark-20261006/ASTRA_19_FAMILY_COMPARISON.md). The observed selected mix costs $26.614194 API-equivalent versus $34.441486 for all-max, a 22.7% saving. These figures exclude parent orchestration and review and are not account billing or a forecast for every ayah.

This is a workflow decision based on one run per family and effort on 1:6. Max often adds source voices, variants and lexical witnesses, but high also recalls material absent from max. The allocation does not establish factual accuracy. Future evidence may justify revising it; retain the approved default until then.
