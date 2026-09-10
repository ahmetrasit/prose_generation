# Book 1C Consultancy Handoff

**Book:** CDBX Book 1C — Validation Evidence for Diagnostic Products
**Scope:** 18 chapters. Lifecycle foundation (25–30%) + validation methods, modality application, and integrated decisions (70–75%). NGS, oncology, liquid biopsy, CDx, digital pathology.
**Current strength:** This is the series entry point. It owns the total-product lifecycle map, the controlled validation taxonomy, and the deep analytical/clinical validation methods that the other books reference but don't teach at protocol level.

---

## What transfers directly to consultancy

1. **Total-product lifecycle map.** The authoritative specimen-to-clinical-action model is the consultant's system-level orientation tool. Every engagement starts with "where in this map is the client's gap?"
2. **Validation taxonomy.** The controlled cross-series definitions of analytical validation, clinical performance/validation, design V&V, software V&V, laboratory verification, and market validation eliminate the terminology confusion that costs consultants credibility.
3. **Analytical validation methods (deep).** Protocol-level coverage of accuracy, precision, LoD/LoQ, measuring range, interference, carryover, stability, platform comparability, and software generalizability. These are the core of validation consultancy.
4. **Clinical validation methods (deep).** Study design, endpoints, estimands, bias controls, sampling, analysis, and failure handling. Directly maps to protocol writing engagements.
5. **Modality application.** NGS (tissue + liquid biopsy), oncology CDx, and digital pathology each get dedicated method chapters. These are the highest-demand consultancy verticals.

## Gaps to close for consultancy use

### Gap 1: Protocol authoring (the primary consultancy deliverable)

**What the book teaches:** How to evaluate whether a validation protocol/study is adequate.
**What a consultant needs:** How to author the protocol from scratch for a client.

**Mitigation — add protocol templates per validation type:**

| Validation type | Protocol template to develop |
|---|---|
| Analytical validation — general | Master analytical validation protocol: study objectives, acceptance criteria derivation from intended use claims, sample plan (matrix, size, selection), measurement procedure, statistical analysis plan, deviation handling |
| Analytical validation — NGS tissue | NGS-specific protocol addendum: variant classes (SNV, indel, CNV, fusion, MSI), truth set construction, LoD by variant type, reproducibility across runs/operators/sites, bioinformatics pipeline version control |
| Analytical validation — liquid biopsy | cfDNA/ctDNA-specific protocol addendum: pre-analytical variables (tube type, time-to-processing, plasma separation), LoD at clinically relevant VAFs, input DNA mass titration, carryover/contamination controls |
| Clinical validation — general | Clinical validation protocol template: primary endpoint, comparator/truth, patient population, sample size justification, site selection, enrollment criteria, data management plan, SAP, DSMB if applicable |
| Clinical validation — digital pathology | WSI reader study protocol: reader panel (pathologist selection, qualification, training), MRMC design, truth panel, washout period, image quality controls, reading environment specifications |
| Clinical validation — CDx | Companion diagnostic co-development protocol: bridging study design, concordance thresholds, clinical utility evidence strategy, drug-diagnostic co-labeling plan |
| Stability | Stability protocol template: real-time and accelerated conditions, time points, acceptance criteria, statistical trending, shipping validation |

### Gap 2: Study report authoring

**What the book teaches:** How to evaluate whether study results support claims.
**What a consultant needs:** How to write the study report that presents results to a reviewer or notified body.

**Mitigation — add study report templates:**

- Analytical performance study report template: methods summary, results by characteristic, acceptance criteria disposition, deviations and impact assessment, conclusions with claim-level mapping
- Clinical performance study report template: STARD-compliant flow diagram, demographics, primary and secondary endpoints, sensitivity/specificity/PPV/NPV with confidence intervals, subgroup analyses, protocol deviations, limitations
- Performance evaluation report (EU): IVDR Annex XIII-compliant structure (routes to Book 2 for full EU treatment, but the data presentation format belongs here)

### Gap 3: Pre-submission strategy

**What the book teaches:** How to evaluate a submission package.
**What a consultant needs:** How to plan the regulatory strategy before the submission exists.

**Mitigation — add pre-submission planning tools:**

- Predicate/substantial equivalence analysis template (510(k) pathway): device comparison table, technological characteristics, performance data comparison, indications for use crosswalk
- De Novo classification request strategy template: risk/benefit analysis, special controls proposal, performance testing rationale
- Pre-submission meeting request template: meeting objectives, specific questions, proposed study design summary, supporting data
- FDA breakthrough device program application template for AI/ML diagnostics

### Gap 4: Specimen and pre-analytical consultancy

**The curriculum gap audit (G-03) flags this as needs-deepening across the series.** Book 1C owns this topic.

**Mitigation for consultancy:**

- Specimen collection and handling validation protocol template: collection device qualification, transport conditions, stability, input adequacy criteria
- Pre-analytical variable assessment framework: systematic identification of pre-analytical factors, experimental design for assessing their impact, acceptance criteria
- Sample equivalence study design template: for platform transfers, site additions, or specimen type extensions

### Gap 5: Revalidation after change (the recurring revenue consultancy)

**The curriculum gap audit (G-17) flags this:** Revalidation after change is distributed across books but has no common decision model. Book 1C owns this.

**Mitigation — this is the highest-value consultancy tool:**

- Change impact assessment template: change description → affected claims → affected validation evidence → revalidation scope → bridging study design → acceptance criteria
- Revalidation decision tree: software change, reagent lot change, instrument platform change, site addition, intended use expansion, algorithm update — each with minimum evidence requirements
- Bridging study protocol template: comparability design, sample size for equivalence/non-inferiority, acceptance criteria, statistical analysis plan

---

## Handoff to other books

- **Book 1A** owns software-specific review and remediation; validation of software components (IEC 62304 verification) stays in Book 1A, while validation of the diagnostic claim routes here
- **Book 1B** owns cybersecurity; any data-integrity or chain-of-custody impacts on validation evidence route here for the validation consequence, to Book 1B for the security control
- **Book 2** owns EU IVDR assessment; Book 1C provides the methods, Book 2 provides the EU conformity assessment context. Performance evaluation reports serve both jurisdictions.
- **Book 3** owns consulting operations; Book 1C provides the technical validation toolkit, Book 3 provides the SOW structure, economics, and client management for validation engagements
- **Book 1D** owns AI/ML development; Book 1C provides the validation endpoint (what evidence is needed), Book 1D provides the development process (how to build toward that evidence)
