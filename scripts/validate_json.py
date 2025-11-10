#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def validate_json(path: Path) -> None:
  data = json.loads(path.read_text())
  if not isinstance(data, dict):
    raise SystemExit(f"{path} must contain a JSON object")
  print(f"Validated {path} with keys: {', '.join(data.keys())}")


def main() -> None:
  if len(sys.argv) < 2:
    raise SystemExit("Usage: validate_json.py <path>")
  for arg in sys.argv[1:]:
    validate_json(Path(arg))


if __name__ == '__main__':
  main()
