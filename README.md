# DentSignal — Twilio evidence

DentSignal is private, so I pulled out the parts of its earlier Twilio implementation that are relevant here.

This is not a fresh demo I built for an application. These are sanitized extracts from the actual DentSignal history: voice calls, TwiML/webhooks, number provisioning, status callbacks, SMS, and the later security/migration work.

### What's in here

- `evidence/twilio_voice_flow.py` — outbound Voice calls, status callbacks, recording callback, AMD, TwiML speech flow, call-status lookup
- `evidence/twilio_number_provisioning.py` — buying numbers, configuring voice/SMS webhooks, updating them, releasing numbers
- `evidence/security_and_migration.md` — the commit trail for logging/security hardening and the move away from Twilio

### Original DentSignal history

The private repo has the original history. The main Twilio commits I pulled this from are:

- `6eb60ec15dcc286a5234c8e6de84174d280b8951` — automated Twilio number provisioning + webhook setup
- `27d321263f31c2fa027995baebc05d8b3ec4b351` — Twilio setup / after-hours call behavior
- `b13ba5983e40052c4b8238aa39d47f3b2b2facbd` — mask phone numbers and Twilio SIDs in logs
- `f311abe1cdc1316ba6c6cfb617b909f4ec95ad9d` — Twilio logging/webhook security fixes
- `df880480dab98bd74d7e394428a7f9433e4de1df` — additional Twilio logging hardening
- `68c2535b51f9ffd57574fb785b1434aedd4b3b1f` — more clear-text / exception exposure fixes
- `130de4c8fba6429e7cb815f1daf48b6bb7592e9b` — healthcare security work + Twilio → Telnyx migration guide
- `07506d612b6bfbad820cd9503a556c848863642a` — final Twilio → Telnyx migration/removal

DentSignal later moved telephony again and currently uses Azure Communication Services. This repo is only here to show the earlier Twilio work I mentioned.

The extracts are intentionally small. I kept out credentials, customer/clinic data, and unrelated product code.
