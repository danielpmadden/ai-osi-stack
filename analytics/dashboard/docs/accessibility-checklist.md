<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Accessibility & Semantic Integrity Checklist

The following checklist operationalizes Update Plans 2 and 3, focusing on civic accessibility, semantic integrity, and dignity safeguards.

## Screen Reader & Semantic Structure
- [x] Provide ARIA labels and roles for navigation, tablists, dialogs, and complementary regions.
- [x] Ensure headings follow logical hierarchy within `LayerCard`, timeline, and modal components.
- [x] Announce CEFR-B2 readability placeholders via polite live regions for each layer.
- [x] Skip link wired to `#main-content` with focus-visible outlines for keyboard traversal.

## Triple-Register Comprehension
- [x] Narrative/Normative/Plain toggle implemented with ARIA tab semantics and keyboard arrow support.
- [x] Translation fidelity placeholders highlight pending T-SIR validator integration.
- [ ] TODO: Log register selection preferences per persona for interpretive analytics.

## Visual Contrast & Motion Preference
- [x] Tailwind palette constrained to WCAG-AA-compliant contrast values (slate/emerald spectrum).
- [x] Badge and timeline status colors selected for 4.5:1 contrast minimum.
- [x] Reduced-motion hook disables transition classes when users opt out of animation.

## Glossary & Plain-Language Support
- [x] Glossary drawer exposes search with keyboard access, tooltip-ready definitions, and plain-language descriptions.
- [x] Layer descriptions provide CEFR-B2-aligned plain register copy.
- [ ] TODO: Surface inline glossary hovers throughout LayerCard content.

## Provenance & Integrity Hooks
- [x] Integrity badge surfaces DOI, SHA512, and notice path for canonical verification.
- [x] AEIP log viewer renders modal with privacy, countersignature, and ledger details plus JSON-LD pretty print.
- [ ] TODO: Automate provenance sync across all components once AEIP endpoints are active.
