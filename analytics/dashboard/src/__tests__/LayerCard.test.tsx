import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, expect, it } from 'vitest';
import LayerCard from '../components/LayerCard';
import type { Layer, Artifact } from '../hooks/useLayerData';

const layer: Layer = {
  id: 'layer-1',
  title: 'Layer 1',
  description: 'Test layer description',
  registers: {
    civic: 'Civic narrative',
    operational: 'Operational narrative',
    strategic: 'Strategic narrative'
  },
  personas: ['Steward'],
  aeipHooks: ['AEIP-001'],
  artifacts: ['artifact-1'],
  status: 'stable'
};

const artifact: Artifact = {
  id: 'artifact-1',
  name: 'Test artifact',
  summary: 'Summary',
  updatedAt: '2024-05-01'
};

describe('LayerCard', () => {
  it('switches registers when tabs are activated', async () => {
    const user = userEvent.setup();
    render(<LayerCard layer={layer} artifact={artifact} />);

    expect(screen.getByText('Civic narrative')).toBeInTheDocument();
    await user.click(screen.getByRole('tab', { name: /operational/i }));
    expect(screen.getByText('Operational narrative')).toBeInTheDocument();
  });
});
