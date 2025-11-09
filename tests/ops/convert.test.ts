import { describe, expect, it } from 'vitest';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

import { convertReceipt, type DashboardEntry } from '../../ops/aeip/convert-for-dashboard';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..', '..');

describe('convert-for-dashboard', () => {
  it('creates normalized entries', () => {
    const receiptsDir = path.join(repoRoot, 'examples/aeip');
    const files = fs
      .readdirSync(receiptsDir)
      .filter((file) => file.endsWith('.jsonld'))
      .map((file) => path.join(receiptsDir, file));
    const entries: DashboardEntry[] = [];
    for (const file of files) {
      const data = JSON.parse(fs.readFileSync(file, 'utf-8'));
      entries.push(convertReceipt(data, file));
    }
    expect(entries.length).toBeGreaterThanOrEqual(5);
    for (const entry of entries) {
      expect(entry.id).toMatch(/^urn:uuid:/);
      expect(entry.hash?.length ?? 0).toBe(128);
      expect(entry.signatures.length).toBeGreaterThan(0);
    }
  });
});
