// SPDX-License-Identifier: Apache-2.0

import React from "react";

const About: React.FC = () => {
  return (
    <main className="mx-auto max-w-3xl px-6 py-10 text-slate-100">
      <h1 className="text-2xl font-semibold">About the AI OSI Stack Dashboard</h1>
      <p className="mt-4 text-sm text-slate-300">
        This dashboard scaffolds civic-governance observability across the AI OSI Stack’s nine layers and AEIP spine.
        It is seeded with canonical audit data and designed for future protocol integrations.
      </p>
      <ul className="mt-6 space-y-3 text-sm text-slate-300">
        <li>// TODO: add stewardship directory once persona API is live</li>
        <li>// TODO: expose AEIP replay simulator via protocol bindings</li>
        <li>// TODO: publish accessibility conformance reports per Update Plan 2 & 3</li>
      </ul>
    </main>
  );
};

export default About;
