// SPDX-License-Identifier: Apache-2.0

import React, { useEffect, useMemo, useState } from "react";
import type { GlossaryTerm } from "@/utils/types";
import { t } from "@/i18n";

export type GlossaryDrawerProps = {
  terms: GlossaryTerm[];
};

export const GlossaryDrawer: React.FC<GlossaryDrawerProps> = ({ terms }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [query, setQuery] = useState("");

  const filtered = useMemo(() => {
    const normalized = query.toLowerCase();
    return terms.filter((term) => term.term.toLowerCase().includes(normalized));
  }, [query, terms]);

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        setIsOpen(false);
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, []);

  return (
    <div className="fixed bottom-6 right-6 z-40">
      <button
        type="button"
        className="rounded-full border border-slate-700 bg-slate-900/90 px-4 py-2 text-sm text-slate-100 shadow-lg shadow-slate-950 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400"
        onClick={() => setIsOpen((prev) => !prev)}
        aria-expanded={isOpen}
        aria-controls="glossary-drawer"
      >
        {isOpen ? t("navigation.closeGlossary") : t("navigation.openGlossary")}
      </button>
      <aside
        id="glossary-drawer"
        className={`mt-3 w-80 max-w-[90vw] rounded-2xl border border-slate-800 bg-slate-900/95 p-4 text-slate-100 shadow-xl shadow-slate-950 transition ${
          isOpen ? "opacity-100" : "pointer-events-none opacity-0"
        }`}
        aria-hidden={!isOpen}
        role="complementary"
      >
        <header className="flex items-center justify-between gap-2">
          <h2 className="text-sm font-semibold">{t("content.glossaryTitle")}</h2>
          <button
            type="button"
            className="rounded-full border border-slate-700 px-2 py-1 text-xs text-slate-300 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400"
            onClick={() => setIsOpen(false)}
            aria-label={t("navigation.closeGlossary")}
          >
            Close
          </button>
        </header>
        <label className="mt-3 block text-xs text-slate-300" htmlFor="glossary-search">
          {t("content.glossarySearch")}
        </label>
        <input
          id="glossary-search"
          type="search"
          className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm text-slate-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400"
          placeholder={t("content.glossaryPlaceholder")}
          value={query}
          onChange={(event) => setQuery(event.target.value)}
        />
        <ul className="mt-3 max-h-60 overflow-y-auto space-y-3" role="list">
          {filtered.map((term) => (
            <li key={term.term} className="rounded-lg border border-slate-800 bg-slate-950/70 p-3" tabIndex={0}>
              <p className="text-sm font-semibold" title={term.definition}>
                {term.term}
              </p>
              <p className="mt-1 text-xs text-slate-300">{term.definition}</p>
              <p className="mt-1 text-[11px] text-slate-500">Source: {term.source}</p>
            </li>
          ))}
          {filtered.length === 0 ? (
            <li className="text-xs text-slate-400">{t("content.glossaryEmpty", { query })}</li>
          ) : null}
        </ul>
        <p className="mt-3 text-[11px] text-slate-500">// TODO: integrate hover tooltips across dashboard via glossary API</p>
      </aside>
    </div>
  );
};

export default GlossaryDrawer;
