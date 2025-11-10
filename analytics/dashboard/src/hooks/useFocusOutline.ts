import { useEffect } from 'react';

export function useFocusOutline() {
  useEffect(() => {
    const handler = () => {
      document.body.classList.add('using-keyboard');
      window.removeEventListener('keydown', handler);
    };

    window.addEventListener('keydown', handler);

    return () => {
      window.removeEventListener('keydown', handler);
    };
  }, []);
}
