"""Copy the front-page image to the make.fun output directory.

Standard library only. The entry image ships in this repository as
entry.png; this program copies it byte for byte to
$MAKEFUN_OUTPUT_DIR/entry.png, then checks the copy: PNG magic bytes,
the sha256 digest, and a full read-back comparison against the source.
"""
import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576  # the competition gate: at most 1 MiB


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    dest = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    with open(SOURCE, "rb") as fh:
        data = fh.read()
    if not data.startswith(PNG_MAGIC):
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print("entry.png is %d bytes, over the 1 MiB limit" % len(data),
              file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    shutil.copyfile(SOURCE, dest)
    with open(dest, "rb") as fh:
        copied = fh.read()
    if copied != data:
        print("copy differs from source", file=sys.stderr)
        return 1
    if hashlib.sha256(copied).hexdigest() != digest:
        print("sha256 mismatch after copy", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)" % (dest, len(copied), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
