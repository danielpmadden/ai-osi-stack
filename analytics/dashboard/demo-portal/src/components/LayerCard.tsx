import { Layer } from "../App";

type LayerCardProps = {
  layer: Layer;
  onSelect: (layerId: number) => void;
};

const statusLabel: Record<Layer["status"], string> = {
  verified: "Verified",
  pending: "Pending",
  unverified: "Unverified",
};

const LayerCard = ({ layer, onSelect }: LayerCardProps) => {
  return (
    <button
      type="button"
      className={`layer-card status-${layer.status}`}
      onClick={() => onSelect(layer.id)}
    >
      <div className="layer-card-header">
        <span className="layer-id">L{layer.id}</span>
        <span className={`status-badge status-${layer.status}`}>
          {statusLabel[layer.status]}
        </span>
      </div>
      <h2>{layer.name}</h2>
      <p>{layer.purpose}</p>
    </button>
  );
};

export default LayerCard;
