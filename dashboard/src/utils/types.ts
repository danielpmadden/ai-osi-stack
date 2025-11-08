// TODO: Extend with runtime fetch typing once AEIP/OpenAI integrations are enabled.

import { z } from "zod";

export const tripleRegisterSchema = z.object({
  narrative: z.string(),
  normative: z.string(),
  plain: z.string()
});

export const layerSchema = z.object({
  id: z.string(),
  name: z.string(),
  description: tripleRegisterSchema,
  risks: z.array(z.string()),
  artifacts: z.array(z.string()),
  standards: z.array(z.string()),
  personas: z.array(z.string()),
  aeip_hooks: z.array(z.string())
});

export const canonicalVersionSchema = z.object({
  label: z.string(),
  doi: z.string(),
  sha512: z.string(),
  integrity_notice: z.string(),
  last_reviewed: z.string()
});

export const layerPayloadSchema = z.object({
  _meta: z.record(z.string()),
  canonical_version: canonicalVersionSchema,
  layers: z.array(layerSchema)
});

export const artifactSchema = z.object({
  id: z.string(),
  type: z.string(),
  layer: z.string(),
  description: z.string(),
  schema_path: z.string(),
  canonical: z.boolean()
});

export const artifactPayloadSchema = z.object({
  _meta: z.record(z.string()),
  artifacts: z.array(artifactSchema)
});

export const personaSchema = z.object({
  id: z.string(),
  name: z.string(),
  mandate: z.string(),
  layer_bindings: z.array(z.string()),
  register: tripleRegisterSchema
});

export const personaPayloadSchema = z.object({
  _meta: z.record(z.string()),
  personas: z.array(personaSchema)
});

export const updatePlanSchema = z.object({
  version: z.string(),
  theme: z.string(),
  type: z.enum(["structural", "custodial", "interpretive"]),
  date: z.string(),
  summary: z.string(),
  related_layers: z.array(z.string()),
  aeip_reference: z.string()
});

export const updatePlanPayloadSchema = z.object({
  _meta: z.record(z.string()),
  plans: z.array(updatePlanSchema)
});

export const glossaryTermSchema = z.object({
  term: z.string(),
  definition: z.string(),
  source: z.string()
});

export const glossaryPayloadSchema = z.object({
  _meta: z.record(z.string()),
  terms: z.array(glossaryTermSchema)
});

export const aeipPrivacySchema = z.object({
  scope: z.string(),
  consent: z.string()
});

export const aeipReceiptSchema = z.object({
  "@context": z.union([z.string(), z.array(z.union([z.string(), z.record(z.unknown())]))]),
  id: z.string(),
  type: z.array(z.string()),
  issuanceDate: z.string(),
  layer: z.string(),
  hook: z.string(),
  intent: z.string(),
  justification: z.string(),
  countersignature: z.object({
    persona: z.string(),
    mandate: z.string(),
    timestamp: z.string()
  }),
  privacy: aeipPrivacySchema,
  integrity: z.object({
    hashAlgorithm: z.string(),
    hashValue: z.string(),
    ledgerReference: z.string()
  }),
  attachments: z.array(
    z.object({
      type: z.string(),
      summary: z.string()
    })
  )
});

export type TripleRegister = z.infer<typeof tripleRegisterSchema>;
export type Layer = z.infer<typeof layerSchema>;
export type CanonicalVersion = z.infer<typeof canonicalVersionSchema>;
export type LayerPayload = z.infer<typeof layerPayloadSchema>;
export type Artifact = z.infer<typeof artifactSchema>;
export type ArtifactPayload = z.infer<typeof artifactPayloadSchema>;
export type Persona = z.infer<typeof personaSchema>;
export type PersonaPayload = z.infer<typeof personaPayloadSchema>;
export type UpdatePlan = z.infer<typeof updatePlanSchema>;
export type UpdatePlanPayload = z.infer<typeof updatePlanPayloadSchema>;
export type GlossaryTerm = z.infer<typeof glossaryTermSchema>;
export type GlossaryPayload = z.infer<typeof glossaryPayloadSchema>;
export type AEIPReceipt = z.infer<typeof aeipReceiptSchema>;
export type TripleRegisterKey = keyof TripleRegister;

export type RegisterToggleOption = {
  key: TripleRegisterKey;
  label: string;
  ariaLabel: string;
};

export const REGISTER_OPTIONS: RegisterToggleOption[] = [
  { key: "narrative", label: "Narrative", ariaLabel: "Narrative register" },
  { key: "normative", label: "Normative", ariaLabel: "Normative register" },
  { key: "plain", label: "Plain", ariaLabel: "Plain-language register" }
];

export const parseDataOrThrow = <T>(schema: z.ZodType<T>, data: unknown, label: string): T => {
  const result = schema.safeParse(data);
  if (!result.success) {
    throw new Error(`${label} failed validation: ${result.error.message}`);
  }
  return result.data;
};
