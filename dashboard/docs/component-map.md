# AI OSI Stack Dashboard Component Map

| Component | Purpose | Data Source | Key Props / State | Accessibility Notes |
| --- | --- | --- | --- | --- |
| `LayerCard` | Render governance layer triple-register narrative with risk, artifact, persona, and AEIP hook summaries. | `layers.json` | Props: `layer` (`Layer`). State: `registerKey` for Narrative/Normative/Plain toggle. | ARIA tablist with arrow-key support, focus-visible styling, CEFR-B2 placeholder live region, translation fidelity notices. |
| `ArtifactGallery` | Display canonical artifacts grouped by layer. | `artifacts.json`, `layers.json` | Props: `artifacts`, `layers`. | Semantic lists, canonical badges, grouped cards with live counts, glossary-ready descriptions. |
| `AEIPLogViewer` | Surface AEIP reasoning receipts with modal detail. | `data/aeip/*.jsonld` | Props: `receipts`. State: `query`, `activeReceipt`. | Searchable list, hash chips, modal exposes privacy/intent fields, JSON-LD pretty print, reduced-motion aware transitions. |
| `VersionTimeline` | Visualize Update Plan chronology. | `update_plans.json` | Props: `plans`. | Ordered list timeline with WCAG-AA color tokens and structural/custodial/interpretive legends. |
| `IntegrityBadge` | Present canonical version, DOI, and hash fingerprint. | `layers.json` (`canonical_version`) | Props: `canonical`. | High-contrast badge with status dot, DOI/hash text, future ledger hook placeholder. |
| `GlossaryDrawer` | Provide searchable civic glossary overlay. | `glossary.json` | Props: `terms`. State: `isOpen`, `query`. | Toggle button with aria-expanded, ESC-to-close listener, keyboard-focusable list items, translation-ready strings. |
| `Dashboard` (page) | Compose sidebar navigation, layer cards, timeline, AEIP log, and glossary drawer. | All JSON payloads + i18n strings | Derived props from parsed Zod payloads, imports `aeipReceipts`. | Landmarks, skip link target, persona count live region, neutral contrast shell. |
| `About` (page) | Static context for stewardship roadmap. | — | — | Plain-language summary, TODO for conformance reports. |
