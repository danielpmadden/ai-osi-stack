// SPDX-License-Identifier: Apache-2.0

import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";
import path from "node:path";

export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,
    environment: "jsdom",
    setupFiles: [path.resolve(__dirname, "vitest.setup.ts")],
    include: ["src/**/*.{spec,test}.tsx"],
    coverage: {
      reporter: ["text", "html"],
      reportsDirectory: "coverage"
    }
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src")
    }
  }
});
