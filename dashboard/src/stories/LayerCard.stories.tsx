import type { Meta, StoryObj } from "@storybook/react";
import layersData from "@/data/layers.json";
import { LayerCard } from "@/components/LayerCard";
import { layerPayloadSchema, parseDataOrThrow } from "@/utils/types";

const { layers } = parseDataOrThrow(layerPayloadSchema, layersData, "layers.json");

const meta: Meta<typeof LayerCard> = {
  title: "Components/LayerCard",
  component: LayerCard,
  parameters: {
    layout: "fullscreen"
  }
};

export default meta;

type Story = StoryObj<typeof LayerCard>;

export const Default: Story = {
  args: {
    layer: layers[0]
  }
};

export const AlignmentLayer: Story = {
  args: {
    layer: layers[Math.min(5, layers.length - 1)]
  }
};
