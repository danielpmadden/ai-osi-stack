import { promises as fs } from 'fs';
import path from 'path';
import process from 'process';
import Ajv, { ValidateFunction } from 'ajv';
import addFormats from 'ajv-formats';
import { fileURLToPath } from 'url';

type GovernanceSchema = {
  canonicalMetadata?: Record<string, unknown>;
};

type GovernanceReceipt = {
  schema_ref: string;
  artifact_type?: string;
  layer?: string;
};

const GOVERNANCE_SCHEMAS = [
  'civic-charter-schema.json',
  'gds-schema.json',
  'incident-report-schema.json',
];

const SCHEMA_ALIASES: Record<string, string> = {
  'civic_charter.schema.json': 'civic-charter-schema.json',
  'gds.schema.json': 'gds-schema.json',
  'incident_report.schema.json': 'incident-report-schema.json',
};

const LAYER_EXPECTATIONS: Record<string, string[]> = {
  'civic-charter': ['L0'],
  'governance-decision-summary': ['L6', 'L7'],
  'incident-report': ['L6', 'L7'],
};

const ajv = new Ajv({ strict: false, allErrors: true });
addFormats(ajv);

const repoRoot = process.cwd();
const schemaDir = path.join(repoRoot, 'schemas', 'aeip');

async function loadJson(target: string) {
  const content = await fs.readFile(target, 'utf-8');
  return JSON.parse(content);
}

async function loadGovernanceSchemas() {
  const validators = new Map<string, ValidateFunction>();
  for (const file of GOVERNANCE_SCHEMAS) {
    const schemaPath = path.join(schemaDir, file);
    const schema = (await loadJson(schemaPath)) as GovernanceSchema;
    const canonical = schema.canonicalMetadata;
    if (!canonical) {
      throw new Error(`${file} is missing canonicalMetadata block`);
    }
    for (const key of [
      'canonical_version',
      'canonical_date',
      'aeip_version',
      'repository_of_record',
      'domain_of_record',
    ]) {
      if (typeof canonical[key] !== 'string' && key !== 'supersedes_all_prior_metadata') {
        throw new Error(`${file} canonicalMetadata.${key} must be present`);
      }
    }
    const validator = ajv.compile(schema);
    validators.set(file, validator);
  }
  return validators;
}

async function gatherReceipts(inputs: string[]): Promise<string[]> {
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

function assertLayerCompliance(receiptPath: string, receipt: GovernanceReceipt) {
  if (!receipt.artifact_type || !receipt.layer) return;
  const expected = LAYER_EXPECTATIONS[receipt.artifact_type];
  if (expected && !expected.includes(receipt.layer)) {
    throw new Error(
      `${receiptPath}: layer ${receipt.layer} is not allowed for artifact_type ${receipt.artifact_type}`,
    );
  }
}

async function main() {
  const args = process.argv.slice(2);
  const targets = args.length > 0 ? args : [path.join(repoRoot, 'examples', 'aeip')];
  const receipts = await gatherReceipts(targets);
  const validators = await loadGovernanceSchemas();

  let hasGovernanceReceipts = false;
  const failures: string[] = [];
  for (const receiptPath of receipts) {
    const data = (await loadJson(receiptPath)) as GovernanceReceipt;
    const normalizedSchemaRef = SCHEMA_ALIASES[data.schema_ref] ?? data.schema_ref;
    if (!normalizedSchemaRef || !validators.has(normalizedSchemaRef)) {
      continue;
    }
    hasGovernanceReceipts = true;
    const validator = validators.get(normalizedSchemaRef)!;
    const valid = validator(data);
    try {
      if (!valid) {
        const message = validator.errors
          ?.map((error) => `${error.instancePath} ${error.message}`)
          .join('; ');
        throw new Error(message ?? 'Validation failed');
      }
      assertLayerCompliance(receiptPath, data);
      console.log(`✔ ${path.relative(repoRoot, receiptPath)} validated against ${normalizedSchemaRef}`);
    } catch (error) {
      failures.push(`${receiptPath}: ${(error as Error).message}`);
    }
  }

  if (!hasGovernanceReceipts) {
    console.warn('No governance receipts referencing civic charter, GDS, or incident schemas were found.');
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
