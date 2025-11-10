import type { Meta, StoryObj } from '@storybook/react';
import IntegrityBadge from '../components/IntegrityBadge';

const meta: Meta<typeof IntegrityBadge> = {
  title: 'Dashboard/IntegrityBadge',
  component: IntegrityBadge,
  args: {
    status: 'verified',
    updatedAt: '2024-05-10'
  }
};

export default meta;

type Story = StoryObj<typeof IntegrityBadge>;

export const Verified: Story = {};
export const Draft: Story = {
  args: {
    status: 'draft'
  }
};
