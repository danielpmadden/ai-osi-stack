import { useMemo, useState } from "react";
import SidebarNav from "./components/SidebarNav";
import LayerCardGrid from "./components/LayerCardGrid";
import ArtifactPanel from "./components/ArtifactPanel";
import layersSource from "./data/layers.json";
import artifactsSource from "./data/sampleArtifacts.json";

export type LayerStatus = "verified" | "pending" | "unverified";

export interface Layer {
  id: number;
  name: string;
  purpose: string;
  status: LayerStatus;
}

export interface ArtifactDetails {
  aeip_version: string;
  schema: string;
  artifact_id: string;
  description: string;
  custodian: string;
  timestamp: string;
  verification: LayerStatus;
}

const App = () => {
  const [selectedLayerId, setSelectedLayerId] = useState<number | null>(null);
  const [statusOverrides, setStatusOverrides] = useState<Record<number, LayerStatus>>(() => {
    const entries = layersSource.map((layer) => [layer.id, layer.status as LayerStatus]);
    return Object.fromEntries(entries);
  });

  const layers = useMemo<Layer[]>(
    () =>
      layersSource.map((layer) => ({
        ...layer,
        status: statusOverrides[layer.id] ?? layer.status,
      })),
    [statusOverrides]
  );

  const selectedLayer = useMemo(
    () => layers.find((layer) => layer.id === selectedLayerId) ?? null,
    [layers, selectedLayerId]
  );

  const selectedArtifact = useMemo(() => {
    if (selectedLayerId === null) {
      return null;
    }
    const artifact = artifactsSource[String(selectedLayerId) as keyof typeof artifactsSource];
    return artifact ?? null;
  }, [selectedLayerId]);

  const handleCardSelect = (layerId: number) => {
    setSelectedLayerId(layerId);
  };

  const handleClosePanel = () => {
    setSelectedLayerId(null);
  };

  const handleReverify = (layerId: number) => {
    setStatusOverrides((prev) => {
      const current = prev[layerId] ?? "pending";
      const next: LayerStatus = current === "verified" ? "pending" : "verified";
      return { ...prev, [layerId]: next };
    });
  };

  return (
    <div className="demo-layout">
      <SidebarNav />
      <main className="demo-main">
        <header className="demo-header">
          <h1>AI Governance Compliance Portal (Demo)</h1>
          <p>A visualization of AI OSI Stack layers and verification states.</p>
        </header>
        <LayerCardGrid layers={layers} onSelect={handleCardSelect} />
      </main>
      <ArtifactPanel
        layer={selectedLayer}
        artifact={selectedArtifact}
        onClose={handleClosePanel}
        onReverify={handleReverify}
      />
    </div>
  );
};

export default App;
