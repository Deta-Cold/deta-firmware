from typing import TYPE_CHECKING

from .keychain import PATTERNS_ADDRESS, with_keychain_from_path

if TYPE_CHECKING:
    from detahard.messages import EthereumGetAddress, EthereumAddress
    from detahard.wire import Context

    from apps.common.keychain import Keychain
    from .definitions import Definitions


@with_keychain_from_path(*PATTERNS_ADDRESS)
async def get_address(
    ctx: Context,
    msg: EthereumGetAddress,
    keychain: Keychain,
    defs: Definitions,
) -> EthereumAddress:
    from detahard.messages import EthereumAddress
    from detahard.ui.layouts import show_address
    from apps.common import paths
    from .helpers import address_from_bytes

    address_n = msg.address_n  # local_cache_attribute

    await paths.validate_path(ctx, keychain, address_n)

    node = keychain.derive(address_n)

    address = address_from_bytes(node.ethereum_pubkeyhash(), defs.network)

    if msg.show_display:
        await show_address(ctx, address, path=paths.address_n_to_str(address_n))

    return EthereumAddress(address=address)
