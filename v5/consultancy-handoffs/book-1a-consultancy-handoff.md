# Book 1A Consultancy Handoff

**Book:** CDBX Book 1A — Medical Device Software, AI, and Diagnostic Evidence Review
**Scope:** 15 chapters, 91 SW-F-CHK items, 383 pages
**Current strength:** Regulatory citation precision is publication-grade. Paired Expert-Eye Labs build genuine reviewer judgment. The 7-pass review structure and evidence-state system (A/U/M/D/C/N-A) are directly usable as consultancy audit frameworks.

---

## What transfers directly to consultancy

1. **91-item checklist as submission-readiness audit.** Run SW-F-CHK items against a client's package before filing. Every U/M/D finding becomes a gap the client fixes before the reviewer finds it.
2. **7-pass review structure as project scaffold.** Reverse the review sequence into a submission-building plan: pass 1 gaps become the project plan, pass 7 is the pre-submission flight check.
3. **Evidence-state vocabulary.** A/U/M/D/C gives you a shared language with clients that is more precise than "ready / not ready."
4. **EU AI Act dual-jurisdiction reasoning (Ch. 15).** Directly usable for clients filing in both US and EU.
5. **Dual-audience design.** The agency-lens/company-lens pairing means the consultant already sees both sides of the table.

## Gaps to close for consultancy use

### Gap 1: Remediation playbooks

**What the book teaches:** How to identify that a software architecture description is inadequate.
**What a consultant also needs:** How to write one, or how to guide a client's engineering team to produce one that will satisfy the reviewer.

**Mitigation — add per-checklist-cluster remediation guides:**

| Checklist cluster | Remediation deliverable to develop |
|---|---|
| SW-F-CHK-01 to -12 (software description) | Software description template with minimum content, common deficiency patterns, and worked before/after examples |
| SW-F-CHK-13 to -28 (risk/hazard) | Risk-traceability matrix template linking hazards → controls → verification → residual risk, with IEC 62304 class-specific requirements |
| SW-F-CHK-29 to -45 (architecture/design) | Architecture documentation template: SOUP/OTS inventory, data flow diagrams, interface specifications, with regulatory-minimum vs. best-practice tiers |
| SW-F-CHK-46 to -62 (V&V) | Verification and validation strategy template: test-level rationale, coverage criteria, anomaly management, regression policy |
| SW-F-CHK-63 to -75 (AI/ML) | PCCP template, training data provenance checklist, monitoring plan template, retraining protocol outline |
| SW-F-CHK-76 to -84 (change/config) | Change control SOP template with regulatory-impact assessment decision tree |
| SW-F-CHK-85 to -91 (submission) | Submission assembly checklist with section-to-evidence mapping and common reviewer-question anticipation guide |

### Gap 2: Remediation prioritization framework

**What the book teaches:** How to identify all gaps.
**What a consultant also needs:** How to triage them — "fix these 5 before your pre-sub, defer these 3 to the final submission, and flag these 2 as acceptable risk."

**Mitigation — add a triage matrix:**

- **Axis 1: Regulatory risk** — Will this gap cause a refuse-to-file, a deficiency letter, or an additional-information request?
- **Axis 2: Remediation cost** — Is this a document rewrite (days), a design change (weeks), or a revalidation (months)?
- **Axis 3: Dependency** — Does fixing this unblock other items?

Produce a worked example using the HelixBridge Dx capstone: given the gaps found in the capstone review, show the prioritized remediation sequence with timeline estimates.

### Gap 3: Study design (not just evaluation)

**What the book teaches:** How to recognize flaws in a validation study (Ch. 11–13).
**What a consultant also needs:** How to design the study — sample size justification, protocol structure, predicate selection rationale, endpoint definition.

**Mitigation — add study-design companion sections for:**

- Analytical validation study protocol template (Ch. 11 extension): specimen selection, sample size tables for key performance claims, acceptance criteria derivation, platform/site comparability design
- Clinical validation study protocol template (Ch. 12 extension): reader panel composition, MRMC power analysis, truth panel governance, washout/carryover design
- Statistical analysis plan template (Ch. 13 extension): pre-specified endpoints, interim analysis rules, missing-data handling, multiplicity adjustment

### Gap 4: Human factors depth for AI diagnostics consultancy

**What the book teaches:** Chapter 14 flags automation bias, clinical reliance, and use-related risk in 7 pages.
**What a consultant needs:** Enough depth to design a formative usability study, write a use-related risk analysis, specify critical tasks, and evaluate summative study results.

**Mitigation — expand or supplement Chapter 14 with:**

- Use specification template: intended users, use environments, user profiles, task analysis
- Use-related risk analysis template: critical tasks, use errors, harm severity, mitigation
- Formative study protocol template: task scenarios, think-aloud protocol, data capture, iteration criteria
- Summative study protocol template: sample size, task completion criteria, effectiveness/efficiency thresholds, root-cause analysis of use errors
- Automation bias assessment framework: specific to AI-assisted diagnostic workflows

### Gap 5: Client-facing report format

**What the book teaches:** How to reach conclusions and record evidence states.
**What a consultant needs:** How to present findings to a client in a way that drives action — executive summary, prioritized findings, remediation roadmap, timeline, and cost implications.

**Mitigation — add a consultancy-report template:**

- Executive summary (1 page): product identity, review scope, overall readiness assessment, top 3 actions
- Findings detail: organized by checklist cluster, with evidence state, gap description, regulatory consequence, and recommended remediation
- Remediation roadmap: Gantt-style timeline with dependencies
- Appendix: raw checklist results with evidence citations

---

## Handoff to other books

- **Book 1B** owns cybersecurity remediation; Book 1A consultancy should cross-reference, not duplicate
- **Book 1C** will own validation study design methods; Book 1A consultancy supplements should be software-scoped and defer general validation to Book 1C
- **Book 2** owns EU-specific assessment; the EU AI Act treatment in Ch. 15 stays here, but IVDR conformity consulting routes to Book 2
- **Book 3** owns the consulting operating model (SOW, economics, delivery, pipeline); Book 1A consultancy stays within technical remediation, not practice management
- **Book 1D** owns AI/ML product development; Book 1A consultancy covers the reviewer's side, Book 1D covers the manufacturer's build side
