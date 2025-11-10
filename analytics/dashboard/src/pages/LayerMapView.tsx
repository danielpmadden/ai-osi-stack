import LayerCard from '../components/LayerCard';
import { useLayerData } from '../hooks/useLayerData';

export default function LayerMapView() {
  const { layers, artifactMap } = useLayerData();
  return (
    <div className="page" aria-labelledby="layer-map-heading">
      <h1 id="layer-map-heading">Layer Map</h1>
      <div className="page__grid">
        {layers.map((layer) => (
          <LayerCard key={layer.id} layer={layer} artifact={artifactMap.get(layer.artifacts[0])} />
        ))}
      </div>
    </div>
  );
}
