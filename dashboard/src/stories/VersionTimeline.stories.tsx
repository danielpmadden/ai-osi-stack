import type { Meta, StoryObj } from "@storybook/react";
import updatePlansData from "@/data/update_plans.json";
import { VersionTimeline } from "@/components/VersionTimeline";
import { parseDataOrThrow, updatePlanPayloadSchema } from "@/utils/types";

const { plans } = parseDataOrThrow(updatePlanPayloadSchema, updatePlansData, "update_plans.json");

const meta: Meta<typeof VersionTimeline> = {
  title: "Components/VersionTimeline",
  component: VersionTimeline
};

export default meta;

type Story = StoryObj<typeof VersionTimeline>;

export const Default: Story = {
  args: {
    plans
  }
};
