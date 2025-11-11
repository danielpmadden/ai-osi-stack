---
Title: AEIP Governance Spine Specification
Version: 5.0.0
Status: Canonical Draft
License: CC BY-NC-ND 4.0
---

# AEIP Specification

The AI Exchange Interface Protocol (AEIP) defines the civic message envelope that transports governance events across the stack. Each message SHALL include:

- **Header Fields**: civic-layer identifier, originating authority, persona context, and semantic version references.
- **Routing Table**: ordered list of civic nodes (municipal registries, archives, oversight forums) with signed hops.
- **Signature Block**: multi-party cryptographic attestations aligned with the Civic Charter and Integrity Ledger hashes.
- **Temporal Seal**: synchronized timestamp cluster with drift tolerance and verification hash chain.
- **Payload Contract**: declarative schema pointer referencing the constitutional clause being exercised.

## JSON Schema Reference

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "AEIP Envelope",
  "type": "object",
  "required": [
    "aeip_version",
    "header",
    "routing",
    "signatures",
    "temporal_seal",
    "payload_reference"
  ],
  "properties": {
    "aeip_version": {
      "type": "string",
      "pattern": "^5\\.\\d+\\.\\d+$",
      "description": "Semantic version for AEIP compatibility."
    },
    "header": {
      "type": "object",
      "required": ["civic_layer", "originating_authority", "persona_id", "svc_pointer"],
      "properties": {
        "civic_layer": { "type": "string", "enum": ["L0","L1","L2","L3","L4","L5","L6","L7","L8"] },
        "originating_authority": { "type": "string" },
        "persona_id": { "type": "string" },
        "svc_pointer": { "type": "string", "description": "Reference to Semantic Version Control manifest." }
      }
    },
    "routing": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["node_id", "node_role", "signature_ref"],
        "properties": {
          "node_id": { "type": "string" },
          "node_role": { "type": "string" },
          "signature_ref": { "type": "string" }
        }
      }
    },
    "signatures": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["authority", "algorithm", "signature"],
        "properties": {
          "authority": { "type": "string" },
          "algorithm": { "type": "string" },
          "signature": { "type": "string" }
        }
      }
    },
    "temporal_seal": {
      "type": "object",
      "required": ["issued_at", "not_before", "not_after", "drift_tolerance"],
      "properties": {
        "issued_at": { "type": "string", "format": "date-time" },
        "not_before": { "type": "string", "format": "date-time" },
        "not_after": { "type": "string", "format": "date-time" },
        "drift_tolerance": { "type": "number", "minimum": 0 }
      }
    },
    "payload_reference": {
      "type": "object",
      "required": ["document_id", "clause_id", "hash_reference"],
      "properties": {
        "document_id": { "type": "string" },
        "clause_id": { "type": "string" },
        "hash_reference": { "type": "string" }
      }
    }
  }
}
```
