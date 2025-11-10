<!-- SPDX-License-Identifier: CC-BY-NC-ND-4.0 -->
# AI OSI Stack v5 Risk Register (Narrative)

## Data Rights
- **Description**: Unauthorized use or processing of data lacking proper consent, contractual rights, or regulatory clearance. Risk extends to synthetic data built on sensitive attributes and cross-border data transfers.
- **Business Impact**: High — legal penalties, injunctions, and reputational damage.
- **Likelihood**: Medium — mitigated by due diligence yet exposed to vendor errors.
- **Inherent Risk**: High (H/H matrix).
- **Residual Risk**: Medium (H/M matrix) given layered controls.
- **Controls**: Layer 2 Data controls from `Controls_Catalog_by_Layer.md`; contractual data rights attestations; privacy impact assessments.
- **Early Warning Indicators**: Vendor audit findings, data subject complaints, anomalies in access logs.
- **Escalation Path**: Data Steward → CRO → Audit & Risk Committee → Full Board if material.
- **Disclosure Considerations**: Evaluate against SEC materiality criteria; coordinate with legal for potential Item 106 or 8-K filing.
- **Cross-References**: Board brief risk snapshot; SEC Disclosure Playbook scope.

## Model Bias
- **Description**: Models producing discriminatory or unfair outcomes, impacting protected classes or leading to systemic errors in decision-making.
- **Business Impact**: High — regulatory sanctions, litigation, loss of customer trust.
- **Likelihood**: Medium — consistent monitoring reduces but does not eliminate risk.
- **Inherent Risk**: High.
- **Residual Risk**: Medium.
- **Controls**: Layer 3 Model controls; bias testing protocols; independent validation memos.
- **Early Warning Indicators**: Disparity metrics, customer complaints, audit findings.
- **Escalation Path**: Model Validation Lead → AIRC → TEC → Board.
- **Disclosure Considerations**: Potential 10-K risk factor updates; incident triggers for Item 1.05 if systemic harm occurs.
- **Cross-References**: Board brief control families; FAQs on model transparency.

## Prompt Injection
- **Description**: Malicious prompts or instructions manipulating model behavior, bypassing guardrails, or exfiltrating data.
- **Business Impact**: Medium to High depending on service impact and data exposure.
- **Likelihood**: High — adversarial tactics proliferating.
- **Inherent Risk**: High.
- **Residual Risk**: Medium-High due to evolving threats.
- **Controls**: Layer 4 Instruction controls; access management; prompt filtering and monitoring.
- **Early Warning Indicators**: Spike in blocked prompts, anomaly detection alerts.
- **Escalation Path**: Prompt Governance Lead → Security Operations → ARC.
- **Disclosure Considerations**: Assess for material data leakage or service disruption; coordinate with SEC playbook.
- **Cross-References**: Incident Response Guide 72-hour clock; Third-Party oversight for API security.

## Leakage / Intellectual Property Misuse
- **Description**: Unauthorized disclosure of proprietary data or models through AI interactions, logging, or third-party integrations.
- **Business Impact**: High — loss of competitive advantage, legal exposure.
- **Likelihood**: Medium — mitigated by controls but vulnerable via human error.
- **Inherent Risk**: High.
- **Residual Risk**: Medium.
- **Controls**: Layer 4 and 7 controls; data loss prevention overlays; contractual restrictions with partners.
- **Early Warning Indicators**: DLP alerts, unusual export activity, whistleblower tips.
- **Escalation Path**: Security Operations → CRO → ARC → Board.
- **Disclosure Considerations**: Potential materiality for 8-K; must assess IP valuation impact.
- **Cross-References**: Board brief risk appetite; Disclosure Safe Harbor samples.

## Third-Party Model Dependency
- **Description**: Reliance on external models or APIs introducing operational and compliance risk, including sudden vendor changes or performance degradation.
- **Business Impact**: Medium-High — service disruption, contractual penalties.
- **Likelihood**: Medium-High.
- **Inherent Risk**: High.
- **Residual Risk**: Medium after due diligence.
- **Controls**: Layer 2 and 3 controls; `ThirdParty_and_ModelSupplyChain.md` due diligence; contractual guardrails.
- **Early Warning Indicators**: Vendor notifications, SLA breaches, adverse media.
- **Escalation Path**: Vendor Manager → CRO → ARC.
- **Disclosure Considerations**: Monitor for material dependency shifts; incorporate into risk factors.
- **Cross-References**: Nasdaq alignment table; SEC playbook scope.

## Toolchain Supply Chain
- **Description**: Compromise of development or deployment tools (CI/CD, model repositories) leading to malicious code insertion or tampering.
- **Business Impact**: High — integrity failures, regulatory scrutiny.
- **Likelihood**: Medium.
- **Inherent Risk**: High.
- **Residual Risk**: Medium due to layered security.
- **Controls**: Layer 6 controls; secure pipeline practices; integrity checks.
- **Early Warning Indicators**: Integrity alerts, unsigned artifacts, vendor advisories.
- **Escalation Path**: DevSecOps Lead → Security Steering Committee → ARC.
- **Disclosure Considerations**: Evaluate for 8-K if compromise impacts material systems.
- **Cross-References**: Controls catalog deployment section; audit checklist supply chain section.

## Shadow AI
- **Description**: Unapproved use of AI tools or services outside governance oversight, potentially bypassing controls and exposing data.
- **Business Impact**: Medium-High — compliance violations, inconsistent outcomes.
- **Likelihood**: High — user adoption pressure.
- **Inherent Risk**: High.
- **Residual Risk**: Medium-High pending training adherence.
- **Controls**: Layer 0/1 mandate; awareness training; policy enforcement.
- **Early Warning Indicators**: IT asset scans, expense reports, user surveys.
- **Escalation Path**: CIO → CRO → ARC.
- **Disclosure Considerations**: Assess for systemic control failures; update risk factor narrative.
- **Cross-References**: Training agenda; FAQs for regulators.

## Reasoning Harms
- **Description**: AI-generated reasoning errors leading to incorrect recommendations, automation bias, or safety incidents.
- **Business Impact**: Medium-High — operational disruption, customer harm.
- **Likelihood**: Medium.
- **Inherent Risk**: Medium-High.
- **Residual Risk**: Medium due to human-in-the-loop controls.
- **Controls**: Layer 5 controls; oversight scorecards; exception handling.
- **Early Warning Indicators**: Override rates, escalation volume, user feedback.
- **Escalation Path**: Human Oversight Lead → CRO → TEC.
- **Disclosure Considerations**: Consider 10-K narrative adjustments if recurring.
- **Cross-References**: Board brief reasoning layer; Incident Response Guide for monitoring.

## Incident Communications Failure
- **Description**: Breakdown in communication channels during AI incidents, causing delayed notifications, inconsistent messaging, or regulatory non-compliance.
- **Business Impact**: High — regulatory penalties, stakeholder distrust.
- **Likelihood**: Medium.
- **Inherent Risk**: High.
- **Residual Risk**: Medium-Low with rehearsed playbooks.
- **Controls**: Layer 7 controls; communication templates; disclosure committee oversight.
- **Early Warning Indicators**: Missed drill objectives, audit findings, message discrepancies.
- **Escalation Path**: Communications Lead → CRO → Board Chair.
- **Disclosure Considerations**: Meta-risk affecting all filings; highlight in disclosure playbook.
- **Cross-References**: Incident Response Guide communications section; Board brief disclosure summary.

> Authored and maintained solely by Daniel P. Madden (custodial).  
> This is a non-operational, publication-grade governance artifact.  
> No AEIP runtime specs or machine-readable schemas are included.
