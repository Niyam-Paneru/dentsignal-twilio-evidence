# Security + migration trail

This is the part I think matters more than just "I called the Twilio SDK once."

The implementation went through provisioning, call/webhook handling, then several rounds of security cleanup before the provider was migrated.

| Date | Commit | What changed |
|---|---|---|
| 2026-01-09 | `6eb60ec15dcc286a5234c8e6de84174d280b8951` | Added automated Twilio number purchasing, voice/SMS webhook configuration, webhook repair, number audit and release endpoints. |
| 2026-01-09 | `27d321263f31c2fa027995baebc05d8b3ec4b351` | Simplified the Twilio setup path and clarified after-hours AI call behavior. |
| 2026-02-03 | `b13ba5983e40052c4b8238aa39d47f3b2b2facbd` | Masked phone numbers and Twilio SIDs in logs; reduced verbose webhook logging. |
| 2026-02-09 | `f311abe1cdc1316ba6c6cfb617b909f4ec95ad9d` | Removed clear-text phone/API-key logging and webhook URL debug logging. |
| 2026-02-09 | `df880480dab98bd74d7e394428a7f9433e4de1df` | Hardened Twilio service/telephony return values and error logging. |
| 2026-02-09 | `68c2535b51f9ffd57574fb785b1434aedd4b3b1f` | Another CodeQL pass: masked account SID/phone data and stopped returning raw exception details. |
| 2026-02-02 | `130de4c8fba6429e7cb815f1daf48b6bb7592e9b` | Healthcare security sprint included the Twilio → Telnyx migration guide. |
| 2026-03-07 | `07506d612b6bfbad820cd9503a556c848863642a` | Completed the Twilio → Telnyx migration/removal from the active code/docs. |

## What the original Twilio path handled

- outbound Voice calls
- call SIDs / status lookup
- lifecycle status callbacks
- call recording callback
- answering-machine detection
- TwiML speech collection
- inbound Voice webhook routing
- SMS webhook routing
- number search + purchase
- per-clinic webhook setup
- webhook repair for existing numbers
- number release
- security hardening around phone numbers, SIDs, webhook URLs and errors

The provider changed later, but the integration work above is from the real DentSignal history rather than a reconstructed sample.

> DentSignal has collaborative project history. The hashes above are included as project provenance; this public repo only contains the sanitized pieces relevant to the Twilio discussion.
