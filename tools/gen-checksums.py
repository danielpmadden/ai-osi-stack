#!/usr/bin/env python3
import hashlib
import os
import datetime

try:
    import yaml  # type: ignore
except ModuleNotFoundError:  # pragma: no cover
    yaml = None  # type: ignore

target_dirs = ["source", "versions", "reference", "README.md"]
manifest = {"generated": str(datetime.datetime.utcnow())[:19], "files": []}

for path in target_dirs:
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for f in files:
                full = os.path.join(root, f)
                if not f.endswith((".pdf", ".tex", ".md", ".yaml")):
                    continue
                with open(full, "rb") as fh:
                    h = hashlib.sha512(fh.read()).hexdigest()
                manifest["files"].append({"path": full, "sha512": h})
    elif os.path.isfile(path):
        with open(path, "rb") as fh:
            h = hashlib.sha512(fh.read()).hexdigest()
        manifest["files"].append({"path": path, "sha512": h})

os.makedirs("meta", exist_ok=True)
if yaml is not None:
    with open("meta/v5-manifest.yaml", "w") as f:
        yaml.safe_dump(manifest, f)
else:
    lines = ["generated: {}".format(manifest["generated"]), "files:"]
    for entry in manifest["files"]:
        lines.append(f"  - path: {entry['path']}")
        lines.append(f"    sha512: {entry['sha512']}")
    with open("meta/v5-manifest.yaml", "w") as f:
        f.write("\n".join(lines) + "\n")

print("Checksums updated:", len(manifest["files"]))
