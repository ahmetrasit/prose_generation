# Book 1B Consultancy Handoff

**Book:** CDBX Book 1B — Cybersecurity and Resilience for Diagnostic Devices
**Scope:** 11 chapters (9 core + Ch. 10 submission + Ch. 11 capstones)
**Current strength:** Threat-informed patient-safety risk model, trust boundary analysis, SBOM/supply chain controls, FDA cybersecurity evidence organization. Ch. 1–9 are rated adequate across the board.

---

## What transfers directly to consultancy

1. **Threat modeling framework (Ch. 2–3).** Trust boundaries, data flows, and threat-informed risk assessment translate directly into client-facing threat model deliverables.
2. **Control architecture (Ch. 4).** Security control selection and justification is a standard consultancy deliverable — the chapter provides the reasoning framework.
3. **SBOM and supply chain audit (Ch. 5).** Software composition analysis, dependency lifecycle, and support-life assessment are high-demand consultancy services.
4. **Security testing scope (Ch. 6).** Boundary, version, environment, method limitations, and exact-release retest principles are directly usable for scoping penetration test engagements.
5. **Lifecycle response model (Ch. 7).** Intake, remediation, patching, transparency, and end-of-support planning are recurring consultancy engagements.

## Gaps to close for consultancy use

### Gap 1: Security architecture deliverable templates

**What the book teaches:** How to evaluate whether a manufacturer's security controls are adequate.
**What a consultant needs:** How to design the security architecture for a client who doesn't have one yet.

**Mitigation — add architecture-level deliverable guides:**

| Topic | Consultancy deliverable to develop |
|---|---|
| Threat model | Threat model document template: system boundary diagram, STRIDE or attack-tree analysis, risk rating with patient-safety tie-in, residual risk justification |
| Security architecture | Security architecture document template: control selection rationale, defense-in-depth layers, cryptographic inventory, authentication/authorization model, network segmentation |
| SBOM management | SBOM generation and lifecycle management SOP template: tool selection, update cadence, vulnerability monitoring, end-of-support planning |
| Penetration test | Penetration test scope and rules-of-engagement template, findings report format with CVSS scoring and remediation priority |
| Incident response | Security incident response plan template for medical device manufacturers: detection, triage, coordinated disclosure, patch deployment, ISAO/CISA notification |

### Gap 2: Security testing depth

**The curriculum gap audit (G-24) already flags this:** Ch. 6 covers useful categories but lacks complete verification-strategy patterns and artifact expectations.

**Mitigation for consultancy:**

- Security verification strategy template: mapping control requirements → test methods → tools → acceptance criteria → evidence artifacts
- Fuzz testing protocol template for diagnostic device interfaces (network, file import, API)
- Static analysis and composition analysis integration guide: tool configuration, triage workflow, false-positive management
- Production-configuration verification checklist: hardening, default credentials, debug interfaces, unnecessary services

### Gap 3: Privacy-by-design (currently absent)

**The curriculum gap audit (G-16) flags this:** Privacy is split between confidentiality-oriented cybersecurity in Book 1B and consulting data governance in Book 3.

**Mitigation for consultancy:**

- Privacy impact assessment template for diagnostic devices: data types (patient, specimen, result, image, genomic), processing purposes, legal basis, retention, cross-border transfer
- Privacy-by-design verification checklist: de-identification, access controls, audit logging, consent management, data minimization
- HIPAA/GDPR/state-law crosswalk for diagnostic device data flows
- Cloud-hosted diagnostic device privacy architecture guide: tenant isolation, key management, data residency, breach notification

### Gap 4: Duplication cleanup (Ch. 10–11) for consultancy clarity

**The curriculum gap audit (G-18, G-19) flags this:** Ch. 10 republishes substantial software-submission bodies from Book 1A; Ch. 11 substantially reproduces Book 1A Ch. 15 capstones.

**Mitigation for consultancy:**

- Replace Ch. 10 copied bodies with an integration crosswalk: "For the software submission evidence, apply Book 1A SW-F-CHK items 85–91; for cyber-specific evidence, use these additional items..."
- Give Ch. 11 capstones cyber-only delta tasks rather than full republication. A consultant needs to know what cybersecurity adds to the Book 1A review, not repeat it.

### Gap 5: Postmarket cybersecurity consultancy

**What the book teaches:** Lifecycle response principles (Ch. 7).
**What a consultant needs:** Operational templates for ongoing cybersecurity advisory engagements.

**Mitigation:**

- Postmarket cybersecurity monitoring SOP template: vulnerability feed monitoring, risk assessment cadence, patch validation, coordinated disclosure
- Cybersecurity CAPA template: linking vulnerability → exploitation scenario → patient safety impact → remediation → verification → field action decision
- Annual cybersecurity report template for manufacturer boards / notified bodies
- FDA cybersecurity postmarket guidance compliance matrix (mapping 2023 final guidance requirements to evidence artifacts)

---

## Handoff to other books

- **Book 1A** owns software review; cybersecurity consultancy should reference the SW-F-CHK items, not duplicate the software assessment
- **Book 1C** will own validation methods; any security impact on validation (data integrity, chain of custody) routes to Book 1C
- **Book 2** owns EU IVDR cybersecurity assessment requirements; Ch. 14 of Book 2 is the EU-specific counterpart
- **Book 3** owns consulting operations and data governance; privacy-by-design verification stays in Book 1B, but practice-level data lifecycle management routes to Book 3 Ch. 12
- **Book 1D** owns AI/ML development; security of ML pipelines, training data integrity, and model supply chain route to Book 1D Ch. 11
