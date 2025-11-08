import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { AEIPLogViewer } from "@/components/AEIPLogViewer";
import { aeipReceipts } from "@/data/aeip";

describe("AEIPLogViewer", () => {
  it("loads mock receipts and opens modal", async () => {
    render(<AEIPLogViewer receipts={aeipReceipts} />);
    const user = userEvent.setup();

    const firstReceipt = await screen.findByRole("button", { name: /reasoningTrace/i });
    await user.click(firstReceipt);

    expect(screen.getByRole("dialog")).toBeInTheDocument();
    expect(screen.getByText(/JSON-LD/i)).toBeInTheDocument();

    const closeButton = screen.getByRole("button", { name: /close aeip receipt dialog/i });
    await user.click(closeButton);
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });
});
