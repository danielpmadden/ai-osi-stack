from __future__ import annotations

CHAPTER_DATA = {
    "source/chapters/chapter-00-introduction-and-purpose.tex": {
        "narrative_intent": (
            "This chapter confronts the civic confusion that emerges when AI governance lacks a shared constitution, "
            "explaining how the Stack anchors obligations in a traceable civic mandate so communities know who is "
            "answering for each promise."
        ),
        "normative_clauses": [
            "Custodians SHALL map introductory assertions to \\texttt{schemas/aeip/aeip-frame-schema.json} so that AEIP records tie narrative claims to enforceable controls.",
            "Stewards SHALL catalogue adoption rationales using \\texttt{schemas/aeip-template.yaml} to preserve provenance for external auditors.",
            "Briefing teams SHOULD surface glossary anchors from \\texttt{schemas/svc/semantic-registry.jsonld} when translating the chapter for civic audiences.",
        ],
        "plain_summary": (
            "The introduction lays out why the AI OSI Stack exists and whom it protects. "
            "It reminds readers that civic consent, legal mandates, and technical controls move together. "
            "It also points to the artefacts that document each promise so anyone can verify the origin. "
            "By following those records, a community can see why the Stack insists on openness."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/aeip/aeip-frame-schema.json}",
            "\\texttt{schemas/aeip-template.yaml}",
            "\\texttt{schemas/svc/semantic-registry.jsonld}",
        ],
    },
    "source/chapters/chapter-01-historical-and-technical-lineage.tex": {
        "narrative_intent": (
            "The lineage chapter addresses the recurring problem of institutional amnesia, detailing how public records, "
            "technical decisions, and civic mandates evolved so implementers do not reinvent past mistakes."
        ),
        "normative_clauses": [
            "Archivists SHALL compile provenance packets using \\texttt{schemas/interpretive-trace-package.jsonld} to demonstrate continuity from prior stack versions.",
            "Custodians SHALL register lineage claims within \\texttt{schemas/integrity-ledger-entry.jsonld} so that auditors can trace when obligations first appeared.",
            "Policy leads SHOULD cite Layer 0 mandates alongside \\texttt{schemas/aeip/aeip-frame-schema.json} entries when briefing legislators on the stack’s history.",
        ],
        "plain_summary": (
            "This chapter retells how the stack was built and why each revision mattered. "
            "It urges teams to keep a public memory so lessons from earlier deployments stay visible. "
            "Readers learn which artefacts capture these commitments. "
            "Anyone checking the history can inspect those logs to confirm what changed and why."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/interpretive-trace-package.jsonld}",
            "\\texttt{schemas/integrity-ledger-entry.jsonld}",
            "\\texttt{schemas/aeip/aeip-frame-schema.json}",
        ],
    },
    "source/chapters/chapter-02-philosophical-foundations.tex": {
        "narrative_intent": (
            "The philosophical foundations confront the human problem of fragmented moral vocabularies, ensuring that "
            "technical teams, policymakers, and communities deliberate with a shared set of ethical anchors."
        ),
        "normative_clauses": [
            "Governance leads SHALL catalogue interpretive commitments within \\texttt{schemas/svc/semantic-registry.jsonld} so lexical drift is immediately visible.",
            "Custodians SHALL align principle-to-layer mappings using \\texttt{schemas/aeip/aeip-frame-schema.json} before approving new obligations.",
            "Ethics councils SHOULD file deliberation outcomes as \\texttt{schemas/oversight-audit-memo.jsonld} artefacts to document contested judgments.",
        ],
        "plain_summary": (
            "This chapter explains the moral logic beneath the stack. "
            "It keeps values debates from becoming abstract by tying them to specific records. "
            "Readers see where to store definitions and disagreements. "
            "That makes philosophical claims testable instead of vague."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/svc/semantic-registry.jsonld}",
            "\\texttt{schemas/aeip/aeip-frame-schema.json}",
            "\\texttt{schemas/oversight-audit-memo.jsonld}",
        ],
    },
    "source/chapters/chapter-03-layer0-civic-mandate.tex": {
        "narrative_intent": (
            "Layer 0 responds to the democratic deficit that occurs when AI deployments skip explicit civic authorization, "
            "ensuring communities can see and challenge the mandate that permits governance technology."
        ),
        "normative_clauses": [
            "Custodians SHALL encode mandate terms within \\texttt{schemas/aeip/civic-charter-schema.json} before any Layer 0 service is activated.",
            "Oversight teams SHALL log accountability triggers using \\texttt{schemas/aeip/incident-report-schema.json} whenever mandate duties are breached.",
            "Civic monitors SHOULD publish summary ledgers referencing \\texttt{schemas/integrity-ledger-entry.jsonld} so residents can verify fulfilment of obligations.",
        ],
        "plain_summary": (
            "This layer states that no AI system should operate without a public license to do so. "
            "It shows how to record that permission and what happens if the mandate is broken. "
            "People can read the logged promises and compare them with reality. "
            "If something goes wrong, the records explain who must fix it."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/aeip/civic-charter-schema.json}",
            "\\texttt{schemas/aeip/incident-report-schema.json}",
            "\\texttt{schemas/integrity-ledger-entry.jsonld}",
        ],
    },
    "source/chapters/chapter-04-layer1-ethical-charter.tex": {
        "narrative_intent": (
            "Layer 1 tackles the frequent gap between stated corporate values and enforceable duties by translating the "
            "ethical charter into testable commitments that teams cannot ignore."
        ),
        "normative_clauses": [
            "Stewards SHALL encode charter clauses in \\texttt{schemas/aeip/ccm-schema.json} before any development milestone is approved.",
            "Compliance leads SHALL update charter change logs through \\texttt{schemas/ccm-template.yaml} whenever values evolve or conflicts are resolved.",
            "Narrative editors SHOULD cross-reference terms with \\texttt{schemas/svc/semantic-registry.jsonld} so that ethical language stays consistent across layers.",
        ],
        "plain_summary": (
            "This chapter turns value statements into obligations people can check. "
            "It tells teams where to store the formal charter and how to record updates. "
            "The guidance keeps words like fairness and dignity tied to specific controls. "
            "Readers can see how ethical promises become requirements they can test."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/aeip/ccm-schema.json}",
            "\\texttt{schemas/ccm-template.yaml}",
            "\\texttt{schemas/svc/semantic-registry.jsonld}",
        ],
    },
    "source/chapters/chapter-05-layer2-data-stewardship.tex": {
        "narrative_intent": (
            "Layer 2 recognises that communities fear losing control of their data, so it articulates how stewardship, "
            "consent, and remedy pathways are enforced throughout the lifecycle."
        ),
        "normative_clauses": [
            "Data custodians SHALL catalogue collection and usage rules in \\texttt{schemas/drr-schema.yaml} prior to ingesting records.",
            "Incident commanders SHALL document breaches of stewardship duties through \\texttt{schemas/aeip/incident-report-schema.json} within mandated timeframes.",
            "Programme owners SHOULD update trust briefings with citations to \\texttt{schemas/aeip-template.yaml} so residents know where stewardship evidence lives.",
        ],
        "plain_summary": (
            "This layer explains how the stack protects the data it relies on. "
            "It points to the forms that describe lawful use, incidents, and responses. "
            "Readers can trace who is responsible for each dataset. "
            "Those records make it clear how to challenge misuse."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/drr-schema.yaml}",
            "\\texttt{schemas/aeip/incident-report-schema.json}",
            "\\texttt{schemas/aeip-template.yaml}",
        ],
    },
    "source/chapters/chapter-06-layer3-model-development.tex": {
        "narrative_intent": (
            "Layer 3 addresses the opacity of model engineering by prescribing transparent development records that align "
            "safety, accountability, and iterative improvement."
        ),
        "normative_clauses": [
            "Engineers SHALL document architectural choices in \\texttt{schemas/aeip/modelcard-schema.json} before models exit sandbox testing.",
            "Product owners SHALL supplement release packages with \\texttt{schemas/modelcard-template.yaml} attachments so evaluators can reuse evidence structures.",
            "Risk reviewers SHOULD link mitigation decisions to \\texttt{schemas/decision-rationale-record.jsonld} entries for traceability across layers.",
        ],
        "plain_summary": (
            "This layer makes model building legible to outsiders. "
            "It requires structured model cards and decision logs before release. "
            "Teams learn which forms to use so audits are repeatable. "
            "The process keeps technical improvements tied to governance expectations."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/aeip/modelcard-schema.json}",
            "\\texttt{schemas/modelcard-template.yaml}",
            "\\texttt{schemas/decision-rationale-record.jsonld}",
        ],
    },
    "source/chapters/chapter-07-layer4-instruction-and-control.tex": {
        "narrative_intent": (
            "Layer 4 responds to the practical risk that instructions and prompts can quietly override safeguards, "
            "mandating a control regime that treats command channels as auditable infrastructure."
        ),
        "normative_clauses": [
            "Operators SHALL register instructional flows with \\texttt{schemas/aeip/instruction-log-schema.json} to expose who issued which commands and why.",
            "Stewards SHALL link contested instruction sessions to \\texttt{schemas/interpretive-trace-package.jsonld} artefacts for reconstructing context.",
            "Oversight reviewers SHOULD summarise control efficacy within \\texttt{schemas/oversight-audit-memo.jsonld} to capture governance responses.",
        ],
        "plain_summary": (
            "This layer makes sure every instruction given to an AI system is traceable. "
            "It records who said what, how the system responded, and whether the process was safe. "
            "When questions arise, investigators can replay the context. "
            "Public reviewers also see how control lessons feed back into governance."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/aeip/instruction-log-schema.json}",
            "\\texttt{schemas/interpretive-trace-package.jsonld}",
            "\\texttt{schemas/oversight-audit-memo.jsonld}",
        ],
    },
    "source/chapters/chapter-08-layer5-reasoning-exchange.tex": {
        "narrative_intent": (
            "Layer 5 is designed for the human problem of inscrutable AI deliberations, forcing conversation trails to be "
            "legible, contestable, and aligned with civic norms."
        ),
        "normative_clauses": [
            "Dialogue stewards SHALL preserve exchange transcripts within \\texttt{schemas/interpretive-trace-package.jsonld} to capture context and participants.",
            "Facilitators SHALL reconcile vocabulary conflicts using \\texttt{schemas/svc/semantic-registry.jsonld} before approving automated reasoning policies.",
            "Governance publishers SHOULD summarise debate outcomes through \\texttt{schemas/governance-decision-summary.jsonld} so civic readers see the implications.",
        ],
        "plain_summary": (
            "This layer keeps AI-human conversations accountable. "
            "It stores dialogue, checks language, and reports what decisions came out of the exchange. "
            "People can replay the reasoning trail without special tools. "
            "That visibility protects against hidden persuasion or bias."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/interpretive-trace-package.jsonld}",
            "\\texttt{schemas/svc/semantic-registry.jsonld}",
            "\\texttt{schemas/governance-decision-summary.jsonld}",
        ],
    },
    "source/chapters/chapter-09-layer6-deployment-and-integration.tex": {
        "narrative_intent": (
            "Layer 6 confronts the operational fear that models will be deployed without context-aware safeguards, "
            "linking rollout decisions to observable accountability checkpoints."
        ),
        "normative_clauses": [
            "Release managers SHALL register launch justifications within \\texttt{schemas/decision-rationale-record.jsonld} before systems go live.",
            "Operational leads SHALL associate each integration with \\texttt{schemas/aeip/incident-report-schema.json} triggers to pre-plan remediation pathways.",
            "Auditors SHOULD reference \\texttt{schemas/oam-schema.yaml} when documenting deployment oversight findings for the public record.",
        ],
        "plain_summary": (
            "This layer explains how deployments are approved and monitored. "
            "It captures the reasoning behind go-live decisions and the safety nets around them. "
            "Teams learn which records to check before shipping updates. "
            "Residents can see what will happen if things fail."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/decision-rationale-record.jsonld}",
            "\\texttt{schemas/aeip/incident-report-schema.json}",
            "\\texttt{schemas/oam-schema.yaml}",
        ],
    },
    "source/chapters/chapter-10-layer7-governance-publication.tex": {
        "narrative_intent": (
            "Layer 7 responds to the common opacity of governance outputs by detailing how deliberations, approvals, and "
            "remediation reports must be published in accessible formats."
        ),
        "normative_clauses": [
            "Governance offices SHALL release canonical summaries using \\texttt{schemas/governance-decision-summary.jsonld} within statutory publication windows.",
            "Oversight chairs SHALL lodge review conclusions through \\texttt{schemas/oam-schema.yaml} whenever audits touch multiple layers.",
            "Communications teams SHOULD cross-link civic briefings to \\texttt{schemas/oversight-audit-memo.jsonld} artefacts to preserve interpretive transparency.",
        ],
        "plain_summary": (
            "This chapter tells institutions how to publish their decisions. "
            "It ensures the same templates are used so people know where to look. "
            "It also keeps audit findings tied to official releases. "
            "Readers get a predictable path to the evidence behind announcements."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/governance-decision-summary.jsonld}",
            "\\texttt{schemas/oam-schema.yaml}",
            "\\texttt{schemas/oversight-audit-memo.jsonld}",
        ],
    },
    "source/chapters/chapter-11-layer8-civic-participation.tex": {
        "narrative_intent": (
            "Layer 8 addresses the exclusion residents feel when AI governance proceeds without their input, specifying how "
            "participatory mechanisms must be recorded and honoured."
        ),
        "normative_clauses": [
            "Custodians SHALL register participation sessions via \\texttt{schemas/aeip/tecl-schema.json} to show who was invited and how feedback shaped obligations.",
            "Engagement leads SHALL attach dialogue archives within \\texttt{schemas/interpretive-trace-package.jsonld} for public review.",
            "Facilitators SHOULD refresh participation glossaries through \\texttt{schemas/svc/semantic-registry.jsonld} so residents understand procedural terms.",
        ],
        "plain_summary": (
            "This layer guarantees that community voices are not symbolic. "
            "It records meetings, attendance, and how ideas change the stack. "
            "People can see whether their feedback mattered. "
            "The language is kept clear so newcomers can engage."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/aeip/tecl-schema.json}",
            "\\texttt{schemas/interpretive-trace-package.jsonld}",
            "\\texttt{schemas/svc/semantic-registry.jsonld}",
        ],
    },
    "source/chapters/chapter-12-aeip-framework-and-operations.tex": {
        "narrative_intent": (
            "This chapter tackles the coordination burden of evidence gathering by explaining how the AEIP becomes the "
            "backbone for lifecycle assurance and multi-party accountability."
        ),
        "normative_clauses": [
            "Implementers SHALL instantiate assurance packages using \\texttt{schemas/aeip-template.yaml} before work enters regulated stages.",
            "Programme leads SHALL align lifecycle checkpoints with the enumerations in \\texttt{schemas/aeip-1-3.jsonld} to maintain interoperability across jurisdictions.",
            "Custodians SHOULD validate cross-layer linkages against \\texttt{schemas/aeip/aeip-frame-schema.json} prior to closing audits.",
        ],
        "plain_summary": (
            "This chapter shows how the AEIP keeps every promise and artefact stitched together. "
            "It walks teams through the templates that must be filled out. "
            "Readers see how those records travel across legal and technical reviews. "
            "Following the AEIP makes audits faster and fairer."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/aeip-template.yaml}",
            "\\texttt{schemas/aeip-1-3.jsonld}",
            "\\texttt{schemas/aeip/aeip-frame-schema.json}",
        ],
    },
    "source/chapters/chapter-13-persona-architecture-integration.tex": {
        "narrative_intent": (
            "This chapter addresses the confusion that arises when human and synthetic personas blur, guiding how roles, "
            "permissions, and accountability boundaries stay intelligible across systems."
        ),
        "normative_clauses": [
            "Integrators SHALL map persona capabilities within \\texttt{schemas/persona/persona-manifest.jsonld} before exposing them to civic interfaces.",
            "Custodians SHALL register stewardship assignments in \\texttt{schemas/persona/registry.jsonld} so role limits are machine-readable.",
            "Auditors SHOULD connect behavioural reviews to \\texttt{schemas/interpretive-trace-package.jsonld} artefacts for contextual accountability.",
        ],
        "plain_summary": (
            "This chapter explains who is allowed to act on behalf of the stack. "
            "It documents what each persona can and cannot do. "
            "The records make it clear when a persona changes or is removed. "
            "People can check those logs to see whether boundaries are respected."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/persona/persona-manifest.jsonld}",
            "\\texttt{schemas/persona/registry.jsonld}",
            "\\texttt{schemas/interpretive-trace-package.jsonld}",
        ],
    },
    "source/chapters/chapter-14-epistemology-by-design.tex": {
        "narrative_intent": (
            "Epistemology by design tackles the difficulty of proving that knowledge claims inside the stack have "
            "verifiable sources, aligning semantics, evidence, and audit pathways."
        ),
        "normative_clauses": [
            "Researchers SHALL bind contested terms to \\texttt{schemas/svc/semantic-registry.jsonld} entries before they influence obligations.",
            "Custodians SHALL register provenance updates within \\texttt{schemas/integrity-ledger-entry.jsonld} to preserve audit trails.",
            "Analysts SHOULD attach inference narratives to \\texttt{schemas/interpretive-trace-package.jsonld} artefacts when documenting knowledge transitions.",
        ],
        "plain_summary": (
            "This chapter makes knowledge claims trackable. "
            "It links definitions, evidence, and reasoning in one place. "
            "Teams see which ledgers to update when facts change. "
            "That way, anyone can challenge or confirm how the stack knows something."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/svc/semantic-registry.jsonld}",
            "\\texttt{schemas/integrity-ledger-entry.jsonld}",
            "\\texttt{schemas/interpretive-trace-package.jsonld}",
        ],
    },
    "source/chapters/chapter-15-governance-transport-and-maturity-model.tex": {
        "narrative_intent": (
            "This chapter solves the challenge of moving the stack between organisations and jurisdictions, clarifying "
            "what maturity milestones must be met before responsibilities are handed over."
        ),
        "normative_clauses": [
            "Transition leads SHALL document readiness assessments in \\texttt{schemas/oam-schema.yaml} to record oversight coverage.",
            "Governance stewards SHALL publish maturity roadmaps referencing \\texttt{schemas/governance-decision-summary.jsonld} so receiving institutions know residual risks.",
            "Auditors SHOULD capture transfer verdicts via \\texttt{schemas/oversight-audit-memo.jsonld} to maintain continuity of accountability.",
        ],
        "plain_summary": (
            "This chapter helps teams hand off responsibility without losing trust. "
            "It defines the documents that prove readiness. "
            "Incoming operators can see what has been checked and what remains. "
            "Communities get a transparent view of stewardship changes."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/oam-schema.yaml}",
            "\\texttt{schemas/governance-decision-summary.jsonld}",
            "\\texttt{schemas/oversight-audit-memo.jsonld}",
        ],
    },
    "source/chapters/chapter-16-strategic-resilience-and-risk-mitigation.tex": {
        "narrative_intent": (
            "Strategic resilience confronts the worry that AI governance collapses under stress, ensuring risk scenarios, "
            "response plays, and recovery commitments are documented before crises occur."
        ),
        "normative_clauses": [
            "Risk officers SHALL log resilience indicators within \\texttt{schemas/integrity-ledger-entry.jsonld} so deterioration is observable.",
            "Response teams SHALL pre-authorise contingency triggers using \\texttt{schemas/aeip/incident-report-schema.json} to accelerate remediation.",
            "Strategists SHOULD connect scenario exercises to \\texttt{schemas/interpretive-trace-package.jsonld} artefacts to capture lessons for future cycles.",
        ],
        "plain_summary": (
            "This chapter prepares the stack for shocks. "
            "It stores the thresholds, playbooks, and learning artefacts needed to recover. "
            "Teams know exactly where to report weaknesses. "
            "Communities can confirm that resilience is practiced, not just promised."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/integrity-ledger-entry.jsonld}",
            "\\texttt{schemas/aeip/incident-report-schema.json}",
            "\\texttt{schemas/interpretive-trace-package.jsonld}",
        ],
    },
    "source/chapters/chapter-17-meta-audit-and-self-accountability.tex": {
        "narrative_intent": (
            "Meta-audit addresses the question of who watches the guardians, describing how the stack inspects its own "
            "controls and invites external challenge."
        ),
        "normative_clauses": [
            "Audit anchors SHALL produce oversight verdicts via \\texttt{schemas/oversight-audit-memo.jsonld} to display method and scope.",
            "Custodians SHALL register self-audit findings within \\texttt{schemas/integrity-ledger-entry.jsonld} to expose remedial actions.",
            "Governance leads SHOULD compare self-assessment outcomes with \\texttt{schemas/aeip/aeip-frame-schema.json} to ensure each layer remains covered.",
        ],
        "plain_summary": (
            "This chapter explains how the stack audits itself. "
            "It records findings in shared ledgers and templates. "
            "The process keeps self-review honest by inviting outside scrutiny. "
            "Readers can trace how identified issues are resolved."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/oversight-audit-memo.jsonld}",
            "\\texttt{schemas/integrity-ledger-entry.jsonld}",
            "\\texttt{schemas/aeip/aeip-frame-schema.json}",
        ],
    },
    "source/chapters/chapter-18-interpretive-and-temporal-continuity.tex": {
        "narrative_intent": (
            "This chapter solves the risk of obligations drifting over time by enforcing interpretive continuity, showing "
            "how each era’s context is preserved for future stewards."
        ),
        "normative_clauses": [
            "Custodians SHALL maintain continuity dossiers within \\texttt{schemas/interpretive-trace-package.jsonld} so future readers inherit full context.",
            "Semantic stewards SHALL track evolving terminology through \\texttt{schemas/svc/semantic-registry.jsonld} to flag meaning shifts.",
            "Governance historians SHOULD document temporal reconciliations in \\texttt{schemas/integrity-ledger-entry.jsonld} to evidence why clauses persist or change.",
        ],
        "plain_summary": (
            "This chapter keeps the stack understandable across decades. "
            "It stores context packages, vocabulary updates, and ledger entries together. "
            "Future teams can see why decisions were made. "
            "That transparency prevents quiet rewrites of civic commitments."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/interpretive-trace-package.jsonld}",
            "\\texttt{schemas/svc/semantic-registry.jsonld}",
            "\\texttt{schemas/integrity-ledger-entry.jsonld}",
        ],
    },
    "source/chapters/chapter-19-epilogue-the-stack-as-living-constitution.tex": {
        "narrative_intent": (
            "The epilogue addresses the challenge of keeping the stack a living constitution, emphasising how stewardship, "
            "public oversight, and iterative amendments stay synchronised."
        ),
        "normative_clauses": [
            "Custodians SHALL log constitutional updates within \\texttt{schemas/integrity-ledger-entry.jsonld} to evidence legitimacy.",
            "Governance councils SHALL publish amendment rationales via \\texttt{schemas/governance-decision-summary.jsonld} for civic review.",
            "Stewards SHOULD refresh lifecycle commitments through \\texttt{schemas/aeip-template.yaml} whenever the constitution evolves.",
        ],
        "plain_summary": (
            "The epilogue reminds readers that the stack must keep adapting without losing its soul. "
            "It records how changes are logged, explained, and adopted. "
            "People can see which commitments endure and which are reworked. "
            "The framework stays alive because every change is accountable."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/integrity-ledger-entry.jsonld}",
            "\\texttt{schemas/governance-decision-summary.jsonld}",
            "\\texttt{schemas/aeip-template.yaml}",
        ],
    },
    "source/interpretive/chapter-19a-usage-and-trust.tex": {
        "narrative_intent": (
            "This interpretive chapter tackles the human anxiety that usage agreements are empty words, translating the "
            "stack’s operational norms into daily practice for participants."
        ),
        "normative_clauses": [
            "Custodians SHALL capture trust covenants using \\texttt{schemas/aeip/tecl-schema.json} before onboarding new communities.",
            "Operators SHALL log breaches or exceptions via \\texttt{schemas/aeip/incident-report-schema.json} so restitution obligations activate.",
            "Trust monitors SHOULD update public dashboards referencing \\texttt{schemas/integrity-ledger-entry.jsonld} to prove adherence over time.",
        ],
        "plain_summary": (
            "This chapter explains how everyday users can rely on the stack. "
            "It lists the agreements, incident processes, and transparency tools they can point to. "
            "People see exactly where promises live and how to enforce them. "
            "Trust is earned by recording proof, not slogans."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/aeip/tecl-schema.json}",
            "\\texttt{schemas/aeip/incident-report-schema.json}",
            "\\texttt{schemas/integrity-ledger-entry.jsonld}",
        ],
    },
    "source/interpretive/chapter-20-rhetoric-and-semantics.tex": {
        "narrative_intent": (
            "This chapter tackles semantic drift and rhetorical manipulation, ensuring language across the stack remains "
            "faithful to civic intent rather than marketing spin."
        ),
        "normative_clauses": [
            "Semantic stewards SHALL register contested or novel terms in \\texttt{schemas/svc/semantic-registry.jsonld} before publication.",
            "Authors SHALL attach annotated discourse records via \\texttt{schemas/interpretive-trace-package.jsonld} to expose persuasive context.",
            "Drafting teams SHOULD log AI-assisted edits through \\texttt{schemas/governance/ai-assisted-drafting.jsonld} to disclose machine contributions.",
        ],
        "plain_summary": (
            "This chapter keeps the stack’s language honest. "
            "It records definitions, rhetorical context, and AI editing trails. "
            "Readers can see how words are chosen and challenged. "
            "That clarity protects the public from subtle semantic shifts."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/svc/semantic-registry.jsonld}",
            "\\texttt{schemas/interpretive-trace-package.jsonld}",
            "\\texttt{schemas/governance/ai-assisted-drafting.jsonld}",
        ],
    },
    "source/interpretive/chapter-21-companion-trap.tex": {
        "narrative_intent": (
            "The companion trap examines how relational AI can blur autonomy, instructing implementers on preserving "
            "healthy boundaries between human care and synthetic personas."
        ),
        "normative_clauses": [
            "Custodians SHALL register intimacy safeguards within \\texttt{schemas/persona/registry.jsonld} before deploying companionship features.",
            "Design leads SHALL document persona behaviour constraints using \\texttt{schemas/persona/persona-manifest.jsonld} to prevent exploitative patterns.",
            "Clinical governance teams SHOULD correlate wellbeing metrics with \\texttt{schemas/therapy/credential-verification.jsonld} to ensure licensed oversight.",
        ],
        "plain_summary": (
            "This chapter warns against letting AI companions quietly replace human support. "
            "It defines the guardrails that keep intimacy respectful and transparent. "
            "Readers can check which experts oversee these systems. "
            "Communities learn how to halt designs that cross ethical lines."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/persona/registry.jsonld}",
            "\\texttt{schemas/persona/persona-manifest.jsonld}",
            "\\texttt{schemas/therapy/credential-verification.jsonld}",
        ],
    },
    "source/interpretive/chapter-22-persona-architecture.tex": {
        "narrative_intent": (
            "This chapter focuses on maintaining persona governance as the stack evolves, giving institutions tools to "
            "track duties, rights, and constraints attached to each role."
        ),
        "normative_clauses": [
            "Persona stewards SHALL update role inventories within \\texttt{schemas/persona/persona-manifest.jsonld} whenever responsibilities shift.",
            "Custodians SHALL ensure persona approvals align with \\texttt{schemas/persona/registry.jsonld} entries before activation.",
            "Governance councils SHOULD verify cross-layer coverage against \\texttt{schemas/aeip/aeip-frame-schema.json} when introducing new personas.",
        ],
        "plain_summary": (
            "This chapter keeps persona management disciplined. "
            "It shows how to update role manifests and check approvals. "
            "New personas are tested against the entire stack. "
            "People can trust that no role appears without review."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/persona/persona-manifest.jsonld}",
            "\\texttt{schemas/persona/registry.jsonld}",
            "\\texttt{schemas/aeip/aeip-frame-schema.json}",
        ],
    },
    "source/interpretive/chapter-23-therapy-tech-and-governance-of-care.tex": {
        "narrative_intent": (
            "This chapter responds to concerns that AI therapy tools could harm patients by clarifying credentialing, "
            "incident response, and persona responsibilities in clinical settings."
        ),
        "normative_clauses": [
            "Clinical operators SHALL verify practitioner status through \\texttt{schemas/therapy/credential-verification.jsonld} before AI-assisted care begins.",
            "Custodians SHALL report adverse events using \\texttt{schemas/aeip/incident-report-schema.json} within mandated health timelines.",
            "Care designers SHOULD align therapeutic personas with \\texttt{schemas/persona/persona-manifest.jsonld} to delineate authority and escalation paths.",
        ],
        "plain_summary": (
            "This chapter protects people who rely on AI-assisted therapy. "
            "It checks clinician credentials, tracks incidents, and clarifies roles. "
            "Patients can see which professionals are accountable. "
            "If harm occurs, the response steps are already mapped."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/therapy/credential-verification.jsonld}",
            "\\texttt{schemas/aeip/incident-report-schema.json}",
            "\\texttt{schemas/persona/persona-manifest.jsonld}",
        ],
    },
    "source/interpretive/chapter-24-governance-paradox.tex": {
        "narrative_intent": (
            "The governance paradox addresses the fear that AI oversight becomes performative, outlining how to balance "
            "automation assistance with human accountability in rulemaking."
        ),
        "normative_clauses": [
            "Policymaking teams SHALL disclose algorithmic drafting inputs via \\texttt{schemas/governance/ai-assisted-drafting.jsonld} for every major revision.",
            "Oversight bodies SHALL record paradox resolutions in \\texttt{schemas/oversight-audit-memo.jsonld} so contradictions are publicly examined.",
            "Custodians SHOULD log final settlements within \\texttt{schemas/integrity-ledger-entry.jsonld} to demonstrate how authority was ultimately exercised.",
        ],
        "plain_summary": (
            "This chapter makes sure AI help does not replace accountable governance. "
            "It documents where machines assist, how conflicts are reviewed, and who signs off. "
            "Readers can track the debate from draft to decision. "
            "That transparency keeps power grounded in human responsibility."
        ),
        "enforcement_schemas": [
            "\\texttt{schemas/governance/ai-assisted-drafting.jsonld}",
            "\\texttt{schemas/oversight-audit-memo.jsonld}",
            "\\texttt{schemas/integrity-ledger-entry.jsonld}",
        ],
    },
}
