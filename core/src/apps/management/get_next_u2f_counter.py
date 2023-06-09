from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from detahard.messages import GetNextU2FCounter, NextU2FCounter
    from detahard.wire import Context


async def get_next_u2f_counter(ctx: Context, msg: GetNextU2FCounter) -> NextU2FCounter:
    import storage.device as storage_device
    from detahard.wire import NotInitialized
    from detahard.enums import ButtonRequestType
    from detahard.messages import NextU2FCounter
    from detahard.ui.layouts import confirm_action

    if not storage_device.is_initialized():
        raise NotInitialized("Device is not initialized")

    await confirm_action(
        ctx,
        "get_u2f_counter",
        "Get next U2F counter",
        description="Do you really want to increase and retrieve the U2F counter?",
        br_code=ButtonRequestType.ProtectCall,
    )

    return NextU2FCounter(u2f_counter=storage_device.next_u2f_counter())
