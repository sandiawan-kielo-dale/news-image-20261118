"""make.fun entry: 'Sum up 18 November's world news in one image'.

Copies the pre-rendered infographic entry.png (next to this file) to
<output dir>/entry.png, where the output dir is $MAKEFUN_OUTPUT_DIR or /output.
Before copying it checks the PNG signature, the IHDR size (<= 1024x1024) and
the file size (<= 1 MiB). Standard library only; output is byte-identical
on every run.
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
PNG_SIG = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
MAX_SIDE = 1024


def validate(path):
    """Return (width, height) of a valid PNG within the limits, else raise."""
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise ValueError(f"{path}: {size} bytes exceeds {MAX_BYTES}")
    with open(path, "rb") as f:
        head = f.read(24)
        f.seek(-12, os.SEEK_END)
        tail = f.read(12)
    if head[:8] != PNG_SIG or head[12:16] != b"IHDR":
        raise ValueError(f"{path}: not a PNG")
    if tail[4:8] != b"IEND":
        raise ValueError(f"{path}: truncated PNG (no IEND)")
    width, height = struct.unpack(">II", head[16:24])
    if not (0 < width <= MAX_SIDE and 0 < height <= MAX_SIDE):
        raise ValueError(f"{path}: {width}x{height} exceeds {MAX_SIDE}px")
    return width, height


def main():
    validate(SRC)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    w, h = validate(dst)
    print(f"wrote {dst} ({w}x{h}, {os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
