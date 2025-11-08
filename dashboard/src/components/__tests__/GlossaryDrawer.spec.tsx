import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import glossaryData from "@/data/glossary.json";
import { GlossaryDrawer } from "@/components/GlossaryDrawer";
import { glossaryPayloadSchema, parseDataOrThrow } from "@/utils/types";

describe("GlossaryDrawer", () => {
  const terms = parseDataOrThrow(glossaryPayloadSchema, glossaryData, "glossary.json").terms;

  it("filters glossary items and exposes keyboard-focusable entries", async () => {
    render(<GlossaryDrawer terms={terms} />);
    const user = userEvent.setup();

    const openButton = screen.getByRole("button", { name: /open civic glossary/i });
    await user.click(openButton);

    const searchBox = await screen.findByRole("searchbox");
    await user.clear(searchBox);
    await user.type(searchBox, "civic");

    const items = screen.getAllByRole("listitem");
    expect(items.length).toBeGreaterThan(0);
    expect(items[0]).toHaveAttribute("tabindex", "0");
  });
});
