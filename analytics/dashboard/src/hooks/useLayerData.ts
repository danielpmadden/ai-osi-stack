import { useMemo } from 'react';
import layers from '../data/layers.json';
import artifacts from '../data/artifacts.json';

export interface Layer {
  id: string;
  title: string;
  description: string;
  registers: Record<string, string>;
  personas: string[];
  aeipHooks: string[];
  artifacts: string[];
  status: string;
}

export interface Artifact {
  id: string;
  name: string;
  summary: string;
  updatedAt: string;
}

export function useLayerData() {
  const layerList = useMemo(() => layers as Layer[], []);
  const artifactMap = useMemo(() => {
    return new Map((artifacts as Artifact[]).map((artifact) => [artifact.id, artifact]));
  }, []);

  return { layers: layerList, artifactMap };
}
