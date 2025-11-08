import React, { useCallback, useMemo, useState } from "react";
import type { Layer, TripleRegisterKey } from "@/utils/types";
import { REGISTER_OPTIONS } from "@/utils/types";
import {
  getRegisterAriaAttributes,
  getRegisterPanelAttributes,
  buildCeFRPlaceholder,
  translationFidelityPlaceholder
} from "@/utils/accessibility";
import { getLayerHooks, formatAeipHookLabel } from "@/utils/aeipUtils";

export type LayerCardProps = {
  layer: Layer;
};

export const LayerCard: React.FC<LayerCardProps> = ({ layer }) => {
  const [registerKey, setRegisterKey] = useState<TripleRegisterKey>("plain");
  const hooks = getLayerHooks(layer);

  const handleSelect = useCallback((key: TripleRegisterKey) => {
    setRegisterKey(key);
  }, []);

  const handleKeyDown = useCallback(
    (event: React.KeyboardEvent<HTMLButtonElement>, index: number) => {
      if (event.key === "ArrowRight" || event.key === "ArrowLeft") {
        event.preventDefault();
        const delta = event.key === "ArrowRight" ? 1 : -1;
        const nextIndex = (index + delta + REGISTER_OPTIONS.length) % REGISTER_OPTIONS.length;
        const nextKey = REGISTER_OPTIONS[nextIndex].key;
        setRegisterKey(nextKey);
        const nextButton = document.getElementById(`register-tab-${nextKey}`);
        nextButton?.focus();
      }
    },
    []
  );

  const personasLabel = useMemo(() => layer.personas.join(", "), [layer.personas]);

  return (
    <article
      className="rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow-sm shadow-slate-900"
      aria-labelledby={`layer-${layer.id}`}
    >
      <header className="flex flex-wrap items-baseline justify-between gap-3">
        <div>
          <h3 id={`layer-${layer.id}`} className="text-lg font-semibold text-slate-100">
            {layer.id} · {layer.name}
          </h3>
          <p className="text-xs text-slate-400" aria-live="polite">
            {buildCeFRPlaceholder(layer.id)}
          </p>
        </div>
        <div className="flex flex-wrap gap-2 text-xs" aria-label={`Linked personas ${personasLabel}`}>
          {layer.personas.map((persona) => (
            <span
              key={persona}
              className="inline-flex items-center rounded-full border border-slate-700 bg-slate-900/70 px-3 py-1 text-slate-300"
            >
              {persona}
            </span>
          ))}
        </div>
      </header>

      <div className="mt-4" role="tablist" aria-label="Layer interpretation register">
        <div className="flex flex-wrap items-center gap-2">
          {REGISTER_OPTIONS.map((option, index) => (
            <button
              aria-label={option.ariaLabel}
              key={option.key}
              type="button"
              onClick={() => handleSelect(option.key)}
              onKeyDown={(event) => handleKeyDown(event, index)}
              className={`rounded-full border px-3 py-1 text-xs transition focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-900 ${
                registerKey === option.key
                  ? "border-emerald-400/80 bg-emerald-500/20 text-emerald-200"
                  : "border-slate-700 text-slate-300 hover:border-slate-500"
              }`}
              {...getRegisterAriaAttributes(option.key, registerKey)}
            >
              <span className="sr-only">Select </span>
              {option.label}
            </button>
          ))}
        </div>
        {REGISTER_OPTIONS.map((option) => (
          <section
            key={option.key}
            className="mt-3 rounded-lg border border-slate-800 bg-slate-950/40 p-4 text-sm text-slate-200"
            {...getRegisterPanelAttributes(option.key, registerKey)}
          >
            {layer.description[option.key]}
          </section>
        ))}
      </div>

      <div className="mt-5 grid gap-4 lg:grid-cols-4" aria-label="Layer governance facets">
        <Facet heading="Risks">
          <List items={layer.risks} empty="No documented risks" />
        </Facet>
        <Facet heading="Safeguards & Standards">
          <List items={layer.standards} empty="Standards pending" />
          <p className="mt-2 text-[11px] text-slate-500">{translationFidelityPlaceholder(layer.id)}</p>
        </Facet>
        <Facet heading="Canonical Artifacts">
          <List items={layer.artifacts} empty="Artifacts forthcoming" />
        </Facet>
        <Facet heading="AEIP Hooks">
          <ul className="space-y-1 text-xs text-slate-200">
            {hooks.map((hook) => (
              <li key={hook}>
                <span className="font-medium text-emerald-200">{formatAeipHookLabel(hook)}</span>
                <span className="ml-2 text-slate-400">({hook})</span>
              </li>
            ))}
            {hooks.length === 0 ? <li className="text-slate-400">Hook mapping pending</li> : null}
          </ul>
        </Facet>
      </div>
    </article>
  );
};

const Facet: React.FC<{ heading: string; children: React.ReactNode }> = ({ heading, children }) => (
  <section className="rounded-lg border border-slate-800 bg-slate-950/50 p-4" aria-label={heading}>
    <h4 className="text-xs font-semibold uppercase tracking-wide text-slate-400">{heading}</h4>
    <div className="mt-2 space-y-2">{children}</div>
  </section>
);

const List: React.FC<{ items: string[]; empty: string }> = ({ items, empty }) => (
  <ul className="space-y-1 text-xs text-slate-200">
    {items.length > 0 ? items.map((item) => <li key={item}>{item}</li>) : <li className="text-slate-400">{empty}</li>}
  </ul>
);

export default LayerCard;
