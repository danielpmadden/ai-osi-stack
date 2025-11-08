import { Layer } from "../App";
import LayerCard from "./LayerCard";

type LayerCardGridProps = {
  layers: Layer[];
  onSelect: (layerId: number) => void;
};

const LayerCardGrid = ({ layers, onSelect }: LayerCardGridProps) => {
  return (
    <section id="layers" className="layer-grid">
      {layers.map((layer) => (
        <LayerCard key={layer.id} layer={layer} onSelect={onSelect} />
      ))}
    </section>
  );
};

export default LayerCardGrid;
