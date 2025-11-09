#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Purpose: Generate reproducible repository inventory metadata.
# Usage: ./ops/inventory/inventory.sh
# Requirements: bash, git, python3. Installs should be handled by the caller or CI pipeline.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
OUTPUT_DIR="$REPO_ROOT/ops/inventory"
FILE_JSON="$OUTPUT_DIR/file-inventory.json"
SOURCE_CSV="$OUTPUT_DIR/source-index.csv"

mkdir -p "$OUTPUT_DIR"

export REPO_ROOT OUTPUT_DIR FILE_JSON SOURCE_CSV

python3 - <<'PY'
"""Generate inventory artifacts describing repository state."""
import csv
import hashlib
import json
import os
import stat
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, Tuple

REPO_ROOT = Path(os.environ.get("REPO_ROOT", ".")).resolve()
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "ops/inventory")).resolve()
FILE_JSON = Path(os.environ.get("FILE_JSON", OUTPUT_DIR / "file-inventory.json")).resolve()
SOURCE_CSV = Path(os.environ.get("SOURCE_CSV", OUTPUT_DIR / "source-index.csv")).resolve()

EXCLUDE_DIRS = {
    ".git",
    ".github/node_modules",
}

TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".py",
    ".ts",
    ".js",
    ".json",
    ".yaml",
    ".yml",
    ".sh",
    ".ps1",
    ".toml",
    ".lock",
    ".csv",
}

LFS_POINTER_PREFIX = "version https://git-lfs.github.com/spec"


def should_skip(path: Path) -> bool:
    parts = path.relative_to(REPO_ROOT).parts
    for index in range(1, len(parts) + 1):
        prefix = Path(*parts[:index])
        if str(prefix) in EXCLUDE_DIRS:
            return True
    return False


def detect_binary(content: bytes) -> bool:
    if not content:
        return False
    if b"\0" in content:
        return True
    text_chars = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x7F)))
    translated = content.translate(None, text_chars)
    return bool(translated)


def sha512(path: Path) -> str:
    digest = hashlib.sha512()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def detect_mime(path: Path) -> str:
    try:
        import mimetypes

        mime, encoding = mimetypes.guess_type(str(path))
        if mime:
            return mime
        if encoding:
            return encoding
    except Exception:
        pass
    return "application/octet-stream"


def has_license_header(path: Path) -> bool:
    try:
        with path.open("r", encoding="utf-8") as handle:
            start = handle.read(512)
    except Exception:
        return False
    return "SPDX-License-Identifier" in start


files: Iterable[Path] = (
    path
    for path in REPO_ROOT.rglob("*")
    if path.is_file() and not should_skip(path)
)

file_records = []
ext_counter: Counter[str] = Counter()
max_line_lengths: Dict[str, int] = {}
line_counts: Dict[str, int] = {}

for path in sorted(files):
    rel = path.relative_to(REPO_ROOT)
    size = path.stat().st_size
    mode = path.stat().st_mode
    executable = bool(mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
    digest = sha512(path)
    mime = detect_mime(path)
    with path.open("rb") as handle:
        content = handle.read(8192)
    binary = detect_binary(content)
    license_header = has_license_header(path) if not binary else False
    is_lfs = False
    try:
        if size < 1024:
            text = path.read_text(encoding="utf-8")
            if text.startswith(LFS_POINTER_PREFIX):
                is_lfs = True
    except Exception:
        pass

    file_records.append(
        {
            "path": str(rel),
            "size_bytes": size,
            "sha512": digest,
            "mime_type": mime,
            "git_lfs_pointer": is_lfs,
            "executable": executable,
            "license_header": license_header,
            "binary": binary,
        }
    )

    ext = path.suffix.lower()
    if ext:
        lines = 0
        max_len = 0
        try:
            with path.open("r", encoding="utf-8", errors="ignore") as handle:
                for line in handle:
                    lines += 1
                    max_len = max(max_len, len(line.rstrip("\n")))
        except Exception:
            lines = 0
            max_len = 0
        ext_counter[ext] += lines
        line_counts[ext] = line_counts.get(ext, 0) + lines
        max_line_lengths[ext] = max(max_line_lengths.get(ext, 0), max_len)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

with FILE_JSON.open("w", encoding="utf-8") as handle:
    json.dump(
        {
            "generated_at": datetime.now(tz=timezone.utc).isoformat(),
            "repository": REPO_ROOT.name,
            "files": file_records,
        },
        handle,
        indent=2,
        sort_keys=True,
    )

with SOURCE_CSV.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow([
        "extension",
        "total_lines",
        "max_line_length",
        "language_bucket",
        "test_coverage_min",
        "test_coverage_max",
    ])
    for ext, total in sorted(line_counts.items()):
        bucket = "other"
        if ext in {".ts", ".tsx"}:
            bucket = "typescript"
        elif ext in {".js", ".jsx"}:
            bucket = "javascript"
        elif ext in {".py"}:
            bucket = "python"
        writer.writerow([
            ext or "(none)",
            total,
            max_line_lengths.get(ext, 0),
            bucket,
            "TBD",
            "TBD",
        ])
PY

printf 'Inventory artifacts generated at %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
