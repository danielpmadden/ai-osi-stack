import LayerCard from '../components/LayerCard';
import AEIPReceiptCard from '../components/AEIPReceiptCard';
import IntegrityBadge from '../components/IntegrityBadge';
import Panel from '../components/Panel';
import Button from '../components/Button';
import { useLayerData } from '../hooks/useLayerData';
import { useAEIPData } from '../hooks/useAEIPData';
import { useLedgerData } from '../hooks/useLedgerData';
import { useJSONContext } from '../context/JSONProvider';

export default function Dashboard() {
  const { layers, artifactMap } = useLayerData();
  const { receipts, loading: aeipLoading, refresh } = useAEIPData();
  const { entries } = useLedgerData();
  const { docs } = useJSONContext();

  return (
    <div className="dashboard" aria-labelledby="dashboard-heading">
      <h1 id="dashboard-heading">Governance Snapshot</h1>
      <section aria-label="Layer map" className="dashboard__layers">
        {layers.map((layer) => (
          <LayerCard key={layer.id} layer={layer} artifact={artifactMap.get(layer.artifacts[0])} />
        ))}
      </section>
      <section className="dashboard__aeip" aria-label="AEIP receipts">
        <header className="dashboard__section-header">
          <h2>AEIP Receipts</h2>
          <Button type="button" onClick={() => refresh()} disabled={aeipLoading}>
            {aeipLoading ? 'Refreshing…' : 'Refresh'}
          </Button>
        </header>
        <div className="dashboard__aeip-grid">
          {receipts.map((receipt) => (
            <AEIPReceiptCard key={receipt.id} receipt={receipt} />
          ))}
        </div>
      </section>
      <section className="dashboard__ledger" aria-label="Integrity ledger">
        <header className="dashboard__section-header">
          <h2>Integrity Ledger</h2>
        </header>
        <div className="dashboard__ledger-grid">
          {entries.map((entry) => (
            <Panel key={entry.id} className="dashboard__ledger-card">
              <h3>{entry.title}</h3>
              <IntegrityBadge status={entry.status} updatedAt={entry.updatedAt} />
            </Panel>
          ))}
        </div>
      </section>
      <section className="dashboard__docs" aria-label="Canonical labels">
        <h2>Canonical Labels</h2>
        <ul>
          {Object.entries(docs.layers).map(([id, label]) => (
            <li key={id}>
              <strong>{id}:</strong> {label}
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
