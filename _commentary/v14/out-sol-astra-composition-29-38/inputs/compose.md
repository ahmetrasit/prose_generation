# Interpretive synthesis from a preserved research archive

Develop the explanation of the focus ayah for a curious Turkish reader with almost no Arabic. The research is
already broad; your task is to make its readings illuminate one another and the ayah. A later writer will receive
your explanation and its selected evidence. You do not write the finished commentary or an inventory report.

Read the focus text and its surrounding movement, then the whole supplied research. Findings and word notes are
proposals, not facts or obligations. The dictionary supplies attested branches; the concordance supplies scoped
usage evidence. Readings may coexist without becoming alternative translations. A proper name, a fixed expression,
a derived noun and the contextual verb need not inherit each other's meaning merely because they share a root
entry. Distinguish the relationship the source attests from the relationship your interpretation proposes.

Let candidate images form and strengthen their parts before deciding what they contribute. Then work out the
actual explanatory relationships: how one reading changes, completes, limits or reverses another, and what becomes
perceptible in the ayah as a result. Physically arranging several objects is not sufficient by itself. Establish
the consequence for this ayah's action, relationships, movement or address to its reader.

Write that integrated explanation in connected analytical prose. Do not supply a root tour, a list of promising
images, a paragraph assignment for each finding, or an outline that leaves the difficult connections to the writer.
The explanation must already carry those connections. Its order and emphasis should arise from the understanding
being developed. Several readings may converge; there is no predetermined principal image or image count.

Allocate attention by contribution. A passage earns development when losing it would remove a consequential part
of the understanding. Repeated evidence may be compressed; a distinct supported surprise must not be discarded
merely for being unusual. Material can remain in the research archive without appearing in this ayah's prose.
The archive is retained automatically. You owe no row, reason or eventual publication promise for every unused ID.
Do not try to maximize represented branches, findings, parallels, quotations or source families.

Turkish losses, significant grammar and Quran-loaded usage belong where they change the explanation. QeQ tests,
clarifies or extends the developing reading; it is not a second survey beside it. Keep genuine counter-evidence
and the limits of the supplied evidence. Use the logged source helper to read exact Quran passages and sufficient
context before developing cross-references. Never read prior target prose, evaluations, the North Star or other
repository material. No external research or invented sources.

There is no length target. Supply enough reasoning to make the selected relationships work, then stop. The task
is neither a compressed paraphrase nor a compendium. The reader's changed understanding is the criterion.

Return only one JSON object, with exactly these fields:

    {
      "schema": 1,
      "ref": "the supplied S:A",
      "explanation": "Connected analytical prose containing the completed reasoning, in English or Turkish.",
      "reader_change": "What the reader can now understand about this ayah that the plain paraphrase left unheard.",
      "source_items": ["actual research IDs supporting that explanation"],
      "branches": ["exact spaced Arabic root plus Bnnn for lexical evidence the writer needs"],
      "quran_refs": ["individual S:A references the writer needs"],
      "concordance_roots": ["exact spaced roots whose usage evidence the writer needs"],
      "limits": ["Material qualifications or unresolved evidence limits affecting the selected explanation"]
    }

The evidence lists select sources for the handover, not a worklist for prose. Select the evidence actually needed
for the explanation and its qualifications. Unselected research stays available through the helper. Do not repeat
every record in these fields, grade your output, assert completeness or manufacture omissions to fill the schema.
