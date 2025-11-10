import type { Meta, StoryObj } from '@storybook/react';
import LayerCard from '../components/LayerCard';
import type { Layer, Artifact } from '../hooks/useLayerData';

const layer: Layer = {
  id: 'layer-1',
  title: 'Layer 1: Civic Signals',
  description: 'Monitors civic signals and orchestrates intake.',
  registers: {
    civic: 'Community feedback aggregated through partner channels.',
    operational: 'Operational readiness metrics updated hourly.',
    strategic: 'Strategic intent linked to OSI roadmap milestone A1.'
  },
  personas: ['Steward', 'Observer'],
  aeipHooks: ['AEIP-001', 'AEIP-014'],
  artifacts: ['artifact-1'],
  status: 'stable'
};

const artifact: Artifact = {
  id: 'artifact-1',
  name: 'Civic Intake Workbook',
  summary: 'Aggregates requests and observations from civic monitors.',
  updatedAt: '2024-05-01'
};

const meta: Meta<typeof LayerCard> = {
  title: 'Dashboard/LayerCard',
  component: LayerCard,
  args: {
    layer,
    artifact
  }
};

export default meta;

type Story = StoryObj<typeof LayerCard>;

export const Default: Story = {};
