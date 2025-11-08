// SPDX-License-Identifier: Apache-2.0

// TODO: Replace static stubs with AEIP client once protocol bindings are available.

import type { Layer, UpdatePlan } from "./types";

export const getLayerHooks = (layer: Layer): string[] => {
  return layer.aeip_hooks;
};

export const formatAeipHookLabel = (hook: string): string => {
  return hook
    .replace(/([A-Z])/g, " $1")
    .trim()
    .replace(/^\w/, (char) => char.toUpperCase());
};

export const mapUpdatePlansByHook = (plans: UpdatePlan[]): Record<string, UpdatePlan[]> => {
  return plans.reduce<Record<string, UpdatePlan[]>>((acc, plan) => {
    const hook = plan.aeip_reference;
    if (!acc[hook]) {
      acc[hook] = [];
    }
    acc[hook].push(plan);
    return acc;
  }, {});
};
