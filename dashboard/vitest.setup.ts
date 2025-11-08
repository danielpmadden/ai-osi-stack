import "@testing-library/jest-dom/vitest";
import { toHaveNoViolations } from "vitest-axe";

expect.extend(toHaveNoViolations);

beforeEach(() => {
  document.body.innerHTML = "";
});
