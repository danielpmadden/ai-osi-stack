<!-- SPDX-License-Identifier: CC-BY-NC-ND-4.0 -->
# AI Incident Response and Materiality Guide

## Definitions
- **Incident**: Any confirmed or suspected event where AI-enabled systems, models, or processes deviate from expected behavior, compromise data, or trigger governance policy breaches.
- **Material Incident**: An incident assessed to have a reasonable likelihood of influencing investor decisions, regulatory obligations, or strategic operations, considering qualitative and quantitative factors in the SEC Disclosure Playbook.
- **AI-Caused vs. AI-Assisted**: AI-caused incidents originate from AI model logic, training, or deployment flaws; AI-assisted incidents involve traditional cyber or operational events amplified by AI misuse or support.

## 72-Hour Clock Narrative
1. **Hour 0–12 (Detection & Stabilization)**
   - Confirm incident scope, isolate affected systems, preserve forensic evidence.
   - Notify CRO, legal, privacy, and custodian; activate AI Risk Council war room.
2. **Hour 12–36 (Assessment & Materiality)**
   - Conduct preliminary impact analysis (data, operations, stakeholders).
   - Apply materiality framework; document findings in incident log.
   - Prepare day 1 board update outlining facts, controls engaged, and next steps.
3. **Hour 36–60 (Remediation & Disclosure Prep)**
   - Implement containment steps, begin remediation, track dependencies.
   - Draft disclosure language options; coordinate with counsel.
   - Deliver day 3 board update emphasizing trajectory and open risks.
4. **Hour 60–72 (Decision & Communications)**
   - Finalize materiality decision; if material, obtain approvals for 8-K filing.
   - Align internal and external communications; ready investor and customer statements.
   - Issue day 7 planning outline anticipating ongoing reporting needs.

## Investigation Data Collected
- System and application logs, access records, configuration baselines relevant to the incident.
- Model version histories, evaluation summaries, and prompt transcripts necessary to understand root cause.
- Evidence purposely excluded: personally identifiable information beyond necessity, proprietary datasets unrelated to the incident, privileged communications (retained in Control Tower only).

## Containment & Remediation Actions
- Suspend affected AI models or functionalities pending validation.
- Apply patches, adjust prompts, or revert to prior model versions as needed.
- Enhance monitoring thresholds and deploy compensating controls.
- Document lessons learned, update control catalogs, and track remediation tasks with owners and due dates.

## Communications Plan
- **Internal**: Immediate notification to executive leadership, affected business units, and support teams. Provide daily updates during active response.
- **Customers**: Tailored notifications if service or data impact is confirmed; coordinate with customer success and legal.
- **Regulators**: Engage relevant agencies once materiality threshold met or as required by sector regulations.
- **Investors**: Align messaging with disclosure decisions; use pre-approved safe harbor language.

## Board Update Templates
- **Day 1 Outline**: Incident summary, detection method, immediate actions, initial risk assessment, next 24-hour plan.
- **Day 3 Outline**: Updated impact analysis, remediation progress, preliminary materiality view, resource needs, stakeholder communications status.
- **Day 7 Outline**: Final materiality determination, disclosure filings made/planned, remediation roadmap, governance updates, requests for board decisions.

## Post-Incident Governance Updates
- Refresh relevant policies, including incident response, disclosure controls, and third-party oversight requirements.
- Schedule targeted training sessions addressing identified gaps.
- Update risk register entries, control catalog narratives, and board briefing materials to reflect new insights.
- Record assurance follow-ups (audits, testing) to validate remediation effectiveness.

> Authored and maintained solely by Daniel P. Madden (custodial).  
> This is a non-operational, publication-grade governance artifact.  
> No AEIP runtime specs or machine-readable schemas are included.
