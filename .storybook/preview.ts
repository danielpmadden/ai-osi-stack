// SPDX-License-Identifier: Apache-2.0

import type { Preview } from "@storybook/react";
import "../dashboard/src/styles/tokens.css";
import "../dashboard/src/styles/global.css";

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
