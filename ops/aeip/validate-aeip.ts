import { promises as fs } from 'fs';
import path from 'path';
import process from 'process';
import Ajv, { ValidateFunction } from 'ajv';
import addFormats from 'ajv-formats';
import { fileURLToPath } from 'url';

const ajv = new Ajv({ strict: false, allErrors: true });
addFormats(ajv);

const repoRoot = process.cwd();
const schemaDir = path.join(repoRoot, 'schemas', 'aeip');
const validators = new Map<string, ValidateFunction>();

type Receipt = {
  schema_ref: string;
  privacy?: { scope?: string };
  provenance?: { source?: string };
  uncertainty?: { score?: number };
  signatures?: Array<Record<string, unknown>>;
};

async function loadJson(target: string) {
  const content = await fs.readFile(target, 'utf-8');
  return JSON.parse(content);
}

async function resolveValidator(schemaRef: string) {
  if (!validators.has(schemaRef)) {
    const schemaPath = path.join(schemaDir, schemaRef);
    const schema = await loadJson(schemaPath);
    validators.set(schemaRef, ajv.compile(schema));
  }
  return validators.get(schemaRef)!;
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

function assertGovernanceFields(receiptPath: string, receipt: Receipt) {
  if (!receipt.privacy || typeof receipt.privacy.scope !== 'string') {
    throw new Error(`${receiptPath}: privacy.scope is required`);
  }
  if (!receipt.provenance || typeof receipt.provenance.source !== 'string') {
    throw new Error(`${receiptPath}: provenance.source is required`);
  }
  if (
    !receipt.uncertainty ||
    typeof receipt.uncertainty.score !== 'number' ||
    receipt.uncertainty.score < 0 ||
    receipt.uncertainty.score > 1
  ) {
    throw new Error(`${receiptPath}: uncertainty.score must be between 0 and 1`);
  }
  if (!Array.isArray(receipt.signatures) || receipt.signatures.length === 0) {
    throw new Error(`${receiptPath}: signatures must include at least one entry`);
  }
}

async function main() {
  const args = process.argv.slice(2);
  const targets = args.length > 0 ? args : [path.join(repoRoot, 'examples', 'aeip')];
  const files = await collectReceipts(targets);
  if (files.length === 0) {
    console.error('No receipts found for validation.');
    process.exit(1);
  }
  const failures: string[] = [];
  for (const file of files) {
    try {
      const data = (await loadJson(file)) as Receipt;
      if (!data.schema_ref) {
        throw new Error('schema_ref is missing');
      }
      const validator = await resolveValidator(data.schema_ref);
      const valid = validator(data);
      if (!valid) {
        const errors = validator.errors?.map((error) => `${error.instancePath} ${error.message}`).join('; ');
        throw new Error(errors ?? 'Validation failed');
      }
      assertGovernanceFields(file, data);
      console.log(`✔ ${path.relative(repoRoot, file)} validated against ${data.schema_ref}`);
    } catch (error) {
      failures.push(`${file}: ${(error as Error).message}`);
    }
  }
  if (failures.length > 0) {
    failures.forEach((failure) => console.error(`✖ ${failure}`));
    process.exit(1);
  }
}

const modulePath = fileURLToPath(import.meta.url);

if (process.argv[1] && path.resolve(process.argv[1]) === modulePath) {
  await main();
}
