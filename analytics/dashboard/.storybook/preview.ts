import type { Preview } from '@storybook/react';
import '../src/styles/tokens.css';
import '../src/styles/theme.css';
import '../src/styles/global.css';

const preview: Preview = {
  parameters: {
    controls: { expanded: true },
    layout: 'fullscreen'
  }
};

export default preview;
