import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { describe, expect, it, vi, afterEach } from 'vitest';
import App from '../App';

const mockFetch = () => vi.spyOn(global, 'fetch').mockRejectedValue(new Error('offline'));

describe('App accessibility', () => {
  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('renders dashboard heading', async () => {
    mockFetch();
    render(
      <MemoryRouter initialEntries={['/']}>
        <App />
      </MemoryRouter>
    );

    expect(await screen.findByRole('heading', { name: /Governance Snapshot/i })).toBeInTheDocument();
  });
});
