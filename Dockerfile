# syntax=docker/dockerfile:1.6
# SPDX-License-Identifier: Apache-2.0

FROM node:20-alpine AS node_deps
WORKDIR /opt/app
COPY package.json package-lock.json ./
RUN npm ci --audit=false --fund=false
COPY tsconfig.json vitest.config.ts .eslintrc.cjs .prettierrc.json ./
COPY ops ops
COPY examples examples
COPY schemas schemas
COPY tests tests
COPY requirements.txt requirements.txt

FROM python:3.12-alpine AS python_deps
WORKDIR /wheel
COPY requirements.txt ./
RUN pip wheel --wheel-dir=/wheel -r requirements.txt

FROM node:20-alpine AS runtime
WORKDIR /opt/app
RUN addgroup -S aiops && adduser -S aiops -G aiops
ENV NODE_ENV=production \
    PYTHONUNBUFFERED=1 \
    HOME=/opt/app
COPY --from=node_deps /opt/app /opt/app
COPY --from=python_deps /wheel /tmp/wheel
RUN apk add --no-cache python3 py3-pip && \
    pip install --no-cache-dir --no-index --find-links=/tmp/wheel -r requirements.txt && \
    rm -rf /tmp/wheel && \
    mkdir -p /opt/app/dist && \
    chown -R aiops:aiops /opt/app
USER aiops
VOLUME ["/opt/app/dist"]
ENTRYPOINT ["/opt/app/ops/container/entrypoint.sh"]
CMD []
