import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    include: ['tests/**/*.test.ts'],
    reporters: ['default', 'junit'],
    outputFile: {
      junit: 'reports/vitest-junit.xml'
    },
    coverage: {
      reporter: ['text', 'lcov'],
      reportsDirectory: 'coverage',
      lines: 60,
      functions: 60,
      statements: 60,
      branches: 40
    }
  }
});
