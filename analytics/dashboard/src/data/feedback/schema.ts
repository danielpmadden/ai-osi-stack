import { z } from 'zod';

export const feedbackEntrySchema = z.object({
  id: z.string(),
  source: z.string(),
  submittedAt: z.string(),
  message: z.string()
});

export const feedbackEntryListSchema = z.array(feedbackEntrySchema);

export type FeedbackEntry = z.infer<typeof feedbackEntrySchema>;
