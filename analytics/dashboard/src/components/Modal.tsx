import { ReactNode, useEffect } from 'react';

interface ModalProps {
  isOpen: boolean;
  title: string;
  onClose: () => void;
  children: ReactNode;
}

export default function Modal({ isOpen, title, onClose, children }: ModalProps) {
  useEffect(() => {
    if (!isOpen) return;
    const handler = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        onClose();
      }
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, [isOpen, onClose]);

  if (!isOpen) {
    return null;
  }

  return (
    <div className="gct-modal" role="dialog" aria-modal="true" aria-label={title}>
      <div className="gct-modal__content">
        <header className="gct-modal__header">
          <h2>{title}</h2>
          <button type="button" className="gct-modal__close" onClick={onClose} aria-label="Close">
            ×
          </button>
        </header>
        <div className="gct-modal__body">{children}</div>
      </div>
    </div>
  );
}
