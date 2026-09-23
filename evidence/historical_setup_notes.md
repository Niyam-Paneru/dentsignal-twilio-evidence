# Historical Twilio setup notes

Sanitized copy of the setup notes that lived with the original DentSignal Twilio implementation.

Source commit: `6eb60ec15dcc286a5234c8e6de84174d280b8951`

## Webhooks used for a clinic number

| Type | URL | Method |
|---|---|---|
| Voice | `{API_BASE_URL}/inbound/voice` | POST |
| SMS | `{API_BASE_URL}/api/sms/inbound` | POST |
| Status callback | `{API_BASE_URL}/twilio/status` | POST |

The normal onboarding path was automated through `provision_clinic_number()`, but the same webhooks could be configured manually in Twilio Console.

## Provisioning path

```text
find available number
    ↓
purchase number
    ↓
set Voice webhook
    ↓
set SMS webhook
    ↓
set status callback
    ↓
persist number + SID to clinic
    ↓
test inbound Voice + SMS
```

Useful operations in the original service:

- `list_available_numbers(area_code)`
- `provision_clinic_number(clinic_id, area_code)`
- `update_number_webhooks(phone_sid)`
- `list_clinic_numbers()`
- `release_number(phone_sid)`

## New-clinic checklist used at the time

- provision the Twilio number
- save the number and SID to the clinic record
- test inbound call → AI path
- test inbound SMS → reply-processing path
- verify webhook URLs in Twilio
- verify call status callbacks

## Common install failures I was checking for

- public webhook URL not reachable
- Voice webhook pointed at the wrong route
- SMS webhook pointed at the wrong route
- bad TwiML returned on the Voice path
- manually created number missing one of the configured webhooks
