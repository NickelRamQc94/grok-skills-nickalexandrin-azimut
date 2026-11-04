#!/usr/bin/env python3
"""tritbyte_loader — assembles payload_XX.b64 → tritbyte.py (gzip+base64)."""
from __future__ import annotations
import base64, gzip, hashlib
from pathlib import Path

EXPECT = "6bd2df445d684db158a1560956331da746a7f60a86bb736632ee6903864997a6"
DIR = Path(__file__).resolve().parent

def main() -> int:
    parts = sorted(DIR.glob("payload_*.b64"))
    if not parts:
        raise SystemExit("no payload_*.b64 next to loader")
    b64 = "".join(p.read_text().strip() for p in parts)
    data = gzip.decompress(base64.b64decode(b64))
    dig = hashlib.sha256(data).hexdigest()
    if dig != EXPECT:
        raise SystemExit(f"sha mismatch {dig}")
    out = DIR / "tritbyte.py"
    out.write_bytes(data)
    print(f"OK {out} {len(data)} bytes")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
