from typing import *


# extmod/moddetahardcrypto/moddetahardcrypto-bech32.h
def decode(
    bech: str,
    max_bech_len: int = 90,
) -> tuple[str, list[int], Encoding]:
    """
    Decode a Bech32 or Bech32m string
    """
