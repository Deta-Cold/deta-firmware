# This file is part of the detahard project.
#
# Copyright (C) 2012-2022 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

from typing import TYPE_CHECKING

from . import messages
from .tools import expect

if TYPE_CHECKING:
    from .client import detahardClient
    from .tools import Address
    from .protobuf import MessageType


# MAINNET = 0
# TESTNET = 1
# STAGENET = 2
# FAKECHAIN = 3


@expect(messages.MoneroAddress, field="address", ret_type=bytes)
def get_address(
    client: "detahardClient",
    n: "Address",
    show_display: bool = False,
    network_type: messages.MoneroNetworkType = messages.MoneroNetworkType.MAINNET,
) -> "MessageType":
    return client.call(
        messages.MoneroGetAddress(
            address_n=n, show_display=show_display, network_type=network_type
        )
    )


@expect(messages.MoneroWatchKey)
def get_watch_key(
    client: "detahardClient",
    n: "Address",
    network_type: messages.MoneroNetworkType = messages.MoneroNetworkType.MAINNET,
) -> "MessageType":
    return client.call(
        messages.MoneroGetWatchKey(address_n=n, network_type=network_type)
    )
