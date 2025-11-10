import { z } from 'zod';

export const aeipReceiptSchema = z.object({
  id: z.string(),
  layerId: z.string(),
  issuedAt: z.string(),
  status: z.enum(['pending', 'complete', 'error']),
  summary: z.string(),
  handshake: z.object({
    counterpart: z.string(),
    nextAction: z.string()
  })
});

export const aeipReceiptListSchema = z.array(aeipReceiptSchema);

export type AEIPReceipt = z.infer<typeof aeipReceiptSchema>;
