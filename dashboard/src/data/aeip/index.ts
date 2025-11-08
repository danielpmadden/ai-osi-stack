// SPDX-License-Identifier: Apache-2.0

import reasoningTrace from "./reasoning_trace.aeip.jsonld";
import civicCharter from "./civic_charter.aeip.jsonld";
import instructionTrace from "./instruction_trace.aeip.jsonld";
import governancePublication from "./governance_publication.aeip.jsonld";
import { aeipReceiptSchema, parseDataOrThrow, type AEIPReceipt } from "@/utils/types";

const receipts = [
  { data: reasoningTrace, label: "reasoning_trace.aeip.jsonld" },
  { data: civicCharter, label: "civic_charter.aeip.jsonld" },
  { data: instructionTrace, label: "instruction_trace.aeip.jsonld" },
  { data: governancePublication, label: "governance_publication.aeip.jsonld" }
] as const;

export const aeipReceipts: AEIPReceipt[] = receipts.map(({ data, label }) =>
  parseDataOrThrow(aeipReceiptSchema, data, label)
);
