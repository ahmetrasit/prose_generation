# Book 1D Consultancy Handoff

**Book:** CDBX Book 1D — Developing AI/ML-Enabled Diagnostic Medical Devices: Product, Data, Evidence, and Lifecycle Control
**Scope:** 16 chapters, 70K words. Standalone v2.1 specialization. Every chapter already produces a manufacturer build artifact and a bounded consultant deliverable with explicit Book 1C/1A/1B/2 handoffs.
**Current strength:** This book is already the closest to consultancy-ready in the series. The chapter architecture (manufacturer artifact + consultant deliverable + handoff) was designed for dual use. The 66 mapped propositions and 63 unique source records provide the regulatory grounding.

---

## What transfers directly to consultancy

1. **Chapter-level build artifacts.** Each chapter produces a specific manufacturer deliverable — these are the consultant's work products when embedded with a client's engineering team.
2. **Bounded consultant deliverables.** Already scoped per chapter. This is the consultancy-specific output layer the other books lack.
3. **Development-through-lifecycle coverage.** Intervention suitability (Ch. 1) → intended use contract (Ch. 2) → product boundary (Ch. 3) → development plan (Ch. 4) → data provenance (Ch. 5) → ... → change/CAPA/retirement (Ch. 15). The full manufacturer journey.
4. **AI/ML-specific development guidance.** Data lineage, reference standard governance, partitioning, model selection, metrics, subgroup robustness, pipeline verification, human-AI team validation, monitoring, PCCP — the complete AI/ML development lifecycle.
5. **Capstone advisory handoff (Ch. 16).** Already designed as a consultant delivery exercise.

## Gaps to close for consultancy use

### Gap 1: Client-facing development plan template

**What the book teaches:** How to construct and evaluate a development/risk/evidence plan (Ch. 4).
**What a consultant needs:** A client-ready development plan template that a manufacturer can adopt.

**Mitigation:**

- AI/ML diagnostic device development plan template: intended use → risk analysis → evidence plan → data plan → model development plan → verification plan → validation plan → regulatory strategy → monitoring plan → change control plan
- Each section maps to Book 1D chapter deliverables and to the regulatory evidence expected by FDA (De Novo, 510(k), PMA) and EU (IVDR technical documentation)
- Include a dependency graph: which plan sections must be complete before which development activities can proceed
- Include decision gates: go/no-go criteria at each stage, with regulatory-risk implications of proceeding without adequate evidence

### Gap 2: Data governance consultancy toolkit

**What the book teaches:** Data provenance, rights, and lineage (Ch. 5); reference and adjudication (Ch. 6); partitions, leakage, and coverage (Ch. 7).
**What a consultant needs:** Operational templates for establishing data governance at a client site.

**Mitigation:**

- Data charter template: data sources, rights/permissions, intended uses, retention, sharing restrictions, provenance tracking requirements
- Training data specification template: inclusion/exclusion criteria, demographic targets, annotation protocol, adjudication rules, inter-annotator agreement thresholds
- Data partitioning plan template: train/validation/test split strategy, patient-level linkage controls, leakage prevention checklist, temporal hold-out rationale
- Reference standard governance SOP: truth definition, adjudication panel composition, disagreement resolution, versioning, bias monitoring

### Gap 3: Model lifecycle consultancy (the recurring engagement)

**What the book teaches:** Model selection (Ch. 8), metrics (Ch. 9), monitoring (Ch. 14), change/PCCP (Ch. 15).
**What a consultant needs:** An operational model lifecycle management framework for ongoing advisory.

**Mitigation:**

- PCCP authoring template: predetermined change control plan with specific triggers, validation requirements per change type, and FDA/EU expectations
- Model monitoring dashboard specification: which metrics to track, alert thresholds, drift detection methods, performance degradation criteria, retraining triggers
- Model update validation protocol template: minimum evidence for each update type (retrained weights, new training data, architecture change, threshold adjustment)
- Model retirement decision framework: when to sunset a model, evidence requirements for replacement, transition plan, legacy data handling

### Gap 4: Human-AI team validation consultancy

**What the book teaches:** Ch. 13 covers human-AI team validation with a worked task script and observation record.
**What a consultant needs:** Enough depth to design and execute a human-AI team validation study for a client.

**Mitigation:**

- Human-AI team validation study protocol template: AI-alone vs. human-alone vs. human+AI design, reader selection, case selection (enrichment strategy), task script, observation protocol, statistical analysis plan
- Automation bias assessment protocol: specific experimental designs for measuring over-reliance and under-reliance on AI output
- Clinical workflow integration assessment: task analysis, time-motion study design, error taxonomy, near-miss capture
- Handoff to Book 1A Ch. 14 for human factors and to Book 1C for clinical validation methods

### Gap 5: Regulatory strategy for AI/ML diagnostics

**What the book teaches:** Development process and evidence generation.
**What a consultant needs:** Regulatory pathway selection and submission strategy specific to AI/ML diagnostics.

**Mitigation:**

- AI/ML regulatory pathway decision tree: 510(k) vs. De Novo vs. PMA, with specific criteria for AI/ML diagnostic devices
- Predetermined change control plan (PCCP) submission strategy: what to include, what level of detail FDA expects, how to negotiate scope during pre-submission
- EU AI Act compliance strategy for diagnostic AI: risk classification, conformity assessment implications, interaction with IVDR, documentation requirements
- SaMD pre-certification / total product lifecycle strategy: positioning for evolving FDA framework

---

## Handoff to other books

- **Book 1A** owns software review from the reviewer side; Book 1D provides the manufacturer's development counterpart. A consultant working both sides uses Book 1A for assessment and Book 1D for remediation guidance.
- **Book 1B** owns cybersecurity; Book 1D Ch. 11 (pipeline/software/system verification) interfaces with Book 1B for security verification of ML pipelines and training infrastructure
- **Book 1C** owns validation methods; Book 1D provides the development process that generates the evidence Book 1C teaches how to evaluate. Protocol templates in Book 1C; development planning templates in Book 1D.
- **Book 2** owns EU IVDR assessment; Book 1D's EU AI Act treatment and IVDR MDSW classification route to Book 2 for the full conformity assessment context
- **Book 3** owns consulting operations; Book 1D's bounded consultant deliverables are technical outputs that feed into Book 3's SOW structure and delivery model
