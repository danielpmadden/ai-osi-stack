import { z } from 'zod';

export const ledgerEntrySchema = z.object({
  id: z.string(),
  title: z.string(),
  status: z.enum(['draft', 'verified', 'archived']),
  updatedAt: z.string()
});

export const ledgerEntryListSchema = z.array(ledgerEntrySchema);

export type LedgerEntry = z.infer<typeof ledgerEntrySchema>;
