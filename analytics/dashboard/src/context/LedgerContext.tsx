import { createContext, useContext, useEffect, useMemo, useState, ReactNode } from 'react';
import { getLedgerEntries } from '../data/ledger';
import type { LedgerEntry } from '../data/ledger/schema';

interface LedgerContextValue {
  entries: LedgerEntry[];
  loading: boolean;
  refresh: () => Promise<void>;
}

const LedgerContext = createContext<LedgerContextValue | undefined>(undefined);

export function LedgerProvider({ children }: { children: ReactNode }) {
  const [entries, setEntries] = useState<LedgerEntry[]>([]);
  const [loading, setLoading] = useState(true);

  const load = async () => {
    setLoading(true);
    try {
      const data = await getLedgerEntries();
      setEntries(data);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    void load();
  }, []);

  const value = useMemo(
    () => ({
      entries,
      loading,
      refresh: async () => load()
    }),
    [entries, loading]
  );

  return <LedgerContext.Provider value={value}>{children}</LedgerContext.Provider>;
}

export function useLedgerContext() {
  const context = useContext(LedgerContext);
  if (!context) {
    throw new Error('useLedgerContext must be used within LedgerProvider');
  }
  return context;
}
