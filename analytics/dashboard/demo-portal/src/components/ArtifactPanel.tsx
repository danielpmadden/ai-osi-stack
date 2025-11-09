import { ArtifactDetails, Layer } from "../App";

type ArtifactPanelProps = {
  layer: Layer | null;
  artifact: ArtifactDetails | null;
  onClose: () => void;
  onReverify: (layerId: number) => void;
};

const ArtifactPanel = ({ layer, artifact, onClose, onReverify }: ArtifactPanelProps) => {
  if (!layer) {
    return null;
  }

  const statusClass = `status-badge status-${layer.status}`;
  const artifactJson = artifact ? JSON.stringify(artifact, null, 2) : null;

  return (
    <div className="artifact-panel-overlay" role="dialog" aria-modal="true">
      <div className="artifact-panel">
        <div className="artifact-panel-header">
          <div>
            <h3>{layer.name}</h3>
            <p>AEIP Artefact Record</p>
          </div>
          <button type="button" className="close-button" onClick={onClose} aria-label="Close">
            ×
          </button>
        </div>
        <div className="artifact-panel-status">
          <span className={statusClass}>
            {layer.status === "verified"
              ? "Evidence Verified ✅"
              : layer.status === "pending"
              ? "Pending Verification ⚠️"
              : "Evidence Unverified ⛔"}
          </span>
          <button type="button" className="reverify-button" onClick={() => onReverify(layer.id)}>
            Re-Verify
          </button>
        </div>
        {artifactJson ? (
          <pre className="artifact-json">{artifactJson}</pre>
        ) : (
          <div className="artifact-placeholder">
            <p>No AEIP artefact has been uploaded for this layer.</p>
          </div>
        )}
        <a className="schema-link" href="#schema" target="_blank" rel="noreferrer">
          View AEIP Schema
        </a>
      </div>
    </div>
  );
};

export default ArtifactPanel;
