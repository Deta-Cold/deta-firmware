def boot() -> None:
    from detahard import loop
    import usb
    from .fido2 import handle_reports

    loop.schedule(handle_reports(usb.iface_webauthn))
