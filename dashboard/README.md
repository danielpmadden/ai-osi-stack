# AI OSI Stack Dashboard Blueprint

This directory scaffolds a static React/Tailwind/Shadcn prototype for visualizing the AI OSI Stack governance layers.

## Folder Structure
```
dashboard/
  ├── Dockerfile              # Container scaffold for future static build serving
  ├── README.md               # This file
  └── src/
      ├── components/
      │   └── Dashboard.tsx   # Primary dashboard component with mock data bindings
      └── data/
          └── layers.json     # Placeholder canonical data for layers, artifacts, and version banner
```

Additional directories to add during implementation:
- `src/components/layers/` for reusable LayerCard, RiskList, AEIPHookBadge.
- `src/components/layout/` for Sidebar, TopBar, IntegrityBadge.
- `src/data/` modules (`ledger.ts`, `timeline.ts`) to parse repository artifacts.
- `src/lib/` for context providers and mock API adapters.
- `public/` for static assets (logos, accessibility icons).

## Mock Data & Static Content
- `layers.json` aggregates layer metadata, evidence pointers, and AEIP hooks.
- Update Plan references are embedded as narrative rationale for future linking to timeline component.
- Artifact gallery preview references ledger hashes to prepare for integrity badge rollups.

## Next Implementation Steps
1. **Set up Tooling**
   - Initialize Vite + React + TypeScript + Tailwind + Shadcn UI.
   - Configure ESLint/Prettier with repository style guide.
2. **Build Core Layout**
   - Implement Sidebar, TopBar, and LayerCard components using Tailwind tokens respecting WCAG AA.
   - Wire React Context to manage selected layer, persona filters, and transparency toggle.
3. **Data Integration**
   - Create parsing utilities that transform `/ledger/*.json` and `/docs/*.md` into typed records.
   - Implement static generation script to hydrate `layers.json` before build.
4. **Governance Features**
   - Add Integrity Badge aggregator reading dignityCompliance fields.
   - Implement Right-to-Opacity controls masking sensitive fields on demand.
   - Provide AEIP Log Viewer timeline stub using sample events extracted from `ledger/ile.json`.
5. **Future Integrations**
   - Introduce AEIP CLI client for live handshake ingestion (feature flagged).
   - Integrate OpenAI API for contextual narratives (with governance disclosure logging).
   - Expand Dockerfile to run build & serve steps with environment variable gates for live APIs.

## Notes on Ethics & Transparency
- Embed comments referencing Update Plan clauses (e.g., Update Plan 8 for transparency safeguards).
- Include accessible descriptions for integrity indicators and ensure focus management for modals.
- Maintain offline-first operation per repository blueprint until governance council ratifies production deployment.

