import { render } from "@testing-library/react";
import { axe } from "vitest-axe";
import App from "@/App";
import glossaryData from "@/data/glossary.json";
import { GlossaryDrawer } from "@/components/GlossaryDrawer";
import { glossaryPayloadSchema, parseDataOrThrow } from "@/utils/types";

const terms = parseDataOrThrow(glossaryPayloadSchema, glossaryData, "glossary.json").terms;

describe("accessibility", () => {
  it("App layout has no critical accessibility violations", async () => {
    const { container } = render(<App />);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  it("Glossary drawer markup is accessible when open", async () => {
    const { container } = render(<GlossaryDrawer terms={terms} />);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });
});
