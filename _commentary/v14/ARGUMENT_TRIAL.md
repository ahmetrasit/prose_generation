# Matched Sol/Astra trial — argument, anchors and partial use

The user authorized the writing changes and rerun, explicitly accepts max effort and this experiment's cost, and
requested Astra 6 max in parallel with Sol 6 max. Two new frozen arms use the same 1:6 evidence, v2 upstream,
full v2 1:5 prose, source corpus and lookup capability. The primary agent compares; the writers never see each
other's output, previous target commentaries or evaluation criteria. One generation per arm, no repair or retry.

- `out-sol-argument`: `gpt-6-sol`, max; initial input 206,599 bytes.
- `out-astra-argument`: `gpt-6-astra`, max; initial input 206,601 bytes.

The only packet difference is the arm tag in the lookup command, needed to attribute source retrieval to the
correct run. After that routing label is normalized, packets must be byte-identical. Tool responses may differ
because the writers choose what to retrieve; report those choices as part of the comparison. This controls the
available input and task, not stochastic variation or hidden compute. One pair cannot establish a universal model
ranking. Billing remains unknown unless the tool provides it; elapsed time and retrieved bytes are recorded.

The writing revision asks for meaningful section turns and sustained consequences between paragraphs, permits
supported new relationships within the supplied evidence, and requires short exact anchors at lexical hinges.
It does not prescribe themes, tag counts, word counts or a fixed number of images. A bare reference can support
narrative context but cannot display the wording carrying a lexical inference. Roles remain progressive-disclosure
guidance rather than a reason to leave this ayah's working part unexplained. Upstream discovery and planning are
not regenerated in this test.

Schema 3 removes writer quality grades and payoff summaries. `links` contain only source IDs and short unique
paragraph anchors. `partial` additionally names the distinct omitted component and its destination; `deferred`
records unused items. The script resolves paragraphs and retains source records and unused passage candidates.
A link is a location, never a claim that all of a record was explained. Independent review is still required.
Schema 1/2 arms and frozen inputs remain supported unchanged.

Fifteen criteria are frozen under each arm's `evaluation/`, excluded by the writer packet's explicit allowlist.
They retain the original ten plus the Book connection lost in the last repeat, the restored fire/guide and bodily
resurrection explanations, local source hinges, and argument orientation. The new criteria are in
`eval/regressions-v3.json`; the historical `eval/regressions.json` is unchanged. Passing these criteria is not a
substitute for reading the complete prose, checking partial records and reporting additional losses.

Twenty-three offline tests pass, including partial-use handforward, rejection of quality grades/duplicate IDs,
unambiguous anchors, separately frozen evaluation without input leakage, old schema compatibility and all prior
source/immutability checks. Preparation made no model call.

Completed: both authorized writers finished one generation, without interruption, restart or repair. Read
ARGUMENT_COMPARISON.md and each arm's review.json / supplemental.review.json. All 110 Sol and 140 Astra tags
pass exactly. Astra preserves more and develops stronger functional relationships; both lose the explicit
trodden-surface connection and remain unaccepted. Frozen inputs and generated responses are unchanged.
