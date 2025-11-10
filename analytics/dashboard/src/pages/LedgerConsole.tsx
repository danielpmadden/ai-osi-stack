import IntegrityBadge from '../components/IntegrityBadge';
import Panel from '../components/Panel';
import { useLedgerData } from '../hooks/useLedgerData';

export default function LedgerConsole() {
  const { entries, loading } = useLedgerData();
  return (
    <div className="page" aria-labelledby="ledger-heading">
      <h1 id="ledger-heading">Integrity Ledger</h1>
      {loading ? <p role="status">Loading ledger…</p> : null}
      <div className="page__grid">
        {entries.map((entry) => (
          <Panel key={entry.id}>
            <h2>{entry.title}</h2>
            <IntegrityBadge status={entry.status} updatedAt={entry.updatedAt} />
          </Panel>
        ))}
      </div>
    </div>
  );
}
