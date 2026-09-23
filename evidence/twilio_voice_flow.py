"""
Sanitized historical extract from DentSignal's earlier Twilio implementation.

Source history:
  6eb60ec15dcc286a5234c8e6de84174d280b8951

Non-essential product code, credentials and customer data were removed.
"""

from typing import Optional

from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse


def make_call(
    client: Client,
    *,
    twilio_number: str,
    to_number: str,
    call_id: int,
    base_url: str,
) -> dict:
    """Start an outbound call and wire the lifecycle callbacks."""

    call = client.calls.create(
        to=to_number,
        from_=twilio_number,
        url=f"{base_url}/twilio/voice/{call_id}",
        status_callback=f"{base_url}/twilio/status/{call_id}",
        status_callback_event=["initiated", "ringing", "answered", "completed"],
        status_callback_method="POST",
        record=True,
        recording_status_callback=f"{base_url}/twilio/recording/{call_id}",
        machine_detection="Enable",
        machine_detection_timeout=5,
    )

    return {
        "success": True,
        "call_sid": call.sid,
        "status": call.status,
        "call_id": call_id,
    }


def generate_greeting_twiml(
    *,
    lead_name: str,
    clinic_name: str,
    call_id: int,
    base_url: str,
) -> str:
    """Collect speech and send it back into the DentSignal call state machine."""

    response = VoiceResponse()

    gather = Gather(
        input="speech",
        action=f"{base_url}/twilio/gather/{call_id}",
        method="POST",
        timeout=5,
        speech_timeout="auto",
        language="en-US",
    )

    gather.say(
        f"Hi, am I speaking with {lead_name}? "
        f"This is Sarah calling from {clinic_name}. "
        "We noticed you were interested in scheduling an appointment. "
        "Is this a good time to talk?",
        voice="Polly.Joanna",
        language="en-US",
    )

    response.append(gather)
    response.say("I'm sorry, I didn't catch that. Let me try again.", voice="Polly.Joanna")
    response.redirect(f"{base_url}/twilio/voice/{call_id}")

    return str(response)


def get_call_status(client: Client, call_sid: str) -> dict:
    """Read the live Twilio call state."""

    call = client.calls(call_sid).fetch()

    return {
        "call_sid": call.sid,
        "status": call.status,
        "direction": call.direction,
        "duration": call.duration,
        "start_time": str(call.start_time) if call.start_time else None,
        "end_time": str(call.end_time) if call.end_time else None,
    }
