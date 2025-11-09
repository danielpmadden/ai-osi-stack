// SPDX-License-Identifier: Apache-2.0

import React from "react";
import type { CanonicalVersion } from "../utils/types";

export type IntegrityBadgeProps = {
  canonical: CanonicalVersion;
};

export const IntegrityBadge: React.FC<IntegrityBadgeProps> = ({ canonical }) => {
  return (
    <section
      className="inline-flex flex-wrap items-center gap-3 rounded-full border border-emerald-400/60 bg-emerald-500/10 px-4 py-2 text-xs text-emerald-100"
      aria-label="Integrity badge"
    >
      <span className="inline-flex h-2 w-2 rounded-full bg-emerald-400" aria-hidden />
      <span className="font-semibold">{canonical.label}</span>
      <span className="text-emerald-200">DOI {canonical.doi}</span>
      <span className="text-[11px] text-emerald-200">Checksum guidance: {canonical.checksum_guidance}</span>
      <span className="text-emerald-200">Last reviewed {canonical.last_reviewed}</span>
      <span className="text-[11px] text-emerald-200">Notice: {canonical.integrity_notice}</span>
      <span className="text-[11px] text-emerald-200">// TODO: embed ledger verification</span>
    </section>
  );
};

export default IntegrityBadge;
