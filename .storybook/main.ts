// SPDX-License-Identifier: Apache-2.0

import type { StorybookConfig } from "@storybook/react-vite";

const config: StorybookConfig = {
  stories: ["../dashboard/src/**/*.stories.@(ts|tsx)"],
  addons: [
    "@storybook/addon-essentials",
    "@storybook/addon-interactions",
    "@storybook/addon-a11y"
  ],
  framework: {
    name: "@storybook/react-vite",
    options: {}
  },
  docs: {
    autodocs: true
  }
};

export default config;
