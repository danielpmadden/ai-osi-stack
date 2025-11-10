import { feedbackEntryListSchema, type FeedbackEntry } from './schema';
import { fetchJSON } from '../../utils/fetcher';

const FALLBACK: FeedbackEntry[] = [
  {
    id: 'feedback-001',
    source: 'Layer 8 Civic Loop',
    submittedAt: '2024-05-18',
    message: 'Stakeholders request clearer handshake transparency.'
  }
];

export async function getFeedback(): Promise<FeedbackEntry[]> {
  try {
    const remote = await fetchJSON<unknown>('/api/feedback');
    return feedbackEntryListSchema.parse(remote);
  } catch (error) {
    console.warn('Using offline civic feedback', error);
    return feedbackEntryListSchema.parse(FALLBACK);
  }
}
