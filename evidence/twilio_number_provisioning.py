"""
Sanitized historical extract from DentSignal's Twilio clinic provisioning path.

Source history:
  6eb60ec15dcc286a5234c8e6de84174d280b8951

The original implementation also exposed admin API routes for:
  GET    /api/admin/available-numbers
  POST   /api/admin/provision-number
  GET    /api/admin/clinic-numbers
  POST   /api/admin/fix-webhooks/{sid}
  DELETE /api/admin/release-number/{sid}
"""

from typing import Optional

from twilio.rest import Client


def list_available_numbers(
    client: Client,
    *,
    area_code: Optional[str] = None,
    country: str = "US",
    limit: int = 10,
) -> list[dict]:
    kwargs = {
        "voice_enabled": True,
        "sms_enabled": True,
        "limit": limit,
    }
    if area_code:
        kwargs["area_code"] = area_code

    numbers = client.available_phone_numbers(country).local.list(**kwargs)

    return [
        {
            "phone_number": number.phone_number,
            "friendly_name": number.friendly_name,
            "locality": number.locality,
            "region": number.region,
            "capabilities": {
                "voice": number.capabilities.get("voice", False),
                "sms": number.capabilities.get("sms", False),
            },
        }
        for number in numbers
    ]


def provision_clinic_number(
    client: Client,
    *,
    clinic_id: int,
    api_base_url: str,
    area_code: Optional[str] = None,
    phone_number: Optional[str] = None,
    friendly_name: Optional[str] = None,
) -> dict:
    """Buy a number and configure the DentSignal voice/SMS webhooks in one step."""

    voice_webhook = f"{api_base_url}/inbound/voice"
    sms_webhook = f"{api_base_url}/api/sms/inbound"
    status_callback = f"{api_base_url}/twilio/status"

    common = {
        "friendly_name": friendly_name or f"Clinic {clinic_id}",
        "voice_url": voice_webhook,
        "voice_method": "POST",
        "sms_url": sms_webhook,
        "sms_method": "POST",
        "status_callback": status_callback,
        "status_callback_method": "POST",
    }

    if phone_number:
        number = client.incoming_phone_numbers.create(
            phone_number=phone_number,
            **common,
        )
    elif area_code:
        number = client.incoming_phone_numbers.create(
            area_code=area_code,
            **common,
        )
    else:
        raise ValueError("area_code or phone_number is required")

    return {
        "success": True,
        "phone_number": number.phone_number,
        "sid": number.sid,
        "friendly_name": number.friendly_name,
        "webhooks": {
            "voice": voice_webhook,
            "sms": sms_webhook,
            "status": status_callback,
        },
    }


def update_number_webhooks(
    client: Client,
    *,
    phone_sid: str,
    api_base_url: str,
) -> dict:
    voice_webhook = f"{api_base_url}/inbound/voice"
    sms_webhook = f"{api_base_url}/api/sms/inbound"

    number = client.incoming_phone_numbers(phone_sid).update(
        voice_url=voice_webhook,
        voice_method="POST",
        sms_url=sms_webhook,
        sms_method="POST",
    )

    return {
        "success": True,
        "sid": number.sid,
        "voice_url": voice_webhook,
        "sms_url": sms_webhook,
    }


def release_number(client: Client, *, phone_sid: str) -> None:
    """Release a clinic number when it is no longer needed."""
    client.incoming_phone_numbers(phone_sid).delete()
