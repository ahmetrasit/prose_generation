# Surah Reading From Final Editorials

Read only the inline editorial input and output schema. The completed ayah
editorials are the sole semantic evidence. Do not read other files, consult
external sources, use remembered interpretations, or recover material from
discovery, scope prose, invitations, translations, Quran datasets, networks,
or previous surah readings. Paths are provenance only. Write JSON, not prose.

Read every supplied ayah editorial. Identify the main movements through which
their already-present readings illuminate one another across the surah. This
is synthesis of what these editorials say, not fresh discovery. A cross-ayah
connection may clarify how their images work together but must be fully
supported by those texts. Preserve source attribution, uncertainty, scope,
alternatives, and substantive restrictions. Do not upgrade an analogy into a
lexical meaning, a reported reading into an established fact, or a local
resonance into a universal claim. Record unresolved tensions in friction.

First describe the surah's primary progression as presented in the editorials,
with exact supporting anchors. Then identify materially distinct whole-surah
movements and their specific reader payoffs. Prefer concrete surprising
readings that expand or shift how the primary meaning is heard. Ordinary
thematic similarity alone does not establish a secondary image system.

Do not compress all findings into an inventory. Select the main cross-ayah
movements that make this surah's reading intelligible, without quotas or a
fixed number of themes. Preserve distinct significant systems rather than
merging them into broad labels such as guidance, mercy, or dependence. Each
movement needs at least two distinct ayah members. Do not manufacture a
second member to rescue a single-ayah image. If the editorials do not support
a cross-ayah movement, an empty movements array is valid; explain this in
friction and keep the primary reading grounded.

For each member, name the image and explain its particular contribution to
the movement. An image's mention is not enough: identify what it does and how
it changes the reader's understanding. State its qualifications affirmatively
where possible, while retaining explicit exclusions where needed. A boundary
belongs to this connection; it does not invalidate unrelated readings.

Every source anchor must be an exact substring of its ayah editorial, contain
at least six whitespace-separated words, and occur exactly once there. Include
all spans necessary to support the image, its function, attribution, and
qualification. Do not substitute a loosely related passage. Multiple anchors
may be needed for one member. Record all ayahs in ayahCoverage, in input order,
including those supplying only primary context; explain their role. Movement
IDs there must exactly match that ayah's actual membership.

Use the requested language for reader-facing descriptions. Preserve the
packetHash. Follow the supplied schema exactly. Do not draft the final prelude
or postlude at this stage.
