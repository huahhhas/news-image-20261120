#!/usr/bin/env python3
"""news-image-20261120 entrypoint: copy entry.png to the output directory.

Runs with the Python 3.13 standard library only, no network. The image was
drawn by the agent in its build session (see draw_poster_20.py) and is
shipped in this repository; this program only copies it to /output/entry.png.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    with open(SRC, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    os.makedirs(OUT_DIR, exist_ok=True)
    dst = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(SRC, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
