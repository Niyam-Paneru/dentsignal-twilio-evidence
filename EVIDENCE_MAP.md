# Evidence map

This repository is a **sanitized historical evidence pack**, not a current runtime or a standalone application.

The `evidence/` directory currently contains exactly the five published artifacts below. The Python files preserve historical control-flow and provider-facing responsibilities, but surrounding private dependency/client wiring and unrelated application code were intentionally removed. A file compiling successfully is therefore **not** evidence that the extract runs end to end by itself.

| Published artifact | What it proves | Boundary / what it does **not** prove |
|---|---|---|
| [`twilio_voice_flow.py`](evidence/twilio_voice_flow.py) | Earlier outbound call creation, TwiML speech collection, status/recording callbacks, answering-machine detection, and call-status lookup. | Does not prove the current provider, current routes/state machine, deployment state, or standalone execution without the omitted application wiring. |
| [`twilio_number_provisioning.py`](evidence/twilio_number_provisioning.py) | Earlier number discovery, purchase, voice/SMS webhook configuration, webhook repair, and release helpers. | Does not prove any number is currently owned/active, that Twilio is current, or that omitted client/configuration wiring is present here. |
| [`admin_number_routes.py`](evidence/admin_number_routes.py) | Historical FastAPI admin-route surface around provisioning operations. | Surrounding auth, clinic CRUD/persistence, and client injection were removed; this is not a standalone current admin API. |
| [`historical_setup_notes.md`](evidence/historical_setup_notes.md) | Setup/webhook assumptions and operational checks used during that earlier Twilio period. | Historical notes are not current provider guidance or a deployment checklist for today. |
| [`security_and_migration.md`](evidence/security_and_migration.md) | Dated hardening and provider-migration history, including public references to source commits in the private project. | Does not expose the private commits, prove every later architecture, or establish current runtime/provider state. |

## Provenance rule

Each public extract maps back to private DentSignal history. The public copy removes credentials, clinic/customer/patient data, environment-specific identifiers, and unrelated product code.

The goal is to show **real implementation history without reconstructing a fake modern demo or publishing the whole private system**.
