<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# AI OSI Stack Dashboard

This Vite + React + TypeScript workspace renders the canonical AI OSI Stack governance dashboard with offline civic data scaffolds and accessibility-first controls.

## Quickstart

```bash
cd dashboard
npm install
npm run validate:data
npm run dev
```

- `npm run validate:data` — checks JSON payloads against AJV schemas.
- `npm run typecheck` — runs TypeScript in strict mode without emitting files.
- `npm run test` — executes Vitest (unit + axe-based accessibility checks).
- `npm run storybook` — launches Storybook with Accessibility and Interactions addons.
- `npm run build` — generates the static site in `dist/`.
- `npm run preview` — previews the production build locally.

## Data Model References

Structured data lives under `src/data/` with schemas in `src/data/schemas/`.

- `layers.json` — layer registry + canonical version metadata.
- `artifacts.json` — governance artifact catalogue.
- `personas.json` — persona manifest with stewardship registers.
- `update_plans.json` — structural, custodial, and interpretive roadmap.
- `glossary.json` — civic glossary with provenance links.
- `data/aeip/*.jsonld` — mock AEIP v1.3 receipts powering the log viewer.

Validate all payloads via `npm run validate:data` or inside Husky pre-commit hooks.

## Testing & Accessibility

Tests live in `src/components/__tests__/` and `src/__tests__/`.

- Unit coverage for LayerCard, AEIPLogViewer, and GlossaryDrawer.
- Accessibility assertions powered by `vitest-axe`.
- Global i18n utilities and accessibility helpers live in `src/i18n/` and `src/utils/accessibility.ts`.

## Storybook

Storybook stories for each dashboard component are located in `src/stories/`. Use them to demo states without running the full app:

```bash
npm run storybook
```

Build the static Storybook output with:

```bash
npm run build-storybook
```

## Docker & Static Preview

Build and run the static container locally:

```bash
docker compose -f dashboard/docker-compose.yml up --build
```

The image uses a Node build stage and serves static assets via `nginx:alpine` with gzip and far-future caching.

## Continuous Integration

GitHub Actions workflows under `.github/workflows/` run data validation, linting, tests, Storybook builds, and Docker image builds on every push and pull request. A dedicated `preview.yml` workflow publishes the static build to GitHub Pages when enabled.

## Civic Accessibility Notes

Implemented per Update Plans 2–3:

- Skip links, keyboard-visible focus outlines, and reduced-motion awareness.
- Triple-register toggle (Narrative · Normative · Plain) across layer narratives.
- Glossary search drawer with keyboard focus targets and CEFR-B2 placeholders.
- AEIP log modal exposing privacy, countersignature, and hash context for each receipt.

// TODO: integrate live AEIP, persona, and governance APIs when ratified by the stewardship council.
