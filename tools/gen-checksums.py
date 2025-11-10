# SPDX-License-Identifier: Apache-2.0

#!/usr/bin/env python3
import datetime
import hashlib
import os
from pathlib import Path
from typing import List, Dict

try:
    import yaml  # type: ignore
except ModuleNotFoundError:  # pragma: no cover
    yaml = None  # type: ignore

REPO_ROOT = Path(__file__).resolve().parent.parent
TARGETS: List[Path] = [
    REPO_ROOT / "source",
    REPO_ROOT / "versions",
    REPO_ROOT / "reference",
    REPO_ROOT / "README.md",
]
manifest: Dict[str, object] = {
    "generated": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
    "checksum_algorithm": "SHA-512",
    "checksum_manifest": "versions/checksums.txt",
    "zenodo_concept_doi": "10.5281/zenodo.10990000",
    "zenodo_record": "10.5281/zenodo.10990001",
    "files": [],
}

pdf_hashes: List[Dict[str, str]] = []
for target in TARGETS:
    if target.is_dir():
        for root, _, files in os.walk(target):
            for filename in sorted(files):
                full_path = Path(root) / filename
                if not filename.endswith((".pdf", ".tex", ".md", ".yaml")):
                    continue
                digest = hashlib.sha512(full_path.read_bytes()).hexdigest()
                rel_path = full_path.relative_to(REPO_ROOT)
                manifest["files"].append({"path": str(rel_path), "sha512": digest})
                if rel_path.suffix == ".pdf":
                    pdf_hashes.append({"path": str(rel_path), "sha512": digest})
    elif target.is_file():
        digest = hashlib.sha512(target.read_bytes()).hexdigest()
        rel_path = target.relative_to(REPO_ROOT)
        manifest["files"].append({"path": str(rel_path), "sha512": digest})

meta_dir = REPO_ROOT / "meta"
meta_dir.mkdir(parents=True, exist_ok=True)
manifest_path = meta_dir / "v5-manifest.yaml"
if yaml is not None:
    with manifest_path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(manifest, handle, sort_keys=False)
else:
    lines = [
        f"generated: {manifest['generated']}",
        f"checksum_algorithm: {manifest['checksum_algorithm']}",
        f"checksum_manifest: {manifest['checksum_manifest']}",
        f"zenodo_concept_doi: {manifest['zenodo_concept_doi']}",
        f"zenodo_record: {manifest['zenodo_record']}",
        "files:",
    ]
    for entry in manifest["files"]:  # type: ignore[index]
        lines.append(f"  - path: {entry['path']}")
        lines.append(f"    sha512: {entry['sha512']}")
    manifest_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

checksum_file = REPO_ROOT / "versions" / "checksums.txt"
checksum_file.parent.mkdir(parents=True, exist_ok=True)
if pdf_hashes:
    with checksum_file.open("a", encoding="utf-8") as handle:
        handle.write("\n")
        for entry in sorted(pdf_hashes, key=lambda item: item["path"]):
            handle.write(
                f"- {entry['path'].split('/')[-1]} — SHA-512: {entry['sha512']} (generated {manifest['generated']})\n"
            )

print(f"Checksums updated: {len(manifest['files'])} artefacts, {len(pdf_hashes)} PDFs logged.")

# Authored and maintained solely by the Custodial Editorial Committee.
# This script is provided for non-operational, reproducibility support.
# No AEIP runtime logic is exposed or executed here.
