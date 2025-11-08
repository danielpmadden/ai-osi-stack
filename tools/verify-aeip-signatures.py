# SPDX-License-Identifier: Apache-2.0

#!/usr/bin/env python3
"""Legacy entry point retained for compatibility; emits advisory guidance."""

from pathlib import Path
import sys

def main() -> int:
    """Deprecated in favour of advisory checksum guidance."""
    notice = (
        "Advisory notice: formal signature validation is no longer provided. "
        "See meta/INTEGRITY_NOTICE.md for recommended checksum logging steps."
    )
    print(notice)
    return 0


if __name__ == "__main__":
    sys.exit(main())
