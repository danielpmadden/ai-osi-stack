import type { Meta, StoryObj } from "@storybook/react";
import { AEIPLogViewer } from "@/components/AEIPLogViewer";
import { aeipReceipts } from "@/data/aeip";

const meta: Meta<typeof AEIPLogViewer> = {
  title: "Components/AEIPLogViewer",
  component: AEIPLogViewer
};

export default meta;

type Story = StoryObj<typeof AEIPLogViewer>;

export const Default: Story = {
  args: {
    receipts: aeipReceipts
  }
};
