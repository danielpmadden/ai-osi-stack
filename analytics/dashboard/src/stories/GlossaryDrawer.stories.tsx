// SPDX-License-Identifier: Apache-2.0

import type { Meta, StoryObj } from "@storybook/react";
import glossaryData from "@/data/glossary.json";
import { GlossaryDrawer } from "@/components/GlossaryDrawer";
import { glossaryPayloadSchema, parseDataOrThrow } from "@/utils/types";

const { terms } = parseDataOrThrow(glossaryPayloadSchema, glossaryData, "glossary.json");

const meta: Meta<typeof GlossaryDrawer> = {
  title: "Components/GlossaryDrawer",
  component: GlossaryDrawer
};

export default meta;

type Story = StoryObj<typeof GlossaryDrawer>;

export const Default: Story = {
  args: {
    terms
  }
};
