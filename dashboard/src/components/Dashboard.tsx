import React from "react";
import layerData from "../data/layers.json";

type Layer = {
  id: string;
  name: string;
  purpose: string;
  rationale?: string;
  risks: string[];
  governanceLevers: string[];
  evidenceArtifacts: string[];
  aeipHooks: string[];
  contextualTransparency: {
    public: boolean;
    notes: string;
  };
};

type CanonicalVersion = {
  label: string;
  hash: string;
  doi: string;
  timestamp: string;
};

type LayerPayload = {
  canonicalVersion: CanonicalVersion;
  layers: Layer[];
  artifactGallery: Array<{
    id: string;
    type: string;
    layer: string;
    hash: string;
    sourcePath: string;
  }>;
};

const payload = layerData as LayerPayload;

export const Dashboard: React.FC = () => {
  const { canonicalVersion, layers, artifactGallery } = payload;

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex">
      {/* Sidebar Navigation */}
      <aside className="w-72 border-r border-slate-800 bg-slate-900/60 backdrop-blur-sm">
        <div className="px-6 py-6">
          <h1 className="text-xl font-semibold tracking-tight">AI OSI Stack</h1>
          <p className="mt-1 text-sm text-slate-400">Governance Control Plane Mock</p>
        </div>
        <nav className="px-6 space-y-3 text-sm">
          <SectionLink label="Overview" />
          <SectionLink label="Governance Map" />
          <SectionLink label="Layers 0–8" active />
          <SectionLink label="AEIP Log Viewer" />
          <SectionLink label="Artifact Gallery" />
          <SectionLink label="Version Timeline" />
          <SectionLink label="Governance Artifacts" />
        </nav>
        <div className="px-6 pt-8 pb-6 text-xs text-slate-500">
          <p>Contextual Transparency Mode</p>
          <p className="mt-1 font-medium text-slate-300">Right-to-Opacity Enabled</p>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col">
        {/* Top Bar */}
        <header className="border-b border-slate-800 bg-slate-900/80 px-8 py-4 flex items-center justify-between">
          <div>
            <h2 className="text-lg font-medium">{canonicalVersion.label}</h2>
            <p className="text-xs text-slate-400">
              Hash {canonicalVersion.hash} • DOI {canonicalVersion.doi} • Timestamp {canonicalVersion.timestamp}
            </p>
          </div>
          <div className="flex items-center gap-3">
            <span className="inline-flex items-center gap-2 rounded-full border border-emerald-400/50 bg-emerald-500/10 px-3 py-1 text-xs text-emerald-300">
              <span className="h-2 w-2 rounded-full bg-emerald-400" aria-hidden />
              Integrity Badge
            </span>
            <button className="rounded-full border border-slate-700 px-3 py-1 text-xs text-slate-300" type="button">
              Toggle Transparency
            </button>
          </div>
        </header>

        {/* Layer Cards */}
        <section className="flex-1 overflow-y-auto px-8 py-6 space-y-6">
          {layers.map((layer) => (
            <article key={layer.id} className="rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow-sm shadow-slate-900">
              <header className="flex flex-wrap items-baseline justify-between gap-2">
                <h3 className="text-lg font-semibold">
                  {layer.id} · {layer.name}
                </h3>
                <p className="text-xs uppercase tracking-wide text-slate-500">
                  {layer.contextualTransparency.public ? "Public" : "Restricted"} • {layer.contextualTransparency.notes}
                </p>
              </header>
              {layer.rationale ? (
                <p className="mt-3 text-sm text-slate-300">{layer.rationale}</p>
              ) : null}
              <div className="mt-4 grid gap-4 md:grid-cols-4">
                <InfoBlock title="Purpose & Rationale">
                  <p className="text-sm text-slate-200">{layer.purpose}</p>
                  {layer.rationale && (
                    <p className="mt-2 text-xs text-slate-400">{layer.rationale}</p>
                  )}
                </InfoBlock>
                <InfoBlock title="Risks & Governance Levers">
                  <ListBlock title="Risks" items={layer.risks} />
                  <ListBlock title="Levers" items={layer.governanceLevers} />
                </InfoBlock>
                <InfoBlock title="Evidence Artifacts">
                  <ListBlock items={layer.evidenceArtifacts} emptyFallback="Pending evidence upload" />
                </InfoBlock>
                <InfoBlock title="AEIP Hooks">
                  <ListBlock items={layer.aeipHooks} emptyFallback="Awaiting AEIP integration" />
                  <p className="mt-2 text-[11px] text-slate-500">{/* Future AEIP/OpenAI integration anchor */}
                    Connect AEIP CLI stream here to hydrate handshake telemetry.
                  </p>
                </InfoBlock>
              </div>
            </article>
          ))}
        </section>

        {/* Artifact Gallery Preview */}
        <section className="border-t border-slate-800 bg-slate-900/70 px-8 py-4">
          <h4 className="text-sm font-semibold text-slate-200">Artifact Gallery Preview</h4>
          <div className="mt-3 flex flex-wrap gap-3">
            {artifactGallery.map((artifact) => (
              <span key={artifact.id} className="rounded-lg border border-slate-800 bg-slate-900/80 px-3 py-2 text-xs text-slate-300">
                {artifact.type} · {artifact.layer} · {artifact.hash}
              </span>
            ))}
          </div>
          <p className="mt-3 text-[11px] text-slate-500">Future OpenAI summarization endpoint can render conversational briefs for selected artifacts.</p>
        </section>
      </main>
    </div>
  );
};

const SectionLink: React.FC<{ label: string; active?: boolean }> = ({ label, active }) => (
  <button
    type="button"
    className={`flex w-full items-center justify-between rounded-lg px-3 py-2 transition hover:bg-slate-800/80 ${
      active ? "bg-slate-800 text-slate-50" : "text-slate-300"
    }`}
  >
    <span>{label}</span>
    {active ? <span className="h-2 w-2 rounded-full bg-emerald-400" /> : null}
  </button>
);

const InfoBlock: React.FC<{ title: string; children: React.ReactNode }> = ({ title, children }) => (
  <div className="rounded-lg border border-slate-800 bg-slate-950/40 p-4">
    <h5 className="text-xs font-semibold uppercase tracking-wide text-slate-400">{title}</h5>
    <div className="mt-2 space-y-2">{children}</div>
  </div>
);

const ListBlock: React.FC<{ title?: string; items: string[]; emptyFallback?: string }> = ({
  title,
  items,
  emptyFallback = "No entries",
}) => (
  <div>
    {title ? <p className="text-[11px] font-semibold uppercase tracking-wide text-slate-500">{title}</p> : null}
    <ul className="mt-1 space-y-1 text-xs text-slate-300">
      {items.length > 0 ? items.map((item) => <li key={item}>{item}</li>) : <li>{emptyFallback}</li>}
    </ul>
  </div>
);

export default Dashboard;
