<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Schema Coherence & Normative Language Audit

_Generated: 2025-11-09 08:50 UTC_

## Normative Language Pulse
The table surfaces the documents with the highest share of modal (MUST/SHALL/SHOULD) language.
| Document | Normative Rate | Modal Share | Modal Hits |
| --- | --- | --- | --- |
| docs/README.md | 0.500 | 0.500 | 1 |
| docs/charter/charter.md | 0.500 | 0.500 | 1 |
| docs/governance-map.md | 0.400 | 0.500 | 5 |
| docs/ai-osi-protocol-spec.md | 0.417 | 0.458 | 11 |
| docs/example-output.md | 0.333 | 0.444 | 4 |
| docs/implementation-notes.md | 0.360 | 0.400 | 10 |
| docs/aeip-crosswalk-matrix.md | 0.333 | 0.400 | 6 |
| docs/aeip-spec-v1.md | 0.333 | 0.333 | 1 |

## Schema Field Clusters
Field names are vectorised with TF-IDF character n-grams when the scikit-learn stack is available; otherwise a prefix-based heuristic groups related terms.
| Cluster | Keywords | Field Count | Sample Fields |
| --- | --- | --- | --- |
| 0 | prope, rties | 1617 | properties; properties.id; properties.id.type; properties.id.pattern; properties.artifact_type; properties.artifact_type.const; properties.schema_ref; properties.schema_ref.const; properties.layer; properties.layer.const … |
| 1 | $defs, $defs | 391 | $defs; $defs.privacyScope; $defs.privacyScope.type; $defs.privacyScope.enum; $defs.privacyConsent; $defs.privacyConsent.type; $defs.privacyConsent.enum; $defs.privacyRedaction; $defs.privacyRedaction.type; $defs.privacyJustification … |
| 2 | defin, tions | 235 | definitions; definitions.aeip:artifactId; definitions.aeip:artifactId.description; definitions.aeip:version; definitions.aeip:version.description; definitions.aeip:lifecycleStage; definitions.aeip:lifecycleStage.description; definitions.aeip:layerPath; definitions.aeip:layerPath.description; definitions.aeip:receipts … |
| 3 | schem, chema | 144 | schema; schema.type; schema.required; schema.properties; schema.properties.id; schema.properties.id.type; schema.properties.version; schema.properties.version.type; schema.properties.source; schema.properties.source.type … |
| 4 | canon, adata | 126 | canonicalMetadata; canonicalMetadata.canonical_version; canonicalMetadata.canonical_date; canonicalMetadata.aeip_version; canonicalMetadata.repository_of_record; canonicalMetadata.domain_of_record; canonicalMetadata.supersedes_all_prior_metadata; canonicalMetadata; canonicalMetadata.canonical_version; canonicalMetadata.canonical_date … |
| 5 | examp, es[0] | 111 | examples[0].artifact_type; examples[0].version; examples[0].uuid; examples[0].timestamp; examples[0].layer; examples[0].issuer; examples[0].issuer.name; examples[0].issuer.role; examples[0].issuer.organization; examples[0].issuer.contact … |
| 6 | title, title | 24 | title; title; title; title; title; title; title; title; title; title … |
| 7 | requi, uired | 21 | required; required; required; required; required; required; required; required; required; required … |