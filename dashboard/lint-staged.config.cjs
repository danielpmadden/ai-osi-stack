// SPDX-License-Identifier: Apache-2.0

module.exports = {
  "*.{ts,tsx,js,jsx,css,json,md}": [
    "prettier --write"
  ],
  "src/**/*.{ts,tsx}": [
    "eslint --fix",
    "npm run validate:data",
    "npm run typecheck"
  ]
};
