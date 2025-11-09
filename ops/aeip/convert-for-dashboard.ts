import { promises as fs } from 'fs';
import path from 'path';
import process from 'process';
import { fileURLToPath } from 'url';

type Receipt = {
  id?: string;
  artifact_type?: string;
  layer?: string;
  lifecycle?: { current?: string; timestamp?: string };
  summary?: string;
  privacy?: { scope?: string };
  provenance?: { source?: string };
  uncertainty?: { score?: number };
  signatures?: Array<{ role?: string; actor?: string; value?: string }>;
  hashes?: { sha512?: string };
  linked_artifacts?: string[];
};

export type DashboardEntry = {
  id: string;
  artifactType: string;
  layer: string;
  lifecycle: string;
  timestamp: string | null;
  summary: string | null;
  privacyScope: string | null;
  provenanceSource: string | null;
  uncertaintyScore: number | null;
  signatures: Array<{ role: string; actor: string; redacted: boolean }>;
  hash: string | null;
  links: string[];
};

async function loadReceipt(file: string): Promise<Receipt> {
  const content = await fs.readFile(file, 'utf-8');
  return JSON.parse(content) as Receipt;
}

export function convertReceipt(receipt: Receipt, file: string): DashboardEntry {
  if (!receipt.id || !receipt.artifact_type || !receipt.layer) {
    throw new Error(`${file} missing required identity fields`);
  }
  const timestamp = receipt.lifecycle?.timestamp ?? null;
  return {
    id: receipt.id,
    artifactType: receipt.artifact_type,
    layer: receipt.layer,
    lifecycle: receipt.lifecycle?.current ?? 'unknown',
    timestamp,
    summary: receipt.summary ?? null,
    privacyScope: receipt.privacy?.scope ?? null,
    provenanceSource: receipt.provenance?.source ?? null,
    uncertaintyScore: typeof receipt.uncertainty?.score === 'number' ? receipt.uncertainty!.score : null,
    signatures:
      receipt.signatures?.map((signature) => ({
        role: signature.role ?? 'unknown',
        actor: signature.actor ?? 'unknown',
        redacted: typeof signature.value === 'string' ? signature.value.includes('[redacted') : false,
      })) ?? [],
    hash: receipt.hashes?.sha512 ?? null,
    links: receipt.linked_artifacts ?? [],
  };
}

async function collectReceipts(inputs: string[]): Promise<string[]> {
  const files: string[] = [];
  for (const input of inputs) {
    const absolute = path.resolve(input);
    const stats = await fs.stat(absolute);
    if (stats.isDirectory()) {
      const entries = await fs.readdir(absolute);
      for (const entry of entries) {
        if (!entry.endsWith('.json') && !entry.endsWith('.jsonld')) continue;
        files.push(path.join(absolute, entry));
      }
    } else if (stats.isFile()) {
      files.push(absolute);
    }
  }
  return files.sort();
}

async function main() {
  const args = process.argv.slice(2);
  const inputs: string[] = [];
  let outPath: string | null = null;
  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];
    if (arg === '--out') {
      outPath = args[index + 1] ?? null;
      index += 1;
    } else {
      inputs.push(arg);
    }
  }
  const targets = inputs.length > 0 ? inputs : [path.join(process.cwd(), 'examples', 'aeip')];
  const files = await collectReceipts(targets);
  if (files.length === 0) {
    throw new Error('No receipts found.');
  }
  const entries: DashboardEntry[] = [];
  for (const file of files) {
    const receipt = await loadReceipt(file);
    entries.push(convertReceipt(receipt, file));
  }
  const output = JSON.stringify(
    {
      generatedAt: new Date().toISOString(),
      entries,
    },
    null,
    2,
  );
  if (outPath) {
    await fs.mkdir(path.dirname(outPath), { recursive: true });
    await fs.writeFile(outPath, output);
    console.log(`Wrote ${entries.length} receipts to ${outPath}`);
  } else {
    process.stdout.write(output);
  }
}

const modulePath = fileURLToPath(import.meta.url);

if (process.argv[1] && path.resolve(process.argv[1]) === modulePath) {
  await main();
}
