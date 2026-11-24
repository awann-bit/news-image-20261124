#!/usr/bin/env python3
"""Sum up Tuesday 24 November 2026's world news in one image.

The entry image is a newspaper-style front page, "THE WORLD IN ONE DAY",
with 35 real stories from 24 November 2026. This program simply writes
that image, stored beside it as entry.png, to the output location.
It uses only the standard library and no network. Running it twice
writes exactly the same bytes both times. If the image is missing,
it exits with a clear error instead of a traceback.
"""

import os
import shutil

# The image lives in the repository next to this program; the harness
# runs the program with the repository present, so resolve it from
# this file's own directory rather than from the working directory.
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)

# Fail fast with a clear message if the image is missing, instead of
# crashing with a traceback from the copy below.
if not os.path.isfile(SRC):
    raise SystemExit("entry image not found: %s" % SRC)

shutil.copyfile(SRC, DST)
print("wrote %s %d bytes" % (DST, os.path.getsize(DST)))
