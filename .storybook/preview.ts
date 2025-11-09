// SPDX-License-Identifier: Apache-2.0

import type { Preview } from "@storybook/react";
import "../analytics/dashboard/src/styles/tokens.css";
import "../analytics/dashboard/src/styles/global.css";

const preview: Preview = {
  parameters: {
    actions: { argTypesRegex: "^on[A-Z].*" },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/
      }
    }
  }
};

export default preview;
