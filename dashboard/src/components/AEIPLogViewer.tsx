// SPDX-License-Identifier: Apache-2.0

import React, { useMemo, useState } from "react";
import type { AEIPReceipt } from "@/utils/types";
import { usePrefersReducedMotion } from "@/utils/accessibility";
import { t } from "@/i18n";

export type AEIPLogViewerProps = {
  receipts: AEIPReceipt[];
};

const formatDate = (value: string) => new Date(value).toUTCString();

export const AEIPLogViewer: React.FC<AEIPLogViewerProps> = ({ receipts }) => {
  const [activeReceipt, setActiveReceipt] = useState<AEIPReceipt | null>(null);
  const [query, setQuery] = useState("");
  const prefersMotionReduced = usePrefersReducedMotion();

  const filteredReceipts = useMemo(() => {
    const normalized = query.trim().toLowerCase();
    if (!normalized) {
      return receipts;
    }
    return receipts.filter((receipt) => {
      return (
        receipt.hook.toLowerCase().includes(normalized) ||
        receipt.layer.toLowerCase().includes(normalized) ||
        receipt.intent.toLowerCase().includes(normalized)
      );
    });
  }, [receipts, query]);

  const transitionClass = prefersMotionReduced ? "" : "transition";

  return (
    <section aria-label={t("content.aeipLogTitle")} className="rounded-xl border border-slate-800 bg-slate-900/70 p-4">
      <header className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h2 className="text-sm font-semibold text-slate-100">{t("content.aeipLogTitle")}</h2>
          <p className="text-xs text-slate-400">// TODO: hydrate from AEIP spine API</p>
        </div>
        <label className="flex w-full items-center gap-2 sm:w-auto" htmlFor="aeip-search">
          <span className="sr-only">{t("content.aeipSearchPlaceholder")}</span>
          <input
            id="aeip-search"
            type="search"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder={t("content.aeipSearchPlaceholder")}
            className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm text-slate-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400"
          />
        </label>
      </header>
      <ul className="mt-3 divide-y divide-slate-800" role="list">
        {filteredReceipts.map((receipt) => (
          <li key={receipt.id} className="py-3">
            <button
              type="button"
              className={`flex w-full flex-col items-start gap-1 text-left focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-900 ${transitionClass}`}
              onClick={() => setActiveReceipt(receipt)}
              aria-haspopup="dialog"
              aria-controls="aeip-receipt-modal"
            >
              <span className="flex w-full items-center justify-between gap-2">
                <span className="text-sm font-medium text-slate-100">{receipt.hook}</span>
                <span className="inline-flex items-center rounded-full border border-slate-700 bg-slate-950 px-2 py-0.5 text-[10px] font-mono text-emerald-200">
                  {receipt.integrity.hashValue.slice(0, 12)}…
                </span>
              </span>
              <span className="text-xs text-slate-400">
                {receipt.layer} · {formatDate(receipt.issuanceDate)}
              </span>
              <span className="text-xs text-slate-300 line-clamp-2">{receipt.intent}</span>
            </button>
          </li>
        ))}
        {filteredReceipts.length === 0 ? (
          <li className="py-3 text-xs text-slate-400">No AEIP receipts match “{query}”.</li>
        ) : null}
      </ul>

      {activeReceipt ? (
        <div
          role="dialog"
          aria-modal="true"
          id="aeip-receipt-modal"
          className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/80 px-4"
        >
          <div className="w-full max-w-2xl rounded-xl border border-slate-800 bg-slate-900 p-6 shadow-lg shadow-slate-950">
            <header className="flex items-start justify-between gap-4">
              <div>
                <h3 className="text-base font-semibold text-slate-100">{activeReceipt.hook}</h3>
                <p className="text-xs text-slate-400">{activeReceipt.layer}</p>
              </div>
              <button
                type="button"
                className="rounded-full border border-slate-700 px-2 py-1 text-xs text-slate-300 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-900"
                onClick={() => setActiveReceipt(null)}
                aria-label={t("content.aeipModalClose")}
              >
                Close
              </button>
            </header>
            <dl className="mt-4 grid gap-3 text-sm text-slate-200 sm:grid-cols-2">
              <div>
                <dt className="text-xs uppercase tracking-wide text-slate-500">Issued</dt>
                <dd>{formatDate(activeReceipt.issuanceDate)}</dd>
              </div>
              <div>
                <dt className="text-xs uppercase tracking-wide text-slate-500">{t("content.aeipModalHash")}</dt>
                <dd className="font-mono text-xs text-emerald-200">{activeReceipt.integrity.hashValue}</dd>
              </div>
              <div>
                <dt className="text-xs uppercase tracking-wide text-slate-500">{t("content.aeipModalIntent")}</dt>
                <dd>{activeReceipt.intent}</dd>
              </div>
              <div>
                <dt className="text-xs uppercase tracking-wide text-slate-500">{t("content.aeipModalJustification")}</dt>
                <dd>{activeReceipt.justification}</dd>
              </div>
              <div>
                <dt className="text-xs uppercase tracking-wide text-slate-500">{t("content.aeipModalCountersignature")}</dt>
                <dd>
                  {activeReceipt.countersignature.persona} · {activeReceipt.countersignature.mandate}
                  <br />
                  <span className="text-xs text-slate-400">{formatDate(activeReceipt.countersignature.timestamp)}</span>
                </dd>
              </div>
              <div>
                <dt className="text-xs uppercase tracking-wide text-slate-500">{t("content.aeipModalPrivacy")}</dt>
                <dd>
                  <span className="font-medium text-emerald-200">{activeReceipt.privacy.scope}</span>
                  <br />
                  <span className="text-xs text-slate-400">{activeReceipt.privacy.consent}</span>
                </dd>
              </div>
              <div>
                <dt className="text-xs uppercase tracking-wide text-slate-500">{t("content.aeipModalLedger")}</dt>
                <dd className="font-mono text-xs text-slate-300">{activeReceipt.integrity.ledgerReference}</dd>
              </div>
              <div>
                <dt className="text-xs uppercase tracking-wide text-slate-500">{t("content.aeipModalAttachments")}</dt>
                <dd>
                  <ul className="space-y-1 text-xs">
                    {activeReceipt.attachments.map((attachment) => (
                      <li key={`${attachment.type}-${attachment.summary}`}>{attachment.type} · {attachment.summary}</li>
                    ))}
                  </ul>
                </dd>
              </div>
            </dl>
            <div className="mt-4">
              <h4 className="text-xs font-semibold uppercase tracking-wide text-slate-500">JSON-LD</h4>
              <pre className="mt-2 max-h-48 overflow-y-auto rounded-lg bg-slate-950/70 p-3 text-[11px] leading-relaxed text-slate-200">
                {JSON.stringify(activeReceipt, null, 2)}
              </pre>
            </div>
          </div>
        </div>
      ) : null}
    </section>
  );
};

export default AEIPLogViewer;
