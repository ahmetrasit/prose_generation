# Worked authoring examples

Read [input.md](input.md), then the [grammar](grammar-output.json),
[semantics](semantics-output.json), and [mapping](mapping-output.json) candidates,
then [page-output.json](page-output.json). These are authored worked examples using
unchanged real commentary excerpts, actual QAC records and dictionary branch/gloss
content. They are not claimed results of three live model calls or an exhaustive
scan of the entire 1:6 page.

All three engines cover both assigned paragraphs, p09 and p12. This makes their
assembly a complete three-perspective example for that bounded input. Independent
production should still discover its own worthwhile observations without a quota.

For the 1:1 particle lesson, “bi- ilişki kurar” needs an explanation of that relation:
“بِسْمِ (bi-smi) sözünde ism ‘ad’dır; bi- burada ‘ile’ ilişkisini ekleyerek ‘adıyla’
anlamını kurar. Türkçe bu ilişkiyi ad-ıyla sözünün sonunda, Arapça ise bi-ism sözünün
başında gösterir.” This uses the familiar Turkish suffix to explain the Arabic
particle's contribution and position, rather than leaving the reader to infer them
from the whole phrase's translation. The observation belongs to word parts and the
local bi- relation (`ML:C001`, `ML:C184`); it does not make every bi- mean “ile.”

[bi-lesson-family.md](bi-lesson-family.md) develops that starting expression into
separate lessons on use, case, translation boundaries, Quranic comparisons and
the special kafā bi-llāh construction. It shows the intended breadth through
actual teaching sentences and sourced examples, without a lesson quota.

## Editorial decisions

- The grammar imperative/prayer candidate and the mapping prayer-function candidate
  teach substantially the same observation. Assembly keeps the grammar identity,
  records the absorbed mapping ID, and retains three taught concepts spanning grammar,
  discourse and Turkish mapping. No single primary concept is chosen.
- Object -nâ and the contrast between acting “we” and receiving “us” are retained
  separately: recognizing the suffix and comparing participant roles add different
  learning value. Both can be read without seeing the other first.
- The common n- in two fiils and their different roots is retained alongside the
  person lesson. It teaches why an inflectional resemblance does not establish a
  word family. It is not merged merely because the same words appear.
- A branch's general road meaning and its straight-road specialization remain
  distinct. The dictionary's qualified identity is respected.
- The mapping lesson uses the actual narrowing profile but checks the entire local
  expression: the adjective already supplies the straightness. It teaches a gloss
  distinction and an adjective relation in one coherent observation, without calling
  a contextually adequate short translation wrong.
- Dictionary pronunciation variants do not by themselves identify a specific Quranic
  qiraat witness. That opportunity stays in deferred and is absent from displayed
  lessons. The supported lexical-variant observation remains teachable.
- Reading the word in isolation versus in connection with its adjective accounts for
  the displayed final vowel. This is not explained as a root difference.
- Assembly replaces unexplained “nesne zamiri” and “nasb uyumu” with the local
  participant relation and visible word features. The adjective lesson retains its
  noun/adjective and agreement annotations; the now-unneeded background reminders
  are removed. The pause/connection lesson drops the nasb claim and its annotation,
  so its level becomes 1. The engine drafts show the wording before these edits.

The evidence-gap exercise has its own [input](deferred-input.md) and
[output](deferred-output.json). It illustrates retaining an exact unresolved question
and resuming that candidate alone when the missing source is supplied.

## Learner state

[learner-state.json](learner-state.json) marks the root/word distinction learned,
the object suffix learning, and one specific lesson seen. The root concept's
reminders are suppressed, but a new lexical lesson using that concept remains
available. The independently muted C017 helpful message does not establish C017
mastery or mute its required variant. The object-suffix state is not automatically
upgraded because its lesson was displayed.

Concept annotations are many-to-many throughout. The same concept can recur in
several lessons; a lesson can belong to several categories. Array order of annotations
does not imply priority. A `contrasts` annotation is used only when the wording
actually contrasts that curriculum concept, not simply because two words differ.
