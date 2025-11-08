// SPDX-License-Identifier: Apache-2.0

import "@testing-library/jest-dom/vitest";
import { toHaveNoViolations } from "vitest-axe";

expect.extend(toHaveNoViolations);

beforeEach(() => {
  document.body.innerHTML = "";
});
