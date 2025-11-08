# AI OSI Stack Dashboard Architecture Proposal

## Component Overview
| Component | Description | Primary Data Sources | Future Integrations |
| --- | --- | --- | --- |
| **Sidebar Navigation** | Persistent left rail with global navigation, persona-aware filters, and contextual transparency toggle. | `docs/architecture-overview.md`, `docs/governance-map.md` | AEIP persona registry lookup (AEIP CLI), role-based access control via OpenAI auth proxy. |
| **Top Bar / Canonical Banner** | Displays version label, hash, DOI, timestamp, and integrity badge summarizing dignity compliance. | `versions/readme.md`, `ledger/integrity/notices/*.txt`, `dashboard/src/data/layers.json` | Automated hash refresh from AEIP receipts; OpenAI API for context-aware announcements. |
| **Layer View** | Scrollable stack of cards for Layers 0–8, each showing purpose, risks, evidence, AEIP hooks, and transparency controls. | `docs/risk-taxonomy.md`, `docs/governance-map.md`, `ledger/*.json`, `dashboard/src/data/layers.json` | Live maturity scores via AEIP node metrics; optional OpenAI summarization for persona rationales. |
| **Governance Map Panel** | Matrix visualization of risks vs. controls with sentinel indicators. | `docs/governance-map.md`, `docs/risk-taxonomy.md` | Ingest periodic CSV exports from risk tooling; AEIP risk streaming endpoint. |
| **Artifact Gallery** | Modal/grid view listing artifacts (GDS, DRR, ITP, Model Card, Solomon Brief, Clarity Package) with hashes and seals. | `/ledger/*.json`, `docs/aeip-artifact-schema-templates.md`, `protocol/*` | Integrate AEIP receipt verification CLI; optional OpenAI Q&A summarizing artifacts. |
| **AEIP Log Viewer** | Timeline drawer visualizing Intent→Update handshake events with filter chips. | `ledger/ile.json`, `schemas/aeip-1-3.jsonld`, `docs/ai-osi-protocol-spec.md` | Streaming AEIP node logs; WebSocket bridge to CLI; optional Dockerized AEIP simulator. |
| **Integrity Badge Widget** | Aggregates dignityCompliance flags and temporal seals into layered badge. | `ledger/gds.json`, `ledger/drr.json`, `ledger/itp.json` | Live badge signing via AEIP node; OpenAI endpoint for anomaly narratives. |
| **Version Timeline** | Horizontal timeline aligning Update Plans, ledger notices, and release tags. | `versions/historical/update-plan-*.md`, `ledger/integrity/notices/*.txt`, `versions/ai-osi-stack-v5.pdf` metadata | Automated ingestion of future release manifests; governance CLI for milestone creation. |

## Data Flow & Mock APIs
1. **Static Data Loader:** `dashboard/src/data/layers.json` seeds initial state for React context (`LayerDataProvider`).
2. **Ledger Adapter:** Utility functions in `dashboard/src/data/ledger.ts` (to be created) parse `/ledger/*.json` for artifact cards and integrity badge.
3. **Update Plan Indexer:** Parser module reads `/versions/historical/*.md` to populate version timeline; preprocessed via script `scripts/build-timeline.py` (future).
4. **Mock API Endpoints:**
   - `GET /api/mock/layers` → returns contents of `dashboard/src/data/layers.json`.
   - `GET /api/mock/aeip/logs` → returns truncated `ledger/ile.json` handshake events.
   - `GET /api/mock/artifacts` → aggregated list of artifacts with hash + seal data.
   - `GET /api/mock/version-timeline` → synthetic list of Update Plan milestones.
   (For static site prototyping these endpoints can be implemented as local JSON imports.)

## State Management Strategy
- Use React Context or Zustand store to share canonical version info, selected layer, and opacity preferences across components.
- Compose selectors for persona filters (actors) and standard alignment overlays using derived data from JSON schemas.

## Accessibility & Ethics Considerations
- Enforce WCAG AA by leveraging Tailwind tokens for contrast and Shadcn components with accessible variants.
- Provide textual alternatives for integrity badges and timeline events.
- Implement Right-to-Opacity toggles per layer: hide sensitive data fields when toggled.

## Deployment Notes
- Offline-first static build via Vite or Next.js static export; no network calls required initially.
- Future Docker image exposes static build served by lightweight Node/Express or Nginx; AEIP/OpenAI integrations remain behind feature flags.

## Accountability Hooks
- Annotate component code with comments linking to normative sources (e.g., `// Layer 4: Update Plan 8 Right-to-Opacity`).
- Include audit log stub capturing user interactions (filter changes) for governance review; stored locally until AEIP sync enabled.

