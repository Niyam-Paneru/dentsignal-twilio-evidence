# DentSignal — Twilio evidence

DentSignal is private, so I pulled out the parts of its earlier Twilio implementation that are relevant here.

This isn't a demo rebuilt for an application. These are sanitized extracts from the real project history: Voice calls, TwiML/webhooks, number provisioning, status callbacks, SMS, admin install routes, and the later security/migration work.

### Files

- [twilio_voice_flow.py](evidence/twilio_voice_flow.py) — outbound Voice, status callbacks, recording callback, AMD, TwiML speech flow, call-status lookup
- [twilio_number_provisioning.py](evidence/twilio_number_provisioning.py) — number search/purchase, voice + SMS webhook config, repair, release
- [admin_number_routes.py](evidence/admin_number_routes.py) — FastAPI install/maintenance endpoints around provisioning
- [historical_setup_notes.md](evidence/historical_setup_notes.md) — the onboarding/webhook checklist used with the Twilio version
- [security_and_migration.md](evidence/security_and_migration.md) — security hardening and the later provider migration

### Original DentSignal history

The private repo has the original history. These are the main hashes behind this pack:

- `6eb60ec15dcc286a5234c8e6de84174d280b8951` — automated number provisioning + webhook setup
- `27d321263f31c2fa027995baebc05d8b3ec4b351` — Twilio setup / after-hours call behavior
- `130de4c8fba6429e7cb815f1daf48b6bb7592e9b` — healthcare security work + Twilio → Telnyx migration guide
- `b13ba5983e40052c4b8238aa39d47f3b2b2facbd` — phone/SID log masking
- `f311abe1cdc1316ba6c6cfb617b909f4ec95ad9d` — logging/webhook security fixes
- `df880480dab98bd74d7e394428a7f9433e4de1df` — additional Twilio logging hardening
- `68c2535b51f9ffd57574fb785b1434aedd4b3b1f` — clear-text / exception-exposure fixes
- `07506d612b6bfbad820cd9503a556c848863642a` — final Twilio → Telnyx migration/removal

DentSignal later moved telephony again and currently uses Azure Communication Services. This repo is only here to show the earlier Twilio work I mentioned.

I left out credentials, clinic/customer data, and unrelated DentSignal code.
