import type { AEIPReceipt } from '../data/aeip/schema';
import Panel from './Panel';

interface Props {
  receipt: AEIPReceipt;
}

export default function AEIPReceiptCard({ receipt }: Props) {
  return (
    <Panel className={`aeip-receipt aeip-receipt--${receipt.status}`}>
      <header className="aeip-receipt__header">
        <h3>{receipt.id}</h3>
        <span>{new Date(receipt.issuedAt).toLocaleString()}</span>
      </header>
      <p>{receipt.summary}</p>
      <dl className="aeip-receipt__meta">
        <div>
          <dt>Layer</dt>
          <dd>{receipt.layerId}</dd>
        </div>
        <div>
          <dt>Counterpart</dt>
          <dd>{receipt.handshake.counterpart}</dd>
        </div>
        <div>
          <dt>Next action</dt>
          <dd>{receipt.handshake.nextAction}</dd>
        </div>
        <div>
          <dt>Status</dt>
          <dd>{receipt.status}</dd>
        </div>
      </dl>
    </Panel>
  );
}
