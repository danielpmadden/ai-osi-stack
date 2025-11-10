import type { Meta, StoryObj } from '@storybook/react';
import AEIPReceiptCard from '../components/AEIPReceiptCard';
import type { AEIPReceipt } from '../data/aeip/schema';

const receipt: AEIPReceipt = {
  id: 'aeip-001',
  layerId: 'layer-1',
  issuedAt: '2024-05-16T10:00:00Z',
  status: 'complete',
  summary: 'Handshake with Civic Signals confirmed',
  handshake: {
    counterpart: 'City Data Office',
    nextAction: 'Deliver weekly brief'
  }
};

const meta: Meta<typeof AEIPReceiptCard> = {
  title: 'Dashboard/AEIPReceiptCard',
  component: AEIPReceiptCard,
  args: {
    receipt
  }
};

export default meta;

type Story = StoryObj<typeof AEIPReceiptCard>;

export const Default: Story = {};
