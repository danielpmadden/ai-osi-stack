// SPDX-License-Identifier: Apache-2.0

import type { Meta, StoryObj } from "@storybook/react";
import artifactsData from "@/data/artifacts.json";
import layersData from "@/data/layers.json";
import { ArtifactGallery } from "@/components/ArtifactGallery";
import { artifactPayloadSchema, layerPayloadSchema, parseDataOrThrow } from "@/utils/types";

const { artifacts } = parseDataOrThrow(artifactPayloadSchema, artifactsData, "artifacts.json");
const { layers } = parseDataOrThrow(layerPayloadSchema, layersData, "layers.json");

const meta: Meta<typeof ArtifactGallery> = {
  title: "Components/ArtifactGallery",
  component: ArtifactGallery
};

export default meta;

type Story = StoryObj<typeof ArtifactGallery>;

export const Default: Story = {
  args: {
    artifacts,
    layers
  }
};
