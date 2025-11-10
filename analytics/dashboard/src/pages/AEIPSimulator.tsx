import { useState } from 'react';
import AEIPReceiptCard from '../components/AEIPReceiptCard';
import Modal from '../components/Modal';
import Button from '../components/Button';
import { useAEIPData } from '../hooks/useAEIPData';

export default function AEIPSimulator() {
  const { receipts } = useAEIPData();
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const selectedReceipt = receipts.find((receipt) => receipt.id === selectedId);

  return (
    <div className="page" aria-labelledby="aeip-sim-heading">
      <h1 id="aeip-sim-heading">AEIP Handshake Simulation</h1>
      <div className="page__grid">
        {receipts.map((receipt) => (
          <button
            key={receipt.id}
            type="button"
            className="page__card-button"
            onClick={() => setSelectedId(receipt.id)}
            aria-haspopup="dialog"
          >
            <AEIPReceiptCard receipt={receipt} />
          </button>
        ))}
      </div>
      <Modal isOpen={Boolean(selectedReceipt)} title={selectedReceipt?.id ?? ''} onClose={() => setSelectedId(null)}>
        {selectedReceipt ? (
          <div className="aeip-modal">
            <p>{selectedReceipt.summary}</p>
            <dl>
              <dt>Layer</dt>
              <dd>{selectedReceipt.layerId}</dd>
              <dt>Counterpart</dt>
              <dd>{selectedReceipt.handshake.counterpart}</dd>
              <dt>Next action</dt>
              <dd>{selectedReceipt.handshake.nextAction}</dd>
            </dl>
            <Button type="button" onClick={() => setSelectedId(null)}>
              Close
            </Button>
          </div>
        ) : null}
      </Modal>
    </div>
  );
}
