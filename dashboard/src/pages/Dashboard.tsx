import React from "react";
import layersData from "@/data/layers.json";
import artifactsData from "@/data/artifacts.json";
import personasData from "@/data/personas.json";
import updatePlansData from "@/data/update_plans.json";
import glossaryData from "@/data/glossary.json";
import { aeipReceipts } from "@/data/aeip";
import {
  layerPayloadSchema,
  artifactPayloadSchema,
  personaPayloadSchema,
  updatePlanPayloadSchema,
  glossaryPayloadSchema,
  parseDataOrThrow
} from "@/utils/types";
import { LayerCard } from "@/components/LayerCard";
import { ArtifactGallery } from "@/components/ArtifactGallery";
import { AEIPLogViewer } from "@/components/AEIPLogViewer";
import { VersionTimeline } from "@/components/VersionTimeline";
import { IntegrityBadge } from "@/components/IntegrityBadge";
import { GlossaryDrawer } from "@/components/GlossaryDrawer";
import { t } from "@/i18n";

const layerPayload = parseDataOrThrow(layerPayloadSchema, layersData, "layers.json");
const artifactPayload = parseDataOrThrow(artifactPayloadSchema, artifactsData, "artifacts.json");
const personaPayload = parseDataOrThrow(personaPayloadSchema, personasData, "personas.json");
const updatePlanPayload = parseDataOrThrow(updatePlanPayloadSchema, updatePlansData, "update_plans.json");
const glossaryPayload = parseDataOrThrow(glossaryPayloadSchema, glossaryData, "glossary.json");

export const Dashboard: React.FC = () => {
  const { canonical_version, layers } = layerPayload;
  const { artifacts } = artifactPayload;
  const { plans } = updatePlanPayload;

  return (
    <div className="flex min-h-screen bg-slate-950 text-slate-100" aria-label={t("layout.shellLabel")}> 
      <aside className="w-72 border-r border-slate-900 bg-slate-950/80 backdrop-blur-sm" aria-label={t("navigation.layers")}>
        <div className="px-6 py-6">
          <h1 className="text-xl font-semibold tracking-tight">{t("layout.title")}</h1>
          <p className="mt-1 text-sm text-slate-400">{t("layout.subtitle")}</p>
        </div>
        <nav className="px-6" aria-label={t("navigation.primary")}>
          <ul className="space-y-2 text-sm" role="list">
            {layers.map((layer) => (
              <li key={layer.id}>
                <a
                  href={`#layer-${layer.id}`}
                  className="flex items-center justify-between rounded-lg px-3 py-2 text-slate-300 transition hover:bg-slate-900/70 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400"
                >
                  <span>{layer.id}</span>
                  <span className="text-xs text-slate-500">{layer.name}</span>
                </a>
              </li>
            ))}
          </ul>
        </nav>
        <div className="px-6 py-6 text-xs text-slate-400" aria-live="polite">
          {t("navigation.personaCount", { count: personaPayload.personas.length })}
        </div>
      </aside>

      <main id="main-content" className="flex flex-1 flex-col" tabIndex={-1}>
        <header className="flex flex-wrap items-center justify-between gap-4 border-b border-slate-900 bg-slate-950/80 px-8 py-4">
          <div>
            <h2 className="text-lg font-semibold text-slate-100">{t("content.snapshotHeading")}</h2>
            <p className="text-xs text-slate-400">{t("content.snapshotSubheading")}</p>
          </div>
          <IntegrityBadge canonical={canonical_version} />
        </header>

        <section className="flex-1 space-y-6 overflow-y-auto px-8 py-6" aria-label={t("content.mainSection")}> 
          {layers.map((layer) => (
            <LayerCard key={layer.id} layer={layer} />
          ))}

          <div className="grid gap-6 xl:grid-cols-2" aria-label={t("content.secondaryPanels")}>
            <ArtifactGallery artifacts={artifacts} layers={layers} />
            <AEIPLogViewer receipts={aeipReceipts} />
          </div>

          <VersionTimeline plans={plans} />
        </section>
      </main>

      <GlossaryDrawer terms={glossaryPayload.terms} />
    </div>
  );
};

export default Dashboard;
