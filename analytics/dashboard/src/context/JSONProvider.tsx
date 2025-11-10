import { createContext, useContext, useEffect, useMemo, useState, ReactNode } from 'react';
import { fetchJSON } from '../utils/fetcher';

interface CanonicalDocs {
  layers: Record<string, string>;
  statuses: Record<string, string>;
}

const DEFAULT_DOCS: CanonicalDocs = {
  layers: {
    'layer-1': 'Civic Signals',
    'layer-8': 'Policy & Federation'
  },
  statuses: {
    stable: 'Stable',
    watch: 'Watch',
    'at-risk': 'At Risk'
  }
};

interface JSONContextValue {
  docs: CanonicalDocs;
  loading: boolean;
}

const JSONContext = createContext<JSONContextValue | undefined>(undefined);

export function JSONProvider({ children }: { children: ReactNode }) {
  const [docs, setDocs] = useState<CanonicalDocs>(DEFAULT_DOCS);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let mounted = true;
    fetchJSON<CanonicalDocs>('/docs/AI_OSI_Stack/00_Project_Definition.json')
      .then((payload) => {
        if (mounted) {
          setDocs({ ...DEFAULT_DOCS, ...payload });
        }
      })
      .catch((error) => {
        console.warn('Using bundled project definition', error);
      })
      .finally(() => {
        if (mounted) {
          setLoading(false);
        }
      });
    return () => {
      mounted = false;
    };
  }, []);

  const value = useMemo(() => ({ docs, loading }), [docs, loading]);

  return <JSONContext.Provider value={value}>{children}</JSONContext.Provider>;
}

export function useJSONContext() {
  const context = useContext(JSONContext);
  if (!context) {
    throw new Error('useJSONContext must be used within JSONProvider');
  }
  return context;
}
