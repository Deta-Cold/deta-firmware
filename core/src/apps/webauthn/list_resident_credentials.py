from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from detahard.messages import WebAuthnListResidentCredentials, WebAuthnCredentials
    from detahard.wire import Context


async def list_resident_credentials(
    ctx: Context, msg: WebAuthnListResidentCredentials
) -> WebAuthnCredentials:
    from detahard.messages import WebAuthnCredential, WebAuthnCredentials
    from detahard.ui.layouts import confirm_action

    from . import resident_credentials

    await confirm_action(
        ctx,
        "credentials_list",
        "List credentials",
        description="Do you want to export information about the resident credentials stored on this device?",
    )
    creds = [
        WebAuthnCredential(
            index=cred.index,
            id=cred.id,
            rp_id=cred.rp_id,
            rp_name=cred.rp_name,
            user_id=cred.user_id,
            user_name=cred.user_name,
            user_display_name=cred.user_display_name,
            creation_time=cred.creation_time,
            hmac_secret=cred.hmac_secret,
            use_sign_count=cred.use_sign_count,
            algorithm=cred.algorithm,
            curve=cred.curve,
        )
        for cred in resident_credentials.find_all()
    ]
    return WebAuthnCredentials(credentials=creds)
