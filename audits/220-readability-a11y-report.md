# Dashboard Readability & Accessibility Audit

## Scope & Method
- **Target**: `dashboard/` documentation, static copy, and UI implementations (React components, JSON data).
- **Approach**: Parsed Markdown sources for readability metrics, inspected React components for semantic/ARIA coverage, and reviewed glossary payloads for jargon coverage. Scripts computed Flesch–Kincaid grade levels and average sentence length.

## Readability Findings
- Aggregate average sentence length across `dashboard/README.md` and docs is **12.54 words**, well below the 25-word threshold. Individual files range from 9.48 to 14.53 words per sentence.【F:dashboard/README.md†L1-L104】【F:dashboard/docs/accessibility-checklist.md†L1-L26】【F:dashboard/docs/component-map.md†L1-L15】【F:audits/220-readability-a11y-report.json†L2-L19】
- Flesch–Kincaid grade levels fall between **12.54 and 15.68**, matching the expected “legal/academic but plain” tone for policymakers and non-engineers.【F:audits/220-readability-a11y-report.json†L2-L19】
- Plain-language register exists for each layer narrative via the triple-register copy, but `About.tsx` still contains roadmap TODO bullet points without contextual framing for new readers.【F:dashboard/src/pages/About.tsx†L1-L19】

## Jargon & Glossary Coverage
- Glossary payload enumerates AEIP, Integrity Ledger, Governance Disclosure Statement, Persona Brief, and Epistemology by Design definitions.【F:dashboard/src/data/glossary.json†L1-L32】
- High-frequency terms **not** represented in the glossary include CEFR-B2 and T-SIR, both highlighted in accessibility docs and utility helpers; policymakers lack immediate definitions for these acronyms.【F:dashboard/docs/accessibility-checklist.md†L9-L25】【F:dashboard/src/utils/accessibility.ts†L1-L94】
- Update Plan references (e.g., Update Plan 8, 9, 13) appear throughout `layers.json` and component copy without glossary cross-links. Consider adding a glossary entry or inline definition to keep non-engineers oriented.【F:dashboard/src/data/layers.json†L1-L198】

## Accessibility Observations
- **Landmarks & Navigation**: Skip link, labeled landmarks (`aria-label` on shell, nav, main section), and tablist semantics are implemented in `App.tsx`, `Dashboard.tsx`, and `LayerCard.tsx` consistent with Update Plans 2–3.【F:dashboard/src/App.tsx†L1-L18】【F:dashboard/src/pages/Dashboard.tsx†L1-L77】【F:dashboard/src/components/LayerCard.tsx†L1-L115】
- **Dialog & Drawer Behaviour**: AEIP modal declares `role="dialog"` with `aria-modal` and labeled controls, but focus trapping/return is not yet implemented; keyboard users can tab behind the modal.【F:dashboard/src/components/AEIPLogViewer.tsx†L1-L119】
- **Glossary Drawer**: Toggle button exposes `aria-expanded`, yet when closed the drawer uses `aria-hidden` without removing focusable list items (`tabIndex={0}`), leaving hidden content in the tab order. Recommend applying `inert`/`hidden` or gating tab stops until open.【F:dashboard/src/components/GlossaryDrawer.tsx†L1-L81】
- **Imagery & Captions**: No `<img>` assets are present; badges and icons use CSS/semantic spans with accessible labeling. Ensure future media adds descriptive alt text and captions.【F:dashboard/src/components/IntegrityBadge.tsx†L1-L22】

## Recommendations
1. Add glossary terms (or inline definitions) for CEFR-B2, T-SIR, and Update Plan references to preserve accessibility for non-specialists.
2. Implement modal focus trapping/return in `AEIPLogViewer` and suppress tab stops when `GlossaryDrawer` is closed to meet WCAG 2.1.1 keyboard requirements.
3. Replace roadmap TODO bullet points in `About.tsx` with plain-language context or move to a maintainer-only note to keep public copy actionable.
4. When introducing images or charts, enforce descriptive alt text and captions aligned with the dashboard’s civic audience expectations.
