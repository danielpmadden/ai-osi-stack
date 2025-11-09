# Container Hardening Notes

The provided `Dockerfile` builds a multi-stage container that installs Node.js and Python dependencies in isolated stages, copies only the required artefacts to the runtime image, and executes AEIP validators under a non-root user.

## Key Properties

- **Base image:** `node:20-alpine` for minimal footprint.
- **Multi-stage:** Separate dependency resolution for Node (`npm ci`) and Python (`pip wheel`).
- **Non-root execution:** User `aiops` runs the entrypoint.
- **Read-only friendly:** Runtime writes only to `/opt/app/dist`; run the container with `--read-only` and mount a writable volume if needed.
- **Entrypoint:** `ops/container/entrypoint.sh` runs AEIP validators and pytest smoke checks.

## Usage

```bash
docker build -t ai-osi-stack/validator .
docker run --rm \
  --read-only \
  -v "$PWD/dist":/opt/app/dist \
  ai-osi-stack/validator
```

For custom commands, override the entrypoint:

```bash
docker run --rm --entrypoint /bin/sh ai-osi-stack/validator -c "npm run validate:aeip"
```

## Security Posture

- No package manager caches are retained in the final layer.
- The container bundles only the code required for validators.
- Combine with `ops/container/trivy-image-scan.sh` to scan built images before release.
