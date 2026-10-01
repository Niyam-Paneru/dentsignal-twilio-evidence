# Evidence map

This repository is a historical slice, not a current runtime.

| File | What it proves | What it does **not** prove |
|---|---|---|
| `twilio_voice_flow.py` | earlier outbound voice/TwiML/status-callback implementation | current production telephony provider |
| `twilio_number_provisioning.py` | search/purchase/configure/release flow around Twilio numbers | that any number is currently owned or active |
| `admin_number_routes.py` | FastAPI admin wrapper around provisioning operations | current admin UI or deployment state |
| `historical_setup_notes.md` | setup/webhook assumptions from that period | that the old checklist is still current |
| `security_and_migration.md` | hardening + later provider-migration context | that every later architecture is represented here |

## Provenance rule

Each public extract is mapped back to private DentSignal history. The public copy removes secrets, clinic/customer data, environment-specific identifiers, and unrelated product code.

The goal is to show **real implementation history without publishing the whole private system**.
