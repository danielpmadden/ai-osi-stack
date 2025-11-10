import { useState } from 'react';
import type { Layer, Artifact } from '../hooks/useLayerData';
import Button from './Button';
import Panel from './Panel';

interface LayerCardProps {
  layer: Layer;
  artifact?: Artifact;
}

const registerKeys: Array<keyof Layer['registers']> = ['civic', 'operational', 'strategic'];

export default function LayerCard({ layer, artifact }: LayerCardProps) {
  const [activeRegister, setActiveRegister] = useState<keyof Layer['registers']>('civic');

  return (
    <Panel className="layer-card" aria-live="polite">
      <header className="layer-card__header">
        <h3>{layer.title}</h3>
        <span className={`layer-card__status layer-card__status--${layer.status}`}>{layer.status}</span>
      </header>
      <p className="layer-card__description">{layer.description}</p>
      <div className="layer-card__registers" role="tablist" aria-label={`Narrative registers for ${layer.title}`}>
        {registerKeys.map((key) => (
          <Button
            key={key}
            role="tab"
            aria-selected={activeRegister === key}
            className={activeRegister === key ? 'layer-card__tab layer-card__tab--active' : 'layer-card__tab'}
            onClick={() => setActiveRegister(key)}
          >
            {key}
          </Button>
        ))}
      </div>
      <div role="tabpanel" className="layer-card__panel">
        <p>{layer.registers[activeRegister]}</p>
      </div>
      <footer className="layer-card__footer">
        <div>
          <strong>Personas:</strong> {layer.personas.join(', ')}
        </div>
        <div>
          <strong>AEIP Hooks:</strong> {layer.aeipHooks.join(', ')}
        </div>
        {artifact && (
          <div>
            <strong>Artifact:</strong> {artifact.name} (updated {artifact.updatedAt})
          </div>
        )}
      </footer>
    </Panel>
  );
}
