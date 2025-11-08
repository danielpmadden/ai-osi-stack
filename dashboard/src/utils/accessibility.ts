// SPDX-License-Identifier: Apache-2.0

// TODO: Integrate automated WCAG validation and T-SIR translation fidelity checks.

import { useEffect, useState } from "react";
import type { TripleRegisterKey } from "./types";

export const prefersReducedMotion = (): boolean => {
  if (typeof window === "undefined" || !window.matchMedia) {
    return false;
  }
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
};

export const usePrefersReducedMotion = (): boolean => {
  const [reducedMotion, setReducedMotion] = useState(prefersReducedMotion());

  useEffect(() => {
    if (typeof window === "undefined" || !window.matchMedia) {
      return;
    }

    const mediaQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
    const handler = (event: MediaQueryListEvent) => setReducedMotion(event.matches);
    mediaQuery.addEventListener("change", handler);
    return () => mediaQuery.removeEventListener("change", handler);
  }, []);

  return reducedMotion;
};

export const useFocusOutline = (): void => {
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Tab") {
        document.body.dataset.focusOutline = "visible";
      }
    };

    const handleMouseDown = () => {
      delete document.body.dataset.focusOutline;
    };

    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("mousedown", handleMouseDown);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("mousedown", handleMouseDown);
    };
  }, []);
};

export const SkipLink: React.FC<{ href: string }> = ({ href }) => (
  <a className="skip-link" href={href}>
    Skip to content
  </a>
);

export const getRegisterAriaAttributes = (
  optionKey: TripleRegisterKey,
  activeKey: TripleRegisterKey
) => {
  return {
    role: "tab",
    id: `register-tab-${optionKey}`,
    "aria-controls": `register-panel-${optionKey}`,
    "aria-selected": activeKey === optionKey,
    tabIndex: activeKey === optionKey ? 0 : -1
  } as const;
};

export const getRegisterPanelAttributes = (
  panelKey: TripleRegisterKey,
  activeKey: TripleRegisterKey
) => {
  return {
    role: "tabpanel",
    id: `register-panel-${panelKey}`,
    "aria-labelledby": `register-tab-${panelKey}`,
    tabIndex: 0,
    hidden: panelKey !== activeKey
  } as const;
};

export const buildCeFRPlaceholder = (layerId: string): string => {
  return `CEFR-B2 readability verification pending for ${layerId}.`;
};

export const translationFidelityPlaceholder = (layerId: string): string => {
  return `Translation fidelity check pending for ${layerId} via future T-SIR validator.`;
};
