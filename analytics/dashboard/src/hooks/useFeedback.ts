import { useEffect, useState } from 'react';
import { getFeedback } from '../data/feedback';
import type { FeedbackEntry } from '../data/feedback/schema';

export function useFeedback() {
  const [entries, setEntries] = useState<FeedbackEntry[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let mounted = true;
    getFeedback()
      .then((payload) => {
        if (mounted) {
          setEntries(payload);
        }
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

  return { entries, loading };
}
