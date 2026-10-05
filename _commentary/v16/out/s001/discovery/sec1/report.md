# S1 first-image discovery test — 2026-10-04

Tested only section 1, **Çiğnenmiş yol: önden giden kılavuz, yolun ortası, nişanlar ve yolu bulamayan**.
The section serves five S1 ayat, names nine roots and has eight commentary paragraphs.
The Codex orchestrator directly spawned **gpt-6-luna/max** and **gpt-5.6-terra/max** with no inherited conversation,
then sent the fixed follow-up itself to the same agent for each model. Two agents, two turns each; no script launched a model call.
The remaining thirteen sections have not started. No Opus run was prepared or launched.

| Model | Initial ayat | Follow-up additions | Final ayat | Status | Check |
|---|---:|---:|---:|---|---|
| Luna | 262 | 192 | 454 | ok | findings |
| Terra 5.6 | 332 | 199 | 531 | ok | ok |

The first-turn union contained **446** distinct ayat, with **148** named by both.
The final union contains **745**, with **240** named by both,
**214** unique to Luna and **291** unique to Terra.
The follow-ups introduced **299** ayat absent from both first-turn lists.
Both models rediscovered all **16** outside-S1 citations already present in the commentary section.
This measures coverage of those known citations; it does not establish exhaustive Quran-wide recall or relevance.

The merged tiers are **450 strong, 235 medium, 55 weak and 5 contrast**.
Luna labelled all **192** follow-up additions strong. Terra labelled its follow-up additions **94 strong, 79 medium and 26 weak**.
The merged tier is the strongest label either model assigned; it is a discovery judgement for the subsequent verdict pass.

All final rows satisfy the four-field schema and reference existing ayat outside S1. Neither final list contains duplicate references.
Each final list preserves its saved first-turn list as an unchanged prefix. The merge retains both models' labels,
explanations and first-turn/follow-up provenance. The two follow-ups used no file reads, retrieval or discovery scripts;
Luna wrote through two append-only shell writes and Terra wrote through the patch tool.

## Findings for review

Luna reread its own TSV in five first-turn tool calls while checking and repairing its output.
This went beyond the package-only read boundary included in its initial agent message. It did not read other run files or external sources.
One first-turn repair command raised **SyntaxError: unterminated string literal (detected at line 4)**;
Luna recovered, split a range into single-ayah rows, removed duplicate references and produced a schema-valid first-turn list.
These findings remain in Luna's run log and tool-call audit; its ledger row has `status: ok`, `check: findings`.
Terra's run has `status: ok`, `check: ok` and no recorded tool diagnostics.

Two explanation spot checks found concrete wording errors in Luna's output:

- **20:53:** its explanation quotes **تَهْتَدُوا**, which is absent from that ayah's canonical Arabic in the repository.
  Terra's explanation instead describes the paths and water actually named there.
- **4:118:** its explanation says Satan curses himself; the Arabic **لَّعَنَهُ ٱللَّهُ** names God as the one who curses him.

The model-written lists and explanations have been preserved without hand correction.
These checks do not constitute a full semantic review. The later Opus packet supplies canonical Arabic independently of the discovery explanations.

## Costs and recorded usage

Discovery estimate **$0**, recorded actual **$0**, for each model and in total, on the Codex subscription.
Usage comes from each agent's native session record; input includes cached input, and output includes reasoning output.

| Model | Input tokens | Cached input subset | Output tokens | Reasoning output subset | Total tokens | Agent elapsed |
|---|---:|---:|---:|---:|---:|---|
| Luna | 664,179 | 513,280 | 64,280 | 43,228 | 728,459 | 21.4 min |
| Terra 5.6 | 1,030,794 | 799,744 | 94,308 | 63,896 | 1,125,102 | 32.9 min |

The fixed follow-up text was:

> tell me if there are any missing ayah that should be in this list - do not read any files or run any scripts. be comprehensive & exhaustive. append your findings to the TSV file following the same schema

The native parent session records one follow-up delivery to each same agent.
Message bodies are encrypted on disk; the run logs retain the exact plaintext sent by the orchestrator and the delivery call IDs.
The audit was corrected to recognise append-only file writes and to find follow-up delivery in the parent record.
No extra model turns or reruns were made.

## Handoff dry build

The section-1 Opus build reads **745 discovered ayat plus 30 neighbours: 775 passages** for paragraphs 1–8.
It estimates **150,510 input tokens** and **$7.82 nominal cost** under the existing script's rates and output allowance.
This was a read-only build; no Opus guard, output directory or model call was created.

The source commentary is unchanged; SHA-256: `782be8c16d10f4684dc7f79db8acefd312f3ca466c57cffa1c3ce02d6429dea7`.
The S1 status check also reports existing reading findings: 1:2 has one unverified source, 1:4 has one process line,
and 1:6 has two process lines. These are outside this discovery test.

## Artifacts

- [Merged discovery list](../sec1.merged.tsv)
- [Full comparison data](comparison.json)
- [Luna final list](luna/list.tsv), [first-turn snapshot](luna/turn1.list.tsv), [run log](luna/run.log.json), [tool audit](luna/tool_calls.json)
- [Terra final list](terra/list.tsv), [first-turn snapshot](terra/turn1.list.tsv), [run log](terra/run.log.json), [tool audit](terra/tool_calls.json)
