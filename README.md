# DentSignal — the old Twilio chapter

Welcome to the old Twilio wing of DentSignal. Please don't try to make a phone call from the museum.

This repo holds **sanitized code from an earlier implementation**: voice flows, TwiML, callbacks, and number management. I kept it public because “I built a receptionist” is a very easy sentence to type. Old code you can inspect is better evidence.

The current DentSignal application is private; these files aren't a deployable receptionist or proof of today's provider.

## What's on display

- [Voice flow](evidence/twilio_voice_flow.py): outbound call creation, speech gathering, status lookups, and callback wiring.
- [Number provisioning](evidence/twilio_number_provisioning.py): search/purchase/release helpers and webhook configuration.
- [Admin routes](evidence/admin_number_routes.py): the earlier FastAPI-facing number operations.
- [Setup notes](evidence/historical_setup_notes.md): assumptions from that implementation period.
- [Migration notes](evidence/security_and_migration.md): hardening and removal history.

The [evidence map](EVIDENCE_MAP.md) labels what each extract supports and what it doesn't. That's the best place to start rather than treating a filename as proof of an entire deployed system.

## A very short museum timeline

| When | What happened |
| --- | --- |
| January 9, 2026 | Earlier Twilio implementation |
| February 2–9, 2026 | Hardening and migration preparation |
| March 7, 2026 | Twilio removed from the active private code |

Those dates describe the older implementation, not what currently answers the phone.

## What the receipts can't prove

Credentials, real clinic data, private identifiers, complete dependencies, auth wiring, persistence, and unrelated application code. The extracts are **not standalone or deployable**, and they don't establish today's provider, current architecture, customer outcomes, or uptime. The files support specific historical implementation claims, not a claim that today's complete receptionist is deployed.

The included CircleCI configuration covers compilation/publication hygiene; its presence doesn't prove a current production voice service. Read [PROVENANCE.md](PROVENANCE.md) and [SECURITY.md](SECURITY.md) before drawing conclusions from the snippets.
