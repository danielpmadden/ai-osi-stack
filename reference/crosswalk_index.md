Layer/Theme: reference_crosswalk_index
Version: v5.0-open-core
Purpose: Provide navigation links across the lowercase schema.

# Crosswalk Index

This index SHALL help readers locate artefacts within the flattened, lowercase directory structure.

## Foundation

- [foundation/overview.md](../foundation/overview.md)
- [foundation/context.md](../foundation/context.md)
- [foundation/design_principles.md](../foundation/design_principles.md)
- [foundation/glossary.md](../foundation/glossary.md)

## Layers

- [layers/civic_mandate.md](../layers/civic_mandate.md)
- [layers/ethical_charter.md](../layers/ethical_charter.md)
- [layers/data_stewardship.md](../layers/data_stewardship.md)
- [layers/model_development.md](../layers/model_development.md)
- [layers/instruction_control.md](../layers/instruction_control.md)
- [layers/deployment_integration.md](../layers/deployment_integration.md)
- [layers/governance_publication.md](../layers/governance_publication.md)
- [layers/reasoning_exchange.md](../layers/reasoning_exchange.md)
- [layers/civic_participation.md](../layers/civic_participation.md)

## Guides

- [guides/implementation_guide.md](../guides/implementation_guide.md)
- [guides/philosophy_ethics.md](../guides/philosophy_ethics.md)
- [guides/security_model.md](../guides/security_model.md)
- [guides/testing_framework.md](../guides/testing_framework.md)

## Reference

- [reference/comparative_models.md](comparative_models.md)
- [reference/faq.md](faq.md)
- [reference/roadmap.md](roadmap.md)
- [reference/crosswalk_index.md](crosswalk_index.md)

## Tools

- [tools/civic_verification.md](../tools/civic_verification.md)

Traceability

Keys: Reference=CrosswalkIndex-v5, Review_Cycle=on_change
Open Civic Artefacts

- Transparency Record: Crosswalk Maintenance Log
- Transparency Record: Navigation Feedback Register

```sql
-- Copy code
SELECT artefact_id, link_status
FROM transparency_registry
WHERE reference = 'crosswalk_index';
```
