import type { Meta, StoryObj } from "@storybook/react";
import layersData from "@/data/layers.json";
import { IntegrityBadge } from "@/components/IntegrityBadge";
import { layerPayloadSchema, parseDataOrThrow } from "@/utils/types";

const { canonical_version } = parseDataOrThrow(layerPayloadSchema, layersData, "layers.json");

const meta: Meta<typeof IntegrityBadge> = {
  title: "Components/IntegrityBadge",
  component: IntegrityBadge
};

export default meta;

type Story = StoryObj<typeof IntegrityBadge>;

export const Default: Story = {
  args: {
    canonical: canonical_version
  }
};
