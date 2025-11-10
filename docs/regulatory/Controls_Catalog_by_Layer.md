<!-- SPDX-License-Identifier: CC-BY-NC-ND-4.0 -->
# Controls Catalog by OSI Layer (Narrative)

## Layer 0: Mandate
- **Control Objectives**: Align AI initiatives with board-approved strategy, ensure authority chains, and set explicit risk appetite.
- **Control Activities**:
  - Annual board review of AI strategy and mandate documentation.
  - Custodian updates to governance briefs following major initiatives.
  - ERM integration of AI risk appetite statements.
- **Evidence Examples**: Board minutes, `BOARD_BRIEF_NACD_SEC_Nasdaq.md`, risk appetite memos.
- **Validation Approach**: Annual charter compliance review and cross-check against strategic plans.
- **Dependencies**: Provides foundation for all other layers; informs ethics and policy decisions.

## Layer 1: Ethics
- **Control Objectives**: Embed responsible AI principles, protect stakeholders, and ensure ethical decision-making.
- **Control Activities**:
  - Conduct ethics impact assessments for new use cases.
  - Convene stakeholder advisory sessions and document outcomes.
  - Maintain escalation protocol for ethical concerns.
- **Evidence Examples**: Ethics assessment summaries, committee meeting notes, FAQs addressing transparency.
- **Validation Approach**: Semi-annual ethical audits reviewing adherence to principles and stakeholder feedback.
- **Dependencies**: Relies on mandate layer guidance; informs data and model evaluations.

## Layer 2: Data
- **Control Objectives**: Safeguard data rights, privacy, quality, and provenance.
- **Control Activities**:
  - Maintain data inventories and provenance attestations.
  - Perform privacy impact assessments and contractual reviews.
  - Implement access controls and segregation for training datasets.
- **Evidence Examples**: Data due diligence checklists, third-party questionnaires, risk register entries.
- **Validation Approach**: Quarterly data governance assurance with remediation tracking.
- **Dependencies**: Supports model accuracy and ethical compliance.

## Layer 3: Model
- **Control Objectives**: Ensure model robustness, fairness, and alignment with intended use.
- **Control Activities**:
  - Independent validation of models prior to deployment.
  - Bias and robustness testing with documented thresholds.
  - Periodic re-evaluation aligned with vendor updates.
- **Evidence Examples**: Validation narratives, evaluation reports, Nasdaq oversight mapping.
- **Validation Approach**: Quarterly validation memos reviewed by Technology & Ethics Committee.
- **Dependencies**: Draws on data controls; informs instruction and reasoning layers.

## Layer 4: Instruction
- **Control Objectives**: Govern prompts, access, and usage parameters to prevent misuse and data leakage.
- **Control Activities**:
  - Maintain authorized prompt libraries with change approvals.
  - Enforce role-based access and multi-factor authentication.
  - Monitor prompt logs for anomalies and injection attempts.
- **Evidence Examples**: Prompt governance policies, access review reports, incident response logs.
- **Validation Approach**: Quarterly access certification and prompt governance review.
- **Dependencies**: Informed by model capabilities and data sensitivity.

## Layer 5: Reasoning
- **Control Objectives**: Maintain interpretability, ensure human oversight, and prevent automation bias.
- **Control Activities**:
  - Implement human-in-the-loop checkpoints for critical decisions.
  - Track override rates and reasoning anomalies.
  - Provide explainability briefs for board review.
- **Evidence Examples**: Oversight scorecards, decision review matrices, training materials.
- **Validation Approach**: Semi-annual oversight effectiveness assessment with exception logs.
- **Dependencies**: Relies on instruction protocols and model transparency.

## Layer 6: Deployment
- **Control Objectives**: Control release processes, maintain rollback readiness, and secure environments.
- **Control Activities**:
  - Change Advisory Board approvals for AI deployments.
  - Segregation of development, testing, and production environments.
  - Regular tabletop exercises for rollback scenarios.
- **Evidence Examples**: Deployment readiness assessments, change logs, audit checklist references.
- **Validation Approach**: Deployment cycle audits verifying approvals and rollback documentation.
- **Dependencies**: Builds on reasoning assurances and feeds into publication controls.

## Layer 7: Publication
- **Control Objectives**: Ensure accurate external communications, protect sensitive information, and meet disclosure obligations.
- **Control Activities**:
  - Coordinate with disclosure committee on AI-related announcements.
  - Maintain investor and regulator communication scripts.
  - Conduct messaging reviews after incidents.
- **Evidence Examples**: Disclosure checklists, safe harbor language, board update templates.
- **Validation Approach**: Quarterly disclosure control assessments with legal review.
- **Dependencies**: Requires input from incident response, risk register, and controls catalog.

## Layer 8: Civic
- **Control Objectives**: Address societal impacts, regulatory engagement, and public transparency.
- **Control Activities**:
  - Track public policy developments and respond to consultations.
  - Maintain civic engagement logs and transparency reports.
  - Align community commitments with governance updates.
- **Evidence Examples**: Civic engagement summaries, board brief civic layer notes.
- **Validation Approach**: Annual stakeholder engagement review.
- **Dependencies**: Informed by all preceding layers; influences mandate refresh cycles.

> Authored and maintained solely by Daniel P. Madden (custodial).  
> This is a non-operational, publication-grade governance artifact.  
> No AEIP runtime specs or machine-readable schemas are included.
