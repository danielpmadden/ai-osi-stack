// SPDX-License-Identifier: Apache-2.0

import path from "node:path";
import { promises as fs } from "node:fs";
import process from "node:process";
import Ajv, { type ErrorObject } from "ajv";
import addFormats from "ajv-formats";

const ajv = new Ajv({ allErrors: true, strict: false });
addFormats(ajv);

const rootDir = path.resolve(__dirname, "..", "src", "data");
const schemaDir = path.join(rootDir, "schemas");

const targets: Array<{ data: string; schema: string }> = [
  { data: "layers.json", schema: "layers.schema.json" },
  { data: "artifacts.json", schema: "artifacts.schema.json" },
  { data: "personas.json", schema: "personas.schema.json" },
  { data: "update_plans.json", schema: "update_plans.schema.json" },
  { data: "glossary.json", schema: "glossary.schema.json" }
];

const formatErrors = (errors: ErrorObject[] = []) =>
  errors
    .map((error) => {
      const dataPath = error.instancePath || "/";
      const message = error.message ?? "Validation error";
      const params = JSON.stringify(error.params);
      return `  • ${dataPath}: ${message} (${params})`;
    })
    .join("\n");

async function validate() {
  let hasErrors = false;

  for (const target of targets) {
    const dataPath = path.join(rootDir, target.data);
    const schemaPath = path.join(schemaDir, target.schema);

    try {
      const [dataRaw, schemaRaw] = await Promise.all([
        fs.readFile(dataPath, "utf-8"),
        fs.readFile(schemaPath, "utf-8")
      ]);

      const schema = JSON.parse(schemaRaw);
      const validateFn = ajv.compile(schema);
      const data = JSON.parse(dataRaw);
      const valid = validateFn(data);

      if (!valid) {
        hasErrors = true;
        console.error(`\nValidation failed for ${path.relative(process.cwd(), dataPath)}`);
        console.error(formatErrors(validateFn.errors));
      } else {
        console.log(`✓ ${target.data} valid`);
      }
    } catch (error) {
      hasErrors = true;
      console.error(`\nError validating ${target.data}:`, error);
    }
  }

  if (hasErrors) {
    process.exit(1);
  }
}

validate();
