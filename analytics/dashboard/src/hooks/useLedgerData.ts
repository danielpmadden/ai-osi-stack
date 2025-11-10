import { useLedgerContext } from '../context/LedgerContext';

export function useLedgerData() {
  return useLedgerContext();
}
