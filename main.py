#!/usr/bin/env python3
"""Ship the entry image: copy entry.png into the output folder.

The image sits next to this program. This script places a copy of it
where the harness expects it: the folder named by MAKEFUN_OUTPUT_DIR
when that is set, otherwise /output.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"


def output_dir():
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    # Stop early with a plain message when the image is absent, instead
    # of failing halfway through the copy below.
    if not source.is_file():
        sys.exit(f"missing entry image: {source}")
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / IMAGE_NAME
    shutil.copyfile(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
