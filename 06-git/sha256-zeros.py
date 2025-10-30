#!/usr/bin/env python3
"""Search for a 32-bit decimal suffix that makes SHA-256('bonjour!' + suffix) start with '00'."""

from __future__ import annotations

import hashlib
import sys
from typing import Tuple

PREFIX = b"BONJOUR!"
REQUIRED_PREFIX = "000000"


def compute_hash(nonce: int) -> Tuple[str, str, bytes]:
    """Return the hexadecimal digest, ascii suffix, and raw bytes for the given nonce."""
    suffix_str = str(nonce)
    suffix_bytes = suffix_str.encode("ascii")
    message = PREFIX + suffix_bytes
    digest = hashlib.sha256(message).digest()
    return digest.hex(), suffix_str, message


def find_nonce() -> Tuple[int, str, str, bytes]:
    """Brute-force a nonce whose digest starts with REQUIRED_PREFIX."""
    for nonce in range(2**32):
        hex_digest, suffix_str, message = compute_hash(nonce)
        if hex_digest.startswith(REQUIRED_PREFIX):
            return nonce, suffix_str, hex_digest, message
    raise RuntimeError("Aucun nonce trouvé dans l'espace 32 bits.")


def main() -> None:
    nonce, suffix_str, hex_digest, message = find_nonce()
    print("Préfixe:", PREFIX.decode("ascii"))
    print("Nonce (entier 32 bits):", nonce)
    print("Nonce (ascii):", suffix_str)
    print("Message complet:", message.decode("ascii"))
    print("Hash SHA-256:", hex_digest)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nInterrompu par l'utilisateur.")
