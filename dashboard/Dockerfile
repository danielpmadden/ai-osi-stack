# AI OSI Stack Dashboard Dockerfile (offline-first scaffold)
FROM node:20-alpine AS base

WORKDIR /app

# Install dependencies (placeholder for future package.json)
COPY package.json package-lock.json* yarn.lock* pnpm-lock.yaml* ./
RUN if [ -f package.json ]; then npm install --legacy-peer-deps; else echo "No package.json yet; skipping install"; fi

# Copy source
COPY . ./

# Build step placeholder (Vite/Next build commands to be added once project bootstrapped)
RUN if [ -f package.json ]; then npm run build || echo "Build script not yet defined"; fi

# Runtime stage
FROM node:20-alpine AS runtime
WORKDIR /app
COPY --from=base /app /app

# Serve static build via simple http server when available
CMD ["sh", "-c", "if [ -d dist ]; then npx serve dist -l 0.0.0.0:4173; else echo 'Static build not found. Run npm run build first.' && sleep 3600; fi"]
