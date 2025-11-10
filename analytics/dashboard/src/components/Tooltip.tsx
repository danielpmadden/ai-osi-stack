import { ReactNode } from 'react';

interface TooltipProps {
  label: string;
  children: ReactNode;
}

export default function Tooltip({ label, children }: TooltipProps) {
  return (
    <span className="gct-tooltip" aria-label={label} role="tooltip">
      {children}
    </span>
  );
}
