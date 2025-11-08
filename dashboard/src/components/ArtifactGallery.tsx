import React, { useMemo } from "react";
import type { Artifact, Layer } from "@/utils/types";
import { t } from "@/i18n";

export type ArtifactGalleryProps = {
  artifacts: Artifact[];
  layers: Layer[];
};

export const ArtifactGallery: React.FC<ArtifactGalleryProps> = ({ artifacts, layers }) => {
  const layerLookup = useMemo(
    () =>
      layers.reduce<Record<string, Layer>>((acc, layer) => {
        acc[layer.id] = layer;
        return acc;
      }, {}),
    [layers]
  );

  const grouped = useMemo(
    () =>
      artifacts.reduce<Record<string, Artifact[]>>((acc, artifact) => {
        if (!acc[artifact.layer]) {
          acc[artifact.layer] = [];
        }
        acc[artifact.layer].push(artifact);
        return acc;
      }, {}),
    [artifacts]
  );

  return (
    <section aria-label={t("content.artifactGallery")} className="space-y-4">
      {Object.entries(grouped).map(([layerId, items]) => {
        const layer = layerLookup[layerId];
        return (
          <div key={layerId} className="rounded-xl border border-slate-800 bg-slate-900/70 p-4">
            <header className="flex items-center justify-between gap-2">
              <h3 className="text-sm font-semibold text-slate-100">
                {layer ? `${layer.id} · ${layer.name}` : layerId}
              </h3>
              <span className="text-xs text-slate-400" aria-live="polite">
                {items.length} artifact{items.length === 1 ? "" : "s"}
              </span>
            </header>
            <ul className="mt-3 grid gap-3 md:grid-cols-2 xl:grid-cols-3" role="list">
              {items.map((artifact) => (
                <li
                  key={artifact.id}
                  className="rounded-lg border border-slate-800 bg-slate-950/40 p-4"
                  aria-label={`${artifact.type} artifact`}
                >
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <p className="text-sm font-medium text-slate-100">{artifact.type}</p>
                      <p className="text-xs text-slate-400">{artifact.description}</p>
                    </div>
                    {artifact.canonical ? (
                      <span className="inline-flex items-center rounded-full border border-emerald-400/60 bg-emerald-500/10 px-2 py-1 text-[11px] text-emerald-200">
                        Canonical
                      </span>
                    ) : null}
                  </div>
                  <p className="mt-3 text-[11px] text-slate-500">
                    Schema: <span className="font-mono text-slate-300">{artifact.schema_path}</span>
                  </p>
                  <p className="mt-1 text-[11px] text-slate-500">// TODO: attach AEIP provenance modal trigger</p>
                </li>
              ))}
            </ul>
          </div>
        );
      })}
    </section>
  );
};

export default ArtifactGallery;
