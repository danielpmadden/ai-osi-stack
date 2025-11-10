import { aeipReceiptListSchema, type AEIPReceipt } from './schema';
import receipts from './receipts.sample.json';
import { fetchJSON } from '../../utils/fetcher';

const ENDPOINT = '/api/aeip/receipts';

export async function getAEIPReceipts(): Promise<AEIPReceipt[]> {
  try {
    const remote = await fetchJSON<unknown>(ENDPOINT);
    const parsed = aeipReceiptListSchema.parse(remote);
    return parsed;
  } catch (error) {
    console.warn('Falling back to local AEIP receipts', error);
    return aeipReceiptListSchema.parse(receipts);
  }
}
