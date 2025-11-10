import { ledgerEntryListSchema, type LedgerEntry } from './schema';
import { fetchJSON } from '../../utils/fetcher';

const FALLBACK: LedgerEntry[] = [
  {
    id: 'ledger-001',
    title: 'Civic Signals Ledger Snapshot',
    status: 'verified',
    updatedAt: '2024-05-10'
  },
  {
    id: 'ledger-002',
    title: 'Policy Federation Commitment',
    status: 'draft',
    updatedAt: '2024-05-18'
  }
];

export async function getLedgerEntries(): Promise<LedgerEntry[]> {
  try {
    const remote = await fetchJSON<unknown>('/api/ledger/entries');
    return ledgerEntryListSchema.parse(remote);
  } catch (error) {
    console.warn('Using fallback ledger entries', error);
    return ledgerEntryListSchema.parse(FALLBACK);
  }
}
