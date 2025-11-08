import React from "react";
import type { UpdatePlan } from "@/utils/types";
import { t } from "@/i18n";

export type VersionTimelineProps = {
  plans: UpdatePlan[];
};

export const VersionTimeline: React.FC<VersionTimelineProps> = ({ plans }) => {
  const sorted = [...plans].sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime());

  const colorForType = (type: UpdatePlan["type"]) => {
    switch (type) {
      case "structural":
        return "bg-emerald-400";
      case "custodial":
        return "bg-sky-400";
      default:
        return "bg-fuchsia-400";
    }
  };

  return (
    <section aria-label={t("content.versionTimeline")} className="rounded-xl border border-slate-800 bg-slate-900/70 p-4">
      <header>
        <h2 className="text-sm font-semibold text-slate-100">{t("content.versionTimeline")}</h2>
        <p className="text-xs text-slate-400">Chronological map of structural, custodial, and interpretive updates.</p>
      </header>
      <ol className="mt-4 space-y-4" role="list">
        {sorted.map((plan) => (
          <li key={plan.version} className="flex items-start gap-3">
            <span aria-hidden className={`mt-1 inline-flex h-3 w-3 flex-none rounded-full ${colorForType(plan.type)}`} />
            <div>
              <p className="text-sm font-semibold text-slate-100">
                {plan.version} · {plan.theme}
              </p>
              <p className="text-xs text-slate-400">{new Date(plan.date).toUTCString()}</p>
              <p className="mt-1 text-xs text-slate-300">{plan.summary}</p>
              <p className="mt-1 text-[11px] text-slate-500">
                Layers: {plan.related_layers.join(", ")} · AEIP Hook: {plan.aeip_reference}
              </p>
            </div>
          </li>
        ))}
      </ol>
      <p className="mt-4 text-[11px] text-slate-500">// TODO: connect to temporal integrity ledger for playback</p>
    </section>
  );
};

export default VersionTimeline;
