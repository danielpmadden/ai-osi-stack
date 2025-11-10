interface IntegrityBadgeProps {
  status: 'draft' | 'verified' | 'archived';
  updatedAt: string;
}

const STATUS_LABELS: Record<IntegrityBadgeProps['status'], string> = {
  draft: 'Draft',
  verified: 'Verified',
  archived: 'Archived'
};

export default function IntegrityBadge({ status, updatedAt }: IntegrityBadgeProps) {
  return (
    <span className={`integrity-badge integrity-badge--${status}`} aria-live="polite">
      <strong>{STATUS_LABELS[status]}</strong>
      <span>Updated {new Date(updatedAt).toLocaleDateString()}</span>
    </span>
  );
}
