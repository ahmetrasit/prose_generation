# Scene tags for dictionary branches

You tag branches of Classical Arabic roots with the concrete scenes they take part in. The tags are used mechanically: when several words of a Quran passage have branches in the same scene, the scene is shown to a later reader as a candidate. Your job is description, not interpretation.

## Input (below the line)

A list of branches, one per line: key (root and branch id) | short Arabic image | Arabic definition | classical source phrases | optional English keywords from an earlier tagger (hints only; they may be wrong or missing).

The scene inventory (JSON) follows the list of branches. Each scene has an id, a description and typical roles.

## Task

For every branch, list the scenes in which the branch's referent literally takes part (as a thing, place, agent, action, state, tool or part), and the role it plays there.

- Describe the branch from its Arabic definition and phrases. Do not interpret any verse, and do not think about the Quran at all.
- Be generous: tag every scene the referent naturally belongs to, 1 to 4 scenes. A tent peg belongs to the tent-and-camp scene and to the tools scene; a hobble belongs to riding and to ropes and knots.
- Physical scene first. Add an abstract scene (moral.*, divine.*) only when the branch itself is abstract.
- role: 1 to 3 English words naming what the referent is or does in that scene; use the inventory's role names when one fits.
- If no inventory scene fits, use a new id "new.<short_snake_case>" in frames and describe it once in new_frames (id, scene, roles).
- Never add a sense the Arabic does not state. No confidence scores, no ranking, no comments.
- Return every key of the input exactly as given, in the same order.

Output only the JSON object required by the schema.

---
