import { createContext, useContext, useEffect, useMemo, useState, ReactNode } from 'react';
import { getAEIPReceipts } from '../data/aeip';
import type { AEIPReceipt } from '../data/aeip/schema';

interface AEIPContextValue {
  receipts: AEIPReceipt[];
  loading: boolean;
  refresh: () => Promise<void>;
}

const AEIPContext = createContext<AEIPContextValue | undefined>(undefined);

export function AEIPProvider({ children }: { children: ReactNode }) {
  const [receipts, setReceipts] = useState<AEIPReceipt[]>([]);
  const [loading, setLoading] = useState(true);

  const load = async () => {
    setLoading(true);
    try {
      const data = await getAEIPReceipts();
      setReceipts(data);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    void load();
  }, []);

  const value = useMemo(
    () => ({
      receipts,
      loading,
      refresh: async () => load()
    }),
    [receipts, loading]
  );

  return <AEIPContext.Provider value={value}>{children}</AEIPContext.Provider>;
}

export function useAEIPContext() {
  const context = useContext(AEIPContext);
  if (!context) {
    throw new Error('useAEIPContext must be used within AEIPProvider');
  }
  return context;
}
