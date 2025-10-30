from __future__ import annotations

# Inspired by the mixing rounds of SHA family: we use constants and rotations
# to diffuse the influence of each byte across the full state.

# First eight bytes of the fractional part of sqrt of the first primes, similar
# to how SHA derives its constants (reduced modulo 256 to fit in a byte).
K_CONSTANTS = [0x5A, 0x6B, 0x79, 0x8F, 0xA1, 0xC3, 0xD5, 0xE9]

# First eight bytes of the fractional part of the cube roots of the first primes.
J_TABLE = [0x42, 0x17, 0x6D, 0x90, 0xB5, 0xCC, 0xE1, 0x3F]


def rotl8(value: int, shift: int) -> int:
    """Rotate an 8‑bit value to the left."""
    shift &= 7
    return ((value << shift) | (value >> (8 - shift))) & 0xFF


def k_mix(index: int, value: int) -> int:
    """K round: rotate and xor with the K constant."""
    rotated = rotl8(value, (index % 3) + 1)
    return rotated ^ K_CONSTANTS[index]


def j_mix(index: int, left: int, right: int) -> int:
    """J round: xor neighbours, add the per-position constant, then rotate."""
    combined = left ^ right ^ J_TABLE[index]
    return rotl8(combined, (index % 5) + 1)


def transform(message: str) -> list[int]:
    """Transform an 8-byte message according to the custom permutation."""
    if len(message.encode("utf-8")) != 8:
        raise ValueError("Le message doit contenir exactement 8 octets UTF-8.")

    block = list(message.encode("utf-8"))
    state = [0] * 8

    for index in range(8):
        left = block[(index - 1) % 8]
        right = block[(index + 1) % 8]
        state[index] = k_mix(index, block[index]) ^ j_mix(index, left, right)

    # Post-round placements as specified:
    state[1] = block[0]  # B goes to second position.
    state[2] = block[1]  # O goes to third position.
    state[4] = block[3] ^ block[4] ^ K_CONSTANTS[4]  # XOR of J, O, and K constant.

    return state


def map_state_to_printable(state: list[int]) -> str:
    """Project bytes onto uppercase ASCII to keep the output human-readable."""
    return "".join(chr(0x41 + (value % 26)) for value in state)


def map_state_to_hex(state: list[int]) -> str:
    """Return the byte state as a contiguous hexadecimal string."""
    return "".join(f"{value:02x}" for value in state)


if __name__ == "__main__":
    input_message = "BONJOUR!"
    output_state = transform(input_message)
    print(f"Entrée : {input_message}")
    print(f"Sortie (ASCII) : {map_state_to_printable(output_state)}")
    print(f"Sortie (hex)   : {map_state_to_hex(output_state)}")
