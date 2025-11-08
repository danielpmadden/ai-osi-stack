import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import layersData from "@/data/layers.json";
import { LayerCard } from "@/components/LayerCard";
import { layerPayloadSchema, parseDataOrThrow } from "@/utils/types";

describe("LayerCard", () => {
  const layer = parseDataOrThrow(layerPayloadSchema, layersData, "layers.json").layers[0];

  it("renders triple register tabs and toggles content", async () => {
    render(<LayerCard layer={layer} />);
    const user = userEvent.setup();

    const narrativeTab = screen.getByRole("tab", { name: /narrative register/i });
    const normativeTab = screen.getByRole("tab", { name: /normative register/i });
    const plainTab = screen.getByRole("tab", { name: /plain-language register/i });

    expect(screen.getAllByRole("tabpanel")).toHaveLength(1);

    await user.click(narrativeTab);
    expect(narrativeTab).toHaveAttribute("aria-selected", "true");

    await user.click(normativeTab);
    expect(normativeTab).toHaveAttribute("aria-selected", "true");

    await user.keyboard("{Tab}{ArrowRight}");
    expect(plainTab).toHaveAttribute("aria-selected", "true");
  });
});
