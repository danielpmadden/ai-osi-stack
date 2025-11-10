import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { MemoryRouter } from 'react-router-dom';
import { describe, expect, it, vi, afterEach } from 'vitest';
import App from '../App';

const mockFetch = () => vi.spyOn(global, 'fetch').mockRejectedValue(new Error('offline'));

describe('AEIP Simulator', () => {
  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('opens a receipt modal on selection', async () => {
    const user = userEvent.setup();
    mockFetch();
    render(
      <MemoryRouter initialEntries={['/aeip']}>
        <App />
      </MemoryRouter>
    );

    const receiptButtons = await screen.findAllByRole('button', { name: /aeip/i });
    await user.click(receiptButtons[0]);
    expect(await screen.findByRole('dialog')).toBeInTheDocument();
  });
});
